#!/usr/bin/env python3
"""Deterministic ingress policy for tending unassigned PRs from any author."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

AUTOMATED_HEAD_PREFIX = "auto/"


@dataclass(frozen=True)
class Decision:
    """A deterministic policy decision and its audit reason."""

    eligible: bool
    reason: str


def agent_candidate_decision(pr: dict) -> Decision:
    """Return whether the repair jobs may tend this PR, regardless of author.

    Draft state is deliberately absent: in DisMech, opening a PR places the work
    in the review queue.  Assignment, review state, and explicit workflow lanes
    carry lifecycle meaning; the GitHub draft bit does not.
    """
    state = str(pr.get("state") or "").upper()
    if state != "OPEN":
        return Decision(False, f"PR is not open (state={state or 'missing'})")
    if pr.get("baseRefName") != "main":
        return Decision(False, "base branch is not main")
    if pr.get("isCrossRepository") is not False:
        return Decision(False, "head does not belong to this repository")
    assignees = pr.get("assignees")
    if not isinstance(assignees, list):
        return Decision(False, "PR response omitted or malformed assignees")
    if assignees:
        logins = ", ".join(str(item.get("login") or "?") for item in assignees)
        return Decision(False, f"PR is assigned to {logins}")

    head = str(pr.get("headRefName") or "")
    if head.startswith(AUTOMATED_HEAD_PREFIX):
        return Decision(False, f"separately managed lane {AUTOMATED_HEAD_PREFIX!r}")

    return Decision(True, "unassigned PR outside separately managed automation lanes")


def _gh_json(args: list[str]) -> object:
    result = subprocess.run(["gh", *args], check=True, capture_output=True, text=True)
    return json.loads(result.stdout)


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


def _controller_owns_approved(pr: dict) -> bool:
    """Whether the closer can finish this PR without branch edits.

    The merge controller does not require the head to contain current main.
    Routing clean, approved but behind PRs here avoids spending every tending
    sweep refreshing branches that the merge queue already tests against main.
    """
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
    controller_owned: bool,
) -> tuple[int, str, int] | None:
    """Put abandoned review work ahead of branch maintenance."""
    review = str(pr.get("reviewDecision") or "").upper()
    updated = str(pr.get("updatedAt") or "")
    number = int(pr["number"])
    mergeable = str(pr.get("mergeable") or "").upper()

    if review == "CHANGES_REQUESTED":
        return (0, updated, number)
    if mergeable == "CONFLICTING":
        return (1, updated, number)
    if review == "APPROVED":
        if controller_owned:
            return None
        # Includes red/blocked PRs and unknown closing state. Neither is safe
        # to silently hand to the closer.
        return (2, updated, number)
    if review == "REVIEW_REQUIRED":
        return (3, updated, number)
    return (4, updated, number)


def list_agent_candidates(
    repo: str, specific_pr: int | None = None, limit: int = 12
) -> list[dict]:
    """Fetch, rank, and bound the PRs the LLM may inspect or modify.

    The output is bounded *after* exact ownership ranking. Do not pre-truncate
    the input by ``updatedAt``: controller ownership is learned by
    the per-approved-PR lookups below, so an early cap can fill with work the
    controller owns and hide genuinely stuck PRs. If this fan-out becomes
    material, optimize those exact lookups without changing the candidate set.
    """
    if limit < 1:
        raise ValueError("candidate limit must be positive")
    fields = (
        "number,baseRefName,headRefName,isDraft,state,reviewDecision,"
        "updatedAt,baseRefOid,headRefOid,mergeable,assignees,isCrossRepository"
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

    ranked = []
    for pr in safe:
        controller_owned = False
        # A known conflict always stays in the agent lane, so checking whether
        # the merge controller owns it cannot change the shortlist.
        if (
            str(pr.get("reviewDecision") or "").upper() == "APPROVED"
            and str(pr.get("mergeable") or "").upper() != "CONFLICTING"
        ):
            try:
                details = _gh_json(
                    [
                        "pr",
                        "view",
                        str(pr["number"]),
                        "--repo",
                        repo,
                        "--json",
                        "headRefOid,reviewDecision,mergeable,isDraft,mergeStateStatus,statusCheckRollup",
                    ]
                )
                if not isinstance(details, dict):
                    raise ValueError("GitHub PR detail response was not an object")
                # Never suppress a candidate using checks from a different
                # head, or an approval that disappeared during discovery.
                if (
                    details.get("headRefOid") == pr.get("headRefOid")
                    and details.get("reviewDecision") == "APPROVED"
                ):
                    controller_owned = _controller_owns_approved({**pr, **details})
            except (subprocess.CalledProcessError, ValueError, json.JSONDecodeError):
                # Unknown closing state stays in the shortlist. An API
                # failure must never silently route a potentially stuck PR away
                # from both lanes.
                controller_owned = False

        rank = _agent_action_rank(pr, controller_owned)
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
