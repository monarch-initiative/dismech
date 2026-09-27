"""Qualitative sequence landmarks survive presentation without implying causality."""

import csv
import json
import re
from pathlib import Path

import pytest
import yaml

from dismech.export.browser_export import BrowserExporter
from dismech.export.cx2_export import disorder_to_cx2
from dismech.export.tabular_export import TabularExporter
from dismech.graph import build_causal_graph, graph_to_json
from dismech.render import render_disorder, render_module


@pytest.fixture
def regions() -> list[dict]:
    epha4 = {"preferred_term": "EPHA4", "term": {"id": "hgnc:3388", "label": "EPHA4"}}
    pax3 = {"preferred_term": "PAX3", "term": {"id": "hgnc:8617", "label": "PAX3"}}
    return [
        {
            "name": "EPHA4-PAX3 boundary",
            "chromosomal_region": "2q36.1",
            "regulatory_element_type": "TAD_BOUNDARY",
            "between_genes": [epha4, pax3],
            "description": "A boundary region, not the extent of the whole deletion.",
        },
        {"name": "Intragenic interval", "within_gene": epha4},
        {"name": "Gene-overlapping interval", "overlaps_genes": [epha4]},
        {"name": "Gene-abutting interval", "adjacent_to_genes": [pax3]},
    ]


@pytest.fixture
def region_record(regions: list[dict]) -> dict:
    context = {"variant_type": "deletion", "affected_regions": regions}
    return {
        "name": "Regional example",
        "pathophysiology": [
            {
                "name": "Physical rearrangement",
                "genetic_context": context,
                "downstream": [{"target": "Developmental abnormality"}],
            },
            # These provide possible targets for any accidental gene-based
            # inference from the positional landmarks.
            {"name": "EPHA4 activity", "genes": [regions[0]["between_genes"][0]]},
            {"name": "PAX3 activity", "genes": [regions[0]["between_genes"][1]]},
        ],
        "phenotypes": [
            {
                "name": "Developmental abnormality",
                "phenotype_contexts": [{"genetic_context": context}],
            }
        ],
        "genetic": [
            {
                "name": "Regional rearrangements",
                "affected_regions": regions,
                "variants": [{"name": "Regional allele", "affected_regions": regions}],
            }
        ],
    }


def test_graph_keeps_regions_separate_from_causal_genes(
    region_record: dict, regions: list[dict]
) -> None:
    graph = build_causal_graph(region_record)
    assert {(e.source, e.target, e.predicate) for e in graph.edges} == {
        ("Physical rearrangement", "Developmental abnormality", "causes"),
        ("Regional allele", "Regional rearrangements", "variant_of"),
    }
    nodes = {
        node["id"]: node
        for node in json.loads(graph_to_json(graph, region_record))["nodes"]
    }
    for name in (
        "Regional rearrangements",
        "Regional allele",
        "Physical rearrangement",
    ):
        meta = nodes[name]["meta"]
        assert "genes" not in meta
        assert "gene_terms" not in meta
        source = meta["genetic_context"] if name == "Physical rearrangement" else meta
        assert source["affected_regions"] == regions
        assert "gene_terms" not in source


def test_cx2_retains_region_structure_without_gene_annotations(
    region_record: dict, regions: list[dict]
) -> None:
    aspects = {
        key: value
        for aspect in disorder_to_cx2(region_record)
        for key, value in aspect.items()
    }
    nodes = {node["v"]["name"]: node["v"] for node in aspects["nodes"]}
    for name in (
        "Regional rearrangements",
        "Regional allele",
        "Physical rearrangement",
    ):
        attributes = nodes[name]
        prefix = "genetic_context_" if name == "Physical rearrangement" else ""
        assert attributes[f"{prefix}affected_regions"] == [
            region["name"] for region in regions
        ]
        assert json.loads(attributes[f"{prefix}affected_regions_json"]) == regions
        assert "genes" not in attributes
        assert "represents" not in attributes
    # The two explicit structural links are the only edges in either format.
    assert len(aspects["edges"]) == 2


