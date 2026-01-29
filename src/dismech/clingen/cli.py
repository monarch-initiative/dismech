"""CLI for querying ClinGen gene-disease validity for GO references.

This tool searches ClinGen curations for:
1. Explicit GO term mentions (GO:XXXXXXX format)
2. GO-relevant functional evidence categories
3. Keywords that map to GO terms
"""

import csv
import json
import sys
from pathlib import Path

import typer

from dismech.clingen.client import ClinGenClient, GeneDiseaseValidity
from dismech.clingen.go_mapper import get_all_go_mappings, GOMapping
from dismech.clingen.go_annotations import (
    GOAnnotationFetcher,
    compare_clingen_to_go,
    get_experimental_evidence_codes,
)

app = typer.Typer(
    name="clingen-go",
    help="Search ClinGen gene-disease validity curations for GO term references",
)


def format_curation_summary(
    curation: GeneDiseaseValidity,
    go_mappings: list[GOMapping],
    verbose: bool = False,
) -> str:
    """Format a curation with its GO mappings for display."""
    lines = [
        f"\n{'='*80}",
        f"Gene: {curation.gene_symbol} ({curation.gene_hgnc_id})",
        f"Disease: {curation.disease_label} ({curation.disease_mondo_id})",
        f"Classification: {curation.classification}",
        f"Expert Panel: {curation.expert_panel}",
    ]

    if curation.curation_id:
        lines.append(f"Curation ID: {curation.curation_id}")

    lines.append(f"\nGO Term Mappings ({len(go_mappings)} found):")

    for mapping in sorted(go_mappings, key=lambda m: m.confidence, reverse=True):
        lines.append(
            f"  {mapping.go_id} - {mapping.go_label} "
            f"[{mapping.mapping_type}:{mapping.confidence}]"
        )

    if verbose and curation.experimental_evidence:
        lines.append("\nExperimental Evidence:")
        for ev in curation.experimental_evidence.function_evidence:
            lines.append(f"  - {ev.category}")
            if ev.explanation:
                # Truncate long explanations
                explanation = ev.explanation[:200]
                if len(ev.explanation) > 200:
                    explanation += "..."
                lines.append(f"    {explanation}")
            if ev.pmids:
                lines.append(f"    PMIDs: {', '.join(ev.pmids)}")

    return "\n".join(lines)


