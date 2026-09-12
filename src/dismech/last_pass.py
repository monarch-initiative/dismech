"""When was each KB entry last given a *real* curation pass?

Git history cannot answer this. ``git log -- kb/disorders/Foo.yaml`` reports every
touch, so a mass reformat, a bulk accession backfill, or a whole-KB slot migration
all look exactly like somebody sitting down and re-curating the entry. That is the
objection raised in issue #5334, and it is the reason ``updated_date`` keeps being
proposed for un-deprecation.

The ``history/`` layer already records what ``updated_date`` could not: per-session
actor, model, agent tool, event type, outcome, and the sections touched. It does so
append-only, one file per session, which is why it does not reintroduce the merge
conflicts that got ``updated_date`` deprecated in the first place (#2892, #3151).

But ``history/`` inherits the same blind spot on its own: **a bulk sweep writes a
history record too.** 700 entries carry an identical ``Backfill therapeutic_modality``
record; 320 carry an identical ``Add public dataset records from GEO``. Reading only
the newest record would report those entries as freshly curated.

So this module separates two questions:

``last touch``
    the newest history record of any kind

``last substantive pass``
    the newest record that is *not* part of a detected bulk sweep and that actually
    changed the entry (``outcome: changed``)

A **bulk sweep** is detected structurally, not from a hand-maintained list: an event
whose summary recurs verbatim across at least ``--bulk-threshold`` distinct targets
was a campaign over many entries, not a pass over this one. The classification is a
heuristic over a continuous gradient, so it is reported rather than hidden — see
``--list-bulk``.

One documented exemption: ``GENERAL`` events whose summary begins with
``Legacy curation summary`` are the roll-ups that imported pre-``history/`` activity.
Several share a summary by coincidence (same event count, same date range) without
being a campaign, so they are never classified as bulk.

The output is ordered stalest-first, which makes it a worklist: the answer to "in
what order should periodic re-passes happen".
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from collections import defaultdict
from collections.abc import Iterable, Iterator
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from dismech.yaml_io import safe_load_path

_REPO_ROOT = Path(__file__).resolve().parents[2]
_DEFAULT_KB = _REPO_ROOT / "kb"
_DEFAULT_HISTORY = _REPO_ROOT / "history"

#: history ``target.kind`` -> directory under ``kb/``. Kinds outside this map
#: (``schema``, ``other``) are provenance for non-KB files and are not reported.
KB_KINDS: dict[str, str] = {
    "disorder": "disorders",
    "module": "modules",
    "comorbidity": "comorbidities",
}

#: history ``target.kind`` -> directory under ``history/``
HISTORY_DIRS: dict[str, str] = {
    "disorder": "disorders",
    "module": "modules",
    "comorbidity": "comorbidities",
}

#: A summary recurring across at least this many distinct targets is a bulk sweep.
DEFAULT_BULK_THRESHOLD = 15

#: Summaries never treated as bulk however often they recur (see module docstring).
_BULK_EXEMPT = re.compile(r"^legacy curation summary\b")

#: An entry's status with respect to substantive curation.
STATUS_PASSED = "PASSED"
STATUS_BULK_ONLY = "BULK_ONLY"
STATUS_NO_HISTORY = "NO_HISTORY"


def _normalize_summary(summary: str) -> str:
    """Collapse a summary to its comparison key."""
    return " ".join(str(summary or "").split()).casefold()


@dataclass(frozen=True)
class Event:
    """One event drawn from one history record, flattened for ranking."""

    slug: str
    kind: str
    timestamp: str
    event_type: str
    outcome: str
    summary: str
    sections: tuple[str, ...]
    actor_type: str | None
    actor_name: str | None
    model: str | None
    agent_tool: str | None
    record: str

    @property
    def date(self) -> str:
        """Calendar date of the session, for display."""
        return self.timestamp[:10]

    def age_days(self, as_of: datetime) -> int | None:
        """Whole days between this event and ``as_of``; ``None`` if unreadable."""
        moment = _parse_timestamp(self.timestamp)
        if moment is None:
            return None
        return max(0, (as_of - moment).days)


@dataclass
class TargetReport:
    """Per-entry verdict."""

    kind: str
    slug: str
    path: str
    status: str
    last_pass: Event | None = None
    last_touch: Event | None = None
    record_count: int = 0
    bulk_event_count: int = 0

    @property
    def touch_is_bulk(self) -> bool:
        """True when the newest record is a sweep, i.e. the entry *looks* fresh."""
        if self.last_touch is None or self.last_pass is None:
            return False
        return self.last_touch.timestamp > self.last_pass.timestamp

    def as_dict(self, as_of: datetime) -> dict[str, object]:
        """JSON/TSV-friendly projection."""
        passed = self.last_pass
        touch = self.last_touch
        return {
            "kind": self.kind,
            "slug": self.slug,
            "path": self.path,
            "status": self.status,
            "last_pass": passed.timestamp if passed else None,
            "age_days": passed.age_days(as_of) if passed else None,
            "event_type": passed.event_type if passed else None,
            "summary": passed.summary if passed else None,
            "model": passed.model if passed else None,
            "agent_tool": passed.agent_tool if passed else None,
            "actor_type": passed.actor_type if passed else None,
            "last_touch": touch.timestamp if touch else None,
            "touch_is_bulk": self.touch_is_bulk,
            "records": self.record_count,
            "bulk_events": self.bulk_event_count,
        }


@dataclass
class Report:
    """Whole-corpus result."""

    targets: list[TargetReport] = field(default_factory=list)
    bulk_summaries: dict[str, int] = field(default_factory=dict)
    bulk_threshold: int = DEFAULT_BULK_THRESHOLD
    unreadable: list[str] = field(default_factory=list)

    def by_status(self, status: str) -> list[TargetReport]:
        return [t for t in self.targets if t.status == status]


def _parse_timestamp(value: str) -> datetime | None:
    """Parse a history timestamp into an aware UTC datetime."""
    text = str(value or "").strip()
    if not text:
        return None
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        moment = datetime.fromisoformat(text)
    except ValueError:
        return None
    if moment.tzinfo is None:
        moment = moment.replace(tzinfo=timezone.utc)
    return moment.astimezone(timezone.utc)


def _iter_record_paths(history_dir: Path, kinds: Iterable[str]) -> Iterator[Path]:
    for kind in kinds:
        root = history_dir / HISTORY_DIRS[kind]
        if not root.is_dir():
            continue
        yield from sorted(root.glob("*/*.yaml"))


def _record_slug(record: dict, path: Path) -> str:
    """Slug a record is attributed to, following a supersession when present.

    History records are append-only, so a renamed entry keeps its original
    ``target.slug`` and records where it went in ``target.superseded_by``. For
    "when was this entry last curated" the work belongs to the successor.
    """
    target = record.get("target") or {}
    superseded = target.get("superseded_by") or {}
    if isinstance(superseded, dict) and superseded.get("slug"):
        return str(superseded["slug"])
    if target.get("slug"):
        return str(target["slug"])
    return path.parent.name


def load_events(
    history_dir: Path, kinds: Iterable[str]
) -> tuple[list[Event], dict[str, set[str]], list[str]]:
    """Flatten every history event, and index summaries by the slugs carrying them."""
    events: list[Event] = []
    summary_slugs: dict[str, set[str]] = defaultdict(set)
    unreadable: list[str] = []

    for path in _iter_record_paths(history_dir, kinds):
        try:
            record = safe_load_path(path)
        except Exception:  # noqa: BLE001 - a malformed record must not abort the report
            unreadable.append(str(path))
            continue
        if not isinstance(record, dict) or "target" not in record:
            unreadable.append(str(path))
            continue

        target = record.get("target") or {}
        kind = str(target.get("kind") or "")
        if kind not in HISTORY_DIRS:
            continue
        slug = _record_slug(record, path)
        session = record.get("session") or {}
        timestamp = str(session.get("timestamp") or "")
        actors = session.get("actors") or [{}]
        actor = actors[0] if isinstance(actors[0], dict) else {}

        for raw in record.get("events") or []:
            if not isinstance(raw, dict):
                continue
            summary = str(raw.get("summary") or "")
            sections = raw.get("sections") or []
            events.append(
                Event(
                    slug=slug,
                    kind=kind,
                    timestamp=timestamp,
                    event_type=str(raw.get("type") or ""),
                    outcome=str(raw.get("outcome") or ""),
                    summary=summary,
                    sections=tuple(str(s) for s in sections),
                    actor_type=actor.get("type"),
                    actor_name=actor.get("name"),
                    model=actor.get("model"),
                    agent_tool=actor.get("agent_tool"),
                    record=str(path),
                )
            )
            summary_slugs[_normalize_summary(summary)].add(slug)

    return events, summary_slugs, unreadable


def detect_bulk_summaries(
    summary_slugs: dict[str, set[str]], threshold: int
) -> dict[str, int]:
    """Summaries that recur across at least ``threshold`` distinct targets."""
    return {
        summary: len(slugs)
        for summary, slugs in summary_slugs.items()
        if len(slugs) >= threshold and not _BULK_EXEMPT.match(summary) and summary
    }


def is_substantive(event: Event, bulk_summaries: dict[str, int]) -> bool:
    """A pass over *this* entry, as opposed to a sweep or a no-op review."""
    if event.outcome != "changed":
        return False
    return _normalize_summary(event.summary) not in bulk_summaries


def build_report(
    kb_dir: Path = _DEFAULT_KB,
    history_dir: Path = _DEFAULT_HISTORY,
    kinds: Iterable[str] = tuple(KB_KINDS),
    bulk_threshold: int = DEFAULT_BULK_THRESHOLD,
) -> Report:
    """Compute the last substantive pass for every KB entry of the given kinds."""
    kinds = tuple(kinds)
    events, summary_slugs, unreadable = load_events(history_dir, kinds)
    bulk_summaries = detect_bulk_summaries(summary_slugs, bulk_threshold)

    by_slug: dict[tuple[str, str], list[Event]] = defaultdict(list)
    for event in events:
        by_slug[(event.kind, event.slug)].append(event)

    targets: list[TargetReport] = []
    for kind in kinds:
        kb_subdir = kb_dir / KB_KINDS[kind]
        if not kb_subdir.is_dir():
            continue
        for entry in sorted(kb_subdir.glob("*.yaml")):
            slug = entry.stem
            entry_events = by_slug.get((kind, slug), [])
            report = TargetReport(
                kind=kind,
                slug=slug,
                path=str(entry.relative_to(kb_dir.parent))
                if kb_dir.parent in entry.parents
                else str(entry),
                status=STATUS_NO_HISTORY,
                record_count=len({e.record for e in entry_events}),
                bulk_event_count=sum(
                    1
                    for e in entry_events
                    if _normalize_summary(e.summary) in bulk_summaries
                ),
            )
            if entry_events:
                report.last_touch = max(entry_events, key=lambda e: e.timestamp)
                substantive = [
                    e for e in entry_events if is_substantive(e, bulk_summaries)
                ]
                if substantive:
                    report.last_pass = max(substantive, key=lambda e: e.timestamp)
                    report.status = STATUS_PASSED
                else:
                    report.status = STATUS_BULK_ONLY
            targets.append(report)

    return Report(
        targets=targets,
        bulk_summaries=bulk_summaries,
        bulk_threshold=bulk_threshold,
        unreadable=unreadable,
    )


def select(
    report: Report,
    *,
    as_of: datetime,
    kinds: Iterable[str] | None = None,
    status: str | None = None,
    model: str | None = None,
    min_age_days: int | None = None,
) -> list[TargetReport]:
    """Filter and order targets stalest-first; entries with no pass sort first."""
    kinds = set(kinds) if kinds else None
    selected: list[TargetReport] = []
    for target in report.targets:
        if kinds and target.kind not in kinds:
            continue
        if status and target.status != status:
            continue
        if model:
            actual = (target.last_pass.model if target.last_pass else None) or ""
            if model.casefold() not in actual.casefold():
                continue
        if min_age_days is not None:
            age = target.last_pass.age_days(as_of) if target.last_pass else None
            if age is None:
                # No recorded pass is staler than any recorded one; keep it.
                pass
            elif age < min_age_days:
                continue
        selected.append(target)

    def sort_key(target: TargetReport) -> tuple[int, str, str]:
        # Entries with no substantive pass rank first — they are the priority — and
        # within that group the one untouched longest comes first, so a sweep last
        # week does not outrank an entry nothing has looked at since December.
        if target.last_pass is None:
            touched = target.last_touch.timestamp if target.last_touch else ""
            return (0, touched, target.slug)
        return (1, target.last_pass.timestamp, target.slug)

    return sorted(selected, key=sort_key)


def format_summary(
    report: Report, selected: list[TargetReport], as_of: datetime, limit: int
) -> str:
    out: list[str] = []
    out.append("Last substantive curation pass per KB entry")
    out.append(f"as of {as_of.date().isoformat()}")
    out.append("")

    total = len(report.targets)
    passed = report.by_status(STATUS_PASSED)
    bulk_only = report.by_status(STATUS_BULK_ONLY)
    no_history = report.by_status(STATUS_NO_HISTORY)
    ages = [
        age
        for t in passed
        if t.last_pass and (age := t.last_pass.age_days(as_of)) is not None
    ]
    stale_looking = [t for t in passed if t.touch_is_bulk]

    out.append(f"  {total} KB entries")
    median = f"{statistics.median(ages):.0f}d" if ages else "n/a"
    out.append(
        f"  {len(passed):>5} PASSED      substantive pass recorded "
        f"(median age {median})"
    )
    out.append(
        f"  {len(bulk_only):>5} BULK_ONLY   history exists, but only bulk sweeps "
        "or no-change events"
    )
    out.append(f"  {len(no_history):>5} NO_HISTORY  no history record at all")
    out.append(
        f"  {len(stale_looking):>5} of the PASSED entries have a bulk sweep as their "
        "NEWEST record"
    )
    out.append("")
    out.append(
        f"  bulk sweeps: {len(report.bulk_summaries)} summaries recurring across "
        f">={report.bulk_threshold} entries (--list-bulk to see them)"
    )
    if report.unreadable:
        out.append(f"  {len(report.unreadable)} unreadable history record(s) skipped")
    out.append("")

    shown = selected[:limit] if limit else selected
    out.append(
        f"Re-pass worklist — stalest {len(shown)} of {len(selected)} selected entries:"
    )
    out.append(
        f"  {'STATUS':<10} {'AGE':>5}  {'ENTRY':<46} {'LAST PASS':<11} "
        f"{'TYPE':<8} MODEL"
    )
    for target in shown:
        passed_event = target.last_pass
        if passed_event is None:
            age = "-"
            date = target.last_touch.date if target.last_touch else "-"
            event_type = "-"
            model = "-"
        else:
            days = passed_event.age_days(as_of)
            age = f"{days}d" if days is not None else "?"
            date = passed_event.date
            event_type = passed_event.event_type
            model = passed_event.model or passed_event.actor_name or "-"
        flag = " *" if target.touch_is_bulk else ""
        out.append(
            f"  {target.status:<10} {age:>5}  {target.slug[:46]:<46} {date:<11} "
            f"{event_type:<8} {model}{flag}"
        )
    out.append("")
    out.append(
        "  LAST PASS for a BULK_ONLY/NO_HISTORY row is the newest *touch*, not a pass"
    )
    out.append("  * newest history record on this entry is a bulk sweep")
    return "\n".join(out)


def format_tsv(selected: list[TargetReport], as_of: datetime) -> str:
    columns = [
        "kind",
        "slug",
        "path",
        "status",
        "last_pass",
        "age_days",
        "event_type",
        "model",
        "agent_tool",
        "actor_type",
        "last_touch",
        "touch_is_bulk",
        "records",
        "bulk_events",
        "summary",
    ]
    rows = ["\t".join(columns)]
    for target in selected:
        record = target.as_dict(as_of)
        rows.append(
            "\t".join(
                " ".join(str(record.get(column) or "").split()) for column in columns
            )
        )
    return "\n".join(rows)


def format_bulk(report: Report) -> str:
    out = [
        f"Bulk sweeps detected (summary recurring across >={report.bulk_threshold} "
        "distinct entries):",
        "",
    ]
    for summary, count in sorted(
        report.bulk_summaries.items(), key=lambda kv: (-kv[1], kv[0])
    ):
        out.append(f"  {count:>5}  {summary}")
    if not report.bulk_summaries:
        out.append("  (none)")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--kb-dir", type=Path, default=_DEFAULT_KB)
    parser.add_argument("--history-dir", type=Path, default=_DEFAULT_HISTORY)
    parser.add_argument(
        "--kind",
        action="append",
        choices=sorted(KB_KINDS),
        help="restrict to a target kind (repeatable; default all)",
    )
    parser.add_argument(
        "--status",
        choices=(STATUS_PASSED, STATUS_BULK_ONLY, STATUS_NO_HISTORY),
        help="only entries with this status",
    )
    parser.add_argument(
        "--model",
        help="only entries whose last substantive pass used a matching model "
        "(substring, case-insensitive)",
    )
    parser.add_argument(
        "--min-age-days",
        type=int,
        help="only entries whose last pass is at least this old",
    )
    parser.add_argument(
        "--bulk-threshold",
        type=int,
        default=DEFAULT_BULK_THRESHOLD,
        help=f"summary recurrence that marks a sweep (default {DEFAULT_BULK_THRESHOLD})",
    )
    parser.add_argument(
        "--limit", type=int, default=25, help="rows in summary output (0 = all)"
    )
    parser.add_argument(
        "--format", choices=("summary", "tsv", "json"), default="summary"
    )
    parser.add_argument(
        "--list-bulk",
        action="store_true",
        help="print the detected bulk sweeps and exit",
    )
    parser.add_argument(
        "--as-of",
        help="ISO date to measure ages against (default: now, UTC)",
    )
    args = parser.parse_args(argv)

    as_of = _parse_timestamp(args.as_of) if args.as_of else datetime.now(timezone.utc)
    if as_of is None:
        parser.error(f"could not parse --as-of {args.as_of!r}")

    kinds = tuple(args.kind) if args.kind else tuple(KB_KINDS)
    report = build_report(
        kb_dir=args.kb_dir,
        history_dir=args.history_dir,
        kinds=kinds,
        bulk_threshold=args.bulk_threshold,
    )

    if args.list_bulk:
        print(format_bulk(report))
        return 0

    selected = select(
        report,
        as_of=as_of,
        kinds=kinds,
        status=args.status,
        model=args.model,
        min_age_days=args.min_age_days,
    )

    if args.format == "json":
        print(
            json.dumps(
                {
                    "as_of": as_of.isoformat(),
                    "bulk_threshold": report.bulk_threshold,
                    "bulk_summaries": report.bulk_summaries,
                    "entries": [t.as_dict(as_of) for t in selected],
                },
                indent=2,
            )
        )
    elif args.format == "tsv":
        print(format_tsv(selected, as_of))
    else:
        print(format_summary(report, selected, as_of, args.limit))
    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
