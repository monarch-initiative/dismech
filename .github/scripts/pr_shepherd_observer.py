#!/usr/bin/env python3
"""Resolve and probe read-only PR Shepherd candidates.

The model receives only the snapshot produced here. This script performs all
GitHub reads before the model starts and fails closed if candidate trust, head
identity, or check-rollup shape changes while the snapshot is assembled.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

TRUSTED_BOTS = frozenset(
    {
        "dragon-ai-agent",
        "dragon-ai-agent[bot]",
        "claude[bot]",
        "github-actions[bot]",
    }
)
TRUSTED_ASSOCIATIONS = frozenset({"OWNER", "MEMBER", "COLLABORATOR"})


class ObserverError(RuntimeError):
    """Raised when a candidate cannot be observed safely."""


def _required_string(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value:
        raise ObserverError(f"missing or invalid string field: {field}")
    return value


def candidate_from_pull(pull: dict[str, Any], repo: str) -> dict[str, Any] | None:
    """Return trusted, immutable candidate metadata or ``None``."""

    try:
        number = pull["number"]
        head = pull["head"]
        author = pull["user"]
        head_repo = head["repo"]["full_name"]
        head_ref = head["ref"]
        head_sha = head["sha"]
        author_login = author["login"]
        association = pull["author_association"]
    except (KeyError, TypeError) as error:
        raise ObserverError("pull response is missing trust metadata") from error

    if not isinstance(number, int) or isinstance(number, bool) or number <= 0:
        raise ObserverError("pull response has an invalid number")
    for value, field in (
        (head_repo, "head.repo.full_name"),
        (head_ref, "head.ref"),
        (head_sha, "head.sha"),
        (author_login, "user.login"),
        (association, "author_association"),
    ):
        _required_string(value, field)

    if head_repo != repo:
        return None
    if author_login in TRUSTED_BOTS:
        trust_basis = "trusted_bot"
    elif head_ref.startswith("claude/") and association in TRUSTED_ASSOCIATIONS:
        trust_basis = "trusted_collaborator_claude_branch"
    else:
        return None

    return {
        "number": number,
        "head_sha": head_sha,
        "head_repo": head_repo,
        "head_ref": head_ref,
        "author": author_login,
        "author_association": association,
        "trust_basis": trust_basis,
    }


def resolve_candidates(
    pulls: list[dict[str, Any]],
    repo: str,
    specific_pr: int | None,
) -> list[dict[str, Any]]:
    """Resolve a sorted deterministic allowlist from open pulls."""

    candidates = []
    for pull in pulls:
        candidate = candidate_from_pull(pull, repo)
        if candidate is None:
            continue
        if specific_pr is None or candidate["number"] == specific_pr:
            candidates.append(candidate)

    candidates.sort(key=lambda item: item["number"])
    if specific_pr is not None and not candidates:
        raise ObserverError(
            f"requested PR #{specific_pr} is not an open trusted candidate"
        )
    return candidates


def validate_rollup(observation: dict[str, Any], expected_head: str) -> None:
    """Validate exact-head identity and the complete rollup response shape."""

    expected_types = {
        "number": int,
        "title": str,
        "body": str,
        "url": str,
        "isDraft": bool,
        "createdAt": str,
        "updatedAt": str,
        "baseRefName": str,
        "baseRefOid": str,
        "headRefName": str,
        "headRefOid": str,
        "isCrossRepository": bool,
        "mergeStateStatus": str,
        "mergeable": str,
        "reviewDecision": str,
        "statusCheckRollup": list,
        "labels": list,
        "reviews": list,
        "latestReviews": list,
        "comments": list,
    }
    for field, expected_type in expected_types.items():
        value = observation.get(field)
        has_expected_type = (
            isinstance(value, int) and not isinstance(value, bool)
            if expected_type is int
            else isinstance(value, expected_type)
        )
        if not has_expected_type:
            raise ObserverError(f"pull observation has an invalid {field} field")
    if observation.get("headRefOid") != expected_head:
        raise ObserverError("candidate head changed while reading check rollup")
    rollup = observation.get("statusCheckRollup")
    if not isinstance(rollup, list):
        raise ObserverError("statusCheckRollup is not an array")

    for item in rollup:
        if not isinstance(item, dict):
            raise ObserverError("statusCheckRollup contains a non-object")
        typename = item.get("__typename")
        if typename == "CheckRun":
            if not all(
                isinstance(item.get(field), str)
                for field in ("name", "status", "conclusion")
            ):
                raise ObserverError("check-run rollup item has an invalid shape")
        elif typename == "StatusContext":
            if not all(
                isinstance(item.get(field), str) for field in ("context", "state")
            ):
                raise ObserverError("status-context rollup item has an invalid shape")
        else:
            raise ObserverError("statusCheckRollup contains an unknown item type")


def validate_check_runs(payload: dict[str, Any]) -> None:
    """Validate the REST checks probe used to prove ``checks: read``."""

    total_count = payload.get("total_count")
    if (
        not isinstance(total_count, int)
        or isinstance(total_count, bool)
        or not isinstance(payload.get("check_runs"), list)
    ):
        raise ObserverError("check-runs probe returned an invalid shape")


def _run_json(args: list[str]) -> Any:
    result = subprocess.run(
        args,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        command = " ".join(args[:3])
        raise ObserverError(f"GitHub read failed: {command}")
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as error:
        raise ObserverError("GitHub read returned invalid JSON") from error


def _atomic_write(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        dir=path.parent,
        delete=False,
    ) as handle:
        json.dump(value, handle, indent=2, sort_keys=True)
        handle.write("\n")
        temporary = Path(handle.name)
    temporary.replace(path)


def _flatten_pages(payload: Any) -> list[dict[str, Any]]:
    if not isinstance(payload, list):
        raise ObserverError("pull listing returned an invalid shape")
    if payload and all(isinstance(page, list) for page in payload):
        pulls = [pull for page in payload for pull in page]
    else:
        pulls = payload
    if not all(isinstance(pull, dict) for pull in pulls):
        raise ObserverError("pull listing contains a non-object")
    return pulls


def resolve(repo: str, specific: str, snapshot: Path, output: Path) -> None:
    if specific and not specific.isdigit():
        raise ObserverError("pr_number must contain digits only")
    specific_pr = int(specific) if specific else None
    pulls = _flatten_pages(
        _run_json(
            [
                "gh",
                "api",
                "--paginate",
                "--slurp",
                f"repos/{repo}/pulls?state=open&per_page=100",
            ]
        )
    )
    candidates = resolve_candidates(pulls, repo, specific_pr)
    _atomic_write(snapshot, {"repository": repo, "candidates": candidates})

    numbers = ",".join(str(item["number"]) for item in candidates)
    with output.open("a", encoding="utf-8") as handle:
        handle.write(f"has_candidates={'true' if candidates else 'false'}\n")
        handle.write(f"prs={numbers}\n")
        handle.write(f"snapshot={snapshot}\n")


def _live_candidate(repo: str, number: int) -> dict[str, Any]:
    pull = _run_json(["gh", "api", f"repos/{repo}/pulls/{number}"])
    if not isinstance(pull, dict):
        raise ObserverError("pull detail returned an invalid shape")
    candidate = candidate_from_pull(pull, repo)
    if candidate is None:
        raise ObserverError(f"PR #{number} no longer satisfies the trust gate")
    return candidate


def probe(repo: str, snapshot: Path) -> None:
    try:
        document = json.loads(snapshot.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ObserverError("candidate snapshot is missing or malformed") from error
    if document.get("repository") != repo or not isinstance(
        document.get("candidates"), list
    ):
        raise ObserverError("candidate snapshot has an invalid shape")

    enriched = []
    for expected in document["candidates"]:
        if not isinstance(expected, dict):
            raise ObserverError("candidate snapshot contains an invalid entry")
        number = expected.get("number")
        if not isinstance(number, int) or isinstance(number, bool):
            raise ObserverError("candidate snapshot contains an invalid entry")

        if _live_candidate(repo, number) != expected:
            raise ObserverError(f"PR #{number} changed before check-rollup probe")

        observation = _run_json(
            [
                "gh",
                "pr",
                "view",
                str(number),
                "--repo",
                repo,
                "--json",
                (
                    "number,title,body,url,isDraft,createdAt,updatedAt,"
                    "baseRefName,baseRefOid,headRefName,headRefOid,"
                    "isCrossRepository,mergeStateStatus,mergeable,"
                    "reviewDecision,statusCheckRollup,labels,reviews,"
                    "latestReviews,comments"
                ),
            ]
        )
        if not isinstance(observation, dict) or observation.get("number") != number:
            raise ObserverError(f"PR #{number} observation has an invalid shape")
        validate_rollup(observation, expected["head_sha"])

        checks = _run_json(
            [
                "gh",
                "api",
                "-H",
                "Accept: application/vnd.github+json",
                f"repos/{repo}/commits/{expected['head_sha']}/check-runs?per_page=1",
            ]
        )
        if not isinstance(checks, dict):
            raise ObserverError("check-runs probe returned a non-object")
        validate_check_runs(checks)

        if _live_candidate(repo, number) != expected:
            raise ObserverError(f"PR #{number} changed during check-rollup probe")
        enriched.append({**expected, "observation": observation})

    _atomic_write(snapshot, {"repository": repo, "candidates": enriched})


def main() -> int:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    resolve_parser = subparsers.add_parser("resolve")
    resolve_parser.add_argument("--repo", required=True)
    resolve_parser.add_argument("--specific", default="")
    resolve_parser.add_argument("--snapshot", type=Path, required=True)
    resolve_parser.add_argument("--github-output", type=Path, required=True)

    probe_parser = subparsers.add_parser("probe")
    probe_parser.add_argument("--repo", required=True)
    probe_parser.add_argument("--snapshot", type=Path, required=True)

    args = parser.parse_args()
    try:
        if args.command == "resolve":
            resolve(
                args.repo,
                args.specific,
                args.snapshot,
                args.github_output,
            )
        else:
            probe(args.repo, args.snapshot)
    except ObserverError as error:
        print(f"::error::{error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
