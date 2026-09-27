#!/usr/bin/env python3
"""Tally the reference-validation results already recorded in ``research/``.

Since ``deep-research-client`` 0.2.9 every ``just research-*`` recipe resolves
a report's citations while generating it and writes the answer into the report
as a ``reference_validation:`` frontmatter block (see
``docs/deep-research-reference-validation.md``). A retro-fitted report --
``just validate-research-reference`` on one generated earlier -- gets the
``## Reference Validation`` body section but *not* the frontmatter block, an
upstream asymmetry recorded in ``project.justfile``.

Nothing summed those per-report answers up. This script does, offline: it
reads the reports and never touches the network or ``references_cache/``. It
answers "how are the providers doing on citation hygiene?" (dismech #8841)
from what is already on disk, and the numbers can be regenerated rather than
trusted.

What it counts
--------------
For every ``*-deep-research-<provider>.md`` anywhere under ``research/``
(``.citations.md`` sidecars excluded) -- the walk is recursive because
``just research-module`` and ``just research-surrogacy`` write their reports
into ``research/modules/`` and ``research/surrogacy/``, and both pass the
same validation flags as the disorder recipe:

* ``frontmatter`` -- the report carries a ``reference_validation:`` block, so
  its counters are summed below;
* ``body-only`` -- no block, but a ``## Reference Validation`` section exists
  (a retro-fitted report: checked, but its counters are not machine-readable
  here);
* ``unvalidated`` -- neither.

A report's provider is the frontmatter ``provider:`` key when present, and
the filename's ``-deep-research-<provider>`` suffix otherwise -- the filename
drifts (date suffixes, ``manual`` vs ``manual_pubmed_review``) while the key
is what the generating recipe wrote.

Counters are summed verbatim from the frontmatter keys upstream emits
(``total_references``, ``verified``, ``not_found``, ``unverifiable``,
``quotes_checked``, ``quotes_valid``, ``quotes_unsupported``,
``quotes_not_checkable``, ``relevance_assessed``, ``on_topic``,
``off_topic``) plus a count of reports with ``needs_review: true``. Keys a
given report omits (upstream drops keys with nothing to report) count as
zero. A counter that is present but not an integer (a bool, a non-integral
float, an unparseable string) is also counted as zero, and the number of such
coercion failures is reported so a deflated sum has a visible cause. Rates are
computed from the sums, not averaged per report. The relevance check leaves an
undecided middle band (assessed, neither on nor off topic); it is printed so
that a low off-topic rate is not read as everything else being cleared.

Caveats the numbers cannot see
------------------------------
The block records what the validator could check at generation time. It says
nothing about Named Entity Confusion (a wrong-disease report validates green),
misattribution (a real paper cited for a claim it does not make), or the
snippet a curator later pastes into ``kb/`` -- CLAUDE.md §2a/§2b are unchanged.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import defaultdict
from collections.abc import Mapping
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import TextIO

import yaml

FRONTMATTER_DELIMITER = "---"
BODY_SECTION_RE = re.compile(r"^## Reference Validation\s*$", re.MULTILINE)
RESEARCH_FILE_RE = re.compile(r"^(?P<disorder>.+)-deep-research-(?P<provider>[^.]+)\.md$")

COUNTER_KEYS: tuple[str, ...] = (
    "total_references",
    "verified",
    "not_found",
    "unverifiable",
    "quotes_checked",
    "quotes_valid",
    "quotes_unsupported",
    "quotes_not_checkable",
    "relevance_assessed",
    "on_topic",
    "off_topic",
)

STATUS_FRONTMATTER = "frontmatter"
STATUS_BODY_ONLY = "body-only"
STATUS_UNVALIDATED = "unvalidated"


@dataclass
class ReportRow:
    """One research report and whatever validation record it carries."""

    path: str
    disorder: str
    provider: str
    status: str
    needs_review: bool = False
    validator_version: str = ""
    counters: dict[str, int] = field(default_factory=dict)
    coercion_failures: int = 0

    def as_flat(self) -> dict[str, object]:
        flat: dict[str, object] = {
            "path": self.path,
            "disorder": self.disorder,
            "provider": self.provider,
            "status": self.status,
            "needs_review": self.needs_review,
            "validator_version": self.validator_version,
        }
        for key in COUNTER_KEYS:
            flat[key] = self.counters.get(key, "")
        return flat


@dataclass
class Totals:
    reports: int = 0
    frontmatter: int = 0
    body_only: int = 0
    unvalidated: int = 0
    needs_review: int = 0
    coercion_failures: int = 0
    counters: dict[str, int] = field(default_factory=lambda: dict.fromkeys(COUNTER_KEYS, 0))

    def add(self, row: ReportRow) -> None:
        self.reports += 1
        if row.status == STATUS_FRONTMATTER:
            self.frontmatter += 1
            self.coercion_failures += row.coercion_failures
            if row.needs_review:
                self.needs_review += 1
            for key in COUNTER_KEYS:
                self.counters[key] += row.counters.get(key, 0)
        elif row.status == STATUS_BODY_ONLY:
            self.body_only += 1
        else:
            self.unvalidated += 1

    @property
    def relevance_undecided(self) -> int:
        return self.counters["relevance_assessed"] - self.counters["on_topic"] - self.counters["off_topic"]

    def rate(self, numerator: str, denominator: str) -> float | None:
        denom = self.counters.get(denominator, 0)
        if not denom:
            return None
        return self.counters.get(numerator, 0) / denom

    def as_dict(self) -> dict[str, object]:
        data: dict[str, object] = asdict(self)
        data["relevance_undecided"] = self.relevance_undecided
        data["rates"] = {
            "not_found_rate": self.rate("not_found", "total_references"),
            "unverifiable_rate": self.rate("unverifiable", "total_references"),
            "quotes_unsupported_rate": self.rate("quotes_unsupported", "quotes_checked"),
            "off_topic_rate": self.rate("off_topic", "relevance_assessed"),
        }
        return data


def read_report(path: Path) -> tuple[Mapping[str, object], str]:
    """Return (frontmatter mapping, body text). Either may be empty."""
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return {}, ""
    lines = text.split("\n")
    if not lines or lines[0].strip() != FRONTMATTER_DELIMITER:
        return {}, text
    for index in range(1, len(lines)):
        if lines[index].strip() == FRONTMATTER_DELIMITER:
            raw = "\n".join(lines[1:index])
            body = "\n".join(lines[index + 1 :])
            try:
                parsed = yaml.safe_load(raw) or {}
            except yaml.YAMLError:
                return {}, body
            return (parsed if isinstance(parsed, Mapping) else {}), body
    return {}, text


def coerce_int(value: object) -> tuple[int, bool]:
    """Return (integer value, whether it parsed). An absent key is ``(0, True)``."""
    if value is None:
        return 0, True
    if isinstance(value, bool):
        return 0, False
    if isinstance(value, int):
        return value, True
    if isinstance(value, float):
        return (int(value), True) if value.is_integer() else (0, False)
    if isinstance(value, str):
        try:
            return int(value.strip()), True
        except ValueError:
            return 0, False
    return 0, False


def report_provider(frontmatter: Mapping[str, object], filename_provider: str) -> str:
    value = frontmatter.get("provider")
    if isinstance(value, str) and value.strip():
        return value.strip()
    return filename_provider


def classify_report(path: Path, research_dir: Path) -> ReportRow | None:
    if path.name.endswith(".citations.md"):
        return None
    match = RESEARCH_FILE_RE.match(path.name)
    if not match:
        return None
    frontmatter, body = read_report(path)
    block = frontmatter.get("reference_validation")
    row = ReportRow(
        path=str(path.relative_to(research_dir)),
        disorder=match.group("disorder"),
        provider=report_provider(frontmatter, match.group("provider")),
        status=STATUS_UNVALIDATED,
    )
    if isinstance(block, Mapping):
        row.status = STATUS_FRONTMATTER
        row.needs_review = block.get("needs_review") is True
        row.validator_version = str(block.get("validator_version", "") or "")
        for key in COUNTER_KEYS:
            value, ok = coerce_int(block.get(key))
            row.counters[key] = value
            if not ok:
                row.coercion_failures += 1
    elif BODY_SECTION_RE.search(body):
        row.status = STATUS_BODY_ONLY
    return row


def collect(research_dir: Path) -> list[ReportRow]:
    rows: list[ReportRow] = []
    for path in sorted(research_dir.rglob("*.md")):
        row = classify_report(path, research_dir)
        if row is not None:
            rows.append(row)
    return rows


def summarize(rows: list[ReportRow]) -> tuple[Totals, dict[str, Totals]]:
    overall = Totals()
    by_provider: dict[str, Totals] = defaultdict(Totals)
    for row in rows:
        overall.add(row)
        by_provider[row.provider].add(row)
    return overall, dict(sorted(by_provider.items()))


def fmt_rate(value: float | None) -> str:
    return "-" if value is None else f"{100 * value:.1f}%"


def write_summary(
    out: TextIO, overall: Totals, by_provider: dict[str, Totals], *, all_providers: bool = False
) -> None:
    c = overall.counters
    out.write("Deep-research reference validation census\n")
    out.write("==========================================\n")
    out.write(f"Reports:              {overall.reports}\n")
    out.write(
        f"  validated (frontmatter block):  {overall.frontmatter}\n"
        f"  retro-fitted (body section only): {overall.body_only}\n"
        f"  unvalidated:                    {overall.unvalidated}\n"
    )
    out.write("\nSummed over the reports with a frontmatter block:\n")
    out.write(
        f"  references checked:   {c['total_references']}\n"
        f"    verified:           {c['verified']}\n"
        f"    not found:          {c['not_found']}  ({fmt_rate(overall.rate('not_found', 'total_references'))})\n"
        f"    unverifiable:       {c['unverifiable']}  ({fmt_rate(overall.rate('unverifiable', 'total_references'))})\n"
        f"  quotes checked:       {c['quotes_checked']}\n"
        f"    valid:              {c['quotes_valid']}\n"
        f"    unsupported:        {c['quotes_unsupported']}  ({fmt_rate(overall.rate('quotes_unsupported', 'quotes_checked'))})\n"
        f"    not checkable:      {c['quotes_not_checkable']}\n"
        f"  relevance assessed:   {c['relevance_assessed']}\n"
        f"    on topic:           {c['on_topic']}\n"
        f"    off topic:          {c['off_topic']}  ({fmt_rate(overall.rate('off_topic', 'relevance_assessed'))})\n"
        f"    undecided:          {overall.relevance_undecided}  (assessed, neither on nor off topic)\n"
        f"  reports needs_review: {overall.needs_review}\n"
    )
    out.write("\nPer provider (reports = all of that provider's; counters from its frontmatter-validated reports only):\n")
    header = (
        f"{'provider':<24}{'reports':>8}{'validated':>10}{'refs':>7}{'not found':>11}"
        f"{'quotes':>8}{'unsupported':>13}{'off topic':>11}{'review':>8}\n"
    )
    out.write(header)
    omitted = 0
    for provider, totals in by_provider.items():
        if not all_providers and totals.frontmatter == 0:
            omitted += 1
            continue
        pc = totals.counters
        out.write(
            f"{provider:<24}{totals.reports:>8}{totals.frontmatter:>10}{pc['total_references']:>7}"
            f"{fmt_rate(totals.rate('not_found', 'total_references')):>11}"
            f"{pc['quotes_checked']:>8}"
            f"{fmt_rate(totals.rate('quotes_unsupported', 'quotes_checked')):>13}"
            f"{fmt_rate(totals.rate('off_topic', 'relevance_assessed')):>11}"
            f"{totals.needs_review:>8}\n"
        )
    if omitted:
        out.write(f"({omitted} provider(s) with no validated reports omitted; --all-providers shows them)\n")
    if overall.coercion_failures:
        out.write(
            f"\nWARNING: {overall.coercion_failures} counter value(s) were present but not integers"
            " and were counted as zero; the sums above are deflated.\n"
        )
    out.write(
        "\nRates are computed from the sums. Keys a report omits count as zero.\n"
        "This sees only what the validator could check: not NEC, not misattribution,\n"
        "not the snippets later pasted into kb/ (CLAUDE.md §2a/§2b).\n"
    )


def write_tsv(out: TextIO, rows: list[ReportRow]) -> None:
    fieldnames = ["path", "disorder", "provider", "status", "needs_review", "validator_version", *COUNTER_KEYS]
    writer = csv.DictWriter(out, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow(row.as_flat())


def write_json(out: TextIO, rows: list[ReportRow], overall: Totals, by_provider: dict[str, Totals]) -> None:
    payload = {
        "totals": overall.as_dict(),
        "by_provider": {provider: totals.as_dict() for provider, totals in by_provider.items()},
        "reports": [row.as_flat() for row in rows],
    }
    json.dump(payload, out, indent=2, sort_keys=False)
    out.write("\n")


def write_needs_review(out: TextIO, rows: list[ReportRow]) -> None:
    flagged = [row for row in rows if row.needs_review]
    if not flagged:
        out.write("No report carries needs_review: true.\n")
        return
    out.write(f"{len(flagged)} report(s) flagged needs_review (not found / unsupported quotes / off topic):\n")
    for row in flagged:
        c = row.counters
        out.write(
            f"  {row.path}\t"
            f"not_found={c.get('not_found', 0)}\t"
            f"quotes_unsupported={c.get('quotes_unsupported', 0)}\t"
            f"off_topic={c.get('off_topic', 0)}\n"
        )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--research-dir",
        type=Path,
        default=Path("research"),
        help="Directory holding the *-deep-research-*.md reports (default: research/)",
    )
    parser.add_argument(
        "--format",
        choices=("summary", "tsv", "json"),
        default="summary",
        help="summary (default): totals + per-provider table; tsv: one row per report; json: everything",
    )
    parser.add_argument(
        "--needs-review",
        action="store_true",
        help="List the reports whose block carries needs_review: true, then exit",
    )
    parser.add_argument(
        "--validated-only",
        action="store_true",
        help="Drop reports that carry no validation record from tsv/json output "
        "(no effect on --needs-review or the summary, which always count everything)",
    )
    parser.add_argument(
        "--all-providers",
        action="store_true",
        help="In the summary table, also list providers with no validated reports",
    )
    parser.add_argument("--out", type=Path, default=None, help="Write to this file instead of stdout")
    args = parser.parse_args(argv)

    if not args.research_dir.is_dir():
        print(f"error: research directory not found: {args.research_dir}", file=sys.stderr)
        return 2

    rows = collect(args.research_dir)
    overall, by_provider = summarize(rows)
    if args.validated_only:
        rows = [row for row in rows if row.status != STATUS_UNVALIDATED]

    out: TextIO = args.out.open("w", encoding="utf-8") if args.out else sys.stdout
    try:
        if args.needs_review:
            write_needs_review(out, rows)
        elif args.format == "tsv":
            write_tsv(out, rows)
        elif args.format == "json":
            write_json(out, rows, overall, by_provider)
        else:
            write_summary(out, overall, by_provider, all_providers=args.all_providers)
    finally:
        if args.out:
            out.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
