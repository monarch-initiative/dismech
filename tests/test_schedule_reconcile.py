"""Unit tests for the pure reconcile/PR classifier (issue #11657).

Table-driven: one test per behavior, walking a table of cases, so the suite
stays small. A failing row names itself in the assert message.
"""

from __future__ import annotations

from dismech.schedule.reconcile import (
    classify_checks,
    classify_pr,
    reconcile,
    unclaimed_claim_issues,
)


def pr(number=1, review=None, mergeable="MERGEABLE", rollup=None):
    return {
        "number": number,
        "title": "Curate X",
        "url": f"https://github.com/monarch-initiative/dismech/pull/{number}",
        "headRefName": "curate/x",
        "isDraft": False,
        "reviewDecision": review,
        "mergeable": mergeable,
        "statusCheckRollup": rollup if rollup is not None else [check_run("SUCCESS")],
    }


def check_run(conclusion="SUCCESS", status="COMPLETED"):
    return {"__typename": "CheckRun", "name": "ci", "status": status, "conclusion": conclusion}


def status_context(state="SUCCESS"):
    return {"__typename": "StatusContext", "context": "legacy", "state": state}


PENDING = check_run(status="IN_PROGRESS", conclusion="")


def test_classify_checks():
    cases = [
        (None, "green"),
        ([], "green"),
        ([check_run("SUCCESS"), check_run("SKIPPED")], "green"),
        ([PENDING], "pending"),
        ([PENDING, check_run("FAILURE")], "failing"),  # failing beats pending
        ([status_context("SUCCESS")], "green"),
        ([status_context("PENDING")], "pending"),
        ([status_context("FAILURE")], "failing"),
    ]
    for rollup, expected in cases:
        assert classify_checks(rollup) == expected, rollup
    # every hard-failure conclusion counts as failing.
    for c in ("FAILURE", "TIMED_OUT", "CANCELLED", "ACTION_REQUIRED", "STARTUP_FAILURE"):
        assert classify_checks([check_run("SUCCESS"), check_run(c)]) == "failing", c


def test_classify_pr_lanes():
    cases = [
        # needs-my-work blockers: changes requested / failing / conflicted.
        ({"review": "CHANGES_REQUESTED"}, "needs_my_work"),
        ({"rollup": [check_run("FAILURE")]}, "needs_my_work"),
        ({"mergeable": "CONFLICTING"}, "needs_my_work"),
        ({"review": "APPROVED", "mergeable": "CONFLICTING"}, "needs_my_work"),
        # parked: awaiting review, or approved-but-not-yet-green.
        ({"review": "REVIEW_REQUIRED"}, "awaiting_review"),
        ({"review": None, "rollup": [PENDING]}, "awaiting_review"),
        ({"review": "APPROVED", "rollup": [PENDING]}, "awaiting_review"),
        # approved + green is the only waiting-to-merge lane.
        ({"review": "APPROVED"}, "waiting_to_merge"),
    ]
    for kwargs, category in cases:
        c = classify_pr(pr(**kwargs))
        assert c.category == category, kwargs
        assert c.needs_my_work == (category == "needs_my_work"), kwargs


def test_unclaimed_claim_issues_filters_out_linked_prs():
    issues = [
        {"number": 10, "closedByPullRequestsReferences": []},
        {"number": 11, "closedByPullRequestsReferences": [{"number": 99}]},
        {"number": 12},  # missing key -> unclaimed
    ]
    assert [i["number"] for i in unclaimed_claim_issues(issues)] == [10, 12]


def test_reconcile_claims_only_when_nothing_needs_work():
    # Clean account -> claim.
    assert reconcile(prs=[], claim_issues=[]).should_claim_new is True

    # Only parked PRs -> still claim; both parked lanes are reported.
    r = reconcile(
        prs=[pr(number=6, review="APPROVED"), pr(number=7, review="REVIEW_REQUIRED")],
        claim_issues=[],
    )
    assert r.should_claim_new is True and r.item_needing_work is None
    assert len(r.waiting_to_merge) == 1 and len(r.awaiting_review) == 1

    # A claim issue that already has a PR does not block.
    r2 = reconcile(
        prs=[pr(number=9, review="APPROVED")],
        claim_issues=[{"number": 22, "closedByPullRequestsReferences": [{"number": 9}]}],
    )
    assert r2.should_claim_new is True


def test_reconcile_finishes_the_one_item_before_claiming():
    # A needs-work PR blocks and is the item to finish.
    r = reconcile(prs=[pr(number=5, review="CHANGES_REQUESTED")], claim_issues=[])
    assert r.should_claim_new is False
    assert r.item_needing_work["kind"] == "pr" and r.item_needing_work["number"] == 5

    # An un-PR'd claim issue also blocks (resume the crashed curation).
    r2 = reconcile(prs=[], claim_issues=[{"number": 20, "closedByPullRequestsReferences": []}])
    assert r2.should_claim_new is False and r2.item_needing_work["kind"] == "claim_issue"

    # A needs-work PR takes precedence over an un-PR'd claim issue.
    r3 = reconcile(
        prs=[pr(number=8, rollup=[check_run("FAILURE")])],
        claim_issues=[{"number": 21, "closedByPullRequestsReferences": []}],
    )
    assert r3.item_needing_work["kind"] == "pr" and r3.item_needing_work["number"] == 8
