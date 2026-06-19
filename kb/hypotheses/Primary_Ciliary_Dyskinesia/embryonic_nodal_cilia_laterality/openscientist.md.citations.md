# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Primary_Ciliary_Dyskinesia
- **Category:** Genetic

## Target Hypothesis
- **Hypothesis ID:** embryonic_nodal_cilia_laterality
- **Hypothesis Label:** Embryonic Nodal-Cilia Laterality-Determination Arm
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: embryonic_nodal_cilia_laterality
hypothesis_label: Embryonic Nodal-Cilia Laterality-Determination Arm
status: CANONICAL
description: 'A mechanistically distinct, organ-specific arm of the same motile-cilia defect: motile monocilia
  at the embryonic node normally generate a leftward fluid flow that establishes left-right body asymmetry.
  When the shared axonemal defect immobilizes nodal cilia, laterality is randomized, so roughly half of
  patients develop situs inversus totalis (or situs ambiguus/heterotaxy). This explains why laterality
  defects segregate with the respiratory phenotype yet affect only ~50% of patients (random, not obligate,
  mislateralization).'
evidence:
- reference: PMID:16036877
  reference_title: 'Primary ciliary dyskinesia: a review.'
  supports: SUPPORT
  snippet: The normal left-right asymmetry of the body is thought to be due to the beating of the cilia
    in the embryonic (Hensen's) node. Total immotility of the cilia should therefore result in random
    asymmetry of the body that is situs inversus in 50% of the cases.
  explanation: Supports the nodal-cilia leftward-flow model and the ~50% random laterality outcome.
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
**Generated:** 2026-06-19T18:49:22.715981

1. PMID:12097914
2. PMID:16035921
3. PMID:17515466
4. PMID:24577564
5. PMID:9353118
6. PMID:10556073
7. PMID:22983710
8. PMID:21307093
9. PMID:23357539
10. PMID:30471718
11. PMID:30471717
12. PMID:38871375
13. PMID:34102041
14. PMID:26777464
15. PMID:42185991
16. PMID:41570615
17. PMID:32788551
18. PMID:32571625
19. PMID:27305836
20. PMID:24518672
21. PMID:24568568
22. PMID:38602513
23. PMID:34133086
24. PMID:37477290
25. PMID:25504577
26. PMID:20126399
27. PMID:27486780
28. PMID:22554696
29. PMID:15889083
30. PMID:40467998
31. PMID:29769531
32. PMID:30139971
33. PMID:24226769
34. PMID:25048963
35. PMID:19879143
36. PMID:20884020