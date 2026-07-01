from pathlib import Path

import yaml

import pytest

from dismech.render import (
    DEEP_RESEARCH_PROVIDERS,
    DETAILS_PROVIDER_BLOCK_BEGIN,
    DETAILS_PROVIDER_BLOCK_END,
    _collect_research_index_rows,
    _display_name_from_provider,
    _format_report_date,
    _humanize_provider,
    _scan_research_reports,
    render_provider_docs_table,
    render_research_index,
    render_research_index_page,
    update_details_provider_docs,
)


def _write_disorder(path: Path, data: dict) -> None:
    path.write_text(yaml.safe_dump(data, sort_keys=False))


def test_collect_research_index_rows_normalizes_provider_categories(
    tmp_path: Path,
) -> None:
    research_dir = tmp_path / "research"
    disorders_dir = tmp_path / "disorders"
    research_dir.mkdir()
    disorders_dir.mkdir()

    _write_disorder(disorders_dir / "Test_Disorder.yaml", {"name": "Test Disorder"})

    valid_reports = [
        "Test_Disorder-deep-research-falcon.md",
        "Test_Disorder-deep-research-cyberian-codex.md",
        "Test_Disorder-deep-research-openscientist-review.md",
        "Test_Disorder-deep-research-codex.md",
        "Test_Disorder-deep-research-fallback.md",
        "Test_Disorder-deep-research-claude_code.md",
        "Test_Disorder-deep-research-claudeweb.md",
    ]
    for filename in valid_reports:
        (research_dir / filename).write_text("# report\n")

    (research_dir / "Test_Disorder-deep-research-falcon.md.citations.md").write_text(
        "# citations\n"
    )
    (research_dir / "Test_Disorder-research-synthesis.md").write_text("# ignore\n")

    rows = _collect_research_index_rows(research_dir, disorders_dir)

    assert len(rows) == 1
    row = rows[0]
    assert row["name"] == "Test Disorder"
    assert row["href"] == "../disorders/Test_Disorder.html#literature-summaries"
    assert row["report_count"] == len(valid_reports)

    providers = {provider["key"]: provider for provider in row["providers"]}
    assert set(providers) == {
        "claude-code",
        "cyberian",
        "edison",
        "fallback",
        "openai",
        "openscientist",
        "other",
    }
    assert providers["edison"]["name"] == "Edison"
    assert providers["cyberian"]["name"] == "Cyberian"
    assert providers["openscientist"]["name"] == "OpenScientist"
    assert providers["openai"]["name"] == "OpenAI"
    assert providers["claude-code"]["name"] == "Claude Code"
    assert providers["fallback"]["name"] == "Fallback"
    assert providers["other"]["name"] == "Other"


def test_render_research_index_exposes_fixed_provider_filters(tmp_path: Path) -> None:
    output_path = tmp_path / "pages" / "research" / "index.html"

    render_research_index(
        [
            {
                "name": "Test Disorder",
                "href": "../disorders/Test_Disorder.html#literature-summaries",
                "report_count": 2,
                "provider_count": 2,
                "providers": [
                    {"name": "Edison", "key": "edison", "count": 1},
                    {"name": "OpenScientist", "key": "openscientist", "count": 1},
                ],
            }
        ],
        output_path=output_path,
    )

    html = output_path.read_text()

    for provider_key in (
        "edison",
        "asta",
        "openai",
        "cyberian",
        "perplexity",
        "claude-code",
        "fallback",
        "openscientist",
        "other",
    ):
        assert f'provider-filter-{provider_key}' in html

    assert "OpenScientist" in html
    assert "Other" in html


def test_registry_drives_filter_chips_in_order(tmp_path: Path) -> None:
    """Every filter chip is generated from the registry, in registry order."""
    output_path = tmp_path / "pages" / "research" / "index.html"
    render_research_index([], output_path=output_path)
    html = output_path.read_text()

    # The filter checkboxes appear in the same order as the registry.
    chip_positions = [
        html.index(f'provider-filter-{entry["key"]}"')
        for entry in DEEP_RESEARCH_PROVIDERS
    ]
    assert chip_positions == sorted(chip_positions)
    assert len(chip_positions) == len(DEEP_RESEARCH_PROVIDERS)


def test_registry_drives_legend_and_pill_colors(tmp_path: Path) -> None:
    """The legend, pill CSS, and link/description all come from the registry."""
    output_path = tmp_path / "pages" / "research" / "index.html"
    render_research_index([], output_path=output_path)
    html = output_path.read_text()

    for entry in DEEP_RESEARCH_PROVIDERS:
        # Legend category name and description text.
        assert entry["name"] in html
        assert entry["description"] in html
        # Pill CSS rule generated per key.
        assert f'.provider-pill.provider-{entry["key"]}' in html
        assert entry["pill"]["background"] in html
        # Product link only for entries that carry one.
        if entry["url"]:
            assert entry["url"] in html


