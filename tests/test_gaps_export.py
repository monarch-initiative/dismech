"""Tests for the knowledge-gap browser data exporter."""

from dismech.export.gaps_export import KnowledgeGapExporter, _node_label


def test_node_label_strips_kind_and_file_scope():
    assert _node_label("pathophysiology#Amyloid Plaque Formation") == "Amyloid Plaque Formation"
    assert _node_label("Liver_Cirrhosis:pathophysiology#Stellate Activation") == "Stellate Activation"
    assert _node_label("bare reference") == "bare reference"


def test_extract_gaps_filters_to_gap_kinds():
    entry = {
        "name": "Test Disorder",
        "category": "Mendelian",
        "parents": ["Genetic Disease"],
        "creation_date": "2025-01-01T00:00:00Z",
        "disease_term": {"term": {"id": "MONDO:0000001"}},
        "discussions": [
            {
                "discussion_id": "gap_one",
                "prompt": "Open question about X?",
                "kind": "KNOWLEDGE_GAP",
                "status": "OPEN",
                "attaches_to": ["pathophysiology#Node A", "phenotype#Pheno B"],
                "rationale": "Why it matters.",
                "proposed_experiments": [{"name": "Experiment 1"}],
                "evidence": [{"reference": "PMID:123"}],
            },
            {
                "discussion_id": "mismatch_one",
                "prompt": "Does the mouse model recapitulate?",
                "kind": "HUMAN_MODEL_MISMATCH",
                "status": "OPEN",
            },
            {
                "discussion_id": "controversy_one",
                "prompt": "A live disagreement.",
                "kind": "CONTROVERSY",
            },
        ],
    }

    exporter = KnowledgeGapExporter()
    records = exporter.extract_gaps(
        entry,
        source_type="Disorder",
        source_file="kb/disorders/Test.yaml",
        page_url="../../pages/disorders/Test_Disorder.html",
    )

    # Only the KNOWLEDGE_GAP and HUMAN_MODEL_MISMATCH discussions are kept.
    assert {r["gap_id"] for r in records} == {"gap_one", "mismatch_one"}

    gap = next(r for r in records if r["gap_id"] == "gap_one")
    assert gap["source_type"] == "Disorder"
    assert gap["source_name"] == "Test Disorder"
    assert gap["disease_id"] == "MONDO:0000001"
    assert gap["kind"] == "KNOWLEDGE GAP"
    assert gap["attached_nodes"] == ["Node A", "Pheno B"]
    assert gap["num_experiments"] == 1
    assert gap["experiment_names"] == ["Experiment 1"]
    assert gap["num_evidence"] == 1
    assert gap["has_experiments"] == "With proposed experiments"
    # Back-link page_url carries the deep-link anchor to the discussion.
    assert gap["page_url"] == "../../pages/disorders/Test_Disorder.html#gap_one"


def test_extract_gaps_module_has_no_disease_facets():
    entry = {
        "name": "fibrotic_response",
        "parents": ["ignored for modules"],
        "discussions": [
            {
                "discussion_id": "mod_gap",
                "prompt": "Module-level gap?",
                "kind": "KNOWLEDGE_GAP",
            }
        ],
    }
    records = KnowledgeGapExporter().extract_gaps(
        entry,
        source_type="Module",
        source_file="kb/modules/fibrotic_response.yaml",
        page_url="../../pages/modules/fibrotic_response.html",
    )
    assert len(records) == 1
    assert records[0]["parents"] == []
    assert records[0]["category"] == ""
    assert records[0]["has_experiments"] == "No proposed experiments"


def test_summary_metrics():
    records = [
        {"source_name": "A", "kind": "KNOWLEDGE GAP", "num_experiments": 1},
        {"source_name": "A", "kind": "HUMAN MODEL MISMATCH", "num_experiments": 0},
        {"source_name": "B", "kind": "KNOWLEDGE GAP", "num_experiments": 2},
    ]
    metrics = KnowledgeGapExporter.build_summary_metrics(records)
    assert metrics["total_gaps"] == 3
    assert metrics["total_source_entries"] == 2
    assert metrics["total_with_experiments"] == 2
    assert metrics["total_gap_kinds"] == 2
