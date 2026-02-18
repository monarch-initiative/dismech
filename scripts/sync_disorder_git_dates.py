#!/usr/bin/env python3
"""Sync entry creation/updated dates from git history.

For each YAML file:
- creation_date := oldest commit timestamp touching the file
- updated_date := newest commit timestamp touching the file

Timestamps are written as ISO 8601 UTC strings with a trailing Z.
"""

from __future__ import annotations

import argparse
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap


def _normalize_iso_to_utc_z(iso_value: str) -> str:
    """Convert an ISO 8601 timestamp (with offset) to UTC Z format."""
    parsed = datetime.fromisoformat(iso_value)
    utc = parsed.astimezone(timezone.utc)
    return utc.replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _git_dates_for_file(path: Path) -> tuple[str, str] | None:
    """Return (creation_date, updated_date) from git log for a file."""
    cmd = ["git", "log", "--follow", "--format=%cI", "--", str(path)]
    proc = subprocess.run(cmd, check=False, capture_output=True, text=True)
    if proc.returncode != 0:
        return None

    lines = [line.strip() for line in proc.stdout.splitlines() if line.strip()]
    if not lines:
        return None

    updated_raw = lines[0]
    creation_raw = lines[-1]
    return (_normalize_iso_to_utc_z(creation_raw), _normalize_iso_to_utc_z(updated_raw))


def _iter_disorder_files(kb_dir: Path, include_history: bool) -> Iterable[Path]:
    for path in sorted(kb_dir.glob("*.yaml")):
        if not include_history and path.name.endswith(".history.yaml"):
            continue
        yield path


def _set_dates(data: CommentedMap, creation_date: str, updated_date: str) -> bool:
    """Insert/update creation_date and updated_date slots.

    Returns True if the map was modified.
    """
    changed = False

    current_creation = data.get("creation_date")
    current_updated = data.get("updated_date")

    if current_creation != creation_date:
        if "creation_date" in data:
            data["creation_date"] = creation_date
        else:
            if "name" in data:
                insert_at = list(data).index("name") + 1
            else:
                insert_at = 0
            data.insert(insert_at, "creation_date", creation_date)
        changed = True

    if current_updated != updated_date:
        if "updated_date" in data:
            data["updated_date"] = updated_date
        else:
            if "creation_date" in data:
                insert_at = list(data).index("creation_date") + 1
            elif "name" in data:
                insert_at = list(data).index("name") + 1
            else:
                insert_at = 0
            data.insert(insert_at, "updated_date", updated_date)
        changed = True

    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--kb-dir",
        default="kb/disorders",
        help="Directory containing YAML files (default: kb/disorders)",
    )
    parser.add_argument(
        "--include-history",
        action="store_true",
        help="Also process *.history.yaml files",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Compute and report changes without writing files",
    )
    parser.add_argument(
        "--missing-only",
        action="store_true",
        help="Only fill files with missing/null creation_date or updated_date",
    )
    args = parser.parse_args()

    kb_dir = Path(args.kb_dir)
    if not kb_dir.exists():
        print(f"ERROR: directory not found: {kb_dir}")
        return 1

    yaml = YAML(typ="rt")
    yaml.preserve_quotes = True
    yaml.width = 4096
    yaml.indent(mapping=2, sequence=2, offset=0)

    total = 0
    changed = 0
    skipped = 0

    for path in _iter_disorder_files(kb_dir, args.include_history):
        total += 1
        dates = _git_dates_for_file(path)
        if dates is None:
            skipped += 1
            print(f"SKIP (no git history): {path}")
            continue
        creation_date, updated_date = dates

        data = yaml.load(path.read_text())
        if not isinstance(data, CommentedMap):
            skipped += 1
            print(f"SKIP (unexpected YAML root): {path}")
            continue

        if args.missing_only:
            has_creation = data.get("creation_date") not in (None, "")
            has_updated = data.get("updated_date") not in (None, "")
            if has_creation and has_updated:
                continue

        file_changed = _set_dates(data, creation_date, updated_date)
        if not file_changed:
            continue

        changed += 1
        if args.dry_run:
            print(
                f"WOULD UPDATE: {path} creation_date={creation_date} updated_date={updated_date}")
            continue

        with path.open("w") as stream:
            yaml.dump(data, stream)
        print(
            f"UPDATED: {path} creation_date={creation_date} updated_date={updated_date}")

    mode = "DRY-RUN" if args.dry_run else "WRITE"
    print(f"{mode} SUMMARY: total={total} changed={changed} skipped={skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
