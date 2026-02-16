"""Tests for augmented matching causal graph rendering."""

from pathlib import Path

import yaml

from phenoagent.match_graph import (
    generate_matching_causal_mermaid,
    render_matching_causal_html,
    render_matching_causal_mermaid,
)


def _example_disorder() -> dict:
    return {
        "name": "Example Disease",
        "pathophysiology": [
            {
                "name": "Mitochondrial energy failure",
                "downstream": [
                    {"target": "Lactic acidosis"},
                    {"target": "Neonatal hypotonia"},
                    {"target": "Ventriculomegaly"},
                ],
            }
        ],
        "phenotypes": [
            {
                "name": "Lactic acidosis",
                "phenotype_term": {
                    "preferred_term": "Lactic acidosis",
                    "term": {"id": "HP:0003128", "label": "Lactic acidosis"},
                },
            },
            {
                "name": "Neonatal hypotonia",
                "phenotype_term": {
                    "preferred_term": "Neonatal hypotonia",
                    "term": {"id": "HP:0001319", "label": "Neonatal hypotonia"},
                },
            },
            {
                "name": "Ventriculomegaly",
                "phenotype_term": {
                    "preferred_term": "Ventriculomegaly",
                    "term": {"id": "HP:0002119", "label": "Ventriculomegaly"},
                },
            },
        ],
    }


def _example_matching_run() -> dict:
    return {
        "run_id": "run-1",
        "case_id": "case-1",
        "disease_slug": "Example_Disease",
        "generated_at": "2026-02-11T00:00:00Z",
        "pr_is_diagnosis": 0.0,
        "explanations": [
            {
                "explanation_id": "NO_EXPLANATION",
                "estimated_probability": 0.0,
                "description": "default",
            },
            {
                "explanation_id": "EXP_NOT_ASSAYED",
                "estimated_probability": 0.7,
                "description": "Likely not assayed in this case.",
            },
        ],
        "matches": [
            {
                "case_term_id": "HP:0003128",
                "case_present": True,
                "case_label": "Lactic acidosis",
                "model_term_id": "HP:0003128",
                "model_label": "Lactic acidosis",
                "exact": True,
                "case_is_broader": False,
                "case_is_narrower": False,
                "case_is_close": False,
                "similarity_percent": 100.0,
            },
            {
                "case_term_id": "HP:0001252",
                "case_present": True,
                "case_label": "Hypotonia",
                "model_term_id": "HP:0001319",
                "model_label": "Neonatal hypotonia",
                "exact": False,
                "case_is_broader": True,
                "case_is_narrower": False,
                "case_is_close": False,
                "similarity_percent": 75.0,
                "explanation_for_no_match": "EXP_NOT_ASSAYED",
            },
            {
                "model_term_id": "HP:0002119",
                "model_label": "Ventriculomegaly",
                "exact": False,
                "case_is_broader": False,
                "case_is_narrower": False,
                "case_is_close": False,
                "explanation_for_no_match": "NO_EXPLANATION",
            },
        ],
    }


def test_augmented_mermaid_contains_model_case_and_explanation_layers():
    mermaid = generate_matching_causal_mermaid(_example_disorder(), _example_matching_run())

    assert mermaid.startswith("graph LR")
    assert "subgraph MODEL_PHENOTYPES[Disease Model Phenotypes]" in mermaid
    assert "subgraph CASE_PHENOTYPES[Case Phenotypes]" in mermaid
    assert "subgraph EXPLANATIONS[Explanations]" in mermaid

    assert "MODEL: Lactic acidosis<br/>[HP:0003128]" in mermaid
    assert "MODEL: Neonatal hypotonia<br/>[HP:0001319]" in mermaid
    assert "MODEL: Ventriculomegaly<br/>[HP:0002119]" in mermaid
    assert "CASE + Lactic acidosis<br/>[HP:0003128]" in mermaid
    assert "CASE + Hypotonia<br/>[HP:0001252]" in mermaid
    assert "EXP: EXP_NOT_ASSAYED<br/>Pr=0.7<br/>Likely not assayed in this case." in mermaid

    assert "class model_Lactic_acidosis model_exact_present" in mermaid
    assert "class model_Neonatal_hypotonia model_related" in mermaid
    assert "class model_Ventriculomegaly model_unmatched" in mermaid
    assert "class exp_NO_EXPLANATION explanation_default" in mermaid

    assert "core_Mitochondrial_energy_failure --> model_Lactic_acidosis" in mermaid
    assert "model_Lactic_acidosis --> case_HP_0003128_1" in mermaid
    assert "model_Neonatal_hypotonia -.-> case_HP_0001252_2" in mermaid
    assert "model_Neonatal_hypotonia -.-> exp_EXP_NOT_ASSAYED" in mermaid
    assert "exp_EXP_NOT_ASSAYED -.-> case_HP_0001252_2" in mermaid


def test_render_matching_causal_mermaid_resolves_disorder_reference(tmp_path: Path):
    kb_dir = tmp_path / "kb" / "disorders"
    kb_dir.mkdir(parents=True)
    disorder_path = kb_dir / "Example_Disease.yaml"
    disorder_path.write_text(yaml.safe_dump(_example_disorder(), sort_keys=False))

    matching_path = tmp_path / "matching.yaml"
    matching_path.write_text(yaml.safe_dump(_example_matching_run(), sort_keys=False))

    mermaid = render_matching_causal_mermaid("Example_Disease", matching_path, kb_dir=kb_dir)
    assert "MODEL: Lactic acidosis<br/>[HP:0003128]" in mermaid
    assert "exp_EXP_NOT_ASSAYED" in mermaid


def test_render_matching_causal_html_contains_metadata_and_mermaid():
    disorder = _example_disorder()
    matching_run = _example_matching_run()
    mermaid = generate_matching_causal_mermaid(disorder, matching_run)

    html = render_matching_causal_html(
        disorder,
        matching_run,
        mermaid,
        disorder_source="kb/disorders/Example_Disease.yaml",
        matching_source="output/matching/example.yaml",
    )

    assert "<!doctype html>" in html.lower()
    assert "Match-Aware Causal Graph" in html
    assert "Run Metadata" in html
    assert "Match Summary" in html
    assert "pr_is_diagnosis" in html
    assert "case-1" in html
    assert "kb/disorders/Example_Disease.yaml" in html
    assert "output/matching/example.yaml" in html
    assert "id=\"match-graph\"" in html
    assert "const graphDefinition =" in html
    assert "Raw Mermaid (.mmd)" in html
