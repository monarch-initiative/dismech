"""Concurrency guards for the required ``Build and test`` workflow (#11941).

Without a ``concurrency`` block, a push to a pull request did not cancel the
run it superseded, so obsolete runs kept their runners and the run on the
current head queued behind them for over an hour.

The block has to cancel only pull-request runs:

- a ``merge_group`` run must never be cancelled, or the PR is ejected from the
  merge queue (#10168, #2034);
- a ``push`` build on ``main`` must never be dropped, because post-merge
  breakage is found there.

``cancel-in-progress: false`` alone does not guarantee the second point. GitHub
keeps at most one *pending* run per concurrency group and cancels the older
pending one regardless of that setting, so ``push`` runs sharing one group would
lose builds when merges land close together. Non-PR runs therefore get a
group of their own, keyed on ``github.run_id``.
"""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / ".github" / "workflows" / "main.yaml"


def concurrency() -> dict:
    return yaml.safe_load(MAIN.read_text(encoding="utf-8"))["concurrency"]


def test_main_workflow_declares_workflow_level_concurrency():
    block = concurrency()
    assert set(block) == {"group", "cancel-in-progress"}


def test_only_pull_request_runs_cancel_in_progress():
    assert (
        concurrency()["cancel-in-progress"]
        == "${{ github.event_name == 'pull_request' }}"
    )


def test_pull_request_runs_share_a_group_per_pr():
    group = concurrency()["group"]
    assert "github.event.pull_request.number" in group


def test_non_pr_runs_are_alone_in_their_group():
    """push and merge_group fall through to run_id, which is unique per run.

    Keying them on ``github.ref`` instead would put every push to main in one
    group, where GitHub cancels an older pending run whatever
    cancel-in-progress says.
    """
    group = concurrency()["group"]
    assert "|| github.run_id" in group
    assert "github.ref" not in group
    assert "github.sha" not in group
