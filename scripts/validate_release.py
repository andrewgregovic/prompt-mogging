#!/usr/bin/env python3
"""Validate Prompt Mogging v0.2.x release artifacts before packaging.

v0.2.x architecture:
  - DISPATCHER_STUB.md lives in the platform/custom-instructions box.
  - SKILL.md is the full semantic-rule runtime and carries the floor semantics.
  - NATIVE_CORE.md is retired; only a tombstone remains under deprecated/.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "DISPATCHER_STUB.md",
    "README.md",
    "ACCEPTANCE_TESTS.md",
    "TUTORIAL.md",
    "CHANGELOG.md",
    "PATCH_NOTES.md",
    "BUILD_MANIFEST.md",
]

# NATIVE_CORE is retired. It must NOT be an active root artifact; the tombstone
# lives under deprecated/ and must not be pasted as runtime instructions.
RETIRED_ROOT_FILES = ["NATIVE_CORE.md"]
TOMBSTONE = Path("deprecated") / "NATIVE_CORE.md"

VERSION_RE = re.compile(r"v\d+\.\d+\.\d+")

# Dispatcher stub body size gate. Convention: stub body only, excluding the
# trailing newline and excluding the markdown fences/header.
MAX_STUB_BODY_CHARS = 600


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def first_version(text: str) -> str | None:
    match = VERSION_RE.search(text)
    return match.group(0) if match else None


def has_any(text: str, patterns: list[str]) -> bool:
    return any(re.search(p, text, re.IGNORECASE | re.DOTALL) for p in patterns)


def fail(errors: list[str], message: str) -> None:
    errors.append(f"ERROR: {message}")


def warn(warnings: list[str], message: str) -> None:
    warnings.append(f"WARNING: {message}")


def stub_body(text: str) -> str | None:
    """Return the fenced stub body, normalized to LF, trailing newline stripped."""
    match = re.search(r"```md\s*\n(.*?)\n```", text, re.DOTALL)
    if not match:
        return None
    return match.group(1).replace("\r\n", "\n").rstrip("\n")


# Concepts that must be present in the full SKILL.md for a valid v0.2.x runtime.
SKILL_CONCEPTS: dict[str, list[str]] = {
    "dispatcher consult model": [r"dispatcher", r"silently consult"],
    "loaded definition includes intent-to-govern": [r"intend(?:ed|s)?\s+to\s+govern"],
    "fragments / review pastes are non-loading": [
        r"are\s+not\s+loading",
        r"do\s+\**not\**\s+constitute\s+loading",
    ],
    "floor not suppressible by mog off while loaded": [r"not\s+suppressible"],
    "Play ordinary-conversation guard": [r"ordinary\s+conversational"],
    "Play commitment split": [r"rigor\s+split"],
    "tag epistemics (best-effort, not causal proof)": [
        r"not\s+causal\s+proof",
        r"best-effort\s+attribution",
    ],
    "debug / diagnostic distinction": [r"\[pm-diagnostic\]"],
    "compact PM_PREF memory format": [r"PM_PREF"],
    "compact PM_REC recurrence format": [r"PM_REC"],
    "factuality hygiene + tic guard": [r"tic\s+guard"],
    "visible activation tags": [r"\[pm-[a-z*]+\]"],
}

# Floor-tier vocabulary that must NOT appear in the consult-only dispatcher stub.
STUB_FORBIDDEN_FLOOR_TERMS = [
    r"no-pill",
    r"not-yet",
    r"frame\s+check",
    r"reframe",
    r"confidence\s+calibration",
    r"factuality",
    r"play\s+mode",
]


def validate() -> tuple[list[str], list[str], str | None]:
    errors: list[str] = []
    warnings: list[str] = []

    files: dict[str, str] = {}
    for name in REQUIRED_FILES:
        path = ROOT / name
        if not path.is_file():
            fail(errors, f"Required file missing: {name}")
            continue
        files[name] = read_text(path)

    # NATIVE_CORE retirement checks.
    for name in RETIRED_ROOT_FILES:
        if (ROOT / name).is_file():
            fail(errors, f"Retired artifact present at root: {name} (move to deprecated/)")
    tombstone_path = ROOT / TOMBSTONE
    if not tombstone_path.is_file():
        fail(errors, f"Tombstone missing: {TOMBSTONE.as_posix()}")
    else:
        tombstone = read_text(tombstone_path)
        if not has_any(tombstone, [r"retired", r"tombstone"]):
            fail(errors, "deprecated/NATIVE_CORE.md does not mark itself retired/tombstoned")

    if errors:
        return errors, warnings, None

    # Version stamp consistency across required files.
    skill_version = first_version(files["SKILL.md"])
    if not skill_version:
        fail(errors, "SKILL.md does not contain a version string like v0.2.3")
        return errors, warnings, None

    for name, text in files.items():
        if skill_version not in text:
            fail(errors, f"{name} does not contain current version string {skill_version}")

    # Dispatcher stub: size gate, no-floor gate, stub-only honesty.
    stub = files["DISPATCHER_STUB.md"]
    body = stub_body(stub)
    if body is None:
        fail(errors, "DISPATCHER_STUB.md has no fenced ```md stub body")
    else:
        if len(body) >= MAX_STUB_BODY_CHARS:
            fail(
                errors,
                f"DISPATCHER_STUB.md body is {len(body)} chars; must be under {MAX_STUB_BODY_CHARS}",
            )
        for pattern in STUB_FORBIDDEN_FLOOR_TERMS:
            if re.search(pattern, body, re.IGNORECASE):
                fail(
                    errors,
                    f"DISPATCHER_STUB.md body contains floor content matching /{pattern}/ "
                    "(stub must be consult-only, no floor)",
                )
        if not has_any(body, [r"not\s+loaded"]):
            fail(errors, 'DISPATCHER_STUB.md does not define stub-only "not loaded" reporting')

    # SKILL.md concept coverage.
    skill = files["SKILL.md"]
    for concept, patterns in SKILL_CONCEPTS.items():
        if not has_any(skill, patterns):
            fail(errors, f"SKILL.md missing required concept: {concept}")

    # README must describe the new architecture, not the retired core.
    readme = files["README.md"]
    if not has_any(readme, [r"DISPATCHER_STUB"]):
        fail(errors, "README.md does not reference DISPATCHER_STUB.md")
    if not has_any(readme, [r"NATIVE_CORE.*(?:retired|tombstone)", r"retired.*NATIVE_CORE"]):
        warn(warnings, "README.md does not clearly mark NATIVE_CORE.md as retired")

    return errors, warnings, skill_version


def main() -> int:
    errors, warnings, version = validate()
    for message in warnings:
        print(message, file=sys.stderr)
    if errors:
        for message in errors:
            print(message, file=sys.stderr)
        return 1
    print(f"Release validation passed for {version}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
