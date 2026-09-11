"""Unit tests for the pure schedule-config parser/expander (issue #11657).

Table-driven: each test walks a table of cases rather than exploding into one
pytest node per case, so the suite stays small while covering every branch. A
failing row names itself in the assert message.
"""

from __future__ import annotations

from datetime import date, datetime, time

import pytest

from dismech.schedule.config import (
    ScheduleConfig,
    ScheduleConfigError,
    Window,
    dst_transitions,
    expand,
    load_config,
    parse_config,
)

LA = "America/Los_Angeles"


def base_config(**overrides) -> dict:
    data = {
        "version": 1,
        "timezone": LA,
        "window": {"start_local": "20:00", "end_local": "00:00"},
        "recurrence": "workday",
        "custom_cron_local": None,
        "expiry": {"mode": "none", "value": None},
        "max_active": 1,
        "model": "claude-sonnet-5",
        "routine": {"trigger_id": None, "environment_id": "env_01Qs4qSVQcgqzrywAKajYQnj"},
    }
    data.update(overrides)
    return data


def test_parse_and_load_valid_config(tmp_path):
    cfg = parse_config(base_config())
    assert isinstance(cfg, ScheduleConfig)
    assert cfg.recurrence == "workday"
    assert (cfg.window.start_local, cfg.window.end_local) == (time(20, 0), time(0, 0))
    assert cfg.max_active == 1
    assert cfg.model == "claude-sonnet-5"
    # custom recurrence carries its local cron through.
    assert parse_config(
        base_config(recurrence="custom", custom_cron_local="0 9 * * 1")
    ).custom_cron_local == "0 9 * * 1"
    # load_config reads and validates the same shape from YAML on disk.
    p = tmp_path / "schedule-config.yaml"
    p.write_text(
        "version: 1\ntimezone: America/Los_Angeles\n"
        "window:\n  start_local: '20:00'\n  end_local: '00:00'\n"
        "recurrence: workday\nexpiry:\n  mode: none\n  value: null\n"
        "max_active: 1\nmodel: claude-sonnet-5\n"
        "routine:\n  trigger_id: null\n  environment_id: env_x\n",
        encoding="utf-8",
    )
    assert load_config(p).routine.environment_id == "env_x"


def test_parse_rejects_bad_values():
    cases = [
        ({"version": 2}, "version"),
        ({"timezone": "Mars/Olympus"}, "timezone"),
        ({"recurrence": "hourly"}, "recurrence"),
        ({"max_active": 0}, "max_active"),
        ({"max_active": 3}, "not supported"),
        ({"window": {"start_local": "20:30", "end_local": "00:00"}}, "whole number of hours"),
        ({"window": {"start_local": "20:00", "end_local": "20:00"}}, "empty"),
        ({"recurrence": "custom", "custom_cron_local": None}, "custom"),
        ({"custom_cron_local": "0 9 * * 1"}, "only valid"),  # non-custom recurrence
        ({"expiry": {"mode": "days", "value": 0}}, "positive integer"),
        ({"expiry": {"mode": "date", "value": "not-a-date"}}, "valid date"),
        ({"expiry": {"mode": "none", "value": 7}}, "must be empty"),
    ]
    for overrides, message in cases:
        with pytest.raises(ScheduleConfigError) as exc:
            parse_config(base_config(**overrides))
        assert message in str(exc.value), f"{overrides} -> {exc.value!r}"


def test_window_fire_hours():
    # end_local 00:00 means end-of-day; a window may cross local midnight.
    assert Window(time(20, 0), time(0, 0)).fire_hours() == [20, 21, 22, 23]
    assert Window(time(22, 0), time(2, 0)).fire_hours() == [22, 23, 0, 1]


def test_expand_dst_shifts_utc_by_one_hour():
    # Jan -> PST (UTC-8): 20:00-23:00 local is 04:00-07:00 UTC the next day, so
    # Mon-Fri evenings become Tue-Sat (cron 2-6). Jul -> PDT (UTC-7): one hour
    # earlier in UTC. This is "convert local->UTC, re-confirm across DST".
    cfg = parse_config(base_config())
    assert expand(cfg, now=datetime(2026, 1, 15, 9)).utc_crons == ["0 4,5,6,7 * * 2,3,4,5,6"]
    assert expand(cfg, now=datetime(2026, 7, 15, 9)).utc_crons == ["0 3,4,5,6 * * 2,3,4,5,6"]


def test_expand_local_to_utc_conversions():
    cases = [
        # (timezone, recurrence, (start, end), expected crons, note)
        (LA, "weekends", ("20:00", "00:00"), ["0 4,5,6,7 * * 0,1"], "day shift to Sun/Mon UTC"),
        (LA, "every-day", ("09:00", "12:00"), ["0 17,18,19 * * *"], "daytime, same UTC day"),
        ("UTC", "every-day", ("08:00", "12:00"), ["0 8,9,10,11 * * *"], "identity"),
        ("Asia/Kolkata", "every-day", ("09:00", "11:00"), ["30 3,4 * * *"], "+5:30 shifts minute"),
    ]
    for tz, recurrence, (start, end), expected, note in cases:
        cfg = parse_config(
            base_config(
                timezone=tz,
                recurrence=recurrence,
                window={"start_local": start, "end_local": end},
            )
        )
        assert expand(cfg, now=datetime(2026, 1, 15, 0)).utc_crons == expected, note


def test_expand_expiry_modes():
    cases = [
        ({"mode": "days", "value": 7}, "2026-01-22"),
        ({"mode": "weeks", "value": 2}, "2026-01-29"),
        ({"mode": "date", "value": "2026-10-01"}, "2026-10-01"),
        ({"mode": "none", "value": None}, None),
    ]
    for expiry, expected in cases:
        cfg = parse_config(base_config(expiry=expiry))
        assert expand(cfg, now=datetime(2026, 1, 15, 9)).expiry_date == expected, expiry


def test_one_shot_uses_run_once_at_not_cron():
    once = base_config(recurrence="once", expiry={"mode": "once", "value": None})
    r = expand(parse_config(once), now=datetime(2026, 1, 15, 9))
    # Next 20:00 local from 09:00 Jan 15 is same day; PST -> 04:00 UTC Jan 16.
    assert r.run_once_at == "2026-01-16T04:00:00Z"
    assert r.utc_crons == [] and r.expiry_date is None and r.dst_transitions == []

    # A one-shot on a non-active weekday picks the next active weekday's start.
    workday_once = base_config(recurrence="workday", expiry={"mode": "once", "value": None})
    r2 = expand(parse_config(workday_once), now=datetime(2026, 1, 17, 9))  # Sat
    assert r2.run_once_at == "2026-01-20T04:00:00Z"  # Mon Jan 19 20:00 PST


def test_dst_transitions_and_prompt_substitutions():
    cfg = parse_config(base_config())
    transitions = dst_transitions(cfg, date(2026, 1, 1), date(2026, 12, 31))
    assert "2026-03-08" in transitions and "2026-11-01" in transitions  # spring/fall
    assert expand(cfg, now=datetime(2026, 1, 15, 9)).window_end_local == "12:00 AM"


def test_custom_cron_converts_hour_to_utc():
    cfg = parse_config(base_config(recurrence="custom", custom_cron_local="30 9 * * 1"))
    # 09:30 PST -> 17:30 UTC; day fields preserved.
    assert expand(cfg, now=datetime(2026, 1, 15, 9)).utc_crons == ["30 17 * * 1"]
