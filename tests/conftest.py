"""Shared pytest fixtures.

The one thing here is the OAK hierarchy stub. Rendering a disorder page walks
`hierarchical_parents` up the ICD10CM/NCIT tree for every mapping and labels each
node, which costs roughly 75 s per page against the local OAK SQLite builds. The
PDAC render test alone took 107 s of the fast suite because of it (issue #11186).

Two things now keep that out of the fast suite. `cache/<prefix>/hierarchy.csv`
answers the lookup for every CURIE mapped in `kb/`, and this fixture stubs the
adapter factory so even a cache miss cannot reach a real database.

The fixture is autouse and exempts tests marked `kb_data` or `oak_db`, rather
than being opt-in per test, because opt-in only protects the tests that remember
to ask: a render test added later would silently reintroduce the cost. The
`oak_db`-marked tests in `tests/test_render_hierarchy_cache.py` are what still
exercise the real adapter.

**The stub is adapter-string-aware, and must stay that way.** `_get_oak_adapter`
is not hierarchy-only — `render` also opens `sqlite:obo:mondo` for MONDO
descendant and label lookups. Returning a hierarchy stub for that string hands
those call sites a truthy object with no `descendants()` method, which their own
`except Exception` swallows, so `_exact_mondo_descendant_terms` stops taking its
`adapter is None` branch and silently drops its "MONDO descendant lookup
unavailable." warning. That is a changed rendered result that nothing asserts on.
So the stub answers only for the adapter strings in `STRICT_HIERARCHIES` and
delegates every other string to the real factory.

Delegation rather than returning `None`, deliberately. `None` looks tempting —
those call sites handle it, and it would keep the suite off every real database.
But it is not a no-op either: it makes `_exact_mondo_descendant_terms` take its
`adapter is None` branch, and `test_render_all_groupings_builds_index_from_grouping_yaml`
asserts on a coverage string that branch does not emit. A fixture whose job is to
neutralise the *hierarchy* lookups should leave every other lookup exactly as it
was, so it delegates. That costs the fast suite nothing measurable: the 75 s/page
problem was the ICD10CM/NCIT `hierarchical_parents` walks, and the MONDO calls
behind this factory are `lru_cache`d and few.
"""

from __future__ import annotations

import pytest

# The real committed ancestries for two CURIEs, lifted verbatim out of
# `cache/<prefix>/hierarchy.csv` so the stub agrees with what OAK actually
# returns rather than inventing a plausible-looking chain. Each entry maps a
# CURIE to its parent; a CURIE absent from the map has no parent, so the walk
# stops there.
STUB_PARENTS: dict[str, str] = {
    # NCIT:C9120 (Pancreatic Ductal Adenocarcinoma) up to the disease root.
    "NCIT:C9120": "NCIT:C8294",
    "NCIT:C8294": "NCIT:C210140",
    "NCIT:C210140": "NCIT:C2852",
    "NCIT:C2852": "NCIT:C2916",
    "NCIT:C2916": "NCIT:C3709",
    "NCIT:C3709": "NCIT:C4741",
    "NCIT:C4741": "NCIT:C3262",
    "NCIT:C3262": "NCIT:C2991",
    "NCIT:C2991": "NCIT:C7057",
    # ICD10CM:C22.0, which tops out at its chapter rather than at the root
    # `STRICT_HIERARCHIES` declares. See the note in CLAUDE.md.
    "ICD10CM:C22.0": "ICD10CM:C22",
    "ICD10CM:C22": "ICD10CM:C15-C26",
    "ICD10CM:C15-C26": "ICD10CM:C00-D49",
}

STUB_LABELS: dict[str, str] = {
    "NCIT:C9120": "Pancreatic Ductal Adenocarcinoma",
    "NCIT:C8294": "Pancreatic Adenocarcinoma",
    "NCIT:C210140": "Digestive System Adenocarcinoma",
    "NCIT:C2852": "Adenocarcinoma",
    "NCIT:C2916": "Carcinoma",
    "NCIT:C3709": "Epithelial Neoplasm",
    "NCIT:C4741": "Neoplasm by Morphology",
    "NCIT:C3262": "Neoplasm",
    "NCIT:C2991": "Disease or Disorder",
    "NCIT:C7057": "Disease, Disorder or Finding",
    "ICD10CM:C22.0": "Liver cell carcinoma",
    "ICD10CM:C22": "Malignant neoplasm of liver and intrahepatic bile ducts",
    "ICD10CM:C15-C26": "Malignant neoplasms of digestive organs (C15-C26)",
    "ICD10CM:C00-D49": "Neoplasms (C00-D49)",
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

    Also clears the render module's per-process memo, the committed-cache
    reader, and the two MONDO lookup caches that sit behind the same adapter
    factory, so a value resolved under the stub cannot leak into a test that
    expects the real adapter, or the reverse.
    """
    from dismech import hierarchy_cache, render

    real_get_oak_adapter = render._get_oak_adapter
    hierarchy_adapters = {h["adapter"] for h in render.STRICT_HIERARCHIES.values()}

    def clear_caches() -> None:
        # On teardown the monkeypatch is still in place — its finalizer runs
        # after this fixture's — so `_get_oak_adapter` may currently be the
        # plain stub function rather than the memoised original.
        for target in (
            render._resolve_hierarchy_path,
            render._get_oak_adapter,
            render._cached_mondo_descendants,
            render._cached_mondo_label,
            hierarchy_cache.load_hierarchy_cache,
        ):
            clear = getattr(target, "cache_clear", None)
            if clear is not None:
                clear()

    clear_caches()

    exempt = any(
        request.node.get_closest_marker(m) is not None for m in ("kb_data", "oak_db")
    )
    if not exempt:

        def _stub_factory(adapter_str: str):
            if adapter_str in hierarchy_adapters:
                return StubHierarchyAdapter()
            return real_get_oak_adapter(adapter_str)

        monkeypatch.setattr(render, "_get_oak_adapter", _stub_factory)

    yield

    clear_caches()
