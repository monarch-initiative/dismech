"""Tests for mechanistic hypothesis deep-research helpers."""

from __future__ import annotations

import hashlib
import importlib.util
import io
import subprocess
import sys
import zipfile
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
SCRIPT_PATH = ROOT / "scripts" / "hypothesis_deep_research.py"
SPEC = importlib.util.spec_from_file_location("hypothesis_deep_research", SCRIPT_PATH)
assert SPEC and SPEC.loader
hypothesis_deep_research = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = hypothesis_deep_research
SPEC.loader.exec_module(hypothesis_deep_research)


def write_disorder(kb_dir: Path) -> Path:
    path = kb_dir / "Long_COVID.yaml"
    path.write_text(
        """
name: Long COVID
category: Complex
mechanistic_hypotheses:
- hypothesis_group_id: canonical_persistence_immune_model
  hypothesis_label: Canonical Viral Persistence-Immune Dysregulation Model
  status: CANONICAL
  description: >
    Persistent viral RNA/antigen reservoirs sustain immune activation and downstream
    multisystem dysfunction.
  applies_to_subtypes:
  - Pain-dominant long COVID phenotype
  evidence:
  - reference: PMID:37140960
    supports: SUPPORT
    evidence_source: HUMAN_CLINICAL
    snippet: "Persistence of SARS-CoV-2 RNA or antigens is reported in some organs"
    explanation: Supports reservoir persistence.
- hypothesis_group_id: vascular_microclot_model
  hypothesis_label: Endothelial-Microclot Perfusion Model
  status: ALTERNATIVE
  description: Microclots impair perfusion.
""".strip()
        + "\n",
        encoding="utf-8",
    )
    return path


def test_find_hypothesis_resolves_disorder_case_insensitively(tmp_path: Path) -> None:
    kb_dir = tmp_path / "kb" / "disorders"
    kb_dir.mkdir(parents=True)
    write_disorder(kb_dir)

    record = hypothesis_deep_research.find_hypothesis(
        kb_dir,
        "long_covid",
        "canonical_persistence_immune_model",
    )

    assert record.disease_slug == "Long_COVID"
    assert record.disease_name == "Long COVID"
    assert record.category == "Complex"
    assert (
        record.hypothesis_label
        == "Canonical Viral Persistence-Immune Dysregulation Model"
    )


def test_dump_hypothesis_yaml_preserves_seed_content(tmp_path: Path) -> None:
    kb_dir = tmp_path / "kb" / "disorders"
    kb_dir.mkdir(parents=True)
    write_disorder(kb_dir)
    record = hypothesis_deep_research.find_hypothesis(
        kb_dir,
        "Long_COVID",
        "canonical_persistence_immune_model",
    )

    rendered = hypothesis_deep_research.dump_hypothesis_yaml(record)

    assert "hypothesis_group_id: canonical_persistence_immune_model" in rendered
    assert (
        "hypothesis_label: Canonical Viral Persistence-Immune Dysregulation Model"
        in rendered
    )
    assert "reference: PMID:37140960" in rendered
    assert "Persistent viral RNA/antigen reservoirs" in rendered


def test_build_command_writes_under_kb_hypotheses_and_aliases_edison(
    tmp_path: Path,
) -> None:
    kb_dir = tmp_path / "kb" / "disorders"
    output_root = tmp_path / "kb" / "hypotheses"
    template = tmp_path / "templates" / "hypothesis.md"
    kb_dir.mkdir(parents=True)
    template.parent.mkdir(parents=True)
    template.write_text("Hypothesis {hypothesis_group_id}\n", encoding="utf-8")
    write_disorder(kb_dir)
    record = hypothesis_deep_research.find_hypothesis(
        kb_dir,
        "Long_COVID",
        "canonical_persistence_immune_model",
    )

    command = hypothesis_deep_research.build_command(
        record,
        provider="edison",
        output_root=output_root,
        template=template,
        extra_args=["--param", "max_iterations=1"],
    )

    assert "--provider" in command
    assert command[command.index("--provider") + 1] == "falcon"
    assert "disease_slug=Long_COVID" not in command
    output_file = (
        output_root / "Long_COVID" / "canonical_persistence_immune_model" / "falcon.md"
    )
    assert str(output_file) in command
    assert f"{output_file}.citations.md" in command
    assert command[-2:] == ["--param", "max_iterations=1"]


