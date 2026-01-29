"""Map ClinGen functional evidence categories to GO terms.

ClinGen uses functional evidence categories that can be mapped to GO terms:
- Biochemical Function → GO:0003674 (molecular_function) and descendants
- Protein Interaction → GO:0005515 (protein binding) and related terms
- Expression → GO:0010467 (gene expression) and related terms
- Functional Alteration → context-dependent GO terms
- Model Systems → model organism phenotypes (may link to GO annotations)
"""

from dataclasses import dataclass


@dataclass
class GOMapping:
    """A mapping from ClinGen evidence to GO term."""

    go_id: str
    go_label: str
    evidence_category: str
    mapping_type: str  # "direct", "inferred", "keyword"
    confidence: str  # "high", "medium", "low"
    notes: str | None = None


# Core mappings from ClinGen experimental evidence categories to GO terms
CATEGORY_GO_MAPPINGS = {
    "Biochemical Function": [
        GOMapping(
            go_id="GO:0003674",
            go_label="molecular_function",
            evidence_category="Biochemical Function",
            mapping_type="direct",
            confidence="high",
            notes="Root term for molecular function - specific term depends on enzyme/activity type",
        ),
        GOMapping(
            go_id="GO:0003824",
            go_label="catalytic activity",
            evidence_category="Biochemical Function",
            mapping_type="inferred",
            confidence="medium",
            notes="When evidence describes enzymatic activity",
        ),
    ],
    "Protein Interaction": [
        GOMapping(
            go_id="GO:0005515",
            go_label="protein binding",
            evidence_category="Protein Interaction",
            mapping_type="direct",
            confidence="high",
        ),
        GOMapping(
            go_id="GO:0006461",
            go_label="protein complex assembly",
            evidence_category="Protein Interaction",
            mapping_type="inferred",
            confidence="medium",
            notes="When evidence describes complex formation",
        ),
    ],
    "Expression": [
        GOMapping(
            go_id="GO:0010467",
            go_label="gene expression",
            evidence_category="Expression",
            mapping_type="direct",
            confidence="high",
        ),
        GOMapping(
            go_id="GO:0006412",
            go_label="translation",
            evidence_category="Expression",
            mapping_type="inferred",
            confidence="medium",
            notes="When evidence describes protein expression levels",
        ),
    ],
    "Functional Alteration": [
        GOMapping(
            go_id="GO:0003674",
            go_label="molecular_function",
            evidence_category="Functional Alteration",
            mapping_type="inferred",
            confidence="low",
            notes="Requires context to determine specific GO term",
        ),
    ],
    "Model Systems": [
        GOMapping(
            go_id="GO:0008150",
            go_label="biological_process",
            evidence_category="Model Systems",
            mapping_type="inferred",
            confidence="low",
            notes="Model organism phenotypes may relate to GO biological processes",
        ),
    ],
}


