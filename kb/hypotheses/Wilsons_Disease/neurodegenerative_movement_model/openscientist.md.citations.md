# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Wilson Disease
- **Category:** Genetic

## Target Hypothesis
- **Hypothesis ID:** neurodegenerative_movement_model
- **Hypothesis Label:** Neurodegenerative Movement Disorder Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: neurodegenerative_movement_model
hypothesis_label: Neurodegenerative Movement Disorder Model
status: CANONICAL
description: |
  Progressive copper-related brain injury in motor control circuits drives dysarthria, dystonia, parkinsonism, and related movement phenotypes.
evidence:
- reference: PMID:28433096
  reference_title: 'Wilson disease: neurologic features.'
  supports: SUPPORT
  snippet: Wilson disease (WD) is a neurodegenerative disorder, which presents as a spectrum of neurologic
    manifestations that includes tremor, bradykinesia, rigidity, dystonia, chorea, dysarthria, and dysphagia
  explanation: Supports neurodegeneration as a major explanatory framework for Wilson disease movement
    phenotypes.
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
**Generated:** 2026-05-17T21:41:24.201902

1. PMID:36165286
2. PMID:31179301
3. PMID:38830145
4. PMID:22720274
5. PMID:26851839
6. PMID:12718440
7. PMID:30341172
8. PMID:39125878
9. PMID:8897491
10. PMID:1333712
11. PMID:33462188
12. PMID:37526174
13. PMID:39322449
14. PMID:41691313
15. PMID:35762218
16. PMID:35114010
17. PMID:36098934
18. PMID:34942565
19. PMID:33078859
20. PMID:19265190
21. PMID:40913012
22. PMID:8208404
23. PMID:1532631
24. PMID:32398357
25. PMID:40513300
26. PMID:34091542
27. PMID:36690883
28. PMID:33590415
29. PMID:41952595
30. PMID:29625923
31. PMID:30249412
32. PMID:35624941
33. PMID:27611852
34. PMID:41275576
35. PMID:35811746
36. PMID:24547944
37. PMID:34289020
