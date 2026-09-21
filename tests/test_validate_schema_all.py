"""Regression coverage for corpus validation exceeding ARG_MAX."""

import os
from types import SimpleNamespace

import pytest

from scripts import validate_schema_all as validator


def test_batches_bound_encoded_bytes():
    files = [f"folder/{i:05d} é space.yaml" for i in range(11000)]
    files += ["long/" + "é" * 2000 + f"{i}.yaml" for i in range(50)]
    batches = list(validator.batches(files))
    assert [path for batch in batches for path in batch] == files
    # Each batch fills the byte budget, avoiding needless validator startups.
    for batch, following in zip(batches, batches[1:]):
        assert sum(len(os.fsencode(p)) + 1 for p in [*batch, following[0]]) > 32768
    assert all(sum(len(os.fsencode(p)) + 1 for p in b) <= 32768 for b in batches)


@pytest.mark.parametrize("kind", ["history", "disorders"])
def test_all_batches_run_after_validation_failure(tmp_path, monkeypatch, capsys, kind):
    for i in range(201):
        (tmp_path / f"{i:03d} space.yaml").touch()
    path_bytes = len(os.fsencode(tmp_path / "000 space.yaml")) + 1
    monkeypatch.setattr(validator, "MAX_PATH_BYTES", 100 * path_bytes)
    calls = []

    def run(command, **kwargs):
        calls.append(command)
        return SimpleNamespace(returncode=1 if len(calls) == 1 else 0)

    monkeypatch.setattr(validator.subprocess, "run", run)
    assert validator.main([kind, str(tmp_path), "schema.yaml"]) == 1
    assert all(
        call[:5]
        == [
            "linkml-validate",
            "--schema",
            "schema.yaml",
            "--target-class",
            "HistoryRecord" if kind == "history" else "Disease",
        ]
        for call in calls
    )
    assert [len(call[5:]) for call in calls] == [100, 100, 1]
    assert len({path for call in calls for path in call[5:]}) == 201
    errors = capsys.readouterr().err
    assert "Validation batch 1 failed" in errors
    assert "100 files" in errors
    assert str(tmp_path / "000 space.yaml") in errors
    assert str(tmp_path / "099 space.yaml") in errors
    assert len(errors.splitlines()) == 1


def test_enumeration_and_exclusion(tmp_path):
    nested = tmp_path / "nested"
    nested.mkdir()
    for name in ["a.yaml", "b.history.yaml", "ignore.txt"]:
        (nested / name).touch()
    assert validator.enumerate_files(tmp_path, False) == [str(nested / "a.yaml")]
    assert len(validator.enumerate_files(tmp_path, True)) == 2


def test_walk_failure_is_distinct_and_never_validates(tmp_path, monkeypatch, capsys):
    def walk(root, onerror):
        onerror(PermissionError("unreadable subtree"))

    monkeypatch.setattr(validator.os, "walk", walk)
    assert validator.main(["history", str(tmp_path), "schema.yaml"]) == 2
    assert "Cannot enumerate history YAML files" in capsys.readouterr().err


def test_missing_and_empty_inputs(tmp_path, capsys):
    assert validator.main(["history", str(tmp_path / "missing"), "schema"]) == 0
    assert "No history directory found." in capsys.readouterr().out
    assert validator.main(["history", str(tmp_path), "schema"]) == 0
    assert "No history YAML files found" in capsys.readouterr().out
    assert validator.main(["disorders", str(tmp_path), "schema"]) == 1
    assert validator.main(["disorders", str(tmp_path / "missing"), "schema"]) == 2


def test_success_and_launch_error(tmp_path, monkeypatch, capsys):
    (tmp_path / "record.yaml").touch()
    monkeypatch.setattr(
        validator.subprocess, "run", lambda *a, **kw: SimpleNamespace(returncode=0)
    )
    assert validator.main(["history", str(tmp_path), "schema"]) == 0

    def cannot_launch(*args, **kwargs):
        raise OSError("argument list too long")

    monkeypatch.setattr(validator.subprocess, "run", cannot_launch)
    assert validator.main(["history", str(tmp_path), "schema"]) == 2
    assert "Cannot launch validation batch 1" in capsys.readouterr().err
