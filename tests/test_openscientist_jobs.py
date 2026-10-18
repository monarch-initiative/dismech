"""Tests for recovering OpenScientist jobs by ID (dismech#13616, #12908, #11254)."""

from __future__ import annotations

import importlib.util
import io
import sys
import zipfile
from pathlib import Path

import httpx
import yaml

from dismech import openscientist_jobs as jobs_module
from dismech.openscientist_jobs import (
    OpenScientistJobs,
    extract_artifact_subtree,
    extract_job_id,
    find_report_markdown,
    read_job_record,
    remove_flattened_duplicates,
    write_job_record,
)

SCRIPT_PATH = (
    Path(__file__).resolve().parents[1] / "scripts" / "hypothesis_deep_research.py"
)
SPEC = importlib.util.spec_from_file_location("hypothesis_deep_research", SCRIPT_PATH)
assert SPEC is not None and SPEC.loader is not None
hdr = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = hdr
SPEC.loader.exec_module(hdr)

JOB_ID = "2ffdfa0c-8377-4d31-8642-2f4671d5b07a"
RUN_DIR = "kb/hypotheses/Long_COVID/canonical_persistence_immune_model/openscientist_artifacts"


def make_bundle(members: dict[str, bytes]) -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as archive:
        for name, data in members.items():
            archive.writestr(name, data)
    return buffer.getvalue()


def sample_bundle(report: str = "ANALYSIS_STATUS: FAILED\n\n# Report\n") -> bytes:
    return make_bundle(
        {
            "final_report.md": report.encode(),
            "final_report.pdf": b"%PDF-1.4",
            ".claude/skills/huge-skill.md": b"x" * 5000,
            f"{RUN_DIR}/MANIFEST.yaml": b"schema_version: '1.0'\nstatus: FAILED\n",
            f"{RUN_DIR}/analysis.py": b"print('hi')\n",
            f"{RUN_DIR}/environment.txt": b"python 3.10\n",
            f"{RUN_DIR}/results/runs.csv": b"a,b\n1,2\n",
            f"{RUN_DIR}/raw/frame.pkl": b"\x00\x01",
            f"{RUN_DIR}/../../../escape.txt": b"nope",
            "other/unrelated.csv": b"x\n",
        }
    )


def write_disorder(kb_dir: Path) -> None:
    kb_dir.mkdir(parents=True, exist_ok=True)
    (kb_dir / "Long_COVID.yaml").write_text(
        yaml.safe_dump(
            {
                "name": "Long COVID",
                "category": "Complex",
                "mechanistic_hypotheses": [
                    {
                        "hypothesis_group_id": "canonical_persistence_immune_model",
                        "hypothesis_label": "Persistence model",
                        "status": "CANONICAL",
                    }
                ],
            }
        ),
        encoding="utf-8",
    )


def test_extract_job_id_reads_the_client_info_log() -> None:
    log = f"INFO - Health check ok\nINFO - OpenScientist job submitted: {JOB_ID.upper()}\n"
    assert extract_job_id(log) == JOB_ID
    assert extract_job_id("INFO - nothing here") is None
    assert extract_job_id(None) is None


def test_job_record_round_trips_beside_the_report(tmp_path: Path) -> None:
    report = tmp_path / "openscientist.md"
    path = write_job_record(report, provider="openscientist", job_id=JOB_ID)
    assert path == tmp_path / "openscientist.md.job.yaml"
    record = read_job_record(report)
    assert record is not None and record["job_id"] == JOB_ID
    assert read_job_record(tmp_path / "missing.md") is None


def test_extract_artifact_subtree_keeps_every_extension_and_canonical_paths(
    tmp_path: Path,
) -> None:
    bundle = tmp_path / "bundle.zip"
    bundle.write_bytes(sample_bundle())
    # A different local output root still matches on <disease>/<hypothesis>/<artifacts>.
    artifact_dir = (
        tmp_path / "out" / "Long_COVID" / "canonical_persistence_immune_model"
    )
    artifact_dir = artifact_dir / "openscientist_artifacts"

    written = extract_artifact_subtree(bundle, artifact_dir)

    names = sorted(path.relative_to(artifact_dir).as_posix() for path in written)
    assert names == [
        "MANIFEST.yaml",
        "analysis.py",
        "environment.txt",
        "raw/frame.pkl",
        "results/runs.csv",
    ]
    assert not (tmp_path / "escape.txt").exists()
    assert not any(path.name == "unrelated.csv" for path in tmp_path.rglob("*"))


