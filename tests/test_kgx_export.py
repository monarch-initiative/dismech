"""Tests for KGX edge exporter."""

import pytest
from biolink_model.datamodel.pydanticmodel_v2 import (
    Association,
    ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation,
    DiseaseOrPhenotypicFeatureToLocationAssociation,
    DiseaseToPhenotypicFeatureAssociation,
    ExposureEventToOutcomeAssociation,
    GeneToDiseaseAssociation,
)

from dismech.export.kgx_export import (
    KNOWLEDGE_SOURCE,
    biological_process_to_edge,
    cell_type_to_edge,
    exposure_to_edge,
    gene_to_edge,
    location_to_edge,
    phenotype_to_edge,
    transform,
    treatment_to_edge,
)


class TestPhenotypeToEdge:
    """Tests for phenotype_to_edge function."""

    def test_valid_phenotype(self):
        """Test with a complete phenotype entry."""
        phenotype = {
            "name": "Wheezing",
            "phenotype_term": {
                "preferred_term": "Wheezing",
                "term": {"id": "HP:0030828", "label": "Wheezing"},
            },
        }
        edge = phenotype_to_edge("MONDO:0004979", phenotype)
        assert isinstance(edge, DiseaseToPhenotypicFeatureAssociation)
        assert edge.subject == "MONDO:0004979"
        assert edge.predicate == "biolink:has_phenotype"
        assert edge.object == "HP:0030828"
        assert edge.primary_knowledge_source == KNOWLEDGE_SOURCE

    def test_missing_phenotype_term(self):
        """Test with missing phenotype_term."""
        phenotype = {"name": "Wheezing"}
        assert phenotype_to_edge("MONDO:0004979", phenotype) is None

    def test_missing_term_id(self):
        """Test with phenotype_term but no term.id."""
        phenotype = {
            "phenotype_term": {"preferred_term": "Wheezing", "term": {"label": "Wheezing"}}
        }
        assert phenotype_to_edge("MONDO:0004979", phenotype) is None

    def test_none_phenotype(self):
        """Test with None phenotype."""
        assert phenotype_to_edge("MONDO:0004979", None) is None


class TestCellTypeToEdge:
    """Tests for cell_type_to_edge function."""

    def test_valid_cell_type(self):
        """Test with a complete cell type entry."""
        cell_type = {
            "preferred_term": "Mast Cell",
            "term": {"id": "CL:0000097", "label": "mast cell"},
        }
        edge = cell_type_to_edge("MONDO:0004979", cell_type)
        assert isinstance(edge, Association)
        assert edge.subject == "MONDO:0004979"
        assert edge.predicate == "biolink:has_participant"
        assert edge.object == "CL:0000097"
        assert edge.primary_knowledge_source == KNOWLEDGE_SOURCE

    def test_missing_term(self):
        """Test with missing term."""
        cell_type = {"preferred_term": "Mast Cell"}
        assert cell_type_to_edge("MONDO:0004979", cell_type) is None

    def test_missing_term_id(self):
        """Test with term but no id."""
        cell_type = {"term": {"label": "mast cell"}}
        assert cell_type_to_edge("MONDO:0004979", cell_type) is None


class TestLocationToEdge:
    """Tests for location_to_edge function."""

    def test_valid_location(self):
        """Test with a complete location entry."""
        location = {
            "preferred_term": "aorta",
            "term": {"id": "UBERON:0000947", "label": "aorta"},
        }
        edge = location_to_edge("MONDO:0007947", location)
        assert isinstance(edge, DiseaseOrPhenotypicFeatureToLocationAssociation)
        assert edge.subject == "MONDO:0007947"
        assert edge.predicate == "biolink:disease_has_location"
        assert edge.object == "UBERON:0000947"
        assert edge.primary_knowledge_source == KNOWLEDGE_SOURCE

    def test_missing_term_id(self):
        """Test with missing term.id."""
        location = {"preferred_term": "aorta", "term": {"label": "aorta"}}
        assert location_to_edge("MONDO:0007947", location) is None


