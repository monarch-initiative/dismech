"""Tests for the ``KNOWLEDGE_GAP`` discussion completeness audit.

The load-bearing rule here is ``BARE_EXPERIMENT_TARGET``: a
``proposed_experiments[].{perturbations,readouts}[].target`` written as a bare
node name rather than ``<kind>#<name>``. No other check in the repo sees it --
``check_entity_refs`` skips a ``target`` with no ``#`` because the slot
legitimately carries bare names in its pathograph homes, and
``check_causal_targets`` excludes experiment readouts outright
(``test_experiment_readout_targets_are_not_checked_here``). Since that state
gates ``qc`` and CI, it needs a regression test of its own.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
SCRIPT_PATH = ROOT / "scripts" / "knowledge_gap_discussion_audit.py"
SPEC = importlib.util.spec_from_file_location(
    "knowledge_gap_discussion_audit", SCRIPT_PATH
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


def _write(kb_dir: Path, slug: str, discussions: str) -> None:
    kb_dir.mkdir(parents=True, exist_ok=True)
    (kb_dir / f"{slug}.yaml").write_text(
        f"name: {slug.replace('_', ' ')}\ndiscussions:\n{discussions}",
        encoding="utf-8",
    )


COMPLETE = """- discussion_id: complete_gap
  kind: KNOWLEDGE_GAP
  status: OPEN
  prompt: Does the proposed mechanism hold in human tissue?
  attaches_to:
  - pathophysiology#Some Node
  proposed_experiments:
  - experiment_id: exp_complete
    name: Isogenic perturbation
    decision_criterion: A twofold change settles it.
    readouts:
    - name: Marker level
      target: pathophysiology#Some Node
"""

UNANCHORED = """- discussion_id: unanchored_gap
  kind: KNOWLEDGE_GAP
  status: OPEN
  prompt: What is the natural history of this disease?
"""

NO_STATUS = """- discussion_id: no_status_gap
  kind: KNOWLEDGE_GAP
  prompt: Which cell type initiates the lesion?
  attaches_to:
  - pathophysiology#Some Node
"""

UNDECIDABLE = """- discussion_id: undecidable_gap
  kind: KNOWLEDGE_GAP
  status: OPEN
  prompt: Which fraction accounts for the protection?
  attaches_to:
  - pathophysiology#Some Node
  proposed_experiments:
  - experiment_id: exp_prose_only
    name: A well-described protocol
    description: Several paragraphs with no stated stopping rule.
"""

BARE_TARGETS = """- discussion_id: bare_target_gap
  kind: KNOWLEDGE_GAP
  status: OPEN
  prompt: Does the readout track the node?
  attaches_to:
  - pathophysiology#Some Node
  proposed_experiments:
  - experiment_id: exp_bare
    name: Two bare targets in one experiment
    perturbations:
    - name: Gene correction
      target: Some Node
    readouts:
    - name: Marker level
      target: Some Node
"""

RESOLVED_BARE = """- discussion_id: resolved_gap
  kind: KNOWLEDGE_GAP
  status: RESOLVED
  prompt: Should this literature be curated here?
  attaches_to:
  - genetic#GENE
"""

RESOLVED_COMPLETE = """- discussion_id: resolved_complete_gap
  kind: KNOWLEDGE_GAP
  status: RESOLVED
  prompt: Should this literature be curated here?
  attaches_to:
  - genetic#GENE
  resolution_note: Out of scope; a different phenotype and variant class.
  resolved_date: '2026-09-02T00:00:00Z'
"""

OTHER_KIND = """- discussion_id: not_a_gap
  kind: CONTROVERSY
  status: OPEN
  prompt: The two published cohorts disagree.
  proposed_experiments:
  - experiment_id: exp_no_logic
    name: Prose only
