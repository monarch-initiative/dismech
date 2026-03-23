# Pheno-CAM Visualization Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Redesign the Pheno-CAM visualization to use expandable module panels, hypothesis-colored edges propagating through the full graph, parallel edge rendering, and an always-visible hypothesis legend — replacing the current flat DAG with hypothesis dropdown.

**Architecture:** The existing `scripts/visualize_phenocam.py` generates self-contained HTML files with embedded D3.js + dagre. The redesign modifies both the Python data builder (`build_graph_data()`) and the JS rendering template. Python adds hypothesis ancestry computation to the JSON data; JS implements two-pass dagre layout, module panels, parallel colored edges, and collapse/expand. No new files are created — all changes are within `visualize_phenocam.py`.

**Tech Stack:** Python 3, PyYAML, D3.js v7, dagre 0.8.5

**Spec:** `docs/superpowers/specs/2026-03-23-phenocam-viz-redesign.md`

> **IMPORTANT — Python template string convention:** The HTML_TEMPLATE in `visualize_phenocam.py` uses Python `.format()` string interpolation. All JavaScript braces must be **doubled** (`{{` and `}}`) in the template string. The JS code snippets in this plan show the *intended JS output* with single braces. When inserting code into the template, double every `{` → `{{` and `}` → `}}`.

---

## File Map

All changes are in a single file:

- **Modify:** `scripts/visualize_phenocam.py`
  - Python: `build_graph_data()` (lines 48-750) — add hypothesis ancestry computation
  - Python: new helper `_compute_hypothesis_ancestry()` — graph traversal for edge coloring
  - JS: `layoutGraph()` (lines 1015-1051) — replace with two-pass layout
  - JS: `render()` (lines 1054-1527) — module panels, parallel edges, new legend
  - JS: `applyHypothesis()` (lines 1533-1566) — remove (replaced by always-visible multi-hypothesis)
  - CSS: (lines 812-935) — new panel styles, edge coloring, legend
  - HTML: (lines 937-965) — remove dropdown, add persistent legend

## Reference Files (read-only)

- `causal_models/diseases/Gorlin_Syndrome.yaml` — primary test case (2 hypotheses, 17 module activities, 4 disease-local activities, 8 routes)
- `causal_models/diseases/Noonan_Syndrome.yaml` — secondary test case (4 hypotheses, 1 module)
- `causal_models/diseases/Ehlers-Danlos_Syndrome_COL5A1.yaml` — simple test case (1 hypothesis)
- `causal_models/modules/hedgehog_signaling.yaml` — module with 17 activities, 22 edges
- `docs/superpowers/specs/2026-03-23-phenocam-viz-redesign.md` — design spec

---

## Task 1: Add Hypothesis Ancestry Computation to Python

Add a new function that computes, for every node and edge, which hypothesis(es) can reach it via the perturbation → propagation → driven_by chain. This data is needed for edge coloring in the JS.

**Files:**
- Modify: `scripts/visualize_phenocam.py` — add `_compute_hypothesis_ancestry()` and integrate into `build_graph_data()`

- [ ] **Step 1: Add `_compute_hypothesis_ancestry()` function**

Insert after the `_extract_tissue_detail()` function (after line 801). This function takes the graph data dict (nodes, edges, hypothesis_groups, intermediate_edges, phenotype_disease_edges) and returns a dict mapping each edge `(source, target)` tuple to a set of hypothesis IDs that can reach it.

```python
def _compute_hypothesis_ancestry(graph_data: dict) -> dict:
    """Compute which hypothesis(es) can reach each node via perturbation chains.

    Returns a dict mapping node_id -> set of hypothesis_ids that perturb it.
    """
    node_ancestry = {}  # node_id -> set of hypothesis_ids

    for hg in graph_data["hypothesis_groups"]:
        hg_id = hg["id"]
        # Seed: only primary perturbation nodes (not propagated states)
        perturbed_nodes = {
            nid for nid, info in hg["states"].items() if info["is_primary"]
        }

        # BFS forward through edges to find all reachable nodes
        visited = set()
        queue = list(perturbed_nodes)
        while queue:
            node = queue.pop(0)
            if node in visited:
                continue
            visited.add(node)
            node_ancestry.setdefault(node, set()).add(hg_id)
            # Find edges where this node is the source
            for e in graph_data["edges"]:
                if e["source"] == node and e["target"] not in visited:
                    queue.append(e["target"])
            for e in graph_data["intermediate_edges"]:
                if e["source"] == node and e["target"] not in visited:
                    queue.append(e["target"])
            for e in graph_data["phenotype_disease_edges"]:
                if e["source"] == node and e["target"] not in visited:
                    queue.append(e["target"])

    return node_ancestry
```

- [ ] **Step 2: Integrate into `build_graph_data()`**

At the end of `build_graph_data()`, before the `return` statement, add:

```python
    # Compute hypothesis ancestry for edge coloring
    result = {
        "disease_name": disease["name"],
        # ... (existing return dict construction)
    }
    node_ancestry = _compute_hypothesis_ancestry(result)

    # Annotate each edge with its hypothesis colors
    hg_ids = [hg["id"] for hg in result["hypothesis_groups"]]
    for e in result["edges"]:
        e["hypothesis_ids"] = sorted(node_ancestry.get(e["source"], set()) & set(hg_ids))
    for e in result["intermediate_edges"]:
        e["hypothesis_ids"] = sorted(node_ancestry.get(e["source"], set()) & set(hg_ids))
    for e in result["phenotype_disease_edges"]:
        e["hypothesis_ids"] = sorted(node_ancestry.get(e["source"], set()) & set(hg_ids))

    # Annotate nodes with hypothesis ancestry
    for n in result["nodes"]:
        n["hypothesis_ids"] = sorted(node_ancestry.get(n["id"], set()))
    for n in result["intermediate_nodes"]:
        n["hypothesis_ids"] = sorted(node_ancestry.get(n["id"], set()))

    # Add hypothesis color palette to data
    HYPOTHESIS_COLORS = ["#e74c3c", "#3498db", "#1abc9c", "#e67e22", "#9b59b6", "#2ecc71"]
    result["hypothesis_colors"] = {}
    for i, hg in enumerate(result["hypothesis_groups"]):
        result["hypothesis_colors"][hg["id"]] = HYPOTHESIS_COLORS[i % len(HYPOTHESIS_COLORS)]

    return result
```

