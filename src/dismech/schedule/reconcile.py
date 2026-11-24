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

**"Needs my work" is not the same as "I can hand this off."** The
donate loop is an *unattended curation* hand-off. A PR that needs work but is
not a routine curation fix — a human (non-bot) reviewer has asked for changes,
or it edits code/schema/tooling/docs rather than KB content — is *deferred* to
the author rather than attempted. Deferral needs evidence the caller passes:
per-review authors in ``reviews`` (to tell a human reviewer from the automated
one) and changed paths in ``files`` (to tell a curation PR from a code one).
With neither, a PR is assumed hand-off-able, so existing callers are unaffected.
A deferred PR does **not** block claiming new work — it is the author's now —
but it is surfaced every fire so it is never silently dropped. Only an
*actionable* (hand-off-able) needs-work PR, or an un-PR'd claim issue, blocks a
new claim.

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

#: A GitHub App / bot login ends in this. A review from such a login is the
#: automated reviewer; a review from any other login is a human whose
#: changes-requested the author owns.
BOT_LOGIN_SUFFIX = "[bot]"

#: Repository-owned machine identities. ``gh pr list/view --json reviews`` goes
#: through GraphQL, which reports a GitHub App's login *without* the ``[bot]``
#: suffix (``ai4c-reviewer``), so the suffix alone cannot recognize the automated
#: reviewer there. Mirrors ``NON_HUMAN_ASSIGNEE_LOGINS`` in
#: ``scripts/auto_merge_ready_prs.py``.
KNOWN_BOT_LOGINS = frozenset(
    {"ai4c-agent", "ai4c-reviewer", "claude", "dragon-ai-agent", "github-actions"}
)

#: Review states that record a verdict. A ``COMMENTED`` (or ``PENDING``) review
#: after a ``CHANGES_REQUESTED`` does not withdraw it on GitHub, so it must not
#: overwrite the reviewer's effective state either.
VERDICT_STATES = frozenset({"APPROVED", "CHANGES_REQUESTED", "DISMISSED"})

#: Repository paths that are NOT curation content. A PR touching any of these is
#: a code / schema / tooling / docs change, out of scope for an unattended
#: curation hand-off, so a needs-work PR that touches one is deferred to the
#: author. KB content (kb/, history/, references_cache/, cache/, stubs/,
#: research/, projects/, pages/, dashboard/, app/) is not listed here, so a
#: pure-curation PR stays hand-off-able.
NON_CURATION_PREFIXES = (
    "src/",
    "tests/",
    "scripts/",
    ".github/",
    ".claude/",
    "conf/",
    "docs/",
)
#: Top-level non-curation files (no directory prefix to match on).
NON_CURATION_FILES = frozenset(
    {"CLAUDE.md", "AGENTS.md", "justfile", "pyproject.toml", "uv.lock", "mkdocs.yml"}
)


def _is_bot(login: str) -> bool:
    lowered = login.lower()
    return lowered.endswith(BOT_LOGIN_SUFFIX) or lowered in KNOWN_BOT_LOGINS


def _is_non_curation_path(path: str) -> bool:
    if path in NON_CURATION_FILES or path.endswith(".justfile"):
        return True
    return any(path.startswith(prefix) for prefix in NON_CURATION_PREFIXES)


def _file_paths(files: list[Any] | None) -> list[str]:
    """Normalize a ``files`` input to path strings.

    Accepts bare strings or the ``gh``/REST file-object shape (``filename`` or
    ``path`` key), so the caller can pass whichever it has to hand.
    """
    out: list[str] = []
    for entry in files or []:
        if isinstance(entry, str):
            out.append(entry)
        elif isinstance(entry, dict):
            path = entry.get("filename") or entry.get("path")
            if path:
                out.append(str(path))
    return out


def _latest_review_state_by_author(
    reviews: list[dict[str, Any]] | None,
) -> dict[str, str]:
    """Reduce a chronological review list to each reviewer's latest state.

    Accepts the ``{"state", "login"}`` shape the skill normalizes to, and the
    richer ``gh``/REST shapes that nest the login under ``user`` or ``author``.
    Later verdicts win, so a reviewer who commented and then requested changes
    is recorded as ``CHANGES_REQUESTED``. A later ``COMMENTED`` review does not
    replace an earlier verdict, matching GitHub's own effective review state; it
    is recorded only when the reviewer has given no verdict at all.
    """
    latest: dict[str, str] = {}
    for review in reviews or []:
        login = review.get("login")
        if not login:
            who = review.get("user") or review.get("author") or {}
            login = who.get("login")
        if not login:
            continue
        state = (review.get("state") or "").upper()
        if state in VERDICT_STATES or str(login) not in latest:
            latest[str(login)] = state
    return latest


