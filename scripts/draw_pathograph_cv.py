#!/usr/bin/env python3
"""Draw a dismech pathograph as a PNG using OpenCV.

An experiment in rendering the causal graph produced by ``dismech.graph`` with
plain OpenCV drawing primitives instead of Mermaid/Cytoscape. Everything --
layout, rounded node cards, bezier edges, drop shadows, antialiased text -- is
done with ``cv2`` calls on a numpy canvas.

Two rendering ideas do most of the visual work:

* **Supersampling.** The whole scene is drawn at ``--scale`` x resolution and
  downsampled with ``INTER_AREA``. OpenCV's Hershey fonts and ``LINE_AA``
  strokes are coarse at 1x; at 3x-then-shrink they read as clean vector art.
* **Blurred shadow layer.** Node silhouettes are drawn into a single-channel
  mask, blurred with ``GaussianBlur``, and alpha-composited under the cards,
  which separates the layers without any per-node compositing work.

Treatments are pulled out of the causal flow into their own band beneath the
graph and connected to the mechanism they act on with blunt inhibition
connectors, since a ``targets`` edge runs against the causal direction and
would otherwise drag every drug into an upstream layer.

Usage::

    uv run python scripts/draw_pathograph_cv.py kb/disorders/Familial_Hypercholesterolemia.yaml -o fh.png
"""

from __future__ import annotations

import argparse
import math
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import cv2
import numpy as np

from dismech.graph import CausalGraph, build_causal_graph
from dismech.yaml_io import safe_load

# ---------------------------------------------------------------------------
# Palette. Declared as RGB hex and flipped for OpenCV's BGR channel order.
# Node hues follow the Mermaid renderer's NODE_COLORS so the two agree.
# ---------------------------------------------------------------------------


def rgb(value: int) -> tuple[int, int, int]:
    """0xRRGGBB -> the (B, G, R) tuple OpenCV expects."""
    return (value & 0xFF, (value >> 8) & 0xFF, (value >> 16) & 0xFF)


BG = rgb(0xF9F8F6)
INK = rgb(0x1E2226)
MUTED = rgb(0x6E7680)
HAIRLINE = rgb(0xD4DADE)
BAND_FILL = rgb(0xF1F0F7)
BAND_EDGE = rgb(0xD8D5E8)
BAND_TEXT = rgb(0x8C84AA)

# node_type -> (card fill, accent bar / border)
TYPE_STYLE = {
    "pathophysiology": (rgb(0xD6E8F6), rgb(0x257AC4)),
    "phenotype": (rgb(0xFAE9D0), rgb(0xC77A25)),
    "genetic": (rgb(0xF3E0EE), rgb(0xA84A96)),
    "biochemical": (rgb(0xCDE8E1), rgb(0x28855E)),
    "environmental": (rgb(0xDEEED6), rgb(0x5E8D38)),
    "treatment": (rgb(0xE9DBDB), rgb(0x80404A)),
    "orphan": (rgb(0xEBD5D5), rgb(0xBE3C3C)),
}
DEFAULT_STYLE = (rgb(0xE9E9E9), rgb(0x8C8C8C))

# predicate -> (stroke colour, dashed?)
EDGE_STYLE = {
    "causes": (rgb(0x7E8A96), False),
    "contributes_to": (rgb(0xBE84B2), False),
    "variant_of": (rgb(0xD4B6CD), True),
    "readout": (rgb(0x78B296), True),
    "targets": (rgb(0xA56C78), True),
}

CAUSAL_PREDICATES = ("causes", "contributes_to", "variant_of", "readout")

FONT = cv2.FONT_HERSHEY_DUPLEX
FONT_LIGHT = cv2.FONT_HERSHEY_SIMPLEX


@dataclass
class Node:
    name: str
    node_type: str
    layer: int = 0
    x: float = 0.0  # left edge
    y: float = 0.0  # centre
    w: float = 0.0
    h: float = 0.0
    lines: list[str] = field(default_factory=list)

    @property
    def cx(self) -> float:
        return self.x + self.w / 2

    @property
    def left(self) -> tuple[float, float]:
        return (self.x, self.y)

    @property
    def right(self) -> tuple[float, float]:
        return (self.x + self.w, self.y)


# ---------------------------------------------------------------------------
# Text measurement / wrapping
# ---------------------------------------------------------------------------


