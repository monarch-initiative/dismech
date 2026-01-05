from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )

    @model_serializer(mode='wrap', when_used='unless-none')
    def treat_empty_lists_as_none(
            self, handler: SerializerFunctionWrapHandler,
            info: SerializationInfo) -> dict[str, Any]:
        if info.exclude_none:
            _instance = self.model_copy()
            for field, field_info in type(_instance).model_fields.items():
                if getattr(_instance, field) == [] and not(
                        field_info.is_required()):
                    setattr(_instance, field, None)
        else:
            _instance = self
        return handler(_instance, info)



class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'dismech',
     'description': 'Disease Pathophysiology Knowledge Base Schema',
     'id': 'https://w3id.org/monarch-initiative/dismech',
     'imports': ['linkml:types'],
     'license': 'BSD-3-Clause',
     'name': 'dismech',
     'prefixes': {'CHEBI': {'prefix_prefix': 'CHEBI',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/CHEBI_'},
                  'CL': {'prefix_prefix': 'CL',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/CL_'},
                  'ECTO': {'prefix_prefix': 'ECTO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/ECTO_'},
                  'ENVO': {'prefix_prefix': 'ENVO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/ENVO_'},
                  'ExO': {'prefix_prefix': 'ExO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/ExO_'},
                  'GENO': {'prefix_prefix': 'GENO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/GENO_'},
                  'GO': {'prefix_prefix': 'GO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/GO_'},
                  'HGNC': {'prefix_prefix': 'HGNC',
                           'prefix_reference': 'https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/'},
                  'HP': {'prefix_prefix': 'HP',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/HP_'},
                  'MONDO': {'prefix_prefix': 'MONDO',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/MONDO_'},
                  'NCBITaxon': {'prefix_prefix': 'NCBITaxon',
                                'prefix_reference': 'http://purl.obolibrary.org/obo/NCBITaxon_'},
                  'OBI': {'prefix_prefix': 'OBI',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/OBI_'},
                  'PMID': {'prefix_prefix': 'PMID',
                           'prefix_reference': 'http://www.ncbi.nlm.nih.gov/pubmed/'},
                  'UBERON': {'prefix_prefix': 'UBERON',
                             'prefix_reference': 'http://purl.obolibrary.org/obo/UBERON_'},
                  'XCO': {'prefix_prefix': 'XCO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/XCO_'},
                  'arrayexpress': {'prefix_prefix': 'arrayexpress',
                                   'prefix_reference': 'https://www.ebi.ac.uk/biostudies/arrayexpress/studies/'},
                  'clinvar': {'prefix_prefix': 'clinvar',
                              'prefix_reference': 'https://www.ncbi.nlm.nih.gov/clinvar/variation/'},
                  'dbgap': {'prefix_prefix': 'dbgap',
                            'prefix_reference': 'https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id='},
                  'dismech': {'prefix_prefix': 'dismech',
                              'prefix_reference': 'https://w3id.org/monarch-initiative/dismech/'},
                  'encode': {'prefix_prefix': 'encode',
                             'prefix_reference': 'https://www.encodeproject.org/experiments/'},
                  'geo': {'prefix_prefix': 'geo',
                          'prefix_reference': 'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc='},
                  'gtex': {'prefix_prefix': 'gtex',
                           'prefix_reference': 'https://gtexportal.org/home/datasets/'},
                  'hca': {'prefix_prefix': 'hca',
                          'prefix_reference': 'https://data.humancellatlas.org/explore/projects/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'metabolights': {'prefix_prefix': 'metabolights',
                                   'prefix_reference': 'https://www.ebi.ac.uk/metabolights/'},
                  'phenopacket-store': {'prefix_prefix': 'phenopacket-store',
                                        'prefix_reference': 'https://github.com/monarch-initiative/phenopacket-store/tree/main/notebooks/'},
                  'pride': {'prefix_prefix': 'pride',
                            'prefix_reference': 'https://www.ebi.ac.uk/pride/archive/projects/'},
                  'sra': {'prefix_prefix': 'sra',
                          'prefix_reference': 'https://www.ncbi.nlm.nih.gov/sra/'},
                  'synapse': {'prefix_prefix': 'synapse',
                              'prefix_reference': 'https://www.synapse.org/#!Synapse:'}},
     'see_also': ['https://monarch-initiative.github.io/dismech'],
     'source_file': 'src/dismech/schema/dismech.yaml',
     'title': 'Disorder Mechanisms Knowledge Base Schema',
     'types': {'FrequencyQuantity': {'from_schema': 'https://w3id.org/monarch-initiative/dismech',
                                     'name': 'FrequencyQuantity',
                                     'typeof': 'string'},
               'PMID': {'from_schema': 'https://w3id.org/monarch-initiative/dismech',
                        'name': 'PMID',
                        'typeof': 'string'}}} )

class EvidenceItemSupportEnum(str, Enum):
    """
    The level of support for an evidence item
    """
    WRONG_STATEMENT = "WRONG_STATEMENT"
    """
    WRONG_STATEMENT
    """
    SUPPORT = "SUPPORT"
    """
    SUPPORT
    """
    REFUTE = "REFUTE"
    """
    REFUTE
    """
    NO_EVIDENCE = "NO_EVIDENCE"
    """
    NO_EVIDENCE
    """
    PARTIAL = "PARTIAL"
    """
    PARTIAL
    """


class FrequencyEnum(str, Enum):
    """
    The frequency of an event or phenomenon
    """
    FREQUENT = "FREQUENT"
    """
    Frequent
    """
    OCCASIONAL = "OCCASIONAL"
    """
    Occasional
    """
    VERY_FREQUENT = "VERY_FREQUENT"
    """
    Very frequent
    """
    VERY_RARE = "VERY_RARE"
    """
    Very rare
    """
    OBLIGATE = "OBLIGATE"
    """
    Obligate
    """


class ClinicalSignificanceEnum(str, Enum):
    """
    The clinical significance of a variant for a condition (ACMG guidelines)
    """
    PATHOGENIC = "PATHOGENIC"
    """
    pathogenic_for_condition
    """
    LIKELY_PATHOGENIC = "LIKELY_PATHOGENIC"
    """
    likely_pathogenic_for_condition
    """
    BENIGN = "BENIGN"
    """
    benign_for_condition
    """
    LIKELY_BENIGN = "LIKELY_BENIGN"
    """
    likely_benign_for_condition
    """
    UNCERTAIN_SIGNIFICANCE = "UNCERTAIN_SIGNIFICANCE"
    """
    has_uncertain_significance_for_condition
    """


class ModifierEnum(str, Enum):
    """
    Qualifiers for direction, intensity, or pathological state of a descriptor
    """
    INCREASED = "INCREASED"
    """
    Upregulated, hyperactive, elevated, or excessive
    """
    DECREASED = "DECREASED"
    """
    Downregulated, hypoactive, reduced, or deficient
    """
    ABNORMAL = "ABNORMAL"
    """
    Qualitatively abnormal (e.g., misfolding, mislocalization, malformed)
    """
    DYSREGULATED = "DYSREGULATED"
    """
    Regulation is impaired (may be increased or decreased)
    """
    ABSENT = "ABSENT"
    """
    Not occurring or not present
    """


class AssayTerm(str):
    """
    A term representing an assay
    """
    pass


class CellularComponentTerm(str):
    """
    A term representing a cellular component
    """
    pass


class BiologicalProcessTerm(str):
    """
    A term representing a biological process or pathway
    """
    pass


class ChemicalEntityTerm(str):
    """
    A term representing a chemical entity
    """
    pass


class PhenotypeTerm(str):
    """
    A term representing a phenotype or disease manifestation
    """
    pass


class AnatomicalEntityTerm(str):
    """
    A term representing an anatomical entity
    """
    pass


class TreatmentActionTerm(str):
    """
    A term representing a medical action or treatment (from MAXO)
    """
    pass


class GeographyTerm(str):
    """
    A place or location
    """
    pass


class PhaseTerm(str):
    """
    A phase or stage
    """
    pass


class TriggerTerm(str):
    """
    A trigger
    """
    pass


class GeneTerm(str):
    """
    A gene
    """
    pass


class CellTypeTerm(str):
    """
    A cell type
    """
    pass


class DiseaseTerm(str):
    """
    A disease or medical condition
    """
    pass


class ExposureTerm(str):
    """
    A term representing an exposure event (from ECTO or XCO)
    """
    pass


class EnvironmentTerm(str):
    """
    A term representing an environmental context, material, or feature (from ENVO)
    """
    pass


class OrganismTerm(str):
    """
    A term representing an organism from NCBITaxon
    """
    pass


class DatasetTypeEnum(str, Enum):
    """
    Type of dataset or data resource
    """
    MICROARRAY = "MICROARRAY"
    """
    Gene expression microarray
    """
    BULK_RNA_SEQ = "BULK_RNA_SEQ"
    """
    Bulk RNA sequencing
    """
    SINGLE_CELL_RNA_SEQ = "SINGLE_CELL_RNA_SEQ"
    """
    Single-cell RNA sequencing
    """
    SPATIAL_TRANSCRIPTOMICS = "SPATIAL_TRANSCRIPTOMICS"
    """
    Spatially resolved transcriptomics
    """
    METHYLATION = "METHYLATION"
    """
    DNA methylation profiling
    """
    CHIP_SEQ = "CHIP_SEQ"
    """
    Chromatin immunoprecipitation sequencing
    """
    ATAC_SEQ = "ATAC_SEQ"
    """
    Assay for transposase-accessible chromatin sequencing
    """
    PROTEOMICS = "PROTEOMICS"
    """
    Protein expression profiling
    """
    METABOLOMICS = "METABOLOMICS"
    """
    Metabolite profiling
    """
    GWAS = "GWAS"
    """
    Genome-wide association study
    """
    WGS = "WGS"
    """
    Whole genome sequencing
    """
    WES = "WES"
    """
    Whole exome sequencing
    """
    PHENOPACKETS = "PHENOPACKETS"
    """
    GA4GH Phenopacket collection (case-level phenotype data)
    """
    VARIANT_DATABASE = "VARIANT_DATABASE"
    """
    Curated genetic variant collection
    """



class Term(ConfiguredBaseModel):
    """
    A structured reference to an ontology term
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    id: str = Field(default=..., description="""Ontology term identifier (CURIE)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Term']} })
    label: Optional[str] = Field(default=None, description="""Human-readable label for the ontology term""", json_schema_extra = { "linkml_meta": {'comments': ['This is automatically validated by the linkml-term-validator '
                      'tool.'],
         'domain_of': ['Term']} })


class Descriptor(ConfiguredBaseModel):
    """
    Base class for structured descriptors that allow a preferred term, optional description, optional ontology term binding, and optional modifier/qualifiers for post-composition.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'description': {'description': 'A description of the '
                                                       'descriptor. This may typically '
                                                       'be redundant with the `term` '
                                                       'object, but the description is '
                                                       'more human-readable and may be '
                                                       'used to communicate nuances '
                                                       'not captured by the rigid '
                                                       'standardization of the term '
                                                       'object.',
                                        'name': 'description',
                                        'recommended': False}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional structured ontology term reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor'], 'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=[], description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })


class Qualifier(ConfiguredBaseModel):
    """
    A predicate-value pair for formal post-composition. Allows OWL-like expressivity with controlled predicates and values, both as full Descriptors.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Use for formal semantic relationships like "has_input some X"',
                      'Both predicate and value are Descriptors, allowing recursive '
                      'composition',
                      'Predicate typically uses RO (Relation Ontology) terms'],
         'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    predicate: Optional[Descriptor] = Field(default=None, description="""The relationship/predicate in a qualifier (e.g., RO:0002233 'has input')""", json_schema_extra = { "linkml_meta": {'domain_of': ['Qualifier']} })
    value: Optional[Descriptor] = Field(default=None, description="""The value/filler in a qualifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Qualifier']} })


class CellTypeDescriptor(Descriptor):
    """
    A descriptor for cell types, bindable to Cell Ontology (CL)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'CellTypeTerm'}],
                                 'description': 'Optional Cell Ontology term reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional Cell Ontology term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'CellTypeTerm'}],
         'domain_of': ['Descriptor'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=[], description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })


class BiologicalProcessDescriptor(Descriptor):
    """
    A descriptor for biological processes, bindable to Gene Ontology (GO)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'description': 'Optional GO biological process term '
                                                'reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional GO biological process term reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor'], 'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=[], description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })


class AnatomicalEntityDescriptor(Descriptor):
    """
    A descriptor for anatomical locations, bindable to UBERON
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'description': 'Optional UBERON anatomical entity '
                                                'term reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional UBERON anatomical entity term reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor'], 'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=[], description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })


class ChemicalEntityDescriptor(Descriptor):
    """
    A descriptor for chemical entities, bindable to CHEBI
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'description': 'Optional CHEBI chemical entity term '
                                                'reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional CHEBI chemical entity term reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor'], 'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=[], description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })


class GeneDescriptor(Descriptor):
    """
    A descriptor for genes, bindable to HGNC or other gene databases
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'description': 'Optional gene database term reference '
                                                '(e.g., HGNC)',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional gene database term reference (e.g., HGNC)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor'], 'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=[], description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })


class CellularComponentDescriptor(Descriptor):
    """
    A descriptor for cellular components, bindable to GO cellular component
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'description': 'Optional GO cellular component term '
                                                'reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional GO cellular component term reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor'], 'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=[], description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })


class AssayDescriptor(Descriptor):
    """
    A descriptor for assays, bindable to OBI
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'description': 'Optional OBI assay term reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional OBI assay term reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor'], 'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=[], description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })


