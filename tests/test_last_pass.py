"""Tests for the last-substantive-pass report (issue #5334)."""

from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

import pytest
import yaml

from dismech.last_pass import (
    DEFAULT_BULK_THRESHOLD,
    STATUS_BULK_ONLY,
    STATUS_NO_HISTORY,
    STATUS_PASSED,
    build_report,
    detect_bulk_summaries,
    format_bulk,
    main,
    select,
)

AS_OF = datetime(2026, 8, 21, tzinfo=UTC)


def write_entry(kb: Path, kind_dir: str, slug: str) -> None:
    target = kb / kind_dir
    target.mkdir(parents=True, exist_ok=True)
    (target / f"{slug}.yaml").write_text(f"name: {slug}\n", encoding="utf-8")


def write_record(
    history: Path,
    kind_dir: str,
    slug: str,
    *,
    timestamp: str,
    summary: str,
    kind: str = "disorder",
    event_type: str = "EDIT",
    outcome: str = "changed",
    model: str | None = "claude-opus-5",
    superseded_slug: str | None = None,
) -> Path:
    directory = history / kind_dir / slug
    directory.mkdir(parents=True, exist_ok=True)
    target: dict[str, object] = {
        "kind": kind,
        "slug": slug,
        "path": f"kb/{kind_dir}/{slug}.yaml",
    }
    if superseded_slug:
        target["superseded_by"] = {
            "slug": superseded_slug,
            "path": f"kb/{kind_dir}/{superseded_slug}.yaml",
            "reason": "renamed",
        }
    record = {
        "history_version": 1,
        "target": target,
        "session": {
            "id": f"{timestamp}-test",
            "timestamp": timestamp,
            "actors": [
                {"type": "ai_agent", "name": "claude-code", "model": model}
                if model
                else {"type": "human", "name": "curator"}
            ],
        },
        "events": [
            {
                "type": event_type,
                "outcome": outcome,
                "summary": summary,
                "details": "test record",
            }
        ],
    }
    path = directory / f"{timestamp.replace(':', '')}-test.yaml"
    path.write_text(yaml.safe_dump(record, sort_keys=False), encoding="utf-8")
    return path


@pytest.fixture()
def corpus(tmp_path: Path) -> tuple[Path, Path]:
    """A miniature KB plus history tree exercising each status."""
    kb = tmp_path / "kb"
    history = tmp_path / "history"

    for slug in ("Swept", "Curated", "Untracked", "NoChangeOnly"):
        write_entry(kb, "disorders", slug)
    write_entry(kb, "modules", "some_module")

    # A bulk sweep: one summary across enough distinct slugs to trip the threshold.
    for index in range(DEFAULT_BULK_THRESHOLD):
        slug = f"Bulk{index}"
        write_entry(kb, "disorders", slug)
        write_record(
            history,
            "disorders",
            slug,
            timestamp="2026-08-01T00:00:00Z",
            summary="Add public dataset records from GEO",
        )
    write_record(
        history,
        "disorders",
        "Swept",
        timestamp="2026-08-01T00:00:00Z",
        summary="Add public dataset records from GEO",
    )
    # Swept also has one real pass, but older than the sweep.
    write_record(
        history,
        "disorders",
        "Swept",
        timestamp="2026-06-01T00:00:00Z",
        summary="Add the neurosteroid withdrawal arm",
    )
    write_record(
        history,
        "disorders",
        "Curated",
        timestamp="2026-08-10T00:00:00Z",
        summary="Rework the pathograph around a single hub node",
        model="claude-fable-5",
    )
    write_record(
        history,
        "disorders",
        "NoChangeOnly",
        timestamp="2026-08-10T00:00:00Z",
        summary="Compliance audit, nothing to change",
        event_type="AUDIT",
        outcome="no_change",
    )
    write_record(
        history,
        "modules",
        "some_module",
        timestamp="2026-07-01T00:00:00Z",
        summary="Add the senolytic drug-target pattern",
        kind="module",
    )
    return kb, history


