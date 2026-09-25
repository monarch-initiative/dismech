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
- **Hypothesis ID:** canonical_transcriptional_dysregulation
- **Hypothesis Label:** Transcriptional Dysregulation
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_transcriptional_dysregulation
hypothesis_label: Transcriptional Dysregulation
status: CANONICAL
description: |
  Mutant huntingtin disrupts transcriptional regulation by sequestering key transcription factors and co-activators (Sp1, CBP, REST/NRSF), leading to widespread downregulation of neuronal survival genes including BDNF. This is a canonical downstream mechanistic layer in HD, linking mutant huntingtin protein interactions to loss of neuronal maintenance programs.
evidence:
- reference: PMID:11839795
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: In HD transgenic mice (R6/2) that express N-terminal-mutant huntingtin, Sp1 binds to the soluble
    form of mutant huntingtin but not to aggregated huntingtin.
  explanation: In vivo evidence from HD transgenic mice showing that Sp1 binds soluble mutant huntingtin,
    supporting the sequestration mechanism.
- reference: PMID:11839795
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: Mutant huntingtin inhibits the binding of nuclear Sp1 to the promoter of nerve growth factor
    receptor and suppresses its transcriptional activity in cultured cells.
  explanation: Cell culture experiments demonstrating that mutant huntingtin suppresses Sp1-regulated
    transcription.
- reference: PMID:11264541
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: We found that CBP was depleted from its normal nuclear location and was present in polyglutamine
    aggregates in HD cell culture models, HD transgenic mice, and human HD postmortem brain.
  explanation: HD cell culture models showing CBP depletion from its normal nuclear location and sequestration
    into polyglutamine aggregates.
- reference: PMID:11264541
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: We found that CBP was depleted from its normal nuclear location and was present in polyglutamine
    aggregates in HD cell culture models, HD transgenic mice, and human HD postmortem brain.
  explanation: HD transgenic mice confirming CBP sequestration into polyglutamine aggregates in vivo.
- reference: PMID:11264541
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: We found that CBP was depleted from its normal nuclear location and was present in polyglutamine
    aggregates in HD cell culture models, HD transgenic mice, and human HD postmortem brain.
  explanation: Human HD postmortem brain tissue showing CBP depletion and sequestration into polyglutamine
    aggregates.
- reference: PMID:12881722
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: aberrant accumulation of REST/NRSF in the nucleus is present in Huntington disease. We show
    that wild-type huntingtin coimmunoprecipitates with REST/NRSF and that less immunoprecipitated material
    is found in brain tissue with Huntington disease.
  explanation: Human postmortem brain data showing aberrant nuclear REST/NRSF accumulation and reduced
    huntingtin-REST/NRSF interaction in HD.
- reference: PMID:12881722
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: loss of expression of NRSE-controlled neuronal genes is shown in cells, mice and human brain
    with Huntington disease.
  explanation: Mouse model data confirming loss of NRSE-controlled gene expression in HD, corroborating
    the REST/NRSF dysregulation mechanism.
- reference: PMID:12881722
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: Wild-type huntingtin inhibits the silencing activity of NRSE, increasing transcription of BDNF.
    We show that this effect occurs through cytoplasmic sequestering of repressor element-1 transcription
    factor/neuron restrictive silencer factor (REST/NRSF), the transcription factor that binds to NRSE.
  explanation: Cell-based experiments showing wild-type huntingtin sequesters REST/NRSF in the cytoplasm
    to permit BDNF transcription, a function lost with the mutant protein.
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
**Generated:** 2026-05-23T05:11:45.601810

1. PMID:11971872
2. PMID:15225551
3. PMID:39938516
4. PMID:11988536
5. PMID:11839795
6. PMID:11264541
7. PMID:16766198
8. PMID:12881722
9. PMID:17596446
10. PMID:23800350
11. PMID:21832040
12. PMID:40490511
13. PMID:39937881
14. PMID:28593442
15. PMID:23455440
16. PMID:33679321
17. PMID:28729730
18. PMID:31696228
19. PMID:32681824
20. PMID:34215255
21. PMID:40482637
22. PMID:30451892
23. PMID:23575829
24. PMID:34011527
25. PMID:33655829
26. PMID:28819135
27. PMID:14522959
28. PMID:19168136
29. PMID:18279698
30. PMID:27601642
31. PMID:39394467
32. PMID:41841355
