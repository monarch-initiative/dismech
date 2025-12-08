# Disorder Mechanisms Knowledge Base (dismech)

A curated knowledge base of disease pathophysiology, with structured evidence from the literature.

## Browse the Knowledge Base

**[View all disorders online](https://monarch-initiative.github.io/dismech/disorders/)** | **[QC Dashboard](https://monarch-initiative.github.io/dismech/dashboard/)**

Each disorder page includes:
- Disease mechanisms and pathophysiology
- Clinical phenotypes with HPO term links
- Genetic factors and variants
- Treatment options with MAXO term links
- All claims backed by PubMed evidence

## How It Works

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

View online: [QC Dashboard](https://monarch-initiative.github.io/dismech/dashboard/) or locally: `open dashboard/index.html`

### HTML Generation

YAML files are rendered to browsable HTML pages with clickable ontology term links.

```bash
uv run python -m dismech.render --all
```

## For Curators

See [CONTRIBUTING.md](CONTRIBUTING.md) for curation guidelines.

## Schema Documentation

- [LinkML Schema Docs](https://monarch-initiative.github.io/dismech)
- Schema source: `src/dismech/schema/dismech.yaml`
