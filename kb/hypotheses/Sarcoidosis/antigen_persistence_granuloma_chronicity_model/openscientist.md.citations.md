# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Sarcoidosis
- **Category:** Immune

## Target Hypothesis
- **Hypothesis ID:** antigen_persistence_granuloma_chronicity_model
- **Hypothesis Label:** Antigen Persistence / Th17.1 / mTORC1 Granuloma Chronicity Model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: antigen_persistence_granuloma_chronicity_model
hypothesis_label: Antigen Persistence / Th17.1 / mTORC1 Granuloma Chronicity Model
status: EMERGING
description: Sarcoidosis is modeled as a genetically conditioned, antigen-driven granulomatous immune
  response in which poorly degradable or repeatedly encountered antigens are presented by macrophage-lineage
  antigen-presenting cells to CD4+ T cells. The activated T-cell compartment polarizes toward IFN-gamma-producing
  Th17.1/Th1-like effector states while regulatory T-cell restraint is insufficient. This cytokine circuit
  recruits and activates macrophages, promotes epithelioid and multinucleated giant-cell granuloma architecture,
  and intersects with macrophage-intrinsic metabolic programs such as mTORC1 activation. Resolution is
  hypothesized to require antigen clearance or sequestration plus restoration of regulatory and apoptotic
  checkpoints; chronic disease and fibrosis occur when antigen persistence, Th17.1 feedback, macrophage
  survival/proliferation, and tissue-repair programs remain engaged.
evidence:
- reference: PMID:38165044
  reference_title: Immune mechanisms of granuloma formation in sarcoidosis and tuberculosis.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Sarcoidosis is a complex immune-mediated disease characterized by clusters of immune cells
    called granulomas.
  explanation: |
    Recent mechanistic review used as the seed reference for the hypothesis-search deep-research run and for the antigen/T-cell/macrophage granuloma-chronicity framing.
- reference: PMID:31273209
  reference_title: Sarcoidosis.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: The disease develops in genetically predisposed individuals with exposure to an as-yet unknown
    antigen.
  explanation: |
    Nature Reviews Disease Primers review supports the central upstream premise of this hypothesis: genetically predisposed patients encounter an unknown antigenic trigger.
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
**Generated:** 2026-06-03T11:40:50.280377

1. PMID:28092373
2. PMID:38147536
3. PMID:38267106
4. PMID:40996589
5. PMID:27379969
6. PMID:29310925
7. PMID:27755127
8. PMID:35546376
9. PMID:26376720
10. PMID:33901497
11. PMID:32551397
12. PMID:41197661
13. PMID:7929830
14. PMID:8881751
15. PMID:22552860
16. PMID:40075078
17. PMID:26051272
18. PMID:41466414
19. PMID:37399103
20. PMID:40667074
21. PMID:33387486
22. PMID:24284293
23. PMID:23863960
24. PMID:42170754
25. PMID:24325385
26. PMID:40103819
27. PMID:30326785
28. PMID:31279873
29. PMID:30220489
30. PMID:33570446
31. PMID:39896662
32. PMID:40393718
33. PMID:36356657
34. PMID:30154391
35. PMID:17975200
36. PMID:21899998
37. PMID:25194337
38. PMID:25771769
39. PMID:41597666
40. PMID:40837573
41. PMID:23993988
42. PMID:42143504
43. PMID:37750561
44. PMID:40086403
