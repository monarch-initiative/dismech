# Disorder Mechanisms Knowledge Base (dismech)

A curated knowledge base of disease pathophysiology, with structured evidence from the literature.

## Browse the Knowledge Base

**[View all disorders online](https://dismech.monarchinitiative.org/app/)** | **[QC Dashboard](https://dismech.monarchinitiative.org/dashboard/)**

Each disorder page includes:
- Disease mechanisms and pathophysiology
- Clinical phenotypes with HPO term links
- Genetic factors and variants
- Treatment options with MAXO term links
- All claims backed by PubMed evidence

## How It Works

### Project Overview Slides

- [Dismech presentation slides from February 2026](https://docs.google.com/presentation/d/1XrbLle8gVQQcoT8IzpIfll4VnUl_68mQVTa6cIzN2vs/edit?usp=sharing)

### Source of Truth: YAML Files

The knowledge base is stored as structured YAML files in `kb/disorders/`. Each disorder has its own file (e.g., `Asthma.yaml`) containing:

```yaml
name: Asthma
pathophysiology:
  - name: Airway Inflammation
    description: Chronic inflammation of the airways
    biological_processes:
      - preferred_term: inflammatory response
        term:
          id: GO:0006954
          label: inflammatory response
    evidence:
      - reference: PMID:12345678
        supports: SUPPORT
        snippet: "Exact quote from the paper"
        explanation: "Why this supports the claim"
phenotypes:
  - name: Wheezing
    frequency: FREQUENT
    phenotype_term:
      preferred_term: Wheezing
      term:
        id: HP:0030828
        label: Wheezing
treatments:
  - name: Bronchodilators
    description: Relax airway smooth muscle
    treatment_term:
      preferred_term: respiratory tract agent therapy
      term:
        id: MAXO:0000312
        label: respiratory tract agent therapy
```

### Ontology Bindings

Entities are linked to authoritative ontologies:
- **Phenotypes**: Human Phenotype Ontology (HP)
- **Cell types**: Cell Ontology (CL)
- **Biological processes**: Gene Ontology (GO)
- **Diseases**: Mondo Disease Ontology (MONDO)
- **Treatments**: Medical Action Ontology (MAXO)
- **Anatomy**: Uberon (UBERON)

### Evidence Requirements

All claims must cite PubMed references with exact quotes. This prevents misinformation and enables verification.

### Validation Pipeline

Multiple layers of automated validation ensure data quality and prevent AI hallucinations:

1. **Schema validation**: Ensures correct YAML structure against the LinkML schema
2. **Ontology term validation**: Verifies term IDs exist and labels match authoritative sources (HPO, MONDO, GO, etc.)
3. **Reference validation**: Confirms that quoted snippets actually appear in cited PubMed abstracts
4. **Compliance analysis**: Measures coverage of recommended fields (descriptions, evidence, ontology terms)

```bash
# Run schema + term validation
just qc

# Validate a single file
just validate kb/disorders/Asthma.yaml

# Validate references against PubMed abstracts
just validate-references kb/disorders/Asthma.yaml

# Analyze compliance with recommended field coverage
just compliance-all

# Compliance with weighted scoring and threshold checks
just compliance-weighted
```

### Why Reference Validation Matters

All evidence snippets must be **exact quotes** from paper abstracts, not paraphrases. The reference validator fetches abstracts from PubMed and checks that the quoted text appears verbatim. This catches:

- AI-generated paraphrases that don't match the actual paper
- Wrong PMIDs (e.g., a PMID that points to an unrelated paper)
- Fabricated citations

When validation fails, either fix the snippet to match the actual abstract or remove the evidence item.

### QC Dashboard

Generate a visual dashboard showing compliance metrics across all disorder files:

```bash
just gen-dashboard
```

This creates `dashboard/index.html` with:
- Summary metrics (files analyzed, average compliance, violations)
- Slot compliance comparison chart
- Detailed views of the 10 lowest-compliance files (priority curation targets)
- Full table of all files sorted by compliance
- A dedicated `not_yet_curated.html` report listing referenced MONDO diseases that do not yet have local DisMech pages

View online: [QC Dashboard](https://dismech.monarchinitiative.org/dashboard/) or locally: `open dashboard/index.html`

### HTML Generation

YAML files are rendered to browsable HTML pages with clickable ontology term links.

```bash
uv run python -m dismech.render --all
```

### CX2 Export For NDEx

Disorder pathographs can also be exported as CX2 networks for publication to NDEx.

```bash
# Write CX2 JSON to a file
uv run dismech-cx2 kb/disorders/Stargardt_Disease.yaml -o Stargardt_Disease.cx2.json

# Same flow via justfile target
just export-cx2 kb/disorders/Stargardt_Disease.yaml -o Stargardt_Disease.cx2.json

# Export all disorders to a directory, skipping those with no pathograph edges
just export-cx2-all -o /tmp/cx2

# Upload directly to NDEx using env vars
export NDEX_USERNAME=...
export NDEX_PASSWORD=...
uv run dismech-cx2 kb/disorders/Stargardt_Disease.yaml --ndex-upload

# Bulk upload all disorders to the NDEx test server
export NDEX_USERNAME=...
export NDEX_PASSWORD=...
just upload-cx2-test-all
```

`dismech-cx2` uses the existing pathograph graph model, preserves node and edge metadata,
and applies a deterministic layout so the uploaded network is immediately viewable in
NDEx. Add `--dot-layout` if Graphviz and `pydot` are available and you want a Graphviz
layout instead of the built-in layered layout. The default NDEx upload visibility is
`PUBLIC`, and the `just` upload targets default the host to `https://test.ndexbio.org`.

## Agentic Curation Guide

This knowledge base is curated with **Claude Code** — an AI agent that knows the schema, validates ontology terms, and checks evidence against PubMed abstracts. There are two ways to start curating:

### Route 1: Clone the repo and use Claude Code CLI

Best for power users who want full control, deep research providers, and iterative curation sessions.

**Prerequisites:** A Claude Pro/Max subscription and `just` installed ([installation](https://github.com/casey/just#installation)).

```bash
# 1. Clone and enter the repo
git clone https://github.com/monarch-initiative/dismech.git
cd dismech

# 2. Launch Claude Code
claude

# 3. Ask it anything — or run a curation skill directly
> Give me a tour of the dismech project
> What disorders are missing ontology terms?
> /curate Parkinson Disease
```

The `/curate` command triggers a full curation workflow: deep literature research, YAML generation, ontology term binding, evidence validation, and a ready-to-review PR.

You can also ask the agent open-ended questions, request targeted edits, or run QC:

```
> Add MAXO treatment terms to the Asthma entry
> Validate references in kb/disorders/Lupus.yaml
> Which files have the lowest compliance scores?
```

**Optional — deep research providers:**

For narrative-style deep research, set up an [Edison Scientific](https://platform.edisonscientific.com/) API key:
```bash
export EDISON_API_KEY=your_key_here
```

For literature-search-style retrieval via Asta, request an API key from [Allen AI Asta](https://allenai.org/asta/resources/mcp) and export:
```bash
export ASTA_API_KEY=your_key_here
```

Then run:
```bash
just research-disorder asta Liver_Cirrhosis
```

Asta outputs are typically literature packets rather than polished narrative reports:
they prioritize relevant papers, summaries, snippets, and metadata such as PMID/DOI.

### Route 2: Use Claude Code on the web

Best for quick contributions — no local setup required.

1. Go to **[claude.ai/code](https://claude.ai/code)**
2. Open the `monarch-initiative/dismech` repository
3. **Set up an environment** with the following settings:
   - **Allow access to external websites** — needed for fetching PubMed abstracts, ClinicalTrials.gov data, and ontology lookups
   - **Set `EDISON_API_KEY`** — for deep literature research via [Edison Scientific](https://platform.edisonscientific.com/) (sign up → Account → Profile → Create new token)
4. Interact with the agent in the web UI — ask questions, request edits, or run `/curate`
5. When you're done, click the **Create pull request** button to submit your changes for review

That's it. The web UI handles git branching, commits, and PR creation automatically.

### What happens during curation

Regardless of which route you use, the agent follows the same workflow:

1. **Research** — gathers pathophysiology, phenotypes, treatments, and genetic factors from the literature
2. **Draft** — generates a structured YAML file with ontology term bindings and PubMed-backed evidence
3. **Validate** — runs schema validation, ontology term checks, and reference verification (`just qc`)
4. **Submit** — commits changes and opens a pull request for human review

For detailed contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Schema Documentation

- [LinkML Schema Docs](https://dismech.monarchinitiative.org/elements/)
- Schema source: `src/dismech/schema/dismech.yaml`
