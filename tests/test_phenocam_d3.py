from pathlib import Path
import pytest

DISEASES_DIR = Path(__file__).parent.parent / "causal_models" / "diseases"
GORLIN = DISEASES_DIR / "Gorlin_Syndrome.yaml"


def test_build_data_returns_required_keys():
    from scripts.phenocam_d3 import build_data
    data = build_data(GORLIN)
    for key in ["disease_name", "disease_id", "disease_term", "nodes", "edges",
                "hypothesis_groups", "phenotype_routes", "phenotype_disease_edges", "disease_node"]:
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


def test_build_nodes_maps_molecular_activity():
    from scripts.phenocam_d3 import _load_modules, _collect_nodes, _build_nodes
    import yaml
    disease = yaml.safe_load(GORLIN.read_text())
    modules = _load_modules(disease)
    catalog = _collect_nodes(disease, modules)
    nodes = _build_nodes(catalog)
    node_map = {n["id"]: n for n in nodes}

    # Module molecular activity
    n = node_map["ptch1_inhibition"]
    assert n["type"] == "activity"
    assert n["node_kind"] == "molecular_activities"
    assert n["module_id"] == "hedgehog_signaling"
    assert "PTCH1" in n["label"]


def test_build_nodes_maps_variant():
    from scripts.phenocam_d3 import _load_modules, _collect_nodes, _build_nodes
    import yaml
    disease = yaml.safe_load(GORLIN.read_text())
    modules = _load_modules(disease)
    catalog = _collect_nodes(disease, modules)
    nodes = _build_nodes(catalog)
    node_map = {n["id"]: n for n in nodes}

    n = node_map["ptch1_lof"]
    assert n["type"] == "local_activity"
    assert n["node_kind"] == "variants"
    assert n["quality"] == "LOSS_OF_FUNCTION"
    assert "PTCH1" in n["label"]


def test_build_nodes_excludes_phenotypes():
    from scripts.phenocam_d3 import _load_modules, _collect_nodes, _build_nodes
    import yaml
    disease = yaml.safe_load(GORLIN.read_text())
    modules = _load_modules(disease)
    catalog = _collect_nodes(disease, modules)
    nodes = _build_nodes(catalog)
    ids = {n["id"] for n in nodes}
    assert "bcc" not in ids
    assert "medulloblastoma" not in ids


def test_build_edges_causal_relations():
    from scripts.phenocam_d3 import _load_modules, _collect_nodes, _build_edges
    import yaml
    disease = yaml.safe_load(GORLIN.read_text())
    modules = _load_modules(disease)
    catalog = _collect_nodes(disease, modules)
    edges = _build_edges(disease, catalog)
    edge_map = {(e["source"], e["target"]): e for e in edges}

    # Cross-module edge: ptch1_lof (disease-local) → ptch1_inhibition (module node)
    e = edge_map[("ptch1_lof", "ptch1_inhibition")]
    assert e["relation_id"] == "RO:0002411"
    assert "ptch1_driven" in e["hypothesis_ids"]
    assert e["edge_context"] == "cross_module"

    # Module-internal edge (from hedgehog_signaling module causal_relations)
    # Both source and target are module nodes — first module edge
    e = edge_map.get(("ptch1_inhibition", "smo_activity"))
    assert e is not None
    assert e["edge_context"] == "module_internal"


def test_build_edges_skips_unresolved():
    from scripts.phenocam_d3 import _load_modules, _collect_nodes, _build_edges, PHENOTYPE_COLLECTION
    import yaml
    disease = yaml.safe_load(GORLIN.read_text())
    modules = _load_modules(disease)
    catalog = _collect_nodes(disease, modules)
    edges = _build_edges(disease, catalog, modules)
    ids = set(catalog.keys())
    pheno_ids = {f"pheno:{nid}" for nid, e in catalog.items() if e["collection"] == PHENOTYPE_COLLECTION}
    valid_targets = ids | pheno_ids
    for e in edges:
        assert e["source"] in ids, f"Unresolved source: {e['source']}"
        assert e["target"] in valid_targets, f"Unresolved target: {e['target']}"


def test_hypothesis_groups_have_states():
    from scripts.phenocam_d3 import _load_modules, _collect_nodes, _assign_hg_colors, _build_hypothesis_groups
    import yaml
    disease = yaml.safe_load(GORLIN.read_text())
    modules = _load_modules(disease)
    catalog = _collect_nodes(disease, modules)
    colors = _assign_hg_colors(disease)
    groups = _build_hypothesis_groups(disease, catalog, colors)
    group_map = {g["id"]: g for g in groups}

    # ptch1_driven hypothesis
    ptch1 = group_map["ptch1_driven"]
    assert ptch1["name"] == "PTCH1-driven"
    assert "~85%" in ptch1["frequency"]

    # ptch1_lof variant should be primary in ptch1_driven
    states = ptch1["states"]
    assert "ptch1_lof" in states
    assert states["ptch1_lof"]["is_primary"] is True
    assert states["ptch1_lof"]["state"] == "decreased"  # LOF → decreased


