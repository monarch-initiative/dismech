"""``python -m dismech.schedule`` — expand a schedule config to its UTC cron.

Thin dispatcher so the skill can shell out deterministically without tripping
the ``-m package.module`` double-import warning.
"""

from __future__ import annotations

from dismech.schedule.config import _main

if __name__ == "__main__":
    raise SystemExit(_main())
