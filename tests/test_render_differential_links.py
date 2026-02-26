"""Tests for internal differential diagnosis links in disorder page rendering."""

from pathlib import Path

import yaml

from dismech.render import _resolve_local_disorder_href, render_disorder


def _write_disorder(path: Path, data: dict) -> None:
    path.write_text(yaml.safe_dump(data, sort_keys=False))


def test_render_differential_links_to_local_disorder_page(tmp_path: Path) -> None:
    """Differential entries with a resolvable MONDO ID should link to local pages."""
    acne_path = tmp_path / "Acne_Vulgaris.yaml"
    rosacea_path = tmp_path / "Rosacea.yaml"

    _write_disorder(
        acne_path,
        {
            "name": "Acne Vulgaris",
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "acne vulgaris"}},
            "differential_diagnoses": [
                {
                    "name": "Rosacea",
                    "disease_term": {"term": {"id": "MONDO:0000002", "label": "rosacea"}},
                }
            ],
        },
    )
    _write_disorder(
        rosacea_path,
        {
            "name": "Rosacea",
            "disease_term": {"term": {"id": "MONDO:0000002", "label": "rosacea"}},
        },
    )

    output_path = tmp_path / "pages" / "disorders" / "Acne_Vulgaris.html"
    render_disorder(acne_path, output_path=output_path)

    html = output_path.read_text()
    assert 'href="Rosacea.html"' in html
    assert "MONDO:0000002" in html


def test_render_differential_links_by_name_fallback(tmp_path: Path) -> None:
    """Differential entries without a term should still link when name maps uniquely."""
    acne_path = tmp_path / "Acne_Vulgaris.yaml"
    rosacea_path = tmp_path / "Rosacea.yaml"

    _write_disorder(
        acne_path,
        {
            "name": "Acne Vulgaris",
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "acne vulgaris"}},
            "differential_diagnoses": [{"name": "Rosacea"}],
        },
    )
    _write_disorder(
        rosacea_path,
        {
            "name": "Rosacea",
            "disease_term": {"term": {"id": "MONDO:0000002", "label": "rosacea"}},
        },
    )

    output_path = tmp_path / "pages" / "disorders" / "Acne_Vulgaris.html"
    render_disorder(acne_path, output_path=output_path)

    html = output_path.read_text()
    assert 'href="Rosacea.html"' in html


def test_render_differential_skips_ambiguous_resolution(tmp_path: Path) -> None:
    """Differential entries should not link when MONDO resolution is ambiguous."""
    acne_path = tmp_path / "Acne_Vulgaris.yaml"
    _write_disorder(
        acne_path,
        {
            "name": "Acne Vulgaris",
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "acne vulgaris"}},
            "differential_diagnoses": [
                {
                    "name": "Unknown Differential",
                    "disease_term": {
                        "term": {"id": "MONDO:0000002", "label": "ambiguous disorder"}
                    },
                }
            ],
        },
    )
    _write_disorder(
        tmp_path / "Rosacea.yaml",
        {
            "name": "Rosacea",
            "disease_term": {"term": {"id": "MONDO:0000002", "label": "rosacea"}},
        },
    )
    _write_disorder(
        tmp_path / "Rosacea_Alternate.yaml",
        {
            "name": "Rosacea Alternate",
            "disease_term": {"term": {"id": "MONDO:0000002", "label": "rosacea alternate"}},
        },
    )

    output_path = tmp_path / "pages" / "disorders" / "Acne_Vulgaris.html"
    render_disorder(acne_path, output_path=output_path)

    html = output_path.read_text()
    assert 'class="item-name-link"' not in html
    assert 'href="Rosacea.html"' not in html
    assert 'href="Rosacea_Alternate.html"' not in html


def test_render_mondo_mapping_links_to_local_disorder_page(tmp_path: Path) -> None:
    """MONDO mappings outside differential sections should resolve to local pages."""
    acne_path = tmp_path / "Acne_Vulgaris.yaml"
    rosacea_path = tmp_path / "Rosacea.yaml"

    _write_disorder(
        acne_path,
        {
            "name": "Acne Vulgaris",
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "acne vulgaris"}},
            "mappings": {
                "mondo_mappings": [
                    {
                        "term": {"id": "MONDO:0000002", "label": "rosacea"},
                        "mapping_source": "MONDO",
                    }
                ]
            },
        },
    )
    _write_disorder(
        rosacea_path,
        {
            "name": "Rosacea",
            "disease_term": {"term": {"id": "MONDO:0000002", "label": "rosacea"}},
        },
    )

    output_path = tmp_path / "pages" / "disorders" / "Acne_Vulgaris.html"
    render_disorder(acne_path, output_path=output_path)

    html = output_path.read_text()
    assert 'href="Rosacea.html"' in html
    assert 'href="http://purl.obolibrary.org/obo/MONDO_0000002"' in html
    assert ">Dismech</a>" in html
    # Keep self MONDO badge external rather than self-linking.
    assert 'href="http://purl.obolibrary.org/obo/MONDO_0000001"' in html
    assert "Not Yet Curated" not in html