def test_runner_binds_new_report_to_exact_manifest_bytes(tmp_path: Path) -> None:
    report = tmp_path / "biomni.md"
    report.write_text(
        "---\nprovider: biomni\n---\n\n"
        "## Question\n\nRun it.\n\n"
        "## Output\n\nANALYSIS_STATUS: SUCCEEDED\n",
        encoding="utf-8",
    )
    artifacts = tmp_path / "biomni_artifacts"
    artifacts.mkdir()
    manifest = artifacts / "MANIFEST.yaml"
    manifest.write_text("schema_version: '1.0'\nstatus: SUCCEEDED\n", encoding="utf-8")

    detail = hypothesis_deep_research.bind_report_to_artifact_manifest(
        report, artifacts
    )

    assert detail == ""
    lines = report.read_text(encoding="utf-8").splitlines()
    frontmatter_end = lines.index("---", 1)
    metadata = yaml.safe_load("\n".join(lines[1:frontmatter_end]))
    expected = f"sha256:{hashlib.sha256(manifest.read_bytes()).hexdigest()}"
    assert metadata["artifact_manifest_sha256"] == expected
    assert "## Output\n\nANALYSIS_STATUS: SUCCEEDED" in report.read_text(
        encoding="utf-8"
    )


def test_biomni_defaults_to_persistent_lake_and_allows_override(
    monkeypatch,
) -> None:
    monkeypatch.setenv("BIOMNI_DATA_PATH", "/tmp/test-biomni-lake")

    assert hypothesis_deep_research.provider_default_params("biomni", []) == [
        "--param",
        "path=/tmp/test-biomni-lake",
        "--param",
        "skip_data_lake=false",
    ]
    assert hypothesis_deep_research.provider_default_params(
        "biomni", ["--param", "path=/tmp/explicit-lake"]
    ) == ["--param", "skip_data_lake=false"]
    assert (
        hypothesis_deep_research.provider_default_params(
            "biomni",
            ["--param", "path=/tmp/explicit-lake", "--param", "skip_data_lake=true"],
        )
        == []
    )


def test_dataset_template_gets_canonical_artifact_dir_and_explicit_inputs(
    tmp_path: Path, monkeypatch
) -> None:
    kb_dir = tmp_path / "kb" / "disorders"
    output_root = tmp_path / "kb" / "hypotheses"
    kb_dir.mkdir(parents=True)
    write_disorder(kb_dir)
    record = hypothesis_deep_research.find_hypothesis(
        kb_dir,
        "Long_COVID",
        "canonical_persistence_immune_model",
    )
    template = ROOT / "templates" / "hypothesis_dataset_analysis.md"
    monkeypatch.delenv("DISMECH_ENABLE_BIOMNI", raising=False)

    result = hypothesis_deep_research.run_record(
        record,
        provider="biomni",
        output_root=output_root,
        template=template,
        extra_args=[],
        timeout_seconds=1,
        dry_run=True,
        overwrite=False,
        template_overrides={
            "dataset_inputs": "geo:GSE1",
            "target_variables": "FDX1",
            "analysis_objective": "Compare case with control.",
        },
        repo_root=tmp_path,
    )

    artifact_dir = Path(
        "kb/hypotheses/Long_COVID/canonical_persistence_immune_model/biomni_artifacts"
    )
    assert result.status == "DRY_RUN"
    assert f"artifact_dir={artifact_dir}" in result.command
    assert "dataset_inputs=geo:GSE1" in result.command


def test_dataset_template_rejects_missing_or_overridden_runner_vars(
    tmp_path: Path,
) -> None:
    kb_dir = tmp_path / "kb" / "disorders"
    output_root = tmp_path / "kb" / "hypotheses"
    kb_dir.mkdir(parents=True)
    write_disorder(kb_dir)
    record = hypothesis_deep_research.find_hypothesis(
        kb_dir,
        "Long_COVID",
        "canonical_persistence_immune_model",
    )
    template = ROOT / "templates" / "hypothesis_dataset_analysis.md"

    missing = hypothesis_deep_research.run_record(
        record,
        provider="biomni",
        output_root=output_root,
        template=template,
        extra_args=[],
        timeout_seconds=1,
        dry_run=True,
        overwrite=False,
    )
    overridden = hypothesis_deep_research.run_record(
        record,
        provider="biomni",
        output_root=output_root,
        template=template,
        extra_args=["--var", "artifact_dir=/tmp/not-canonical"],
        timeout_seconds=1,
        dry_run=True,
        overwrite=False,
        template_overrides={
            "dataset_inputs": "geo:GSE1",
            "target_variables": "FDX1",
            "analysis_objective": "Compare case with control.",
        },
    )

    assert missing.status == "INVALID_TEMPLATE_VARIABLES"
    assert "analysis_objective" in missing.detail
    assert overridden.status == "INVALID_TEMPLATE_VARIABLES"
    assert "runner-controlled" in overridden.detail

    blank = hypothesis_deep_research.run_record(
        record,
        provider="biomni",
        output_root=output_root,
        template=template,
        extra_args=[],
        timeout_seconds=1,
        dry_run=True,
        overwrite=False,
        template_overrides={
            "dataset_inputs": " ",
            "target_variables": "FDX1",
            "analysis_objective": "Compare case with control.",
        },
    )
    assert blank.status == "INVALID_TEMPLATE_VARIABLES"
    assert "dataset_inputs" in blank.detail


