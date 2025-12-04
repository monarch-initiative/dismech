# Contributing to dismech

Thank you for your interest in contributing to the Disorder Mechanisms Knowledge Base!

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

Human curators are welcome! To understand the curation guidelines:

1. **Read `CLAUDE.md`** - Contains the same instructions AI agents follow
2. **Review `.claude/skills/`** - Detailed guidelines for term and reference validation
3. **Run QC locally** before submitting PRs:
   ```bash
   just qc
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
