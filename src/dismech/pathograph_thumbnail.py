"""Label-free SVG thumbnails of a disorder's pathograph.

A thumbnail draws the same :class:`~dismech.graph.CausalGraph` the interactive
pathograph uses, but as coloured dots with no labels, so that it fits in a
page header or a card grid and shows the *shape* of an entry's causal model at
a glance: how deep the mechanism chain is, how widely it fans out, and how many
phenotypes nothing explains.

Layout is deterministic (no force simulation), so a thumbnail changes only when
the entry does:

* upstream nodes (genes, exposures, mechanisms) go in columns by longest causal
  path from a root;
* outcome nodes (biomarkers, phenotypes) go in the columns to their right, with
  one extra column for sequelae;
* columns taller than ``max_rows`` wrap into sub-columns;
* treatments and models are small squares in a band under the nodes they act on;
* outcome nodes with no causal edge at all form a grey row at the bottom.

Colours are CSS custom properties with literal fallbacks, so the same SVG is
themeable inside a page and still renders correctly as a standalone file.

>>> from dismech.graph import build_causal_graph
>>> disorder = {
...     "genetic": [{"name": "GLA", "association": "causative"}],
...     "pathophysiology": [
...         {"name": "Enzyme deficiency", "downstream": [{"target": "Substrate storage"}]},
...         {"name": "Substrate storage", "downstream": [{"target": "Pain"}]},
...     ],
...     "phenotypes": [{"name": "Pain"}, {"name": "Rash"}],
... }
>>> thumb = render_thumbnail(build_causal_graph(disorder))
>>> thumb.phenotypes, thumb.phenotypes_connected, thumb.unconnected
(2, 1, 1)
>>> thumb.svg.startswith("<svg")
True
"""

from __future__ import annotations

import html
from collections import defaultdict
from dataclasses import dataclass

from dismech.graph import CausalGraph
from dismech.qc_plugins import CAUSAL_PREDICATES

UPSTREAM_TYPES = frozenset({"genetic", "environmental", "pathophysiology"})
OUTCOME_TYPES = frozenset({"biochemical", "phenotype"})
SIDE_TYPES = frozenset(
    {"treatment", "animal_model", "experimental_model", "computational_model"}
)

# Hues follow the interactive pathograph's node colours, darkened so a 3px dot
# stays visible. Override any of them on the page through the CSS variable.
NODE_COLORS = {
    "genetic": ("--pt-gene", "#7c3aed"),
    "environmental": ("--pt-env", "#16a34a"),
    "pathophysiology": ("--pt-mech", "#2563eb"),
    "biochemical": ("--pt-bio", "#4f46e5"),
    "phenotype": ("--pt-pheno", "#d97706"),
    "treatment": ("--pt-tx", "#db2777"),
    "animal_model": ("--pt-model", "#64748b"),
    "experimental_model": ("--pt-model", "#64748b"),
    "computational_model": ("--pt-model", "#64748b"),
}
EDGE_COLOR = "var(--pt-edge, #b4c3c5)"
SIDE_EDGE_COLOR = "var(--pt-side-edge, #d6dfe0)"
LOOSE_COLOR = "var(--pt-loose, #b9bfc4)"
HALO_COLOR = "var(--pt-halo, #ffffff)"


@dataclass(frozen=True)
class Thumbnail:
    """An SVG thumbnail plus the counts its caption reports."""

    svg: str
    edges: int
    phenotypes: int
    phenotypes_connected: int
    unconnected: int


def _color(node_type: str) -> str:
    """Return the CSS colour expression for a node type.

    >>> _color("phenotype")
    'var(--pt-pheno, #d97706)'
    """
    var, fallback = NODE_COLORS[node_type]
    return f"var({var}, {fallback})"


def longest_path_layers(
    nodes: list[str], edges: list[tuple[str, str]]
) -> dict[str, int]:
    """Assign each node its longest path length from a root.

    An edge that would close a cycle is ignored, so the result is defined for
    any graph.

    >>> longest_path_layers(["a", "b", "c"], [("a", "b"), ("b", "c"), ("a", "c")])
    {'a': 0, 'b': 1, 'c': 2}
    >>> longest_path_layers(["a", "b"], [("a", "b"), ("b", "a")])
    {'a': 1, 'b': 0}
    """
    node_set = set(nodes)
    parents: dict[str, list[str]] = defaultdict(list)
    for source, target in edges:
        if source in node_set and target in node_set:
            parents[target].append(source)
    layer: dict[str, int] = {}
    on_stack: set[str] = set()

    def visit(node: str) -> int:
        if node in layer:
            return layer[node]
        on_stack.add(node)
        depths = [visit(p) + 1 for p in parents[node] if p not in on_stack]
        layer[node] = max(depths, default=0)
        on_stack.discard(node)
        return layer[node]

    for node in nodes:
        visit(node)
    return {node: layer[node] for node in nodes}


