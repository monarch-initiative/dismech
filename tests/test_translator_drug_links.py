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

import pytest
import yaml

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
    return {candidate.node_id: candidate for candidate in candidates}


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
    candidate = tdl.Candidate(node_id="CHEBI:45783", name="Imatinib", equivalent_ids=["NCIT:C62035"])
    novel = tdl.Candidate(node_id="CHEBI:1234", name="Speculatinib")

    tdl.annotate_curated([candidate, novel], {"NCIT:C62035": "imatinib"}, {})
    assert candidate.curated_as == "imatinib"
    assert candidate.status == "CURATED"
    assert novel.curated_as is None
    assert novel.status == "NEW"


def test_annotate_curated_falls_back_to_name_match():
    candidate = tdl.Candidate(node_id="CHEBI:45783", name="Imatinib")
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


DRUG = "CHEBI:45783"
GENE = "NCBIGene:25"


def _path_message() -> dict:
    """A miniature two-hop message: one on-category gene path, one off-category answer."""
    return {
        "query_graph": {"nodes": {"chem": {"ids": [DRUG]}, "mid": {}, "disease": {"ids": [DISEASE]}}},
        "knowledge_graph": {
            "nodes": {
                DRUG: {"name": "imatinib", "categories": ["biolink:ChemicalEntity"]},
                GENE: {"name": "ABL1", "categories": ["biolink:Gene"]},
                "CHEBI:8888": {"name": "bevacizumab", "categories": ["biolink:ChemicalEntity"]},
                DISEASE: {"name": "chronic myelogenous leukemia, BCR-ABL1 positive"},
            },
            "edges": {
                "hop1": {
                    "subject": DRUG,
                    "object": GENE,
                    "predicate": "biolink:physically_interacts_with",
                    "sources": [{"resource_id": "infores:dgidb", "resource_role": "primary_knowledge_source"}],
                    "attributes": [{"attribute_type_id": "biolink:publications", "value": ["PMID:11287973"]}],
                },
                "hop2": {
                    "subject": GENE,
                    "object": DISEASE,
                    "predicate": "biolink:genetically_associated_with",
                    "sources": [{"resource_id": "infores:disgenet", "resource_role": "primary_knowledge_source"}],
                    "attributes": [{"attribute_type_id": "biolink:publications", "value": ["PMID:2406902"]}],
                },
                "offcat1": {"subject": "CHEBI:8888", "object": DRUG, "predicate": "biolink:interacts_with"},
                "offcat2": {"subject": "CHEBI:8888", "object": DISEASE, "predicate": "biolink:treats"},
            },
        },
        "results": [
            {
                "node_bindings": {
                    "chem": [{"id": DRUG}],
                    "mid": [{"id": GENE}],
                    "disease": [{"id": DISEASE}],
                },
                "analyses": [
                    {"score": 0.4, "edge_bindings": {"e1": [{"id": "hop1"}], "e2": [{"id": "hop2"}]}},
                    {"score": 0.78, "edge_bindings": {"e1": [{"id": "hop1"}], "e2": [{"id": "hop2"}]}},
                ],
            },
            {
                "node_bindings": {
                    "chem": [{"id": DRUG}],
                    "mid": [{"id": "CHEBI:8888"}],
                    "disease": [{"id": DISEASE}],
                },
                "analyses": [{"score": 0.61, "edge_bindings": {"e1": [{"id": "offcat1"}], "e2": [{"id": "offcat2"}]}}],
            },
        ],
    }


def _cml_entry() -> dict:
    return {
        "name": "Chronic Myeloid Leukemia",
        "genetic": [
            {"name": "ABL1", "gene_term": {"preferred_term": "ABL1", "term": {"id": "hgnc:76", "label": "ABL1"}}}
        ],
        "pathophysiology": [
            {
                "name": "Constitutive Tyrosine Kinase Activation",
                "biological_processes": [
                    {"preferred_term": "peptidyl-tyrosine phosphorylation", "term": {"id": "GO:0018108"}}
                ],
            }
        ],
        "treatments": [
            {
                "name": "Imatinib",
                "treatment_term": {"therapeutic_agent": [{"preferred_term": "imatinib", "term": {"id": "CHEBI:45783"}}]},
                "target_mechanisms": [
                    {"target": "Constitutive Tyrosine Kinase Activation", "treatment_effect": "INHIBITS"}
                ],
            }
        ],
        "mechanistic_hypotheses": [
            {"hypothesis_group_id": "canonical_bcr_abl1_model", "hypothesis_label": "BCR-ABL1 model", "status": "CANONICAL"}
        ],
    }