@app.command()
def search(
    limit: int = typer.Option(
        100,
        "--limit",
        "-n",
        help="Maximum number of curations to process",
    ),
    cache_dir: Path = typer.Option(
        Path("cache/clingen"),
        "--cache-dir",
        "-c",
        help="Cache directory for downloaded data",
    ),
    classification: list[str] = typer.Option(
        None,
        "--classification",
        "-C",
        help="Filter by classification (e.g., Definitive, Strong)",
    ),
    category: list[str] = typer.Option(
        None,
        "--category",
        help="Filter by evidence category (e.g., 'Biochemical Function')",
    ),
    min_go_mappings: int = typer.Option(
        1,
        "--min-mappings",
        "-m",
        help="Minimum number of GO mappings to include curation",
    ),
    output_format: str = typer.Option(
        "text",
        "--format",
        "-f",
        help="Output format: text, json, csv",
    ),
    output_file: Path = typer.Option(
        None,
        "--output",
        "-o",
        help="Output file (default: stdout)",
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Show detailed experimental evidence",
    ),
    rate_limit: float = typer.Option(
        0.3,
        "--rate-limit",
        help="Delay between requests in seconds",
    ),
):
    """Search ClinGen curations for GO term references.

    This command downloads ClinGen gene-disease validity curations and
    analyzes them for Gene Ontology (GO) term references. It finds:

    - Explicit GO term mentions (GO:XXXXXXX)
    - GO-relevant keywords in functional evidence descriptions
    - Mappings from evidence categories to GO terms
    """
    results = []

    with ClinGenClient(cache_dir=cache_dir, rate_limit_delay=rate_limit) as client:
        typer.echo(f"Downloading ClinGen gene-disease validity curations...", err=True)

        count = 0
        processed = 0

        for curation in client.iter_curations():
            if limit and count >= limit:
                break

            # Apply classification filter
            if classification and curation.classification not in classification:
                continue

            count += 1
            typer.echo(
                f"\rProcessing {count}: {curation.gene_symbol}...",
                err=True,
                nl=False,
            )

            # Fetch detailed evidence
            curation = client.fetch_curation_details(curation)

            # Collect all GO mappings for this curation
            go_mappings = []

            if curation.experimental_evidence:
                # Apply category filter
                if category:
                    evidence_categories = [
                        e.category
                        for e in curation.experimental_evidence.function_evidence
                    ]
                    if not any(c in evidence_categories for c in category):
                        continue

                for ev in curation.experimental_evidence.function_evidence:
                    # Get mappings from category and explanation text
                    mappings = get_all_go_mappings(
                        category=ev.category,
                        text=ev.explanation,
                    )
                    go_mappings.extend(mappings)

                # Also check raw text for explicit GO terms
                if curation.experimental_evidence.raw_text:
                    import re

                    explicit_gos = re.findall(
                        r"\bGO:\d{7}\b",
                        curation.experimental_evidence.raw_text,
                    )
                    for go_id in explicit_gos:
                        go_mappings.append(
                            GOMapping(
                                go_id=go_id,
                                go_label="(explicit mention)",
                                evidence_category="explicit",
                                mapping_type="direct",
                                confidence="high",
                            )
                        )

            # Deduplicate GO mappings
            seen_go_ids = set()
            unique_mappings = []
            for mapping in go_mappings:
                if mapping.go_id not in seen_go_ids:
                    seen_go_ids.add(mapping.go_id)
                    unique_mappings.append(mapping)

            if len(unique_mappings) >= min_go_mappings:
                results.append((curation, unique_mappings))
                processed += 1

        typer.echo(f"\n\nFound {processed} curations with GO references", err=True)

    # Output results
    output = output_file.open("w") if output_file else sys.stdout

    if output_format == "json":
        json_results = []
        for curation, mappings in results:
            json_results.append({
                "gene_symbol": curation.gene_symbol,
                "gene_hgnc_id": curation.gene_hgnc_id,
                "disease_label": curation.disease_label,
                "disease_mondo_id": curation.disease_mondo_id,
                "classification": curation.classification,
                "expert_panel": curation.expert_panel,
                "curation_id": curation.curation_id,
                "report_url": curation.report_url,
                "go_mappings": [
                    {
                        "go_id": m.go_id,
                        "go_label": m.go_label,
                        "mapping_type": m.mapping_type,
                        "confidence": m.confidence,
                        "evidence_category": m.evidence_category,
                    }
                    for m in mappings
                ],
                "experimental_evidence": (
                    {
                        "total_points": curation.experimental_evidence.total_points,
                        "categories": [
                            {
                                "category": e.category,
                                "explanation": e.explanation,
                                "pmids": e.pmids,
                            }
                            for e in curation.experimental_evidence.function_evidence
                        ],
                    }
                    if curation.experimental_evidence
                    else None
                ),
            })
        json.dump(json_results, output, indent=2)

    elif output_format == "csv":
        writer = csv.writer(output)
        writer.writerow([
            "gene_symbol",
            "gene_hgnc_id",
            "disease_label",
            "disease_mondo_id",
            "classification",
            "go_id",
            "go_label",
            "mapping_type",
            "confidence",
            "evidence_category",
        ])
        for curation, mappings in results:
            for mapping in mappings:
                writer.writerow([
                    curation.gene_symbol,
                    curation.gene_hgnc_id,
                    curation.disease_label,
                    curation.disease_mondo_id,
                    curation.classification,
                    mapping.go_id,
                    mapping.go_label,
                    mapping.mapping_type,
                    mapping.confidence,
                    mapping.evidence_category,
                ])

    else:  # text format
        for curation, mappings in results:
            output.write(format_curation_summary(curation, mappings, verbose))
            output.write("\n")

    if output_file:
        output.close()
        typer.echo(f"Results written to {output_file}", err=True)


