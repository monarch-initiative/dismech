"""Tests for the experiment_design backfill's idempotence boundary.

The interesting case is a re-run over a file where one experiment already
carries a value and the next one does not. A fixed lookahead window reaches
past the first experiment into the second, sees the first's
``experiment_design`` from the second's position, and skips the insert the
second one needs -- silently, because a skip is a normal outcome.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_DIR / "scripts"))

from backfill_experiment_design import experiment_block, patch_file

#: Two experiments in one discussion, in the order that exposes the bug: the
#: one still needing a value comes FIRST, and the one that already has a value
#: follows it well inside a 60-line forward window. A fixed window looks ahead
#: from the first experiment, sees the second's value, and skips the insert.
TWO_EXPERIMENTS = """\
name: Test Disease
discussions:
- discussion_id: d1
  kind: KNOWLEDGE_GAP
  proposed_experiments:
  - experiment_id: needs_one
    name: The one that still needs a value
    description: >-
      This must receive its own line even though the next experiment already
      carries one a few lines further down the file.
    decision_criterion: Something.
  - experiment_id: already_done
    experiment_design: TARGETED_PERTURBATION
    name: The one that already carries a value
    description: >-
      Padding that sits inside a fixed lookahead window of the first.
"""


def test_an_earlier_experiment_still_gets_its_value_on_a_rerun(tmp_path):
    """The first experiment is inserted even though the next one has a value."""
    path = tmp_path / "Test_Disease.yaml"
    path.write_text(TWO_EXPERIMENTS)

    inserted, already = patch_file(
        path,
        {"already_done": "TARGETED_PERTURBATION", "needs_one": "HUMAN_OBSERVATIONAL"},
    )

    assert inserted == 1, "the first experiment should have been given a value"
    assert already == ["already_done"], "only the second should count as already done"

    text = path.read_text()
    assert "experiment_design: HUMAN_OBSERVATIONAL" in text
    # And exactly one value per experiment, not two on the first.
    assert text.count("experiment_design:") == 2


def test_patching_twice_is_a_no_op(tmp_path):
    """Running the patch again inserts nothing and rewrites nothing."""
    path = tmp_path / "Test_Disease.yaml"
    path.write_text(TWO_EXPERIMENTS)
    assignments = {
        "already_done": "TARGETED_PERTURBATION",
        "needs_one": "HUMAN_OBSERVATIONAL",
    }

    patch_file(path, assignments)
    after_first = path.read_text()
    inserted, already = patch_file(path, assignments)

    assert inserted == 0
    assert sorted(already) == ["already_done", "needs_one"]
    assert path.read_text() == after_first


def test_the_block_stops_at_the_next_experiment():
    """The block never includes a line belonging to the following experiment."""
    lines = TWO_EXPERIMENTS.splitlines(keepends=True)
    start = next(
        i for i, line in enumerate(lines) if "experiment_id: needs_one" in line
    )
    block = experiment_block(lines, start, key_indent=4)

    assert any("decision_criterion" in line for line in block), "own block included"
    assert not any("already_done" in line for line in block)
    assert not any("experiment_design:" in line for line in block), (
        "the next experiment's value must be out of scope"
    )