class TestBiologicalProcessToEdge:
    """Tests for biological_process_to_edge function."""

    def test_valid_process(self):
        """Test with a complete biological process entry."""
        process = {
            "preferred_term": "inflammatory response",
            "term": {"id": "GO:0006954", "label": "inflammatory response"},
        }
        edge = biological_process_to_edge("MONDO:0004979", process)
        assert isinstance(edge, Association)
        assert edge.subject == "MONDO:0004979"
        assert edge.predicate == "biolink:affects"
        assert edge.object == "GO:0006954"
        assert edge.primary_knowledge_source == KNOWLEDGE_SOURCE

    def test_missing_term_id(self):
        """Test with missing term.id."""
        process = {"preferred_term": "inflammatory response"}
        assert biological_process_to_edge("MONDO:0004979", process) is None


class TestTreatmentToEdge:
    """Tests for treatment_to_edge function."""

    def test_valid_treatment(self):
        """Test with a complete treatment entry."""
        treatment = {
            "name": "Inhaled Corticosteroid",
            "treatment_term": {
                "preferred_term": "respiratory tract agent therapy",
                "term": {"id": "MAXO:0000312", "label": "respiratory tract agent therapy"},
            },
        }
        edge = treatment_to_edge("MONDO:0004979", treatment)
        assert isinstance(edge, ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation)
        # Treatment is subject, disease is object
        assert edge.subject == "MAXO:0000312"
        assert edge.predicate == "biolink:treats_or_applied_or_studied_to_treat"
        assert edge.object == "MONDO:0004979"
        assert edge.primary_knowledge_source == KNOWLEDGE_SOURCE

    def test_missing_treatment_term(self):
        """Test with missing treatment_term."""
        treatment = {"name": "Inhaled Corticosteroid"}
        assert treatment_to_edge("MONDO:0004979", treatment) is None

    def test_missing_term_id(self):
        """Test with treatment_term but no term.id."""
        treatment = {
            "treatment_term": {"preferred_term": "respiratory tract agent therapy"}
        }
        assert treatment_to_edge("MONDO:0004979", treatment) is None


class TestGeneToEdge:
    """Tests for gene_to_edge function."""

    def test_valid_gene(self):
        """Test with a complete gene entry."""
        gene = {"name": "IL4", "association": "Associated"}
        edge = gene_to_edge("MONDO:0004979", gene)
        assert isinstance(edge, GeneToDiseaseAssociation)
        assert edge.subject == "HGNC.SYMBOL:IL4"
        assert edge.predicate == "biolink:gene_associated_with_condition"
        assert edge.object == "MONDO:0004979"
        assert edge.primary_knowledge_source == KNOWLEDGE_SOURCE

    def test_missing_name(self):
        """Test with missing gene name."""
        gene = {"association": "Associated"}
        assert gene_to_edge("MONDO:0004979", gene) is None

    def test_none_gene(self):
        """Test with None gene."""
        assert gene_to_edge("MONDO:0004979", None) is None

    def test_empty_name(self):
        """Test with empty gene name."""
        gene = {"name": "", "association": "Associated"}
        assert gene_to_edge("MONDO:0004979", gene) is None


class TestExposureToEdge:
    """Tests for exposure_to_edge function."""

    def test_valid_exposure(self):
        """Test with a complete exposure entry."""
        environmental = {
            "name": "Tobacco Smoke",
            "exposure_term": {
                "preferred_term": "exposure to tobacco smoking",
                "term": {"id": "ECTO:6000029", "label": "exposure to tobacco smoking"},
            },
        }
        edge = exposure_to_edge("MONDO:0004979", environmental)
        assert isinstance(edge, ExposureEventToOutcomeAssociation)
        # Exposure is subject, disease is object
        assert edge.subject == "ECTO:6000029"
        assert edge.predicate == "biolink:contributes_to"
        assert edge.object == "MONDO:0004979"
        assert edge.primary_knowledge_source == KNOWLEDGE_SOURCE

    def test_missing_exposure_term(self):
        """Test with missing exposure_term."""
        environmental = {"name": "Tobacco Smoke"}
        assert exposure_to_edge("MONDO:0004979", environmental) is None

    def test_missing_term_id(self):
        """Test with exposure_term but no term.id."""
        environmental = {
            "exposure_term": {"preferred_term": "exposure to tobacco smoking"}
        }
        assert exposure_to_edge("MONDO:0004979", environmental) is None


