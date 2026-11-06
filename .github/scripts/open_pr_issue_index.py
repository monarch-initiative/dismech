#!/usr/bin/env python3
"""Which open issues already have an open PR working on them (issue #5105).

The curation scanner picks an open, unassigned `curation` issue and opens a PR
against it. Nothing on the issue changes when that PR opens, so the next hourly
run, or another effort tier's run, sees the same issue as still untouched and
opens a second PR. #4990 and #5105 record clusters of two to four PRs against
one issue; #12842 got two that both merged. The scanner's prompt told the agent
to check for linked PRs, and the agent did not always do it.

This script answers the question deterministically so the workflow can hand the
agent the answer instead of asking it to find out:

    open_pr_issue_index.py                 # JSON {"<issue>": [<pr>, ...]}
    open_pr_issue_index.py --list          # space-separated issue numbers
    open_pr_issue_index.py --check 1234    # exit 1 if #1234 has an open PR

A PR counts as working on an issue when its title or body says `Closes #N`,
`Fixes #N`, `Resolves #N` (any tense) or `Addresses #N`, the phrasing several
agent PRs use instead. A link made only in the PR sidebar, with no keyword in
the body, is not seen: the REST list does not return it. Agent PRs always carry
the keyword, which is the case this exists for.
A bare `#N` mention does not count: PR bodies cite related issues constantly,
and excluding every one of them would starve the scanner's queue.

Why the REST pulls list, not the search API: search lags creation by seconds
to minutes, which is the window two concurrent runs race in. The list endpoint
is immediately consistent, the same reason claim_dedupe_guard.py uses
`gh issue list`. (Not GraphQL either, so the script also runs from a Claude
Code session, where GraphQL is blocked.)

Why not label or assign the issue instead: one issue legitimately gets several
PRs (#13103 is being split into one entry per SCA subtype), and a label would
need removing whenever a PR closes unmerged. Computing the set from live PR
state at the start of each run has nothing to go stale.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from collections.abc import Iterable

# `Closes #12`, `fixes: #12`, `Resolved #12`, `Addresses #12`. GitHub itself
# links the first three (and their tenses) as closing references; matching them
# here as well covers a PR body GitHub has not linked, e.g. one that names
# several issues in a list it does not parse.
REFERENCE_RE = re.compile(
    r"\b(?:close[sd]?|fix(?:e[sd])?|resolve[sd]?|address(?:e[sd])?)\b"
    r"\s*:?\s*#(\d+)\b",
    re.IGNORECASE,
)


def referenced_issues(pr: dict) -> set[int]:
    """Issue numbers this PR says it works on.

    `#N` is always same-repo here: a cross-repo reference is written
    `owner/repo#N`, which the pattern does not match because `#` must follow
    the keyword and whitespace directly.
    """

    text = f"{pr.get('title') or ''}\n{pr.get('body') or ''}"
    found = {int(n) for n in REFERENCE_RE.findall(text)}
    found.discard(int(pr["number"]))
    return found


def build_index(prs: Iterable[dict]) -> dict[int, list[int]]:
    """Map each referenced issue to the sorted open PR numbers referencing it."""

    index: dict[int, set[int]] = {}
    for pr in prs:
        for issue in referenced_issues(pr):
            index.setdefault(issue, set()).add(int(pr["number"]))
    return {issue: sorted(prs_) for issue, prs_ in sorted(index.items())}


def fetch_open_prs(repo: str) -> list[dict]:
    out = subprocess.run(
        [
            "gh",
            "api",
            "--paginate",
            f"repos/{repo}/pulls?state=open&per_page=100",
            "--jq",
            ".[] | {number, title, body}",
        ],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    return [json.loads(line) for line in out.splitlines() if line.strip()]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--repo", default=os.environ.get("REPO") or os.environ.get("GITHUB_REPOSITORY")
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--list", action="store_true", help="print issue numbers only")
    mode.add_argument(
        "--check",
        type=int,
        metavar="ISSUE",
        help="exit 1 if ISSUE already has an open PR",
    )
    parser.add_argument(
        "--exclude-pr",
        type=int,
        action="append",
        default=[],
        help="ignore this PR (e.g. the one you are updating)",
    )
    args = parser.parse_args(argv)
    if not args.repo:
        parser.error("--repo (or REPO / GITHUB_REPOSITORY) is required")

    prs = [
        p for p in fetch_open_prs(args.repo) if int(p["number"]) not in args.exclude_pr
    ]
    index = build_index(prs)

    if args.check is not None:
        holders = index.get(args.check, [])
        if holders:
            names = ", ".join(f"#{n}" for n in holders)
            print(
                f"#{args.check} already has an open PR: {names}. "
                f"Follow up on that PR instead of opening another."
            )
            return 1
        print(f"#{args.check} has no open PR.")
        return 0
    if args.list:
        print(" ".join(str(n) for n in index))
        return 0
    print(json.dumps({str(k): v for k, v in index.items()}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
