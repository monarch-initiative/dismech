---
name: curate-next
description: Use when asked to curate the next N disease curation issues already assigned to the current GitHub user. Filters open issues to those where the user is the sole assignee and no PR exists yet, picks the first N, then dispatches /curate in parallel for each. Accepts a positional integer N between 1 and 8.
---

# curate-next

Curate the next N disease curation issues that are assigned **solely** to the current GitHub user and not yet covered by a PR. Dispatches `/curate` in parallel — one agent per disease.

## When to use

- "Curate my next 3 diseases"
- "/curate-next 5"
- "Take the next available curation assignments off my plate"

Skip when:
- The user names a specific disease — invoke `/curate <name>` directly instead.
- The user has no open curation assignments — invoke `/claim-disease N` first to file issues.
- The user wants to claim *and* curate in one step — that's a `/claim-disease` then `/curate-next` chain, not this skill alone.

## Inputs

- Required positional argument **N**: number of diseases to curate in parallel. Must be a positive integer between 1 and 8 inclusive.
- Invoked as `/curate-next 3`. If N is missing, non-integer, `<= 0`, or `> 8`, stop and ask the user to clarify rather than guess. The cap exists because each `/curate` flow is long-running and parallel sub-agents past 8 saturate the orchestrator's context.

## Workflow

1. **Validate N.** Parse the positional argument. Reject if missing, non-integer, `<= 0`, or `> 8` — ask the user rather than silently capping. Never default to a value the user did not provide.
2. **Resolve the current GitHub user**: `USER=$(gh api user -q .login)`. Use that login as the assignee filter and never hardcode a username.
3. **Shortlist with the shared selector.** One call does what used to be four
   hand-run filters:
   ```bash
   just select-issues N --mine --lane new-entry
   ```
   - `--mine` keeps issues assigned to the current user **and nobody else**. An
     issue assigned to both `alice` and `bob` is a team task, even if the
     current user is `alice` (`ASSIGNED_OTHER`); one assigned to nobody is not
     yours (`NOT_MINE`).
   - `--lane new-entry` keeps claim issues: the `claim` label, or the title
     `Curate <label> (<MONDO_ID>)` that `/claim-disease` writes.
   - The default `--prs active` drops an issue that an **open** PR will close or
     is linked to (`PR_ACTIVE`), from GitHub's own link and cross-reference
     records. A merged PR on a still-open issue is shown, not hidden. Run
     `just issue-prs <ISSUE_NUM>` to see any issue's PRs on their own.
   - `KB_COVERED` drops an issue whose MONDO ID or label the KB already curates,
     using the coverage index `tidy-stubs` uses. A `git grep` for the ID is too
     loose: it also matches a sibling entry's `differential_diagnoses`, which is
     not curation, and skipped real candidates that way.
   - `OPEN_PR` drops an issue when an open PR names its MONDO ID or label.
   - Survivors are ranked oldest first (after any `high-priority` label), the
     conventional FIFO for a curation queue, and the first N are the picks.
     Fewer than N prints `SHORTFALL`; do not pad. The `EXCLUDED` block gives
     the reason for every issue left out; carry it into the final report.

   If the selector prints a NOTE that the checkout is behind `origin/main`, run
   `git pull` on main and re-run: `KB_COVERED` reads the local `kb/`.

   **Do NOT use `gh pr list --search "closes #${ISSUE_NUM}"` as a PR-link check.**
   GitHub's free-text search matches the literal string `#${ISSUE_NUM}` anywhere
   in a PR body or commit, including `ORPHA:${ISSUE_NUM}`. This produced a false
   positive in production on issue #2704 (Orphanet ID `ORPHA:2704` in PR #1992's
   body matched `#2704`).
4. **Extract the disease label and MONDO ID from each title.** Titles follow
   `Curate <label> (<MONDO_ID>)`; the selector prints the MONDO ID under each
   pick. A claim with no MONDO ID in its title (`UNKEYED_CLAIM` beside it)
   cannot be passed to `/curate` safely: skip it and note it in the final
   report rather than passing a garbled label.
