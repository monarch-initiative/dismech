"""Tests for `scripts/backfill_animal_model_terms.py`.

Focused on `verify_only_additions`, the guard that makes line-level text surgery
on KB YAML safe. The script inserts `species_term` / `associated_phenotype_terms`
by line anchor rather than by a ruamel round-trip (a round-trip re-wrapped
hand-wrapped scalars and produced thousands of lines of pure churn), so the guard
is what proves the rewrite is semantically a pure addition.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import backfill_animal_model_terms as B  # noqa: E402

KEYS = ("species_term", "associated_phenotype_terms")

BOUND = """animal_models:
- name: A
  species: Dog
  species_term:
    preferred_term: Dog
    term:
      id: NCBITaxon:9615
      label: Canis lupus familiaris
  genotype: x
- name: B
  species: Mouse
  genotype: y
"""


def _insert_species_term_on_b(text: str) -> str:
    """Add the binding model B is missing, leaving model A untouched."""
    block = B._emit_block(
        {"species_term": B._descriptor("Mouse", "NCBITaxon:10090", "Mus musculus")}, 2
    )
    lines = text.splitlines(keepends=True)
    idx = next(i for i, l in enumerate(lines) if l.startswith("  species: Mouse"))
    lines[idx + 1 : idx + 1] = block
    return "".join(lines)


def test_pure_addition_passes():
    assert B.verify_only_additions(BOUND, _insert_species_term_on_b(BOUND), KEYS) is None


def test_partly_bound_file_is_not_rejected():
    """Regression: a file that ALREADY carries a binding must still verify.

    The first version stripped the added keys from the updated document only, so
    model A's pre-existing `species_term` survived in `before` and not in
    `after`, and a correct rewrite was rejected as "changed content beyond the
    added keys". Eight files failed this way on the first re-run over a KB that
    an earlier run had already partly bound -- i.e. the script was not idempotent,
    which is the one property a re-runnable migration has to have.
    """
    updated = _insert_species_term_on_b(BOUND)
    assert "species_term" in BOUND  # the precondition that triggered the bug
    assert B.verify_only_additions(BOUND, updated, KEYS) is None


def test_changed_existing_binding_is_rejected():
    """Stripping both sides must not blind the guard to a modified binding."""
    tampered = _insert_species_term_on_b(BOUND).replace("NCBITaxon:9615", "NCBITaxon:9606")
    problem = B.verify_only_additions(BOUND, tampered, KEYS)
    assert problem is not None and "existing" in problem


def test_unrelated_edit_is_rejected():
    tampered = _insert_species_term_on_b(BOUND).replace("genotype: y", "genotype: CHANGED")
    assert B.verify_only_additions(BOUND, tampered, KEYS) is not None


def test_dropped_model_is_rejected():
    truncated = "\n".join(BOUND.splitlines()[:-3]) + "\n"
    problem = B.verify_only_additions(BOUND, truncated, KEYS)
    assert problem is not None


def test_unparseable_result_is_rejected():
    problem = B.verify_only_additions(BOUND, BOUND + "\n  : : bad\n", KEYS)
    assert problem is not None and "parse" in problem


@pytest.mark.parametrize(
    "raw,expect",
    [
        ("Mus musculus", "AUTO"),
        ("Mouse and rat", "MULTI_SPECIES"),
    ],
)
def test_species_verdicts_offline(raw, expect):
    """Resolution verdicts that need no network: the multi-species refusal."""
    resolver = B.Resolver(B.TAXON_ADAPTER, {}, offline=True)
    res = B.resolve_species(resolver, raw)
    if expect == "MULTI_SPECIES":
        assert res.verdict == "MULTI_SPECIES" and not res.bindable
    else:
        # offline with an empty cache cannot resolve; it must refuse, never guess
        assert not res.bindable
