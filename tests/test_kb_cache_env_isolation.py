"""`DISMECH_KB_CACHE` set by one test never reaches the next (issue #11942).

`preserve_kb_cache_environment` in `tests/conftest.py` does the work. These
tests pin it: each "leak" test pollutes the variable the way a scanner's
`main()` does, and the test defined after it checks that nothing survived.
pytest runs a module's tests in definition order, so the pairs are ordered.
"""

from __future__ import annotations

import os

from dismech import kb_cache

# Read at import, before any test in this module runs. The conftest fixture
# resets to the value captured when conftest was imported, which is earlier
# still, and nothing between the two writes the variable.
AT_IMPORT = os.environ.get("DISMECH_KB_CACHE")


def test_a_leak_through_default_off():
    os.environ.pop("DISMECH_KB_CACHE", None)
    kb_cache.default_off()
    assert os.environ["DISMECH_KB_CACHE"] == "0"


def test_b_default_off_did_not_leak():
    assert os.environ.get("DISMECH_KB_CACHE") == AT_IMPORT


def test_c_leak_that_monkeypatch_records_as_the_original(monkeypatch):
    # default_off() bypasses monkeypatch, so the later setenv snapshots the
    # polluted "0" and monkeypatch's own teardown restores it.
    os.environ.pop("DISMECH_KB_CACHE", None)
    kb_cache.default_off()
    monkeypatch.setenv("DISMECH_KB_CACHE", "1")


def test_d_monkeypatch_teardown_did_not_leak():
    assert os.environ.get("DISMECH_KB_CACHE") == AT_IMPORT
