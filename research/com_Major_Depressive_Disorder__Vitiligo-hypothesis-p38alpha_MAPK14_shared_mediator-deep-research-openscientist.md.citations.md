# Citations for Research Query

**Query:** # Focused Mechanistic Hypothesis Search: MDD–Vitiligo p38α/MAPK14 Shared Mediator

This is a focused hypothesis investigation for DisMech issue #5921, not a general overview of either disease.

## Authoritative disease identities and scope

- Major depressive disorder (MDD): MONDO:0002009, “major depressive disorder.”
- Vitiligo: MONDO:0008661, the autoimmune melanocyte-destruction disorder. Prioritize acquired generalized/nonsegmental vitiligo, while explicitly stratifying segmental or other subtypes when a source does not study the same entity.
- Search literature available through 2026-07-26.

Do not treat depressive symptoms, distress questionnaire scores, other mental disorders, or rodent “depression-like behavior” as equivalent to clinically diagnosed human MDD. Do not treat leukoderma, melanoma-associated depigmentation, chemical leukoderma, or other inflammatory skin diseases as vitiligo. Evidence about only one disease is not evidence of a shared MDD–vitiligo mechanism.

## Seed hypothesis

Hypothesis ID: `mdd_vitiligo_acquired_mapk14_shared_mediator`

Status: unresolved, hypothesis-generating pair-level knowledge gap; not an established DisMech pathophysiology node or conserved module.

An acquired, cell-state-specific inflammatory program involving p38α/MAPK14 may act as a shared mediator of MDD–vitiligo comorbidity. Candidate compartments include peripheral immune cells; serotonergic neurons, microglia, or astrocytes relevant to MDD; and melanocytes, keratinocytes, dendritic cells, or cytotoxic T cells relevant to vitiligo. A genuine shared mediator would require evidence that a defined MAPK14-dependent state, or a causally connected cross-compartment program, precedes and contributes to both disease outcomes. Mere MAPK14 RNA expression in separate tissues, generic phospho-p38 activation, or independent use of p38 signaling in unrelated cell types would instead support a correlated marker or parallel tissue-specific models.

## Seed evidence requiring critical audit

1. PMID:42418414 computationally compared separate disease datasets:
   - MDD GSE98793: 128 MDD and 64 control whole-blood samples.
   - Vitiligo GSE65127 plus GSE53146: 15 vitiligo and 15 control samples after integration.
   - Differential-expression threshold was any nonzero |log2FC| with nominal P < 0.05.
   - Immune-cell results were ssGSEA enrichment signatures, not measured cell abundance.
   - MAPK14 was selected as a candidate marker through differential expression, PPI/network analysis, and machine-learning feature selection.
   - There was no explicitly ascertained comorbid cohort, paired skin/blood/brain material from the same participants, direct MAPK14 activity assay, or causal perturbation.
   - The authors explicitly characterize the result as hypothesis-generating.

2. PMID:30528503 reports adjusted temporal associations in both directions:
   - MDD preceding vitiligo: HR 1.64, 95% CI 1.43–1.87.
   - Vitiligo preceding MDD: HR 1.31 before age 30 and HR 1.22 at age 30 or older.
   These estimates establish association and temporal ordering of recorded diagnoses, not mediation.

3. DOI:10.1111/exd.14979 reports no significant bidirectional Mendelian-randomization effect between generalized vitiligo and the study’s broad mental-disorder/depression phenotypes. This constrains the tested genetically instrumented disease-to-disease directions but does not test shared pleiotropic liability, acquired mechanisms, weak effects, or clinically defined MDD subgroups.

4. PMID:41781039 reports a mental-health comorbidity profile in vitiligo largely comparable to atopic dermatitis, challenging vitiligo specificity.

5. PMID:21835346 shows that serotonergic-neuron-selective p38α deletion changes stress-related behavior in mice. It is model-organism evidence for a neural p38α route, not human MDD or cross-disease evidence.

