# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Tuberous Sclerosis Complex
- **Category:** Mendelian

## Target Hypothesis
- **Hypothesis ID:** canonical_tsc1_tsc2_mtorc1_hyperactivation_model
- **Hypothesis Label:** Canonical TSC1 / TSC2 / mTORC1 Hyperactivation Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_tsc1_tsc2_mtorc1_hyperactivation_model
hypothesis_label: Canonical TSC1 / TSC2 / mTORC1 Hyperactivation Model
status: CANONICAL
description: 'Tuberous sclerosis complex (TSC) is caused by germline heterozygous loss-of-function variants
  in TSC1 (hamartin, 9q34.13) or TSC2 (tuberin, 16p13.3). The TSC1-TSC2 complex functions as a GTPase-
  activating protein (GAP) for the Rheb GTPase, restraining mTORC1. Biallelic somatic loss (''second hit'')
  in individual cells releases Rheb-GTP and drives constitutive mTORC1 activation, producing cell growth,
  proliferation, and characteristic hamartomas in nearly every organ system: cortical tubers and subependymal
  nodules (SEN/SEGA) in the brain, cardiac rhabdomyomas, renal angiomyolipomas, pulmonary lymphangioleiomyomatosis,
  hypomelanotic macules, facial angiofibromas. Neurologically, the mTORC1-hyperactivation lesion produces
  epilepsy (infantile spasms, refractory seizures), TSC-associated neuropsychiatric disorders (TAND),
  and intellectual disability. Rapamycin/everolimus and sirolimus (mTORC1 inhibitors) provide direct pharmacologic
  validation: shrinking SEGAs, angiomyolipomas, and LAM lesions and reducing seizure frequency, definitively
  confirming the mTORC1-hyperactivation axis as the canonical mechanism.'
evidence:
- reference: PMID:39334956
  reference_title: Tuberous sclerosis complex.
  supports: SUPPORT
  evidence_source: OTHER
  snippet: Tuberous sclerosis complex (TSC) is a rare multisystem disorder caused by heterozygous loss-of-function
    pathogenic variants in the tumour suppressor genes TSC1 and TSC2 encoding the tuberin and hamartin
    proteins, respectively.
  explanation: |
    Existing canonical mechanism citation in the dismech knowledge base, used as the seed for the hypothesis-search deep-research run.
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
**Generated:** 2026-05-25T13:04:52.103299

1. PMID:33436626
2. PMID:22795129
3. PMID:37462942
4. PMID:27494029
5. PMID:30127391
6. PMID:26837766
7. PMID:36229934
8. PMID:30192751
9. PMID:31217257
10. PMID:41061327
11. PMID:41135308
12. PMID:32705817
13. PMID:33972524
14. PMID:41379617
15. PMID:41502066
16. PMID:41238564
17. PMID:37880800
18. PMID:24395886
19. PMID:19202070
20. PMID:38714540
21. PMID:40993764
22. PMID:41352576
23. PMID:32954437
24. PMID:24948799
25. PMID:34173252
26. PMID:26003087
27. PMID:29466735
28. PMID:18023148
29. PMID:11112665
30. PMID:40579409
31. PMID:39352229
32. PMID:39144255
33. PMID:41789478
34. PMID:40996830
35. PMID:23325902
36. PMID:30564495
37. PMID:40673944
38. PMID:40836528
39. PMID:41266529
40. PMID:39762914
41. PMID:40504787
