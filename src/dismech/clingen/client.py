"""ClinGen gene-disease validity client.

Provides access to ClinGen gene-disease validity curations with support for
extracting experimental evidence and searching for GO term references.
"""

import csv
import re
import time
from dataclasses import dataclass, field
from io import StringIO
from pathlib import Path
from typing import Iterator

import httpx
from bs4 import BeautifulSoup

# ClinGen endpoints
CLINGEN_GDV_CSV_URL = "https://search.clinicalgenome.org/kb/gene-validity/download"
CLINGEN_BASE_URL = "https://search.clinicalgenome.org"

# GO term pattern: GO:0000000 format
GO_TERM_PATTERN = re.compile(r"\bGO:\d{7}\b")

# Keywords that suggest GO-relevant functional evidence
GO_RELEVANT_KEYWORDS = [
    "gene ontology",
    "molecular function",
    "biological process",
    "cellular component",
    "catalytic activity",
    "binding",
    "transporter activity",
    "enzyme",
    "kinase",
    "phosphatase",
    "protease",
    "ligase",
    "transferase",
    "hydrolase",
    "oxidoreductase",
    "signaling",
    "signal transduction",
    "transcription",
    "translation",
    "protein folding",
    "protein transport",
    "cell cycle",
    "apoptosis",
    "autophagy",
    "metabolism",
    "biosynthesis",
    "catabolism",
]


@dataclass
class FunctionalEvidence:
    """A single piece of functional evidence from a ClinGen curation."""

    category: str  # e.g., "Biochemical Function", "Protein Interaction"
    subcategory: str | None = None  # e.g., "A" or "B" for biochemical function
    label: str | None = None  # e.g., gene/protein name
    explanation: str | None = None
    pmids: list[str] = field(default_factory=list)
    points: float = 0.0
    go_terms: list[str] = field(default_factory=list)  # Extracted GO terms
    go_relevant_keywords: list[str] = field(default_factory=list)  # Matched keywords


@dataclass
class ExperimentalEvidence:
    """Experimental evidence summary from a ClinGen gene-disease validity curation."""

    total_points: float = 0.0
    max_points: float = 6.0
    function_evidence: list[FunctionalEvidence] = field(default_factory=list)
    model_organism_evidence: list[FunctionalEvidence] = field(default_factory=list)
    rescue_evidence: list[FunctionalEvidence] = field(default_factory=list)
    raw_text: str | None = None  # Full experimental evidence section text


@dataclass
class GeneDiseaseValidity:
    """A ClinGen gene-disease validity curation record."""

    gene_symbol: str
    gene_hgnc_id: str
    disease_label: str
    disease_mondo_id: str
    mode_of_inheritance: str
    sop_version: str
    classification: str
    report_url: str
    classification_date: str
    expert_panel: str
    curation_id: str | None = None
    experimental_evidence: ExperimentalEvidence | None = None
    summary_text: str | None = None


