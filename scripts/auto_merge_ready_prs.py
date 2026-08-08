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

Two things about "approved" that are load-bearing here:

- **It usually is not a human.** ``.github/workflows/claude-code-review.yml``
  has the ``ai4c-reviewer`` app submit ``gh pr review --approve``, so for
  agent-authored curation PRs this closes an author → approve → merge loop
  with no human in it. That is the intended operating mode for this repo at
  its curation volume; the human controls are the 3-day delay and assignment.
- **It cannot go stale.** ``main`` has branch protection with
  ``dismiss_stale_reviews: true``, so any push to a PR drops the approval and
  ``reviewDecision`` reverts from APPROVED. The sweep therefore cannot merge a
  commit that was pushed after the review — including a fix pushed by the
  shepherd's own agent step. This script does *not* re-derive that itself; if
  stale-review dismissal is ever turned off, add an explicit check that the
  approving review's commit equals ``headRefOid``.

Eligibility is evaluated in two stages. The list stage applies the criteria
that a bulk ``gh pr list`` can answer; the final stage re-applies all of them
to a freshly fetched per-PR view immediately before merging, so a PR whose
state changed mid-run is not merged on stale data. The split is not just an
optimization; two independent forces require it:

1. GitHub computes mergeability *lazily per PR*, so a bulk list reports
   ``mergeable: UNKNOWN`` for most PRs and only a single-PR query forces the
   computation (which is why ``view_pr`` retries while it is pending).
2. Asking for ``mergeStateStatus`` across hundreds of PRs in one query makes
   GitHub's GraphQL API intermittently return **HTTP 502** — measured on this
   repo at ~200 open PRs. It is therefore in ``VIEW_FIELDS`` only. Keep it out
   of ``LIST_FIELDS``: the list stage never reads it (``evaluate`` returns
   before the merge-state check when ``final=False``), so its only effect
   there is to make the one unguarded call in the script flaky.

The list stage therefore defers the mergeability, merge-state, and status-check
criteria rather than rejecting on them.

Usage::

    python3 scripts/auto_merge_ready_prs.py --repo owner/name --dry-run
    python3 scripts/auto_merge_ready_prs.py --repo owner/name \\
        --min-age-days 3 --summary-file "$GITHUB_STEP_SUMMARY"

Requires the ``gh`` CLI authenticated with a token that can merge (``GH_TOKEN``).
Stdlib only, so it runs even when the workflow's ``uv sync`` step has failed —
hence ``uv run --no-project python`` at both call sites, which skips the project
environment but still guarantees an interpreter at the repo's 3.12 floor instead
of trusting whatever ``python3`` happens to be on PATH.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta

# Fields fetched for the initial scan; a superset is re-fetched per candidate.
# `mergeStateStatus` is deliberately NOT here — see the module docstring.
LIST_FIELDS = (
    "number,title,author,isDraft,createdAt,assignees,reviewDecision,"
    "mergeable,baseRefName,headRefName,url"
)
# headRefOid pins the merge to the exact commit whose checks were evaluated.
VIEW_FIELDS = LIST_FIELDS + ",state,statusCheckRollup,headRefOid,mergeStateStatus"

# Check conclusions that do not count as a failure. SKIPPED/NEUTRAL are how
# conditional workflow jobs report "not applicable to this PR".
PASSING_CONCLUSIONS = frozenset({"SUCCESS", "SKIPPED", "NEUTRAL"})
# Legacy commit-status states (StatusContext rollup entries).
PASSING_STATES = frozenset({"SUCCESS", "EXPECTED", "NEUTRAL"})

