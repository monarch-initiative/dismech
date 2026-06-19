# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Glutaryl-CoA Dehydrogenase Deficiency
- **Category:** Mendelian

## Target Hypothesis
- **Hypothesis ID:** canonical_ga1_metabolic_model
- **Hypothesis Label:** Canonical GCDH Deficiency-Toxic Metabolite Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_ga1_metabolic_model
hypothesis_label: Canonical GCDH Deficiency-Toxic Metabolite Model
status: CANONICAL
description: Biallelic GCDH loss of function impairs lysine catabolism, resulting in accumulation of neurotoxic
  metabolites (GA, 3-OH-GA, C5DC) that drive striatal injury and dystonia, particularly during catabolic
  stress.
evidence:
- reference: PMID:37685964
  reference_title: Glutaryl-CoA Dehydrogenase Misfolding in Glutaric Acidemia Type 1.
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: Glutaric acidemia type 1 (GA1) is a neurotoxic metabolic disorder due to glutaryl-CoA dehydrogenase
    (GCDH) deficiency.
  explanation: Establishes the canonical disease mechanism linking GCDH deficiency to neurotoxic metabolic
    pathology.
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
**Generated:** 2026-05-23T05:45:42.817249

1. barroso2023glutarylcoadehydrogenasemisfolding pages 1-2
2. biagosch2017elevatedglutaricacid pages 1-6
3. sauer2011therapeuticmodulationof pages 1-2
4. mateubosch2024systemicdeliveryof pages 6-7
5. gragnaniello2025diagnosisofglutaric pages 2-5
6. zaunseder2024digitaltierstrategyimproves pages 1-2
7. zaunseder2024digitaltierstrategyimproves pages 8-10
8. gragnaniello2025diagnosisofglutaric pages 1-2
9. mateubosch2024systemicdeliveryof pages 7-9
10. kolker2004excitotoxicityandbioenergetics pages 3-6
11. mateubosch2024systemicdeliveryof pages 1-2
12. saad2026aminoadipatesemialdehydesynthasea pages 1-6
13. oliverabravo2015striatalneuronaldeath pages 10-11
14. oliverabravo2015striatalneuronaldeath pages 5-7
15. oliverabravo2015striatalneuronaldeath pages 8-10
16. kolker2004excitotoxicityandbioenergetics pages 1-3
17. GA
18. 3‑OH‑GA
19. https://doi.org/10.3390/ijms241713158
20. https://doi.org/10.1016/j.omtm.2024.101276
21. https://doi.org/10.1002/jimd.12276
22. https://doi.org/10.1093/hmg/ddv175
23. https://doi.org/10.3390/ijns10040083
24. https://doi.org/10.1186/s13052-025-01975-z
25. https://doi.org/10.1016/j.bbadis.2017.05.018
26. https://doi.org/10.1093/brain/awq269
27. https://doi.org/10.1016/j.omtm.2024.101276,
28. https://doi.org/10.1186/s13052-025-01975-z,
29. https://doi.org/10.3390/ijns10040083,
30. https://doi.org/10.1023/b:boli.0000045762.37248.28,
31. https://doi.org/10.3390/ijms241713158,
32. https://doi.org/10.1002/jimd.12276,
33. https://doi.org/10.1038/s41598-026-44377-9,
34. https://doi.org/10.1093/hmg/ddv175,
35. https://doi.org/10.1016/j.bbadis.2017.05.018,
36. https://doi.org/10.1093/brain/awq269,
