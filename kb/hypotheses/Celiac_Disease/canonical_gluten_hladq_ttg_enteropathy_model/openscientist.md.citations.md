# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Celiac Disease
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** canonical_gluten_hladq_ttg_enteropathy_model
- **Hypothesis Label:** Canonical Gluten / HLA-DQ2-DQ8 / tTG Enteropathy Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_gluten_hladq_ttg_enteropathy_model
hypothesis_label: Canonical Gluten / HLA-DQ2-DQ8 / tTG Enteropathy Model
status: CANONICAL
description: Celiac disease arises in HLA-DQ2 / HLA-DQ8 positive individuals from a CD4 T-cell-mediated
  immune response to dietary gluten/gliadin peptides that have been deamidated by tissue transglutaminase
  2 (TG2/tTG). Deamidation converts neutral glutamine residues to negatively charged glutamate, dramatically
  increasing peptide affinity for HLA-DQ2/DQ8 and licensing presentation to gluten- reactive CD4 T cells
  in the lamina propria. The resulting Th1/IFN-γ cytokine response drives intraepithelial lymphocyte cytotoxicity,
  IL-15-mediated epithelial activation, B-cell expansion with anti-TG2 autoantibody production, crypt
  hyperplasia, and villous atrophy. Gluten-free diet remission, HLA-DQ2/DQ8 restriction, and TG2 inhibitor
  (ZED1227) trials all corroborate the gluten / HLA / TG2 axis as the canonical pathogenic mechanism.
evidence:
- reference: PMID:38914866
  reference_title: 'Transglutaminase 2 in celiac disease: pathogenic role and therapeutic target.'
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Transglutaminase 2 (TG2) plays a pivotal role in the pathogenesis of
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

**Provider:** openscientist
**Generated:** 2026-05-23T22:39:43.397866

1. PMID:34192430
2. PMID:23775608
3. PMID:32051586
4. PMID:38914866
5. PMID:37445994
6. PMID:10700238
7. PMID:24724018
8. PMID:17629515
9. PMID:12949719
10. PMID:15357948
11. PMID:26001928
12. PMID:19805228
13. PMID:40818857
14. PMID:25920553
15. PMID:38552723
16. PMID:22750506
17. PMID:21908620
18. PMID:31285344
19. PMID:12219789
20. PMID:3170777
21. PMID:20061410
22. PMID:21206487
23. PMID:22785229
24. PMID:27993525
25. PMID:29574077
26. PMID:36898393
27. PMID:21822909
28. PMID:34339872
29. PMID:23163616
30. PMID:28188172
31. PMID:29787419
32. PMID:30978358
33. PMID:22811741
34. PMID:22214930
35. PMID:15489956
36. PMID:27352981
37. PMID:28386004
38. PMID:27548641
39. PMID:23982754
40. PMID:17215859
41. PMID:31593953
42. PMID:31622625
43. PMID:17697209
44. PMID:42016930
45. PMID:40133841
46. PMID:33134034