# Merge failures that mean "the guards worked" rather than "something is
# broken": the PR moved under us between verification and merge, or somebody
# else got there first. The sweep runs six times a day, so the right response
# is to record a skip and reconsider next run — NOT to fail the workflow and
# page a human about a race that resolved itself correctly.
#
# "Benign" therefore means *assumed transient*. Each run is stateless, so a PR
# that fails this way every time is retried and skipped indefinitely without
# escalating. It stays visible in the step summary's skip list, which is the
# only signal; if a permanently-stuck PR ever needs to escalate, that requires
# cross-run state this script deliberately does not keep.
BENIGN_MERGE_FAILURES = (
    "head branch was modified",  # --match-head-commit fired: a push landed
    "base branch was modified",
    "already merged",
    "not mergeable",
    "pull request is closed",
    "no commits between",
)

# Status glyphs gh prefixes to its stderr lines, stripped for readability.
GH_STATUS_MARKERS = ("X ", "! ", "✓ ")

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


def non_negative_int(value: str) -> int:
    """Parse an age threshold, rejecting negatives.

    A negative threshold would make every PR satisfy the age check — silently
    turning "merge nothing younger than N days" into "merge regardless of
    age". Since this value is settable from a workflow input, a stray `-3`
    must fail loudly rather than widen what gets merged. ``int()`` raising on
    non-numeric input is handled by argparse itself.
    """
    parsed = int(value)
    if parsed < 0:
        raise argparse.ArgumentTypeError(
            f"must be zero or positive, got {parsed}; a negative threshold "
            f"would merge PRs of any age"
        )
    return parsed


def _parse_ts(value: str) -> datetime:
    """Parse a GitHub ISO-8601 timestamp into an aware datetime.

    ``fromisoformat`` handles the trailing ``Z`` natively on the Python this
    project requires (>=3.12), so no offset rewriting is needed.
    """
    return datetime.fromisoformat(value)


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
        # Prefer GitHub's own type tag; fall back to shape for payloads that
        # omit it (older gh versions, hand-built test fixtures).
        typename = entry.get("__typename")
        is_check_run = (
            typename == "CheckRun"
            if typename
            else ("conclusion" in entry or "status" in entry)
        )
        if is_check_run:
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
    # `state` is absent from LIST_FIELDS (the list call already filters to open
    # PRs) but present in VIEW_FIELDS, so in the final stage a missing value
    # means the response was not what we think it was — fail closed.
    state = (pr.get("state") or "").upper()
    if final and not state:
        return Decision(False, "no state in the API response")
    if state and state != "OPEN":
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


def _gh_error(exc: subprocess.CalledProcessError) -> str:
    """Condense a gh failure into one reportable line.

    Take the *first* non-empty line, not the last: when ``gh pr merge`` refuses
    a merge it puts the actionable sentence first and appends ``--auto`` and
    ``--admin`` hint lines, so the last line is advice rather than a diagnosis.
    """
    for line in (exc.stderr or "").splitlines():
        cleaned = line.strip()
        # removeprefix, not lstrip: lstrip takes a character *set*, so it would
        # eat the leading "X" and "-" of a line like "X-Ratelimit is 0".
        for marker in GH_STATUS_MARKERS:
            cleaned = cleaned.removeprefix(marker)
        cleaned = cleaned.strip()
        if cleaned:
            return cleaned
    return f"gh exited {exc.returncode}"


def is_benign_merge_failure(stderr: str) -> bool:
    """True when a failed merge means the PR moved, not that we are broken.

    Matches against the *whole* stderr. gh's refusal messages are multi-line
    and the marker can be on any of them, so classifying on a single extracted
    line silently misses cases — that is how "not mergeable" (the commonest
    benign race) previously ended up reported as a hard failure.
    """
    lowered = stderr.lower()
    return any(marker in lowered for marker in BENIGN_MERGE_FAILURES)


