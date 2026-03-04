"""Tests for matching CLI helpers and disease reference resolution."""

from pathlib import Path

import json
import yaml

from phenoagent.matching import resolve_disease_reference
from phenoagent.matching_cli import create_initial_matching_file


def _write_disease_file(path: Path, *, disease_name: str, disease_id: str) -> None:
    disease = {
        "name": disease_name,
        "disease_term": {
            "preferred_term": disease_name,
            "term": {"id": disease_id, "label": disease_name},
        },
        "phenotypes": [
            {
                "name": "Seizure",
                "description": "Model-side seizure description.",
                "frequency": "FREQUENT",
                "phenotype_term": {
                    "preferred_term": "Seizure",
                    "term": {"id": "HP:0001250", "label": "Seizure"},
                },
            }
        ],
    }
    with open(path, "w") as stream:
        yaml.safe_dump(disease, stream, sort_keys=False)


def _write_phenopacket(path: Path) -> None:
    phenopacket = {
        "id": "test_ppkt_001",
        "phenotypicFeatures": [
            {
                "type": {"id": "HP:0001250", "label": "Seizure"},
                "description": "Case-side seizure description.",
            }
        ],
    }
    path.write_text(json.dumps(phenopacket, indent=2))


def test_resolve_disease_reference_slug_id_name_and_path(tmp_path: Path):
    kb_dir = tmp_path / "kb" / "disorders"
    kb_dir.mkdir(parents=True)
    disease_path = kb_dir / "Test_Disease.yaml"
    _write_disease_file(disease_path, disease_name="Test Disease", disease_id="MONDO:1234567")

    slug, path = resolve_disease_reference("Test_Disease", kb_dir=kb_dir)
    assert slug == "Test_Disease"
    assert path == disease_path.resolve()

    slug, path = resolve_disease_reference("MONDO:1234567", kb_dir=kb_dir)
    assert slug == "Test_Disease"
    assert path == disease_path.resolve()

    slug, path = resolve_disease_reference("Test Disease", kb_dir=kb_dir)
    assert slug == "Test_Disease"
    assert path == disease_path.resolve()

    slug, path = resolve_disease_reference(disease_path, kb_dir=kb_dir)
    assert slug == "Test_Disease"
    assert path == disease_path.resolve()


def test_create_initial_matching_file_default_output(tmp_path: Path, monkeypatch):
    kb_dir = tmp_path / "kb" / "disorders"
    kb_dir.mkdir(parents=True)
    disease_path = kb_dir / "Test_Disease.yaml"
    _write_disease_file(disease_path, disease_name="Test Disease", disease_id="MONDO:1234567")

    phenopacket_path = tmp_path / "input_phenopacket.json"
    _write_phenopacket(phenopacket_path)

    monkeypatch.chdir(tmp_path)
    output_path = create_initial_matching_file(
        phenopacket_path=phenopacket_path,
        disease_reference="MONDO:1234567",
        kb_dir=kb_dir,
    )

    assert output_path.exists()
    assert output_path.resolve() == (tmp_path / "output" / "matching" / "test_ppkt_001__Test_Disease.yaml").resolve()

    with open(output_path) as stream:
        data = yaml.safe_load(stream)

    assert data["case_id"] == "test_ppkt_001"
    assert data["disease_slug"] == "Test_Disease"
    assert data["pr_is_diagnosis"] == 1.0
    assert data["explanations"] == [
        {
            "explanation_id": "NO_EXPLANATION",
            "estimated_probability": 0.0,
            "description": "No explanation assigned yet for this non-match.",
        }
    ]
    assert len(data["matches"]) == 1
    match = data["matches"][0]
    assert match["case_description"] == "Case-side seizure description."
    assert match["model_term_id"] == "HP:0001250"
    assert "explanation_for_no_match" not in match
