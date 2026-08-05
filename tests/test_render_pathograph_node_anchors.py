"""Tests for jumping from a pathograph node to its card (issue #8032).

Every node the pathograph draws should resolve to exactly one card carrying
matching ``data-dismech-node`` / ``data-dismech-type`` attributes, so the
graph's click handler can scroll the reader to the details.
"""

import html as html_lib
import json
import re
from collections import Counter
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
    """Colliding slugs get distinct anchor IDs, even across suffix collisions."""
    disorder = dict(DISORDER)
    disorder["phenotypes"] = [
        {"name": "Bronchiectasis"},
        {"name": "Bronchiectasis!"},
        # Slugifies to the same value the de-dup suffix would hand the previous
        # item, so a naive counter would put two cards on phenotype-bronchiectasis-2.
        {"name": "Bronchiectasis 2"},
        {"name": "Pancreatic Insufficiency"},
    ]
    html = _render(tmp_path, disorder)

    phenotype_ids = re.findall(r'id="(phenotype-[^"]*)"', html)
    assert "phenotype-bronchiectasis" in phenotype_ids
    assert "phenotype-bronchiectasis-2" in phenotype_ids
    assert len(phenotype_ids) == len(set(phenotype_ids))


def test_page_has_no_duplicate_element_ids(tmp_path: Path) -> None:
    """Anchors must not collide with any other ID on the rendered page."""
    html = _render(tmp_path, DISORDER)
    all_ids = re.findall(r'\sid="([^"]+)"', html)
    duplicates = [item for item, count in Counter(all_ids).items() if count > 1]
    assert not duplicates, f"duplicate element IDs on the page: {duplicates}"


def test_jump_affordance_is_rendered(tmp_path: Path) -> None:
    """The pathograph offers a jump affordance wired to the card attributes."""
    html = _render(tmp_path, DISORDER)
    assert 'class="tt-jump"' in html
    assert "Jump to details" in html
    assert "dismech-jump-flash" in html
    # The handler resolves cards through the attribute pair the cards emit.
    assert "data-dismech-node" in html
    assert "data-dismech-type" in html


def test_semantic_ref_nodes_fall_back_to_the_named_card(tmp_path: Path) -> None:
    """A dangling "section#Name" ref still finds the card that Name refers to."""
    disorder = dict(DISORDER)
    disorder["pathophysiology"] = [
        {
            "name": "CFTR Dysfunction",
            "downstream": [{"target": "phenotype#Pancreatic Insufficiency"}],
        }
    ]
    html = _render(tmp_path, disorder)

    graph = build_causal_graph(disorder)
    payload = json.loads(graph_to_json(graph, disorder))
    orphans = [n["id"] for n in payload["nodes"] if n["node_type"] == "orphan"]
    assert "phenotype#Pancreatic Insufficiency" in orphans

    # The card the ref names is present, so the JS prefix fallback has a target.
    assert ("Pancreatic Insufficiency", "phenotype") in _cards(html)
    assert 'var hash = nodeId.indexOf("#");' in html