"""


def _states(tmp_path: Path) -> dict[str, list[str]]:
    return {g.discussion_id: g.states for g in audit.collect(tmp_path)}


# --------------------------------------------------------------------------- #
# state detection
# --------------------------------------------------------------------------- #


def test_a_complete_gap_is_in_no_state(tmp_path: Path) -> None:
    _write(tmp_path / "kb" / "disorders", "A", COMPLETE)
    assert _states(tmp_path)["complete_gap"] == []


def test_each_state_fires_independently(tmp_path: Path) -> None:
    kb = tmp_path / "kb" / "disorders"
    _write(kb, "A", UNANCHORED)
    _write(kb, "B", NO_STATUS)
    _write(kb, "C", UNDECIDABLE)
    _write(kb, "D", BARE_TARGETS)
    _write(kb, "E", RESOLVED_BARE)

    states = _states(tmp_path)

    assert states["unanchored_gap"] == ["UNANCHORED"]
    assert states["no_status_gap"] == ["NO_STATUS"]
    assert states["undecidable_gap"] == ["UNDECIDABLE_EXPERIMENT"]
    assert states["bare_target_gap"] == ["BARE_EXPERIMENT_TARGET"]
    assert set(states["resolved_gap"]) == {"RESOLVED_NO_NOTE", "RESOLVED_NO_DATE"}


def test_a_resolved_gap_with_note_and_date_is_clean(tmp_path: Path) -> None:
    _write(tmp_path / "kb" / "disorders", "A", RESOLVED_COMPLETE)
    assert _states(tmp_path)["resolved_complete_gap"] == []


def test_only_knowledge_gap_discussions_are_audited(tmp_path: Path) -> None:
    _write(tmp_path / "kb" / "disorders", "A", OTHER_KIND)
    assert audit.collect(tmp_path) == []


# --------------------------------------------------------------------------- #
# the bare-target rule
# --------------------------------------------------------------------------- #


def test_a_prefixed_target_is_not_flagged_but_a_bare_name_is(tmp_path: Path) -> None:
    kb = tmp_path / "kb" / "disorders"
    _write(kb, "A", COMPLETE)  # target: pathophysiology#Some Node
    _write(kb, "B", BARE_TARGETS)

    states = _states(tmp_path)

    assert "BARE_EXPERIMENT_TARGET" not in states["complete_gap"]
    assert "BARE_EXPERIMENT_TARGET" in states["bare_target_gap"]


def test_bare_target_state_is_recorded_once_but_every_site_is_detailed(
    tmp_path: Path,
) -> None:
    _write(tmp_path / "kb" / "disorders", "A", BARE_TARGETS)

    (gap,) = audit.collect(tmp_path)

    assert gap.states.count("BARE_EXPERIMENT_TARGET") == 1
    assert len(gap.detail) == 2
    assert any("perturbations" in line for line in gap.detail)
    assert any("readouts" in line for line in gap.detail)


def test_detail_falls_back_to_the_name_when_experiment_id_is_absent(
    tmp_path: Path,
) -> None:
    _write(
        tmp_path / "kb" / "disorders",
        "A",
        """- discussion_id: g
  kind: KNOWLEDGE_GAP
  status: OPEN
  prompt: Does the readout track the node?
  attaches_to:
  - pathophysiology#Some Node
  proposed_experiments:
  - name: Unidentified experiment
    readouts:
    - name: Marker
      target: Some Node
