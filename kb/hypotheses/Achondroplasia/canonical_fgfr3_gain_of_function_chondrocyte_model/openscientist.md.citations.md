# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Achondroplasia
- **Category:** Mendelian

## Target Hypothesis
- **Hypothesis ID:** canonical_fgfr3_gain_of_function_chondrocyte_model
- **Hypothesis Label:** Canonical FGFR3 Gain-of-Function Chondrocyte Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_fgfr3_gain_of_function_chondrocyte_model
hypothesis_label: Canonical FGFR3 Gain-of-Function Chondrocyte Model
status: CANONICAL
description: A recurrent heterozygous activating mutation in FGFR3 (most commonly G380R) produces a constitutively
  active fibroblast growth factor receptor 3 that hyperactivates STAT1, MAPK/ERK, and p38 MAPK signaling
  in growth-plate chondrocytes. The resulting inhibition of chondrocyte proliferation and accelerated
  terminal differentiation impair endochondral ossification, producing rhizomelic short stature, macrocephaly
  with frontal bossing, midface hypoplasia, foramen magnum stenosis, and characteristic trident hand.
  C-type natriuretic peptide analogues (vosoritide) that antagonize downstream MAPK signaling directly
  validate the FGFR3-signaling axis as the pathogenic driver.
evidence:
- reference: PMID:7913883
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: DNA studies revealed point mutations in the FGFR3 gene in ACH
  explanation: |
    Canonical mechanism review used as the seed reference for the hypothesis-search deep-research run.
```

## Research Objective

Build a focused hypothesis-search report that answers:

1. What is the strongest direct evidence for this hypothesis?
2. What evidence argues against it, fails to reproduce it, or limits its scope?
3. Which claims are established, emerging, speculative, or contradicted?
4. Which patient subtypes, stages, tissues, cell types, molecular pathways, or
   biomarkers does the hypothesis best explain?
5. Which alternative or competing mechanistic hypotheses explain the same disease
   features better or more parsimoniously?
6. What are the explicit knowledge gaps: missing causal steps, unconfirmed edges,
   contradictory evidence, unknown source-to-target links, or source/data absences?
7. What experiments, cohorts, assays, datasets, or trials would most directly
   distinguish this hypothesis from alternatives?

Use primary literature whenever possible. Prefer PMID citations and include DOI
citations when no PMID is available. Treat reviews as orientation unless they
contain directly relevant synthesized evidence that should be clearly labeled as
review-level support.

## Required Output

### Executive Judgment

Give a concise verdict on the hypothesis as of the current literature:
supported, partially supported, unresolved, weakly supported, or refuted. Explain
the reasoning and the most important caveats.

### Evidence Matrix

Create a table with one row per important evidence item:

- Citation (PMID preferred)
- Evidence type (human clinical, model organism, in vitro, computational, review)
- Supports / refutes / qualifies / competing
- Mechanistic claim tested
- Key finding
- Disease subtype or context
- Confidence and limitations

### Mechanistic Causal Chain

Describe the causal chain implied by the hypothesis from upstream trigger to
clinical manifestation. Identify where the literature is strong, where the links
are inferred, and where there are missing causal steps.

### Knowledge Gaps

Identify explicit known unknowns surfaced by the search. Treat absence of
evidence as a curation-relevant finding only when the search actually checked for
it. Include:

- Unknown or weakly supported causal steps in the hypothesis
- Unconfirmed causal graph edges that need direct perturbation or longitudinal
  evidence
- Conflicting evidence, failed replications, or incompatible subtype-specific
  findings
- Unknown mechanism of action for relevant treatments, biomarkers, or
  interventions tied to this hypothesis
- Source-level or dataset-level absences, such as no relevant GenCC, ClinGen,
  trial, omics, or cohort evidence found as of the search date

For each gap, state the scope, why it matters, what was checked, and what
evidence or experiment would resolve it.

### Alternative Models

List competing or complementary hypotheses. For each, explain whether it is an
alternative to the seed hypothesis, a downstream consequence, an upstream cause,
or a parallel mechanism.

### Discriminating Tests

Recommend concrete studies or assays that would most efficiently test this
hypothesis against alternatives. Include patient stratification, biomarkers,
sample type, model system, perturbation, and expected result where applicable.

### Curation Leads

Provide candidate updates for the KB, but label these as leads requiring curator
verification. Include:

- candidate evidence references and exact abstract snippets to verify
- candidate pathophysiology nodes or edges
- candidate ontology terms for cell types and biological processes
- candidate subtype restrictions or status changes
- candidate `knowledge_gaps` or discussion prompts for unresolved causal claims,
  conflicting evidence, or explicit source/data absences

If the provider supports artifacts, produce artifact-friendly outputs such as an
evidence matrix, mechanistic diagram, knowledge-gap table, or comparison table.
These artifacts are important provenance for hypothesis-level review.

**Provider:** openscientist
**Generated:** 2026-05-23T16:17:13.173615

1. PMID:20624921
2. PMID:10611230
3. PMID:11742142
4. PMID:28230213
5. PMID:41121704
6. PMID:14702637
7. PMID:14751560
8. PMID:27064282
9. PMID:39674288
10. PMID:34341520
11. PMID:34431071
12. PMID:35698202
13. PMID:29360984
14. PMID:29040558
15. PMID:41954527
16. PMID:41748604
17. PMID:41091812
18. PMID:40373614
19. PMID:23740942
20. PMID:27070266
21. PMID:37568254
22. PMID:38397181
23. PMID:7913883
24. PMID:28583899
25. PMID:33370388
26. PMID:48048522
27. PMID:38590263
28. PMID:35078974
29. PMID:30685387
