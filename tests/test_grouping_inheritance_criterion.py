"""Tests for the HAS_INHERITANCE membership criterion.

`HAS_INHERITANCE` used to be unevaluable: the predicate carried its constraint
in free-text `description` only, so every leaf resolved to UNKNOWN. That was not
a cosmetic gap. Groupings keyed on inheritance could not audit their own
members, could not surface a qualifying non-member as a candidate, and - worst -
an UNKNOWN leaf inside an AND poisons the whole conjunction, so a single
inheritance clause masked the checkable clauses beside it. Several groupings
worked around it in prose (see Familial_Hypertrophic_Cardiomyopathy, which drops
its Mendelian clause from the structured logic for exactly this reason).

The payload stays OPTIONAL: a leaf naming an `inheritance_term` is evaluated,
while a leaf that can only be said in words ("hereditary rather than acquired",
which no single HPO term names) keeps its old UNKNOWN behaviour.
"""

from __future__ import annotations

import pytest

from dismech import groupings as G

# HP:0010984 (digenic) and HP:0010983 (oligogenic) are HPO SIBLINGS under
# HP:0001426 (non-Mendelian inheritance) - neither subsumes the other.
HIERARCHY = {
    "HP:0001426": ["HP:0010982", "HP:0010983", "HP:0010984"],
    "HP:0000007": [],
}


class _FakeAdapter:
    def __init__(self, hierarchy: dict[str, list[str]]):
        self.hierarchy = hierarchy

    def descendants(self, seeds, predicates=None):
        out: set[str] = set()
        for seed in seeds:
            out.add(seed)
            out.update(self.hierarchy.get(seed, []))
        return out


@pytest.fixture
def fake_ontology(monkeypatch):
    monkeypatch.setattr(G, "_get_oak_adapter", lambda _s: _FakeAdapter(HIERARCHY))
    G.term_closure.cache_clear()
    G.set_closure_enabled(True)
    yield
    G.term_closure.cache_clear()
    G.set_closure_enabled(True)


def _leaf(term_id: str | None = None, **extra) -> dict:
    node: dict = {
        "criterion_predicate": "HAS_INHERITANCE",
        "description": "some inheritance constraint",
        **extra,
    }
    if term_id:
        node["inheritance_term"] = {"term": {"id": term_id}}
    return node


def _facts(*inheritance_ids: str) -> G.DiseaseFacts:
    return G.DiseaseFacts(name="Test Disease", inheritance_ids=set(inheritance_ids))


def test_matching_inheritance_term_is_satisfied(fake_ontology):
    assert G._eval_node(_leaf("HP:0010984"), _facts("HP:0010984")) is G.Satisfaction.SATISFIED


def test_absent_inheritance_term_is_not_satisfied(fake_ontology):
    assert G._eval_node(_leaf("HP:0010984"), _facts("HP:0000007")) is G.Satisfaction.NOT_SATISFIED


def test_payload_less_leaf_still_unknown(fake_ontology):
    """A constraint stated only in words stays unevaluated rather than guessed."""
    assert G._eval_node(_leaf(), _facts("HP:0010984")) is G.Satisfaction.UNKNOWN


def test_digenic_does_not_satisfy_an_oligogenic_criterion(fake_ontology):
    """The two are siblings, not parent/child - a grouping meaning either must OR them."""
    assert G._eval_node(_leaf("HP:0010983"), _facts("HP:0010984")) is G.Satisfaction.NOT_SATISFIED


def test_parent_criterion_satisfied_by_descendant_term(fake_ontology):
    """Closure applies, as it does for HAS_PHENOTYPE."""
    node = _leaf("HP:0001426")
    assert G._eval_node(node, _facts("HP:0010984")) is G.Satisfaction.SATISFIED


def test_negated_leaf_inverts(fake_ontology):
    node = _leaf("HP:0010984", negated=True)
    assert G._eval_node(node, _facts("HP:0010984")) is G.Satisfaction.NOT_SATISFIED


def test_leaf_does_not_require_the_payload_to_lint(fake_ontology):
    """Payload is optional, so a description-only leaf must remain well-formed."""
    assert G.lint_criterion(_leaf()) == []
    assert G.lint_criterion(_leaf("HP:0010984")) == []


def test_evaluable_leaf_no_longer_poisons_a_conjunction(fake_ontology):
    """The regression that made groupings avoid the predicate: UNKNOWN in an AND."""
    conjunction = {
        "operator": "AND",
        "operands": [
            _leaf("HP:0010984"),
            {
                "criterion_predicate": "CONFORMS_TO_MODULE",
                "module": "ciliopathy_dysfunction#Basal Body and Transition Zone Dysfunction",
            },
        ],
    }
    facts = G.DiseaseFacts(
        name="Test Disease",
        inheritance_ids={"HP:0010984"},
        module_stems={"ciliopathy_dysfunction"},
    )
    assert G._eval_node(conjunction, facts) is G.Satisfaction.SATISFIED


def test_inheritance_ids_extracted_from_every_curated_branch():
    """A disorder qualifies if ANY curated branch of it does.

    All three places an `inheritance` block is curated count: disease level,
    `has_subtypes`, and the per-gene blocks under `genetic`. The gene-level
    path is the easy one to overlook - no entry currently puts a multi-locus
    term there, but a per-gene digenic assertion is a reasonable place to make
    one, and it must not be silently dropped.
    """
    data = {
        "name": "Test Disease",
        "inheritance": [{"inheritance_term": {"term": {"id": "HP:0000007"}}}],
        "has_subtypes": [
            {
                "name": "Digenic subtype",
                "inheritance": [{"inheritance_term": {"term": {"id": "HP:0010984"}}}],
            }
        ],
        "genetic": [
            {
                "name": "SOME_GENE",
                "inheritance": [{"inheritance_term": {"term": {"id": "HP:0010983"}}}],
            }
        ],
    }
    facts = G.extract_disease_facts("Test Disease", data)
    assert facts.inheritance_ids == {"HP:0000007", "HP:0010984", "HP:0010983"}
    # Inheritance terms must not leak into the phenotype set, which would make
    # them satisfy HAS_PHENOTYPE criteria as well.
    assert "HP:0000007" not in facts.phenotype_freq


def test_non_hp_inheritance_terms_are_ignored():
    """Only HP ids are mode-of-inheritance terms; anything else is not one."""
    data = {
        "name": "Test Disease",
        "inheritance": [
            {"inheritance_term": {"term": {"id": "MONDO:0000001"}}},
            {"inheritance_term": {"preferred_term": "Sporadic occurrence"}},
        ],
    }
    facts = G.extract_disease_facts("Test Disease", data)
    assert facts.inheritance_ids == set()
