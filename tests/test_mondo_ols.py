"""MONDO identity facts from OLS when the local build is absent (#15436).

Without ``mondo.db``, ``just preflight-dr`` used to exit 2 and
``dismech.research_anchors`` sent the provider no OMIM number and no MONDO
synonyms. Both now read the term from OLS. These tests pin that the OLS path is
taken only without the local build, that it yields the same facts the local
build would (MONDO:0013686 -> CAV3, OMIM:614321), and that an unreachable OLS
still fails loudly in the preflight rather than reading as "no causal gene".

The OLS responses are recorded fixtures under ``tests/data/ols``, trimmed to the
fields :mod:`dismech.mondo_ols` reads. Nothing here touches the network or opens
an ontology build.
"""

from __future__ import annotations

import json
import urllib.error
from pathlib import Path

import pytest

import dismech.mondo_ols as ols
import dismech.preflight_dr as P
from dismech import research_anchors
from dismech.mondo_ols import (
    OlsLookupError,
    OlsMondoAdapter,
    OlsTermNotFound,
    entity_url,
    fetch_mondo_term,
    parse_mondo_entity,
)
from dismech.preflight_dr import (
    PASS,
    SKIP,
    WARN,
    MondoBuildUnavailable,
    fetch_mondo_record,
    main,
)
from dismech.research_anchors import collect_anchors

FIXTURES = Path(__file__).parent / "data" / "ols"
TATEYAMA = "MONDO:0013686"  # distal myopathy, Tateyama type: CAV3, OMIM:614321
MRD64 = "MONDO:0030934"  # intellectual developmental disorder, AD 64: ZNF292
OBSOLETE = "MONDO:0000002"  # obsolete 46,XX sex reversal, replaced by MONDO:0009299


def _fixture(curie: str) -> dict:
    return json.loads((FIXTURES / f"{curie.replace(':', '_')}.json").read_text())


@pytest.fixture
def ols_calls(monkeypatch):
    """Serve the recorded fixtures in place of OLS, recording each URL asked for."""
    calls: list[str] = []
    responses = {entity_url(c): _fixture(c) for c in (TATEYAMA, MRD64, OBSOLETE)}
    responses[f"{ols.OLS_API}/ontologies/mondo"] = {"config": {"version": "2026-10-06"}}

    def _get_json(url, timeout):
        calls.append(url)
        if url not in responses:
            raise OlsTermNotFound(f"OLS returned HTTP 404 for {url}")
        return responses[url]

    monkeypatch.setattr(ols, "_get_json", _get_json)
    return calls


@pytest.fixture
def ols_down(monkeypatch):
    def _get_json(url, timeout):
        raise OlsLookupError(f"could not reach OLS ({url}): connection refused")

    monkeypatch.setattr(ols, "_get_json", _get_json)


@pytest.fixture
def no_local_builds(monkeypatch, tmp_path):
    """An empty build directory, and opening any OAK adapter is fatal.

    Opening ``sqlite:obo:*`` on a missing build downloads it, so the test must
    prove no adapter is opened at all.
    """
    monkeypatch.setenv("PYSTOW_HOME", str(tmp_path))

    def _explode(spec, *_args, **_kwargs):  # pragma: no cover - must never run
        raise AssertionError(f"{spec} was opened; it would have been downloaded")

    monkeypatch.setattr("oaklib.get_adapter", _explode)


# --------------------------------------------------------------------------
# Parsing the OLS response
# --------------------------------------------------------------------------


def test_the_entity_url_double_encodes_the_iri():
    assert entity_url(TATEYAMA) == (
        "https://www.ebi.ac.uk/ols4/api/v2/ontologies/mondo/entities/"
        "http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FMONDO_0013686"
    )


