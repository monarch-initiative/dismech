"""Tests for KGX edge and node exporter."""

import pytest

pytest.importorskip("biolink_model", reason="biolink-model not installed (install with: uv sync --group export)")

from biolink_model.datamodel.pydanticmodel_v2 import (
    AnatomicalEntity,
    Association,
    BiologicalProcess,
    Cell,
    CellularComponent,
    ChemicalEntity,
    ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation,
    Disease,
    DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation,
    DiseaseOrPhenotypicFeatureToLocationAssociation,
    DiseaseToPhenotypicFeatureAssociation,
    ExposureEvent,
    ExposureEventToOutcomeAssociation,
    Gene,
    GeneticInheritance,
    GeneToDiseaseAssociation,
    MacromolecularComplex,
    MolecularActivity,
    MolecularEntity,
    OrganismTaxon,
    Pathway,
    PhenotypicFeature,
    Treatment,
)

from dismech.export.kgx_export import (
    KNOWLEDGE_SOURCE,
    biomarker_to_edge,
    biological_process_to_edge,
    cell_type_to_edge,
    cellular_component_to_edge,
    chemical_entity_to_edge,
    exposure_to_edge,
    extract_nodes,
    gene_to_edge,
    histopathology_to_edge,
    infectious_agent_to_edge,
    inheritance_to_edge,
    location_to_edge,
    molecular_function_to_edge,
    pathway_to_edge,
    phenotype_to_edge,
    protein_complex_to_edge,
    therapeutic_agent_to_edge,
    transform,
    treatment_to_edge,
    treatment_target_phenotype_to_edge,
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
        assert edge.subject_category == "biolink:Disease"
        assert edge.object_category == "biolink:PhenotypicFeature"
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
        assert edge.subject_category == "biolink:Disease"
        assert edge.object_category == "biolink:Cell"
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
        assert edge.subject_category == "biolink:Disease"
        assert edge.object_category == "biolink:AnatomicalEntity"
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
        assert edge.subject_category == "biolink:Disease"
        assert edge.object_category == "biolink:BiologicalProcess"
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
        assert edge.subject_category == "biolink:Treatment"
        assert edge.object_category == "biolink:Disease"
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
        assert edge.predicate == "biolink:contributes_to"
        assert edge.object == "MONDO:0004979"
        assert edge.subject_category == "biolink:Gene"
        assert edge.object_category == "biolink:Disease"
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
        assert edge.subject_category == "biolink:ExposureEvent"
        assert edge.object_category == "biolink:Disease"
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


class TestMolecularFunctionToEdge:
    """Tests for molecular_function_to_edge function."""

    def test_valid_molecular_function(self):
        """Test with a complete molecular function entry."""
        mf = {
            "preferred_term": "kinase activity",
            "term": {"id": "GO:0016301", "label": "kinase activity"},
            "modifier": "INCREASED",
        }
        edge = molecular_function_to_edge("MONDO:0004979", mf)
        assert isinstance(edge, Association)
        assert edge.subject == "MONDO:0004979"
        assert edge.predicate == "biolink:affects"
        assert edge.object == "GO:0016301"
        assert edge.subject_category == "biolink:Disease"
        assert edge.object_category == "biolink:MolecularActivity"
        assert "direction:increased" in edge.qualifiers

    def test_missing_term_id(self):
        """Test with missing term.id."""
        mf = {"preferred_term": "kinase activity"}
        assert molecular_function_to_edge("MONDO:0004979", mf) is None


class TestCellularComponentToEdge:
    """Tests for cellular_component_to_edge function."""

    def test_valid_cellular_component(self):
        """Test with a complete cellular component entry."""
        component = {
            "preferred_term": "cilium",
            "term": {"id": "GO:0005929", "label": "cilium"},
        }
        edge = cellular_component_to_edge("MONDO:0004979", component)
        assert isinstance(edge, Association)
        assert edge.subject == "MONDO:0004979"
        assert edge.predicate == "biolink:has_participant"
        assert edge.object == "GO:0005929"
        assert edge.subject_category == "biolink:Disease"
        assert edge.object_category == "biolink:CellularComponent"

    def test_missing_term_id(self):
        """Test with missing term.id."""
        component = {"preferred_term": "cilium"}
        assert cellular_component_to_edge("MONDO:0004979", component) is None


class TestChemicalEntityToEdge:
    """Tests for chemical_entity_to_edge function."""

    def test_valid_chemical_entity(self):
        """Test with a complete chemical entity entry."""
        chemical = {
            "preferred_term": "phenylpyruvate",
            "term": {"id": "CHEBI:29048", "label": "phenylpyruvate"},
        }
        edge = chemical_entity_to_edge("MONDO:0004979", chemical)
        assert isinstance(edge, Association)
        assert edge.subject == "MONDO:0004979"
        assert edge.predicate == "biolink:has_participant"
        assert edge.object == "CHEBI:29048"
        assert edge.subject_category == "biolink:Disease"
        assert edge.object_category == "biolink:ChemicalEntity"

    def test_missing_term_id(self):
        """Test with missing term.id."""
        chemical = {"preferred_term": "phenylpyruvate"}
        assert chemical_entity_to_edge("MONDO:0004979", chemical) is None


class TestPathwayToEdge:
    """Tests for pathway_to_edge function."""

    def test_valid_pathway(self):
        """Test with a complete pathway entry."""
        pathway = {
            "preferred_term": "Wnt signaling pathway",
            "term": {"id": "GO:0016055", "label": "Wnt signaling pathway"},
            "modifier": "DECREASED",
        }
        edge = pathway_to_edge("MONDO:0004979", pathway)
        assert isinstance(edge, Association)
        assert edge.subject == "MONDO:0004979"
        assert edge.predicate == "biolink:affects"
        assert edge.object == "GO:0016055"
        assert edge.subject_category == "biolink:Disease"
        assert edge.object_category == "biolink:Pathway"
        assert "direction:decreased" in edge.qualifiers

    def test_missing_term_id(self):
        """Test with missing term.id."""
        pathway = {"preferred_term": "Wnt signaling pathway"}
        assert pathway_to_edge("MONDO:0004979", pathway) is None


class TestProteinComplexToEdge:
    """Tests for protein_complex_to_edge function."""

    def test_valid_protein_complex(self):
        """Test with a complete protein complex entry."""
        complex_ = {
            "preferred_term": "MutL complex",
            "term": {"id": "GO:0030391", "label": "DNA mismatch repair complex"},
        }
        edge = protein_complex_to_edge("MONDO:0004979", complex_)
        assert isinstance(edge, Association)
        assert edge.subject == "MONDO:0004979"
        assert edge.predicate == "biolink:has_participant"
        assert edge.object == "GO:0030391"
        assert edge.subject_category == "biolink:Disease"
        assert edge.object_category == "biolink:MacromolecularComplex"

    def test_missing_term_id(self):
        """Test with missing term.id."""
        complex_ = {"preferred_term": "MutL complex"}
        assert protein_complex_to_edge("MONDO:0004979", complex_) is None


class TestInheritanceToEdge:
    """Tests for inheritance_to_edge function."""

    def test_valid_inheritance(self):
        """Test with a complete inheritance entry."""
        inheritance = {
            "inheritance_term": {
                "preferred_term": "Autosomal dominant inheritance",
                "term": {"id": "HP:0000006", "label": "Autosomal dominant inheritance"},
            },
        }
        edge = inheritance_to_edge("MONDO:0004979", inheritance)
        assert isinstance(edge, DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation)
        assert edge.subject == "MONDO:0004979"
        assert edge.predicate == "biolink:has_mode_of_inheritance"
        assert edge.object == "HP:0000006"
        assert edge.subject_category == "biolink:Disease"
        assert edge.object_category == "biolink:GeneticInheritance"

    def test_missing_inheritance_term(self):
        """Test with missing inheritance_term."""
        inheritance = {"description": "Some description"}
        assert inheritance_to_edge("MONDO:0004979", inheritance) is None

    def test_missing_term_id(self):
        """Test with inheritance_term but no term.id."""
        inheritance = {
            "inheritance_term": {"preferred_term": "Autosomal dominant"}
        }
        assert inheritance_to_edge("MONDO:0004979", inheritance) is None


class TestInfectiousAgentToEdge:
    """Tests for infectious_agent_to_edge function."""

    def test_valid_infectious_agent(self):
        """Test with a complete infectious agent entry."""
        agent = {
            "name": "Chlamydia trachomatis",
            "infectious_agent_term": {
                "preferred_term": "Chlamydia trachomatis",
                "term": {"id": "NCBITaxon:813", "label": "Chlamydia trachomatis"},
            },
        }
        edge = infectious_agent_to_edge("MONDO:0004979", agent)
        assert isinstance(edge, Association)
        # Agent is subject, disease is object
        assert edge.subject == "NCBITaxon:813"
        assert edge.predicate == "biolink:causes"
        assert edge.object == "MONDO:0004979"
        assert edge.subject_category == "biolink:OrganismTaxon"
        assert edge.object_category == "biolink:Disease"

    def test_missing_agent_term(self):
        """Test with missing infectious_agent_term."""
        agent = {"name": "Some organism"}
        assert infectious_agent_to_edge("MONDO:0004979", agent) is None

    def test_missing_term_id(self):
        """Test with infectious_agent_term but no term.id."""
        agent = {
            "infectious_agent_term": {"preferred_term": "Chlamydia trachomatis"}
        }
        assert infectious_agent_to_edge("MONDO:0004979", agent) is None


class TestHistopathologyToEdge:
    """Tests for histopathology_to_edge function."""

    def test_valid_histopathology(self):
        """Test with a complete histopathology finding."""
        finding = {
            "name": "Squamous metaplasia",
            "finding_term": {
                "preferred_term": "Squamous metaplasia",
                "term": {"id": "NCIT:C3237", "label": "Squamous Metaplasia"},
            },
        }
        edge = histopathology_to_edge("MONDO:0004979", finding)
        assert isinstance(edge, DiseaseToPhenotypicFeatureAssociation)
        assert edge.subject == "MONDO:0004979"
        assert edge.predicate == "biolink:has_phenotype"
        assert edge.object == "NCIT:C3237"
        assert edge.subject_category == "biolink:Disease"
        assert edge.object_category == "biolink:PhenotypicFeature"

    def test_missing_finding_term(self):
        """Test with missing finding_term."""
        finding = {"name": "Squamous metaplasia"}
        assert histopathology_to_edge("MONDO:0004979", finding) is None

    def test_missing_term_id(self):
        """Test with finding_term but no term.id."""
        finding = {
            "finding_term": {"preferred_term": "Squamous metaplasia"}
        }
        assert histopathology_to_edge("MONDO:0004979", finding) is None


class TestBiomarkerToEdge:
    """Tests for biomarker_to_edge function."""

    def test_valid_biomarker(self):
        """Test with a complete biomarker entry."""
        biochemical = {
            "name": "Mesothelin",
            "biomarker_term": {
                "preferred_term": "Mesothelin",
                "term": {"id": "NCIT:C20887", "label": "Mesothelin"},
            },
        }
        edge = biomarker_to_edge("MONDO:0004979", biochemical)
        assert isinstance(edge, Association)
        assert edge.subject == "MONDO:0004979"
        assert edge.predicate == "biolink:has_biomarker"
        assert edge.object == "NCIT:C20887"
        assert edge.subject_category == "biolink:Disease"
        assert edge.object_category == "biolink:MolecularEntity"

    def test_missing_biomarker_term(self):
        """Test with missing biomarker_term."""
        biochemical = {"name": "Mesothelin"}
        assert biomarker_to_edge("MONDO:0004979", biochemical) is None

    def test_missing_term_id(self):
        """Test with biomarker_term but no term.id."""
        biochemical = {
            "biomarker_term": {"preferred_term": "Mesothelin"}
        }
        assert biomarker_to_edge("MONDO:0004979", biochemical) is None


class TestTherapeuticAgentToEdge:
    """Tests for therapeutic_agent_to_edge function."""

    def test_valid_therapeutic_agent(self):
        """Test with a complete therapeutic agent entry."""
        agent = {
            "preferred_term": "adalimumab",
            "term": {"id": "NCIT:C65216", "label": "Adalimumab"},
        }
        edge = therapeutic_agent_to_edge("MONDO:0004979", agent)
        assert isinstance(edge, ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation)
        # Agent is subject, disease is object
        assert edge.subject == "NCIT:C65216"
        assert edge.predicate == "biolink:treats_or_applied_or_studied_to_treat"
        assert edge.object == "MONDO:0004979"
        assert edge.subject_category == "biolink:ChemicalEntity"
        assert edge.object_category == "biolink:Disease"

    def test_missing_term_id(self):
        """Test with missing term.id."""
        agent = {"preferred_term": "adalimumab"}
        assert therapeutic_agent_to_edge("MONDO:0004979", agent) is None


class TestTreatmentTargetPhenotypeToEdge:
    """Tests for treatment_target_phenotype_to_edge function."""

    def test_valid_target_phenotype(self):
        """Test with a complete target phenotype entry."""
        phenotype = {
            "preferred_term": "Fatigue",
            "term": {"id": "HP:0012378", "label": "Fatigue"},
        }
        edge = treatment_target_phenotype_to_edge(
            "MONDO:0004979", "MAXO:0000058", phenotype
        )
        assert isinstance(edge, ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation)
        assert edge.subject == "MAXO:0000058"
        assert edge.predicate == "biolink:treats_or_applied_or_studied_to_treat"
        assert edge.object == "HP:0012378"
        assert edge.subject_category == "biolink:Treatment"
        assert edge.object_category == "biolink:PhenotypicFeature"
        assert edge.disease_context_qualifier == "MONDO:0004979"

    def test_missing_term_id(self):
        """Test with missing term.id."""
        phenotype = {"preferred_term": "Fatigue"}
        assert treatment_target_phenotype_to_edge(
            "MONDO:0004979", "MAXO:0000058", phenotype
        ) is None


class TestGeneToEdgeWithGeneTerm:
    """Tests for gene_to_edge with gene_term.term.id upgrade."""

    def test_prefers_gene_term_id(self):
        """Test that gene_term.term.id is preferred over name."""
        gene = {
            "name": "FGFR3",
            "gene_term": {
                "preferred_term": "FGFR3",
                "term": {"id": "hgnc:3690", "label": "FGFR3"},
            },
        }
        edge = gene_to_edge("MONDO:0004979", gene)
        assert isinstance(edge, GeneToDiseaseAssociation)
        assert edge.subject == "hgnc:3690"
        assert edge.subject_category == "biolink:Gene"
        assert edge.object_category == "biolink:Disease"

    def test_falls_back_to_name(self):
        """Test fallback to HGNC.SYMBOL:name when gene_term is missing."""
        gene = {"name": "IL4", "association": "Associated"}
        edge = gene_to_edge("MONDO:0004979", gene)
        assert isinstance(edge, GeneToDiseaseAssociation)
        assert edge.subject == "HGNC.SYMBOL:IL4"

    def test_no_gene_term_no_name(self):
        """Test that None is returned when neither gene_term nor name is present."""
        gene = {"association": "Associated"}
        assert gene_to_edge("MONDO:0004979", gene) is None


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
                    "molecular_functions": [
                        {"term": {"id": "GO:0000002", "label": "Function A"}},
                    ],
                    "cellular_components": [
                        {"term": {"id": "GO:0000003", "label": "Component A"}},
                    ],
                    "chemical_entities": [
                        {"term": {"id": "CHEBI:00001", "label": "Chemical A"}},
                    ],
                    "pathways": [
                        {"term": {"id": "GO:0000004", "label": "Pathway A"}},
                    ],
                    "protein_complexes": [
                        {"term": {"id": "GO:0000005", "label": "Complex A"}},
                    ],
                },
            ],
            "treatments": [
                {
                    "name": "Treatment A",
                    "treatment_term": {
                        "term": {"id": "MAXO:0000001", "label": "Treatment A"},
                        "therapeutic_agent": [
                            {"term": {"id": "NCIT:C00001", "label": "Drug A"}},
                        ],
                    },
                    "target_phenotypes": [
                        {"term": {"id": "HP:0000003", "label": "Target Phenotype A"}},
                    ],
                },
            ],
            "genetic": [
                {"name": "GENE1", "association": "Associated"},
            ],
            "inheritance": [
                {
                    "inheritance_term": {
                        "term": {"id": "HP:0000006", "label": "Autosomal dominant"},
                    },
                },
            ],
            "infectious_agent": [
                {
                    "infectious_agent_term": {
                        "term": {"id": "NCBITaxon:813", "label": "Chlamydia trachomatis"},
                    },
                },
            ],
            "histopathology": [
                {
                    "finding_term": {
                        "term": {"id": "NCIT:C3237", "label": "Squamous Metaplasia"},
                    },
                },
            ],
            "biochemical": [
                {
                    "biomarker_term": {
                        "term": {"id": "NCIT:C20887", "label": "Mesothelin"},
                    },
                },
            ],
        }

    def test_transform_extracts_all_edges(self, sample_disorder):
        """Test that transform extracts all edge types."""
        edges = list(transform(sample_disorder))

        # 2 phenotypes + 1 cell_type + 1 location + 1 process + 1 mol_function +
        # 1 cell_component + 1 chemical + 1 pathway + 1 protein_complex +
        # 1 treatment + 1 therapeutic_agent + 1 target_phenotype +
        # 1 gene + 1 inheritance + 1 infectious_agent +
        # 1 histopathology + 1 biomarker = 18
        assert len(edges) == 18

        # All edges should be Association instances
        for edge in edges:
            assert isinstance(edge, Association)

        # Check edge types are present
        predicates = [e.predicate for e in edges]
        # phenotypes (2) + histopathology (1) = 3
        assert predicates.count("biolink:has_phenotype") == 3
        # cell_type + cellular_component + chemical_entity + protein_complex = 4
        assert predicates.count("biolink:has_participant") == 4
        # biological_process + molecular_function + pathway = 3
        assert predicates.count("biolink:affects") == 3
        assert predicates.count("biolink:disease_has_location") == 1
        # treatment + therapeutic_agent + target_phenotype = 3
        assert predicates.count("biolink:treats_or_applied_or_studied_to_treat") == 3
        assert predicates.count("biolink:contributes_to") == 1  # gene
        assert predicates.count("biolink:has_mode_of_inheritance") == 1
        assert predicates.count("biolink:causes") == 1
        assert predicates.count("biolink:has_biomarker") == 1

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


