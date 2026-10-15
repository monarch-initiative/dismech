# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Huntington's Disease
- **Category:** Genetic

## Target Hypothesis
- **Hypothesis ID:** canonical_toxic_gain_of_function
- **Hypothesis Label:** Toxic Gain-of-Function (Polyglutamine Aggregation)
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_toxic_gain_of_function
hypothesis_label: Toxic Gain-of-Function (Polyglutamine Aggregation)
status: CANONICAL
description: |
  The expanded polyglutamine tract in mutant huntingtin confers a toxic gain-of-function through protein misfolding, oligomerization, and aggregation into inclusion bodies. This is the widely accepted primary disease mechanism, with polyQ expansion beyond the pathogenic threshold (~36 repeats) driving neurodegeneration predominantly in the striatum.
evidence:
- reference: PMID:22180703
  supports: SUPPORT
  evidence_source: OTHER
  snippet: It is caused by expansion of a polyglutamine tract within the N-terminal domain of the Huntingtin
    protein. The mutation confers a toxic gain-of-function phenotype, resulting in neurodegeneration that
    is most severe in the striatum.
  explanation: Explicitly names the toxic gain-of-function phenotype as the consequence of polyQ expansion
    and links it to striatal neurodegeneration.
- reference: PMID:25336039
  supports: SUPPORT
  evidence_source: OTHER
  snippet: The mutational expansion of polyglutamine beyond a critical length produces a toxic gain of
    function in huntingtin and results in neuronal death. In the course of the disease, expanded huntingtin
    is proteolyzed, becomes abnormally folded, and accumulates in oligomers, fibrils, and microscopic
    inclusions.
  explanation: Directly states the toxic gain-of-function framing and details the aggregation cascade
    from proteolysis through misfolding to inclusion body formation.
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
**Generated:** 2026-05-23T05:23:55.672740

1. PMID:35023827
2. PMID:25336039
3. PMID:29904030
4. PMID:37823007
5. PMID:20190273
6. PMID:18466116
7. PMID:39801710
8. PMID:32898862
9. PMID:39938516
10. PMID:22970194
11. PMID:21897851
12. PMID:23468640
13. PMID:37177784
14. PMID:31203656
15. PMID:22932724
16. PMID:31223078
17. PMID:17041811
18. PMID:16377565
19. PMID:17012230
20. PMID:32681824
21. PMID:18595722
22. PMID:15548548
23. PMID:30239724
24. PMID:19909260
25. PMID:27529325
26. PMID:33172304
27. PMID:41303392
28. PMID:20026656
29. PMID:26106822
30. PMID:31880908
31. PMID:22180703
32. PMID:38393920
33. PMID:24022020
34. PMID:40330856
35. PMID:32463364
36. PMID:33250715
37. PMID:40778304
38. PMID:27514446
39. PMID:31529216
40. PMID:41495356
41. PMID:38861215
42. PMID:42101426
43. PMID:41389205
44. PMID:41841481
