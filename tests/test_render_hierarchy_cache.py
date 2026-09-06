"""Tests for the mapping-breadcrumb hierarchy cache (issue #11186).

Rendering used to walk `hierarchical_parents` against the local OAK SQLite
builds for every ICD10CM/NCIT mapping, at roughly 75 s per page. Three things
now avoid that, and each is covered here: a committed per-prefix cache, a
per-process memo over the resolved path, and a stub adapter in the fast suite.
"""

from __future__ import annotations

import csv
from pathlib import Path

import pytest

from dismech import hierarchy_cache
from dismech.render import (
    STRICT_HIERARCHIES,
    _build_hierarchy_path,
    _get_oak_adapter,
    _resolve_hierarchy_path,
)

REPO_ROOT = Path(__file__).resolve().parents[1]


# --- the committed cache ----------------------------------------------------


def test_cache_lookup_returns_none_when_file_is_absent(tmp_path: Path) -> None:
    """A missing cache is a miss, not an error: the caller falls back to OAK."""
    assert hierarchy_cache.lookup("NCIT", "NCIT:C9120", str(tmp_path)) is None


def test_cache_round_trips_a_path(tmp_path: Path) -> None:
    (tmp_path / "ncit").mkdir()
    (tmp_path / "ncit" / "hierarchy.csv").write_text(
        "curie,ancestor_curies,ancestor_labels,retrieved_at\n"
        "NCIT:C9120,NCIT:C7057|NCIT:C9120,Disease|PDAC,2026-01-01T00:00:00+00:00\n",
        encoding="utf-8",
    )
    assert hierarchy_cache.lookup("NCIT", "NCIT:C9120", str(tmp_path)) == (
        ("NCIT:C7057", "Disease"),
        ("NCIT:C9120", "PDAC"),
    )


def test_malformed_rows_are_skipped_rather_than_trusted(tmp_path: Path) -> None:
    """A row whose CURIE and label counts disagree cannot be zipped safely."""
    (tmp_path / "ncit").mkdir()
    (tmp_path / "ncit" / "hierarchy.csv").write_text(
        "curie,ancestor_curies,ancestor_labels,retrieved_at\n"
        "NCIT:C1,NCIT:A|NCIT:C1,OnlyOneLabel,2026-01-01T00:00:00+00:00\n"
        "NCIT:C2,NCIT:A|NCIT:C2,A|Two,2026-01-01T00:00:00+00:00\n",
        encoding="utf-8",
    )
    assert hierarchy_cache.lookup("NCIT", "NCIT:C1", str(tmp_path)) is None
    assert hierarchy_cache.lookup("NCIT", "NCIT:C2", str(tmp_path)) is not None


def test_join_field_rejects_a_value_containing_the_separator() -> None:
    """The builder must fail loudly rather than write an ambiguous row."""
    with pytest.raises(ValueError, match="path separator"):
        hierarchy_cache.join_field(["fine", "not|fine"])


def test_committed_caches_are_well_formed_and_sorted() -> None:
    """Every committed hierarchy cache parses, is sorted, and is self-consistent."""
    for prefix in STRICT_HIERARCHIES:
        path = hierarchy_cache.cache_path(prefix)
        if not path.exists():
            continue
        rows = list(csv.DictReader(path.read_text(encoding="utf-8").splitlines()))
        assert rows, f"{path} is empty"

        curies = [row["curie"] for row in rows]
        assert curies == sorted(curies), f"{path} is not sorted by CURIE"
        assert len(curies) == len(set(curies)), f"{path} has duplicate CURIEs"

        for row in rows:
            ancestors = row["ancestor_curies"].split(hierarchy_cache.PATH_SEPARATOR)
            labels = row["ancestor_labels"].split(hierarchy_cache.PATH_SEPARATOR)
            assert len(ancestors) == len(labels), f"{path}: {row['curie']} is ragged"
            assert ancestors[-1] == row["curie"], (
                f"{path}: {row['curie']} path does not end at its own CURIE"
            )
            assert all(ancestors), f"{path}: {row['curie']} has an empty path node"


def test_ncit_paths_reach_the_configured_root() -> None:
    """NCIT walks terminate at the root `STRICT_HIERARCHIES` declares."""
    cached = hierarchy_cache.load_hierarchy_cache("NCIT")
    if not cached:
        pytest.skip("no committed NCIT hierarchy cache")
    root = STRICT_HIERARCHIES["NCIT"]["root"]
    assert all(path[0][0] == root for path in cached.values())


def test_icd10cm_paths_stop_at_a_chapter_not_at_the_configured_root() -> None:
    """ICD10CM breadcrumbs start at a chapter, and that is the honest answer.

    `STRICT_HIERARCHIES` declares `ICD10CM:ICD-10-CM` as the root, but in the
    `sqlite:obo:icd10cm` build that node has no incoming hierarchy: chapter codes
    such as `ICD10CM:C00-D49` return no `hierarchical_parents`, so the walk
    terminates there and never reaches the declared root. None of the 47 mapped
    CURIEs reach it.

    This predates the cache — the live renderer produced the same chapter-topped
    breadcrumbs — so the cache is faithful to what OAK returns rather than wrong.
    The test pins the behaviour so that if a future ICD10CM build does connect
    the chapters to the root, the change is noticed rather than silently
    altering every ICD10CM breadcrumb.
    """
    cached = hierarchy_cache.load_hierarchy_cache("ICD10CM")
    if not cached:
        pytest.skip("no committed ICD10CM hierarchy cache")
    declared_root = STRICT_HIERARCHIES["ICD10CM"]["root"]
    tops = {path[0][0] for path in cached.values()}
    assert declared_root not in tops
    assert all(top.startswith("ICD10CM:") for top in tops)


# --- the per-process memo ---------------------------------------------------


