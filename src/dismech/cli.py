"""Top-level CLI entry points for dismech utilities."""

from __future__ import annotations

from pathlib import Path

import typer

from dismech.claims import (
    default_claim_input_paths,
    extract_claim_rows_from_files,
    write_claim_rows,
)
from dismech.compare.support import default_kb_dir

app = typer.Typer(help="dismech command-line tools.")


@app.callback()
def app_callback() -> None:
    """Top-level dismech CLI group."""


@app.command("extract-claims")
def extract_claims_command(
    disorder_yaml: Path | None = typer.Argument(
        None,
        exists=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        help="Path to a disorder YAML file.",
    ),
    all_: bool = typer.Option(
        False,
        "--all",
        help="Extract claims from every disorder YAML in the knowledge base.",
    ),
    out: Path | None = typer.Option(
        None,
        "--out",
        "-o",
        resolve_path=True,
        help="Write CSV output to this path instead of stdout.",
    ),
    kb_dir: Path = typer.Option(
        ...,
        "--kb-dir",
        default_factory=default_kb_dir,
        exists=True,
        file_okay=False,
        dir_okay=True,
        resolve_path=True,
        help="Directory containing disorder YAML files for --all mode.",
    ),
) -> None:
    """Extract disease claims and their evidence as flat CSV rows."""
    if all_ == (disorder_yaml is not None):
        raise typer.BadParameter("Provide either a disorder YAML path or --all.")

    paths = default_claim_input_paths(kb_dir) if all_ else [disorder_yaml]
    rows = extract_claim_rows_from_files([path for path in paths if path is not None])

    if out is None:
        write_claim_rows(rows, typer.get_text_stream("stdout"))
        return

    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as stream:
        write_claim_rows(rows, stream)


@app.command("pathograph-thumbnail")
def pathograph_thumbnail_command(
    disorder_yaml: Path = typer.Argument(
        ...,
        exists=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        help="Path to a disorder YAML file.",
    ),
    out: Path | None = typer.Option(
        None,
        "--out",
        "-o",
        resolve_path=True,
        help="Write the SVG to this path instead of stdout.",
    ),
) -> None:
    """Draw a disorder's pathograph as a label-free SVG thumbnail."""
    from dismech.graph import build_causal_graph
    from dismech.pathograph_thumbnail import render_thumbnail
    from dismech.yaml_io import safe_load_path

    thumbnail = render_thumbnail(build_causal_graph(safe_load_path(disorder_yaml)))
    if out is None:
        typer.echo(thumbnail.svg)
    else:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(thumbnail.svg, encoding="utf-8")
    typer.echo(
        f"{thumbnail.edges} causal edges, "
        f"{thumbnail.phenotypes_connected}/{thumbnail.phenotypes} phenotypes connected, "
        f"{thumbnail.unconnected} unconnected outcomes",
        err=True,
    )


@app.command("hdruk-definition")
def hdruk_definition_command(
    phenotype_ids: list[str] = typer.Argument(
        ..., help="HDR UK phenotype ids, e.g. PH304 or HDRUK:PH304."
    ),
    detail_json: Path | None = typer.Option(
        None,
        "--detail-json",
        exists=True,
        dir_okay=False,
        help="Offline: a saved detail payload (one id only).",
    ),
    codes_json: Path | None = typer.Option(
        None,
        "--codes-json",
        exists=True,
        dir_okay=False,
        help="Offline: a saved codes-export payload (one id only).",
    ),
    write_cache: bool = typer.Option(
        True,
        "--write-cache/--no-write-cache",
        help="Also write references_cache/HDRUK_<id>.md.",
    ),
) -> None:
    """Print a dismech `definitions:` fragment for HDR UK phenotype(s).

    Fetches each record from the HDR UK Phenotype Library API (or reads the
    saved payloads), writes its HDRUK: reference cache file so the fragment's
    evidence and code lists verify, and prints the fragment as YAML.
    """
    import json

    import yaml

    from dismech.computable_phenotypes import definition_from_hdruk
    from dismech.repo_root import repo_root
    from dismech.structured_sources.hdruk import HDRUKSource, entry_for, parse_record

    if (detail_json is None) != (codes_json is None):
        raise typer.BadParameter("--detail-json and --codes-json go together.")
    if detail_json is not None and len(phenotype_ids) != 1:
        raise typer.BadParameter("Saved payloads describe one phenotype; give one id.")
    cache_dir = repo_root() / "references_cache"
    source = HDRUKSource(repo_root() / "data" / "hdruk", cache_dir=cache_dir)
    definitions = []
    for phenotype_id in phenotype_ids:
        if detail_json is not None and codes_json is not None:
            record = parse_record(
                json.loads(detail_json.read_text(encoding="utf-8")),
                json.loads(codes_json.read_text(encoding="utf-8")),
            )
        else:
            record = source.fetch(phenotype_id)
        if write_cache:
            entry = entry_for(record)
            cache_dir.mkdir(parents=True, exist_ok=True)
            (cache_dir / entry.filename()).write_text(entry.render(), encoding="utf-8")
        definitions.append(definition_from_hdruk(record))
    typer.echo(
        yaml.safe_dump(
            {"definitions": definitions}, sort_keys=False, allow_unicode=True, width=100
        ),
        nl=False,
    )


@app.command("check-codelists")
def check_codelists_command(
    paths: list[Path] | None = typer.Argument(
        None, help="KB files to check; default: every file under kb/."
    ),
) -> None:
    """Check every CodeList in the KB against its code system and cached source.

    Fails (exit 1) when a code's prefix is not its list's code_system, a code
    is malformed for its system, a code or its label is absent from the cited
    source_reference, or that source is not cached.
    """
    from dismech import kb_cache
    from dismech.computable_phenotypes import check_document, iter_code_lists
    from dismech.repo_root import repo_root

    root = repo_root()
    if paths:
        files = list(paths)
    else:
        kb_cache.default_off()
        # Only a file that spells the slot can hold a code list; skipping the
        # rest avoids parsing the whole corpus (~25 s -> ~1 s).
        files = [
            p
            for p in sorted((root / "kb").rglob("*.yaml"))
            if "code_lists:" in p.read_text(encoding="utf-8")
        ]
    findings = []
    lists = 0
    for path in files:
        doc = kb_cache.load_document(path)
        file_findings = check_document(
            doc, path, root / "references_cache", root / "cache"
        )
        findings.extend(file_findings)
        lists += sum(1 for _ in iter_code_lists(doc))
    for finding in findings:
        typer.echo(finding.format())
    typer.echo(
        f"{len(files)} files scanned, {lists} code lists, {len(findings)} findings",
        err=True,
    )
    if findings:
        raise typer.Exit(code=1)


def main() -> None:
    app()


if __name__ == "__main__":
    main()