def test_run_missing_rejects_execution_gated_dataset_template(
    tmp_path: Path, capsys
) -> None:
    kb_dir = tmp_path / "kb" / "disorders"
    output_root = tmp_path / "kb" / "hypotheses"
    kb_dir.mkdir(parents=True)
    write_disorder(kb_dir)

    status = hypothesis_deep_research.main(
        [
            "run-missing",
            "biomni",
            "--kb-dir",
            str(kb_dir),
            "--output-root",
            str(output_root),
            "--template",
            str(ROOT / "templates" / "hypothesis_dataset_analysis.md"),
        ]
    )

    assert status == 2
    assert "use the run command" in capsys.readouterr().err


def test_run_missing_rejects_named_biomni_fallback_before_writing_report(
    tmp_path: Path, monkeypatch, capsys
) -> None:
    kb_dir = tmp_path / "kb" / "disorders"
    output_root = tmp_path / "kb" / "hypotheses"
    report_dir = tmp_path / "output"
    template = tmp_path / "templates" / "literature.md"
    kb_dir.mkdir(parents=True)
    template.parent.mkdir(parents=True)
    template.write_text("Write a literature report.\n", encoding="utf-8")
    write_disorder(kb_dir)
    monkeypatch.delenv("DISMECH_ENABLE_BIOMNI", raising=False)

    status = hypothesis_deep_research.main(
        [
            "run-missing",
            "openscientist",
            "--kb-dir",
            str(kb_dir),
            "--output-root",
            str(output_root),
            "--template",
            str(template),
            "--report-dir",
            str(report_dir),
            "--",
            "--fallback-provider",
            "biomni",
        ]
    )

    assert status == 2
    assert "DISMECH_ENABLE_BIOMNI=1" in capsys.readouterr().err
    assert not report_dir.exists()


def test_existing_outputs_detects_citations_and_artifacts(tmp_path: Path) -> None:
    kb_dir = tmp_path / "kb" / "disorders"
    output_root = tmp_path / "kb" / "hypotheses"
    kb_dir.mkdir(parents=True)
    write_disorder(kb_dir)
    record = hypothesis_deep_research.find_hypothesis(
        kb_dir,
        "Long_COVID",
        "canonical_persistence_immune_model",
    )
    output_dir = output_root / "Long_COVID" / "canonical_persistence_immune_model"
    output_dir.mkdir(parents=True)
    (output_dir / "openscientist.md").write_text("report\n", encoding="utf-8")
    (output_dir / "openscientist.md.citations.md").write_text(
        "PMID:1\n", encoding="utf-8"
    )
    artifact_dir = output_dir / "openscientist_artifacts"
    artifact_dir.mkdir()
    (artifact_dir / "matrix.md").write_text("artifact\n", encoding="utf-8")

    outputs = hypothesis_deep_research.existing_outputs(record, output_root)

    assert len(outputs) == 1
    assert outputs[0].provider == "openscientist"
    assert outputs[0].citations_exists is True
    assert outputs[0].artifact_exists is True


def test_existing_outputs_ignores_only_raw_or_empty_artifacts(tmp_path: Path) -> None:
    kb_dir = tmp_path / "kb" / "disorders"
    output_root = tmp_path / "kb" / "hypotheses"
    kb_dir.mkdir(parents=True)
    write_disorder(kb_dir)
    record = hypothesis_deep_research.find_hypothesis(
        kb_dir,
        "Long_COVID",
        "canonical_persistence_immune_model",
    )
    output_dir = output_root / "Long_COVID" / "canonical_persistence_immune_model"
    output_dir.mkdir(parents=True)
    (output_dir / "biomni.md").write_text("report\n", encoding="utf-8")
    artifact_dir = output_dir / "biomni_artifacts"
    (artifact_dir / "raw").mkdir(parents=True)
    (artifact_dir / "raw" / "matrix.tsv").write_text("raw\n", encoding="utf-8")
    (artifact_dir / "empty.txt").write_text("", encoding="utf-8")

    outputs = hypothesis_deep_research.existing_outputs(record, output_root)

    assert len(outputs) == 1
    assert outputs[0].artifact_exists is False

    (artifact_dir / "nested").mkdir()
    (artifact_dir / "nested" / "MANIFEST.yaml").write_text(
        "status: FAILED\n", encoding="utf-8"
    )
    outputs = hypothesis_deep_research.existing_outputs(record, output_root)
    assert outputs[0].artifact_exists is True


def test_run_record_dry_run_does_not_create_output(tmp_path: Path) -> None:
    kb_dir = tmp_path / "kb" / "disorders"
    output_root = tmp_path / "kb" / "hypotheses"
    template = tmp_path / "templates" / "hypothesis.md"
    kb_dir.mkdir(parents=True)
    template.parent.mkdir(parents=True)
    template.write_text("Hypothesis {hypothesis_group_id}\n", encoding="utf-8")
    write_disorder(kb_dir)
    record = hypothesis_deep_research.find_hypothesis(
        kb_dir,
        "Long_COVID",
        "canonical_persistence_immune_model",
    )

    result = hypothesis_deep_research.run_record(
        record,
        provider="openscientist",
        output_root=output_root,
        template=template,
        extra_args=[],
        timeout_seconds=1,
        dry_run=True,
        overwrite=False,
    )

    assert result.status == "DRY_RUN"
    assert result.provider == "openscientist"
    assert not result.output_file.exists()


