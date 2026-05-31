# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Long COVID
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** autoimmune_model
- **Hypothesis Label:** Autoimmunity and B-cell Dysregulation Model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: autoimmune_model
hypothesis_label: Autoimmunity and B-cell Dysregulation Model
status: EMERGING
description: |
  SARS-CoV-2 triggers de novo autoantibody production through B-cell dysregulation, molecular mimicry, and bystander activation, contributing to multisystem symptoms and immune-mediated tissue damage in Long COVID.
applies_to_subtypes:
- Pain-dominant long COVID phenotype
- Cardiopulmonary-dominant long COVID phenotype
evidence:
- reference: PMID:39956285
  reference_title: Autoimmunity in long COVID.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Several studies show preexisting and/or de novo production of autoantibodies after infection
    with SARS-CoV-2, but the persistence of these antibodies and their role in causing long COVID is debated.
  explanation: Supports autoimmunity as an emerging mechanistic hypothesis for Long COVID.
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
**Generated:** 2026-05-23T06:18:35.752371

1. PMID:42053865
2. PMID:37490975
3. PMID:35598178
4. PMID:40915391
5. PMID:39847575
6. PMID:39956285
7. PMID:41259457
8. PMID:36044993
9. PMID:33950285
10. PMID:36471421
11. PMID:36300787
12. PMID:38318183
13. PMID:34242919
14. PMID:40343769
15. PMID:41007425
16. PMID:36182877
17. PMID:38454468
18. PMID:34082475
19. PMID:36715690
20. PMID:35911726
21. PMID:41794369
22. PMID:41287121
23. PMID:41494535
24. PMID:42002663
25. PMID:41518079
26. PMID:40540397
27. PMID:37178769
28. PMID:36015078
29. PMID:32602200
30. PMID:40924481
31. PMID:39154907
32. PMID:39389388
33. PMID:41639746
