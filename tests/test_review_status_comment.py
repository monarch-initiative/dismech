"""Tests for the `/review` status comment (dismech#18311).

A `/review` comment used to get no sign it had been accepted until the review
job reached a runner. `scripts/review_status_comment.sh` posts and updates one
status comment per run; `claude-code-review.yml` calls it from a small
`acknowledge` job and from the review job.

The script is run against a fake `gh` that applies the script's own `--jq`
filter to a canned comment list with the real `jq`, so the comment-matching
logic is exercised rather than restated.
"""

import json
import os
import shutil
import subprocess
from pathlib import Path

import pytest

from dismech.yaml_io import safe_load_path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "review_status_comment.sh"
WORKFLOW = ROOT / ".github" / "workflows" / "claude-code-review.yml"

pytestmark = pytest.mark.skipif(
    shutil.which("jq") is None or shutil.which("bash") is None,
    reason="needs bash and jq",
)

FAKE_GH = r"""#!/usr/bin/env bash
# Records every call; serves $FAKE_COMMENTS for the list call through real jq.
printf '%s\036' "$*" >> "$FAKE_LOG"
if [[ " $* " == *" --paginate "* ]]; then
  [[ -n "${FAKE_LIST_FAILS:-}" ]] && exit 1
  filter=""
  while [[ $# -gt 0 ]]; do
    if [[ "$1" == "--jq" ]]; then filter="$2"; shift; fi
    shift
  done
  jq -r "$filter" "$FAKE_COMMENTS"
fi
exit 0
"""


def _marker(run_id: int) -> str:
    return f"<!-- claude-review-status run={run_id} -->"


def run_script(tmp_path, state, comments, *, run_id=500, extra_env=None):
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir(exist_ok=True)
    gh = bin_dir / "gh"
    gh.write_text(FAKE_GH)
    gh.chmod(0o755)
    comments_file = tmp_path / "comments.json"
    comments_file.write_text(json.dumps(comments))
    log = tmp_path / "gh.log"
    log.write_text("")
    env = {
        "PATH": f"{bin_dir}{os.pathsep}{os.environ['PATH']}",
        "FAKE_LOG": str(log),
        "FAKE_COMMENTS": str(comments_file),
        "GH_TOKEN": "x",
        "REPO": "owner/repo",
        "PR_NUMBER": "42",
        "RUN_ID": str(run_id),
        "REQUESTER": "someone",
        **(extra_env or {}),
    }
    result = subprocess.run(
        ["bash", str(SCRIPT), state],
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )
    calls = [call for call in log.read_text().split("\x1e") if call]
    return result, calls


def writes(calls):
    return [c for c in calls if " -X POST " in f" {c} " or " -X PATCH " in f" {c} "]


def test_queued_posts_a_new_marked_comment(tmp_path):
    result, calls = run_script(tmp_path, "queued", [])
    assert result.returncode == 0
    (call,) = writes(calls)
    assert "-X POST repos/owner/repo/issues/42/comments" in call
    assert _marker(500) in call
    assert "Review queued" in call
    assert "actions/runs/500" in call
    # States the /review limitation found on #18300.
    assert "cannot clear a failing" in call


def test_queued_never_overwrites_this_runs_comment(tmp_path):
    """The review job can reach a runner before the acknowledge job does."""
    comments = [{"id": 7, "body": f"{_marker(500)}\n⏳ **Review running.**"}]
    result, calls = run_script(tmp_path, "queued", comments)
    assert result.returncode == 0
    assert writes(calls) == []


def test_later_states_edit_this_runs_comment(tmp_path):
    comments = [{"id": 7, "body": f"{_marker(500)}\n🕐 **Review queued.**"}]
    for state, phrase in [
        ("started", "Review running"),
        ("success", "Review finished"),
        ("failure", "Review failed"),
        ("cancelled", "Review cancelled"),
        ("skipped", "Review skipped"),
    ]:
        _, calls = run_script(tmp_path, state, comments)
        (call,) = writes(calls)
        assert "-X PATCH repos/owner/repo/issues/comments/7" in call
        assert phrase in call