def test_parse_reads_the_causal_gene_omim_xref_and_label():
    facts = parse_mondo_entity(_fixture(TATEYAMA), TATEYAMA)
    assert facts.label == "distal myopathy, Tateyama type"
    # The casing the local sqlite:obo:mondo build emits for an RO:0004003 object.
    assert facts.genes == ("HGNC:1529",)
    assert dict(facts.gene_labels) == {"HGNC:1529": "CAV3"}
    assert facts.omim_ids == ("614321",)
    assert "Orphanet:488650" in facts.xrefs
    # Its two synonyms are related, not exact, so neither is an identity anchor.
    assert facts.exact_synonyms == ()


def test_parse_reads_exact_synonyms_but_not_broad_ones():
    facts = parse_mondo_entity(_fixture(MRD64), MRD64)
    assert facts.genes == ("HGNC:18410",)
    assert facts.omim_ids == ("619188",)
    assert "ZNF292-related neurodevelopmental disorder" in facts.exact_synonyms
    assert "MRD64" in facts.exact_synonyms
    assert "ZNF292-related syndrome" not in facts.exact_synonyms  # a broad synonym


def test_parse_accepts_single_values_where_ols_usually_sends_lists():
    payload = {
        "iri": "http://purl.obolibrary.org/obo/MONDO_0000001",
        "label": "x",
        "relatedTo": {
            "property": ols.GENE_PROPERTY,
            "value": "http://identifiers.org/hgnc/5",
        },
        ols.DBXREF: "OMIM:100100",
        ols.EXACT_SYNONYM: {"value": "y", "axioms": []},
    }
    facts = parse_mondo_entity(payload, "MONDO:0000001")
    assert facts.genes == ("HGNC:5",)
    assert facts.omim_ids == ("100100",)
    assert facts.exact_synonyms == ("y",)


def test_parse_refuses_an_answer_about_another_term():
    with pytest.raises(OlsLookupError, match="different entity"):
        parse_mondo_entity(_fixture(MRD64), TATEYAMA)


def test_omimps_is_not_an_omim_entry():
    facts = ols.MondoTermFacts(id=TATEYAMA, xrefs=("OMIMPS:160000", "OMIM:614321"))
    assert facts.omim_ids == ("614321",)


def test_a_404_is_reported_as_an_unknown_term(monkeypatch):
    def _urlopen(request, timeout):
        raise urllib.error.HTTPError(request.full_url, 404, "Not Found", {}, None)

    monkeypatch.setattr(ols.urllib.request, "urlopen", _urlopen)
    with pytest.raises(OlsTermNotFound, match="OLS has no MONDO term MONDO:9999999"):
        fetch_mondo_term("MONDO:9999999")


def test_an_unreachable_ols_raises_rather_than_answering_empty(monkeypatch):
    def _urlopen(request, timeout):
        raise urllib.error.URLError("timed out")

    monkeypatch.setattr(ols.urllib.request, "urlopen", _urlopen)
    with pytest.raises(OlsLookupError, match="could not reach OLS"):
        fetch_mondo_term(TATEYAMA)


def test_the_adapter_fetches_each_term_once(ols_calls):
    adapter = OlsMondoAdapter()
    assert adapter.label(TATEYAMA) == "distal myopathy, Tateyama type"
    assert list(adapter.relationships([TATEYAMA])) == [
        (TATEYAMA, "RO:0004003", "HGNC:1529")
    ]
    assert adapter.label("HGNC:1529") == "CAV3"
    assert ("oio:hasDbXref", "OMIM:614321") in adapter.simple_mappings_by_curie(
        TATEYAMA
    )
    assert ols_calls == [entity_url(TATEYAMA)]


def test_the_adapter_refuses_a_reverse_query(ols_calls):
    adapter = OlsMondoAdapter()
    assert adapter.supports_reverse_relationships is False
    with pytest.raises(NotImplementedError, match="local MONDO build"):
        list(adapter.relationships(predicates=["RO:0004003"], objects=["HGNC:1529"]))


# --------------------------------------------------------------------------
# preflight-dr
# --------------------------------------------------------------------------


def test_preflight_reads_mondo_from_ols_without_the_local_build(
    no_local_builds, ols_calls
):
    record = fetch_mondo_record(TATEYAMA, use_hgnc=False)
    assert record.genes == ("CAV3",)
    assert record.gene_curies == {"CAV3": "HGNC:1529"}
    assert record.omim_ids == ("614321",)
    assert record.lookup_errors == ()
    assert record.source.startswith("OLS (")
    assert "MONDO release 2026-10-06" in record.source


