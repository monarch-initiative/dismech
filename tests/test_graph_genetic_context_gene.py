"""A pathophysiology node's `genetic_context.gene` wires genetic records (#11999)."""

from __future__ import annotations

from dismech.export.cx2_export import disorder_to_cx2
from dismech.graph import build_causal_graph
from dismech.qc_plugins import gene_mechanism_wiring_coverage

DOCK2 = {"preferred_term": "DOCK2", "term": {"id": "hgnc:2988", "label": "DOCK2"}}
MEF2C_AS1 = {
    "preferred_term": "MEF2C-AS1",
    "term": {"id": "hgnc:48908", "label": "MEF2C-AS1"},
}


def _dock2_disorder() -> dict:
    """Shape of kb/disorders/DOCK2_Deficiency.yaml: gene only under genetic_context."""
    return {
        "name": "DOCK2 Deficiency",
        "pathophysiology": [
            {
                "name": "DOCK2 Loss of Function",
                "genetic_context": {
                    "gene": DOCK2,
                    "variant_origin": "GERMLINE",
                    "functional_impact_category": "LOSS_OF_FUNCTION",
                },
            }
        ],
        "genetic": [
            {"name": "DOCK2", "relationship_type": "CAUSATIVE", "gene_term": DOCK2}
        ],
    }


def _contributes_to(disorder: dict) -> set[tuple[str, str]]:
    return {
        (edge.source, edge.target)
        for edge in build_causal_graph(disorder).edges
        if edge.predicate == "contributes_to"
    }


def test_genetic_record_wires_to_node_recording_gene_under_genetic_context() -> None:
    assert ("DOCK2", "DOCK2 Loss of Function") in _contributes_to(_dock2_disorder())


def test_genetic_context_genes_list_is_also_read() -> None:
    disorder = _dock2_disorder()
    context = disorder["pathophysiology"][0]["genetic_context"]
    context["genes"] = [context.pop("gene")]

    assert ("DOCK2", "DOCK2 Loss of Function") in _contributes_to(disorder)


def test_mechanism_outlink_counts_a_genetic_context_node_as_wired() -> None:
    assert gene_mechanism_wiring_coverage(_dock2_disorder()) == (1, 1, [])


def test_noncontributing_record_still_gets_no_edge() -> None:
    disorder = _dock2_disorder()
    disorder["genetic"][0]["relationship_type"] = "UNKNOWN"

    assert _contributes_to(disorder) == set()


def test_cx2_export_matches_the_pathograph() -> None:
    cx2 = disorder_to_cx2(_dock2_disorder())
    aspects = {key: value for aspect in cx2 for key, value in aspect.items()}
    names = {node["id"]: node["v"]["name"] for node in aspects["nodes"]}
    endpoints = {(names[edge["s"]], names[edge["t"]]) for edge in aspects["edges"]}

    assert ("DOCK2", "DOCK2 Loss of Function") in endpoints


def test_variant_does_not_match_every_same_gene_genetic_context_node() -> None:
    """A variant is one event; genetic_context usually names one lesion.

    Mirrors kb/disorders/MEF2C-Related_Disorder.yaml, where two breakpoint
    nodes share MEF2C-AS1 and each variant belongs to only one of them.
    Matching the variant by gene alone would wire each to both.
    """
    disorder = {
        "name": "Example",
        "pathophysiology": [
            {"name": "Breakpoint A", "genetic_context": {"gene": MEF2C_AS1}},
            {"name": "Breakpoint B", "genetic_context": {"gene": MEF2C_AS1}},
        ],
        "variants": [{"name": "Rearrangement A", "gene": MEF2C_AS1}],
    }

    assert _contributes_to(disorder) == set()
