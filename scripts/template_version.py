#!/usr/bin/env python3
"""Stamp and audit the research-template revision behind each report.

Two subcommands, matching the two halves of issue #10183:

``stamp``
    Record the template's git blob hash in a report's frontmatter. Run after a
    research recipe writes a report, so that from now on a report says which
    revision of the prompt produced it rather than only which path it lived at.
    Idempotent, and silent when there is nothing to stamp.

``audit``
    Report which revision each existing report was generated from, how that was
    determined, and how many predate the current prompt. Historical reports are
    resolved from their ``start_time`` against the template's commit history, so
    this answers the question for the whole corpus without rewriting a single
    committed file.

Usage:
    scripts/template_version.py stamp research/Asthma-deep-research-falcon.md
    scripts/template_version.py audit
    scripts/template_version.py audit --template templates/disease_pathophysiology_research.md
    scripts/template_version.py audit --format tsv --out /tmp/versions.tsv
    scripts/template_version.py audit --stale-only
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict
from pathlib import Path

from dismech.template_versions import (
    Provenance,
    Resolution,
    blob_sha,
    iter_reports,
    resolve_report,
    stamp_report,
)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    stamp = sub.add_parser("stamp", help="Record the template blob hash in a report.")
    stamp.add_argument("reports", nargs="+", type=Path, help="Reports to stamp.")
    stamp.add_argument(
        "--repo-root",
        type=Path,
        default=Path("."),
        help="Root that template_file paths are relative to.",
    )
    stamp.add_argument(
        "--quiet",
        action="store_true",
        help="Say nothing on success. For use inside recipes.",
    )

    audit = sub.add_parser("audit", help="Report template revisions across reports.")
    audit.add_argument(
        "--reports-dir", type=Path, default=Path("research"), help="Directory to scan."
    )
    audit.add_argument(
        "--template",
        help="Restrict to reports generated from this template path.",
    )
    audit.add_argument(
        "--format",
        choices=("summary", "tsv", "list"),
        default="summary",
        help="summary (default), tsv for a spreadsheet, list for one line per report.",
    )
    audit.add_argument(
        "--out", type=Path, help="Write the output here instead of stdout."
    )
    audit.add_argument(
        "--stale-only",
        action="store_true",
        help="Only reports generated from a superseded template revision.",
    )
    audit.add_argument(
        "--unresolved-only",
        action="store_true",
        help="Only reports whose template revision could not be determined.",
    )
    return parser.parse_args(argv)


def run_stamp(args: argparse.Namespace) -> int:
    written = 0
    for report in args.reports:
        if not report.is_file():
            print(f"error: no such report: {report}", file=sys.stderr)
            return 1
        sha = stamp_report(report, repo_root=args.repo_root)
        if sha:
            written += 1
            if not args.quiet:
                print(f"stamped {report}: template_sha {sha[:12]}")
        elif not args.quiet:
            print(f"nothing to stamp in {report}")
    if args.quiet and written:
        # One line even when quiet, so a recipe's log records that it happened.
        print(f"template_sha recorded on {written} report(s)")
    return 0


def _current_blobs(templates: set[str], repo_root: Path) -> dict[str, str | None]:
    """Blob hash of each named template as it stands on disk now."""
    current: dict[str, str | None] = {}
    for template in templates:
        path = repo_root / template
        current[template] = blob_sha(path) if path.is_file() else None
    return current


def _render_summary(
    resolutions: list[Resolution], current: dict[str, str | None]
) -> str:
    lines: list[str] = []
    total = len(resolutions)
    provenance = Counter(r.provenance.value for r in resolutions)

    lines.append(f"Reports scanned: {total}")
    lines.append("")
    lines.append("How the template revision was determined:")
    for name in ("stamped", "inferred", "unknown"):
        count = provenance.get(name, 0)
        share = f"{100 * count / total:.1f}%" if total else "-"
        lines.append(f"  {name:9} {count:6}  {share}")
    lines.append("")

    by_template: dict[str, list[Resolution]] = defaultdict(list)
    for resolution in resolutions:
        by_template[resolution.template or "(none recorded)"].append(resolution)

    lines.append("Per template — reports by the revision that produced them:")
    for template in sorted(by_template):
        group = by_template[template]
        head = current.get(template)
        lines.append("")
        lines.append(f"  {template}  ({len(group)} report(s))")
        if head:
            lines.append(f"    current revision: {head[:12]}")
        counts = Counter(r.short_blob for r in group)
        for blob, count in counts.most_common():
            if blob == "-":
                label = "undetermined"
            elif head and blob == head[:12]:
                label = "current"
            else:
                label = "superseded"
            lines.append(f"    {blob:14} {count:6}  {label}")

    stale = sum(
        1 for r in resolutions if r.is_current(current.get(r.template)) is False
    )
    undetermined = sum(
        1 for r in resolutions if r.is_current(current.get(r.template)) is None
    )
    lines.append("")
    lines.append(f"Generated from a superseded revision: {stale}")
    lines.append(f"Undetermined (not the same as stale): {undetermined}")
    return "\n".join(lines) + "\n"


def _render_tsv(resolutions: list[Resolution], current: dict[str, str | None]) -> str:
    rows = ["report\ttemplate\tblob\tprovenance\tis_current\tdetail"]
    for r in resolutions:
        state = r.is_current(current.get(r.template))
        rows.append(
            "\t".join(
                (
                    str(r.report),
                    r.template or "",
                    r.blob or "",
                    r.provenance.value,
                    "" if state is None else str(state).lower(),
                    r.detail,
                )
            )
        )
    return "\n".join(rows) + "\n"


def _render_list(resolutions: list[Resolution], current: dict[str, str | None]) -> str:
    rows = []
    for r in resolutions:
        state = r.is_current(current.get(r.template))
        mark = {True: "current", False: "superseded", None: "undetermined"}[state]
        rows.append(f"{r.report}\t{r.short_blob}\t{r.provenance.value}\t{mark}")
    return "\n".join(rows) + "\n"


def run_audit(args: argparse.Namespace) -> int:
    if not args.reports_dir.is_dir():
        print(f"error: no such directory: {args.reports_dir}", file=sys.stderr)
        return 1

    resolutions = [resolve_report(report) for report in iter_reports(args.reports_dir)]
    if args.template:
        resolutions = [r for r in resolutions if r.template == args.template]

    current = _current_blobs({r.template for r in resolutions if r.template}, Path("."))

    if args.stale_only:
        resolutions = [
            r for r in resolutions if r.is_current(current.get(r.template)) is False
        ]
    if args.unresolved_only:
        resolutions = [r for r in resolutions if r.provenance is Provenance.UNKNOWN]

    render = {
        "summary": _render_summary,
        "tsv": _render_tsv,
        "list": _render_list,
    }[args.format]
    output = render(resolutions, current)

    if args.out:
        args.out.write_text(output, encoding="utf-8")
        print(f"wrote {args.out}")
    else:
        sys.stdout.write(output)
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.command == "stamp":
        return run_stamp(args)
    return run_audit(args)


if __name__ == "__main__":
    raise SystemExit(main())
