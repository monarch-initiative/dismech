"""Tests for the computational hypothesis-analysis run hard gate."""

from __future__ import annotations

import hashlib
from copy import deepcopy
from pathlib import Path

import yaml

from dismech.hypothesis_analysis_run import iter_analysis_run_problems, main


def _record(path: Path, role: str) -> dict:
    content = path.read_bytes()
    return {
        "path": path.name,
        "role": role,
        "byte_count": len(content),
        "sha256": hashlib.sha256(content).hexdigest(),
    }


def _write_manifest(path: Path, data: dict) -> None:
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    report = path.parent.parent / f"{path.parent.name.removesuffix('_artifacts')}.md"
    if not report.is_file():
        return
    report_lines = report.read_text(encoding="utf-8").splitlines()
    if not report_lines or report_lines[0] != "---":
        return
    report_lines = [
        line
        for line in report_lines
        if not line.startswith("artifact_manifest_sha256:")
    ]
    frontmatter_end = report_lines.index("---", 1)
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    report_lines.insert(frontmatter_end, f"artifact_manifest_sha256: sha256:{digest}")
    report.write_text("\n".join(report_lines) + "\n", encoding="utf-8")


def _fixture(tmp_path: Path) -> tuple[Path, Path, dict]:
    report = tmp_path / "biomni.md"
    report.write_text(
        "---\n"
        "provider: biomni\n"
        "start_time: '2026-08-29T00:00:00Z'\n"
        "end_time: '2026-08-29T00:01:00Z'\n"
        "---\n\n"
        "## Question\n\nRun the analysis.\n\n"
        "## Output\n\n"
        "ANALYSIS_STATUS: SUCCEEDED\n\n"
        "Results follow.\n",
        encoding="utf-8",
    )
    artifacts = tmp_path / "biomni_artifacts"
    artifacts.mkdir()
    source = artifacts / "input.json"
    code = artifacts / "analysis.py"
    environment = artifacts / "environment.txt"
    result = artifacts / "results.csv"
    replay_dir = artifacts / "replay"
    replay_dir.mkdir()
    replay_result = replay_dir / "results.csv"
    source.write_text('{"accession": "GSE1"}\n', encoding="utf-8")
    code.write_text("print('analysis')\n", encoding="utf-8")
    environment.write_text("python==3.12\n", encoding="utf-8")
    result.write_text("gene,log2fc\nFDX1,-0.2\n", encoding="utf-8")
    replay_result.write_bytes(result.read_bytes())
    source_bytes = source.read_bytes()
    manifest = {
        "schema_version": "1.0",
        "status": "SUCCEEDED",
        "provider": "biomni",
        "fallback_used": False,
        "direct_analysis_completed": True,
        "inputs": [
            {
                "identifier": "geo:GSE1",
                "canonical_url": "https://example.org/data?acc=GSE1",
                "retrieved_at": "2026-08-29T00:00:00Z",
                "byte_count": len(source_bytes),
                "sha256": hashlib.sha256(source_bytes).hexdigest(),
                "local_path": "input.json",
            }
        ],
        "outputs": [
            _record(code, "CODE"),
            _record(environment, "ENVIRONMENT"),
            _record(result, "TABULAR_RESULT"),
        ],
        "replay": {
            "command": "python analysis.py --output-dir replay",
            "verified": True,
            "byte_identity": {"results.csv": True},
            "assets": [
                {
                    "path": "replay/results.csv",
                    "role": "REPLAY_RESULTS",
                    "byte_count": replay_result.stat().st_size,
                    "sha256": hashlib.sha256(replay_result.read_bytes()).hexdigest(),
                }
            ],
        },
    }
    _write_manifest(artifacts / "MANIFEST.yaml", manifest)
    return report, artifacts, manifest


def _problems(report: Path, artifacts: Path) -> list[str]:
    return list(iter_analysis_run_problems(report, artifacts))


def test_valid_bundle_and_exact_status_marker_pass(tmp_path, capsys):
    report, artifacts, _manifest = _fixture(tmp_path)

    assert _problems(report, artifacts) == []
    assert main([str(report), str(artifacts)]) == 0
    assert "passed the hard gate" in capsys.readouterr().out


def test_report_requires_artifact_manifest_checksum(tmp_path):
    report, artifacts, _manifest = _fixture(tmp_path)
    report.write_text(
        "\n".join(
            line
            for line in report.read_text(encoding="utf-8").splitlines()
            if not line.startswith("artifact_manifest_sha256:")
        )
        + "\n",
        encoding="utf-8",
    )

    assert any(
        "requires artifact_manifest_sha256" in problem
        for problem in _problems(report, artifacts)
    )


