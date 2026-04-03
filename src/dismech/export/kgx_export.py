"""
KGX edge exporter for dismech.

Transforms disorder YAML files into KGX-format edges for the knowledge graph.
Each function extracts edges from a specific collection type within the disorder.
"""

import uuid
from typing import Any, Iterator

import koza
from koza import KozaTransform

from biolink_model.datamodel.pydanticmodel_v2 import (
    AgentTypeEnum,
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
    KnowledgeLevelEnum,
    MacromolecularComplex,
    MolecularActivity,
    MolecularEntity,
    NamedThing,
    OrganismTaxon,
    Pathway,
    PhenotypicFeature,
    Treatment,
)


# Knowledge source for all edges
KNOWLEDGE_SOURCE = "infores:dismech"

# Frequency enum to HP term mapping
FREQUENCY_TO_HP = {
    "OBLIGATE": "HP:0040280",
    "VERY_FREQUENT": "HP:0040281",
    "FREQUENT": "HP:0040282",
    "OCCASIONAL": "HP:0040283",
    "VERY_RARE": "HP:0040284",
}

# Modifier enum to biolink direction qualifier
MODIFIER_TO_DIRECTION = {
    "INCREASED": "increased",
    "DECREASED": "decreased",
}


def _format_evidence(
    evidence_items: list[dict[str, Any]] | None, indirect: bool = False
) -> tuple[list[str], list[str]]:
    """
    Format evidence items for KGX export.

    Each evidence item is formatted as a concatenated string that preserves
    the PMID, support status, snippet, and explanation together.

    Args:
        evidence_items: List of evidence dicts from dismech
        indirect: If True, flag as inherited from parent mechanism

    Returns:
        Tuple of (publications list, supporting_text list)
    """
    publications = []
    supporting_text = []

    for e in evidence_items or []:
        ref = e.get("reference", "")
        if ref:
            publications.append(ref)

        # Build concatenated supporting text
        # Format: [PMID:xxx] [INDIRECT EVIDENCE] [SUPPORT] snippet --- Explanation: explanation
        supports = e.get("supports", "SUPPORT")
        snippet = e.get("snippet", "")
        explanation = e.get("explanation", "")

        if snippet:
            indirect_flag = "[INDIRECT EVIDENCE] " if indirect else ""
            text = f"[{ref}] {indirect_flag}[{supports}] {snippet}"
            if explanation:
                text += f" --- Explanation: {explanation}"
            supporting_text.append(text)

    return publications, supporting_text


def _make_edge_id() -> str:
    """Generate a unique edge ID."""
    return f"urn:uuid:{uuid.uuid4()}"


def _get_term_id(obj: dict[str, Any] | None, path: list[str]) -> str | None:
    """
    Safely navigate a nested dict to extract a term ID.

    Args:
        obj: The object to navigate
        path: List of keys to traverse (e.g., ["term", "id"])

    Returns:
        The term ID string if found, None otherwise
    """
    if obj is None:
        return None
    current = obj
    for key in path:
        if not isinstance(current, dict) or key not in current:
            return None
        current = current[key]
    return current if isinstance(current, str) else None


def phenotype_to_edge(disease_id: str, phenotype: dict[str, Any]) -> DiseaseToPhenotypicFeatureAssociation | None:
    """
    Convert a phenotype entry to a KGX edge.

    Args:
        disease_id: The disease term ID (e.g., "MONDO:0004979")
        phenotype: A phenotype dict from phenotypes[]

    Returns:
        DiseaseToPhenotypicFeatureAssociation or None if phenotype_term.term.id is missing
    """
    term_id = _get_term_id(phenotype, ["phenotype_term", "term", "id"])
    if not term_id:
        return None

    # Map frequency enum to HP term for qualifier
    frequency = phenotype.get("frequency")
    frequency_qualifier = FREQUENCY_TO_HP.get(frequency) if frequency else None

    # Format evidence (direct - attached to phenotype)
    publications, supporting_text = _format_evidence(phenotype.get("evidence"), indirect=False)

    predicate = "biolink:has_phenotype"
    return DiseaseToPhenotypicFeatureAssociation(
        id=_make_edge_id(),
        subject=disease_id,
        predicate=predicate,
        object=term_id,
        subject_category="biolink:Disease",
        object_category="biolink:PhenotypicFeature",
        frequency_qualifier=frequency_qualifier,
        publications=publications if publications else None,
        supporting_text=supporting_text if supporting_text else None,
        primary_knowledge_source=KNOWLEDGE_SOURCE,
        knowledge_level=KnowledgeLevelEnum.knowledge_assertion,
        agent_type=AgentTypeEnum.manual_validation_of_automated_agent,
    )


