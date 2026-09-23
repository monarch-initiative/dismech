"""Find a DOI's reference-cache file whatever capitalization the DOI was written in.

DOI suffixes are case-insensitive (Crossref: "Suffixes are case insensitive, so
10.1006/abc is the same in the system as 10.1006/ABC"), but a cache filename is
derived from the DOI exactly as written. So ``DOI:10.1172/JCI89626`` and
``DOI:10.1172/jci89626`` name two different files, and on a case-sensitive
filesystem -- Linux, which is CI and the curation agents -- fetching the second
spelling writes a second copy of the same paper (#9112). On macOS the two names
are one file, so the copy never appears locally and only shows up in a commit.

The fix is to look for an existing file by case-folded name before using the name
as written. Nothing is renamed: an existing file keeps its capitalization, and a
DOI with no cache file yet is saved as written. Choosing one capitalization for
the whole cache is a separate decision, and doing it before the lookup is
case-insensitive would make every mixed-case DOI cited in ``kb/`` miss its file
and be fetched again (see #9112).
"""

from __future__ import annotations

import os
from pathlib import Path

DOI_CACHE_PREFIX = "DOI_"

# One case-folded filename index per cache directory, built on first use.
# ``references_cache/`` holds tens of thousands of files and a validation run
# looks up thousands of references, so the directory is listed once per process.
_INDEXES: dict[Path, dict[str, str]] = {}


def is_doi_reference(reference_id: str) -> bool:
    """True for a ``DOI:`` reference id, whatever the prefix's capitalization."""
    return reference_id[:4].upper() == "DOI:"


def _index_for(cache_dir: Path) -> dict[str, str]:
    index = _INDEXES.get(cache_dir)
    if index is None:
        index = {}
        try:
            with os.scandir(cache_dir) as entries:
                for entry in entries:
                    name = entry.name
                    if name[: len(DOI_CACHE_PREFIX)].upper() == DOI_CACHE_PREFIX:
                        index.setdefault(name.casefold(), name)
        except OSError:
            pass  # a cache directory that does not exist yet has no files to reuse
        _INDEXES[cache_dir] = index
    return index


def resolve_doi_cache_path(path: Path) -> Path:
    """Return the existing cache file matching ``path`` case-insensitively.

    ``path`` is the path derived from the DOI as written. If a file whose name
    differs only in capitalization already exists in the same directory, that
    file's path is returned; otherwise ``path`` itself is returned and recorded,
    so a later lookup of the same DOI in another capitalization in this process
    lands on the same file once it has been written.
    """
    cache_dir = path.parent
    index = _index_for(cache_dir)
    folded = path.name.casefold()
    existing = index.get(folded)
    if existing is not None and existing != path.name:
        candidate = cache_dir / existing
        if candidate.exists():
            return candidate
    index[folded] = path.name
    return path


def reset_indexes() -> None:
    """Forget every directory index (for tests that create files mid-process)."""
    _INDEXES.clear()
