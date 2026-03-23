# Pheno-CAM Visualization Redesign

## Problem

The current Pheno-CAM visualization renders all node types (module activities, disease-local activities, tissue intermediates, phenotypes, disease) into a single flat DAG with no spatial grouping. This makes it hard for colleagues to:

1. **Follow the causal story** from mutation through molecular signaling to tissue pathology to clinical phenotype
2. **See the disease architecture** — how multiple genetic entry points converge on shared downstream pathology

The hypothesis group dropdown requires mentally comparing node states across switches rather than seeing convergence at a glance.

## Goals

- Communicate the causal story (mutation → molecular → tissue → phenotype) via clear left-to-right reading order
- Show disease architecture — multiple hypotheses visible simultaneously with convergence apparent at a glance
- Handle Gorlin-scale complexity (2+ hypotheses, 8+ module activities, 6+ disease-local activities, 10+ phenotypes)
- Work standalone (self-explanatory for colleagues browsing on their own) and in presentation (focusable)
- Remain a single self-contained HTML file with D3.js + dagre

## Non-Goals

- Changing the Pheno-CAM data model (YAML schema is unchanged)
- Supporting editing or authoring in the visualization
- Multi-disease comparison views

---

## Design

### 1. Layout & Spatial Organization

**Overall layout**: Left-to-right DAG with two kinds of elements:

1. **Module panels** — bordered, labeled containers with expand/collapse. Each imported module gets its own panel. Internal activities and edges render inside the panel when expanded, or collapse to a summary bar.

2. **Free-flowing nodes** — everything else (perturbation nodes, disease-local activities, tissue intermediates, phenotype targets, disease node) laid out by dagre as regular graph nodes with no container.

**Reading order** (left to right):

```
Perturbation nodes → Module panel(s) → Disease-local activities → Tissue intermediates → Phenotypes → Disease
```

**Two-pass layout strategy**: Dagre's compound node support is limited (children can overflow parent bounds, no automatic parent sizing). Instead, use a two-pass approach:

1. **Inner layout**: Run dagre on each expanded module's internal activities + edges independently. This produces the module's internal node positions and bounding box dimensions.
2. **Outer layout**: Run dagre on the top-level graph, where each expanded module is a single fixed-size node (using the bounding box from pass 1). Free-flowing nodes (perturbations, disease activities, intermediates, phenotypes, disease) participate normally. Collapsed modules are fixed-size bars.
3. **Compose**: Translate internal node positions by the module's top-level position to produce final coordinates.

**Initial viewport**: Fit the entire graph on load (scale to fit within the viewport with padding), same as current behavior.

**Zoom/pan**: Preserved (d3.zoom with scroll-to-zoom, drag-to-pan).

### 2. Hypothesis Visualization

**Perturbation nodes**: Float freely to the left of the module panel(s). Each gets:
- A bold colored border matching its hypothesis color
- Gene name + variant class + perturbed state as labels
- A small frequency badge (e.g., "~70%")

**Hypothesis color assignment**: Each hypothesis group gets a distinct color from a fixed palette (e.g., red, blue, teal, orange — up to ~6). Assigned in declaration order from the YAML.

**Colored edges**: Each hypothesis's perturbation edge is drawn as a distinct, parallel line in its hypothesis color. When two hypotheses target the same module node, edges arrive as separate colored lines side by side (not overlaid or dashed).

**Legend**: A persistent legend in the bottom-left corner (fixed position, does not scroll with graph), mapping hypothesis colors to names + frequencies. Replaces the current dropdown. Clicking a legend entry is not interactive in v1 (could add highlight-on-click in a future iteration).

### 3. Edge Coloring: Full Transitive Propagation

Hypothesis colors propagate transitively through the **entire graph** — from perturbation entry through module internals, cross-boundary edges, tissue intermediates, all the way to phenotype and disease nodes.

**Rule**: An edge is colored by whichever hypothesis(es) caused the upstream node to be in a perturbed state. This is determined by tracing backward through the graph to find which perturbation(s) are ancestral.

**After convergence**: Edges carry multiple parallel colored lines (one per contributing hypothesis). A phenotype reachable by all hypotheses shows all hypothesis colors arriving at it.

**Unperturbed module-internal edges**: Light gray (background wiring, not part of the causal story under any hypothesis).

### 4. Edge Semantics via Dash Pattern

Three dash patterns distinguish edge semantics, all drawn in hypothesis color (or gray if unperturbed):

| Pattern | Semantic | Used for |
|---------|----------|----------|
| Solid | Direct causal regulation | Module edges (RO:0002629, RO:0002630, RO:0002413), cross-boundary driven_by, intermediate driven_by |
| Dashed | Causes condition | Target driven_by (RO:0003303) — tissue pathology → clinical phenotype |
| Dotted | Has phenotype (annotation) | Disease has_phenotype (RO:0002200) — phenotype → disease |

**Negative regulation**: Edges with `RO:0002630` (directly negatively regulates) or `RO:0002305` (causally upstream of, negative effect) use a T-bar or flat-head terminator instead of an arrowhead, in addition to the hypothesis color.

### 5. Node Types & Visual Treatment