def cell_type_to_edge(
    disease_id: str, cell_type: dict[str, Any], parent_evidence: list[dict[str, Any]] | None = None
) -> Association | None:
    """
    Convert a cell type entry to a KGX edge.

    Args:
        disease_id: The disease term ID
        cell_type: A cell type dict from pathophysiology[].cell_types[]
        parent_evidence: Evidence from parent pathophysiology mechanism (indirect)

    Returns:
        Association or None if term.id is missing
    """
    term_id = _get_term_id(cell_type, ["term", "id"])
    if not term_id:
        return None

    # Format evidence (indirect - inherited from parent mechanism)
    publications, supporting_text = _format_evidence(parent_evidence, indirect=True)

    predicate = "biolink:has_participant"
    return Association(
        id=_make_edge_id(),
        subject=disease_id,
        predicate=predicate,
        object=term_id,
        subject_category="biolink:Disease",
        object_category="biolink:Cell",
        publications=publications if publications else None,
        supporting_text=supporting_text if supporting_text else None,
        primary_knowledge_source=KNOWLEDGE_SOURCE,
        knowledge_level=KnowledgeLevelEnum.knowledge_assertion,
        agent_type=AgentTypeEnum.manual_validation_of_automated_agent,
    )


def location_to_edge(
    disease_id: str, location: dict[str, Any], parent_evidence: list[dict[str, Any]] | None = None
) -> DiseaseOrPhenotypicFeatureToLocationAssociation | None:
    """
    Convert a location entry to a KGX edge.

    Args:
        disease_id: The disease term ID
        location: A location dict from pathophysiology[].locations[]
        parent_evidence: Evidence from parent pathophysiology mechanism (indirect)

    Returns:
        DiseaseOrPhenotypicFeatureToLocationAssociation or None if term.id is missing
    """
    term_id = _get_term_id(location, ["term", "id"])
    if not term_id:
        return None

    # Format evidence (indirect - inherited from parent mechanism)
    publications, supporting_text = _format_evidence(parent_evidence, indirect=True)

    predicate = "biolink:disease_has_location"
    return DiseaseOrPhenotypicFeatureToLocationAssociation(
        id=_make_edge_id(),
        subject=disease_id,
        predicate=predicate,
        object=term_id,
        subject_category="biolink:Disease",
        object_category="biolink:AnatomicalEntity",
        publications=publications if publications else None,
        supporting_text=supporting_text if supporting_text else None,
        primary_knowledge_source=KNOWLEDGE_SOURCE,
        knowledge_level=KnowledgeLevelEnum.knowledge_assertion,
        agent_type=AgentTypeEnum.manual_validation_of_automated_agent,
    )


def biological_process_to_edge(
    disease_id: str, process: dict[str, Any], parent_evidence: list[dict[str, Any]] | None = None
) -> Association | None:
    """
    Convert a biological process entry to a KGX edge.

    Uses biolink:affects predicate. The modifier field (INCREASED/DECREASED)
    is captured in the qualifiers list for future use when biolink supports
    typed qualifier fields on a Disease→BiologicalProcess association.

    Args:
        disease_id: The disease term ID
        process: A process dict from pathophysiology[].biological_processes[]
        parent_evidence: Evidence from parent pathophysiology mechanism (indirect)

    Returns:
        Association or None if term.id is missing
    """
    term_id = _get_term_id(process, ["term", "id"])
    if not term_id:
        return None

    # Get modifier and map to direction qualifier string
    # Note: Base Association class doesn't support typed qualifiers like
    # object_direction_qualifier, so we store it in the qualifiers list
    modifier = process.get("modifier")
    direction = MODIFIER_TO_DIRECTION.get(modifier) if modifier else None

    # Format evidence (indirect - inherited from parent mechanism)
    publications, supporting_text = _format_evidence(parent_evidence, indirect=True)

    predicate = "biolink:affects"
    qualifiers = []
    if direction:
        qualifiers.append(f"direction:{direction}")

    return Association(
        id=_make_edge_id(),
        subject=disease_id,
        predicate=predicate,
        object=term_id,
        subject_category="biolink:Disease",
        object_category="biolink:BiologicalProcess",
        qualifiers=qualifiers if qualifiers else None,
        publications=publications if publications else None,
        supporting_text=supporting_text if supporting_text else None,
        primary_knowledge_source=KNOWLEDGE_SOURCE,
        knowledge_level=KnowledgeLevelEnum.knowledge_assertion,
        agent_type=AgentTypeEnum.manual_validation_of_automated_agent,
    )


def treatment_to_edge(disease_id: str, treatment: dict[str, Any]) -> ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation | None:
    """
    Convert a treatment entry to a KGX edge.

    Treatment → Disease using treats_or_applied_or_studied_to_treat.
    This is the safe/broad predicate since dismech doesn't capture
    evidence level to distinguish treats vs studied_to_treat.

    Args:
        disease_id: The disease term ID
        treatment: A treatment dict from treatments[]

    Returns:
        ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation or None if treatment_term.term.id is missing
    """
    treatment_id = _get_term_id(treatment, ["treatment_term", "term", "id"])
    if not treatment_id:
        return None

    # Format evidence (direct - attached to treatment)
    publications, supporting_text = _format_evidence(treatment.get("evidence"), indirect=False)

    predicate = "biolink:treats_or_applied_or_studied_to_treat"
    return ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation(
        id=_make_edge_id(),
        subject=treatment_id,
        predicate=predicate,
        object=disease_id,
        subject_category="biolink:Treatment",
        object_category="biolink:Disease",
        publications=publications if publications else None,
        supporting_text=supporting_text if supporting_text else None,
        primary_knowledge_source=KNOWLEDGE_SOURCE,
        knowledge_level=KnowledgeLevelEnum.knowledge_assertion,
        agent_type=AgentTypeEnum.manual_validation_of_automated_agent,
    )


