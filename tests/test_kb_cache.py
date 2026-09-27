"""Tests for the process-wide parsed-document cache (dismech.kb_cache, #11003)."""

from __future__ import annotations

import copy
import os
from pathlib import Path

import pytest

from dismech import kb_cache

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module", autouse=True)
def _kb_cache_env():
    """Whatever DISMECH_KB_CACHE was before this module ran, restored after.

    Module scope so it finalizes after every function-scoped fixture, including
    `monkeypatch` -- nothing this file does can escape into another worker.
    """
    before = os.environ.get("DISMECH_KB_CACHE")
    yield before
    if before is None:
        os.environ.pop("DISMECH_KB_CACHE", None)
    else:
        os.environ["DISMECH_KB_CACHE"] = before


@pytest.fixture(autouse=True)
def _fresh_cache(_kb_cache_env):
    """Reset the cache and the env knob before each test in this file.

    The reset is at **setup**, not teardown, and that is the whole point.
    `kb_cache.default_off()` writes `os.environ` directly, so monkeypatch never
    records an undo for it; and `monkeypatch.delenv(..., raising=False)` on an
    unset variable records nothing either, so a later `setenv` snapshots the
    already-modified value and teardown faithfully restores the wrong one. A
    teardown-based restore here does not fix that, because monkeypatch's
    finalizer can run after this fixture's -- verified, it does. Establishing a
    known state before each test is immune to finalizer ordering.

    Without this the file poisons itself: `default_off()` leaves
    `DISMECH_KB_CACHE=0` set, every later `load_document` returns a fresh parse,
    and `test_shared_index_walk_stores_no_live_reference_into_the_document`
    passes vacuously because disjoint identities are then guaranteed.
    """
    if _kb_cache_env is None:
        os.environ.pop("DISMECH_KB_CACHE", None)
    else:
        os.environ["DISMECH_KB_CACHE"] = _kb_cache_env
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


@pytest.mark.parametrize("value", ["0", "false", "FALSE", "no", "off", " Off "])
def test_falsey_environment_values_all_disable(value, tmp_path, monkeypatch):
    monkeypatch.setenv("DISMECH_KB_CACHE", value)
    path = tmp_path / "A.yaml"
    path.write_text("name: A\n")
    assert kb_cache.load_document(path) is not kb_cache.load_document(path)
    assert kb_cache.cache_size() == 0


@pytest.mark.parametrize("value", ["1", "true", "yes", "on", "", "anything"])
def test_every_other_environment_value_leaves_caching_on(value, tmp_path, monkeypatch):
    """Only the four documented words turn it off; nothing else is a kill switch."""
    monkeypatch.setenv("DISMECH_KB_CACHE", value)
    path = tmp_path / "A.yaml"
    path.write_text("name: A\n")
    assert kb_cache.load_document(path) is kb_cache.load_document(path)


def test_iter_documents_honours_the_pattern(tmp_path):
    (tmp_path / "A.yaml").write_text("name: A\n")
    (tmp_path / "B.yml").write_text("name: B\n")
    assert [p.name for p, _ in kb_cache.iter_documents(tmp_path)] == ["A.yaml"]
    assert [p.name for p, _ in kb_cache.iter_documents(tmp_path, "*.yml")] == ["B.yml"]
    both = kb_cache.iter_documents(tmp_path, "*.y*ml")
    assert [p.name for p, _ in both] == ["A.yaml", "B.yml"]


def test_default_off_sets_the_knob_but_never_overrides_the_operator(monkeypatch):
    """`main()` calls this; an explicit DISMECH_KB_CACHE still wins."""
    monkeypatch.delenv("DISMECH_KB_CACHE", raising=False)
    kb_cache.default_off()
    assert os.environ["DISMECH_KB_CACHE"] == "0"

    monkeypatch.setenv("DISMECH_KB_CACHE", "1")
    kb_cache.default_off()
    assert os.environ["DISMECH_KB_CACHE"] == "1"


def test_single_walk_cli_mains_default_the_cache_off():
    """The four one-walk gates pay full retention for zero hits (PR #11185 review).

    Pinned by source rather than by running them: each main() then walks the
    whole corpus. The call must be in main(), not at import -- pytest imports
    their scan_repo functions directly and runs several in one process, which is
    the case the cache exists for.
    """
    import ast

    for name in (
        "check_snippet_length",
        "check_title_snippets",
        "check_empty_snippets",
        "nec_risk_audit",
    ):
        source = (ROOT / "scripts" / f"{name}.py").read_text(encoding="utf-8")
        tree = ast.parse(source)
        main = next(
            node
            for node in tree.body
            if isinstance(node, ast.FunctionDef) and node.name == "main"
        )
        calls = {
            ast.unparse(node.func)
            for node in ast.walk(main)
            if isinstance(node, ast.Call)
        }
        assert "kb_cache.default_off" in calls, f"{name}.main() must default it off"

        module_level = {
            ast.unparse(node.value.func)
            for node in tree.body
            if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)
        }
        assert "kb_cache.default_off" not in module_level, f"{name}: not at import"


def _container_ids(obj, seen=None):
    """ids of every dict/list reachable from obj (scalars are shared harmlessly)."""
    if seen is None:
        seen = set()
    if isinstance(obj, dict):
        seen.add(id(obj))
        for value in obj.values():
            _container_ids(value, seen)
    elif isinstance(obj, list):
        seen.add(id(obj))
        for item in obj:
            _container_ids(item, seen)
    return seen


def test_shared_index_walk_stores_no_live_reference_into_the_document(tmp_path):
    """The read-only contract, pinned for the grouping index walk.

    render._build_grouping_disorder_context builds several long-lived indexes
    from shared documents. Storing a live sub-object would mean a later
    annotation on the index leaked into every other walk in the process, so it
    must construct its own values -- which today it does. Identity is checked on
    containers only; scalars are immutable and share freely.
    """
    from dismech import render

    (tmp_path / "A.yaml").write_text(
        "name: Alpha\n"
        "disease_term:\n"
        "  preferred_term: alpha\n"
        "  term: {id: 'MONDO:0000001', label: alpha}\n"
        "mappings:\n"
        "  mondo_mappings:\n"
        "  - mapping_predicate: skos:narrowMatch\n"
        "    term: {id: 'MONDO:0000002', label: beta}\n"
        "phenotypes:\n"
        "- name: P\n"
        "  phenotype_term:\n"
        "    term: {id: 'HP:0000001', label: p}\n"
    )
    document = kb_cache.load_document(tmp_path / "A.yaml")
    snapshot = copy.deepcopy(document)

    render._build_grouping_disorder_context.cache_clear()
    try:
        context = render._build_grouping_disorder_context(str(tmp_path))
    finally:
        render._build_grouping_disorder_context.cache_clear()

    assert context["identity_by_name"], "fixture should have produced an index"
    # Without this the test passes vacuously when the cache is off: every
    # load_document returns a fresh parse, so the identities below are disjoint
    # by construction rather than because the walk built its own values.
    assert kb_cache.cache_size() == 1, "the walk must have gone through the cache"
    assert document == snapshot, "index walk mutated the shared document"
    shared = _container_ids(document)
    assert not (_container_ids(context) & shared), (
        "index holds a live reference into the shared document"
    )
