"""Tests for the SEPIO evidence/provenance exporter."""

import json

import pytest

from dismech.export.sepio_export import (
    DataItem,
    Document,
    EvidenceLine,
    Statement,
    dump_statement,
    evidence_item_to_line,
    evidence_to_lines,
    pathophysiology_node_id,
    pathophysiology_statement_id,
    pathophysiology_statements,
    statement_from_association,
    write_jsonl,
)

# The Cystic Fibrosis "CFTR Dysfunction" evidence from kb/disorders/Cystic_Fibrosis.yaml,
# which is the worked example the SEPIO profile was designed against.
CFTR_EVIDENCE = [
    {
        "reference": "PMID:9922375",
        "reference_title": "Structure and function of the CFTR chloride channel.",
        "supports": "SUPPORT",
        "evidence_source": "HUMAN_CLINICAL",
        "snippet": (
            "The cystic fibrosis transmembrane conductance regulator (CFTR) is a unique "
            "member of the ABC transporter family that forms a novel Cl- channel."
        ),
        "explanation": (
            "Comprehensive review establishes CFTR as chloride channel whose dysfunction "
            "causes cystic fibrosis."
        ),
    },
    {
        "reference": "PMID:9922375",
        "reference_title": "Structure and function of the CFTR chloride channel.",
        "supports": "SUPPORT",
        "evidence_source": "HUMAN_CLINICAL",
        "snippet": "The CFTR is composed of five domains",
        "explanation": "Describes the five-domain architecture of CFTR.",
    },
]

CFTR_RECORD = {
    "name": "Cystic Fibrosis",
    "disease_term": {"term": {"id": "MONDO:0009061", "label": "cystic fibrosis"}},
    "pathophysiology": [
        {
            "name": "CFTR Dysfunction",
            "evidence": CFTR_EVIDENCE,
            "downstream": [
                {
                    "target": "Airway Surface Liquid Depletion",
                    "causal_link_type": "DIRECT",
                    "evidence": [
                        {
                            "reference": "PMID:23878362",
                            "supports": "SUPPORT",
                            "evidence_source": "HUMAN_CLINICAL",
                            "snippet": "CF lungs are characterized by viscous, dehydrated mucus",
                            "explanation": "Links CFTR loss to airway dehydration.",
                        }
                    ],
                }
            ],
        }
    ],
}


