"""Tests for deep-research provider coverage reporting."""

from __future__ import annotations

import importlib.util
import sys
from io import StringIO
from pathlib import Path


ROOT = Path(__file__).parent.parent
SCRIPT_PATH = ROOT / "scripts" / "deep_research_coverage.py"
SPEC = importlib.util.spec_from_file_location("deep_research_coverage", SCRIPT_PATH)
assert SPEC and SPEC.loader
deep_research_coverage = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = deep_research_coverage
SPEC.loader.exec_module(deep_research_coverage)


def write_report(path: Path, provider: str, end_time: str, citation_count: int) -> None:
    path.write_text(
        f"""---
provider: {provider}
end_time: '{end_time}'
citation_count: {citation_count}
---

## Output
""",
        encoding="utf-8",
    )


def test_build_coverage_reports_one_row_per_disorder(tmp_path: Path) -> None:
    kb_dir = tmp_path / "kb" / "disorders"
    research_dir = tmp_path / "research"
    kb_dir.mkdir(parents=True)
    research_dir.mkdir()
    (kb_dir / "Foo_Disease.yaml").write_text(
        "name: Foo Disease\ncategory: Genetic\n", encoding="utf-8"
    )
    (kb_dir / "Bar_Disease.yaml").write_text(
        "name: Bar Disease\ncategory: Complex\n", encoding="utf-8"
    )
    (kb_dir / "Old_Disease.history.yaml").write_text(
        "name: Old Disease\n", encoding="utf-8"
    )

    falcon = research_dir / "Foo_Disease-deep-research-falcon.md"
    openscientist = research_dir / "Foo_Disease-deep-research-openscientist.md"
    write_report(falcon, "falcon", "2026-05-01T00:00:00", 3)
    write_report(openscientist, "openscientist", "2026-05-02T00:00:00", 4)
    Path(f"{falcon}.citations.md").write_text("PMID:1\n", encoding="utf-8")
    Path(f"{openscientist}.citations.md").write_text("", encoding="utf-8")
    (research_dir / "Foo_Disease-deep-research-fallback.citations.md").write_text(
        "PMID:2\n", encoding="utf-8"
    )
    write_report(
        research_dir / "com_Foo__Bar-deep-research-falcon.md",
        "falcon",
        "2026-05-03T00:00:00",
        1,
    )

    rows = deep_research_coverage.build_coverage(kb_dir, research_dir)

    assert [row.disorder.slug for row in rows] == ["Bar_Disease", "Foo_Disease"]
    foo = next(row for row in rows if row.disorder.slug == "Foo_Disease")
    assert foo.providers == ("falcon", "openscientist")
    assert foo.report_count == 2
    assert foo.citation_file_count == 1
    assert foo.latest_report.provider == "openscientist"


def test_status_output_is_tsv_with_comment_summary(tmp_path: Path) -> None:
    kb_dir = tmp_path / "kb" / "disorders"
    research_dir = tmp_path / "research"
    kb_dir.mkdir(parents=True)
    research_dir.mkdir()
    (kb_dir / "Foo_Disease.yaml").write_text("name: Foo Disease\n", encoding="utf-8")
    (kb_dir / "Bar_Disease.yaml").write_text("name: Bar Disease\n", encoding="utf-8")
    write_report(
        research_dir / "Foo_Disease-deep-research-openscientist.md",
        "openscientist",
        "2026-05-02T00:00:00",
        4,
    )

    rows = deep_research_coverage.build_coverage(kb_dir, research_dir)
    out = StringIO()
    deep_research_coverage.write_status(
        rows,
        rows,
        target_provider="openscientist",
        missing_provider=None,
        out=out,
        include_summary=True,
    )

    lines = out.getvalue().splitlines()
    assert lines[0].split("\t")[:4] == [
        "disorder",
        "name",
        "category",
        "providers",
    ]
    assert "\ttarget_provider\thas_target_provider\t" in lines[0]
    assert len(lines[0].split("\t")) == len(lines[1].split("\t"))
    assert any(line.startswith("# provider\topenscientist\t1\t1\t0") for line in lines)
    assert any(line == "# target_provider_missing\t1" for line in lines)


def test_missing_provider_filter_and_research_commands(tmp_path: Path) -> None:
    kb_dir = tmp_path / "kb" / "disorders"
    research_dir = tmp_path / "research"
    kb_dir.mkdir(parents=True)
    research_dir.mkdir()
    (kb_dir / "Foo_Disease.yaml").write_text("name: Foo Disease\n", encoding="utf-8")
    (kb_dir / "Bar_Disease.yaml").write_text("name: Bar Disease\n", encoding="utf-8")
    write_report(
        research_dir / "Foo_Disease-deep-research-openscientist.md",
        "openscientist",
        "2026-05-02T00:00:00",
        4,
    )

    rows = deep_research_coverage.build_coverage(kb_dir, research_dir)
    missing = deep_research_coverage.filter_rows(
        rows,
        missing_provider="openscientist",
    )

    assert [row.disorder.slug for row in missing] == ["Bar_Disease"]
    assert deep_research_coverage.build_research_command(
        "openscientist", "Bar_Disease", ["--param", "max_iterations=1"]
    ) == [
        "just",
        "research-disorder",
        "openscientist",
        "Bar_Disease",
        "--param",
        "max_iterations=1",
    ]
    assert deep_research_coverage.build_research_command(
        "cyberian-codex", "Bar_Disease", []
    ) == ["just", "research-disorder-cyberian-codex", "Bar_Disease"]


def test_run_missing_dry_run_writes_attempt_report(tmp_path: Path) -> None:
    kb_dir = tmp_path / "kb" / "disorders"
    research_dir = tmp_path / "research"
    output_dir = tmp_path / "output"
    kb_dir.mkdir(parents=True)
    research_dir.mkdir()
    (kb_dir / "Foo_Disease.yaml").write_text("name: Foo Disease\n", encoding="utf-8")

    rows = deep_research_coverage.build_coverage(kb_dir, research_dir)
    status = deep_research_coverage.run_missing(
        rows,
        provider="openscientist",
        research_dir=research_dir,
        output_dir=output_dir,
        max_disorders=None,
        only=None,
        dry_run=True,
        timeout_seconds=1,
        stop_on_error=False,
        extra_args=[],
    )

    assert status == 0
    reports = list(output_dir.glob("deep_research_missing_openscientist_*.tsv"))
    assert len(reports) == 1
    assert "DRY_RUN" in reports[0].read_text(encoding="utf-8")


def test_run_missing_parser_keeps_wrapper_args_separate_from_research_args() -> None:
    args = deep_research_coverage.parse_args(
        [
            "run-missing",
            "openscientist",
            "--dry-run",
            "--max-disorders",
            "2",
            "--",
            "--param",
            "max_iterations=1",
        ]
    )

    assert args.provider == "openscientist"
    assert args.dry_run is True
    assert args.max_disorders == 2
    assert args.research_args == ["--param", "max_iterations=1"]
