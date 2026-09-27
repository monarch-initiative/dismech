"""Tests for the browser-index dead-link gate (PR #7903 follow-up).

``app/data.js`` is rebuilt from the whole KB on every generate-pages run while
disorder pages may build incrementally, so the index can link to pages that
were never rendered. These tests pin the gate's behaviour on that shape.
"""

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

_SPEC = importlib.util.spec_from_file_location(
    "check_browser_data_links",
    Path(__file__).resolve().parents[1] / "scripts" / "check_browser_data_links.py",
)
check_browser_data_links = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = check_browser_data_links
_SPEC.loader.exec_module(check_browser_data_links)

find_broken_links = check_browser_data_links.find_broken_links
find_ignored_paths = check_browser_data_links.find_ignored_paths
extract_page_urls = check_browser_data_links.extract_page_urls
parse_search_data = check_browser_data_links.parse_search_data
BrowserDataError = check_browser_data_links.BrowserDataError


def _write_data_js(tmp_path: Path, names: list[str]) -> Path:
    """Write an app/data.js in the real generator's framing."""
    app_dir = tmp_path / "app"
    app_dir.mkdir(parents=True, exist_ok=True)
    records = [
        {"name": name, "page_url": f"../pages/disorders/{name.replace(' ', '_')}.html"}
        for name in names
    ]
    data_path = app_dir / "data.js"
    data_path.write_text(
        f"window.searchData = {json.dumps(records, indent=2)};\n"
        'window.searchMetrics = {"total_disorders": ' + str(len(records)) + "};\n"
        "window.dispatchEvent(new Event('searchDataReady'));\n",
        encoding="utf-8",
    )
    return data_path


def _render_pages(tmp_path: Path, names: list[str]) -> None:
    pages_dir = tmp_path / "pages" / "disorders"
    pages_dir.mkdir(parents=True, exist_ok=True)
    for name in names:
        (pages_dir / f"{name.replace(' ', '_')}.html").write_text("<html></html>")


def test_all_pages_present_is_clean(tmp_path):
    names = ["Asthma", "Marfan Syndrome"]
    data_path = _write_data_js(tmp_path, names)
    _render_pages(tmp_path, names)
    broken, total = find_broken_links(data_path)
    assert broken == []
    assert total == 2


def test_unrendered_page_is_reported_as_broken(tmp_path):
    # The PR #7903 shape: data.js carries the whole KB, pages lag behind.
    data_path = _write_data_js(tmp_path, ["Asthma", "ADPRS-Related Neurodegeneration"])
    _render_pages(tmp_path, ["Asthma"])
    broken, total = find_broken_links(data_path)
    assert total == 2
    assert [(name, reason) for name, _, reason in broken] == [
        ("ADPRS-Related Neurodegeneration", "missing")
    ]


def test_missing_pages_directory_reports_every_link(tmp_path):
    data_path = _write_data_js(tmp_path, ["Asthma", "Marfan Syndrome"])
    broken, total = find_broken_links(data_path)
    assert len(broken) == total == 2


def test_page_urls_resolve_relative_to_data_js(tmp_path):
    # A page next to data.js must NOT satisfy a '../pages/disorders/' link.
    data_path = _write_data_js(tmp_path, ["Asthma"])
    (data_path.parent / "Asthma.html").write_text("<html></html>")
    broken, _ = find_broken_links(data_path)
    assert len(broken) == 1


def test_unparseable_data_js_falls_back_to_regex_scan():
    # A framing change must degrade to a regex scan, never to a silent pass.
    text = 'window.somethingElse = [{"page_url": "../pages/disorders/Asthma.html"}]'
    pairs = extract_page_urls(text)
    assert pairs == [("<unparsed record>", "../pages/disorders/Asthma.html")]


def test_data_js_with_no_links_is_an_error(tmp_path):
    data_path = tmp_path / "data.js"
    data_path.write_text("window.searchData = [];\n", encoding="utf-8")
    with pytest.raises(BrowserDataError):
        find_broken_links(data_path)


