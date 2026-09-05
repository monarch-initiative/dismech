#!/usr/bin/env python3
"""Deterministically merge or enqueue PRs that are ready by every signal.

This runs in the ``pr-shepherd`` workflow's fresh closing job, isolated from the
LLM runner. The shepherd agent *judges* stuck PRs; this controller deliberately
does not. It applies a fixed predicate to GitHub-reported state and merges what
passes, so the outcome of a run is reproducible from the API response alone.

A PR is merged only when ALL of these hold:

- open and targeting the expected base branch (``main``); a draft is treated as
  queue metadata and promoted immediately before the final verification
- **not human-assigned** — bot/agent assignees do not hold a PR
- **reviewer approved** — ``reviewDecision == "APPROVED"``
- **no conflicts** — ``mergeable == "MERGEABLE"``
- **green** — ``mergeStateStatus == "CLEAN"`` (GitHub's configured protection
  rules are satisfied). The PR branch is not required to contain current
  ``main``. The active merge queue tests that integration on a temporary
  merge-group commit; if the queue is disabled, direct loose merging remains
  intentional repository policy.
- **tests passing** — the head commit's status-check rollup has at least one
  SUCCESS and nothing failing, cancelled, or still running. This is stricter
  than ``CLEAN``, which only accounts for *required* checks: a failing
  non-required check also blocks the merge here.
- **older than N days** (default 3), measured from ``createdAt``

Anything else — including ``mergeable == "UNKNOWN"`` once GitHub has had its
chance to compute mergeability — is skipped with a recorded reason. Skipping is
always safe: the workflow runs hourly and will reconsider the PR.

Escape hatch: **assign the PR to a human.** Human assignment is the per-PR veto.
Bot or agent assignment is routing metadata and does not hold a PR. Requesting
changes also blocks the merge. Draft state deliberately does not: opening a PR
places it in DisMech's review queue.

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
controller performs a final PR read and pins the merge/enqueue operation to that
verified head SHA. It deliberately does not require the PR head to contain the
latest ``main`` commit. The active merge queue performs current-main integration
testing on its temporary merge-group commit. If that queue is disabled, direct
loose merging of the verified green PR remains intentional repository policy.

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

# Fields fetched for the initial scan; a superset is re-fetched per candidate.
# `mergeStateStatus` is deliberately NOT here — see the module docstring.
LIST_FIELDS = (
    "number,title,isDraft,createdAt,assignees,reviewDecision,mergeable,baseRefName"
)
# headRefOid pins the reviewed head for the merge request. `baseRefOid` is
# intentionally absent: GitHub's field is the PR's associated base-ref OID, not
# proof that the head contains it, and exact-base ancestry is not a policy gate.
VIEW_FIELDS = LIST_FIELDS + ",state,statusCheckRollup,headRefOid,mergeStateStatus"

# Check conclusions that do not count as a failure. SKIPPED/NEUTRAL are how
# conditional workflow jobs report "not applicable to this PR".
PASSING_CONCLUSIONS = frozenset({"SUCCESS", "SKIPPED", "NEUTRAL"})
# Legacy commit-status states (StatusContext rollup entries).
PASSING_STATES = frozenset({"SUCCESS", "EXPECTED", "NEUTRAL"})

# Each successful enqueue creates a PR comment, and GitHub applies an
# 80-content-creating-requests/minute secondary limit. Fifty leaves headroom
# for other automation and keeps the controller comfortably inside its
# 15-minute job timeout even though every candidate is re-read twice.
DEFAULT_MAX_ENQUEUE_PER_RUN = 50

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
GH_WARNING_MARKER = "! "
GH_STATUS_MARKERS = ("X ", GH_WARNING_MARKER, "✓ ")

MERGE_COMMENT = (
    "🐑 **PR Shepherd** (deterministic sweep) — Squash-merged: approved, "
    "no human assignee, no conflicts, all checks green, and open longer than "
    "{days} days. No further action needed."
)

ENQUEUE_COMMENT = (
    "🐑 **PR Shepherd** (deterministic sweep) — Added to the merge queue: "
    "approved, no human assignee, no conflicts, all checks green, and open "
    "longer than {days} days. GitHub will test this PR against current "
    "`main` and merge it if that passes; if it does not, this PR stops being "
    "eligible and needs a look."
)

# GitHub Apps cannot normally be assignees. The retired Dragon machine identity
# is a GitHub ``User``, however, so API object type alone cannot distinguish it
# from a person. Keep repository-owned machine identities explicit and also
# recognize GitHub's conventional ``[bot]`` suffix.
NON_HUMAN_ASSIGNEE_LOGINS = frozenset(
    {
        "ai4c-agent",
        "ai4c-reviewer",
        "claude",
        "dragon-ai-agent",
        "github-actions",
    }
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


def is_human_assignee(assignee: dict) -> bool:
    """Return whether an assignee represents a human hold on the PR.

    Missing or unfamiliar identities fail closed as human. This lets known
    repository automation use assignment as routing metadata without allowing
    a typo or newly introduced machine account to silently remove a hold.
    """
    login = str(assignee.get("login") or "").strip().casefold()
    if not login:
        return True
    return not (login.endswith("[bot]") or login in NON_HUMAN_ASSIGNEE_LOGINS)


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
    assignees = pr.get("assignees") or []
    human_logins = [
        str(assignee.get("login") or "?")
        for assignee in assignees
        if is_human_assignee(assignee)
    ]
    if human_logins:
        return Decision(False, f"assigned to human(s): {', '.join(human_logins)}")
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

    Lines ``gh`` marked as warnings ("! ...") are *deprioritized* rather than
    dropped. On a queue-required branch ``gh`` prints a warning before doing
    its work, so reporting the literal first line would attribute every
    failure -- whatever its real cause -- to that warning. A warning is still
    returned when it is all stderr contains, which is better than discarding
    the only information available.
    """
    warnings: list[str] = []
    for line in (exc.stderr or "").splitlines():
        cleaned = line.strip()
        is_warning = cleaned.startswith(GH_WARNING_MARKER)
        # removeprefix, not lstrip: lstrip takes a character *set*, so it would
        # eat the leading "X" and "-" of a line like "X-Ratelimit is 0".
        for marker in GH_STATUS_MARKERS:
            cleaned = cleaned.removeprefix(marker)
        cleaned = cleaned.strip()
        if not cleaned:
            continue
        if is_warning:
            warnings.append(cleaned)
            continue
        return cleaned
    if warnings:
        return warnings[0]
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