class TestTransform:
    """Tests for the full transform function."""

    @pytest.fixture
    def sample_disorder(self):
        """Create a sample disorder with all edge types."""
        return {
            "name": "Test Disorder",
            "disease_term": {
                "preferred_term": "test disorder",
                "term": {"id": "MONDO:0000001", "label": "test disorder"},
            },
            "phenotypes": [
                {
                    "name": "Phenotype A",
                    "phenotype_term": {
                        "term": {"id": "HP:0000001", "label": "Phenotype A"}
                    },
                },
                {
                    "name": "Phenotype B",
                    "phenotype_term": {
                        "term": {"id": "HP:0000002", "label": "Phenotype B"}
                    },
                },
            ],
            "pathophysiology": [
                {
                    "name": "Mechanism A",
                    "cell_types": [
                        {"term": {"id": "CL:0000001", "label": "Cell Type A"}},
                    ],
                    "locations": [
                        {"term": {"id": "UBERON:0000001", "label": "Location A"}},
                    ],
                    "biological_processes": [
                        {"term": {"id": "GO:0000001", "label": "Process A"}},
                    ],
                },
            ],
            "treatments": [
                {
                    "name": "Treatment A",
                    "treatment_term": {
                        "term": {"id": "MAXO:0000001", "label": "Treatment A"}
                    },
                },
            ],
            "genetic": [
                {"name": "GENE1", "association": "Associated"},
            ],
        }

    def test_transform_extracts_all_edges(self, sample_disorder):
        """Test that transform extracts all edge types."""
        edges = list(transform(sample_disorder))

        # Should have: 2 phenotypes + 1 cell_type + 1 location + 1 process + 1 treatment + 1 gene = 7
        assert len(edges) == 7

        # All edges should be Association instances
        for edge in edges:
            assert isinstance(edge, Association)

        # Check edge types are present
        predicates = [e.predicate for e in edges]
        assert predicates.count("biolink:has_phenotype") == 2
        assert predicates.count("biolink:has_participant") == 1  # cell_type only
        assert predicates.count("biolink:affects") == 1  # biological process
        assert predicates.count("biolink:disease_has_location") == 1
        assert predicates.count("biolink:treats_or_applied_or_studied_to_treat") == 1
        assert predicates.count("biolink:gene_associated_with_condition") == 1

    def test_transform_missing_disease_term(self):
        """Test that transform returns nothing if disease_term is missing."""
        disorder = {"name": "Test Disorder", "phenotypes": []}
        edges = list(transform(disorder))
        assert len(edges) == 0

    def test_transform_empty_collections(self):
        """Test transform with empty/None collections."""
        disorder = {
            "name": "Test Disorder",
            "disease_term": {"term": {"id": "MONDO:0000001"}},
            "phenotypes": None,
            "pathophysiology": None,
            "treatments": [],
            "genetic": None,
        }
        edges = list(transform(disorder))
        assert len(edges) == 0

    def test_transform_skips_incomplete_entries(self):
        """Test that transform skips entries without term IDs."""
        disorder = {
            "name": "Test Disorder",
            "disease_term": {"term": {"id": "MONDO:0000001"}},
            "phenotypes": [
                {"name": "Complete", "phenotype_term": {"term": {"id": "HP:0000001"}}},
                {"name": "Incomplete"},  # No phenotype_term
            ],
            "pathophysiology": [
                {
                    "cell_types": [
                        {"term": {"id": "CL:0000001"}},
                        {"preferred_term": "No ID"},  # No term.id
                    ],
                }
            ],
        }
        edges = list(transform(disorder))

        # Should only have 1 phenotype + 1 cell_type = 2
        assert len(edges) == 2
