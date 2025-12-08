# Auto generated from dismech.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-12-05T19:06:24
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

from linkml_runtime.linkml_model.types import Boolean, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE

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
HP = CurieNamespace('HP', 'http://purl.obolibrary.org/obo/HP_')
MONDO = CurieNamespace('MONDO', 'http://purl.obolibrary.org/obo/MONDO_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
PMID = CurieNamespace('PMID', 'http://www.ncbi.nlm.nih.gov/pubmed/')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
XCO = CurieNamespace('XCO', 'http://purl.obolibrary.org/obo/XCO_')
DISMECH = CurieNamespace('dismech', 'https://w3id.org/monarch-initiative/dismech/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = DISMECH


# Types
class PMID(String):
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "PMID"
    type_model_uri = DISMECH.PMID


class FrequencyQuantity(String):
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "FrequencyQuantity"
    type_model_uri = DISMECH.FrequencyQuantity


# Class references
class TermId(URIorCURIE):
    pass


class SubtypeName(extended_str):
    pass


class PublicationReferenceReference(PMID):
    pass


class EpidemiologyInfoName(extended_str):
    pass


class PathophysiologyName(extended_str):
    pass


class PhenotypeName(extended_str):
    pass


class BiochemicalName(extended_str):
    pass


class GeneticName(extended_str):
    pass


class EnvironmentalName(extended_str):
    pass


class DiseaseName(extended_str):
    pass


class StageName(extended_str):
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


Any = Any

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
    binding, and optional modifier.
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
class Subtype(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Subtype"]
    class_class_curie: ClassVar[str] = "dismech:Subtype"
    class_name: ClassVar[str] = "Subtype"
    class_model_uri: ClassVar[URIRef] = DISMECH.Subtype

    name: Union[str, SubtypeName] = None
    description: Optional[str] = None
    evidence: Optional[Union[Union[dict, "EvidenceItem"], list[Union[dict, "EvidenceItem"]]]] = empty_list()
    review_notes: Optional[str] = None
    locations: Optional[Union[Union[dict, AnatomicalEntityDescriptor], list[Union[dict, AnatomicalEntityDescriptor]]]] = empty_list()
    geography: Optional[Union[Union[str, "GeographyTerm"], list[Union[str, "GeographyTerm"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, SubtypeName):
            self.name = SubtypeName(self.name)

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

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EvidenceItem(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["EvidenceItem"]
    class_class_curie: ClassVar[str] = "dismech:EvidenceItem"
    class_name: ClassVar[str] = "EvidenceItem"
    class_model_uri: ClassVar[URIRef] = DISMECH.EvidenceItem

    reference: Optional[Union[str, PMID]] = None
    supports: Optional[Union[str, "EvidenceItemSupportEnum"]] = None
    snippet: Optional[str] = None
    explanation: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.reference is not None and not isinstance(self.reference, PMID):
            self.reference = PMID(self.reference)

        if self.supports is not None and not isinstance(self.supports, EvidenceItemSupportEnum):
            self.supports = EvidenceItemSupportEnum(self.supports)

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
    A key finding or claim extracted from a publication
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Finding"]
    class_class_curie: ClassVar[str] = "dismech:Finding"
    class_name: ClassVar[str] = "Finding"
    class_model_uri: ClassVar[URIRef] = DISMECH.Finding

    statement: str = None
    supporting_text: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.statement):
            self.MissingRequiredField("statement")
        if not isinstance(self.statement, str):
            self.statement = str(self.statement)

        if self.supporting_text is not None and not isinstance(self.supporting_text, str):
            self.supporting_text = str(self.supporting_text)

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
    chemical_entities: Optional[Union[Union[dict, ChemicalEntityDescriptor], list[Union[dict, ChemicalEntityDescriptor]]]] = empty_list()
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

        if not isinstance(self.chemical_entities, list):
            self.chemical_entities = [self.chemical_entities] if self.chemical_entities is not None else []
        self.chemical_entities = [v if isinstance(v, ChemicalEntityDescriptor) else ChemicalEntityDescriptor(**as_dict(v)) for v in self.chemical_entities]

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

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Biochemical(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Biochemical"]
    class_class_curie: ClassVar[str] = "dismech:Biochemical"
    class_name: ClassVar[str] = "Biochemical"
    class_model_uri: ClassVar[URIRef] = DISMECH.Biochemical

    name: Union[str, BiochemicalName] = None
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
class Genetic(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DISMECH["Genetic"]
    class_class_curie: ClassVar[str] = "dismech:Genetic"
    class_name: ClassVar[str] = "Genetic"
    class_model_uri: ClassVar[URIRef] = DISMECH.Genetic

    name: Union[str, GeneticName] = None
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
    description: Optional[str] = None
    references: Optional[Union[dict[Union[str, PublicationReferenceReference], Union[dict, PublicationReference]], list[Union[dict, PublicationReference]]]] = empty_dict()
    category: Optional[str] = None
    parents: Optional[Union[str, list[str]]] = empty_list()
    has_subtypes: Optional[Union[dict[Union[str, SubtypeName], Union[dict, Subtype]], list[Union[dict, Subtype]]]] = empty_dict()
    prevalence: Optional[Union[Union[dict, Prevalence], list[Union[dict, Prevalence]]]] = empty_list()
    progression: Optional[Union[Union[dict, ProgressionInfo], list[Union[dict, ProgressionInfo]]]] = empty_list()
    pathophysiology: Optional[Union[dict[Union[str, PathophysiologyName], Union[dict, Pathophysiology]], list[Union[dict, Pathophysiology]]]] = empty_dict()
    phenotypes: Optional[Union[dict[Union[str, PhenotypeName], Union[dict, Phenotype]], list[Union[dict, Phenotype]]]] = empty_dict()
    biochemical: Optional[Union[dict[Union[str, BiochemicalName], Union[dict, Biochemical]], list[Union[dict, Biochemical]]]] = empty_dict()
    stages: Optional[Union[dict[Union[str, StageName], Union[dict, "Stage"]], list[Union[dict, "Stage"]]]] = empty_dict()
    genetic: Optional[Union[dict[Union[str, GeneticName], Union[dict, Genetic]], list[Union[dict, Genetic]]]] = empty_dict()
    variants: Optional[Union[dict[Union[str, VariantName], Union[dict, "Variant"]], list[Union[dict, "Variant"]]]] = empty_dict()
    environmental: Optional[Union[dict[Union[str, EnvironmentalName], Union[dict, Environmental]], list[Union[dict, Environmental]]]] = empty_dict()
    treatments: Optional[Union[dict[Union[str, TreatmentName], Union[dict, "Treatment"]], list[Union[dict, "Treatment"]]]] = empty_dict()
    categories: Optional[Union[str, list[str]]] = empty_list()
    infectious_agent: Optional[Union[dict[Union[str, InfectiousAgentName], Union[dict, "InfectiousAgent"]], list[Union[dict, "InfectiousAgent"]]]] = empty_dict()
    transmission: Optional[Union[dict[Union[str, TransmissionName], Union[dict, "Transmission"]], list[Union[dict, "Transmission"]]]] = empty_dict()
    modeling_considerations: Optional[Union[dict[Union[str, ModelingConsiderationName], Union[dict, "ModelingConsideration"]], list[Union[dict, "ModelingConsideration"]]]] = empty_dict()
    epidemiology: Optional[Union[dict[Union[str, EpidemiologyInfoName], Union[dict, EpidemiologyInfo]], list[Union[dict, EpidemiologyInfo]]]] = empty_dict()
    diagnosis: Optional[Union[dict[Union[str, DiagnosisName], Union[dict, "Diagnosis"]], list[Union[dict, "Diagnosis"]]]] = empty_dict()
    synonyms: Optional[Union[str, list[str]]] = empty_list()
    inheritance: Optional[Union[dict[Union[str, InheritanceName], Union[dict, "Inheritance"]], list[Union[dict, "Inheritance"]]]] = empty_dict()
    animal_models: Optional[Union[Union[dict, "AnimalModel"], list[Union[dict, "AnimalModel"]]]] = empty_list()
    notes: Optional[str] = None
    review_notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, DiseaseName):
            self.name = DiseaseName(self.name)

        if self.disease_term is not None and not isinstance(self.disease_term, DiseaseDescriptor):
            self.disease_term = DiseaseDescriptor(**as_dict(self.disease_term))

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

        self._normalize_inlined_as_list(slot_name="phenotypes", slot_type=Phenotype, key_name="name", keyed=True)

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

        self._normalize_inlined_as_list(slot_name="transmission", slot_type=Transmission, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="modeling_considerations", slot_type=ModelingConsideration, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="epidemiology", slot_type=EpidemiologyInfo, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="diagnosis", slot_type=Diagnosis, key_name="name", keyed=True)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        self._normalize_inlined_as_list(slot_name="inheritance", slot_type=Inheritance, key_name="name", keyed=True)

        if not isinstance(self.animal_models, list):
            self.animal_models = [self.animal_models] if self.animal_models is not None else []
        self.animal_models = [v if isinstance(v, AnimalModel) else AnimalModel(**as_dict(v)) for v in self.animal_models]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.review_notes is not None and not isinstance(self.review_notes, str):
            self.review_notes = str(self.review_notes)

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
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    description: Optional[str] = None
    has_subtypes: Optional[Union[dict[Union[str, SubtypeName], Union[dict, Subtype]], list[Union[dict, Subtype]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, InfectiousAgentName):
            self.name = InfectiousAgentName(self.name)

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
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, InheritanceName):
            self.name = InheritanceName(self.name)

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
    A term representing a phenotype
    """
    _defn = EnumDefinition(
        name="PhenotypeTerm",
        description="A term representing a phenotype",
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
    A gene
    """
    _defn = EnumDefinition(
        name="GeneTerm",
        description="A gene",
    )

class CellTypeTerm(EnumDefinitionImpl):
    """
    A cell type
    """
    _defn = EnumDefinition(
        name="CellTypeTerm",
        description="A cell type",
    )

class DiseaseTerm(EnumDefinitionImpl):
    """
    A disease or medical condition
    """
    _defn = EnumDefinition(
        name="DiseaseTerm",
        description="A disease or medical condition",
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
    A term representing an environmental context or setting (from ENVO)
    """
    _defn = EnumDefinition(
        name="EnvironmentTerm",
        description="A term representing an environmental context or setting (from ENVO)",
    )

# Slots
class slots:
    pass

slots.name = Slot(uri=DISMECH.name, name="name", curie=DISMECH.curie('name'),
                   model_uri=DISMECH.name, domain=None, range=URIRef)

slots.description = Slot(uri=DISMECH.description, name="description", curie=DISMECH.curie('description'),
                   model_uri=DISMECH.description, domain=None, range=Optional[str])

slots.preferred_term = Slot(uri=DISMECH.preferred_term, name="preferred_term", curie=DISMECH.curie('preferred_term'),
                   model_uri=DISMECH.preferred_term, domain=None, range=str)

slots.term = Slot(uri=DISMECH.term, name="term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.term, domain=None, range=Optional[Union[dict, Term]])

slots.modifier = Slot(uri=DISMECH.modifier, name="modifier", curie=DISMECH.curie('modifier'),
                   model_uri=DISMECH.modifier, domain=None, range=Optional[Union[str, "ModifierEnum"]])

slots.id = Slot(uri=DISMECH.id, name="id", curie=DISMECH.curie('id'),
                   model_uri=DISMECH.id, domain=None, range=URIRef)

slots.label = Slot(uri=DISMECH.label, name="label", curie=DISMECH.curie('label'),
                   model_uri=DISMECH.label, domain=None, range=Optional[str])

slots.evidence = Slot(uri=DISMECH.evidence, name="evidence", curie=DISMECH.curie('evidence'),
                   model_uri=DISMECH.evidence, domain=None, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.review_notes = Slot(uri=DISMECH.review_notes, name="review_notes", curie=DISMECH.curie('review_notes'),
                   model_uri=DISMECH.review_notes, domain=None, range=Optional[str])

slots.geography = Slot(uri=DISMECH.geography, name="geography", curie=DISMECH.curie('geography'),
                   model_uri=DISMECH.geography, domain=None, range=Optional[Union[Union[str, "GeographyTerm"], list[Union[str, "GeographyTerm"]]]])

slots.locations = Slot(uri=DISMECH.locations, name="locations", curie=DISMECH.curie('locations'),
                   model_uri=DISMECH.locations, domain=None, range=Optional[Union[Union[dict, AnatomicalEntityDescriptor], list[Union[dict, AnatomicalEntityDescriptor]]]])

slots.reference = Slot(uri=DISMECH.reference, name="reference", curie=DISMECH.curie('reference'),
                   model_uri=DISMECH.reference, domain=None, range=Optional[Union[str, PMID]])

slots.supports = Slot(uri=DISMECH.supports, name="supports", curie=DISMECH.curie('supports'),
                   model_uri=DISMECH.supports, domain=None, range=Optional[Union[str, "EvidenceItemSupportEnum"]])

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

slots.cellular_components = Slot(uri=DISMECH.cellular_components, name="cellular_components", curie=DISMECH.curie('cellular_components'),
                   model_uri=DISMECH.cellular_components, domain=None, range=Optional[Union[Union[dict, CellularComponentDescriptor], list[Union[dict, CellularComponentDescriptor]]]])

slots.chemical_entities = Slot(uri=DISMECH.chemical_entities, name="chemical_entities", curie=DISMECH.curie('chemical_entities'),
                   model_uri=DISMECH.chemical_entities, domain=None, range=Optional[Union[Union[dict, ChemicalEntityDescriptor], list[Union[dict, ChemicalEntityDescriptor]]]])

slots.triggers = Slot(uri=DISMECH.triggers, name="triggers", curie=DISMECH.curie('triggers'),
                   model_uri=DISMECH.triggers, domain=None, range=Optional[Union[Union[dict, TriggerDescriptor], list[Union[dict, TriggerDescriptor]]]])

slots.assays = Slot(uri=DISMECH.assays, name="assays", curie=DISMECH.curie('assays'),
                   model_uri=DISMECH.assays, domain=None, range=Optional[Union[Union[dict, AssayDescriptor], list[Union[dict, AssayDescriptor]]]])

slots.disease_term = Slot(uri=DISMECH.disease_term, name="disease_term", curie=DISMECH.curie('disease_term'),
                   model_uri=DISMECH.disease_term, domain=None, range=Optional[Union[dict, DiseaseDescriptor]])

slots.phenotype_term = Slot(uri=DISMECH.phenotype_term, name="phenotype_term", curie=DISMECH.curie('phenotype_term'),
                   model_uri=DISMECH.phenotype_term, domain=None, range=Optional[Union[dict, PhenotypeDescriptor]])

slots.treatment_term = Slot(uri=DISMECH.treatment_term, name="treatment_term", curie=DISMECH.curie('treatment_term'),
                   model_uri=DISMECH.treatment_term, domain=None, range=Optional[Union[dict, TreatmentDescriptor]])

slots.exposure_term = Slot(uri=DISMECH.exposure_term, name="exposure_term", curie=DISMECH.curie('exposure_term'),
                   model_uri=DISMECH.exposure_term, domain=None, range=Optional[Union[dict, ExposureDescriptor]])

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

slots.transmission = Slot(uri=DISMECH.transmission, name="transmission", curie=DISMECH.curie('transmission'),
                   model_uri=DISMECH.transmission, domain=None, range=Optional[Union[dict[Union[str, TransmissionName], Union[dict, Transmission]], list[Union[dict, Transmission]]]])

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

slots.AssayDescriptor_term = Slot(uri=DISMECH.term, name="AssayDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.AssayDescriptor_term, domain=AssayDescriptor, range=Optional[Union[dict, Term]])

slots.TriggerDescriptor_term = Slot(uri=DISMECH.term, name="TriggerDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.TriggerDescriptor_term, domain=TriggerDescriptor, range=Optional[Union[dict, Term]])

slots.DiseaseDescriptor_term = Slot(uri=DISMECH.term, name="DiseaseDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.DiseaseDescriptor_term, domain=DiseaseDescriptor, range=Optional[Union[dict, Term]])

slots.PhenotypeDescriptor_term = Slot(uri=DISMECH.term, name="PhenotypeDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.PhenotypeDescriptor_term, domain=PhenotypeDescriptor, range=Optional[Union[dict, Term]])

slots.TreatmentDescriptor_term = Slot(uri=DISMECH.term, name="TreatmentDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.TreatmentDescriptor_term, domain=TreatmentDescriptor, range=Optional[Union[dict, Term]])

slots.ExposureDescriptor_term = Slot(uri=DISMECH.term, name="ExposureDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.ExposureDescriptor_term, domain=ExposureDescriptor, range=Optional[Union[dict, Term]])

slots.EnvironmentDescriptor_term = Slot(uri=DISMECH.term, name="EnvironmentDescriptor_term", curie=DISMECH.curie('term'),
                   model_uri=DISMECH.EnvironmentDescriptor_term, domain=EnvironmentDescriptor, range=Optional[Union[dict, Term]])

slots.PublicationReference_reference = Slot(uri=DISMECH.reference, name="PublicationReference_reference", curie=DISMECH.curie('reference'),
                   model_uri=DISMECH.PublicationReference_reference, domain=PublicationReference, range=Union[str, PublicationReferenceReference])