@dataclass(frozen=True)
class QueueState:
    """Whether a merge queue is in force on the base branch, and who is in it.

    Both answers come from one read taken **once per run**, before the
    candidate loop: queue-required is branch state, not per-PR state, and this
    module works hard to keep the window between the final base check and the
    write narrow. A per-merge lookup would widen exactly that window.

    ``active`` is False when the lookup fails, keeping pre-queue behavior
    rather than silently changing how merges are issued on a bad API day. A
    null ``mergeQueue`` node is also False, and that is what makes this track
    the break-glass pause: disabling the ruleset nulls the node (verified
    against a scratch branch -- active returns an ``MQ_`` id, ruleset disabled
    returns null).
    """

    active: bool
    queued_pr_numbers: frozenset[int]
    # False only when the read itself failed. Without this, "no queue in
    # force" and "could not tell" are the same value, and an inert fix is
    # indistinguishable from the starvation bug it was meant to remove.
    readable: bool = True
    truncated: int = 0

    def summary_line(self) -> str:
        """One line for the run report, so inertness is visible immediately."""
        if not self.readable:
            return (
                "**Merge queue:** state unavailable — falling back to direct "
                "merge. If a queue is in force on the base branch, queued PRs "
                "will be reselected and re-enqueued."
            )
        if not self.active:
            return "**Merge queue:** not in force on the base branch."
        line = f"**Merge queue:** active, {len(self.queued_pr_numbers)} queued."
        if self.truncated:
            line += (
                f" Only the first {len(self.queued_pr_numbers)} of "
                f"{self.truncated} entries were read, so a queued PR beyond "
                "that may be reselected."
            )
        return line


