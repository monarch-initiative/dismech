"""Tests for the deterministic auto-merge predicate used by pr-shepherd.

The predicate decides whether a PR is squash-merged without human review, so
every criterion gets an explicit negative test: a bug that loosens the
predicate merges someone's unfinished work.
"""

import importlib.util
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

_SPEC = importlib.util.spec_from_file_location(
    "auto_merge_ready_prs",
    Path(__file__).resolve().parents[1] / "scripts" / "auto_merge_ready_prs.py",
)
auto_merge = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = auto_merge
_SPEC.loader.exec_module(auto_merge)

NOW = datetime(2026, 8, 5, 12, 0, 0, tzinfo=timezone.utc)


def make_pr(**overrides):
    """A PR payload that satisfies every criterion; override to break one."""
    pr = {
        "number": 100,
        "title": "feat: Add Example Disease",
        "state": "OPEN",
        "isDraft": False,
        "baseRefName": "main",
        "headRefName": "claude/curate-example",
        "assignees": [],
        "reviewDecision": "APPROVED",
        "mergeable": "MERGEABLE",
        "mergeStateStatus": "CLEAN",
        "createdAt": (NOW - timedelta(days=5)).isoformat().replace("+00:00", "Z"),
        "statusCheckRollup": [
            {"name": "test (3.13)", "status": "COMPLETED", "conclusion": "SUCCESS"},
            {"name": "claude-review", "status": "COMPLETED", "conclusion": "SUCCESS"},
        ],
    }
    pr.update(overrides)
    return pr


def decide(pr, **kwargs):
    kwargs.setdefault("now", NOW)
    kwargs.setdefault("min_age_days", 3)
    kwargs.setdefault("base_branch", "main")
    return auto_merge.evaluate(pr, **kwargs)


# --- the happy path -------------------------------------------------------


def test_fully_ready_pr_is_eligible():
    assert decide(make_pr()).eligible


def test_human_authored_pr_is_eligible():
    """Authorship is deliberately not a criterion (see the workflow step)."""
    assert decide(make_pr(headRefName="ci/some-fix")).eligible


def test_skipped_and_neutral_checks_do_not_block():
    pr = make_pr(
        statusCheckRollup=[
            {"name": "test (3.13)", "status": "COMPLETED", "conclusion": "SUCCESS"},
            {"name": "claude", "status": "COMPLETED", "conclusion": "SKIPPED"},
            {"name": "optional", "status": "COMPLETED", "conclusion": "NEUTRAL"},
        ]
    )
    assert decide(pr).eligible


def test_legacy_status_contexts_are_understood():
    pr = make_pr(statusCheckRollup=[{"context": "ci/legacy", "state": "SUCCESS"}])
    assert decide(pr).eligible


# --- one test per blocking criterion --------------------------------------


@pytest.mark.parametrize(
    "overrides,expected",
    [
        ({"state": "CLOSED"}, "not open"),
        ({"isDraft": True}, "draft"),
        ({"baseRefName": "some-feature"}, "base branch"),
        ({"assignees": [{"login": "cmungall"}]}, "assigned to cmungall"),
        ({"reviewDecision": "CHANGES_REQUESTED"}, "not approved"),
        ({"reviewDecision": "REVIEW_REQUIRED"}, "not approved"),
        ({"reviewDecision": None}, "not approved"),
        ({"mergeable": "CONFLICTING"}, "merge conflicts"),
        ({"mergeable": "UNKNOWN"}, "mergeability is unknown"),
        ({"mergeStateStatus": "BLOCKED"}, "not clean"),
        ({"mergeStateStatus": "BEHIND"}, "not clean"),
        ({"mergeStateStatus": "DIRTY"}, "not clean"),
        ({"mergeStateStatus": "UNSTABLE"}, "not clean"),
    ],
)
def test_blocking_criteria(overrides, expected):
    decision = decide(make_pr(**overrides))
    assert not decision.eligible
    assert expected in decision.reason


def test_pr_younger_than_three_days_is_skipped():
    pr = make_pr(
        createdAt=(NOW - timedelta(days=2, hours=23)).isoformat().replace("+00:00", "Z")
    )
    decision = decide(pr)
    assert not decision.eligible
    assert "<3d" in decision.reason
    # Tagged so the near-miss report can drop it: it needs no human attention.
    assert decision.code == auto_merge.TOO_YOUNG


def test_only_the_age_criterion_is_tagged_too_young():
    """Guards the report filter: nothing else may be silently suppressed."""
    for overrides in (
        {"isDraft": True},
        {"assignees": [{"login": "cmungall"}]},
        {"reviewDecision": "CHANGES_REQUESTED"},
        {"mergeable": "CONFLICTING"},
        {"mergeStateStatus": "BLOCKED"},
        {"statusCheckRollup": []},
    ):
        assert decide(make_pr(**overrides)).code != auto_merge.TOO_YOUNG


