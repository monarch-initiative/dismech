"""Regression tests for rendered pathograph payloads."""

import json
import re
from collections import defaultdict, deque
from pathlib import Path

from dismech.render import render_disorder


def _extract_graph_data(html: str) -> dict:
    """Extract the embedded graphData payload from a rendered disorder page."""
    match = re.search(r"var graphData = JSON\.parse\((\".*?\")\);", html, re.S)
    assert match is not None, "Rendered HTML did not include graphData payload"
    return json.loads(json.loads(match.group(1)))


def _connected_component_count(graph_data: dict) -> int:
    """Return the number of connected components in an undirected view of the graph."""
    adjacency: dict[str, set[str]] = defaultdict(set)
    nodes = {node["id"] for node in graph_data.get("nodes", [])}

    for edge in graph_data.get("edges", []):
        source = edge["source"]
        target = edge["target"]
        adjacency[source].add(target)
        adjacency[target].add(source)
        nodes.add(source)
        nodes.add(target)

    remaining = set(nodes)
    components = 0
    while remaining:
        components += 1
        start = remaining.pop()
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neighbor in adjacency[node]:
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    queue.append(neighbor)
    return components


def test_rendered_crohn_pathograph_payload_is_connected(tmp_path: Path) -> None:
    """Crohn's rendered graph payload should remain a single connected graph."""
    repo_root = Path(__file__).resolve().parents[1]
    disorder_path = repo_root / "kb" / "disorders" / "Crohn_Disease.yaml"
    output_path = tmp_path / "pages" / "disorders" / "Crohn_Disease.html"

    render_disorder(disorder_path, output_path=output_path)
    graph_data = _extract_graph_data(output_path.read_text())
    edges = {(edge["source"], edge["target"]) for edge in graph_data["edges"]}

    assert (
        "Dysregulated Immune Response",
        "Intestinal Inflammation and Epithelial Injury",
    ) in edges
    assert (
        "Antimicrobial Defense Deficiency",
        "Intestinal Barrier Dysfunction",
    ) in edges
    assert (
        "Intestinal Barrier Dysfunction",
        "Dysregulated Immune Response",
    ) in edges
    assert (
        "Intestinal Inflammation and Epithelial Injury",
        "Diarrhea",
    ) in edges
    assert (
        "TL1A-Mediated T Cell Activation",
        "Dysregulated Immune Response",
    ) in edges
    assert (
        "Dysregulated Immune Response",
        "Diarrhea",
    ) not in edges
    assert _connected_component_count(graph_data) == 1
