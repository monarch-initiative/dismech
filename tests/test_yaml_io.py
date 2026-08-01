"""Tests for the shared YAML loading helpers (issue #7502)."""

from __future__ import annotations

import io
import os

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


def test_safe_load_path_pins_utf8_rather_than_the_locale_default(tmp_path):
    """Part of why the helper exists: non-ASCII must not depend on the locale."""
    path = tmp_path / "disorder.yaml"
    path.write_bytes("name: Béhçet Diseáse — ünicode\n".encode())
    assert yaml_io.safe_load_path(path)["name"] == "Béhçet Diseáse — ünicode"


def test_safe_load_is_safe_and_rejects_arbitrary_object_construction():
    """A "fast" loader that silently became unsafe would be a security regression."""
    with pytest.raises(yaml.YAMLError):
        yaml_io.safe_load("!!python/object/apply:os.system ['echo pwned']")


def test_safe_load_propagates_parse_errors():
    with pytest.raises(yaml.YAMLError):
        yaml_io.safe_load("key: [unclosed\n")


def test_libyaml_is_available_in_this_environment():
    """Guard the performance win, but only where losing it is a real regression.

    The fallback keeps results correct without libyaml, so losing the C loader is a
    performance bug, not a correctness one — and a source-built PyYAML (no libyaml
    headers available at build time) is exactly the case the fallback exists to
    support. So this hard-fails on CI, where a silent fallback would quietly hand
    back the ~4x recovered in #7502, and merely skips with a warning locally.
    """
    if yaml_io.HAVE_LIBYAML:
        return

    message = (
        "libyaml (yaml.CSafeLoader) is unavailable; YAML parsing has fallen back to "
        "the pure-Python loader and whole-KB operations will be ~12x slower. Install "
        "a PyYAML wheel, or libyaml headers before building it from source."
    )
    if os.environ.get("CI"):
        pytest.fail(message)
    pytest.skip(message)
