"""Fetch GO annotations for genes in ClinGen curations.

This module uses the QuickGO API and UniProt to fetch GO annotations
for genes referenced in ClinGen gene-disease validity curations.
"""

import time
from dataclasses import dataclass, field

import httpx

# QuickGO API endpoint
QUICKGO_BASE_URL = "https://www.ebi.ac.uk/QuickGO/services"


@dataclass
class GOAnnotation:
    """A GO annotation for a gene/protein."""

    go_id: str
    go_name: str
    aspect: str  # F (molecular function), P (biological process), C (cellular component)
    evidence_code: str
    gene_symbol: str | None = None
    uniprot_id: str | None = None
    reference: str | None = None
    qualifier: str | None = None


@dataclass
class GeneGOAnnotations:
    """All GO annotations for a gene."""

    gene_symbol: str
    hgnc_id: str | None = None
    uniprot_ids: list[str] = field(default_factory=list)
    annotations: list[GOAnnotation] = field(default_factory=list)

    @property
    def molecular_functions(self) -> list[GOAnnotation]:
        """Get molecular function annotations."""
        return [a for a in self.annotations if a.aspect == "F"]

    @property
    def biological_processes(self) -> list[GOAnnotation]:
        """Get biological process annotations."""
        return [a for a in self.annotations if a.aspect == "P"]

    @property
    def cellular_components(self) -> list[GOAnnotation]:
        """Get cellular component annotations."""
        return [a for a in self.annotations if a.aspect == "C"]


class GOAnnotationFetcher:
    """Fetches GO annotations for genes using QuickGO API."""

    def __init__(self, rate_limit_delay: float = 0.5):
        """Initialize the fetcher.

        Args:
            rate_limit_delay: Delay between API requests in seconds.
        """
        self.rate_limit_delay = rate_limit_delay
        self._client = httpx.Client(timeout=30.0, follow_redirects=True)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self._client.close()

    def close(self):
        """Close the HTTP client."""
        self._client.close()

    def get_uniprot_id_for_gene(self, gene_symbol: str, taxon: int = 9606) -> str | None:
        """Get the primary UniProt ID for a human gene symbol.

        Args:
            gene_symbol: Gene symbol (e.g., "BRCA1")
            taxon: NCBI taxonomy ID (default: 9606 for human)

        Returns:
            Primary UniProt ID or None if not found.
        """
        time.sleep(self.rate_limit_delay)

        url = "https://rest.uniprot.org/uniprotkb/search"
        params = {
            "query": f"gene:{gene_symbol} AND organism_id:{taxon} AND reviewed:true",
            "format": "json",
            "size": 1,
        }

        response = self._client.get(url, params=params)
        if response.status_code != 200:
            return None

        data = response.json()
        results = data.get("results", [])
        if results:
            return results[0].get("primaryAccession")

        return None

    def get_go_annotations_for_uniprot(
        self,
        uniprot_id: str,
        evidence_codes: list[str] | None = None,
    ) -> list[GOAnnotation]:
        """Get GO annotations for a UniProt ID using QuickGO.

        Args:
            uniprot_id: UniProt accession (e.g., "P38398")
            evidence_codes: Filter by specific GO evidence codes (e.g., ["IDA", "IPI"])
                          Note: These are GO evidence codes (IDA, IPI, etc.), not ECO codes

        Returns:
            List of GO annotations.
        """
        time.sleep(self.rate_limit_delay)

        url = f"{QUICKGO_BASE_URL}/annotation/search"
        params: dict = {
            "geneProductId": uniprot_id,
            "taxonId": 9606,  # Human
            "limit": 100,  # QuickGO max is 100 per page
        }

        if evidence_codes:
            # QuickGO uses goEvidence parameter with comma-separated values
            params["goEvidence"] = ",".join(evidence_codes)

        response = self._client.get(url, params=params, headers={"Accept": "application/json"})
        if response.status_code != 200:
            return []

        data = response.json()
        annotations = []

        for result in data.get("results", []):
            # Get GO aspect abbreviation
            aspect = result.get("goAspect", "")
            if aspect == "biological_process":
                aspect = "P"
            elif aspect == "molecular_function":
                aspect = "F"
            elif aspect == "cellular_component":
                aspect = "C"

            annotations.append(
                GOAnnotation(
                    go_id=result.get("goId", ""),
                    go_name=result.get("goName") or "(name not provided)",
                    aspect=aspect,
                    evidence_code=result.get("goEvidence", ""),
                    gene_symbol=result.get("symbol"),
                    uniprot_id=uniprot_id,
                    reference=result.get("reference"),
                    qualifier=result.get("qualifier"),
                )
            )

        return annotations

    def get_annotations_for_gene(
        self,
        gene_symbol: str,
        hgnc_id: str | None = None,
        evidence_codes: list[str] | None = None,
    ) -> GeneGOAnnotations:
        """Get all GO annotations for a gene.

        Args:
            gene_symbol: Gene symbol (e.g., "BRCA1")
            hgnc_id: Optional HGNC ID
            evidence_codes: Filter by evidence codes

        Returns:
            GeneGOAnnotations with all annotations.
        """
        result = GeneGOAnnotations(gene_symbol=gene_symbol, hgnc_id=hgnc_id)

        # Get UniProt ID
        uniprot_id = self.get_uniprot_id_for_gene(gene_symbol)
        if not uniprot_id:
            return result

        result.uniprot_ids.append(uniprot_id)

        # Get GO annotations
        annotations = self.get_go_annotations_for_uniprot(uniprot_id, evidence_codes)
        result.annotations = annotations

        return result


