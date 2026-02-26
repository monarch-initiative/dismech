"""Tests for internal DisMech links in rendered classification pages."""

from pathlib import Path

import yaml

from dismech.render import render_classification_pages


def _write_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False))


def test_render_classification_page_includes_internal_link_for_mondo_term(
    tmp_path: Path,
) -> None:
    """Classification enum nodes with MONDO meanings should link to local disorder pages."""
    input_dir = tmp_path / "kb" / "disorders"
    output_dir = tmp_path / "pages" / "classifications"

    _write_yaml(
        input_dir / "Epilepsy.yaml",
        {
            "name": "Epilepsy",
            "disease_term": {"term": {"id": "MONDO:0005027", "label": "epilepsy"}},
            "classifications": {
                "harrisons_chapter": [{"classification_value": "epilepsy"}]
            },
        },
    )

    render_classification_pages(input_dir=input_dir, output_dir=output_dir)
    html = (output_dir / "HarrisonsChapterEnum.html").read_text()

    # External MONDO link for the enum value.
    assert 'href="http://purl.obolibrary.org/obo/MONDO_0005027"' in html

    # Internal DisMech link generated via dismech_page_url filter.
    assert 'class="linkout dismech-link" href="../disorders/Epilepsy.html"' in html
