"""Tests for the Mendelian variant-mechanism audit (``scripts/audit_variant_mechanism.py``)."""

from __future__ import annotations

import importlib.util
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT_PATH = ROOT / "scripts" / "audit_variant_mechanism.py"
_spec = importlib.util.spec_from_file_location("audit_variant_mechanism", SCRIPT_PATH)
audit = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(audit)

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
