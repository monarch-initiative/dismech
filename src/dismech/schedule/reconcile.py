"""Classify the current user's in-flight work into the finish-first decision.

Every ``/schedule`` fire begins by reconciling against GitHub — **the only
state** — and deciding whether it may claim a *new* disease. The governing rule
(issue #11657):

    A new disease may be claimed only when **no PR of the user's still needs the
    user's own work** and **no un-PR'd claim issue exists**.

This module is the pure classifier behind that rule. It takes the JSON that
``gh pr list`` / ``gh issue list`` already return and produces a
:class:`Reconciliation` — no network, no cloud API — so it can be unit-tested
against fixtures.

A PR **needs my work** (and blocks a new claim) when it is any of:

- ``reviewDecision == "CHANGES_REQUESTED"`` (a reviewer, including the automated
  one, came back),
- **failing** a required check, or
- ``mergeable == "CONFLICTING"``.

A PR does **not** need my work — it is *parked* — when it is either awaiting
review (green/pending checks, no changes requested) or approved-and-green and
merely waiting for the deterministic auto-merge sweep. An un-PR'd claim issue
always needs my work (a prior fire that crashed before pushing; resume it).

Note the check semantics here are intentionally *looser* than
``scripts/auto_merge_ready_prs.py``: that script decides merge-readiness and so
treats an empty rollup or ``UNKNOWN`` mergeability as not-ready. Reconcile asks
only "must I act?", so an empty/pending rollup is "nothing to fix" (parked), not
a blocker.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Literal

#: CheckRun conclusions that count as a hard failure the curator must fix.
#: ``CANCELLED`` is deliberately *not* here (review #11658, item 9): a cancelled
#: run is almost always a superseded workflow (a newer push cancelled the old
#: run), which ``scripts/retry_failed_reviews.py`` recovers on its own backoff —
#: it is not something the curator fixes by editing, so it is treated as pending
#: rather than as a blocking failure. This diverges from the issue's original
#: classifier spec on purpose.
FAILING_CONCLUSIONS = frozenset(
    {"FAILURE", "TIMED_OUT", "ACTION_REQUIRED", "STARTUP_FAILURE"}
)
#: Conclusions treated as "not my problem, will resolve/retry itself" -> pending.
SUPERSEDED_CONCLUSIONS = frozenset({"CANCELLED"})
#: StatusContext states that count as a failure (the legacy commit-status shape).
FAILING_STATES = frozenset({"FAILURE", "ERROR", "ACTION_REQUIRED"})

ChecksState = Literal["failing", "pending", "green"]
PRCategory = Literal["needs_my_work", "awaiting_review", "waiting_to_merge"]


def classify_checks(rollup: list[dict[str, Any]] | None) -> ChecksState:
    """Classify a PR's ``statusCheckRollup`` into failing / pending / green.

    ``rollup`` mixes ``CheckRun`` entries (``status`` + ``conclusion``) and
    ``StatusContext`` entries (``state``). A missing or empty rollup is *green*
    — there is nothing to fix — matching the issue's "else green" spec and,
    unlike the merge sweep, treating "no checks yet" as not-my-problem.
    """
    if not rollup:
        return "green"

    pending = False
    for entry in rollup:
        typename = entry.get("__typename")
        is_check_run = (
            typename == "CheckRun"
            if typename
            else ("conclusion" in entry or "status" in entry)
        )
        if is_check_run:
            status = (entry.get("status") or "").upper()
            conclusion = (entry.get("conclusion") or "").upper()
            if conclusion in FAILING_CONCLUSIONS:
                return "failing"
            if conclusion in SUPERSEDED_CONCLUSIONS:
                pending = True  # superseded run; a newer run is the real signal
            elif status != "COMPLETED" or not conclusion:
                pending = True
        else:
            state = (entry.get("state") or "").upper()
            if state in FAILING_STATES:
                return "failing"
            if state == "PENDING" or not state:
                pending = True
    return "pending" if pending else "green"


@dataclass(frozen=True)
class PRClassification:
    number: int
    title: str
    url: str
    category: PRCategory
    checks: ChecksState
    review_decision: str
    mergeable: str
    reasons: tuple[str, ...] = ()

    @property
    def needs_my_work(self) -> bool:
        return self.category == "needs_my_work"


def classify_pr(pr: dict[str, Any]) -> PRClassification:
    """Classify one PR (as returned by ``gh pr list --json ...``)."""
    checks = classify_checks(pr.get("statusCheckRollup"))
    review = (pr.get("reviewDecision") or "").upper()
    mergeable = (pr.get("mergeable") or "").upper()

    reasons: list[str] = []
    if review == "CHANGES_REQUESTED":
        reasons.append("reviewer requested changes")
    if checks == "failing":
        reasons.append("required checks failing")
    if mergeable == "CONFLICTING":
        reasons.append("merge conflict with base")

    if reasons:
        category: PRCategory = "needs_my_work"
    elif review == "APPROVED" and checks == "green":
        category = "waiting_to_merge"
    else:
        category = "awaiting_review"

    return PRClassification(
        number=int(pr.get("number", 0)),
        title=str(pr.get("title", "")),
        url=str(pr.get("url", "")),
        category=category,
        checks=checks,
        review_decision=review or "NONE",
        mergeable=mergeable or "UNKNOWN",
        reasons=tuple(reasons),
    )


def unclaimed_claim_issues(issues: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Filter open ``claim`` issues down to those with no linked PR.

    Uses the same authoritative link ``/curate-next`` uses:
    ``closedByPullRequestsReferences`` empty means no PR has been opened yet, so
    the claim was made but curation has not reached a pushed PR.
    """
    out = []
    for issue in issues:
        refs = issue.get("closedByPullRequestsReferences") or []
        if len(refs) == 0:
            out.append(issue)
    return out