@app.command()
def stats(
    cache_dir: Path = typer.Option(
        Path("cache/clingen"),
        "--cache-dir",
        "-c",
        help="Cache directory for downloaded data",
    ),
):
    """Show statistics about ClinGen curations."""
    with ClinGenClient(cache_dir=cache_dir) as client:
        classifications = {}
        sop_versions = {}
        expert_panels = {}

        for curation in client.iter_curations():
            classifications[curation.classification] = (
                classifications.get(curation.classification, 0) + 1
            )
            sop_versions[curation.sop_version] = (
                sop_versions.get(curation.sop_version, 0) + 1
            )
            expert_panels[curation.expert_panel] = (
                expert_panels.get(curation.expert_panel, 0) + 1
            )

        typer.echo("ClinGen Gene-Disease Validity Statistics")
        typer.echo("=" * 50)

        typer.echo(f"\nTotal curations: {sum(classifications.values())}")

        typer.echo("\nBy Classification:")
        for cls, count in sorted(classifications.items(), key=lambda x: -x[1]):
            typer.echo(f"  {cls}: {count}")

        typer.echo("\nBy SOP Version:")
        for sop, count in sorted(sop_versions.items(), key=lambda x: -x[1]):
            typer.echo(f"  {sop}: {count}")

        typer.echo(f"\nExpert Panels: {len(expert_panels)}")
        typer.echo("\nTop 10 Expert Panels:")
        for panel, count in sorted(expert_panels.items(), key=lambda x: -x[1])[:10]:
            typer.echo(f"  {panel}: {count}")


@app.command()
def list_curations(
    limit: int = typer.Option(
        None,
        "--limit",
        "-n",
        help="Maximum number of curations to list",
    ),
    cache_dir: Path = typer.Option(
        Path("cache/clingen"),
        "--cache-dir",
        "-c",
        help="Cache directory",
    ),
    classification: list[str] = typer.Option(
        None,
        "--classification",
        "-C",
        help="Filter by classification",
    ),
):
    """List all gene-disease validity curations."""
    with ClinGenClient(cache_dir=cache_dir) as client:
        count = 0
        for curation in client.iter_curations():
            if classification and curation.classification not in classification:
                continue

            if limit and count >= limit:
                break

            typer.echo(
                f"{curation.gene_symbol}\t{curation.disease_label}\t"
                f"{curation.classification}\t{curation.expert_panel}"
            )
            count += 1