def read_queue_state(repo: str, branch: str) -> QueueState:
    """Read the base branch's complete merge queue with GraphQL pagination."""
    owner, _, name = repo.partition("/")
    query = (
        "query($owner:String!,$name:String!,$branch:String!,$endCursor:String){"
        "repository(owner:$owner,name:$name){mergeQueue(branch:$branch){id "
        "entries(first:100,after:$endCursor){totalCount "
        "pageInfo{hasNextPage endCursor} nodes{pullRequest{number}}}}}}"
    )
    try:
        payload = _gh(
            [
                "api",
                "graphql",
                "--paginate",
                "--slurp",
                "-f",
                f"owner={owner}",
                "-f",
                f"name={name}",
                "-f",
                f"branch={branch}",
                "-f",
                f"query={query}",
            ]
        )
        data = json.loads(payload)
    except (subprocess.CalledProcessError, OSError, ValueError) as exc:
        print(f"WARN  could not read merge-queue state: {exc}", file=sys.stderr)
        return QueueState(False, frozenset(), readable=False)
    # `gh api --paginate --slurp` returns a list. Accept one object as well so
    # callers using an older gh and focused unit-test fixtures fail safely.
    pages = data if isinstance(data, list) else [data]
    if not pages or not all(isinstance(page, dict) for page in pages):
        print("WARN  merge-queue read returned an unexpected shape", file=sys.stderr)
        return QueueState(False, frozenset(), readable=False)

    numbers: set[int] = set()
    total: int | None = None
    nodes_read = 0
    for index, page in enumerate(pages):
        repository = (page.get("data") or {}).get("repository") or {}
        if not isinstance(repository, dict):
            print(
                "WARN  merge-queue read returned an unexpected repository",
                file=sys.stderr,
            )
            return QueueState(False, frozenset(), readable=False)
        queue = repository.get("mergeQueue")
        if not queue:
            if index == 0:
                return QueueState(False, frozenset())
            print("WARN  merge queue disappeared during pagination", file=sys.stderr)
            return QueueState(False, frozenset(), readable=False)
        if not isinstance(queue, dict):
            print(
                "WARN  merge-queue read returned an unexpected queue", file=sys.stderr
            )
            return QueueState(False, frozenset(), readable=False)
        entries = queue.get("entries") or {}
        if not isinstance(entries, dict):
            print("WARN  merge-queue read returned unexpected entries", file=sys.stderr)
            return QueueState(False, frozenset(), readable=False)
        nodes = entries.get("nodes") or []
        if not isinstance(nodes, list):
            print("WARN  merge-queue read returned unexpected nodes", file=sys.stderr)
            return QueueState(False, frozenset(), readable=False)
        nodes_read += len(nodes)
        numbers.update(
            int(entry["pullRequest"]["number"])
            for entry in nodes
            if isinstance(entry, dict)
            and isinstance(entry.get("pullRequest"), dict)
            and entry["pullRequest"].get("number")
        )
        page_total = entries.get("totalCount")
        if isinstance(page_total, int):
            total = page_total if total is None else max(total, page_total)

    truncated = total if total is not None and total > nodes_read else 0
    if truncated:
        # Truncation is only a missed skip, never a bad merge -- but say so
        # rather than letting the page size silently bound correctness.
        print(
            f"WARN  merge queue holds {total} entries; only the first "
            f"{len(nodes)} were read, so a queued PR beyond that may be "
            "reselected",
            file=sys.stderr,
        )
    return QueueState(True, frozenset(numbers), truncated=truncated)


# A PR that fails the queue twice running, with no push in between, has had
# the same build repeated on the same content. One failure is not evidence of
# guilt (see EjectionMemory); two, unchanged, is enough to stop retrying.
EJECTION_STRIKE_LIMIT = 2


@dataclass(frozen=True)
class EjectionMemory:
    """Whether prior queue ejections should stop this PR re-entering now.

    The merge queue ejects a PR when the group containing it fails, but that
    ejection is invisible to eligibility: the PR stays open and approved, so
    the next sweep re-enqueues it, it fails again, and the cycle repeats. PR
    #9852 did exactly that three times in fifteen hours, and because the queue
    builds speculatively each cycle also failed every stack behind it -- about
    three hours of queue throughput and a dozen builds (#10988).

    An ejection does NOT imply the PR is at fault, so this deliberately does
    not judge a single one. Three causes were observed in one 24-hour window:
    the PR's own content failing (#9852), a PR *ahead* of it poisoning the
    speculative stack (#9996 and five others behind #10142), and a third-party
    outage (#10677/#10700/#10727, EBI read timeouts the validator itself calls
    "not a data error"). Blocking on one ejection would mostly block innocents.

    What distinguishes them is repetition against unchanged content. Collateral
    and infrastructure failures do not reproduce once the queue has moved on;
    a defect in the PR itself does. So the rule counts ``failed_checks``
    ejections that happened *after* the head commit was last written: reaching
    ``strike_limit`` holds the PR back. The count is keyed on the head
    commit's ``committedDate``: rewriting the head (a push, amend, rebase or
    a merge of the base branch) moves that date past the earlier removals and
    resets the count to zero, because the content under test has changed.

    Note ``RemovedFromMergeQueueEvent.beforeCommit`` is NOT the base-branch tip
    -- it is the queue's own temporary merge commit, and compares as diverged
    from ``main`` -- so it cannot be used to detect base movement. Verified
    against the #9852 events on 2026-09-04.
    """

    blocked: bool
    strikes: int = 0
    reason: str = ""


