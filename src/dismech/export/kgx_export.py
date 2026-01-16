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
    Association,
    ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation,
    DiseaseOrPhenotypicFeatureToLocationAssociation,
    DiseaseToPhenotypicFeatureAssociation,
    ExposureEventToOutcomeAssociation,
    GeneToDiseaseAssociation,
    KnowledgeLevelEnum,
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

    Note:
        The `supporting_text` field is not currently available on biolink
        Association classes (only on TextMiningStudyResult). For MVP, we
        return the formatted strings but they may not be usable until
        biolink model is updated. The `publications` list is always usable.
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


def _make_edge_id(subject: str, predicate: str, obj: str) -> str:
    """Generate a deterministic edge ID from subject, predicate, object."""
    # Use uuid5 with a namespace to create deterministic IDs
    namespace = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")  # URL namespace
    edge_string = f"{subject}|{predicate}|{obj}"
    return f"urn:uuid:{uuid.uuid5(namespace, edge_string)}"


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
    # Note: supporting_text not yet available on biolink Association classes
    publications, _supporting_text = _format_evidence(phenotype.get("evidence"), indirect=False)

    predicate = "biolink:has_phenotype"
    return DiseaseToPhenotypicFeatureAssociation(
        id=_make_edge_id(disease_id, predicate, term_id),
        subject=disease_id,
        predicate=predicate,
        object=term_id,
        frequency_qualifier=frequency_qualifier,
        publications=publications if publications else None,
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
    # Note: supporting_text not yet available on biolink Association classes
    publications, _supporting_text = _format_evidence(parent_evidence, indirect=True)

    predicate = "biolink:has_participant"
    return Association(
        id=_make_edge_id(disease_id, predicate, term_id),
        subject=disease_id,
        predicate=predicate,
        object=term_id,
        publications=publications if publications else None,
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
    # Note: supporting_text not yet available on biolink Association classes
    publications, _supporting_text = _format_evidence(parent_evidence, indirect=True)

    predicate = "biolink:disease_has_location"
    return DiseaseOrPhenotypicFeatureToLocationAssociation(
        id=_make_edge_id(disease_id, predicate, term_id),
        subject=disease_id,
        predicate=predicate,
        object=term_id,
        publications=publications if publications else None,
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
    # Note: supporting_text not yet available on biolink Association classes
    publications, _supporting_text = _format_evidence(parent_evidence, indirect=True)

    predicate = "biolink:affects"
    qualifiers = []
    if direction:
        qualifiers.append(f"direction:{direction}")

    return Association(
        id=_make_edge_id(disease_id, predicate, term_id),
        subject=disease_id,
        predicate=predicate,
        object=term_id,
        qualifiers=qualifiers if qualifiers else None,
        publications=publications if publications else None,
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
    # Note: supporting_text not yet available on biolink Association classes
    publications, _supporting_text = _format_evidence(treatment.get("evidence"), indirect=False)

    predicate = "biolink:treats_or_applied_or_studied_to_treat"
    return ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation(
        id=_make_edge_id(treatment_id, predicate, disease_id),
        subject=treatment_id,
        predicate=predicate,
        object=disease_id,
        publications=publications if publications else None,
        primary_knowledge_source=KNOWLEDGE_SOURCE,
        knowledge_level=KnowledgeLevelEnum.knowledge_assertion,
        agent_type=AgentTypeEnum.manual_validation_of_automated_agent,
    )


def gene_to_edge(disease_id: str, gene: dict[str, Any]) -> GeneToDiseaseAssociation | None:
    """
    Convert a genetic association entry to a KGX edge.

    Note: Gene entries use name (symbol) rather than term IDs.
    We create edges using HGNC symbol format.

    Args:
        disease_id: The disease term ID
        gene: A gene dict from genetic[]

    Returns:
        GeneToDiseaseAssociation or None if name is missing
    """
    gene_name = gene.get("name") if gene else None
    if not gene_name:
        return None

    # Use HGNC symbol format for gene identifier
    gene_id = f"HGNC.SYMBOL:{gene_name}"
    predicate = "biolink:gene_associated_with_condition"

    # Format evidence (direct - attached to genetic entry)
    # Note: supporting_text not yet available on biolink Association classes
    publications, _supporting_text = _format_evidence(gene.get("evidence"), indirect=False)

    return GeneToDiseaseAssociation(
        id=_make_edge_id(gene_id, predicate, disease_id),
        subject=gene_id,
        predicate=predicate,
        object=disease_id,
        publications=publications if publications else None,
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
    # Note: supporting_text not yet available on biolink Association classes
    publications, _supporting_text = _format_evidence(environmental.get("evidence"), indirect=False)

    predicate = "biolink:contributes_to"
    return ExposureEventToOutcomeAssociation(
        id=_make_edge_id(exposure_id, predicate, disease_id),
        subject=exposure_id,
        predicate=predicate,
        object=disease_id,
        publications=publications if publications else None,
        primary_knowledge_source=KNOWLEDGE_SOURCE,
        knowledge_level=KnowledgeLevelEnum.knowledge_assertion,
        agent_type=AgentTypeEnum.manual_validation_of_automated_agent,
    )


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

    # Extract treatment edges
    for treatment in record.get("treatments") or []:
        edge = treatment_to_edge(disease_id, treatment)
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


@koza.transform_record()
def koza_transform(koza_ctx: KozaTransform, record: dict[str, Any]) -> None:
    """
    Koza-decorated transform that wraps the pure transform function.

    This function is called by the Koza runner for each record.
    It calls the pure transform() function and writes each edge.

    Args:
        koza_ctx: The Koza transform context for writing output
        record: A disorder dict loaded from YAML
    """
    for edge in transform(record):
        koza_ctx.write(edge)
