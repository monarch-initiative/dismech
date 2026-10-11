"""Model cards render the same structured content on disorder and module pages.

Issue #13123: a module page showed a computational model as a name, a
description, a bare list of target names and its notes, while the disorder page
rendered findings, variables, and per-link readouts. Both pages now render the
model sections from one set of shared includes, so these tests render the same
model through both and assert on the structured content, not on markup detail.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest
import yaml

import dismech.render as render_mod
from dismech.render import render_disorder, render_module

NODE = "Microtubule-Based Neuronal Motility Failure"


def _link(target: str) -> dict:
    return {
        "target": target,
        "relationship": "PARTIALLY_RECAPITULATES",
        "fidelity": "LOW",
        "model_scale": "CELLULAR",
        "limitations": "One-dimensional and cell-autonomous.",
        "divergences": [
            {
                "divergence_type": "BOUNDARY_OMISSION",
                "materiality": "INVALIDATING",
                "description": "The radial-glial scaffold is outside the model.",
            }
        ],
        "readouts": [
            {
                "name": "Mean arrival delay from birth to settling",
                "target": target,
                "direction": "INCREASED",
                "interpretation": "Rises monotonically with the perturbation.",
            }
        ],
    }


def _entry(**extra: object) -> dict:
    return {
        "pathophysiology": [{"name": NODE}],
        "computational_models": [
            {
                "name": "Radial migration ABM",
                "model_id": "example_abm",
                "model_type": "AGENT_BASED",
                "description": "A one-dimensional agent-based model.",
                "variables": [
                    {
                        "name": "cortical_plate_fraction",
                        "unit": "dimensionless",
                        "mappings_list": [
                            {
                                "preferred_term": "Abnormality of neuronal migration",
                                "term": {
                                    "id": "HP:0002269",
                                    "label": "Abnormality of neuronal migration",
                                },
                                "threshold": 0.95,
                                "threshold_direction": "below",
                            }
                        ],
                    }
                ],
                "findings": [{"statement": "Arrest, not slowing, produces ectopia."}],
                "modeled_mechanisms": [_link(NODE)],
                "notes": "x" * 500,
            }
        ],
        "animal_models": [
            {
                "name": "Pafah1b1 allelic-series mouse",
                "species": "Mouse",
                "modeled_mechanisms": [_link(NODE)],
            }
        ],
        **extra,
    }


def _strip_yaml_preview(html: str) -> str:
    return re.sub(r'<pre class="yaml-preview">.*?</pre>', "", html, flags=re.DOTALL)


def _render_module(tmp_path: Path) -> str:
    path = tmp_path / "example_module.yaml"
    path.write_text(
        yaml.safe_dump(
            {"name": "Example Module", "category": "Module", **_entry()},
            sort_keys=False,
        )
    )
    disorders_dir = tmp_path / "kb" / "disorders"
    disorders_dir.mkdir(parents=True)
    out = tmp_path / "pages" / "modules" / "example_module.html"
    render_module(path, output_path=out, disorders_dir=disorders_dir)
    return _strip_yaml_preview(out.read_text())


def _render_disorder(tmp_path: Path) -> str:
    path = tmp_path / "Example_Disease.yaml"
    path.write_text(
        yaml.safe_dump({"name": "Example Disease", **_entry()}, sort_keys=False)
    )
    out = tmp_path / "pages" / "disorders" / "Example_Disease.html"
    render_disorder(path, output_path=out)
    return _strip_yaml_preview(out.read_text())


@pytest.fixture(params=["module", "disorder"])
def html(request: pytest.FixtureRequest, tmp_path: Path) -> str:
    if request.param == "module":
        return _render_module(tmp_path)
    return _render_disorder(tmp_path)


def test_model_card_renders_structured_content(html: str) -> None:
    assert "Arrest, not slowing, produces ectopia." in html  # findings
    assert "cortical_plate_fraction" in html  # variables table
    assert "Abnormality of neuronal migration" in html  # variable-to-phenotype mapping
    assert "Mean arrival delay from birth to settling" in html  # link readout
    assert "partially recapitulates" in html
    assert "fidelity: low" in html
    assert "observes: cellular" in html
    assert "boundary omission" in html
    assert "model-materiality-INVALIDATING" in html
    assert "The radial-glial scaffold is outside the model." in html


def test_both_model_sections_render(html: str) -> None:
    assert "Pafah1b1 allelic-series mouse" in html
    assert "Radial migration ABM" in html


def test_long_notes_collapse(html: str) -> None:
    assert 'class="model-notes-details"' in html


def test_pathograph_links_resolve_to_node_anchors(html: str) -> None:
    hrefs = set(re.findall(r'href="#([^"]*pathophysiology[^"]*)"', html))
    assert hrefs, "a model link should point at its pathophysiology node"
    for anchor in hrefs:
        assert f'id="{anchor}"' in html, anchor


def test_module_links_use_module_node_anchors(tmp_path: Path) -> None:
    html = _render_module(tmp_path)
    assert 'href="#module-pathophysiology-' in html


def test_authored_model_thresholds_are_absolute(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """dismech-perturb reads a `below` threshold as a ratio of baseline; an
    authored model (spec.yaml) compares absolutely, so no ratio suffix."""
    models_root = tmp_path / "models"
    monkeypatch.setattr(render_mod, "MODELS_ROOT", models_root)

    html = _render_disorder(tmp_path)
    assert "&times; baseline" in html  # no models/ folder: perturb convention

    (models_root / "example_abm").mkdir(parents=True)
    (models_root / "example_abm" / "spec.yaml").write_text("model_id: example_abm\n")
    html = _render_module(tmp_path)
    assert "&times; baseline" not in html
    assert "models/example_abm" in html  # "Model files" link