Refactor the return statement: currently `build_graph_data()` constructs and returns a dict literal at line 737. Change it to build the dict into a `result` variable first, then run ancestry computation, then return `result`.

- [ ] **Step 3: Verify the visualization still generates**

Run:
```bash
uv run python scripts/visualize_phenocam.py causal_models/diseases/Gorlin_Syndrome.yaml
```
Expected: HTML file generated at `causal_models/viz/gorlin_syndrome.html` without errors. Open it to verify it still renders (the JS doesn't use the new fields yet, so it should look the same).

- [ ] **Step 4: Verify with all disease files**

Run:
```bash
uv run python scripts/visualize_phenocam.py --all
```
Expected: All 4 HTML files generated without errors.

- [ ] **Step 5: Commit**

```bash
git add scripts/visualize_phenocam.py
git commit -m "phenocam viz: add hypothesis ancestry computation for edge coloring"
```

---

## Task 2: Add Module Metadata to Graph Data

The JS needs to know which nodes belong to which module so it can group them into panels. Add module membership info and identify module boundary edges (edges that cross into/out of a module).

**Files:**
- Modify: `scripts/visualize_phenocam.py` — extend `build_graph_data()` return data

- [ ] **Step 1: Add module boundary data**

After the hypothesis ancestry computation (added in Task 1), add:

```python
    # Build module membership and boundary data for panel rendering
    module_nodes = {}  # module_id -> list of node IDs
    for n in result["nodes"]:
        if n["module_id"]:
            module_nodes.setdefault(n["module_id"], []).append(n["id"])

    # Identify module-internal edges (both source and target in same module)
    # vs boundary edges (source in module, target outside or vice versa)
    node_module = {}
    for n in result["nodes"]:
        if n["module_id"]:
            node_module[n["id"]] = n["module_id"]

    for e in result["edges"]:
        src_mod = node_module.get(e["source"])
        tgt_mod = node_module.get(e["target"])
        if src_mod and tgt_mod and src_mod == tgt_mod:
            e["edge_context"] = "module_internal"
            e["module_id"] = src_mod
        else:
            e["edge_context"] = "cross_boundary"
            e["module_id"] = None

    result["module_nodes"] = module_nodes
```

- [ ] **Step 2: Add perturbation-to-module target mapping**

For collapsed module port dots, the JS needs to know which internal activity each perturbation targets. Add to the hypothesis group data:

```python
    # Annotate perturbation targets for port dot rendering
    for hg in result["hypothesis_groups"]:
        hg["perturbation_targets"] = []
        for raw_hg in disease.get("hypothesis_groups", []):
            if raw_hg["id"] == hg["id"]:
                for p in raw_hg.get("perturbations", []):
                    hg["perturbation_targets"].append(p["target_activity"])
                break
```

- [ ] **Step 3: Identify module output nodes**

Nodes inside a module that have edges to nodes outside the module — these become right-side port dots when collapsed:

```python
    # Identify module output nodes (have edges leaving the module)
    module_outputs = {}  # module_id -> list of {node_id, short_label}
    for mod_id, node_ids in module_nodes.items():
        node_set = set(node_ids)
        outputs = set()
        # Check module edges
        for e in result["edges"]:
            if e["source"] in node_set and e["target"] not in node_set:
                outputs.add(e["source"])
        # Check cross-boundary driven_by edges
        for e in result["intermediate_edges"]:
            if e["source"] in node_set:
                outputs.add(e["source"])
        # Also check disease-local activity driven_by (edges from module to local activities)
        for e in result["edges"]:
            if e["edge_context"] == "cross_boundary" and e["source"] in node_set:
                outputs.add(e["source"])

        node_label_map = {n["id"]: n["short_label"] for n in result["nodes"]}
        module_outputs[mod_id] = [
            {"id": nid, "label": node_label_map.get(nid, nid)}
            for nid in sorted(outputs)
        ]
    result["module_outputs"] = module_outputs
```

- [ ] **Step 4: Verify generation still works**

Run:
```bash
uv run python scripts/visualize_phenocam.py --all
```
Expected: All HTML files generated without errors.

- [ ] **Step 5: Commit**

```bash
git add scripts/visualize_phenocam.py
git commit -m "phenocam viz: add module membership and boundary data for panel rendering"
```

---

## Task 3: Implement Two-Pass Dagre Layout in JS

Replace the current single-pass `layoutGraph()` with a two-pass approach: (1) layout each module's internal graph, (2) layout the outer graph using computed module bounding boxes.

**Files:**
- Modify: `scripts/visualize_phenocam.py` — replace `layoutGraph()` JS function in HTML_TEMPLATE

- [ ] **Step 1: Replace `layoutGraph()` with two-pass implementation**

Replace the existing `layoutGraph(data)` function (lines 1015-1051) with:

```javascript
// Layout constants (module-level)
const PANEL_PADDING = 20;
const PANEL_HEADER_HEIGHT = 30;

// Module collapse state
const _moduleState = {};  // module_id -> "expanded" | "collapsed"

function initModuleState(data) {
  (data.modules || []).forEach(m => {
    _moduleState[m.id] = "expanded";
  });
}

function toggleModule(moduleId) {
  _moduleState[moduleId] = _moduleState[moduleId] === "expanded" ? "collapsed" : "expanded";
  render();
}

function layoutGraph(data) {
  // Pass 1: Layout each expanded module's internal graph
  const moduleLayouts = {};

  (data.modules || []).forEach(mod => {
    const modNodes = (data.module_nodes || {})[mod.id] || [];
    if (_moduleState[mod.id] !== "expanded" || modNodes.length === 0) return;

    const mg = new dagre.graphlib.Graph();
    mg.setGraph({ rankdir: "LR", ranksep: 60, nodesep: 30, marginx: PANEL_PADDING, marginy: PANEL_PADDING });
    mg.setDefaultEdgeLabel(() => ({}));

    // Add module-internal nodes
    const modNodeSet = new Set(modNodes);
    data.nodes.filter(n => modNodeSet.has(n.id)).forEach(n => {
      const w = Math.max(140, n.short_label.length * 8 + 30);
      mg.setNode(n.id, { label: n.short_label, width: w, height: 60 });
    });

    // Add module-internal edges
    data.edges.filter(e => e.module_id === mod.id).forEach(e => {
      if (mg.hasNode(e.source) && mg.hasNode(e.target)) {
        mg.setEdge(e.source, e.target);
      }
    });

    dagre.layout(mg);
    const gInfo = mg.graph();
    moduleLayouts[mod.id] = {
      graph: mg,
      width: gInfo.width + PANEL_PADDING * 2,
      height: gInfo.height + PANEL_PADDING * 2 + PANEL_HEADER_HEIGHT,
    };
  });

  // Pass 2: Layout outer graph
  const og = new dagre.graphlib.Graph();
  og.setGraph({ rankdir: "LR", ranksep: 80, nodesep: 40, marginx: 40, marginy: 40 });
  og.setDefaultEdgeLabel(() => ({}));

  // Add module panels as single large nodes (expanded) or bars (collapsed)
  const moduleNodeIds = new Set();
  (data.modules || []).forEach(mod => {
    const modNodes = (data.module_nodes || {})[mod.id] || [];
    modNodes.forEach(nid => moduleNodeIds.add(nid));

    if (_moduleState[mod.id] === "expanded" && moduleLayouts[mod.id]) {
      const ml = moduleLayouts[mod.id];
      og.setNode("module:" + mod.id, {
        label: mod.name,
        width: ml.width,
        height: ml.height,
      });
    } else {
      // Collapsed: fixed bar size, height grows with port count
      const outputs = (data.module_outputs || {})[mod.id] || [];
      const portCount = Math.max(outputs.length, 2);
      og.setNode("module:" + mod.id, {
        label: mod.name,
        width: 260,
        height: Math.max(40, portCount * 14 + 20),
      });
    }
  });

  // Add edges from perturbation nodes to module panels
  // (perturbation targets are inside modules — route to the module node)
  const nodeToModule = {};
  data.nodes.forEach(n => { if (n.module_id) nodeToModule[n.id] = n.module_id; });

  // Add free-flowing nodes (non-module)
  data.nodes.filter(n => !moduleNodeIds.has(n.id)).forEach(n => {
    const w = Math.max(140, n.short_label.length * 8 + 30);
    og.setNode(n.id, { label: n.short_label, width: w, height: 60 });
  });

  // Add intermediate nodes
  (data.intermediate_nodes || []).forEach(n => {
    const w = Math.max(130, n.short_label.length * 7 + 24);
    og.setNode(n.id, { label: n.short_label, width: w, height: 50 });
  });

  // Add phenotype nodes
  data.phenotype_routes.forEach(pr => {
    const pid = "pheno:" + pr.id;
    og.setNode(pid, { label: pr.phenotype_label, width: 140, height: 54 });
  });

  // Add disease node
  if (data.disease_node) {
    og.setNode(data.disease_node.id, { label: data.disease_node.name, width: 180, height: 54 });
  }

  // Add outer edges: cross-boundary module edges route to/from module panel node
  data.edges.forEach(e => {
    if (e.edge_context === "module_internal") return;  // handled inside module
    const src = moduleNodeIds.has(e.source) ? "module:" + nodeToModule[e.source] : e.source;
    const tgt = moduleNodeIds.has(e.target) ? "module:" + nodeToModule[e.target] : e.target;
    if (og.hasNode(src) && og.hasNode(tgt)) og.setEdge(src, tgt);
  });

  // Add intermediate edges
  (data.intermediate_edges || []).forEach(e => {
    const src = moduleNodeIds.has(e.source) ? "module:" + nodeToModule[e.source] : e.source;
    const tgt = moduleNodeIds.has(e.target) ? "module:" + nodeToModule[e.target] : e.target;
    if (og.hasNode(src) && og.hasNode(tgt)) og.setEdge(src, tgt);
  });

  // Add phenotype-disease edges
  (data.phenotype_disease_edges || []).forEach(e => {
    if (og.hasNode(e.source) && og.hasNode(e.target)) og.setEdge(e.source, e.target);
  });

  dagre.layout(og);

  return { outer: og, modules: moduleLayouts, moduleNodeIds };
}
```

- [ ] **Step 2: Verify the template is syntactically valid**

Run:
```bash
uv run python scripts/visualize_phenocam.py causal_models/diseases/Gorlin_Syndrome.yaml
```
Expected: HTML file generates without Python errors. (The `render()` function still references old layout, so the viz may be broken — that's fine, we fix it in Task 4.)

- [ ] **Step 3: Commit**

```bash
git add scripts/visualize_phenocam.py
git commit -m "phenocam viz: implement two-pass dagre layout for module panels"
```

---

## Task 4: Rewrite `render()` — Module Panels and Free-Flowing Nodes

Replace the existing `render()` function with the new version that draws module panels (expanded/collapsed) and positions free-flowing nodes using the two-pass layout.

**Files:**
- Modify: `scripts/visualize_phenocam.py` — replace `render()` JS function

- [ ] **Step 1: Write the new `render()` function skeleton**

Replace the existing `render()` function. This is a large replacement — the new function handles:
1. Layout computation via two-pass `layoutGraph()`
2. SVG setup (zoom, fit-to-view, arrow markers)
3. Module panel backgrounds (expanded: bordered rect with header; collapsed: bar with port dots)
4. Module-internal nodes and edges (positioned within panel)
5. Free-flowing nodes (perturbation, disease-local, intermediate, phenotype, disease)
6. All edge types with hypothesis coloring and dash patterns
7. Click handler on module panel headers for collapse/expand

The full replacement is long. Structure the function as:

```javascript
function render() {
  const svg = d3.select("svg");
  svg.selectAll("*").remove();

  const layout = layoutGraph(DATA);
  const og = layout.outer;
  const moduleLayouts = layout.modules;
  const moduleNodeIds = layout.moduleNodeIds;
  const graphInfo = og.graph();

  // Zoom/pan setup (same as current)
  const zoom = d3.zoom().scaleExtent([0.3, 3]).on("zoom", (e) => {
    container.attr("transform", e.transform);
  });
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

  // Arrow markers — define per hypothesis color + gray
  const defs = svg.append("defs");
  defineArrowMarkers(defs);

  // Build label lookups
  const nodeLabels = {};
  DATA.nodes.forEach(n => { nodeLabels[n.id] = n.short_label; });
  (DATA.intermediate_nodes || []).forEach(n => { nodeLabels[n.id] = n.short_label; });

  const edgeGroup = container.append("g").attr("class", "edges");
  const nodeGroup = container.append("g").attr("class", "nodes");
  const nodeMap = {};

  // --- Draw module panels ---
  drawModulePanels(container, og, moduleLayouts, nodeGroup, edgeGroup, nodeLabels, nodeMap);

  // --- Draw free-flowing nodes ---
  drawFreeNodes(og, nodeGroup, nodeLabels, nodeMap);

  // --- Draw all edges ---
  drawEdges(og, moduleLayouts, edgeGroup, nodeLabels, moduleNodeIds);

  // --- Draw intermediate nodes ---
  drawIntermediateNodes(og, nodeGroup, nodeLabels, nodeMap);

  // --- Draw phenotype nodes ---
  drawPhenotypeNodes(og, nodeGroup, nodeLabels);

  // --- Draw disease node ---
  drawDiseaseNode(og, nodeGroup);

  // --- Draw phenotype → disease edges ---
  drawPhenotypeDiseaseEdges(og, edgeGroup, nodeLabels);

  window._nodeMap = nodeMap;
  applyAllHypotheses();
}
```

Then implement each `draw*` helper as a separate function. Each helper is responsible for one visual element type. This keeps the render function readable.

- [ ] **Step 2: Implement `drawModulePanels()`**

This function draws module panels (expanded or collapsed) and their contents:

```javascript
function drawModulePanels(container, og, moduleLayouts, nodeGroup, edgeGroup, nodeLabels, nodeMap) {
  (DATA.modules || []).forEach(mod => {
    const modNodeId = "module:" + mod.id;
    const outerPos = og.node(modNodeId);
    if (!outerPos) return;

    const isExpanded = _moduleState[mod.id] === "expanded";
    const panelG = container.append("g").attr("class", "module-panel");

    if (isExpanded && moduleLayouts[mod.id]) {
      const ml = moduleLayouts[mod.id];
      const px = outerPos.x - ml.width / 2;
      const py = outerPos.y - ml.height / 2;

      // Panel background
      panelG.append("rect")
        .attr("x", px).attr("y", py)
        .attr("width", ml.width).attr("height", ml.height)
        .attr("rx", 10).attr("fill", "#fafbff")
        .attr("stroke", "#8090c0").attr("stroke-width", 2);

      // Panel header (clickable)
      const headerG = panelG.append("g")
        .attr("class", "module-header")
        .style("cursor", "pointer")
        .on("click", () => toggleModule(mod.id));

      headerG.append("rect")
        .attr("x", px).attr("y", py)
        .attr("width", ml.width).attr("height", 26)
        .attr("rx", 10).attr("fill", "#e8ecf8");

      headerG.append("text")
        .attr("x", px + 12).attr("y", py + 18)
        .attr("font-size", "10px").attr("font-weight", "700").attr("fill", "#3050a0")
        .text("▼ " + mod.name);

      headerG.append("text")
        .attr("x", px + ml.width - 12).attr("y", py + 18)
        .attr("font-size", "9px").attr("fill", "#8090c0").attr("text-anchor", "end")
        .text((DATA.module_nodes[mod.id] || []).length + " activities");

      // Draw internal nodes at translated positions
      const mg = ml.graph;
      const modNodeSet = new Set((DATA.module_nodes || {})[mod.id] || []);
      DATA.nodes.filter(n => modNodeSet.has(n.id)).forEach(n => {
        const ipos = mg.node(n.id);
        if (!ipos) return;
        // Translate internal position to global SVG coordinates
        const nx = px + ipos.x;
        const ny = py + PANEL_HEADER_HEIGHT + ipos.y;
        const w = Math.max(140, n.short_label.length * 8 + 30);
        const hw = w / 2;

        const ng = nodeGroup.append("g")
          .attr("class", "node state-normal")
          .attr("transform", `translate(${nx - hw},${ny - 30})`)
          .attr("data-id", n.id);
        ng.append("rect").attr("width", w).attr("height", 60);
        ng.append("text").attr("class", "gene-label")
          .attr("x", hw).attr("y", 22).attr("text-anchor", "middle").text(n.short_label);
        ng.append("text").attr("class", "func-label")
          .attr("x", hw).attr("y", 36).attr("text-anchor", "middle")
          .text(truncate(n.function_short || n.function, Math.floor(w / 6)));
        ng.append("text").attr("class", "state-badge")
          .attr("x", hw).attr("y", 52).attr("text-anchor", "middle").text("");
        nodeMap[n.id] = ng;
        // Store global position for edge routing
        n._gx = nx;
        n._gy = ny;

        // Attach tooltip (reuse existing tooltip logic)
        attachActivityTooltip(ng, n, nodeLabels);
      });

      // Draw module-internal edges
      DATA.edges.filter(e => e.module_id === mod.id).forEach(e => {
        const srcPos = mg.node(e.source);
        const tgtPos = mg.node(e.target);
        if (!srcPos || !tgtPos) return;
        // Translate to global coords
        const pts = mg.edge(e.source, e.target);
        if (!pts || !pts.points) return;
        const globalPts = pts.points.map(p => ({
          x: px + p.x,
          y: py + PANEL_HEADER_HEIGHT + p.y
        }));
        drawSingleEdge(edgeGroup, globalPts, e, nodeLabels, "solid");
      });

    } else {
      // Collapsed: draw summary bar
      const barW = outerPos.width || 260;
      const barH = outerPos.height || 40;
      const bx = outerPos.x - barW / 2;
      const by = outerPos.y - barH / 2;

      const barG = panelG.append("g")
        .style("cursor", "pointer")
        .on("click", () => toggleModule(mod.id));

      barG.append("rect")
        .attr("x", bx).attr("y", by)
        .attr("width", barW).attr("height", barH)
        .attr("rx", 10).attr("fill", "#e8ecf8")
        .attr("stroke", "#8090c0").attr("stroke-width", 2);

      barG.append("text")
        .attr("x", bx + 12).attr("y", by + barH / 2 + 4)
        .attr("font-size", "10px").attr("font-weight", "700").attr("fill", "#3050a0")
        .text("▶ " + mod.name);

      barG.append("text")
        .attr("x", bx + barW - 12).attr("y", by + barH / 2 + 4)
        .attr("font-size", "9px").attr("fill", "#8090c0").attr("text-anchor", "end")
        .text((DATA.module_nodes[mod.id] || []).length + " activities");

      // Left port dots (perturbation entry points, colored by hypothesis)
      const hgColors = DATA.hypothesis_colors || {};
      let leftPortY = by + 8;
      DATA.hypothesis_groups.forEach(hg => {
        const targets = hg.perturbation_targets || [];
        const modNodes = new Set((DATA.module_nodes || {})[mod.id] || []);
        const hasEntry = targets.some(t => modNodes.has(t));
        if (hasEntry) {
          barG.append("circle")
            .attr("cx", bx).attr("cy", leftPortY + 6)
            .attr("r", 4)
            .attr("fill", hgColors[hg.id] || "#999")
            .attr("stroke", "white").attr("stroke-width", 1);
          leftPortY += 14;
        }
      });

      // Right port dots (output activities)
      const outputs = (DATA.module_outputs || {})[mod.id] || [];
      let rightPortY = by + 8;
      outputs.forEach(out => {
        barG.append("circle")
          .attr("cx", bx + barW).attr("cy", rightPortY + 6)
          .attr("r", 4)
          .attr("fill", "#28a745")
          .attr("stroke", "white").attr("stroke-width", 1);
        barG.append("text")
          .attr("x", bx + barW + 8).attr("y", rightPortY + 10)
          .attr("font-size", "7px").attr("fill", "#6c757d")
          .text(out.label);
        rightPortY += 14;
      });
    }
  });
}
```

- [ ] **Step 3: Implement `drawFreeNodes()`**

Draw perturbation nodes (with hypothesis-colored borders and frequency badges) and disease-local activity nodes:

```javascript
function drawFreeNodes(og, nodeGroup, nodeLabels, nodeMap) {
  const hgColors = DATA.hypothesis_colors || {};
  const moduleNodeIds = new Set();
  Object.values(DATA.module_nodes || {}).forEach(ids => ids.forEach(id => moduleNodeIds.add(id)));

  DATA.nodes.filter(n => !moduleNodeIds.has(n.id)).forEach(n => {
    const pos = og.node(n.id);
    if (!pos) return;
    const w = Math.max(140, n.short_label.length * 8 + 30);
    const hw = w / 2;

    // Check if this is a perturbation entry node
    let isPerturbation = false;
    let pertHgId = null;
    let pertFreq = "";
    let pertVariant = "";
    DATA.hypothesis_groups.forEach(hg => {
      if (hg.states[n.id] && hg.states[n.id].is_primary) {
        isPerturbation = true;
        pertHgId = hg.id;
        pertFreq = hg.frequency;
        pertVariant = hg.states[n.id].variant_class;
      }
    });

    const baseClass = n.type === "local_activity" ? "node local-activity state-normal" : "node state-normal";
    const ng = nodeGroup.append("g")
      .attr("class", baseClass)
      .attr("transform", `translate(${pos.x - hw},${pos.y - 30})`)
      .attr("data-id", n.id);

    ng.append("rect").attr("width", w).attr("height", 60);

    if (isPerturbation && pertHgId) {
      // Override border with hypothesis color
      ng.select("rect")
        .attr("stroke", hgColors[pertHgId] || "#999")
        .attr("stroke-width", 2.5);
      // Frequency badge
      if (pertFreq) {
        ng.append("rect")
          .attr("x", w - 36).attr("y", 2).attr("width", 34).attr("height", 14)
          .attr("rx", 7).attr("fill", hgColors[pertHgId] || "#999");
        ng.append("text")
          .attr("x", w - 19).attr("y", 12)
          .attr("text-anchor", "middle").attr("font-size", "7px")
          .attr("fill", "white").attr("font-weight", "600")
          .text(pertFreq);
      }
    }

    ng.append("text").attr("class", "gene-label")
      .attr("x", hw).attr("y", 22).attr("text-anchor", "middle").text(n.short_label);
    ng.append("text").attr("class", "func-label")
      .attr("x", hw).attr("y", 36).attr("text-anchor", "middle")
      .text(truncate(n.function_short || n.function, Math.floor(w / 6)));
    ng.append("text").attr("class", "state-badge")
      .attr("x", hw).attr("y", 52).attr("text-anchor", "middle").text("");
    nodeMap[n.id] = ng;
    n._gx = pos.x;
    n._gy = pos.y;

    attachActivityTooltip(ng, n, nodeLabels);
  });
}
```

- [ ] **Step 4: Implement edge drawing with hypothesis colors and parallel offsets**

```javascript
function drawSingleEdge(edgeGroup, points, edgeData, nodeLabels, dashStyle) {
  const hypothesisIds = edgeData.hypothesis_ids || [];
  const hgColors = DATA.hypothesis_colors || {};
  const isNeg = edgeData.relation_id === "RO:0002630" || edgeData.relation_id === "RO:0002305";

  // Determine dash pattern
  let strokeDash = "";
  if (dashStyle === "dashed") strokeDash = "6,3";
  else if (dashStyle === "dotted") strokeDash = "2,3";

  if (hypothesisIds.length === 0) {
    // Unperturbed edge: gray
    const line = d3.line().x(d => d.x).y(d => d.y).curve(d3.curveBasis);
    const eg = edgeGroup.append("g").attr("class", "edge");
    const pathD = line(points);
    eg.append("path")
      .attr("d", pathD)
      .attr("stroke", "#ccc")
      .attr("stroke-width", 1)
      .attr("fill", "none")
      .attr("stroke-dasharray", strokeDash)
      .attr("marker-end", isNeg ? "url(#tbar-gray)" : "url(#arrow-gray)");
    eg.append("path").attr("class", "edge-hover").attr("d", pathD);
    attachEdgeTooltip(eg, edgeData, nodeLabels);
    return;
  }

  // Hypothesis-colored edges: draw parallel offset lines
  const numLines = hypothesisIds.length;
  const OFFSET = 2;  // px between parallel lines
  const totalSpread = (numLines - 1) * OFFSET;

  hypothesisIds.forEach((hgId, idx) => {
    const offset = -totalSpread / 2 + idx * OFFSET;
    const color = hgColors[hgId] || "#999";
    const offsetPts = offsetPath(points, offset);
    const line = d3.line().x(d => d.x).y(d => d.y).curve(d3.curveBasis);
    const eg = edgeGroup.append("g").attr("class", "edge");
    const pathD = line(offsetPts);
    eg.append("path")
      .attr("d", pathD)
      .attr("stroke", color)
      .attr("stroke-width", 1.5)
      .attr("fill", "none")
      .attr("stroke-dasharray", strokeDash)
      .attr("marker-end", isNeg ? `url(#tbar-${hgId})` : `url(#arrow-${hgId})`);
    if (idx === 0) {
      // Only add hover target and tooltip once per edge group
      eg.append("path").attr("class", "edge-hover").attr("d", pathD);
      attachEdgeTooltip(eg, edgeData, nodeLabels);
    }
  });
}

