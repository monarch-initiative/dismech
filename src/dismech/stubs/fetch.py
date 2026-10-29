"""Fetch the open `claim`-labelled issues into a claims file.

This is what `just fetch-claims` runs. Two routes, tried in order:

1. **`gh issue list`** (GraphQL). Preferred, because it can report
   ``closedByPullRequestsReferences``: the PRs that would close each issue,
   which is how `check-claims` tells a long-running claim from a stale one.
2. **`gh api --paginate`** (REST). Used when the GraphQL call fails. A Claude
   Code cloud session has an authenticated `gh` but its proxy rejects every
   GraphQL request with HTTP 403 (#15854); a `gh` older than v2.73.0 does not
   know the ``closedByPullRequestsReferences`` field and exits 1 (#11814). REST
   has no equivalent of that field, so rows fetched this way omit it, and
   `check-claims` says its stale list may over-report instead of silently
   over-reporting.

Both routes hit the list endpoint, which is immediately consistent, unlike a
search (see :mod:`dismech.stubs.claims`).

The output file is written only when a route succeeded and returned a well-formed
list. A failed fetch exits non-zero and leaves any existing file untouched; the
old recipe redirected `gh` straight into the file, so a failure truncated it to
zero bytes and the next recipe had to work out why.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
from collections.abc import Callable, Sequence
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

#: The repository whose `claim` issues are the lock.
CLAIMS_REPO = "monarch-initiative/dismech"

#: `--limit` for the GraphQL route. `gh issue list` truncates silently at this
#: number, so a GraphQL result of exactly this size is treated as truncated and
#: the REST route, which paginates with no cap, is used instead.
CLAIM_FETCH_LIMIT = 1000

#: Fields requested on the GraphQL route.
GRAPHQL_FIELDS = "number,title,assignees,url,createdAt,closedByPullRequestsReferences"

#: Projection applied on the REST route, one compact JSON object per line. The
#: issues endpoint also returns pull requests, which carry `pull_request`.
REST_JQ = (
    ".[] | select(.pull_request | not) | "
    "{number, title, created_at, html_url, assignees: [.assignees[].login]}"
)

#: Printed when there is no `gh` at all (Claude Code web sessions).
NO_GH_MESSAGE = """\
fetch-claims needs the gh CLI, which is not installed in this environment.

Claude Code web/remote sessions have no gh, and cannot reach api.github.com
directly either -- the agent proxy denies it even though GH_TOKEN is set.
Use the GitHub MCP server instead: see 'No gh CLI (web and remote sessions)'
in .claude/skills/claim-disease/SKILL.md for the exact fallback, including
the minimal titles-only claims file that is enough to pick from."""

Runner = Callable[..., subprocess.CompletedProcess]


class ClaimFetchError(RuntimeError):
    """A route failed, or returned something that is not a claim list."""


@dataclass
class FetchResult:
    rows: list[dict[str, Any]]
    #: "graphql" or "rest".
    route: str
    #: Why an earlier route was not used, for the user to read.
    notes: list[str] = field(default_factory=list)

    @property
    def linked_prs_available(self) -> bool:
        return self.route == "graphql"


def _run(runner: Runner | None, args: Sequence[str]) -> str:
    # Looked up at call time, not bound as a default, so a test can replace it.
    runner = runner or subprocess.run
    try:
        proc = runner(list(args), capture_output=True, text=True, check=False)
    except OSError as exc:
        raise ClaimFetchError(f"could not run {args[0]}: {exc}") from exc
    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout or "").strip().splitlines()
        reason = detail[0] if detail else "no output"
        if len(reason) > 200:
            reason = reason[:200] + "..."
        raise ClaimFetchError(
            f"`{' '.join(args[:3])}` exited {proc.returncode}: {reason}"
        )
    return proc.stdout or ""


def _check_rows(rows: Any, route: str) -> list[dict[str, Any]]:
    if not isinstance(rows, list):
        raise ClaimFetchError(
            f"{route} route returned {type(rows).__name__}, not a list"
        )
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get("title"), str):
            raise ClaimFetchError(
                f"{route} route returned a row with no title: {row!r}"
            )
    return rows


def fetch_via_graphql(
    repo: str = CLAIMS_REPO, runner: Runner | None = None
) -> list[dict]:
    out = _run(
        runner,
        [
            "gh", "issue", "list",
            "--repo", repo,
            "--label", "claim",
            "--state", "open",
            "--json", GRAPHQL_FIELDS,
            "--limit", str(CLAIM_FETCH_LIMIT),
        ],
    )  # fmt: skip
    if not out.strip():
        raise ClaimFetchError("GraphQL route exited 0 with no output")
    try:
        rows = json.loads(out)
    except json.JSONDecodeError as exc:
        raise ClaimFetchError(f"GraphQL route returned invalid JSON: {exc}") from exc
    return _check_rows(rows, "GraphQL")


def fetch_via_rest(repo: str = CLAIMS_REPO, runner: Runner | None = None) -> list[dict]:
    out = _run(
        runner,
        [
            "gh", "api", "--paginate",
            f"repos/{repo}/issues?labels=claim&state=open&per_page=100",
            "--jq", REST_JQ,
        ],
    )  # fmt: skip
    rows = []
    for line in out.splitlines():
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ClaimFetchError(f"REST route returned invalid JSON: {exc}") from exc
    return _check_rows(rows, "REST")


def fetch_claims(repo: str = CLAIMS_REPO, runner: Runner | None = None) -> FetchResult:
    """GraphQL first, REST on any GraphQL failure or truncation."""
    notes: list[str] = []
    try:
        rows = fetch_via_graphql(repo, runner)
    except ClaimFetchError as exc:
        notes.append(
            f"gh issue list (GraphQL) failed, falling back to the REST API: {exc}"
        )
    else:
        if len(rows) < CLAIM_FETCH_LIMIT:
            return FetchResult(rows=rows, route="graphql")
        notes.append(
            f"gh issue list returned exactly {CLAIM_FETCH_LIMIT} claims, so the "
            "list was probably truncated; used the REST API, which paginates."
        )
    try:
        rows = fetch_via_rest(repo, runner)
    except ClaimFetchError as exc:
        raise ClaimFetchError(
            "; ".join([*notes, f"REST route also failed: {exc}"])
        ) from exc
    return FetchResult(rows=rows, route="rest", notes=notes)


def write_claims_file(rows: list[dict[str, Any]], out: Path) -> None:
    """Write via a temporary file in the same directory, then rename into place,
    so a crash mid-write never leaves a partial or empty claims file."""
    out.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=f".{out.name}.", suffix=".tmp", dir=out.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(rows, handle, indent=1)
            handle.write("\n")
        os.replace(tmp, out)
    except BaseException:
        Path(tmp).unlink(missing_ok=True)
        raise


def gh_available() -> bool:
    return shutil.which("gh") is not None
