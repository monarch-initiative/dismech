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
        # custom cron field validation happens at load time, not in expand()
        ({"recurrence": "custom", "custom_cron_local": "0,30 9 * * 1"}, "minute must be"),
        ({"recurrence": "custom", "custom_cron_local": "0 9 * * 9"}, "day-of-week"),
        # custom + once is incoherent (custom has no window to bound the run)
        (
            {"recurrence": "custom", "custom_cron_local": "0 9 * * 1",
             "expiry": {"mode": "once", "value": None}},
            "cannot be combined",
        ),
        ({"github_login": 5}, "github_login"),
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


def test_once_fires_the_window_hourly_then_self_disables():
    # "once"/tonight is NOT a single fire: it registers the same hourly heartbeat
    # crons as a recurring window, bounded by an expiry on the window's own date
    # so it self-disables the next day.
    once = base_config(recurrence="once", expiry={"mode": "none", "value": None})
    r = expand(parse_config(once), now=datetime(2026, 1, 15, 9))  # Thu 9am
    assert r.utc_crons == ["0 4,5,6,7 * * *"]  # every-day hourly (PST)
    assert r.self_disabling is True
    assert r.expiry_date == "2026-01-15"  # tonight's window date -> self-disable tomorrow

    # `expiry.mode: once` on a weekday recurrence keeps the weekday cron and
    # bounds it to the next active window date.
    workday_once = base_config(recurrence="workday", expiry={"mode": "once", "value": None})
    r2 = expand(parse_config(workday_once), now=datetime(2026, 1, 17, 9))  # Sat
    assert r2.utc_crons == ["0 4,5,6,7 * * 2,3,4,5,6"]
    assert r2.self_disabling is True
    assert r2.expiry_date == "2026-01-19"  # next workday (Mon)


def test_dst_transitions_and_prompt_substitutions():
    cfg = parse_config(base_config())
    transitions = dst_transitions(cfg, date(2026, 1, 1), date(2026, 12, 31))
    assert "2026-03-08" in transitions and "2026-11-01" in transitions  # spring/fall
    assert expand(cfg, now=datetime(2026, 1, 15, 9)).window_end_local == "12:00 AM"


def test_custom_cron_converts_hour_to_utc():
    cfg = parse_config(base_config(recurrence="custom", custom_cron_local="30 9 * * 1"))
    # 09:30 PST -> 17:30 UTC, same UTC day so Monday (dow 1) is preserved.
    assert expand(cfg, now=datetime(2026, 1, 15, 9)).utc_crons == ["30 17 * * 1"]


def test_custom_cron_shifts_day_of_week_across_utc_rollover():
    # Mon 8pm Pacific -> Tue 04:00 UTC (PST), so the dow must shift Mon(1)->Tue(2),
    # not stay Mon (which would fire Sunday 8pm Pacific). Ranges shift too.
    cfg = parse_config(base_config(recurrence="custom", custom_cron_local="0 20 * * 1"))
    assert expand(cfg, now=datetime(2026, 1, 15, 9)).utc_crons == ["0 4 * * 2"]
    cfg2 = parse_config(base_config(recurrence="custom", custom_cron_local="0 20 * * 5-6"))
    # Fri,Sat 8pm PT -> Sat,Sun 04:00 UTC -> dow {6,0} rendered sorted "0,6".
    assert expand(cfg2, now=datetime(2026, 1, 15, 9)).utc_crons == ["0 4 * * 0,6"]


def test_past_date_expiry_is_rejected():
    cfg = parse_config(base_config(expiry={"mode": "date", "value": "2020-01-01"}))
    with pytest.raises(ScheduleConfigError, match="in the past"):
        expand(cfg, now=datetime(2026, 1, 15, 9))


def test_dst_transitions_probe_avoids_the_spring_forward_gap():
    # A window starting inside the spring-forward gap must still report the true
    # transition date (2027-03-14), not a day late.
    cfg = parse_config(
        base_config(recurrence="every-day", window={"start_local": "02:00", "end_local": "06:00"})
    )
    transitions = dst_transitions(cfg, date(2027, 1, 1), date(2027, 12, 31))
    assert "2027-03-14" in transitions and "2027-03-15" not in transitions


def test_github_login_parses():
    assert parse_config(base_config(github_login="alice")).github_login == "alice"
    assert parse_config(base_config()).github_login is None
