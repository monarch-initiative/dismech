"""The persistent cache behind `build_coverage_index()` (#15116).

`next`, `check` and `coverage` are one-shot processes that used to parse every
KB entry on every call, about half a minute. The cache keeps each file's
derived ids and labels between runs, keyed on content, so these tests pin the
contract: an unchanged tree parses nothing, an edit re-parses exactly the
edited file, a deleted file drops out, a version bump rebuilds, and
`DISMECH_KB_CACHE=0` turns the cache off.
"""

from __future__ import annotations

import json
import os
import time
from pathlib import Path

import pytest

from dismech.stubs import model
from dismech.stubs.model import build_coverage_index

_HOUR_NS = 3600 * 1_000_000_000


def _disorder(mondo_id: str, name: str) -> str:
    return (
        f"name: {name}\n"
        "disease_term:\n"
        f"  preferred_term: {name}\n"
        "  term:\n"
        f"    id: {mondo_id}\n"
        f"    label: {name}\n"
    )


@pytest.fixture
def kb(tmp_path):
    disorders = tmp_path / "kb" / "disorders"
    groupings = tmp_path / "kb" / "groupings"
    disorders.mkdir(parents=True)
    groupings.mkdir(parents=True)
    (disorders / "Alpha_Disease.yaml").write_text(
        _disorder("MONDO:0000001", "Alpha storage disease")
    )
    (disorders / "Beta_Disease.yaml").write_text(
        _disorder("MONDO:0000002", "Beta storage disease")
    )
    (groupings / "Gamma_Group.yaml").write_text(
        "name: Gamma grouping disorders\n"
        "mappings:\n"
        "  mondo_mappings:\n"
        "  - term:\n"
        "      id: MONDO:0000003\n"
        "      label: gamma grouping disorders\n"
        "    mapping_predicate: skos:broadMatch\n"
    )
    return [disorders, groupings]


@pytest.fixture
def counters(monkeypatch):
    """Count YAML parses and content hashes inside `dismech.stubs.model`."""
    counts = {"parse": 0, "digest": 0}
    real_load, real_digest = model.safe_load, model._digest

    def counting_load(text):
        counts["parse"] += 1
        return real_load(text)

    def counting_digest(raw):
        counts["digest"] += 1
        return real_digest(raw)

    monkeypatch.setattr(model, "safe_load", counting_load)
    monkeypatch.setattr(model, "_digest", counting_digest)
    return counts


def _age(paths, by_ns=_HOUR_NS):
    """Backdate mtimes past the racy window, as a file committed earlier would be."""
    then = time.time_ns() - by_ns
    for directory in paths:
        for path in directory.glob("*.yaml"):
            os.utime(path, ns=(then, then))


def _reset(counts):
    counts["parse"] = counts["digest"] = 0


def test_second_run_on_an_unchanged_tree_parses_nothing(kb, tmp_path, counters):
    _age(kb)
    cache = tmp_path / "cache.json"
    first = build_coverage_index(kb, cache_path=cache)
    assert counters["parse"] == 3
    assert cache.is_file()

    _reset(counters)
    second = build_coverage_index(kb, cache_path=cache)
    # Settled files are trusted on (mtime_ns, size): no hash, no parse.
    assert counters == {"parse": 0, "digest": 0}
    assert second.ids == first.ids
    assert second.labels == first.labels
    assert second.ids == {
        "MONDO:0000001": "disorders/Alpha_Disease.yaml",
        "MONDO:0000002": "disorders/Beta_Disease.yaml",
        "MONDO:0000003": "groupings/Gamma_Group.yaml",
    }
    assert second.entry_labelled("Beta storage disease") == (
        "disorders/Beta_Disease.yaml"
    )


def test_a_recently_written_file_is_hashed_not_trusted(kb, tmp_path, counters):
    """A file written just before the build may change within one mtime tick."""
    cache = tmp_path / "cache.json"
    build_coverage_index(kb, cache_path=cache)
    _reset(counters)
    build_coverage_index(kb, cache_path=cache)
    assert counters["parse"] == 0
    assert counters["digest"] == 3