def test_the_local_build_is_preferred_when_present(monkeypatch, tmp_path):
    monkeypatch.setenv("PYSTOW_HOME", str(tmp_path))
    (tmp_path / "oaklib").mkdir()
    (tmp_path / "oaklib" / "mondo.db").write_bytes(b"")
    opened = []
    sentinel = object()

    def _get_adapter(spec, *_args, **_kwargs):
        opened.append(spec)
        return sentinel

    def _no_ols(url, timeout):  # pragma: no cover - must never run
        raise AssertionError(f"OLS was asked ({url}) although the build is present")

    monkeypatch.setattr("oaklib.get_adapter", _get_adapter)
    monkeypatch.setattr(ols, "_get_json", _no_ols)
    assert P.open_mondo_adapter(TATEYAMA) is sentinel
    assert opened == ["sqlite:obo:mondo"]


def test_cli_gives_a_verdict_through_ols(no_local_builds, ols_calls, tmp_path, capsys):
    report = tmp_path / "report.md"
    report.write_text(
        "Tateyama distal myopathy (OMIM 614321) is caused by CAV3.\n" * 5,
        encoding="utf-8",
    )
    assert main([str(report), TATEYAMA, "--no-hgnc"]) == 0
    out = capsys.readouterr().out
    assert out.startswith(PASS)
    assert "MONDO source    : OLS (" in out
    assert "canonical gene  : CAV3" in out
    assert "OMIM (MONDO)    : 614321" in out


def test_cli_json_records_the_mondo_source(
    no_local_builds, ols_calls, tmp_path, capsys
):
    report = tmp_path / "report.md"
    report.write_text("CAV3 " * 5 + "\n", encoding="utf-8")
    assert main([str(report), TATEYAMA, "--no-hgnc", "--json"]) == 0
    result = json.loads(capsys.readouterr().out)
    assert result["mondo_source"].startswith("OLS (")


def test_cli_exits_2_when_neither_the_build_nor_ols_answers(
    no_local_builds, ols_down, monkeypatch, tmp_path, capsys
):
    """No verdict, and above all no SKIP, when MONDO cannot be read at all."""

    def _no_lexicon(**_kwargs):  # pragma: no cover - must never run
        raise AssertionError("HGNC lexicon was built for a run that cannot finish")

    monkeypatch.setattr("dismech.preflight_dr.default_lexicon", _no_lexicon)
    report = tmp_path / "report.md"
    report.write_text("CAV3 CAV3 CAV3\n", encoding="utf-8")
    with pytest.raises(SystemExit) as excinfo:
        main([str(report), TATEYAMA])
    assert excinfo.value.code == 2
    captured = capsys.readouterr()
    assert SKIP not in captured.out
    assert "OLS fallback could not answer" in captured.err
    assert "connection refused" in captured.err
    assert "just fetch-ontology-dbs mondo" in captured.err


def test_fetch_mondo_record_raises_when_ols_is_down_too(no_local_builds, ols_down):
    with pytest.raises(MondoBuildUnavailable, match="OLS fallback could not answer"):
        fetch_mondo_record(TATEYAMA, use_hgnc=False)


def test_an_unknown_mondo_id_exits_2_instead_of_skipping(
    no_local_builds, ols_calls, tmp_path, capsys
):
    report = tmp_path / "report.md"
    report.write_text("CAV3\n", encoding="utf-8")
    with pytest.raises(SystemExit) as excinfo:
        main([str(report), "MONDO:9999999", "--no-hgnc"])
    assert excinfo.value.code == 2
    assert "OLS has no MONDO term MONDO:9999999" in capsys.readouterr().err


