#!/usr/bin/env python3
"""Post-filing self-check: did this session win the claim race? (issue #16202)

Run by the claim-disease skill **immediately after filing a claim issue**, before
any curation work:

    just claim-self-check MONDO:0014821 --self-issue 16263

It lists the open `claim` issues for the given MONDO ID off GitHub's
immediately-consistent list endpoint, applies the same lowest-issue-number keeper
rule as the creation-time workflow guard (`.github/scripts/claim_dedupe_guard.py`),
and reports whether the session's own claim is the keeper.

- exit 0  -> this session's claim IS the keeper. Proceed to curate.
- exit 3  -> a lower-numbered open claim exists for this MONDO. This session LOST
             the race; it must stand down WITHOUT curating. The keeper number is
             printed as `KEEPER=<n>` so the caller can close its own claim against
             it.
- exit 2  -> usage / transport error (bad MONDO, own issue never became visible).

Why this exists and why it is separate from the workflow guard: the guard labels
the losing issue for a *human*, but it cannot stop a *running* session — and the
colliding sessions are often on different Claude accounts, so neither can see the
other's session. The only thing they share is GitHub state, so each session
re-reads the list endpoint here and stands down on its own if it lost. This saves
the losing session's entire curation spend, which the pre-PR check
(`preflight_claim_conflict.py`) cannot: that one only fires once the work is done.

Transport: `gh api` REST, paged with explicit `page=` params — the same reason
`preflight_claim_conflict.py` avoids `gh --paginate` (the agent proxy a curation
session runs behind rejects the numeric-ID pagination URLs it follows) and avoids
`gh issue list` (GraphQL, 403 in a Claude Code session). The list endpoint is
immediately consistent and the MONDO ID is an exact key, so there is no
search-index lag to wait out — only the brief moment for the session's own
just-created issue to appear, which the retry loop below covers.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time

REPO = "monarch-initiative/dismech"
MONDO_RE = re.compile(r"MONDO:\d+")
_PER_PAGE = 100
_MAX_PAGES = 50
_RETRIES = 5
_RETRY_SLEEP = 3.0  # seconds; the list endpoint is consistent, this covers propagation only


def gh_pages(path: str, *params: str) -> list[dict]:
    rows: list[dict] = []
    for page in range(1, _MAX_PAGES + 1):
        cmd = ["gh", "api", "-X", "GET", path, "-f", f"per_page={_PER_PAGE}", "-f", f"page={page}"]
        for p in params:
            cmd += ["-f", p]
        out = subprocess.run(cmd, check=True, capture_output=True, text=True).stdout
        batch = json.loads(out)
        if not batch:
            break
        rows.extend(batch)
        if len(batch) < _PER_PAGE:
            break
    return rows


def open_claims_for(mondo: str) -> list[dict]:
    """Open `claim` issues whose title carries exactly this MONDO ID."""
    hits = []
    for issue in gh_pages(f"repos/{REPO}/issues", "labels=claim", "state=open"):
        if "pull_request" in issue:  # the issues endpoint also returns PRs
            continue
        title = issue.get("title", "")
        if any(m == mondo for m in MONDO_RE.findall(title)):
            hits.append(issue)
    return hits


def keeper_number(members: list[dict]) -> int:
    """Keeper = lowest issue number — identical rule to the workflow guard, so a
    session self-checking here and the guard labelling later always agree."""
    return min(m["number"] for m in members)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mondo", help="MONDO ID just claimed, e.g. MONDO:0014821")
    ap.add_argument("--self-issue", type=int, required=True, help="this session's own claim issue number")
    args = ap.parse_args()

    if not re.fullmatch(r"MONDO:\d+", args.mondo):
        print(f"not a MONDO ID: {args.mondo}", file=sys.stderr)
        return 2

    # Retry until our own just-filed claim is visible, so we never read a list
    # that predates it and wrongly conclude we are alone / the keeper.
    members: list[dict] = []
    for attempt in range(_RETRIES):
        members = open_claims_for(args.mondo)
        if any(m["number"] == args.self_issue for m in members):
            break
        if attempt < _RETRIES - 1:
            time.sleep(_RETRY_SLEEP)
    else:
        print(
            f"own claim #{args.self_issue} not visible among open claims for "
            f"{args.mondo} after {_RETRIES} tries; cannot determine the keeper",
            file=sys.stderr,
        )
        return 2

    keeper = keeper_number(members)
    others = sorted(m["number"] for m in members if m["number"] != args.self_issue)

    if keeper == args.self_issue:
        if others:
            print(
                f"OK: #{args.self_issue} is the keeper for {args.mondo} "
                f"(also open, higher-numbered: {', '.join('#' + str(n) for n in others)}). Proceed."
            )
        else:
            print(f"OK: #{args.self_issue} is the only open claim for {args.mondo}. Proceed.")
        return 0

    print(f"KEEPER={keeper}")
    print(
        f"STAND DOWN: #{args.self_issue} LOST the race for {args.mondo}. "
        f"#{keeper} is the lower-numbered open claim and is the canonical one. "
        f"Do not curate. Close #{args.self_issue} as a duplicate of #{keeper} and stop."
    )
    return 3


if __name__ == "__main__":
    sys.exit(main())
