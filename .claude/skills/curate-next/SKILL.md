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
3. **Fetch open curation issues assigned to the user.**
   ```bash
   gh issue list \
     --assignee @me \
     --state open \
     --label curation \
     --json number,title,assignees,body,createdAt \
     --limit 100
   ```
   The `--label curation` filter is what restricts to "new disease curation requests" — issues filed by `/claim-disease` carry the `curation,enhancement` labels and the title pattern `Curate <label> (<MONDO_ID>)`. If a contributor opens curation issues with a different label, document it in this skill rather than relaxing the filter.
4. **Filter to sole-assignee issues.** Drop any issue whose `assignees` array has more than one entry. The user explicitly wants solo work — an issue assigned to both `alice` and `bob` is a team task, even if the current user is `alice`. Do this filter in jq, not by hand:
   ```bash
   jq '[.[] | select((.assignees | length) == 1)]'
   ```
5. **Filter out issues with an existing PR.** For each remaining issue number `ISSUE_NUM`, check the authoritative GitHub linkage on the issue itself:
   ```bash
   # Authoritative: PRs GitHub has linked via closes/fixes/resolves keywords
   # (this is the same data the issue's "Development" sidebar shows)
   gh issue view "${ISSUE_NUM}" --json closedByPullRequestsReferences \
     -q '.closedByPullRequestsReferences | length'
   ```
   Skip the issue if the count is non-zero. A merged PR usually means the issue should already be closed, but stale links happen — be conservative.

   **Do NOT use `gh pr list --search "closes #${ISSUE_NUM}"` as a forward check.** GitHub's free-text search matches the literal string `#${ISSUE_NUM}` anywhere in PR body or commits, including unrelated occurrences like `ORPHA:${ISSUE_NUM}`. This produced a false positive in production on issue #2704 (Orphanet ID `ORPHA:2704` in PR #1992's body matched `#2704`). `closedByPullRequestsReferences` is structured GitHub linkage and avoids the trap.

   If `closedByPullRequestsReferences` is rejected as an unknown field by the local `gh` version, upgrade `gh` rather than falling back to the lossy text search.
