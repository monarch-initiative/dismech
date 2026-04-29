"""Tests for rendering experimental model to pathophysiology links."""

from pathlib import Path

import yaml

from dismech.render import render_disorder


def test_render_experimental_model_links_are_bidirectional(tmp_path: Path) -> None:
    """Model cards and pathophysiology cards should link to each other."""
    disorder_path = tmp_path / "Example_Disease.yaml"
    disorder_path.write_text(
        yaml.safe_dump(
            {
                "name": "Example Disease",
                "pathophysiology": [
                    {
                        "name": "CFTR Dysfunction",
                        "downstream": [{"target": "Bronchiectasis"}],
                    }
                ],
                "phenotypes": [{"name": "Bronchiectasis"}],
                "experimental_models": [
                    {
                        "name": "Patient-derived airway organoid",
                        "experimental_model_type": "ORGANOID",
                        "namo_type": "namo:Organoid",
                        "modeled_mechanisms": [
                            {
                                "target": "CFTR Dysfunction",
                                "description": "Assays epithelial CFTR rescue in patient-derived tissue.",
                            }
                        ],
                    }
                ],
            },
            sort_keys=False,
        )
    )

    output_path = tmp_path / "pages" / "disorders" / "Example_Disease.html"
    render_disorder(disorder_path, output_path=output_path)

    html = output_path.read_text()
    assert 'id="experimental-model-patient-derived-airway-organoid"' in html
    assert 'href="#pathophysiology-cftr-dysfunction"' in html
    assert 'href="#experimental-model-patient-derived-airway-organoid"' in html
    assert "Experimental Models" in html
    assert "Pathograph links" in html
    assert "Use the checkboxes to hide or show graph categories." in html
