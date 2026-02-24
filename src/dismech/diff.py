"""Semantic YAML diff tool.

Compares YAML files at the data level (post yaml.safe_load()),
ignoring serialization differences like key ordering, quoting, and wrapping.

Usage:
    # Compare two files
    uv run python -m dismech.diff files OLD.yaml NEW.yaml

    # Compare git refs (single file)
    uv run python -m dismech.diff git REF_OLD REF_NEW --file path/to/file.yaml

    # Compare git refs (directory, summary)
    uv run python -m dismech.diff git REF_OLD REF_NEW --dir kb/disorders --summary
"""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import asdict, dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Any

import yaml

KEY_CANDIDATES = ["name", "id", "reference", "hypothesis_group_id", "preferred_term"]


@dataclass
class DiffEntry:
    """A single difference between two YAML documents."""

    path: str
    change_type: str  # "added", "removed", "changed"
    old_value: Any = None
    new_value: Any = None


@dataclass
class FileDiffResult:
    """Diff results for a single file."""

    filename: str
    changes: list[DiffEntry] = field(default_factory=list)

    @property
    def has_changes(self) -> bool:
        return len(self.changes) > 0


def _normalize_value(v: Any) -> Any:
    """Normalize values for comparison.

    Handles yaml.safe_load quirks like datetime parsing.

    >>> _normalize_value(datetime(2025, 1, 15, 10, 30, 0))
    '2025-01-15T10:30:00'
    >>> _normalize_value(date(2025, 1, 15))
    '2025-01-15'
    >>> _normalize_value("  hello  ")
    'hello'
    >>> _normalize_value(42)
    42
    >>> _normalize_value(None) is None
    True
    """
    if isinstance(v, datetime):
        return v.isoformat()
    if isinstance(v, date):
        return v.isoformat()
    if isinstance(v, str):
        return v.strip()
    return v


def _find_key_field(items: list[dict]) -> str | None:
    """Auto-detect a key field that uniquely identifies list items.

    Checks KEY_CANDIDATES in order. Returns the first field that is
    present in every item and has unique values across all items.

    >>> _find_key_field([{"name": "a", "x": 1}, {"name": "b", "x": 2}])
    'name'
    >>> _find_key_field([{"name": "a"}, {"name": "a"}]) is None
    True
    >>> _find_key_field([{"x": 1}, {"x": 2}]) is None
    True
    >>> _find_key_field([]) is None
    True
    >>> _find_key_field([{"id": "x"}, {"name": "y"}]) is None
    True
    """
    if not items:
        return None
    for candidate in KEY_CANDIDATES:
        values = []
        all_present = True
        for item in items:
            if not isinstance(item, dict) or candidate not in item:
                all_present = False
                break
            values.append(item[candidate])
        if all_present and len(values) == len(set(str(v) for v in values)):
            return candidate
    return None


def diff_dicts(
    old: dict,
    new: dict,
    path: str = "",
    ignore_fields: set[str] | None = None,
) -> list[DiffEntry]:
    """Recursively compare two dicts, returning a list of differences.

    >>> diff_dicts({"a": 1}, {"a": 1})
    []
    >>> diff_dicts({"a": 1}, {"a": 2})
    [DiffEntry(path='a', change_type='changed', old_value=1, new_value=2)]
    >>> diff_dicts({}, {"b": 3})
    [DiffEntry(path='b', change_type='added', old_value=None, new_value=3)]
    >>> diff_dicts({"b": 3}, {})
    [DiffEntry(path='b', change_type='removed', old_value=3, new_value=None)]
    """
    ignore_fields = ignore_fields or set()
    entries: list[DiffEntry] = []
    all_keys = sorted(set(old.keys()) | set(new.keys()))

    for key in all_keys:
        if key in ignore_fields:
            continue
        full_path = f"{path}.{key}" if path else key
        if key not in old:
            entries.append(DiffEntry(full_path, "added", new_value=new[key]))
        elif key not in new:
            entries.append(DiffEntry(full_path, "removed", old_value=old[key]))
        else:
            entries.extend(_diff_values(old[key], new[key], full_path, ignore_fields))
    return entries


def diff_lists(
    old: list,
    new: list,
    path: str,
    ignore_fields: set[str] | None = None,
) -> list[DiffEntry]:
    """Compare two lists using keyed or positional matching.

    Keyed matching uses _find_key_field to match items by a unique key.
    Falls back to positional (index-based) comparison.

    >>> diff_lists([1, 2], [1, 2], "x")
    []
    >>> diff_lists([1], [1, 2], "x")
    [DiffEntry(path='x[1]', change_type='added', old_value=None, new_value=2)]
    """
    ignore_fields = ignore_fields or set()

    # Try keyed matching for lists of dicts
    all_items = [i for i in old + new if isinstance(i, dict)]
    if all_items and len(all_items) == len(old) + len(new):
        # All items are dicts - check combined list for key field
        key_field = (
            _find_key_field(old) if len(old) >= len(new) else _find_key_field(new)
        )
        # Verify the key field works across both lists combined
        if key_field:
            old_keys = [str(item.get(key_field)) for item in old]
            new_keys = [str(item.get(key_field)) for item in new]
            # Only use keyed matching if keys are unique within each list
            if len(old_keys) == len(set(old_keys)) and len(new_keys) == len(
                set(new_keys)
            ):
                return _diff_lists_keyed(old, new, path, key_field, ignore_fields)

    # Positional fallback
    return _diff_lists_positional(old, new, path, ignore_fields)