def gene_to_edge(disease_id: str, gene: dict[str, Any]) -> GeneToDiseaseAssociation | None:
    """
    Convert a genetic association entry to a KGX edge.

    Prefers gene_term.term.id (proper HGNC CURIE) when available,
    falls back to constructing HGNC.SYMBOL:{name} from the name field.

    Args:
        disease_id: The disease term ID
        gene: A gene dict from genetic[]

    Returns:
        GeneToDiseaseAssociation or None if neither gene_term.term.id nor name is available
    """
    if not gene:
        return None

    # Prefer proper HGNC CURIE from gene_term, fall back to symbol from name
    gene_id = _get_term_id(gene, ["gene_term", "term", "id"])
    if not gene_id:
        gene_name = gene.get("name")
        if not gene_name:
            return None
        gene_id = f"HGNC.SYMBOL:{gene_name}"

    predicate = "biolink:contributes_to"

    # Format evidence (direct - attached to genetic entry)
    publications, supporting_text = _format_evidence(gene.get("evidence"), indirect=False)

    return GeneToDiseaseAssociation(
        id=_make_edge_id(),
        subject=gene_id,
        predicate=predicate,
        object=disease_id,
        subject_category="biolink:Gene",
        object_category="biolink:Disease",
        publications=publications if publications else None,
        supporting_text=supporting_text if supporting_text else None,
        primary_knowledge_source=KNOWLEDGE_SOURCE,
        knowledge_level=KnowledgeLevelEnum.knowledge_assertion,
        agent_type=AgentTypeEnum.manual_validation_of_automated_agent,
    )


def exposure_to_edge(disease_id: str, environmental: dict[str, Any]) -> ExposureEventToOutcomeAssociation | None:
    """
    Convert an environmental exposure entry to a KGX edge.

    Exposure → Disease using contributes_to (risk factor relationship).
    Uses ExposureEventToOutcomeAssociation since Disease is-a Outcome in Biolink.

    Args:
        disease_id: The disease term ID
        environmental: An environmental dict from environmental[]

    Returns:
        ExposureEventToOutcomeAssociation or None if exposure_term.term.id is missing
    """
    exposure_id = _get_term_id(environmental, ["exposure_term", "term", "id"])
    if not exposure_id:
        return None

    # Format evidence (direct - attached to environmental entry)
    publications, supporting_text = _format_evidence(environmental.get("evidence"), indirect=False)

    predicate = "biolink:contributes_to"
    return ExposureEventToOutcomeAssociation(
        id=_make_edge_id(),
        subject=exposure_id,
        predicate=predicate,
        object=disease_id,
        subject_category="biolink:ExposureEvent",
        object_category="biolink:Disease",
        publications=publications if publications else None,
        supporting_text=supporting_text if supporting_text else None,
        primary_knowledge_source=KNOWLEDGE_SOURCE,
        knowledge_level=KnowledgeLevelEnum.knowledge_assertion,
        agent_type=AgentTypeEnum.manual_validation_of_automated_agent,
    )


def molecular_function_to_edge(
    disease_id: str, mf: dict[str, Any], parent_evidence: list[dict[str, Any]] | None = None
) -> Association | None:
    """
    Convert a molecular function entry to a KGX edge.

    Same pattern as biological_process_to_edge: Disease affects GO molecular function,
    with optional direction qualifier from modifier.

    Args:
        disease_id: The disease term ID
        mf: A molecular function dict from pathophysiology[].molecular_functions[]
        parent_evidence: Evidence from parent pathophysiology mechanism (indirect)

    Returns:
        Association or None if term.id is missing
    """
    term_id = _get_term_id(mf, ["term", "id"])
    if not term_id:
        return None

    modifier = mf.get("modifier")
    direction = MODIFIER_TO_DIRECTION.get(modifier) if modifier else None

    publications, supporting_text = _format_evidence(parent_evidence, indirect=True)

    qualifiers = []
    if direction:
        qualifiers.append(f"direction:{direction}")

    return Association(
        id=_make_edge_id(),
        subject=disease_id,
        predicate="biolink:affects",
        object=term_id,
        subject_category="biolink:Disease",
        object_category="biolink:MolecularActivity",
        qualifiers=qualifiers if qualifiers else None,
        publications=publications if publications else None,
        supporting_text=supporting_text if supporting_text else None,
        primary_knowledge_source=KNOWLEDGE_SOURCE,
        knowledge_level=KnowledgeLevelEnum.knowledge_assertion,
        agent_type=AgentTypeEnum.manual_validation_of_automated_agent,
    )


