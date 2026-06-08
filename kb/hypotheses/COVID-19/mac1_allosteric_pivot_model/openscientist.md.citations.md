# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** COVID-19
- **Category:**

## Target Hypothesis
- **Hypothesis ID:** mac1_allosteric_pivot_model
- **Hypothesis Label:** Mac1 Allosteric Conformational Pivot Model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: mac1_allosteric_pivot_model
hypothesis_label: Mac1 Allosteric Conformational Pivot Model
status: EMERGING
description: The conserved Mac1 fold across coronaviruses (SARS-CoV-2, SARS-CoV, MERS-CoV) supports treating
  Mac1 as a thermodynamic pivot point rather than only an active-site target. Allosteric stabilization
  of distinct Mac1 conformational states or PROTAC-based physical degradation would rebalance the host
  interactome toward antiviral ADP-ribosylation, with potential broad anti-coronavirus activity that active-site
  inhibition alone may not achieve. Active drug-discovery programs (including the third CACHE community
  challenge) have established Mac1 as a tractable structural target with hundreds of crystallographically
  characterized ligands, providing a strong starting point for conformational-pivot chemistry.
evidence:
- reference: PMID:33158944
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: SARS-CoV-2, SARS-CoV, and Middle East respiratory syndrome coronavirus (MERS-CoV) Mac1 domains
    exhibit similar structural folds, and all 3 proteins bound to ADP-ribose with affinities in the low
    micromolar range
  explanation: Structural conservation of Mac1 across coronaviruses supports the feasibility of a pan-CoV
    pivot-control strategy beyond active-site inhibition.
- reference: PMID:40964377
  supports: SUPPORT
  evidence_source: COMPUTATIONAL
  snippet: Significant efforts have been recently dedicated to the discovery of small molecule inhibitors
    against the Macrodomain 1 (Mac1) of nonstructural protein 3 (NSP3) as potential antivirals for SARS-CoV-2.
  explanation: Ban et al. and the CACHE3 challenge directly demonstrate that Mac1 is an active drug-discovery
    target with community-wide investment, supporting the feasibility of allosteric and PROTAC-warhead
    programs.
- reference: PMID:40964377
  supports: SUPPORT
  evidence_source: COMPUTATIONAL
  snippet: Our results illustrate the effectiveness of ML-accelerated docking to rapidly identify novel
    chemical series and provide a strong foundation for the development of SARS-CoV-2 NSP3 Mac1 inhibitors.
  explanation: The community-level chemistry infrastructure for Mac1 hit-finding lowers the experimental
    barrier for the proposed Mac1 conformational pivot experiment.
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
**Generated:** 2026-05-27T00:18:21.163476

1. PMID:38260573
2. PMID:36598939
3. PMID:28991428
4. PMID:37607224
5. PMID:27965448
6. PMID:37066301
7. PMID:39229055
8. PMID:41258893
9. PMID:39554145
10. PMID:40407321
11. PMID:41820535
12. PMID:40736256
13. PMID:30918076
14. PMID:29567296
15. PMID:41279050
16. PMID:41780340
17. PMID:41536548
18. PMID:41189073
19. PMID:36841740
20. PMID:37196358
21. PMID:33158944
22. PMID:34686999
23. PMID:41565251
24. PMID:31095648
25. PMID:32511412
26. PMID:40871554
27. PMID:40462918
28. PMID:41279697
29. PMID:41979330