6. **Sort and pick.** Sort the survivors by `number` ascending (oldest issue first — that's the conventional FIFO for a curation queue) and take the first N. If fewer than N survive, do not pad — report the shortfall in step 8.
7. **Extract the disease label and MONDO ID from each title.** Issue titles follow `Curate <label> (<MONDO_ID>)`. Parse with a regex; if a title does not match (e.g. an old hand-filed issue), skip it and note it in the final report rather than passing a garbled label to `/curate`.
8. **Dispatch /curate in parallel.** In a **single message**, launch N Agent tool calls — one per disease — using `subagent_type: general-purpose` so each agent has full tool access (`Tools: *`). `claude` works too on harnesses that register it as a catch-all type, but `general-purpose` is the canonical name across harnesses; prefer it for portability. Each agent's prompt MUST:
   - State the disease label and MONDO ID verbatim.
   - Quote any deep-research provider hints from the issue body (e.g. "using falcon", "using deep-research"). Default to **falcon** when none are mentioned.
   - Reference the GitHub issue number so the agent links the resulting PR back to it.
   - Instruct the agent to consult the `initiate-new-disorder-creation` skill for the full curation workflow (this is what `/curate` does — sub-agents cannot invoke slash commands directly, so this skill must be named in the prompt).
   - For `CURATE_ROOT_WITH_SUBTYPES` issues, note that subtypes should be modelled with `has_subtypes`.
   - **MUST tell the agent to create a git worktree of its own and `cd` into it, then use RELATIVE paths for every Read/Edit/Write/Bash file operation.** Never give the agent the parent checkout's absolute path as its working directory. In a real production incident, two of three agents took an absolute parent path from the prompt (`/Users/.../dismech-1`) and wrote `kb/disorders/<disease>.yaml` plus dozens of `references_cache/*.md` files into the parent checkout instead of their own worktree — branches were left empty and recovery required surgery. The agent prompt should include something like:

     ```
     Create your own git worktree (use the `superpowers:using-git-worktrees` skill) on a fresh branch off origin/main, then `cd` into that worktree. After `cd`, run `pwd` and confirm the path ends in `.claude/worktrees/<your-id>` BEFORE any file write. Use RELATIVE paths for all Read/Edit/Write/Bash calls in this session — never an absolute path that contains the parent checkout's location. Commit and push from inside the worktree.
     ```

   Dispatching all N in one message is the whole point — sequential dispatch defeats the skill. See `superpowers:dispatching-parallel-agents` if you need a refresher on parallel sub-agent semantics. Run the agents in the background (`run_in_background: true`) so the orchestrator regains control immediately and can report; you will be notified as each finishes.

   **After every agent finishes (or stalls), verify each branch has at least one commit:** `git log main..<branch> --oneline`. If empty, the agent's work is likely uncommitted in its worktree's working tree — or worse, leaked into the parent checkout. Check `git status` in the parent before dispatching another batch.
9. **Report.** After all agents finish, list:
   - Issues processed (number + label + agent result summary)
   - Issues skipped and why (already has PR / co-assigned / unparseable title)
   - The shortfall, if you delivered fewer than N curations

## Quick reference

| Step | Command |
|------|---------|
| Resolve user | `gh api user -q .login` |
| List my open curation issues | `gh issue list --assignee @me --state open --label curation --json number,title,assignees,body,createdAt --limit 100` |
| Filter sole-assignee | `jq '[.[] \| select((.assignees \| length) == 1)]'` |
| PR linking check | `gh issue view <ISSUE_NUM> --json closedByPullRequestsReferences -q '.closedByPullRequestsReferences \| length'` |
| Dispatch | Single message with N `Agent` calls, `subagent_type: general-purpose`, `run_in_background: true` |

## Common mistakes

- **Treating co-assigned issues as solo work.** `gh issue list --assignee @me` returns issues where the user is *an* assignee, not the *only* assignee. The jq length-1 filter in step 4 is mandatory.
- **Skipping the PR-existence check.** If a contributor opened a PR three days ago and is still under review, re-running `/curate` will overwrite their work and waste the reviewer's time. Always check `closedByPullRequestsReferences` on the issue before dispatching.
- **Using `gh pr list --search "closes #N"` as a PR-link check.** GitHub's free-text search matches the literal `#N` anywhere — including `ORPHA:N`, `MONDO:0000N`, line numbers in code blocks, etc. This caused a real false positive on issue #2704 (matched on `ORPHA:2704`). The structured `closedByPullRequestsReferences` field on the issue is the authoritative signal.
- **Running `/curate` sequentially.** Sequential dispatch defeats the skill. All N Agent calls go in one message.
- **Silently picking fewer than N.** If only 2 issues survive when the user asked for 5, say so explicitly in the report. Do not pad the count with co-assigned or PR-linked issues just to hit N.
- **Hardcoding the GitHub username.** Always resolve via `gh api user -q .login` so the skill works for any contributor.
- **Defaulting N when the user didn't supply it.** This skill requires an explicit N — unlike `/claim-disease`, there is no sensible default for "how many of your in-flight assignments to attack at once." Ask.
- **Looking up MONDO IDs from `dashboard/priority.json`.** That is `/claim-disease`'s job. This skill is strictly issue-driven — every disease curated comes from an existing GitHub issue title.
- **Trying to call `/curate` from inside a sub-agent.** Slash commands are not available in sub-agent context. Inline the `/curate` instructions (consult `initiate-new-disorder-creation`, use falcon by default) into the agent prompt.
- **Giving the agent the parent checkout's absolute path as its working directory.** If the dispatch prompt says `Working directory: /Users/.../dismech-1`, the agent will happily use that path in its `Write` tool calls and your new disorder YAML lands in the parent checkout instead of the agent's worktree. The branch will be empty (no commits) and the work is hard to attribute when multiple agents leak in parallel. Always instruct the agent to create its own worktree, `cd` into it, and use relative paths.
- **Skipping the post-dispatch branch-commit audit.** Even with a worktree instruction, an agent that stalls mid-write leaves uncommitted work in its worktree. If you don't check `git log main..<branch>` for each agent before deleting/pruning, you can lose draft YAMLs and fetched reference caches.

## Relationship to other skills

- **`/claim-disease N`** — files **new** curation issues for the top-N priority uncurated diseases. Use first if you have no open assignments.
- **`/curate <name>`** — curates a single disease end-to-end. This skill dispatches it in parallel.
- **`/curate-next N`** — this skill. Reads your assigned-but-unstarted curation issues and runs the `/curate` workflow on the first N.

A typical batch session is `/claim-disease 5` (file 5 issues) → `/curate-next 5` (curate them in parallel).
