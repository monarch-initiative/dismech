"""Homepage stat cards must match their dedicated section pages (issue #5567).

The root ``index.html`` hero grid injects counts from ``window.searchMetrics``
(built by ``browser_export``), while the section pages compute their counts in
``render``. These tests assert the two agree, so the homepage cannot silently
drift as the KB grows. They compare *derived* values, not hardcoded numbers, so
they stay valid as content changes.
"""

from pathlib import Path

import pytest

from dismech import render
from dismech.export import utils
from dismech.export.browser_export import BrowserExporter

REPO_ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="session")
def metrics() -> dict:
    """Homepage stat-card metrics, built once for the whole session.

    Building these parses every disorder in the KB (~1700 files). Each test below
    used to rebuild them from scratch, paying that cost four times over for a
    read-only dict. Session scope makes it one build. See issue #7502.
    """
    files = utils.discover_disorder_files(REPO_ROOT / "kb" / "disorders")
    exporter = BrowserExporter()
    disorders = [exporter.load_disorder(path) for path in files]
    return exporter.build_summary_metrics(
        disorders,
        num_modules=0,
        num_research_reports=utils.count_research_reports(REPO_ROOT / "research"),
        num_classifications=utils.count_classifications(),
        num_comorbidities=utils.count_comorbidities(REPO_ROOT / "kb" / "comorbidities"),
        num_groupings=utils.count_groupings(REPO_ROOT / "kb" / "groupings"),
    )


def test_research_report_count_matches_research_index(metrics):
    rows = render._index_rows_from_reports(
        render._scan_research_reports(
            REPO_ROOT / "research", REPO_ROOT / "kb" / "disorders"
        )
    )
    section_total = sum(int(row.get("report_count") or 0) for row in rows)
    assert metrics["total_research_reports"] == section_total


def test_classification_count_matches_classification_index(metrics):
    assert metrics["total_classifications"] == len(render._load_classification_enums())


def test_comorbidity_count_matches_comorbidity_files(metrics):
    files = utils.discover_disorder_files(REPO_ROOT / "kb" / "comorbidities")
    assert metrics["total_comorbidities"] == len(files)


def test_grouping_count_matches_grouping_files(metrics):
    files = utils.discover_disorder_files(REPO_ROOT / "kb" / "groupings")
    assert metrics["total_groupings"] == len(files)


def test_homepage_stat_spans_are_wired_to_search_metrics():
    """Every stat span in index.html must have a matching setStat() JS hook."""
    html = (REPO_ROOT / "index.html").read_text()
    for stat_class in (
        "stat-research-reports",
        "stat-classifications",
        "stat-comorbidities",
        "stat-groupings",
    ):
        assert f'class="{stat_class}"' in html, f"missing span for {stat_class}"
        assert f"setStat('.{stat_class}'" in html, f"missing setStat for {stat_class}"
