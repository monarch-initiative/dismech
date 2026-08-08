"""Tests for rendering animal model to pathophysiology links.

Animal models reach the pathograph through the same ModelMechanismLink object
as experimental (NAM) and computational models, but AnimalModel's `name` is
optional, so the label falls back to genotype/species.
"""

from pathlib import Path

import yaml

from dismech.graph import animal_model_label
from dismech.render import render_disorder


def _write(tmp_path: Path, animal_models: list[dict]) -> Path:
    disorder_path = tmp_path / "Example_Disease.yaml"
    disorder_path.write_text(
        yaml.safe_dump(
            {
                "name": "Example Disease",
                "pathophysiology": [
                    {
                        "name": "Motor Neuron Degeneration",
                        "downstream": [{"target": "Muscle weakness"}],
                    }
                ],
                "phenotypes": [{"name": "Muscle weakness"}],
                "animal_models": animal_models,
            },
            sort_keys=False,
        )
    )
    return disorder_path


def test_render_animal_model_links_are_bidirectional(tmp_path: Path) -> None:
    """Animal model cards and pathophysiology cards should link to each other."""
    disorder_path = _write(
        tmp_path,
        [
            {
                "name": "SOD1-G93A transgenic mouse",
                "species": "Mus musculus",
                "genotype": "SOD1-G93A",
                "modeled_mechanisms": [
                    {
                        "target": "Motor Neuron Degeneration",
                        "relationship": "RECAPITULATES",
                        "fidelity": "MODERATE",
                        "description": "Progressive spinal motor neuron loss.",
                        "limitations": "Supraphysiological transgene copy number.",
                        "readouts": [
                            {
                                "name": "Spinal motor neuron count",
                                "target": "Motor Neuron Degeneration",
                                "direction": "DECREASED",
                                "interpretation": "Ventral horn loss vs littermates.",
                            }
                        ],
                    }
                ],
            }
        ],
    )

    output_path = tmp_path / "pages" / "disorders" / "Example_Disease.html"
    render_disorder(disorder_path, output_path=output_path)

    html = output_path.read_text()
    assert 'id="animal-model-sod1-g93a-transgenic-mouse"' in html
    assert 'href="#pathophysiology-motor-neuron-degeneration"' in html
    assert 'href="#animal-model-sod1-g93a-transgenic-mouse"' in html
    assert "Animal Models" in html
    assert "Pathograph links" in html
    # The measured aspect, its caveat, and the outcome measure all surface.
    assert "recapitulates" in html
    assert "fidelity: moderate" in html
    assert "Supraphysiological transgene copy number." in html
    assert "Spinal motor neuron count" in html
    assert "Direction: DECREASED" in html


def test_render_animal_model_without_name_uses_genotype_species_label(
    tmp_path: Path,
) -> None:
    """A pre-existing entry with no `name` still reaches the pathograph."""
    disorder_path = _write(
        tmp_path,
        [
            {
                "species": "Mus musculus",
                "genotype": "Msx1-null",
                "modeled_mechanisms": [
                    {"target": "Motor Neuron Degeneration", "relationship": "PERTURBS"}
                ],
            }
        ],
    )

    output_path = tmp_path / "pages" / "disorders" / "Example_Disease.html"
    render_disorder(disorder_path, output_path=output_path)

    html = output_path.read_text()
    assert 'id="animal-model-msx1-null-mus-musculus"' in html
    assert "Msx1-null Mus musculus" in html
    assert 'href="#pathophysiology-motor-neuron-degeneration"' in html


def test_animal_model_label_prefers_name_and_degrades_gracefully() -> None:
    assert animal_model_label({"name": "SOD1-G93A mouse"}) == "SOD1-G93A mouse"
    assert (
        animal_model_label({"genotype": "Msx1-null", "species": "Mus musculus"})
        == "Msx1-null Mus musculus"
    )
    assert animal_model_label({"species": "Danio rerio"}) == "Danio rerio"
    assert animal_model_label({"description": "unnamed"}) is None