**Module activity nodes** (inside panels):
- Rounded rectangles, neutral gray when unperturbed
- When perturbed: background colored by perturbation state (green=increased, red/pink=decreased, dark red=absent, etc.)
- Split background when hypotheses disagree on state: divide the node background into equal vertical stripes (one per disagreeing hypothesis, in hypothesis color mapped to that hypothesis's state color). For 2 hypotheses: left/right split. For 3+: equal-width vertical stripes. Tooltip shows the full per-hypothesis breakdown.
- Two-line label: gene symbol (bold) + shortened molecular function
- State badge at bottom

**Perturbation nodes** (free-floating):
- Rounded rectangles with thick hypothesis-colored border
- Gene name + variant class + state
- Frequency badge (small pill in hypothesis color)

**Disease-local activity nodes** (free-floating):
- Same shape as module activities but with a distinct border style to show they're not part of a module

**Tissue intermediate nodes** (free-floating):
- Neutral background with state-colored border
- Label: name + tissue annotation (e.g., "Basal cell prolif. / epidermis")
- State badge

**Phenotype nodes** (free-floating):
- Rounded pill shape
- Label + HPO ID

**Disease node** (free-floating):
- Rounded pill shape
- Disease name + MONDO ID

### 6. Expand/Collapse Behavior

**Expanded state**:
- Module panel shows full internal DAG (activities + edges)
- Clickable header bar: "▼ Module Name" + activity count
- Internal layout by dagre within panel bounds

**Collapsed state**:
- Single horizontal bar: "▶ Module Name — N activities"
- Left port dots: one per perturbation entry point, colored by hypothesis. Spaced evenly along the left edge of the bar.
- Right port dots: one per activity that has outgoing edges to external nodes. Labeled with activity name on hover. Spaced evenly along the right edge. If many ports exist (>4), the bar height grows to accommodate them (minimum spacing of 12px between ports).
- Edges reroute to appropriate port dots

**Expanded state edge attachment**: Edges from outside the panel connect directly to the internal activity node, visually crossing the panel border. No port-dot indirection when expanded — the panel border is just a visual container, not an edge barrier.

**Transition**: Re-layout with dagre on toggle (two-pass re-run). No animation for v1 — the graph snaps to the new layout. A smooth transition could be added later.

**Edge cases**:
- Module with zero external edges: collapsed bar has no right port dots (just a summary bar)
- Hypothesis with no perturbation in a given module: no left port dot for that hypothesis on that module

**Default state**: Expanded.

**Multiple modules**: Each collapses independently.

### 7. Tooltips

Preserved from current implementation:
- Hover to preview, click to pin (with close button + Escape + click-outside to unpin)
- Activity tooltips: gene/complex, molecular function, location, process, perturbation state per hypothesis, evidence
- Edge tooltips: source → target, RO relation, ECO code, evidence snippets
- Intermediate tooltips: name, process, tissue, driven_by details with evidence
- Phenotype tooltips: HPO term, route description, intermediates summary
- Raw YAML collapsible section on all tooltips

---

## Multi-Module Considerations

Currently every disease imports exactly one module. The design supports multiple modules naturally:
- Each imported module gets its own expandable panel
- Cross-module edges route between panels (just like module → disease-local edges)
- Activities are namespaced (`module_id:activity_id`) so no identity conflicts
- Each panel collapses independently

---

## Perturbation State Color Palette

Carried from current with no changes:

| State | Background | Border |
|-------|-----------|--------|
| Normal (unperturbed) | `#f8f9fa` | `#dee2e6` |
| Increased | `#d4edda` | `#28a745` |
| Decreased | `#fde8e8` | `#e57373` |
| Absent | `#f8d7da` | `#dc3545` (dashed) |
| Constitutively active | `#c3e6cb` | `#1b5e20` (thick) |
| Substrate accumulated | `#fff3cd` | `#ff8f00` |

---

## Implementation Scope

This redesign modifies only `scripts/visualize_phenocam.py`. No changes to the data model, YAML files, or other scripts. The Python `build_graph_data()` function may need minor additions (e.g., computing hypothesis ancestry for edge coloring), but the bulk of the work is in the HTML/JS template.

### Key Implementation Challenges

1. **Two-pass dagre layout**: Run dagre separately for each expanded module's internals, then for the outer graph using computed bounding boxes. Compose final positions by translating inner coordinates.

2. **Hypothesis edge propagation**: Requires computing, for each node, which hypothesis(es) can reach it. This is a graph traversal from each perturbation entry point through module edges and driven_by chains. Computed in Python (`build_graph_data()`) and passed as a `hypothesis_colors` field on each edge in the JSON.

3. **Parallel edge rendering**: When multiple hypothesis colors share an edge, offset them perpendicular to the edge path. Use a fixed offset of 2px per hypothesis. For curved dagre paths (polylines rendered with `d3.curveBasis`), compute the perpendicular at each control point and offset the entire path. For 5-6 hypotheses (10-12px total spread), this remains visually acceptable at typical zoom levels.

4. **Collapsed port routing**: When a module is collapsed, edges that targeted internal nodes reroute to port dots on the collapsed bar. Maintain a mapping of `internal_activity_id → port_position` that updates when the module toggles state.

5. **Re-layout on toggle**: Collapsing/expanding changes the outer graph node size, requiring a two-pass dagre re-run and SVG re-render. The snap transition is acceptable for v1.