class TestExtractNodes:
    """Tests for the extract_nodes function."""

    @pytest.fixture
    def sample_disorder(self):
        """Create a sample disorder with all entity types."""
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
                        {"preferred_term": "Cell A", "term": {"id": "CL:0000001", "label": "cell a"}},
                    ],
                    "locations": [
                        {"preferred_term": "Location A", "term": {"id": "UBERON:0000001", "label": "location a"}},
                    ],
                    "biological_processes": [
                        {"preferred_term": "Process A", "term": {"id": "GO:0000001", "label": "process a"}},
                    ],
                    "molecular_functions": [
                        {"preferred_term": "Function A", "term": {"id": "GO:0000002", "label": "function a"}},
                    ],
                    "cellular_components": [
                        {"preferred_term": "Component A", "term": {"id": "GO:0000003", "label": "component a"}},
                    ],
                    "chemical_entities": [
                        {"preferred_term": "Chemical A", "term": {"id": "CHEBI:00001", "label": "chemical a"}},
                    ],
                    "pathways": [
                        {"preferred_term": "Pathway A", "term": {"id": "GO:0000004", "label": "pathway a"}},
                    ],
                    "protein_complexes": [
                        {"preferred_term": "Complex A", "term": {"id": "GO:0000005", "label": "complex a"}},
                    ],
                },
            ],
            "treatments": [
                {
                    "name": "Treatment A",
                    "treatment_term": {
                        "term": {"id": "MAXO:0000001", "label": "treatment a"},
                        "therapeutic_agent": [
                            {"preferred_term": "Drug A", "term": {"id": "NCIT:C00001", "label": "drug a"}},
                        ],
                    },
                    "target_phenotypes": [
                        {"preferred_term": "Target Phenotype A", "term": {"id": "HP:0000003", "label": "target phenotype a"}},
                    ],
                },
            ],
            "genetic": [
                {"name": "GENE1", "association": "Associated"},
            ],
            "environmental": [
                {
                    "name": "Exposure A",
                    "exposure_term": {
                        "term": {"id": "ECTO:0000001", "label": "exposure a"},
                    },
                },
            ],
            "inheritance": [
                {
                    "inheritance_term": {
                        "term": {"id": "HP:0000006", "label": "Autosomal dominant"},
                    },
                },
            ],
            "infectious_agent": [
                {
                    "name": "Agent A",
                    "infectious_agent_term": {
                        "term": {"id": "NCBITaxon:813", "label": "Chlamydia trachomatis"},
                    },
                },
            ],
            "histopathology": [
                {
                    "name": "Finding A",
                    "finding_term": {
                        "term": {"id": "NCIT:C3237", "label": "Squamous Metaplasia"},
                    },
                },
            ],
            "biochemical": [
                {
                    "name": "Biomarker A",
                    "biomarker_term": {
                        "term": {"id": "NCIT:C20887", "label": "Mesothelin"},
                    },
                },
            ],
        }

    def test_extracts_all_nodes(self, sample_disorder):
        """Test that extract_nodes yields all unique entity nodes."""
        nodes = list(extract_nodes(sample_disorder))

        # 1 disease + 2 phenotypes + 1 cell + 1 location + 1 process +
        # 1 mol_function + 1 cell_component + 1 chemical + 1 pathway +
        # 1 protein_complex + 1 treatment + 1 therapeutic_agent +
        # 1 target_phenotype + 1 gene + 1 exposure + 1 inheritance +
        # 1 infectious_agent + 1 histopathology + 1 biomarker = 20
        assert len(nodes) == 20

    def test_node_types(self, sample_disorder):
        """Test that nodes have correct biolink types."""
        nodes = list(extract_nodes(sample_disorder))
        node_by_id = {n.id: n for n in nodes}

        assert isinstance(node_by_id["MONDO:0000001"], Disease)
        assert isinstance(node_by_id["HP:0000001"], PhenotypicFeature)
        assert isinstance(node_by_id["HP:0000002"], PhenotypicFeature)
        assert isinstance(node_by_id["CL:0000001"], Cell)
        assert isinstance(node_by_id["UBERON:0000001"], AnatomicalEntity)
        assert isinstance(node_by_id["GO:0000001"], BiologicalProcess)
        assert isinstance(node_by_id["GO:0000002"], MolecularActivity)
        assert isinstance(node_by_id["GO:0000003"], CellularComponent)
        assert isinstance(node_by_id["CHEBI:00001"], ChemicalEntity)
        assert isinstance(node_by_id["GO:0000004"], Pathway)
        assert isinstance(node_by_id["GO:0000005"], MacromolecularComplex)
        assert isinstance(node_by_id["MAXO:0000001"], Treatment)
        assert isinstance(node_by_id["NCIT:C00001"], ChemicalEntity)
        assert isinstance(node_by_id["HP:0000003"], PhenotypicFeature)
        assert isinstance(node_by_id["HGNC.SYMBOL:GENE1"], Gene)
        assert isinstance(node_by_id["ECTO:0000001"], ExposureEvent)
        assert isinstance(node_by_id["HP:0000006"], GeneticInheritance)
        assert isinstance(node_by_id["NCBITaxon:813"], OrganismTaxon)
        assert isinstance(node_by_id["NCIT:C3237"], PhenotypicFeature)
        assert isinstance(node_by_id["NCIT:C20887"], MolecularEntity)

    def test_node_names(self, sample_disorder):
        """Test that nodes have correct names."""
        nodes = list(extract_nodes(sample_disorder))
        node_by_id = {n.id: n for n in nodes}

        # Disease uses record name
        assert node_by_id["MONDO:0000001"].name == "Test Disorder"
        # Phenotype uses name field
        assert node_by_id["HP:0000001"].name == "Phenotype A"
        # Cell type uses preferred_term
        assert node_by_id["CL:0000001"].name == "Cell A"
        # Treatment uses treatment name
        assert node_by_id["MAXO:0000001"].name == "Treatment A"
        # Gene uses gene name
        assert node_by_id["HGNC.SYMBOL:GENE1"].name == "GENE1"

    def test_node_provided_by(self, sample_disorder):
        """Test that all nodes have provided_by set."""
        nodes = list(extract_nodes(sample_disorder))
        for node in nodes:
            assert node.provided_by == [KNOWLEDGE_SOURCE]

    def test_node_categories(self, sample_disorder):
        """Test that node categories are auto-populated by biolink model."""
        nodes = list(extract_nodes(sample_disorder))
        node_by_id = {n.id: n for n in nodes}

        assert "biolink:Disease" in node_by_id["MONDO:0000001"].category
        assert "biolink:PhenotypicFeature" in node_by_id["HP:0000001"].category
        assert "biolink:Cell" in node_by_id["CL:0000001"].category
        assert "biolink:Gene" in node_by_id["HGNC.SYMBOL:GENE1"].category

    def test_deduplicates_nodes(self):
        """Test that duplicate term IDs only produce one node."""
        disorder = {
            "name": "Test Disorder",
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "test"}},
            "phenotypes": [
                {"name": "Pheno A", "phenotype_term": {"term": {"id": "HP:0000001"}}},
            ],
            "treatments": [
                {
                    "name": "Treatment A",
                    "treatment_term": {"term": {"id": "MAXO:0000001"}},
                    "target_phenotypes": [
                        # Same HP term as phenotype above - should not produce duplicate
                        {"term": {"id": "HP:0000001", "label": "Pheno A"}},
                    ],
                },
            ],
        }
        nodes = list(extract_nodes(disorder))
        ids = [n.id for n in nodes]
        assert ids.count("HP:0000001") == 1

    def test_missing_disease_term(self):
        """Test that extract_nodes returns nothing if disease_term is missing."""
        disorder = {"name": "Test Disorder", "phenotypes": []}
        nodes = list(extract_nodes(disorder))
        assert len(nodes) == 0

    def test_skips_entries_without_term_ids(self):
        """Test that entries without term IDs are skipped."""
        disorder = {
            "name": "Test Disorder",
            "disease_term": {"term": {"id": "MONDO:0000001"}},
            "phenotypes": [
                {"name": "Complete", "phenotype_term": {"term": {"id": "HP:0000001"}}},
                {"name": "Incomplete"},  # No phenotype_term
            ],
        }
        nodes = list(extract_nodes(disorder))
        ids = [n.id for n in nodes]
        assert "MONDO:0000001" in ids
        assert "HP:0000001" in ids
        assert len(nodes) == 2  # disease + 1 valid phenotype

    def test_gene_prefers_gene_term_id(self):
        """Test that gene nodes prefer gene_term.term.id over HGNC.SYMBOL."""
        disorder = {
            "name": "Test Disorder",
            "disease_term": {"term": {"id": "MONDO:0000001"}},
            "genetic": [
                {
                    "name": "FGFR3",
                    "gene_term": {
                        "preferred_term": "FGFR3",
                        "term": {"id": "hgnc:3690", "label": "FGFR3"},
                    },
                },
            ],
        }
        nodes = list(extract_nodes(disorder))
        node_by_id = {n.id: n for n in nodes}
        assert "hgnc:3690" in node_by_id
        assert "HGNC.SYMBOL:FGFR3" not in node_by_id
        assert isinstance(node_by_id["hgnc:3690"], Gene)
