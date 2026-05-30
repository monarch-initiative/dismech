"""Tests for model metadata in pathograph JSON."""

import json

from dismech.graph import (
    _genetic_item_infers_mechanism_edges,
    build_causal_graph,
    graph_to_json,
)


def test_genetic_item_infers_mechanism_edges_respects_relationship_type() -> None:
    assert _genetic_item_infers_mechanism_edges({"relationship_type": "CAUSATIVE"})
    assert _genetic_item_infers_mechanism_edges({"association": "Risk factor"})

    assert not _genetic_item_infers_mechanism_edges({"relationship_type": "MODIFIER"})
    assert not _genetic_item_infers_mechanism_edges({"association": "Disease modifier"})
    assert not _genetic_item_infers_mechanism_edges({"relationship_type": "PROTECTIVE"})


def test_graph_to_json_includes_experimental_and_computational_model_links() -> None:
    """Pathophysiology nodes should expose linked model metadata in graph JSON."""
    disorder = {
        "name": "Example Disease",
        "pathophysiology": [
            {
                "name": "CFTR Dysfunction",
                "downstream": [{"target": "Bronchiectasis"}],
            }
        ],
        "phenotypes": [{"name": "Bronchiectasis"}],
        "experimental_models": [
            {
                "name": "Patient-derived airway organoid",
                "experimental_model_type": "ORGANOID",
                "namo_type": "namo:Organoid",
                "modeled_mechanisms": [
                    {
                        "target": "CFTR Dysfunction",
                        "description": "Assays epithelial CFTR rescue in patient-derived tissue.",
                    }
                ],
            }
        ],
        "computational_models": [
            {
                "name": "Airway signaling simulator",
                "model_type": "MECHANISTIC_NETWORK",
                "model_software": "PySB",
                "model_format": "Python",
                "modeled_mechanisms": [
                    {
                        "target": "CFTR Dysfunction",
                        "description": "Encodes CFTR-dependent signaling states for in silico perturbation.",
                    }
                ],
            }
        ],
    }

    graph = build_causal_graph(disorder)
    data = json.loads(graph_to_json(graph, disorder))
    node = next(node for node in data["nodes"] if node["id"] == "CFTR Dysfunction")

    assert node["meta"]["experimental_models"] == [
        {
            "name": "Patient-derived airway organoid",
            "model_type": "ORGANOID",
            "namo_type": "namo:Organoid",
            "description": "Assays epithelial CFTR rescue in patient-derived tissue.",
        }
    ]
    assert node["meta"]["computational_models"] == [
        {
            "name": "Airway signaling simulator",
            "model_type": "MECHANISTIC_NETWORK",
            "model_software": "PySB",
            "model_format": "Python",
            "description": "Encodes CFTR-dependent signaling states for in silico perturbation.",
        }
    ]


def test_build_causal_graph_includes_linked_models_treatments_and_genetics() -> None:
    """Linked non-causal content should now participate in the pathograph."""
    disorder = {
        "name": "Example Disease",
        "pathophysiology": [
            {
                "name": "CFTR Dysfunction",
                "gene": {
                    "preferred_term": "CFTR",
                    "term": {"id": "hgnc:1884", "label": "CFTR"},
                },
                "downstream": [{"target": "Bronchiectasis"}],
            }
        ],
        "phenotypes": [
            {
                "name": "Bronchiectasis",
                "phenotype_term": {
                    "preferred_term": "Bronchiectasis",
                    "term": {"id": "HP:0002110", "label": "Bronchiectasis"},
                },
            }
        ],
        "genetic": [
            {
                "name": "CFTR",
                "association": "Causative",
                "variants": [{"name": "F508del"}],
            },
            {
                "name": "CFTR modifier locus",
                "association": "Disease modifier",
                "gene_term": {
                    "preferred_term": "CFTR",
                    "term": {"id": "hgnc:1884", "label": "CFTR"},
                },
            },
        ],
        "treatments": [
            {
                "name": "Ivacaftor",
                "target_mechanisms": [{"target": "CFTR Dysfunction"}],
                "target_phenotypes": [
                    {
                        "preferred_term": "Bronchiectasis",
                        "term": {"id": "HP:0002110", "label": "Bronchiectasis"},
                    }
                ],
            }
        ],
        "experimental_models": [
            {
                "name": "Patient-derived airway organoid",
                "experimental_model_type": "ORGANOID",
                "modeled_mechanisms": [{"target": "CFTR Dysfunction"}],
            }
        ],
        "computational_models": [
            {
                "name": "CFTR network model",
                "model_type": "MECHANISTIC_NETWORK",
                "modeled_mechanisms": [{"target": "CFTR Dysfunction"}],
            }
        ],
    }

    graph = build_causal_graph(disorder)
    edges = {(edge.source, edge.target, edge.predicate) for edge in graph.edges}

    assert ("Patient-derived airway organoid", "CFTR Dysfunction", "models") in edges
    assert ("CFTR network model", "CFTR Dysfunction", "models") in edges
    assert ("Ivacaftor", "CFTR Dysfunction", "targets") in edges
    assert ("Ivacaftor", "Bronchiectasis", "treats") in edges
    assert ("CFTR", "CFTR Dysfunction", "contributes_to") in edges
    assert ("CFTR modifier locus", "CFTR Dysfunction", "contributes_to") not in edges
    assert ("F508del", "CFTR", "variant_of") in edges

    data = json.loads(graph_to_json(graph, disorder))
    node_types = {node["id"]: node["node_type"] for node in data["nodes"]}
    assert node_types["Patient-derived airway organoid"] == "experimental_model"
    assert node_types["CFTR network model"] == "computational_model"
    assert node_types["Ivacaftor"] == "treatment"
    assert node_types["CFTR"] == "genetic"
    assert node_types["F508del"] == "genetic"


