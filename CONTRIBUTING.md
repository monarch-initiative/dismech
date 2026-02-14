# Contributing to dismech

Thank you for your interest in contributing to the Disorder Mechanisms Knowledge Base!

## Prerequisites for Contributing

This repository uses **Claude Code** for AI-assisted curation. To contribute as an agent manager:

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

### 3. Set Up Deep Research Provider (Recommended)
For comprehensive biomedical literature research, we recommend **Edison Scientific (falcon)**:

1. Create an account at [platform.edisonscientific.com](https://platform.edisonscientific.com/)
2. Navigate to: Account → Profile → + Create new token
3. Copy your API key and set it in your environment:
   ```bash
   export EDISON_API_KEY=your_key_here
   ```

**Alternative providers:** perplexity, openai, cyberian (see `.claude/skills/initiate-new-disorder-creation/` for details)

### 4. Clone and Start
```bash
git clone https://github.com/monarch-initiative/dismech.git
cd dismech
```

Open Claude Code and ask:
```
Give me a tour of the dismech project
```

Then start curating:
```
/curate Parkinson Disease
```

For more guidance on AI-assisted curation workflows, see [ai4curation/aidocs](https://github.com/ai4curation/aidocs).

## Curation Model: AI-Assisted with Human Oversight

This knowledge base uses an **AI-first curation model**:

- **YAML files are the source of truth** (`kb/disorders/*.yaml`)
- **AI agents make most edits** via automated pipelines and GitHub integrations
- **Human curators review and validate** AI-generated content
- **Automated validation** catches errors before merge

### GitHub AI Integrations

We use [ai4curation/github-ai-integrations](https://github.com/ai4curation/github-ai-integrations) to enable AI agents to propose changes via pull requests. AI agents can:

- Add new disorder entries
- Expand existing entries with additional pathophysiology, phenotypes, or treatments
- Add ontology term bindings (HPO, GO, MAXO, etc.)
- Fix validation errors and label mismatches

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

## Pull Request Process

1. Create a branch for your changes
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
