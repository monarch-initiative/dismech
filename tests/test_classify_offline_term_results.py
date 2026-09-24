"""Unit tests for scripts/classify_offline_term_results.py (dismech#12658).

The fixtures are real linkml-term-validator 0.4.5 ``--offline`` output. If an
upgrade rewords the "not checked" messages these tests should fail, not the
classifier silently start treating them as errors, or errors as unchecked.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "classify_offline_term_results.py"

_spec = importlib.util.spec_from_file_location("classify_offline", SCRIPT)
classify_offline = importlib.util.module_from_spec(_spec)
# Registered first: @dataclass looks its module up in sys.modules.
sys.modules[_spec.name] = classify_offline
_spec.loader.exec_module(classify_offline)
classify = classify_offline.classify

ENUM_NOT_MATERIALIZED = """\
  ❌ ERROR: Cannot validate 'GO:0006954' against dynamic enum 'PhenotypeTerm' offline: enum closure not materialized in cache (materialize it online first with --saturate-enum-caches or --cache-strategy greedy, then re-run offline)
      path: phenotypes[1].phenotype_term.term
      slot: term
      field: id
      validation: offline (enum cache not materialized)
"""

NOT_IN_CACHE = """\
  ❌ ERROR: Term 'HP:9999998' not found in offline cache
      path: phenotypes[2].phenotype_term.term
      slot: term
      field: id
      prefix: HP (offline: cache-only)
"""

LABEL_MISMATCH = """\
  ⚠️  WARN: Label mismatch for 'HP:0030828': expected 'Wheezing', got 'Wheezingz'
      path: phenotypes[0].phenotype_term.term
      slot: term
      label_field: label
      curie: HP:0030828
"""

HEADER = "\n❌ Validation failed with N issue(s):\n\n"


def test_a_passing_offline_run_is_clean() -> None:
    code, lines = classify("✅ Validation passed", 0)
    assert code == 0
    assert not any("not checked" in line for line in lines)


def test_unchecked_terms_pass_and_are_named() -> None:
    code, lines = classify(HEADER + ENUM_NOT_MATERIALIZED + NOT_IN_CACHE, 1)
    assert code == 0
    assert (
        "  not checked: GO:0006954 at phenotypes[1].phenotype_term.term "
        "(PhenotypeTerm membership not in the local enum cache)"
    ) in lines
    assert (
        "  not checked: HP:9999998 at phenotypes[2].phenotype_term.term "
        "(not in the local term cache)"
    ) in lines


def test_both_reasons_for_one_term_are_merged_into_one_line() -> None:
    same_term = ENUM_NOT_MATERIALIZED.replace("GO:0006954", "HP:9999998").replace(
        "phenotypes[1]", "phenotypes[2]"
    )
    code, lines = classify(HEADER + same_term + NOT_IN_CACHE, 1)
    assert code == 0
    unchecked = [line for line in lines if "not checked:" in line]
    assert unchecked == [
        (
            "  not checked: HP:9999998 at phenotypes[2].phenotype_term.term "
            "(PhenotypeTerm membership not in the local enum cache; "
            "not in the local term cache)"
        )
    ]


def test_a_cached_label_mismatch_blocks() -> None:
    code, lines = classify(HEADER + LABEL_MISMATCH + NOT_IN_CACHE, 1)
    assert code == 1
    assert any("Label mismatch for 'HP:0030828'" in line for line in lines)
    assert not any("HP:9999998" in line for line in lines)


def test_an_unrecognised_error_blocks() -> None:
    """Anything not known to mean 'unchecked' is treated as a real error."""
    other = "  ❌ ERROR: Value 'HP:1' not in enum 'PhenotypeTerm'\n      path: x\n"
    code, _ = classify(HEADER + other, 1)
    assert code == 1


def test_unreadable_output_keeps_the_old_warning() -> None:
    code, lines = classify("Traceback (most recent call last):\n  boom", 1)
    assert code == 0
    assert lines == [
        (
            "not checked: all terms (the offline recheck exited 1 without results "
            "this script could read)"
        )
    ]


def test_classifier_edits_trigger_the_pytest_lane() -> None:
    """A PR touching only this script must still run these tests."""
    workflow = (ROOT / ".github" / "workflows" / "main.yaml").read_text()
    assert "- 'scripts/classify_offline_term_results.py'" in workflow
