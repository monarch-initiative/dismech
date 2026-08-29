#!/usr/bin/env python3
"""Deterministically squash-merge pull requests that are ready by every signal.

This runs in the ``pr-shepherd`` workflow's fresh closing job, isolated from the
LLM runner. The shepherd agent *judges* stuck PRs; this controller deliberately
does not. It applies a fixed predicate to GitHub-reported state and merges what
passes, so the outcome of a run is reproducible from the API response alone.

A PR is merged only when ALL of these hold:

- open and targeting the expected base branch (``main``); a draft is treated as
  queue metadata and promoted immediately before the final verification
- **unassigned** — ``assignees`` is empty
- **reviewer approved** — ``reviewDecision == "APPROVED"``
- **no conflicts** — ``mergeable == "MERGEABLE"``
- **green** — ``mergeStateStatus == "CLEAN"`` (GitHub's configured protection
  rules are satisfied). Because required checks are non-strict, this alone does
  *not* prove the branch includes current main; an explicit compare does that
  below.
- **tests passing** — the head commit's status-check rollup has at least one
  SUCCESS and nothing failing, cancelled, or still running. This is stricter
  than ``CLEAN``, which only accounts for *required* checks: a failing
  non-required check also blocks the merge here.
- **older than N days** (default 3), measured from ``createdAt``
- the required GitHub Actions-owned health check succeeded on the exact current
  base SHA, GitHub's compare API proves that SHA is an ancestor of the PR head,
  and the base remains current after the final PR-state read
- the head branch is not in a separately managed ``auto/`` lane

Anything else — including ``mergeable == "UNKNOWN"`` once GitHub has had its
chance to compute mergeability — is skipped with a recorded reason. Skipping is
always safe: the workflow runs hourly and will reconsider the PR.

Escape hatch: **assign the PR to someone.** The unassigned criterion is the
per-PR veto — an assigned PR is somebody's active work and is never merged
here. Requesting changes also blocks the merge. Draft state deliberately does
not: opening a PR places it in DisMech's review queue.

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
criteria rather than rejecting on them. Immediately before merging, the
controller checks the required status on current main, performs a final PR read,
and proves main still has that healthy SHA. It merges at most one PR per run, so
serialization does not depend on GitHub immediately exposing the post-merge SHA.
GitHub can atomically pin the expected PR head but offers no expected-base field;
strict branch protection or a merge queue is required to eliminate the final
narrow race after the last base read.

Usage::

    python3 scripts/auto_merge_ready_prs.py --repo owner/name --dry-run
    python3 scripts/auto_merge_ready_prs.py --repo owner/name \\
        --min-age-days 3 --summary-file "$GITHUB_STEP_SUMMARY"
    python3 scripts/auto_merge_ready_prs.py --repo owner/name --specific-pr 123

Requires Python 3.12+ and the ``gh`` CLI. Discovery subprocesses use
``GH_TOKEN``; execution additionally requires ``GH_MERGE_TOKEN``, which the
fixed controller passes only to its write subprocesses. The script is stdlib
only and does not need the project environment.
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
from urllib.parse import quote

# Fields fetched for the initial scan; a superset is re-fetched per candidate.
# `mergeStateStatus` is deliberately NOT here — see the module docstring.
LIST_FIELDS = (
    "number,title,author,isDraft,createdAt,assignees,reviewDecision,"
    "mergeable,baseRefName,headRefName,url"
)
# headRefOid pins the reviewed head and is compared against the exact healthy
# current-main SHA before merge. `baseRefOid` is intentionally absent: GitHub's
# field is the PR's associated base-ref OID, not proof that the head contains it.
VIEW_FIELDS = LIST_FIELDS + ",state,statusCheckRollup,headRefOid,mergeStateStatus"

# Check conclusions that do not count as a failure. SKIPPED/NEUTRAL are how
# conditional workflow jobs report "not applicable to this PR".
PASSING_CONCLUSIONS = frozenset({"SUCCESS", "SKIPPED", "NEUTRAL"})
# Legacy commit-status states (StatusContext rollup entries).
PASSING_STATES = frozenset({"SUCCESS", "EXPECTED", "NEUTRAL"})

# Merge failures that mean "the guards worked" rather than "something is
# broken": the PR moved under us between verification and merge, or somebody
# else got there first. The sweep runs hourly, so the right response
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

DEFAULT_BASE_HEALTH_CHECK = "test (3.13)"
DEFAULT_BASE_HEALTH_APP_ID = 15368  # GitHub Actions, matching branch protection
AUTOMATED_HEAD_PREFIX = "auto/"


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


@dataclass(frozen=True)
class BaseHealth:
    """Health of the exact current base-branch commit."""

    healthy: bool
    sha: str
    reason: str


def base_alignment_decision(
    comparison: dict, healthy_base_sha: str, head_sha: str
) -> Decision:
    """Require GitHub's comparison to prove current base is in the PR head."""
    expected = healthy_base_sha.strip()
    head = head_sha.strip()
    if not expected:
        return Decision(False, "current healthy base SHA is missing")
    if not head:
        return Decision(False, "PR response returned no head SHA")
    if not isinstance(comparison, dict):
        return Decision(False, "GitHub comparison response was not an object")

    compared_base = str((comparison.get("base_commit") or {}).get("sha") or "")
    merge_base = str((comparison.get("merge_base_commit") or {}).get("sha") or "")
    try:
        behind_by = int(comparison["behind_by"])
    except (KeyError, TypeError, ValueError):
        return Decision(False, "GitHub comparison returned no valid behind count")

    if compared_base.casefold() != expected.casefold():
        return Decision(False, "GitHub comparison returned the wrong base commit")
    if merge_base.casefold() != expected.casefold() or behind_by != 0:
        return Decision(
            False,
            f"PR head {head[:12]} does not contain current healthy base "
            f"{expected[:12]} (merge base {merge_base[:12] or 'missing'}, "
            f"behind by {behind_by})",
        )
    return Decision(True, f"PR head contains healthy base {expected[:12]}")


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
    include_drafts: bool = True,
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
    if pr.get("isDraft") and not include_drafts:
        return Decision(False, "draft")
    if pr.get("baseRefName") != base_branch:
        return Decision(
            False, f"base branch is {pr.get('baseRefName')!r}, not {base_branch!r}"
        )
    head_ref = str(pr.get("headRefName") or "")
    if head_ref.startswith(AUTOMATED_HEAD_PREFIX):
        return Decision(False, "head branch is in separately managed lane 'auto/'")
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
    draft_preflight_state = (
        bool(pr.get("isDraft"))
        and include_drafts
        and merge_state in {"BLOCKED", "DRAFT"}
    )
    if merge_state != "CLEAN" and not draft_preflight_state:
        return Decision(
            False, f"merge state is {merge_state.lower() or 'unset'}, not clean"
        )

    checks = check_rollup_decision(pr.get("statusCheckRollup"))
    if not checks.eligible:
        return checks

    return Decision(True, f"ready ({age.days}d old)")


