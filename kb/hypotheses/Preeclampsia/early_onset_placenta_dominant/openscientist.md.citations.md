# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Preeclampsia
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** early_onset_placenta_dominant
- **Hypothesis Label:** Early-Onset Placenta-Dominant Antiangiogenic Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: early_onset_placenta_dominant
hypothesis_label: Early-Onset Placenta-Dominant Antiangiogenic Model
status: CANONICAL
applies_to_subtypes:
- Early-onset
- HELLP
description: |
  In early-onset preeclampsia, immune maladaptation at the maternal-fetal interface and defective trophoblast invasion produce severe placental malperfusion before clinical disease. Placental hypoxia and stress drive a marked antiangiogenic shift, especially excess sFlt-1 and soluble endoglin with reduced free PlGF, causing maternal endothelial dysfunction and organ-specific renal, hepatic, CNS, and uteroplacental manifestations.
evidence:
- reference: PMID:35177220
  reference_title: 'Preeclampsia and eclampsia: the conceptual evolution of a syndrome.'
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Early-onset preeclampsia has many features in common with atherosclerosis, whereas late-onset
    preeclampsia seems to result from a mismatch of fetal demands and maternal supply, that is, a metabolic
    crisis.
  explanation: Supports modeling early-onset preeclampsia separately from late-onset disease.
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
**Generated:** 2026-06-03T09:56:04.435262

1. PMID:40253080
2. PMID:41582793
3. PMID:21810665
4. PMID:29858106
5. PMID:41814104
6. PMID:31188674
7. PMID:41213792
8. PMID:35670085
9. PMID:39440423
10. PMID:28628106
11. PMID:29138037
12. PMID:24091323
13. PMID:20972337
14. PMID:22103497
15. PMID:25298513
16. PMID:39224973
17. PMID:24335973
18. PMID:30399576
19. PMID:29466360
20. PMID:28619690
21. PMID:34666379
22. PMID:23228435
23. PMID:42041953
24. PMID:22217911
25. PMID:41275618
26. PMID:38300220
27. PMID:41294257
28. PMID:35177220
29. PMID:41897533
30. PMID:38983853