""",
    )

    (gap,) = audit.collect(tmp_path)

    assert "None." not in gap.detail[0]
    assert "Unidentified experiment" in gap.detail[0]


# --------------------------------------------------------------------------- #
# retired-grade prose
# --------------------------------------------------------------------------- #


def test_retired_grade_matches_whole_word_only(tmp_path: Path) -> None:
    kb = tmp_path / "kb" / "disorders"
    _write(
        kb,
        "A",
        """- discussion_id: retired
  kind: KNOWLEDGE_GAP
  status: OPEN
  prompt: p
  attaches_to: [pathophysiology#N]
  evidence:
  - reference: PMID:1
    supports: SUPPORT
    explanation: Graded PARTIAL because the cohort was small.
""",
    )
    _write(
        kb,
        "B",
        """- discussion_id: ordinary_prose
  kind: KNOWLEDGE_GAP
  status: OPEN
  prompt: p
  attaches_to: [pathophysiology#N]
  evidence:
  - reference: PMID:2
    supports: SUPPORT
    explanation: The mechanism is PARTIALLY understood.
""",
    )

    states = _states(tmp_path)

    assert "RETIRED_GRADE_PROSE" in states["retired"]
    assert "RETIRED_GRADE_PROSE" not in states["ordinary_prose"]


def test_evidence_nested_in_a_proposed_experiment_is_searched_too(
    tmp_path: Path,
) -> None:
    _write(
        tmp_path / "kb" / "disorders",
        "A",
        """- discussion_id: nested
  kind: KNOWLEDGE_GAP
  status: OPEN
  prompt: p
  attaches_to: [pathophysiology#N]
  proposed_experiments:
  - experiment_id: e
    name: n
    decision_criterion: c
    readouts:
    - name: r
      target: pathophysiology#N
      evidence:
      - reference: PMID:3
        supports: SUPPORT
        explanation: Marked PARTIAL for the reasons above.
""",
    )

    assert "RETIRED_GRADE_PROSE" in _states(tmp_path)["nested"]


# --------------------------------------------------------------------------- #
# corpus walking
# --------------------------------------------------------------------------- #


def test_every_kb_subtree_that_can_carry_discussions_is_walked(
    tmp_path: Path,
) -> None:
    for subdir in ("disorders", "modules", "comorbidities", "groupings"):
        _write(tmp_path / "kb" / subdir, subdir.title(), UNANCHORED)

    assert len(audit.collect(tmp_path)) == 4


def test_history_records_beside_an_entry_are_skipped(tmp_path: Path) -> None:
    kb = tmp_path / "kb" / "disorders"
    _write(kb, "A", UNANCHORED)
    (kb / "A.history.yaml").write_text("name: stray\n", encoding="utf-8")

    assert len(audit.collect(tmp_path)) == 1


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #


def test_strict_exits_nonzero_on_a_bare_target(
    tmp_path: Path, monkeypatch, capsys
) -> None:
    _write(tmp_path / "kb" / "disorders", "A", BARE_TARGETS)
    monkeypatch.setattr(audit, "_REPO_ROOT", tmp_path)

    assert audit.main(["--strict"]) == 1
    assert "BARE_EXPERIMENT_TARGET" in capsys.readouterr().err


def test_strict_exits_nonzero_on_a_resolved_gap_with_no_note(
    tmp_path: Path, monkeypatch
) -> None:
    _write(tmp_path / "kb" / "disorders", "A", RESOLVED_BARE)
    monkeypatch.setattr(audit, "_REPO_ROOT", tmp_path)

    assert audit.main(["--strict"]) == 1


def test_strict_ignores_the_states_that_are_backlog(
    tmp_path: Path, monkeypatch
) -> None:
    kb = tmp_path / "kb" / "disorders"
    _write(kb, "A", UNANCHORED)
    _write(kb, "B", NO_STATUS)
    _write(kb, "C", UNDECIDABLE)
    monkeypatch.setattr(audit, "_REPO_ROOT", tmp_path)

    # Three reported states, none of them breakage: the gate stays green.
    assert audit.main(["--strict"]) == 0


def test_quiet_strict_prints_one_line_and_no_census(
    tmp_path: Path, monkeypatch, capsys
) -> None:
    _write(tmp_path / "kb" / "disorders", "A", COMPLETE)
    monkeypatch.setattr(audit, "_REPO_ROOT", tmp_path)

    assert audit.main(["--strict", "--quiet"]) == 0
    out = capsys.readouterr().out
    assert out.startswith("OK:")
    assert "KNOWLEDGE_GAP discussions:" not in out


def test_summary_counts_the_whole_corpus_and_reports_experiment_figures(
    tmp_path: Path, monkeypatch, capsys
) -> None:
    kb = tmp_path / "kb" / "disorders"
    _write(kb, "A", COMPLETE)
    _write(kb, "B", UNDECIDABLE)
    monkeypatch.setattr(audit, "_REPO_ROOT", tmp_path)

    assert audit.main([]) == 0
    out = capsys.readouterr().out

    assert "KNOWLEDGE_GAP discussions: 2 across 2 entries" in out
    assert "Proposed experiments: 2" in out
    assert "with no decision logic: 1 (50%)" in out
    assert "decision_criterion" in out


def test_state_filter_narrows_the_list(tmp_path: Path, monkeypatch, capsys) -> None:
    kb = tmp_path / "kb" / "disorders"
    _write(kb, "A", UNANCHORED)
    _write(kb, "B", NO_STATUS)
    monkeypatch.setattr(audit, "_REPO_ROOT", tmp_path)

    assert audit.main(["--format", "list", "--state", "UNANCHORED"]) == 0
    out = capsys.readouterr().out

    assert "unanchored_gap" in out
    assert "no_status_gap" not in out


def test_out_writes_to_a_file_in_every_format(
    tmp_path: Path, monkeypatch, capsys
) -> None:
    _write(tmp_path / "kb" / "disorders", "A", BARE_TARGETS)
    monkeypatch.setattr(audit, "_REPO_ROOT", tmp_path)

    expected = {
        "summary": "BARE_EXPERIMENT_TARGET",
        "list": "bare_target_gap",
        "tsv": "bare_target_gap",
    }
    for fmt, needle in expected.items():
        out = tmp_path / f"audit.{fmt}"
        assert audit.main(["--format", fmt, "--out", str(out)]) == 0
        assert needle in out.read_text(encoding="utf-8")
        # The report went to the file, not to stdout.
        assert capsys.readouterr().out == ""


def test_tsv_round_trips_the_per_gap_row(tmp_path: Path, monkeypatch, capsys) -> None:
    _write(tmp_path / "kb" / "disorders", "A", BARE_TARGETS)
    monkeypatch.setattr(audit, "_REPO_ROOT", tmp_path)

    assert audit.main(["--format", "tsv"]) == 0
    lines = capsys.readouterr().out.strip().splitlines()

    header = lines[0].split("\t")
    row = dict(zip(header, lines[1].split("\t"), strict=True))
    assert row["discussion_id"] == "bare_target_gap"
    assert row["states"] == "BARE_EXPERIMENT_TARGET"
    assert row["n_experiments"] == "1"
