"""Command line for gene pages: ``python -m dismech.genes <command>``."""

from __future__ import annotations

import csv
import json
import logging
import sys
from pathlib import Path

import typer

from dismech.genes.render import MIN_DISORDERS_FOR_PAGE

app = typer.Typer(help="Gene pages: ingest, KB slice, curated summaries, rendering.")


@app.command("ingest-refresh")
def ingest_refresh_cmd(
    repin: bool = typer.Option(
        False, "--repin", help="Accept new upstream releases and rewrite the manifests."
    ),
    force: bool = typer.Option(
        False, "--force", help="Re-download HGNC even if the checksum matches."
    ),
) -> None:
    """Fetch the pinned HGNC and ClinGen files and ai-gene-review commit into data/."""
    from dismech.genes.ingest import (
        refresh_ai_gene_review,
        refresh_clingen,
        refresh_hgnc,
    )

    for label, notes in (
        ("data/hgnc/MANIFEST.yaml", refresh_hgnc(force=force, repin=repin)),
        ("data/clingen-genes/MANIFEST.yaml", refresh_clingen(force=force, repin=repin)),
        ("data/ai-gene-review/MANIFEST.yaml", refresh_ai_gene_review(repin=repin)),
    ):
        for note in notes:
            typer.echo(f"repinned {label}: {note}")
    if repin:
        typer.echo("Now run `just genes-ingest-build` and review both diffs together.")


@app.command("ingest-build")
def ingest_build_cmd() -> None:
    """Rewrite kb/genes/ingest/*.tsv for every gene the KB names or curates."""
    from dismech import kb_cache
    from dismech.genes.ingest import build_ingest

    kb_cache.default_off()
    report = build_ingest()
    for line in report.lines():
        typer.echo(line)


@app.command("slice")
def slice_cmd(
    gene: list[str] = typer.Argument(
        None, help="hgnc:<n> CURIEs; omit for every gene."
    ),
    fmt: str = typer.Option("summary", "--format", help="summary | tsv | json"),
    min_disorders: int = typer.Option(1, "--min-disorders"),
) -> None:
    """Print what the KB says about a gene (computed from kb/, never committed)."""
    from dismech.genes.slice import build_gene_index, normalize_hgnc_id

    index = build_gene_index()
    wanted = {normalize_hgnc_id(g) for g in gene} if gene else None
    genes = [
        g
        for g in sorted(index.values(), key=lambda s: (-len(s.entries()), s.label))
        if (wanted is None or g.hgnc_id in wanted) and len(g.entries()) >= min_disorders
    ]
    if fmt == "tsv":
        writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
        writer.writerow(
            [
                "hgnc_id",
                "symbol",
                "entry_kind",
                "entry",
                "section",
                "item",
                "slots",
                "relationship_type",
                "subtype",
                "functional_impact_category",
                "variant_origin",
            ]
        )
        for g in genes:
            for o in g.occurrences:
                writer.writerow(
                    [
                        g.hgnc_id,
                        g.label,
                        o.entry_kind,
                        o.entry_name,
                        o.section,
                        o.item_name,
                        "|".join(o.slots),
                        o.details.get("relationship_type", ""),
                        o.details.get("subtype", ""),
                        o.details.get("functional_impact_category", ""),
                        o.details.get("variant_origin", ""),
                    ]
                )
    elif fmt == "json":
        payload = [
            {
                "hgnc_id": g.hgnc_id,
                "symbol": g.label,
                "disorders": g.entries(),
                "modules": g.modules(),
                "relationship_types": g.relationship_types(),
            }
            for g in genes
        ]
        typer.echo(json.dumps(payload, indent=2))
    else:
        for g in genes:
            typer.echo(
                f"{g.hgnc_id}\t{g.label}\t{len(g.entries())} disorders\t"
                f"{', '.join(g.relationship_types()) or '-'}"
            )


