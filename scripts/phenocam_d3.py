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


# Implementations — Tasks 3–7
def _load_modules(disease: dict) -> dict:
    """Return {module_id: module_dict} for all imports."""
    modules = {}
    for imp in disease.get("imports") or []:
        mid = imp.get("module")
        if not mid:
            continue
        path = MODULES_DIR / f"{mid}.yaml"
        if path.exists():
            modules[mid] = yaml.safe_load(path.read_text())
    return modules


def _collect_nodes(disease: dict, modules: dict) -> dict:
    """Return flat catalog: {node_id: {node, collection, is_module, module_id}}."""
    catalog = {}

    # Module nodes first (lower priority — disease nodes override on id collision)
    for mid, mod in modules.items():
        for col in NODE_COLLECTIONS + [PHENOTYPE_COLLECTION]:
            for node in mod.get(col) or []:
                nid = node.get("id")
                if nid:
                    catalog[nid] = {
                        "node": node,
                        "collection": col,
                        "is_module": True,
                        "module_id": mid,
                    }

    # Disease-local nodes (override module nodes with same id)
    for col in NODE_COLLECTIONS + [PHENOTYPE_COLLECTION]:
        for node in disease.get(col) or []:
            nid = node.get("id")
            if nid:
                catalog[nid] = {
                    "node": node,
                    "collection": col,
                    "is_module": False,
                    "module_id": None,
                }

    return catalog
VARIANT_TYPE_QUALITY = {
    "loss_of_function_variant": "LOSS_OF_FUNCTION",
    "gain_of_function_variant": "GAIN_OF_FUNCTION",
}


def _node_label(node: dict, collection: str) -> str:
    """Build multi-line label for a node."""
    if collection == "variants":
        gene = (node.get("gene") or {}).get("symbol", node.get("id", ""))
        vtype = (node.get("variant_type") or {}).get("label", "variant")
        short_vtype = vtype.replace("loss_of_function_variant", "LOF").replace("gain_of_function_variant", "GOF")
        parts = [gene, short_vtype]
    elif collection == "molecular_activities":
        gene = (node.get("gene") or {}).get("symbol", "")
        mf = (node.get("molecular_function") or {}).get("label", "")
        cx = node.get("complex_name", "")
        name = gene or cx or node.get("id", "")
        short_mf = mf[:22] + "…" if len(mf) > 22 else mf
        parts = [name, short_mf] if short_mf else [name]
    elif collection == "molecular_entities":
        ent = (node.get("entity") or {}).get("label", "")
        gene = (node.get("gene") or {}).get("symbol", "")
        name = ent or gene or node.get("id", "")
        parts = [name[:28] + "…" if len(name) > 28 else name]
    elif collection == "cellular_processes":
        ct = (node.get("cell_type") or {}).get("label", "")
        bp = (node.get("biological_process") or {}).get("label", "")
        short_bp = bp[:20] + "…" if len(bp) > 20 else bp
        parts = [ct, short_bp] if ct else [short_bp or node.get("id", "")]
    elif collection == "tissue_processes":
        anat = (node.get("anatomy") or {}).get("label", "")
        bp = (node.get("biological_process") or {}).get("label", "")
        short_bp = bp[:20] + "…" if len(bp) > 20 else bp
        parts = [anat, short_bp] if anat else [short_bp or node.get("id", "")]
    elif collection == "modulators":
        agent = (node.get("agent") or {}).get("label", node.get("id", ""))
        parts = [agent[:28] + "…" if len(agent) > 28 else agent]
    elif collection == "chemical_exposures":
        agent = (node.get("agent") or {}).get("label", node.get("id", ""))
        parts = [agent[:28] + "…" if len(agent) > 28 else agent]
    elif collection == "environmental_factors":
        factor = (node.get("factor") or {}).get("label", node.get("id", ""))
        parts = [factor[:28] + "…" if len(factor) > 28 else factor]
    else:
        parts = [node.get("id", "?")]
    return "\n".join(p for p in parts if p)


def _node_short_label(node: dict, collection: str) -> str:
    if collection == "molecular_activities":
        return (node.get("gene") or {}).get("symbol", "") or node.get("complex_name", "") or node.get("id", "")
    if collection == "variants":
        return (node.get("gene") or {}).get("symbol", node.get("id", ""))
    return _node_label(node, collection).split("\n")[0]


def _build_nodes(catalog: dict) -> list:
    """Convert catalog entries (non-phenotype) to DATA.nodes format."""
    result = []
    for nid, entry in catalog.items():
        col = entry["collection"]
        if col == PHENOTYPE_COLLECTION:
            continue
        node = entry["node"]
        node_type = NODE_TYPE_MAP.get(col, "activity")
        gene = (node.get("gene") or {}).get("symbol", "")
        mf = (node.get("molecular_function") or {}).get("label", "")
        loc = (node.get("location") or {}).get("label", "")
        bp = (node.get("biological_process") or {}).get("label", "")
        # Derive quality: explicit field wins; fall back to variant_type mapping
        quality = node.get("quality")
        if quality is None and col == "variants":
            vt_label = (node.get("variant_type") or {}).get("label", "")
            quality = VARIANT_TYPE_QUALITY.get(vt_label)
        result.append({
            "id": nid,
            "label": _node_label(node, col),
            "short_label": _node_short_label(node, col),
            "type": node_type,
            "node_kind": col,
            "gene": gene,
            "function": mf,
            "function_short": mf[:18] + "…" if len(mf) > 18 else mf,
            "location": loc,
            "process": bp,
            "module_id": entry["module_id"],
            "hypothesis_ids": node.get("hypotheses") or [],
            "quality": quality,
            "description": node.get("description", ""),
        })
    return result