def cellular_component_to_edge(
    disease_id: str, component: dict[str, Any], parent_evidence: list[dict[str, Any]] | None = None
) -> Association | None:
    """
    Convert a cellular component entry to a KGX edge.

    Args:
        disease_id: The disease term ID
        component: A cellular component dict from pathophysiology[].cellular_components[]
        parent_evidence: Evidence from parent pathophysiology mechanism (indirect)

    Returns:
        Association or None if term.id is missing
    """
    term_id = _get_term_id(component, ["term", "id"])
    if not term_id:
        return None

    publications, supporting_text = _format_evidence(parent_evidence, indirect=True)

    return Association(
        id=_make_edge_id(),
        subject=disease_id,
        predicate="biolink:has_participant",
        object=term_id,
        subject_category="biolink:Disease",
        object_category="biolink:CellularComponent",
        publications=publications if publications else None,
        supporting_text=supporting_text if supporting_text else None,
        primary_knowledge_source=KNOWLEDGE_SOURCE,
        knowledge_level=KnowledgeLevelEnum.knowledge_assertion,
        agent_type=AgentTypeEnum.manual_validation_of_automated_agent,
    )


def chemical_entity_to_edge(
    disease_id: str, chemical: dict[str, Any], parent_evidence: list[dict[str, Any]] | None = None
) -> Association | None:
    """
    Convert a chemical entity entry to a KGX edge.

    Args:
        disease_id: The disease term ID
        chemical: A chemical entity dict from pathophysiology[].chemical_entities[]
        parent_evidence: Evidence from parent pathophysiology mechanism (indirect)

    Returns:
        Association or None if term.id is missing
    """
    term_id = _get_term_id(chemical, ["term", "id"])
    if not term_id:
        return None

    publications, supporting_text = _format_evidence(parent_evidence, indirect=True)

    return Association(
        id=_make_edge_id(),
        subject=disease_id,
        predicate="biolink:has_participant",
        object=term_id,
        subject_category="biolink:Disease",
        object_category="biolink:ChemicalEntity",
        publications=publications if publications else None,
        supporting_text=supporting_text if supporting_text else None,
        primary_knowledge_source=KNOWLEDGE_SOURCE,
        knowledge_level=KnowledgeLevelEnum.knowledge_assertion,
        agent_type=AgentTypeEnum.manual_validation_of_automated_agent,
    )


def pathway_to_edge(
    disease_id: str, pathway: dict[str, Any], parent_evidence: list[dict[str, Any]] | None = None
) -> Association | None:
    """
    Convert a pathway entry to a KGX edge.

    Same pattern as biological_process_to_edge: Disease affects GO biological process
    (pathways are GO BP terms), with optional direction qualifier.

    Args:
        disease_id: The disease term ID
        pathway: A pathway dict from pathophysiology[].pathways[]
        parent_evidence: Evidence from parent pathophysiology mechanism (indirect)

    Returns:
        Association or None if term.id is missing
    """
    term_id = _get_term_id(pathway, ["term", "id"])
    if not term_id:
        return None

    modifier = pathway.get("modifier")
    direction = MODIFIER_TO_DIRECTION.get(modifier) if modifier else None

    publications, supporting_text = _format_evidence(parent_evidence, indirect=True)

    qualifiers = []
    if direction:
        qualifiers.append(f"direction:{direction}")

    return Association(
        id=_make_edge_id(),
        subject=disease_id,
        predicate="biolink:affects",
        object=term_id,
        subject_category="biolink:Disease",
        object_category="biolink:Pathway",
        qualifiers=qualifiers if qualifiers else None,
        publications=publications if publications else None,
        supporting_text=supporting_text if supporting_text else None,
        primary_knowledge_source=KNOWLEDGE_SOURCE,
        knowledge_level=KnowledgeLevelEnum.knowledge_assertion,
        agent_type=AgentTypeEnum.manual_validation_of_automated_agent,
    )


def protein_complex_to_edge(
    disease_id: str, complex_: dict[str, Any], parent_evidence: list[dict[str, Any]] | None = None
) -> Association | None:
    """
    Convert a protein complex entry to a KGX edge.

    Args:
        disease_id: The disease term ID
        complex_: A protein complex dict from pathophysiology[].protein_complexes[]
        parent_evidence: Evidence from parent pathophysiology mechanism (indirect)

    Returns:
        Association or None if term.id is missing
    """
    term_id = _get_term_id(complex_, ["term", "id"])
    if not term_id:
        return None

    publications, supporting_text = _format_evidence(parent_evidence, indirect=True)

    return Association(
        id=_make_edge_id(),
        subject=disease_id,
        predicate="biolink:has_participant",
        object=term_id,
        subject_category="biolink:Disease",
        object_category="biolink:MacromolecularComplex",
        publications=publications if publications else None,
        supporting_text=supporting_text if supporting_text else None,
        primary_knowledge_source=KNOWLEDGE_SOURCE,
        knowledge_level=KnowledgeLevelEnum.knowledge_assertion,
        agent_type=AgentTypeEnum.manual_validation_of_automated_agent,
    )


def inheritance_to_edge(
    disease_id: str, inheritance: dict[str, Any]
) -> DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation | None:
    """
    Convert an inheritance entry to a KGX edge.

    Args:
        disease_id: The disease term ID
        inheritance: An inheritance dict from inheritance[]

    Returns:
        DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation or None if
        inheritance_term.term.id is missing
    """
    term_id = _get_term_id(inheritance, ["inheritance_term", "term", "id"])
    if not term_id:
        return None

    publications, supporting_text = _format_evidence(inheritance.get("evidence"), indirect=False)

    return DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation(
        id=_make_edge_id(),
        subject=disease_id,
        predicate="biolink:has_mode_of_inheritance",
        object=term_id,
        subject_category="biolink:Disease",
        object_category="biolink:GeneticInheritance",
        publications=publications if publications else None,
        supporting_text=supporting_text if supporting_text else None,
        primary_knowledge_source=KNOWLEDGE_SOURCE,
        knowledge_level=KnowledgeLevelEnum.knowledge_assertion,
        agent_type=AgentTypeEnum.manual_validation_of_automated_agent,
    )


