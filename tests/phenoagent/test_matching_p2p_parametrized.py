"""Parametrized unit tests for single phenotype-to-phenotype matching."""

from pathlib import Path

import pytest
import yaml

from phenoagent.matching import build_matching_run_from_phenopacket

MODEL_FREQUENCIES = (
    "OBLIGATE",
    "VERY_FREQUENT",
    "FREQUENT",
    "OCCASIONAL",
    "VERY_RARE",
)

RELATION_CASES = (
    pytest.param(
        "exact",
        "HP:0001250",
        "Seizure",
        "HP:0001250",
        "Seizure",
        {"exact": True, "case_is_broader": False, "case_is_narrower": False},
        id="exact",
    ),
    pytest.param(
        "broader",
        "HP:0001250",
        "Seizure",
        "HP:0002123",
        "Focal seizure",
        {"exact": False, "case_is_broader": True, "case_is_narrower": False},
        id="broader",
    ),
    pytest.param(
        "narrower",
        "HP:0002123",
        "Focal seizure",
        "HP:0001250",
        "Seizure",
        {"exact": False, "case_is_broader": False, "case_is_narrower": True},
        id="narrower",
    ),
)


def _write_single_model_file(
    target_path: Path,
    model_term_id: str,
    model_label: str,
    model_frequency: str,
) -> None:
    """Write a one-phenotype disease model YAML file."""
    disease = {
        "name": "Test Disease",
        "phenotypes": [
            {
                "name": model_label,
                "description": "Model-side phenotype description.",
                "frequency": model_frequency,
                "phenotype_term": {
                    "preferred_term": model_label,
                    "term": {"id": model_term_id, "label": model_label},
                },
            }
        ],
    }
    with open(target_path, "w") as stream:
        yaml.safe_dump(disease, stream, sort_keys=False)


@pytest.mark.parametrize("model_frequency", MODEL_FREQUENCIES, ids=lambda frequency: f"freq_{frequency.lower()}")
@pytest.mark.parametrize(
    ("relation", "case_term_id", "case_label", "model_term_id", "model_label", "expected"),
    RELATION_CASES,
)
@pytest.mark.parametrize("case_present", (True, False), ids=("case_present", "case_absent"))
def test_single_p2p_relation_matrix(
    tmp_path: Path,
    model_frequency: str,
    relation: str,
    case_term_id: str,
    case_label: str,
    model_term_id: str,
    model_label: str,
    expected: dict[str, bool],
    case_present: bool,
):
    """Test case presence x relation x model frequency combinations."""
    disease_slug = "Test_Disease"
    disease_path = tmp_path / f"{disease_slug}.yaml"
    _write_single_model_file(disease_path, model_term_id, model_label, model_frequency)

    phenopacket = {
        "id": f"case-{relation}-{model_frequency}-{str(case_present).lower()}",
        "phenotypicFeatures": [
            {
                "type": {"id": case_term_id, "label": case_label},
                "excluded": not case_present,
                "description": "Case-side phenotype description.",
            }
        ],
    }

    run = build_matching_run_from_phenopacket(
        phenopacket,
        disease_slug=disease_slug,
        kb_dir=tmp_path,
        run_id="run-p2p-matrix",
    )
    assert len(run["matches"]) == 1
    row = run["matches"][0]

    assert row["case_present"] is case_present
    assert row["case_description"] == "Case-side phenotype description."
    assert row["model_term_id"] == model_term_id
    assert row["model_label"] == model_label
    assert row["model_description"] == "Model-side phenotype description."
    assert row["model_frequency"] == model_frequency

    assert row["exact"] is expected["exact"]
    assert row["case_is_broader"] is expected["case_is_broader"]
    assert row["case_is_narrower"] is expected["case_is_narrower"]
    assert row["case_is_close"] is False

    if expected["exact"]:
        assert run["pr_is_diagnosis"] == 1.0
        assert row["similarity_percent"] == 100.0
        assert "explanation_for_no_match" not in row
    else:
        assert run["pr_is_diagnosis"] == 0.0
        assert row["similarity_percent"] == 75.0
        assert row["explanation_for_no_match"] == "NO_EXPLANATION"


def test_exact_id_match_ignores_label_mismatch(tmp_path: Path):
    """Exact term ID match should not depend on lexical label similarity."""
    disease_slug = "Test_Disease"
    disease_path = tmp_path / f"{disease_slug}.yaml"
    _write_single_model_file(
        disease_path,
        model_term_id="HP:0001250",
        model_label="Seizure",
        model_frequency="FREQUENT",
    )

    phenopacket = {
        "id": "label-mismatch-case",
        "phenotypicFeatures": [
            {
                "type": {"id": "HP:0001250", "label": "Completely unrelated text"},
                "description": "Case label is intentionally mismatched.",
            }
        ],
    }
    run = build_matching_run_from_phenopacket(
        phenopacket,
        disease_slug=disease_slug,
        kb_dir=tmp_path,
        run_id="run-label-mismatch",
    )

    assert run["pr_is_diagnosis"] == 1.0
    row = run["matches"][0]
    assert row["model_term_id"] == "HP:0001250"
    assert row["exact"] is True
    assert row["similarity_percent"] == 100.0
