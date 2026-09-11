"""Parse and expand the ``/schedule`` donation-window configuration.

The user describes a donation window in *local* terms — "8pm-12am every
workday, for two weeks". The Claude Code cloud-routine API
(``RemoteTrigger``) speaks only in **UTC cron instants** and has no notion of a
window or an expiry. This module is the pure translation layer between the two,
and it is deliberately free of any network or cloud-API call so the whole of it
is unit-testable.

Three facts about the ``RemoteTrigger`` API shape everything here (see issue
#11657):

1. **Cloud cron is UTC.** ``8pm America/Los_Angeles`` is ``0 3 * * *`` in PDT
   but ``0 4 * * *`` in PST, so the local->UTC conversion is DST-dependent and a
   registered cron is only valid for one DST period. :func:`expand` computes the
   cron for a reference instant and :func:`dst_transitions` reports when the
   offset changes inside the routine's lifetime so the caller can re-register.
2. **The scheduler cannot enforce a window.** A cron fires at an instant; there
   is no "stop at midnight". A window is therefore registered as *hourly fires
   across the window* (8/9/10/11pm), coordinated by the skill's single-flight
   guard, and the prompt is told the local window-end so it stops claiming new
   work past it.
3. **The minimum interval is one hour**, so a window is always a whole number of
   hourly fires and non-hour-aligned windows are rejected.

The public surface is :func:`load_config` / :func:`parse_config` (validate the
YAML into a :class:`ScheduleConfig`) and :func:`expand` (turn a config into the
UTC cron list, ``run_once_at``, and the prompt substitutions).
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass, field
from datetime import date, datetime, time, timedelta
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

import yaml

# --------------------------------------------------------------------------- #
# Vocabulary
# --------------------------------------------------------------------------- #

#: Recurrence aliases -> the *local* cron day-of-week field they expand to.
#: ``once`` and ``custom`` are handled separately (``run_once_at`` and a
#: user-supplied local cron respectively) and are intentionally absent here.
RECURRENCE_DOW: dict[str, str] = {
    "every-day": "*",
    "workday": "1-5",
    "weekends": "0,6",
}

VALID_RECURRENCES = frozenset({*RECURRENCE_DOW, "once", "custom"})
VALID_EXPIRY_MODES = frozenset({"none", "days", "weeks", "date", "once"})

#: Map Python ``weekday()`` (Mon=0..Sun=6) to cron day-of-week (Sun=0..Sat=6).
_CRON_DOW_FROM_PY = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 0}


class ScheduleConfigError(ValueError):
    """Raised when the schedule configuration is malformed or unsupported."""


# --------------------------------------------------------------------------- #
# Config model
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class Window:
    """A local donation window ``[start_local, end_local)``.

    ``end_local`` of ``"00:00"`` means local midnight *at the end of the day*
    (i.e. 24:00), not the start — that is the flagship ``20:00``-``00:00`` case.
    A window may cross local midnight (``22:00``-``02:00``); it must be a whole
    number of hours long because the cloud minimum interval is one hour.
    """

    start_local: time
    end_local: time

    @property
    def start_hour(self) -> int:
        return self.start_local.hour

    @property
    def start_minute(self) -> int:
        return self.start_local.minute

    def fire_hours(self) -> list[int]:
        """Local hours (0-23) the routine fires at, in window order.

        ``20:00``-``00:00`` -> ``[20, 21, 22, 23]``;
        ``22:00``-``02:00`` -> ``[22, 23, 0, 1]``.
        """
        return [(self.start_hour + i) % 24 for i in range(self.duration_hours)]

    @property
    def duration_hours(self) -> int:
        start = self.start_local.hour * 60 + self.start_local.minute
        end = self.end_local.hour * 60 + self.end_local.minute
        if self.end_local == time(0, 0):
            end = 24 * 60
        if end == start:
            raise ScheduleConfigError("window is empty (start equals end)")
        if end < start:
            end += 24 * 60  # crosses local midnight
        span = end - start
        if span % 60 != 0:
            raise ScheduleConfigError(
                "window must be a whole number of hours (cloud minimum interval "
                f"is one hour); got {span} minutes"
            )
        if span > 24 * 60:
            raise ScheduleConfigError("window longer than 24 hours is not supported")
        return span // 60


@dataclass(frozen=True)
class Expiry:
    """When the routine should self-disable. ``mode == 'none'`` never expires."""

    mode: str = "none"
    value: Any = None


@dataclass(frozen=True)
class Routine:
    trigger_id: str | None = None
    environment_id: str | None = None


@dataclass(frozen=True)
class ScheduleConfig:
    version: int
    timezone: str
    window: Window
    recurrence: str
    custom_cron_local: str | None = None
    expiry: Expiry = field(default_factory=Expiry)
    max_active: int = 1
    model: str = "claude-sonnet-5"
    routine: Routine = field(default_factory=Routine)

    @property
    def tzinfo(self) -> ZoneInfo:
        try:
            return ZoneInfo(self.timezone)
        except ZoneInfoNotFoundError as exc:  # pragma: no cover - env dependent
            raise ScheduleConfigError(f"unknown timezone {self.timezone!r}") from exc


# --------------------------------------------------------------------------- #
# Parsing / validation
# --------------------------------------------------------------------------- #


def _parse_hhmm(value: Any, field_name: str) -> time:
    if not isinstance(value, str) or ":" not in value:
        raise ScheduleConfigError(f"{field_name} must be a 'HH:MM' string, got {value!r}")
    try:
        hh, mm = (int(part) for part in value.split(":", 1))
    except ValueError as exc:
        raise ScheduleConfigError(f"{field_name} is not a valid time: {value!r}") from exc
    if not (0 <= hh <= 24 and 0 <= mm < 60) or (hh == 24 and mm != 0):
        raise ScheduleConfigError(f"{field_name} out of range: {value!r}")
    return time(hh % 24, mm)


def parse_config(data: dict[str, Any]) -> ScheduleConfig:
    """Validate a parsed-YAML mapping into a :class:`ScheduleConfig`.

    Raises :class:`ScheduleConfigError` with an actionable message on any
    unsupported or malformed field rather than letting a bad value reach the
    cloud-API call.
    """
    if not isinstance(data, dict):
        raise ScheduleConfigError("schedule config must be a mapping")

    version = data.get("version")
    if version != 1:
        raise ScheduleConfigError(f"unsupported config version {version!r} (expected 1)")

    timezone = data.get("timezone")
    if not isinstance(timezone, str) or not timezone:
        raise ScheduleConfigError("timezone is required (e.g. 'America/Los_Angeles')")
    try:
        ZoneInfo(timezone)
    except ZoneInfoNotFoundError as exc:
        raise ScheduleConfigError(f"unknown timezone {timezone!r}") from exc

    win = data.get("window") or {}
    if not isinstance(win, dict):
        raise ScheduleConfigError("window must be a mapping with start_local/end_local")
    window = Window(
        start_local=_parse_hhmm(win.get("start_local"), "window.start_local"),
        end_local=_parse_hhmm(win.get("end_local"), "window.end_local"),
    )
    window.duration_hours  # validate hour alignment eagerly

    recurrence = data.get("recurrence")
    if recurrence not in VALID_RECURRENCES:
        raise ScheduleConfigError(
            f"recurrence must be one of {sorted(VALID_RECURRENCES)}, got {recurrence!r}"
        )

    custom_cron_local = data.get("custom_cron_local")
    if recurrence == "custom":
        if not isinstance(custom_cron_local, str) or len(custom_cron_local.split()) != 5:
            raise ScheduleConfigError(
                "recurrence: custom requires a 5-field custom_cron_local string"
            )
    elif custom_cron_local not in (None, ""):
        raise ScheduleConfigError(
            "custom_cron_local is only valid with recurrence: custom"
        )

    expiry = _parse_expiry(data.get("expiry") or {})

    max_active = data.get("max_active", 1)
    if not isinstance(max_active, int) or max_active < 1:
        raise ScheduleConfigError("max_active must be a positive integer")
    if max_active != 1:
        # This version is deliberately single-concurrency; a larger value would
        # need the per-disease lease and top-up counting that are out of scope.
        raise ScheduleConfigError(
            "max_active > 1 is not supported in this version (active concurrency is 1)"
        )

    model = data.get("model", "claude-sonnet-5")
    if not isinstance(model, str) or not model:
        raise ScheduleConfigError("model must be a non-empty string")

    routine_data = data.get("routine") or {}
    if not isinstance(routine_data, dict):
        raise ScheduleConfigError("routine must be a mapping")
    routine = Routine(
        trigger_id=routine_data.get("trigger_id"),
        environment_id=routine_data.get("environment_id"),
    )

    return ScheduleConfig(
        version=version,
        timezone=timezone,
        window=window,
        recurrence=recurrence,
        custom_cron_local=custom_cron_local or None,
        expiry=expiry,
        max_active=max_active,
        model=model,
        routine=routine,
    )


def _parse_expiry(data: dict[str, Any]) -> Expiry:
    if not isinstance(data, dict):
        raise ScheduleConfigError("expiry must be a mapping")
    mode = data.get("mode", "none")
    if mode not in VALID_EXPIRY_MODES:
        raise ScheduleConfigError(
            f"expiry.mode must be one of {sorted(VALID_EXPIRY_MODES)}, got {mode!r}"
        )
    value = data.get("value")
    if mode in ("days", "weeks"):
        if not isinstance(value, int) or value < 1:
            raise ScheduleConfigError(f"expiry.value for mode {mode} must be a positive integer")
    elif mode == "date":
        if not isinstance(value, (str, date)):
            raise ScheduleConfigError("expiry.value for mode date must be an ISO 'YYYY-MM-DD' string")
        try:
            _coerce_date(value)
        except ValueError as exc:
            raise ScheduleConfigError(f"expiry.value is not a valid date: {value!r}") from exc
    elif mode in ("none", "once") and value not in (None, ""):
        raise ScheduleConfigError(f"expiry.value must be empty for mode {mode}")
    return Expiry(mode=mode, value=value if value != "" else None)


def _coerce_date(value: str | date) -> date:
    if isinstance(value, date):
        return value
    return date.fromisoformat(value)


def load_config(path: str | Path) -> ScheduleConfig:
    """Load and validate ``.claude/schedule-config.yaml`` (or any path)."""
    text = Path(path).read_text(encoding="utf-8")
    data = yaml.safe_load(text)
    return parse_config(data)


# --------------------------------------------------------------------------- #
# Expansion (local window -> UTC cron + prompt substitutions)
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class ExpansionResult:
    """The registration payload derived from a :class:`ScheduleConfig`.

    ``utc_crons`` is empty for a one-shot schedule; ``run_once_at`` is set only
    for a one-shot. Exactly one of the two is populated.
    """

    timezone: str
    reference_date: str
    utc_crons: list[str]
    run_once_at: str | None
    window_end_local: str
    expiry_date: str | None
    dst_transitions: list[str]
    model: str
    environment_id: str | None

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2, sort_keys=True)


def utc_offset_hours(tz: ZoneInfo, moment: datetime) -> float:
    """UTC offset (hours) in effect at ``moment`` (naive local) for ``tz``."""
    aware = moment.replace(tzinfo=tz)
    offset = aware.utcoffset()
    assert offset is not None
    return offset.total_seconds() / 3600.0


def _local_fire_datetimes(config: ScheduleConfig, ref: date) -> list[datetime]:
    """Naive local datetimes for every fire on the active weekdays of one week.

    The week is anchored on the Monday of ``ref``'s week. For ``once`` /
    ``custom`` recurrences this is not used (see :func:`expand`).
    """
    dow_field = RECURRENCE_DOW[config.recurrence]
    if dow_field == "*":
        active_py_dows = set(range(7))  # 0=Mon..6=Sun
    elif dow_field == "1-5":
        active_py_dows = {0, 1, 2, 3, 4}
    else:  # "0,6" -> Sun, Sat in cron == py Sun(6), Sat(5)
        active_py_dows = {5, 6}

    monday = ref - timedelta(days=ref.weekday())
    fires: list[datetime] = []
    for offset in range(7):
        day = monday + timedelta(days=offset)
        if day.weekday() not in active_py_dows:
            continue
        for hour in config.window.fire_hours():
            # A window crossing local midnight rolls later hours onto the next
            # day; keep them attached to the window's start day so the UTC-side
            # weekday shift is computed from the true local instant.
            wrap_days = 0
            if hour < config.window.start_hour:
                wrap_days = 1
            fire_day = day + timedelta(days=wrap_days)
            fires.append(
                datetime(
                    fire_day.year,
                    fire_day.month,
                    fire_day.day,
                    hour,
                    config.window.start_minute,
                    tzinfo=None,
                )
            )
    return fires


def _utc_crons(config: ScheduleConfig, ref: date) -> list[str]:
    """Build the UTC cron list for a recurring schedule at reference ``ref``.

    One cron per distinct ``(minute, hour, day-of-week set)`` group, which is
    always unambiguous even when the local->UTC conversion shifts the weekday or
    splits a midnight-crossing window across two UTC days.
    """
    tz = config.tzinfo
    # group: (utc_minute, utc_hour) -> set of cron day-of-week ints
    groups: dict[tuple[int, int], set[int]] = {}
    for local_dt in _local_fire_datetimes(config, ref):
        aware = local_dt.replace(tzinfo=tz)
        utc = aware.astimezone(ZoneInfo("UTC"))
        cron_dow = _CRON_DOW_FROM_PY[utc.weekday()]
        groups.setdefault((utc.minute, utc.hour), set()).add(cron_dow)

    crons: list[str] = []
    # Merge hours that share an identical day-of-week set and minute into a
    # single cron with an hour list, so a plain 8-11pm workday window collapses
    # to one line.
    by_dowset: dict[tuple[int, frozenset[int]], list[int]] = {}
    for (minute, hour), dows in groups.items():
        by_dowset.setdefault((minute, frozenset(dows)), []).append(hour)
    for (minute, dows), hours in by_dowset.items():
        hour_field = ",".join(str(h) for h in sorted(hours))
        dow_field = _format_dow(dows)
        crons.append(f"{minute} {hour_field} * * {dow_field}")
    return sorted(crons, key=_cron_sort_key)


def _format_dow(dows: frozenset[int]) -> str:
    if dows == frozenset(range(7)):
        return "*"
    return ",".join(str(d) for d in sorted(dows))


def _cron_sort_key(cron: str) -> tuple:
    minute, hours, _dom, _mon, dow = cron.split()
    first_hour = int(hours.split(",")[0])
    return (dow, first_hour, int(minute))


def _next_local_start(config: ScheduleConfig, now_local: datetime) -> datetime:
    """The next local window-start instant at or after ``now_local``.

    Respects the recurrence's active weekdays (and, for ``custom``, is not
    used — one-shot ``custom`` is disallowed).
    """
    start = time(config.window.start_hour, config.window.start_minute)
    dow_field = RECURRENCE_DOW.get(config.recurrence, "*")
    if dow_field == "1-5":
        active = {0, 1, 2, 3, 4}
    elif dow_field == "0,6":
        active = {5, 6}
    else:
        active = set(range(7))
    for add in range(8):
        day = (now_local + timedelta(days=add)).date()
        if day.weekday() not in active:
            continue
        candidate = datetime.combine(day, start)
        if candidate >= now_local.replace(tzinfo=None):
            return candidate
    raise ScheduleConfigError("could not find a next start instant")  # pragma: no cover


def _rfc3339_utc(local_dt: datetime, tz: ZoneInfo) -> str:
    aware = local_dt.replace(tzinfo=tz)
    utc = aware.astimezone(ZoneInfo("UTC"))
    return utc.strftime("%Y-%m-%dT%H:%M:%SZ")


def _expiry_date(config: ScheduleConfig, ref: date) -> str | None:
    exp = config.expiry
    if exp.mode == "none":
        return None
    if exp.mode == "days":
        return (ref + timedelta(days=int(exp.value))).isoformat()
    if exp.mode == "weeks":
        return (ref + timedelta(weeks=int(exp.value))).isoformat()
    if exp.mode == "date":
        return _coerce_date(exp.value).isoformat()
    # mode == "once": expires by firing; no standing expiry date.
    return None


def _format_local_time(t: time) -> str:
    """Human-friendly local time for the prompt, e.g. '12:00 AM'."""
    return t.strftime("%-I:%M %p")


def dst_transitions(config: ScheduleConfig, start: date, end: date) -> list[str]:
    """ISO dates within ``[start, end]`` where the local UTC offset changes.

    A registered UTC cron is only correct for one offset, so each returned date
    marks a day the routine must be re-registered (the skill re-confirms the
    conversion on each fire and updates the cron when this list is non-empty).
    """
    tz = config.tzinfo
    transitions: list[str] = []
    probe = time(config.window.start_hour, config.window.start_minute)
    prev = utc_offset_hours(tz, datetime.combine(start, probe))
    day = start
    while day <= end:
        cur = utc_offset_hours(tz, datetime.combine(day, probe))
        if cur != prev:
            transitions.append(day.isoformat())
            prev = cur
        day += timedelta(days=1)
    return transitions


def expand(config: ScheduleConfig, *, now: datetime | None = None) -> ExpansionResult:
    """Expand a validated config into the cloud-routine registration payload.

    ``now`` (an aware or naive local datetime; defaults to the current instant
    in the config's timezone) fixes the reference date the DST-dependent UTC
    conversion is computed against.
    """
    tz = config.tzinfo
    if now is None:
        now_local = datetime.now(tz).replace(tzinfo=None)
    elif now.tzinfo is not None:
        now_local = now.astimezone(tz).replace(tzinfo=None)
    else:
        now_local = now
    ref = now_local.date()

    one_shot = config.recurrence == "once" or config.expiry.mode == "once"

    utc_crons: list[str] = []
    run_once_at: str | None = None
    if one_shot:
        start_local = _next_local_start(config, now_local)
        run_once_at = _rfc3339_utc(start_local, tz)
    elif config.recurrence == "custom":
        # A local 5-field cron: convert only the hour/minute against the
        # reference offset, leaving the day fields as authored. Weekday-shift
        # across the offset is the operator's call for a hand-written cron.
        utc_crons = [_convert_custom_cron(config, ref)]
    else:
        utc_crons = _utc_crons(config, ref)

    # DST transitions across the routine's life (bounded by expiry, else a year).
    expiry_date = _expiry_date(config, ref)
    horizon = _coerce_date(expiry_date) if expiry_date else ref + timedelta(days=365)
    transitions = [] if one_shot else dst_transitions(config, ref, horizon)

    return ExpansionResult(
        timezone=config.timezone,
        reference_date=ref.isoformat(),
        utc_crons=utc_crons,
        run_once_at=run_once_at,
        window_end_local=_format_local_time(config.window.end_local),
        expiry_date=expiry_date,
        dst_transitions=transitions,
        model=config.model,
        environment_id=config.routine.environment_id,
    )


def _convert_custom_cron(config: ScheduleConfig, ref: date) -> str:
    minute_f, hour_f, dom_f, mon_f, dow_f = config.custom_cron_local.split()
    if minute_f in ("*",) or hour_f in ("*",) or "," in hour_f or "/" in hour_f or "-" in hour_f:
        raise ScheduleConfigError(
            "custom_cron_local hour/minute must be single values for UTC conversion"
        )
    tz = config.tzinfo
    local_dt = datetime.combine(ref, time(int(hour_f), int(minute_f)))
    utc = local_dt.replace(tzinfo=tz).astimezone(ZoneInfo("UTC"))
    return f"{utc.minute} {utc.hour} {dom_f} {mon_f} {dow_f}"


# --------------------------------------------------------------------------- #
# CLI (used by the skill to expand a config deterministically)
# --------------------------------------------------------------------------- #


def _main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Expand a dismech schedule config to UTC cron.")
    parser.add_argument("--config", required=True, help="path to schedule-config.yaml")
    parser.add_argument("--now", help="reference local datetime (ISO 8601), for testing")
    args = parser.parse_args(argv)

    try:
        config = load_config(args.config)
        now = datetime.fromisoformat(args.now) if args.now else None
        result = expand(config, now=now)
    except ScheduleConfigError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(result.to_json())
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(_main())
