"""Semantic checks for ``phenotype_term`` usage across disorder files.

Background (issue #817): The ``PhenotypeTerm`` enum in ``dismech.yaml`` allows
both HP terms and MONDO terms (under ``MONDO:0000001``) so that legitimate
disease-as-feature patterns can be represented (e.g. post-infectious sequelae,
hereditary cancer-syndrome cancer risks, surgical complications). The
``linkml-term-validator`` checks that an ID is reachable and that the label is
correct, but it does not check whether the term is *semantically appropriate*
for the slot.

This module fills the QC gap with two cheap, deterministic guardrails:

1. A disorder must never list its **own** ``id`` as a ``phenotype_term`` --
   that would always be a curation error (a disease cannot be its own
   phenotype).
2. The set of MONDO terms used as ``phenotype_term`` is pinned to an
   allowlist. New MONDO usages must be added to the allowlist explicitly,
   forcing a curator to acknowledge the design intent and preventing
   accidental drift back into the patterns that motivated issue #817.
"""

from __future__ import annotations

import glob
from pathlib import Path
from typing import Iterator

import pytest
import yaml

ROOT_DIR = Path(__file__).parent.parent
KB_DIR = ROOT_DIR / "kb" / "disorders"

DISORDER_FILES = sorted(
    f for f in glob.glob(str(KB_DIR / "*.yaml")) if not f.endswith(".history.yaml")
)

# Frozen allowlist of MONDO IDs intentionally used in ``phenotype_term`` slots.
# Each entry has been reviewed and represents a legitimate disease-as-feature
# pattern (sequela, hereditary-syndrome cancer risk, organ complication, etc.).
# Adding to this set should be a deliberate curation decision -- not a default.
ALLOWED_MONDO_PHENOTYPE_TERMS: frozenset[str] = frozenset(
    {
        "MONDO:0002375",  # sebaceous adenoma (Lynch / Muir-Torre variant)
        "MONDO:0004235",  # diverticulitis (Meckel diverticulum complication)
        "MONDO:0005052",  # irritable bowel syndrome (post-infectious sequela)
        "MONDO:0005081",  # preeclampsia (antiphospholipid syndrome obstetric)
        "MONDO:0005140",  # ovarian carcinoma (Lynch cancer risk)
        "MONDO:0005575",  # colorectal cancer (Lynch cancer risk)
        "MONDO:0005851",  # Miller Fisher syndrome (Campylobacter sequela)
        "MONDO:0006807",  # intestinal perforation (Meckel complication)
        "MONDO:0007835",  # intussusception (Meckel complication)
        "MONDO:0011962",  # endometrial cancer (Lynch cancer risk)
        "MONDO:0016218",  # Guillain-Barre syndrome (Campylobacter sequela)
        "MONDO:0017376",  # reactive arthritis (Campylobacter sequela)
        "MONDO:0020654",  # renal pelvis/ureter urothelial carcinoma (Lynch)
    }
)


def _iter_phenotype_terms(node: object) -> Iterator[tuple[str, str]]:
    """Yield ``(curie, preferred_term)`` tuples for every ``phenotype_term``
    block found anywhere in ``node``.
    """
    if isinstance(node, dict):
        pt = node.get("phenotype_term")
        if isinstance(pt, dict):
            term = pt.get("term") or {}
            tid = term.get("id") if isinstance(term, dict) else None
            if isinstance(tid, str):
                yield tid, pt.get("preferred_term") or ""
        for value in node.values():
            yield from _iter_phenotype_terms(value)
    elif isinstance(node, list):
        for item in node:
            yield from _iter_phenotype_terms(item)


def _disease_term_id(data: dict) -> str | None:
    """Return the disorder's own ontology CURIE (from ``disease_term``)."""
    dt = data.get("disease_term")
    if isinstance(dt, dict):
        term = dt.get("term")
        if isinstance(term, dict):
            tid = term.get("id")
            if isinstance(tid, str):
                return tid
    return None


@pytest.mark.parametrize("filepath", DISORDER_FILES)
def test_disorder_does_not_use_own_id_as_phenotype_term(filepath: str) -> None:
    """A disorder must never list its own MONDO id as a phenotype term."""
    data = yaml.safe_load(Path(filepath).read_text())
    own_id = _disease_term_id(data)
    if not own_id:
        pytest.skip("disorder has no disease_term")

    offenders = [
        (curie, label)
        for curie, label in _iter_phenotype_terms(data)
        if curie == own_id
    ]
    assert not offenders, (
        f"{Path(filepath).name} uses its own id {own_id} as a phenotype_term: "
        f"{offenders}. A disease cannot be a phenotype of itself; move this "
        f"to differential_diagnoses, comorbidities, or remove it."
    )


def test_mondo_phenotype_terms_match_allowlist() -> None:
    """All MONDO terms used as ``phenotype_term`` must be in the allowlist.

    The allowlist exists to enforce deliberate curation: ``PhenotypeTerm``
    accepts MONDO IDs (issue #817), but every such use should be a reviewed
    disease-as-feature pattern, not an accidental fallback when an HP term
    would be more appropriate.

    To add a new MONDO phenotype term, add the CURIE to
    ``ALLOWED_MONDO_PHENOTYPE_TERMS`` with a one-line justification.
    """
    used: set[str] = set()
    used_by: dict[str, list[str]] = {}
    for filepath in DISORDER_FILES:
        data = yaml.safe_load(Path(filepath).read_text())
        for curie, _label in _iter_phenotype_terms(data):
            if curie.startswith("MONDO:"):
                used.add(curie)
                used_by.setdefault(curie, []).append(Path(filepath).name)

    unexpected = used - ALLOWED_MONDO_PHENOTYPE_TERMS
    assert not unexpected, (
        "New MONDO IDs found in phenotype_term slots that are not on the "
        "allowlist (see issue #817):\n"
        + "\n".join(
            f"  {curie} -- used in: {', '.join(sorted(set(used_by[curie])))}"
            for curie in sorted(unexpected)
        )
        + "\n\nIf this is a legitimate disease-as-feature pattern (sequela, "
        "cancer-syndrome risk, organ complication), add the CURIE to "
        "ALLOWED_MONDO_PHENOTYPE_TERMS in tests/test_phenotype_term_semantics.py "
        "with a one-line justification. Otherwise, replace the MONDO term "
        "with a more appropriate HP term."
    )

    # Also fail if an allowlist entry is no longer used -- keeps the list
    # honest as files evolve.
    stale = ALLOWED_MONDO_PHENOTYPE_TERMS - used
    assert not stale, (
        "ALLOWED_MONDO_PHENOTYPE_TERMS contains entries that are no longer "
        "used as phenotype_term anywhere in kb/disorders/. Please remove: "
        f"{sorted(stale)}"
    )