def test_build_path_query_pins_both_ends():
    query = tdl.build_path_query(DISEASE, DRUG, via_categories=["biolink:Gene"])
    graph = query["message"]["query_graph"]
    assert graph["nodes"]["chem"]["ids"] == [DRUG]
    assert graph["nodes"]["disease"]["ids"] == [DISEASE]
    assert graph["nodes"]["mid"]["categories"] == ["biolink:Gene"]
    assert set(graph["edges"]) == {"e1", "e2"}
    # Predicates stay open: providers spell the drug-target relation many ways.
    assert "predicates" not in graph["edges"]["e1"]


def test_extract_paths_groups_by_intermediate_and_keeps_best_score():
    paths = tdl.extract_paths(_path_message(), via_categories=["biolink:Gene"])
    assert [path.node_id for path in paths] == [GENE]
    path = paths[0]
    assert path.score == 0.78
    assert path.render() == (
        "imatinib --physically_interacts_with--> ABL1 | ABL1 --genetically_associated_with--> "
        "chronic myelogenous leukemia, BCR-ABL1 positive"
    )
    assert path.publications == ["PMID:11287973", "PMID:2406902"]
    assert path.sources == {"dgidb", "disgenet"}


def test_extract_paths_drops_off_category_intermediates():
    """An ARA answering a Gene slot with a biologic must not be reported as a gene path."""
    unfiltered = tdl.extract_paths(_path_message())
    assert {path.node_id for path in unfiltered} == {GENE, "CHEBI:8888"}
    filtered = tdl.extract_paths(_path_message(), via_categories=["biolink:Gene"])
    assert {path.node_id for path in filtered} == {GENE}


def test_curated_mechanism_index_covers_genes_and_pathophysiology():
    by_curie, by_name = tdl.curated_mechanism_index(_cml_entry())
    assert by_curie["hgnc:76"] == "genetic: ABL1"
    assert by_curie["GO:0018108"] == "pathophysiology: Constitutive Tyrosine Kinase Activation"
    assert by_name["abl1"] == "genetic: ABL1"


def test_annotate_paths_matches_hgnc_case_insensitively():
    """dismech writes `hgnc:76`; the SRI normalizer returns `HGNC:76`."""
    path = tdl.PathCandidate(node_id=GENE, name="ABL1", equivalent_ids=["HGNC:76", "UniProtKB:P00519"])
    novel = tdl.PathCandidate(node_id="NCBIGene:9429", name="ABCG2", equivalent_ids=["HGNC:74"])

    tdl.annotate_paths([path, novel], *tdl.curated_mechanism_index(_cml_entry()))
    assert path.curated_as == "genetic: ABL1"
    assert path.status == "IN ENTRY"
    assert novel.curated_as is None
    assert novel.status == "NEW"


def test_drug_target_mechanisms_reports_declared_targets():
    assert tdl.drug_target_mechanisms(_cml_entry(), "imatinib") == [
        "Constitutive Tyrosine Kinase Activation (INHIBITS)"
    ]
    assert tdl.drug_target_mechanisms(_cml_entry(), "dasatinib") == []


def test_render_paths_markdown_shows_the_path_and_the_warning():
    paths = tdl.extract_paths(_path_message(), via_categories=["biolink:Gene"])
    tdl.annotate_paths(paths, *tdl.curated_mechanism_index(_cml_entry()))
    rendered = tdl.render_paths_markdown(
        paths,
        drug_curie=DRUG,
        drug_label="imatinib",
        disease_curie=DISEASE,
        disease_label="chronic myeloid leukemia",
        via="gene",
        pk="test-pk",
        ui_url="https://ui.transltr.io/main/results?q=test-pk",
        complete=True,
        entry_path="kb/disorders/Chronic_Myeloid_Leukemia.yaml",
        curated_drug="imatinib",
        curated_targets=["Constitutive Tyrosine Kinase Activation (INHIBITS)"],
        generated_at="2026-08-02T00:00:00Z",
    )
    assert "machine-generated leads" in rendered
    assert "--physically_interacts_with--> ABL1" in rendered
    assert "genetic: ABL1" in rendered
    assert "Constitutive Tyrosine Kinase Activation (INHIBITS)" in rendered


def test_find_hypothesis_matches_and_lists_alternatives_on_a_miss():
    entry = _cml_entry()
    assert tdl.find_hypothesis(entry, "canonical_bcr_abl1_model")["status"] == "CANONICAL"
    with pytest.raises(SystemExit) as error:
        tdl.find_hypothesis(entry, "no_such_model")
    assert "canonical_bcr_abl1_model" in str(error.value)


def test_hypothesis_report_paths_follow_the_provider_convention():
    report, citations = tdl.hypothesis_report_paths(
        Path("kb/hypotheses"), "Chronic_Myeloid_Leukemia", "canonical_bcr_abl1_model"
    )
    assert report == Path("kb/hypotheses/Chronic_Myeloid_Leukemia/canonical_bcr_abl1_model/translator.md")
    assert citations == report.with_name("translator.md.citations.md")


