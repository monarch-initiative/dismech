import pytest
from dismech.render import collect_reports


@pytest.fixture
def reports_dir(tmp_path):
    disorder_dir = tmp_path / "reports" / "Test_Disorder"
    disorder_dir.mkdir(parents=True)
    (disorder_dir / "01-perturbation-analysis.md").write_text(
        "# Perturbation Analysis\n\nSome **bold** results.\n\n| Gene | Effect |\n|------|--------|\n| CASR | LoF |\n"
    )
    (disorder_dir / "02-simulation-summary.md").write_text(
        "# Simulation Summary\n\nMore results here.\n"
    )
    return tmp_path


def test_collect_reports_finds_files(reports_dir):
    results = collect_reports("Test_Disorder", reports_root=reports_dir / "reports")
    assert len(results) == 2
    assert results[0]["title"] == "Perturbation Analysis"
    assert results[1]["title"] == "Simulation Summary"


def test_collect_reports_contains_html(reports_dir):
    results = collect_reports("Test_Disorder", reports_root=reports_dir / "reports")
    assert "<strong>bold</strong>" in results[0]["html"]
    assert "<table>" in results[0]["html"]


def test_collect_reports_empty_dir(tmp_path):
    results = collect_reports("Nonexistent_Disorder", reports_root=tmp_path / "reports")
    assert results == []


def test_collect_reports_fallback_title(reports_dir):
    disorder_dir = reports_dir / "reports" / "Test_Disorder"
    (disorder_dir / "03-no-heading.md").write_text(
        "Just some text without a heading.\n"
    )
    results = collect_reports("Test_Disorder", reports_root=reports_dir / "reports")
    no_heading = [r for r in results if r["filename"] == "03-no-heading.md"][0]
    assert no_heading["title"] == "03-no-heading"