def test_status_classification(corpus: tuple[Path, Path]) -> None:
    kb, history = corpus
    report = build_report(kb_dir=kb, history_dir=history)
    status = {t.slug: t.status for t in report.targets}

    assert status["Curated"] == STATUS_PASSED
    assert status["Swept"] == STATUS_PASSED  # the June pass still counts
    assert status["Untracked"] == STATUS_NO_HISTORY
    # An audit that changed nothing is not a pass.
    assert status["NoChangeOnly"] == STATUS_BULK_ONLY
    # Entries carrying only the sweep have no substantive pass.
    assert status["Bulk0"] == STATUS_BULK_ONLY


def test_bulk_sweep_does_not_count_as_a_pass(corpus: tuple[Path, Path]) -> None:
    kb, history = corpus
    report = build_report(kb_dir=kb, history_dir=history)
    swept = next(t for t in report.targets if t.slug == "Swept")

    assert swept.last_touch is not None
    assert swept.last_touch.timestamp.startswith("2026-08-01")
    assert swept.last_pass is not None
    assert swept.last_pass.timestamp.startswith("2026-06-01")
    # The entry looks fresh in git and in the raw history tree, but is not.
    assert swept.touch_is_bulk is True
    assert swept.last_pass.age_days(AS_OF) == 81


def test_bulk_threshold_is_a_dial(corpus: tuple[Path, Path]) -> None:
    kb, history = corpus
    loose = build_report(kb_dir=kb, history_dir=history, bulk_threshold=10_000)
    swept = next(t for t in loose.targets if t.slug == "Swept")

    # With no sweep detected, the August record is accepted as the last pass.
    assert loose.bulk_summaries == {}
    assert swept.last_pass is not None
    assert swept.last_pass.timestamp.startswith("2026-08-01")
    assert swept.touch_is_bulk is False


def test_legacy_rollups_are_exempt_from_bulk_detection() -> None:
    summary = "legacy curation summary: 4 recorded events, 2025-12-15 to 2025-12-15."
    slugs = {f"slug{i}" for i in range(50)}
    assert detect_bulk_summaries({summary: slugs}, DEFAULT_BULK_THRESHOLD) == {}


def test_supersession_attributes_work_to_the_successor(tmp_path: Path) -> None:
    kb = tmp_path / "kb"
    history = tmp_path / "history"
    write_entry(kb, "disorders", "New_Name")
    write_record(
        history,
        "disorders",
        "Old_Name",
        timestamp="2026-05-05T00:00:00Z",
        summary="Curate the original entry",
        superseded_slug="New_Name",
    )

    report = build_report(kb_dir=kb, history_dir=history)
    successor = next(t for t in report.targets if t.slug == "New_Name")
    assert successor.status == STATUS_PASSED
    assert successor.last_pass is not None
    assert successor.last_pass.timestamp.startswith("2026-05-05")


@pytest.mark.parametrize(
    ("earlier", "later"),
    [
        # A non-UTC offset: 20:00-05:00 is 01:00Z the *next* day, so it is the
        # later session, but it sorts before "…23:00:00Z" as a string.
        ("2026-08-01T23:00:00Z", "2026-08-01T20:00:00-05:00"),
        # Fractional seconds: "." sorts before "Z".
        ("2026-08-01T23:00:00Z", "2026-08-01T23:00:00.500000Z"),
    ],
)
def test_newest_event_wins_across_timestamp_formats(
    tmp_path: Path, earlier: str, later: str
) -> None:
    """The newest *moment* wins, not the lexically largest string.

    ``src/dismech/schema/history.yaml`` permits ``[+-]HH:MM`` offsets and
    fractional seconds as well as ``Z``. Every committed record ends in ``Z``
    and ``scripts/new_history.py`` only ever emits ``Z``, but hand-written
    records are supported and the schema blesses both forms — and picking the
    newest event is this module's single core operation.
    """
    kb = tmp_path / "kb"
    history = tmp_path / "history"
    write_entry(kb, "disorders", "Offset_Entry")
    write_record(
        history,
        "disorders",
        "Offset_Entry",
        timestamp=earlier,
        summary="EARLIER pass",
    )
    write_record(
        history,
        "disorders",
        "Offset_Entry",
        timestamp=later,
        summary="LATER pass",
    )

    report = build_report(kb_dir=kb, history_dir=history)
    target = next(t for t in report.targets if t.slug == "Offset_Entry")
    assert target.last_pass is not None
    assert target.last_pass.summary == "LATER pass"
    assert target.last_touch is not None
    assert target.last_touch.summary == "LATER pass"


