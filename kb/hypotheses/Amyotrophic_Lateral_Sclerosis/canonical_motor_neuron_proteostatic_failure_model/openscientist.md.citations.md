# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Amyotrophic Lateral Sclerosis
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** canonical_motor_neuron_proteostatic_failure_model
- **Hypothesis Label:** Canonical Motor Neuron Proteostatic Failure Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_motor_neuron_proteostatic_failure_model
hypothesis_label: Canonical Motor Neuron Proteostatic Failure Model
status: CANONICAL
description: Progressive upper and lower motor neuron degeneration in ALS is the convergent endpoint of
  multiple genetic and sporadic insults that ultimately cause proteostatic failure. Key drivers include
  cytoplasmic mislocalization and aggregation of TDP-43 (in >97% of cases), C9orf72 hexanucleotide repeat
  expansion–derived dipeptide repeats and RNA foci, SOD1 misfolding, FUS/EWSR1 phase-separation defects,
  impaired autophagy, mitochondrial dysfunction, axonal transport failure, and neuroinflammation. Selective
  vulnerability of cortical layer-5 Betz cells and spinal alpha motor neurons leads to progressive muscle
  denervation, weakness, atrophy, and ultimately respiratory failure. Antisense-oligonucleotide therapies
  targeting SOD1 (tofersen) and C9orf72 RNA validate the genetic-pathogenetic axes of this canonical multi-hit
  model.
evidence:
- reference: PMID:38891021
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: upper and lower motor neurons in the brain and spinal cord progressively degenerate
  explanation: |
    Canonical mechanism review used as the seed reference for the hypothesis-search deep-research run.
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
**Generated:** 2026-05-23T16:01:09.200504

1. PMID:41996987
2. PMID:36922834
3. PMID:38175301
4. PMID:41661214
5. PMID:41670738
6. PMID:41850233
7. PMID:39059407
8. PMID:39986312
9. PMID:41260310
10. PMID:39779681
11. PMID:39288267
12. PMID:32865792
13. PMID:40819564
14. PMID:40891053
15. PMID:39312574
16. PMID:41145518
17. PMID:19330001
18. PMID:41890591
19. PMID:41838122
20. PMID:23382207
21. PMID:37394036
22. PMID:39755715
23. PMID:41378777
24. PMID:34873335
25. PMID:41573891
26. PMID:41525888
27. PMID:38891774
28. PMID:25656065
29. PMID:36745687
30. PMID:38325718
31. PMID:34997540
32. PMID:38451707
33. PMID:34975400
34. PMID:34173837
35. PMID:27455348
