"""Tests for disorder model sections in rendered pages."""

import re
from pathlib import Path

import yaml

from dismech.render import render_disorder


def _write_disorder(path: Path, data: dict) -> None:
    path.write_text(yaml.safe_dump(data, sort_keys=False))


def _models_stat_pattern(count: int) -> str:
    return (
        r'href="#models">\s*<div class="stat-item">\s*<div class="stat-value">'
        f"{count}"
        r"</div>\s*<div class=\"stat-label\">Models</div>"
    )


def _card_title_pattern(title: str) -> str:
    return rf"<h2 class=\"card-title\">{re.escape(title)}</h2>"


def test_render_disorder_combines_experimental_and_computational_models(
    tmp_path: Path,
) -> None:
    """The top-level models stat should include both experimental and computational entries."""
    disorder_path = tmp_path / "Model_Disorder.yaml"
    output_path = tmp_path / "pages" / "disorders" / "Model_Disorder.html"

    _write_disorder(
        disorder_path,
        {
            "name": "Model Disorder",
            "experimental_models": [
                {
                    "name": "Patient-derived airway organoid model",
                    "description": "Airway organoid platform for mutation-resolved testing.",
                    "experimental_model_type": "ORGANOID",
                    "namo_type": "namo:Organoid",
                    "organism": {
                        "preferred_term": "human",
                        "term": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
                    },
                    "tissue_term": {
                        "preferred_term": "respiratory airway",
                        "term": {
                            "id": "UBERON:0001005",
                            "label": "respiratory airway",
                        },
                    },
                    "cell_types": [
                        {
                            "preferred_term": "bronchial epithelial cell",
                            "term": {
                                "id": "CL:0002328",
                                "label": "bronchial epithelial cell",
                            },
                        }
                    ],
                    "conditions": ["disease state", "microbial challenge"],
                    "cell_source": "Patient-derived airway epithelial cells",
                    "culture_system": "Three-dimensional organoid culture",
                    "publication": "PMID:12345678",
                }
            ],
            "computational_models": [
                {
                    "name": "Flux Balance Model",
                    "description": "Constraint-based metabolic model.",
                    "model_type": "GENOME_SCALE_METABOLIC",
                    "publication": "PMID:23456789",
                }
            ],
        },
    )

    render_disorder(disorder_path, output_path=output_path)
    html = output_path.read_text()

    assert re.search(_models_stat_pattern(2), html)
    assert re.search(_card_title_pattern("Experimental Models"), html)
    assert "Patient-derived airway organoid model" in html
    assert "namo:Organoid" in html
    assert "microbial challenge" in html
    assert re.search(_card_title_pattern("Computational Models"), html)
    assert "Flux Balance Model" in html
    assert re.search(
        r'<div class="card" id="models">\s*<div class="card-header">.*?Experimental Models',
        html,
        re.S,
    )


def test_render_disorder_anchors_models_to_experimental_section_when_only_experimental(
    tmp_path: Path,
) -> None:
    """Experimental-model-only pages should still expose the models section and stat link."""
    disorder_path = tmp_path / "Experimental_Disorder.yaml"
    output_path = tmp_path / "pages" / "disorders" / "Experimental_Disorder.html"

    _write_disorder(
        disorder_path,
        {
            "name": "Experimental Disorder",
            "experimental_models": [
                {
                    "name": "Disease organ-on-chip",
                    "experimental_model_type": "ORGAN_ON_CHIP",
                    "namo_type": "namo:OrganOnChip",
                    "culture_system": "Microfluidic chip",
                }
            ],
        },
    )

    render_disorder(disorder_path, output_path=output_path)
    html = output_path.read_text()

    assert re.search(_models_stat_pattern(1), html)
    assert re.search(_card_title_pattern("Experimental Models"), html)
    assert "Disease organ-on-chip" in html
    assert not re.search(_card_title_pattern("Computational Models"), html)
    assert re.search(
        r'<div class="card" id="models">\s*<div class="card-header">.*?Experimental Models',
        html,
        re.S,
    )


def test_render_disorder_keeps_computational_models_working(
    tmp_path: Path,
) -> None:
    """Computational-model-only pages should keep the pre-existing rendering behavior."""
    disorder_path = tmp_path / "Computational_Disorder.yaml"
    output_path = tmp_path / "pages" / "disorders" / "Computational_Disorder.html"

    _write_disorder(
        disorder_path,
        {
            "name": "Computational Disorder",
            "computational_models": [
                {
                    "name": "Mechanistic signaling model",
                    "model_type": "MECHANISTIC_NETWORK",
                    "model_software": "PySB",
                    "publication": "PMID:34567890",
                }
            ],
        },
    )

    render_disorder(disorder_path, output_path=output_path)
    html = output_path.read_text()

    assert re.search(_models_stat_pattern(1), html)
    assert not re.search(_card_title_pattern("Experimental Models"), html)
    assert re.search(_card_title_pattern("Computational Models"), html)
    assert "Mechanistic signaling model" in html
    assert "PySB" in html
    assert re.search(
        r'<div class="card" id="models">\s*<div class="card-header">.*?Computational Models',
        html,
        re.S,
    )


def test_render_disorder_exposes_pathograph_icon_mappings_for_model_types(
    tmp_path: Path,
) -> None:
    """Rendered pages should include lightweight icon mappings for graph model nodes."""
    disorder_path = tmp_path / "Icon_Disorder.yaml"
    output_path = tmp_path / "pages" / "disorders" / "Icon_Disorder.html"

    _write_disorder(
        disorder_path,
        {
            "name": "Icon Disorder",
            "pathophysiology": [
                {
                    "name": "Barrier Defect",
                    "downstream": [{"target": "Inflammation"}],
                }
            ],
            "phenotypes": [{"name": "Inflammation"}],
            "experimental_models": [
                {
                    "name": "Reusable airway cell line",
                    "experimental_model_type": "CELL_LINE",
                    "modeled_mechanisms": [{"target": "Barrier Defect"}],
                }
            ],
        },
    )

    render_disorder(disorder_path, output_path=output_path)
    html = output_path.read_text()

    assert 'experimental_model: "🧫"' in html
    assert 'CELL_LINE: "🧫"' in html
    assert 'ORGANOID: "◍"' in html
    assert 'ORGAN_ON_CHIP: "▣"' in html
