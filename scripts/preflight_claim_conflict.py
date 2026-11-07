#!/usr/bin/env python3
"""Pre-PR duplicate-claim/PR check (issue #16202, proposal C).

Run as `just preflight-claim-conflict MONDO:0014821 --self-issue 16098` as the
last step before a curation session opens its PR; the claim-disease skill names
it there.

What it catches that the creation-time guard (claim-dedupe-guard.yml) does not:
the case where two claims both passed the open-time check and then one pulled
ahead into a PR during the hours of curation. In the worked case (#16098 -> PR
#16142) the open-time preflight was clean, and by the time the PR opened, the
sibling claim #16096 was already PR #16116 -- which nothing re-checked. This
re-checks, keyed on the MONDO ID, over BOTH open claims and open PRs, and exits
non-zero if a competitor exists so the session stops instead of opening a
duplicate.

Transport: `gh api` REST (list issues, list pulls), paginated by explicit
`page=` params. These repo-scoped REST endpoints work both inside a Claude Code
session (where `gh issue/pr list` and the search API are blocked) and on a CI
runner. Explicit paging is used rather than `gh --paginate` because the agent
proxy a curation session runs behind rejects the numeric-ID pagination URLs
`gh --paginate` follows, so `--paginate` silently stops after one page there.
The MONDO ID is an exact key and the list endpoints are immediately consistent,
so there is no search-index lag.

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
MONDO_RE = re.compile(r"MONDO:\d+")
_PER_PAGE = 100
_MAX_PAGES = 50  # 5000 open items is far above the live counts; a guard against a loop


def gh_pages(path: str, *params: str) -> list[dict]:
    """All rows of a repo-scoped REST list endpoint, paged explicitly."""
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


def has_mondo(text: str, mondo: str) -> bool:
    # exact-ID match, not substring: MONDO:0014821 must not match MONDO:00148210
    return any(m == mondo for m in MONDO_RE.findall(text or ""))


def open_claims_with_mondo(mondo: str, self_issue: int | None) -> list[dict]:
    hits = []
    for issue in gh_pages(f"repos/{REPO}/issues", "labels=claim", "state=open"):
        if "pull_request" in issue:  # the issues endpoint also returns PRs
            continue
        if issue["number"] == self_issue:
            continue
        if has_mondo(issue.get("title", ""), mondo):
            hits.append(issue)
    return hits


def open_prs_for(mondo: str, name: str | None, self_branch: str | None) -> list[dict]:
    hits = []
    for pr in gh_pages(f"repos/{REPO}/pulls", "state=open"):
        if self_branch and pr.get("head", {}).get("ref") == self_branch:
            continue
        title = pr.get("title") or ""
        ref = pr.get("head", {}).get("ref") or ""
        if has_mondo(f"{title}\n{ref}", mondo) or (name and name.lower() in f"{title}\n{ref}".lower()):
            hits.append(pr)
    return hits


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mondo", help="MONDO ID of the disease being curated, e.g. MONDO:0014821")
    ap.add_argument("--self-issue", type=int, default=None, help="own claim issue number, to exclude")
    ap.add_argument("--self-branch", default=None, help="own PR head branch, to exclude")
    ap.add_argument("--name", default=None, help="disease name substring for the PR title/branch fallback; a short name can cause false STOPs, so use a distinctive one")
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