def list_open_prs(repo: str, limit: int, base_branch: str) -> list[dict]:
    out = _gh(
        [
            "pr",
            "list",
            "--repo",
            repo,
            "--state",
            "open",
            "--base",
            base_branch,
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
        # Both fields resolve from the same background computation and either
        # can still read UNKNOWN while it runs, so wait for both — otherwise a
        # PR is skipped as "merge state is unknown" purely for being asked early.
        unresolved = {
            (pr.get("mergeable") or "").upper(),
            (pr.get("mergeStateStatus") or "").upper(),
        }
        if "UNKNOWN" not in unresolved:
            return pr
        if attempt < attempts - 1:
            time.sleep(delay)
    return pr


def merge_pr(repo: str, number: int, min_age_days: int, head_sha: str | None) -> None:
    """Squash-merge one PR, then announce it.

    ``--match-head-commit`` makes GitHub reject the merge if a push landed
    after the verification read, so the commit merged is provably the commit
    whose checks and review state were evaluated.
    """
    merge_cmd = ["pr", "merge", str(number), "--repo", repo, "--squash"]
    if head_sha:
        merge_cmd += ["--match-head-commit", head_sha]
    _gh(merge_cmd)

    # The merge is the operation that matters and it has already succeeded;
    # a failure to post the courtesy comment must not be reported as — or
    # retried as — a failed merge.
    try:
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
    except subprocess.CalledProcessError as exc:
        print(
            f"WARN  #{number}: merged, but posting the comment failed: "
            f"{_gh_error(exc)}",
            file=sys.stderr,
        )


def render_summary(
    merged: list[dict],
    skipped: list[dict],
    failed: list[dict],
    *,
    dry_run: bool = False,
) -> str:
    """Render the run report.

    ``dry_run`` retitles the merged section: a dry run that logs "Merged 3"
    into the step summary leaves a permanent, false audit trail.
    """
    title = "## 🐑 Deterministic auto-merge sweep"
    if dry_run:
        title += " (dry run — nothing was merged)"
    lines = [title, ""]
    verb = "Would merge" if dry_run else "Merged"
    if merged:
        lines.append(f"**{verb} {len(merged)}:**")
        lines += [f"- #{r['number']} — {r['title']}" for r in merged]
    else:
        lines.append(f"**{verb} 0** — nothing met every criterion.")
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
        type=non_negative_int,
        default=3,
        help=(
            "only merge PRs created more than this many days ago "
            "(default: 3; 0 disables the age requirement)"
        ),
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

    now = datetime.now(UTC)
    prs = list_open_prs(args.repo, args.limit, args.base_branch)
    if len(prs) >= args.limit:
        # Silent truncation would look identical to "nothing else was eligible".
        print(
            f"WARNING: hit the --limit of {args.limit} open PRs; older PRs were "
            f"not scanned. Raise --limit.",
            file=sys.stderr,
        )

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
        try:
            fresh = view_pr(args.repo, number)
        except subprocess.CalledProcessError as exc:
            # One unreadable PR must not abandon the candidates behind it.
            reason = f"could not re-verify: {_gh_error(exc)}"
            print(f"SKIP  #{number}: {reason}", file=sys.stderr)
            skipped.append({"number": number, "reason": reason})
            continue
        decision = evaluate(
            fresh,
            now=datetime.now(UTC),
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
            merge_pr(args.repo, number, args.min_age_days, fresh.get("headRefOid"))
        except subprocess.CalledProcessError as exc:
            reason = _gh_error(exc)
            # Classify on the full stderr, report the condensed line.
            if is_benign_merge_failure(exc.stderr or reason):
                # The PR moved between verification and merge. That is the
                # guard working; next run reconsiders it.
                print(f"SKIP  #{number}: {reason}")
                skipped.append({"number": number, "reason": reason})
            else:
                print(f"FAIL  #{number}: {reason}", file=sys.stderr)
                failed.append({"number": number, "reason": reason})
            continue
        print(f"MERGED #{number}: {fresh['title']}")
        merged.append({"number": number, "title": fresh["title"]})

    report = render_summary(merged, skipped, failed, dry_run=args.dry_run)
    print()
    print(report)
    if args.summary_file:
        with open(args.summary_file, "a", encoding="utf-8") as handle:
            handle.write(report)

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