def test_stale_artifact_manifest_checksum_fails(tmp_path):
    report, artifacts, _manifest = _fixture(tmp_path)
    with (artifacts / "MANIFEST.yaml").open("a", encoding="utf-8") as stream:
        stream.write("# manifest bytes changed after report generation\n")

    assert any(
        "does not match MANIFEST.yaml bytes" in problem
        for problem in _problems(report, artifacts)
    )


def test_artifact_manifest_checksum_requires_prefixed_lowercase_sha256(tmp_path):
    report, artifacts, _manifest = _fixture(tmp_path)
    report.write_text(
        report.read_text(encoding="utf-8").replace(
            "artifact_manifest_sha256: sha256:",
            "artifact_manifest_sha256: SHA256:",
        ),
        encoding="utf-8",
    )

    assert any(
        "requires artifact_manifest_sha256" in problem
        for problem in _problems(report, artifacts)
    )


def test_status_marker_must_be_an_exact_line(tmp_path):
    report, artifacts, _manifest = _fixture(tmp_path)
    report.write_text("  ANALYSIS_STATUS: SUCCEEDED  \n", encoding="utf-8")

    assert any("exact line" in problem for problem in _problems(report, artifacts))


def test_successful_report_must_not_also_claim_failure(tmp_path):
    report, artifacts, _manifest = _fixture(tmp_path)
    with report.open("a", encoding="utf-8") as stream:
        stream.write("\nANALYSIS_STATUS: FAILED\n")

    assert any(
        "must not contain" in problem for problem in _problems(report, artifacts)
    )


def test_plain_log_cannot_masquerade_as_provider_report(tmp_path):
    report, artifacts, _manifest = _fixture(tmp_path)
    report.write_text(
        "some agent log\n## Output\nANALYSIS_STATUS: SUCCEEDED\n",
        encoding="utf-8",
    )

    assert any(
        "YAML frontmatter" in problem for problem in _problems(report, artifacts)
    )


def test_marker_must_be_in_output_and_provider_must_match(tmp_path):
    report, artifacts, manifest = _fixture(tmp_path)
    report.write_text(
        "---\nprovider: openscientist\n---\n"
        "ANALYSIS_STATUS: SUCCEEDED\n"
        "## Output\nResults only.\n",
        encoding="utf-8",
    )
    manifest["provider"] = "biomni"
    _write_manifest(artifacts / "MANIFEST.yaml", manifest)

    problems = _problems(report, artifacts)
    assert any("inside the report's ## Output" in problem for problem in problems)
    assert any("does not match report provider" in problem for problem in problems)


def test_fallback_or_incomplete_direct_analysis_fails(tmp_path):
    report, artifacts, manifest = _fixture(tmp_path)
    manifest["fallback_used"] = True
    manifest["direct_analysis_completed"] = False
    _write_manifest(artifacts / "MANIFEST.yaml", manifest)

    problems = _problems(report, artifacts)
    assert "fallback_used must be false" in problems
    assert "direct_analysis_completed must be true" in problems


def test_absolute_and_escaping_paths_fail(tmp_path):
    report, artifacts, manifest = _fixture(tmp_path)
    manifest["inputs"][0]["local_path"] = str(artifacts / "input.json")
    manifest["outputs"][0]["path"] = "../outside.py"
    _write_manifest(artifacts / "MANIFEST.yaml", manifest)

    problems = _problems(report, artifacts)
    assert any("must be relative, not absolute" in problem for problem in problems)
    assert any("escapes the artifact directory" in problem for problem in problems)


def test_missing_empty_size_and_checksum_mismatches_fail(tmp_path):
    report, artifacts, manifest = _fixture(tmp_path)
    (artifacts / "analysis.py").unlink()
    (artifacts / "environment.txt").write_text("", encoding="utf-8")
    manifest["outputs"][1]["byte_count"] = 1
    manifest["outputs"][2]["byte_count"] += 1
    manifest["outputs"][2]["sha256"] = "0" * 64
    _write_manifest(artifacts / "MANIFEST.yaml", manifest)

    problems = _problems(report, artifacts)
    assert any("outputs[0].path does not exist" in problem for problem in problems)
    assert any("outputs[1].path is empty" in problem for problem in problems)
    assert any("outputs[1].path byte_count mismatch" in problem for problem in problems)
    assert any("outputs[2].path byte_count mismatch" in problem for problem in problems)
    assert any("outputs[2].path sha256 mismatch" in problem for problem in problems)


def test_sha256_must_be_lowercase(tmp_path):
    report, artifacts, manifest = _fixture(tmp_path)
    manifest["outputs"][0]["sha256"] = manifest["outputs"][0]["sha256"].upper()
    _write_manifest(artifacts / "MANIFEST.yaml", manifest)

    assert any(
        "lowercase hexadecimal" in problem for problem in _problems(report, artifacts)
    )