def test_pr_just_over_three_days_is_eligible():
    pr = make_pr(
        createdAt=(NOW - timedelta(days=3, minutes=1))
        .isoformat()
        .replace("+00:00", "Z")
    )
    assert decide(pr).eligible


def test_min_age_days_is_configurable():
    pr = make_pr(createdAt=(NOW - timedelta(days=4)).isoformat().replace("+00:00", "Z"))
    assert decide(pr).eligible
    assert not decide(pr, min_age_days=7).eligible


# --- check rollup ---------------------------------------------------------


@pytest.mark.parametrize(
    "rollup,expected",
    [
        (None, "no status checks"),
        ([], "no status checks"),
        (
            [{"name": "test (3.13)", "status": "COMPLETED", "conclusion": "FAILURE"}],
            "checks not passing: test (3.13)=failure",
        ),
        (
            [{"name": "build", "status": "COMPLETED", "conclusion": "CANCELLED"}],
            "checks not passing",
        ),
        (
            [{"name": "build", "status": "COMPLETED", "conclusion": "TIMED_OUT"}],
            "checks not passing",
        ),
        (
            [
                {"name": "ok", "status": "COMPLETED", "conclusion": "SUCCESS"},
                {"name": "slow", "status": "IN_PROGRESS", "conclusion": None},
            ],
            "checks still running: slow",
        ),
        (
            [{"name": "queued", "status": "QUEUED", "conclusion": None}],
            "checks still running",
        ),
        ([{"context": "ci/legacy", "state": "FAILURE"}], "checks not passing"),
        ([{"context": "ci/legacy", "state": "PENDING"}], "checks still running"),
        (
            [{"name": "claude", "status": "COMPLETED", "conclusion": "SKIPPED"}],
            "no successful check",
        ),
    ],
)
def test_rollup_blocks_merge(rollup, expected):
    decision = decide(make_pr(statusCheckRollup=rollup))
    assert not decision.eligible
    assert expected in decision.reason


def test_failure_is_reported_ahead_of_pending():
    """A failing check is the actionable signal even when others still run."""
    decision = auto_merge.check_rollup_decision(
        [
            {"name": "slow", "status": "IN_PROGRESS", "conclusion": None},
            {"name": "test (3.13)", "status": "COMPLETED", "conclusion": "FAILURE"},
        ]
    )
    assert not decision.eligible
    assert "not passing" in decision.reason


def test_list_stage_defers_check_evaluation():
    """The cheap list scan has no rollup; it must not reject on that alone."""
    pr = make_pr()
    del pr["statusCheckRollup"]
    assert not decide(pr).eligible
    assert decide(pr, final=False).eligible


def test_list_stage_defers_unresolved_mergeability():
    """GitHub reports UNKNOWN mergeability in bulk lists and only computes it
    when a single PR is queried, so the list stage must not reject on it —
    otherwise no PR is ever promoted to the per-PR check that resolves it."""
    pr = make_pr(mergeable="UNKNOWN", mergeStateStatus="UNKNOWN")
    assert decide(pr, final=False).eligible
    assert not decide(pr).eligible


def test_list_stage_still_rejects_known_conflicts():
    """A conflict IS reported reliably in bulk, so don't waste a per-PR call."""
    assert not decide(make_pr(mergeable="CONFLICTING"), final=False).eligible


@pytest.mark.parametrize(
    "overrides",
    [
        {"isDraft": True},
        {"assignees": [{"login": "cmungall"}]},
        {"reviewDecision": "CHANGES_REQUESTED"},
        {"baseRefName": "some-feature"},
        {"createdAt": (NOW - timedelta(hours=4)).isoformat().replace("+00:00", "Z")},
    ],
)
def test_list_stage_rejects_criteria_it_can_answer(overrides):
    assert not decide(make_pr(**overrides), final=False).eligible


# --- reporting ------------------------------------------------------------


def test_summary_reports_merges_skips_and_failures():
    report = auto_merge.render_summary(
        merged=[{"number": 1, "title": "feat: A"}],
        skipped=[{"number": 2, "reason": "draft"}],
        failed=[{"number": 3, "reason": "protected branch"}],
    )
    assert "Merged 1" in report
    assert "#1 — feat: A" in report
    assert "#2 — draft" in report
    assert "Failed to merge 1" in report


def test_summary_when_nothing_merged():
    report = auto_merge.render_summary(merged=[], skipped=[], failed=[])
    assert "Merged 0" in report
