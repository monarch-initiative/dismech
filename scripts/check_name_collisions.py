#!/usr/bin/env python3
"""Report rows that share a pathograph node name, and gate the accidental ones.

``dismech.graph`` keys its node table on an item's ``name``. Two rows with the
same name therefore become **one** node: the second overwrites the first, the
surviving node takes its attributes from whichever row came last, and the
pathograph shows one node where the YAML has two curated rows. Nothing else
reports it. ``check-duplicate-keys`` looks at mapping keys, not repeated
``- name:`` list items; ``check-causal-targets`` asks whether a target
resolves, and a target naming two rows resolves fine; and a repeated ``name``
in a list is valid YAML and valid LinkML (issue #15443).

Three classes, from :func:`dismech.graph.find_name_collisions`:

``UNSTRATIFIED`` (gated)
    Rows in one section not told apart by ``subtype:``: at least one has no
    subtype, or two share one. Almost always an accident -- the rows should be
    merged, or one renamed. The backlog on ``main`` when this landed is
    grandfathered in ``tests/name_collision_baseline.txt``, which only shrinks.

``STRATIFIED`` (reported)
    Rows in one section, each with a different ``subtype:`` -- e.g. the same
    phenotype for CAIS and for PAIS. That is the stratification CLAUDE.md asks
    curators to do, so it is not a defect in the entry. It is a limit of the
    graph, which cannot show them as separate nodes, and fixing that means
    changing how bare targets resolve, which this script does not decide.

``CROSS_SECTION`` (reported)
    Rows in different sections, most often a pathophysiology node and a
    phenotype with the same name. Also one node, and an edge between the two
    becomes a self-loop (the case issue #9896 found). Common enough that it
    needs its own decision rather than a gate.

Usage::

    python scripts/check_name_collisions.py                 # gate, whole KB
    python scripts/check_name_collisions.py kb/disorders/X.yaml
    python scripts/check_name_collisions.py --report        # census, exit 0
    python scripts/check_name_collisions.py --report --format tsv
    python scripts/check_name_collisions.py --update-baseline   # shrink only
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dismech.graph import NameCollision, find_name_collisions
from dismech.yaml_io import safe_load

BASELINE_PATH = ROOT / "tests" / "name_collision_baseline.txt"
DEFAULT_ROOTS = ("kb/disorders", "kb/modules", "kb/comorbidities")
KINDS = ("UNSTRATIFIED", "STRATIFIED", "CROSS_SECTION")
GATED = "UNSTRATIFIED"


def _display(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def iter_yaml_files(paths: list[str]) -> tuple[list[Path], list[str]]:
    """Same convention as ``check_causal_targets.iter_yaml_files`` (#11939)."""
    if not paths:
        files: list[Path] = []
        for root in DEFAULT_ROOTS:
            files.extend(sorted((ROOT / root).rglob("*.yaml")))
        return files, []
    files = []
    usage_errors: list[str] = []
    for raw in paths:
        path = Path(raw)
        if path.is_dir():
            found = sorted(path.rglob("*.yaml"))
            if not found:
                usage_errors.append(
                    f"{_display(path)}: directory contains no *.yaml files"
                )
            files.extend(found)
        else:
            files.append(path)
    return files, usage_errors


def collect(paths: list[str]) -> tuple[list[tuple[str, NameCollision]], list[str]]:
    """Return ``([(display_path, collision), ...], usage_errors)``."""
    found: list[tuple[str, NameCollision]] = []
    files, usage_errors = iter_yaml_files(paths)
    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            usage_errors.append(f"{_display(path)}: {exc.strerror or exc}")
            continue
        try:
            data = safe_load(text)
        except yaml.YAMLError:
            continue  # check-duplicate-keys / linkml-validate report parse errors
        if isinstance(data, dict):
            display = _display(path)
            found.extend((display, c) for c in find_name_collisions(data))
    return found, usage_errors


def baseline_key(path: str, collision: NameCollision) -> str:
    return f"{path}\t{collision.rows[0].source}\t{collision.name}"


def load_baseline() -> set[str]:
    if not BASELINE_PATH.exists():
        return set()
    return {
        line
        for line in BASELINE_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    }


def describe(collision: NameCollision) -> str:
    parts = []
    for row in collision.rows:
        parts.append(
            f"{row.source}[subtype={row.subtype}]" if row.subtype else row.source
        )
    return ", ".join(parts)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__.splitlines()[0],
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("paths", nargs="*", help=f"default: {', '.join(DEFAULT_ROOTS)}")
    parser.add_argument(
        "--report", action="store_true", help="print every class and exit 0"
    )
    parser.add_argument(
        "--format",
        choices=("text", "tsv"),
        default="text",
        help="report format (with --report)",
    )
    parser.add_argument(
        "--update-baseline",
        action="store_true",
        help="drop baseline rows that no longer match; never adds one",
    )
    args = parser.parse_args(argv)

    if args.update_baseline and args.paths:
        parser.error("--update-baseline is whole-KB only; re-run it with no paths.")

    found, usage_errors = collect(args.paths)
    if usage_errors:
        for message in usage_errors:
            print(f"ERROR: {message}", file=sys.stderr)
        return 2

    gated = [(p, c) for p, c in found if c.kind == GATED]
    baseline = load_baseline()

    if args.update_baseline:
        live = {baseline_key(p, c) for p, c in gated}
        kept = sorted(baseline & live)
        header = [
            line
            for line in BASELINE_PATH.read_text(encoding="utf-8").splitlines()
            if line.startswith("#")
        ]
        BASELINE_PATH.write_text("\n".join(header + kept) + "\n", encoding="utf-8")
        print(
            f"kept {len(kept)} of {len(baseline)} baseline row(s); removed {len(baseline) - len(kept)}"
        )
        return 0

    if args.report:
        if args.format == "tsv":
            print("path\tkind\tname\tlost_rows\trows")
            for path, c in found:
                print(f"{path}\t{c.kind}\t{c.name}\t{c.lost_rows}\t{describe(c)}")
            return 0
        for kind in KINDS:
            group = [(p, c) for p, c in found if c.kind == kind]
            lost = sum(c.lost_rows for _, c in group)
            label = "gated" if kind == GATED else "reported"
            print(
                f"\n== {kind} ({label}): {len(group)} name(s), {lost} row(s) merged away =="
            )
            for path, c in group:
                print(f"  {path}: {c.name!r} <- {describe(c)}")
        return 0

    new = [(p, c) for p, c in gated if baseline_key(p, c) not in baseline]
    stale: list[str] = []
    if not args.paths:
        stale = sorted(baseline - {baseline_key(p, c) for p, c in gated})

    if stale:
        print(
            f"note: {len(stale)} baseline row(s) no longer collide. Shrink the "
            "baseline with `just update-name-collision-baseline`:"
        )
        for key in stale:
            print(f"  {key.replace(chr(9), '  ')}")
        print()

    if not new:
        others = {k: sum(1 for _, c in found if c.kind == k) for k in KINDS[1:]}
        print(
            f"OK: no new unstratified name collisions "
            f"({len(baseline) - len(stale)} grandfathered; "
            f"{others['STRATIFIED']} stratified and {others['CROSS_SECTION']} "
            "cross-section collision(s) reported by `just list-name-collisions`)."
        )
        return 0

    print("Rows sharing a name collapse into one pathograph node (issue #15443).\n")
    print(
        "The graph keys nodes on `name`, so these rows render as a single node and\n"
        "all but the last are silently dropped. Merge the rows, or rename one so\n"
        "every row has its own name. If the rows really are the same feature in\n"
        "different subtypes, give each its own distinct `subtype:` instead.\n"
        "Any bare `target:` naming a renamed row must be updated too.\n"
    )
    for path, c in new:
        print(f"  {path}: {c.name!r} <- {describe(c)}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
