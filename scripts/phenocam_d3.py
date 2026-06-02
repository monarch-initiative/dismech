#!/usr/bin/env python3
"""Generate D3+dagre interactive HTML from a PhenoCAM V2 DiseaseCourse YAML.

Usage:
    uv run python scripts/phenocam_d3.py causal_models/diseases/Gorlin_Syndrome.yaml
    uv run python scripts/phenocam_d3.py --all
"""
import argparse
import json
from pathlib import Path
import yaml

MODULES_DIR = Path(__file__).parent.parent / "causal_models" / "modules"
DISEASES_DIR = Path(__file__).parent.parent / "causal_models" / "diseases"
VIZ_DIR = Path(__file__).parent.parent / "causal_models" / "viz"
TEMPLATE = Path(__file__).parent / "phenocam_d3_template.html"

QUALITY_STATE = {
    "INCREASED":        "increased",
    "DECREASED":        "decreased",
    "ABSENT":           "absent",
    "GAIN_OF_FUNCTION": "constitutively_active",
    "LOSS_OF_FUNCTION": "decreased",
}

RO_LABELS = {
    "RO:0002411": "causally upstream of",
    "RO:0002410": "causally related to",
    "RO:0002630": "directly negatively regulates",
    "RO:0002629": "directly positively regulates",
    "RO:0002200": "has phenotype",
}

HG_PALETTE = ["#0d6efd", "#198754", "#dc3545", "#fd7e14", "#6f42c1", "#20c997"]

NODE_TYPE_MAP = {
    "molecular_activities":   "activity",
    "variants":               "local_activity",
    "chemical_exposures":     "local_activity",
    "environmental_factors":  "local_activity",
    "molecular_entities":     "entity",
    "cellular_processes":     "process",
    "tissue_processes":       "tissue",
    "modulators":             "modulator",
}

NODE_COLLECTIONS = list(NODE_TYPE_MAP.keys())
PHENOTYPE_COLLECTION = "phenotypes"


def build_data(disease_path: Path) -> dict:
    disease = yaml.safe_load(disease_path.read_text())
    modules = _load_modules(disease)
    all_node_catalog = _collect_nodes(disease, modules)
    data_nodes = _build_nodes(all_node_catalog)
    data_edges = _build_edges(disease, all_node_catalog)
    hg_colors = _assign_hg_colors(disease)
    hg_groups = _build_hypothesis_groups(disease, all_node_catalog, hg_colors)
    pheno_nodes = _build_phenotype_nodes(disease)
    pheno_edges = _build_phenotype_edges(disease)
    disease_node = _build_disease_node(disease)
    modules_meta = _build_modules_meta(disease, modules)
    return {
        "disease_name": disease.get("name", ""),
        "disease_id": disease.get("id", ""),
        "disease_term": disease.get("realises_disease", {}),
        "modules": modules_meta,
        "nodes": data_nodes,
        "edges": data_edges,
        "hypothesis_groups": hg_groups,
        "hypothesis_colors": hg_colors,
        "phenotype_nodes": pheno_nodes,
        "phenotype_disease_edges": pheno_edges,
        "disease_node": disease_node,
    }


def render_html(data: dict) -> str:
    template = TEMPLATE.read_text()
    data_json = json.dumps(data, ensure_ascii=False, indent=2)
    return template.replace("__DATA__", data_json, 1)


def main():
    parser = argparse.ArgumentParser(description="Generate D3+dagre HTML from PhenoCAM V2 YAML")
    parser.add_argument("file", nargs="?", type=Path, help="DiseaseCourse YAML path")
    parser.add_argument("--all", action="store_true", help="Generate for all diseases")
    parser.add_argument("-o", "--output", type=Path, help="Output HTML file (default: causal_models/viz/<name>.html)")
    args = parser.parse_args()

    VIZ_DIR.mkdir(parents=True, exist_ok=True)

    if args.all:
        for path in sorted(DISEASES_DIR.glob("*.yaml")):
            data = build_data(path)
            out = VIZ_DIR / path.with_suffix(".html").name
            out.write_text(render_html(data))
            print(f"✓ {out}")
        return

    if not args.file:
        parser.error("Provide a file path or use --all")

    data = build_data(args.file)
    out = args.output or (VIZ_DIR / args.file.with_suffix(".html").name)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_html(data))
    print(f"✓ {out}")


# Stub implementations — filled in Tasks 3–7
def _load_modules(disease: dict) -> dict: return {}
def _collect_nodes(disease: dict, modules: dict) -> dict: return {}
def _build_nodes(catalog: dict) -> list: return []
def _build_edges(disease: dict, catalog: dict) -> list: return []
def _assign_hg_colors(disease: dict) -> dict: return {}
def _build_hypothesis_groups(disease: dict, catalog: dict, colors: dict) -> list: return []
def _build_phenotype_nodes(disease: dict) -> list: return []
def _build_phenotype_edges(disease: dict) -> list: return []
def _build_disease_node(disease: dict) -> dict: return {}
def _build_modules_meta(disease: dict, modules: dict) -> list: return []


if __name__ == "__main__":
    main()
