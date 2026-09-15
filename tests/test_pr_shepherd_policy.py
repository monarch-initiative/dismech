"""Tests for deterministic PR-shepherd ingress policy."""

import importlib.util
import sys
from pathlib import Path

import pytest

_SPEC = importlib.util.spec_from_file_location(
    "pr_shepherd_policy",
    Path(__file__).resolve().parents[1] / "scripts" / "pr_shepherd_policy.py",
)
policy = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = policy
_SPEC.loader.exec_module(policy)


@pytest.mark.parametrize(
    "raw",
    [
        "ai4c-agent",
        "AI4C-Agent",
        "app/ai4c-agent",
        "ai4c-agent[bot]",
        {"login": "app/ai4c-agent"},
    ],
)
def test_ai4c_login_spellings_normalize(raw):
    assert policy.normalize_login(raw) == "ai4c-agent"


@pytest.mark.parametrize(
    "raw,expected",
    [
        ("app/claude", "claude"),
        ("github-actions[bot]", "github-actions"),
        ("dragon-ai-agent", "dragon-ai-agent"),
    ],
)
def test_other_known_agent_logins_normalize(raw, expected):
    assert policy.normalize_login(raw) == expected


def make_pr(**overrides):
    pr = {
        "number": 7,
        "author": {"login": "app/ai4c-agent", "is_bot": True},
        "headRefName": "curation/example",
        "headRefOid": "head-7",
        "baseRefName": "main",
        "assignees": [],
        "isDraft": False,
        "state": "OPEN",
        "title": "🤖 Weekly Compliance Fixes: Example",
        "reviewDecision": "CHANGES_REQUESTED",
        "updatedAt": "2026-08-20T00:00:00Z",
        "baseRefOid": "old-base",
        "mergeable": "MERGEABLE",
    }
    pr.update(overrides)
    return pr


def test_agent_candidates_include_drafts():
    assert policy.agent_candidate_decision(make_pr(isDraft=True)).eligible


def test_human_claude_branch_is_not_an_author_override():
    decision = policy.agent_candidate_decision(
        make_pr(author={"login": "cmungall", "is_bot": False}, headRefName="claude/fix")
    )
    assert not decision.eligible


def test_human_account_named_claude_is_not_mistaken_for_the_bot():
    decision = policy.agent_candidate_decision(
        make_pr(author={"login": "claude", "is_bot": False})
    )
    assert not decision.eligible
    assert "verified Bot identity" in decision.reason


def test_known_machine_user_is_allowed_without_bot_type():
    assert policy.agent_candidate_decision(
        make_pr(author={"login": "dragon-ai-agent", "is_bot": False})
    ).eligible


@pytest.mark.parametrize("overrides", [{"state": "CLOSED"}, {"state": None}])
def test_agent_candidates_fail_closed_unless_open(overrides):
    assert not policy.agent_candidate_decision(make_pr(**overrides)).eligible


@pytest.mark.parametrize("base", ["feature", None])
def test_agent_candidates_require_main_base(base):
    assert not policy.agent_candidate_decision(make_pr(baseRefName=base)).eligible


def test_assigned_pr_is_a_hold_for_the_agent_lane():
    decision = policy.agent_candidate_decision(
        make_pr(assignees=[{"login": "cmungall"}])
    )
    assert not decision.eligible
    assert "assigned to cmungall" in decision.reason


def test_generated_lane_is_excluded_for_every_author():
    decision = policy.agent_candidate_decision(
        make_pr(headRefName="auto/generate-pages")
    )
    assert not decision.eligible


def test_other_automated_lanes_are_also_excluded():
    decision = policy.agent_candidate_decision(
        make_pr(headRefName="auto/warm-reference-cache")
    )
    assert not decision.eligible


def test_scan_candidates_are_ranked_bounded_and_leave_ready_work_to_controller(
    monkeypatch,
):
    prs = [
        make_pr(
            number=1,
            headRefOid="head-1",
            reviewDecision="APPROVED",
            baseRefOid="old-base",
            mergeable="MERGEABLE",
            updatedAt="2026-08-05T00:00:00Z",
        ),
        make_pr(
            number=2,
            headRefOid="head-2",
            reviewDecision="APPROVED",
            baseRefOid="old-base",
            mergeable="CONFLICTING",
            updatedAt="2026-08-01T00:00:00Z",
        ),
        make_pr(number=3, headRefOid="head-3", updatedAt="2026-07-01T00:00:00Z"),
        make_pr(number=4, headRefOid="head-4", reviewDecision="REVIEW_REQUIRED"),
        make_pr(
            number=5,
            headRefOid="head-5",
            reviewDecision="APPROVED",
            baseRefOid="current-base",
            mergeable="MERGEABLE",
        ),
    ]
    calls = []

    def fake_gh_json(args):
        calls.append(args)
        if args[0:2] == ["pr", "list"]:
            return prs
        if args[0] == "api" and "/branches/main" in args[1]:
            return {"commit": {"sha": "current-base"}}
        if args[0] == "api" and "/compare/" in args[1]:
            head = args[1].rsplit("...", maxsplit=1)[-1]
            integrated = head == "head-5"
            return {
                "base_commit": {"sha": "current-base"},
                "merge_base_commit": {
                    "sha": "current-base" if integrated else "old-base"
                },
                "behind_by": 0 if integrated else 1,
            }
        return {
            "isDraft": False,
            "mergeStateStatus": "CLEAN",
            "statusCheckRollup": [{"status": "COMPLETED", "conclusion": "SUCCESS"}],
        }

    monkeypatch.setattr(policy, "_gh_json", fake_gh_json)
    selected = policy.list_agent_candidates("o/r", limit=3)
    assert [pr["number"] for pr in selected] == [1, 2, 3]
    list_fields = calls[0][calls[0].index("--json") + 1]
    assert "baseRefOid" in list_fields
    assert "headRefOid" in list_fields
    assert "reviewDecision" in list_fields


def test_aligned_approved_red_pr_stays_in_agent_lane(monkeypatch):
    red = make_pr(
        number=8,
        headRefOid="head-8",
        reviewDecision="APPROVED",
        mergeable="MERGEABLE",
    )

    def fake_gh_json(args):
        if args[0:2] == ["pr", "list"]:
            return [red]
        if args[0] == "api" and "/branches/main" in args[1]:
            return {"commit": {"sha": "current-base"}}
        if args[0] == "api":
            return {
                "base_commit": {"sha": "current-base"},
                "merge_base_commit": {"sha": "current-base"},
                "behind_by": 0,
            }
        return {
            "isDraft": False,
            "mergeStateStatus": "UNSTABLE",
            "statusCheckRollup": [{"status": "COMPLETED", "conclusion": "FAILURE"}],
        }

    monkeypatch.setattr(policy, "_gh_json", fake_gh_json)
    assert [pr["number"] for pr in policy.list_agent_candidates("o/r")] == [8]


def test_base_ref_oid_is_not_used_as_ancestry_proof():
    comparison = {
        "base_commit": {"sha": "current-base"},
        "merge_base_commit": {"sha": "older-base"},
        "behind_by": 2,
    }
    assert not policy._comparison_contains_base(comparison, "current-base", "head-8")


def test_specific_candidate_uses_same_state_and_base_guards(monkeypatch):
    calls = []

    def fake_gh_json(args):
        calls.append(args)
        return make_pr(state="CLOSED")

    monkeypatch.setattr(policy, "_gh_json", fake_gh_json)
    assert policy.list_agent_candidates("o/r", specific_pr=7) == []
    fields = calls[0][calls[0].index("--json") + 1]
    assert "state" in fields
    assert "baseRefName" in fields
