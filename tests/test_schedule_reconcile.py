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


def pr(
    number=1, review=None, mergeable="MERGEABLE", rollup=None, reviews=None, files=None
):
    out = {
        "number": number,
        "title": "Curate X",
        "url": f"https://github.com/monarch-initiative/dismech/pull/{number}",
        "headRefName": "curate/x",
        "isDraft": False,
        "reviewDecision": review,
        "mergeable": mergeable,
        "statusCheckRollup": rollup if rollup is not None else [check_run("SUCCESS")],
    }
    if reviews is not None:
        out["reviews"] = reviews
    if files is not None:
        out["files"] = files
    return out


def check_run(conclusion="SUCCESS", status="COMPLETED"):
    return {
        "__typename": "CheckRun",
        "name": "ci",
        "status": status,
        "conclusion": conclusion,
    }


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
        # CANCELLED is a superseded run, not a curator-fixable failure -> pending.
        ([check_run("SUCCESS"), check_run("CANCELLED")], "pending"),
    ]
    for rollup, expected in cases:
        assert classify_checks(rollup) == expected, rollup
    # every hard-failure conclusion counts as failing (CANCELLED excluded above).
    for c in ("FAILURE", "TIMED_OUT", "ACTION_REQUIRED", "STARTUP_FAILURE"):
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
        claim_issues=[
            {"number": 22, "closedByPullRequestsReferences": [{"number": 9}]}
        ],
    )
    assert r2.should_claim_new is True


def test_reconcile_finishes_the_one_item_before_claiming():
    # A needs-work PR blocks and is the item to finish.
    r = reconcile(prs=[pr(number=5, review="CHANGES_REQUESTED")], claim_issues=[])
    assert r.should_claim_new is False
    assert r.item_needing_work["kind"] == "pr" and r.item_needing_work["number"] == 5

    # An un-PR'd claim issue also blocks (resume the crashed curation).
    r2 = reconcile(
        prs=[], claim_issues=[{"number": 20, "closedByPullRequestsReferences": []}]
    )
    assert (
        r2.should_claim_new is False and r2.item_needing_work["kind"] == "claim_issue"
    )

    # A needs-work PR takes precedence over an un-PR'd claim issue, and the one
    # chosen is deterministic (lowest number) regardless of input order.
    r3 = reconcile(
        prs=[
            pr(number=12, rollup=[check_run("FAILURE")]),
            pr(number=8, review="CHANGES_REQUESTED"),
        ],
        claim_issues=[{"number": 21, "closedByPullRequestsReferences": []}],
    )
    assert r3.item_needing_work["kind"] == "pr" and r3.item_needing_work["number"] == 8


def test_hand_off_able_defers_human_review_and_code_prs():
    # No reviews/files passed -> hand-off-able (back-compat: attempt everything).
    c = classify_pr(pr(number=1, review="CHANGES_REQUESTED"))
    assert c.hand_off_able is True and c.defer_reasons == ()

    # A bot reviewer's changes-requested is still hand-off-able.
    bot = classify_pr(
        pr(
            number=2,
            review="CHANGES_REQUESTED",
            reviews=[{"state": "CHANGES_REQUESTED", "login": "ai4c-reviewer[bot]"}],
        )
    )
    assert bot.hand_off_able is True

    # A human reviewer's changes-requested defers to the author. Latest state per
    # author wins, and the gh user/author nesting is accepted.
    human = classify_pr(
        pr(
            number=3,
            review="CHANGES_REQUESTED",
            reviews=[
                {"state": "COMMENTED", "user": {"login": "caufieldjh"}},
                {"state": "CHANGES_REQUESTED", "user": {"login": "caufieldjh"}},
            ],
        )
    )
    assert human.hand_off_able is False
    assert any("caufieldjh" in r for r in human.defer_reasons)

    # A code/config/docs change is deferred even with only a bot review.
    for path in (
        "src/dismech/schedule/reconcile.py",
        "CLAUDE.md",
        ".claude/skills/x/SKILL.md",
        "docs/x.md",
        "project.justfile",
    ):
        code = classify_pr(
            pr(number=4, rollup=[check_run("FAILURE")], files=[{"filename": path}])
        )
        assert code.hand_off_able is False, path

    # A pure-curation PR (only KB content) stays hand-off-able.
    curation = classify_pr(
        pr(
            number=5,
            rollup=[check_run("FAILURE")],
            files=[
                "kb/disorders/X.yaml",
                "history/disorders/X/r.yaml",
                "references_cache/PMID_1.md",
            ],
        )
    )
    assert curation.hand_off_able is True and curation.defer_reasons == ()


def test_reconcile_deferred_pr_does_not_block_a_claim():
    # One deferred human-review PR, nothing else -> still claim; it is reported.
    human_review = [{"state": "CHANGES_REQUESTED", "login": "cmungall"}]
    r = reconcile(
        prs=[pr(number=12, review="CHANGES_REQUESTED", reviews=human_review)],
        claim_issues=[],
    )
    assert r.should_claim_new is True
    assert r.item_needing_work is None
    assert [c.number for c in r.deferred_prs] == [12]
    assert "#12" in r.summary

    # An actionable PR is still chosen ahead of claiming, and a deferred one does
    # not shadow it: #8 (actionable) is the item, #5 (human review) is deferred.
    r2 = reconcile(
        prs=[
            pr(number=5, review="CHANGES_REQUESTED", reviews=human_review),
            pr(number=8, review="CHANGES_REQUESTED"),
        ],
        claim_issues=[],
    )
    assert r2.item_needing_work["number"] == 8
    assert [c.number for c in r2.deferred_prs] == [5]
    assert r2.should_claim_new is False

    # A deferred PR does not block resuming an un-PR'd claim issue either.
    r3 = reconcile(
        prs=[pr(number=9, review="CHANGES_REQUESTED", reviews=human_review)],
        claim_issues=[{"number": 20, "closedByPullRequestsReferences": []}],
    )
    assert r3.item_needing_work["kind"] == "claim_issue"
    assert [c.number for c in r3.deferred_prs] == [9]


def test_reconcile_identity_gate():
    # Right account: behaves normally (clean -> claim).
    ok = reconcile([], [], authenticated_login="alice", expected_login="alice")
    assert ok.identity_ok is True and ok.should_claim_new is True

    # Wrong / missing account: do nothing at all, even though lists are empty.
    for who in ("bot[bot]", None, ""):
        r = reconcile([], [], authenticated_login=who, expected_login="alice")
        assert r.identity_ok is False
        assert r.should_claim_new is False and r.item_needing_work is None
        assert "expected alice" in r.summary

    # No expected_login configured -> gate is the caller's responsibility (open).
    assert reconcile([], []).should_claim_new is True
