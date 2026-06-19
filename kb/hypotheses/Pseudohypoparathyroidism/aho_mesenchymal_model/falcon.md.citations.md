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
- **Hypothesis ID:** aho_mesenchymal_model
- **Hypothesis Label:** AHO Mesenchymal Differentiation Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: aho_mesenchymal_model
hypothesis_label: AHO Mesenchymal Differentiation Model
status: CANONICAL
description: Altered GNAS-dependent signaling in bone and mesenchymal lineages drives brachydactyly, ectopic
  ossification, and related AHO structural phenotypes.
applies_to_subtypes:
- PHP1A
- Pseudopseudohypoparathyroidism
evidence:
- reference: PMID:29959430
  reference_title: 'Diagnosis and management of pseudohypoparathyroidism and related disorders: first
    international Consensus Statement.'
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: resistance to PTH, ectopic ossifications, brachydactyly and early-onset obesity.
  explanation: Supports the core AHO morphologic feature set grouped in this model.
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
**Generated:** 2026-05-23T06:57:06.028899

1. salemi2018ossificationsinalbright pages 3-5
2. xu2022gnaslosscauses pages 6-8
3. elli2024targetedsilencingof pages 1-2
4. huso2011heterotopicossificationsin pages 1-2
5. mcmullan2022aberrantboneregulation pages 5-7
6. bastepe2018gnasmutationsand pages 9-13
7. salemi2018ossificationsinalbright pages 1-2
8. pignolo2011heterozygousinactivationof pages 6-8
9. regard2013activationofhedgehog pages 5-7
10. krishnan2023prevalenceofchiari pages 1-2
11. ertl2023recombinantgrowthhormone pages 1-3
12. regard2013activationofhedgehog pages 7-8
13. salemi2018ossificationsinalbright pages 8-9
14. bastepe2018gnasmutationsand pages 6-9
15. yang2023gnaslocusbone pages 11-12
16. pignolo2011heterozygousinactivationof pages 1-2
17. pignolo2011heterozygousinactivationof pages 5-6
18. huso2011heterotopicossificationsin pages 2-3
19. salemi2018ossificationsinalbright pages 5-6
20. salemi2018ossificationsinalbright pages 2-3
21. mcmullan2022aberrantboneregulation pages 10-10
22. mcmullan2022aberrantboneregulation pages 2-4
23. mcmullan2022aberrantboneregulation pages 1-2
24. yang2023gnaslocusbone pages 18-18
25. yang2023gnaslocusbone pages 9-10
26. PPHP
27. 20/20
28. https://doi.org/10.1038/nm.3314
29. https://doi.org/10.1002/jbmr.481
30. https://doi.org/10.1371/journal.pone.0021755
31. https://doi.org/10.1210/jc.2017-00860
32. https://doi.org/10.1177/00220345221075215
33. https://doi.org/10.1016/j.bone.2017.09.002
34. https://doi.org/10.1007/s11914-022-00719-w
35. https://doi.org/10.3389/fendo.2024.1296886
36. https://doi.org/10.3389/fendo.2023.1255864
37. https://doi.org/10.3390/ijms252010913
38. https://doi.org/10.1371/journal.pone.0280463
39. https://doi.org/10.1093/ejendo/lvad085
40. https://doi.org/10.3389/fendo.2024.1296886.
41. https://doi.org/10.1210/jc.2017-00860,
42. https://doi.org/10.1038/nm.3314,
43. https://doi.org/10.1177/00220345221075215,
44. https://doi.org/10.1016/j.bone.2017.09.002,
45. https://doi.org/10.1007/s11914-022-00719-w,
46. https://doi.org/10.3389/fendo.2023.1255864,
47. https://doi.org/10.1002/jbmr.481,
48. https://doi.org/10.1371/journal.pone.0021755,
49. https://doi.org/10.3389/fendo.2024.1296886,
50. https://doi.org/10.3390/ijms252010913,
51. https://doi.org/10.1371/journal.pone.0280463,
52. https://doi.org/10.1093/ejendo/lvad085,