def test_hypothesis_colors_assigned():
    from scripts.phenocam_d3 import _assign_hg_colors
    import yaml
    disease = yaml.safe_load(GORLIN.read_text())
    colors = _assign_hg_colors(disease)
    assert "ptch1_driven" in colors
    assert "sufu_driven" in colors
    assert colors["ptch1_driven"].startswith("#")


def test_phenotype_nodes():
    from scripts.phenocam_d3 import _build_phenotype_nodes
    import yaml
    disease = yaml.safe_load(GORLIN.read_text())
    phenos = _build_phenotype_nodes(disease)
    ids = {p["id"] for p in phenos}
    assert "bcc" in ids
    assert "medulloblastoma" in ids
    bcc = next(p for p in phenos if p["id"] == "bcc")
    assert bcc["phenotype_id"] == "HP:0002671"
    assert "Basal cell carcinoma" in bcc["phenotype_label"]
    # bcc and medulloblastoma have causal chains — not unrouted
    assert bcc["unrouted"] is False
    assert next(p for p in phenos if p["id"] == "medulloblastoma")["unrouted"] is False
    # falx_calcification has no causal chain — unrouted
    assert next(p for p in phenos if p["id"] == "falx_calcification")["unrouted"] is True
    assert next(p for p in phenos if p["id"] == "macrocephaly")["unrouted"] is True


def test_phenotype_edges():
    from scripts.phenocam_d3 import _build_phenotype_edges, _build_disease_node
    import yaml
    disease = yaml.safe_load(GORLIN.read_text())
    edges = _build_phenotype_edges(disease)
    dn = _build_disease_node(disease)
    assert dn["term_id"] == "MONDO:0007187"
    bcc_edge = next((e for e in edges if e["source"] == "pheno:bcc"), None)
    assert bcc_edge is not None
    assert bcc_edge["target"] == "disease:gorlin_syndrome"


def test_modules_meta():
    from scripts.phenocam_d3 import _load_modules, _build_modules_meta
    import yaml
    disease = yaml.safe_load(GORLIN.read_text())
    modules = _load_modules(disease)
    meta = _build_modules_meta(disease, modules)
    assert len(meta) == 1
    assert meta[0]["id"] == "hedgehog_signaling"


def test_render_html_produces_valid_html():
    from scripts.phenocam_d3 import build_data, render_html
    data = build_data(GORLIN)
    html = render_html(data)
    assert html.startswith("<!DOCTYPE html")
    assert "__DATA__" not in html
    assert "Gorlin Syndrome" in html
    assert "d3" in html.lower()
    assert "dagre" in html.lower()
    assert len(html) > 10_000


def test_render_html_node_count():
    from scripts.phenocam_d3 import build_data
    data = build_data(GORLIN)
    assert len(data["nodes"]) >= 5
    assert len(data["edges"]) >= 3
    assert len(data["phenotype_routes"]) >= 4


def test_hedgehog_module_has_full_node_set():
    """Module must contain all 15 nodes present in V1 hand-crafted DATA."""
    from scripts.phenocam_d3 import _load_modules, _collect_nodes
    import yaml
    disease = yaml.safe_load(
        (Path(__file__).parent.parent / "causal_models/diseases/Gorlin_Syndrome.yaml").read_text()
    )
    modules = _load_modules(disease)
    catalog = _collect_nodes(disease, modules)

    expected_module_nodes = {
        "ptch1_inhibition", "smo_activity", "sufu_sequestering_gli1", "gli1_activation",
        # Arm A
        "bbsome_transport", "iftb_transport", "gpr161_activity",
        "pka_activity", "gsk3b_kinase", "btrc_ubiquitination",
        # Arm B
        "sufu_sequestering_gli3", "gli3a_activation", "gli3r_production",
        # Arm C
        "mapk1_kinase", "dyrk2_kinase",
    }
    module_nodes = {nid for nid, e in catalog.items() if e["is_module"]}
    missing = expected_module_nodes - module_nodes
    assert not missing, f"Missing module nodes: {missing}"


