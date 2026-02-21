# Auto generated from dismech.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-02-18T15:38:30
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

from linkml_runtime.linkml_model.types import Boolean, Datetime, Float, Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URI, URIorCURIE, XSDDateTime

metamodel_version = "1.7.0"
version = None

# Namespaces
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
CL = CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_')
ECTO = CurieNamespace('ECTO', 'http://purl.obolibrary.org/obo/ECTO_')
ENVO = CurieNamespace('ENVO', 'http://purl.obolibrary.org/obo/ENVO_')
EXO = CurieNamespace('ExO', 'http://purl.obolibrary.org/obo/ExO_')
GENO = CurieNamespace('GENO', 'http://purl.obolibrary.org/obo/GENO_')
GO = CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_')
HGNC = CurieNamespace('HGNC', 'https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/')
HP = CurieNamespace('HP', 'http://purl.obolibrary.org/obo/HP_')
ICD10CM = CurieNamespace('ICD10CM', 'http://purl.obolibrary.org/obo/ICD10CM_')
MONDO = CurieNamespace('MONDO', 'http://purl.obolibrary.org/obo/MONDO_')
NCBITAXON = CurieNamespace('NCBITaxon', 'http://purl.obolibrary.org/obo/NCBITaxon_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
OPL = CurieNamespace('OPL', 'http://purl.obolibrary.org/obo/OPL_')
PMID = CurieNamespace('PMID', 'http://www.ncbi.nlm.nih.gov/pubmed/')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
XCO = CurieNamespace('XCO', 'http://purl.obolibrary.org/obo/XCO_')
ARRAYEXPRESS = CurieNamespace('arrayexpress', 'https://www.ebi.ac.uk/biostudies/arrayexpress/studies/')
BIGG = CurieNamespace('bigg', 'https://bigg.ucsd.edu/models/')
BIOMODELS = CurieNamespace('biomodels', 'https://www.ebi.ac.uk/biomodels/')
CLINICALTRIALS = CurieNamespace('clinicaltrials', 'https://clinicaltrials.gov/study/')
CLINVAR = CurieNamespace('clinvar', 'https://www.ncbi.nlm.nih.gov/clinvar/variation/')
DBGAP = CurieNamespace('dbgap', 'https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=')
DISMECH = CurieNamespace('dismech', 'https://w3id.org/monarch-initiative/dismech/')
ENCODE = CurieNamespace('encode', 'https://www.encodeproject.org/experiments/')
GEO = CurieNamespace('geo', 'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=')
GTEX = CurieNamespace('gtex', 'https://gtexportal.org/home/datasets/')
HCA = CurieNamespace('hca', 'https://data.humancellatlas.org/explore/projects/')
ICD11F = CurieNamespace('icd11f', 'http://purl.obolibrary.org/obo/icd11f_')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
METABOLIGHTS = CurieNamespace('metabolights', 'https://www.ebi.ac.uk/metabolights/')
PHENOPACKET_STORE = CurieNamespace('phenopacket-store', 'https://github.com/monarch-initiative/phenopacket-store/tree/main/notebooks/')
PRIDE = CurieNamespace('pride', 'https://www.ebi.ac.uk/pride/archive/projects/')
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


class ClinicalTrialName(extended_str):
    pass


class ComputationalModelName(extended_str):
    pass


class DifferentialDiagnosisName(extended_str):
    pass


class SubtypeName(extended_str):
    pass


class PublicationReferenceReference(extended_str):
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
    binding, and post-composition via modifier, located_in, and laterality slots.
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
    A descriptor for histopathologic findings, bindable to NCIT Morphologic Finding (C35867), Histologic Grade
    (C18000), or HP Abnormal cell morphology (HP:0025461)
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
    A descriptor for treatments/medical actions, bindable to Medical Action Ontology (MAXO)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["TreatmentDescriptor"]
    class_class_curie: ClassVar[str] = "dismech:TreatmentDescriptor"
    class_name: ClassVar[str] = "TreatmentDescriptor"
    class_model_uri: ClassVar[URIRef] = DISMECH.TreatmentDescriptor

    preferred_term: str = None
    therapeutic_agent: Optional[Union[Union[dict, ChemicalEntityDescriptor], list[Union[dict, ChemicalEntityDescriptor]]]] = empty_list()
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_dict(slot_name="therapeutic_agent", slot_type=ChemicalEntityDescriptor, key_name="preferred_term", keyed=False)

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
    zygosity: Optional[Union[str, "ZygosityEnum"]] = None
    functional_impact: Optional[str] = None
    complementation_group: Optional[str] = None
    description: Optional[str] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.gene is not None and not isinstance(self.gene, GeneDescriptor):
            self.gene = GeneDescriptor(**as_dict(self.gene))

        if not isinstance(self.genes, list):
            self.genes = [self.genes] if self.genes is not None else []
        self.genes = [v if isinstance(v, GeneDescriptor) else GeneDescriptor(**as_dict(v)) for v in self.genes]

        if self.allele_type is not None and not isinstance(self.allele_type, str):
            self.allele_type = str(self.allele_type)

        if self.zygosity is not None and not isinstance(self.zygosity, ZygosityEnum):
            self.zygosity = ZygosityEnum(self.zygosity)

        if self.functional_impact is not None and not isinstance(self.functional_impact, str):
            self.functional_impact = str(self.functional_impact)

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
    severity: Optional[str] = None
    onset: Optional[Union[dict, OnsetDescriptor]] = None
    notes: Optional[str] = None
    evidence: Optional[Union[Union[dict, "EvidenceItem"], list[Union[dict, "EvidenceItem"]]]] = empty_list()
    genetic_context: Optional[Union[dict, GeneticContext]] = None
    sex: Optional[Union[str, "SexEnum"]] = None
    population: Optional[str] = None
    age_range: Optional[str] = None
    subtype: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.severity is not None and not isinstance(self.severity, str):
            self.severity = str(self.severity)

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

        if not isinstance(self.sample_types, list):
            self.sample_types = [self.sample_types] if self.sample_types is not None else []
        self.sample_types = [v if isinstance(v, SampleTypeDescriptor) else SampleTypeDescriptor(**as_dict(v)) for v in self.sample_types]

        if self.sample_count is not None and not isinstance(self.sample_count, int):
            self.sample_count = int(self.sample_count)

        if not isinstance(self.conditions, list):
            self.conditions = [self.conditions] if self.conditions is not None else []
        self.conditions = [v if isinstance(v, str) else str(v) for v in self.conditions]

        if not isinstance(self.exposures, list):
            self.exposures = [self.exposures] if self.exposures is not None else []
        self.exposures = [v if isinstance(v, ExposureDescriptor) else ExposureDescriptor(**as_dict(v)) for v in self.exposures]

        if not isinstance(self.genes, list):
            self.genes = [self.genes] if self.genes is not None else []
        self.genes = [v if isinstance(v, GeneDescriptor) else GeneDescriptor(**as_dict(v)) for v in self.genes]

        if self.platform is not None and not isinstance(self.platform, str):
            self.platform = str(self.platform)

        if self.publication is not None and not isinstance(self.publication, str):
            self.publication = str(self.publication)

        if not isinstance(self.findings, list):
            self.findings = [self.findings] if self.findings is not None else []
        self.findings = [v if isinstance(v, Finding) else Finding(**as_dict(v)) for v in self.findings]

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

        if not isinstance(self.target_phenotypes, list):
            self.target_phenotypes = [self.target_phenotypes] if self.target_phenotypes is not None else []
        self.target_phenotypes = [v if isinstance(v, PhenotypeDescriptor) else PhenotypeDescriptor(**as_dict(v)) for v in self.target_phenotypes]

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

        if not isinstance(self.perturbations, list):
            self.perturbations = [self.perturbations] if self.perturbations is not None else []
        self.perturbations = [v if isinstance(v, GeneDescriptor) else GeneDescriptor(**as_dict(v)) for v in self.perturbations]

        if self.model_software is not None and not isinstance(self.model_software, str):
            self.model_software = str(self.model_software)

        if self.model_format is not None and not isinstance(self.model_format, str):
            self.model_format = str(self.model_format)

        if self.publication is not None and not isinstance(self.publication, str):
            self.publication = str(self.publication)

        if not isinstance(self.findings, list):
            self.findings = [self.findings] if self.findings is not None else []
        self.findings = [v if isinstance(v, Finding) else Finding(**as_dict(v)) for v in self.findings]

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

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
    subtype_term: Optional[Union[dict, DiseaseDescriptor]] = None
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

        if self.subtype_term is not None and not isinstance(self.subtype_term, DiseaseDescriptor):
            self.subtype_term = DiseaseDescriptor(**as_dict(self.subtype_term))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.review_notes is not None and not isinstance(self.review_notes, str):
            self.review_notes = str(self.review_notes)

        if not isinstance(self.locations, list):
            self.locations = [self.locations] if self.locations is not None else []
        self.locations = [v if isinstance(v, AnatomicalEntityDescriptor) else AnatomicalEntityDescriptor(**as_dict(v)) for v in self.locations]

        if self.classification is not None and not isinstance(self.classification, str):
            self.classification = str(self.classification)

        if not isinstance(self.children, list):
            self.children = [self.children] if self.children is not None else []
        self.children = [v if isinstance(v, str) else str(v) for v in self.children]

        if not isinstance(self.genes, list):
            self.genes = [self.genes] if self.genes is not None else []
        self.genes = [v if isinstance(v, GeneDescriptor) else GeneDescriptor(**as_dict(v)) for v in self.genes]

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
    supports: Optional[Union[str, "EvidenceItemSupportEnum"]] = None
    evidence_source: Optional[Union[str, "EvidenceSourceEnum"]] = None
    snippet: Optional[str] = None
    explanation: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.reference is not None and not isinstance(self.reference, str):
            self.reference = str(self.reference)

        if self.supports is not None and not isinstance(self.supports, EvidenceItemSupportEnum):
            self.supports = EvidenceItemSupportEnum(self.supports)

        if self.evidence_source is not None and not isinstance(self.evidence_source, EvidenceSourceEnum):
            self.evidence_source = EvidenceSourceEnum(self.evidence_source)

        if self.snippet is not None and not isinstance(self.snippet, str):
            self.snippet = str(self.snippet)

        if self.explanation is not None and not isinstance(self.explanation, str):
            self.explanation = str(self.explanation)

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
    findings: Optional[Union[Union[dict, "Finding"], list[Union[dict, "Finding"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.reference):
            self.MissingRequiredField("reference")
        if not isinstance(self.reference, PublicationReferenceReference):
            self.reference = PublicationReferenceReference(self.reference)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.findings, list):
            self.findings = [self.findings] if self.findings is not None else []
        self.findings = [v if isinstance(v, Finding) else Finding(**as_dict(v)) for v in self.findings]

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
    percentage: Optional[Union[dict, Any]] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subtype is not None and not isinstance(self.subtype, str):
            self.subtype = str(self.subtype)

        if self.population is not None and not isinstance(self.population, str):
            self.population = str(self.population)

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
    locations: Optional[Union[Union[dict, AnatomicalEntityDescriptor], list[Union[dict, AnatomicalEntityDescriptor]]]] = empty_list()
    examples: Optional[Union[str, list[str]]] = empty_list()
    role: Optional[str] = None
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

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, PathophysiologyName):
            self.name = PathophysiologyName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.cell_types, list):
            self.cell_types = [self.cell_types] if self.cell_types is not None else []
        self.cell_types = [v if isinstance(v, CellTypeDescriptor) else CellTypeDescriptor(**as_dict(v)) for v in self.cell_types]

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if not isinstance(self.biological_processes, list):
            self.biological_processes = [self.biological_processes] if self.biological_processes is not None else []
        self.biological_processes = [v if isinstance(v, BiologicalProcessDescriptor) else BiologicalProcessDescriptor(**as_dict(v)) for v in self.biological_processes]

        if not isinstance(self.locations, list):
            self.locations = [self.locations] if self.locations is not None else []
        self.locations = [v if isinstance(v, AnatomicalEntityDescriptor) else AnatomicalEntityDescriptor(**as_dict(v)) for v in self.locations]

        if not isinstance(self.examples, list):
            self.examples = [self.examples] if self.examples is not None else []
        self.examples = [v if isinstance(v, str) else str(v) for v in self.examples]

        if self.role is not None and not isinstance(self.role, str):
            self.role = str(self.role)

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

        if not isinstance(self.pathways, list):
            self.pathways = [self.pathways] if self.pathways is not None else []
        self.pathways = [v if isinstance(v, BiologicalProcessDescriptor) else BiologicalProcessDescriptor(**as_dict(v)) for v in self.pathways]

        if not isinstance(self.downstream, list):
            self.downstream = [self.downstream] if self.downstream is not None else []
        self.downstream = [v if isinstance(v, CausalEdge) else CausalEdge(**as_dict(v)) for v in self.downstream]

        if not isinstance(self.genes, list):
            self.genes = [self.genes] if self.genes is not None else []
        self.genes = [v if isinstance(v, GeneDescriptor) else GeneDescriptor(**as_dict(v)) for v in self.genes]

        if not isinstance(self.subtypes, list):
            self.subtypes = [self.subtypes] if self.subtypes is not None else []
        self.subtypes = [v if isinstance(v, str) else str(v) for v in self.subtypes]

        if not isinstance(self.cellular_components, list):
            self.cellular_components = [self.cellular_components] if self.cellular_components is not None else []
        self.cellular_components = [v if isinstance(v, CellularComponentDescriptor) else CellularComponentDescriptor(**as_dict(v)) for v in self.cellular_components]

        if not isinstance(self.protein_complexes, list):
            self.protein_complexes = [self.protein_complexes] if self.protein_complexes is not None else []
        self.protein_complexes = [v if isinstance(v, ProteinComplexDescriptor) else ProteinComplexDescriptor(**as_dict(v)) for v in self.protein_complexes]

        if not isinstance(self.chemical_entities, list):
            self.chemical_entities = [self.chemical_entities] if self.chemical_entities is not None else []
        self.chemical_entities = [v if isinstance(v, ChemicalEntityDescriptor) else ChemicalEntityDescriptor(**as_dict(v)) for v in self.chemical_entities]

        if not isinstance(self.gene_products, list):
            self.gene_products = [self.gene_products] if self.gene_products is not None else []
        self.gene_products = [v if isinstance(v, GeneProductDescriptor) else GeneProductDescriptor(**as_dict(v)) for v in self.gene_products]

        if not isinstance(self.triggers, list):
            self.triggers = [self.triggers] if self.triggers is not None else []
        self.triggers = [v if isinstance(v, TriggerDescriptor) else TriggerDescriptor(**as_dict(v)) for v in self.triggers]

        if not isinstance(self.assays, list):
            self.assays = [self.assays] if self.assays is not None else []
        self.assays = [v if isinstance(v, AssayDescriptor) else AssayDescriptor(**as_dict(v)) for v in self.assays]

        if not isinstance(self.mechanisms, list):
            self.mechanisms = [self.mechanisms] if self.mechanisms is not None else []
        self.mechanisms = [v if isinstance(v, str) else str(v) for v in self.mechanisms]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

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
    severity: Optional[str] = None
    notes: Optional[str] = None
    subtype: Optional[str] = None
    phenotype_contexts: Optional[Union[Union[dict, PhenotypeContext], list[Union[dict, PhenotypeContext]]]] = empty_list()

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

        if not isinstance(self.sequelae, list):
            self.sequelae = [self.sequelae] if self.sequelae is not None else []
        self.sequelae = [v if isinstance(v, CausalEdge) else CausalEdge(**as_dict(v)) for v in self.sequelae]

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.context is not None and not isinstance(self.context, str):
            self.context = str(self.context)

        if self.review_notes is not None and not isinstance(self.review_notes, str):
            self.review_notes = str(self.review_notes)

        if self.severity is not None and not isinstance(self.severity, str):
            self.severity = str(self.severity)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.subtype is not None and not isinstance(self.subtype, str):
            self.subtype = str(self.subtype)

        if not isinstance(self.phenotype_contexts, list):
            self.phenotype_contexts = [self.phenotype_contexts] if self.phenotype_contexts is not None else []
        self.phenotype_contexts = [v if isinstance(v, PhenotypeContext) else PhenotypeContext(**as_dict(v)) for v in self.phenotype_contexts]

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
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    specificity: Optional[str] = None
    frequency: Optional[Union[dict, Any]] = None
    notes: Optional[str] = None
    context: Optional[str] = None
    subtype: Optional[str] = None
    cell_types: Optional[Union[Union[dict, CellTypeDescriptor], list[Union[dict, CellTypeDescriptor]]]] = empty_list()
    assays: Optional[Union[Union[dict, AssayDescriptor], list[Union[dict, AssayDescriptor]]]] = empty_list()
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

        if not isinstance(self.cell_types, list):
            self.cell_types = [self.cell_types] if self.cell_types is not None else []
        self.cell_types = [v if isinstance(v, CellTypeDescriptor) else CellTypeDescriptor(**as_dict(v)) for v in self.cell_types]

        if not isinstance(self.assays, list):
            self.assays = [self.assays] if self.assays is not None else []
        self.assays = [v if isinstance(v, AssayDescriptor) else AssayDescriptor(**as_dict(v)) for v in self.assays]

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
    review_notes: Optional[str] = None
    subtype: Optional[str] = None
    frequency: Optional[Union[dict, Any]] = None
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

        if self.review_notes is not None and not isinstance(self.review_notes, str):
            self.review_notes = str(self.review_notes)

        if self.subtype is not None and not isinstance(self.subtype, str):
            self.subtype = str(self.subtype)

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
    pathophysiology: Optional[Union[dict[Union[str, PathophysiologyName], Union[dict, Pathophysiology]], list[Union[dict, Pathophysiology]]]] = empty_dict()
    mechanistic_hypotheses: Optional[Union[Union[dict, "MechanisticHypothesis"], list[Union[dict, "MechanisticHypothesis"]]]] = empty_list()
    phenotypes: Optional[Union[dict[Union[str, PhenotypeName], Union[dict, Phenotype]], list[Union[dict, Phenotype]]]] = empty_dict()
    histopathology: Optional[Union[dict[Union[str, HistopathologyFindingName], Union[dict, HistopathologyFinding]], list[Union[dict, HistopathologyFinding]]]] = empty_dict()
    biochemical: Optional[Union[dict[Union[str, BiochemicalName], Union[dict, Biochemical]], list[Union[dict, Biochemical]]]] = empty_dict()
    stages: Optional[Union[dict[Union[str, StageName], Union[dict, "Stage"]], list[Union[dict, "Stage"]]]] = empty_dict()
    genetic: Optional[Union[dict[Union[str, GeneticName], Union[dict, Genetic]], list[Union[dict, Genetic]]]] = empty_dict()
    variants: Optional[Union[dict[Union[str, VariantName], Union[dict, "Variant"]], list[Union[dict, "Variant"]]]] = empty_dict()
    environmental: Optional[Union[dict[Union[str, EnvironmentalName], Union[dict, Environmental]], list[Union[dict, Environmental]]]] = empty_dict()
    treatments: Optional[Union[dict[Union[str, TreatmentName], Union[dict, "Treatment"]], list[Union[dict, "Treatment"]]]] = empty_dict()
    categories: Optional[Union[str, list[str]]] = empty_list()
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
    datasets: Optional[Union[dict[Union[str, DatasetAccession], Union[dict, Dataset]], list[Union[dict, Dataset]]]] = empty_dict()
    clinical_trials: Optional[Union[dict[Union[str, ClinicalTrialName], Union[dict, ClinicalTrial]], list[Union[dict, ClinicalTrial]]]] = empty_dict()
    computational_models: Optional[Union[dict[Union[str, ComputationalModelName], Union[dict, ComputationalModel]], list[Union[dict, ComputationalModel]]]] = empty_dict()
    classifications: Optional[Union[dict, "DiseaseClassifications"]] = None
    definitions: Optional[Union[dict[Union[str, DefinitionName], Union[dict, "Definition"]], list[Union[dict, "Definition"]]]] = empty_dict()
    mappings: Optional[Union[dict, "DiseaseMappings"]] = None
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

        self._normalize_inlined_as_list(slot_name="pathophysiology", slot_type=Pathophysiology, key_name="name", keyed=True)

        if not isinstance(self.mechanistic_hypotheses, list):
            self.mechanistic_hypotheses = [self.mechanistic_hypotheses] if self.mechanistic_hypotheses is not None else []
        self.mechanistic_hypotheses = [v if isinstance(v, MechanisticHypothesis) else MechanisticHypothesis(**as_dict(v)) for v in self.mechanistic_hypotheses]

        self._normalize_inlined_as_list(slot_name="phenotypes", slot_type=Phenotype, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="histopathology", slot_type=HistopathologyFinding, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="biochemical", slot_type=Biochemical, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="stages", slot_type=Stage, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="genetic", slot_type=Genetic, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="variants", slot_type=Variant, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="environmental", slot_type=Environmental, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="treatments", slot_type=Treatment, key_name="name", keyed=True)

        if not isinstance(self.categories, list):
            self.categories = [self.categories] if self.categories is not None else []
        self.categories = [v if isinstance(v, str) else str(v) for v in self.categories]

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

        self._normalize_inlined_as_list(slot_name="datasets", slot_type=Dataset, key_name="accession", keyed=True)

        self._normalize_inlined_as_list(slot_name="clinical_trials", slot_type=ClinicalTrial, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="computational_models", slot_type=ComputationalModel, key_name="name", keyed=True)

        if self.classifications is not None and not isinstance(self.classifications, DiseaseClassifications):
            self.classifications = DiseaseClassifications(**as_dict(self.classifications))

        self._normalize_inlined_as_list(slot_name="definitions", slot_type=Definition, key_name="name", keyed=True)

        if self.mappings is not None and not isinstance(self.mappings, DiseaseMappings):
            self.mappings = DiseaseMappings(**as_dict(self.mappings))

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.review_notes is not None and not isinstance(self.review_notes, str):
            self.review_notes = str(self.review_notes)

        if not isinstance(self.curation_history, list):
            self.curation_history = [self.curation_history] if self.curation_history is not None else []
        self.curation_history = [v if isinstance(v, CurationEvent) else CurationEvent(**as_dict(v)) for v in self.curation_history]

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

        if not isinstance(self.hosts, list):
            self.hosts = [self.hosts] if self.hosts is not None else []
        self.hosts = [v if isinstance(v, HostDescriptor) else HostDescriptor(**as_dict(v)) for v in self.hosts]

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
    associated_phenotypes: Optional[Union[str, list[str]]] = empty_list()
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.species is not None and not isinstance(self.species, str):
            self.species = str(self.species)

        if self.genotype is not None and not isinstance(self.genotype, str):
            self.genotype = str(self.genotype)

        if self.background is not None and not isinstance(self.background, str):
            self.background = str(self.background)

        if not isinstance(self.genes, list):
            self.genes = [self.genes] if self.genes is not None else []
        self.genes = [v if isinstance(v, GeneDescriptor) else GeneDescriptor(**as_dict(v)) for v in self.genes]

        if self.category is not None and not isinstance(self.category, str):
            self.category = str(self.category)

        if not isinstance(self.alleles, list):
            self.alleles = [self.alleles] if self.alleles is not None else []
        self.alleles = [v if isinstance(v, str) else str(v) for v in self.alleles]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.associated_phenotypes, list):
            self.associated_phenotypes = [self.associated_phenotypes] if self.associated_phenotypes is not None else []
        self.associated_phenotypes = [v if isinstance(v, str) else str(v) for v in self.associated_phenotypes]

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

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
    treatment_term: Optional[Union[dict, TreatmentDescriptor]] = None
    regimen_term: Optional[Union[dict, RegimenDescriptor]] = None
    target_phenotypes: Optional[Union[Union[dict, PhenotypeDescriptor], list[Union[dict, PhenotypeDescriptor]]]] = empty_list()
    target_mechanisms: Optional[Union[Union[dict, TreatmentMechanismTarget], list[Union[dict, TreatmentMechanismTarget]]]] = empty_list()
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

        if self.treatment_term is not None and not isinstance(self.treatment_term, TreatmentDescriptor):
            self.treatment_term = TreatmentDescriptor(**as_dict(self.treatment_term))

        if self.regimen_term is not None and not isinstance(self.regimen_term, RegimenDescriptor):
            self.regimen_term = RegimenDescriptor(**as_dict(self.regimen_term))

        if not isinstance(self.target_phenotypes, list):
            self.target_phenotypes = [self.target_phenotypes] if self.target_phenotypes is not None else []
        self.target_phenotypes = [v if isinstance(v, PhenotypeDescriptor) else PhenotypeDescriptor(**as_dict(v)) for v in self.target_phenotypes]

        if not isinstance(self.target_mechanisms, list):
            self.target_mechanisms = [self.target_mechanisms] if self.target_mechanisms is not None else []
        self.target_mechanisms = [v if isinstance(v, TreatmentMechanismTarget) else TreatmentMechanismTarget(**as_dict(v)) for v in self.target_mechanisms]

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
class InfectiousAgent(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["InfectiousAgent"]
    class_class_curie: ClassVar[str] = "dismech:InfectiousAgent"
    class_name: ClassVar[str] = "InfectiousAgent"
    class_model_uri: ClassVar[URIRef] = DISMECH.InfectiousAgent

    name: Union[str, InfectiousAgentName] = None
    infectious_agent_term: Optional[Union[dict, OrganismDescriptor]] = None
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
    sequence_length: Optional[int] = None
    clinical_significance: Optional[Union[str, "ClinicalSignificanceEnum"]] = None
    type: Optional[str] = None

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

        if self.sequence_length is not None and not isinstance(self.sequence_length, int):
            self.sequence_length = int(self.sequence_length)

        if self.clinical_significance is not None and not isinstance(self.clinical_significance, ClinicalSignificanceEnum):
            self.clinical_significance = ClinicalSignificanceEnum(self.clinical_significance)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FunctionalEffect(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["FunctionalEffect"]
    class_class_curie: ClassVar[str] = "dismech:FunctionalEffect"
    class_name: ClassVar[str] = "FunctionalEffect"
    class_model_uri: ClassVar[URIRef] = DISMECH.FunctionalEffect

    function: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.function is not None and not isinstance(self.function, str):
            self.function = str(self.function)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

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

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.icdo_morphology is not None and not isinstance(self.icdo_morphology, ICDOMorphologyAssignment):
            self.icdo_morphology = ICDOMorphologyAssignment(**as_dict(self.icdo_morphology))

        self._normalize_inlined_as_dict(slot_name="harrisons_chapter", slot_type=HarrisonsChapterAssignment, key_name="classification_value", keyed=False)

        if self.lysosomal_storage_category is not None and not isinstance(self.lysosomal_storage_category, LysosomalStorageAssignment):
            self.lysosomal_storage_category = LysosomalStorageAssignment(**as_dict(self.lysosomal_storage_category))

        self._normalize_inlined_as_dict(slot_name="mechanistic_category", slot_type=MechanisticNosologyAssignment, key_name="classification_value", keyed=False)

        if self.iuis_category is not None and not isinstance(self.iuis_category, IUISAssignment):
            self.iuis_category = IUISAssignment(**as_dict(self.iuis_category))

        if self.channelopathy_category is not None and not isinstance(self.channelopathy_category, ChannelopathyAssignment):
            self.channelopathy_category = ChannelopathyAssignment(**as_dict(self.channelopathy_category))

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
    description: Optional[str] = None
    scope: Optional[str] = None
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

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.scope is not None and not isinstance(self.scope, str):
            self.scope = str(self.scope)

        self._normalize_inlined_as_list(slot_name="criteria_sets", slot_type=CriteriaSet, key_name="name", keyed=True)

        if not isinstance(self.inclusion_criteria, list):
            self.inclusion_criteria = [self.inclusion_criteria] if self.inclusion_criteria is not None else []
        self.inclusion_criteria = [v if isinstance(v, CriteriaItem) else CriteriaItem(**as_dict(v)) for v in self.inclusion_criteria]

        if not isinstance(self.exclusion_criteria, list):
            self.exclusion_criteria = [self.exclusion_criteria] if self.exclusion_criteria is not None else []
        self.exclusion_criteria = [v if isinstance(v, CriteriaItem) else CriteriaItem(**as_dict(v)) for v in self.exclusion_criteria]

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

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

        if not isinstance(self.core_clinical_characteristics, list):
            self.core_clinical_characteristics = [self.core_clinical_characteristics] if self.core_clinical_characteristics is not None else []
        self.core_clinical_characteristics = [v if isinstance(v, CriteriaItem) else CriteriaItem(**as_dict(v)) for v in self.core_clinical_characteristics]

        if not isinstance(self.inclusion_criteria, list):
            self.inclusion_criteria = [self.inclusion_criteria] if self.inclusion_criteria is not None else []
        self.inclusion_criteria = [v if isinstance(v, CriteriaItem) else CriteriaItem(**as_dict(v)) for v in self.inclusion_criteria]

        if not isinstance(self.exclusion_criteria, list):
            self.exclusion_criteria = [self.exclusion_criteria] if self.exclusion_criteria is not None else []
        self.exclusion_criteria = [v if isinstance(v, CriteriaItem) else CriteriaItem(**as_dict(v)) for v in self.exclusion_criteria]

        if not isinstance(self.imaging_requirements, list):
            self.imaging_requirements = [self.imaging_requirements] if self.imaging_requirements is not None else []
        self.imaging_requirements = [v if isinstance(v, CriteriaItem) else CriteriaItem(**as_dict(v)) for v in self.imaging_requirements]

        if not isinstance(self.laboratory_requirements, list):
            self.laboratory_requirements = [self.laboratory_requirements] if self.laboratory_requirements is not None else []
        self.laboratory_requirements = [v if isinstance(v, CriteriaItem) else CriteriaItem(**as_dict(v)) for v in self.laboratory_requirements]

        if not isinstance(self.additional_requirements, list):
            self.additional_requirements = [self.additional_requirements] if self.additional_requirements is not None else []
        self.additional_requirements = [v if isinstance(v, CriteriaItem) else CriteriaItem(**as_dict(v)) for v in self.additional_requirements]

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

        if not isinstance(self.consistency, list):
            self.consistency = [self.consistency] if self.consistency is not None else []
        self.consistency = [v if isinstance(v, MappingConsistency) else MappingConsistency(**as_dict(v)) for v in self.consistency]

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
    Container for external identifier mappings for a disease
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["DiseaseMappings"]
    class_class_curie: ClassVar[str] = "dismech:DiseaseMappings"
    class_name: ClassVar[str] = "DiseaseMappings"
    class_model_uri: ClassVar[URIRef] = DISMECH.DiseaseMappings

    icd10cm_mappings: Optional[Union[Union[dict, ICD10CMMapping], list[Union[dict, ICD10CMMapping]]]] = empty_list()
    icd11f_mappings: Optional[Union[Union[dict, ICD11FMapping], list[Union[dict, ICD11FMapping]]]] = empty_list()
    mondo_mappings: Optional[Union[Union[dict, MondoMapping], list[Union[dict, MondoMapping]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.icd10cm_mappings, list):
            self.icd10cm_mappings = [self.icd10cm_mappings] if self.icd10cm_mappings is not None else []
        self.icd10cm_mappings = [v if isinstance(v, ICD10CMMapping) else ICD10CMMapping(**as_dict(v)) for v in self.icd10cm_mappings]

        if not isinstance(self.icd11f_mappings, list):
            self.icd11f_mappings = [self.icd11f_mappings] if self.icd11f_mappings is not None else []
        self.icd11f_mappings = [v if isinstance(v, ICD11FMapping) else ICD11FMapping(**as_dict(v)) for v in self.icd11f_mappings]

        if not isinstance(self.mondo_mappings, list):
            self.mondo_mappings = [self.mondo_mappings] if self.mondo_mappings is not None else []
        self.mondo_mappings = [v if isinstance(v, MondoMapping) else MondoMapping(**as_dict(v)) for v in self.mondo_mappings]

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

        if not isinstance(self.components, list):
            self.components = [self.components] if self.components is not None else []
        self.components = [v if isinstance(v, ConditionDescriptor) else ConditionDescriptor(**as_dict(v)) for v in self.components]

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
    limited_precision: Optional[bool] = None
    precision_count_threshold: Optional[int] = None
    directionality: Optional[Union[str, "ComorbidityDirectionEnum"]] = None
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

        if self.limited_precision is not None and not isinstance(self.limited_precision, bool):
            self.limited_precision = bool(self.limited_precision)

        if self.precision_count_threshold is not None and not isinstance(self.precision_count_threshold, int):
            self.precision_count_threshold = int(self.precision_count_threshold)

        if self.directionality is not None and not isinstance(self.directionality, ComorbidityDirectionEnum):
            self.directionality = ComorbidityDirectionEnum(self.directionality)

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


# Enumerations
class EvidenceItemSupportEnum(EnumDefinitionImpl):
    """
    The level of support for an evidence item
    """
    WRONG_STATEMENT = PermissibleValue(
        text="WRONG_STATEMENT",
        description="WRONG_STATEMENT")
    SUPPORT = PermissibleValue(
        text="SUPPORT",
        description="SUPPORT")
    REFUTE = PermissibleValue(
        text="REFUTE",
        description="REFUTE")
    NO_EVIDENCE = PermissibleValue(
        text="NO_EVIDENCE",
        description="NO_EVIDENCE")
    PARTIAL = PermissibleValue(
        text="PARTIAL",
        description="PARTIAL")

    _defn = EnumDefinition(
        name="EvidenceItemSupportEnum",
        description="The level of support for an evidence item",
    )

class EvidenceSourceEnum(EnumDefinitionImpl):
    """
    The provenance/source of the evidence item
    """
    HUMAN_CLINICAL = PermissibleValue(
        text="HUMAN_CLINICAL",
        description="Human clinical observations (patients, cohorts, case reports, clinical trials, epidemiology)")
    MODEL_ORGANISM = PermissibleValue(
        text="MODEL_ORGANISM",
        description="""In vivo animal evidence (mouse, zebrafish, primate, veterinary case series including dog/cat/horse, other non-human animal models etc.)""")
    IN_VITRO = PermissibleValue(
        text="IN_VITRO",
        description="In vitro or ex vivo assays (cell culture, organoids, tissue slices, biochemical assays)")
    COMPUTATIONAL = PermissibleValue(
        text="COMPUTATIONAL",
        description="""In silico/modeling studies (simulation, docking, ML predictions, network inference) even when using clinical data inputs""")
    OTHER = PermissibleValue(
        text="OTHER",
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
        description="Algorithmic phenotype definition (e.g., PheKB-style)")
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
    FREQUENT = PermissibleValue(
        text="FREQUENT",
        description="Frequent",
        meaning=HP["0040282"])
    OCCASIONAL = PermissibleValue(
        text="OCCASIONAL",
        description="Occasional",
        meaning=HP["0040283"])
    VERY_FREQUENT = PermissibleValue(
        text="VERY_FREQUENT",
        description="Very frequent",
        meaning=HP["0040281"])
    VERY_RARE = PermissibleValue(
        text="VERY_RARE",
        description="Very rare",
        meaning=HP["0040284"])
    OBLIGATE = PermissibleValue(
        text="OBLIGATE",
        description="Obligate",
        meaning=HP["0040280"])

    _defn = EnumDefinition(
        name="FrequencyEnum",
        description="The frequency of an event or phenomenon",
    )

class ClinicalSignificanceEnum(EnumDefinitionImpl):
    """
    The clinical significance of a variant for a condition (ACMG guidelines)
    """
    PATHOGENIC = PermissibleValue(
        text="PATHOGENIC",
        description="pathogenic_for_condition",
        meaning=GENO["0000840"])
    LIKELY_PATHOGENIC = PermissibleValue(
        text="LIKELY_PATHOGENIC",
        description="likely_pathogenic_for_condition",
        meaning=GENO["0000841"])
    BENIGN = PermissibleValue(
        text="BENIGN",
        description="benign_for_condition",
        meaning=GENO["0000843"])
    LIKELY_BENIGN = PermissibleValue(
        text="LIKELY_BENIGN",
        description="likely_benign_for_condition",
        meaning=GENO["0000844"])
    UNCERTAIN_SIGNIFICANCE = PermissibleValue(
        text="UNCERTAIN_SIGNIFICANCE",
        description="has_uncertain_significance_for_condition",
        meaning=GENO["0000845"])

    _defn = EnumDefinition(
        name="ClinicalSignificanceEnum",
        description="The clinical significance of a variant for a condition (ACMG guidelines)",
    )

class ModifierEnum(EnumDefinitionImpl):
    """
    Qualifiers for direction, intensity, or pathological state of a descriptor
    """
    INCREASED = PermissibleValue(
        text="INCREASED",
        description="Upregulated, hyperactive, elevated, or excessive")
    DECREASED = PermissibleValue(
        text="DECREASED",
        description="Downregulated, hypoactive, reduced, or deficient")
    ABNORMAL = PermissibleValue(
        text="ABNORMAL",
        description="Qualitatively abnormal (e.g., misfolding, mislocalization, malformed)")
    DYSREGULATED = PermissibleValue(
        text="DYSREGULATED",
        description="Regulation is impaired (may be increased or decreased)")
    ABSENT = PermissibleValue(
        text="ABSENT",
        description="Not occurring or not present")

    _defn = EnumDefinition(
        name="ModifierEnum",
        description="Qualifiers for direction, intensity, or pathological state of a descriptor",
    )

class PenetranceEnum(EnumDefinitionImpl):
    """
    Penetrance classification for inheritance
    """
    COMPLETE = PermissibleValue(
        text="COMPLETE",
        description="Complete penetrance")
    INCOMPLETE = PermissibleValue(
        text="INCOMPLETE",
        description="Incomplete or partial penetrance")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="Unknown or not specified")

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
        description="Variable expressivity")
    CONSISTENT = PermissibleValue(
        text="CONSISTENT",
        description="Consistent or uniform expressivity")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="Unknown or not specified")

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
        description="Left side of the body")
    RIGHT = PermissibleValue(
        text="RIGHT",
        description="Right side of the body")
    BILATERAL = PermissibleValue(
        text="BILATERAL",
        description="Both sides of the body")

    _defn = EnumDefinition(
        name="LateralityEnum",
        description="Laterality qualifier for anatomical structures or procedures",
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
    A term representing a medical action or treatment (from MAXO)
    """
    _defn = EnumDefinition(
        name="TreatmentActionTerm",
        description="A term representing a medical action or treatment (from MAXO)",
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
    A histopathologic finding term from NCIT. Includes morphologic findings, architectural patterns, growth patterns,
    cellular features, and grading. Rooted at NCIT:C35867 (Morphologic Finding) and NCIT:C18000 (Histologic Grade).
    """
    _defn = EnumDefinition(
        name="HistopathologyFindingTerm",
        description="""A histopathologic finding term from NCIT. Includes morphologic findings, architectural patterns, growth patterns, cellular features, and grading. Rooted at NCIT:C35867 (Morphologic Finding) and NCIT:C18000 (Histologic Grade).""",
    )

class DiseaseTerm(EnumDefinitionImpl):
    """
    A disease or medical condition
    """
    _defn = EnumDefinition(
        name="DiseaseTerm",
        description="A disease or medical condition",
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

    _defn = EnumDefinition(
        name="DatasetTypeEnum",
        description="Type of dataset or data resource",
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

    _defn = EnumDefinition(
        name="ComputationalModelTypeEnum",
        description="Type of computational or in-silico model",
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
    Traditional internal medicine chapter groupings for disease classification. Based on Harrison's Principles of
    Internal Medicine organization. Sub-chapters use is_a to indicate parent category.
    """
    cardiomyopathy = PermissibleValue(
        text="cardiomyopathy",
        title="Diseases of heart muscle (dilated, hypertrophic, restrictive)",
        description="Primary diseases of the myocardium affecting systolic or diastolic function.",
        meaning=MONDO["0004994"])
    anemia = PermissibleValue(
        text="anemia",
        title="Red blood cell disorders",
        description="Reduced red cell mass or hemoglobin due to production defects, blood loss, or hemolysis.",
        meaning=MONDO["0002280"])
    cancer = PermissibleValue(
        text="cancer",
        title="Neoplastic diseases and cancer",
        description="Neoplastic diseases characterized by uncontrolled cell proliferation and invasion.",
        meaning=MONDO["0004992"])
    epilepsy = PermissibleValue(
        text="epilepsy",
        title="Seizure disorders",
        description="Recurrent unprovoked seizures from abnormal neuronal activity.",
        meaning=MONDO["0005027"])

    _defn = EnumDefinition(
        name="HarrisonsChapterEnum",
        description="""Traditional internal medicine chapter groupings for disease classification. Based on Harrison's Principles of Internal Medicine organization. Sub-chapters use is_a to indicate parent category.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "cardiovascular disorder",
            PermissibleValue(
                text="cardiovascular disorder",
                title="Diseases of the heart and blood vessels",
                description="""Heart and vascular diseases, including ischemic, structural, rhythm, and vascular conditions.""",
                meaning=MONDO["0004995"]))
        setattr(cls, "coronary artery disorder",
            PermissibleValue(
                text="coronary artery disorder",
                title="Ischemic heart disease, myocardial infarction, angina",
                description="""Ischemic heart disease due to coronary artery pathology; includes myocardial infarction and angina.""",
                meaning=MONDO["0005010"]))
        setattr(cls, "cardiac rhythm disease",
            PermissibleValue(
                text="cardiac rhythm disease",
                title="Arrhythmias, conduction disorders",
                description="Electrical conduction or rhythm disorders causing arrhythmias or heart block.",
                meaning=MONDO["0007263"]))
        setattr(cls, "valvular heart disease",
            PermissibleValue(
                text="valvular heart disease",
                title="Diseases of heart valves (stenosis, regurgitation)",
                description="""Structural or functional valve disease (stenosis or regurgitation) affecting cardiac hemodynamics.""",
                meaning=MONDO["0002869"]))
        setattr(cls, "vascular disease",
            PermissibleValue(
                text="vascular disease",
                title="Diseases of arteries and veins (aneurysm, PAD, DVT)",
                description="""Arterial or venous disorders such as aneurysm, peripheral artery disease, or thrombosis.""",
                meaning=MONDO["0005385"]))
        setattr(cls, "respiratory system disorder",
            PermissibleValue(
                text="respiratory system disorder",
                title="Diseases of the lungs and airways",
                description="""Diseases of airways, lung parenchyma, and pleura that impair ventilation or gas exchange.""",
                meaning=MONDO["0005087"]))
        setattr(cls, "obstructive lung disease",
            PermissibleValue(
                text="obstructive lung disease",
                title="COPD, asthma, bronchiectasis",
                description="Airflow limitation from airway narrowing or collapse, including COPD and asthma.",
                meaning=MONDO["0002267"]))
        setattr(cls, "interstitial lung disease",
            PermissibleValue(
                text="interstitial lung disease",
                title="Pulmonary fibrosis, sarcoidosis",
                description="""Diffuse parenchymal lung disorders with inflammation or fibrosis that reduce gas exchange.""",
                meaning=MONDO["0015925"]))
        setattr(cls, "pulmonary vascular disease",
            PermissibleValue(
                text="pulmonary vascular disease",
                title="Pulmonary hypertension, pulmonary embolism",
                description="Pulmonary arterial or venous vascular disorders, including hypertension and embolism."))
        setattr(cls, "digestive system disorder",
            PermissibleValue(
                text="digestive system disorder",
                title="Diseases of the digestive tract and accessory organs",
                description="""Diseases of the gastrointestinal tract and accessory organs affecting digestion or absorption.""",
                meaning=MONDO["0004335"]))
        setattr(cls, "inflammatory bowel disease",
            PermissibleValue(
                text="inflammatory bowel disease",
                title="Crohn's disease, ulcerative colitis",
                description="""Chronic immune-mediated intestinal inflammation, typically Crohn disease or ulcerative colitis.""",
                meaning=MONDO["0005265"]))
        setattr(cls, "peptic disorder",
            PermissibleValue(
                text="peptic disorder",
                title="Peptic ulcer, GERD, gastritis",
                description="""Acid-related disorders of the esophagus, stomach, or duodenum such as GERD and peptic ulcer disease.""",
                meaning=MONDO["0004247"]))
        setattr(cls, "liver disorder",
            PermissibleValue(
                text="liver disorder",
                title="Diseases of the liver, gallbladder, and biliary system",
                description="Hepatobiliary diseases involving liver parenchyma, bile ducts, or gallbladder.",
                meaning=MONDO["0005154"]))
        setattr(cls, "kidney disorder",
            PermissibleValue(
                text="kidney disorder",
                title="Diseases of the kidneys and urinary system",
                description="""Renal and urinary tract diseases affecting filtration, electrolyte balance, or urine flow.""",
                meaning=MONDO["0005240"]))
        setattr(cls, "glomerular disease",
            PermissibleValue(
                text="glomerular disease",
                title="Glomerulonephritis, nephrotic syndrome",
                description="""Diseases of the glomerulus causing hematuria, proteinuria, or nephrotic/nephritic syndromes.""",
                meaning=MONDO["0019722"]))
        setattr(cls, "hematologic disorder",
            PermissibleValue(
                text="hematologic disorder",
                title="Diseases of blood and blood-forming organs",
                description="Disorders of blood cells, bone marrow, and hemostasis.",
                meaning=MONDO["0005570"]))
        setattr(cls, "coagulation disorder",
            PermissibleValue(
                text="coagulation disorder",
                title="Bleeding and thrombotic disorders",
                description="""Bleeding or thrombotic disorders from clotting factor, platelet, or regulatory defects.""",
                meaning=MONDO["0001531"]))
        setattr(cls, "hematologic malignancy",
            PermissibleValue(
                text="hematologic malignancy",
                title="Leukemia, lymphoma, myeloma",
                description="Cancers of blood, bone marrow, and lymphoid tissues such as leukemia or lymphoma.",
                meaning=MONDO["0002334"]))
        setattr(cls, "solid tumor",
            PermissibleValue(
                text="solid tumor",
                title="Carcinomas, sarcomas, other solid neoplasms",
                description="Non-hematologic neoplasms arising in organs or soft tissues."))
        setattr(cls, "infectious disease",
            PermissibleValue(
                text="infectious disease",
                title="Diseases caused by pathogenic microorganisms",
                description="Illness caused by pathogenic organisms with host invasion and immune response.",
                meaning=MONDO["0005550"]))
        setattr(cls, "bacterial infectious disease",
            PermissibleValue(
                text="bacterial infectious disease",
                title="Infections caused by bacteria",
                description="""Infections caused by bacteria, including community and healthcare-associated pathogens.""",
                meaning=MONDO["0005113"]))
        setattr(cls, "viral infectious disease",
            PermissibleValue(
                text="viral infectious disease",
                title="Infections caused by viruses",
                description="Infections caused by viruses affecting any organ system.",
                meaning=MONDO["0005108"]))
        setattr(cls, "fungal infectious disease",
            PermissibleValue(
                text="fungal infectious disease",
                title="Infections caused by fungi",
                description="Mycoses ranging from superficial to invasive systemic infections.",
                meaning=MONDO["0002041"]))
        setattr(cls, "parasitic infectious disease",
            PermissibleValue(
                text="parasitic infectious disease",
                title="Infections caused by parasites (protozoa, helminths)",
                description="Protozoal or helminth infections, often vector-borne or food/water transmitted.",
                meaning=MONDO["0005135"]))
        setattr(cls, "mycobacterial infection",
            PermissibleValue(
                text="mycobacterial infection",
                title="Tuberculosis, NTM, leprosy",
                description="""Infections due to Mycobacterium species, including tuberculosis and non-tuberculous mycobacteria.""",
                meaning=MONDO["0020590"]))
        setattr(cls, "immune system disorder",
            PermissibleValue(
                text="immune system disorder",
                title="Diseases of the immune system including autoimmunity",
                description="""Immune dysregulation disorders including autoimmunity, immunodeficiency, or hypersensitivity.""",
                meaning=MONDO["0005046"]))
        setattr(cls, "autoimmune disease",
            PermissibleValue(
                text="autoimmune disease",
                title="Diseases caused by immune attack on self",
                description="Immune-mediated tissue damage due to loss of self-tolerance.",
                meaning=MONDO["0007179"]))
        setattr(cls, "allergic disease",
            PermissibleValue(
                text="allergic disease",
                title="Hypersensitivity disorders, anaphylaxis",
                description="Hypersensitivity disorders including atopy, allergic asthma, and anaphylaxis.",
                meaning=MONDO["0005271"]))
        setattr(cls, "endocrine system disorder",
            PermissibleValue(
                text="endocrine system disorder",
                title="Diseases of hormonal and metabolic systems",
                description="Hormonal and metabolic gland disorders affecting systemic homeostasis.",
                meaning=MONDO["0005151"]))
        setattr(cls, "diabetes mellitus",
            PermissibleValue(
                text="diabetes mellitus",
                title="Type 1, type 2, and other forms of diabetes",
                description="Disorders of glucose regulation due to insulin deficiency and/or insulin resistance.",
                meaning=MONDO["0005015"]))
        setattr(cls, "thyroid disorder",
            PermissibleValue(
                text="thyroid disorder",
                title="Hyper/hypothyroidism, thyroid nodules, thyroid cancer",
                description="Thyroid gland dysfunction or structural disease altering metabolic control.",
                meaning=MONDO["0003240"]))
        setattr(cls, "adrenal disorder",
            PermissibleValue(
                text="adrenal disorder",
                title="Cushing's, Addison's, pheochromocytoma",
                description="Adrenal cortex or medulla disorders causing hormone excess or deficiency.",
                meaning=MONDO["0005495"]))
        setattr(cls, "nervous system disorder",
            PermissibleValue(
                text="nervous system disorder",
                title="Diseases of the central and peripheral nervous system",
                description="""Central or peripheral nervous system diseases affecting cognition, sensation, or movement.""",
                meaning=MONDO["0005071"]))
        setattr(cls, "cerebrovascular disorder",
            PermissibleValue(
                text="cerebrovascular disorder",
                title="Stroke, TIA, vascular dementia",
                description="Brain ischemia or hemorrhage due to vascular disease, including stroke and TIA.",
                meaning=MONDO["0011057"]))
        setattr(cls, "neurodegenerative disease",
            PermissibleValue(
                text="neurodegenerative disease",
                title="Alzheimer's, Parkinson's, ALS, Huntington's",
                description="Progressive neuronal loss leading to cognitive or motor decline.",
                meaning=MONDO["0005559"]))
        setattr(cls, "demyelinating disease",
            PermissibleValue(
                text="demyelinating disease",
                title="Multiple sclerosis, NMO, ADEM",
                description="Disorders with loss of myelin in the nervous system, often immune-mediated.",
                meaning=MONDO["0002562"]))
        setattr(cls, "neuromuscular disease",
            PermissibleValue(
                text="neuromuscular disease",
                title="Myopathies, neuropathies, NMJ disorders",
                description="Diseases of peripheral nerve, neuromuscular junction, or muscle leading to weakness.",
                meaning=MONDO["0019056"]))
        setattr(cls, "movement disorder",
            PermissibleValue(
                text="movement disorder",
                title="Parkinsonism, dystonia, chorea, ataxia",
                description="Motor control disorders causing tremor, rigidity, dystonia, chorea, or ataxia.",
                meaning=MONDO["0005395"]))
        setattr(cls, "musculoskeletal system disorder",
            PermissibleValue(
                text="musculoskeletal system disorder",
                title="Diseases of joints, connective tissue, and musculoskeletal system",
                description="Diseases of joints, bones, muscles, or connective tissue.",
                meaning=MONDO["0002081"]))
        setattr(cls, "inflammatory arthritis",
            PermissibleValue(
                text="inflammatory arthritis",
                title="Rheumatoid arthritis, spondyloarthritis, gout",
                description="Inflammatory joint disorders with synovitis, such as RA or spondyloarthropathies."))
        setattr(cls, "connective tissue disease",
            PermissibleValue(
                text="connective tissue disease",
                title="SLE, scleroderma, Sjogren's, vasculitis",
                description="""Systemic autoimmune connective tissue disorders affecting skin, joints, vessels, and organs.""",
                meaning=MONDO["0003900"]))
        setattr(cls, "skin disorder",
            PermissibleValue(
                text="skin disorder",
                title="Diseases of the skin and appendages",
                description="Diseases of the skin, hair, nails, and related appendages.",
                meaning=MONDO["0005093"]))
        setattr(cls, "psychiatric disorder",
            PermissibleValue(
                text="psychiatric disorder",
                title="Mental and behavioral disorders",
                description="Mental and behavioral disorders affecting mood, thought, or behavior.",
                meaning=MONDO["0002025"]))
        setattr(cls, "hereditary disease",
            PermissibleValue(
                text="hereditary disease",
                title="Inherited diseases and birth defects",
                description="Genetic or congenital disorders due to inherited variants or developmental anomalies.",
                meaning=MONDO["0003847"]))

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

# Slots
class slots:
    pass

slots.name = Slot(uri=DISMECH.name, name="name", curie=DISMECH.curie('name'),
                   model_uri=DISMECH.name, domain=None, range=URIRef)

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

slots.therapeutic_agent = Slot(uri=DISMECH.therapeutic_agent, name="therapeutic_agent", curie=DISMECH.curie('therapeutic_agent'),
                   model_uri=DISMECH.therapeutic_agent, domain=None, range=Optional[Union[Union[dict, ChemicalEntityDescriptor], list[Union[dict, ChemicalEntityDescriptor]]]])

slots.qualifiers = Slot(uri=DISMECH.qualifiers, name="qualifiers", curie=DISMECH.curie('qualifiers'),
                   model_uri=DISMECH.qualifiers, domain=None, range=Optional[Union[Union[dict, Qualifier], list[Union[dict, Qualifier]]]])

slots.predicate = Slot(uri=DISMECH.predicate, name="predicate", curie=DISMECH.curie('predicate'),
                   model_uri=DISMECH.predicate, domain=None, range=Optional[Union[dict, Descriptor]])

slots.value = Slot(uri=DISMECH.value, name="value", curie=DISMECH.curie('value'),
                   model_uri=DISMECH.value, domain=None, range=Optional[Union[dict, Descriptor]])

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

slots.evidence_source = Slot(uri=DISMECH.evidence_source, name="evidence_source", curie=DISMECH.curie('evidence_source'),
                   model_uri=DISMECH.evidence_source, domain=None, range=Optional[Union[str, "EvidenceSourceEnum"]])

slots.snippet = Slot(uri=DISMECH.snippet, name="snippet", curie=DISMECH.curie('snippet'),
                   model_uri=DISMECH.snippet, domain=None, range=Optional[str])

slots.explanation = Slot(uri=DISMECH.explanation, name="explanation", curie=DISMECH.curie('explanation'),
                   model_uri=DISMECH.explanation, domain=None, range=Optional[str])

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

slots.subtype = Slot(uri=DISMECH.subtype, name="subtype", curie=DISMECH.curie('subtype'),
                   model_uri=DISMECH.subtype, domain=None, range=Optional[str])

slots.population = Slot(uri=DISMECH.population, name="population", curie=DISMECH.curie('population'),
                   model_uri=DISMECH.population, domain=None, range=Optional[str])

slots.percentage = Slot(uri=DISMECH.percentage, name="percentage", curie=DISMECH.curie('percentage'),
                   model_uri=DISMECH.percentage, domain=None, range=Optional[Union[dict, Any]])

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

slots.epidemiology = Slot(uri=DISMECH.epidemiology, name="epidemiology", curie=DISMECH.curie('epidemiology'),
                   model_uri=DISMECH.epidemiology, domain=None, range=Optional[Union[dict[Union[str, EpidemiologyInfoName], Union[dict, EpidemiologyInfo]], list[Union[dict, EpidemiologyInfo]]]])

slots.examples = Slot(uri=DISMECH.examples, name="examples", curie=DISMECH.curie('examples'),
                   model_uri=DISMECH.examples, domain=None, range=Optional[Union[str, list[str]]])

slots.role = Slot(uri=DISMECH.role, name="role", curie=DISMECH.curie('role'),
                   model_uri=DISMECH.role, domain=None, range=Optional[str])

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

slots.regimen_term = Slot(uri=DISMECH.regimen_term, name="regimen_term", curie=DISMECH.curie('regimen_term'),
                   model_uri=DISMECH.regimen_term, domain=None, range=Optional[Union[dict, RegimenDescriptor]])

slots.biomarker_term = Slot(uri=DISMECH.biomarker_term, name="biomarker_term", curie=DISMECH.curie('biomarker_term'),
                   model_uri=DISMECH.biomarker_term, domain=None, range=Optional[Union[dict, BiomarkerDescriptor]])

slots.finding_term = Slot(uri=DISMECH.finding_term, name="finding_term", curie=DISMECH.curie('finding_term'),
                   model_uri=DISMECH.finding_term, domain=None, range=Optional[Union[dict, HistopathologyFindingDescriptor]])

slots.diagnosis_term = Slot(uri=DISMECH.diagnosis_term, name="diagnosis_term", curie=DISMECH.curie('diagnosis_term'),
                   model_uri=DISMECH.diagnosis_term, domain=None, range=Optional[Union[dict, TreatmentDescriptor]])

slots.subtype_term = Slot(uri=DISMECH.subtype_term, name="subtype_term", curie=DISMECH.curie('subtype_term'),
                   model_uri=DISMECH.subtype_term, domain=None, range=Optional[Union[dict, DiseaseDescriptor]])

slots.infectious_agent_term = Slot(uri=DISMECH.infectious_agent_term, name="infectious_agent_term", curie=DISMECH.curie('infectious_agent_term'),
                   model_uri=DISMECH.infectious_agent_term, domain=None, range=Optional[Union[dict, OrganismDescriptor]])

slots.exposure_term = Slot(uri=DISMECH.exposure_term, name="exposure_term", curie=DISMECH.curie('exposure_term'),
                   model_uri=DISMECH.exposure_term, domain=None, range=Optional[Union[dict, ExposureDescriptor]])

slots.life_cycle_stage_term = Slot(uri=DISMECH.life_cycle_stage_term, name="life_cycle_stage_term", curie=DISMECH.curie('life_cycle_stage_term'),
                   model_uri=DISMECH.life_cycle_stage_term, domain=None, range=Optional[Union[dict, LifeCycleStageDescriptor]])

slots.environment_context = Slot(uri=DISMECH.environment_context, name="environment_context", curie=DISMECH.curie('environment_context'),
                   model_uri=DISMECH.environment_context, domain=None, range=Optional[Union[dict, EnvironmentDescriptor]])

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
                   model_uri=DISMECH.severity, domain=None, range=Optional[str])

slots.presence = Slot(uri=DISMECH.presence, name="presence", curie=DISMECH.curie('presence'),
                   model_uri=DISMECH.presence, domain=None, range=Optional[str])

slots.specificity = Slot(uri=DISMECH.specificity, name="specificity", curie=DISMECH.curie('specificity'),
                   model_uri=DISMECH.specificity, domain=None, range=Optional[str])

slots.synonyms = Slot(uri=DISMECH.synonyms, name="synonyms", curie=DISMECH.curie('synonyms'),
                   model_uri=DISMECH.synonyms, domain=None, range=Optional[Union[str, list[str]]])

slots.association = Slot(uri=DISMECH.association, name="association", curie=DISMECH.curie('association'),
                   model_uri=DISMECH.association, domain=None, range=Optional[str])

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

slots.unit = Slot(uri=DISMECH.unit, name="unit", curie=DISMECH.curie('unit'),
                   model_uri=DISMECH.unit, domain=None, range=Optional[str])

slots.function = Slot(uri=DISMECH.function, name="function", curie=DISMECH.curie('function'),
                   model_uri=DISMECH.function, domain=None, range=Optional[str])

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

slots.target_phenotypes = Slot(uri=DISMECH.target_phenotypes, name="target_phenotypes", curie=DISMECH.curie('target_phenotypes'),
                   model_uri=DISMECH.target_phenotypes, domain=None, range=Optional[Union[Union[dict, PhenotypeDescriptor], list[Union[dict, PhenotypeDescriptor]]]])

slots.target_mechanisms = Slot(uri=DISMECH.target_mechanisms, name="target_mechanisms", curie=DISMECH.curie('target_mechanisms'),
                   model_uri=DISMECH.target_mechanisms, domain=None, range=Optional[Union[Union[dict, TreatmentMechanismTarget], list[Union[dict, TreatmentMechanismTarget]]]])

slots.treatment_effect = Slot(uri=DISMECH.treatment_effect, name="treatment_effect", curie=DISMECH.curie('treatment_effect'),
                   model_uri=DISMECH.treatment_effect, domain=None, range=Optional[Union[str, "TreatmentEffectEnum"]])

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

slots.conditions = Slot(uri=DISMECH.conditions, name="conditions", curie=DISMECH.curie('conditions'),
                   model_uri=DISMECH.conditions, domain=None, range=Optional[Union[str, list[str]]])

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

slots.classification_value = Slot(uri=DISMECH.classification_value, name="classification_value", curie=DISMECH.curie('classification_value'),
                   model_uri=DISMECH.classification_value, domain=None, range=Optional[str])

slots.icd10cm_mappings = Slot(uri=DISMECH.icd10cm_mappings, name="icd10cm_mappings", curie=DISMECH.curie('icd10cm_mappings'),
                   model_uri=DISMECH.icd10cm_mappings, domain=None, range=Optional[Union[Union[dict, ICD10CMMapping], list[Union[dict, ICD10CMMapping]]]])

slots.icd11f_mappings = Slot(uri=DISMECH.icd11f_mappings, name="icd11f_mappings", curie=DISMECH.curie('icd11f_mappings'),
                   model_uri=DISMECH.icd11f_mappings, domain=None, range=Optional[Union[Union[dict, ICD11FMapping], list[Union[dict, ICD11FMapping]]]])

slots.mondo_mappings = Slot(uri=DISMECH.mondo_mappings, name="mondo_mappings", curie=DISMECH.curie('mondo_mappings'),
                   model_uri=DISMECH.mondo_mappings, domain=None, range=Optional[Union[Union[dict, MondoMapping], list[Union[dict, MondoMapping]]]])

slots.mapping_predicate = Slot(uri=DISMECH.mapping_predicate, name="mapping_predicate", curie=DISMECH.curie('mapping_predicate'),
                   model_uri=DISMECH.mapping_predicate, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.mapping_source = Slot(uri=DISMECH.mapping_source, name="mapping_source", curie=DISMECH.curie('mapping_source'),
                   model_uri=DISMECH.mapping_source, domain=None, range=Optional[str])

slots.mapping_justification = Slot(uri=DISMECH.mapping_justification, name="mapping_justification", curie=DISMECH.curie('mapping_justification'),
                   model_uri=DISMECH.mapping_justification, domain=None, range=Optional[str])

slots.definition_type = Slot(uri=DISMECH.definition_type, name="definition_type", curie=DISMECH.curie('definition_type'),
                   model_uri=DISMECH.definition_type, domain=None, range=Optional[Union[str, "DefinitionTypeEnum"]])

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
                   model_uri=DISMECH.limited_precision, domain=None, range=Optional[bool])

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

slots.zygosity = Slot(uri=DISMECH.zygosity, name="zygosity", curie=DISMECH.curie('zygosity'),
                   model_uri=DISMECH.zygosity, domain=None, range=Optional[Union[str, "ZygosityEnum"]])

slots.functional_impact = Slot(uri=DISMECH.functional_impact, name="functional_impact", curie=DISMECH.curie('functional_impact'),
                   model_uri=DISMECH.functional_impact, domain=None, range=Optional[str])

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

slots.CurationEvent_curation_timestamp = Slot(uri=DISMECH.curation_timestamp, name="CurationEvent_curation_timestamp", curie=DISMECH.curie('curation_timestamp'),
                   model_uri=DISMECH.CurationEvent_curation_timestamp, domain=CurationEvent, range=Union[str, XSDDateTime])

slots.Descriptor_description = Slot(uri=DISMECH.description, name="Descriptor_description", curie=DISMECH.curie('description'),
                   model_uri=DISMECH.Descriptor_description, domain=Descriptor, range=Optional[str])

slots.CellTypeDescriptor_term = Slot(uri=DISMECH.term, name="CellTypeDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.CellTypeDescriptor_term, domain=CellTypeDescriptor, range=Optional[Union[dict, Term]])

slots.BiologicalProcessDescriptor_term = Slot(uri=DISMECH.term, name="BiologicalProcessDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.BiologicalProcessDescriptor_term, domain=BiologicalProcessDescriptor, range=Optional[Union[dict, Term]])

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

slots.BiomarkerDescriptor_term = Slot(uri=DISMECH.term, name="BiomarkerDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.BiomarkerDescriptor_term, domain=BiomarkerDescriptor, range=Optional[Union[dict, Term]])

slots.GeneProductDescriptor_term = Slot(uri=DISMECH.term, name="GeneProductDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.GeneProductDescriptor_term, domain=GeneProductDescriptor, range=Optional[Union[dict, Term]])

slots.HistopathologyFindingDescriptor_term = Slot(uri=DISMECH.term, name="HistopathologyFindingDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.HistopathologyFindingDescriptor_term, domain=HistopathologyFindingDescriptor, range=Optional[Union[dict, Term]])

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

slots.RegimenDescriptor_term = Slot(uri=DISMECH.term, name="RegimenDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.RegimenDescriptor_term, domain=RegimenDescriptor, range=Optional[Union[dict, Term]])

slots.ExposureDescriptor_term = Slot(uri=DISMECH.term, name="ExposureDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.ExposureDescriptor_term, domain=ExposureDescriptor, range=Optional[Union[dict, Term]])

slots.EnvironmentDescriptor_term = Slot(uri=DISMECH.term, name="EnvironmentDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.EnvironmentDescriptor_term, domain=EnvironmentDescriptor, range=Optional[Union[dict, Term]])

slots.OrganismDescriptor_term = Slot(uri=DISMECH.term, name="OrganismDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.OrganismDescriptor_term, domain=OrganismDescriptor, range=Optional[Union[dict, Term]])

slots.PhenotypeContext_sex = Slot(uri=DISMECH.sex, name="PhenotypeContext_sex", curie=DISMECH.curie('sex'),
                   model_uri=DISMECH.PhenotypeContext_sex, domain=PhenotypeContext, range=Optional[Union[str, "SexEnum"]])

slots.PhenotypeContext_evidence = Slot(uri=DISMECH.evidence, name="PhenotypeContext_evidence", curie=DISMECH.curie('evidence'),
                   model_uri=DISMECH.PhenotypeContext_evidence, domain=PhenotypeContext, range=Optional[Union[Union[dict, "EvidenceItem"], list[Union[dict, "EvidenceItem"]]]])

slots.Dataset_description = Slot(uri=DISMECH.description, name="Dataset_description", curie=DISMECH.curie('description'),
                   model_uri=DISMECH.Dataset_description, domain=Dataset, range=Optional[str])

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

slots.PublicationReference_reference = Slot(uri=DISMECH.reference, name="PublicationReference_reference", curie=DISMECH.curie('reference'),
                   model_uri=DISMECH.PublicationReference_reference, domain=PublicationReference, range=Union[str, PublicationReferenceReference])

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

slots.Disease_name = Slot(uri=DISMECH.name, name="Disease_name", curie=DISMECH.curie('name'),
                   model_uri=DISMECH.Disease_name, domain=Disease, range=Union[str, DiseaseName])

slots.Disease_creation_date = Slot(uri=DISMECH.creation_date, name="Disease_creation_date", curie=DISMECH.curie('creation_date'),
                   model_uri=DISMECH.Disease_creation_date, domain=Disease, range=Optional[str],
                   pattern=re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+\-]\d{2}:\d{2})$'))

slots.Disease_updated_date = Slot(uri=DISMECH.updated_date, name="Disease_updated_date", curie=DISMECH.curie('updated_date'),
                   model_uri=DISMECH.Disease_updated_date, domain=Disease, range=Optional[str],
                   pattern=re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+\-]\d{2}:\d{2})$'))

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

slots.Definition_name = Slot(uri=DISMECH.name, name="Definition_name", curie=DISMECH.curie('name'),
                   model_uri=DISMECH.Definition_name, domain=Definition, range=Union[str, DefinitionName])

slots.Definition_definition_type = Slot(uri=DISMECH.definition_type, name="Definition_definition_type", curie=DISMECH.curie('definition_type'),
                   model_uri=DISMECH.Definition_definition_type, domain=Definition, range=Union[str, "DefinitionTypeEnum"])

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
