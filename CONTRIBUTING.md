# Contributing to dismech (guide for humans)

Thank you for your interest in contributing to the Disorder Mechanisms Knowledge Base!

> [!WARNING]
> This guide is aimed at **real humans**. Agents are welcome to read this for context,
> but instructions aimed at people should not be confused for instructions for agents.
> Agent instructions are in the usual places.

Most of this guide assumes some familiarity with running agent harnesses such as claude code
or codex. Even if you are not familiar with these, you are welcome to file issues
(__UPDATE__: see [#6833](https://github.com/monarch-initiative/dismech/issues/6833) for instructions on filing issues as a non-collaborator).

This guide also assumes you are a member of the Monarch Initiative and specifically the dismech team.
While we welcome contributions from anyone, if you intend to make a PR, please read the note below
about forks. Issues are welcome from anyone.

If you are a subject matter expert, please give us feedback via the issue tracker! This can
be about anything.

## General philosophy

DisMech curation is currently running in heavily agent-forward mode. This may change in future.

- dismech is alpha stage and experimental. AI may make mistakes.
- agent activities are initiated by humans or by github actions
- humans are encouraged to let agents do work without editorializing
    - this includes the generation of issue and PR comments
- the default assumption for any issue or PR is that the contents AND comments are AI-generated
    - unlike some repos, humans are NOT assumed to be accountable for verifying all content their agents generate
    - if you are writing content yourself and wish it to be identified as such, you may indicate this, but this is not required
         - e.g. in an issue comment write something like `[human authored]`

## Ask your agent to explain the contribution process

Assume that content aimed at humans (such as this document) may become stale. The multiple interlocking curatorial
processes in dismech are inherently dynamic and complex. But fear not, you can always ask your agent to explain things.

These are all perfectly valid things to ask claude/codex at the start of your session:

- "I want to contribute. How?"
- "Explain what this repo is"
- "I noticed a problem on one of the pages -- what should I do?"

And you are always welcome to ask a friendly human on Slack, or in an issue!

## Always use top-tier models and harnesses

You should always use best-of-class models, and up to date high quality harnesses. Using less powerful
models is more likely to generate lower quality content. While this will typically be caught during agentic review
(which always uses high quality models), use of lower quality models can lead to wasteful back and forth. Also,
this is more of a drain on your time.

Advanced users are welcome to try using alternative models and harnesses as experiments, or use them intentionally
when you know how to match the level of difficulty with a task (but you should coordinate on Slack before doing this).

## Be bold

Every member of the dismech team is encouraged to do work that ends in a PR. You are not expected to check the results
for yourself. We assume that you are acting in good faith and you are not intentionally pushing the agent to add bad content (though we
welcome this as an experiment, if you coordinate first! you can see a few examples of this already, e.g. [Bixonimania request](https://github.com/monarch-initiative/dismech/issues/1565)).

The general philosophy is to **trust the process**. All PRs are reviewed by agents using rubrics that have been
extensively evaluated by agents and humans in collaboration. Additionally, a battery of hard validation checks
and anti-hallucination measures are applied. This is not guaranteed to be perfect, but we also believe
in incremental improvement. No entry is ever considered "finished", and in fact all entries are continuously being refined.

## Important: Open PRs from Origin Branches, Not Forks

Do not open pull requests from forks. This repository depends on automated AI
review and GitHub does not expose repository secrets to workflows triggered from
forks, so fork-based PRs will not receive automated AI review.

Contributors should push branches directly to `origin` and open PRs from those
branches. If you are a new contributor and do not yet have access, first open an
issue asking to be added to the repository. Known members of the Monarch and
biomedical informatics communities will be added promptly. Other contributors
are welcome to join a community call and introduce themselves before being
granted branch access.

## A note on 'draft' status

Currently the GitHub 'draft' status is not very meaningful. Any PR that is created will be reviewed
and possibly modified and advanced towards a final merge, regardless of draft status. If you do not wish this to
happen then you can push changes without making a PR. However, in general you should follow the "be bold" guidelines.

In terms of GitHub mechanics, draft status may block auto-merge.

In future the workflow may be modified since the current status is a bit confusing.

## Technical Guidelines for Contributing

As described above, contributions to DisMech are made by humans invoking AI agents, with other AI agents vetting the contributions.

### Coding agent

Most contributors use **Claude Code** or **Codex** for AI-assisted curation.
The instructions below explain how to install the Claude Code command-line interface (CLI).
An easier option for many people who want to curate diseases in DisMech is to set up the Claude Code web interface ([claude.ai/code](https://claude.ai/code)).
For instructions on that, please see the section on [Running dismech in Claude Code on the web](#running-dismech-in-claude-code-on-the-web).

### 1. Install Claude Code
- Get a Claude Pro subscription at [claude.ai](https://claude.ai) - you won't be able to do curation with the free version of Claude.
- Install Claude Code CLI:
  ```bash
  brew install claude-code  # macOS
  ```

For installing on other (non-macOS) platforms, see [claude.ai/code](https://claude.ai/code).

### 2. Install `just` Command Runner
Test if you have it:
```bash
just --version
```

If not, install it:
```bash
brew install just  # macOS
# Or see https://github.com/casey/just#installation for other platforms
```

(or just ask your agent to do this)

### 3. Set Up a Deep Research Provider (Required)

For comprehensive biomedical literature research, we recommend **Edison Scientific (falcon)**:

1. Create an account at [platform.edisonscientific.com](https://platform.edisonscientific.com/)
2. Navigate to: Account → Profile → + Create new token
3. Copy your API key and set it in your environment:
   ```bash
   export EDISON_API_KEY=your_key_here
   ```

(The Edison literature tool was originally called Falcon, hence the filenames this makes will be called `*-falcon.md`)

Note that the Edison API key, unlike other keys, should be written as just the plain key, not with the "keyname:" prefix.
WRONG: EDISON_API_KEY=Edison-for-dismech2:asdfjlkajsdfklasjdf
RIGHT: EDISON_API_KEY=asdfjlkajsdfklasjdf

Note: if you are affiliated with an academic institution you should be able to request bonus credits with Edison

**Alternative providers:** openscientist, perplexity, openai, cyberian (see `.claude/skills/initiate-new-disorder-creation/` for details).
For example, `openscientist` uses its own `OPENSCIENTIST_API_KEY` — see [3b](#3b-set-up-openscientist-for-hypothesis-exploration) below.

We no longer recommend Asta for the deep research role.

#### 3b. Set up OpenScientist for hypothesis exploration

[OpenScientist](https://github.com/openscientist-io/openscientist) is our autonomous AI scientist that generates and tests hypotheses from scientific data.

Any agent can use OpenScientist in two ways:

1. as a literature deep research tool
2. as a tool combining literature search, hypothesis generation, data analysis, and data exploration

In fact, 1 is really just a subset of 2.

In both cases, you will need to obtain an API key from [openscientist.io](https://openscientist.io)

```bash
   export OPENSCIENTIST_API_KEY=your_key_here
   ```

### 4. Clone repo and start curating
```bash
git clone https://github.com/monarch-initiative/dismech.git
cd dismech
```

Open Claude Code and ask:
```
Give me a tour of the dismech project
```

Then start curating using the `curate` skill:

```
/curate Parkinson Disease
```

For more guidance on AI-assisted curation workflows, see [ai4curation/aidocs](https://github.com/ai4curation/aidocs).

### Running dismech in Claude Code on the web

Assuming you have Claude Pro or Max (or a Team plan), you can curate from [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web)
instead of the local CLI. This makes the curation process simpler. The repo is cloned for you, and when you're done you
just press **Create PR** — commits and the PR are handled for you.

The one non-obvious part is a **one-time cloud environment setup**. An
*environment* is a reusable config (network access, environment variables, and
an optional setup script) that your cloud sessions run in. Instructions are below.

#### Setting up Claude Code on the web

NOTE: these instructions and screenshots were added on 2026-07-28 and may change in the future.

1. Go to [claude.ai/code](https://claude.ai/code). Click the grayed-out tab near the top left that says "`</>` Code".
   <img width="372" height="289" alt="Screenshot 2026-07-28 at 3 34 35 PM" src="https://github.com/user-attachments/assets/e3733117-cd95-40b1-a256-ad1753ff455f" />

2. Ignore the "Download for macOS" button and click the "Continue on web →" button lower down.
   <img width="679" height="578" alt="Screenshot 2026-07-28 at 3 59 39 PM" src="https://github.com/user-attachments/assets/f2be279f-f5f7-4860-83a4-11c7afe8b9ca" />

3. Click "Get Started" and then, on the next screen, click "Connect a different way".
   <img width="409" height="396" alt="Screenshot 2026-07-28 at 4 23 47 PM" src="https://github.com/user-attachments/assets/d355f9e8-00fc-4433-bdca-90adb60603fc" />

4. Click "Continue with GitHub", then click "Authorize".
   <img width="755" height="383" alt="Screenshot 2026-07-28 at 4 25 48 PM" src="https://github.com/user-attachments/assets/821ff73e-91a6-4998-b312-720db905a824" />

5. You should now be at claude.ai/code. Click the "+ Select repo" button above the query box, and select "monarch-initiative/dismech" from the list of repos. If it doesn't appear there, find it via the query box.
   <img width="498" height="564" alt="Screenshot 2026-07-28 at 4 33 47 PM" src="https://github.com/user-attachments/assets/91c46ea4-f990-414d-bd7b-ee6e1989c90a" />

Now you're ready to set up your cloud environment (this is a one-time step).

#### Setting up your cloud environment

1. **Configure the environment.** At [claude.ai/code](https://claude.ai/code), select
   the current environment by clicking the button with a cloud icon (which probably says "Default") to open the environment selector.
   
   <img width="378" height="338" alt="Screenshot 2026-07-28 at 4 36 54 PM" src="https://github.com/user-attachments/assets/8b0eb12b-954a-4e50-a9c9-282d0db22a4d" />

   Now (this is a bit non-obvious) _hover_ your mouse over the checkmark next to "Default" to make the gear icon appear, and click the gear to open the environment settings dialog.
   
   <img width="355" height="104" alt="Screenshot 2026-07-28 at 4 37 20 PM" src="https://github.com/user-attachments/assets/2d91832c-2742-4f4d-ac9a-ce548a2414d6" />

   The dialog has fields for the name, network access level, environment
   variables, and setup script.
   (The "Create your environment" step of [the get-started guide](https://code.claude.com/docs/en/web-quickstart) describes these fields.)

3. **Name your environment.**
   Click on the Name box and choose a name for your environment (e.g., "dismech").
   
4. **Set Network access to Full.**
   Use the **Network
   access** selector and choose **Full**. The default setting, **Trusted**,
   only allows an allowlist of package registries and GitHub, which blocks the
   literature/deep-research and structured-source hosts that dismech curation accesses
   (PubMed, ClinicalTrials.gov, Edison, OpenScientist, Orphanet, ClinGen).

5. **Add your deep-research API keys** in the Environment variables field. This field
   uses `.env` format — one `KEY=value` per line, and **do not use quotes** (quotes are stored as part of the value):
   ```text
   EDISON_API_KEY=<YOUR_EDISON_KEY>
   OPENSCIENTIST_API_KEY=<YOUR_OPENSCIENTIST_KEY>
   ```

   These are the same keys as the local setup — see
   [Set Up a Deep Research Provider](#3-set-up-a-deep-research-provider-required)
   above for how to obtain them. If you set these up locally, they're in whatever
   shell profile you exported them from (e.g. `~/.zshrc`).

   Note: the Environment variables field is plain text, not a secrets store — the values are
   visible to anyone who can open the environment's settings. On a personal account, that's only you.
   
6. **Add an install of `just` to the setup script** in the "Setup script" box (just this one line):
   ```
   uv tool install rust-just
   ```
   If you don't do this, every session has to re-install `just` before curation can start.

   Note that the "Setup script" is the home for any other one-time bootstraps that you may want to add.

Setting up the cloud configuration is the only hard part. Once the environment exists, curation on the web works the same
as on the command line — `/curate` a disorder, then create the PR when ready.

#### Cloud sessions

One of the nice things about running Claude on the web is that you can set up multiple sessions, and archive them when they're finished. Archived sessions don't use any tokens, but you can restart them if you want.

**Tip: keep each session focused.** Every cloud session runs in a fresh VM with
approximate ceilings (a memory limit and ~30 GB of disk). A single session that
curates one disorder or a small group of related disorders stays well within
those limits; one that keeps going across many unrelated diseases accumulates
context and on-disk state (downloaded ontology DBs, caches) and can slow down or
hit the ceiling. Prefer a **new session per disorder or small themed batch**,
then let it finish; you can archive finished sessions from the sidebar to keep
the list tidy. The environment config is reused automatically, so a new session
costs you nothing to set up.

**Tip: how to find (and potentially restart) your archived sessions.** In the sidebar, click the toggle icon next to Recents,
choose "Status", and change from "Active" to "Archived" or "All".

## Curation Model: AI-Assisted with Human Oversight

This knowledge base uses an **AI-first curation model**:

- **YAML files are the source of truth** (`kb/disorders/*.yaml`)
- **AI agents make the vast majority of edits** via automated pipelines and GitHub integrations
- **Human curators review and validate processes**
- **Automated validation** catches errors before merge

## Contributing Curation Expertise

We welcome any corrections. Our general philosophy is to curate the *process* (we also call this "human regulating the loop" rather than "human in the loop"):

- look for *patterns* where results are suboptimal; curate examples and counter-examples; work with agent to integrate this into the process
- review the reviews: are there things the AI reviewer misses, or does it obsess over things that are less relevant? work with an agent to improve this
- curate the process: look at the various automated and user-triggered processes in this repo. Are some too eager, not eager enough?

We also welcome curation at the level of individual entries. Reports can be filed on the issue tracker. For users who are familiar with coding agents:

- open your agent in the repo
- say "I am an expert on X. Where can I contribute my expertise?"

### GitHub Automation

We use a number of GitHub automations in this project. Some of these derive from [ai4curation/github-ai-integrations](https://github.com/ai4curation/github-ai-integrations)
but we have gone much further.

You can explore these in the "Actions" tab in GitHub. For up to date documentation, ask an agent. What follows here may be out of date, but should
still give a flavor of what we do.

**Two different things get called "assigning an agent".** GitHub's own **"Assign
agent to issue"** (Preview) dispatches a coding agent — there, assignment *is* the
trigger. DisMech's own workflow agents are **mention**-driven (`@claude`,
`@dragon-ai-agent`) and never fire on assignment; to them an assignee means
"claimed", which removes the issue from the curation scanner's queue. See
[What assigning an issue actually does](https://monarch-initiative.github.io/dismech/explanation/automation-and-agents/#what-assigning-an-issue-actually-does).

### dragon-ai-agent

In dismech, dragon-ai-agent acts as an autonomous curator/reviewer bot integrated into the repo's issue and PR workflow.

- Summon by writing **@dragon-ai-agent please &lt;your request&gt;** in an issue or PR
  comment/body. Write it as ordinary prose — the mention is ignored if it appears
  inside an inline code span or fenced code block (so that documenting the keyword
  doesn't accidentally trigger the agent).
- You must be a registered ai-controller in the json file

### Claude issue responder

- watches github issues and responds
- you must be part of the project for this to work. Contact dismech team to be added.
- Note: letting it watch issues consumes org API tokens, so use that judiciously

### Standard CI/CD

- rigorous battery of linkml schema checks, linkml-term-validator, linkml-reference-validator

### AI reviewers

The "AI reviewers" here are the claude-code-review and post-review-agent workflows (models configured in `.github/agent-config.yaml`, cadence in `.github/cron-profiles.yaml`); the dismech-pr-review skill defines the review rubric they apply.

- reviews all PRs
- will mark PRs as being "changes requested" or "ready to merge"
- does not work on forks; see above

### Scanners

Various scanners operate at different intervals:

- scanning literature for new papers, creating issues
- scanning unadopted open issues and PRs, and moves them forward
- scans for incomplete entries using linkml-data-qc and creates PRs to enhance them

Unlike the review agent, which always uses a top-tier model, some scanners for low-risk tasks may
use cheaper models. Additionally, github labels can be used to manually assign tasks to
lower quality models (use the `low_effort` tag).

### For AI Agents (Claude Code, etc.)

If you're an AI agent working on this repository:

1. **Read `CLAUDE.md`** for project-specific instructions and commands
2. **Use the skills in `.claude/skills/`**:
   - `dismech-terms/` - Guidelines for ontology term annotations
   - `dismech-references/` - Guidelines for evidence validation
3. **Always run validation** before committing:
   ```bash
   just qc
   ```
4. **Use OAK** to look up ontology terms (never guess IDs or labels):
   ```bash
   uv run runoak -i sqlite:obo:hp info "seizure"
   ```

### For Human Curators

Human curators are welcome! However, humans are encouraged to spend their precious time on high level evaluation and
direction of AI agents rather than directly editing files.

To understand the curation guidelines:

1. **Read `CLAUDE.md`** - Contains the same instructions AI agents follow
2. **Review `.claude/skills/`** - Detailed guidelines for term and reference validation
3. **Run QC locally** before submitting PRs:
   ```bash
   just qc
   ```

## Regenerating Site Content

After making changes to `kb/disorders/*.yaml` files, a github job will regenerate the site. You don't need to
know the details but we provide them here anyway:

### Browser App & HTML Pages

This is now automated, but the following command will manually rebuild all browser pages.

```bash
just gen-all
```

This updates:
- `app/data.js` - Main browser app data
- `pages/disorders/*.html` - Individual disorder pages

### Embedding Explorer

The embedding explorer (`app/embeddings/`) visualizes disorders in semantic space. **One command rebuilds everything:**

```bash
just embed-all
```

This:
1. Re-indexes embeddings via OpenAI API (requires `OPENAI_API_KEY`)
2. Computes UMAP/t-SNE coordinates
3. Generates `app/embeddings/data.js`

**View the explorer locally:**
```bash
open app/embeddings/index.html
```

## What to Contribute

### High-Value Contributions

- **New disorders**: Add YAML files for diseases not yet covered
- **Missing ontology terms**: Add `phenotype_term`, `treatment_term`, etc. to existing entries
- **Evidence**: Add PMID-backed evidence for existing claims
- **Corrections**: Fix incorrect information (with evidence)

### Quality Standards

All contributions must pass validation (this is done for you; your PR will not be merged until your agent resolves these)

```bash
# Schema validation
just validate-all

# Ontology term validation (catches fake/mismatched term IDs)
just validate-terms

# Snippet check against the local reference cache (seconds — use this while you
# curate; it accepts any number of files)
just count-verified-snippets kb/disorders/YourFile.yaml

# Before opening the PR: the batched schema + terms + references sweep CI runs
just validate-disorders kb/disorders/YourFile.yaml

# Reference validation for one file (slow; permits full-text matches)
just validate-references kb/disorders/YourFile.yaml
```


### Ontology databases and constrained environments

Term validation is backed by OAK's `sqlite:obo:*` databases (mapped in
`conf/oak_config.yaml`). When a database is missing, OAK downloads it on demand
from the public [`bbop-sqlite`](https://s3.amazonaws.com/bbop-sqlite) bucket into
`~/.data/oaklib/`. Some of these are large:

| Ontology | Approx. size (unpacked) |
|----------|-------------------------|
| `ncbitaxon` | ~13.5 GB (2.1 GB gzipped) |
| `ncit` | ~2.7 GB |
| `mondo`, `chebi`, `uberon`, `hp`, `go` | tens–hundreds of MB each |

In network- or disk-constrained environments (Claude Code on the web, sandboxed
agents, metered connections) an interrupted big-file download can abort a
validation run. Two things make this manageable:

NOTE: we should be using OLS for the above now

- **Single-file validation does not force these downloads.** `just validate`,
  `just validate-terms`, `just validate-module`, `just validate-grouping`, and
  `just validate-comorbidity` trust the committed `cache/*.csv` and only query
  OAK for CURIEs that are *not* already cached (typically only when you add a
  brand-new term). They deliberately skip the whole-cache `check-enum-cache`
  integrity step, which re-derives every dynamic enum from OAK (and would pull
  `ncbitaxon`/`ncit`). That integrity check still runs in whole-KB commands
  (`just validate-all`, `just qc`) and in CI.

- **Pre-provision the databases when you do need them** (e.g. before a full
  `just qc`, or when adding a novel organism/NCIT term). This fetches with
  resume + retry and reports the disk footprint, instead of failing mid-run:

  ```bash
  just fetch-ontology-dbs                 # all sqlite:obo:* DBs in oak_config.yaml
  just fetch-ontology-dbs ncbitaxon hp    # only the ones you need
  ```

  Unpacking `ncbitaxon` needs ~16 GB free; the full OAK cache can reach ~26 GB.

- **Offline structural check.** `just check-enum-cache-offline` audits the
  committed enum caches (stale files, malformed headers, duplicate rows) without
  any OAK access or downloads; only the CURIE-membership re-derivation is
  skipped.

To stop OAK from repeatedly re-attempting a download once the DBs are present,
you can set a no-refresh cache policy at
`~/.config/ontology-access-kit/cache.conf`:

```
[default]
default = no-refresh
```

## Pull Request Process

1. Create a branch for your changes on `origin`, not on a fork
2. Make edits to YAML files in `kb/disorders/`
3. Run `just qc` to validate
4. Submit a pull request
5. Address any CI failures
6. Wait for review from maintainers

## Questions?

- **Issues**: [GitHub Issues](https://github.com/monarch-initiative/dismech/issues)
- **Discussions**: [GitHub Discussions](https://github.com/monarch-initiative/dismech/discussions)

See also

 - https://github.com/monarch-initiative/dismech/issues/6833
 - https://github.com/monarch-initiative/dismech/issues/4794

## Code of Conduct

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.
