# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Lynch Syndrome
- **Category:**

## Target Hypothesis
- **Hypothesis ID:** canonical_mmr_msi_carcinogenesis_model
- **Hypothesis Label:** Canonical Mismatch Repair Loss / MSI Carcinogenesis Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_mmr_msi_carcinogenesis_model
hypothesis_label: Canonical Mismatch Repair Loss / MSI Carcinogenesis Model
status: CANONICAL
description: Lynch syndrome is caused by germline heterozygous loss-of-function variants in the DNA mismatch
  repair genes MLH1, MSH2, MSH6, or PMS2, or by EPCAM 3' deletions that silence MSH2 in epithelial tissue.
  Somatic biallelic MMR inactivation ('second hit') in intestinal, endometrial, and other epithelium produces
  microsatellite instability (MSI-H), accumulating insertion/deletion mutations at short tandem repeats
  and frameshift mutations in tumor suppressor genes (TGFBR2, BAX, MSH3) that drive colorectal, endometrial,
  ovarian, gastric, and urothelial carcinogenesis. The accelerated adenoma-carcinoma sequence in MMR-deficient
  colon (versus the Vogelstein chromosomal-instability path in FAP) explains the early-onset, right-sided,
  often poorly differentiated phenotype. MSI testing and IHC for MLH1/MSH2/MSH6/PMS2 are now standard
  tumor screening modalities. Immune checkpoint blockade (pembrolizumab, nivolumab) is highly effective
  in MSI-H tumors, corroborating that hypermutation-driven neoantigen load is mechanistically coupled
  to MMR loss and validates the MSI carcinogenesis axis of the canonical model.
evidence:
- reference: PMID:19466295
  reference_title: 'Mismatch repair genes in Lynch syndrome: a review.'
  supports: SUPPORT
  evidence_source: OTHER
  snippet: Lynch syndrome represents 1-7% of all cases of colorectal cancer and is an autosomal-dominant
    inherited cancer predisposition syndrome caused by germline mutations in deoxyribonucleic acid (DNA)
    mismatch repair genes.
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

**Provider:** falcon
**Generated:** 2026-05-25T12:49:55.107797

1. walker2023dnamismatchrepair pages 2-3
2. walker2023dnamismatchrepair pages 16-16
3. deng2024pathologicalresponsefollowing pages 1-2
4. pantaleo2023tumortestingand pages 1-2
5. snowsill2017moleculartestingfor pages 35-36
6. storandt2026deficientmismatchrepairmicrosatellite pages 1-2
7. kavun2023microsatelliteinstabilitya pages 13-15
8. eroglu2025lynchsyndromein pages 7-9
9. tosi2024curativeimmunecheckpoint pages 1-2
10. jonchere2024microsatelliteinstabilityat pages 10-12
11. buono2024lynchsyndromefrom pages 3-5
12. buono2024lynchsyndromefrom pages 1-2
13. vazzano2023universaltumorscreening pages 1-2
14. jonchere2024microsatelliteinstabilityat pages 15-16
15. ascrizzi2023lynchsyndromebiopathology pages 2-4
16. ascrizzi2023lynchsyndromebiopathology pages 4-6
17. kavun2023microsatelliteinstabilitya pages 7-9
18. walker2023dnamismatchrepair pages 3-5
19. tosi2024curativeimmunecheckpoint pages 2-3
20. kavun2023microsatelliteinstabilitya pages 9-10
21. ascrizzi2023lynchsyndromebiopathology pages 20-21
22. walker2023dnamismatchrepair pages 23-24
23. jonchere2024microsatelliteinstabilityat pages 1-2
24. vazzano2023universaltumorscreening pages 2-4
25. eroglu2025lynchsyndromein pages 22-25
26. https://doi.org/10.1038/bjc.2015.281
27. https://doi.org/10.3390/cancers16050849
28. https://doi.org/10.3390/cancers15153930
29. https://doi.org/10.3390/cancers15204925
30. https://doi.org/10.1186/s13059-024-03340-5
31. https://doi.org/10.1007/s10689-022-00302-3
32. https://doi.org/10.3390/cancers15205061
33. https://doi.org/10.3390/cancers17243981
34. https://doi.org/10.1016/j.esmoop.2024.103929
35. https://doi.org/10.3389/fimmu.2024.1466497
36. https://doi.org/10.3390/cancers15082288
37. https://doi.org/10.3310/hta21510
38. https://doi.org/10.1007/s00292-023-01208-2
39. https://doi.org/10.3390/cancers16050849,
40. https://doi.org/10.3390/cancers15204925,
41. https://doi.org/10.3390/cancers17243981,
42. https://doi.org/10.1016/j.esmoop.2024.103929,
43. https://doi.org/10.3310/hta21510,
44. https://doi.org/10.1136/bmjonc-2025-000980,
45. https://doi.org/10.1007/s00292-023-01208-2,
46. https://doi.org/10.1186/s13059-024-03340-5,
47. https://doi.org/10.3390/cancers15153930,
48. https://doi.org/10.3390/cancers15082288,
49. https://doi.org/10.3389/fimmu.2024.1466497,
50. https://doi.org/10.1007/s10689-022-00302-3,
51. https://doi.org/10.3390/cancers15205061,