function offsetPath(points, offset) {
  if (offset === 0 || points.length < 2) return points;
  return points.map((p, i) => {
    // Compute perpendicular direction at this point
    let dx, dy;
    if (i === 0) {
      dx = points[1].x - p.x;
      dy = points[1].y - p.y;
    } else if (i === points.length - 1) {
      dx = p.x - points[i - 1].x;
      dy = p.y - points[i - 1].y;
    } else {
      dx = points[i + 1].x - points[i - 1].x;
      dy = points[i + 1].y - points[i - 1].y;
    }
    const len = Math.sqrt(dx * dx + dy * dy) || 1;
    // Perpendicular unit vector
    const px = -dy / len;
    const py = dx / len;
    return { x: p.x + px * offset, y: p.y + py * offset };
  });
}
```

- [ ] **Step 5: Implement `drawEdges()` — the main edge drawing dispatcher**

This function iterates all edge types, resolves positions, selects dash style, and delegates to `drawSingleEdge()`:

```javascript
function drawEdges(og, moduleLayouts, edgeGroup, nodeLabels, moduleNodeIds) {
  const nodeToModule = {};
  DATA.nodes.forEach(n => { if (n.module_id) nodeToModule[n.id] = n.module_id; });

  // Module-internal edges are drawn inside drawModulePanels() — skip them here

  // Cross-boundary module edges (source or target outside module)
  DATA.edges.filter(e => e.edge_context !== "module_internal").forEach(e => {
    const srcId = moduleNodeIds.has(e.source) ? "module:" + nodeToModule[e.source] : e.source;
    const tgtId = moduleNodeIds.has(e.target) ? "module:" + nodeToModule[e.target] : e.target;
    const pts = og.edge(srcId, tgtId);
    if (!pts || !pts.points) return;
    drawSingleEdge(edgeGroup, pts.points, e, nodeLabels, "solid");
  });

  // Intermediate edges (activity→intermediate, intermediate→intermediate, intermediate→phenotype)
  (DATA.intermediate_edges || []).forEach(e => {
    const srcId = moduleNodeIds.has(e.source) ? "module:" + nodeToModule[e.source] : e.source;
    const tgtId = moduleNodeIds.has(e.target) ? "module:" + nodeToModule[e.target] : e.target;
    const pts = og.edge(srcId, tgtId);
    if (!pts || !pts.points) return;
    // Determine dash style from edge type
    const dashStyle = e.edge_type === "intermediate_to_phenotype" ? "dashed" : "solid";
    drawSingleEdge(edgeGroup, pts.points, e, nodeLabels, dashStyle);
  });
}

