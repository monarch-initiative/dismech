"""Tests for MONDO + Dismech link rendering in comorbidity pages."""

from pathlib import Path

import yaml

from dismech.render import render_comorbidity


def _write_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False))


def test_render_comorbidity_signal_ids_show_dual_links_and_missing_badge(tmp_path: Path) -> None:
    """Comorbidity signal MONDO IDs should show MONDO links and local Dismech links when available."""
    disorders_dir = tmp_path / "kb" / "disorders"
    comorbidity_dir = tmp_path / "kb" / "comorbidities"

    _write_yaml(
        disorders_dir / "Local_Disease.yaml",
        {
            "name": "Local Disease",
            "disease_term": {
                "term": {"id": "MONDO:1234567", "label": "local disease"}
            },
        },
    )
    _write_yaml(
        disorders_dir / "Another_Disease.yaml",
        {
            "name": "Another Disease",
            "disease_term": {
                "term": {"id": "MONDO:1234000", "label": "another disease"}
            },
        },
    )

    comorbidity_path = comorbidity_dir / "com_Local_Disease__Another_Disease.yaml"
    _write_yaml(
        comorbidity_path,
        {
            "name": "Local Disease / Another Disease",
            "disease_a": {"slug": "Local_Disease"},
            "disease_b": {"slug": "Another_Disease"},
            "association_signals": [
                {
                    "source": "unit-test",
                    "signal_disorder_a_id": "MONDO:1234567",
                    "signal_disorder_b_id": "MONDO:8888888",
                }
            ],
        },
    )

    output_path = tmp_path / "pages" / "comorbidities" / "com_test.html"
    render_comorbidity(comorbidity_path, output_path=output_path)

    html = output_path.read_text()

    # MONDO external links always present.
    assert 'href="http://purl.obolibrary.org/obo/MONDO_1234567"' in html
    assert 'href="http://purl.obolibrary.org/obo/MONDO_8888888"' in html

    # Local Dismech link for known MONDO.
    assert 'class="dismech-inline-link" href="../disorders/Local_Disease.html"' in html

    # Missing local page should be clearly indicated.
    assert "Not Yet Curated" in html
    assert "missing-ontology-link" in html

    # Existing explicit local disease links are now visibly underlined/internal.
    assert 'class="internal-link" href="../disorders/Local_Disease.html"' in html
    assert 'class="internal-link" href="../disorders/Another_Disease.html"' in html


def test_render_comorbidity_components_only_link_when_local_page_exists(tmp_path: Path) -> None:
    """Composite component slugs should only link when a matching local disorder page exists."""
    disorders_dir = tmp_path / "kb" / "disorders"
    comorbidity_dir = tmp_path / "kb" / "comorbidities"

    _write_yaml(
        disorders_dir / "Present_Disease.yaml",
        {
            "name": "Present Disease",
            "disease_term": {
                "term": {"id": "MONDO:7000001", "label": "present disease"}
            },
        },
    )
    _write_yaml(
        disorders_dir / "Another_Disease.yaml",
        {
            "name": "Another Disease",
            "disease_term": {
                "term": {"id": "MONDO:7000002", "label": "another disease"}
            },
        },
    )

    comorbidity_path = comorbidity_dir / "com_components.yaml"
    _write_yaml(
        comorbidity_path,
        {
            "name": "Composite components test",
            "disease_a": {
                "slug": "Composite_A",
                "components": [
                    {"slug": "Present_Disease"},
                    {"slug": "Missing_Disease"},
                ],
            },
            "disease_b": {"slug": "Another_Disease"},
        },
    )

    output_path = tmp_path / "pages" / "comorbidities" / "com_components.html"
    render_comorbidity(comorbidity_path, output_path=output_path)
    html = output_path.read_text()

    assert 'href="../disorders/Present_Disease.html"' in html
    assert 'href="../disorders/Another_Disease.html"' in html

    # Missing component should render as plain text, not a broken link.
    assert 'href="../disorders/Missing_Disease.html"' not in html
