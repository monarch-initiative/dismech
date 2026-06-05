#!/usr/bin/env python3
"""Reconcile Epic #1079 checkboxes against the dismech KB.

For each MONDO ID listed in the epic issue's checklist, marks the item as
checked ([x]) if the disease is covered in kb/disorders/ — either as a root
entry, a has_subtypes subtype, or a mondo_mappings cross-reference.

This correctly handles LUMP_INTO_PARENT diseases whose parent has been curated
and lists them as a subtype, even though no standalone kb/disorders/ file
exists for the subtype itself.

Usage:
    # Dry-run to preview changes
    python scripts/sync_epic_checkboxes.py --dry-run

    # Apply changes to GitHub issue #1079
    python scripts/sync_epic_checkboxes.py

    # Target a different issue or repo
    python scripts/sync_epic_checkboxes.py --issue 1079 --repo monarch-initiative/dismech

Environment:
    Requires `gh` (GitHub CLI) to be authenticated.
"""

from __future__ import annotations

import argparse
import glob
import json
import re
import subprocess
import sys
import yaml
from pathlib import Path


_CHECKBOX_PATTERN = re.compile(
    r"^(?P<indent>[ \t]*)- (?P<state>\[ \]|\[x\]|\[X\]) "
    r"(?P<rest>\[.+?\]\(https://monarchinitiative\.org/(?P<mondo_id>MONDO:\d+)\).*)"
)

_SECTION_HEADER_PATTERN = re.compile(
    r"^(##+ .+?)\((\d+) diseases?,\s+(\d+) curated in dismech\)"
)


def build_covered_ids(kb_dir: Path) -> dict[str, str]:
    """Build a mapping of covered MONDO IDs → kb filename.

    Includes root entries, has_subtypes subtypes, and mondo_mappings so that
    LUMP_INTO_PARENT diseases covered via a parent's has_subtypes are correctly
    identified as curated.
    """
    covered: dict[str, str] = {}

    for path in sorted(kb_dir.glob("*.yaml")):
        if path.name.endswith(".history.yaml"):
            continue
        try:
            with open(path, encoding="utf-8") as fh:
                data = yaml.safe_load(fh)
        except Exception:
            continue
        if not isinstance(data, dict):
            continue

        fname = path.name

        root_id = (((data.get("disease_term") or {}).get("term") or {}).get("id"))
        if root_id:
            covered.setdefault(str(root_id), fname)

        for sub in data.get("has_subtypes") or []:
            if not isinstance(sub, dict):
                continue
            # Subtype entries use `subtype_term` (not `disease_term`)
            sub_id = (((sub.get("subtype_term") or {}).get("term") or {}).get("id"))
            if sub_id:
                covered.setdefault(str(sub_id), fname)

        for m in ((data.get("mappings") or {}).get("mondo_mappings") or []):
            if not isinstance(m, dict):
                continue
            map_id = ((m.get("term") or {}).get("id"))
            if map_id:
                covered.setdefault(str(map_id), fname)

    return covered


def fetch_issue_body(repo: str, issue: int) -> str:
    result = subprocess.run(
        ["gh", "issue", "view", str(issue), "--repo", repo, "--json", "body", "-q", ".body"],
        capture_output=True, text=True, check=True,
    )
    return result.stdout


def update_issue_body(repo: str, issue: int, body: str, dry_run: bool) -> None:
    if dry_run:
        print(f"[dry-run] Would update issue #{issue} body ({len(body)} chars)")
        return
    subprocess.run(
        ["gh", "issue", "edit", str(issue), "--repo", repo, "--body", body],
        check=True,
    )
    print(f"Updated issue #{issue} body.")


def reconcile_body(body: str, covered: dict[str, str]) -> tuple[str, int, int]:
    """Return updated body, count of newly checked items, and total checked items."""
    lines = body.splitlines()
    newly_checked = 0
    total_checked = 0

    # Pass 1: update checkboxes and collect section-level counts
    # Track which section we're in for header updating
    section_mondo_ids: list[list[str]] = []  # per-section list of MONDO IDs
    section_header_lines: list[int] = []  # line indices of section headers
    current_section_ids: list[str] = []

    updated_lines = []
    for i, line in enumerate(lines):
        m = _CHECKBOX_PATTERN.match(line)
        if m:
            mondo_id = m.group("mondo_id")
            current_state = m.group("state")
            current_section_ids.append(mondo_id)

            if current_state == "[ ]" and mondo_id in covered:
                line = f"{m.group('indent')}- [x] {m.group('rest')}"
                newly_checked += 1
                total_checked += 1
            elif current_state in ("[x]", "[X]"):
                total_checked += 1
        else:
            # Check if this is a section header
            hdr_m = _SECTION_HEADER_PATTERN.match(line)
            if hdr_m:
                section_header_lines.append(len(updated_lines))
                section_mondo_ids.append(current_section_ids)
                current_section_ids = []

        updated_lines.append(line)

    # Capture the last section's IDs
    section_mondo_ids.append(current_section_ids)

    # Pass 2: update section headers with accurate curated counts
    # We have one extra entry in section_mondo_ids (before the first header),
    # so zip pairs header_line[i] with section_mondo_ids[i+1]
    for idx, header_line_idx in enumerate(section_header_lines):
        section_ids = section_mondo_ids[idx + 1]
        if not section_ids:
            continue
        line = updated_lines[header_line_idx]
        hdr_m = _SECTION_HEADER_PATTERN.match(line)
        if not hdr_m:
            continue
        total_in_section = len(section_ids)
        curated_in_section = sum(1 for mid in section_ids if mid in covered)
        new_line = (
            f"{hdr_m.group(1)}"
            f"({total_in_section} disease{'s' if total_in_section != 1 else ''}, "
            f"{curated_in_section} curated in dismech)"
        )
        updated_lines[header_line_idx] = new_line

    return "\n".join(updated_lines), newly_checked, total_checked


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--issue", type=int, default=1079, help="GitHub issue number")
    parser.add_argument("--repo", default="monarch-initiative/dismech", help="GitHub repo")
    parser.add_argument("--kb-dir", default="kb/disorders", help="Path to kb/disorders/")
    parser.add_argument("--dry-run", action="store_true", help="Print diff without updating")
    args = parser.parse_args()

    kb_dir = Path(args.kb_dir)
    if not kb_dir.is_dir():
        print(f"ERROR: kb_dir not found: {kb_dir}", file=sys.stderr)
        return 1

    print(f"Building coverage index from {kb_dir} ...")
    covered = build_covered_ids(kb_dir)
    print(f"  {len(covered)} MONDO IDs covered (root + has_subtypes + mondo_mappings)")

    print(f"Fetching issue #{args.issue} from {args.repo} ...")
    body = fetch_issue_body(args.repo, args.issue)

    updated_body, newly_checked, total_checked = reconcile_body(body, covered)

    if updated_body == body:
        print("No changes — all checkboxes already up to date.")
        return 0

    print(f"  {newly_checked} newly checked, {total_checked} total checked after reconciliation")

    if args.dry_run:
        # Show a compact diff
        old_lines = body.splitlines()
        new_lines = updated_body.splitlines()
        for i, (old, new) in enumerate(zip(old_lines, new_lines)):
            if old != new:
                print(f"  line {i+1}:")
                print(f"    - {old}")
                print(f"    + {new}")
        print("[dry-run] No changes written.")
        return 0

    update_issue_body(args.repo, args.issue, updated_body, dry_run=False)
    return 0


if __name__ == "__main__":
    sys.exit(main())