def infectious_agent_to_edge(
    disease_id: str, agent: dict[str, Any]
) -> Association | None:
    """
    Convert an infectious agent entry to a KGX edge.

    Organism → Disease using biolink:causes.

    Args:
        disease_id: The disease term ID
        agent: An infectious agent dict from infectious_agent[]

    Returns:
        Association or None if infectious_agent_term.term.id is missing
    """
    agent_id = _get_term_id(agent, ["infectious_agent_term", "term", "id"])
    if not agent_id:
        return None

    publications, supporting_text = _format_evidence(agent.get("evidence"), indirect=False)

    return Association(
        id=_make_edge_id(),
        subject=agent_id,
        predicate="biolink:causes",
        object=disease_id,
        subject_category="biolink:OrganismTaxon",
        object_category="biolink:Disease",
        publications=publications if publications else None,
        supporting_text=supporting_text if supporting_text else None,
        primary_knowledge_source=KNOWLEDGE_SOURCE,
        knowledge_level=KnowledgeLevelEnum.knowledge_assertion,
        agent_type=AgentTypeEnum.manual_validation_of_automated_agent,
    )


def histopathology_to_edge(
    disease_id: str, finding: dict[str, Any]
) -> DiseaseToPhenotypicFeatureAssociation | None:
    """
    Convert a histopathology finding to a KGX edge.

    Histopathological findings (NCIT morphologic findings) are treated as
    phenotypic features: Disease has_phenotype HistopathologyFinding.

    Args:
        disease_id: The disease term ID
        finding: A histopathology dict from histopathology[]

    Returns:
        DiseaseToPhenotypicFeatureAssociation or None if finding_term.term.id is missing
    """
    term_id = _get_term_id(finding, ["finding_term", "term", "id"])
    if not term_id:
        return None

    publications, supporting_text = _format_evidence(finding.get("evidence"), indirect=False)

    return DiseaseToPhenotypicFeatureAssociation(
        id=_make_edge_id(),
        subject=disease_id,
        predicate="biolink:has_phenotype",
        object=term_id,
        subject_category="biolink:Disease",
        object_category="biolink:PhenotypicFeature",
        publications=publications if publications else None,
        supporting_text=supporting_text if supporting_text else None,
        primary_knowledge_source=KNOWLEDGE_SOURCE,
        knowledge_level=KnowledgeLevelEnum.knowledge_assertion,
        agent_type=AgentTypeEnum.manual_validation_of_automated_agent,
    )


def biomarker_to_edge(
    disease_id: str, biochemical: dict[str, Any]
) -> Association | None:
    """
    Convert a biochemical/biomarker entry to a KGX edge.

    Disease has_biomarker ChemicalEntity/Biomarker.

    Args:
        disease_id: The disease term ID
        biochemical: A biochemical dict from biochemical[]

    Returns:
        Association or None if biomarker_term.term.id is missing
    """
    term_id = _get_term_id(biochemical, ["biomarker_term", "term", "id"])
    if not term_id:
        return None

    publications, supporting_text = _format_evidence(biochemical.get("evidence"), indirect=False)

    return Association(
        id=_make_edge_id(),
        subject=disease_id,
        predicate="biolink:has_biomarker",
        object=term_id,
        subject_category="biolink:Disease",
        object_category="biolink:MolecularEntity",
        publications=publications if publications else None,
        supporting_text=supporting_text if supporting_text else None,
        primary_knowledge_source=KNOWLEDGE_SOURCE,
        knowledge_level=KnowledgeLevelEnum.knowledge_assertion,
        agent_type=AgentTypeEnum.manual_validation_of_automated_agent,
    )


def therapeutic_agent_to_edge(
    disease_id: str, agent: dict[str, Any], parent_evidence: list[dict[str, Any]] | None = None
) -> ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation | None:
    """
    Convert a therapeutic agent (specific drug) to a KGX edge.

    TherapeuticAgent → Disease using treats_or_applied_or_studied_to_treat.
    These are specific drugs (NCIT/CHEBI) nested under treatment_term.therapeutic_agent[].

    Args:
        disease_id: The disease term ID
        agent: A therapeutic agent dict from treatments[].treatment_term.therapeutic_agent[]
        parent_evidence: Evidence from parent treatment (indirect)

    Returns:
        ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation or None if term.id is missing
    """
    agent_id = _get_term_id(agent, ["term", "id"])
    if not agent_id:
        return None

    publications, supporting_text = _format_evidence(parent_evidence, indirect=True)

    return ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation(
        id=_make_edge_id(),
        subject=agent_id,
        predicate="biolink:treats_or_applied_or_studied_to_treat",
        object=disease_id,
        subject_category="biolink:ChemicalEntity",
        object_category="biolink:Disease",
        publications=publications if publications else None,
        supporting_text=supporting_text if supporting_text else None,
        primary_knowledge_source=KNOWLEDGE_SOURCE,
        knowledge_level=KnowledgeLevelEnum.knowledge_assertion,
        agent_type=AgentTypeEnum.manual_validation_of_automated_agent,
    )