def test_hedgehog_module_edge_count():
    """Module must have at least 13 intra-module causal edges."""
    from scripts.phenocam_d3 import _load_modules, _collect_nodes, _build_edges
    import yaml
    disease = yaml.safe_load(
        (Path(__file__).parent.parent / "causal_models/diseases/Gorlin_Syndrome.yaml").read_text()
    )
    modules = _load_modules(disease)
    catalog = _collect_nodes(disease, modules)
    edges = _build_edges(disease, catalog, modules)
    module_edges = [e for e in edges if e["edge_context"] == "module_internal"]
    assert len(module_edges) >= 13, f"Expected >=13 module-internal edges, got {len(module_edges)}"


def test_gorlin_has_bcl2_mycn_gli3_nodes():
    """Disease file must contain BCL2, MYCN, and GLI3 A/R imbalance nodes."""
    from scripts.phenocam_d3 import build_data
    from pathlib import Path
    data = build_data(Path("causal_models/diseases/Gorlin_Syndrome.yaml"))
    node_ids = {n["id"] for n in data["nodes"]}
    assert "bcl2_upregulation" in node_ids, "Missing bcl2_upregulation"
    assert "mycn_upregulation" in node_ids, "Missing mycn_upregulation"
    assert "gli3_ar_imbalance" in node_ids, "Missing gli3_ar_imbalance"


def test_gorlin_gli1_targets_edges():
    """GLI1 activation must have causal edges to BCL2, MYCN in disease file."""
    from scripts.phenocam_d3 import _load_modules, _collect_nodes, _build_edges
    import yaml
    from pathlib import Path
    disease = yaml.safe_load(
        (Path("causal_models/diseases/Gorlin_Syndrome.yaml")).read_text()
    )
    modules = _load_modules(disease)
    catalog = _collect_nodes(disease, modules)
    edges = _build_edges(disease, catalog, modules)
    edge_pairs = {(e["source"], e["target"]) for e in edges}
    assert ("gli1_activation", "bcl2_upregulation") in edge_pairs
    assert ("gli1_activation", "mycn_upregulation") in edge_pairs
    assert ("gli3a_activation", "gli3_ar_imbalance") in edge_pairs


def test_gorlin_has_all_v1_phenotypes():
    """Gorlin must expose all 11 phenotype routes present in V1."""
    from scripts.phenocam_d3 import build_data
    from pathlib import Path
    data = build_data(Path("causal_models/diseases/Gorlin_Syndrome.yaml"))
    pheno_ids = {p["id"] for p in data["phenotype_routes"]}
    expected = {
        "bcc", "odontogenic_keratocysts", "medulloblastoma",
        "macrocephaly", "palmar_pits", "falx_calcification",
        "plantar_pits", "abnormal_rib_morphology",
        "abnormal_vertebral_morphology", "cardiac_fibroma", "ovarian_fibroma",
    }
    missing = expected - pheno_ids
    assert not missing, f"Missing phenotype routes: {missing}"


def test_skeletal_phenotypes_are_routed():
    """Rib and vertebral morphology phenotypes must be routed (have incoming causal edges)."""
    from scripts.phenocam_d3 import build_data
    from pathlib import Path
    data = build_data(Path("causal_models/diseases/Gorlin_Syndrome.yaml"))
    pheno_map = {p["id"]: p for p in data["phenotype_routes"]}
    assert pheno_map["abnormal_rib_morphology"]["unrouted"] is False
    assert pheno_map["abnormal_vertebral_morphology"]["unrouted"] is False


def test_unrouted_phenotypes():
    """Plantar pits, cardiac/ovarian fibromas must be unrouted (no curated causal chain)."""
    from scripts.phenocam_d3 import build_data
    from pathlib import Path
    data = build_data(Path("causal_models/diseases/Gorlin_Syndrome.yaml"))
    pheno_map = {p["id"]: p for p in data["phenotype_routes"]}
    assert pheno_map["plantar_pits"]["unrouted"] is True
    assert pheno_map["cardiac_fibroma"]["unrouted"] is True
    assert pheno_map["ovarian_fibroma"]["unrouted"] is True


def test_v2_node_count_matches_v1():
    """V2 DATA must have >=19 nodes, >=11 phenotype routes, >=20 edges (matching V1)."""
    from scripts.phenocam_d3 import build_data
    from pathlib import Path
    data = build_data(Path("causal_models/diseases/Gorlin_Syndrome.yaml"))
    assert len(data["nodes"]) >= 19, f"Expected >=19 nodes, got {len(data['nodes'])}"
    assert len(data["phenotype_routes"]) >= 11, (
        f"Expected >=11 phenotype_routes, got {len(data['phenotype_routes'])}"
    )
    assert len(data["edges"]) >= 20, f"Expected >=20 edges, got {len(data['edges'])}"