function drawPhenotypeDiseaseEdges(og, edgeGroup, nodeLabels) {
  (DATA.phenotype_disease_edges || []).forEach(e => {
    const pts = og.edge(e.source, e.target);
    if (!pts || !pts.points) return;
    drawSingleEdge(edgeGroup, pts.points, e, nodeLabels, "dotted");
  });
}
```

- [ ] **Step 6: Implement arrow marker definitions per hypothesis color**

```javascript
function defineArrowMarkers(defs) {
  const hgColors = DATA.hypothesis_colors || {};

  // Gray markers for unperturbed edges
  _defineArrow(defs, "arrow-gray", "#ccc");
  _defineTBar(defs, "tbar-gray", "#ccc");

  // Per-hypothesis markers
  Object.entries(hgColors).forEach(([hgId, color]) => {
    _defineArrow(defs, `arrow-${hgId}`, color);
    _defineTBar(defs, `tbar-${hgId}`, color);
  });

  // Disease edge markers
  _defineArrow(defs, "arrow-disease", "#0d6efd");
}

function _defineArrow(defs, id, color) {
  defs.append("marker")
    .attr("id", id).attr("viewBox", "0 0 10 10")
    .attr("refX", 10).attr("refY", 5)
    .attr("markerWidth", 8).attr("markerHeight", 8)
    .attr("orient", "auto")
    .append("path").attr("d", "M 0 0 L 10 5 L 0 10 z").attr("fill", color);
}