def test_write_hypothesis_report_emits_frontmatter_and_citations(tmp_path):
    entry = _cml_entry()
    hypothesis = entry["mechanistic_hypotheses"][0]
    report, citations = tdl.hypothesis_report_paths(tmp_path, "Chronic_Myeloid_Leukemia", "canonical_bcr_abl1_model")
    frontmatter = tdl.build_hypothesis_frontmatter(
        hypothesis=hypothesis,
        disease_name="Chronic Myeloid Leukemia",
        query=tdl.build_path_query(DISEASE, DRUG),
        ars_url="https://ars-prod.transltr.io",
        pk="test-pk",
        merged_pk="merged-pk",
        citation_count=2,
        started_at="2026-08-02T00:00:00+00:00",
        ended_at="2026-08-02T00:04:00+00:00",
        duration_seconds=240.0,
    )
    tdl.write_hypothesis_report(
        report,
        citations,
        frontmatter=frontmatter,
        body="# body\n",
        references=["PMID:11287973", "PMID:2406902"],
        query_description="two-hop lookup",
    )

    text = report.read_text()
    assert text.startswith("---\nprovider: translator\n")
    parsed = yaml.safe_load(text.split("---")[1])
    assert parsed["citation_count"] == 2
    assert parsed["provider_config"]["ars_pk"] == "test-pk"
    assert parsed["template_variables"]["hypothesis_status"] == "CANONICAL"
    assert "# body" in text
    assert "1. PMID:11287973" in citations.read_text()


def test_build_pathfinder_query_uses_the_paths_element():
    """The QPath spec: constraints carry intermediate_categories; predicates are a hint."""
    query = tdl.build_pathfinder_query(DRUG, DISEASE, intermediate_categories=["biolink:Gene"])
    graph = query["message"]["query_graph"]
    assert "edges" not in graph
    path = graph["paths"]["p0"]
    assert (path["subject"], path["object"]) == ("n0", "n1")
    assert path["constraints"] == [{"intermediate_categories": ["biolink:Gene"]}]
    assert graph["nodes"]["n0"]["ids"] == [DRUG]


def test_build_pathfinder_query_omits_unconstrained_intermediates():
    path = tdl.build_pathfinder_query(DRUG, DISEASE)["message"]["query_graph"]["paths"]["p0"]
    assert "constraints" not in path


def test_build_regulation_query_puts_direction_on_the_qualifier_set():
    query = tdl.build_regulation_query(gene_curie=GENE, direction="decreased")
    graph = query["message"]["query_graph"]
    edge = graph["edges"]["e"]
    assert graph["nodes"]["gene"]["ids"] == [GENE]
    assert "ids" not in graph["nodes"]["chem"]  # the chemical is the answer
    assert edge["predicates"] == ["biolink:affects"]  # direction is NOT in the predicate
    qualifiers = {q["qualifier_type_id"]: q["qualifier_value"] for q in edge["qualifier_constraints"][0]["qualifier_set"]}
    assert qualifiers["biolink:object_direction_qualifier"] == "decreased"
    assert qualifiers["biolink:object_aspect_qualifier"] == "activity_or_abundance"


def test_build_regulation_query_can_pin_either_end():
    inverse = tdl.build_regulation_query(chemical_curie=DRUG, direction="increased")
    nodes = inverse["message"]["query_graph"]["nodes"]
    assert nodes["chem"]["ids"] == [DRUG]
    assert "ids" not in nodes["gene"]  # the gene is the answer
    with pytest.raises(ValueError):
        tdl.build_regulation_query()


def test_extract_candidates_can_answer_a_non_disease_template():
    """The regulation templates bind chem/gene, not chem/disease."""
    message = {
        "knowledge_graph": {
            "nodes": {DRUG: {"name": "imatinib"}, GENE: {"name": "ABL1"}},
            "edges": {
                "e1": {
                    "subject": DRUG,
                    "object": GENE,
                    "predicate": "biolink:affects",
                    "sources": [{"resource_id": "infores:ctd", "resource_role": "primary_knowledge_source"}],
                    "attributes": [{"attribute_type_id": "biolink:knowledge_level", "value": "knowledge_assertion"}],
                }
            },
        },
        "results": [
            {
                "node_bindings": {"chem": [{"id": DRUG}], "gene": [{"id": GENE}]},
                "analyses": [{"score": 1.0, "edge_bindings": {"e": [{"id": "e1"}]}}],
            }
        ],
    }
    candidates = tdl.extract_candidates(message, answer_key="chem", pinned_key="gene")
    assert [c.node_id for c in candidates] == [DRUG]
    assert candidates[0].asserted is True


