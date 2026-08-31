"""Ontology terms nested in `qualifiers` need their own guard.

`Qualifier.predicate` and `Qualifier.value` are plain `Descriptor`s, so each
carries a real `term:` binding. But `linkml-term-validator` validates slots whose
range is bound to an ontology-backed dynamic enum, and the generic `Descriptor`
has no such binding — so nothing under `qualifiers` is ever looked at. Putting
"Totally Bogus Fabricated Label" on one and running

    just validate-terms kb/disorders/Clostridioides_difficile_Infection.yaml

reports "Validation passed" (issue #10197).

That blind spot had already admitted a real defect: NCIT:C288 was curated as
"vancomycin" when NCIT's label for that code is Azacitidine, an antineoplastic.
Vancomycin is NCIT:C925.
"""

import subprocess
import sys
from pathlib import Path

# See the note in test_causal_targets.py: the `sys.path` preamble must sit
# directly before the import for ruff's E402 allowance to apply.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from check_qualifier_terms import (
    Term,
    classify,
    configured_prefixes,
    iter_qualifier_terms,
)

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_qualifier_terms.py"

CACHE = {"NCIT:C925": "Vancomycin", "NCIT:C2259": "Therapeutic Agent"}


def test_finds_terms_on_both_qualifier_roles():
    data = {
        "treatments": [
            {
                "treatment_term": {
                    "qualifiers": [
                        {
                            "predicate": {"term": {"id": "NCIT:C2259", "label": "A"}},
                            "value": {"term": {"id": "NCIT:C925", "label": "B"}},
                        }
                    ]
                }
            }
        ]
    }
    found = iter_qualifier_terms(data, "x.yaml")
    assert {(t.role, t.curie) for t in found} == {
        ("predicate", "NCIT:C2259"),
        ("value", "NCIT:C925"),
    }


def test_label_disagreeing_with_the_ontology_is_a_finding():
    """The defect that reached main: a CURIE naming a different concept."""
    terms = [Term("x.yaml", "value", "NCIT:C925", "azacitidine")]
    wrong, _unverified, _unconfigured, ok = classify(terms, CACHE)
    assert [(t.curie, actual) for t, actual in wrong] == [("NCIT:C925", "Vancomycin")]
    assert ok == 0


def test_matching_label_is_clean():
    terms = [Term("x.yaml", "value", "NCIT:C925", "Vancomycin")]
    wrong, _, _, ok = classify(terms, CACHE)
    assert wrong == [] and ok == 1


def test_uncached_curie_is_reported_not_failed():
    """The caches are populated by validating a term, and these never are.

    'Absent from the cache' is therefore the normal state for a qualifier-only
    CURIE, not evidence of a defect — gating on it would be wrong.
    """
    terms = [Term("x.yaml", "value", "NCIT:C99999", "Whatever")]
    wrong, unverified, _, _ = classify(terms, CACHE)
    assert wrong == []
    assert [t.curie for t in unverified] == ["NCIT:C99999"]


def test_prefixes_without_an_adapter_are_counted_separately():
    """RO and PR have no adapter, so no tooling can check them at all.

    Kept apart from `unverified` because the fix is a config decision, not a
    cache refresh.
    """
    terms = [
        Term("x.yaml", "predicate", "RO:0000057", "has participant"),
        Term("x.yaml", "value", "PR:000029971", "creatine kinase"),
    ]
    wrong, unverified, unconfigured, _ = classify(terms, CACHE)
    assert wrong == [] and unverified == []
    assert {t.curie.split(":")[0] for t in unconfigured} == {"RO", "PR"}


def test_unconfigured_set_is_derived_from_oak_config_not_hardcoded():
    """Adding an adapter must move a prefix out of the unvalidatable bucket.

    A hardcoded list fails quietly: close the RO gap this script reports, and a
    stale constant keeps excusing those terms until somebody notices.
    """
    real = configured_prefixes()
    assert "NCIT" in real and "CHEBI" in real
    assert "RO" not in real and "PR" not in real

    term = [Term("x.yaml", "predicate", "RO:0000057", "has participant")]
    # With RO configured, it is no longer excused — it becomes an ordinary
    # uncached term instead.
    _, unverified, unconfigured, _ = classify(term, CACHE, configured=real | {"RO"})
    assert unconfigured == []
    assert [t.curie for t in unverified] == ["RO:0000057"]


def test_committed_kb_qualifier_labels_are_correct():
    """The gate itself, over the real KB."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
