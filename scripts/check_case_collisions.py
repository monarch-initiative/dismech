#!/usr/bin/env python3
"""Guard against tracked paths that differ only in letter case.

macOS and Windows use case-insensitive filesystems by default. When git tracks
both ``references_cache/DOI_10.1172_JCI89626.md`` and
``references_cache/DOI_10.1172_jci89626.md``, only one file can exist on disk,
so git compares that one file against both index entries and reports one of
them as modified forever. No ``git checkout``, ``git restore`` or ``git stash``
clears it, and ``git rebase`` refuses to run on the dirty tree. On Linux and in
CI both files coexist and nothing looks wrong.

Why this needs a whole-repo sweep
---------------------------------
This has been cleaned up by hand four times: schema docs (#565, #598), a
disorder entry and its page (#1305, #9540), and 17 pairs of DOI reference-cache
files (#11204). A guard was proposed each time and never landed; the last one
(#9114) was closed unmerged. The PRs that add a collision are usually curation
PRs touching only ``kb/`` and ``references_cache/``, which no ``src/``/``tests/``
path filter selects, so this runs as an ungated CI step rather than only as a
test -- the same reason ``check_duplicate_yaml_keys.py`` does.

The recurring source is DOI capitalization: a DOI resolves case-insensitively,
but the reference fetcher derives the cache filename from the DOI exactly as it
was written (#9112), and several scripts lowercase a DOI first (#11903). Fixing
those write paths is tracked separately; this check stops the result from being
committed.

Usage
-----
    python scripts/check_case_collisions.py      # gate: fail on any collision
"""
from __future__ import annotations

import subprocess
import sys
from collections import defaultdict
from collections.abc import Iterable
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOI_CACHE_PREFIX = "references_cache/DOI_"


def find_case_collisions(paths: Iterable[str]) -> list[list[str]]:
    """Return groups of two or more paths that are equal after case-folding.

    Each group is sorted, and groups are ordered by their first path.
    """
    by_folded: dict[str, list[str]] = defaultdict(list)
    for path in paths:
        by_folded[path.casefold()].append(path)
    return sorted(sorted(group) for group in by_folded.values() if len(group) > 1)


def tracked_paths(root: Path = ROOT) -> list[str]:
    """Every path in the git index, as git spells it."""
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=root,
        capture_output=True,
        check=True,
        text=True,
    )
    return [path for path in result.stdout.split("\0") if path]


def main() -> int:
    try:
        paths = tracked_paths()
    except (OSError, subprocess.CalledProcessError) as exc:
        print(f"could not list tracked files with `git ls-files`: {exc}", file=sys.stderr)
        return 1

    collisions = find_case_collisions(paths)
    if not collisions:
        print(f"OK: no case-colliding paths among {len(paths)} tracked file(s).")
        return 0

    print("Tracked paths that differ only in letter case.\n")
    print("On a case-insensitive filesystem (the macOS and Windows default) only")
    print("one file of each group can exist, so one path always shows as modified")
    print("and blocks `git rebase`. Keep one path per group and remove the others")
    print("from the index with `git rm --cached <path>`.\n")
    for group in collisions:
        print("  " + "  <->  ".join(group))

    if any(all(p.startswith(DOI_CACHE_PREFIX) for p in group) for group in collisions):
        print("\nFor references_cache/DOI_* files: the same DOI was fetched in two")
        print("capitalizations (#9112). Keep the file whose name matches the")
        print("publisher's capitalization, and check nothing in kb/ cites the other.")

    print(f"\n{len(collisions)} colliding group(s) among {len(paths)} tracked file(s).")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
