"""Tests for scripts/fetch_edison_artifacts.py.

These tests exercise the pure-Python logic (frontmatter patching, artifact
writing, filename de-duplication) without making any network calls.  All Edison
/ deep-research-client objects are constructed locally from real model classes
rather than being mocked, so the tests remain faithful to the actual data
structures while staying fast and offline.
"""

from __future__ import annotations

import base64
import textwrap
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest
import yaml

pytest.importorskip("deep_research_client", reason="deep-research-client not installed")
pytest.importorskip("edison_client", reason="edison_client not installed")

# Import the helpers under test directly so tests don't depend on __main__ entry
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
import fetch_edison_artifacts as fea  # noqa: E402  (import after sys.path manipulation)

from deep_research_client.models import ResearchArtifact  # noqa: E402


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

def _make_artifact(
    filename: str = "figure.png",
    media_type: str = "image/png",
    source: str = "edison_answer_artifacts",
    description: str = "Figure 1",
    content: bytes = b"PNG_BYTES",
    data_storage_id: str | None = None,
) -> ResearchArtifact:
    return ResearchArtifact(
        filename=filename,
        content_base64=base64.b64encode(content).decode("ascii"),
        media_type=media_type,
        source=source,
        description=description,
        data_storage_id=data_storage_id,
    )


def _base_report(extra_fm: str = "", body: str = "## Output\n\nBody text.\n") -> str:
    fm = textwrap.dedent(f"""\
        provider: falcon
        model: Edison Scientific Literature
        cached: false
        citation_count: 3
        {extra_fm}
    """).strip()
    return f"---\n{fm}\n---\n\n{body}"


# ---------------------------------------------------------------------------
# _load_api_key
# ---------------------------------------------------------------------------

def test_load_api_key_from_env(monkeypatch):
    monkeypatch.setenv("EDISON_API_KEY", "test-key-123")
    assert fea._load_api_key() == "test-key-123"


def test_load_api_key_futurehouse_fallback(monkeypatch):
    monkeypatch.delenv("EDISON_API_KEY", raising=False)
    monkeypatch.setenv("FUTUREHOUSE_API_KEY", "fh-legacy-key")
    assert fea._load_api_key() == "fh-legacy-key"


def test_load_api_key_strips_whitespace(monkeypatch):
    monkeypatch.setenv("EDISON_API_KEY", "  my-key  \n")
    assert fea._load_api_key() == "my-key"


def test_load_api_key_raises_when_missing(monkeypatch):
    monkeypatch.delenv("EDISON_API_KEY", raising=False)
    monkeypatch.delenv("FUTUREHOUSE_API_KEY", raising=False)
    with pytest.raises(SystemExit):
        fea._load_api_key()


# ---------------------------------------------------------------------------
# _write_artifacts
# ---------------------------------------------------------------------------

def test_write_artifacts_creates_directory(tmp_path):
    report = tmp_path / "Foo-deep-research-falcon.md"
    report.write_text(_base_report())
    artifacts = [_make_artifact("fig1.png", content=b"PNG1")]

    fea._write_artifacts(artifacts, report)

    artifact_dir = tmp_path / "Foo-deep-research-falcon_artifacts"
    assert artifact_dir.is_dir()
    assert (artifact_dir / "fig1.png").exists()
    assert (artifact_dir / "fig1.png").read_bytes() == b"PNG1"


def test_write_artifacts_sets_relative_path_on_artifact(tmp_path):
    report = tmp_path / "Foo-deep-research-falcon.md"
    report.write_text(_base_report())
    artifact = _make_artifact("chart.png")

    fea._write_artifacts([artifact], report)

    assert artifact.path == "Foo-deep-research-falcon_artifacts/chart.png"


# ---------------------------------------------------------------------------
# _update_research_file – frontmatter patching
# ---------------------------------------------------------------------------

def test_update_research_file_adds_trajectory_id(tmp_path):
    report = tmp_path / "report.md"
    report.write_text(_base_report())
    artifact = _make_artifact()
    artifact.path = "report_artifacts/figure.png"

    fea._update_research_file(report, "traj-abc-123", [artifact])

    fm = yaml.safe_load(report.read_text().split("\n---\n")[0].lstrip("---\n"))
    assert fm["trajectory_id"] == "traj-abc-123"


def test_update_research_file_adds_artifact_count(tmp_path):
    report = tmp_path / "report.md"
    report.write_text(_base_report())
    artifacts = [_make_artifact(), _make_artifact("table.md", media_type="text/markdown")]
    for a in artifacts:
        a.path = f"report_artifacts/{a.filename}"

    fea._update_research_file(report, "traj-xyz", artifacts)

    fm = yaml.safe_load(report.read_text().split("\n---\n")[0].lstrip("---\n"))
    assert fm["artifact_count"] == 2
    assert len(fm["artifacts"]) == 2


