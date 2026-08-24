"""Tests for rendering variant entries as cards (issue #8037).

Variants are drawn as ``genetic`` pathograph nodes but used to have no card
anywhere on the disorder page, so clicking one led nowhere. These tests cover
both placements: disease-level ``variants:`` get their own section, and
per-gene ``genetic[].variants:`` render inside their gene's card.
"""

import html as html_lib
import json
import re
from collections import Counter
from pathlib import Path

import yaml

from dismech.graph import build_causal_graph, graph_to_json
from dismech.render import render_disorder

CARD_RE = re.compile(r'data-dismech-node="([^"]*)" data-dismech-type="([a-z_]*)"')

DISORDER = {
    "name": "Example Disease",
    "pathophysiology": [
        {"name": "CFTR Dysfunction", "downstream": [{"target": "Bronchiectasis"}]}
    ],
    "phenotypes": [{"name": "Bronchiectasis"}],
    "genetic": [
        {
            "name": "CFTR",
            "downstream": [{"target": "CFTR Dysfunction"}],
            "variants": [
                {
                    "name": "CFTR c.1521_1523del (p.Phe508del)",
                    "description": "The most common CFTR allele.",
                    "clinical_significance": "PATHOGENIC",
                    "type": "inframe_deletion",
                    "gene": {
                        "preferred_term": "CFTR",
                        "term": {"id": "hgnc:1884", "label": "CFTR"},
                    },
                    "synonyms": ["F508del"],
                    "identifiers": ["CLINVAR:7105"],
                    "functional_effects": [
                        {
                            "function": "chloride channel activity",
                            "description": "Misfolding blocks trafficking.",
                            "type": "loss-of-function",
                        }
                    ],
                    "external_assertions": [
                        {
                            "name": "Allele registry record",
                            "source": "ClinGen Allele Registry",
                            "assertion_type": "allele registry record",
                            "external_id": "CA123456",
                            "url": "https://example.org/CA123456",
                            "description": "Canonical allele identifier.",
                        }
                    ],
                }
            ],
        }
    ],
    "variants": [
        {
            "name": "CFTR c.3718-2477C>T",
            "description": "Deep intronic splicing allele.",
            "clinical_significance": "LIKELY_PATHOGENIC",
        }
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


def test_variant_pathograph_nodes_have_cards(tmp_path: Path) -> None:
    """The gap this issue reports: every variant node now resolves to a card."""
    html = _render(tmp_path, DISORDER)
    graph = build_causal_graph(DISORDER)
    payload = json.loads(graph_to_json(graph, DISORDER))

    cards = _cards(html)
    variant_nodes = [
        n["id"]
        for n in payload["nodes"]
        if n["id"].startswith("CFTR c.") and n["node_type"] == "genetic"
    ]
    assert variant_nodes, "fixture should put variants in the pathograph"
    for node_id in variant_nodes:
        assert (node_id, "genetic") in cards, f"variant {node_id!r} has no card"


def test_disease_level_variants_render_their_own_section(tmp_path: Path) -> None:
    """Disease-level variants get a top-level Variants card."""
    html = _render(tmp_path, DISORDER)
    assert '<div class="card" id="variants">' in html
    assert "CFTR c.3718-2477C&gt;T" in html
    assert "Deep intronic splicing allele." in html
    assert 'id="variant-cftr-c-3718-2477c-t"' in html


def test_gene_nested_variants_render_inside_the_gene_card(tmp_path: Path) -> None:
    """Per-gene variants render in a collapsible block within the gene card."""
    html = _render(tmp_path, DISORDER)
    assert '<details class="variant-list">' in html
    assert "Variants (1)" in html
    assert 'class="item-box variant-box variant-box-nested anchor-target"' in html


def test_variant_detail_fields_are_rendered(tmp_path: Path) -> None:
    """The fields curators actually populate all reach the page."""
    html = _render(tmp_path, DISORDER)
    # clinical significance badge, variant type, gene link
    assert "variant-significance-pathogenic" in html
    assert "variant-significance-likely-pathogenic" in html
    assert "inframe deletion" in html
    assert "hgnc:1884" in html
    # synonyms, identifiers
    assert "F508del" in html
    assert "CLINVAR:7105" in html
    # functional effects
    assert "Functional effects" in html
    assert "chloride channel activity" in html
    assert "Misfolding blocks trafficking." in html
    # external assertions -- the curator-written name disambiguates two
    # assertions that otherwise render as an identical source/type tag pair
    assert "External assertions" in html
    assert "Allele registry record" in html
    assert "ClinGen Allele Registry" in html
    assert "https://example.org/CA123456" in html


def test_variants_stat_tile_counts_both_placements(tmp_path: Path) -> None:
    """The stat bar counts disease-level plus gene-nested variants."""
    html = _render(tmp_path, DISORDER)
    stat = re.search(
        r'<div class="stat-value">(\d+)</div>\s*<div class="stat-label">Variants</div>',
        html,
    )
    assert stat, "expected a Variants stat tile"
    assert stat.group(1) == "2"


def test_variants_stat_links_to_genetic_without_a_variants_section(
    tmp_path: Path,
) -> None:
    """With only gene-nested variants the tile points at the genetic card."""
    disorder = {k: v for k, v in DISORDER.items() if k != "variants"}
    html = _render(tmp_path, disorder)
    assert '<div class="card" id="variants">' not in html
    assert '<a class="stat-link" href="#genetic">' in html


def test_variant_anchor_ids_are_unique(tmp_path: Path) -> None:
    """Same-named variants under different genes get distinct anchors."""
    disorder = dict(DISORDER)
    disorder["genetic"] = [
        {"name": "GENE_A", "variants": [{"name": "Truncating variants"}]},
        {"name": "GENE_B", "variants": [{"name": "Truncating variants"}]},
    ]
    disorder["variants"] = [{"name": "Truncating variants"}]
    html = _render(tmp_path, disorder)

    variant_ids = re.findall(r'id="(variant-[^"]*)"', html)
    assert len(variant_ids) == 3
    assert len(set(variant_ids)) == 3
    duplicates = [
        i for i, c in Counter(re.findall(r'\sid="([^"]+)"', html)).items() if c > 1
    ]
    assert not duplicates, f"duplicate element IDs on the page: {duplicates}"


def test_external_assertion_urls_are_scheme_guarded(tmp_path: Path) -> None:
    """A curated non-http URL must not become a clickable link."""
    disorder = dict(DISORDER)
    disorder["variants"] = [
        {
            "name": "Suspicious allele",
            "external_assertions": [
                {
                    "name": "Bad link",
                    "external_id": "XX1",
                    "url": "javascript:alert(1)",
                }
            ],
        }
    ]
    html = _render(tmp_path, disorder)
    assert "Bad link" in html
    assert "XX1" in html
    # The raw-YAML footer echoes the source, so assert on the rendered link only.
    assert 'href="javascript:' not in html
    assert 'curie-chip" href="javascript:' not in html


def test_functional_effect_regulatory_fields_render(tmp_path: Path) -> None:
    """The regulatory-variant slots on FunctionalEffect reach the page."""
    disorder = dict(DISORDER)
    disorder["variants"] = [
        {
            "name": "Enhancer allele",
            "functional_effects": [
                {
                    "function": "enhancer activity",
                    "regulatory_element_type": "ENHANCER",
                    "regulatory_mechanism": "Loss of TF binding.",
                    "affected_developmental_stage": "fetal liver",
                    "affected_cell_types": [
                        {
                            "preferred_term": "hepatocyte",
                            "term": {"id": "CL:0000182", "label": "hepatocyte"},
                        }
                    ],
                }
            ],
        }
    ]
    html = _render(tmp_path, disorder)
    assert "ENHANCER" in html
    assert "Loss of TF binding." in html
    assert "Developmental stage:" in html
    assert "fetal liver" in html
    assert "hepatocyte" in html
