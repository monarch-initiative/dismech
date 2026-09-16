#!/usr/bin/env python3
"""Deterministic ingress policy for PR-shepherd automation.

GitHub exposes App identities in more than one spelling depending on the API
surface (for example ``app/ai4c-agent`` and ``ai4c-agent[bot]``).  Keep that
normalization here rather than duplicating fragile login strings in prompts and
workflow shell.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

BOT_APP_LOGINS = frozenset({"ai4c-agent", "claude", "github-actions"})
MACHINE_USER_LOGINS = frozenset({"dragon-ai-agent"})
AGENT_LOGINS = BOT_APP_LOGINS | MACHINE_USER_LOGINS
AUTOMATED_HEAD_PREFIX = "auto/"


@dataclass(frozen=True)
class Decision:
    """A deterministic policy decision and its audit reason."""

    eligible: bool
    reason: str


def normalize_login(value: str | dict | None) -> str:
    """Normalize GraphQL, REST, and plain GitHub actor spellings."""
    if isinstance(value, dict):
        value = value.get("login")
    login = str(value or "").strip().casefold()
    if login.startswith("app/"):
        login = login.removeprefix("app/")
    if login.endswith("[bot]"):
        login = login.removesuffix("[bot]")
    return login


def agent_candidate_decision(pr: dict) -> Decision:
    """Return whether the LLM shepherd may tend this PR.

    Draft state is deliberately absent: in DisMech, opening a PR places the work
    in the review queue.  Assignment, review state, and explicit workflow lanes
    carry lifecycle meaning; the GitHub draft bit does not.
    """
    state = str(pr.get("state") or "").upper()
    if state != "OPEN":
        return Decision(False, f"PR is not open (state={state or 'missing'})")
    if pr.get("baseRefName") != "main":
        return Decision(False, "base branch is not main")
    if "assignees" not in pr:
        return Decision(False, "PR response omitted assignees")
    assignees = pr.get("assignees") or []
    if assignees:
        logins = ", ".join(str(item.get("login") or "?") for item in assignees)
        return Decision(False, f"PR is assigned to {logins}")

    head = str(pr.get("headRefName") or "")
    if head.startswith(AUTOMATED_HEAD_PREFIX):
        return Decision(False, f"separately managed lane {AUTOMATED_HEAD_PREFIX!r}")

    author = pr.get("author")
    login = normalize_login(author)
    if login not in AGENT_LOGINS:
        return Decision(False, f"author {login or '(missing)'} is not allowlisted")
    if login in BOT_APP_LOGINS and not (
        isinstance(author, dict) and author.get("is_bot") is True
    ):
        return Decision(False, f"author {login} lacks a verified Bot identity")
    return Decision(True, f"allowlisted agent author {login}")


def _gh_json(args: list[str]) -> object:
    result = subprocess.run(["gh", *args], check=True, capture_output=True, text=True)
    return json.loads(result.stdout)


def _comparison_contains_base(
    comparison: dict, current_base_sha: str, head_sha: str
) -> bool:
    """Return whether an exact GitHub comparison proves base is in head."""
    base = current_base_sha.strip()
    head = head_sha.strip()
    if not base or not head or not isinstance(comparison, dict):
        raise ValueError("comparison inputs are incomplete")
    compared_base = str((comparison.get("base_commit") or {}).get("sha") or "")
    merge_base = str((comparison.get("merge_base_commit") or {}).get("sha") or "")
    try:
        behind_by = int(comparison["behind_by"])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError("comparison returned no valid behind count") from exc
    return (
        compared_base.casefold() == base.casefold()
        and merge_base.casefold() == base.casefold()
        and behind_by == 0
    )


def _rollup_disposition(rollup: list[dict] | None) -> str:
    """Classify an approved PR's checks for shortlist ownership routing."""
    if not rollup:
        return "failing"
    pending = False
    successful = False
    for entry in rollup:
        typename = entry.get("__typename")
        is_check_run = (
            typename == "CheckRun"
            if typename
            else ("conclusion" in entry or "status" in entry)
        )
        if is_check_run:
            status = str(entry.get("status") or "").upper()
            conclusion = str(entry.get("conclusion") or "").upper()
            if status != "COMPLETED" or not conclusion:
                pending = True
            elif conclusion == "SUCCESS":
                successful = True
            elif conclusion not in {"SKIPPED", "NEUTRAL"}:
                return "failing"
        else:
            state = str(entry.get("state") or "").upper()
            if state == "PENDING" or not state:
                pending = True
            elif state == "SUCCESS":
                successful = True
            elif state not in {"EXPECTED", "NEUTRAL"}:
                return "failing"
    if pending:
        return "pending"
    return "passing" if successful else "failing"


def _controller_owns_approved(pr: dict, contains_current_base: bool) -> bool:
    """Whether the deterministic closer can finish this PR without agent work."""
    if not contains_current_base:
        return False
    if str(pr.get("mergeable") or "").upper() != "MERGEABLE":
        return False
    merge_state = str(pr.get("mergeStateStatus") or "").upper()
    if pr.get("isDraft"):
        if merge_state not in {"BLOCKED", "CLEAN", "DRAFT"}:
            return False
    elif merge_state != "CLEAN":
        return False
    return _rollup_disposition(pr.get("statusCheckRollup")) in {"passing", "pending"}


