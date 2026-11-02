"""Guard test: every evidence item in kb/ carries a reference_title.

The presence half of the title guard; tests/test_reference_titles.py covers
titles that are present but wrong. See scripts/find_missing_reference_titles.py.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

from scripts.find_missing_reference_titles import (
    SCAN_DIR,
    cache_has_no_title,
    main,
    scan,
    walk,
)

ROOT = Path(__file__).resolve().parents[1]


def _walk(data):
    missing_ev, missing_ref = [], []
    walk(data, missing_ev, missing_ref)
    return missing_ev, missing_ref


@pytest.mark.ci_step_twin("scripts/find_missing_reference_titles.py")
def test_committed_kb_has_no_evidence_item_without_a_reference_title():
    """The gate itself, over the real KB."""
    result = subprocess.run(
        [sys.executable, "scripts/find_missing_reference_titles.py", "--details"],
        check=False,
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout[-4000:] + result.stderr[-2000:]


def test_flags_an_absent_reference_title_at_any_depth():
    data = {
        "pathophysiology": [
            {"downstream": [{"evidence": [{"reference": "PMID:1", "supports": "SUPPORT"}]}]}
        ]
    }
    ev, ref = _walk(data)
    assert ev == [("pathophysiology[0].downstream[0].evidence[0]", "PMID:1")]
    assert ref == []


def test_blank_and_whitespace_titles_count_as_missing():
    data = {
        "evidence": [
            {"reference": "PMID:1", "reference_title": ""},
            {"reference": "PMID:2", "reference_title": "   "},
            {"reference": "PMID:3", "reference_title": None},
        ]
    }
    ev, _ = _walk(data)
    assert [r for _, r in ev] == ["PMID:1", "PMID:2", "PMID:3"]


def test_literature_evidence_is_an_evidence_list_too():
    data = {"association_signals": [{"literature_evidence": [{"reference": "PMID:1"}]}]}
    ev, _ = _walk(data)
    assert ev == [("association_signals[0].literature_evidence[0]", "PMID:1")]


def test_a_titled_item_is_never_flagged():
    data = {"evidence": [{"reference": "PMID:1", "reference_title": "A study."}]}
    assert _walk(data) == ([], [])


def test_publication_references_are_collected_separately():
    # PublicationReference uses `title`, not `reference_title`, and is report-only.
    data = {
        "references": [
            {"reference": "PMID:1"},
            {"reference": "PMID:2", "title": "Has one."},
            {"reference": "PMID:3", "reference_title": "Wrong slot for this class."},
        ]
    }
    ev, ref = _walk(data)
    assert ev == []
    assert [r for _, r in ref] == ["PMID:1", "PMID:3"]


def test_scan_dir_is_the_kb_root_not_just_disorders():
    assert SCAN_DIR == ROOT / "kb"


def _write(tmp_path, body):
    path = tmp_path / "kb" / "modules" / "m.yaml"
    path.parent.mkdir(parents=True)
    path.write_text(body, encoding="utf-8")
    return path


def test_main_fails_on_an_evidence_gap(tmp_path, capsys):
    path = _write(tmp_path, "name: M\nevidence:\n- reference: PMID:1\n  supports: SUPPORT\n")
    assert main([str(path)]) == 1
    assert "backfill_reference_titles.py" in capsys.readouterr().err


def test_main_passes_when_only_a_publication_reference_lacks_a_title(tmp_path):
    path = _write(tmp_path, "name: M\nreferences:\n- reference: PMID:1\n")
    assert main([str(path)]) == 0


def test_scan_reports_paths_relative_to_the_given_root(tmp_path):
    path = _write(tmp_path, "name: M\nevidence:\n- reference: PMID:1\n")
    rows = scan([path], rel_to=tmp_path)
    assert rows == [("kb/modules/m.yaml", [("evidence[0]", "PMID:1")], [])]


def test_scan_skips_unparseable_yaml(tmp_path, capsys):
    path = _write(tmp_path, "not: [valid: yaml")
    assert scan([path], rel_to=tmp_path) == []
    assert "skipping unparseable" in capsys.readouterr().err


def _cache(tmp_path, name, frontmatter):
    cache = tmp_path / "references_cache"
    cache.mkdir(exist_ok=True)
    (cache / name).write_text(f"---\n{frontmatter}---\n\nbody\n", encoding="utf-8")
    return cache


def test_a_cached_reference_with_no_title_is_detected(tmp_path):
    cache = _cache(tmp_path, "PMID_1.md", "reference_id: PMID:1\nyear: '2012'\n")
    assert cache_has_no_title("PMID:1", cache)


def test_an_empty_title_value_counts_as_no_title(tmp_path):
    cache = _cache(tmp_path, "PMID_1.md", "reference_id: PMID:1\ntitle: ''\n")
    assert cache_has_no_title("PMID:1", cache)


def test_a_cached_title_means_the_gap_is_fillable(tmp_path):
    cache = _cache(tmp_path, "PMID_1.md", "reference_id: PMID:1\ntitle: A study.\n")
    assert not cache_has_no_title("PMID:1", cache)


def test_an_uncached_reference_is_fillable_by_fetching(tmp_path):
    cache = _cache(tmp_path, "PMID_2.md", "reference_id: PMID:2\n")
    assert not cache_has_no_title("PMID:1", cache)


def test_doi_slashes_map_to_the_cache_filename(tmp_path):
    cache = _cache(tmp_path, "DOI_10.1_x.y.md", "reference_id: DOI:10.1/x.y\n")
    assert cache_has_no_title("DOI:10.1/x.y", cache)


def test_url_references_map_to_the_validators_cache_filename(tmp_path):
    cache = _cache(
        tmp_path, "url_https___example.org_a.pdf.md", "reference_id: url:https://example.org/a.pdf\n"
    )
    assert cache_has_no_title("url:https://example.org/a.pdf#page=3", cache)


def test_main_reports_but_passes_an_item_whose_cache_has_no_title(tmp_path, monkeypatch, capsys):
    import scripts.find_missing_reference_titles as fmrt

    cache = _cache(tmp_path, "PMID_1.md", "reference_id: PMID:1\n")
    monkeypatch.setattr(fmrt, "CACHE_DIR", cache)
    monkeypatch.setattr(fmrt.cache_has_no_title, "__defaults__", (cache,))
    path = _write(tmp_path, "name: M\nevidence:\n- reference: PMID:1\n")
    assert main([str(path), "--details"]) == 0
    assert "cache has no title; report-only" in capsys.readouterr().out