6. PMID:18575770 reports H2O2-induced JNK and p38 activation in cultured mouse melanocytes. It is not MAPK14-specific and does not establish a shared human mechanism.

Retrieve and assess the primary papers rather than treating PMID:42418414’s narrative citations as independent proof.

## Central question

Does current evidence support an acquired, MAPK14-specific, cell-state-resolved causal mediator shared by MDD and vitiligo, or is the observed comorbidity better explained by one or more of the following models?

1. Psychosocial mediation from visible skin disease, stigma, distress, reduced quality of life, or chronic stress.
2. Healthcare-surveillance, diagnostic-contact, or treatment effects.
3. Nonspecific systemic inflammatory burden shared with many inflammatory diseases.
4. Shared pleiotropic genetic liability independently increasing both risks.
5. Directional causation:
   - MDD or chronic stress causing or exacerbating vitiligo.
   - Vitiligo causing MDD through psychosocial or biological routes.
6. Parallel tissue-specific p38 models in which p38α has separate upstream triggers, cellular locations, substrates, and consequences in brain and skin, without one shared mediator.

## Required investigation

### 1. Audit the seed computational result

Determine whether MAPK14 differential expression and direction replicate in genuinely independent MDD and vitiligo datasets after appropriate multiple-testing correction and meaningful effect-size thresholds. Check:

- Original tissues, platforms, diagnostic definitions, treatments, disease activity, demographics, batch correction, sample overlap, and cell-composition confounding for GSE98793, GSE65127, GSE53146, GSE52790, and GSE80009.
- Whether external validation was statistically independent of feature selection.
- MAPK14 effect direction and magnitude, confidence intervals, adjusted P values, and cell-type attribution.
- Whether MAPK14 outperforms generic inflammatory markers or merely tracks leukocyte composition.
- Whether any study directly analyzes comorbid MDD–vitiligo participants or paired samples from the same people.
- Whether EXOSC7, KLRG1, IL-17, or another candidate has stronger cross-disease evidence than MAPK14.

### 2. Search for direct human bridge evidence

Look specifically for comorbid or longitudinal human cohorts with:

- Clinically adjudicated MDD and subtype/activity-defined vitiligo.
- MAPK14 RNA, p38α protein, phospho-p38 activity, downstream substrate phosphorylation, cytokines, and cell-state-resolved measurements.
- Single-cell, spatial, sorted-cell, or paired blood/skin data; CSF or postmortem brain data only when disease and treatment context are clear.
- Measurements before onset of the second condition or repeated within-person disease trajectories.
- Mediation analyses adjusting for disease visibility/severity, stigma, stress, socioeconomic factors, smoking, BMI, autoimmune comorbidity, medications, and healthcare utilization.

State explicitly if no such direct bridge study is found, but only after documenting what databases and search terms were checked.

### 3. Establish MAPK14 specificity and causal strength

Separate:

- MAPK14/p38α from MAPK11/p38β, MAPK12/p38γ, and MAPK13/p38δ.
- MAPK14 transcript abundance from p38α protein abundance, phosphorylation/activity, downstream substrate activity, and causal necessity.
- Isoform-specific genetic perturbation from pan-p38 antibodies or inhibitors.
- On-target p38α effects from inhibitor off-targets, toxicity, scaffolding effects, or JNK/ERK effects.

Search for genetic loss-of-function, CRISPR interference/knockout, cell-restricted conditional deletion, selective pharmacology, dose response, and rescue with wild-type versus kinase-dead MAPK14. Identify the precise upstream signal, cell type, downstream substrate, and phenotype in each disease arm.

### 4. Test the competing explanations

For each alternative model, seek direct supporting, refuting, and qualifying evidence.

