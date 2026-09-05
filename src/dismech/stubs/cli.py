"""`dismech-stubs` — inspect and maintain the curation stub queue."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import typer

from .claims import (
    DEFAULT_STALE_DAYS,
    double_claims,
    index_claims,
    non_disease_claims,
    parse_claims,
    unkeyed_claims,
)
from .model import (
    build_coverage_index,
    check_stubs,
    default_stub_dir,
    load_stubs,
    load_stubs_reporting_errors,
)
from .seed import seed_stubs

#: Must match the `--limit` in the `just fetch-claims` recipe.
CLAIM_FETCH_LIMIT = 1000

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
    """Check that each stub file is well formed.

    Errors are malformed files — unparseable YAML, a bad MONDO ID, a duplicate,
    a bad enum value. Only the author of that stub sees them, and they are cheap
    to fix, so they gate.

    Everything else is an advisory and never gates. A stub going stale because
    somebody curated its disease is expected drift, not a fault: gating on it
    would turn every open stub PR red the moment an unrelated curation PR merged.
    `dismech-stubs tidy` clears those on a sweep.
    """
    issues = check_stubs(stub_dir)
    errors = [i for i in issues if i.severity == "error"]
    advisories = [i for i in issues if i.severity != "error"]
    # Counted from the same loader `check_stubs` used, so a malformed file is
    # reported as an `unparseable` error rather than raising here.
    stubs, _ = load_stubs_reporting_errors(stub_dir)
    count = len(stubs)

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
        False,
        "--include-claimed",
        help="Do not filter out diseases with an open claim issue.",
    ),
    alpha: bool = typer.Option(
        False, "--alpha", help="Sort alphabetically within a band instead of by hash."
    ),
    claims_path: str = typer.Option(
        None,
        "--claims",
        help=(
            "Open claim issues as JSON, to exclude already-claimed diseases. "
            "Use '-' for stdin. Produce it with: gh issue list --label claim "
            "--state open --json number,title,assignees,url,createdAt --limit 1000"
        ),
    ),
    as_json: bool = typer.Option(False, "--json", help="Emit JSON instead of text."),
) -> None:
    """Show the next stubs to curate.

    Two phases, both cheap. Phase 1 is `--claims`: what somebody has already
    taken, read from the open `claim`-labelled issues. Phase 2 is the stub
    queue: what is left to do at all. Without `--claims` you get phase 2 only,
    and the output may include diseases that are already spoken for.

    Ordering is the hand-set `priority` band, then an arbitrary but stable
    spread — there is no computed score, and no ranking within a band. This is a
    pool to choose from, not a recommendation: pick the disease you actually
    know something about rather than the first row.
    """
    stubs = [
        s
        for s in load_stubs(stub_dir)
        if s.status == "OPEN" and s.entry_type in {"UNDECIDED", "DISEASE"}
    ]

    claimed = _load_claim_index(claims_path)
    if claimed is not None and not include_claimed:
        stubs = [s for s in stubs if s.mondo_id not in claimed]

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


def _read_json_arg(path: str | None):
    if not path:
        return None
    if path == "-":
        return json.loads(sys.stdin.read())
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _load_claim_index(path: str | None):
    payload = _read_json_arg(path)
    if payload is None:
        return None
    return index_claims(parse_claims(payload))


@app.command("claims")
def claims_command(
    claims_path: str = typer.Argument(
        "-",
        help="Claim issues as JSON ('-' for stdin). See `next --claims` for the gh command.",
    ),
    stub_dir: Path = _STUB_DIR_OPTION,
    stale_days: int = typer.Option(
        DEFAULT_STALE_DAYS,
        "--stale-days",
        help="Report claims older than this with no linked PR.",
    ),
) -> None:
    """Cross-check open claim issues against the stub queue.

    Reports four things a person should look at: claims whose disease has no
    stub (already curated, or never queued), stubs that are claimed twice,
    disease claims with no MONDO ID in the title (they lock nothing), and stale
    claims — old, with no PR to show for them. A claim with an open PR is never
    stale; long-running curation PRs are normal and the lock should outlast them.

    The `claim` label covers entries other than diseases; module and grouping
    claims are listed separately and nothing is asked of them.
    """
    claims = parse_claims(_read_json_arg(claims_path))
    stub_ids = {s.mondo_id: s for s in load_stubs(stub_dir)}
    keyed = [c for c in claims if c.mondo_id]

    typer.echo(f"open claims: {len(claims)} ({len(keyed)} carrying a MONDO ID)")
    if len(claims) >= CLAIM_FETCH_LIMIT:
        # `gh issue list --limit N` truncates silently, and a truncated claim
        # list means the two-phase check can hand out a disease somebody holds.
        typer.echo(
            f"WARNING: exactly {CLAIM_FETCH_LIMIT} claims returned — the fetch "
            "limit was probably hit and this list may be truncated. Re-fetch "
            "with a higher --limit before trusting it."
        )

    orphaned = [c for c in keyed if c.mondo_id not in stub_ids]
    if orphaned:
        typer.echo(f"\nclaimed but not in the stub queue ({len(orphaned)}):")
        for claim in orphaned:
            typer.echo(f"  #{claim.number} {claim.title}")

    doubles = double_claims(claims)
    if doubles:
        typer.echo(f"\nclaimed more than once ({len(doubles)}):")
        for mondo_id, group in sorted(doubles.items()):
            numbers = ", ".join(f"#{c.number}" for c in group)
            typer.echo(f"  {mondo_id}: {numbers}")

    unkeyed = unkeyed_claims(claims)
    if unkeyed:
        typer.echo(f"\nno MONDO ID in the title, so locking nothing ({len(unkeyed)}):")
        for claim in unkeyed:
            typer.echo(f"  #{claim.number} {claim.title}")

    other = non_disease_claims(claims)
    if other:
        typer.echo(f"\nnot disease claims, nothing needed ({len(other)}):")
        for claim in other:
            typer.echo(f"  #{claim.number} {claim.title}")

    stale = [c for c in claims if c.is_stale(stale_days)]
    if stale:
        typer.echo(
            f"\nstale — over {stale_days}d old with no linked PR ({len(stale)}):"
        )
        for claim in sorted(stale, key=lambda c: -(c.age_days() or 0)):
            age = claim.age_days()
            who = ", ".join(claim.assignees) or "unassigned"
            typer.echo(f"  #{claim.number} {int(age or 0):4d}d {who:20s} {claim.title}")


#: Findings that mean "the queue drifted", not "this file is broken". These are
#: what `tidy` clears and what `check` refuses to gate on.
STALE_KINDS = ("already_curated", "obsolete_term")


@app.command("tidy")
def tidy_command(
    stub_dir: Path = _STUB_DIR_OPTION,
    apply: bool = typer.Option(
        False, "--apply", help="Delete the stale stubs. Without this, only lists them."
    ),
) -> None:
    """Remove stubs the queue has outgrown.

    A stub goes stale when somebody curates its disease, or when MONDO retires
    the term. Neither is anybody's mistake and neither blocks anything — stubs
    are informative, not curated content — so this is a periodic sweep rather
    than something a curator is ever asked to service mid-task.
    """
    stale = [i for i in check_stubs(stub_dir) if i.kind in STALE_KINDS]
    if not stale:
        typer.echo("Nothing stale.")
        return
    for issue in stale:
        typer.echo(issue.format())
    if not apply:
        unique = len({i.path for i in stale if i.path})
        typer.echo(f"\n{unique} stale stub(s). Re-run with --apply to delete them.")
        return
    # Iterate paths, not findings: one stub can be stale twice over. A MONDO
    # term retired *after* somebody curated the disease under it yields both
    # `obsolete_term` and `already_curated` for the same file, and unlinking it
    # a second time aborted the sweep mid-batch with FileNotFoundError — having
    # already deleted an arbitrary prefix of it.
    paths = list(dict.fromkeys(i.path for i in stale if i.path))
    for path in paths:
        path.unlink()
    typer.echo(f"\nDeleted {len(paths)} stale stub(s).")


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
        f"obsolete={result.obsolete} "
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
