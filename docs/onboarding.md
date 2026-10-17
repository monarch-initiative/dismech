# Onboarding

DisMech is a knowledge base of disease mechanisms — what goes wrong, in what
order, with a citation for every step. Entries are written by AI agents that a
person points at a disease, reviewed by other agents, and merged automatically.
Your job is to point, to judge, and to argue.

The fastest way in is to do one curation end to end before reading anything about
how the machinery works. You do not need to understand the schema, the validation
stack or the merge rules to produce a good first entry — the agent knows all of
that, and you can ask it anything at any point: *"explain what this repo is"*,
*"why did the reviewer reject this"*, *"what should I do about this page"*.

Before you start, spend five minutes reading a finished entry in the
[disorder browser](https://dismech.monarchinitiative.org/app/). Pick a disease you
know. That tells you more about what we are building than any description of it.

## What you need

- **A Claude subscription** — Pro, Max or a Team plan. An Anthropic API key is not
  an alternative: Claude Code on the web runs on the subscription.
- **A deep-research key**, usually Edison ("falcon"). Academic accounts can
  request bonus credits.
- **Either** Claude Code on the web — no install, but a one-time cloud environment
  with network access set to **Full** and your keys as environment variables —
  **or** the local CLI, which needs `claude`, `just` and a clone.

All of it is written up in
[CONTRIBUTING.md](https://github.com/monarch-initiative/dismech/blob/main/CONTRIBUTING.md):
[install](https://github.com/monarch-initiative/dismech/blob/main/CONTRIBUTING.md#1-install-claude-code),
[research provider](https://github.com/monarch-initiative/dismech/blob/main/CONTRIBUTING.md#3-set-up-a-deep-research-provider-required),
[cloud environment](https://github.com/monarch-initiative/dismech/blob/main/CONTRIBUTING.md#running-dismech-in-claude-code-on-the-web).
Setup is the most annoying part of this whole thing and it is a one-time cost. If
it fights you, ask in Slack instead of grinding — you are almost certainly hitting
something we already know about.

One rule worth stating up front: use a top-tier model. The reviewer runs on one,
and weaker models mostly produce work that gets sent back.

## Your first curation

**On the web.** Open [claude.ai/code](https://claude.ai/code), select
`monarch-initiative/dismech`, start a new session and say:

```text
Give me a tour of this repo, then help me pick a disease to curate
```

Say what you care about if you have a preference — *"I'm a nephrologist, find me
something renal"* — otherwise let the agent choose. When you've agreed on one,
`/claim-disease` files the claim so nobody duplicates your work and starts the
curation; `/curate <Disease Name>` goes straight at a specific target. Then answer
questions when asked and leave it alone the rest of the time. When it's done,
press **Create pull request**; branching and commits are handled for you.

Keep the session open until the PR goes green — the reviewer will comment, and
your agent can answer it in the same session. Then archive it and start a fresh
session for the next disease.

**Locally.** Same conversation, after `git clone` and `claude`. `just next-stubs`
shows what's in the queue if you'd rather browse first. The agent validates as it
goes; to run the checks yourself, after each edit:

```bash
just validate kb/disorders/Your_Disease.yaml                  # schema
just validate-terms kb/disorders/Your_Disease.yaml            # ontology IDs + labels
just count-verified-snippets kb/disorders/Your_Disease.yaml   # snippets vs cached abstracts
```

and once before opening the PR, `just validate-disorders <your files>` — the
batched pass CI runs. Two surprises: the first `validate-terms` run downloads
ontology databases and some are multi-GB, and `just validate-references` on a
single file takes about an hour, so leave that one to CI. Push to a branch on
`origin`, never a fork — fork PRs don't get the automated review.

**After the PR is open**, an agent reviewer approves or requests changes, and a
deterministic sweep merges it once it is approved, green, unassigned and more than
three days old. So don't assign anyone to your own PR, and don't sit waiting for
the merge.

## The part that actually matters

Most people finish their first entry thinking: *I didn't make a single meaningful
decision.* That reaction is correct, and it is the most interesting thing about
this project rather than a flaw in it. The first curation is training wheels — it
teaches you the shape of the loop, and it is deliberately a loop where the agent
does the deciding.

What we don't yet know is where *your* judgement pays off most. That's the open
question, and the reason to write down what you try.

The habit that changes everything: **tell the agent who you are.** Open a session
with what you actually know and what you want out of this — clinician, bench
scientist, developer, program officer, or "no domain expertise, but I want to
understand X" — and ask what you could work on together. Then pick a direction:

- **Curate in your own field.** Take something you can judge and argue with the
  agent about the mechanism. Where the literature genuinely disagrees, say so and
  have it recorded as an open question instead of a confident sentence.
- **Review instead of write.** Read an entry in your field in the
  [browser](https://dismech.monarchinitiative.org/app/) and file issues, or have
  your agent review an open PR. Clinicians: see
  [Clinical Review Instructions](clinical-review-instructions.md).
- **Work above one disease.** Mechanisms that recur across disorders — fibrosis,
  senescence, granuloma formation — are modelled once and reused. Ask which of
  your diseases should reuse an existing one, or whether a new one is warranted
  ([modules primer](primers/modules-and-conformance.md)).
- **Chase something you think is wrong.** Pick a mechanism you suspect is
  under-evidenced or contested and have the agent assemble the case both ways.
- **Use it to learn.** "Assemble what is actually known about X, with citations I
  can check" is a legitimate session. The citations really are checked, which is
  more than you get from a chat window.
- **Improve what's there rather than add more.** `just compliance-all` ranks
  entries by what they're missing. Fixing the worst ten in your field is worth
  more than ten new ones.
- **Build on it.** The knowledge base exports to KGX and CX2/NDEx and has an
  embedding explorer and a [browser extension](browser-extension.md). Ask how it
  could plug into a portal or agent system you're working on.
- **Argue with other resources.** `just d2p-compare <Disease>` diffs our
  phenotypes against OMIM and Orphanet; disagreements are curation leads.

Then tell us what happened — in Slack, or as an issue. What worked, what felt
pointless, what you wanted to do and couldn't. Half the value of this phase is
finding out which of these is actually worth anyone's time, and that only works if
people say.

## If you want to know how it works

Read these when you need them, not before:

- [Data Model](data-model.md) — what an entry may say. The YAML files in `kb/`
  *are* the database; there is nothing behind them.
- [Curation Stub Queue](curation-stubs.md) — the work queue is a directory, not a
  ranking, and skipping candidates you can't judge is expected.
- [Quality Control & Compliance](quality-control.md) — how claims get checked:
  schema, ontology terms, and evidence snippets matched against the cited
  abstract. This is the main defence against confident fabrication.
- [Automation & Agents](explanation/automation-and-agents.md) — who reviews, what
  merges, and why a script rather than a person does the merging.
- [Design Decisions](explanation/design-decisions.md) — why it is built this way.
  Worth reading before arguing with a convention; the argument is usually there.
- [Pathographs](pathographs.md) and [Use Cases](use-cases.md) — the causal graph
  at the heart of an entry, and what it is all for.

## Getting unstuck

Ask your agent first — it reads the same conventions the reviewer enforces. File
an issue for anything that looks wrong; subject-matter feedback is welcome,
especially "this entry is wrong and here's why". Or ask a human in Slack; nobody
minds.

Two things to know early: everything here is
[AI-curated and not medical advice](disclaimer.md), and the default assumption is
that issue and PR content is agent-generated. If you wrote something yourself and
want that known, mark it `[human authored]`.
