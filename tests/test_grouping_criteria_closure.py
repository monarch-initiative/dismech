"""Tests for ontology closure in grouping membership-criteria evaluation.

A criteria leaf asserting "has P" must be satisfied by a member annotated with
any is_a/part_of descendant of P. Without closure, a grouping whose criteria
cite high-level anatomical terms reads as violated by every member that curated
a more specific child term (see the Motor Neuron Disorders grouping, where
HP:0007354 amyotrophic lateral sclerosis did not match its parent HP:0007373
motor neuron atrophy).

Closures are read from the committed ``cache/closure/<prefix>.csv`` first and
only then from the ontology. A term with no known closure evaluates to UNKNOWN:
the old behaviour of degrading to an exact match reported 58 false
contradictions across the KB, because a criterion deliberately stated at a
parent term is a *different* criterion once it is matched exactly.

The tests fake both the cache directory and the OAK adapter so they stay
offline and deterministic.
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
def empty_cache(monkeypatch, tmp_path):
    """Point the closure cache at an empty directory and reset every memo."""
    monkeypatch.setattr(G, "CLOSURE_CACHE_DIR", tmp_path)
    G.reset_closure_caches()
    G.set_live_lookup_enabled(True)
    yield tmp_path
    G.reset_closure_caches()
    G.set_live_lookup_enabled(True)


@pytest.fixture
def fake_ontology(monkeypatch, empty_cache):
    """Serve the fake hierarchy live, with nothing cached."""
    monkeypatch.setattr(G, "_get_oak_adapter", lambda _s: _FakeAdapter(HIERARCHY))
    yield


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


def test_cache_is_read_before_the_ontology(monkeypatch, empty_cache):
    """A cached closure is used even when the ontology is unreachable."""
    monkeypatch.setattr(G, "_get_oak_adapter", lambda _s: None)
    G.write_closure_cache(
        G.closure_cache_path("HP", empty_cache), {"HP:0007373": {"HP:0007354"}}
    )
    G.reset_closure_caches()
    assert G.term_closure("HP:0007373") == frozenset({"HP:0007373", "HP:0007354"})
    facts = G.DiseaseFacts(name="ALS-PDC", phenotype_freq={"HP:0007354": None})
    assert (
        G._eval_leaf(_phenotype_leaf("HP:0007373"), facts) is G.Satisfaction.SATISFIED
    )


def test_cached_term_with_no_descendants_is_known(empty_cache):
    """The reflexive row records "no descendants" as a fact, not a miss."""
    G.write_closure_cache(
        G.closure_cache_path("HP", empty_cache), {"HP:0007354": set()}
    )
    G.reset_closure_caches()
    G.set_live_lookup_enabled(False)
    assert G.term_closure("HP:0007354") == frozenset({"HP:0007354"})
    assert G.cached_closure("HP:0007373") is None


def test_offline_uncached_term_evaluates_unknown(fake_ontology):
    """--offline never contacts the ontology; an uncached term is UNKNOWN."""
    G.set_live_lookup_enabled(False)
    assert G.term_closure("HP:0007373") is None
    facts = G.DiseaseFacts(name="ALS-PDC", phenotype_freq={"HP:0007354": None})
    assert G._eval_leaf(_phenotype_leaf("HP:0007373"), facts) is G.Satisfaction.UNKNOWN


def test_unreachable_ontology_evaluates_unknown_not_exact(monkeypatch, empty_cache):
    """An unreachable ontology must not be downgraded to exact matching.

    Under exact matching a member curating the criterion's child term reads as
    a contradiction, which is a fabricated verdict, not an under-report.
    """
    monkeypatch.setattr(G, "_get_oak_adapter", lambda _s: None)
    assert G.term_closure("HP:0007373") is None
    child = G.DiseaseFacts(name="ALS", phenotype_freq={"HP:0007354": None})
    assert G._eval_leaf(_phenotype_leaf("HP:0007373"), child) is G.Satisfaction.UNKNOWN
    # Even an exact-term member is UNKNOWN: the evaluator does not know the
    # closure, so it does not claim to.
    exact = G.DiseaseFacts(name="ALS", phenotype_freq={"HP:0007373": None})
    assert G._eval_leaf(_phenotype_leaf("HP:0007373"), exact) is G.Satisfaction.UNKNOWN


def test_unknown_closure_in_a_conjunction_is_unknown_not_contradiction(
    monkeypatch, empty_cache
):
    """The whole point: no closure -> UNKNOWN, which cannot fail --strict."""
    monkeypatch.setattr(G, "_get_oak_adapter", lambda _s: None)
    gene = {"criterion_predicate": "HAS_GENE", "gene": {"term": {"id": "hgnc:1"}}}
    logic = {"operator": "AND", "operands": [gene, _phenotype_leaf("HP:0007373")]}
    facts = G.DiseaseFacts(
        name="X", gene_ids={"hgnc:1"}, phenotype_freq={"HP:0007354": None}
    )
    assert G._eval_node(logic, facts) is G.Satisfaction.UNKNOWN


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


def test_biological_process_unknown_closure_only_matters_without_a_match(
    monkeypatch, empty_cache
):
    """With two listed processes, a match under a known one still satisfies."""
    G.write_closure_cache(
        G.closure_cache_path("GO", empty_cache), {"GO:0006914": {"GO:0000045"}}
    )
    G.reset_closure_caches()
    G.set_live_lookup_enabled(False)
    leaf = {
        "criterion_predicate": "HAS_BIOLOGICAL_PROCESS",
        "biological_processes": [
            {"term": {"id": "GO:0006914"}},
            {"term": {"id": "GO:0099999"}},  # uncached
        ],
    }
    assert (
        G._eval_leaf(leaf, G.DiseaseFacts(name="X", go_ids={"GO:0000045"}))
        is G.Satisfaction.SATISFIED
    )
    assert (
        G._eval_leaf(leaf, G.DiseaseFacts(name="Y", go_ids={"GO:0007249"}))
        is G.Satisfaction.UNKNOWN
    )


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


# --------------------------------------------------------------------------- #
# Cache file contract and builder
# --------------------------------------------------------------------------- #


def test_closure_cache_round_trips_sorted_with_reflexive_rows(tmp_path):
    path = G.closure_cache_path("HP", tmp_path)
    G.write_closure_cache(path, {"HP:0000002": {"HP:0000001"}, "HP:0000001": set()})
    assert path.read_text() == (
        "term,descendant\n"
        "HP:0000001,HP:0000001\n"
        "HP:0000002,HP:0000001\n"
        "HP:0000002,HP:0000002\n"
    )
    assert G.read_closure_cache(path) == {
        "HP:0000001": frozenset({"HP:0000001"}),
        "HP:0000002": frozenset({"HP:0000001", "HP:0000002"}),
    }


def test_closure_cache_rejects_wrong_header(tmp_path):
    path = tmp_path / "hp.csv"
    path.write_text("curie,label\nHP:1,x\n")
    with pytest.raises(ValueError):
        G.read_closure_cache(path)


def _grouping_file(tmp_path, name: str, *term_ids: str):
    leaves = "\n".join(
        f"""    - criterion_predicate: HAS_PHENOTYPE
      phenotype_term:
        term:
          id: {tid}
          label: x"""
        for tid in term_ids
    )
    path = tmp_path / f"{name}.yaml"
    path.write_text(
        f"""name: {name}