5. **Search other issues for the same disease.** The selector checks the KB and
   open PRs; it does not search other issues. Before dispatch:
   ```bash
   gh issue list --repo monarch-initiative/dismech --state all \
     --search "\"<MONDO_ID>\" OR \"<label>\"" \
     --json number,title,state,url,labels --limit 100
   ```
   The current issue itself is expected in the results. A `DOUBLE_CLAIM` note
   beside a pick means another open claim already has the same MONDO ID. Skip
   the candidate if another issue already covers the same disorder, and report
   the skip.
6. **Dispatch /curate in parallel.** In a **single message**, launch N Agent tool calls — one per disease — using `subagent_type: general-purpose` so each agent has full tool access (`Tools: *`). `claude` works too on harnesses that register it as a catch-all type, but `general-purpose` is the canonical name across harnesses; prefer it for portability. Each agent's prompt MUST:
   - State the disease label and MONDO ID verbatim.
   - State that the duplicate preflight against the latest KB, open PRs, and all
     issues has already been performed, and tell the agent to repeat it before
     writing files if its worktree is created later from stale refs.
   - Quote any deep-research provider hints from the issue body (e.g. "using falcon", "using deep-research"). Default to **falcon** when none are mentioned.
   - Reference the GitHub issue number so the agent links the resulting PR back to it.
   - Instruct the agent to consult the `initiate-new-disorder-creation` skill for the full curation workflow (this is what `/curate` does — sub-agents cannot invoke slash commands directly, so this skill must be named in the prompt).
   - Tell the agent to decide **what the concept should be** before curating: a `kb/disorders/` Disease, a `kb/groupings/` Grouping, a `has_subtypes` entry on an existing disease, or out of scope. A disorder entry needs one reasonably conserved pathograph; a union of distinct diseases is a grouping. If it turns out to be a grouping or out of scope, the right output is to record that in the stub's `entry_type` with the reasoning in `notes` — that is a completed curation, not a failed one. See `docs/curation-stubs.md`.
   - Tell the agent the curation PR should **delete the disease's stub** (`stubs/<Name>.yaml`) alongside adding the KB entry, and carry `Closes #<issue>` so merging releases the claim. Forgetting the stub does not fail anything — stubs are informative, and a periodic `just tidy-stubs --apply` sweeps stale ones.
   - **MUST tell the agent to create a git worktree of its own and `cd` into it, then root every Read/Edit/Write/Bash file operation in the worktree's path — never in the parent checkout's path.** Never give the agent the parent checkout's absolute path as its working directory. In a real production incident, two of three agents took an absolute parent path from the prompt (`/Users/.../dismech-1`) and wrote `kb/disorders/<disease>.yaml` plus dozens of `references_cache/*.md` files into the parent checkout instead of their own worktree — branches were left empty and recovery required surgery. The agent prompt should include something like:

     ```
     Create your own git worktree (use the `superpowers:using-git-worktrees` skill) on a fresh branch off `origin/main`, then `cd` into that worktree. After `cd`, run `pwd` and confirm the printed path is the worktree's path and is NOT the parent checkout's path BEFORE any file write. For Read/Edit/Write tool calls (which require absolute paths), use absolute paths rooted in the worktree — never an absolute path that contains the parent checkout's location. For Bash calls, prefer relative paths after `cd`-ing into the worktree. Commit and push from inside the worktree.
     ```

   Dispatching all N in one message is the whole point — sequential dispatch defeats the skill. See `superpowers:dispatching-parallel-agents` if you need a refresher on parallel sub-agent semantics. Run the agents in the background (`run_in_background: true`) so the orchestrator regains control immediately and can report; you will be notified as each finishes.

   **After every agent finishes (or stalls), verify each branch has at least one commit:** `git log origin/main..<branch> --oneline`. If empty, the agent's work is likely uncommitted in its worktree's working tree — or worse, leaked into the parent checkout. Check `git status` in the parent before dispatching another batch.
7. **Report.** After all agents finish, list:
   - Issues processed (number + label + agent result summary)
   - Issues skipped and why (duplicate KB/PR/issue / already has PR / co-assigned / unparseable title)
   - The shortfall, if you delivered fewer than N curations

