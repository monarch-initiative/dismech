#!/usr/bin/env python3
"""Generate interactive HTML visualization of pheno-CAM disease models.

Reads a disease YAML + its imported module(s) and produces a self-contained HTML
file with D3.js + dagre-d3 layout showing:
  - Module activities as nodes (colored by perturbation state)
  - Module edges as arrows (with RO relation labels)
  - Phenotype routes connecting terminal activities to HPO phenotype boxes
  - Hypothesis group selector to switch between perturbation overlays

Usage:
    python scripts/visualize_phenocam.py causal_models/diseases/Noonan_Syndrome.yaml
    python scripts/visualize_phenocam.py causal_models/diseases/Noonan_Syndrome.yaml -o viz.html
    python scripts/visualize_phenocam.py --all  # visualize all disease files
"""

import argparse
import json
import sys
from pathlib import Path

import yaml

CAUSAL_DIR = Path("causal_models")
OUTPUT_DIR = Path("causal_models/viz")


def load_disease(path: Path) -> dict:
    with open(path) as f:
        return yaml.safe_load(f)["disease_model"]


def load_module(module_id: str) -> dict:
    path = CAUSAL_DIR / "modules" / f"{module_id}.yaml"
    with open(path) as f:
        return yaml.safe_load(f)["module"]