def text_size(text: str, font: int, fs: float, th: int) -> tuple[int, int]:
    (w, h), _ = cv2.getTextSize(text, font, fs, th)
    return w, h


def wrap(text: str, max_w: float, font: int, fs: float, th: int) -> list[str]:
    """Greedy word wrap using OpenCV's own text metrics."""
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = f"{cur} {word}".strip()
        if cur and text_size(trial, font, fs, th)[0] > max_w:
            lines.append(cur)
            cur = word
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines or [""]


def ellipsize(text: str, max_w: float, font: int, fs: float, th: int) -> str:
    """Trim to one line, with a trailing ellipsis if it had to be cut."""
    if text_size(text, font, fs, th)[0] <= max_w:
        return text
    cut = text
    while cut and text_size(cut + "...", font, fs, th)[0] > max_w:
        cut = cut[:-1]
    return cut.rstrip() + "..."


# ---------------------------------------------------------------------------
# Layered layout
# ---------------------------------------------------------------------------


def assign_layers(nodes: dict[str, Node], edges: list[tuple[str, str]]) -> None:
    """Layer the DAG left-to-right, then right-justify every internal node.

    Longest-path layering alone puts each node as early as it can go, which
    breaks up sibling sets: FH's five gene-defect nodes all feed the same
    consumer but land in three different columns because the LDLR variant chain
    is deeper than the APOE one. A second pass pulls every node with successors
    to ``min(successor layer) - 1``, so siblings that converge on one mechanism
    line up in one column. Sinks keep their earliest layer and stay next to the
    node that produced them.
    """
    if not nodes:
        return
    for _ in range(len(nodes) + 1):
        changed = False
        for src, tgt in edges:
            if nodes[tgt].layer < nodes[src].layer + 1:
                nodes[tgt].layer = nodes[src].layer + 1
                changed = True
        if not changed:
            break

    succs: dict[str, list[str]] = defaultdict(list)
    for src, tgt in edges:
        succs[src].append(tgt)
    for _ in range(len(nodes) + 1):
        changed = False
        for name, node in nodes.items():
            if not succs[name]:
                continue
            latest = min(nodes[t].layer for t in succs[name]) - 1
            if latest > node.layer:
                node.layer = latest
                changed = True
        if not changed:
            break

    shift = min(n.layer for n in nodes.values())
    for node in nodes.values():
        node.layer -= shift


def order_layers(
    layers: dict[int, list[Node]],
    preds: dict[str, list[str]],
    succs: dict[str, list[str]],
    sweeps: int = 6,
) -> None:
    """Median heuristic, alternating forward/backward, to cut edge crossings."""
    index = {n.name: i for layer in layers.values() for i, n in enumerate(layer)}

    def median(name: str, neighbours: dict[str, list[str]]) -> float:
        positions = sorted(index[m] for m in neighbours.get(name, []) if m in index)
        if not positions:
            return float(index[name])
        mid = len(positions) // 2
        if len(positions) % 2:
            return float(positions[mid])
        return (positions[mid - 1] + positions[mid]) / 2

    for sweep in range(sweeps):
        keys = sorted(layers) if sweep % 2 == 0 else sorted(layers, reverse=True)
        neighbours = preds if sweep % 2 == 0 else succs
        for key in keys:
            layers[key].sort(key=lambda n: median(n.name, neighbours))
            for i, n in enumerate(layers[key]):
                index[n.name] = i


def pack_layer(layer: list[Node], gap: float) -> None:
    """Resolve overlaps inside one layer while preserving order.

    Two passes -- push down, then pull up -- keep the block centred on its
    original mean instead of drifting toward the bottom of the canvas.
    """
    for i in range(1, len(layer)):
        lo = layer[i - 1].y + layer[i - 1].h / 2 + gap + layer[i].h / 2
        layer[i].y = max(layer[i].y, lo)
    for i in range(len(layer) - 2, -1, -1):
        hi = layer[i + 1].y - layer[i + 1].h / 2 - gap - layer[i].h / 2
        layer[i].y = min(layer[i].y, hi)