class TestEvidenceItemToLine:
    """Tests for the dismech EvidenceItem -> SEPIO EvidenceLine mapping."""

    def test_full_evidence_item(self):
        """Every dismech evidence field lands on the expected SEPIO slot."""
        line = evidence_item_to_line(CFTR_EVIDENCE[0], "urn:uuid:statement", 0)
        assert isinstance(line, EvidenceLine)
        assert line.type == "EvidenceLine"
        assert line.evidence_type == "HUMAN_CLINICAL"
        assert line.direction_of_evidence_provided == "SUPPORT"
        assert line.description == CFTR_EVIDENCE[0]["explanation"]

        assert len(line.has_evidence_items) == 1
        item = line.has_evidence_items[0]
        assert isinstance(item, DataItem)
        assert item.data_type == "TextSpan"
        assert item.value == CFTR_EVIDENCE[0]["snippet"]

        document = item.reported_in
        assert isinstance(document, Document)
        assert document.id == "PMID:9922375"
        assert document.title == "Structure and function of the CFTR chloride channel."
        assert document.document_type == "PRIMARY_LITERATURE"

    @pytest.mark.parametrize(
        ("reference", "expected"),
        [
            ("PMID:9922375", "PRIMARY_LITERATURE"),
            ("DOI:10.1038/nature12373", "PRIMARY_LITERATURE"),
            ("PPR:PPR123456", "PREPRINT"),
            ("clinicaltrials:NCT05813288", "CLINICAL_TRIAL_RECORD"),
            ("ORPHA:558", "DATABASE_RECORD"),
            ("CGGV:assertion_7f53", "DATABASE_RECORD"),
            ("GEO:GSE12345", "DATASET_RECORD"),
            ("url:https://example.org", "WEB_PAGE"),
        ],
    )
    def test_document_type_inferred_from_prefix(self, reference, expected):
        """dismech has no document-type field, so it is inferred from the CURIE prefix."""
        line = evidence_item_to_line({"reference": reference, "snippet": "text"}, "s", 0)
        assert line.has_evidence_items[0].reported_in.document_type == expected

    def test_unknown_prefix_omits_document_type(self):
        """An unrecognized prefix leaves document_type unset rather than guessing."""
        line = evidence_item_to_line({"reference": "widget:1", "snippet": "text"}, "s", 0)
        assert line.has_evidence_items[0].reported_in.document_type is None

    @pytest.mark.parametrize(
        ("supports", "expected"),
        [
            ("SUPPORT", "SUPPORT"),
            ("PARTIAL", "PARTIAL"),
            ("REFUTE", "REFUTE"),
            ("WRONG_STATEMENT", "REFUTE"),
            ("NO_EVIDENCE", "NEUTRAL"),
        ],
    )
    def test_supports_maps_to_direction(self, supports, expected):
        """EvidenceItemSupportEnum casts onto direction_of_evidence_provided."""
        line = evidence_item_to_line(
            {"reference": "PMID:1", "snippet": "t", "supports": supports}, "s", 0
        )
        assert line.direction_of_evidence_provided == expected

    def test_raw_supports_survives_the_lossy_direction_mapping(self):
        """WRONG_STATEMENT and REFUTE share a direction, so the raw value round-trips."""
        wrong = evidence_item_to_line(
            {"reference": "PMID:1", "snippet": "t", "supports": "WRONG_STATEMENT"}, "s", 0
        )
        refute = evidence_item_to_line(
            {"reference": "PMID:1", "snippet": "t", "supports": "REFUTE"}, "s", 0
        )
        assert wrong.direction_of_evidence_provided == refute.direction_of_evidence_provided
        assert wrong.dismech_supports == "WRONG_STATEMENT"
        assert refute.dismech_supports == "REFUTE"

    def test_raw_supports_absent_when_unset(self):
        """An item with no `supports` gets neither a direction nor a raw value."""
        line = evidence_item_to_line({"reference": "PMID:1", "snippet": "t"}, "s", 0)
        assert line.direction_of_evidence_provided is None
        assert line.dismech_supports is None

    def test_reference_only_item_still_yields_a_data_item(self):
        """A citation with no quoted span is still evidence, just an untyped one."""
        line = evidence_item_to_line({"reference": "PMID:1"}, "s", 0)
        item = line.has_evidence_items[0]
        assert item.value is None
        assert item.data_type is None
        assert item.reported_in.id == "PMID:1"

    def test_snippet_only_item_has_no_document(self):
        """A quoted span with no reference has nowhere to point `reported_in`."""
        line = evidence_item_to_line({"snippet": "unattributed text"}, "s", 0)
        item = line.has_evidence_items[0]
        assert item.value == "unattributed text"
        assert item.reported_in is None

    def test_empty_evidence_item_dropped(self):
        """An item with neither reference nor snippet carries no evidence."""
        assert evidence_item_to_line({}, "s", 0) is None
        assert evidence_item_to_line({"explanation": "just a note"}, "s", 0) is None

    def test_non_dict_evidence_item_dropped(self):
        """Malformed YAML must not crash the export."""
        assert evidence_item_to_line("PMID:1", "s", 0) is None

    def test_data_item_id_is_stable_for_same_span(self):
        """A text span's identity is its document plus its exact text."""
        first = evidence_item_to_line(CFTR_EVIDENCE[0], "statement-a", 0)
        second = evidence_item_to_line(CFTR_EVIDENCE[0], "statement-b", 3)
        assert first.has_evidence_items[0].id == second.has_evidence_items[0].id
        # ...but distinct spans from the same paper are distinct data items.
        other = evidence_item_to_line(CFTR_EVIDENCE[1], "statement-a", 1)
        assert other.has_evidence_items[0].id != first.has_evidence_items[0].id


class TestEvidenceToLines:
    """Tests for converting a whole dismech evidence list."""

    def test_one_line_per_evidence_item(self):
        """Each snippet is its own interpretation, so each gets its own line."""
        lines = evidence_to_lines(CFTR_EVIDENCE, "urn:uuid:statement")
        assert len(lines) == 2
        assert lines[0].id != lines[1].id

    def test_none_and_empty(self):
        assert evidence_to_lines(None, "s") == []
        assert evidence_to_lines([], "s") == []


class FakeAssociation:
    """Minimal stand-in for a Biolink Association (biolink-model is an optional dep)."""

    def __init__(self, id="urn:uuid:edge-1", subject="MONDO:0009061",
                 predicate="biolink:has_phenotype", object="HP:0030828"):
        self.id = id
        self.subject = subject
        self.predicate = predicate
        self.object = object