def build_graph_data(disease: dict) -> dict:
    """Build a JSON-serializable graph structure for the visualization."""
    modules = {}
    for imp in disease.get("imports", []):
        mod = load_module(imp["module"])
        modules[mod["id"]] = mod

    # Build nodes from module activities
    nodes = []
    for mod_id, mod in modules.items():
        for act in mod.get("activities", []):
            node_id = f"{mod_id}:{act['id']}"
            display_name = act.get("display_name", "")
            gene = act.get("gene", {}).get("symbol", "")
            complex_name = act.get("complex", "")
            mf_label = act.get("molecular_function", {}).get("label", "")
            loc_label = act.get("location", {}).get("label", "")
            substrate = act.get("substrate", {}).get("symbol", "")

            # Label priority: display_name > gene [substrate] > gene > complex > id
            if display_name:
                short_label = display_name
            elif substrate:
                primary = gene or complex_name
                short_label = f"{primary} [{substrate}]"
            else:
                short_label = gene or complex_name or act["id"]

            func_short = _shorten_function(mf_label, substrate)

            mf_id = act.get("molecular_function", {}).get("id", "")
            loc_id = act.get("location", {}).get("id", "")
            proc_label = act.get("process", {}).get("label", "")
            proc_id = act.get("process", {}).get("id", "")
            hgnc_id = act.get("gene", {}).get("hgnc_id", "")
            substrate_hgnc = act.get("substrate", {}).get("hgnc_id", "")

            nodes.append({
                "id": node_id,
                "gene": gene,
                "hgnc_id": hgnc_id,
                "complex": complex_name,
                "display_name": display_name,
                "function": mf_label,
                "function_id": mf_id,
                "function_short": func_short,
                "location": loc_label,
                "location_id": loc_id,
                "process": proc_label,
                "process_id": proc_id,
                "substrate": substrate,
                "substrate_hgnc": substrate_hgnc,
                "label": f"{short_label}\n{func_short}",
                "short_label": short_label,
                "type": "activity",
            })

    # Build edges from module edges
    edges = []
    for mod_id, mod in modules.items():
        for edge in mod.get("edges", []):
            evidence_list = []
            for ev in edge.get("evidence", []):
                if ev.get("type") == "go_cam":
                    evidence_list.append({"type": "GO-CAM", "id": ev.get("id", "")})
                elif ev.get("type") == "literature":
                    evidence_list.append({
                        "type": "literature",
                        "id": ev.get("reference", ""),
                        "snippet": ev.get("snippet", ""),
                    })
            edges.append({
                "source": f"{mod_id}:{edge['source']}",
                "target": f"{mod_id}:{edge['target']}",
                "relation": edge["relation"]["label"],
                "relation_id": edge["relation"]["id"],
                "evidence": evidence_list,
            })

    # Build hypothesis groups with perturbation data
    hypothesis_groups = []
    for hg in disease.get("hypothesis_groups", []):
        states = {}
        # Primary perturbations
        for p in hg.get("perturbations", []):
            variant = p.get("variant_class", {}).get("label", "")
            ev_snippets = [e.get("snippet", "") for e in p.get("evidence", []) if e.get("snippet")]
            ev_refs = [e.get("reference", "") for e in p.get("evidence", []) if e.get("reference")]
            states[p["target_activity"]] = {
                "state": p["perturbed_state"],
                "mechanism": p.get("mechanism", ""),
                "variant_class": variant,
                "is_primary": True,
                "provenance": "primary_mutation",
                "cause": "",
                "evidence_refs": ev_refs,
                "evidence_snippet": ev_snippets[0] if ev_snippets else "",
            }
        # Propagated states
        for ps in hg.get("propagated_states", []):
            ev_snippets = [e.get("snippet", "") for e in ps.get("evidence", []) if e.get("snippet")]
            ev_refs = [e.get("reference", "") for e in ps.get("evidence", []) if e.get("reference")]
            states[ps["activity"]] = {
                "state": ps["perturbed_state"],
                "mechanism": "",
                "variant_class": "",
                "is_primary": False,
                "provenance": ps.get("provenance", ""),
                "cause": ps.get("cause", ""),
                "evidence_refs": ev_refs,
                "evidence_snippet": ev_snippets[0] if ev_snippets else "",
            }
        hypothesis_groups.append({
            "id": hg["id"],
            "name": hg["name"],
            "frequency": hg.get("frequency", ""),
            "description": hg.get("description", "").strip(),
            "states": states,
        })

    # Build label lookup from activity nodes (for resolving driven_by references)
    node_label_lookup = {}
    for n in nodes:
        node_label_lookup[n["id"]] = n["short_label"]

    # Build phenotype routes with intermediate nodes and edges
    phenotype_routes = []
    intermediate_nodes = []
    intermediate_edges = []

    for pr in disease.get("phenotype_routes", []):
        route_id = pr["id"]
        route_name = pr["name"]
        raw_intermediates = pr.get("intermediates", [])
        inter_node_ids = []  # track IDs for chaining
        route_tissue = _extract_tissue(pr)
        route_tissue_detail = _extract_tissue_detail(pr)
        route_evidence = _extract_route_evidence(pr)

        for i, inter in enumerate(raw_intermediates):
            inter_id = f"inter:{route_id}:{i}"
            gene_sym = inter.get("gene", {}).get("symbol", "")
            hgnc = inter.get("gene", {}).get("hgnc_id", "")
            bp_label = inter.get("biological_process", {}).get("label", "")
            bp_id = inter.get("biological_process", {}).get("id", "")
            state = inter.get("perturbed_state", "")
            driven_by = inter.get("driven_by", [])

            # Resolve driven_by to human-readable labels
            driven_by_labels = [node_label_lookup.get(src, src) for src in driven_by]

            # Short label: gene symbol if present, otherwise abbreviated name
            if gene_sym:
                short_label = gene_sym
            else:
                name = inter.get("name", "")
                short_label = name if len(name) <= 28 else name[:25] + "..."

            intermediate_nodes.append({
                "id": inter_id,
                "name": inter.get("name", ""),
                "gene": gene_sym,
                "hgnc_id": hgnc,
                "process": bp_label,
                "process_id": bp_id,
                "state": state,
                "short_label": short_label,
                "type": "intermediate",
                "route_id": route_id,
                "route_name": route_name,
                "driven_by": driven_by,
                "driven_by_labels": driven_by_labels,
                "tissue": route_tissue,
                "tissue_detail": route_tissue_detail,
                "route_evidence": route_evidence,
            })
            # Also register in label lookup for edge resolution
            node_label_lookup[inter_id] = short_label
            inter_node_ids.append(inter_id)

            # Edges: activity → intermediate (from driven_by)
            if driven_by:
                for src in driven_by:
                    intermediate_edges.append({
                        "source": src,
                        "target": inter_id,
                        "edge_type": "activity_to_intermediate",
                        "source_label": node_label_lookup.get(src, src),
                        "target_label": short_label,
                    })
            else:
                # Convergence: connect from all preceding intermediates in this route
                for prev_id in inter_node_ids[:-1]:
                    intermediate_edges.append({
                        "source": prev_id,
                        "target": inter_id,
                        "edge_type": "intermediate_chain",
                        "source_label": node_label_lookup.get(prev_id, prev_id),
                        "target_label": short_label,
                    })

        # Edge from last intermediate → phenotype
        tp = pr.get("target_phenotype", {})
        pheno_node_id = f"pheno:{route_id}"
        pheno_label = tp.get("preferred_term", "")
        if inter_node_ids:
            intermediate_edges.append({
                "source": inter_node_ids[-1],
                "target": pheno_node_id,
                "edge_type": "intermediate_to_phenotype",
                "source_label": node_label_lookup.get(inter_node_ids[-1], inter_node_ids[-1]),
                "target_label": pheno_label,
            })
        # Also register phenotype in label lookup
        node_label_lookup[pheno_node_id] = pheno_label

        # Build intermediates summary for phenotype tooltip
        intermediates_summary = []
        for iid in inter_node_ids:
            for inode in intermediate_nodes:
                if inode["id"] == iid:
                    intermediates_summary.append({
                        "name": inode["name"],
                        "gene": inode["gene"],
                        "process": inode["process"],
                        "state": inode["state"],
                    })
                    break

        phenotype_routes.append({
            "id": route_id,
            "name": route_name,
            "description": pr.get("description", "").strip(),
            "intermediate_ids": inter_node_ids,
            "intermediates": intermediates_summary,
            "phenotype_label": pheno_label,
            "phenotype_id": tp.get("term", {}).get("id", ""),
            "tissue": route_tissue,
            "tissue_detail": route_tissue_detail,
            "evidence": route_evidence,
        })

    return {
        "disease_name": disease["name"],
        "disease_id": disease["id"],
        "disease_term": disease.get("disease_term", {}),
        "nodes": nodes,
        "edges": edges,
        "hypothesis_groups": hypothesis_groups,
        "phenotype_routes": phenotype_routes,
        "intermediate_nodes": intermediate_nodes,
        "intermediate_edges": intermediate_edges,
    }


