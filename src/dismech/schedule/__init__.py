"""Scheduling support for the ``/schedule`` curation-donation skill.

This package holds the two *pure*, unit-tested pieces the skill leans on so the
cloud-routine orchestration stays a thin shell over deterministic logic:

- :mod:`dismech.schedule.config` parses ``.claude/schedule-config.yaml`` and
  expands a local window/recurrence/expiry into the UTC cron(s) and prompt
  substitutions the ``RemoteTrigger`` cloud-routine API needs.
- :mod:`dismech.schedule.reconcile` classifies the current user's open PRs and
  un-PR'd claim issues into the finish-first / claim-one decision that governs
  every fire.

Neither module touches the network or the cloud API; both are exercised by
``tests/test_schedule_config.py`` and ``tests/test_schedule_reconcile.py``.
"""

from dismech.schedule.config import (
    ExpansionResult,
    ScheduleConfig,
    ScheduleConfigError,
    expand,
    load_config,
    parse_config,
)
from dismech.schedule.reconcile import (
    PRClassification,
    Reconciliation,
    classify_checks,
    classify_pr,
    reconcile,
    unclaimed_claim_issues,
)

__all__ = [
    "ExpansionResult",
    "PRClassification",
    "Reconciliation",
    "ScheduleConfig",
    "ScheduleConfigError",
    "classify_checks",
    "classify_pr",
    "expand",
    "load_config",
    "parse_config",
    "reconcile",
    "unclaimed_claim_issues",
]