class TriggerDescriptor(Descriptor):
    """
    A descriptor for triggers/causes
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'description': 'Optional ontology term reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional ontology term reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor'], 'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=[], description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })


class DiseaseDescriptor(Descriptor):
    """
    A descriptor for the focal disease, bindable to MONDO
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'DiseaseTerm'}],
                                 'description': 'Optional MONDO disease term reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional MONDO disease term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'DiseaseTerm'}],
         'domain_of': ['Descriptor'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=[], description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })


class PhenotypeDescriptor(Descriptor):
    """
    A descriptor for phenotypes, bindable to Human Phenotype Ontology (HP)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'PhenotypeTerm'}],
                                 'description': 'Optional HP phenotype term reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional HP phenotype term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'PhenotypeTerm'}],
         'domain_of': ['Descriptor'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=[], description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })


class TreatmentDescriptor(Descriptor):
    """
    A descriptor for treatments/medical actions, bindable to Medical Action Ontology (MAXO)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'TreatmentActionTerm'}],
                                 'description': 'Optional MAXO treatment term '
                                                'reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional MAXO treatment term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'TreatmentActionTerm'}],
         'domain_of': ['Descriptor'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=[], description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })


class ExposureDescriptor(Descriptor):
    """
    A descriptor for exposure events, bindable to ECTO or XCO
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Use ECTO (Environmental Conditions, Treatments, and Exposures '
                      'Ontology) for general exposures',
                      'Use XCO (Experimental Conditions Ontology) for experimental '
                      'exposure conditions'],
         'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'ExposureTerm'}],
                                 'description': 'Optional ECTO/XCO exposure term '
                                                'reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional ECTO/XCO exposure term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'ExposureTerm'}],
         'domain_of': ['Descriptor'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=[], description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })


class EnvironmentDescriptor(Descriptor):
    """
    A descriptor for environmental contexts/settings, bindable to ENVO
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Use ENVO (Environment Ontology) for habitats, biomes, and '
                      'environmental features'],
         'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'EnvironmentTerm'}],
                                 'description': 'Optional ENVO environment term '
                                                'reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional ENVO environment term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'EnvironmentTerm'}],
         'domain_of': ['Descriptor'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=[], description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })


class OrganismDescriptor(Descriptor):
    """
    A descriptor for organisms, bindable to NCBITaxon
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'term': {'bindings': [{'binds_value_of': 'id',
                                               'obligation_level': 'REQUIRED',
                                               'range': 'OrganismTerm'}],
                                 'description': 'NCBITaxon term reference',
                                 'name': 'term'}}})

    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""NCBITaxon term reference""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'OrganismTerm'}],
         'domain_of': ['Descriptor'],
         'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=[], description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })


class SampleTypeDescriptor(Descriptor):
    """
    A descriptor for biological sample types (tissue and/or cell type)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    tissue_term: Optional[AnatomicalEntityDescriptor] = Field(default=None, description="""UBERON term for the tissue""", json_schema_extra = { "linkml_meta": {'domain_of': ['SampleTypeDescriptor']} })
    cell_type_term: Optional[CellTypeDescriptor] = Field(default=None, description="""CL term for the cell type""", json_schema_extra = { "linkml_meta": {'domain_of': ['SampleTypeDescriptor']} })
    preferred_term: str = Field(default=..., description="""The preferred human-readable term for this descriptor""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, description="""A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration'],
         'recommended': False} })
    term: Optional[Term] = Field(default=None, description="""Optional structured ontology term reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor'], 'recommended': True} })
    modifier: Optional[ModifierEnum] = Field(default=None, description="""Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })
    qualifiers: Optional[list[Qualifier]] = Field(default=[], description="""List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor']} })


class Dataset(ConfiguredBaseModel):
    """
    A reference to a publicly available omics or phenotype dataset
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Supports GEO, ArrayExpress, SRA, dbGaP, GTEx, ENCODE, '
                      'phenopacket-store, and other repositories'],
         'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'description': {'description': 'A description of the dataset. '
                                                       'This may typically be '
                                                       'redundant with the `title` '
                                                       'slot, but the description is '
                                                       'more human-readable and may be '
                                                       'used to communicate nuances '
                                                       'not captured by the rigid '
                                                       'standardization of the title '
                                                       'slot.',
                                        'name': 'description',
                                        'recommended': True}}})

    accession: str = Field(default=..., description="""Dataset accession identifier as a CURIE (e.g., geo:GSE67472)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    title: Optional[str] = Field(default=None, description="""Title of the publication""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'PublicationReference']} })
    description: Optional[str] = Field(default=None, description="""A description of the dataset. This may typically be redundant with the `title` slot, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the title slot.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration'],
         'recommended': True} })
    organism: Optional[OrganismDescriptor] = Field(default=None, description="""The organism from which samples were derived""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    data_type: Optional[DatasetTypeEnum] = Field(default=None, description="""The type of omics or other data in the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    sample_types: Optional[list[SampleTypeDescriptor]] = Field(default=[], description="""Types of biological samples in the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    sample_count: Optional[int] = Field(default=None, description="""Total number of samples in the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    conditions: Optional[list[str]] = Field(default=[], description="""Experimental conditions or disease states represented""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    exposures: Optional[list[ExposureDescriptor]] = Field(default=[], description="""Environmental exposures studied in the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    genes: Optional[list[GeneDescriptor]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'Pathophysiology', 'AnimalModel'],
         'examples': [{'value': '[{preferred_term: HLA-DQ2}, {preferred_term: INS}]'}]} })
    platform: Optional[str] = Field(default=None, description="""Sequencing or array platform used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    publication: Optional[str] = Field(default=None, description="""Associated publication (PMID)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Subtype',
                       'CausalEdge',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class Subtype(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    subtype_term: Optional[DiseaseDescriptor] = Field(default=None, description="""The MONDO term for a disease subtype""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Subtype',
                       'CausalEdge',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration'],
         'recommended': True} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype',
                       'ProgressionInfo',
                       'Phenotype',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment'],
         'examples': [{'value': 'Added an additional clinically relevant subtype.'}]} })
    locations: Optional[list[AnatomicalEntityDescriptor]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype', 'Pathophysiology']} })
    geography: Optional[list[GeographyTerm]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype'], 'examples': [{'value': "['Philippines']"}]} })


class EvidenceItem(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    reference: Optional[str] = Field(default=None, description="""The authoritative reference (publication) for this evidence item""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem', 'PublicationReference'],
         'examples': [{'value': 'PMID:35533128'}],
         'implements': ['linkml:authoritative_reference']} })
    supports: Optional[EvidenceItemSupportEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem'], 'examples': [{'value': 'SUPPORT'}]} })
    snippet: Optional[str] = Field(default=None, description="""An exact excerpt/quote from the referenced publication that supports or refutes the claim""", json_schema_extra = { "linkml_meta": {'comments': ['This is automatically validated by the '
                      'linkml-reference-validator tool.'],
         'domain_of': ['EvidenceItem'],
         'examples': [{'value': 'At the moment there is no healing therapy, so early '
                                'kidney transplant is a fundamental tool to improve '
                                'prognosis.'}],
         'implements': ['linkml:excerpt']} })
    explanation: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem'],
         'examples': [{'value': 'There is no curative treatment for nephronophthisis, '
                                'indicating that supportive care, including '
                                'symptomatic treatment and monitoring, is currently '
                                'applied to manage associated complications.'}]} })


class CausalEdge(ConfiguredBaseModel):
    """
    A reference to a downstream effect or consequence in a causal relationship
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    target: str = Field(default=..., description="""The name of the target element in a causal relationship""", json_schema_extra = { "linkml_meta": {'domain_of': ['CausalEdge']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Subtype',
                       'CausalEdge',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration'],
         'recommended': True} })


class PublicationReference(ConfiguredBaseModel):
    """
    A reference to a publication with associated findings
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'slot_usage': {'reference': {'identifier': True,
                                      'name': 'reference',
                                      'required': True}}})

    reference: str = Field(default=..., description="""The authoritative reference (publication) for this evidence item""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem', 'PublicationReference'],
         'examples': [{'value': 'PMID:35533128'}],
         'implements': ['linkml:authoritative_reference']} })
    title: Optional[str] = Field(default=None, description="""Title of the publication""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'PublicationReference']} })
    findings: Optional[list[Finding]] = Field(default=[], description="""Key findings or claims extracted from this reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['PublicationReference']} })