def test_worklist_orders_unpassed_entries_first(corpus: tuple[Path, Path]) -> None:
    kb, history = corpus
    report = build_report(kb_dir=kb, history_dir=history)
    ordered = select(report, as_of=AS_OF)

    unpassed = [t for t in ordered if t.last_pass is None]
    passed = [t for t in ordered if t.last_pass is not None]
    assert ordered[: len(unpassed)] == unpassed, "unpassed entries must sort first"
    # Within the passed group, stalest first.
    timestamps = [t.last_pass.timestamp for t in passed if t.last_pass]
    assert timestamps == sorted(timestamps)


def test_filters(corpus: tuple[Path, Path]) -> None:
    kb, history = corpus
    report = build_report(kb_dir=kb, history_dir=history)

    only_modules = select(report, as_of=AS_OF, kinds=["module"])
    assert [t.slug for t in only_modules] == ["some_module"]

    fable = select(report, as_of=AS_OF, model="fable")
    assert [t.slug for t in fable] == ["Curated"]

    never = select(report, as_of=AS_OF, status=STATUS_NO_HISTORY)
    assert [t.slug for t in never] == ["Untracked"]

    old = select(report, as_of=AS_OF, status=STATUS_PASSED, min_age_days=60)
    assert [t.slug for t in old] == ["Swept"]


def test_unreadable_record_is_reported_not_fatal(
    corpus: tuple[Path, Path], tmp_path: Path
) -> None:
    kb, history = corpus
    broken = history / "disorders" / "Curated" / "broken.yaml"
    broken.write_text("{ not: valid: yaml", encoding="utf-8")

    report = build_report(kb_dir=kb, history_dir=history)
    assert len(report.unreadable) == 1
    assert (
        next(t for t in report.targets if t.slug == "Curated").status == STATUS_PASSED
    )


@pytest.mark.parametrize(
    "body",
    [
        # `session:` as a string rather than a mapping.
        "history_version: 1\ntarget: {kind: disorder, slug: Curated}\nsession: today\n",
        # `actors:` as a mapping rather than a list.
        (
            "history_version: 1\n"
            "target: {kind: disorder, slug: Curated}\n"
            "session:\n"
            "  timestamp: '2026-08-11T00:00:00Z'\n"
            "  actors: {type: human, name: curator}\n"
            "events: []\n"
        ),
        # `events:` as a mapping rather than a list.
        (
            "history_version: 1\n"
            "target: {kind: disorder, slug: Curated}\n"
            "session: {timestamp: '2026-08-11T00:00:00Z'}\n"
            "events: {type: EDIT}\n"
        ),
    ],
)
def test_schema_invalid_record_is_reported_not_fatal(
    corpus: tuple[Path, Path], body: str
) -> None:
    """Parseable YAML of the wrong *shape* must not abort the report either.

    `history/` records are not schema-checked here, so the guard has to cover
    more than "YAML will not load". Each of these loads fine and then raises on
    attribute or index access, which used to take the whole run down and
    contradict the point of collecting `unreadable`.
    """
    kb, history = corpus
    (history / "disorders" / "Curated" / "malformed.yaml").write_text(
        body, encoding="utf-8"
    )

    report = build_report(kb_dir=kb, history_dir=history)
    assert len(report.unreadable) == 1
    curated = next(t for t in report.targets if t.slug == "Curated")
    assert curated.status == STATUS_PASSED
    assert curated.last_pass is not None
    assert curated.last_pass.summary.startswith("Rework the pathograph")


