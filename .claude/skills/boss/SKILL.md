---
name: boss
description: Use ONLY when the user explicitly asks to orchestrate parallel external agents (Codex or Claude Code) in tmux sessions via tp (tmux-pilot). Or when a user tells you that you're the boss or orchestrator. You can also use this if you are an operclaw agent. NEVER auto-invoke for a generic "do this in parallel" request. For in-process subagents, use superpowers:dispatching-parallel-agents instead.
argument-hint: [ "curate" | "new" | "status" | "kill" | "research" | <QUESTION> ] [INFO]
---

# boss: orchestrate multiple agents in the dismech repo

## Overview

Use this skill when the user wants you to orchestrate one of more dismech jobs, in such a way the user has observability via the `tmux` wrapper `tp`

Ground rules:

* bosses are knowledgeable about dismech but delegate all work involving editing files
* bosses will answer questions in response to a user, and may do preliminary research, but if it turns into something bigger, should be delegated to an agent
* bosses delegate reviews to the claude github actions review; they may give their own perspective but reviewers decisions must not be overridden
* bosses proactively keep things moving with high autonomy, and ask the human to resolve complex difficulties
* bosses should understand that the agents they delegate to are knowledgeable with access to same CLAUDE.md, so no need for duplicate information

Example user invocations:

* `/boss curate foo syndrome`
   * user intent: create a new tp session to curate a new disease
   * SOP:
      * create an issue (may be skipped): use `gh`.
      * start a tmux/tp session: `tp new dismech-issue-NNNN-<handle> --profile codex --repo ~/repos/dismech --branch feat/dismech-issue-NNNN-<handle> --description <desc> --prompt "/curate <DISEASE> <INFO>"`
* `/boss status`
   * user intent: I want to know the status of all sessions in this repo
      - are they active?
      - is the agent on the right track? If not, use `tp send ...`
      - is there a PR? What is it?
      - is the PR passing?
      - has the PR been reviewed? If so, was it approved? If not, send `tp send <name> "address comments in #<NN>`
      - is the PR in conflict? I so, prompt the agent to fix: `tp send ...`
* `/boss status`
   * user intend: PR is merged, and I don't need to do further work


## About

Turn the main session into an **orchestrator of external agents running in tmux**. Each worker is a Codex or Claude Code process inside its own tmux session, on its own branch, in its own git worktree. Boss observes and steers via `tp` (tmux-pilot) — never via raw `tmux send-keys`. Boss does not write code itself.

**Core principle:** one worker = one task = one branch = one worktree.

## When NOT to use

- The user did not explicitly invoke boss / tp / tmux-pilot / "external agents". A bare "do these in parallel" is **not** a boss invocation — use `superpowers:dispatching-parallel-agents` (in-process subagents) instead.
- Single-task or strictly sequential work — just do it directly.
- Tasks have cross-dependencies. Boss assumes **embarrassingly parallel** work (in dismech: one PR per disease). Serialize dependent work yourself.

## Hard rules

