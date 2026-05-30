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
- **Hypothesis ID:** canonical_imprinting_model
- **Hypothesis Label:** Canonical GNAS Imprinting Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_imprinting_model
hypothesis_label: Canonical GNAS Imprinting Model
status: CANONICAL
description: 'Parent-of-origin-specific GNAS expression explains subtype stratification: maternal alterations
  more often produce hormone resistance, while paternal coding variants favor AHO-predominant phenotypes.'
applies_to_subtypes:
- PHP1A
- PHP1B
- Pseudopseudohypoparathyroidism
evidence:
- reference: PMID:40972900
  reference_title: 'Imprinting and skeletal disorders: lessons from pseudohypoparathyroidism and related
    disorders.'
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Thus, genomic imprinting plays a key role in the phenotypes associated with GNAS alterations.
  explanation: Supports imprinting as the organizing principle for subtype-specific phenotype patterns.
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
**Generated:** 2026-05-23T06:23:57.643184

1. iwasaki2023thelongrangeinteraction pages 10-11
2. li2024recurrentsmallvariants pages 10-11
3. yang2023gnaslocusbone pages 8-9
4. root2023onehalfcenturyof pages 6-7
5. iwasaki2023thelongrangeinteraction pages 1-2
6. li2024recurrentsmallvariants pages 1-2
7. https://doi.org/10.1172/JCI167953
8. https://doi.org/10.1172/jci.insight.185874
9. https://doi.org/10.1297/cpe.2023-0065
10. https://doi.org/10.1002/mgg3.2144
11. https://doi.org/10.1515/jpem-2022-0624
12. https://doi.org/10.3389/fendo.2023.1255864
13. https://doi.org/10.1172/JCI167953.
14. https://doi.org/10.1172/jci.insight.185874.
15. https://doi.org/10.1297/cpe.2023-0065,
16. https://doi.org/10.1172/jci167953,
17. https://doi.org/10.1172/jci.insight.185874,
18. https://doi.org/10.3389/fendo.2023.1255864,
19. https://doi.org/10.1002/mgg3.2144,
20. https://doi.org/10.1515/jpem-2022-0624,
