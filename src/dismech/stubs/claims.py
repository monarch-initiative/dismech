"""GitHub claim issues: the live lock on who is curating what.

A claim is an **open GitHub issue labelled `claim`** whose title carries the
MONDO ID. The stub queue says what is left to do; the claim label says what is
being done right now. They are separate on purpose:

- A stub is a durable judgement, edited by pull request. It becomes visible when
  the PR merges, which can be days — useless as a lock.
- A claim is live state that changes many times a day, and GitHub already
  arbitrates it: an issue exists or it does not, the moment it is created.

The label is what makes the check cheap and correct. `gh issue list --label
claim` hits the **list** endpoint, which is immediately consistent, so an issue
filed thirty seconds ago is already visible. The `--search` form the old
preflight used hits the search API, whose index lags issue creation by seconds
to minutes — which is precisely the width of the race window it was meant to
close.

One call fetches every open claim; matching then happens locally, so the check
costs one request no matter how many candidates are in the pool.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any

#: MONDO ID as it appears in a claim issue title: `Curate rickets (MONDO:0005520)`.
_TITLE_MONDO_PATTERN = re.compile(r"MONDO:[0-9]{7}")

#: A disease claim announces itself with a leading "Curate". The label is
#: deliberately broader than diseases -- "claim a disease (or other entry) for
#: curation" -- so a module or grouping claim legitimately has no MONDO ID and
#: must not be nagged for missing one.
_DISEASE_CLAIM_PATTERN = re.compile(r"^\s*curate\b", re.IGNORECASE)

#: A claim with no linked PR older than this is reported as stale. A claim with
#: an open PR is never stale however old it is -- long-running curation PRs are
#: normal here, and the point of the lock is to survive them.
DEFAULT_STALE_DAYS = 30


@dataclass
class Claim:
    """One open `claim`-labelled issue."""

    number: int
    title: str
    mondo_id: str | None
    assignees: list[str] = field(default_factory=list)
    url: str = ""
    created_at: str = ""
    has_linked_pr: bool = False

    def age_days(self, now: datetime | None = None) -> float | None:
        if not self.created_at:
            return None
        try:
            created = datetime.fromisoformat(self.created_at)
        except ValueError:
            return None
        reference = now or datetime.now(UTC)
        return (reference - created).total_seconds() / 86400.0

    def is_stale(
        self, stale_days: int = DEFAULT_STALE_DAYS, now: datetime | None = None
    ) -> bool:
        """An old claim with nothing to show for it.

        Having an open PR clears staleness outright: a curation PR can sit in
        review for weeks and the claim should hold that whole time.
        """
        if self.has_linked_pr:
            return False
        age = self.age_days(now)
        return age is not None and age > stale_days


def _assignee_logins(value: Any) -> list[str]:
    """Read assignees from either `gh` shape: [{"login": x}] or ["x"]."""
    logins = []
    for entry in value or []:
        if isinstance(entry, dict):
            login = entry.get("login")
            if login:
                logins.append(str(login))
        elif entry:
            logins.append(str(entry))
    return logins


def _has_linked_pr(row: dict[str, Any]) -> bool:
    """Whether the issue names an open PR.

    `gh issue list --json closedByPullRequestsReferences` reports PRs that would
    close the issue. Absent that field the answer is False, which errs toward
    calling a claim stale -- and a stale claim is reported for a human to look
    at, never auto-taken, so the conservative direction is safe.
    """
    refs = row.get("closedByPullRequestsReferences")
    if isinstance(refs, dict):
        refs = refs.get("references") or refs.get("nodes")
    return bool(isinstance(refs, list) and refs)


def parse_claims(payload: Any) -> list[Claim]:
    """Parse `gh issue list --label claim --json ...` output."""
    if isinstance(payload, str):
        payload = json.loads(payload)
    rows = payload.get("issues") if isinstance(payload, dict) else payload
    claims: list[Claim] = []
    for row in rows or []:
        if not isinstance(row, dict):
            continue
        title = str(row.get("title") or "")
        match = _TITLE_MONDO_PATTERN.search(title)
        claims.append(
            Claim(
                number=int(row.get("number") or 0),
                title=title,
                mondo_id=match.group(0) if match else None,
                assignees=_assignee_logins(row.get("assignees")),
                url=str(row.get("url") or row.get("html_url") or ""),
                created_at=str(row.get("createdAt") or row.get("created_at") or ""),
                has_linked_pr=_has_linked_pr(row),
            )
        )
    return claims


def index_claims(claims: list[Claim]) -> dict[str, Claim]:
    """MONDO ID -> claim. First claim wins; a second one on the same ID is a
    double-claim, which :func:`double_claims` reports separately."""
    index: dict[str, Claim] = {}
    for claim in claims:
        if claim.mondo_id:
            index.setdefault(claim.mondo_id, claim)
    return index


def unkeyed_claims(claims: list[Claim]) -> list[Claim]:
    """Disease claims whose title carries no MONDO ID.

    These lock nothing -- no candidate check can match them -- so they are
    reported rather than ignored. The fix is to retitle the issue to
    `Curate <label> (MONDO:NNNNNNN)`.

    Scoped to titles beginning "Curate". The `claim` label covers entries other
    than diseases (modules, groupings), which have no MONDO ID to carry; those
    are not broken and are not reported here.
    """
    return [
        c for c in claims if not c.mondo_id and _DISEASE_CLAIM_PATTERN.match(c.title)
    ]


def non_disease_claims(claims: list[Claim]) -> list[Claim]:
    """Claims that are neither MONDO-keyed nor disease-shaped.

    Module and grouping claims. Counted so the totals add up, but nothing is
    asked of them.
    """
    return [
        c
        for c in claims
        if not c.mondo_id and not _DISEASE_CLAIM_PATTERN.match(c.title)
    ]


def double_claims(claims: list[Claim]) -> dict[str, list[Claim]]:
    """MONDO IDs claimed by more than one open issue."""
    by_id: dict[str, list[Claim]] = {}
    for claim in claims:
        if claim.mondo_id:
            by_id.setdefault(claim.mondo_id, []).append(claim)
    return {k: v for k, v in by_id.items() if len(v) > 1}
