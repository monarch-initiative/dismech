"""ClinGen gene-disease validity data access module.

This module provides tools to:
1. Download ClinGen gene-disease validity curations
2. Extract experimental evidence details from curation pages
3. Search for Gene Ontology (GO) term references in evidence
4. Map functional evidence categories to GO terms
"""

from dismech.clingen.client import (
    ClinGenClient,
    GeneDiseaseValidity,
    ExperimentalEvidence,
    FunctionalEvidence,
)
from dismech.clingen.go_mapper import (
    GOMapping,
    get_all_go_mappings,
    get_go_mappings_for_category,
    get_go_mappings_for_keywords,
)
from dismech.clingen.go_annotations import (
    GOAnnotation,
    GeneGOAnnotations,
    GOAnnotationFetcher,
    get_experimental_evidence_codes,
    compare_clingen_to_go,
)

__all__ = [
    "ClinGenClient",
    "GeneDiseaseValidity",
    "ExperimentalEvidence",
    "FunctionalEvidence",
    "GOMapping",
    "get_all_go_mappings",
    "get_go_mappings_for_category",
    "get_go_mappings_for_keywords",
    "GOAnnotation",
    "GeneGOAnnotations",
    "GOAnnotationFetcher",
    "get_experimental_evidence_codes",
    "compare_clingen_to_go",
]