def _pathfinder_message() -> dict:
    """Pathfinder returns each route as an unordered bag of edges in an aux graph."""
    return {
        "knowledge_graph": {
            "nodes": {
                DRUG: {"name": "Imatinib", "categories": ["biolink:ChemicalEntity"]},
                "NCBIGene:2263": {"name": "SIN3A", "categories": ["biolink:Gene"]},
                "NCBIGene:613": {"name": "BCR", "categories": ["biolink:Gene"]},
                "CHEBI:31941": {"name": "Oxaliplatin", "categories": ["biolink:ChemicalEntity"]},
                DISEASE: {"name": "CML", "categories": ["biolink:Disease"]},
            },
            "edges": {
                # Deliberately out of order, and the middle hop runs backwards.
                "b": {"subject": "NCBIGene:613", "object": "NCBIGene:2263", "predicate": "biolink:interacts_with"},
                "c": {"subject": "NCBIGene:613", "object": DISEASE, "predicate": "biolink:affects"},
                "a": {"subject": DRUG, "object": "NCBIGene:2263", "predicate": "biolink:affects"},
                "x": {"subject": DRUG, "object": "CHEBI:31941", "predicate": "biolink:interacts_with"},
                "y": {"subject": "CHEBI:31941", "object": DISEASE, "predicate": "biolink:contributes_to"},
            },
        },
        "auxiliary_graphs": {"a_1": {"edges": ["b", "c", "a"]}, "a_2": {"edges": ["x", "y"]}},
        "results": [
            {
                "node_bindings": {"n0": [{"id": DRUG}], "n1": [{"id": DISEASE}]},
                "analyses": [
                    {"score": 0.74, "path_bindings": {"p0": [{"id": "a_1"}]}},
                    {"score": 0.69, "path_bindings": {"p0": [{"id": "a_2"}]}},
                ],
            }
        ],
    }


def test_order_path_edges_walks_an_unordered_bag_into_a_chain():
    message = _pathfinder_message()
    edges = message["knowledge_graph"]["edges"]
    chain = tdl.order_path_edges(["b", "c", "a"], edges, DRUG, DISEASE)
    assert chain == [("a", True), ("b", False), ("c", True)]  # middle hop traversed backwards


def test_order_path_edges_returns_nothing_when_the_bag_is_disconnected():
    edges = _pathfinder_message()["knowledge_graph"]["edges"]
    assert tdl.order_path_edges(["b"], edges, DRUG, DISEASE) == []


def test_extract_pathfinder_paths_renders_ordered_chains():
    # The 0.69 route hops through another drug and is dropped by default.
    paths = tdl.extract_pathfinder_paths(_pathfinder_message(), start=DRUG, end=DISEASE)
    assert [path.score for path in paths] == [0.74]
    # The middle hop is walked backwards, so it points back rather than being flipped.
    assert paths[0].render() == (
        "Imatinib --affects--> SIN3A | SIN3A <--interacts_with-- BCR | BCR --affects--> CML"
    )
    assert paths[0].intermediates == ["NCBIGene:2263", "NCBIGene:613"]
    assert paths[0].name == "SIN3A > BCR"


def test_extract_pathfinder_paths_drops_co_target_routes_by_default():
    """A route whose intermediate is another drug is a co-target artifact, not mechanism."""
    assert [path.name for path in tdl.extract_pathfinder_paths(_pathfinder_message(), start=DRUG, end=DISEASE)] == [
        "SIN3A > BCR"
    ]
    kept = tdl.extract_pathfinder_paths(
        _pathfinder_message(), start=DRUG, end=DISEASE, include_chemical_intermediates=True
    )
    assert [path.name for path in kept] == ["SIN3A > BCR", "Oxaliplatin"]


def test_chemical_intermediates_are_caught_without_an_explicit_chemicalentity_category():
    """Node categories are often partial: a drug may only carry biolink:MolecularEntity."""
    message = _pathfinder_message()
    message["knowledge_graph"]["nodes"]["CHEBI:31941"]["categories"] = ["biolink:MolecularEntity"]
    assert [path.name for path in tdl.extract_pathfinder_paths(message, start=DRUG, end=DISEASE)] == ["SIN3A > BCR"]


def test_annotate_paths_matches_any_intermediate_on_a_multi_hop_route():
    paths = tdl.extract_pathfinder_paths(_pathfinder_message(), start=DRUG, end=DISEASE)
    entry = {"genetic": [{"name": "BCR", "gene_term": {"term": {"id": "hgnc:1014", "label": "BCR"}}}]}
    tdl.annotate_paths(paths, *tdl.curated_mechanism_index(entry))
    assert paths[0].curated_as == "genetic: BCR"  # matched on the second intermediate


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
