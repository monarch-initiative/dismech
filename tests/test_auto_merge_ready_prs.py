"""Tests for the deterministic auto-merge predicate used by pr-shepherd.

The predicate decides whether a PR is squash-merged without human review, so
every criterion gets an explicit negative test: a bug that loosens the
predicate merges someone's unfinished work.
"""

import argparse
import importlib.util
import json
import subprocess
import sys
from datetime import UTC, datetime, timedelta
from pathlib import Path

import pytest

_SPEC = importlib.util.spec_from_file_location(
    "auto_merge_ready_prs",
    Path(__file__).resolve().parents[1] / "scripts" / "auto_merge_ready_prs.py",
)
auto_merge = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = auto_merge
_SPEC.loader.exec_module(auto_merge)

NOW = datetime(2026, 8, 5, 12, 0, 0, tzinfo=UTC)


def make_pr(**overrides):
    """A PR payload that satisfies every criterion; override to break one."""
    pr = {
        "number": 100,
        "title": "feat: Add Example Disease",
        "state": "OPEN",
        "isDraft": False,
        "baseRefName": "main",
        "headRefName": "claude/curate-example",
        "headRefOid": "head123",
        "baseRefOid": "base123",
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


def test_weekly_compliance_pr_uses_the_common_controller():
    pr = make_pr(
        headRefName="weekly-compliance-2026-08",
        isDraft=True,
        mergeStateStatus="DRAFT",
    )
    assert decide(pr).eligible


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


def test_typename_discriminates_rollup_entries():
    """gh tags each rollup entry; prefer that over guessing from shape."""
    pr = make_pr(
        statusCheckRollup=[
            {
                "__typename": "CheckRun",
                "name": "test (3.13)",
                "status": "COMPLETED",
                "conclusion": "SUCCESS",
            },
            {"__typename": "StatusContext", "context": "ci/legacy", "state": "SUCCESS"},
        ]
    )
    assert decide(pr).eligible


def test_typename_wins_over_shape():
    """A StatusContext that also carries a `status` key must still be read as a
    StatusContext — this is the failure mode `__typename` guards against."""
    decision = auto_merge.check_rollup_decision(
        [
            {
                "__typename": "StatusContext",
                "context": "ci/legacy",
                "state": "FAILURE",
                "status": "COMPLETED",
            }
        ]
    )
    assert not decision.eligible
    assert "ci/legacy=failure" in decision.reason


# --- one test per blocking criterion --------------------------------------


@pytest.mark.parametrize(
    "overrides,expected",
    [
        ({"state": "CLOSED"}, "not open"),
        ({"baseRefName": "some-feature"}, "base branch"),
        ({"assignees": [{"login": "cmungall"}]}, "assigned to human(s): cmungall"),
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


def test_draft_is_included_by_repository_policy():
    pr = make_pr(isDraft=True, mergeStateStatus="DRAFT")
    assert decide(pr).eligible


def test_draft_can_be_rejected_during_post_transition_verification():
    decision = decide(make_pr(isDraft=True), include_drafts=False)
    assert not decision.eligible
    assert decision.reason == "draft"


def test_draft_blocked_merge_state_is_accepted_only_for_preflight():
    pr = make_pr(isDraft=True, mergeStateStatus="BLOCKED")
    assert decide(pr).eligible
    assert not decide(pr, include_drafts=False).eligible


def test_auto_lane_pr_uses_the_common_controller():
    assert decide(make_pr(headRefName="auto/generate-pages")).eligible


@pytest.mark.parametrize(
    "login",
    ["dragon-ai-agent", "github-actions[bot]", "ai4c-agent", "AI4C-AGENT[bot]"],
)
def test_machine_assignee_does_not_hold_pr(login):
    assert decide(make_pr(assignees=[{"login": login}])).eligible


def test_machine_and_human_assignee_still_holds_pr():
    decision = decide(
        make_pr(
            assignees=[
                {"login": "dragon-ai-agent"},
                {"login": "cmungall"},
            ]
        )
    )
    assert not decision.eligible
    assert decision.reason == "assigned to human(s): cmungall"


def test_missing_assignee_login_fails_closed_as_human():
    assert not decide(make_pr(assignees=[{}])).eligible


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


@pytest.mark.parametrize("value,expected", [("0", 0), ("3", 3), ("14", 14)])
def test_non_negative_int_accepts_valid_thresholds(value, expected):
    assert auto_merge.non_negative_int(value) == expected


@pytest.mark.parametrize("value", ["-1", "-3"])
def test_non_negative_int_rejects_negatives(value):
    """A negative threshold makes every PR pass the age check — i.e. silently
    merges regardless of age. Settable from a workflow input, so it must fail
    loudly rather than widen the merge criteria."""
    with pytest.raises(argparse.ArgumentTypeError, match="zero or positive"):
        auto_merge.non_negative_int(value)


def test_default_scan_limit_covers_the_large_backlog(monkeypatch, tmp_path):
    calls = []

    def fake_gh(args, *, token=None):
        calls.append(args)
        if args[:2] == ["pr", "list"]:
            return "[]"
        return ""

    monkeypatch.setattr(auto_merge, "_gh", fake_gh)
    code = auto_merge.main(
        ["--repo", "o/r", "--dry-run", "--summary-file", str(tmp_path / "s.md")]
    )
    assert code == 0
    list_call = next(call for call in calls if call[:2] == ["pr", "list"])
    assert list_call[list_call.index("--limit") + 1] == "1000"


@pytest.mark.parametrize("value", ["", "three", "3.5", "1e3"])
def test_non_negative_int_rejects_non_integers(value):
    with pytest.raises(ValueError):
        auto_merge.non_negative_int(value)


def test_zero_threshold_merges_a_brand_new_pr():
    """0 is explicitly allowed: it means 'no age requirement'."""
    pr = make_pr(
        createdAt=(NOW - timedelta(minutes=1)).isoformat().replace("+00:00", "Z")
    )
    assert not decide(pr).eligible
    assert decide(pr, min_age_days=0).eligible


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
        {"assignees": [{"login": "cmungall"}]},
        {"reviewDecision": "CHANGES_REQUESTED"},
        {"baseRefName": "some-feature"},
        {"createdAt": (NOW - timedelta(hours=4)).isoformat().replace("+00:00", "Z")},
    ],
)
def test_list_stage_rejects_criteria_it_can_answer(overrides):
    assert not decide(make_pr(**overrides), final=False).eligible


# --- benign vs real merge failures ----------------------------------------

# Verbatim stderr from `gh pr merge --squash --match-head-commit <wrong sha>`
# against a blocked PR (gh 2.x). The shape is what matters: the actionable
# sentence is FIRST and two hint lines follow, so anything that classifies or
# reports on the last line reads the advice instead of the diagnosis.
GH_REFUSAL_STDERR = (
    "X Pull request monarch-initiative/dismech#8018 is not mergeable: "
    "the base branch policy prohibits the merge.\n"
    "To have the pull request merged after all the requirements have been met, "
    "add the `--auto` flag.\n"
    "To use administrator privileges to immediately merge the pull request, "
    "add the `--admin` flag.\n"
)


def test_real_gh_refusal_is_classified_benign():
    """Regression: classifying on the last line saw only the `--admin` hint,
    so this race was reported as a hard failure and turned the workflow red."""
    assert auto_merge.is_benign_merge_failure(GH_REFUSAL_STDERR)
    # The old last-line-only behaviour, pinned so it cannot silently return.
    assert not auto_merge.is_benign_merge_failure(GH_REFUSAL_STDERR.splitlines()[-1])


def test_real_gh_refusal_reports_the_diagnosis_not_the_hint():
    exc = subprocess.CalledProcessError(1, "gh", stderr=GH_REFUSAL_STDERR)
    reported = auto_merge._gh_error(exc)
    assert reported.startswith("Pull request")
    assert "is not mergeable" in reported
    assert "--admin" not in reported


def test_gh_error_strips_status_markers():
    exc = subprocess.CalledProcessError(1, "gh", stderr="! something happened\n")
    assert auto_merge._gh_error(exc) == "something happened"


def test_discovery_subprocesses_cannot_inherit_the_writer_token(monkeypatch):
    environments = []

    class Result:
        stdout = ""

    def fake_run(*args, **kwargs):
        environments.append(kwargs["env"])
        return Result()

    monkeypatch.setenv("GH_TOKEN", "reader")
    monkeypatch.setenv("GH_MERGE_TOKEN", "writer")
    monkeypatch.setattr(auto_merge.subprocess, "run", fake_run)
    auto_merge._gh(["pr", "list"])
    auto_merge._gh(["pr", "merge"], token="writer")
    assert environments[0]["GH_TOKEN"] == "reader"
    assert "GH_MERGE_TOKEN" not in environments[0]
    assert environments[1]["GH_TOKEN"] == "writer"
    assert "GH_MERGE_TOKEN" not in environments[1]


def test_gh_error_strips_a_prefix_not_a_character_set():
    """`lstrip("X!  ")` would eat the leading `X` *and* `-` here."""
    exc = subprocess.CalledProcessError(1, "gh", stderr="X-Ratelimit is 0\n")
    assert auto_merge._gh_error(exc) == "X-Ratelimit is 0"


def test_gh_upgrade_banner_is_not_reported_as_the_failure():
    """gh appends its release banner to stderr last, so a last-line rule would
    report a version notice as the reason the merge failed."""
    exc = subprocess.CalledProcessError(
        1,
        "gh",
        stderr=(
            "X Pull request #42 is not mergeable: head branch was modified.\n"
            "\n"
            "A new release of gh is available: 2.40.0 → 2.62.0\n"
        ),
    )
    assert "not mergeable" in auto_merge._gh_error(exc)
    assert "new release" not in auto_merge._gh_error(exc)
    assert auto_merge.is_benign_merge_failure(exc.stderr)


@pytest.mark.parametrize(
    "message",
    [
        "Head branch was modified. Review and try the merge again.",
        "Pull request #7 is already merged",
        "Pull request is not mergeable",
        "GraphQL: Base branch was modified",
    ],
)
def test_races_are_benign(message):
    assert auto_merge.is_benign_merge_failure(message)


@pytest.mark.parametrize(
    "message",
    [
        "HTTP 403: Resource not accessible by integration",
        "HTTP 502: Bad Gateway",
        "protected branch rules not met",
        "gh exited 1",
    ],
)
def test_real_errors_are_not_benign(message):
    assert not auto_merge.is_benign_merge_failure(message)


# --- end-to-end main() ----------------------------------------------------


def _run_main(
    monkeypatch, tmp_path, *, view, listed=None, extra_args=(), queue_payload=None
):
    """Drive main() against a stubbed gh, returning (exit code, gh calls)."""
    if listed is None:
        listed = [make_pr(number=42, mergeable="MERGEABLE")]
    views = view if isinstance(view, list) else [view]
    view_index = 0
    calls = []

    def fake_gh(args, *, token=None):
        nonlocal view_index
        calls.append(args)
        if args[:2] == ["pr", "list"]:
            return json.dumps(listed)
        if args[:2] == ["pr", "view"]:
            payload = views[min(view_index, len(views) - 1)]
            view_index += 1
            return json.dumps(payload)
        if args[:2] == ["api", "graphql"]:
            # No queue by default, so existing tests keep the direct-merge path.
            return queue_payload or json.dumps(
                {"data": {"repository": {"mergeQueue": None}}}
            )
        return ""

    monkeypatch.setattr(auto_merge, "_gh", fake_gh)
    monkeypatch.setattr(auto_merge.time, "sleep", lambda _: None)
    monkeypatch.setenv("GH_MERGE_TOKEN", "writer-token")
    code = auto_merge.main(
        [
            "--repo",
            "o/r",
            "--summary-file",
            str(tmp_path / "summary.md"),
            *extra_args,
        ]
    )
    return code, calls


def test_main_merges_a_fully_ready_pr(monkeypatch, tmp_path):
    view = make_pr(number=42, headRefOid="cafe1234")
    code, calls = _run_main(monkeypatch, tmp_path, view=view)
    merges = [c for c in calls if c[:2] == ["pr", "merge"]]
    assert code == 0
    assert len(merges) == 1
    assert "cafe1234" in merges[0]


def test_specific_pr_never_falls_back_to_a_global_scan(monkeypatch, tmp_path):
    target = make_pr(number=99, headRefOid="head99")
    code, calls = _run_main(
        monkeypatch,
        tmp_path,
        view=target,
        listed=[make_pr(number=42)],
        extra_args=["--specific-pr", "99"],
    )
    assert code == 0
    assert not [call for call in calls if call[:2] == ["pr", "list"]]
    merges = [call for call in calls if call[:2] == ["pr", "merge"]]
    assert len(merges) == 1
    assert merges[0][2] == "99"


def test_specific_pr_reports_why_an_unapproved_target_was_skipped(
    monkeypatch, tmp_path
):
    target = make_pr(
        number=99,
        headRefOid="head99",
        reviewDecision="REVIEW_REQUIRED",
    )
    code, calls = _run_main(
        monkeypatch,
        tmp_path,
        view=target,
        listed=[make_pr(number=42)],
        extra_args=["--specific-pr", "99"],
    )
    assert code == 0
    assert not [call for call in calls if call[:2] == ["pr", "list"]]
    assert not [call for call in calls if call[:2] == ["pr", "merge"]]
    summary = (tmp_path / "summary.md").read_text()
    assert "#99 — review decision is review_required, not approved" in summary


def test_main_does_not_merge_when_only_the_per_pr_view_disqualifies(
    monkeypatch, tmp_path
):
    """The list payload looks ready but the fresh view is BLOCKED. If the
    second loop ever regressed to `final=False`, this PR would be merged on
    stale data — that is the bug this test exists to catch."""
    view = make_pr(number=42, mergeStateStatus="BLOCKED")
    code, calls = _run_main(monkeypatch, tmp_path, view=view)
    assert code == 0
    assert not [c for c in calls if c[:2] == ["pr", "merge"]]


def test_main_does_not_merge_when_checks_fail(monkeypatch, tmp_path):
    view = make_pr(
        number=42,
        statusCheckRollup=[
            {"name": "test (3.13)", "status": "COMPLETED", "conclusion": "FAILURE"}
        ],
    )
    code, calls = _run_main(monkeypatch, tmp_path, view=view)
    assert code == 0
    assert not [c for c in calls if c[:2] == ["pr", "merge"]]


def test_final_pr_read_catches_a_hold_added_after_health(monkeypatch, tmp_path):
    before = make_pr(number=42, headRefOid="cafe1234")
    after = make_pr(
        number=42,
        headRefOid="cafe1234",
        assignees=[{"login": "cmungall"}],
    )
    code, calls = _run_main(monkeypatch, tmp_path, view=[before, after])
    assert code == 0
    assert len([c for c in calls if c[:2] == ["pr", "view"]]) == 2
    assert not [c for c in calls if c[:2] == ["pr", "merge"]]


def test_main_dry_run_merges_nothing(monkeypatch, tmp_path):
    view = make_pr(number=42, headRefOid="cafe1234")
    code, calls = _run_main(monkeypatch, tmp_path, view=view, extra_args=["--dry-run"])
    assert code == 0
    assert not [c for c in calls if c[:2] == ["pr", "merge"]]
    assert "Would merge 1" in (tmp_path / "summary.md").read_text()


def test_main_dry_run_reports_only_the_one_merge_a_real_run_would_attempt(
    monkeypatch, tmp_path
):
    listed = [make_pr(number=41), make_pr(number=42)]
    view = make_pr(number=41, headRefOid="head41")
    code, calls = _run_main(
        monkeypatch,
        tmp_path,
        view=view,
        listed=listed,
        extra_args=["--dry-run"],
    )
    assert code == 0
    assert len([c for c in calls if c[:2] == ["pr", "view"]]) == 2
    summary = (tmp_path / "summary.md").read_text()
    assert "Would merge 1" in summary
    assert "#41" in summary
    assert "#42" not in summary


def test_main_promotes_reverifies_and_merges_an_approved_draft(monkeypatch, tmp_path):
    listed = [
        make_pr(
            number=42,
            isDraft=True,
            mergeable="MERGEABLE",
            mergeStateStatus="DRAFT",
        )
    ]
    before = make_pr(
        number=42,
        isDraft=True,
        mergeStateStatus="DRAFT",
        headRefOid="cafe1234",
    )
    after = make_pr(number=42, isDraft=False, headRefOid="cafe1234")
    code, calls = _run_main(monkeypatch, tmp_path, view=[before, after], listed=listed)
    assert code == 0
    ready_calls = [c for c in calls if c[:2] == ["pr", "ready"]]
    assert len(ready_calls) == 1
    assert "--undo" not in ready_calls[0]
    assert len([c for c in calls if c[:2] == ["pr", "view"]]) == 2
    assert len([c for c in calls if c[:2] == ["pr", "merge"]]) == 1


def test_main_retries_a_stale_draft_read_after_marking_ready(monkeypatch, tmp_path):
    listed = [
        make_pr(
            number=42,
            isDraft=True,
            mergeable="MERGEABLE",
            mergeStateStatus="DRAFT",
        )
    ]
    before = make_pr(
        number=42,
        isDraft=True,
        mergeStateStatus="DRAFT",
        headRefOid="cafe1234",
    )
    lagging = make_pr(
        number=42,
        isDraft=True,
        mergeStateStatus="DRAFT",
        headRefOid="cafe1234",
    )
    after = make_pr(number=42, isDraft=False, headRefOid="cafe1234")
    code, calls = _run_main(
        monkeypatch,
        tmp_path,
        view=[before, lagging, after],
        listed=listed,
    )
    assert code == 0
    ready_calls = [c for c in calls if c[:2] == ["pr", "ready"]]
    assert len(ready_calls) == 1
    assert len([c for c in calls if c[:2] == ["pr", "view"]]) == 3
    assert len([c for c in calls if c[:2] == ["pr", "merge"]]) == 1


def test_draft_dry_run_reports_transition_without_mutating(monkeypatch, tmp_path):
    draft = make_pr(
        number=42,
        isDraft=True,
        mergeStateStatus="DRAFT",
        headRefOid="cafe1234",
    )
    code, calls = _run_main(
        monkeypatch,
        tmp_path,
        view=draft,
        listed=[draft],
        extra_args=["--dry-run"],
    )
    assert code == 0
    assert not [c for c in calls if c[:2] == ["pr", "ready"]]
    assert not [c for c in calls if c[:2] == ["pr", "merge"]]
    assert "mark ready and merge" in (tmp_path / "summary.md").read_text().lower()


def test_failed_post_ready_guard_restores_draft(monkeypatch, tmp_path):
    listed = [
        make_pr(
            number=42,
            isDraft=True,
            mergeable="MERGEABLE",
            mergeStateStatus="DRAFT",
        )
    ]
    before = make_pr(
        number=42,
        isDraft=True,
        mergeStateStatus="DRAFT",
        headRefOid="cafe1234",
    )
    after = make_pr(
        number=42,
        isDraft=False,
        assignees=[{"login": "cmungall"}],
        headRefOid="cafe1234",
    )
    code, calls = _run_main(monkeypatch, tmp_path, view=[before, after], listed=listed)
    assert code == 0
    assert not [c for c in calls if c[:2] == ["pr", "merge"]]
    ready_calls = [c for c in calls if c[:2] == ["pr", "ready"]]
    assert len(ready_calls) == 2
    assert "--undo" in ready_calls[-1]


def _run_draft_controller(
    monkeypatch,
    tmp_path,
    *,
    final=None,
    ready_error=None,
    merge_error=None,
):
    """Exercise draft transitions with policy reads stubbed above the gh layer."""
    initial = make_pr(
        number=42,
        isDraft=True,
        mergeStateStatus="DRAFT",
        headRefOid="cafe1234",
    )
    final = final or make_pr(number=42, isDraft=False, headRefOid="cafe1234")
    views = iter([initial, final])
    calls = []

    monkeypatch.setattr(auto_merge, "list_open_prs", lambda *_: [initial])
    monkeypatch.setattr(auto_merge, "view_pr", lambda *_, **__: next(views))

    def mark_ready(*_):
        calls.append("ready")
        if ready_error:
            raise ready_error

    def mark_draft(*_):
        calls.append("draft")

    def merge(*_):
        calls.append("merge")
        if merge_error:
            raise merge_error

    monkeypatch.setattr(auto_merge, "mark_pr_ready", mark_ready)
    monkeypatch.setattr(auto_merge, "mark_pr_draft", mark_draft)
    monkeypatch.setattr(auto_merge, "merge_pr", merge)
    monkeypatch.setenv("GH_MERGE_TOKEN", "writer-token")
    code = auto_merge.main(
        ["--repo", "o/r", "--summary-file", str(tmp_path / "draft-summary.md")]
    )
    return code, calls


def test_failed_ready_transition_does_not_arm_rollback(monkeypatch, tmp_path):
    error = subprocess.CalledProcessError(1, "gh", stderr="transition rejected")
    code, calls = _run_draft_controller(monkeypatch, tmp_path, ready_error=error)
    assert code == 1
    assert calls == ["ready"]


@pytest.mark.parametrize(
    "message,expect_rollback",
    [
        ("HTTP 403: Resource not accessible by integration", True),
        ("Head branch was modified", True),
        ("No commits between main and branch", True),
        ("Pull request #42 is already merged", False),
        ("Pull request is closed", False),
    ],
)
def test_post_ready_merge_failures_restore_draft_unless_pr_is_gone(
    monkeypatch, tmp_path, message, expect_rollback
):
    error = subprocess.CalledProcessError(1, "gh", stderr=message)
    code, calls = _run_draft_controller(monkeypatch, tmp_path, merge_error=error)
    assert ("draft" in calls) is expect_rollback
    assert code == (1 if message.startswith("HTTP 403") else 0)


def test_ready_transition_still_draft_after_retry_budget_is_rolled_back(
    monkeypatch, tmp_path
):
    still_draft = make_pr(
        number=42,
        isDraft=True,
        mergeStateStatus="DRAFT",
        headRefOid="cafe1234",
    )
    code, calls = _run_draft_controller(monkeypatch, tmp_path, final=still_draft)
    assert code == 0
    assert calls == ["ready", "draft"]


def test_behind_draft_is_promoted_and_merged(monkeypatch, tmp_path):
    behind = make_pr(
        number=42,
        isDraft=True,
        mergeStateStatus="DRAFT",
        headRefOid="cafe1234",
        baseRefOid="base123",
    )
    code, calls = _run_main(
        monkeypatch,
        tmp_path,
        view=[behind, make_pr(number=42, headRefOid="cafe1234")],
        listed=[behind],
    )
    assert code == 0
    assert [call for call in calls if call[:2] == ["pr", "ready"]]
    assert [call for call in calls if call[:2] == ["pr", "merge"]]


def test_main_list_call_does_not_request_merge_state_status(monkeypatch, tmp_path):
    """Requesting mergeStateStatus for every open PR intermittently 502s and
    the list stage never reads it."""
    _, calls = _run_main(monkeypatch, tmp_path, view=make_pr(number=42))
    list_call = next(c for c in calls if c[:2] == ["pr", "list"])
    fields = list_call[list_call.index("--json") + 1]
    assert "mergeStateStatus" not in fields
    assert "mergeStateStatus" in auto_merge.VIEW_FIELDS


def test_main_reports_a_race_as_skipped_not_failed(monkeypatch, tmp_path):
    """A benign race must not turn the six-times-daily workflow red."""

    def fake_gh(args, *, token=None):
        if args[:2] == ["pr", "list"]:
            return json.dumps([make_pr(number=42)])
        if args[:2] == ["pr", "view"]:
            return json.dumps(make_pr(number=42, headRefOid="cafe1234"))
        if args[:2] == ["pr", "merge"]:
            raise subprocess.CalledProcessError(1, "gh", stderr=GH_REFUSAL_STDERR)
        return ""

    monkeypatch.setattr(auto_merge, "_gh", fake_gh)
    monkeypatch.setenv("GH_MERGE_TOKEN", "writer-token")
    code = auto_merge.main(["--repo", "o/r", "--summary-file", str(tmp_path / "s.md")])
    summary = (tmp_path / "s.md").read_text()
    assert code == 0
    assert "Failed to merge" not in summary
    # ...and the skip line states the diagnosis rather than suggesting --admin.
    assert "is not mergeable" in summary
    assert "--admin" not in summary


def test_main_exits_nonzero_on_a_genuine_merge_error(monkeypatch, tmp_path):
    def fake_gh(args, *, token=None):
        if args[:2] == ["pr", "list"]:
            return json.dumps([make_pr(number=42)])
        if args[:2] == ["pr", "view"]:
            return json.dumps(make_pr(number=42, headRefOid="cafe1234"))
        if args[:2] == ["pr", "merge"]:
            raise subprocess.CalledProcessError(
                1, "gh", stderr="HTTP 403: Resource not accessible by integration"
            )
        return ""

    monkeypatch.setattr(auto_merge, "_gh", fake_gh)
    monkeypatch.setenv("GH_MERGE_TOKEN", "writer-token")
    code = auto_merge.main(["--repo", "o/r", "--summary-file", str(tmp_path / "s.md")])
    assert code == 1
    assert "Failed to merge 1" in (tmp_path / "s.md").read_text()


def test_execute_merges_at_most_one(monkeypatch, tmp_path):
    listed = [make_pr(number=41), make_pr(number=42)]
    calls = []

    def fake_gh(args, *, token=None):
        calls.append(args)
        if args[:2] == ["pr", "list"]:
            return json.dumps(listed)
        if args[:2] == ["pr", "view"]:
            number = int(args[2])
            return json.dumps(make_pr(number=number, headRefOid=f"head{number}"))
        return ""

    monkeypatch.setattr(auto_merge, "_gh", fake_gh)
    monkeypatch.setenv("GH_MERGE_TOKEN", "writer-token")
    code = auto_merge.main(["--repo", "o/r", "--summary-file", str(tmp_path / "s.md")])
    assert code == 0
    merges = [c for c in calls if c[:2] == ["pr", "merge"]]
    assert len(merges) == 1
    assert len([c for c in calls if c[:2] == ["pr", "view"]]) == 2


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


def test_dry_run_summary_never_claims_a_merge_happened():
    """A dry run writes to $GITHUB_STEP_SUMMARY too; it must not log
    'Merged 1' into a permanent audit trail when nothing was merged."""
    report = auto_merge.render_summary(
        merged=[{"number": 1, "title": "feat: A"}],
        skipped=[],
        failed=[],
        dry_run=True,
    )
    assert "Would merge 1" in report
    assert "dry run" in report
    assert "**Merged" not in report


# --- fetching -------------------------------------------------------------


def _stub_views(monkeypatch, payloads):
    """Make view_pr return each payload in turn, and count the calls."""
    calls = []

    def fake_gh(args):
        calls.append(args)
        return json.dumps(payloads[min(len(calls) - 1, len(payloads) - 1)])

    monkeypatch.setattr(auto_merge, "_gh", fake_gh)
    monkeypatch.setattr(auto_merge.time, "sleep", lambda _: None)
    return calls


def test_view_pr_retries_until_mergeability_resolves(monkeypatch):
    calls = _stub_views(
        monkeypatch,
        [
            {"mergeable": "UNKNOWN", "mergeStateStatus": "UNKNOWN"},
            {"mergeable": "MERGEABLE", "mergeStateStatus": "CLEAN"},
        ],
    )
    pr = auto_merge.view_pr("o/r", 7)
    assert pr["mergeable"] == "MERGEABLE"
    assert len(calls) == 2


def test_view_pr_also_waits_on_merge_state_status(monkeypatch):
    """Both fields come from the same background computation; waiting only on
    `mergeable` skips PRs as 'merge state is unknown' for being asked early."""
    calls = _stub_views(
        monkeypatch,
        [
            {"mergeable": "MERGEABLE", "mergeStateStatus": "UNKNOWN"},
            {"mergeable": "MERGEABLE", "mergeStateStatus": "CLEAN"},
        ],
    )
    pr = auto_merge.view_pr("o/r", 7)
    assert pr["mergeStateStatus"] == "CLEAN"
    assert len(calls) == 2


def test_view_pr_can_wait_for_a_ready_transition_to_be_observable(monkeypatch):
    calls = _stub_views(
        monkeypatch,
        [
            {"isDraft": True, "mergeable": "MERGEABLE", "mergeStateStatus": "DRAFT"},
            {"isDraft": False, "mergeable": "MERGEABLE", "mergeStateStatus": "CLEAN"},
        ],
    )
    pr = auto_merge.view_pr("o/r", 7, expected_draft=False)
    assert not pr["isDraft"]
    assert len(calls) == 2


def test_view_pr_gives_up_after_the_attempt_budget(monkeypatch):
    calls = _stub_views(monkeypatch, [{"mergeable": "UNKNOWN"}])
    pr = auto_merge.view_pr("o/r", 7, attempts=3)
    assert len(calls) == 3
    # Unresolved is returned, not merged — evaluate() rejects it.
    assert not decide(make_pr(**pr)).eligible


# --- merge invocation -----------------------------------------------------


def test_merge_pins_the_verified_head_commit(monkeypatch):
    """A push landing between verification and merge must abort the merge, not
    silently merge an unreviewed commit."""
    calls = []
    monkeypatch.setattr(
        auto_merge, "_gh", lambda args, token=None: calls.append((args, token)) or ""
    )
    auto_merge.merge_pr("o/r", 7, 3, "deadbeef", "writer-token", False)
    merge_cmd, token = calls[0]
    assert "--squash" in merge_cmd
    assert merge_cmd[merge_cmd.index("--match-head-commit") + 1] == "deadbeef"
    assert token == "writer-token"


def test_merge_drops_the_strategy_flag_when_a_queue_is_in_force(monkeypatch):
    """gh only warns on a strategy flag here, but that warning would become
    the reported cause of every real failure, so drop it. The head pin must
    survive: it becomes the enqueue mutation's expectedHeadOid."""
    calls = []
    monkeypatch.setattr(
        auto_merge, "_gh", lambda args, token=None: calls.append((args, token)) or ""
    )
    auto_merge.merge_pr("o/r", 7, 3, "deadbeef", "writer-token", True)
    merge_cmd, _token = calls[0]
    assert "--squash" not in merge_cmd
    assert merge_cmd[merge_cmd.index("--match-head-commit") + 1] == "deadbeef"
    body = " ".join(calls[1][0])
    assert "merge queue" in body
    assert "Squash-merged" not in body
    assert "No further action needed" not in body


def test_queue_state_reports_active_queue_and_its_members(monkeypatch):
    payload = (
        '{"data":{"repository":{"mergeQueue":{"id":"MQ_x","entries":'
        '{"nodes":[{"pullRequest":{"number":11}},{"pullRequest":{"number":22}}]}}}}}'
    )
    monkeypatch.setattr(auto_merge, "_gh", lambda args, token=None: payload)
    state = auto_merge.read_queue_state("o/r", "main")
    assert state.active is True
    assert state.queued_pr_numbers == frozenset({11, 22})


def test_queue_state_is_inactive_when_the_queue_is_paused(monkeypatch):
    """Disabling the ruleset nulls the node; that is the break-glass signal."""
    monkeypatch.setattr(
        auto_merge, "_gh",
        lambda args, token=None: '{"data":{"repository":{"mergeQueue":null}}}',
    )
    state = auto_merge.read_queue_state("o/r", "main")
    assert state.active is False
    assert state.queued_pr_numbers == frozenset()


def test_queue_state_failure_keeps_pre_queue_behavior(monkeypatch):
    def boom(args, token=None):
        raise subprocess.CalledProcessError(1, ["gh"], stderr="nope")

    monkeypatch.setattr(auto_merge, "_gh", boom)
    assert auto_merge.read_queue_state("o/r", "main").active is False


def test_gh_error_skips_the_queue_warning_line():
    """gh prints its queue warning first; it is not the cause of the failure."""
    exc = subprocess.CalledProcessError(
        1, ["gh"],
        stderr=(
            "! The merge strategy for main is set by the merge queue\n"
            "X Pull request #7 is not mergeable: the base branch was modified\n"
        ),
    )
    assert "base branch was modified" in auto_merge._gh_error(exc)
    assert "merge strategy" not in auto_merge._gh_error(exc)


def test_summary_does_not_claim_a_queued_pr_was_merged():
    body = auto_merge.render_summary(
        [{"number": 7, "title": "t", "queued": True}], [], [], dry_run=False
    )
    assert "Added to the merge queue" in body
    assert "**Merged 1:**" not in body


def test_merge_fails_closed_when_the_sha_is_unavailable(monkeypatch):
    calls = []
    monkeypatch.setattr(
        auto_merge, "_gh", lambda args, token=None: calls.append((args, token)) or ""
    )
    with pytest.raises(ValueError, match="without a verified head"):
        auto_merge.merge_pr("o/r", 7, 3, None, "writer-token")
    assert calls == []


def test_merge_requires_a_dedicated_write_token(monkeypatch):
    calls = []
    monkeypatch.setattr(
        auto_merge, "_gh", lambda args, token=None: calls.append((args, token)) or ""
    )
    with pytest.raises(ValueError, match="dedicated write token"):
        auto_merge.merge_pr("o/r", 7, 3, "abc123", "")
    assert calls == []


def test_comment_failure_does_not_mask_a_successful_merge(monkeypatch):
    """The merge already succeeded; a failed courtesy comment must not be
    reported as a failed merge (which would also invite a retry)."""

    def fake_gh(args, *, token=None):
        if args[1] == "comment":
            raise subprocess.CalledProcessError(1, "gh", stderr="rate limited")
        return ""

    monkeypatch.setattr(auto_merge, "_gh", fake_gh)
    auto_merge.merge_pr("o/r", 7, 3, "abc123", "writer-token")  # must not raise


def test_merge_failure_still_propagates(monkeypatch):
    def fake_gh(args, *, token=None):
        raise subprocess.CalledProcessError(1, "gh", stderr="not mergeable")

    monkeypatch.setattr(auto_merge, "_gh", fake_gh)
    with pytest.raises(subprocess.CalledProcessError):
        auto_merge.merge_pr("o/r", 7, 3, "abc123", "writer-token")


def test_gh_error_condenses_stderr():
    # First non-empty line, not last: gh puts the diagnosis first and appends
    # `--auto`/`--admin` hints (see GH_REFUSAL_STDERR).
    exc = subprocess.CalledProcessError(1, "gh", stderr="line one\nfinal line\n")
    assert auto_merge._gh_error(exc) == "line one"
    assert auto_merge._gh_error(subprocess.CalledProcessError(1, "gh", stderr="")) == (
        "gh exited 1"
    )


def test_gh_error_still_reports_a_warning_when_it_is_all_there_is():
    exc = subprocess.CalledProcessError(1, "gh", stderr="! something happened\n")
    assert auto_merge._gh_error(exc) == "something happened"


def test_a_queued_pr_is_skipped_and_the_sweep_reaches_the_next_one(
    monkeypatch, tmp_path
):
    """The queued PR here is stubbed CLEAN/MERGEABLE, which is the state
    measured on #10576 at 2026-09-02T23:37Z while its entry was UNMERGEABLE:
    it passes every predicate, and re-enqueueing SUCCEEDS (gh exits 0 on an
    already-queued PR), so without this skip the sweep spends its one action
    re-announcing a PR that is already queued.

    An AWAITING_CHECKS entry reports UNKNOWN instead and is already rejected
    by `evaluate` with a `continue`, so for that state the skip buys a cheaper
    path and an accurate reason rather than different behavior."""
    queued, next_up = 11, 22
    listed = [
        make_pr(number=queued, mergeable="MERGEABLE"),
        make_pr(number=next_up, mergeable="MERGEABLE"),
    ]
    acted_on = []
    monkeypatch.setattr(
        auto_merge, "merge_pr",
        lambda repo, number, days, head, token, q=False: acted_on.append(number)
        or bool(q),
    )
    queue_payload = json.dumps(
        {"data": {"repository": {"mergeQueue": {
            "id": "MQ_x",
            "entries": {"nodes": [{"pullRequest": {"number": queued}}]},
        }}}}
    )
    code, _calls = _run_main(
        monkeypatch, tmp_path,
        view=[make_pr(number=queued, mergeable="MERGEABLE"),
              make_pr(number=next_up, mergeable="MERGEABLE")],
        listed=listed,
        queue_payload=queue_payload,
    )
    assert code == 0
    assert acted_on == [next_up], (
        "the queued PR must be skipped and the next candidate acted on"
    )
