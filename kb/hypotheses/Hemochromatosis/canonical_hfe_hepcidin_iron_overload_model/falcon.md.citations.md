# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Hemochromatosis
- **Category:** Mendelian

## Target Hypothesis
- **Hypothesis ID:** canonical_hfe_hepcidin_iron_overload_model
- **Hypothesis Label:** Canonical HFE / Hepcidin / Systemic Iron Overload Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_hfe_hepcidin_iron_overload_model
hypothesis_label: Canonical HFE / Hepcidin / Systemic Iron Overload Model
status: CANONICAL
description: Hereditary hemochromatosis (HH), most commonly HFE-related (C282Y homozygotes), arises from
  inappropriately low hepatic hepcidin expression relative to body iron stores. Hepcidin is the master
  regulator of systemic iron homeostasis, binding ferroportin on enterocytes and macrophages and causing
  its internalization and degradation, thereby restricting duodenal iron absorption and reticuloendothelial
  iron release. Loss-of-function variants in HFE, HJV, TfR2, and HAMP all converge on a final common pathway
  of relative hepcidin deficiency, leading to chronic increased duodenal iron absorption, transferrin
  saturation, and progressive non-transferrin-bound iron accumulation in hepatocytes, cardiomyocytes,
  pancreatic β-cells, and endocrine tissues. Tissue iron toxicity produces cirrhosis, hepatocellular carcinoma,
  cardiomyopathy, diabetes, hypogonadism, and arthropathy. Therapeutic phlebotomy and investigational
  hepcidin agonists / ferroportin inhibitors all corroborate the hepcidin-deficient-iron-overload axis
  as the canonical pathogenic mechanism.
evidence:
- reference: PMID:23985001
  reference_title: Hereditary hemochromatosis.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Hereditary hemochromatosis is an inherited iron overload disorder caused by inappropriately
    low hepcidin secretion leading to increased duodenal absorption of dietary iron
  explanation: |
    Canonical mechanism reference used as the seed for the hypothesis-search deep-research run.
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

**Provider:** falcon
**Generated:** 2026-05-24T00:09:08.371099

1. girelli2024diagnosisandmanagement pages 1-2
2. marcon2024tsaturatedinsightsclarifying pages 2-4
3. modi2024pharmacokineticsandpharmacodynamics pages 1-2
4. crawford2023clinicalpracticeguidelines pages 5-6
5. turshudzhyan2023primarynonhfehemochromatosis pages 1-2
6. sgro2024hemojuvelindeficiencydoes pages 42-47
7. girelli2024diagnosisandmanagement pages 2-4
8. pilo2024vamifeportmonographyof pages 9-9
9. crawford2023clinicalpracticeguidelines pages 1-3
10. crawford2023clinicalpracticeguidelines pages 3-5
11. crawford2023clinicalpracticeguidelines pages 6-7
12. infanti2024blooddonationfor pages 1-2
13. infanti2024blooddonationfor pages 5-7
14. barton2023nonalcoholicfattyliver pages 1-2
15. barton2023nonalcoholicfattyliver pages 4-5
16. sgro2024hemojuvelindeficiencydoes pages 22-27
17. sgro2024hemojuvelindeficiencydoes pages 47-48
18. modi2024pharmacokineticsandpharmacodynamics pages 14-14
19. infanti2024blooddonationfor pages 7-9
20. barton2023nonalcoholicfattyliver pages 2-4
21. castro2024ironrestrictionin pages 6-6
22. infanti2024blooddonationfor pages 4-5
23. infanti2024blooddonationfor pages 3-4
24. https://doi.org/10.1186/s13023-024-03439-9
25. https://doi.org/10.1007/s40268-024-00497-z
26. https://doi.org/10.1371/journal.pbio.3001936
27. https://doi.org/10.1007/s12072-023-10510-3
28. https://doi.org/10.3389/fmed.2024.1362941
29. https://clinicaltrials.gov/study/NCT04202965
30. https://doi.org/10.1182/hematology.2024000568
31. https://doi.org/10.1186/s12876-023-02763-x
32. https://doi.org/10.3390/hemato5040035
33. https://doi.org/10.14218/jcth.2022.00373
34. https://doi.org/10.3390/jcm13185524
35. https://doi.org/10.1182/hematology.2024000568,
36. https://doi.org/10.3390/hemato5040035,
37. https://doi.org/10.1007/s12072-023-10510-3,
38. https://doi.org/10.1007/s40268-024-00497-z,
39. https://doi.org/10.14218/jcth.2022.00373,
40. https://doi.org/10.1186/s13023-024-03439-9,
41. https://doi.org/10.1371/journal.pbio.3001936,
42. https://doi.org/10.3389/fmed.2024.1362941,
43. https://doi.org/10.1186/s12876-023-02763-x,
44. https://doi.org/10.3390/jcm13185524,
45. https://doi.org/10.1002/ajh.27267,