@app.command()
def compare_go(
    gene_symbol: str = typer.Argument(..., help="Gene symbol to compare"),
    experimental_only: bool = typer.Option(
        True,
        "--experimental-only",
        "-e",
        help="Only use experimental GO evidence codes",
    ),
    cache_dir: Path = typer.Option(
        Path("cache/clingen"),
        "--cache-dir",
        "-c",
        help="Cache directory",
    ),
):
    """Compare ClinGen-inferred GO terms with actual GO annotations for a gene.

    This fetches actual GO annotations from QuickGO/UniProt and compares
    them with the GO terms we infer from ClinGen functional evidence.
    """
    # First, find the gene in ClinGen
    typer.echo(f"Looking up {gene_symbol} in ClinGen...")

    with ClinGenClient(cache_dir=cache_dir) as client:
        curation = None
        for c in client.iter_curations():
            if c.gene_symbol.upper() == gene_symbol.upper():
                curation = c
                break

        if not curation:
            typer.echo(f"Gene {gene_symbol} not found in ClinGen curations", err=True)
            raise typer.Exit(1)

        typer.echo(f"Found: {curation.gene_symbol} - {curation.disease_label}")
        typer.echo(f"Classification: {curation.classification}")

        # Fetch detailed evidence
        curation = client.fetch_curation_details(curation)

        # Get ClinGen GO mappings
        go_mappings = []
        if curation.experimental_evidence:
            for ev in curation.experimental_evidence.function_evidence:
                mappings = get_all_go_mappings(
                    category=ev.category,
                    text=ev.explanation,
                )
                go_mappings.extend(mappings)

    clingen_go_ids = list({m.go_id for m in go_mappings})
    typer.echo(f"\nClinGen-inferred GO terms ({len(clingen_go_ids)}):")
    for m in go_mappings:
        typer.echo(f"  {m.go_id} - {m.go_label} [{m.mapping_type}:{m.confidence}]")

    # Fetch actual GO annotations
    typer.echo(f"\nFetching actual GO annotations from QuickGO...")

    with GOAnnotationFetcher() as fetcher:
        evidence_codes = get_experimental_evidence_codes() if experimental_only else None
        annotations = fetcher.get_annotations_for_gene(
            gene_symbol,
            hgnc_id=curation.gene_hgnc_id,
            evidence_codes=evidence_codes,
        )

    if not annotations.annotations:
        typer.echo("No GO annotations found for this gene")
        return

    typer.echo(f"\nActual GO annotations ({len(annotations.annotations)}):")
    typer.echo(f"  UniProt ID: {annotations.uniprot_ids}")
    typer.echo(f"  Molecular Functions: {len(annotations.molecular_functions)}")
    typer.echo(f"  Biological Processes: {len(annotations.biological_processes)}")
    typer.echo(f"  Cellular Components: {len(annotations.cellular_components)}")

    # Sample of each type
    for mf in annotations.molecular_functions[:3]:
        typer.echo(f"    F: {mf.go_id} - {mf.go_name} ({mf.evidence_code})")
    if len(annotations.molecular_functions) > 3:
        typer.echo(f"    ... and {len(annotations.molecular_functions) - 3} more")

    for bp in annotations.biological_processes[:3]:
        typer.echo(f"    P: {bp.go_id} - {bp.go_name} ({bp.evidence_code})")
    if len(annotations.biological_processes) > 3:
        typer.echo(f"    ... and {len(annotations.biological_processes) - 3} more")

    # Compare
    comparison = compare_clingen_to_go(gene_symbol, clingen_go_ids, annotations)

    typer.echo("\n" + "=" * 50)
    typer.echo("Comparison Results:")
    typer.echo(f"  ClinGen-inferred: {comparison['clingen_go_count']} GO terms")
    typer.echo(f"  Actual annotations: {comparison['actual_go_count']} GO terms")
    typer.echo(f"  Overlapping: {comparison['overlapping_count']} GO terms")
    typer.echo(f"  Precision: {comparison['precision']:.2%}")
    typer.echo(f"  Recall: {comparison['recall']:.2%}")

    if comparison["overlapping_terms"]:
        typer.echo("\n  Overlapping terms:")
        for go_id in comparison["overlapping_terms"]:
            typer.echo(f"    {go_id}")


@app.command()
def fetch_go(
    gene_symbol: str = typer.Argument(..., help="Gene symbol to fetch GO annotations for"),
    experimental_only: bool = typer.Option(
        True,
        "--experimental-only",
        "-e",
        help="Only use experimental GO evidence codes",
    ),
):
    """Fetch GO annotations for a gene from QuickGO/UniProt."""
    typer.echo(f"Fetching GO annotations for {gene_symbol}...")

    with GOAnnotationFetcher() as fetcher:
        evidence_codes = get_experimental_evidence_codes() if experimental_only else None
        annotations = fetcher.get_annotations_for_gene(
            gene_symbol,
            evidence_codes=evidence_codes,
        )

    if not annotations.uniprot_ids:
        typer.echo(f"Could not find UniProt ID for {gene_symbol}", err=True)
        raise typer.Exit(1)

    typer.echo(f"UniProt ID: {annotations.uniprot_ids}")
    typer.echo(f"\nTotal annotations: {len(annotations.annotations)}")

    typer.echo(f"\nMolecular Functions ({len(annotations.molecular_functions)}):")
    for mf in annotations.molecular_functions:
        typer.echo(f"  {mf.go_id} - {mf.go_name} ({mf.evidence_code})")

    typer.echo(f"\nBiological Processes ({len(annotations.biological_processes)}):")
    for bp in annotations.biological_processes:
        typer.echo(f"  {bp.go_id} - {bp.go_name} ({bp.evidence_code})")

    typer.echo(f"\nCellular Components ({len(annotations.cellular_components)}):")
    for cc in annotations.cellular_components:
        typer.echo(f"  {cc.go_id} - {cc.go_name} ({cc.evidence_code})")


def main():
    """Entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()