def treatment_target_phenotype_to_edge(
    disease_id: str, treatment_id: str, phenotype: dict[str, Any],
    parent_evidence: list[dict[str, Any]] | None = None
) -> ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation | None:
    """
    Convert a treatment's target phenotype to a KGX edge.

    Treatment → Phenotype with disease_context_qualifier linking back to the disease.
    This captures "treatment X treats phenotype Y in the context of disease Z".

    Args:
        disease_id: The disease term ID (used as disease_context_qualifier)
        treatment_id: The treatment term ID (MAXO)
        phenotype: A phenotype descriptor dict from treatments[].target_phenotypes[]
        parent_evidence: Evidence from parent treatment (indirect)

    Returns:
        ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation or None if term.id is missing
    """
    phenotype_id = _get_term_id(phenotype, ["term", "id"])
    if not phenotype_id:
        return None

    publications, supporting_text = _format_evidence(parent_evidence, indirect=True)

    return ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation(
        id=_make_edge_id(),
        subject=treatment_id,
        predicate="biolink:treats_or_applied_or_studied_to_treat",
        object=phenotype_id,
        subject_category="biolink:Treatment",
        object_category="biolink:PhenotypicFeature",
        disease_context_qualifier=disease_id,
        publications=publications if publications else None,
        supporting_text=supporting_text if supporting_text else None,
        primary_knowledge_source=KNOWLEDGE_SOURCE,
        knowledge_level=KnowledgeLevelEnum.knowledge_assertion,
        agent_type=AgentTypeEnum.manual_validation_of_automated_agent,
    )


# Mapping from category string to biolink node class
_CATEGORY_TO_NODE_CLASS: dict[str, type[NamedThing]] = {
    "biolink:Disease": Disease,
    "biolink:PhenotypicFeature": PhenotypicFeature,
    "biolink:Cell": Cell,
    "biolink:AnatomicalEntity": AnatomicalEntity,
    "biolink:BiologicalProcess": BiologicalProcess,
    "biolink:MolecularActivity": MolecularActivity,
    "biolink:CellularComponent": CellularComponent,
    "biolink:ChemicalEntity": ChemicalEntity,
    "biolink:Pathway": Pathway,
    "biolink:MacromolecularComplex": MacromolecularComplex,
    "biolink:Treatment": Treatment,
    "biolink:Gene": Gene,
    "biolink:GeneticInheritance": GeneticInheritance,
    "biolink:OrganismTaxon": OrganismTaxon,
    "biolink:MolecularEntity": MolecularEntity,
    "biolink:ExposureEvent": ExposureEvent,
}


def _make_node(node_id: str, name: str | None, category: str) -> NamedThing:
    """
    Create a biolink node of the appropriate type.

    Args:
        node_id: The CURIE identifier (e.g., "MONDO:0004979")
        name: Human-readable label
        category: Biolink category string (e.g., "biolink:Disease")

    Returns:
        A NamedThing subclass instance with the correct category
    """
    cls = _CATEGORY_TO_NODE_CLASS.get(category, NamedThing)
    return cls(id=node_id, name=name, provided_by=[KNOWLEDGE_SOURCE])


