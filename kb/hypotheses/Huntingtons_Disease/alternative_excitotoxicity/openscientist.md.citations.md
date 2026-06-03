# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Huntington's Disease
- **Category:** Genetic

## Target Hypothesis
- **Hypothesis ID:** alternative_excitotoxicity
- **Hypothesis Label:** NMDA Receptor-Mediated Excitotoxicity
- **Status in KB:** ALTERNATIVE

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: alternative_excitotoxicity
hypothesis_label: NMDA Receptor-Mediated Excitotoxicity
status: ALTERNATIVE
description: |
  Historical but still supported superimposed model proposing that mutant huntingtin and corticostriatal circuit dysfunction enhance NMDA receptor-mediated excitotoxicity in striatal medium spiny neurons. This hypothesis is best viewed as a selective-vulnerability amplifier rather than the sole initiating lesion.
evidence:
- reference: PMID:17188796
  supports: SUPPORT
  evidence_source: OTHER
  snippet: Many lines of evidence support a role for neuronal damage arising as a result of excessive
    activation of glutamate receptors by excitatory amino acids in the pathogenesis of Huntington disease.
    The N-methyl-d-aspartate subclass of ionotropic glutamate receptors (NMDARs) is more selective and
    effective than the other subclasses in mediating this damage.
  explanation: Comprehensive review establishing NMDAR-mediated excitotoxicity as a key pathogenic mechanism
    in HD with evidence from human tissue, animal models, and cell-based systems.
- reference: PMID:19279257
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: This is the first direct in vivo evidence of NR2B-NMDAR-mediated excitotoxicity in the context
    of HD. Our results are consistent with previous suggestions that direct and/or indirect interactions
    of mutant huntingtin with NMDARs are a proximate cause of neurodegeneration in HD.
  explanation: Provides the first direct in vivo genetic evidence for the excitotoxicity hypothesis by
    showing exacerbated striatal neurodegeneration when NR2B-NMDAR subunits are overexpressed in an HD
    mouse model.
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
**Generated:** 2026-05-23T05:06:10.340393

1. PMID:22668780
2. PMID:22523092
3. PMID:19726651
4. PMID:19279257
5. PMID:38776957
6. PMID:33250715
7. PMID:22198502
8. PMID:39938516
9. PMID:38749429
10. PMID:38387080
11. PMID:36517241
12. PMID:33198566
13. PMID:33016873
14. PMID:1710657
15. PMID:2563916
16. PMID:9100675
17. PMID:40461488
18. PMID:19168136
19. PMID:15717010
20. PMID:11554551
21. PMID:24204323
22. PMID:30502498
23. PMID:41578740
24. PMID:32642868
25. PMID:26282324
26. PMID:29254102
27. PMID:32004439
28. PMID:39170678
29. PMID:28099414
30. PMID:21539755
31. PMID:23994717
32. PMID:30666558
33. PMID:29794227
34. PMID:29121220
