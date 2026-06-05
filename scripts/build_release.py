#!/usr/bin/env python3
"""Build the Prompt Mogging release manifest and zip package."""

from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

from validate_release import ROOT, read_text, validate


PACKAGE_FILES = [
    "SKILL.md",
    "NATIVE_CORE.md",
    "ACCEPTANCE_TESTS.md",
    "CHANGELOG.md",
    "PATCH_NOTES.md",
    "README.md",
    "BUILD_MANIFEST.md",
]

MANIFEST_NAME = "BUILD_MANIFEST.md"
ZIP_EPOCH = (1980, 1, 1, 0, 0, 0)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_timestamp() -> str:
    source_date_epoch = os.environ.get("SOURCE_DATE_EPOCH")
    if source_date_epoch:
        timestamp = datetime.fromtimestamp(int(source_date_epoch), tz=timezone.utc)
    else:
        timestamp = datetime.now(timezone.utc)
    return timestamp.replace(microsecond=0).isoformat().replace("+00:00", "Z")


def file_row(name: str, version: str) -> str:
    path = ROOT / name
    text = read_text(path)
    version_stamp = "YES" if version in text else "NO"
    digest = sha256_file(path)
    return f"| `{name}` | {len(text)} | `{digest}` | {version_stamp} |"


def manifest_text(version: str) -> str:
    rows = [file_row(name, version) for name in PACKAGE_FILES if name != MANIFEST_NAME]
    file_list = "\n".join(f"- `{name}`" for name in PACKAGE_FILES)
    table = "\n".join(rows)
    return f"""# Prompt Mogging {version} Build Manifest

Build timestamp: {build_timestamp()}

## Package Files

{file_list}

## Character Counts and SHA-256 Hashes

| File | Characters | SHA-256 | {version} stamp |
|---|---:|---|---|
{table}

## Manifest Note

`BUILD_MANIFEST.md` is included in the release zip. Its own hash is omitted from the table because embedding a file's cryptographic hash inside itself is self-referential.

## Release Gate

Validation must pass before packaging. The package is valid only when `SKILL.md`, `NATIVE_CORE.md`, `ACCEPTANCE_TESTS.md`, `CHANGELOG.md`, `README.md`, and this manifest share the same current version stamp.
"""


def write_manifest(version: str) -> None:
    (ROOT / MANIFEST_NAME).write_text(manifest_text(version), encoding="utf-8", newline="\n")


def write_zip(version: str) -> Path:
    zip_path = ROOT / f"Prompt_Mogging_{version}_Release_Pack.zip"
    if zip_path.exists():
        zip_path.unlink()

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in PACKAGE_FILES:
            path = ROOT / name
            info = zipfile.ZipInfo(filename=name, date_time=ZIP_EPOCH)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())
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
    version = run_validation_or_exit()
    write_manifest(version)

    # Re-run through the script entry point so local output matches CI behavior.
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_release.py")],
        cwd=ROOT,
        check=True,
    )

    zip_path = write_zip(version)
    print(f"Built {zip_path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