def test_resolve_local_disorder_href_with_prefix_and_exclusion() -> None:
    """Helper should apply relative prefixes and respect exclusions."""
    by_term = {"MONDO:0000002": "Rosacea.html"}
    assert (
        _resolve_local_disorder_href(
            "MONDO:0000002",
            by_term,
            local_prefix="../disorders/",
        )
        == "../disorders/Rosacea.html"
    )
    assert (
        _resolve_local_disorder_href(
            "MONDO:0000002",
            by_term,
            excluded_term_ids={"MONDO:0000002"},
        )
        is None
    )


def test_render_differential_highlights_missing_disorder_page(tmp_path: Path) -> None:
    """Differentials with MONDO terms but no local page should be visually flagged."""
    acne_path = tmp_path / "Acne_Vulgaris.yaml"
    _write_disorder(
        acne_path,
        {
            "name": "Acne Vulgaris",
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "acne vulgaris"}},
            "differential_diagnoses": [
                {
                    "name": "Uncurated Disease",
                    "disease_term": {
                        "term": {"id": "MONDO:0099999", "label": "uncurated disease"}
                    },
                }
            ],
        },
    )

    output_path = tmp_path / "pages" / "disorders" / "Acne_Vulgaris.html"
    render_disorder(acne_path, output_path=output_path)

    html = output_path.read_text()
    assert "missing-disease-name" in html
    assert "Not Yet Curated" in html
    assert "missing-ontology-link" in html
    assert 'href="http://purl.obolibrary.org/obo/MONDO_0099999"' in html


def test_render_mondo_mapping_highlights_missing_disorder_page(tmp_path: Path) -> None:
    """MONDO mapping labels should be flagged when no local disorder page exists."""
    acne_path = tmp_path / "Acne_Vulgaris.yaml"
    _write_disorder(
        acne_path,
        {
            "name": "Acne Vulgaris",
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "acne vulgaris"}},
            "mappings": {
                "mondo_mappings": [
                    {
                        "term": {"id": "MONDO:0099999", "label": "uncurated disease"},
                        "mapping_source": "MONDO",
                    }
                ]
            },
        },
    )

    output_path = tmp_path / "pages" / "disorders" / "Acne_Vulgaris.html"
    render_disorder(acne_path, output_path=output_path)

    html = output_path.read_text()
    assert "Not Yet Curated" in html
    assert "missing-disease-name" in html
    assert "missing-ontology-link" in html
    assert 'href="http://purl.obolibrary.org/obo/MONDO_0099999"' in html


def test_render_subtype_links_to_local_disorder_page(tmp_path: Path) -> None:
    """Subtype disease names should link to local pages when MONDO resolves locally."""
    acne_path = tmp_path / "Acne_Vulgaris.yaml"
    rosacea_path = tmp_path / "Rosacea.yaml"

    _write_disorder(
        acne_path,
        {
            "name": "Acne Vulgaris",
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "acne vulgaris"}},
            "has_subtypes": [
                {
                    "name": "Rosacea-like subtype",
                    "subtype_term": {
                        "term": {"id": "MONDO:0000002", "label": "rosacea"}
                    },
                }
            ],
        },
    )
    _write_disorder(
        rosacea_path,
        {
            "name": "Rosacea",
            "disease_term": {"term": {"id": "MONDO:0000002", "label": "rosacea"}},
        },
    )

    output_path = tmp_path / "pages" / "disorders" / "Acne_Vulgaris.html"
    render_disorder(acne_path, output_path=output_path)

    html = output_path.read_text()
    assert 'href="Rosacea.html">Rosacea-like subtype</a>' in html
    assert 'href="http://purl.obolibrary.org/obo/MONDO_0000002"' in html
    assert ">Dismech</a>" in html
    assert "Not Yet Curated" not in html


def test_render_subtype_highlights_missing_disorder_page(tmp_path: Path) -> None:
    """Subtype disease names should be flagged when MONDO has no local page."""
    acne_path = tmp_path / "Acne_Vulgaris.yaml"
    _write_disorder(
        acne_path,
        {
            "name": "Acne Vulgaris",
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "acne vulgaris"}},
            "has_subtypes": [
                {
                    "name": "Uncurated subtype",
                    "subtype_term": {
                        "term": {"id": "MONDO:0099999", "label": "uncurated disease"}
                    },
                }
            ],
        },
    )

    output_path = tmp_path / "pages" / "disorders" / "Acne_Vulgaris.html"
    render_disorder(acne_path, output_path=output_path)

    html = output_path.read_text()
    assert "missing-disease-name" in html
    assert "Not Yet Curated" in html
    assert "missing-ontology-link" in html
    assert 'href="http://purl.obolibrary.org/obo/MONDO_0099999"' in html