def test_the_rival_lookup_says_it_did_not_run_over_ols(ols_calls):
    """OLS cannot list a gene's diseases; that is a gap, not "no rival disease"."""
    lookup = P._default_rival_lookup(OlsMondoAdapter(), use_hgnc=False)
    found, errors = lookup(["TBK1"], TATEYAMA)
    assert found == {}
    assert len(errors) == 1 and "OLS" in errors[0]
    assert ols_calls == []


def test_a_never_named_gene_with_a_matching_omim_stays_a_warn_over_ols(
    no_local_builds, ols_calls, tmp_path, capsys
):
    """Without the reverse lookup, the shared-OMIM case cannot be raised to FAIL."""
    report = tmp_path / "report.md"
    report.write_text("OMIM 614321.\n" + "PTRF is discussed.\n" * 6, encoding="utf-8")
    assert main([str(report), TATEYAMA, "--no-hgnc"]) == 0
    out = capsys.readouterr().out
    assert out.startswith(WARN)
    assert "rival-gene disease lookup did not complete" in out


# --------------------------------------------------------------------------
# research anchors
# --------------------------------------------------------------------------


def test_research_anchors_get_omim_and_genes_via_ols(
    no_local_builds, ols_calls, tmp_path
):
    anchors = collect_anchors(
        {"name": "Distal Myopathy, Tateyama Type"}, TATEYAMA, stubs_dir=tmp_path
    )
    assert anchors.template_vars()["omim_id"] == "OMIM:614321"
    assert anchors.causal_genes == ("CAV3",)
    assert anchors.gene_source == "MONDO via OLS"
    assert "OMIM 614321 (MONDO via OLS)" in anchors.summary()


def test_research_anchors_prefer_mondo_synonyms_over_the_entry_via_ols(
    no_local_builds, ols_calls, tmp_path
):
    entry = {
        "name": "Intellectual Developmental Disorder, Autosomal Dominant 64",
        "synonyms": ["an unverified skeleton synonym"],
    }
    anchors = collect_anchors(entry, MRD64, stubs_dir=tmp_path)
    assert anchors.synonym_source == "MONDO via OLS"
    assert "ZNF292-related neurodevelopmental disorder" in anchors.synonyms
    assert "an unverified skeleton synonym" not in anchors.synonyms
    assert anchors.template_vars()["omim_id"] == "OMIM:619188"


def test_research_anchors_degrade_and_log_when_ols_is_down(
    no_local_builds, ols_down, tmp_path, capsys
):
    entry = {"name": "Foo", "synonyms": ["Foo syndrome"]}
    anchors = collect_anchors(entry, TATEYAMA, stubs_dir=tmp_path)
    assert anchors.omim_ids == ()
    assert anchors.synonyms == ("Foo syndrome",)
    assert anchors.synonym_source == "entry"
    assert "via OLS failed" in capsys.readouterr().err


def test_research_anchors_no_mondo_skips_ols_too(tmp_path, monkeypatch):
    def _no_ols(url, timeout):  # pragma: no cover - must never run
        raise AssertionError("OLS was asked under --no-mondo")

    monkeypatch.setattr(ols, "_get_json", _no_ols)
    anchors = collect_anchors(
        {"name": "Foo"}, TATEYAMA, use_local_mondo=False, stubs_dir=tmp_path
    )
    assert anchors.omim_ids == ()
    assert research_anchors.NOT_RECORDED in anchors.template_vars()["omim_id"]


def test_gene_labels_answer_either_hgnc_casing_and_nothing_else(ols_calls):
    adapter = OlsMondoAdapter()
    adapter.term(TATEYAMA)
    assert adapter.label("hgnc:1529") == "CAV3"
    assert adapter.label("NCBIGene:1529") is None


def test_a_lowercase_mondo_prefix_still_names_the_mondo_iri():
    assert entity_url("mondo:0013686") == entity_url(TATEYAMA)


# --------------------------------------------------------------------------
# Obsolete terms, and naming the MONDO source honestly
# --------------------------------------------------------------------------


def test_parse_reads_obsolescence_and_the_replacement():
    facts = parse_mondo_entity(_fixture(OBSOLETE), OBSOLETE)
    assert facts.obsolete is True
    assert facts.replaced_by == ("MONDO:0009299",)
    assert facts.genes == ()


