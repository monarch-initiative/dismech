#!/usr/bin/env python3
"""Package the dismech-curator browser extension into a distributable zip.

Writes ``dist/dismech-curator-<version>.zip`` with the extension's runtime files
at the archive root, so a user can unzip it and point Chrome/Edge "Load unpacked"
at the resulting folder (which contains ``manifest.json``). Dev-only files (the
test suite and the icon generator) are excluded.

The archive is deterministic — entries are sorted and stamped with a fixed
timestamp — so identical inputs produce a byte-identical zip (handy for release
reproducibility). Pure standard library; no third-party dependencies.

Usage:
    python3 scripts/package_extension.py
"""

from __future__ import annotations

import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXT = ROOT / "extension"
DIST = ROOT / "dist"

# Dev-only paths that should not ship in the installable extension.
EXCLUDE_DIRS = {"test"}
EXCLUDE_FILES = {"icons/gen_icons.py"}

# Fixed DOS epoch (1980-01-01) so the archive is reproducible across runs.
FIXED_TIMESTAMP = (1980, 1, 1, 0, 0, 0)


def _runtime_files():
    """Yield (absolute_path, relative_posix_path) for each file to include."""
    for path in sorted(EXT.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(EXT)
        if rel.parts and rel.parts[0] in EXCLUDE_DIRS:
            continue
        if rel.as_posix() in EXCLUDE_FILES:
            continue
        if path.name == ".DS_Store":
            continue
        yield path, rel.as_posix()


def main() -> None:
    manifest = json.loads((EXT / "manifest.json").read_text(encoding="utf-8"))
    version = manifest["version"]
    DIST.mkdir(exist_ok=True)
    out = DIST / f"dismech-curator-{version}.zip"
    out.unlink(missing_ok=True)

    count = 0
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for path, arcname in _runtime_files():
            info = zipfile.ZipInfo(arcname, date_time=FIXED_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16  # regular file, rw-r--r--
            zf.writestr(info, path.read_bytes())
            count += 1

    print(f"Wrote {out.relative_to(ROOT)} ({count} files, {out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
