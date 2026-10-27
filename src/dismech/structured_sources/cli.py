"""CLI for structured-database reference sources.

Exposes operations to refresh bulk data and (re)build cache files.

    uv run python -m dismech.structured_sources.cli refresh orphanet
    uv run python -m dismech.structured_sources.cli rebuild orphanet
    uv run python -m dismech.structured_sources.cli rebuild orphanet --id 558
    uv run python -m dismech.structured_sources.cli rebuild clingen --id CGGV:assertion_...
    uv run python -m dismech.structured_sources.cli rebuild clingen-dosage --id HGNC:25662
    uv run python -m dismech.structured_sources.cli rebuild civic --id CIVIC_EID:260

``data/``, ``references_cache/`` and ``kb/disorders/`` default to the checkout
containing the working directory, or to ``$DISMECH_ROOT`` when that is set
(see ``dismech.repo_root``).
"""

from __future__ import annotations

import logging
from pathlib import Path

import typer

from dismech.repo_root import is_in_working_tree, repo_root
from dismech.structured_sources.base import (
    ChecksumMismatchError,
    MissingBulkDataError,
    StructuredSource,
    repin_manifest,
)
from dismech.structured_sources.civic import CivicSource
from dismech.structured_sources.clingen import ClinGenSource
from dismech.structured_sources.clingen_dosage import ClinGenDosageSource
from dismech.structured_sources.clingen_yaml_audit import (
    audit_clingen_yaml,
    format_summary,
    format_tsv,
)
from dismech.structured_sources.icees import ICEESSource
from dismech.structured_sources.ictrp import ICTRPSource
from dismech.structured_sources.mygeneset import MyGenesetSource
from dismech.structured_sources.ontology_edges import OntologyEdgeSource
from dismech.structured_sources.orphanet import OrphanetSource
from dismech.structured_sources.strchive import StrchiveSource

app = typer.Typer(help="dismech structured-database source utilities.")


# Resolved at call time from the working directory, never from this file's
# location: with a virtualenv shared across git worktrees, ``__file__`` is in
# the primary checkout, and every rebuild run in a worktree wrote there while
# reporting success (#15051). See ``dismech.repo_root``.
def _data_dir() -> Path:
    return repo_root() / "data"


def _cache_dir() -> Path:
    return repo_root() / "references_cache"


def _kb_dir() -> Path:
    return repo_root() / "kb" / "disorders"


def _warn_if_outside_working_tree(path: Path, what: str) -> None:
    """Name the destination when a default directory is not in this tree."""
    if not is_in_working_tree(path):
        typer.echo(
            f"warning: {what} {path} is outside the tree this command was run "
            f"in ({Path.cwd()}); pass an explicit directory or unset DISMECH_ROOT "
            "if that is not intended.",
            err=True,
        )


_MANIFEST_DIRS: dict[str, str] = {
    "orphanet": "orphadata",
    "orpha": "orphadata",
    "clingen": "clingen",
    "cggv": "clingen",
    "clingen-dosage": "clingen-dosage",
    "clingen_dosage": "clingen-dosage",
    "cgds": "clingen-dosage",
    "civic": "civic",
    "civicdb": "civic",
    "mygeneset": "genesets",
    "genesets": "genesets",
    "geneset": "genesets",
    "icees": "icees-kg",
    "icees-kg": "icees-kg",
    "icees_kg": "icees-kg",
    "strchive": "strchive",
    "str": "strchive",
    "strchive-loci": "strchive",
    "ncit": "ncit-edges",
    "ncit-edges": "ncit-edges",
    "ncit_edges": "ncit-edges",
}


def _manifest_path(name: str) -> Path | None:
    """The MANIFEST.yaml pinning ``name``'s bulk files, if it has one."""
    subdir = _MANIFEST_DIRS.get(name.lower())
    if subdir is None:
        return None
    path = _data_dir() / subdir / "MANIFEST.yaml"
    return path if path.exists() else None