- Psychosocial: visibility, extent, stigma, quality of life, and stress preceding MDD; comparisons with nonvisible vitiligo or visible nonvitiligo skin diseases; persistence after severity and distress adjustment.
- Surveillance/treatment: incident-diagnosis studies with equalized follow-up, active comparators, negative-control outcomes/exposures, lag analyses, and medication-specific effects.
- Nonspecific inflammation: comparisons with atopic dermatitis, psoriasis, alopecia areata, and other autoimmune/inflammatory disorders; whether inflammatory or p38 signatures distinguish vitiligo–MDD from generic inflammatory comorbidity.
- Shared pleiotropy: cross-trait LDSC or other global/local genetic correlation, locus-level colocalization, cross-trait GWAS, shared eQTL/pQTL effects, and multivariable analyses. Distinguish true colocalization from linkage and sample overlap.
- Directional causation: bidirectional MR, prospective incidence, temporal mediation, and sensitivity analyses. Report the exact phenotype definitions and instrument strength; do not generalize null results beyond the tested traits.
- Parallel p38 models: compare upstream triggers, relevant cell types, substrates, and outcomes in serotonergic neurons/glia versus melanocytes/keratinocytes/immune cells. Different causal compartments or upstream programs count against one shared circuit even if both use p38α.

### 5. Construct and grade the causal chain

Build separate chains for:

- MDD arm: upstream stress/inflammatory signal → specified cell state → MAPK14 activity → defined substrate/output → neural or immune dysfunction → clinically relevant MDD outcome.
- Vitiligo arm: oxidative/immune signal → specified cell state → MAPK14 activity → defined substrate/output → melanocyte injury or cytotoxic recruitment → vitiligo activity/depigmentation.
- Proposed bridge: shared upstream state, circulating mediator, or homologous cell program connecting both arms.

Grade every edge as established, supported, partial, speculative, contradicted, or missing. A source supporting only one arm cannot upgrade the bridge edge.

## Scope and named-entity-confusion guards

- Confirm that every human study actually concerns MONDO:0002009 MDD and MONDO:0008661 vitiligo, recording diagnostic criteria and subtype.
- If a report resolves either disease to a different entity, discard that report rather than cherry-picking it.
- Keep human clinical, model-organism, in-vitro/ex-vivo, computational, and review evidence separate.
- Do not upgrade rodent stress behavior to human MDD.
- Do not upgrade mouse melanocyte or generic oxidative-stress findings to human vitiligo.
- Do not call pan-p38 results MAPK14-specific without isoform-resolving evidence.
- Do not equate whole-blood bulk RNA with brain, skin, or a defined immune-cell state.
- Do not infer causality from coexpression, PPI centrality, machine-learning selection, ROC performance, ssGSEA, pathway enrichment, temporal association, or shared neural-crest origin.
- Do not interpret null directional MR as evidence against shared pleiotropy.
- Do not call two independent tissue-specific p38 pathways a shared mediator.
- Treat medications, disease activity, cell mixture, technical batch, and healthcare contact as plausible confounders unless directly controlled.
- Flag retractions, corrections, preprints, overlapping cohorts, sample reuse, and review-level claims.

## Required output

### Executive judgment

Give one verdict: supported, partially supported, unresolved, weakly supported, or refuted. State separately whether evidence supports:

1. MAPK14 involvement in MDD.
2. MAPK14 involvement in vitiligo.
3. A shared MAPK14-dependent mediator of their comorbidity.

### Evidence matrix

One row per important evidence item, with:

- PMID preferred; DOI only when no PMID exists.
- Study design and evidence type.
- Species and exact disease/phenotype definition.
- Cohort/sample size.
- Tissue and cell type.
- MAPK14 measurement or perturbation.
- Quantitative result, direction, uncertainty, and adjusted significance where available.
- Which model it supports, refutes, or qualifies.
- Confidence and limitations.
- A short exact source sentence suitable as a curator-verification lead.

Split mixed-source publications into separate rows when needed.

### PMID:42418414 replication/method audit

