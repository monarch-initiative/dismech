"""Unit tests for the pure reconcile/PR classifier (issue #11657)."""

from __future__ import annotations

from dismech.schedule.reconcile import (
    classify_checks,
    classify_pr,
    reconcile,
    unclaimed_claim_issues,
)


def pr(
    number=1,
    review=None,
    mergeable="MERGEABLE",
    rollup=None,
    title="Curate X",
):
    return {
        "number": number,
        "title": title,
        "url": f"https://github.com/monarch-initiative/dismech/pull/{number}",
        "headRefName": "curate/x",
        "isDraft": False,
        "reviewDecision": review,
        "mergeable": mergeable,
        "statusCheckRollup": rollup if rollup is not None else [],
    }


def check_run(conclusion="SUCCESS", status="COMPLETED", name="ci"):
    return {"__typename": "CheckRun", "name": name, "status": status, "conclusion": conclusion}


def status_context(state="SUCCESS", context="legacy"):
    return {"__typename": "StatusContext", "context": context, "state": state}


# --------------------------------------------------------------------------- #
# classify_checks
# --------------------------------------------------------------------------- #


def test_empty_rollup_is_green():
    assert classify_checks([]) == "green"
    assert classify_checks(None) == "green"


def test_all_success_is_green():
    assert classify_checks([check_run("SUCCESS"), check_run("SKIPPED")]) == "green"


def test_pending_when_not_completed():
    assert classify_checks([check_run(status="IN_PROGRESS", conclusion="")]) == "pending"


def test_failing_conclusions_detected():
    for c in ("FAILURE", "TIMED_OUT", "CANCELLED", "ACTION_REQUIRED", "STARTUP_FAILURE"):
        assert classify_checks([check_run("SUCCESS"), check_run(c)]) == "failing"


def test_failing_beats_pending():
    rollup = [check_run(status="IN_PROGRESS", conclusion=""), check_run("FAILURE")]
    assert classify_checks(rollup) == "failing"


def test_status_context_shape_handled():
    assert classify_checks([status_context("SUCCESS")]) == "green"
    assert classify_checks([status_context("FAILURE")]) == "failing"
    assert classify_checks([status_context("PENDING")]) == "pending"


# --------------------------------------------------------------------------- #
# classify_pr
# --------------------------------------------------------------------------- #


def test_changes_requested_needs_my_work():
    c = classify_pr(pr(review="CHANGES_REQUESTED", rollup=[check_run("SUCCESS")]))
    assert c.category == "needs_my_work"
    assert "reviewer requested changes" in c.reasons


def test_failing_checks_needs_my_work():
    c = classify_pr(pr(review=None, rollup=[check_run("FAILURE")]))
    assert c.category == "needs_my_work"
    assert "required checks failing" in c.reasons


def test_conflicting_needs_my_work():
    c = classify_pr(pr(review=None, mergeable="CONFLICTING", rollup=[check_run("SUCCESS")]))
    assert c.category == "needs_my_work"
    assert "merge conflict with base" in c.reasons


def test_awaiting_review_is_parked():
    c = classify_pr(pr(review="REVIEW_REQUIRED", rollup=[check_run("SUCCESS")]))
    assert c.category == "awaiting_review"
    assert not c.needs_my_work


def test_null_review_with_pending_checks_is_awaiting_review():
    c = classify_pr(pr(review=None, rollup=[check_run(status="QUEUED", conclusion="")]))
    assert c.category == "awaiting_review"


def test_approved_and_green_is_waiting_to_merge():
    c = classify_pr(pr(review="APPROVED", rollup=[check_run("SUCCESS")]))
    assert c.category == "waiting_to_merge"
    assert not c.needs_my_work


def test_approved_but_conflicting_still_needs_work():
    c = classify_pr(pr(review="APPROVED", mergeable="CONFLICTING", rollup=[check_run("SUCCESS")]))
    assert c.category == "needs_my_work"


def test_approved_but_pending_checks_is_not_yet_mergeable():
    # Approved but checks still running -> parked (awaiting_review lane), not my work.
    c = classify_pr(pr(review="APPROVED", rollup=[check_run(status="IN_PROGRESS", conclusion="")]))
    assert c.category == "awaiting_review"
    assert not c.needs_my_work


# --------------------------------------------------------------------------- #
# unclaimed_claim_issues
# --------------------------------------------------------------------------- #


def test_unclaimed_filters_out_issues_with_a_pr():
    issues = [
        {"number": 10, "title": "Curate A", "closedByPullRequestsReferences": []},
        {"number": 11, "title": "Curate B", "closedByPullRequestsReferences": [{"number": 99}]},
        {"number": 12, "title": "Curate C"},  # missing key -> treated as unclaimed
    ]
    out = unclaimed_claim_issues(issues)
    assert [i["number"] for i in out] == [10, 12]


# --------------------------------------------------------------------------- #
# reconcile — the finish-first / claim-one decision
# --------------------------------------------------------------------------- #


def test_clean_account_claims_new():
    r = reconcile(prs=[], claim_issues=[])
    assert r.should_claim_new is True
    assert r.item_needing_work is None
    assert "claim one new disease" in r.summary


def test_needs_work_pr_blocks_new_claim():
    prs = [pr(number=5, review="CHANGES_REQUESTED", rollup=[check_run("SUCCESS")])]
    r = reconcile(prs=prs, claim_issues=[])
    assert r.should_claim_new is False
    assert r.item_needing_work["kind"] == "pr"
    assert r.item_needing_work["number"] == 5


def test_only_parked_prs_allow_new_claim():
    prs = [
        pr(number=6, review="APPROVED", rollup=[check_run("SUCCESS")]),  # waiting to merge
        pr(number=7, review="REVIEW_REQUIRED", rollup=[check_run("SUCCESS")]),  # awaiting review
    ]
    r = reconcile(prs=prs, claim_issues=[])
    assert r.should_claim_new is True
    assert r.item_needing_work is None
    assert len(r.waiting_to_merge) == 1
    assert len(r.awaiting_review) == 1


def test_unclaimed_issue_blocks_new_claim():
    issues = [{"number": 20, "title": "Curate D", "closedByPullRequestsReferences": []}]
    r = reconcile(prs=[], claim_issues=issues)
    assert r.should_claim_new is False
    assert r.item_needing_work["kind"] == "claim_issue"
    assert r.item_needing_work["number"] == 20


def test_pr_needing_work_takes_precedence_over_unclaimed_issue():
    prs = [pr(number=8, review=None, rollup=[check_run("FAILURE")])]
    issues = [{"number": 21, "title": "Curate E", "closedByPullRequestsReferences": []}]
    r = reconcile(prs=prs, claim_issues=issues)
    assert r.should_claim_new is False
    assert r.item_needing_work["kind"] == "pr"
    assert r.item_needing_work["number"] == 8


def test_issue_with_linked_pr_does_not_block():
    # The claim issue has a PR (which is itself parked), so nothing needs my work.
    prs = [pr(number=9, review="APPROVED", rollup=[check_run("SUCCESS")])]
    issues = [{"number": 22, "closedByPullRequestsReferences": [{"number": 9}]}]
    r = reconcile(prs=prs, claim_issues=issues)
    assert r.should_claim_new is True
