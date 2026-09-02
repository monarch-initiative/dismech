# Auto generated from dismech.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-08-31T23:26:40
# Schema: dismech
#
# id: https://w3id.org/monarch-initiative/dismech
# description: Disease Pathophysiology Knowledge Base Schema
# license: BSD-3-Clause

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Date, Datetime, Float, Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URI, URIorCURIE, XSDDate, XSDDateTime

metamodel_version = "1.7.0"
version = None

# Namespaces
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
CIVIC_ASSERTION = CurieNamespace('CIVIC_ASSERTION', 'https://civicdb.org/links/assertions/')
CIVIC_EID = CurieNamespace('CIVIC_EID', 'https://civicdb.org/links/evidence_items/')
CL = CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_')
ECTO = CurieNamespace('ECTO', 'http://purl.obolibrary.org/obo/ECTO_')
ENVO = CurieNamespace('ENVO', 'http://purl.obolibrary.org/obo/ENVO_')
EXO = CurieNamespace('ExO', 'http://purl.obolibrary.org/obo/ExO_')
FOODON = CurieNamespace('FOODON', 'http://purl.obolibrary.org/obo/FOODON_')
GENO = CurieNamespace('GENO', 'http://purl.obolibrary.org/obo/GENO_')
GO = CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_')
HGNC = CurieNamespace('HGNC', 'https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/')
HP = CurieNamespace('HP', 'http://purl.obolibrary.org/obo/HP_')
ICD10CM = CurieNamespace('ICD10CM', 'http://purl.obolibrary.org/obo/ICD10CM_')
ICTRP = CurieNamespace('ICTRP', 'https://trialsearch.who.int/Trial2.aspx?TrialID=')
LOINC = CurieNamespace('LOINC', 'https://loinc.org/')
MONDO = CurieNamespace('MONDO', 'http://purl.obolibrary.org/obo/MONDO_')
NCBITAXON = CurieNamespace('NCBITaxon', 'http://purl.obolibrary.org/obo/NCBITaxon_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
OPL = CurieNamespace('OPL', 'http://purl.obolibrary.org/obo/OPL_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
PMID = CurieNamespace('PMID', 'http://www.ncbi.nlm.nih.gov/pubmed/')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
XCO = CurieNamespace('XCO', 'http://purl.obolibrary.org/obo/XCO_')
ARRAYEXPRESS = CurieNamespace('arrayexpress', 'https://www.ebi.ac.uk/biostudies/arrayexpress/studies/')
BIGG = CurieNamespace('bigg', 'https://bigg.ucsd.edu/models/')
BIOMODELS = CurieNamespace('biomodels', 'https://www.ebi.ac.uk/biomodels/')
BIOPROJECT = CurieNamespace('bioproject', 'https://www.ncbi.nlm.nih.gov/bioproject/')
CELLXGENE = CurieNamespace('cellxgene', 'https://cellxgene.cziscience.com/collections/')
CLINICALTRIALS = CurieNamespace('clinicaltrials', 'https://clinicaltrials.gov/study/')
CLINVAR = CurieNamespace('clinvar', 'https://www.ncbi.nlm.nih.gov/clinvar/variation/')
DBGAP = CurieNamespace('dbgap', 'https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
DISMECH = CurieNamespace('dismech', 'https://w3id.org/monarch-initiative/dismech/')
EGA = CurieNamespace('ega', 'https://ega-archive.org/studies/')
ENCODE = CurieNamespace('encode', 'https://www.encodeproject.org/experiments/')
GEO = CurieNamespace('geo', 'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=')
GTEX = CurieNamespace('gtex', 'https://gtexportal.org/home/datasets/')
HCA = CurieNamespace('hca', 'https://data.humancellatlas.org/explore/projects/')
ICD11F = CurieNamespace('icd11f', 'http://purl.obolibrary.org/obo/icd11f_')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MASSIVE = CurieNamespace('massive', 'https://massive.ucsd.edu/ProteoSAFe/dataset.jsp?task=')
METABOLIGHTS = CurieNamespace('metabolights', 'https://www.ebi.ac.uk/metabolights/')
METABOLOMICS_WORKBENCH = CurieNamespace('metabolomics_workbench', 'https://www.metabolomicsworkbench.org/data/DRCCMetadata.php?Mode=Study&StudyID=')
MGNIFY = CurieNamespace('mgnify', 'https://www.ebi.ac.uk/metagenomics/studies/')
MORPHIC = CurieNamespace('morphic', 'https://data.morphic.bio/')
NAMO = CurieNamespace('namo', 'https://w3id.org/monarch-initiative/namo/')
OSDR = CurieNamespace('osdr', 'https://osdr.nasa.gov/bio/repo/data/studies/')
PHENOPACKET_STORE = CurieNamespace('phenopacket-store', 'https://github.com/monarch-initiative/phenopacket-store/tree/main/notebooks/')
PRIDE = CurieNamespace('pride', 'https://www.ebi.ac.uk/pride/archive/projects/')
PROTEOMEXCHANGE = CurieNamespace('proteomexchange', 'https://www.ebi.ac.uk/pride/archive/projects/')
SCEA = CurieNamespace('scea', 'https://www.ebi.ac.uk/gxa/sc/experiments/')
SEPIO = CurieNamespace('sepio', 'https://w3id.org/sepio-model/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
SRA = CurieNamespace('sra', 'https://www.ncbi.nlm.nih.gov/sra/')
SYNAPSE = CurieNamespace('synapse', 'https://www.synapse.org/#!Synapse:')
VMH = CurieNamespace('vmh', 'https://www.vmh.life/#human/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = DISMECH


# Types
class PMID(str):
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "PMID"
    type_model_uri = DISMECH.PMID


class FrequencyQuantity(str):
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "FrequencyQuantity"
    type_model_uri = DISMECH.FrequencyQuantity


# Class references
class TermId(URIorCURIE):
    pass


class DatasetAccession(URIorCURIE):
    pass


class ExperimentalModelName(extended_str):
    pass


class ExperimentName(extended_str):
    pass


class ExperimentalPerturbationName(extended_str):
    pass


class ExperimentalReadoutName(extended_str):
    pass


class ExperimentalControlName(extended_str):
    pass


class ClinicalTrialName(extended_str):
    pass


class ComputationalModelName(extended_str):
    pass


class ModelVariableName(extended_str):
    pass


class SeverityTierName(extended_str):
    pass


class DifferentialDiagnosisName(extended_str):
    pass


class SubtypeName(extended_str):
    pass


class ReferenceRangeBandName(extended_str):
    pass


class SurrogateEndpointRowId(extended_str):
    pass


class SurrogateEndpointCollectionName(extended_str):
    pass


class PublicationReferenceReference(extended_str):
    pass


class ExternalAssertionName(extended_str):
    pass


class EpidemiologyInfoName(extended_str):
    pass


class PathophysiologyName(extended_str):
    pass


class PhenotypeName(extended_str):
    pass


class BiochemicalName(extended_str):
    pass


class HistopathologyFindingName(extended_str):
    pass


class ImagingFindingName(extended_str):
    pass


class GeneticName(extended_str):
    pass


class EnvironmentalName(extended_str):
    pass


class DiseaseName(extended_str):
    pass


class StageName(extended_str):
    pass


class AgentLifeCycleStageName(extended_str):
    pass


class TreatmentName(extended_str):
    pass


class InfectiousAgentName(extended_str):
    pass


class TransmissionName(extended_str):
    pass


class AssayName(extended_str):
    pass


class DiagnosisName(extended_str):
    pass


class InheritanceName(extended_str):
    pass


class VariantName(extended_str):
    pass


class MechanismName(extended_str):
    pass


class ModelingConsiderationName(extended_str):
    pass


class DefinitionName(extended_str):
    pass


class CriteriaSetName(extended_str):
    pass


class ComorbidityAssociationName(extended_str):
    pass


class FDASurrogateEndpointCollectionName(SurrogateEndpointCollectionName):
    pass


class GroupingName(extended_str):
    pass


class ModuleCollectionName(extended_str):
    pass


Any = Any

@dataclass(repr=False)
class CurationEvent(YAMLRoot):
    """
    A single curation event in the audit trail
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["CurationEvent"]
    class_class_curie: ClassVar[str] = "dismech:CurationEvent"
    class_name: ClassVar[str] = "CurationEvent"
    class_model_uri: ClassVar[URIRef] = DISMECH.CurationEvent

    curation_timestamp: Union[str, XSDDateTime] = None
    curation_model: Optional[str] = None
    curation_action: Optional[Union[str, "CurationActionEnum"]] = None
    curation_description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.curation_timestamp):
            self.MissingRequiredField("curation_timestamp")
        if not isinstance(self.curation_timestamp, XSDDateTime):
            self.curation_timestamp = XSDDateTime(self.curation_timestamp)

        if self.curation_model is not None and not isinstance(self.curation_model, str):
            self.curation_model = str(self.curation_model)

        if self.curation_action is not None and not isinstance(self.curation_action, CurationActionEnum):
            self.curation_action = CurationActionEnum(self.curation_action)

        if self.curation_description is not None and not isinstance(self.curation_description, str):
            self.curation_description = str(self.curation_description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Term(YAMLRoot):
    """
    A structured reference to an ontology term
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Term"]
    class_class_curie: ClassVar[str] = "dismech:Term"
    class_name: ClassVar[str] = "Term"
    class_model_uri: ClassVar[URIRef] = DISMECH.Term

    id: Union[str, TermId] = None
    label: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TermId):
            self.id = TermId(self.id)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Descriptor(YAMLRoot):
    """
    Base class for structured descriptors that allow a preferred term, optional description, optional ontology term
    binding, and post-composition via modifier, located_in, laterality, spatial_extent, onset, temporality,
    clinical_course, and severity slots.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Descriptor"]
    class_class_curie: ClassVar[str] = "dismech:Descriptor"
    class_name: ClassVar[str] = "Descriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.Descriptor

    preferred_term: str = None
    description: Optional[str] = None
    term: Optional[Union[dict, Term]] = None
    modifier: Optional[Union[str, "ModifierEnum"]] = None
    located_in: Optional[Union[dict, "AnatomicalEntityDescriptor"]] = None
    laterality: Optional[Union[str, "LateralityEnum"]] = None
    spatial_extent: Optional[Union[str, "SpatialExtentEnum"]] = None
    onset: Optional[Union[dict, "OnsetDescriptor"]] = None
    temporality: Optional[Union[str, "TemporalityEnum"]] = None
    clinical_course: Optional[Union[str, "ClinicalCourseEnum"]] = None
    severity: Optional[Union[dict, Any]] = None
    qualifiers: Optional[Union[Union[dict, "Qualifier"], list[Union[dict, "Qualifier"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.preferred_term):
            self.MissingRequiredField("preferred_term")
        if not isinstance(self.preferred_term, str):
            self.preferred_term = str(self.preferred_term)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        if self.modifier is not None and not isinstance(self.modifier, ModifierEnum):
            self.modifier = ModifierEnum(self.modifier)

        if self.located_in is not None and not isinstance(self.located_in, AnatomicalEntityDescriptor):
            self.located_in = AnatomicalEntityDescriptor(**as_dict(self.located_in))

        if self.laterality is not None and not isinstance(self.laterality, LateralityEnum):
            self.laterality = LateralityEnum(self.laterality)

        if self.spatial_extent is not None and not isinstance(self.spatial_extent, SpatialExtentEnum):
            self.spatial_extent = SpatialExtentEnum(self.spatial_extent)

        if self.onset is not None and not isinstance(self.onset, OnsetDescriptor):
            self.onset = OnsetDescriptor(**as_dict(self.onset))

        if self.temporality is not None and not isinstance(self.temporality, TemporalityEnum):
            self.temporality = TemporalityEnum(self.temporality)

        if self.clinical_course is not None and not isinstance(self.clinical_course, ClinicalCourseEnum):
            self.clinical_course = ClinicalCourseEnum(self.clinical_course)

        if not isinstance(self.qualifiers, list):
            self.qualifiers = [self.qualifiers] if self.qualifiers is not None else []
        self.qualifiers = [v if isinstance(v, Qualifier) else Qualifier(**as_dict(v)) for v in self.qualifiers]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Qualifier(YAMLRoot):
    """
    A predicate-value pair for formal post-composition. Allows OWL-like expressivity with controlled predicates and
    values, both as full Descriptors.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Qualifier"]
    class_class_curie: ClassVar[str] = "dismech:Qualifier"
    class_name: ClassVar[str] = "Qualifier"
    class_model_uri: ClassVar[URIRef] = DISMECH.Qualifier

    predicate: Optional[Union[dict, Descriptor]] = None
    value: Optional[Union[dict, Descriptor]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.predicate is not None and not isinstance(self.predicate, Descriptor):
            self.predicate = Descriptor(**as_dict(self.predicate))

        if self.value is not None and not isinstance(self.value, Descriptor):
            self.value = Descriptor(**as_dict(self.value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DietaryModification(YAMLRoot):
    """
    A structured dietary addition, restriction, avoidance, or substitution used to post-compose a treatment descriptor
    with FOODON foods or beverages.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["DietaryModification"]
    class_class_curie: ClassVar[str] = "dismech:DietaryModification"
    class_name: ClassVar[str] = "DietaryModification"
    class_model_uri: ClassVar[URIRef] = DISMECH.DietaryModification

    action: Optional[Union[str, "DietaryModificationActionEnum"]] = None
    food: Optional[Union[dict, "FoodDescriptor"]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.action is not None and not isinstance(self.action, DietaryModificationActionEnum):
            self.action = DietaryModificationActionEnum(self.action)

        if self.food is not None and not isinstance(self.food, FoodDescriptor):
            self.food = FoodDescriptor(**as_dict(self.food))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CellTypeDescriptor(Descriptor):
    """
    A descriptor for cell types, bindable to Cell Ontology (CL)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["CellTypeDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:CellTypeDescriptor"
    class_name: ClassVar[str] = "CellTypeDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.CellTypeDescriptor

    preferred_term: str = None
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiologicalProcessDescriptor(Descriptor):
    """
    A descriptor for biological processes, bindable to Gene Ontology (GO)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["BiologicalProcessDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:BiologicalProcessDescriptor"
    class_name: ClassVar[str] = "BiologicalProcessDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.BiologicalProcessDescriptor

    preferred_term: str = None
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolecularFunctionDescriptor(Descriptor):
    """
    A descriptor for molecular functions, bindable to Gene Ontology (GO)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["MolecularFunctionDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:MolecularFunctionDescriptor"
    class_name: ClassVar[str] = "MolecularFunctionDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.MolecularFunctionDescriptor

    preferred_term: str = None
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnatomicalEntityDescriptor(Descriptor):
    """
    A descriptor for anatomical locations, bindable to UBERON
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["AnatomicalEntityDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:AnatomicalEntityDescriptor"
    class_name: ClassVar[str] = "AnatomicalEntityDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.AnatomicalEntityDescriptor

    preferred_term: str = None
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalEntityDescriptor(Descriptor):
    """
    A descriptor for chemical entities, bindable to CHEBI
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ChemicalEntityDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:ChemicalEntityDescriptor"
    class_name: ClassVar[str] = "ChemicalEntityDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.ChemicalEntityDescriptor

    preferred_term: str = None
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneDescriptor(Descriptor):
    """
    A descriptor for genes, bindable to HGNC or other gene databases
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["GeneDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:GeneDescriptor"
    class_name: ClassVar[str] = "GeneDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.GeneDescriptor

    preferred_term: str = None
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CellularComponentDescriptor(Descriptor):
    """
    A descriptor for cellular components, bindable to GO cellular component
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["CellularComponentDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:CellularComponentDescriptor"
    class_name: ClassVar[str] = "CellularComponentDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.CellularComponentDescriptor

    preferred_term: str = None
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProteinComplexDescriptor(Descriptor):
    """
    A descriptor for protein complexes that gene products participate in, bindable to GO protein complex terms
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ProteinComplexDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:ProteinComplexDescriptor"
    class_name: ClassVar[str] = "ProteinComplexDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.ProteinComplexDescriptor

    preferred_term: str = None
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneSetAssociation(YAMLRoot):
    """
    A curated link between this disease and an external gene set, referenced by its structured-source id
    (MYGENESET:<id>, resolving to references_cache/MYGENESET_<id>.md). The gene set's membership and curated GO
    interpretation live upstream / in the cache file; this object records only the precise disease<->set link and its
    semantics, avoiding re-duplication of genes in the KB. It is the anchor for BP alignment (`just genesets-align`):
    the set's curated biological processes are scored against this disease's pathograph.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["GeneSetAssociation"]
    class_class_curie: ClassVar[str] = "dismech:GeneSetAssociation"
    class_name: ClassVar[str] = "GeneSetAssociation"
    class_model_uri: ClassVar[URIRef] = DISMECH.GeneSetAssociation

    gene_set: Union[str, URIorCURIE] = None
    relationship: Optional[Union[str, "GeneSetRelationshipEnum"]] = None
    note: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.gene_set):
            self.MissingRequiredField("gene_set")
        if not isinstance(self.gene_set, URIorCURIE):
            self.gene_set = URIorCURIE(self.gene_set)

        if self.relationship is not None and not isinstance(self.relationship, GeneSetRelationshipEnum):
            self.relationship = GeneSetRelationshipEnum(self.relationship)

        if self.note is not None and not isinstance(self.note, str):
            self.note = str(self.note)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssayDescriptor(Descriptor):
    """
    A descriptor for assays, bindable to OBI
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["AssayDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:AssayDescriptor"
    class_name: ClassVar[str] = "AssayDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.AssayDescriptor

    preferred_term: str = None
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TriggerDescriptor(Descriptor):
    """
    A descriptor for triggers/causes
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["TriggerDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:TriggerDescriptor"
    class_name: ClassVar[str] = "TriggerDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.TriggerDescriptor

    preferred_term: str = None
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiseaseDescriptor(Descriptor):
    """
    A descriptor for the focal disease, bindable to MONDO
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["DiseaseDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:DiseaseDescriptor"
    class_name: ClassVar[str] = "DiseaseDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.DiseaseDescriptor

    preferred_term: str = None
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SubtypeDescriptor(Descriptor):
    """
    A descriptor for disease subtypes, bindable to MONDO disease terms or NCIT oncology subtype terms.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["SubtypeDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:SubtypeDescriptor"
    class_name: ClassVar[str] = "SubtypeDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.SubtypeDescriptor

    preferred_term: str = None
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiomarkerDescriptor(Descriptor):
    """
    A descriptor for biomarkers, bindable to NCIT
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["BiomarkerDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:BiomarkerDescriptor"
    class_name: ClassVar[str] = "BiomarkerDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.BiomarkerDescriptor

    preferred_term: str = None
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneProductDescriptor(Descriptor):
    """
    A descriptor for gene products (proteins, fusion proteins, oncoproteins), bindable to NCIT Gene Product hierarchy
    (NCIT:C26548)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["GeneProductDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:GeneProductDescriptor"
    class_name: ClassVar[str] = "GeneProductDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.GeneProductDescriptor

    preferred_term: str = None
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HistopathologyFindingDescriptor(Descriptor):
    """
    A descriptor for histopathologic findings, bindable to the NCIT Histopathology Result branch (C83490) -
    Morphologic Finding (C35867), Immunophenotypic Finding (C40998), Ultrastructural Finding (C43265), Staining
    Intensity (C127762), Histologic Grade (C18000) - or HP Abnormal cell morphology (HP:0025461)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["HistopathologyFindingDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:HistopathologyFindingDescriptor"
    class_name: ClassVar[str] = "HistopathologyFindingDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.HistopathologyFindingDescriptor

    preferred_term: str = None
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImagingFindingDescriptor(Descriptor):
    """
    A descriptor for an in-vivo imaging finding, bindable to the NCIT Imaging Finding branch (C176708 / C199145) or an
    HP imaging-observable phenotype. Inherits located_in (UBERON body site), laterality, spatial_extent, and modifier
    from Descriptor for post-composition.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ImagingFindingDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:ImagingFindingDescriptor"
    class_name: ClassVar[str] = "ImagingFindingDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.ImagingFindingDescriptor

    preferred_term: str = None
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ElectrophysiologyContext(YAMLRoot):
    """
    An optional post-composition sidecar on a Phenotype, carrying the electrophysiologic axes that a flat HP phenotype
    term cannot express: the modality it was recorded on, whether it is ictal/interictal/postictal, and the
    behavioural/activation recording state. Used ONLY on phenotypes whose phenotype_term is an electrophysiologic
    finding (the HP EEG/EMG/EKG abnormality subtrees, e.g. descendants of HP:0002353). Deliberately NOT a separate
    finding class: because electrophysiologic findings are already HP phenotypes, they live in `phenotypes` and this
    block only post-composes them, exactly as temporality/clinical_course/severity/onset do elsewhere.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ElectrophysiologyContext"]
    class_class_curie: ClassVar[str] = "dismech:ElectrophysiologyContext"
    class_name: ClassVar[str] = "ElectrophysiologyContext"
    class_model_uri: ClassVar[URIRef] = DISMECH.ElectrophysiologyContext

    electrophysiology_modality: Optional[Union[str, "ElectrophysiologyModalityEnum"]] = None
    ictal_state: Optional[Union[str, "IctalStateEnum"]] = None
    recording_state: Optional[Union[str, "EEGRecordingStateEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.electrophysiology_modality is not None and not isinstance(self.electrophysiology_modality, ElectrophysiologyModalityEnum):
            self.electrophysiology_modality = ElectrophysiologyModalityEnum(self.electrophysiology_modality)

        if self.ictal_state is not None and not isinstance(self.ictal_state, IctalStateEnum):
            self.ictal_state = IctalStateEnum(self.ictal_state)

        if self.recording_state is not None and not isinstance(self.recording_state, EEGRecordingStateEnum):
            self.recording_state = EEGRecordingStateEnum(self.recording_state)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LifeCycleStageDescriptor(Descriptor):
    """
    A descriptor for parasite life cycle stages, bindable to OPL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["LifeCycleStageDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:LifeCycleStageDescriptor"
    class_name: ClassVar[str] = "LifeCycleStageDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.LifeCycleStageDescriptor

    preferred_term: str = None
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhenotypeDescriptor(Descriptor):
    """
    A descriptor for phenotypes, bindable to Human Phenotype Ontology (HP)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["PhenotypeDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:PhenotypeDescriptor"
    class_name: ClassVar[str] = "PhenotypeDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.PhenotypeDescriptor

    preferred_term: str = None
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InheritanceDescriptor(Descriptor):
    """
    A descriptor for inheritance patterns, bindable to HPO mode of inheritance terms
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["InheritanceDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:InheritanceDescriptor"
    class_name: ClassVar[str] = "InheritanceDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.InheritanceDescriptor

    preferred_term: str = None
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TreatmentDescriptor(Descriptor):
    """
    A descriptor for treatments/medical actions, bindable to NCIT clinical interventions
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["TreatmentDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:TreatmentDescriptor"
    class_name: ClassVar[str] = "TreatmentDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.TreatmentDescriptor

    preferred_term: str = None
    therapeutic_agent: Optional[Union[Union[dict, ChemicalEntityDescriptor], list[Union[dict, ChemicalEntityDescriptor]]]] = empty_list()
    dietary_modifications: Optional[Union[Union[dict, DietaryModification], list[Union[dict, DietaryModification]]]] = empty_list()
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="therapeutic_agent", slot_type=ChemicalEntityDescriptor, key_name="preferred_term", keyed=False)

        if not isinstance(self.dietary_modifications, list):
            self.dietary_modifications = [self.dietary_modifications] if self.dietary_modifications is not None else []
        self.dietary_modifications = [v if isinstance(v, DietaryModification) else DietaryModification(**as_dict(v)) for v in self.dietary_modifications]

        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RegimenDescriptor(Descriptor):
    """
    A descriptor for treatment regimens, bindable to NCIT
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["RegimenDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:RegimenDescriptor"
    class_name: ClassVar[str] = "RegimenDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.RegimenDescriptor

    preferred_term: str = None
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureDescriptor(Descriptor):
    """
    A descriptor for exposure events, bindable to ECTO or XCO
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ExposureDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:ExposureDescriptor"
    class_name: ClassVar[str] = "ExposureDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.ExposureDescriptor

    preferred_term: str = None
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnvironmentDescriptor(Descriptor):
    """
    A descriptor for environmental contexts/settings, bindable to ENVO
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["EnvironmentDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:EnvironmentDescriptor"
    class_name: ClassVar[str] = "EnvironmentDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.EnvironmentDescriptor

    preferred_term: str = None
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FoodDescriptor(Descriptor):
    """
    A descriptor for foods, beverages, nutrients, minerals, and supplements, bindable to FOODON or CHEBI
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["FoodDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:FoodDescriptor"
    class_name: ClassVar[str] = "FoodDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.FoodDescriptor

    preferred_term: str = None
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrganismDescriptor(Descriptor):
    """
    A descriptor for organisms, bindable to NCBITaxon
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["OrganismDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:OrganismDescriptor"
    class_name: ClassVar[str] = "OrganismDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.OrganismDescriptor

    preferred_term: str = None
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HostDescriptor(OrganismDescriptor):
    """
    A descriptor for hosts in an infectious agent life cycle
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["HostDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:HostDescriptor"
    class_name: ClassVar[str] = "HostDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.HostDescriptor

    preferred_term: str = None
    role: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.role is not None and not isinstance(self.role, str):
            self.role = str(self.role)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SampleTypeDescriptor(Descriptor):
    """
    A descriptor for biological sample types (tissue and/or cell type)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["SampleTypeDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:SampleTypeDescriptor"
    class_name: ClassVar[str] = "SampleTypeDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.SampleTypeDescriptor

    preferred_term: str = None
    tissue_term: Optional[Union[dict, AnatomicalEntityDescriptor]] = None
    cell_type_term: Optional[Union[dict, CellTypeDescriptor]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.tissue_term is not None and not isinstance(self.tissue_term, AnatomicalEntityDescriptor):
            self.tissue_term = AnatomicalEntityDescriptor(**as_dict(self.tissue_term))

        if self.cell_type_term is not None and not isinstance(self.cell_type_term, CellTypeDescriptor):
            self.cell_type_term = CellTypeDescriptor(**as_dict(self.cell_type_term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneticContext(YAMLRoot):
    """
    A structured description of a genetic context that modifies phenotype frequency, severity, or presentation.
    Flexible enough to capture single genes, multiple genes, mutation types, zygosity, complementation groups, and
    complex genotypes. The description slot accommodates contexts that don't fit neatly into the structured fields
    (e.g., structural variants, complex rearrangements).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["GeneticContext"]
    class_class_curie: ClassVar[str] = "dismech:GeneticContext"
    class_name: ClassVar[str] = "GeneticContext"
    class_model_uri: ClassVar[URIRef] = DISMECH.GeneticContext

    gene: Optional[Union[dict, GeneDescriptor]] = None
    genes: Optional[Union[Union[dict, GeneDescriptor], list[Union[dict, GeneDescriptor]]]] = empty_list()
    allele_type: Optional[str] = None
    variant_origin: Optional[Union[str, "VariantOriginEnum"]] = None
    allelic_hit_role: Optional[Union[str, "AllelicHitRoleEnum"]] = None
    allelic_events: Optional[Union[Union[str, "AllelicEventEnum"], list[Union[str, "AllelicEventEnum"]]]] = empty_list()
    zygosity: Optional[Union[str, "ZygosityEnum"]] = None
    functional_impact: Optional[str] = None
    functional_impact_category: Optional[Union[str, "FunctionalImpactEnum"]] = None
    complementation_group: Optional[str] = None
    description: Optional[str] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.gene is not None and not isinstance(self.gene, GeneDescriptor):
            self.gene = GeneDescriptor(**as_dict(self.gene))

        self._normalize_inlined_as_list(slot_name="genes", slot_type=GeneDescriptor, key_name="preferred_term", keyed=False)

        if self.allele_type is not None and not isinstance(self.allele_type, str):
            self.allele_type = str(self.allele_type)

        if self.variant_origin is not None and not isinstance(self.variant_origin, VariantOriginEnum):
            self.variant_origin = VariantOriginEnum(self.variant_origin)

        if self.allelic_hit_role is not None and not isinstance(self.allelic_hit_role, AllelicHitRoleEnum):
            self.allelic_hit_role = AllelicHitRoleEnum(self.allelic_hit_role)

        if not isinstance(self.allelic_events, list):
            self.allelic_events = [self.allelic_events] if self.allelic_events is not None else []
        self.allelic_events = [v if isinstance(v, AllelicEventEnum) else AllelicEventEnum(v) for v in self.allelic_events]

        if self.zygosity is not None and not isinstance(self.zygosity, ZygosityEnum):
            self.zygosity = ZygosityEnum(self.zygosity)

        if self.functional_impact is not None and not isinstance(self.functional_impact, str):
            self.functional_impact = str(self.functional_impact)

        if self.functional_impact_category is not None and not isinstance(self.functional_impact_category, FunctionalImpactEnum):
            self.functional_impact_category = FunctionalImpactEnum(self.functional_impact_category)

        if self.complementation_group is not None and not isinstance(self.complementation_group, str):
            self.complementation_group = str(self.complementation_group)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OnsetDescriptor(YAMLRoot):
    """
    Structured description of age of onset. Combines an HPO onset category with optional quantitative age data and
    notes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["OnsetDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:OnsetDescriptor"
    class_name: ClassVar[str] = "OnsetDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.OnsetDescriptor

    onset_category: Optional[Union[str, "OnsetEnum"]] = None
    mean_age_years: Optional[float] = None
    min_age_years: Optional[float] = None
    max_age_years: Optional[float] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.onset_category is not None and not isinstance(self.onset_category, OnsetEnum):
            self.onset_category = OnsetEnum(self.onset_category)

        if self.mean_age_years is not None and not isinstance(self.mean_age_years, float):
            self.mean_age_years = float(self.mean_age_years)

        if self.min_age_years is not None and not isinstance(self.min_age_years, float):
            self.min_age_years = float(self.min_age_years)

        if self.max_age_years is not None and not isinstance(self.max_age_years, float):
            self.max_age_years = float(self.max_age_years)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhenotypeContext(YAMLRoot):
    """
    A context-specific annotation qualifying how a phenotype manifests under particular conditions. Each context can
    specify a genetic context, demographic stratum, or disease subtype, along with frequency, severity, onset, and
    supporting evidence specific to that context.
    When no context qualifier slots are set (no genetic_context, sex, population, age_range, or subtype), the context
    provides evidence for the overall/default frequency claim, addressing the evidence separation problem (issue
    #112).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["PhenotypeContext"]
    class_class_curie: ClassVar[str] = "dismech:PhenotypeContext"
    class_name: ClassVar[str] = "PhenotypeContext"
    class_model_uri: ClassVar[URIRef] = DISMECH.PhenotypeContext

    frequency: Optional[Union[dict, Any]] = None
    severity: Optional[Union[dict, Any]] = None
    onset: Optional[Union[dict, OnsetDescriptor]] = None
    notes: Optional[str] = None
    evidence: Optional[Union[Union[dict, "EvidenceItem"], list[Union[dict, "EvidenceItem"]]]] = empty_list()
    genetic_context: Optional[Union[dict, GeneticContext]] = None
    sex: Optional[Union[str, "SexEnum"]] = None
    population: Optional[str] = None
    age_range: Optional[str] = None
    subtype: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.onset is not None and not isinstance(self.onset, OnsetDescriptor):
            self.onset = OnsetDescriptor(**as_dict(self.onset))

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.genetic_context is not None and not isinstance(self.genetic_context, GeneticContext):
            self.genetic_context = GeneticContext(**as_dict(self.genetic_context))

        if self.sex is not None and not isinstance(self.sex, SexEnum):
            self.sex = SexEnum(self.sex)

        if self.population is not None and not isinstance(self.population, str):
            self.population = str(self.population)

        if self.age_range is not None and not isinstance(self.age_range, str):
            self.age_range = str(self.age_range)

        if self.subtype is not None and not isinstance(self.subtype, str):
            self.subtype = str(self.subtype)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dataset(YAMLRoot):
    """
    A reference to a publicly available omics or phenotype dataset
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Dataset"]
    class_class_curie: ClassVar[str] = "dismech:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = DISMECH.Dataset

    accession: Union[str, DatasetAccession] = None
    title: Optional[str] = None
    description: Optional[str] = None
    organism: Optional[Union[dict, OrganismDescriptor]] = None
    data_type: Optional[Union[str, "DatasetTypeEnum"]] = None
    sample_types: Optional[Union[Union[dict, SampleTypeDescriptor], list[Union[dict, SampleTypeDescriptor]]]] = empty_list()
    sample_count: Optional[int] = None
    conditions: Optional[Union[str, list[str]]] = empty_list()
    exposures: Optional[Union[Union[dict, ExposureDescriptor], list[Union[dict, ExposureDescriptor]]]] = empty_list()
    genes: Optional[Union[Union[dict, GeneDescriptor], list[Union[dict, GeneDescriptor]]]] = empty_list()
    platform: Optional[str] = None
    publication: Optional[str] = None
    findings: Optional[Union[Union[dict, "Finding"], list[Union[dict, "Finding"]]]] = empty_list()
    evidence: Optional[Union[Union[dict, "EvidenceItem"], list[Union[dict, "EvidenceItem"]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.accession):
            self.MissingRequiredField("accession")
        if not isinstance(self.accession, DatasetAccession):
            self.accession = DatasetAccession(self.accession)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.organism is not None and not isinstance(self.organism, OrganismDescriptor):
            self.organism = OrganismDescriptor(**as_dict(self.organism))

        if self.data_type is not None and not isinstance(self.data_type, DatasetTypeEnum):
            self.data_type = DatasetTypeEnum(self.data_type)

        self._normalize_inlined_as_list(slot_name="sample_types", slot_type=SampleTypeDescriptor, key_name="preferred_term", keyed=False)

        if self.sample_count is not None and not isinstance(self.sample_count, int):
            self.sample_count = int(self.sample_count)

        if not isinstance(self.conditions, list):
            self.conditions = [self.conditions] if self.conditions is not None else []
        self.conditions = [v if isinstance(v, str) else str(v) for v in self.conditions]

        self._normalize_inlined_as_list(slot_name="exposures", slot_type=ExposureDescriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="genes", slot_type=GeneDescriptor, key_name="preferred_term", keyed=False)

        if self.platform is not None and not isinstance(self.platform, str):
            self.platform = str(self.platform)

        if self.publication is not None and not isinstance(self.publication, str):
            self.publication = str(self.publication)

        self._normalize_inlined_as_list(slot_name="findings", slot_type=Finding, key_name="statement", keyed=False)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExperimentalModel(YAMLRoot):
    """
    A disease-relevant non-animal experimental model system — a New Approach Methodology (NAM) such as an organoid,
    organ-on-chip, cell line, iPSC-derived model, or primary culture. This is a disease-centric bridge class inspired
    by NAMO, intended to capture the model itself while keeping dismech focused on disease mechanisms rather than
    study-level model registries.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ExperimentalModel"]
    class_class_curie: ClassVar[str] = "dismech:ExperimentalModel"
    class_name: ClassVar[str] = "ExperimentalModel"
    class_model_uri: ClassVar[URIRef] = DISMECH.ExperimentalModel

    name: Union[str, ExperimentalModelName] = None
    description: Optional[str] = None
    experimental_model_type: Optional[Union[str, "ExperimentalModelTypeEnum"]] = None
    namo_type: Optional[Union[str, URIorCURIE]] = None
    organism: Optional[Union[dict, OrganismDescriptor]] = None
    tissue_term: Optional[Union[dict, AnatomicalEntityDescriptor]] = None
    cell_types: Optional[Union[Union[dict, CellTypeDescriptor], list[Union[dict, CellTypeDescriptor]]]] = empty_list()
    conditions: Optional[Union[str, list[str]]] = empty_list()
    cell_source: Optional[str] = None
    culture_system: Optional[str] = None
    publication: Optional[str] = None
    modeled_mechanisms: Optional[Union[Union[dict, "ModelMechanismLink"], list[Union[dict, "ModelMechanismLink"]]]] = empty_list()
    findings: Optional[Union[Union[dict, "Finding"], list[Union[dict, "Finding"]]]] = empty_list()
    evidence: Optional[Union[Union[dict, "EvidenceItem"], list[Union[dict, "EvidenceItem"]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ExperimentalModelName):
            self.name = ExperimentalModelName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.experimental_model_type is not None and not isinstance(self.experimental_model_type, ExperimentalModelTypeEnum):
            self.experimental_model_type = ExperimentalModelTypeEnum(self.experimental_model_type)

        if self.namo_type is not None and not isinstance(self.namo_type, URIorCURIE):
            self.namo_type = URIorCURIE(self.namo_type)

        if self.organism is not None and not isinstance(self.organism, OrganismDescriptor):
            self.organism = OrganismDescriptor(**as_dict(self.organism))

        if self.tissue_term is not None and not isinstance(self.tissue_term, AnatomicalEntityDescriptor):
            self.tissue_term = AnatomicalEntityDescriptor(**as_dict(self.tissue_term))

        self._normalize_inlined_as_list(slot_name="cell_types", slot_type=CellTypeDescriptor, key_name="preferred_term", keyed=False)

        if not isinstance(self.conditions, list):
            self.conditions = [self.conditions] if self.conditions is not None else []
        self.conditions = [v if isinstance(v, str) else str(v) for v in self.conditions]

        if self.cell_source is not None and not isinstance(self.cell_source, str):
            self.cell_source = str(self.cell_source)

        if self.culture_system is not None and not isinstance(self.culture_system, str):
            self.culture_system = str(self.culture_system)

        if self.publication is not None and not isinstance(self.publication, str):
            self.publication = str(self.publication)

        self._normalize_inlined_as_list(slot_name="modeled_mechanisms", slot_type=ModelMechanismLink, key_name="target", keyed=False)

        self._normalize_inlined_as_list(slot_name="findings", slot_type=Finding, key_name="statement", keyed=False)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Experiment(YAMLRoot):
    """
    A structured experiment or protocol-level study design that can be proposed to resolve a knowledge gap, or later
    reused to represent experiments that have been carried out. The object itself is intentionally status-neutral:
    proposal, execution, and evidentiary status are expressed by the containing slot or future evidence context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Experiment"]
    class_class_curie: ClassVar[str] = "dismech:Experiment"
    class_name: ClassVar[str] = "Experiment"
    class_model_uri: ClassVar[URIRef] = DISMECH.Experiment

    name: Union[str, ExperimentName] = None
    experiment_id: str = None
    description: Optional[str] = None
    experiment_type: Optional[Union[dict, Descriptor]] = None
    model_systems: Optional[Union[dict[Union[str, ExperimentalModelName], Union[dict, ExperimentalModel]], list[Union[dict, ExperimentalModel]]]] = empty_dict()
    perturbations: Optional[Union[dict[Union[str, ExperimentalPerturbationName], Union[dict, "ExperimentalPerturbation"]], list[Union[dict, "ExperimentalPerturbation"]]]] = empty_dict()
    assays: Optional[Union[Union[dict, AssayDescriptor], list[Union[dict, AssayDescriptor]]]] = empty_list()
    readouts: Optional[Union[dict[Union[str, ExperimentalReadoutName], Union[dict, "ExperimentalReadout"]], list[Union[dict, "ExperimentalReadout"]]]] = empty_dict()
    controls: Optional[Union[dict[Union[str, ExperimentalControlName], Union[dict, "ExperimentalControl"]], list[Union[dict, "ExperimentalControl"]]]] = empty_dict()
    decision_criterion: Optional[str] = None
    would_support: Optional[Union[str, list[str]]] = empty_list()
    would_refute: Optional[Union[str, list[str]]] = empty_list()
    supporting_outcome: Optional[Union[str, list[str]]] = empty_list()
    refuting_outcome: Optional[Union[str, list[str]]] = empty_list()
    protocol_reference: Optional[str] = None
    datasets: Optional[Union[dict[Union[str, DatasetAccession], Union[dict, Dataset]], list[Union[dict, Dataset]]]] = empty_dict()
    evidence: Optional[Union[Union[dict, "EvidenceItem"], list[Union[dict, "EvidenceItem"]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ExperimentName):
            self.name = ExperimentName(self.name)

        if self._is_empty(self.experiment_id):
            self.MissingRequiredField("experiment_id")
        if not isinstance(self.experiment_id, str):
            self.experiment_id = str(self.experiment_id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.experiment_type is not None and not isinstance(self.experiment_type, Descriptor):
            self.experiment_type = Descriptor(**as_dict(self.experiment_type))

        self._normalize_inlined_as_list(slot_name="model_systems", slot_type=ExperimentalModel, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="perturbations", slot_type=ExperimentalPerturbation, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="assays", slot_type=AssayDescriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="readouts", slot_type=ExperimentalReadout, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="controls", slot_type=ExperimentalControl, key_name="name", keyed=True)

        if self.decision_criterion is not None and not isinstance(self.decision_criterion, str):
            self.decision_criterion = str(self.decision_criterion)

        if not isinstance(self.would_support, list):
            self.would_support = [self.would_support] if self.would_support is not None else []
        self.would_support = [v if isinstance(v, str) else str(v) for v in self.would_support]

        if not isinstance(self.would_refute, list):
            self.would_refute = [self.would_refute] if self.would_refute is not None else []
        self.would_refute = [v if isinstance(v, str) else str(v) for v in self.would_refute]

        if not isinstance(self.supporting_outcome, list):
            self.supporting_outcome = [self.supporting_outcome] if self.supporting_outcome is not None else []
        self.supporting_outcome = [v if isinstance(v, str) else str(v) for v in self.supporting_outcome]

        if not isinstance(self.refuting_outcome, list):
            self.refuting_outcome = [self.refuting_outcome] if self.refuting_outcome is not None else []
        self.refuting_outcome = [v if isinstance(v, str) else str(v) for v in self.refuting_outcome]

        if self.protocol_reference is not None and not isinstance(self.protocol_reference, str):
            self.protocol_reference = str(self.protocol_reference)

        self._normalize_inlined_as_list(slot_name="datasets", slot_type=Dataset, key_name="accession", keyed=True)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExperimentalPerturbation(YAMLRoot):
    """
    A structured perturbation, intervention, or exposure used in an experiment. Prefer ontology-backed descriptors for
    genes, chemicals, treatments, exposures, triggers, and biological processes rather than plain string lists.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ExperimentalPerturbation"]
    class_class_curie: ClassVar[str] = "dismech:ExperimentalPerturbation"
    class_name: ClassVar[str] = "ExperimentalPerturbation"
    class_model_uri: ClassVar[URIRef] = DISMECH.ExperimentalPerturbation

    name: Union[str, ExperimentalPerturbationName] = None
    target: str = None
    description: Optional[str] = None
    gene: Optional[Union[dict, GeneDescriptor]] = None
    genes: Optional[Union[Union[dict, GeneDescriptor], list[Union[dict, GeneDescriptor]]]] = empty_list()
    chemical_entities: Optional[Union[Union[dict, ChemicalEntityDescriptor], list[Union[dict, ChemicalEntityDescriptor]]]] = empty_list()
    treatment_term: Optional[Union[dict, TreatmentDescriptor]] = None
    exposure_term: Optional[Union[dict, ExposureDescriptor]] = None
    triggers: Optional[Union[Union[dict, TriggerDescriptor], list[Union[dict, TriggerDescriptor]]]] = empty_list()
    biological_processes: Optional[Union[Union[dict, BiologicalProcessDescriptor], list[Union[dict, BiologicalProcessDescriptor]]]] = empty_list()
    effect: Optional[str] = None
    evidence: Optional[Union[Union[dict, "EvidenceItem"], list[Union[dict, "EvidenceItem"]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ExperimentalPerturbationName):
            self.name = ExperimentalPerturbationName(self.name)

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, str):
            self.target = str(self.target)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.gene is not None and not isinstance(self.gene, GeneDescriptor):
            self.gene = GeneDescriptor(**as_dict(self.gene))

        self._normalize_inlined_as_list(slot_name="genes", slot_type=GeneDescriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="chemical_entities", slot_type=ChemicalEntityDescriptor, key_name="preferred_term", keyed=False)

        if self.treatment_term is not None and not isinstance(self.treatment_term, TreatmentDescriptor):
            self.treatment_term = TreatmentDescriptor(**as_dict(self.treatment_term))

        if self.exposure_term is not None and not isinstance(self.exposure_term, ExposureDescriptor):
            self.exposure_term = ExposureDescriptor(**as_dict(self.exposure_term))

        self._normalize_inlined_as_list(slot_name="triggers", slot_type=TriggerDescriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="biological_processes", slot_type=BiologicalProcessDescriptor, key_name="preferred_term", keyed=False)

        if self.effect is not None and not isinstance(self.effect, str):
            self.effect = str(self.effect)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExperimentalReadout(YAMLRoot):
    """
    A structured readout or outcome measured in an experiment or reported by a model. Use descriptor slots to ground
    readouts to phenotypes, biomarkers, biological processes, and assays.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ExperimentalReadout"]
    class_class_curie: ClassVar[str] = "dismech:ExperimentalReadout"
    class_name: ClassVar[str] = "ExperimentalReadout"
    class_model_uri: ClassVar[URIRef] = DISMECH.ExperimentalReadout

    name: Union[str, ExperimentalReadoutName] = None
    target: str = None
    description: Optional[str] = None
    phenotype_term: Optional[Union[dict, PhenotypeDescriptor]] = None
    biomarker_term: Optional[Union[dict, BiomarkerDescriptor]] = None
    biological_processes: Optional[Union[Union[dict, BiologicalProcessDescriptor], list[Union[dict, BiologicalProcessDescriptor]]]] = empty_list()
    assays: Optional[Union[Union[dict, AssayDescriptor], list[Union[dict, AssayDescriptor]]]] = empty_list()
    direction: Optional[Union[dict, Any]] = None
    interpretation: Optional[str] = None
    evidence: Optional[Union[Union[dict, "EvidenceItem"], list[Union[dict, "EvidenceItem"]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ExperimentalReadoutName):
            self.name = ExperimentalReadoutName(self.name)

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, str):
            self.target = str(self.target)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.phenotype_term is not None and not isinstance(self.phenotype_term, PhenotypeDescriptor):
            self.phenotype_term = PhenotypeDescriptor(**as_dict(self.phenotype_term))

        if self.biomarker_term is not None and not isinstance(self.biomarker_term, BiomarkerDescriptor):
            self.biomarker_term = BiomarkerDescriptor(**as_dict(self.biomarker_term))

        self._normalize_inlined_as_list(slot_name="biological_processes", slot_type=BiologicalProcessDescriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="assays", slot_type=AssayDescriptor, key_name="preferred_term", keyed=False)

        if self.interpretation is not None and not isinstance(self.interpretation, str):
            self.interpretation = str(self.interpretation)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExperimentalControl(YAMLRoot):
    """
    A comparator or control condition for an experiment, such as an isogenic wild-type line, mock perturbation,
    vehicle control, rescue arm, or untreated disease model.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ExperimentalControl"]
    class_class_curie: ClassVar[str] = "dismech:ExperimentalControl"
    class_name: ClassVar[str] = "ExperimentalControl"
    class_model_uri: ClassVar[URIRef] = DISMECH.ExperimentalControl

    name: Union[str, ExperimentalControlName] = None
    description: Optional[str] = None
    model_systems: Optional[Union[dict[Union[str, ExperimentalModelName], Union[dict, ExperimentalModel]], list[Union[dict, ExperimentalModel]]]] = empty_dict()
    perturbations: Optional[Union[dict[Union[str, ExperimentalPerturbationName], Union[dict, ExperimentalPerturbation]], list[Union[dict, ExperimentalPerturbation]]]] = empty_dict()
    evidence: Optional[Union[Union[dict, "EvidenceItem"], list[Union[dict, "EvidenceItem"]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ExperimentalControlName):
            self.name = ExperimentalControlName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="model_systems", slot_type=ExperimentalModel, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="perturbations", slot_type=ExperimentalPerturbation, key_name="name", keyed=True)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ClinicalTrial(YAMLRoot):
    """
    A clinical trial relevant to treatment or research of a disease
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ClinicalTrial"]
    class_class_curie: ClassVar[str] = "dismech:ClinicalTrial"
    class_name: ClassVar[str] = "ClinicalTrial"
    class_model_uri: ClassVar[URIRef] = DISMECH.ClinicalTrial

    name: Union[str, ClinicalTrialName] = None
    description: Optional[str] = None
    phase: Optional[Union[str, "ClinicalTrialPhaseEnum"]] = None
    status: Optional[Union[str, "ClinicalTrialStatusEnum"]] = None
    evidence: Optional[Union[Union[dict, "EvidenceItem"], list[Union[dict, "EvidenceItem"]]]] = empty_list()
    target_phenotypes: Optional[Union[Union[dict, PhenotypeDescriptor], list[Union[dict, PhenotypeDescriptor]]]] = empty_list()
    notes: Optional[str] = None
    review_notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ClinicalTrialName):
            self.name = ClinicalTrialName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.phase is not None and not isinstance(self.phase, ClinicalTrialPhaseEnum):
            self.phase = ClinicalTrialPhaseEnum(self.phase)

        if self.status is not None and not isinstance(self.status, ClinicalTrialStatusEnum):
            self.status = ClinicalTrialStatusEnum(self.status)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        self._normalize_inlined_as_list(slot_name="target_phenotypes", slot_type=PhenotypeDescriptor, key_name="preferred_term", keyed=False)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.review_notes is not None and not isinstance(self.review_notes, str):
            self.review_notes = str(self.review_notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComputationalModel(YAMLRoot):
    """
    A computational or in-silico model relevant to understanding disease mechanisms
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ComputationalModel"]
    class_class_curie: ClassVar[str] = "dismech:ComputationalModel"
    class_name: ClassVar[str] = "ComputationalModel"
    class_model_uri: ClassVar[URIRef] = DISMECH.ComputationalModel

    name: Union[str, ComputationalModelName] = None
    description: Optional[str] = None
    model_type: Optional[Union[str, "ComputationalModelTypeEnum"]] = None
    repository_url: Optional[Union[str, URI]] = None
    model_id: Optional[str] = None
    base_model: Optional[str] = None
    perturbations: Optional[Union[Union[dict, GeneDescriptor], list[Union[dict, GeneDescriptor]]]] = empty_list()
    variables: Optional[Union[dict[Union[str, ModelVariableName], Union[dict, "ModelVariable"]], list[Union[dict, "ModelVariable"]]]] = empty_dict()
    modeled_mechanisms: Optional[Union[Union[dict, "ModelMechanismLink"], list[Union[dict, "ModelMechanismLink"]]]] = empty_list()
    model_software: Optional[str] = None
    model_format: Optional[str] = None
    publication: Optional[str] = None
    findings: Optional[Union[Union[dict, "Finding"], list[Union[dict, "Finding"]]]] = empty_list()
    evidence: Optional[Union[Union[dict, "EvidenceItem"], list[Union[dict, "EvidenceItem"]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ComputationalModelName):
            self.name = ComputationalModelName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.model_type is not None and not isinstance(self.model_type, ComputationalModelTypeEnum):
            self.model_type = ComputationalModelTypeEnum(self.model_type)

        if self.repository_url is not None and not isinstance(self.repository_url, URI):
            self.repository_url = URI(self.repository_url)

        if self.model_id is not None and not isinstance(self.model_id, str):
            self.model_id = str(self.model_id)

        if self.base_model is not None and not isinstance(self.base_model, str):
            self.base_model = str(self.base_model)

        self._normalize_inlined_as_list(slot_name="perturbations", slot_type=GeneDescriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="variables", slot_type=ModelVariable, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="modeled_mechanisms", slot_type=ModelMechanismLink, key_name="target", keyed=False)

        if self.model_software is not None and not isinstance(self.model_software, str):
            self.model_software = str(self.model_software)

        if self.model_format is not None and not isinstance(self.model_format, str):
            self.model_format = str(self.model_format)

        if self.publication is not None and not isinstance(self.publication, str):
            self.publication = str(self.publication)

        self._normalize_inlined_as_list(slot_name="findings", slot_type=Finding, key_name="statement", keyed=False)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModelVariable(YAMLRoot):
    """
    A variable in a computational model, identified by a human-readable name, with an optional dataset_identifier for
    the native name in the model file and ontology term mappings (e.g., LOINC for clinical observables, CHEBI for
    metabolites, HP for phenotypic readouts).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ModelVariable"]
    class_class_curie: ClassVar[str] = "dismech:ModelVariable"
    class_name: ClassVar[str] = "ModelVariable"
    class_model_uri: ClassVar[URIRef] = DISMECH.ModelVariable

    name: Union[str, ModelVariableName] = None
    dataset_identifier: Optional[str] = None
    description: Optional[str] = None
    unit: Optional[str] = None
    mappings_list: Optional[Union[Union[dict, "ModelVariableDescriptor"], list[Union[dict, "ModelVariableDescriptor"]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ModelVariableName):
            self.name = ModelVariableName(self.name)

        if self.dataset_identifier is not None and not isinstance(self.dataset_identifier, str):
            self.dataset_identifier = str(self.dataset_identifier)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        self._normalize_inlined_as_list(slot_name="mappings_list", slot_type=ModelVariableDescriptor, key_name="preferred_term", keyed=False)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SeverityTier(YAMLRoot):
    """
    A threshold-severity pair defining one tier in a severity scale
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["SeverityTier"]
    class_class_curie: ClassVar[str] = "dismech:SeverityTier"
    class_name: ClassVar[str] = "SeverityTier"
    class_model_uri: ClassVar[URIRef] = DISMECH.SeverityTier

    name: Union[str, SeverityTierName] = None
    threshold: float = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, SeverityTierName):
            self.name = SeverityTierName(self.name)

        if self._is_empty(self.threshold):
            self.MissingRequiredField("threshold")
        if not isinstance(self.threshold, float):
            self.threshold = float(self.threshold)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModelVariableDescriptor(Descriptor):
    """
    A descriptor mapping a model variable to an ontology term (LOINC, CHEBI, HP, etc.). When the mapped term is an HP
    phenotype, optional threshold fields specify when the variable value activates that phenotype and at what
    severity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ModelVariableDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:ModelVariableDescriptor"
    class_name: ClassVar[str] = "ModelVariableDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.ModelVariableDescriptor

    preferred_term: str = None
    threshold: Optional[float] = None
    threshold_direction: Optional[Union[str, "ThresholdDirectionEnum"]] = None
    severity_scale: Optional[Union[dict[Union[str, SeverityTierName], Union[dict, SeverityTier]], list[Union[dict, SeverityTier]]]] = empty_dict()
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.threshold is not None and not isinstance(self.threshold, float):
            self.threshold = float(self.threshold)

        if self.threshold_direction is not None and not isinstance(self.threshold_direction, ThresholdDirectionEnum):
            self.threshold_direction = ThresholdDirectionEnum(self.threshold_direction)

        self._normalize_inlined_as_list(slot_name="severity_scale", slot_type=SeverityTier, key_name="name", keyed=True)

        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DifferentialDiagnosis(YAMLRoot):
    """
    A disease or condition that presents similarly to the focal disease and must be differentiated
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["DifferentialDiagnosis"]
    class_class_curie: ClassVar[str] = "dismech:DifferentialDiagnosis"
    class_name: ClassVar[str] = "DifferentialDiagnosis"
    class_model_uri: ClassVar[URIRef] = DISMECH.DifferentialDiagnosis

    name: Union[str, DifferentialDiagnosisName] = None
    description: Optional[str] = None
    phenotypes: Optional[Union[dict[Union[str, PhenotypeName], Union[dict, "Phenotype"]], list[Union[dict, "Phenotype"]]]] = empty_dict()
    distinguishing_features: Optional[Union[str, list[str]]] = empty_list()
    evidence: Optional[Union[Union[dict, "EvidenceItem"], list[Union[dict, "EvidenceItem"]]]] = empty_list()
    notes: Optional[str] = None
    disease_term: Optional[Union[dict, DiseaseDescriptor]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, DifferentialDiagnosisName):
            self.name = DifferentialDiagnosisName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="phenotypes", slot_type=Phenotype, key_name="name", keyed=True)

        if not isinstance(self.distinguishing_features, list):
            self.distinguishing_features = [self.distinguishing_features] if self.distinguishing_features is not None else []
        self.distinguishing_features = [v if isinstance(v, str) else str(v) for v in self.distinguishing_features]

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.disease_term is not None and not isinstance(self.disease_term, DiseaseDescriptor):
            self.disease_term = DiseaseDescriptor(**as_dict(self.disease_term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Subtype(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Subtype"]
    class_class_curie: ClassVar[str] = "dismech:Subtype"
    class_name: ClassVar[str] = "Subtype"
    class_model_uri: ClassVar[URIRef] = DISMECH.Subtype

    name: Union[str, SubtypeName] = None
    display_name: Optional[str] = None
    subtype_term: Optional[Union[dict, SubtypeDescriptor]] = None
    mappings: Optional[Union[dict, "DiseaseMappings"]] = None
    description: Optional[str] = None
    evidence: Optional[Union[Union[dict, "EvidenceItem"], list[Union[dict, "EvidenceItem"]]]] = empty_list()
    review_notes: Optional[str] = None
    locations: Optional[Union[Union[dict, AnatomicalEntityDescriptor], list[Union[dict, AnatomicalEntityDescriptor]]]] = empty_list()
    geography: Optional[Union[Union[str, "GeographyTerm"], list[Union[str, "GeographyTerm"]]]] = empty_list()
    classification: Optional[str] = None
    children: Optional[Union[str, list[str]]] = empty_list()
    genes: Optional[Union[Union[dict, GeneDescriptor], list[Union[dict, GeneDescriptor]]]] = empty_list()
    subtype_frequency: Optional[str] = None
    inheritance: Optional[Union[dict[Union[str, InheritanceName], Union[dict, "Inheritance"]], list[Union[dict, "Inheritance"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, SubtypeName):
            self.name = SubtypeName(self.name)

        if self.display_name is not None and not isinstance(self.display_name, str):
            self.display_name = str(self.display_name)

        if self.subtype_term is not None and not isinstance(self.subtype_term, SubtypeDescriptor):
            self.subtype_term = SubtypeDescriptor(**as_dict(self.subtype_term))

        if self.mappings is not None and not isinstance(self.mappings, DiseaseMappings):
            self.mappings = DiseaseMappings(**as_dict(self.mappings))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.review_notes is not None and not isinstance(self.review_notes, str):
            self.review_notes = str(self.review_notes)

        self._normalize_inlined_as_list(slot_name="locations", slot_type=AnatomicalEntityDescriptor, key_name="preferred_term", keyed=False)

        if self.classification is not None and not isinstance(self.classification, str):
            self.classification = str(self.classification)

        if not isinstance(self.children, list):
            self.children = [self.children] if self.children is not None else []
        self.children = [v if isinstance(v, str) else str(v) for v in self.children]

        self._normalize_inlined_as_list(slot_name="genes", slot_type=GeneDescriptor, key_name="preferred_term", keyed=False)

        if self.subtype_frequency is not None and not isinstance(self.subtype_frequency, str):
            self.subtype_frequency = str(self.subtype_frequency)

        self._normalize_inlined_as_list(slot_name="inheritance", slot_type=Inheritance, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EvidenceItem(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["EvidenceItem"]
    class_class_curie: ClassVar[str] = "dismech:EvidenceItem"
    class_name: ClassVar[str] = "EvidenceItem"
    class_model_uri: ClassVar[URIRef] = DISMECH.EvidenceItem

    reference: Optional[str] = None
    reference_title: Optional[str] = None
    supports: Optional[Union[str, "EvidenceItemSupportEnum"]] = None
    directness: Optional[Union[str, "DirectnessEnum"]] = None
    evidence_source: Optional[Union[str, "EvidenceSourceEnum"]] = None
    snippet: Optional[str] = None
    explanation: Optional[str] = None
    images: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.reference is not None and not isinstance(self.reference, str):
            self.reference = str(self.reference)

        if self.reference_title is not None and not isinstance(self.reference_title, str):
            self.reference_title = str(self.reference_title)

        if self.supports is not None and not isinstance(self.supports, EvidenceItemSupportEnum):
            self.supports = EvidenceItemSupportEnum(self.supports)

        if self.directness is not None and not isinstance(self.directness, DirectnessEnum):
            self.directness = DirectnessEnum(self.directness)

        if self.evidence_source is not None and not isinstance(self.evidence_source, EvidenceSourceEnum):
            self.evidence_source = EvidenceSourceEnum(self.evidence_source)

        if self.snippet is not None and not isinstance(self.snippet, str):
            self.snippet = str(self.snippet)

        if self.explanation is not None and not isinstance(self.explanation, str):
            self.explanation = str(self.explanation)

        if not isinstance(self.images, list):
            self.images = [self.images] if self.images is not None else []
        self.images = [v if isinstance(v, str) else str(v) for v in self.images]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CausalEdge(YAMLRoot):
    """
    A reference to a downstream effect or consequence in a causal relationship
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["CausalEdge"]
    class_class_curie: ClassVar[str] = "dismech:CausalEdge"
    class_name: ClassVar[str] = "CausalEdge"
    class_model_uri: ClassVar[URIRef] = DISMECH.CausalEdge

    target: str = None
    description: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    hypothesis_groups: Optional[Union[str, list[str]]] = empty_list()
    causal_link_type: Optional[Union[str, "CausalLinkTypeEnum"]] = None
    intermediate_mechanisms: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, str):
            self.target = str(self.target)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if not isinstance(self.hypothesis_groups, list):
            self.hypothesis_groups = [self.hypothesis_groups] if self.hypothesis_groups is not None else []
        self.hypothesis_groups = [v if isinstance(v, str) else str(v) for v in self.hypothesis_groups]

        if self.causal_link_type is not None and not isinstance(self.causal_link_type, CausalLinkTypeEnum):
            self.causal_link_type = CausalLinkTypeEnum(self.causal_link_type)

        if not isinstance(self.intermediate_mechanisms, list):
            self.intermediate_mechanisms = [self.intermediate_mechanisms] if self.intermediate_mechanisms is not None else []
        self.intermediate_mechanisms = [v if isinstance(v, str) else str(v) for v in self.intermediate_mechanisms]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TreatmentMechanismTarget(YAMLRoot):
    """
    Links a treatment to a specific pathophysiology mechanism node it targets. Enables reasoning about which
    downstream phenotypes should respond to therapy and why resistance may emerge when the causal chain shifts.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["TreatmentMechanismTarget"]
    class_class_curie: ClassVar[str] = "dismech:TreatmentMechanismTarget"
    class_name: ClassVar[str] = "TreatmentMechanismTarget"
    class_model_uri: ClassVar[URIRef] = DISMECH.TreatmentMechanismTarget

    target: str = None
    treatment_effect: Optional[Union[str, "TreatmentEffectEnum"]] = None
    description: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, str):
            self.target = str(self.target)

        if self.treatment_effect is not None and not isinstance(self.treatment_effect, TreatmentEffectEnum):
            self.treatment_effect = TreatmentEffectEnum(self.treatment_effect)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnvironmentalMechanismTarget(YAMLRoot):
    """
    Links an environmental factor or exposure to a specific pathophysiology mechanism node it acts on. The
    environmental counterpart of TreatmentMechanismTarget: it places exposures inside the causal graph as upstream
    initiating (or protective) steps instead of leaving them as a disconnected disease-level list.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["EnvironmentalMechanismTarget"]
    class_class_curie: ClassVar[str] = "dismech:EnvironmentalMechanismTarget"
    class_name: ClassVar[str] = "EnvironmentalMechanismTarget"
    class_model_uri: ClassVar[URIRef] = DISMECH.EnvironmentalMechanismTarget

    target: str = None
    environmental_effect: Optional[Union[str, "EnvironmentalEffectEnum"]] = None
    causal_link_type: Optional[Union[str, "CausalLinkTypeEnum"]] = None
    description: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, str):
            self.target = str(self.target)

        if self.environmental_effect is not None and not isinstance(self.environmental_effect, EnvironmentalEffectEnum):
            self.environmental_effect = EnvironmentalEffectEnum(self.environmental_effect)

        if self.causal_link_type is not None and not isinstance(self.causal_link_type, CausalLinkTypeEnum):
            self.causal_link_type = CausalLinkTypeEnum(self.causal_link_type)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModelMechanismLink(YAMLRoot):
    """
    Links an experimental (NAM), animal, or computational model to a specific pathophysiology mechanism node,
    recording which facet of that mechanism the model recapitulates, perturbs, or reads out; how faithfully it does
    so; and the outcome measures that ground the claim.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ModelMechanismLink"]
    class_class_curie: ClassVar[str] = "dismech:ModelMechanismLink"
    class_name: ClassVar[str] = "ModelMechanismLink"
    class_model_uri: ClassVar[URIRef] = DISMECH.ModelMechanismLink

    target: str = None
    relationship: Optional[Union[str, "ModelMechanismRelationshipEnum"]] = None
    description: Optional[str] = None
    readouts: Optional[Union[dict[Union[str, ExperimentalReadoutName], Union[dict, ExperimentalReadout]], list[Union[dict, ExperimentalReadout]]]] = empty_dict()
    fidelity: Optional[Union[str, "ModelFidelityEnum"]] = None
    limitations: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, str):
            self.target = str(self.target)

        if self.relationship is not None and not isinstance(self.relationship, ModelMechanismRelationshipEnum):
            self.relationship = ModelMechanismRelationshipEnum(self.relationship)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="readouts", slot_type=ExperimentalReadout, key_name="name", keyed=True)

        if self.fidelity is not None and not isinstance(self.fidelity, ModelFidelityEnum):
            self.fidelity = ModelFidelityEnum(self.fidelity)

        if self.limitations is not None and not isinstance(self.limitations, str):
            self.limitations = str(self.limitations)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiomarkerReadout(YAMLRoot):
    """
    Links a biochemical biomarker to a pathograph node that it measures, reflects, predicts, or pharmacodynamically
    reports on. This is an observational readout link, not a causal claim that the biomarker causes the target
    mechanism or phenotype.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["BiomarkerReadout"]
    class_class_curie: ClassVar[str] = "dismech:BiomarkerReadout"
    class_name: ClassVar[str] = "BiomarkerReadout"
    class_model_uri: ClassVar[URIRef] = DISMECH.BiomarkerReadout

    target: str = None
    relationship: Union[str, "BiomarkerReadoutRelationshipEnum"] = None
    direction: Optional[Union[str, "BiomarkerReadoutDirectionEnum"]] = None
    endpoint_context: Optional[Union[str, "BiomarkerEndpointContextEnum"]] = None
    regulatory_endpoint_refs: Optional[Union[str, list[str]]] = empty_list()
    interpretation: Optional[str] = None
    description: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, str):
            self.target = str(self.target)

        if self._is_empty(self.relationship):
            self.MissingRequiredField("relationship")
        if not isinstance(self.relationship, BiomarkerReadoutRelationshipEnum):
            self.relationship = BiomarkerReadoutRelationshipEnum(self.relationship)

        if self.direction is not None and not isinstance(self.direction, BiomarkerReadoutDirectionEnum):
            self.direction = BiomarkerReadoutDirectionEnum(self.direction)

        if self.endpoint_context is not None and not isinstance(self.endpoint_context, BiomarkerEndpointContextEnum):
            self.endpoint_context = BiomarkerEndpointContextEnum(self.endpoint_context)

        if not isinstance(self.regulatory_endpoint_refs, list):
            self.regulatory_endpoint_refs = [self.regulatory_endpoint_refs] if self.regulatory_endpoint_refs is not None else []
        self.regulatory_endpoint_refs = [v if isinstance(v, str) else str(v) for v in self.regulatory_endpoint_refs]

        if self.interpretation is not None and not isinstance(self.interpretation, str):
            self.interpretation = str(self.interpretation)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhenotypeReadout(YAMLRoot):
    """
    Links an investigation-readout phenotype (an abnormal electrophysiology, functional-test, or clinical-laboratory
    finding, e.g. HP:0000512 Abnormal electroretinogram) to the pathograph node whose underlying state it measures or
    reflects. This is an observational readout link, not a causal claim that the target mechanism causes the test
    result. It is the phenotype-side counterpart of BiomarkerReadout, deliberately lean: it omits the
    surrogate-endpoint/regulatory slots (regulatory_endpoint_refs and the source-table bridge) that belong only to
    molecular biomarker readouts.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["PhenotypeReadout"]
    class_class_curie: ClassVar[str] = "dismech:PhenotypeReadout"
    class_name: ClassVar[str] = "PhenotypeReadout"
    class_model_uri: ClassVar[URIRef] = DISMECH.PhenotypeReadout

    target: str = None
    relationship: Union[str, "BiomarkerReadoutRelationshipEnum"] = None
    direction: Optional[Union[str, "BiomarkerReadoutDirectionEnum"]] = None
    endpoint_context: Optional[Union[str, "BiomarkerEndpointContextEnum"]] = None
    interpretation: Optional[str] = None
    description: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, str):
            self.target = str(self.target)

        if self._is_empty(self.relationship):
            self.MissingRequiredField("relationship")
        if not isinstance(self.relationship, BiomarkerReadoutRelationshipEnum):
            self.relationship = BiomarkerReadoutRelationshipEnum(self.relationship)

        if self.direction is not None and not isinstance(self.direction, BiomarkerReadoutDirectionEnum):
            self.direction = BiomarkerReadoutDirectionEnum(self.direction)

        if self.endpoint_context is not None and not isinstance(self.endpoint_context, BiomarkerEndpointContextEnum):
            self.endpoint_context = BiomarkerEndpointContextEnum(self.endpoint_context)

        if self.interpretation is not None and not isinstance(self.interpretation, str):
            self.interpretation = str(self.interpretation)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReferenceRangeBand(YAMLRoot):
    """
    A single graded interpretation band within a reference range, mapping a value interval to a categorical clinical
    label (e.g., "Normal", "Mild", "Moderate", "Severe", "Critical"). Bands partition the measurement scale so a
    numeric result can be classified into a clinical category. This expresses the "above value X is mild, above value
    Y is moderate" style of graded result interpretation that a single normal interval cannot capture.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ReferenceRangeBand"]
    class_class_curie: ClassVar[str] = "dismech:ReferenceRangeBand"
    class_name: ClassVar[str] = "ReferenceRangeBand"
    class_model_uri: ClassVar[URIRef] = DISMECH.ReferenceRangeBand

    name: Union[str, ReferenceRangeBandName] = None
    lower_bound: Optional[float] = None
    upper_bound: Optional[float] = None
    unit: Optional[str] = None
    abnormal_flag: Optional[Union[str, "AbnormalFlagEnum"]] = None
    severity: Optional[Union[dict, Any]] = None
    phenotype_term: Optional[Union[dict, PhenotypeDescriptor]] = None
    interpretation: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ReferenceRangeBandName):
            self.name = ReferenceRangeBandName(self.name)

        if self.lower_bound is not None and not isinstance(self.lower_bound, float):
            self.lower_bound = float(self.lower_bound)

        if self.upper_bound is not None and not isinstance(self.upper_bound, float):
            self.upper_bound = float(self.upper_bound)

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if self.abnormal_flag is not None and not isinstance(self.abnormal_flag, AbnormalFlagEnum):
            self.abnormal_flag = AbnormalFlagEnum(self.abnormal_flag)

        if self.phenotype_term is not None and not isinstance(self.phenotype_term, PhenotypeDescriptor):
            self.phenotype_term = PhenotypeDescriptor(**as_dict(self.phenotype_term))

        if self.interpretation is not None and not isinstance(self.interpretation, str):
            self.interpretation = str(self.interpretation)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReferenceRange(YAMLRoot):
    """
    A population reference interval for a clinical laboratory analyte. Captures the numeric normal range (lower and
    upper bounds), measurement unit in UCUM notation, and population qualifier. Provenance is carried by structured
    evidence items (the same EvidenceItem model used elsewhere in dismech), consistent with how all other assertions
    are attributed. Complements ModelVariableDescriptor thresholds (which define disease-model activation points) with
    empirically grounded clinical reference intervals.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ReferenceRange"]
    class_class_curie: ClassVar[str] = "dismech:ReferenceRange"
    class_name: ClassVar[str] = "ReferenceRange"
    class_model_uri: ClassVar[URIRef] = DISMECH.ReferenceRange

    loinc_term: Optional[Union[dict, Term]] = None
    lower_bound: Optional[float] = None
    upper_bound: Optional[float] = None
    unit: Optional[str] = None
    population: Optional[str] = None
    interpretation_bands: Optional[Union[dict[Union[str, ReferenceRangeBandName], Union[dict, ReferenceRangeBand]], list[Union[dict, ReferenceRangeBand]]]] = empty_dict()
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.loinc_term is not None and not isinstance(self.loinc_term, Term):
            self.loinc_term = Term(**as_dict(self.loinc_term))

        if self.lower_bound is not None and not isinstance(self.lower_bound, float):
            self.lower_bound = float(self.lower_bound)

        if self.upper_bound is not None and not isinstance(self.upper_bound, float):
            self.upper_bound = float(self.upper_bound)

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if self.population is not None and not isinstance(self.population, str):
            self.population = str(self.population)

        self._normalize_inlined_as_list(slot_name="interpretation_bands", slot_type=ReferenceRangeBand, key_name="name", keyed=True)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SurrogateEndpoint(YAMLRoot):
    """
    A regulatory surrogate endpoint assertion curated from FDA's surrogate endpoint table or a similar authoritative
    source. This captures an endpoint used as a substitute for direct clinical benefit in a specified disease/use,
    patient population, approval-pathway, and therapeutic mechanism context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["SurrogateEndpoint"]
    class_class_curie: ClassVar[str] = "dismech:SurrogateEndpoint"
    class_name: ClassVar[str] = "SurrogateEndpoint"
    class_model_uri: ClassVar[URIRef] = DISMECH.SurrogateEndpoint

    row_id: Union[str, SurrogateEndpointRowId] = None
    source_table: Union[str, "SurrogateEndpointTableEnum"] = None
    source_sheet: str = None
    source_row_number: int = None
    disease_or_use: str = None
    patient_population: str = None
    surrogate_endpoint: str = None
    approval_type: Union[str, "SurrogateEndpointApprovalTypeEnum"] = None
    endpoint_validation_level: Union[str, "SurrogateEndpointValidationLevelEnum"] = None
    clinical_benefit_linkage: Union[str, "ClinicalBenefitLinkageEnum"] = None
    mapping_status: Union[str, "SurrogateEndpointMappingStatusEnum"] = None
    drug_mechanism_of_action: Optional[str] = None
    age_range: Optional[str] = None
    clinical_benefit: Optional[str] = None
    clinical_benefit_linkage_basis: Optional[str] = None
    footnotes: Optional[Union[Union[str, "SurrogateEndpointFootnoteEnum"], list[Union[str, "SurrogateEndpointFootnoteEnum"]]]] = empty_list()
    context_of_use: Optional[str] = None
    mapped_diseases: Optional[Union[str, list[str]]] = empty_list()
    mapped_disease_files: Optional[Union[str, list[str]]] = empty_list()
    mapping_notes: Optional[str] = None
    source_url: Optional[Union[str, URI]] = None
    source_workbook_url: Optional[Union[str, URI]] = None
    source_workbook_sha256: Optional[str] = None
    source_content_current_as_of: Optional[Union[str, XSDDate]] = None
    retrieved_date: Optional[Union[str, XSDDate]] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.row_id):
            self.MissingRequiredField("row_id")
        if not isinstance(self.row_id, SurrogateEndpointRowId):
            self.row_id = SurrogateEndpointRowId(self.row_id)

        if self._is_empty(self.source_table):
            self.MissingRequiredField("source_table")
        if not isinstance(self.source_table, SurrogateEndpointTableEnum):
            self.source_table = SurrogateEndpointTableEnum(self.source_table)

        if self._is_empty(self.source_sheet):
            self.MissingRequiredField("source_sheet")
        if not isinstance(self.source_sheet, str):
            self.source_sheet = str(self.source_sheet)

        if self._is_empty(self.source_row_number):
            self.MissingRequiredField("source_row_number")
        if not isinstance(self.source_row_number, int):
            self.source_row_number = int(self.source_row_number)

        if self._is_empty(self.disease_or_use):
            self.MissingRequiredField("disease_or_use")
        if not isinstance(self.disease_or_use, str):
            self.disease_or_use = str(self.disease_or_use)

        if self._is_empty(self.patient_population):
            self.MissingRequiredField("patient_population")
        if not isinstance(self.patient_population, str):
            self.patient_population = str(self.patient_population)

        if self._is_empty(self.surrogate_endpoint):
            self.MissingRequiredField("surrogate_endpoint")
        if not isinstance(self.surrogate_endpoint, str):
            self.surrogate_endpoint = str(self.surrogate_endpoint)

        if self._is_empty(self.approval_type):
            self.MissingRequiredField("approval_type")
        if not isinstance(self.approval_type, SurrogateEndpointApprovalTypeEnum):
            self.approval_type = SurrogateEndpointApprovalTypeEnum(self.approval_type)

        if self._is_empty(self.endpoint_validation_level):
            self.MissingRequiredField("endpoint_validation_level")
        if not isinstance(self.endpoint_validation_level, SurrogateEndpointValidationLevelEnum):
            self.endpoint_validation_level = SurrogateEndpointValidationLevelEnum(self.endpoint_validation_level)

        if self._is_empty(self.clinical_benefit_linkage):
            self.MissingRequiredField("clinical_benefit_linkage")
        if not isinstance(self.clinical_benefit_linkage, ClinicalBenefitLinkageEnum):
            self.clinical_benefit_linkage = ClinicalBenefitLinkageEnum(self.clinical_benefit_linkage)

        if self._is_empty(self.mapping_status):
            self.MissingRequiredField("mapping_status")
        if not isinstance(self.mapping_status, SurrogateEndpointMappingStatusEnum):
            self.mapping_status = SurrogateEndpointMappingStatusEnum(self.mapping_status)

        if self.drug_mechanism_of_action is not None and not isinstance(self.drug_mechanism_of_action, str):
            self.drug_mechanism_of_action = str(self.drug_mechanism_of_action)

        if self.age_range is not None and not isinstance(self.age_range, str):
            self.age_range = str(self.age_range)

        if self.clinical_benefit is not None and not isinstance(self.clinical_benefit, str):
            self.clinical_benefit = str(self.clinical_benefit)

        if self.clinical_benefit_linkage_basis is not None and not isinstance(self.clinical_benefit_linkage_basis, str):
            self.clinical_benefit_linkage_basis = str(self.clinical_benefit_linkage_basis)

        if not isinstance(self.footnotes, list):
            self.footnotes = [self.footnotes] if self.footnotes is not None else []
        self.footnotes = [v if isinstance(v, SurrogateEndpointFootnoteEnum) else SurrogateEndpointFootnoteEnum(v) for v in self.footnotes]

        if self.context_of_use is not None and not isinstance(self.context_of_use, str):
            self.context_of_use = str(self.context_of_use)

        if not isinstance(self.mapped_diseases, list):
            self.mapped_diseases = [self.mapped_diseases] if self.mapped_diseases is not None else []
        self.mapped_diseases = [v if isinstance(v, str) else str(v) for v in self.mapped_diseases]

        if not isinstance(self.mapped_disease_files, list):
            self.mapped_disease_files = [self.mapped_disease_files] if self.mapped_disease_files is not None else []
        self.mapped_disease_files = [v if isinstance(v, str) else str(v) for v in self.mapped_disease_files]

        if self.mapping_notes is not None and not isinstance(self.mapping_notes, str):
            self.mapping_notes = str(self.mapping_notes)

        if self.source_url is not None and not isinstance(self.source_url, URI):
            self.source_url = URI(self.source_url)

        if self.source_workbook_url is not None and not isinstance(self.source_workbook_url, URI):
            self.source_workbook_url = URI(self.source_workbook_url)

        if self.source_workbook_sha256 is not None and not isinstance(self.source_workbook_sha256, str):
            self.source_workbook_sha256 = str(self.source_workbook_sha256)

        if self.source_content_current_as_of is not None and not isinstance(self.source_content_current_as_of, XSDDate):
            self.source_content_current_as_of = XSDDate(self.source_content_current_as_of)

        if self.retrieved_date is not None and not isinstance(self.retrieved_date, XSDDate):
            self.retrieved_date = XSDDate(self.retrieved_date)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SurrogateEndpointCollection(YAMLRoot):
    """
    A source-level collection of curated regulatory surrogate endpoint assertions
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["SurrogateEndpointCollection"]
    class_class_curie: ClassVar[str] = "dismech:SurrogateEndpointCollection"
    class_name: ClassVar[str] = "SurrogateEndpointCollection"
    class_model_uri: ClassVar[URIRef] = DISMECH.SurrogateEndpointCollection

    name: Union[str, SurrogateEndpointCollectionName] = None
    surrogate_endpoints: Union[dict[Union[str, SurrogateEndpointRowId], Union[dict, SurrogateEndpoint]], list[Union[dict, SurrogateEndpoint]]] = empty_dict()
    description: Optional[str] = None
    source_url: Optional[Union[str, URI]] = None
    source_workbook_url: Optional[Union[str, URI]] = None
    source_workbook_sha256: Optional[str] = None
    source_content_current_as_of: Optional[Union[str, XSDDate]] = None
    retrieved_date: Optional[Union[str, XSDDate]] = None
    tracked_issues: Optional[Union[Union[dict, "TrackedIssue"], list[Union[dict, "TrackedIssue"]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, SurrogateEndpointCollectionName):
            self.name = SurrogateEndpointCollectionName(self.name)

        if self._is_empty(self.surrogate_endpoints):
            self.MissingRequiredField("surrogate_endpoints")
        self._normalize_inlined_as_list(slot_name="surrogate_endpoints", slot_type=SurrogateEndpoint, key_name="row_id", keyed=True)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.source_url is not None and not isinstance(self.source_url, URI):
            self.source_url = URI(self.source_url)

        if self.source_workbook_url is not None and not isinstance(self.source_workbook_url, URI):
            self.source_workbook_url = URI(self.source_workbook_url)

        if self.source_workbook_sha256 is not None and not isinstance(self.source_workbook_sha256, str):
            self.source_workbook_sha256 = str(self.source_workbook_sha256)

        if self.source_content_current_as_of is not None and not isinstance(self.source_content_current_as_of, XSDDate):
            self.source_content_current_as_of = XSDDate(self.source_content_current_as_of)

        if self.retrieved_date is not None and not isinstance(self.retrieved_date, XSDDate):
            self.retrieved_date = XSDDate(self.retrieved_date)

        self._normalize_inlined_as_list(slot_name="tracked_issues", slot_type=TrackedIssue, key_name="url", keyed=False)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProteinStructure(YAMLRoot):
    """
    A 3D protein structure from PDB or AlphaFold relevant to understanding a treatment's mechanism of action. Enables
    embedded 3D visualization of drug-target interactions via Mol* viewer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ProteinStructure"]
    class_class_curie: ClassVar[str] = "dismech:ProteinStructure"
    class_name: ClassVar[str] = "ProteinStructure"
    class_model_uri: ClassVar[URIRef] = DISMECH.ProteinStructure

    pdb_id: str = None
    description: Optional[str] = None
    resolution_angstrom: Optional[float] = None
    method: Optional[str] = None
    ligand: Optional[str] = None
    target_protein: Optional[str] = None
    publication: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.pdb_id):
            self.MissingRequiredField("pdb_id")
        if not isinstance(self.pdb_id, str):
            self.pdb_id = str(self.pdb_id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.resolution_angstrom is not None and not isinstance(self.resolution_angstrom, float):
            self.resolution_angstrom = float(self.resolution_angstrom)

        if self.method is not None and not isinstance(self.method, str):
            self.method = str(self.method)

        if self.ligand is not None and not isinstance(self.ligand, str):
            self.ligand = str(self.ligand)

        if self.target_protein is not None and not isinstance(self.target_protein, str):
            self.target_protein = str(self.target_protein)

        if self.publication is not None and not isinstance(self.publication, str):
            self.publication = str(self.publication)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PublicationReference(YAMLRoot):
    """
    A reference to a publication with associated findings
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["PublicationReference"]
    class_class_curie: ClassVar[str] = "dismech:PublicationReference"
    class_name: ClassVar[str] = "PublicationReference"
    class_model_uri: ClassVar[URIRef] = DISMECH.PublicationReference

    reference: Union[str, PublicationReferenceReference] = None
    title: Optional[str] = None
    found_in: Optional[Union[str, list[str]]] = empty_list()
    tags: Optional[Union[Union[str, "ReferenceTagEnum"], list[Union[str, "ReferenceTagEnum"]]]] = empty_list()
    findings: Optional[Union[Union[dict, "Finding"], list[Union[dict, "Finding"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.reference):
            self.MissingRequiredField("reference")
        if not isinstance(self.reference, PublicationReferenceReference):
            self.reference = PublicationReferenceReference(self.reference)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.found_in, list):
            self.found_in = [self.found_in] if self.found_in is not None else []
        self.found_in = [v if isinstance(v, str) else str(v) for v in self.found_in]

        if not isinstance(self.tags, list):
            self.tags = [self.tags] if self.tags is not None else []
        self.tags = [v if isinstance(v, ReferenceTagEnum) else ReferenceTagEnum(v) for v in self.tags]

        self._normalize_inlined_as_list(slot_name="findings", slot_type=Finding, key_name="statement", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExternalAssertion(YAMLRoot):
    """
    An externally curated assertion or registry record relevant to a disease or variant, such as a ClinGen
    gene-disease validity assertion or a ClinGen Allele Registry record.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ExternalAssertion"]
    class_class_curie: ClassVar[str] = "dismech:ExternalAssertion"
    class_name: ClassVar[str] = "ExternalAssertion"
    class_model_uri: ClassVar[URIRef] = DISMECH.ExternalAssertion

    name: Union[str, ExternalAssertionName] = None
    source: str = None
    external_id: str = None
    assertion_type: Optional[str] = None
    url: Optional[Union[str, URI]] = None
    description: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ExternalAssertionName):
            self.name = ExternalAssertionName(self.name)

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, str):
            self.source = str(self.source)

        if self._is_empty(self.external_id):
            self.MissingRequiredField("external_id")
        if not isinstance(self.external_id, str):
            self.external_id = str(self.external_id)

        if self.assertion_type is not None and not isinstance(self.assertion_type, str):
            self.assertion_type = str(self.assertion_type)

        if self.url is not None and not isinstance(self.url, URI):
            self.url = URI(self.url)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TrackedIssue(YAMLRoot):
    """
    Structured pointer to an external tracker issue (typically a GitHub issue) used to record curation provenance. Use
    this for things like upstream ontology term requests, ontology coverage gaps, schema follow-ups, or any external
    ticket tied to a dismech object, instead of stashing raw URLs in free-text `notes` fields. Attachable at multiple
    levels of the model (disease entries, mappings, etc.).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["TrackedIssue"]
    class_class_curie: ClassVar[str] = "dismech:TrackedIssue"
    class_name: ClassVar[str] = "TrackedIssue"
    class_model_uri: ClassVar[URIRef] = DISMECH.TrackedIssue

    url: Union[str, URI] = None
    title: Optional[str] = None
    tracked_issue_role: Optional[str] = None
    tracked_issue_status: Optional[str] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.url):
            self.MissingRequiredField("url")
        if not isinstance(self.url, URI):
            self.url = URI(self.url)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.tracked_issue_role is not None and not isinstance(self.tracked_issue_role, str):
            self.tracked_issue_role = str(self.tracked_issue_role)

        if self.tracked_issue_status is not None and not isinstance(self.tracked_issue_status, str):
            self.tracked_issue_status = str(self.tracked_issue_status)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Finding(YAMLRoot):
    """
    A key finding or claim extracted from a source (publication or dataset)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Finding"]
    class_class_curie: ClassVar[str] = "dismech:Finding"
    class_name: ClassVar[str] = "Finding"
    class_model_uri: ClassVar[URIRef] = DISMECH.Finding

    statement: str = None
    supporting_text: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.statement):
            self.MissingRequiredField("statement")
        if not isinstance(self.statement, str):
            self.statement = str(self.statement)

        if self.supporting_text is not None and not isinstance(self.supporting_text, str):
            self.supporting_text = str(self.supporting_text)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Prevalence(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Prevalence"]
    class_class_curie: ClassVar[str] = "dismech:Prevalence"
    class_name: ClassVar[str] = "Prevalence"
    class_model_uri: ClassVar[URIRef] = DISMECH.Prevalence

    subtype: Optional[str] = None
    population: Optional[str] = None
    measure_type: Optional[Union[str, "PrevalenceMeasureEnum"]] = None
    prevalence_class: Optional[Union[str, "PrevalenceClassEnum"]] = None
    rate_per_100000: Optional[float] = None
    rate_low: Optional[float] = None
    rate_high: Optional[float] = None
    percentage: Optional[Union[dict, Any]] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subtype is not None and not isinstance(self.subtype, str):
            self.subtype = str(self.subtype)

        if self.population is not None and not isinstance(self.population, str):
            self.population = str(self.population)

        if self.measure_type is not None and not isinstance(self.measure_type, PrevalenceMeasureEnum):
            self.measure_type = PrevalenceMeasureEnum(self.measure_type)

        if self.prevalence_class is not None and not isinstance(self.prevalence_class, PrevalenceClassEnum):
            self.prevalence_class = PrevalenceClassEnum(self.prevalence_class)

        if self.rate_per_100000 is not None and not isinstance(self.rate_per_100000, float):
            self.rate_per_100000 = float(self.rate_per_100000)

        if self.rate_low is not None and not isinstance(self.rate_low, float):
            self.rate_low = float(self.rate_low)

        if self.rate_high is not None and not isinstance(self.rate_high, float):
            self.rate_high = float(self.rate_high)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneCaseFraction(YAMLRoot):
    """
    A structured estimate of the fraction of cases of a genetically heterogeneous disease attributable to one gene, in
    a defined cohort. The genetic-spectrum analog of a population Prevalence record: it pairs a cohort/population with
    a normalized percentage (plus optional range bounds and cohort size), source notes, and citable evidence. Distinct
    from population occurrence (Prevalence) and from population allele frequency; this is "what share of patients have
    their disease explained by this gene". Complements the coarse free-text `frequency` band on the Genetic entry.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["GeneCaseFraction"]
    class_class_curie: ClassVar[str] = "dismech:GeneCaseFraction"
    class_name: ClassVar[str] = "GeneCaseFraction"
    class_model_uri: ClassVar[URIRef] = DISMECH.GeneCaseFraction

    population: Optional[str] = None
    case_fraction_percent: Optional[float] = None
    case_fraction_low: Optional[float] = None
    case_fraction_high: Optional[float] = None
    cohort_size: Optional[int] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.population is not None and not isinstance(self.population, str):
            self.population = str(self.population)

        if self.case_fraction_percent is not None and not isinstance(self.case_fraction_percent, float):
            self.case_fraction_percent = float(self.case_fraction_percent)

        if self.case_fraction_low is not None and not isinstance(self.case_fraction_low, float):
            self.case_fraction_low = float(self.case_fraction_low)

        if self.case_fraction_high is not None and not isinstance(self.case_fraction_high, float):
            self.case_fraction_high = float(self.case_fraction_high)

        if self.cohort_size is not None and not isinstance(self.cohort_size, int):
            self.cohort_size = int(self.cohort_size)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProgressionInfo(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ProgressionInfo"]
    class_class_curie: ClassVar[str] = "dismech:ProgressionInfo"
    class_name: ClassVar[str] = "ProgressionInfo"
    class_model_uri: ClassVar[URIRef] = DISMECH.ProgressionInfo

    phase: Optional[Union[str, "PhaseTerm"]] = None
    subtype: Optional[str] = None
    age_range: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    incubation_days: Optional[str] = None
    review_notes: Optional[str] = None
    incubation_years: Optional[str] = None
    notes: Optional[str] = None
    duration_days: Optional[str] = None
    duration: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subtype is not None and not isinstance(self.subtype, str):
            self.subtype = str(self.subtype)

        if self.age_range is not None and not isinstance(self.age_range, str):
            self.age_range = str(self.age_range)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.incubation_days is not None and not isinstance(self.incubation_days, str):
            self.incubation_days = str(self.incubation_days)

        if self.review_notes is not None and not isinstance(self.review_notes, str):
            self.review_notes = str(self.review_notes)

        if self.incubation_years is not None and not isinstance(self.incubation_years, str):
            self.incubation_years = str(self.incubation_years)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.duration_days is not None and not isinstance(self.duration_days, str):
            self.duration_days = str(self.duration_days)

        if self.duration is not None and not isinstance(self.duration, str):
            self.duration = str(self.duration)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ClinicalBurden(YAMLRoot):
    """
    Disease-level assessment of the typical clinical burden imposed by a disease. This captures the overall burden of
    the disease concept and is distinct from severity annotations on individual phenotypes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ClinicalBurden"]
    class_class_curie: ClassVar[str] = "dismech:ClinicalBurden"
    class_name: ClassVar[str] = "ClinicalBurden"
    class_model_uri: ClassVar[URIRef] = DISMECH.ClinicalBurden

    burden_level: Union[str, "ClinicalBurdenLevelEnum"] = None
    rationale: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.burden_level):
            self.MissingRequiredField("burden_level")
        if not isinstance(self.burden_level, ClinicalBurdenLevelEnum):
            self.burden_level = ClinicalBurdenLevelEnum(self.burden_level)

        if self.rationale is not None and not isinstance(self.rationale, str):
            self.rationale = str(self.rationale)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EpidemiologyInfo(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["EpidemiologyInfo"]
    class_class_curie: ClassVar[str] = "dismech:EpidemiologyInfo"
    class_name: ClassVar[str] = "EpidemiologyInfo"
    class_model_uri: ClassVar[URIRef] = DISMECH.EpidemiologyInfo

    name: Union[str, EpidemiologyInfoName] = None
    description: Optional[str] = None
    minimum_value: Optional[float] = None
    maximum_value: Optional[float] = None
    mean_range: Optional[str] = None
    notes: Optional[str] = None
    factors: Optional[Union[str, list[str]]] = empty_list()
    unit: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, EpidemiologyInfoName):
            self.name = EpidemiologyInfoName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.minimum_value is not None and not isinstance(self.minimum_value, float):
            self.minimum_value = float(self.minimum_value)

        if self.maximum_value is not None and not isinstance(self.maximum_value, float):
            self.maximum_value = float(self.maximum_value)

        if self.mean_range is not None and not isinstance(self.mean_range, str):
            self.mean_range = str(self.mean_range)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if not isinstance(self.factors, list):
            self.factors = [self.factors] if self.factors is not None else []
        self.factors = [v if isinstance(v, str) else str(v) for v in self.factors]

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Pathophysiology(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Pathophysiology"]
    class_class_curie: ClassVar[str] = "dismech:Pathophysiology"
    class_name: ClassVar[str] = "Pathophysiology"
    class_model_uri: ClassVar[URIRef] = DISMECH.Pathophysiology

    name: Union[str, PathophysiologyName] = None
    description: Optional[str] = None
    cell_types: Optional[Union[Union[dict, CellTypeDescriptor], list[Union[dict, CellTypeDescriptor]]]] = empty_list()
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    biological_processes: Optional[Union[Union[dict, BiologicalProcessDescriptor], list[Union[dict, BiologicalProcessDescriptor]]]] = empty_list()
    molecular_functions: Optional[Union[Union[dict, MolecularFunctionDescriptor], list[Union[dict, MolecularFunctionDescriptor]]]] = empty_list()
    locations: Optional[Union[Union[dict, AnatomicalEntityDescriptor], list[Union[dict, AnatomicalEntityDescriptor]]]] = empty_list()
    examples: Optional[Union[str, list[str]]] = empty_list()
    role: Optional[str] = None
    conforms_to: Optional[str] = None
    synonyms: Optional[Union[str, list[str]]] = empty_list()
    consequence: Optional[str] = None
    consequences: Optional[Union[str, list[str]]] = empty_list()
    gene: Optional[Union[dict, GeneDescriptor]] = None
    pathways: Optional[Union[Union[dict, BiologicalProcessDescriptor], list[Union[dict, BiologicalProcessDescriptor]]]] = empty_list()
    downstream: Optional[Union[Union[dict, CausalEdge], list[Union[dict, CausalEdge]]]] = empty_list()
    genes: Optional[Union[Union[dict, GeneDescriptor], list[Union[dict, GeneDescriptor]]]] = empty_list()
    subtypes: Optional[Union[str, list[str]]] = empty_list()
    cellular_components: Optional[Union[Union[dict, CellularComponentDescriptor], list[Union[dict, CellularComponentDescriptor]]]] = empty_list()
    protein_complexes: Optional[Union[Union[dict, ProteinComplexDescriptor], list[Union[dict, ProteinComplexDescriptor]]]] = empty_list()
    chemical_entities: Optional[Union[Union[dict, ChemicalEntityDescriptor], list[Union[dict, ChemicalEntityDescriptor]]]] = empty_list()
    gene_products: Optional[Union[Union[dict, GeneProductDescriptor], list[Union[dict, GeneProductDescriptor]]]] = empty_list()
    triggers: Optional[Union[Union[dict, TriggerDescriptor], list[Union[dict, TriggerDescriptor]]]] = empty_list()
    assays: Optional[Union[Union[dict, AssayDescriptor], list[Union[dict, AssayDescriptor]]]] = empty_list()
    mechanisms: Optional[Union[str, list[str]]] = empty_list()
    notes: Optional[str] = None
    frequency: Optional[Union[dict, Any]] = None
    genetic_context: Optional[Union[dict, GeneticContext]] = None
    pdb_structures: Optional[Union[Union[dict, ProteinStructure], list[Union[dict, ProteinStructure]]]] = empty_list()
    mechanism_confidence: Optional[Union[str, "MechanismConfidenceEnum"]] = None
    biological_scale: Optional[Union[str, "BiologicalScaleEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, PathophysiologyName):
            self.name = PathophysiologyName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="cell_types", slot_type=CellTypeDescriptor, key_name="preferred_term", keyed=False)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        self._normalize_inlined_as_list(slot_name="biological_processes", slot_type=BiologicalProcessDescriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="molecular_functions", slot_type=MolecularFunctionDescriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="locations", slot_type=AnatomicalEntityDescriptor, key_name="preferred_term", keyed=False)

        if not isinstance(self.examples, list):
            self.examples = [self.examples] if self.examples is not None else []
        self.examples = [v if isinstance(v, str) else str(v) for v in self.examples]

        if self.role is not None and not isinstance(self.role, str):
            self.role = str(self.role)

        if self.conforms_to is not None and not isinstance(self.conforms_to, str):
            self.conforms_to = str(self.conforms_to)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        if self.consequence is not None and not isinstance(self.consequence, str):
            self.consequence = str(self.consequence)

        if not isinstance(self.consequences, list):
            self.consequences = [self.consequences] if self.consequences is not None else []
        self.consequences = [v if isinstance(v, str) else str(v) for v in self.consequences]

        if self.gene is not None and not isinstance(self.gene, GeneDescriptor):
            self.gene = GeneDescriptor(**as_dict(self.gene))

        self._normalize_inlined_as_list(slot_name="pathways", slot_type=BiologicalProcessDescriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="downstream", slot_type=CausalEdge, key_name="target", keyed=False)

        self._normalize_inlined_as_list(slot_name="genes", slot_type=GeneDescriptor, key_name="preferred_term", keyed=False)

        if not isinstance(self.subtypes, list):
            self.subtypes = [self.subtypes] if self.subtypes is not None else []
        self.subtypes = [v if isinstance(v, str) else str(v) for v in self.subtypes]

        self._normalize_inlined_as_list(slot_name="cellular_components", slot_type=CellularComponentDescriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="protein_complexes", slot_type=ProteinComplexDescriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="chemical_entities", slot_type=ChemicalEntityDescriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="gene_products", slot_type=GeneProductDescriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="triggers", slot_type=TriggerDescriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="assays", slot_type=AssayDescriptor, key_name="preferred_term", keyed=False)

        if not isinstance(self.mechanisms, list):
            self.mechanisms = [self.mechanisms] if self.mechanisms is not None else []
        self.mechanisms = [v if isinstance(v, str) else str(v) for v in self.mechanisms]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.genetic_context is not None and not isinstance(self.genetic_context, GeneticContext):
            self.genetic_context = GeneticContext(**as_dict(self.genetic_context))

        self._normalize_inlined_as_list(slot_name="pdb_structures", slot_type=ProteinStructure, key_name="pdb_id", keyed=False)

        if self.mechanism_confidence is not None and not isinstance(self.mechanism_confidence, MechanismConfidenceEnum):
            self.mechanism_confidence = MechanismConfidenceEnum(self.mechanism_confidence)

        if self.biological_scale is not None and not isinstance(self.biological_scale, BiologicalScaleEnum):
            self.biological_scale = BiologicalScaleEnum(self.biological_scale)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Phenotype(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Phenotype"]
    class_class_curie: ClassVar[str] = "dismech:Phenotype"
    class_name: ClassVar[str] = "Phenotype"
    class_model_uri: ClassVar[URIRef] = DISMECH.Phenotype

    name: Union[str, PhenotypeName] = None
    category: Optional[str] = None
    phenotype_term: Optional[Union[dict, PhenotypeDescriptor]] = None
    frequency: Optional[Union[dict, Any]] = None
    description: Optional[str] = None
    diagnostic: Optional[Union[bool, Bool]] = None
    sequelae: Optional[Union[Union[dict, CausalEdge], list[Union[dict, CausalEdge]]]] = empty_list()
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    context: Optional[str] = None
    review_notes: Optional[str] = None
    severity: Optional[Union[dict, Any]] = None
    notes: Optional[str] = None
    subtype: Optional[str] = None
    subtypes: Optional[Union[str, list[str]]] = empty_list()
    phenotype_contexts: Optional[Union[Union[dict, PhenotypeContext], list[Union[dict, PhenotypeContext]]]] = empty_list()
    electrophysiology: Optional[Union[dict, ElectrophysiologyContext]] = None
    reports_on: Optional[Union[Union[dict, PhenotypeReadout], list[Union[dict, PhenotypeReadout]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, PhenotypeName):
            self.name = PhenotypeName(self.name)

        if self.category is not None and not isinstance(self.category, str):
            self.category = str(self.category)

        if self.phenotype_term is not None and not isinstance(self.phenotype_term, PhenotypeDescriptor):
            self.phenotype_term = PhenotypeDescriptor(**as_dict(self.phenotype_term))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.diagnostic is not None and not isinstance(self.diagnostic, Bool):
            self.diagnostic = Bool(self.diagnostic)

        self._normalize_inlined_as_list(slot_name="sequelae", slot_type=CausalEdge, key_name="target", keyed=False)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.context is not None and not isinstance(self.context, str):
            self.context = str(self.context)

        if self.review_notes is not None and not isinstance(self.review_notes, str):
            self.review_notes = str(self.review_notes)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.subtype is not None and not isinstance(self.subtype, str):
            self.subtype = str(self.subtype)

        if not isinstance(self.subtypes, list):
            self.subtypes = [self.subtypes] if self.subtypes is not None else []
        self.subtypes = [v if isinstance(v, str) else str(v) for v in self.subtypes]

        if not isinstance(self.phenotype_contexts, list):
            self.phenotype_contexts = [self.phenotype_contexts] if self.phenotype_contexts is not None else []
        self.phenotype_contexts = [v if isinstance(v, PhenotypeContext) else PhenotypeContext(**as_dict(v)) for v in self.phenotype_contexts]

        if self.electrophysiology is not None and not isinstance(self.electrophysiology, ElectrophysiologyContext):
            self.electrophysiology = ElectrophysiologyContext(**as_dict(self.electrophysiology))

        self._normalize_inlined_as_list(slot_name="reports_on", slot_type=PhenotypeReadout, key_name="target", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Biochemical(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Biochemical"]
    class_class_curie: ClassVar[str] = "dismech:Biochemical"
    class_name: ClassVar[str] = "Biochemical"
    class_model_uri: ClassVar[URIRef] = DISMECH.Biochemical

    name: Union[str, BiochemicalName] = None
    biomarker_term: Optional[Union[dict, BiomarkerDescriptor]] = None
    presence: Optional[str] = None
    readouts: Optional[Union[Union[dict, BiomarkerReadout], list[Union[dict, BiomarkerReadout]]]] = empty_list()
    reference_ranges: Optional[Union[Union[dict, ReferenceRange], list[Union[dict, ReferenceRange]]]] = empty_list()
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    specificity: Optional[str] = None
    frequency: Optional[Union[dict, Any]] = None
    notes: Optional[str] = None
    context: Optional[str] = None
    subtype: Optional[str] = None
    subtypes: Optional[Union[str, list[str]]] = empty_list()
    cell_types: Optional[Union[Union[dict, CellTypeDescriptor], list[Union[dict, CellTypeDescriptor]]]] = empty_list()
    assays: Optional[Union[Union[dict, AssayDescriptor], list[Union[dict, AssayDescriptor]]]] = empty_list()
    mappings_list: Optional[Union[Union[dict, ModelVariableDescriptor], list[Union[dict, ModelVariableDescriptor]]]] = empty_list()
    synonyms: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, BiochemicalName):
            self.name = BiochemicalName(self.name)

        if self.biomarker_term is not None and not isinstance(self.biomarker_term, BiomarkerDescriptor):
            self.biomarker_term = BiomarkerDescriptor(**as_dict(self.biomarker_term))

        if self.presence is not None and not isinstance(self.presence, str):
            self.presence = str(self.presence)

        self._normalize_inlined_as_list(slot_name="readouts", slot_type=BiomarkerReadout, key_name="target", keyed=False)

        if not isinstance(self.reference_ranges, list):
            self.reference_ranges = [self.reference_ranges] if self.reference_ranges is not None else []
        self.reference_ranges = [v if isinstance(v, ReferenceRange) else ReferenceRange(**as_dict(v)) for v in self.reference_ranges]

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.specificity is not None and not isinstance(self.specificity, str):
            self.specificity = str(self.specificity)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.context is not None and not isinstance(self.context, str):
            self.context = str(self.context)

        if self.subtype is not None and not isinstance(self.subtype, str):
            self.subtype = str(self.subtype)

        if not isinstance(self.subtypes, list):
            self.subtypes = [self.subtypes] if self.subtypes is not None else []
        self.subtypes = [v if isinstance(v, str) else str(v) for v in self.subtypes]

        self._normalize_inlined_as_list(slot_name="cell_types", slot_type=CellTypeDescriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="assays", slot_type=AssayDescriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="mappings_list", slot_type=ModelVariableDescriptor, key_name="preferred_term", keyed=False)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HistopathologyFinding(YAMLRoot):
    """
    A histopathologic finding from microscopic examination of tissue. Includes morphologic features, architectural
    patterns, cellular characteristics, growth patterns, and histologic grading.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["HistopathologyFinding"]
    class_class_curie: ClassVar[str] = "dismech:HistopathologyFinding"
    class_name: ClassVar[str] = "HistopathologyFinding"
    class_model_uri: ClassVar[URIRef] = DISMECH.HistopathologyFinding

    name: Union[str, HistopathologyFindingName] = None
    finding_term: Optional[Union[dict, HistopathologyFindingDescriptor]] = None
    description: Optional[str] = None
    frequency: Optional[Union[dict, Any]] = None
    diagnostic: Optional[Union[bool, Bool]] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None
    context: Optional[str] = None
    subtype: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, HistopathologyFindingName):
            self.name = HistopathologyFindingName(self.name)

        if self.finding_term is not None and not isinstance(self.finding_term, HistopathologyFindingDescriptor):
            self.finding_term = HistopathologyFindingDescriptor(**as_dict(self.finding_term))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.diagnostic is not None and not isinstance(self.diagnostic, Bool):
            self.diagnostic = Bool(self.diagnostic)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.context is not None and not isinstance(self.context, str):
            self.context = str(self.context)

        if self.subtype is not None and not isinstance(self.subtype, str):
            self.subtype = str(self.subtype)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImagingFinding(YAMLRoot):
    """
    A finding detected by in-vivo medical imaging (MRI, CT, PET, ultrasound, etc.) that reflects disease
    pathophysiology or defines a diagnostic criterion. The macroscopic / in-vivo counterpart of HistopathologyFinding.
    Captures the modality plus the imaging appearance - NOT acquisition protocol, per-patient reads, or radiology
    decision support.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ImagingFinding"]
    class_class_curie: ClassVar[str] = "dismech:ImagingFinding"
    class_name: ClassVar[str] = "ImagingFinding"
    class_model_uri: ClassVar[URIRef] = DISMECH.ImagingFinding

    name: Union[str, ImagingFindingName] = None
    modality: Optional[Union[str, "ImagingModalityEnum"]] = None
    imaging_finding_term: Optional[Union[dict, ImagingFindingDescriptor]] = None
    description: Optional[str] = None
    located_in: Optional[Union[dict, AnatomicalEntityDescriptor]] = None
    laterality: Optional[Union[str, "LateralityEnum"]] = None
    spatial_extent: Optional[Union[str, "SpatialExtentEnum"]] = None
    phenotype_term: Optional[Union[dict, PhenotypeDescriptor]] = None
    diagnostic: Optional[Union[bool, Bool]] = None
    frequency: Optional[Union[dict, Any]] = None
    modifier: Optional[Union[str, "ModifierEnum"]] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None
    context: Optional[str] = None
    subtype: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ImagingFindingName):
            self.name = ImagingFindingName(self.name)

        if self.modality is not None and not isinstance(self.modality, ImagingModalityEnum):
            self.modality = ImagingModalityEnum(self.modality)

        if self.imaging_finding_term is not None and not isinstance(self.imaging_finding_term, ImagingFindingDescriptor):
            self.imaging_finding_term = ImagingFindingDescriptor(**as_dict(self.imaging_finding_term))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.located_in is not None and not isinstance(self.located_in, AnatomicalEntityDescriptor):
            self.located_in = AnatomicalEntityDescriptor(**as_dict(self.located_in))

        if self.laterality is not None and not isinstance(self.laterality, LateralityEnum):
            self.laterality = LateralityEnum(self.laterality)

        if self.spatial_extent is not None and not isinstance(self.spatial_extent, SpatialExtentEnum):
            self.spatial_extent = SpatialExtentEnum(self.spatial_extent)

        if self.phenotype_term is not None and not isinstance(self.phenotype_term, PhenotypeDescriptor):
            self.phenotype_term = PhenotypeDescriptor(**as_dict(self.phenotype_term))

        if self.diagnostic is not None and not isinstance(self.diagnostic, Bool):
            self.diagnostic = Bool(self.diagnostic)

        if self.modifier is not None and not isinstance(self.modifier, ModifierEnum):
            self.modifier = ModifierEnum(self.modifier)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.context is not None and not isinstance(self.context, str):
            self.context = str(self.context)

        if self.subtype is not None and not isinstance(self.subtype, str):
            self.subtype = str(self.subtype)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Genetic(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Genetic"]
    class_class_curie: ClassVar[str] = "dismech:Genetic"
    class_name: ClassVar[str] = "Genetic"
    class_model_uri: ClassVar[URIRef] = DISMECH.Genetic

    name: Union[str, GeneticName] = None
    gene_term: Optional[Union[dict, GeneDescriptor]] = None
    presence: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    association: Optional[str] = None
    relationship_type: Optional[Union[str, "GeneDiseaseRelationshipEnum"]] = None
    variant_origin: Optional[Union[str, "VariantOriginEnum"]] = None
    review_notes: Optional[str] = None
    subtype: Optional[str] = None
    frequency: Optional[Union[dict, Any]] = None
    case_fractions: Optional[Union[Union[dict, GeneCaseFraction], list[Union[dict, GeneCaseFraction]]]] = empty_list()
    inheritance: Optional[Union[dict[Union[str, InheritanceName], Union[dict, "Inheritance"]], list[Union[dict, "Inheritance"]]]] = empty_dict()
    variants: Optional[Union[dict[Union[str, VariantName], Union[dict, "Variant"]], list[Union[dict, "Variant"]]]] = empty_dict()
    features: Optional[str] = None
    notes: Optional[str] = None
    examples: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, GeneticName):
            self.name = GeneticName(self.name)

        if self.gene_term is not None and not isinstance(self.gene_term, GeneDescriptor):
            self.gene_term = GeneDescriptor(**as_dict(self.gene_term))

        if self.presence is not None and not isinstance(self.presence, str):
            self.presence = str(self.presence)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.association is not None and not isinstance(self.association, str):
            self.association = str(self.association)

        if self.relationship_type is not None and not isinstance(self.relationship_type, GeneDiseaseRelationshipEnum):
            self.relationship_type = GeneDiseaseRelationshipEnum(self.relationship_type)

        if self.variant_origin is not None and not isinstance(self.variant_origin, VariantOriginEnum):
            self.variant_origin = VariantOriginEnum(self.variant_origin)

        if self.review_notes is not None and not isinstance(self.review_notes, str):
            self.review_notes = str(self.review_notes)

        if self.subtype is not None and not isinstance(self.subtype, str):
            self.subtype = str(self.subtype)

        if not isinstance(self.case_fractions, list):
            self.case_fractions = [self.case_fractions] if self.case_fractions is not None else []
        self.case_fractions = [v if isinstance(v, GeneCaseFraction) else GeneCaseFraction(**as_dict(v)) for v in self.case_fractions]

        self._normalize_inlined_as_list(slot_name="inheritance", slot_type=Inheritance, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="variants", slot_type=Variant, key_name="name", keyed=True)

        if self.features is not None and not isinstance(self.features, str):
            self.features = str(self.features)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if not isinstance(self.examples, list):
            self.examples = [self.examples] if self.examples is not None else []
        self.examples = [v if isinstance(v, str) else str(v) for v in self.examples]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Environmental(YAMLRoot):
    """
    An environmental factor, exposure, or context relevant to disease
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Environmental"]
    class_class_curie: ClassVar[str] = "dismech:Environmental"
    class_name: ClassVar[str] = "Environmental"
    class_model_uri: ClassVar[URIRef] = DISMECH.Environmental

    name: Union[str, EnvironmentalName] = None
    presence: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None
    description: Optional[str] = None
    chemicals: Optional[Union[str, list[str]]] = empty_list()
    synonyms: Optional[Union[str, list[str]]] = empty_list()
    effect: Optional[str] = None
    examples: Optional[Union[str, list[str]]] = empty_list()
    review_notes: Optional[str] = None
    exposure_term: Optional[Union[dict, ExposureDescriptor]] = None
    environment_context: Optional[Union[dict, EnvironmentDescriptor]] = None
    food_source: Optional[Union[dict, FoodDescriptor]] = None
    influences_mechanisms: Optional[Union[Union[dict, EnvironmentalMechanismTarget], list[Union[dict, EnvironmentalMechanismTarget]]]] = empty_list()
    exposure_classifications: Optional[Union[dict, "ExposureClassifications"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, EnvironmentalName):
            self.name = EnvironmentalName(self.name)

        if self.presence is not None and not isinstance(self.presence, str):
            self.presence = str(self.presence)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.chemicals, list):
            self.chemicals = [self.chemicals] if self.chemicals is not None else []
        self.chemicals = [v if isinstance(v, str) else str(v) for v in self.chemicals]

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        if self.effect is not None and not isinstance(self.effect, str):
            self.effect = str(self.effect)

        if not isinstance(self.examples, list):
            self.examples = [self.examples] if self.examples is not None else []
        self.examples = [v if isinstance(v, str) else str(v) for v in self.examples]

        if self.review_notes is not None and not isinstance(self.review_notes, str):
            self.review_notes = str(self.review_notes)

        if self.exposure_term is not None and not isinstance(self.exposure_term, ExposureDescriptor):
            self.exposure_term = ExposureDescriptor(**as_dict(self.exposure_term))

        if self.environment_context is not None and not isinstance(self.environment_context, EnvironmentDescriptor):
            self.environment_context = EnvironmentDescriptor(**as_dict(self.environment_context))

        if self.food_source is not None and not isinstance(self.food_source, FoodDescriptor):
            self.food_source = FoodDescriptor(**as_dict(self.food_source))

        self._normalize_inlined_as_list(slot_name="influences_mechanisms", slot_type=EnvironmentalMechanismTarget, key_name="target", keyed=False)

        if self.exposure_classifications is not None and not isinstance(self.exposure_classifications, ExposureClassifications):
            self.exposure_classifications = ExposureClassifications(**as_dict(self.exposure_classifications))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Disease(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Disease"]
    class_class_curie: ClassVar[str] = "dismech:Disease"
    class_name: ClassVar[str] = "Disease"
    class_model_uri: ClassVar[URIRef] = DISMECH.Disease

    name: Union[str, DiseaseName] = None
    disease_term: Optional[Union[dict, DiseaseDescriptor]] = None
    creation_date: Optional[str] = None
    updated_date: Optional[str] = None
    description: Optional[str] = None
    references: Optional[Union[dict[Union[str, PublicationReferenceReference], Union[dict, PublicationReference]], list[Union[dict, PublicationReference]]]] = empty_dict()
    category: Optional[str] = None
    parents: Optional[Union[str, list[str]]] = empty_list()
    has_subtypes: Optional[Union[dict[Union[str, SubtypeName], Union[dict, Subtype]], list[Union[dict, Subtype]]]] = empty_dict()
    prevalence: Optional[Union[Union[dict, Prevalence], list[Union[dict, Prevalence]]]] = empty_list()
    progression: Optional[Union[Union[dict, ProgressionInfo], list[Union[dict, ProgressionInfo]]]] = empty_list()
    clinical_burden: Optional[Union[dict, ClinicalBurden]] = None
    pathophysiology: Optional[Union[dict[Union[str, PathophysiologyName], Union[dict, Pathophysiology]], list[Union[dict, Pathophysiology]]]] = empty_dict()
    mechanistic_hypotheses: Optional[Union[Union[dict, "MechanisticHypothesis"], list[Union[dict, "MechanisticHypothesis"]]]] = empty_list()
    phenotypes: Optional[Union[dict[Union[str, PhenotypeName], Union[dict, Phenotype]], list[Union[dict, Phenotype]]]] = empty_dict()
    histopathology: Optional[Union[dict[Union[str, HistopathologyFindingName], Union[dict, HistopathologyFinding]], list[Union[dict, HistopathologyFinding]]]] = empty_dict()
    imaging_findings: Optional[Union[dict[Union[str, ImagingFindingName], Union[dict, ImagingFinding]], list[Union[dict, ImagingFinding]]]] = empty_dict()
    biochemical: Optional[Union[dict[Union[str, BiochemicalName], Union[dict, Biochemical]], list[Union[dict, Biochemical]]]] = empty_dict()
    stages: Optional[Union[dict[Union[str, StageName], Union[dict, "Stage"]], list[Union[dict, "Stage"]]]] = empty_dict()
    genetic: Optional[Union[dict[Union[str, GeneticName], Union[dict, Genetic]], list[Union[dict, Genetic]]]] = empty_dict()
    variants: Optional[Union[dict[Union[str, VariantName], Union[dict, "Variant"]], list[Union[dict, "Variant"]]]] = empty_dict()
    environmental: Optional[Union[dict[Union[str, EnvironmentalName], Union[dict, Environmental]], list[Union[dict, Environmental]]]] = empty_dict()
    treatments: Optional[Union[dict[Union[str, TreatmentName], Union[dict, "Treatment"]], list[Union[dict, "Treatment"]]]] = empty_dict()
    categories: Optional[Union[str, list[str]]] = empty_list()
    module_categories: Optional[Union[Union[str, "ModuleCategoryEnum"], list[Union[str, "ModuleCategoryEnum"]]]] = empty_list()
    infectious_agent: Optional[Union[dict[Union[str, InfectiousAgentName], Union[dict, "InfectiousAgent"]], list[Union[dict, "InfectiousAgent"]]]] = empty_dict()
    agent_life_cycle: Optional[Union[dict, "AgentLifeCycle"]] = None
    transmission: Optional[Union[dict[Union[str, TransmissionName], Union[dict, "Transmission"]], list[Union[dict, "Transmission"]]]] = empty_dict()
    modeling_considerations: Optional[Union[dict[Union[str, ModelingConsiderationName], Union[dict, "ModelingConsideration"]], list[Union[dict, "ModelingConsideration"]]]] = empty_dict()
    epidemiology: Optional[Union[dict[Union[str, EpidemiologyInfoName], Union[dict, EpidemiologyInfo]], list[Union[dict, EpidemiologyInfo]]]] = empty_dict()
    diagnosis: Optional[Union[dict[Union[str, DiagnosisName], Union[dict, "Diagnosis"]], list[Union[dict, "Diagnosis"]]]] = empty_dict()
    differential_diagnoses: Optional[Union[dict[Union[str, DifferentialDiagnosisName], Union[dict, DifferentialDiagnosis]], list[Union[dict, DifferentialDiagnosis]]]] = empty_dict()
    synonyms: Optional[Union[str, list[str]]] = empty_list()
    inheritance: Optional[Union[dict[Union[str, InheritanceName], Union[dict, "Inheritance"]], list[Union[dict, "Inheritance"]]]] = empty_dict()
    animal_models: Optional[Union[Union[dict, "AnimalModel"], list[Union[dict, "AnimalModel"]]]] = empty_list()
    experimental_models: Optional[Union[dict[Union[str, ExperimentalModelName], Union[dict, ExperimentalModel]], list[Union[dict, ExperimentalModel]]]] = empty_dict()
    datasets: Optional[Union[dict[Union[str, DatasetAccession], Union[dict, Dataset]], list[Union[dict, Dataset]]]] = empty_dict()
    clinical_trials: Optional[Union[dict[Union[str, ClinicalTrialName], Union[dict, ClinicalTrial]], list[Union[dict, ClinicalTrial]]]] = empty_dict()
    surrogate_endpoints: Optional[Union[dict[Union[str, SurrogateEndpointRowId], Union[dict, SurrogateEndpoint]], list[Union[dict, SurrogateEndpoint]]]] = empty_dict()
    computational_models: Optional[Union[dict[Union[str, ComputationalModelName], Union[dict, ComputationalModel]], list[Union[dict, ComputationalModel]]]] = empty_dict()
    classifications: Optional[Union[dict, "DiseaseClassifications"]] = None
    definitions: Optional[Union[dict[Union[str, DefinitionName], Union[dict, "Definition"]], list[Union[dict, "Definition"]]]] = empty_dict()
    gene_sets: Optional[Union[Union[dict, GeneSetAssociation], list[Union[dict, GeneSetAssociation]]]] = empty_list()
    mappings: Optional[Union[dict, "DiseaseMappings"]] = None
    external_assertions: Optional[Union[dict[Union[str, ExternalAssertionName], Union[dict, ExternalAssertion]], list[Union[dict, ExternalAssertion]]]] = empty_dict()
    tracked_issues: Optional[Union[Union[dict, TrackedIssue], list[Union[dict, TrackedIssue]]]] = empty_list()
    discussions: Optional[Union[Union[dict, "Discussion"], list[Union[dict, "Discussion"]]]] = empty_list()
    notes: Optional[str] = None
    review_notes: Optional[str] = None
    curation_history: Optional[Union[Union[dict, CurationEvent], list[Union[dict, CurationEvent]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, DiseaseName):
            self.name = DiseaseName(self.name)

        if self.disease_term is not None and not isinstance(self.disease_term, DiseaseDescriptor):
            self.disease_term = DiseaseDescriptor(**as_dict(self.disease_term))

        if self.creation_date is not None and not isinstance(self.creation_date, str):
            self.creation_date = str(self.creation_date)

        if self.updated_date is not None and not isinstance(self.updated_date, str):
            self.updated_date = str(self.updated_date)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="references", slot_type=PublicationReference, key_name="reference", keyed=True)

        if self.category is not None and not isinstance(self.category, str):
            self.category = str(self.category)

        if not isinstance(self.parents, list):
            self.parents = [self.parents] if self.parents is not None else []
        self.parents = [v if isinstance(v, str) else str(v) for v in self.parents]

        self._normalize_inlined_as_list(slot_name="has_subtypes", slot_type=Subtype, key_name="name", keyed=True)

        if not isinstance(self.prevalence, list):
            self.prevalence = [self.prevalence] if self.prevalence is not None else []
        self.prevalence = [v if isinstance(v, Prevalence) else Prevalence(**as_dict(v)) for v in self.prevalence]

        if not isinstance(self.progression, list):
            self.progression = [self.progression] if self.progression is not None else []
        self.progression = [v if isinstance(v, ProgressionInfo) else ProgressionInfo(**as_dict(v)) for v in self.progression]

        if self.clinical_burden is not None and not isinstance(self.clinical_burden, ClinicalBurden):
            self.clinical_burden = ClinicalBurden(**as_dict(self.clinical_burden))

        self._normalize_inlined_as_list(slot_name="pathophysiology", slot_type=Pathophysiology, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="mechanistic_hypotheses", slot_type=MechanisticHypothesis, key_name="hypothesis_group_id", keyed=False)

        self._normalize_inlined_as_list(slot_name="phenotypes", slot_type=Phenotype, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="histopathology", slot_type=HistopathologyFinding, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="imaging_findings", slot_type=ImagingFinding, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="biochemical", slot_type=Biochemical, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="stages", slot_type=Stage, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="genetic", slot_type=Genetic, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="variants", slot_type=Variant, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="environmental", slot_type=Environmental, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="treatments", slot_type=Treatment, key_name="name", keyed=True)

        if not isinstance(self.categories, list):
            self.categories = [self.categories] if self.categories is not None else []
        self.categories = [v if isinstance(v, str) else str(v) for v in self.categories]

        if not isinstance(self.module_categories, list):
            self.module_categories = [self.module_categories] if self.module_categories is not None else []
        self.module_categories = [v if isinstance(v, ModuleCategoryEnum) else ModuleCategoryEnum(v) for v in self.module_categories]

        self._normalize_inlined_as_list(slot_name="infectious_agent", slot_type=InfectiousAgent, key_name="name", keyed=True)

        if self.agent_life_cycle is not None and not isinstance(self.agent_life_cycle, AgentLifeCycle):
            self.agent_life_cycle = AgentLifeCycle(**as_dict(self.agent_life_cycle))

        self._normalize_inlined_as_list(slot_name="transmission", slot_type=Transmission, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="modeling_considerations", slot_type=ModelingConsideration, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="epidemiology", slot_type=EpidemiologyInfo, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="diagnosis", slot_type=Diagnosis, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="differential_diagnoses", slot_type=DifferentialDiagnosis, key_name="name", keyed=True)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        self._normalize_inlined_as_list(slot_name="inheritance", slot_type=Inheritance, key_name="name", keyed=True)

        if not isinstance(self.animal_models, list):
            self.animal_models = [self.animal_models] if self.animal_models is not None else []
        self.animal_models = [v if isinstance(v, AnimalModel) else AnimalModel(**as_dict(v)) for v in self.animal_models]

        self._normalize_inlined_as_list(slot_name="experimental_models", slot_type=ExperimentalModel, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="datasets", slot_type=Dataset, key_name="accession", keyed=True)

        self._normalize_inlined_as_list(slot_name="clinical_trials", slot_type=ClinicalTrial, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="surrogate_endpoints", slot_type=SurrogateEndpoint, key_name="row_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="computational_models", slot_type=ComputationalModel, key_name="name", keyed=True)

        if self.classifications is not None and not isinstance(self.classifications, DiseaseClassifications):
            self.classifications = DiseaseClassifications(**as_dict(self.classifications))

        self._normalize_inlined_as_list(slot_name="definitions", slot_type=Definition, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="gene_sets", slot_type=GeneSetAssociation, key_name="gene_set", keyed=False)

        if self.mappings is not None and not isinstance(self.mappings, DiseaseMappings):
            self.mappings = DiseaseMappings(**as_dict(self.mappings))

        self._normalize_inlined_as_list(slot_name="external_assertions", slot_type=ExternalAssertion, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="tracked_issues", slot_type=TrackedIssue, key_name="url", keyed=False)

        self._normalize_inlined_as_list(slot_name="discussions", slot_type=Discussion, key_name="discussion_id", keyed=False)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.review_notes is not None and not isinstance(self.review_notes, str):
            self.review_notes = str(self.review_notes)

        self._normalize_inlined_as_list(slot_name="curation_history", slot_type=CurationEvent, key_name="curation_timestamp", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Stage(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Stage"]
    class_class_curie: ClassVar[str] = "dismech:Stage"
    class_name: ClassVar[str] = "Stage"
    class_model_uri: ClassVar[URIRef] = DISMECH.Stage

    name: Union[str, StageName] = None
    description: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None
    context: Optional[str] = None
    review_notes: Optional[str] = None
    role: Optional[str] = None
    examples: Optional[Union[str, list[str]]] = empty_list()
    pathophysiology: Optional[Union[dict[Union[str, PathophysiologyName], Union[dict, Pathophysiology]], list[Union[dict, Pathophysiology]]]] = empty_dict()
    substages: Optional[Union[dict[Union[str, StageName], Union[dict, "Stage"]], list[Union[dict, "Stage"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, StageName):
            self.name = StageName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.context is not None and not isinstance(self.context, str):
            self.context = str(self.context)

        if self.review_notes is not None and not isinstance(self.review_notes, str):
            self.review_notes = str(self.review_notes)

        if self.role is not None and not isinstance(self.role, str):
            self.role = str(self.role)

        if not isinstance(self.examples, list):
            self.examples = [self.examples] if self.examples is not None else []
        self.examples = [v if isinstance(v, str) else str(v) for v in self.examples]

        self._normalize_inlined_as_list(slot_name="pathophysiology", slot_type=Pathophysiology, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="substages", slot_type=Stage, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AgentLifeCycle(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["AgentLifeCycle"]
    class_class_curie: ClassVar[str] = "dismech:AgentLifeCycle"
    class_name: ClassVar[str] = "AgentLifeCycle"
    class_model_uri: ClassVar[URIRef] = DISMECH.AgentLifeCycle

    description: Optional[str] = None
    life_cycle_stages: Optional[Union[dict[Union[str, AgentLifeCycleStageName], Union[dict, "AgentLifeCycleStage"]], list[Union[dict, "AgentLifeCycleStage"]]]] = empty_dict()
    hosts: Optional[Union[Union[dict, HostDescriptor], list[Union[dict, HostDescriptor]]]] = empty_list()
    vectors: Optional[Union[str, list[str]]] = empty_list()
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None
    context: Optional[str] = None
    review_notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="life_cycle_stages", slot_type=AgentLifeCycleStage, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="hosts", slot_type=HostDescriptor, key_name="preferred_term", keyed=False)

        if not isinstance(self.vectors, list):
            self.vectors = [self.vectors] if self.vectors is not None else []
        self.vectors = [v if isinstance(v, str) else str(v) for v in self.vectors]

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.context is not None and not isinstance(self.context, str):
            self.context = str(self.context)

        if self.review_notes is not None and not isinstance(self.review_notes, str):
            self.review_notes = str(self.review_notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AgentLifeCycleStage(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["AgentLifeCycleStage"]
    class_class_curie: ClassVar[str] = "dismech:AgentLifeCycleStage"
    class_name: ClassVar[str] = "AgentLifeCycleStage"
    class_model_uri: ClassVar[URIRef] = DISMECH.AgentLifeCycleStage

    name: Union[str, AgentLifeCycleStageName] = None
    life_cycle_stage_term: Optional[Union[dict, LifeCycleStageDescriptor]] = None
    description: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None
    context: Optional[str] = None
    review_notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, AgentLifeCycleStageName):
            self.name = AgentLifeCycleStageName(self.name)

        if self.life_cycle_stage_term is not None and not isinstance(self.life_cycle_stage_term, LifeCycleStageDescriptor):
            self.life_cycle_stage_term = LifeCycleStageDescriptor(**as_dict(self.life_cycle_stage_term))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.context is not None and not isinstance(self.context, str):
            self.context = str(self.context)

        if self.review_notes is not None and not isinstance(self.review_notes, str):
            self.review_notes = str(self.review_notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnimalModel(YAMLRoot):
    """
    A whole-organism animal model of the disease. This is the home for animal models; non-animal systems (organoids,
    organ-chips, cell lines, iPSC-derived and primary cultures) belong in `experimental_models` as ExperimentalModel.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["AnimalModel"]
    class_class_curie: ClassVar[str] = "dismech:AnimalModel"
    class_name: ClassVar[str] = "AnimalModel"
    class_model_uri: ClassVar[URIRef] = DISMECH.AnimalModel

    species: Optional[str] = None
    genotype: Optional[str] = None
    background: Optional[str] = None
    genes: Optional[Union[Union[dict, GeneDescriptor], list[Union[dict, GeneDescriptor]]]] = empty_list()
    category: Optional[str] = None
    alleles: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[str] = None
    publication: Optional[str] = None
    associated_phenotypes: Optional[Union[str, list[str]]] = empty_list()
    modeled_mechanisms: Optional[Union[Union[dict, ModelMechanismLink], list[Union[dict, ModelMechanismLink]]]] = empty_list()
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.species is not None and not isinstance(self.species, str):
            self.species = str(self.species)

        if self.genotype is not None and not isinstance(self.genotype, str):
            self.genotype = str(self.genotype)

        if self.background is not None and not isinstance(self.background, str):
            self.background = str(self.background)

        self._normalize_inlined_as_list(slot_name="genes", slot_type=GeneDescriptor, key_name="preferred_term", keyed=False)

        if self.category is not None and not isinstance(self.category, str):
            self.category = str(self.category)

        if not isinstance(self.alleles, list):
            self.alleles = [self.alleles] if self.alleles is not None else []
        self.alleles = [v if isinstance(v, str) else str(v) for v in self.alleles]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.publication is not None and not isinstance(self.publication, str):
            self.publication = str(self.publication)

        if not isinstance(self.associated_phenotypes, list):
            self.associated_phenotypes = [self.associated_phenotypes] if self.associated_phenotypes is not None else []
        self.associated_phenotypes = [v if isinstance(v, str) else str(v) for v in self.associated_phenotypes]

        self._normalize_inlined_as_list(slot_name="modeled_mechanisms", slot_type=ModelMechanismLink, key_name="target", keyed=False)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Treatment(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Treatment"]
    class_class_curie: ClassVar[str] = "dismech:Treatment"
    class_name: ClassVar[str] = "Treatment"
    class_model_uri: ClassVar[URIRef] = DISMECH.Treatment

    name: Union[str, TreatmentName] = None
    description: Optional[str] = None
    action_category: Optional[Union[str, "MedicalActionCategoryEnum"]] = None
    treatment_term: Optional[Union[dict, TreatmentDescriptor]] = None
    regimen_term: Optional[Union[dict, RegimenDescriptor]] = None
    therapeutic_modality: Optional[Union[str, "TherapeuticModalityEnum"]] = None
    aso_details: Optional[Union[dict, "AntisenseOligonucleotideDetail"]] = None
    target_phenotypes: Optional[Union[Union[dict, PhenotypeDescriptor], list[Union[dict, PhenotypeDescriptor]]]] = empty_list()
    target_mechanisms: Optional[Union[Union[dict, TreatmentMechanismTarget], list[Union[dict, TreatmentMechanismTarget]]]] = empty_list()
    pdb_structures: Optional[Union[Union[dict, ProteinStructure], list[Union[dict, ProteinStructure]]]] = empty_list()
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None
    context: Optional[str] = None
    review_notes: Optional[str] = None
    role: Optional[str] = None
    mechanism: Optional[Union[dict[Union[str, MechanismName], Union[dict, "Mechanism"]], list[Union[dict, "Mechanism"]]]] = empty_dict()
    examples: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, TreatmentName):
            self.name = TreatmentName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.action_category is not None and not isinstance(self.action_category, MedicalActionCategoryEnum):
            self.action_category = MedicalActionCategoryEnum(self.action_category)

        if self.treatment_term is not None and not isinstance(self.treatment_term, TreatmentDescriptor):
            self.treatment_term = TreatmentDescriptor(**as_dict(self.treatment_term))

        if self.regimen_term is not None and not isinstance(self.regimen_term, RegimenDescriptor):
            self.regimen_term = RegimenDescriptor(**as_dict(self.regimen_term))

        if self.therapeutic_modality is not None and not isinstance(self.therapeutic_modality, TherapeuticModalityEnum):
            self.therapeutic_modality = TherapeuticModalityEnum(self.therapeutic_modality)

        if self.aso_details is not None and not isinstance(self.aso_details, AntisenseOligonucleotideDetail):
            self.aso_details = AntisenseOligonucleotideDetail(**as_dict(self.aso_details))

        self._normalize_inlined_as_list(slot_name="target_phenotypes", slot_type=PhenotypeDescriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="target_mechanisms", slot_type=TreatmentMechanismTarget, key_name="target", keyed=False)

        self._normalize_inlined_as_list(slot_name="pdb_structures", slot_type=ProteinStructure, key_name="pdb_id", keyed=False)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.context is not None and not isinstance(self.context, str):
            self.context = str(self.context)

        if self.review_notes is not None and not isinstance(self.review_notes, str):
            self.review_notes = str(self.review_notes)

        if self.role is not None and not isinstance(self.role, str):
            self.role = str(self.role)

        self._normalize_inlined_as_list(slot_name="mechanism", slot_type=Mechanism, key_name="name", keyed=True)

        if not isinstance(self.examples, list):
            self.examples = [self.examples] if self.examples is not None else []
        self.examples = [v if isinstance(v, str) else str(v) for v in self.examples]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AntisenseOligonucleotideDetail(YAMLRoot):
    """
    Structured attributes specific to an antisense oligonucleotide (ASO) treatment: its molecular mechanism, RNA
    target, splice exon (for splice-switching ASOs), backbone chemistry, and targeting conjugate. Attach via the
    aso_details slot on a Treatment whose therapeutic_modality is ANTISENSE_OLIGONUCLEOTIDE.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["AntisenseOligonucleotideDetail"]
    class_class_curie: ClassVar[str] = "dismech:AntisenseOligonucleotideDetail"
    class_name: ClassVar[str] = "AntisenseOligonucleotideDetail"
    class_model_uri: ClassVar[URIRef] = DISMECH.AntisenseOligonucleotideDetail

    aso_mechanism: Optional[Union[str, "AsoMechanismEnum"]] = None
    target_gene: Optional[Union[dict, GeneDescriptor]] = None
    target_transcript: Optional[str] = None
    target_exon: Optional[str] = None
    aso_chemistry: Optional[Union[str, "AsoChemistryEnum"]] = None
    conjugation: Optional[Union[str, "AsoConjugationEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.aso_mechanism is not None and not isinstance(self.aso_mechanism, AsoMechanismEnum):
            self.aso_mechanism = AsoMechanismEnum(self.aso_mechanism)

        if self.target_gene is not None and not isinstance(self.target_gene, GeneDescriptor):
            self.target_gene = GeneDescriptor(**as_dict(self.target_gene))

        if self.target_transcript is not None and not isinstance(self.target_transcript, str):
            self.target_transcript = str(self.target_transcript)

        if self.target_exon is not None and not isinstance(self.target_exon, str):
            self.target_exon = str(self.target_exon)

        if self.aso_chemistry is not None and not isinstance(self.aso_chemistry, AsoChemistryEnum):
            self.aso_chemistry = AsoChemistryEnum(self.aso_chemistry)

        if self.conjugation is not None and not isinstance(self.conjugation, AsoConjugationEnum):
            self.conjugation = AsoConjugationEnum(self.conjugation)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InfectiousAgent(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["InfectiousAgent"]
    class_class_curie: ClassVar[str] = "dismech:InfectiousAgent"
    class_name: ClassVar[str] = "InfectiousAgent"
    class_model_uri: ClassVar[URIRef] = DISMECH.InfectiousAgent

    name: Union[str, InfectiousAgentName] = None
    infectious_agent_term: Optional[Union[dict, OrganismDescriptor]] = None
    food_source: Optional[Union[dict, FoodDescriptor]] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    description: Optional[str] = None
    has_subtypes: Optional[Union[dict[Union[str, SubtypeName], Union[dict, Subtype]], list[Union[dict, Subtype]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, InfectiousAgentName):
            self.name = InfectiousAgentName(self.name)

        if self.infectious_agent_term is not None and not isinstance(self.infectious_agent_term, OrganismDescriptor):
            self.infectious_agent_term = OrganismDescriptor(**as_dict(self.infectious_agent_term))

        if self.food_source is not None and not isinstance(self.food_source, FoodDescriptor):
            self.food_source = FoodDescriptor(**as_dict(self.food_source))

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="has_subtypes", slot_type=Subtype, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Transmission(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Transmission"]
    class_class_curie: ClassVar[str] = "dismech:Transmission"
    class_name: ClassVar[str] = "Transmission"
    class_model_uri: ClassVar[URIRef] = DISMECH.Transmission

    name: Union[str, TransmissionName] = None
    description: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None
    effect: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, TransmissionName):
            self.name = TransmissionName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.effect is not None and not isinstance(self.effect, str):
            self.effect = str(self.effect)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Assay(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Assay"]
    class_class_curie: ClassVar[str] = "dismech:Assay"
    class_name: ClassVar[str] = "Assay"
    class_model_uri: ClassVar[URIRef] = DISMECH.Assay

    name: Union[str, AssayName] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, AssayName):
            self.name = AssayName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Diagnosis(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Diagnosis"]
    class_class_curie: ClassVar[str] = "dismech:Diagnosis"
    class_name: ClassVar[str] = "Diagnosis"
    class_model_uri: ClassVar[URIRef] = DISMECH.Diagnosis

    name: Union[str, DiagnosisName] = None
    diagnosis_term: Optional[Union[dict, TreatmentDescriptor]] = None
    presence: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None
    results: Optional[str] = None
    markers: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, DiagnosisName):
            self.name = DiagnosisName(self.name)

        if self.diagnosis_term is not None and not isinstance(self.diagnosis_term, TreatmentDescriptor):
            self.diagnosis_term = TreatmentDescriptor(**as_dict(self.diagnosis_term))

        if self.presence is not None and not isinstance(self.presence, str):
            self.presence = str(self.presence)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.results is not None and not isinstance(self.results, str):
            self.results = str(self.results)

        if self.markers is not None and not isinstance(self.markers, str):
            self.markers = str(self.markers)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Inheritance(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Inheritance"]
    class_class_curie: ClassVar[str] = "dismech:Inheritance"
    class_name: ClassVar[str] = "Inheritance"
    class_model_uri: ClassVar[URIRef] = DISMECH.Inheritance

    name: Union[str, InheritanceName] = None
    inheritance_term: Optional[Union[dict, InheritanceDescriptor]] = None
    penetrance: Optional[Union[str, "PenetranceEnum"]] = None
    penetrance_percentage: Optional[str] = None
    expressivity: Optional[Union[str, "ExpressivityEnum"]] = None
    de_novo_rate: Optional[str] = None
    parent_of_origin_effect: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, InheritanceName):
            self.name = InheritanceName(self.name)

        if self.inheritance_term is not None and not isinstance(self.inheritance_term, InheritanceDescriptor):
            self.inheritance_term = InheritanceDescriptor(**as_dict(self.inheritance_term))

        if self.penetrance is not None and not isinstance(self.penetrance, PenetranceEnum):
            self.penetrance = PenetranceEnum(self.penetrance)

        if self.penetrance_percentage is not None and not isinstance(self.penetrance_percentage, str):
            self.penetrance_percentage = str(self.penetrance_percentage)

        if self.expressivity is not None and not isinstance(self.expressivity, ExpressivityEnum):
            self.expressivity = ExpressivityEnum(self.expressivity)

        if self.de_novo_rate is not None and not isinstance(self.de_novo_rate, str):
            self.de_novo_rate = str(self.de_novo_rate)

        if self.parent_of_origin_effect is not None and not isinstance(self.parent_of_origin_effect, str):
            self.parent_of_origin_effect = str(self.parent_of_origin_effect)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Variant(YAMLRoot):
    """
    A genetic variant associated with a disease, including coding and non-coding regulatory variants. For regulatory
    variants, use regulatory_category to classify the variant's impact on gene expression (LOE/mLOE/GOE per Cheng et
    al. 2024).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Variant"]
    class_class_curie: ClassVar[str] = "dismech:Variant"
    class_name: ClassVar[str] = "Variant"
    class_model_uri: ClassVar[URIRef] = DISMECH.Variant

    name: Union[str, VariantName] = None
    description: Optional[str] = None
    gene: Optional[Union[dict, GeneDescriptor]] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    functional_effects: Optional[Union[Union[dict, "FunctionalEffect"], list[Union[dict, "FunctionalEffect"]]]] = empty_list()
    synonyms: Optional[Union[str, list[str]]] = empty_list()
    identifiers: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    external_assertions: Optional[Union[dict[Union[str, ExternalAssertionName], Union[dict, ExternalAssertion]], list[Union[dict, ExternalAssertion]]]] = empty_dict()
    sequence_length: Optional[int] = None
    clinical_significance: Optional[Union[str, "ClinicalSignificanceEnum"]] = None
    type: Optional[str] = None
    regulatory_category: Optional[Union[str, "RegulatoryVariantCategoryEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, VariantName):
            self.name = VariantName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.gene is not None and not isinstance(self.gene, GeneDescriptor):
            self.gene = GeneDescriptor(**as_dict(self.gene))

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if not isinstance(self.functional_effects, list):
            self.functional_effects = [self.functional_effects] if self.functional_effects is not None else []
        self.functional_effects = [v if isinstance(v, FunctionalEffect) else FunctionalEffect(**as_dict(v)) for v in self.functional_effects]

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        if not isinstance(self.identifiers, list):
            self.identifiers = [self.identifiers] if self.identifiers is not None else []
        self.identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.identifiers]

        self._normalize_inlined_as_list(slot_name="external_assertions", slot_type=ExternalAssertion, key_name="name", keyed=True)

        if self.sequence_length is not None and not isinstance(self.sequence_length, int):
            self.sequence_length = int(self.sequence_length)

        if self.clinical_significance is not None and not isinstance(self.clinical_significance, ClinicalSignificanceEnum):
            self.clinical_significance = ClinicalSignificanceEnum(self.clinical_significance)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.regulatory_category is not None and not isinstance(self.regulatory_category, RegulatoryVariantCategoryEnum):
            self.regulatory_category = RegulatoryVariantCategoryEnum(self.regulatory_category)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FunctionalEffect(YAMLRoot):
    """
    Describes the functional consequence of a genetic variant, including regulatory impact classification
    (LOE/mLOE/GOE) for non-coding variants and the type of regulatory element affected.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["FunctionalEffect"]
    class_class_curie: ClassVar[str] = "dismech:FunctionalEffect"
    class_name: ClassVar[str] = "FunctionalEffect"
    class_model_uri: ClassVar[URIRef] = DISMECH.FunctionalEffect

    function: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    regulatory_category: Optional[Union[str, "RegulatoryVariantCategoryEnum"]] = None
    regulatory_element_type: Optional[Union[str, "RegulatoryElementTypeEnum"]] = None
    affected_cell_types: Optional[Union[Union[dict, CellTypeDescriptor], list[Union[dict, CellTypeDescriptor]]]] = empty_list()
    affected_developmental_stage: Optional[str] = None
    regulatory_mechanism: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.function is not None and not isinstance(self.function, str):
            self.function = str(self.function)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.regulatory_category is not None and not isinstance(self.regulatory_category, RegulatoryVariantCategoryEnum):
            self.regulatory_category = RegulatoryVariantCategoryEnum(self.regulatory_category)

        if self.regulatory_element_type is not None and not isinstance(self.regulatory_element_type, RegulatoryElementTypeEnum):
            self.regulatory_element_type = RegulatoryElementTypeEnum(self.regulatory_element_type)

        self._normalize_inlined_as_list(slot_name="affected_cell_types", slot_type=CellTypeDescriptor, key_name="preferred_term", keyed=False)

        if self.affected_developmental_stage is not None and not isinstance(self.affected_developmental_stage, str):
            self.affected_developmental_stage = str(self.affected_developmental_stage)

        if self.regulatory_mechanism is not None and not isinstance(self.regulatory_mechanism, str):
            self.regulatory_mechanism = str(self.regulatory_mechanism)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Mechanism(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Mechanism"]
    class_class_curie: ClassVar[str] = "dismech:Mechanism"
    class_name: ClassVar[str] = "Mechanism"
    class_model_uri: ClassVar[URIRef] = DISMECH.Mechanism

    name: Union[str, MechanismName] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, MechanismName):
            self.name = MechanismName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModelingConsideration(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ModelingConsideration"]
    class_class_curie: ClassVar[str] = "dismech:ModelingConsideration"
    class_name: ClassVar[str] = "ModelingConsideration"
    class_model_uri: ClassVar[URIRef] = DISMECH.ModelingConsideration

    name: Union[str, ModelingConsiderationName] = None
    description: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ModelingConsiderationName):
            self.name = ModelingConsiderationName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ClassificationAssignment(YAMLRoot):
    """
    Base class for classification assignments with evidence
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ClassificationAssignment"]
    class_class_curie: ClassVar[str] = "dismech:ClassificationAssignment"
    class_name: ClassVar[str] = "ClassificationAssignment"
    class_model_uri: ClassVar[URIRef] = DISMECH.ClassificationAssignment

    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ICDOMorphologyAssignment(ClassificationAssignment):
    """
    ICD-O morphology classification assignment for neoplastic diseases
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ICDOMorphologyAssignment"]
    class_class_curie: ClassVar[str] = "dismech:ICDOMorphologyAssignment"
    class_name: ClassVar[str] = "ICDOMorphologyAssignment"
    class_model_uri: ClassVar[URIRef] = DISMECH.ICDOMorphologyAssignment

    classification_value: Union[str, "ICDOMorphologyEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.classification_value):
            self.MissingRequiredField("classification_value")
        if not isinstance(self.classification_value, ICDOMorphologyEnum):
            self.classification_value = ICDOMorphologyEnum(self.classification_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HarrisonsChapterAssignment(ClassificationAssignment):
    """
    Harrison's internal medicine chapter classification assignment
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["HarrisonsChapterAssignment"]
    class_class_curie: ClassVar[str] = "dismech:HarrisonsChapterAssignment"
    class_name: ClassVar[str] = "HarrisonsChapterAssignment"
    class_model_uri: ClassVar[URIRef] = DISMECH.HarrisonsChapterAssignment

    classification_value: Union[str, "HarrisonsChapterEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.classification_value):
            self.MissingRequiredField("classification_value")
        if not isinstance(self.classification_value, HarrisonsChapterEnum):
            self.classification_value = HarrisonsChapterEnum(self.classification_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LysosomalStorageAssignment(ClassificationAssignment):
    """
    Lysosomal storage disease biochemical classification assignment
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["LysosomalStorageAssignment"]
    class_class_curie: ClassVar[str] = "dismech:LysosomalStorageAssignment"
    class_name: ClassVar[str] = "LysosomalStorageAssignment"
    class_model_uri: ClassVar[URIRef] = DISMECH.LysosomalStorageAssignment

    classification_value: Union[str, "LysosomalStorageEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.classification_value):
            self.MissingRequiredField("classification_value")
        if not isinstance(self.classification_value, LysosomalStorageEnum):
            self.classification_value = LysosomalStorageEnum(self.classification_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MechanisticNosologyAssignment(ClassificationAssignment):
    """
    Mechanistic/pathway-based disease classification assignment
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["MechanisticNosologyAssignment"]
    class_class_curie: ClassVar[str] = "dismech:MechanisticNosologyAssignment"
    class_name: ClassVar[str] = "MechanisticNosologyAssignment"
    class_model_uri: ClassVar[URIRef] = DISMECH.MechanisticNosologyAssignment

    classification_value: Union[str, "MechanisticNosologyEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.classification_value):
            self.MissingRequiredField("classification_value")
        if not isinstance(self.classification_value, MechanisticNosologyEnum):
            self.classification_value = MechanisticNosologyEnum(self.classification_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IUISAssignment(ClassificationAssignment):
    """
    IUIS primary immunodeficiency classification assignment
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["IUISAssignment"]
    class_class_curie: ClassVar[str] = "dismech:IUISAssignment"
    class_name: ClassVar[str] = "IUISAssignment"
    class_model_uri: ClassVar[URIRef] = DISMECH.IUISAssignment

    classification_value: Union[str, "IUISCategoryEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.classification_value):
            self.MissingRequiredField("classification_value")
        if not isinstance(self.classification_value, IUISCategoryEnum):
            self.classification_value = IUISCategoryEnum(self.classification_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChannelopathyAssignment(ClassificationAssignment):
    """
    Channelopathy organ system classification assignment
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ChannelopathyAssignment"]
    class_class_curie: ClassVar[str] = "dismech:ChannelopathyAssignment"
    class_name: ClassVar[str] = "ChannelopathyAssignment"
    class_model_uri: ClassVar[URIRef] = DISMECH.ChannelopathyAssignment

    classification_value: Union[str, "ChannelopathyOrganSystemEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.classification_value):
            self.MissingRequiredField("classification_value")
        if not isinstance(self.classification_value, ChannelopathyOrganSystemEnum):
            self.classification_value = ChannelopathyOrganSystemEnum(self.classification_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ICIMDAssignment(ClassificationAssignment):
    """
    ICIMD category/group classification assignment for inherited metabolic disorders. Assign the most specific
    applicable node (usually a group); the parent category is derivable via the enum's ``is_a`` hierarchy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ICIMDAssignment"]
    class_class_curie: ClassVar[str] = "dismech:ICIMDAssignment"
    class_name: ClassVar[str] = "ICIMDAssignment"
    class_model_uri: ClassVar[URIRef] = DISMECH.ICIMDAssignment

    classification_value: Union[str, "ICIMDEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.classification_value):
            self.MissingRequiredField("classification_value")
        if not isinstance(self.classification_value, ICIMDEnum):
            self.classification_value = ICIMDEnum(self.classification_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ISDSNosologyAssignment(ClassificationAssignment):
    """
    ISDS Nosology group assignment for a genetic skeletal disorder, per the Nosology of Genetic Skeletal Disorders
    (2023 revision, 11th edition; Unger et al., PMID:36779427), which supersedes the 2019 revision (PMID:31633310).
    Record the provenance — which revision, the group number/name, and the listed disorder name where it differs from
    the dismech entry name — in ``notes``. Assignments may legitimately cite either revision while the 2019-derived
    backfill is being re-verified against the 2023 table; the ``notes`` must say which one.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ISDSNosologyAssignment"]
    class_class_curie: ClassVar[str] = "dismech:ISDSNosologyAssignment"
    class_name: ClassVar[str] = "ISDSNosologyAssignment"
    class_model_uri: ClassVar[URIRef] = DISMECH.ISDSNosologyAssignment

    classification_value: Union[str, "ISDSNosologyGroupEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.classification_value):
            self.MissingRequiredField("classification_value")
        if not isinstance(self.classification_value, ISDSNosologyGroupEnum):
            self.classification_value = ISDSNosologyGroupEnum(self.classification_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NIHResearchPriorityAssignment(ClassificationAssignment):
    """
    NIH Highlighted Topics funding-priority assignment. A secondary, grant-strategy tag (not a disease nosology)
    recording which NIH highlighted funding topic the disease is relevant to. Use ``notes`` to explain the relevance
    and ``evidence`` where a specific claim backs it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["NIHResearchPriorityAssignment"]
    class_class_curie: ClassVar[str] = "dismech:NIHResearchPriorityAssignment"
    class_name: ClassVar[str] = "NIHResearchPriorityAssignment"
    class_model_uri: ClassVar[URIRef] = DISMECH.NIHResearchPriorityAssignment

    classification_value: Union[str, "NIHResearchPriorityEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.classification_value):
            self.MissingRequiredField("classification_value")
        if not isinstance(self.classification_value, NIHResearchPriorityEnum):
            self.classification_value = NIHResearchPriorityEnum(self.classification_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ILOCausativeAgentAssignment(ClassificationAssignment):
    """
    Assignment of a disease to a **causative-agent-axis** item of the ILO List of Occupational Diseases (revised
    2010), annexed to the List of Occupational Diseases Recommendation, 2002 (No. 194) — sections 1 and 3. Record the
    revision and item number in ``notes``, together with whether the disease occurs only occupationally or also has
    non-occupational forms — the assignment records that an occupational form is recognised, not that every case is
    occupational.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ILOCausativeAgentAssignment"]
    class_class_curie: ClassVar[str] = "dismech:ILOCausativeAgentAssignment"
    class_name: ClassVar[str] = "ILOCausativeAgentAssignment"
    class_model_uri: ClassVar[URIRef] = DISMECH.ILOCausativeAgentAssignment

    classification_value: Union[str, "ILOCausativeAgentEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.classification_value):
            self.MissingRequiredField("classification_value")
        if not isinstance(self.classification_value, ILOCausativeAgentEnum):
            self.classification_value = ILOCausativeAgentEnum(self.classification_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ILODiseaseCategoryAssignment(ClassificationAssignment):
    """
    Assignment of a disease to a **disease-category-axis** item of the ILO List of Occupational Diseases (revised
    2010) — section 2 (by target organ system) and section 4 (other diseases). Same ``notes`` discipline as
    ``ILOCausativeAgentAssignment``.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ILODiseaseCategoryAssignment"]
    class_class_curie: ClassVar[str] = "dismech:ILODiseaseCategoryAssignment"
    class_name: ClassVar[str] = "ILODiseaseCategoryAssignment"
    class_model_uri: ClassVar[URIRef] = DISMECH.ILODiseaseCategoryAssignment

    classification_value: Union[str, "ILODiseaseCategoryEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.classification_value):
            self.MissingRequiredField("classification_value")
        if not isinstance(self.classification_value, ILODiseaseCategoryEnum):
            self.classification_value = ILODiseaseCategoryEnum(self.classification_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EUOccupationalScheduleAssignment(ClassificationAssignment):
    """
    Assignment of a disease to an item of the European schedule of occupational diseases (Commission Recommendation
    2003/670/EC, as amended by Recommendation (EU) 2022/2337 and Recommendation (EU) 2025/2609). Record the item
    number and annex in ``notes``. An Annex II (``suspected_*``) value asserts a SUSPECTED occupational origin only,
    and must not be reported as a recognised occupational disease.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["EUOccupationalScheduleAssignment"]
    class_class_curie: ClassVar[str] = "dismech:EUOccupationalScheduleAssignment"
    class_name: ClassVar[str] = "EUOccupationalScheduleAssignment"
    class_model_uri: ClassVar[URIRef] = DISMECH.EUOccupationalScheduleAssignment

    classification_value: Union[str, "EUOccupationalScheduleEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.classification_value):
            self.MissingRequiredField("classification_value")
        if not isinstance(self.classification_value, EUOccupationalScheduleEnum):
            self.classification_value = EUOccupationalScheduleEnum(self.classification_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HazardAgentTypeAssignment(ClassificationAssignment):
    """
    Occupational-hygiene hazard-agent-type assignment for an exposure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["HazardAgentTypeAssignment"]
    class_class_curie: ClassVar[str] = "dismech:HazardAgentTypeAssignment"
    class_name: ClassVar[str] = "HazardAgentTypeAssignment"
    class_model_uri: ClassVar[URIRef] = DISMECH.HazardAgentTypeAssignment

    classification_value: Union[str, "HazardAgentTypeEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.classification_value):
            self.MissingRequiredField("classification_value")
        if not isinstance(self.classification_value, HazardAgentTypeEnum):
            self.classification_value = HazardAgentTypeEnum(self.classification_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureRouteAssignment(ClassificationAssignment):
    """
    Route-of-exposure assignment for an exposure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ExposureRouteAssignment"]
    class_class_curie: ClassVar[str] = "dismech:ExposureRouteAssignment"
    class_name: ClassVar[str] = "ExposureRouteAssignment"
    class_model_uri: ClassVar[URIRef] = DISMECH.ExposureRouteAssignment

    classification_value: Union[str, "ExposureRouteEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.classification_value):
            self.MissingRequiredField("classification_value")
        if not isinstance(self.classification_value, ExposureRouteEnum):
            self.classification_value = ExposureRouteEnum(self.classification_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureDurationAssignment(ClassificationAssignment):
    """
    Exposure-duration assignment, using the ATSDR Minimal Risk Level day ranges (acute 1-14 d, intermediate 15-364 d,
    chronic 365 d and longer). Where the cited source uses a different convention, note it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ExposureDurationAssignment"]
    class_class_curie: ClassVar[str] = "dismech:ExposureDurationAssignment"
    class_name: ClassVar[str] = "ExposureDurationAssignment"
    class_model_uri: ClassVar[URIRef] = DISMECH.ExposureDurationAssignment

    classification_value: Union[str, "ExposureDurationEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.classification_value):
            self.MissingRequiredField("classification_value")
        if not isinstance(self.classification_value, ExposureDurationEnum):
            self.classification_value = ExposureDurationEnum(self.classification_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IARCCarcinogenGroupAssignment(ClassificationAssignment):
    """
    IARC Monographs carcinogenicity group assignment for an agent, per the Preamble as amended January 2019. This is
    hazard identification, not risk assessment: the group states the strength of evidence that the agent can cause
    cancer, not its potency or the size of any attributable burden. Record the Monograph volume and the tumour sites
    with sufficient evidence in ``notes``.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["IARCCarcinogenGroupAssignment"]
    class_class_curie: ClassVar[str] = "dismech:IARCCarcinogenGroupAssignment"
    class_name: ClassVar[str] = "IARCCarcinogenGroupAssignment"
    class_model_uri: ClassVar[URIRef] = DISMECH.IARCCarcinogenGroupAssignment

    classification_value: Union[str, "IARCCarcinogenGroupEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.classification_value):
            self.MissingRequiredField("classification_value")
        if not isinstance(self.classification_value, IARCCarcinogenGroupEnum):
            self.classification_value = IARCCarcinogenGroupEnum(self.classification_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GHSHealthHazardClassAssignment(ClassificationAssignment):
    """
    UN GHS health hazard class assignment for an agent. The numbered category within the class (e.g. "Carc. 1A",
    "Acute Tox. 3") is class-specific and is recorded in ``notes`` rather than as a permissible value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["GHSHealthHazardClassAssignment"]
    class_class_curie: ClassVar[str] = "dismech:GHSHealthHazardClassAssignment"
    class_name: ClassVar[str] = "GHSHealthHazardClassAssignment"
    class_model_uri: ClassVar[URIRef] = DISMECH.GHSHealthHazardClassAssignment

    classification_value: Union[str, "GHSHealthHazardClassEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.classification_value):
            self.MissingRequiredField("classification_value")
        if not isinstance(self.classification_value, GHSHealthHazardClassEnum):
            self.classification_value = GHSHealthHazardClassEnum(self.classification_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposomeDomainAssignment(ClassificationAssignment):
    """
    Exposome-domain assignment (Wild 2012, PMID:22296988). The domains overlap by design, so a placement is a framing
    choice rather than a sharp claim.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ExposomeDomainAssignment"]
    class_class_curie: ClassVar[str] = "dismech:ExposomeDomainAssignment"
    class_name: ClassVar[str] = "ExposomeDomainAssignment"
    class_model_uri: ClassVar[URIRef] = DISMECH.ExposomeDomainAssignment

    classification_value: Union[str, "ExposomeDomainEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.classification_value):
            self.MissingRequiredField("classification_value")
        if not isinstance(self.classification_value, ExposomeDomainEnum):
            self.classification_value = ExposomeDomainEnum(self.classification_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureClassifications(YAMLRoot):
    """
    Container for exposure- and agent-level classification assignments on an ``Environmental`` entry. Deliberately
    separate from ``DiseaseClassifications``: everything here classifies the agent or the exposure event (benzene is
    an IARC Group 1 carcinogen), not the disease.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ExposureClassifications"]
    class_class_curie: ClassVar[str] = "dismech:ExposureClassifications"
    class_name: ClassVar[str] = "ExposureClassifications"
    class_model_uri: ClassVar[URIRef] = DISMECH.ExposureClassifications

    hazard_agent_type: Optional[Union[Union[dict, HazardAgentTypeAssignment], list[Union[dict, HazardAgentTypeAssignment]]]] = empty_list()
    exposure_route: Optional[Union[Union[dict, ExposureRouteAssignment], list[Union[dict, ExposureRouteAssignment]]]] = empty_list()
    exposure_duration: Optional[Union[Union[dict, ExposureDurationAssignment], list[Union[dict, ExposureDurationAssignment]]]] = empty_list()
    iarc_carcinogen_group: Optional[Union[dict, IARCCarcinogenGroupAssignment]] = None
    ghs_health_hazard_class: Optional[Union[Union[dict, GHSHealthHazardClassAssignment], list[Union[dict, GHSHealthHazardClassAssignment]]]] = empty_list()
    exposome_domain: Optional[Union[Union[dict, ExposomeDomainAssignment], list[Union[dict, ExposomeDomainAssignment]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="hazard_agent_type", slot_type=HazardAgentTypeAssignment, key_name="classification_value", keyed=False)

        self._normalize_inlined_as_list(slot_name="exposure_route", slot_type=ExposureRouteAssignment, key_name="classification_value", keyed=False)

        self._normalize_inlined_as_list(slot_name="exposure_duration", slot_type=ExposureDurationAssignment, key_name="classification_value", keyed=False)

        if self.iarc_carcinogen_group is not None and not isinstance(self.iarc_carcinogen_group, IARCCarcinogenGroupAssignment):
            self.iarc_carcinogen_group = IARCCarcinogenGroupAssignment(**as_dict(self.iarc_carcinogen_group))

        self._normalize_inlined_as_list(slot_name="ghs_health_hazard_class", slot_type=GHSHealthHazardClassAssignment, key_name="classification_value", keyed=False)

        self._normalize_inlined_as_list(slot_name="exposome_domain", slot_type=ExposomeDomainAssignment, key_name="classification_value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiseaseClassifications(YAMLRoot):
    """
    Container for all classification assignments for a disease
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["DiseaseClassifications"]
    class_class_curie: ClassVar[str] = "dismech:DiseaseClassifications"
    class_name: ClassVar[str] = "DiseaseClassifications"
    class_model_uri: ClassVar[URIRef] = DISMECH.DiseaseClassifications

    icdo_morphology: Optional[Union[dict, ICDOMorphologyAssignment]] = None
    harrisons_chapter: Optional[Union[Union[dict, HarrisonsChapterAssignment], list[Union[dict, HarrisonsChapterAssignment]]]] = empty_list()
    lysosomal_storage_category: Optional[Union[dict, LysosomalStorageAssignment]] = None
    mechanistic_category: Optional[Union[Union[dict, MechanisticNosologyAssignment], list[Union[dict, MechanisticNosologyAssignment]]]] = empty_list()
    iuis_category: Optional[Union[dict, IUISAssignment]] = None
    channelopathy_category: Optional[Union[dict, ChannelopathyAssignment]] = None
    icimd_category: Optional[Union[Union[dict, ICIMDAssignment], list[Union[dict, ICIMDAssignment]]]] = empty_list()
    isds_skeletal_category: Optional[Union[Union[dict, ISDSNosologyAssignment], list[Union[dict, ISDSNosologyAssignment]]]] = empty_list()
    nih_research_priority: Optional[Union[Union[dict, NIHResearchPriorityAssignment], list[Union[dict, NIHResearchPriorityAssignment]]]] = empty_list()
    ilo_agent_category: Optional[Union[Union[dict, ILOCausativeAgentAssignment], list[Union[dict, ILOCausativeAgentAssignment]]]] = empty_list()
    ilo_disease_category: Optional[Union[Union[dict, ILODiseaseCategoryAssignment], list[Union[dict, ILODiseaseCategoryAssignment]]]] = empty_list()
    eu_occupational_category: Optional[Union[Union[dict, EUOccupationalScheduleAssignment], list[Union[dict, EUOccupationalScheduleAssignment]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.icdo_morphology is not None and not isinstance(self.icdo_morphology, ICDOMorphologyAssignment):
            self.icdo_morphology = ICDOMorphologyAssignment(**as_dict(self.icdo_morphology))

        self._normalize_inlined_as_list(slot_name="harrisons_chapter", slot_type=HarrisonsChapterAssignment, key_name="classification_value", keyed=False)

        if self.lysosomal_storage_category is not None and not isinstance(self.lysosomal_storage_category, LysosomalStorageAssignment):
            self.lysosomal_storage_category = LysosomalStorageAssignment(**as_dict(self.lysosomal_storage_category))

        self._normalize_inlined_as_list(slot_name="mechanistic_category", slot_type=MechanisticNosologyAssignment, key_name="classification_value", keyed=False)

        if self.iuis_category is not None and not isinstance(self.iuis_category, IUISAssignment):
            self.iuis_category = IUISAssignment(**as_dict(self.iuis_category))

        if self.channelopathy_category is not None and not isinstance(self.channelopathy_category, ChannelopathyAssignment):
            self.channelopathy_category = ChannelopathyAssignment(**as_dict(self.channelopathy_category))

        self._normalize_inlined_as_list(slot_name="icimd_category", slot_type=ICIMDAssignment, key_name="classification_value", keyed=False)

        self._normalize_inlined_as_list(slot_name="isds_skeletal_category", slot_type=ISDSNosologyAssignment, key_name="classification_value", keyed=False)

        self._normalize_inlined_as_list(slot_name="nih_research_priority", slot_type=NIHResearchPriorityAssignment, key_name="classification_value", keyed=False)

        self._normalize_inlined_as_list(slot_name="ilo_agent_category", slot_type=ILOCausativeAgentAssignment, key_name="classification_value", keyed=False)

        self._normalize_inlined_as_list(slot_name="ilo_disease_category", slot_type=ILODiseaseCategoryAssignment, key_name="classification_value", keyed=False)

        self._normalize_inlined_as_list(slot_name="eu_occupational_category", slot_type=EUOccupationalScheduleAssignment, key_name="classification_value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Definition(YAMLRoot):
    """
    A diagnostic or phenotype definition for the disease
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Definition"]
    class_class_curie: ClassVar[str] = "dismech:Definition"
    class_name: ClassVar[str] = "Definition"
    class_model_uri: ClassVar[URIRef] = DISMECH.Definition

    name: Union[str, DefinitionName] = None
    definition_type: Union[str, "DefinitionTypeEnum"] = None
    derivation_basis: Optional[Union[str, "DefinitionDerivationBasisEnum"]] = None
    validation_status: Optional[Union[dict, "AlgorithmValidationStatus"]] = None
    description: Optional[str] = None
    scope: Optional[str] = None
    attaches_to: Optional[Union[str, list[str]]] = empty_list()
    criteria_sets: Optional[Union[dict[Union[str, CriteriaSetName], Union[dict, "CriteriaSet"]], list[Union[dict, "CriteriaSet"]]]] = empty_dict()
    inclusion_criteria: Optional[Union[Union[dict, "CriteriaItem"], list[Union[dict, "CriteriaItem"]]]] = empty_list()
    exclusion_criteria: Optional[Union[Union[dict, "CriteriaItem"], list[Union[dict, "CriteriaItem"]]]] = empty_list()
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, DefinitionName):
            self.name = DefinitionName(self.name)

        if self._is_empty(self.definition_type):
            self.MissingRequiredField("definition_type")
        if not isinstance(self.definition_type, DefinitionTypeEnum):
            self.definition_type = DefinitionTypeEnum(self.definition_type)

        if self.derivation_basis is not None and not isinstance(self.derivation_basis, DefinitionDerivationBasisEnum):
            self.derivation_basis = DefinitionDerivationBasisEnum(self.derivation_basis)

        if self.validation_status is not None and not isinstance(self.validation_status, AlgorithmValidationStatus):
            self.validation_status = AlgorithmValidationStatus(**as_dict(self.validation_status))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.scope is not None and not isinstance(self.scope, str):
            self.scope = str(self.scope)

        if not isinstance(self.attaches_to, list):
            self.attaches_to = [self.attaches_to] if self.attaches_to is not None else []
        self.attaches_to = [v if isinstance(v, str) else str(v) for v in self.attaches_to]

        self._normalize_inlined_as_list(slot_name="criteria_sets", slot_type=CriteriaSet, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="inclusion_criteria", slot_type=CriteriaItem, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="exclusion_criteria", slot_type=CriteriaItem, key_name="preferred_term", keyed=False)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AlgorithmValidationStatus(YAMLRoot):
    """
    Validation maturity of a phenotype algorithm / computable case definition: a graded status plus a free-text
    rationale and optional citing evidence (the standard EvidenceItem model — reference + verbatim snippet +
    explanation).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["AlgorithmValidationStatus"]
    class_class_curie: ClassVar[str] = "dismech:AlgorithmValidationStatus"
    class_name: ClassVar[str] = "AlgorithmValidationStatus"
    class_model_uri: ClassVar[URIRef] = DISMECH.AlgorithmValidationStatus

    status: Union[str, "AlgorithmValidationStatusEnum"] = None
    rationale: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.status):
            self.MissingRequiredField("status")
        if not isinstance(self.status, AlgorithmValidationStatusEnum):
            self.status = AlgorithmValidationStatusEnum(self.status)

        if self.rationale is not None and not isinstance(self.rationale, str):
            self.rationale = str(self.rationale)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CriteriaSet(YAMLRoot):
    """
    A named criteria grouping within a definition
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["CriteriaSet"]
    class_class_curie: ClassVar[str] = "dismech:CriteriaSet"
    class_name: ClassVar[str] = "CriteriaSet"
    class_model_uri: ClassVar[URIRef] = DISMECH.CriteriaSet

    name: Union[str, CriteriaSetName] = None
    description: Optional[str] = None
    scope: Optional[str] = None
    minimum_required: Optional[int] = None
    core_clinical_characteristics: Optional[Union[Union[dict, "CriteriaItem"], list[Union[dict, "CriteriaItem"]]]] = empty_list()
    inclusion_criteria: Optional[Union[Union[dict, "CriteriaItem"], list[Union[dict, "CriteriaItem"]]]] = empty_list()
    exclusion_criteria: Optional[Union[Union[dict, "CriteriaItem"], list[Union[dict, "CriteriaItem"]]]] = empty_list()
    imaging_requirements: Optional[Union[Union[dict, "CriteriaItem"], list[Union[dict, "CriteriaItem"]]]] = empty_list()
    laboratory_requirements: Optional[Union[Union[dict, "CriteriaItem"], list[Union[dict, "CriteriaItem"]]]] = empty_list()
    additional_requirements: Optional[Union[Union[dict, "CriteriaItem"], list[Union[dict, "CriteriaItem"]]]] = empty_list()
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, CriteriaSetName):
            self.name = CriteriaSetName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.scope is not None and not isinstance(self.scope, str):
            self.scope = str(self.scope)

        if self.minimum_required is not None and not isinstance(self.minimum_required, int):
            self.minimum_required = int(self.minimum_required)

        self._normalize_inlined_as_list(slot_name="core_clinical_characteristics", slot_type=CriteriaItem, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="inclusion_criteria", slot_type=CriteriaItem, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="exclusion_criteria", slot_type=CriteriaItem, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="imaging_requirements", slot_type=CriteriaItem, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="laboratory_requirements", slot_type=CriteriaItem, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="additional_requirements", slot_type=CriteriaItem, key_name="preferred_term", keyed=False)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CriteriaItem(Descriptor):
    """
    A criterion element (clinical feature, test result, imaging requirement)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["CriteriaItem"]
    class_class_curie: ClassVar[str] = "dismech:CriteriaItem"
    class_name: ClassVar[str] = "CriteriaItem"
    class_model_uri: ClassVar[URIRef] = DISMECH.CriteriaItem

    preferred_term: str = None

@dataclass(repr=False)
class TermMapping(YAMLRoot):
    """
    Mapping from this disease entry to an external term or code
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["TermMapping"]
    class_class_curie: ClassVar[str] = "dismech:TermMapping"
    class_name: ClassVar[str] = "TermMapping"
    class_model_uri: ClassVar[URIRef] = DISMECH.TermMapping

    term: Union[dict, Term] = None
    mapping_predicate: Union[str, URIorCURIE] = None
    mapping_source: Optional[str] = None
    mapping_justification: Optional[str] = None
    consistency: Optional[Union[Union[dict, "MappingConsistency"], list[Union[dict, "MappingConsistency"]]]] = empty_list()
    tracked_issues: Optional[Union[Union[dict, TrackedIssue], list[Union[dict, TrackedIssue]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.term):
            self.MissingRequiredField("term")
        if not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        if self._is_empty(self.mapping_predicate):
            self.MissingRequiredField("mapping_predicate")
        if not isinstance(self.mapping_predicate, URIorCURIE):
            self.mapping_predicate = URIorCURIE(self.mapping_predicate)

        if self.mapping_source is not None and not isinstance(self.mapping_source, str):
            self.mapping_source = str(self.mapping_source)

        if self.mapping_justification is not None and not isinstance(self.mapping_justification, str):
            self.mapping_justification = str(self.mapping_justification)

        self._normalize_inlined_as_list(slot_name="consistency", slot_type=MappingConsistency, key_name="reference", keyed=False)

        self._normalize_inlined_as_list(slot_name="tracked_issues", slot_type=TrackedIssue, key_name="url", keyed=False)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ICD10CMMapping(TermMapping):
    """
    ICD-10-CM diagnosis code mapping
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ICD10CMMapping"]
    class_class_curie: ClassVar[str] = "dismech:ICD10CMMapping"
    class_name: ClassVar[str] = "ICD10CMMapping"
    class_model_uri: ClassVar[URIRef] = DISMECH.ICD10CMMapping

    mapping_predicate: Union[str, URIorCURIE] = None
    term: Union[dict, Term] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.term):
            self.MissingRequiredField("term")
        if not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ICD11FMapping(TermMapping):
    """
    ICD-11 Foundation diagnosis code mapping
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ICD11FMapping"]
    class_class_curie: ClassVar[str] = "dismech:ICD11FMapping"
    class_name: ClassVar[str] = "ICD11FMapping"
    class_model_uri: ClassVar[URIRef] = DISMECH.ICD11FMapping

    mapping_predicate: Union[str, URIorCURIE] = None
    term: Union[dict, Term] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.term):
            self.MissingRequiredField("term")
        if not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MondoMapping(TermMapping):
    """
    MONDO disease ontology mapping
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["MondoMapping"]
    class_class_curie: ClassVar[str] = "dismech:MondoMapping"
    class_name: ClassVar[str] = "MondoMapping"
    class_model_uri: ClassVar[URIRef] = DISMECH.MondoMapping

    mapping_predicate: Union[str, URIorCURIE] = None
    term: Union[dict, Term] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.term):
            self.MissingRequiredField("term")
        if not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NCITMapping(TermMapping):
    """
    NCIT disease, subtype, or disease/finding ontology mapping for cancer entries
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["NCITMapping"]
    class_class_curie: ClassVar[str] = "dismech:NCITMapping"
    class_name: ClassVar[str] = "NCITMapping"
    class_model_uri: ClassVar[URIRef] = DISMECH.NCITMapping

    mapping_predicate: Union[str, URIorCURIE] = None
    term: Union[dict, Term] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.term):
            self.MissingRequiredField("term")
        if not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MappingConsistency(YAMLRoot):
    """
    Consistency assertion for a mapping relative to another source
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["MappingConsistency"]
    class_class_curie: ClassVar[str] = "dismech:MappingConsistency"
    class_name: ClassVar[str] = "MappingConsistency"
    class_model_uri: ClassVar[URIRef] = DISMECH.MappingConsistency

    reference: str = None
    consistent: Union[str, "MappingConsistencyEnum"] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.reference):
            self.MissingRequiredField("reference")
        if not isinstance(self.reference, str):
            self.reference = str(self.reference)

        if self._is_empty(self.consistent):
            self.MissingRequiredField("consistent")
        if not isinstance(self.consistent, MappingConsistencyEnum):
            self.consistent = MappingConsistencyEnum(self.consistent)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiseaseMappings(YAMLRoot):
    """
    Container for external identifier mappings for a disease or subtype
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["DiseaseMappings"]
    class_class_curie: ClassVar[str] = "dismech:DiseaseMappings"
    class_name: ClassVar[str] = "DiseaseMappings"
    class_model_uri: ClassVar[URIRef] = DISMECH.DiseaseMappings

    icd10cm_mappings: Optional[Union[Union[dict, ICD10CMMapping], list[Union[dict, ICD10CMMapping]]]] = empty_list()
    icd11f_mappings: Optional[Union[Union[dict, ICD11FMapping], list[Union[dict, ICD11FMapping]]]] = empty_list()
    mondo_mappings: Optional[Union[Union[dict, MondoMapping], list[Union[dict, MondoMapping]]]] = empty_list()
    ncit_mappings: Optional[Union[Union[dict, NCITMapping], list[Union[dict, NCITMapping]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="icd10cm_mappings", slot_type=ICD10CMMapping, key_name="mapping_predicate", keyed=False)

        self._normalize_inlined_as_list(slot_name="icd11f_mappings", slot_type=ICD11FMapping, key_name="mapping_predicate", keyed=False)

        self._normalize_inlined_as_list(slot_name="mondo_mappings", slot_type=MondoMapping, key_name="mapping_predicate", keyed=False)

        self._normalize_inlined_as_list(slot_name="ncit_mappings", slot_type=NCITMapping, key_name="mapping_predicate", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConditionDescriptor(Descriptor):
    """
    A descriptor for a condition or disease, optionally bound to MONDO. External coding identifiers (ICD-10, OMOP,
    SNOMED, etc.) are captured on association signals.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ConditionDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:ConditionDescriptor"
    class_name: ClassVar[str] = "ConditionDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.ConditionDescriptor

    preferred_term: str = None
    slug: Optional[str] = None
    description: Optional[str] = None
    term: Optional[Union[dict, Term]] = None
    composition: Optional[Union[str, "ConditionCompositionEnum"]] = None
    components: Optional[Union[Union[dict, "ConditionDescriptor"], list[Union[dict, "ConditionDescriptor"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.preferred_term):
            self.MissingRequiredField("preferred_term")
        if not isinstance(self.preferred_term, str):
            self.preferred_term = str(self.preferred_term)

        if self.slug is not None and not isinstance(self.slug, str):
            self.slug = str(self.slug)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        if self.composition is not None and not isinstance(self.composition, ConditionCompositionEnum):
            self.composition = ConditionCompositionEnum(self.composition)

        self._normalize_inlined_as_list(slot_name="components", slot_type=ConditionDescriptor, key_name="preferred_term", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComorbidityAssociation(YAMLRoot):
    """
    An association between two conditions, including directionality, evidence, and computational characterizations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ComorbidityAssociation"]
    class_class_curie: ClassVar[str] = "dismech:ComorbidityAssociation"
    class_name: ClassVar[str] = "ComorbidityAssociation"
    class_model_uri: ClassVar[URIRef] = DISMECH.ComorbidityAssociation

    name: Union[str, ComorbidityAssociationName] = None
    creation_date: Optional[str] = None
    updated_date: Optional[str] = None
    disease_a: Optional[Union[dict, ConditionDescriptor]] = None
    disease_b: Optional[Union[dict, ConditionDescriptor]] = None
    directionality: Optional[Union[str, "ComorbidityDirectionEnum"]] = None
    effect_direction: Optional[Union[str, "ComorbidityEffectDirectionEnum"]] = None
    association_signals: Optional[Union[Union[dict, "AssociationSignal"], list[Union[dict, "AssociationSignal"]]]] = empty_list()
    literature_evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    hypotheses: Optional[Union[Union[dict, "ComorbidityHypothesis"], list[Union[dict, "ComorbidityHypothesis"]]]] = empty_list()
    shared_upstream_hypotheses: Optional[Union[Union[dict, "UpstreamConditionHypothesis"], list[Union[dict, "UpstreamConditionHypothesis"]]]] = empty_list()
    phenotypes: Optional[Union[dict[Union[str, PhenotypeName], Union[dict, Phenotype]], list[Union[dict, Phenotype]]]] = empty_dict()
    notes: Optional[str] = None
    curation_status: Optional[Union[str, "CurationStatusEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ComorbidityAssociationName):
            self.name = ComorbidityAssociationName(self.name)

        if self.creation_date is not None and not isinstance(self.creation_date, str):
            self.creation_date = str(self.creation_date)

        if self.updated_date is not None and not isinstance(self.updated_date, str):
            self.updated_date = str(self.updated_date)

        if self.disease_a is not None and not isinstance(self.disease_a, ConditionDescriptor):
            self.disease_a = ConditionDescriptor(**as_dict(self.disease_a))

        if self.disease_b is not None and not isinstance(self.disease_b, ConditionDescriptor):
            self.disease_b = ConditionDescriptor(**as_dict(self.disease_b))

        if self.directionality is not None and not isinstance(self.directionality, ComorbidityDirectionEnum):
            self.directionality = ComorbidityDirectionEnum(self.directionality)

        if self.effect_direction is not None and not isinstance(self.effect_direction, ComorbidityEffectDirectionEnum):
            self.effect_direction = ComorbidityEffectDirectionEnum(self.effect_direction)

        if not isinstance(self.association_signals, list):
            self.association_signals = [self.association_signals] if self.association_signals is not None else []
        self.association_signals = [v if isinstance(v, AssociationSignal) else AssociationSignal(**as_dict(v)) for v in self.association_signals]

        if not isinstance(self.literature_evidence, list):
            self.literature_evidence = [self.literature_evidence] if self.literature_evidence is not None else []
        self.literature_evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.literature_evidence]

        if not isinstance(self.hypotheses, list):
            self.hypotheses = [self.hypotheses] if self.hypotheses is not None else []
        self.hypotheses = [v if isinstance(v, ComorbidityHypothesis) else ComorbidityHypothesis(**as_dict(v)) for v in self.hypotheses]

        if not isinstance(self.shared_upstream_hypotheses, list):
            self.shared_upstream_hypotheses = [self.shared_upstream_hypotheses] if self.shared_upstream_hypotheses is not None else []
        self.shared_upstream_hypotheses = [v if isinstance(v, UpstreamConditionHypothesis) else UpstreamConditionHypothesis(**as_dict(v)) for v in self.shared_upstream_hypotheses]

        self._normalize_inlined_as_list(slot_name="phenotypes", slot_type=Phenotype, key_name="name", keyed=True)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.curation_status is not None and not isinstance(self.curation_status, CurationStatusEnum):
            self.curation_status = CurationStatusEnum(self.curation_status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssociationSignal(YAMLRoot):
    """
    An association signal from EHR, registry, or computational sources, optionally stratified by sex, age, or cohort.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["AssociationSignal"]
    class_class_curie: ClassVar[str] = "dismech:AssociationSignal"
    class_name: ClassVar[str] = "AssociationSignal"
    class_model_uri: ClassVar[URIRef] = DISMECH.AssociationSignal

    source: Optional[Union[str, "AssociationSignalSourceEnum"]] = None
    method: Optional[Union[str, "AssociationSignalMethodEnum"]] = None
    signal_disorder_a_id: Optional[Union[str, URIorCURIE]] = None
    signal_disorder_b_id: Optional[Union[str, URIorCURIE]] = None
    population: Optional[str] = None
    demographics: Optional[Union[dict, "Demographics"]] = None
    mapping_notes: Optional[str] = None
    disorder_a_count: Optional[int] = None
    disorder_b_count: Optional[int] = None
    pair_count: Optional[int] = None
    limited_precision: Optional[Union[bool, Bool]] = None
    precision_count_threshold: Optional[int] = None
    directionality: Optional[Union[str, "ComorbidityDirectionEnum"]] = None
    effect_direction: Optional[Union[str, "ComorbidityEffectDirectionEnum"]] = None
    a_before_b: Optional[float] = None
    b_before_a: Optional[float] = None
    same_time: Optional[float] = None
    metrics: Optional[Union[Union[dict, "AssociationMetric"], list[Union[dict, "AssociationMetric"]]]] = empty_list()
    statistics: Optional[Union[dict, "AssociationStatistics"]] = None
    go_enrichment: Optional[Union[dict, "GOEnrichment"]] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.source is not None and not isinstance(self.source, AssociationSignalSourceEnum):
            self.source = AssociationSignalSourceEnum(self.source)

        if self.method is not None and not isinstance(self.method, AssociationSignalMethodEnum):
            self.method = AssociationSignalMethodEnum(self.method)

        if self.signal_disorder_a_id is not None and not isinstance(self.signal_disorder_a_id, URIorCURIE):
            self.signal_disorder_a_id = URIorCURIE(self.signal_disorder_a_id)

        if self.signal_disorder_b_id is not None and not isinstance(self.signal_disorder_b_id, URIorCURIE):
            self.signal_disorder_b_id = URIorCURIE(self.signal_disorder_b_id)

        if self.population is not None and not isinstance(self.population, str):
            self.population = str(self.population)

        if self.demographics is not None and not isinstance(self.demographics, Demographics):
            self.demographics = Demographics(**as_dict(self.demographics))

        if self.mapping_notes is not None and not isinstance(self.mapping_notes, str):
            self.mapping_notes = str(self.mapping_notes)

        if self.disorder_a_count is not None and not isinstance(self.disorder_a_count, int):
            self.disorder_a_count = int(self.disorder_a_count)

        if self.disorder_b_count is not None and not isinstance(self.disorder_b_count, int):
            self.disorder_b_count = int(self.disorder_b_count)

        if self.pair_count is not None and not isinstance(self.pair_count, int):
            self.pair_count = int(self.pair_count)

        if self.limited_precision is not None and not isinstance(self.limited_precision, Bool):
            self.limited_precision = Bool(self.limited_precision)

        if self.precision_count_threshold is not None and not isinstance(self.precision_count_threshold, int):
            self.precision_count_threshold = int(self.precision_count_threshold)

        if self.directionality is not None and not isinstance(self.directionality, ComorbidityDirectionEnum):
            self.directionality = ComorbidityDirectionEnum(self.directionality)

        if self.effect_direction is not None and not isinstance(self.effect_direction, ComorbidityEffectDirectionEnum):
            self.effect_direction = ComorbidityEffectDirectionEnum(self.effect_direction)

        if self.a_before_b is not None and not isinstance(self.a_before_b, float):
            self.a_before_b = float(self.a_before_b)

        if self.b_before_a is not None and not isinstance(self.b_before_a, float):
            self.b_before_a = float(self.b_before_a)

        if self.same_time is not None and not isinstance(self.same_time, float):
            self.same_time = float(self.same_time)

        if not isinstance(self.metrics, list):
            self.metrics = [self.metrics] if self.metrics is not None else []
        self.metrics = [v if isinstance(v, AssociationMetric) else AssociationMetric(**as_dict(v)) for v in self.metrics]

        if self.statistics is not None and not isinstance(self.statistics, AssociationStatistics):
            self.statistics = AssociationStatistics(**as_dict(self.statistics))

        if self.go_enrichment is not None and not isinstance(self.go_enrichment, GOEnrichment):
            self.go_enrichment = GOEnrichment(**as_dict(self.go_enrichment))

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Demographics(YAMLRoot):
    """
    Demographic stratification for an association signal
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Demographics"]
    class_class_curie: ClassVar[str] = "dismech:Demographics"
    class_name: ClassVar[str] = "Demographics"
    class_model_uri: ClassVar[URIRef] = DISMECH.Demographics

    sex: Optional[Union[str, "SexEnum"]] = None
    age_range: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.sex is not None and not isinstance(self.sex, SexEnum):
            self.sex = SexEnum(self.sex)

        if self.age_range is not None and not isinstance(self.age_range, str):
            self.age_range = str(self.age_range)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssociationMetric(YAMLRoot):
    """
    Quantitative association metric and its uncertainty.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["AssociationMetric"]
    class_class_curie: ClassVar[str] = "dismech:AssociationMetric"
    class_name: ClassVar[str] = "AssociationMetric"
    class_model_uri: ClassVar[URIRef] = DISMECH.AssociationMetric

    metric_type: Optional[Union[str, "AssociationMetricTypeEnum"]] = None
    metric_value: Optional[float] = None
    metric_ci_lower: Optional[float] = None
    metric_ci_upper: Optional[float] = None
    p_value: Optional[float] = None
    fdr: Optional[float] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.metric_type is not None and not isinstance(self.metric_type, AssociationMetricTypeEnum):
            self.metric_type = AssociationMetricTypeEnum(self.metric_type)

        if self.metric_value is not None and not isinstance(self.metric_value, float):
            self.metric_value = float(self.metric_value)

        if self.metric_ci_lower is not None and not isinstance(self.metric_ci_lower, float):
            self.metric_ci_lower = float(self.metric_ci_lower)

        if self.metric_ci_upper is not None and not isinstance(self.metric_ci_upper, float):
            self.metric_ci_upper = float(self.metric_ci_upper)

        if self.p_value is not None and not isinstance(self.p_value, float):
            self.p_value = float(self.p_value)

        if self.fdr is not None and not isinstance(self.fdr, float):
            self.fdr = float(self.fdr)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssociationStatistics(YAMLRoot):
    """
    Statistical summary with evidence for an association signal.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["AssociationStatistics"]
    class_class_curie: ClassVar[str] = "dismech:AssociationStatistics"
    class_name: ClassVar[str] = "AssociationStatistics"
    class_model_uri: ClassVar[URIRef] = DISMECH.AssociationStatistics

    metrics: Optional[Union[Union[dict, AssociationMetric], list[Union[dict, AssociationMetric]]]] = empty_list()
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.metrics, list):
            self.metrics = [self.metrics] if self.metrics is not None else []
        self.metrics = [v if isinstance(v, AssociationMetric) else AssociationMetric(**as_dict(v)) for v in self.metrics]

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GOEnrichment(YAMLRoot):
    """
    GO enrichment results for an association signal.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["GOEnrichment"]
    class_class_curie: ClassVar[str] = "dismech:GOEnrichment"
    class_name: ClassVar[str] = "GOEnrichment"
    class_model_uri: ClassVar[URIRef] = DISMECH.GOEnrichment

    method: Optional[str] = None
    description: Optional[str] = None
    go_terms: Optional[Union[Union[dict, "GOEnrichmentTerm"], list[Union[dict, "GOEnrichmentTerm"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.method is not None and not isinstance(self.method, str):
            self.method = str(self.method)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.go_terms, list):
            self.go_terms = [self.go_terms] if self.go_terms is not None else []
        self.go_terms = [v if isinstance(v, GOEnrichmentTerm) else GOEnrichmentTerm(**as_dict(v)) for v in self.go_terms]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GOEnrichmentTerm(YAMLRoot):
    """
    GO term enrichment result with statistical metrics.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["GOEnrichmentTerm"]
    class_class_curie: ClassVar[str] = "dismech:GOEnrichmentTerm"
    class_name: ClassVar[str] = "GOEnrichmentTerm"
    class_model_uri: ClassVar[URIRef] = DISMECH.GOEnrichmentTerm

    term: Optional[Union[dict, Term]] = None
    p_value: Optional[float] = None
    fdr: Optional[float] = None
    overlap: Optional[float] = None
    combined_score: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        if self.p_value is not None and not isinstance(self.p_value, float):
            self.p_value = float(self.p_value)

        if self.fdr is not None and not isinstance(self.fdr, float):
            self.fdr = float(self.fdr)

        if self.overlap is not None and not isinstance(self.overlap, float):
            self.overlap = float(self.overlap)

        if self.combined_score is not None and not isinstance(self.combined_score, float):
            self.combined_score = float(self.combined_score)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComorbidityHypothesis(YAMLRoot):
    """
    Mechanistic hypothesis for a comorbidity association, with rich text and embedded evidence plus atomic
    pathophysiology elements.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ComorbidityHypothesis"]
    class_class_curie: ClassVar[str] = "dismech:ComorbidityHypothesis"
    class_name: ClassVar[str] = "ComorbidityHypothesis"
    class_model_uri: ClassVar[URIRef] = DISMECH.ComorbidityHypothesis

    description: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    pathophysiology: Optional[Union[dict[Union[str, PathophysiologyName], Union[dict, Pathophysiology]], list[Union[dict, Pathophysiology]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        self._normalize_inlined_as_list(slot_name="pathophysiology", slot_type=Pathophysiology, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UpstreamConditionHypothesis(YAMLRoot):
    """
    Hypothesized upstream condition that may explain both A and B.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["UpstreamConditionHypothesis"]
    class_class_curie: ClassVar[str] = "dismech:UpstreamConditionHypothesis"
    class_name: ClassVar[str] = "UpstreamConditionHypothesis"
    class_model_uri: ClassVar[URIRef] = DISMECH.UpstreamConditionHypothesis

    upstream_disorder: Optional[Union[dict, ConditionDescriptor]] = None
    description: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.upstream_disorder is not None and not isinstance(self.upstream_disorder, ConditionDescriptor):
            self.upstream_disorder = ConditionDescriptor(**as_dict(self.upstream_disorder))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MechanisticHypothesis(YAMLRoot):
    """
    Disease-level hypothesis metadata used to organize downstream causal edges into canonical or alternative
    explanatory models.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["MechanisticHypothesis"]
    class_class_curie: ClassVar[str] = "dismech:MechanisticHypothesis"
    class_name: ClassVar[str] = "MechanisticHypothesis"
    class_model_uri: ClassVar[URIRef] = DISMECH.MechanisticHypothesis

    hypothesis_group_id: str = None
    hypothesis_label: Optional[str] = None
    status: Optional[Union[str, "MechanisticHypothesisStatusEnum"]] = None
    description: Optional[str] = None
    applies_to_subtypes: Optional[Union[str, list[str]]] = empty_list()
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.hypothesis_group_id):
            self.MissingRequiredField("hypothesis_group_id")
        if not isinstance(self.hypothesis_group_id, str):
            self.hypothesis_group_id = str(self.hypothesis_group_id)

        if self.hypothesis_label is not None and not isinstance(self.hypothesis_label, str):
            self.hypothesis_label = str(self.hypothesis_label)

        if self.status is not None and not isinstance(self.status, MechanisticHypothesisStatusEnum):
            self.status = MechanisticHypothesisStatusEnum(self.status)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.applies_to_subtypes, list):
            self.applies_to_subtypes = [self.applies_to_subtypes] if self.applies_to_subtypes is not None else []
        self.applies_to_subtypes = [v if isinstance(v, str) else str(v) for v in self.applies_to_subtypes]

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Discussion(YAMLRoot):
    """
    A thread-like record of an open question, controversy, curation todo, emerging hypothesis, or interpretation
    debate attached to a disease entry or sub-object. Discussions capture the *discourse* layer of curation (what is
    being argued or asked), complementing the structural knowledge-gap layer proposed in
    monarch-initiative/dismech#2617 (what is missing from the model). External thread links (e.g., Alzforum
    commentaries, GitHub issues) are not modelled as a separate slot; instead they are cited via the standard
    `evidence` block using the same EvidenceItem shape as primary literature.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Discussion"]
    class_class_curie: ClassVar[str] = "dismech:Discussion"
    class_name: ClassVar[str] = "Discussion"
    class_model_uri: ClassVar[URIRef] = DISMECH.Discussion

    discussion_id: str = None
    prompt: str = None
    kind: Optional[Union[str, "DiscussionKindEnum"]] = None
    status: Optional[Union[str, "DiscussionStatusEnum"]] = None
    attaches_to: Optional[Union[str, list[str]]] = empty_list()
    rationale: Optional[str] = None
    proposed_experiments: Optional[Union[dict[Union[str, ExperimentName], Union[dict, Experiment]], list[Union[dict, Experiment]]]] = empty_dict()
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    posed_by: Optional[str] = None
    posed_date: Optional[Union[str, XSDDateTime]] = None
    resolved_date: Optional[Union[str, XSDDateTime]] = None
    resolution_note: Optional[str] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.discussion_id):
            self.MissingRequiredField("discussion_id")
        if not isinstance(self.discussion_id, str):
            self.discussion_id = str(self.discussion_id)

        if self._is_empty(self.prompt):
            self.MissingRequiredField("prompt")
        if not isinstance(self.prompt, str):
            self.prompt = str(self.prompt)

        if self.kind is not None and not isinstance(self.kind, DiscussionKindEnum):
            self.kind = DiscussionKindEnum(self.kind)

        if self.status is not None and not isinstance(self.status, DiscussionStatusEnum):
            self.status = DiscussionStatusEnum(self.status)

        if not isinstance(self.attaches_to, list):
            self.attaches_to = [self.attaches_to] if self.attaches_to is not None else []
        self.attaches_to = [v if isinstance(v, str) else str(v) for v in self.attaches_to]

        if self.rationale is not None and not isinstance(self.rationale, str):
            self.rationale = str(self.rationale)

        self._normalize_inlined_as_list(slot_name="proposed_experiments", slot_type=Experiment, key_name="name", keyed=True)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.posed_by is not None and not isinstance(self.posed_by, str):
            self.posed_by = str(self.posed_by)

        if self.posed_date is not None and not isinstance(self.posed_date, XSDDateTime):
            self.posed_date = XSDDateTime(self.posed_date)

        if self.resolved_date is not None and not isinstance(self.resolved_date, XSDDateTime):
            self.resolved_date = XSDDateTime(self.resolved_date)

        if self.resolution_note is not None and not isinstance(self.resolution_note, str):
            self.resolution_note = str(self.resolution_note)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiseaseCollection(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["DiseaseCollection"]
    class_class_curie: ClassVar[str] = "dismech:DiseaseCollection"
    class_name: ClassVar[str] = "DiseaseCollection"
    class_model_uri: ClassVar[URIRef] = DISMECH.DiseaseCollection

    diseases: Optional[Union[dict[Union[str, DiseaseName], Union[dict, Disease]], list[Union[dict, Disease]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="diseases", slot_type=Disease, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FDASurrogateEndpointCollection(SurrogateEndpointCollection):
    """
    FDA surrogate endpoint table import preserving row-level source provenance
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["FDASurrogateEndpointCollection"]
    class_class_curie: ClassVar[str] = "dismech:FDASurrogateEndpointCollection"
    class_name: ClassVar[str] = "FDASurrogateEndpointCollection"
    class_model_uri: ClassVar[URIRef] = DISMECH.FDASurrogateEndpointCollection

    name: Union[str, FDASurrogateEndpointCollectionName] = None
    surrogate_endpoints: Union[dict[Union[str, SurrogateEndpointRowId], Union[dict, SurrogateEndpoint]], list[Union[dict, SurrogateEndpoint]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, FDASurrogateEndpointCollectionName):
            self.name = FDASurrogateEndpointCollectionName(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Grouping(YAMLRoot):
    """
    An explicit, curated union of distinct Disease entries assembled below the level of the formal classification
    taxonomies. A Grouping points DOWN: it lists its members rather than being inferred from them, and it does not
    recapitulate MONDO (an optional `mappings` block may cross-reference an external grouping term). Its purpose is to
    make the grouping boundary auditable — recording WHY these conditions are grouped (`grouping_basis`,
    `grouping_rationale`), the shared `membership_criteria` (prose plus an optional boolean expression), and, per
    member, the mechanisms that differentiate it from its siblings.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Grouping"]
    class_class_curie: ClassVar[str] = "dismech:Grouping"
    class_name: ClassVar[str] = "Grouping"
    class_model_uri: ClassVar[URIRef] = DISMECH.Grouping

    name: Union[str, GroupingName] = None
    members: Union[Union[dict, "GroupingMember"], list[Union[dict, "GroupingMember"]]] = None
    display_name: Optional[str] = None
    creation_date: Optional[str] = None
    description: Optional[str] = None
    grouping_basis: Optional[Union[Union[str, "GroupingBasisEnum"], list[Union[str, "GroupingBasisEnum"]]]] = empty_list()
    grouping_rationale: Optional[str] = None
    membership_criteria: Optional[Union[Union[dict, "GroupingCriteria"], list[Union[dict, "GroupingCriteria"]]]] = empty_list()
    mappings: Optional[Union[dict, DiseaseMappings]] = None
    references: Optional[Union[dict[Union[str, PublicationReferenceReference], Union[dict, PublicationReference]], list[Union[dict, PublicationReference]]]] = empty_dict()
    discussions: Optional[Union[Union[dict, Discussion], list[Union[dict, Discussion]]]] = empty_list()
    curation_history: Optional[Union[Union[dict, CurationEvent], list[Union[dict, CurationEvent]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, GroupingName):
            self.name = GroupingName(self.name)

        if self._is_empty(self.members):
            self.MissingRequiredField("members")
        self._normalize_inlined_as_list(slot_name="members", slot_type=GroupingMember, key_name="member", keyed=False)

        if self.display_name is not None and not isinstance(self.display_name, str):
            self.display_name = str(self.display_name)

        if self.creation_date is not None and not isinstance(self.creation_date, str):
            self.creation_date = str(self.creation_date)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.grouping_basis, list):
            self.grouping_basis = [self.grouping_basis] if self.grouping_basis is not None else []
        self.grouping_basis = [v if isinstance(v, GroupingBasisEnum) else GroupingBasisEnum(v) for v in self.grouping_basis]

        if self.grouping_rationale is not None and not isinstance(self.grouping_rationale, str):
            self.grouping_rationale = str(self.grouping_rationale)

        self._normalize_inlined_as_list(slot_name="membership_criteria", slot_type=GroupingCriteria, key_name="description", keyed=False)

        if self.mappings is not None and not isinstance(self.mappings, DiseaseMappings):
            self.mappings = DiseaseMappings(**as_dict(self.mappings))

        self._normalize_inlined_as_list(slot_name="references", slot_type=PublicationReference, key_name="reference", keyed=True)

        self._normalize_inlined_as_list(slot_name="discussions", slot_type=Discussion, key_name="discussion_id", keyed=False)

        self._normalize_inlined_as_list(slot_name="curation_history", slot_type=CurationEvent, key_name="curation_timestamp", keyed=False)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GroupingCriteria(YAMLRoot):
    """
    The shared membership criteria for a grouping, pairing a human-readable description with an optional structured
    boolean expression and a necessary/sufficient/equivalent semantics marker.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["GroupingCriteria"]
    class_class_curie: ClassVar[str] = "dismech:GroupingCriteria"
    class_name: ClassVar[str] = "GroupingCriteria"
    class_model_uri: ClassVar[URIRef] = DISMECH.GroupingCriteria

    description: str = None
    criteria_semantics: Optional[Union[str, "CriteriaSemanticsEnum"]] = None
    logic: Optional[Union[dict, "LogicalCriterion"]] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.criteria_semantics is not None and not isinstance(self.criteria_semantics, CriteriaSemanticsEnum):
            self.criteria_semantics = CriteriaSemanticsEnum(self.criteria_semantics)

        if self.logic is not None and not isinstance(self.logic, LogicalCriterion):
            self.logic = LogicalCriterion(**as_dict(self.logic))

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LogicalCriterion(YAMLRoot):
    """
    A node in a nested boolean membership-criteria expression. A branch node sets `operator` and combines child
    `operands`; a leaf node sets `criterion_predicate` and the payload slots relevant to that predicate. This is a
    deliberately lightweight, OWL-inspired representation, not a full logical formalism.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["LogicalCriterion"]
    class_class_curie: ClassVar[str] = "dismech:LogicalCriterion"
    class_name: ClassVar[str] = "LogicalCriterion"
    class_model_uri: ClassVar[URIRef] = DISMECH.LogicalCriterion

    operator: Optional[Union[str, "LogicalOperatorEnum"]] = None
    operands: Optional[Union[Union[dict, "LogicalCriterion"], list[Union[dict, "LogicalCriterion"]]]] = empty_list()
    criterion_predicate: Optional[Union[str, "CriterionPredicateEnum"]] = None
    description: Optional[str] = None
    negated: Optional[Union[bool, Bool]] = None
    phenotype_term: Optional[Union[dict, PhenotypeDescriptor]] = None
    min_frequency: Optional[Union[str, "FrequencyEnum"]] = None
    inheritance_term: Optional[Union[dict, InheritanceDescriptor]] = None
    gene: Optional[Union[dict, GeneDescriptor]] = None
    biological_processes: Optional[Union[Union[dict, BiologicalProcessDescriptor], list[Union[dict, BiologicalProcessDescriptor]]]] = empty_list()
    module: Optional[str] = None
    classification: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.operator is not None and not isinstance(self.operator, LogicalOperatorEnum):
            self.operator = LogicalOperatorEnum(self.operator)

        if not isinstance(self.operands, list):
            self.operands = [self.operands] if self.operands is not None else []
        self.operands = [v if isinstance(v, LogicalCriterion) else LogicalCriterion(**as_dict(v)) for v in self.operands]

        if self.criterion_predicate is not None and not isinstance(self.criterion_predicate, CriterionPredicateEnum):
            self.criterion_predicate = CriterionPredicateEnum(self.criterion_predicate)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.negated is not None and not isinstance(self.negated, Bool):
            self.negated = Bool(self.negated)

        if self.phenotype_term is not None and not isinstance(self.phenotype_term, PhenotypeDescriptor):
            self.phenotype_term = PhenotypeDescriptor(**as_dict(self.phenotype_term))

        if self.min_frequency is not None and not isinstance(self.min_frequency, FrequencyEnum):
            self.min_frequency = FrequencyEnum(self.min_frequency)

        if self.inheritance_term is not None and not isinstance(self.inheritance_term, InheritanceDescriptor):
            self.inheritance_term = InheritanceDescriptor(**as_dict(self.inheritance_term))

        if self.gene is not None and not isinstance(self.gene, GeneDescriptor):
            self.gene = GeneDescriptor(**as_dict(self.gene))

        self._normalize_inlined_as_list(slot_name="biological_processes", slot_type=BiologicalProcessDescriptor, key_name="preferred_term", keyed=False)

        if self.module is not None and not isinstance(self.module, str):
            self.module = str(self.module)

        if self.classification is not None and not isinstance(self.classification, str):
            self.classification = str(self.classification)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GroupingMember(YAMLRoot):
    """
    One member of a grouping, referenced by foreign key, together with the mechanisms that differentiate it from its
    siblings.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["GroupingMember"]
    class_class_curie: ClassVar[str] = "dismech:GroupingMember"
    class_name: ClassVar[str] = "GroupingMember"
    class_model_uri: ClassVar[URIRef] = DISMECH.GroupingMember

    member: str = None
    member_type: Optional[Union[str, "GroupingMemberTypeEnum"]] = None
    display_name: Optional[str] = None
    disease_term: Optional[Union[dict, DiseaseDescriptor]] = None
    differentiating_mechanisms: Optional[Union[Union[dict, "DifferentiatingMechanism"], list[Union[dict, "DifferentiatingMechanism"]]]] = empty_list()
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.member):
            self.MissingRequiredField("member")
        if not isinstance(self.member, str):
            self.member = str(self.member)

        if self.member_type is not None and not isinstance(self.member_type, GroupingMemberTypeEnum):
            self.member_type = GroupingMemberTypeEnum(self.member_type)

        if self.display_name is not None and not isinstance(self.display_name, str):
            self.display_name = str(self.display_name)

        if self.disease_term is not None and not isinstance(self.disease_term, DiseaseDescriptor):
            self.disease_term = DiseaseDescriptor(**as_dict(self.disease_term))

        self._normalize_inlined_as_list(slot_name="differentiating_mechanisms", slot_type=DifferentiatingMechanism, key_name="description", keyed=False)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DifferentiatingMechanism(YAMLRoot):
    """
    A mechanism or feature that distinguishes a grouping member from its siblings, as prose plus optional structured
    descriptors (gene, phenotype, biological process, module).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["DifferentiatingMechanism"]
    class_class_curie: ClassVar[str] = "dismech:DifferentiatingMechanism"
    class_name: ClassVar[str] = "DifferentiatingMechanism"
    class_model_uri: ClassVar[URIRef] = DISMECH.DifferentiatingMechanism

    description: str = None
    gene: Optional[Union[dict, GeneDescriptor]] = None
    phenotype_term: Optional[Union[dict, PhenotypeDescriptor]] = None
    biological_processes: Optional[Union[Union[dict, BiologicalProcessDescriptor], list[Union[dict, BiologicalProcessDescriptor]]]] = empty_list()
    module: Optional[str] = None
    modifier: Optional[Union[str, "ModifierEnum"]] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.gene is not None and not isinstance(self.gene, GeneDescriptor):
            self.gene = GeneDescriptor(**as_dict(self.gene))

        if self.phenotype_term is not None and not isinstance(self.phenotype_term, PhenotypeDescriptor):
            self.phenotype_term = PhenotypeDescriptor(**as_dict(self.phenotype_term))

        self._normalize_inlined_as_list(slot_name="biological_processes", slot_type=BiologicalProcessDescriptor, key_name="preferred_term", keyed=False)

        if self.module is not None and not isinstance(self.module, str):
            self.module = str(self.module)

        if self.modifier is not None and not isinstance(self.modifier, ModifierEnum):
            self.modifier = ModifierEnum(self.modifier)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModuleCollection(YAMLRoot):
    """
    A curated navigation or framework record that organizes mechanism modules. A ModuleCollection is not itself a
    mechanism and does not assert disease membership. It points down to module filename stems, may nest more specific
    collections, and may cite the publication that defines the framework.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ModuleCollection"]
    class_class_curie: ClassVar[str] = "dismech:ModuleCollection"
    class_name: ClassVar[str] = "ModuleCollection"
    class_model_uri: ClassVar[URIRef] = DISMECH.ModuleCollection

    name: Union[str, ModuleCollectionName] = None
    collection_type: Union[str, "ModuleCollectionTypeEnum"] = None
    module_members: Union[Union[dict, "ModuleCollectionMember"], list[Union[dict, "ModuleCollectionMember"]]] = None
    display_name: Optional[str] = None
    creation_date: Optional[str] = None
    description: Optional[str] = None
    child_collections: Optional[Union[str, list[str]]] = empty_list()
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ModuleCollectionName):
            self.name = ModuleCollectionName(self.name)

        if self._is_empty(self.collection_type):
            self.MissingRequiredField("collection_type")
        if not isinstance(self.collection_type, ModuleCollectionTypeEnum):
            self.collection_type = ModuleCollectionTypeEnum(self.collection_type)

        if self._is_empty(self.module_members):
            self.MissingRequiredField("module_members")
        self._normalize_inlined_as_list(slot_name="module_members", slot_type=ModuleCollectionMember, key_name="module", keyed=False)

        if self.display_name is not None and not isinstance(self.display_name, str):
            self.display_name = str(self.display_name)

        if self.creation_date is not None and not isinstance(self.creation_date, str):
            self.creation_date = str(self.creation_date)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.child_collections, list):
            self.child_collections = [self.child_collections] if self.child_collections is not None else []
        self.child_collections = [v if isinstance(v, str) else str(v) for v in self.child_collections]

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModuleCollectionMember(YAMLRoot):
    """
    A mechanism module included in a ModuleCollection, with optional labels and explanation specific to the source
    framework.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["ModuleCollectionMember"]
    class_class_curie: ClassVar[str] = "dismech:ModuleCollectionMember"
    class_name: ClassVar[str] = "ModuleCollectionMember"
    class_model_uri: ClassVar[URIRef] = DISMECH.ModuleCollectionMember

    module: str = None
    framework_terms: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.module):
            self.MissingRequiredField("module")
        if not isinstance(self.module, str):
            self.module = str(self.module)

        if not isinstance(self.framework_terms, list):
            self.framework_terms = [self.framework_terms] if self.framework_terms is not None else []
        self.framework_terms = [v if isinstance(v, str) else str(v) for v in self.framework_terms]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


# Enumerations
class EvidenceItemSupportEnum(EnumDefinitionImpl):
    """
    Which way the cited evidence cuts relative to the claim. This is direction only. How *directly* the quote bears on
    the claim is a separate axis -- see DirectnessEnum and the `directness` slot -- and how strong the evidence is has
    no slot at all (see design decisions section 12).
    """
    SUPPORT = PermissibleValue(
        text="SUPPORT",
        title="Supports",
        description="The cited evidence supports the claim")
    REFUTE = PermissibleValue(
        text="REFUTE",
        title="Refutes",
        description="The cited evidence contradicts the claim")
    NO_EVIDENCE = PermissibleValue(
        text="NO_EVIDENCE",
        title="No evidence",
        description="The cited reference does not contain evidence relevant to the claim")

    _defn = EnumDefinition(
        name="EvidenceItemSupportEnum",
        description="""Which way the cited evidence cuts relative to the claim. This is direction only. How *directly* the quote bears on the claim is a separate axis -- see DirectnessEnum and the `directness` slot -- and how strong the evidence is has no slot at all (see design decisions section 12).""",
    )

class DirectnessEnum(EnumDefinitionImpl):
    """
    How directly the quoted evidence bears on the claim it is attached to. The evidential counterpart of
    CausalLinkTypeEnum, which records the same notion of directness for a causal edge.
    """
    DIRECT = PermissibleValue(
        text="DIRECT",
        title="Direct",
        description="The quoted text asserts the claim itself")
    INDIRECT = PermissibleValue(
        text="INDIRECT",
        title="Indirect",
        description="""The quoted text asserts something from which the claim follows by an inference step -- for example a therapeutic response cited as validation of the mechanism it targets, or a result from an inverted or non-human model system.""")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        title="Unknown",
        description="Directness has not yet been assessed")

    _defn = EnumDefinition(
        name="DirectnessEnum",
        description="""How directly the quoted evidence bears on the claim it is attached to. The evidential counterpart of CausalLinkTypeEnum, which records the same notion of directness for a causal edge.""",
    )

class EvidenceSourceEnum(EnumDefinitionImpl):
    """
    The provenance/source of the evidence item
    """
    HUMAN_CLINICAL = PermissibleValue(
        text="HUMAN_CLINICAL",
        title="Human clinical",
        description="Human clinical observations (patients, cohorts, case reports, clinical trials, epidemiology)")
    MODEL_ORGANISM = PermissibleValue(
        text="MODEL_ORGANISM",
        title="Model organism",
        description="""In vivo animal evidence (mouse, zebrafish, primate, veterinary case series including dog/cat/horse, other non-human animal models etc.)""")
    IN_VITRO = PermissibleValue(
        text="IN_VITRO",
        title="In vitro / ex vivo",
        description="In vitro or ex vivo assays (cell culture, organoids, tissue slices, biochemical assays)")
    COMPUTATIONAL = PermissibleValue(
        text="COMPUTATIONAL",
        title="Computational",
        description="""In silico/modeling studies (simulation, docking, ML predictions, network inference) even when using clinical data inputs""")
    OTHER = PermissibleValue(
        text="OTHER",
        title="Other",
        description="""Evidence not fitting the above (e.g., expert consensus without data, image atlases without cohort context)""")

    _defn = EnumDefinition(
        name="EvidenceSourceEnum",
        description="The provenance/source of the evidence item",
    )

class DefinitionTypeEnum(EnumDefinitionImpl):
    """
    The type of definition or criteria set
    """
    DIAGNOSTIC_CRITERIA = PermissibleValue(
        text="DIAGNOSTIC_CRITERIA",
        description="Published diagnostic criteria (clinical/serologic/imaging)")
    PHENOTYPE_ALGORITHM = PermissibleValue(
        text="PHENOTYPE_ALGORITHM",
        description="Algorithmic phenotype definition (e.g., PheKB-/OHDSI-style)")
    CASE_DEFINITION = PermissibleValue(
        text="CASE_DEFINITION",
        description="Case definition for surveillance or reporting")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Other definition type")

    _defn = EnumDefinition(
        name="DefinitionTypeEnum",
        description="The type of definition or criteria set",
    )

class DefinitionDerivationBasisEnum(EnumDefinitionImpl):
    """
    The epistemic grounding of a definition / phenotype algorithm, orthogonal to definition_type. Records where the
    definition comes from and how well established it is, so a mechanism-predicated case-finding query is not
    conflated with a consensus- or gold-standard-validated one. When the basis is a hypothesis, the definition should
    attaches_to the pathophysiology node(s)/edge(s) it is predicated on, so the basis can be cross-checked against
    those edges' hypothesis_groups.
    """
    ESTABLISHED_CRITERIA = PermissibleValue(
        text="ESTABLISHED_CRITERIA",
        description="""Published consensus criteria or a validated computable phenotype (e.g. an OHDSI Phenotype Library cohort). The implicit default for existing definitions.""")
    MECHANISTIC_HYPOTHESIS = PermissibleValue(
        text="MECHANISTIC_HYPOTHESIS",
        description="""Predicated on a specific, not-yet-proven disease mechanism hypothesis; membership is contingent on that hypothesis holding.""")
    MODEL_SYSTEM_EXTRAPOLATION = PermissibleValue(
        text="MODEL_SYSTEM_EXTRAPOLATION",
        description="Extrapolated from an animal or in-vitro model result not yet demonstrated in humans.")

    _defn = EnumDefinition(
        name="DefinitionDerivationBasisEnum",
        description="""The epistemic grounding of a definition / phenotype algorithm, orthogonal to definition_type. Records where the definition comes from and how well established it is, so a mechanism-predicated case-finding query is not conflated with a consensus- or gold-standard-validated one. When the basis is a hypothesis, the definition should attaches_to the pathophysiology node(s)/edge(s) it is predicated on, so the basis can be cross-checked against those edges' hypothesis_groups.""",
    )

class AlgorithmValidationStatusEnum(EnumDefinitionImpl):
    """
    Validation maturity of a phenotype algorithm / computable case definition.
    """
    PROPOSED = PermissibleValue(
        text="PROPOSED",
        description="Drafted; never executed against data.")
    UNVALIDATED = PermissibleValue(
        text="UNVALIDATED",
        description="Executable but not yet evaluated against a gold-standard or labeled cohort.")
    VALIDATED_AGAINST_GOLD_STANDARD = PermissibleValue(
        text="VALIDATED_AGAINST_GOLD_STANDARD",
        description="PPV/sensitivity characterized against a reference standard.")

    _defn = EnumDefinition(
        name="AlgorithmValidationStatusEnum",
        description="Validation maturity of a phenotype algorithm / computable case definition.",
    )

class MappingConsistencyEnum(EnumDefinitionImpl):
    """
    Consistency of a mapping relative to another reference source
    """
    CONSISTENT = PermissibleValue(
        text="CONSISTENT",
        description="Mapping is consistent with the reference source")
    INCONSISTENT = PermissibleValue(
        text="INCONSISTENT",
        description="Mapping conflicts with the reference source")
    MISSING = PermissibleValue(
        text="MISSING",
        description="Mapping is missing from the reference source")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="Consistency not assessed or unclear")

    _defn = EnumDefinition(
        name="MappingConsistencyEnum",
        description="Consistency of a mapping relative to another reference source",
    )

class FrequencyEnum(EnumDefinitionImpl):
    """
    The frequency of an event or phenomenon
    """
    OBLIGATE = PermissibleValue(
        text="OBLIGATE",
        title="Obligate (100%)",
        description="Present in all cases (100% of patients)",
        meaning=HP["0040280"])
    VERY_FREQUENT = PermissibleValue(
        text="VERY_FREQUENT",
        title="Very frequent (80-99%)",
        description="Present in most cases (80-99% of patients)",
        meaning=HP["0040281"])
    FREQUENT = PermissibleValue(
        text="FREQUENT",
        title="Frequent (30-79%)",
        description="Present in many cases (30-79% of patients)",
        meaning=HP["0040282"])
    OCCASIONAL = PermissibleValue(
        text="OCCASIONAL",
        title="Occasional (5-29%)",
        description="Present in some cases (5-29% of patients)",
        meaning=HP["0040283"])
    VERY_RARE = PermissibleValue(
        text="VERY_RARE",
        title="Very rare (<5%)",
        description="Present in rare cases (<5% of patients)",
        meaning=HP["0040284"])

    _defn = EnumDefinition(
        name="FrequencyEnum",
        description="The frequency of an event or phenomenon",
    )

class PrevalenceMeasureEnum(EnumDefinitionImpl):
    """
    The kind of epidemiological measure a Prevalence record reports. Disease occurrence is reported in several
    non-interchangeable ways; this enum makes the measure explicit so a point prevalence is never silently compared
    with an incidence rate or a literature case-count. Mirrors the "type" column of the Orphanet epidemiology table.
    """
    POINT_PREVALENCE = PermissibleValue(
        text="POINT_PREVALENCE",
        title="Point prevalence",
        description="Proportion of a population affected at a single point in time.")
    BIRTH_PREVALENCE = PermissibleValue(
        text="BIRTH_PREVALENCE",
        title="Prevalence at birth",
        description="Proportion of live births (or births) affected; common for congenital disorders.")
    LIFETIME_PREVALENCE = PermissibleValue(
        text="LIFETIME_PREVALENCE",
        title="Lifetime prevalence",
        description="Proportion of a population affected at some point during their lifetime.")
    PERIOD_PREVALENCE = PermissibleValue(
        text="PERIOD_PREVALENCE",
        title="Period prevalence",
        description="""Proportion of a population affected during a defined interval (e.g., five-year period prevalence).""")
    ANNUAL_INCIDENCE = PermissibleValue(
        text="ANNUAL_INCIDENCE",
        title="Annual incidence",
        description="Rate of new cases arising in a population per year (an incidence, not a prevalence).")
    CARRIER_FREQUENCY = PermissibleValue(
        text="CARRIER_FREQUENCY",
        title="Carrier frequency",
        description="Frequency of heterozygous carriers in a population (not affected individuals).")
    CASES_IN_LITERATURE = PermissibleValue(
        text="CASES_IN_LITERATURE",
        title="Cases/families reported in the literature",
        description="""Count of reported cases or families rather than a population rate; used for ultra-rare disorders where no denominator-based estimate exists.""")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        title="Unknown",
        description="The measure type is not stated or cannot be determined from the source.")

    _defn = EnumDefinition(
        name="PrevalenceMeasureEnum",
        description="""The kind of epidemiological measure a Prevalence record reports. Disease occurrence is reported in several non-interchangeable ways; this enum makes the measure explicit so a point prevalence is never silently compared with an incidence rate or a literature case-count. Mirrors the \"type\" column of the Orphanet epidemiology table.""",
    )

class PrevalenceClassEnum(EnumDefinitionImpl):
    """
    Coarse, always-fillable band for disease occurrence — the population-rate analog of the HPO-style FrequencyEnum
    used for phenotype frequency. The numeric bands are the Orphanet prevalence classes (so the ~7% of records already
    quoting Orphanet map directly and the ICEES/ORPHA structured sources stay aligned); the qualitative tiers cover
    records that report only prose ("rare", "common") with no numeric estimate. When a numeric estimate exists, also
    populate rate_per_100000 (or rate_low/rate_high); the band is the queryable summary, the rate carries the
    precision.
    """
    ABOVE_1_IN_1000 = PermissibleValue(
        text="ABOVE_1_IN_1000",
        title=">1 / 1,000",
        description="More than 1 in 1,000 (more than 100 per 100,000). Orphanet class.")
    BAND_1_5_PER_10000 = PermissibleValue(
        text="BAND_1_5_PER_10000",
        title="1-9 / 10,000",
        description="""1 to 9 per 10,000 (10-99 per 100,000). Combines the Orphanet 1-5 and 6-9 per 10,000 classes into one decade-spanning band, matching the other per-decade bands and the _band_from_rate() boundaries.""")
    BAND_1_9_PER_100000 = PermissibleValue(
        text="BAND_1_9_PER_100000",
        title="1-9 / 100,000",
        description="1 to 9 per 100,000. Orphanet class.")
    BAND_1_9_PER_1000000 = PermissibleValue(
        text="BAND_1_9_PER_1000000",
        title="1-9 / 1,000,000",
        description="1 to 9 per 1,000,000 (0.1-0.9 per 100,000). Orphanet class.")
    BELOW_1_IN_1000000 = PermissibleValue(
        text="BELOW_1_IN_1000000",
        title="<1 / 1,000,000",
        description="Fewer than 1 in 1,000,000 (less than 0.1 per 100,000). Orphanet class.")
    COMMON = PermissibleValue(
        text="COMMON",
        title="Common",
        description="""Qualitative tier for disorders described as common/endemic with no numeric estimate captured. Roughly corresponds to the >1/1,000 region but asserted only qualitatively.""")
    RARE = PermissibleValue(
        text="RARE",
        title="Rare",
        description="""Qualitative tier for disorders described as \"rare\" in the source without a numeric estimate (the EU rare-disease threshold is <1 in 2,000).""")
    ULTRA_RARE = PermissibleValue(
        text="ULTRA_RARE",
        title="Ultra-rare",
        description="""Qualitative tier for disorders described as ultra-rare / only a handful of reported cases, with no population rate available. Often paired with measure_type CASES_IN_LITERATURE.""")
    NOT_YET_DOCUMENTED = PermissibleValue(
        text="NOT_YET_DOCUMENTED",
        title="Not yet documented",
        description="Source states prevalence is not yet documented. Orphanet class.")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        title="Unknown",
        description="Prevalence is unknown or not stated.")

    _defn = EnumDefinition(
        name="PrevalenceClassEnum",
        description="""Coarse, always-fillable band for disease occurrence — the population-rate analog of the HPO-style FrequencyEnum used for phenotype frequency. The numeric bands are the Orphanet prevalence classes (so the ~7% of records already quoting Orphanet map directly and the ICEES/ORPHA structured sources stay aligned); the qualitative tiers cover records that report only prose (\"rare\", \"common\") with no numeric estimate. When a numeric estimate exists, also populate rate_per_100000 (or rate_low/rate_high); the band is the queryable summary, the rate carries the precision.""",
    )

class ClinicalSignificanceEnum(EnumDefinitionImpl):
    """
    The clinical significance of a variant for a condition (ACMG guidelines)
    """
    PATHOGENIC = PermissibleValue(
        text="PATHOGENIC",
        title="Pathogenic",
        description="Variant is pathogenic for the condition (ACMG class 5)",
        meaning=GENO["0000840"])
    LIKELY_PATHOGENIC = PermissibleValue(
        text="LIKELY_PATHOGENIC",
        title="Likely pathogenic",
        description="Variant is likely pathogenic for the condition (ACMG class 4)",
        meaning=GENO["0000841"])
    BENIGN = PermissibleValue(
        text="BENIGN",
        title="Benign",
        description="Variant is benign for the condition (ACMG class 1)",
        meaning=GENO["0000843"])
    LIKELY_BENIGN = PermissibleValue(
        text="LIKELY_BENIGN",
        title="Likely benign",
        description="Variant is likely benign for the condition (ACMG class 2)",
        meaning=GENO["0000844"])
    UNCERTAIN_SIGNIFICANCE = PermissibleValue(
        text="UNCERTAIN_SIGNIFICANCE",
        title="Uncertain significance",
        description="Clinical significance of the variant is uncertain (ACMG class 3)",
        meaning=GENO["0000845"])

    _defn = EnumDefinition(
        name="ClinicalSignificanceEnum",
        description="The clinical significance of a variant for a condition (ACMG guidelines)",
    )

class RegulatoryVariantCategoryEnum(EnumDefinitionImpl):
    """
    Functional classification of non-coding gene regulatory variants based on their impact on gene expression
    patterns. Adapted from Cheng et al. 2024 (PMID:38436667). Includes traditional coding variant categories for
    completeness.
    """
    LOE = PermissibleValue(
        text="LOE",
        title="Loss of expression",
        description="""Non-modular loss-of-expression. Diminishes or abolishes gene expression across all cell types that intrinsically express the gene. Analogous to coding amorphic or hypomorphic loss-of-function.""")
    mLOE = PermissibleValue(
        text="mLOE",
        title="Modular loss of expression",
        description="""Modular loss-of-expression. Diminishes or abolishes gene expression in only a subset of cell types or developmental windows. Represents a disease mechanism largely unique to non-coding regulatory variants.""")
    GOE = PermissibleValue(
        text="GOE",
        title="Gain of ectopic expression",
        description="""Gain-of-ectopic-expression. Results in ectopic spatial and/or temporal expression of a gene. Can arise from enhancer adoption, novel TFBS creation, promoter switching, or repressor site disruption.""")
    LOF = PermissibleValue(
        text="LOF",
        title="Loss of function",
        description="""Coding loss-of-function. Loss of normal biological function via complete (amorphic) or partial (hypomorphic) loss of protein activity.""")
    GOF = PermissibleValue(
        text="GOF",
        title="Gain of function",
        description="""Coding gain-of-function. Creates a protein with increased activity (hypermorphic) or entirely new function (neomorphic).""")
    DN = PermissibleValue(
        text="DN",
        title="Dominant negative",
        description="""Dominant-negative. Creates a protein that blocks the normal function of the remaining wild-type protein (antimorphic).""")

    _defn = EnumDefinition(
        name="RegulatoryVariantCategoryEnum",
        description="""Functional classification of non-coding gene regulatory variants based on their impact on gene expression patterns. Adapted from Cheng et al. 2024 (PMID:38436667). Includes traditional coding variant categories for completeness.""",
    )

class RegulatoryElementTypeEnum(EnumDefinitionImpl):
    """
    Type of gene regulatory element disrupted by a non-coding variant.
    """
    PROMOTER = PermissibleValue(
        text="PROMOTER",
        title="Promoter",
        description="""Promoter-proximal element overlapping the transcription start site, containing core TF binding elements (TATA, CAAT, GC, CACCC boxes).""")
    ENHANCER = PermissibleValue(
        text="ENHANCER",
        title="Enhancer",
        description="""Distal regulatory element that upregulates transcriptional activity. May be cell-type-specific or shared across cell types.""")
    SILENCER = PermissibleValue(
        text="SILENCER",
        title="Silencer",
        description="Regulatory element that represses or silences gene transcription.")
    INSULATOR = PermissibleValue(
        text="INSULATOR",
        title="Insulator",
        description="""Boundary element (often CTCF-bound) that compartmentalizes adjacent gene regulatory domains and limits enhancer-promoter interactions.""")
    TAD_BOUNDARY = PermissibleValue(
        text="TAD_BOUNDARY",
        title="TAD boundary",
        description="""Topologically associating domain boundary. Structural element maintaining chromatin loop domains; disruption can cause enhancer adoption or ectopic regulatory interactions.""")
    LOCUS_CONTROL_REGION = PermissibleValue(
        text="LOCUS_CONTROL_REGION",
        title="Locus control region",
        description="""A cluster of regulatory elements that controls expression of a gene cluster (e.g., the beta-globin LCR).""")

    _defn = EnumDefinition(
        name="RegulatoryElementTypeEnum",
        description="Type of gene regulatory element disrupted by a non-coding variant.",
    )

class GeneDiseaseRelationshipEnum(EnumDefinitionImpl):
    """
    The qualitative relationship between a gene (or locus) and a disease. Use to constrain the free-text `association`
    slot to a controlled vocabulary aligned with ClinGen gene-disease validity concepts and common cancer/somatic
    driver classifications. The free-text `association` slot may still be used for narrative detail.
    """
    CAUSATIVE = PermissibleValue(
        text="CAUSATIVE",
        title="Causative",
        description="""Variants in the gene are sufficient to cause the disease in a mendelian or near-mendelian sense (corresponds to ClinGen \"Definitive\" or \"Strong\" gene-disease validity).""")
    RISK_FACTOR = PermissibleValue(
        text="RISK_FACTOR",
        title="Risk factor",
        description="""Variants in the gene increase risk of disease but are neither necessary nor sufficient to cause it. Includes common-variant associations and HLA risk alleles.""")
    PROTECTIVE = PermissibleValue(
        text="PROTECTIVE",
        title="Protective",
        description="Variants in the gene reduce the risk or severity of disease.")
    MODIFIER = PermissibleValue(
        text="MODIFIER",
        title="Modifier",
        description="""Variants in the gene modify the severity, age of onset, or expressivity of disease without being a primary driver.""")
    SUSCEPTIBILITY = PermissibleValue(
        text="SUSCEPTIBILITY",
        title="Susceptibility",
        description="""Variants in the gene confer susceptibility to disease in combination with other genetic or environmental factors. Used for polygenic susceptibility loci such as GWAS hits.""")
    SOMATIC_DRIVER = PermissibleValue(
        text="SOMATIC_DRIVER",
        title="Somatic driver",
        description="""Somatic alterations in the gene drive tumor initiation or progression (e.g., recurrent oncogenic drivers in cancer).""")
    COOPERATING = PermissibleValue(
        text="COOPERATING",
        title="Cooperating alteration",
        description="""Co-occurring somatic or germline alterations that cooperate with a primary driver to shape disease behavior or therapy response.""")
    BIOMARKER = PermissibleValue(
        text="BIOMARKER",
        title="Biomarker",
        description="""Gene whose expression, mutation, or amplification status serves as a diagnostic, prognostic, or predictive biomarker without a required causal role.""")
    DISPUTED = PermissibleValue(
        text="DISPUTED",
        title="Disputed",
        description="""Reported gene-disease association whose validity is contested (corresponds to ClinGen \"Disputed\" or \"Refuted\").""")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        title="Unknown",
        description="The relationship between the gene and the disease is unclear or not yet classified.")

    _defn = EnumDefinition(
        name="GeneDiseaseRelationshipEnum",
        description="""The qualitative relationship between a gene (or locus) and a disease. Use to constrain the free-text `association` slot to a controlled vocabulary aligned with ClinGen gene-disease validity concepts and common cancer/somatic driver classifications. The free-text `association` slot may still be used for narrative detail.""",
    )

class VariantOriginEnum(EnumDefinitionImpl):
    """
    The origin of variation in a gene with respect to a disease entry. Bound to GENO allele origin terms.
    """
    GERMLINE = PermissibleValue(
        text="GERMLINE",
        title="Germline",
        description="germline allele origin",
        meaning=GENO["0000888"])
    SOMATIC = PermissibleValue(
        text="SOMATIC",
        title="Somatic",
        description="somatic allele origin",
        meaning=GENO["0000882"])
    DE_NOVO = PermissibleValue(
        text="DE_NOVO",
        title="De novo",
        description="de novo allele origin",
        meaning=GENO["0000880"])
    GERMLINE_AND_SOMATIC = PermissibleValue(
        text="GERMLINE_AND_SOMATIC",
        title="Germline and somatic",
        description="""The gene is implicated by both germline and somatic variants in the disease (e.g., tumor suppressors with two-hit mechanisms).""")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        title="Unknown",
        description="unknown allele origin",
        meaning=GENO["0000881"])

    _defn = EnumDefinition(
        name="VariantOriginEnum",
        description="""The origin of variation in a gene with respect to a disease entry. Bound to GENO allele origin terms.""",
    )

class AllelicHitRoleEnum(EnumDefinitionImpl):
    """
    Role of a genetic alteration in a multi-hit disease mechanism. This is intentionally separate from variant origin,
    event type, and functional impact so two-hit models can be represented compositionally.
    """
    FIRST_HIT = PermissibleValue(
        text="FIRST_HIT",
        title="First hit",
        description="""Initial alteration that creates a predisposed or partially disabled state, typically a germline alteration in tumor-suppressor syndromes.""")
    SECOND_HIT = PermissibleValue(
        text="SECOND_HIT",
        title="Second hit",
        description="""Additional alteration that completes functional inactivation or activation in the relevant disease tissue or clone.""")
    BIALLELIC_INACTIVATION = PermissibleValue(
        text="BIALLELIC_INACTIVATION",
        title="Biallelic inactivation",
        description="Combined state in which both alleles of a gene are functionally inactivated.")
    COOPERATING_HIT = PermissibleValue(
        text="COOPERATING_HIT",
        title="Cooperating hit",
        description="""Alteration that cooperates with another primary alteration without necessarily being ordered as the first or second hit.""")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        title="Unknown",
        description="The hit role has not been determined.")

    _defn = EnumDefinition(
        name="AllelicHitRoleEnum",
        description="""Role of a genetic alteration in a multi-hit disease mechanism. This is intentionally separate from variant origin, event type, and functional impact so two-hit models can be represented compositionally.""",
    )

class AllelicEventEnum(EnumDefinitionImpl):
    """
    Type of genetic or epigenetic event affecting an allele. Use together with variant_origin, allelic_hit_role,
    zygosity, and functional impact rather than creating cross-product terms.
    """
    PATHOGENIC_VARIANT = PermissibleValue(
        text="PATHOGENIC_VARIANT",
        title="Pathogenic variant",
        description="Pathogenic sequence variant or small variant not otherwise specified.")
    MISSENSE_VARIANT = PermissibleValue(
        text="MISSENSE_VARIANT",
        title="Missense variant",
        description="Sequence variant that changes an amino acid.")
    NONSENSE_VARIANT = PermissibleValue(
        text="NONSENSE_VARIANT",
        title="Nonsense variant",
        description="Sequence variant that introduces a premature termination codon.")
    FRAMESHIFT_VARIANT = PermissibleValue(
        text="FRAMESHIFT_VARIANT",
        title="Frameshift variant",
        description="Insertion or deletion that changes the coding reading frame.")
    SPLICE_SITE_VARIANT = PermissibleValue(
        text="SPLICE_SITE_VARIANT",
        title="Splice site variant",
        description="Variant that disrupts or alters RNA splicing.")
    DELETION = PermissibleValue(
        text="DELETION",
        title="Deletion",
        description="Sequence or chromosomal deletion event.")
    COPY_NUMBER_LOSS = PermissibleValue(
        text="COPY_NUMBER_LOSS",
        title="Copy-number loss",
        description="Loss of DNA copy number affecting the gene or locus.")
    COPY_NUMBER_GAIN = PermissibleValue(
        text="COPY_NUMBER_GAIN",
        title="Copy-number gain",
        description="Gain of DNA copy number affecting the gene or locus.")
    LOSS_OF_HETEROZYGOSITY = PermissibleValue(
        text="LOSS_OF_HETEROZYGOSITY",
        title="Loss of heterozygosity",
        description="Loss of the wild-type or alternate allele in a tissue or clone.")
    PROMOTER_METHYLATION = PermissibleValue(
        text="PROMOTER_METHYLATION",
        title="Promoter methylation",
        description="Epigenetic promoter methylation affecting gene expression.")
    BIALLELIC_INACTIVATION = PermissibleValue(
        text="BIALLELIC_INACTIVATION",
        title="Biallelic inactivation",
        description="Composite event state in which both alleles are functionally inactivated.")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        title="Unknown",
        description="The allelic event type has not been determined.")

    _defn = EnumDefinition(
        name="AllelicEventEnum",
        description="""Type of genetic or epigenetic event affecting an allele. Use together with variant_origin, allelic_hit_role, zygosity, and functional impact rather than creating cross-product terms.""",
    )

class FunctionalImpactEnum(EnumDefinitionImpl):
    """
    Directional or qualitative functional consequence of a variant or genetic context.
    """
    LOSS_OF_FUNCTION = PermissibleValue(
        text="LOSS_OF_FUNCTION",
        title="Loss of function",
        description="Complete or partial reduction of normal gene product function.")
    GAIN_OF_FUNCTION = PermissibleValue(
        text="GAIN_OF_FUNCTION",
        title="Gain of function",
        description="Increased, novel, or constitutive gene product function.")
    PARTIAL_LOSS_OF_FUNCTION = PermissibleValue(
        text="PARTIAL_LOSS_OF_FUNCTION",
        title="Partial loss of function",
        description="Hypomorphic reduction of normal gene product function.")
    DOMINANT_NEGATIVE = PermissibleValue(
        text="DOMINANT_NEGATIVE",
        title="Dominant negative",
        description="Mutant product interferes with the remaining wild-type product.")
    HYPERMORPHIC = PermissibleValue(
        text="HYPERMORPHIC",
        title="Hypermorphic",
        description="Increased normal gene product activity.")
    NEOMORPHIC = PermissibleValue(
        text="NEOMORPHIC",
        title="Neomorphic",
        description="Novel gene product activity not present in the wild type.")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        title="Unknown",
        description="Functional impact is not known.")

    _defn = EnumDefinition(
        name="FunctionalImpactEnum",
        description="Directional or qualitative functional consequence of a variant or genetic context.",
    )

class ModifierEnum(EnumDefinitionImpl):
    """
    Qualifiers for direction, intensity, functional impact, or pathological state of a descriptor (biological process,
    molecular function, cell type, etc.). GAIN_OF_FUNCTION and LOSS_OF_FUNCTION describe the activity *state* of a
    pathway or process regardless of underlying cause (genetic variant, viral protein, epigenetic silencing,
    post-translational modification, etc.). For the functional consequence of a specific genetic *variant*, use
    GeneticContext.functional_impact_category (FunctionalImpactEnum) instead. Boundary with INCREASED/DECREASED:
    prefer the PATO-bound INCREASED/DECREASED when the claim is *quantitative* — a normally regulated process running
    above or below its normal level. Reserve GAIN_OF_FUNCTION/LOSS_OF_FUNCTION for a *qualitative* change in
    regulatory control, where the process is driven outside its normal regulatory constraints (viral oncoprotein,
    autocrine loop, epigenetic silencing, protein sequestration). Existing INCREASED/DECREASED annotations should not
    be migrated to GAIN_OF_FUNCTION/LOSS_OF_FUNCTION without that qualitative justification.
    """
    INCREASED = PermissibleValue(
        text="INCREASED",
        title="Increased",
        description="Upregulated, hyperactive, elevated, or excessive",
        meaning=PATO["0002300"])
    DECREASED = PermissibleValue(
        text="DECREASED",
        title="Decreased",
        description="Downregulated, hypoactive, reduced, or deficient",
        meaning=PATO["0002301"])
    ABNORMAL = PermissibleValue(
        text="ABNORMAL",
        title="Abnormal",
        description="Qualitatively abnormal (e.g., misfolding, mislocalization, malformed)",
        meaning=PATO["0000460"])
    DYSREGULATED = PermissibleValue(
        text="DYSREGULATED",
        title="Dysregulated",
        description="Regulation is impaired (may be increased or decreased)")
    ABSENT = PermissibleValue(
        text="ABSENT",
        title="Absent",
        description="Not occurring or not present",
        meaning=PATO["0000462"])
    GAIN_OF_FUNCTION = PermissibleValue(
        text="GAIN_OF_FUNCTION",
        title="Gain of function",
        description="""Constitutive or aberrant activation of a pathway, process, or molecular function regardless of underlying mechanism (viral oncoprotein, autocrine loop, post-translational modification, etc.). For mutation-driven GOF, use GeneticContext.functional_impact_category: GAIN_OF_FUNCTION.""")
    LOSS_OF_FUNCTION = PermissibleValue(
        text="LOSS_OF_FUNCTION",
        title="Loss of function",
        description="""Reduction or abolition of normal pathway, process, or molecular function regardless of underlying mechanism (epigenetic silencing, protein sequestration, competitive inhibition, etc.). For mutation-driven LOF, use GeneticContext.functional_impact_category: LOSS_OF_FUNCTION.""")

    _defn = EnumDefinition(
        name="ModifierEnum",
        description="""Qualifiers for direction, intensity, functional impact, or pathological state of a descriptor (biological process, molecular function, cell type, etc.). GAIN_OF_FUNCTION and LOSS_OF_FUNCTION describe the activity *state* of a pathway or process regardless of underlying cause (genetic variant, viral protein, epigenetic silencing, post-translational modification, etc.). For the functional consequence of a specific genetic *variant*, use GeneticContext.functional_impact_category (FunctionalImpactEnum) instead. Boundary with INCREASED/DECREASED: prefer the PATO-bound INCREASED/DECREASED when the claim is *quantitative* — a normally regulated process running above or below its normal level. Reserve GAIN_OF_FUNCTION/LOSS_OF_FUNCTION for a *qualitative* change in regulatory control, where the process is driven outside its normal regulatory constraints (viral oncoprotein, autocrine loop, epigenetic silencing, protein sequestration). Existing INCREASED/DECREASED annotations should not be migrated to GAIN_OF_FUNCTION/LOSS_OF_FUNCTION without that qualitative justification.""",
    )

class DietaryModificationActionEnum(EnumDefinitionImpl):
    """
    Action applied to a food or beverage as part of a dietary treatment
    """
    ADD = PermissibleValue(
        text="ADD",
        title="Add",
        description="Increase intake or deliberately include the specified food or beverage")
    RESTRICT = PermissibleValue(
        text="RESTRICT",
        title="Restrict",
        description="Limit intake of the specified food or beverage without full elimination")
    AVOID = PermissibleValue(
        text="AVOID",
        title="Avoid",
        description="Eliminate or strictly avoid the specified food or beverage")
    SUBSTITUTE = PermissibleValue(
        text="SUBSTITUTE",
        title="Substitute",
        description="Use the specified food or beverage as a replacement within a dietary regimen")

    _defn = EnumDefinition(
        name="DietaryModificationActionEnum",
        description="Action applied to a food or beverage as part of a dietary treatment",
    )

class PenetranceEnum(EnumDefinitionImpl):
    """
    Penetrance classification for inheritance
    """
    COMPLETE = PermissibleValue(
        text="COMPLETE",
        title="Complete",
        description="All individuals with the variant express the phenotype")
    INCOMPLETE = PermissibleValue(
        text="INCOMPLETE",
        title="Incomplete",
        description="Not all individuals with the variant express the phenotype")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        title="Unknown",
        description="Penetrance has not been determined")

    _defn = EnumDefinition(
        name="PenetranceEnum",
        description="Penetrance classification for inheritance",
    )

class ExpressivityEnum(EnumDefinitionImpl):
    """
    Expressivity classification for inheritance
    """
    VARIABLE = PermissibleValue(
        text="VARIABLE",
        title="Variable",
        description="Phenotype severity or features vary among individuals with the same variant")
    CONSISTENT = PermissibleValue(
        text="CONSISTENT",
        title="Consistent",
        description="Phenotype is uniform among individuals with the same variant")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        title="Unknown",
        description="Expressivity has not been determined")

    _defn = EnumDefinition(
        name="ExpressivityEnum",
        description="Expressivity classification for inheritance",
    )

class LateralityEnum(EnumDefinitionImpl):
    """
    Laterality qualifier for anatomical structures or procedures
    """
    LEFT = PermissibleValue(
        text="LEFT",
        title="Left",
        description="Left side of the body")
    RIGHT = PermissibleValue(
        text="RIGHT",
        title="Right",
        description="Right side of the body")
    BILATERAL = PermissibleValue(
        text="BILATERAL",
        title="Bilateral",
        description="Both sides of the body")

    _defn = EnumDefinition(
        name="LateralityEnum",
        description="Laterality qualifier for anatomical structures or procedures",
    )

class SpatialExtentEnum(EnumDefinitionImpl):
    """
    Qualifiers for the spatial extent or distribution of a phenotype or process
    """
    FOCAL = PermissibleValue(
        text="FOCAL",
        title="Focal",
        description="Confined to a single location or region")
    MULTIFOCAL = PermissibleValue(
        text="MULTIFOCAL",
        title="Multifocal",
        description="Affecting multiple discrete locations")
    DIFFUSE = PermissibleValue(
        text="DIFFUSE",
        title="Diffuse",
        description="Widespread, continuous distribution")
    EXTENSIVE = PermissibleValue(
        text="EXTENSIVE",
        title="Extensive",
        description="Large extent, typically involving multiple segments or regions")
    PATCHY = PermissibleValue(
        text="PATCHY",
        title="Patchy",
        description="Irregular, discontinuous distribution")
    SEGMENTAL = PermissibleValue(
        text="SEGMENTAL",
        title="Segmental",
        description="Affecting a specific segment or dermatome")

    _defn = EnumDefinition(
        name="SpatialExtentEnum",
        description="Qualifiers for the spatial extent or distribution of a phenotype or process",
    )

class TemporalityEnum(EnumDefinitionImpl):
    """
    Temporal qualifiers for descriptor post-composition
    """
    ACUTE = PermissibleValue(
        text="ACUTE",
        title="Acute",
        description="Acute manifestation or episode",
        meaning=HP["0011009"])
    TRANSIENT = PermissibleValue(
        text="TRANSIENT",
        title="Transient",
        description="Transient manifestation",
        meaning=HP["0025153"])
    SUBACUTE = PermissibleValue(
        text="SUBACUTE",
        title="Subacute",
        description="Subacute manifestation or episode",
        meaning=HP["0011011"])
    CHRONIC = PermissibleValue(
        text="CHRONIC",
        title="Chronic",
        description="Chronic or persistent over time",
        meaning=HP["0011010"])
    RECURRENT = PermissibleValue(
        text="RECURRENT",
        title="Recurrent",
        description="Repeated episodes separated by symptom-free intervals",
        meaning=HP["0031796"])
    DIURNAL = PermissibleValue(
        text="DIURNAL",
        title="Diurnal",
        description="Manifestation occurring during the day",
        meaning=HP["0025302"])
    NOCTURNAL = PermissibleValue(
        text="NOCTURNAL",
        title="Nocturnal",
        description="Manifestation occurring at night",
        meaning=HP["0025301"])
    PROLONGED = PermissibleValue(
        text="PROLONGED",
        title="Prolonged",
        description="Manifestation lasting longer than typical",
        meaning=HP["0025297"])

    _defn = EnumDefinition(
        name="TemporalityEnum",
        description="Temporal qualifiers for descriptor post-composition",
    )

class ClinicalCourseEnum(EnumDefinitionImpl):
    """
    Clinical course qualifiers for descriptor post-composition
    """
    PROGRESSIVE = PermissibleValue(
        text="PROGRESSIVE",
        title="Progressive",
        description="Worsening over time",
        meaning=HP["0003676"])
    STABLE = PermissibleValue(
        text="STABLE",
        title="Stable",
        description="Not varying in severity or amount over time",
        meaning=HP["0031915"])

    _defn = EnumDefinition(
        name="ClinicalCourseEnum",
        description="Clinical course qualifiers for descriptor post-composition",
    )

class SeverityQualifierEnum(EnumDefinitionImpl):
    """
    Severity qualifiers for descriptor post-composition
    """
    MILD = PermissibleValue(
        text="MILD",
        title="Mild",
        description="Mild severity",
        meaning=HP["0012825"])
    MODERATE = PermissibleValue(
        text="MODERATE",
        title="Moderate",
        description="Moderate severity",
        meaning=HP["0012826"])
    SEVERE = PermissibleValue(
        text="SEVERE",
        title="Severe",
        description="Severe severity",
        meaning=HP["0012828"])

    _defn = EnumDefinition(
        name="SeverityQualifierEnum",
        description="Severity qualifiers for descriptor post-composition",
    )

class ClinicalBurdenLevelEnum(EnumDefinitionImpl):
    """
    Coarse disease-level assessment of the typical clinical burden imposed by a disease, considering functional
    impact, morbidity, duration, monitoring/treatment burden, and expected long-term consequences. This is distinct
    from phenotype-level severity.
    """
    LOW = PermissibleValue(
        text="LOW",
        title="Low",
        description="""Typical cases impose limited functional impact, morbidity, management burden, or long-term consequences.""")
    MODERATE = PermissibleValue(
        text="MODERATE",
        title="Moderate",
        description="""Typical cases impose clinically meaningful but not usually life-threatening or highly disabling burden.""")
    HIGH = PermissibleValue(
        text="HIGH",
        title="High",
        description="""Typical cases impose substantial morbidity, disability, intensive management needs, major long-term consequences, or mortality risk.""")
    VARIABLE = PermissibleValue(
        text="VARIABLE",
        title="Variable",
        description="""Clinical burden varies widely across patients, subtypes, stages, or contexts, and no single low/moderate/high level is representative.""")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        title="Unknown",
        description="The typical clinical burden is not established or has not been assessed.")

    _defn = EnumDefinition(
        name="ClinicalBurdenLevelEnum",
        description="""Coarse disease-level assessment of the typical clinical burden imposed by a disease, considering functional impact, morbidity, duration, monitoring/treatment burden, and expected long-term consequences. This is distinct from phenotype-level severity.""",
    )

class AssayTerm(EnumDefinitionImpl):
    """
    A term representing an assay
    """
    _defn = EnumDefinition(
        name="AssayTerm",
        description="A term representing an assay",
    )

class CellularComponentTerm(EnumDefinitionImpl):
    """
    A term representing a cellular component
    """
    _defn = EnumDefinition(
        name="CellularComponentTerm",
        description="A term representing a cellular component",
    )

class ProteinComplexTerm(EnumDefinitionImpl):
    """
    A term representing a protein complex
    """
    _defn = EnumDefinition(
        name="ProteinComplexTerm",
        description="A term representing a protein complex",
    )

class BiologicalProcessTerm(EnumDefinitionImpl):
    """
    A term representing a biological process or pathway
    """
    _defn = EnumDefinition(
        name="BiologicalProcessTerm",
        description="A term representing a biological process or pathway",
    )

class MolecularFunctionTerm(EnumDefinitionImpl):
    """
    A term representing a molecular function
    """
    _defn = EnumDefinition(
        name="MolecularFunctionTerm",
        description="A term representing a molecular function",
    )

class ChemicalEntityTerm(EnumDefinitionImpl):
    """
    A term representing a chemical entity
    """
    _defn = EnumDefinition(
        name="ChemicalEntityTerm",
        description="A term representing a chemical entity",
    )

class PhenotypeTerm(EnumDefinitionImpl):
    """
    A term representing a phenotype or disease manifestation
    """
    _defn = EnumDefinition(
        name="PhenotypeTerm",
        description="A term representing a phenotype or disease manifestation",
    )

class InheritanceTerm(EnumDefinitionImpl):
    """
    A term representing mode of inheritance
    """
    _defn = EnumDefinition(
        name="InheritanceTerm",
        description="A term representing mode of inheritance",
    )

class AnatomicalEntityTerm(EnumDefinitionImpl):
    """
    A term representing an anatomical entity
    """
    _defn = EnumDefinition(
        name="AnatomicalEntityTerm",
        description="A term representing an anatomical entity",
    )

class TreatmentActionTerm(EnumDefinitionImpl):
    """
    A term representing a medical action or treatment (from NCIT)
    """
    _defn = EnumDefinition(
        name="TreatmentActionTerm",
        description="A term representing a medical action or treatment (from NCIT)",
    )

class RegimenTerm(EnumDefinitionImpl):
    """
    A term representing a treatment regimen (from NCIT)
    """
    _defn = EnumDefinition(
        name="RegimenTerm",
        description="A term representing a treatment regimen (from NCIT)",
    )

class GeographyTerm(EnumDefinitionImpl):
    """
    A place or location
    """
    _defn = EnumDefinition(
        name="GeographyTerm",
        description="A place or location",
    )

class PhaseTerm(EnumDefinitionImpl):
    """
    A phase or stage
    """
    _defn = EnumDefinition(
        name="PhaseTerm",
        description="A phase or stage",
    )

class LifeCycleStageTerm(EnumDefinitionImpl):
    """
    A parasite life cycle stage term (from OPL)
    """
    _defn = EnumDefinition(
        name="LifeCycleStageTerm",
        description="A parasite life cycle stage term (from OPL)",
    )

class TriggerTerm(EnumDefinitionImpl):
    """
    A trigger
    """
    _defn = EnumDefinition(
        name="TriggerTerm",
        description="A trigger",
    )

class GeneTerm(EnumDefinitionImpl):
    """
    A gene term from HGNC
    """
    _defn = EnumDefinition(
        name="GeneTerm",
        description="A gene term from HGNC",
    )

class CellTypeTerm(EnumDefinitionImpl):
    """
    A cell type
    """
    _defn = EnumDefinition(
        name="CellTypeTerm",
        description="A cell type",
    )

class BiomarkerTerm(EnumDefinitionImpl):
    """
    A biomarker term from NCIT. Includes proteins, gene products, fusion products, and other molecular markers. No
    hierarchy constraint - validates term exists and label matches.
    """
    _defn = EnumDefinition(
        name="BiomarkerTerm",
        description="""A biomarker term from NCIT. Includes proteins, gene products, fusion products, and other molecular markers. No hierarchy constraint - validates term exists and label matches.""",
    )

class BiomarkerReadoutRelationshipEnum(EnumDefinitionImpl):
    """
    Relationship between a biomarker and the pathograph node it reports on
    """
    READOUT_OF = PermissibleValue(
        text="READOUT_OF",
        title="Readout of",
        description="The biomarker directly or indirectly measures the linked event or mechanism")
    CORRELATES_WITH = PermissibleValue(
        text="CORRELATES_WITH",
        title="Correlates with",
        description="The biomarker is statistically or clinically associated with the linked event or endpoint")
    PREDICTS = PermissibleValue(
        text="PREDICTS",
        title="Predicts",
        description="The biomarker predicts a later event, endpoint, or clinical outcome")
    PHARMACODYNAMIC_MARKER_OF = PermissibleValue(
        text="PHARMACODYNAMIC_MARKER_OF",
        title="Pharmacodynamic marker of",
        description="The biomarker reports biological response to a treatment or intervention at the linked node")

    _defn = EnumDefinition(
        name="BiomarkerReadoutRelationshipEnum",
        description="Relationship between a biomarker and the pathograph node it reports on",
    )

class BiomarkerReadoutDirectionEnum(EnumDefinitionImpl):
    """
    Direction of association between biomarker value/presence and the linked event or endpoint
    """
    POSITIVE = PermissibleValue(
        text="POSITIVE",
        title="Positive",
        description="Higher biomarker value or stronger presence tracks with more of the linked event")
    NEGATIVE = PermissibleValue(
        text="NEGATIVE",
        title="Negative",
        description="Higher biomarker value or stronger presence tracks with less of the linked event")
    PRESENT_ABSENT = PermissibleValue(
        text="PRESENT_ABSENT",
        title="Present/absent",
        description="Biomarker presence or absence, rather than monotonic level, is the interpretable signal")
    THRESHOLD_DEPENDENT = PermissibleValue(
        text="THRESHOLD_DEPENDENT",
        title="Threshold dependent",
        description="Interpretation depends on threshold, range, genotype, assay, or clinical context")

    _defn = EnumDefinition(
        name="BiomarkerReadoutDirectionEnum",
        description="Direction of association between biomarker value/presence and the linked event or endpoint",
    )

class BiomarkerEndpointContextEnum(EnumDefinitionImpl):
    """
    Endpoint or use context for a biomarker readout link
    """
    DIAGNOSTIC = PermissibleValue(
        text="DIAGNOSTIC",
        title="Diagnostic",
        description="Used to support diagnosis or disease classification")
    PROGNOSTIC = PermissibleValue(
        text="PROGNOSTIC",
        title="Prognostic",
        description="Associated with future risk, disease severity, or clinical outcome")
    MONITORING = PermissibleValue(
        text="MONITORING",
        title="Monitoring",
        description="Used to track disease state or progression over time")
    PHARMACODYNAMIC = PermissibleValue(
        text="PHARMACODYNAMIC",
        title="Pharmacodynamic",
        description="Used to track biological response to treatment or perturbation")
    CANDIDATE_SURROGATE = PermissibleValue(
        text="CANDIDATE_SURROGATE",
        title="Candidate surrogate",
        description="Potential surrogate endpoint candidate requiring explicit outcome-link evidence")

    _defn = EnumDefinition(
        name="BiomarkerEndpointContextEnum",
        description="Endpoint or use context for a biomarker readout link",
    )

class SurrogateEndpointTableEnum(EnumDefinitionImpl):
    """
    FDA surrogate endpoint table section from which a row was curated
    """
    ADULT_NONCANCER = PermissibleValue(
        text="ADULT_NONCANCER",
        title="Adult non-cancer related",
        description="Adult Surrogate Endpoints - Non-cancer Related")
    ADULT_CANCER = PermissibleValue(
        text="ADULT_CANCER",
        title="Adult cancer related",
        description="Adult Surrogate Endpoints - Cancer Related")
    PEDIATRIC_NONCANCER = PermissibleValue(
        text="PEDIATRIC_NONCANCER",
        title="Pediatric non-cancer related",
        description="Pediatric Surrogate Endpoints - Non-cancer Related")
    PEDIATRIC_CANCER = PermissibleValue(
        text="PEDIATRIC_CANCER",
        title="Pediatric cancer related",
        description="Pediatric Surrogate Endpoints - Cancer Related")

    _defn = EnumDefinition(
        name="SurrogateEndpointTableEnum",
        description="FDA surrogate endpoint table section from which a row was curated",
    )

class SurrogateEndpointApprovalTypeEnum(EnumDefinitionImpl):
    """
    Regulatory approval pathway context represented in the FDA surrogate endpoint table
    """
    ACCELERATED = PermissibleValue(
        text="ACCELERATED",
        title="Accelerated",
        description="Endpoint may support accelerated approval in the curated context")
    TRADITIONAL = PermissibleValue(
        text="TRADITIONAL",
        title="Traditional",
        description="Endpoint may support traditional approval in the curated context")
    ACCELERATED_OR_TRADITIONAL = PermissibleValue(
        text="ACCELERATED_OR_TRADITIONAL",
        title="Accelerated or traditional",
        description="Endpoint may support accelerated or traditional approval depending on context of use")
    TRADITIONAL_AND_MONOGRAPH = PermissibleValue(
        text="TRADITIONAL_AND_MONOGRAPH",
        title="Traditional and monograph",
        description="Endpoint appears in FDA table as traditional and monograph")

    _defn = EnumDefinition(
        name="SurrogateEndpointApprovalTypeEnum",
        description="Regulatory approval pathway context represented in the FDA surrogate endpoint table",
    )

class SurrogateEndpointValidationLevelEnum(EnumDefinitionImpl):
    """
    BEST-aligned regulatory validation level inferred or curated for a surrogate endpoint
    """
    VALIDATED_SURROGATE_ENDPOINT = PermissibleValue(
        text="VALIDATED_SURROGATE_ENDPOINT",
        title="Validated surrogate endpoint",
        description="""Supported by clinical data providing strong evidence that the endpoint predicts clinical benefit""")
    REASONABLY_LIKELY_SURROGATE_ENDPOINT = PermissibleValue(
        text="REASONABLY_LIKELY_SURROGATE_ENDPOINT",
        title="Reasonably likely surrogate endpoint",
        description="""Supported by strong mechanistic and/or epidemiologic rationale, but without sufficient clinical validation for full surrogate validation""")
    CONTEXT_DEPENDENT_SURROGATE_ENDPOINT = PermissibleValue(
        text="CONTEXT_DEPENDENT_SURROGATE_ENDPOINT",
        title="Context-dependent surrogate endpoint",
        description="""Validation and approval pathway depend on context of use, disease setting, effect size, duration, residual uncertainty, and available therapy""")

    _defn = EnumDefinition(
        name="SurrogateEndpointValidationLevelEnum",
        description="BEST-aligned regulatory validation level inferred or curated for a surrogate endpoint",
    )

class ClinicalBenefitLinkageEnum(EnumDefinitionImpl):
    """
    How a surrogate endpoint is linked to clinical benefit in the regulatory context
    """
    KNOWN_TO_PREDICT_CLINICAL_BENEFIT = PermissibleValue(
        text="KNOWN_TO_PREDICT_CLINICAL_BENEFIT",
        title="Known to predict clinical benefit",
        description="""FDA table approval context indicates the endpoint is known to predict clinical benefit for the curated context""")
    REASONABLY_LIKELY_TO_PREDICT_CLINICAL_BENEFIT = PermissibleValue(
        text="REASONABLY_LIKELY_TO_PREDICT_CLINICAL_BENEFIT",
        title="Reasonably likely to predict clinical benefit",
        description="""FDA table approval context indicates the endpoint is reasonably likely to predict clinical benefit""")
    CONTEXT_DEPENDENT = PermissibleValue(
        text="CONTEXT_DEPENDENT",
        title="Context dependent",
        description="Clinical-benefit linkage depends on context of use and approval pathway")

    _defn = EnumDefinition(
        name="ClinicalBenefitLinkageEnum",
        description="How a surrogate endpoint is linked to clinical benefit in the regulatory context",
    )

class SurrogateEndpointFootnoteEnum(EnumDefinitionImpl):
    """
    Footnotes and symbols used in the FDA surrogate endpoint workbook
    """
    COMPOSITE_BIOMARKER_SURROGATE = PermissibleValue(
        text="COMPOSITE_BIOMARKER_SURROGATE",
        title="Composite biomarker surrogate",
        description="Surrogate endpoint is part of a composite of biomarker surrogate endpoints")
    MECHANISM_AGNOSTIC = PermissibleValue(
        text="MECHANISM_AGNOSTIC",
        title="Mechanism agnostic",
        description="""Many mechanisms of action are associated with the surrogate endpoint, so it is not directly related to a particular causal pathway""")
    TUMOR_BURDEN_CONTEXT_DEPENDENT = PermissibleValue(
        text="TUMOR_BURDEN_CONTEXT_DEPENDENT",
        title="Tumor burden context dependent",
        description="""Tumor-burden endpoints may support accelerated or traditional approval depending on context of use""")
    ANTICIPATED_PRIMARY_EFFICACY_USE = PermissibleValue(
        text="ANTICIPATED_PRIMARY_EFFICACY_USE",
        title="Anticipated primary efficacy use",
        description="""FDA anticipates the endpoint could be appropriate as a primary efficacy endpoint although it has not yet supported an approved NDA or BLA""")
    BONE_MINERAL_DENSITY_CONTEXT = PermissibleValue(
        text="BONE_MINERAL_DENSITY_CONTEXT",
        title="Bone mineral density context",
        description="Bone mineral density footnote for male or glucocorticoid-induced osteoporosis contexts")
    CLINICAL_ENDPOINTS_REQUIRED = PermissibleValue(
        text="CLINICAL_ENDPOINTS_REQUIRED",
        title="Clinical endpoints required",
        description="Clinical endpoints were required for the approvals")
    ARRHYTHMIA_RESPONSE_DEFINITION = PermissibleValue(
        text="ARRHYTHMIA_RESPONSE_DEFINITION",
        title="Arrhythmia response definition",
        description="Specialized response definition footnote for supraventricular tachycardia endpoint")

    _defn = EnumDefinition(
        name="SurrogateEndpointFootnoteEnum",
        description="Footnotes and symbols used in the FDA surrogate endpoint workbook",
    )

class SurrogateEndpointMappingStatusEnum(EnumDefinitionImpl):
    """
    Status of mapping an FDA disease/use row to dismech disease entries
    """
    EXACT_DISMECH_MATCH = PermissibleValue(
        text="EXACT_DISMECH_MATCH",
        title="Exact dismech match",
        description="FDA disease/use maps directly to an existing dismech disease entry")
    CURATED_DISMECH_MAPPING = PermissibleValue(
        text="CURATED_DISMECH_MAPPING",
        title="Curated dismech mapping",
        description="Mapping was manually curated despite non-identical labels")
    CANDIDATE_DISMECH_MAPPING = PermissibleValue(
        text="CANDIDATE_DISMECH_MAPPING",
        title="Candidate dismech mapping",
        description="""Row mentions a disease represented in dismech but the FDA disease/use row is broader, multi-condition, or otherwise requires review""")
    NEEDS_CURATION = PermissibleValue(
        text="NEEDS_CURATION",
        title="Needs curation",
        description="No dismech disease mapping has been assigned yet")
    NOT_DISEASE_SPECIFIC = PermissibleValue(
        text="NOT_DISEASE_SPECIFIC",
        title="Not disease specific",
        description="""FDA row is a use, vaccine, or broad product context rather than a directly mappable disease entry""")

    _defn = EnumDefinition(
        name="SurrogateEndpointMappingStatusEnum",
        description="Status of mapping an FDA disease/use row to dismech disease entries",
    )

class GeneProductTerm(EnumDefinitionImpl):
    """
    A gene product term from NCIT. Includes proteins, fusion proteins, oncoproteins, and other gene products involved
    in disease mechanisms.
    """
    _defn = EnumDefinition(
        name="GeneProductTerm",
        description="""A gene product term from NCIT. Includes proteins, fusion proteins, oncoproteins, and other gene products involved in disease mechanisms.""",
    )

class HistopathologyFindingTerm(EnumDefinitionImpl):
    """
    A histopathologic finding term from NCIT. Covers the full NCIT Histopathology Result branch (NCIT:C83490):
    morphologic findings, architectural/growth patterns, cellular features, grading, immunophenotype (IHC/flow
    markers), ultrastructure, and staining intensity.
    """
    _defn = EnumDefinition(
        name="HistopathologyFindingTerm",
        description="""A histopathologic finding term from NCIT. Covers the full NCIT Histopathology Result branch (NCIT:C83490): morphologic findings, architectural/growth patterns, cellular features, grading, immunophenotype (IHC/flow markers), ultrastructure, and staining intensity.""",
    )

class ImagingFindingTerm(EnumDefinitionImpl):
    """
    An in-vivo imaging finding term. Imaging findings are drawn from the NCIT Imaging Finding branch (NCIT:C176708 /
    NCIT:C199145) and, because most radiologic observations coincide with a described phenotype, from the HP
    Phenotypic abnormality branch (HP:0000118) - e.g. white-matter lesions, atrophy, hyperintensity. Binding is
    RECOMMENDED (not REQUIRED): many specific radiologic appearances lack a dedicated NCIT/HP term and are left to
    preferred_term until a radiology ontology (e.g. RadLex via BioPortal) is wired in.
    """
    _defn = EnumDefinition(
        name="ImagingFindingTerm",
        description="""An in-vivo imaging finding term. Imaging findings are drawn from the NCIT Imaging Finding branch (NCIT:C176708 / NCIT:C199145) and, because most radiologic observations coincide with a described phenotype, from the HP Phenotypic abnormality branch (HP:0000118) - e.g. white-matter lesions, atrophy, hyperintensity. Binding is RECOMMENDED (not REQUIRED): many specific radiologic appearances lack a dedicated NCIT/HP term and are left to preferred_term until a radiology ontology (e.g. RadLex via BioPortal) is wired in.""",
    )

class DiseaseTerm(EnumDefinitionImpl):
    """
    A MONDO disease, inherited disease susceptibility, or related medical condition term used to anchor a curated
    disorder entry
    """
    _defn = EnumDefinition(
        name="DiseaseTerm",
        description="""A MONDO disease, inherited disease susceptibility, or related medical condition term used to anchor a curated disorder entry""",
    )

class NCITDiseaseOrFindingTerm(EnumDefinitionImpl):
    """
    An NCIT disease-oriented oncology term used for disease-level cancer mappings and subtype grounding, including
    neoplasm-by-morphology, special-category neoplasm, and clinically used disease/finding boundary concepts.
    """
    _defn = EnumDefinition(
        name="NCITDiseaseOrFindingTerm",
        description="""An NCIT disease-oriented oncology term used for disease-level cancer mappings and subtype grounding, including neoplasm-by-morphology, special-category neoplasm, and clinically used disease/finding boundary concepts.""",
    )

class DiseaseOrSubtypeTerm(EnumDefinitionImpl):
    """
    A MONDO disease term or NCIT cancer disease/subtype term used to ground a disease subtype or cancer facet value.
    """
    _defn = EnumDefinition(
        name="DiseaseOrSubtypeTerm",
        description="""A MONDO disease term or NCIT cancer disease/subtype term used to ground a disease subtype or cancer facet value.""",
    )

class ICD10CMTerm(EnumDefinitionImpl):
    """
    An ICD-10-CM diagnosis code
    """
    _defn = EnumDefinition(
        name="ICD10CMTerm",
        description="An ICD-10-CM diagnosis code",
    )

class ICD11FTerm(EnumDefinitionImpl):
    """
    An ICD-11 Foundation diagnosis code
    """
    _defn = EnumDefinition(
        name="ICD11FTerm",
        description="An ICD-11 Foundation diagnosis code",
    )

class ExposureTerm(EnumDefinitionImpl):
    """
    A term representing an exposure event (from ECTO or XCO)
    """
    _defn = EnumDefinition(
        name="ExposureTerm",
        description="A term representing an exposure event (from ECTO or XCO)",
    )

class EnvironmentTerm(EnumDefinitionImpl):
    """
    A term representing an environmental context, material, or feature (from ENVO)
    """
    _defn = EnumDefinition(
        name="EnvironmentTerm",
        description="A term representing an environmental context, material, or feature (from ENVO)",
    )

class FoodTerm(EnumDefinitionImpl):
    """
    A term representing a food, beverage, nutrient, mineral, or supplement source (from FOODON or CHEBI)
    """
    _defn = EnumDefinition(
        name="FoodTerm",
        description="A term representing a food, beverage, nutrient, mineral, or supplement source (from FOODON or CHEBI)",
    )

class OrganismTerm(EnumDefinitionImpl):
    """
    A term representing an organism from NCBITaxon
    """
    _defn = EnumDefinition(
        name="OrganismTerm",
        description="A term representing an organism from NCBITaxon",
    )

class OnsetEnum(EnumDefinitionImpl):
    """
    Age of onset categories from HPO
    """
    ANTENATAL = PermissibleValue(
        text="ANTENATAL",
        description="Antenatal onset",
        meaning=HP["0030674"])
    EMBRYONAL = PermissibleValue(
        text="EMBRYONAL",
        description="Embryonal onset",
        meaning=HP["0011460"])
    FETAL = PermissibleValue(
        text="FETAL",
        description="Fetal onset",
        meaning=HP["0011461"])
    CONGENITAL = PermissibleValue(
        text="CONGENITAL",
        description="Congenital onset",
        meaning=HP["0003577"])
    NEONATAL = PermissibleValue(
        text="NEONATAL",
        description="Neonatal onset",
        meaning=HP["0003623"])
    INFANTILE = PermissibleValue(
        text="INFANTILE",
        description="Infantile onset",
        meaning=HP["0003593"])
    CHILDHOOD = PermissibleValue(
        text="CHILDHOOD",
        description="Childhood onset",
        meaning=HP["0011463"])
    JUVENILE = PermissibleValue(
        text="JUVENILE",
        description="Juvenile onset",
        meaning=HP["0003621"])
    ADULT = PermissibleValue(
        text="ADULT",
        description="Adult onset",
        meaning=HP["0003581"])
    YOUNG_ADULT = PermissibleValue(
        text="YOUNG_ADULT",
        description="Young adult onset",
        meaning=HP["0011462"])
    MIDDLE_AGE = PermissibleValue(
        text="MIDDLE_AGE",
        description="Middle age onset",
        meaning=HP["0003596"])
    LATE = PermissibleValue(
        text="LATE",
        description="Late onset",
        meaning=HP["0003584"])
    PUERPERAL = PermissibleValue(
        text="PUERPERAL",
        description="Puerperal onset",
        meaning=HP["4000040"])

    _defn = EnumDefinition(
        name="OnsetEnum",
        description="Age of onset categories from HPO",
    )

class ZygosityEnum(EnumDefinitionImpl):
    """
    Zygosity categories from GENO
    """
    HETEROZYGOUS = PermissibleValue(
        text="HETEROZYGOUS",
        description="Heterozygous",
        meaning=GENO["0000135"])
    SIMPLE_HETEROZYGOUS = PermissibleValue(
        text="SIMPLE_HETEROZYGOUS",
        description="Simple heterozygous",
        meaning=GENO["0000458"])
    COMPOUND_HETEROZYGOUS = PermissibleValue(
        text="COMPOUND_HETEROZYGOUS",
        description="Compound heterozygous",
        meaning=GENO["0000402"])
    HOMOZYGOUS = PermissibleValue(
        text="HOMOZYGOUS",
        description="Homozygous",
        meaning=GENO["0000136"])
    HEMIZYGOUS = PermissibleValue(
        text="HEMIZYGOUS",
        description="Hemizygous",
        meaning=GENO["0000134"])

    _defn = EnumDefinition(
        name="ZygosityEnum",
        description="Zygosity categories from GENO",
    )

class DatasetTypeEnum(EnumDefinitionImpl):
    """
    Type of dataset or data resource
    """
    MICROARRAY = PermissibleValue(
        text="MICROARRAY",
        description="Gene expression microarray")
    BULK_RNA_SEQ = PermissibleValue(
        text="BULK_RNA_SEQ",
        description="Bulk RNA sequencing")
    SINGLE_CELL_RNA_SEQ = PermissibleValue(
        text="SINGLE_CELL_RNA_SEQ",
        description="Single-cell RNA sequencing")
    SPATIAL_TRANSCRIPTOMICS = PermissibleValue(
        text="SPATIAL_TRANSCRIPTOMICS",
        description="Spatially resolved transcriptomics")
    METHYLATION = PermissibleValue(
        text="METHYLATION",
        description="DNA methylation profiling")
    CHIP_SEQ = PermissibleValue(
        text="CHIP_SEQ",
        description="Chromatin immunoprecipitation sequencing")
    ATAC_SEQ = PermissibleValue(
        text="ATAC_SEQ",
        description="Assay for transposase-accessible chromatin sequencing")
    PROTEOMICS = PermissibleValue(
        text="PROTEOMICS",
        description="Protein expression profiling")
    METABOLOMICS = PermissibleValue(
        text="METABOLOMICS",
        description="Metabolite profiling")
    GWAS = PermissibleValue(
        text="GWAS",
        description="Genome-wide association study")
    WGS = PermissibleValue(
        text="WGS",
        description="Whole genome sequencing")
    WES = PermissibleValue(
        text="WES",
        description="Whole exome sequencing")
    PHENOPACKETS = PermissibleValue(
        text="PHENOPACKETS",
        description="GA4GH Phenopacket collection (case-level phenotype data)")
    VARIANT_DATABASE = PermissibleValue(
        text="VARIANT_DATABASE",
        description="Curated genetic variant collection")
    MULTI_OMICS = PermissibleValue(
        text="MULTI_OMICS",
        description="Integrated multi-omics profiling (e.g., combined transcriptomics, proteomics, metabolomics)")
    MULTI_OMICS_PERTURBATION = PermissibleValue(
        text="MULTI_OMICS_PERTURBATION",
        description="""Multi-omics profiling of genetic perturbations (e.g., CRISPR knockout combined with transcriptomic, chromatin accessibility, and cellular phenotyping)""")

    _defn = EnumDefinition(
        name="DatasetTypeEnum",
        description="Type of dataset or data resource",
    )

class ExperimentalModelTypeEnum(EnumDefinitionImpl):
    """
    Broad disease-centric categories for experimental model systems, primarily non-animal systems curated in this
    section
    """
    ORGANOID = PermissibleValue(
        text="ORGANOID",
        description="Self-organizing three-dimensional tissue model, often stem-cell-derived")
    ORGAN_ON_CHIP = PermissibleValue(
        text="ORGAN_ON_CHIP",
        description="Microfluidic organ- or tissue-on-chip model")
    CELL_LINE = PermissibleValue(
        text="CELL_LINE",
        description="Immortalized cell line-based disease model")
    IPSC_DERIVED_MODEL = PermissibleValue(
        text="IPSC_DERIVED_MODEL",
        description="Differentiated model derived from induced pluripotent stem cells")
    PRIMARY_CELL_CULTURE = PermissibleValue(
        text="PRIMARY_CELL_CULTURE",
        description="Primary-cell or biopsy-derived culture system, including monolayers")
    CO_CULTURE = PermissibleValue(
        text="CO_CULTURE",
        description="Host-microbe or multi-cell-type coculture system")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Other experimental model type not covered above")

    _defn = EnumDefinition(
        name="ExperimentalModelTypeEnum",
        description="""Broad disease-centric categories for experimental model systems, primarily non-animal systems curated in this section""",
    )

class ModelMechanismRelationshipEnum(EnumDefinitionImpl):
    """
    Controlled relationship between an experimental, animal, or computational model and the pathophysiology node it is
    linked to. Distinguishes a model that reproduces a mechanism from one that merely manipulates or measures it, and
    gives negative results (a model that does NOT reproduce the human mechanism) a first-class home rather than
    leaving them in prose.
    """
    RECAPITULATES = PermissibleValue(
        text="RECAPITULATES",
        title="Recapitulates",
        description="""The model reproduces the linked mechanism, such that observations in the model are taken to be informative about the human mechanism.""")
    PARTIALLY_RECAPITULATES = PermissibleValue(
        text="PARTIALLY_RECAPITULATES",
        title="Partially recapitulates",
        description="""The model reproduces some but not all of the linked mechanism. Use `limitations` to state which facets are and are not reproduced.""")
    FAILS_TO_RECAPITULATE = PermissibleValue(
        text="FAILS_TO_RECAPITULATE",
        title="Fails to recapitulate",
        description="""The model does NOT reproduce the linked mechanism. This is a substantive negative claim and the structural signal for a HUMAN_MODEL_MISMATCH discussion; it requires `limitations` and supporting `evidence`.""")
    PERTURBS = PermissibleValue(
        text="PERTURBS",
        title="Perturbs",
        description="""The model manipulates the linked mechanism (knockout, knockdown, overexpression, chemical challenge) without itself being a claim that the full mechanism is reproduced.""")
    MEASURES = PermissibleValue(
        text="MEASURES",
        title="Measures",
        description="""The model provides a readout of the linked mechanism without claiming to reproduce or perturb it.""")
    RESCUES = PermissibleValue(
        text="RESCUES",
        title="Rescues",
        description="""The model demonstrates reversal or correction of the linked mechanism, typically a genetic-correction, drug-rescue, or isogenic-repair arm.""")

    _defn = EnumDefinition(
        name="ModelMechanismRelationshipEnum",
        description="""Controlled relationship between an experimental, animal, or computational model and the pathophysiology node it is linked to. Distinguishes a model that reproduces a mechanism from one that merely manipulates or measures it, and gives negative results (a model that does NOT reproduce the human mechanism) a first-class home rather than leaving them in prose.""",
    )

class ModelFidelityEnum(EnumDefinitionImpl):
    """
    Curator assessment of how faithfully a model captures the linked human mechanism. Deliberately coarse: this is a
    translational-validity caveat, not a metric. Pair with `limitations` for the specific caveat.
    """
    HIGH = PermissibleValue(
        text="HIGH",
        title="High",
        description="""Human-derived or otherwise closely matched system reproducing the mechanism with well-characterized correspondence to human disease.""")
    MODERATE = PermissibleValue(
        text="MODERATE",
        title="Moderate",
        description="""Reproduces the mechanism with known and material divergences from human biology (species differences, supraphysiological expression, reduced cellular complexity).""")
    LOW = PermissibleValue(
        text="LOW",
        title="Low",
        description="""Informative but with divergences substantial enough that findings should not be transferred to human disease without corroboration.""")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        title="Unknown",
        description="""Correspondence to the human mechanism has not been established. Prefer this over guessing a tier.""")

    _defn = EnumDefinition(
        name="ModelFidelityEnum",
        description="""Curator assessment of how faithfully a model captures the linked human mechanism. Deliberately coarse: this is a translational-validity caveat, not a metric. Pair with `limitations` for the specific caveat.""",
    )

class ModelReadoutDirectionEnum(EnumDefinitionImpl):
    """
    Direction of a measured effect in an experimental, animal, or computational model, relative to the model's control
    or comparator arm. Complements BiomarkerReadoutDirectionEnum, which describes the direction of a clinical
    biomarker's *association* with an endpoint rather than the direction of an experimental measurement.
    """
    INCREASED = PermissibleValue(
        text="INCREASED",
        title="Increased",
        description="The readout is higher in the model condition than in the comparator")
    DECREASED = PermissibleValue(
        text="DECREASED",
        title="Decreased",
        description="The readout is lower in the model condition than in the comparator")
    UNCHANGED = PermissibleValue(
        text="UNCHANGED",
        title="Unchanged",
        description="""The readout does not differ materially from the comparator. A genuine negative result, not missing data; omit `direction` entirely when the measurement was not made or not reported.""")
    RESTORED = PermissibleValue(
        text="RESTORED",
        title="Restored",
        description="""The readout returns toward the comparator/wild-type value, typically in a rescue, correction, or treatment arm.""")
    ABOLISHED = PermissibleValue(
        text="ABOLISHED",
        title="Abolished",
        description="The readout is lost or reduced to background in the model condition")
    ALTERED = PermissibleValue(
        text="ALTERED",
        title="Altered",
        description="""The readout differs from the comparator in a way that is not monotonic (e.g. a shifted distribution or changed kinetics). Prefer a directional value when one applies.""")

    _defn = EnumDefinition(
        name="ModelReadoutDirectionEnum",
        description="""Direction of a measured effect in an experimental, animal, or computational model, relative to the model's control or comparator arm. Complements BiomarkerReadoutDirectionEnum, which describes the direction of a clinical biomarker's *association* with an endpoint rather than the direction of an experimental measurement.""",
    )

class CurationActionEnum(EnumDefinitionImpl):
    """
    Simple action types for curation audit trail
    """
    CREATED = PermissibleValue(
        text="CREATED",
        description="Initial file creation")
    EDITED = PermissibleValue(
        text="EDITED",
        description="File modification")

    _defn = EnumDefinition(
        name="CurationActionEnum",
        description="Simple action types for curation audit trail",
    )

class ClinicalTrialPhaseEnum(EnumDefinitionImpl):
    """
    Clinical trial phase categories per FDA/NIH standards
    """
    PHASE_I = PermissibleValue(
        text="PHASE_I",
        description="Phase I - Initial safety and dosage assessment in small group (20-100 participants)")
    PHASE_II = PermissibleValue(
        text="PHASE_II",
        description="Phase II - Efficacy and side effects assessment in larger group (100-500 participants)")
    PHASE_III = PermissibleValue(
        text="PHASE_III",
        description="Phase III - Efficacy confirmation and monitoring in large population (1000-5000 participants)")
    PHASE_IV = PermissibleValue(
        text="PHASE_IV",
        description="Phase IV - Post-market surveillance and additional benefits/risks studies")
    NOT_APPLICABLE = PermissibleValue(
        text="NOT_APPLICABLE",
        description="Trial does not follow standard FDA phase classification (e.g., observational, device studies)")

    _defn = EnumDefinition(
        name="ClinicalTrialPhaseEnum",
        description="Clinical trial phase categories per FDA/NIH standards",
    )

class ClinicalTrialStatusEnum(EnumDefinitionImpl):
    """
    Clinical trial recruitment and status categories per ClinicalTrials.gov
    """
    RECRUITING = PermissibleValue(
        text="RECRUITING",
        description="Currently enrolling participants")
    NOT_RECRUITING = PermissibleValue(
        text="NOT_RECRUITING",
        description="Not currently enrolling but may in the future")
    ACTIVE_NOT_RECRUITING = PermissibleValue(
        text="ACTIVE_NOT_RECRUITING",
        description="Actively recruiting previously enrolled participants (closed to new enrollment)")
    COMPLETED = PermissibleValue(
        text="COMPLETED",
        description="Trial data collection and analysis completed")
    ENROLLING_BY_INVITATION = PermissibleValue(
        text="ENROLLING_BY_INVITATION",
        description="Enrollment restricted to invited participants only")
    SUSPENDED = PermissibleValue(
        text="SUSPENDED",
        description="Temporarily halted pending review or administrative action")
    TERMINATED = PermissibleValue(
        text="TERMINATED",
        description="Stopped before completion, may include safety or efficacy concerns")
    WITHDRAWN = PermissibleValue(
        text="WITHDRAWN",
        description="Closed before enrollment began (never enrolled participants)")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="Status unknown or not provided")

    _defn = EnumDefinition(
        name="ClinicalTrialStatusEnum",
        description="Clinical trial recruitment and status categories per ClinicalTrials.gov",
    )

class ComputationalModelTypeEnum(EnumDefinitionImpl):
    """
    Type of computational or in-silico model
    """
    GENOME_SCALE_METABOLIC = PermissibleValue(
        text="GENOME_SCALE_METABOLIC",
        description="Genome-scale metabolic reconstruction (e.g., Recon3D, Harvey)")
    FLUX_BALANCE_ANALYSIS = PermissibleValue(
        text="FLUX_BALANCE_ANALYSIS",
        description="Constraint-based FBA model")
    KINETIC = PermissibleValue(
        text="KINETIC",
        description="ODE-based kinetic model with rate equations")
    AGENT_BASED = PermissibleValue(
        text="AGENT_BASED",
        description="Agent-based simulation model")
    BOOLEAN_NETWORK = PermissibleValue(
        text="BOOLEAN_NETWORK",
        description="Boolean gene regulatory network")
    PHYSIOLOGICAL = PermissibleValue(
        text="PHYSIOLOGICAL",
        description="Physiologically-based pharmacokinetic (PBPK) or organ model")
    DIGITAL_TWIN = PermissibleValue(
        text="DIGITAL_TWIN",
        description="Patient-specific computational model")
    MACHINE_LEARNING = PermissibleValue(
        text="MACHINE_LEARNING",
        description="ML/AI predictive model trained on disease data")
    PERTURBATION_PREDICTION = PermissibleValue(
        text="PERTURBATION_PREDICTION",
        description="""Cell-based perturbation models (CRISPR screens, chemical perturbations) with gene expression readouts""")
    FOUNDATION_MODEL = PermissibleValue(
        text="FOUNDATION_MODEL",
        description="""Pre-trained single-cell foundation models (scGPT, Geneformer, scGenePT) for perturbation response prediction""")
    STRUCTURAL_PREDICTION = PermissibleValue(
        text="STRUCTURAL_PREDICTION",
        description="""Protein structure prediction (AlphaFold, RoseTTAFold) or experimental structure (PDB X-ray, cryo-EM) used to understand disease mechanisms""")
    MOLECULAR_DOCKING = PermissibleValue(
        text="MOLECULAR_DOCKING",
        description="""Computational docking or molecular dynamics simulation of drug candidates to protein targets, typically informed by PDB/AlphaFold structures""")

    _defn = EnumDefinition(
        name="ComputationalModelTypeEnum",
        description="Type of computational or in-silico model",
    )

class ThresholdDirectionEnum(EnumDefinitionImpl):
    """
    Whether a threshold activates when the variable goes above or below the value
    """
    above = PermissibleValue(
        text="above",
        description="Activates when the variable exceeds the threshold")
    below = PermissibleValue(
        text="below",
        description="Activates when the variable falls below the threshold")

    _defn = EnumDefinition(
        name="ThresholdDirectionEnum",
        description="Whether a threshold activates when the variable goes above or below the value",
    )

class AbnormalFlagEnum(EnumDefinitionImpl):
    """
    Categorical interpretation flag for a clinical laboratory result band, aligned with HL7 v2 / LOINC abnormal-flag
    conventions.
    """
    NORMAL = PermissibleValue(
        text="NORMAL",
        description="Result within the reference interval (HL7 \"N\")")
    LOW = PermissibleValue(
        text="LOW",
        description="Result below the reference interval (HL7 \"L\")")
    HIGH = PermissibleValue(
        text="HIGH",
        description="Result above the reference interval (HL7 \"H\")")
    CRITICAL_LOW = PermissibleValue(
        text="CRITICAL_LOW",
        description="Critically (panic) low result requiring urgent action (HL7 \"LL\")")
    CRITICAL_HIGH = PermissibleValue(
        text="CRITICAL_HIGH",
        description="Critically (panic) high result requiring urgent action (HL7 \"HH\")")

    _defn = EnumDefinition(
        name="AbnormalFlagEnum",
        description="""Categorical interpretation flag for a clinical laboratory result band, aligned with HL7 v2 / LOINC abnormal-flag conventions.""",
    )

class CausalLinkTypeEnum(EnumDefinitionImpl):
    """
    Degree of mechanistic directness represented by a causal edge
    """
    DIRECT = PermissibleValue(
        text="DIRECT",
        description="Direct causal influence at the current graph granularity")
    INDIRECT_KNOWN_INTERMEDIATES = PermissibleValue(
        text="INDIRECT_KNOWN_INTERMEDIATES",
        description="Indirect relationship where one or more intermediates are known but omitted from the graph")
    INDIRECT_UNKNOWN_INTERMEDIATES = PermissibleValue(
        text="INDIRECT_UNKNOWN_INTERMEDIATES",
        description="Indirect relationship where at least one required intermediate mechanism is currently unknown")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="Directness has not yet been determined")

    _defn = EnumDefinition(
        name="CausalLinkTypeEnum",
        description="Degree of mechanistic directness represented by a causal edge",
    )

class TreatmentEffectEnum(EnumDefinitionImpl):
    """
    How a treatment affects a pathophysiology mechanism node
    """
    INHIBITS = PermissibleValue(
        text="INHIBITS",
        description="Blocks or decreases the mechanism (e.g., TKI inhibiting constitutive kinase activity)")
    ACTIVATES = PermissibleValue(
        text="ACTIVATES",
        description="Promotes or increases the mechanism (e.g., enzyme replacement restoring a deficient pathway)")
    MODULATES = PermissibleValue(
        text="MODULATES",
        description="Alters the mechanism without clear unidirectional effect")
    BYPASSES = PermissibleValue(
        text="BYPASSES",
        description="Works around the disrupted mechanism via an alternative pathway")
    RESTORES = PermissibleValue(
        text="RESTORES",
        description="Restores normal function of a disrupted mechanism (e.g., gene therapy, enzyme replacement)")

    _defn = EnumDefinition(
        name="TreatmentEffectEnum",
        description="How a treatment affects a pathophysiology mechanism node",
    )

class EnvironmentalEffectEnum(EnumDefinitionImpl):
    """
    How an environmental factor or exposure acts on a pathophysiology mechanism node. The environmental analogue of
    TreatmentEffectEnum, used to keep causative, aggravating, and protective exposures visually and semantically
    distinct in the pathograph.
    """
    TRIGGERS = PermissibleValue(
        text="TRIGGERS",
        title="Triggers",
        description="""The exposure initiates the mechanism, which would not otherwise occur in its absence (e.g., inorganic arsenic ingestion initiating systemic arsenic exposure; allergen contact initiating sensitization).""")
    EXACERBATES = PermissibleValue(
        text="EXACERBATES",
        title="Exacerbates",
        description="""The exposure worsens or amplifies a mechanism that is already present or can arise independently (e.g., tobacco smoke amplifying airway inflammation).""")
    PREDISPOSES = PermissibleValue(
        text="PREDISPOSES",
        title="Predisposes",
        description="""The exposure increases susceptibility to the mechanism without being sufficient to produce it (e.g., a risk-factor exposure that requires additional genetic or environmental hits).""")
    PROTECTS_AGAINST = PermissibleValue(
        text="PROTECTS_AGAINST",
        title="Protects against",
        description="""The exposure reduces the occurrence or severity of the mechanism (e.g., early-life microbial exposure and allergic sensitization).""")
    MODULATES = PermissibleValue(
        text="MODULATES",
        title="Modulates",
        description="""The exposure alters the mechanism without a clear unidirectional effect, or the direction is context dependent.""")

    _defn = EnumDefinition(
        name="EnvironmentalEffectEnum",
        description="""How an environmental factor or exposure acts on a pathophysiology mechanism node. The environmental analogue of TreatmentEffectEnum, used to keep causative, aggravating, and protective exposures visually and semantically distinct in the pathograph.""",
    )

class ImagingModalityEnum(EnumDefinitionImpl):
    """
    In-vivo medical imaging modality by which an ImagingFinding is detected. Meanings bind to the NCI Thesaurus
    Diagnostic Imaging branch.
    """
    MRI = PermissibleValue(
        text="MRI",
        title="Magnetic Resonance Imaging",
        description="Magnetic resonance imaging, including structural and contrast-enhanced MRI",
        meaning=NCIT["C16809"])
    FUNCTIONAL_MRI = PermissibleValue(
        text="FUNCTIONAL_MRI",
        title="Functional Magnetic Resonance Imaging",
        description="Blood-oxygen-level-dependent functional MRI",
        meaning=NCIT["C17958"])
    CT = PermissibleValue(
        text="CT",
        title="Computed Tomography",
        description="X-ray computed tomography",
        meaning=NCIT["C17204"])
    PET = PermissibleValue(
        text="PET",
        title="Positron Emission Tomography",
        description="Positron emission tomography (e.g., FDG-PET, amyloid-PET)",
        meaning=NCIT["C17007"])
    SPECT = PermissibleValue(
        text="SPECT",
        title="Single Photon Emission Computed Tomography",
        description="Single-photon emission computed tomography",
        meaning=NCIT["C17203"])
    ULTRASOUND = PermissibleValue(
        text="ULTRASOUND",
        title="Ultrasound Imaging",
        description="Diagnostic ultrasonography, including Doppler and echocardiography",
        meaning=NCIT["C17230"])
    XRAY = PermissibleValue(
        text="XRAY",
        title="X-Ray Imaging",
        description="Projectional radiography (plain film)",
        meaning=NCIT["C38101"])
    MAMMOGRAPHY = PermissibleValue(
        text="MAMMOGRAPHY",
        title="Mammography",
        description="X-ray imaging of the breast",
        meaning=NCIT["C16818"])
    ANGIOGRAPHY = PermissibleValue(
        text="ANGIOGRAPHY",
        title="Angiography",
        description="Imaging of blood vessels (CT, MR, or catheter angiography)",
        meaning=NCIT["C190556"])
    OCT = PermissibleValue(
        text="OCT",
        title="Optical Coherence Tomography",
        description="Optical coherence tomography (e.g., retinal OCT)",
        meaning=NCIT["C20828"])
    OTHER = PermissibleValue(
        text="OTHER",
        title="Other imaging modality",
        description="An imaging modality not otherwise enumerated")

    _defn = EnumDefinition(
        name="ImagingModalityEnum",
        description="""In-vivo medical imaging modality by which an ImagingFinding is detected. Meanings bind to the NCI Thesaurus Diagnostic Imaging branch.""",
    )

class ElectrophysiologyModalityEnum(EnumDefinitionImpl):
    """
    In-vivo electrophysiologic / neurophysiologic investigation on which an electrophysiologic phenotype was recorded
    (carried on the ElectrophysiologyContext phenotype sidecar). Meanings bind to the NCI Thesaurus
    diagnostic-procedure branch.
    """
    EEG = PermissibleValue(
        text="EEG",
        title="Electroencephalography",
        description="Scalp electroencephalography (routine, prolonged, or ambulatory)",
        meaning=NCIT["C38054"])
    VIDEO_EEG = PermissibleValue(
        text="VIDEO_EEG",
        title="Video Electroencephalography",
        description="""Simultaneous video and EEG monitoring for seizure semiology-EEG correlation. No distinct NCIT procedure term; a specialization of EEG.""")
    ECG = PermissibleValue(
        text="ECG",
        title="Electrocardiography",
        description="Electrocardiography, including resting and stress ECG",
        meaning=NCIT["C38053"])
    EMG = PermissibleValue(
        text="EMG",
        title="Electromyography",
        description="Needle or surface electromyography",
        meaning=NCIT["C38056"])
    NERVE_CONDUCTION_STUDY = PermissibleValue(
        text="NERVE_CONDUCTION_STUDY",
        title="Nerve Conduction Velocity Test",
        description="Nerve conduction study (motor/sensory conduction velocity and amplitude)",
        meaning=NCIT["C88502"])
    EVOKED_POTENTIAL = PermissibleValue(
        text="EVOKED_POTENTIAL",
        title="Evoked Potential",
        description="""Evoked-potential testing (visual, brainstem-auditory, or somatosensory). No clean generic NCIT procedure term.""")
    POLYSOMNOGRAPHY = PermissibleValue(
        text="POLYSOMNOGRAPHY",
        title="Polysomnography",
        description="Overnight sleep study combining EEG, EOG, EMG, ECG, and respiratory channels",
        meaning=NCIT["C114185"])
    MEG = PermissibleValue(
        text="MEG",
        title="Magnetoencephalography",
        description="Magnetoencephalography (magnetic-field source localization)",
        meaning=NCIT["C16811"])
    OTHER = PermissibleValue(
        text="OTHER",
        title="Other electrophysiologic modality",
        description="An electrophysiologic modality not otherwise enumerated")

    _defn = EnumDefinition(
        name="ElectrophysiologyModalityEnum",
        description="""In-vivo electrophysiologic / neurophysiologic investigation on which an electrophysiologic phenotype was recorded (carried on the ElectrophysiologyContext phenotype sidecar). Meanings bind to the NCI Thesaurus diagnostic-procedure branch.""",
    )

class IctalStateEnum(EnumDefinitionImpl):
    """
    Timing of an electrophysiologic finding relative to a seizure or paroxysmal event - the axis a flat HP phenotype
    term cannot express.
    """
    ICTAL = PermissibleValue(
        text="ICTAL",
        description="Recorded during a seizure / paroxysmal event")
    INTERICTAL = PermissibleValue(
        text="INTERICTAL",
        description="Recorded between events, in the baseline state")
    POSTICTAL = PermissibleValue(
        text="POSTICTAL",
        description="Recorded in the period immediately following an event")

    _defn = EnumDefinition(
        name="IctalStateEnum",
        description="""Timing of an electrophysiologic finding relative to a seizure or paroxysmal event - the axis a flat HP phenotype term cannot express.""",
    )

class EEGRecordingStateEnum(EnumDefinitionImpl):
    """
    Behavioural state or activation procedure under which an EEG finding is recorded, since many findings are state-
    or provocation-dependent.
    """
    AWAKE = PermissibleValue(
        text="AWAKE",
        description="Recorded during wakefulness")
    ASLEEP = PermissibleValue(
        text="ASLEEP",
        description="Recorded during sleep (findings may be sleep-activated)")
    DROWSY = PermissibleValue(
        text="DROWSY",
        description="Recorded during drowsiness / transition to sleep")
    SLEEP_DEPRIVED = PermissibleValue(
        text="SLEEP_DEPRIVED",
        description="Recorded after sleep deprivation (a seizure-activation procedure)")
    PHOTIC_STIMULATION = PermissibleValue(
        text="PHOTIC_STIMULATION",
        description="Recorded during intermittent photic stimulation")
    HYPERVENTILATION = PermissibleValue(
        text="HYPERVENTILATION",
        description="Recorded during hyperventilation activation")

    _defn = EnumDefinition(
        name="EEGRecordingStateEnum",
        description="""Behavioural state or activation procedure under which an EEG finding is recorded, since many findings are state- or provocation-dependent.""",
    )

class MedicalActionCategoryEnum(EnumDefinitionImpl):
    """
    Broad functional category for a clinical action currently represented in the treatments section. Specific actions
    such as genetic counseling should be represented by treatment_term, while this category stays at the level needed
    for validation and rendering.
    """
    THERAPEUTIC = PermissibleValue(
        text="THERAPEUTIC",
        title="Therapeutic Procedure",
        description="""An action intended to treat, prevent, mitigate, or manage disease processes, complications, or symptoms. These actions may link to pathophysiology nodes or phenotypes through target_mechanisms or target_phenotypes.""",
        meaning=NCIT["C49236"])
    DIAGNOSTIC = PermissibleValue(
        text="DIAGNOSTIC",
        title="Diagnostic Procedure",
        description="""A diagnostic procedure or testing action used to establish or refine a diagnosis. These actions should not use target_mechanisms or target_phenotypes because they do not treat pathophysiology nodes or phenotypes.""",
        meaning=NCIT["C18020"])
    SCREENING = PermissibleValue(
        text="SCREENING",
        title="Disease Screening",
        description="""Screening or surveillance intended to detect disease, risk, or early manifestations. These actions should not use target_mechanisms or target_phenotypes.""",
        meaning=NCIT["C15419"])
    MONITORING = PermissibleValue(
        text="MONITORING",
        title="Monitoring",
        description="""Clinical, laboratory, imaging, or longitudinal follow-up used to observe disease status or complications. These actions should not use target_mechanisms or target_phenotypes.""",
        meaning=NCIT["C61256"])
    COUNSELING_INFORMATIONAL = PermissibleValue(
        text="COUNSELING_INFORMATIONAL",
        title="Counseling",
        description="""Counseling, education, risk communication, cascade-testing support, or reproductive planning actions. Use this broad category for genetic counseling and related informational interventions. These actions should not use target_mechanisms or target_phenotypes because they do not directly modify disease pathophysiology or phenotypes.""",
        meaning=NCIT["C61547"])

    _defn = EnumDefinition(
        name="MedicalActionCategoryEnum",
        description="""Broad functional category for a clinical action currently represented in the treatments section. Specific actions such as genetic counseling should be represented by treatment_term, while this category stays at the level needed for validation and rendering.""",
    )

class TherapeuticModalityEnum(EnumDefinitionImpl):
    """
    Broad therapeutic modality / platform of a treatment, independent of the specific agent or NCIT action term.
    Captures the "kind of thing" a treatment is (e.g., a small molecule vs. an antisense oligonucleotide vs. a gene
    therapy) so treatments are queryable by platform across diseases.
    """
    SMALL_MOLECULE = PermissibleValue(
        text="SMALL_MOLECULE",
        description="Small-molecule pharmacotherapy (orally or parenterally administered chemical drugs)",
        meaning=NCIT["C48809"])
    MONOCLONAL_ANTIBODY = PermissibleValue(
        text="MONOCLONAL_ANTIBODY",
        description="""Monoclonal antibody or antibody-derived biologic (including bispecifics and antibody-drug conjugates)""",
        meaning=NCIT["C20401"])
    NANOBODY = PermissibleValue(
        text="NANOBODY",
        title="Nanobody / single-domain antibody",
        description="""Single-domain antibody (sdAb/VHH/Nanobody) — a single variable-domain immunoglobulin fragment (e.g., caplacizumab), distinct from full-size monoclonal antibodies""")
    ANTISENSE_OLIGONUCLEOTIDE = PermissibleValue(
        text="ANTISENSE_OLIGONUCLEOTIDE",
        title="Antisense oligonucleotide",
        description="""Single-stranded antisense oligonucleotide (ASO) acting on RNA via RNase H, splice modulation, or steric blockade""",
        meaning=NCIT["C1291"])
    SIRNA = PermissibleValue(
        text="SIRNA",
        title="siRNA / RNAi",
        description="Small interfering RNA or other double-stranded RNAi therapeutic",
        meaning=NCIT["C2191"])
    MRNA_THERAPY = PermissibleValue(
        text="MRNA_THERAPY",
        title="mRNA therapy",
        description="""Therapeutic messenger RNA delivering a functional transcript (excludes prophylactic mRNA vaccines, see VACCINE)""")
    GENE_THERAPY = PermissibleValue(
        text="GENE_THERAPY",
        description="Gene addition/replacement therapy (e.g., AAV- or lentivirus-delivered transgene)",
        meaning=NCIT["C15238"])
    GENE_EDITING = PermissibleValue(
        text="GENE_EDITING",
        description="In vivo or ex vivo genome editing (e.g., CRISPR/Cas, base or prime editing)")
    CELL_THERAPY = PermissibleValue(
        text="CELL_THERAPY",
        description="Cell-based therapy (e.g., CAR-T, stem cell transplantation, engineered cells)",
        meaning=NCIT["C70601"])
    PROTEIN_REPLACEMENT = PermissibleValue(
        text="PROTEIN_REPLACEMENT",
        description="Recombinant protein or enzyme replacement therapy",
        meaning=NCIT["C16221"])
    PEPTIDE = PermissibleValue(
        text="PEPTIDE",
        description="Therapeutic peptide or peptide analog",
        meaning=CHEBI["16670"])
    VACCINE = PermissibleValue(
        text="VACCINE",
        description="Prophylactic or therapeutic vaccine",
        meaning=NCIT["C923"])
    RADIOTHERAPY = PermissibleValue(
        text="RADIOTHERAPY",
        description="Radiation-based therapy",
        meaning=NCIT["C15313"])
    SURGERY = PermissibleValue(
        text="SURGERY",
        description="Surgical or procedural intervention",
        meaning=NCIT["C15329"])
    DEVICE = PermissibleValue(
        text="DEVICE",
        description="Implanted or external therapeutic device",
        meaning=NCIT["C16830"])
    BEHAVIORAL = PermissibleValue(
        text="BEHAVIORAL",
        description="Non-pharmacologic behavioral, physical, dietary, or lifestyle intervention")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Modality not covered by the above categories")

    _defn = EnumDefinition(
        name="TherapeuticModalityEnum",
        description="""Broad therapeutic modality / platform of a treatment, independent of the specific agent or NCIT action term. Captures the \"kind of thing\" a treatment is (e.g., a small molecule vs. an antisense oligonucleotide vs. a gene therapy) so treatments are queryable by platform across diseases.""",
    )

class AsoMechanismEnum(EnumDefinitionImpl):
    """
    Molecular mechanism of action of an antisense oligonucleotide, following the three core ASO paradigms (RNase
    H-mediated degradation, splice modulation, and steric blockade) described in Sang et al. 2024 (PMID:38914784).
    """
    RNASE_H_KNOCKDOWN = PermissibleValue(
        text="RNASE_H_KNOCKDOWN",
        title="RNase H knockdown",
        description="""ASO:RNA heteroduplex recruits RNase H1 to cleave the target mRNA, reducing a toxic or gain-of-function protein""",
        meaning=GO["0004523"])
    SPLICE_MODULATION_EXON_SKIPPING = PermissibleValue(
        text="SPLICE_MODULATION_EXON_SKIPPING",
        title="Splice modulation (exon skipping)",
        description="""ASO occludes a splice site or splicing element to exclude an exon, restoring an in-frame transcript (e.g., DMD exon skipping)""")
    SPLICE_MODULATION_EXON_INCLUSION = PermissibleValue(
        text="SPLICE_MODULATION_EXON_INCLUSION",
        title="Splice modulation (exon inclusion)",
        description="""ASO blocks an intronic splicing silencer to promote exon inclusion (e.g., nusinersen at SMN2 ISS-N1)""")
    STERIC_BLOCKADE = PermissibleValue(
        text="STERIC_BLOCKADE",
        title="Steric translational blockade",
        description="""ASO sterically blocks ribosome access or other RNA-protein interactions without inducing cleavage (e.g., fomivirsen)""")
    MIRNA_MODULATION = PermissibleValue(
        text="MIRNA_MODULATION",
        title="miRNA modulation",
        description="ASO sequesters or inhibits a microRNA (antimiR) or blocks a miRNA binding site")

    _defn = EnumDefinition(
        name="AsoMechanismEnum",
        description="""Molecular mechanism of action of an antisense oligonucleotide, following the three core ASO paradigms (RNase H-mediated degradation, splice modulation, and steric blockade) described in Sang et al. 2024 (PMID:38914784).""",
    )

class AsoChemistryEnum(EnumDefinitionImpl):
    """
    Backbone / sugar chemistry of an antisense oligonucleotide. Determines nuclease resistance, binding affinity, and
    whether the ASO supports RNase H recruitment (gapmer designs) or acts purely by steric occupancy.
    """
    PHOSPHOROTHIOATE = PermissibleValue(
        text="PHOSPHOROTHIOATE",
        title="Phosphorothioate backbone",
        description="""Phosphorothioate (PS) backbone modification conferring nuclease resistance; common base chemistry for RNase H ASOs""",
        meaning=CHEBI["76674"])
    PHOSPHORODIAMIDATE_MORPHOLINO = PermissibleValue(
        text="PHOSPHORODIAMIDATE_MORPHOLINO",
        title="Phosphorodiamidate morpholino (PMO)",
        description="""Morpholino backbone (PMO); charge-neutral, steric-block/splice-switching chemistry (e.g., eteplirsen, golodirsen)""")
    TWO_PRIME_O_METHYL = PermissibleValue(
        text="TWO_PRIME_O_METHYL",
        title="2'-O-methyl",
        description="2'-O-methyl (2'-OMe) ribose modification")
    TWO_PRIME_O_METHOXYETHYL = PermissibleValue(
        text="TWO_PRIME_O_METHOXYETHYL",
        title="2'-O-methoxyethyl (2'-MOE)",
        description="2'-O-methoxyethyl (2'-MOE) ribose modification (e.g., nusinersen, inotersen, eplontersen)")
    LOCKED_NUCLEIC_ACID = PermissibleValue(
        text="LOCKED_NUCLEIC_ACID",
        title="Locked nucleic acid (LNA)",
        description="Locked nucleic acid bridged-bicyclic sugar modification")
    CONSTRAINED_ETHYL = PermissibleValue(
        text="CONSTRAINED_ETHYL",
        title="Constrained ethyl (cEt)",
        description="Constrained ethyl (cEt) bridged sugar modification")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Chemistry not covered by the above categories")

    _defn = EnumDefinition(
        name="AsoChemistryEnum",
        description="""Backbone / sugar chemistry of an antisense oligonucleotide. Determines nuclease resistance, binding affinity, and whether the ASO supports RNase H recruitment (gapmer designs) or acts purely by steric occupancy.""",
    )

class AsoConjugationEnum(EnumDefinitionImpl):
    """
    Targeting ligand or conjugate attached to an antisense oligonucleotide to direct tissue uptake or improve
    pharmacokinetics.
    """
    UNCONJUGATED = PermissibleValue(
        text="UNCONJUGATED",
        description="No targeting conjugate (naked ASO)")
    GALNAC = PermissibleValue(
        text="GALNAC",
        title="GalNAc-conjugated",
        description="""Tri-antennary N-acetylgalactosamine conjugate for hepatocyte (ASGR-mediated) uptake (e.g., eplontersen, olezarsen)""",
        meaning=CHEBI["28037"])
    LIPID = PermissibleValue(
        text="LIPID",
        description="Lipid or fatty-acid conjugate")
    PEPTIDE = PermissibleValue(
        text="PEPTIDE",
        description="Cell-penetrating or targeting peptide conjugate")
    ANTIBODY = PermissibleValue(
        text="ANTIBODY",
        description="Antibody-oligonucleotide conjugate (AOC) for receptor-targeted delivery")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Conjugate not covered by the above categories")

    _defn = EnumDefinition(
        name="AsoConjugationEnum",
        description="""Targeting ligand or conjugate attached to an antisense oligonucleotide to direct tissue uptake or improve pharmacokinetics.""",
    )

class MechanisticHypothesisStatusEnum(EnumDefinitionImpl):
    """
    Curation/maturity status for a disease-level mechanistic hypothesis
    """
    CANONICAL = PermissibleValue(
        text="CANONICAL",
        description="Widely accepted explanatory model used as the default disease mechanism")
    ALTERNATIVE = PermissibleValue(
        text="ALTERNATIVE",
        description="Plausible competing or superimposed hypothesis with supporting evidence")
    EMERGING = PermissibleValue(
        text="EMERGING",
        description="Early-stage hypothesis with limited or recently reported evidence")
    DEPRECATED = PermissibleValue(
        text="DEPRECATED",
        description="Historical hypothesis no longer supported as the current model")

    _defn = EnumDefinition(
        name="MechanisticHypothesisStatusEnum",
        description="Curation/maturity status for a disease-level mechanistic hypothesis",
    )

class BiologicalScaleEnum(EnumDefinitionImpl):
    """
    Biological scale of the substrate a pathophysiology node describes. A tag capturing which level of biological
    organisation the node is primarily situated at — molecular, cellular, tissue/organ, or organism. Each value covers
    both ongoing processes AND persistent states at that scale (a fusion protein exists / a cell population
    accumulates / an ectopic tissue persists / a metabolite is chronically elevated). See
    projects/PATHOPHYSIOLOGY_SCALE_FEASIBILITY.md for the survey that led to this enum design.
    """
    MOLECULAR = PermissibleValue(
        text="MOLECULAR",
        description="""Molecular scale — molecular activities (kinase activity, transcription factor binding, ion transport, catalysis) or molecular states (a fusion protein exists, a chemical accumulates, an enzyme is functionally deficient, a gene carries a variant burden). Substrate is a molecule, complex, or genetic element.""")
    CELLULAR = PermissibleValue(
        text="CELLULAR",
        description="""Cellular scale — cellular processes (differentiation, apoptosis, autophagy, intracellular signaling) or cellular states (a cell population is in a maintained aberrant condition, an organelle is structurally disrupted, a cell type has accumulated). Substrate is a single cell or cell type.""")
    TISSUE = PermissibleValue(
        text="TISSUE",
        description="""Tissue / organ scale — tissue processes (inflammation, fibrosis, granuloma formation, neoplastic outgrowth) or tissue states (an ectopic tissue persists, an organ is malformed, a structural lesion exists). Substrate is a tissue, organ, or anatomical structure.""")
    ORGANISM = PermissibleValue(
        text="ORGANISM",
        description="""Organism scale — systemic / multi-organ / whole-body processes (DIC, cytokine storm, fever, cachexia) or systemic states (a metabolite is chronically elevated, the microbiome is dysbiotic, a syndromic developmental phenotype bundles multi-organ features). Substrate is the whole organism.""")

    _defn = EnumDefinition(
        name="BiologicalScaleEnum",
        description="""Biological scale of the substrate a pathophysiology node describes. A tag capturing which level of biological organisation the node is primarily situated at — molecular, cellular, tissue/organ, or organism. Each value covers both ongoing processes AND persistent states at that scale (a fusion protein exists / a cell population accumulates / an ectopic tissue persists / a metabolite is chronically elevated). See projects/PATHOPHYSIOLOGY_SCALE_FEASIBILITY.md for the survey that led to this enum design.""",
    )

class DiscussionKindEnum(EnumDefinitionImpl):
    """
    Kind of unresolved/in-progress item captured by a Discussion. Discussions are thread-like objects that record open
    questions, controversies, curation todos, emerging hypotheses, or interpretation debates attached to a disease
    entry or sub-object. Knowledge gaps are represented as a discussion kind so they can reuse the existing pointer,
    evidence, and lifecycle machinery, while optional proposed experiments capture how a gap could be resolved.
    """
    OPEN_QUESTION = PermissibleValue(
        text="OPEN_QUESTION",
        description="An unresolved scientific question posed by curators or experts")
    KNOWLEDGE_GAP = PermissibleValue(
        text="KNOWLEDGE_GAP",
        description="""A missing causal, evidentiary, model-system, or translational assertion whose resolution would materially improve the disease mechanism model""")
    CONTROVERSY = PermissibleValue(
        text="CONTROVERSY",
        description="A live disagreement or competing interpretation between published positions")
    CURATION_TODO = PermissibleValue(
        text="CURATION_TODO",
        description="A curation task captured inline (e.g., \"phenotype needs HPO term refinement\")")
    EMERGING_HYPOTHESIS = PermissibleValue(
        text="EMERGING_HYPOTHESIS",
        description="A recently reported hypothesis under active discussion in the community")
    INTERPRETATION = PermissibleValue(
        text="INTERPRETATION",
        description="A discussion about how to interpret existing evidence or model an edge")
    HUMAN_MODEL_MISMATCH = PermissibleValue(
        text="HUMAN_MODEL_MISMATCH",
        description="""A knowledge gap where model-system evidence exists but its fidelity to human disease-relevant biology is uncertain — the model may recapitulate a proximal mechanism or phenotype only partially, or the relevant human cell type (e.g., outer radial glia) or anatomy (e.g., gyrencephalic cortex) is absent from the model. Distinct from KNOWLEDGE_GAP (which covers any missing assertion) in that some mechanistic evidence exists but translational validity is the open question. Use when a curator wants to flag that model-organism, organoid, or in vitro data support a node but it is unclear whether the same mechanism operates in the human disease context.""")

    _defn = EnumDefinition(
        name="DiscussionKindEnum",
        description="""Kind of unresolved/in-progress item captured by a Discussion. Discussions are thread-like objects that record open questions, controversies, curation todos, emerging hypotheses, or interpretation debates attached to a disease entry or sub-object. Knowledge gaps are represented as a discussion kind so they can reuse the existing pointer, evidence, and lifecycle machinery, while optional proposed experiments capture how a gap could be resolved.""",
    )

class DiscussionStatusEnum(EnumDefinitionImpl):
    """
    Lifecycle status for a Discussion
    """
    OPEN = PermissibleValue(
        text="OPEN",
        description="Posed but not yet under active discussion")
    UNDER_DISCUSSION = PermissibleValue(
        text="UNDER_DISCUSSION",
        description="Actively being discussed in one or more linked venues")
    RESOLVED = PermissibleValue(
        text="RESOLVED",
        description="Closed with a documented resolution; kept for provenance")
    ARCHIVED = PermissibleValue(
        text="ARCHIVED",
        description="No longer active and not resolved (deferred, stale, or superseded)")

    _defn = EnumDefinition(
        name="DiscussionStatusEnum",
        description="Lifecycle status for a Discussion",
    )

class ComorbidityDirectionEnum(EnumDefinitionImpl):
    """
    Directionality of a comorbidity/trajectory association
    """
    A_BEFORE_B = PermissibleValue(
        text="A_BEFORE_B",
        description="A precedes B")
    B_BEFORE_A = PermissibleValue(
        text="B_BEFORE_A",
        description="B precedes A")
    BIDIRECTIONAL = PermissibleValue(
        text="BIDIRECTIONAL",
        description="Evidence supports both directions")
    SAME_TIME = PermissibleValue(
        text="SAME_TIME",
        description="Co-incident or same-time association")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="Directionality is unknown or not established")

    _defn = EnumDefinition(
        name="ComorbidityDirectionEnum",
        description="Directionality of a comorbidity/trajectory association",
    )

class ComorbidityEffectDirectionEnum(EnumDefinitionImpl):
    """
    The sign (effect direction) of a comorbidity/trajectory association - whether the presence of one condition raises
    or lowers the risk, incidence, or severity of the other. This is orthogonal to ComorbidityDirectionEnum, which
    captures only the temporal ordering (which condition comes first), not whether the effect is positive or inverse.
    A conventional risk comorbidity (A increases risk of B) is RISK; the cancer/Alzheimer's-disease inverse
    correlation is PROTECTIVE.
    """
    RISK = PermissibleValue(
        text="RISK",
        title="Risk (positive) association",
        description="""Positive association: the presence of one condition increases the risk, incidence, or severity of the other. This is the conventional comorbidity direction and the default for most curated pairs.""")
    PROTECTIVE = PermissibleValue(
        text="PROTECTIVE",
        title="Protective (inverse) association",
        description="""Inverse association: the presence of one condition is associated with a reduced risk or incidence of the other (e.g., the reciprocal cancer/Alzheimer's-disease inverse correlation, atopy and glioma, balancing-selection heterozygote advantage). Quantitatively an odds ratio / hazard ratio / relative risk below 1.""")
    MIXED = PermissibleValue(
        text="MIXED",
        title="Mixed / direction-dependent association",
        description="""The effect direction is not uniform: it is protective in some contexts (subtype, direction, population) and risk-conferring in others (e.g., Parkinson's disease shows an inverse association with most cancers but a positive association with melanoma). Use the per-signal effect_direction and notes to record the split.""")
    NO_ASSOCIATION = PermissibleValue(
        text="NO_ASSOCIATION",
        title="No association",
        description="""Evidence indicates no significant association in either direction (a null result). Useful for recording examined-but-refuted pairs.""")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="The effect direction (risk vs. protective) has not been established.")

    _defn = EnumDefinition(
        name="ComorbidityEffectDirectionEnum",
        description="""The sign (effect direction) of a comorbidity/trajectory association - whether the presence of one condition raises or lowers the risk, incidence, or severity of the other. This is orthogonal to ComorbidityDirectionEnum, which captures only the temporal ordering (which condition comes first), not whether the effect is positive or inverse. A conventional risk comorbidity (A increases risk of B) is RISK; the cancer/Alzheimer's-disease inverse correlation is PROTECTIVE.""",
    )

class CurationStatusEnum(EnumDefinitionImpl):
    """
    Curation workflow status for an association
    """
    CANDIDATE = PermissibleValue(
        text="CANDIDATE",
        description="Prioritized for curation")
    IN_PROGRESS = PermissibleValue(
        text="IN_PROGRESS",
        description="Curation in progress")
    CURATED = PermissibleValue(
        text="CURATED",
        description="Curated with literature-backed evidence")
    DEFERRED = PermissibleValue(
        text="DEFERRED",
        description="Deferred or deprioritized")

    _defn = EnumDefinition(
        name="CurationStatusEnum",
        description="Curation workflow status for an association",
    )

class AssociationSignalSourceEnum(EnumDefinitionImpl):
    """
    Source of an association signal
    """
    DISEASE_TRAJECTORIES = PermissibleValue(
        text="DISEASE_TRAJECTORIES",
        description="Disease Trajectories (CSH/Austria)")
    COHD = PermissibleValue(
        text="COHD",
        description="Columbia Open Health Data (COHD)")
    ICEES = PermissibleValue(
        text="ICEES",
        description="Integrated Clinical and Environmental Exposures Service KG (RENCI/UNC)")
    LITERATURE = PermissibleValue(
        text="LITERATURE",
        description="Published literature source")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Other or unspecified source")

    _defn = EnumDefinition(
        name="AssociationSignalSourceEnum",
        description="Source of an association signal",
    )

class AssociationSignalMethodEnum(EnumDefinitionImpl):
    """
    Method used to derive an association signal
    """
    EHR_TEMPORAL_COMORBIDITY = PermissibleValue(
        text="EHR_TEMPORAL_COMORBIDITY",
        description="EHR-derived temporal comorbidity/trajectory signal")
    EHR_COHORT_ASSOCIATION = PermissibleValue(
        text="EHR_COHORT_ASSOCIATION",
        description="EHR-derived cohort association (non-temporal)")
    LITERATURE_ASSOCIATION = PermissibleValue(
        text="LITERATURE_ASSOCIATION",
        description="Association reported in the literature")
    COMPUTATIONAL_INFERENCE = PermissibleValue(
        text="COMPUTATIONAL_INFERENCE",
        description="Computational inference or enrichment")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Other or unspecified method")

    _defn = EnumDefinition(
        name="AssociationSignalMethodEnum",
        description="Method used to derive an association signal",
    )

class SexEnum(EnumDefinitionImpl):
    """
    Sex-specific stratum
    """
    MALE = PermissibleValue(
        text="MALE",
        description="Male")
    FEMALE = PermissibleValue(
        text="FEMALE",
        description="Female")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Other or nonbinary")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="Unknown or not specified")

    _defn = EnumDefinition(
        name="SexEnum",
        description="Sex-specific stratum",
    )

class ConditionCompositionEnum(EnumDefinitionImpl):
    """
    Composition type for a composite condition descriptor
    """
    SINGLE = PermissibleValue(
        text="SINGLE",
        description="Single condition (default)")
    UNION = PermissibleValue(
        text="UNION",
        description="Union of multiple component conditions")
    CATEGORY = PermissibleValue(
        text="CATEGORY",
        description="Category code encompassing multiple conditions")
    OVERLAPS = PermissibleValue(
        text="OVERLAPS",
        description="Overlapping condition set (non-exhaustive)")
    SUBSET_OF = PermissibleValue(
        text="SUBSET_OF",
        description="Subset of a broader condition group")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Other or unspecified composition")

    _defn = EnumDefinition(
        name="ConditionCompositionEnum",
        description="Composition type for a composite condition descriptor",
    )

class AssociationMetricTypeEnum(EnumDefinitionImpl):
    """
    Type of association metric
    """
    OR = PermissibleValue(
        text="OR",
        description="Odds ratio")
    AOR = PermissibleValue(
        text="AOR",
        description="Adjusted odds ratio")
    RR = PermissibleValue(
        text="RR",
        description="Relative risk")
    HR = PermissibleValue(
        text="HR",
        description="Hazard ratio")
    PREVALENCE = PermissibleValue(
        text="PREVALENCE",
        description="Prevalence proportion")
    INCIDENCE_RATE = PermissibleValue(
        text="INCIDENCE_RATE",
        description="Incidence rate")
    IRR = PermissibleValue(
        text="IRR",
        description="Incidence rate ratio")
    CHI_SQUARE = PermissibleValue(
        text="CHI_SQUARE",
        description="Chi-square association statistic")
    LOG_OBS_EXP_RATIO = PermissibleValue(
        text="LOG_OBS_EXP_RATIO",
        description="Natural-log observed-to-expected co-occurrence ratio")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Other or unspecified metric")

    _defn = EnumDefinition(
        name="AssociationMetricTypeEnum",
        description="Type of association metric",
    )

class MechanismConfidenceEnum(EnumDefinitionImpl):
    """
    Level of confidence in a pathophysiology mechanism
    """
    ESTABLISHED = PermissibleValue(
        text="ESTABLISHED",
        title="Established",
        description="Well-established mechanism with strong evidence from multiple independent studies")
    HYPOTHETICAL = PermissibleValue(
        text="HYPOTHETICAL",
        title="Hypothetical",
        description="Hypothetical mechanism with limited or indirect evidence; plausible but not yet validated")
    PROVISIONAL = PermissibleValue(
        text="PROVISIONAL",
        title="Provisional",
        description="Provisional mechanism under active investigation with emerging but incomplete evidence")

    _defn = EnumDefinition(
        name="MechanismConfidenceEnum",
        description="Level of confidence in a pathophysiology mechanism",
    )

class GroupingBasisEnum(EnumDefinitionImpl):
    """
    The axis (or axes) on which a disease Grouping is drawn. A grouping assembles already-distinct Disease entries
    into an explicit union; this enum records WHY they belong together, supporting an audit of the grouping boundary.
    Multivalued — a grouping may rest on more than one basis (e.g., the mucopolysaccharidoses are grouped on both a
    shared mechanism and a shared gene/enzyme family).
    """
    SHARED_MECHANISM = PermissibleValue(
        text="SHARED_MECHANISM",
        title="Shared mechanism",
        description="""Members converge on a common pathophysiological mechanism or final-common-pathway (often a shared mechanism module).""")
    SHARED_GENE_FAMILY = PermissibleValue(
        text="SHARED_GENE_FAMILY",
        title="Shared gene family",
        description="""Members are caused by variants in the same gene, gene family, or functionally related set of genes/enzymes.""")
    SHARED_PATHWAY = PermissibleValue(
        text="SHARED_PATHWAY",
        title="Shared pathway",
        description="Members perturb the same biological pathway or process.")
    SHARED_PHENOTYPE = PermissibleValue(
        text="SHARED_PHENOTYPE",
        title="Shared phenotype",
        description="Members share a defining clinical phenotype or phenotypic spectrum.")
    SHARED_TREATMENT_RESPONSE = PermissibleValue(
        text="SHARED_TREATMENT_RESPONSE",
        title="Shared treatment response",
        description="""Members are grouped by a shared therapeutic vulnerability or response to a common class of treatment.""")
    CLINICAL_CONVENTION = PermissibleValue(
        text="CLINICAL_CONVENTION",
        title="Clinical convention",
        description="""Members are grouped by established clinical or nosological convention rather than a single mechanistic axis.""")
    OTHER = PermissibleValue(
        text="OTHER",
        title="Other",
        description="A grouping basis that does not fit the categories above.")

    _defn = EnumDefinition(
        name="GroupingBasisEnum",
        description="""The axis (or axes) on which a disease Grouping is drawn. A grouping assembles already-distinct Disease entries into an explicit union; this enum records WHY they belong together, supporting an audit of the grouping boundary. Multivalued — a grouping may rest on more than one basis (e.g., the mucopolysaccharidoses are grouped on both a shared mechanism and a shared gene/enzyme family).""",
    )

class LogicalOperatorEnum(EnumDefinitionImpl):
    """
    Boolean operator for a branch node in a nested membership-criteria expression (LogicalCriterion). Branch nodes set
    an operator and combine child operands; leaf nodes set a criterion_predicate instead.
    """
    AND = PermissibleValue(
        text="AND",
        description="All operands must hold (conjunction).")
    OR = PermissibleValue(
        text="OR",
        description="At least one operand must hold (disjunction).")
    NOT = PermissibleValue(
        text="NOT",
        description="Negation. Conventionally applied to a single operand (or to the conjunction of its operands).")

    _defn = EnumDefinition(
        name="LogicalOperatorEnum",
        description="""Boolean operator for a branch node in a nested membership-criteria expression (LogicalCriterion). Branch nodes set an operator and combine child operands; leaf nodes set a criterion_predicate instead.""",
    )

class CriterionPredicateEnum(EnumDefinitionImpl):
    """
    The kind of constraint expressed by a leaf node in a membership-criteria expression (LogicalCriterion). The leaf's
    payload slots are interpreted according to this predicate (e.g., HAS_PHENOTYPE uses phenotype_term and optional
    min_frequency; HAS_GENE uses gene; CONFORMS_TO_MODULE uses module).
    """
    HAS_PHENOTYPE = PermissibleValue(
        text="HAS_PHENOTYPE",
        description="""Members present a given phenotype (phenotype_term), optionally at or above a frequency threshold (min_frequency).""")
    HAS_GENE = PermissibleValue(
        text="HAS_GENE",
        description="Members carry causal variants in a given gene (gene).")
    CONFORMS_TO_MODULE = PermissibleValue(
        text="CONFORMS_TO_MODULE",
        description="Members have a pathophysiology node conforming to a given mechanism module (module).")
    HAS_BIOLOGICAL_PROCESS = PermissibleValue(
        text="HAS_BIOLOGICAL_PROCESS",
        description="""Members involve a given biological process (biological_processes), optionally with a directional modifier.""")
    HAS_CLASSIFICATION = PermissibleValue(
        text="HAS_CLASSIFICATION",
        description="Members carry a given nosology/classification assignment (classification).")
    HAS_INHERITANCE = PermissibleValue(
        text="HAS_INHERITANCE",
        description="Members share a mode of inheritance (description carries the value).")
    HAS_MAPPING = PermissibleValue(
        text="HAS_MAPPING",
        description="Members map to a given external term or code namespace (description carries the value).")
    OTHER = PermissibleValue(
        text="OTHER",
        description="""A membership constraint that does not fit the categories above; described in free text via the description slot.""")

    _defn = EnumDefinition(
        name="CriterionPredicateEnum",
        description="""The kind of constraint expressed by a leaf node in a membership-criteria expression (LogicalCriterion). The leaf's payload slots are interpreted according to this predicate (e.g., HAS_PHENOTYPE uses phenotype_term and optional min_frequency; HAS_GENE uses gene; CONFORMS_TO_MODULE uses module).""",
    )

class CriteriaSemanticsEnum(EnumDefinitionImpl):
    """
    The logical direction relating a grouping's membership criteria to its members, mirroring the OWL
    necessary/sufficient/equivalent distinction. This determines what tooling may infer: NECESSARY criteria can only
    be used to AUDIT listed members (member => criteria); SUFFICIENT criteria can be used to CLASSIFY non-members as
    candidates (criteria => member); NECESSARY_AND_SUFFICIENT criteria do both (member <=> criteria).
    """
    NECESSARY = PermissibleValue(
        text="NECESSARY",
        title="Necessary (member => criteria)",
        description="""Every member satisfies these criteria, but satisfying them does not by itself establish membership. Used to audit members for violations.""")
    SUFFICIENT = PermissibleValue(
        text="SUFFICIENT",
        title="Sufficient (criteria => member)",
        description="""Any disorder satisfying these criteria is a member. Used to classify non-members as candidate members.""")
    NECESSARY_AND_SUFFICIENT = PermissibleValue(
        text="NECESSARY_AND_SUFFICIENT",
        title="Necessary and sufficient (member <=> criteria)",
        description="""These criteria define the grouping: a disorder is a member if and only if it satisfies them. Supports both auditing and classification.""")

    _defn = EnumDefinition(
        name="CriteriaSemanticsEnum",
        description="""The logical direction relating a grouping's membership criteria to its members, mirroring the OWL necessary/sufficient/equivalent distinction. This determines what tooling may infer: NECESSARY criteria can only be used to AUDIT listed members (member => criteria); SUFFICIENT criteria can be used to CLASSIFY non-members as candidates (criteria => member); NECESSARY_AND_SUFFICIENT criteria do both (member <=> criteria).""",
    )

class GroupingMemberTypeEnum(EnumDefinitionImpl):
    """
    The kind of entity referenced by a GroupingMember.
    """
    DISEASE = PermissibleValue(
        text="DISEASE",
        description="A Disease entry in kb/disorders/.")
    SUBTYPE = PermissibleValue(
        text="SUBTYPE",
        description="A named subtype within a Disease entry.")
    GROUPING = PermissibleValue(
        text="GROUPING",
        description="Another Grouping (nested grouping).")

    _defn = EnumDefinition(
        name="GroupingMemberTypeEnum",
        description="The kind of entity referenced by a GroupingMember.",
    )

class ModuleCollectionTypeEnum(EnumDefinitionImpl):
    """
    The organizing principle for a curated collection of mechanism modules. Collections are navigation and framework
    records, not mechanism modules themselves and not disease groupings.
    """
    PUBLISHED_FRAMEWORK = PermissibleValue(
        text="PUBLISHED_FRAMEWORK",
        title="Published framework",
        description="""A named framework or model defined in the scientific literature, such as the Hallmarks of Aging.""")
    MECHANISTIC_FAMILY = PermissibleValue(
        text="MECHANISTIC_FAMILY",
        title="Mechanistic family",
        description="Modules sharing a broad mechanistic pattern or process family.")
    BIOLOGICAL_SYSTEM = PermissibleValue(
        text="BIOLOGICAL_SYSTEM",
        title="Biological system",
        description="Modules organized by the biological system or compartment involved.")
    PATHOLOGICAL_OUTCOME = PermissibleValue(
        text="PATHOLOGICAL_OUTCOME",
        title="Pathological outcome",
        description="Modules organized by a shared class of pathological outcome.")
    THERAPEUTIC_STRATEGY = PermissibleValue(
        text="THERAPEUTIC_STRATEGY",
        title="Therapeutic strategy",
        description="Modules organized by a shared intervention or therapeutic strategy.")
    OTHER = PermissibleValue(
        text="OTHER",
        title="Other",
        description="A module-collection basis not covered by the other values.")

    _defn = EnumDefinition(
        name="ModuleCollectionTypeEnum",
        description="""The organizing principle for a curated collection of mechanism modules. Collections are navigation and framework records, not mechanism modules themselves and not disease groupings.""",
    )

class ModuleCategoryEnum(EnumDefinitionImpl):
    """
    Areas of study a mechanism module is relevant to. A category asserts "this module is relevant to this area of
    study" — it is a discovery and browsing aid, not a mechanistic claim and not a classification of the diseases that
    conform to the module. Multivalued and deliberately non-exclusive: a drug-toxicity module is both TOXICOLOGY and
    PHARMACOLOGY, and an antiviral drug-target module is both PHARMACOLOGY and INFECTIOUS_DISEASE. Applied through the
    `module_categories` slot, which is intended for entries under `kb/modules/`.
    """
    TOXICOLOGY = PermissibleValue(
        text="TOXICOLOGY",
        title="Toxicology",
        description="""Injury caused by exposure to a xenobiotic — environmental toxicants, poisons, occupational and dietary exposures, and adverse drug reactions modelled as mechanism rather than as an outcome. Includes drug-toxicity modules and any module whose trigger arm carries a toxicant or drug exposure.""")
    PHARMACOLOGY = PermissibleValue(
        text="PHARMACOLOGY",
        title="Pharmacology",
        description="""Drug mechanism of action and therapeutic targeting: modules built around a molecular drug target, a therapeutic modality, or an acquired-resistance pathway that gates drug choice. Typically carries the target_mechanisms drug pattern.""")
    ONCOLOGY = PermissibleValue(
        text="ONCOLOGY",
        title="Oncology",
        description="""Tumor biology and cancer therapeutics — the hallmark-of-cancer capability modules, tumor-microenvironment mechanisms, and cancer-specific therapeutic vulnerabilities and resistance patterns.""")
    INFECTIOUS_DISEASE = PermissibleValue(
        text="INFECTIOUS_DISEASE",
        title="Infectious disease",
        description="""Host-pathogen mechanism and antimicrobial therapy: pathogen entry, replication, persistence and immune evasion, together with the antibacterial, antifungal, and antiviral drug-target modules.""")
    IMMUNOLOGY = PermissibleValue(
        text="IMMUNOLOGY",
        title="Immunology",
        description="""Immune-mediated mechanism — innate and adaptive immune activation, autoimmunity, hypersensitivity, chronic inflammation, and the immune contribution to tissue injury and repair.""")
    NEUROSCIENCE = PermissibleValue(
        text="NEUROSCIENCE",
        title="Neuroscience",
        description="""Nervous-system mechanism across the central, peripheral, and sensory systems: neurodegeneration, synaptic and circuit dysfunction, excitability, neurodevelopmental patterning of the brain, and neural waste clearance.""")
    DEVELOPMENTAL_BIOLOGY = PermissibleValue(
        text="DEVELOPMENTAL_BIOLOGY",
        title="Developmental biology",
        description="""Morphogenesis and embryonic patterning — signalling gradients, segmentation, cell-fate specification, and migration defects whose lesion acts during development rather than in mature tissue.""")
    METABOLISM = PermissibleValue(
        text="METABOLISM",
        title="Metabolism",
        description="""Intermediary metabolism, bioenergetics, and cellular quality control of metabolic substrate: inborn errors of metabolism, mitochondrial and lysosomal function, nutrient sensing, and storage or intoxication phenotypes.""")
    AGING = PermissibleValue(
        text="AGING",
        title="Aging",
        description="""Geroscience mechanism — the hallmarks of aging and the age-associated processes (senescence, telomere attrition, stem-cell exhaustion, proteostasis and genome-maintenance decline) that drive late-onset disease.""")

    _defn = EnumDefinition(
        name="ModuleCategoryEnum",
        description="""Areas of study a mechanism module is relevant to. A category asserts \"this module is relevant to this area of study\" — it is a discovery and browsing aid, not a mechanistic claim and not a classification of the diseases that conform to the module. Multivalued and deliberately non-exclusive: a drug-toxicity module is both TOXICOLOGY and PHARMACOLOGY, and an antiviral drug-target module is both PHARMACOLOGY and INFECTIOUS_DISEASE. Applied through the `module_categories` slot, which is intended for entries under `kb/modules/`.""",
    )

class ReferenceTagEnum(EnumDefinitionImpl):
    """
    Controlled vocabulary for tagging top-level references by authoritative source type. Enables queries like "which
    disorders lack a GeneReviews citation?"
    """
    GeneReviews = PermissibleValue(
        text="GeneReviews",
        title="GeneReviews",
        description="""Reference is a GeneReviews article published in the NCBI Bookshelf (https://www.ncbi.nlm.nih.gov/books/NBK1116/). GeneReviews are expert-authored, peer-reviewed summaries updated on a rolling basis; they are the gold-standard narrative resource for rare Mendelian disease phenotyping and management.""")

    _defn = EnumDefinition(
        name="ReferenceTagEnum",
        description="""Controlled vocabulary for tagging top-level references by authoritative source type. Enables queries like \"which disorders lack a GeneReviews citation?\"""",
    )

class GeneSetRelationshipEnum(EnumDefinitionImpl):
    """
    How an external gene set (e.g. an MSigDB/KEGG pathway, a cell-type signature, or an expression-perturbation
    signature) relates to a disease entry. Records the semantics of a curated disease<->gene-set link so the link is
    auditable and the right kind of alignment can be applied.
    """
    CANONICAL_PATHWAY = PermissibleValue(
        text="CANONICAL_PATHWAY",
        description="""A curated pathway gene set representing the disease's canonical mechanism (e.g. KEGG_ASTHMA for asthma). The primary target for BP alignment against the pathograph.""")
    CELL_TYPE_SIGNATURE = PermissibleValue(
        text="CELL_TYPE_SIGNATURE",
        description="A marker gene set for a cell type relevant to the disease.")
    PERTURBATION_SIGNATURE = PermissibleValue(
        text="PERTURBATION_SIGNATURE",
        description="""An up/down expression signature from a perturbation or contrast (e.g. drug response, knockout) relevant to the disease.""")
    DISEASE_SIGNATURE = PermissibleValue(
        text="DISEASE_SIGNATURE",
        description="A differential-expression signature derived from the disease itself.")
    OTHER = PermissibleValue(
        text="OTHER",
        description="A related gene set that does not fit the categories above.")

    _defn = EnumDefinition(
        name="GeneSetRelationshipEnum",
        description="""How an external gene set (e.g. an MSigDB/KEGG pathway, a cell-type signature, or an expression-perturbation signature) relates to a disease entry. Records the semantics of a curated disease<->gene-set link so the link is auditable and the right kind of alignment can be applied.""",
    )

class ICDOMorphologyEnum(EnumDefinitionImpl):
    """
    ICD-O morphology axis classification for cancer subtypes. Values link to NCI Thesaurus for formal definitions.
    """
    Carcinoma = PermissibleValue(
        text="Carcinoma",
        description="Cancer arising from epithelial cells",
        meaning=NCIT["C2916"])
    Adenocarcinoma = PermissibleValue(
        text="Adenocarcinoma",
        description="Carcinoma arising from glandular epithelium",
        meaning=NCIT["C2852"])
    Sarcoma = PermissibleValue(
        text="Sarcoma",
        description="Cancer arising from mesenchymal tissue",
        meaning=NCIT["C9118"])
    Leukemia = PermissibleValue(
        text="Leukemia",
        description="Cancer of blood-forming tissues",
        meaning=NCIT["C3161"])
    Lymphoma = PermissibleValue(
        text="Lymphoma",
        description="Cancer of the lymphatic system",
        meaning=NCIT["C3208"])
    Melanoma = PermissibleValue(
        text="Melanoma",
        description="Cancer arising from melanocytes",
        meaning=NCIT["C3224"])
    Glioma = PermissibleValue(
        text="Glioma",
        description="Cancer arising from glial cells",
        meaning=NCIT["C3059"])

    _defn = EnumDefinition(
        name="ICDOMorphologyEnum",
        description="""ICD-O morphology axis classification for cancer subtypes. Values link to NCI Thesaurus for formal definitions.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Squamous Cell Carcinoma",
            PermissibleValue(
                text="Squamous Cell Carcinoma",
                description="Carcinoma arising from squamous epithelium",
                meaning=NCIT["C2929"]))
        setattr(cls, "Multiple Myeloma",
            PermissibleValue(
                text="Multiple Myeloma",
                description="Cancer of plasma cells",
                meaning=NCIT["C3242"]))
        setattr(cls, "Embryonal Neoplasm",
            PermissibleValue(
                text="Embryonal Neoplasm",
                description="Cancer arising from embryonic tissue",
                meaning=NCIT["C3264"]))

class HarrisonsChapterEnum(EnumDefinitionImpl):
    """
    Harrison's Principles of Internal Medicine classification by Part. Values correspond to the high-level Parts
    (organ-system or topical groupings) of Harrison's 21st edition (2022). The slot is named `harrisons_chapter` for
    historical reasons, but the controlled vocabulary lives at the Part level since this is the granularity that
    matches how curators classify disorders. A single disease may be assigned to multiple Parts (e.g., a hereditary
    skin disorder could be tagged DERMATOLOGY and GENETICS_ENVIRONMENT_DISEASE). Free-text values used in earlier
    curation are preserved as `aliases` on the closest-fit Part so that legacy entries continue to validate.
    """
    GENERAL_CONSIDERATIONS = PermissibleValue(
        text="GENERAL_CONSIDERATIONS",
        title="General Considerations in Clinical Medicine",
        description="""Approach to the patient, clinical decision-making, ethics, evidence-based medicine, screening, and global aspects of medicine. Use sparingly for diseases - most diseases fit a more specific organ-system Part.""")
    CARDINAL_MANIFESTATIONS = PermissibleValue(
        text="CARDINAL_MANIFESTATIONS",
        title="Cardinal Manifestations and Presentation of Diseases",
        description="""Cardinal symptom and sign presentations (pain, fever, fatigue, weight change, cough, dyspnea, etc.) and chapters on alterations of the skin, ear, nose, and throat. Use for symptom-defined entries that cut across organ systems.""")
    PHARMACOLOGY = PermissibleValue(
        text="PHARMACOLOGY",
        title="Pharmacology",
        description="""Principles of clinical pharmacology, drug therapeutics, and adverse drug reactions. Rarely used for disorder entries.""")
    ONCOLOGY_HEMATOLOGY = PermissibleValue(
        text="ONCOLOGY_HEMATOLOGY",
        title="Oncology and Hematology",
        description="""Cancers (solid tumors and hematologic malignancies) and non-malignant hematologic disorders including anemias, coagulation disorders, transfusion medicine, and bone marrow failure syndromes.""")
    INFECTIOUS_DISEASES = PermissibleValue(
        text="INFECTIOUS_DISEASES",
        title="Infectious Diseases",
        description="""Bacterial, viral, fungal, parasitic, and other microbial infections; antimicrobial therapy; infections in immunocompromised hosts; and infections by organ system when presented from an infectious-disease perspective.""")
    CARDIOVASCULAR = PermissibleValue(
        text="CARDIOVASCULAR",
        title="Disorders of the Cardiovascular System",
        description="""Cardiac and vascular diseases including ischemic heart disease, heart failure, arrhythmias, cardiomyopathies, valvular and pericardial disease, congenital heart disease, and disorders of the aorta and peripheral vasculature.""")
    RESPIRATORY = PermissibleValue(
        text="RESPIRATORY",
        title="Disorders of the Respiratory System",
        description="""Pulmonary diseases including obstructive lung disease (asthma, COPD), interstitial and restrictive lung disease, pulmonary vascular disease, and respiratory failure.""")
    CRITICAL_CARE = PermissibleValue(
        text="CRITICAL_CARE",
        title="Critical Care Medicine",
        description="""Approach to the critically ill patient, including sepsis and septic shock, ARDS, multi-organ failure, and neurologic critical illness.""")
    KIDNEY_URINARY_TRACT = PermissibleValue(
        text="KIDNEY_URINARY_TRACT",
        title="Disorders of the Kidney and Urinary Tract",
        description="""Renal and urinary tract diseases including glomerular and tubulointerstitial disorders, acute kidney injury, chronic kidney disease, electrolyte and acid-base disturbances, and urolithiasis.""")
    GASTROINTESTINAL = PermissibleValue(
        text="GASTROINTESTINAL",
        title="Disorders of the Gastrointestinal System",
        description="""Digestive-system disorders including esophageal, gastric, small-bowel, colonic, hepatic, biliary, and pancreatic disease.""")
    IMMUNE_RHEUMATOLOGIC = PermissibleValue(
        text="IMMUNE_RHEUMATOLOGIC",
        title="Immune-Mediated, Inflammatory, and Rheumatologic Disorders",
        description="""Autoimmune and immune-mediated conditions, connective-tissue diseases, vasculitides, and rheumatologic disorders. Musculoskeletal disorders are also covered here in Harrison's.""")
    ENDOCRINOLOGY_METABOLISM = PermissibleValue(
        text="ENDOCRINOLOGY_METABOLISM",
        title="Endocrinology and Metabolism",
        description="""Endocrine and metabolic diseases including diabetes mellitus, thyroid, adrenal, pituitary, gonadal, calcium and bone metabolism, lipid disorders, and inborn errors of metabolism.""")
    NEUROLOGIC = PermissibleValue(
        text="NEUROLOGIC",
        title="Neurologic Disorders",
        description="""Diseases of the central and peripheral nervous system, including stroke, epilepsy, neurodegenerative disease, movement disorders, demyelinating disease, neuromuscular disease, headache, and psychiatric disorders.""")
    DERMATOLOGY = PermissibleValue(
        text="DERMATOLOGY",
        title="Disorders of the Skin",
        description="""Skin and cutaneous disorders. In Harrison's 21st edition, dermatology is organized as a section within the cardinal manifestations Part; this enum value is provided separately so that disorders that are primarily dermatologic can be classified directly.""")
    POISONING_ENVENOMATION = PermissibleValue(
        text="POISONING_ENVENOMATION",
        title="Poisoning, Drug Overdose, and Envenomation",
        description="Toxicology, poisoning syndromes, drug overdose, and bites or other venom exposures.")
    ENVIRONMENTAL_EXPOSURES = PermissibleValue(
        text="ENVIRONMENTAL_EXPOSURES",
        title="Disorders Associated with Environmental Exposures",
        description="""Disorders attributable to environmental exposures such as altitude, hypothermia/hyperthermia, drowning, and radiation injury.""")
    GENETICS_ENVIRONMENT_DISEASE = PermissibleValue(
        text="GENETICS_ENVIRONMENT_DISEASE",
        title="Genes, the Environment, and Disease",
        description="""Genetic and genomic medicine, chromosomal and Mendelian disorders not better classified by organ system, and the interplay of genes and environment in disease. Use for mechanism-defined entries (RASopathies, ciliopathies, mitochondrial disease, etc.) that span multiple organ systems.""")
    DISORDER_OF_EAR = PermissibleValue(
        text="DISORDER_OF_EAR",
        title="Disorders of the Ear",
        description="""Disorders of hearing and the vestibular system. Covered in Harrison's under cardinal-manifestation chapters on the ear.""")
    GLOBAL_MEDICINE = PermissibleValue(
        text="GLOBAL_MEDICINE",
        title="Global Medicine",
        description="Diseases and health issues that are predominantly addressed in a global health context.")
    AGING = PermissibleValue(
        text="AGING",
        title="Aging",
        description="Disorders, syndromes, and physiologic considerations specific to older adults.")
    CONSULTATIVE_MEDICINE = PermissibleValue(
        text="CONSULTATIVE_MEDICINE",
        title="Consultative Medicine",
        description="""Approach to the patient when consulting across specialties (medical consultation in surgical patients, perioperative evaluation, etc.).""")
    OTHER = PermissibleValue(
        text="OTHER",
        title="Other",
        description="""The disorder does not fit cleanly into any of the above Parts. Use sparingly and prefer the most relevant Part where possible.""")

    _defn = EnumDefinition(
        name="HarrisonsChapterEnum",
        description="""Harrison's Principles of Internal Medicine classification by Part. Values correspond to the high-level Parts (organ-system or topical groupings) of Harrison's 21st edition (2022). The slot is named `harrisons_chapter` for historical reasons, but the controlled vocabulary lives at the Part level since this is the granularity that matches how curators classify disorders. A single disease may be assigned to multiple Parts (e.g., a hereditary skin disorder could be tagged DERMATOLOGY and GENETICS_ENVIRONMENT_DISEASE). Free-text values used in earlier curation are preserved as `aliases` on the closest-fit Part so that legacy entries continue to validate.""",
    )

class LysosomalStorageEnum(EnumDefinitionImpl):
    """
    Classification of lysosomal storage diseases by accumulated substrate type. Values link to MONDO disease grouping
    terms.
    """
    sphingolipidosis = PermissibleValue(
        text="sphingolipidosis",
        description="Accumulation of sphingolipids (Gaucher, Fabry, Niemann-Pick, Krabbe, etc.)",
        meaning=MONDO["0019255"])
    mucopolysaccharidosis = PermissibleValue(
        text="mucopolysaccharidosis",
        description="Accumulation of glycosaminoglycans (MPS I through IX)",
        meaning=MONDO["0019249"])
    mucolipidosis = PermissibleValue(
        text="mucolipidosis",
        description="Features of both sphingolipidoses and mucopolysaccharidoses",
        meaning=MONDO["0019248"])
    glycoproteinosis = PermissibleValue(
        text="glycoproteinosis",
        description="Accumulation of glycoproteins (fucosidosis, mannosidosis, sialidosis)",
        meaning=MONDO["0017731"])

    _defn = EnumDefinition(
        name="LysosomalStorageEnum",
        description="""Classification of lysosomal storage diseases by accumulated substrate type. Values link to MONDO disease grouping terms.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "disorder of glycogen metabolism",
            PermissibleValue(
                text="disorder of glycogen metabolism",
                description="""Accumulation of glycogen in tissues (Pompe disease and related glycogen storage diseases)""",
                meaning=MONDO["0002412"]))
        setattr(cls, "neuronal ceroid lipofuscinosis",
            PermissibleValue(
                text="neuronal ceroid lipofuscinosis",
                description="Accumulation of lipofuscin in neurons (Batten disease family)",
                meaning=MONDO["0016295"]))

class MechanisticNosologyEnum(EnumDefinitionImpl):
    """
    Classification of diseases by molecular mechanism or affected cellular system. Tag diseases with their primary
    mechanistic category.
    """
    RASopathy = PermissibleValue(
        text="RASopathy",
        description="RAS/MAPK signaling pathway disorders (Noonan, Costello, CFC, NF1)",
        meaning=MONDO["0021060"])
    ciliopathy = PermissibleValue(
        text="ciliopathy",
        description="Primary cilia structure/function disorders (PKD, Bardet-Biedl, Joubert)",
        meaning=MONDO["0005308"])
    laminopathy = PermissibleValue(
        text="laminopathy",
        description="Nuclear lamina disorders (EDMD, progeria, lipodystrophy)",
        meaning=MONDO["0021106"])
    collagenopathy = PermissibleValue(
        text="collagenopathy",
        description="Collagen synthesis/structure disorders (OI, EDS, Alport)",
        meaning=MONDO["0004603"])
    desmosomopathy = PermissibleValue(
        text="desmosomopathy",
        description="""Desmosomal cell-cell adhesion disorders (Naxos disease, Carvajal syndrome, arrhythmogenic cardiomyopathy, pemphigus, desmosomal palmoplantar keratodermas)""")
    amyloidopathy = PermissibleValue(
        text="amyloidopathy",
        description="""Amyloid protein aggregation disorders (Alzheimer's, CAA, hereditary cerebral amyloid angiopathy)""")
    tauopathy = PermissibleValue(
        text="tauopathy",
        description="Tau protein aggregation disorders (Alzheimer's, PSP, CBD)",
        meaning=MONDO["0005574"])
    synucleinopathy = PermissibleValue(
        text="synucleinopathy",
        description="Alpha-synuclein aggregation disorders (Parkinson's, DLB, MSA)",
        meaning=MONDO["0000510"])

    _defn = EnumDefinition(
        name="MechanisticNosologyEnum",
        description="""Classification of diseases by molecular mechanism or affected cellular system. Tag diseases with their primary mechanistic category.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "mitochondrial disease",
            PermissibleValue(
                text="mitochondrial disease",
                description="Mitochondrial function/genome disorders (MELAS, MERRF, Leigh)",
                meaning=MONDO["0044970"]))
        setattr(cls, "intermediate filament disease",
            PermissibleValue(
                text="intermediate filament disease",
                description="""Intermediate filament structure/aggregation disorders (Alexander disease/GFAP, epidermolysis bullosa simplex/keratins)"""))
        setattr(cls, "proteotoxic disease",
            PermissibleValue(
                text="proteotoxic disease",
                description="""Diseases driven by toxic protein misfolding/aggregation and proteostasis failure (Alexander disease, polyQ disorders)"""))

class IUISCategoryEnum(EnumDefinitionImpl):
    """
    IUIS classification tables for inborn errors of immunity (IEI). Based on IUIS 2022 phenotypic classification.
    """
    _defn = EnumDefinition(
        name="IUISCategoryEnum",
        description="""IUIS classification tables for inborn errors of immunity (IEI). Based on IUIS 2022 phenotypic classification.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "combined immunodeficiency",
            PermissibleValue(
                text="combined immunodeficiency",
                description="""Table 1 - Immunodeficiencies affecting cellular and humoral immunity (SCID, CID, Omenn)""",
                meaning=MONDO["0015131"]))
        setattr(cls, "combined immunodeficiency with syndromic features",
            PermissibleValue(
                text="combined immunodeficiency with syndromic features",
                description="Table 2 - CID with associated or syndromic features (WAS, AT, DiGeorge, CHARGE)"))
        setattr(cls, "predominantly antibody deficiency",
            PermissibleValue(
                text="predominantly antibody deficiency",
                description="""Table 3 - Predominantly antibody deficiencies (XLA, CVID, selective Ig deficiency, hyper-IgM)"""))
        setattr(cls, "immune dysregulation",
            PermissibleValue(
                text="immune dysregulation",
                description="Table 4 - Diseases of immune dysregulation (HLH, ALPS, IPEX, APECED)"))
        setattr(cls, "phagocyte defect",
            PermissibleValue(
                text="phagocyte defect",
                description="Table 5 - Congenital defects of phagocyte number or function (SCN, CGD, LAD)"))
        setattr(cls, "innate immunity defect",
            PermissibleValue(
                text="innate immunity defect",
                description="Table 6 - Defects in intrinsic and innate immunity (MSMD, HSE susceptibility, CMC)"))
        setattr(cls, "autoinflammatory syndrome",
            PermissibleValue(
                text="autoinflammatory syndrome",
                description="Table 7 - Autoinflammatory disorders (FMF, CAPS, TRAPS, HIDS, interferonopathies)",
                meaning=MONDO["0019751"]))
        setattr(cls, "complement deficiency",
            PermissibleValue(
                text="complement deficiency",
                description="Table 8 - Complement deficiencies (C1-C9, MBL, factor H/I/B, properdin)",
                meaning=MONDO["0003832"]))
        setattr(cls, "bone marrow failure",
            PermissibleValue(
                text="bone marrow failure",
                description="Table 9 - Bone marrow failure syndromes (Fanconi, DKC, SDS, DBA)"))
        setattr(cls, "phenocopy of IEI",
            PermissibleValue(
                text="phenocopy of IEI",
                description="Table 10 - Phenocopies of IEI (somatic mutations, autoantibodies to cytokines)"))

class ChannelopathyOrganSystemEnum(EnumDefinitionImpl):
    """
    Classification categories for channelopathies by affected organ system. Tag diseases like Long QT syndrome
    (cardiac), periodic paralysis (skeletal muscle), episodic ataxia (neurological), cystic fibrosis (epithelial).
    """
    _defn = EnumDefinition(
        name="ChannelopathyOrganSystemEnum",
        description="""Classification categories for channelopathies by affected organ system. Tag diseases like Long QT syndrome (cardiac), periodic paralysis (skeletal muscle), episodic ataxia (neurological), cystic fibrosis (epithelial).""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "cardiac channelopathy",
            PermissibleValue(
                text="cardiac channelopathy",
                description="Ion channel disorders primarily affecting cardiac rhythm (Long QT, Brugada, CPVT)"))
        setattr(cls, "skeletal muscle channelopathy",
            PermissibleValue(
                text="skeletal muscle channelopathy",
                description="Ion channel disorders causing episodic weakness or myotonia"))
        setattr(cls, "neurological channelopathy",
            PermissibleValue(
                text="neurological channelopathy",
                description="Ion channel disorders affecting CNS (episodic ataxia, epilepsy, migraine)"))
        setattr(cls, "epithelial channelopathy",
            PermissibleValue(
                text="epithelial channelopathy",
                description="Ion channel disorders affecting epithelial transport (cystic fibrosis)"))

class PhenotypeCategoryEnum(EnumDefinitionImpl):
    """
    Broad phenotype categories from the Human Phenotype Ontology. Each value corresponds to a direct child of
    HP:0000118 (Phenotypic abnormality).
    """
    Blood = PermissibleValue(
        text="Blood",
        title="Abnormality of blood and blood-forming tissues",
        description="""Abnormalities of the hematopoietic system including anemias, coagulopathies, and leukocyte disorders""",
        meaning=HP["0001871"])
    Breast = PermissibleValue(
        text="Breast",
        title="Abnormality of the breast",
        description="Abnormalities of breast development, morphology, or function",
        meaning=HP["0000769"])
    Cardiovascular = PermissibleValue(
        text="Cardiovascular",
        title="Abnormality of the cardiovascular system",
        description="Abnormalities of the heart and vasculature",
        meaning=HP["0001626"])
    Digestive = PermissibleValue(
        text="Digestive",
        title="Abnormality of the digestive system",
        description="Abnormalities of the gastrointestinal tract, liver, and pancreas",
        meaning=HP["0025031"])
    Ear = PermissibleValue(
        text="Ear",
        title="Abnormality of the ear",
        description="Abnormalities of ear morphology or hearing",
        meaning=HP["0000598"])
    Endocrine = PermissibleValue(
        text="Endocrine",
        title="Abnormality of the endocrine system",
        description="Abnormalities of hormone-producing glands and endocrine regulation",
        meaning=HP["0000818"])
    Eye = PermissibleValue(
        text="Eye",
        title="Abnormality of the eye",
        description="Abnormalities of the eye and visual system",
        meaning=HP["0000478"])
    Genitourinary = PermissibleValue(
        text="Genitourinary",
        title="Abnormality of the genitourinary system",
        description="Abnormalities of the kidneys, urinary tract, and reproductive organs",
        meaning=HP["0000119"])
    Immune = PermissibleValue(
        text="Immune",
        title="Abnormality of the immune system",
        description="Abnormalities of innate or adaptive immunity",
        meaning=HP["0002715"])
    Integument = PermissibleValue(
        text="Integument",
        title="Abnormality of the integument",
        description="Abnormalities of skin, hair, nails, and sweat glands",
        meaning=HP["0001574"])
    Limbs = PermissibleValue(
        text="Limbs",
        title="Abnormality of limbs",
        description="Abnormalities of upper or lower limb structure",
        meaning=HP["0040064"])
    Metabolism = PermissibleValue(
        text="Metabolism",
        title="Abnormality of metabolism/homeostasis",
        description="Abnormalities of metabolic processes and biochemical homeostasis",
        meaning=HP["0001939"])
    Musculoskeletal = PermissibleValue(
        text="Musculoskeletal",
        title="Abnormality of the musculoskeletal system",
        description="Abnormalities of bones, joints, muscles, and connective tissue",
        meaning=HP["0033127"])
    Respiratory = PermissibleValue(
        text="Respiratory",
        title="Abnormality of the respiratory system",
        description="Abnormalities of the airways, lungs, and respiratory function",
        meaning=HP["0002086"])
    Voice = PermissibleValue(
        text="Voice",
        title="Abnormality of the voice",
        description="Abnormalities of voice production and quality",
        meaning=HP["0001608"])
    Cellular = PermissibleValue(
        text="Cellular",
        title="Abnormal cellular phenotype",
        description="Abnormalities at the cellular level including cell morphology and behavior",
        meaning=HP["0025354"])
    Constitutional = PermissibleValue(
        text="Constitutional",
        title="Constitutional symptom",
        description="Systemic symptoms such as fever, fatigue, and weight loss",
        meaning=HP["0025142"])
    Growth = PermissibleValue(
        text="Growth",
        title="Growth abnormality",
        description="Abnormalities of growth including short stature, tall stature, and growth delay",
        meaning=HP["0001507"])
    Neoplasm = PermissibleValue(
        text="Neoplasm",
        title="Neoplasm",
        description="Benign or malignant neoplasms (tumors)",
        meaning=HP["0002664"])

    _defn = EnumDefinition(
        name="PhenotypeCategoryEnum",
        description="""Broad phenotype categories from the Human Phenotype Ontology. Each value corresponds to a direct child of HP:0000118 (Phenotypic abnormality).""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Head and Neck",
            PermissibleValue(
                text="Head and Neck",
                title="Abnormality of head or neck",
                description="Abnormalities of craniofacial structures and the neck",
                meaning=HP["0000152"]))
        setattr(cls, "Nervous System",
            PermissibleValue(
                text="Nervous System",
                title="Abnormality of the nervous system",
                description="Abnormalities of the central and peripheral nervous system",
                meaning=HP["0000707"]))
        setattr(cls, "Prenatal and Birth",
            PermissibleValue(
                text="Prenatal and Birth",
                title="Abnormality of prenatal development or birth",
                description="Abnormalities arising during prenatal development or at birth",
                meaning=HP["0001197"]))
        setattr(cls, "Thoracic Cavity",
            PermissibleValue(
                text="Thoracic Cavity",
                title="Abnormality of the thoracic cavity",
                description="Abnormalities of thoracic structures (pleura, mediastinum, diaphragm)",
                meaning=HP["0045027"]))

class ICIMDEnum(EnumDefinitionImpl):
    """
    ICIMD category (layer 1) and disease group (layer 2) assignments. Groups point to their parent category via
    ``is_a``. See the schema-level description for provenance and the assign-most-specific rule.
    """
    amino_acid_metabolism = PermissibleValue(
        text="amino_acid_metabolism",
        description="""ICIMD category 1: Disorders of amino acid metabolism (super-domain: intermediary metabolism — nutrients). Enzyme deficiencies of amino acid pathways, frequently causing accumulation of toxic metabolites.""")
    branched_chain_amino_acids = PermissibleValue(
        text="branched_chain_amino_acids",
        description="Disorders of branched-chain amino acid (leucine, isoleucine, valine) metabolism.")
    phe_and_tyr = PermissibleValue(
        text="phe_and_tyr",
        description="Disorders of phenylalanine and tyrosine metabolism.")
    sulfur_containing_amino_acids = PermissibleValue(
        text="sulfur_containing_amino_acids",
        description="Disorders of sulfur-containing amino acid (methionine, homocysteine, cysteine) metabolism.")
    gly_and_ser = PermissibleValue(
        text="gly_and_ser",
        description="Disorders of glycine and serine metabolism.")
    orn_pro_and_hyp = PermissibleValue(
        text="orn_pro_and_hyp",
        description="Disorders of ornithine, proline and hydroxyproline metabolism.")
    lys_hyl_and_trp = PermissibleValue(
        text="lys_hyl_and_trp",
        description="Disorders of lysine, hydroxylysine and tryptophan metabolism.")
    glu_gln_and_asp_asn = PermissibleValue(
        text="glu_gln_and_asp_asn",
        description="Disorders of glutamate/glutamine and aspartate/asparagine metabolism.")
    histidine_metabolism = PermissibleValue(
        text="histidine_metabolism",
        description="Disorders of histidine metabolism.")
    organic_acidurias = PermissibleValue(
        text="organic_acidurias",
        description="""Organic acidurias — deficiencies of mitochondrial enzymes for breakdown of CoA-activated small carboxylic acids, mostly from amino acid deamination.""")
    urea_cycle_and_hyperammonemias = PermissibleValue(
        text="urea_cycle_and_hyperammonemias",
        description="Urea cycle disorders and other hyperammonemias.")
    amino_acid_transport = PermissibleValue(
        text="amino_acid_transport",
        description="Disorders of amino acid transport.")
    amino_acids_other = PermissibleValue(
        text="amino_acids_other",
        description="Other disorders of amino acid metabolism.")
    peptide_and_amine_metabolism = PermissibleValue(
        text="peptide_and_amine_metabolism",
        description="""ICIMD category 2: Disorders of peptide and amine metabolism (super-domain: intermediary metabolism — nutrients).""")
    glutathione_metabolism = PermissibleValue(
        text="glutathione_metabolism",
        description="Disorders of glutathione biosynthesis and regeneration.")
    peptides_other = PermissibleValue(
        text="peptides_other",
        description="Other peptide disorders, including dipeptidase deficiencies.")
    methylamine_metabolism = PermissibleValue(
        text="methylamine_metabolism",
        description="Disorders of methylamine metabolism.")
    polyamine_metabolism = PermissibleValue(
        text="polyamine_metabolism",
        description="Disorders of polyamine metabolism.")
    carbohydrate_metabolism = PermissibleValue(
        text="carbohydrate_metabolism",
        description="""ICIMD category 3: Disorders of carbohydrate metabolism (super-domain: intermediary metabolism — nutrients).""")
    galactose_and_fructose = PermissibleValue(
        text="galactose_and_fructose",
        description="Disorders of galactose and fructose metabolism.")
    gluconeogenesis = PermissibleValue(
        text="gluconeogenesis",
        description="Disorders of gluconeogenesis (including pyruvate carboxylase deficiency).")
    glycolysis = PermissibleValue(
        text="glycolysis",
        description="Disorders of glycolysis.")
    glycogen_metabolism = PermissibleValue(
        text="glycogen_metabolism",
        description="Disorders of glycogen metabolism (glycogen storage diseases).")
    pentose_polyol_metabolism = PermissibleValue(
        text="pentose_polyol_metabolism",
        description="Disorders of pentose and polyol metabolism.")
    carbohydrate_transport_and_absorption = PermissibleValue(
        text="carbohydrate_transport_and_absorption",
        description="Disorders of carbohydrate (hexose) transmembrane transport and absorption.")
    fatty_acid_and_ketone_body_metabolism = PermissibleValue(
        text="fatty_acid_and_ketone_body_metabolism",
        description="""ICIMD category 4: Disorders of fatty acid and ketone body metabolism (super-domain: intermediary metabolism — nutrients).""")
    carnitine_metabolism = PermissibleValue(
        text="carnitine_metabolism",
        description="Disorders of carnitine metabolism.")
    mitochondrial_fatty_acid_oxidation = PermissibleValue(
        text="mitochondrial_fatty_acid_oxidation",
        description="Disorders of mitochondrial fatty acid oxidation.")
    ketone_body_metabolism = PermissibleValue(
        text="ketone_body_metabolism",
        description="Disorders of ketone body synthesis, breakdown and transport.")
    energy_substrate_metabolism = PermissibleValue(
        text="energy_substrate_metabolism",
        description="""ICIMD category 5: Disorders of energy substrate metabolism (super-domain: intermediary metabolism — energy).""")
    pyruvate_metabolism = PermissibleValue(
        text="pyruvate_metabolism",
        description="Disorders of pyruvate metabolism.")
    krebs_cycle = PermissibleValue(
        text="krebs_cycle",
        description="Disorders of the Krebs (tricarboxylic acid) cycle.")
    creatine_metabolism = PermissibleValue(
        text="creatine_metabolism",
        description="Disorders of creatine metabolism.")
    mitochondrial_dna_related_disorders = PermissibleValue(
        text="mitochondrial_dna_related_disorders",
        description="""ICIMD category 6: Mitochondrial DNA-related disorders (super-domain: intermediary metabolism — energy).""")
    mtdna_encoded_respiratory_chain_proteins = PermissibleValue(
        text="mtdna_encoded_respiratory_chain_proteins",
        description="Disorders of the 13 mtDNA protein-coding (respiratory chain) genes.")
    mtdna_encoded_trna_rrna = PermissibleValue(
        text="mtdna_encoded_trna_rrna",
        description="Disorders of mtDNA-encoded tRNA and rRNA genes.")
    single_large_scale_mtdna_deletions = PermissibleValue(
        text="single_large_scale_mtdna_deletions",
        description="Disorders associated with single large-scale mtDNA deletions.")
    nuclear_encoded_oxidative_phosphorylation = PermissibleValue(
        text="nuclear_encoded_oxidative_phosphorylation",
        description="""ICIMD category 7: Nuclear-encoded disorders of oxidative phosphorylation (super-domain: intermediary metabolism — energy).""")
    complex_i_subunits_and_assembly_factors = PermissibleValue(
        text="complex_i_subunits_and_assembly_factors",
        description="Nuclear-encoded complex I subunit and assembly factor defects.")
    complex_ii_subunits_and_assembly_factors = PermissibleValue(
        text="complex_ii_subunits_and_assembly_factors",
        description="Nuclear-encoded complex II subunit and assembly factor defects.")
    complex_iii_subunits_and_assembly_factors = PermissibleValue(
        text="complex_iii_subunits_and_assembly_factors",
        description="Nuclear-encoded complex III subunit and assembly factor defects.")
    complex_iv_subunits_and_assembly_factors = PermissibleValue(
        text="complex_iv_subunits_and_assembly_factors",
        description="Nuclear-encoded complex IV subunit and assembly factor defects.")
    complex_v_subunits_and_assembly_factors = PermissibleValue(
        text="complex_v_subunits_and_assembly_factors",
        description="Nuclear-encoded complex V subunit and assembly factor defects.")
    mitochondrial_cofactor_biosynthesis = PermissibleValue(
        text="mitochondrial_cofactor_biosynthesis",
        description="""ICIMD category 8: Disorders of mitochondrial cofactor biosynthesis (super-domain: intermediary metabolism — energy).""")
    coenzyme_q10_biosynthesis = PermissibleValue(
        text="coenzyme_q10_biosynthesis",
        description="Disorders of coenzyme Q10 (ubiquinone) biosynthesis.")
    lipoic_acid_and_iron_sulfur = PermissibleValue(
        text="lipoic_acid_and_iron_sulfur",
        description="Disorders of lipoic acid and iron-sulfur cluster biosynthesis.")
    cytochrome_c = PermissibleValue(
        text="cytochrome_c",
        description="Disorders of cytochrome c.")
    mitochondrial_dna_maintenance_and_replication = PermissibleValue(
        text="mitochondrial_dna_maintenance_and_replication",
        description="""ICIMD category 9: Disorders of mitochondrial DNA maintenance and replication (super-domain: intermediary metabolism — energy).""")
    nucleotide_pool_maintenance = PermissibleValue(
        text="nucleotide_pool_maintenance",
        description="Disorders of mitochondrial nucleotide pool maintenance.")
    mtdna_replication_and_maintenance = PermissibleValue(
        text="mtdna_replication_and_maintenance",
        description="Disorders of mtDNA replication and maintenance.")
    mitochondrial_gene_expression = PermissibleValue(
        text="mitochondrial_gene_expression",
        description="""ICIMD category 10: Disorders of mitochondrial gene expression (super-domain: intermediary metabolism — energy).""")
    mtdna_transcript_processing_and_modification = PermissibleValue(
        text="mtdna_transcript_processing_and_modification",
        description="Disorders of mtDNA transcript processing and modification.")
    mitochondrial_aminoacyl_trna_synthetases = PermissibleValue(
        text="mitochondrial_aminoacyl_trna_synthetases",
        description="Disorders of mitochondrial aminoacyl-tRNA synthetases.")
    mitoribosome = PermissibleValue(
        text="mitoribosome",
        description="Disorders of the mitoribosome.")
    other_mitochondrial_function = PermissibleValue(
        text="other_mitochondrial_function",
        description="""ICIMD category 11: Other disorders of mitochondrial function (super-domain: intermediary metabolism — energy).""")
    mitochondrial_shuttles_and_carriers = PermissibleValue(
        text="mitochondrial_shuttles_and_carriers",
        description="Disorders of mitochondrial shuttles and carriers.")
    mitochondrial_protein_import = PermissibleValue(
        text="mitochondrial_protein_import",
        description="Disorders of mitochondrial protein import.")
    mitochondrial_protein_quality_control = PermissibleValue(
        text="mitochondrial_protein_quality_control",
        description="Disorders of mitochondrial protein quality control.")
    mitochondrial_dysfunction_miscellaneous = PermissibleValue(
        text="mitochondrial_dysfunction_miscellaneous",
        description="Miscellaneous mitochondrial disorders not fitting other groups.")
    metabolite_repair_proofreading = PermissibleValue(
        text="metabolite_repair_proofreading",
        description="""ICIMD category 12: Disorders of metabolite repair/proofreading (super-domain: intermediary metabolism — other).""")
    metabolite_proofreading = PermissibleValue(
        text="metabolite_proofreading",
        description="""Disorders of metabolite proofreading, addressing the promiscuity of certain intermediary-metabolism enzymes.""")
    miscellaneous_intermediary_metabolism = PermissibleValue(
        text="miscellaneous_intermediary_metabolism",
        description="""ICIMD category 13: Miscellaneous disorders of intermediary metabolism (super-domain: intermediary metabolism — other).""")
    glyoxylate_and_oxalate = PermissibleValue(
        text="glyoxylate_and_oxalate",
        description="Disorders of glyoxylate and oxalate metabolism.")
    intermediary_metabolism_miscellaneous = PermissibleValue(
        text="intermediary_metabolism_miscellaneous",
        description="Other miscellaneous disorders of intermediary metabolism.")
    lipid_metabolism = PermissibleValue(
        text="lipid_metabolism",
        description="""ICIMD category 14: Disorders of lipid metabolism (super-domain: lipid metabolism and transport); follows the LIPID MAPS lipid classification.""")
    fatty_acyl_synthesis_elongation_and_recycling = PermissibleValue(
        text="fatty_acyl_synthesis_elongation_and_recycling",
        description="Disorders of fatty acyl synthesis, elongation, and recycling.")
    peroxisomal_fatty_acid_oxidation = PermissibleValue(
        text="peroxisomal_fatty_acid_oxidation",
        description="Disorders of peroxisomal fatty acid oxidation.")
    eicosanoid_metabolism = PermissibleValue(
        text="eicosanoid_metabolism",
        description="Disorders of eicosanoid metabolism.")
    glycerolipid_metabolism = PermissibleValue(
        text="glycerolipid_metabolism",
        description="Disorders of glycerolipid metabolism.")
    glycerophospholipid_metabolism = PermissibleValue(
        text="glycerophospholipid_metabolism",
        description="Disorders of glycerophospholipid metabolism.")
    sphingolipid_synthesis_and_recycling = PermissibleValue(
        text="sphingolipid_synthesis_and_recycling",
        description="Disorders of sphingolipid synthesis and recycling.")
    sterol_metabolism = PermissibleValue(
        text="sterol_metabolism",
        description="Disorders of sterol metabolism.")
    bile_acid_metabolism = PermissibleValue(
        text="bile_acid_metabolism",
        description="Disorders of bile acid metabolism.")
    lipoprotein_metabolism = PermissibleValue(
        text="lipoprotein_metabolism",
        description="""ICIMD category 15: Disorders of lipoprotein metabolism (super-domain: lipid metabolism and transport).""")
    hypercholesterolemias = PermissibleValue(
        text="hypercholesterolemias",
        description="Hypercholesterolemias.")
    hypertriglyceridemias = PermissibleValue(
        text="hypertriglyceridemias",
        description="Hypertriglyceridemias.")
    mixed_hyperlipidemias = PermissibleValue(
        text="mixed_hyperlipidemias",
        description="Mixed hyperlipidemias.")
    hdl_metabolism = PermissibleValue(
        text="hdl_metabolism",
        description="Disorders of high-density lipoprotein (HDL) metabolism.")
    decreased_ldl_triglycerides = PermissibleValue(
        text="decreased_ldl_triglycerides",
        description="Disorders with decreased LDL and/or triglycerides.")
    lipoproteins_other = PermissibleValue(
        text="lipoproteins_other",
        description="Other disorders of lipoprotein metabolism.")
    nucleobase_nucleotide_nucleic_acid_metabolism = PermissibleValue(
        text="nucleobase_nucleotide_nucleic_acid_metabolism",
        description="""ICIMD category 16: Disorders of nucleobase, nucleotide and nucleic acid metabolism (super-domain: metabolism of heterocyclic compounds).""")
    purine_metabolism = PermissibleValue(
        text="purine_metabolism",
        description="Disorders of purine metabolism.")
    pyrimidine_metabolism = PermissibleValue(
        text="pyrimidine_metabolism",
        description="Disorders of pyrimidine metabolism.")
    ectonucleotides_and_nucleic_acids = PermissibleValue(
        text="ectonucleotides_and_nucleic_acids",
        description="Disorders of ectonucleotides and nucleic acids.")
    non_mitochondrial_trna_metabolism = PermissibleValue(
        text="non_mitochondrial_trna_metabolism",
        description="Disorders of non-mitochondrial tRNA metabolism.")
    ribosomal_biogenesis = PermissibleValue(
        text="ribosomal_biogenesis",
        description="Disorders of ribosomal biogenesis (non-mitochondrial rRNA metabolism).")
    tetrapyrrole_metabolism = PermissibleValue(
        text="tetrapyrrole_metabolism",
        description="""ICIMD category 17: Disorders of tetrapyrrole metabolism (super-domain: metabolism of heterocyclic compounds).""")
    heme_synthesis_and_porphyrias = PermissibleValue(
        text="heme_synthesis_and_porphyrias",
        description="Disorders of heme biosynthesis (porphyrias).")
    heme_degradation_and_bilirubin = PermissibleValue(
        text="heme_degradation_and_bilirubin",
        description="Disorders of heme breakdown (biliverdin and bilirubin).")
    congenital_disorders_of_glycosylation = PermissibleValue(
        text="congenital_disorders_of_glycosylation",
        description="""ICIMD category 18: Congenital disorders of glycosylation (super-domain: complex molecule and organelle metabolism).""")
    n_linked_protein_glycosylation = PermissibleValue(
        text="n_linked_protein_glycosylation",
        description="Disorders of N-linked protein glycosylation.")
    o_linked_protein_glycosylation = PermissibleValue(
        text="o_linked_protein_glycosylation",
        description="Disorders of O-linked protein glycosylation (including glycosaminoglycan synthesis).")
    lipid_glycosylation = PermissibleValue(
        text="lipid_glycosylation",
        description="Disorders of lipid glycosylation (including glycosylphosphatidylinositol biosynthesis).")
    multiple_glycosylation_pathways = PermissibleValue(
        text="multiple_glycosylation_pathways",
        description="""Disorders affecting multiple glycosylation pathways (dolichol metabolism, Golgi transport and homeostasis, sialic acid metabolism).""")
    other_glycan_metabolism = PermissibleValue(
        text="other_glycan_metabolism",
        description="Other disorders of glycan metabolism.")
    organelle_biogenesis_dynamics_and_interactions = PermissibleValue(
        text="organelle_biogenesis_dynamics_and_interactions",
        description="""ICIMD category 19: Disorders of organelle biogenesis, dynamics and interactions (super-domain: complex molecule and organelle metabolism).""")
    mitochondrial_membrane_biogenesis_and_remodeling = PermissibleValue(
        text="mitochondrial_membrane_biogenesis_and_remodeling",
        description="Disorders of mitochondrial membrane biogenesis and remodeling.")
    mitochondrial_and_peroxisomal_dynamics = PermissibleValue(
        text="mitochondrial_and_peroxisomal_dynamics",
        description="Disorders of mitochondrial and peroxisomal dynamics.")
    peroxisomal_biogenesis = PermissibleValue(
        text="peroxisomal_biogenesis",
        description="Peroxisomal biogenesis disorders (peroxin-related).")
    lysosome_related_organelle_biogenesis = PermissibleValue(
        text="lysosome_related_organelle_biogenesis",
        description="Disorders of lysosome-related organelle biogenesis.")
    organelle_interplay = PermissibleValue(
        text="organelle_interplay",
        description="Disorders of organelle interplay.")
    vesicular_trafficking = PermissibleValue(
        text="vesicular_trafficking",
        description="Disorders of vesicular trafficking.")
    complex_molecule_degradation = PermissibleValue(
        text="complex_molecule_degradation",
        description="""ICIMD category 20: Disorders of complex molecule degradation (super-domain: complex molecule and organelle metabolism); the classical lysosomal disorders.""")
    sphingolipid_degradation = PermissibleValue(
        text="sphingolipid_degradation",
        description="Disorders of sphingolipid degradation (sphingolipidoses).")
    glycosaminoglycan_degradation = PermissibleValue(
        text="glycosaminoglycan_degradation",
        description="Disorders of glycosaminoglycan degradation (mucopolysaccharidoses).")
    glycoprotein_degradation = PermissibleValue(
        text="glycoprotein_degradation",
        description="Disorders of glycoprotein degradation.")
    neuronal_ceroid_lipofuscinosis = PermissibleValue(
        text="neuronal_ceroid_lipofuscinosis",
        description="Neuronal ceroid lipofuscinoses.")
    autophagy = PermissibleValue(
        text="autophagy",
        description="Disorders of autophagy.")
    complex_molecule_degradation_other = PermissibleValue(
        text="complex_molecule_degradation_other",
        description="Other disorders of complex molecule degradation.")
    vitamin_and_cofactor_metabolism = PermissibleValue(
        text="vitamin_and_cofactor_metabolism",
        description="""ICIMD category 21: Disorders of vitamin and cofactor metabolism (super-domain: cofactor and mineral metabolism).""")
    tetrahydrobiopterin_metabolism = PermissibleValue(
        text="tetrahydrobiopterin_metabolism",
        description="Disorders of tetrahydrobiopterin metabolism.")
    thiamine_metabolism = PermissibleValue(
        text="thiamine_metabolism",
        description="Disorders of thiamine (vitamin B1) metabolism.")
    riboflavin_metabolism = PermissibleValue(
        text="riboflavin_metabolism",
        description="Disorders of riboflavin (vitamin B2) metabolism.")
    niacin_and_nad_metabolism = PermissibleValue(
        text="niacin_and_nad_metabolism",
        description="Disorders of niacin/nicotinamide (vitamin B3) and NAD metabolism.")
    pantothenate_and_coa_metabolism = PermissibleValue(
        text="pantothenate_and_coa_metabolism",
        description="Disorders of pantothenate (vitamin B5) and coenzyme A metabolism.")
    pyridoxine_metabolism = PermissibleValue(
        text="pyridoxine_metabolism",
        description="Disorders of pyridoxine (vitamin B6) metabolism.")
    biotin_metabolism = PermissibleValue(
        text="biotin_metabolism",
        description="Disorders of biotin (vitamin B7) metabolism.")
    folate_metabolism = PermissibleValue(
        text="folate_metabolism",
        description="Disorders of folate (vitamin B9) metabolism.")
    cobalamin_metabolism = PermissibleValue(
        text="cobalamin_metabolism",
        description="Disorders of cobalamin (vitamin B12) metabolism.")
    molybdenum_cofactor_metabolism = PermissibleValue(
        text="molybdenum_cofactor_metabolism",
        description="Disorders of molybdenum cofactor metabolism.")
    vitamins_other = PermissibleValue(
        text="vitamins_other",
        description="Other disorders of vitamin and cofactor metabolism.")
    trace_elements_and_metals = PermissibleValue(
        text="trace_elements_and_metals",
        description="""ICIMD category 22: Disorders of trace elements and metals (super-domain: cofactor and mineral metabolism).""")
    copper_metabolism = PermissibleValue(
        text="copper_metabolism",
        description="Disorders of copper metabolism.")
    iron_metabolism = PermissibleValue(
        text="iron_metabolism",
        description="Disorders of iron metabolism.")
    manganese_metabolism = PermissibleValue(
        text="manganese_metabolism",
        description="Disorders of manganese metabolism.")
    zinc_metabolism = PermissibleValue(
        text="zinc_metabolism",
        description="Disorders of zinc metabolism.")
    trace_element_other = PermissibleValue(
        text="trace_element_other",
        description="Other disorders of trace element and metal metabolism.")
    neurotransmitter_disorders = PermissibleValue(
        text="neurotransmitter_disorders",
        description="ICIMD category 23: Neurotransmitter disorders (super-domain: metabolic cell signaling).")
    monoamine_metabolism = PermissibleValue(
        text="monoamine_metabolism",
        description="Disorders of monoamine neurotransmitter metabolism.")
    gaba_metabolism = PermissibleValue(
        text="gaba_metabolism",
        description="Disorders of GABA metabolism.")
    glutamate_neurotransmission = PermissibleValue(
        text="glutamate_neurotransmission",
        description="Disorders of glutamate neurotransmitter function.")
    glycine_neurotransmission = PermissibleValue(
        text="glycine_neurotransmission",
        description="Disorders of glycine neurotransmitter function.")
    choline_metabolism = PermissibleValue(
        text="choline_metabolism",
        description="Disorders of choline metabolism.")
    synaptic_vesicle_cycle = PermissibleValue(
        text="synaptic_vesicle_cycle",
        description="Disorders of the synaptic vesicle cycle.")
    endocrine_metabolic_disorders = PermissibleValue(
        text="endocrine_metabolic_disorders",
        description="ICIMD category 24: Endocrine metabolic disorders (super-domain: metabolic cell signaling).")
    insulin_metabolism = PermissibleValue(
        text="insulin_metabolism",
        description="Disorders affecting insulin metabolism.")
    steroid_hormone_metabolism = PermissibleValue(
        text="steroid_hormone_metabolism",
        description="Disorders of steroid hormone metabolism.")

    _defn = EnumDefinition(
        name="ICIMDEnum",
        description="""ICIMD category (layer 1) and disease group (layer 2) assignments. Groups point to their parent category via ``is_a``. See the schema-level description for provenance and the assign-most-specific rule.""",
    )

class ISDSNosologyGroupEnum(EnumDefinitionImpl):
    """
    The 41 groups of the ISDS Nosology of Genetic Skeletal Disorders, 2023 revision (PMID:36779427), plus four groups
    deprecated from the 2019 revision (PMID:31633310) that the 2023 revision dissolved. Values are ordered by their
    2023 group number; each description opens with that number and records the 2019 number where it differed.
    """
    fgfr3_chondrodysplasia = PermissibleValue(
        text="fgfr3_chondrodysplasia",
        description="""Group 1 (2023 revision): FGFR3 chondrodysplasias. Disorders caused by gain-of-function (and, for CATSHL, loss-of-function) variation in FGFR3 — thanatophoric dysplasia types 1 and 2, SADDAN, achondroplasia, hypochondroplasia, CATSHL syndrome. FGFR3-related craniosynostosis is listed in group 34 and LADD syndrome in group 40 instead.""")
    type_2_collagen = PermissibleValue(
        text="type_2_collagen",
        description="""Group 2 (2023 revision): Type 2 collagen disorders. COL2A1-related type II collagenopathies spanning a lethal-to-mild continuum — achondrogenesis type 2, hypochondrogenesis, platyspondylic dysplasia Torrance type, spondyloepiphyseal dysplasia congenita, SEMD Strudwick type, Kniest dysplasia, spondyloperipheral dysplasia, Czech dysplasia, Stickler syndrome type 1.""")
    type_11_collagen = PermissibleValue(
        text="type_11_collagen",
        description="""Group 3 (2023 revision): Type 11 collagen disorders. COL11A1/COL11A2 disorders — Stickler syndrome types 2 and 3, Marshall syndrome, fibrochondrogenesis, otospondylomegaepiphyseal dysplasia (OSMED, recessive and dominant/Weissenbacher-Zweymuller types).""")
    sulphation_disorders = PermissibleValue(
        text="sulphation_disorders",
        description="""Group 4 (2023 revision): Sulfation disorders. Defects of sulfate transport and proteoglycan sulfation — SLC26A2 (achondrogenesis type 1B, atelosteogenesis type 2, diastrophic dysplasia, recessive MED), PAPSS2 (SEMD PAPSS2 type, recessive brachyolmia), IMPAD1, CHST3 (chondrodysplasia with congenital joint dislocations), and CHST14/DSE (musculocontractural Ehlers-Danlos syndrome).""")
    dysplasias_with_multiple_joint_dislocations = PermissibleValue(
        text="dysplasias_with_multiple_joint_dislocations",
        description="""Group 5 (2023 revision): Dysplasias with multiple joint dislocations. Largely proteoglycan-biosynthesis (linkeropathy) disorders — Desbuquois dysplasia types 1 and 2 (CANT1, XYLT1), spondyloepimetaphyseal dysplasia with joint laxity (KIF22, B3GALT6, EXOC6B), CSGALNACT1 and B3GAT3 deficiency, pseudodiastrophic dysplasia, the kyphoscoliotic Ehlers-Danlos syndromes (PLOD1, FKBP14), and spondylodysplastic Ehlers-Danlos syndrome types 1 and 2 (B4GALT7, B3GALT6) — type 3 (SLC39A13) is in group 13 instead, so a dismech entry covering all three needs both values. Was group 20 in the 2019 revision.""")
    filamin_and_related = PermissibleValue(
        text="filamin_and_related",
        description="""Group 6 (2023 revision): Filamins and related disorders. FLNA/FLNB filaminopathies and mechanistically allied conditions — frontometaphyseal dysplasia (FLNA, MAP3K7, TAB2), Melnick-Needles syndrome, otopalatodigital syndromes types 1 and 2, terminal osseous dysplasia, atelosteogenesis types 1 and 3, dominant Larsen syndrome, spondylocarpotarsal synostosis (FLNB, MYH3), Frank-ter Haar syndrome (SH3PXD2B), cardiospondylocarpofacial syndrome (MAP3K7). Was group 7 in the 2019 revision.""")
    proteoglycan_core_protein_disorders = PermissibleValue(
        text="proteoglycan_core_protein_disorders",
        description="""Group 7 (2023 revision): Proteoglycan core proteins disorders. Disorders of the core proteins of cartilage proteoglycans, formed in the 2023 revision by merging the former Perlecan (HSPG2 - dyssegmental dysplasia, Schwartz-Jampel syndrome) and Aggrecan (ACAN - SED Kimberley type, SEMD aggrecan type, short stature with advanced bone age) groups, and additionally holding the biglycan (BGN) entry, SEMD Camera type — the revision's only BGN row, which is why the BGN-related Meester-Loeys syndrome is not in group 31. Distinct from the sulfation/linkeropathy disorders of group 4, which affect glycosaminoglycan chain synthesis rather than the core protein. Has no single counterpart in the 2019 revision: it fuses two of them.""")
    trpv4 = PermissibleValue(
        text="trpv4",
        description="""Group 8 (2023 revision): TRPV4 disorders. TRPV4 skeletal channelopathies spanning a severity continuum — metatropic dysplasia, SED Maroteaux type, spondylometaphyseal dysplasia Kozlowski type, autosomal dominant brachyolmia, familial digital arthropathy-brachydactyly.""")
    multiple_epiphyseal_dysplasia_and_pseudoachondroplasia = PermissibleValue(
        text="multiple_epiphyseal_dysplasia_and_pseudoachondroplasia",
        description="""Group 9 (2023 revision): Pseudoachondroplasia and the multiple epiphyseal dysplasias. COMP, MATN3, and type IX collagen (COL9A1/2/3) disorders — pseudoachondroplasia, dominant multiple epiphyseal dysplasia, recessive Stickler syndrome. Also holds Lowry-Wood syndrome, NOS 09-0110 \"Multiple epiphyseal dysplasia with microcephaly and nystagmus (Lowry-Wood syndrome), RNU4ATAC-related\" (OMIM 226960), which the 2023 revision moved here from the primordial dwarfism and slender bones group — see that group's description. Was group 10 in the 2019 revision.""")
    ciliopathies_with_major_skeletal_involvement = PermissibleValue(
        text="ciliopathies_with_major_skeletal_involvement",
        description="""Group 10 (2023 revision): Skeletal disorders caused by abnormalities of cilia or ciliary signaling. Skeletal ciliopathies caused by intraflagellar-transport and basal-body defects — chondroectodermal dysplasia (Ellis-van Creveld), short-rib-polydactyly syndromes types 1-5, asphyxiating thoracic dysplasia (Jeune), cranioectodermal dysplasia (Levin-Sensenbrenner), Mainzer-Saldino syndrome, axial spondylometaphyseal dysplasia, orofaciodigital syndrome types 2 and 4, thoracolaryngopelvic dysplasia. Weyers acrofacial (acrodental) dysostosis is listed in group 35 instead. Was group 9 in the 2019 revision.""")
    metaphyseal_dysplasias = PermissibleValue(
        text="metaphyseal_dysplasias",
        description="""Group 11 (2023 revision): Metaphyseal dysplasias. Disorders with predominantly metaphyseal change — metaphyseal dysplasia Schmid type (COL10A1), cartilage-hair hypoplasia (RMRP), the CHH-like short-stature dysplasias (POP1, NEPRO), Shwachman-Diamond syndrome (SBDS, EFL1, DNAJC21, SRP54), metaphyseal dysplasia Spahr and metaphyseal anadysplasia (MMP13, MMP9), metaphyseal dysplasia with maxillary hypoplasia (RUNX2).""")
    spondylometaphyseal_dysplasias = PermissibleValue(
        text="spondylometaphyseal_dysplasias",
        description="""Group 12 (2023 revision): Spondylometaphyseal dysplasias (SMD). Combined vertebral and metaphyseal involvement. The group has exactly six members, NOS 12-0010 to 12-0060 — spondyloenchondrodysplasia with immune dysregulation (ACP5), odontochondrodysplasia (TRIP11), SMD Sutcliffe or 'corner fracture' type (FN1), SMD with cone-rod dystrophy (PCYT1A), SMD with corneal dystrophy (PLCB3), and chondrodysplasia-pseudohermaphroditism / Nivelon-Nivelon-Mabille syndrome (HHAT).
Four disorders carrying an SMD name are deliberately placed elsewhere, and the group's own \"see also\" note lists all four: SMD Kozlowski (TRPV4, group 10), severe SMD Sedaghatian type (GPX4, group 14), and axial SMD in its CFAP410-related and NEK1-related forms (group 10, skeletal ciliopathies). TRIP11 additionally spans two groups by severity — odontochondrodysplasia here, achondrogenesis type 1A in group 14 — and MIM 184255 is gene-split between NOS 12-0030 (FN1) and NOS 02-0050 (COL2A1), with the row note \"Some cases are linked to COL2A1 but not the original family\". A radiographic SMD label is therefore a poor predictor of group-12 membership; check Table 1.""")
    spondylo_epi_metaphyseal_dysplasias = PermissibleValue(
        text="spondylo_epi_metaphyseal_dysplasias",
        description="""Group 13 (2023 revision): Spondyloepi(meta)physeal dysplasias (SE(M)D). A large, molecularly heterogeneous group with vertebral plus epiphyseal (with or without metaphyseal) involvement — Dyggve-Melchior-Clausen dysplasia, immuno-osseous dysplasia (Schimke), Wolcott-Rallison syndrome, the named SEMD types (matrilin/MATN3, biglycan, NANS, RSPRY1, TMEM165, EXTL3, DDRGK1, UFSP2, DDR2), X-linked SED tarda (TRAPPC2), spondylodysplastic Ehlers-Danlos syndrome (SLC39A13), SPONASTRIME dysplasia, Steel syndrome, CODAS, EVEN-PLUS and CAGSSS syndromes.""")
    severe_spondylodysplastic_dysplasias = PermissibleValue(
        text="severe_spondylodysplastic_dysplasias",
        description="""Group 14 (2023 revision): Severe spondylodysplastic dysplasias. Perinatally severe/lethal platyspondylic conditions — achondrogenesis type 1A (TRIP11), Schneckenbecken dysplasia (SLC35D1), SMD Sedaghatian type (GPX4), opsismodysplasia (INPPL1).""")
    mesomelic_and_rhizomesomelic_dysplasias = PermissibleValue(
        text="mesomelic_and_rhizomesomelic_dysplasias",
        description="""Group 15 (2023 revision): Mesomelic and rhizo-mesomelic dysplasias. Middle-segment (with or without proximal-segment) shortening — Leri-Weill dyschondrosteosis and Langer mesomelic dysplasia (SHOX), Robinow syndrome (ROR2, NXN, WNT5A, DVL1, DVL3, FZD2), omodysplasia (GPC6, FZD2), and the Kantaputra, Nievergelt, Kozlowski-Reardon, Savarirayan, and Verloes-David-Pfeiffer mesomelic dysplasias. Was group 17 in the 2019 revision.""")
    acromesomelic_dysplasias = PermissibleValue(
        text="acromesomelic_dysplasias",
        description="""Group 16 (2023 revision): Acromesomelic dysplasias. BMP/GDF/NPR2-pathway disorders with combined middle- and distal-segment shortening — acromesomelic dysplasia type Maroteaux (NPR2), Grebe dysplasia and the GDF5/BMPR1B chondrodysplasias, fibular hypoplasia with complex brachydactyly (Du Pan).""")
    acromelic_dysplasias = PermissibleValue(
        text="acromelic_dysplasias",
        description="""Group 17 (2023 revision): Acromelic dysplasias. Short-hand/foot dysplasias — acrocapitofemoral dysplasia (IHH), geleophysic and acromicric dysplasia (ADAMTSL2, FBN1, LTBP3), Weill-Marchesani syndrome, Myhre dysplasia (SMAD4), acrodysostosis (PDE4D, PRKAR1A), Albright hereditary osteodystrophy (GNAS), Leri pleonosteosis. The 2023 revision moved trichorhinophalangeal dysplasia types 1-3 and Langer-Giedion syndrome out of this group into group 19, Brachydactylies as part of syndromes, and moved in the GNAS entity that the 2019 revision listed as \"Pseudohypoparathyroidism type IA\" in group 38 — same OMIM 103580, renamed to Albright hereditary osteodystrophy. This is the only PTH-adjacent GNAS disorder in the nosology outside group 30; note that it is here and NOT in group 28, which despite its name holds only PTH1R/PTHLH/SIK3 disorders. Was group 15 in the 2019 revision.""")
    brachydactyly_without_extraskeletal_manifestations = PermissibleValue(
        text="brachydactyly_without_extraskeletal_manifestations",
        description="""Group 18 (2023 revision): Brachydactylies (isolated). Isolated brachydactyly types A1 (IHH), A2 (BMPR1B, BMP2, GDF5), B (ROR2), B2 (NOG), C (GDF5), D (HOXD13) and E (HOXD13; the PTHLH-related type E2 is in group 28), plus brachydactyly with anonychia (Cooks syndrome, KCNJ2). Was group 37 in the 2019 revision.""")
    brachydactyly_with_extraskeletal_manifestations = PermissibleValue(
        text="brachydactyly_with_extraskeletal_manifestations",
        description="""Group 19 (2023 revision): Brachydactylies as part of syndromes. Syndromic brachydactyly — brachydactyly-mental retardation syndrome (HDAC4), hyperphosphatasia with mental retardation (PIGV), brachydactyly-hypertension/Bilginturan syndrome (PDE3A), Temtamy preaxial brachydactyly (CHSY1), Rubinstein-Taybi syndrome (CREBBP, EP300), Coffin-Siris syndrome and the BAF-complex genes (ARID1B, SMARCB1, SMARCA4, SMARCE1), Feingold syndrome (MYCN), hand-foot-genital syndrome (HOXA13), Catel-Manzke syndrome (TGDS), DOORS syndrome (TBC1D24), and the trichorhinophalangeal dysplasias types 1-3 with Langer-Giedion syndrome (TRPS1, EXT1), which the 2023 revision moved here from group 17. The 2019 group-38 member \"Pseudohypoparathyroidism type IA\" (GNAS) is NOT here in 2023: the same entity (OMIM 103580) was renamed Albright hereditary osteodystrophy and moved to group 17. Was group 38 in the 2019 revision.""")
    bent_bone_dysplasia = PermissibleValue(
        text="bent_bone_dysplasia",
        description="""Group 20 (2023 revision): Bent bones dysplasia group. Disorders sharing the radiographic sign of bent (angulated) long bones — campomelic dysplasia (SOX9), Stuve-Wiedemann dysplasia (LIFR), kyphomelic dysplasia, bent bone dysplasia FGFR2 type. Renamed in the 2019 revision from \"Campomelic dysplasia and related disorders\". Was group 18 in the 2019 revision.""")
    primordial_dwarfism_and_slender_bones = PermissibleValue(
        text="primordial_dwarfism_and_slender_bones",
        description="""Group 21 (2023 revision): Primordial dwarfism and slender bone dysplasias. Severe pre- and postnatal growth restriction with gracile tubular bones. Thirty-five rows, NOS 21-0010 through NOS 21-0350: 3-M syndrome (CUL7, OBSL1, CCDC8); Sanjad-Sakati syndrome (TBCE); dominant Kenny-Caffey syndrome and osteocraniostenosis (both FAM111A); Hallermann-Streiff syndrome; microcephalic osteodysplastic primordial dwarfism across RNU4ATAC, PCNT, ATR, RBBP8, CEP152, DNA2, TRAIP, NSMCE2, CENPE, CRIPT, XRCC4 and DONSON; Roifman syndrome (RNU4ATAC); IMAGe syndrome (CDKN1C) and IMAGe/FILS syndrome (POLE); Saul-Wilson syndrome (COG4); the SCUBE3 short stature-facial dysmorphism-skeletal and dental anomalies syndrome; and the ear-patella-primordial short stature (Meier-Gorlin) syndrome across its pre-replication-complex genes (ORC1, ORC4, ORC6, CDT1, CDC6, GMNN, CDC45, MCM3/5/7, GINS2) - which belongs here and NOT in group 37, patellar dysostoses, despite the \"ear-patella\" in its name. Two consequences of the 2023 dyadic renaming are easy to miss here. First, Seckel syndrome does not appear in the table under that name: its six rows were rewritten as \"Microcephalic osteodysplastic primordial dwarfism, <GENE>-related\" and are identifiable only by gene and OMIM number - ATR (210600, SCKL1), RBBP8 (606744, SCKL2), CEP152 (613823, SCKL5), DNA2 (615807, SCKL8), TRAIP (616777, SCKL9) and NSMCE2 (617253, SCKL10). Searching the table for \"Seckel\" therefore returns nothing, which is a naming artefact and not an exclusion; the same applies to the XRCC4 row (616541), which is the entity published as short stature, microcephaly and endocrine dysfunction (SSMED). Second, Lowry-Wood syndrome is no longer in this group: the 2019 revision listed it here, and the 2023 revision moved it to group 9 as NOS 09-0110 \"Multiple epiphyseal dysplasia with microcephaly and nystagmus (Lowry-Wood syndrome), RNU4ATAC-related\" (OMIM 226960), so RNU4ATAC spans two groups and gene identity does not settle placement for its three phenotypes. Renamed in the 2019 revision from \"Slender bone dysplasia group\". Was group 19 in the 2019 revision.""")
    lysosomal_storage_with_skeletal_involvement = PermissibleValue(
        text="lysosomal_storage_with_skeletal_involvement",
        description="""Group 22 (2023 revision): Lysosomal Storage Diseases with Skeletal Involvement. Mucopolysaccharidoses (types 1-4, 6 and 7, plus VPS33A-related MPS-plus syndrome), mucolipidoses II and III, oligosaccharidoses (fucosidosis, alpha- and beta-mannosidosis, aspartylglucosaminuria, sialidosis, galactosialidosis), sialic acid storage disease, GM1 gangliosidosis, multiple sulfatase deficiency. Was group 27 in the 2019 revision.""")
    chondrodysplasia_punctata = PermissibleValue(
        text="chondrodysplasia_punctata",
        description="""Group 23 (2023 revision): Chondrodysplasia punctata (CDP) group. Disorders with epiphyseal stippling — X-linked dominant Conradi-Hunermann CDPX2 (EBP) and X-linked recessive brachytelephalangic CDPX1 (ARSE/ARSL), rhizomelic CDP (PEX7, GNPAT, AGPS, FAR1, PEX5), CHILD syndrome (NSDHL), Greenberg dysplasia (LBR), Keutel syndrome (MGP). Was group 21 in the 2019 revision.""")
    osteopetrosis_and_related = PermissibleValue(
        text="osteopetrosis_and_related",
        description="""Group 24 (2023 revision): Osteopetrosis and related osteoclast disorders. Osteoclast failure with defective bone resorption — infantile and intermediate osteopetrosis (TCIRG1, CLCN7, OSTM1, SNX10, TNFSF11, TNFRSF11A, PLEKHM1), late-onset (Albers-Schonberg) osteopetrosis, osteopetrosis with renal tubular acidosis (CA2), syndromic forms with ectodermal dysplasia/immune defect (IKBKG) or defective leucocyte adhesion (FERMT3), osteosclerotic metaphyseal dysplasia (LRRK1), pycnodysostosis (CTSK), dysosteosclerosis. Was group 23 in the 2019 revision.""")
    osteosclerotic_disorders = PermissibleValue(
        text="osteosclerotic_disorders",
        description="""Group 25 (2023 revision): Osteosclerotic disorders. Non-osteopetrotic increased bone mass or density, formed in the 2023 revision by fusing the former Neonatal osteosclerotic dysplasias and Other sclerosing bone disorders groups - osteopoikilosis and melorheostosis (LEMD3, MAP2K1), osteopathia striata with cranial sclerosis (AMER1), sclerosteosis and van Buchem disease (SOST, LRP4), craniometaphyseal and craniodiaphyseal dysplasia, Camurati-Engelmann diaphyseal dysplasia (TGFB1), Raine dysplasia (FAM20C), Caffey disease, Pyle disease (SFRP4), Lenz-Majewski hyperostotic dysplasia (PTDSS1). Osteoclast-failure osteopetrosis stays in group 24, and the PTH1R-related Blomstrand dysplasia moved to group 28. Has no single counterpart in the 2019 revision: it fuses two of them.""")
    osteogenesis_imperfecta_and_decreased_bone_density = PermissibleValue(
        text="osteogenesis_imperfecta_and_decreased_bone_density",
        description="""Group 26 (2023 revision): Osteogenesis Imperfecta and bone fragility group. OI types 1-5 across the classical COL1A1/COL1A2 loci and the collagen chaperone/modification, WNT1, IFITM5, and SERPINF1 genes, plus non-OI low-bone-mass and bone-fragility conditions — X-linked and autosomal dominant osteoporosis, osteoporosis-pseudoglioma syndrome (LRP5), Bruck syndrome types 1 and 2, Cole-Carpenter dysplasia (P4HB, SEC24D), spondylo-ocular dysplasia (XYLT2), gnathodiaphyseal dysplasia (ANO5), geroderma osteodysplasticum, autosomal recessive cutis laxa types 2A and 2B, and the Wiedemann-Rautenstrauch and Singleton-Merten syndromes. The B4GALT7-related spondylodysplastic Ehlers-Danlos syndrome that the 2019 revision listed here moved to group 5, Dysplasias with multiple joint dislocations. Was group 25 in the 2019 revision.""")
    abnormal_mineralization = PermissibleValue(
        text="abnormal_mineralization",
        description="""Group 27 (2023 revision): Disorders of bone mineralisation. Disorders of the mineral/phosphate axis with skeletal consequences — hypophosphatasia (ALPL), X-linked and autosomal hypophosphatemic rickets (PHEX, FGF23, DMP1, ENPP1, CLCN5, SLC34A3), vitamin D-dependent rickets types 1A/1B/2A/2B (CYP27B1, CYP2R1, VDR), familial and neonatal hyperparathyroidism (CDC73, GCM2, CASR, TRPV6) and familial hypocalciuric hypercalcemia, and familial chondrocalcinosis / calcium pyrophosphate deposition disease type 2 (ANKH). Was group 26 in the 2019 revision.""")
    parathyroid_hormone_signaling = PermissibleValue(
        text="parathyroid_hormone_signaling",
        description="""Group 28 (2023 revision): Skeletal disorders of parathyroid hormone signaling cascade. New in 2023, collecting the PTH/PTHrP-axis conditions the 2019 revision distributed across other groups. All six members, transcribed from the 2023 table: Jansen-type (PTH1R) and Csukasi-Krakow-type (SIK3) metaphyseal dysplasia, Blomstrand dysplasia (PTH1R), Eiken dysplasia (PTH1R), PTHLH-related brachydactyly type E2, and PTHLH-related osteolysis. Jansen and Eiken came from the 2019 metaphyseal group, Blomstrand from the 2019 neonatal osteosclerotic group. NOTE: despite the group's name, no GNAS disorder belongs here - the 2023 table places Albright hereditary osteodystrophy (GNAS) in group 17 and fibrous dysplasia/McCune-Albright and progressive osseous heteroplasia (GNAS) in group 30, and does not list pseudohypoparathyroidism under that name at all. Do not file PHP/PPHP entries here on mechanistic grounds. Has no counterpart in the 2019 revision.""")
    osteolysis = PermissibleValue(
        text="osteolysis",
        description="""Group 29 (2023 revision): Osteolysis group. Progressive resorption of bone — familial expansile osteolysis (TNFRSF11A), multicentric osteolysis with nodulosis and arthropathy (MMP2, MMP14), multicentric carpal-tarsal osteolysis (MAFB), Hajdu-Cheney syndrome (NOTCH2), mandibuloacral dysplasia and Hutchinson-Gilford progeria (LMNA, ZMPSTE24). Was group 28 in the 2019 revision.""")
    disorganized_development_of_skeletal_components = PermissibleValue(
        text="disorganized_development_of_skeletal_components",
        description="""Group 30 (2023 revision): Disorganized development of skeletal components group. Focal or mosaic disorganized bone and cartilage growth — multiple cartilaginous exostoses (EXT1, EXT2), enchondromatosis (Ollier) and Maffucci syndrome (IDH1, IDH2), metachondromatosis (PTPN11), cherubism (SH3BP2), polyostotic fibrous dysplasia / McCune-Albright syndrome (GNAS), fibrodysplasia ossificans progressiva (ACVR1), neurofibromatosis type 1, osteoglophonic dysplasia (FGFR1), Nasu-Hakola disease (TREM2, TYROBP), dysplasia epiphysealis hemimelica (Trevor), Gorham-Stout disease, osteofibrous dysplasia (MET). Was group 29 in the 2019 revision.""")
    overgrowth_syndromes_with_skeletal_involvement = PermissibleValue(
        text="overgrowth_syndromes_with_skeletal_involvement",
        description="""Group 31 (2023 revision): Overgrowth (tall stature) syndromes and segmental overgrowth. Sotos (NSD1), Weaver (EZH2), Tatton-Brown-Rahman (DNMT3A), Luscan-Lumish (SETD2) and Marshall-Smith (NFIX) syndromes, Proteus syndrome (AKT1) and CLOVES (PIK3CA), Marfan syndrome (FBN1), congenital contractural arachnodactyly (FBN2), Loeys-Dietz syndrome types 1-6 (TGFBR1, TGFBR2, TGFB2, TGFB3, SMAD2, SMAD3), Simpson-Golabi-Behmel (GPC3) and Beckwith-Wiedemann (11p15 imprinting) syndromes. The BGN-related Meester-Loeys syndrome is not listed here — the 2023 revision's only BGN entry is SEMD Camera type in group 7, Proteoglycan core protein disorders. Was group 30 in the 2019 revision.""")
    genetic_inflammatory_rheumatoid_like_osteoarthropathies = PermissibleValue(
        text="genetic_inflammatory_rheumatoid_like_osteoarthropathies",
        description="""Group 32 (2023 revision): Genetic inflammatory or rheumatoid-like osteoarthropathies. Monogenic conditions mimicking inflammatory arthritis or osteomyelitis — progressive pseudorheumatoid dysplasia (WISP3/CCN6), CINCA/NOMID (NLRP3/CIAS1), deficiency of the IL-1 receptor antagonist (IL1RN), Majeed syndrome (LPIN2), hyaline fibromatosis syndrome (ANTXR2). Was group 31 in the 2019 revision.""")
    cleidocranial_dysplasia_and_related = PermissibleValue(
        text="cleidocranial_dysplasia_and_related",
        description="""Group 33 (2023 revision): Cleidocranial dysplasia and related disorders. Cleidocranial dysplasia (RUNX2), CDAGS syndrome, Yunis-Varon dysplasia (FIG4, VAC14), isolated parietal foramina (ALX4, MSX2) and parietal foramina with cleidocranial dysplasia. Was group 32 in the 2019 revision.""")
    craniosynostosis_syndromes = PermissibleValue(
        text="craniosynostosis_syndromes",
        description="""Group 34 (2023 revision): Syndromes featuring craniosynostosis. Syndromic premature suture fusion — Pfeiffer (FGFR1, FGFR2), Apert (FGFR2), Crouzon (FGFR2) and Beare-Stevenson cutis gyrata (FGFR2) syndromes, and the two FGFR3 entries that group 1 points here — Crouzon-like craniosynostosis with acanthosis nigricans (FGFR3) and Muenke-type craniosynostosis (FGFR3), which belong to this group and not to the FGFR3 chondrodysplasias. Also Saethre-Chotzen syndrome (TWIST1), Antley-Bixler syndrome (POR), Boston-type (MSX2), coronal (TCF12) and complex (ERF) craniosynostosis, Shprintzen-Goldberg syndrome (SKI), Baller-Gerold syndrome (RECQL4), Carpenter syndrome (RAB23, MEGF8). Was group 33 in the 2019 revision.""")
    dysostoses_with_predominant_craniofacial_involvement = PermissibleValue(
        text="dysostoses_with_predominant_craniofacial_involvement",
        description="""Group 35 (2023 revision): Craniofacial Dysostoses. Mandibulofacial dysostoses (Treacher Collins — TCOF1, POLR1C, POLR1D; EFTUD2-related with microcephaly; EDNRA-related with alopecia), acrofacial dysostoses (Nager and Rodriguez — SF3B4; Miller — DHODH; Cincinnati — POLR1A), frontonasal dysplasias types 1-3 (ALX3, ALX4, ALX1), craniofrontonasal syndrome (EFNB1), acromelic frontonasal dysostosis (ZSWIM6), auriculocondylar syndrome (GNAI3, PLCB4, EDN1), Richieri-Costa-Pereira syndrome (EIF4A3), orofaciodigital syndrome type I (OFD1), Weyers acrofacial (acrodental) dysostosis (EVC1, EVC2), hemifacial microsomia. Was group 34 in the 2019 revision.""")
    dysostoses_with_predominant_vertebral_and_costal_involvement = PermissibleValue(
        text="dysostoses_with_predominant_vertebral_and_costal_involvement",
        description="""Group 36 (2023 revision): Vertebral and costal dysostoses. Spondylocostal dysostosis (DLL3, MESP2, LFNG, HES7, TBX6, RIPPLY2) and vertebral segmentation defects, Klippel-Feil syndrome (GDF6, MEOX1, GDF3, MYO18B), Currarino syndrome (MNX1), cerebrocostomandibular syndrome (SNRPB), NAD deficiency syndrome (HAAO, KYNU), diaphanospondylodysostosis (BMPER), spondylo-megaepiphyseal-metaphyseal dysplasia (NKX3-2). Was group 35 in the 2019 revision.""")
    patellar_dysostoses = PermissibleValue(
        text="patellar_dysostoses",
        description="""Group 37 (2023 revision): Patellar dysostoses. Ischiopatellar (small patella) dysplasia (TBX4), nail-patella syndrome (LMX1B), and genitopatellar syndrome (KAT6B). Despite its name, the ear-patella-primordial short stature (Meier-Gorlin) syndrome and its pre-replication-complex genes (ORC1, ORC4, ORC6, CDT1, CDC6, GMNN, CDC45, MCM3/5/7, GINS2) are NOT in this group: the 2023 revision lists them in group 21, Primordial dwarfism and slender bone dysplasias. The 2019 revision called it \"ear-patella-short stature syndrome\" and did list it here, in the group's 2019 predecessor — the inserted \"primordial\" is the rename that accompanied the move. Was group 36 in the 2019 revision.""")
    limb_hypoplasia_reduction_defects = PermissibleValue(
        text="limb_hypoplasia_reduction_defects",
        description="""Group 38 (2023 revision): Limb hypoplasia - reduction defects group. Ulnar-mammary syndrome (TBX3), Holt-Oram syndrome (TBX5), Cornelia de Lange syndrome and the cohesinopathies (NIPBL, SMC1A, SMC3, RAD21, HDAC8), Fanconi anemia, thrombocytopenia-absent radius (RBM8A), Roberts syndrome (ESCO2), Okihiro/Duane-radial ray syndrome (SALL4), RAPADILINO syndrome (RECQL4), Adams-Oliver syndrome (ARHGAP31, DOCK6, NOTCH1, DLL4, RBPJ, EOGT), tibial hemimelia, acheiropodia (LMBR1) and tetra-amelia (WNT3, RSPO2), Al-Awadi/ Raas-Rothschild and Fuhrmann syndromes (WNT7A), Poland syndrome. Werner syndrome (tibial hemimelia with polysyndactyly and triphalangeal thumb) is here too, as a ZRS variant; ZRS is the limb-specific SHH enhancer inside LMBR1, so this group and group 40 both touch SHH regulation while listing different disorders. Was group 39 in the 2019 revision.""")
    ectrodactyly_with_and_without_other_manifestations = PermissibleValue(
        text="ectrodactyly_with_and_without_other_manifestations",
        description="""Group 39 (2023 revision): Split hand/foot with and without other manifestations. Split-hand/foot malformation and the ectrodactyly-ectodermal dysplasia-clefting spectrum — TP63-related EEC3, AEC, limb-mammary and SHFM4 phenotypes, SHFM1 (DLX5, DLX6), the 10q24-duplication SHFM3 locus, SHFM6 (WNT10B), split-foot malformation with mesoaxial polydactyly (ZAK), EEM syndrome (CDH3), Hartsfield syndrome (FGFR1). Was group 40 in the 2019 revision.""")
    polydactyly_syndactyly_triphalangism = PermissibleValue(
        text="polydactyly_syndactyly_triphalangism",
        description="""Group 40 (2023 revision): Polydactyly-Syndactyly-Triphalangism group. Preaxial polydactyly types 1-4 and the SHH/ZRS limb enhancer, GLI3-related Greig cephalopolysyndactyly and Pallister-Hall syndromes, synpolydactyly (HOXD13, FBLN1), Townes-Brocks syndrome (SALL1), syndactyly types 1-5 and Cenani-Lenz syndactyly (LRP4), Laurin-Sandrow mirror-image polydactyly, acrocallosal syndrome (KIF7), Filippi syndrome (CKAP2L), STAR syndrome (FAM58A), Meckel syndrome types 1-6, LADD syndrome (FGFR2, FGFR3, FGF10). Was group 41 in the 2019 revision.""")
    defects_in_joint_formation_and_synostoses = PermissibleValue(
        text="defects_in_joint_formation_and_synostoses",
        description="""Group 41 (2023 revision): Defects in joint formation and synostoses. Multiple synostoses syndrome (NOG, GDF5, FGF9, GDF6), radio-ulnar synostosis with amegakaryocytic thrombocytopenia (HOXA11, MECOM), Liebenberg syndrome (PITX1), SAMS syndrome (GSC). Was group 42 in the 2019 revision.""")
    perlecan = PermissibleValue(
        text="perlecan",
        description="""DEPRECATED - HSPG2 (perlecan) disorders — dyssegmental dysplasia (Silverman-Handmaker and Rolland-Desbuquois types) and Schwartz-Jampel syndrome (myotonic chondrodystrophy).""")
    aggrecan = PermissibleValue(
        text="aggrecan",
        description="""DEPRECATED - ACAN disorders — SED Kimberley type, SEMD aggrecan type, and short stature with advanced bone age.""")
    neonatal_osteosclerotic_dysplasias = PermissibleValue(
        text="neonatal_osteosclerotic_dysplasias",
        description="""DEPRECATED - Increased bone density presenting at birth or in early infancy — Blomstrand dysplasia (PTH1R), desmosterolosis (DHCR24), Caffey disease (COL1A1), Raine dysplasia (FAM20C), Al-Gazali-type dysplastic cortical hyperostosis.""")
    other_sclerosing_bone_disorders = PermissibleValue(
        text="other_sclerosing_bone_disorders",
        description="""DEPRECATED - Increased bone mass or density from mechanisms other than osteoclast failure — osteopoikilosis and melorheostosis (LEMD3, MAP2K1), osteopathia striata with cranial sclerosis (AMER1), sclerosteosis and van Buchem disease (SOST, LRP4), craniometaphyseal dysplasia (ANKH, GJA1) and craniodiaphyseal dysplasia (SOST), Camurati-Engelmann diaphyseal dysplasia (TGFB1), hyperostosis-hyperphosphatemia syndrome (GALNT3, FGF23, KL), high-bone-mass LRP5 phenotypes, juvenile Paget disease (TNFRSF11B), Pyle disease (SFRP4), Lenz-Majewski hyperostotic dysplasia (PTDSS1), oculodentoosseous dysplasia (GJA1), Ghosal hematodiaphyseal dysplasia, hypertrophic osteoarthropathy.""")

    _defn = EnumDefinition(
        name="ISDSNosologyGroupEnum",
        description="""The 41 groups of the ISDS Nosology of Genetic Skeletal Disorders, 2023 revision (PMID:36779427), plus four groups deprecated from the 2019 revision (PMID:31633310) that the 2023 revision dissolved. Values are ordered by their 2023 group number; each description opens with that number and records the 2019 number where it differed.""",
    )

class NIHResearchPriorityEnum(EnumDefinitionImpl):
    """
    NIH Highlighted Topics funding-priority areas. Tag entries/projects with the topic(s) whose research goals they
    advance. Snapshot: 2026-07-12.
    """
    NIH_HT_2_transition_from_pediatric_to_adult_health = PermissibleValue(
        text="NIH_HT_2_transition_from_pediatric_to_adult_health",
        description="""Research on the Transition from Pediatric to Adult Health Care (NIH Highlighted Topic 2; expires August 29, 2027). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/2""")
    NIH_HT_3_prevention_treatment_bacterial_sexually_transmitted_infections = PermissibleValue(
        text="NIH_HT_3_prevention_treatment_bacterial_sexually_transmitted_infections",
        description="""Advancing Prevention and Treatment of Bacterial Sexually Transmitted Infections in HIV-Affected Populations (NIH Highlighted Topic 3; expires September 11, 2027). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/3""")
    NIH_HT_4_impact_immune_function_neurocognition_substance_use = PermissibleValue(
        text="NIH_HT_4_impact_immune_function_neurocognition_substance_use",
        description="""Understanding the Impact of Immune Function on Neurocognition and Substance Use Disorder Risk Across the Lifespan (IMMUNE-LIFESPAN) (NIH Highlighted Topic 4; expires September 10, 2027). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/4""")
    NIH_HT_5_sleep_circadian_rhythms_substance_use_disorders = PermissibleValue(
        text="NIH_HT_5_sleep_circadian_rhythms_substance_use_disorders",
        description="""Sleep, Circadian Rhythms, and Substance Use Disorders (NIH Highlighted Topic 5; expires September 10, 2027). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/5""")
    NIH_HT_6_novel_targets_methods_pharmacological_approaches_to = PermissibleValue(
        text="NIH_HT_6_novel_targets_methods_pharmacological_approaches_to",
        description="""Novel Targets, Methods, and Pharmacological Approaches to Treat Substance Use Disorder (NIH Highlighted Topic 6; expires January 28, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/6""")
    NIH_HT_7_novel_circuits_mechanisms_modulating_sensory_integration = PermissibleValue(
        text="NIH_HT_7_novel_circuits_mechanisms_modulating_sensory_integration",
        description="""Novel Circuits and Mechanisms Modulating Sensory Integration and Addiction (NIH Highlighted Topic 7; expires January 9, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/7""")
    NIH_HT_8_data_science_artificial_intelligence_approaches_biomedical = PermissibleValue(
        text="NIH_HT_8_data_science_artificial_intelligence_approaches_biomedical",
        description="""Data Science and Artificial Intelligence Approaches for Biomedical, Biobehavioral and Social Science Research (NIH Highlighted Topic 8; expires June 25, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/8""")
    NIH_HT_9_drowning_prevention = PermissibleValue(
        text="NIH_HT_9_drowning_prevention",
        description="""Research on Drowning Prevention (NIH Highlighted Topic 9; expires August 29, 2027). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/9""")
    NIH_HT_10_effects_contraception_as_treatment_gynecologic_disorders = PermissibleValue(
        text="NIH_HT_10_effects_contraception_as_treatment_gynecologic_disorders",
        description="""Effects of Contraception as Treatment for Gynecologic Disorders (NIH Highlighted Topic 10; expires August 29, 2027). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/10""")
    NIH_HT_11_school_mental_behavioral_health_expanding_access = PermissibleValue(
        text="NIH_HT_11_school_mental_behavioral_health_expanding_access",
        description="""School Mental and Behavioral Health: Expanding Access to Evidence-Based Interventions and Services (NIH Highlighted Topic 11; expires September 11, 2027). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/11""")
    NIH_HT_12_computational_approaches_in_fundamental_neuroscience = PermissibleValue(
        text="NIH_HT_12_computational_approaches_in_fundamental_neuroscience",
        description="""Computational Approaches in Fundamental Neuroscience (NIH Highlighted Topic 12; expires January 27, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/12""")
    NIH_HT_13_combating_chronic_disease_burden_role_trauma = PermissibleValue(
        text="NIH_HT_13_combating_chronic_disease_burden_role_trauma",
        description="""Understanding and Combating Chronic Disease Burden: The Role of Trauma (NIH Highlighted Topic 13; expires September 10, 2027). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/13""")
    NIH_HT_16_priority_questions_in_fundamental_cellular_molecular = PermissibleValue(
        text="NIH_HT_16_priority_questions_in_fundamental_cellular_molecular",
        description="""Priority Research Questions in Fundamental Cellular and Molecular Neuroscience (NIH Highlighted Topic 16; expires September 15, 2027). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/16""")
    NIH_HT_18_brain_initiative_data_knowledgebase_ecosystem_neuroai = PermissibleValue(
        text="NIH_HT_18_brain_initiative_data_knowledgebase_ecosystem_neuroai",
        description="""BRAIN Initiative: Data Knowledgebase Ecosystem and NeuroAI Integration (NIH Highlighted Topic 18; expires September 29, 2027). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/18""")
    NIH_HT_19_brain_initiative_human_neuroscience_precision_molecular = PermissibleValue(
        text="NIH_HT_19_brain_initiative_human_neuroscience_precision_molecular",
        description="""BRAIN Initiative: Advancing Human Neuroscience and Precision Molecular Therapies for Transformative Treatments (NIH Highlighted Topic 19; expires January 22, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/19""")
    NIH_HT_20_implementation_science_to_optimize_hiv_prevention = PermissibleValue(
        text="NIH_HT_20_implementation_science_to_optimize_hiv_prevention",
        description="""Implementation Science to Optimize HIV Prevention and Treatment (NIH Highlighted Topic 20; expires December 2, 2027). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/20""")
    NIH_HT_21_microbiome_science_through_multidisciplinary_mechanistic_investigations = PermissibleValue(
        text="NIH_HT_21_microbiome_science_through_multidisciplinary_mechanistic_investigations",
        description="""Advancing Microbiome Science Through Multidisciplinary Mechanistic Investigations of the Human Microbiome in Health and Disease (NIH Highlighted Topic 21; expires January 15, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/21""")
    NIH_HT_22_short_lived_long_lived_plasma_cells = PermissibleValue(
        text="NIH_HT_22_short_lived_long_lived_plasma_cells",
        description="""Research on Short-Lived and Long-Lived Plasma Cells in Humans (NIH Highlighted Topic 22; expires September 10, 2027). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/22""")
    NIH_HT_23_in_celiac_disease = PermissibleValue(
        text="NIH_HT_23_in_celiac_disease",
        description="""Accelerating Research in Celiac Disease (NIH Highlighted Topic 23; expires September 10, 2027). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/23""")
    NIH_HT_24_computational_modeling_complex_processes_across_biological = PermissibleValue(
        text="NIH_HT_24_computational_modeling_complex_processes_across_biological",
        description="""Computational Modeling of Complex Processes Across Biological Scales (NIH Highlighted Topic 24; expires April 17, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/24""")
    NIH_HT_25_neural_exposome_factors_that_affect_brain = PermissibleValue(
        text="NIH_HT_25_neural_exposome_factors_that_affect_brain",
        description="""Neural Exposome Factors that Affect Brain Health and Neurological Disorders (NIH Highlighted Topic 25; expires December 2, 2027). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/25""")
    NIH_HT_27_technology_development_genomics = PermissibleValue(
        text="NIH_HT_27_technology_development_genomics",
        description="""Technology Development for Genomics (NIH Highlighted Topic 27; expires August 29, 2027). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/27""")
    NIH_HT_28_use_genomic_information_clinical_care = PermissibleValue(
        text="NIH_HT_28_use_genomic_information_clinical_care",
        description="""Advancing the Use of Genomic Information Into Clinical Care (NIH Highlighted Topic 28; expires August 29, 2027). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/28""")
    NIH_HT_31_resources_from_osteoarthritis_initiative_oai = PermissibleValue(
        text="NIH_HT_31_resources_from_osteoarthritis_initiative_oai",
        description="""Supporting Research Using the Resources from the Osteoarthritis Initiative (OAI) (NIH Highlighted Topic 31; expires January 26, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/31""")
    NIH_HT_33_training_career_development_in_dissemination_implementation = PermissibleValue(
        text="NIH_HT_33_training_career_development_in_dissemination_implementation",
        description="""Training and Career Development in Dissemination and Implementation Science (NIH Highlighted Topic 33; expires April 14, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/33""")
    NIH_HT_34_evaluating_evidence_based_practice_users_augmentative = PermissibleValue(
        text="NIH_HT_34_evaluating_evidence_based_practice_users_augmentative",
        description="""Developing and Evaluating Evidence-Based Practice for Users of Augmentative and Alternative Communication (AAC) (NIH Highlighted Topic 34; expires January 26, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/34""")
    NIH_HT_35_use_3d_technologies_human_auditory_vestibular = PermissibleValue(
        text="NIH_HT_35_use_3d_technologies_human_auditory_vestibular",
        description="""Advancing the Use of 3D Technologies Using Human Auditory, Vestibular and Chemosensory Organoids to Create New Approach Models (NAMs) for Treatments (NIH Highlighted Topic 35; expires December 2, 2027). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/35""")
    NIH_HT_36_meaningful_outcome_measures_in_adult_hearing = PermissibleValue(
        text="NIH_HT_36_meaningful_outcome_measures_in_adult_hearing",
        description="""Advancing Meaningful Outcome Measures in Adult Hearing Care (NIH Highlighted Topic 36; expires December 8, 2027). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/36""")
    NIH_HT_37_fundamental_science_neural_circuits_underlying_sensory = PermissibleValue(
        text="NIH_HT_37_fundamental_science_neural_circuits_underlying_sensory",
        description="""Fundamental Science Research on the Neural Circuits Underlying Sensory Processing (NIH Highlighted Topic 37; expires January 22, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/37""")
    NIH_HT_38_leveraging_new_approach_methodologies_non_animal = PermissibleValue(
        text="NIH_HT_38_leveraging_new_approach_methodologies_non_animal",
        description="""Leveraging New Approach Methodologies and Non-Animal Technologies to Accelerate Osteoarthritis Research (NIH Highlighted Topic 38; expires August 29, 2027). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/38""")
    NIH_HT_42_rare_cancers_across_cancer_control_continuum = PermissibleValue(
        text="NIH_HT_42_rare_cancers_across_cancer_control_continuum",
        description="""Research on Rare Cancers Across the Cancer Control Continuum (NIH Highlighted Topic 42; expires February 20, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/42""")
    NIH_HT_43_autoimmune_disease_integrating_genetic_environmental_immunological = PermissibleValue(
        text="NIH_HT_43_autoimmune_disease_integrating_genetic_environmental_immunological",
        description="""Advancing Autoimmune Disease Research: Integrating Genetic, Environmental, and Immunological Factors to Improve Diagnosis and Treatment (NIH Highlighted Topic 43; expires February 12, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/43""")
    NIH_HT_45_optimal_interprofessional_teaming_care_coordination_strategies = PermissibleValue(
        text="NIH_HT_45_optimal_interprofessional_teaming_care_coordination_strategies",
        description="""Optimal Interprofessional Teaming and Care Coordination Strategies for Cancer Care Quality and Outcomes (NIH Highlighted Topic 45; expires February 13, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/45""")
    NIH_HT_46_drug_discovery_nervous_system_disorders = PermissibleValue(
        text="NIH_HT_46_drug_discovery_nervous_system_disorders",
        description="""Drug Discovery for Nervous System Disorders (NIH Highlighted Topic 46; expires January 28, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/46""")
    NIH_HT_48_nutrition_to_inform_regulatory_practice = PermissibleValue(
        text="NIH_HT_48_nutrition_to_inform_regulatory_practice",
        description="""Advancing Nutrition Research to Inform Regulatory Practice (NIH Highlighted Topic 48; expires March 20, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/48""")
    NIH_HT_49_science_prenatal_dietary_supplements = PermissibleValue(
        text="NIH_HT_49_science_prenatal_dietary_supplements",
        description="""Advancing the Science of Prenatal Dietary Supplements (NIH Highlighted Topic 49; expires May 21, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/49""")
    NIH_HT_50_nanotechnology_to_improve_diagnosis_treatment_options = PermissibleValue(
        text="NIH_HT_50_nanotechnology_to_improve_diagnosis_treatment_options",
        description="""Advancing Nanotechnology Research to Improve Diagnosis and Treatment Options (NIH Highlighted Topic 50; expires March 10, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/50""")
    NIH_HT_51_treatment_options_targeted_degrader_technologies = PermissibleValue(
        text="NIH_HT_51_treatment_options_targeted_degrader_technologies",
        description="""Advancing Treatment Options using Targeted Degrader Technologies (NIH Highlighted Topic 51; expires March 10, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/51""")
    NIH_HT_52_biomedical_promoting_trust_improving_health_through = PermissibleValue(
        text="NIH_HT_52_biomedical_promoting_trust_improving_health_through",
        description="""Strengthening Biomedical Research, Promoting Trust, and Improving Health through Bioethics Research (NIH Highlighted Topic 52; expires January 12, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/52""")
    NIH_HT_53_multidisciplinary_studies_hiv_aids_aging = PermissibleValue(
        text="NIH_HT_53_multidisciplinary_studies_hiv_aids_aging",
        description="""Multidisciplinary Studies of HIV/AIDS and Aging (NIH Highlighted Topic 53; expires March 20, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/53""")
    NIH_HT_54_science_science_to_understand_strengthen_biomedical = PermissibleValue(
        text="NIH_HT_54_science_science_to_understand_strengthen_biomedical",
        description="""Advancing \"Science of Science\" Research to Understand and Strengthen the Biomedical Research Ecosystem (NIH Highlighted Topic 54; expires March 31, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/54""")
    NIH_HT_55_mechanism_driven_translational_beneficial_detrimental_effect = PermissibleValue(
        text="NIH_HT_55_mechanism_driven_translational_beneficial_detrimental_effect",
        description="""Advancing Mechanism-driven Translational Research of Beneficial and Detrimental Effect of Psilocybin on Cancer and Other Health Conditions (NIH Highlighted Topic 55; expires April 10, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/55""")
    NIH_HT_56_characterizing_interactions_between_biology_electromagnetic_radiation = PermissibleValue(
        text="NIH_HT_56_characterizing_interactions_between_biology_electromagnetic_radiation",
        description="""Characterizing Interactions between Biology and Electromagnetic Radiation (NIH Highlighted Topic 56; expires April 20, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/56""")
    NIH_HT_57_quantum_information_science_technologies_biomedical_applications = PermissibleValue(
        text="NIH_HT_57_quantum_information_science_technologies_biomedical_applications",
        description="""Quantum Information Science & Technologies for Biomedical Applications (NIH Highlighted Topic 57; expires April 9, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/57""")
    NIH_HT_58_nutritional_influences_neurodevelopmental_disorders_in_children = PermissibleValue(
        text="NIH_HT_58_nutritional_influences_neurodevelopmental_disorders_in_children",
        description="""Understanding Nutritional Influences on Neurodevelopmental Disorders in Children (NIH Highlighted Topic 58; expires March 10, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/58""")
    NIH_HT_59_otitis_media_workforce_development = PermissibleValue(
        text="NIH_HT_59_otitis_media_workforce_development",
        description="""Accelerating Otitis Media Research and Workforce Development (NIH Highlighted Topic 59; expires May 26, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/59""")
    NIH_HT_60_glp_1s_implications_nutritional_status_metabolic = PermissibleValue(
        text="NIH_HT_60_glp_1s_implications_nutritional_status_metabolic",
        description="""GLP-1s: Implications for Nutritional Status and Metabolic Health Outcomes (NIH Highlighted Topic 60; expires April 24, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/60""")
    NIH_HT_61_hidradenitis_suppurativa = PermissibleValue(
        text="NIH_HT_61_hidradenitis_suppurativa",
        description="""Accelerating Hidradenitis Suppurativa Research (NIH Highlighted Topic 61; expires April 7, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/61""")
    NIH_HT_62_new_approach_methodologies_nams_dietary_supplement = PermissibleValue(
        text="NIH_HT_62_new_approach_methodologies_nams_dietary_supplement",
        description="""New Approach Methodologies (NAMs) for Dietary Supplement and Nutrition research (NIH Highlighted Topic 62; expires May 20, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/62""")
    NIH_HT_66_scientific_rigor_transparency_replicability = PermissibleValue(
        text="NIH_HT_66_scientific_rigor_transparency_replicability",
        description="""Enhancing Scientific Rigor, Transparency and Replicability (NIH Highlighted Topic 66; expires April 27, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/66""")
    NIH_HT_67_cause_treatment_rare_skin_diseases = PermissibleValue(
        text="NIH_HT_67_cause_treatment_rare_skin_diseases",
        description="""Advancing Research into the Cause and Treatment of Rare Skin Diseases (NIH Highlighted Topic 67; expires April 2, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/67""")
    NIH_HT_68_childhood_adolescent_young_adult_aya_cancer = PermissibleValue(
        text="NIH_HT_68_childhood_adolescent_young_adult_aya_cancer",
        description="""Advancing Childhood and Adolescent & Young Adult (AYA) Cancer Research (NIH Highlighted Topic 68; expires April 15, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/68""")
    NIH_HT_69_health_extreme_weather_critical_to_address = PermissibleValue(
        text="NIH_HT_69_health_extreme_weather_critical_to_address",
        description="""Health and Extreme Weather: Advancing Critical Research to Address the Direct and Indirect Health Impacts of Weather-Related Natural Disasters and Emerging Weather-Related Harms (NIH Highlighted Topic 69; expires May 1, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/69""")
    NIH_HT_70_chatbots_their_usage = PermissibleValue(
        text="NIH_HT_70_chatbots_their_usage",
        description="""Research on Chatbots and their Usage (NIH Highlighted Topic 70; expires April 15, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/70""")
    NIH_HT_71_tackling_acquisition_language_in_kids_talk = PermissibleValue(
        text="NIH_HT_71_tackling_acquisition_language_in_kids_talk",
        description="""Tackling Acquisition of Language in Kids (TALK) (NIH Highlighted Topic 71; expires April 21, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/71""")
    NIH_HT_72_cure_acquired_neuropathy = PermissibleValue(
        text="NIH_HT_72_cure_acquired_neuropathy",
        description="""Advancing Toward a Cure for Acquired Neuropathy (NIH Highlighted Topic 72; expires April 6, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/72""")
    NIH_HT_73_behavioral_cognitive_signals_aging_in_real = PermissibleValue(
        text="NIH_HT_73_behavioral_cognitive_signals_aging_in_real",
        description="""Behavioral and Cognitive Signals of Aging in Real-World Contexts (NIH Highlighted Topic 73; expires June 24, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/73""")
    NIH_HT_74_oral_health_aging = PermissibleValue(
        text="NIH_HT_74_oral_health_aging",
        description="""Oral Health and Aging (NIH Highlighted Topic 74; expires June 5, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/74""")
    NIH_HT_76_role_post_translational_modifications_in_human = PermissibleValue(
        text="NIH_HT_76_role_post_translational_modifications_in_human",
        description="""Research on the Role of Post-Translational Modifications in Human Health and Disease (NIH Highlighted Topic 76; expires June 26, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/76""")
    NIH_HT_78_food_is_medicine = PermissibleValue(
        text="NIH_HT_78_food_is_medicine",
        description="""Food Is Medicine (NIH Highlighted Topic 78; expires June 3, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/78""")
    NIH_HT_79_data_usage_utility_to_advance_biomedical = PermissibleValue(
        text="NIH_HT_79_data_usage_utility_to_advance_biomedical",
        description="""Enhancing Data Usage and Utility to Advance Biomedical Research (NIH Highlighted Topic 79; expires June 24, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/79""")
    NIH_HT_82_breaking_barriers_integrating_immunology_neuroscience_to = PermissibleValue(
        text="NIH_HT_82_breaking_barriers_integrating_immunology_neuroscience_to",
        description="""Breaking Barriers: Integrating Immunology and Neuroscience to Transform AD/ADRD Research and Bring a Better Understanding of the Aging Brain (NIH Highlighted Topic 82; expires May 1, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/82""")
    NIH_HT_83_biology_physics_informed_explainable_ai_across = PermissibleValue(
        text="NIH_HT_83_biology_physics_informed_explainable_ai_across",
        description="""Biology- and Physics-Informed Explainable AI Across the Lifespan (NIH Highlighted Topic 83; expires June 2, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/83""")
    NIH_HT_84_postnatal_human_developmental_stages_transitions_relationships = PermissibleValue(
        text="NIH_HT_84_postnatal_human_developmental_stages_transitions_relationships",
        description="""Postnatal Human Developmental Stages and Transitions: Relationships to Aging Changes and Outcomes over the Life Course (NIH Highlighted Topic 84; expires May 22, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/84""")
    NIH_HT_85_improve_funded_maternal_health_centers_excellence = PermissibleValue(
        text="NIH_HT_85_improve_funded_maternal_health_centers_excellence",
        description="""Enhancing the IMPROVE-funded Maternal Health Centers of Excellence (NIH Highlighted Topic 85; expires April 7, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/85""")
    NIH_HT_86_biomarker_discovery_validation_alcohol_related_cardiovascular = PermissibleValue(
        text="NIH_HT_86_biomarker_discovery_validation_alcohol_related_cardiovascular",
        description="""Biomarker Discovery and Validation for Alcohol-Related Cardiovascular Diseases (NIH Highlighted Topic 86; expires May 22, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/86""")
    NIH_HT_88_unexplained_anemia_in_older_persons_elucidating = PermissibleValue(
        text="NIH_HT_88_unexplained_anemia_in_older_persons_elucidating",
        description="""Unexplained Anemia in Older Persons: Elucidating Etiologies, Improving Diagnoses, and Identifying and Testing Potential Treatment Strategies (NIH Highlighted Topic 88; expires May 11, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/88""")
    NIH_HT_89_cellular_quiescence_senescence_cell_death_in = PermissibleValue(
        text="NIH_HT_89_cellular_quiescence_senescence_cell_death_in",
        description="""Cellular Quiescence, Senescence, and Cell Death in Aging and Disease (NIH Highlighted Topic 89; expires July 1, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/89""")
    NIH_HT_90_integrating_environmental_science_engineering_with_biomedical = PermissibleValue(
        text="NIH_HT_90_integrating_environmental_science_engineering_with_biomedical",
        description="""Integrating Environmental Science and Engineering with Biomedical Research for Effective Exposure Prevention and Disease Intervention (NIH Highlighted Topic 90; expires June 18, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/90""")
    NIH_HT_93_implementation_science_to_optimize_alcohol_misuse = PermissibleValue(
        text="NIH_HT_93_implementation_science_to_optimize_alcohol_misuse",
        description="""Implementation Science to Optimize Alcohol Misuse Prevention and Treatment in the Criminal Justice System (NIH Highlighted Topic 93; expires July 7, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/93""")
    NIH_HT_94_increasing_engagement_in_treatment_behavioral_health = PermissibleValue(
        text="NIH_HT_94_increasing_engagement_in_treatment_behavioral_health",
        description="""Increasing Engagement in Treatment for Behavioral Health (NIH Highlighted Topic 94; expires July 8, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/94""")
    NIH_HT_95_rna_metabolism_in_aging_healthy_lifespan = PermissibleValue(
        text="NIH_HT_95_rna_metabolism_in_aging_healthy_lifespan",
        description="""RNA Metabolism in Aging and Healthy Lifespan (NIH Highlighted Topic 95; expires July 10, 2028). https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics/95""")

    _defn = EnumDefinition(
        name="NIHResearchPriorityEnum",
        description="""NIH Highlighted Topics funding-priority areas. Tag entries/projects with the topic(s) whose research goals they advance. Snapshot: 2026-07-12.""",
    )

class ILOCausativeAgentEnum(EnumDefinitionImpl):
    """
    The **causative-agent axis** of the ILO List of Occupational Diseases (revised 2010): section 1 (diseases caused
    by chemical, physical and biological agents arising from work activities) and section 3 (occupational cancer,
    itself titled "Cancer caused by the following agents"). Items point to their subsection, and subsections to their
    section, via ``is_a``; assign the most specific applicable item.
    Orthogonal to ``ILODiseaseCategoryEnum`` — a disease commonly takes an item from both, and this slot is
    multivalued because more than one agent item can apply.
    """
    caused_by_agents_arising_from_work = PermissibleValue(
        text="caused_by_agents_arising_from_work",
        description="""ILO section 1: Occupational diseases caused by exposure to agents arising from work activities. Classifies by causative agent rather than by the resulting disease. Orthogonal to section 2.""")
    chemical_agents = PermissibleValue(
        text="chemical_agents",
        description="""ILO section 1.1: Diseases caused by chemical agents. The largest subsection (41 items); each item names an agent or agent family, and covers whatever disease that agent causes at work.""")
    beryllium = PermissibleValue(
        text="beryllium",
        description="ILO item 1.1.1: Diseases caused by beryllium or its compounds.")
    cadmium = PermissibleValue(
        text="cadmium",
        description="ILO item 1.1.2: Diseases caused by cadmium or its compounds.")
    phosphorus = PermissibleValue(
        text="phosphorus",
        description="ILO item 1.1.3: Diseases caused by phosphorus or its compounds.")
    chromium = PermissibleValue(
        text="chromium",
        description="ILO item 1.1.4: Diseases caused by chromium or its compounds.")
    manganese = PermissibleValue(
        text="manganese",
        description="ILO item 1.1.5: Diseases caused by manganese or its compounds.")
    arsenic = PermissibleValue(
        text="arsenic",
        description="ILO item 1.1.6: Diseases caused by arsenic or its compounds.")
    mercury = PermissibleValue(
        text="mercury",
        description="ILO item 1.1.7: Diseases caused by mercury or its compounds.")
    lead = PermissibleValue(
        text="lead",
        description="ILO item 1.1.8: Diseases caused by lead or its compounds.")
    fluorine = PermissibleValue(
        text="fluorine",
        description="ILO item 1.1.9: Diseases caused by fluorine or its compounds.")
    carbon_disulfide = PermissibleValue(
        text="carbon_disulfide",
        description="ILO item 1.1.10: Diseases caused by carbon disulfide.")
    halogen_derivatives_of_hydrocarbons = PermissibleValue(
        text="halogen_derivatives_of_hydrocarbons",
        description="ILO item 1.1.11: Diseases caused by halogen derivatives of aliphatic or aromatic hydrocarbons.")
    benzene_and_homologues = PermissibleValue(
        text="benzene_and_homologues",
        description="ILO item 1.1.12: Diseases caused by benzene or its homologues.")
    nitro_and_amino_derivatives_of_benzene = PermissibleValue(
        text="nitro_and_amino_derivatives_of_benzene",
        description="ILO item 1.1.13: Diseases caused by nitro- and amino-derivatives of benzene or its homologues.")
    nitric_acid_esters = PermissibleValue(
        text="nitric_acid_esters",
        description="ILO item 1.1.14: Diseases caused by nitroglycerine or other nitric acid esters.")
    alcohols_glycols_or_ketones = PermissibleValue(
        text="alcohols_glycols_or_ketones",
        description="ILO item 1.1.15: Diseases caused by alcohols, glycols or ketones.")
    asphyxiants = PermissibleValue(
        text="asphyxiants",
        description="""ILO item 1.1.16: Diseases caused by asphyxiants like carbon monoxide, hydrogen sulfide, hydrogen cyanide or its derivatives.""")
    acrylonitrile = PermissibleValue(
        text="acrylonitrile",
        description="ILO item 1.1.17: Diseases caused by acrylonitrile.")
    oxides_of_nitrogen = PermissibleValue(
        text="oxides_of_nitrogen",
        description="ILO item 1.1.18: Diseases caused by oxides of nitrogen.")
    vanadium = PermissibleValue(
        text="vanadium",
        description="ILO item 1.1.19: Diseases caused by vanadium or its compounds.")
    antimony = PermissibleValue(
        text="antimony",
        description="ILO item 1.1.20: Diseases caused by antimony or its compounds.")
    hexane = PermissibleValue(
        text="hexane",
        description="ILO item 1.1.21: Diseases caused by hexane.")
    mineral_acids = PermissibleValue(
        text="mineral_acids",
        description="ILO item 1.1.22: Diseases caused by mineral acids.")
    pharmaceutical_agents = PermissibleValue(
        text="pharmaceutical_agents",
        description="ILO item 1.1.23: Diseases caused by pharmaceutical agents.")
    nickel = PermissibleValue(
        text="nickel",
        description="ILO item 1.1.24: Diseases caused by nickel or its compounds.")
    thallium = PermissibleValue(
        text="thallium",
        description="ILO item 1.1.25: Diseases caused by thallium or its compounds.")
    osmium = PermissibleValue(
        text="osmium",
        description="ILO item 1.1.26: Diseases caused by osmium or its compounds.")
    selenium = PermissibleValue(
        text="selenium",
        description="ILO item 1.1.27: Diseases caused by selenium or its compounds.")
    copper = PermissibleValue(
        text="copper",
        description="ILO item 1.1.28: Diseases caused by copper or its compounds.")
    platinum = PermissibleValue(
        text="platinum",
        description="ILO item 1.1.29: Diseases caused by platinum or its compounds.")
    tin = PermissibleValue(
        text="tin",
        description="ILO item 1.1.30: Diseases caused by tin or its compounds.")
    zinc = PermissibleValue(
        text="zinc",
        description="ILO item 1.1.31: Diseases caused by zinc or its compounds.")
    phosgene = PermissibleValue(
        text="phosgene",
        description="ILO item 1.1.32: Diseases caused by phosgene.")
    corneal_irritants = PermissibleValue(
        text="corneal_irritants",
        description="ILO item 1.1.33: Diseases caused by corneal irritants like benzoquinone.")
    ammonia = PermissibleValue(
        text="ammonia",
        description="ILO item 1.1.34: Diseases caused by ammonia.")
    isocyanates = PermissibleValue(
        text="isocyanates",
        description="ILO item 1.1.35: Diseases caused by isocyanates.")
    pesticides = PermissibleValue(
        text="pesticides",
        description="ILO item 1.1.36: Diseases caused by pesticides.")
    sulphur_oxides = PermissibleValue(
        text="sulphur_oxides",
        description="ILO item 1.1.37: Diseases caused by sulphur oxides.")
    organic_solvents = PermissibleValue(
        text="organic_solvents",
        description="ILO item 1.1.38: Diseases caused by organic solvents.")
    latex = PermissibleValue(
        text="latex",
        description="ILO item 1.1.39: Diseases caused by latex or latex-containing products.")
    chlorine = PermissibleValue(
        text="chlorine",
        description="ILO item 1.1.40: Diseases caused by chlorine.")
    other_chemical_agents = PermissibleValue(
        text="other_chemical_agents",
        description="""ILO item 1.1.41 (open item): Diseases caused by other chemical agents at work not mentioned in the preceding items where a direct link is established scientifically, or determined by methods appropriate to national conditions and practice, between the exposure to these chemical agents arising from work activities and the disease(s) contracted by the worker. Name the actual agent in ``notes``.""")
    physical_agents = PermissibleValue(
        text="physical_agents",
        description="ILO section 1.2: Diseases caused by physical agents.")
    hearing_impairment_caused_by_noise = PermissibleValue(
        text="hearing_impairment_caused_by_noise",
        description="ILO item 1.2.1: Hearing impairment caused by noise.")
    vibration = PermissibleValue(
        text="vibration",
        description="""ILO item 1.2.2: Diseases caused by vibration (disorders of muscles, tendons, bones, joints, peripheral blood vessels or peripheral nerves).""")
    compressed_or_decompressed_air = PermissibleValue(
        text="compressed_or_decompressed_air",
        description="ILO item 1.2.3: Diseases caused by compressed or decompressed air.")
    ionizing_radiation = PermissibleValue(
        text="ionizing_radiation",
        description="ILO item 1.2.4: Diseases caused by ionizing radiations.")
    optical_radiation = PermissibleValue(
        text="optical_radiation",
        description="""ILO item 1.2.5: Diseases caused by optical (ultraviolet, visible light, infrared) radiations including laser.""")
    extreme_temperatures = PermissibleValue(
        text="extreme_temperatures",
        description="ILO item 1.2.6: Diseases caused by exposure to extreme temperatures.")
    other_physical_agents = PermissibleValue(
        text="other_physical_agents",
        description="""ILO item 1.2.7 (open item): Diseases caused by other physical agents at work not mentioned in the preceding items where a direct link is established scientifically, or determined by methods appropriate to national conditions and practice, between the exposure to these physical agents arising from work activities and the disease(s) contracted by the worker. Name the actual agent in ``notes``.""")
    biological_agents_and_infectious_or_parasitic_diseases = PermissibleValue(
        text="biological_agents_and_infectious_or_parasitic_diseases",
        description="""ILO section 1.3: Biological agents and infectious or parasitic diseases. Unlike the rest of section 1, most items name the disease directly rather than the agent.""")
    brucellosis = PermissibleValue(
        text="brucellosis",
        description="ILO item 1.3.1: Brucellosis.")
    hepatitis_viruses = PermissibleValue(
        text="hepatitis_viruses",
        description="ILO item 1.3.2: Hepatitis viruses.")
    human_immunodeficiency_virus = PermissibleValue(
        text="human_immunodeficiency_virus",
        description="ILO item 1.3.3: Human immunodeficiency virus (HIV).")
    tetanus = PermissibleValue(
        text="tetanus",
        description="ILO item 1.3.4: Tetanus.")
    tuberculosis = PermissibleValue(
        text="tuberculosis",
        description="ILO item 1.3.5: Tuberculosis.")
    toxic_or_inflammatory_syndromes_from_bacterial_or_fungal_contaminants = PermissibleValue(
        text="toxic_or_inflammatory_syndromes_from_bacterial_or_fungal_contaminants",
        description="""ILO item 1.3.6: Toxic or inflammatory syndromes associated with bacterial or fungal contaminants.""")
    anthrax = PermissibleValue(
        text="anthrax",
        description="ILO item 1.3.7: Anthrax.")
    leptospirosis = PermissibleValue(
        text="leptospirosis",
        description="ILO item 1.3.8: Leptospirosis.")
    other_biological_agents = PermissibleValue(
        text="other_biological_agents",
        description="""ILO item 1.3.9 (open item): Diseases caused by other biological agents at work not mentioned in the preceding items where a direct link is established scientifically, or determined by methods appropriate to national conditions and practice, between the exposure to these biological agents arising from work activities and the disease(s) contracted by the worker. Name the actual agent in ``notes``. This is the item under which COVID-19 in health and care workers is recognised, the ILO list predating the pandemic.""")
    occupational_cancer = PermissibleValue(
        text="occupational_cancer",
        description="""ILO section 3: Occupational cancer. Its single subsection lists the agents whose causal link to cancer is recognised; the item names the agent, not the tumour type.""")
    cancer_caused_by_agents = PermissibleValue(
        text="cancer_caused_by_agents",
        description="ILO section 3.1: Cancer caused by the following agents.")
    cancer_asbestos = PermissibleValue(
        text="cancer_asbestos",
        description="ILO item 3.1.1: Cancer caused by asbestos.")
    cancer_benzidine_and_salts = PermissibleValue(
        text="cancer_benzidine_and_salts",
        description="ILO item 3.1.2: Cancer caused by benzidine and its salts.")
    cancer_bis_chloromethyl_ether = PermissibleValue(
        text="cancer_bis_chloromethyl_ether",
        description="ILO item 3.1.3: Cancer caused by bis-chloromethyl ether (BCME).")
    cancer_chromium_vi_compounds = PermissibleValue(
        text="cancer_chromium_vi_compounds",
        description="ILO item 3.1.4: Cancer caused by chromium VI compounds.")
    cancer_coal_tars_pitches_or_soots = PermissibleValue(
        text="cancer_coal_tars_pitches_or_soots",
        description="ILO item 3.1.5: Cancer caused by coal tars, coal tar pitches or soots.")
    cancer_beta_naphthylamine = PermissibleValue(
        text="cancer_beta_naphthylamine",
        description="ILO item 3.1.6: Cancer caused by beta-naphthylamine.")
    cancer_vinyl_chloride = PermissibleValue(
        text="cancer_vinyl_chloride",
        description="ILO item 3.1.7: Cancer caused by vinyl chloride.")
    cancer_benzene = PermissibleValue(
        text="cancer_benzene",
        description="ILO item 3.1.8: Cancer caused by benzene.")
    cancer_nitro_and_amino_derivatives_of_benzene = PermissibleValue(
        text="cancer_nitro_and_amino_derivatives_of_benzene",
        description="""ILO item 3.1.9: Cancer caused by toxic nitro- and amino-derivatives of benzene or its homologues.""")
    cancer_ionizing_radiation = PermissibleValue(
        text="cancer_ionizing_radiation",
        description="ILO item 3.1.10: Cancer caused by ionizing radiations.")
    cancer_tar_pitch_bitumen_mineral_oil_anthracene = PermissibleValue(
        text="cancer_tar_pitch_bitumen_mineral_oil_anthracene",
        description="""ILO item 3.1.11: Cancer caused by tar, pitch, bitumen, mineral oil, anthracene, or the compounds, products or residues of these substances.""")
    cancer_coke_oven_emissions = PermissibleValue(
        text="cancer_coke_oven_emissions",
        description="ILO item 3.1.12: Cancer caused by coke oven emissions.")
    cancer_nickel_compounds = PermissibleValue(
        text="cancer_nickel_compounds",
        description="ILO item 3.1.13: Cancer caused by nickel compounds.")
    cancer_wood_dust = PermissibleValue(
        text="cancer_wood_dust",
        description="ILO item 3.1.14: Cancer caused by wood dust.")
    cancer_arsenic = PermissibleValue(
        text="cancer_arsenic",
        description="ILO item 3.1.15: Cancer caused by arsenic and its compounds.")
    cancer_beryllium = PermissibleValue(
        text="cancer_beryllium",
        description="ILO item 3.1.16: Cancer caused by beryllium and its compounds.")
    cancer_cadmium = PermissibleValue(
        text="cancer_cadmium",
        description="ILO item 3.1.17: Cancer caused by cadmium and its compounds.")
    cancer_erionite = PermissibleValue(
        text="cancer_erionite",
        description="ILO item 3.1.18: Cancer caused by erionite.")
    cancer_ethylene_oxide = PermissibleValue(
        text="cancer_ethylene_oxide",
        description="ILO item 3.1.19: Cancer caused by ethylene oxide.")
    cancer_hepatitis_b_and_c_viruses = PermissibleValue(
        text="cancer_hepatitis_b_and_c_viruses",
        description="ILO item 3.1.20: Cancer caused by hepatitis B virus (HBV) and hepatitis C virus (HCV).")
    cancer_other_agents = PermissibleValue(
        text="cancer_other_agents",
        description="""ILO item 3.1.21 (open item): Cancers caused by other agents at work not mentioned in the preceding items where a direct link is established scientifically, or determined by methods appropriate to national conditions and practice, between the exposure to these agents arising from work activities and the cancer(s) contracted by the worker. Name the actual agent in ``notes``.""")

    _defn = EnumDefinition(
        name="ILOCausativeAgentEnum",
        description="""The **causative-agent axis** of the ILO List of Occupational Diseases (revised 2010): section 1 (diseases caused by chemical, physical and biological agents arising from work activities) and section 3 (occupational cancer, itself titled \"Cancer caused by the following agents\"). Items point to their subsection, and subsections to their section, via ``is_a``; assign the most specific applicable item.
Orthogonal to ``ILODiseaseCategoryEnum`` — a disease commonly takes an item from both, and this slot is multivalued because more than one agent item can apply.""",
    )

class ILODiseaseCategoryEnum(EnumDefinitionImpl):
    """
    The **disease-category axis** of the ILO List of Occupational Diseases (revised 2010): section 2 (occupational
    diseases by target organ systems — respiratory, skin, musculoskeletal, mental and behavioural) and section 4
    ("Other diseases", the residual section). Items here name a clinical entity rather than an agent.
    Orthogonal to ``ILOCausativeAgentEnum``. Multivalued, because more than one disease item from this axis can apply
    to one entry — silicosis takes both 2.1.1 and 2.1.2.
    Note that section 4 is placed on this axis by dismech's reading of the instrument (its named item, miners'
    nystagmus, is a clinical entity), not by an explicit ILO statement; see the schema-level description.
    """
    by_target_organ_system = PermissibleValue(
        text="by_target_organ_system",
        description="""ILO section 2: Occupational diseases by target organ systems. Classifies by the affected organ system rather than by causative agent. Orthogonal to section 1 — a disease commonly takes an item from both.""")
    respiratory_diseases = PermissibleValue(
        text="respiratory_diseases",
        description="ILO section 2.1: Respiratory diseases.")
    pneumoconiosis_from_fibrogenic_mineral_dust = PermissibleValue(
        text="pneumoconiosis_from_fibrogenic_mineral_dust",
        description="""ILO item 2.1.1: Pneumoconioses caused by fibrogenic mineral dust (silicosis, anthraco-silicosis, asbestosis).""")
    silicotuberculosis = PermissibleValue(
        text="silicotuberculosis",
        description="ILO item 2.1.2: Silicotuberculosis.")
    pneumoconiosis_from_non_fibrogenic_mineral_dust = PermissibleValue(
        text="pneumoconiosis_from_non_fibrogenic_mineral_dust",
        description="ILO item 2.1.3: Pneumoconioses caused by non-fibrogenic mineral dust.")
    siderosis = PermissibleValue(
        text="siderosis",
        description="ILO item 2.1.4: Siderosis.")
    bronchopulmonary_disease_from_hard_metal_dust = PermissibleValue(
        text="bronchopulmonary_disease_from_hard_metal_dust",
        description="ILO item 2.1.5: Bronchopulmonary diseases caused by hard-metal dust.")
    bronchopulmonary_disease_from_organic_dust = PermissibleValue(
        text="bronchopulmonary_disease_from_organic_dust",
        description="""ILO item 2.1.6: Bronchopulmonary diseases caused by dust of cotton (byssinosis), flax, hemp, sisal or sugar cane (bagassosis).""")
    occupational_asthma = PermissibleValue(
        text="occupational_asthma",
        description="""ILO item 2.1.7: Asthma caused by recognized sensitizing agents or irritants inherent to the work process.""")
    extrinsic_allergic_alveolitis = PermissibleValue(
        text="extrinsic_allergic_alveolitis",
        description="""ILO item 2.1.8: Extrinsic allergic alveolitis caused by the inhalation of organic dusts or microbially contaminated aerosols, arising from work activities.""")
    chronic_obstructive_pulmonary_disease = PermissibleValue(
        text="chronic_obstructive_pulmonary_disease",
        description="""ILO item 2.1.9: Chronic obstructive pulmonary diseases caused by inhalation of coal dust, dust from stone quarries, wood dust, dust from cereals and agricultural work, dust in animal stables, dust from textiles, and paper dust, arising from work activities.""")
    lung_disease_caused_by_aluminium = PermissibleValue(
        text="lung_disease_caused_by_aluminium",
        description="ILO item 2.1.10: Diseases of the lung caused by aluminium.")
    upper_airways_disorders = PermissibleValue(
        text="upper_airways_disorders",
        description="""ILO item 2.1.11: Upper airways disorders caused by recognized sensitizing agents or irritants inherent to the work process.""")
    other_respiratory_diseases = PermissibleValue(
        text="other_respiratory_diseases",
        description="""ILO item 2.1.12 (open item): Other respiratory diseases not mentioned in the preceding items where a direct link is established scientifically, or determined by methods appropriate to national conditions and practice, between the exposure to risk factors arising from work activities and the disease(s) contracted by the worker.""")
    skin_diseases = PermissibleValue(
        text="skin_diseases",
        description="ILO section 2.2: Skin diseases.")
    allergic_contact_dermatosis_and_contact_urticaria = PermissibleValue(
        text="allergic_contact_dermatosis_and_contact_urticaria",
        description="""ILO item 2.2.1: Allergic contact dermatoses and contact urticaria caused by other recognized allergy-provoking agents arising from work activities not included in other items.""")
    irritant_contact_dermatosis = PermissibleValue(
        text="irritant_contact_dermatosis",
        description="""ILO item 2.2.2: Irritant contact dermatoses caused by other recognized irritant agents arising from work activities not included in other items.""")
    occupational_vitiligo = PermissibleValue(
        text="occupational_vitiligo",
        description="""ILO item 2.2.3: Vitiligo caused by other recognized agents arising from work activities not included in other items.""")
    other_skin_diseases = PermissibleValue(
        text="other_skin_diseases",
        description="""ILO item 2.2.4 (open item): Other skin diseases caused by physical, chemical or biological agents at work not included under other items where a direct link is established scientifically, or determined by methods appropriate to national conditions and practice, between the exposure to risk factors arising from work activities and the skin disease(s) contracted by the worker.""")
    musculoskeletal_disorders = PermissibleValue(
        text="musculoskeletal_disorders",
        description="""ILO section 2.3: Musculoskeletal disorders. Each item names both the lesion and the biomechanical exposure (repetitive movement, forceful exertion, extreme posture, prolonged pressure) that recognises it as occupational.""")
    radial_styloid_tenosynovitis = PermissibleValue(
        text="radial_styloid_tenosynovitis",
        description="""ILO item 2.3.1: Radial styloid tenosynovitis due to repetitive movements, forceful exertions and extreme postures of the wrist.""")
    chronic_tenosynovitis_of_hand_and_wrist = PermissibleValue(
        text="chronic_tenosynovitis_of_hand_and_wrist",
        description="""ILO item 2.3.2: Chronic tenosynovitis of hand and wrist due to repetitive movements, forceful exertions and extreme postures of the wrist.""")
    olecranon_bursitis = PermissibleValue(
        text="olecranon_bursitis",
        description="ILO item 2.3.3: Olecranon bursitis due to prolonged pressure of the elbow region.")
    prepatellar_bursitis = PermissibleValue(
        text="prepatellar_bursitis",
        description="ILO item 2.3.4: Prepatellar bursitis due to prolonged stay in kneeling position.")
    epicondylitis = PermissibleValue(
        text="epicondylitis",
        description="ILO item 2.3.5: Epicondylitis due to repetitive forceful work.")
    meniscus_lesions = PermissibleValue(
        text="meniscus_lesions",
        description="""ILO item 2.3.6: Meniscus lesions following extended periods of work in a kneeling or squatting position.""")
    carpal_tunnel_syndrome = PermissibleValue(
        text="carpal_tunnel_syndrome",
        description="""ILO item 2.3.7: Carpal tunnel syndrome due to extended periods of repetitive forceful work, work involving vibration, extreme postures of the wrist, or a combination of the three.""")
    other_musculoskeletal_disorders = PermissibleValue(
        text="other_musculoskeletal_disorders",
        description="""ILO item 2.3.8 (open item): Other musculoskeletal disorders not mentioned in the preceding items where a direct link is established scientifically, or determined by methods appropriate to national conditions and practice, between the exposure to risk factors arising from work activities and the musculoskeletal disorder(s) contracted by the worker.""")
    mental_and_behavioural_disorders = PermissibleValue(
        text="mental_and_behavioural_disorders",
        description="""ILO section 2.4: Mental and behavioural disorders. New in the 2010 revision — the first time the ILO list named a mental disorder explicitly.""")
    post_traumatic_stress_disorder = PermissibleValue(
        text="post_traumatic_stress_disorder",
        description="ILO item 2.4.1: Post-traumatic stress disorder.")
    other_mental_or_behavioural_disorders = PermissibleValue(
        text="other_mental_or_behavioural_disorders",
        description="""ILO item 2.4.2 (open item): Other mental or behavioural disorders not mentioned in the preceding item where a direct link is established scientifically, or determined by methods appropriate to national conditions and practice, between the exposure to risk factors arising from work activities and the mental and behavioural disorder(s) contracted by the worker.""")
    other_diseases = PermissibleValue(
        text="other_diseases",
        description="""ILO section 4: Other diseases. A residual section with a single named disease and one open item; its items sit directly under the section with no intervening subsection.""")
    miners_nystagmus = PermissibleValue(
        text="miners_nystagmus",
        description="ILO item 4.1: Miners' nystagmus.")
    other_specific_diseases = PermissibleValue(
        text="other_specific_diseases",
        description="""ILO item 4.2 (open item): Other specific diseases caused by occupations or processes not mentioned in this list where a direct link is established scientifically, or determined by methods appropriate to national conditions and practice, between the exposure arising from work activities and the disease(s) contracted by the worker. Name the occupation or process in ``notes``.""")

    _defn = EnumDefinition(
        name="ILODiseaseCategoryEnum",
        description="""The **disease-category axis** of the ILO List of Occupational Diseases (revised 2010): section 2 (occupational diseases by target organ systems — respiratory, skin, musculoskeletal, mental and behavioural) and section 4 (\"Other diseases\", the residual section). Items here name a clinical entity rather than an agent.
Orthogonal to ``ILOCausativeAgentEnum``. Multivalued, because more than one disease item from this axis can apply to one entry — silicosis takes both 2.1.1 and 2.1.2.
Note that section 4 is placed on this axis by dismech's reading of the instrument (its named item, miners' nystagmus, is a clinical entity), not by an explicit ILO statement; see the schema-level description.""",
    )

class EUOccupationalScheduleEnum(EnumDefinitionImpl):
    """
    Annexes, chapters and items of the European schedule of occupational diseases (Commission Recommendation
    2003/670/EC as amended by 2022/2337 and 2025/2609). Items point to their chapter, and chapters to their annex, via
    ``is_a``. Assign the most specific applicable item. Annex II values (``suspected_*``) record a SUSPECTED
    occupational aetiology, not an established one.
    ``source`` on this enum is the consolidated instrument. Individual values carry their own ``source`` ONLY where
    the item was introduced by an amendment rather than by the 2003 base schedule, so a per-value ``source`` is a
    positive signal that the item is a recent addition.
    """
    annex_i = PermissibleValue(
        text="annex_i",
        description="""Annex I: the European schedule of occupational diseases proper - the recognised list Member States are asked to introduce into national law, liable for compensation and subject to prevention measures. The diseases mentioned must be linked directly to the occupation.""")
    annex_ii = PermissibleValue(
        text="annex_ii",
        description="""Annex II: the additional list of diseases suspected of being occupational in origin, which should be subject to notification and which may be considered at a later stage for inclusion in Annex I. A value under this node records a SUSPECTED, not established, occupational aetiology.""")
    annex_i_chemical_agents = PermissibleValue(
        text="annex_i_chemical_agents",
        description="Annex I chapter 1: Diseases caused by the following chemical agents.")
    acrylonitrile = PermissibleValue(
        text="acrylonitrile",
        description="EU schedule item 100: Acrylonitrile.")
    arsenic_compounds = PermissibleValue(
        text="arsenic_compounds",
        description="EU schedule item 101: Arsenic or compounds thereof.")
    beryllium_compounds = PermissibleValue(
        text="beryllium_compounds",
        description="EU schedule item 102: Beryllium (glucinium) or compounds thereof.")
    carbon_monoxide = PermissibleValue(
        text="carbon_monoxide",
        description="EU schedule item 103.01: Carbon monoxide.")
    carbon_oxychloride = PermissibleValue(
        text="carbon_oxychloride",
        description="EU schedule item 103.02: Carbon oxychloride.")
    hydrocyanic_acid = PermissibleValue(
        text="hydrocyanic_acid",
        description="EU schedule item 104.01: Hydrocyanic acid.")
    cyanides_compounds = PermissibleValue(
        text="cyanides_compounds",
        description="EU schedule item 104.02: Cyanides and compounds thereof.")
    isocyanates = PermissibleValue(
        text="isocyanates",
        description="EU schedule item 104.03: Isocyanates.")
    cadmium_compounds = PermissibleValue(
        text="cadmium_compounds",
        description="EU schedule item 105: Cadmium or compounds thereof.")
    chromium_compounds = PermissibleValue(
        text="chromium_compounds",
        description="EU schedule item 106: Chromium or compounds thereof.")
    mercury_compounds = PermissibleValue(
        text="mercury_compounds",
        description="EU schedule item 107: Mercury or compounds thereof.")
    manganese_compounds = PermissibleValue(
        text="manganese_compounds",
        description="EU schedule item 108: Manganese or compounds thereof.")
    nitric_acid = PermissibleValue(
        text="nitric_acid",
        description="EU schedule item 109.01: Nitric acid.")
    oxides_nitrogen = PermissibleValue(
        text="oxides_nitrogen",
        description="EU schedule item 109.02: Oxides of nitrogen.")
    ammonia = PermissibleValue(
        text="ammonia",
        description="EU schedule item 109.03: Ammonia.")
    nickel_compounds = PermissibleValue(
        text="nickel_compounds",
        description="EU schedule item 110: Nickel or compounds thereof.")
    phosphorus_compounds = PermissibleValue(
        text="phosphorus_compounds",
        description="EU schedule item 111: Phosphorus or compounds thereof.")
    lead_compounds = PermissibleValue(
        text="lead_compounds",
        description="EU schedule item 112: Lead or compounds thereof.")
    oxides_sulphur = PermissibleValue(
        text="oxides_sulphur",
        description="EU schedule item 113.01: Oxides of sulphur.")
    sulphuric_acid = PermissibleValue(
        text="sulphuric_acid",
        description="EU schedule item 113.02: Sulphuric acid.")
    carbon_disulphide = PermissibleValue(
        text="carbon_disulphide",
        description="EU schedule item 113.03: Carbon disulphide.")
    vanadium_compounds = PermissibleValue(
        text="vanadium_compounds",
        description="EU schedule item 114: Vanadium or compounds thereof.")
    chlorine = PermissibleValue(
        text="chlorine",
        description="EU schedule item 115.01: Chlorine.")
    bromine = PermissibleValue(
        text="bromine",
        description="EU schedule item 115.02: Bromine.")
    iodine = PermissibleValue(
        text="iodine",
        description="EU schedule item 115.04: Iodine.")
    fluorine_compounds = PermissibleValue(
        text="fluorine_compounds",
        description="EU schedule item 115.05: Fluorine or compounds thereof.")
    aliphatic_or_alicyclic_hydrocarbons = PermissibleValue(
        text="aliphatic_or_alicyclic_hydrocarbons",
        description="""EU schedule item 116: Aliphatic or alicyclic hydrocarbons derived from petroleum spirit or petrol.""")
    halogenated_aliphatic_hydrocarbons = PermissibleValue(
        text="halogenated_aliphatic_hydrocarbons",
        description="EU schedule item 117: Halogenated derivatives of the aliphatic or alicyclic hydrocarbons.")
    butyl = PermissibleValue(
        text="butyl",
        description="EU schedule item 118: Butyl, methyl and isopropyl alcohol.")
    glycols_and_nitrated_derivatives = PermissibleValue(
        text="glycols_and_nitrated_derivatives",
        description="""EU schedule item 119: Ethylene glycol, diethylene glycol, 1,4-butanediol and the nitrated derivatives of the glycols and of glycerol.""")
    ethers = PermissibleValue(
        text="ethers",
        description="""EU schedule item 120: Methyl ether, ethyl ether, isopropyl ether, vinyl ether, dichloroisopropyl ether, guaiacol, methyl ether and ethyl ether of ethylene glycol.""")
    ketones = PermissibleValue(
        text="ketones",
        description="""EU schedule item 121: Acetone, chloroacetone, bromoacetone, hexafluoroacetone, methyl ethyl ketone, methyl n-butyl ketone, methyl isobutyl ketone, diacetone alcohol, mesityl oxide, 2-methylcyclohexanone.""")
    organophosphorus_esters = PermissibleValue(
        text="organophosphorus_esters",
        description="EU schedule item 122: Organophosphorus esters.")
    organic_acids = PermissibleValue(
        text="organic_acids",
        description="EU schedule item 123: Organic acids.")
    formaldehyde = PermissibleValue(
        text="formaldehyde",
        description="EU schedule item 124: Formaldehyde.")
    aliphatic_nitrated_derivatives = PermissibleValue(
        text="aliphatic_nitrated_derivatives",
        description="EU schedule item 125: Aliphatic nitrated derivatives.")
    benzene_and_counterparts = PermissibleValue(
        text="benzene_and_counterparts",
        description="""EU schedule item 126.01: Benzene or counterparts thereof (the counterparts of benzene are defined by the formula: CnH2n-6).""")
    naphthalene_and_counterparts = PermissibleValue(
        text="naphthalene_and_counterparts",
        description="""EU schedule item 126.02: Naphthalene or naphthalene counterparts (the counterpart of naphthalene is defined by the formula: CnH2n-12).""")
    vinylbenzene_divinylbenzene = PermissibleValue(
        text="vinylbenzene_divinylbenzene",
        description="EU schedule item 126.03: Vinylbenzene and divinylbenzene.")
    halogenated_aromatic_hydrocarbons = PermissibleValue(
        text="halogenated_aromatic_hydrocarbons",
        description="EU schedule item 127: Halogenated derivatives of the aromatic hydrocarbons.")
    phenols = PermissibleValue(
        text="phenols",
        description="EU schedule item 128.01: Phenols or counterparts or halogenated derivatives thereof.")
    naphthols = PermissibleValue(
        text="naphthols",
        description="EU schedule item 128.02: Naphthols or counterparts or halogenated derivatives thereof.")
    halogenated_alkylaryl_oxides = PermissibleValue(
        text="halogenated_alkylaryl_oxides",
        description="EU schedule item 128.03: Halogenated derivatives of the alkylaryl oxides.")
    halogenated_alkylaryl_sulfonates = PermissibleValue(
        text="halogenated_alkylaryl_sulfonates",
        description="EU schedule item 128.04: Halogenated derivatives of the alkylaryl sulfonates.")
    benzoquinones = PermissibleValue(
        text="benzoquinones",
        description="EU schedule item 128.05: Benzoquinones.")
    aromatic_amines_and_hydrazines = PermissibleValue(
        text="aromatic_amines_and_hydrazines",
        description="""EU schedule item 129.01: Aromatic amines or aromatic hydrazines or halogenated, phenolic, nitrified, nitrated or sulfonated derivatives thereof.""")
    aliphatic_amines = PermissibleValue(
        text="aliphatic_amines",
        description="EU schedule item 129.02: Aliphatic amines and halogenated derivatives thereof.")
    nitrated_aromatic_hydrocarbons = PermissibleValue(
        text="nitrated_aromatic_hydrocarbons",
        description="EU schedule item 130.01: Nitrated derivatives of aromatic hydrocarbons.")
    nitrated_phenols = PermissibleValue(
        text="nitrated_phenols",
        description="EU schedule item 130.02: Nitrated derivatives of phenols or their counterparts.")
    antimony_derivatives = PermissibleValue(
        text="antimony_derivatives",
        description="EU schedule item 131: Antimony and derivatives thereof.")
    nitric_acid_esters = PermissibleValue(
        text="nitric_acid_esters",
        description="EU schedule item 132: Nitric acid esters.")
    hydrogen_sulphide = PermissibleValue(
        text="hydrogen_sulphide",
        description="EU schedule item 133: Hydrogen sulphide.")
    solvent_encephalopathy = PermissibleValue(
        text="solvent_encephalopathy",
        description="""EU schedule item 135: Encephalopathies due to organic solvents which do not come under other headings.""")
    solvent_polyneuropathy = PermissibleValue(
        text="solvent_polyneuropathy",
        description="""EU schedule item 136: Polyneuropathies due to organic solvents which do not come under other headings.""")
    annex_i_skin_diseases = PermissibleValue(
        text="annex_i_skin_diseases",
        description="""Annex I chapter 2: Skin diseases caused by substances and agents not included under other headings.""")
    skin_diseases_and_skin_cancers = PermissibleValue(
        text="skin_diseases_and_skin_cancers",
        description="EU schedule item 201: Skin diseases and skin cancers caused by:")
    soot = PermissibleValue(
        text="soot",
        description="EU schedule item 201.01: Soot.")
    tar = PermissibleValue(
        text="tar",
        description="EU schedule item 201.03: Tar.")
    bitumen = PermissibleValue(
        text="bitumen",
        description="EU schedule item 201.02: Bitumen.")
    pitch = PermissibleValue(
        text="pitch",
        description="EU schedule item 201.04: Pitch.")
    anthracene_compounds = PermissibleValue(
        text="anthracene_compounds",
        description="EU schedule item 201.05: Anthracene or compounds thereof.")
    mineral_oils = PermissibleValue(
        text="mineral_oils",
        description="EU schedule item 201.06: Mineral and other oils.")
    crude_paraffin = PermissibleValue(
        text="crude_paraffin",
        description="EU schedule item 201.07: Crude paraffin.")
    carbazole_compounds = PermissibleValue(
        text="carbazole_compounds",
        description="EU schedule item 201.08: Carbazole or compounds thereof.")
    by = PermissibleValue(
        text="by",
        description="EU schedule item 201.09: By-products of the distillation of coal.")
    occupational_skin_ailments_allergic_or_irritant = PermissibleValue(
        text="occupational_skin_ailments_allergic_or_irritant",
        description="""EU schedule item 202: Occupational skin ailments caused by scientifically recognised allergy-provoking or irritative substances not included under other headings.""")
    annex_i_inhalation_diseases = PermissibleValue(
        text="annex_i_inhalation_diseases",
        description="""Annex I chapter 3: Diseases caused by the inhalation of substances and agents not included under other headings.""")
    respiratory_diseases_and_cancers = PermissibleValue(
        text="respiratory_diseases_and_cancers",
        description="EU schedule item 301: Diseases of the respiratory system and cancers.")
    silicosis = PermissibleValue(
        text="silicosis",
        description="EU schedule item 301.11: Silicosis.")
    silicosis_combined_pulmonary_tuberculosis = PermissibleValue(
        text="silicosis_combined_pulmonary_tuberculosis",
        description="EU schedule item 301.12: Silicosis combined with pulmonary tuberculosis.")
    asbestosis = PermissibleValue(
        text="asbestosis",
        description="EU schedule item 301.21: Asbestosis.")
    mesothelioma_inhalation_asbestos_dust = PermissibleValue(
        text="mesothelioma_inhalation_asbestos_dust",
        description="EU schedule item 301.22: Mesothelioma following the inhalation of asbestos dust.")
    pneumoconioses_dusts_silicates = PermissibleValue(
        text="pneumoconioses_dusts_silicates",
        description="EU schedule item 301.31: Pneumoconioses caused by dusts of silicates.")
    bronchial_cancer_complicating_asbestosis = PermissibleValue(
        text="bronchial_cancer_complicating_asbestosis",
        description="EU schedule item 302: Complication of asbestosis in the form of bronchial cancer.")
    sintered_metal_dust_bronchopulmonary_disease = PermissibleValue(
        text="sintered_metal_dust_bronchopulmonary_disease",
        description="EU schedule item 303: Broncho-pulmonary ailments caused by dusts from sintered metals.")
    extrinsic_allergic_alveolites = PermissibleValue(
        text="extrinsic_allergic_alveolites",
        description="EU schedule item 304.01: Extrinsic allergic alveolites.")
    cotton_flax_hemp_jute_sisal_bagasse_lung_disease = PermissibleValue(
        text="cotton_flax_hemp_jute_sisal_bagasse_lung_disease",
        description="""EU schedule item 304.02: Lung diseases caused by the inhalation of dusts and fibres from cotton, flax, hemp, jute, sisal and bagasse.""")
    cobalt_tin_barium_graphite_respiratory_ailments = PermissibleValue(
        text="cobalt_tin_barium_graphite_respiratory_ailments",
        description="""EU schedule item 304.04: Respiratory ailments caused by the inhalation of dust from cobalt, tin, barium and graphite.""")
    siderosis = PermissibleValue(
        text="siderosis",
        description="EU schedule item 304.05: Siderosis.")
    upper_respiratory_tract_cancer_from_wood_dust = PermissibleValue(
        text="upper_respiratory_tract_cancer_from_wood_dust",
        description="""EU schedule item 305.01: Cancerous diseases of the upper respiratory tract caused by dust from wood.""")
    allergic_asthma = PermissibleValue(
        text="allergic_asthma",
        description="""EU schedule item 304.06: Allergic asthmas caused by the inhalation of substances consistently recognised as causing allergies and inherent to the type of work.""")
    allergic_rhinitis = PermissibleValue(
        text="allergic_rhinitis",
        description="""EU schedule item 304.07: Allergic rhinitis caused by the inhalation of substances consistently recognised as causing allergies and inherent to the type of work.""")
    asbestos_pleural_fibrosis = PermissibleValue(
        text="asbestos_pleural_fibrosis",
        description="""EU schedule item 306: Fibrotic diseases of the pleura, with respiratory restriction, caused by asbestos.""")
    coal_miners_chronic_bronchitis_or_emphysema = PermissibleValue(
        text="coal_miners_chronic_bronchitis_or_emphysema",
        description="""EU schedule item 307: Chronic obstructive bronchitis or emphysema in miners working in underground coal mines.""")
    lung_cancer_from_asbestos = PermissibleValue(
        text="lung_cancer_from_asbestos",
        description="EU schedule item 308: Lung cancer following the inhalation of asbestos dust.")
    aluminium_bronchopulmonary_disease = PermissibleValue(
        text="aluminium_bronchopulmonary_disease",
        description="""EU schedule item 309: Broncho-pulmonary ailments caused by dusts or fumes from aluminium or compounds thereof.""")
    basic_slag_bronchopulmonary_disease = PermissibleValue(
        text="basic_slag_bronchopulmonary_disease",
        description="EU schedule item 310: Broncho-pulmonary ailments caused by dusts from basic slags.")
    laryngeal_cancer_from_asbestos = PermissibleValue(
        text="laryngeal_cancer_from_asbestos",
        description="EU schedule item 311: Cancer of the larynx caused by asbestos.")
    ovarian_cancer_from_asbestos = PermissibleValue(
        text="ovarian_cancer_from_asbestos",
        description="EU schedule item 312: Cancer of the ovary caused by asbestos.")
    asbestos_pleural_plaques_with_impairment = PermissibleValue(
        text="asbestos_pleural_plaques_with_impairment",
        description="""EU schedule item 313: Pleural plaques with functional impairment of the lungs caused by asbestos.""")
    asbestos_non_malignant_pleural_effusion = PermissibleValue(
        text="asbestos_non_malignant_pleural_effusion",
        description="EU schedule item 314: Non-malignant pleural effusion caused by asbestos.")
    annex_i_infectious_and_parasitic_diseases = PermissibleValue(
        text="annex_i_infectious_and_parasitic_diseases",
        description="Annex I chapter 4: Infectious and parasitic diseases.")
    zoonotic_infectious_or_parasitic_diseases = PermissibleValue(
        text="zoonotic_infectious_or_parasitic_diseases",
        description="""EU schedule item 401: Infectious or parasitic diseases transmitted to man by animals or remains of animals.""")
    tetanus = PermissibleValue(
        text="tetanus",
        description="EU schedule item 402: Tetanus.")
    brucellosis = PermissibleValue(
        text="brucellosis",
        description="EU schedule item 403: Brucellosis.")
    viral_hepatitis = PermissibleValue(
        text="viral_hepatitis",
        description="EU schedule item 404: Viral hepatitis.")
    tuberculosis = PermissibleValue(
        text="tuberculosis",
        description="EU schedule item 405: Tuberculosis.")
    amoebiasis = PermissibleValue(
        text="amoebiasis",
        description="EU schedule item 406: Amoebiasis.")
    other_occupational_infectious_diseases = PermissibleValue(
        text="other_occupational_infectious_diseases",
        description="""EU schedule item 407: Other infectious diseases caused by work in disease prevention, health care, domicilary assistance and other comparable activities for which a risk of infection has been proven.""")
    covid_19 = PermissibleValue(
        text="covid_19",
        description="""EU schedule item 408: COVID-19 caused by work in disease prevention, in health and social care and in domiciliary assistance, or, in a pandemic context, in sectors where there is an outbreak in activities in which a risk of infection has been proven.""")
    annex_i_physical_agents = PermissibleValue(
        text="annex_i_physical_agents",
        description="Annex I chapter 5: Diseases caused by the following physical agents.")
    cataracts_heat_radiation = PermissibleValue(
        text="cataracts_heat_radiation",
        description="EU schedule item 502.01: Cataracts caused by heat radiation.")
    ultraviolet_conjunctival_ailments = PermissibleValue(
        text="ultraviolet_conjunctival_ailments",
        description="EU schedule item 502.02: Conjunctival ailments following exposure to ultraviolet radiation.")
    noise_induced_hypoacousis_or_deafness = PermissibleValue(
        text="noise_induced_hypoacousis_or_deafness",
        description="EU schedule item 503: Hypoacousis or deafness caused by noise.")
    atmospheric_compression_or_decompression = PermissibleValue(
        text="atmospheric_compression_or_decompression",
        description="EU schedule item 504: Diseases caused by atmospheric compression or decompression.")
    vibration_osteoarticular_disease_of_hand_and_wrist = PermissibleValue(
        text="vibration_osteoarticular_disease_of_hand_and_wrist",
        description="""EU schedule item 505.01: Osteoarticular diseases of the hands and wrists caused by mechanical vibration.""")
    vibration_angioneurotic_disease = PermissibleValue(
        text="vibration_angioneurotic_disease",
        description="EU schedule item 505.02: Angioneurotic diseases caused by mechanical vibration.")
    periarticular_sac_disease_from_pressure = PermissibleValue(
        text="periarticular_sac_disease_from_pressure",
        description="EU schedule item 506.10: Diseases of the periarticular sacs due to pressure.")
    pre = PermissibleValue(
        text="pre",
        description="EU schedule item 506.11: Pre-patellar and sub-patellar bursitis.")
    olecranon_bursitis = PermissibleValue(
        text="olecranon_bursitis",
        description="EU schedule item 506.12: Olecranon bursitis.")
    shoulder_bursitis = PermissibleValue(
        text="shoulder_bursitis",
        description="EU schedule item 506.13: Shoulder bursitis.")
    tendon_sheath_overstraining = PermissibleValue(
        text="tendon_sheath_overstraining",
        description="EU schedule item 506.21: Diseases due to overstraining of the tendon sheaths.")
    peritendineum_overstraining = PermissibleValue(
        text="peritendineum_overstraining",
        description="EU schedule item 506.22: Diseases due to overstraining of the peritendineum.")
    muscular_and_tendonous_insertion_overstraining = PermissibleValue(
        text="muscular_and_tendonous_insertion_overstraining",
        description="""EU schedule item 506.23: Diseases due to overstraining of the muscular and tendonous insertions.""")
    meniscus_lesions = PermissibleValue(
        text="meniscus_lesions",
        description="""EU schedule item 506.30: Meniscus lesions following extended periods of work in a kneeling or squatting position.""")
    nerve_paralysis_from_pressure = PermissibleValue(
        text="nerve_paralysis_from_pressure",
        description="EU schedule item 506.40: Paralysis of the nerves due to pressure.")
    carpal_tunnel_syndrome = PermissibleValue(
        text="carpal_tunnel_syndrome",
        description="EU schedule item 506.45: Carpal tunnel syndrome.")
    miners_nystagmus = PermissibleValue(
        text="miners_nystagmus",
        description="EU schedule item 507: Miner's nystagmus.")
    ionising_radiation = PermissibleValue(
        text="ionising_radiation",
        description="EU schedule item 508: Diseases caused by ionising radiation.")
    annex_ii_agents = PermissibleValue(
        text="annex_ii_agents",
        description="Annex II chapter 2.1: Diseases caused by the following agents.")
    suspected_ozone = PermissibleValue(
        text="suspected_ozone",
        description="EU schedule item 2.101: Ozone.")
    suspected_aliphatic_hydrocarbons = PermissibleValue(
        text="suspected_aliphatic_hydrocarbons",
        description="""EU schedule item 2.102: Aliphatic hydrocarbons other than those referred to under heading 1.116 of Annex I.""")
    suspected_diphenyl = PermissibleValue(
        text="suspected_diphenyl",
        description="EU schedule item 2.103: Diphenyl.")
    suspected_decalin = PermissibleValue(
        text="suspected_decalin",
        description="EU schedule item 2.104: Decalin.")
    suspected_aromatic_acids_and_anhydrides = PermissibleValue(
        text="suspected_aromatic_acids_and_anhydrides",
        description="EU schedule item 2.105: Aromatic acids - aromatic anhydrides or their halogenated derivatives.")
    suspected_diphenyl_oxide = PermissibleValue(
        text="suspected_diphenyl_oxide",
        description="EU schedule item 2.106: Diphenyl oxide.")
    suspected_tetrahydrophurane = PermissibleValue(
        text="suspected_tetrahydrophurane",
        description="EU schedule item 2.107: Tetrahydrophurane.")
    suspected_thiophene = PermissibleValue(
        text="suspected_thiophene",
        description="EU schedule item 2.108: Thiophene.")
    suspected_methacrylonitrile = PermissibleValue(
        text="suspected_methacrylonitrile",
        description="EU schedule item 2.109: Methacrylonitrile.")
    suspected_acetonitrile = PermissibleValue(
        text="suspected_acetonitrile",
        description="EU schedule item 2.110: Acetonitrile.")
    suspected_thioalcohols = PermissibleValue(
        text="suspected_thioalcohols",
        description="EU schedule item 2.111: Thioalcohols.")
    suspected_mercaptans_thioethers = PermissibleValue(
        text="suspected_mercaptans_thioethers",
        description="EU schedule item 2.112: Mercaptans and thioethers.")
    suspected_thallium_compounds = PermissibleValue(
        text="suspected_thallium_compounds",
        description="EU schedule item 2.113: Thallium or compounds thereof.")
    suspected_alcohols = PermissibleValue(
        text="suspected_alcohols",
        description="""EU schedule item 2.114: Alcohols or their halogenated derivatives not referred to under heading 1.118 of Annex I.""")
    suspected_glycols = PermissibleValue(
        text="suspected_glycols",
        description="""EU schedule item 2.115: Glycols or their halogenated derivatives not referred to under heading 1.119 of Annex I.""")
    suspected_ethers = PermissibleValue(
        text="suspected_ethers",
        description="""EU schedule item 2.116: Ethers or their halogenated derivatives not referred to under heading 1.120 of Annex I.""")
    suspected_ketones = PermissibleValue(
        text="suspected_ketones",
        description="""EU schedule item 2.117: Ketones or their halogenated derivatives not referred to under heading 1.121 of Annex I.""")
    suspected_esters = PermissibleValue(
        text="suspected_esters",
        description="""EU schedule item 2.118: Esters or their halogenated derivatives not referred to under heading 1.122 of Annex I.""")
    suspected_furfural = PermissibleValue(
        text="suspected_furfural",
        description="EU schedule item 2.119: Furfural.")
    suspected_thiophenols = PermissibleValue(
        text="suspected_thiophenols",
        description="EU schedule item 2.120: Thiophenols or counterparts or halogenated derivatives thereof.")
    suspected_silver = PermissibleValue(
        text="suspected_silver",
        description="EU schedule item 2.121: Silver.")
    suspected_selenium = PermissibleValue(
        text="suspected_selenium",
        description="EU schedule item 2.122: Selenium.")
    suspected_copper = PermissibleValue(
        text="suspected_copper",
        description="EU schedule item 2.123: Copper.")
    suspected_zinc = PermissibleValue(
        text="suspected_zinc",
        description="EU schedule item 2.124: Zinc.")
    suspected_magnesium = PermissibleValue(
        text="suspected_magnesium",
        description="EU schedule item 2.125: Magnesium.")
    suspected_platinum = PermissibleValue(
        text="suspected_platinum",
        description="EU schedule item 2.126: Platinum.")
    suspected_tantalum = PermissibleValue(
        text="suspected_tantalum",
        description="EU schedule item 2.127: Tantalum.")
    suspected_titanium = PermissibleValue(
        text="suspected_titanium",
        description="EU schedule item 2.128: Titanium.")
    suspected_terpenes = PermissibleValue(
        text="suspected_terpenes",
        description="EU schedule item 2.129: Terpenes.")
    suspected_boranes = PermissibleValue(
        text="suspected_boranes",
        description="EU schedule item 2.130: Boranes.")
    suspected_nacre_dust = PermissibleValue(
        text="suspected_nacre_dust",
        description="EU schedule item 2.140: Diseases caused by inhaling nacre dust.")
    suspected_hormonal_substances = PermissibleValue(
        text="suspected_hormonal_substances",
        description="EU schedule item 2.141: Diseases caused by hormonal substances.")
    suspected_dental_caries = PermissibleValue(
        text="suspected_dental_caries",
        description="""EU schedule item 2.150: Dental caries associated with work in the chocolate, sugar and flour industries.""")
    suspected_silicium_oxide = PermissibleValue(
        text="suspected_silicium_oxide",
        description="EU schedule item 2.160: Silicium oxide.")
    suspected_polycyclic_aromatic_hydrocarbons = PermissibleValue(
        text="suspected_polycyclic_aromatic_hydrocarbons",
        description="""EU schedule item 2.170: Polycyclic aromatic hydrocarbons which do not come under other headings.""")
    suspected_dimethylformamide = PermissibleValue(
        text="suspected_dimethylformamide",
        description="EU schedule item 2.190: Dimethylformamide.")
    annex_ii_skin_diseases = PermissibleValue(
        text="annex_ii_skin_diseases",
        description="""Annex II chapter 2.2: Skin diseases caused by substances and agents not included under other headings.""")
    suspected_allergic_and_orthoallergic_skin_ailments = PermissibleValue(
        text="suspected_allergic_and_orthoallergic_skin_ailments",
        description="EU schedule item 2.201: Allergic and orthoallergic skin ailments not recognised in Annex I.")
    annex_ii_inhalation_diseases = PermissibleValue(
        text="annex_ii_inhalation_diseases",
        description="""Annex II chapter 2.3: Diseases caused by inhaling substances not included under other headings.""")
    suspected_metal_pulmonary_fibrosis = PermissibleValue(
        text="suspected_metal_pulmonary_fibrosis",
        description="""EU schedule item 2.301: Pulmonary fibroses due to metals not included in the European schedule.""")
    suspected_soot_tar_bitumen_bronchopulmonary_disease_and_cancer = PermissibleValue(
        text="suspected_soot_tar_bitumen_bronchopulmonary_disease_and_cancer",
        description="""EU schedule item 2.303: Broncho-pulmonary ailments and cancers associated with exposure to the following: - soot - tar - bitumen - pitch - anthracene or compounds thereof - mineral and other oils.""")
    suspected_man_made_mineral_fibre_disease = PermissibleValue(
        text="suspected_man_made_mineral_fibre_disease",
        description="EU schedule item 2.304: Broncho-pulmonary ailments caused by man-made mineral fibres.")
    suspected_synthetic_fibre_disease = PermissibleValue(
        text="suspected_synthetic_fibre_disease",
        description="EU schedule item 2.305: Broncho-pulmonary ailments caused by synthetic fibres.")
    suspected_irritant_respiratory_ailments = PermissibleValue(
        text="suspected_irritant_respiratory_ailments",
        description="""EU schedule item 2.307: Respiratory ailments, particularly asthma, caused by irritants not listed in Annex I.""")
    suspected_colon_cancer_from_asbestos = PermissibleValue(
        text="suspected_colon_cancer_from_asbestos",
        description="EU schedule item 2.309: Colon cancer caused by asbestos.")
    suspected_rectal_cancer_from_asbestos = PermissibleValue(
        text="suspected_rectal_cancer_from_asbestos",
        description="EU schedule item 2.310: Rectum cancer caused by asbestos.")
    suspected_stomach_cancer_from_asbestos = PermissibleValue(
        text="suspected_stomach_cancer_from_asbestos",
        description="EU schedule item 2.311: Stomach cancer caused by asbestos.")
    annex_ii_infectious_and_parasitic_diseases = PermissibleValue(
        text="annex_ii_infectious_and_parasitic_diseases",
        description="Annex II chapter 2.4: Infectious and parasitic diseases not described in Annex I.")
    suspected_parasitic_diseases = PermissibleValue(
        text="suspected_parasitic_diseases",
        description="EU schedule item 2.401: Parasitic diseases.")
    suspected_tropical_diseases = PermissibleValue(
        text="suspected_tropical_diseases",
        description="EU schedule item 2.402: Tropical diseases.")
    annex_ii_physical_agents = PermissibleValue(
        text="annex_ii_physical_agents",
        description="Annex II chapter 2.5: Diseases caused by physical agents.")
    suspected_spinous_process_avulsion = PermissibleValue(
        text="suspected_spinous_process_avulsion",
        description="EU schedule item 2.501: Avulsion due to overstraining of the spinous processes.")
    suspected_whole_body_vibration_disc_disease = PermissibleValue(
        text="suspected_whole_body_vibration_disc_disease",
        description="""EU schedule item 2.502: Disc-related diseases of the lumbar vertebral column caused by the repeated vertical effects of whole-body vibration.""")
    suspected_vocal_cord_nodules = PermissibleValue(
        text="suspected_vocal_cord_nodules",
        description="""EU schedule item 2.503: Nodules on the vocal chords caused by sustained work-related vocal effort.""")

    _defn = EnumDefinition(
        name="EUOccupationalScheduleEnum",
        description="""Annexes, chapters and items of the European schedule of occupational diseases (Commission Recommendation 2003/670/EC as amended by 2022/2337 and 2025/2609). Items point to their chapter, and chapters to their annex, via ``is_a``. Assign the most specific applicable item. Annex II values (``suspected_*``) record a SUSPECTED occupational aetiology, not an established one.
``source`` on this enum is the consolidated instrument. Individual values carry their own ``source`` ONLY where the item was introduced by an amendment rather than by the 2003 base schedule, so a per-value ``source`` is a positive signal that the item is a recent addition.""",
    )

class HazardAgentTypeEnum(EnumDefinitionImpl):
    """
    The classical occupational-hygiene classification of workplace hazards by the *nature of the agent*. This is the
    organising scheme used throughout occupational health practice and teaching, and it is the axis the ILO list uses
    for its section 1 (chemical / physical / biological agents), extended with the two categories that scheme
    historically omitted — ergonomic and psychosocial — both of which the ILO list now recognises as causes in section
    2 (musculoskeletal disorders; mental and behavioural disorders).
    Assign the agent's nature, not its effect: noise-induced hearing loss is a PHYSICAL hazard, not a physiological
    one.
    """
    CHEMICAL = PermissibleValue(
        text="CHEMICAL",
        description="""A chemical agent — dusts, fumes, gases, vapours, mists, solvents, metals, pesticides, pharmaceuticals. The ILO list's section 1.1 and the European schedule's chapter 1.""")
    PHYSICAL = PermissibleValue(
        text="PHYSICAL",
        description="""A physical energy or condition — noise, vibration, ionizing and optical radiation, extreme temperature, compressed or decompressed air. ILO section 1.2, European schedule chapter 5.""")
    BIOLOGICAL = PermissibleValue(
        text="BIOLOGICAL",
        description="""A living agent or its product — bacteria, viruses, fungi, parasites, endotoxin, allergenic proteins such as latex. ILO section 1.3, European schedule chapter 4.""")
    ERGONOMIC = PermissibleValue(
        text="ERGONOMIC",
        description="""A biomechanical exposure — repetitive movement, forceful exertion, sustained or extreme posture, prolonged pressure, manual handling, whole-body vibration. The exposure class behind ILO section 2.3.""")
    PSYCHOSOCIAL = PermissibleValue(
        text="PSYCHOSOCIAL",
        description="""A work-organisation or psychosocial exposure — traumatic incident, violence, harassment, excessive demand, low control, shift work, effort-reward imbalance. The exposure class behind ILO section 2.4.""")
    SAFETY = PermissibleValue(
        text="SAFETY",
        description="""A mechanical or safety hazard producing acute injury rather than disease — machinery, falls, electricity, fire, confined spaces. Present for completeness of the hazard taxonomy; dismech entries are diseases, so this value is rarely the right one.""")
    OTHER = PermissibleValue(
        text="OTHER",
        description="An agent that does not fall into any of the above classes.")

    _defn = EnumDefinition(
        name="HazardAgentTypeEnum",
        description="""The classical occupational-hygiene classification of workplace hazards by the *nature of the agent*. This is the organising scheme used throughout occupational health practice and teaching, and it is the axis the ILO list uses for its section 1 (chemical / physical / biological agents), extended with the two categories that scheme historically omitted — ergonomic and psychosocial — both of which the ILO list now recognises as causes in section 2 (musculoskeletal disorders; mental and behavioural disorders).
Assign the agent's nature, not its effect: noise-induced hearing loss is a PHYSICAL hazard, not a physiological one.""",
    )

class ExposureRouteEnum(EnumDefinitionImpl):
    """
    Route of exposure — the portal by which an agent reaches the organism. Standard toxicological/regulatory axis,
    used by ATSDR toxicological profiles, EPA risk assessment and the GHS alike, and post-composed into ECTO exposure
    terms ("exposure to arsenic in water via ingestion").
    The route is a property of the exposure event, so one agent commonly has several — the slot is multivalued. Route
    matters mechanistically: the same agent produces different disease by different routes (inhaled versus ingested
    hexavalent chromium), which is why this is worth recording separately rather than leaving implicit in the ECTO
    label.
    """
    INHALATION = PermissibleValue(
        text="INHALATION",
        description="""Uptake via the respiratory tract — gases, vapours, aerosols, dusts, fumes, fibres. The dominant route in occupational exposure.""")
    ORAL = PermissibleValue(
        text="ORAL",
        description="""Uptake by ingestion, including incidental hand-to-mouth transfer and contaminated food or drinking water.""")
    DERMAL = PermissibleValue(
        text="DERMAL",
        description="Uptake through intact or damaged skin, and local action on the skin itself.")
    OCULAR = PermissibleValue(
        text="OCULAR",
        description="Contact with, or uptake through, the eye and conjunctiva.")
    PARENTERAL = PermissibleValue(
        text="PARENTERAL",
        description="""Uptake bypassing epithelial barriers — needlestick and sharps injury, injection, implantation, wound contamination. The route for occupational bloodborne infection.""")
    TRANSPLACENTAL = PermissibleValue(
        text="TRANSPLACENTAL",
        description="""Uptake by the conceptus across the placenta following maternal exposure. The route underlying developmental toxicity and prenatal origins of later disease.""")
    LACTATIONAL = PermissibleValue(
        text="LACTATIONAL",
        description="Uptake by the infant through breast milk following maternal exposure.")
    MULTIPLE = PermissibleValue(
        text="MULTIPLE",
        description="""Substantial exposure by more than one route where the individual routes are not separable. Prefer listing the specific routes when they are known.""")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="Route not established or not reported by the cited source.")

    _defn = EnumDefinition(
        name="ExposureRouteEnum",
        description="""Route of exposure — the portal by which an agent reaches the organism. Standard toxicological/regulatory axis, used by ATSDR toxicological profiles, EPA risk assessment and the GHS alike, and post-composed into ECTO exposure terms (\"exposure to arsenic in water via ingestion\").
The route is a property of the exposure event, so one agent commonly has several — the slot is multivalued. Route matters mechanistically: the same agent produces different disease by different routes (inhaled versus ingested hexavalent chromium), which is why this is worth recording separately rather than leaving implicit in the ECTO label.""",
    )

class ExposureDurationEnum(EnumDefinitionImpl):
    """
    Duration of exposure. The day ranges given are those used by the US Agency for Toxic Substances and Disease
    Registry (ATSDR) in deriving Minimal Risk Levels, which is the most precisely specified of the common conventions:
    acute 1-14 days, intermediate 15-364 days, chronic 365 days and longer.
    Beware that agencies do not agree on the bin boundaries — EPA risk assessment uses acute / short-term / subchronic
    / chronic with different cut points, and the occupational literature often uses "chronic" to mean simply
    "long-term" with no threshold. The values here carry the ATSDR ranges as their definition; when a source uses a
    different convention, pick the value whose *meaning* matches and say so in ``notes`` rather than forcing the
    source's word onto a value with a different range.
    This describes the exposure, not the disease course. A single acute exposure can cause a chronic disease; use
    ``temporality`` / ``clinical_course`` on the phenotype descriptor for the latter.
    """
    ACUTE = PermissibleValue(
        text="ACUTE",
        description="""A single exposure or repeated exposure over 1-14 days (ATSDR acute duration). Includes the single high-dose incident, spill or release.""")
    INTERMEDIATE = PermissibleValue(
        text="INTERMEDIATE",
        description="""Repeated exposure over 15-364 days (ATSDR intermediate duration). Overlaps what other agencies call subacute or subchronic.""")
    CHRONIC = PermissibleValue(
        text="CHRONIC",
        description="""Repeated exposure over 365 days or longer (ATSDR chronic duration). The usual shape of an occupational exposure across a working life.""")
    INTERMITTENT = PermissibleValue(
        text="INTERMITTENT",
        description="""Recurrent discrete exposures separated by exposure-free intervals, where the episodic pattern rather than the cumulative dose is the salient feature (task-based peak exposure, seasonal work).""")
    LIFETIME = PermissibleValue(
        text="LIFETIME",
        description="""Continuous exposure across the whole lifespan, the framing used for ubiquitous environmental agents (background air pollution, residential radon) and for lifetime-risk cancer estimates.""")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="Duration not established or not reported by the cited source.")

    _defn = EnumDefinition(
        name="ExposureDurationEnum",
        description="""Duration of exposure. The day ranges given are those used by the US Agency for Toxic Substances and Disease Registry (ATSDR) in deriving Minimal Risk Levels, which is the most precisely specified of the common conventions: acute 1-14 days, intermediate 15-364 days, chronic 365 days and longer.
Beware that agencies do not agree on the bin boundaries — EPA risk assessment uses acute / short-term / subchronic / chronic with different cut points, and the occupational literature often uses \"chronic\" to mean simply \"long-term\" with no threshold. The values here carry the ATSDR ranges as their definition; when a source uses a different convention, pick the value whose *meaning* matches and say so in ``notes`` rather than forcing the source's word onto a value with a different range.
This describes the exposure, not the disease course. A single acute exposure can cause a chronic disease; use ``temporality`` / ``clinical_course`` on the phenotype descriptor for the latter.""",
    )

class IARCCarcinogenGroupEnum(EnumDefinitionImpl):
    """
    Carcinogenicity classification of an agent by the IARC Monographs on the Identification of Carcinogenic Hazards to
    Humans (International Agency for Research on Cancer, WHO). Encodes the group set established by the Preamble as
    amended in January 2019.
    **This is a hazard identification, not a risk assessment.** The group states how strong the evidence is that the
    agent *can* cause cancer under some circumstance — it says nothing about potency, exposure level, or how much
    cancer the agent actually causes in a population. Group 1 contains both plutonium and processed meat. Curators
    must not paraphrase a group as a statement of risk, and a Group 1 listing is not by itself evidence that a
    particular disease entry's exposure caused a particular cancer.
    Groups are assigned to an *agent* (or a mixture, or an exposure circumstance such as "painter, occupational
    exposure as a"), so this belongs on the exposure, never on the disease. Note also that a group applies to the
    agent overall; the specific tumour sites with sufficient evidence are stated separately in the Monograph and
    should go in ``notes`` if they matter.
    """
    GROUP_1 = PermissibleValue(
        text="GROUP_1",
        description="""Group 1 - Carcinogenic to humans. Sufficient evidence of carcinogenicity in humans, or (exceptionally) sufficient evidence in experimental animals plus strong mechanistic evidence in exposed humans.""")
    GROUP_2A = PermissibleValue(
        text="GROUP_2A",
        description="""Group 2A - Probably carcinogenic to humans. Typically limited evidence in humans together with sufficient evidence in experimental animals, or strong mechanistic evidence.""")
    GROUP_2B = PermissibleValue(
        text="GROUP_2B",
        description="""Group 2B - Possibly carcinogenic to humans. Limited evidence in humans and less than sufficient evidence in experimental animals, or sufficient animal evidence alone, or strong mechanistic evidence alone.""")
    GROUP_3 = PermissibleValue(
        text="GROUP_3",
        description="""Group 3 - Not classifiable as to its carcinogenicity to humans. A statement that the evidence is inadequate, NOT a finding of safety. Do not report a Group 3 agent as non-carcinogenic.""")
    GROUP_4 = PermissibleValue(
        text="GROUP_4",
        description="""Group 4 - Probably not carcinogenic to humans. **Withdrawn**: the category was removed by the January 2019 amendment to the Preamble, having only ever been applied to a single agent - caprolactam, which was moved to Group 3 in the same revision. Retained only so historical assignments citing the pre-2019 scheme remain resolvable; never use for new curation.""")

    _defn = EnumDefinition(
        name="IARCCarcinogenGroupEnum",
        description="""Carcinogenicity classification of an agent by the IARC Monographs on the Identification of Carcinogenic Hazards to Humans (International Agency for Research on Cancer, WHO). Encodes the group set established by the Preamble as amended in January 2019.
**This is a hazard identification, not a risk assessment.** The group states how strong the evidence is that the agent *can* cause cancer under some circumstance — it says nothing about potency, exposure level, or how much cancer the agent actually causes in a population. Group 1 contains both plutonium and processed meat. Curators must not paraphrase a group as a statement of risk, and a Group 1 listing is not by itself evidence that a particular disease entry's exposure caused a particular cancer.
Groups are assigned to an *agent* (or a mixture, or an exposure circumstance such as \"painter, occupational exposure as a\"), so this belongs on the exposure, never on the disease. Note also that a group applies to the agent overall; the specific tumour sites with sufficient evidence are stated separately in the Monograph and should go in ``notes`` if they matter.""",
    )

class GHSHealthHazardClassEnum(EnumDefinitionImpl):
    """
    Health hazard classes of the United Nations Globally Harmonized System of Classification and Labelling of
    Chemicals (GHS), the international standard implemented in EU law as the CLP Regulation (EC) No 1272/2008 and in
    the US as the OSHA Hazard Communication Standard.
    These ten classes are the GHS *health* hazards. GHS also defines physical hazard classes (flammability,
    explosivity, …) and environmental hazard classes (hazardous to the aquatic environment, hazardous to the ozone
    layer); neither is in scope here, since this axis exists to describe how an agent harms an exposed organism.
    Each class is subdivided into numbered categories (and sub-categories) that grade severity — Carcinogenicity
    1A/1B/2, acute toxicity 1-5, and so on. The category is *not* encoded as a permissible value, because the category
    boundaries are defined per class in terms of class-specific criteria and flattening them into one enum would
    produce values that only make sense in context. Record the category in the assignment's ``notes`` (for example,
    "Carc. 1A") alongside the class.
    """
    ACUTE_TOXICITY = PermissibleValue(
        text="ACUTE_TOXICITY",
        description="""Acute toxicity - serious adverse effects, up to lethality, after a single or short-term oral, dermal or inhalation exposure.""")
    SKIN_CORROSION_IRRITATION = PermissibleValue(
        text="SKIN_CORROSION_IRRITATION",
        description="""Skin corrosion / irritation - irreversible damage to, or reversible inflammation of, the skin after application of a substance.""")
    SERIOUS_EYE_DAMAGE_IRRITATION = PermissibleValue(
        text="SERIOUS_EYE_DAMAGE_IRRITATION",
        description="""Serious eye damage / eye irritation - tissue damage or serious physical decay of vision, or reversible ocular changes.""")
    RESPIRATORY_OR_SKIN_SENSITIZATION = PermissibleValue(
        text="RESPIRATORY_OR_SKIN_SENSITIZATION",
        description="""Respiratory or skin sensitization - induction of hypersensitivity of the airways after inhalation, or an allergic response after skin contact. The GHS class corresponding to occupational asthma and allergic contact dermatitis.""")
    GERM_CELL_MUTAGENICITY = PermissibleValue(
        text="GERM_CELL_MUTAGENICITY",
        description="""Germ cell mutagenicity - heritable gene mutations, including structural and numerical chromosome aberrations, in germ cells.""")
    CARCINOGENICITY = PermissibleValue(
        text="CARCINOGENICITY",
        description="""Carcinogenicity - induction of cancer or an increase in cancer incidence after exposure. Classified independently of, and on different criteria from, the IARC groups; the two frequently but not always agree, so record both rather than inferring one from the other.""")
    REPRODUCTIVE_TOXICITY = PermissibleValue(
        text="REPRODUCTIVE_TOXICITY",
        description="""Reproductive toxicity - adverse effects on sexual function and fertility in adults, and developmental toxicity in the offspring.""")
    STOT_SINGLE_EXPOSURE = PermissibleValue(
        text="STOT_SINGLE_EXPOSURE",
        description="""Specific target organ toxicity, single exposure (STOT-SE) - specific, non-lethal target-organ effects after one exposure.""")
    STOT_REPEATED_EXPOSURE = PermissibleValue(
        text="STOT_REPEATED_EXPOSURE",
        description="""Specific target organ toxicity, repeated exposure (STOT-RE) - specific target-organ effects after repeated or prolonged exposure.""")
    ASPIRATION_HAZARD = PermissibleValue(
        text="ASPIRATION_HAZARD",
        description="""Aspiration hazard - chemical pneumonia, pulmonary injury or death following aspiration of a substance into the trachea and lower respiratory system.""")

    _defn = EnumDefinition(
        name="GHSHealthHazardClassEnum",
        description="""Health hazard classes of the United Nations Globally Harmonized System of Classification and Labelling of Chemicals (GHS), the international standard implemented in EU law as the CLP Regulation (EC) No 1272/2008 and in the US as the OSHA Hazard Communication Standard.
These ten classes are the GHS *health* hazards. GHS also defines physical hazard classes (flammability, explosivity, …) and environmental hazard classes (hazardous to the aquatic environment, hazardous to the ozone layer); neither is in scope here, since this axis exists to describe how an agent harms an exposed organism.
Each class is subdivided into numbered categories (and sub-categories) that grade severity — Carcinogenicity 1A/1B/2, acute toxicity 1-5, and so on. The category is *not* encoded as a permissible value, because the category boundaries are defined per class in terms of class-specific criteria and flattening them into one enum would produce values that only make sense in context. Record the category in the assignment's ``notes`` (for example, \"Carc. 1A\") alongside the class.""",
    )

class ExposomeDomainEnum(EnumDefinitionImpl):
    """
    Domain of the exposome, following the three-domain framing set out by Christopher Wild ("The exposome: from
    concept to utility", Int J Epidemiol 2012;41(1):24-32, PMID:22296988), which extended his 2005 proposal of the
    exposome as the totality of non-genetic exposures from conception onwards.
    Wild is explicit that the domains overlap and that some exposures are hard to place — the internal domain is
    partly a *response* to the external. Use the value that names where the exposure is measured or acts, and do not
    treat a placement as a sharp claim. This axis is included because it is the standard vocabulary of exposome-scale
    epidemiology, which is increasingly the source of the environmental associations dismech curates; it is a framing
    device, not a regulatory instrument like the other enums here.
    """
    GENERAL_EXTERNAL = PermissibleValue(
        text="GENERAL_EXTERNAL",
        description="""The general external environment - the wider social, economic and built context: socioeconomic position, education, urban-rural setting, climate, and other exposures acting at population rather than individual scale.""")
    SPECIFIC_EXTERNAL = PermissibleValue(
        text="SPECIFIC_EXTERNAL",
        description="""The specific external environment - identifiable individual-level exposures: chemical contaminants, occupational agents, radiation, infections, diet, tobacco, alcohol, physical activity.""")
    INTERNAL = PermissibleValue(
        text="INTERNAL",
        description="""The internal environment - internal biological processes reflecting and responding to exposure: metabolism, endogenous hormones, oxidative stress, inflammation, gut microbiome, epigenetic modification.""")

    _defn = EnumDefinition(
        name="ExposomeDomainEnum",
        description="""Domain of the exposome, following the three-domain framing set out by Christopher Wild (\"The exposome: from concept to utility\", Int J Epidemiol 2012;41(1):24-32, PMID:22296988), which extended his 2005 proposal of the exposome as the totality of non-genetic exposures from conception onwards.
Wild is explicit that the domains overlap and that some exposures are hard to place — the internal domain is partly a *response* to the external. Use the value that names where the exposure is measured or acts, and do not treat a placement as a sharp claim. This axis is included because it is the standard vocabulary of exposome-scale epidemiology, which is increasingly the source of the environmental associations dismech curates; it is a framing device, not a regulatory instrument like the other enums here.""",
    )

# Slots
class slots:
    pass

slots.gene_sets = Slot(uri=DISMECH.gene_sets, name="gene_sets", curie=DISMECH.curie('gene_sets'),
                   model_uri=DISMECH.gene_sets, domain=None, range=Optional[Union[Union[dict, GeneSetAssociation], list[Union[dict, GeneSetAssociation]]]])

slots.name = Slot(uri=DISMECH.name, name="name", curie=DISMECH.curie('name'),
                   model_uri=DISMECH.name, domain=None, range=URIRef)

slots.display_name = Slot(uri=DISMECH.display_name, name="display_name", curie=DISMECH.curie('display_name'),
                   model_uri=DISMECH.display_name, domain=None, range=Optional[str])

slots.slug = Slot(uri=DISMECH.slug, name="slug", curie=DISMECH.curie('slug'),
                   model_uri=DISMECH.slug, domain=None, range=Optional[str])

slots.description = Slot(uri=DISMECH.description, name="description", curie=DISMECH.curie('description'),
                   model_uri=DISMECH.description, domain=None, range=Optional[str])

slots.preferred_term = Slot(uri=DISMECH.preferred_term, name="preferred_term", curie=DISMECH.curie('preferred_term'),
                   model_uri=DISMECH.preferred_term, domain=None, range=str)

slots.term = Slot(uri=DISMECH.term, name="term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.term, domain=None, range=Optional[Union[dict, Term]])

slots.modifier = Slot(uri=DISMECH.modifier, name="modifier", curie=DISMECH.curie('modifier'),
                   model_uri=DISMECH.modifier, domain=None, range=Optional[Union[str, "ModifierEnum"]])

slots.located_in = Slot(uri=DISMECH.located_in, name="located_in", curie=DISMECH.curie('located_in'),
                   model_uri=DISMECH.located_in, domain=None, range=Optional[Union[dict, AnatomicalEntityDescriptor]])

slots.laterality = Slot(uri=DISMECH.laterality, name="laterality", curie=DISMECH.curie('laterality'),
                   model_uri=DISMECH.laterality, domain=None, range=Optional[Union[str, "LateralityEnum"]])

slots.spatial_extent = Slot(uri=DISMECH.spatial_extent, name="spatial_extent", curie=DISMECH.curie('spatial_extent'),
                   model_uri=DISMECH.spatial_extent, domain=None, range=Optional[Union[str, "SpatialExtentEnum"]])

slots.temporality = Slot(uri=DISMECH.temporality, name="temporality", curie=DISMECH.curie('temporality'),
                   model_uri=DISMECH.temporality, domain=None, range=Optional[Union[str, "TemporalityEnum"]])

slots.clinical_course = Slot(uri=DISMECH.clinical_course, name="clinical_course", curie=DISMECH.curie('clinical_course'),
                   model_uri=DISMECH.clinical_course, domain=None, range=Optional[Union[str, "ClinicalCourseEnum"]])

slots.therapeutic_agent = Slot(uri=DISMECH.therapeutic_agent, name="therapeutic_agent", curie=DISMECH.curie('therapeutic_agent'),
                   model_uri=DISMECH.therapeutic_agent, domain=None, range=Optional[Union[Union[dict, ChemicalEntityDescriptor], list[Union[dict, ChemicalEntityDescriptor]]]])

slots.dietary_modifications = Slot(uri=DISMECH.dietary_modifications, name="dietary_modifications", curie=DISMECH.curie('dietary_modifications'),
                   model_uri=DISMECH.dietary_modifications, domain=None, range=Optional[Union[Union[dict, DietaryModification], list[Union[dict, DietaryModification]]]])

slots.qualifiers = Slot(uri=DISMECH.qualifiers, name="qualifiers", curie=DISMECH.curie('qualifiers'),
                   model_uri=DISMECH.qualifiers, domain=None, range=Optional[Union[Union[dict, Qualifier], list[Union[dict, Qualifier]]]])

slots.predicate = Slot(uri=DISMECH.predicate, name="predicate", curie=DISMECH.curie('predicate'),
                   model_uri=DISMECH.predicate, domain=None, range=Optional[Union[dict, Descriptor]])

slots.value = Slot(uri=DISMECH.value, name="value", curie=DISMECH.curie('value'),
                   model_uri=DISMECH.value, domain=None, range=Optional[Union[dict, Descriptor]])

slots.action = Slot(uri=DISMECH.action, name="action", curie=DISMECH.curie('action'),
                   model_uri=DISMECH.action, domain=None, range=Optional[Union[str, "DietaryModificationActionEnum"]])

slots.food = Slot(uri=DISMECH.food, name="food", curie=DISMECH.curie('food'),
                   model_uri=DISMECH.food, domain=None, range=Optional[Union[dict, FoodDescriptor]])

slots.id = Slot(uri=DISMECH.id, name="id", curie=DISMECH.curie('id'),
                   model_uri=DISMECH.id, domain=None, range=URIRef)

slots.label = Slot(uri=DISMECH.label, name="label", curie=DISMECH.curie('label'),
                   model_uri=DISMECH.label, domain=None, range=Optional[str])

slots.evidence = Slot(uri=DISMECH.evidence, name="evidence", curie=DISMECH.curie('evidence'),
                   model_uri=DISMECH.evidence, domain=None, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.distinguishing_features = Slot(uri=DISMECH.distinguishing_features, name="distinguishing_features", curie=DISMECH.curie('distinguishing_features'),
                   model_uri=DISMECH.distinguishing_features, domain=None, range=Optional[Union[str, list[str]]])

slots.review_notes = Slot(uri=DISMECH.review_notes, name="review_notes", curie=DISMECH.curie('review_notes'),
                   model_uri=DISMECH.review_notes, domain=None, range=Optional[str])

slots.geography = Slot(uri=DISMECH.geography, name="geography", curie=DISMECH.curie('geography'),
                   model_uri=DISMECH.geography, domain=None, range=Optional[Union[Union[str, "GeographyTerm"], list[Union[str, "GeographyTerm"]]]])

slots.locations = Slot(uri=DISMECH.locations, name="locations", curie=DISMECH.curie('locations'),
                   model_uri=DISMECH.locations, domain=None, range=Optional[Union[Union[dict, AnatomicalEntityDescriptor], list[Union[dict, AnatomicalEntityDescriptor]]]])

slots.reference = Slot(uri=DISMECH.reference, name="reference", curie=DISMECH.curie('reference'),
                   model_uri=DISMECH.reference, domain=None, range=Optional[str])

slots.supports = Slot(uri=DISMECH.supports, name="supports", curie=DISMECH.curie('supports'),
                   model_uri=DISMECH.supports, domain=None, range=Optional[Union[str, "EvidenceItemSupportEnum"]])

slots.directness = Slot(uri=DISMECH.directness, name="directness", curie=DISMECH.curie('directness'),
                   model_uri=DISMECH.directness, domain=None, range=Optional[Union[str, "DirectnessEnum"]])

slots.evidence_source = Slot(uri=DISMECH.evidence_source, name="evidence_source", curie=DISMECH.curie('evidence_source'),
                   model_uri=DISMECH.evidence_source, domain=None, range=Optional[Union[str, "EvidenceSourceEnum"]])

slots.snippet = Slot(uri=DISMECH.snippet, name="snippet", curie=DISMECH.curie('snippet'),
                   model_uri=DISMECH.snippet, domain=None, range=Optional[str])

slots.reference_title = Slot(uri=DISMECH.reference_title, name="reference_title", curie=DISMECH.curie('reference_title'),
                   model_uri=DISMECH.reference_title, domain=None, range=Optional[str])

slots.explanation = Slot(uri=DISMECH.explanation, name="explanation", curie=DISMECH.curie('explanation'),
                   model_uri=DISMECH.explanation, domain=None, range=Optional[str])

slots.images = Slot(uri=DISMECH.images, name="images", curie=DISMECH.curie('images'),
                   model_uri=DISMECH.images, domain=None, range=Optional[Union[str, list[str]]])

slots.references = Slot(uri=DISMECH.references, name="references", curie=DISMECH.curie('references'),
                   model_uri=DISMECH.references, domain=None, range=Optional[Union[dict[Union[str, PublicationReferenceReference], Union[dict, PublicationReference]], list[Union[dict, PublicationReference]]]])

slots.findings = Slot(uri=DISMECH.findings, name="findings", curie=DISMECH.curie('findings'),
                   model_uri=DISMECH.findings, domain=None, range=Optional[Union[Union[dict, Finding], list[Union[dict, Finding]]]])

slots.statement = Slot(uri=DISMECH.statement, name="statement", curie=DISMECH.curie('statement'),
                   model_uri=DISMECH.statement, domain=None, range=str)

slots.supporting_text = Slot(uri=DISMECH.supporting_text, name="supporting_text", curie=DISMECH.curie('supporting_text'),
                   model_uri=DISMECH.supporting_text, domain=None, range=Optional[str])

slots.title = Slot(uri=DISMECH.title, name="title", curie=DISMECH.curie('title'),
                   model_uri=DISMECH.title, domain=None, range=Optional[str])

slots.found_in = Slot(uri=DISMECH.found_in, name="found_in", curie=DISMECH.curie('found_in'),
                   model_uri=DISMECH.found_in, domain=None, range=Optional[Union[str, list[str]]])

slots.tags = Slot(uri=DISMECH.tags, name="tags", curie=DISMECH.curie('tags'),
                   model_uri=DISMECH.tags, domain=None, range=Optional[Union[Union[str, "ReferenceTagEnum"], list[Union[str, "ReferenceTagEnum"]]]])

slots.subtype = Slot(uri=DISMECH.subtype, name="subtype", curie=DISMECH.curie('subtype'),
                   model_uri=DISMECH.subtype, domain=None, range=Optional[str])

slots.population = Slot(uri=DISMECH.population, name="population", curie=DISMECH.curie('population'),
                   model_uri=DISMECH.population, domain=None, range=Optional[str])

slots.percentage = Slot(uri=DISMECH.percentage, name="percentage", curie=DISMECH.curie('percentage'),
                   model_uri=DISMECH.percentage, domain=None, range=Optional[Union[dict, Any]])

slots.measure_type = Slot(uri=DISMECH.measure_type, name="measure_type", curie=DISMECH.curie('measure_type'),
                   model_uri=DISMECH.measure_type, domain=None, range=Optional[Union[str, "PrevalenceMeasureEnum"]])

slots.prevalence_class = Slot(uri=DISMECH.prevalence_class, name="prevalence_class", curie=DISMECH.curie('prevalence_class'),
                   model_uri=DISMECH.prevalence_class, domain=None, range=Optional[Union[str, "PrevalenceClassEnum"]])

slots.rate_per_100000 = Slot(uri=DISMECH.rate_per_100000, name="rate_per_100000", curie=DISMECH.curie('rate_per_100000'),
                   model_uri=DISMECH.rate_per_100000, domain=None, range=Optional[float])

slots.rate_low = Slot(uri=DISMECH.rate_low, name="rate_low", curie=DISMECH.curie('rate_low'),
                   model_uri=DISMECH.rate_low, domain=None, range=Optional[float])

slots.rate_high = Slot(uri=DISMECH.rate_high, name="rate_high", curie=DISMECH.curie('rate_high'),
                   model_uri=DISMECH.rate_high, domain=None, range=Optional[float])

slots.case_fractions = Slot(uri=DISMECH.case_fractions, name="case_fractions", curie=DISMECH.curie('case_fractions'),
                   model_uri=DISMECH.case_fractions, domain=None, range=Optional[Union[Union[dict, GeneCaseFraction], list[Union[dict, GeneCaseFraction]]]])

slots.case_fraction_percent = Slot(uri=DISMECH.case_fraction_percent, name="case_fraction_percent", curie=DISMECH.curie('case_fraction_percent'),
                   model_uri=DISMECH.case_fraction_percent, domain=None, range=Optional[float])

slots.case_fraction_low = Slot(uri=DISMECH.case_fraction_low, name="case_fraction_low", curie=DISMECH.curie('case_fraction_low'),
                   model_uri=DISMECH.case_fraction_low, domain=None, range=Optional[float])

slots.case_fraction_high = Slot(uri=DISMECH.case_fraction_high, name="case_fraction_high", curie=DISMECH.curie('case_fraction_high'),
                   model_uri=DISMECH.case_fraction_high, domain=None, range=Optional[float])

slots.cohort_size = Slot(uri=DISMECH.cohort_size, name="cohort_size", curie=DISMECH.curie('cohort_size'),
                   model_uri=DISMECH.cohort_size, domain=None, range=Optional[int])

slots.phase = Slot(uri=DISMECH.phase, name="phase", curie=DISMECH.curie('phase'),
                   model_uri=DISMECH.phase, domain=None, range=Optional[Union[str, "PhaseTerm"]])

slots.status = Slot(uri=DISMECH.status, name="status", curie=DISMECH.curie('status'),
                   model_uri=DISMECH.status, domain=None, range=Optional[str])

slots.age_range = Slot(uri=DISMECH.age_range, name="age_range", curie=DISMECH.curie('age_range'),
                   model_uri=DISMECH.age_range, domain=None, range=Optional[str])

slots.incubation_days = Slot(uri=DISMECH.incubation_days, name="incubation_days", curie=DISMECH.curie('incubation_days'),
                   model_uri=DISMECH.incubation_days, domain=None, range=Optional[str])

slots.incubation_years = Slot(uri=DISMECH.incubation_years, name="incubation_years", curie=DISMECH.curie('incubation_years'),
                   model_uri=DISMECH.incubation_years, domain=None, range=Optional[str])

slots.notes = Slot(uri=DISMECH.notes, name="notes", curie=DISMECH.curie('notes'),
                   model_uri=DISMECH.notes, domain=None, range=Optional[str])

slots.duration_days = Slot(uri=DISMECH.duration_days, name="duration_days", curie=DISMECH.curie('duration_days'),
                   model_uri=DISMECH.duration_days, domain=None, range=Optional[str])

slots.duration = Slot(uri=DISMECH.duration, name="duration", curie=DISMECH.curie('duration'),
                   model_uri=DISMECH.duration, domain=None, range=Optional[str])

slots.cell_types = Slot(uri=DISMECH.cell_types, name="cell_types", curie=DISMECH.curie('cell_types'),
                   model_uri=DISMECH.cell_types, domain=None, range=Optional[Union[Union[dict, CellTypeDescriptor], list[Union[dict, CellTypeDescriptor]]]])

slots.biological_processes = Slot(uri=DISMECH.biological_processes, name="biological_processes", curie=DISMECH.curie('biological_processes'),
                   model_uri=DISMECH.biological_processes, domain=None, range=Optional[Union[Union[dict, BiologicalProcessDescriptor], list[Union[dict, BiologicalProcessDescriptor]]]])

slots.molecular_functions = Slot(uri=DISMECH.molecular_functions, name="molecular_functions", curie=DISMECH.curie('molecular_functions'),
                   model_uri=DISMECH.molecular_functions, domain=None, range=Optional[Union[Union[dict, MolecularFunctionDescriptor], list[Union[dict, MolecularFunctionDescriptor]]]])

slots.epidemiology = Slot(uri=DISMECH.epidemiology, name="epidemiology", curie=DISMECH.curie('epidemiology'),
                   model_uri=DISMECH.epidemiology, domain=None, range=Optional[Union[dict[Union[str, EpidemiologyInfoName], Union[dict, EpidemiologyInfo]], list[Union[dict, EpidemiologyInfo]]]])

slots.examples = Slot(uri=DISMECH.examples, name="examples", curie=DISMECH.curie('examples'),
                   model_uri=DISMECH.examples, domain=None, range=Optional[Union[str, list[str]]])

slots.role = Slot(uri=DISMECH.role, name="role", curie=DISMECH.curie('role'),
                   model_uri=DISMECH.role, domain=None, range=Optional[str])

slots.conforms_to = Slot(uri=DISMECH.conforms_to, name="conforms_to", curie=DISMECH.curie('conforms_to'),
                   model_uri=DISMECH.conforms_to, domain=None, range=Optional[str])

slots.consequence = Slot(uri=DISMECH.consequence, name="consequence", curie=DISMECH.curie('consequence'),
                   model_uri=DISMECH.consequence, domain=None, range=Optional[str])

slots.consequences = Slot(uri=DISMECH.consequences, name="consequences", curie=DISMECH.curie('consequences'),
                   model_uri=DISMECH.consequences, domain=None, range=Optional[Union[str, list[str]]])

slots.gene = Slot(uri=DISMECH.gene, name="gene", curie=DISMECH.curie('gene'),
                   model_uri=DISMECH.gene, domain=None, range=Optional[Union[dict, GeneDescriptor]])

slots.pathways = Slot(uri=DISMECH.pathways, name="pathways", curie=DISMECH.curie('pathways'),
                   model_uri=DISMECH.pathways, domain=None, range=Optional[Union[Union[dict, BiologicalProcessDescriptor], list[Union[dict, BiologicalProcessDescriptor]]]])

slots.downstream = Slot(uri=DISMECH.downstream, name="downstream", curie=DISMECH.curie('downstream'),
                   model_uri=DISMECH.downstream, domain=None, range=Optional[Union[Union[dict, CausalEdge], list[Union[dict, CausalEdge]]]])

slots.genes = Slot(uri=DISMECH.genes, name="genes", curie=DISMECH.curie('genes'),
                   model_uri=DISMECH.genes, domain=None, range=Optional[Union[Union[dict, GeneDescriptor], list[Union[dict, GeneDescriptor]]]])

slots.subtypes = Slot(uri=DISMECH.subtypes, name="subtypes", curie=DISMECH.curie('subtypes'),
                   model_uri=DISMECH.subtypes, domain=None, range=Optional[Union[str, list[str]]])

slots.has_subtypes = Slot(uri=DISMECH.has_subtypes, name="has_subtypes", curie=DISMECH.curie('has_subtypes'),
                   model_uri=DISMECH.has_subtypes, domain=None, range=Optional[Union[dict[Union[str, SubtypeName], Union[dict, Subtype]], list[Union[dict, Subtype]]]])

slots.classification = Slot(uri=DISMECH.classification, name="classification", curie=DISMECH.curie('classification'),
                   model_uri=DISMECH.classification, domain=None, range=Optional[str])

slots.children = Slot(uri=DISMECH.children, name="children", curie=DISMECH.curie('children'),
                   model_uri=DISMECH.children, domain=None, range=Optional[Union[str, list[str]]])

slots.subtype_frequency = Slot(uri=DISMECH.subtype_frequency, name="subtype_frequency", curie=DISMECH.curie('subtype_frequency'),
                   model_uri=DISMECH.subtype_frequency, domain=None, range=Optional[str])

slots.cellular_components = Slot(uri=DISMECH.cellular_components, name="cellular_components", curie=DISMECH.curie('cellular_components'),
                   model_uri=DISMECH.cellular_components, domain=None, range=Optional[Union[Union[dict, CellularComponentDescriptor], list[Union[dict, CellularComponentDescriptor]]]])

slots.protein_complexes = Slot(uri=DISMECH.protein_complexes, name="protein_complexes", curie=DISMECH.curie('protein_complexes'),
                   model_uri=DISMECH.protein_complexes, domain=None, range=Optional[Union[Union[dict, ProteinComplexDescriptor], list[Union[dict, ProteinComplexDescriptor]]]])

slots.chemical_entities = Slot(uri=DISMECH.chemical_entities, name="chemical_entities", curie=DISMECH.curie('chemical_entities'),
                   model_uri=DISMECH.chemical_entities, domain=None, range=Optional[Union[Union[dict, ChemicalEntityDescriptor], list[Union[dict, ChemicalEntityDescriptor]]]])

slots.gene_products = Slot(uri=DISMECH.gene_products, name="gene_products", curie=DISMECH.curie('gene_products'),
                   model_uri=DISMECH.gene_products, domain=None, range=Optional[Union[Union[dict, GeneProductDescriptor], list[Union[dict, GeneProductDescriptor]]]])

slots.triggers = Slot(uri=DISMECH.triggers, name="triggers", curie=DISMECH.curie('triggers'),
                   model_uri=DISMECH.triggers, domain=None, range=Optional[Union[Union[dict, TriggerDescriptor], list[Union[dict, TriggerDescriptor]]]])

slots.assays = Slot(uri=DISMECH.assays, name="assays", curie=DISMECH.curie('assays'),
                   model_uri=DISMECH.assays, domain=None, range=Optional[Union[Union[dict, AssayDescriptor], list[Union[dict, AssayDescriptor]]]])

slots.disease_term = Slot(uri=DISMECH.disease_term, name="disease_term", curie=DISMECH.curie('disease_term'),
                   model_uri=DISMECH.disease_term, domain=None, range=Optional[Union[dict, DiseaseDescriptor]])

slots.phenotype_term = Slot(uri=DISMECH.phenotype_term, name="phenotype_term", curie=DISMECH.curie('phenotype_term'),
                   model_uri=DISMECH.phenotype_term, domain=None, range=Optional[Union[dict, PhenotypeDescriptor]])

slots.inheritance_term = Slot(uri=DISMECH.inheritance_term, name="inheritance_term", curie=DISMECH.curie('inheritance_term'),
                   model_uri=DISMECH.inheritance_term, domain=None, range=Optional[Union[dict, InheritanceDescriptor]])

slots.gene_term = Slot(uri=DISMECH.gene_term, name="gene_term", curie=DISMECH.curie('gene_term'),
                   model_uri=DISMECH.gene_term, domain=None, range=Optional[Union[dict, GeneDescriptor]])

slots.treatment_term = Slot(uri=DISMECH.treatment_term, name="treatment_term", curie=DISMECH.curie('treatment_term'),
                   model_uri=DISMECH.treatment_term, domain=None, range=Optional[Union[dict, TreatmentDescriptor]])

slots.action_category = Slot(uri=DISMECH.action_category, name="action_category", curie=DISMECH.curie('action_category'),
                   model_uri=DISMECH.action_category, domain=None, range=Optional[Union[str, "MedicalActionCategoryEnum"]])

slots.regimen_term = Slot(uri=DISMECH.regimen_term, name="regimen_term", curie=DISMECH.curie('regimen_term'),
                   model_uri=DISMECH.regimen_term, domain=None, range=Optional[Union[dict, RegimenDescriptor]])

slots.biomarker_term = Slot(uri=DISMECH.biomarker_term, name="biomarker_term", curie=DISMECH.curie('biomarker_term'),
                   model_uri=DISMECH.biomarker_term, domain=None, range=Optional[Union[dict, BiomarkerDescriptor]])

slots.readouts = Slot(uri=DISMECH.readouts, name="readouts", curie=DISMECH.curie('readouts'),
                   model_uri=DISMECH.readouts, domain=None, range=Optional[Union[Union[dict, BiomarkerReadout], list[Union[dict, BiomarkerReadout]]]])

slots.relationship = Slot(uri=DISMECH.relationship, name="relationship", curie=DISMECH.curie('relationship'),
                   model_uri=DISMECH.relationship, domain=None, range=Optional[Union[str, "BiomarkerReadoutRelationshipEnum"]])

slots.direction = Slot(uri=DISMECH.direction, name="direction", curie=DISMECH.curie('direction'),
                   model_uri=DISMECH.direction, domain=None, range=Optional[Union[str, "BiomarkerReadoutDirectionEnum"]])

slots.endpoint_context = Slot(uri=DISMECH.endpoint_context, name="endpoint_context", curie=DISMECH.curie('endpoint_context'),
                   model_uri=DISMECH.endpoint_context, domain=None, range=Optional[Union[str, "BiomarkerEndpointContextEnum"]])

slots.regulatory_endpoint_refs = Slot(uri=DISMECH.regulatory_endpoint_refs, name="regulatory_endpoint_refs", curie=DISMECH.curie('regulatory_endpoint_refs'),
                   model_uri=DISMECH.regulatory_endpoint_refs, domain=None, range=Optional[Union[str, list[str]]])

slots.interpretation = Slot(uri=DISMECH.interpretation, name="interpretation", curie=DISMECH.curie('interpretation'),
                   model_uri=DISMECH.interpretation, domain=None, range=Optional[str])

slots.reports_on = Slot(uri=DISMECH.reports_on, name="reports_on", curie=DISMECH.curie('reports_on'),
                   model_uri=DISMECH.reports_on, domain=None, range=Optional[Union[Union[dict, PhenotypeReadout], list[Union[dict, PhenotypeReadout]]]])

slots.row_id = Slot(uri=DISMECH.row_id, name="row_id", curie=DISMECH.curie('row_id'),
                   model_uri=DISMECH.row_id, domain=None, range=URIRef)

slots.source_table = Slot(uri=DISMECH.source_table, name="source_table", curie=DISMECH.curie('source_table'),
                   model_uri=DISMECH.source_table, domain=None, range=Optional[Union[str, "SurrogateEndpointTableEnum"]])

slots.source_sheet = Slot(uri=DISMECH.source_sheet, name="source_sheet", curie=DISMECH.curie('source_sheet'),
                   model_uri=DISMECH.source_sheet, domain=None, range=Optional[str])

slots.source_row_number = Slot(uri=DISMECH.source_row_number, name="source_row_number", curie=DISMECH.curie('source_row_number'),
                   model_uri=DISMECH.source_row_number, domain=None, range=Optional[int])

slots.source_url = Slot(uri=DISMECH.source_url, name="source_url", curie=DISMECH.curie('source_url'),
                   model_uri=DISMECH.source_url, domain=None, range=Optional[Union[str, URI]])

slots.source_workbook_url = Slot(uri=DISMECH.source_workbook_url, name="source_workbook_url", curie=DISMECH.curie('source_workbook_url'),
                   model_uri=DISMECH.source_workbook_url, domain=None, range=Optional[Union[str, URI]])

slots.source_workbook_sha256 = Slot(uri=DISMECH.source_workbook_sha256, name="source_workbook_sha256", curie=DISMECH.curie('source_workbook_sha256'),
                   model_uri=DISMECH.source_workbook_sha256, domain=None, range=Optional[str])

slots.source_content_current_as_of = Slot(uri=DISMECH.source_content_current_as_of, name="source_content_current_as_of", curie=DISMECH.curie('source_content_current_as_of'),
                   model_uri=DISMECH.source_content_current_as_of, domain=None, range=Optional[Union[str, XSDDate]])

slots.retrieved_date = Slot(uri=DISMECH.retrieved_date, name="retrieved_date", curie=DISMECH.curie('retrieved_date'),
                   model_uri=DISMECH.retrieved_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.disease_or_use = Slot(uri=DISMECH.disease_or_use, name="disease_or_use", curie=DISMECH.curie('disease_or_use'),
                   model_uri=DISMECH.disease_or_use, domain=None, range=Optional[str])

slots.patient_population = Slot(uri=DISMECH.patient_population, name="patient_population", curie=DISMECH.curie('patient_population'),
                   model_uri=DISMECH.patient_population, domain=None, range=Optional[str])

slots.surrogate_endpoint = Slot(uri=DISMECH.surrogate_endpoint, name="surrogate_endpoint", curie=DISMECH.curie('surrogate_endpoint'),
                   model_uri=DISMECH.surrogate_endpoint, domain=None, range=Optional[str])

slots.approval_type = Slot(uri=DISMECH.approval_type, name="approval_type", curie=DISMECH.curie('approval_type'),
                   model_uri=DISMECH.approval_type, domain=None, range=Optional[Union[str, "SurrogateEndpointApprovalTypeEnum"]])

slots.drug_mechanism_of_action = Slot(uri=DISMECH.drug_mechanism_of_action, name="drug_mechanism_of_action", curie=DISMECH.curie('drug_mechanism_of_action'),
                   model_uri=DISMECH.drug_mechanism_of_action, domain=None, range=Optional[str])

slots.endpoint_validation_level = Slot(uri=DISMECH.endpoint_validation_level, name="endpoint_validation_level", curie=DISMECH.curie('endpoint_validation_level'),
                   model_uri=DISMECH.endpoint_validation_level, domain=None, range=Optional[Union[str, "SurrogateEndpointValidationLevelEnum"]])

slots.clinical_benefit_linkage = Slot(uri=DISMECH.clinical_benefit_linkage, name="clinical_benefit_linkage", curie=DISMECH.curie('clinical_benefit_linkage'),
                   model_uri=DISMECH.clinical_benefit_linkage, domain=None, range=Optional[Union[str, "ClinicalBenefitLinkageEnum"]])

slots.clinical_benefit = Slot(uri=DISMECH.clinical_benefit, name="clinical_benefit", curie=DISMECH.curie('clinical_benefit'),
                   model_uri=DISMECH.clinical_benefit, domain=None, range=Optional[str])

slots.clinical_benefit_linkage_basis = Slot(uri=DISMECH.clinical_benefit_linkage_basis, name="clinical_benefit_linkage_basis", curie=DISMECH.curie('clinical_benefit_linkage_basis'),
                   model_uri=DISMECH.clinical_benefit_linkage_basis, domain=None, range=Optional[str])

slots.footnotes = Slot(uri=DISMECH.footnotes, name="footnotes", curie=DISMECH.curie('footnotes'),
                   model_uri=DISMECH.footnotes, domain=None, range=Optional[Union[Union[str, "SurrogateEndpointFootnoteEnum"], list[Union[str, "SurrogateEndpointFootnoteEnum"]]]])

slots.context_of_use = Slot(uri=DISMECH.context_of_use, name="context_of_use", curie=DISMECH.curie('context_of_use'),
                   model_uri=DISMECH.context_of_use, domain=None, range=Optional[str])

slots.mapping_status = Slot(uri=DISMECH.mapping_status, name="mapping_status", curie=DISMECH.curie('mapping_status'),
                   model_uri=DISMECH.mapping_status, domain=None, range=Optional[Union[str, "SurrogateEndpointMappingStatusEnum"]])

slots.mapped_diseases = Slot(uri=DISMECH.mapped_diseases, name="mapped_diseases", curie=DISMECH.curie('mapped_diseases'),
                   model_uri=DISMECH.mapped_diseases, domain=None, range=Optional[Union[str, list[str]]])

slots.mapped_disease_files = Slot(uri=DISMECH.mapped_disease_files, name="mapped_disease_files", curie=DISMECH.curie('mapped_disease_files'),
                   model_uri=DISMECH.mapped_disease_files, domain=None, range=Optional[Union[str, list[str]]])

slots.surrogate_endpoints = Slot(uri=DISMECH.surrogate_endpoints, name="surrogate_endpoints", curie=DISMECH.curie('surrogate_endpoints'),
                   model_uri=DISMECH.surrogate_endpoints, domain=None, range=Optional[Union[dict[Union[str, SurrogateEndpointRowId], Union[dict, SurrogateEndpoint]], list[Union[dict, SurrogateEndpoint]]]])

slots.finding_term = Slot(uri=DISMECH.finding_term, name="finding_term", curie=DISMECH.curie('finding_term'),
                   model_uri=DISMECH.finding_term, domain=None, range=Optional[Union[dict, HistopathologyFindingDescriptor]])

slots.diagnosis_term = Slot(uri=DISMECH.diagnosis_term, name="diagnosis_term", curie=DISMECH.curie('diagnosis_term'),
                   model_uri=DISMECH.diagnosis_term, domain=None, range=Optional[Union[dict, TreatmentDescriptor]])

slots.subtype_term = Slot(uri=DISMECH.subtype_term, name="subtype_term", curie=DISMECH.curie('subtype_term'),
                   model_uri=DISMECH.subtype_term, domain=None, range=Optional[Union[dict, SubtypeDescriptor]])

slots.infectious_agent_term = Slot(uri=DISMECH.infectious_agent_term, name="infectious_agent_term", curie=DISMECH.curie('infectious_agent_term'),
                   model_uri=DISMECH.infectious_agent_term, domain=None, range=Optional[Union[dict, OrganismDescriptor]])

slots.exposure_term = Slot(uri=DISMECH.exposure_term, name="exposure_term", curie=DISMECH.curie('exposure_term'),
                   model_uri=DISMECH.exposure_term, domain=None, range=Optional[Union[dict, ExposureDescriptor]])

slots.life_cycle_stage_term = Slot(uri=DISMECH.life_cycle_stage_term, name="life_cycle_stage_term", curie=DISMECH.curie('life_cycle_stage_term'),
                   model_uri=DISMECH.life_cycle_stage_term, domain=None, range=Optional[Union[dict, LifeCycleStageDescriptor]])

slots.environment_context = Slot(uri=DISMECH.environment_context, name="environment_context", curie=DISMECH.curie('environment_context'),
                   model_uri=DISMECH.environment_context, domain=None, range=Optional[Union[dict, EnvironmentDescriptor]])

slots.food_source = Slot(uri=DISMECH.food_source, name="food_source", curie=DISMECH.curie('food_source'),
                   model_uri=DISMECH.food_source, domain=None, range=Optional[Union[dict, FoodDescriptor]])

slots.mechanisms = Slot(uri=DISMECH.mechanisms, name="mechanisms", curie=DISMECH.curie('mechanisms'),
                   model_uri=DISMECH.mechanisms, domain=None, range=Optional[Union[str, list[str]]])

slots.category = Slot(uri=DISMECH.category, name="category", curie=DISMECH.curie('category'),
                   model_uri=DISMECH.category, domain=None, range=Optional[str])

slots.frequency = Slot(uri=DISMECH.frequency, name="frequency", curie=DISMECH.curie('frequency'),
                   model_uri=DISMECH.frequency, domain=None, range=Optional[Union[dict, Any]])

slots.diagnostic = Slot(uri=DISMECH.diagnostic, name="diagnostic", curie=DISMECH.curie('diagnostic'),
                   model_uri=DISMECH.diagnostic, domain=None, range=Optional[Union[bool, Bool]])

slots.sequelae = Slot(uri=DISMECH.sequelae, name="sequelae", curie=DISMECH.curie('sequelae'),
                   model_uri=DISMECH.sequelae, domain=None, range=Optional[Union[Union[dict, CausalEdge], list[Union[dict, CausalEdge]]]])

slots.context = Slot(uri=DISMECH.context, name="context", curie=DISMECH.curie('context'),
                   model_uri=DISMECH.context, domain=None, range=Optional[str])

slots.severity = Slot(uri=DISMECH.severity, name="severity", curie=DISMECH.curie('severity'),
                   model_uri=DISMECH.severity, domain=None, range=Optional[Union[dict, Any]])

slots.burden_level = Slot(uri=DISMECH.burden_level, name="burden_level", curie=DISMECH.curie('burden_level'),
                   model_uri=DISMECH.burden_level, domain=None, range=Optional[Union[str, "ClinicalBurdenLevelEnum"]])

slots.presence = Slot(uri=DISMECH.presence, name="presence", curie=DISMECH.curie('presence'),
                   model_uri=DISMECH.presence, domain=None, range=Optional[str])

slots.specificity = Slot(uri=DISMECH.specificity, name="specificity", curie=DISMECH.curie('specificity'),
                   model_uri=DISMECH.specificity, domain=None, range=Optional[str])

slots.synonyms = Slot(uri=DISMECH.synonyms, name="synonyms", curie=DISMECH.curie('synonyms'),
                   model_uri=DISMECH.synonyms, domain=None, range=Optional[Union[str, list[str]]])

slots.association = Slot(uri=DISMECH.association, name="association", curie=DISMECH.curie('association'),
                   model_uri=DISMECH.association, domain=None, range=Optional[str])

slots.relationship_type = Slot(uri=DISMECH.relationship_type, name="relationship_type", curie=DISMECH.curie('relationship_type'),
                   model_uri=DISMECH.relationship_type, domain=None, range=Optional[Union[str, "GeneDiseaseRelationshipEnum"]])

slots.variant_origin = Slot(uri=DISMECH.variant_origin, name="variant_origin", curie=DISMECH.curie('variant_origin'),
                   model_uri=DISMECH.variant_origin, domain=None, range=Optional[Union[str, "VariantOriginEnum"]])

slots.inheritance = Slot(uri=DISMECH.inheritance, name="inheritance", curie=DISMECH.curie('inheritance'),
                   model_uri=DISMECH.inheritance, domain=None, range=Optional[Union[dict[Union[str, InheritanceName], Union[dict, Inheritance]], list[Union[dict, Inheritance]]]])

slots.penetrance = Slot(uri=DISMECH.penetrance, name="penetrance", curie=DISMECH.curie('penetrance'),
                   model_uri=DISMECH.penetrance, domain=None, range=Optional[Union[str, "PenetranceEnum"]])

slots.penetrance_percentage = Slot(uri=DISMECH.penetrance_percentage, name="penetrance_percentage", curie=DISMECH.curie('penetrance_percentage'),
                   model_uri=DISMECH.penetrance_percentage, domain=None, range=Optional[str])

slots.expressivity = Slot(uri=DISMECH.expressivity, name="expressivity", curie=DISMECH.curie('expressivity'),
                   model_uri=DISMECH.expressivity, domain=None, range=Optional[Union[str, "ExpressivityEnum"]])

slots.de_novo_rate = Slot(uri=DISMECH.de_novo_rate, name="de_novo_rate", curie=DISMECH.curie('de_novo_rate'),
                   model_uri=DISMECH.de_novo_rate, domain=None, range=Optional[str])

slots.parent_of_origin_effect = Slot(uri=DISMECH.parent_of_origin_effect, name="parent_of_origin_effect", curie=DISMECH.curie('parent_of_origin_effect'),
                   model_uri=DISMECH.parent_of_origin_effect, domain=None, range=Optional[str])

slots.variants = Slot(uri=DISMECH.variants, name="variants", curie=DISMECH.curie('variants'),
                   model_uri=DISMECH.variants, domain=None, range=Optional[Union[dict[Union[str, VariantName], Union[dict, Variant]], list[Union[dict, Variant]]]])

slots.features = Slot(uri=DISMECH.features, name="features", curie=DISMECH.curie('features'),
                   model_uri=DISMECH.features, domain=None, range=Optional[str])

slots.chemicals = Slot(uri=DISMECH.chemicals, name="chemicals", curie=DISMECH.curie('chemicals'),
                   model_uri=DISMECH.chemicals, domain=None, range=Optional[Union[str, list[str]]])

slots.alleles = Slot(uri=DISMECH.alleles, name="alleles", curie=DISMECH.curie('alleles'),
                   model_uri=DISMECH.alleles, domain=None, range=Optional[Union[str, list[str]]])

slots.species = Slot(uri=DISMECH.species, name="species", curie=DISMECH.curie('species'),
                   model_uri=DISMECH.species, domain=None, range=Optional[str])

slots.effect = Slot(uri=DISMECH.effect, name="effect", curie=DISMECH.curie('effect'),
                   model_uri=DISMECH.effect, domain=None, range=Optional[str])

slots.parents = Slot(uri=DISMECH.parents, name="parents", curie=DISMECH.curie('parents'),
                   model_uri=DISMECH.parents, domain=None, range=Optional[Union[str, list[str]]])

slots.prevalence = Slot(uri=DISMECH.prevalence, name="prevalence", curie=DISMECH.curie('prevalence'),
                   model_uri=DISMECH.prevalence, domain=None, range=Optional[Union[Union[dict, Prevalence], list[Union[dict, Prevalence]]]])

slots.progression = Slot(uri=DISMECH.progression, name="progression", curie=DISMECH.curie('progression'),
                   model_uri=DISMECH.progression, domain=None, range=Optional[Union[Union[dict, ProgressionInfo], list[Union[dict, ProgressionInfo]]]])

slots.clinical_burden = Slot(uri=DISMECH.clinical_burden, name="clinical_burden", curie=DISMECH.curie('clinical_burden'),
                   model_uri=DISMECH.clinical_burden, domain=None, range=Optional[Union[dict, ClinicalBurden]])

slots.pathophysiology = Slot(uri=DISMECH.pathophysiology, name="pathophysiology", curie=DISMECH.curie('pathophysiology'),
                   model_uri=DISMECH.pathophysiology, domain=None, range=Optional[Union[dict[Union[str, PathophysiologyName], Union[dict, Pathophysiology]], list[Union[dict, Pathophysiology]]]])

slots.stages = Slot(uri=DISMECH.stages, name="stages", curie=DISMECH.curie('stages'),
                   model_uri=DISMECH.stages, domain=None, range=Optional[Union[dict[Union[str, StageName], Union[dict, Stage]], list[Union[dict, Stage]]]])

slots.substages = Slot(uri=DISMECH.substages, name="substages", curie=DISMECH.curie('substages'),
                   model_uri=DISMECH.substages, domain=None, range=Optional[Union[dict[Union[str, StageName], Union[dict, Stage]], list[Union[dict, Stage]]]])

slots.phenotypes = Slot(uri=DISMECH.phenotypes, name="phenotypes", curie=DISMECH.curie('phenotypes'),
                   model_uri=DISMECH.phenotypes, domain=None, range=Optional[Union[dict[Union[str, PhenotypeName], Union[dict, Phenotype]], list[Union[dict, Phenotype]]]])

slots.histopathology = Slot(uri=DISMECH.histopathology, name="histopathology", curie=DISMECH.curie('histopathology'),
                   model_uri=DISMECH.histopathology, domain=None, range=Optional[Union[dict[Union[str, HistopathologyFindingName], Union[dict, HistopathologyFinding]], list[Union[dict, HistopathologyFinding]]]])

slots.imaging_findings = Slot(uri=DISMECH.imaging_findings, name="imaging_findings", curie=DISMECH.curie('imaging_findings'),
                   model_uri=DISMECH.imaging_findings, domain=None, range=Optional[Union[dict[Union[str, ImagingFindingName], Union[dict, ImagingFinding]], list[Union[dict, ImagingFinding]]]])

slots.modality = Slot(uri=DISMECH.modality, name="modality", curie=DISMECH.curie('modality'),
                   model_uri=DISMECH.modality, domain=None, range=Optional[Union[str, "ImagingModalityEnum"]])

slots.imaging_finding_term = Slot(uri=DISMECH.imaging_finding_term, name="imaging_finding_term", curie=DISMECH.curie('imaging_finding_term'),
                   model_uri=DISMECH.imaging_finding_term, domain=None, range=Optional[Union[dict, ImagingFindingDescriptor]])

slots.electrophysiology = Slot(uri=DISMECH.electrophysiology, name="electrophysiology", curie=DISMECH.curie('electrophysiology'),
                   model_uri=DISMECH.electrophysiology, domain=None, range=Optional[Union[dict, ElectrophysiologyContext]])

slots.electrophysiology_modality = Slot(uri=DISMECH.electrophysiology_modality, name="electrophysiology_modality", curie=DISMECH.curie('electrophysiology_modality'),
                   model_uri=DISMECH.electrophysiology_modality, domain=None, range=Optional[Union[str, "ElectrophysiologyModalityEnum"]])

slots.ictal_state = Slot(uri=DISMECH.ictal_state, name="ictal_state", curie=DISMECH.curie('ictal_state'),
                   model_uri=DISMECH.ictal_state, domain=None, range=Optional[Union[str, "IctalStateEnum"]])

slots.recording_state = Slot(uri=DISMECH.recording_state, name="recording_state", curie=DISMECH.curie('recording_state'),
                   model_uri=DISMECH.recording_state, domain=None, range=Optional[Union[str, "EEGRecordingStateEnum"]])

slots.biochemical = Slot(uri=DISMECH.biochemical, name="biochemical", curie=DISMECH.curie('biochemical'),
                   model_uri=DISMECH.biochemical, domain=None, range=Optional[Union[dict[Union[str, BiochemicalName], Union[dict, Biochemical]], list[Union[dict, Biochemical]]]])

slots.genetic = Slot(uri=DISMECH.genetic, name="genetic", curie=DISMECH.curie('genetic'),
                   model_uri=DISMECH.genetic, domain=None, range=Optional[Union[dict[Union[str, GeneticName], Union[dict, Genetic]], list[Union[dict, Genetic]]]])

slots.environmental = Slot(uri=DISMECH.environmental, name="environmental", curie=DISMECH.curie('environmental'),
                   model_uri=DISMECH.environmental, domain=None, range=Optional[Union[dict[Union[str, EnvironmentalName], Union[dict, Environmental]], list[Union[dict, Environmental]]]])

slots.treatments = Slot(uri=DISMECH.treatments, name="treatments", curie=DISMECH.curie('treatments'),
                   model_uri=DISMECH.treatments, domain=None, range=Optional[Union[dict[Union[str, TreatmentName], Union[dict, Treatment]], list[Union[dict, Treatment]]]])

slots.categories = Slot(uri=DISMECH.categories, name="categories", curie=DISMECH.curie('categories'),
                   model_uri=DISMECH.categories, domain=None, range=Optional[Union[str, list[str]]])

slots.module_categories = Slot(uri=DISMECH.module_categories, name="module_categories", curie=DISMECH.curie('module_categories'),
                   model_uri=DISMECH.module_categories, domain=None, range=Optional[Union[Union[str, "ModuleCategoryEnum"], list[Union[str, "ModuleCategoryEnum"]]]])

slots.infectious_agent = Slot(uri=DISMECH.infectious_agent, name="infectious_agent", curie=DISMECH.curie('infectious_agent'),
                   model_uri=DISMECH.infectious_agent, domain=None, range=Optional[Union[dict[Union[str, InfectiousAgentName], Union[dict, InfectiousAgent]], list[Union[dict, InfectiousAgent]]]])

slots.agent_life_cycle = Slot(uri=DISMECH.agent_life_cycle, name="agent_life_cycle", curie=DISMECH.curie('agent_life_cycle'),
                   model_uri=DISMECH.agent_life_cycle, domain=None, range=Optional[Union[dict, AgentLifeCycle]])

slots.transmission = Slot(uri=DISMECH.transmission, name="transmission", curie=DISMECH.curie('transmission'),
                   model_uri=DISMECH.transmission, domain=None, range=Optional[Union[dict[Union[str, TransmissionName], Union[dict, Transmission]], list[Union[dict, Transmission]]]])

slots.life_cycle_stages = Slot(uri=DISMECH.life_cycle_stages, name="life_cycle_stages", curie=DISMECH.curie('life_cycle_stages'),
                   model_uri=DISMECH.life_cycle_stages, domain=None, range=Optional[Union[dict[Union[str, AgentLifeCycleStageName], Union[dict, AgentLifeCycleStage]], list[Union[dict, AgentLifeCycleStage]]]])

slots.hosts = Slot(uri=DISMECH.hosts, name="hosts", curie=DISMECH.curie('hosts'),
                   model_uri=DISMECH.hosts, domain=None, range=Optional[Union[Union[dict, HostDescriptor], list[Union[dict, HostDescriptor]]]])

slots.vectors = Slot(uri=DISMECH.vectors, name="vectors", curie=DISMECH.curie('vectors'),
                   model_uri=DISMECH.vectors, domain=None, range=Optional[Union[str, list[str]]])

slots.diagnosis = Slot(uri=DISMECH.diagnosis, name="diagnosis", curie=DISMECH.curie('diagnosis'),
                   model_uri=DISMECH.diagnosis, domain=None, range=Optional[Union[dict[Union[str, DiagnosisName], Union[dict, Diagnosis]], list[Union[dict, Diagnosis]]]])

slots.modeling_considerations = Slot(uri=DISMECH.modeling_considerations, name="modeling_considerations", curie=DISMECH.curie('modeling_considerations'),
                   model_uri=DISMECH.modeling_considerations, domain=None, range=Optional[Union[dict[Union[str, ModelingConsiderationName], Union[dict, ModelingConsideration]], list[Union[dict, ModelingConsideration]]]])

slots.mechanism = Slot(uri=DISMECH.mechanism, name="mechanism", curie=DISMECH.curie('mechanism'),
                   model_uri=DISMECH.mechanism, domain=None, range=Optional[Union[dict[Union[str, MechanismName], Union[dict, Mechanism]], list[Union[dict, Mechanism]]]])

slots.results = Slot(uri=DISMECH.results, name="results", curie=DISMECH.curie('results'),
                   model_uri=DISMECH.results, domain=None, range=Optional[str])

slots.markers = Slot(uri=DISMECH.markers, name="markers", curie=DISMECH.curie('markers'),
                   model_uri=DISMECH.markers, domain=None, range=Optional[str])

slots.diseases = Slot(uri=DISMECH.diseases, name="diseases", curie=DISMECH.curie('diseases'),
                   model_uri=DISMECH.diseases, domain=None, range=Optional[Union[dict[Union[str, DiseaseName], Union[dict, Disease]], list[Union[dict, Disease]]]])

slots.animal_models = Slot(uri=DISMECH.animal_models, name="animal_models", curie=DISMECH.curie('animal_models'),
                   model_uri=DISMECH.animal_models, domain=None, range=Optional[Union[Union[dict, AnimalModel], list[Union[dict, AnimalModel]]]])

slots.functional_effects = Slot(uri=DISMECH.functional_effects, name="functional_effects", curie=DISMECH.curie('functional_effects'),
                   model_uri=DISMECH.functional_effects, domain=None, range=Optional[Union[Union[dict, FunctionalEffect], list[Union[dict, FunctionalEffect]]]])

slots.genotype = Slot(uri=DISMECH.genotype, name="genotype", curie=DISMECH.curie('genotype'),
                   model_uri=DISMECH.genotype, domain=None, range=Optional[str])

slots.type = Slot(uri=DISMECH.type, name="type", curie=DISMECH.curie('type'),
                   model_uri=DISMECH.type, domain=None, range=Optional[str])

slots.clinical_significance = Slot(uri=DISMECH.clinical_significance, name="clinical_significance", curie=DISMECH.curie('clinical_significance'),
                   model_uri=DISMECH.clinical_significance, domain=None, range=Optional[Union[str, "ClinicalSignificanceEnum"]])

slots.background = Slot(uri=DISMECH.background, name="background", curie=DISMECH.curie('background'),
                   model_uri=DISMECH.background, domain=None, range=Optional[str])

slots.sequence_length = Slot(uri=DISMECH.sequence_length, name="sequence_length", curie=DISMECH.curie('sequence_length'),
                   model_uri=DISMECH.sequence_length, domain=None, range=Optional[int])

slots.identifiers = Slot(uri=DISMECH.identifiers, name="identifiers", curie=DISMECH.curie('identifiers'),
                   model_uri=DISMECH.identifiers, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.external_assertions = Slot(uri=DISMECH.external_assertions, name="external_assertions", curie=DISMECH.curie('external_assertions'),
                   model_uri=DISMECH.external_assertions, domain=None, range=Optional[Union[dict[Union[str, ExternalAssertionName], Union[dict, ExternalAssertion]], list[Union[dict, ExternalAssertion]]]])

slots.external_id = Slot(uri=DISMECH.external_id, name="external_id", curie=DISMECH.curie('external_id'),
                   model_uri=DISMECH.external_id, domain=None, range=Optional[str])

slots.assertion_type = Slot(uri=DISMECH.assertion_type, name="assertion_type", curie=DISMECH.curie('assertion_type'),
                   model_uri=DISMECH.assertion_type, domain=None, range=Optional[str])

slots.url = Slot(uri=DISMECH.url, name="url", curie=DISMECH.curie('url'),
                   model_uri=DISMECH.url, domain=None, range=Optional[Union[str, URI]])

slots.associated_phenotypes = Slot(uri=DISMECH.associated_phenotypes, name="associated_phenotypes", curie=DISMECH.curie('associated_phenotypes'),
                   model_uri=DISMECH.associated_phenotypes, domain=None, range=Optional[Union[str, list[str]]])

slots.minimum_value = Slot(uri=DISMECH.minimum_value, name="minimum_value", curie=DISMECH.curie('minimum_value'),
                   model_uri=DISMECH.minimum_value, domain=None, range=Optional[float])

slots.maximum_value = Slot(uri=DISMECH.maximum_value, name="maximum_value", curie=DISMECH.curie('maximum_value'),
                   model_uri=DISMECH.maximum_value, domain=None, range=Optional[float])

slots.mean_range = Slot(uri=DISMECH.mean_range, name="mean_range", curie=DISMECH.curie('mean_range'),
                   model_uri=DISMECH.mean_range, domain=None, range=Optional[str])

slots.factors = Slot(uri=DISMECH.factors, name="factors", curie=DISMECH.curie('factors'),
                   model_uri=DISMECH.factors, domain=None, range=Optional[Union[str, list[str]]])

slots.dataset_identifier = Slot(uri=DISMECH.dataset_identifier, name="dataset_identifier", curie=DISMECH.curie('dataset_identifier'),
                   model_uri=DISMECH.dataset_identifier, domain=None, range=Optional[str])

slots.threshold = Slot(uri=DISMECH.threshold, name="threshold", curie=DISMECH.curie('threshold'),
                   model_uri=DISMECH.threshold, domain=None, range=Optional[float])

slots.threshold_direction = Slot(uri=DISMECH.threshold_direction, name="threshold_direction", curie=DISMECH.curie('threshold_direction'),
                   model_uri=DISMECH.threshold_direction, domain=None, range=Optional[Union[str, "ThresholdDirectionEnum"]])

slots.severity_scale = Slot(uri=DISMECH.severity_scale, name="severity_scale", curie=DISMECH.curie('severity_scale'),
                   model_uri=DISMECH.severity_scale, domain=None, range=Optional[Union[dict[Union[str, SeverityTierName], Union[dict, SeverityTier]], list[Union[dict, SeverityTier]]]])

slots.unit = Slot(uri=DISMECH.unit, name="unit", curie=DISMECH.curie('unit'),
                   model_uri=DISMECH.unit, domain=None, range=Optional[str])

slots.loinc_term = Slot(uri=DISMECH.loinc_term, name="loinc_term", curie=DISMECH.curie('loinc_term'),
                   model_uri=DISMECH.loinc_term, domain=None, range=Optional[Union[dict, Term]])

slots.lower_bound = Slot(uri=DISMECH.lower_bound, name="lower_bound", curie=DISMECH.curie('lower_bound'),
                   model_uri=DISMECH.lower_bound, domain=None, range=Optional[float])

slots.upper_bound = Slot(uri=DISMECH.upper_bound, name="upper_bound", curie=DISMECH.curie('upper_bound'),
                   model_uri=DISMECH.upper_bound, domain=None, range=Optional[float])

slots.reference_ranges = Slot(uri=DISMECH.reference_ranges, name="reference_ranges", curie=DISMECH.curie('reference_ranges'),
                   model_uri=DISMECH.reference_ranges, domain=None, range=Optional[Union[Union[dict, ReferenceRange], list[Union[dict, ReferenceRange]]]])

slots.interpretation_bands = Slot(uri=DISMECH.interpretation_bands, name="interpretation_bands", curie=DISMECH.curie('interpretation_bands'),
                   model_uri=DISMECH.interpretation_bands, domain=None, range=Optional[Union[dict[Union[str, ReferenceRangeBandName], Union[dict, ReferenceRangeBand]], list[Union[dict, ReferenceRangeBand]]]])

slots.abnormal_flag = Slot(uri=DISMECH.abnormal_flag, name="abnormal_flag", curie=DISMECH.curie('abnormal_flag'),
                   model_uri=DISMECH.abnormal_flag, domain=None, range=Optional[Union[str, "AbnormalFlagEnum"]])

slots.function = Slot(uri=DISMECH.function, name="function", curie=DISMECH.curie('function'),
                   model_uri=DISMECH.function, domain=None, range=Optional[str])

slots.regulatory_category = Slot(uri=DISMECH.regulatory_category, name="regulatory_category", curie=DISMECH.curie('regulatory_category'),
                   model_uri=DISMECH.regulatory_category, domain=None, range=Optional[Union[str, "RegulatoryVariantCategoryEnum"]])

slots.regulatory_element_type = Slot(uri=DISMECH.regulatory_element_type, name="regulatory_element_type", curie=DISMECH.curie('regulatory_element_type'),
                   model_uri=DISMECH.regulatory_element_type, domain=None, range=Optional[Union[str, "RegulatoryElementTypeEnum"]])

slots.affected_cell_types = Slot(uri=DISMECH.affected_cell_types, name="affected_cell_types", curie=DISMECH.curie('affected_cell_types'),
                   model_uri=DISMECH.affected_cell_types, domain=None, range=Optional[Union[Union[dict, CellTypeDescriptor], list[Union[dict, CellTypeDescriptor]]]])

slots.affected_developmental_stage = Slot(uri=DISMECH.affected_developmental_stage, name="affected_developmental_stage", curie=DISMECH.curie('affected_developmental_stage'),
                   model_uri=DISMECH.affected_developmental_stage, domain=None, range=Optional[str])

slots.regulatory_mechanism = Slot(uri=DISMECH.regulatory_mechanism, name="regulatory_mechanism", curie=DISMECH.curie('regulatory_mechanism'),
                   model_uri=DISMECH.regulatory_mechanism, domain=None, range=Optional[str])

slots.target = Slot(uri=DISMECH.target, name="target", curie=DISMECH.curie('target'),
                   model_uri=DISMECH.target, domain=None, range=str)

slots.hypothesis_groups = Slot(uri=DISMECH.hypothesis_groups, name="hypothesis_groups", curie=DISMECH.curie('hypothesis_groups'),
                   model_uri=DISMECH.hypothesis_groups, domain=None, range=Optional[Union[str, list[str]]])

slots.causal_link_type = Slot(uri=DISMECH.causal_link_type, name="causal_link_type", curie=DISMECH.curie('causal_link_type'),
                   model_uri=DISMECH.causal_link_type, domain=None, range=Optional[Union[str, "CausalLinkTypeEnum"]])

slots.intermediate_mechanisms = Slot(uri=DISMECH.intermediate_mechanisms, name="intermediate_mechanisms", curie=DISMECH.curie('intermediate_mechanisms'),
                   model_uri=DISMECH.intermediate_mechanisms, domain=None, range=Optional[Union[str, list[str]]])

slots.hypothesis_group_id = Slot(uri=DISMECH.hypothesis_group_id, name="hypothesis_group_id", curie=DISMECH.curie('hypothesis_group_id'),
                   model_uri=DISMECH.hypothesis_group_id, domain=None, range=Optional[str])

slots.hypothesis_label = Slot(uri=DISMECH.hypothesis_label, name="hypothesis_label", curie=DISMECH.curie('hypothesis_label'),
                   model_uri=DISMECH.hypothesis_label, domain=None, range=Optional[str])

slots.applies_to_subtypes = Slot(uri=DISMECH.applies_to_subtypes, name="applies_to_subtypes", curie=DISMECH.curie('applies_to_subtypes'),
                   model_uri=DISMECH.applies_to_subtypes, domain=None, range=Optional[Union[str, list[str]]])

slots.discussion_id = Slot(uri=DISMECH.discussion_id, name="discussion_id", curie=DISMECH.curie('discussion_id'),
                   model_uri=DISMECH.discussion_id, domain=None, range=Optional[str])

slots.prompt = Slot(uri=DISMECH.prompt, name="prompt", curie=DISMECH.curie('prompt'),
                   model_uri=DISMECH.prompt, domain=None, range=Optional[str])

slots.kind = Slot(uri=DISMECH.kind, name="kind", curie=DISMECH.curie('kind'),
                   model_uri=DISMECH.kind, domain=None, range=Optional[str])

slots.attaches_to = Slot(uri=DISMECH.attaches_to, name="attaches_to", curie=DISMECH.curie('attaches_to'),
                   model_uri=DISMECH.attaches_to, domain=None, range=Optional[Union[str, list[str]]])

slots.rationale = Slot(uri=DISMECH.rationale, name="rationale", curie=DISMECH.curie('rationale'),
                   model_uri=DISMECH.rationale, domain=None, range=Optional[str])

slots.proposed_experiments = Slot(uri=DISMECH.proposed_experiments, name="proposed_experiments", curie=DISMECH.curie('proposed_experiments'),
                   model_uri=DISMECH.proposed_experiments, domain=None, range=Optional[Union[dict[Union[str, ExperimentName], Union[dict, Experiment]], list[Union[dict, Experiment]]]])

slots.experiment_id = Slot(uri=DISMECH.experiment_id, name="experiment_id", curie=DISMECH.curie('experiment_id'),
                   model_uri=DISMECH.experiment_id, domain=None, range=Optional[str])

slots.experiment_type = Slot(uri=DISMECH.experiment_type, name="experiment_type", curie=DISMECH.curie('experiment_type'),
                   model_uri=DISMECH.experiment_type, domain=None, range=Optional[Union[dict, Descriptor]])

slots.model_systems = Slot(uri=DISMECH.model_systems, name="model_systems", curie=DISMECH.curie('model_systems'),
                   model_uri=DISMECH.model_systems, domain=None, range=Optional[Union[dict[Union[str, ExperimentalModelName], Union[dict, ExperimentalModel]], list[Union[dict, ExperimentalModel]]]])

slots.controls = Slot(uri=DISMECH.controls, name="controls", curie=DISMECH.curie('controls'),
                   model_uri=DISMECH.controls, domain=None, range=Optional[Union[dict[Union[str, ExperimentalControlName], Union[dict, ExperimentalControl]], list[Union[dict, ExperimentalControl]]]])

slots.decision_criterion = Slot(uri=DISMECH.decision_criterion, name="decision_criterion", curie=DISMECH.curie('decision_criterion'),
                   model_uri=DISMECH.decision_criterion, domain=None, range=Optional[str])

slots.would_support = Slot(uri=DISMECH.would_support, name="would_support", curie=DISMECH.curie('would_support'),
                   model_uri=DISMECH.would_support, domain=None, range=Optional[Union[str, list[str]]])

slots.would_refute = Slot(uri=DISMECH.would_refute, name="would_refute", curie=DISMECH.curie('would_refute'),
                   model_uri=DISMECH.would_refute, domain=None, range=Optional[Union[str, list[str]]])

slots.supporting_outcome = Slot(uri=DISMECH.supporting_outcome, name="supporting_outcome", curie=DISMECH.curie('supporting_outcome'),
                   model_uri=DISMECH.supporting_outcome, domain=None, range=Optional[Union[str, list[str]]])

slots.refuting_outcome = Slot(uri=DISMECH.refuting_outcome, name="refuting_outcome", curie=DISMECH.curie('refuting_outcome'),
                   model_uri=DISMECH.refuting_outcome, domain=None, range=Optional[Union[str, list[str]]])

slots.protocol_reference = Slot(uri=DISMECH.protocol_reference, name="protocol_reference", curie=DISMECH.curie('protocol_reference'),
                   model_uri=DISMECH.protocol_reference, domain=None, range=Optional[str])

slots.posed_by = Slot(uri=DISMECH.posed_by, name="posed_by", curie=DISMECH.curie('posed_by'),
                   model_uri=DISMECH.posed_by, domain=None, range=Optional[str])

slots.posed_date = Slot(uri=DISMECH.posed_date, name="posed_date", curie=DISMECH.curie('posed_date'),
                   model_uri=DISMECH.posed_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.resolved_date = Slot(uri=DISMECH.resolved_date, name="resolved_date", curie=DISMECH.curie('resolved_date'),
                   model_uri=DISMECH.resolved_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.resolution_note = Slot(uri=DISMECH.resolution_note, name="resolution_note", curie=DISMECH.curie('resolution_note'),
                   model_uri=DISMECH.resolution_note, domain=None, range=Optional[str])

slots.discussions = Slot(uri=DISMECH.discussions, name="discussions", curie=DISMECH.curie('discussions'),
                   model_uri=DISMECH.discussions, domain=None, range=Optional[Union[Union[dict, Discussion], list[Union[dict, Discussion]]]])

slots.target_phenotypes = Slot(uri=DISMECH.target_phenotypes, name="target_phenotypes", curie=DISMECH.curie('target_phenotypes'),
                   model_uri=DISMECH.target_phenotypes, domain=None, range=Optional[Union[Union[dict, PhenotypeDescriptor], list[Union[dict, PhenotypeDescriptor]]]])

slots.target_mechanisms = Slot(uri=DISMECH.target_mechanisms, name="target_mechanisms", curie=DISMECH.curie('target_mechanisms'),
                   model_uri=DISMECH.target_mechanisms, domain=None, range=Optional[Union[Union[dict, TreatmentMechanismTarget], list[Union[dict, TreatmentMechanismTarget]]]])

slots.modeled_mechanisms = Slot(uri=DISMECH.modeled_mechanisms, name="modeled_mechanisms", curie=DISMECH.curie('modeled_mechanisms'),
                   model_uri=DISMECH.modeled_mechanisms, domain=None, range=Optional[Union[Union[dict, ModelMechanismLink], list[Union[dict, ModelMechanismLink]]]])

slots.fidelity = Slot(uri=DISMECH.fidelity, name="fidelity", curie=DISMECH.curie('fidelity'),
                   model_uri=DISMECH.fidelity, domain=None, range=Optional[Union[str, "ModelFidelityEnum"]])

slots.limitations = Slot(uri=DISMECH.limitations, name="limitations", curie=DISMECH.curie('limitations'),
                   model_uri=DISMECH.limitations, domain=None, range=Optional[str])

slots.influences_mechanisms = Slot(uri=DISMECH.influences_mechanisms, name="influences_mechanisms", curie=DISMECH.curie('influences_mechanisms'),
                   model_uri=DISMECH.influences_mechanisms, domain=None, range=Optional[Union[Union[dict, EnvironmentalMechanismTarget], list[Union[dict, EnvironmentalMechanismTarget]]]])

slots.environmental_effect = Slot(uri=DISMECH.environmental_effect, name="environmental_effect", curie=DISMECH.curie('environmental_effect'),
                   model_uri=DISMECH.environmental_effect, domain=None, range=Optional[Union[str, "EnvironmentalEffectEnum"]])

slots.treatment_effect = Slot(uri=DISMECH.treatment_effect, name="treatment_effect", curie=DISMECH.curie('treatment_effect'),
                   model_uri=DISMECH.treatment_effect, domain=None, range=Optional[Union[str, "TreatmentEffectEnum"]])

slots.pdb_structures = Slot(uri=DISMECH.pdb_structures, name="pdb_structures", curie=DISMECH.curie('pdb_structures'),
                   model_uri=DISMECH.pdb_structures, domain=None, range=Optional[Union[Union[dict, ProteinStructure], list[Union[dict, ProteinStructure]]]])

slots.therapeutic_modality = Slot(uri=DISMECH.therapeutic_modality, name="therapeutic_modality", curie=DISMECH.curie('therapeutic_modality'),
                   model_uri=DISMECH.therapeutic_modality, domain=None, range=Optional[Union[str, "TherapeuticModalityEnum"]])

slots.aso_details = Slot(uri=DISMECH.aso_details, name="aso_details", curie=DISMECH.curie('aso_details'),
                   model_uri=DISMECH.aso_details, domain=None, range=Optional[Union[dict, AntisenseOligonucleotideDetail]])

slots.aso_mechanism = Slot(uri=DISMECH.aso_mechanism, name="aso_mechanism", curie=DISMECH.curie('aso_mechanism'),
                   model_uri=DISMECH.aso_mechanism, domain=None, range=Optional[Union[str, "AsoMechanismEnum"]])

slots.target_gene = Slot(uri=DISMECH.target_gene, name="target_gene", curie=DISMECH.curie('target_gene'),
                   model_uri=DISMECH.target_gene, domain=None, range=Optional[Union[dict, GeneDescriptor]])

slots.target_transcript = Slot(uri=DISMECH.target_transcript, name="target_transcript", curie=DISMECH.curie('target_transcript'),
                   model_uri=DISMECH.target_transcript, domain=None, range=Optional[str])

slots.target_exon = Slot(uri=DISMECH.target_exon, name="target_exon", curie=DISMECH.curie('target_exon'),
                   model_uri=DISMECH.target_exon, domain=None, range=Optional[str])

slots.aso_chemistry = Slot(uri=DISMECH.aso_chemistry, name="aso_chemistry", curie=DISMECH.curie('aso_chemistry'),
                   model_uri=DISMECH.aso_chemistry, domain=None, range=Optional[Union[str, "AsoChemistryEnum"]])

slots.conjugation = Slot(uri=DISMECH.conjugation, name="conjugation", curie=DISMECH.curie('conjugation'),
                   model_uri=DISMECH.conjugation, domain=None, range=Optional[Union[str, "AsoConjugationEnum"]])

slots.mechanism_confidence = Slot(uri=DISMECH.mechanism_confidence, name="mechanism_confidence", curie=DISMECH.curie('mechanism_confidence'),
                   model_uri=DISMECH.mechanism_confidence, domain=None, range=Optional[Union[str, "MechanismConfidenceEnum"]])

slots.biological_scale = Slot(uri=DISMECH.biological_scale, name="biological_scale", curie=DISMECH.curie('biological_scale'),
                   model_uri=DISMECH.biological_scale, domain=None, range=Optional[Union[str, "BiologicalScaleEnum"]])

slots.accession = Slot(uri=DISMECH.accession, name="accession", curie=DISMECH.curie('accession'),
                   model_uri=DISMECH.accession, domain=None, range=URIRef)

slots.organism = Slot(uri=DISMECH.organism, name="organism", curie=DISMECH.curie('organism'),
                   model_uri=DISMECH.organism, domain=None, range=Optional[Union[dict, OrganismDescriptor]])

slots.data_type = Slot(uri=DISMECH.data_type, name="data_type", curie=DISMECH.curie('data_type'),
                   model_uri=DISMECH.data_type, domain=None, range=Optional[Union[str, "DatasetTypeEnum"]])

slots.sample_types = Slot(uri=DISMECH.sample_types, name="sample_types", curie=DISMECH.curie('sample_types'),
                   model_uri=DISMECH.sample_types, domain=None, range=Optional[Union[Union[dict, SampleTypeDescriptor], list[Union[dict, SampleTypeDescriptor]]]])

slots.sample_count = Slot(uri=DISMECH.sample_count, name="sample_count", curie=DISMECH.curie('sample_count'),
                   model_uri=DISMECH.sample_count, domain=None, range=Optional[int])

slots.experimental_model_type = Slot(uri=DISMECH.experimental_model_type, name="experimental_model_type", curie=DISMECH.curie('experimental_model_type'),
                   model_uri=DISMECH.experimental_model_type, domain=None, range=Optional[Union[str, "ExperimentalModelTypeEnum"]])

slots.namo_type = Slot(uri=DISMECH.namo_type, name="namo_type", curie=DISMECH.curie('namo_type'),
                   model_uri=DISMECH.namo_type, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.conditions = Slot(uri=DISMECH.conditions, name="conditions", curie=DISMECH.curie('conditions'),
                   model_uri=DISMECH.conditions, domain=None, range=Optional[Union[str, list[str]]])

slots.cell_source = Slot(uri=DISMECH.cell_source, name="cell_source", curie=DISMECH.curie('cell_source'),
                   model_uri=DISMECH.cell_source, domain=None, range=Optional[str])

slots.culture_system = Slot(uri=DISMECH.culture_system, name="culture_system", curie=DISMECH.curie('culture_system'),
                   model_uri=DISMECH.culture_system, domain=None, range=Optional[str])

slots.exposures = Slot(uri=DISMECH.exposures, name="exposures", curie=DISMECH.curie('exposures'),
                   model_uri=DISMECH.exposures, domain=None, range=Optional[Union[Union[dict, ExposureDescriptor], list[Union[dict, ExposureDescriptor]]]])

slots.platform = Slot(uri=DISMECH.platform, name="platform", curie=DISMECH.curie('platform'),
                   model_uri=DISMECH.platform, domain=None, range=Optional[str])

slots.publication = Slot(uri=DISMECH.publication, name="publication", curie=DISMECH.curie('publication'),
                   model_uri=DISMECH.publication, domain=None, range=Optional[str])

slots.tissue_term = Slot(uri=DISMECH.tissue_term, name="tissue_term", curie=DISMECH.curie('tissue_term'),
                   model_uri=DISMECH.tissue_term, domain=None, range=Optional[Union[dict, AnatomicalEntityDescriptor]])

slots.cell_type_term = Slot(uri=DISMECH.cell_type_term, name="cell_type_term", curie=DISMECH.curie('cell_type_term'),
                   model_uri=DISMECH.cell_type_term, domain=None, range=Optional[Union[dict, CellTypeDescriptor]])

slots.experimental_models = Slot(uri=DISMECH.experimental_models, name="experimental_models", curie=DISMECH.curie('experimental_models'),
                   model_uri=DISMECH.experimental_models, domain=None, range=Optional[Union[dict[Union[str, ExperimentalModelName], Union[dict, ExperimentalModel]], list[Union[dict, ExperimentalModel]]]])

slots.datasets = Slot(uri=DISMECH.datasets, name="datasets", curie=DISMECH.curie('datasets'),
                   model_uri=DISMECH.datasets, domain=None, range=Optional[Union[dict[Union[str, DatasetAccession], Union[dict, Dataset]], list[Union[dict, Dataset]]]])

slots.clinical_trials = Slot(uri=DISMECH.clinical_trials, name="clinical_trials", curie=DISMECH.curie('clinical_trials'),
                   model_uri=DISMECH.clinical_trials, domain=None, range=Optional[Union[dict[Union[str, ClinicalTrialName], Union[dict, ClinicalTrial]], list[Union[dict, ClinicalTrial]]]])

slots.creation_date = Slot(uri=DISMECH.creation_date, name="creation_date", curie=DISMECH.curie('creation_date'),
                   model_uri=DISMECH.creation_date, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+\-]\d{2}:\d{2})$'))

slots.updated_date = Slot(uri=DISMECH.updated_date, name="updated_date", curie=DISMECH.curie('updated_date'),
                   model_uri=DISMECH.updated_date, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+\-]\d{2}:\d{2})$'))

slots.curation_history = Slot(uri=DISMECH.curation_history, name="curation_history", curie=DISMECH.curie('curation_history'),
                   model_uri=DISMECH.curation_history, domain=None, range=Optional[Union[Union[dict, CurationEvent], list[Union[dict, CurationEvent]]]])

slots.curation_timestamp = Slot(uri=DISMECH.curation_timestamp, name="curation_timestamp", curie=DISMECH.curie('curation_timestamp'),
                   model_uri=DISMECH.curation_timestamp, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.curation_model = Slot(uri=DISMECH.curation_model, name="curation_model", curie=DISMECH.curie('curation_model'),
                   model_uri=DISMECH.curation_model, domain=None, range=Optional[str])

slots.curation_action = Slot(uri=DISMECH.curation_action, name="curation_action", curie=DISMECH.curie('curation_action'),
                   model_uri=DISMECH.curation_action, domain=None, range=Optional[Union[str, "CurationActionEnum"]])

slots.curation_description = Slot(uri=DISMECH.curation_description, name="curation_description", curie=DISMECH.curie('curation_description'),
                   model_uri=DISMECH.curation_description, domain=None, range=Optional[str])

slots.model_type = Slot(uri=DISMECH.model_type, name="model_type", curie=DISMECH.curie('model_type'),
                   model_uri=DISMECH.model_type, domain=None, range=Optional[Union[str, "ComputationalModelTypeEnum"]])

slots.repository_url = Slot(uri=DISMECH.repository_url, name="repository_url", curie=DISMECH.curie('repository_url'),
                   model_uri=DISMECH.repository_url, domain=None, range=Optional[Union[str, URI]])

slots.model_id = Slot(uri=DISMECH.model_id, name="model_id", curie=DISMECH.curie('model_id'),
                   model_uri=DISMECH.model_id, domain=None, range=Optional[str])

slots.base_model = Slot(uri=DISMECH.base_model, name="base_model", curie=DISMECH.curie('base_model'),
                   model_uri=DISMECH.base_model, domain=None, range=Optional[str])

slots.model_software = Slot(uri=DISMECH.model_software, name="model_software", curie=DISMECH.curie('model_software'),
                   model_uri=DISMECH.model_software, domain=None, range=Optional[str])

slots.model_format = Slot(uri=DISMECH.model_format, name="model_format", curie=DISMECH.curie('model_format'),
                   model_uri=DISMECH.model_format, domain=None, range=Optional[str])

slots.perturbations = Slot(uri=DISMECH.perturbations, name="perturbations", curie=DISMECH.curie('perturbations'),
                   model_uri=DISMECH.perturbations, domain=None, range=Optional[Union[Union[dict, GeneDescriptor], list[Union[dict, GeneDescriptor]]]])

slots.variables = Slot(uri=DISMECH.variables, name="variables", curie=DISMECH.curie('variables'),
                   model_uri=DISMECH.variables, domain=None, range=Optional[Union[dict[Union[str, ModelVariableName], Union[dict, ModelVariable]], list[Union[dict, ModelVariable]]]])

slots.mappings_list = Slot(uri=DISMECH.mappings_list, name="mappings_list", curie=DISMECH.curie('mappings_list'),
                   model_uri=DISMECH.mappings_list, domain=None, range=Optional[Union[Union[dict, ModelVariableDescriptor], list[Union[dict, ModelVariableDescriptor]]]])

slots.computational_models = Slot(uri=DISMECH.computational_models, name="computational_models", curie=DISMECH.curie('computational_models'),
                   model_uri=DISMECH.computational_models, domain=None, range=Optional[Union[dict[Union[str, ComputationalModelName], Union[dict, ComputationalModel]], list[Union[dict, ComputationalModel]]]])

slots.classifications = Slot(uri=DISMECH.classifications, name="classifications", curie=DISMECH.curie('classifications'),
                   model_uri=DISMECH.classifications, domain=None, range=Optional[Union[dict, DiseaseClassifications]])

slots.definitions = Slot(uri=DISMECH.definitions, name="definitions", curie=DISMECH.curie('definitions'),
                   model_uri=DISMECH.definitions, domain=None, range=Optional[Union[dict[Union[str, DefinitionName], Union[dict, Definition]], list[Union[dict, Definition]]]])

slots.mappings = Slot(uri=DISMECH.mappings, name="mappings", curie=DISMECH.curie('mappings'),
                   model_uri=DISMECH.mappings, domain=None, range=Optional[Union[dict, DiseaseMappings]])

slots.icdo_morphology = Slot(uri=DISMECH.icdo_morphology, name="icdo_morphology", curie=DISMECH.curie('icdo_morphology'),
                   model_uri=DISMECH.icdo_morphology, domain=None, range=Optional[Union[dict, ICDOMorphologyAssignment]])

slots.harrisons_chapter = Slot(uri=DISMECH.harrisons_chapter, name="harrisons_chapter", curie=DISMECH.curie('harrisons_chapter'),
                   model_uri=DISMECH.harrisons_chapter, domain=None, range=Optional[Union[Union[dict, HarrisonsChapterAssignment], list[Union[dict, HarrisonsChapterAssignment]]]])

slots.lysosomal_storage_category = Slot(uri=DISMECH.lysosomal_storage_category, name="lysosomal_storage_category", curie=DISMECH.curie('lysosomal_storage_category'),
                   model_uri=DISMECH.lysosomal_storage_category, domain=None, range=Optional[Union[dict, LysosomalStorageAssignment]])

slots.mechanistic_category = Slot(uri=DISMECH.mechanistic_category, name="mechanistic_category", curie=DISMECH.curie('mechanistic_category'),
                   model_uri=DISMECH.mechanistic_category, domain=None, range=Optional[Union[Union[dict, MechanisticNosologyAssignment], list[Union[dict, MechanisticNosologyAssignment]]]])

slots.iuis_category = Slot(uri=DISMECH.iuis_category, name="iuis_category", curie=DISMECH.curie('iuis_category'),
                   model_uri=DISMECH.iuis_category, domain=None, range=Optional[Union[dict, IUISAssignment]])

slots.channelopathy_category = Slot(uri=DISMECH.channelopathy_category, name="channelopathy_category", curie=DISMECH.curie('channelopathy_category'),
                   model_uri=DISMECH.channelopathy_category, domain=None, range=Optional[Union[dict, ChannelopathyAssignment]])

slots.icimd_category = Slot(uri=DISMECH.icimd_category, name="icimd_category", curie=DISMECH.curie('icimd_category'),
                   model_uri=DISMECH.icimd_category, domain=None, range=Optional[Union[Union[dict, ICIMDAssignment], list[Union[dict, ICIMDAssignment]]]])

slots.isds_skeletal_category = Slot(uri=DISMECH.isds_skeletal_category, name="isds_skeletal_category", curie=DISMECH.curie('isds_skeletal_category'),
                   model_uri=DISMECH.isds_skeletal_category, domain=None, range=Optional[Union[Union[dict, ISDSNosologyAssignment], list[Union[dict, ISDSNosologyAssignment]]]])

slots.nih_research_priority = Slot(uri=DISMECH.nih_research_priority, name="nih_research_priority", curie=DISMECH.curie('nih_research_priority'),
                   model_uri=DISMECH.nih_research_priority, domain=None, range=Optional[Union[Union[dict, NIHResearchPriorityAssignment], list[Union[dict, NIHResearchPriorityAssignment]]]])

slots.occupational_classification = Slot(uri=DISMECH.occupational_classification, name="occupational_classification", curie=DISMECH.curie('occupational_classification'),
                   model_uri=DISMECH.occupational_classification, domain=None, range=Optional[str])

slots.ilo_agent_category = Slot(uri=DISMECH.ilo_agent_category, name="ilo_agent_category", curie=DISMECH.curie('ilo_agent_category'),
                   model_uri=DISMECH.ilo_agent_category, domain=None, range=Optional[Union[Union[dict, ILOCausativeAgentAssignment], list[Union[dict, ILOCausativeAgentAssignment]]]])

slots.ilo_disease_category = Slot(uri=DISMECH.ilo_disease_category, name="ilo_disease_category", curie=DISMECH.curie('ilo_disease_category'),
                   model_uri=DISMECH.ilo_disease_category, domain=None, range=Optional[Union[Union[dict, ILODiseaseCategoryAssignment], list[Union[dict, ILODiseaseCategoryAssignment]]]])

slots.eu_occupational_category = Slot(uri=DISMECH.eu_occupational_category, name="eu_occupational_category", curie=DISMECH.curie('eu_occupational_category'),
                   model_uri=DISMECH.eu_occupational_category, domain=None, range=Optional[Union[Union[dict, EUOccupationalScheduleAssignment], list[Union[dict, EUOccupationalScheduleAssignment]]]])

slots.exposure_classifications = Slot(uri=DISMECH.exposure_classifications, name="exposure_classifications", curie=DISMECH.curie('exposure_classifications'),
                   model_uri=DISMECH.exposure_classifications, domain=None, range=Optional[Union[dict, ExposureClassifications]])

slots.hazard_agent_type = Slot(uri=DISMECH.hazard_agent_type, name="hazard_agent_type", curie=DISMECH.curie('hazard_agent_type'),
                   model_uri=DISMECH.hazard_agent_type, domain=None, range=Optional[Union[Union[dict, HazardAgentTypeAssignment], list[Union[dict, HazardAgentTypeAssignment]]]])

slots.exposure_route = Slot(uri=DISMECH.exposure_route, name="exposure_route", curie=DISMECH.curie('exposure_route'),
                   model_uri=DISMECH.exposure_route, domain=None, range=Optional[Union[Union[dict, ExposureRouteAssignment], list[Union[dict, ExposureRouteAssignment]]]])

slots.exposure_duration = Slot(uri=DISMECH.exposure_duration, name="exposure_duration", curie=DISMECH.curie('exposure_duration'),
                   model_uri=DISMECH.exposure_duration, domain=None, range=Optional[Union[Union[dict, ExposureDurationAssignment], list[Union[dict, ExposureDurationAssignment]]]])

slots.iarc_carcinogen_group = Slot(uri=DISMECH.iarc_carcinogen_group, name="iarc_carcinogen_group", curie=DISMECH.curie('iarc_carcinogen_group'),
                   model_uri=DISMECH.iarc_carcinogen_group, domain=None, range=Optional[Union[dict, IARCCarcinogenGroupAssignment]])

slots.ghs_health_hazard_class = Slot(uri=DISMECH.ghs_health_hazard_class, name="ghs_health_hazard_class", curie=DISMECH.curie('ghs_health_hazard_class'),
                   model_uri=DISMECH.ghs_health_hazard_class, domain=None, range=Optional[Union[Union[dict, GHSHealthHazardClassAssignment], list[Union[dict, GHSHealthHazardClassAssignment]]]])

slots.exposome_domain = Slot(uri=DISMECH.exposome_domain, name="exposome_domain", curie=DISMECH.curie('exposome_domain'),
                   model_uri=DISMECH.exposome_domain, domain=None, range=Optional[Union[Union[dict, ExposomeDomainAssignment], list[Union[dict, ExposomeDomainAssignment]]]])

slots.classification_value = Slot(uri=DISMECH.classification_value, name="classification_value", curie=DISMECH.curie('classification_value'),
                   model_uri=DISMECH.classification_value, domain=None, range=Optional[str])

slots.icd10cm_mappings = Slot(uri=DISMECH.icd10cm_mappings, name="icd10cm_mappings", curie=DISMECH.curie('icd10cm_mappings'),
                   model_uri=DISMECH.icd10cm_mappings, domain=None, range=Optional[Union[Union[dict, ICD10CMMapping], list[Union[dict, ICD10CMMapping]]]])

slots.icd11f_mappings = Slot(uri=DISMECH.icd11f_mappings, name="icd11f_mappings", curie=DISMECH.curie('icd11f_mappings'),
                   model_uri=DISMECH.icd11f_mappings, domain=None, range=Optional[Union[Union[dict, ICD11FMapping], list[Union[dict, ICD11FMapping]]]])

slots.mondo_mappings = Slot(uri=DISMECH.mondo_mappings, name="mondo_mappings", curie=DISMECH.curie('mondo_mappings'),
                   model_uri=DISMECH.mondo_mappings, domain=None, range=Optional[Union[Union[dict, MondoMapping], list[Union[dict, MondoMapping]]]])

slots.ncit_mappings = Slot(uri=DISMECH.ncit_mappings, name="ncit_mappings", curie=DISMECH.curie('ncit_mappings'),
                   model_uri=DISMECH.ncit_mappings, domain=None, range=Optional[Union[Union[dict, NCITMapping], list[Union[dict, NCITMapping]]]])

slots.mapping_predicate = Slot(uri=DISMECH.mapping_predicate, name="mapping_predicate", curie=DISMECH.curie('mapping_predicate'),
                   model_uri=DISMECH.mapping_predicate, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.mapping_source = Slot(uri=DISMECH.mapping_source, name="mapping_source", curie=DISMECH.curie('mapping_source'),
                   model_uri=DISMECH.mapping_source, domain=None, range=Optional[str])

slots.mapping_justification = Slot(uri=DISMECH.mapping_justification, name="mapping_justification", curie=DISMECH.curie('mapping_justification'),
                   model_uri=DISMECH.mapping_justification, domain=None, range=Optional[str])

slots.definition_type = Slot(uri=DISMECH.definition_type, name="definition_type", curie=DISMECH.curie('definition_type'),
                   model_uri=DISMECH.definition_type, domain=None, range=Optional[Union[str, "DefinitionTypeEnum"]])

slots.derivation_basis = Slot(uri=DISMECH.derivation_basis, name="derivation_basis", curie=DISMECH.curie('derivation_basis'),
                   model_uri=DISMECH.derivation_basis, domain=None, range=Optional[Union[str, "DefinitionDerivationBasisEnum"]])

slots.validation_status = Slot(uri=DISMECH.validation_status, name="validation_status", curie=DISMECH.curie('validation_status'),
                   model_uri=DISMECH.validation_status, domain=None, range=Optional[Union[dict, AlgorithmValidationStatus]])

slots.criteria_sets = Slot(uri=DISMECH.criteria_sets, name="criteria_sets", curie=DISMECH.curie('criteria_sets'),
                   model_uri=DISMECH.criteria_sets, domain=None, range=Optional[Union[dict[Union[str, CriteriaSetName], Union[dict, CriteriaSet]], list[Union[dict, CriteriaSet]]]])

slots.scope = Slot(uri=DISMECH.scope, name="scope", curie=DISMECH.curie('scope'),
                   model_uri=DISMECH.scope, domain=None, range=Optional[str])

slots.inclusion_criteria = Slot(uri=DISMECH.inclusion_criteria, name="inclusion_criteria", curie=DISMECH.curie('inclusion_criteria'),
                   model_uri=DISMECH.inclusion_criteria, domain=None, range=Optional[Union[Union[dict, CriteriaItem], list[Union[dict, CriteriaItem]]]])

slots.exclusion_criteria = Slot(uri=DISMECH.exclusion_criteria, name="exclusion_criteria", curie=DISMECH.curie('exclusion_criteria'),
                   model_uri=DISMECH.exclusion_criteria, domain=None, range=Optional[Union[Union[dict, CriteriaItem], list[Union[dict, CriteriaItem]]]])

slots.core_clinical_characteristics = Slot(uri=DISMECH.core_clinical_characteristics, name="core_clinical_characteristics", curie=DISMECH.curie('core_clinical_characteristics'),
                   model_uri=DISMECH.core_clinical_characteristics, domain=None, range=Optional[Union[Union[dict, CriteriaItem], list[Union[dict, CriteriaItem]]]])

slots.imaging_requirements = Slot(uri=DISMECH.imaging_requirements, name="imaging_requirements", curie=DISMECH.curie('imaging_requirements'),
                   model_uri=DISMECH.imaging_requirements, domain=None, range=Optional[Union[Union[dict, CriteriaItem], list[Union[dict, CriteriaItem]]]])

slots.laboratory_requirements = Slot(uri=DISMECH.laboratory_requirements, name="laboratory_requirements", curie=DISMECH.curie('laboratory_requirements'),
                   model_uri=DISMECH.laboratory_requirements, domain=None, range=Optional[Union[Union[dict, CriteriaItem], list[Union[dict, CriteriaItem]]]])

slots.additional_requirements = Slot(uri=DISMECH.additional_requirements, name="additional_requirements", curie=DISMECH.curie('additional_requirements'),
                   model_uri=DISMECH.additional_requirements, domain=None, range=Optional[Union[Union[dict, CriteriaItem], list[Union[dict, CriteriaItem]]]])

slots.minimum_required = Slot(uri=DISMECH.minimum_required, name="minimum_required", curie=DISMECH.curie('minimum_required'),
                   model_uri=DISMECH.minimum_required, domain=None, range=Optional[int])

slots.consistency = Slot(uri=DISMECH.consistency, name="consistency", curie=DISMECH.curie('consistency'),
                   model_uri=DISMECH.consistency, domain=None, range=Optional[Union[Union[dict, MappingConsistency], list[Union[dict, MappingConsistency]]]])

slots.consistent = Slot(uri=DISMECH.consistent, name="consistent", curie=DISMECH.curie('consistent'),
                   model_uri=DISMECH.consistent, domain=None, range=Optional[Union[str, "MappingConsistencyEnum"]])

slots.differential_diagnoses = Slot(uri=DISMECH.differential_diagnoses, name="differential_diagnoses", curie=DISMECH.curie('differential_diagnoses'),
                   model_uri=DISMECH.differential_diagnoses, domain=None, range=Optional[Union[dict[Union[str, DifferentialDiagnosisName], Union[dict, DifferentialDiagnosis]], list[Union[dict, DifferentialDiagnosis]]]])

slots.disease_a = Slot(uri=DISMECH.disease_a, name="disease_a", curie=DISMECH.curie('disease_a'),
                   model_uri=DISMECH.disease_a, domain=None, range=Optional[Union[dict, ConditionDescriptor]])

slots.disease_b = Slot(uri=DISMECH.disease_b, name="disease_b", curie=DISMECH.curie('disease_b'),
                   model_uri=DISMECH.disease_b, domain=None, range=Optional[Union[dict, ConditionDescriptor]])

slots.upstream_disorder = Slot(uri=DISMECH.upstream_disorder, name="upstream_disorder", curie=DISMECH.curie('upstream_disorder'),
                   model_uri=DISMECH.upstream_disorder, domain=None, range=Optional[Union[dict, ConditionDescriptor]])

slots.source = Slot(uri=DISMECH.source, name="source", curie=DISMECH.curie('source'),
                   model_uri=DISMECH.source, domain=None, range=Optional[str])

slots.signal_disorder_a_id = Slot(uri=DISMECH.signal_disorder_a_id, name="signal_disorder_a_id", curie=DISMECH.curie('signal_disorder_a_id'),
                   model_uri=DISMECH.signal_disorder_a_id, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.signal_disorder_b_id = Slot(uri=DISMECH.signal_disorder_b_id, name="signal_disorder_b_id", curie=DISMECH.curie('signal_disorder_b_id'),
                   model_uri=DISMECH.signal_disorder_b_id, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.code_system = Slot(uri=DISMECH.code_system, name="code_system", curie=DISMECH.curie('code_system'),
                   model_uri=DISMECH.code_system, domain=None, range=Optional[str])

slots.code = Slot(uri=DISMECH.code, name="code", curie=DISMECH.curie('code'),
                   model_uri=DISMECH.code, domain=None, range=Optional[str])

slots.directionality = Slot(uri=DISMECH.directionality, name="directionality", curie=DISMECH.curie('directionality'),
                   model_uri=DISMECH.directionality, domain=None, range=Optional[Union[str, "ComorbidityDirectionEnum"]])

slots.effect_direction = Slot(uri=DISMECH.effect_direction, name="effect_direction", curie=DISMECH.curie('effect_direction'),
                   model_uri=DISMECH.effect_direction, domain=None, range=Optional[Union[str, "ComorbidityEffectDirectionEnum"]])

slots.composition = Slot(uri=DISMECH.composition, name="composition", curie=DISMECH.curie('composition'),
                   model_uri=DISMECH.composition, domain=None, range=Optional[Union[str, "ConditionCompositionEnum"]])

slots.components = Slot(uri=DISMECH.components, name="components", curie=DISMECH.curie('components'),
                   model_uri=DISMECH.components, domain=None, range=Optional[Union[Union[dict, ConditionDescriptor], list[Union[dict, ConditionDescriptor]]]])

slots.association_signals = Slot(uri=DISMECH.association_signals, name="association_signals", curie=DISMECH.curie('association_signals'),
                   model_uri=DISMECH.association_signals, domain=None, range=Optional[Union[Union[dict, AssociationSignal], list[Union[dict, AssociationSignal]]]])

slots.literature_evidence = Slot(uri=DISMECH.literature_evidence, name="literature_evidence", curie=DISMECH.curie('literature_evidence'),
                   model_uri=DISMECH.literature_evidence, domain=None, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.hypotheses = Slot(uri=DISMECH.hypotheses, name="hypotheses", curie=DISMECH.curie('hypotheses'),
                   model_uri=DISMECH.hypotheses, domain=None, range=Optional[Union[Union[dict, ComorbidityHypothesis], list[Union[dict, ComorbidityHypothesis]]]])

slots.mechanistic_hypotheses = Slot(uri=DISMECH.mechanistic_hypotheses, name="mechanistic_hypotheses", curie=DISMECH.curie('mechanistic_hypotheses'),
                   model_uri=DISMECH.mechanistic_hypotheses, domain=None, range=Optional[Union[Union[dict, MechanisticHypothesis], list[Union[dict, MechanisticHypothesis]]]])

slots.shared_upstream_hypotheses = Slot(uri=DISMECH.shared_upstream_hypotheses, name="shared_upstream_hypotheses", curie=DISMECH.curie('shared_upstream_hypotheses'),
                   model_uri=DISMECH.shared_upstream_hypotheses, domain=None, range=Optional[Union[Union[dict, UpstreamConditionHypothesis], list[Union[dict, UpstreamConditionHypothesis]]]])

slots.curation_status = Slot(uri=DISMECH.curation_status, name="curation_status", curie=DISMECH.curie('curation_status'),
                   model_uri=DISMECH.curation_status, domain=None, range=Optional[Union[str, "CurationStatusEnum"]])

slots.demographics = Slot(uri=DISMECH.demographics, name="demographics", curie=DISMECH.curie('demographics'),
                   model_uri=DISMECH.demographics, domain=None, range=Optional[Union[dict, Demographics]])

slots.mapping_notes = Slot(uri=DISMECH.mapping_notes, name="mapping_notes", curie=DISMECH.curie('mapping_notes'),
                   model_uri=DISMECH.mapping_notes, domain=None, range=Optional[str])

slots.disorder_a_count = Slot(uri=DISMECH.disorder_a_count, name="disorder_a_count", curie=DISMECH.curie('disorder_a_count'),
                   model_uri=DISMECH.disorder_a_count, domain=None, range=Optional[int])

slots.disorder_b_count = Slot(uri=DISMECH.disorder_b_count, name="disorder_b_count", curie=DISMECH.curie('disorder_b_count'),
                   model_uri=DISMECH.disorder_b_count, domain=None, range=Optional[int])

slots.pair_count = Slot(uri=DISMECH.pair_count, name="pair_count", curie=DISMECH.curie('pair_count'),
                   model_uri=DISMECH.pair_count, domain=None, range=Optional[int])

slots.limited_precision = Slot(uri=DISMECH.limited_precision, name="limited_precision", curie=DISMECH.curie('limited_precision'),
                   model_uri=DISMECH.limited_precision, domain=None, range=Optional[Union[bool, Bool]])

slots.precision_count_threshold = Slot(uri=DISMECH.precision_count_threshold, name="precision_count_threshold", curie=DISMECH.curie('precision_count_threshold'),
                   model_uri=DISMECH.precision_count_threshold, domain=None, range=Optional[int])

slots.sex = Slot(uri=DISMECH.sex, name="sex", curie=DISMECH.curie('sex'),
                   model_uri=DISMECH.sex, domain=None, range=Optional[str])

slots.a_before_b = Slot(uri=DISMECH.a_before_b, name="a_before_b", curie=DISMECH.curie('a_before_b'),
                   model_uri=DISMECH.a_before_b, domain=None, range=Optional[float])

slots.b_before_a = Slot(uri=DISMECH.b_before_a, name="b_before_a", curie=DISMECH.curie('b_before_a'),
                   model_uri=DISMECH.b_before_a, domain=None, range=Optional[float])

slots.same_time = Slot(uri=DISMECH.same_time, name="same_time", curie=DISMECH.curie('same_time'),
                   model_uri=DISMECH.same_time, domain=None, range=Optional[float])

slots.metrics = Slot(uri=DISMECH.metrics, name="metrics", curie=DISMECH.curie('metrics'),
                   model_uri=DISMECH.metrics, domain=None, range=Optional[Union[Union[dict, AssociationMetric], list[Union[dict, AssociationMetric]]]])

slots.statistics = Slot(uri=DISMECH.statistics, name="statistics", curie=DISMECH.curie('statistics'),
                   model_uri=DISMECH.statistics, domain=None, range=Optional[Union[dict, AssociationStatistics]])

slots.metric_type = Slot(uri=DISMECH.metric_type, name="metric_type", curie=DISMECH.curie('metric_type'),
                   model_uri=DISMECH.metric_type, domain=None, range=Optional[Union[str, "AssociationMetricTypeEnum"]])

slots.metric_value = Slot(uri=DISMECH.metric_value, name="metric_value", curie=DISMECH.curie('metric_value'),
                   model_uri=DISMECH.metric_value, domain=None, range=Optional[float])

slots.metric_ci_lower = Slot(uri=DISMECH.metric_ci_lower, name="metric_ci_lower", curie=DISMECH.curie('metric_ci_lower'),
                   model_uri=DISMECH.metric_ci_lower, domain=None, range=Optional[float])

slots.metric_ci_upper = Slot(uri=DISMECH.metric_ci_upper, name="metric_ci_upper", curie=DISMECH.curie('metric_ci_upper'),
                   model_uri=DISMECH.metric_ci_upper, domain=None, range=Optional[float])

slots.p_value = Slot(uri=DISMECH.p_value, name="p_value", curie=DISMECH.curie('p_value'),
                   model_uri=DISMECH.p_value, domain=None, range=Optional[float])

slots.fdr = Slot(uri=DISMECH.fdr, name="fdr", curie=DISMECH.curie('fdr'),
                   model_uri=DISMECH.fdr, domain=None, range=Optional[float])

slots.go_terms = Slot(uri=DISMECH.go_terms, name="go_terms", curie=DISMECH.curie('go_terms'),
                   model_uri=DISMECH.go_terms, domain=None, range=Optional[Union[Union[dict, GOEnrichmentTerm], list[Union[dict, GOEnrichmentTerm]]]])

slots.go_enrichment = Slot(uri=DISMECH.go_enrichment, name="go_enrichment", curie=DISMECH.curie('go_enrichment'),
                   model_uri=DISMECH.go_enrichment, domain=None, range=Optional[Union[dict, GOEnrichment]])

slots.combined_score = Slot(uri=DISMECH.combined_score, name="combined_score", curie=DISMECH.curie('combined_score'),
                   model_uri=DISMECH.combined_score, domain=None, range=Optional[float])

slots.overlap = Slot(uri=DISMECH.overlap, name="overlap", curie=DISMECH.curie('overlap'),
                   model_uri=DISMECH.overlap, domain=None, range=Optional[float])

slots.method = Slot(uri=DISMECH.method, name="method", curie=DISMECH.curie('method'),
                   model_uri=DISMECH.method, domain=None, range=Optional[str])

slots.phenotype_contexts = Slot(uri=DISMECH.phenotype_contexts, name="phenotype_contexts", curie=DISMECH.curie('phenotype_contexts'),
                   model_uri=DISMECH.phenotype_contexts, domain=None, range=Optional[Union[Union[dict, PhenotypeContext], list[Union[dict, PhenotypeContext]]]])

slots.genetic_context = Slot(uri=DISMECH.genetic_context, name="genetic_context", curie=DISMECH.curie('genetic_context'),
                   model_uri=DISMECH.genetic_context, domain=None, range=Optional[Union[dict, GeneticContext]])

slots.allele_type = Slot(uri=DISMECH.allele_type, name="allele_type", curie=DISMECH.curie('allele_type'),
                   model_uri=DISMECH.allele_type, domain=None, range=Optional[str])

slots.allelic_hit_role = Slot(uri=DISMECH.allelic_hit_role, name="allelic_hit_role", curie=DISMECH.curie('allelic_hit_role'),
                   model_uri=DISMECH.allelic_hit_role, domain=None, range=Optional[Union[str, "AllelicHitRoleEnum"]])

slots.allelic_events = Slot(uri=DISMECH.allelic_events, name="allelic_events", curie=DISMECH.curie('allelic_events'),
                   model_uri=DISMECH.allelic_events, domain=None, range=Optional[Union[Union[str, "AllelicEventEnum"], list[Union[str, "AllelicEventEnum"]]]])

slots.zygosity = Slot(uri=DISMECH.zygosity, name="zygosity", curie=DISMECH.curie('zygosity'),
                   model_uri=DISMECH.zygosity, domain=None, range=Optional[Union[str, "ZygosityEnum"]])

slots.functional_impact = Slot(uri=DISMECH.functional_impact, name="functional_impact", curie=DISMECH.curie('functional_impact'),
                   model_uri=DISMECH.functional_impact, domain=None, range=Optional[str])

slots.functional_impact_category = Slot(uri=DISMECH.functional_impact_category, name="functional_impact_category", curie=DISMECH.curie('functional_impact_category'),
                   model_uri=DISMECH.functional_impact_category, domain=None, range=Optional[Union[str, "FunctionalImpactEnum"]])

slots.complementation_group = Slot(uri=DISMECH.complementation_group, name="complementation_group", curie=DISMECH.curie('complementation_group'),
                   model_uri=DISMECH.complementation_group, domain=None, range=Optional[str])

slots.onset = Slot(uri=DISMECH.onset, name="onset", curie=DISMECH.curie('onset'),
                   model_uri=DISMECH.onset, domain=None, range=Optional[Union[dict, OnsetDescriptor]])

slots.onset_category = Slot(uri=DISMECH.onset_category, name="onset_category", curie=DISMECH.curie('onset_category'),
                   model_uri=DISMECH.onset_category, domain=None, range=Optional[Union[str, "OnsetEnum"]])

slots.mean_age_years = Slot(uri=DISMECH.mean_age_years, name="mean_age_years", curie=DISMECH.curie('mean_age_years'),
                   model_uri=DISMECH.mean_age_years, domain=None, range=Optional[float])

slots.min_age_years = Slot(uri=DISMECH.min_age_years, name="min_age_years", curie=DISMECH.curie('min_age_years'),
                   model_uri=DISMECH.min_age_years, domain=None, range=Optional[float])

slots.max_age_years = Slot(uri=DISMECH.max_age_years, name="max_age_years", curie=DISMECH.curie('max_age_years'),
                   model_uri=DISMECH.max_age_years, domain=None, range=Optional[float])

slots.tracked_issues = Slot(uri=DISMECH.tracked_issues, name="tracked_issues", curie=DISMECH.curie('tracked_issues'),
                   model_uri=DISMECH.tracked_issues, domain=None, range=Optional[Union[Union[dict, TrackedIssue], list[Union[dict, TrackedIssue]]]])

slots.tracked_issue_role = Slot(uri=DISMECH.tracked_issue_role, name="tracked_issue_role", curie=DISMECH.curie('tracked_issue_role'),
                   model_uri=DISMECH.tracked_issue_role, domain=None, range=Optional[str])

slots.tracked_issue_status = Slot(uri=DISMECH.tracked_issue_status, name="tracked_issue_status", curie=DISMECH.curie('tracked_issue_status'),
                   model_uri=DISMECH.tracked_issue_status, domain=None, range=Optional[str])

slots.grouping_basis = Slot(uri=DISMECH.grouping_basis, name="grouping_basis", curie=DISMECH.curie('grouping_basis'),
                   model_uri=DISMECH.grouping_basis, domain=None, range=Optional[Union[Union[str, "GroupingBasisEnum"], list[Union[str, "GroupingBasisEnum"]]]])

slots.grouping_rationale = Slot(uri=DISMECH.grouping_rationale, name="grouping_rationale", curie=DISMECH.curie('grouping_rationale'),
                   model_uri=DISMECH.grouping_rationale, domain=None, range=Optional[str])

slots.membership_criteria = Slot(uri=DISMECH.membership_criteria, name="membership_criteria", curie=DISMECH.curie('membership_criteria'),
                   model_uri=DISMECH.membership_criteria, domain=None, range=Optional[Union[Union[dict, GroupingCriteria], list[Union[dict, GroupingCriteria]]]])

slots.criteria_semantics = Slot(uri=DISMECH.criteria_semantics, name="criteria_semantics", curie=DISMECH.curie('criteria_semantics'),
                   model_uri=DISMECH.criteria_semantics, domain=None, range=Optional[Union[str, "CriteriaSemanticsEnum"]])

slots.logic = Slot(uri=DISMECH.logic, name="logic", curie=DISMECH.curie('logic'),
                   model_uri=DISMECH.logic, domain=None, range=Optional[Union[dict, LogicalCriterion]])

slots.operator = Slot(uri=DISMECH.operator, name="operator", curie=DISMECH.curie('operator'),
                   model_uri=DISMECH.operator, domain=None, range=Optional[Union[str, "LogicalOperatorEnum"]])

slots.operands = Slot(uri=DISMECH.operands, name="operands", curie=DISMECH.curie('operands'),
                   model_uri=DISMECH.operands, domain=None, range=Optional[Union[Union[dict, LogicalCriterion], list[Union[dict, LogicalCriterion]]]])

slots.criterion_predicate = Slot(uri=DISMECH.criterion_predicate, name="criterion_predicate", curie=DISMECH.curie('criterion_predicate'),
                   model_uri=DISMECH.criterion_predicate, domain=None, range=Optional[Union[str, "CriterionPredicateEnum"]])

slots.min_frequency = Slot(uri=DISMECH.min_frequency, name="min_frequency", curie=DISMECH.curie('min_frequency'),
                   model_uri=DISMECH.min_frequency, domain=None, range=Optional[Union[str, "FrequencyEnum"]])

slots.module = Slot(uri=DISMECH.module, name="module", curie=DISMECH.curie('module'),
                   model_uri=DISMECH.module, domain=None, range=Optional[str])

slots.negated = Slot(uri=DISMECH.negated, name="negated", curie=DISMECH.curie('negated'),
                   model_uri=DISMECH.negated, domain=None, range=Optional[Union[bool, Bool]])

slots.members = Slot(uri=DISMECH.members, name="members", curie=DISMECH.curie('members'),
                   model_uri=DISMECH.members, domain=None, range=Optional[Union[Union[dict, GroupingMember], list[Union[dict, GroupingMember]]]])

slots.member = Slot(uri=DISMECH.member, name="member", curie=DISMECH.curie('member'),
                   model_uri=DISMECH.member, domain=None, range=str)

slots.member_type = Slot(uri=DISMECH.member_type, name="member_type", curie=DISMECH.curie('member_type'),
                   model_uri=DISMECH.member_type, domain=None, range=Optional[Union[str, "GroupingMemberTypeEnum"]])

slots.differentiating_mechanisms = Slot(uri=DISMECH.differentiating_mechanisms, name="differentiating_mechanisms", curie=DISMECH.curie('differentiating_mechanisms'),
                   model_uri=DISMECH.differentiating_mechanisms, domain=None, range=Optional[Union[Union[dict, DifferentiatingMechanism], list[Union[dict, DifferentiatingMechanism]]]])

slots.collection_type = Slot(uri=DISMECH.collection_type, name="collection_type", curie=DISMECH.curie('collection_type'),
                   model_uri=DISMECH.collection_type, domain=None, range=Optional[Union[str, "ModuleCollectionTypeEnum"]])

slots.module_members = Slot(uri=DISMECH.module_members, name="module_members", curie=DISMECH.curie('module_members'),
                   model_uri=DISMECH.module_members, domain=None, range=Optional[Union[Union[dict, ModuleCollectionMember], list[Union[dict, ModuleCollectionMember]]]])

slots.framework_terms = Slot(uri=DISMECH.framework_terms, name="framework_terms", curie=DISMECH.curie('framework_terms'),
                   model_uri=DISMECH.framework_terms, domain=None, range=Optional[Union[str, list[str]]])

slots.child_collections = Slot(uri=DISMECH.child_collections, name="child_collections", curie=DISMECH.curie('child_collections'),
                   model_uri=DISMECH.child_collections, domain=None, range=Optional[Union[str, list[str]]])

slots.geneSetAssociation__gene_set = Slot(uri=DISMECH.gene_set, name="geneSetAssociation__gene_set", curie=DISMECH.curie('gene_set'),
                   model_uri=DISMECH.geneSetAssociation__gene_set, domain=None, range=Union[str, URIorCURIE])

slots.geneSetAssociation__relationship = Slot(uri=DISMECH.relationship, name="geneSetAssociation__relationship", curie=DISMECH.curie('relationship'),
                   model_uri=DISMECH.geneSetAssociation__relationship, domain=None, range=Optional[Union[str, "GeneSetRelationshipEnum"]])

slots.geneSetAssociation__note = Slot(uri=DISMECH.note, name="geneSetAssociation__note", curie=DISMECH.curie('note'),
                   model_uri=DISMECH.geneSetAssociation__note, domain=None, range=Optional[str])

slots.proteinStructure__pdb_id = Slot(uri=DISMECH.pdb_id, name="proteinStructure__pdb_id", curie=DISMECH.curie('pdb_id'),
                   model_uri=DISMECH.proteinStructure__pdb_id, domain=None, range=str)

slots.proteinStructure__description = Slot(uri=DISMECH.description, name="proteinStructure__description", curie=DISMECH.curie('description'),
                   model_uri=DISMECH.proteinStructure__description, domain=None, range=Optional[str])

slots.proteinStructure__resolution_angstrom = Slot(uri=DISMECH.resolution_angstrom, name="proteinStructure__resolution_angstrom", curie=DISMECH.curie('resolution_angstrom'),
                   model_uri=DISMECH.proteinStructure__resolution_angstrom, domain=None, range=Optional[float])

slots.proteinStructure__method = Slot(uri=DISMECH.method, name="proteinStructure__method", curie=DISMECH.curie('method'),
                   model_uri=DISMECH.proteinStructure__method, domain=None, range=Optional[str])

slots.proteinStructure__ligand = Slot(uri=DISMECH.ligand, name="proteinStructure__ligand", curie=DISMECH.curie('ligand'),
                   model_uri=DISMECH.proteinStructure__ligand, domain=None, range=Optional[str])

slots.proteinStructure__target_protein = Slot(uri=DISMECH.target_protein, name="proteinStructure__target_protein", curie=DISMECH.curie('target_protein'),
                   model_uri=DISMECH.proteinStructure__target_protein, domain=None, range=Optional[str])

slots.proteinStructure__publication = Slot(uri=DISMECH.publication, name="proteinStructure__publication", curie=DISMECH.curie('publication'),
                   model_uri=DISMECH.proteinStructure__publication, domain=None, range=Optional[str])

slots.animalModel__name = Slot(uri=DISMECH.name, name="animalModel__name", curie=DISMECH.curie('name'),
                   model_uri=DISMECH.animalModel__name, domain=None, range=Optional[str])

slots.CurationEvent_curation_timestamp = Slot(uri=DISMECH.curation_timestamp, name="CurationEvent_curation_timestamp", curie=DISMECH.curie('curation_timestamp'),
                   model_uri=DISMECH.CurationEvent_curation_timestamp, domain=CurationEvent, range=Union[str, XSDDateTime])

slots.Descriptor_description = Slot(uri=DISMECH.description, name="Descriptor_description", curie=DISMECH.curie('description'),
                   model_uri=DISMECH.Descriptor_description, domain=Descriptor, range=Optional[str])

slots.CellTypeDescriptor_term = Slot(uri=DISMECH.term, name="CellTypeDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.CellTypeDescriptor_term, domain=CellTypeDescriptor, range=Optional[Union[dict, Term]])

slots.BiologicalProcessDescriptor_term = Slot(uri=DISMECH.term, name="BiologicalProcessDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.BiologicalProcessDescriptor_term, domain=BiologicalProcessDescriptor, range=Optional[Union[dict, Term]])

slots.MolecularFunctionDescriptor_term = Slot(uri=DISMECH.term, name="MolecularFunctionDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.MolecularFunctionDescriptor_term, domain=MolecularFunctionDescriptor, range=Optional[Union[dict, Term]])

slots.AnatomicalEntityDescriptor_term = Slot(uri=DISMECH.term, name="AnatomicalEntityDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.AnatomicalEntityDescriptor_term, domain=AnatomicalEntityDescriptor, range=Optional[Union[dict, Term]])

slots.ChemicalEntityDescriptor_term = Slot(uri=DISMECH.term, name="ChemicalEntityDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.ChemicalEntityDescriptor_term, domain=ChemicalEntityDescriptor, range=Optional[Union[dict, Term]])

slots.GeneDescriptor_term = Slot(uri=DISMECH.term, name="GeneDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.GeneDescriptor_term, domain=GeneDescriptor, range=Optional[Union[dict, Term]])

slots.CellularComponentDescriptor_term = Slot(uri=DISMECH.term, name="CellularComponentDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.CellularComponentDescriptor_term, domain=CellularComponentDescriptor, range=Optional[Union[dict, Term]])

slots.ProteinComplexDescriptor_term = Slot(uri=DISMECH.term, name="ProteinComplexDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.ProteinComplexDescriptor_term, domain=ProteinComplexDescriptor, range=Optional[Union[dict, Term]])

slots.AssayDescriptor_term = Slot(uri=DISMECH.term, name="AssayDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.AssayDescriptor_term, domain=AssayDescriptor, range=Optional[Union[dict, Term]])

slots.TriggerDescriptor_term = Slot(uri=DISMECH.term, name="TriggerDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.TriggerDescriptor_term, domain=TriggerDescriptor, range=Optional[Union[dict, Term]])

slots.DiseaseDescriptor_term = Slot(uri=DISMECH.term, name="DiseaseDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.DiseaseDescriptor_term, domain=DiseaseDescriptor, range=Optional[Union[dict, Term]])

slots.SubtypeDescriptor_term = Slot(uri=DISMECH.term, name="SubtypeDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.SubtypeDescriptor_term, domain=SubtypeDescriptor, range=Optional[Union[dict, Term]])

slots.BiomarkerDescriptor_term = Slot(uri=DISMECH.term, name="BiomarkerDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.BiomarkerDescriptor_term, domain=BiomarkerDescriptor, range=Optional[Union[dict, Term]])

slots.GeneProductDescriptor_term = Slot(uri=DISMECH.term, name="GeneProductDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.GeneProductDescriptor_term, domain=GeneProductDescriptor, range=Optional[Union[dict, Term]])

slots.HistopathologyFindingDescriptor_term = Slot(uri=DISMECH.term, name="HistopathologyFindingDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.HistopathologyFindingDescriptor_term, domain=HistopathologyFindingDescriptor, range=Optional[Union[dict, Term]])

slots.ImagingFindingDescriptor_term = Slot(uri=DISMECH.term, name="ImagingFindingDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.ImagingFindingDescriptor_term, domain=ImagingFindingDescriptor, range=Optional[Union[dict, Term]])

slots.LifeCycleStageDescriptor_term = Slot(uri=DISMECH.term, name="LifeCycleStageDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.LifeCycleStageDescriptor_term, domain=LifeCycleStageDescriptor, range=Optional[Union[dict, Term]])

slots.PhenotypeDescriptor_term = Slot(uri=DISMECH.term, name="PhenotypeDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.PhenotypeDescriptor_term, domain=PhenotypeDescriptor, range=Optional[Union[dict, Term]])

slots.InheritanceDescriptor_term = Slot(uri=DISMECH.term, name="InheritanceDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.InheritanceDescriptor_term, domain=InheritanceDescriptor, range=Optional[Union[dict, Term]])

slots.TreatmentDescriptor_term = Slot(uri=DISMECH.term, name="TreatmentDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.TreatmentDescriptor_term, domain=TreatmentDescriptor, range=Optional[Union[dict, Term]])

slots.TreatmentDescriptor_therapeutic_agent = Slot(uri=DISMECH.therapeutic_agent, name="TreatmentDescriptor_therapeutic_agent", curie=DISMECH.curie('therapeutic_agent'),
                   model_uri=DISMECH.TreatmentDescriptor_therapeutic_agent, domain=TreatmentDescriptor, range=Optional[Union[Union[dict, ChemicalEntityDescriptor], list[Union[dict, ChemicalEntityDescriptor]]]])

slots.TreatmentDescriptor_dietary_modifications = Slot(uri=DISMECH.dietary_modifications, name="TreatmentDescriptor_dietary_modifications", curie=DISMECH.curie('dietary_modifications'),
                   model_uri=DISMECH.TreatmentDescriptor_dietary_modifications, domain=TreatmentDescriptor, range=Optional[Union[Union[dict, DietaryModification], list[Union[dict, DietaryModification]]]])

slots.RegimenDescriptor_term = Slot(uri=DISMECH.term, name="RegimenDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.RegimenDescriptor_term, domain=RegimenDescriptor, range=Optional[Union[dict, Term]])

slots.ExposureDescriptor_term = Slot(uri=DISMECH.term, name="ExposureDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.ExposureDescriptor_term, domain=ExposureDescriptor, range=Optional[Union[dict, Term]])

slots.EnvironmentDescriptor_term = Slot(uri=DISMECH.term, name="EnvironmentDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.EnvironmentDescriptor_term, domain=EnvironmentDescriptor, range=Optional[Union[dict, Term]])

slots.FoodDescriptor_term = Slot(uri=DISMECH.term, name="FoodDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.FoodDescriptor_term, domain=FoodDescriptor, range=Optional[Union[dict, Term]])

slots.OrganismDescriptor_term = Slot(uri=DISMECH.term, name="OrganismDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.OrganismDescriptor_term, domain=OrganismDescriptor, range=Optional[Union[dict, Term]])

slots.PhenotypeContext_sex = Slot(uri=DISMECH.sex, name="PhenotypeContext_sex", curie=DISMECH.curie('sex'),
                   model_uri=DISMECH.PhenotypeContext_sex, domain=PhenotypeContext, range=Optional[Union[str, "SexEnum"]])

slots.PhenotypeContext_evidence = Slot(uri=DISMECH.evidence, name="PhenotypeContext_evidence", curie=DISMECH.curie('evidence'),
                   model_uri=DISMECH.PhenotypeContext_evidence, domain=PhenotypeContext, range=Optional[Union[Union[dict, "EvidenceItem"], list[Union[dict, "EvidenceItem"]]]])

slots.Dataset_description = Slot(uri=DISMECH.description, name="Dataset_description", curie=DISMECH.curie('description'),
                   model_uri=DISMECH.Dataset_description, domain=Dataset, range=Optional[str])

slots.Experiment_experiment_id = Slot(uri=DISMECH.experiment_id, name="Experiment_experiment_id", curie=DISMECH.curie('experiment_id'),
                   model_uri=DISMECH.Experiment_experiment_id, domain=Experiment, range=str)

slots.Experiment_perturbations = Slot(uri=DISMECH.perturbations, name="Experiment_perturbations", curie=DISMECH.curie('perturbations'),
                   model_uri=DISMECH.Experiment_perturbations, domain=Experiment, range=Optional[Union[dict[Union[str, ExperimentalPerturbationName], Union[dict, "ExperimentalPerturbation"]], list[Union[dict, "ExperimentalPerturbation"]]]])

slots.Experiment_readouts = Slot(uri=DISMECH.readouts, name="Experiment_readouts", curie=DISMECH.curie('readouts'),
                   model_uri=DISMECH.Experiment_readouts, domain=Experiment, range=Optional[Union[dict[Union[str, ExperimentalReadoutName], Union[dict, "ExperimentalReadout"]], list[Union[dict, "ExperimentalReadout"]]]])

slots.Experiment_assays = Slot(uri=DISMECH.assays, name="Experiment_assays", curie=DISMECH.curie('assays'),
                   model_uri=DISMECH.Experiment_assays, domain=Experiment, range=Optional[Union[Union[dict, AssayDescriptor], list[Union[dict, AssayDescriptor]]]])

slots.Experiment_evidence = Slot(uri=DISMECH.evidence, name="Experiment_evidence", curie=DISMECH.curie('evidence'),
                   model_uri=DISMECH.Experiment_evidence, domain=Experiment, range=Optional[Union[Union[dict, "EvidenceItem"], list[Union[dict, "EvidenceItem"]]]])

slots.ExperimentalPerturbation_target = Slot(uri=DISMECH.target, name="ExperimentalPerturbation_target", curie=DISMECH.curie('target'),
                   model_uri=DISMECH.ExperimentalPerturbation_target, domain=ExperimentalPerturbation, range=str)

slots.ExperimentalReadout_target = Slot(uri=DISMECH.target, name="ExperimentalReadout_target", curie=DISMECH.curie('target'),
                   model_uri=DISMECH.ExperimentalReadout_target, domain=ExperimentalReadout, range=str)

slots.ExperimentalReadout_direction = Slot(uri=DISMECH.direction, name="ExperimentalReadout_direction", curie=DISMECH.curie('direction'),
                   model_uri=DISMECH.ExperimentalReadout_direction, domain=ExperimentalReadout, range=Optional[Union[dict, Any]])

slots.ExperimentalReadout_interpretation = Slot(uri=DISMECH.interpretation, name="ExperimentalReadout_interpretation", curie=DISMECH.curie('interpretation'),
                   model_uri=DISMECH.ExperimentalReadout_interpretation, domain=ExperimentalReadout, range=Optional[str])

slots.ExperimentalControl_perturbations = Slot(uri=DISMECH.perturbations, name="ExperimentalControl_perturbations", curie=DISMECH.curie('perturbations'),
                   model_uri=DISMECH.ExperimentalControl_perturbations, domain=ExperimentalControl, range=Optional[Union[dict[Union[str, ExperimentalPerturbationName], Union[dict, ExperimentalPerturbation]], list[Union[dict, ExperimentalPerturbation]]]])

slots.ClinicalTrial_name = Slot(uri=DISMECH.name, name="ClinicalTrial_name", curie=DISMECH.curie('name'),
                   model_uri=DISMECH.ClinicalTrial_name, domain=ClinicalTrial, range=Union[str, ClinicalTrialName])

slots.ClinicalTrial_description = Slot(uri=DISMECH.description, name="ClinicalTrial_description", curie=DISMECH.curie('description'),
                   model_uri=DISMECH.ClinicalTrial_description, domain=ClinicalTrial, range=Optional[str])

slots.ClinicalTrial_phase = Slot(uri=DISMECH.phase, name="ClinicalTrial_phase", curie=DISMECH.curie('phase'),
                   model_uri=DISMECH.ClinicalTrial_phase, domain=ClinicalTrial, range=Optional[Union[str, "ClinicalTrialPhaseEnum"]])

slots.ClinicalTrial_status = Slot(uri=DISMECH.status, name="ClinicalTrial_status", curie=DISMECH.curie('status'),
                   model_uri=DISMECH.ClinicalTrial_status, domain=ClinicalTrial, range=Optional[Union[str, "ClinicalTrialStatusEnum"]])

slots.ClinicalTrial_evidence = Slot(uri=DISMECH.evidence, name="ClinicalTrial_evidence", curie=DISMECH.curie('evidence'),
                   model_uri=DISMECH.ClinicalTrial_evidence, domain=ClinicalTrial, range=Optional[Union[Union[dict, "EvidenceItem"], list[Union[dict, "EvidenceItem"]]]])

slots.SeverityTier_threshold = Slot(uri=DISMECH.threshold, name="SeverityTier_threshold", curie=DISMECH.curie('threshold'),
                   model_uri=DISMECH.SeverityTier_threshold, domain=SeverityTier, range=float)

slots.SeverityTier_name = Slot(uri=DISMECH.name, name="SeverityTier_name", curie=DISMECH.curie('name'),
                   model_uri=DISMECH.SeverityTier_name, domain=SeverityTier, range=Union[str, SeverityTierName])

slots.ModelVariableDescriptor_term = Slot(uri=DISMECH.term, name="ModelVariableDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.ModelVariableDescriptor_term, domain=ModelVariableDescriptor, range=Optional[Union[dict, Term]])

slots.ModelVariableDescriptor_threshold = Slot(uri=DISMECH.threshold, name="ModelVariableDescriptor_threshold", curie=DISMECH.curie('threshold'),
                   model_uri=DISMECH.ModelVariableDescriptor_threshold, domain=ModelVariableDescriptor, range=Optional[float])

slots.ModelVariableDescriptor_threshold_direction = Slot(uri=DISMECH.threshold_direction, name="ModelVariableDescriptor_threshold_direction", curie=DISMECH.curie('threshold_direction'),
                   model_uri=DISMECH.ModelVariableDescriptor_threshold_direction, domain=ModelVariableDescriptor, range=Optional[Union[str, "ThresholdDirectionEnum"]])

slots.ModelVariableDescriptor_severity_scale = Slot(uri=DISMECH.severity_scale, name="ModelVariableDescriptor_severity_scale", curie=DISMECH.curie('severity_scale'),
                   model_uri=DISMECH.ModelVariableDescriptor_severity_scale, domain=ModelVariableDescriptor, range=Optional[Union[dict[Union[str, SeverityTierName], Union[dict, SeverityTier]], list[Union[dict, SeverityTier]]]])

slots.DifferentialDiagnosis_description = Slot(uri=DISMECH.description, name="DifferentialDiagnosis_description", curie=DISMECH.curie('description'),
                   model_uri=DISMECH.DifferentialDiagnosis_description, domain=DifferentialDiagnosis, range=Optional[str])

slots.DifferentialDiagnosis_distinguishing_features = Slot(uri=DISMECH.distinguishing_features, name="DifferentialDiagnosis_distinguishing_features", curie=DISMECH.curie('distinguishing_features'),
                   model_uri=DISMECH.DifferentialDiagnosis_distinguishing_features, domain=DifferentialDiagnosis, range=Optional[Union[str, list[str]]])

slots.DifferentialDiagnosis_notes = Slot(uri=DISMECH.notes, name="DifferentialDiagnosis_notes", curie=DISMECH.curie('notes'),
                   model_uri=DISMECH.DifferentialDiagnosis_notes, domain=DifferentialDiagnosis, range=Optional[str])

slots.CausalEdge_evidence = Slot(uri=DISMECH.evidence, name="CausalEdge_evidence", curie=DISMECH.curie('evidence'),
                   model_uri=DISMECH.CausalEdge_evidence, domain=CausalEdge, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.CausalEdge_hypothesis_groups = Slot(uri=DISMECH.hypothesis_groups, name="CausalEdge_hypothesis_groups", curie=DISMECH.curie('hypothesis_groups'),
                   model_uri=DISMECH.CausalEdge_hypothesis_groups, domain=CausalEdge, range=Optional[Union[str, list[str]]])

slots.CausalEdge_causal_link_type = Slot(uri=DISMECH.causal_link_type, name="CausalEdge_causal_link_type", curie=DISMECH.curie('causal_link_type'),
                   model_uri=DISMECH.CausalEdge_causal_link_type, domain=CausalEdge, range=Optional[Union[str, "CausalLinkTypeEnum"]])

slots.CausalEdge_intermediate_mechanisms = Slot(uri=DISMECH.intermediate_mechanisms, name="CausalEdge_intermediate_mechanisms", curie=DISMECH.curie('intermediate_mechanisms'),
                   model_uri=DISMECH.CausalEdge_intermediate_mechanisms, domain=CausalEdge, range=Optional[Union[str, list[str]]])

slots.TreatmentMechanismTarget_target = Slot(uri=DISMECH.target, name="TreatmentMechanismTarget_target", curie=DISMECH.curie('target'),
                   model_uri=DISMECH.TreatmentMechanismTarget_target, domain=TreatmentMechanismTarget, range=str)

slots.TreatmentMechanismTarget_evidence = Slot(uri=DISMECH.evidence, name="TreatmentMechanismTarget_evidence", curie=DISMECH.curie('evidence'),
                   model_uri=DISMECH.TreatmentMechanismTarget_evidence, domain=TreatmentMechanismTarget, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.EnvironmentalMechanismTarget_target = Slot(uri=DISMECH.target, name="EnvironmentalMechanismTarget_target", curie=DISMECH.curie('target'),
                   model_uri=DISMECH.EnvironmentalMechanismTarget_target, domain=EnvironmentalMechanismTarget, range=str)

slots.EnvironmentalMechanismTarget_environmental_effect = Slot(uri=DISMECH.environmental_effect, name="EnvironmentalMechanismTarget_environmental_effect", curie=DISMECH.curie('environmental_effect'),
                   model_uri=DISMECH.EnvironmentalMechanismTarget_environmental_effect, domain=EnvironmentalMechanismTarget, range=Optional[Union[str, "EnvironmentalEffectEnum"]])

slots.EnvironmentalMechanismTarget_causal_link_type = Slot(uri=DISMECH.causal_link_type, name="EnvironmentalMechanismTarget_causal_link_type", curie=DISMECH.curie('causal_link_type'),
                   model_uri=DISMECH.EnvironmentalMechanismTarget_causal_link_type, domain=EnvironmentalMechanismTarget, range=Optional[Union[str, "CausalLinkTypeEnum"]])

slots.EnvironmentalMechanismTarget_evidence = Slot(uri=DISMECH.evidence, name="EnvironmentalMechanismTarget_evidence", curie=DISMECH.curie('evidence'),
                   model_uri=DISMECH.EnvironmentalMechanismTarget_evidence, domain=EnvironmentalMechanismTarget, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.ModelMechanismLink_target = Slot(uri=DISMECH.target, name="ModelMechanismLink_target", curie=DISMECH.curie('target'),
                   model_uri=DISMECH.ModelMechanismLink_target, domain=ModelMechanismLink, range=str)

slots.ModelMechanismLink_relationship = Slot(uri=DISMECH.relationship, name="ModelMechanismLink_relationship", curie=DISMECH.curie('relationship'),
                   model_uri=DISMECH.ModelMechanismLink_relationship, domain=ModelMechanismLink, range=Optional[Union[str, "ModelMechanismRelationshipEnum"]])

slots.ModelMechanismLink_description = Slot(uri=DISMECH.description, name="ModelMechanismLink_description", curie=DISMECH.curie('description'),
                   model_uri=DISMECH.ModelMechanismLink_description, domain=ModelMechanismLink, range=Optional[str])

slots.ModelMechanismLink_readouts = Slot(uri=DISMECH.readouts, name="ModelMechanismLink_readouts", curie=DISMECH.curie('readouts'),
                   model_uri=DISMECH.ModelMechanismLink_readouts, domain=ModelMechanismLink, range=Optional[Union[dict[Union[str, ExperimentalReadoutName], Union[dict, ExperimentalReadout]], list[Union[dict, ExperimentalReadout]]]])

slots.ModelMechanismLink_evidence = Slot(uri=DISMECH.evidence, name="ModelMechanismLink_evidence", curie=DISMECH.curie('evidence'),
                   model_uri=DISMECH.ModelMechanismLink_evidence, domain=ModelMechanismLink, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.BiomarkerReadout_target = Slot(uri=DISMECH.target, name="BiomarkerReadout_target", curie=DISMECH.curie('target'),
                   model_uri=DISMECH.BiomarkerReadout_target, domain=BiomarkerReadout, range=str)

slots.BiomarkerReadout_relationship = Slot(uri=DISMECH.relationship, name="BiomarkerReadout_relationship", curie=DISMECH.curie('relationship'),
                   model_uri=DISMECH.BiomarkerReadout_relationship, domain=BiomarkerReadout, range=Union[str, "BiomarkerReadoutRelationshipEnum"])

slots.BiomarkerReadout_direction = Slot(uri=DISMECH.direction, name="BiomarkerReadout_direction", curie=DISMECH.curie('direction'),
                   model_uri=DISMECH.BiomarkerReadout_direction, domain=BiomarkerReadout, range=Optional[Union[str, "BiomarkerReadoutDirectionEnum"]])

slots.BiomarkerReadout_endpoint_context = Slot(uri=DISMECH.endpoint_context, name="BiomarkerReadout_endpoint_context", curie=DISMECH.curie('endpoint_context'),
                   model_uri=DISMECH.BiomarkerReadout_endpoint_context, domain=BiomarkerReadout, range=Optional[Union[str, "BiomarkerEndpointContextEnum"]])

slots.BiomarkerReadout_regulatory_endpoint_refs = Slot(uri=DISMECH.regulatory_endpoint_refs, name="BiomarkerReadout_regulatory_endpoint_refs", curie=DISMECH.curie('regulatory_endpoint_refs'),
                   model_uri=DISMECH.BiomarkerReadout_regulatory_endpoint_refs, domain=BiomarkerReadout, range=Optional[Union[str, list[str]]])

slots.BiomarkerReadout_interpretation = Slot(uri=DISMECH.interpretation, name="BiomarkerReadout_interpretation", curie=DISMECH.curie('interpretation'),
                   model_uri=DISMECH.BiomarkerReadout_interpretation, domain=BiomarkerReadout, range=Optional[str])

slots.BiomarkerReadout_evidence = Slot(uri=DISMECH.evidence, name="BiomarkerReadout_evidence", curie=DISMECH.curie('evidence'),
                   model_uri=DISMECH.BiomarkerReadout_evidence, domain=BiomarkerReadout, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.PhenotypeReadout_target = Slot(uri=DISMECH.target, name="PhenotypeReadout_target", curie=DISMECH.curie('target'),
                   model_uri=DISMECH.PhenotypeReadout_target, domain=PhenotypeReadout, range=str)

slots.PhenotypeReadout_relationship = Slot(uri=DISMECH.relationship, name="PhenotypeReadout_relationship", curie=DISMECH.curie('relationship'),
                   model_uri=DISMECH.PhenotypeReadout_relationship, domain=PhenotypeReadout, range=Union[str, "BiomarkerReadoutRelationshipEnum"])

slots.PhenotypeReadout_direction = Slot(uri=DISMECH.direction, name="PhenotypeReadout_direction", curie=DISMECH.curie('direction'),
                   model_uri=DISMECH.PhenotypeReadout_direction, domain=PhenotypeReadout, range=Optional[Union[str, "BiomarkerReadoutDirectionEnum"]])

slots.PhenotypeReadout_endpoint_context = Slot(uri=DISMECH.endpoint_context, name="PhenotypeReadout_endpoint_context", curie=DISMECH.curie('endpoint_context'),
                   model_uri=DISMECH.PhenotypeReadout_endpoint_context, domain=PhenotypeReadout, range=Optional[Union[str, "BiomarkerEndpointContextEnum"]])

slots.PhenotypeReadout_interpretation = Slot(uri=DISMECH.interpretation, name="PhenotypeReadout_interpretation", curie=DISMECH.curie('interpretation'),
                   model_uri=DISMECH.PhenotypeReadout_interpretation, domain=PhenotypeReadout, range=Optional[str])

slots.PhenotypeReadout_evidence = Slot(uri=DISMECH.evidence, name="PhenotypeReadout_evidence", curie=DISMECH.curie('evidence'),
                   model_uri=DISMECH.PhenotypeReadout_evidence, domain=PhenotypeReadout, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.ReferenceRangeBand_name = Slot(uri=DISMECH.name, name="ReferenceRangeBand_name", curie=DISMECH.curie('name'),
                   model_uri=DISMECH.ReferenceRangeBand_name, domain=ReferenceRangeBand, range=Union[str, ReferenceRangeBandName])

slots.ReferenceRangeBand_lower_bound = Slot(uri=DISMECH.lower_bound, name="ReferenceRangeBand_lower_bound", curie=DISMECH.curie('lower_bound'),
                   model_uri=DISMECH.ReferenceRangeBand_lower_bound, domain=ReferenceRangeBand, range=Optional[float])

slots.ReferenceRangeBand_upper_bound = Slot(uri=DISMECH.upper_bound, name="ReferenceRangeBand_upper_bound", curie=DISMECH.curie('upper_bound'),
                   model_uri=DISMECH.ReferenceRangeBand_upper_bound, domain=ReferenceRangeBand, range=Optional[float])

slots.ReferenceRangeBand_unit = Slot(uri=DISMECH.unit, name="ReferenceRangeBand_unit", curie=DISMECH.curie('unit'),
                   model_uri=DISMECH.ReferenceRangeBand_unit, domain=ReferenceRangeBand, range=Optional[str])

slots.ReferenceRangeBand_abnormal_flag = Slot(uri=DISMECH.abnormal_flag, name="ReferenceRangeBand_abnormal_flag", curie=DISMECH.curie('abnormal_flag'),
                   model_uri=DISMECH.ReferenceRangeBand_abnormal_flag, domain=ReferenceRangeBand, range=Optional[Union[str, "AbnormalFlagEnum"]])

slots.ReferenceRangeBand_severity = Slot(uri=DISMECH.severity, name="ReferenceRangeBand_severity", curie=DISMECH.curie('severity'),
                   model_uri=DISMECH.ReferenceRangeBand_severity, domain=ReferenceRangeBand, range=Optional[Union[dict, Any]])

slots.ReferenceRangeBand_phenotype_term = Slot(uri=DISMECH.phenotype_term, name="ReferenceRangeBand_phenotype_term", curie=DISMECH.curie('phenotype_term'),
                   model_uri=DISMECH.ReferenceRangeBand_phenotype_term, domain=ReferenceRangeBand, range=Optional[Union[dict, PhenotypeDescriptor]])

slots.ReferenceRangeBand_interpretation = Slot(uri=DISMECH.interpretation, name="ReferenceRangeBand_interpretation", curie=DISMECH.curie('interpretation'),
                   model_uri=DISMECH.ReferenceRangeBand_interpretation, domain=ReferenceRangeBand, range=Optional[str])

slots.ReferenceRange_loinc_term = Slot(uri=DISMECH.loinc_term, name="ReferenceRange_loinc_term", curie=DISMECH.curie('loinc_term'),
                   model_uri=DISMECH.ReferenceRange_loinc_term, domain=ReferenceRange, range=Optional[Union[dict, Term]])

slots.ReferenceRange_interpretation_bands = Slot(uri=DISMECH.interpretation_bands, name="ReferenceRange_interpretation_bands", curie=DISMECH.curie('interpretation_bands'),
                   model_uri=DISMECH.ReferenceRange_interpretation_bands, domain=ReferenceRange, range=Optional[Union[dict[Union[str, ReferenceRangeBandName], Union[dict, ReferenceRangeBand]], list[Union[dict, ReferenceRangeBand]]]])

slots.ReferenceRange_lower_bound = Slot(uri=DISMECH.lower_bound, name="ReferenceRange_lower_bound", curie=DISMECH.curie('lower_bound'),
                   model_uri=DISMECH.ReferenceRange_lower_bound, domain=ReferenceRange, range=Optional[float])

slots.ReferenceRange_upper_bound = Slot(uri=DISMECH.upper_bound, name="ReferenceRange_upper_bound", curie=DISMECH.curie('upper_bound'),
                   model_uri=DISMECH.ReferenceRange_upper_bound, domain=ReferenceRange, range=Optional[float])

slots.ReferenceRange_unit = Slot(uri=DISMECH.unit, name="ReferenceRange_unit", curie=DISMECH.curie('unit'),
                   model_uri=DISMECH.ReferenceRange_unit, domain=ReferenceRange, range=Optional[str])

slots.ReferenceRange_population = Slot(uri=DISMECH.population, name="ReferenceRange_population", curie=DISMECH.curie('population'),
                   model_uri=DISMECH.ReferenceRange_population, domain=ReferenceRange, range=Optional[str])

slots.ReferenceRange_evidence = Slot(uri=DISMECH.evidence, name="ReferenceRange_evidence", curie=DISMECH.curie('evidence'),
                   model_uri=DISMECH.ReferenceRange_evidence, domain=ReferenceRange, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.ReferenceRange_notes = Slot(uri=DISMECH.notes, name="ReferenceRange_notes", curie=DISMECH.curie('notes'),
                   model_uri=DISMECH.ReferenceRange_notes, domain=ReferenceRange, range=Optional[str])

slots.SurrogateEndpoint_row_id = Slot(uri=DISMECH.row_id, name="SurrogateEndpoint_row_id", curie=DISMECH.curie('row_id'),
                   model_uri=DISMECH.SurrogateEndpoint_row_id, domain=SurrogateEndpoint, range=Union[str, SurrogateEndpointRowId])

slots.SurrogateEndpoint_source_table = Slot(uri=DISMECH.source_table, name="SurrogateEndpoint_source_table", curie=DISMECH.curie('source_table'),
                   model_uri=DISMECH.SurrogateEndpoint_source_table, domain=SurrogateEndpoint, range=Union[str, "SurrogateEndpointTableEnum"])

slots.SurrogateEndpoint_source_sheet = Slot(uri=DISMECH.source_sheet, name="SurrogateEndpoint_source_sheet", curie=DISMECH.curie('source_sheet'),
                   model_uri=DISMECH.SurrogateEndpoint_source_sheet, domain=SurrogateEndpoint, range=str)

slots.SurrogateEndpoint_source_row_number = Slot(uri=DISMECH.source_row_number, name="SurrogateEndpoint_source_row_number", curie=DISMECH.curie('source_row_number'),
                   model_uri=DISMECH.SurrogateEndpoint_source_row_number, domain=SurrogateEndpoint, range=int)

slots.SurrogateEndpoint_disease_or_use = Slot(uri=DISMECH.disease_or_use, name="SurrogateEndpoint_disease_or_use", curie=DISMECH.curie('disease_or_use'),
                   model_uri=DISMECH.SurrogateEndpoint_disease_or_use, domain=SurrogateEndpoint, range=str)

slots.SurrogateEndpoint_patient_population = Slot(uri=DISMECH.patient_population, name="SurrogateEndpoint_patient_population", curie=DISMECH.curie('patient_population'),
                   model_uri=DISMECH.SurrogateEndpoint_patient_population, domain=SurrogateEndpoint, range=str)

slots.SurrogateEndpoint_surrogate_endpoint = Slot(uri=DISMECH.surrogate_endpoint, name="SurrogateEndpoint_surrogate_endpoint", curie=DISMECH.curie('surrogate_endpoint'),
                   model_uri=DISMECH.SurrogateEndpoint_surrogate_endpoint, domain=SurrogateEndpoint, range=str)

slots.SurrogateEndpoint_approval_type = Slot(uri=DISMECH.approval_type, name="SurrogateEndpoint_approval_type", curie=DISMECH.curie('approval_type'),
                   model_uri=DISMECH.SurrogateEndpoint_approval_type, domain=SurrogateEndpoint, range=Union[str, "SurrogateEndpointApprovalTypeEnum"])

slots.SurrogateEndpoint_endpoint_validation_level = Slot(uri=DISMECH.endpoint_validation_level, name="SurrogateEndpoint_endpoint_validation_level", curie=DISMECH.curie('endpoint_validation_level'),
                   model_uri=DISMECH.SurrogateEndpoint_endpoint_validation_level, domain=SurrogateEndpoint, range=Union[str, "SurrogateEndpointValidationLevelEnum"])

slots.SurrogateEndpoint_clinical_benefit_linkage = Slot(uri=DISMECH.clinical_benefit_linkage, name="SurrogateEndpoint_clinical_benefit_linkage", curie=DISMECH.curie('clinical_benefit_linkage'),
                   model_uri=DISMECH.SurrogateEndpoint_clinical_benefit_linkage, domain=SurrogateEndpoint, range=Union[str, "ClinicalBenefitLinkageEnum"])

slots.SurrogateEndpoint_clinical_benefit = Slot(uri=DISMECH.clinical_benefit, name="SurrogateEndpoint_clinical_benefit", curie=DISMECH.curie('clinical_benefit'),
                   model_uri=DISMECH.SurrogateEndpoint_clinical_benefit, domain=SurrogateEndpoint, range=Optional[str])

slots.SurrogateEndpoint_mapping_status = Slot(uri=DISMECH.mapping_status, name="SurrogateEndpoint_mapping_status", curie=DISMECH.curie('mapping_status'),
                   model_uri=DISMECH.SurrogateEndpoint_mapping_status, domain=SurrogateEndpoint, range=Union[str, "SurrogateEndpointMappingStatusEnum"])

slots.SurrogateEndpointCollection_name = Slot(uri=DISMECH.name, name="SurrogateEndpointCollection_name", curie=DISMECH.curie('name'),
                   model_uri=DISMECH.SurrogateEndpointCollection_name, domain=SurrogateEndpointCollection, range=Union[str, SurrogateEndpointCollectionName])

slots.SurrogateEndpointCollection_surrogate_endpoints = Slot(uri=DISMECH.surrogate_endpoints, name="SurrogateEndpointCollection_surrogate_endpoints", curie=DISMECH.curie('surrogate_endpoints'),
                   model_uri=DISMECH.SurrogateEndpointCollection_surrogate_endpoints, domain=SurrogateEndpointCollection, range=Union[dict[Union[str, SurrogateEndpointRowId], Union[dict, SurrogateEndpoint]], list[Union[dict, SurrogateEndpoint]]])

slots.PublicationReference_reference = Slot(uri=DISMECH.reference, name="PublicationReference_reference", curie=DISMECH.curie('reference'),
                   model_uri=DISMECH.PublicationReference_reference, domain=PublicationReference, range=Union[str, PublicationReferenceReference])

slots.PublicationReference_title = Slot(uri=DISMECH.title, name="PublicationReference_title", curie=DISMECH.curie('title'),
                   model_uri=DISMECH.PublicationReference_title, domain=PublicationReference, range=Optional[str])

slots.ExternalAssertion_source = Slot(uri=DISMECH.source, name="ExternalAssertion_source", curie=DISMECH.curie('source'),
                   model_uri=DISMECH.ExternalAssertion_source, domain=ExternalAssertion, range=str)

slots.ExternalAssertion_external_id = Slot(uri=DISMECH.external_id, name="ExternalAssertion_external_id", curie=DISMECH.curie('external_id'),
                   model_uri=DISMECH.ExternalAssertion_external_id, domain=ExternalAssertion, range=str)

slots.TrackedIssue_url = Slot(uri=DISMECH.url, name="TrackedIssue_url", curie=DISMECH.curie('url'),
                   model_uri=DISMECH.TrackedIssue_url, domain=TrackedIssue, range=Union[str, URI])

slots.TrackedIssue_title = Slot(uri=DISMECH.title, name="TrackedIssue_title", curie=DISMECH.curie('title'),
                   model_uri=DISMECH.TrackedIssue_title, domain=TrackedIssue, range=Optional[str])

slots.ClinicalBurden_burden_level = Slot(uri=DISMECH.burden_level, name="ClinicalBurden_burden_level", curie=DISMECH.curie('burden_level'),
                   model_uri=DISMECH.ClinicalBurden_burden_level, domain=ClinicalBurden, range=Union[str, "ClinicalBurdenLevelEnum"])

slots.ClinicalBurden_rationale = Slot(uri=DISMECH.rationale, name="ClinicalBurden_rationale", curie=DISMECH.curie('rationale'),
                   model_uri=DISMECH.ClinicalBurden_rationale, domain=ClinicalBurden, range=Optional[str])

slots.ClinicalBurden_evidence = Slot(uri=DISMECH.evidence, name="ClinicalBurden_evidence", curie=DISMECH.curie('evidence'),
                   model_uri=DISMECH.ClinicalBurden_evidence, domain=ClinicalBurden, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.HistopathologyFinding_name = Slot(uri=DISMECH.name, name="HistopathologyFinding_name", curie=DISMECH.curie('name'),
                   model_uri=DISMECH.HistopathologyFinding_name, domain=HistopathologyFinding, range=Union[str, HistopathologyFindingName])

slots.HistopathologyFinding_description = Slot(uri=DISMECH.description, name="HistopathologyFinding_description", curie=DISMECH.curie('description'),
                   model_uri=DISMECH.HistopathologyFinding_description, domain=HistopathologyFinding, range=Optional[str])

slots.HistopathologyFinding_frequency = Slot(uri=DISMECH.frequency, name="HistopathologyFinding_frequency", curie=DISMECH.curie('frequency'),
                   model_uri=DISMECH.HistopathologyFinding_frequency, domain=HistopathologyFinding, range=Optional[Union[dict, Any]])

slots.HistopathologyFinding_diagnostic = Slot(uri=DISMECH.diagnostic, name="HistopathologyFinding_diagnostic", curie=DISMECH.curie('diagnostic'),
                   model_uri=DISMECH.HistopathologyFinding_diagnostic, domain=HistopathologyFinding, range=Optional[Union[bool, Bool]])

slots.HistopathologyFinding_context = Slot(uri=DISMECH.context, name="HistopathologyFinding_context", curie=DISMECH.curie('context'),
                   model_uri=DISMECH.HistopathologyFinding_context, domain=HistopathologyFinding, range=Optional[str])

slots.ImagingFinding_name = Slot(uri=DISMECH.name, name="ImagingFinding_name", curie=DISMECH.curie('name'),
                   model_uri=DISMECH.ImagingFinding_name, domain=ImagingFinding, range=Union[str, ImagingFindingName])

slots.ImagingFinding_description = Slot(uri=DISMECH.description, name="ImagingFinding_description", curie=DISMECH.curie('description'),
                   model_uri=DISMECH.ImagingFinding_description, domain=ImagingFinding, range=Optional[str])

slots.ImagingFinding_modality = Slot(uri=DISMECH.modality, name="ImagingFinding_modality", curie=DISMECH.curie('modality'),
                   model_uri=DISMECH.ImagingFinding_modality, domain=ImagingFinding, range=Optional[Union[str, "ImagingModalityEnum"]])

slots.ImagingFinding_located_in = Slot(uri=DISMECH.located_in, name="ImagingFinding_located_in", curie=DISMECH.curie('located_in'),
                   model_uri=DISMECH.ImagingFinding_located_in, domain=ImagingFinding, range=Optional[Union[dict, AnatomicalEntityDescriptor]])

slots.ImagingFinding_phenotype_term = Slot(uri=DISMECH.phenotype_term, name="ImagingFinding_phenotype_term", curie=DISMECH.curie('phenotype_term'),
                   model_uri=DISMECH.ImagingFinding_phenotype_term, domain=ImagingFinding, range=Optional[Union[dict, PhenotypeDescriptor]])

slots.ImagingFinding_diagnostic = Slot(uri=DISMECH.diagnostic, name="ImagingFinding_diagnostic", curie=DISMECH.curie('diagnostic'),
                   model_uri=DISMECH.ImagingFinding_diagnostic, domain=ImagingFinding, range=Optional[Union[bool, Bool]])

slots.ImagingFinding_context = Slot(uri=DISMECH.context, name="ImagingFinding_context", curie=DISMECH.curie('context'),
                   model_uri=DISMECH.ImagingFinding_context, domain=ImagingFinding, range=Optional[str])

slots.Disease_name = Slot(uri=DISMECH.name, name="Disease_name", curie=DISMECH.curie('name'),
                   model_uri=DISMECH.Disease_name, domain=Disease, range=Union[str, DiseaseName])

slots.Disease_creation_date = Slot(uri=DISMECH.creation_date, name="Disease_creation_date", curie=DISMECH.curie('creation_date'),
                   model_uri=DISMECH.Disease_creation_date, domain=Disease, range=Optional[str],
                   pattern=re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+\-]\d{2}:\d{2})$'))

slots.Disease_updated_date = Slot(uri=DISMECH.updated_date, name="Disease_updated_date", curie=DISMECH.curie('updated_date'),
                   model_uri=DISMECH.Disease_updated_date, domain=Disease, range=Optional[str],
                   pattern=re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+\-]\d{2}:\d{2})$'))

slots.AnimalModel_publication = Slot(uri=DISMECH.publication, name="AnimalModel_publication", curie=DISMECH.curie('publication'),
                   model_uri=DISMECH.AnimalModel_publication, domain=AnimalModel, range=Optional[str])

slots.AnimalModel_modeled_mechanisms = Slot(uri=DISMECH.modeled_mechanisms, name="AnimalModel_modeled_mechanisms", curie=DISMECH.curie('modeled_mechanisms'),
                   model_uri=DISMECH.AnimalModel_modeled_mechanisms, domain=AnimalModel, range=Optional[Union[Union[dict, ModelMechanismLink], list[Union[dict, ModelMechanismLink]]]])

slots.ICDOMorphologyAssignment_classification_value = Slot(uri=DISMECH.classification_value, name="ICDOMorphologyAssignment_classification_value", curie=DISMECH.curie('classification_value'),
                   model_uri=DISMECH.ICDOMorphologyAssignment_classification_value, domain=ICDOMorphologyAssignment, range=Union[str, "ICDOMorphologyEnum"])

slots.HarrisonsChapterAssignment_classification_value = Slot(uri=DISMECH.classification_value, name="HarrisonsChapterAssignment_classification_value", curie=DISMECH.curie('classification_value'),
                   model_uri=DISMECH.HarrisonsChapterAssignment_classification_value, domain=HarrisonsChapterAssignment, range=Union[str, "HarrisonsChapterEnum"])

slots.LysosomalStorageAssignment_classification_value = Slot(uri=DISMECH.classification_value, name="LysosomalStorageAssignment_classification_value", curie=DISMECH.curie('classification_value'),
                   model_uri=DISMECH.LysosomalStorageAssignment_classification_value, domain=LysosomalStorageAssignment, range=Union[str, "LysosomalStorageEnum"])

slots.MechanisticNosologyAssignment_classification_value = Slot(uri=DISMECH.classification_value, name="MechanisticNosologyAssignment_classification_value", curie=DISMECH.curie('classification_value'),
                   model_uri=DISMECH.MechanisticNosologyAssignment_classification_value, domain=MechanisticNosologyAssignment, range=Union[str, "MechanisticNosologyEnum"])

slots.IUISAssignment_classification_value = Slot(uri=DISMECH.classification_value, name="IUISAssignment_classification_value", curie=DISMECH.curie('classification_value'),
                   model_uri=DISMECH.IUISAssignment_classification_value, domain=IUISAssignment, range=Union[str, "IUISCategoryEnum"])

slots.ChannelopathyAssignment_classification_value = Slot(uri=DISMECH.classification_value, name="ChannelopathyAssignment_classification_value", curie=DISMECH.curie('classification_value'),
                   model_uri=DISMECH.ChannelopathyAssignment_classification_value, domain=ChannelopathyAssignment, range=Union[str, "ChannelopathyOrganSystemEnum"])

slots.ICIMDAssignment_classification_value = Slot(uri=DISMECH.classification_value, name="ICIMDAssignment_classification_value", curie=DISMECH.curie('classification_value'),
                   model_uri=DISMECH.ICIMDAssignment_classification_value, domain=ICIMDAssignment, range=Union[str, "ICIMDEnum"])

slots.ISDSNosologyAssignment_classification_value = Slot(uri=DISMECH.classification_value, name="ISDSNosologyAssignment_classification_value", curie=DISMECH.curie('classification_value'),
                   model_uri=DISMECH.ISDSNosologyAssignment_classification_value, domain=ISDSNosologyAssignment, range=Union[str, "ISDSNosologyGroupEnum"])

slots.NIHResearchPriorityAssignment_classification_value = Slot(uri=DISMECH.classification_value, name="NIHResearchPriorityAssignment_classification_value", curie=DISMECH.curie('classification_value'),
                   model_uri=DISMECH.NIHResearchPriorityAssignment_classification_value, domain=NIHResearchPriorityAssignment, range=Union[str, "NIHResearchPriorityEnum"])

slots.ILOCausativeAgentAssignment_classification_value = Slot(uri=DISMECH.classification_value, name="ILOCausativeAgentAssignment_classification_value", curie=DISMECH.curie('classification_value'),
                   model_uri=DISMECH.ILOCausativeAgentAssignment_classification_value, domain=ILOCausativeAgentAssignment, range=Union[str, "ILOCausativeAgentEnum"])

slots.ILODiseaseCategoryAssignment_classification_value = Slot(uri=DISMECH.classification_value, name="ILODiseaseCategoryAssignment_classification_value", curie=DISMECH.curie('classification_value'),
                   model_uri=DISMECH.ILODiseaseCategoryAssignment_classification_value, domain=ILODiseaseCategoryAssignment, range=Union[str, "ILODiseaseCategoryEnum"])

slots.EUOccupationalScheduleAssignment_classification_value = Slot(uri=DISMECH.classification_value, name="EUOccupationalScheduleAssignment_classification_value", curie=DISMECH.curie('classification_value'),
                   model_uri=DISMECH.EUOccupationalScheduleAssignment_classification_value, domain=EUOccupationalScheduleAssignment, range=Union[str, "EUOccupationalScheduleEnum"])

slots.HazardAgentTypeAssignment_classification_value = Slot(uri=DISMECH.classification_value, name="HazardAgentTypeAssignment_classification_value", curie=DISMECH.curie('classification_value'),
                   model_uri=DISMECH.HazardAgentTypeAssignment_classification_value, domain=HazardAgentTypeAssignment, range=Union[str, "HazardAgentTypeEnum"])

slots.ExposureRouteAssignment_classification_value = Slot(uri=DISMECH.classification_value, name="ExposureRouteAssignment_classification_value", curie=DISMECH.curie('classification_value'),
                   model_uri=DISMECH.ExposureRouteAssignment_classification_value, domain=ExposureRouteAssignment, range=Union[str, "ExposureRouteEnum"])

slots.ExposureDurationAssignment_classification_value = Slot(uri=DISMECH.classification_value, name="ExposureDurationAssignment_classification_value", curie=DISMECH.curie('classification_value'),
                   model_uri=DISMECH.ExposureDurationAssignment_classification_value, domain=ExposureDurationAssignment, range=Union[str, "ExposureDurationEnum"])

slots.IARCCarcinogenGroupAssignment_classification_value = Slot(uri=DISMECH.classification_value, name="IARCCarcinogenGroupAssignment_classification_value", curie=DISMECH.curie('classification_value'),
                   model_uri=DISMECH.IARCCarcinogenGroupAssignment_classification_value, domain=IARCCarcinogenGroupAssignment, range=Union[str, "IARCCarcinogenGroupEnum"])

slots.GHSHealthHazardClassAssignment_classification_value = Slot(uri=DISMECH.classification_value, name="GHSHealthHazardClassAssignment_classification_value", curie=DISMECH.curie('classification_value'),
                   model_uri=DISMECH.GHSHealthHazardClassAssignment_classification_value, domain=GHSHealthHazardClassAssignment, range=Union[str, "GHSHealthHazardClassEnum"])

slots.ExposomeDomainAssignment_classification_value = Slot(uri=DISMECH.classification_value, name="ExposomeDomainAssignment_classification_value", curie=DISMECH.curie('classification_value'),
                   model_uri=DISMECH.ExposomeDomainAssignment_classification_value, domain=ExposomeDomainAssignment, range=Union[str, "ExposomeDomainEnum"])

slots.Definition_name = Slot(uri=DISMECH.name, name="Definition_name", curie=DISMECH.curie('name'),
                   model_uri=DISMECH.Definition_name, domain=Definition, range=Union[str, DefinitionName])

slots.Definition_definition_type = Slot(uri=DISMECH.definition_type, name="Definition_definition_type", curie=DISMECH.curie('definition_type'),
                   model_uri=DISMECH.Definition_definition_type, domain=Definition, range=Union[str, "DefinitionTypeEnum"])

slots.Definition_attaches_to = Slot(uri=DISMECH.attaches_to, name="Definition_attaches_to", curie=DISMECH.curie('attaches_to'),
                   model_uri=DISMECH.Definition_attaches_to, domain=Definition, range=Optional[Union[str, list[str]]])

slots.AlgorithmValidationStatus_status = Slot(uri=DISMECH.status, name="AlgorithmValidationStatus_status", curie=DISMECH.curie('status'),
                   model_uri=DISMECH.AlgorithmValidationStatus_status, domain=AlgorithmValidationStatus, range=Union[str, "AlgorithmValidationStatusEnum"])

slots.AlgorithmValidationStatus_rationale = Slot(uri=DISMECH.rationale, name="AlgorithmValidationStatus_rationale", curie=DISMECH.curie('rationale'),
                   model_uri=DISMECH.AlgorithmValidationStatus_rationale, domain=AlgorithmValidationStatus, range=Optional[str])

slots.CriteriaSet_name = Slot(uri=DISMECH.name, name="CriteriaSet_name", curie=DISMECH.curie('name'),
                   model_uri=DISMECH.CriteriaSet_name, domain=CriteriaSet, range=Union[str, CriteriaSetName])

slots.TermMapping_term = Slot(uri=DISMECH.term, name="TermMapping_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.TermMapping_term, domain=TermMapping, range=Union[dict, Term])

slots.TermMapping_mapping_predicate = Slot(uri=DISMECH.mapping_predicate, name="TermMapping_mapping_predicate", curie=DISMECH.curie('mapping_predicate'),
                   model_uri=DISMECH.TermMapping_mapping_predicate, domain=TermMapping, range=Union[str, URIorCURIE])

slots.ICD10CMMapping_term = Slot(uri=DISMECH.term, name="ICD10CMMapping_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.ICD10CMMapping_term, domain=ICD10CMMapping, range=Union[dict, Term])

slots.ICD11FMapping_term = Slot(uri=DISMECH.term, name="ICD11FMapping_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.ICD11FMapping_term, domain=ICD11FMapping, range=Union[dict, Term])

slots.MondoMapping_term = Slot(uri=DISMECH.term, name="MondoMapping_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.MondoMapping_term, domain=MondoMapping, range=Union[dict, Term])

slots.NCITMapping_term = Slot(uri=DISMECH.term, name="NCITMapping_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.NCITMapping_term, domain=NCITMapping, range=Union[dict, Term])

slots.MappingConsistency_reference = Slot(uri=DISMECH.reference, name="MappingConsistency_reference", curie=DISMECH.curie('reference'),
                   model_uri=DISMECH.MappingConsistency_reference, domain=MappingConsistency, range=str)

slots.MappingConsistency_consistent = Slot(uri=DISMECH.consistent, name="MappingConsistency_consistent", curie=DISMECH.curie('consistent'),
                   model_uri=DISMECH.MappingConsistency_consistent, domain=MappingConsistency, range=Union[str, "MappingConsistencyEnum"])

slots.ConditionDescriptor_slug = Slot(uri=DISMECH.slug, name="ConditionDescriptor_slug", curie=DISMECH.curie('slug'),
                   model_uri=DISMECH.ConditionDescriptor_slug, domain=ConditionDescriptor, range=Optional[str])

slots.ConditionDescriptor_term = Slot(uri=DISMECH.term, name="ConditionDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.ConditionDescriptor_term, domain=ConditionDescriptor, range=Optional[Union[dict, Term]])

slots.ConditionDescriptor_preferred_term = Slot(uri=DISMECH.preferred_term, name="ConditionDescriptor_preferred_term", curie=DISMECH.curie('preferred_term'),
                   model_uri=DISMECH.ConditionDescriptor_preferred_term, domain=ConditionDescriptor, range=str)

slots.ComorbidityAssociation_creation_date = Slot(uri=DISMECH.creation_date, name="ComorbidityAssociation_creation_date", curie=DISMECH.curie('creation_date'),
                   model_uri=DISMECH.ComorbidityAssociation_creation_date, domain=ComorbidityAssociation, range=Optional[str],
                   pattern=re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+\-]\d{2}:\d{2})$'))

slots.ComorbidityAssociation_updated_date = Slot(uri=DISMECH.updated_date, name="ComorbidityAssociation_updated_date", curie=DISMECH.curie('updated_date'),
                   model_uri=DISMECH.ComorbidityAssociation_updated_date, domain=ComorbidityAssociation, range=Optional[str],
                   pattern=re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+\-]\d{2}:\d{2})$'))

slots.AssociationSignal_source = Slot(uri=DISMECH.source, name="AssociationSignal_source", curie=DISMECH.curie('source'),
                   model_uri=DISMECH.AssociationSignal_source, domain=AssociationSignal, range=Optional[Union[str, "AssociationSignalSourceEnum"]])

slots.AssociationSignal_method = Slot(uri=DISMECH.method, name="AssociationSignal_method", curie=DISMECH.curie('method'),
                   model_uri=DISMECH.AssociationSignal_method, domain=AssociationSignal, range=Optional[Union[str, "AssociationSignalMethodEnum"]])

slots.Demographics_sex = Slot(uri=DISMECH.sex, name="Demographics_sex", curie=DISMECH.curie('sex'),
                   model_uri=DISMECH.Demographics_sex, domain=Demographics, range=Optional[Union[str, "SexEnum"]])

slots.MechanisticHypothesis_hypothesis_group_id = Slot(uri=DISMECH.hypothesis_group_id, name="MechanisticHypothesis_hypothesis_group_id", curie=DISMECH.curie('hypothesis_group_id'),
                   model_uri=DISMECH.MechanisticHypothesis_hypothesis_group_id, domain=MechanisticHypothesis, range=str)

slots.MechanisticHypothesis_status = Slot(uri=DISMECH.status, name="MechanisticHypothesis_status", curie=DISMECH.curie('status'),
                   model_uri=DISMECH.MechanisticHypothesis_status, domain=MechanisticHypothesis, range=Optional[Union[str, "MechanisticHypothesisStatusEnum"]])

slots.Discussion_discussion_id = Slot(uri=DISMECH.discussion_id, name="Discussion_discussion_id", curie=DISMECH.curie('discussion_id'),
                   model_uri=DISMECH.Discussion_discussion_id, domain=Discussion, range=str)

slots.Discussion_prompt = Slot(uri=DISMECH.prompt, name="Discussion_prompt", curie=DISMECH.curie('prompt'),
                   model_uri=DISMECH.Discussion_prompt, domain=Discussion, range=str)

slots.Discussion_kind = Slot(uri=DISMECH.kind, name="Discussion_kind", curie=DISMECH.curie('kind'),
                   model_uri=DISMECH.Discussion_kind, domain=Discussion, range=Optional[Union[str, "DiscussionKindEnum"]])

slots.Discussion_status = Slot(uri=DISMECH.status, name="Discussion_status", curie=DISMECH.curie('status'),
                   model_uri=DISMECH.Discussion_status, domain=Discussion, range=Optional[Union[str, "DiscussionStatusEnum"]])

slots.Grouping_name = Slot(uri=DISMECH.name, name="Grouping_name", curie=DISMECH.curie('name'),
                   model_uri=DISMECH.Grouping_name, domain=Grouping, range=Union[str, GroupingName])

slots.Grouping_creation_date = Slot(uri=DISMECH.creation_date, name="Grouping_creation_date", curie=DISMECH.curie('creation_date'),
                   model_uri=DISMECH.Grouping_creation_date, domain=Grouping, range=Optional[str],
                   pattern=re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+\-]\d{2}:\d{2})$'))

slots.Grouping_members = Slot(uri=DISMECH.members, name="Grouping_members", curie=DISMECH.curie('members'),
                   model_uri=DISMECH.Grouping_members, domain=Grouping, range=Union[Union[dict, "GroupingMember"], list[Union[dict, "GroupingMember"]]])

slots.GroupingCriteria_description = Slot(uri=DISMECH.description, name="GroupingCriteria_description", curie=DISMECH.curie('description'),
                   model_uri=DISMECH.GroupingCriteria_description, domain=GroupingCriteria, range=str)

slots.GroupingMember_member = Slot(uri=DISMECH.member, name="GroupingMember_member", curie=DISMECH.curie('member'),
                   model_uri=DISMECH.GroupingMember_member, domain=GroupingMember, range=str)

slots.GroupingMember_member_type = Slot(uri=DISMECH.member_type, name="GroupingMember_member_type", curie=DISMECH.curie('member_type'),
                   model_uri=DISMECH.GroupingMember_member_type, domain=GroupingMember, range=Optional[Union[str, "GroupingMemberTypeEnum"]])

slots.DifferentiatingMechanism_description = Slot(uri=DISMECH.description, name="DifferentiatingMechanism_description", curie=DISMECH.curie('description'),
                   model_uri=DISMECH.DifferentiatingMechanism_description, domain=DifferentiatingMechanism, range=str)

slots.ModuleCollection_name = Slot(uri=DISMECH.name, name="ModuleCollection_name", curie=DISMECH.curie('name'),
                   model_uri=DISMECH.ModuleCollection_name, domain=ModuleCollection, range=Union[str, ModuleCollectionName])

slots.ModuleCollection_creation_date = Slot(uri=DISMECH.creation_date, name="ModuleCollection_creation_date", curie=DISMECH.curie('creation_date'),
                   model_uri=DISMECH.ModuleCollection_creation_date, domain=ModuleCollection, range=Optional[str],
                   pattern=re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+\-]\d{2}:\d{2})$'))

slots.ModuleCollection_collection_type = Slot(uri=DISMECH.collection_type, name="ModuleCollection_collection_type", curie=DISMECH.curie('collection_type'),
                   model_uri=DISMECH.ModuleCollection_collection_type, domain=ModuleCollection, range=Union[str, "ModuleCollectionTypeEnum"])

slots.ModuleCollection_module_members = Slot(uri=DISMECH.module_members, name="ModuleCollection_module_members", curie=DISMECH.curie('module_members'),
                   model_uri=DISMECH.ModuleCollection_module_members, domain=ModuleCollection, range=Union[Union[dict, "ModuleCollectionMember"], list[Union[dict, "ModuleCollectionMember"]]])

slots.ModuleCollectionMember_module = Slot(uri=DISMECH.module, name="ModuleCollectionMember_module", curie=DISMECH.curie('module'),
                   model_uri=DISMECH.ModuleCollectionMember_module, domain=ModuleCollectionMember, range=str)
