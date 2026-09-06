"""Exercise retry writes, backoff, supersession and workflow isolation."""

import importlib.util
import subprocess
from datetime import UTC, datetime, timedelta
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "retry_reviews", ROOT / "scripts/retry_failed_reviews.py"
)
retry = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(retry)
NOW = datetime(2026, 9, 6, 12, tzinfo=UTC)


def run(**overrides):
    row = {
        "id": 20,
        "event": "pull_request",
        "status": "completed",
        "conclusion": "failure",
        "head_sha": "abc",
        "run_attempt": 1,
        "pull_requests": [{"number": 7}],
        "created_at": (NOW - timedelta(hours=5)).isoformat(),
        "updated_at": (NOW - timedelta(hours=2)).isoformat(),
    }
    return row | overrides


def pr(**overrides):
    # These are deliberately the opposite of merge eligibility.
    return {
        "state": "open",
        "draft": True,
        "user": {"login": "human"},
        "assignees": [{"login": "human"}],
        "head": {"sha": "abc", "ref": "feature"},
    } | overrides


def reason(row=None, pull=None, peers=(), reviews=()):
    return retry.skip_reason(row or run(), pull or pr(), peers, reviews, NOW, 1)


def test_human_owned_assigned_draft_can_be_retried():
    assert reason() is None


@pytest.mark.parametrize(
    "attempt,hours,eligible",
    [
        (1, 0.5, False),
        (1, 1, True),
        (2, 5, False),
        (2, 6, True),
        (3, 23, False),
        (3, 24, True),
        (8, 24, True),
    ],
)
def test_backoff_uses_latest_attempt_completion(attempt, hours, eligible):
    row = run(
        run_attempt=attempt, updated_at=(NOW - timedelta(hours=hours)).isoformat()
    )
    assert (reason(row) is None) == eligible


@pytest.mark.parametrize(
    "changes",
    [
        {"status": "queued", "conclusion": None},
        {"status": "in_progress", "conclusion": None},
        {"conclusion": "success"},
        {"conclusion": "cancelled"},
        {"conclusion": "skipped"},
        {"run_attempt": 50},
        {"created_at": (NOW - timedelta(days=30)).isoformat()},
        {"head_sha": "old"},
    ],
)
def test_ineligible_attempts_are_not_retried(changes):
    assert reason(run(**changes))


def test_closed_pr_and_superseding_reviews():
    assert reason(pull=pr(state="closed"))
    assert reason(peers=[run(id=21, status="in_progress", conclusion=None)])
    assert reason(peers=[run(id=21, created_at=(NOW - timedelta(hours=1)).isoformat())])
    assert reason(peers=[run(id=21, conclusion="success", updated_at=NOW.isoformat())])
    assert reason(peers=[run(id=21, conclusion="skipped")]) is None


@pytest.mark.parametrize("state", ["APPROVED", "CHANGES_REQUESTED"])
def test_current_bot_verdict_stops_retry_but_old_verdict_does_not(state):
    review = {
        "id": 1,
        "user": {"login": "ai4c-reviewer[bot]"},
        "state": state,
        "commit_id": "abc",
    }
    assert reason(reviews=[review])
    assert reason(reviews=[review | {"commit_id": "old"}]) is None
    assert reason(reviews=[review | {"state": "DISMISSED"}]) is None


def test_manual_run_is_rerunnable_despite_main_sha():
    assert reason(run(event="workflow_dispatch", head_sha="main-sha")) is None


def harness(monkeypatch, rows=None, current=None, reviews=None, fresh=None):
    rows = rows or [run()]
    writes = []
    monkeypatch.setattr(retry, "workflow_runs", lambda *args: list(rows))
    monkeypatch.setattr(retry, "pages", lambda *args: reviews or [])

    def read(path):
        if "/actions/runs/" in path:
            return current or next(r for r in rows if path.endswith(str(r["id"])))
        if "/pulls/" in path:
            return pr()
        if "/workflows/" in path:
            return {"workflow_runs": fresh or rows}
        raise AssertionError(path)

    monkeypatch.setattr(retry, "api", read)
    monkeypatch.setattr(
        retry, "gh", lambda *args, **kwargs: writes.append((args, kwargs))
    )
    return writes


def test_sweep_issues_exact_failed_job_rerun(monkeypatch):
    writes = harness(monkeypatch)
    rows, errors = retry.sweep("owner/repo", NOW)
    assert errors == 0
    assert writes == [
        (("run", "rerun", "20", "--failed", "--repo", "owner/repo"), {"write": True})
    ]
    assert "retried failed jobs" in rows[0]


@pytest.mark.parametrize(
    "kwargs", [{"dry_run": True}, {"limit": 0}, {"specific_pr": 8}]
)
def test_dry_run_zero_budget_and_specific_pr_never_write(monkeypatch, kwargs):
    writes = harness(monkeypatch)
    retry.sweep("owner/repo", NOW, **kwargs)
    assert not writes


def test_manual_retry_started_since_discovery_is_left_alone(monkeypatch):
    writes = harness(
        monkeypatch, current=run(status="queued", conclusion=None, run_attempt=2)
    )
    retry.sweep("owner/repo", NOW)
    assert not writes


def test_new_review_arriving_during_sweep_prevents_retry(monkeypatch):
    writes = harness(
        monkeypatch, fresh=[run(id=30, status="in_progress", conclusion=None)]
    )
    retry.sweep("owner/repo", NOW)
    assert not writes


