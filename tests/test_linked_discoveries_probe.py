"""Argument parsing for scripts/linked_discoveries_probe.py (no network)."""

import importlib.util
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "linked_discoveries_probe.py"


@pytest.fixture
def probe(monkeypatch):
    spec = importlib.util.spec_from_file_location("linked_discoveries_probe", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    seen = {}

    def capture(args):
        seen["args"] = args
        return 0

    monkeypatch.setattr(module, "cmd_neighborhood", capture)
    monkeypatch.setattr(module, "cmd_seed_status", capture)
    return module, seen


@pytest.mark.parametrize(
    "argv",
    [
        ["--format", "json", "--pause", "0", "neighborhood", "20301443"],
        ["neighborhood", "20301443", "--format", "json", "--pause", "0"],
    ],
)
def test_common_flags_accepted_before_or_after_subcommand(probe, argv):
    module, seen = probe
    assert module.main(argv) == 0
    assert seen["args"].format == "json"
    assert seen["args"].pause == 0.0


def test_defaults_apply_when_flags_omitted(probe):
    module, seen = probe
    assert module.main(["seed-status", "9500320"]) == 0
    assert seen["args"].format == "tsv"
    assert seen["args"].pause == 0.5


def test_report_reproduction_command_parses(probe):
    module, seen = probe
    argv = [
        "neighborhood",
        "20301443",
        "--neighbors",
        "200",
        "--cui",
        "C0031269",
        "--mark-kb",
        "--format",
        "tsv",
    ]
    assert module.main(argv) == 0
    assert seen["args"].cui == ["C0031269"]
    assert seen["args"].mark_kb is True
