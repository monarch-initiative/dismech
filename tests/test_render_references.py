"""Tests for top-level reference rendering on disorder pages."""

from pathlib import Path

import yaml

from dismech.render import curie_to_url, render_disorder


def _write_disorder(path: Path, data: dict) -> None:
    path.write_text(yaml.safe_dump(data, sort_keys=False))


def test_render_disorder_shows_top_level_references_with_findings(
    tmp_path: Path,
) -> None:
    """Disorder pages should render top-level references, findings, and supporting text."""
    disorder_path = tmp_path / "Reference_Disorder.yaml"
    output_path = tmp_path / "pages" / "disorders" / "Reference_Disorder.html"

    _write_disorder(
        disorder_path,
        {
            "name": "Reference Disorder",
            "references": [
                {
                    "reference": "PMID:3159974",
                    "title": "Molecular basis of Down syndrome phenotypes.",
                    "findings": [
                        {
                            "statement": "Chromosome 21 triplication produces broad developmental effects.",
                            "supporting_text": "The extra chromosome 21 dosage perturbs multiple developmental pathways.",
                            "evidence": [
                                {
                                    "reference": "PMID:3159974",
                                    "supports": "SUPPORT",
                                    "snippet": "The extra chromosome 21 dosage perturbs multiple developmental pathways.",
                                    "explanation": "Supports the top-level summary finding.",
                                }
                            ],
                        }
                    ],
                }
            ],
        },
    )

    render_disorder(disorder_path, output_path=output_path)
    html = output_path.read_text()

    assert '<div class="card reference-card" id="references">' in html
    assert f'href="{curie_to_url("PMID:3159974")}"' in html
    assert "Molecular basis of Down syndrome phenotypes." in html
    assert "Chromosome 21 triplication produces broad developmental effects." in html
    assert (
        "The extra chromosome 21 dosage perturbs multiple developmental pathways."
        in html
    )
    assert "Show evidence (1 reference)" in html


def test_render_disorder_references_without_findings_show_empty_state(
    tmp_path: Path,
) -> None:
    """Reference entries without findings should still render a stable empty state."""
    disorder_path = tmp_path / "Reference_Disorder.yaml"
    output_path = tmp_path / "pages" / "disorders" / "Reference_Disorder.html"

    _write_disorder(
        disorder_path,
        {
            "name": "Reference Disorder",
            "references": [
                {
                    "reference": "PMID:1671712",
                    "title": "Down syndrome developmental review.",
                    "findings": [],
                }
            ],
        },
    )

    render_disorder(disorder_path, output_path=output_path)
    html = output_path.read_text()

    assert "Down syndrome developmental review." in html
    assert "No top-level findings curated for this source." in html