def get_experimental_evidence_codes() -> list[str]:
    """Get a list of experimental GO evidence codes.

    These are the evidence codes that indicate experimental support,
    which are most relevant for comparing with ClinGen functional evidence.

    Note: EXP is a deprecated code; the specific subtypes are used instead.
    """
    return [
        "IDA",  # Inferred from Direct Assay
        "IPI",  # Inferred from Physical Interaction
        "IMP",  # Inferred from Mutant Phenotype
        "IGI",  # Inferred from Genetic Interaction
        "IEP",  # Inferred from Expression Pattern
        "HTP",  # Inferred from High Throughput Experiment
        "HDA",  # Inferred from High Throughput Direct Assay
        "HMP",  # Inferred from High Throughput Mutant Phenotype
        "HGI",  # Inferred from High Throughput Genetic Interaction
        "HEP",  # Inferred from High Throughput Expression Pattern
    ]


def compare_clingen_to_go(
    gene_symbol: str,
    clingen_go_mappings: list[str],
    go_annotations: GeneGOAnnotations,
) -> dict:
    """Compare ClinGen-inferred GO terms with actual GO annotations.

    Args:
        gene_symbol: Gene symbol
        clingen_go_mappings: GO terms inferred from ClinGen evidence
        go_annotations: Actual GO annotations from QuickGO

    Returns:
        Dictionary with comparison results.
    """
    clingen_go_ids = set(clingen_go_mappings)
    actual_go_ids = {a.go_id for a in go_annotations.annotations}

    # Find overlaps
    overlapping = clingen_go_ids & actual_go_ids
    clingen_only = clingen_go_ids - actual_go_ids
    actual_only = actual_go_ids - clingen_go_ids

    return {
        "gene_symbol": gene_symbol,
        "clingen_go_count": len(clingen_go_ids),
        "actual_go_count": len(actual_go_ids),
        "overlapping_count": len(overlapping),
        "overlapping_terms": list(overlapping),
        "clingen_only_terms": list(clingen_only),
        "actual_only_count": len(actual_only),
        "precision": len(overlapping) / len(clingen_go_ids) if clingen_go_ids else 0,
        "recall": len(overlapping) / len(actual_go_ids) if actual_go_ids else 0,
    }
