# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Familial Adenomatous Polyposis
- **Category:**

## Target Hypothesis
- **Hypothesis ID:** canonical_apc_wnt_betacatenin_polyp_carcinoma_model
- **Hypothesis Label:** Canonical APC / Wnt-β-Catenin / Polyp-to-Carcinoma Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_apc_wnt_betacatenin_polyp_carcinoma_model
hypothesis_label: Canonical APC / Wnt-β-Catenin / Polyp-to-Carcinoma Model
status: CANONICAL
description: Familial adenomatous polyposis (FAP) is caused by germline heterozygous loss-of-function
  variants in APC on 5q22.2 encoding the adenomatous polyposis coli tumor suppressor. APC normally serves
  as a scaffold in the β-catenin destruction complex (with Axin, GSK-3β, CK1) targeting β-catenin for
  ubiquitin-proteasomal degradation. Biallelic APC inactivation (germline + somatic 'second hit') stabilizes
  cytoplasmic β-catenin, allowing nuclear translocation and TCF/LEF-dependent transcription of pro-proliferative
  targets (MYC, CCND1, LGR5), initiating colorectal adenoma formation throughout the colon. Sequential
  acquisition of KRAS, TP53, and SMAD4 mutations follows the Vogelstein adenoma- carcinoma progression
  model, producing virtually 100% CRC risk by age 40 in classic FAP without intervention. Prophylactic
  colectomy is the standard of care; mouse Apc^Min/+ models recapitulate intestinal polyposis and validate
  the Wnt-axis as the canonical initiating lesion.
evidence:
- reference: PMID:28668823
  reference_title: Familial adenomatous polyposis.
  supports: SUPPORT
  evidence_source: OTHER
  snippet: It is characterized by the presence of hundreds of colonic polyps, which have a high tendency
    to undergo malignant transformation.
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
**Generated:** 2026-05-24T17:21:40.882783

1. PMID:12045208
2. PMID:11283620
3. PMID:15561772
4. PMID:36586069
5. PMID:31416464
6. PMID:15710876
7. PMID:31867777
8. PMID:27511199
9. PMID:40237877
10. PMID:30046385
11. PMID:37800450
12. PMID:34352208
13. PMID:19092804
14. PMID:18403596
15. PMID:35849876
16. PMID:15327768
17. PMID:22120905
18. PMID:28010732
19. PMID:23169527
20. PMID:18836487
21. PMID:19197353
22. PMID:24026117
23. PMID:29556067
24. PMID:35803914
25. PMID:19169759
26. PMID:33948826
27. PMID:40237887
28. PMID:22654442
29. PMID:27661107
30. PMID:17155896
31. PMID:11854387
32. PMID:14565811
33. PMID:18433509
34. PMID:9824584
35. PMID:39395692
36. PMID:26622826
37. PMID:36873622
38. PMID:17952864
39. PMID:9250146
40. PMID:40879644
41. PMID:40356044
42. PMID:37853284
43. PMID:12130875
44. PMID:40840111
45. PMID:26613750
46. PMID:27816598
47. PMID:18474248
48. PMID:26780541
49. PMID:37848928
50. PMID:30881361
51. PMID:34253565