## Quick reference

| Step | Command |
|------|---------|
| Shortlist (sole assignee, claim issues, no active PR, not in the KB, no open PR) | `just select-issues N --mine --lane new-entry` |
| PRs attached to one issue | `just issue-prs <ISSUE_NUM>` |
| Other issues on the same disease | `gh issue list --state all --search '"<MONDO_ID>" OR "<label>"'` |
| Dispatch | Single message with N `Agent` calls, `subagent_type: general-purpose`, `run_in_background: true` |

## Common mistakes

- **Treating co-assigned issues as solo work.** `gh issue list --assignee @me` returns issues where the user is *an* assignee, not the *only* assignee. `--mine` is what makes the shortlist solo-only; do not swap it for `--assignee @me`.
- **Skipping the PR-existence check.** If a contributor opened a PR three days ago and is still under review, re-running `/curate` will overwrite their work and waste the reviewer's time. The selector's default `--prs active` drops those; never pass `--prs ignore` here.
- **Skipping the duplicate preflight.** The current issue may have been filed
  before another agent opened a PR or before a newer disorder entry reached
  `origin/main`. Re-check latest KB, all PRs, and all issues immediately before
  dispatch.
- **Using `gh pr list --search "closes #N"` as a PR-link check.** GitHub's free-text search matches the literal `#N` anywhere — including `ORPHA:N`, `MONDO:0000N`, line numbers in code blocks, etc. This caused a real false positive on issue #2704 (matched on `ORPHA:2704`). `just issue-prs N` reads GitHub's structured link and cross-reference records instead.
- **Running `/curate` sequentially.** Sequential dispatch defeats the skill. All N Agent calls go in one message.
- **Silently picking fewer than N.** If only 2 issues survive when the user asked for 5, say so explicitly in the report. Do not pad the count with co-assigned or PR-linked issues just to hit N.
- **Hardcoding the GitHub username.** The selector resolves the current user itself (`gh api user`); never pass a login.
- **Defaulting N when the user didn't supply it.** This skill requires an explicit N — unlike `/claim-disease`, there is no sensible default for "how many of your in-flight assignments to attack at once." Ask.
- **Looking up MONDO IDs from the stub queue in `stubs/`.** That is `/claim-disease`'s job. This skill is strictly issue-driven — every disease curated comes from an existing GitHub issue title.
- **Trying to call `/curate` from inside a sub-agent.** Slash commands are not available in sub-agent context. Inline the `/curate` instructions (consult `initiate-new-disorder-creation`, use falcon by default) into the agent prompt.
- **Giving the agent the parent checkout's absolute path as its working directory.** If the dispatch prompt says `Working directory: /Users/.../dismech-1`, the agent will happily use that path in its `Write` tool calls and your new disorder YAML lands in the parent checkout instead of the agent's worktree. The branch will be empty (no commits) and the work is hard to attribute when multiple agents leak in parallel. Always instruct the agent to create its own worktree, `cd` into it, and root every file operation in the worktree's path (absolute for Read/Edit/Write, relative is fine for Bash post-`cd`).
- **Skipping the post-dispatch branch-commit audit.** Even with a worktree instruction, an agent that stalls mid-write leaves uncommitted work in its worktree. If you don't check `git log origin/main..<branch>` for each agent before deleting/pruning, you can lose draft YAMLs and fetched reference caches.

## Relationship to other skills

- **`/claim-disease N`** — files **new** curation issues for the top-N priority uncurated diseases. Use first if you have no open assignments.
- **`/curate <name>`** — curates a single disease end-to-end. This skill dispatches it in parallel.
- **`/curate-next N`** — this skill. Reads your assigned-but-unstarted curation issues and runs the `/curate` workflow on the first N.
- **`browse-issues`** — lets the user browse, search and choose among every kind of open issue, not only claims, and opens one issue they name as an interactive session. Its selector (`just select-issues`) is the one step 3 runs.

A typical batch session is `/claim-disease 5` (file 5 issues) → `/curate-next 5` (curate them in parallel).