membership_criteria:
- description: d
  criteria_semantics: NECESSARY
  logic:
    operator: OR
    operands:
{leaves}
members:
- member: Nobody
"""
    )
    return path


def test_builder_is_append_only_and_reports_failures(monkeypatch, empty_cache):
    """Only uncached terms are fetched; a failed fetch is reported, not written."""
    path = G.closure_cache_path("HP", empty_cache)
    G.write_closure_cache(path, {"HP:0007373": {"HP:0007354"}})
    G.reset_closure_caches()

    calls: list[str] = []

    def fake_fetch(term_id: str):
        calls.append(term_id)
        return None if term_id == "HP:0000404" else frozenset({term_id, "HP:0000001"})

    monkeypatch.setattr(G, "fetch_closure", fake_fetch)
    grouping = _grouping_file(
        empty_cache, "G", "HP:0007373", "HP:0000118", "HP:0000404"
    )
    report = G.build_closure_cache([grouping], cache_dir=empty_cache)

    assert calls == ["HP:0000118", "HP:0000404"]  # cached term not re-fetched
    assert report.fetched == ["HP:0000118"]
    assert report.failed == ["HP:0000404"]
    cached = G.read_closure_cache(path)
    assert set(cached) == {"HP:0007373", "HP:0000118"}
    assert cached["HP:0007373"] == frozenset({"HP:0007373", "HP:0007354"})


def test_builder_refresh_and_prune(monkeypatch, empty_cache):
    path = G.closure_cache_path("HP", empty_cache)
    G.write_closure_cache(
        path, {"HP:0007373": {"HP:0000000"}, "HP:0009999": {"HP:0000000"}}
    )
    G.reset_closure_caches()
    monkeypatch.setattr(G, "fetch_closure", lambda t: frozenset({t, "HP:0000001"}))
    grouping = _grouping_file(empty_cache, "G", "HP:0007373")

    report = G.build_closure_cache([grouping], cache_dir=empty_cache, refresh=True)
    cached = G.read_closure_cache(path)
    assert cached["HP:0007373"] == frozenset({"HP:0007373", "HP:0000001"})
    assert "HP:0009999" in cached and not report.dropped  # kept without --prune

    report = G.build_closure_cache([grouping], cache_dir=empty_cache, prune=True)
    assert report.dropped == ["HP:0009999"]
    assert set(G.read_closure_cache(path)) == {"HP:0007373"}


def test_uncached_closure_terms_names_the_gap(empty_cache):
    G.write_closure_cache(
        G.closure_cache_path("HP", empty_cache), {"HP:0007373": set()}
    )
    G.reset_closure_caches()
    grouping = {
        "membership_criteria": [
            {
                "logic": {
                    "operator": "AND",
                    "operands": [
                        _phenotype_leaf("HP:0007373"),
                        _phenotype_leaf("HP:0000118"),
                        {
                            "criterion_predicate": "HAS_GENE",
                            "gene": {"term": {"id": "hgnc:1"}},
                        },
                    ],
                }
            }
        ]
    }
    assert G.criterion_closure_terms(grouping) == {"HP:0007373", "HP:0000118"}
    assert G.uncached_closure_terms(grouping) == ["HP:0000118"]


def test_lint_grouping_references_reports_every_dangling_key():
    grouping = {
        "members": [
            {"member": "Real", "member_type": "DISEASE"},
            {"member": "Ghost", "member_type": "SUBTYPE"},
            {"member": "Kids", "member_type": "GROUPING"},
            {"member": "Real", "member_type": "MODULE"},
            {
                "member": "Real",
                "differentiating_mechanisms": [{"module": "nope#Node"}],
            },
        ],
        "membership_criteria": [
            {
                "logic": {
                    "criterion_predicate": "CONFORMS_TO_MODULE",
                    "module": "fibrotic_response#X",
                }
            }
        ],
    }
    errors = G.lint_grouping_references(
        grouping,
        disease_names={"Real"},
        grouping_names=set(),
        module_stems={"fibrotic_response"},
    )
    assert len(errors) == 4
    assert any("Ghost" in e and "SUBTYPE" in e for e in errors)
    assert any("Kids" in e and "grouping" in e for e in errors)
    assert any("MODULE" in e and "unknown member type" in e for e in errors)
    assert any("nope" in e for e in errors)
