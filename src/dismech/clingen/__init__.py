"""ClinGen gene-disease validity data access module.

This module provides tools to:
1. Download ClinGen gene-disease validity curations
2. Extract experimental evidence details from curation pages
3. Search for Gene Ontology (GO) term references in evidence
4. Map functional evidence categories to GO terms
"""

from dismech.clingen.client import (
    ClinGenClient,
    ExperimentalEvidence,
    FunctionalEvidence,
    GeneDiseaseValidity,
)
from dismech.clingen.go_annotations import (
    GeneGOAnnotations,
    GOAnnotation,
    GOAnnotationFetcher,
    compare_clingen_to_go,
    get_experimental_evidence_codes,
)
from dismech.clingen.go_mapper import (
    GOMapping,
    get_all_go_mappings,
    get_go_mappings_for_category,
    get_go_mappings_for_keywords,
)

__all__ = [
    "ClinGenClient",
    "ExperimentalEvidence",
    "FunctionalEvidence",
    "GOAnnotation",
    "GOAnnotationFetcher",
    "GOMapping",
    "GeneDiseaseValidity",
    "GeneGOAnnotations",
    "compare_clingen_to_go",
    "get_all_go_mappings",
    "get_experimental_evidence_codes",
    "get_go_mappings_for_category",
    "get_go_mappings_for_keywords",
]
