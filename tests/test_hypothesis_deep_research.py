"""Tests for mechanistic hypothesis deep-research helpers."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

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
