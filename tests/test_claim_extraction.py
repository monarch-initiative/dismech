from __future__ import annotations

import csv
import io
from pathlib import Path

import yaml
from typer.testing import CliRunner

from dismech.claims import extract_claim_rows
from dismech.claims import extract_claim_rows_from_file
from dismech.cli import app


def _write_yaml(path: Path, payload: dict) -> None:
    path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")


def _base_evidence(reference: str) -> dict[str, str]:
    return {
        "reference": reference,
        "supports": "SUPPORT",
        "evidence_source": "HUMAN_CLINICAL",
        "snippet": f"Snippet for {reference}",
        "explanation": f"Explanation for {reference}",
    }


def _claim_fixture() -> dict:
    return {
        "name": "Test Disease",
        "disease_term": {"term": {"id": "MONDO:1234567", "label": "test disease"}},
        "phenotypes": [
            {
                "name": "Dyspnea",
                "phenotype_term": {"term": {"id": "HP:0002094", "label": "dyspnea"}},
                "frequency": "FREQUENT",
                "evidence": [_base_evidence("PMID:111")],
            }
        ],
        "pathophysiology": [
            {
                "name": "Airway Inflammation",
                "description": "Inflammatory pathway dysregulation.",
                "evidence": [_base_evidence("PMID:222")],
            }
        ],
        "treatments": [
            {
                "name": "Inhaled Corticosteroids",
                "treatment_term": {
                    "preferred_term": "inhaled corticosteroid therapy",
                    "term": {"id": "NCIT:C15986", "label": "Pharmacotherapy"},
                },
                "evidence": [_base_evidence("PMID:333")],
            }
        ],
        "histopathology": [
            {
                "name": "Goblet Cell Hyperplasia",
                "finding_term": {
                    "term": {"id": "NCIT:C35867", "label": "Morphologic Finding"}
                },
                "evidence": [_base_evidence("PMID:444")],
            }
        ],
    }


def test_extracts_phenotype_claim_and_frequency_subclaim() -> None:
    rows = extract_claim_rows(_claim_fixture())

    phenotype_rows = [
        row
        for row in rows
        if row.claim_type == "phenotype" and row.evidence_reference == "PMID:111"
    ]

    assert len(phenotype_rows) == 2

    base_row = next(row for row in phenotype_rows if not row.is_subclaim)
    assert base_row.object_id == "HP:0002094"
    assert base_row.object_label == "dyspnea"
    assert base_row.claim_text == "Test Disease has phenotype Dyspnea"

    qualifier_row = next(row for row in phenotype_rows if row.is_subclaim)
    assert qualifier_row.qualifier_name == "frequency"
    assert qualifier_row.qualifier_value == "FREQUENT"
    assert qualifier_row.qualifier_value_id == "HP:0040282"
    assert qualifier_row.qualifier_evidence_missing is True
    assert qualifier_row.claim_text.endswith("with frequency frequent")


def test_default_phenotype_context_evidence_covers_frequency_subclaim() -> None:
    disease = _claim_fixture()
    disease["phenotypes"][0]["phenotype_contexts"] = [
        {
            "frequency": "FREQUENT",
            "evidence": [_base_evidence("PMID:112")],
        }
    ]

    rows = extract_claim_rows(disease)
    frequency_rows = [
        row
        for row in rows
        if row.claim_type == "phenotype" and row.qualifier_name == "frequency"
    ]

    assert len(frequency_rows) == 1
    row = frequency_rows[0]
    assert row.evidence_reference == "PMID:112"
    assert row.qualifier_evidence_missing is False
    assert row.source_path.endswith("phenotype_contexts[0]")


def test_phenotype_context_emits_contextual_subclaims_with_context_evidence() -> None:
    disease = {
        "name": "Familial Hypercholesterolemia",
        "disease_term": {
            "term": {
                "id": "MONDO:0007750",
                "label": "familial hypercholesterolemia",
            }
        },
        "phenotypes": [
            {
                "name": "Hypercholesterolemia",
                "phenotype_term": {
                    "term": {
                        "id": "HP:0003124",
                        "label": "Hypercholesterolemia",
                    }
                },
                "phenotype_contexts": [
                    {
                        "genetic_context": {
                            "zygosity": "HOMOZYGOUS",
                            "description": "Homozygous FH",
                        },
                        "severity": "Severe",
                        "evidence": [_base_evidence("PMID:113")],
                    }
                ],
                "evidence": [_base_evidence("PMID:111")],
            }
        ],
    }

    rows = extract_claim_rows(disease)

    severity_row = next(
        row
        for row in rows
        if row.qualifier_name == "severity" and row.evidence_reference == "PMID:113"
    )
    assert severity_row.qualifier_evidence_missing is False
    assert "genetic_context" in severity_row.qualifiers_json
    assert severity_row.claim_text.startswith(
        "Familial Hypercholesterolemia has phenotype Hypercholesterolemia with severity severe"
    )

    genetic_context_row = next(
        row
        for row in rows
        if row.qualifier_name == "genetic_context"
        and row.evidence_reference == "PMID:113"
    )
    assert genetic_context_row.qualifier_evidence_missing is False
    assert genetic_context_row.source_path.endswith("phenotype_contexts[0]")
    assert genetic_context_row.qualifier_value == "Homozygous FH"