def test_build_causal_graph_includes_biomarker_readout_links() -> None:
    """Biochemical marker readouts should add observational pathograph edges."""
    disorder = {
        "name": "Example Disease",
        "pathophysiology": [
            {
                "name": "Membrane Injury",
                "downstream": [{"target": "Muscle Weakness"}],
            }
        ],
        "phenotypes": [{"name": "Muscle Weakness"}],
        "biochemical": [
            {
                "name": "Creatine Kinase",
                "presence": "Elevated",
                "biomarker_term": {
                    "preferred_term": "creatine kinase measurement",
                    "term": {
                        "id": "NCIT:C64489",
                        "label": "Creatine Kinase Measurement",
                    },
                },
                "readouts": [
                    {
                        "target": "Membrane Injury",
                        "relationship": "READOUT_OF",
                        "direction": "POSITIVE",
                        "endpoint_context": "MONITORING",
                        "regulatory_endpoint_refs": ["FDA-SE-test-001"],
                        "interpretation": "Higher CK reflects greater membrane injury.",
                    }
                ],
            }
        ],
    }

    graph = build_causal_graph(disorder)
    edges = {(edge.source, edge.target, edge.predicate) for edge in graph.edges}

    assert ("Membrane Injury", "Creatine Kinase", "readout") in edges

    data = json.loads(graph_to_json(graph, disorder))
    edge = next(
        edge
        for edge in data["edges"]
        if edge["source"] == "Membrane Injury" and edge["target"] == "Creatine Kinase"
    )
    assert edge["predicate"] == "readout"
    assert edge["relationship"] == "READOUT_OF"
    assert edge["direction"] == "POSITIVE"
    assert edge["endpoint_context"] == "MONITORING"

    node = next(node for node in data["nodes"] if node["id"] == "Creatine Kinase")
    assert node["node_type"] == "biochemical"
    assert node["meta"]["presence"] == "Elevated"
    assert node["meta"]["readouts"] == [
        {
            "target": "Membrane Injury",
            "relationship": "READOUT_OF",
            "direction": "POSITIVE",
            "endpoint_context": "MONITORING",
            "regulatory_endpoint_refs": ["FDA-SE-test-001"],
            "interpretation": "Higher CK reflects greater membrane injury.",
        }
    ]


def test_graph_to_json_includes_hypothesis_group_edge_metadata() -> None:
    """Pathograph edges should preserve curated hypothesis group links."""
    disorder = {
        "name": "Example Disease",
        "pathophysiology": [
            {
                "name": "Upstream mechanism",
                "downstream": [
                    {
                        "target": "Downstream mechanism",
                        "description": "Mechanistic bridge.",
                        "hypothesis_groups": ["canonical_model"],
                        "causal_link_type": "INDIRECT_KNOWN_INTERMEDIATES",
                        "intermediate_mechanisms": ["Intermediate step"],
                    }
                ],
            },
            {"name": "Downstream mechanism"},
        ],
    }

    graph = build_causal_graph(disorder)
    data = json.loads(graph_to_json(graph, disorder))
    edge = next(
        edge
        for edge in data["edges"]
        if edge["source"] == "Upstream mechanism"
        and edge["target"] == "Downstream mechanism"
    )

    assert edge["description"] == "Mechanistic bridge."
    assert edge["hypothesis_groups"] == ["canonical_model"]
    assert edge["causal_link_type"] == "INDIRECT_KNOWN_INTERMEDIATES"
    assert edge["intermediate_mechanisms"] == ["Intermediate step"]


def test_graph_to_json_includes_matching_histopathology_terms() -> None:
    """Matching pathograph nodes should expose NCIT-backed histopathology metadata."""
    disorder = {
        "name": "Example Disease",
        "pathophysiology": [
            {
                "name": "Desmoplastic Stroma",
                "downstream": [{"target": "CAF-Mediated T Cell Exclusion"}],
            }
        ],
        "phenotypes": [{"name": "CAF-Mediated T Cell Exclusion"}],
        "histopathology": [
            {
                "name": "Desmoplastic Stroma",
                "finding_term": {
                    "preferred_term": "Desmoplastic Stroma",
                    "term": {
                        "id": "NCIT:C36178",
                        "label": "Fibrotic Stroma Formation",
                    },
                },
            }
        ],
    }

    graph = build_causal_graph(disorder)
    data = json.loads(graph_to_json(graph, disorder))
    node = next(node for node in data["nodes"] if node["id"] == "Desmoplastic Stroma")

    assert node["meta"]["histopathology_terms"] == [
        {
            "name": "Desmoplastic Stroma",
            "preferred_term": "Desmoplastic Stroma",
            "term_id": "NCIT:C36178",
            "term_label": "Fibrotic Stroma Formation",
        }
    ]
