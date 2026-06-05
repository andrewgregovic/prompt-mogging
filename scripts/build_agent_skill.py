#!/usr/bin/env python3
"""Build an Agent Skills / Codex Skills package for Prompt Mogging."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

from validate_release import ROOT, read_text, validate


DIST_ROOT = ROOT / "dist" / "agent-skill" / "prompt-mogging"
REFERENCES = DIST_ROOT / "references"


AGENT_SKILL_DESCRIPTION = (
    "Constructive-adversarial interaction mode for sharper exploratory, "
    "strategic, diagnostic, and framing conversations."
)


def generated_skill_md(native_core: str) -> str:
    return f"""---
name: prompt-mogging
description: {AGENT_SKILL_DESCRIPTION}
---

# Prompt Mogging

Use this skill for exploratory, strategic, diagnostic, ideation, learning, research, model-building, and framing conversations where the user benefits from constructive challenge, hidden-assumption surfacing, confidence calibration, or sharper decision framing.

Do not use this skill for routine execution, extraction, formatting, mechanical conversion, simple rewriting under clear constraints, or closed-form lookup.

The activation core below is generated from the repository `NATIVE_CORE.md`. The full canonical specification is available in `references/FULL_SPEC.md`.

## Activation Core

{native_core.strip()}
"""


def run_validation_or_exit() -> None:
    errors, warnings, version = validate()
    for message in warnings:
        print(message, file=sys.stderr)
    if errors:
        for message in errors:
            print(message, file=sys.stderr)
        raise SystemExit(1)
    print(f"Release validation passed for {version}.")


def main() -> int:
    run_validation_or_exit()

    if DIST_ROOT.exists():
        shutil.rmtree(DIST_ROOT)
    REFERENCES.mkdir(parents=True, exist_ok=True)

    native_core = read_text(ROOT / "NATIVE_CORE.md")
    (DIST_ROOT / "SKILL.md").write_text(
        generated_skill_md(native_core),
        encoding="utf-8",
        newline="\n",
    )

    copies = {
        "SKILL.md": REFERENCES / "FULL_SPEC.md",
        "NATIVE_CORE.md": REFERENCES / "NATIVE_CORE.md",
        "ACCEPTANCE_TESTS.md": REFERENCES / "ACCEPTANCE_TESTS.md",
        "CHANGELOG.md": REFERENCES / "CHANGELOG.md",
    }
    for source, target in copies.items():
        shutil.copyfile(ROOT / source, target)

    print(f"Built {DIST_ROOT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