FELL_BACK_REPORT = """---
provider: claude_code
fell_back: true
requested_provider: falcon
---

# Report
"""


def _run_with(monkeypatch, tmp_path: Path, returncode: int):
    """Run one hypothesis job whose client wrote a fallback report and exited.

    The client writes the report before it validates it, so a validation
    failure exits 3 with a real report already on disk.
    """
    import subprocess

    kb_dir = tmp_path / "kb" / "disorders"
    output_root = tmp_path / "kb" / "hypotheses"
    template = tmp_path / "templates" / "hypothesis.md"
    kb_dir.mkdir(parents=True)
    template.parent.mkdir(parents=True)
    template.write_text("Hypothesis {hypothesis_group_id}\n", encoding="utf-8")
    write_disorder(kb_dir)
    record = hypothesis_deep_research.find_hypothesis(
        kb_dir, "Long_COVID", "canonical_persistence_immune_model"
    )
    written = hypothesis_deep_research.output_file_for(record, output_root, "falcon")

    def fake_run(command, **kwargs):
        written.parent.mkdir(parents=True, exist_ok=True)
        written.write_text(FELL_BACK_REPORT, encoding="utf-8")
        return subprocess.CompletedProcess(command, returncode, stdout="", stderr="")

    monkeypatch.setattr(subprocess, "run", fake_run)
    return hypothesis_deep_research.run_record(
        record,
        provider="falcon",
        output_root=output_root,
        template=template,
        extra_args=[],
        timeout_seconds=10,
        dry_run=False,
        overwrite=True,
    )


def test_biomni_execution_is_disabled_by_default_before_side_effects(
    tmp_path: Path, monkeypatch
) -> None:
    kb_dir = tmp_path / "kb" / "disorders"
    output_root = tmp_path / "kb" / "hypotheses"
    template = tmp_path / "templates" / "hypothesis.md"
    kb_dir.mkdir(parents=True)
    template.parent.mkdir(parents=True)
    template.write_text("Hypothesis {hypothesis_group_id}\n", encoding="utf-8")
    write_disorder(kb_dir)
    record = hypothesis_deep_research.find_hypothesis(
        kb_dir,
        "Long_COVID",
        "canonical_persistence_immune_model",
    )
    monkeypatch.delenv("DISMECH_ENABLE_BIOMNI", raising=False)

    def fail_if_called(*args, **kwargs):
        raise AssertionError("disabled Biomni must not launch a subprocess")

    monkeypatch.setattr(hypothesis_deep_research.subprocess, "run", fail_if_called)

    result = hypothesis_deep_research.run_record(
        record,
        provider="biomni",
        output_root=output_root,
        template=template,
        extra_args=[],
        timeout_seconds=1,
        dry_run=False,
        overwrite=False,
    )

    assert result.status == "PROVIDER_DISABLED"
    assert result.returncode == 2
    assert "DISMECH_ENABLE_BIOMNI=1" in result.detail
    assert not result.output_file.parent.exists()


def test_other_provider_subprocess_disables_biomni_automatic_fallback(
    tmp_path: Path, monkeypatch
) -> None:
    kb_dir = tmp_path / "kb" / "disorders"
    output_root = tmp_path / "kb" / "hypotheses"
    template = tmp_path / "templates" / "hypothesis.md"
    kb_dir.mkdir(parents=True)
    template.parent.mkdir(parents=True)
    template.write_text("Hypothesis {hypothesis_group_id}\n", encoding="utf-8")
    write_disorder(kb_dir)
    record = hypothesis_deep_research.find_hypothesis(
        kb_dir,
        "Long_COVID",
        "canonical_persistence_immune_model",
    )
    output_file = hypothesis_deep_research.output_file_for(
        record, output_root, "openscientist"
    )
    monkeypatch.delenv("DISMECH_ENABLE_BIOMNI", raising=False)

    def fake_run(command, **kwargs):
        assert kwargs["env"]["DISABLE_BIOMNI_PROVIDER"] == "true"
        output_file.write_text("# Literature report\n", encoding="utf-8")
        return subprocess.CompletedProcess(command, 0, stdout="", stderr="")

    monkeypatch.setattr(hypothesis_deep_research.subprocess, "run", fake_run)

    result = hypothesis_deep_research.run_record(
        record,
        provider="openscientist",
        output_root=output_root,
        template=template,
        extra_args=["--fallback"],
        timeout_seconds=1,
        dry_run=False,
        overwrite=False,
    )

    assert result.status == "OK"


