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
- **Hypothesis ID:** canonical_atp7b_copper_retention
- **Hypothesis Label:** Canonical ATP7B Copper-Retention Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_atp7b_copper_retention
hypothesis_label: Canonical ATP7B Copper-Retention Model
status: CANONICAL
description: |
  ATP7B loss impairs biliary copper excretion and ceruloplasmin loading, causing hepatic copper retention with secondary extrahepatic toxicity.
evidence:
- reference: PMID:12426114
  reference_title: Molecular mechanism of copper transport in Wilson disease.
  supports: SUPPORT
  snippet: The Wilson disease protein is a putative copper-transporting P-type ATPase, ATP7B, whose malfunction
    results in the toxic accumulation of copper in the liver and brain, causing the hepatic and/or neurological
    symptoms accompanying this disease.
  explanation: Supports ATP7B dysfunction as the core mechanism that links copper retention to hepatic
    and neurologic disease.
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
**Generated:** 2026-05-17T20:07:41.877815

1. PMID:11961729
2. PMID:11273771
3. PMID:17889170
4. PMID:39535360
5. PMID:37968102
6. PMID:41480142
7. PMID:21645498
8. PMID:32532207
9. PMID:38552405
10. PMID:24517502
11. PMID:30230192
12. PMID:29059476
13. PMID:10982773
14. PMID:14998371
15. PMID:16554302
16. PMID:19937698
17. PMID:41230834
18. PMID:41944514
19. PMID:39322449
20. PMID:34620762
21. PMID:39674827
22. PMID:24356057
23. PMID:16606763
24. PMID:22629446
25. PMID:19595438
26. PMID:39233127
27. PMID:29482344
28. PMID:38830145
29. PMID:17919502
30. PMID:38081365
31. PMID:41566726
32. PMID:41637185
33. PMID:34831341
34. PMID:41780554
35. PMID:27935710
36. PMID:15865413
37. PMID:34098115
38. PMID:40980162
39. PMID:12426114
