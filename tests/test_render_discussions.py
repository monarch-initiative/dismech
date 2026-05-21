"""Tests for rendering discussions and proposed experiments."""

from pathlib import Path

import yaml

from dismech.render import render_disorder


def test_render_discussion_proposed_experiment(tmp_path: Path) -> None:
    """Knowledge-gap discussions should render nested experiment details."""
    disorder_path = tmp_path / "Gap_Disorder.yaml"
    output_path = tmp_path / "pages" / "disorders" / "Gap_Disorder.html"

    disorder_path.write_text(
        yaml.safe_dump(
            {
                "name": "Gap Disorder",
                "pathophysiology": [
                    {
                        "name": "Missing Step",
                        "description": "A declared pathophysiology node.",
                    }
                ],
                "discussions": [
                    {
                        "discussion_id": "gap_test",
                        "prompt": "Does the model have a missing causal step?",
                        "kind": "KNOWLEDGE_GAP",
                        "status": "OPEN",
                        "attaches_to": ["pathophysiology#Missing Step"],
                        "rationale": "This determines which mechanism should be tested.",
                        "proposed_experiments": [
                            {
                                "experiment_id": "exp_gap_test",
                                "name": "Laser-bioprinted organ-on-chip assay",
                                "description": "Pattern cells in a vascular chip.",
                                "experiment_type": {
                                    "preferred_term": "organ-on-chip perturbation experiment"
                                },
                                "model_systems": [
                                    {
                                        "name": "Human organ-on-chip model",
                                        "experimental_model_type": "ORGAN_ON_CHIP",
                                        "namo_type": "namo:OrganOnChip",
                                    }
                                ],
                                "perturbations": [
                                    {
                                        "name": "Cell placement",
                                        "target": "pathophysiology#Missing Step",
                                    }
                                ],
                                "readouts": [
                                    {
                                        "name": "Barrier permeability",
                                        "target": "pathophysiology#Missing Step",
                                        "direction": "POSITIVE",
                                    }
                                ],
                                "controls": [{"name": "Mock-patterned control"}],
                                "decision_criterion": "Barrier leak should track the perturbation.",
                                "would_support": ["pathophysiology#Missing Step"],
                            }
                        ],
                    }
                ],
            },
            sort_keys=False,
        )
    )

    render_disorder(disorder_path, output_path=output_path)
    html = output_path.read_text()

    assert "Discussions and Knowledge Gaps" in html
    assert "KNOWLEDGE GAP" in html
    assert "Laser-bioprinted organ-on-chip assay" in html
    assert "Model systems" in html
    assert "Perturbations" in html
    assert "Readouts" in html
    assert "Barrier leak should track the perturbation." in html
    assert 'href="#discussions"' in html
    assert 'id="pathophysiology-missing-step"' in html
    assert html.count('href="#pathophysiology-missing-step"') >= 4
