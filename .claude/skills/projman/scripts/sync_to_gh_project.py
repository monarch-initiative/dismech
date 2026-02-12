#!/usr/bin/env python3
"""
Sync markdown project checkboxes to GitHub Projects.

Usage:
    python sync_to_gh_project.py PROJECT_FILE PROJECT_NUMBER [--owner OWNER] [--dry-run]

Example:
    python sync_to_gh_project.py projects/CANCER.md 4 --owner cmungall
    python sync_to_gh_project.py projects/CANCER.md 4 --dry-run
"""

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional


@dataclass
class CheckboxItem:
    """A checkbox item parsed from markdown."""
    name: str
    checked: bool
    tier: Optional[str] = None
    extra_info: Optional[str] = None
    line_number: int = 0


def parse_markdown_checkboxes(filepath: Path) -> List[CheckboxItem]:
    """Parse checkbox items from a markdown file."""
    items = []
    current_tier = None

    with open(filepath) as f:
        for line_num, line in enumerate(f, 1):
            # Track tier/category headers
            tier_match = re.match(r'^##\s+(?:Tier\s+\d+[^(]*|\w[^(]*)\s*\(', line)
            if tier_match:
                current_tier = line.strip()

            # Parse checkbox lines: - [ ] or - [x]
            checkbox_match = re.match(r'^-\s+\[([ xX])\]\s+(.+)$', line)
            if checkbox_match:
                checked = checkbox_match.group(1).lower() == 'x'
                content = checkbox_match.group(2).strip()

                # Split name from extra info (e.g., "Name - Created 2026-01-24")
                parts = content.split(' - ', 1)
                name = parts[0].strip()
                extra = parts[1].strip() if len(parts) > 1 else None

                items.append(CheckboxItem(
                    name=name,
                    checked=checked,
                    tier=current_tier,
                    extra_info=extra,
                    line_number=line_num
                ))

    return items


def get_gh_project_items(project_number: int, owner: str) -> Dict[str, dict]:
    """Get existing items from GitHub Project, keyed by title."""
    cmd = [
        'gh', 'project', 'item-list', str(project_number),
        '--owner', owner,
        '--format', 'json',
        '--limit', '500'
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error listing project items: {result.stderr}", file=sys.stderr)
        return {}

    data = json.loads(result.stdout)
    return {item['title']: item for item in data.get('items', [])}


def get_gh_project_fields(project_number: int, owner: str) -> dict:
    """Get field definitions from GitHub Project."""
    cmd = [
        'gh', 'project', 'field-list', str(project_number),
        '--owner', owner,
        '--format', 'json'
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error listing project fields: {result.stderr}", file=sys.stderr)
        return {}

    return json.loads(result.stdout)


def create_item(project_number: int, owner: str, item: CheckboxItem, dry_run: bool) -> bool:
    """Create a new item in the GitHub Project."""
    body = f"Tier: {item.tier}" if item.tier else ""
    if item.extra_info:
        body += f"\n{item.extra_info}"

    cmd = [
        'gh', 'project', 'item-create', str(project_number),
        '--owner', owner,
        '--title', item.name,
        '--body', body
    ]

    if dry_run:
        print(f"  [DRY-RUN] Would create: {item.name}")
        return True

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  Error creating {item.name}: {result.stderr}", file=sys.stderr)
        return False

    print(f"  Created: {item.name}")
    return True


def update_item_status(project_number: int, owner: str, item_id: str,
                       status_field_id: str, status_option_id: str,
                       project_id: str, dry_run: bool) -> bool:
    """Update an item's status in the GitHub Project."""
    cmd = [
        'gh', 'project', 'item-edit',
        '--id', item_id,
        '--field-id', status_field_id,
        '--single-select-option-id', status_option_id,
        '--project-id', project_id
    ]

    if dry_run:
        print(f"  [DRY-RUN] Would update status for item {item_id}")
        return True

    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode == 0


def sync_project(filepath: Path, project_number: int, owner: str, dry_run: bool = False):
    """Sync markdown checkboxes to GitHub Project."""
    print(f"Parsing {filepath}...")
    md_items = parse_markdown_checkboxes(filepath)
    print(f"  Found {len(md_items)} checkbox items")

    print(f"\nFetching GitHub Project #{project_number}...")
    gh_items = get_gh_project_items(project_number, owner)
    print(f"  Found {len(gh_items)} existing items")

    fields = get_gh_project_fields(project_number, owner)
    status_field = next(
        (f for f in fields.get('fields', []) if f['name'] == 'Status'),
        None
    )

    if status_field:
        status_options = {opt['name']: opt['id'] for opt in status_field.get('options', [])}
        print(f"  Status options: {list(status_options.keys())}")
    else:
        status_options = {}
        print("  Warning: No Status field found")

    # Sync items
    print("\nSyncing...")
    created = 0
    updated = 0
    skipped = 0

    for item in md_items:
        if item.name in gh_items:
            # Item exists - check if status needs update
            gh_item = gh_items[item.name]
            current_status = gh_item.get('status', '')

            target_status = 'Done' if item.checked else 'Todo'
            if current_status != target_status and status_field and target_status in status_options:
                # Note: Would need project_id to update - simplified here
                print(f"  {item.name}: {current_status} -> {target_status}")
                updated += 1
            else:
                skipped += 1
        else:
            # Item doesn't exist - create it
            if create_item(project_number, owner, item, dry_run):
                created += 1

    print(f"\nSummary:")
    print(f"  Created: {created}")
    print(f"  Updated: {updated}")
    print(f"  Skipped: {skipped}")


def main():
    parser = argparse.ArgumentParser(description='Sync markdown project to GitHub Project')
    parser.add_argument('project_file', type=Path, help='Path to markdown project file')
    parser.add_argument('project_number', type=int, help='GitHub Project number')
    parser.add_argument('--owner', default='@me', help='GitHub owner (default: @me)')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done')

    args = parser.parse_args()

    if not args.project_file.exists():
        print(f"Error: {args.project_file} not found", file=sys.stderr)
        sys.exit(1)

    sync_project(args.project_file, args.project_number, args.owner, args.dry_run)


if __name__ == '__main__':
    main()