def test_remove_flattened_duplicates_only_drops_identical_copies(
    tmp_path: Path,
) -> None:
    artifact_dir = Path(RUN_DIR)
    root = tmp_path / artifact_dir
    (root / "results").mkdir(parents=True)
    (root / "results" / "runs.csv").write_text("a\n")
    (root / "notes.md").write_text("canonical\n")
    prefix = RUN_DIR.replace("/", "_") + "_"
    (root / f"{prefix}results_runs.csv").write_text("a\n")
    (root / f"{prefix}notes.md").write_text("different\n")

    # The helper works on the path as the runner passes it (relative to the repo).
    original = Path.cwd()
    try:
        import os

        os.chdir(tmp_path)
        removed = remove_flattened_duplicates(artifact_dir)
    finally:
        os.chdir(original)

    assert [path.name for path in removed] == [f"{prefix}results_runs.csv"]
    assert (root / f"{prefix}notes.md").exists()


def test_find_report_markdown_prefers_final_report_and_skips_tooling(
    tmp_path: Path,
) -> None:
    bundle = tmp_path / "bundle.zip"
    bundle.write_bytes(sample_bundle("# The report\n"))
    assert find_report_markdown(bundle, Path(RUN_DIR)) == (
        "final_report.md",
        "# The report\n",
    )


def test_download_bundle_retries_a_gateway_timeout(tmp_path: Path) -> None:
    payload = sample_bundle()
    calls: list[int] = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        if len(calls) == 1:
            return httpx.Response(524, text="error code: 524")
        return httpx.Response(200, content=payload)

    client = OpenScientistJobs(
        api_key="k", backoff_seconds=0, transport=httpx.MockTransport(handler)
    )
    path = client.download_bundle(JOB_ID, tmp_path / "bundle.zip")
    assert path.read_bytes() == payload
    assert len(calls) == 2


def test_download_bundle_resumes_a_partial_file(tmp_path: Path) -> None:
    payload = sample_bundle()
    split = len(payload) // 2
    (tmp_path / "bundle.zip.part").write_bytes(payload[:split])
    seen: list[str | None] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request.headers.get("Range"))
        return httpx.Response(206, content=payload[split:])

    client = OpenScientistJobs(
        api_key="k", backoff_seconds=0, transport=httpx.MockTransport(handler)
    )
    path = client.download_bundle(JOB_ID, tmp_path / "bundle.zip")
    assert seen == [f"bytes={split}-"]
    assert path.read_bytes() == payload


def test_download_bundle_gives_up_with_the_last_error(tmp_path: Path) -> None:
    client = OpenScientistJobs(
        api_key="k",
        retries=1,
        backoff_seconds=0,
        transport=httpx.MockTransport(lambda request: httpx.Response(524)),
    )
    try:
        client.download_bundle(JOB_ID, tmp_path / "bundle.zip")
    except RuntimeError as error:
        assert "after 2 attempts" in str(error) and "524" in str(error)
    else:
        raise AssertionError("expected RuntimeError")


def test_build_command_logs_job_id_only_for_openscientist(tmp_path: Path) -> None:
    kb_dir = tmp_path / "kb" / "disorders"
    write_disorder(kb_dir)
    template = tmp_path / "t.md"
    template.write_text("Hypothesis {hypothesis_group_id}\n", encoding="utf-8")
    record = hdr.find_hypothesis(
        kb_dir, "Long_COVID", "canonical_persistence_immune_model"
    )
    os_command = hdr.build_command(
        record,
        provider="openscientist",
        output_root=tmp_path,
        template=template,
        extra_args=[],
    )
    falcon_command = hdr.build_command(
        record,
        provider="falcon",
        output_root=tmp_path,
        template=template,
        extra_args=[],
    )
    assert os_command[3:5] == ["-v", "research"]
    assert falcon_command[3] == "research"


def test_failed_run_records_job_and_names_the_recovery_command(
    tmp_path: Path, monkeypatch
) -> None:
    kb_dir = tmp_path / "kb" / "disorders"
    write_disorder(kb_dir)
    template = tmp_path / "t.md"
    template.write_text("Hypothesis {hypothesis_group_id}\n", encoding="utf-8")
    record = hdr.find_hypothesis(
        kb_dir, "Long_COVID", "canonical_persistence_immune_model"
    )

    def fake_run(command, **kwargs):
        stderr = f"INFO - OpenScientist job submitted: {JOB_ID}\nhttpx.ReadTimeout\n"
        return hdr.subprocess.CompletedProcess(command, 1, stdout="", stderr=stderr)

    monkeypatch.setattr(hdr.subprocess, "run", fake_run)
    result = hdr.run_record(
        record,
        provider="openscientist",
        output_root=tmp_path / "out",
        template=template,
        extra_args=[],
        timeout_seconds=10,
        dry_run=False,
        overwrite=False,
    )
    assert result.status == "ERROR_1"
    assert JOB_ID in result.detail and "fetch openscientist Long_COVID" in result.detail
    assert f"--template {template}" in result.detail
    job_record = read_job_record(result.output_file)
    assert job_record["job_id"] == JOB_ID
    assert job_record["template_file"] == str(template)
    assert len(job_record["template_sha"]) == 40