class TestStatementFromAssociation:
    """Tests for the KGX association -> SEPIO Statement mapping."""

    def test_statement_reuses_edge_id(self):
        """The shared id is what joins the SEPIO sidecar to the KGX edge file."""
        association = FakeAssociation()
        statement = statement_from_association(
            association, CFTR_EVIDENCE, disease_name="Cystic Fibrosis", section="phenotypes"
        )
        assert statement.id == association.id
        assert statement.subject == "MONDO:0009061"
        assert statement.predicate == "biolink:has_phenotype"
        assert statement.object == "HP:0030828"
        assert statement.source_disease == "Cystic Fibrosis"
        assert statement.dismech_section == "phenotypes"
        assert len(statement.has_evidence_lines) == 2

    def test_association_without_evidence_yields_no_statement(self):
        """A SEPIO Statement with no evidence line would assert nothing."""
        assert statement_from_association(FakeAssociation(), None) is None
        assert statement_from_association(FakeAssociation(), []) is None

    def test_inherited_evidence_is_attributed(self):
        """Indirect evidence points back at the node statement that owns it."""
        parent_id = pathophysiology_statement_id("Cystic Fibrosis", "CFTR Dysfunction")
        statement = statement_from_association(
            FakeAssociation(),
            CFTR_EVIDENCE,
            disease_name="Cystic Fibrosis",
            section="pathophysiology.cell_types",
            inherited_from=parent_id,
        )
        assert statement.evidence_inherited_from == parent_id


class TestPathophysiologyStatements:
    """Tests for the assertions that have no KGX counterpart."""

    def test_node_and_causal_edge_statements(self):
        statements = list(pathophysiology_statements(CFTR_RECORD))
        assert len(statements) == 2

        node, causal = statements
        assert node.subject == "MONDO:0009061"
        assert node.predicate == "dismech:has_pathophysiology"
        assert node.object == "dismech:Cystic_Fibrosis#CFTR_Dysfunction"
        assert node.object_label == "CFTR Dysfunction"
        assert len(node.has_evidence_lines) == 2

        assert causal.subject == node.object
        assert causal.predicate == "dismech:causally_upstream_of"
        assert causal.object == "dismech:Cystic_Fibrosis#Airway_Surface_Liquid_Depletion"
        assert causal.qualifiers == ["DIRECT"]
        assert len(causal.has_evidence_lines) == 1

    def test_node_statement_id_is_deterministic(self):
        """Statement ids must be stable across runs so downstream links survive."""
        first = next(iter(pathophysiology_statements(CFTR_RECORD)))
        second = next(iter(pathophysiology_statements(CFTR_RECORD)))
        assert first.id == second.id
        assert first.id == pathophysiology_statement_id("Cystic Fibrosis", "CFTR Dysfunction")

    def test_node_id_slugified(self):
        assert pathophysiology_node_id("Cystic Fibrosis", "CFTR Dysfunction") == (
            "dismech:Cystic_Fibrosis#CFTR_Dysfunction"
        )

    def test_competing_hypothesis_edges_get_distinct_ids(self):
        """Two edges between the same nodes under rival models are distinct assertions.

        Glutaryl-CoA Dehydrogenase Deficiency asserts both an intracerebral and a
        hepatic origin for the same downstream node.
        """
        record = {
            "name": "GA1",
            "disease_term": {"term": {"id": "MONDO:1"}},
            "pathophysiology": [
                {
                    "name": "A",
                    "downstream": [
                        {
                            "target": "B",
                            "hypothesis_groups": ["intracerebral_model"],
                            "evidence": [{"reference": "PMID:1", "snippet": "one"}],
                        },
                        {
                            "target": "B",
                            "hypothesis_groups": ["hepatic_model"],
                            "evidence": [{"reference": "PMID:1", "snippet": "two"}],
                        },
                    ],
                }
            ],
        }
        statements = list(pathophysiology_statements(record))
        assert len({s.id for s in statements}) == 2
        assert statements[0].hypothesis_groups == ["intracerebral_model"]
        assert statements[1].hypothesis_groups == ["hepatic_model"]

    def test_identical_edges_still_get_distinct_ids(self):
        """The occurrence counter is the backstop when nothing else separates them."""
        record = {
            "name": "X",
            "disease_term": {"term": {"id": "MONDO:1"}},
            "pathophysiology": [
                {
                    "name": "A",
                    "downstream": [
                        {"target": "B", "evidence": [{"reference": "PMID:1", "snippet": "one"}]},
                        {"target": "B", "evidence": [{"reference": "PMID:1", "snippet": "two"}]},
                    ],
                }
            ],
        }
        statements = list(pathophysiology_statements(record))
        assert len({s.id for s in statements}) == 2
        # ...and the ids are still reproducible run to run.
        assert [s.id for s in pathophysiology_statements(record)] == [s.id for s in statements]

    def test_duplicate_node_names_get_distinct_statement_ids(self):
        """Two node names that slug to the same value must not collide on one id.

        No such collision exists in `kb/` today; this is the backstop that keeps
        the invariant enforced rather than assumed, mirroring the causal-edge
        occurrence counter.
        """
        record = {
            "name": "X",
            "disease_term": {"term": {"id": "MONDO:1"}},
            "pathophysiology": [
                {"name": "Node A", "evidence": [{"reference": "PMID:1", "snippet": "one"}]},
                {"name": "Node-A", "evidence": [{"reference": "PMID:1", "snippet": "two"}]},
            ],
        }
        statements = list(pathophysiology_statements(record))
        assert len(statements) == 2
        assert len({s.id for s in statements}) == 2
        # The first occurrence keeps the plain deterministic id, so the public
        # `pathophysiology_statement_id` (and any `evidence_inherited_from`
        # pointing at it) still resolves.
        assert statements[0].id == pathophysiology_statement_id("X", "Node A")
        assert [s.id for s in pathophysiology_statements(record)] == [s.id for s in statements]

    def test_missing_disease_term_yields_nothing(self):
        assert list(pathophysiology_statements({"name": "X", "pathophysiology": []})) == []

    def test_nodes_and_edges_without_evidence_skipped(self):
        record = {
            "name": "X",
            "disease_term": {"term": {"id": "MONDO:1"}},
            "pathophysiology": [
                {"name": "Node A", "downstream": [{"target": "Node B"}]},
                {"name": None, "evidence": CFTR_EVIDENCE},
            ],
        }
        assert list(pathophysiology_statements(record)) == []


