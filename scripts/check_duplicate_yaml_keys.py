#!/usr/bin/env python3
"""Guard against duplicated mapping keys in KB YAML.

A YAML mapping may not repeat a key. PyYAML's safe loaders -- what
``dismech.yaml_io.safe_load`` and therefore nearly all of this codebase uses --
accept a repeated key anyway and silently keep the *last* value. The
ruamel-backed ``linkml-reference-validator`` does not: it raises
``DuplicateKeyError`` and aborts. So a duplicate is simultaneously invisible to
every test and renderer here, and fatal to the validator CI runs.

Why this needs a whole-KB sweep
-------------------------------
Duplicates arrive by *merge*, not by authoring. Two concurrent curation PRs each
adding a ``classifications:`` block at a different point in the same file merge
without a git conflict, and the result is a document no strict parser will read.
Each PR is green on its own base; main goes red on the push build afterwards.

That is issue #8623: PRs #8592 and #8580 both added ``classifications:`` to
``Atopic_Dermatitis.yaml``. The same collision had already happened to
``Ulcerative_Colitis.yaml`` and sat unnoticed, because the reference validator
only ever sees the files a PR *changed*.

The existing whole-KB sweep (``just test-kb``) cannot cover this: it is gated on
schema changes, on the reasoning that only a schema edit can flip a KB file's
validity. A merge-born duplicate flips validity with no schema edit at all.

Usage
-----
    python scripts/check_duplicate_yaml_keys.py           # gate: fail on any finding
    python scripts/check_duplicate_yaml_keys.py kb/disorders/Asthma.yaml
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dismech.yaml_io import find_duplicate_keys

# Curated KB content. ``history`` is excluded for the same reason the folded-hyphen
# guard excludes it: those records are append-only, so a finding there cannot be
# fixed in place.
DEFAULT_ROOTS = ("kb",)


def iter_yaml_files(paths: list[str]) -> list[Path]:
    """Expand explicit paths, or the default KB roots when none are given."""
    if paths:
        return [Path(p) for p in paths]
    files: list[Path] = []
    for root in DEFAULT_ROOTS:
        files.extend(sorted((ROOT / root).rglob("*.yaml")))
    return files


def _display(path: Path) -> str:
    """Repo-relative path when the file is inside the repo, else the path as given."""
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        help="YAML files to check (default: every file under kb/)",
    )
    args = parser.parse_args()

    files = iter_yaml_files(args.paths)
    findings: list[tuple[Path, str, str, int]] = []
    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:  # pragma: no cover - unreadable file
            print(f"{path}: could not read ({exc})", file=sys.stderr)
            return 1
        for location, key, line in find_duplicate_keys(text):
            findings.append((path, location, key, line))

    if findings:
        print("Duplicate mapping key(s) detected in KB YAML.\n")
        print("A YAML mapping cannot repeat a key. PyYAML keeps the last value")
        print("silently, but the ruamel-based reference validator rejects the")
        print("file outright, so this turns CI red on every later run that")
        print("touches it. Merge the duplicated blocks into one.\n")
        for path, location, key, line in findings:
            print(f"{_display(path)}:{line}: duplicate key '{key}' in {location}")
        print(f"\n{len(findings)} duplicate key(s) across {len(files)} file(s).")
        return 1

    print(f"OK: no duplicate mapping keys in {len(files)} YAML file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