def _gh(args: list[str], *, token: str | None = None) -> str:
    """Run ``gh`` without exposing the dedicated writer to discovery calls."""
    env = os.environ.copy()
    env.pop("GH_MERGE_TOKEN", None)
    if token is not None:
        env["GH_TOKEN"] = token
    result = subprocess.run(
        ["gh", *args], check=True, capture_output=True, text=True, env=env
    )
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


def main_health_decision(
    base_sha: str,
    check_runs: list[dict] | None,
    required_check: str,
    required_app_id: int = DEFAULT_BASE_HEALTH_APP_ID,
) -> BaseHealth:
    """Require the latest named check to pass on exactly ``base_sha``."""
    sha = base_sha.strip()
    if not sha:
        return BaseHealth(False, "", "base branch returned no head SHA")

    matches = [
        run
        for run in check_runs or []
        if str(run.get("name") or "") == required_check
        and str(run.get("head_sha") or "").casefold() == sha.casefold()
        and int((run.get("app") or {}).get("id") or 0) == required_app_id
    ]
    if not matches:
        return BaseHealth(
            False,
            sha,
            f"{required_check!r} has not reported on current base {sha[:12]}",
        )

    # Reruns can leave more than one check with the same name on one SHA. IDs
    # are monotonically increasing; the newest attempt is authoritative.
    latest = max(matches, key=lambda run: int(run.get("id") or 0))
    status = str(latest.get("status") or "").casefold()
    conclusion = str(latest.get("conclusion") or "").casefold()
    if status != "completed":
        return BaseHealth(
            False,
            sha,
            f"{required_check!r} on current base {sha[:12]} is {status or 'pending'}",
        )
    if conclusion != "success":
        return BaseHealth(
            False,
            sha,
            f"{required_check!r} on current base {sha[:12]} concluded "
            f"{conclusion or 'without a result'}",
        )
    return BaseHealth(
        True,
        sha,
        f"{required_check!r} passed on current base {sha[:12]}",
    )