def wrap_column(nodes: list[str], max_rows: int) -> list[list[str]]:
    """Split a column into evenly sized sub-columns of at most ``max_rows``.

    >>> wrap_column(list("abcde"), 2)
    [['a', 'b'], ['c', 'd'], ['e']]
    >>> wrap_column(list("abcd"), 3)
    [['a', 'b'], ['c', 'd']]
    >>> wrap_column([], 3)
    []
    """
    if not nodes:
        return []
    parts = -(-len(nodes) // max_rows)
    per = -(-len(nodes) // parts)
    return [nodes[i : i + per] for i in range(0, len(nodes), per)]


def _order_columns(
    columns: dict[int, list[str]],
    column_of: dict[str, int],
    edges: list[tuple[str, str]],
) -> None:
    """Reduce crossings in place with alternating barycentre sweeps."""
    neighbours: dict[str, list[str]] = defaultdict(list)
    for source, target in edges:
        neighbours[source].append(target)
        neighbours[target].append(source)
    for nodes in columns.values():
        nodes.sort()
    position = {n: i for nodes in columns.values() for i, n in enumerate(nodes)}
    order = sorted(columns)
    for sweep in range(6):
        for col in order if sweep % 2 == 0 else reversed(order):
            nodes = columns[col]

            def barycentre(
                node: str, col: int = col, nodes: list[str] = nodes
            ) -> float:
                rel = [
                    position[x] / max(len(columns[column_of[x]]), 1)
                    for x in neighbours[node]
                    if x in column_of and column_of[x] != col
                ]
                if rel:
                    return sum(rel) / len(rel)
                return position[node] / max(len(nodes), 1)

            nodes.sort(key=barycentre)
            for i, node in enumerate(nodes):
                position[node] = i


def render_thumbnail(
    graph: CausalGraph,
    *,
    width: int = 300,
    max_rows: int = 18,
    row_step: float = 8.0,
) -> Thumbnail:
    """Draw ``graph`` as a label-free SVG thumbnail.

    >>> from dismech.graph import build_causal_graph
    >>> thumb = render_thumbnail(build_causal_graph({}))
    >>> (thumb.edges, thumb.phenotypes, thumb.unconnected)
    (0, 0, 0)
    """
    node_type = {name: node.node_type for name, node in graph.nodes.items()}
    core = {
        name: t for name, t in node_type.items() if t in UPSTREAM_TYPES | OUTCOME_TYPES
    }
    core_edges = [
        (e.source, e.target)
        for e in graph.edges
        if e.source in core and e.target in core and e.source != e.target
    ]
    side_edges = [
        (e.source, e.target)
        for e in graph.edges
        if e.target in core and node_type.get(e.source) in SIDE_TYPES
    ]

    connected = {node for edge in core_edges for node in edge}
    # Same rule as qc_plugins.causal_inlink_coverage (the compliance gate and
    # `just list-disconnected-phenotypes`): readout and non-causal environmental
    # edges are drawn, but do not count a phenotype as connected.
    explained = {
        e.target
        for e in graph.edges
        if e.predicate in CAUSAL_PREDICATES
        and e.source in core
        and e.target in core
        and e.source != e.target
    }
    loose = sorted(n for n in core if n not in connected and core[n] in OUTCOME_TYPES)
    upstream = [n for n in core if core[n] in UPSTREAM_TYPES]
    outcomes = [n for n in core if core[n] in OUTCOME_TYPES and n in connected]

    up_layers = longest_path_layers(upstream, core_edges)
    out_layers = longest_path_layers(outcomes, core_edges)
    first_outcome = max(up_layers.values(), default=-1) + 1
    column_of = dict(up_layers)
    column_of.update({n: first_outcome + min(out_layers[n], 1) for n in outcomes})

    columns: dict[int, list[str]] = defaultdict(list)
    for node, col in column_of.items():
        columns[col].append(node)
    _order_columns(columns, column_of, core_edges)

    slots = [
        part for col in sorted(columns) for part in wrap_column(columns[col], max_rows)
    ]
    rows = max((len(s) for s in slots), default=1)
    pad = 8.0
    body_height = pad * 2 + max(rows - 1, 1) * row_step
    xy: dict[str, tuple[float, float]] = {}
    for i, slot in enumerate(slots):
        x = pad + (width - 2 * pad) * (i / (len(slots) - 1) if len(slots) > 1 else 0.5)
        offset = (rows - len(slot)) * row_step / 2
        for j, node in enumerate(slot):
            xy[node] = (x, pad + offset + j * row_step)

    side_targets: dict[str, list[float]] = defaultdict(list)
    for source, target in side_edges:
        if target in xy:
            side_targets[source].append(xy[target][0])
    side_y = body_height + 10
    side_x: dict[str, float] = {}
    last = float("-inf")
    for source in sorted(
        side_targets, key=lambda s: sum(side_targets[s]) / len(side_targets[s])
    ):
        mean = sum(side_targets[source]) / len(side_targets[source])
        side_x[source] = min(max(mean, last + 6), width - pad)
        last = side_x[source]

    loose_y = side_y + (14 if side_x else 4)
    per_row = max(int((width - 2 * pad) // 7), 1)
    height = loose_y + ((-(-len(loose) // per_row)) * 7 + 6 if loose else 0)

    parts = [
        (
            f'<svg class="pathograph-thumbnail" viewBox="0 0 {width} {height:.0f}" '
            'xmlns="http://www.w3.org/2000/svg" role="img" '
            f'aria-label="Pathograph thumbnail: {len(xy)} connected nodes, '
            f'{len(loose)} unconnected outcomes">'
        )
    ]
    parts.append(f'<g fill="none" stroke="{EDGE_COLOR}" stroke-width="0.8">')
    for source, target in core_edges:
        if source not in xy or target not in xy:
            continue
        (x1, y1), (x2, y2) = xy[source], xy[target]
        if x2 > x1:
            mid = (x1 + x2) / 2
            d = f"M{x1:.1f},{y1:.1f} C{mid:.1f},{y1:.1f} {mid:.1f},{y2:.1f} {x2:.1f},{y2:.1f}"
        else:
            d = f"M{x1:.1f},{y1:.1f} Q{(x1 + x2) / 2:.1f},{min(y1, y2) - 14:.1f} {x2:.1f},{y2:.1f}"
        parts.append(f'<path d="{d}"/>')
    parts.append("</g>")

    if side_x:
        parts.append(f'<g fill="none" stroke="{SIDE_EDGE_COLOR}" stroke-width="0.6">')
        for source, target in side_edges:
            if source in side_x and target in xy:
                tx, ty = xy[target]
                parts.append(
                    f'<path d="M{side_x[source]:.1f},{side_y:.1f} L{tx:.1f},{ty:.1f}"/>'
                )
        parts.append("</g>")
        for source, x in side_x.items():
            parts.append(
                f'<rect x="{x - 2.4:.1f}" y="{side_y - 2.4:.1f}" width="4.8" height="4.8" '
                f'fill="{_color(node_type[source])}"><title>{html.escape(source)}</title></rect>'
            )

    for node, (x, y) in xy.items():
        radius = 3.4 if core[node] in UPSTREAM_TYPES else 2.9
        parts.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{radius}" fill="{_color(core[node])}" '
            f'stroke="{HALO_COLOR}" stroke-width="0.8"><title>{html.escape(node)}</title></circle>'
        )

    for i, node in enumerate(loose):
        x = pad + (i % per_row) * 7
        y = loose_y + (i // per_row) * 7 + 3
        parts.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.5" fill="{LOOSE_COLOR}">'
            f"<title>{html.escape(node)} (no causal edge)</title></circle>"
        )
    parts.append("</svg>")

    phenotypes = [n for n, t in core.items() if t == "phenotype"]
    return Thumbnail(
        svg="".join(parts),
        edges=len(core_edges),
        phenotypes=len(phenotypes),
        phenotypes_connected=sum(1 for n in phenotypes if n in explained),
        unconnected=len(loose),
    )
