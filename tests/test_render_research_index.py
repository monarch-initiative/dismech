from pathlib import Path

import yaml

from dismech.render import _collect_research_index_rows, render_research_index


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
        "fallback",
        "openscientist",
        "other",
    ):
        assert f'provider-filter-{provider_key}' in html

    assert "OpenScientist" in html
    assert "Other" in html