# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Alzheimer Disease
- **Category:** Neurodegenerative Disorder

## Target Hypothesis
- **Hypothesis ID:** tau_neurodegeneration_model
- **Hypothesis Label:** Tau Neurodegeneration Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: tau_neurodegeneration_model
hypothesis_label: Tau Neurodegeneration Model
status: CANONICAL
description: Tau hyperphosphorylation and aggregation into neurofibrillary tangles are modeled as proximate
  drivers of neuronal dysfunction, microtubule disruption, neurodegeneration, and clinical progression.
applies_to_subtypes:
- Early-Onset Alzheimer's Disease
- Late-Onset Alzheimer's Disease
evidence:
- reference: PMID:21509508
  reference_title: 'Tau mediated neurodegeneration: an insight into Alzheimer''s disease pathology.'
  supports: SUPPORT
  snippet: Extracellular accumulations of Abeta, hyperphosphorylation of tau and intracellular neurofibrillary
    tangle formation have been the hallmarks of Alzheimer's Disease (AD).
  explanation: Supports tau hyperphosphorylation and tangle formation as central Alzheimer disease pathology.
- reference: PMID:19542604
  reference_title: The microtubule-associated protein tau is also phosphorylated on tyrosine.
  supports: SUPPORT
  snippet: Tau protein is the principal component of the neurofibrillary tangles found in Alzheimer's
    disease (AD), where it is hyperphosphorylated on serine and threonine residues.
  explanation: Identifies hyperphosphorylated tau as the principal neurofibrillary tangle component in
    Alzheimer disease.
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
**Generated:** 2026-05-18T21:45:56.028675

1. PMID:41770504
2. PMID:41465514
3. PMID:41532780
4. PMID:39868491
5. PMID:38542104
6. PMID:40883301
7. PMID:30742061
8. PMID:33895632
9. PMID:35985329
10. PMID:38554150
11. PMID:38012285
12. PMID:36730056
13. PMID:35696185
14. PMID:37643887
15. PMID:38101301
16. PMID:39887500
17. PMID:41695614
18. PMID:31456657
19. PMID:39211286
20. PMID:40234685
21. PMID:31277708
22. PMID:35534858
23. PMID:41745721
24. PMID:41569436
25. PMID:41904008
26. PMID:19071093
27. PMID:22049418
28. PMID:11441005
29. PMID:24713000
30. PMID:23922015
31. PMID:40734174
32. PMID:31362787
33. PMID:41890022
34. PMID:41759740
35. PMID:34738197
36. PMID:22621232
37. PMID:41291371
38. PMID:41823685
