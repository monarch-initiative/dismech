# Onboarding: your first week in dismech

A short front door for new contributors. Read this once, do one curation, then
come back for the "what to try next" section at the bottom.

This page deliberately stays brief and links out. The two long-form documents it
sits on top of are
[CONTRIBUTING.md](https://github.com/monarch-initiative/dismech/blob/main/CONTRIBUTING.md)
(setup, philosophy, house rules) and
[Automation & Agents](explanation/automation-and-agents.md) (what the robots do
while you sleep).

## 1. What the system actually is

Five things, in the order work flows through them:

1. **A schema.** One LinkML model
   (`src/dismech/schema/dismech.yaml`) defines what a disease entry may say —
   pathophysiology nodes, phenotypes, evidence, treatments, genetics. Start with the
   [Data Model overview](data-model.md); the generated
   [Schema Reference](schema/schemas/dismech.md) has the exact details.
2. **A knowledge base of YAML files.** `kb/disorders/*.yaml` is the source of
   truth — one file per disease, plus `kb/modules/` (mechanisms recurring across
   diseases), `kb/groupings/`, `kb/comorbidities/`. Nothing is stored in a
   database; the files *are* the database.
3. **A queue.** `stubs/` holds one YAML file per disease we intend to curate.
   The queue is a directory, not a ranked score, and you are expected to skip
   past candidates you can't curate well — see
   [Curation Stub Queue](curation-stubs.md).
4. **A validation stack.** Every claim has to survive machine checking: schema
   conformance, ontology term IDs *and* labels checked against the real
   ontologies, and evidence snippets checked as exact substrings of the cited
   abstract. This is the project's main defence against confident-sounding
   fabrication. See [Quality Control & Compliance](quality-control.md).
5. **An agent pipeline.** You start an agent, it curates, it opens a PR, a
   *different* agent reviews it, and a deterministic script merges it once it is
   approved, green, unassigned and three days old. Details in
   [Automation & Agents](explanation/automation-and-agents.md).

The output is rendered as browsable pages — the
[disorder browser](https://dismech.monarchinitiative.org/app/) is the fastest way
to see what a finished entry looks like. Pick any disease and read its
pathograph before you curate one.

**Why it is built this way** — the scope of what counts as a dismech entry, why
LinkML, why the ontology set is constrained, the evidence policy — is recorded in
the [design decision register](explanation/design-decisions.md). Read it before
arguing with a convention; it usually already contains the argument.

Two framing documents worth ten minutes each: [Pathographs](pathographs.md) (the
causal graph at the heart of an entry) and [Use Cases](use-cases.md) (what this is
all *for*).

## 2. Before your first curation

You need a Claude Pro or Max subscription (or a Team plan), and a decision about
where to run: **Claude Code on the web** (nothing to install, recommended for your
first one) or the **local CLI** (full control, your own tooling).

Both routes need the same one-time bits, and both are written up properly in
CONTRIBUTING.md — don't reinvent them:

- [Install Claude Code + `just`](https://github.com/monarch-initiative/dismech/blob/main/CONTRIBUTING.md#1-install-claude-code)
- [Set up a deep-research provider](https://github.com/monarch-initiative/dismech/blob/main/CONTRIBUTING.md#3-set-up-a-deep-research-provider-required)
  (Edison/falcon; academic accounts can request bonus credits)
- [Set up Claude Code on the web](https://github.com/monarch-initiative/dismech/blob/main/CONTRIBUTING.md#running-dismech-in-claude-code-on-the-web),
  including the cloud environment — network access **Full**, your API keys as
  environment variables, and `uv tool install rust-just` in the setup script

!!! warning "Use a top-tier model"

    Weaker models produce entries that fail review and waste everybody's time,
    including yours. The reviewer always runs on a strong model; match it.

## 3. Your first curation, step by step

The goal of the first one is to watch the machine work end to end. Let the agent
drive. You are not expected to verify every claim — the reviewer will.

### Route A — Claude Code on the web (recommended first)

1. Open [claude.ai/code](https://claude.ai/code), select
   `monarch-initiative/dismech`, and confirm your dismech environment is selected
   (the cloud icon near the prompt).
2. Start a **new session** and type:

    ```text
    Give me a tour of this repo, then help me pick a disease to curate
    ```

    If you have a domain you care about, say so — "I'm a nephrologist, find me
    something renal". If you don't, let the agent pick.

3. When you've agreed on a disease, let it run:

    ```text
    /claim-disease
    ```

    That files a claim issue (so nobody duplicates your work) and starts the
    curation. To curate something specific instead, use `/curate <Disease Name>`.

4. **Answer questions when asked, otherwise leave it alone.** The agent does deep
   research, drafts the YAML, binds ontology terms, fetches abstracts, and runs
   validation. This takes a while.
5. When it says it's done, click **Create pull request**. Branching, commits and
   the PR are handled for you.
6. **Keep the session alive until the PR is green.** The reviewer bot will
   comment; the agent can answer it in the same session. Once checks pass and it
   is approved, archive the session from the sidebar.
7. Start a **new session** for your next disease. Cloud sessions are cheap to
   create and get slow if you pile unrelated work into one.

### Route B — local Claude Code CLI

1. Clone and enter the repo, then launch the agent:

    ```bash
    git clone https://github.com/monarch-initiative/dismech.git
    cd dismech
    claude
    ```

2. Same conversation as above — `/claim-disease`, or `/curate Parkinson Disease`
   for a specific target. `just next-stubs` shows you what's in the queue if you
   want to browse first.
3. The agent works in the repo and validates as it goes. After each edit — these
   are fast and offline:

    ```bash
    just validate kb/disorders/Your_Disease.yaml                  # schema
    just validate-terms kb/disorders/Your_Disease.yaml            # ontology IDs + labels
    just count-verified-snippets kb/disorders/Your_Disease.yaml   # snippets vs cached abstracts
    ```

    Once, before you open the PR — the batched pass CI runs on your changed files:

    ```bash
    just validate-disorders kb/disorders/Your_Disease.yaml
    ```

    Two things that surprise people: the first `just validate-terms` run downloads
    ontology databases and some are multi-GB
    ([details](https://github.com/monarch-initiative/dismech/blob/main/CONTRIBUTING.md#ontology-databases-and-constrained-environments)),
    and `just validate-references` on a single file takes about an hour — leave
    that one to CI.

4. Ask it to open the PR (`/create-pr`), or let it do so as part of the curation
   flow. Push to a branch on `origin`, **not a fork** — fork PRs don't get the
   automated review, because GitHub withholds secrets from them.

!!! note "Never hand-write a reference cache file"

    `references_cache/*.md` is created **only** by `just fetch-reference PMID:...`.
    A hand-written cache file makes snippet validation meaningless, and it is the
    single most common way an agent quietly breaks the evidence chain.

### What happens after you open the PR

- An agent reviewer (`ai4c-reviewer`) reviews the diff and submits either
  **approve** or **request changes**, with severity-tagged comments.
- If changes are requested, your session's agent can address them — or a scheduled
  **PR Shepherd** run will pick it up within a few hours.
- A deterministic sweep then squash-merges the PR once it is *simultaneously*
  approved, not a draft, **unassigned**, conflict-free, green, and **more than
  three days old**. Nobody judges it at that point; the predicate is mechanical.
- Practical consequences: **don't assign anyone to your PR** unless you want to
  hold it open, and **don't wait around for the merge** — three days is normal.

The full state vocabulary (what `DISMISSED` means, `mergeable` vs
`mergeStateStatus`, why the sweep is separate from the agent step) is in
[Automation & Agents](explanation/automation-and-agents.md).

## 4. Things to play with next

The first curation is training wheels — you are mostly clicking "continue". That's
deliberate, and it is not the interesting part of the job. Once the flow is
familiar, the point is to put your own judgement somewhere the agent can't.

**Tell the agent who you are.** Start a session with what you actually know and
what you want out of this — clinician, bench scientist, developer, program
officer, or "no domain expertise but I want to understand X". Then ask it what you
could work on together. This changes the work substantially, and it is the single
highest-value habit to build.

Concrete directions, roughly in order of how much they lean on you:

- **Curate in your own domain.** Use `just next-stubs` (or ask the agent) and pick
  something you can judge. Argue with the agent about mechanism. Where the
  literature is genuinely unresolved, that's a `mechanistic_hypotheses` entry or a
  `KNOWLEDGE_GAP` discussion, not a confident sentence.
- **Review instead of create.** Read an existing entry in your field on the
  [browser](https://dismech.monarchinitiative.org/app/) and file issues, or ask
  your agent to review an open PR with the `dismech-pr-review` skill. Clinical
  reviewers should read [Clinical Review Instructions](clinical-review-instructions.md).
- **Work above the level of one disease.** Mechanism *modules* (a conserved
  process reused across disorders — fibrosis, senescence, granuloma formation),
  *groupings*, and *comorbidities* are where the model gets interesting. Read
  [Modules & Conformance](primers/modules-and-conformance.md), then ask the agent
  which of your diseases should conform to an existing module — or whether a new
  one is warranted.
- **Chase a hypothesis or a knowledge gap.** Pick a mechanism you think is wrong,
  under-evidenced, or contested, and have the agent assemble the evidence for and
  against. See [Hypothesis Report Assessments](hypothesis-report-assessments.md).
- **Use it as a teaching tool.** With no domain expertise, "assemble what is
  actually known about X, with citations I can check" is a legitimate and useful
  session. The validation stack means the citations are real, which is more than
  most chat sessions give you.
- **Attack quality rather than coverage.** `just compliance-all` ranks entries by
  missing fields; `just gen-dashboard` builds the QC dashboard. Fixing the worst
  ten entries in your domain is worth more than ten new stubs.
- **Developer angles.** The KB exports to KGX and CX2/NDEx, has an embedding
  explorer (`just embed-similar <Disease>`, `just embed-search "<query>"`), a
  browser app, and a [browser extension](browser-extension.md). Ask how dismech
  could plug into a portal or agentic system you're building — that conversation
  usually produces issues worth filing.
- **Compare against other resources.** `just d2p-compare <Disease>` diffs our
  phenotypes against OMIM/Orphanet; `just g2p-compare <GENE>` does the same for
  gene-disease assertions. Disagreements are curation leads.

Whatever you pick, say what you're doing in Slack. Half the value of the current
phase is finding out which of these actually works.

## 5. When something looks wrong

- **Ask your agent first.** "Explain what this repo is", "why did the reviewer
  reject this", "what should I do about this page" are all good opening moves, and
  the agent reads the same conventions the reviewer enforces.
- **File an issue.** Anyone can. Subject-matter feedback is welcome even (perhaps
  especially) when it is "this entry is wrong and here's why".
- **Ask a human on Slack.** Nobody minds.

Two things to internalise early: everything here is
[AI-curated and not medical advice](disclaimer.md), and the default assumption is
that issue and PR content is agent-generated. If *you* wrote something yourself
and want that known, mark it `[human authored]`.