def test_named_biomni_fallback_requires_opt_in(tmp_path: Path, monkeypatch) -> None:
    kb_dir = tmp_path / "kb" / "disorders"
    output_root = tmp_path / "kb" / "hypotheses"
    template = tmp_path / "templates" / "hypothesis.md"
    kb_dir.mkdir(parents=True)
    template.parent.mkdir(parents=True)
    template.write_text("Hypothesis {hypothesis_group_id}\n", encoding="utf-8")
    write_disorder(kb_dir)
    record = hypothesis_deep_research.find_hypothesis(
        kb_dir,
        "Long_COVID",
        "canonical_persistence_immune_model",
    )
    monkeypatch.delenv("DISMECH_ENABLE_BIOMNI", raising=False)

    def fail_if_called(*args, **kwargs):
        raise AssertionError("a disabled named Biomni fallback must not launch")

    monkeypatch.setattr(hypothesis_deep_research.subprocess, "run", fail_if_called)

    result = hypothesis_deep_research.run_record(
        record,
        provider="openscientist",
        output_root=output_root,
        template=template,
        extra_args=["--fallback-provider", "biomni"],
        timeout_seconds=1,
        dry_run=False,
        overwrite=False,
    )

    assert result.status == "PROVIDER_DISABLED"
    assert "DISMECH_ENABLE_BIOMNI=1" in result.detail
    assert not result.output_file.parent.exists()


def test_run_record_does_not_skip_invalid_existing_analysis(
    tmp_path: Path, monkeypatch
) -> None:
    kb_dir = tmp_path / "kb" / "disorders"
    output_root = tmp_path / "kb" / "hypotheses"
    template = tmp_path / "templates" / "dataset.md"
    kb_dir.mkdir(parents=True)
    template.parent.mkdir(parents=True)
    template.write_text(
        "---\nanalysis_contract: required\n---\nRun the dataset analysis.\n",
        encoding="utf-8",
    )
    write_disorder(kb_dir)
    record = hypothesis_deep_research.find_hypothesis(
        kb_dir,
        "Long_COVID",
        "canonical_persistence_immune_model",
    )
    output_file = hypothesis_deep_research.output_file_for(
        record, output_root, "biomni"
    )
    output_file.parent.mkdir(parents=True)
    output_file.write_text("# Proposed analysis only\n", encoding="utf-8")
    monkeypatch.setenv("DISMECH_ENABLE_BIOMNI", "1")

    result = hypothesis_deep_research.run_record(
        record,
        provider="biomni",
        output_root=output_root,
        template=template,
        extra_args=[],
        timeout_seconds=1,
        dry_run=False,
        overwrite=False,
    )

    assert result.status == "INVALID_ANALYSIS_RUN"
    assert "requires an exact ANALYSIS_STATUS marker" in result.detail


def test_overwrite_quarantines_stale_artifacts_before_provider_run(
    tmp_path: Path, monkeypatch
) -> None:
    kb_dir = tmp_path / "kb" / "disorders"
    output_root = tmp_path / "kb" / "hypotheses"
    template = tmp_path / "templates" / "literature.md"
    kb_dir.mkdir(parents=True)
    template.parent.mkdir(parents=True)
    template.write_text("Write a literature report.\n", encoding="utf-8")
    write_disorder(kb_dir)
    record = hypothesis_deep_research.find_hypothesis(
        kb_dir,
        "Long_COVID",
        "canonical_persistence_immune_model",
    )
    output_file = hypothesis_deep_research.output_file_for(
        record, output_root, "biomni"
    )
    artifact_dir = output_file.parent / "biomni_artifacts"
    artifact_dir.mkdir(parents=True)
    (artifact_dir / "stale.tsv").write_text("old\n", encoding="utf-8")
    output_file.write_text("old report\n", encoding="utf-8")
    backup_root = tmp_path / "backup-root"
    monkeypatch.setenv("DISMECH_ENABLE_BIOMNI", "1")

    def fake_mkdtemp(*, prefix: str) -> str:
        assert prefix.startswith("biomni_artifacts-pre-overwrite-")
        backup_root.mkdir()
        return str(backup_root)

    def fake_run(command, **kwargs):
        assert not artifact_dir.exists()
        assert (backup_root / "biomni_artifacts" / "stale.tsv").exists()
        assert "DISABLE_BIOMNI_PROVIDER" not in kwargs["env"]
        output_file.write_text("# Replacement literature report\n", encoding="utf-8")
        return subprocess.CompletedProcess(command, 0, stdout="", stderr="")

    monkeypatch.setattr(hypothesis_deep_research.tempfile, "mkdtemp", fake_mkdtemp)
    monkeypatch.setattr(hypothesis_deep_research.subprocess, "run", fake_run)

    result = hypothesis_deep_research.run_record(
        record,
        provider="biomni",
        output_root=output_root,
        template=template,
        extra_args=[],
        timeout_seconds=1,
        dry_run=False,
        overwrite=True,
    )

    assert result.status == "OK"
    assert not backup_root.exists()
    assert not artifact_dir.exists()


