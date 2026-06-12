# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Bipolar Disorder
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** canonical_polygenic_synaptic_circadian_dysregulation_model
- **Hypothesis Label:** Canonical Polygenic / Synaptic / Circadian Dysregulation Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_polygenic_synaptic_circadian_dysregulation_model
hypothesis_label: Canonical Polygenic / Synaptic / Circadian Dysregulation Model
status: CANONICAL
description: Bipolar disorder is a highly heritable polygenic mood disorder in which common variants in
  CACNA1C, ANK3, ODZ4, and other ion-channel and synaptic genes combine with circadian/clock gene variants
  (CLOCK, BMAL1, NR1D1) to produce episodic mood instability. Mitochondrial dysfunction, calcium- signaling
  dysregulation, and altered neuroplasticity in fronto-limbic circuits (anterior cingulate, amygdala,
  ventral striatum) drive cycling between depressive and manic states. Lithium's mood- stabilizing efficacy
  (targeting GSK-3β / inositol monophosphatase / circadian amplitude), valproate's modulation of histone
  deacetylases, and the recurrent involvement of the dopaminergic reward system during manic episodes
  corroborate the polygenic-synaptic-circadian framework as the canonical model.
evidence:
- reference: PMID:21057379
  reference_title: Voltage-dependent calcium channels in bipolar disorder and schizophrenia
  supports: SUPPORT
  evidence_source: OTHER
  snippet: The finding for CACNG5, taken together with the earlier implication of CACNA1C and CACNA1B,
    strongly suggests a key role for voltage-dependent calcium channel genes in the susceptibility to
    bipolar disorder and/or schizophrenia.
  explanation: |
    Existing canonical mechanism citation in the dismech knowledge base, used as the seed for the hypothesis-search deep-research run.
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
**Generated:** 2026-05-24T15:55:47.427164

1. PMID:33442739
2. PMID:9790159
3. PMID:38395906
4. PMID:24716566
5. PMID:32646651
6. PMID:25403839
7. PMID:34002096
8. PMID:26524527
9. PMID:20591414
10. PMID:16143731
11. PMID:37306960
12. PMID:35101157
13. PMID:39370418
14. PMID:10418700
15. PMID:21167476
16. PMID:28093238
17. PMID:35410376
18. PMID:32404948
19. PMID:27003509
20. PMID:22981886
21. PMID:16179524
22. PMID:11252650
23. PMID:17696880
24. PMID:17451429
25. PMID:41672966
26. PMID:36322065
27. PMID:27226262
28. PMID:41421618
29. PMID:34375219
30. PMID:31917880
31. PMID:24677591
32. PMID:25807948
33. PMID:36969554
34. PMID:40253403
35. PMID:41313566
36. PMID:23820096
37. PMID:34320487
38. PMID:25954495
39. PMID:28483660
40. PMID:25487697
41. PMID:31249382
42. PMID:29414032
43. PMID:21074545
44. PMID:37711124
45. PMID:41429665
46. PMID:33673277
47. PMID:30051546
48. PMID:34531727
49. PMID:30201969
