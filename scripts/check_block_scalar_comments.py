#!/usr/bin/env python3
"""Reject yamlfix's suspicious '  # <digit>' spacing inside KB block scalars.

The default whole-KB gate grandfathers the recorded backlog and rejects new
findings. --strict fails on every finding; --update-baseline only removes
repaired findings. Review against the source; never auto-repair quotes (#12101).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

import yaml
from yaml.events import ScalarEvent

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dismech.yaml_io import SafeLoader

FINGERPRINT = re.compile(r"  # [0-9]")
BASELINE = ROOT / "tests" / "block_scalar_comments_baseline.txt"


def read_baseline(path: Path) -> Counter:
    """Read counted (file, exact source line) findings, independent of line number."""
    counts = Counter()
    for row in path.read_text(encoding="utf-8").splitlines():
        if row and not row.startswith("#"):
            file, text, count = json.loads(row)
            if not isinstance(count, int) or count < 1 or (file, text) in counts:
                raise ValueError(f"invalid baseline row: {row}")
            counts[file, text] = count
    return counts


def write_baseline(path: Path, counts: Counter) -> None:
    """Serialize the recorded backlog; the CLI only calls this with an intersection."""
    rows = [
        "# Existing suspicious block-scalar lines for review (dismech#12101).",
        "# JSON rows: [file, source line without indentation, occurrence count].",
        "# Shrink only: just check-block-scalar-comments --update-baseline",
    ]
    rows.extend(
        json.dumps([*key, count], ensure_ascii=False)
        for key, count in sorted(counts.items())
    )
    path.write_text("\n".join(rows) + "\n", encoding="utf-8")


def find_corruption(text: str) -> list[int]:
    """Return 1-based source lines matching the fingerprint in | or > content.

    Parse YAML events rather than guessing block boundaries from indentation:
    quoted strings, actual comments, explicit indent/chomping indicators and
    nested sequences must all be distinguished correctly.
    """
    findings = []
    for token in yaml.parse(text, Loader=SafeLoader):
        if not isinstance(token, ScalarEvent) or token.style not in ("|", ">"):
            continue
        raw = text[token.start_mark.index : token.end_mark.index]
        for offset, line in enumerate(raw.splitlines()[1:], start=1):
            if FINGERPRINT.search(line):
                findings.append(token.start_mark.line + offset + 1)
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths", nargs="*", type=Path, help="YAML files (default: all kb/)"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="fail on every finding, including the backlog",
    )
    parser.add_argument("--baseline", type=Path, default=BASELINE)
    parser.add_argument(
        "--update-baseline",
        action="store_true",
        help="drop repaired findings; never add exemptions",
    )
    args = parser.parse_args(argv)
    if args.update_baseline and args.paths:
        parser.error("--update-baseline requires a whole-KB scan (no paths)")
    try:
        baseline = read_baseline(args.baseline)
    except (OSError, ValueError, TypeError) as exc:
        print(f"{args.baseline}: could not read baseline ({exc})", file=sys.stderr)
        return 1
    files = args.paths or sorted(
        path for path in (ROOT / "kb").rglob("*") if path.suffix in (".yaml", ".yml")
    )
    count = 0
    affected = 0
    failed = False
    current = Counter()
    new = 0
    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
            lines = find_corruption(text)
        except (OSError, UnicodeError, yaml.YAMLError) as exc:
            print(f"{path}: could not check ({exc})", file=sys.stderr)
            failed = True
            continue
        count += len(lines)
        affected += bool(lines)
        try:
            display = str(path.resolve().relative_to(ROOT.resolve()))
        except ValueError:
            display = str(path)
        source_lines = text.splitlines()
        for line in lines:
            key = (display, source_lines[line - 1].lstrip())
            current[key] += 1
            is_new = current[key] > baseline[key]
            new += is_new
            if args.strict or is_new:
                print(
                    f"{display}:{line}: suspicious '  # <digit>' in block scalar; review against source"
                )
    if args.update_baseline and not failed:
        write_baseline(args.baseline, baseline & current)
    print(f"{count} suspicious line(s) in {affected} of {len(files)} YAML file(s).")
    print(
        f"{new} new; {count - new} in the existing review backlog (--strict to list all)."
    )
    return int(failed or bool(count if args.strict else new))


if __name__ == "__main__":
    raise SystemExit(main())
