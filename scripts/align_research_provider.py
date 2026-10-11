#!/usr/bin/env python3
"""Rename a deep-research report to the provider that actually produced it.

Run after a research recipe, so that an opt-in provider fallback cannot leave a
report named for a provider that did not write it. Does nothing unless the
report's frontmatter records ``fell_back: true``.

With ``--into DIR`` the report is a freshly staged run output, and it is moved
into DIR -- under the provider-aligned name, or under that name with the run
date appended when a report already holds it. A run never replaces an existing
report, its citations or its artifacts (dismech#12700); this is how every
research recipe places its output.

Usage:
    scripts/align_research_provider.py <report.md> --requested <provider slug>
    scripts/align_research_provider.py <report.md> --requested falcon --dry-run
    scripts/align_research_provider.py tmp/research-staging/x/Foo-deep-research-falcon.md \
        --requested falcon --into research

Exits non-zero when a fallback happened but the report cannot be renamed
safely — a missing file, a provider slug that is not in the filename, a
destination that is already taken (in-place mode only), or a source that is
committed content this run did not write. That is deliberate: the file on disk is then
a report by one provider carrying another's name, which is the whole defect
this guards against.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from dismech.research_reports import (
    AlignmentError,
    align_report_provider,
    place_report,
)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path, help="The report the run just wrote.")
    parser.add_argument(
        "--requested",
        required=True,
        help="Provider slug the run asked for, as it appears in the filename.",
    )
    parser.add_argument(
        "--into",
        type=Path,
        help=(
            "Move the (staged) report into this directory without replacing "
            "anything already there."
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Say what would move without moving anything.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        if args.into is not None:
            alignment = place_report(
                args.report, args.into, args.requested, dry_run=args.dry_run
            )
        else:
            alignment = align_report_provider(
                args.report, args.requested, dry_run=args.dry_run
            )
    except AlignmentError as error:
        print(f"error: {error}", file=sys.stderr)
        if args.into is not None:
            print(
                f"The run's output is still at {args.report}; nothing in "
                f"{args.into} was changed.",
                file=sys.stderr,
            )
        return 1

    verb = "would rename" if args.dry_run else "renamed"
    if args.into is not None:
        place_verb = "would place" if args.dry_run else "placed"
        print(f"{place_verb} report at {alignment.report}")
        if alignment.kept_alongside is not None:
            print(
                f"  {alignment.kept_alongside} already exists and was left "
                "untouched; the new report sits beside it under a dated name."
            )
    if not alignment.fell_back:
        return 0

    print(
        f"{args.requested} could not run this job; "
        f"{alignment.actual_provider} produced the report instead, so it is "
        f"named for {alignment.actual_provider}:"
    )
    for old, new in alignment.moved:
        print(f"  {verb} {old} -> {new}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
