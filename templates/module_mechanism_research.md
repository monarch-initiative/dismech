# Mechanism Module Research Template

## Target Module
- **Module Name:** {module_name}
- **Module Slug:** {module_slug}
- **Category:** {category}

## Current Module Description

{module_description}

## Current Provisional Nodes

{pathophysiology_summary}

## Research Objective

Prepare a mechanism-focused research report for the dismech module above. This
is not a disease entry. The goal is to support a reusable mechanism module that
multiple gene-axis disease entries can conform to.

Focus the search on the shared biology of meiotic prophase I failure leading to
gametogenic failure. Prioritize evidence for:

- The conserved causal chain: meiotic prophase entry, homolog pairing,
  synaptonemal complex assembly, meiotic homologous-recombination repair,
  pachytene checkpoint arrest, germ-cell apoptosis, and sex-dimorphic outcomes.
- The boundary between synaptonemal complex structural genes and homologous
  recombination / DNA-repair genes.
- Gene-specific branches for MCM8 and MCM9 somatic DNA repair and cancer
  predisposition, while distinguishing these from the core meiotic module.
- Explicit exclusions: gonadal organogenesis and steroidogenesis transcription
  factor disorders such as NR5A1, WT1, SOX9, SRY, FOXL2, and DHH.

## Key Genes In Scope

SYCE1, MCM8, MCM9, STAG3, HFM1, MSH4, MSH5, DMC1, SYCP3.

## Questions To Answer

1. What is the best-supported shared mechanism across these genes?
2. Should the module be named `meiotic_prophase_failure`,
   `meiotic_recombination_failure`, or something else?
3. Which nodes should be core and required for conformance, and which nodes
   should be optional or gene-specific?
4. Which genes support the synaptonemal-complex branch, the homologous
   recombination branch, and the somatic DNA-repair/cancer branch?
5. What evidence supports pachytene checkpoint arrest and apoptosis as the
   shared terminal mechanism in both 46,XX and 46,XY presentations?
6. What direct human evidence links the same gene or variant class to both
   primary ovarian insufficiency and non-obstructive azoospermia?
7. What model organism evidence clarifies the causal path from meiotic defect
   to germ-cell loss?
8. What Gene Ontology biological process terms, Cell Ontology cell types, and
   anatomical terms should be used in the module?
9. What claims are speculative, weakly supported, or should remain out of scope?

## Evidence Requirements

- Cite primary literature with PMID identifiers whenever possible.
- Include exact abstract quotes for candidate evidence snippets.
- Separate human clinical, model organism, in vitro, and review evidence.
- Flag papers where the abstract is insufficient and full-text verification is
  needed before curation.
- Do not invent ontology IDs. Suggest terms by label when unsure.

## Desired Output

Structure the report with:

- Executive recommendation for module name and scope.
- Proposed DAG nodes and causal edges.
- Gene-to-node mapping table.
- Evidence table with PMID, evidence type, exact quote, and supported claim.
- Ontology suggestions for GO, CL, and UBERON terms.
- Out-of-scope boundary notes.
- Open questions for curator review.