Provide a dedicated table covering every source GEO dataset, sample provenance, tissue, disease definition, preprocessing, statistical threshold, independence, MAPK14 effect direction, multiple-testing control, and cell-composition risk. State which claims reproduce independently and which remain unsupported.

### Model-comparison table

Compare the shared-MAPK14, psychosocial, surveillance/treatment, nonspecific-inflammation, shared-pleiotropy, each directional-causation model, and parallel-tissue-specific-p38 model. For each give:

- Causal prediction.
- Best supporting evidence.
- Best contradictory evidence.
- Findings that would distinguish it.
- Current relative plausibility.

### Cell-state and mechanistic map

Map upstream trigger → cell type → p38 isoform/activity → substrate/output → disease consequence separately for brain/neural, circulating immune, and skin compartments. Identify whether any state is truly shared or merely analogous.

### Negative evidence and search audit

List the databases, registries, datasets, search strings, and search date used to check for:

- Human comorbid-cohort MAPK14 evidence.
- Longitudinal or mediation evidence.
- GWAS genetic correlation/colocalization.
- MAPK14-specific perturbation and rescue.
- Clinical p38α-inhibitor evidence relevant to either condition.
- Failed replications or contradictory results.

Use “no evidence found” only for explicitly searched scopes. Do not claim comprehensive absence from a nonsystematic search.

### Discriminating studies

Rank the most efficient studies to separate the models. Include:

- Treatment-naive MDD-only, active nonsegmental-vitiligo-only, comorbid, matched disease-free, and visible-inflammatory-skin comparator groups.
- Longitudinal repeated phenotyping with equalized surveillance.
- Single-cell plus surface-protein/phospho-p38 profiling in blood and paired lesional/nonlesional skin.
- Cell-restricted MAPK14 perturbation in human donor-derived serotonergic neuron/glia and melanocyte/keratinocyte/cytotoxic-T-cell systems.
- Selective p38α pharmacology plus CRISPR-resistant wild-type versus kinase-dead rescue.
- Prespecified decision criteria distinguishing shared mediation, psychosocial mediation, surveillance bias, generic inflammation, pleiotropy, parallel p38 use, and a correlated marker.

For each study provide sample/model, perturbation, controls, readouts, expected result under each competing model, and major feasibility limitation.

### Curation leads

Provide only candidate leads requiring independent verification:

- Primary references and exact snippets.
- Candidate evidence classifications.
- Candidate refinements to the MDD and vitiligo KNOWLEDGE_GAP discussions.
- Whether the pair-level hypothesis should remain a discussion, become an EMERGING mechanistic hypothesis, be narrowed to parallel tissue-specific models, or be deprecated.
- Explicitly state whether evidence justifies a MAPK14 pathophysiology node, biomarker, causal edge, or conserved module.

## Citation standards

- Prefer primary literature and PMID identifiers.
- Use reviews for orientation only, labeled as reviews.
- Cite every substantive empirical claim at the point of use.
- Never invent a PMID, DOI, cohort, statistic, quote, negative result, or ontology identifier.
- Supply short verbatim snippets and identify whether each comes from an abstract or accessible full text; all snippets remain leads that DisMech curators must independently validate.
- Preserve exact numeric estimates and uncertainty.
- Distinguish direct evidence from author interpretation and from your inference.
- End with a complete citation manifest containing identifier, title, year, study type, and every report section in which each source was used.
**Provider:** openscientist
**Generated:** 2026-07-26T07:15:03.299344

1. PMID:21835346
2. PMID:24699061
3. PMID:20085492
4. PMID:39890561
5. PMID:37975615
6. PMID:41781039
7. PMID:42418414
8. PMID:42051022
9. PMID:34554406
10. PMID:42082425
11. PMID:30528503
12. PMID:40840361
13. PMID:17481858
14. PMID:21514118
15. PMID:41884389
16. PMID:41707798
17. PMID:41786069
18. PMID:42134655
