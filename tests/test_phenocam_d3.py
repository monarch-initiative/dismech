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


def test_collect_nodes_includes_disease_and_module_nodes():
    from scripts.phenocam_d3 import _load_modules, _collect_nodes
    import yaml
    disease = yaml.safe_load(GORLIN.read_text())
    modules = _load_modules(disease)
    catalog = _collect_nodes(disease, modules)

    # Disease-local nodes
    assert "ptch1_lof" in catalog
    assert catalog["ptch1_lof"]["collection"] == "variants"
    assert catalog["ptch1_lof"]["is_module"] is False

    # Module nodes (from hedgehog_signaling)
    assert "ptch1_inhibition" in catalog
    assert catalog["ptch1_inhibition"]["is_module"] is True
    assert catalog["ptch1_inhibition"]["module_id"] == "hedgehog_signaling"

def test_collect_nodes_includes_phenotypes():
    from scripts.phenocam_d3 import _load_modules, _collect_nodes
    import yaml
    disease = yaml.safe_load(GORLIN.read_text())
    modules = _load_modules(disease)
    catalog = _collect_nodes(disease, modules)
    assert "bcc" in catalog
    assert catalog["bcc"]["collection"] == "phenotypes"
