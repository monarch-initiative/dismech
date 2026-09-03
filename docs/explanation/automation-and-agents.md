# Automation & Agents: how CI is put together

DisMech runs **27 GitHub Actions workflows**. Most repositories this size have
CI that builds and tests; this one also has automation that *curates* — scanning
literature, opening pull requests, reviewing them, and merging them. That is
unusual enough to deserve an explanation of the shape rather than a per-workflow
manual.

This page is the map. It explains **why the automation is arranged the way it
is**. Counts and sampled statistics below were measured **2026-08-05** and will
drift — they are given to make the reasoning concrete, and none of the arguments
depend on the exact numbers holding. For the individual knobs, see [Cron Profiles](../cron-profiles.md)
(cadence), [Agent Model Config](../agent-config.md) (which model), and
[Page Build](../page-build.md) (full vs incremental rendering).

If you are here because a bot did something to your PR and you want to know why,
skip to [Review states and merge state](#review-states-and-merge-state).

---

## The stance: agent-forward, with a human *window* rather than a sign-off

[Design decision §7](design-decisions.md) states it: DisMech is **agent-forward**.
Most curation is performed by AI agents, initiated either by humans or by
scheduled workflows. Assume issue and PR content is AI-generated unless marked
otherwise.

The consequence people underestimate: at this volume, **a human cannot be the
throughput bottleneck on every change**. Roughly 200 PRs are open at any time.
So the human role is not "approve each diff" — it is "set the policy the
automation enforces, and intervene where it flags uncertainty."

**Be precise about what "reviewed" means here.** The automated reviewer is
itself a model: `claude-code-review.yml` mints an `ai4c-reviewer` GitHub App
token and has it run `gh pr review --approve`. So `reviewDecision == APPROVED`
— the load-bearing condition in the auto-merge criteria — is normally produced
by an LLM, not a person. For an agent-authored curation PR, that closes an
**author → approve → merge** loop with no human in it.

That is deliberate at this repo's curation volume, but it means the human
control is *not* a sign-off gate. It is the **3-day delay and the assignee
check** — see [the auto-merge criteria](#the-auto-merge-criteria-in-this-vocabulary).
Those two otherwise arbitrary-looking conditions exist precisely to be the
window in which a human can notice and intervene; everything else in the
predicate is a correctness check that a machine can evaluate.

That only works if the automation is trustworthy in a specific way, which is the
next section.

## The organising principle: deterministic gates around model judgement

The single most important pattern in this repo's CI:

> **Models judge. Deterministic code decides.**

An LLM is excellent at reading a paper, spotting a bundled mechanistic claim, or
noticing that a snippet doesn't support its citation. It is not a thing you want
holding merge rights on the strength of its own say-so. So wherever an action is
consequential and reversible only with effort, there is a *deterministic*
component that gates it — plain code applying a fixed predicate to observable
state, producing the same answer every run.

Worked examples, each a place where the two halves sit side by side:

| Workflow | The model's job (judgement) | The deterministic gate (decision) |
|---|---|---|
| `pr-shepherd` | Agent step reads stuck PRs, resolves review comments, pushes fixes | Closing sweep merges only PRs passing a fixed predicate ([`scripts/auto_merge_ready_prs.py`](https://github.com/monarch-initiative/dismech/blob/main/scripts/auto_merge_ready_prs.py)) |
| `claude-code-review` | Agent reviews the diff, writes findings, **and submits the approving review** | *(none on this path — see below)* |
| Curation generally | Agent writes the YAML and picks the evidence | The [validation stack](../quality-control.md) — schema, term, and reference validators — decides whether it's admissible |
| `generate-pages` | — | [`classify_page_build.py`](https://github.com/monarch-initiative/dismech/blob/main/scripts/classify_page_build.py) decides full vs incremental, defaulting to full on anything unrecognised |
| `close-fork-prs` | — | Closes every fork PR. "No model is involved" (its own header comment) |

**The review row is the honest exception**, and worth stating plainly in a page
arguing this principle. Branch protection does gate the merge, but the approval
it requires is produced by the reviewing model itself, so on that path the
"deterministic decides" half is satisfied by model judgement. The real
deterministic gates on a curation PR are the **validation stack** and the
**merge sweep's fixed predicate** — not the review requirement. Wherever this
page says a change is gated, that is what is doing the work.

The validation stack is the load-bearing instance. Agents hallucinate PMIDs,
snippets, and ontology IDs; the answer is not "prompt the agent harder" but
`linkml-reference-validator` checking each snippet is a literal substring of a
cached abstract, and `linkml-term-validator` checking each CURIE against OAK.
The agent proposes; the validator disposes. Everything in
[CLAUDE.md](https://github.com/monarch-initiative/dismech/blob/main/CLAUDE.md)
about never hand-writing `references_cache/` or `cache/**/*.csv` follows from
this: **a cache that can be written by the thing it is meant to check is not a
check at all.** It makes validation circular.

Two corollaries worth internalising:

- **Fail closed.** Unrecognised input escalates to the expensive-but-safe path.
  The page-build classifier treats any path it doesn't recognise as "full
  rebuild". The merge sweep skips anything it cannot positively verify.
- **Deterministic parts get unit tests; judgement parts get guardrails.** You
  can pin a predicate with a test. You cannot unit-test a model's opinion, so
  those get bounded scope, explicit allow-lists, and a human escalation path.

## What the workflows do, by role

Grouped by what they're *for*, which is more useful than alphabetically.

**Ordinary CI** — `main.yaml` (build, test, lint, schema/term/reference
validation; the `test (3.13)` job is the only *required* status check on `main`),
`test-linkml-rc3.yml` (forward-compatibility against a linkml release
candidate), `deploy-docs.yaml`.

**Curation discovery** — scheduled scanners that find work and open issues or
PRs: `curation-scanner`, `literature-scan`, `preprint-scan`,
`knowledge-gap-scan`, `discussion-scanner`. These are the top of the funnel.

**PR lifecycle** — `claude-code-review` (automated review on every PR),
`post-review-agent` (acts on editorial review comments), `pr-shepherd` (unsticks
stalled bot-authored PRs and deterministically merges ready PRs, including weekly
compliance PRs, through one common closing controller).

**Interactive agents** — `claude.yml` and `dragon-ai.yml` respond to `@`-mentions
on issues, PRs, and review comments (`dragon-ai.yml` is summoned as `@ai4c-agent`;
the file keeps its old name). `claude-issue-triage` and
`claude-issue-summarize` process new issues.

**Derived artifacts** — `generate-pages`, `generate-grouping-pages`,
`generate-project-pages` render HTML; `warm-reference-cache` pre-resolves
publisher PDFs.

**Scheduled housekeeping** — `weekly-compliance` opens a periodic
compliance-fix PR, which enters the ordinary review and PR-shepherd closing path;
`sync-epic-checkboxes` reconciles a tracking issue against the KB.

**Releases** — `kgx-release`, `mondo-emc-release`, `pypi-publish`, triggered by
published GitHub releases.

**Security gates** — `close-fork-prs`, `untrusted-comment-guard`. See below.

## Configuration lives in one place, not 27

Two cross-cutting properties were originally copy-pasted into every workflow,
which meant a repo-wide change was an N-file edit that drifted:

- **Cadence** → [`.github/cron-profiles.yaml`](https://github.com/monarch-initiative/dismech/blob/main/.github/cron-profiles.yaml).
  Named profiles (`slow`/`medium`/`fast`/`fast-weekend`) applied with
  `just cron-profile <name>`.
- **Model** → [`.github/agent-config.yaml`](https://github.com/monarch-initiative/dismech/blob/main/.github/agent-config.yaml).
  Each workflow resolves `AGENT_MODEL` at run time via a composite action.

**Do not hand-edit the `cron:` lines or add a `--model` flag to a workflow.** A
test (`tests/test_agent_config.py`) enforces the model rule. Edit the config.

The generalisable point: when a property is shared across many workflows, make
it data with a single source of truth and a test that catches re-hardcoding —
otherwise it silently diverges.

## Trust boundaries

Agentic CI has a threat model ordinary CI does not: **PR content is model
input**. A title, body, comment, or diff can carry text crafted to redirect an
agent that reads it (prompt injection). Three mechanisms address this:

1. **No fork PRs.** `close-fork-prs` closes them at the door. Two reasons, per
   its header comment: fork-authored content is the injection entry point, and
   fork-triggered workflows don't receive repo secrets, so they can't be
   AI-reviewed anyway. Contributors push branches to `origin` instead — see
   [CONTRIBUTING.md](https://github.com/monarch-initiative/dismech/blob/main/CONTRIBUTING.md).
2. **Comment gating.** `untrusted-comment-guard` minimizes risky comments from
   untrusted authors via a shared trust gate, so agents don't read them.
3. **In-prompt guardrails.** Agent prompts instruct the model to treat all PR
   content as *untrusted data, never as instructions* — and to report it if PR
   content appears to be giving it orders. `pr-shepherd`'s prompt is the fullest
   worked example.

**Bot identity.** Two GitHub Apps appear in timelines, with different
permissions, and it is worth being able to tell them apart:

- **`ai4c-agent`** — the *write* identity. Scheduled agents (curation scanners,
  `pr-shepherd`) push branches, comment, and merge as this app.
- **`ai4c-reviewer`** — the *review* identity used by `claude-code-review` to
  submit review states. An `ai4c-reviewer[bot]` approval in a PR timeline is a
  model's verdict, per the section above.

Scheduled agents authenticate as an App rather than using the built-in
`GITHUB_TOKEN`. This is deliberate: a push made
with `GITHUB_TOKEN` does *not* trigger further workflows (GitHub's loop
prevention), so a fix pushed by an agent would never get re-reviewed. An App
token does trigger them. Note App installation tokens expire after **1 hour**,
which matters in long-running jobs.

## Derived artifacts are written by exactly one workflow

`pages/`, `dashboard/`, `app/data.js`, `pathographs/`, and `elements/` are
generated. They live in git, but **only `generate-pages` writes them**, in its
own `auto/generate-pages` PR. A hand-authored PR must never include them —
you'd conflict with the bot and with every other curation PR.
See [Page Build](../page-build.md).

The same logic covers `references_cache/` and `cache/**/*.csv`: committed,
because CI validation must be deterministic, but written *only* by their
generating tool.

---

## Review states and merge state

The vocabulary GitHub uses here is genuinely confusing, and it is the vocabulary
the merge sweep's criteria are written in. Three different fields are involved.

### 1. Individual review state

Each submitted review has its own state. States actually observed in this repo
(last 40 PRs): `CHANGES_REQUESTED` ×46, `APPROVED` ×33, `DISMISSED` ×15.
GitHub also defines `COMMENTED` (feedback without a verdict) and `PENDING` (a
started, unsubmitted review).

### 2. `reviewDecision` — the aggregate

The PR's *overall* verdict, computed from the individual reviews plus branch
protection: `APPROVED`, `CHANGES_REQUESTED`, `REVIEW_REQUIRED`, or null.

This is the one automation keys on. The distinction that trips people up: an
individual review being `APPROVED` does **not** mean `reviewDecision` is
`APPROVED` — a later `CHANGES_REQUESTED` from anyone overrides it.

### 3. What `DISMISSED` actually means

**A dismissed review is one that has been explicitly set aside so it no longer
counts toward `reviewDecision`.** It is not deleted and not withdrawn by its
author — it stays in the timeline with its state changed to `DISMISSED`, so the
history remains auditable.

Two ways it happens:

- **Automatically, on a new push.** `main` here is protected with
  **`dismiss_stale_reviews: true`**, so pushing any commit to a PR dismisses the
  existing approvals. The reasoning: an approval is a statement about *specific
  code*, so new code invalidates it.
- **Manually**, by someone with write access, via "Dismiss review".

This is why you see `DISMISSED` so often in this repo (15 of the last ~94
reviews): agents push fix commits onto reviewed PRs constantly, and each push
dismisses the standing approval, which then triggers a fresh review.

A worked example — PR #8018, from its own reviews API:

| Time (UTC) | Event |
|---|---|
| 13:47:19 | review submitted (approving) |
| 13:49:18 | commit `9fd68a7` pushed |
| 13:54:34 | **fresh** approving review of the new commit |

The 13:47:19 review now reads `DISMISSED`. The push invalidated it; the
automated reviewer then re-reviewed the new head commit and approved that.

**Why this matters for auto-merge:** it is the guarantee that the merge sweep
cannot merge a commit nobody reviewed. Approve commit A → push commit B → the
approval is dismissed → `reviewDecision` reverts from `APPROVED` → the sweep
skips it. The guarantee lives in a *repository setting*, not in the repo, which
is tracked as [issue #8020](https://github.com/monarch-initiative/dismech/issues/8020).

### 4. `mergeable` and `mergeStateStatus`

Separate from review, and separate from each other:

- **`mergeable`** — can git merge it? `MERGEABLE`, `CONFLICTING`, or `UNKNOWN`.
- **`mergeStateStatus`** — may it be merged *now*, per all rules? The useful
  values: `CLEAN` (nothing blocking), `BLOCKED` (a required review or check is
  missing), `BEHIND` (base has moved and the branch must update), `DIRTY`
  (conflicts), `UNSTABLE` (a non-required check failed), `DRAFT`, `UNKNOWN`.

`BLOCKED` is the one people misread: it usually means "approved, but a required
check hasn't finished", not that anything is wrong.

**`UNKNOWN` is normal, not an error.** GitHub computes mergeability *lazily, per
PR* — asking for it is what starts the computation. Sampling 60 open PRs in this
repo returned `UNKNOWN` for **58** of them on first ask. Any tool reading these
fields in bulk must expect `UNKNOWN` and re-ask per PR; treating it as "not
mergeable" means never merging anything. Both this and a GraphQL cost issue are
why the merge sweep is split into a cheap list pass and a per-PR verification
pass.

### The auto-merge criteria, in this vocabulary

`pr-shepherd`'s closing sweep merges a PR only when **all** hold:

`reviewDecision == APPROVED` · **no human assignees** ·
`mergeable == MERGEABLE` · `mergeStateStatus == CLEAN` · every status check
passing (stricter than `CLEAN`, which only covers *required* checks) ·
created more than **3 days** ago · targeting `main`. Author identity, head-branch
prefix, draft status, and exact ancestry with current `main` are not eligibility
criteria. A known bot/agent assignee is routing metadata rather than a human hold.

Draft state is metadata, not a hold. An otherwise eligible draft is marked
ready immediately before a complete re-read of the merge guards. If the attempt
does not merge, its original draft state is restored.

The agent-tending shortlist is authorized by verified author identity, not by a
head-branch naming convention. In particular, a human-authored `claude/` branch
does not become agent-tendable, while an allowlisted bot-authored PR may use any
head name outside the separately managed `auto/` lanes. This deliberately
replaces the older `claude/` prefix heuristic with the boundary the guardrail
actually means: never modify a human-authored PR.

The closing controller runs on a fresh runner, separate from the LLM job, and
uses a read-only token for discovery plus a dedicated write token only for its
fixed transitions. The controller runs hourly; under the active `slow` cron
profile, the costlier agent tending job runs every four hours on a separate
concurrency lane (hourly in the faster profiles) and receives a ranked shortlist
capped at three times its action budget. The controller acts on at most one PR
per run. Before that request it performs the final PR-state read and pins the
operation to the verified head SHA. On a queue-required branch GitHub tests the
latest-main combination as a temporary merge group; without a queue the repo's
loose required-check policy permits the already-green PR to merge directly.

This runner split protects the deterministic job from process-level changes
made during the LLM run. It is not a complete GitHub capability boundary: the
agent's own App token needs contents-write access to repair branches, which also
permits merge operations. Its no-merge rule remains prompt-enforced until a
separate identity, broker, or repository ruleset can enforce that distinction.

The final head pin prevents merging a commit that changed after verification.
The controller does not chase current `main`; doing so would dismiss approvals
and restart CI without being required by branch protection or queue admission.

The `merge_group` CI half of that project is in place (#10168): `main.yaml`
declares the trigger, and merge-group runs execute the **full suite** — every
path-filter gate that scopes an ordinary PR run is forced on for queue builds,
except the two changed-file KB validations discussed below, because path
filtering is the specific reason the #9538 cross-file enum incompatibility
stayed invisible until the branch was updated, and that class of break is
exactly what a queue build exists to catch. The dorny/paths-filter step itself
still runs on merge-group refs (supported since its v4.0.1, with `base`/`ref`
defaulting to the event's commit hashes): its changed-file lists drive the
changed-disorder and changed-comorbidity validations — the two steps that stay
filter-gated rather than forced, since forcing them would run them with empty
file lists — so those validate the KB files actually entering `main`, in the
merged context where a co-queued PR may have changed `cache/**` or
`references_cache/**`. `tests/test_merge_group_ci.py` pins the trigger, the
filter's event coverage and its v4.0.1 version floor, the no-suppression rule,
and the never-forced rule for the two file-scoped steps. Enabling an actual
queue on `main` (branch ruleset, shepherd enqueue behavior) is the remaining,
separately gated half.

**Merge-integrity verification.** Passing tests are not evidence of correct
history: in the April 2026 GitHub merge-queue incident (#2034), squash merges
of multi-PR merge groups silently reverted other PRs' changes and CI stayed
green — GitHub learned of the bug from customer reports, because it corrupted
content, not availability. The `verify-merge-integrity` workflow is the local
monitoring that closes that gap: on every push to `main` it recomputes, for
each squash commit, the tree that merging the PR's head into the previous tip
should have produced (`git merge-tree --write-tree`), compares it to the tree
actually pushed, and on mismatch fails red and opens (or comments on) a
`merge-integrity`-labelled issue. Merge commits, rebase merges, and direct
pushes are reported as skipped, not judged — see
`scripts/verify_merge_integrity.py` for the exact contract, including the two
known false-positive sources (a PR branch reused after merge, and rename-
detection divergence between local merge-ort and GitHub's merge machinery):
a `MISMATCH` alarm warrants comparing the trees by hand before declaring an
incident, especially in the workflow's first weeks. This must be live
**before** a merge queue with build concurrency above 1 is enabled on `main`,
because speculative merge groups contain multiple PRs — the structural shape
of the incident — and it is cheap insurance against non-queue merge anomalies
in the meantime.

**Merge-queue break-glass.** A required merge queue removes the ordinary
escape hatch — the merge button becomes "add to queue", and a red or wedged
required check on `main` (the #5074 shape) blocks every entry. The queue is
managed as a repository ruleset, and pausing it is one admin API call each
way:

```bash
# find the ruleset carrying the merge_queue rule (don't rely on its name)
gh api repos/monarch-initiative/dismech/rulesets --jq '.[] | "\(.id) \(.name)"'
gh api repos/monarch-initiative/dismech/rulesets/<id> \
  --jq '[.rules[].type]'   # confirm it includes "merge_queue"
# pause (PRs merge normally again; queue state is abandoned)
gh api -X PUT repos/monarch-initiative/dismech/rulesets/<id> -f enforcement=disabled
# resume
gh api -X PUT repos/monarch-initiative/dismech/rulesets/<id> -f enforcement=active
```

Pause when `main`'s required check is red for a reason no queued PR can fix,
when the queue itself is misbehaving, or when `verify-merge-integrity` has
flagged a mismatch and history needs auditing before more merges land. While
paused, branch protection's other rules (required check, review) still apply;
what is lost is only current-`main` integration testing, so treat a pause as
an incident state to exit, not a convenience. Note that the queue rule also
blocks direct pushes to `main` while active — a deliberate side effect that
also covers resetting a branch the rule targets.

GitHub auto-merge is a separate server-side path and does not execute these
controller guards. Ordinary agents must not arm it, and weekly-compliance PRs use
the common controller rather than a separate merge path. The separately managed
`auto/` workflows own their own merge path. A maintainer can still enable it
manually as an explicit override.

Those `auto/` workflows mint a short-lived `ai4c-agent` token after their long
build phase, leave checkout credentials unpersisted, and use the App specifically
for the three writes that advance the lane: branch push, PR creation, and
`gh pr merge --auto`. The late mint avoids the App token's one-hour lifetime
expiring during a full page build. The identity is load-bearing twice.
App-authenticated branch pushes and PR creation start the required
`pull_request` checks; the built-in token instead leaves these bot runs at
`action_required`. App-attributed merges then trigger the `push` workflows on
the new `main` SHA, providing the normal post-merge `test (3.13)` result. Each
lane also removes an
existing auto-merge request before re-enabling it, because merely issuing
`--auto` again can preserve the previous request's `enabledBy` actor. A workflow
test enumerates the six lanes and protects all three App-authenticated writes.

This applies to **all authors, humans included**.

**Two of those criteria are the human control, and the rest are machine checks.**
Approval, mergeability, and green checks are all things a machine evaluates —
and since the approving reviewer is itself a model, they contain no human
judgement at all. What remains is:

- **more than 3 days old** — a standing window in which any human can look at
  any queued PR before it merges;
- **not human-assigned** — the per-PR veto. Assigning a PR to a human marks it as
  somebody's active work, and the sweep never touches it. Bot/agent assignment
  remains eligible.

So "a human is in the loop" here means *a human has a guaranteed opportunity to
intervene*, not *a human signed off*. Read the 3-day delay as the price paid for
that opportunity rather than as an arbitrary cooling-off period.

> **To stop a PR being auto-merged, assign it to a human or leave a
> `CHANGES_REQUESTED` review.** Draft status does not block it.

Preview what the next sweep would do, read-only: `just auto-merge-preview`.

---

## What assigning an issue actually does

Two different systems attach meaning to assignment, and they mean **opposite**
things. Knowing which one you are invoking is the whole game.

### GitHub's agent assignment (a platform feature)

GitHub itself offers **"Assign agent to issue"** — currently a **Preview**
feature, reached from the issue's assignee control. It opens a dialog with an
optional prompt, a target repository, and an agent selector; assigning dispatches
a coding agent (`copilot-swe-agent`, assignable wherever the organisation has the
Copilot coding agent enabled) to work the issue and open a pull request.

**There, assignment *is* the dispatch.** It is a GitHub product feature, so none
of the Actions machinery on this page applies to it — no `if:` gate, no
`cron-profiles.yaml` cadence, no `AGENT_MODEL` resolution, and none of the
[trust boundaries](#trust-boundaries) above.

**It is not, however, unaware of this repo.** `.github/copilot-instructions.md` is
a **symlink to `../CLAUDE.md`** (and `AGENTS.md` points there too), so a dispatched
coding agent receives the same curation rulebook every other agent here works
from — the evidence SOP, the never-hand-write-the-caches rule, the whole thing.
Because it is a symlink rather than a copy, it cannot drift out of date.

What it does *not* inherit is the Claude Code-specific tooling: the skills in
`.claude/skills/` and the deep-research providers, which need local API keys. So
it is well-suited to bounded, well-specified work and poorly suited to new
disease curation. Its output is still gated the same way as anything else — the
[validation stack](../quality-control.md) and `claude-code-review` do not care
which agent wrote the YAML, which is the point of *models judge, deterministic
code decides*.

### DisMech's own agents (this repo's workflows)

The workflow fleet described on this page is **mention-driven**. None of it
listens for assignment:

| Agent | Trigger | Who may fire it |
|---|---|---|
| `claude.yml` | `@claude` in the issue body/title, or in an issue/PR/review comment | Author of the issue or comment must be `OWNER`/`MEMBER`/`COLLABORATOR` |
| `dragon-ai.yml` | `@ai4c-agent please …` as ordinary prose, or the legacy `@dragon-ai-agent please …` — ignored inside code spans and fenced blocks, so documenting the keyword doesn't fire it. Both are text keywords, not accounts: the agent runs as the ai4c-agent GitHub App, which cannot be @-mentioned. The handles live in [`.github/scripts/agent-mention.js`](https://github.com/monarch-initiative/dismech/blob/main/.github/scripts/agent-mention.js), shared with the comment trust gate | Must be listed in [`.github/ai-controllers.json`](https://github.com/monarch-initiative/dismech/blob/main/.github/ai-controllers.json) |

`dragon-ai.yml` once supported assignment dispatch and **dropped it** — its header
records the retirement of the machine account and of the programmatic assigner
(`stale-pr-reassign`) that drove it. The `dragon-ai-agent` account still exists
and still appears in the assignee picker, but assigning to it does nothing: the
workflow does not list `assigned` among its trigger types. `pr-shepherd`'s prompt
carries the matching rule for agents — never assign `dragon-ai-agent` just to
trigger work.

`claude.yml` *does* list `issues: [assigned]` among its trigger types, which looks
like an exception but isn't: its `if:` still requires `@claude` in the body or
title. Assigning an issue that already mentions `@claude` re-fires it; assigning
one that doesn't mention it does nothing. That path also gates on the **issue
author's** association rather than the assigner's, so assigning an
externally-authored issue cannot turn untrusted issue text into an agent trigger
— the same trust boundary as [above](#trust-boundaries).

### To this repo's automation, an assignee means "claimed"

`curation-scanner` selects with `is:open is:issue no:assignee` and is explicitly
"restricted to items with no human / non-agent assignee, so the scanner never
steps on work a person has already claimed." Assignment on an *issue* is therefore
the same claim signal as assignment on a *PR*, where it vetoes the auto-merge
sweep.

> **To DisMech's own workflows an assignee means "somebody has this" — never "an
> agent should pick this up."** To get *their* attention, mention the agent.

**The two systems collide, quietly.** Assigning an issue to GitHub's coding agent
gives that issue an assignee, so it simultaneously **removes the issue from
`curation-scanner`'s queue**. That is usually the outcome you want — two agents
should not work the same issue — but nothing announces it, and it is the reason
the distinction on this page matters in practice rather than only in theory.

Finally, two automations need no prompting at all: `claude-issue-triage` and
`claude-issue-summarize` both fire on `issues: [opened]`. If a bot commented on
your issue moments after you filed it and you did nothing, that was one of these.

---

## See also

- [Design Decisions §7](design-decisions.md) — curation governance policy
- [Cron Profiles](../cron-profiles.md) · [Agent Model Config](../agent-config.md) · [Page Build](../page-build.md)
- [Quality Control & Compliance](../quality-control.md) — the validation stack
- [CONTRIBUTING.md](https://github.com/monarch-initiative/dismech/blob/main/CONTRIBUTING.md) — why branches, not forks