def _diff_lists_keyed(
    old: list[dict],
    new: list[dict],
    path: str,
    key_field: str,
    ignore_fields: set[str],
) -> list[DiffEntry]:
    """Compare lists of dicts matched by a key field."""
    entries: list[DiffEntry] = []
    old_map = {str(item[key_field]): item for item in old}
    new_map = {str(item[key_field]): item for item in new}

    old_key_set = set(old_map.keys())
    new_key_set = set(new_map.keys())

    for key in sorted(new_key_set - old_key_set):
        entries.append(
            DiffEntry(f"{path}[{key_field}={key}]", "added", new_value=new_map[key])
        )
    for key in sorted(old_key_set - new_key_set):
        entries.append(
            DiffEntry(f"{path}[{key_field}={key}]", "removed", old_value=old_map[key])
        )
    for key in sorted(old_key_set & new_key_set):
        entries.extend(
            diff_dicts(
                old_map[key],
                new_map[key],
                f"{path}[{key_field}={key}]",
                ignore_fields,
            )
        )
    return entries


def _diff_lists_positional(
    old: list,
    new: list,
    path: str,
    ignore_fields: set[str],
) -> list[DiffEntry]:
    """Compare lists by positional index."""
    entries: list[DiffEntry] = []
    max_len = max(len(old), len(new))
    for i in range(max_len):
        item_path = f"{path}[{i}]"
        if i >= len(old):
            entries.append(DiffEntry(item_path, "added", new_value=new[i]))
        elif i >= len(new):
            entries.append(DiffEntry(item_path, "removed", old_value=old[i]))
        else:
            entries.extend(_diff_values(old[i], new[i], item_path, ignore_fields))
    return entries


def _diff_values(
    old: Any,
    new: Any,
    path: str,
    ignore_fields: set[str],
) -> list[DiffEntry]:
    """Compare two arbitrary values, dispatching to the right comparator."""
    old_n = _normalize_value(old)
    new_n = _normalize_value(new)

    if isinstance(old_n, dict) and isinstance(new_n, dict):
        return diff_dicts(old_n, new_n, path, ignore_fields)
    if isinstance(old_n, list) and isinstance(new_n, list):
        return diff_lists(old_n, new_n, path, ignore_fields)
    if old_n != new_n:
        return [DiffEntry(path, "changed", old_value=old_n, new_value=new_n)]
    return []


# --- Git integration ---


