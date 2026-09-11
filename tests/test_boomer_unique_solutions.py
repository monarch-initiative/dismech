"""Opt-in regression checks for the merged Boomer unique-solutions fix.

Run with BOOMER_SRC=/path/to/merged/boomer-py/src. Boomer is deliberately
not a dismech runtime dependency; these checks skip when no source is supplied.
"""

import importlib
from itertools import product
from math import prod
import os
from pathlib import Path

import pytest

from dismech import kb_cache

REPO = Path(__file__).resolve().parents[1]


@pytest.fixture
def boomer(monkeypatch):
    source = os.environ.get("BOOMER_SRC")
    if not source:
        pytest.skip("Set BOOMER_SRC to the merged Boomer source directory")
    source = Path(source).expanduser().resolve()
    monkeypatch.syspath_prepend(str(source))
    model = importlib.import_module("boomer.model")
    search = importlib.import_module("boomer.search")
    assert Path(search.__file__).resolve().is_relative_to(source)
    return model, search


@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize(
    "slug,expected_worlds,expected_confidence",
    [
        ("2-Methylbutyryl-CoA_Dehydrogenase_Deficiency", 128, 0.9),
        ("ADan_amyloidosis", 192, 0.5),
        ("CANVAS", 384, 0.5),
    ],
)
def test_solution_probabilities_match_exhaustive_assignments(
    boomer, slug, expected_worlds, expected_confidence, reverse
):
    model, search = boomer
    path = REPO / "analyses/boomer/disorders" / slug / "kb.yaml"
    original = path.read_bytes()
    kb = model.KB.model_validate(kb_cache.load_document(path))
    if reverse:
        kb.pfacts.reverse()
    before = kb.model_dump()
    config = model.SearchConfig(
        partition_initial_threshold=len(kb.pfacts),
        max_pfacts_per_clique=None,
        max_candidate_solutions=0,
        max_iterations=2**63 - 1,
    )
    reasoner = search.get_reasoner(config.reasoner_class)
    # Enumerate every Boolean assignment once, independently of search paths.
    worlds = {}
    for values in product([False, True], repeat=len(kb.pfacts)):
        if reasoner.reason(kb, list(enumerate(values))).satisfiable:
            worlds[values] = prod(
                pfact.prob if value else 1 - pfact.prob
                for pfact, value in zip(kb.pfacts, values)
            )
    assert len(worlds) == expected_worlds
    total = sum(worlds.values())
    ranked = sorted(worlds.values(), reverse=True)
    solution = search.solve(kb, config)
    assert not solution.timed_out
    assert solution.number_of_satisfiable_combinations == expected_worlds
    assert solution.confidence == pytest.approx(expected_confidence)
    assert solution.confidence == pytest.approx(ranked[0] / sum(ranked[:2]))
    assert solution.prior_prob == pytest.approx(ranked[0])
    assert solution.posterior_prob == pytest.approx(ranked[0] / total)
    best_values = tuple(f.truth_value for f in solution.solved_pfacts)
    assert worlds[best_values] == pytest.approx(ranked[0])
    for index, fact in enumerate(solution.solved_pfacts):
        expected = sum(pr for values, pr in worlds.items() if values[index]) / total
        assert fact.posterior_prob == pytest.approx(expected)
    assert kb.model_dump() == before
    assert path.read_bytes() == original


@pytest.mark.parametrize("prior", [0.5, 0.8])
def test_duplicate_paths_preserve_raw_candidate_cap(boomer, monkeypatch, prior):
    model, search = boomer
    kb = model.KB(
        pfacts=[
            model.PFact(fact=model.EquivalentTo(sub="a", equivalent="b"), prob=prior),
            model.PFact(fact=model.EquivalentTo(sub="c", equivalent="d"), prob=0.9),
        ]
    )

    def node(selections, probability):
        return model.TreeNode(
            selections=selections,
            terminal=True,
            pr=probability,
            pr_selected=probability,
        )

    nodes = [
        node([(0, True), (1, True)], prior * 0.9),
        node([(1, True), (0, True)], prior * 0.9),
        node([(0, False), (1, True)], (1 - prior) * 0.9),
    ]
    monkeypatch.setattr(search, "search", lambda *args: iter(nodes))
    solution = search.solve(kb, model.SearchConfig(max_candidate_solutions=2))
    assert solution.number_of_combinations == 2
    assert solution.number_of_satisfiable_combinations == 1
    assert solution.confidence == 1.0
    assert solution.solved_pfacts[0].posterior_prob == 1.0


def test_separate_priors_for_same_logical_fact_are_preserved(boomer):
    model, search = boomer
    kb = model.KB(
        pfacts=[
            model.PFact(fact=model.EquivalentTo(sub="a", equivalent="b"), prob=0.9),
            model.PFact(fact=model.EquivalentTo(sub="a", equivalent="b"), prob=0.8),
        ]
    )
    solution = search.solve(kb)
    assert [f.pfact.prob for f in solution.solved_pfacts] == [0.9, 0.8]
    assert solution.number_of_satisfiable_combinations == 2
    # Both priors contribute: true weight .72, false weight .02.
    assert solution.prior_prob == pytest.approx(0.72)
    for fact in solution.solved_pfacts:
        assert fact.posterior_prob == pytest.approx(0.72 / 0.74)
