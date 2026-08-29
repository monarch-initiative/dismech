"""Focused tests for hypothesis-reconciliation semantic validation."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import yaml

from dismech.hypothesis_reconciliation import iter_reconciliation_problems


def _write_yaml(path: Path, data: dict) -> None:
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")


def _fixture(tmp_path: Path) -> tuple[Path, dict]:
    root = tmp_path / "kb" / "hypotheses" / "Test_Disease" / "canonical_model"
    assessments = root / "assessments"
    assessments.mkdir(parents=True)

    reports = {
        "alpha": "Alpha independently supports the mechanism.\n",
        "beta": "Beta supports only the narrower mechanism.\n",
    }
    for provider, text in reports.items():
        (root / f"{provider}.md").write_text(text, encoding="utf-8")
        _write_yaml(
            assessments / f"{provider}-assessment-by-reviewer.yaml",
            {
                "schema_version": "1.0.0",
                "provider": provider,
                "assessor": "reviewer",
                "source_report": f"../{provider}.md",
                "hypothesis_id": "canonical_model",
                "assessed_at": "2026-08-29T00:00:00Z",
                "overall_verdict": "PARTIALLY_SUPPORTED",
                "summary": f"Assessment of {provider}.",
                "claims": [
                    {
                        "claim_id": f"{provider}_claim",
                        "statement": f"{provider} addresses the mechanism.",
                        "disposition": "RETAINED",
                        "report_quote": text.strip(),
                        "rationale": "The raw report states this directly.",
                    }
                ],
            },
        )

    data = {
        "schema_version": "1.0.0",
        "assessor": "reconciler",
        "hypothesis_id": "canonical_model",
        "reconciled_at": "2026-08-29T00:00:00Z",
        "providers": [
            {
                "provider": provider,
                "source_assessment": (
                    f"assessments/{provider}-assessment-by-reviewer.yaml"
                ),
                "source_report": f"{provider}.md",
            }
            for provider in reports
        ],
        "overall_verdict": "PARTIALLY_SUPPORTED",
        "summary": "The two separately assessed reports overlap in scope.",
        "reconciled_claims": [
            {
                "claim_id": "shared_mechanism",
                "claim_kind": "SCIENTIFIC_CLAIM",
                "statement": "The narrower mechanism has support.",
                "disposition": "QUALIFIED",
                "rationale": "Alpha is broader than beta.",
                "provider_support": [
                    {
                        "provider": "alpha",
                        "stance": "CONCORDANT",
                        "assessment_claim_ids": ["alpha_claim"],
                        "report_quote": reports["alpha"].strip(),
                        "claim_origin": "PROVIDER_DISCOVERY",
                        "rationale": "Alpha directly states the broad claim.",
                    },
                    {
                        "provider": "beta",
                        "stance": "PARTIAL",
                        "assessment_claim_ids": ["beta_claim"],
                        "report_quote": reports["beta"].strip(),
                        "claim_origin": "PROVIDER_EXTRACTION",
                        "rationale": "Beta supports only the narrower claim.",
                    },
                ],
            }
        ],
    }
    path = root / "reconciliation.yaml"
    _write_yaml(path, data)
    return path, data


def test_valid_reconciliation_has_no_semantic_problems(tmp_path):
    path, _ = _fixture(tmp_path)

    assert list(iter_reconciliation_problems(path)) == []


def test_reconciliation_requires_complete_provider_coverage(tmp_path):
    path, data = _fixture(tmp_path)
    position = data["reconciled_claims"][0]["provider_support"][0]
    position.update({"stance": "SILENT"})
    for field in ("assessment_claim_ids", "report_quote", "claim_origin"):
        position.pop(field)
    data["reconciled_claims"][0]["provider_support"].pop()
    _write_yaml(path, data)

    problems = list(iter_reconciliation_problems(path))

    assert any("has no non-SILENT provider position" in problem for problem in problems)
    assert any("omits declared provider(s): beta" in problem for problem in problems)


def test_reconciliation_rejects_bad_claim_links_and_quotes(tmp_path):
    path, data = _fixture(tmp_path)
    position = data["reconciled_claims"][0]["provider_support"][0]
    position["assessment_claim_ids"] = ["missing_claim"]
    position["report_quote"] = "This sentence is absent from the report."
    _write_yaml(path, data)

    problems = list(iter_reconciliation_problems(path))

    assert any("does not resolve" in problem for problem in problems)
    assert any("not a verbatim substring" in problem for problem in problems)


def test_reconciliation_rejects_whitespace_only_quote_anchors(tmp_path):
    path, data = _fixture(tmp_path)
    data["reconciled_claims"][0]["provider_support"][0]["report_quote"] = "   "
    _write_yaml(path, data)

    problems = list(iter_reconciliation_problems(path))

    assert any("requires report_quote" in problem for problem in problems)


def test_reconciliation_rejects_whitespace_source_assessment_anchor(tmp_path):
    path, _ = _fixture(tmp_path)
    assessment_path = path.parent / "assessments/alpha-assessment-by-reviewer.yaml"
    assessment = yaml.safe_load(assessment_path.read_text(encoding="utf-8"))
    assessment["claims"][0]["report_quote"] = "   "
    _write_yaml(assessment_path, assessment)

    problems = list(iter_reconciliation_problems(path))

    assert any("must contain non-whitespace text" in problem for problem in problems)
    assert any("has no report_quote anchor" in problem for problem in problems)


def test_prior_provider_lineage_requires_a_different_declared_provider(tmp_path):
    path, data = _fixture(tmp_path)
    position = data["reconciled_claims"][0]["provider_support"][0]
    position["claim_origin"] = "PRIOR_PROVIDER_DERIVED"
    _write_yaml(path, data)

    problems = list(iter_reconciliation_problems(path))
    assert any("requires derived_from_provider" in problem for problem in problems)

    position["derived_from_provider"] = "alpha"
    _write_yaml(path, data)
    problems = list(iter_reconciliation_problems(path))
    assert any("cannot derive a claim from the same provider" in p for p in problems)


def test_reconciliation_rejects_cyclic_or_silent_provider_lineage(tmp_path):
    path, data = _fixture(tmp_path)
    positions = data["reconciled_claims"][0]["provider_support"]
    positions[0].update(
        {
            "claim_origin": "PRIOR_PROVIDER_DERIVED",
            "derived_from_provider": "beta",
        }
    )
    positions[1].update(
        {
            "claim_origin": "PRIOR_PROVIDER_DERIVED",
            "derived_from_provider": "alpha",
        }
    )
    _write_yaml(path, data)

    problems = list(iter_reconciliation_problems(path))
    assert any("cyclic provider lineage" in problem for problem in problems)

    positions[1]["stance"] = "SILENT"
    for field in (
        "assessment_claim_ids",
        "report_quote",
        "claim_origin",
        "derived_from_provider",
    ):
        positions[1].pop(field, None)
    _write_yaml(path, data)
    problems = list(iter_reconciliation_problems(path))
    assert any("derives from SILENT provider 'beta'" in p for p in problems)


def test_reconciliation_rejects_duplicate_providers_and_claim_ids(tmp_path):
    path, data = _fixture(tmp_path)
    data["providers"].append(deepcopy(data["providers"][0]))
    data["reconciled_claims"].append(deepcopy(data["reconciled_claims"][0]))
    _write_yaml(path, data)

    problems = list(iter_reconciliation_problems(path))

    assert any("duplicates provider 'alpha'" in problem for problem in problems)
    assert any(
        "duplicates claim_id 'shared_mechanism'" in problem for problem in problems
    )


def test_reconciliation_requires_schema_valid_source_assessments(tmp_path):
    path, _ = _fixture(tmp_path)
    assessment_path = path.parent / "assessments/alpha-assessment-by-reviewer.yaml"
    assessment = yaml.safe_load(assessment_path.read_text(encoding="utf-8"))
    assessment.pop("overall_verdict")
    _write_yaml(assessment_path, assessment)

    problems = list(iter_reconciliation_problems(path))

    assert any("source assessment schema invalid" in problem for problem in problems)
    assert any("overall_verdict" in problem for problem in problems)


def test_reconciliation_rejects_duplicate_source_assessment_claim_ids(tmp_path):
    path, _ = _fixture(tmp_path)
    assessment_path = path.parent / "assessments/alpha-assessment-by-reviewer.yaml"
    assessment = yaml.safe_load(assessment_path.read_text(encoding="utf-8"))
    assessment["claims"].append(deepcopy(assessment["claims"][0]))
    _write_yaml(assessment_path, assessment)

    problems = list(iter_reconciliation_problems(path))

    assert any("duplicates claim_id 'alpha_claim'" in problem for problem in problems)


def test_reconciliation_handles_malformed_source_assessment_types(tmp_path):
    path, _ = _fixture(tmp_path)
    assessment_path = path.parent / "assessments/alpha-assessment-by-reviewer.yaml"
    assessment = yaml.safe_load(assessment_path.read_text(encoding="utf-8"))
    assessment["claims"] = 42
    _write_yaml(assessment_path, assessment)

    problems = list(iter_reconciliation_problems(path))

    assert any("source assessment schema invalid" in problem for problem in problems)
    assert any("claims must be a list" in problem for problem in problems)


def test_reconciliation_handles_malformed_nested_collection_types(tmp_path):
    path, data = _fixture(tmp_path)
    valid_support = deepcopy(data["reconciled_claims"][0]["provider_support"])
    data["reconciled_claims"][0]["provider_support"] = 42
    data["artifacts"] = 42
    _write_yaml(path, data)

    problems = list(iter_reconciliation_problems(path))

    assert any("provider_support must be a list" in problem for problem in problems)
    assert any("artifacts must be a list" in problem for problem in problems)

    data["reconciled_claims"][0]["provider_support"] = valid_support
    data.pop("artifacts")
    valid_support[0]["assessment_claim_ids"] = 42
    _write_yaml(path, data)
    problems = list(iter_reconciliation_problems(path))
    assert any("assessment_claim_ids must be a list" in p for p in problems)


def test_reconciliation_enforces_repository_and_raw_report_layout(tmp_path):
    path, data = _fixture(tmp_path)
    misplaced_path = tmp_path / "reconciliation.yaml"
    _write_yaml(misplaced_path, data)

    problems = list(iter_reconciliation_problems(misplaced_path))
    assert any("must live at kb/hypotheses" in problem for problem in problems)

    nested = path.parent / "nested"
    nested.mkdir()
    nested_report = nested / "alpha.md"
    nested_report.write_text(
        (path.parent / "alpha.md").read_text(encoding="utf-8"), encoding="utf-8"
    )
    data["providers"][0]["source_report"] = "nested/alpha.md"
    assessment_path = path.parent / "assessments/alpha-assessment-by-reviewer.yaml"
    assessment = yaml.safe_load(assessment_path.read_text(encoding="utf-8"))
    assessment["source_report"] = "../nested/alpha.md"
    _write_yaml(assessment_path, assessment)
    _write_yaml(path, data)

    problems = list(iter_reconciliation_problems(path))
    assert any("raw .md report directly" in problem for problem in problems)