def test_display_name_matches_registry_categories() -> None:
    """_display_name_from_provider returns the registry category for each slug."""
    for entry in DEEP_RESEARCH_PROVIDERS:
        for match_key in entry["match_keys"]:
            assert _display_name_from_provider(match_key) == entry["name"]
    # Unknown slugs fall through to the catch-all category.
    assert _display_name_from_provider("totally-unknown-provider") == "Other"


def test_humanize_provider_uses_registry_overrides() -> None:
    """_humanize_provider honors registry overrides, else title-cases the slug."""
    assert _humanize_provider("openai") == "OpenAI"
    assert _humanize_provider("openscientist") == "OpenScientist"
    assert _humanize_provider("falcon") == "Falcon"
    assert _humanize_provider("cyberian-codex") == "Cyberian Codex"
    assert _humanize_provider("claude_code") == "Claude Code"
    # Slugs without an override fall back to title-casing.
    assert _humanize_provider("codex") == "Codex"
    assert _humanize_provider("some_new-provider") == "Some New Provider"
    assert _humanize_provider(None) is None


def test_provider_docs_table_covers_whole_registry() -> None:
    """The docs table lists every registry provider with its description/link."""
    table = render_provider_docs_table()

    for entry in DEEP_RESEARCH_PROVIDERS:
        assert entry["name"] in table
        assert entry["description"] in table
        if entry["url"]:
            assert entry["url"] in table
        if entry["prefix"]:
            assert entry["prefix"] in table  # e.g. the fallback warning glyph

    # One table row per provider.
    assert table.count("<tr>") == len(DEEP_RESEARCH_PROVIDERS) + 1  # + header row


def _details_stub() -> str:
    return (
        "<html><body>\n"
        "            <h3>Deep Research Providers</h3>\n"
        f"            {DETAILS_PROVIDER_BLOCK_BEGIN}\n"
        "            <table><tbody>STALE</tbody></table>\n"
        f"            {DETAILS_PROVIDER_BLOCK_END}\n"
        "            <h3>Next section</h3>\n"
        "</body></html>\n"
    )


def test_update_details_provider_docs_replaces_block_idempotently(
    tmp_path: Path,
) -> None:
    details = tmp_path / "index.html"
    details.write_text(_details_stub())

    update_details_provider_docs(details)
    once = details.read_text()

    # Stale content is gone; registry content and surrounding page are intact.
    assert "STALE" not in once
    assert "Edison" in once
    assert "<h3>Next section</h3>" in once
    assert once.count(DETAILS_PROVIDER_BLOCK_BEGIN) == 1
    assert once.count(DETAILS_PROVIDER_BLOCK_END) == 1

    # Re-running is a no-op (safe to wire into a generation pipeline).
    update_details_provider_docs(details)
    assert details.read_text() == once


def test_update_details_provider_docs_requires_markers(tmp_path: Path) -> None:
    details = tmp_path / "index.html"
    details.write_text("<html><body>no markers here</body></html>")
    with pytest.raises(SystemExit):
        update_details_provider_docs(details)


def _seed_research_dirs(tmp_path: Path) -> tuple[Path, Path]:
    """Create a small research + disorders fixture and return their paths."""
    research_dir = tmp_path / "research"
    disorders_dir = tmp_path / "disorders"
    research_dir.mkdir()
    disorders_dir.mkdir()

    _write_disorder(
        disorders_dir / "Asthma.yaml",
        {
            "name": "Asthma",
            "disease_term": {"term": {"id": "MONDO:0004979", "label": "asthma"}},
        },
    )

    (research_dir / "Asthma-deep-research-falcon.md").write_text(
        "---\nprovider: falcon\nmodel: falcon-1\ncitation_count: 12\n"
        "end_time: '2025-05-01T09:30:00.123456'\n---\n"
        "# Asthma Pathophysiology Report\n\n## Executive Summary\n\n"
        "Asthma is chronic airway inflammation.\n"
    )
    (research_dir / "Asthma-deep-research-cyberian-codex.md").write_text(
        "# Asthma\n\n## Key Findings\n\nBronchial hyperresponsiveness.\n"
    )
    # An orphan report whose slug has no matching disorder YAML page.
    (research_dir / "Mystery_Disease-deep-research-openscientist.md").write_text(
        "# Mystery\n\n## Key Findings\n\nUnknown.\n"
    )
    # These must be ignored by the scanner.
    (research_dir / "Asthma-deep-research-falcon.md.citations.md").write_text("# c\n")
    (research_dir / "Asthma-research-synthesis.md").write_text("# s\n")
    return research_dir, disorders_dir


