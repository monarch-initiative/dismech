#!/usr/bin/env python3
"""DRAFT for review (issue #16202) — pre-PR duplicate-claim/PR check (proposal C).

Proposed home: scripts/preflight_claim_conflict.py, run as
`just preflight-claim-conflict MONDO:0014821 --self-issue 16098` as the last
step before a curation session opens its PR, and named in the create-pr / curate
skills.

What it catches that the creation-time guard (proposal A) does not: the case
where two claims both passed the open-time check and then one pulled ahead into
a PR during the hours of curation. In the worked case (#16098 -> PR #16142) the
open-time preflight was clean, and by the time the PR opened, the sibling claim
#16096 was already PR #16116 — which nothing re-checked. This re-checks, keyed
on the MONDO ID, over BOTH open claims and open PRs, and exits non-zero if a
competitor exists so the session stops instead of opening a duplicate.

Transport: uses `gh api` REST (list issues, list pulls). These repo-scoped REST
endpoints work both inside a Claude Code session (where `gh issue/pr list` and
the search API are blocked) and on a CI runner. The MONDO ID is an exact key and
the list endpoints are immediately consistent, so there is no search-index lag.

Residual gap (shared with the existing open-PR search in the claim skill): a
curation PR whose title and branch name carry no MONDO ID cannot be matched on
the ID. Curation PR titles here do carry it; a name-substring fallback covers
the rest imperfectly, which is why this is a check, not a gate that can promise
zero duplicates.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys

REPO = "monarch-initiative/dismech"


def gh_json(path: str, *params: str) -> list[dict]:
    """One page of a repo-scoped REST list endpoint (max 100; enough here)."""
    cmd = ["gh", "api", "-X", "GET", path, "-f", "per_page=100"]
    for p in params:
        cmd += ["-f", p]
    out = subprocess.run(cmd, check=True, capture_output=True, text=True).stdout
    return json.loads(out)


def open_claims_with_mondo(mondo: str, self_issue: int | None) -> list[dict]:
    hits = []
    for issue in gh_json(f"repos/{REPO}/issues", "labels=claim", "state=open"):
        if "pull_request" in issue:  # the issues endpoint also returns PRs
            continue
        if issue["number"] == self_issue:
            continue
        if mondo in (issue.get("title") or ""):
            hits.append(issue)
    return hits


def open_prs_for(mondo: str, name: str | None, self_branch: str | None) -> list[dict]:
    hits = []
    for pr in gh_json(f"repos/{REPO}/pulls", "state=open"):
        if self_branch and pr.get("head", {}).get("ref") == self_branch:
            continue
        hay = f"{pr.get('title') or ''}\n{pr.get('head', {}).get('ref') or ''}"
        if mondo in hay or (name and name.lower() in hay.lower()):
            hits.append(pr)
    return hits


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mondo", help="MONDO ID of the disease being curated, e.g. MONDO:0014821")
    ap.add_argument("--self-issue", type=int, default=None, help="own claim issue number, to exclude")
    ap.add_argument("--self-branch", default=None, help="own PR head branch, to exclude")
    ap.add_argument("--name", default=None, help="disease name substring, for the PR title/branch fallback")
    args = ap.parse_args()

    if not re.fullmatch(r"MONDO:\d+", args.mondo):
        print(f"not a MONDO ID: {args.mondo}", file=sys.stderr)
        return 2

    claims = open_claims_with_mondo(args.mondo, args.self_issue)
    prs = open_prs_for(args.mondo, args.name, args.self_branch)

    if not claims and not prs:
        print(f"OK: no other open claim or PR for {args.mondo}. Safe to open the PR.")
        return 0

    print(f"STOP: another session may already be curating {args.mondo}.")
    for c in claims:
        print(f"  competing claim:  #{c['number']}  {c['title']}")
    for p in prs:
        print(f"  competing PR:     #{p['number']}  {p['title']}  ({p['html_url']})")
    print(
        "\nDo not open a duplicate PR. Follow the 'two PRs curate the same disease'\n"
        "protocol in the claim-disease skill: if the other PR is further along, stop\n"
        "and let it land; otherwise coordinate on the claim issue."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