def test_a_fallback_report_is_renamed_on_a_successful_run(
    monkeypatch, tmp_path: Path
) -> None:
    result = _run_with(monkeypatch, tmp_path, 0)

    assert result.status == "OK"
    assert result.provider == "claude_code"
    assert result.output_file.name == "claude_code.md"
    assert result.output_file.exists()


def test_a_fallback_report_is_renamed_when_validation_failed(
    monkeypatch, tmp_path: Path
) -> None:
    """Exit 3 means validation failed, not that the report is missing.

    Aligning only on a zero exit would leave that report named for the provider
    that could not run, and `existing_outputs` reads the provider straight out
    of the filename.
    """
    result = _run_with(monkeypatch, tmp_path, 3)

    assert result.status == "ERROR_3", "the validation failure must still be reported"
    assert result.provider == "claude_code"
    assert result.output_file.name == "claude_code.md"
    assert result.output_file.exists()
    assert not (result.output_file.parent / "falcon.md").exists()


def test_analysis_contract_status_rejects_explicit_failure(tmp_path: Path) -> None:
    report = tmp_path / "biomni.md"
    report.write_text("ANALYSIS_STATUS: FAILED\n", encoding="utf-8")

    status, detail = hypothesis_deep_research.analysis_contract_status(
        report, tmp_path / "biomni_artifacts"
    )

    assert status == "ANALYSIS_FAILED"
    assert "explicitly reported" in detail


def test_analysis_contract_status_gates_claimed_success(tmp_path: Path) -> None:
    report = tmp_path / "biomni.md"
    report.write_text(
        "---\nprovider: biomni\n---\n\n## Output\n\nANALYSIS_STATUS: SUCCEEDED\n",
        encoding="utf-8",
    )

    status, detail = hypothesis_deep_research.analysis_contract_status(
        report, tmp_path / "biomni_artifacts"
    )

    assert status == "INVALID_ANALYSIS_RUN"
    assert "artifact_manifest_sha256" in detail


def test_analysis_contract_status_ignores_ordinary_literature_report(
    tmp_path: Path,
) -> None:
    report = tmp_path / "openscientist.md"
    report.write_text("# Literature report\n", encoding="utf-8")

    status, detail = hypothesis_deep_research.analysis_contract_status(
        report, tmp_path / "openscientist_artifacts"
    )

    assert status is None
    assert detail == ""


def test_analysis_contract_status_requires_marker_for_analysis_template(
    tmp_path: Path,
) -> None:
    report = tmp_path / "biomni.md"
    report.write_text("# Proposed analysis without execution\n", encoding="utf-8")

    status, detail = hypothesis_deep_research.analysis_contract_status(
        report,
        tmp_path / "biomni_artifacts",
        required=True,
    )

    assert status == "INVALID_ANALYSIS_RUN"
    assert "requires an exact ANALYSIS_STATUS marker" in detail


def test_dataset_template_opts_into_analysis_contract(tmp_path: Path) -> None:
    template = tmp_path / "dataset.md"
    template.write_text(
        "---\nanalysis_contract: required\n---\nRun the dataset analysis.\n",
        encoding="utf-8",
    )
    literature_template = tmp_path / "literature.md"
    literature_template.write_text("Write a literature review.\n", encoding="utf-8")

    assert hypothesis_deep_research.template_requires_analysis_contract(template)
    assert not hypothesis_deep_research.template_requires_analysis_contract(
        literature_template
    )


def test_existing_output_completeness_honors_analysis_contract(tmp_path: Path) -> None:
    report = tmp_path / "biomni.md"
    report.write_text("# Literature-only fallback\n", encoding="utf-8")
    output = hypothesis_deep_research.ExistingHypothesisOutput(
        provider="biomni",
        path=report,
        citations_path=tmp_path / "biomni.md.citations.md",
        citations_exists=False,
        artifact_dir=tmp_path / "biomni_artifacts",
        artifact_exists=False,
    )

    assert hypothesis_deep_research.existing_output_is_complete(
        output, analysis_contract_required=False
    )
    assert not hypothesis_deep_research.existing_output_is_complete(
        output, analysis_contract_required=True
    )


def _dataset_record(tmp_path: Path):
    kb_dir = tmp_path / "kb" / "disorders"
    kb_dir.mkdir(parents=True)
    write_disorder(kb_dir)
    return hypothesis_deep_research.find_hypothesis(
        kb_dir, "Long_COVID", "canonical_persistence_immune_model"
    )


DATASET_VARS = {
    "dataset_inputs": "geo:GSE1",
    "target_variables": "FDX1",
    "analysis_objective": "Compare case with control.",
}