def ejection_memory(
    repo: str, number: int, strike_limit: int = EJECTION_STRIKE_LIMIT
) -> EjectionMemory:
    """Count unchanged-content queue failures for one PR."""
    owner, _, name = repo.partition("/")
    query = (
        "query($owner:String!,$name:String!,$number:Int!){"
        "repository(owner:$owner,name:$name){"
        "pullRequest(number:$number){"
        "commits(last:1){nodes{commit{committedDate}}} "
        "timelineItems(last:20,itemTypes:[REMOVED_FROM_MERGE_QUEUE_EVENT])"
        "{nodes{... on RemovedFromMergeQueueEvent{createdAt reason}}}}}}"
    )
    try:
        payload = _gh([
            "api", "graphql",
            "-f", f"owner={owner}", "-f", f"name={name}",
            "-F", f"number={number}", "-f", f"query={query}",
        ])
        data = json.loads(payload)
    except subprocess.CalledProcessError as exc:
        # Fail open: a lookup failure must not hold back a ready PR.
        print(f"WARN  #{number}: could not read ejection history: "
              f"{_gh_error(exc)}", file=sys.stderr)
        return EjectionMemory(False)
    except (OSError, ValueError) as exc:
        print(f"WARN  #{number}: could not read ejection history: {exc}",
              file=sys.stderr)
        return EjectionMemory(False)
    if not isinstance(data, dict):
        return EjectionMemory(False)
    pr = ((data.get("data") or {}).get("repository") or {}).get("pullRequest") or {}
    commits = ((pr.get("commits") or {}).get("nodes")) or []
    head_written = ""
    if commits and isinstance(commits[0], dict):
        head_written = str((commits[0].get("commit") or {}).get("committedDate") or "")
    if not head_written:
        # Without the head's write time a strike cannot be attributed to the
        # current content, so fail open rather than hold on a guess.
        print(f"WARN  #{number}: no head commit date; not applying an "
              "ejection hold", file=sys.stderr)
        return EjectionMemory(False)
    nodes = ((pr.get("timelineItems") or {}).get("nodes")) or []
    strikes = 0
    latest = ""
    for node in nodes:
        if not isinstance(node, dict) or node.get("reason") != "failed_checks":
            continue
        when = str(node.get("createdAt") or "")
        # ISO-8601 UTC strings from GitHub compare correctly as text.
        if when <= head_written:
            continue  # predates the current content; a push has since reset it
        strikes += 1
        latest = max(latest, when)
    if strike_limit <= 0 or strikes < strike_limit:
        return EjectionMemory(False, strikes)
    return EjectionMemory(
        True,
        strikes,
        f"failed the merge queue {strikes} times since its head commit was "
        f"last written (most recently {latest}); push a fix to retry",
    )


