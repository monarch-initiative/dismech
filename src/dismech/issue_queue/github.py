"""GitHub and git reads for the issue queue. Read-only."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

from dismech.issue_queue.rules import REPO

SNAPSHOT = Path("tmp/issues.json")
OWNER, NAME = REPO.split("/")
BATCH = 25


def sh(*args: str) -> str:
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    if result.returncode:
        sys.exit(f"{' '.join(args[:3])}... failed: {result.stderr.strip()}")
    return result.stdout


def require_gh() -> None:
    if shutil.which("gh") is None:
        sys.exit(
            "this needs the gh CLI, which is not installed here; see "
            "'No gh CLI' in .claude/skills/claim-disease/SKILL.md for web and remote sessions"
        )


def current_user() -> str:
    return sh("gh", "api", "user", "-q", ".login").strip()


def fetch_snapshot(path: Path = SNAPSHOT) -> list[dict]:
    """Every open issue, written to `path`. Every later step reads this file."""
    raw = sh(
        "gh",
        "issue",
        "list",
        "--repo",
        REPO,
        "--state",
        "open",
        "--limit",
        "5000",
        "--json",
        "number,title,author,assignees,labels,createdAt,body",
    )
    issues = json.loads(raw)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(issues, indent=1))
    return issues


def _graphql(fields: str) -> dict:
    query = f'{{ repository(owner:"{OWNER}", name:"{NAME}") {{ {fields} }} }}'
    return json.loads(sh("gh", "api", "graphql", "-f", f"query={query}"))["data"][
        "repository"
    ]


_PR_FIELDS = (
    "closedByPullRequestsReferences(first:20, includeClosedPrs:true) { nodes { number state } } "
    "timelineItems(first:100, itemTypes:[CROSS_REFERENCED_EVENT, CONNECTED_EVENT]) { nodes { "
    "... on CrossReferencedEvent { willCloseTarget source { ... on PullRequest { number state repository { nameWithOwner } } } } "
    "... on ConnectedEvent { subject { ... on PullRequest { number state repository { nameWithOwner } } } } } }"
)
_RELATION_RANK = {"closes": 0, "linked": 1, "mentions": 2}


def _add_pr(
    prs: dict[tuple[int, str], dict], num: int, repo: str, state: str, relation: str
) -> None:
    """Keep one entry per PR, with its strongest relation to the issue."""
    old = prs.get((num, repo))
    if old is None or _RELATION_RANK[relation] < _RELATION_RANK[old["relation"]]:
        prs[(num, repo)] = {
            "number": num,
            "repo": repo,
            "state": state,
            "relation": relation,
        }


def linked_prs(numbers: list[int]) -> dict[int, list[dict]]:
    """Every PR attached to each issue, with its state and relation.

    Relation is `closes` (merging it closes the issue), `linked` (the
    Development sidebar) or `mentions` (cites the issue without closing it).
    This is GitHub's own link and cross-reference record, so `ORPHA:2704` in a
    PR body never counts as a reference to #2704, which the text search
    `gh pr list --search "#2704"` gets wrong.
    """
    out: dict[int, list[dict]] = {}
    for start in range(0, len(numbers), BATCH):
        chunk = numbers[start : start + BATCH]
        data = _graphql(
            " ".join(f"i{n}: issue(number:{n}) {{ {_PR_FIELDS} }}" for n in chunk)
        )
        for n in chunk:
            node = data[f"i{n}"]
            prs: dict[tuple[int, str], dict] = {}

            for pr in node["closedByPullRequestsReferences"]["nodes"]:
                _add_pr(prs, pr["number"], REPO, pr["state"], "closes")
            for item in node["timelineItems"]["nodes"]:
                if (item.get("source") or {}).get("number"):
                    pr = item["source"]
                    _add_pr(
                        prs,
                        pr["number"],
                        pr["repository"]["nameWithOwner"],
                        pr["state"],
                        "closes" if item.get("willCloseTarget") else "mentions",
                    )
                elif (item.get("subject") or {}).get("number"):
                    pr = item["subject"]
                    _add_pr(
                        prs,
                        pr["number"],
                        pr["repository"]["nameWithOwner"],
                        pr["state"],
                        "linked",
                    )
            out[n] = sorted(
                prs.values(), key=lambda pr: (pr["repo"] != REPO, pr["number"])
            )
    return out


def comments_matching(numbers: list[int], needle: str) -> dict[int, bool]:
    """Whether any comment on each issue contains `needle` (already casefolded).

    Comments are not in the snapshot, so this is always a live read. An issue
    with more than 100 comments is re-read in full rather than judged on a
    truncated page. GitHub's `in:comments` search is not used: its index lags
    and it matches words, not substrings.
    """
    out: dict[int, bool] = {}
    for start in range(0, len(numbers), BATCH):
        chunk = numbers[start : start + BATCH]
        data = _graphql(
            " ".join(
                f"i{n}: issue(number:{n}) {{ comments(first:100) {{ totalCount nodes {{ body }} }} }}"
                for n in chunk
            )
        )
        for n in chunk:
            comments = data[f"i{n}"]["comments"]
            bodies = [c["body"] for c in comments["nodes"]]
            if comments["totalCount"] > len(bodies):
                full = json.loads(
                    sh(
                        "gh",
                        "issue",
                        "view",
                        str(n),
                        "--repo",
                        REPO,
                        "--json",
                        "comments",
                    )
                )
                bodies = [c["body"] for c in full["comments"]]
            out[n] = any(needle in (b or "").casefold() for b in bodies)
    return out


def open_prs_naming(mondo: str, label: str) -> list[str]:
    """Open PRs whose text names the MONDO ID or the label (a curation PR often names only the disease)."""
    raw = sh(
        "gh",
        "pr",
        "list",
        "--repo",
        REPO,
        "--state",
        "open",
        "--limit",
        "50",
        "--search",
        f'"{mondo}" OR "{label}"',
        "--json",
        "number,title",
    )
    return [f"#{pr['number']} {pr['title']}" for pr in json.loads(raw)]


def repo_labels() -> list[str]:
    raw = sh("gh", "label", "list", "--repo", REPO, "--limit", "500", "--json", "name")
    return [lab["name"] for lab in json.loads(raw)]


def on_main(path: str) -> bool:
    return (
        subprocess.run(
            ["git", "cat-file", "-e", f"origin/main:{path}"],
            capture_output=True,
            check=False,
        ).returncode
        == 0
    )


def checkout_lag() -> int:
    """Commits the local checkout is behind origin/main; the coverage index reads the local kb/."""
    out = subprocess.run(
        ["git", "rev-list", "--count", "HEAD..origin/main"],
        capture_output=True,
        text=True,
        check=False,
    )
    return int(out.stdout.strip() or 0)


_COVERAGE = None


def kb_covered(mondo: str, label: str) -> list[str]:
    """Coverage as CLAUDE.md defines it, via the index `tidy-stubs` uses.

    A text search for the ID is too loose: a sibling disease names it under
    `differential_diagnoses`, which is not curation.
    """
    global _COVERAGE
    if _COVERAGE is None:
        from dismech.stubs.model import build_coverage_index

        _COVERAGE = build_coverage_index()
    hits = [_COVERAGE.covered_by(mondo), _COVERAGE.entry_labelled(label)]
    return sorted({h for h in hits if h})
