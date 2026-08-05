"""Tests for jumping from a pathograph node to its card (issue #8032).

Every node the pathograph draws should resolve to exactly one card carrying
matching ``data-dismech-node`` / ``data-dismech-type`` attributes, so the
graph's click handler can scroll the reader to the details.
"""

import html as html_lib
import json
import re
from pathlib import Path

import yaml

from dismech.graph import build_causal_graph, graph_to_json
from dismech.render import render_disorder

CARD_RE = re.compile(
    r'data-dismech-node="([^"]*)" data-dismech-type="([a-z_]*)"',
)

DISORDER = {
    "name": "Example Disease",
    "pathophysiology": [
        {
            "name": "CFTR Dysfunction",
            "downstream": [
                {"target": "Bronchiectasis"},
                {"target": "Sweat Chloride Elevation"},
            ],
        }
    ],
    "phenotypes": [
        {"name": "Bronchiectasis", "category": "Respiratory"},
        {"name": "Pancreatic Insufficiency", "category": "Gastrointestinal"},
    ],
    "genetic": [{"name": "CFTR", "downstream": [{"target": "CFTR Dysfunction"}]}],
    "biochemical": [{"name": "Sweat Chloride Elevation"}],
    "environmental": [
        {"name": "Tobacco Smoke Exposure", "downstream": [{"target": "Bronchiectasis"}]}
    ],
    "treatments": [
        {"name": "CFTR Modulator Therapy", "target_mechanisms": ["CFTR Dysfunction"]}
    ],
}


def _render(tmp_path: Path, disorder: dict) -> str:
    disorder_path = tmp_path / "Example_Disease.yaml"
    disorder_path.write_text(yaml.safe_dump(disorder, sort_keys=False))
    output_path = tmp_path / "pages" / "disorders" / "Example_Disease.html"
    render_disorder(disorder_path, output_path=output_path)
    return output_path.read_text()


def _cards(html: str) -> set[tuple[str, str]]:
    return {
        (html_lib.unescape(node), node_type)
        for node, node_type in CARD_RE.findall(html)
    }


def test_every_pathograph_node_has_a_matching_card(tmp_path: Path) -> None:
    """Each graph node resolves to a card of the same section type."""
    html = _render(tmp_path, DISORDER)
    graph = build_causal_graph(DISORDER)
    payload = json.loads(graph_to_json(graph, DISORDER))

    cards = _cards(html)
    assert payload["nodes"], "fixture should produce a pathograph"
    for node in payload["nodes"]:
        assert (node["id"], node["node_type"]) in cards, (
            f"pathograph node {node['id']!r} ({node['node_type']}) "
            "has no card to jump to"
        )


def test_card_anchor_ids_are_unique(tmp_path: Path) -> None:
    """Same-slug names in one section get distinct anchor IDs."""
    disorder = dict(DISORDER)
    disorder["phenotypes"] = [
        {"name": "Bronchiectasis"},
        {"name": "Bronchiectasis!"},
        {"name": "Pancreatic Insufficiency"},
    ]
    html = _render(tmp_path, disorder)

    anchor_ids = re.findall(r'id="(phenotype-[^"]*)"', html)
    assert "phenotype-bronchiectasis" in anchor_ids
    assert "phenotype-bronchiectasis-2" in anchor_ids
    assert len(anchor_ids) == len(set(anchor_ids))


def test_jump_helpers_are_wired_into_the_page(tmp_path: Path) -> None:
    """The pathograph click handler offers a jump affordance."""
    html = _render(tmp_path, DISORDER)
    assert "function jumpToCard(nodeId, nodeType)" in html
    assert "function findCardForNode(nodeId, nodeType)" in html
    assert "Jump to details" in html
    assert "dismech-jump-flash" in html
    # Clicking pins the tooltip so the jump button stays reachable.
    assert "pinnedNodeId = n.id;" in html
