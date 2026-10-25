"""KB-wide pathograph statistics, committed so a page render need not walk the KB.

A disorder page opens its pathograph grouped when the graph has more edges than
the mean over every entry that draws one (#14539). Computing that mean means
building the causal graph of every disorder, which costs tens of seconds -- a
one-off cost in a full page build, but a large one for a single-file render.
So the value lives in ``cache/pathograph_stats.json``, rewritten by the page
build (``just gen-pathograph-stats``) and read by ``render``.

The mean is rounded to a whole number, so the file changes rarely rather than
on every curation PR. A stale value only moves the threshold at which a page
opens grouped by an edge or so; the reader can change the grouping either way.

Usage::

    python -m dismech.pathograph_stats            # rewrite the file
    python -m dismech.pathograph_stats --check    # exit 1 if it is stale
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from dismech import kb_cache
from dismech.graph import build_causal_graph
from dismech.repo_root import LazyRepoPaths

# Resolved from the working directory when read, so a worktree reads and writes
# its own cache/pathograph_stats.json (#15109).
_PATHS = LazyRepoPaths(
    __name__,
    PATHOGRAPH_STATS_PATH=lambda root: root / "cache" / "pathograph_stats.json",
    DEFAULT_DISORDERS_DIR=lambda root: root / "kb" / "disorders",
)
__getattr__ = _PATHS.module_getattr

_DESCRIPTION = (
    "Derived from kb/disorders by `just gen-pathograph-stats`; do not hand-edit. "
    "mean_edge_count is the rounded mean pathograph edge count over entries "
    "that draw a pathograph."
)


def compute_mean_edge_count(disorders_dir: Path) -> int | None:
    """Mean pathograph edge count over the entries in ``disorders_dir``.

    Only entries that draw a pathograph count. Returns ``None`` when none do.
    """
    counts = []
    for path in sorted(disorders_dir.glob("*.yaml")):
        try:
            document = kb_cache.load_document(path)
        except Exception:  # an unparsable entry must not break the statistic
            continue
        if not isinstance(document, dict):
            continue
        edge_count = len(build_causal_graph(document).edges)
        if edge_count:
            counts.append(edge_count)
    if not counts:
        return None
    return round(sum(counts) / len(counts))


def compute_stats(disorders_dir: Path) -> dict:
    return {
        "description": _DESCRIPTION,
        "mean_edge_count": compute_mean_edge_count(disorders_dir),
    }


def read_stats(path: Path | None = None) -> dict | None:
    """Return the committed statistics, or ``None`` if the file is absent or unreadable."""
    if path is None:
        path = _PATHS.get("PATHOGRAPH_STATS_PATH")
    try:
        data = json.loads(path.read_text())
    except (OSError, ValueError):
        return None
    return data if isinstance(data, dict) else None


def _serialize(stats: dict) -> str:
    return json.dumps(stats, indent=2) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument(
        "-i", "--input", type=Path, default=_PATHS.get("DEFAULT_DISORDERS_DIR")
    )
    parser.add_argument(
        "-o", "--output", type=Path, default=_PATHS.get("PATHOGRAPH_STATS_PATH")
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Report whether the committed file matches the KB; exit 1 if stale.",
    )
    args = parser.parse_args(argv)
    kb_cache.default_off()  # one walk, so the parsed-KB cache would be pure cost

    stats = compute_stats(args.input)
    if args.check:
        committed = read_stats(args.output)
        if committed == stats:
            print(
                f"{args.output}: up to date (mean_edge_count={stats['mean_edge_count']})"
            )
            return 0
        found = committed.get("mean_edge_count") if committed else None
        print(
            f"{args.output}: stale (committed mean_edge_count={found}, "
            f"KB gives {stats['mean_edge_count']}); run `just gen-pathograph-stats`"
        )
        return 1

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(_serialize(stats))
    print(f"Wrote {args.output} (mean_edge_count={stats['mean_edge_count']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
