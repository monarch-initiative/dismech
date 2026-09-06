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


def test_rebuild_keeps_the_timestamp_on_unchanged_rows() -> None:
    """A rebuild must not restamp rows whose path did not move.

    The builder re-resolves every mapped CURIE on every run, so stamping them all
    with one fresh timestamp would turn a one-mapping addition into a whole-file
    diff, and make two PRs adding neighbouring CURIEs collide on every line. That
    is the shape of the `cache/dataset_accessions.json` problem recorded in
    CLAUDE.md, and `cache/<prefix>/terms.csv` avoids it by being incremental.
    """
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "build_hierarchy_cache", REPO_ROOT / "scripts" / "build_hierarchy_cache.py"
    )
    builder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(builder)

    previous = {
        "NCIT:C1": {
            "curie": "NCIT:C1",
            "ancestor_curies": "NCIT:A|NCIT:C1",
            "ancestor_labels": "Root|One",
            "retrieved_at": "2020-01-01T00:00:00+00:00",
        },
        "NCIT:C2": {
            "curie": "NCIT:C2",
            "ancestor_curies": "NCIT:A|NCIT:C2",
            "ancestor_labels": "Root|Two",
            "retrieved_at": "2020-01-01T00:00:00+00:00",
        },
    }
    resolved = {
        "NCIT:C1": [("NCIT:A", "Root"), ("NCIT:C1", "One")],
        # C2's label moved, so only this row should take the new timestamp.
        "NCIT:C2": [("NCIT:A", "Root"), ("NCIT:C2", "Two, renamed")],
        "NCIT:C3": [("NCIT:A", "Root"), ("NCIT:C3", "Three")],
    }
    now = "2099-01-01T00:00:00+00:00"
    rows = list(
        csv.DictReader(builder.render_csv(resolved, now, previous).splitlines())
    )
    stamps = {row["curie"]: row["retrieved_at"] for row in rows}

    assert stamps["NCIT:C1"] == "2020-01-01T00:00:00+00:00"
    assert stamps["NCIT:C2"] == now, "a changed row must be restamped"
    assert stamps["NCIT:C3"] == now, "a new row must be stamped"


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

    from dismech import render

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

    from dismech import render

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

    from dismech import render

    monkeypatch.setattr(render, "_get_oak_adapter", explode)
    monkeypatch.setattr(
        hierarchy_cache, "lookup", lambda *_a, **_k: (("NCIT:C7057", "Disease"),)
    )
    render._resolve_hierarchy_path.cache_clear()

    assert render._resolve_hierarchy_path("NCIT", "NCIT:C9120") == (
        ("NCIT:C7057", "Disease"),
    )


# --- the real adapter -------------------------------------------------------


@pytest.mark.oak_db
def test_real_oak_adapter_resolves_a_known_ncit_path() -> None:
    """The one test that still exercises a real OAK walk.

    The fast suite stubs the adapter factory, so without this nothing would
    notice if the live lookup broke — a renderer that silently stopped
    producing breadcrumbs would still pass.

    **This runs on a developer machine and nowhere else.** No CI workflow
    fetches the OAK SQLite builds, so the skip below is taken in every CI lane
    including the nightly sweep. `just check-hierarchy-cache` is the offline
    coverage check that does run there.
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


class _MemoisingAdapter:
    """Answers each parent lookup once, so a whole-prefix sweep stays affordable.

    Terms in one vocabulary share most of their upper ancestry, so walking every
    cached CURIE independently re-asks the same questions. Against the 2.7 GB
    NCIT build a single `hierarchical_parents` call costs seconds, which is the
    difference between this test taking minutes and taking seconds. The builder
    carries the same wrapper for the same reason.
    """

    def __init__(self, adapter) -> None:
        self._adapter = adapter
        self._parents: dict[str, list[str]] = {}

    def hierarchical_parents(self, term_id: str) -> list[str]:
        if term_id not in self._parents:
            self._parents[term_id] = list(self._adapter.hierarchical_parents(term_id))
        return self._parents[term_id]

    def label(self, term_id: str) -> str:
        return self._adapter.label(term_id)


@pytest.mark.oak_db
@pytest.mark.parametrize("prefix", sorted(STRICT_HIERARCHIES))
def test_committed_cache_agrees_with_the_live_adapter(prefix: str) -> None:
    """Every committed row must match what OAK actually returns, in both prefixes.

    A stale cache is worse than no cache: it renders a confidently wrong
    breadcrumb where a miss would merely be slow. Checking one CURIE would leave
    the other 87 rows unverified, and opening the adapter is the expensive part,
    so this compares the whole prefix once it is paying for that.

    Local-only, like its neighbour above: no CI workflow fetches the OAK builds.
    Budget about 15 minutes for the pair against the local ICD10CM and NCIT
    builds; the memoisation below is what keeps it to that rather than hours.
    """
    cached = hierarchy_cache.load_hierarchy_cache(prefix)
    if not cached:
        pytest.skip(f"no committed {prefix} hierarchy cache to compare against")

    hierarchy = STRICT_HIERARCHIES[prefix]
    raw = _get_oak_adapter(hierarchy["adapter"])
    if raw is None:
        pytest.skip(f"{hierarchy['adapter']} is not available in this environment")
    adapter = _MemoisingAdapter(raw)

    mismatches = []
    for curie in sorted(cached):
        live = _build_hierarchy_path(adapter, curie, hierarchy["root"])
        if not live:
            mismatches.append(f"{curie}: cached, but the live build resolves nothing")
            continue
        stored = [node for node, _ in cached[curie]]
        if stored != live:
            mismatches.append(f"{curie}: cached {stored} != live {live}")

    assert not mismatches, (
        "committed cache has drifted from the ontology:\n" + "\n".join(mismatches)
    )


# --- end to end -------------------------------------------------------------


def test_render_uses_the_stub_and_still_emits_a_breadcrumb(monkeypatch) -> None:
    """With the autouse stub in place, a real page still renders a breadcrumb.

    Guards against "fixed the cost by silently dropping the feature". The
    committed-cache lookup is forced to miss, because `NCIT:C9120` is in
    `cache/ncit/hierarchy.csv` and the cache hit would otherwise short-circuit
    before the adapter is ever consulted — so without this the test would pass
    identically with the autouse fixture deleted and would cover nothing.
    """
    from dismech.render import _augment_mapping_hierarchies

    monkeypatch.setattr(hierarchy_cache, "lookup", lambda *_a, **_k: None)

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
