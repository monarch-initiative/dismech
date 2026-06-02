from pathlib import Path
import pytest

DISEASES_DIR = Path(__file__).parent.parent / "causal_models" / "diseases"
GORLIN = DISEASES_DIR / "Gorlin_Syndrome.yaml"


def test_build_data_returns_required_keys():
    from scripts.phenocam_d3 import build_data
    data = build_data(GORLIN)
    for key in ["disease_name", "disease_id", "disease_term", "nodes", "edges",
                "hypothesis_groups", "phenotype_nodes", "phenotype_disease_edges", "disease_node"]:
        assert key in data, f"Missing key: {key}"
