"""Tests for experimental-model metadata in pathograph JSON."""

import json

from dismech.graph import build_causal_graph, graph_to_json


def test_graph_to_json_includes_experimental_model_links() -> None:
    """Pathophysiology nodes should expose linked experimental models in graph JSON."""
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
            }
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
    }

    graph = build_causal_graph(disorder)
    edges = {(edge.source, edge.target, edge.predicate) for edge in graph.edges}

    assert ("Patient-derived airway organoid", "CFTR Dysfunction", "models") in edges
    assert ("Ivacaftor", "CFTR Dysfunction", "targets") in edges
    assert ("Ivacaftor", "Bronchiectasis", "treats") in edges
    assert ("CFTR", "CFTR Dysfunction", "contributes_to") in edges
    assert ("F508del", "CFTR", "variant_of") in edges

    data = json.loads(graph_to_json(graph, disorder))
    node_types = {node["id"]: node["node_type"] for node in data["nodes"]}
    assert node_types["Patient-derived airway organoid"] == "experimental_model"
    assert node_types["Ivacaftor"] == "treatment"
    assert node_types["CFTR"] == "genetic"
    assert node_types["F508del"] == "genetic"
