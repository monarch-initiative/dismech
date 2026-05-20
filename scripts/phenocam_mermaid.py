#!/usr/bin/env python3
"""Generate Mermaid flowchart diagrams from PhenoCAM V2 YAML files.

Usage:
    uv run python scripts/phenocam_mermaid.py causal_models/diseases/Gorlin_Syndrome.yaml --target-class DiseaseCourse
    uv run python scripts/phenocam_mermaid.py causal_models/modules/hedgehog_signaling.yaml --target-class Module
    uv run python scripts/phenocam_mermaid.py --all   # generates all files into causal_models/viz/
"""

import argparse
import textwrap
from pathlib import Path

import yaml

MODULES_DIR = Path(__file__).parent.parent / "causal_models" / "modules"
VIZ_DIR = Path(__file__).parent.parent / "causal_models" / "viz"

# Mermaid shape brackets per node-kind collection
_SHAPES = {
    "variants":             (">",   "]"),
    "chemical_exposures":   (">",   "]"),
    "environmental_factors": (">",  "]"),
    "molecular_entities":   ("([",  "])"),
    "molecular_activities": ("[",   "]"),
    "cellular_processes":   ("((",  "))"),
    "tissue_processes":     ("[[",  "]]"),
    "phenotypes":           ("{",   "}"),
    "modulators":           ("[(", ")]"),
}

# CSS class per collection
_CLASSES = {
    "variants":             "variant",
    "chemical_exposures":   "chemical",
    "environmental_factors": "envfactor",
    "molecular_entities":   "molEntity",
    "molecular_activities": "molActivity",
    "cellular_processes":   "cellProcess",
    "tissue_processes":     "tissueProcess",
    "phenotypes":           "phenotype",
    "modulators":           "modulator",
}

_CLASS_STYLES = {
    "variant":      "fill:#ffd6d6,stroke:#c0392b,color:#000",
    "chemical":     "fill:#fdebd0,stroke:#e67e22,color:#000",
    "envfactor":    "fill:#fde8e8,stroke:#922b21,color:#000",
    "molEntity":    "fill:#fef9e7,stroke:#d4ac0d,color:#000",
    "molActivity":  "fill:#d6eaf8,stroke:#2471a3,color:#000",
    "cellProcess":  "fill:#d5f5e3,stroke:#1e8449,color:#000",
    "tissueProcess":"fill:#e8daef,stroke:#7d3c98,color:#000",
    "phenotype":    "fill:#fef5e7,stroke:#ca6f1e,color:#000",
    "modulator":    "fill:#eaf2ff,stroke:#2e4057,color:#000",
    "module_node":  "fill:#f2f3f4,stroke:#aab7b8,color:#666,stroke-dasharray:5 3",
}

# RO predicate → (arrow syntax, default label)
_PREDICATES = {
    "RO:0002411": ("-->",   ""),
    "RO:0002410": ("-.->",  ""),
    "RO:0002630": ("--o",   "inhibits"),
    "RO:0002629": ("==>",   "activates"),
    "RO:0002200": ("-.->",  "has phenotype"),
}

_QUALITY_BADGES = {
    "INCREASED":       "↑",
    "DECREASED":       "↓",
    "ABSENT":          "∅",
    "GAIN_OF_FUNCTION":"GOF",
    "LOSS_OF_FUNCTION":"LOF",
}


def _safe(node_id: str) -> str:
    """Sanitize a node ID to be valid in Mermaid."""
    return node_id.replace("-", "_").replace(" ", "_").replace(":", "_").replace(".", "_")


def _label(node: dict, collection: str) -> str:
    """Build a short, human-readable label for a node."""
    nid = node.get("id", "?")
    quality = node.get("quality", "")
    badge = _QUALITY_BADGES.get(quality, "")

    if collection == "variants":
        gene = (node.get("gene") or {}).get("symbol", nid)
        vtype = (node.get("variant_type") or {}).get("label", "variant")
        short = vtype.replace("loss of function variant", "LOF").replace("loss_of_function_variant", "LOF")
        return f"{gene} {short}"

    if collection == "molecular_entities":
        ent = (node.get("entity") or {}).get("label", nid)
        return _truncate(ent, 28)

    if collection == "molecular_activities":
        gene = (node.get("gene") or {}).get("symbol", "")
        mf = (node.get("molecular_function") or {}).get("label", "")
        if gene and mf:
            short_mf = _truncate(mf, 22)
            lbl = f"{gene}\n{short_mf}"
        elif gene:
            lbl = gene
        else:
            lbl = _truncate(nid, 28)
        if badge:
            lbl += f" [{badge}]"
        return lbl

    if collection == "cellular_processes":
        ct = (node.get("cell_type") or {}).get("label", "")
        bp = (node.get("biological_process") or {}).get("label", "")
        lbl = f"{ct}\n{_truncate(bp, 20)}" if ct else _truncate(bp or nid, 28)
        if badge:
            lbl += f" [{badge}]"
        return lbl

    if collection == "tissue_processes":
        anat = (node.get("anatomy") or {}).get("label", "")
        bp = (node.get("biological_process") or {}).get("label", "")
        lbl = f"{anat}\n{_truncate(bp, 20)}" if anat else _truncate(bp or nid, 28)
        if badge:
            lbl += f" [{badge}]"
        return lbl

    if collection == "phenotypes":
        hpo = (node.get("hpo_term") or {}).get("label", nid)
        return _truncate(hpo, 28)

    if collection == "modulators":
        agent = (node.get("agent") or {}).get("label", nid)
        return _truncate(agent, 28)

    return _truncate(nid, 28)


