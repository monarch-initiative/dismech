"""Guard against case-duplicate paths in the git index.

macOS and Windows checkouts are case-insensitive: when the index tracks both
``Foo.md`` and ``foo.md``, only one of them can exist on disk, so every
contributor on those platforms sees a permanent phantom modification that
cannot be discarded or committed away.

This has now been introduced three times — schema docs (#598), a disorder entry
and a rendered page (#1305), and reference-cache files for the same DOI in two
casings (the `DOI_10.1056_NEJMoa2307952` / `DOI_10.1056_nejmoa2307952` pair).
Each time it was cleaned up by hand. This test makes the fourth time fail in
CI, on the pull request that adds it, instead of on someone's laptop.
"""

import subprocess
from collections import defaultdict
from pathlib import Path

import pytest

ROOT_DIR = Path(__file__).parent.parent


def _tracked_paths() -> list[str]:
    try:
        result = subprocess.run(
            ["git", "ls-files", "-z"],
            cwd=ROOT_DIR,
            capture_output=True,
            check=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError) as exc:  # not a git checkout
        pytest.skip(f"git ls-files unavailable: {exc}")
    return [path for path in result.stdout.split("\0") if path]


def test_no_case_duplicate_paths_in_git_index():
    by_folded = defaultdict(list)
    for path in _tracked_paths():
        by_folded[path.casefold()].append(path)

    collisions = {
        folded: sorted(paths) for folded, paths in by_folded.items() if len(paths) > 1
    }

    assert not collisions, (
        "The git index tracks paths that differ only in case. On a "
        "case-insensitive filesystem (macOS, Windows) these show up as phantom "
        "modifications that cannot be discarded.\n\n"
        + "\n".join(" <-> ".join(paths) for paths in collisions.values())
        + "\n\nFix: keep the original casing and drop the other index entry with "
        "`git rm --cached <path>` (which leaves the file on disk untouched)."
    )
