---
name: schedule
description: Donate this Claude Code instance to dismech curation on a recurring local window (e.g. "8pm-12am every day"). Runs as an Anthropic cloud routine on the user's own subscription; each fire reconciles against GitHub and either finishes the one item that still needs the user's work or, if nothing does, claims and curates one new disease. Also `/schedule` (run once now), `/schedule status`, `/schedule stop`. Active concurrency is 1.
---

# schedule

Donate this Claude Code instance to dismech curation for a timeframe the user
chooses. The skill **produces PRs and keeps them unblocked** during the window;
the production `pr-shepherd` automation carries the long tail (review re-request,
the deterministic auto-merge sweep) after the window closes.

**Active concurrency is 1 in this version.** The skill works one disease at a
time and claims a new one only when no PR of the user's still needs the user's
own work. Parked PRs (awaiting review, or approved+green waiting to auto-merge)
may accumulate harmlessly; they do not block the next disease. The 8-parallel
design that `/curate-next` supports is a deliberate later scale-up.

The skill **never merges, dismisses reviews, or self-approves.** Those are the
reviewer's and the `auto_merge_ready_prs.py` sweep's job.

> For a plain-language walkthrough aimed at a non-technical user (what to type,
> what happens each night, how to stop it), see
> [`docs/schedule-donation.md`](../../../docs/schedule-donation.md). This file is
> the technical orchestrator spec.

> This is a project skill that composes the Claude Code cloud-routine API
> (`RemoteTrigger`) — the same mechanism as the built-in `schedule` skill — but
> wired to the dismech curation loop specifically. When the user types
> `/schedule ...` inside this repo, this is the skill they mean.

## Commands

- **`/schedule`** — run once, now: reconcile against GitHub and either finish the
  one item that needs the user's work or (if nothing does) claim and curate one
  disease. No routine is registered.
- **`/schedule <window> [<recurrence>] [for <expiry>]`** — register a recurring
  cloud routine for the window (see **Schedule syntax**), after a one-off proving
  fire.
- **`/schedule status`** — show the active routine (cron / window / expiry) and
  the one in-flight item's state.
- **`/schedule stop`** — disable the recurring routine and print the hard-delete
  link.

## The one rule everything hangs on

Every invocation — manual `/schedule`, or a scheduled cloud fire — begins by
**reconciling against GitHub, which is the only state** (there is no local
ledger to go stale). The gate for claiming a **new** disease is:

> **No PR of the user's still needs the user's own work, and no un-PR'd claim
> issue exists.**

A PR **needs my work** (blocks a new claim) when it is `CHANGES_REQUESTED`,
**failing** a required check, or **conflicted**. A PR does **not** need my work —
it is *parked* — when it is awaiting review (green/pending checks) or approved +
green waiting only for the auto-merge sweep. An un-PR'd claim issue always needs
my work (a prior fire that crashed before pushing — resume it).

This classification is a **pure, unit-tested function**, not prose to
re-interpret each run. Do not hand-classify PRs; call the module.

## Step 1 — reconcile (every invocation)

Fetch the user's in-flight work and classify it with
`dismech.schedule.reconcile`:

```bash
gh pr list --author @me --state open \
  --json number,title,url,headRefName,isDraft,reviewDecision,mergeable,statusCheckRollup \
  > /tmp/schedule_prs.json

gh issue list --assignee @me --state open --label claim \
  --json number,title,closedByPullRequestsReferences \
  > /tmp/schedule_claims.json

uv run python - <<'PY'
import json
from dismech.schedule.reconcile import reconcile
prs = json.load(open("/tmp/schedule_prs.json"))
claims = json.load(open("/tmp/schedule_claims.json"))
r = reconcile(prs, claims)
print(r.summary)
print("SHOULD_CLAIM_NEW:", r.should_claim_new)
if r.item_needing_work:
    print("ITEM:", json.dumps(r.item_needing_work))
for c in r.pr_classifications:
    print(f"  PR #{c.number}: {c.category} (checks={c.checks}, review={c.review_decision}, mergeable={c.mergeable})")
PY
```

