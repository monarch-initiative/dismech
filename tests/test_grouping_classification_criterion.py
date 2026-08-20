"""Tests for the HAS_CLASSIFICATION grouping membership criterion.

``HAS_CLASSIFICATION`` was declared in the schema's ``CriterionPredicateEnum``
but never implemented in the evaluator, so every criterion using it fell through
to UNKNOWN. That made whole grouping families unauditable: the nine IUIS-table
sub-groupings under Inborn Errors of Immunity each assert "member carries this
``classifications.iuis_category``" as a NECESSARY criterion, which is exactly the
kind of claim the audit exists to check, and the audit could not check it.

DisMech has no single canonical nosology slot, so the criterion reads three
sources: the structured ``classifications:`` block (both bare and keyed
``<slot>:<value>``), and the free-text ``parents:`` and ``categories:`` lists
where tags such as ``RASopathy`` live.
"""

from __future__ import annotations

from dismech import groupings as G


def _leaf(value: str, **extra) -> dict:
    return {"criterion_predicate": "HAS_CLASSIFICATION", "classification": value, **extra}


def _facts(entry: dict) -> G.DiseaseFacts:
    return G.extract_disease_facts(entry.get("name", "X"), entry)


IEI_ENTRY = {
    "name": "STK4 Deficiency",
    "classifications": {
        "iuis_category": {"classification_value": "combined immunodeficiency"},
        "harrisons_chapter": [{"classification_value": "IMMUNE_RHEUMATOLOGIC"}],
    },
}

RASOPATHY_ENTRY = {"name": "Noonan Syndrome", "parents": ["RASopathy"]}


def test_structured_classification_value_satisfies_bare_criterion():
    assert (
        G._eval_leaf(_leaf("combined immunodeficiency"), _facts(IEI_ENTRY))
        is G.Satisfaction.SATISFIED
    )


def test_structured_classification_value_satisfies_keyed_criterion():
    """The keyed form is what the IUIS groupings use, so it must resolve."""
    assert (
        G._eval_leaf(
            _leaf("iuis_category:combined immunodeficiency"), _facts(IEI_ENTRY)
        )
        is G.Satisfaction.SATISFIED
    )


def test_keyed_criterion_is_not_satisfied_by_the_same_value_under_another_slot():
    """The point of the keyed form: disambiguate schemes sharing a string."""
    assert (
        G._eval_leaf(
            _leaf("harrisons_chapter:combined immunodeficiency"), _facts(IEI_ENTRY)
        )
        is G.Satisfaction.NOT_SATISFIED
    )


def test_multivalued_classification_slot_contributes_every_assignment():
    assert (
        G._eval_leaf(_leaf("IMMUNE_RHEUMATOLOGIC"), _facts(IEI_ENTRY))
        is G.Satisfaction.SATISFIED
    )


def test_wrong_table_is_a_contradiction_not_an_unknown():
    """A member in the wrong IUIS sub-grouping must surface, not go quiet."""
    assert (
        G._eval_leaf(
            _leaf("iuis_category:immune dysregulation"), _facts(IEI_ENTRY)
        )
        is G.Satisfaction.NOT_SATISFIED
    )


def test_free_text_parents_slot_counts():
    """RASopathies tags members in `parents:`, not in `classifications:`."""
    assert (
        G._eval_leaf(_leaf("RASopathy"), _facts(RASOPATHY_ENTRY))
        is G.Satisfaction.SATISFIED
    )


def test_free_text_categories_slot_counts():
    entry = {"name": "Neurofibromatosis Type 1", "categories": ["RASopathy"]}
    assert G._eval_leaf(_leaf("RASopathy"), _facts(entry)) is G.Satisfaction.SATISFIED


def test_matching_is_case_and_whitespace_insensitive():
    entry = {
        "name": "X",
        "classifications": {"iuis_category": {"classification_value": "Phagocyte  Defect"}},
    }
    assert (
        G._eval_leaf(_leaf("iuis_category:phagocyte defect"), _facts(entry))
        is G.Satisfaction.SATISFIED
    )


def test_plural_drift_is_reported_rather_than_normalized_away():
    """`RASopathies` must not silently satisfy a `RASopathy` criterion.

    Normalizing plurals would hide exactly the tag drift the RASopathies
    grouping had to normalize by hand; surfacing it as NOT_SATISFIED is the
    point.
    """
    entry = {"name": "Costello Syndrome", "parents": ["RASopathies"]}
    assert G._eval_leaf(_leaf("RASopathy"), _facts(entry)) is G.Satisfaction.NOT_SATISFIED


def test_negated_criterion_is_satisfied_by_absence():
    """B-Cell Non-Hodgkin Lymphoma excludes members via a negated leaf."""
    assert (
        G._eval_leaf(_leaf("Hodgkin lymphoma", negated=True), _facts(IEI_ENTRY))
        is G.Satisfaction.SATISFIED
    )


def test_criterion_without_a_classification_payload_stays_unknown():
    """An unfillable leaf must not be read as a violation."""
    leaf = {"criterion_predicate": "HAS_CLASSIFICATION"}
    assert G._eval_leaf(leaf, _facts(IEI_ENTRY)) is G.Satisfaction.UNKNOWN