@pytest.mark.parametrize("bound_gene", [False, True])
def test_gene_like_region_name_needs_an_explicit_gene_descriptor(
    region_record: dict, regions: list[dict], bound_gene: bool
) -> None:
    regional_row = region_record["genetic"][0]
    regional_row["name"] = "EPHA4"
    if bound_gene:
        regional_row["gene_term"] = regions[0]["between_genes"][0]
    graph = build_causal_graph(region_record)
    inferred = [e for e in graph.edges if e.source == "EPHA4"]
    assert [(e.target, e.predicate) for e in inferred] == (
        [("EPHA4 activity", "contributes_to")] if bound_gene else []
    )
    aspects = {
        key: value
        for aspect in disorder_to_cx2(region_record)
        for key, value in aspect.items()
    }
    attributes = next(
        node["v"] for node in aspects["nodes"] if node["v"]["name"] == "EPHA4"
    )
    assert attributes.get("iquery_gene_symbols", []) == (
        ["EPHA4"] if bound_gene else []
    )
    browser_record = BrowserExporter().extract_disorder(region_record, "example.yaml")
    assert browser_record["genes"] == (["EPHA4"] if bound_gene else [])


@pytest.mark.parametrize("module_page", [False, True])
def test_visible_region_cards_and_pathograph_metadata(
    tmp_path: Path, region_record: dict, regions: list[dict], module_page: bool
) -> None:
    if module_page:
        region_record["category"] = "Module"
    source = tmp_path / "regional_example.yaml"
    source.write_text(yaml.safe_dump(region_record, sort_keys=False))
    output = tmp_path / "pages" / "regional_example.html"
    if module_page:
        render_module(source, output_path=output, usage_index={})
    else:
        render_disorder(source, output_path=output)
    html = output.read_text()
    # Match visible cards, not embedded YAML or JavaScript strings. The disorder
    # has one card each on the trigger, phenotype context, regional row and allele.
    assert html.count('<div class="affected-regions">') == (1 if module_page else 4)
    for label in (
        "Between genes:",
        "Within gene:",
        "Overlaps genes:",
        "Abuts genes (shared boundary):",
    ):
        assert f"<span>{label}</span>" in html
    assert "<strong>EPHA4-PAX3 boundary</strong>" in html
    assert 'href="https://bioregistry.io/hgnc:3388"' in html
    graph_match = re.search(r'var graphData = JSON\.parse\((".*?")\);', html, re.DOTALL)
    assert graph_match
    payload = json.loads(json.loads(graph_match.group(1)))
    trigger = next(
        node for node in payload["nodes"] if node["id"] == "Physical rearrangement"
    )
    assert trigger["meta"]["genetic_context"]["affected_regions"] == regions


def test_tabular_export_preserves_regions_and_positional_descriptor_paths(
    tmp_path: Path, region_record: dict, regions: list[dict]
) -> None:
    source = tmp_path / "regional_example.yaml"
    source.write_text(yaml.safe_dump(region_record, sort_keys=False))
    output = tmp_path / "tables"
    TabularExporter().export([source], output)
    with (output / "assertions.tsv").open() as stream:
        rows = {row["name"]: row for row in csv.DictReader(stream, delimiter="\t")}
    assert (
        json.loads(rows["Regional rearrangements"]["raw_json"])["affected_regions"]
        == regions
    )
    assert (
        json.loads(rows["Physical rearrangement"]["raw_json"])["genetic_context"][
            "affected_regions"
        ]
        == regions
    )
    with (output / "descriptors.tsv").open() as stream:
        descriptors = list(csv.DictReader(stream, delimiter="\t"))
    assert any(
        row["path"] == "genetic_context.affected_regions[0].between_genes[1]"
        and row["term_id"] == "hgnc:8617"
        for row in descriptors
    )


def test_kgx_does_not_turn_region_landmarks_into_gene_disease_associations(
    region_record: dict,
) -> None:
    pytest.importorskip("biolink_model")
    from dismech.export.kgx_export import extract_nodes, transform

    region_record["disease_term"] = {
        "preferred_term": "Example disease",
        "term": {"id": "MONDO:0000001", "label": "disease"},
    }
    # KGX has no regional entity model. Positional genes must not leak into its
    # curated gene-disease associations or acquire invented gene identifiers.
    assert not any(
        "Gene" in str(node.category) for node in extract_nodes(region_record)
    )
    assert not list(transform(region_record))
