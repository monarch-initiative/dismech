"""Guard test: no two tracked paths differ only in letter case (#11204).

See scripts/check_case_collisions.py for why a collision breaks macOS and
Windows checkouts, and why the check also runs as an ungated CI step.
"""
import subprocess

import pytest

from scripts.check_case_collisions import find_case_collisions, tracked_paths


def test_finds_paths_differing_only_in_case():
    paths = [
        "references_cache/DOI_10.1172_JCI89626.md",
        "references_cache/DOI_10.1172_jci89626.md",
        "references_cache/PMID_12345678.md",
    ]
    assert find_case_collisions(paths) == [
        [
            "references_cache/DOI_10.1172_JCI89626.md",
            "references_cache/DOI_10.1172_jci89626.md",
        ]
    ]


def test_directory_case_counts_as_a_collision():
    # `Docs/a.md` and `docs/a.md` are the same file on a case-insensitive disk.
    assert find_case_collisions(["Docs/a.md", "docs/a.md"]) == [["Docs/a.md", "docs/a.md"]]


def test_distinct_paths_are_not_reported():
    assert find_case_collisions(["kb/disorders/Asthma.yaml", "kb/disorders/Asthma_2.yaml"]) == []


def test_groups_of_three_are_reported_together():
    assert find_case_collisions(["A.md", "a.md", "a.MD"]) == [["A.md", "a.MD", "a.md"]]


def test_no_case_colliding_paths_in_git_index():
    try:
        paths = tracked_paths()
    except (OSError, subprocess.CalledProcessError) as exc:  # not a git checkout
        pytest.skip(f"git ls-files unavailable: {exc}")
    collisions = find_case_collisions(paths)
    assert not collisions, "\n".join("  <->  ".join(group) for group in collisions)