def _truncate(s: str, n: int) -> str:
    return s if len(s) <= n else s[:n - 1] + "…"


def _mermaid_node(sid: str, label: str, collection: str) -> str:
    open_, close = _SHAPES.get(collection, ("[", "]"))
    # Escape double-quotes inside labels; use double-quote wrapping for multi-word labels
    label_escaped = label.replace('"', "'")
    return f'    {sid}{open_}"{label_escaped}"{close}'


def _mermaid_edge(subj: str, obj: str, predicate_id: str, label_override: str = "") -> str:
    arrow, default_lbl = _PREDICATES.get(predicate_id, ("-->", ""))
    lbl = label_override or default_lbl
    if not lbl:
        return f"    {subj} {arrow} {obj}"
    # Use "-- label -->" style so label text doesn't conflict with Mermaid bracket syntax
    if arrow == "-->":
        return f"    {subj} -- {lbl} --> {obj}"
    if arrow == "--o":
        return f"    {subj} -- {lbl} --o {obj}"
    if arrow == "-.->":
        return f"    {subj} -. {lbl} .-> {obj}"
    if arrow == "==>":
        return f"    {subj} == {lbl} ==> {obj}"
    return f"    {subj} -- {lbl} --> {obj}"


def collect_nodes(data: dict) -> dict[str, tuple[dict, str]]:
    """Return {node_id: (node_dict, collection)} for all nodes in a document."""
    nodes = {}
    for col in _SHAPES:
        for node in data.get(col) or []:
            if nid := node.get("id"):
                nodes[nid] = (node, col)
    return nodes