class ClinGenClient:
    """Client for accessing ClinGen gene-disease validity data."""

    def __init__(
        self,
        cache_dir: Path | None = None,
        rate_limit_delay: float = 0.5,
    ):
        """Initialize the ClinGen client.

        Args:
            cache_dir: Directory to cache downloaded data. If None, no caching.
            rate_limit_delay: Delay between requests in seconds to avoid rate limiting.
        """
        self.cache_dir = Path(cache_dir) if cache_dir else None
        self.rate_limit_delay = rate_limit_delay
        self._client = httpx.Client(timeout=30.0, follow_redirects=True)

        if self.cache_dir:
            self.cache_dir.mkdir(parents=True, exist_ok=True)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self._client.close()

    def close(self):
        """Close the HTTP client."""
        self._client.close()

    def download_curations_csv(self, force: bool = False) -> str:
        """Download the gene-disease validity curations CSV.

        Args:
            force: If True, re-download even if cached.

        Returns:
            CSV content as string.
        """
        cache_file = self.cache_dir / "gene_validity.csv" if self.cache_dir else None

        if cache_file and cache_file.exists() and not force:
            return cache_file.read_text()

        response = self._client.get(CLINGEN_GDV_CSV_URL)
        response.raise_for_status()
        content = response.text

        if cache_file:
            cache_file.write_text(content)

        return content

    def iter_curations(self, force_download: bool = False) -> Iterator[GeneDiseaseValidity]:
        """Iterate over all gene-disease validity curations.

        Args:
            force_download: If True, re-download the CSV.

        Yields:
            GeneDiseaseValidity objects.
        """
        csv_content = self.download_curations_csv(force=force_download)
        reader = csv.reader(StringIO(csv_content))

        # Skip header rows (4 lines of metadata + header row)
        for _ in range(5):
            next(reader, None)

        for row in reader:
            if len(row) < 10:
                continue

            # Skip empty or separator rows
            if not row[0] or row[0].startswith("+"):
                continue

            yield GeneDiseaseValidity(
                gene_symbol=row[0],
                gene_hgnc_id=row[1],
                disease_label=row[2],
                disease_mondo_id=row[3],
                mode_of_inheritance=row[4],
                sop_version=row[5],
                classification=row[6],
                report_url=row[7],
                classification_date=row[8],
                expert_panel=row[9],
            )

    def get_curation_count(self) -> int:
        """Get the total number of curations."""
        return sum(1 for _ in self.iter_curations())

    def fetch_curation_details(
        self,
        curation: GeneDiseaseValidity,
    ) -> GeneDiseaseValidity:
        """Fetch detailed information for a curation by scraping the report page.

        Args:
            curation: The curation to fetch details for.

        Returns:
            Updated curation with experimental evidence details.
        """
        time.sleep(self.rate_limit_delay)

        response = self._client.get(curation.report_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Extract curation ID
        curation_id_elem = soup.find(string=re.compile(r"CCID:\d+"))
        if curation_id_elem:
            match = re.search(r"CCID:(\d+)", str(curation_id_elem))
            if match:
                curation.curation_id = f"CCID:{match.group(1)}"

        # Extract summary text
        summary_section = soup.find("div", class_="card-body")
        if summary_section:
            summary_p = summary_section.find("p")
            if summary_p:
                curation.summary_text = summary_p.get_text(strip=True)

        # Parse experimental evidence
        curation.experimental_evidence = self._parse_experimental_evidence(soup)

        return curation

    def _parse_experimental_evidence(self, soup: BeautifulSoup) -> ExperimentalEvidence:
        """Parse experimental evidence section from the curation page."""
        evidence = ExperimentalEvidence()

        # Find experimental evidence section
        exp_section = soup.find("div", id="tag_experimental_evidence")
        if not exp_section:
            return evidence

        # Extract total points
        points_text = exp_section.find(string=re.compile(r"Total Points:"))
        if points_text:
            match = re.search(r"Total Points:\s*([\d.]+)", str(points_text))
            if match:
                evidence.total_points = float(match.group(1))

        # Extract raw text for keyword searching
        evidence.raw_text = exp_section.get_text()

        # Parse the evidence table
        table = exp_section.find("table")
        if table:
            evidence.function_evidence = self._parse_evidence_table(table)

        return evidence

    def _parse_evidence_table(self, table) -> list[FunctionalEvidence]:
        """Parse the experimental evidence table."""
        evidence_list = []

        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if len(cells) < 2:
                continue

            # Look for category indicators
            category_cell = None
            for cell in cells:
                strong = cell.find("strong")
                if strong:
                    text = strong.get_text(strip=True)
                    if text in [
                        "Biochemical Function",
                        "Protein Interaction",
                        "Expression",
                        "Functional Alteration",
                        "Model Systems",
                        "Rescue",
                    ]:
                        category_cell = cell
                        break

            if not category_cell:
                continue

            func_ev = FunctionalEvidence(
                category=category_cell.find("strong").get_text(strip=True)
            )

            # Extract explanation text
            for cell in cells:
                p_tags = cell.find_all("p")
                for p in p_tags:
                    text = p.get_text(strip=True)
                    if text and len(text) > 20:
                        func_ev.explanation = text
                        break

            # Extract PMIDs
            pmid_links = row.find_all("a", href=re.compile(r"pubmed\.ncbi\.nlm\.nih\.gov"))
            for link in pmid_links:
                pmid_match = re.search(r"(\d{7,8})", link.get("href", ""))
                if pmid_match:
                    func_ev.pmids.append(f"PMID:{pmid_match.group(1)}")

            # Search for GO terms in explanation
            if func_ev.explanation:
                func_ev.go_terms = GO_TERM_PATTERN.findall(func_ev.explanation)

                # Search for GO-relevant keywords
                explanation_lower = func_ev.explanation.lower()
                func_ev.go_relevant_keywords = [
                    kw for kw in GO_RELEVANT_KEYWORDS if kw in explanation_lower
                ]

            if func_ev.category:
                evidence_list.append(func_ev)

        return evidence_list

    def search_go_references(
        self,
        limit: int | None = None,
        classification_filter: list[str] | None = None,
    ) -> Iterator[tuple[GeneDiseaseValidity, list[str]]]:
        """Search curations for GO term references or GO-relevant functional evidence.

        Args:
            limit: Maximum number of curations to process.
            classification_filter: Only include curations with these classifications.

        Yields:
            Tuples of (curation, list of GO terms or relevant keywords found).
        """
        count = 0
        for curation in self.iter_curations():
            if limit and count >= limit:
                break

            if classification_filter and curation.classification not in classification_filter:
                continue

            # Fetch detailed evidence
            curation = self.fetch_curation_details(curation)

            go_references = []

            # Check experimental evidence
            if curation.experimental_evidence:
                ev = curation.experimental_evidence

                # Check raw text for GO terms
                if ev.raw_text:
                    go_references.extend(GO_TERM_PATTERN.findall(ev.raw_text))

                # Check individual function evidence
                for func_ev in ev.function_evidence:
                    go_references.extend(func_ev.go_terms)
                    # Also include GO-relevant keywords
                    go_references.extend(
                        [f"KEYWORD:{kw}" for kw in func_ev.go_relevant_keywords]
                    )

            # Check summary text
            if curation.summary_text:
                go_references.extend(GO_TERM_PATTERN.findall(curation.summary_text))

            if go_references:
                yield curation, list(set(go_references))

            count += 1

    def get_curations_with_experimental_evidence(
        self,
        categories: list[str] | None = None,
        limit: int | None = None,
    ) -> Iterator[GeneDiseaseValidity]:
        """Get curations that have specific types of experimental evidence.

        Args:
            categories: Filter by evidence categories (e.g., ["Biochemical Function"])
            limit: Maximum number of curations to return.

        Yields:
            GeneDiseaseValidity objects with experimental evidence.
        """
        count = 0
        for curation in self.iter_curations():
            if limit and count >= limit:
                break

            curation = self.fetch_curation_details(curation)

            if not curation.experimental_evidence:
                continue

            if categories:
                has_category = any(
                    ev.category in categories
                    for ev in curation.experimental_evidence.function_evidence
                )
                if not has_category:
                    continue

            yield curation
            count += 1


def main():
    """CLI entry point for testing."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Query ClinGen gene-disease validity for GO references"
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Maximum curations to process",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=Path("cache/clingen"),
        help="Cache directory",
    )
    parser.add_argument(
        "--search-go",
        action="store_true",
        help="Search for GO term references",
    )
    parser.add_argument(
        "--list-curations",
        action="store_true",
        help="List all curations",
    )
    parser.add_argument(
        "--classification",
        type=str,
        nargs="*",
        help="Filter by classification (e.g., Definitive Strong)",
    )

    args = parser.parse_args()

    with ClinGenClient(cache_dir=args.cache_dir) as client:
        if args.list_curations:
            for curation in client.iter_curations():
                print(
                    f"{curation.gene_symbol}\t{curation.disease_label}\t"
                    f"{curation.classification}"
                )

        elif args.search_go:
            print("Searching for GO references in ClinGen curations...")
            print("-" * 80)

            for curation, go_refs in client.search_go_references(
                limit=args.limit,
                classification_filter=args.classification,
            ):
                print(f"\n{curation.gene_symbol} - {curation.disease_label}")
                print(f"  Classification: {curation.classification}")
                print(f"  GO References: {', '.join(go_refs)}")

                if curation.experimental_evidence:
                    for ev in curation.experimental_evidence.function_evidence:
                        print(f"  - {ev.category}: {ev.explanation[:100]}...")
                        if ev.pmids:
                            print(f"    PMIDs: {', '.join(ev.pmids)}")


if __name__ == "__main__":
    main()
