# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Myotonic Dystrophy Type 1
- **Category:** Mendelian

## Target Hypothesis
- **Hypothesis ID:** canonical_dmpk_ctg_rna_toxicity_splicing_dysregulation_model
- **Hypothesis Label:** Canonical DMPK CTG Expansion / RNA Toxicity / Splicing Dysregulation Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_dmpk_ctg_rna_toxicity_splicing_dysregulation_model
hypothesis_label: Canonical DMPK CTG Expansion / RNA Toxicity / Splicing Dysregulation Model
status: CANONICAL
description: Myotonic dystrophy type 1 (DM1) is caused by CTG-trinucleotide repeat expansion (>50 repeats;
  severe congenital >1000) in the 3' UTR of DMPK on 19q13.3. Expanded CUG-repeat RNA transcripts form
  nuclear foci that sequester MBNL1 (muscleblind-like 1) splicing factor and induce aberrant upregulation
  of CELF1, producing dysregulated alternative splicing of >100 developmentally regulated transcripts
  (e.g., CLCN1, INSR, SCN5A, BIN1). Mis-splicing reverts adult-tissue isoforms toward embryonic patterns,
  producing myotonia (CLCN1), insulin resistance (INSR), cardiac conduction defects (SCN5A), muscle weakness
  and atrophy, cataracts, frontal balding, hypogonadism, and characteristic CNS involvement. CTG repeat
  instability drives intergenerational anticipation. MBNL transgenic rescue, CUG-ASO therapy, and small-molecule
  MBNL/CELF1 normalizers corroborate the RNA-toxicity / splicing- dysregulation axis as the canonical
  pathogenic mechanism.
evidence:
- reference: PMID:31326502
  reference_title: Myotonic Dystrophy type 1.
  supports: SUPPORT
  evidence_source: OTHER
  snippet: Myotonic Dystrophy type 1 (DM1) is a neuromuscular disease showing strong genetic anticipation,
    and is caused by the expansion of a CTG repeat tract in the 3'-UTR of the DMPK gene.
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
**Generated:** 2026-05-24T17:15:02.259238

1. PMID:25761764
2. PMID:16864772
3. PMID:31253581
4. PMID:19223393
5. PMID:39126705
6. PMID:41855125
7. PMID:22062891
8. PMID:17101631
9. PMID:31853004
10. PMID:17158949
11. PMID:11528389
12. PMID:21623381
13. PMID:27063795
14. PMID:21484823
15. PMID:36804094
16. PMID:37744174
17. PMID:35567413
18. PMID:40238630
19. PMID:15546872
20. PMID:17936705
21. PMID:21400563
22. PMID:22453899
23. PMID:37029100
24. PMID:24185704
25. PMID:31220271
26. PMID:26994442
27. PMID:34371182
28. PMID:41722569
29. PMID:40238915
30. PMID:39180495
31. PMID:19246640
32. PMID:19207265
33. PMID:39710919
34. PMID:23139243
35. PMID:40599975
36. PMID:39258536
37. PMID:41621483
38. PMID:23209425
39. PMID:35274098
40. PMID:41848171
41. PMID:22884328
42. PMID:10021468
43. PMID:36724941
44. PMID:42003432
45. PMID:41285302
46. PMID:34432028
47. PMID:28102759
48. PMID:26756355