def test_output_root_outside_repo_still_gives_provider_a_relative_artifact_dir(
    tmp_path: Path,
) -> None:
    """An absolute --output-root must not send the bundle outside the job workspace."""
    record = _dataset_record(tmp_path)
    repo_root = tmp_path / "repo"
    repo_root.mkdir()
    output_root = tmp_path / "elsewhere"

    result = hypothesis_deep_research.run_record(
        record,
        provider="openscientist",
        output_root=output_root,
        template=ROOT / "templates" / "hypothesis_dataset_analysis.md",
        extra_args=[],
        timeout_seconds=1,
        dry_run=True,
        overwrite=False,
        template_overrides=DATASET_VARS,
        repo_root=repo_root,
    )

    assert result.status == "DRY_RUN"
    assert result.output_file == (
        output_root
        / "Long_COVID"
        / "canonical_persistence_immune_model"
        / "openscientist.md"
    )
    [artifact_var] = [arg for arg in result.command if arg.startswith("artifact_dir=")]
    assert artifact_var == (
        "artifact_dir=Long_COVID/canonical_persistence_immune_model/"
        "openscientist_artifacts"
    )


def test_run_label_names_a_second_report_beside_the_first(tmp_path: Path) -> None:
    record = _dataset_record(tmp_path)
    output_root = tmp_path / "kb" / "hypotheses"
    literature = hypothesis_deep_research.output_file_for(
        record, output_root, "openscientist"
    )
    literature.parent.mkdir(parents=True)
    literature.write_text("# Literature report\n", encoding="utf-8")

    result = hypothesis_deep_research.run_record(
        record,
        provider="openscientist",
        output_root=output_root,
        template=ROOT / "templates" / "hypothesis_dataset_analysis.md",
        extra_args=[],
        timeout_seconds=1,
        dry_run=True,
        overwrite=False,
        template_overrides=DATASET_VARS,
        run_label="dataset",
        repo_root=tmp_path,
    )

    assert result.status == "DRY_RUN"
    assert result.output_file == literature.parent / "openscientist-dataset.md"
    assert (
        "artifact_dir=kb/hypotheses/Long_COVID/canonical_persistence_immune_model/"
        "openscientist-dataset_artifacts"
    ) in result.command
    assert "-v" in result.command[: result.command.index("research")]
    assert literature.read_text(encoding="utf-8") == "# Literature report\n"


def test_cli_rejects_malformed_run_label(tmp_path: Path, capsys) -> None:
    exit_code = hypothesis_deep_research.main(
        [
            "run",
            "openscientist",
            "Long_COVID",
            "canonical_persistence_immune_model",
            "--run-label",
            "Dataset Run",
            "--kb-dir",
            str(tmp_path),
            "--dry-run",
        ]
    )
    assert exit_code == 2
    assert "run label" in capsys.readouterr().err


def _zip(members: dict[str, bytes]) -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as archive:
        for name, content in members.items():
            archive.writestr(name, content)
    return buffer.getvalue()


def test_restore_artifact_subtree_copies_provider_bytes_at_their_paths(
    tmp_path: Path,
) -> None:
    provider_dir = Path("kb/hypotheses/D/h/openscientist_artifacts")
    manifest = b"schema_version: '1.0'\ninputs:\n- local_path: raw/GSE1.txt\n"
    bundle = _zip(
        {
            "workspace/kb/hypotheses/D/h/openscientist_artifacts/MANIFEST.yaml": manifest,
            "workspace/kb/hypotheses/D/h/openscientist_artifacts/raw/GSE1.txt": b"x",
            "workspace/kb/hypotheses/D/h/openscientist_artifacts/replay/samples.csv": (
                b"a,b\n"
            ),
            "workspace/final_report.md": b"# report",
        }
    )
    artifact_dir = tmp_path / "openscientist_artifacts"
    artifact_dir.mkdir()
    (artifact_dir / "figure.png").write_bytes(b"png")
    (artifact_dir / "MANIFEST.yaml").write_bytes(b"flattened copy")

    problem = hypothesis_deep_research.restore_artifact_subtree(
        bundle, provider_dir, artifact_dir
    )

    assert problem == ""
    assert (artifact_dir / "MANIFEST.yaml").read_bytes() == manifest
    assert (artifact_dir / "raw" / "GSE1.txt").read_bytes() == b"x"
    assert (artifact_dir / "replay" / "samples.csv").read_bytes() == b"a,b\n"
    assert (artifact_dir / "figure.png").read_bytes() == b"png"
    assert not (artifact_dir / "final_report.md").exists()
    assert not list(tmp_path.glob(".openscientist_artifacts-*"))


