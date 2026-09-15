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
from unittest import mock

# See the note in test_causal_targets.py: the `sys.path` preamble must sit
# directly before the import for ruff's E402 allowance to apply.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import check_qualifier_terms
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


def test_a_transport_failure_is_not_reported_as_a_wrong_binding():
    """ "We could not check this" and "this is wrong" are different claims.

    `--resolve` used to catch every lookup failure and print it as
    `<CURIE DOES NOT RESOLVE>` under the wrong-label heading, so a flaky link
    accused correct bindings of being fabricated. Six consecutive runs against an
    unchanged tree once produced 8, 2, 2, 0, 9 and 12 "findings", every one a
    transport error and not one a real mismatch. This script already keeps that
    distinction for prefixes with no adapter; it owes the same honesty here.
    """
    from requests.exceptions import ConnectionError as RequestsConnectionError

    class _Unreachable:
        def label(self, curie):
            raise RequestsConnectionError("connection reset")

    term = Term("x.yaml", "value", "NCIT:C925", "Vancomycin")
    with mock.patch("oaklib.get_adapter", return_value=_Unreachable()):
        wrong, missing, unreachable = check_qualifier_terms.resolve_remote(
            [term], attempts=2
        )

    assert wrong == [], "a network failure is not evidence about the binding"
    assert missing == [], "unreachable is not the same claim as nonexistent"
    assert [t.curie for t, _ in unreachable] == ["NCIT:C925"]
    assert "could not be reached" in unreachable[0][1]


def test_a_404_is_reported_as_a_nonexistent_curie():
    """A definitive not-found is the most serious thing this check can say.

    So it gets its own bucket rather than sharing one with transport failures:
    it is definitive, it is about the binding, and it has to gate. Sharing the
    bucket meant `--resolve` could be handed two invented CURIEs, name them
    correctly, and still exit 0 on a line reading `OK: ... match the ontology`.
    """
    from requests.exceptions import HTTPError
    from requests.models import Response

    response = Response()
    response.status_code = 404

    class _NotFound:
        def label(self, curie):
            raise HTTPError(response=response)

    term = Term("x.yaml", "value", "NCIT:C99999999", "Nonexistent")
    with mock.patch("oaklib.get_adapter", return_value=_NotFound()):
        wrong, missing, unreachable = check_qualifier_terms.resolve_remote(
            [term], attempts=2
        )

    assert wrong == [], "a 404 is not a label mismatch; there is no label"
    assert unreachable == [], "a 404 is definitive, not a failed lookup"
    assert [t.curie for t, _ in missing] == ["NCIT:C99999999"]
    assert "does not exist" in missing[0][1]


def test_a_nonexistent_curie_makes_the_run_fail(tmp_path, capsys):
    """The class the docstring calls most serious has to actually gate.

    It previously shared the advisory bucket with transport failures, so a run
    against two fabricated CURIEs printed them and then exited 0 under
    `OK: 0 qualifier term label(s) match the ontology`.
    """
    from requests.exceptions import HTTPError
    from requests.models import Response

    response = Response()
    response.status_code = 404

    class _NotFound:
        def label(self, curie):
            raise HTTPError(response=response)

    entry = tmp_path / "Probe.yaml"
    entry.write_text(
        "name: Probe\n"
        "treatments:\n"
        "- name: T\n"
        "  treatment_term:\n"
        "    preferred_term: t\n"
        "    qualifiers:\n"
        "    - predicate:\n"
        "        preferred_term: p\n"
        "        term: {id: NCIT:C99999999, label: Invented}\n"
        "      value:\n"
        "        preferred_term: v\n"
        "        term: {id: NCIT:C88888888, label: Also Invented}\n"
    )

    argv = ["check_qualifier_terms.py", str(entry), "--resolve"]
    with (
        mock.patch("oaklib.get_adapter", return_value=_NotFound()),
        mock.patch.object(check_qualifier_terms.sys, "argv", argv),
    ):
        rc = check_qualifier_terms.main()

    out = capsys.readouterr().out
    assert rc == 1, "two fabricated CURIEs must not finish on exit 0"
    assert "do not exist in the ontology" in out
    assert "2 finding(s)." in out
    assert "OK:" not in out, "the summary must not read as a pass"


def test_not_found_classification_walks_the_exception_chain():
    """OAK wraps the underlying HTTP error, so the 404 is not the outer type."""
    from requests.exceptions import ConnectionError as RequestsConnectionError
    from requests.exceptions import HTTPError
    from requests.models import Response

    not_found = Response()
    not_found.status_code = 404
    server_error = Response()
    server_error.status_code = 503

    wrapped = RuntimeError("adapter failed")
    wrapped.__cause__ = HTTPError(response=not_found)

    assert check_qualifier_terms._is_not_found(wrapped) is True
    assert (
        check_qualifier_terms._is_not_found(HTTPError(response=server_error)) is False
    )
    assert (
        check_qualifier_terms._is_not_found(RequestsConnectionError("reset")) is False
    )


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
