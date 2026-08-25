"""Tests for the 'Conditions satisfied' column on grouping coverage tables.

``evaluate_grouping`` computes an aggregate verdict per (member, criteria
block), but the coverage table used to render only the per-leaf columns — so a
listed member failing an OR of three leaves showed three red cells and nothing
naming the actual problem. A listed member that does not satisfy a NECESSARY
criterion is a contradiction between two curated assertions; the column reports
it as such and leaves the interpretation (curation gap? criteria too strict?
wrong member?) to the reader.
"""

from __future__ import annotations

from dismech.render import _coverage_conditions_cell


def _block(result: str, **extra) -> dict:
    return {
        "criteria_index": 0,
        "semantics": "NECESSARY",
        "result": result,
        "leaves": [],
        "unmet": [],
        **extra,
    }


def test_listed_member_failing_necessary_criteria_is_a_contradiction():
    cell = _coverage_conditions_cell(
        ["Kennedy Disease"],
        {"Kennedy Disease": [_block("NOT_SATISFIED", unmet=["Motor neuron atrophy."])]},
        is_listed=True,
    )
    assert cell["contradiction"] is True
    assert cell["result"] == "NOT_SATISFIED"
    assert cell["label"] == "contradiction"
    assert "Motor neuron atrophy." in cell["title"]
    assert "Contradiction" in cell["title"]


def test_unlisted_row_failing_criteria_is_not_a_contradiction():
    """Only a *listed* member contradicts the criteria by failing them."""
    cell = _coverage_conditions_cell(
        ["Some Disease"],
        {"Some Disease": [_block("NOT_SATISFIED")]},
        is_listed=False,
    )
    assert cell["contradiction"] is False
    assert cell["label"] == "not satisfied"


def test_satisfied_member_reports_plainly():
    cell = _coverage_conditions_cell(
        ["Amyotrophic Lateral Sclerosis"],
        {"Amyotrophic Lateral Sclerosis": [_block("SATISFIED")]},
        is_listed=True,
    )
    assert cell["contradiction"] is False
    assert cell["result"] == "SATISFIED"
    assert cell["label"] == "satisfied"


def test_row_without_audit_entries_is_not_evaluated():
    cell = _coverage_conditions_cell(["Unknown Disease"], {}, is_listed=False)
    assert cell["result"] == ""
    assert cell["label"] == "not evaluated"
    assert cell["contradiction"] is False


def test_worst_result_wins_across_criteria_blocks():
    """A member passing one block and failing another still contradicts."""
    cell = _coverage_conditions_cell(
        ["D"],
        {"D": [_block("SATISFIED"), _block("NOT_SATISFIED", criteria_index=1)]},
        is_listed=True,
    )
    assert cell["result"] == "NOT_SATISFIED"
    assert cell["contradiction"] is True


def test_unknown_does_not_read_as_a_contradiction():
    """UNKNOWN means unevaluable, not a violated axiom."""
    cell = _coverage_conditions_cell(["D"], {"D": [_block("UNKNOWN")]}, is_listed=True)
    assert cell["result"] == "UNKNOWN"
    assert cell["contradiction"] is False
    assert cell["label"] == "unknown"
