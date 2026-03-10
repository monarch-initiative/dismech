#!/usr/bin/env python3
"""Add reference_title to EvidenceItem entries and restructure Dataset.publication.

This script:
1. Adds `reference_title` field to every EvidenceItem that has a `reference: PMID:xxx`
2. Restructures Dataset `publication: PMID:xxx` to nested PublicationReference format

Titles are looked up from the references_cache/ directory.
"""

import re
import sys
from pathlib import Path

CACHE_DIR = Path("references_cache")


def get_title_from_cache(pmid: str) -> str | None:
    """Look up a PMID title from the references cache."""
    # PMID:12345678 -> PMID_12345678.md
    cache_file = CACHE_DIR / f"PMID_{pmid}.md"
    if not cache_file.exists():
        return None

    content = cache_file.read_text()
    # Parse YAML frontmatter
    match = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', content, re.MULTILINE)
    if match:
        title = match.group(1).strip()
        # Handle quoted titles that may have trailing quote
        if title.endswith('"') or title.endswith("'"):
            title = title[:-1]
        return title

    # Try multi-line or complex title formats
    match = re.search(r'^title:\s*"(.+)"', content, re.MULTILINE)
    if match:
        return match.group(1).strip()

    return None


def yaml_quote(s: str) -> str:
    """Quote a string for YAML if it contains special characters."""
    # Always double-quote titles to avoid YAML parsing issues
    escaped = s.replace('\\', '\\\\').replace('"', '\\"')
    return f'"{escaped}"'


def add_reference_titles(content: str) -> tuple[str, int, int]:
    """Add reference_title after each reference: PMID:xxx line in evidence blocks.

    Returns (new_content, added_count, missing_count).
    """
    lines = content.split('\n')
    new_lines = []
    added = 0
    missing = 0
    i = 0

    while i < len(lines):
        line = lines[i]
        new_lines.append(line)

        # Match "    - reference: PMID:12345678" or "      reference: PMID:12345678"
        m = re.match(r'^(\s+)(-\s+)?reference:\s+PMID:(\d+)\s*$', line)
        if m:
            indent = m.group(1)
            is_list_start = m.group(2)  # "- " prefix if list item
            pmid = m.group(3)

            # Check if next line already has reference_title
            if i + 1 < len(lines) and 'reference_title:' in lines[i + 1]:
                i += 1
                continue

            title = get_title_from_cache(pmid)
            if title:
                # Calculate the indentation for reference_title
                if is_list_start:
                    # "    - reference:" -> reference_title needs "      " (indent + 2 spaces for "- ")
                    title_indent = indent + "  "
                else:
                    title_indent = indent

                new_lines.append(f"{title_indent}reference_title: {yaml_quote(title)}")
                added += 1
            else:
                missing += 1

        i += 1

    return '\n'.join(new_lines), added, missing


def restructure_publication(content: str) -> tuple[str, int, int]:
    """Restructure `publication: PMID:xxx` to nested PublicationReference.

    Before:
      publication: PMID:12345678

    After:
      publication:
        reference: PMID:12345678
        title: "Paper title here"

    Returns (new_content, restructured_count, missing_count).
    """
    lines = content.split('\n')
    new_lines = []
    restructured = 0
    missing = 0
    i = 0

    while i < len(lines):
        line = lines[i]

        # Match "  publication: PMID:12345678"
        m = re.match(r'^(\s+)publication:\s+PMID:(\d+)\s*$', line)
        if m:
            indent = m.group(1)
            pmid = m.group(2)
            title = get_title_from_cache(pmid)

            new_lines.append(f"{indent}publication:")
            new_lines.append(f"{indent}  reference: PMID:{pmid}")
            if title:
                new_lines.append(f"{indent}  title: {yaml_quote(title)}")
                restructured += 1
            else:
                missing += 1
                restructured += 1  # Still restructured, just no title
        else:
            new_lines.append(line)

        i += 1

    return '\n'.join(new_lines), restructured, missing


def process_file(filepath: Path, dry_run: bool = False) -> dict:
    """Process a single disorder YAML file."""
    content = filepath.read_text()
    original = content

    # Step 1: Add reference_title to evidence items
    content, ref_added, ref_missing = add_reference_titles(content)

    # Step 2: Restructure publication fields
    content, pub_restructured, pub_missing = restructure_publication(content)

    stats = {
        'file': str(filepath),
        'ref_titles_added': ref_added,
        'ref_titles_missing': ref_missing,
        'publications_restructured': pub_restructured,
        'pub_titles_missing': pub_missing,
        'changed': content != original,
    }

    if not dry_run and content != original:
        filepath.write_text(content)

    return stats


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Add PMID titles to disorder YAML files')
    parser.add_argument('files', nargs='*', help='Specific files to process (default: all kb/disorders/*.yaml)')
    parser.add_argument('--dry-run', action='store_true', help='Show what would change without modifying files')
    args = parser.parse_args()

    if args.files:
        files = [Path(f) for f in args.files]
    else:
        files = sorted(Path('kb/disorders').glob('*.yaml'))

    total_ref_added = 0
    total_ref_missing = 0
    total_pub_restructured = 0
    total_pub_missing = 0
    files_changed = 0

    for f in files:
        stats = process_file(f, dry_run=args.dry_run)
        total_ref_added += stats['ref_titles_added']
        total_ref_missing += stats['ref_titles_missing']
        total_pub_restructured += stats['publications_restructured']
        total_pub_missing += stats['pub_titles_missing']
        if stats['changed']:
            files_changed += 1
            if stats['ref_titles_added'] or stats['publications_restructured']:
                print(f"  {stats['file']}: +{stats['ref_titles_added']} titles, {stats['publications_restructured']} pubs restructured", file=sys.stderr)
        if stats['ref_titles_missing'] or stats['pub_titles_missing']:
            print(f"  {stats['file']}: {stats['ref_titles_missing']} ref titles missing, {stats['pub_titles_missing']} pub titles missing", file=sys.stderr)

    action = "Would modify" if args.dry_run else "Modified"
    print(f"\n{action} {files_changed}/{len(files)} files", file=sys.stderr)
    print(f"  Reference titles added: {total_ref_added}", file=sys.stderr)
    print(f"  Reference titles missing (no cache): {total_ref_missing}", file=sys.stderr)
    print(f"  Publications restructured: {total_pub_restructured}", file=sys.stderr)
    print(f"  Publication titles missing (no cache): {total_pub_missing}", file=sys.stderr)


if __name__ == '__main__':
    main()