def _get_source(name: str) -> StructuredSource:
    name = name.lower()
    data_dir = _data_dir()
    if name in {"orphanet", "orpha"}:
        manifest = data_dir / "orphadata" / "MANIFEST.yaml"
        if manifest.exists():
            OrphanetSource.load_manifest(manifest)
        return OrphanetSource(data_dir / "orphadata")
    if name in {"clingen", "cggv"}:
        manifest = data_dir / "clingen" / "MANIFEST.yaml"
        if manifest.exists():
            ClinGenSource.load_manifest(manifest)
        return ClinGenSource(data_dir / "clingen")
    if name in {"clingen-dosage", "clingen_dosage", "cgds"}:
        manifest = data_dir / "clingen-dosage" / "MANIFEST.yaml"
        if manifest.exists():
            ClinGenDosageSource.load_manifest(manifest)
        return ClinGenDosageSource(data_dir / "clingen-dosage")
    if name in {"civic", "civicdb"}:
        manifest = data_dir / "civic" / "MANIFEST.yaml"
        if manifest.exists():
            CivicSource.load_manifest(manifest)
        return CivicSource(data_dir / "civic")
    if name in {"mygeneset", "genesets", "geneset"}:
        manifest = data_dir / "genesets" / "MANIFEST.yaml"
        if manifest.exists():
            MyGenesetSource.load_manifest(manifest)
        return MyGenesetSource(data_dir / "genesets")
    if name in {"icees", "icees-kg", "icees_kg"}:
        manifest = data_dir / "icees-kg" / "MANIFEST.yaml"
        if manifest.exists():
            ICEESSource.load_manifest(manifest)
        return ICEESSource(data_dir / "icees-kg")
    if name in {"strchive", "str", "strchive-loci"}:
        manifest = data_dir / "strchive" / "MANIFEST.yaml"
        if manifest.exists():
            StrchiveSource.load_manifest(manifest)
        return StrchiveSource(data_dir / "strchive")
    if name in {"ictrp", "who-ictrp", "chictr"}:
        # No bulk file: ICTRP records are fetched per identifier on demand, so
        # the cache directory *is* the index of what this source knows about.
        return ICTRPSource(data_dir / "ictrp", cache_dir=_cache_dir())
    if name in {"ncit", "ncit-edges", "ncit_edges"}:
        manifest = data_dir / "ncit-edges" / "MANIFEST.yaml"
        if not manifest.exists():
            raise typer.BadParameter(f"manifest not found: {manifest}")
        OntologyEdgeSource.load_manifest(manifest)
        return OntologyEdgeSource(data_dir / "ncit-edges")
    raise typer.BadParameter(f"unknown source: {name}")


@app.command("refresh")
def refresh_cmd(
    source: str = typer.Argument(..., help="Source name (e.g. 'orphanet')"),
    force: bool = typer.Option(False, "--force", help="Re-download even if cached"),
    repin: bool = typer.Option(
        False,
        "--repin",
        help=(
            "Accept a new upstream release: record the downloaded files' "
            "checksums in the manifest instead of failing. Leaves a diff to review."
        ),
    ),
) -> None:
    """Download bulk-data files for a source and verify checksums.

    Most of these manifests pin a checksum against an unversioned upstream URL,
    so the pin goes stale every time upstream publishes. `--repin` is the
    supported way through that: it writes the new checksums (and snapshot date)
    into the manifest so the fix is one command and one reviewable diff, rather
    than a manual download-and-hand-edit.
    """
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    _warn_if_outside_working_tree(_data_dir(), "download directory")
    src = _get_source(source)
    try:
        changes = src.refresh(force=force, repin=repin)
    except ChecksumMismatchError as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=1) from exc

    if repin and not changes:
        # `refresh` skips the download entirely when a local file already matches
        # the pin, so `--repin` on an up-to-date checkout has nothing to record.
        # Say so: a silent no-op reads like the repin failed.
        typer.echo(
            "--repin: nothing to repin. Every bulk file either matches the pinned "
            "checksum already or was re-downloaded and still matches, so the "
            "manifest is current.\n"
            "If you expected a change, the local copy may predate the upstream "
            "release; re-run with --force to download regardless."
        )

    if changes:
        manifest = _manifest_path(source)
        if manifest is None:
            raise typer.BadParameter(
                f"--repin: no manifest found for source {source!r}; "
                "nothing to write the new checksums into."
            )
        notes = repin_manifest(manifest, changes)
        typer.echo(f"repinned {manifest}:")
        for note in notes:
            typer.echo(f"  {note}")
        typer.echo(
            "\nReview the manifest diff, then rebuild the cache "
            "(e.g. `just structured-rebuild-orphanet`) and review that diff too."
        )
    typer.echo(f"refreshed {source}")


