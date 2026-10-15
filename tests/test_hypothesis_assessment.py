"""Focused tests for hypothesis-assessment data and analysis provenance."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin

from dismech.hypothesis_assessment import iter_assessment_problems

_SCHEMA = Path(__file__).parents[1] / "src/dismech/schema/hypothesis_assessment.yaml"


def _write_yaml(path: Path, data: dict) -> None:
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")


def _fixture(tmp_path: Path) -> tuple[Path, dict]:
    root = tmp_path / "kb/hypotheses/Test_Disease/dataset_model"
    assessments = root / "assessments"
    artifacts = root / "provider_artifacts"
    assessments.mkdir(parents=True)
    artifacts.mkdir()
    (root / "provider.md").write_text(
        "The deposited cohort analysis supports the mechanism.\n", encoding="utf-8"
    )
    for name, content in {
        "input-manifest.json": "{}\n",
        "analysis.py": "print('analysis')\n",
        "uv.lock": "version = 1\n",
        "results.csv": "feature,value\nA,1\n",
        "run.log": "completed\n",
    }.items():
        (artifacts / name).write_text(content, encoding="utf-8")

    data = {
        "schema_version": "1.1.0",
        "provider": "provider",
        "assessor": "reviewer",
        "source_report": "../provider.md",
        "hypothesis_id": "dataset_model",
        "assessed_at": "2026-08-29T00:00:00Z",
        "overall_verdict": "PARTIALLY_SUPPORTED",
        "summary": "The provider preserved a reproducible dataset analysis.",
        "artifact_root": "../provider_artifacts",
        "data_sources": [
            {
                "data_source_id": "geo_cohort",
                "source_type": "PUBLIC_DATASET",
                "name": "Test GEO cohort",
                "identifier": "geo:GSE000000",
                "version": "series-matrix retrieved 2026-08-29",
                "uri": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE000000",
                "retrieved_at": "2026-08-29T00:00:00Z",
                "access_status": "ACCESSED",
                "query": "GSE000000",
                "cohort": "Affected and control samples",
                "subset": "Pretreatment samples",
                "organism": "Homo sapiens",
                "tissue": "whole blood",
                "assay": "RNA-seq",
                "checksum": f"sha256:{'a' * 64}",
                "byte_count": 3,
                "source_artifacts": ["../provider_artifacts/input-manifest.json"],
            }
        ],
        "analyses": [
            {
                "analysis_id": "cohort_analysis",
                "status": "SUCCEEDED",
                "auditability": "REPRODUCIBLE",
                "method": "Normalize counts and compare affected with control samples.",
                "comparison": "Affected versus control samples",
                "input_data_source_ids": ["geo_cohort"],
                "software": [
                    {
                        "software_name": "analysis-tool",
                        "software_version": "1.2.3",
                        "software_uri": "https://example.org/analysis-tool",
                    }
                ],
                "parameters": ["normalization=median-ratio", "fdr=0.05"],
                "code_artifacts": ["../provider_artifacts/analysis.py"],
                "environment_artifact": "../provider_artifacts/uv.lock",
                "output_artifacts": ["../provider_artifacts/results.csv"],
            }
        ],
        "claims": [
            {
                "claim_id": "cohort_result",
                "statement": "The deposited cohort supports the mechanism.",
                "disposition": "RETAINED",
                "report_quote": "The deposited cohort analysis supports the mechanism.",
                "rationale": "The committed analysis record supports the result.",
                "analysis_ids": ["cohort_analysis"],
            }
        ],
    }
    path = assessments / "provider-assessment-by-reviewer.yaml"
    _write_yaml(path, data)
    return path, data


def test_reproducible_dataset_analysis_is_schema_and_semantically_valid(tmp_path):
    path, data = _fixture(tmp_path)
    report = Validator(
        _SCHEMA,
        validation_plugins=[JsonschemaValidationPlugin(closed=True)],
    ).validate(data, target_class="HypothesisAssessment")

    assert [
        result for result in report.results if result.severity.name == "ERROR"
    ] == []
    assert list(iter_assessment_problems(path)) == []


def test_assessment_layout_and_hypothesis_directory_identity_are_enforced(tmp_path):
    path, data = _fixture(tmp_path)
    data["hypothesis_id"] = "different_model"
    _write_yaml(path, data)

    assert any(
        "hypothesis_id='different_model' does not match directory 'dataset_model'"
        in problem
        for problem in iter_assessment_problems(path)
    )

    misplaced = (
        tmp_path
        / "not-kb/hypotheses/Test_Disease/dataset_model/assessments"
        / path.name
    )
    misplaced.parent.mkdir(parents=True)
    data["hypothesis_id"] = "dataset_model"
    _write_yaml(misplaced, data)
    assert any(
        "must live at kb/hypotheses/<Disease>/<hypothesis_id>/assessments/" in problem
        for problem in iter_assessment_problems(misplaced)
    )


def test_data_source_checksum_requires_a_complete_sha256_digest(tmp_path):
    path, data = _fixture(tmp_path)
    source = data["data_sources"][0]
    invalid_checksums = (
        "a" * 64,
        f"sha256:{'a' * 63}",
        f"sha256:{'g' * 64}",
        f"SHA256:{'a' * 64}",
    )
    for checksum in invalid_checksums:
        source["checksum"] = checksum
        _write_yaml(path, data)
        assert any(
            "checksum must use sha256:<64 hexadecimal characters>" in problem
            for problem in iter_assessment_problems(path)
        )

    source["checksum"] = f"sha256:{'A' * 64}"
    _write_yaml(path, data)
    assert list(iter_assessment_problems(path)) == []


def test_successful_negative_search_analysis_is_valid(tmp_path):
    path, data = _fixture(tmp_path)
    source = data["data_sources"][0]
    source.update(
        {
            "access_status": "SEARCHED_NO_RESULT",
            "query": "condition AND transcriptomics",
            "source_artifacts": ["../provider_artifacts/run.log"],
        }
    )
    data["analyses"][0]["method"] = "Execute and preserve a negative dataset search."
    _write_yaml(path, data)

    assert list(iter_assessment_problems(path)) == []


def test_artifacts_must_be_nonempty_regular_files(tmp_path):
    path, data = _fixture(tmp_path)
    artifact_root = path.parent.parent / "provider_artifacts"
    for name in ("empty-source.json", "empty-environment.lock", "empty-output.csv"):
        (artifact_root / name).write_text("", encoding="utf-8")
    (artifact_root / "code-directory").mkdir()
    (artifact_root / "empty-narrative.md").write_text("", encoding="utf-8")

    data["data_sources"][0]["source_artifacts"] = [
        "../provider_artifacts/empty-source.json"
    ]
    analysis = data["analyses"][0]
    analysis["code_artifacts"] = ["../provider_artifacts/code-directory"]
    analysis["environment_artifact"] = "../provider_artifacts/empty-environment.lock"
    analysis["output_artifacts"] = ["../provider_artifacts/empty-output.csv"]
    data["artifacts"] = ["../provider_artifacts/empty-narrative.md"]
    _write_yaml(path, data)

    problems = list(iter_assessment_problems(path))

    assert any("source_artifacts[0]" in p and "is empty" in p for p in problems)
    assert any("code_artifacts[0]" in p and "not a regular file" in p for p in problems)
    assert any("environment_artifact" in p and "is empty" in p for p in problems)
    assert any("output_artifacts[0]" in p and "is empty" in p for p in problems)
    assert any("artifacts[0]" in p and "is empty" in p for p in problems)


def test_structured_artifacts_are_provider_local_and_not_metadata_files(tmp_path):
    path, data = _fixture(tmp_path)
    root = path.parent.parent
    (root / "provider.md.citations.md").write_text("PMID:1\n", encoding="utf-8")
    other_root = root / "other-provider_artifacts"
    other_root.mkdir()
    (other_root / "result.csv").write_text("result\n", encoding="utf-8")

    data["data_sources"][0]["source_artifacts"] = ["../provider.md"]
    analysis = data["analyses"][0]
    analysis["code_artifacts"] = ["provider-assessment-by-reviewer.yaml"]
    analysis["environment_artifact"] = "../provider.md.citations.md"
    analysis["output_artifacts"] = ["../other-provider_artifacts/result.csv"]
    _write_yaml(path, data)

    problems = list(iter_assessment_problems(path))

    assert any("must not point to a raw report" in p for p in problems)
    assert any("must not point inside assessments/" in p for p in problems)
    assert any("must not point to a citation sidecar" in p for p in problems)
    assert any("must be beneath artifact_root" in p for p in problems)


def test_structured_artifacts_require_exact_provider_artifact_root(tmp_path):
    path, data = _fixture(tmp_path)
    data.pop("artifact_root")
    _write_yaml(path, data)
    assert any(
        "artifact_root is required when structured artifacts are declared" in problem
        for problem in iter_assessment_problems(path)
    )

    wrong_root = path.parent.parent / "other_artifacts"
    wrong_root.mkdir()
    data["artifact_root"] = "../other_artifacts"
    _write_yaml(path, data)
    assert any(
        "artifact_root must resolve to the provider-specific directory" in problem
        for problem in iter_assessment_problems(path)
    )


def test_reproducible_analysis_artifact_roles_are_pairwise_disjoint(tmp_path):
    path, data = _fixture(tmp_path)
    shared = "../provider_artifacts/analysis.py"
    analysis = data["analyses"][0]
    analysis["environment_artifact"] = shared
    analysis["output_artifacts"] = [shared]
    _write_yaml(path, data)

    problems = list(iter_assessment_problems(path))

    assert any(
        "reused across code_artifacts and environment_artifact" in p for p in problems
    )
    assert any(
        "reused across code_artifacts and output_artifacts" in p for p in problems
    )


def test_accessed_database_and_api_sources_require_queries(tmp_path):
    path, data = _fixture(tmp_path)
    source = data["data_sources"][0]
    source.pop("query")
    for source_type in ("DATABASE", "API"):
        source["source_type"] = source_type
        _write_yaml(path, data)
        assert any(
            f"ACCESSED {source_type} requires query" in problem
            for problem in iter_assessment_problems(path)
        )


def test_accessed_and_negative_search_sources_require_a_committed_record(tmp_path):
    path, data = _fixture(tmp_path)
    source = data["data_sources"][0]
    source.pop("retrieved_at")
    source["source_artifacts"] = ["../../../outside.json"]
    _write_yaml(path, data)

    problems = list(iter_assessment_problems(path))

    assert any("ACCESSED requires retrieved_at" in problem for problem in problems)
    assert any("escapes the hypothesis directory" in problem for problem in problems)

    source.update(
        {
            "access_status": "SEARCHED_NO_RESULT",
            "retrieved_at": "2026-08-29T00:00:00Z",
            "source_artifacts": ["../provider_artifacts/run.log"],
        }
    )
    source.pop("query")
    data["analyses"] = []
    data["claims"][0].pop("analysis_ids")
    _write_yaml(path, data)
    assert any(
        "SEARCHED_NO_RESULT requires query" in problem
        for problem in iter_assessment_problems(path)
    )


def test_succeeded_analysis_requires_complete_reproducibility_record(tmp_path):
    path, data = _fixture(tmp_path)
    analysis = data["analyses"][0]
    analysis["software"][0].pop("software_version")
    analysis.pop("code_artifacts")
    analysis.pop("environment_artifact")
    analysis.pop("output_artifacts")
    _write_yaml(path, data)

    problems = list(iter_assessment_problems(path))

    assert any("software_version is required" in problem for problem in problems)
    assert any("requires code_artifacts" in problem for problem in problems)
    assert any("requires environment_artifact" in problem for problem in problems)
    assert any("requires output_artifacts" in problem for problem in problems)


def test_reported_only_analysis_cannot_support_a_retained_claim(tmp_path):
    path, data = _fixture(tmp_path)
    analysis = data["analyses"][0]
    analysis.update(
        {
            "status": "REPORTED_ONLY",
            "auditability": "UNVERIFIABLE",
            "status_reason": "The report provides prose results but no execution record.",
        }
    )
    for field in ("code_artifacts", "environment_artifact", "output_artifacts"):
        analysis.pop(field)
    _write_yaml(path, data)

    problems = list(iter_assessment_problems(path))

    assert any("RETAINED claim cannot rely on analysis" in p for p in problems)

    data["claims"][0]["disposition"] = "NEEDS_VERIFICATION"
    _write_yaml(path, data)
    assert list(iter_assessment_problems(path)) == []


def test_reported_only_analysis_may_preserve_partial_artifacts(tmp_path):
    path, data = _fixture(tmp_path)
    analysis = data["analyses"][0]
    analysis.update(
        {
            "status": "REPORTED_ONLY",
            "auditability": "PARTIALLY_AUDITABLE",
            "status_reason": (
                "The provider preserved outputs, but they do not establish execution."
            ),
        }
    )
    data["claims"][0]["disposition"] = "NEEDS_VERIFICATION"
    _write_yaml(path, data)

    assert list(iter_assessment_problems(path)) == []


def test_qualified_analysis_claim_requires_a_usable_linked_run(tmp_path):
    path, data = _fixture(tmp_path)
    analysis = data["analyses"][0]
    analysis.update(
        {
            "status": "REPORTED_ONLY",
            "auditability": "PARTIALLY_AUDITABLE",
            "status_reason": "Outputs exist, but execution cannot be established.",
        }
    )
    data["claims"][0]["disposition"] = "QUALIFIED"
    _write_yaml(path, data)

    assert any(
        "QUALIFIED claim with analysis_ids requires at least one SUCCEEDED or PARTIAL"
        in problem
        for problem in iter_assessment_problems(path)
    )

    partial = deepcopy(analysis)
    partial.update(
        {
            "analysis_id": "partial_analysis",
            "status": "PARTIAL",
            "auditability": "PARTIALLY_AUDITABLE",
            "status_reason": "The run completed only the primary comparison.",
        }
    )
    data["analyses"].append(partial)
    data["claims"][0]["analysis_ids"].append("partial_analysis")
    _write_yaml(path, data)
    assert list(iter_assessment_problems(path)) == []


def test_successful_analysis_rejects_unaccessed_inputs_and_bad_foreign_keys(tmp_path):
    path, data = _fixture(tmp_path)
    data["data_sources"][0].update(
        {
            "access_status": "CITED_NOT_ACCESSED",
        }
    )
    data["data_sources"][0].pop("retrieved_at")
    data["data_sources"][0].pop("source_artifacts")
    data["analyses"][0]["input_data_source_ids"].append("missing_source")
    data["claims"][0]["analysis_ids"].append("missing_analysis")
    _write_yaml(path, data)

    problems = list(iter_assessment_problems(path))

    assert any("cannot use 'geo_cohort'" in problem for problem in problems)
    assert any(
        "input_data_source_id='missing_source' does not resolve" in p for p in problems
    )
    assert any("analysis_id='missing_analysis' does not resolve" in p for p in problems)


def test_fallback_lineage_must_resolve_from_an_unsuccessful_analysis(tmp_path):
    path, data = _fixture(tmp_path)
    fallback = data["analyses"][0]
    fallback["fallback_from_analysis_id"] = "primary_analysis"
    fallback["status_reason"] = (
        "The preferred provider toolbox failed, so this documented fallback ran."
    )
    primary = {
        "analysis_id": "primary_analysis",
        "status": "FAILED",
        "auditability": "REPRODUCIBLE",
        "method": "Run the preferred provider toolbox.",
        "input_data_source_ids": ["geo_cohort"],
        "software": [{"software_name": "preferred-tool", "software_version": "1.0"}],
        "code_artifacts": ["../provider_artifacts/analysis.py"],
        "environment_artifact": "../provider_artifacts/uv.lock",
        "output_artifacts": ["../provider_artifacts/run.log"],
        "status_reason": "The required provider tool could not be imported.",
    }
    data["analyses"].insert(0, primary)
    _write_yaml(path, data)
    assert list(iter_assessment_problems(path)) == []

    fallback.pop("status_reason")
    _write_yaml(path, data)
    assert any(
        "fallback_from_analysis_id requires status_reason" in problem
        for problem in iter_assessment_problems(path)
    )
    fallback["status_reason"] = "The preferred provider toolbox failed."

    primary.update(
        {
            "status": "SUCCEEDED",
            "auditability": "REPRODUCIBLE",
            "input_data_source_ids": ["geo_cohort"],
            "software": [
                {"software_name": "preferred-tool", "software_version": "1.0"}
            ],
            "code_artifacts": ["../provider_artifacts/analysis.py"],
            "environment_artifact": "../provider_artifacts/uv.lock",
            "output_artifacts": ["../provider_artifacts/results.csv"],
        }
    )
    primary.pop("status_reason")
    _write_yaml(path, data)

    assert any(
        "fallback source 'primary_analysis' must have status" in problem
        for problem in iter_assessment_problems(path)
    )

    primary.update(
        {
            "status": "FAILED",
            "auditability": "UNVERIFIABLE",
            "status_reason": "The preferred tool failed.",
            "fallback_from_analysis_id": "cohort_analysis",
        }
    )
    for field in (
        "input_data_source_ids",
        "software",
        "code_artifacts",
        "environment_artifact",
        "output_artifacts",
    ):
        primary.pop(field)
    _write_yaml(path, data)
    assert any(
        "cyclic fallback lineage" in problem
        for problem in iter_assessment_problems(path)
    )


def test_duplicate_dataset_analysis_and_claim_links_are_rejected(tmp_path):
    path, data = _fixture(tmp_path)
    data["data_sources"].append(deepcopy(data["data_sources"][0]))
    data["analyses"].append(deepcopy(data["analyses"][0]))
    data["claims"][0]["analysis_ids"].append("cohort_analysis")
    _write_yaml(path, data)

    problems = list(iter_assessment_problems(path))

    assert any("duplicates data_source_id 'geo_cohort'" in p for p in problems)
    assert any("duplicates analysis_id 'cohort_analysis'" in p for p in problems)
    assert any(
        "claims[0] duplicates analysis_id 'cohort_analysis'" in p for p in problems
    )