1. **One task, one session, one branch, one worktree.** Never reuse a session for a second task.
2. **Every worker gets its own isolated worktree under `~/worktrees/`** (`tp`'s default). Multiple boss-managed agents run in parallel on different branches — they **cannot share a worktree** (git only permits one worktree per branch), **cannot reuse the orchestrator's checkout**, and **must never be placed inside the repo** (`.worktrees/`, `.claude/worktrees/`, `workdirs/`, etc.). Isolation is the whole point of the parallel-agents model: one agent per `~/worktrees/<slug>/`, period.
3. **Use `tp` exclusively for agent control** — `tp new`, `tp send`, `tp peek`, `tp status`, `tp ls`, `tp set`, `tp kill`, `tp clean`. **Never** use raw `tmux send-keys` or `tmux capture-pane` for agent interaction. Read-only `tmux list-sessions` is acceptable if `tp` cannot cover it, but prefer `tp ls --json`.
4. **Default profile is `codex`.** Use `--profile claude` only when the user says so or the task is reasoning/review-heavy rather than mechanical.
5. **Issue linkage:**
   - Multi-commit work: `--issue N` is required. `tp` pulls the issue title into `@desc` and derives a branch like `fix/N-<slug>`.
   - Single-commit chore: `--issue` optional; `-d "description"` is enough and you pick the slug.
6. **Every `tp send` after session creation uses `--wait`.** Agents are not always at a sendable prompt; `--wait` blocks until they are.
7. **NEVER use local `git rebase` to resolve conflicts on curation branches.** Use GitHub's server-side "Update branch" API instead:
   ```bash
   gh api repos/monarch-initiative/dismech/pulls/PR_NUMBER/update-branch \
     -X PUT -f expected_head_sha="$(git rev-parse HEAD)"
   ```
   This is the same as GitHub's "Update branch" button: it merges `main` into the PR branch server-side, touches only conflicting files, and avoids local working-tree pollution. If it succeeds, `git pull` in the worker worktree and re-run validation. If GitHub reports unresolvable conflicts, set `@status waiting-human` and report the conflicting files. Do **not** attempt local resolution. See #1430 and #1575.
8. **If `tp` has friction, talk to Chris** and/or file an issue at `cmungall/tmux-pilot`. **Do not** fall back to raw `tmux send-keys` without explicit permission.

## Workflow

Generally the orchestrator should be run as an agent from an up to date main branch; not from a worktree

```
plan → dispatch → monitor → steer → complete → clean
```

### 1. Plan

Use TodoWrite. One item per task. For each, note:

- **Slug** (session name): short (< 20 chars), lowercase, hyphens. **Do NOT prefix with the repo name.** `tp` prepends the repo basename to the worktree path automatically, so a `dismech-` prefix produces a doubled path like `~/worktrees/dismech-dismech-curate-ipf` (cmungall/tmux-pilot#23). Use `curate-prpf31`, not `dismech-curate-prpf31`.
- **GH issue number** (if multi-commit — required per rule 5)
- **Profile** (default `codex`)
- **One-sentence description** (→ `@desc`)
- **Initial prompt** (one line, terse — see step 2.3 below)

Confirm the plan with the user before dispatching if there are more than ~3 tasks or if issue linkage is ambiguous.

### 2. Dispatch — ordered sequence, do not skip steps

`tp new` bundles worktree creation, branch creation, session start, agent launch, and prompt delivery into one call. Several of those silently fail or drift in known ways. Always verify each step.

#### 2.1 Confirm or create the GH issue (multi-commit only)

Per rule 5, multi-commit work requires `--issue N`. If no existing issue covers the task, file one:

```bash
gh issue create --repo monarch-initiative/dismech \
  --title "Add dismech entry: PRPF31-related retinitis pigmentosa; fixes #<NNN>" \
  --body "..."
# → capture the issue number, e.g. 1081
```

For a single-commit chore, skip this and use `-d "description"` in the next step.

#### 2.2 Run `tp new`

```bash
# Multi-commit, issue-driven
tp new curate-prpf31 --profile codex \
  --repo ~/repos/dismech \
  --issue 1081 \
  --branch feat/dismech-prpf31_retinitis_pigmentosa \
  --prompt "curate PRPF31-related retinitis pigmentosa"
```

```bash
# Single-commit chore, no issue
tp new fix-maxo-typo --profile codex \
  --repo ~/repos/dismech \
  --branch fix/maxo-list-typo \
  -d "Fix MAXO term list typo in CLAUDE.md" \
  --prompt "fix the typo in the MAXO terms list in CLAUDE.md and open a PR"
```

What `tp new` does, atomically in one call:
- creates an isolated worktree at `~/worktrees/<repo>-<slug>/`
- creates the branch (override auto-derived name with `--branch` to match dismech convention: `feat/dismech-<snake_case>` for new disorders)
- starts a detached tmux session
- launches the agent (codex / claude) inside the worktree
- attempts to type the `--prompt` as the first user turn

**Expect `tp new` to exit non-zero with `Timed out waiting for session to become ready`.** This is cmungall/tmux-pilot#22 — `tp new --prompt` races agent startup and frequently drops the prompt. A timeout exit does **not** mean the dispatch failed; it means readiness detection gave up before the agent's TUI finished rendering. Always verify with the next steps. Empirically, `--prompt` lands successfully on roughly 1 in 5 first attempts, so plan for step 2.4 (redeliver) to run on most dispatches.

**Parallel-dispatch cancellation gotcha.** If you fire multiple `tp new` calls in a single parallel batch (e.g., multiple Bash tool uses in one message), a timeout exit in one call can **cancel the sibling calls mid-flight**. The cancelled calls' tmux sessions may still have been partially created by `tp` before cancellation (session creation is front-loaded; readiness detection is the slow part), so after a parallel batch **always run `tp ls` to inventory which expected slugs actually exist** and re-dispatch only the missing ones sequentially. For batches of 2–4, sequential dispatch is more predictable and the serial overhead is small. For larger batches, dispatch in parallel but budget for retries and verify every slug individually.

**Keep `--prompt` terse.** The worker launches inside the worktree and inherits everything: `CLAUDE.md`, all project skills (`curate`, `initiate-new-disorder-creation`, `dismech-terms`, `dismech-references`, …), the `just` targets, and the validation stack. Do **not** restate SOPs, validation steps, or skill names in the prompt — the worker finds and invokes them on its own. A one-line directive (`"curate X"`, `"fix the bug in Y"`) is almost always enough. Over-instructing wastes tokens, crowds out the worker's own planning, and risks contradicting project guidance.

#### 2.3 Verify the worktree path (parallelism invariant)

```bash
tp status curate-prpf31 | grep ^Dir:
# expected: Dir:  /Users/cjm/worktrees/dismech-curate-prpf31
```

The worktree path **must**:
- live under `~/worktrees/`
- have exactly one `dismech-` prefix (not `dismech-dismech-...`)
- not be inside the repo (`.worktrees/`, `.claude/worktrees/`, `workdirs/`)

If any of those is wrong, **abort and redispatch** — do not try to patch it live:

```bash
tp clean curate-prpf31 --force        # removes session + worktree + branch
# fix the slug, then re-run step 2.2
```

Isolation of every agent under `~/worktrees/` is the whole basis of the parallel-agents model. Don't compromise it "just this once".

#### 2.4 Verify the prompt landed

```bash
tp peek curate-prpf31 -n 15
```

If the pane shows only the codex TUI header (model name, directory, `Tip: …`) with no task line after the `›` input prompt, `--prompt` was dropped. Redeliver manually:

```bash
tp send --wait curate-prpf31 "curate PRPF31-related retinitis pigmentosa"
```

`--wait` is required — the agent may not be at a sendable prompt yet.

#### 2.5 Mark bookkeeping

```bash
tp set curate-prpf31 status active
```

Now the session is dispatched, verified, and tracked. Move on to Monitor (step 3).

### 3. Monitor

Be proactive. Check sessions every few minutes during active dispatch. Don't wait to be asked.

```bash
tp ls --json                           # all sessions, machine-readable
tp ls --status active                  # only what's in flight
tp peek dismech-curate-prpf31 -n 40    # recent scrollback
tp status dismech-curate-prpf31        # detailed + agent state
```

**Two state dimensions — do not confuse them:**

| Dimension | Source | Vocabulary | Read with |
|---|---|---|---|
| **`tp` agent state** (transient, observed) | agent transcript + pane | `idle` `running` `completed` `interrupted` `error` `unknown` | `tp status <name>` |
| **boss `@status`** (curated, your bookkeeping) | you set it | `active` `idle` `waiting-human` `blocked` `done-ish` | `tp get <name> status` |

### 4. Steer

Send follow-ups only when sendable. Always `--wait`:
```bash
tp send --wait dismech-curate-prpf31 "Also add HPO phenotype HP:0000556."
tp send --wait --timeout 120 dismech-curate-prpf31 "continue"  # long-running
tp send --wait dismech-curate-prpf31 'if the curation PR branch is behind or conflicted, do NOT rebase locally; use gh api repos/monarch-initiative/dismech/pulls/PR_NUMBER/update-branch -X PUT -f expected_head_sha="$(git rev-parse HEAD)"; if it succeeds, git pull and re-run validation; if GitHub reports unresolvable conflicts, mark @status waiting-human and report the conflicting files'
```

#### Mandatory conflict rule for curation branches

When a curation PR branch is behind or conflicted, the conflict policy is strict:

- Never use local `git rebase`, `merge origin/main`, or any other local conflict-resolution flow on a curation branch.
- First use GitHub's server-side "Update branch" API:
  ```bash
  gh api repos/monarch-initiative/dismech/pulls/PR_NUMBER/update-branch \
    -X PUT -f expected_head_sha="$(git rev-parse HEAD)"
  ```
- If the API succeeds, `git pull` in the worker worktree and re-run validation.
- If GitHub reports unresolvable conflicts, set `@status waiting-human`, report the conflicting files, and do **not** attempt local resolution.

Use an explicit steer, not a vague "fix conflicts" message:

```bash
tp send --wait <name> 'the curation PR branch is behind or conflicted; do NOT rebase locally. Use gh api repos/monarch-initiative/dismech/pulls/PR_NUMBER/update-branch -X PUT -f expected_head_sha="$(git rev-parse HEAD)". If it succeeds, git pull and re-run validation. If GitHub reports unresolvable conflicts, mark @status waiting-human and report the conflicting files. Do not attempt local resolution.'
```

### 5. Stuck-agent protocol

Symptoms: `tp status` shows `error`, `interrupted`, or stuck on `running`/`unknown` for too long; `tp peek` shows a Codex trust prompt, repeated failure, or confusion. Note: brand-new repos and worktrees in Codex often pause at a trust prompt; sometimes Codex needs an extra Enter to advance.

Playbook:
1. **Nudge once** with `tp send --wait <name> "<clarifying instruction>"`. For trust prompts, often `"yes"` or another `Enter` is enough.
2. **If still stuck** after one nudge: `tp set <name> status waiting-human`, then report to the user with the session name, the symptom, and a proposed next step. **Do not** rescue the same session more than twice — escalate.

### 6. PR follow-through (this is the actual completion loop)

**A PR being opened is NOT completion.** In this repo the user does not typically review PRs by hand — an automatic `claude-review` job runs on every PR and acts as the reviewer. A task is only "done" when the PR has been **approved by claude-review AND all CI checks pass**. Until then the worker's job isn't finished.

After the worker reports "PR opened, validation passes" and goes idle, boss's standard SOP is to **prod the worker to watch its own PR through to approval**. Boss does not run `gh pr view` / `gh pr checks` itself — boss delegates that to the worker.

Standard prod sequence:

1. Worker reports PR opened, goes idle.
2. Boss sends:
   ```bash
   tp send --wait <name> 'check the PR — wait for the claude-review comment, address any feedback, fix any failing CI checks; if GitHub says the curation PR branch is behind or conflicted, do NOT rebase locally and instead use gh api repos/monarch-initiative/dismech/pulls/PR_NUMBER/update-branch -X PUT -f expected_head_sha="$(git rev-parse HEAD)", then git pull and re-run validation; if GitHub cannot resolve the conflicts, mark @status waiting-human and report the conflicting files'
   ```
3. Worker polls `gh pr view` / `gh pr checks`, reads the `claude-review` bot's comment, and addresses issues in new commits (re-pushes automatically; PR updates in place).
4. Boss peeks periodically. If the worker reports **approval + all checks green**, that is the real completion signal:
   ```bash
   tp set <name> status done-ish
   ```
5. If the worker says it can't address the review feedback, a check is failing in a way it doesn't understand, or it loops more than twice without convergence:
   ```bash
   tp set <name> status waiting-human
   ```
   then report to the user with the PR URL, the specific failing check or review comment, and what the worker tried.

**Never mark `done-ish` on PR-opened alone.** "I opened a PR" is a milestone, not a finish line. If you mark it done-ish and walk away, you've left an un-reviewed draft sitting in the queue.

### 6a. Conflicted PR branches

If the worker reports that a curation PR branch is behind or in conflict, do **not** tell it to `git rebase origin/main`, `merge origin/main`, or do any other local conflict resolution. Local rebase operates on the entire working tree and has already caused silent infrastructure reversions in this repo (#1430, #1575).

Use GitHub's server-side "Update branch" API instead:

```bash
gh api repos/monarch-initiative/dismech/pulls/PR_NUMBER/update-branch \
  -X PUT -f expected_head_sha="$(git rev-parse HEAD)"
```

This is the same as GitHub's "Update branch" button. It merges `main` into the PR branch server-side, so only the conflicting files are touched and the local worktree stays clean. This avoids the stale-branch reversion failure mode described in #1575 and the protected-path loss documented in #1430.

Boss's prod template for this case:

```bash
tp send --wait <name> 'the curation PR branch is behind or conflicted; do NOT rebase locally. Use gh api repos/monarch-initiative/dismech/pulls/PR_NUMBER/update-branch -X PUT -f expected_head_sha="$(git rev-parse HEAD)". If it succeeds, git pull and re-run validation. If GitHub reports unresolvable conflicts, mark @status waiting-human and report the conflicting files. Do not attempt local resolution.'
```

If the API succeeds, the worker should `git pull` in its worktree to pick up the merge commit, then re-run validation. If GitHub reports unresolvable conflicts, boss should set `@status waiting-human` and report the conflicting files. Do **not** try to "just fix it locally."

Tear down only after `done-ish`:
```bash
tp kill dismech-curate-prpf31              # one
tp ls --status done-ish                    # check the batch
tp clean --status done-ish --dry-run       # preview
tp clean --status done-ish --force         # remove sessions + worktrees
```

Before any `tp clean`, verify the target session is **not your own boss/orchestrator session**.

## Command cheatsheet

| Intent | Command |
|---|---|
| Dispatch Codex on a GH issue | `tp new <name> --profile codex --repo <path> --issue <N> --prompt "..."` |
| Dispatch Claude on an ad-hoc branch | `tp new <name> --profile claude --repo <path> --branch <br> --prompt "..."` |
| List everything (machine-readable) | `tp ls --json` |
| Recent output | `tp peek <name> -n 40` |
| Detailed state | `tp status <name>` |
| Send follow-up | `tp send --wait <name> "..."` |
| Long follow-up | `tp send --wait --timeout 120 <name> "..."` |
| Set boss status | `tp set <name> status <active\|waiting-human\|done-ish>` |
| Tear down one | `tp kill <name>` |
| Clean batch | `tp clean --status done-ish --force` |

Run `tp <command> --help` for full flag lists.

## Red flags — STOP

| Thought | Reality |
|---|---|
| "I'll just use `tmux send-keys` once" | **No.** Talk to Chris or file an issue at `cmungall/tmux-pilot`. |
| "Let me reuse this session for a second task" | One task = one session. Spin a new one. |
| "I'll have task A pipe its branch into task B" | Boss is for embarrassingly parallel work. Serialize dependent work yourself. |
| "I'll skip `--wait`, it's faster" | You'll race the prompt and lose input. Every send uses `--wait`. |
| "PR is open, I'll mark it done-ish" | **No.** PR-opened is a milestone, not completion. Prod the worker to watch its own PR through claude-review approval + green CI. Only then done-ish. |
| "I'll git rebase origin/main to fix conflicts" | NEVER local rebase on curation branches. Use `gh api update-branch` instead. Local rebase operates on the entire working tree and has caused silent infrastructure reversions (PR #1425 reverted 855 files). See #1430 and #1575. |
| "I'll run `gh pr view` / `gh pr checks` myself" | No — delegate. `tp send --wait <name> "check the PR, address review feedback, fix failing checks"`. Boss orchestrates, worker executes. |
| "The user said 'in parallel', activate boss" | Only if they named boss / tp / tmux / external agents. Otherwise use `dispatching-parallel-agents`. |
| "Worktree inside the repo is fine just this once" | No. Every agent needs an isolated worktree under `~/worktrees/`. Parallelism requires isolation — git only allows one worktree per branch, and agents step on each other if they share a checkout. |
| "Two agents can share a worktree if they work on different files" | No. Shared worktree = shared git index, shared dirty state, shared branch. One agent per worktree. |
| "Firing 5 `tp new` calls in parallel is faster" | Beware the parallel-cancellation gotcha — a timeout in one call can cancel sibling calls mid-flight, leaving a mix of created, partially-created, and missing sessions. After any parallel dispatch, run `tp ls` and re-dispatch the missing slugs sequentially. |
| "The parallel `tp new` batch returned, so all 3 sessions exist" | No — always run `tp ls` after a batch. One timeout can cancel the others; some of those sibling sessions may exist, some may not, and the ones that do exist may have dropped their `--prompt`. |
| "This session shows MERGED, I'll clean it" | Check that it is **not your own session first**. If you clean yourself, the user has to restart the entire orchestration context. |
| "I should remind the worker about CLAUDE.md rules / validation / the right skill to use" | No. The worker inherits CLAUDE.md and all project skills automatically. One-line prompts only. |

## Related skills

- **`superpowers:dispatching-parallel-agents`** — in-process subagents via the `Agent` tool. Use when work is read-only, stateless, or fits in one Claude context. **Boss is the external-process counterpart** for stateful, observable, multi-hour code work.
- **`superpowers:using-git-worktrees`** — worktree hygiene. Mostly redundant under boss because `tp` creates worktrees for you; useful for any manual recovery.