function _defineTBar(defs, id, color) {
  defs.append("marker")
    .attr("id", id).attr("viewBox", "0 0 10 10")
    .attr("refX", 5).attr("refY", 5)
    .attr("markerWidth", 8).attr("markerHeight", 10)
    .attr("orient", "auto")
    .append("line")
    .attr("x1", 5).attr("y1", 0).attr("x2", 5).attr("y2", 10)
    .attr("stroke", color).attr("stroke-width", 2);
}
```

- [ ] **Step 7: Implement `applyAllHypotheses()` replacing the old dropdown-based approach**

```javascript
function applyAllHypotheses() {
  const nodeMap = window._nodeMap;
  if (!nodeMap) return;
  const hgColors = DATA.hypothesis_colors || {};

  // Reset all module nodes to normal
  DATA.nodes.forEach(n => {
    const ng = nodeMap[n.id];
    if (!ng) return;
    const base = n.type === "local_activity" ? "node local-activity" : "node";
    ng.attr("class", base + " state-normal");
    ng.select(".state-badge").text("");
  });

  // Collect all states across all hypotheses
  // If hypotheses agree on state, show that state
  // If they disagree, show split
  const nodeStates = {};  // node_id -> { hg_id: state_info }
  DATA.hypothesis_groups.forEach(hg => {
    Object.entries(hg.states).forEach(([nodeId, info]) => {
      if (!nodeStates[nodeId]) nodeStates[nodeId] = {};
      nodeStates[nodeId][hg.id] = info;
    });
  });

  Object.entries(nodeStates).forEach(([nodeId, hgStates]) => {
    const ng = nodeMap[nodeId];
    if (!ng) return;
    const nodeType = DATA.nodes.find(n => n.id === nodeId);
    const base = nodeType && nodeType.type === "local_activity" ? "node local-activity" : "node";

    const states = Object.values(hgStates);
    const uniqueStates = [...new Set(states.map(s => s.state))];

    if (uniqueStates.length === 1) {
      // All hypotheses agree
      const state = uniqueStates[0];
      const isPrimary = states.some(s => s.is_primary);
      let cls = base + " state-" + state;
      if (isPrimary) cls += " state-primary";
      ng.attr("class", cls);
      const label = state.replace(/_/g, " ");
      ng.select(".state-badge").text(isPrimary ? "● " + label : label);
    } else {
      // Disagreement: apply the most severe state for the CSS class,
      // but show split badge
      ng.attr("class", base + " state-split");
      const labels = Object.entries(hgStates).map(([hgId, info]) => {
        const color = hgColors[hgId] || "#999";
        return info.state.replace(/_/g, " ");
      }).join(" / ");
      ng.select(".state-badge").text(labels);
    }
  });
}
```

- [ ] **Step 8: Implement remaining draw helpers (drawIntermediateNodes, drawPhenotypeNodes, drawDiseaseNode, tooltip extractors)**

Implement `drawIntermediateNodes()`, `drawPhenotypeNodes()`, `drawDiseaseNode()` — these are largely carried forward from the current `render()` function (lines 1305-1523) but use the outer dagre layout (`og`) for positions instead of the old single `g`.

Also extract the existing inline tooltip code into reusable functions:
- `attachActivityTooltip(ng, nodeData, nodeLabels)` — extract from current lines 1253-1302
- `attachEdgeTooltip(eg, edgeData, nodeLabels)` — extract from current lines 1137-1170

**Important:** Preserve the existing `truncate(s, max)` function (current line 1529-1531) — it is used throughout the draw helpers.

The key changes from current:
- Use `og.node(id)` for positions instead of `g.node(id)`
- Tooltip for activities now shows per-hypothesis state breakdown (implemented in Task 7 Step 2) instead of single-hypothesis lookup via dropdown

- [ ] **Step 9: Verify Gorlin renders correctly**

Run:
```bash
uv run python scripts/visualize_phenocam.py causal_models/diseases/Gorlin_Syndrome.yaml
```
Open `causal_models/viz/gorlin_syndrome.html` in a browser. Verify:
- Module panel is visible with header "▼ Hedgehog Signaling"
- Internal module nodes are inside the panel
- Perturbation nodes (PTCH1, SUFU) are to the left with colored borders
- Edges show hypothesis colors (red for PTCH1, blue for SUFU)
- Disease activities, intermediates, phenotypes flow freely to the right
- Clicking module header collapses to summary bar
- Tooltips still work on hover/click

- [ ] **Step 10: Verify all diseases render**

Run:
```bash
uv run python scripts/visualize_phenocam.py --all
```
Open each HTML file and verify basic rendering.

- [ ] **Step 11: Commit**

```bash
git add scripts/visualize_phenocam.py
git commit -m "phenocam viz: rewrite render with module panels, hypothesis colors, parallel edges"
```

---

## Task 5: Update CSS and HTML Structure

Replace the hypothesis dropdown with a persistent legend, update CSS for module panels and new edge/node styles.

**Files:**
- Modify: `scripts/visualize_phenocam.py` — CSS and HTML sections of HTML_TEMPLATE

- [ ] **Step 1: Add module panel CSS**

Add to the `<style>` section:

```css
.module-panel rect { cursor: default; }
.module-header { cursor: pointer; }
.module-header:hover rect { fill: #dde0f0; }

.state-split rect {
  fill: #f0e6ff;
  stroke: #9b59b6;
  stroke-width: 2;
  stroke-dasharray: 4,2;
}
```

- [ ] **Step 2: Replace hypothesis dropdown with persistent legend**

Replace the `#controls` and `#hg-select` HTML with a persistent legend in the `#header`:

```html
<div id="header">
  <div>
    <h1>Pheno-CAM: {disease_name}</h1>
    <span class="disease-term">{disease_term_id} &mdash; {disease_term_label}</span>
  </div>
  <div id="hypothesis-legend"></div>
</div>
```

Add CSS for the legend:

```css
#hypothesis-legend {
  display: flex; align-items: center; gap: 16px; flex-wrap: wrap;
  font-size: 12px;
}
.hg-legend-item {
  display: flex; align-items: center; gap: 6px;
}
.hg-legend-swatch {
  width: 24px; height: 3px; border-radius: 2px;
}
.hg-legend-freq {
  font-size: 10px; color: #6c757d;
}
```

- [ ] **Step 3: Populate legend in JS init**

Replace the DOMContentLoaded handler:

```javascript
document.addEventListener("DOMContentLoaded", () => {
  const hgColors = DATA.hypothesis_colors || {};
  const legendEl = document.getElementById("hypothesis-legend");
  DATA.hypothesis_groups.forEach(hg => {
    const color = hgColors[hg.id] || "#999";
    const item = document.createElement("div");
    item.className = "hg-legend-item";
    item.innerHTML = `<div class="hg-legend-swatch" style="background:${color}"></div>`
      + `<span>${hg.name}</span>`
      + (hg.frequency ? `<span class="hg-legend-freq">(${hg.frequency})</span>` : "");
    legendEl.appendChild(item);
  });

  initModuleState(DATA);
  render();
});
```

- [ ] **Step 4: Remove old `applyHypothesis()` and dropdown code**

Remove:
- The `#controls` div with `<select id="hg-select">`
- The `#hg-info` div
- The old `applyHypothesis(hgIdx)` function
- The old DOMContentLoaded handler that populated the dropdown

- [ ] **Step 5: Update the bottom-left legend**

Update the existing `#legend` box to only show node type and state explanations (remove the items that are now covered by the hypothesis legend in the header):

Keep: perturbation state swatches (normal, increased, decreased, absent, etc.), module panel, process/intermediate, phenotype, disease node explanations.

Remove: any hypothesis-specific items.

- [ ] **Step 6: Verify all diseases render with new layout**

Run:
```bash
uv run python scripts/visualize_phenocam.py --all
```
Open each HTML file and verify:
- Header shows hypothesis legend with colored swatches
- No dropdown visible
- Module panel renders correctly
- Bottom-left legend shows node types

- [ ] **Step 7: Commit**

```bash
git add scripts/visualize_phenocam.py
git commit -m "phenocam viz: replace hypothesis dropdown with persistent legend, update CSS"
```

---

## Task 6: Edge Routing for Collapsed Modules

When a module is collapsed, edges that connected to internal nodes need to route to port dots on the collapsed bar instead.

**Files:**
- Modify: `scripts/visualize_phenocam.py` — edge drawing logic in JS

- [ ] **Step 1: Add edge routing resolution**

Add a function that resolves edge endpoints when modules are collapsed:

```javascript
function resolveEdgeEndpoint(nodeId, og, moduleNodeIds, nodeToModule) {
  // If node is inside a collapsed module, route to the module bar position
  if (moduleNodeIds.has(nodeId)) {
    const modId = nodeToModule[nodeId];
    if (_moduleState[modId] !== "expanded") {
      const modNodeId = "module:" + modId;
      const modPos = og.node(modNodeId);
      if (modPos) {
        return { x: modPos.x, y: modPos.y, resolved: true, moduleId: modId, originalId: nodeId };
      }
    }
  }
  return null;  // use normal position
}
```

- [ ] **Step 2: Integrate into edge drawing**

In the `drawEdges()` function (and `drawIntermediateEdges()`), before drawing each edge:
1. Check if source or target needs resolution via `resolveEdgeEndpoint()`
2. If resolved, use the module bar position (adjusted to the appropriate port dot) instead of the internal node position
3. For collapsed modules, compute port dot Y positions matching those drawn in `drawModulePanels()`

- [ ] **Step 3: Test collapse/expand cycle**

Open the Gorlin visualization, click the module header to collapse, verify:
- Edges from PTCH1/SUFU perturbations connect to left port dots
- Edges to disease activities connect from right port dots
- Clicking again re-expands and edges reconnect to internal nodes

- [ ] **Step 4: Commit**

```bash
git add scripts/visualize_phenocam.py
git commit -m "phenocam viz: edge routing through collapsed module port dots"
```

---

## Task 7: Visual Polish and Final Verification

Final cleanup: edge label positioning, tooltip refinements, and comprehensive testing across all diseases.

**Files:**
- Modify: `scripts/visualize_phenocam.py`

- [ ] **Step 1: Add edge labels for module-internal edges**

Carry forward the existing edge label rendering (shortened RO relation at midpoint) for module-internal edges. Only show labels on expanded module edges, not on cross-boundary or intermediate edges (they're visually distinct by dash pattern).

- [ ] **Step 2: Update tooltip to show per-hypothesis state breakdown**

In the activity tooltip, instead of showing state for "the selected hypothesis" (old dropdown approach), show a table of all hypotheses and their states for that node:

```javascript
// In attachActivityTooltip:
const nodeStates = {};
DATA.hypothesis_groups.forEach(hg => {
  if (hg.states[n.id]) {
    nodeStates[hg.id] = hg.states[n.id];
  }
});
if (Object.keys(nodeStates).length > 0) {
  html += `<div class="tt-section"><b>Perturbation states:</b>`;
  Object.entries(nodeStates).forEach(([hgId, info]) => {
    const color = hgColors[hgId] || "#999";
    const hgName = DATA.hypothesis_groups.find(h => h.id === hgId)?.name || hgId;
    const stClass = "tt-state tt-state-" + info.state;
    html += `<div class="tt-detail">`;
    html += `<span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:${color};margin-right:4px"></span>`;
    html += `${hgName}: <span class="${stClass}">${info.state.replace(/_/g, " ")}</span>`;
    if (info.is_primary) html += ` <b>(primary)</b>`;
    html += `</div>`;
  });
  html += `</div>`;
}
```

- [ ] **Step 3: Verify Gorlin Syndrome (complex case)**

Open `causal_models/viz/gorlin_syndrome.html`:
- [ ] Module panel visible with "▼ Hedgehog Signaling"
- [ ] PTCH1 and SUFU perturbation nodes to the left with red/blue borders and frequency badges
- [ ] Red edges trace from PTCH1 through module to GLI1
- [ ] Blue edges trace from SUFU through module to GLI1
- [ ] After GLI1, parallel red+blue edges continue to disease activities
- [ ] Edges propagate colors through intermediates to phenotypes
- [ ] Module collapses/expands on header click
- [ ] Collapsed module shows colored port dots
- [ ] Tooltips show per-hypothesis state breakdown
- [ ] Legend in header shows both hypotheses with colors

- [ ] **Step 4: Verify Noonan Syndrome (4 hypotheses)**

Open `causal_models/viz/noonan_syndrome.html`:
- [ ] 4 hypothesis colors visible in legend
- [ ] 4 perturbation nodes with distinct colors
- [ ] Parallel colored edges (up to 4 lines) visible
- [ ] Convergence at ERK shows all 4 colors arriving

- [ ] **Step 5: Verify EDS (simple case, 1 hypothesis)**

Open `causal_models/viz/ehlers_danlos_col5a1.html`:
- [ ] Single hypothesis color
- [ ] Module panel works
- [ ] No visual artifacts from single-hypothesis edge rendering

- [ ] **Step 6: Verify CFC Syndrome**

Open `causal_models/viz/cardiofaciocutaneous_syndrome.html`:
- [ ] Renders without errors
- [ ] Shares RAS-MAPK module with Noonan (different perturbation entries)

- [ ] **Step 7: Final commit**

```bash
git add scripts/visualize_phenocam.py
git commit -m "phenocam viz: visual polish, tooltip updates, final verification"
```