def test_editing_one_entry_reparses_exactly_that_file(kb, tmp_path, counters):
    _age(kb)
    cache = tmp_path / "cache.json"
    build_coverage_index(kb, cache_path=cache)

    beta = kb[0] / "Beta_Disease.yaml"
    # Same length, so only the mtime and the content tell the edit apart.
    beta.write_text(_disorder("MONDO:0000009", "Beta storage disease"))
    _reset(counters)
    index = build_coverage_index(kb, cache_path=cache)
    assert counters["parse"] == 1
    assert index.covered_by("MONDO:0000009") == "disorders/Beta_Disease.yaml"
    assert index.covered_by("MONDO:0000002") is None


def test_an_edit_inside_one_mtime_tick_is_still_seen(kb, tmp_path, counters):
    """Same size and a restored mtime: only the content hash can tell."""
    cache = tmp_path / "cache.json"
    build_coverage_index(kb, cache_path=cache)
    beta = kb[0] / "Beta_Disease.yaml"
    stat = beta.stat()
    beta.write_text(_disorder("MONDO:0000009", "Beta storage disease"))
    os.utime(beta, ns=(stat.st_atime_ns, stat.st_mtime_ns))
    assert beta.stat().st_size == stat.st_size

    index = build_coverage_index(kb, cache_path=cache)
    assert index.covered_by("MONDO:0000009") == "disorders/Beta_Disease.yaml"


def test_a_deleted_file_drops_out(kb, tmp_path):
    _age(kb)
    cache = tmp_path / "cache.json"
    build_coverage_index(kb, cache_path=cache)
    (kb[0] / "Alpha_Disease.yaml").unlink()

    index = build_coverage_index(kb, cache_path=cache)
    assert index.covered_by("MONDO:0000001") is None
    files = json.loads(cache.read_text())["dirs"][0]["files"]
    assert set(files) == {"Beta_Disease.yaml"}


def test_a_version_bump_forces_a_rebuild(kb, tmp_path, counters, monkeypatch):
    _age(kb)
    cache = tmp_path / "cache.json"
    build_coverage_index(kb, cache_path=cache)
    monkeypatch.setattr(
        model, "COVERAGE_CACHE_VERSION", model.COVERAGE_CACHE_VERSION + 1
    )
    _reset(counters)
    build_coverage_index(kb, cache_path=cache)
    assert counters["parse"] == 3
    assert json.loads(cache.read_text())["version"] == model.COVERAGE_CACHE_VERSION


def test_a_corrupt_cache_file_reads_as_empty(kb, tmp_path, counters):
    cache = tmp_path / "cache.json"
    cache.write_text('{"version": ')
    index = build_coverage_index(kb, cache_path=cache)
    assert counters["parse"] == 3
    assert index.covered_by("MONDO:0000001") == "disorders/Alpha_Disease.yaml"
    assert json.loads(cache.read_text())["version"] == model.COVERAGE_CACHE_VERSION


def test_dismech_kb_cache_0_turns_it_off(kb, tmp_path, counters, monkeypatch):
    _age(kb)
    cache = tmp_path / "cache.json"
    build_coverage_index(kb, cache_path=cache)
    monkeypatch.setenv("DISMECH_KB_CACHE", "0")
    _reset(counters)
    index = build_coverage_index(kb, cache_path=cache)
    assert counters["parse"] == 3
    assert index.covered_by("MONDO:0000002") == "disorders/Beta_Disease.yaml"

    cache.unlink()
    build_coverage_index(kb, cache_path=cache)
    assert not cache.exists()


def test_explicit_kb_dirs_without_a_cache_path_do_not_persist(
    kb, tmp_path, monkeypatch
):
    """An ad hoc directory list must not overwrite the default KB's cache."""
    default = tmp_path / "default.json"
    monkeypatch.setenv(model.COVERAGE_CACHE_ENV, str(default))
    build_coverage_index(kb)
    assert not default.exists()


def test_a_different_directory_list_rebuilds(kb, tmp_path, counters):
    _age(kb)
    cache = tmp_path / "cache.json"
    build_coverage_index(kb, cache_path=cache)
    _reset(counters)
    index = build_coverage_index(kb[:1], cache_path=cache)
    assert counters["parse"] == 2
    assert index.covered_by("MONDO:0000003") is None


def test_default_cache_path_lives_in_the_checkout_tmp(monkeypatch):
    monkeypatch.delenv(model.COVERAGE_CACHE_ENV, raising=False)
    monkeypatch.delenv("DISMECH_ROOT", raising=False)
    root = Path(__file__).resolve().parent.parent
    monkeypatch.chdir(root)
    assert model.default_coverage_cache_path() == (
        root / "tmp" / "stub_coverage_index.json"
    )