class Finding(ConfiguredBaseModel):
    """
    A key finding or claim extracted from a publication
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    statement: str = Field(default=..., description="""A key finding or claim from the publication""", json_schema_extra = { "linkml_meta": {'domain_of': ['Finding']} })
    supporting_text: Optional[str] = Field(default=None, description="""Exact excerpt/quote from the publication supporting the statement""", json_schema_extra = { "linkml_meta": {'domain_of': ['Finding']} })


class Prevalence(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    subtype: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Prevalence',
                       'ProgressionInfo',
                       'Phenotype',
                       'Biochemical',
                       'Genetic'],
         'examples': [{'value': 'Eyelid Myoclonia with Absences'}]} })
    population: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Prevalence'], 'examples': [{'value': 'Global'}]} })
    percentage: Optional[Union[float, int, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'float'},
                    {'range': 'integer'},
                    {'description': 'for ranges', 'range': 'string'}],
         'domain_of': ['Prevalence'],
         'examples': [{'value': '0.1'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Subtype',
                       'CausalEdge',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })


class ProgressionInfo(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    phase: Optional[PhaseTerm] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ProgressionInfo'], 'examples': [{'value': 'Active TB'}]} })
    subtype: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Prevalence',
                       'ProgressionInfo',
                       'Phenotype',
                       'Biochemical',
                       'Genetic'],
         'examples': [{'value': 'Eyelid Myoclonia with Absences'}]} })
    age_range: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ProgressionInfo'],
         'examples': [{'value': 'Childhood-Adolescence'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Subtype',
                       'CausalEdge',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration'],
         'recommended': True} })
    incubation_days: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ProgressionInfo'], 'examples': [{'value': '3-14'}]} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype',
                       'ProgressionInfo',
                       'Phenotype',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment'],
         'examples': [{'value': 'Added an additional clinically relevant subtype.'}]} })
    incubation_years: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ProgressionInfo'], 'examples': [{'value': '2-15'}]} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    duration_days: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ProgressionInfo'], 'examples': [{'value': '2-5'}]} })
    duration: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ProgressionInfo'], 'examples': [{'value': 'Variable'}]} })


class EpidemiologyInfo(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration']} })
    minimum_value: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EpidemiologyInfo']} })
    maximum_value: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EpidemiologyInfo']} })
    mean_range: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EpidemiologyInfo']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    factors: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['EpidemiologyInfo'],
         'examples': [{'value': "['Genetic', 'Environmental', 'Infectious', "
                                "'Autoimmune', 'Metabolic', 'Neoplastic', 'Traumatic', "
                                "'Iatrogenic', 'Idiopathic']"}]} })
    unit: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EpidemiologyInfo'], 'examples': [{'value': 'cm'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Subtype',
                       'CausalEdge',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration'],
         'recommended': True} })


class Pathophysiology(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration']} })
    cell_types: Optional[list[CellTypeDescriptor]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology', 'Biochemical'],
         'examples': [{'value': '[{preferred_term: Macrophage}, {preferred_term: T '
                                'Cell}]'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Subtype',
                       'CausalEdge',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration'],
         'recommended': True} })
    biological_processes: Optional[list[BiologicalProcessDescriptor]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology'],
         'examples': [{'value': '[{preferred_term: TNF-alpha Production}]'}]} })
    locations: Optional[list[AnatomicalEntityDescriptor]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype', 'Pathophysiology']} })
    examples: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'Treatment'],
         'examples': [{'value': "['Kaposi Sarcoma']"}]} })
    role: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology', 'Stage', 'Treatment'],
         'examples': [{'value': 'Primary'}]} })
    synonyms: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology',
                       'Biochemical',
                       'Environmental',
                       'Disease',
                       'Variant'],
         'examples': [{'value': "['CYFRA 21-1']"}]} })
    consequence: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology'],
         'examples': [{'value': 'Leads to abnormal sexual development and bone '
                                'maturation.'}]} })
    consequences: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology'],
         'todos': ['unify consequences and consequence']} })
    gene: Optional[GeneDescriptor] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology', 'Variant'],
         'examples': [{'value': '{preferred_term: MEFV}'}]} })
    pathways: Optional[list[BiologicalProcessDescriptor]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology'],
         'examples': [{'value': '[{preferred_term: Wnt Pathway}]'}]} })
    downstream: Optional[list[CausalEdge]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology'],
         'examples': [{'value': '[{target: Tissue Damage}]'}]} })
    genes: Optional[list[GeneDescriptor]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'Pathophysiology', 'AnimalModel'],
         'examples': [{'value': '[{preferred_term: HLA-DQ2}, {preferred_term: INS}]'}]} })
    subtypes: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology'],
         'examples': [{'value': "['DENV-1', 'DENV-2', 'DENV-3', 'DENV-4']"}]} })
    cellular_components: Optional[list[CellularComponentDescriptor]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology'],
         'examples': [{'value': '[{preferred_term: Peroxisome}]'}]} })
    chemical_entities: Optional[list[ChemicalEntityDescriptor]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology'],
         'examples': [{'value': '[{preferred_term: Plasmalogen}]'}]} })
    triggers: Optional[list[TriggerDescriptor]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology'],
         'examples': [{'value': '[{preferred_term: Viral Infections}]'}]} })
    assays: Optional[list[AssayDescriptor]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology', 'Biochemical'],
         'examples': [{'value': '[{preferred_term: Elevated Blood Glucose}]'}]} })
    mechanisms: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology'],
         'examples': [{'value': "['Thrombocytopenia', 'Platelet Dysfunction', "
                                "'Disseminated Intravascular Coagulation (DIC)']"}]} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    frequency: Optional[Union[FrequencyEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'FrequencyEnum'}, {'range': 'FrequencyQuantity'}],
         'domain_of': ['Pathophysiology', 'Phenotype', 'Biochemical', 'Genetic'],
         'examples': [{'value': 'Occasional'}]} })


class Phenotype(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    category: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype', 'Disease', 'AnimalModel'],
         'examples': [{'value': 'Hematologic'}]} })
    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    phenotype_term: Optional[PhenotypeDescriptor] = Field(default=None, description="""The HP term for this phenotype""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    frequency: Optional[Union[FrequencyEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'FrequencyEnum'}, {'range': 'FrequencyQuantity'}],
         'domain_of': ['Pathophysiology', 'Phenotype', 'Biochemical', 'Genetic'],
         'examples': [{'value': 'Occasional'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration']} })
    diagnostic: Optional[bool] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    sequelae: Optional[list[CausalEdge]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype'],
         'examples': [{'value': '[{target: Diabetic Ketoacidosis}, {target: Chronic '
                                'Complications}]'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Subtype',
                       'CausalEdge',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration'],
         'recommended': True} })
    context: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype', 'Biochemical', 'Stage', 'Treatment'],
         'examples': [{'value': 'Pregnancy'}]} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype',
                       'ProgressionInfo',
                       'Phenotype',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment'],
         'examples': [{'value': 'Added an additional clinically relevant subtype.'}]} })
    severity: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype'], 'examples': [{'value': 'Severe'}]} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    subtype: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Prevalence',
                       'ProgressionInfo',
                       'Phenotype',
                       'Biochemical',
                       'Genetic'],
         'examples': [{'value': 'Eyelid Myoclonia with Absences'}]} })


