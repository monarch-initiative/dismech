from scripts.apply_cron_profile import rewrite_schedule


def test_rewrite_schedule_replaces_existing_schedule_entries():
    original = """name: Demo

on:
  schedule:
    - cron: "0 0 30 2 *"  # old
  workflow_dispatch:
    inputs:
      note:
        type: string
"""

    updated = rewrite_schedule(
        original,
        [
            {"cron": "0 */4 * * 1-5", "comment": "weekday"},
            {"cron": "0 */8 * * 0,6", "comment": "weekend"},
        ],
        wf_name="demo",
    )

    assert '    - cron: "0 */4 * * 1-5"  # weekday' in updated
    assert '    - cron: "0 */8 * * 0,6"  # weekend' in updated
    assert "workflow_dispatch:" in updated
    assert "0 0 30 2 *" not in updated


def test_rewrite_schedule_removes_schedule_block_for_empty_entries():
    original = """name: Demo

on:
  schedule:
    - cron: "37 * * * *"  # hourly
  workflow_dispatch:
    inputs:
      note:
        type: string
"""

    updated = rewrite_schedule(original, [], wf_name="demo")

    assert "schedule:" not in updated
    assert "cron:" not in updated
    assert "workflow_dispatch:" in updated
    assert "inputs:" in updated


def test_rewrite_schedule_inserts_schedule_block_when_reenabling():
    original = """name: Demo

on:
  workflow_dispatch:
    inputs:
      note:
        type: string

jobs:
  test:
    runs-on: ubuntu-latest
"""

    updated = rewrite_schedule(
        original,
        [{"cron": "37 * * * *", "comment": "hourly"}],
        wf_name="demo",
    )

    assert (
        """on:
  schedule:
    - cron: "37 * * * *"  # hourly
  workflow_dispatch:
"""
        in updated
    )
    assert "jobs:" in updated
