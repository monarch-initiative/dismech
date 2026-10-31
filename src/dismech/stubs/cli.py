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
from .fetch import (
    CLAIM_FETCH_LIMIT,
    CLAIMS_REPO,
    NO_GH_MESSAGE,
    ClaimFetchError,
    fetch_claims,
    gh_available,
    write_claims_file,
)
from .model import (
    build_coverage_index,
    check_stubs,
    default_stub_dir,
    load_stubs,
    load_stubs_reporting_errors,
)
from .obsolescence import default_mondo_db, load_obsolescence
from .seed import seed_stubs

app = typer.Typer(
    name="dismech-stubs",
    help="Inspect and maintain the curation stub queue under stubs/.",
)

# A factory, not a value, so the default is the checkout the command runs in
# rather than whichever was current when this module was imported (#15109).
_STUB_DIR_OPTION = typer.Option(
    ...,
    "--stub-dir",
    default_factory=default_stub_dir,
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


#: Fields `just enrich-stubs` (and the seed) write that the lump/split call
#: turns on. `next --json` passes each through only when the stub carries it,
#: because the enrichment omits an empty block rather than writing it empty, so
#: an absent key keeps that meaning instead of becoming a `null`.
ENRICHMENT_KEYS = (
    "mondo_parents",
    "mondo_descendants",
    "mondo_descendant_count",
    "genes",
    "synonyms",
)


@app.command("next")
def next_command(
    count: int = typer.Argument(1, min=1, help="How many stubs to show."),
    stub_dir: Path = _STUB_DIR_OPTION,
    include_claimed: bool = typer.Option(
        False,
        "--include-claimed",
        help="Do not filter out diseases with an open claim issue.",
    ),
    include_stale: bool = typer.Option(
        False,
        "--include-stale",
        help=(
            "Do not filter out stale stubs (disease already curated, or MONDO "
            "term retired with no replacement)."
        ),
    ),
    alpha: bool = typer.Option(
        False, "--alpha", help="Sort alphabetically within a band instead of by hash."
    ),
    claims_path: str = typer.Option(
        None,
        "--claims",
        help=(
            "Open claim issues as JSON, to exclude already-claimed diseases. "
            "Use '-' for stdin. Produce it with `just fetch-claims` "
            "(`dismech-stubs fetch-claims`)."
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

    Stale stubs (`already_curated`, `obsolete_term`; see `STALE_KINDS`) are left
    out, because `tidy` would delete them and nobody should claim one in the
    meantime. Every other advisory `check` raises on a stub, such as
    `possible_kb_duplicate`, keeps it in the pool and is printed beside it, so
    the lump/split call is made before the claim rather than after. A finding
    that points at a MONDO successor (`REPOINT_KINDS`, and
    `successor_already_stubbed`) names it beside the kind and as `successor` in
    `--json`, so nobody claims a disease under the identifier it is leaving.
    """
    # Read the claims first, so a missing file fails before the slow KB walk.
    claimed = _load_claim_index(claims_path)

    stubs = [
        s
        for s in load_stubs(stub_dir)
        if s.status == "OPEN" and s.entry_type in {"UNDECIDED", "DISEASE"}
    ]

    # Reuse `check`'s own classification rather than re-deriving staleness here,
    # so `next` and `tidy` can never disagree about which stubs are stale.
    advisories: dict[Path, list] = {}
    for issue in check_stubs(stub_dir):
        if issue.path is not None and issue.severity != "error":
            advisories.setdefault(issue.path, []).append(issue)
    if not include_stale:
        stubs = [
            s
            for s in stubs
            if not any(i.kind in STALE_KINDS for i in advisories.get(s.path, []))
        ]

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
                        "advisories": [
                            _advisory_record(i) for i in advisories.get(s.path, [])
                        ],
                        **{
                            key: s.data[key]
                            for key in ENRICHMENT_KEYS
                            if s.data.get(key) is not None
                        },
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
        line = f"{stub.priority:6s} {stub.mondo_id}  {stub.label}"
        # The clearest single "this is a grouping" signal, so it goes on the row.
        if stub.data.get("mondo_descendant_count"):
            line += f"  (MONDO descendants: {stub.data['mondo_descendant_count']})"
        typer.echo(line)
        typer.echo(f"       {stub.path.name}")
        for issue in advisories.get(stub.path, []):
            arrow = f" -> {issue.successor}" if issue.successor else ""
            typer.echo(f"       [advisory] {issue.kind}{arrow}: {issue.message}")


def _advisory_record(issue) -> dict:
    """One `--json` advisory. `successor` appears only when the finding has one."""
    record = {"kind": issue.kind, "message": issue.message}
    if issue.successor:
        record["successor"] = issue.successor
    return record


def _read_json_arg(path: str | None):
    if not path:
        return None
    try:
        text = (
            sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
        )
    except FileNotFoundError:
        typer.echo(
            f"claims file not found: {path}. Write it with `just fetch-claims`, "
            "or build it from the GitHub MCP server where there is no gh CLI "
            "(see the claim-disease skill).",
            err=True,
        )
        raise typer.Exit(2) from None
    if not text.strip():
        # What a failed `gh ... > tmp/claims.json` used to leave behind
        # (#15854, #11814). Reading it as "no claims" would offer every
        # claimed disease as free, so it is an error, not an empty list.
        typer.echo(
            f"claims file is empty: {path}. An earlier fetch probably failed; "
            "re-run `just fetch-claims` and check its output.",
            err=True,
        )
        raise typer.Exit(2)
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        typer.echo(f"claims file is not valid JSON: {path}: {exc}", err=True)
        raise typer.Exit(2) from None


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
        # `fetch-claims` already switches to the uncapped REST route when it
        # sees exactly this many; this catches a file produced some other way.
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
        unknown = sum(1 for c in stale if not c.linked_pr_known)
        if unknown:
            typer.echo(
                f"  NOTE: linked-PR data is unavailable for {unknown} of these "
                "(the claims file was fetched over the REST API or the GitHub "
                "MCP server, which cannot report PRs that close an issue), so "
                "this list may over-report. Check an issue for an open PR "
                "before treating its claim as stale."
            )
        for claim in sorted(stale, key=lambda c: -(c.age_days() or 0)):
            age = claim.age_days()
            who = ", ".join(claim.assignees) or "unassigned"
            typer.echo(f"  #{claim.number} {int(age or 0):4d}d {who:20s} {claim.title}")


@app.command("fetch-claims")
def fetch_claims_command(
    out: Path = typer.Option(
        Path("tmp/claims.json"), "--out", help="Where to write the claims JSON."
    ),
    repo: str = typer.Option(CLAIMS_REPO, "--repo", help="owner/name to read."),
) -> None:
    """Fetch the open `claim` issues and write them to OUT.

    Tries `gh issue list` (GraphQL, which reports linked PRs) and falls back
    to `gh api --paginate` (REST) when that fails, as it does in Claude Code
    cloud sessions and on gh older than v2.73.0. OUT is written only on
    success; a failed fetch exits 1 and leaves any existing file as it was.
    """
    if not gh_available():
        typer.echo(NO_GH_MESSAGE, err=True)
        raise typer.Exit(127)
    try:
        result = fetch_claims(repo)
    except ClaimFetchError as exc:
        typer.echo(f"fetch-claims failed, {out} not written: {exc}", err=True)
        raise typer.Exit(1) from None
    for note in result.notes:
        typer.echo(note, err=True)
    if not result.rows:
        typer.echo(
            f"WARNING: GitHub reports no open `claim` issues in {repo}. That is "
            "possible but unusual; check before trusting an empty claim list.",
            err=True,
        )
    write_claims_file(result.rows, out)
    route = "gh issue list" if result.route == "graphql" else "the REST API"
    typer.echo(f"wrote {len(result.rows)} claims to {out} (via {route})")
    if not result.linked_prs_available:
        typer.echo(
            "linked-PR data is not available over REST, so `check-claims` may "
            "over-report stale claims.",
            err=True,
        )


#: Findings that mean "the queue drifted", not "this file is broken". These are
#: what `tidy` clears and what `check` refuses to gate on.
#:
#: `obsolete_term_replaced` is deliberately NOT here. A merged term still names
#: a disease nobody has curated — the identifier moved, the work did not — so
#: deleting the stub would silently drop real queue content. Those are repointed
#: at the replacement instead, and `tidy` lists them for a person rather than
#: sweeping them. Nor is `obsoletion_candidate`: that term is still live.
STALE_KINDS = ("already_curated", "obsolete_term")

#: Advisories `tidy` reports but never acts on, because the remedy is an edit
#: rather than a deletion.
REPOINT_KINDS = ("obsolete_term_replaced", "obsoletion_candidate")

#: A stub whose MONDO successor already has a stub of its own. Repointing it
#: would collide with that stub, so the remedy is to fold the two by hand; `tidy`
#: lists these and, as with `REPOINT_KINDS`, deletes nothing.
FOLD_KINDS = ("successor_already_stubbed",)


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
    findings = check_stubs(stub_dir)
    stale = [i for i in findings if i.kind in STALE_KINDS]
    fold = [i for i in findings if i.kind in FOLD_KINDS]
    # A stub to fold is not also listed as one to repoint: repointing it at a
    # successor that already has a stub would only create a duplicate ID.
    folding = {i.path for i in fold}
    repoint = [i for i in findings if i.kind in REPOINT_KINDS and i.path not in folding]
    if fold:
        typer.echo(
            f"duplicates a stub for its MONDO successor ({len(fold)}) — fold the "
            "two by hand, then delete this one:"
        )
        for issue in fold:
            typer.echo(f"  {issue.format()}")
        typer.echo("")
    if repoint:
        typer.echo(
            f"needs a repointed `mondo_id`, not deletion ({len(repoint)}) — "
            "the disease is still uncurated:"
        )
        for issue in repoint:
            typer.echo(f"  {issue.format()}")
        typer.echo("")
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


@app.command("obsolescence")
def obsolescence_command(
    stub_dir: Path = _STUB_DIR_OPTION,
    mondo_db: Path = typer.Option(
        None,
        "--mondo-db",
        help="MONDO semantic-SQL build. Defaults to OAK's cache (mondo.db).",
    ),
    as_json: bool = typer.Option(False, "--json", help="Emit JSON instead of text."),
) -> None:
    """Ask MONDO which stub terms it has retired, or decided to retire.

    The exact version of the obsolescence signal. `check` reads the answer out
    of the committed stub fields, which is offline and free but only as fresh as
    the last `just enrich-stubs`; this asks the ontology directly.

    Two facts, and the second is the one that catches things. A term is
    `owl:deprecated` only in a MONDO release built *after* the merge lands,
    which can be months later — but MONDO puts the term in its
    `obsoletion_candidate` subset the moment it decides, with a note saying what
    the term will merge into. `MONDO:0859244` (dismech#10785) has carried that
    note since 2026-04 and is still not deprecated in the pinned release.

    Needs the MONDO build, which is a ~1.2 GB download. Absent, this reports
    that and exits 0 — it is a census for a person, not a gate.
    """
    stubs = load_stubs(stub_dir)
    by_id: dict[str, list] = {}
    for stub in stubs:
        if stub.mondo_id:
            by_id.setdefault(stub.mondo_id, []).append(stub)

    index = load_obsolescence(mondo_db, list(by_id))
    if index is None:
        where = mondo_db or default_mondo_db()
        message = (
            f"MONDO database not found at {where} — skipping the ontology check. "
            "Fetch it with `just fetch-ontology-dbs mondo`, or read the committed "
            "answer with `just check-stubs`."
        )
        typer.echo(
            json.dumps({"available": False, "message": message}) if as_json else message
        )
        return

    rows = []
    for mondo_id, status in sorted(index.terms.items()):
        for stub in by_id.get(mondo_id, []):
            rows.append(
                {
                    "mondo_id": mondo_id,
                    "label": stub.label,
                    "stub": stub.path.name,
                    "obsolete": status.obsolete,
                    "replaced_by": status.replaced_by,
                    "obsoletion_candidate": status.obsoletion_candidate,
                    "proposed_replacement": status.proposed_replacement,
                    "note": status.obsoletion_note,
                    "summary": status.describe(),
                }
            )

    if as_json:
        typer.echo(
            json.dumps(
                {
                    "available": True,
                    "mondo_version": index.version,
                    "stubs": len(stubs),
                    "obsolete": sum(1 for r in rows if r["obsolete"]),
                    "obsoletion_candidates": sum(
                        1 for r in rows if r["obsoletion_candidate"]
                    ),
                    "findings": rows,
                },
                indent=2,
            )
        )
        return

    obsolete = [r for r in rows if r["obsolete"]]
    candidates = [r for r in rows if r["obsoletion_candidate"]]
    typer.echo(f"mondo: {index.version or 'unknown'}  stubs: {len(stubs)}")
    typer.echo(
        f"obsolete mondo_id: {len(obsolete)}  "
        f"scheduled for obsoletion: {len(candidates)}"
    )
    for row in obsolete:
        typer.echo(f"\n  {row['stub']}")
        typer.echo(f"    {row['summary']}")
    for row in candidates:
        typer.echo(f"\n  {row['stub']}")
        typer.echo(f"    {row['summary']}")
        if row["note"]:
            typer.echo(f"    MONDO: {' '.join(row['note'].split())}")
    if not rows:
        typer.echo("\nNo stub names a term MONDO has retired or scheduled.")


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
