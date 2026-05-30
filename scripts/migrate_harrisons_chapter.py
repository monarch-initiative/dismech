"""Migrate legacy free-text `harrisons_chapter` values to HarrisonsChapterEnum keys.

Reads the alias mappings out of `src/dismech/schema/dismech.yaml` and rewrites
each `classification_value:` line under a `harrisons_chapter:` block to use the
canonical enum key. Unmapped values are reported and left untouched so a human
can decide.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
SCHEMA = REPO / "src" / "dismech" / "schema" / "dismech.yaml"
DISORDERS = REPO / "kb" / "disorders"


def load_alias_map() -> dict[str, str]:
    with SCHEMA.open() as f:
        data = yaml.safe_load(f)
    pvs = data["enums"]["HarrisonsChapterEnum"]["permissible_values"]
    mapping: dict[str, str] = {}
    for key, body in pvs.items():
        mapping[key] = key
        for alias in (body or {}).get("aliases") or []:
            mapping[alias] = key
    return mapping


HARRISONS_BLOCK_RE = re.compile(r"^(\s*)harrisons_chapter:\s*$")
CLASSIFICATION_LINE_RE = re.compile(
    r"^(?P<indent>\s*)(?P<dash>-?\s*)classification_value:\s*(?P<value>.+?)\s*$"
)


def rewrite_file(path: Path, alias_map: dict[str, str]) -> tuple[int, list[str]]:
    lines = path.read_text().splitlines(keepends=False)
    out: list[str] = []
    in_block = False
    block_indent = ""
    seen_in_block: set[str] = set()
    dropping_item = False  # we are inside the body of a dropped duplicate item
    item_body_indent = 0
    changes = 0
    unmapped: list[str] = []

    for line in lines:
        match = HARRISONS_BLOCK_RE.match(line)
        if match:
            in_block = True
            block_indent = match.group(1)
            seen_in_block = set()
            dropping_item = False
            out.append(line)
            continue

        if in_block:
            stripped_indent = len(line) - len(line.lstrip(" "))
            stripped = line.lstrip(" ")
            # Exit only on a sibling key at the parent indent (not a sequence item).
            if line.strip() and stripped_indent <= len(block_indent) and not stripped.startswith("-"):
                in_block = False
                seen_in_block = set()
                dropping_item = False
                out.append(line)
                continue

            # If we're discarding a duplicate classification entry, drop its
            # body lines too (anything indented deeper than the item indent
            # itself). Stop dropping when we hit the next list item or the end
            # of the block.
            if dropping_item:
                if not line.strip():
                    # Blank line — drop it along with the item body.
                    continue
                if stripped_indent > item_body_indent:
                    continue
                dropping_item = False  # fall through to normal handling

            cm = CLASSIFICATION_LINE_RE.match(line)
            if cm:
                value = cm.group("value").strip().strip('"').strip("'")
                if value in alias_map:
                    new_value = alias_map[value]
                    if new_value in seen_in_block:
                        # Drop this entire item, including its body.
                        dropping_item = True
                        item_body_indent = len(cm.group("indent"))
                        changes += 1
                        continue
                    seen_in_block.add(new_value)
                    if new_value != value:
                        line = (
                            f"{cm.group('indent')}{cm.group('dash')}"
                            f"classification_value: {new_value}"
                        )
                        changes += 1
                else:
                    unmapped.append(value)
                out.append(line)
                continue
        out.append(line)

    if changes:
        path.write_text("\n".join(out) + "\n")
    return changes, unmapped


def main() -> int:
    alias_map = load_alias_map()
    total_changes = 0
    files_touched = 0
    all_unmapped: dict[str, list[str]] = {}
    for path in sorted(DISORDERS.glob("*.yaml")):
        changes, unmapped = rewrite_file(path, alias_map)
        if changes:
            files_touched += 1
            total_changes += changes
        if unmapped:
            all_unmapped[path.name] = unmapped
    print(f"Rewrote {total_changes} classification_value lines across {files_touched} files")
    if all_unmapped:
        print("\nUnmapped values (left untouched):")
        for fname, vals in all_unmapped.items():
            print(f"  {fname}: {vals}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