def test_extracts_pathophysiology_claim() -> None:
    rows = extract_claim_rows(_claim_fixture())

    row = next(
        row
        for row in rows
        if row.claim_type == "pathophysiology"
        and row.evidence_reference == "PMID:222"
        and not row.is_subclaim
    )

    assert row.object_label == "Airway Inflammation"
    assert row.object_id == ""
    assert row.claim_text == "Test Disease has pathophysiology Airway Inflammation"


def test_pathophysiology_structural_fields_do_not_emit_qualifier_rows() -> None:
    disease = _claim_fixture()
    disease["pathophysiology"][0].update(
        {
            "conforms_to": "fibrotic_response#Mesenchymal Cell Activation",
            "consequence": "Leads to downstream airway remodeling.",
            "role": "Primary",
        }
    )

    rows = [
        row
        for row in extract_claim_rows(disease)
        if row.claim_type == "pathophysiology" and row.evidence_reference == "PMID:222"
    ]

    assert len(rows) == 1
    assert not rows[0].is_subclaim
    assert rows[0].qualifier_name == ""


def test_extracts_treatment_claim() -> None:
    rows = extract_claim_rows(_claim_fixture())

    row = next(
        row
        for row in rows
        if row.claim_type == "treatment"
        and row.evidence_reference == "PMID:333"
        and not row.is_subclaim
    )

    assert row.object_label == "inhaled corticosteroid therapy"
    assert row.object_id == "NCIT:C15986"
    assert row.claim_text == "Test Disease has treatment Inhaled Corticosteroids"


def test_extracts_histopathology_claim() -> None:
    rows = extract_claim_rows(_claim_fixture())

    row = next(
        row
        for row in rows
        if row.claim_type == "histopathology"
        and row.evidence_reference == "PMID:444"
        and not row.is_subclaim
    )

    assert row.object_label == "Morphologic Finding"
    assert row.object_id == "NCIT:C35867"
    assert (
        row.claim_text
        == "Test Disease has histopathology finding Goblet Cell Hyperplasia"
    )


def test_extract_claims_cli_outputs_csv(tmp_path: Path) -> None:
    disorder_path = tmp_path / "Claim_Test.yaml"
    _write_yaml(disorder_path, _claim_fixture())

    runner = CliRunner()
    result = runner.invoke(app, ["extract-claims", str(disorder_path)])

    assert result.exit_code == 0

    reader = csv.DictReader(io.StringIO(result.stdout))
    rows = list(reader)
    assert rows
    assert rows[0]["disease_name"] == "Test Disease"


def test_extract_claim_rows_from_file(tmp_path: Path) -> None:
    disorder_path = tmp_path / "Claim_Test.yaml"
    _write_yaml(disorder_path, _claim_fixture())

    rows = extract_claim_rows_from_file(disorder_path)

    assert any(row.evidence_reference == "PMID:111" for row in rows)
    assert any(row.evidence_reference == "PMID:444" for row in rows)


def test_extract_claims_cli_all_mode_writes_csv(tmp_path: Path) -> None:
    kb_dir = tmp_path / "kb"
    kb_dir.mkdir()
    _write_yaml(kb_dir / "Claim_Test_One.yaml", _claim_fixture())
    second = _claim_fixture()
    second["name"] = "Second Disease"
    second["disease_term"]["term"]["id"] = "MONDO:7654321"
    _write_yaml(kb_dir / "Claim_Test_Two.yaml", second)

    out_path = tmp_path / "all_claims.csv"
    runner = CliRunner()
    result = runner.invoke(
        app,
        ["extract-claims", "--all", "--kb-dir", str(kb_dir), "--out", str(out_path)],
    )

    assert result.exit_code == 0
    assert out_path.exists()

    with out_path.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))

    assert rows
    assert {row["disease_name"] for row in rows} == {"Test Disease", "Second Disease"}