def _agent_action_rank(
    pr: dict,
    contains_current_base: bool | None,
    controller_owned: bool,
) -> tuple[int, str, int] | None:
    """Rank stuck bot PRs after deterministic ancestry/ownership checks."""
    review = str(pr.get("reviewDecision") or "").upper()
    updated = str(pr.get("updatedAt") or "")
    number = int(pr["number"])
    mergeable = str(pr.get("mergeable") or "").upper()

    if review == "APPROVED":
        if controller_owned:
            return None
        if contains_current_base is False and mergeable == "MERGEABLE":
            return (0, updated, number)
        if mergeable == "CONFLICTING":
            return (1, updated, number)
        # Includes aligned-but-red PRs and comparisons that could not be
        # established. Neither is safe to silently hand to the closer.
        return (2, updated, number)
    if review == "CHANGES_REQUESTED":
        return (3, updated, number)
    if review == "REVIEW_REQUIRED":
        return (4, updated, number)
    return (5, updated, number)


def list_agent_candidates(
    repo: str, specific_pr: int | None = None, limit: int = 12
) -> list[dict]:
    """Fetch, rank, and bound the PRs the LLM may inspect or modify.

    The output is bounded *after* exact ownership ranking. Do not pre-truncate
    the input by ``updatedAt``: ancestry and controller ownership are learned by
    the per-approved-PR lookups below, so an early cap can fill with work the
    controller owns and hide genuinely stuck PRs. If this fan-out becomes
    material, optimize those exact lookups without changing the candidate set.
    """
    if limit < 1:
        raise ValueError("candidate limit must be positive")
    fields = (
        "number,author,baseRefName,headRefName,isDraft,state,reviewDecision,"
        "updatedAt,baseRefOid,headRefOid,mergeable,assignees"
    )
    if specific_pr is not None:
        payload = _gh_json(
            ["pr", "view", str(specific_pr), "--repo", repo, "--json", fields]
        )
        prs = [payload]
    else:
        prs = _gh_json(
            [
                "pr",
                "list",
                "--repo",
                repo,
                "--state",
                "open",
                "--base",
                "main",
                "--limit",
                "1000",
                "--json",
                fields,
            ]
        )
    if not isinstance(prs, list):
        raise ValueError("GitHub PR response was not a list")
    safe = [pr for pr in prs if agent_candidate_decision(pr).eligible]
    if specific_pr is not None:
        return safe[:1]

    branch = _gh_json(["api", f"repos/{repo}/branches/main"])
    if not isinstance(branch, dict):
        raise ValueError("GitHub branch response was not an object")
    current_base_sha = str((branch.get("commit") or {}).get("sha") or "")
    if not current_base_sha:
        raise ValueError("GitHub branch response returned no head SHA")
    ranked = []
    for pr in safe:
        contains_current_base: bool | None = None
        controller_owned = False
        if str(pr.get("reviewDecision") or "").upper() == "APPROVED":
            head_sha = str(pr.get("headRefOid") or "")
            try:
                comparison = _gh_json(
                    [
                        "api",
                        f"repos/{repo}/compare/{current_base_sha}...{head_sha}",
                    ]
                )
                contains_current_base = _comparison_contains_base(
                    comparison, current_base_sha, head_sha
                )
                if contains_current_base:
                    details = _gh_json(
                        [
                            "pr",
                            "view",
                            str(pr["number"]),
                            "--repo",
                            repo,
                            "--json",
                            "isDraft,mergeStateStatus,statusCheckRollup",
                        ]
                    )
                    if not isinstance(details, dict):
                        raise ValueError("GitHub PR detail response was not an object")
                    controller_owned = _controller_owns_approved(
                        {**pr, **details}, contains_current_base
                    )
            except (subprocess.CalledProcessError, ValueError, json.JSONDecodeError):
                # Unknown ancestry/closing state stays in the shortlist. An API
                # failure must never silently route a potentially stuck PR away
                # from both lanes.
                contains_current_base = None
                controller_owned = False

        rank = _agent_action_rank(pr, contains_current_base, controller_owned)
        if rank is not None:
            ranked.append((rank, pr))
    ranked.sort(key=lambda row: row[0])
    return [pr for _, pr in ranked[:limit]]


def _write_outputs(path: str | None, values: dict[str, str]) -> None:
    for key, value in values.items():
        print(f"{key}={value}")
    if not path:
        return
    with Path(path).open("a", encoding="utf-8") as handle:
        for key, value in values.items():
            handle.write(f"{key}={value}\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    subparsers = parser.add_subparsers(dest="command", required=True)

    candidates = subparsers.add_parser(
        "candidates", help="list PR numbers the LLM shepherd may tend"
    )
    candidates.add_argument("--repo", required=True)
    candidates.add_argument("--specific-pr", type=int)
    candidates.add_argument("--limit", type=int, default=12)
    candidates.add_argument("--github-output")

    args = parser.parse_args(argv)
    prs = list_agent_candidates(args.repo, args.specific_pr, args.limit)
    _write_outputs(
        args.github_output,
        {"pr_numbers": ",".join(str(pr["number"]) for pr in prs)},
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
