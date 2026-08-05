# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Alpha-gal Syndrome
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** tick_salivary_constituent_sensitization
- **Hypothesis Label:** Tick-Intrinsic Salivary Constituent Model
- **Status in KB:** ALTERNATIVE

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: tick_salivary_constituent_sensitization
hypothesis_label: Tick-Intrinsic Salivary Constituent Model
status: ALTERNATIVE
description: The anti-alpha-gal IgE response is induced by normal, tick-derived constituents of tick saliva.
  Contemporary work supports ticks synthesizing alpha-gal via their own galactosyltransferases and presenting
  it (with Th2- skewing salivary factors) at the bite site, so the sensitizing antigen is intrinsic to
  the tick rather than borrowed.
evidence:
- reference: PMID:25747720
  reference_title: 'The alpha-gal story: lessons learned from connecting the dots.'
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: That the response is induced by the normal (i.e. tick derived) constituents of their saliva.
  explanation: States the tick-intrinsic salivary-constituent theory as one of the competing explanations
    for alpha-gal sensitization.
- reference: PMID:38390396
  reference_title: Tick bite-induced alpha-gal syndrome and immunologic responses in an alpha-gal deficient
    murine model.
  supports: PARTIAL
  evidence_source: MODEL_ORGANISM
  snippet: Gene expression analysis revealed that Am. americanum bites direct mouse immunity toward Th2
    and facilitate host sensitization to the α-gal antigen.
  explanation: The AGKO-mouse model shows lone-star tick bites themselves drive Th2 polarization and alpha-gal
    sensitization, consistent with a tick-intrinsic route.
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
**Generated:** 2026-07-05T14:15:11.616354

1. PMID:30242261
2. PMID:39053323
3. PMID:38741222
4. PMID:34034363
5. PMID:38390396
6. PMID:40485140
7. PMID:35382677
8. PMID:34904495
9. PMID:41317280
10. PMID:42245641
11. PMID:29319188
12. PMID:41949618
13. PMID:23414348
14. PMID:41785334
15. PMID:40817895
16. PMID:25747720
17. PMID:42391055
18. PMID:21453959
19. PMID:42343501
20. PMID:37468955
21. PMID:33988703
22. PMID:38193233
23. PMID:29903734