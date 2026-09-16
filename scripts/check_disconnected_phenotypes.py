#!/usr/bin/env python3
"""Report phenotypes that no causal edge explains (issue #11935).

A phenotype joins the pathograph only when some other item names it as a
target: a ``pathophysiology[].downstream[].target``, another phenotype's
``sequelae[].target``, or an ``environmental[].influences_mechanisms[].target``
carrying a causal effect. Nothing requires that edge, and nothing reported its
absence -- so on a large share of entries the graph stops at the
pathophysiology layer and the phenotypes render as a disconnected island beside
it.

This is the **complement** of ``just check-causal-targets``, which asks the
opposite question: which declared edges name a target that resolves to nothing.
An entry can pass that check perfectly -- every edge resolving cleanly -- while
no edge lands on a phenotype at all. The motivating instance,
``SLC35A1-Congenital_Disorder_of_Glycosylation``, has 8 pathophysiology nodes,
12 phenotype nodes and 7 causal edges, none of which reaches a phenotype.

Reuses the metric rather than recomputing it
--------------------------------------------
The connectivity computation already existed as
:func:`dismech.qc_plugins.causal_inlink_coverage`, the metric behind the
``phenotypes[].causal_inlink`` compliance score (``conf/qc_config.yaml``, weight
1.5, ``min_compliance: null``), and was already exposed as
``just compliance-connectivity``. This script calls the same function, so the
two can never disagree on a number, and it does not supersede that recipe:
``compliance-connectivity`` remains the compliance view, reporting phenotype
inlink and gene-to-mechanism outlink coverage together with ``--fail-under`` on
each.

What it adds is the per-entry triage the compliance view has no room for -- a
ranked zero-connectivity worklist, ``--format tsv``/``json``, and an attachment
class per stranded phenotype -- under a name filed next to
``just list-causal-targets`` and ``just list-cancer-origin`` rather than under
compliance, which is plausibly why neither issue #11935 nor the review round
that prompted it found the existing recipe.

What counts as connected
------------------------
Exactly what ``causal_inlink_coverage`` counts: an inbound edge whose predicate
is in :data:`dismech.qc_plugins.CAUSAL_PREDICATES` (``causes``, ``leads_to``,
``triggers``, ``exacerbates``). Self-loops do not count. That settles the two
questions issue #11935 left open, and settles them the strict way:

``treatments[].target_mechanisms`` / ``target_phenotypes`` do **not** connect a
    phenotype. A ``treats`` or ``targets`` edge says the phenotype is addressed
    by an intervention, not which mechanism produces it.
``phenotypes[].reports_on`` does **not** connect the phenotype it names. That
    edge carries the ``readout`` predicate -- an observational link ("this
    abnormal test result reports on that mechanism"), not a causal claim.
``subtype`` scoping does not connect anything either. A phenotype restricted to
    a subtype still needs an edge from whatever produces it.

Rather than argue those three out of the denominator, the report keeps them
visible: every disconnected phenotype carries an **attachment** class saying
whether anything in the graph touches it at all
(:data:`ATTACH_ISOLATED` through :data:`ATTACH_SEQUELA_SOURCE`). A phenotype
reached by a treatment edge and a phenotype no edge touches are both
unexplained, but they are not the same curation job.

Report-only, and not a number to drive up
-----------------------------------------
Exit 0 always, unless you ask otherwise with ``--strict`` or ``--fail-under``.
Connecting a phenotype is real curation: the edge asserts which mechanism
produces which clinical feature, which is often exactly what the literature
does not settle. Some phenotypes legitimately have no upstream node in the
entry -- a laboratory readout, or a feature whose mechanism is genuinely
unknown. An edge added to clear a report is worse than no edge.

So the useful output is not the corpus percentage but the per-entry triage: the
default summary ranks the entries where **nothing** is connected by how many
phenotypes are stranded, because an entry with 12 phenotypes and 0 connected is
one sitting's work and a different signal from one with 12 and 11.

    just list-disconnected-phenotypes                        # census + worklist
    just list-disconnected-phenotypes --format tsv           # one row per phenotype
    just list-disconnected-phenotypes kb/disorders/Foo.yaml  # one entry

See ``docs/quality-control.md`` and ``.claude/skills/dismech-compliance``.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Iterator
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dismech import kb_cache
from dismech.graph import build_causal_graph
from dismech.qc_plugins import CAUSAL_PREDICATES, causal_inlink_coverage
from dismech.yaml_io import safe_load_path

DEFAULT_KB_DIRS = ("kb/disorders",)

# Why a disconnected phenotype is still not isolated. Ordered from "nothing
# knows about this node" to "it explains something, but nothing explains it";
# a phenotype carries every class that applies.
ATTACH_ISOLATED = "ISOLATED"
ATTACH_TREATED = "TREATED"
ATTACH_READOUT = "READOUT"
ATTACH_NONCAUSAL = "NONCAUSAL_INBOUND"
ATTACH_SEQUELA_SOURCE = "SEQUELA_SOURCE"

# Predicates a treatment contributes: `targets` from `target_mechanisms`,
# `treats` from `target_phenotypes`.
TREATMENT_PREDICATES = frozenset({"targets", "treats"})

# Per-entry findings.
FINDING_ZERO = "ZERO_CONNECTED"
FINDING_PARTIAL = "PARTIAL"
FINDINGS = (FINDING_ZERO, FINDING_PARTIAL)


@dataclass
class PhenotypeRow:
    """One disconnected phenotype."""

    name: str
    subtype: str | None
    category: str | None
    attachment: list[str] = field(default_factory=list)

    @property
    def attachment_str(self) -> str:
        return ",".join(self.attachment) or ATTACH_ISOLATED


@dataclass
class EntryReport:
    path: str
    name: str
    connected: int
    total: int
    disconnected: list[PhenotypeRow] = field(default_factory=list)

    @property
    def percentage(self) -> float:
        return self.connected / self.total * 100 if self.total else 100.0

    @property
    def findings(self) -> list[str]:
        if not self.disconnected:
            return []
        return [FINDING_ZERO if self.connected == 0 else FINDING_PARTIAL]

    @property
    def isolated_count(self) -> int:
        return sum(1 for row in self.disconnected if not row.attachment)


def _classify_attachment(graph, names: set[str]) -> dict[str, list[str]]:
    """Which non-causal edges, if any, touch each named phenotype."""
    classes: dict[str, set[str]] = {name: set() for name in names}
    for edge in graph.edges:
        if edge.source == edge.target:
            continue
        if edge.target in classes:
            if edge.predicate in TREATMENT_PREDICATES:
                classes[edge.target].add(ATTACH_TREATED)
            elif edge.predicate == "readout":
                classes[edge.target].add(ATTACH_READOUT)
            elif edge.predicate not in CAUSAL_PREDICATES:
                classes[edge.target].add(ATTACH_NONCAUSAL)
        if edge.source in classes:
            if edge.predicate in CAUSAL_PREDICATES:
                classes[edge.source].add(ATTACH_SEQUELA_SOURCE)
            elif edge.predicate == "readout":
                classes[edge.source].add(ATTACH_READOUT)
    # Deterministic order, matching the declaration order above.
    order = (
        ATTACH_TREATED,
        ATTACH_READOUT,
        ATTACH_NONCAUSAL,
        ATTACH_SEQUELA_SOURCE,
    )
    return {
        name: [cls for cls in order if cls in found] for name, found in classes.items()
    }


def _display_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def assess(path: Path) -> EntryReport | None:
    """Assess one entry, or return None when it carries no phenotype nodes."""
    try:
        data = safe_load_path(path)
    except FileNotFoundError:
        print(f"warning: {_display_path(path)} does not exist", file=sys.stderr)
        return None
    if not isinstance(data, dict):
        return None

    connected, total, unconnected = causal_inlink_coverage(data)
    if total == 0:
        return None

    report = EntryReport(
        path=_display_path(path),
        name=str(data.get("name") or path.stem),
        connected=connected,
        total=total,
    )
    if not unconnected:
        return report

    # Subtype / category come from the YAML rather than the graph: NodeInfo
    # carries neither, and both are triage context rather than connectivity.
    meta: dict[str, dict[str, str | None]] = {}
    for item in data.get("phenotypes", []) or []:
        if isinstance(item, dict) and item.get("name"):
            meta[str(item["name"])] = {
                "subtype": item.get("subtype"),
                "category": item.get("category"),
            }

    attachment = _classify_attachment(build_causal_graph(data), set(unconnected))
    for name in unconnected:
        info = meta.get(name, {})
        report.disconnected.append(
            PhenotypeRow(
                name=name,
                subtype=info.get("subtype"),
                category=info.get("category"),
                attachment=attachment.get(name, []),
            )
        )
    return report


def iter_paths(files: list[str]) -> Iterator[Path]:
    if files:
        for raw in files:
            path = Path(raw)
            yield path if path.is_absolute() else (ROOT / path)
        return
    for directory in DEFAULT_KB_DIRS:
        base = ROOT / directory
        if base.is_dir():
            yield from sorted(base.glob("*.yaml"))


# --- reporting ---------------------------------------------------------------


def _aggregate(reports: list[EntryReport]) -> tuple[int, int]:
    return (
        sum(r.connected for r in reports),
        sum(r.total for r in reports),
    )


def render_summary(reports: list[EntryReport], *, limit: int, verbose: bool) -> None:
    connected, total = _aggregate(reports)
    zero = sorted(
        (r for r in reports if FINDING_ZERO in r.findings),
        key=lambda r: (-r.total, r.path),
    )
    partial = sorted(
        (r for r in reports if FINDING_PARTIAL in r.findings),
        key=lambda r: (r.percentage, -r.total, r.path),
    )

    pct = connected / total * 100 if total else 100.0
    print(f"Entries with phenotype nodes:        {len(reports)}")
    print(f"  no phenotype causally connected:   {len(zero)}")
    print(f"  some connected, some not:          {len(partial)}")
    print(
        f"  every phenotype connected:         {len(reports) - len(zero) - len(partial)}"
    )
    print(f"Phenotype nodes:                     {total}")
    print(f"  causally connected:                {connected} ({pct:.1f}%)")
    print()

    if zero:
        print(f"-- {len(zero)} entry(ies) where NO phenotype is causally connected --")
        print(
            "   Ranked by how many phenotypes are stranded: the pathograph stops at\n"
            "   the pathophysiology layer and the phenotypes render beside it. This is\n"
            "   the class a curator can act on in one sitting, not a number to drive\n"
            "   up -- an edge added to clear a report is worse than no edge.\n"
        )
        shown = zero if verbose else zero[:limit]
        for report in shown:
            isolated = report.isolated_count
            touch = (
                f", {report.total - isolated} touched by a non-causal edge"
                if isolated < report.total
                else ""
            )
            print(f"  {report.path}: 0/{report.total} connected{touch}")
        if len(shown) < len(zero):
            print(
                f"  ... and {len(zero) - len(shown)} more "
                f"(--limit 0 or --format list for all)"
            )
        print()

    if partial:
        worst = [r for r in partial if r.percentage < 50]
        print(
            f"-- {len(partial)} entry(ies) partially connected; "
            f"{len(worst)} below 50% --"
        )
        shown = partial if verbose else worst[:limit]
        for report in shown:
            print(
                f"  {report.path}: {report.connected}/{report.total} connected "
                f"({report.percentage:.0f}%)"
            )
        if len(shown) < len(worst):
            print(
                f"  ... and {len(worst) - len(shown)} more below 50% "
                f"(--format list for all)"
            )
        print()


def render_list(reports: list[EntryReport]) -> None:
    """Every entry with a gap, then each disconnected phenotype beneath it."""
    gaps = sorted(
        (r for r in reports if r.disconnected),
        key=lambda r: (r.percentage, -r.total, r.path),
    )
    for report in gaps:
        print(
            f"{report.path}: {report.connected}/{report.total} connected "
            f"({report.percentage:.0f}%)"
        )
        for row in report.disconnected:
            extra = []
            if row.subtype:
                extra.append(f"subtype={row.subtype}")
            if row.category:
                extra.append(f"category={row.category}")
            suffix = f"  [{'; '.join(extra)}]" if extra else ""
            print(f"    - {row.name}  ({row.attachment_str}){suffix}")


TSV_COLUMNS = (
    "path",
    "entry",
    "phenotype",
    "attachment",
    "subtype",
    "category",
    "entry_connected",
    "entry_total",
    "entry_percentage",
    "finding",
)


def render_tsv(reports: list[EntryReport]) -> None:
    print("\t".join(TSV_COLUMNS))
    for report in reports:
        finding = report.findings[0] if report.findings else "OK"
        for row in report.disconnected:
            print(
                "\t".join(
                    [
                        report.path,
                        report.name,
                        row.name,
                        row.attachment_str,
                        row.subtype or "",
                        row.category or "",
                        str(report.connected),
                        str(report.total),
                        f"{report.percentage:.1f}",
                        finding,
                    ]
                )
            )


def render_json(reports: list[EntryReport]) -> None:
    connected, total = _aggregate(reports)
    payload = {
        "entries_with_phenotypes": len(reports),
        "phenotypes": total,
        "phenotypes_connected": connected,
        "percentage": round(connected / total * 100, 2) if total else 100.0,
        "entries": [
            {
                "path": r.path,
                "name": r.name,
                "connected": r.connected,
                "total": r.total,
                "percentage": round(r.percentage, 2),
                "findings": r.findings,
                "disconnected": [
                    {
                        "name": row.name,
                        "attachment": row.attachment,
                        "subtype": row.subtype,
                        "category": row.category,
                    }
                    for row in r.disconnected
                ],
            }
            for r in reports
            if r.disconnected
        ],
    }
    print(json.dumps(payload, indent=2))


def main(argv: list[str] | None = None) -> int:
    kb_cache.default_off()

    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "files", nargs="*", help="KB YAML files (default: kb/disorders)"
    )
    parser.add_argument(
        "--format",
        choices=("summary", "list", "tsv", "json"),
        default="summary",
        help=(
            "summary (default) is the per-entry triage view; list adds every "
            "disconnected phenotype; tsv is one row per disconnected phenotype"
        ),
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=25,
        help="worklist rows per section in the summary (0 for all; default 25)",
    )
    parser.add_argument(
        "--zero-only",
        action="store_true",
        help="restrict the report to entries where no phenotype is connected",
    )
    parser.add_argument(
        "--min-phenotypes",
        type=int,
        default=0,
        help="only report entries carrying at least this many phenotype nodes",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help=(
            "exit 1 if any reported entry has a disconnected phenotype "
            "(report-only by default: at this scale a gate would be a baseline "
            "the size of the problem)"
        ),
    )
    parser.add_argument(
        "--fail-under",
        type=float,
        default=None,
        help="exit 1 if aggregate phenotype connectivity falls below this percent",
    )
    args = parser.parse_args(argv)

    reports = [r for r in (assess(p) for p in iter_paths(args.files)) if r is not None]
    if args.min_phenotypes:
        reports = [r for r in reports if r.total >= args.min_phenotypes]
    if args.zero_only:
        reports = [r for r in reports if FINDING_ZERO in r.findings]

    limit = len(reports) if args.limit <= 0 else args.limit
    if args.format == "tsv":
        render_tsv(reports)
    elif args.format == "json":
        render_json(reports)
    elif args.format == "list":
        render_summary(reports, limit=limit, verbose=False)
        render_list(reports)
    else:
        render_summary(reports, limit=limit, verbose=False)

    connected, total = _aggregate(reports)
    failed = False
    if args.fail_under is not None and total:
        pct = connected / total * 100
        if pct < args.fail_under:
            print(
                f"FAIL: phenotype connectivity {pct:.1f}% is below "
                f"{args.fail_under:.1f}%",
                file=sys.stderr,
            )
            failed = True
    if args.strict:
        hits = [r for r in reports if r.disconnected]
        if hits:
            print(
                f"FAIL: {len(hits)} entry(ies) carry a disconnected phenotype",
                file=sys.stderr,
            )
            failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
