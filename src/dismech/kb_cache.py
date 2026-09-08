"""Process-wide cache of parsed KB YAML documents.

Many code paths walk ``kb/disorders/`` and parse every file to build a small
index: disorder name to page, ``model_id`` to the entry that curates it, MONDO
term to disorder, the set of evidence snippets. On the current corpus (about
2,700 files, 158 MB of YAML) one such walk costs about 17 s of parsing, and the
test suite alone performed a dozen of them per run (#11003). This module keeps
one parsed copy of each file per process, so the second and later walks pay a
read and a hash instead of a parse.

Contract
--------
* :func:`load_document` returns the parsed document for a path. The object is
  **shared**: treat it as read-only. Code that annotates or edits a document
  must load its own copy with :func:`dismech.yaml_io.safe_load_path` (or
  ``copy.deepcopy`` the shared one). The renderer's per-page load does exactly
  that, because it decorates the document in place.
* Freshness is decided by content, not by mtime. Every call reads the file's
  bytes and hashes them; a changed file is re-parsed. Reading and hashing the
  whole corpus costs about a quarter of a second against 17 s of parsing, and it
  cannot be fooled by a rewrite that lands inside the filesystem's timestamp
  granularity, which a tmp_path-based test can do.
* Memory: the parsed disorder corpus is roughly 450 MB per process. Under
  ``pytest -n 6`` that is per worker. Set ``DISMECH_KB_CACHE=0`` to turn caching
  off; every call then parses afresh and nothing is retained.

Caching only pays off when a process walks the corpus more than once, and the
cost when it does not is real -- measured on this corpus, ``check_snippet_length``
(one walk) goes from 17.1 s / 34 MB to 20.5 s / 522 MB, while
``check_environmental_evidence`` (two walks) goes from 28.0 s / 34 MB down to
18.3 s / 522 MB. A single-walk CLI should therefore call :func:`default_off` in
its ``main`` -- see that function for why it belongs there and not at import.
"""

from __future__ import annotations

import hashlib
import os
from collections.abc import Iterator
from pathlib import Path
from typing import Any

from dismech.yaml_io import safe_load

__all__ = [
    "cache_size",
    "clear_cache",
    "default_off",
    "iter_documents",
    "load_document",
]

#: absolute (but not symlink-resolved) path -> (content digest, parsed
#: document). Resolving would cost a stat per call to merge the entries for
#: two paths reaching one file; the digest makes that a duplicate rather
#: than a stale answer, so it is not worth paying for on every load.
_CACHE: dict[str, tuple[bytes, Any]] = {}


def _enabled() -> bool:
    return os.environ.get("DISMECH_KB_CACHE", "1").strip().lower() not in {
        "0",
        "false",
        "no",
        "off",
    }


def default_off() -> None:
    """Default this process to no caching, unless the operator asked for it.

    For a CLI that walks the corpus exactly once there are no cache hits to
    collect, so the cache is pure cost: an extra hash per file and the whole
    parsed corpus retained. Call this from ``main`` -- **not** at import, because
    pytest imports these scripts' ``scan_repo`` functions directly and runs
    several of them in one process, which is exactly the case caching is for.

    Uses ``setdefault``, so an explicit ``DISMECH_KB_CACHE`` in the environment
    still wins.
    """
    os.environ.setdefault("DISMECH_KB_CACHE", "0")


def load_document(path: str | os.PathLike[str]) -> Any:
    """Return the parsed YAML document at ``path``, shared and read-only.

    Reads the file, hashes its bytes, and returns the cached parse when the
    digest matches the one stored for that path. Otherwise parses, stores, and
    returns. An empty file parses to ``None`` and is cached as such.
    """
    file_path = Path(path)
    raw = file_path.read_bytes()
    if not _enabled():
        return safe_load(raw)
    key = os.path.abspath(file_path)
    digest = hashlib.blake2b(raw, digest_size=16).digest()
    cached = _CACHE.get(key)
    if cached is not None and cached[0] == digest:
        return cached[1]
    document = safe_load(raw)
    _CACHE[key] = (digest, document)
    return document


def iter_documents(
    directory: str | os.PathLike[str],
    pattern: str = "*.yaml",
    *,
    skip_history: bool = True,
) -> Iterator[tuple[Path, Any]]:
    """Yield ``(path, document)`` for every file matching ``pattern`` in ``directory``.

    Sorted by path. ``*.history.yaml`` snapshots are skipped unless
    ``skip_history`` is false. Documents come from :func:`load_document` and are
    shared, so the same read-only contract applies.
    """
    for file_path in sorted(Path(directory).glob(pattern)):
        if skip_history and file_path.name.endswith(".history.yaml"):
            continue
        yield file_path, load_document(file_path)


def clear_cache() -> None:
    """Forget every cached document (tests, or to release memory)."""
    _CACHE.clear()


def cache_size() -> int:
    """Number of documents currently held."""
    return len(_CACHE)
