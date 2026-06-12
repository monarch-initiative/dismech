# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Friedreich Ataxia
- **Category:** Mendelian

## Target Hypothesis
- **Hypothesis ID:** canonical_fxn_loss_of_function
- **Hypothesis Label:** Canonical FXN Loss-of-Function Mitochondrial Pathograph
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_fxn_loss_of_function
hypothesis_label: Canonical FXN Loss-of-Function Mitochondrial Pathograph
status: CANONICAL
description: |
  Biallelic FXN intron 1 GAA repeat expansion causes epigenetic transcriptional silencing and frataxin deficiency. Frataxin deficiency impairs mitochondrial Fe-S cluster biogenesis, oxidative phosphorylation, and iron handling, creating tissue-selective vulnerability in dorsal root ganglion sensory neurons, dentate/spinal pathways, cardiomyocytes, pancreatic beta cells, and the skeleton.
evidence:
- reference: PMID:21315377
  reference_title: 'Friedreich''s ataxia: pathology, pathogenesis, and molecular genetics.'
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Deficiency of frataxin, a small mitochondrial protein, is responsible for all clinical and
    morphological manifestations of FRDA.
  explanation: Establishes frataxin deficiency as the common causal mechanism underlying the multisystem
    FRDA phenotype.
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
**Generated:** 2026-05-23T02:40:42.620302

1. PMID:42157962
2. PMID:31511419
3. PMID:24971490
4. PMID:21776984
5. PMID:26401053
6. PMID:26896803
7. PMID:22522441
8. PMID:42127908
9. PMID:39243573
10. PMID:41579709
11. PMID:40308559
12. PMID:23334592
13. PMID:14985441
14. PMID:28912677
15. PMID:30761510
16. PMID:41628678
17. PMID:23169664
18. PMID:39632806
19. PMID:41372413
20. PMID:42150975
21. PMID:31031004
22. PMID:25112865
23. PMID:33209958
24. PMID:40498047
25. PMID:22379112
26. PMID:38631900
27. PMID:29261783
28. PMID:27572719
29. PMID:22513953
30. PMID:36798283
31. PMID:31417369