def place_vertically(
    layers: dict[int, list[Node]],
    preds: dict[str, list[str]],
    succs: dict[str, list[str]],
    nodes: dict[str, Node],
    gap: float,
    passes: int = 24,
) -> None:
    """Seed each layer as a stack, then relax nodes toward their neighbours."""
    for layer in layers.values():
        cursor = 0.0
        for node in layer:
            node.y = cursor + node.h / 2
            cursor += node.h + gap

    for sweep in range(passes):
        keys = sorted(layers) if sweep % 2 == 0 else sorted(layers, reverse=True)
        neighbours = preds if sweep % 2 == 0 else succs
        for key in keys:
            for node in layers[key]:
                ys = [nodes[m].y for m in neighbours.get(node.name, []) if m in nodes]
                if ys:
                    node.y = sum(ys) / len(ys)
            layers[key].sort(key=lambda n: n.y)
            pack_layer(layers[key], gap)


# ---------------------------------------------------------------------------
# Drawing primitives
# ---------------------------------------------------------------------------


def rounded_rect(
    img: np.ndarray,
    x: float,
    y: float,
    w: float,
    h: float,
    r: float,
    colour: tuple[int, int, int],
    thickness: int = -1,
) -> None:
    """Filled or stroked rounded rectangle (cv2 has no primitive for this)."""
    x, y, w, h, r = int(round(x)), int(round(y)), int(round(w)), int(round(h)), int(round(r))
    r = max(0, min(r, w // 2, h // 2))
    if thickness < 0:
        cv2.rectangle(img, (x + r, y), (x + w - r, y + h), colour, -1, cv2.LINE_AA)
        cv2.rectangle(img, (x, y + r), (x + w, y + h - r), colour, -1, cv2.LINE_AA)
    else:
        cv2.line(img, (x + r, y), (x + w - r, y), colour, thickness, cv2.LINE_AA)
        cv2.line(img, (x + r, y + h), (x + w - r, y + h), colour, thickness, cv2.LINE_AA)
        cv2.line(img, (x, y + r), (x, y + h - r), colour, thickness, cv2.LINE_AA)
        cv2.line(img, (x + w, y + r), (x + w, y + h - r), colour, thickness, cv2.LINE_AA)
    for cx, cy, a0 in (
        (x + r, y + r, 180),
        (x + w - r, y + r, 270),
        (x + w - r, y + h - r, 0),
        (x + r, y + h - r, 90),
    ):
        cv2.ellipse(img, (cx, cy), (r, r), 0, a0, a0 + 90, colour, thickness, cv2.LINE_AA)


def bezier(p0, p1, p2, p3, samples: int = 48) -> np.ndarray:
    t = np.linspace(0.0, 1.0, samples).reshape(-1, 1)
    p0, p1, p2, p3 = (np.array(p, dtype=float) for p in (p0, p1, p2, p3))
    return (
        (1 - t) ** 3 * p0
        + 3 * (1 - t) ** 2 * t * p1
        + 3 * (1 - t) * t**2 * p2
        + t**3 * p3
    )


def draw_polyline(
    img: np.ndarray,
    pts: np.ndarray,
    colour: tuple[int, int, int],
    thickness: int,
    dashed: bool = False,
    dash: int = 26,
    gap: int = 16,
) -> None:
    """Stroke a polyline, optionally dashed by walking arc length."""
    ipts = np.round(pts).astype(np.int32)
    if not dashed:
        cv2.polylines(img, [ipts], False, colour, thickness, cv2.LINE_AA)
        return
    travelled, drawing, run = 0.0, True, 0.0
    for a, b in zip(pts[:-1], pts[1:]):
        seg = float(np.hypot(*(b - a)))
        if seg == 0:
            continue
        if drawing:
            cv2.line(
                img,
                tuple(np.round(a).astype(int)),
                tuple(np.round(b).astype(int)),
                colour,
                thickness,
                cv2.LINE_AA,
            )
        run += seg
        travelled += seg
        limit = dash if drawing else gap
        if run >= limit:
            drawing = not drawing
            run = 0.0


def arrow_head(
    img: np.ndarray,
    pts: np.ndarray,
    colour: tuple[int, int, int],
    size: float,
) -> None:
    """Filled triangle oriented along the curve's terminal tangent."""
    tip = pts[-1]
    direction = tip - pts[-6]
    norm = float(np.hypot(*direction))
    if norm == 0:
        return
    ux, uy = direction / norm
    base = tip - np.array([ux, uy]) * size
    perp = np.array([-uy, ux]) * size * 0.42
    tri = np.round(np.array([tip, base + perp, base - perp])).astype(np.int32)
    cv2.fillConvexPoly(img, tri, colour, cv2.LINE_AA)


def blunt_head(
    img: np.ndarray,
    pts: np.ndarray,
    colour: tuple[int, int, int],
    size: float,
    thickness: int,
) -> None:
    """T-bar terminator, the inhibition convention."""
    tip = pts[-1]
    direction = tip - pts[-6]
    norm = float(np.hypot(*direction))
    if norm == 0:
        return
    ux, uy = direction / norm
    perp = np.array([-uy, ux]) * size * 0.62
    a = np.round(tip + perp).astype(int)
    b = np.round(tip - perp).astype(int)
    cv2.line(img, tuple(a), tuple(b), colour, thickness, cv2.LINE_AA)


def put_text(
    img: np.ndarray,
    text: str,
    org: tuple[float, float],
    font: int,
    fs: float,
    colour: tuple[int, int, int],
    th: int,
    anchor: str = "left",
) -> None:
    w, _ = text_size(text, font, fs, th)
    x, y = org
    if anchor == "center":
        x -= w / 2
    elif anchor == "right":
        x -= w
    cv2.putText(img, text, (int(round(x)), int(round(y))), font, fs, colour, th, cv2.LINE_AA)


# ---------------------------------------------------------------------------
# Renderer
# ---------------------------------------------------------------------------


class PathographRenderer:
    def __init__(self, graph: CausalGraph, title: str, subtitle: str, scale: int = 3):
        self.graph = graph
        self.title = title
        self.subtitle = subtitle
        self.s = scale

        # Geometry in final-image pixels; multiplied by `scale` at draw time.
        self.col_w = 216.0
        self.col_gap = 96.0
        self.row_gap = 20.0
        self.pad_x, self.pad_y = 13.0, 11.0
        self.radius = 9.0
        self.margin = 46.0
        self.header_h = 96.0
        self.legend_h = 46.0
        self.band_gap = 60.0

        self.node_fs = 0.40
        self.node_th = 1
        self.line_h = 17.0

    # -- model -------------------------------------------------------------

    def build(self) -> None:
        g = self.graph
        causal = [
            (e.source, e.target, e.predicate)
            for e in g.edges
            if e.predicate in CAUSAL_PREDICATES
        ]
        self.treat_edges = [
            (e.source, e.target) for e in g.edges if e.predicate == "targets"
        ]

        # A handful of entries (e.g. Myasthenia_Gravis) carry only treatment
        # edges and no causal backbone. There is no flow to pull the drugs out
        # of, so draw the targeting edges as the graph itself.
        if not causal and self.treat_edges:
            causal = [(s, t, "targets") for s, t in self.treat_edges]
            self.treat_edges = []

        used = {n for s, t, _ in causal for n in (s, t)}
        treat_names = {s for s, _ in self.treat_edges}

        def node_type(name: str) -> str:
            if name in g.orphan_targets:
                return "orphan"
            info = g.nodes.get(name)
            return info.node_type if info else "orphan"

        self.nodes = {n: Node(n, node_type(n)) for n in sorted(used)}
        self.treatments = {n: Node(n, "treatment") for n in sorted(treat_names)}

        for node in list(self.nodes.values()) + list(self.treatments.values()):
            node.lines = wrap(
                node.name, self.col_w - 2 * self.pad_x - 8, FONT, self.node_fs, self.node_th
            )
            node.w = self.col_w
            node.h = max(38.0, len(node.lines) * self.line_h + 2 * self.pad_y)

        self.edges = [(s, t, p) for s, t, p in causal if s in self.nodes and t in self.nodes]

        preds: dict[str, list[str]] = defaultdict(list)
        succs: dict[str, list[str]] = defaultdict(list)
        for s, t, _ in self.edges:
            preds[t].append(s)
            succs[s].append(t)

        assign_layers(self.nodes, [(s, t) for s, t, _ in self.edges])
        layers: dict[int, list[Node]] = defaultdict(list)
        for node in self.nodes.values():
            layers[node.layer].append(node)
        for key in layers:
            layers[key].sort(key=lambda n: n.name)

        order_layers(layers, preds, succs)
        place_vertically(layers, preds, succs, self.nodes, self.row_gap)

        for key, layer in layers.items():
            for node in layer:
                node.x = key * (self.col_w + self.col_gap)
        self.layers = layers

        self._layout_treatment_band()
        self._normalise()

    def _layout_treatment_band(self) -> None:
        """Cluster drugs into a band under the graph, grouped by their target.

        Each group is a small grid of chips rather than one tall stack, and the
        whole group gets a single connector up to the mechanism it acts on --
        16 individual dashed lines would be unreadable, and group membership
        already says which drug hits what.
        """
        self.treat_groups: list[tuple[str, list[Node], tuple[float, float, float, float]]] = []
        if not self.treat_edges:
            self.band_top = max(n.y + n.h / 2 for n in self.nodes.values())
            return

        by_target: dict[str, list[Node]] = defaultdict(list)
        for src, tgt in self.treat_edges:
            if src in self.treatments and tgt in self.nodes:
                by_target[tgt].append(self.treatments[src])

        chip_w, chip_gap, inset = 168.0, 7.0, 13.0
        for node in self.treatments.values():
            node.lines = wrap(node.name, chip_w - 20.0, FONT, self.node_fs, self.node_th)
            node.w = chip_w
            node.h = max(30.0, len(node.lines) * self.line_h + 16.0)

        self.band_top = max(n.y + n.h / 2 for n in self.nodes.values()) + self.band_gap
        top = self.band_top + 30.0
        cursor = 0.0

        for target, drugs in sorted(by_target.items(), key=lambda kv: self.nodes[kv[0]].cx):
            drugs.sort(key=lambda n: n.name)
            # Keep clusters roughly square: at most four chips per column.
            cols = max(1, math.ceil(len(drugs) / 4))
            rows = math.ceil(len(drugs) / cols)
            row_h = max(d.h for d in drugs) + chip_gap
            gw = cols * chip_w + (cols - 1) * chip_gap + 2 * inset
            gh = rows * row_h - chip_gap + 2 * inset + 16.0

            x = max(cursor, self.nodes[target].cx - gw / 2)
            for i, drug in enumerate(drugs):
                drug.x = x + inset + (i // rows) * (chip_w + chip_gap)
                drug.y = top + inset + 16.0 + (i % rows) * row_h + drug.h / 2
            self.treat_groups.append((target, drugs, (x, top, gw, gh)))
            cursor = x + gw + 26.0

    def _normalise(self) -> None:
        every = list(self.nodes.values()) + list(self.treatments.values())
        min_x = min(n.x for n in every)
        min_y = min(n.y - n.h / 2 for n in every)
        off_x = self.margin - min_x
        off_y = self.margin + self.header_h - min_y
        for node in every:
            node.x += off_x
            node.y += off_y
        self.treat_groups = [
            (t, d, (x + off_x, y + off_y, w, h)) for t, d, (x, y, w, h) in self.treat_groups
        ]
        self.band_top += off_y
        right = max(n.x + n.w for n in every)
        bottom = max(n.y + n.h / 2 for n in every)
        for _t, _d, (x, y, w, h) in self.treat_groups:
            right = max(right, x + w)
            bottom = max(bottom, y + h)
        self.width = right + self.margin
        self.height = bottom + self.margin + self.legend_h

    # -- painting ----------------------------------------------------------

    def render(self) -> np.ndarray:
        s = self.s
        W, H = int(self.width * s), int(self.height * s)
        img = np.full((H, W, 3), BG, dtype=np.uint8)

        self._draw_band_backdrop(img)
        self._draw_shadows(img)
        self._draw_edges(img)
        for node in self.nodes.values():
            self._draw_node(img, node)
        for node in self.treatments.values():
            self._draw_node(img, node)
        self._draw_header(img)
        self._draw_legend(img)

        return cv2.resize(img, (int(self.width), int(self.height)), interpolation=cv2.INTER_AREA)

    def _draw_band_backdrop(self, img: np.ndarray) -> None:
        """One tinted panel per drug cluster, captioned with its target."""
        if not self.treat_groups:
            return
        s = self.s
        for target, _drugs, (x, y, w, h) in self.treat_groups:
            rounded_rect(img, x * s, y * s, w * s, h * s, 11 * s, BAND_FILL, -1)
            rounded_rect(img, x * s, y * s, w * s, h * s, 11 * s, BAND_EDGE, max(1, s // 2))
            caption = ellipsize(target.upper(), w - 26, FONT_LIGHT, 0.33, 1)
            put_text(
                img,
                caption,
                ((x + 13) * s, (y + 19) * s),
                FONT_LIGHT,
                0.33 * s,
                BAND_TEXT,
                max(1, s - 1),
            )

    def _draw_shadows(self, img: np.ndarray) -> None:
        """One blurred mask for every card, composited in a single pass."""
        s = self.s
        mask = np.zeros(img.shape[:2], dtype=np.uint8)
        for node in list(self.nodes.values()) + list(self.treatments.values()):
            rounded_rect(
                mask,
                node.x * s,
                (node.y - node.h / 2 + 2.0) * s,
                node.w * s,
                node.h * s,
                self.radius * s,
                255,
                -1,
            )
        k = max(3, int(5 * s) | 1)
        mask = cv2.GaussianBlur(mask, (k, k), 0)
        alpha = (mask.astype(np.float32) / 255.0 * 0.24)[..., None]
        shadow = np.zeros_like(img, dtype=np.float32)
        np.copyto(img, (img.astype(np.float32) * (1 - alpha) + shadow * alpha).astype(np.uint8))

    def _draw_node(self, img: np.ndarray, node: Node) -> None:
        s = self.s
        fill, accent = TYPE_STYLE.get(node.node_type, DEFAULT_STYLE)
        top = node.y - node.h / 2
        rounded_rect(img, node.x * s, top * s, node.w * s, node.h * s, self.radius * s, fill, -1)
        rounded_rect(
            img, node.x * s, top * s, node.w * s, node.h * s, self.radius * s,
            accent, max(1, int(round(0.9 * s))),
        )
        # Accent bar hugging the left edge, clipped to the rounded corners.
        bar = np.zeros(img.shape[:2], dtype=np.uint8)
        rounded_rect(bar, node.x * s, top * s, node.w * s, node.h * s, self.radius * s, 255, -1)
        cv2.rectangle(
            bar,
            (int((node.x + 4.5) * s), 0),
            (bar.shape[1], bar.shape[0]),
            0,
            -1,
        )
        img[bar > 0] = accent

        text_y = node.y - (len(node.lines) - 1) * self.line_h / 2 + 4.0
        for line in node.lines:
            put_text(
                img,
                line,
                ((node.x + node.w / 2 + 2.5) * s, text_y * s),
                FONT,
                self.node_fs * s,
                INK,
                max(1, int(round(self.node_th * s * 0.62))),
                anchor="center",
            )
            text_y += self.line_h

    def _edge_points(self, a: Node, b: Node) -> np.ndarray:
        (x0, y0), (x1, y1) = a.right, b.left
        stretch = max(38.0, (x1 - x0) * 0.45)
        return bezier((x0, y0), (x0 + stretch, y0), (x1 - stretch, y1), (x1, y1))

    def _draw_edges(self, img: np.ndarray) -> None:
        s = self.s
        for src, tgt, predicate in self.edges:
            colour, dashed = EDGE_STYLE.get(predicate, ((160, 160, 160), False))
            a, b = self.nodes[src], self.nodes[tgt]
            pts = self._edge_points(a, b) * s
            pts[-1, 0] -= 5.0 * s  # leave room for the head
            thickness = max(1, int(round(1.35 * s)))
            draw_polyline(img, pts, colour, thickness, dashed, dash=9 * s, gap=6 * s)
            arrow_head(img, pts, colour, 8.0 * s)

        colour, dashed = EDGE_STYLE["targets"]
        for tgt, _drugs, (x, y, w, _h) in self.treat_groups:
            target = self.nodes[tgt]
            x0, y0 = x + w / 2, y
            x1, y1 = target.cx, target.y + target.h / 2 + 4.0
            lift = max(34.0, (y0 - y1) * 0.45)
            pts = bezier((x0, y0), (x0, y0 - lift), (x1, y1 + lift), (x1, y1)) * s
            thickness = max(1, int(round(1.5 * s)))
            draw_polyline(img, pts, colour, thickness, dashed, dash=9 * s, gap=6 * s)
            blunt_head(img, pts, colour, 11.0 * s, thickness + max(1, s // 2))

    def _draw_header(self, img: np.ndarray) -> None:
        s = self.s
        x = self.margin * s
        put_text(img, self.title, (x, 44 * s), FONT, 0.86 * s, INK, max(1, int(1.15 * s)))
        put_text(img, self.subtitle, (x, 70 * s), FONT_LIGHT, 0.42 * s, MUTED, max(1, s - 1))
        cv2.line(
            img,
            (int(x), int(86 * s)),
            (int(self.width * s - self.margin * s), int(86 * s)),
            HAIRLINE,
            max(1, s // 2),
            cv2.LINE_AA,
        )

    def _draw_legend(self, img: np.ndarray) -> None:
        s = self.s
        present = {n.node_type for n in self.nodes.values()}
        if self.treatments:
            present.add("treatment")
        order = [
            ("genetic", "gene / variant"),
            ("pathophysiology", "mechanism"),
            ("biochemical", "biochemical readout"),
            ("phenotype", "phenotype"),
            ("environmental", "environmental"),
            ("treatment", "treatment"),
            ("orphan", "unresolved target"),
        ]
        y = self.height - self.legend_h + 18.0
        cv2.line(
            img,
            (int(self.margin * s), int((y - 16) * s)),
            (int((self.width - self.margin) * s), int((y - 16) * s)),
            HAIRLINE,
            max(1, s // 2),
            cv2.LINE_AA,
        )
        x = self.margin
        for key, label in order:
            if key not in present:
                continue
            fill, accent = TYPE_STYLE[key]
            rounded_rect(img, x * s, (y - 8) * s, 15 * s, 11 * s, 3 * s, fill, -1)
            rounded_rect(img, x * s, (y - 8) * s, 15 * s, 11 * s, 3 * s, accent, max(1, s // 2))
            put_text(img, label, ((x + 21) * s, y * s), FONT_LIGHT, 0.36 * s, MUTED, max(1, s - 1))
            x += 21 + text_size(label, FONT_LIGHT, 0.36, 1)[0] + 26

        drawn = {p for _s, _t, p in self.edges}
        if self.treat_groups:
            drawn.add("targets")
        for predicate, label in (
            ("causes", "causes"),
            ("contributes_to", "contributes to"),
            ("variant_of", "variant of"),
            ("readout", "readout"),
            ("targets", "inhibits"),
        ):
            if predicate not in drawn:
                continue
            colour, dashed = EDGE_STYLE[predicate]
            pts = np.array([[x, y - 3], [x + 22, y - 3]], dtype=float) * s
            draw_polyline(img, pts, colour, max(1, int(1.2 * s)), dashed, dash=5 * s, gap=4 * s)
            if predicate == "targets":
                cv2.line(
                    img,
                    (int((x + 22) * s), int((y - 8) * s)),
                    (int((x + 22) * s), int((y + 2) * s)),
                    colour,
                    max(1, int(1.2 * s)),
                    cv2.LINE_AA,
                )
            else:
                tri = np.array(
                    [[x + 24, y - 3], [x + 18, y - 6], [x + 18, y]], dtype=float
                ) * s
                cv2.fillConvexPoly(img, np.round(tri).astype(np.int32), colour, cv2.LINE_AA)
            put_text(img, label, ((x + 30) * s, y * s), FONT_LIGHT, 0.36 * s, MUTED, max(1, s - 1))
            x += 30 + text_size(label, FONT_LIGHT, 0.36, 1)[0] + 22


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("disorder", type=Path, help="path to a kb/disorders/*.yaml file")
    ap.add_argument("-o", "--out", type=Path, default=Path("pathograph.png"))
    ap.add_argument("--scale", type=int, default=3, help="supersampling factor")
    args = ap.parse_args()

    disorder = safe_load(args.disorder.read_text())
    graph = build_causal_graph(disorder)
    if not graph.edges:
        raise SystemExit(f"{args.disorder} has no causal edges to draw")

    n_nodes = len({n for e in graph.edges for n in (e.source, e.target)})
    renderer = PathographRenderer(
        graph,
        title=disorder.get("name", args.disorder.stem).replace("_", " "),
        subtitle=f"pathograph - {n_nodes} nodes, {len(graph.edges)} causal edges - drawn with OpenCV",
        scale=args.scale,
    )
    renderer.build()
    img = renderer.render()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(args.out), img)
    print(f"wrote {args.out} ({img.shape[1]}x{img.shape[0]})")


if __name__ == "__main__":
    main()
