"""Open one issue as its own interactive Claude Code session.

    just launch-issue-session 14182 --dry-run
    just launch-issue-session 14182 --model opus --note "only fix the error message"

Run from the repo root, and only for an issue the user named. In order,
stopping at the first failure:

  1. checks that `gh`, `git`, `tmux` and `claude` are installed, before
     changing anything;
  2. reads the issue live and refuses one that is closed, assigned to someone
     else (their hold), or a discussion;
  3. assigns it to the current user. The curation-scanner only picks up
     unassigned issues, so assignment keeps it off this one, and also takes
     the issue out of the scanner's pool; the launcher says so when it does it;
  4. creates a worktree at <worktree-root>/dismech-issue-<N> on a new branch
     issue-<N>-<slug> off origin/main;
  5. opens a window in the tmux session (created if needed) running `claude`
     interactively there, with a short first prompt naming the issue.

The prompt is the `claude` command's own argument; nothing is ever typed into
a running session. It never files or retitles a claim; `just check-claims`
stays the authority on claims. Location and names are configurable:

  --worktree-root  or DISMECH_WORKTREE_ROOT   (default ~/worktrees)
  --tmux-session   or DISMECH_TMUX_SESSION    (default dismech-issues)
  --claude-bin     or DISMECH_CLAUDE_BIN      (default claude)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
from pathlib import Path

from dismech.issue_queue.rules import (
    MONDO_TITLE,
    NON_ACTIONABLE,
    REPO,
    classify,
    label_names,
)

#: One line per lane: which repo skill or rule the session should start from.
#: Kept terse on purpose: the session runs in the repo and inherits CLAUDE.md
#: and every project skill, so restating SOPs here only crowds them out.
LANE_HINT = {
    "NEW_ENTRY": "Curate it with /curate (the initiate-new-disorder-creation workflow), deciding first whether "
    "it is a Disease, a Grouping, a subtype, or out of scope. Delete its stub in the PR.",
    "LIT_SCAN": "Augment only the entry the issue names; do not create a new one.",
    "PREPRINT_SCAN": "Augment only the entry the issue names; cite the preprint as PPR:<id> and never as sole support.",
    "KGAP_SCAN": "Augment only the entry the issue names; an unresolved gap becomes a KNOWLEDGE_GAP discussion, "
    "per CLAUDE.md.",
    "GENETICS_PASS": "Follow the issue body's own method; one PR per disease.",
    "EVIDENCE_REVIEW": "Use the evidence-claim-mismatch skill.",
    "CURATION": "Make exactly the change the issue asks for, to the evidence standard.",
    "SCHEMA": "Use the extend-schema skill, including deciding whether a schema change is warranted.",
    "TOOLING": "Reproduce first, and add a test that fails before the fix.",
    "BUG": "Reproduce first, and add a test that fails before the fix.",
    "DOCS": "Write for a human reader, and add any new page to the mkdocs.yml nav.",
    "ENTRY_REVIEW": "Review the entry the issue names in the way it asks; report findings on the issue and edit "
    "only what the review justifies.",
    "GENERAL": "The issue is not labelled by kind, so first say what kind of change it needs (KB content, "
    "schema, code, or docs) and follow the matching repo skill.",
}


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:30].rstrip("-")


def branch_name(number: int, title: str) -> str:
    m = MONDO_TITLE.match(title)
    return f"issue-{number}-{slugify(m.group('label') if m else title)}"


def build_prompt(
    number: int, title: str, lane: str, branch: str, note: str | None = None
) -> str:
    prompt = (
        f'Work {REPO}#{number}: "{title}". '
        f"Read it first with `gh issue view {number} --comments`; comments may have narrowed it. "
        f"{LANE_HINT[lane]} "
        f"You are already in your own worktree on branch {branch}; stay in it. "
        f"Open one PR with `Closes #{number}`. If the issue needs a decision it does not make, "
        f"ask me before guessing."
    )
    if note and note.strip():
        prompt += (
            " My instructions for this issue, which take precedence over the issue text "
            f"where they conflict: {note.strip()}"
        )
    return prompt


def run(args: list[str], dry: bool, mutating: bool = True) -> str:
    if dry and mutating:
        print("  would run:", shlex.join(args))
        return ""
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    if result.returncode:
        sys.exit(f"failed: {shlex.join(args)}\n{result.stderr.strip()}")
    return result.stdout


def main(argv: list[str] | None = None) -> None:
    p = argparse.ArgumentParser(
        prog="launch-issue-session",
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("issue", type=int)
    p.add_argument(
        "--model", help="model for the new session (default: your Claude Code default)"
    )
    p.add_argument(
        "--note",
        help="the user's instructions for this session, added to its first prompt",
    )
    p.add_argument(
        "--worktree-root",
        default=os.environ.get("DISMECH_WORKTREE_ROOT", "~/worktrees"),
    )
    p.add_argument(
        "--tmux-session",
        default=os.environ.get("DISMECH_TMUX_SESSION", "dismech-issues"),
    )
    p.add_argument(
        "--claude-bin", default=os.environ.get("DISMECH_CLAUDE_BIN", "claude")
    )
    p.add_argument(
        "--dry-run", action="store_true", help="print every step and change nothing"
    )
    a = p.parse_args(argv)

    if not (Path("justfile").exists() and Path("kb/disorders").is_dir()):
        sys.exit("run this from the dismech repo root")
    missing = [
        tool
        for tool in ("gh", "git", "tmux", a.claude_bin)
        if shutil.which(tool) is None
    ]
    if missing:
        sys.exit(
            f"not installed or not on PATH: {', '.join(missing)}. The launcher opens a tmux window running "
            f"`claude`; without them, open a worktree and start a session by hand."
        )

    me = run(["gh", "api", "user", "-q", ".login"], a.dry_run, mutating=False).strip()
    issue = json.loads(
        run(
            [
                "gh",
                "issue",
                "view",
                str(a.issue),
                "--repo",
                REPO,
                "--json",
                "number,title,labels,assignees,state",
            ],
            a.dry_run,
            mutating=False,
        )
    )
    if issue["state"] != "OPEN":
        sys.exit(f"#{a.issue} is {issue['state']}")
    assignees = [u["login"] for u in issue["assignees"]]
    if others := [u for u in assignees if u != me]:
        sys.exit(
            f"#{a.issue} is assigned to {','.join(others)}; not launching on someone else's hold"
        )
    lane = classify(issue)
    if lane in NON_ACTIONABLE:
        sys.exit(
            f"#{a.issue} is a {lane} issue; that is a conversation, not a session to launch"
        )

    branch = branch_name(a.issue, issue["title"])
    root = Path(a.worktree_root).expanduser()
    path = root / f"dismech-issue-{a.issue}"
    window = f"issue-{a.issue}"
    if path.exists():
        sys.exit(
            f"{path} already exists. If its session is still open: "
            f"tmux attach -t {a.tmux_session}:{window}. Otherwise remove the worktree first."
        )

    prompt = build_prompt(a.issue, issue["title"], lane, branch, a.note)
    claude = [a.claude_bin, "-n", f"#{a.issue} {issue['title'][:50]}"]
    if a.model:
        claude += ["--model", a.model]
    claude.append(prompt)

    print(f"#{a.issue} [{lane}] {issue['title']}")
    if lane == "NEW_ENTRY" and "claim" not in label_names(issue):
        print(
            "  note: this issue has no `claim` label, so it does not lock the disease; "
            "`just check-claims` will not see it"
        )
    if me not in assignees:
        run(
            ["gh", "issue", "edit", str(a.issue), "--repo", REPO, "--add-assignee", me],
            a.dry_run,
        )
        print(
            f"  note: assigned to {me}; the curation-scanner only picks up unassigned issues, so this "
            f"takes the issue out of its pool until it is unassigned"
        )
    run(["git", "fetch", "-q", "origin", "main"], a.dry_run)
    if not a.dry_run:
        root.mkdir(parents=True, exist_ok=True)
    run(["git", "worktree", "add", "-b", branch, str(path), "origin/main"], a.dry_run)

    has_session = (
        subprocess.run(
            ["tmux", "has-session", "-t", a.tmux_session],
            capture_output=True,
            check=False,
        ).returncode
        == 0
    )
    if has_session:
        tmux = [
            "tmux",
            "new-window",
            "-t",
            a.tmux_session,
            "-n",
            window,
            "-c",
            str(path),
        ]
    else:
        tmux = [
            "tmux",
            "new-session",
            "-d",
            "-s",
            a.tmux_session,
            "-n",
            window,
            "-c",
            str(path),
        ]
    run(tmux + [shlex.join(claude)], a.dry_run)

    print(
        f"\n{'would open' if a.dry_run else 'opened'}: tmux window {window} in session {a.tmux_session}"
    )
    print(f"  worktree {path}  branch {branch}")
    print(f"  watch it:   tmux attach -t {a.tmux_session}:{window}")
    print(
        "  once inside, tmux reads Ctrl-b before Claude does: press Ctrl-b, let go, then"
        " w (pick a window), n / p (next / previous) or d (detach, leaving it running)"
    )
    if a.dry_run:
        print(f"\nfirst prompt:\n  {prompt}")


if __name__ == "__main__":
    main()
