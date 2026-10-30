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


def main() -> None:
    app()


if __name__ == "__main__":
    main()
