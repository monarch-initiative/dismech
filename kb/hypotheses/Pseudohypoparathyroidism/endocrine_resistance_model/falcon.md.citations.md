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
- **Hypothesis ID:** endocrine_resistance_model
- **Hypothesis Label:** Endocrine Resistance Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: endocrine_resistance_model
hypothesis_label: Endocrine Resistance Model
status: CANONICAL
description: Impaired Gs alpha signaling in hormone-responsive tissues causes PTH-centered mineral metabolism
  abnormalities and variable resistance to additional endocrine axes such as TSH and GH pathways.
applies_to_subtypes:
- PHP1A
- PHP1B
evidence:
- reference: PMID:29959430
  reference_title: 'Diagnosis and management of pseudohypoparathyroidism and related disorders: first
    international Consensus Statement.'
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: specific features, such as PTH resistance, TSH resistance, growth hormone deficiency
  explanation: Consensus guidance supports a multiaxis endocrine resistance framework.
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
**Generated:** 2026-05-23T06:34:59.176852

1. iwasaki2023thelongrangeinteraction pages 10-11
2. linglart2018pseudohypoparathyroidism pages 1-3
3. iwasaki2023thelongrangeinteraction pages 1-2
4. li2024recurrentsmallvariants pages 1-2
5. li2024recurrentsmallvariants pages 10-11
6. maneroazua2024heterodisomyinthe pages 1-2
7. sippelli2024identificationofa pages 1-2
8. linglart2018pseudohypoparathyroidism pages 8-10
9. urakawa2026amaternalexon pages 1-2
10. li2024recurrentsmallvariants pages 5-7
11. mantovani2018multiplehormoneresistance pages 8-10
12. mantovani2018multiplehormoneresistance pages 6-8
13. mantovani2018multiplehormoneresistance pages 11-12
14. li2024recurrentsmallvariants pages 7-10
15. mantovani2018multiplehormoneresistance pages 1-3
16. https://doi.org/10.1172/jci167953
17. https://doi.org/10.1172/jci.insight.185874
18. https://doi.org/10.3389/fendo.2024.1505244
19. https://doi.org/10.1186/s12887-024-04761-8
20. https://doi.org/10.1016/j.ecl.2018.07.011
21. https://doi.org/10.1016/j.beem.2018.01.002
22. https://doi.org/10.1016/B978-0-12-804182-6.00035-6
23. https://doi.org/10.3389/fgene.2025.1638472
24. https://doi.org/10.1186/s13148-026-02107-y
25. https://doi.org/10.1172/jci167953.
26. https://doi.org/10.1172/jci.insight.185874.
27. https://doi.org/10.3389/fendo.2024.1505244.
28. https://doi.org/10.1016/j.ecl.2018.07.011,
29. https://doi.org/10.1016/b978-0-12-804182-6.00035-6,
30. https://doi.org/10.1172/jci.insight.185874,
31. https://doi.org/10.1172/jci167953,
32. https://doi.org/10.1186/s12887-024-04761-8,
33. https://doi.org/10.1016/j.beem.2018.01.002,
34. https://doi.org/10.3389/fendo.2024.1505244,
35. https://doi.org/10.3389/fgene.2025.1638472,
36. https://doi.org/10.1186/s13148-026-02107-y,
