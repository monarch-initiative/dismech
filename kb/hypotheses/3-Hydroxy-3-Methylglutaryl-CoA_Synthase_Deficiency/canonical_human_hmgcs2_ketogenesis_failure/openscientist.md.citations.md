# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency
- **Category:** Mendelian

## Target Hypothesis
- **Hypothesis ID:** canonical_hmgcs2_ketogenesis_failure_model
- **Hypothesis Label:** Canonical HMGCS2 Ketogenesis Failure Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_hmgcs2_ketogenesis_failure_model
hypothesis_label: Canonical HMGCS2 Ketogenesis Failure Model
status: CANONICAL
description: |
  Biallelic HMGCS2 pathogenic variants reduce mitochondrial hydroxymethylglutaryl-CoA synthase activity in hepatocytes. During fasting or illness, fatty acid beta-oxidation supplies acetyl-CoA but defective HMGCS2 blocks conversion of acetyl-CoA and acetoacetyl-CoA into HMG-CoA, the rate-limiting step in ketone body synthesis. The liver therefore fails to produce adequate ketone bodies when glucose availability falls, producing hypoketotic hypoglycemia and a characteristic acute-phase metabolite pattern including dicarboxylic aciduria, 4HMP excretion, and elevated C2/C0 acylcarnitine ratio.
evidence:
- reference: PMID:32952630
  reference_title: 'Japanese patients with mitochondrial 3-hydroxy-3-methylglutaryl-CoA synthase deficiency:
    In vitro functional analysis of five novel HMGCS2 mutations.'
  supports: SUPPORT
  evidence_source: OTHER
  snippet: which is the rate-limiting step of ketone body synthesis
  explanation: This review statement places HMGCS2 at the rate-limiting step of ketogenesis.
- reference: PMID:39798988
  reference_title: Mitochondrial HMG-CoA synthase deficiency.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: mutations in the HMGCS2 gene, leading to impaired ketogenesis.
  explanation: The systematic review links HMGCS2 mutations to impaired ketogenesis.
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
**Generated:** 2026-05-23T02:15:31.641601

1. PMID:39798988
2. PMID:40515583
3. PMID:33619377
4. PMID:35421611
5. PMID:40272888
6. PMID:32952630
7. PMID:32905056
8. PMID:40004108
9. PMID:40937626
10. PMID:38876267
11. PMID:40692014
12. PMID:40548098
13. PMID:41383544
14. PMID:33045405
15. PMID:37931961
16. PMID:28512002
17. PMID:41960367
18. PMID:40960113
19. PMID:40199742
20. PMID:35224990
21. PMID:41568909
22. PMID:35943247
23. PMID:37503004
24. PMID:32259399
25. PMID:32726607
26. PMID:36220812
27. PMID:29030856
28. PMID:38469099