def test_scan_research_reports_extracts_per_report_metadata(tmp_path: Path) -> None:
    research_dir, disorders_dir = _seed_research_dirs(tmp_path)

    reports = _scan_research_reports(research_dir, disorders_dir)

    # Citation and synthesis files are excluded; three real reports remain.
    assert len(reports) == 3

    by_output = {report["output_name"]: report for report in reports}
    assert set(by_output) == {
        "Asthma-falcon.html",
        "Asthma-cyberian-codex.html",
        "Mystery_Disease-openscientist.html",
    }

    falcon = by_output["Asthma-falcon.html"]
    assert falcon["disorder_name"] == "Asthma"
    assert falcon["provider_key"] == "edison"  # falcon collapses into the Edison pill
    assert falcon["provider_label"] == "Falcon"  # per-report label keeps the raw name
    assert falcon["mondo_id"] == "MONDO:0004979"
    assert falcon["disorder_page_href"] == (
        "../disorders/Asthma.html#literature-summaries"
    )
    assert falcon["row_key"] == "Asthma.html"

    # An orphan report (no disorder page) still scans, without a disorder link.
    orphan = by_output["Mystery_Disease-openscientist.html"]
    assert orphan["disorder_name"] == "Mystery Disease"
    assert orphan["disorder_page_href"] is None

    # Reports are sorted by disorder name, then provider label.
    assert [report["output_name"] for report in reports] == [
        "Asthma-cyberian-codex.html",
        "Asthma-falcon.html",
        "Mystery_Disease-openscientist.html",
    ]


def test_collect_index_rows_carries_report_links_and_mondo(tmp_path: Path) -> None:
    research_dir, disorders_dir = _seed_research_dirs(tmp_path)

    rows = _collect_research_index_rows(research_dir, disorders_dir)
    by_name = {row["name"]: row for row in rows}

    asthma = by_name["Asthma"]
    assert asthma["report_count"] == 2
    assert asthma["mondo_id"] == "MONDO:0004979"
    # Two per-report links, each pointing at its standalone page.
    report_hrefs = {report["href"] for report in asthma["reports"]}
    assert report_hrefs == {"Asthma-falcon.html", "Asthma-cyberian-codex.html"}
    labels = {report["label"] for report in asthma["reports"]}
    assert labels == {"Falcon", "Cyberian Codex"}

    # The category-aggregated provider pills are still present for filtering.
    provider_keys = {provider["key"] for provider in asthma["providers"]}
    assert provider_keys == {"edison", "cyberian"}


def test_render_research_index_page_writes_index_and_report_pages(
    tmp_path: Path,
) -> None:
    research_dir, disorders_dir = _seed_research_dirs(tmp_path)
    output_path = tmp_path / "pages" / "research" / "index.html"

    render_research_index_page(
        research_dir=research_dir,
        disorders_dir=disorders_dir,
        output_path=output_path,
    )

    generated = {p.name for p in output_path.parent.glob("*.html")}
    assert generated == {
        "index.html",
        "Asthma-falcon.html",
        "Asthma-cyberian-codex.html",
        "Mystery_Disease-openscientist.html",
    }

    # Index uses the card layout, exposes the name search, and links to reports.
    index_html = output_path.read_text()
    assert "report-card" in index_html
    assert 'id="disorder-search"' in index_html
    assert "MONDO:0004979" in index_html
    assert 'href="Asthma-falcon.html"' in index_html

    # A per-report page renders the markdown body and the disorder metadata.
    report_html = (output_path.parent / "Asthma-falcon.html").read_text()
    assert "Asthma Pathophysiology Report" in report_html
    assert "Executive Summary" in report_html
    assert "MONDO:0004979" in report_html
    assert "Model: falcon-1" in report_html
    assert "12 citations" in report_html
    # The date is rendered above the pills, date-only (time component dropped).
    assert '<div class="report-date">2025-05-01</div>' in report_html
    assert "09:30" not in report_html
    # Breadcrumb / links back to the index and the disorder page.
    assert "../disorders/Asthma.html#literature-summaries" in report_html
    # "Other Reports" sidebar links to the sibling report.
    assert 'href="Asthma-cyberian-codex.html"' in report_html
    # Source-of-truth link points at the markdown in the repo.
    assert "blob/main/research/Asthma-deep-research-falcon.md" in report_html


def test_format_report_date_reduces_to_date_only() -> None:
    import datetime

    assert _format_report_date("2025-05-01T09:30:00.123456") == "2025-05-01"
    assert _format_report_date("2025-05-01 09:30:00") == "2025-05-01"
    assert _format_report_date("2025-05-01") == "2025-05-01"
    assert _format_report_date(datetime.datetime(2025, 5, 1, 9, 30)) == "2025-05-01"
    assert _format_report_date(datetime.date(2025, 5, 1)) == "2025-05-01"
    assert _format_report_date(None) is None
    assert _format_report_date("") is None


def test_render_research_report_page_orphan_has_no_disorder_link(
    tmp_path: Path,
) -> None:
    research_dir, disorders_dir = _seed_research_dirs(tmp_path)
    output_path = tmp_path / "pages" / "research" / "index.html"

    render_research_index_page(
        research_dir=research_dir,
        disorders_dir=disorders_dir,
        output_path=output_path,
    )

    orphan_html = (
        output_path.parent / "Mystery_Disease-openscientist.html"
    ).read_text()
    assert "Mystery Disease" in orphan_html
    # No disorder page exists, so no relative disorder link should be emitted.
    assert "../disorders/" not in orphan_html