def generate(data: dict, target_class: str, title: str = "") -> str:
    """Generate a Mermaid flowchart string from a V2 YAML document."""
    local_nodes = collect_nodes(data)

    # For DiseaseCourse: load imported module nodes (shown differently)
    module_nodes: dict[str, tuple[dict, str]] = {}
    if target_class == "DiseaseCourse":
        for imp in data.get("imports") or []:
            module_id = imp.get("module")
            if not module_id:
                continue
            module_path = MODULES_DIR / f"{module_id}.yaml"
            if module_path.exists():
                with open(module_path) as f:
                    mod_data = yaml.safe_load(f)
                for nid, pair in collect_nodes(mod_data or {}).items():
                    module_nodes[nid] = (pair[0], pair[1])

    all_nodes = {**module_nodes, **local_nodes}

    lines: list[str] = []
    lines.append("%%{init: {'flowchart': {'curve': 'basis', 'htmlLabels': true}}}%%")
    lines.append("flowchart TD")
    lines.append("")

    # Class definitions
    for cls, style in _CLASS_STYLES.items():
        lines.append(f"    classDef {cls} {style}")
    lines.append("")

    # Module nodes in a subgraph (if any)
    if module_nodes:
        imports = [imp.get("module", "") for imp in (data.get("imports") or [])]
        module_label = " + ".join(imports)
        lines.append(f"    subgraph mod[\"📦 {module_label} module\"]")
        for nid, (node, col) in module_nodes.items():
            sid = _safe(nid)
            lbl = _label(node, col)
            lines.append(_mermaid_node(sid, lbl, col))
            lines.append(f"    class {sid} module_node")
        lines.append("    end")
        lines.append("")

    # Hypothesis subgraphs for local nodes
    hyp_groups = {g["id"]: g for g in (data.get("hypothesis_groups") or []) if "id" in g}

    # Group local nodes by hypothesis (nodes with exactly one hypothesis)
    hyp_to_nodes: dict[str, list] = {hid: [] for hid in hyp_groups}
    shared_nodes: list = []

    for nid, (node, col) in local_nodes.items():
        hyps = node.get("hypotheses") or []
        if len(hyps) == 1 and hyps[0] in hyp_groups:
            hyp_to_nodes[hyps[0]].append((nid, node, col))
        else:
            shared_nodes.append((nid, node, col))

    # Emit shared local nodes
    if shared_nodes:
        for nid, node, col in shared_nodes:
            sid = _safe(nid)
            lbl = _label(node, col)
            lines.append(_mermaid_node(sid, lbl, col))
            lines.append(f"    class {sid} {_CLASSES.get(col, 'molActivity')}")
        lines.append("")

    # Emit hypothesis-tagged nodes in subgraphs
    for hid, nodes in hyp_to_nodes.items():
        if not nodes:
            continue
        hg = hyp_groups[hid]
        freq = hg.get("frequency", "")
        subgraph_label = hg.get("name", hid)
        if freq:
            subgraph_label += f" ({freq})"
        lines.append(f"    subgraph hyp_{_safe(hid)}[\"🧬 {subgraph_label}\"]")
        for nid, node, col in nodes:
            sid = _safe(nid)
            lbl = _label(node, col)
            lines.append(_mermaid_node(sid, lbl, col))
            lines.append(f"    class {sid} {_CLASSES.get(col, 'variant')}")
        lines.append("    end")
        lines.append("")

    # Edges from causal_relations
    lines.append("    %% Causal relations")
    for rel in data.get("causal_relations") or []:
        subj = rel.get("subject", "")
        obj = rel.get("object", "")
        if not subj or not obj:
            continue
        if subj not in all_nodes or obj not in all_nodes:
            continue  # skip unresolved (shouldn't happen after validation)
        pred = (rel.get("predicate") or {}).get("id", "RO:0002411")
        effect = rel.get("effect", "")
        hyps = rel.get("hypotheses") or []
        hyp_label = hyps[0] if len(hyps) == 1 else ""
        label = effect or hyp_label
        lines.append(_mermaid_edge(_safe(subj), _safe(obj), pred, label))

    lines.append("")

    # Build markdown output
    doc_title = title or data.get("name", "PhenoCAM V2 Model")
    mondo = (data.get("realises_disease") or {}).get("label", "")
    subtitle = f" — {mondo}" if mondo else ""

    md_lines = [
        f"# {doc_title}{subtitle}",
        "",
        "```mermaid",
    ] + lines + [
        "```",
        "",
    ]

    # Legend
    md_lines += [
        "## Legend",
        "",
        "| Shape | Node kind |",
        "|-------|-----------|",
        "| `>rect]` | Variant / input |",
        "| `([pill])` | Molecular entity (protein / chemical) |",
        "| `[rect]` | Molecular activity |",
        "| `((circle))` | Cellular process |",
        "| `[[double-rect]]` | Tissue process |",
        "| `{diamond}` | Phenotype |",
        "| `[(cylinder)]` | Modulator (therapeutic / dietary) |",
        "| dashed grey | Imported module node |",
        "",
    ]

    return "\n".join(md_lines)


def main():
    parser = argparse.ArgumentParser(description="Generate Mermaid diagram from PhenoCAM V2 YAML")
    parser.add_argument("file", nargs="?", type=Path, help="Path to module or disease YAML file")
    parser.add_argument("--target-class", choices=["Module", "DiseaseCourse"], help="Target class")
    parser.add_argument("--all", action="store_true", help="Generate viz for all modules and diseases")
    parser.add_argument("-o", "--output", type=Path, help="Output markdown file (default: stdout)")
    args = parser.parse_args()

    VIZ_DIR.mkdir(parents=True, exist_ok=True)

    if args.all:
        for path in sorted(MODULES_DIR.glob("*.yaml")):
            with open(path) as f:
                data = yaml.safe_load(f)
            md = generate(data, "Module")
            out = VIZ_DIR / path.with_suffix(".md").name
            out.write_text(md)
            print(f"✓ {out}")
        diseases_dir = MODULES_DIR.parent / "diseases"
        for path in sorted(diseases_dir.glob("*.yaml")):
            with open(path) as f:
                data = yaml.safe_load(f)
            md = generate(data, "DiseaseCourse")
            out = VIZ_DIR / path.with_suffix(".md").name
            out.write_text(md)
            print(f"✓ {out}")
        return

    if not args.file:
        parser.error("Provide a file path or use --all")
    if not args.target_class:
        parser.error("--target-class is required when specifying a file")

    with open(args.file) as f:
        data = yaml.safe_load(f)

    md = generate(data, args.target_class)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(md)
        print(f"✓ Written to {args.output}")
    else:
        print(md)


if __name__ == "__main__":
    main()
