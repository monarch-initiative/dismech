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


def test_model_edge_styling_matches_cx2_for_every_predicate(tmp_path: Path) -> None:
    """Every model predicate must be styled, and non-causal ones must not
    end in a causal arrowhead.

    The HTML pathograph and cx2 style the same edge, so an unstyled predicate
    in one renderer means the two disagree about what a link claims. Pins the
    markers a falsified model, a pure readout, and a rescue depend on.
    """
    from dismech.export.cx2_export import EDGE_STYLE_BY_PREDICATE
    from dismech.graph import MODEL_RELATIONSHIP_PREDICATES

    disorder_path = _write(
        tmp_path,
        [
            {
                "name": f"Model {relationship}",
                "species": "Mus musculus",
                "modeled_mechanisms": [
                    {
                        "target": "Motor Neuron Degeneration",
                        "relationship": relationship,
                        **(
                            {
                                "limitations": "No motor phenotype.",
                                "evidence": [
                                    {
                                        "reference": "PMID:1",
                                        "supports": "REFUTE",
                                        "snippet": "s",
                                        "explanation": "e",
                                    }
                                ],
                            }
                            if relationship == "FAILS_TO_RECAPITULATE"
                            else {}
                        ),
                    }
                ],
            }
            for relationship in MODEL_RELATIONSHIP_PREDICATES
        ],
    )

    output_path = tmp_path / "pages" / "disorders" / "Example_Disease.html"
    render_disorder(disorder_path, output_path=output_path)
    html = output_path.read_text()

    # Every predicate cx2 styles is also styled in the HTML table.
    for predicate in MODEL_RELATIONSHIP_PREDICATES.values():
        assert predicate in EDGE_STYLE_BY_PREDICATE, f"cx2 missing {predicate}"
        assert f"{predicate}:" in html or f'"{predicate}"' in html, (
            f"HTML MODEL_EDGE_STYLES missing {predicate}"
        )

    # The non-causal heads must be *defined* in defs, not merely named. A bare
    # substring check would also match the marker id inside MODEL_EDGE_STYLES,
    # so it would pass for a style table pointing at a marker that does not
    # exist -- which is the failure this is meant to catch.
    for marker in (
        "pg-arrow-failed-model",
        "pg-arrow-model-tee",
        "pg-arrow-model-readout",
    ):
        assert f'.attr("id", "{marker}")' in html, f"marker {marker} not in defs"

    # cx2 agrees that these three are non-causal.
    assert EDGE_STYLE_BY_PREDICATE["fails_to_model"].target_arrow_shape == "tee"
    assert EDGE_STYLE_BY_PREDICATE["rescues"].target_arrow_shape == "tee"
    assert EDGE_STYLE_BY_PREDICATE["measures"].target_arrow_shape == "circle"


def test_animal_model_label_prefers_name_and_degrades_gracefully() -> None:
    assert animal_model_label({"name": "SOD1-G93A mouse"}) == "SOD1-G93A mouse"
    assert (
        animal_model_label({"genotype": "Msx1-null", "species": "Mus musculus"})
        == "Msx1-null Mus musculus"
    )
    assert animal_model_label({"species": "Danio rerio"}) == "Danio rerio"
    assert animal_model_label({"description": "unnamed"}) is None
    # A genotype YAML parses as a scalar must degrade, not raise.
    assert animal_model_label({"genotype": 2, "species": "Mus musculus"}) == (
        "2 Mus musculus"
    )
