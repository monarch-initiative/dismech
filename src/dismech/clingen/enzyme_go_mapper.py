"""Extract enzyme names from ClinGen evidence and map to GO terms.

This module provides a more precise GO term extraction by:
1. Identifying enzyme names from text (words ending in -ase, -lyase, etc.)
2. Searching GO for matching molecular function terms
3. Returning specific GO terms rather than generic ones
"""

import re
import time
from dataclasses import dataclass

import httpx

# QuickGO API endpoint
QUICKGO_SEARCH_URL = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/search"

# Enzyme suffix patterns (must end with these)
ENZYME_SUFFIXES = [
    "dehydrogenase", "transferase", "kinase", "phosphatase", "synthase",
    "synthetase", "lyase", "ligase", "hydrolase", "oxidase", "reductase",
    "isomerase", "mutase", "deaminase", "aminase", "transporter",
    "protease", "peptidase", "esterase", "amidase", "glucosidase",
    "galactosidase", "mannosidase", "sulfatase", "carboxylase",
    "decarboxylase", "cyclase", "phosphorylase", "racemase", "epimerase",
    "permease", "translocase", "helicase", "gyrase", "topoisomerase",
    "polymerase", "nuclease", "endonuclease", "exonuclease", "ribonuclease",
]

# Build regex patterns from suffixes
ENZYME_PATTERNS = [
    # Multi-word enzyme names (e.g., "isobutyryl-CoA dehydrogenase")
    r"\b([\w-]+(?:\s+[\w-]+)*\s+(?:" + "|".join(ENZYME_SUFFIXES) + r"))\b",
    # Single word enzyme names ending in standard suffixes
    r"\b(\w*(?:" + "|".join(ENZYME_SUFFIXES) + r"))\b",
    # Activity phrases
    r"\b([\w-]+(?:\s+[\w-]+)?)\s+activity\b",
]

# Words to exclude (too generic or not enzymes)
EXCLUDE_WORDS = {
    "disease", "case", "base", "increase", "decrease", "release",
    "phase", "please", "these", "those", "whose", "cause", "because",
    "purpose", "otherwise", "database", "metabase", "purchase",
}


@dataclass
class EnzymeGOMapping:
    """A mapping from an enzyme name to a GO term."""

    enzyme_name: str
    go_id: str
    go_name: str
    source_text: str  # The original text where enzyme was found
    confidence: float  # 0-1 based on how well the GO term matches


def extract_enzyme_names(text: str) -> list[str]:
    """Extract potential enzyme names from text.

    Args:
        text: Text to search for enzyme names.

    Returns:
        List of potential enzyme names.
    """
    enzymes = set()
    text_lower = text.lower()

    for pattern in ENZYME_PATTERNS:
        matches = re.findall(pattern, text_lower)
        for match in matches:
            # Clean up the match
            enzyme = match.strip()

            # Skip excluded words
            if enzyme in EXCLUDE_WORDS:
                continue

            # Skip very short matches
            if len(enzyme) < 4:
                continue

            # Skip if doesn't look like an enzyme (must contain enzyme suffix)
            if not any(enzyme.endswith(suffix) for suffix in ENZYME_SUFFIXES):
                # Also check for general -ase ending
                if not enzyme.endswith("ase"):
                    continue

            enzymes.add(enzyme)

    return list(enzymes)


