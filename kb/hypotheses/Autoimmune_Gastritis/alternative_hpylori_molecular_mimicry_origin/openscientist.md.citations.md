# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Autoimmune Gastritis
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** alternative_hpylori_molecular_mimicry_origin
- **Hypothesis Label:** Alternative H. pylori Molecular-Mimicry ("Hit-and-Run") Origin
- **Status in KB:** ALTERNATIVE

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: alternative_hpylori_molecular_mimicry_origin
hypothesis_label: Alternative H. pylori Molecular-Mimicry ("Hit-and-Run") Origin
status: ALTERNATIVE
description: Autoimmune gastritis is initiated by Helicobacter pylori infection via molecular mimicry
  between H. pylori antigens and the gastric H+/K+ ATPase, generating cross-reactive T- and B-cell responses
  that, through epitope spreading and bystander activation in a genetically susceptible host, become self-perpetuating
  autoimmunity and persist after the organism is cleared (established AIG is frequently H. pylori-negative).
  A corollary is that a subset of cases are reversible with early eradication. Causation in humans remains
  unproven and is the basis of a knowledge-gap discussion.
evidence:
- reference: PMID:21174235
  reference_title: Cutting edge issues in autoimmune gastritis.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: a role for Helicobacter pylori as an infective trigger through molecular mimicry
  explanation: States H. pylori as a candidate infective trigger of autoimmune gastritis via molecular
    mimicry.
- reference: PMID:42254085
  reference_title: 'Pernicious Anemia and Helicobacter pylori Infection: What a Hematologist Needs to
    Know?'
  supports: PARTIAL
  evidence_source: HUMAN_CLINICAL
  snippet: Rapid eradication of H. pylori can significantly improve hematologic parameters and prevent
    the progression of autoimmune gastritis.
  explanation: A reversible, H. pylori-attributable presentation is consistent with an infection-triggered
    origin in a subset of cases.
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
**Generated:** 2026-07-01T15:00:08.716366

1. PMID:14568977
2. PMID:11159878
3. PMID:15242679
4. PMID:15866204
5. PMID:7599605
6. PMID:8675304
7. PMID:10654796
8. PMID:36742095
9. PMID:10809040
10. PMID:11815766
11. PMID:11225441
12. PMID:10738313
13. PMID:10077749
14. PMID:41484031
15. PMID:38976374
16. PMID:15763991
17. PMID:15147343
18. PMID:26405069
19. PMID:34003463
20. PMID:41963817
21. PMID:41867096
22. PMID:11549834
23. PMID:9773482
24. PMID:9432348
25. PMID:29920721
26. PMID:42106905
27. PMID:27538411
28. PMID:19786202
29. PMID:39854274
30. PMID:41670890
31. PMID:9026476
32. PMID:41425574
33. PMID:37885562
34. PMID:15763993
35. PMID:35772926