def get_base_sha(repo: str, base_branch: str) -> str:
    """Read the current head SHA of ``base_branch`` from GitHub."""
    branch = json.loads(
        _gh(["api", f"repos/{repo}/branches/{quote(base_branch, safe='')}"])
    )
    sha = str((branch.get("commit") or {}).get("sha") or "")
    if not sha:
        raise ValueError("base branch response returned no head SHA")
    return sha


def get_base_alignment(repo: str, base_sha: str, head_sha: str) -> Decision:
    """Ask GitHub whether ``head_sha`` actually contains ``base_sha``.

    ``baseRefOid`` cannot answer this: it identifies the PR's associated base
    ref, which may be newer than the branch's real merge base. The compare API
    returns the graph relationship for the two exact commits.
    """
    base = base_sha.strip()
    head = head_sha.strip()
    if not base or not head:
        return base_alignment_decision({}, base, head)
    comparison_url = (
        f"repos/{repo}/compare/{quote(base, safe='')}...{quote(head, safe='')}"
    )
    comparison = json.loads(_gh(["api", comparison_url]))
    return base_alignment_decision(comparison, base, head)


def get_base_health(
    repo: str,
    base_branch: str,
    required_check: str,
    required_app_id: int = DEFAULT_BASE_HEALTH_APP_ID,
) -> BaseHealth:
    """Read the exact base head and its latest check runs from GitHub."""
    sha = get_base_sha(repo, base_branch)
    check_runs_url = (
        f"repos/{repo}/commits/{sha}/check-runs?filter=latest"
        f"&check_name={quote(required_check, safe='')}&per_page=100"
    )
    checks = json.loads(_gh(["api", check_runs_url]))
    return main_health_decision(
        sha, checks.get("check_runs"), required_check, required_app_id
    )


def is_benign_merge_failure(stderr: str) -> bool:
    """True when a failed merge means the PR moved, not that we are broken.

    Matches against the *whole* stderr. gh's refusal messages are multi-line
    and the marker can be on any of them, so classifying on a single extracted
    line silently misses cases — that is how "not mergeable" (the commonest
    benign race) previously ended up reported as a hard failure.
    """
    lowered = stderr.lower()
    return any(marker in lowered for marker in BENIGN_MERGE_FAILURES)


def is_pr_gone_merge_failure(stderr: str) -> bool:
    """Return whether a merge race left no open PR whose draft state can restore."""
    lowered = stderr.lower()
    return any(
        marker in lowered for marker in ("already merged", "pull request is closed")
    )


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