def test_only_latest_failure_retried_once_per_pr(monkeypatch):
    old = run(
        id=10,
        created_at=(NOW - timedelta(days=1)).isoformat(),
        updated_at=(NOW - timedelta(hours=8)).isoformat(),
    )
    writes = harness(monkeypatch, rows=[old, run()])
    retry.sweep("owner/repo", NOW)
    assert len(writes) == 1
    assert writes[0][0][2] == "20"


def test_read_failure_does_not_retry(monkeypatch):
    writes = harness(monkeypatch)

    def fail(path):
        raise subprocess.CalledProcessError(1, ["gh"])

    monkeypatch.setattr(retry, "api", fail)
    rows, errors = retry.sweep("owner/repo", NOW)
    assert not writes and errors == 1
    assert "error" in rows[0]


def test_resolve_dispatch_and_legacy_dispatch(monkeypatch):
    assert (
        retry.run_pr(run(pull_requests=[], display_title="Review PR #42"), "o/r") == 42
    )
    monkeypatch.setattr(
        retry,
        "pages",
        lambda *args: [{"id": 99, "name": "dispatch-guard", "status": "completed"}],
    )
    monkeypatch.setattr(
        retry,
        "gh",
        lambda *args: "2026-09-06 Dispatched PR #7: head_ref='feature' author='human'",
    )
    assert retry.run_pr(run(event="workflow_dispatch", pull_requests=[]), "o/r") == 7


def test_unresolved_active_legacy_run_defers_without_duplicate_writes(monkeypatch):
    writes = harness(
        monkeypatch,
        rows=[run(), run(id=30, pull_requests=[], status="queued", conclusion=None)],
    )
    rows, _ = retry.sweep("o/r", NOW)
    assert not writes
    assert "active legacy review" in rows[-1]


def test_writer_token_only_reaches_rerun(monkeypatch):
    monkeypatch.setenv("GH_TOKEN", "reader")
    monkeypatch.setenv("GH_RETRY_TOKEN", "writer")
    environments = []

    def execute(args, **kwargs):
        environments.append(kwargs["env"])
        return subprocess.CompletedProcess(args, 0, stdout="{}")

    monkeypatch.setattr(retry.subprocess, "run", execute)
    retry.gh("api", "some/path")
    retry.gh("run", "rerun", "20", "--failed", write=True)
    assert [env["GH_TOKEN"] for env in environments] == ["reader", "writer"]
    assert all("GH_RETRY_TOKEN" not in env for env in environments)


def test_pr_event_with_empty_association_resolves_by_commit_and_branch(monkeypatch):
    monkeypatch.setattr(
        retry,
        "pages",
        lambda path: [
            {"number": 7, "head": {"ref": "feature"}},
            {"number": 8, "head": {"ref": "different"}},
        ],
    )
    assert retry.run_pr(run(pull_requests=[], head_branch="feature"), "o/r") == 7


def test_discovery_splits_above_github_search_limit(monkeypatch):
    calls = []

    def read(path):
        calls.append(path)
        if len(calls) == 1:
            return {"total_count": 1001, "workflow_runs": []}
        return {"total_count": 1, "workflow_runs": [run(id=len(calls))]}

    monkeypatch.setattr(retry, "api", read)
    found = retry.workflow_runs("o/r", NOW - timedelta(days=1), NOW, "failure")
    assert len(calls) == 3
    assert {r["id"] for r in found} == {2, 3}
    assert all("status=failure" in path for path in calls)


def test_discovery_reads_later_pages(monkeypatch):
    def read(path):
        rows = (
            [run(id=i) for i in range(100)]
            if path.endswith("&page=1")
            else [run(id=101)]
        )
        return {"total_count": 101, "workflow_runs": rows}

    monkeypatch.setattr(retry, "api", read)
    assert (
        len(retry.workflow_runs("o/r", NOW - timedelta(days=1), NOW, "failure")) == 101
    )


def test_operator_minimum_delay_can_increase_backoff():
    assert retry.delay_hours(1, 12) == 12
    assert retry.delay_hours(2, 12) == 12
    assert retry.delay_hours(3, 12) == 24


def test_newer_manual_review_prevents_write(monkeypatch):
    manual = run(
        id=30,
        event="workflow_dispatch",
        head_sha="main",
        pull_requests=[],
        display_title="Review PR #7",
        status="in_progress",
        conclusion=None,
    )
    writes = harness(monkeypatch, rows=[run(), manual])
    retry.sweep("o/r", NOW)
    assert not writes


def test_late_success_on_old_commit_does_not_hide_current_failure():
    old = run(id=15, head_sha="old", conclusion="success", updated_at=NOW.isoformat())
    assert reason(peers=[old]) is None


def test_workflow_job_is_independent_and_respects_dry_run():
    config = yaml.safe_load((ROOT / ".github/workflows/pr-shepherd.yml").read_text())
    job = config["jobs"]["retry-reviews"]
    assert "needs" not in job and "if" not in job
    assert job["concurrency"]["cancel-in-progress"] is False
    assert all("anthropics/" not in s.get("uses", "") for s in job["steps"])
    token = next(s for s in job["steps"] if s["name"] == "Generate scoped retry token")
    assert token["if"] == "${{ env.DRY_RUN != 'true' }}"
    assert token["with"]["permission-actions"] == "write"
    assert "--dry-run" in job["steps"][-1]["run"]
    review = yaml.safe_load(
        (ROOT / ".github/workflows/claude-code-review.yml").read_text()
    )
    assert review["run-name"].startswith("Review PR #${{")