`reconcile()` returns `should_claim_new` and, when something needs work, the
single `item_needing_work` to finish this fire. **Trust its verdict.**

## Step 2 — finish-first (if anything needs my work)

If `should_claim_new` is false, handle **the one** `item_needing_work` and then
**stop — claim nothing new this fire**:

- **PR `CHANGES_REQUESTED` / failing / conflicted** → dispatch a fix subagent
  (`Task`) that **reuses `pr-shepherd`'s logic and scripts**, not a bespoke
  loop. It must obey the CLAUDE.md review rules:
  - Fix **everything in one push** — every blocking finding, worthwhile optional
    suggestions, the `history/` record for the round, and any conflict
    resolution. `main` has `dismiss_stale_reviews`, so every push costs a full
    re-review cycle; a chore commit afterward is a wasted cycle.
  - Re-request review via `scripts/retry_failed_reviews.py` (its scoped App
    token is the real workaround for the #9321 `workflow_dispatch` 403 — do not
    re-solve that here).
  - **Never dismiss a review, merge with `--admin`, or approve its own work.**
  - **Do not push while a review is in flight;** wait for the verdict, then push
    once. After pushing, **confirm checks are not still red** before treating the
    PR as parked (guards against racing our own push).
  - Work in a git **worktree**; root all file ops in the worktree (the
    `/curate-next` parent-checkout-leak incident). Commit/push after each
    meaningful step so a token/rate limit loses nothing.
- **Un-PR'd claim issue** → a prior fire claimed a disease but crashed before
  pushing a PR. **Resume** curating it to a pushed PR (use the
  `initiate-new-disorder-creation` workflow), in its own worktree.

Then report and stop.

## Step 3 — claim one (only if nothing needs my work)

If `should_claim_new` is true, invoke **`/claim-disease 1`** (its preflight
already searches open PRs per #7830) to file the `Curate <label>
(MONDO:NNNNNNN)` issue, then curate that **one** disease end-to-end to a pushed
PR carrying `Closes #<issue>`, in its own worktree. Use `/curate` /
`initiate-new-disorder-creation` for the curation itself.

## Step 4 — report

Report the one item's final state (curating / PR needs-fix-pushed /
awaiting-review / waiting-to-merge / merged) and whether a new disease was
claimed or the fire deferred because a PR needed work. Leave awaiting-review and
approved-waiting PRs to the review / `auto_merge_ready_prs.py` automation — report
their state only, never merge them.

## Registering a recurring window (`/schedule <window> ...`)

### Which scheduler

Claude Code exposes two schedulers; only one runs unattended:

- **`CronCreate`/`CronList`/`CronDelete`** — in-session cron. Session-only,
  in-memory, fires only while the REPL is idle, auto-expires after 7 days. It
  **cannot** run when Claude is closed → **not usable here.**
- **`RemoteTrigger` cloud routine (CCR)** — each fire spawns a fully isolated
  cloud session with its own git checkout, on the user's own subscription; the
  Mac need not be on. **This is what `/schedule <window>` uses.**

### Expand the config to a UTC cron (do not hand-compute)