def _rebuild(
    src: StructuredSource,
    id_: list[str] | None,
    source: str,
    cache_dir: Path,
    progress_every: int,
) -> tuple[int, list[str], list[str]]:
    """Write cache files; return (written, skipped ids, targets)."""
    targets = list(id_) if id_ else list(src.identifiers())
    typer.echo(f"rebuilding {len(targets)} {source} entries → {cache_dir}")
    written = 0
    skipped: list[str] = []
    for ident in targets:
        try:
            src.write_cache_file(ident, cache_dir)
        except KeyError as exc:
            typer.echo(f"  skipped {ident}: {exc}", err=True)
            skipped.append(ident)
            continue
        written += 1
        if written % progress_every == 0:
            typer.echo(f"  ... {written}/{len(targets)}")
    return written, skipped, targets


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
    cache_dir: Path | None = typer.Option(
        None,
        "--cache-dir",
        help="Output directory (default: references_cache/ in this checkout)",
    ),
    progress_every: int = typer.Option(
        500, "--progress-every", help="Log every N entries"
    ),
    csv: Path | None = typer.Option(
        None,
        "--csv",
        help=(
            "ClinGen gene validity only: read this export instead of "
            "data/clingen/gene_validity.csv (or the committed fallback). The "
            "cache file is stamped with this file's own date and sha256."
        ),
    ),
) -> None:
    """Regenerate cache files for a source from current bulk data."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    logging.getLogger("httpx").setLevel(logging.WARNING)
    if cache_dir is None:
        cache_dir = _cache_dir()
        _warn_if_outside_working_tree(cache_dir, "cache directory")
    src = _get_source(source)
    if isinstance(src, (ClinGenSource, ClinGenDosageSource)):
        src.include_report_text = include_report_text
    if csv is not None:
        if not isinstance(src, ClinGenSource):
            raise typer.BadParameter("--csv is only supported for the clingen source")
        src.csv_path = csv
    cache_dir.mkdir(parents=True, exist_ok=True)
    try:
        written, skipped, targets = _rebuild(
            src, id_, source, cache_dir, progress_every
        )
    except MissingBulkDataError as exc:
        # The message names the refresh command; a traceback buries it (#13941).
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=1) from exc
    typer.echo(f"wrote {written} cache files")
    if id_ and skipped:
        # An explicitly requested id that is not in the export is a failure,
        # not a quiet skip: `just fetch-reference` routes here, agents read its
        # exit code, and a typo or a withdrawn assertion must not look like
        # success (review on #13766). The ids that did resolve are written.
        typer.echo(
            f"{len(skipped)} of {len(targets)} requested id(s) not found in the "
            f"{source} export: " + ", ".join(skipped),
            err=True,
        )
        raise typer.Exit(code=1)


@app.command("list")
def list_cmd(
    source: str = typer.Argument(..., help="Source name"),
    limit: int = typer.Option(20, "--limit"),
) -> None:
    """List the first N identifiers a source can serialize."""
    src = _get_source(source)
    try:
        ids = list(src.identifiers())
    except MissingBulkDataError as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=1) from exc
    typer.echo(f"{len(ids)} identifiers in {source}")
    for ident in ids[:limit]:
        typer.echo(f"  {ident}")


@app.command("align")
def align_cmd(
    disease: str = typer.Argument(..., help="Disorder name or path to its YAML"),
    gene_set: str = typer.Argument(
        ..., help="Gene set id, e.g. KEGG_ASTHMA or MYGENESET:KEGG_ASTHMA"
    ),
    kb_dir: Path | None = typer.Option(
        None,
        "--kb-dir",
        help="Disorder YAML directory (default: kb/disorders/ in this checkout)",
    ),
    cache_dir: Path | None = typer.Option(
        None,
        "--cache-dir",
        help="Reference cache directory (default: references_cache/ in this checkout)",
    ),
    no_hierarchy: bool = typer.Option(
        False, "--no-hierarchy", help="Exact GO-id match only (skip the OAK GO adapter)"
    ),
) -> None:
    """Align a gene set's curated BPs to a disorder's pathograph BPs."""
    from dismech import genesets_align as ga

    kb_dir = kb_dir or _kb_dir()
    cache_dir = cache_dir or _cache_dir()

    # Resolve the disorder file (accept a name or a path).
    disease_path = Path(disease)
    if not disease_path.exists():
        disease_path = kb_dir / f"{disease}.yaml"
    if not disease_path.exists():
        raise typer.BadParameter(f"disorder not found: {disease}")
    disease_name = disease_path.stem

    local_id = ga_local_id(gene_set)
    cache_path = cache_dir / f"MYGENESET_{local_id}.md"
    if not cache_path.exists():
        raise typer.BadParameter(
            f"no cache file {cache_path.name}; run `just genesets-rebuild` first"
        )

    set_bps = ga.read_set_bps(cache_path)
    pathograph_bps = ga.extract_pathograph_bps(disease_path)

    adapter = None
    if not no_hierarchy:
        try:
            from oaklib import get_adapter

            adapter = get_adapter("sqlite:obo:go")
        except Exception as exc:  # pragma: no cover - degrade to exact match
            typer.echo(f"(GO adapter unavailable, exact-match only: {exc})", err=True)

    result = ga.align(
        f"MYGENESET:{local_id}", disease_name, set_bps, pathograph_bps, adapter
    )
    typer.echo(ga.format_report(result))


def ga_local_id(gene_set: str) -> str:
    return MyGenesetSource.local_id_from_gene_set_id(gene_set)


@app.command("align-all")
def align_all_cmd(
    kb_dir: Path | None = typer.Option(
        None,
        "--kb-dir",
        help="Disorder YAML directory (default: kb/disorders/ in this checkout)",
    ),
    cache_dir: Path | None = typer.Option(
        None,
        "--cache-dir",
        help="Reference cache directory (default: references_cache/ in this checkout)",
    ),
    no_hierarchy: bool = typer.Option(
        False, "--no-hierarchy", help="Exact GO-id match only (skip the OAK GO adapter)"
    ),
) -> None:
    """Align every disease-context gene set to its dismech disorder (by MONDO)."""
    from dismech import genesets_align as ga

    kb_dir = kb_dir or _kb_dir()
    cache_dir = cache_dir or _cache_dir()

    adapter = None
    if not no_hierarchy:
        try:
            from oaklib import get_adapter

            adapter = get_adapter("sqlite:obo:go")
        except Exception as exc:  # pragma: no cover - degrade to exact match
            typer.echo(f"(GO adapter unavailable, exact-match only: {exc})", err=True)

    entries = ga.sweep(cache_dir, kb_dir, adapter)
    typer.echo(ga.format_sweep(entries))


@app.command("clingen-audit-yaml")
def clingen_audit_yaml_cmd(
    kb_dir: Path | None = typer.Option(
        None,
        "--kb-dir",
        help="Directory containing disorder YAML files (default: kb/disorders/)",
    ),
    data_dir: Path | None = typer.Option(
        None,
        "--data-dir",
        help=(
            "Directory containing ClinGen Gene-Disease Validity bulk data "
            "(default: data/clingen/)"
        ),
    ),
    cache_dir: Path | None = typer.Option(
        None,
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

    kb_dir = kb_dir or _kb_dir()
    data_dir = data_dir or _data_dir() / "clingen"
    cache_dir = cache_dir or _cache_dir()
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
