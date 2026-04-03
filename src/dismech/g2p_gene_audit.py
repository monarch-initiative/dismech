"""Backward-compatible wrapper around the G2P comparison module."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import typer

from .compare_support import default_kb_dir
from .g2p_compare import compare_gene
from .g2p_compare import load_g2p_index
from .g2p_compare import survey_genes
from .g2p_compare import build_dismech_gene_index
from .g2p_compare import compute_release_overview
from .g2p_compare import write_batch_summary
from .g2p_compare import write_summary

__all__ = ["app", "audit", "compare_gene", "load_g2p_index", "survey_genes"]

app = typer.Typer(help="Audit G2P gene rows against dismech disease coverage.")


@app.command()
def audit(
    gene_symbols: list[str] = typer.Argument(
        help="One or more HGNC gene symbols to audit."
    ),
    g2p_source: str | None = typer.Option(
        None,
        "--g2p-source",
        help="Path or URL to a G2P CSV/CSV.GZ export. Defaults to the latest allG2P FTP release.",
    ),
    kb_dir: Path = typer.Option(
        default_kb_dir(),
        "--kb-dir",
        help="Path to kb/disorders.",
    ),
    format: str = typer.Option(
        "summary",
        "--format",
        help="Output format: summary or json.",
    ),
    output: Path | None = typer.Option(
        None,
        "--output",
        help="Optional output file path. Defaults to stdout.",
    ),
) -> None:
    """Compatibility CLI for the first-pass G2P audit workflow."""
    resolved_source, rows_by_gene = load_g2p_index(g2p_source)
    dismech_matches_by_gene = build_dismech_gene_index(kb_dir)
    reports = [
        compare_gene(
            gene_symbol,
            kb_dir=kb_dir,
            g2p_source=resolved_source,
            g2p_rows_by_gene=rows_by_gene,
            resolved_g2p_source=resolved_source,
            dismech_matches_by_gene=dismech_matches_by_gene,
        )
        for gene_symbol in gene_symbols
    ]

    out_stream = output.open("w", encoding="utf-8") if output else None
    try:
        if format == "summary":
            if len(reports) == 1:
                write_summary(reports[0], file=out_stream)
            else:
                summaries = [report["summary"] for report in reports]
                overview = compute_release_overview(reports, summaries)
                write_batch_summary(
                    overview,
                    summaries,
                    g2p_source=resolved_source,
                    top=len(summaries),
                    file=out_stream,
                )
        elif format == "json":
            out = out_stream or typer.get_text_stream("stdout")
            payload: Any = reports[0] if len(reports) == 1 else reports
            json.dump(payload, out, indent=2)
            out.write("\n")
        else:
            raise typer.BadParameter("format must be one of: summary, json")
    finally:
        if out_stream:
            out_stream.close()


if __name__ == "__main__":
    app()