Edit `.claude/schedule-config.yaml` (or write it from the user's phrasing), then
let the pure module derive the UTC cron, one-shot instant, prompt window-end,
expiry date, and DST-transition dates:

```bash
uv run python -m dismech.schedule --config .claude/schedule-config.yaml
```

Key facts the module encodes, so you don't re-derive them:

1. **Cloud cron is UTC.** `8pm America/Los_Angeles` = `0 3 * * *` PDT / `0 4 * *
   *` PST. The module converts local→UTC for the current DST period and lists
   the `dst_transitions` dates; re-register (or let a fire re-register) when the
   offset flips.
2. **The scheduler cannot enforce a window.** A window becomes **hourly restart
   fires across the window** (8/9/10/11pm), *not* four parallel workers — the
   single-flight guard means a fire is a no-op if the previous one is still
   running. `window_end_local` is passed into the prompt so the session stops
   claiming new work past it.
3. **Minimum interval is one hour** (validated by the config parser).

### `RemoteTrigger {action:"create"}` mapping

- `cron_expression` — each string in `utc_crons` (register one event per cron);
  or `run_once_at` (the module's RFC3339 UTC value) for `once` / `for 1 day`.
- `job_config.ccr.environment_id` — `routine.environment_id` from the config
  (the dismech cloud env).
- `job_config.ccr.session_context.sources` —
  `https://github.com/monarch-initiative/dismech`.
- `job_config.ccr.session_context.model` — the config `model`.
- `job_config.ccr.session_context.allowed_tools` — `Bash, Read, Write, Edit,
  Glob, Grep, Task, WebFetch, WebSearch, Skill, TodoWrite`, plus `RemoteTrigger`
  **if Step 0 confirms it is callable in-session** (needed for single-flight and
  expiry self-disable).
- `events[].data.message.content` — the **frozen prompt** below, with
  `<WINDOW_END_LOCAL>` and `<EXPIRY_DATE>` substituted from the expansion.

Record the returned trigger id back into `routine.trigger_id` in the config.

### Step 0 — the prerequisite spike (run once, before trusting the cadence)

Two facts the cloud design assumes are **unconfirmed** and must be answered with
one diagnostic fire (`RemoteTrigger {action:"run"}` on a throwaway one-off
routine, then `get_run_log`) **before** enabling any recurring routine. Record
the answers on issue #11657:

1. **Does a cloud-routine session load this repo's `.claude/skills`?** i.e. can
   the frozen prompt say "use the `claim-disease` skill" and have it resolve, or
   must the skill logic be inlined into the prompt?
2. **Is `RemoteTrigger` callable from inside a routine session?** The expiry
   self-disable and the single-flight `list_runs` check both assume it is; if
   not, use the GitHub fallbacks noted in the prompt.
3. While there, confirm the env carries `uv`, `just`, `gh` auth, ontology DBs,
   and network to OLS / PubMed / ClinicalTrials, and that **one** full curation
   fits a single session's token/time budget. If not, the save-early /
   reconcile-first resume path must carry a partial disease across fires — verify
   that works before relying on the nightly cadence.

First delivery therefore includes one `RemoteTrigger {action:"run"}` proving
fire that claims + curates a single disease, reviewed via `get_run_log`, before
the recurring routine is enabled.

### The frozen routine prompt

Substitute `<WINDOW_END_LOCAL>` and `<EXPIRY_DATE>` from the expansion. If Step 0
finds project skills do **not** load in-session, expand the `claim-disease` /
`initiate-new-disorder-creation` references into inline instructions.

```
You are a scheduled dismech curation donation run. Repo: monarch-initiative/dismech.
Work strictly ONE disease at a time. Do not merge, dismiss reviews, or self-approve.
Commit and push after every meaningful step so a token/rate limit loses nothing.

1. SINGLE-FLIGHT: If RemoteTrigger is available, call list_runs on this routine; if another
   run is still active, STOP now (do nothing). If RemoteTrigger is unavailable, rely on the
   reconcile gate below plus the claim label as the lock.
2. RECONCILE from GitHub (the only state) using dismech.schedule.reconcile:
   - my open PRs (gh pr list --author @me ...), classified as needs-my-work / awaiting-review /
     waiting-to-merge;
   - my open `claim` issues with no linked PR.
3. FINISH-FIRST: If any PR needs my work, or an un-PR'd claim issue exists, handle that ONE item:
   - PR CHANGES_REQUESTED/failing/conflicted -> fix everything in ONE push (blocking findings,
     worthwhile optional suggestions, the history/ record, conflicts), following CLAUDE.md's
     review rules; re-request review via scripts/retry_failed_reviews.py. Do NOT push while a
     review is in flight. After pushing, confirm checks are not red before considering it parked.
   - Un-PR'd claim issue -> resume curating it to a pushed PR (initiate-new-disorder-creation
     workflow; work in a git worktree; root all file ops in the worktree).
   Then STOP. Claim nothing new this fire.
4. CLAIM ONE only if NOTHING needs my work and no un-PR'd claim issue exists: claim exactly one
   disease (claim-disease logic: two-phase pick, file the `Curate <label> (MONDO:NNNNNNN)` issue),
   then curate it end-to-end to a pushed PR carrying `Closes #<issue>`, in its own worktree.
5. WINDOW END: stop claiming new work after <WINDOW_END_LOCAL>; let in-flight subagent work commit.
6. EXPIRY: if today is past <EXPIRY_DATE>, disable this routine (RemoteTrigger update enabled:false
   if available; otherwise do nothing each fire — a disabled cron is the operator's job).
7. Report what you did: the one item's final state, and whether a disease was claimed or deferred.
```

## Concurrency control across hourly fires

Cloud fires are isolated sessions with no shared memory; they coordinate only
through shared external state — GitHub plus the routine's own `list_runs`. At
concurrency 1, two guards suffice and are already encoded above:

1. **Single-flight per routine** (Step 1 of the frozen prompt): a fire is a
   no-op if a prior run is still active. The hourly cron is a *restart
   heartbeat*, not four workers.
2. **The needs-my-work gate** (`reconcile`): a durable GitHub fact that survives
   restarts, so at most one disease is ever actively in hand and a crashed
   predecessor's item is *resumed*, not duplicated.

## `/schedule status`

Read `routine.trigger_id` from the config; if set, `RemoteTrigger
{action:"list_runs"}` (and/or `get_run_log` on the latest) to show cron / window
/ expiry and the latest fire's state. Then run **Step 1 (reconcile)** and print
the one in-flight item's classification. If no `trigger_id` is set, say no
recurring routine is registered and show only the reconcile result.

## `/schedule stop`

Routines **cannot be hard-deleted via the API** — only disabled. So:

1. `RemoteTrigger {action:"update", body:{enabled:false}}` on
   `routine.trigger_id`.
2. Clear `routine.trigger_id` in the config (leave `environment_id`).
3. Print the hard-delete link: `https://claude.ai/code/routines` (web UI only).

Stopping never merges, dismisses, or abandons in-flight work: in-flight
subagents are allowed to commit/push; `pr-shepherd` carries the tail.

## Schedule syntax

`/schedule <window> [<recurrence>] [for <expiry>]`. The user says **when** it
starts, **how long** each window runs, and **how long the routine lives**. Map
the phrasing onto `.claude/schedule-config.yaml`:

- **window** → `window.start_local` / `window.end_local` (whole hours).
  `8pm-12am` → `20:00` / `00:00`.
- **recurrence** → `every day` = `every-day`, `every workday`/`weekdays` =
  `workday`, `weekends` = `weekends`, `once`/`tonight` = `once`, an explicit
  local cron = `custom` + `custom_cron_local`.
- **expiry** → `for N days` = `expiry.mode: days` / `value: N`; `for N weeks` =
  `weeks`/N; `until YYYY-MM-DD` = `date`; `once` / `for 1 day` = `once`; no
  phrase = `none` (never expires).

Always confirm the derived UTC cron and DST-transition dates back to the user
before registering — the local→UTC conversion is the easiest thing to get wrong.

## Rate-limit behaviour

On hitting a limit, start **no** new claims; let in-flight subagents commit/push
and exit cleanly. Because reconcile is the first step of every run, the next fire
resumes the in-flight PRs automatically — "finish what you started before
starting new ones", realized through GitHub-as-ledger rather than a resume file.

## What is pure code vs. orchestration

- **Pure, unit-tested (call it, don't reimplement):**
  `dismech.schedule.config` (window/recurrence/expiry → UTC cron, one-shot
  instant, prompt substitutions, DST dates) and `dismech.schedule.reconcile`
  (PR classifier + finish-first decision). Tests:
  `tests/test_schedule_config.py`, `tests/test_schedule_reconcile.py`.
- **Reused, not forked:** `/claim-disease`, `/curate` /
  `initiate-new-disorder-creation`, `/create-pr`, and `pr-shepherd`
  (`scripts/retry_failed_reviews.py`, `scripts/auto_merge_ready_prs.py`, the
  shepherd job).
- **This skill:** the thin orchestrator that ties them together and the
  cloud-routine registration.