def load_yaml_from_git(ref: str, filepath: str) -> dict | None:
    """Load a YAML file from a git ref via `git show`."""
    result = subprocess.run(
        ["git", "show", f"{ref}:{filepath}"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None
    return yaml.safe_load(result.stdout)


def _git_changed_files(
    old_ref: str, new_ref: str, directory: str | None = None
) -> list[str]:
    """List YAML files changed between two git refs."""
    cmd = ["git", "diff", "--name-only", old_ref, new_ref]
    if directory:
        cmd.append("--")
        cmd.append(directory)
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        return []
    return [f for f in result.stdout.strip().split("\n") if f and f.endswith(".yaml")]


def _git_list_files(ref: str, directory: str) -> list[str]:
    """List all YAML files at a given ref in a directory."""
    result = subprocess.run(
        ["git", "ls-tree", "--name-only", ref, directory + "/"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return []
    return [f for f in result.stdout.strip().split("\n") if f and f.endswith(".yaml")]


def diff_git_refs(
    old_ref: str,
    new_ref: str,
    filepath: str | None = None,
    directory: str | None = None,
    ignore_fields: set[str] | None = None,
) -> list[FileDiffResult]:
    """Compare YAML files between two git refs.

    If filepath is given, compare that single file.
    If directory is given, find all changed YAML files in that directory.
    """
    ignore_fields = ignore_fields or set()

    if filepath:
        files = [filepath]
    elif directory:
        # Get files that exist in either ref, then check changed ones
        files = _git_changed_files(old_ref, new_ref, directory)
        # Also check for files that only exist in one ref
        old_files = set(_git_list_files(old_ref, directory))
        new_files = set(_git_list_files(new_ref, directory))
        added_files = new_files - old_files
        removed_files = old_files - new_files
        # Merge: changed + added + removed (deduplicated)
        files = sorted(set(files) | added_files | removed_files)
    else:
        files = _git_changed_files(old_ref, new_ref)

    results = []
    for f in files:
        old_data = load_yaml_from_git(old_ref, f)
        new_data = load_yaml_from_git(new_ref, f)
        changes: list[DiffEntry] = []

        if old_data is None and new_data is not None:
            changes.append(DiffEntry(f, "added", new_value="<new file>"))
        elif old_data is not None and new_data is None:
            changes.append(DiffEntry(f, "removed", old_value="<deleted file>"))
        elif old_data is not None and new_data is not None:
            changes = diff_dicts(old_data, new_data, ignore_fields=ignore_fields)

        results.append(FileDiffResult(filename=f, changes=changes))
    return results


# --- Formatting ---


def _truncate(v: Any, maxlen: int = 60) -> str:
    """Truncate a value for display."""
    s = str(v)
    if len(s) > maxlen:
        return s[: maxlen - 3] + "..."
    return s


def _summarize_value(v: Any) -> str:
    """Produce a compact summary of a value."""
    if isinstance(v, list):
        return f"{len(v)} items"
    if isinstance(v, dict):
        keys = list(v.keys())
        if len(keys) <= 3:
            return "{" + ", ".join(f"{k}: ..." for k in keys) + "}"
        return f"dict with {len(keys)} keys"
    return _truncate(repr(v))


def format_text(results: list[FileDiffResult], summary: bool = False) -> str:
    """Format diff results as human-readable text."""
    lines: list[str] = []
    files_with_changes = 0

    for r in results:
        if not r.has_changes:
            continue
        files_with_changes += 1
        lines.append(f"=== {r.filename} ({len(r.changes)} changes) ===")
        if not summary:
            for c in r.changes:
                tag = f"[{c.change_type}]"
                path = c.path
                if c.change_type == "added":
                    detail = _summarize_value(c.new_value)
                    lines.append(f"  {tag:<12} {path:<45} {detail}")
                elif c.change_type == "removed":
                    detail = _summarize_value(c.old_value)
                    lines.append(f"  {tag:<12} {path:<45} {detail}")
                else:
                    old_s = _truncate(repr(c.old_value), 30)
                    new_s = _truncate(repr(c.new_value), 30)
                    lines.append(f"  {tag:<12} {path:<45} {old_s} -> {new_s}")
        lines.append("")

    total = len(results)
    lines.append(f"{total} files compared, {files_with_changes} with differences")
    return "\n".join(lines)


def format_json(results: list[FileDiffResult]) -> str:
    """Format diff results as JSON."""
    data = []
    for r in results:
        if not r.has_changes:
            continue
        data.append(
            {
                "filename": r.filename,
                "change_count": len(r.changes),
                "changes": [asdict(c) for c in r.changes],
            }
        )
    return json.dumps(data, indent=2, default=str)


# --- CLI ---


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Semantic YAML diff tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # files subcommand
    files_parser = subparsers.add_parser("files", help="Compare two YAML files")
    files_parser.add_argument("old_file", help="Old YAML file path")
    files_parser.add_argument("new_file", help="New YAML file path")
    files_parser.add_argument(
        "--ignore-fields", default="", help="Comma-separated fields to ignore"
    )
    files_parser.add_argument(
        "--format", choices=["text", "json"], default="text", dest="output_format"
    )

    # git subcommand
    git_parser = subparsers.add_parser("git", help="Compare YAML between git refs")
    git_parser.add_argument("old_ref", help="Old git ref (branch, tag, commit)")
    git_parser.add_argument("new_ref", help="New git ref")
    git_parser.add_argument("--file", help="Single file to compare")
    git_parser.add_argument("--dir", help="Directory of YAML files to compare")
    git_parser.add_argument(
        "--summary", action="store_true", help="Show only filenames and change counts"
    )
    git_parser.add_argument(
        "--ignore-fields", default="", help="Comma-separated fields to ignore"
    )
    git_parser.add_argument(
        "--format", choices=["text", "json"], default="text", dest="output_format"
    )

    args = parser.parse_args()
    ignore = {f.strip() for f in args.ignore_fields.split(",") if f.strip()}

    if args.command == "files":
        old_data = yaml.safe_load(Path(args.old_file).read_text())
        new_data = yaml.safe_load(Path(args.new_file).read_text())
        changes = diff_dicts(old_data, new_data, ignore_fields=ignore)
        result = FileDiffResult(
            filename=f"{args.old_file} -> {args.new_file}", changes=changes
        )
        results = [result]

    elif args.command == "git":
        if not args.file and not args.dir:
            print("Error: --file or --dir required for git mode", file=sys.stderr)
            sys.exit(1)
        results = diff_git_refs(
            args.old_ref,
            args.new_ref,
            filepath=args.file,
            directory=args.dir,
            ignore_fields=ignore,
        )

    if args.output_format == "json":
        print(format_json(results))
    else:
        summary = getattr(args, "summary", False)
        print(format_text(results, summary=summary))


if __name__ == "__main__":
    main()