def merge_pr(
    repo: str,
    number: int,
    min_age_days: int,
    head_sha: str | None,
    write_token: str,
    queued: bool = False,
) -> bool:
    """Squash-merge one PR -- or add it to the merge queue -- then announce it.

    ``--match-head-commit`` makes GitHub reject the operation if a push landed
    after the verification read, so the commit acted on is provably the commit
    whose checks and review state were evaluated. It pins the enqueued head
    the same way it pins a direct merge: ``gh`` assigns it to
    ``payload.expectedHeadOid`` before the queue branch.

    With ``queued`` set, the base branch requires a merge queue and this
    **enqueues** rather than merges: the PR is tested against current ``main``
    on a temporary branch and merged only if that passes. So a successful call
    no longer means "merged", and the announcement says so. A PR whose own
    required checks have not yet passed is armed for auto-merge and enters the
    queue when they do.

    The strategy flag is dropped on that path for accuracy, not necessity.
    ``gh`` only *warns* when given one on a queue-required branch and enqueues
    anyway with exit status 0 (the ``// only warn for now`` branch of
    ``mergeRun`` in ``cli/cli``, checked against gh 2.96.0). Passing
    ``--squash`` there is harmless to the merge but not to diagnosis: ``gh``
    prints that warning first, and ``_gh_error`` reports the first stderr
    line, so every genuine failure would be misreported as the queue warning.

    Returns whether the PR was enqueued rather than merged, so callers can
    report the operation they actually performed.
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
        *([] if queued else ["--squash"]),
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
                (ENQUEUE_COMMENT if queued else MERGE_COMMENT).format(
                    days=min_age_days
                ),
            ],
            token=writer,
        )
    except subprocess.CalledProcessError as exc:
        print(
            f"WARN  #{number}: {'enqueued' if queued else 'merged'}, but "
            f"posting the comment failed: {_gh_error(exc)}",
            file=sys.stderr,
        )
    return queued


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
    unprocessed: list[dict] | None = None,
    *,
    dry_run: bool = False,
    queue_state: QueueState | None = None,
) -> str:
    """Render the run report.

    ``dry_run`` retitles the merged section: a dry run that logs "Merged 3"
    into the step summary leaves a permanent, false audit trail.

    ``queue_state`` is reported unconditionally, not just when it changed the
    outcome. A failed queue read makes this controller behave exactly as it
    did before queue awareness -- reselecting and re-enqueueing a queued PR --
    so "the fix is inert" must be visible in the artifact operators read,
    rather than inferred from the absence of a skip line.
    """
    title = "## 🐑 Deterministic auto-merge sweep"
    if dry_run:
        title += " (dry run — no changes made)"
    lines = [title, ""]
    if queue_state is not None:
        lines.extend([queue_state.summary_line(), ""])
    queued = [row for row in merged if row.get("queued")]
    direct = [row for row in merged if not row.get("queued")]
    sections = [
        (
            "Would add to the merge queue" if dry_run else "Added to the merge queue",
            queued,
        ),
        ("Would merge" if dry_run else "Merged", direct),
    ]
    shown = False
    for verb, rows in sections:
        if not rows:
            continue
        shown = True
        lines.append(f"**{verb} {len(rows)}:**")
        lines += [
            f"- #{row['number']} — {row['title']}"
            + (f" ({row['action']})" if row.get("action") else "")
            for row in rows
        ]
        lines.append("")
    if not shown:
        verb = "Would merge" if dry_run else "Merged"
        lines.append(f"**{verb} 0** — nothing met every criterion.")
        lines.append("")
    if failed:
        lines.append(f"**Failed {len(failed)}:**")
        lines += [f"- #{r['number']} — {r['reason']}" for r in failed]
        lines.append("")
    if unprocessed:
        lines.append(f"**Unprocessed candidates {len(unprocessed)}:**")
        lines += [f"- #{r['number']} — {r['reason']}" for r in unprocessed]
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
        "--limit", type=int, default=1000, help="max open PRs to scan (default: 1000)"
    )
    parser.add_argument(
        "--specific-pr",
        type=int,
        help="evaluate only this PR instead of scanning all open PRs",
    )
    parser.add_argument(
        "--max-enqueue-per-run",
        type=non_negative_int,
        default=DEFAULT_MAX_ENQUEUE_PER_RUN,
        help=(
            "maximum enqueue attempts in one queue-mode run "
            f"(default: {DEFAULT_MAX_ENQUEUE_PER_RUN}; ignored for dry runs)"
        ),
    )
    parser.add_argument(
        "--ejection-strike-limit",
        type=non_negative_int,
        default=EJECTION_STRIKE_LIMIT,
        help=(
            "hold a PR after this many merge-queue failures with no push in "
            "between (0 disables the hold)"
        ),
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

    # Once per run, before any write: is a queue in force, and who is in it?
    #
    # What a queued PR reports depends on its ENTRY state, and the two cases
    # were measured separately on the live queue:
    #
    #   AWAITING_CHECKS -> mergeable/mergeStateStatus are UNKNOWN while the
    #     queue builds. `evaluate` rejects that ("mergeability is unknown")
    #     and the loop `continue`s, so the sweep already moves on. Skipping
    #     here saves the repeated view_pr attempts and their backoff sleeps
    #     spent waiting for an UNKNOWN that will not resolve, and reports an
    #     accurate reason instead of a misleading mergeability one.
    #
    #   UNMERGEABLE -> observed on #10576 at 2026-09-02T23:37Z: entry state
    #     UNMERGEABLE, isInMergeQueue true, yet the PR itself reported
    #     mergeable=MERGEABLE and mergeStateStatus=CLEAN, and it stayed that
    #     way for ~48 minutes before GitHub ejected it. THAT is the
    #     budget-consuming case: it passes every predicate, re-enqueueing
    #     SUCCEEDS (gh exits 0 on an already-queued PR), and the sweep spends
    #     its one action re-announcing a PR that is already queued.
    #
    # So the skip is load-bearing for the second case and a cost/clarity win
    # for the first. It also stops correct behavior resting on GitHub's
    # undocumented UNKNOWN reporting for queued PRs.
    queue_state = read_queue_state(args.repo, args.base_branch)
    if queue_state.active:
        already = [
            pr for pr in candidates if pr["number"] in queue_state.queued_pr_numbers
        ]
        for pr in already:
            reason = "already in the merge queue"
            print(f"SKIP  #{pr['number']}: {reason}")
            skipped.append({"number": pr["number"], "reason": reason})
        candidates = [
            pr for pr in candidates if pr["number"] not in queue_state.queued_pr_numbers
        ]
        print(
            f"Merge queue is in force on {args.base_branch}: "
            f"{len(queue_state.queued_pr_numbers)} PR(s) queued, "
            f"{len(candidates)} candidate(s) remain."
        )

    # Oldest first is deterministic and honors the standing human-review window.
    candidates.sort(key=lambda pr: (_parse_ts(pr["createdAt"]), int(pr["number"])))

    merged: list[dict] = []
    failed: list[dict] = []
    unprocessed: list[dict] = []
    enqueue_attempts = 0
    for index, pr in enumerate(candidates):
        if (
            queue_state.active
            and not args.dry_run
            and enqueue_attempts >= args.max_enqueue_per_run
        ):
            reason = (
                "not re-verified: enqueue-attempt budget of "
                f"{args.max_enqueue_per_run} reached"
            )
            unprocessed = [
                {"number": remaining["number"], "reason": reason}
                for remaining in candidates[index:]
            ]
            print(
                f"STOP  enqueue-attempt budget reached; "
                f"{len(unprocessed)} candidate(s) remain unprocessed"
            )
            break
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

        # Before the draft transition, not after: a held PR that is a draft
        # would otherwise be marked ready, skipped, and re-drafted on every
        # run for as long as the hold lasts -- and a failing re-draft would
        # turn the run red over a PR the sweep never intended to touch.
        # Checked here rather than per candidate, so it costs one extra read
        # per run.
        memory = ejection_memory(args.repo, number, args.ejection_strike_limit)
        if memory.blocked:
            print(f"SKIP  #{number}: {memory.reason}")
            skipped.append({"number": number, "reason": memory.reason})
            continue

        was_draft = bool(fresh.get("isDraft"))

        ready_transition_succeeded = False
        merge_completed = False
        # Bound here, not only inside the try below: line-of-sight beats a
        # non-local invariant for a variable read after a write has happened.
        enqueued = False
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

            # This is the load-bearing PR read for both drafts and non-drafts.
            # The write below is pinned to the head SHA returned here.
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
            if args.dry_run:
                if queue_state.active:
                    action = (
                        "mark ready and add to the merge queue"
                        if was_draft
                        else "add to the merge queue"
                    )
                else:
                    action = "mark ready and merge" if was_draft else "merge"
                print(
                    f"DRY-RUN would {action} #{number}: {fresh['title']} — "
                    f"{decision.reason}"
                )
                merged.append(
                    {
                        "number": number,
                        "title": fresh["title"],
                        "action": action,
                        "queued": queue_state.active,
                    }
                )
                if queue_state.active:
                    continue
                print("STOP  one-merge safety limit reached")
                break

            try:
                if queue_state.active:
                    enqueue_attempts += 1
                enqueued = merge_pr(
                    args.repo,
                    number,
                    args.min_age_days,
                    fresh.get("headRefOid"),
                    write_token,
                    queue_state.active,
                )
                # Load-bearing on the enqueue path too: it stops the `finally`
                # block converting the PR back to draft, which would eject it
                # from the queue it was just added to.
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
        print(f"{'QUEUED' if enqueued else 'MERGED'} #{number}: {fresh['title']}")
        merged.append({"number": number, "title": fresh["title"], "queued": enqueued})
        if queue_state.active:
            continue
        # Direct mode changes main immediately, so preserve its explicit
        # serialization boundary. Queue mode delegates serialization to GitHub.
        print("STOP  one-merge safety limit reached")
        break

    report = render_summary(
        merged,
        skipped,
        failed,
        unprocessed,
        dry_run=args.dry_run,
        queue_state=queue_state,
    )
    print()
    print(report)
    if args.summary_file:
        with open(args.summary_file, "a", encoding="utf-8") as handle:
            handle.write(report)

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
