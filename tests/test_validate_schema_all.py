"""Regression coverage for corpus validation exceeding ARG_MAX."""

import os
from types import SimpleNamespace

import pytest

from scripts import validate_schema_all as validator


def test_batches_bound_count_and_encoded_bytes():
    files = [f"folder/{i:05d} é space.yaml" for i in range(11000)]
    files += ["long/" + "é" * 2000 + f"{i}.yaml" for i in range(50)]
    batches = list(validator.batches(files))
    assert [path for batch in batches for path in batch] == files
    assert all(len(batch) <= 100 for batch in batches)
    assert all(sum(len(os.fsencode(p)) + 1 for p in b) <= 32768 for b in batches)


@pytest.mark.parametrize("kind", ["history", "disorders"])
def test_all_batches_run_after_validation_failure(tmp_path, monkeypatch, capsys, kind):
    for i in range(201):
        (tmp_path / f"{i:03d} space.yaml").touch()
    calls = []

    def run(command, **kwargs):
        calls.append(command)
        return SimpleNamespace(returncode=1 if len(calls) == 1 else 0)

    monkeypatch.setattr(validator.subprocess, "run", run)
    assert validator.main([kind, str(tmp_path), "schema.yaml"]) == 1
    assert [len(call[5:]) for call in calls] == [100, 100, 1]
    assert len({path for call in calls for path in call[5:]}) == 201
    assert "Validation batch 1 failed" in capsys.readouterr().err


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
