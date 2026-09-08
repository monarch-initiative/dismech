"""No code path may fetch a multi-gigabyte OAK build by accident (issue #11299).

The fast test lane was leaving 588 MB of `mondo.db` and 440 MB of `hp.db` behind
on a clean runner. Nothing asked for either: `get_adapter("sqlite:obo:mondo")`
does not fail when the build is absent, it downloads it, silently, so three MONDO
lookups in `render` and one HP lookup in `browser_export` each pulled a build
nobody had requested.

The rule these tests pin is the one #11251 established for NCIT and ICD10CM:
"did the adapter open?" is not a test for "is the build present". Anything that
must not trigger a download has to ask `oak_db.local_build_present` about the
file, and degrade when the answer is no.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from dismech import oak_db, render
from dismech.export import browser_export
from dismech.export.browser_export import HPOCategoryResolver

REPO_ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(autouse=True)
def _clear_mondo_memos():
    """`_mondo_adapter` is `@cache`d, so a verdict must not leak between tests."""
    render._mondo_adapter.cache_clear()
    render._cached_mondo_descendants.cache_clear()
    render._cached_mondo_label.cache_clear()
    yield
    render._mondo_adapter.cache_clear()
    render._cached_mondo_descendants.cache_clear()
    render._cached_mondo_label.cache_clear()


# --- MONDO, in render -------------------------------------------------------


def test_mondo_adapter_is_none_without_a_local_build(monkeypatch) -> None:
    """The whole point: no build on disk means no adapter, so no download."""
    monkeypatch.setattr(oak_db, "local_build_present", lambda spec: False)

    def _explode(spec: str):  # pragma: no cover - only runs on regression
        raise AssertionError(f"opened {spec} without a local build")

    monkeypatch.setattr(render, "_get_oak_adapter", _explode)
    assert render._mondo_adapter() is None


def test_mondo_lookups_degrade_rather_than_download(monkeypatch) -> None:
    monkeypatch.setattr(oak_db, "local_build_present", lambda spec: False)
    assert render._cached_mondo_descendants("MONDO:0007947") == ()
    # An unresolvable label falls back to the CURIE, which is what renders.
    assert render._cached_mondo_label("MONDO:0007947") == "MONDO:0007947"


def test_mondo_adapter_is_opened_when_the_build_is_present(monkeypatch) -> None:
    """The guard is about the file, not about disabling MONDO lookups."""
    sentinel = object()
    monkeypatch.setattr(oak_db, "local_build_present", lambda spec: True)
    monkeypatch.setattr(render, "_get_oak_adapter", lambda spec: sentinel)
    assert render._mondo_adapter() is sentinel


def test_unavailable_descendants_keep_the_exact_roots_in_scope(monkeypatch) -> None:
    """The roots come from the grouping YAML, so losing MONDO must not lose them.

    Dropping them emptied the scope set, which collapsed a grouping's coverage
    figure to "not assessed" even though it is computable from the file alone.
    The failure branch already kept them; the unavailable branch now agrees.
    """
    monkeypatch.setattr(oak_db, "local_build_present", lambda spec: False)
    roots = ["MONDO:1234567"]
    terms, scope, shadowed, note = render._exact_mondo_descendant_terms(roots, {})
    assert terms == {}
    assert scope == set(roots)
    assert shadowed == set()
    assert note is not None and "unavailable" in note


def test_no_exact_roots_still_reports_no_note(monkeypatch) -> None:
    """A grouping with no exact-match mapping is not an ontology outage."""
    monkeypatch.setattr(oak_db, "local_build_present", lambda spec: False)
    assert render._exact_mondo_descendant_terms([], {}) == ({}, set(), set(), None)


# --- HP, in browser_export --------------------------------------------------


def test_hpo_resolver_does_not_open_hp_without_a_local_build(monkeypatch) -> None:
    monkeypatch.setattr(oak_db, "local_build_present", lambda spec: False)

    def _explode(spec: str):  # pragma: no cover - only runs on regression
        raise AssertionError(f"opened {spec} without a local build")

    monkeypatch.setattr(browser_export, "get_adapter", _explode)
    resolver = HPOCategoryResolver()
    resolver._seed = {}
    assert resolver.resolve("HP:0002014") == []


def test_unresolved_terms_are_counted_and_never_cached(monkeypatch) -> None:
    """An unresolved term must not be written into the committed cache as empty.

    `_write_hpo_category_cache` dumps `_cache`, so memoising "no categories"
    because an ontology was missing would bake the gap in permanently.
    """
    monkeypatch.setattr(oak_db, "local_build_present", lambda spec: False)
    resolver = HPOCategoryResolver()
    resolver._seed = {}
    resolver.resolve("HP:0002014")
    resolver.resolve("HP:0002014")
    assert resolver._cache == {}
    assert resolver.unresolved_count == 1


def test_hpo_resolver_answers_from_the_committed_cache(monkeypatch) -> None:
    """The committed cache covers the KB, so a normal run opens no ontology."""
    monkeypatch.setattr(oak_db, "local_build_present", lambda spec: False)
    resolver = HPOCategoryResolver()
    resolver._seed = {"HP:0002014": ["Digestive"]}
    assert resolver.resolve("HP:0002014") == ["Digestive"]
    # Seeded hits are real answers, so they belong in the written cache.
    assert resolver._cache == {"HP:0002014": ["Digestive"]}
    assert resolver.unresolved_count == 0


def test_top_level_terms_never_need_an_ontology(monkeypatch) -> None:
    monkeypatch.setattr(oak_db, "local_build_present", lambda spec: False)
    resolver = HPOCategoryResolver()
    resolver._seed = {}
    assert resolver.resolve("HP:0025031") == ["Digestive"]


# --- the committed seed itself ----------------------------------------------


def test_the_committed_hpo_cache_is_where_both_sides_look() -> None:
    """Writer and readers share one path, resolved from the package, not the cwd."""
    assert browser_export.HPO_CATEGORY_CACHE_PATH == (
        REPO_ROOT / "app" / "hpo_category_cache.json"
    )
    assert render._HPO_CATEGORY_CACHE_PATH == browser_export.HPO_CATEGORY_CACHE_PATH


def test_the_committed_hpo_cache_seeds_the_resolver() -> None:
    """It is committed and non-trivial, which is what makes the miss path rare."""
    seed = browser_export._load_seed_categories()
    committed = json.loads(browser_export.HPO_CATEGORY_CACHE_PATH.read_text())
    assert seed and len(seed) == len(committed)
