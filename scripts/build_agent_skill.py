#!/usr/bin/env python3
"""Build the Agent Skills / Codex Skills package for Prompt Mogging v0.2.x.

The dist package is a thin wrapper that points hosts at the full repository
artifacts:

  dist/agent-skill/prompt-mogging/
    SKILL.md                     generated wrapper (frontmatter + pointers)
    references/
      FULL_SPEC.md               copy of root SKILL.md (the real runtime)
      DISPATCHER_STUB.md         copy of root DISPATCHER_STUB.md
      ACCEPTANCE_TESTS.md        copy of root ACCEPTANCE_TESTS.md
      CHANGELOG.md               copy of root CHANGELOG.md
      NATIVE_CORE.md             copy of the deprecated/ tombstone

Floor semantics live in the full skill, not in this wrapper or the stub.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

from validate_release import ROOT, first_version, read_text, validate


DIST_ROOT = ROOT / "dist" / "agent-skill" / "prompt-mogging"
REFERENCES = DIST_ROOT / "references"

AGENT_SKILL_DESCRIPTION = (
    "Chat-native semantic rule runtime for exploratory, strategic, diagnostic, "
    "ideation, learning, research, model-building, and framing conversations "
    "where the user benefits from constructive challenge, confidence calibration, "
    "or sharper decision framing."
)

# Root source -> dist reference target. The wrapper SKILL.md is generated.
REFERENCE_COPIES = {
    "SKILL.md": "FULL_SPEC.md",
    "DISPATCHER_STUB.md": "DISPATCHER_STUB.md",
    "ACCEPTANCE_TESTS.md": "ACCEPTANCE_TESTS.md",
    "CHANGELOG.md": "CHANGELOG.md",
}
# The retired core ships only as the deprecated/ tombstone.
TOMBSTONE_SOURCE = Path("deprecated") / "NATIVE_CORE.md"


def wrapper_skill_md(version: str) -> str:
    return f"""---
name: prompt-mogging
description: {AGENT_SKILL_DESCRIPTION}
---

# Prompt Mogging agent-skill wrapper {version}

Use this skill when the user is doing exploratory, strategic, diagnostic, ideation, learning, research, model-building, or framing work.

Do not use it for routine execution, extraction, formatting, simple rewriting under clear constraints, mechanical conversion, or closed-form lookup.

This dist package mirrors the repository release:

- Full canonical spec: `references/FULL_SPEC.md`
- Dispatcher stub for platform/custom instructions: `references/DISPATCHER_STUB.md`
- Acceptance tests: `references/ACCEPTANCE_TESTS.md`
- Changelog: `references/CHANGELOG.md`

## Runtime note

`NATIVE_CORE.md` is retired as of {version}. The full skill spec contains the floor semantics. The dispatcher stub is consult-only and contains no floor.

If this agent-skill package is loaded as a full skill by a host that reads this `SKILL.md`, apply the full runtime specification in `references/FULL_SPEC.md`.
"""


def run_validation_or_exit() -> str:
    errors, warnings, version = validate()
    for message in warnings:
        print(message, file=sys.stderr)
    if errors:
        for message in errors:
            print(message, file=sys.stderr)
        raise SystemExit(1)
    assert version is not None
    print(f"Release validation passed for {version}.")
    return version


def main() -> int:
    version = run_validation_or_exit()

    if DIST_ROOT.exists():
        shutil.rmtree(DIST_ROOT)
    REFERENCES.mkdir(parents=True, exist_ok=True)

    (DIST_ROOT / "SKILL.md").write_text(
        wrapper_skill_md(version),
        encoding="utf-8",
        newline="\n",
    )

    for source, target in REFERENCE_COPIES.items():
        text = read_text(ROOT / source)
        (REFERENCES / target).write_text(text, encoding="utf-8", newline="\n")

    tombstone = read_text(ROOT / TOMBSTONE_SOURCE)
    (REFERENCES / "NATIVE_CORE.md").write_text(tombstone, encoding="utf-8", newline="\n")

    print(f"Built {DIST_ROOT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