def _edge_context(source_id: str, target_id: str, catalog: dict) -> tuple:
    """Return (edge_context, module_id)."""
    src = catalog.get(source_id, {})
    tgt = catalog.get(target_id, {})
    src_mod = src.get("module_id")
    tgt_mod = tgt.get("module_id")
    if src_mod and src_mod == tgt_mod:
        return "module_internal", src_mod
    if src_mod or tgt_mod:
        return "cross_module", src_mod or tgt_mod
    return "disease_local", None


def _evidence_list(evidence: list) -> list:
    result = []
    for ev in (evidence or []):
        ref = ev.get("reference", "")
        result.append({
            "type": "literature",
            "id": ref,
            "snippet": ev.get("snippet", ""),
        })
    return result


def _build_edges(disease: dict, catalog: dict) -> list:
    result = []

    # Disease causal_relations
    for rel in disease.get("causal_relations") or []:
        src = rel.get("subject", "")
        tgt = rel.get("object", "")
        if not src or not tgt:
            continue
        if src not in catalog or tgt not in catalog:
            continue
        pred = (rel.get("predicate") or {})
        pred_id = pred.get("id", "RO:0002411")
        eco = rel.get("eco") or {}
        ctx, mod_id = _edge_context(src, tgt, catalog)
        result.append({
            "source": src,
            "target": tgt,
            "relation": RO_LABELS.get(pred_id, pred.get("label", "")),
            "relation_id": pred_id,
            "eco_id": eco.get("id", ""),
            "eco_label": eco.get("label", ""),
            "evidence": _evidence_list(rel.get("evidence")),
            "hypothesis_ids": rel.get("hypotheses") or [],
            "edge_context": ctx,
            "module_id": mod_id,
        })

    # Module internal causal_relations
    for mid, mod in _load_modules(disease).items():
        for rel in mod.get("causal_relations") or []:
            src = rel.get("subject", "")
            tgt = rel.get("object", "")
            if not src or not tgt:
                continue
            if src not in catalog or tgt not in catalog:
                continue
            pred = (rel.get("predicate") or {})
            pred_id = pred.get("id", "RO:0002411")
            eco = rel.get("eco") or {}
            result.append({
                "source": src,
                "target": tgt,
                "relation": RO_LABELS.get(pred_id, pred.get("label", "")),
                "relation_id": pred_id,
                "eco_id": eco.get("id", ""),
                "eco_label": eco.get("label", ""),
                "evidence": _evidence_list(rel.get("evidence")),
                "hypothesis_ids": rel.get("hypotheses") or [],
                "edge_context": "module_internal",
                "module_id": mid,
            })

    return result
def _assign_hg_colors(disease: dict) -> dict:
    colors = {}
    palette = list(HG_PALETTE)
    for i, hg in enumerate(disease.get("hypothesis_groups") or []):
        hid = hg.get("id", "")
        colors[hid] = palette[i % len(palette)]
    return colors


def _build_hypothesis_groups(disease: dict, catalog: dict, hg_colors: dict) -> list:
    result = []
    for hg in disease.get("hypothesis_groups") or []:
        hid = hg.get("id", "")
        states = {}

        for nid, entry in catalog.items():
            node = entry["node"]
            col = entry["collection"]
            if col == PHENOTYPE_COLLECTION:
                continue
            node_hyps = node.get("hypotheses") or []
            if hid not in node_hyps:
                continue

            quality = node.get("quality")
            # Derive quality from variant_type if missing (variants collection)
            if quality is None and col == "variants":
                vtype_label = (node.get("variant_type") or {}).get("label", "")
                quality = VARIANT_TYPE_QUALITY.get(vtype_label)

            state = QUALITY_STATE.get(quality, "decreased" if quality else "normal")
            is_primary = col == "variants"
            states[nid] = {
                "state": state,
                "is_primary": is_primary,
                "eco_id": "",
                "eco_label": "",
                "evidence_refs": [],
                "evidence_snippet": "",
            }

        result.append({
            "id": hid,
            "name": hg.get("name", hid),
            "frequency": hg.get("frequency", ""),
            "description": hg.get("description", ""),
            "color": hg_colors.get(hid, "#999"),
            "states": states,
        })
    return result
def _build_phenotype_nodes(disease: dict) -> list: return []
def _build_phenotype_edges(disease: dict) -> list: return []
def _build_disease_node(disease: dict) -> dict: return {}
def _build_modules_meta(disease: dict, modules: dict) -> list: return []


if __name__ == "__main__":
    main()