class TestStatementsFromRecord:
    """Tests for the full per-record walk (requires biolink-model for the KGX edges)."""

    def test_covers_kgx_edges_and_pathophysiology(self):
        pytest.importorskip("biolink_model", reason="biolink-model not installed")
        from dismech.export.sepio_export import statements_from_record

        record = dict(CFTR_RECORD)
        record["phenotypes"] = [
            {
                "name": "Chronic cough",
                "phenotype_term": {"term": {"id": "HP:0012735", "label": "Chronic cough"}},
                "evidence": [
                    {
                        "reference": "PMID:33526571",
                        "supports": "SUPPORT",
                        "snippet": "progressive obstructive lung disease",
                    }
                ],
            }
        ]
        statements = list(statements_from_record(record))
        sections = {s.dismech_section for s in statements}
        assert "phenotypes" in sections
        assert "pathophysiology" in sections
        assert "pathophysiology.downstream" in sections

    def test_kgx_edge_ids_join_to_statement_ids(self):
        """The KGX edge and its SEPIO statement must be the same run's same id."""
        pytest.importorskip("biolink_model", reason="biolink-model not installed")
        from dismech.export.kgx_export import iter_edges_with_evidence

        record = {
            "name": "Cystic Fibrosis",
            "disease_term": {"term": {"id": "MONDO:0009061"}},
            "pathophysiology": CFTR_RECORD["pathophysiology"],
        }
        record["pathophysiology"][0]["cell_types"] = [
            {"preferred_term": "Epithelial cell", "term": {"id": "CL:0000066"}}
        ]
        edges = list(iter_edges_with_evidence(record))
        assert edges
        edge = edges[0]
        assert edge.indirect is True
        assert edge.source_node == "CFTR Dysfunction"
        assert edge.evidence == CFTR_EVIDENCE
        statement = statement_from_association(edge.association, edge.evidence)
        assert statement.id == edge.association.id

    def test_statements_for_edges_is_the_shared_builder(self):
        """The koza transform and statements_from_record must agree line for line."""
        pytest.importorskip("biolink_model", reason="biolink-model not installed")
        from dismech.export.kgx_export import iter_edges_with_evidence
        from dismech.export.sepio_export import statements_for_edges

        record = {
            "name": "Cystic Fibrosis",
            "disease_term": {"term": {"id": "MONDO:0009061"}},
            "pathophysiology": [
                {
                    "name": "CFTR Dysfunction",
                    "evidence": CFTR_EVIDENCE,
                    "cell_types": [
                        {"preferred_term": "Epithelial cell", "term": {"id": "CL:0000066"}}
                    ],
                }
            ],
        }
        edges = list(iter_edges_with_evidence(record))
        statements = list(statements_for_edges(edges, record["name"]))
        assert statements
        # Indirect evidence resolves back to the node statement that owns it.
        assert statements[0].evidence_inherited_from == pathophysiology_statement_id(
            "Cystic Fibrosis", "CFTR Dysfunction"
        )
        assert statements[0].id == edges[0].association.id

    def test_statements_for_edges_skips_evidence_free_edges(self):
        """No biolink needed: the helper only reads the EdgeWithEvidence fields."""
        from dismech.export.sepio_export import statements_for_edges

        class FakeEdge:
            def __init__(self, evidence):
                self.association = FakeAssociation()
                self.evidence = evidence
                self.section = "phenotypes"
                self.indirect = False
                self.source_node = None

        assert list(statements_for_edges([FakeEdge(None), FakeEdge([])], "X")) == []
        assert len(list(statements_for_edges([FakeEdge(CFTR_EVIDENCE)], "X"))) == 1


