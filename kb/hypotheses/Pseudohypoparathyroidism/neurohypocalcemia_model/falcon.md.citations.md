# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Pseudohypoparathyroidism
- **Category:** Genetic

## Target Hypothesis
- **Hypothesis ID:** neurohypocalcemia_model
- **Hypothesis Label:** Neurohypocalcemia Symptom Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: neurohypocalcemia_model
hypothesis_label: Neurohypocalcemia Symptom Model
status: CANONICAL
description: Neurologic symptoms, including tetany and seizures, arise primarily from downstream hypocalcemia
  and associated mineral imbalance.
applies_to_subtypes:
- PHP1A
- PHP1B
evidence:
- reference: PMID:38423572
  reference_title: Epileptic seizures and abnormal tooth development as primary presentation of pseudohypoparathyroidism
    type 1B.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: This case demonstrates the importance of screening for hypocalcaemia in patients with de novo
    epileptic seizures.
  explanation: Supports neurologic manifestations as a downstream consequence of hypocalcemia in PHP.
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
**Generated:** 2026-05-23T07:12:12.944148

1. zhang2020paroxysmaldyskinesiaand pages 1-2
2. wen2025atypicalpresentationof pages 2-4
3. sindaco2024pthresistancesyndromes pages 64-68
4. paparella2026endocrinedisordersof pages 19-20
5. paparella2026endocrinedisordersof pages 10-11
6. sindaco2024pthresistancesyndromes pages 7-13
7. https://doi.org/10.1297/cpe.2023-0080
8. https://doi.org/10.1002/mgg3.1423
9. https://doi.org/10.3389/fgene.2025.1638472
10. https://doi.org/10.1186/s12902-025-01933-0
11. https://doi.org/10.1007/s40618-020-01355-w
12. https://doi.org/10.1038/nrendo.2016.52
13. https://doi.org/10.1016/S0140-6736(15
14. https://doi.org/10.3390/cells15020140
15. https://doi.org/10.1136/bcr-2023-258403
16. https://doi.org/10.1297/cpe.2023-0080,
17. https://doi.org/10.1002/mgg3.1423,
18. https://doi.org/10.3389/fgene.2025.1638472,
19. https://doi.org/10.1186/s12902-025-01933-0,
20. https://doi.org/10.3390/cells15020140,