class FakeJobs:
    """Stands in for the OpenScientist API in fetch tests."""

    def __init__(self, bundle: bytes, status: str = "completed", matches=None):
        self.bundle = bundle
        self.status = status
        self.matches = matches if matches is not None else []
        self.fetched: list[str] = []

    def job(self, job_id: str) -> dict:
        return {
            "id": job_id,
            "status": self.status,
            "created_at": "2026-10-05T23:24:28Z",
            "research_question": "# Hypothesis Test by Simulation",
        }

    def find_jobs(self, *needles: str) -> list[dict]:
        return self.matches

    def download_bundle(self, job_id: str, destination: Path) -> Path:
        self.fetched.append(job_id)
        destination.write_bytes(self.bundle)
        return destination


def _record(tmp_path: Path):
    kb_dir = tmp_path / "kb" / "disorders"
    write_disorder(kb_dir)
    return hdr.find_hypothesis(
        kb_dir, "Long_COVID", "canonical_persistence_immune_model"
    )


def test_fetch_recovers_report_and_artifacts_from_recorded_job(tmp_path: Path) -> None:
    record = _record(tmp_path)
    output_root = tmp_path / "out"
    report = hdr.output_file_for(record, output_root, "openscientist")
    write_job_record(report, provider="openscientist", job_id=JOB_ID)
    jobs = FakeJobs(sample_bundle())

    result = hdr.fetch_record(
        record,
        provider="openscientist",
        output_root=output_root,
        template=Path("templates/hypothesis_dataset_analysis.md"),
        jobs=jobs,
    )

    assert jobs.fetched == [JOB_ID]
    # The provider reported a failed analysis: recovered faithfully, and gated as such.
    assert result.status == "ANALYSIS_FAILED"
    text = report.read_text(encoding="utf-8")
    assert f"job_id: {JOB_ID}" in text and "ANALYSIS_STATUS: FAILED" in text
    artifacts = report.parent / "openscientist_artifacts"
    assert (artifacts / "MANIFEST.yaml").is_file()
    assert (artifacts / "analysis.py").is_file()


def test_fetch_refuses_an_unfinished_job(tmp_path: Path) -> None:
    record = _record(tmp_path)
    result = hdr.fetch_record(
        record,
        provider="openscientist",
        output_root=tmp_path / "out",
        template=Path("templates/hypothesis_dataset_analysis.md"),
        job_id=JOB_ID,
        jobs=FakeJobs(sample_bundle(), status="running"),
    )
    assert result.status == "JOB_RUNNING"
    assert not result.output_file.exists()


def test_fetch_asks_for_a_job_id_when_the_search_is_ambiguous(tmp_path: Path) -> None:
    record = _record(tmp_path)
    matches = [
        {"id": "a", "status": "completed", "created_at": "x"},
        {"id": "b", "status": "failed", "created_at": "y"},
    ]
    result = hdr.fetch_record(
        record,
        provider="openscientist",
        output_root=tmp_path / "out",
        template=Path("templates/hypothesis_dataset_analysis.md"),
        jobs=FakeJobs(sample_bundle(), matches=matches),
    )
    assert result.status == "JOB_NOT_FOUND"
    assert "pass --job-id" in result.detail


def test_fetch_rejects_other_providers(tmp_path: Path) -> None:
    record = _record(tmp_path)
    result = hdr.fetch_record(
        record,
        provider="falcon",
        output_root=tmp_path / "out",
        template=Path("templates/hypothesis_dataset_analysis.md"),
        jobs=FakeJobs(sample_bundle()),
    )
    assert result.status == "UNSUPPORTED_PROVIDER"


def test_module_constants_cover_cloudflare_gateway_timeouts() -> None:
    assert 524 in jobs_module.RETRYABLE_STATUS_CODES


