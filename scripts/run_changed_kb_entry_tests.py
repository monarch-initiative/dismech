#!/usr/bin/env python3
"""Run the per-entry ``kb_data`` tests on the given KB files only.

The whole-KB conformance sweep (``just test-kb``) runs in the merge queue and
when the schema changes, never on a ``kb/``-only curation PR. So an entry could
pass every check on its own PR and then fail the queue on a structural check in
``tests/test_data.py`` it was never given the chance to run (issue #18313).

This script takes the changed KB paths (the paths-filter lists in CI, or any
paths locally) and runs exactly the parametrized items that check those files:

    kb/disorders/X.yaml     -> tests/test_data.py::test_disorder_file[kb/disorders/X.yaml]
    kb/modules/X.yaml       -> tests/test_data.py::test_module_file[kb/modules/X.yaml]
    kb/comorbidities/X.yaml -> tests/test_data.py::test_comorbidity_file[kb/comorbidities/X.yaml]

Explicit node IDs rather than ``-k``: ``-k Asthma`` would also select
``Asthma_Severe``. Deleted files and paths outside those directories are
skipped. Cross-file breakage is out of scope; that stays with the queue.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

TEST_FILE = "tests/test_data.py"

# Directory (relative to the repo root) -> parametrized test that checks one
# file in it. Mirrors the ``test_*_file`` functions at the bottom of
# tests/test_data.py; tests/test_run_changed_kb_entry_tests.py pins the two
# together.
KIND_TESTS = {
    "kb/disorders": "test_disorder_file",
    "kb/modules": "test_module_file",
    "kb/comorbidities": "test_comorbidity_file",
}


# At or above this many entries, run under xdist. Below it, worker start-up
# costs more than it saves.
PARALLEL_THRESHOLD = 40


def _has_xdist_flag(args: list[str]) -> bool:
    return any(a.startswith(("-n", "--numprocesses")) for a in args)


def _repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def node_ids(paths: list[str], root: Path) -> tuple[list[str], list[str]]:
    """Map KB paths to pytest node IDs.

    Returns ``(ids, skipped)``; ``skipped`` holds a human-readable reason per
    path that produced no node ID.
    """
    ids: list[str] = []
    skipped: list[str] = []
    seen: set[str] = set()
    for raw in paths:
        candidate = Path(raw)
        absolute = candidate if candidate.is_absolute() else root / candidate
        try:
            rel = absolute.resolve().relative_to(root.resolve())
        except ValueError:
            skipped.append(f"{raw}: outside the repository")
            continue
        rel_str = rel.as_posix()
        test = KIND_TESTS.get(rel.parent.as_posix())
        if test is None or rel.suffix != ".yaml" or rel.name.endswith(".history.yaml"):
            skipped.append(f"{raw}: not a disorder, module or comorbidity entry")
            continue
        if not absolute.is_file():
            skipped.append(f"{raw}: deleted or missing")
            continue
        node = f"{TEST_FILE}::{test}[{rel_str}]"
        if node not in seen:
            seen.add(node)
            ids.append(node)
    return ids, skipped


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("paths", nargs="*", help="KB entry paths")
    parser.add_argument(
        "--print-only",
        action="store_true",
        help="print the node IDs and exit without running pytest",
    )
    args, pytest_args = parser.parse_known_args(argv)

    root = _repo_root()
    ids, skipped = node_ids(args.paths, root)
    for reason in skipped:
        print(f"Skipping {reason}")
    if not ids:
        print("No existing disorder, module or comorbidity entries to test.")
        return 0
    if args.print_only:
        print("\n".join(ids))
        return 0

    print(f"Running per-entry conformance tests on {len(ids)} file(s)...")
    # -m kb_data: the target tests carry that marker, and naming it keeps any
    # future ``-m "not kb_data"`` addopts from deselecting them silently. A
    # node ID that does not exist is a pytest error, not a silent skip, so a
    # renamed test function fails here rather than testing nothing.
    if len(ids) >= PARALLEL_THRESHOLD and not _has_xdist_flag(pytest_args):
        # A bulk-sweep PR can touch hundreds of entries. Four workers matches
        # the runner's vCPUs, as in the test-python-code step.
        pytest_args = ["-n", "4", *pytest_args]
    cmd = [sys.executable, "-m", "pytest", "-m", "kb_data", *pytest_args, *ids]
    return subprocess.call(cmd, cwd=root)


if __name__ == "__main__":
    sys.exit(main())
