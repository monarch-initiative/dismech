#!/usr/bin/env python3
"""Repair additive CSV cache conflicts without checking out or executing PR code.

Run on a trusted main checkout. A private index overlays verified cache rows on
Git's merge result; everything else must retain that result's exact blob/mode.
Only a head-pinned fast-forward push of a two-parent merge commit is permitted.
Requires Git >= 2.38. Dry-run performs the same planning without remote writes.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path

from generated_cache_merge import UnsafeMerge, is_supported_cache_path, merge_cache_csv
from pr_shepherd_policy import agent_candidate_decision

OID = re.compile(r"[0-9a-f]{40}(?:[0-9a-f]{24})?\Z")
# Root-level JSON caches are never merge inputs. Inspect tree metadata only;
# in particular, the retired shared dataset cache must never be opened.
PROTECTED_CACHE = re.compile(r"cache/[^/]+\.json\Z")
FIELDS = (
    "number,author,assignees,baseRefName,headRefName,headRefOid,"
    "isCrossRepository,state,mergeable,updatedAt"
)


def process_env(*, write: bool = False) -> dict[str, str]:
    env = os.environ.copy()
    writer = env.pop("GH_CACHE_REPAIR_TOKEN", "")
    if write:
        if not writer:
            raise UnsafeMerge("write token is missing")
        env["GH_TOKEN"] = writer
    # Never inherit a caller's index, custom drivers, hooks, or signing config.
    for key in list(env):
        if key.startswith("GIT_"):
            env.pop(key)
    env.update(
        GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull, GIT_TERMINAL_PROMPT="0"
    )
    return env


class GitRepo:
    def __init__(self, path: Path):
        self.path = path

    def git(
        self,
        *args: str,
        input: bytes | None = None,
        check: bool = True,
        env: dict[str, str] | None = None,
    ) -> subprocess.CompletedProcess:
        return subprocess.run(
            [
                "git",
                "-C",
                str(self.path),
                "-c",
                "core.hooksPath=/dev/null",
                "-c",
                "commit.gpgSign=false",
                "-c",
                "core.attributesFile=/dev/null",
                *args,
            ],
            input=input,
            check=check,
            capture_output=True,
            env=env if env is not None else process_env(),
            timeout=180,
        )

    def tree(self, revision: str) -> dict[str, tuple[str, str]]:
        rows = self.git("ls-tree", "-rz", revision).stdout.split(b"\0")
        result = {}
        for row in filter(None, rows):
            info, path = row.split(b"\t", 1)
            mode, _kind, oid = info.decode("ascii").split()
            result[path.decode("utf-8")] = (mode, oid)
        return result


@dataclass(frozen=True)
class MergePlan:
    tree: str
    head: str
    base: str
    paths: tuple[str, ...]


def _merge_output(data: bytes) -> tuple[str, dict[str, dict[int, tuple[str, str]]]]:
    """Read NUL-delimited stages AND diagnostics; reject non-content conflicts."""
    fields = data.split(b"\0")
    tree = fields.pop(0).decode("ascii")
    if not OID.fullmatch(tree):
        raise UnsafeMerge("merge-tree returned no valid tree")
    stages: dict[str, dict[int, tuple[str, str]]] = {}
    while fields and fields[0]:
        info, path_bytes = fields.pop(0).split(b"\t", 1)
        mode, oid, stage = info.decode("ascii").split()
        path = path_bytes.decode("utf-8")
        by_stage = stages.setdefault(path, {})
        if int(stage) in by_stage or not OID.fullmatch(oid):
            raise UnsafeMerge("invalid merge stages")
        by_stage[int(stage)] = (mode, oid)
    if fields:
        fields.pop(0)
    while fields and fields[0]:
        count = int(fields.pop(0))
        if count < 1 or len(fields) < count + 2:
            raise UnsafeMerge("invalid merge diagnostic")
        paths = [fields.pop(0).decode("utf-8") for _ in range(count)]
        kind = fields.pop(0).decode("utf-8")
        fields.pop(0)  # Human-readable text is data, never shell input.
        if kind == "Auto-merging":
            continue
        if kind not in {"CONFLICT (contents)", "CONFLICT (add/add)"}:
            raise UnsafeMerge(f"unsupported merge diagnostic: {kind}")
        if any(path not in stages for path in paths):
            raise UnsafeMerge("conflict diagnostic has no matching stages")
    if any(fields):
        raise UnsafeMerge("unparsed merge diagnostics")
    return tree, stages


def build_merge(repo: GitRepo, head: str, base: str) -> MergePlan:
    """Plan an all-or-nothing resolution; never change HEAD, refs or worktree."""
    if not OID.fullmatch(head) or not OID.fullmatch(base):
        raise UnsafeMerge("expected full commit IDs")
    ancestors = repo.git("merge-base", "--all", head, base).stdout.decode().split()
    if len(ancestors) != 1:
        raise UnsafeMerge("expected exactly one merge base")
    trees = [repo.tree(rev) for rev in (ancestors[0], head, base)]
    all_paths = set().union(*trees)
    for path in all_paths:
        if PROTECTED_CACHE.fullmatch(path) and len({t.get(path) for t in trees}) != 1:
            raise UnsafeMerge(f"protected cache changed: {path}")
    merged = repo.git("merge-tree", "--write-tree", "-z", head, base, check=False)
    if merged.returncode == 0:
        raise UnsafeMerge("no conflicts to repair")
    if merged.returncode != 1:
        raise UnsafeMerge("merge-tree failed (Git >= 2.38 is required)")
    initial_tree, stages = _merge_output(merged.stdout)
    if not stages or any(not is_supported_cache_path(path) for path in stages):
        raise UnsafeMerge(
            "conflicts include unsupported paths; leave them for the shepherd"
        )

    # Check EVERY path before reading or generating ANY replacement blob.
    for path, entries in stages.items():
        expected = {i: tree[path] for i, tree in enumerate(trees, 1) if path in tree}
        if entries != expected or set(entries) not in ({1, 2, 3}, {2, 3}):
            raise UnsafeMerge(f"rename/deletion or unexpected stages: {path}")
        if any(mode != "100644" for mode, _ in entries.values()):
            raise UnsafeMerge(f"non-regular cache or mode change: {path}")
    replacements = {}
    for path, entries in stages.items():
        blobs = {
            i: repo.git("cat-file", "blob", oid).stdout
            for i, (_, oid) in entries.items()
        }
        replacements[path] = merge_cache_csv(path, blobs.get(1), blobs[2], blobs[3])

    with tempfile.TemporaryDirectory(prefix="cache-merge-index-") as tmp:
        env = process_env()
        env["GIT_INDEX_FILE"] = str(Path(tmp) / "index")
        repo.git("read-tree", initial_tree, env=env)
        for path, content in replacements.items():
            oid = (
                repo.git("hash-object", "-w", "--stdin", input=content)
                .stdout.decode()
                .strip()
            )
            repo.git("update-index", "--cacheinfo", f"100644,{oid},{path}", env=env)
        tree = repo.git("write-tree", env=env).stdout.decode().strip()
    before, after = repo.tree(initial_tree), repo.tree(tree)
    for path in set(before) | set(after):
        if path not in replacements and before.get(path) != after.get(path):
            raise UnsafeMerge(f"unexpected change outside resolved caches: {path}")
    # Git can merge disjoint case variants without noticing the collision.
    folded = [path.casefold() for path in after]
    if len(folded) != len(set(folded)):
        raise UnsafeMerge("merged tree has case-colliding paths")
    return MergePlan(tree, head, base, tuple(sorted(replacements)))


def gh(*args: str) -> object:
    result = subprocess.run(
        ["gh", *args],
        check=True,
        capture_output=True,
        text=True,
        env=process_env(),
        timeout=60,
    )
    return json.loads(result.stdout)


def current_pr(repo: str, number: int) -> dict:
    return gh(
        "pr",
        "view",
        str(number),
        "--repo",
        repo,
        "--json",
        FIELDS + ",statusCheckRollup",
    )


def repair_guard(pr: dict) -> None:
    decision = agent_candidate_decision(pr)
    if not decision.eligible:
        raise UnsafeMerge(decision.reason)
    if pr.get("isCrossRepository") is not False:
        raise UnsafeMerge("head must belong to this repository")
    if pr.get("headRefName") == "main" or not OID.fullmatch(pr.get("headRefOid", "")):
        raise UnsafeMerge("invalid head branch or SHA")
    if pr.get("mergeable") != "CONFLICTING":
        raise UnsafeMerge("PR is not currently conflicting")
    if not isinstance(pr.get("statusCheckRollup"), list):
        raise UnsafeMerge("checks were not returned")
    for check in pr["statusCheckRollup"]:
        if not isinstance(check, dict):
            raise UnsafeMerge("malformed check metadata")
        if "status" in check:
            if check["status"] != "COMPLETED" or not check.get("conclusion"):
                raise UnsafeMerge("checks are unfinished or incomplete")
        elif check.get("state") not in {"SUCCESS", "FAILURE", "ERROR"}:
            raise UnsafeMerge("status context is unfinished or incomplete")


def main_sha(repo: str) -> str:
    sha = gh("api", f"repos/{repo}/git/ref/heads/main")["object"]["sha"]
    if not OID.fullmatch(sha):
        raise UnsafeMerge("main lookup returned no SHA")
    return sha


def repair_one(local: GitRepo, repo: str, number: int, *, dry_run: bool) -> str:
    pr = current_pr(repo, number)
    repair_guard(pr)
    head, branch, base = pr["headRefOid"], pr["headRefName"], main_sha(repo)
    ref = f"refs/heads/{branch}"
    local.git("check-ref-format", ref)
    url = f"https://github.com/{repo}.git"
    # Fetch objects only, with the discovery token. No PR checkout, hooks,
    # project install, generator, or test ever executes in this writer job.
    local.git(
        "-c",
        "credential.helper=!gh auth git-credential",
        "fetch",
        "--no-tags",
        "--no-write-fetch-head",
        url,
        head,
        base,
    )
    plan = build_merge(local, head, base)
    if dry_run:
        return f"WOULD REPAIR {', '.join(plan.paths)} at {head[:12]}"

    fresh = current_pr(repo, number)
    repair_guard(fresh)
    if (
        fresh["headRefOid"] != head
        or fresh["headRefName"] != branch
        or main_sha(repo) != base
    ):
        raise UnsafeMerge(
            "head, branch, or main changed during planning; retry next sweep"
        )
    # An ordinary merge commit retains both histories. The explicit lease below
    # is compare-and-swap, not permission to rewrite history: the parent and
    # ancestry checks prove the update fast-forwards exactly the expected head.
    # A normal push alone misses a concurrent rewind or branch recreation.
    commit = (
        local.git(
            "-c",
            "user.name=PR Shepherd",
            "-c",
            "user.email=41898282+github-actions[bot]@users.noreply.github.com",
            "commit-tree",
            plan.tree,
            "-p",
            head,
            "-p",
            base,
            input=b"Merge main: preserve additive generated cache rows from both branches\n",
        )
        .stdout.decode()
        .strip()
    )
    parents = (
        local.git("rev-list", "--parents", "-n", "1", commit).stdout.decode().split()
    )
    if parents != [commit, head, base]:
        raise UnsafeMerge("unexpected merge commit parents")
    local.git("merge-base", "--is-ancestor", head, commit)
    local.git(
        "-c",
        "credential.helper=!gh auth git-credential",
        "push",
        "--porcelain",
        f"--force-with-lease={ref}:{head}",
        url,
        f"{commit}:{ref}",
        env=process_env(write=True),
    )
    return f"REPAIRED {', '.join(plan.paths)}; pushed {commit[:12]}, fresh CI/review follows"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repo", required=True)
    parser.add_argument("--specific-pr", type=int)
    parser.add_argument("--max-repairs", type=int, default=3)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", args.repo):
        parser.error("expected owner/repository")
    if args.max_repairs < 0 or (args.specific_pr is not None and args.specific_pr < 1):
        parser.error("invalid repair limit or PR number")
    if args.max_repairs == 0:
        return 0
    if not args.dry_run and not os.environ.get("GH_CACHE_REPAIR_TOKEN"):
        parser.error("execution requires GH_CACHE_REPAIR_TOKEN")
    prs = (
        [{"number": args.specific_pr}]
        if args.specific_pr
        else gh(
            "pr",
            "list",
            "--repo",
            args.repo,
            "--state",
            "open",
            "--base",
            "main",
            "--limit",
            "1000",
            "--json",
            FIELDS,
        )
    )
    if not args.specific_pr:
        prs = sorted(
            (
                pr
                for pr in prs
                if agent_candidate_decision(pr).eligible
                and pr.get("mergeable") in {"CONFLICTING", "UNKNOWN"}
            ),
            key=lambda pr: (pr.get("updatedAt", ""), pr["number"]),
        )
    local = GitRepo(Path.cwd())
    lines, repaired, errors = [], 0, 0
    for pr in prs:
        if repaired >= args.max_repairs:
            lines.append(
                "Repair budget reached; remaining PRs will be reconsidered next sweep."
            )
            break
        number = pr["number"]
        try:
            result = repair_one(local, args.repo, number, dry_run=args.dry_run)
            repaired += 1
        except UnsafeMerge as exc:
            result = f"DEFERRED: {exc}"
        except (subprocess.SubprocessError, ValueError, KeyError, OSError) as exc:
            # Never print command arguments/environment that might hold a token.
            result = f"ERROR: {type(exc).__name__}; no repair confirmed"
            errors += 1
        line = f"PR #{number}: {result}"
        print(line)
        lines.append(line)
    summary = (
        "Generated cache conflict repair\n\n"
        + "\n".join(lines or ["No candidates."])
        + "\n"
    )
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as handle:
            handle.write(summary)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
