"""Tests for ontology closure in grouping membership-criteria evaluation.

A criteria leaf asserting "has P" must be satisfied by a member annotated with
any is_a/part_of descendant of P. Without closure, a grouping whose criteria
cite high-level anatomical terms reads as violated by every member that curated
a more specific child term (see the Motor Neuron Disorders grouping, where
HP:0007354 amyotrophic lateral sclerosis did not match its parent HP:0007373
motor neuron atrophy).

The tests fake the OAK adapter so they stay offline and deterministic.
"""

from __future__ import annotations

import pytest

from dismech import groupings as G


class _FakeAdapter:
    """Minimal OAK stand-in exposing just the descendants() call we use."""

    def __init__(self, hierarchy: dict[str, list[str]]):
        self.hierarchy = hierarchy

    def descendants(self, seeds, predicates=None):
        out: set[str] = set()
        for seed in seeds:
            out.add(seed)
            out.update(self.hierarchy.get(seed, []))
        return out


HIERARCHY = {
    # HP:0007354 (ALS) is an is_a descendant of HP:0007373 (motor neuron atrophy).
    "HP:0007373": ["HP:0002398", "HP:0007354"],
    "GO:0006914": ["GO:0000045"],
}


@pytest.fixture
def fake_ontology(monkeypatch):
    """Point term_closure at a fake hierarchy and reset its caches."""
    monkeypatch.setattr(G, "_get_oak_adapter", lambda _s: _FakeAdapter(HIERARCHY))
    G.term_closure.cache_clear()
    G.set_closure_enabled(True)
    yield
    G.term_closure.cache_clear()
    G.set_closure_enabled(True)


def _phenotype_leaf(term_id: str, **extra) -> dict:
    return {
        "criterion_predicate": "HAS_PHENOTYPE",
        "phenotype_term": {"term": {"id": term_id}},
        **extra,
    }


def test_phenotype_criterion_satisfied_by_descendant_term(fake_ontology):
    """A member annotated with a descendant satisfies a parent-term criterion."""
    facts = G.DiseaseFacts(name="ALS-PDC", phenotype_freq={"HP:0007354": None})
    assert (
        G._eval_leaf(_phenotype_leaf("HP:0007373"), facts) is G.Satisfaction.SATISFIED
    )


def test_phenotype_criterion_not_satisfied_outside_closure(fake_ontology):
    """A term outside the criterion's closure still reports NOT_SATISFIED."""
    facts = G.DiseaseFacts(name="Konzo", phenotype_freq={"HP:0002061": None})
    assert (
        G._eval_leaf(_phenotype_leaf("HP:0007373"), facts)
        is G.Satisfaction.NOT_SATISFIED
    )


def test_closure_can_be_disabled_for_exact_matching(fake_ontology):
    """--no-closure restores exact-ID matching."""
    facts = G.DiseaseFacts(name="ALS-PDC", phenotype_freq={"HP:0007354": None})
    G.set_closure_enabled(False)
    G.term_closure.cache_clear()
    assert (
        G._eval_leaf(_phenotype_leaf("HP:0007373"), facts)
        is G.Satisfaction.NOT_SATISFIED
    )


def test_closure_degrades_to_exact_match_when_ontology_unavailable(monkeypatch):
    """An unreachable ontology under-reports rather than raising."""
    monkeypatch.setattr(G, "_get_oak_adapter", lambda _s: None)
    G.term_closure.cache_clear()
    try:
        assert G.term_closure("HP:0007373") == frozenset({"HP:0007373"})
        exact = G.DiseaseFacts(name="ALS", phenotype_freq={"HP:0007373": None})
        assert (
            G._eval_leaf(_phenotype_leaf("HP:0007373"), exact)
            is G.Satisfaction.SATISFIED
        )
    finally:
        G.term_closure.cache_clear()


def test_gene_criterion_is_not_closed_over(fake_ontology):
    """HGNC has no subsumption hierarchy, so gene criteria stay exact matches."""
    assert G.term_closure("hgnc:11117") == frozenset({"hgnc:11117"})


def test_biological_process_criterion_uses_closure(fake_ontology):
    """GO criteria match descendant processes too."""
    leaf = {
        "criterion_predicate": "HAS_BIOLOGICAL_PROCESS",
        "biological_processes": [{"term": {"id": "GO:0006914"}}],
    }
    facts = G.DiseaseFacts(name="X", go_ids={"GO:0000045"})
    assert G._eval_leaf(leaf, facts) is G.Satisfaction.SATISFIED
    unrelated = G.DiseaseFacts(name="Y", go_ids={"GO:0007249"})
    assert G._eval_leaf(leaf, unrelated) is G.Satisfaction.NOT_SATISFIED


def test_min_frequency_uses_strongest_matching_descendant(fake_ontology):
    """With several matching descendants, the strongest frequency is compared."""
    leaf = _phenotype_leaf("HP:0007373", min_frequency="FREQUENT")
    facts = G.DiseaseFacts(
        name="X",
        phenotype_freq={"HP:0002398": "OCCASIONAL", "HP:0007354": "VERY_FREQUENT"},
    )
    assert G._eval_leaf(leaf, facts) is G.Satisfaction.SATISFIED

    weak = G.DiseaseFacts(name="Y", phenotype_freq={"HP:0002398": "OCCASIONAL"})
    assert G._eval_leaf(leaf, weak) is G.Satisfaction.NOT_SATISFIED