def test_missing_manifest_and_empty_manifest_fail(tmp_path):
    report, artifacts, _manifest = _fixture(tmp_path)
    manifest_path = artifacts / "MANIFEST.yaml"
    manifest_path.unlink()
    assert "artifact directory must contain MANIFEST.yaml" in _problems(
        report, artifacts
    )

    manifest_path.write_text("", encoding="utf-8")
    assert "MANIFEST.yaml is empty" in _problems(report, artifacts)


def test_required_artifact_roles_must_all_be_present(tmp_path):
    report, artifacts, manifest = _fixture(tmp_path)
    manifest["outputs"] = [
        output for output in manifest["outputs"] if output["role"] != "ENVIRONMENT"
    ]
    _write_manifest(artifacts / "MANIFEST.yaml", manifest)

    assert any(
        "missing required role(s): ENVIRONMENT" in problem
        for problem in _problems(report, artifacts)
    )


def test_replay_must_be_verified_and_byte_identical(tmp_path):
    report, artifacts, manifest = _fixture(tmp_path)
    manifest["replay"]["verified"] = False
    manifest["replay"]["byte_identity"] = {"results.csv": False}
    _write_manifest(artifacts / "MANIFEST.yaml", manifest)

    problems = _problems(report, artifacts)
    assert "replay.verified must be true" in problems
    assert any(
        "replay.byte_identity" in problem and "must be true" in problem
        for problem in problems
    )


def test_replay_requires_coverage_files_and_actual_byte_identity(tmp_path):
    report, artifacts, manifest = _fixture(tmp_path)
    manifest["replay"]["byte_identity"] = {"analysis.py": True}
    (artifacts / "replay" / "results.csv").write_text(
        "gene,log2fc\nFDX1,99\n", encoding="utf-8"
    )
    replay_asset = manifest["replay"]["assets"][0]
    replay_bytes = (artifacts / "replay" / "results.csv").read_bytes()
    replay_asset["byte_count"] = len(replay_bytes)
    replay_asset["sha256"] = hashlib.sha256(replay_bytes).hexdigest()
    _write_manifest(artifacts / "MANIFEST.yaml", manifest)

    problems = _problems(report, artifacts)
    assert any(
        "missing TABULAR_RESULT 'results.csv'" in problem for problem in problems
    )
    assert any(
        "non-TABULAR_RESULT path 'analysis.py'" in problem for problem in problems
    )
    assert any("not byte-identical" in problem for problem in problems)


def test_report_and_artifacts_must_be_canonical_siblings(tmp_path):
    report, artifacts, _manifest = _fixture(tmp_path)
    wrong_artifacts = tmp_path / "artifacts"
    artifacts.rename(wrong_artifacts)

    assert any(
        "canonical sibling" in problem for problem in _problems(report, wrong_artifacts)
    )


def test_duplicate_reserved_and_undeclared_replay_paths_fail(tmp_path):
    report, artifacts, manifest = _fixture(tmp_path)
    reserved = artifacts / "raw"
    reserved.mkdir()
    reserved_result = reserved / "results.csv"
    reserved_result.write_text("gene,value\nFDX1,1\n", encoding="utf-8")
    manifest["outputs"][0]["path"] = "input.json"
    manifest["outputs"][0]["byte_count"] = manifest["inputs"][0]["byte_count"]
    manifest["outputs"][0]["sha256"] = manifest["inputs"][0]["sha256"]
    manifest["outputs"][2] = {
        **_record(reserved_result, "TABULAR_RESULT"),
        "path": "raw/results.csv",
    }
    manifest["replay"]["byte_identity"] = {"not-declared.csv": True}
    _write_manifest(artifacts / "MANIFEST.yaml", manifest)

    problems = _problems(report, artifacts)
    assert any("duplicates declared path" in problem for problem in problems)
    assert any("reserved output directory" in problem for problem in problems)
    assert any("must name a declared output path" in problem for problem in problems)


def test_sensitive_source_urls_fail(tmp_path):
    report, artifacts, manifest = _fixture(tmp_path)
    source = deepcopy(manifest["inputs"][0])
    source.pop("local_path")
    source["identifier"] = "private:1"
    source["canonical_url"] = "https://user:password@example.org/data?api_key=x"
    manifest["inputs"].append(source)
    _write_manifest(artifacts / "MANIFEST.yaml", manifest)

    problems = _problems(report, artifacts)
    assert any("userinfo or credentials" in problem for problem in problems)
    assert any("sensitive query key 'api_key'" in problem for problem in problems)
