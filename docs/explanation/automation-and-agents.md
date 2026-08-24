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
stalled PRs and merges ready ones), `auto-merge-compliance` (auto-merge for the
narrowly-scoped weekly compliance PR).

**Interactive agents** — `claude.yml` and `dragon-ai.yml` respond to `@`-mentions
on issues, PRs, and review comments. `claude-issue-triage` and
`claude-issue-summarize` process new issues.

**Derived artifacts** — `generate-pages`, `generate-grouping-pages`,
`generate-project-pages` render HTML; `warm-reference-cache` pre-resolves
publisher PDFs.

**Scheduled housekeeping** — `weekly-compliance` opens a periodic
compliance-fix PR (the one `auto-merge-compliance` is scoped to);
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

`reviewDecision == APPROVED` · not draft · **no assignees** ·
`mergeable == MERGEABLE` · `mergeStateStatus == CLEAN` · every status check
passing (stricter than `CLEAN`, which only covers *required* checks) ·
created more than **3 days** ago · targeting `main`.

This applies to **all authors, humans included**.

**Two of those criteria are the human control, and the rest are machine checks.**
Approval, mergeability, and green checks are all things a machine evaluates —
and since the approving reviewer is itself a model, they contain no human
judgement at all. What remains is:

- **more than 3 days old** — a standing window in which any human can look at
  any queued PR before it merges;
- **unassigned** — the per-PR veto. Assigning a PR marks it as somebody's active
  work, and the sweep never touches it.

So "a human is in the loop" here means *a human has a guaranteed opportunity to
intervene*, not *a human signed off*. Read the 3-day delay as the price paid for
that opportunity rather than as an arbitrary cooling-off period.

> **To stop a PR being auto-merged, assign it to someone.** Converting to draft
> or leaving a `CHANGES_REQUESTED` review also blocks it.

Preview what the next sweep would do, read-only: `just auto-merge-preview`.

---

## See also

- [Design Decisions §7](design-decisions.md) — curation governance policy
- [Cron Profiles](../cron-profiles.md) · [Agent Model Config](../agent-config.md) · [Page Build](../page-build.md)
- [Quality Control & Compliance](../quality-control.md) — the validation stack
- [CONTRIBUTING.md](https://github.com/monarch-initiative/dismech/blob/main/CONTRIBUTING.md) — why branches, not forks