def _defer_reasons(pr: dict[str, Any]) -> tuple[str, ...]:
    """Why a needs-work PR should go to the author instead of being attempted.

    Empty means hand-off-able. Both signals are evidence-gated: absent
    ``reviews``/``files`` yield no reason, so a caller that passes neither keeps
    the old "attempt everything that needs work" behavior.
    """
    reasons: list[str] = []
    for login, state in _latest_review_state_by_author(pr.get("reviews")).items():
        if state == "CHANGES_REQUESTED" and not _is_bot(login):
            reasons.append(
                f"{login} (human reviewer) requested changes; the author decides"
            )
            break
    non_curation = sorted(
        {p for p in _file_paths(pr.get("files")) if _is_non_curation_path(p)}
    )
    if non_curation:
        shown = ", ".join(non_curation[:3]) + (" …" if len(non_curation) > 3 else "")
        reasons.append(
            f"changes non-curation files ({shown}); not an unattended curation task"
        )
    return tuple(reasons)


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
    #: True when a needs-work PR is a routine curation fix the loop may attempt
    #: unattended. False when it is deferred to the author (a human reviewer
    #: asked for changes, or it changes non-curation files). Always True for a
    #: parked PR; only consulted for ``needs_my_work`` ones.
    hand_off_able: bool = True
    #: Why it was deferred, for the report. Empty when hand-off-able.
    defer_reasons: tuple[str, ...] = ()

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

    defer = _defer_reasons(pr)
    return PRClassification(
        number=int(pr.get("number", 0)),
        title=str(pr.get("title", "")),
        url=str(pr.get("url", "")),
        category=category,
        checks=checks,
        review_decision=review or "NONE",
        mergeable=mergeable or "UNKNOWN",
        reasons=tuple(reasons),
        hand_off_able=not defer,
        defer_reasons=defer,
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
    def actionable_prs(self) -> tuple[PRClassification, ...]:
        """Needs-work PRs the loop may attempt unattended this fire."""
        return tuple(
            c for c in self.pr_classifications if c.needs_my_work and c.hand_off_able
        )

    @property
    def deferred_prs(self) -> tuple[PRClassification, ...]:
        """Needs-work PRs handed to the author; reported, not attempted."""
        return tuple(
            c
            for c in self.pr_classifications
            if c.needs_my_work and not c.hand_off_able
        )

    @property
    def awaiting_review(self) -> tuple[PRClassification, ...]:
        return tuple(
            c for c in self.pr_classifications if c.category == "awaiting_review"
        )

    @property
    def waiting_to_merge(self) -> tuple[PRClassification, ...]:
        return tuple(
            c for c in self.pr_classifications if c.category == "waiting_to_merge"
        )


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
        sorted(
            unclaimed_claim_issues(claim_issues), key=lambda i: int(i.get("number", 0))
        )
    )

    actionable = [c for c in classifications if c.needs_my_work and c.hand_off_able]
    deferred = [c for c in classifications if c.needs_my_work and not c.hand_off_able]
    # A deferred PR is the author's, so it does NOT block a new claim; only an
    # actionable needs-work PR or an un-PR'd claim issue does.
    should_claim = not actionable and not unclaimed

    item: dict[str, Any] | None = None
    if actionable:
        first = actionable[0]
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

    summary = _summarize(classifications, unclaimed, should_claim, item, deferred)
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
    deferred: list[PRClassification] | None = None,
) -> str:
    deferred = deferred or []
    needs = sum(1 for c in classifications if c.needs_my_work)
    actionable = needs - len(deferred)
    awaiting = sum(1 for c in classifications if c.category == "awaiting_review")
    merging = sum(1 for c in classifications if c.category == "waiting_to_merge")
    parts = [
        (
            f"{len(classifications)} open PR(s): "
            f"{needs} need work ({actionable} actionable, {len(deferred)} deferred to author), "
            f"{awaiting} awaiting review, {merging} waiting to merge"
        ),
        f"{len(unclaimed)} un-PR'd claim issue(s)",
    ]
    if should_claim:
        parts.append(
            "decision: nothing actionable needs my work -> claim one new disease"
        )
    elif item:
        label = (
            f"PR #{item['number']}"
            if item["kind"] == "pr"
            else f"claim issue #{item['number']}"
        )
        parts.append(f"decision: finish {label}, claim nothing new this fire")
    if deferred:
        names = ", ".join(f"#{c.number}" for c in deferred)
        parts.append(f"deferred to author (not attempted): {names}")
    return "; ".join(parts)
