"""Tests for the shared YAML loading helpers (issue #7502)."""

from __future__ import annotations

import io

import pytest
import yaml

from dismech import yaml_io

DOC = """
name: Example Disorder
phenotypes:
  - name: Wheezing
    frequency: FREQUENT
  - name: Dyspnea
nested:
  a: [1, 2, 3]
  b: {c: true, d: null}
"""


def test_safe_load_matches_pyyaml_safe_load():
    """The fast loader must be a behavioural drop-in, not just a faster one."""
    assert yaml_io.safe_load(DOC) == yaml.safe_load(DOC)


def test_safe_load_accepts_a_file_object():
    assert yaml_io.safe_load(io.StringIO(DOC))["name"] == "Example Disorder"


def test_safe_load_path_reads_from_disk(tmp_path):
    path = tmp_path / "disorder.yaml"
    path.write_text(DOC, encoding="utf-8")
    assert yaml_io.safe_load_path(path) == yaml.safe_load(DOC)


def test_safe_load_all_yields_every_document():
    stream = "a: 1\n---\na: 2\n"
    assert [doc["a"] for doc in yaml_io.safe_load_all(stream)] == [1, 2]


def test_safe_load_is_safe_and_rejects_arbitrary_object_construction():
    """A "fast" loader that silently became unsafe would be a security regression."""
    with pytest.raises(yaml.YAMLError):
        yaml_io.safe_load("!!python/object/apply:os.system ['echo pwned']")


def test_safe_load_propagates_parse_errors():
    with pytest.raises(yaml.YAMLError):
        yaml_io.safe_load("key: [unclosed\n")


def test_libyaml_is_available_in_this_environment():
    """Guard the performance win.

    The fallback keeps results correct without libyaml, but silently losing the C
    loader would quietly hand CI back the ~4x it recovered in #7502. PyYAML's Linux
    wheels bundle libyaml, so this should hold on the runner and on any normal dev
    install.
    """
    assert yaml_io.HAVE_LIBYAML, (
        "libyaml (yaml.CSafeLoader) is unavailable; YAML parsing has fallen back to "
        "the pure-Python loader and whole-KB operations will be ~12x slower."
    )
