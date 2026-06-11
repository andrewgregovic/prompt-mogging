#!/usr/bin/env python3
"""Build the Prompt Mogging v0.2.x release: validate, rebuild dist, manifest, zip.

Single entrypoint for a release build:
  1. Validate release artifacts (scripts/validate_release.py rules).
  2. Regenerate the dist/ agent-skill package from root source files.
  3. Regenerate BUILD_MANIFEST.md (char counts, SHA-256, version stamps).
  4. Write the release zip.

Char counts in the manifest are Unicode code-point counts (Python ``len``).
SHA-256 is computed over the on-disk file bytes.
"""

from __future__ import annotations

import hashlib
import os
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

import build_agent_skill
from validate_release import ROOT, first_version, read_text, validate


RELEASE_TITLE = "Dispatcher / Semantic Rule Runtime"
MANIFEST_NAME = "BUILD_MANIFEST.md"
ZIP_EPOCH = (1980, 1, 1, 0, 0, 0)

# Root artifacts shipped in the release zip and listed in the manifest.
ROOT_PACKAGE_FILES = [
    "README.md",
    "DISPATCHER_STUB.md",
    "SKILL.md",
    "deprecated/NATIVE_CORE.md",
    "ACCEPTANCE_TESTS.md",
    "TUTORIAL.md",
    "CHANGELOG.md",
    "PATCH_NOTES.md",
    "CLAUDE_REVIEW_PROMPT_v0_2_3.md",
]

# Generated dist artifacts also listed in the manifest.
DIST_FILES = [
    "dist/agent-skill/prompt-mogging/SKILL.md",
    "dist/agent-skill/prompt-mogging/references/FULL_SPEC.md",
    "dist/agent-skill/prompt-mogging/references/DISPATCHER_STUB.md",
    "dist/agent-skill/prompt-mogging/references/ACCEPTANCE_TESTS.md",
    "dist/agent-skill/prompt-mogging/references/CHANGELOG.md",
    "dist/agent-skill/prompt-mogging/references/NATIVE_CORE.md",
]

AUTHORITY_CHECKS = [
    "`DISPATCHER_STUB.md` is the platform/custom-instructions consult stub.",
    "`SKILL.md` is the canonical full runtime specification and contains floor semantics.",
    "`NATIVE_CORE.md` is retired/tombstoned and must not be used as active runtime instructions.",
    "Stub-only state is inert and reports `not loaded` for `mog status` / `mog help`.",
    "Fragments, quotes, diffs, review pastes, and discussion are not loading unless explicitly run.",
    "`TUTORIAL.md` illustrates behavior; `ACCEPTANCE_TESTS.md` adjudicates behavior.",
    "Dist package is regenerated from root source files.",
]

REVIEW_GATES = [
    "Dispatcher stub remains under 600 characters under the stated convention.",
    "Loaded definition includes intent-to-govern.",
    "Play ordinary-conversation guard is present.",
    "Play commitment split is present.",
    "Tag epistemics are present.",
    "Debug/diagnostic distinction is present.",
    "Compact PM_PREF / PM_REC memory discipline is present.",
    "No active `NATIVE_CORE` runtime instructions remain.",
]


def lf_bytes(path: Path) -> bytes:
    """File content as LF-normalized UTF-8 bytes.

    Hashing/packaging the LF form keeps the manifest and zip reproducible
    regardless of the checkout's autocrlf line-ending setting.
    """
    return read_text(path).encode("utf-8")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(lf_bytes(path)).hexdigest()


def build_timestamp() -> str:
    source_date_epoch = os.environ.get("SOURCE_DATE_EPOCH")
    if source_date_epoch:
        ts = datetime.fromtimestamp(int(source_date_epoch), tz=timezone.utc)
    else:
        ts = datetime.now(timezone.utc)
    return ts.replace(microsecond=0).isoformat().replace("+00:00", "Z")


def file_line(rel: str, version: str) -> str:
    path = ROOT / rel
    text = read_text(path)
    stamp = "YES" if version in text else "NO"
    digest = sha256_file(path)
    return f"- `{rel}` — {len(text)} chars — {version} stamp: {stamp} — SHA-256: `{digest}`"


def manifest_text(version: str) -> str:
    listed = [f for f in ROOT_PACKAGE_FILES if f != MANIFEST_NAME] + DIST_FILES
    files_block = "\n".join(file_line(rel, version) for rel in listed)
    authority = "\n".join(f"- {item}" for item in AUTHORITY_CHECKS)
    gates = "\n".join(f"- {item}" for item in REVIEW_GATES)
    return f"""# Prompt Mogging {version} — Build Manifest

**Build timestamp (UTC):** {build_timestamp()}
**Release:** {version} — {RELEASE_TITLE}

## Files

{files_block}

## Authority and sync checks

{authority}

## Candidate review gates

{gates}
"""


def write_zip(version: str) -> Path:
    safe_version = version.replace(".", "_")
    zip_path = ROOT / f"Prompt_Mogging_{safe_version}_Release_Pack.zip"
    if zip_path.exists():
        zip_path.unlink()

    members = [f for f in ROOT_PACKAGE_FILES] + [MANIFEST_NAME]
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for rel in members:
            info = zipfile.ZipInfo(filename=rel, date_time=ZIP_EPOCH)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, lf_bytes(ROOT / rel))
    return zip_path


def run_validation_or_exit() -> str:
    errors, warnings, version = validate()
    for message in warnings:
        print(message, file=sys.stderr)
    if errors:
        for message in errors:
            print(message, file=sys.stderr)
        raise SystemExit(1)
    assert version is not None
    return version


def main() -> int:
    # 1. Validate, 2. rebuild dist from root sources.
    version = run_validation_or_exit()
    build_agent_skill.main()

    # 3. Regenerate the manifest (after dist exists so dist rows are current).
    (ROOT / MANIFEST_NAME).write_text(manifest_text(version), encoding="utf-8", newline="\n")

    # 4. Re-validate post-write, then zip.
    run_validation_or_exit()
    zip_path = write_zip(version)
    print(f"Built {zip_path.name} for {version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
