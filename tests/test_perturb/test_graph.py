"""Tests for causal graph extraction with perturbation enrichment."""

import yaml
from pathlib import Path

import pytest

from dismech.perturb.graph import (
    build_perturbation_graph,
    extract_causal_edges,
    PerturbationGraph,
    CausalEdgeEnriched,
    trace_causal_paths,
)


@pytest.fixture
def ckd_mbd_disorder():
    """Load CKD-MBD disorder YAML."""
    path = Path("kb/disorders/CKD-Mineral_Bone_Disorder.yaml")
    if not path.exists():
        pytest.skip("CKD-MBD YAML not found")
    with open(path) as f:
        return yaml.safe_load(f)


def test_build_perturbation_graph(ckd_mbd_disorder):
    """Test that we can build a perturbation graph from CKD-MBD YAML."""
    pg = build_perturbation_graph(ckd_mbd_disorder)
    assert isinstance(pg, PerturbationGraph)
    assert len(pg.causal_graph.nodes) > 0
    assert len(pg.genes) > 0
    assert any(g.name == "CASR" for g in pg.genes)
    assert len(pg.biochemical_mappings) > 0


def test_computational_models_extracted(ckd_mbd_disorder):
    """Test that computational models are extracted."""
    pg = build_perturbation_graph(ckd_mbd_disorder)
    assert len(pg.computational_models) > 0
    model = pg.computational_models[0]
    assert model["model_id"] == "BIOMD0000000613"


def test_gene_entries(ckd_mbd_disorder):
    """Test that genetic entries are extracted with HGNC IDs."""
    pg = build_perturbation_graph(ckd_mbd_disorder)
    casr = next((g for g in pg.genes if g.name == "CASR"), None)
    assert casr is not None
    assert casr.hgnc_id is None  # CKD-MBD genetic entries lack gene_term


def test_biochemical_mappings(ckd_mbd_disorder):
    """Test that biochemical mappings include LOINC/CHEBI terms."""
    pg = build_perturbation_graph(ckd_mbd_disorder)
    phosphate = next(
        (b for b in pg.biochemical_mappings if "Phosphate" in b.name), None
    )
    assert phosphate is not None
    assert len(phosphate.mappings) > 0


def test_extract_causal_edges_from_yaml(ckd_mbd_disorder):
    """Test that downstream edges are extracted from pathophysiology."""
    edges = extract_causal_edges(ckd_mbd_disorder)
    assert len(edges) > 0
    # Check a known edge: Phosphate Retention -> Secondary HPT
    phos_to_hpt = [
        e
        for e in edges
        if "Phosphate" in e.source and "Hyperparathyroidism" in e.target
    ]
    assert len(phos_to_hpt) == 1
    # Check edge from RANKL/OPG -> Decreased Bone Mineral Density
    rankl_to_bmd = [
        e for e in edges if "RANKL" in e.source and "Bone Mineral" in e.target
    ]
    assert len(rankl_to_bmd) == 1
    # All edges should have source and target
    for e in edges:
        assert e.source
        assert e.target
        assert e.mechanism


def test_extract_causal_edges_traceable(ckd_mbd_disorder):
    """Test that extracted edges can be used for causal chain tracing."""
    edges = extract_causal_edges(ckd_mbd_disorder)
    paths = trace_causal_paths("Phosphate Retention and FGF23 Axis", edges)
    assert len(paths) > 0
    # Should reach phenotype targets through multi-hop paths
    targets = {p[-1].target for p in paths}
    assert "Decreased Bone Mineral Density" in targets or any(
        "Bone" in t for t in targets
    )


# --- Causal chain tracer tests ---


def test_trace_simple_path():
    """Test tracing through a simple linear graph."""
    edges = [
        CausalEdgeEnriched("A", "B", "INCREASES", "mech1"),
        CausalEdgeEnriched("B", "C", "DECREASES", "mech1"),
        CausalEdgeEnriched("C", "D", "INCREASES", "mech2"),
    ]
    paths = trace_causal_paths("A", edges)
    assert len(paths) > 0
    longest = max(paths, key=len)
    assert len(longest) == 3


def test_trace_no_cycles():
    """Cycles should not cause infinite loops."""
    edges = [
        CausalEdgeEnriched("A", "B", "INCREASES", "mech1"),
        CausalEdgeEnriched("B", "A", "INCREASES", "mech1"),
    ]
    paths = trace_causal_paths("A", edges)
    assert len(paths) == 1


def test_trace_branching():
    """Test tracing through a branching graph."""
    edges = [
        CausalEdgeEnriched("A", "B", "INCREASES", "mech1"),
        CausalEdgeEnriched("A", "C", "DECREASES", "mech2"),
        CausalEdgeEnriched("B", "D", "INCREASES", "mech1"),
    ]
    paths = trace_causal_paths("A", edges)
    assert len(paths) == 3  # A->B, A->C, A->B->D