def view_pr(
    repo: str,
    number: int,
    *,
    attempts: int = 3,
    delay: float = 2.0,
    expected_draft: bool | None = None,
) -> dict:
    """Fetch one PR, waiting for GitHub to expose expected computed state.

    Requesting a single PR is what *triggers* the background mergeability
    computation, so the first response often still says ``UNKNOWN``. Retry a
    couple of times before giving up. ``expected_draft`` also covers the short
    GraphQL read-after-write lag following ``gh pr ready``. An unresolved or
    stale response is returned after the attempt budget and then fails closed.
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
        draft_state_pending = (
            expected_draft is not None and bool(pr.get("isDraft")) != expected_draft
        )
        if "UNKNOWN" not in unresolved and not draft_state_pending:
            return pr
        if attempt < attempts - 1:
            time.sleep(delay)
    return pr


def merge_pr(
    repo: str,
    number: int,
    min_age_days: int,
    head_sha: str | None,
    write_token: str,
) -> None:
    """Squash-merge one PR, then announce it.

    ``--match-head-commit`` makes GitHub reject the merge if a push landed
    after the verification read, so the commit merged is provably the commit
    whose checks and review state were evaluated.
    """
    verified_head = str(head_sha or "").strip()
    if not verified_head:
        raise ValueError("refusing to merge without a verified head commit SHA")
    writer = write_token.strip()
    if not writer:
        raise ValueError("refusing to merge without a dedicated write token")
    merge_cmd = [
        "pr",
        "merge",
        str(number),
        "--repo",
        repo,
        "--squash",
        "--match-head-commit",
        verified_head,
    ]
    _gh(merge_cmd, token=writer)

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
            ],
            token=writer,
        )
    except subprocess.CalledProcessError as exc:
        print(
            f"WARN  #{number}: merged, but posting the comment failed: "
            f"{_gh_error(exc)}",
            file=sys.stderr,
        )


def mark_pr_ready(repo: str, number: int, write_token: str) -> None:
    """Convert a verified draft immediately before the final guard pass."""
    writer = write_token.strip()
    if not writer:
        raise ValueError("refusing to mark a draft ready without a write token")
    _gh(["pr", "ready", str(number), "--repo", repo], token=writer)


def mark_pr_draft(repo: str, number: int, write_token: str) -> None:
    """Restore draft state when a just-in-time promotion does not merge."""
    writer = write_token.strip()
    if not writer:
        raise ValueError("refusing to restore draft state without a write token")
    _gh(["pr", "ready", str(number), "--repo", repo, "--undo"], token=writer)


def render_summary(
    merged: list[dict],
    skipped: list[dict],
    failed: list[dict],
    *,
    dry_run: bool = False,
    circuit_open: str | None = None,
) -> str:
    """Render the run report.

    ``dry_run`` retitles the merged section: a dry run that logs "Merged 3"
    into the step summary leaves a permanent, false audit trail.
    """
    title = "## 🐑 Deterministic auto-merge sweep"
    if dry_run:
        title += " (dry run — nothing was merged)"
    lines = [title, ""]
    if circuit_open:
        lines.extend([f"**Main-health circuit open:** {circuit_open}", ""])
    verb = "Would merge" if dry_run else "Merged"
    if merged:
        lines.append(f"**{verb} {len(merged)}:**")
        lines += [
            f"- #{row['number']} — {row['title']}"
            + (f" ({row['action']})" if row.get("action") else "")
            for row in merged
        ]
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
        "--base-health-check",
        default=DEFAULT_BASE_HEALTH_CHECK,
        help=(
            "check that must pass on the exact current base SHA before every merge "
            f"(default: {DEFAULT_BASE_HEALTH_CHECK!r})"
        ),
    )
    parser.add_argument(
        "--base-health-app-id",
        type=int,
        default=DEFAULT_BASE_HEALTH_APP_ID,
        help=(
            "GitHub App ID that must own the base health check "
            f"(default: {DEFAULT_BASE_HEALTH_APP_ID})"
        ),
    )
    parser.add_argument(
        "--limit", type=int, default=300, help="max open PRs to scan (default: 300)"
    )
    parser.add_argument(
        "--specific-pr",
        type=int,
        help="evaluate only this PR instead of scanning all open PRs",
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
    write_token = os.environ.get("GH_MERGE_TOKEN", "").strip()
    if not args.dry_run and not write_token:
        parser.error("merge execution requires a non-empty GH_MERGE_TOKEN")

    now = datetime.now(UTC)
    if args.specific_pr is not None:
        try:
            prs = [view_pr(args.repo, args.specific_pr)]
        except subprocess.CalledProcessError as exc:
            print(
                f"ERROR: could not read specific PR #{args.specific_pr}: {_gh_error(exc)}",
                file=sys.stderr,
            )
            return 1
    else:
        prs = list_open_prs(args.repo, args.limit, args.base_branch)
    if args.specific_pr is None and len(prs) >= args.limit:
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
        elif args.specific_pr is not None or (
            (pr.get("reviewDecision") or "").upper() == "APPROVED"
            and decision.code != TOO_YOUNG
        ):
            # Report near-misses only. An unapproved PR is not this step's
            # business, and a too-young one needs nothing from anybody. An
            # explicitly requested PR is the exception: always say why it did
            # not qualify so a targeted dispatch is diagnostically useful.
            skipped.append({"number": pr["number"], "reason": decision.reason})

    print(
        f"Scanned {len(prs)} open PR(s); {len(candidates)} passed the list-level predicate."
    )

    # Oldest first is deterministic and honors the standing human-review window.
    candidates.sort(key=lambda pr: (_parse_ts(pr["createdAt"]), int(pr["number"])))

    merged: list[dict] = []
    failed: list[dict] = []
    circuit_open: str | None = None
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

        # Check the exact current base immediately before any write. After one
        # merge, main points at an untested commit, so the next candidate opens
        # the circuit until that new push build succeeds.
        try:
            health = get_base_health(
                args.repo,
                args.base_branch,
                args.base_health_check,
                args.base_health_app_id,
            )
        except (subprocess.CalledProcessError, ValueError, json.JSONDecodeError) as exc:
            detail = (
                _gh_error(exc)
                if isinstance(exc, subprocess.CalledProcessError)
                else str(exc)
            )
            circuit_open = f"could not verify current base health: {detail}"
            print(f"FAIL  circuit: {circuit_open}", file=sys.stderr)
            failed.append({"number": number, "reason": circuit_open})
            break
        if not health.healthy:
            circuit_open = health.reason
            # A red, pending, or not-yet-observed base is repository state, not
            # a controller malfunction. Keep the workflow green while making
            # the fail-closed stop prominent in stdout and the step summary.
            print(f"STOP  main-health circuit: {circuit_open}")
            break
        was_draft = bool(fresh.get("isDraft"))
        # Avoid a visible ready/draft flip for a branch that cannot pass the
        # final ancestry guard. Non-drafts wait for the load-bearing comparison
        # after the final PR read below.
        if was_draft:
            try:
                alignment = get_base_alignment(
                    args.repo, health.sha, str(fresh.get("headRefOid") or "")
                )
            except (
                subprocess.CalledProcessError,
                ValueError,
                json.JSONDecodeError,
            ) as exc:
                detail = (
                    _gh_error(exc)
                    if isinstance(exc, subprocess.CalledProcessError)
                    else str(exc)
                )
                reason = f"could not verify PR ancestry: {detail}"
                print(f"SKIP  #{number}: {reason}", file=sys.stderr)
                skipped.append({"number": number, "reason": reason})
                continue
            if not alignment.eligible:
                print(f"SKIP  #{number}: {alignment.reason}")
                skipped.append({"number": number, "reason": alignment.reason})
                continue

        ready_transition_succeeded = False
        merge_completed = False
        pr_gone = False
        try:
            if was_draft and not args.dry_run:
                try:
                    mark_pr_ready(args.repo, number, write_token)
                    ready_transition_succeeded = True
                except (subprocess.CalledProcessError, ValueError) as exc:
                    detail = (
                        _gh_error(exc)
                        if isinstance(exc, subprocess.CalledProcessError)
                        else str(exc)
                    )
                    reason = f"could not mark verified draft ready: {detail}"
                    print(f"FAIL  #{number}: {reason}", file=sys.stderr)
                    failed.append({"number": number, "reason": reason})
                    continue

                # The transition took time and emitted an event. Re-establish
                # base health before the final PR-state read.
                try:
                    health = get_base_health(
                        args.repo,
                        args.base_branch,
                        args.base_health_check,
                        args.base_health_app_id,
                    )
                except (
                    subprocess.CalledProcessError,
                    ValueError,
                    json.JSONDecodeError,
                ) as exc:
                    detail = (
                        _gh_error(exc)
                        if isinstance(exc, subprocess.CalledProcessError)
                        else str(exc)
                    )
                    circuit_open = f"could not re-verify current base health: {detail}"
                    print(f"FAIL  circuit: {circuit_open}", file=sys.stderr)
                    failed.append({"number": number, "reason": circuit_open})
                    break
                if not health.healthy:
                    circuit_open = health.reason
                    print(f"STOP  main-health circuit: {circuit_open}")
                    break

            # This is the load-bearing PR read for both drafts and non-drafts:
            # it occurs after the successful base-health lookup and immediately
            # before the final base-SHA comparison and head-pinned merge.
            try:
                fresh = view_pr(
                    args.repo,
                    number,
                    expected_draft=False if ready_transition_succeeded else None,
                )
            except (subprocess.CalledProcessError, ValueError) as exc:
                detail = (
                    _gh_error(exc)
                    if isinstance(exc, subprocess.CalledProcessError)
                    else str(exc)
                )
                reason = f"could not perform final PR verification: {detail}"
                print(f"FAIL  #{number}: {reason}", file=sys.stderr)
                failed.append({"number": number, "reason": reason})
                continue
            decision = evaluate(
                fresh,
                now=datetime.now(UTC),
                min_age_days=args.min_age_days,
                base_branch=args.base_branch,
                include_drafts=args.dry_run,
            )
            if not decision.eligible:
                phase = "after ready" if ready_transition_succeeded else "before merge"
                reason = f"state changed {phase}: {decision.reason}"
                print(f"SKIP  #{number}: {reason}")
                skipped.append({"number": number, "reason": reason})
                continue
            try:
                alignment = get_base_alignment(
                    args.repo, health.sha, str(fresh.get("headRefOid") or "")
                )
            except (
                subprocess.CalledProcessError,
                ValueError,
                json.JSONDecodeError,
            ) as exc:
                detail = (
                    _gh_error(exc)
                    if isinstance(exc, subprocess.CalledProcessError)
                    else str(exc)
                )
                reason = f"could not perform final ancestry verification: {detail}"
                print(f"SKIP  #{number}: {reason}", file=sys.stderr)
                skipped.append({"number": number, "reason": reason})
                continue
            if not alignment.eligible:
                reason = f"state changed before merge: {alignment.reason}"
                print(f"SKIP  #{number}: {reason}")
                skipped.append({"number": number, "reason": reason})
                continue

            # GitHub's merge API can pin the PR head but has no expected-base
            # argument. Minimize that residual race by proving main still has
            # the exact healthy SHA after the final PR-state read.
            try:
                current_base_sha = get_base_sha(args.repo, args.base_branch)
            except (subprocess.CalledProcessError, ValueError) as exc:
                detail = (
                    _gh_error(exc)
                    if isinstance(exc, subprocess.CalledProcessError)
                    else str(exc)
                )
                circuit_open = f"could not perform final base verification: {detail}"
                print(f"FAIL  circuit: {circuit_open}", file=sys.stderr)
                failed.append({"number": number, "reason": circuit_open})
                break
            if current_base_sha.casefold() != health.sha.casefold():
                circuit_open = (
                    "base changed after its health check "
                    f"({health.sha[:12]} -> {current_base_sha[:12]}); no merge attempted"
                )
                print(f"STOP  main-health circuit: {circuit_open}")
                break

            if args.dry_run:
                action = "mark ready and merge" if was_draft else "merge"
                print(
                    f"DRY-RUN would {action} #{number}: {fresh['title']} — "
                    f"{decision.reason}"
                )
                merged.append(
                    {"number": number, "title": fresh["title"], "action": action}
                )
                print(
                    "STOP  one-merge safety limit reached; remaining PRs would "
                    "wait for the next run"
                )
                break

            try:
                merge_pr(
                    args.repo,
                    number,
                    args.min_age_days,
                    fresh.get("headRefOid"),
                    write_token,
                )
                merge_completed = True
            except (subprocess.CalledProcessError, ValueError) as exc:
                reason = (
                    _gh_error(exc)
                    if isinstance(exc, subprocess.CalledProcessError)
                    else str(exc)
                )
                # Classify on the full stderr, report the condensed line.
                if isinstance(exc, subprocess.CalledProcessError) and (
                    is_benign_merge_failure(exc.stderr or reason)
                ):
                    pr_gone = is_pr_gone_merge_failure(exc.stderr or reason)
                    print(f"SKIP  #{number}: {reason}")
                    skipped.append({"number": number, "reason": reason})
                else:
                    print(f"FAIL  #{number}: {reason}", file=sys.stderr)
                    failed.append({"number": number, "reason": reason})
                continue
        finally:
            if ready_transition_succeeded and not merge_completed and not pr_gone:
                try:
                    mark_pr_draft(args.repo, number, write_token)
                except (subprocess.CalledProcessError, ValueError) as exc:
                    detail = (
                        _gh_error(exc)
                        if isinstance(exc, subprocess.CalledProcessError)
                        else str(exc)
                    )
                    reason = f"could not restore draft state: {detail}"
                    print(f"FAIL  #{number}: {reason}", file=sys.stderr)
                    failed.append({"number": number, "reason": reason})
        print(f"MERGED #{number}: {fresh['title']}")
        merged.append({"number": number, "title": fresh["title"]})
        # One merge per run is an explicit serialization boundary. It does not
        # rely on the branch endpoint immediately reflecting the new main SHA.
        print(
            "STOP  one-merge safety limit reached; remaining PRs wait for the next run"
        )
        break

    report = render_summary(
        merged,
        skipped,
        failed,
        dry_run=args.dry_run,
        circuit_open=circuit_open,
    )
    print()
    print(report)
    if args.summary_file:
        with open(args.summary_file, "a", encoding="utf-8") as handle:
            handle.write(report)

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
