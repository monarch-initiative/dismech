"""Tests for the shared YAML loading helpers (issue #7502)."""

from __future__ import annotations

import io
import os
from pathlib import Path

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


def test_safe_load_path_pins_utf8_rather_than_the_locale_default(tmp_path, monkeypatch):
    """Part of why the helper exists: non-ASCII must not depend on the locale.

    Reading the file and asserting the text round-trips proves nothing on its own —
    it passes against a bare ``read_text()`` too, because the locale encoding is
    already UTF-8 on CI and most dev machines. To actually exercise the guarantee,
    simulate a non-UTF-8 locale: a bare ``read_text()`` would mojibake or raise,
    so the assertion only holds if the helper passes ``encoding`` explicitly.
    """
    content = "name: Béhçet Diseáse — ünicode\n"
    path = tmp_path / "disorder.yaml"
    path.write_bytes(content.encode("utf-8"))

    real_read_text = Path.read_text
    seen: dict[str, object] = {}

    def locale_bound_read_text(self, encoding=None, **kwargs):
        # Stand in for a machine whose locale default is not UTF-8.
        seen["encoding"] = encoding
        return real_read_text(self, encoding=encoding or "cp1252", **kwargs)

    monkeypatch.setattr(Path, "read_text", locale_bound_read_text)

    # The real guarantee: correct text even when the platform default is not UTF-8.
    assert yaml_io.safe_load_path(path)["name"] == "Béhçet Diseáse — ünicode"

    # Belt and braces, deliberately soft. `.get` rather than `[...]` so a legitimate
    # reimplementation (e.g. `path.open(encoding="utf-8")`, which never touches
    # read_text) fails with this message instead of an unhelpful KeyError.
    assert seen.get("encoding", "utf-8") == "utf-8", (
        "safe_load_path must pass encoding explicitly rather than inheriting the "
        "platform default, or non-ASCII KB content breaks on non-UTF-8 locales."
    )


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
    if os.environ.get("CI", "").lower() not in ("", "0", "false"):
        pytest.fail(message)
    pytest.skip(message)
