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
- **Hypothesis ID:** neuroendocrine_obesity_model
- **Hypothesis Label:** GNAS-Related Neuroendocrine Obesity Model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: neuroendocrine_obesity_model
hypothesis_label: GNAS-Related Neuroendocrine Obesity Model
status: EMERGING
description: Early-onset obesity may reflect disrupted Gs alpha-dependent GPCR signaling in energy-homeostasis
  pathways, superimposed on classic PHP endocrine and skeletal mechanisms.
applies_to_subtypes:
- PHP1A
- PHP1B
evidence:
- reference: PMID:38103632
  reference_title: The role of genetic and epigenetic GNAS alterations in the development of early-onset
    obesity.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Genetic or epigenetic alterations in GNAS are known to cause pseudohypoparathyroidism in its
    different subtypes and have been recently associated with isolated, early-onset, severe obesity.
  explanation: Supports obesity-specific mechanistic superimposition on canonical PHP pathophysiology.
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
**Generated:** 2026-05-23T07:31:07.233571

1. chen2009centralnervoussystem pages 4-6
2. gruterskieslich2017earlyonsetobesityunrecognized pages 9-10
3. roizen2016restingenergyexpenditure pages 4-6
4. perez2018glucosehomeostasisand pages 1-2
5. gruterskieslich2017earlyonsetobesityunrecognized pages 5-7
6. modica2023parathyroiddiseasesand pages 9-10
7. abbas2024gnasknockdowninduces pages 1-2
8. abbas2024gnasknockdowninduces pages 9-12
9. weinstein2010theroleof pages 1-2
10. weinstein2010theroleof pages 3-4
11. shoemaker2013energyexpenditurein pages 1-2
12. shoemaker2013energyexpenditurein pages 4-5
13. abbas2024gnasknockdowninduces pages 12-14
14. gruterskieslich2017earlyonsetobesityunrecognized pages 7-9
15. gruterskieslich2017earlyonsetobesityunrecognized pages 3-5
16. gruterskieslich2017earlyonsetobesityunrecognized pages 1-3
17. shoemaker2013energyexpenditurein pages 5-6
18. perez2018glucosehomeostasisand pages 9-9
19. germainlee2019managementofpseudohypoparathyroidism pages 3-4
20. germainlee2019managementofpseudohypoparathyroidism pages 9-10
21. https://doi.org/10.1016/j.cmet.2009.05.004
22. https://doi.org/10.1172/jci88622
23. https://doi.org/10.1074/jbc.ra118.003450
24. https://doi.org/10.1210/jc.2015-3895
25. https://doi.org/10.1038/ijo.2012.200
26. https://doi.org/10.1210/jc.2018-01067
27. https://doi.org/10.1186/1687-9856-2014-21
28. https://doi.org/10.1007/s40618-023-02018-2
29. https://doi.org/10.1186/s13023-023-02979-w
30. https://doi.org/10.3390/ijms252312674
31. https://doi.org/10.1210/jc.2017-00395
32. https://doi.org/10.1172/jci.insight.177190
33. https://doi.org/10.1097/mop.0000000000000783
34. https://clinicaltrials.gov/study/NCT07496463
35. https://doi.org/10.1016/j.cmet.2009.05.004,
36. https://doi.org/10.1210/jc.2015-3895,
37. https://doi.org/10.1210/jc.2018-01067,
38. https://doi.org/10.1172/jci88622,
39. https://doi.org/10.1210/jc.2017-00395,
40. https://doi.org/10.1007/s40618-023-02018-2,
41. https://doi.org/10.1172/jci.insight.177190,
42. https://doi.org/10.3390/ijms252312674,
43. https://doi.org/10.1038/ijo.2009.222,
44. https://doi.org/10.1055/s-0034-1387798,
45. https://doi.org/10.1038/ijo.2012.200,
46. https://doi.org/10.1097/mop.0000000000000783,
