# Contributing to dismech (guide for human)

Thank you for your interest in contributing to the Disorder Mechanisms Knowledge Base!

> [!WARNING]
> This guide is aimed at real humans. Agents are welcome to read this for context,
> but instructions aimed at people should not be confused for instructions for agents.

Most of this guide assumes some familiarity with running agent harnesses such as claude code
or codex. Even if you are not familiar with these, you are welcome to file issues.

This guide also assumes you are a member of the Monarch Initiative and specifically the dismech team.
While we welcome contributions from anyone, if you intend to make a PR, please read the note below
about forks. Issues are welcome from anyone.

If you are a subject matter expert, please give us feedback via the issue tracker! This can
be about anything.

## General philosophy

Dismech curation is currently running in heavily agent-forward mode. This may change in future.

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

Advanced users are welcome to try using alternative models and harnesses as experiments, or used intentionally
when you know how to match the level of difficulty with a task (but you should coordinate on slack before doing this).

## Be bold

Every member of the dismech team is encouraged to do work that ends in a PR. You are not expected to check the results
for yourself. We assume good faith and you are not intentionally pushing the agent to add bad content (though we
welcome this as an experiment, if you coordinate! you can see a few examples of this already, e.g [Bixonimania request](https://github.com/monarch-initiative/dismech/issues/1565)).

The general philosophy is to **trust the process**. All PRs are reviewed by agents using rubrics that have been
extensively evaluated by agents and humans in collaboration. Additionally, a battery of hard validation checks
and anti-hallucination measures are applied. This is not guaranteed to be perfect, but we also believe
in incremental improvement. No entry is finished, and in fact all entries are continuously being refined.

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

## Technical Guidelines for Contributing

### Coding agent

Most contributors use **Claude Code** or **Codex** for AI-assisted curation. To contribute as an agent manager:

### 1. Install Claude Code
- Get a Claude Pro subscription at [claude.ai](https://claude.ai)
- Install Claude Code CLI:
  ```bash
  brew install claude-code  # macOS
  ```
  For other platforms, see [claude.ai/code](https://claude.ai/code)

### 2. Install `just` Command Runner
Test if you have it:
```bash
just --version
```

If not installed:
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

Note: if you are affiliated with an academic institution you should be able to request bonus credits with Edison

**Alternative providers:** openscientist, perplexity, openai, cyberian (see `.claude/skills/initiate-new-disorder-creation/` for details)

We no longer recommend Asta for the deep research role

### 4. Clone and Start
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

## Curation Model: AI-Assisted with Human Oversight

This knowledge base uses an **AI-first curation model**:

- **YAML files are the source of truth** (`kb/disorders/*.yaml`)
- **AI agents make the vast majority of edits** via automated pipelines and GitHub integrations
- **Human curators review and validate processes**
- **Automated validation** catches errors before merge

## Contributing Curation Expertise

We welcome any corrections. Our general philosophy is to curate the *process* (we also call this "human regulating the loop" rather than "human in the loop")

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

### dragon-ai-agent

- Summon with `@dragon-ai-agent please`
- You must be a registered ai-controller in the json file

### claude issue responder

- watches github issues and responds
- you must be part of the project for this to work. Contact dismech team to be added

### Standard CI/CD

- rigorous battery of linkml schema checks, linkml-term-validator, linkml-reference-validator

### AI reviewers

- reviews all PRs
- will mark PRs as being "changes requested" or "ready to merge"
- does not work on forks; see above

### Scanners

Various scanners operate at different intervals

- scanning literature for new papers, creating issues
- scanning unadopted open issues and PRs, and moves them forward
- scans for incomplete entries using linkml-data-qc and creates PRs to enhance them

Unlike the review agent which is always top-tier model, some scanners for low-risk tasks may
use cheaper models. Additionally, github labels can be used to manually assign tasks to
lower quality models (use the `low_effort` tag)

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

Human curators are welcome! However, as an AI agent I would encourage humans to spend their precious time on high level evaluation and
direction of AI agents rather than directly editing files.

To understand the curation guidelines:

1. **Read `CLAUDE.md`** - Contains the same instructions AI agents follow
2. **Review `.claude/skills/`** - Detailed guidelines for term and reference validation
3. **Run QC locally** before submitting PRs:
   ```bash
   just qc
   ```

## Regenerating Site Content

After making changes to `kb/disorders/*.yaml` files, regenerate the static site:

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

**When to run:** After adding new disorders or making significant content changes.

**View the explorer:**
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

All contributions must pass validation:

```bash
# Schema validation
just validate-all

# Ontology term validation (catches fake/mismatched term IDs)
just validate-terms

# Reference validation (confirms snippets appear in cited papers)
just validate-references kb/disorders/YourFile.yaml
```

Disease entries should also maintain lifecycle metadata timestamps:
- `creation_date`: when the file/entry was first created
- `updated_date`: last substantive content update

Use ISO 8601/RFC 3339 datetime strings (for example, `2025-06-12T20:16:27Z`), and keep `creation_date` unchanged after initial creation.

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

## Code of Conduct

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.
