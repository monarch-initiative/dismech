#!/usr/bin/env python3
"""Guard against NUL bytes in ``references_cache/`` (#12543).

A NUL byte makes ``grep`` classify a file as binary: it prints ``binary file
matches`` on stderr and drops the file from its output. Every grep-based count
over ``references_cache/`` therefore undercounted silently, and two reasonable
measurements of the same directory disagreed during review of #12535 without
either one saying data had been dropped.

The NULs come from PDF text extraction (``pypdf``, inside
linkml-reference-validator): a glyph whose font has no ToUnicode entry is
emitted as U+0000. It is usually an ``fi``/``fl``/``ffi`` ligature, sometimes a
digit or a minus sign. ``scripts/repair_reference_cache_nuls.py`` restores the
ligatures it can identify and replaces the rest with U+FFFD. Until the extractor
is fixed upstream, a newly fetched PDF can bring NULs back, so this runs as an
ungated, whole-tree CI step: the PRs that add a cache file touch only ``kb/`` and
``references_cache/``, which no path-filtered pytest lane selects -- the same
reason ``check_case_collisions.py`` runs that way.

Usage
-----
    python scripts/check_reference_cache_nul_bytes.py      # gate: fail on any NUL
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE_DIR = ROOT / "references_cache"


def nul_counts(cache_dir: Path = CACHE_DIR) -> dict[Path, int]:
    """Map each cache file containing a NUL byte to its NUL count."""
    found: dict[Path, int] = {}
    for path in sorted(cache_dir.glob("*.md")):
        count = path.read_bytes().count(b"\x00")
        if count:
            found[path] = count
    return found


def main() -> int:
    if not CACHE_DIR.is_dir():
        print(f"no {CACHE_DIR.relative_to(ROOT)}/ directory; nothing to check.")
        return 0
    total = sum(1 for _ in CACHE_DIR.glob("*.md"))
    found = nul_counts()
    if not found:
        print(f"OK: no NUL bytes in {total} references_cache file(s).")
        return 0

    print("references_cache files containing NUL bytes.\n")
    print("grep treats these files as binary and silently omits them from its")
    print("output. They come from PDF text extraction emitting an unmapped glyph,")
    print("usually an fi/fl ligature, as U+0000. Repair them with")
    print("  uv run python scripts/repair_reference_cache_nuls.py --apply")
    print("which restores identifiable ligatures and replaces the rest with U+FFFD.\n")
    for path, count in found.items():
        print(f"  {path.relative_to(ROOT)}: {count} NUL byte(s)")
    print(f"\n{len(found)} file(s) with NUL bytes among {total} cache file(s).")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