def _shorten_function(mf_label: str, substrate: str = "") -> str:
    """Produce a concise function description for node display."""
    if not mf_label:
        return ""
    # Common shortenings
    short = mf_label
    short = short.replace("protein serine/threonine kinase activity", "Ser/Thr kinase")
    short = short.replace("cAMP-dependent protein kinase activity", "cAMP-dep. kinase")
    short = short.replace("G protein-coupled receptor activity", "GPCR activity")
    short = short.replace("Hedgehog receptor activity", "Hh receptor")
    short = short.replace("protein sequestering activity", f"sequesters {substrate}" if substrate else "sequestering")
    short = short.replace("DNA-binding transcription activator activity, RNA polymerase II-specific", "tx activator")
    short = short.replace("DNA-binding transcription repressor activity, RNA polymerase II-specific", "tx repressor")
    short = short.replace("ubiquitin-like ligase-substrate adaptor activity", "ubiquitin ligase adaptor")
    short = short.replace("protein carrier chaperone activity", "carrier/chaperone")
    short = short.replace("Ras guanyl-nucleotide exchange factor activity", "Ras GEF")
    short = short.replace("GTPase activity", "GTPase")
    short = short.replace("protein-macromolecule adaptor activity", "adaptor")
    short = short.replace("epidermal growth factor-activated receptor activity", "EGF receptor")
    short = short.replace("protein tyrosine phosphatase activity", "Tyr phosphatase")
    short = short.replace("MAP kinase kinase activity", "MAP2K (MEK)")
    short = short.replace("MAP kinase activity", "MAPK (ERK)")
    return short


def _extract_tissue(pr: dict) -> str:
    tissue = pr.get("tissue", {})
    parts = []
    if "cell_type" in tissue:
        parts.append(tissue["cell_type"].get("label", ""))
    if "anatomy" in tissue:
        parts.append(tissue["anatomy"].get("label", ""))
    return " / ".join(p for p in parts if p)


def _extract_tissue_detail(pr: dict) -> dict:
    """Extract full tissue detail with ontology IDs."""
    tissue = pr.get("tissue", {})
    detail = {}
    ct = tissue.get("cell_type", {})
    if ct:
        detail["cell_type_label"] = ct.get("label", "")
        detail["cell_type_id"] = ct.get("id", "")
    anat = tissue.get("anatomy", {})
    if anat:
        detail["anatomy_label"] = anat.get("label", "")
        detail["anatomy_id"] = anat.get("id", "")
    return detail


def _extract_route_evidence(pr: dict) -> list:
    """Extract evidence from a phenotype route."""
    result = []
    for ev in pr.get("evidence", []):
        entry = {"type": ev.get("type", ""), "reference": ev.get("reference", "")}
        if ev.get("snippet"):
            entry["snippet"] = ev["snippet"]
        result.append(entry)
    return result


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Pheno-CAM: {disease_name}</title>
<script src="https://d3js.org/d3.v7.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/dagre@0.8.5/dist/dagre.min.js"></script>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #f8f9fa; }}
#header {{
  padding: 16px 24px; background: white; border-bottom: 1px solid #dee2e6;
  display: flex; align-items: center; gap: 24px; flex-wrap: wrap;
}}
#header h1 {{ font-size: 20px; color: #212529; }}
#header .disease-term {{ color: #6c757d; font-size: 14px; }}
#controls {{ display: flex; align-items: center; gap: 12px; }}
#controls label {{ font-size: 13px; color: #495057; font-weight: 600; }}
#controls select {{ font-size: 13px; padding: 4px 8px; border-radius: 4px; border: 1px solid #ced4da; }}
#hg-info {{ font-size: 12px; color: #6c757d; max-width: 500px; }}
#canvas {{ width: 100%; height: calc(100vh - 70px); }}
svg {{ width: 100%; height: 100%; }}

