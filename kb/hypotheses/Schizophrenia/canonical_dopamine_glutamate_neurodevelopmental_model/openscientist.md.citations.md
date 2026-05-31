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
- **Hypothesis ID:** canonical_dopamine_glutamate_neurodevelopmental_model
- **Hypothesis Label:** Canonical Dopamine / Glutamate / Neurodevelopmental Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_dopamine_glutamate_neurodevelopmental_model
hypothesis_label: Canonical Dopamine / Glutamate / Neurodevelopmental Model
status: CANONICAL
description: Schizophrenia is a polygenic neurodevelopmental disorder in which rare large-effect (e.g.,
  22q11.2 deletion, NRXN1, SETD1A) and common variants (>250 GWAS loci) converge on synaptic, dopaminergic,
  and glutamatergic pathways. Striatal dopamine D2-receptor hyperactivity drives positive symptoms (psychosis,
  hallucinations); cortical NMDA-receptor hypofunction and parvalbumin-interneuron dysfunction produce
  negative and cognitive symptoms. Aberrant synaptic pruning during adolescence (C4-complement-driven)
  and altered early-life neurodevelopment provide the substrate for later-onset psychotic phenotypes.
  Antipsychotic efficacy (all first-line drugs are D2 antagonists) and NMDA- channel-blocker models (ketamine,
  PCP) corroborate the dopamine-glutamate axis as the canonical pharmacologic substrate.
evidence:
- reference: PMID:11532718
  reference_title: The emerging role of glutamate in the pathophysiology and treatment of schizophrenia.
  supports: SUPPORT
  evidence_source: OTHER
  snippet: Research has implicated dysfunction of glutamatergic neurotransmission in the pathophysiology
    of schizophrenia.
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
**Generated:** 2026-05-24T15:46:10.106159

1. PMID:29301039
2. PMID:21768612
3. PMID:36979877
4. PMID:27857125
5. PMID:34789848
6. PMID:31135051
7. PMID:32827700
8. PMID:42000733
9. PMID:38898401
10. PMID:41986308
11. PMID:39018984
12. PMID:32681171
13. PMID:38490084
14. PMID:40436282
15. PMID:41506001
16. PMID:41868713
17. PMID:25539791
18. PMID:40908273
19. PMID:40162239
20. PMID:41422157
21. PMID:40962831
22. PMID:36581615
23. PMID:37519478
24. PMID:20143199
25. PMID:32719622
26. PMID:35396580
27. PMID:34035170
28. PMID:25756805
29. PMID:22238649
30. PMID:41413202
31. PMID:33190236
32. PMID:38685343
33. PMID:19198118
34. PMID:26134644
35. PMID:40236399
36. PMID:19689327
37. PMID:34875009
38. PMID:40952174
39. PMID:31192814
40. PMID:40635756
41. PMID:34819729
42. PMID:41326319
43. PMID:41233083
44. PMID:37543251
45. PMID:41418563
46. PMID:40098750
47. PMID:38110609