class FakeWriter:
    """Stand-in for a koza JSONL writer: one instance per transform run."""

    def __init__(self, output_dir, source_name="kgx_export"):
        self.output_dir = str(output_dir)
        self.source_name = source_name


class FakeKozaContext:
    """Minimal stand-in for KozaTransform: the sidecar hooks only use these three."""

    def __init__(self, writer):
        self.writer = writer
        self.state = {}
        self.logged = []

    def log(self, message, level="INFO"):
        self.logged.append((level, message))


class TestSepioSidecarLifecycle:
    """Tests for the sidecar file handle managed by the on_data_begin/end hooks."""

    @staticmethod
    def _run(writer, line):
        """One transform run: open the sidecar, write a line, close it."""
        kgx_export = pytest.importorskip(
            "dismech.export.kgx_export", reason="biolink-model not installed"
        )
        koza_ctx = FakeKozaContext(writer)
        kgx_export.open_sepio_sidecar(koza_ctx)
        handle = koza_ctx.state[kgx_export._SEPIO_STATE_KEY]
        handle.write(line + "\n")
        kgx_export.close_sepio_sidecar(koza_ctx)
        assert koza_ctx.state == {}

    def test_second_run_truncates_the_sidecar(self, tmp_path):
        """A new run gets a new writer, so it must rewrite — not append to — the sidecar.

        The node/edge files are rewritten from scratch by koza's writer on every
        run; a sidecar that appended instead would silently disagree with them.
        """
        sidecar = tmp_path / "kgx_export_sepio.jsonl"

        self._run(FakeWriter(tmp_path), "run-1")
        assert sidecar.read_text(encoding="utf-8").splitlines() == ["run-1"]

        self._run(FakeWriter(tmp_path), "run-2")
        assert sidecar.read_text(encoding="utf-8").splitlines() == ["run-2"]

    def test_second_tag_of_one_run_appends(self, tmp_path):
        """Koza builds a context per input tag but shares one writer across them."""
        sidecar = tmp_path / "kgx_export_sepio.jsonl"
        writer = FakeWriter(tmp_path)

        self._run(writer, "tag-1")
        self._run(writer, "tag-2")
        assert sidecar.read_text(encoding="utf-8").splitlines() == ["tag-1", "tag-2"]

    def test_writer_without_output_dir_skips_the_sidecar(self, tmp_path):
        """The passthrough writer has no destination, so there is nothing to open."""
        kgx_export = pytest.importorskip(
            "dismech.export.kgx_export", reason="biolink-model not installed"
        )

        class PassthroughWriter:
            pass

        koza_ctx = FakeKozaContext(PassthroughWriter())
        kgx_export.open_sepio_sidecar(koza_ctx)
        assert kgx_export._SEPIO_STATE_KEY not in koza_ctx.state
        assert koza_ctx.logged and koza_ctx.logged[0][0] == "WARNING"
        # ...and closing without a handle is a no-op rather than a crash.
        kgx_export.close_sepio_sidecar(koza_ctx)


class TestSerialization:
    """Tests for the JSONL output shape."""

    def test_dump_statement_omits_empty_fields(self):
        statement = Statement(
            id="urn:uuid:1",
            subject="MONDO:1",
            predicate="biolink:has_phenotype",
            object="HP:1",
            has_evidence_lines=evidence_to_lines(CFTR_EVIDENCE[:1], "urn:uuid:1"),
        )
        payload = json.loads(dump_statement(statement))
        assert payload["type"] == "Statement"
        assert "subject_label" not in payload
        assert "evidence_inherited_from" not in payload
        assert payload["has_evidence_lines"][0]["has_evidence_items"][0]["data_type"] == "TextSpan"

    def test_write_jsonl(self, tmp_path):
        out = tmp_path / "nested" / "sepio.jsonl"
        count = write_jsonl(pathophysiology_statements(CFTR_RECORD), out)
        assert count == 2
        lines = out.read_text(encoding="utf-8").strip().split("\n")
        assert len(lines) == 2
        assert all(json.loads(line)["type"] == "Statement" for line in lines)
