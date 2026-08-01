"""Tests for the Translator disease-drug lead explorer (``scripts/translator_drug_links.py``).

The script talks to the NCATS Biomedical Translator ARS, so the network layer
is deliberately thin and untested here. What is pinned instead is the pure
core that decides *what a curator sees*:

  * only chemical->disease edges contribute provenance (mechanism-path edges
    reached through a support graph describe how a prediction was made, not
    whether the drug treats the disease);
  * ``prediction``-only answers are never labelled as asserted knowledge;
  * answers that normalize to the same chemical collapse into one row;
  * a drug already curated in the entry is reported as CURATED, not as a gap.

Those four properties are what make the output safe to hand to a curator as
leads rather than as evidence.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
SCRIPT_PATH = ROOT / "scripts" / "translator_drug_links.py"
SPEC = importlib.util.spec_from_file_location("translator_drug_links", SCRIPT_PATH)
assert SPEC and SPEC.loader
tdl = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = tdl
SPEC.loader.exec_module(tdl)


DISEASE = "MONDO:0011996"


def _message() -> dict:
    """A miniature TRAPI message: one asserted answer, one prediction-only answer."""
    return {
        "knowledge_graph": {
            "nodes": {
                "CHEBI:45783": {"name": "imatinib"},
                "CHEBI:9999": {"name": "imatinib mesylate"},
                "CHEBI:1234": {"name": "speculatinib"},
                "NCBIGene:25": {"name": "ABL1"},
                DISEASE: {"name": "chronic myelogenous leukemia, BCR-ABL1 positive"},
            },
            "edges": {
                "direct-asserted": {
                    "subject": "CHEBI:45783",
                    "object": DISEASE,
                    "predicate": "biolink:treats",
                    "sources": [
                        {"resource_id": "infores:drugcentral", "resource_role": "primary_knowledge_source"},
                        {"resource_id": "infores:arax", "resource_role": "aggregator_knowledge_source"},
                    ],
                    "attributes": [
                        {"attribute_type_id": "biolink:knowledge_level", "value": "knowledge_assertion"},
                        {"attribute_type_id": "biolink:publications", "value": ["PMID:11287973"]},
                        {"attribute_type_id": "biolink:supporting_study", "value": "NCT00006343"},
                        {
                            "attribute_type_id": "biolink:clinical_approval_status",
                            "value": "biolink:approved_for_condition",
                        },
                        {"attribute_type_id": "biolink:max_research_phase", "value": 4.0},
                    ],
                },
                # Salt form of the same drug, reported as a separate answer.
                "direct-salt": {
                    "subject": "CHEBI:9999",
                    "object": DISEASE,
                    "predicate": "biolink:treats",
                    "sources": [
                        {"resource_id": "infores:ctd", "resource_role": "primary_knowledge_source"},
                    ],
                    "attributes": [
                        {"attribute_type_id": "biolink:knowledge_level", "value": "knowledge_assertion"},
                        {"attribute_type_id": "biolink:publications", "value": ["PMID:12393516"]},
                    ],
                },
                # Mechanism-path edge: must NOT contribute publications.
                "indirect": {
                    "subject": "CHEBI:45783",
                    "object": "NCBIGene:25",
                    "predicate": "biolink:affects",
                    "sources": [{"resource_id": "infores:dgidb", "resource_role": "primary_knowledge_source"}],
                    "attributes": [
                        {"attribute_type_id": "biolink:publications", "value": ["PMID:99999999"]},
                    ],
                },
                "direct-predicted": {
                    "subject": "CHEBI:1234",
                    "object": DISEASE,
                    "predicate": "biolink:treats",
                    "sources": [{"resource_id": "infores:openpredict", "resource_role": "primary_knowledge_source"}],
                    "attributes": [
                        {"attribute_type_id": "biolink:knowledge_level", "value": "prediction"},
                    ],
                },
            },
        },
        "results": [
            {
                "node_bindings": {"disease": [{"id": DISEASE}], "chem": [{"id": "CHEBI:45783"}]},
                "analyses": [
                    {"score": 0.8, "edge_bindings": {"e": [{"id": "direct-asserted"}, {"id": "indirect"}]}},
                    {"score": 0.95, "edge_bindings": {"e": [{"id": "direct-asserted"}]}},
                ],
            },
            {
                "node_bindings": {"disease": [{"id": DISEASE}], "chem": [{"id": "CHEBI:9999"}]},
                "analyses": [{"score": 0.7, "edge_bindings": {"e": [{"id": "direct-salt"}]}}],
            },
            {
                "node_bindings": {"disease": [{"id": DISEASE}], "chem": [{"id": "CHEBI:1234"}]},
                "analyses": [{"score": 0.4, "edge_bindings": {"e": [{"id": "direct-predicted"}]}}],
            },
        ],
    }


def _by_id(candidates):
    return {candidate.chem_id: candidate for candidate in candidates}


def test_build_query_requests_creative_mode():
    query = tdl.build_query(DISEASE)
    edge = query["message"]["query_graph"]["edges"]["e"]
    assert query["message"]["query_graph"]["nodes"]["disease"]["ids"] == [DISEASE]
    assert edge["predicates"] == ["biolink:treats"]
    assert edge["knowledge_type"] == "inferred"
    assert edge["subject"] == "chem" and edge["object"] == "disease"


def test_build_query_can_disable_creative_mode():
    edge = tdl.build_query(DISEASE, inferred=False)["message"]["query_graph"]["edges"]["e"]
    assert "knowledge_type" not in edge


def test_extract_candidates_keeps_best_score_and_direct_provenance():
    candidates = _by_id(tdl.extract_candidates(_message()))
    imatinib = candidates["CHEBI:45783"]

    assert imatinib.name == "imatinib"
    assert imatinib.score == 0.95  # best analysis wins
    assert imatinib.publications == ["PMID:11287973"]  # the mechanism-path PMID is excluded
    assert imatinib.trials == ["NCT00006343"]
    assert imatinib.approval_status == "approved_for_condition"
    assert imatinib.max_research_phase == 4.0
    assert imatinib.sources == {"drugcentral"}  # aggregators are not primary sources
    assert imatinib.asserted is True


def test_extract_candidates_marks_prediction_only_answers():
    candidates = _by_id(tdl.extract_candidates(_message()))
    speculative = candidates["CHEBI:1234"]

    assert speculative.knowledge_levels == {"prediction"}
    assert speculative.asserted is False
    assert speculative.publications == []


def test_merge_equivalents_collapses_salt_and_base_forms():
    candidates = tdl.extract_candidates(_message())
    normalized = {
        "CHEBI:45783": {
            "id": "CHEBI:45783",
            "label": "Imatinib",
            "equivalents": ["CHEBI:45783", "NCIT:C62035"],
        },
        "CHEBI:9999": {
            "id": "CHEBI:45783",
            "label": "Imatinib",
            "equivalents": ["CHEBI:45783", "NCIT:C62035"],
        },
        "CHEBI:1234": {"id": "CHEBI:1234", "label": "Speculatinib", "equivalents": ["CHEBI:1234"]},
    }

    merged = _by_id(tdl.merge_equivalents(candidates, normalized))
    assert set(merged) == {"CHEBI:45783", "CHEBI:1234"}
    imatinib = merged["CHEBI:45783"]
    assert imatinib.name == "Imatinib"
    assert imatinib.score == 0.95
    assert imatinib.publications == ["PMID:11287973", "PMID:12393516"]
    assert imatinib.sources == {"drugcentral", "ctd"}


def test_merge_equivalents_survives_an_unavailable_normalizer():
    candidates = tdl.extract_candidates(_message())
    merged = tdl.merge_equivalents(candidates, {})
    assert len(merged) == 3  # nothing collapsed, nothing lost


def test_curated_agents_reads_curies_and_names():
    disease = {
        "treatments": [
            {
                "name": "Imatinib",
                "treatment_term": {
                    "term": {"id": "NCIT:C15986"},
                    "therapeutic_agent": [
                        {"preferred_term": "imatinib", "term": {"id": "NCIT:C62035"}},
                    ],
                },
            },
            {"name": "Allogeneic Stem Cell Transplantation"},
        ]
    }
    by_curie, by_name = tdl.curated_agents(disease)
    assert by_curie["NCIT:C62035"] == "imatinib"
    assert by_name["imatinib"] == "Imatinib"  # the treatment's display name wins over the agent label
    assert by_name["allogeneic stem cell transplantation"] == "Allogeneic Stem Cell Transplantation"


def test_annotate_curated_matches_through_equivalent_identifiers():
    candidate = tdl.Candidate(chem_id="CHEBI:45783", name="Imatinib", equivalent_ids=["NCIT:C62035"])
    novel = tdl.Candidate(chem_id="CHEBI:1234", name="Speculatinib")

    tdl.annotate_curated([candidate, novel], {"NCIT:C62035": "imatinib"}, {})
    assert candidate.curated_as == "imatinib"
    assert candidate.status == "CURATED"
    assert novel.curated_as is None
    assert novel.status == "NEW"


def test_annotate_curated_falls_back_to_name_match():
    candidate = tdl.Candidate(chem_id="CHEBI:45783", name="Imatinib")
    tdl.annotate_curated([candidate], {}, {"imatinib": "Imatinib"})
    assert candidate.curated_as == "Imatinib"


def test_normalize_publication_handles_the_shapes_translator_emits():
    assert tdl.normalize_publication("PMID:11287973") == "PMID:11287973"
    assert tdl.normalize_publication("http://www.ncbi.nlm.nih.gov/pubmed/11287973") == "PMID:11287973"
    assert tdl.normalize_publication("NCT00006343") == "NCT00006343"
    assert tdl.normalize_publication("https://doi.org/10.1056/NEJM200104053441401") == "doi:10.1056/NEJM200104053441401"
    assert tdl.normalize_publication("some free text") is None
    assert tdl.normalize_publication(None) is None


def test_render_markdown_carries_the_leads_not_evidence_warning():
    candidates = tdl.merge_equivalents(tdl.extract_candidates(_message()), {})
    rendered = tdl.render_markdown(
        candidates,
        disease_curie=DISEASE,
        disease_label="chronic myeloid leukemia",
        pk="test-pk",
        ui_url="https://ui.transltr.io/main/results?q=test-pk",
        complete=True,
        entry_path="kb/disorders/Chronic_Myeloid_Leukemia.yaml",
        generated_at="2026-08-01T00:00:00Z",
    )
    assert "lead, not evidence" in rendered
    assert "just fetch-reference PMID:11287973" in rendered
    assert "test-pk" in rendered


class _StubARS:
    """Minimal ARS stand-in: replays a fixed sequence of trace payloads."""

    def __init__(self, traces):
        self.traces = list(traces)
        self.calls = 0

    def trace(self, pk):  # noqa: ARG002 - signature mirrors ARSClient
        self.calls += 1
        return self.traces[min(self.calls - 1, len(self.traces) - 1)]


def _trace(status, *, merged=None, children=()):
    return {
        "status": status,
        "merged_version": merged,
        "children": [
            {"actor": {"agent": agent}, "status": child_status, "result_count": count}
            for agent, child_status, count in children
        ],
    }


def test_poll_returns_complete_when_the_run_finishes():
    stub = _StubARS([_trace("Done", merged="merged-pk", children=[("ara-arax", "Done", 12)])])
    merged_pk, complete = tdl.poll_for_merged(stub, "pk", timeout_seconds=30, poll_seconds=0, verbose=False)
    assert (merged_pk, complete) == ("merged-pk", True)


def test_poll_gives_up_on_a_stalled_straggler():
    """One ARA stuck in Running must not block a report the merged set can already support."""
    stalled = _trace(
        "Running",
        merged="merged-pk",
        children=[("ara-arax", "Done", 12), ("ara-aragorn", "Running", None)],
    )
    stub = _StubARS([stalled])
    merged_pk, complete = tdl.poll_for_merged(
        stub, "pk", timeout_seconds=60, poll_seconds=0, stall_seconds=1, verbose=False
    )
    assert merged_pk == "merged-pk"
    assert complete is False  # report is marked partial
    assert tdl.pending_agents(stalled) == ["ara-aragorn"]


def test_trace_signature_changes_when_an_agent_reports_progress():
    before = _trace("Running", children=[("ara-arax", "Running", None)])
    after = _trace("Running", children=[("ara-arax", "Done", 12)])
    assert tdl.trace_signature(before) != tdl.trace_signature(after)
    assert tdl.trace_signature(before) == tdl.trace_signature(dict(before))


def test_render_tsv_is_machine_readable():
    candidates = tdl.merge_equivalents(tdl.extract_candidates(_message()), {})
    rows = tdl.render_tsv(candidates).strip().split("\n")
    assert rows[0].split("\t")[:4] == ["rank", "status", "drug", "curie"]
    assert len(rows) == len(candidates) + 1