def test_fetched_report_puts_the_response_inside_one_output_section(
    tmp_path: Path,
) -> None:
    record = _record(tmp_path)
    result = hdr.fetch_record(
        record,
        provider="openscientist",
        output_root=tmp_path / "out",
        template=Path("templates/hypothesis_dataset_analysis.md"),
        job_id=JOB_ID,
        jobs=FakeJobs(sample_bundle()),
    )
    lines = result.output_file.read_text(encoding="utf-8").splitlines()
    assert lines.count("## Output") == 1
    assert lines.index("ANALYSIS_STATUS: FAILED") > lines.index("## Output")
    assert lines.index("## Question") < lines.index("# Hypothesis Test by Simulation")
    assert lines.index("# Hypothesis Test by Simulation") < lines.index("## Output")


def test_download_bundle_restarts_when_the_resume_range_is_rejected(
    tmp_path: Path,
) -> None:
    payload = sample_bundle()
    (tmp_path / "bundle.zip.part").write_bytes(payload)
    seen: list[str | None] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request.headers.get("Range"))
        if request.headers.get("Range"):
            return httpx.Response(416)
        return httpx.Response(200, content=payload)

    client = OpenScientistJobs(
        api_key="k", backoff_seconds=0, transport=httpx.MockTransport(handler)
    )
    path = client.download_bundle(JOB_ID, tmp_path / "bundle.zip")
    assert seen == [f"bytes={len(payload)}-", None]
    assert path.read_bytes() == payload


def test_fetch_uses_the_template_recorded_at_run_time(tmp_path: Path) -> None:
    record = _record(tmp_path)
    output_root = tmp_path / "out"
    report = hdr.output_file_for(record, output_root, "openscientist")
    write_job_record(
        report,
        provider="openscientist",
        job_id=JOB_ID,
        template_file="templates/hypothesis_dataset_analysis.md",
        template_sha="a" * 40,
    )
    # No marker at all: under the recorded analysis template this is invalid,
    # where the default literature template would have passed it as OK.
    result = hdr.fetch_record(
        record,
        provider="openscientist",
        output_root=output_root,
        jobs=FakeJobs(sample_bundle("# Report without a status marker\n")),
    )
    assert result.status == "INVALID_ANALYSIS_RUN"
    frontmatter = yaml.safe_load(report.read_text().split("---")[1])
    assert frontmatter["template_file"] == "templates/hypothesis_dataset_analysis.md"
    assert frontmatter["template_file_source"] == "recorded-at-run"
    assert frontmatter["template_sha"] == "a" * 40
    assert frontmatter["report_member"] == "final_report.md"


def test_fetch_refuses_a_template_that_contradicts_the_job_record(
    tmp_path: Path,
) -> None:
    record = _record(tmp_path)
    output_root = tmp_path / "out"
    report = hdr.output_file_for(record, output_root, "openscientist")
    write_job_record(
        report,
        provider="openscientist",
        job_id=JOB_ID,
        template_file="templates/hypothesis_dataset_analysis.md",
    )
    jobs = FakeJobs(sample_bundle())
    result = hdr.fetch_record(
        record,
        provider="openscientist",
        output_root=output_root,
        template=Path("templates/hypothesis_deep_research.md"),
        jobs=jobs,
    )
    assert result.status == "TEMPLATE_MISMATCH"
    assert jobs.fetched == []


def test_literature_run_does_not_download_the_bundle(
    tmp_path: Path, monkeypatch
) -> None:
    kb_dir = tmp_path / "kb" / "disorders"
    write_disorder(kb_dir)
    template = tmp_path / "t.md"
    template.write_text("Hypothesis {hypothesis_group_id}\n", encoding="utf-8")
    record = hdr.find_hypothesis(
        kb_dir, "Long_COVID", "canonical_persistence_immune_model"
    )
    output_root = tmp_path / "out"
    report = hdr.output_file_for(record, output_root, "openscientist")

    def fake_run(command, **kwargs):
        report.parent.mkdir(parents=True, exist_ok=True)
        report.write_text("---\nprovider: openscientist\n---\n\n# Report\n")
        stderr = f"INFO - OpenScientist job submitted: {JOB_ID}\n"
        return hdr.subprocess.CompletedProcess(command, 0, stdout="", stderr=stderr)

    def no_download(*args, **kwargs):
        raise AssertionError("a literature run must not download the bundle")

    monkeypatch.setattr(hdr.subprocess, "run", fake_run)
    monkeypatch.setattr(hdr, "restore_openscientist_artifacts", no_download)
    result = hdr.run_record(
        record,
        provider="openscientist",
        output_root=output_root,
        template=template,
        extra_args=[],
        timeout_seconds=10,
        dry_run=False,
        overwrite=False,
        validate_terms=False,
    )
    assert result.status == "OK"
    assert read_job_record(report)["job_id"] == JOB_ID
