# MC4R Pathway Obesity Curation Project

## Overview

Create a mechanism-centered dismech entry for obesity caused by disruption of the
leptin-melanocortin-4 receptor pathway. The scope includes:

- acquired hypothalamic obesity
- congenital hypothalamic obesity
- syndromic obesity converging on MC4R signaling
- rare monogenic obesity involving LEP, LEPR, POMC, PCSK1, MC4R, SH2B1, and NCOA1

## Modeling Choice

Use one umbrella disorder entry, `Obesity_Due_to_MC4R_Pathway_Disruption.yaml`,
with `has_subtypes` to represent the major presentations and gene-defined
monogenic forms. This follows the repo's spectrum-style pattern for disorders
with a shared proximal mechanism and clinically important internal heterogeneity.

Do not create separate top-level disorder YAML files for each monogenic gene in
this pass.

## Expected Outputs

- `kb/disorders/Obesity_Due_to_MC4R_Pathway_Disruption.yaml`
- `research/Obesity_Due_to_MC4R_Pathway_Disruption-deep-research-*.md`
- `research/Obesity_Due_to_MC4R_Pathway_Disruption-deep-research-*.md.citations.md`
- `references_cache/*` for new PMIDs

## Workflow

1. Create initial stub disorder entry.
2. Run deep research on the new disorder slug.
3. Curate mechanism, phenotypes, genetics, and treatments with PMID-backed evidence.
4. Validate schema, terms, references, and compliance.
5. Commit, push, and open a PR.

---

# STATUS

- [x] Initial stub created
- [x] Deep research completed
- [x] YAML curated with evidence
- [x] Validation passed
- [ ] Commit pushed
- [ ] PR opened

# NOTES

- Local MONDO search in this worktree surfaced `MONDO:0019182 inherited obesity`
  for monogenic obesity but not a single exact term covering the full umbrella
  of acquired, congenital hypothalamic, syndromic, and monogenic MC4R-pathway
  disruption. The entry is therefore seeded with the broader `obesity disorder`
  MONDO term and a more specific preferred term.
- Deep research completed with the `asta` provider in
  `research/Obesity_Due_to_MC4R_Pathway_Disruption-deep-research-asta.md`.
