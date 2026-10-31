#!/usr/bin/env python3
"""Deterministic duplicate-claim guard (issue #16202, proposal A).

Finds open `claim` issues whose titles carry the same MONDO ID and flags the
duplicates. The keeper is the lowest issue number in each same-MONDO group; any
higher-numbered open claim in the group is a duplicate. Flagging = add the
`duplicate-claim` label and post one comment naming the keeper. It never closes
an issue -- a legitimate re-claim, where the lower one is abandoned, must not be
auto-closed -- so a maintainer closes the loser; the label makes them findable.
It is idempotent (skips an issue that already has the label).

Why list, not search: the title MONDO ID is an exact key and `gh issue list`
hits GitHub's immediately-consistent list endpoint, so a claim filed seconds
ago is already visible -- unlike the search API the LLM dedupe uses.

On an `issues.opened` or `workflow_dispatch` run it scopes to the MONDO ID of
the triggering issue; on a `schedule` run it sweeps every open claim (the
backstop for a sibling that was invisible at open time).

Runs on a normal Actions runner where `gh` works (the GraphQL block is specific
to Claude Code sessions, not CI). Set DRY_RUN=1 to report without labelling or
commenting.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys

MONDO_RE = re.compile(r"MONDO:\d+")
DUPLICATE_LABEL = "duplicate-claim"


def gh(*args: str) -> str:
    return subprocess.run(
        ["gh", *args], check=True, capture_output=True, text=True
    ).stdout


def open_claims(repo: str) -> list[dict]:
    # --label is the immediately consistent list filter; --limit is well above
    # the live open-claim count so gh returns the whole set in one call.
    out = gh(
        "issue", "list", "--repo", repo, "--label", "claim", "--state", "open",
        "--limit", "2000", "--json", "number,title,labels",
    )
    return json.loads(out)


def mondo_of(title: str) -> str | None:
    m = MONDO_RE.search(title or "")
    return m.group(0) if m else None


def groups_by_mondo(claims: list[dict]) -> dict[str, list[dict]]:
    g: dict[str, list[dict]] = {}
    for c in claims:
        key = mondo_of(c["title"])
        if key:
            g.setdefault(key, []).append(c)
    return g


def keeper_and_duplicates(members: list[dict]) -> tuple[int, list[dict]]:
    """Keeper = lowest issue number in a same-MONDO group; the rest are duplicates.

    Pure and deterministic: every run over the same group picks the same keeper,
    which is what makes two parallel runs agree on which issue is the loser.
    """
    keeper = min(m["number"] for m in members)
    return keeper, [m for m in members if m["number"] != keeper]


def already_flagged(issue: dict) -> bool:
    return any(l.get("name") == DUPLICATE_LABEL for l in issue.get("labels", []))


def ensure_label(repo: str) -> None:
    """Create the duplicate-claim label if the repo does not have it yet.

    `gh issue edit --add-label` fails on a missing label, so make the guard
    self-sufficient rather than depending on a manual one-off setup.
    """
    try:
        gh("label", "create", DUPLICATE_LABEL, "--repo", repo,
           "--color", "d93f0b",
           "--description", "A later claim issue for a MONDO ID already claimed by a lower-numbered open issue")
    except subprocess.CalledProcessError:
        pass  # already exists


def flag(repo: str, dup: dict, keeper: int, dry_run: bool) -> None:
    body = (
        f"Duplicate claim of #{keeper}: both claim the same MONDO ID. "
        f"Do not start curation here -- #{keeper} (the lower issue number) is the "
        f"canonical claim. A maintainer should close this one; if #{keeper} turns "
        f"out to be abandoned, this claim can take over instead.\n\n"
        f"Flagged deterministically by the claim-dedupe guard (issue #16202), "
        f"keyed on the MONDO ID in the title."
    )
    if dry_run:
        print(f"[dry-run] would flag #{dup['number']} as duplicate of #{keeper}")
        return
    gh("issue", "edit", str(dup["number"]), "--repo", repo, "--add-label", DUPLICATE_LABEL)
    gh("issue", "comment", str(dup["number"]), "--repo", repo, "--body", body)
    print(f"flagged #{dup['number']} as duplicate of #{keeper}")


def main() -> int:
    repo = os.environ["REPO"]
    event = os.environ.get("EVENT", "")
    trigger = os.environ.get("TRIGGER_ISSUE", "").strip()
    dry_run = os.environ.get("DRY_RUN", "").strip() not in ("", "0", "false", "False")

    claims = open_claims(repo)
    groups = groups_by_mondo(claims)

    # Scope: a specific MONDO on an issue/dispatch event, every group on a sweep.
    if event in ("issues", "workflow_dispatch") and trigger:
        by_num = {c["number"]: c for c in claims}
        trig = by_num.get(int(trigger))
        if trig is None:
            print(f"#{trigger} is not an open claim issue; nothing to do")
            return 0
        key = mondo_of(trig["title"])
        if key is None:
            print(f"#{trigger} has no MONDO ID in its title; nothing to do")
            return 0
        scoped = {key: groups.get(key, [])}
    else:
        scoped = groups

    to_flag = []
    for members in scoped.values():
        if len(members) < 2:
            continue
        keeper, dups = keeper_and_duplicates(members)
        for m in dups:
            if not already_flagged(m):
                to_flag.append((m, keeper))

    if to_flag and not dry_run:
        ensure_label(repo)
    for dup, keeper in to_flag:
        flag(repo, dup, keeper, dry_run)

    print(f"done: {len(to_flag)} issue(s) {'would be ' if dry_run else ''}flagged")
    return 0


if __name__ == "__main__":
    sys.exit(main())