def test_an_obsolete_term_is_named_as_such_not_only_as_geneless(
    no_local_builds, ols_calls, tmp_path, capsys
):
    report = tmp_path / "report.md"
    report.write_text("SOX9 SOX9 SOX9\n", encoding="utf-8")
    assert main([str(report), OBSOLETE, "--no-hgnc"]) == 0
    out = capsys.readouterr().out
    assert out.startswith(SKIP)  # the verdict rules are unchanged
    assert "MONDO status    : obsolete; replaced by MONDO:0009299" in out
    assert (
        f"{OBSOLETE} is obsolete in MONDO; MONDO replaced it with MONDO:0009299" in out
    )


def test_a_current_term_reports_no_obsolescence(no_local_builds, ols_calls):
    record = fetch_mondo_record(TATEYAMA, use_hgnc=False)
    assert record.obsolete is False
    assert record.replaced_by == ()


def test_an_adapter_handed_in_is_not_called_the_local_build():
    class SomeAdapter:
        def label(self, curie):
            return None

        def relationships(self, subjects=None, predicates=None, objects=None):
            return []

        def simple_mappings_by_curie(self, curie):
            return []

    record = fetch_mondo_record(TATEYAMA, adapter=SomeAdapter(), use_hgnc=False)
    assert record.source == "adapter: SomeAdapter"


def test_the_adapter_opened_on_the_local_build_is_named_as_such(monkeypatch, tmp_path):
    monkeypatch.setenv("PYSTOW_HOME", str(tmp_path))
    (tmp_path / "oaklib").mkdir()
    (tmp_path / "oaklib" / "mondo.db").write_bytes(b"")

    class LocalAdapter:
        pass

    monkeypatch.setattr("oaklib.get_adapter", lambda spec, *a, **k: LocalAdapter())
    adapter = P.open_mondo_adapter(TATEYAMA)
    assert P._mondo_source(adapter) == P.LOCAL_MONDO_SOURCE


# --------------------------------------------------------------------------
# HGNC is never downloaded either (#12687)
# --------------------------------------------------------------------------


def test_the_hgnc_lexicon_refuses_a_missing_build(no_local_builds):
    with pytest.raises(P.LexiconUnavailable, match="just fetch-ontology-dbs hgnc"):
        P.HgncLexicon().probe()
    lexicon = P.default_lexicon()
    assert lexicon.name == "heuristic"
    assert "just fetch-ontology-dbs hgnc" in lexicon.reason


def test_alias_lookup_is_skipped_without_the_hgnc_build(no_local_builds, ols_calls):
    """As --no-hgnc: no aliases, no HGNC opened, and no failed-lookup error."""
    record = fetch_mondo_record(TATEYAMA, use_hgnc=True)
    assert record.genes == ("CAV3",)
    assert record.gene_aliases == {}
    assert record.lookup_errors == ()


def test_cli_without_no_hgnc_skips_a_missing_hgnc_build_with_one_note(
    no_local_builds, ols_calls, tmp_path, capsys
):
    report = tmp_path / "report.md"
    report.write_text("CAV3 " * 5 + "\n", encoding="utf-8")
    assert main([str(report), TATEYAMA]) == 0
    captured = capsys.readouterr()
    assert captured.out.startswith(PASS)
    assert "lexicon         : heuristic" in captured.out
    notes = [line for line in captured.err.splitlines() if line.startswith("note:")]
    assert len(notes) == 1
    assert "just fetch-ontology-dbs hgnc" in notes[0]


def test_require_hgnc_still_fails_loudly_without_the_build(
    no_local_builds, ols_calls, tmp_path, capsys
):
    report = tmp_path / "report.md"
    report.write_text("CAV3\n", encoding="utf-8")
    with pytest.raises(SystemExit) as excinfo:
        main([str(report), TATEYAMA, "--require-hgnc"])
    assert excinfo.value.code == 2
    assert "just fetch-ontology-dbs hgnc" in capsys.readouterr().err
