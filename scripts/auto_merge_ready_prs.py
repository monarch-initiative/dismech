#!/usr/bin/env python3
"""Deterministically squash-merge pull requests that are ready by every signal.

This is the closing step of the ``pr-shepherd`` workflow. The shepherd's main
step is an LLM agent that *judges* stuck PRs; this step deliberately does not
judge anything. It applies a fixed predicate to GitHub-reported state and
merges what passes, so the outcome of a run is reproducible from the API
response alone.

A PR is merged only when ALL of these hold:

- open, not a draft, and targeting the expected base branch (``main``)
- **unassigned** — ``assignees`` is empty
- **reviewer approved** — ``reviewDecision == "APPROVED"``
- **no conflicts** — ``mergeable == "MERGEABLE"``
- **green** — ``mergeStateStatus == "CLEAN"`` (GitHub's own "nothing is
  blocking this merge": required checks satisfied, branch not behind, no
  unresolved protection rule)
- **tests passing** — the head commit's status-check rollup has at least one
  SUCCESS and nothing failing, cancelled, or still running. This is stricter
  than ``CLEAN``, which only accounts for *required* checks: a failing
  non-required check also blocks the merge here.
- **older than N days** (default 3), measured from ``createdAt``

Anything else — including ``mergeable == "UNKNOWN"`` once GitHub has had its
chance to compute mergeability — is skipped with a recorded reason. Skipping is
always safe: the workflow runs every 4 hours and will reconsider the PR.

Escape hatch: **assign the PR to someone.** The unassigned criterion is the
per-PR veto — an assigned PR is somebody's active work and is never merged
here. Requesting changes and converting to draft also block the merge.

Eligibility is evaluated in two stages. The list stage applies the criteria
that a bulk ``gh pr list`` can answer; the final stage re-applies all of them
to a freshly fetched per-PR view immediately before merging, so a PR whose
state changed mid-run is not merged on stale data. The split is not just an
optimization: GitHub computes mergeability *lazily per PR*, so a bulk list
reports ``mergeable: UNKNOWN`` for most PRs and only a single-PR query forces
the computation (which is why ``view_pr`` retries while it is pending). The
list stage therefore defers the mergeability, merge-state, and status-check
criteria rather than rejecting on them.

Usage::

    python3 scripts/auto_merge_ready_prs.py --repo owner/name --dry-run
    python3 scripts/auto_merge_ready_prs.py --repo owner/name \\
        --min-age-days 3 --summary-file "$GITHUB_STEP_SUMMARY"

Requires the ``gh`` CLI authenticated with a token that can merge (``GH_TOKEN``).
Stdlib only, so it runs even when the workflow's ``uv sync`` step has failed.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

# Fields fetched for the initial scan; a superset is re-fetched per candidate.
LIST_FIELDS = (
    "number,title,author,isDraft,createdAt,assignees,reviewDecision,"
    "mergeable,mergeStateStatus,baseRefName,headRefName,url"
)
VIEW_FIELDS = LIST_FIELDS + ",state,statusCheckRollup"

# Check conclusions that do not count as a failure. SKIPPED/NEUTRAL are how
# conditional workflow jobs report "not applicable to this PR".
PASSING_CONCLUSIONS = frozenset({"SUCCESS", "SKIPPED", "NEUTRAL"})
# Legacy commit-status states (StatusContext rollup entries).
PASSING_STATES = frozenset({"SUCCESS", "EXPECTED", "NEUTRAL"})

MERGE_COMMENT = (
    "🐑 **PR Shepherd** (deterministic sweep) — Squash-merged: approved, "
    "unassigned, no conflicts, all checks green, and open longer than "
    "{days} days. No further action needed."
)


# A PR that is merely too young needs no attention — it becomes eligible on its
# own — so it is filtered out of the near-miss report rather than shown as a
# skip. Every other reason describes something a human may want to look at.
TOO_YOUNG = "too_young"


@dataclass(frozen=True)
class Decision:
    """Outcome of applying the predicate to one PR."""

    eligible: bool
    reason: str
    code: str = ""


def _parse_ts(value: str) -> datetime:
    """Parse a GitHub ISO-8601 timestamp into an aware datetime."""
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def check_rollup_decision(rollup: list[dict] | None) -> Decision:
    """Classify a PR's status-check rollup.

    ``rollup`` mixes two shapes: ``CheckRun`` entries (``status`` +
    ``conclusion``) and ``StatusContext`` entries (``state``).
    """
    if not rollup:
        return Decision(False, "no status checks reported on the head commit")

    pending: list[str] = []
    failing: list[str] = []
    successes = 0

    for entry in rollup:
        name = entry.get("name") or entry.get("context") or "(unnamed check)"
        if "conclusion" in entry or "status" in entry:
            status = (entry.get("status") or "").upper()
            conclusion = (entry.get("conclusion") or "").upper()
            if status != "COMPLETED" or not conclusion:
                pending.append(name)
            elif conclusion in PASSING_CONCLUSIONS:
                if conclusion == "SUCCESS":
                    successes += 1
            else:
                failing.append(f"{name}={conclusion.lower()}")
        else:
            state = (entry.get("state") or "").upper()
            if state == "PENDING" or not state:
                pending.append(name)
            elif state in PASSING_STATES:
                if state == "SUCCESS":
                    successes += 1
            else:
                failing.append(f"{name}={state.lower()}")

    if failing:
        return Decision(False, "checks not passing: " + ", ".join(sorted(failing)))
    if pending:
        return Decision(False, "checks still running: " + ", ".join(sorted(pending)))
    if not successes:
        return Decision(False, "no successful check on the head commit")
    return Decision(True, f"{successes} check(s) passing")


def evaluate(
    pr: dict,
    *,
    now: datetime,
    min_age_days: int,
    base_branch: str,
    final: bool = True,
) -> Decision:
    """Apply the merge predicate to one PR payload.

    With ``final=False`` (the cheap list pass) the criteria a bulk list cannot
    answer yet — mergeability, merge state, and the status-check rollup — are
    deferred rather than treated as failures. Only the ``final`` pass, run
    against a single-PR view, can decide those, and only that pass gates a
    merge.
    """
    state = (pr.get("state") or "OPEN").upper()
    if state != "OPEN":
        return Decision(False, f"not open (state={state.lower()})")
    if pr.get("isDraft"):
        return Decision(False, "draft")
    if pr.get("baseRefName") != base_branch:
        return Decision(
            False, f"base branch is {pr.get('baseRefName')!r}, not {base_branch!r}"
        )
    assignees = pr.get("assignees") or []
    if assignees:
        logins = ", ".join(a.get("login", "?") for a in assignees)
        return Decision(False, f"assigned to {logins}")
    review = (pr.get("reviewDecision") or "").upper()
    if review != "APPROVED":
        return Decision(
            False, f"review decision is {review.lower() or 'none'}, not approved"
        )
    created = _parse_ts(pr["createdAt"])
    age = now - created
    if age < timedelta(days=min_age_days):
        hours = age.total_seconds() / 3600
        return Decision(False, f"only {hours:.0f}h old (<{min_age_days}d)", TOO_YOUNG)

    # A conflict IS reported reliably in bulk, so reject it in either stage
    # rather than spending a per-PR round trip on it.
    mergeable = (pr.get("mergeable") or "").upper()
    if mergeable == "CONFLICTING":
        return Decision(False, "merge conflicts with the base branch")

    if not final:
        # Mergeability and checks are unresolved in a bulk list; defer them.
        return Decision(True, "candidate (pending per-PR verification)")

    if mergeable != "MERGEABLE":
        return Decision(False, f"mergeability is {mergeable.lower() or 'unset'}")
    merge_state = (pr.get("mergeStateStatus") or "").upper()
    if merge_state != "CLEAN":
        return Decision(
            False, f"merge state is {merge_state.lower() or 'unset'}, not clean"
        )

    checks = check_rollup_decision(pr.get("statusCheckRollup"))
    if not checks.eligible:
        return checks

    return Decision(True, f"ready ({age.days}d old)")


def _gh(args: list[str]) -> str:
    """Run a gh command and return stdout, raising on failure."""
    result = subprocess.run(["gh", *args], check=True, capture_output=True, text=True)
    return result.stdout


def list_open_prs(repo: str, limit: int) -> list[dict]:
    out = _gh(
        [
            "pr",
            "list",
            "--repo",
            repo,
            "--state",
            "open",
            "--limit",
            str(limit),
            "--json",
            LIST_FIELDS,
        ]
    )
    return json.loads(out)


def view_pr(repo: str, number: int, *, attempts: int = 3, delay: float = 2.0) -> dict:
    """Fetch one PR, waiting for GitHub to finish computing mergeability.

    Requesting a single PR is what *triggers* the background mergeability
    computation, so the first response often still says ``UNKNOWN``. Retry a
    couple of times before giving up; an unresolved PR is skipped, not merged.
    """
    pr: dict = {}
    for attempt in range(attempts):
        pr = json.loads(
            _gh(["pr", "view", str(number), "--repo", repo, "--json", VIEW_FIELDS])
        )
        if (pr.get("mergeable") or "").upper() != "UNKNOWN":
            return pr
        if attempt < attempts - 1:
            time.sleep(delay)
    return pr


def merge_pr(repo: str, number: int, min_age_days: int) -> None:
    _gh(["pr", "merge", str(number), "--repo", repo, "--squash"])
    _gh(
        [
            "pr",
            "comment",
            str(number),
            "--repo",
            repo,
            "--body",
            MERGE_COMMENT.format(days=min_age_days),
        ]
    )


def render_summary(merged: list[dict], skipped: list[dict], failed: list[dict]) -> str:
    lines = ["## 🐑 Deterministic auto-merge sweep", ""]
    if merged:
        lines.append(f"**Merged {len(merged)}:**")
        lines += [f"- #{r['number']} — {r['title']}" for r in merged]
    else:
        lines.append("**Merged 0** — nothing met every criterion.")
    lines.append("")
    if failed:
        lines.append(f"**Failed to merge {len(failed)}:**")
        lines += [f"- #{r['number']} — {r['reason']}" for r in failed]
        lines.append("")
    if skipped:
        lines.append(
            f"<details><summary>Skipped {len(skipped)} near-miss PR(s)</summary>"
        )
        lines.append("")
        lines += [f"- #{r['number']} — {r['reason']}" for r in skipped]
        lines.append("")
        lines.append("</details>")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repo", required=True, help="owner/name of the repository")
    parser.add_argument(
        "--min-age-days",
        type=int,
        default=3,
        help="only merge PRs created more than this many days ago (default: 3)",
    )
    parser.add_argument(
        "--base-branch",
        default="main",
        help="only merge PRs targeting this base branch (default: main)",
    )
    parser.add_argument(
        "--limit", type=int, default=300, help="max open PRs to scan (default: 300)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="report what would be merged without merging or commenting",
    )
    parser.add_argument(
        "--summary-file",
        default=os.environ.get("GITHUB_STEP_SUMMARY"),
        help="append a markdown report here (default: $GITHUB_STEP_SUMMARY)",
    )
    args = parser.parse_args(argv)

    now = datetime.now(timezone.utc)
    prs = list_open_prs(args.repo, args.limit)

    candidates: list[dict] = []
    skipped: list[dict] = []
    for pr in prs:
        decision = evaluate(
            pr,
            now=now,
            min_age_days=args.min_age_days,
            base_branch=args.base_branch,
            final=False,
        )
        if decision.eligible:
            candidates.append(pr)
        elif (
            pr.get("reviewDecision") or ""
        ).upper() == "APPROVED" and decision.code != TOO_YOUNG:
            # Report near-misses only. An unapproved PR is not this step's
            # business, and a too-young one needs nothing from anybody.
            skipped.append({"number": pr["number"], "reason": decision.reason})

    print(
        f"Scanned {len(prs)} open PR(s); {len(candidates)} passed the list-level predicate."
    )

    merged: list[dict] = []
    failed: list[dict] = []
    for pr in candidates:
        number = pr["number"]
        fresh = view_pr(args.repo, number)
        decision = evaluate(
            fresh,
            now=datetime.now(timezone.utc),
            min_age_days=args.min_age_days,
            base_branch=args.base_branch,
        )
        if not decision.eligible:
            print(f"SKIP  #{number}: {decision.reason}")
            skipped.append({"number": number, "reason": decision.reason})
            continue
        if args.dry_run:
            print(
                f"DRY-RUN would merge #{number}: {fresh['title']} — {decision.reason}"
            )
            merged.append({"number": number, "title": fresh["title"]})
            continue
        try:
            merge_pr(args.repo, number, args.min_age_days)
        except subprocess.CalledProcessError as exc:
            reason = (
                (exc.stderr or "").strip().splitlines()[-1]
                if exc.stderr
                else "gh error"
            )
            print(f"FAIL  #{number}: {reason}", file=sys.stderr)
            failed.append({"number": number, "reason": reason})
            continue
        print(f"MERGED #{number}: {fresh['title']}")
        merged.append({"number": number, "title": fresh["title"]})

    report = render_summary(merged, skipped, failed)
    print()
    print(report)
    if args.summary_file:
        with open(args.summary_file, "a", encoding="utf-8") as handle:
            handle.write(report)

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