@dataclass(frozen=True)
class Reconciliation:
    pr_classifications: tuple[PRClassification, ...]
    unclaimed_issues: tuple[dict[str, Any], ...]
    should_claim_new: bool
    #: The single item this fire must finish (a PR or a claim issue), or None.
    item_needing_work: dict[str, Any] | None = None
    summary: str = ""
    #: False when an identity check was requested and the authenticated login did
    #: not match the expected one. When False the fire does nothing at all — it
    #: neither claims nor tries to finish work that is not the curator's.
    identity_ok: bool = True

    @property
    def needs_work_prs(self) -> tuple[PRClassification, ...]:
        return tuple(c for c in self.pr_classifications if c.needs_my_work)

    @property
    def awaiting_review(self) -> tuple[PRClassification, ...]:
        return tuple(c for c in self.pr_classifications if c.category == "awaiting_review")

    @property
    def waiting_to_merge(self) -> tuple[PRClassification, ...]:
        return tuple(c for c in self.pr_classifications if c.category == "waiting_to_merge")


def reconcile(
    prs: list[dict[str, Any]],
    claim_issues: list[dict[str, Any]],
    *,
    authenticated_login: str | None = None,
    expected_login: str | None = None,
) -> Reconciliation:
    """Reduce the user's open PRs and claim issues to a claim-or-finish decision.

    ``prs`` is ``gh pr list --author @me --state open --json
    number,title,url,reviewDecision,mergeable,statusCheckRollup``; ``claim_issues``
    is ``gh issue list --assignee @me --state open --label claim --json
    number,title,closedByPullRequestsReferences``.

    The result's ``should_claim_new`` is true only when nothing needs the user's
    work. When something does, ``item_needing_work`` names the single item to
    finish this fire — PRs that need work take precedence over un-PR'd claim
    issues, and both are considered in ascending number order so the choice is
    stable across fires (review #11658, item 10).

    **Identity gate (review #11658, item 4).** ``reconcile`` fails *open* by
    design — an empty ``prs``/``claim_issues`` means "clean account, claim one".
    But those lists come from ``--author @me`` / ``--assignee @me``, so a cloud
    fire authenticated as the wrong account (a bot/App) sees empty lists every
    fire and would claim a new disease hourly. When ``expected_login`` is given
    and ``authenticated_login`` does not match it, the fire does **nothing**:
    ``identity_ok`` is False, ``should_claim_new`` is False, and no item is
    selected. Pass both from the skill (``gh api user --jq .login`` vs the
    config's ``github_login``).
    """
    if expected_login is not None and (authenticated_login or "") != expected_login:
        return Reconciliation(
            pr_classifications=(),
            unclaimed_issues=(),
            should_claim_new=False,
            item_needing_work=None,
            identity_ok=False,
            summary=(
                f"refusing to act: authenticated as {authenticated_login or 'nobody'}, "
                f"expected {expected_login}. Not this curator's account -> no claim, no fix."
            ),
        )

    classifications = tuple(
        classify_pr(pr) for pr in sorted(prs, key=lambda p: int(p.get("number", 0)))
    )
    unclaimed = tuple(
        sorted(unclaimed_claim_issues(claim_issues), key=lambda i: int(i.get("number", 0)))
    )

    needs_work = [c for c in classifications if c.needs_my_work]
    should_claim = not needs_work and not unclaimed

    item: dict[str, Any] | None = None
    if needs_work:
        first = needs_work[0]
        item = {
            "kind": "pr",
            "number": first.number,
            "title": first.title,
            "url": first.url,
            "reasons": list(first.reasons),
        }
    elif unclaimed:
        issue = unclaimed[0]
        item = {
            "kind": "claim_issue",
            "number": issue.get("number"),
            "title": issue.get("title"),
            "reasons": ["un-PR'd claim issue: resume curating to a pushed PR"],
        }

    summary = _summarize(classifications, unclaimed, should_claim, item)
    return Reconciliation(
        pr_classifications=classifications,
        unclaimed_issues=unclaimed,
        should_claim_new=should_claim,
        item_needing_work=item,
        summary=summary,
    )


def _summarize(
    classifications: tuple[PRClassification, ...],
    unclaimed: tuple[dict[str, Any], ...],
    should_claim: bool,
    item: dict[str, Any] | None,
) -> str:
    needs = sum(1 for c in classifications if c.needs_my_work)
    awaiting = sum(1 for c in classifications if c.category == "awaiting_review")
    merging = sum(1 for c in classifications if c.category == "waiting_to_merge")
    parts = [
        f"{len(classifications)} open PR(s): "
        f"{needs} need work, {awaiting} awaiting review, {merging} waiting to merge",
        f"{len(unclaimed)} un-PR'd claim issue(s)",
    ]
    if should_claim:
        parts.append("decision: nothing needs my work -> claim one new disease")
    elif item:
        label = (
            f"PR #{item['number']}" if item["kind"] == "pr" else f"claim issue #{item['number']}"
        )
        parts.append(f"decision: finish {label}, claim nothing new this fire")
    return "; ".join(parts)
