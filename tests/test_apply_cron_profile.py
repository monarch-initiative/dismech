import shutil
from pathlib import Path

import pytest
import yaml

import scripts.apply_cron_profile as cron_profile
from scripts.apply_cron_profile import rewrite_schedule

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / ".github" / "cron-profiles.yaml"
WORKFLOW_DIR = ROOT / ".github" / "workflows"
PROFILE_NAMES = tuple(cron_profile.load_config(CONFIG)["profiles"])


def workflow_crons(path: Path) -> list[str]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return [item["cron"] for item in data[True].get("schedule", [])]


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


@pytest.mark.parametrize("profile_name", PROFILE_NAMES)
def test_each_configured_profile_applies_to_workflows_in_isolation(
    profile_name: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    """Exercise the real applier, including removal under the `off` profile."""
    temp_root = tmp_path / "repo"
    temp_workflows = temp_root / ".github" / "workflows"
    temp_workflows.mkdir(parents=True)
    temp_config = temp_root / ".github" / "cron-profiles.yaml"
    shutil.copyfile(CONFIG, temp_config)

    config = cron_profile.load_config(CONFIG)
    managed = config["profiles"][profile_name]["workflows"]
    for stem in managed:
        candidates = [WORKFLOW_DIR / f"{stem}.yml", WORKFLOW_DIR / f"{stem}.yaml"]
        source = next(path for path in candidates if path.exists())
        shutil.copyfile(source, temp_workflows / source.name)

    monkeypatch.setattr(cron_profile, "REPO_ROOT", temp_root)
    monkeypatch.setattr(cron_profile, "WORKFLOW_DIR", temp_workflows)

    assert (
        cron_profile.main([profile_name, "--config", str(temp_config), "--no-commit"])
        == 0
    )

    applied_config = cron_profile.load_config(temp_config)
    assert applied_config["active"] == profile_name
    for stem, entries in managed.items():
        candidates = [
            temp_workflows / f"{stem}.yml",
            temp_workflows / f"{stem}.yaml",
        ]
        workflow_path = next(path for path in candidates if path.exists())
        assert workflow_crons(workflow_path) == [entry["cron"] for entry in entries]
