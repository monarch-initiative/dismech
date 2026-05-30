# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Duchenne Muscular Dystrophy
- **Category:** Genetic

## Target Hypothesis
- **Hypothesis ID:** canonical_dystrophin_loss_membrane_fragility_model
- **Hypothesis Label:** Canonical Dystrophin Loss and Membrane Fragility Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_dystrophin_loss_membrane_fragility_model
hypothesis_label: Canonical Dystrophin Loss and Membrane Fragility Model
status: CANONICAL
description: Out-of-frame DMD variants abolish functional dystrophin, the cytoskeletal link between cytoplasmic
  F-actin and the sarcolemmal dystrophin-glycoprotein complex (DGC). Without dystrophin the DGC is destabilized
  at the sarcolemma, leaving muscle fibers vulnerable to contraction-induced mechanical injury, calcium
  influx through stretched/damaged membrane, and activation of calcium-dependent proteases. Repeated cycles
  of fiber necrosis, satellite-cell-driven regeneration, chronic inflammation, and progressive fibro-fatty
  replacement of muscle ultimately exhaust regenerative capacity, producing the characteristic progressive
  proximal weakness, cardiomyopathy, respiratory failure, and short life expectancy of Duchenne muscular
  dystrophy. Exon-skipping and gene-replacement therapies that restore even partial dystrophin expression
  provide interventional validation of this canonical chain.
evidence:
- reference: PMID:16770791
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: severe Duchenne and milder Becker muscular dystrophy are both caused by mutations
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

**Provider:** falcon
**Generated:** 2026-05-23T19:03:11.288051

1. zhou2024systemicdeliveryof pages 1-2
2. russell2023modulatingfastskeletal pages 1-2
3. matsumura2011stretchactivatedcalciumchannel pages 1-2
4. millay2009calciuminfluxis pages 1-2
5. burr2015geneticevidencein pages 5-6
6. head2010branchedfibresin pages 1-2
7. hahn2023rapidrestitutionof pages 1-2
8. dambrosio2023evolvingtherapeuticoptions pages 8-9
9. gandhi2024cardiomyopathyinduchenne pages 2-4
10. boehler2024nterminaltitinfragment pages 1-2
11. roberts2023therapeuticapproachesfor pages 12-15
12. lorin2015dystrophiccardiomyopathyrole pages 11-13
13. gandhi2024mitochondriainduchenne pages 3-5
14. https://doi.org/10.1038/s41467-024-50569-6
15. https://doi.org/10.1172/jci153837
16. https://doi.org/10.1152/ajpcell.00056.2011
17. https://doi.org/10.1073/pnas.0906591106
18. https://doi.org/10.1038/cdd.2015.65
19. https://doi.org/10.1113/expphysiol.2009.052019
20. https://doi.org/10.1186/s13395-023-00318-y
21. https://doi.org/10.1007/s13311-023-01423-y
22. https://doi.org/10.1002/mus.27955
23. https://doi.org/10.1186/s13395-023-00334-y
24. https://clinicaltrials.gov/study/NCT03769116
25. https://doi.org/10.1038/s41573-023-00775-6
26. https://doi.org/10.3390/cells13141168
27. https://doi.org/10.1172/jci153837,
28. https://doi.org/10.1186/s13395-023-00318-y,
29. https://doi.org/10.1073/pnas.0906591106,
30. https://doi.org/10.1002/mus.27955,
31. https://doi.org/10.1186/s13395-023-00334-y,
32. https://doi.org/10.1038/s41467-024-50569-6,
33. https://doi.org/10.1007/s13311-023-01423-y,
34. https://doi.org/10.1038/cdd.2015.65,
35. https://doi.org/10.1113/expphysiol.2009.052019,
36. https://doi.org/10.1093/cvr/cvv021,
37. https://doi.org/10.1152/ajpcell.00056.2011,
38. https://doi.org/10.1038/s41573-023-00775-6,
39. https://doi.org/10.3390/cells13141168,
40. https://doi.org/10.20944/preprints202401.2158.v1,
