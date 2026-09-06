"""Committed ancestor-path cache for the strict mapping hierarchies.

Rendering a disorder page draws a breadcrumb for each ICD10CM/NCIT mapping by
walking `hierarchical_parents` up to the vocabulary root and then labelling every
node on the way. Against the local OAK SQLite builds that is roughly 75 s per
page (issue #11186), which every developer pays on every fast-suite run.

The walk is deterministic: the same CURIE yields the same path until the
underlying ontology release changes. So it is cached here the same way term
labels are cached under `cache/<prefix>/terms.csv` — as a committed, derived,
authority-backed artifact.

Layout, one file per prefix beside the existing label cache:

    cache/<prefix>/hierarchy.csv
    curie,ancestor_curies,ancestor_labels,retrieved_at

`ancestor_curies` is the full root-to-term path, pipe-joined, and
`ancestor_labels` holds each of those nodes' labels in the same order. The path
is stored uncompacted; the renderer decides how much of it to show, so changing
that presentation choice does not invalidate the cache.

Like every other `cache/` artifact these files are derived and must never be
hand-edited — regenerate with `just build-hierarchy-cache`. A miss is not an
error: the renderer falls back to OAK, so an entry curated after the last cache
build still renders, just slowly.
"""

from __future__ import annotations

import csv
from functools import cache
from pathlib import Path

#: Field separator inside the two pipe-joined columns. A label containing this
#: character would make the row ambiguous, so the builder refuses to write one
#: rather than emitting a row that silently round-trips wrong.
PATH_SEPARATOR = "|"

CACHE_FILENAME = "hierarchy.csv"

CACHE_HEADER = ["curie", "ancestor_curies", "ancestor_labels", "retrieved_at"]


def cache_path(prefix: str, cache_root: Path | None = None) -> Path:
    """Return the hierarchy cache file for an ontology prefix."""
    root = cache_root if cache_root is not None else default_cache_root()
    return root / prefix.lower() / CACHE_FILENAME


def default_cache_root() -> Path:
    """Repository `cache/` directory."""
    return Path(__file__).resolve().parents[2] / "cache"


@cache
def load_hierarchy_cache(
    prefix: str, cache_root: str | None = None
) -> dict[str, tuple[tuple[str, str], ...]]:
    """Load one prefix's cache as `{curie: ((curie, label), ...)}`.

    Returns an empty mapping when the file is absent or unreadable — the caller
    treats that as a miss and falls back to a live lookup, so a missing cache
    degrades speed and never correctness.
    """
    root = Path(cache_root) if cache_root is not None else None
    path = cache_path(prefix, root)
    try:
        text = path.read_text(encoding="utf-8")
    except (FileNotFoundError, NotADirectoryError, OSError):
        return {}

    entries: dict[str, tuple[tuple[str, str], ...]] = {}
    for row in csv.DictReader(text.splitlines()):
        curie = (row.get("curie") or "").strip()
        if not curie:
            continue
        curies = _split(row.get("ancestor_curies"))
        labels = _split(row.get("ancestor_labels"))
        if not curies or len(curies) != len(labels):
            # A malformed row is skipped rather than trusted; the live lookup
            # will supply the path instead.
            continue
        entries[curie] = tuple(zip(curies, labels))
    return entries


def lookup(
    prefix: str, curie: str, cache_root: str | None = None
) -> tuple[tuple[str, str], ...] | None:
    """Return the cached root-to-term path, or None on a miss."""
    return load_hierarchy_cache(prefix, cache_root).get(curie)


def _split(value: str | None) -> list[str]:
    if not value:
        return []
    return value.split(PATH_SEPARATOR)


def join_field(values: list[str]) -> str:
    """Join one path column, rejecting values that would corrupt the row."""
    for value in values:
        if PATH_SEPARATOR in value:
            raise ValueError(
                f"value contains the {PATH_SEPARATOR!r} path separator and "
                f"cannot be stored in the hierarchy cache: {value!r}"
            )
    return PATH_SEPARATOR.join(values)
