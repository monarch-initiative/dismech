#!/usr/bin/env python3
"""
Tag top-level PublicationReference entries in disorder YAML files.

For each disorder file the script:
1. Collects every PMID cited anywhere in the file (evidence items *and*
   top-level references).
2. Detects which PMIDs are GeneReviews articles by inspecting the local
   references_cache (looks for "GeneReviews" in the cached abstract body).
3. For each GeneReviews PMID:
   - If the PMID already appears in the top-level `references` list, ensures it
     has `tags:\n  - GeneReviews` immediately after its `reference:` / `title:`
     line.
   - If the PMID is only used in evidence items (not in top-level `references`),
     prepends a minimal PublicationReference entry with `tags: [GeneReviews]`
     and the title from cache.

The script edits files using targeted text operations so that YAML formatting
(indentation style, block scalars, quotes) is completely preserved.

Usage
-----
    uv run python scripts/tag_references.py              # tag all disorders
    uv run python scripts/tag_references.py --dry-run    # preview changes
    uv run python scripts/tag_references.py kb/disorders/Noonan_Syndrome.yaml

Options
-------
  --dry-run         Print what would change without writing files.
  --cache-dir PATH  Path to references_cache/ (default: references_cache/).
  --disorders-dir PATH  Path to kb/disorders/ (default: kb/disorders/).
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

GENEREVIEW_MARKERS = ["GeneReviews", "genereview"]

REPO_ROOT = Path(__file__).parent.parent


# ---------------------------------------------------------------------------
# Cache helpers
# ---------------------------------------------------------------------------


def is_genereview_pmid(pmid_str: str, cache_dir: Path) -> bool:
    """Return True if the cached abstract for pmid_str is a GeneReviews article."""
    pmid_num = pmid_str.replace("PMID:", "").strip()
    cache_file = cache_dir / f"PMID_{pmid_num}.md"
    if not cache_file.exists():
        return False
    content = cache_file.read_text(encoding="utf-8")
    return any(marker in content for marker in GENEREVIEW_MARKERS)


def title_from_cache(pmid_str: str, cache_dir: Path) -> str | None:
    """Return the title field from the YAML frontmatter of a cached reference."""
    pmid_num = pmid_str.replace("PMID:", "").strip()
    cache_file = cache_dir / f"PMID_{pmid_num}.md"
    if not cache_file.exists():
        return None
    content = cache_file.read_text(encoding="utf-8")
    m = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
    if m:
        return m.group(1).strip().strip("\"'")
    return None


# ---------------------------------------------------------------------------
# Text-level YAML helpers
# ---------------------------------------------------------------------------


def collect_all_pmids_text(text: str) -> set[str]:
    """Return all PMID values cited anywhere in the file (not just top-level)."""
    return set(re.findall(r"PMID:\d+", text))


def find_references_section(lines: list[str]) -> tuple[int, int]:
    """
    Return (start_line_idx, end_line_idx) for the top-level `references:` section.

    start_line_idx is the line containing `references:`.
    end_line_idx is the exclusive end — the first line of the next top-level key
    (a line that starts with a non-space, non-list-item character and contains ':').
    Returns (-1, -1) if no `references:` key is found.
    """
    start = -1
    for i, line in enumerate(lines):
        if re.match(r"^references\s*:", line):
            start = i
        elif start != -1:
            # A new top-level key ends the section (but not list items or blank lines)
            if re.match(r"^[a-zA-Z_]", line):
                return start, i
    if start == -1:
        return -1, -1
    return start, len(lines)


def top_level_ref_ids(lines: list[str], sec_start: int, sec_end: int) -> dict[str, int]:
    """
    Return a dict mapping reference_id → line_index for each top-level entry
    in the references section.  Top-level entries start with `^- reference:`.
    """
    result: dict[str, int] = {}
    for i in range(sec_start + 1, sec_end):
        m = re.match(r"^- reference:\s*(\S+)", lines[i])
        if m:
            result[m.group(1)] = i
    return result


def entry_field_line(lines: list[str], entry_start: int, sec_end: int, field: str) -> int:
    """
    Within the entry beginning at entry_start, find the line index of `field:`.
    Returns -1 if not found before the entry ends.
    """
    for i in range(entry_start + 1, sec_end):
        line = lines[i]
        # A new top-level list item or a new section ends this entry
        if re.match(r"^- ", line) or re.match(r"^[a-zA-Z_]", line):
            break
        if re.match(rf"^\s+{re.escape(field)}\s*:", line):
            return i
    return -1


def next_entry_line(lines: list[str], entry_start: int, sec_end: int) -> int:
    """Return the line index of the next top-level list entry after entry_start."""
    for i in range(entry_start + 1, sec_end):
        if re.match(r"^- ", lines[i]):
            return i
    return sec_end


def has_tag_in_entry(lines: list[str], entry_start: int, sec_end: int, tag: str) -> bool:
    """Return True if the entry already contains `- GeneReviews` under a `tags:` key."""
    in_tags = False
    for i in range(entry_start, min(next_entry_line(lines, entry_start, sec_end), sec_end)):
        line = lines[i]
        if re.match(r"^\s+tags\s*:", line):
            in_tags = True
        elif in_tags:
            if re.match(r"^\s+- " + re.escape(tag), line):
                return True
            # Another field ends the tags list
            if re.match(r"^\s+\w", line) and not re.match(r"^\s+-", line):
                in_tags = False
    return False


# ---------------------------------------------------------------------------
# Core mutation helpers
# ---------------------------------------------------------------------------


def add_tag_to_existing_entry(
    lines: list[str],
    entry_start: int,
    sec_end: int,
    tag: str,
) -> list[str]:
    """
    Insert `  tags:\n  - {tag}\n` into an existing top-level reference entry.
    Inserts after `title:` if present, else after `reference:`.
    """
    insert_after = entry_field_line(lines, entry_start, sec_end, "title")
    if insert_after == -1:
        insert_after = entry_start  # fallback: after the `- reference:` line itself

    tag_lines = ["  tags:", f"  - {tag}"]
    new_lines = lines[: insert_after + 1] + tag_lines + lines[insert_after + 1 :]
    return new_lines


def prepend_new_reference_entry(
    lines: list[str],
    sec_start: int,
    pmid: str,
    title: str | None,
    tag: str,
) -> list[str]:
    """
    Prepend a new PublicationReference entry at the start of the references section.
    Handles both `references: []` (inline empty) and block-list forms.
    """
    ref_line = lines[sec_start]

    # Build the new entry block
    new_entry: list[str] = [f"- reference: {pmid}"]
    if title:
        # Yaml-safe: escape double quotes, use double-quote style for safety
        safe_title = title.replace("\\", "\\\\").replace('"', '\\"')
        new_entry.append(f'  title: "{safe_title}"')
    new_entry.append("  tags:")
    new_entry.append(f"  - {tag}")
    new_entry.append("  findings: []")

    if re.match(r"^references\s*:\s*\[\]\s*$", ref_line):
        # Replace `references: []` with block form + new entry
        return (
            lines[:sec_start]
            + ["references:"]
            + new_entry
            + lines[sec_start + 1 :]
        )
    else:
        # `references:` (block form) — insert after the `references:` line
        return lines[: sec_start + 1] + new_entry + lines[sec_start + 1 :]


# ---------------------------------------------------------------------------
# Per-file driver
# ---------------------------------------------------------------------------


def tag_disorder_file(
    path: Path,
    cache_dir: Path,
    dry_run: bool = False,
) -> dict:
    """
    Tag GeneReviews references in a single disorder YAML file.
    Returns a summary dict: {added: int, tagged: int, already_ok: int}.
    """
    text = path.read_text(encoding="utf-8")
    all_pmids = collect_all_pmids_text(text)
    gr_pmids = {p for p in all_pmids if is_genereview_pmid(p, cache_dir)}

    if not gr_pmids:
        return {"added": 0, "tagged": 0, "already_ok": 0}

    lines = text.splitlines()
    sec_start, sec_end = find_references_section(lines)

    added = 0
    tagged = 0
    already_ok = 0

    for gr_pmid in sorted(gr_pmids):
        tag = "GeneReviews"
        # Re-compute section bounds each iteration (lines may have grown)
        sec_start, sec_end = find_references_section(lines)
        existing = top_level_ref_ids(lines, sec_start, sec_end)

        if gr_pmid in existing:
            entry_start = existing[gr_pmid]
            if has_tag_in_entry(lines, entry_start, sec_end, tag):
                already_ok += 1
            else:
                if not dry_run:
                    lines = add_tag_to_existing_entry(lines, entry_start, sec_end, tag)
                tagged += 1
        else:
            # Add a new minimal entry
            pmid_title = title_from_cache(gr_pmid, cache_dir)
            if not dry_run:
                # Ensure references section exists
                if sec_start == -1:
                    lines.append("references:")
                    sec_start = len(lines) - 1
                    sec_end = len(lines)
                lines = prepend_new_reference_entry(lines, sec_start, gr_pmid, pmid_title, tag)
            added += 1

    if not dry_run and (added > 0 or tagged > 0):
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    return {"added": added, "tagged": tagged, "already_ok": already_ok}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "files",
        nargs="*",
        type=Path,
        help="Disorder YAML files to process (default: all in kb/disorders/)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would change without writing files",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=REPO_ROOT / "references_cache",
        help="Path to references_cache/ directory",
    )
    parser.add_argument(
        "--disorders-dir",
        type=Path,
        default=REPO_ROOT / "kb" / "disorders",
        help="Path to kb/disorders/ directory",
    )
    args = parser.parse_args()

    files = args.files if args.files else sorted(args.disorders_dir.glob("*.yaml"))

    total_added = 0
    total_tagged = 0
    total_already_ok = 0
    files_modified: list[str] = []
    files_with_gr: list[str] = []

    for path in files:
        result = tag_disorder_file(path, args.cache_dir, dry_run=args.dry_run)
        n = result["added"] + result["tagged"] + result["already_ok"]
        if n:
            files_with_gr.append(path.name)
        if result["added"] or result["tagged"]:
            files_modified.append(path.name)
        total_added += result["added"]
        total_tagged += result["tagged"]
        total_already_ok += result["already_ok"]

    action = "Would tag" if args.dry_run else "Tagged"
    print(f"\n{action} GeneReviews references:")
    print(f"  Disorders with GeneReviews citations : {len(files_with_gr)}")
    print(f"  New top-level entries added          : {total_added}")
    print(f"  Existing entries tagged              : {total_tagged}")
    print(f"  Already correctly tagged             : {total_already_ok}")
    if files_modified:
        print(f"\nModified files ({len(files_modified)}):")
        for f in files_modified:
            print(f"  {f}")
    else:
        print("\nNo files needed modification.")

    if files_with_gr:
        print(f"\nDisorders with ≥1 GeneReviews citation ({len(files_with_gr)}):")
        for f in sorted(files_with_gr):
            print(f"  {f}")


if __name__ == "__main__":
    main()