def extract_nodes(record: dict[str, Any]) -> Iterator[NamedThing]:
    """
    Extract all unique KGX nodes from a disorder record.

    Walks the same record structure as transform() but yields node objects
    instead of edges. Each unique entity ID is emitted only once.

    Args:
        record: A disorder dict loaded from YAML

    Yields:
        NamedThing subclass instances for all unique entities
    """
    seen: set[str] = set()

    def _emit(node_id: str | None, name: str | None, category: str) -> NamedThing | None:
        if not node_id or node_id in seen:
            return None
        seen.add(node_id)
        return _make_node(node_id, name, category)

    # Disease node
    disease_id = _get_term_id(record, ["disease_term", "term", "id"])
    if not disease_id:
        return
    disease_label = _get_term_id(record, ["disease_term", "term", "label"])
    node = _emit(disease_id, record.get("name") or disease_label, "biolink:Disease")
    if node:
        yield node

    # Phenotype nodes
    for phenotype in record.get("phenotypes") or []:
        term_id = _get_term_id(phenotype, ["phenotype_term", "term", "id"])
        label = _get_term_id(phenotype, ["phenotype_term", "term", "label"])
        node = _emit(term_id, phenotype.get("name") or label, "biolink:PhenotypicFeature")
        if node:
            yield node

    # Pathophysiology sub-entities
    for patho in record.get("pathophysiology") or []:
        for cell_type in patho.get("cell_types") or []:
            term_id = _get_term_id(cell_type, ["term", "id"])
            label = _get_term_id(cell_type, ["term", "label"])
            node = _emit(term_id, cell_type.get("preferred_term") or label, "biolink:Cell")
            if node:
                yield node

        for location in patho.get("locations") or []:
            term_id = _get_term_id(location, ["term", "id"])
            label = _get_term_id(location, ["term", "label"])
            node = _emit(term_id, location.get("preferred_term") or label, "biolink:AnatomicalEntity")
            if node:
                yield node

        for process in patho.get("biological_processes") or []:
            term_id = _get_term_id(process, ["term", "id"])
            label = _get_term_id(process, ["term", "label"])
            node = _emit(term_id, process.get("preferred_term") or label, "biolink:BiologicalProcess")
            if node:
                yield node

        for mf in patho.get("molecular_functions") or []:
            term_id = _get_term_id(mf, ["term", "id"])
            label = _get_term_id(mf, ["term", "label"])
            node = _emit(term_id, mf.get("preferred_term") or label, "biolink:MolecularActivity")
            if node:
                yield node

        for component in patho.get("cellular_components") or []:
            term_id = _get_term_id(component, ["term", "id"])
            label = _get_term_id(component, ["term", "label"])
            node = _emit(term_id, component.get("preferred_term") or label, "biolink:CellularComponent")
            if node:
                yield node

        for chemical in patho.get("chemical_entities") or []:
            term_id = _get_term_id(chemical, ["term", "id"])
            label = _get_term_id(chemical, ["term", "label"])
            node = _emit(term_id, chemical.get("preferred_term") or label, "biolink:ChemicalEntity")
            if node:
                yield node

        for pathway in patho.get("pathways") or []:
            term_id = _get_term_id(pathway, ["term", "id"])
            label = _get_term_id(pathway, ["term", "label"])
            node = _emit(term_id, pathway.get("preferred_term") or label, "biolink:Pathway")
            if node:
                yield node

        for complex_ in patho.get("protein_complexes") or []:
            term_id = _get_term_id(complex_, ["term", "id"])
            label = _get_term_id(complex_, ["term", "label"])
            node = _emit(term_id, complex_.get("preferred_term") or label, "biolink:MacromolecularComplex")
            if node:
                yield node

    # Treatment nodes (action term + therapeutic agents)
    for treatment in record.get("treatments") or []:
        treatment_id = _get_term_id(treatment, ["treatment_term", "term", "id"])
        treatment_label = _get_term_id(treatment, ["treatment_term", "term", "label"])
        node = _emit(treatment_id, treatment.get("name") or treatment_label, "biolink:Treatment")
        if node:
            yield node

        treatment_term = treatment.get("treatment_term") or {}
        for agent in treatment_term.get("therapeutic_agent") or []:
            term_id = _get_term_id(agent, ["term", "id"])
            label = _get_term_id(agent, ["term", "label"])
            node = _emit(term_id, agent.get("preferred_term") or label, "biolink:ChemicalEntity")
            if node:
                yield node

        # Target phenotype nodes
        for phenotype in treatment.get("target_phenotypes") or []:
            term_id = _get_term_id(phenotype, ["term", "id"])
            label = _get_term_id(phenotype, ["term", "label"])
            node = _emit(term_id, phenotype.get("preferred_term") or label, "biolink:PhenotypicFeature")
            if node:
                yield node

    # Gene nodes
    for gene in record.get("genetic") or []:
        gene_id = _get_term_id(gene, ["gene_term", "term", "id"])
        if gene_id:
            label = _get_term_id(gene, ["gene_term", "term", "label"])
            node = _emit(gene_id, gene.get("name") or label, "biolink:Gene")
        else:
            gene_name = gene.get("name") if gene else None
            if gene_name:
                gene_id = f"HGNC.SYMBOL:{gene_name}"
                node = _emit(gene_id, gene_name, "biolink:Gene")
            else:
                node = None
        if node:
            yield node

    # Environmental exposure nodes
    for environmental in record.get("environmental") or []:
        term_id = _get_term_id(environmental, ["exposure_term", "term", "id"])
        label = _get_term_id(environmental, ["exposure_term", "term", "label"])
        node = _emit(term_id, environmental.get("name") or label, "biolink:ExposureEvent")
        if node:
            yield node

    # Inheritance nodes
    for inheritance in record.get("inheritance") or []:
        term_id = _get_term_id(inheritance, ["inheritance_term", "term", "id"])
        label = _get_term_id(inheritance, ["inheritance_term", "term", "label"])
        node = _emit(term_id, label, "biolink:GeneticInheritance")
        if node:
            yield node

    # Infectious agent nodes
    for agent in record.get("infectious_agent") or []:
        term_id = _get_term_id(agent, ["infectious_agent_term", "term", "id"])
        label = _get_term_id(agent, ["infectious_agent_term", "term", "label"])
        node = _emit(term_id, agent.get("name") or label, "biolink:OrganismTaxon")
        if node:
            yield node

    # Histopathology finding nodes
    for finding in record.get("histopathology") or []:
        term_id = _get_term_id(finding, ["finding_term", "term", "id"])
        label = _get_term_id(finding, ["finding_term", "term", "label"])
        node = _emit(term_id, finding.get("name") or label, "biolink:PhenotypicFeature")
        if node:
            yield node

    # Biochemical/biomarker nodes
    for biochemical in record.get("biochemical") or []:
        term_id = _get_term_id(biochemical, ["biomarker_term", "term", "id"])
        label = _get_term_id(biochemical, ["biomarker_term", "term", "label"])
        node = _emit(term_id, biochemical.get("name") or label, "biolink:MolecularEntity")
        if node:
            yield node


