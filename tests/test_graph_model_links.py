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