class Biochemical(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    biomarker_term: Optional[Descriptor] = Field(default=None, description="""Ontology term for a biomarker (from NCIT, CHEBI, or LOINC)""", json_schema_extra = { "linkml_meta": {'comments': ['Biomarkers may come from multiple ontologies (NCIT for '
                      'proteins, CHEBI for chemicals, LOINC for lab tests)'],
         'domain_of': ['Biochemical']} })
    presence: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Biochemical', 'Genetic', 'Environmental', 'Diagnosis'],
         'examples': [{'value': 'Positive'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Subtype',
                       'CausalEdge',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration'],
         'recommended': True} })
    specificity: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Biochemical'], 'examples': [{'value': 'High'}]} })
    frequency: Optional[Union[FrequencyEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'FrequencyEnum'}, {'range': 'FrequencyQuantity'}],
         'domain_of': ['Pathophysiology', 'Phenotype', 'Biochemical', 'Genetic'],
         'examples': [{'value': 'Occasional'}]} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    context: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype', 'Biochemical', 'Stage', 'Treatment'],
         'examples': [{'value': 'Pregnancy'}]} })
    subtype: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Prevalence',
                       'ProgressionInfo',
                       'Phenotype',
                       'Biochemical',
                       'Genetic'],
         'examples': [{'value': 'Eyelid Myoclonia with Absences'}]} })
    cell_types: Optional[list[CellTypeDescriptor]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology', 'Biochemical'],
         'examples': [{'value': '[{preferred_term: Macrophage}, {preferred_term: T '
                                'Cell}]'}]} })
    assays: Optional[list[AssayDescriptor]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology', 'Biochemical'],
         'examples': [{'value': '[{preferred_term: Elevated Blood Glucose}]'}]} })
    synonyms: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology',
                       'Biochemical',
                       'Environmental',
                       'Disease',
                       'Variant'],
         'examples': [{'value': "['CYFRA 21-1']"}]} })


class Genetic(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    presence: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Biochemical', 'Genetic', 'Environmental', 'Diagnosis'],
         'examples': [{'value': 'Positive'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Subtype',
                       'CausalEdge',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration'],
         'recommended': True} })
    association: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Genetic'], 'examples': [{'value': 'Susceptibility'}]} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype',
                       'ProgressionInfo',
                       'Phenotype',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment'],
         'examples': [{'value': 'Added an additional clinically relevant subtype.'}]} })
    subtype: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Prevalence',
                       'ProgressionInfo',
                       'Phenotype',
                       'Biochemical',
                       'Genetic'],
         'examples': [{'value': 'Eyelid Myoclonia with Absences'}]} })
    frequency: Optional[Union[FrequencyEnum, str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'FrequencyEnum'}, {'range': 'FrequencyQuantity'}],
         'domain_of': ['Pathophysiology', 'Phenotype', 'Biochemical', 'Genetic'],
         'examples': [{'value': 'Occasional'}]} })
    inheritance: Optional[list[Inheritance]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Genetic', 'Disease'],
         'examples': [{'value': 'Autosomal Dominant'}]} })
    variants: Optional[list[Variant]] = Field(default=[], json_schema_extra = { "linkml_meta": {'comments': ['can currently be used at gene or disease level, TODO - decide '
                      'the best level'],
         'domain_of': ['Genetic', 'Disease']} })
    features: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Genetic'],
         'examples': [{'value': 'DNA virus from the Orthopoxvirus genus'}]} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    examples: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'Treatment'],
         'examples': [{'value': "['Kaposi Sarcoma']"}]} })


