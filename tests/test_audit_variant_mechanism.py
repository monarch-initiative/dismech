"""Tests for the Mendelian variant-mechanism audit (``scripts/audit_variant_mechanism.py``)."""

from __future__ import annotations

import importlib.util
import os
import textwrap
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SCRIPT_PATH = ROOT / "scripts" / "audit_variant_mechanism.py"
_spec = importlib.util.spec_from_file_location("audit_variant_mechanism", SCRIPT_PATH)
audit = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(audit)


@pytest.fixture(autouse=True)
def _restore_kb_cache_env():
    """Keep ``main()``'s ``kb_cache.default_off()`` inside this test.

    ``default_off()`` belongs in ``main()`` (CLAUDE.md), but it sets a
    process-wide environment variable. Calling ``main()`` from a test would
    otherwise disable the parsed-KB cache for every test that runs after it in
    the same pytest process -- which silently failed ``tests/test_kb_cache.py``.
    """
    sentinel = object()
    before = os.environ.get("DISMECH_KB_CACHE", sentinel)
    try:
        yield
    finally:
        if before is sentinel:
            os.environ.pop("DISMECH_KB_CACHE", None)
        else:
            os.environ["DISMECH_KB_CACHE"] = before

BASE = """\
name: Test Disorder
inheritance:
- name: Autosomal dominant
  inheritance_term:
    preferred_term: Autosomal dominant inheritance
    term:
      id: HP:0000006
      label: Autosomal dominant inheritance
genetic:
- name: GENE1
  relationship_type: CAUSATIVE
pathophysiology:
- name: GENE1 Loss-of-Function Variant
  description: Heterozygous loss-of-function variants in GENE1.
{extra}
"""


def _write(tmp_path, extra=""):
    path = tmp_path / "Test_Disorder.yaml"
    path.write_text(BASE.format(extra=textwrap.indent(extra, "  ")), encoding="utf-8")
    return str(path)


def test_mendelian_entry_without_category_is_a_gap(tmp_path):
    row = audit.audit_file(_write(tmp_path))
    assert row["mendelian"] is True
    assert row["modes"] == "AD"
    assert row["n_causal"] == 1
    assert row["annotated"] is False
    assert "lof" in row["prose"].split(",")


def test_functional_impact_category_marks_entry_annotated(tmp_path):
    extra = textwrap.dedent(
        """\
        genetic_context:
          functional_impact_category: LOSS_OF_FUNCTION
        """
    )
    row = audit.audit_file(_write(tmp_path, extra))
    assert row["annotated"] is True
    assert row["categories"] == "LOSS_OF_FUNCTION"


def test_somatic_driver_entry_is_not_mendelian(tmp_path):
    path = tmp_path / "Somatic.yaml"
    path.write_text(
        BASE.format(extra="").replace("relationship_type: CAUSATIVE",
                                      "relationship_type: SOMATIC_DRIVER"),
        encoding="utf-8",
    )
    row = audit.audit_file(str(path))
    assert row["mendelian"] is False


def test_summary_runs_on_given_files(tmp_path, capsys):
    path = _write(tmp_path)
    assert audit.main([path, "--cache-dir", str(tmp_path)]) == 0
    out = capsys.readouterr().out
    assert "without (the gap):                      1" in out


def test_summary_breaks_out_unknown_only_entries(tmp_path, capsys):
    """UNKNOWN is a recorded claim, but a contested one must stay countable."""
    extra = textwrap.dedent(
        """\
        genetic_context:
          functional_impact_category: UNKNOWN
        """
    )
    path = _write(tmp_path, extra)
    assert audit.main([path, "--cache-dir", str(tmp_path)]) == 0
    out = capsys.readouterr().out
    assert "with functional_impact_category:        1" in out
    assert "of which recorded as UNKNOWN only:    1" in out
    assert "without (the gap):                      0" in out


def test_with_cached_hits_also_filters_under_all(tmp_path, capsys):
    """``--with-cached-hits`` used to be dropped when ``--all`` was given.

    ``--all`` widens the listing from the gap to every Mendelian entry; it is
    not a request to stop filtering, so an entry with no cached mechanism
    sentence must still be excluded.
    """
    annotated = textwrap.dedent(
        """\
        genetic_context:
          functional_impact_category: LOSS_OF_FUNCTION
        """
    )
    path = _write(tmp_path, annotated)

    # No PMID is cited, so cached_hits is 0 for this entry.
    assert audit.main([path, "--cache-dir", str(tmp_path), "--format", "list", "--all"]) == 0
    assert "Test Disorder" in capsys.readouterr().out

    assert audit.main(
        [path, "--cache-dir", str(tmp_path), "--format", "list", "--all", "--with-cached-hits"]
    ) == 0
    assert capsys.readouterr().out.strip() == ""
