"""Regulatory target links must not imply that an SV alters the target sequence."""

import json

import pytest

from dismech.graph import build_causal_graph, graph_to_json


@pytest.mark.parametrize(
    ("target_symbol", "target_id", "sequence_symbol"),
    [
        ("ID4", "hgnc:5363", None),
        ("LMNB1", "hgnc:6637", "LMNB1"),
        ("SHH", "hgnc:10848", "LMBR1"),
    ],
)
def test_explicit_target_separates_regulation_from_sequence_gene(
    target_symbol: str, target_id: str, sequence_symbol: str | None
) -> None:
    target = {
        "preferred_term": target_symbol,
        "term": {"id": target_id, "label": target_symbol},
    }
    variant = {"name": "Regulatory SV", "regulatory_target_gene": target}
    if sequence_symbol:
        variant["gene"] = {"preferred_term": sequence_symbol}
    genetic = [{"name": target_symbol, "gene_term": target, "variants": [variant]}]
    if sequence_symbol and sequence_symbol != target_symbol:
        genetic.append({"name": sequence_symbol})
    disorder = {"name": "Regulatory example", "genetic": genetic}

    graph = build_causal_graph(disorder)
    edges = {(edge.source, edge.target, edge.predicate) for edge in graph.edges}
    expected = {("Regulatory SV", target_symbol, "has_regulatory_target")}
    if sequence_symbol:
        expected.add(("Regulatory SV", sequence_symbol, "variant_of"))
    assert edges == expected
    assert not graph.integrity_issues

    payload = json.loads(graph_to_json(graph, disorder))
    meta = next(n["meta"] for n in payload["nodes"] if n["id"] == "Regulatory SV")
    target_term = {"label": target_symbol, "id": target_id}
    assert meta["regulatory_target_gene"] == target_term
    assert target_term in meta["gene_terms"]


def test_regulatory_target_falls_back_to_matching_mechanism() -> None:
    disorder = {
        "name": "Regulatory example",
        "variants": [
            {
                "name": "Regulatory SV",
                "regulatory_target_gene": {"preferred_term": "ID4"},
            }
        ],
        "pathophysiology": [
            {"name": "Proposed ID4 misexpression", "gene": {"preferred_term": "ID4"}}
        ],
    }

    graph = build_causal_graph(disorder)

    assert {(e.source, e.target, e.predicate) for e in graph.edges} == {
        ("Regulatory SV", "Proposed ID4 misexpression", "contributes_to")
    }


def test_unresolved_regulatory_target_does_not_imply_parent_overlap() -> None:
    disorder = {
        "name": "Regulatory example",
        "genetic": [
            {
                "name": "Other locus",
                "variants": [
                    {
                        "name": "Regulatory SV",
                        "regulatory_target_gene": {"preferred_term": "ID4"},
                    }
                ],
            }
        ],
    }

    assert not build_causal_graph(disorder).edges


def test_legacy_gene_nesting_keeps_variant_of() -> None:
    disorder = {
        "name": "Legacy example",
        "genetic": [{"name": "CFTR", "variants": [{"name": "Legacy allele"}]}],
    }

    graph = build_causal_graph(disorder)

    assert {(e.source, e.target, e.predicate) for e in graph.edges} == {
        ("Legacy allele", "CFTR", "variant_of")
    }