class Environmental(ConfiguredBaseModel):
    """
    An environmental factor, exposure, or context relevant to disease
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    presence: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Biochemical', 'Genetic', 'Environmental', 'Diagnosis'],
         'examples': [{'value': 'Positive'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Subtype',
                       'CausalEdge',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration']} })
    chemicals: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Environmental'], 'examples': [{'value': "['Phenol']"}]} })
    synonyms: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology',
                       'Biochemical',
                       'Environmental',
                       'Disease',
                       'Variant'],
         'examples': [{'value': "['CYFRA 21-1']"}]} })
    effect: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Environmental', 'Transmission'],
         'examples': [{'value': 'Potential trigger for flare-ups'}]} })
    examples: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'Treatment'],
         'examples': [{'value': "['Kaposi Sarcoma']"}]} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype',
                       'ProgressionInfo',
                       'Phenotype',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment'],
         'examples': [{'value': 'Added an additional clinically relevant subtype.'}]} })
    exposure_term: Optional[ExposureDescriptor] = Field(default=None, description="""The ECTO/XCO term for this exposure event""", json_schema_extra = { "linkml_meta": {'domain_of': ['Environmental']} })
    environment_context: Optional[EnvironmentDescriptor] = Field(default=None, description="""The ENVO term for the environmental context/setting""", json_schema_extra = { "linkml_meta": {'domain_of': ['Environmental']} })


class Disease(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    disease_term: Optional[DiseaseDescriptor] = Field(default=None, description="""The MONDO disease term for this disease""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration']} })
    references: Optional[list[PublicationReference]] = Field(default=[], description="""Top-level list of references with their key findings for this disease""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    category: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype', 'Disease', 'AnimalModel'],
         'examples': [{'value': 'Hematologic'}]} })
    parents: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Disease'], 'examples': [{'value': "['Bacterial Infection']"}]} })
    has_subtypes: Optional[list[Subtype]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'InfectiousAgent']} })
    prevalence: Optional[list[Prevalence]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    progression: Optional[list[ProgressionInfo]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    pathophysiology: Optional[list[Pathophysiology]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Stage']} })
    phenotypes: Optional[list[Phenotype]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    biochemical: Optional[list[Biochemical]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    stages: Optional[list[Stage]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    genetic: Optional[list[Genetic]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    variants: Optional[list[Variant]] = Field(default=[], json_schema_extra = { "linkml_meta": {'comments': ['can currently be used at gene or disease level, TODO - decide '
                      'the best level'],
         'domain_of': ['Genetic', 'Disease']} })
    environmental: Optional[list[Environmental]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    treatments: Optional[list[Treatment]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    categories: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    infectious_agent: Optional[list[InfectiousAgent]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    transmission: Optional[list[Transmission]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    modeling_considerations: Optional[list[ModelingConsideration]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    epidemiology: Optional[list[EpidemiologyInfo]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Disease'], 'examples': [{'value': "['Global']"}]} })
    diagnosis: Optional[list[Diagnosis]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    synonyms: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology',
                       'Biochemical',
                       'Environmental',
                       'Disease',
                       'Variant'],
         'examples': [{'value': "['CYFRA 21-1']"}]} })
    inheritance: Optional[list[Inheritance]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Genetic', 'Disease'],
         'examples': [{'value': 'Autosomal Dominant'}]} })
    animal_models: Optional[list[AnimalModel]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    datasets: Optional[list[Dataset]] = Field(default=[], description="""Publicly available datasets relevant to disease research""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease'], 'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype',
                       'ProgressionInfo',
                       'Phenotype',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment'],
         'examples': [{'value': 'Added an additional clinically relevant subtype.'}]} })


class Stage(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Subtype',
                       'CausalEdge',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    context: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype', 'Biochemical', 'Stage', 'Treatment'],
         'examples': [{'value': 'Pregnancy'}]} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype',
                       'ProgressionInfo',
                       'Phenotype',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment'],
         'examples': [{'value': 'Added an additional clinically relevant subtype.'}]} })
    role: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology', 'Stage', 'Treatment'],
         'examples': [{'value': 'Primary'}]} })
    examples: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'Treatment'],
         'examples': [{'value': "['Kaposi Sarcoma']"}]} })
    pathophysiology: Optional[list[Pathophysiology]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Stage']} })
    substages: Optional[list[Stage]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Stage']} })


class AnimalModel(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    species: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['AnimalModel'], 'examples': [{'value': 'Human'}]} })
    genotype: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['AnimalModel'], 'examples': [{'value': 'HLA-DQ2'}]} })
    background: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['AnimalModel']} })
    genes: Optional[list[GeneDescriptor]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'Pathophysiology', 'AnimalModel'],
         'examples': [{'value': '[{preferred_term: HLA-DQ2}, {preferred_term: INS}]'}]} })
    category: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype', 'Disease', 'AnimalModel'],
         'examples': [{'value': 'Hematologic'}]} })
    alleles: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['AnimalModel']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration']} })
    associated_phenotypes: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['AnimalModel'],
         'examples': [{'value': "['Celiac Disease', 'Type 1 Diabetes', 'Autoimmune "
                                "Thyroid Disease']"}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Subtype',
                       'CausalEdge',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration'],
         'recommended': True} })


class Treatment(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration']} })
    treatment_term: Optional[TreatmentDescriptor] = Field(default=None, description="""The MAXO term for this treatment/medical action""", json_schema_extra = { "linkml_meta": {'domain_of': ['Treatment']} })
    target_phenotypes: Optional[list[str]] = Field(default=[], description="""Names of phenotypes that this treatment addresses or targets""", json_schema_extra = { "linkml_meta": {'comments': ["Should reference phenotype names defined in the same disease's "
                      'phenotypes list',
                      'Enables linking treatments to the symptoms/manifestations they '
                      'aim to manage'],
         'domain_of': ['Treatment']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Subtype',
                       'CausalEdge',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    context: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype', 'Biochemical', 'Stage', 'Treatment'],
         'examples': [{'value': 'Pregnancy'}]} })
    review_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype',
                       'ProgressionInfo',
                       'Phenotype',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment'],
         'examples': [{'value': 'Added an additional clinically relevant subtype.'}]} })
    role: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology', 'Stage', 'Treatment'],
         'examples': [{'value': 'Primary'}]} })
    mechanism: Optional[list[Mechanism]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Treatment']} })
    examples: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'Treatment'],
         'examples': [{'value': "['Kaposi Sarcoma']"}]} })


