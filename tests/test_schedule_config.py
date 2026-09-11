"""Unit tests for the pure schedule-config parser/expander (issue #11657)."""

from __future__ import annotations

from datetime import datetime, time

import pytest

from dismech.schedule.config import (
    RECURRENCE_DOW,
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


# --------------------------------------------------------------------------- #
# Parsing / validation
# --------------------------------------------------------------------------- #


def test_parse_minimal_valid_config():
    cfg = parse_config(base_config())
    assert isinstance(cfg, ScheduleConfig)
    assert cfg.recurrence == "workday"
    assert cfg.window.start_local == time(20, 0)
    assert cfg.window.end_local == time(0, 0)
    assert cfg.max_active == 1
    assert cfg.routine.environment_id == "env_01Qs4qSVQcgqzrywAKajYQnj"


def test_load_config_from_repo_default(tmp_path):
    p = tmp_path / "schedule-config.yaml"
    p.write_text(
        "version: 1\n"
        "timezone: America/Los_Angeles\n"
        "window:\n  start_local: '20:00'\n  end_local: '00:00'\n"
        "recurrence: workday\n"
        "expiry:\n  mode: none\n  value: null\n"
        "max_active: 1\n"
        "model: claude-sonnet-5\n"
        "routine:\n  trigger_id: null\n  environment_id: env_x\n",
        encoding="utf-8",
    )
    cfg = load_config(p)
    assert cfg.model == "claude-sonnet-5"
    assert cfg.routine.environment_id == "env_x"


@pytest.mark.parametrize(
    "overrides,message",
    [
        ({"version": 2}, "version"),
        ({"timezone": "Mars/Olympus"}, "timezone"),
        ({"recurrence": "hourly"}, "recurrence"),
        ({"max_active": 0}, "max_active"),
        ({"max_active": 3}, "not supported"),
        ({"window": {"start_local": "20:30", "end_local": "00:00"}}, "whole number of hours"),
        ({"window": {"start_local": "20:00", "end_local": "20:00"}}, "empty"),
    ],
)
def test_parse_rejects_bad_values(overrides, message):
    with pytest.raises(ScheduleConfigError) as exc:
        parse_config(base_config(**overrides))
    assert message in str(exc.value)


def test_custom_recurrence_requires_cron():
    with pytest.raises(ScheduleConfigError, match="custom"):
        parse_config(base_config(recurrence="custom", custom_cron_local=None))
    cfg = parse_config(base_config(recurrence="custom", custom_cron_local="0 9 * * 1"))
    assert cfg.custom_cron_local == "0 9 * * 1"


def test_custom_cron_rejected_without_custom_recurrence():
    with pytest.raises(ScheduleConfigError, match="custom_cron_local is only valid"):
        parse_config(base_config(recurrence="workday", custom_cron_local="0 9 * * 1"))


@pytest.mark.parametrize(
    "expiry,message",
    [
        ({"mode": "days", "value": 0}, "positive integer"),
        ({"mode": "weeks", "value": "two"}, "positive integer"),
        ({"mode": "date", "value": "not-a-date"}, "valid date"),
        ({"mode": "none", "value": 7}, "must be empty"),
    ],
)
def test_parse_rejects_bad_expiry(expiry, message):
    with pytest.raises(ScheduleConfigError) as exc:
        parse_config(base_config(expiry=expiry))
    assert message in str(exc.value)


# --------------------------------------------------------------------------- #
# Window mechanics
# --------------------------------------------------------------------------- #


def test_window_fire_hours_midnight_end():
    w = Window(start_local=time(20, 0), end_local=time(0, 0))
    assert w.duration_hours == 4
    assert w.fire_hours() == [20, 21, 22, 23]


def test_window_fire_hours_crossing_midnight():
    w = Window(start_local=time(22, 0), end_local=time(2, 0))
    assert w.duration_hours == 4
    assert w.fire_hours() == [22, 23, 0, 1]


def test_recurrence_dow_vocabulary():
    assert RECURRENCE_DOW["every-day"] == "*"
    assert RECURRENCE_DOW["workday"] == "1-5"
    assert RECURRENCE_DOW["weekends"] == "0,6"


# --------------------------------------------------------------------------- #
# Local -> UTC expansion, DST
# --------------------------------------------------------------------------- #


def test_expand_workday_window_pst():
    # January -> PST (UTC-8). 20:00-23:00 PST is 04:00-07:00 UTC the next day,
    # so Mon-Fri local evenings become Tue-Sat (cron 2-6) UTC mornings.
    cfg = parse_config(base_config())
    result = expand(cfg, now=datetime(2026, 1, 15, 9, 0))
    assert result.utc_crons == ["0 4,5,6,7 * * 2,3,4,5,6"]
    assert result.run_once_at is None


def test_expand_workday_window_pdt():
    # July -> PDT (UTC-7). One hour earlier in UTC than PST.
    cfg = parse_config(base_config())
    result = expand(cfg, now=datetime(2026, 7, 15, 9, 0))
    assert result.utc_crons == ["0 3,4,5,6 * * 2,3,4,5,6"]


def test_expand_dst_makes_a_one_hour_difference():
    cfg = parse_config(base_config())
    pst = expand(cfg, now=datetime(2026, 1, 15, 9, 0)).utc_crons[0]
    pdt = expand(cfg, now=datetime(2026, 7, 15, 9, 0)).utc_crons[0]
    assert pst != pdt
    assert pst.split()[1] == "4,5,6,7"
    assert pdt.split()[1] == "3,4,5,6"


def test_expand_weekends_shifts_days_in_utc():
    # Sat/Sun evening Pacific lands on Sun/Mon UTC.
    cfg = parse_config(base_config(recurrence="weekends"))
    result = expand(cfg, now=datetime(2026, 1, 15, 9, 0))
    assert result.utc_crons == ["0 4,5,6,7 * * 0,1"]


def test_expand_every_day_daytime_window_same_utc_day():
    cfg = parse_config(
        base_config(
            recurrence="every-day",
            window={"start_local": "09:00", "end_local": "12:00"},
        )
    )
    result = expand(cfg, now=datetime(2026, 1, 15, 0, 0))
    assert result.utc_crons == ["0 17,18,19 * * *"]


def test_expand_utc_timezone_is_identity():
    cfg = parse_config(
        base_config(
            timezone="UTC",
            recurrence="every-day",
            window={"start_local": "08:00", "end_local": "12:00"},
        )
    )
    result = expand(cfg, now=datetime(2026, 1, 15, 0, 0))
    assert result.utc_crons == ["0 8,9,10,11 * * *"]
    assert result.dst_transitions == []


def test_expand_half_hour_offset_timezone():
    # India Standard Time is UTC+5:30 with no DST; the minute field must shift.
    cfg = parse_config(
        base_config(
            timezone="Asia/Kolkata",
            recurrence="every-day",
            window={"start_local": "09:00", "end_local": "11:00"},
            expiry={"mode": "none", "value": None},
        )
    )
    result = expand(cfg, now=datetime(2026, 1, 15, 0, 0))
    # 09:00 IST = 03:30 UTC, 10:00 IST = 04:30 UTC.
    assert result.utc_crons == ["30 3,4 * * *"]
    assert result.dst_transitions == []


# --------------------------------------------------------------------------- #
# Expiry and one-shot
# --------------------------------------------------------------------------- #


def test_expiry_days_computes_date():
    cfg = parse_config(base_config(expiry={"mode": "days", "value": 7}))
    result = expand(cfg, now=datetime(2026, 1, 15, 9, 0))
    assert result.expiry_date == "2026-01-22"


def test_expiry_weeks_computes_date():
    cfg = parse_config(base_config(expiry={"mode": "weeks", "value": 2}))
    result = expand(cfg, now=datetime(2026, 1, 15, 9, 0))
    assert result.expiry_date == "2026-01-29"


def test_expiry_explicit_date_passthrough():
    cfg = parse_config(base_config(expiry={"mode": "date", "value": "2026-10-01"}))
    result = expand(cfg, now=datetime(2026, 1, 15, 9, 0))
    assert result.expiry_date == "2026-10-01"


def test_expiry_none_is_null():
    cfg = parse_config(base_config(expiry={"mode": "none", "value": None}))
    result = expand(cfg, now=datetime(2026, 1, 15, 9, 0))
    assert result.expiry_date is None


def test_once_recurrence_uses_run_once_at():
    cfg = parse_config(base_config(recurrence="once", expiry={"mode": "once", "value": None}))
    result = expand(cfg, now=datetime(2026, 1, 15, 9, 0))
    # Next 20:00 local from 09:00 on Jan 15 is the same day; PST -> 04:00 UTC Jan 16.
    assert result.run_once_at == "2026-01-16T04:00:00Z"
    assert result.utc_crons == []
    assert result.expiry_date is None
    assert result.dst_transitions == []


def test_once_picks_next_active_weekday():
    # Sat Jan 17 2026 with workday recurrence + once expiry -> next start is Mon.
    cfg = parse_config(base_config(recurrence="workday", expiry={"mode": "once", "value": None}))
    result = expand(cfg, now=datetime(2026, 1, 17, 9, 0))
    assert result.run_once_at == "2026-01-20T04:00:00Z"  # Mon Jan 19 20:00 PST


# --------------------------------------------------------------------------- #
# DST transition reporting
# --------------------------------------------------------------------------- #


def test_dst_transitions_found_across_spring_and_fall():
    from datetime import date

    cfg = parse_config(base_config())
    transitions = dst_transitions(cfg, date(2026, 1, 1), date(2026, 12, 31))
    assert "2026-03-08" in transitions  # spring forward
    assert "2026-11-01" in transitions  # fall back


def test_window_end_local_rendered_for_prompt():
    cfg = parse_config(base_config())
    result = expand(cfg, now=datetime(2026, 1, 15, 9, 0))
    assert result.window_end_local == "12:00 AM"


# --------------------------------------------------------------------------- #
# Custom cron
# --------------------------------------------------------------------------- #


def test_custom_cron_converts_hour_to_utc():
    cfg = parse_config(base_config(recurrence="custom", custom_cron_local="30 9 * * 1"))
    result = expand(cfg, now=datetime(2026, 1, 15, 9, 0))
    # 09:30 PST -> 17:30 UTC; day fields preserved.
    assert result.utc_crons == ["30 17 * * 1"]