.node rect {{
  rx: 6; ry: 6; stroke-width: 2; cursor: pointer;
  transition: opacity 0.3s;
}}
.node text {{ font-size: 11px; pointer-events: none; }}
.node .gene-label {{ font-weight: 700; font-size: 13px; }}
.node .func-label {{ font-size: 10px; fill: #495057; }}
.node .state-badge {{
  font-size: 9px; font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.5px;
}}

.edge path {{ fill: none; stroke-width: 1.5; }}
.edge marker {{ fill: #868e96; }}
.edge .edge-label {{ font-size: 9px; fill: #868e96; }}

.intermediate-node rect {{
  rx: 6; ry: 6; fill: #ede0f7; stroke: #6f42c1; stroke-width: 2; cursor: pointer;
}}
.intermediate-node text {{ font-size: 11px; pointer-events: none; }}
.intermediate-node .gene-label {{ font-weight: 700; font-size: 12px; fill: #3d1f6d; }}
.intermediate-node .func-label {{ font-size: 9px; fill: #6f42c1; }}
.intermediate-node .state-badge {{ font-size: 9px; font-weight: 700; fill: #3d1f6d; }}

.phenotype-node rect {{
  rx: 12; ry: 12; fill: #fff3cd; stroke: #ffc107; stroke-width: 2;
}}
.phenotype-node text {{ font-size: 11px; font-weight: 600; fill: #856404; }}
.phenotype-edge path {{ fill: none; stroke: #ffc107; stroke-width: 1.5; stroke-dasharray: 5,3; }}
.intermediate-edge path {{ fill: none; stroke: #6f42c1; stroke-width: 1.5; }}
.intermediate-to-pheno-edge path {{ fill: none; stroke: #ffc107; stroke-width: 1.5; stroke-dasharray: 5,3; }}

/* Perturbation state colors */
.state-normal rect {{ fill: #f8f9fa; stroke: #dee2e6; }}
.state-absent rect {{ fill: #f8d7da; stroke: #dc3545; stroke-dasharray: 4,2; }}
.state-decreased rect {{ fill: #fde8e8; stroke: #e57373; }}
.state-increased rect {{ fill: #d4edda; stroke: #28a745; }}
.state-constitutively_active rect {{ fill: #c3e6cb; stroke: #1b5e20; stroke-width: 3; }}
.state-substrate_accumulated rect {{ fill: #fff3cd; stroke: #ff8f00; }}
.state-haploinsufficient rect {{ fill: #fde8e8; stroke: #e57373; stroke-dasharray: 4,2; }}

.state-primary rect {{ stroke-width: 3; }}
.state-primary .gene-label {{ text-decoration: underline; }}

/* Legend */
#legend {{
  position: absolute; bottom: 16px; left: 16px; background: white;
  border: 1px solid #dee2e6; border-radius: 8px; padding: 12px 16px;
  font-size: 11px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}}
#legend h3 {{ font-size: 12px; margin-bottom: 8px; color: #495057; }}
.legend-item {{ display: flex; align-items: center; gap: 8px; margin: 4px 0; }}
.legend-swatch {{
  width: 20px; height: 14px; border-radius: 3px; flex-shrink: 0;
}}

/* Tooltip */
#tooltip {{
  position: absolute; display: none; background: white; border: 1px solid #dee2e6;
  border-radius: 6px; padding: 12px 16px; font-size: 12px; max-width: 420px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15); pointer-events: none; z-index: 100;
  line-height: 1.4;
}}
#tooltip .tt-title {{ font-weight: 700; margin-bottom: 6px; font-size: 13px; }}
#tooltip .tt-subtitle {{ color: #6c757d; font-size: 11px; margin-bottom: 6px; }}
#tooltip .tt-detail {{ color: #495057; margin: 3px 0; }}
#tooltip .tt-detail b {{ color: #212529; }}
#tooltip .tt-section {{ margin-top: 8px; padding-top: 6px; border-top: 1px solid #e9ecef; }}
#tooltip .tt-evidence {{ font-size: 11px; color: #6c757d; font-style: italic; margin-top: 4px; }}
#tooltip .tt-ref {{ font-size: 10px; color: #0d6efd; }}
#tooltip .tt-state {{ display: inline-block; padding: 1px 6px; border-radius: 3px; font-size: 10px; font-weight: 600; }}
#tooltip .tt-state-increased {{ background: #d4edda; color: #155724; }}
#tooltip .tt-state-decreased {{ background: #fde8e8; color: #721c24; }}
#tooltip .tt-state-absent {{ background: #f8d7da; color: #721c24; }}
#tooltip .tt-state-constitutively_active {{ background: #c3e6cb; color: #155724; }}
#tooltip .tt-state-substrate_accumulated {{ background: #fff3cd; color: #856404; }}

.edge path.edge-hover {{ stroke: transparent; stroke-width: 12; cursor: pointer; fill: none; }}
</style>
</head>
<body>
<div id="header">
  <div>
    <h1>Pheno-CAM: {disease_name}</h1>
    <span class="disease-term">{disease_term_id} &mdash; {disease_term_label}</span>
  </div>
  <div id="controls">
    <label for="hg-select">Hypothesis:</label>
    <select id="hg-select"></select>
  </div>
  <div id="hg-info"></div>
</div>
<div id="canvas"><svg></svg></div>
<div id="legend">
  <h3>Perturbation States</h3>
  <div class="legend-item"><div class="legend-swatch" style="background:#f8f9fa;border:1px solid #dee2e6"></div> Normal</div>
  <div class="legend-item"><div class="legend-swatch" style="background:#c3e6cb;border:2px solid #1b5e20"></div> Constitutively active</div>
  <div class="legend-item"><div class="legend-swatch" style="background:#d4edda;border:1px solid #28a745"></div> Increased</div>
  <div class="legend-item"><div class="legend-swatch" style="background:#fde8e8;border:1px solid #e57373"></div> Decreased</div>
  <div class="legend-item"><div class="legend-swatch" style="background:#f8d7da;border:1px dashed #dc3545"></div> Absent</div>
  <div class="legend-item"><div class="legend-swatch" style="background:#fff3cd;border:1px solid #ff8f00"></div> Accumulated</div>
  <div class="legend-item"><div class="legend-swatch" style="background:#ede0f7;border:2px solid #6f42c1"></div> Intermediate</div>
  <div class="legend-item"><div class="legend-swatch" style="background:#fff3cd;border:2px solid #ffc107;border-radius:8px"></div> Phenotype</div>
  <div class="legend-item" style="margin-top:6px"><div style="width:20px;height:2px;background:#1b5e20"></div> <b>Bold border</b> = primary site</div>
</div>
<div id="tooltip"></div>
<script>
const DATA = {graph_json};

// --- Layout with dagre ---
function layoutGraph(data) {{
  const g = new dagre.graphlib.Graph({{ compound: false }});
  g.setGraph({{ rankdir: "LR", ranksep: 80, nodesep: 40, marginx: 40, marginy: 40 }});
  g.setDefaultEdgeLabel(() => ({{}}));

  data.nodes.forEach(n => {{
    const w = Math.max(140, n.short_label.length * 8 + 30);
    g.setNode(n.id, {{ label: n.short_label, width: w, height: 60 }});
  }});
  data.edges.forEach(e => {{
    g.setEdge(e.source, e.target);
  }});
  // Add intermediate nodes
  (data.intermediate_nodes || []).forEach(n => {{
    const w = Math.max(130, n.short_label.length * 7 + 24);
    g.setNode(n.id, {{ label: n.short_label, width: w, height: 50 }});
  }});
  // Add intermediate edges (activity→inter, inter→inter, inter→phenotype)
  (data.intermediate_edges || []).forEach(e => {{
    g.setEdge(e.source, e.target);
  }});
  // Add phenotype nodes (no longer directly connected from activities)
  data.phenotype_routes.forEach(pr => {{
    const pid = "pheno:" + pr.id;
    g.setNode(pid, {{ label: pr.phenotype_label, width: 140, height: 40 }});
    // If route has no intermediates, fall back to direct connection
    if (!pr.intermediate_ids || pr.intermediate_ids.length === 0) {{
      // No intermediates — shouldn't happen, but safety fallback
    }}
  }});

  dagre.layout(g);
  return g;
}}

// --- Render ---
function render() {{
  const svg = d3.select("svg");
  svg.selectAll("*").remove();

  const g = layoutGraph(DATA);
  const graphInfo = g.graph();

  // Zoom/pan
  const zoom = d3.zoom().scaleExtent([0.3, 3]).on("zoom", (e) => {{
    container.attr("transform", e.transform);
  }});
  svg.call(zoom);

  const container = svg.append("g");

  // Fit to view
  const svgEl = svg.node();
  const W = svgEl.clientWidth || 900;
  const H = svgEl.clientHeight || 600;
  const gW = graphInfo.width || 800;
  const gH = graphInfo.height || 400;
  const scale = Math.min(W / (gW + 80), H / (gH + 80), 1.2);
  const tx = (W - gW * scale) / 2;
  const ty = (H - gH * scale) / 2;
  svg.call(zoom.transform, d3.zoomIdentity.translate(tx, ty).scale(scale));

  // Arrow marker
  svg.append("defs").append("marker")
    .attr("id", "arrowhead").attr("viewBox", "0 0 10 10")
    .attr("refX", 10).attr("refY", 5)
    .attr("markerWidth", 8).attr("markerHeight", 8)
    .attr("orient", "auto")
    .append("path").attr("d", "M 0 0 L 10 5 L 0 10 z").attr("fill", "#868e96");

  svg.select("defs").append("marker")
    .attr("id", "arrowhead-phenotype").attr("viewBox", "0 0 10 10")
    .attr("refX", 10).attr("refY", 5)
    .attr("markerWidth", 8).attr("markerHeight", 8)
    .attr("orient", "auto")
    .append("path").attr("d", "M 0 0 L 10 5 L 0 10 z").attr("fill", "#ffc107");

  svg.select("defs").append("marker")
    .attr("id", "arrowhead-intermediate").attr("viewBox", "0 0 10 10")
    .attr("refX", 10).attr("refY", 5)
    .attr("markerWidth", 8).attr("markerHeight", 8)
    .attr("orient", "auto")
    .append("path").attr("d", "M 0 0 L 10 5 L 0 10 z").attr("fill", "#6f42c1");

  // Draw module edges
  const edgeGroup = container.append("g").attr("class", "edges");
  // Build a lookup from node id to short_label for edge tooltips
  const nodeLabels = {{}};
  DATA.nodes.forEach(n => {{ nodeLabels[n.id] = n.short_label; }});
  (DATA.intermediate_nodes || []).forEach(n => {{ nodeLabels[n.id] = n.short_label; }});

  DATA.edges.forEach(e => {{
    const pts = g.edge(e.source, e.target);
    if (!pts || !pts.points) return;
    const line = d3.line().x(d => d.x).y(d => d.y).curve(d3.curveBasis);
    const isNeg = e.relation_id === "RO:0002630" || e.relation_id === "RO:0002409";
    const eg = edgeGroup.append("g").attr("class", "edge");
    const pathD = line(pts.points);
    eg.append("path")
      .attr("d", pathD)
      .attr("stroke", isNeg ? "#e57373" : "#868e96")
      .attr("marker-end", "url(#arrowhead)");
    // Invisible wider path for hover target
    eg.append("path").attr("class", "edge-hover").attr("d", pathD);
    // Label at midpoint
    const mid = pts.points[Math.floor(pts.points.length / 2)];
    const shortRel = e.relation.replace("directly ", "").replace("regulates", "reg.");
    eg.append("text").attr("class", "edge-label")
      .attr("x", mid.x).attr("y", mid.y - 6)
      .attr("text-anchor", "middle").text(shortRel);
    // Edge tooltip
    eg.on("mouseover", (event) => {{
      const tt = d3.select("#tooltip");
      tt.style("display", "block")
        .style("left", (event.pageX + 12) + "px")
        .style("top", (event.pageY - 10) + "px");
      const srcLabel = nodeLabels[e.source] || e.source;
      const tgtLabel = nodeLabels[e.target] || e.target;
      let evHtml = "";
      if (e.evidence && e.evidence.length) {{
        evHtml = `<div class="tt-section"><b>Evidence:</b>`;
        e.evidence.forEach(ev => {{
          if (ev.type === "GO-CAM") {{
            evHtml += `<div class="tt-ref">📦 ${{ev.id}}</div>`;
          }} else {{
            evHtml += `<div class="tt-ref">📄 ${{ev.id}}</div>`;
            if (ev.snippet) evHtml += `<div class="tt-evidence">"${{ev.snippet}}"</div>`;
          }}
        }});
        evHtml += `</div>`;
      }}
      tt.html(`<div class="tt-title">${{srcLabel}} → ${{tgtLabel}}</div>
        <div class="tt-detail"><b>Relation:</b> ${{e.relation}}</div>
        <div class="tt-detail"><b>Relation ID:</b> ${{e.relation_id}}</div>
        ${{evHtml}}`);
    }}).on("mouseout", () => d3.select("#tooltip").style("display", "none"));
  }});

  // Draw intermediate edges
  const edgeTypeLabels = {{
    "activity_to_intermediate": "drives",
    "intermediate_chain": "contributes to",
    "intermediate_to_phenotype": "leads to",
  }};
  (DATA.intermediate_edges || []).forEach(e => {{
    const pts = g.edge(e.source, e.target);
    if (!pts || !pts.points) return;
    const line = d3.line().x(d => d.x).y(d => d.y).curve(d3.curveBasis);
    const pathD = line(pts.points);
    let eg;
    if (e.edge_type === "intermediate_to_phenotype") {{
      eg = edgeGroup.append("g").attr("class", "intermediate-to-pheno-edge");
      eg.append("path").attr("d", pathD).attr("marker-end", "url(#arrowhead-phenotype)");
    }} else {{
      eg = edgeGroup.append("g").attr("class", "intermediate-edge");
      eg.append("path").attr("d", pathD).attr("marker-end", "url(#arrowhead-intermediate)");
    }}
    // Invisible wider path for hover target
    eg.append("path").attr("class", "edge-hover").attr("d", pathD);
    // Tooltip
    const srcLabel = e.source_label || nodeLabels[e.source] || e.source;
    const tgtLabel = e.target_label || nodeLabels[e.target] || e.target;
    const relLabel = edgeTypeLabels[e.edge_type] || e.edge_type;
    eg.on("mouseover", (event) => {{
      const tt = d3.select("#tooltip");
      tt.style("display", "block")
        .style("left", (event.pageX + 12) + "px")
        .style("top", (event.pageY - 10) + "px");
      tt.html(`<div class="tt-title">${{srcLabel}} → ${{tgtLabel}}</div>
        <div class="tt-detail"><b>Relationship:</b> ${{srcLabel}} ${{relLabel}} ${{tgtLabel}}</div>
        <div class="tt-detail" style="font-size:10px;color:#6c757d">Type: ${{e.edge_type.replace(/_/g, " ")}}</div>`);
    }}).on("mouseout", () => d3.select("#tooltip").style("display", "none"));
  }});

  // Draw activity nodes
  const nodeGroup = container.append("g").attr("class", "nodes");
  const nodeMap = {{}};
  DATA.nodes.forEach(n => {{
    const pos = g.node(n.id);
    if (!pos) return;
    const w = Math.max(140, n.short_label.length * 8 + 30);
    const hw = w / 2;
    const ng = nodeGroup.append("g")
      .attr("class", "node state-normal")
      .attr("transform", `translate(${{pos.x - hw}},${{pos.y - 30}})`)
      .attr("data-id", n.id);
    ng.append("rect").attr("width", w).attr("height", 60);
    ng.append("text").attr("class", "gene-label")
      .attr("x", hw).attr("y", 22).attr("text-anchor", "middle").text(n.short_label);
    ng.append("text").attr("class", "func-label")
      .attr("x", hw).attr("y", 36).attr("text-anchor", "middle")
      .text(truncate(n.function_short || n.function, Math.floor(w / 6)));
    // State badge (hidden by default)
    ng.append("text").attr("class", "state-badge")
      .attr("x", hw).attr("y", 52).attr("text-anchor", "middle").text("");
    nodeMap[n.id] = ng;

    // Tooltip
    ng.on("mouseover", (event) => {{
      const tt = d3.select("#tooltip");
      tt.style("display", "block")
        .style("left", (event.pageX + 12) + "px")
        .style("top", (event.pageY - 10) + "px");
      const name = n.display_name || n.gene || n.complex || n.id.split(":")[1];
      const geneInfo = n.gene ? `${{n.gene}} (${{n.hgnc_id}})` : (n.complex || "");
      let html = `<div class="tt-title">${{name}}</div>`;
      if (geneInfo) html += `<div class="tt-subtitle">${{geneInfo}}</div>`;
      html += `<div class="tt-detail"><b>Function:</b> ${{n.function || "—"}}</div>`;
      if (n.function_id) html += `<div class="tt-detail" style="font-size:10px;color:#6c757d">${{n.function_id}}</div>`;
      if (n.substrate) html += `<div class="tt-detail"><b>Substrate:</b> ${{n.substrate}} (${{n.substrate_hgnc}})</div>`;
      html += `<div class="tt-detail"><b>Location:</b> ${{n.location || "—"}}</div>`;
      if (n.location_id) html += `<div class="tt-detail" style="font-size:10px;color:#6c757d">${{n.location_id}}</div>`;
      if (n.process) html += `<div class="tt-detail"><b>Process:</b> ${{n.process}}</div>`;
      if (n.process_id) html += `<div class="tt-detail" style="font-size:10px;color:#6c757d">${{n.process_id}}</div>`;
      // Show perturbation state if a hypothesis is selected
      const hgIdx = +document.getElementById("hg-select").value;
      const hg = DATA.hypothesis_groups[hgIdx];
      if (hg && hg.states[n.id]) {{
        const st = hg.states[n.id];
        const stClass = "tt-state tt-state-" + st.state;
        html += `<div class="tt-section">`;
        html += `<div class="tt-detail"><b>State:</b> <span class="${{stClass}}">${{st.state.replace(/_/g, " ")}}</span></div>`;
        if (st.is_primary) {{
          html += `<div class="tt-detail"><b>Role:</b> Primary mutation site</div>`;
          if (st.variant_class) html += `<div class="tt-detail"><b>Variant:</b> ${{st.variant_class}}</div>`;
          if (st.mechanism) html += `<div class="tt-detail"><b>Mechanism:</b> ${{st.mechanism.replace(/_/g, " ")}}</div>`;
        }} else {{
          html += `<div class="tt-detail"><b>Role:</b> Propagated from ${{st.cause ? nodeLabels[st.cause] || st.cause : "upstream"}}</div>`;
          if (st.provenance) html += `<div class="tt-detail"><b>Provenance:</b> ${{st.provenance.replace(/_/g, " ")}}</div>`;
        }}
        if (st.evidence_refs && st.evidence_refs.length) {{
          html += `<div class="tt-detail"><b>Evidence:</b></div>`;
          st.evidence_refs.forEach(r => {{ html += `<div class="tt-ref">📄 ${{r}}</div>`; }});
        }}
        if (st.evidence_snippet) html += `<div class="tt-evidence">"${{st.evidence_snippet}}"</div>`;
        html += `</div>`;
      }}
      html += `<div style="margin-top:6px;font-size:10px;color:#adb5bd">${{n.id}}</div>`;
      tt.html(html);
    }}).on("mouseout", () => d3.select("#tooltip").style("display", "none"));
  }});

  // Draw intermediate nodes
  (DATA.intermediate_nodes || []).forEach(n => {{
    const pos = g.node(n.id);
    if (!pos) return;
    const w = Math.max(130, n.short_label.length * 7 + 24);
    const hw = w / 2;
    const ng = nodeGroup.append("g")
      .attr("class", "intermediate-node")
      .attr("transform", `translate(${{pos.x - hw}},${{pos.y - 25}})`);
    ng.append("rect").attr("width", w).attr("height", 50);
    ng.append("text").attr("class", "gene-label")
      .attr("x", hw).attr("y", 18).attr("text-anchor", "middle")
      .text(n.short_label);
    ng.append("text").attr("class", "func-label")
      .attr("x", hw).attr("y", 30).attr("text-anchor", "middle")
      .text(truncate(n.process, Math.floor(w / 6)));
    // State badge
    const stateLabel = n.state ? n.state.replace(/_/g, " ") : "";
    ng.append("text").attr("class", "state-badge")
      .attr("x", hw).attr("y", 43).attr("text-anchor", "middle")
      .text(stateLabel);
    // Tooltip
    ng.on("mouseover", (event) => {{
      const tt = d3.select("#tooltip");
      tt.style("display", "block")
        .style("left", (event.pageX + 12) + "px")
        .style("top", (event.pageY - 10) + "px");
      let html = `<div class="tt-title">${{n.name}}</div>`;
      if (n.gene) html += `<div class="tt-subtitle">${{n.gene}} (${{n.hgnc_id}})</div>`;
      if (n.process) html += `<div class="tt-detail"><b>Process:</b> ${{n.process}}</div>`;
      if (n.process_id) html += `<div class="tt-detail" style="font-size:10px;color:#6c757d">${{n.process_id}}</div>`;
      if (n.state) {{
        const stClass = "tt-state tt-state-" + n.state;
        html += `<div class="tt-detail"><b>State:</b> <span class="${{stClass}}">${{n.state.replace(/_/g, " ")}}</span></div>`;
      }}
      // Driven by
      if (n.driven_by_labels && n.driven_by_labels.length) {{
        html += `<div class="tt-detail"><b>Driven by:</b> ${{n.driven_by_labels.join(", ")}}</div>`;
      }} else if (n.driven_by && n.driven_by.length === 0) {{
        html += `<div class="tt-detail"><b>Driven by:</b> convergence of upstream intermediates</div>`;
      }}
      // Route
      html += `<div class="tt-detail"><b>Route:</b> ${{n.route_name || n.route_id.replace(/_/g, " ")}}</div>`;
      // Tissue
      if (n.tissue) {{
        html += `<div class="tt-detail"><b>Tissue:</b> ${{n.tissue}}</div>`;
        const td = n.tissue_detail || {{}};
        let tissueIds = [];
        if (td.cell_type_id) tissueIds.push(td.cell_type_id);
        if (td.anatomy_id) tissueIds.push(td.anatomy_id);
        if (tissueIds.length) html += `<div class="tt-detail" style="font-size:10px;color:#6c757d">${{tissueIds.join(" / ")}}</div>`;
      }}
      // Route-level evidence
      if (n.route_evidence && n.route_evidence.length) {{
        html += `<div class="tt-section"><b>Evidence:</b>`;
        n.route_evidence.forEach(ev => {{
          html += `<div class="tt-ref">📄 ${{ev.reference}}</div>`;
          if (ev.snippet) html += `<div class="tt-evidence">"${{ev.snippet}}"</div>`;
        }});
        html += `</div>`;
      }}
      html += `<div style="margin-top:6px;font-size:10px;color:#adb5bd">${{n.id}}</div>`;
      tt.html(html);
    }}).on("mouseout", () => d3.select("#tooltip").style("display", "none"));
  }});

  // Draw phenotype nodes
  DATA.phenotype_routes.forEach(pr => {{
    const pid = "pheno:" + pr.id;
    const pos = g.node(pid);
    if (!pos) return;
    const ng = nodeGroup.append("g")
      .attr("class", "phenotype-node")
      .attr("transform", `translate(${{pos.x - 70}},${{pos.y - 20}})`);
    ng.append("rect").attr("width", 140).attr("height", 40);
    ng.append("text")
      .attr("x", 70).attr("y", 16).attr("text-anchor", "middle")
      .text(truncate(pr.phenotype_label, 20));
    ng.append("text")
      .attr("x", 70).attr("y", 30).attr("text-anchor", "middle")
      .style("font-size", "9px").style("fill", "#a17c10")
      .text(pr.phenotype_id);

    ng.on("mouseover", (event) => {{
      const tt = d3.select("#tooltip");
      tt.style("display", "block")
        .style("left", (event.pageX + 12) + "px")
        .style("top", (event.pageY - 10) + "px");
      let html = `<div class="tt-title">${{pr.phenotype_label}}</div>`;
      html += `<div class="tt-subtitle">${{pr.phenotype_id}}</div>`;
      html += `<div class="tt-detail"><b>Route:</b> ${{pr.name}}</div>`;
      if (pr.tissue) {{
        html += `<div class="tt-detail"><b>Tissue:</b> ${{pr.tissue}}</div>`;
        const td = pr.tissue_detail || {{}};
        let tissueIds = [];
        if (td.cell_type_id) tissueIds.push(td.cell_type_id);
        if (td.anatomy_id) tissueIds.push(td.anatomy_id);
        if (tissueIds.length) html += `<div class="tt-detail" style="font-size:10px;color:#6c757d">${{tissueIds.join(" / ")}}</div>`;
      }}
      html += `<div class="tt-detail" style="margin-top:6px">${{pr.description}}</div>`;
      // Show intermediates
      if (pr.intermediates && pr.intermediates.length) {{
        html += `<div class="tt-section"><b>Intermediates:</b>`;
        pr.intermediates.forEach(inter => {{
          html += `<div class="tt-detail">• ${{inter.name}}`;
          if (inter.gene) html += ` (${{inter.gene}})`;
          if (inter.process) html += ` — ${{inter.process}}`;
          html += `</div>`;
        }});
        html += `</div>`;
      }}
      // Route-level evidence
      if (pr.evidence && pr.evidence.length) {{
        html += `<div class="tt-section"><b>Evidence:</b>`;
        pr.evidence.forEach(ev => {{
          html += `<div class="tt-ref">📄 ${{ev.reference}}</div>`;
          if (ev.snippet) html += `<div class="tt-evidence">"${{ev.snippet}}"</div>`;
        }});
        html += `</div>`;
      }}
      tt.html(html);
    }}).on("mouseout", () => d3.select("#tooltip").style("display", "none"));
  }});

  // Store nodeMap for hypothesis switching
  window._nodeMap = nodeMap;
}}

function truncate(s, max) {{
  return s && s.length > max ? s.slice(0, max - 1) + "…" : (s || "");
}}

// --- Hypothesis group switching ---
function applyHypothesis(hgIdx) {{
  const hg = DATA.hypothesis_groups[hgIdx];
  const nodeMap = window._nodeMap;
  if (!nodeMap) return;

  // Reset all nodes
  DATA.nodes.forEach(n => {{
    const ng = nodeMap[n.id];
    if (!ng) return;
    ng.attr("class", "node state-normal");
    ng.select(".state-badge").text("");
  }});

  // Apply perturbation states
  Object.entries(hg.states).forEach(([nodeId, info]) => {{
    const ng = nodeMap[nodeId];
    if (!ng) return;
    let cls = "node state-" + info.state;
    if (info.is_primary) cls += " state-primary";
    ng.attr("class", cls);
    const label = info.state.replace(/_/g, " ");
    ng.select(".state-badge").text(info.is_primary ? "⬤ " + label : label);
  }});

  // Update info
  d3.select("#hg-info").html(
    `<b>${{hg.frequency}}</b> of cases. ${{hg.description}}`
  );
}}

// --- Init ---
document.addEventListener("DOMContentLoaded", () => {{
  const sel = d3.select("#hg-select");
  DATA.hypothesis_groups.forEach((hg, i) => {{
    sel.append("option").attr("value", i).text(hg.name);
  }});
  sel.on("change", function() {{ applyHypothesis(+this.value); }});

  render();
  if (DATA.hypothesis_groups.length > 0) applyHypothesis(0);
}});
</script>
</body>
</html>"""


def generate_html(disease_path: Path, output_path: Path | None = None) -> Path:
    disease = load_disease(disease_path)
    graph_data = build_graph_data(disease)

    html = HTML_TEMPLATE.format(
        disease_name=disease["name"],
        disease_term_id=disease.get("disease_term", {}).get("id", ""),
        disease_term_label=disease.get("disease_term", {}).get("label", ""),
        graph_json=json.dumps(graph_data, indent=2),
    )

    if output_path is None:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        output_path = OUTPUT_DIR / f"{disease['id']}.html"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html)
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Visualize pheno-CAM disease models")
    parser.add_argument("disease_file", nargs="?", help="Path to disease YAML file")
    parser.add_argument("-o", "--output", help="Output HTML path")
    parser.add_argument("--all", action="store_true", help="Visualize all disease files")
    args = parser.parse_args()

    if args.all:
        disease_dir = CAUSAL_DIR / "diseases"
        for f in sorted(disease_dir.glob("*.yaml")):
            out = generate_html(f)
            print(f"  {f.name} → {out}", file=sys.stderr)
        return

    if not args.disease_file:
        parser.error("Provide a disease YAML file or use --all")

    disease_path = Path(args.disease_file)
    output_path = Path(args.output) if args.output else None
    out = generate_html(disease_path, output_path)
    print(f"Generated: {out}", file=sys.stderr)


if __name__ == "__main__":
    main()
