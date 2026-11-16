"""A deep-research run marked ``answer_status: unsuccessful`` is never a report.

deep-research-client 0.2.14 writes that frontmatter (and exits 4) when the
provider could not answer, or when the claude_code/antigravity agent answered
from memory, declined, or marked its report incomplete. The file still lands in
``research/``; these tests pin every place that must not treat it as coverage.
"""

from __future__ import annotations

import importlib.util
import subprocess
import sys
from io import StringIO
from pathlib import Path

import pytest

from dismech import preflight_dr
from dismech.research_reports import (
    is_unsuccessful,
    read_frontmatter_only,
    report_is_unsuccessful,
)
from scripts.check_unsuccessful_research import find_unsuccessful
from scripts.check_unsuccessful_research import main as check_main

ROOT = Path(__file__).parent.parent


def _load_script(name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


deep_research_coverage = _load_script("deep_research_coverage")
qc_deep_research = _load_script("qc_deep_research")


def _report(path: Path, provider: str, answer_status: str | None = None) -> Path:
    status_line = f"answer_status: {answer_status}\n" if answer_status else ""
    path.write_text(
        f"---\nprovider: {provider}\n{status_line}citation_count: 0\n---\n\n"
        "> **Warning:** not a finished report.\n\n## Output\n",
        encoding="utf-8",
    )
    return path


# --- the shared predicate ---------------------------------------------------


def test_only_an_explicit_unsuccessful_status_counts() -> None:
    assert is_unsuccessful({"answer_status": "unsuccessful"})
    assert is_unsuccessful({"answer_status": " Unsuccessful "})
    assert not is_unsuccessful({"answer_status": "successful"})
    assert not is_unsuccessful({})
    assert not is_unsuccessful({"answer_status": None})


def test_frontmatter_reader_stops_at_the_block_and_tolerates_bad_input(tmp_path: Path) -> None:
    good = _report(tmp_path / "a.md", "claude_code", "unsuccessful")
    assert read_frontmatter_only(good)["answer_status"] == "unsuccessful"
    assert report_is_unsuccessful(good)

    no_block = tmp_path / "b.md"
    no_block.write_text("# heading\nanswer_status: unsuccessful\n", encoding="utf-8")
    assert read_frontmatter_only(no_block) == {}

    unterminated = tmp_path / "c.md"
    unterminated.write_text("---\nanswer_status: unsuccessful\n", encoding="utf-8")
    assert read_frontmatter_only(unterminated) == {}

    malformed = tmp_path / "d.md"
    malformed.write_text("---\nanswer_status: [unclosed\n---\n", encoding="utf-8")
    assert read_frontmatter_only(malformed) == {}

    # A body line that looks like the field is not frontmatter.
    body = tmp_path / "e.md"
    body.write_text("---\nprovider: falcon\n---\nanswer_status: unsuccessful\n", encoding="utf-8")
    assert not report_is_unsuccessful(body)


# --- the gate ---------------------------------------------------------------


def test_gate_flags_only_unsuccessful_reports(tmp_path: Path) -> None:
    research = tmp_path / "research"
    (research / "modules").mkdir(parents=True)
    artifacts = research / "Foo-deep-research-falcon_artifacts"
    artifacts.mkdir()

    bad = _report(research / "Foo-deep-research-claude_code.md", "claude_code", "unsuccessful")
    nested_bad = _report(
        research / "modules" / "bar-deep-research-antigravity.md", "antigravity", "unsuccessful"
    )
    _report(research / "Foo-deep-research-falcon.md", "falcon", "successful")
    _report(research / "Foo-deep-research-openai.md", "openai")
    # Sidecars and artifacts are not reports, whatever they contain.
    _report(Path(f"{bad}.citations.md"), "claude_code", "unsuccessful")
    _report(artifacts / "note.md", "falcon", "unsuccessful")

    assert find_unsuccessful(research) == sorted([bad, nested_bad])
    assert check_main([str(research)]) == 1


def test_gate_passes_a_clean_tree(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    research = tmp_path / "research"
    research.mkdir()
    _report(research / "Foo-deep-research-falcon.md", "falcon", "successful")
    assert check_main([str(research)]) == 0
    assert "OK" in capsys.readouterr().out


def test_gate_rejects_a_missing_directory(tmp_path: Path) -> None:
    assert check_main([str(tmp_path / "absent")]) == 2


# --- coverage ---------------------------------------------------------------


def _kb(tmp_path: Path) -> tuple[Path, Path]:
    kb_dir = tmp_path / "kb" / "disorders"
    research_dir = tmp_path / "research"
    kb_dir.mkdir(parents=True)
    research_dir.mkdir()
    (kb_dir / "Foo_Disease.yaml").write_text("name: Foo Disease\n", encoding="utf-8")
    return kb_dir, research_dir


def test_coverage_does_not_count_an_unsuccessful_run(tmp_path: Path) -> None:
    kb_dir, research_dir = _kb(tmp_path)
    dud = _report(
        research_dir / "Foo_Disease-deep-research-claude_code.md", "claude_code", "unsuccessful"
    )
    _report(research_dir / "Foo_Disease-deep-research-falcon.md", "falcon")

    (row,) = deep_research_coverage.build_coverage(kb_dir, research_dir)
    assert row.providers == ("falcon",)
    assert not row.has_provider("claude_code")
    assert [report.path for report in row.unsuccessful_reports] == [dud]

    out = StringIO()
    deep_research_coverage.write_status(
        [row], [row], target_provider=None, missing_provider=None, out=out, include_summary=True
    )
    text = out.getvalue()
    header, record = text.splitlines()[:2]
    columns = dict(zip(header.split("\t"), record.split("\t"), strict=True))
    assert columns["unsuccessful_reports"] == str(dud)
    assert "# unsuccessful_reports_total\t1" in text


def test_missing_provider_sweep_reruns_an_unsuccessful_run(tmp_path: Path) -> None:
    kb_dir, research_dir = _kb(tmp_path)
    _report(research_dir / "Foo_Disease-deep-research-claude_code.md", "claude_code", "unsuccessful")
    rows = deep_research_coverage.build_coverage(kb_dir, research_dir)
    assert [row.disorder.slug for row in deep_research_coverage.filter_rows(
        rows, missing_provider="claude_code"
    )] == ["Foo_Disease"]


def test_run_missing_labels_exit_4_unsuccessful(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    kb_dir, research_dir = _kb(tmp_path)
    rows = deep_research_coverage.build_coverage(kb_dir, research_dir)

    def fake_run(command, **kwargs):
        _report(
            research_dir / "Foo_Disease-deep-research-claude_code.md",
            "claude_code",
            "unsuccessful",
        )
        return subprocess.CompletedProcess(command, 4, "", "")

    monkeypatch.setattr(deep_research_coverage.subprocess, "run", fake_run)
    status = deep_research_coverage.run_missing(
        rows,
        provider="claude_code",
        research_dir=research_dir,
        output_dir=tmp_path / "out",
        max_disorders=None,
        only=None,
        dry_run=False,
        timeout_seconds=1,
        stop_on_error=False,
        extra_args=[],
    )
    assert status != 0
    (attempts,) = (tmp_path / "out").glob("deep_research_missing_claude_code_*.tsv")
    assert "\tUNSUCCESSFUL\t" in attempts.read_text(encoding="utf-8")


def test_qc_provider_map_skips_unsuccessful_runs_and_their_sidecars(tmp_path: Path) -> None:
    research = tmp_path / "research"
    research.mkdir()
    dud = _report(research / "Foo-deep-research-claude_code.md", "claude_code", "unsuccessful")
    Path(f"{dud}.citations.md").write_text("PMID:1\n", encoding="utf-8")
    _report(research / "Foo-deep-research-falcon.md", "falcon")

    assert dict(qc_deep_research.research_provider_map(str(research))) == {"Foo": {"falcon"}}


# --- preflight --------------------------------------------------------------


def test_preflight_refuses_an_unsuccessful_run_before_opening_mondo(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    dud = _report(tmp_path / "Foo-deep-research-claude_code.md", "claude_code", "unsuccessful")

    def must_not_open(*args, **kwargs):
        raise AssertionError("MONDO was opened for a report with nothing to vet")

    monkeypatch.setattr(preflight_dr, "open_mondo_adapter", must_not_open)
    with pytest.raises(SystemExit) as exc:
        preflight_dr.main([str(dud), "MONDO:0014572"])
    assert exc.value.code == 2
    assert "answer_status: unsuccessful" in capsys.readouterr().err
