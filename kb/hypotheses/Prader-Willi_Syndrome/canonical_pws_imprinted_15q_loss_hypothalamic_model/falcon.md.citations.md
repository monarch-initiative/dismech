# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Prader-Willi Syndrome
- **Category:** Mendelian

## Target Hypothesis
- **Hypothesis ID:** canonical_pws_imprinted_15q_loss_hypothalamic_model
- **Hypothesis Label:** Canonical 15q11.2-q13 Paternal Imprinted Locus Loss / Hypothalamic Dysfunction Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_pws_imprinted_15q_loss_hypothalamic_model
hypothesis_label: Canonical 15q11.2-q13 Paternal Imprinted Locus Loss / Hypothalamic Dysfunction Model
status: CANONICAL
description: 'Prader-Willi syndrome is caused by loss of paternally-expressed imprinted genes in the 15q11.2-q13
  region — most commonly by paternal deletion (~70%), maternal uniparental disomy (~25%), or imprinting
  center defect (~3%). Loss of paternal expression of SNRPN, MAGEL2, MKRN3, NDN, and the SNORD116 snoRNA
  cluster disrupts hypothalamic neurodevelopment and function, producing the characteristic biphasic phenotype:
  neonatal hypotonia and failure to thrive followed in early childhood by hyperphagia, morbid obesity,
  hypogonadotropic hypogonadism, short stature, intellectual disability, and behavioral/psychiatric features.
  SNORD116 paternal deletion alone is sufficient to produce the core PWS phenotype, identifying it as
  the critical region. Growth hormone therapy improves body composition and stature; oxytocin and MC4R-targeted
  setmelanotide therapies are in trials; MAGEL2-knockout mice recapitulate hypothalamic dysfunction and
  validate the imprinted-locus / hypothalamic-axis model.'
evidence:
- reference: PMID:40708003
  reference_title: Prader-Willi syndrome.
  supports: SUPPORT
  evidence_source: OTHER
  snippet: Prader-Willi syndrome (PWS) is a rare, genetic neurobehavioral and metabolic disorder marked
    by hyperphagia, behavioral challenges, and significant comorbidities, requiring a multidisciplinary
    approach for effective management.
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

**Provider:** falcon
**Generated:** 2026-05-25T14:00:12.989140

1. salminen2023geneticandevolutionary pages 82-87
2. gilmore2024identifyingkeyunderlying pages 10-11
3. salles2024differentialdnamethylation pages 1-5
4. sarkar2024clinicalefficacylandscaping pages 27-30
5. pascut2024characterizationofcirculating pages 1-2
6. sanchez2023hormonalimbalancesin pages 1-4
7. sohn2023updatesonobesity pages 4-6
8. correadasilva2024microglialphagolysosomedysfunction pages 1-2
9. correadasilva2024microglialphagolysosomedysfunction pages 6-9
10. correadasilva2024microglialphagolysosomedysfunction pages 9-10
11. hoybye2025theroleof pages 4-6
12. hoybye2025theroleof pages 2-4
13. butler2025barrierslimitationsand pages 4-5
14. hoybye2025theroleof pages 9-10
15. pascut2024characterizationofcirculating pages 7-11
16. lipka2025advancingtherapeuticstrategies pages 18-21
17. madeo2024endocrinefeaturesof pages 10-11
18. madeo2024endocrinefeaturesof pages 2-3
19. https://doi.org/10.1007/s00401-024-02714-0
20. https://doi.org/10.1093/nar/gkae1129
21. https://doi.org/10.1038/s41380-024-02542-4
22. https://doi.org/10.3390/jcm13195697
23. https://doi.org/10.3390/ijms241713109
24. https://doi.org/10.3389/fendo.2024.1382583
25. https://doi.org/10.1155/2023/4225092
26. https://doi.org/10.3390/cimb47030192
27. https://clinicaltrials.gov/study/NCT02311673
28. https://doi.org/10.12771/emj.2023.e33
29. https://doi.org/10.1101/2024.08.02.24311335
30. https://doi.org/10.1007/s00401-024-02714-0.
31. https://doi.org/10.1155/2023/4225092.
32. https://doi.org/10.1093/nar/gkae1129.
33. https://doi.org/10.3390/jcm13195697.
34. https://doi.org/10.1155/2023/4225092,
35. https://doi.org/10.1007/s00401-024-02714-0,
36. https://doi.org/10.1093/nar/gkae1129,
37. https://doi.org/10.1038/s41380-024-02542-4,
38. https://doi.org/10.3390/cimb47030192,
39. https://doi.org/10.12771/emj.2023.e33,
40. https://doi.org/10.3390/genes16121436,
41. https://doi.org/10.3390/jcm13195697,
42. https://doi.org/10.1101/2024.08.02.24311335,
43. https://doi.org/10.3390/ijms241713109,
44. https://doi.org/10.3389/fendo.2024.1382583,