def test_model_is_read_from_the_agent_actor_not_the_first_one(tmp_path: Path) -> None:
    """A human listed first must not hide the agent's model and tool.

    Every committed multi-actor record happens to list the agent first, so
    reading `actors[0]` works today — but that is how `just new-history` orders
    them, not something the schema requires.
    """
    kb = tmp_path / "kb"
    history = tmp_path / "history"
    write_entry(kb, "disorders", "Co_Curated")
    directory = history / "disorders" / "Co_Curated"
    directory.mkdir(parents=True)
    (directory / "session.yaml").write_text(
        yaml.safe_dump(
            {
                "history_version": 1,
                "target": {
                    "kind": "disorder",
                    "slug": "Co_Curated",
                    "path": "kb/disorders/Co_Curated.yaml",
                },
                "session": {
                    "id": "s1",
                    "timestamp": "2026-08-10T00:00:00Z",
                    "actors": [
                        {"type": "human", "name": "curator"},
                        {
                            "type": "ai_agent",
                            "name": "claude-code",
                            "model": "claude-opus-5",
                            "agent_tool": "claude-code",
                        },
                    ],
                },
                "events": [
                    {
                        "type": "EDIT",
                        "outcome": "changed",
                        "summary": "Co-curated pass",
                        "details": "test record",
                    }
                ],
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )

    report = build_report(kb_dir=kb, history_dir=history)
    target = next(t for t in report.targets if t.slug == "Co_Curated")
    assert target.last_pass is not None
    assert target.last_pass.model == "claude-opus-5"
    assert target.last_pass.agent_tool == "claude-code"
    assert select(report, as_of=AS_OF, model="opus") == [target]


def test_list_bulk_output_greps_against_the_ledger(corpus: tuple[Path, Path]) -> None:
    """`--list-bulk` must print a summary as written, not its casefolded key."""
    kb, history = corpus
    report = build_report(kb_dir=kb, history_dir=history)

    assert "add public dataset records from geo" in report.bulk_summaries
    assert (
        report.bulk_display["add public dataset records from geo"]
        == "Add public dataset records from GEO"
    )
    assert "Add public dataset records from GEO" in format_bulk(report)


def test_kind_filter_does_not_change_classification(corpus: tuple[Path, Path]) -> None:
    """`--kind` is a view. Narrowing it must not re-run bulk detection narrowed.

    Bulk detection counts distinct targets, so building over one kind looks for
    a 15-target sweep inside that kind alone — which a smaller corpus can never
    reach, and which would stop recognising a cross-kind campaign.
    """
    kb, history = corpus
    whole = build_report(kb_dir=kb, history_dir=history)
    expected = {
        t.slug: t.status for t in select(whole, as_of=AS_OF, kinds=("disorder",))
    }

    narrowed = build_report(kb_dir=kb, history_dir=history, kinds=("disorder",))
    assert {t.slug: t.status for t in select(narrowed, as_of=AS_OF)} == expected, (
        "building narrowed changed the verdicts; select() must do the filtering"
    )


@pytest.mark.parametrize("fmt", ["summary", "tsv", "json"])
def test_cli_formats(corpus: tuple[Path, Path], capsys, fmt: str) -> None:
    kb, history = corpus
    exit_code = main(
        [
            "--kb-dir",
            str(kb),
            "--history-dir",
            str(history),
            "--as-of",
            "2026-08-21",
            "--format",
            fmt,
        ]
    )
    assert exit_code == 0
    assert "Swept" in capsys.readouterr().out


def test_cli_list_bulk(corpus: tuple[Path, Path], capsys) -> None:
    kb, history = corpus
    assert (
        main(
            [
                "--kb-dir",
                str(kb),
                "--history-dir",
                str(history),
                "--list-bulk",
            ]
        )
        == 0
    )
    # Printed as written, not as the casefolded matching key, so the line can be
    # pasted straight back at `history/`.
    assert "Add public dataset records from GEO" in capsys.readouterr().out


def test_report_runs_against_the_real_repository() -> None:
    """The committed corpus must actually be readable by the report."""
    report = build_report()
    assert len(report.targets) > 100
    assert report.by_status(STATUS_PASSED), "no entry has a recorded substantive pass"
    assert not report.unreadable, f"unreadable history records: {report.unreadable}"
