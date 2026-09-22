"""Controlled variant classes reach mechanism and phenotype genetic contexts."""

import html as html_lib
import json
import re
from pathlib import Path

import pytest
import yaml

from dismech.graph import build_causal_graph, graph_to_json
from dismech.render import render_disorder, render_module


def _disorder(context: dict) -> dict:
    return {
        "name": "Example regulatory disorder",
        "pathophysiology": [
            {
                "name": "Structural rearrangement",
                "genetic_context": context,
                "downstream": [{"target": "Limb abnormality"}],
            }
        ],
        "phenotypes": [
            {
                "name": "Limb abnormality",
                "phenotype_contexts": [{"genetic_context": context}],
            }
        ],
    }


@pytest.mark.parametrize(
    "context",
    [
        {
            "variant_type": "deletion",
            "genomic_contexts": ["coding sequence", "intergenic region"],
            "allele_type": "approximately 2 Mb microdeletion",
        },
        {"variant_type": "inversion"},
        {"allele_type": "legacy structural rearrangement"},
    ],
)
def test_graph_preserves_controlled_and_legacy_genetic_context(context: dict) -> None:
    disorder = _disorder(context)
    payload = json.loads(graph_to_json(build_causal_graph(disorder), disorder))
    trigger = next(
        node for node in payload["nodes"] if node["id"] == "Structural rearrangement"
    )

    assert trigger["meta"]["genetic_context"] == context


@pytest.mark.parametrize("module_page", [False, True])
@pytest.mark.parametrize(
    ("regulatory_category", "confidence", "expected_label"),
    [
        ("GOE", "HYPOTHETICAL", "Regulatory category: GOE (Hypothetical)"),
        (None, "PROVISIONAL", "Mechanism confidence: Provisional"),
    ],
)
def test_rendered_mechanism_preserves_classification_confidence(
    tmp_path: Path,
    module_page: bool,
    regulatory_category: str | None,
    confidence: str,
    expected_label: str,
) -> None:
    mechanism = {
        "name": "Proposed ectopic expression",
        "mechanism_confidence": confidence,
        "downstream": [{"target": "Altered limb development"}],
    }
    if regulatory_category:
        mechanism["regulatory_category"] = regulatory_category
    record = {
        "name": "Regulatory example",
        "pathophysiology": [mechanism, {"name": "Altered limb development"}],
    }
    if module_page:
        record["category"] = "Module"
    yaml_path = tmp_path / "regulatory_example.yaml"
    yaml_path.write_text(yaml.safe_dump(record, sort_keys=False))
    output_path = tmp_path / "pages" / "regulatory_example.html"

    if module_page:
        render_module(yaml_path, output_path=output_path, usage_index={})
    else:
        render_disorder(yaml_path, output_path=output_path)
    html = output_path.read_text()

    assert re.search(
        rf'<span class="tag[^\"]*">{re.escape(expected_label)}</span>', html
    )
    graph_match = re.search(r'var graphData = JSON\.parse\((".*?")\);', html, re.DOTALL)
    assert graph_match is not None
    graph_data = json.loads(json.loads(graph_match.group(1)))
    meta = next(
        node["meta"]
        for node in graph_data["nodes"]
        if node["id"] == "Proposed ectopic expression"
    )
    assert meta["mechanism_confidence"] == confidence
    assert meta.get("regulatory_category") == regulatory_category


def test_render_genetic_context_fields_on_mechanism_and_phenotype(
    tmp_path: Path,
) -> None:
    context = {
        "variant_type": "deletion",
        "genomic_contexts": ["5' UTR", "intergenic region"],
        "allele_type": "promoter deletion with legacy detail",
    }
    disorder_path = tmp_path / "Example_regulatory_disorder.yaml"
    disorder_path.write_text(yaml.safe_dump(_disorder(context), sort_keys=False))
    output_path = tmp_path / "pages" / "disorders" / "Example_regulatory_disorder.html"

    render_disorder(disorder_path, output_path=output_path)
    html = output_path.read_text()
    visible_html = html_lib.unescape(html)

    # Require actual visible badges in both sections, not just raw YAML or JSON.
    for label in (
        "Variant type: deletion",
        "Genomic context: 5' UTR",
        "Genomic context: intergenic region",
    ):
        assert f'<span class="tag tag-classification">{label}</span>' in visible_html
        assert re.search(
            rf'<span class="context-gene-tag"[^>]*>{re.escape(label)}</span>',
            visible_html,
        )
    assert "allele_type: promoter deletion with legacy detail</span>" in html
    assert re.search(
        r'<span class="context-gene-tag"[^>]*>promoter deletion with legacy detail</span>',
        html,
    )

    graph_match = re.search(r'var graphData = JSON\.parse\((".*?")\);', html, re.DOTALL)
    assert graph_match is not None
    graph_data = json.loads(json.loads(graph_match.group(1)))
    trigger = next(
        node for node in graph_data["nodes"] if node["id"] == "Structural rearrangement"
    )
    assert trigger["meta"]["genetic_context"] == context
