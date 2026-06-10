# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Autosomal Dominant Polycystic Kidney Disease
- **Category:** Mendelian

## Target Hypothesis
- **Hypothesis ID:** canonical_pkd1_pkd2_cilia_signaling_cystogenesis_model
- **Hypothesis Label:** Canonical PKD1/PKD2 / Primary Cilium / Cystogenesis Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_pkd1_pkd2_cilia_signaling_cystogenesis_model
hypothesis_label: Canonical PKD1/PKD2 / Primary Cilium / Cystogenesis Model
status: CANONICAL
description: Autosomal dominant polycystic kidney disease (ADPKD) is caused by heterozygous loss-of-function
  variants in PKD1 (~78%) or PKD2 (~15%) encoding polycystin-1 and polycystin-2, transmembrane proteins
  that localize to the primary cilium of renal tubular epithelial cells and form a mechanosensitive calcium
  channel complex. Loss of polycystin function disrupts ciliary calcium signaling, elevates cAMP, activates
  B-Raf/MEK/ERK proliferative signaling, and triggers progressive cyst formation, expansion, and tubular
  dilation throughout the kidney (and liver/pancreas). The 'two-hit' model — germline heterozygosity followed
  by somatic second-hit events in individual tubular epithelial cells — explains the focal nature of cyst
  initiation. Tolvaptan (V2-vasopressin receptor antagonist, lowering renal cAMP) is the first disease-modifying
  therapy and slows GFR decline, corroborating the cAMP-driven cystogenesis axis of the canonical model.
evidence:
- reference: PMID:40126492
  reference_title: Autosomal dominant polycystic kidney disease.
  supports: SUPPORT
  evidence_source: OTHER
  snippet: Most persons with ADPKD have an affected parent, but de novo disease is suggested in 10% to
    25% of families.
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
**Generated:** 2026-05-25T12:41:25.028800

1. qiu2023mechanismsofcyst pages 3-4
2. zhou2023drugrepurposingin pages 6-9
3. zhou2023drugrepurposingin pages 1-6
4. boletta2025physiologicmechanismsunderlying pages 14-15
5. preval2025pathogenicpathwaysand pages 2-4
6. alorjani2025mechanisticinsightsinto pages 3-4
7. afrin2025kidneyorganoidmodels pages 12-16
8. wu2024stingpromotesthe pages 1-2
9. kim2023recentupdatesin pages 6-8
10. alorjani2025mechanisticinsightsinto pages 18-20
11. kim2023recentupdatesin pages 1-2
12. alorjani2025mechanisticinsightsinto pages 15-17
13. boletta2025physiologicmechanismsunderlying pages 12-14
14. kim2023recentupdatesin pages 4-5
15. qiu2023mechanismsofcyst pages 7-9
16. alorjani2025mechanisticinsightsinto pages 17-18
17. lapao2025autosomaldominantpolycystic pages 2-4
18. https://platform.opentargets.org
19. https://doi.org/10.1053/j.akdh.2023.03.001
20. https://doi.org/10.1016/j.kint.2023.02.010
21. https://doi.org/10.3390/cells14151203
22. https://doi.org/10.1152/physrev.00018.2024
23. https://doi.org/10.3390/ijms25052936
24. https://doi.org/10.1038/s41467-024-55684-y
25. https://doi.org/10.3390/biom14101215
26. https://doi.org/10.1016/j.kint.2023.02.010,
27. https://doi.org/10.1053/j.akdh.2023.03.001,
28. https://doi.org/10.3390/cells14151203,
29. https://doi.org/10.1152/physrev.00018.2024,
30. https://doi.org/10.33696/signaling.6.144,
31. https://doi.org/10.3390/cells13201722,
32. https://doi.org/10.1152/ajprenal.00116.2025,
33. https://doi.org/10.3390/biom14101215,
34. https://doi.org/10.3904/kjim.2022.376,
35. https://doi.org/10.3390/ijms26031121,
