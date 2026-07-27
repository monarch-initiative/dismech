#!/usr/bin/env python3
"""Print an agent run's final report from a claude-code-action execution log.

claude-code-action writes ``execution_file`` as a JSON array of stream events.
The agent's closing message is the ``result`` field of the last event whose
``type`` is ``result``; an errored run carries ``errors`` instead. This exists
because the action has no ``result`` output — workflows that wrote
``${{ steps.<id>.outputs.result }}`` were emitting an empty string.

Kept dependency-free and side-effect free so it can be unit tested directly.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def extract_result(events: list) -> str:
    """Return the agent's closing report, or an explanation of its absence."""
    results = [e for e in events if isinstance(e, dict) and e.get("type") == "result"]
    if not results:
        return (
            "No result event in the execution log — the agent did not complete. "
            "A Claude usage limit presents this way; check the run log for a "
            "quota message."
        )

    last = results[-1]
    report = str(last.get("result") or "").strip()
    errors = [str(e) for e in (last.get("errors") or [])]

    parts = []
    if report:
        parts.append(report)
    if errors:
        parts.append("ERRORS: " + "; ".join(errors))
    if not parts:
        parts.append(
            f"The agent produced no closing report (subtype={last.get('subtype')!r}, "
            f"is_error={last.get('is_error')!r})."
        )

    stats = (
        f"[turns={last.get('num_turns')} cost=${last.get('total_cost_usd')} "
        f"subtype={last.get('subtype')}]"
    )
    parts.append(stats)
    return "\n\n".join(parts)


def main(argv: list[str]) -> int:
    path = Path(argv[1])
    events = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(events, list):
        events = [events]
    print(extract_result(events))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