def test_git_ignored_page_is_a_dead_link(tmp_path):
    """A page that renders but is .gitignore'd never reaches the published site."""
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    names = ["Asthma", "Holt-Oram syndrome"]
    data_path = _write_data_js(tmp_path, names)
    _render_pages(tmp_path, names)
    (tmp_path / ".gitignore").write_text(
        "pages/disorders/Holt-Oram_syndrome.html\n", encoding="utf-8"
    )
    broken, total = find_broken_links(data_path)
    assert total == 2
    # Present on disk, so the existence check alone would have passed it.
    assert (tmp_path / "pages" / "disorders" / "Holt-Oram_syndrome.html").exists()
    assert [(name, reason) for name, _, reason in broken] == [
        ("Holt-Oram syndrome", "git-ignored")
    ]


def test_tracked_page_is_not_flagged_even_if_a_pattern_matches(tmp_path):
    # git check-ignore reports ignored AND untracked paths only; a committed
    # page must never be flagged.
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    data_path = _write_data_js(tmp_path, ["Asthma"])
    _render_pages(tmp_path, ["Asthma"])
    (tmp_path / ".gitignore").write_text("pages/disorders/Asthma.html\n", encoding="utf-8")
    subprocess.run(["git", "add", "-f", "pages/"], cwd=tmp_path, check=True)
    broken, _ = find_broken_links(data_path)
    assert broken == []


def test_ignored_check_is_inert_when_git_is_unavailable(tmp_path, monkeypatch):
    """No git binary must degrade to the on-disk check, not crash the gate."""
    names = ["Asthma"]
    data_path = _write_data_js(tmp_path, names)
    _render_pages(tmp_path, names)

    def _no_git(*args, **kwargs):
        raise OSError("git not found")

    monkeypatch.setattr(check_browser_data_links.subprocess, "run", _no_git)
    assert find_ignored_paths([Path("x")], tmp_path) == set()
    assert find_broken_links(data_path)[0] == []


def test_ignored_check_is_inert_when_git_errors(tmp_path, monkeypatch):
    """A non-repo cwd (rc=128) must not be read as 'everything is ignored'."""
    names = ["Asthma"]
    data_path = _write_data_js(tmp_path, names)
    _render_pages(tmp_path, names)

    class _Result:
        returncode = 128
        stdout = "fatal: not a git repository\n"

    monkeypatch.setattr(
        check_browser_data_links.subprocess, "run", lambda *a, **k: _Result()
    )
    assert find_broken_links(data_path)[0] == []


def test_fragment_bearing_page_url_resolves_to_the_page_file(tmp_path):
    """app/discussions/data.js and app/models/data.js link to an in-page anchor."""
    app_dir = tmp_path / "app" / "discussions"
    app_dir.mkdir(parents=True)
    pages_dir = tmp_path / "pages" / "disorders"
    pages_dir.mkdir(parents=True)
    (pages_dir / "Crohn_Disease.html").write_text("<html></html>")
    records = [
        {
            "name": "Crohn Disease",
            "page_url": "../../pages/disorders/Crohn_Disease.html#gap_abc",
        },
        {
            "name": "Missing Disease",
            "page_url": "../../pages/disorders/Missing_Disease.html#gap_xyz",
        },
    ]
    data_path = app_dir / "data.js"
    data_path.write_text(f"window.searchData = {json.dumps(records, indent=2)};\n")
    broken, total = find_broken_links(data_path)
    assert total == 2
    assert [(name, reason) for name, _, reason in broken] == [
        ("Missing Disease", "missing")
    ]


def test_parse_search_data_rejects_missing_assignment():
    with pytest.raises(BrowserDataError):
        parse_search_data("const x = 1;")


# Deliberately NOT tested here: the committed app/data.js against the committed
# pages/. Every curation PR adds a disorder YAML before the generate-pages
# workflow renders its page, so such a test would fail on the whole curation
# stream rather than on the drift it is meant to catch. The invariant belongs to
# the generate-pages run (which renders first, then gates), not to repo state.