@app.command("clingen-gaps")
def clingen_gaps_cmd(
    fmt: str = typer.Option("summary", "--format", help="summary | tsv"),
    classification: list[str] = typer.Option(
        None,
        "--classification",
        help="Only these ClinGen tiers, e.g. Definitive (repeatable).",
    ),
) -> None:
    """Entries ClinGen classifies a gene for whose own record does not type it.

    Report-only. Each row is a curation lead, not a defect: typing the record
    means reading the ClinGen assertion and the entry, and some pairs (a
    Disputed or Refuted tier) are reasons *not* to add a causal claim.
    """
    from collections import Counter

    from dismech.genes.ingest import load_ingest
    from dismech.genes.join import (
        NO_GENETIC_RECORD,
        NOT_NAMED,
        UNTYPED,
        clingen_matches,
    )
    from dismech.genes.slice import build_gene_index, entry_mondo_index

    wanted = {c.lower() for c in classification} if classification else None
    index, mondo, ingest = build_gene_index(), entry_mondo_index(), load_ingest()
    rows = []
    for hgnc_id, gene in sorted(index.items(), key=lambda kv: kv[1].label):
        for match in clingen_matches(gene, ingest.clingen.get(hgnc_id, []), mondo):
            if wanted and match.classification.lower() not in wanted:
                continue
            for entry, status in match.entries.items():
                if status in {UNTYPED, NO_GENETIC_RECORD, NOT_NAMED}:
                    rows.append((gene.label, hgnc_id, entry, status, match))
    if fmt == "tsv":
        writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
        writer.writerow(
            [
                "symbol",
                "hgnc_id",
                "entry",
                "kb_status",
                "clingen_disease",
                "mondo_id",
                "moi",
                "classification",
                "assertion_id",
            ]
        )
        for symbol, hgnc_id, entry, status, m in rows:
            writer.writerow(
                [
                    symbol,
                    hgnc_id,
                    entry,
                    status,
                    m.row["disease_label"],
                    m.row["mondo_id"],
                    m.row["moi"],
                    m.classification,
                    m.row["assertion_id"],
                ]
            )
        return
    counts = Counter((status, m.classification) for _s, _h, _e, status, m in rows)
    typer.echo(
        f"{len(rows)} entry-gene pairs ClinGen classifies that the entry does not type"
    )
    for (status, tier), n in sorted(counts.items(), key=lambda kv: -kv[1]):
        typer.echo(f"  {n:5d}  {status:18s} {tier}")
    typer.echo(
        "Use --format tsv for the worklist, --classification Definitive to narrow it."
    )


@app.command("verify")
def verify_cmd(
    paths: list[Path] = typer.Argument(
        None, help="Curated summaries; omit for all of kb/genes/curated/."
    ),
    strict: bool = typer.Option(
        False, "--strict", help="Exit 1 if any summary fails or errors."
    ),
) -> None:
    """Re-run every provedown claim in the curated summaries against the KB."""
    from dismech.genes.curated import CURATED_DIR, verify_summary

    files = list(paths) if paths else sorted(CURATED_DIR.glob("*.md"))
    failed = 0
    for path in files:
        result = verify_summary(path)
        typer.echo(result.line())
        for finding in result.problems:
            typer.echo(f"    {finding}")
        failed += not result.ok
    typer.echo(f"{len(files) - failed}/{len(files)} summaries verified")
    if strict and failed:
        raise typer.Exit(1)


@app.command("render")
def render_cmd(
    output_dir: Path = typer.Option(Path("pages/genes"), "--output-dir"),
    min_disorders: int = typer.Option(
        MIN_DISORDERS_FOR_PAGE,
        "--min-disorders",
        help="Full page threshold; others are index rows.",
    ),
    gene: list[str] = typer.Option(
        None, "--gene", help="Render only these hgnc:<n> pages (plus the index)."
    ),
    verify: bool = typer.Option(
        True, "--verify/--no-verify", help="Run provedown on curated summaries."
    ),
) -> None:
    """Render pages/genes/: one page per gene plus the index."""
    from dismech.genes.render import render_gene_pages

    written = render_gene_pages(
        output_dir=output_dir,
        min_disorders=min_disorders,
        only=gene or None,
        verify=verify,
    )
    typer.echo(f"Wrote {len(written) - 1} gene pages and the index to {output_dir}")


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    app()


if __name__ == "__main__":
    main()
