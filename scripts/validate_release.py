#!/usr/bin/env python3
"""Validate Prompt Mogging release artifacts before packaging."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "NATIVE_CORE.md",
    "ACCEPTANCE_TESTS.md",
    "CHANGELOG.md",
    "README.md",
    "BUILD_MANIFEST.md",
]

VERSION_RE = re.compile(r"v\d+\.\d+\.\d+")
MAX_NATIVE_CORE_CHARS = 7000
WARN_NATIVE_CORE_CHARS = 6500


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def compact(text: str) -> str:
    return re.sub(r"\s+", " ", text).casefold()


def has_any(text: str, patterns: list[str]) -> bool:
    return any(re.search(pattern, text, re.IGNORECASE | re.DOTALL) for pattern in patterns)


def first_version(text: str) -> str | None:
    match = VERSION_RE.search(text)
    return match.group(0) if match else None


def fail(errors: list[str], message: str) -> None:
    errors.append(f"ERROR: {message}")


def warn(warnings: list[str], message: str) -> None:
    warnings.append(f"WARNING: {message}")


NATIVE_CORE_CONCEPTS: dict[str, list[str]] = {
    "adversarial but constructive default": [
        r"default[^.\n]*(?:adversarial[- ]but[- ]constructive|adversarial but constructive)",
        r"default stance[^.\n]*adversarial",
    ],
    "in-scope activation": [
        r"on by default[^.\n]*(?:exploratory|strategic|diagnostic|ideation|learning|research|framing)",
        r"in[- ]scope activation",
        r"opt[- ]out for in[- ]scope",
    ],
    "integrated posture/floor behaviors always active": [
        r"integrated posture/floor behaviors are active",
        r"always[- ]on integrated behaviors",
    ],
    "visible-delta rule": [r"visible[- ]delta rule"],
    "no manufactured challenge / fake-adversarial guard": [
        r"manufactured challenge",
        r"fake[- ]adversarial",
    ],
    "honest-null rule": [
        r"honest null",
        r"nothing to push on here",
    ],
    "Play mode opt-in": [
        r"play is off by default and explicit only",
        r"play mode[^.\n]*(?:explicit|opt[- ]in)",
    ],
    "skill off hard dormancy": [
        r"skill off[^.\n]*hard dormant",
        r"skill off[^.\n]*disables",
    ],
    "chill soft suppression": [r"chill[^.\n]*soft suppression"],
    "load-state honesty": [r"load[- ]state honesty"],
    "retrieved/RAG-gated load warning": [
        r"retrieved[^.\n]*rag[- ]gated",
        r"rag[^.\n]*not guaranteed",
        r"do not rely on rag",
    ],
}


SKILL_CONCEPTS: dict[str, list[str]] = {
    **NATIVE_CORE_CONCEPTS,
    "canonical/native two-artifact authority": [
        r"skill\.md[^.\n]*canonical full specification",
        r"native_core\.md[^.\n]*canonical always[- ]in[- ]context activation core",
    ],
}


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

    if errors:
        return errors, warnings, None

    skill_version = first_version(files["SKILL.md"])
    if not skill_version:
        fail(errors, "SKILL.md does not contain a version string like v0.1.4")
        return errors, warnings, None

    for name, text in files.items():
        version = first_version(text)
        if version != skill_version:
            fail(
                errors,
                f"{name} first version stamp is {version or 'missing'}, expected {skill_version}",
            )
        if skill_version not in text:
            fail(errors, f"{name} does not contain current version string {skill_version}")

    native_core = files["NATIVE_CORE.md"]
    native_chars = len(native_core)
    if native_chars >= MAX_NATIVE_CORE_CHARS:
        fail(
            errors,
            f"NATIVE_CORE.md is {native_chars} characters; must be under {MAX_NATIVE_CORE_CHARS}",
        )
    elif native_chars > WARN_NATIVE_CORE_CHARS:
        warn(
            warnings,
            f"NATIVE_CORE.md is {native_chars} characters; over {WARN_NATIVE_CORE_CHARS} warning threshold",
        )

    for concept, patterns in NATIVE_CORE_CONCEPTS.items():
        if not has_any(native_core, patterns):
            fail(errors, f"NATIVE_CORE.md missing required concept: {concept}")

    skill = files["SKILL.md"]
    for concept, patterns in SKILL_CONCEPTS.items():
        if not has_any(skill, patterns):
            fail(errors, f"SKILL.md missing required concept: {concept}")

    skill_flat = compact(skill)
    if re.search(
        r"(default active stance|active default|default stance)[^.\n]{0,120}balanced candor and collaboration",
        skill,
        re.IGNORECASE,
    ):
        fail(
            errors,
            'SKILL.md appears to restore old active default "Balanced candor and collaboration"',
        )
    chill_hard_disable = False
    for line in skill.splitlines():
        line_flat = line.casefold()
        if "chill" not in line_flat:
            continue
        if "skill off" in line_flat or "drop the skill" in line_flat:
            continue
        if re.search(
            r"hard dormant|hard disable|disables prompt_mogging|disables the skill|turns? the skill off",
            line,
            re.IGNORECASE,
        ):
            chill_hard_disable = True
            break
    if chill_hard_disable:
        fail(errors, "SKILL.md appears to give chill hard-disable semantics")
    if "visible-delta rule" not in skill_flat:
        fail(errors, "SKILL.md missing visible-delta rule")

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