def search_go_for_enzyme(
    enzyme_name: str,
    rate_limit_delay: float = 0.3,
) -> list[tuple[str, str, float]]:
    """Search GO for terms matching an enzyme name.

    Args:
        enzyme_name: Enzyme name to search for.
        rate_limit_delay: Delay between API requests.

    Returns:
        List of (go_id, go_name, confidence) tuples.
    """
    time.sleep(rate_limit_delay)

    # Try different search strategies
    search_queries = [
        f"{enzyme_name} activity",
        enzyme_name,
    ]

    results = []
    seen_ids = set()

    with httpx.Client(timeout=30.0) as client:
        for query in search_queries:
            params = {"query": query, "limit": 5}

            response = client.get(
                QUICKGO_SEARCH_URL,
                params=params,
                headers={"Accept": "application/json"},
            )

            if response.status_code != 200:
                continue

            data = response.json()
            for result in data.get("results", []):
                go_id = result.get("id", "")
                go_name = result.get("name", "")

                if go_id in seen_ids:
                    continue
                seen_ids.add(go_id)

                # Calculate confidence based on name similarity
                confidence = calculate_match_confidence(enzyme_name, go_name)
                results.append((go_id, go_name, confidence))

            # If we found good matches, don't try other queries
            if any(conf > 0.7 for _, _, conf in results):
                break

    # Sort by confidence
    results.sort(key=lambda x: x[2], reverse=True)
    return results


def calculate_match_confidence(enzyme_name: str, go_name: str) -> float:
    """Calculate how well a GO term matches an enzyme name.

    Args:
        enzyme_name: The enzyme name from the text.
        go_name: The GO term name.

    Returns:
        Confidence score 0-1.
    """
    enzyme_lower = enzyme_name.lower()
    go_lower = go_name.lower()

    # Exact match
    if enzyme_lower in go_lower:
        return 0.95

    # Check word overlap
    enzyme_words = set(enzyme_lower.split())
    go_words = set(go_lower.split())

    # Remove common words
    common_words = {"activity", "the", "a", "an", "of", "in", "to"}
    enzyme_words -= common_words
    go_words -= common_words

    if not enzyme_words or not go_words:
        return 0.1

    overlap = len(enzyme_words & go_words)
    total = len(enzyme_words | go_words)

    return overlap / total if total > 0 else 0.0


def map_evidence_to_go(
    evidence_text: str,
    rate_limit_delay: float = 0.3,
) -> list[EnzymeGOMapping]:
    """Map ClinGen evidence text to GO terms.

    Args:
        evidence_text: The biochemical function evidence text.
        rate_limit_delay: Delay between API requests.

    Returns:
        List of EnzymeGOMapping objects.
    """
    # Extract enzyme names
    enzymes = extract_enzyme_names(evidence_text)

    mappings = []
    for enzyme in enzymes:
        # Search GO for this enzyme
        results = search_go_for_enzyme(enzyme, rate_limit_delay)

        # Take the best match if confidence is good enough
        if results:
            go_id, go_name, confidence = results[0]
            if confidence > 0.3:  # Threshold for accepting a match
                mappings.append(
                    EnzymeGOMapping(
                        enzyme_name=enzyme,
                        go_id=go_id,
                        go_name=go_name,
                        source_text=evidence_text[:200],
                        confidence=confidence,
                    )
                )

    return mappings


def main():
    """Test the enzyme mapper."""
    # Example evidence texts from ClinGen
    test_cases = [
        (
            "ADA",
            "Presented the first characterization of ADA activity, catalyzing the "
            "hydrolytic deamination of adenosine to inosine, within the lysosomal "
            "compartment of human fibroblasts."
        ),
        (
            "ACAD8",
            "ACAD8 encodes Isobutyryl-CoA dehydrogenase which catalyzes the 3rd step "
            "in the degradation of valine."
        ),
        (
            "ABCA3",
            "ABCA3 encodes the ATP-binding cassette phospholipid transporter, which "
            "is required for the normal organization and packaging of surfactant "
            "phospholipids into specialized secretory organelles."
        ),
    ]

    for gene, evidence in test_cases:
        print(f"\n{'='*60}")
        print(f"Gene: {gene}")
        print(f"Evidence: {evidence[:100]}...")

        mappings = map_evidence_to_go(evidence)

        if mappings:
            print("\nGO Mappings:")
            for m in mappings:
                print(f"  {m.enzyme_name} → {m.go_id}: {m.go_name} (conf: {m.confidence:.2f})")
        else:
            print("\nNo enzyme mappings found")


if __name__ == "__main__":
    main()