def test_resolved_path_is_memoised_per_process(monkeypatch) -> None:
    """A second lookup of the same CURIE must not re-query the adapter.

    This is what makes `render_all` cheap: one walk per distinct CURIE across
    the whole build rather than one per page that mentions it.
    """
    calls: list[str] = []

    class CountingAdapter:
        def hierarchical_parents(self, term_id: str) -> list[str]:
            calls.append(term_id)
            return [] if term_id == "NCIT:C7057" else ["NCIT:C7057"]

        def label(self, term_id: str) -> str:
            return f"label for {term_id}"

    import dismech.render as render

    monkeypatch.setattr(render, "_get_oak_adapter", lambda _s: CountingAdapter())
    # Force the OAK path rather than a committed-cache hit.
    monkeypatch.setattr(hierarchy_cache, "lookup", lambda *_a, **_k: None)
    render._resolve_hierarchy_path.cache_clear()

    first = render._resolve_hierarchy_path("NCIT", "NCIT:C0000001")
    calls_after_first = len(calls)
    second = render._resolve_hierarchy_path("NCIT", "NCIT:C0000001")

    assert first == second
    assert first  # a path was resolved, so the memo is not caching a trivial miss
    assert len(calls) == calls_after_first, "adapter was queried twice for one CURIE"


def test_unresolvable_terms_are_memoised_too(monkeypatch) -> None:
    """A term OAK cannot resolve must not be re-queried on every later page."""
    calls: list[str] = []

    class BrokenAdapter:
        def hierarchical_parents(self, term_id: str):
            calls.append(term_id)
            raise RuntimeError("database disk image is malformed")

        def label(self, term_id: str) -> str:
            return term_id

    import dismech.render as render

    monkeypatch.setattr(render, "_get_oak_adapter", lambda _s: BrokenAdapter())
    monkeypatch.setattr(hierarchy_cache, "lookup", lambda *_a, **_k: None)
    render._resolve_hierarchy_path.cache_clear()

    assert render._resolve_hierarchy_path("NCIT", "NCIT:C0000002") == ()
    assert render._resolve_hierarchy_path("NCIT", "NCIT:C0000002") == ()
    assert len(calls) == 1


def test_cache_hit_short_circuits_the_adapter(monkeypatch) -> None:
    """A committed-cache hit must not open an adapter at all."""

    def explode(_adapter_str):  # pragma: no cover - must never run
        raise AssertionError("the adapter was opened despite a cache hit")

    import dismech.render as render

    monkeypatch.setattr(render, "_get_oak_adapter", explode)
    monkeypatch.setattr(
        hierarchy_cache, "lookup", lambda *_a, **_k: (("NCIT:C7057", "Disease"),)
    )
    render._resolve_hierarchy_path.cache_clear()

    assert render._resolve_hierarchy_path("NCIT", "NCIT:C9120") == (
        ("NCIT:C7057", "Disease"),
    )


# --- the real adapter -------------------------------------------------------


@pytest.mark.kb_data
def test_real_oak_adapter_resolves_a_known_ncit_path() -> None:
    """The one test that still exercises a real OAK walk.

    The fast suite stubs the adapter factory, so without this nothing would
    notice if the live lookup broke — a renderer that silently stopped
    producing breadcrumbs would still pass. Marked `kb_data` so it runs under
    `just test-kb` rather than on every developer save; skipped when the local
    SQLite build is absent, since that is an environment gap, not a defect.
    """
    hierarchy = STRICT_HIERARCHIES["NCIT"]
    adapter = _get_oak_adapter(hierarchy["adapter"])
    if adapter is None:
        pytest.skip(f"{hierarchy['adapter']} is not available in this environment")

    path = _build_hierarchy_path(adapter, "NCIT:C9120", hierarchy["root"])
    if not path:
        pytest.skip("local NCIT build could not resolve NCIT:C9120")

    assert path[0] == hierarchy["root"]
    assert path[-1] == "NCIT:C9120"
    assert len(path) > 1


@pytest.mark.kb_data
def test_committed_cache_agrees_with_the_live_adapter() -> None:
    """The committed cache must not drift from what OAK actually returns.

    A stale cache is worse than no cache: it renders a confidently wrong
    breadcrumb where a miss would merely be slow.
    """
    prefix = "NCIT"
    cached = hierarchy_cache.load_hierarchy_cache(prefix)
    if not cached:
        pytest.skip("no committed NCIT hierarchy cache to compare against")

    hierarchy = STRICT_HIERARCHIES[prefix]
    adapter = _get_oak_adapter(hierarchy["adapter"])
    if adapter is None:
        pytest.skip(f"{hierarchy['adapter']} is not available in this environment")

    curie = sorted(cached)[0]
    live = _build_hierarchy_path(adapter, curie, hierarchy["root"])
    if not live:
        pytest.skip(f"local build could not resolve {curie}")

    assert [node for node, _ in cached[curie]] == live


# --- end to end -------------------------------------------------------------


def test_render_uses_the_stub_and_still_emits_a_breadcrumb(tmp_path: Path) -> None:
    """With the autouse stub in place, a real page still renders a breadcrumb.

    Guards against "fixed the cost by silently dropping the feature".
    """
    from dismech.render import _augment_mapping_hierarchies

    disorder = {
        "mappings": {
            "ncit_mappings": [
                {"term": {"id": "NCIT:C9120", "label": "PDAC"}},
            ]
        }
    }
    _augment_mapping_hierarchies(disorder)

    breadcrumb = disorder["mappings"]["ncit_mappings"][0].get("hierarchy_path")
    assert breadcrumb, "no hierarchy_path was produced"
    assert breadcrumb[-1]["id"] == "NCIT:C9120"
    assert all("label" in node for node in breadcrumb)
