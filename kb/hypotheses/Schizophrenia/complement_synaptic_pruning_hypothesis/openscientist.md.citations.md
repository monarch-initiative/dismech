# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Schizophrenia
- **Category:** Psychiatric

## Target Hypothesis
- **Hypothesis ID:** complement_synaptic_pruning_hypothesis
- **Hypothesis Label:** Complement-Mediated Synaptic Pruning Hypothesis
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: complement_synaptic_pruning_hypothesis
hypothesis_label: Complement-Mediated Synaptic Pruning Hypothesis
status: EMERGING
description: Schizophrenia risk alleles that increase complement C4A activity may increase complement
  tagging of vulnerable synapses during adolescent and young-adult cortical maturation. Microglia then
  remove more synaptic material than is developmentally appropriate, especially in prefrontal and hippocampal
  circuits, creating synaptic-density loss and circuit dysconnectivity that can feed into downstream dopamine
  dysregulation and clinical symptom domains.
notes: Modeled separately from the canonical dopamine/glutamate framework because the complement-C4A link
  has strong genetic, patient-derived cellular, and mouse-model support, but the full human causal chain
  from C4A dosage to synapse loss, dopamine changes, developmental timing, and symptom-domain specificity
  remains partially inferred.
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
**Generated:** 2026-07-06T04:13:56.531418

1. PMID:26814963
2. PMID:35396580
3. PMID:33353966
4. PMID:41903141
5. PMID:39227431
6. PMID:30718903
7. PMID:33190236
8. PMID:42000733
9. PMID:31699629
10. PMID:34819729
11. PMID:32499649
12. PMID:40053590
13. PMID:42276261
14. PMID:41983246
15. PMID:41978241
16. PMID:41274180
17. PMID:39741241
18. PMID:28138113
19. PMID:25195065
20. PMID:42113976
21. PMID:30864461
22. PMID:34789848
23. PMID:38906225
24. PMID:40752823
25. PMID:37041206
26. PMID:41130556
27. PMID:40502190