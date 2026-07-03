# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Charcot-Marie-Tooth Disease
- **Category:** Mendelian

## Target Hypothesis
- **Hypothesis ID:** canonical_pmp22_mpz_axonal_demyelinating_neuropathy_model
- **Hypothesis Label:** Canonical PMP22 / MPZ / Axonal & Demyelinating Peripheral Neuropathy Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_pmp22_mpz_axonal_demyelinating_neuropathy_model
hypothesis_label: Canonical PMP22 / MPZ / Axonal & Demyelinating Peripheral Neuropathy Model
status: CANONICAL
description: Charcot-Marie-Tooth (CMT) disease is a clinically and genetically heterogeneous group of
  inherited peripheral neuropathies caused by variants in >100 genes encoding myelin components (PMP22,
  MPZ, GJB1), axonal cytoskeleton and transport proteins (MFN2, NEFL, KIF1B), and other Schwann-cell-axon
  interface factors. CMT1A (most common, PMP22 duplication on 17p11.2) produces demyelinating neuropathy
  through PMP22 overexpression-driven Schwann cell dysfunction and secondary axonal loss. Axonal CMT2
  forms (MFN2, MPZ, others) primarily impair axonal function. The uniform clinical phenotype — distal
  motor and sensory loss in a length-dependent pattern, with foot deformity, distal weakness, and absent
  reflexes — reflects convergent length-dependent axonal degeneration regardless of upstream gene defect.
  The PMP22 duplication CMT1A mouse and rat models recapitulate the human phenotype, and PMP22-lowering
  ASO and PXT3003 (low-dose drug combination) corroborate the PMP22-dosage axis as a canonical mechanism
  in the most common subtype.
evidence:
- reference: DOI:10.1093/brain/awae064
  reference_title: Whole genome sequencing increases the diagnostic rate in Charcot-Marie-Tooth disease
  supports: SUPPORT
  evidence_source: OTHER
  snippet: The most common genetic diagnosis was PMP22 duplication (CMT1A; 505/1165, 43.3%)
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
**Generated:** 2026-05-25T14:47:10.689285

1. PMID:38481354
2. PMID:31852984
3. PMID:30258273
4. PMID:19923170
5. PMID:21487305
6. PMID:41400104
7. PMID:32511821
8. PMID:36287202
9. PMID:35501630
10. PMID:16775375
11. PMID:26865613
12. PMID:34153322
13. PMID:36926597
14. PMID:26450076
15. PMID:21393063
16. PMID:23525455
17. PMID:29202483
18. PMID:41948127
19. PMID:34656144
20. PMID:30958311
21. PMID:22189569
22. PMID:28704293
23. PMID:39957630
24. PMID:39882365
25. PMID:32982928
26. PMID:37979968
27. PMID:25216747
28. PMID:32686211
29. PMID:38581130
30. PMID:28796392
31. PMID:29350067
32. PMID:11389829
33. PMID:30126838
34. PMID:41108054
35. PMID:37455204
36. PMID:36314052
37. PMID:25762662
38. PMID:32741968
39. PMID:35153971
40. PMID:40055046
41. PMID:26010264
42. PMID:40320863
