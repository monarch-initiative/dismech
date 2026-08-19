"""`dismech-stubs` — inspect and maintain the curation stub queue."""

from __future__ import annotations

import json
from pathlib import Path

import typer

from .model import (
    build_coverage_index,
    check_stubs,
    default_stub_dir,
    load_stubs,
)
from .seed import seed_stubs

app = typer.Typer(
    name="dismech-stubs",
    help="Inspect and maintain the curation stub queue under stubs/.",
)

_STUB_DIR_OPTION = typer.Option(
    default_stub_dir(),
    "--stub-dir",
    file_okay=False,
    dir_okay=True,
    resolve_path=True,
    help="Directory holding the stub YAML files.",
)


@app.callback()
def app_callback() -> None:
    """Curation stub queue tools."""


@app.command("check")
def check_command(
    stub_dir: Path = _STUB_DIR_OPTION,
    strict: bool = typer.Option(
        True,
        "--strict/--no-strict",
        help="Exit non-zero when any error is found. Advisories never gate.",
    ),
    show_advisories: bool = typer.Option(
        True,
        "--advisories/--no-advisories",
        help="Also print advisory findings (name collisions with KB entries).",
    ),
) -> None:
    """Check the stub queue's invariants.

    The one that matters: a stub whose MONDO ID is already covered by a
    committed KB entry must be deleted. Curating a disease and leaving its stub
    behind fails here.
    """
    issues = check_stubs(stub_dir)
    errors = [i for i in issues if i.severity == "error"]
    advisories = [i for i in issues if i.severity != "error"]
    count = len(load_stubs(stub_dir))

    for issue in errors:
        typer.echo(issue.format())
    if advisories and show_advisories:
        for issue in advisories:
            typer.echo(issue.format())

    if not errors:
        typer.echo(f"OK: {count} stubs, no errors ({len(advisories)} advisory)")
        return
    typer.echo(f"\n{len(errors)} error(s), {len(advisories)} advisory")
    if strict:
        raise typer.Exit(1)


@app.command("next")
def next_command(
    count: int = typer.Argument(1, min=1, help="How many stubs to show."),
    stub_dir: Path = _STUB_DIR_OPTION,
    include_claimed: bool = typer.Option(
        False, "--include-claimed", help="Also show CLAIMED stubs."
    ),
    alpha: bool = typer.Option(
        False, "--alpha", help="Sort alphabetically within a band instead of by hash."
    ),
    as_json: bool = typer.Option(False, "--json", help="Emit JSON instead of text."),
) -> None:
    """Show the next stubs to curate.

    Ordering is the hand-set `priority` band, then an arbitrary but stable
    spread — there is no computed score, and no ranking within a band. This is a
    pool to choose from, not a recommendation: pick the disease you actually
    know something about rather than the first row.
    """
    wanted = {"OPEN"} if not include_claimed else {"OPEN", "CLAIMED"}
    stubs = [
        s
        for s in load_stubs(stub_dir)
        if s.status in wanted and s.entry_type in {"UNDECIDED", "DISEASE"}
    ]
    stubs.sort(key=lambda s: s.alpha_sort_key if alpha else s.sort_key)
    picked = stubs[:count]

    if as_json:
        typer.echo(
            json.dumps(
                [
                    {
                        "mondo_id": s.mondo_id,
                        "label": s.label,
                        "priority": s.priority,
                        "status": s.status,
                        "entry_type": s.entry_type,
                        "proposed_name": s.data.get("proposed_name"),
                        "rationale": s.data.get("rationale"),
                        "stub_path": str(s.path.relative_to(Path.cwd()))
                        if s.path.is_relative_to(Path.cwd())
                        else str(s.path),
                    }
                    for s in picked
                ],
                indent=2,
            )
        )
        return

    if not picked:
        typer.echo("No open stubs.")
        return
    for stub in picked:
        typer.echo(f"{stub.priority:6s} {stub.mondo_id}  {stub.label}")
        typer.echo(f"       {stub.path.name}")


@app.command("stats")
def stats_command(stub_dir: Path = _STUB_DIR_OPTION) -> None:
    """Summarize the queue by status, entry type, and priority."""
    stubs = load_stubs(stub_dir)
    typer.echo(f"stubs: {len(stubs)}")
    for field_name, getter in (
        ("status", lambda s: s.status),
        ("entry_type", lambda s: s.entry_type),
        ("priority", lambda s: s.priority),
    ):
        counts: dict[str, int] = {}
        for stub in stubs:
            counts[getter(stub)] = counts.get(getter(stub), 0) + 1
        rendered = ", ".join(f"{k}={v}" for k, v in sorted(counts.items()))
        typer.echo(f"  {field_name}: {rendered}")


@app.command("seed")
def seed_command(
    source: Path = typer.Argument(
        ...,
        exists=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        help="Nomination list to seed from (see `--source-format`).",
    ),
    stub_dir: Path = _STUB_DIR_OPTION,
    source_format: str = typer.Option(
        "rare-disease-identification",
        "--source-format",
        help="Format of the nomination list.",
    ),
    dry_run: bool = typer.Option(
        False, "--dry-run", help="Report what would be written without writing."
    ),
    limit: int = typer.Option(
        0, "--limit", help="Stop after N new stubs (0 = no limit)."
    ),
) -> None:
    """Create stubs for nominated diseases that are not curated and have no stub.

    Never overwrites an existing stub — a stub is hand-editable content once it
    exists, so re-running this only adds what is missing.
    """
    result = seed_stubs(
        source=source,
        stub_dir=stub_dir,
        source_format=source_format,
        dry_run=dry_run,
        limit=limit or None,
    )
    typer.echo(
        f"nominated={result.nominated} "
        f"already_curated={result.already_curated} "
        f"already_stubbed={result.already_stubbed} "
        f"skipped={result.skipped} "
        f"written={result.written}"
    )
    if dry_run:
        typer.echo("(dry run — nothing written)")


@app.command("coverage")
def coverage_command() -> None:
    """Report how many MONDO IDs the committed KB already covers."""
    index = build_coverage_index()
    disorders = sum(1 for v in index.ids.values() if v.startswith("disorders/"))
    groupings = sum(1 for v in index.ids.values() if v.startswith("groupings/"))
    typer.echo(
        f"covered MONDO IDs: {len(index.ids)} "
        f"(disorders {disorders}, groupings {groupings})"
    )


def main() -> None:
    app()


if __name__ == "__main__":
    main()
