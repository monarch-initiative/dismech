"""Tests for the CONFORMS_TO_MODULE `#Node` anchor advisory (dismech#9403).

A grouping criterion is written ``module_stem#Node Name``, but the evaluator
matches on the stem alone — so SATISFIED means "conforms to that module
somewhere", not "conforms at the node the criterion names". Honouring the
anchor as a verdict would flip live results, and some of those flips are
criteria bugs rather than curation gaps, so the gap is *reported* instead.

The contract these tests pin:

* the verdict is unchanged — stem matching still decides SATISFIED;
* ``anchor_misses`` names every criterion satisfied only on the stem;
* ``anchor_exact_result`` is set **only** when honouring the anchors would
  change the block verdict, so an OR-sibling miss is not dressed up as a
  pending contradiction.
"""

from __future__ import annotations

import pytest

from dismech import groupings as G
from dismech.groupings import DiseaseFacts, Satisfaction, evaluate_grouping


@pytest.fixture(autouse=True)
def offline_terms():
    """Keep term-valued leaves offline; these tests only exercise modules."""
    G.set_closure_enabled(False)
    yield
    G.set_closure_enabled(True)


def _facts(name: str, *conforms: str) -> DiseaseFacts:
    facts = DiseaseFacts(name=name)
    for ref in conforms:
        facts.module_stems.add(ref.split("#", 1)[0].strip())
        facts.module_refs.add(G._normalize_module_ref(ref))
    return facts


def _grouping(logic: dict, member: str = "D", semantics: str = "NECESSARY") -> dict:
    return {
        "name": "G",
        "members": [{"member": member, "member_type": "DISEASE"}],
        "membership_criteria": [{"criteria_semantics": semantics, "logic": logic}],
    }


LEAF_BASAL = {
    "criterion_predicate": "CONFORMS_TO_MODULE",
    "module": "ciliopathy_dysfunction#Basal Body and Transition Zone Dysfunction",
}
LEAF_MOTILE = {
    "criterion_predicate": "CONFORMS_TO_MODULE",
    "module": "ciliopathy_dysfunction#Motile Cilia Beat Dysfunction",
}


def test_anchor_mismatch_still_satisfies_on_the_stem():
    """The verdict is unchanged: this is an advisory, not a semantics change."""
    index = {
        "D": _facts(
            "D", "ciliopathy_dysfunction#Basal Body and Transition Zone Dysfunction"
        )
    }
    (ev,) = evaluate_grouping(_grouping(LEAF_MOTILE), index)

    assert ev.result is Satisfaction.SATISFIED
    assert ev.anchor_misses == ["ciliopathy_dysfunction#Motile Cilia Beat Dysfunction"]


def test_anchor_match_reports_nothing():
    index = {"D": _facts("D", "ciliopathy_dysfunction#Motile Cilia Beat Dysfunction")}
    (ev,) = evaluate_grouping(_grouping(LEAF_MOTILE), index)

    assert ev.result is Satisfaction.SATISFIED
    assert ev.anchor_misses == []
    assert ev.anchor_exact_result is None


def test_stem_miss_is_not_an_anchor_advisory():
    """A member that does not conform to the module at all is plain NOT_SATISFIED."""
    index = {"D": _facts("D", "fibrotic_response#Mesenchymal Cell Activation")}
    (ev,) = evaluate_grouping(_grouping(LEAF_MOTILE), index)

    assert ev.result is Satisfaction.NOT_SATISFIED
    assert ev.anchor_misses == []
    assert ev.anchor_exact_result is None


def test_or_sibling_miss_does_not_flag_a_verdict_change():
    """The Ciliopathies shape: an OR over both arms, member is on one of them.

    28 of the 47 leaf misses in `kb/` are this. Reporting them as pending
    contradictions is exactly the false-alarm mode the advisory exists to avoid.
    """
    logic = {"operator": "OR", "operands": [LEAF_BASAL, LEAF_MOTILE]}
    index = {
        "D": _facts(
            "D", "ciliopathy_dysfunction#Basal Body and Transition Zone Dysfunction"
        )
    }
    (ev,) = evaluate_grouping(_grouping(logic), index)

    assert ev.result is Satisfaction.SATISFIED
    assert ev.anchor_misses == ["ciliopathy_dysfunction#Motile Cilia Beat Dysfunction"]
    assert ev.anchor_exact_result is None  # the block verdict is unaffected


def test_conjunctive_miss_reports_the_verdict_it_would_get():
    """A bare or AND-ed leaf is the actionable case: the block verdict moves."""
    logic = {"operator": "AND", "operands": [LEAF_BASAL, LEAF_MOTILE]}
    index = {
        "D": _facts(
            "D", "ciliopathy_dysfunction#Basal Body and Transition Zone Dysfunction"
        )
    }
    (ev,) = evaluate_grouping(_grouping(logic), index)

    assert ev.result is Satisfaction.SATISFIED
    assert ev.anchor_exact_result is Satisfaction.NOT_SATISFIED


def test_anchor_free_criterion_keeps_stem_semantics_under_anchor_exact():
    """A criterion naming no node has nothing to tighten, so it never flips."""
    bare = {
        "criterion_predicate": "CONFORMS_TO_MODULE",
        "module": "ciliopathy_dysfunction",
    }
    logic = {"operator": "AND", "operands": [bare, LEAF_MOTILE]}
    index = {
        "D": _facts(
            "D", "ciliopathy_dysfunction#Basal Body and Transition Zone Dysfunction"
        )
    }
    (ev,) = evaluate_grouping(_grouping(logic), index)

    # The motile leaf flips the block; the bare-stem leaf must not contribute.
    assert ev.anchor_misses == ["ciliopathy_dysfunction#Motile Cilia Beat Dysfunction"]
    assert G._eval_leaf(bare, index["D"], anchor_exact=True) is Satisfaction.SATISFIED


def test_empty_anchor_criterion_is_not_advised_on():
    """`"module#"` names no node, so it cannot be missing one."""
    empty = {
        "criterion_predicate": "CONFORMS_TO_MODULE",
        "module": "ciliopathy_dysfunction#",
    }
    index = {
        "D": _facts(
            "D", "ciliopathy_dysfunction#Basal Body and Transition Zone Dysfunction"
        )
    }
    (ev,) = evaluate_grouping(_grouping(empty), index)

    assert ev.result is Satisfaction.SATISFIED
    assert ev.anchor_misses == []
    assert ev.anchor_exact_result is None


def test_negated_leaf_is_not_advised_on():
    """Under `negated`, a stem match already yields NOT_SATISFIED."""
    negated = dict(LEAF_MOTILE, negated=True)
    index = {
        "D": _facts(
            "D", "ciliopathy_dysfunction#Basal Body and Transition Zone Dysfunction"
        )
    }
    (ev,) = evaluate_grouping(_grouping(negated), index)

    assert ev.result is Satisfaction.NOT_SATISFIED
    assert ev.anchor_misses == []


def test_whitespace_and_empty_anchor_normalize():
    assert G._normalize_module_ref(
        "  fibrotic_response # Mesenchymal Cell Activation "
    ) == ("fibrotic_response#Mesenchymal Cell Activation")
    assert G._normalize_module_ref("fibrotic_response#") == "fibrotic_response"
    assert G._normalize_module_ref("fibrotic_response") == "fibrotic_response"
