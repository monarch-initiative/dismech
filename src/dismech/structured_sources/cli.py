"""CLI for structured-database reference sources.

Exposes operations to refresh bulk data and (re)build cache files.

    uv run python -m dismech.structured_sources.cli refresh orphanet
    uv run python -m dismech.structured_sources.cli rebuild orphanet
    uv run python -m dismech.structured_sources.cli rebuild orphanet --id 558
    uv run python -m dismech.structured_sources.cli rebuild clingen --id CGGV:assertion_...
    uv run python -m dismech.structured_sources.cli rebuild clingen-dosage --id HGNC:25662
"""

from __future__ import annotations

import logging
from pathlib import Path

import typer

from dismech.structured_sources.base import StructuredSource
from dismech.structured_sources.clingen import ClinGenSource
from dismech.structured_sources.clingen_dosage import ClinGenDosageSource
from dismech.structured_sources.clingen_yaml_audit import (
    audit_clingen_yaml,
    format_summary,
    format_tsv,
)
from dismech.structured_sources.orphanet import OrphanetSource

app = typer.Typer(help="dismech structured-database source utilities.")

_REPO_ROOT = Path(__file__).resolve().parents[3]
_DEFAULT_DATA_DIR = _REPO_ROOT / "data"
_DEFAULT_CACHE_DIR = _REPO_ROOT / "references_cache"


def _get_source(name: str) -> StructuredSource:
    name = name.lower()
    if name in {"orphanet", "orpha"}:
        manifest = _DEFAULT_DATA_DIR / "orphadata" / "MANIFEST.yaml"
        if manifest.exists():
            OrphanetSource.load_manifest(manifest)
        return OrphanetSource(_DEFAULT_DATA_DIR / "orphadata")
    if name in {"clingen", "cggv"}:
        manifest = _DEFAULT_DATA_DIR / "clingen" / "MANIFEST.yaml"
        if manifest.exists():
            ClinGenSource.load_manifest(manifest)
        return ClinGenSource(_DEFAULT_DATA_DIR / "clingen")
    if name in {"clingen-dosage", "clingen_dosage", "cgds"}:
        manifest = _DEFAULT_DATA_DIR / "clingen-dosage" / "MANIFEST.yaml"
        if manifest.exists():
            ClinGenDosageSource.load_manifest(manifest)
        return ClinGenDosageSource(_DEFAULT_DATA_DIR / "clingen-dosage")
    raise typer.BadParameter(f"unknown source: {name}")


@app.command("refresh")
def refresh_cmd(
    source: str = typer.Argument(..., help="Source name (e.g. 'orphanet')"),
    force: bool = typer.Option(False, "--force", help="Re-download even if cached"),
) -> None:
    """Download bulk-data files for a source and verify checksums."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    src = _get_source(source)
    src.refresh(force=force)
    typer.echo(f"refreshed {source}")


@app.command("rebuild")
def rebuild_cmd(
    source: str = typer.Argument(..., help="Source name"),
    id_: list[str] = typer.Option(
        None, "--id", help="Restrict to specific identifier(s); default: all"
    ),
    include_report_text: bool = typer.Option(
        True,
        "--include-report-text/--csv-only",
        help="For ClinGen sources, include narrative text scraped from reports",
    ),
    cache_dir: Path = typer.Option(
        _DEFAULT_CACHE_DIR, "--cache-dir", help="Output directory"
    ),
    progress_every: int = typer.Option(
        500, "--progress-every", help="Log every N entries"
    ),
) -> None:
    """Regenerate cache files for a source from current bulk data."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    logging.getLogger("httpx").setLevel(logging.WARNING)
    src = _get_source(source)
    if isinstance(src, (ClinGenSource, ClinGenDosageSource)):
        src.include_report_text = include_report_text
    cache_dir.mkdir(parents=True, exist_ok=True)
    if id_:
        targets = list(id_)
    else:
        targets = list(src.identifiers())
    typer.echo(f"rebuilding {len(targets)} {source} entries → {cache_dir}")
    written = 0
    for ident in targets:
        try:
            src.write_cache_file(ident, cache_dir)
        except KeyError as exc:
            typer.echo(f"  skipped {ident}: {exc}", err=True)
            continue
        written += 1
        if written % progress_every == 0:
            typer.echo(f"  ... {written}/{len(targets)}")
    typer.echo(f"wrote {written} cache files")


@app.command("list")
def list_cmd(
    source: str = typer.Argument(..., help="Source name"),
    limit: int = typer.Option(20, "--limit"),
) -> None:
    """List the first N identifiers a source can serialize."""
    src = _get_source(source)
    ids = list(src.identifiers())
    typer.echo(f"{len(ids)} identifiers in {source}")
    for ident in ids[:limit]:
        typer.echo(f"  {ident}")


@app.command("clingen-audit-yaml")
def clingen_audit_yaml_cmd(
    kb_dir: Path = typer.Option(
        _REPO_ROOT / "kb" / "disorders",
        "--kb-dir",
        help="Directory containing disorder YAML files",
    ),
    data_dir: Path = typer.Option(
        _DEFAULT_DATA_DIR / "clingen",
        "--data-dir",
        help="Directory containing ClinGen Gene-Disease Validity bulk data",
    ),
    cache_dir: Path = typer.Option(
        _DEFAULT_CACHE_DIR,
        "--cache-dir",
        help="Reference cache directory used to check CGGV snippets",
    ),
    limit: int = typer.Option(
        20,
        "--limit",
        help="Number of remaining disorder-file examples to print; 0 hides examples",
    ),
    output_format: str = typer.Option(
        "summary",
        "--format",
        help="Output format: summary or tsv",
    ),
    status: list[str] = typer.Option(
        None,
        "--status",
        help="Restrict TSV rows to a status; may be repeated",
    ),
) -> None:
    """Audit ClinGen Gene-Disease Validity coverage in disorder YAML."""

    manifest = data_dir / "MANIFEST.yaml"
    if manifest.exists():
        ClinGenSource.load_manifest(manifest)
    summary = audit_clingen_yaml(
        kb_dir=kb_dir,
        data_dir=data_dir,
        cache_dir=cache_dir,
    )
    if output_format == "summary":
        typer.echo(format_summary(summary, limit=limit))
    elif output_format == "tsv":
        typer.echo(format_tsv(summary, statuses=status))
    else:
        raise typer.BadParameter("--format must be 'summary' or 'tsv'")


def main() -> None:
    app()


if __name__ == "__main__":
    main()