def test_a_new_request_supersedes_older_unfinished_ones_only(tmp_path):
    comments = [
        {"id": 1, "body": f"{_marker(100)}\n🕐 **Review queued.**"},
        {"id": 2, "body": f"{_marker(200)}\n⏳ **Review running.**"},
        {"id": 3, "body": f"{_marker(300)}\n✅ **Review finished.**"},
        {"id": 4, "body": f"{_marker(900)}\n🕐 **Review queued.**"},
        {"id": 5, "body": "an ordinary comment"},
    ]
    _, calls = run_script(tmp_path, "queued", comments)
    patched = sorted(
        c.split("issues/comments/")[1].split()[0] for c in writes(calls) if "PATCH" in c
    )
    # 1 and 2 are older and unfinished; 3 is finished; 4 is a newer run.
    assert patched == ["1", "2"]
    assert any("Review superseded" in c for c in writes(calls))
    assert sum("-X POST" in c for c in writes(calls)) == 1


def test_refusal_names_the_association(tmp_path):
    _, calls = run_script(
        tmp_path, "refused", [], extra_env={"AUTHOR_ASSOCIATION": "CONTRIBUTOR"}
    )
    (call,) = writes(calls)
    assert "Review not started" in call
    assert "CONTRIBUTOR" in call


def test_failures_never_fail_the_calling_job(tmp_path):
    result, calls = run_script(
        tmp_path, "started", [], extra_env={"FAKE_LIST_FAILS": "1"}
    )
    assert result.returncode == 0
    assert writes(calls) == []
    result, _ = run_script(tmp_path, "no-such-state", [])
    assert result.returncode == 0


# --- workflow wiring -------------------------------------------------------


@pytest.fixture(scope="module")
def workflow():
    return safe_load_path(WORKFLOW)


def test_ordinary_comments_cannot_cancel_a_review(workflow):
    group = workflow["concurrency"]["group"]
    assert "github.event.comment.body != '/review'" in group
    assert "github.run_id" in group
    assert workflow["concurrency"]["cancel-in-progress"] is True


def test_acknowledge_job_runs_only_for_review_comments(workflow):
    job = workflow["jobs"]["acknowledge"]
    assert "github.event.comment.body == '/review'" in job["if"]
    assert "github.event.issue.pull_request != null" in job["if"]
    step = next(
        s for s in job["steps"] if s.get("name", "").startswith("Post the review")
    )
    assert step["continue-on-error"] is True
    assert "review_status_comment.sh queued" in step["run"]
    assert "review_status_comment.sh refused" in step["run"]


def test_acknowledge_uses_the_same_author_rule_as_the_review(workflow):
    trusted = '["OWNER","MEMBER","COLLABORATOR"]'
    ack = workflow["jobs"]["acknowledge"]["steps"][-1]["env"]["ACCEPTED"]
    assert trusted in ack
    assert trusted in workflow["jobs"]["claude-review"]["if"]


def test_review_job_marks_start_and_outcome(workflow):
    steps = workflow["jobs"]["claude-review"]["steps"]
    names = [s.get("name", "") for s in steps]
    started = names.index("Mark the /review status comment as started")
    pr_checkout = names.index("Checkout PR branch (for manual review triggers)")
    # The script is copied out before the PR branch replaces the checkout.
    assert started < pr_checkout
    assert "RUNNER_TEMP" in steps[started]["run"]

    final = steps[-1]
    assert final["name"] == "Record the /review outcome in the status comment"
    assert final["if"].startswith("always()")
    assert final["continue-on-error"] is True
    assert final["env"]["JOB_STATUS"] == "${{ job.status }}"
    for s in (steps[started], final):
        assert "issue_comment" in s["if"]
