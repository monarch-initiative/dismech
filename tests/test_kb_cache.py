"""Tests for the process-wide parsed-document cache (dismech.kb_cache, #11003)."""

from __future__ import annotations

import pytest

from dismech import kb_cache


@pytest.fixture(autouse=True)
def _fresh_cache():
    kb_cache.clear_cache()
    yield
    kb_cache.clear_cache()


def test_unchanged_file_returns_the_same_parsed_object(tmp_path):
    path = tmp_path / "A.yaml"
    path.write_text("name: A\nphenotypes:\n- name: P\n")
    first = kb_cache.load_document(path)
    second = kb_cache.load_document(path)
    assert first is second
    assert first == {"name": "A", "phenotypes": [{"name": "P"}]}
    assert kb_cache.cache_size() == 1


def test_changed_content_is_reparsed_even_with_the_same_size(tmp_path):
    """Freshness is by content hash, so a same-size rewrite inside the
    filesystem's timestamp granularity still invalidates."""
    path = tmp_path / "A.yaml"
    path.write_text("name: AB\n")
    first = kb_cache.load_document(path)
    path.write_text("name: BA\n")
    second = kb_cache.load_document(path)
    assert first == {"name": "AB"}
    assert second == {"name": "BA"}
    assert kb_cache.cache_size() == 1


def test_empty_file_parses_to_none_and_is_cached(tmp_path):
    path = tmp_path / "empty.yaml"
    path.write_text("")
    assert kb_cache.load_document(path) is None
    assert kb_cache.load_document(path) is None
    assert kb_cache.cache_size() == 1


def test_missing_file_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        kb_cache.load_document(tmp_path / "nope.yaml")


def test_disabled_by_environment_parses_afresh(tmp_path, monkeypatch):
    monkeypatch.setenv("DISMECH_KB_CACHE", "0")
    path = tmp_path / "A.yaml"
    path.write_text("name: A\n")
    first = kb_cache.load_document(path)
    second = kb_cache.load_document(path)
    assert first == second == {"name": "A"}
    assert first is not second
    assert kb_cache.cache_size() == 0


def test_iter_documents_is_sorted_and_skips_history_snapshots(tmp_path):
    (tmp_path / "B.yaml").write_text("name: B\n")
    (tmp_path / "A.yaml").write_text("name: A\n")
    (tmp_path / "A.history.yaml").write_text("sessions: []\n")
    (tmp_path / "notes.txt").write_text("not yaml\n")
    docs = list(kb_cache.iter_documents(tmp_path))
    assert [p.name for p, _ in docs] == ["A.yaml", "B.yaml"]
    assert [d["name"] for _, d in docs] == ["A", "B"]
    with_history = list(kb_cache.iter_documents(tmp_path, skip_history=False))
    assert [p.name for p, _ in with_history] == ["A.history.yaml", "A.yaml", "B.yaml"]


def test_renderer_keeps_a_private_copy_for_the_page_it_decorates(tmp_path):
    """render.load_disorder must not hand back the shared object.

    render_disorder mutates what it loads (page hrefs, anchors), so if it read
    from the cache every later index walk would see those decorations.
    """
    from dismech import render

    path = tmp_path / "A.yaml"
    path.write_text("name: A\n")
    shared = render.load_disorder_shared(path)
    private = render.load_disorder(path)
    assert shared == private
    assert shared is not private
    assert shared is kb_cache.load_document(path)