class InfectiousAgent(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Subtype',
                       'CausalEdge',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration'],
         'recommended': True} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration']} })
    has_subtypes: Optional[list[Subtype]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'InfectiousAgent']} })


class Transmission(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Subtype',
                       'CausalEdge',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    effect: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Environmental', 'Transmission'],
         'examples': [{'value': 'Potential trigger for flare-ups'}]} })


class Assay(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration']} })


class Diagnosis(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    diagnosis_term: Optional[TreatmentDescriptor] = Field(default=None, description="""The MAXO term for this diagnostic procedure""", json_schema_extra = { "linkml_meta": {'comments': ['MAXO includes diagnostic procedures under medical actions',
                      'Use qualifiers with UBERON terms to specify anatomical location '
                      '(e.g., right heart catheterization)'],
         'domain_of': ['Diagnosis']} })
    presence: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Biochemical', 'Genetic', 'Environmental', 'Diagnosis'],
         'examples': [{'value': 'Positive'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Subtype',
                       'CausalEdge',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration'],
         'recommended': True} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'Transmission',
                       'Diagnosis'],
         'examples': [{'value': 'Contagious stage where symptoms appear and the '
                                'bacteria can be spread to others.'}]} })
    results: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Diagnosis'],
         'examples': [{'value': 'Identifies MEFV mutations'}]} })
    markers: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Diagnosis'], 'examples': [{'value': 'CRP, ESR, SAA'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration']} })


class Inheritance(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Subtype',
                       'CausalEdge',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration'],
         'recommended': True} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration']} })


class Variant(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration']} })
    gene: Optional[GeneDescriptor] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology', 'Variant'],
         'examples': [{'value': '{preferred_term: MEFV}'}]} })
    evidence: Optional[list[EvidenceItem]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Subtype',
                       'CausalEdge',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration'],
         'recommended': True} })
    functional_effects: Optional[list[FunctionalEffect]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Variant']} })
    synonyms: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Pathophysiology',
                       'Biochemical',
                       'Environmental',
                       'Disease',
                       'Variant'],
         'examples': [{'value': "['CYFRA 21-1']"}]} })
    identifiers: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Variant']} })
    sequence_length: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Variant']} })
    clinical_significance: Optional[ClinicalSignificanceEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Variant']} })
    type: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Variant', 'FunctionalEffect']} })


class FunctionalEffect(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    function: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['FunctionalEffect']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration']} })
    type: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Variant', 'FunctionalEffect']} })


class Mechanism(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration']} })


class ModelingConsideration(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Subtype',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'Mechanism',
                       'ModelingConsideration'],
         'examples': [{'value': 'Adolescent Nephronophthisis'}]} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Descriptor',
                       'Dataset',
                       'Subtype',
                       'CausalEdge',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Environmental',
                       'Disease',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Assay',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'FunctionalEffect',
                       'Mechanism',
                       'ModelingConsideration']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Subtype',
                       'CausalEdge',
                       'Prevalence',
                       'ProgressionInfo',
                       'EpidemiologyInfo',
                       'Pathophysiology',
                       'Phenotype',
                       'Biochemical',
                       'Genetic',
                       'Environmental',
                       'Stage',
                       'AnimalModel',
                       'Treatment',
                       'InfectiousAgent',
                       'Transmission',
                       'Diagnosis',
                       'Inheritance',
                       'Variant',
                       'ModelingConsideration'],
         'recommended': True} })


class DiseaseCollection(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/dismech',
         'tree_root': True})

    diseases: Optional[list[Disease]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseCollection']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Term.model_rebuild()
Descriptor.model_rebuild()
Qualifier.model_rebuild()
CellTypeDescriptor.model_rebuild()
BiologicalProcessDescriptor.model_rebuild()
AnatomicalEntityDescriptor.model_rebuild()
ChemicalEntityDescriptor.model_rebuild()
GeneDescriptor.model_rebuild()
CellularComponentDescriptor.model_rebuild()
AssayDescriptor.model_rebuild()
TriggerDescriptor.model_rebuild()
DiseaseDescriptor.model_rebuild()
PhenotypeDescriptor.model_rebuild()
TreatmentDescriptor.model_rebuild()
ExposureDescriptor.model_rebuild()
EnvironmentDescriptor.model_rebuild()
OrganismDescriptor.model_rebuild()
SampleTypeDescriptor.model_rebuild()
Dataset.model_rebuild()
Subtype.model_rebuild()
EvidenceItem.model_rebuild()
CausalEdge.model_rebuild()
PublicationReference.model_rebuild()
Finding.model_rebuild()
Prevalence.model_rebuild()
ProgressionInfo.model_rebuild()
EpidemiologyInfo.model_rebuild()
Pathophysiology.model_rebuild()
Phenotype.model_rebuild()
Biochemical.model_rebuild()
Genetic.model_rebuild()
Environmental.model_rebuild()
Disease.model_rebuild()
Stage.model_rebuild()
AnimalModel.model_rebuild()
Treatment.model_rebuild()
InfectiousAgent.model_rebuild()
Transmission.model_rebuild()
Assay.model_rebuild()
Diagnosis.model_rebuild()
Inheritance.model_rebuild()
Variant.model_rebuild()
FunctionalEffect.model_rebuild()
Mechanism.model_rebuild()
ModelingConsideration.model_rebuild()
DiseaseCollection.model_rebuild()
