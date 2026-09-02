#!/usr/bin/env python3
"""Verify that squash merges landing on ``main`` contain what their PR changed.

Passing tests are not evidence of correct history. In the April 2026 GitHub
merge-queue incident (see #2034), squash merges of multi-PR merge groups
produced commits that silently reverted changes from previously merged PRs --
and the test suite stayed green, because the reverted code still passed its
own tests. GitHub found that bug through customer reports, not monitoring.
With a merge queue planned for ``main`` (#10168) at ~50 merges/day, this
script is the local detection GitHub did not have: it recomputes, for every
squash commit a push lands on ``main``, the tree that merging the PR's head
into the previous ``main`` tip *should* have produced, and compares it against
the tree GitHub actually pushed.

The identity being checked::

    git merge-tree --write-tree <parent-of-C> <pr-head>   ==   C^{tree}

holds for a clean squash merge because GitHub's squash content is exactly the
merge result of the PR head and the base at merge time; a clean ``git merge
--squash`` produces the same index. A mismatch means the pushed commit does
not contain what merging that PR would have produced -- the incident
signature -- and the run fails so a human looks.

What is deliberately NOT verified:

- **Merge commits** (two parents, ~4.5% of landings): reported as skipped.
  The equivalent identity exists but the failure mode being guarded is the
  squash path, and GitHub's RCA said merge-method groups were unaffected.
- **Rebase merges and direct pushes**: a rebase merge maps one PR onto
  several commits none of which is the PR's ``merge_commit_sha`` recorded
  here, and a direct push has no PR at all. Both are reported as skipped.
- **PRs whose recorded ``merge_commit_sha`` does not match the commit**:
  skipped with a note rather than guessed at -- a wrong guess either way
  (false alarm, or false clearance) is worse than an honest "could not
  verify".

Two known false-positive sources, accepted rather than hidden: the PR's
``head.sha`` is read from the *current* PR payload, which equals the head at
merge time for the normal delete-branch-on-merge flow but can diverge if a
branch is reused after merging; and ``git merge-tree`` applies local
merge-ort rename-detection defaults where GitHub's merge machinery applies
its own. Both directions of disagreement surface as ``MISMATCH`` -- if an
alarm fires, compare the trees by hand before declaring an incident.

A conflicted ``merge-tree`` result is reported as unverifiable rather than a
mismatch: GitHub would not have auto-merged a conflicting pair, so hitting one
here means our reconstruction (usually the head SHA) is wrong, not that the
merge is.

Requires git >= 2.38 (``merge-tree --write-tree``) and, for PR lookups, a
``gh`` CLI authenticated for the repository. Run from anywhere inside a clone
whose history includes the commit range; blobs may be lazily fetched if the
clone is partial.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass

SQUASH_SUBJECT_RE = re.compile(r"\(#(\d+)\)\s*$")

VERIFIED = "VERIFIED"
MISMATCH = "MISMATCH"
SKIPPED_MERGE_COMMIT = "SKIPPED_MERGE_COMMIT"
SKIPPED_NO_PR_NUMBER = "SKIPPED_NO_PR_NUMBER"
SKIPPED_PR_MAPPING = "SKIPPED_PR_MAPPING"
SKIPPED_LOOKUP_ERROR = "SKIPPED_LOOKUP_ERROR"
UNVERIFIABLE = "UNVERIFIABLE"


@dataclass
class Result:
    commit: str
    status: str
    detail: str
    pr_number: int | None = None


def pr_number_from_subject(subject: str) -> int | None:
    """The PR number a GitHub squash/merge subject line ends with, if any."""
    match = SQUASH_SUBJECT_RE.search(subject.strip())
    return int(match.group(1)) if match else None


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], check=True, capture_output=True, text=True
    ).stdout.strip()


def gh_pr(repo: str, number: int) -> dict:
    out = subprocess.run(
        [
            "gh", "api", f"repos/{repo}/pulls/{number}",
            "--jq", "{head_sha: .head.sha, merge_commit_sha: .merge_commit_sha}",
        ],
        check=True, capture_output=True, text=True,
    ).stdout
    return json.loads(out)


HEX_OID_RE = re.compile(r"^[0-9a-f]{40,64}$")


def merge_tree(parent: str, head: str) -> tuple[str | None, str]:
    """(tree oid, outcome) where outcome is 'clean', 'conflict', or an error.

    Conflict and invocation failure are different stories, and the log must
    not tell the conflict story about a broken invocation. Exit codes alone
    cannot separate them -- git 2.43 exits 1 both for a conflicted merge and
    for "not something we can merge" -- so the discriminator is whether
    stdout's first line is a tree OID (a conflicted --write-tree run still
    writes one; a failed lookup writes none).
    """
    proc = subprocess.run(
        ["git", "merge-tree", "--write-tree", parent, head],
        check=False, capture_output=True, text=True,
    )
    first = proc.stdout.splitlines()[0].strip() if proc.stdout else ""
    tree = first if HEX_OID_RE.match(first) else None
    if proc.returncode == 0 and tree:
        return tree, "clean"
    if tree:
        return tree, "conflict"
    message = (proc.stderr.strip() or proc.stdout.strip())[:200]
    return None, f"merge-tree failed: {message}"


def _have_commit(sha: str) -> bool:
    return subprocess.run(
        ["git", "cat-file", "-e", f"{sha}^{{commit}}"],
        check=False, capture_output=True,
    ).returncode == 0


def ensure_commit(
    sha: str, remote: str = "origin", pr_number: int | None = None
) -> bool:
    """Make ``sha`` available locally, fetching it if necessary.

    Fetch-by-SHA works on github.com but is a server-configuration-dependent
    capability; ``refs/pull/<n>/head`` is the guaranteed-present ref, so it
    is the fallback when a PR number is known.
    """
    if _have_commit(sha):
        return True
    subprocess.run(
        ["git", "fetch", "--no-tags", remote, sha],
        check=False, capture_output=True,
    )
    if _have_commit(sha):
        return True
    if pr_number is not None:
        subprocess.run(
            ["git", "fetch", "--no-tags", remote, f"refs/pull/{pr_number}/head"],
            check=False, capture_output=True,
        )
    return _have_commit(sha)


def verify_commit(repo: str, commit: str) -> Result:
    parents = git("rev-list", "--parents", "-n", "1", commit).split()[1:]
    if len(parents) != 1:
        return Result(
            commit, SKIPPED_MERGE_COMMIT,
            f"{len(parents)} parents; only single-parent squash commits "
            "are verified")
    subject = git("log", "-n", "1", "--format=%s", commit)
    number = pr_number_from_subject(subject)
    if number is None:
        return Result(commit, SKIPPED_NO_PR_NUMBER,
                      f"no trailing PR number in subject {subject!r}")
    try:
        pr = gh_pr(repo, number)
    except subprocess.CalledProcessError as exc:
        return Result(commit, SKIPPED_LOOKUP_ERROR, pr_number=number,
                      detail=f"PR lookup failed: {exc.stderr.strip()[:200]}")
    except OSError as exc:
        return Result(commit, SKIPPED_LOOKUP_ERROR, pr_number=number,
                      detail=f"PR lookup failed: {exc}")
    if pr["merge_commit_sha"] != commit:
        return Result(
            commit, SKIPPED_PR_MAPPING, pr_number=number,
            detail=(
                "PR's recorded merge_commit_sha is "
                f"{pr['merge_commit_sha']} (rebase merge, or subject "
                "number is not this commit's PR)"
            ),
        )
    head = pr["head_sha"]
    if not ensure_commit(head, pr_number=number):
        return Result(commit, UNVERIFIABLE, pr_number=number,
                      detail=f"could not fetch PR head {head}")
    expected, outcome = merge_tree(parents[0], head)
    if outcome == "conflict":
        return Result(commit, UNVERIFIABLE, pr_number=number,
                      detail="merge-tree reported conflicts; reconstruction "
                             "does not represent the merge GitHub performed")
    if outcome != "clean" or expected is None:
        return Result(commit, UNVERIFIABLE, pr_number=number, detail=outcome)
    actual = git("rev-parse", f"{commit}^{{tree}}")
    if expected == actual:
        return Result(commit, VERIFIED, pr_number=number,
                      detail=f"tree {actual[:12]} matches recomputed merge")
    return Result(
        commit, MISMATCH, pr_number=number,
        detail=(
            f"pushed tree {actual} != recomputed merge tree {expected} "
            f"(parent {parents[0][:12]}, PR head {head[:12]}) -- the commit "
            "does not contain what merging this PR into its parent produces"
        ),
    )


def emit_output(name: str, value: str) -> None:
    """Append a step output when running under GitHub Actions."""
    path = os.environ.get("GITHUB_OUTPUT")
    if path:
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(f"{name}={value}\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--repo", required=True, help="owner/name for PR lookups")
    parser.add_argument("--before", required=True,
                        help="main tip before the push (github.event.before)")
    parser.add_argument("--after", required=True,
                        help="main tip after the push (github.event.after)")
    args = parser.parse_args()
    emit_output("mismatch", "false")

    if set(args.before) == {"0"}:
        # A branch-creation push reports the null SHA; nothing to compare.
        print(f"before-commit {args.before} is the null SHA; nothing verified")
        return 0
    if not ensure_commit(args.before):
        print(f"before-commit {args.before} unavailable; nothing verified")
        return 0
    commits = git(
        "rev-list", "--first-parent", "--reverse", f"{args.before}..{args.after}"
    ).split()
    results = []
    for c in commits:
        # A crash on one commit must not abort the run (nor, upstream, be
        # mistaken for a mismatch): contain it as UNVERIFIABLE and move on.
        try:
            results.append(verify_commit(args.repo, c))
        except (subprocess.CalledProcessError, OSError) as exc:
            results.append(Result(c, UNVERIFIABLE,
                                  detail=f"verifier error: {exc}"))
    mismatches = [r for r in results if r.status == MISMATCH]
    for r in results:
        pr = f" PR #{r.pr_number}" if r.pr_number else ""
        line = f"{r.status}: {r.commit[:12]}{pr} -- {r.detail}"
        if r.status == MISMATCH:
            print(f"::error::{line}")
        print(line)
    counts: dict[str, int] = {}
    for r in results:
        counts[r.status] = counts.get(r.status, 0) + 1
    print(f"Checked {len(results)} commit(s): "
          + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    if mismatches:
        emit_output("mismatch", "true")
        return 1
    # Fail closed: a run where lookups or reconstruction failed for every
    # squash-shaped commit has verified nothing, which is the same silent
    # blindness this script exists to prevent. (A push whose only commits are
    # legitimately out of scope -- merge commits, direct pushes, rebase
    # mappings -- still passes; those are policy skips, not failures.)
    broken = counts.get(SKIPPED_LOOKUP_ERROR, 0) + counts.get(UNVERIFIABLE, 0)
    if broken and not counts.get(VERIFIED, 0):
        print("::error::verifier completed but verified nothing: "
              f"{broken} commit(s) hit lookup or reconstruction failures")
        return 2
    if broken:
        print(f"::warning::{broken} commit(s) could not be verified "
              "(lookup or reconstruction failure); see statuses above")
    return 0


if __name__ == "__main__":
    sys.exit(main())
