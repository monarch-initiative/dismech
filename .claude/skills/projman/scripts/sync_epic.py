#!/usr/bin/env python3
"""
Sync markdown project files with GitHub epic issues.

Usage:
    sync_epic.py push <markdown_file>   # Push markdown → GitHub issue
    sync_epic.py pull <markdown_file>   # Pull GitHub issue → markdown
    sync_epic.py status <markdown_file> # Show sync status

The markdown file should have:
- A link to the GitHub issue (blockquote or frontmatter)
- Content between "## Overview" and "---" or "# NOTES" syncs to issue body
- Checkbox state can be synced bidirectionally

Example markdown:
    # Project Title

    > **GitHub Epic**: https://github.com/owner/repo/issues/123

    ## Overview
    ...

    ## Progress
    - [x] Done item
    - [ ] Pending item

    ---
    # NOTES
    [not synced]
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path
from typing import Optional, Tuple


def extract_issue_info(content: str) -> Optional[Tuple[str, str, int]]:
    """Extract owner, repo, issue number from markdown content."""
    # Match: https://github.com/owner/repo/issues/123
    pattern = r'https://github\.com/([^/]+)/([^/]+)/issues/(\d+)'
    match = re.search(pattern, content)
    if match:
        return match.group(1), match.group(2), int(match.group(3))
    return None


def extract_sync_content(content: str) -> str:
    """Extract the portion of markdown that should sync to GitHub issue."""
    lines = content.split('\n')

    # Find start: first ## heading (usually Overview)
    start_idx = 0
    for i, line in enumerate(lines):
        if line.startswith('## '):
            start_idx = i
            break

    # Find end: --- followed by # NOTES, or just # NOTES, or # STATUS
    end_idx = len(lines)
    for i, line in enumerate(lines):
        # Stop at horizontal rule before NOTES
        if line.strip() == '---':
            # Check if next non-empty line is NOTES
            for j in range(i + 1, min(i + 5, len(lines))):
                if lines[j].strip().startswith('# NOTES') or lines[j].strip().startswith('# STATUS'):
                    end_idx = i
                    break
            if end_idx != len(lines):
                break
        # Also stop at # NOTES directly
        if line.strip().startswith('# NOTES'):
            end_idx = i
            break

    sync_lines = lines[start_idx:end_idx]

    # Add sync source comment at the end
    return '\n'.join(sync_lines).strip()


def parse_checkboxes(content: str) -> dict:
    """Parse checkbox items from content. Returns {item_text: checked}."""
    checkboxes = {}
    for line in content.split('\n'):
        match = re.match(r'^(\s*)-\s+\[([ xX])\]\s+(.+)$', line)
        if match:
            checked = match.group(2).lower() == 'x'
            item_text = match.group(3).strip()
            # Normalize: remove trailing file references like "- `File.yaml`"
            item_key = re.sub(r'\s*-\s*`[^`]+`\s*$', '', item_text).strip()
            checkboxes[item_key] = checked
    return checkboxes


def update_checkboxes(content: str, checkbox_states: dict) -> str:
    """Update checkbox states in content based on checkbox_states dict."""
    lines = content.split('\n')
    updated_lines = []

    for line in lines:
        match = re.match(r'^(\s*-\s+\[)([ xX])(\]\s+)(.+)$', line)
        if match:
            prefix = match.group(1)
            current_state = match.group(2)
            middle = match.group(3)
            item_text = match.group(4)

            # Normalize key
            item_key = re.sub(r'\s*-\s*`[^`]+`\s*$', '', item_text).strip()

            if item_key in checkbox_states:
                new_state = 'x' if checkbox_states[item_key] else ' '
                line = f"{prefix}{new_state}{middle}{item_text}"

        updated_lines.append(line)

    return '\n'.join(updated_lines)


def get_issue_body(owner: str, repo: str, issue_num: int) -> Optional[str]:
    """Fetch issue body from GitHub."""
    cmd = ['gh', 'issue', 'view', str(issue_num),
           '--repo', f'{owner}/{repo}', '--json', 'body', '--jq', '.body']
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error fetching issue: {result.stderr}", file=sys.stderr)
        return None
    return result.stdout.strip()


def update_issue_body(owner: str, repo: str, issue_num: int, body: str) -> bool:
    """Update issue body on GitHub."""
    cmd = ['gh', 'issue', 'edit', str(issue_num),
           '--repo', f'{owner}/{repo}', '--body', body]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error updating issue: {result.stderr}", file=sys.stderr)
        return False
    return True


def cmd_push(filepath: Path) -> int:
    """Push markdown content to GitHub issue."""
    content = filepath.read_text()

    issue_info = extract_issue_info(content)
    if not issue_info:
        print("Error: No GitHub issue link found in markdown", file=sys.stderr)
        print("Add: > **GitHub Epic**: https://github.com/owner/repo/issues/NUM", file=sys.stderr)
        return 1

    owner, repo, issue_num = issue_info
    print(f"Syncing to {owner}/{repo}#{issue_num}")

    sync_content = extract_sync_content(content)

    # Add sync marker
    sync_content += f"\n\n---\n<!-- SYNC_SOURCE: {filepath.name} -->"

    if update_issue_body(owner, repo, issue_num, sync_content):
        print(f"✓ Updated issue #{issue_num}")
        return 0
    return 1


def cmd_pull(filepath: Path) -> int:
    """Pull checkbox states from GitHub issue to markdown."""
    content = filepath.read_text()

    issue_info = extract_issue_info(content)
    if not issue_info:
        print("Error: No GitHub issue link found in markdown", file=sys.stderr)
        return 1

    owner, repo, issue_num = issue_info
    print(f"Pulling from {owner}/{repo}#{issue_num}")

    issue_body = get_issue_body(owner, repo, issue_num)
    if issue_body is None:
        return 1

    # Parse checkbox states from issue
    gh_checkboxes = parse_checkboxes(issue_body)

    if not gh_checkboxes:
        print("No checkboxes found in issue body")
        return 0

    # Update markdown with GitHub states
    updated_content = update_checkboxes(content, gh_checkboxes)

    if updated_content != content:
        filepath.write_text(updated_content)
        print(f"✓ Updated {filepath.name} with {len(gh_checkboxes)} checkbox states")
    else:
        print("No changes needed")

    return 0


def cmd_status(filepath: Path) -> int:
    """Show sync status between markdown and GitHub issue."""
    content = filepath.read_text()

    issue_info = extract_issue_info(content)
    if not issue_info:
        print("Error: No GitHub issue link found in markdown", file=sys.stderr)
        return 1

    owner, repo, issue_num = issue_info
    print(f"Epic: {owner}/{repo}#{issue_num}")

    # Parse local checkboxes
    md_checkboxes = parse_checkboxes(content)
    completed = sum(1 for v in md_checkboxes.values() if v)
    total = len(md_checkboxes)

    print(f"Local:  {completed}/{total} ({100*completed//total if total else 0}%)")

    # Fetch and parse GitHub checkboxes
    issue_body = get_issue_body(owner, repo, issue_num)
    if issue_body:
        gh_checkboxes = parse_checkboxes(issue_body)
        gh_completed = sum(1 for v in gh_checkboxes.values() if v)
        gh_total = len(gh_checkboxes)
        print(f"GitHub: {gh_completed}/{gh_total} ({100*gh_completed//gh_total if gh_total else 0}%)")

        # Show differences
        diffs = []
        all_keys = set(md_checkboxes.keys()) | set(gh_checkboxes.keys())
        for key in sorted(all_keys):
            md_state = md_checkboxes.get(key)
            gh_state = gh_checkboxes.get(key)
            if md_state != gh_state:
                md_mark = '[x]' if md_state else '[ ]' if md_state is not None else '---'
                gh_mark = '[x]' if gh_state else '[ ]' if gh_state is not None else '---'
                diffs.append(f"  {key}: local={md_mark} github={gh_mark}")

        if diffs:
            print("\nDifferences:")
            for d in diffs[:10]:
                print(d)
            if len(diffs) > 10:
                print(f"  ... and {len(diffs) - 10} more")
        else:
            print("\n✓ In sync")

    return 0


def main():
    parser = argparse.ArgumentParser(
        description='Sync markdown project files with GitHub epic issues'
    )
    parser.add_argument('command', choices=['push', 'pull', 'status'],
                        help='push=md→GH, pull=GH→md, status=compare')
    parser.add_argument('markdown_file', type=Path,
                        help='Path to markdown project file')

    args = parser.parse_args()

    if not args.markdown_file.exists():
        print(f"Error: {args.markdown_file} not found", file=sys.stderr)
        return 1

    if args.command == 'push':
        return cmd_push(args.markdown_file)
    elif args.command == 'pull':
        return cmd_pull(args.markdown_file)
    elif args.command == 'status':
        return cmd_status(args.markdown_file)


if __name__ == '__main__':
    sys.exit(main())