def test_restore_artifact_subtree_refuses_missing_or_ambiguous_trees(
    tmp_path: Path,
) -> None:
    provider_dir = Path("p_artifacts")
    artifact_dir = tmp_path / "p_artifacts"

    missing = hypothesis_deep_research.restore_artifact_subtree(
        _zip({"final_report.md": b"#"}), provider_dir, artifact_dir
    )
    ambiguous = hypothesis_deep_research.restore_artifact_subtree(
        _zip(
            {"a/p_artifacts/MANIFEST.yaml": b"1", "b/p_artifacts/MANIFEST.yaml": b"2"}
        ),
        provider_dir,
        artifact_dir,
    )

    assert "contain no" in missing
    assert "several prefixes" in ambiguous
    assert not artifact_dir.exists()


def test_openscientist_dataset_run_records_job_and_restores_bundle(
    tmp_path: Path, monkeypatch
) -> None:
    """The job ID reaches the report and the job's own manifest reaches the gate."""
    record = _dataset_record(tmp_path)
    output_root = tmp_path / "kb" / "hypotheses"
    output_file = hypothesis_deep_research.output_file_for(
        record, output_root, "openscientist", "dataset"
    )
    manifest = b"schema_version: '1.0'\nstatus: SUCCEEDED\n"
    fetched: list[str] = []

    def fake_run(command, **kwargs):
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(
            "---\nprovider: openscientist\n---\n\n## Output\n\n"
            "ANALYSIS_STATUS: SUCCEEDED\n",
            encoding="utf-8",
        )
        return subprocess.CompletedProcess(
            command,
            0,
            stdout="",
            stderr="INFO - OpenScientist job submitted: 19cc0c3f-fbd2\n",
        )

    def fake_fetch(job_id: str) -> bytes:
        fetched.append(job_id)
        return _zip(
            {
                "kb/hypotheses/Long_COVID/canonical_persistence_immune_model/"
                "openscientist-dataset_artifacts/MANIFEST.yaml": manifest
            }
        )

    monkeypatch.setattr(hypothesis_deep_research.subprocess, "run", fake_run)
    monkeypatch.chdir(tmp_path)

    result = hypothesis_deep_research.run_record(
        record,
        provider="openscientist",
        output_root=Path("kb/hypotheses"),
        template=ROOT / "templates" / "hypothesis_dataset_analysis.md",
        extra_args=[],
        timeout_seconds=1,
        dry_run=False,
        overwrite=False,
        template_overrides=DATASET_VARS,
        run_label="dataset",
        fetch_openscientist_artifacts=fake_fetch,
    )

    assert fetched == ["19cc0c3f-fbd2"]
    assert "over 2097152 bytes" not in result.detail
    assert "openscientist_job_id=19cc0c3f-fbd2" in result.detail
    metadata = hypothesis_deep_research.read_report_frontmatter(output_file)
    assert metadata["openscientist_job_id"] == "19cc0c3f-fbd2"
    assert metadata["artifact_manifest_sha256"] == (
        f"sha256:{hashlib.sha256(manifest).hexdigest()}"
    )
    # The restored manifest is deliberately incomplete, so the gate still
    # rejects it -- on its content, not because the manifest is missing.
    assert result.status == "INVALID_ANALYSIS_RUN"
    assert result.detail.startswith("manifest provider is required")


def test_runner_flags_oversized_committable_artifacts(tmp_path: Path, monkeypatch):
    """A file too large to commit is named in the run detail, raw/ excepted."""
    record = _dataset_record(tmp_path)
    output_file = hypothesis_deep_research.output_file_for(
        record, Path("kb/hypotheses"), "openscientist"
    )
    limit = hypothesis_deep_research.MAX_COMMITTED_ARTIFACT_BYTES
    prefix = (
        "kb/hypotheses/Long_COVID/canonical_persistence_immune_model/"
        "openscientist_artifacts/"
    )

    def fake_run(command, **kwargs):
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(
            "---\nprovider: openscientist\n---\n\n## Output\n\n"
            "ANALYSIS_STATUS: FAILED\n",
            encoding="utf-8",
        )
        return subprocess.CompletedProcess(
            command, 0, stdout="", stderr="OpenScientist job submitted: job-1\n"
        )

    def fake_fetch(job_id: str) -> bytes:
        return _zip(
            {
                prefix + "MANIFEST.yaml": b"status: FAILED\n",
                prefix + "all_probes.tsv": b"0" * (limit + 1),
                prefix + "raw/matrix.gz": b"0" * (limit + 1),
            }
        )

    monkeypatch.setattr(hypothesis_deep_research.subprocess, "run", fake_run)
    monkeypatch.chdir(tmp_path)
    result = hypothesis_deep_research.run_record(
        record,
        provider="openscientist",
        output_root=Path("kb/hypotheses"),
        template=ROOT / "templates" / "hypothesis_dataset_analysis.md",
        extra_args=[],
        timeout_seconds=1,
        dry_run=False,
        overwrite=False,
        template_overrides=DATASET_VARS,
        fetch_openscientist_artifacts=fake_fetch,
    )

    assert result.status == "ANALYSIS_FAILED"
    assert f"all_probes.tsv ({limit + 1} bytes)" in result.detail
    assert "matrix.gz" not in result.detail
