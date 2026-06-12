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
- **Hypothesis ID:** canonical_persistence_immune_model
- **Hypothesis Label:** Canonical Viral Persistence-Immune Dysregulation Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_persistence_immune_model
hypothesis_label: Canonical Viral Persistence-Immune Dysregulation Model
status: CANONICAL
description: |
  Persistent viral RNA/antigen reservoirs sustain immune activation and downstream multisystem dysfunction, providing the default explanatory framework for Long COVID.
applies_to_subtypes:
- Pain-dominant long COVID phenotype
- Cardiopulmonary-dominant long COVID phenotype
evidence:
- reference: PMID:37140960
  reference_title: Viral persistence, reactivation, and mechanisms of long COVID.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Persistence of SARS-CoV-2 RNA or antigens is reported in some organs, yet the mechanism by
    which they do so and how they may be associated with pathogenic immune responses is unclear.
  explanation: Supports reservoir persistence linked to pathogenic immune responses.
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
**Generated:** 2026-05-23T05:49:52.916297

1. PMID:36517603
2. PMID:36131932
3. PMID:40987794
4. PMID:37140960
5. PMID:36052466
6. PMID:40618677
7. PMID:40188838
8. PMID:41562079
9. PMID:41200182
10. PMID:38327880
11. PMID:40247373
12. PMID:41840045
13. PMID:41274384
14. PMID:37848036
15. PMID:40429707
16. PMID:40175252
17. PMID:38589621
18. PMID:42039182
19. PMID:38138102
20. PMID:41824803
21. PMID:37310140
22. PMID:41830160
23. PMID:37080828
24. PMID:39271627
25. PMID:38668888
26. PMID:41513611