def test_update_research_file_preserves_existing_fields(tmp_path):
    report = tmp_path / "report.md"
    report.write_text(_base_report())
    artifact = _make_artifact()
    artifact.path = "report_artifacts/figure.png"

    fea._update_research_file(report, "traj-1", [artifact])

    fm = yaml.safe_load(report.read_text().split("\n---\n")[0].lstrip("---\n"))
    assert fm["provider"] == "falcon"
    assert fm["citation_count"] == 3


def test_update_research_file_overwrites_existing_trajectory_id(tmp_path):
    report = tmp_path / "report.md"
    report.write_text(_base_report(extra_fm="trajectory_id: old-traj"))
    artifact = _make_artifact()
    artifact.path = "report_artifacts/figure.png"

    fea._update_research_file(report, "new-traj", [artifact])

    fm = yaml.safe_load(report.read_text().split("\n---\n")[0].lstrip("---\n"))
    assert fm["trajectory_id"] == "new-traj"


def test_update_research_file_skips_when_no_frontmatter(tmp_path, capsys):
    report = tmp_path / "report.md"
    report.write_text("No frontmatter here.\n")
    artifact = _make_artifact()

    fea._update_research_file(report, "traj-1", [artifact])

    assert "Warning" in capsys.readouterr().out
    # File should be unchanged
    assert report.read_text() == "No frontmatter here.\n"


# ---------------------------------------------------------------------------
# _update_research_file – ## Artifacts section (images only)
# ---------------------------------------------------------------------------

def test_update_injects_artifacts_section_for_images(tmp_path):
    body = "## Output\n\nSome text.\n\n## Citations\n\n1. Ref.\n"
    report = tmp_path / "report.md"
    report.write_text(_base_report(body=body))
    artifact = _make_artifact("fig.png", media_type="image/png")
    artifact.path = "report_artifacts/fig.png"

    fea._update_research_file(report, "traj-1", [artifact])

    text = report.read_text()
    assert "## Artifacts" in text
    assert "![Figure 1](report_artifacts/fig.png)" in text
    # Artifacts section should appear before Citations
    assert text.index("## Artifacts") < text.index("## Citations")


def test_update_does_not_inject_artifacts_section_for_non_images(tmp_path):
    report = tmp_path / "report.md"
    report.write_text(_base_report())
    artifact = _make_artifact("table.md", media_type="text/markdown")
    artifact.path = "report_artifacts/table.md"

    fea._update_research_file(report, "traj-1", [artifact])

    assert "## Artifacts" not in report.read_text()


def test_update_does_not_duplicate_artifacts_section(tmp_path):
    body = "## Output\n\nText.\n\n## Artifacts\n\n![old](old.png)\n"
    report = tmp_path / "report.md"
    report.write_text(_base_report(body=body))
    artifact = _make_artifact("new.png", media_type="image/png")
    artifact.path = "report_artifacts/new.png"

    fea._update_research_file(report, "traj-1", [artifact])

    # Only one ## Artifacts heading
    assert report.read_text().count("## Artifacts") == 1


# ---------------------------------------------------------------------------
# fetch_artifacts – smoke test with mocked Edison client
# ---------------------------------------------------------------------------

def test_fetch_artifacts_returns_zero_when_no_artifacts(tmp_path, monkeypatch):
    """fetch_artifacts returns 0 gracefully when the trajectory has no artifacts."""
    monkeypatch.setenv("EDISON_API_KEY", "dummy-key")
    report = tmp_path / "report.md"
    report.write_text(_base_report())

    mock_response = MagicMock()
    mock_response.status = "completed"
    # TaskResponseVerbose type check
    from edison_client.models.app import TaskResponseVerbose
    mock_response.__class__ = TaskResponseVerbose

    with (
        patch("edison_client.EdisonClient") as MockClient,
        patch("deep_research_client.providers.falcon.FalconProvider") as MockProvider,
    ):
        MockClient.return_value.get_task.return_value = mock_response
        MockProvider.return_value._extract_artifacts.return_value = []

        result = fea.fetch_artifacts("traj-empty", report)

    assert result == 0


def test_fetch_artifacts_saves_artifacts_and_returns_count(tmp_path, monkeypatch):
    """fetch_artifacts writes files and returns the number of artifacts saved."""
    monkeypatch.setenv("EDISON_API_KEY", "dummy-key")
    report = tmp_path / "report.md"
    report.write_text(_base_report())

    mock_response = MagicMock()
    mock_response.status = "completed"
    from edison_client.models.app import TaskResponseVerbose
    mock_response.__class__ = TaskResponseVerbose

    artifact = _make_artifact("figure.png", media_type="image/png", content=b"PNG")

    with (
        patch("edison_client.EdisonClient") as MockClient,
        patch("deep_research_client.providers.falcon.FalconProvider") as MockProvider,
    ):
        MockClient.return_value.get_task.return_value = mock_response
        MockProvider.return_value._extract_artifacts.return_value = [artifact]

        result = fea.fetch_artifacts("traj-has-artifacts", report)

    assert result == 1
    artifact_dir = tmp_path / "report_artifacts"
    assert artifact_dir.is_dir()
    assert (artifact_dir / "figure.png").read_bytes() == b"PNG"