def transform(record: dict[str, Any]) -> Iterator[Association]:
    """
    Extract all KGX edges from a disorder record.

    This is the pure function for extracting edges. It can be called directly
    for testing without the Koza runner.

    Args:
        record: A disorder dict loaded from YAML

    Yields:
        Association objects for all associations in the disorder
    """
    # Get disease ID - required for all edges
    disease_id = _get_term_id(record, ["disease_term", "term", "id"])
    if not disease_id:
        return

    # Extract phenotype edges
    for phenotype in record.get("phenotypes") or []:
        edge = phenotype_to_edge(disease_id, phenotype)
        if edge:
            yield edge

    # Extract edges from pathophysiology
    for patho in record.get("pathophysiology") or []:
        # Get parent evidence for indirect attribution to children
        parent_evidence = patho.get("evidence")

        # Cell types (indirect evidence from parent mechanism)
        for cell_type in patho.get("cell_types") or []:
            edge = cell_type_to_edge(disease_id, cell_type, parent_evidence)
            if edge:
                yield edge

        # Locations (indirect evidence from parent mechanism)
        for location in patho.get("locations") or []:
            edge = location_to_edge(disease_id, location, parent_evidence)
            if edge:
                yield edge

        # Biological processes (indirect evidence from parent mechanism)
        for process in patho.get("biological_processes") or []:
            edge = biological_process_to_edge(disease_id, process, parent_evidence)
            if edge:
                yield edge

        # Molecular functions (indirect evidence from parent mechanism)
        for mf in patho.get("molecular_functions") or []:
            edge = molecular_function_to_edge(disease_id, mf, parent_evidence)
            if edge:
                yield edge

        # Cellular components (indirect evidence from parent mechanism)
        for component in patho.get("cellular_components") or []:
            edge = cellular_component_to_edge(disease_id, component, parent_evidence)
            if edge:
                yield edge

        # Chemical entities (indirect evidence from parent mechanism)
        for chemical in patho.get("chemical_entities") or []:
            edge = chemical_entity_to_edge(disease_id, chemical, parent_evidence)
            if edge:
                yield edge

        # Pathways (indirect evidence from parent mechanism)
        for pathway in patho.get("pathways") or []:
            edge = pathway_to_edge(disease_id, pathway, parent_evidence)
            if edge:
                yield edge

        # Protein complexes (indirect evidence from parent mechanism)
        for complex_ in patho.get("protein_complexes") or []:
            edge = protein_complex_to_edge(disease_id, complex_, parent_evidence)
            if edge:
                yield edge

    # Extract treatment edges (action, therapeutic agents, and target phenotypes)
    for treatment in record.get("treatments") or []:
        edge = treatment_to_edge(disease_id, treatment)
        if edge:
            yield edge

        # Therapeutic agents (specific drugs nested under treatment_term)
        treatment_evidence = treatment.get("evidence")
        treatment_term = treatment.get("treatment_term") or {}
        for agent in treatment_term.get("therapeutic_agent") or []:
            edge = therapeutic_agent_to_edge(disease_id, agent, treatment_evidence)
            if edge:
                yield edge

        # Target phenotypes (treatment → phenotype with disease context)
        treatment_id = _get_term_id(treatment, ["treatment_term", "term", "id"])
        if treatment_id:
            for phenotype in treatment.get("target_phenotypes") or []:
                edge = treatment_target_phenotype_to_edge(
                    disease_id, treatment_id, phenotype, treatment_evidence
                )
                if edge:
                    yield edge

    # Extract gene association edges
    for gene in record.get("genetic") or []:
        edge = gene_to_edge(disease_id, gene)
        if edge:
            yield edge

    # Extract environmental exposure edges
    for environmental in record.get("environmental") or []:
        edge = exposure_to_edge(disease_id, environmental)
        if edge:
            yield edge

    # Extract inheritance edges
    for inheritance in record.get("inheritance") or []:
        edge = inheritance_to_edge(disease_id, inheritance)
        if edge:
            yield edge

    # Extract infectious agent edges
    for agent in record.get("infectious_agent") or []:
        edge = infectious_agent_to_edge(disease_id, agent)
        if edge:
            yield edge

    # Extract histopathology edges
    for finding in record.get("histopathology") or []:
        edge = histopathology_to_edge(disease_id, finding)
        if edge:
            yield edge

    # Extract biochemical/biomarker edges
    for biochemical in record.get("biochemical") or []:
        edge = biomarker_to_edge(disease_id, biochemical)
        if edge:
            yield edge


@koza.transform_record()
def koza_transform(koza_ctx: KozaTransform, record: dict[str, Any]) -> None:
    """
    Koza-decorated transform that wraps the pure transform function.

    This function is called by the Koza runner for each record.
    It writes node records for all unique entities, then edge records
    for all associations.

    Args:
        koza_ctx: The Koza transform context for writing output
        record: A disorder dict loaded from YAML
    """
    for node in extract_nodes(record):
        koza_ctx.write(node)
    for edge in transform(record):
        koza_ctx.write(edge)
