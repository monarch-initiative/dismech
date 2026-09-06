"""Shared pytest fixtures.

The one thing here is the OAK hierarchy stub. Rendering a disorder page walks
`hierarchical_parents` up the ICD10CM/NCIT tree for every mapping and labels each
node, which costs roughly 75 s per page against the local OAK SQLite builds. The
PDAC render test alone took 107 s of the fast suite because of it (issue #11186).

Two things now keep that out of the fast suite. `cache/<prefix>/hierarchy.csv`
answers the lookup for every CURIE mapped in `kb/`, and this fixture stubs the
adapter factory so even a cache miss cannot reach a real database.

The fixture is autouse and exempts tests marked `kb_data`, rather than being
opt-in per test, because opt-in only protects the tests that remember to ask:
a render test added later would silently reintroduce the cost. The marked test
in `tests/test_render_hierarchy_cache.py` is what still exercises the real
adapter.
"""

from __future__ import annotations

import pytest

# A small slice of the real NCIT and ICD10CM ancestries, enough for the render
# tests to build a breadcrumb. Each entry maps a CURIE to its parent; a CURIE
# absent from the map has no parent, so the walk stops there.
STUB_PARENTS: dict[str, str] = {
    # NCIT:C9120 (Pancreatic Ductal Adenocarcinoma) up to the disease root.
    "NCIT:C9120": "NCIT:C8294",
    "NCIT:C8294": "NCIT:C3850",
    "NCIT:C3850": "NCIT:C4978",
    "NCIT:C4978": "NCIT:C3262",
    "NCIT:C3262": "NCIT:C7057",
    # ICD10CM chapter spine.
    "ICD10CM:C25.0": "ICD10CM:C25",
    "ICD10CM:C25": "ICD10CM:C00-D49",
    "ICD10CM:C00-D49": "ICD10CM:ICD-10-CM",
}

STUB_LABELS: dict[str, str] = {
    "NCIT:C9120": "Pancreatic Ductal Adenocarcinoma",
    "NCIT:C8294": "Pancreatic Carcinoma",
    "NCIT:C3850": "Pancreatic Neoplasm",
    "NCIT:C4978": "Digestive System Neoplasm",
    "NCIT:C3262": "Neoplasm",
    "NCIT:C7057": "Disease, Disorder or Finding",
    "ICD10CM:C25.0": "Malignant neoplasm of head of pancreas",
    "ICD10CM:C25": "Malignant neoplasm of pancreas",
    "ICD10CM:C00-D49": "Neoplasms",
    "ICD10CM:ICD-10-CM": "ICD-10-CM",
}


class StubHierarchyAdapter:
    """Stands in for an OAK adapter over the fixed ancestry above."""

    def hierarchical_parents(self, term_id: str) -> list[str]:
        parent = STUB_PARENTS.get(term_id)
        return [parent] if parent else []

    def label(self, term_id: str) -> str:
        return STUB_LABELS.get(term_id, term_id)


@pytest.fixture(autouse=True)
def stub_oak_hierarchy(request, monkeypatch):
    """Keep mapping-breadcrumb lookups off the real OAK databases.

    Also clears the render module's per-process memo and the committed-cache
    reader between tests, so a path resolved under the stub cannot leak into a
    test that expects the real adapter, or the reverse.
    """
    from dismech import hierarchy_cache, render

    def clear_caches() -> None:
        # On teardown the monkeypatch is still in place — its finalizer runs
        # after this fixture's — so `_get_oak_adapter` may currently be the
        # plain stub lambda rather than the memoised original.
        for target in (
            render._resolve_hierarchy_path,
            render._get_oak_adapter,
            hierarchy_cache.load_hierarchy_cache,
        ):
            clear = getattr(target, "cache_clear", None)
            if clear is not None:
                clear()

    clear_caches()

    if request.node.get_closest_marker("kb_data") is None:
        monkeypatch.setattr(
            render, "_get_oak_adapter", lambda _adapter_str: StubHierarchyAdapter()
        )

    yield

    clear_caches()
