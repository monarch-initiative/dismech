# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Long COVID
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** vascular_microclot_model
- **Hypothesis Label:** Endothelial-Microclot Perfusion Model
- **Status in KB:** ALTERNATIVE

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: vascular_microclot_model
hypothesis_label: Endothelial-Microclot Perfusion Model
status: ALTERNATIVE
description: |
  Fibrin amyloid microclots impair capillary flow and oxygen exchange, driving fatigue, dyspnea, and energy deficits in a vascular-predominant subtype.
applies_to_subtypes:
- Cardiopulmonary-dominant long COVID phenotype
evidence:
- reference: PMID:35195253
  reference_title: 'A central role for amyloid fibrin microclots in long COVID/PASC: origins and therapeutic
    implications.'
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: the ability of these fibrin amyloid microclots (fibrinaloids) to block up capillaries, and
    thus to limit the passage of red blood cells and hence O2 exchange, can actually underpin the majority
    of these symptoms
  explanation: Supports a perfusion-limitation mechanism that can coexist with immune-driven models.
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
**Generated:** 2026-05-23T06:00:04.674083

1. PMID:34425843
2. PMID:36131342
3. PMID:39409138
4. PMID:36015078
5. PMID:34328172
6. PMID:34389297
7. PMID:40892700
8. PMID:36223120
9. PMID:32750108
10. PMID:41591353
11. PMID:40185235
12. PMID:41372813
13. PMID:37175942
14. PMID:36253560
15. PMID:41794369
16. PMID:41494535
17. PMID:40441540
18. PMID:40843001
19. PMID:41459516
20. PMID:40652046
21. PMID:41576003
22. PMID:35195253
23. PMID:37301958
24. PMID:41353681
25. PMID:39942772
26. PMID:41516301
27. PMID:39240417
28. PMID:38041762
29. PMID:37981644
30. PMID:42051540
31. PMID:41513611
32. PMID:41516190
33. PMID:41864480
