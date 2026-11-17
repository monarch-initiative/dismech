#!/usr/bin/env python3
"""Fail when ``research/`` holds a deep-research run that produced no report.

Since 0.2.14, ``deep-research-client`` marks a run unsuccessful when the
provider says it could not answer, or (for the ``claude_code`` and
``antigravity`` agents) when the agent answered from memory without retrieving
anything, declined the task, or wrote a line beginning ``**Incomplete
report:**``. The client still writes the output, because a long paid run's
drafts are worth keeping, and the research recipes still place it in
``research/`` under the ordinary report name. What marks it is
``answer_status: unsuccessful`` in the frontmatter, a warning on its first
line, and exit code 4 from the command.

Nothing else stops such a file being committed as an entry's deep-research
report, and a from-memory answer is exactly the unsourced text the
deep-research step exists to replace. So this check refuses it.

Why this needs a whole-tree sweep
---------------------------------
The PRs that add a report touch ``research/`` and ``kb/``, which no
``src/``/``tests/`` path filter selects, so this runs as an ungated CI step as
well as in ``just qc`` -- the same reason ``check_duplicate_yaml_keys.py`` does.
No committed report carried the field when the check landed, so there is no
baseline.

The remedy is to delete the file (and its ``.citations.md`` sidecar and
``_artifacts/`` directory, if any) and re-run, or run another provider. Do not
edit ``answer_status`` away: the frontmatter is the provider's record of what
happened.

Usage
-----
    python scripts/check_unsuccessful_research.py              # gate research/
    python scripts/check_unsuccessful_research.py path/to/dir  # another tree
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Iterable
from pathlib import Path

from dismech.research_reports import report_is_unsuccessful

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESEARCH_DIR = ROOT / "research"


def candidate_reports(research_dir: Path) -> Iterable[Path]:
    """Every markdown file under ``research_dir`` that could be a report.

    Citations sidecars and files inside ``_artifacts/`` directories are
    skipped: neither is a report, and neither carries ``answer_status``.
    """
    for path in sorted(research_dir.rglob("*.md")):
        if path.name.endswith(".citations.md"):
            continue
        if any(part.endswith("_artifacts") for part in path.relative_to(research_dir).parts[:-1]):
            continue
        yield path


def find_unsuccessful(research_dir: Path) -> list[Path]:
    """Return the reports under ``research_dir`` marked ``answer_status: unsuccessful``."""
    return [path for path in candidate_reports(research_dir) if report_is_unsuccessful(path)]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "research_dir",
        nargs="?",
        type=Path,
        default=DEFAULT_RESEARCH_DIR,
        help="Directory to sweep (default: research/).",
    )
    args = parser.parse_args(argv)

    if not args.research_dir.is_dir():
        print(f"error: not a directory: {args.research_dir}", file=sys.stderr)
        return 2

    checked = sum(1 for _ in candidate_reports(args.research_dir))
    found = find_unsuccessful(args.research_dir)
    if not found:
        print(f"OK: none of {checked} research file(s) is marked answer_status: unsuccessful.")
        return 0

    print(
        "These files are deep-research runs that produced no report "
        "(answer_status: unsuccessful).\n"
        "The provider answered from memory, declined, or marked its report "
        "incomplete. Delete each one,\nwith its .citations.md sidecar and "
        "_artifacts/ directory, and re-run or use another provider.\n"
    )
    for path in found:
        try:
            shown = path.relative_to(ROOT)
        except ValueError:
            shown = path
        print(f"  {shown}")
    print(f"\n{len(found)} unsuccessful run(s) among {checked} research file(s).")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