# Keyword to GO term mappings
KEYWORD_GO_MAPPINGS: dict[str, list[GOMapping]] = {
    "kinase": [
        GOMapping(
            go_id="GO:0016301",
            go_label="kinase activity",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="high",
        ),
        GOMapping(
            go_id="GO:0016310",
            go_label="phosphorylation",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="high",
        ),
    ],
    "phosphatase": [
        GOMapping(
            go_id="GO:0016791",
            go_label="phosphatase activity",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="high",
        ),
        GOMapping(
            go_id="GO:0016311",
            go_label="dephosphorylation",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="high",
        ),
    ],
    "protease": [
        GOMapping(
            go_id="GO:0008233",
            go_label="peptidase activity",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="high",
        ),
        GOMapping(
            go_id="GO:0006508",
            go_label="proteolysis",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="high",
        ),
    ],
    "transcription": [
        GOMapping(
            go_id="GO:0006351",
            go_label="DNA-templated transcription",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="high",
        ),
    ],
    "translation": [
        GOMapping(
            go_id="GO:0006412",
            go_label="translation",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="high",
        ),
    ],
    "binding": [
        GOMapping(
            go_id="GO:0005488",
            go_label="binding",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="medium",
        ),
    ],
    "transport": [
        GOMapping(
            go_id="GO:0006810",
            go_label="transport",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="medium",
        ),
    ],
    "transporter": [
        GOMapping(
            go_id="GO:0005215",
            go_label="transporter activity",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="high",
        ),
    ],
    "signaling": [
        GOMapping(
            go_id="GO:0023052",
            go_label="signaling",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="medium",
        ),
    ],
    "signal transduction": [
        GOMapping(
            go_id="GO:0007165",
            go_label="signal transduction",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="high",
        ),
    ],
    "apoptosis": [
        GOMapping(
            go_id="GO:0006915",
            go_label="apoptotic process",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="high",
        ),
    ],
    "autophagy": [
        GOMapping(
            go_id="GO:0006914",
            go_label="autophagy",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="high",
        ),
    ],
    "cell cycle": [
        GOMapping(
            go_id="GO:0007049",
            go_label="cell cycle",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="high",
        ),
    ],
    "dna repair": [
        GOMapping(
            go_id="GO:0006281",
            go_label="DNA repair",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="high",
        ),
    ],
    "metabolism": [
        GOMapping(
            go_id="GO:0008152",
            go_label="metabolic process",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="medium",
        ),
    ],
    "biosynthesis": [
        GOMapping(
            go_id="GO:0009058",
            go_label="biosynthetic process",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="medium",
        ),
    ],
    "catabolism": [
        GOMapping(
            go_id="GO:0009056",
            go_label="catabolic process",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="medium",
        ),
    ],
    "oxidoreductase": [
        GOMapping(
            go_id="GO:0016491",
            go_label="oxidoreductase activity",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="high",
        ),
    ],
    "transferase": [
        GOMapping(
            go_id="GO:0016740",
            go_label="transferase activity",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="high",
        ),
    ],
    "hydrolase": [
        GOMapping(
            go_id="GO:0016787",
            go_label="hydrolase activity",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="high",
        ),
    ],
    "ligase": [
        GOMapping(
            go_id="GO:0016874",
            go_label="ligase activity",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="high",
        ),
    ],
    "receptor": [
        GOMapping(
            go_id="GO:0038023",
            go_label="signaling receptor activity",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="medium",
        ),
    ],
    "channel": [
        GOMapping(
            go_id="GO:0005216",
            go_label="ion channel activity",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="medium",
        ),
    ],
    "ion channel": [
        GOMapping(
            go_id="GO:0005216",
            go_label="ion channel activity",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="high",
        ),
    ],
    "mitochondri": [
        GOMapping(
            go_id="GO:0005739",
            go_label="mitochondrion",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="medium",
        ),
    ],
    "nucleus": [
        GOMapping(
            go_id="GO:0005634",
            go_label="nucleus",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="high",
        ),
    ],
    "cytoplasm": [
        GOMapping(
            go_id="GO:0005737",
            go_label="cytoplasm",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="high",
        ),
    ],
    "membrane": [
        GOMapping(
            go_id="GO:0016020",
            go_label="membrane",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="medium",
        ),
    ],
    "plasma membrane": [
        GOMapping(
            go_id="GO:0005886",
            go_label="plasma membrane",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="high",
        ),
    ],
    "endoplasmic reticulum": [
        GOMapping(
            go_id="GO:0005783",
            go_label="endoplasmic reticulum",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="high",
        ),
    ],
    "golgi": [
        GOMapping(
            go_id="GO:0005794",
            go_label="Golgi apparatus",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="high",
        ),
    ],
    "lysosom": [
        GOMapping(
            go_id="GO:0005764",
            go_label="lysosome",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="high",
        ),
    ],
    "ubiquitin": [
        GOMapping(
            go_id="GO:0016567",
            go_label="protein ubiquitination",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="high",
        ),
    ],
    "glycosylation": [
        GOMapping(
            go_id="GO:0006486",
            go_label="protein glycosylation",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="high",
        ),
    ],
    "methylation": [
        GOMapping(
            go_id="GO:0032259",
            go_label="methylation",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="medium",
        ),
    ],
    "acetylation": [
        GOMapping(
            go_id="GO:0006473",
            go_label="protein acetylation",
            evidence_category="keyword",
            mapping_type="keyword",
            confidence="medium",
        ),
    ],
}


def get_go_mappings_for_category(category: str) -> list[GOMapping]:
    """Get GO term mappings for a ClinGen evidence category."""
    return CATEGORY_GO_MAPPINGS.get(category, [])


def get_go_mappings_for_keywords(text: str) -> list[GOMapping]:
    """Extract GO term mappings from keywords found in text."""
    mappings = []
    text_lower = text.lower()

    for keyword, keyword_mappings in KEYWORD_GO_MAPPINGS.items():
        if keyword in text_lower:
            mappings.extend(keyword_mappings)

    return mappings


def get_all_go_mappings(
    category: str | None = None,
    text: str | None = None,
) -> list[GOMapping]:
    """Get all GO term mappings for a combination of category and text.

    Args:
        category: ClinGen evidence category (e.g., "Biochemical Function")
        text: Free text to search for keywords

    Returns:
        List of GOMapping objects, deduplicated by GO ID.
    """
    mappings = []

    if category:
        mappings.extend(get_go_mappings_for_category(category))

    if text:
        mappings.extend(get_go_mappings_for_keywords(text))

    # Deduplicate by GO ID, keeping highest confidence
    seen = {}
    for mapping in mappings:
        if mapping.go_id not in seen:
            seen[mapping.go_id] = mapping
        else:
            # Keep higher confidence mapping
            confidence_order = {"high": 3, "medium": 2, "low": 1}
            if confidence_order.get(mapping.confidence, 0) > confidence_order.get(
                seen[mapping.go_id].confidence, 0
            ):
                seen[mapping.go_id] = mapping

    return list(seen.values())
