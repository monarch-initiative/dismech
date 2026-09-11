"""Tests for applying the candidate node-class tree across kb/."""

from __future__ import annotations

from pathlib import Path

import pytest

from dismech.node_class_scan import (
    CONFLICT,
    Assignment,
    ScanResult,
    classify_node,
    conformance_mismatches,
    conformance_pairs,
    load_seed,
    scan,
    summarize,
)

ROOT = Path(__file__).parent.parent
SEED = ROOT / "docs" / "superpowers" / "pathograph_node_class_go_seed.tsv"

# GO:0006915 apoptotic process -> CELLULAR HIGH; GO:0006325 chromatin
# organization -> GENOMIC HIGH; GO:0006954 inflammatory response -> TISSUE LOW.
CELL = "GO:0006915"
GENOME = "GO:0006325"
SOFT = "GO:0006954"


@pytest.fixture(scope="module")
def seed():
    return load_seed(SEED)


def bp(*ids):
    return {"biological_processes": [{"term": {"id": i}} for i in ids]}


def test_single_high_go_bp_term_assigns_its_class(seed):
    a = classify_node({"name": "N", **bp(CELL)}, seed)
    assert (a.node_class, a.basis, a.confidence) == ("CELLULAR", "go_bp", "HIGH")


def test_two_high_go_bp_classes_flag_a_debundle_candidate(seed):
    a = classify_node({"name": "N", **bp(CELL, GENOME)}, seed)
    assert a.node_class == CONFLICT
    assert a.is_conflict
    assert a.detail == "CELLULAR + GENOMIC"


def test_low_confidence_seed_terms_do_not_classify(seed):
    """A LOW term suggests; it must not seed on its own."""
    a = classify_node({"name": "N", **bp(SOFT)}, seed)
    assert a.node_class is None
    assert a.basis == "none"


def test_two_go_bp_terms_of_the_same_class_are_not_a_conflict(seed):
    a = classify_node({"name": "N", **bp(CELL, "GO:0006914")}, seed)
    assert a.node_class == "CELLULAR"


@pytest.mark.parametrize(
    "node, expected_class, expected_basis, expected_confidence",
    [
        ({"molecular_functions": [{"term": {"id": "GO:0004672"}}]}, "ACTIVITY", "go_mf", "HIGH"),
        ({"chemical_entities": [{"term": {"id": "CHEBI:15377"}}]}, "SUBSTANCE", "chebi", "MEDIUM"),
        ({"genes": [{"term": {"id": "hgnc:1"}}]}, "GENOMIC", "gene", "LOW"),
        ({"locations": [{"term": {"id": "UBERON:0002107"}}]}, "TISSUE", "uberon", "LOW"),
        ({"cell_types": [{"term": {"id": "CL:0000540"}}]}, "CELLULAR", "cl", "LOW"),
    ],
)
def test_fallback_rules_and_their_confidences(
    seed, node, expected_class, expected_basis, expected_confidence
):
    a = classify_node({"name": "N", **node}, seed)
    assert a.node_class == expected_class
    assert a.basis == expected_basis
    assert a.confidence == expected_confidence


def test_go_bp_wins_over_every_fallback(seed):
    a = classify_node(
        {
            "name": "N",
            **bp(CELL),
            "molecular_functions": [{"term": {"id": "GO:0004672"}}],
            "genes": [{"term": {"id": "hgnc:1"}}],
        },
        seed,
    )
    assert (a.node_class, a.basis) == ("CELLULAR", "go_bp")


def test_uberon_yields_tissue_only_without_a_cell_type(seed):
    """UBERON alongside CL is a located cell, not a tissue-tier claim."""
    node = {
        "name": "N",
        "locations": [{"term": {"id": "UBERON:0002107"}}],
        "cell_types": [{"term": {"id": "CL:0000540"}}],
    }
    assert classify_node(node, seed).node_class == "CELLULAR"


def test_node_with_no_grounding_is_left_unclassified(seed):
    a = classify_node({"name": "N", "description": "prose only"}, seed)
    assert a.node_class is None and a.confidence == "NONE"


def test_scan_reads_a_kb_directory(tmp_path):
    kb = tmp_path / "disorders"
    kb.mkdir()
    (kb / "Demo.yaml").write_text(
        "pathophysiology:\n"
        "- name: Apoptotic Node\n"
        "  biological_processes:\n"
        f"  - term: {{id: {CELL}}}\n"
        "- name: Bare Node\n",
        encoding="utf-8",
    )
    result = scan([kb], SEED)
    assert [a.node for a in result.assignments] == ["Apoptotic Node", "Bare Node"]
    assert result.index[("Demo", "Apoptotic Node")].node_class == "CELLULAR"
    s = summarize(result)
    assert s["total"] == 2 and s["classified"] == 1 and s["unclassified"] == 1


def _pair(disorder_class, disorder_conf, module_class, module_conf):
    """Build a minimal ScanResult holding one conforms_to pair."""
    src = Assignment("Dis", "D node", disorder_class, "go_bp", disorder_conf)
    tgt = Assignment("mod", "M node", module_class, "go_bp", module_conf)
    r = ScanResult(
        assignments=[src, tgt],
        index={("Dis", "D node"): src, ("mod", "M node"): tgt},
        conforms_to={("Dis", "D node"): "mod#M node"},
    )
    return r


def test_conformance_reports_a_mismatched_pair():
    rows = conformance_mismatches(_pair("ACTIVITY", "HIGH", "CELLULAR", "HIGH"))
    assert len(rows) == 1
    assignment, ref, module_class, disorder_class = rows[0]
    assert (disorder_class, module_class) == ("ACTIVITY", "CELLULAR")
    assert ref == "mod#M node"
    assert assignment.disease == "Dis"


def test_conformance_ignores_matching_pairs():
    assert conformance_mismatches(_pair("CELLULAR", "HIGH", "CELLULAR", "HIGH")) == []


def test_conformance_gate_excludes_low_confidence_sides():
    r = _pair("ACTIVITY", "LOW", "CELLULAR", "HIGH")
    assert conformance_mismatches(r) == []
    assert len(conformance_mismatches(r, high_only=False)) == 1
    assert len(conformance_pairs(r, high_only=False)) == 1
    assert conformance_pairs(r) == []


def test_conformance_skips_conflicts_and_unresolvable_targets():
    assert conformance_mismatches(_pair(CONFLICT, "HIGH", "CELLULAR", "HIGH")) == []
    r = _pair("ACTIVITY", "HIGH", "CELLULAR", "HIGH")
    r.conforms_to[("Dis", "D node")] = "no_such_module#Missing"
    assert conformance_mismatches(r) == []


# --- the committed seed table --------------------------------------------------


def test_committed_seed_table_is_well_formed(seed):
    assert len(seed) > 600
    classes = {c for c, _ in seed.values()}
    assert classes <= {
        "GENOMIC", "ACTIVITY", "SUBSTANCE", "PATHWAY",
        "CELLULAR", "TISSUE", "SYSTEMIC", "OUTCOME",
    }
    assert {q for _, q in seed.values()} == {"HIGH", "LOW"}
    assert all(k.startswith("GO:") for k in seed)


def test_seed_table_has_no_duplicate_terms():
    ids = [
        line.split("\t")[0]
        for line in SEED.read_text(encoding="utf-8").splitlines()
        if line and not line.startswith(("#", "go_id"))
    ]
    assert len(ids) == len(set(ids))
