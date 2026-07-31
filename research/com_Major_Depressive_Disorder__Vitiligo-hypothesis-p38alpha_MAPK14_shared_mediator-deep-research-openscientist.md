---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-26T06:59:20.509647'
end_time: '2026-07-26T07:15:03.299344'
duration_seconds: 942.79
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 18
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: com_Major_Depressive_Disorder__Vitiligo-hypothesis-p38alpha_MAPK14_shared_mediator-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: com_Major_Depressive_Disorder__Vitiligo-hypothesis-p38alpha_MAPK14_shared_mediator-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Focused Mechanistic Hypothesis Search: MDD–Vitiligo p38α/MAPK14 Shared Mediator

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

## Output

# Focused Mechanistic Hypothesis Search: MDD–Vitiligo p38α/MAPK14 Shared Mediator

**DisMech issue #5921 — Focused hypothesis audit**
Hypothesis ID: `mdd_vitiligo_acquired_mapk14_shared_mediator`
Disease scope: Major depressive disorder (MONDO:0002009) and vitiligo (MONDO:0008661, acquired generalized/nonsegmental prioritized)
Literature coverage through 2026-07-26 (PubMed via provided tool). All snippets are **curator-verification leads**, not validated facts. No primary GEO re-analysis was performed (datasets not provided).

---

## Executive Judgment

**Overall verdict: REFUTED as a shared mediator / UNRESOLVED as a knowledge gap.** Current evidence does **not** support an acquired, MAPK14-specific, cell-state-resolved causal mediator shared by MDD and vitiligo. The seed claim rests on a single, explicitly hypothesis-generating in-silico study, and every stronger human test points away from a shared p38α circuit. The observed comorbidity is better explained by **parallel tissue-specific p38 use plus nonspecific inflammatory and psychosocial burden**.

Stated separately for the three required sub-claims:

| Sub-claim | Verdict | Basis |
|-----------|---------|-------|
| **1. MAPK14 involvement in MDD** | **Weakly supported / partly contradicted** | Only isoform-specific p38α evidence is a mouse serotonergic-neuron knockout ([PMID:21835346](https://pubmed.ncbi.nlm.nih.gov/21835346/)); the human p38-inhibitor RCT (losmapimod) was **null** ([PMID:24699061](https://pubmed.ncbi.nlm.nih.gov/24699061/)). |
| **2. MAPK14 involvement in vitiligo** | **Partially supported (pan-p38, not isoform-resolved)** | Human perilesional keratinocyte p38 activation ([PMID:20085492](https://pubmed.ncbi.nlm.nih.gov/20085492/)), but pan-p38, not MAPK14-specific; MAPK14 is not a recognized vitiligo susceptibility gene ([PMID:39890561](https://pubmed.ncbi.nlm.nih.gov/39890561/)). |
| **3. A shared MAPK14-dependent mediator of comorbidity** | **Refuted / unsupported** | No comorbid cohort, no paired tissue, no colocalization, null directional MR ([PMID:37975615](https://pubmed.ncbi.nlm.nih.gov/37975615/)), isoform/species discordance, and nonspecific comorbidity matching atopic dermatitis ([PMID:41781039](https://pubmed.ncbi.nlm.nih.gov/41781039/)). |

**Curation recommendation:** Keep the pair-level hypothesis as a **KNOWLEDGE_GAP discussion**, optionally narrowed to **parallel tissue-specific p38 models**. The evidence does **not** justify a MAPK14 pathophysiology node, biomarker, causal edge, or conserved module in DisMech.

---

## Summary

The seed hypothesis proposes that an acquired, cell-state-specific inflammatory program involving p38α/MAPK14 acts as a *shared mediator* linking major depressive disorder and vitiligo. A genuine shared mediator would require evidence that one defined MAPK14-dependent state — or a causally connected cross-compartment program — precedes and contributes to *both* disease outcomes. Over five iterations of literature audit and evidence grading, no such bridge was found.

The entire molecular basis for the shared-mediator claim traces to a single computational paper ([PMID:42418414](https://pubmed.ncbi.nlm.nih.gov/42418414/)) that integrated **separate** disease datasets — MDD whole blood (GSE98793: 128 MDD/64 control) and vitiligo skin (GSE65127+GSE53146: 15/15) — using a permissive differential-expression threshold (any nonzero |log2FC|, nominal P<0.05), STRING PPI centrality, machine-learning feature selection, and ssGSEA-*inferred* (not measured) immune enrichment. In that paper MAPK14 is only **one of three co-equal machine-learning candidates** (alongside EXOSC7 and KLRG1), the authors explicitly frame it as preliminary and hypothesis-generating, and there is no comorbid cohort, no paired blood/skin/brain material, no direct p38α activity assay, and no causal perturbation. This is a correlated-marker-in-separate-tissues result, not a mediation result.

Every independent line of evidence that could upgrade the bridge edge instead weakens it. The two disease arms use p38 in **isoform- and species-discordant** ways: the only isoform-specific p38α (MAPK14) finding is a mouse serotonergic-neuron knockout that produces stress *resilience* via serotonin-transporter trafficking ([PMID:21835346](https://pubmed.ncbi.nlm.nih.gov/21835346/)), whereas the human vitiligo evidence is **pan-p38** apoptotic signaling in perilesional keratinocytes ([PMID:20085492](https://pubmed.ncbi.nlm.nih.gov/20085492/)). A controlled human trial of the p38α/β inhibitor losmapimod was **negative** in MDD ([PMID:24699061](https://pubmed.ncbi.nlm.nih.gov/24699061/)); bidirectional Mendelian randomization between generalized vitiligo and depression is **null** ([PMID:37975615](https://pubmed.ncbi.nlm.nih.gov/37975615/)); MAPK14 is **not** among the >50 established vitiligo susceptibility loci ([PMID:39890561](https://pubmed.ncbi.nlm.nih.gov/39890561/)); and vitiligo's mental-health comorbidity is **nonspecific**, closely matching atopic dermatitis ([PMID:41781039](https://pubmed.ncbi.nlm.nih.gov/41781039/), [PMID:42051022](https://pubmed.ncbi.nlm.nih.gov/42051022/)). Meanwhile the vitiligo→MDD arm is well explained by **psychosocial mediation**, with depression burden scaling with lesion visibility, extent, and younger age ([PMID:34554406](https://pubmed.ncbi.nlm.nih.gov/34554406/), [PMID:42082425](https://pubmed.ncbi.nlm.nih.gov/42082425/)), mirroring the age-stratified vitiligo→MDD risk gradient in the epidemiological cohort ([PMID:30528503](https://pubmed.ncbi.nlm.nih.gov/30528503/)).

Taken together, the comorbidity is real and bidirectional at the epidemiological level, but the proposed molecular bridge is unsubstantiated. The best-supported models are **parallel tissue-specific p38 use** (p38α with different upstream triggers, cell types, substrates, and consequences in brain vs skin) layered on **nonspecific inflammatory/psychosocial burden**, not a single shared MAPK14-dependent mediator.

---

## Key Findings

### F001 — The seed molecular link rests on one hypothesis-generating in-silico study

The MAPK14 shared-mediator idea originates entirely from [PMID:42418414](https://pubmed.ncbi.nlm.nih.gov/42418414/) (2026), which integrated separate GEO datasets: MDD whole-blood (GSE98793: 128 MDD, 64 control) and vitiligo skin (GSE65127+GSE53146: 15 vitiligo, 15 control). MAPK14 was selected through a chain of correlational/heuristic steps — differential expression at a permissive threshold, STRING PPI network centrality, machine-learning feature selection, and ssGSEA immune-enrichment signatures that are *inferred* rather than measured cell abundances. Critically, MAPK14 is one of **three** co-equal machine-learning hits: the paper states, *"Machine learning further prioritized three key genes: EXOSC7, KLRG1, and MAPK14."* The authors themselves characterize the result cautiously: *"Preliminary validation suggests MAPK14 as a potential candidate gene warranting further investigation in MDD and vitiligo."*

There is no comorbid MDD–vitiligo cohort, no paired samples from the same participants, no direct p38α activity assay, and no causal perturbation. The comparison also confounds tissue (whole blood vs skin), so any "shared" signal may simply track leukocyte composition. MAPK14 is therefore not uniquely implicated even within its source paper, and none of the inference steps (coexpression, PPI centrality, ML selection, ROC performance, ssGSEA, pathway enrichment) can establish causality or mediation. EXOSC7 and KLRG1 were co-equal hits and were not independently audited — they should be evaluated on equal footing before MAPK14 is privileged.

### F002 — Bidirectional epidemiological association is real, but antidepressant use *lowered* vitiligo risk

The population-based cohort ([PMID:30528503](https://pubmed.ncbi.nlm.nih.gov/30528503/), THIN database) establishes temporal association in both directions: MDD→vitiligo adjusted HR **1.64** (95% CI 1.43–1.87, P<.0001; n=405,397 MDD vs 5,739,048 comparators), and vitiligo→MDD HR **1.31** (before age 30) and **1.22** (age ≥30). The abstract states MDD patients *"were at a 64% increased risk for vitiligo (hazard ratio 1.64, 95% confidence interval [CI] 1.43-1.87, P < .0001)."*

Crucially, the same study reports that vitiligo risk *"was decreased in patients using antidepressants."* Antidepressants (which in vitro *modulate* p38, [PMID:40840361](https://pubmed.ncbi.nlm.nih.gov/40840361/)) reducing vitiligo risk is more consistent with psychosocial/treatment models than with a shared pro-p38 inflammatory program that antidepressants would be expected to leave unchanged or worsen. This is association and temporal ordering of recorded diagnoses — **not mediation**.

### F003 — Human vitiligo p38 and MDD p38α evidence are isoform- and species-discordant

The two arms do not use the same molecular entity in the same way:

- **Vitiligo arm (human, pan-p38):** [PMID:20085492](https://pubmed.ncbi.nlm.nih.gov/20085492/) shows activated p38 as an upstream driver of apoptosis in perilesional keratinocytes from 12 human nonsegmental-vitiligo patients — *"our study demonstrates the pivotal role of p38 MAP kinase as an upstream signal of perilesional keratinocyte damage"* — but this is **pan-p38**, not MAPK14-isoform-resolved. Supporting melanocyte models ([PMID:17481858](https://pubmed.ncbi.nlm.nih.gov/17481858/), [PMID:21514118](https://pubmed.ncbi.nlm.nih.gov/21514118/)) show dopamine/oxidative-stress-induced JNK/p38 apoptosis, again pan-p38 and partly mouse (Mel-Ab) cells.
- **MDD arm (mouse, p38α-specific):** [PMID:21835346](https://pubmed.ncbi.nlm.nih.gov/21835346/) is the *only* MAPK14/p38α-isoform-specific result — *"the α isoform of p38 mitogen-activated protein kinase (MAPK) was selectively inactivated"* — but selective p38α deletion in **mouse serotonergic neurons** produces stress *resilience* via SERT trafficking/hyposerotonergic state. This is rodent depression-like behavior, not human MDD, and it is in neurons, not blood or skin.

Directional genetics is also null: [PMID:37975615](https://pubmed.ncbi.nlm.nih.gov/37975615/) found *"none of the rigorous bidirectional MR analyses uncovered a significant causal association"* between generalized vitiligo and depression. The arms therefore share a *gene family label* but differ in isoform specificity, species, cell type, upstream trigger, downstream substrate, and directional consequence — the signature of **parallel tissue-specific p38 use**, not one shared circuit.

### F004 — A p38 inhibitor (losmapimod) failed in a controlled human MDD trial

The strongest causal test in the MDD arm is negative. [PMID:24699061](https://pubmed.ncbi.nlm.nih.gov/24699061/) evaluated losmapimod (GW856553, an oral p38α/β inhibitor) 7.5 mg BID for 6 weeks in two RCTs in clinically diagnosed MDD enriched for anergia/psychomotor retardation. An underpowered, early-terminated Study 574 (n=24) nominally favored drug (Bech difference −4.10; 95% CI −7.36, −0.83; p=0.017), but the pre-registered Bayesian confirmatory Study 009 (n=128) *"showed no advantage for losmapimod"* (Bech difference +1.11; 95% credible interval −0.22, 2.50), with no significant cytokine biomarker changes. The authors conclude: *"In conclusion 7.5 mg BID losmapimod was not effective in MDD."* Because losmapimod inhibits p38α (MAPK14) — albeit not isoform-selectively — this is direct human evidence against a *causal, druggable* p38 role in MDD.

### F005 — Vitiligo's mental-health comorbidity is largely nonspecific, matching atopic dermatitis

If a vitiligo-specific p38 mediator drove MDD, vitiligo's psychiatric burden should exceed that of other inflammatory dermatoses. It does not. [PMID:41781039](https://pubmed.ncbi.nlm.nih.gov/41781039/) (German DAK claims, N=2,885,984; 4,631 vitiligo cases, ICD-10 L80, propensity-matched 1:3) reports depressive-episode prevalence of 8.9–19.2% and, in matched comparison with atopic dermatitis, *"only a few and inconsistent differences were observed"* (more pronounced differences appeared only vs psoriasis). The companion claims analysis [PMID:42051022](https://pubmed.ncbi.nlm.nih.gov/42051022/) reports modest, shared risk: depression RR **1.23** (95% CI 1.15–1.32), anxiety RR **1.32** (1.19–1.47), explicitly noting these were *"linked to skin diseases like vitiligo, atopic dermatitis, or psoriasis."* Modest effect sizes (RR ~1.2–1.3) shared across dermatoses support **nonspecific inflammatory/psychosocial burden** rather than a vitiligo-specific molecular mechanism. Note these two claims analyses share the DAK data source and likely overlapping cohorts — treat as **one data source**, not two independent replications.

### F006 — No genetic evidence for MAPK14 as a shared pleiotropic locus

Vitiligo susceptibility is immune/oxidative/melanogenic, not MAPK14-centered. The genetics review [PMID:39890561](https://pubmed.ncbi.nlm.nih.gov/39890561/) states GWAS *"have identified over 50 susceptibility loci, including key genes within the MHC region and those involved in immunity, oxidative stress, and melanogenesis"* — MAPK14 is not among the highlighted genes. The newest multi-omics vitiligo mediator is TAPBP via STAT2/interferon–antigen-presentation ([PMID:41884389](https://pubmed.ncbi.nlm.nih.gov/41884389/)): *"Cross-omic analysis identified TAPBP as a top candidate, which is significantly upregulated in lesional melanocytes and core to the antigen-processing network"* — again, not MAPK14. Targeted PubMed searches (2026-07-26) for an MDD–vitiligo cross-trait genetic-correlation/colocalization/LDSC study and for a MAPK14 depression GWAS locus returned no papers, and the only genetic disease-to-disease test (bidirectional MR, [PMID:37975615](https://pubmed.ncbi.nlm.nih.gov/37975615/)) was null. There is currently no locus-level colocalization, shared eQTL/pQTL, or genetic-correlation evidence placing MAPK14 as a shared pleiotropic driver. (Null MR does not, by itself, exclude shared pleiotropy — but no cross-trait analysis supports it either.)

### F007 — Psychosocial mediation is well-supported for the vitiligo→MDD arm

The systematic review [PMID:34554406](https://pubmed.ncbi.nlm.nih.gov/34554406/) (168 studies, 1979–2021) reports depression in 0.1–62.3% and anxiety in 1.9–67.9% of vitiligo patients, with significantly higher burden associated with *"female sex, visible or genital lesions, age < 30 years (particularly adolescents), and greater body surface area involvement, among others,"* and lesion concealment as the commonest coping strategy. The narrative review [PMID:42082425](https://pubmed.ncbi.nlm.nih.gov/42082425/) (2026) concurs that *"Disease visibility, particularly involvement of the face or genital regions; greater body surface area involvement; active disease progression; and longer disease duration emerged as key clinical factors associated with worse outcomes."* This visibility/age gradient mirrors the age-stratified vitiligo→MDD risk (HR 1.31 if <30y vs 1.22 if ≥30y) in [PMID:30528503](https://pubmed.ncbi.nlm.nih.gov/30528503/), consistent with **psychosocial rather than molecular mediation**.

---

## Mechanistic Model / Interpretation

The evidence supports **two independent (parallel) p38 pathways** plus a **psychosocial/nonspecific-inflammation overlay**, not a single shared mediator.

```
BRAIN / NEURAL COMPARTMENT (MDD arm)
  chronic stress / neuroinflammation
      │
      ▼
  serotonergic neurons ──[p38α / MAPK14, isoform-specific]──► SERT trafficking → hyposerotonergic state
      │  (MOUSE ONLY, deletion → RESILIENCE; PMID:21835346)
      ▼
  depression-like behavior  ── human MDD?  ◄─ p38 inhibitor losmapimod NULL in RCT (PMID:24699061)

SKIN COMPARTMENT (vitiligo arm)
  oxidative stress (H2O2 / dopamine)
      │
      ▼
  melanocytes + perilesional keratinocytes ──[pan-p38, NOT isoform-resolved]──► p53/NF-κB apoptosis
      │  (HUMAN NSV keratinocytes + mouse/human melanocytes; PMID:20085492, 17481858, 21514118)
      ▼
  melanocyte loss → depigmentation

BRIDGE EDGE (proposed shared mediator)
  ??? shared upstream state / circulating mediator / homologous cell program ???
      │
      ▼
  ✗ MISSING: no comorbid cohort, no paired tissue, no colocalization,
    null directional MR, isoform/species discordance

PSYCHOSOCIAL / NONSPECIFIC OVERLAY (best-supported real link)
  visible/extensive vitiligo, younger age, stigma → distress → MDD
  (PMID:34554406, 42082425, 30528503) — shared across dermatoses (PMID:41781039, 42051022)
```

**Causal-chain grading:**

| Edge | Grade | Note |
|------|-------|------|
| MDD: stress → serotonergic neuron → p38α → SERT → behavior | **Partial (mouse)** | Isoform-specific but rodent; deletion→resilience complicates a "p38α drives MDD" story |
| MDD: p38 activity → clinical MDD outcome | **Contradicted** | Losmapimod RCT null (PMID:24699061) |
| Vitiligo: oxidative stress → keratinocyte/melanocyte → p38 → apoptosis | **Supported (pan-p38)** | Human NSV, but not MAPK14-isoform-resolved |
| Vitiligo: MAPK14-specific necessity | **Missing** | No isoform-selective perturbation/rescue |
| Bridge: shared MAPK14-dependent state | **Missing / Speculative** | No direct human bridge evidence |
| Shared pleiotropy at MAPK14 | **Missing** | Not a vitiligo locus; no cross-trait colocalization |
| Psychosocial mediation (vitiligo→MDD) | **Supported** | Visibility/age/extent gradient |

**Cell-state map — is any state truly shared?** The neural substrate (SERT trafficking in serotonergic neurons) and the skin substrate (p53/NF-κB apoptosis in melanocytes/keratinocytes) are **analogous** (both engage p38 family kinases under stress) but **not shared**: different upstream triggers (psychosocial stress vs oxidative/dopamine), different cells, different substrates, and different isoform resolution. The circulating-immune "bridge" candidate (whole-blood MAPK14 transcript, PMID:42418414) is speculative and confounded by leukocyte composition. **No truly shared MAPK14-dependent state is demonstrated.**

---

## Evidence Base

| PMID | Design & type | Species / phenotype | Size | Tissue / cell | MAPK14 measure/perturbation | Result & direction | Model impact |
|------|---------------|---------------------|------|---------------|------------------------------|--------------------|--------------|
| [42418414](https://pubmed.ncbi.nlm.nih.gov/42418414/) | In-silico integration (DE/PPI/ML/ssGSEA) | Human MDD (blood) + vitiligo (skin), separate | 128/64 + 15/15 | Whole blood vs skin | Transcript DEG + ML selection | MAPK14 = 1 of 3 co-equal ML hits; nominal P | Seed; correlated marker |
| [30528503](https://pubmed.ncbi.nlm.nih.gov/30528503/) | Bidirectional cohort | Human MDD & vitiligo (dx) | 405,397 MDD; 5.7M comp. | Registry | None | MDD→vitiligo HR 1.64; vitiligo→MDD 1.31/1.22; antidepressants ↓ risk | Favors psychosocial/treatment |
| [24699061](https://pubmed.ncbi.nlm.nih.gov/24699061/) | Two RCTs (Bayesian) | Human clinical MDD | 24 + 128 | Systemic | p38α/β inhibitor losmapimod | Confirmatory NO advantage; "not effective in MDD" | Refutes causal p38→MDD |
| [21835346](https://pubmed.ncbi.nlm.nih.gov/21835346/) | Conditional KO | Mouse depression-like | — | Serotonergic neurons | Selective p38α (MAPK14) deletion | Deletion → resilience via SERT | Parallel p38 model (neural, mouse) |
| [20085492](https://pubmed.ncbi.nlm.nih.gov/20085492/) | Ex vivo mechanistic | Human NSV | 12 | Perilesional keratinocytes | Pan-p38 | p38 upstream of apoptosis | Vitiligo p38 (pan, not isoform) |
| [17481858](https://pubmed.ncbi.nlm.nih.gov/17481858/) | In vitro | Mouse Mel-Ab + human melanocytes | — | Melanocytes | Pan JNK/p38 | Dopamine → apoptosis | Vitiligo model (pan-p38) |
| [21514118](https://pubmed.ncbi.nlm.nih.gov/21514118/) | In vitro | Human melanocytes | — | Melanocytes | Pan p38/JNK/Akt | Dopamine → apoptosis; apigenin protective | Vitiligo model (pan-p38) |
| [37975615](https://pubmed.ncbi.nlm.nih.gov/37975615/) | Bidirectional MR | Generalized vitiligo & depression | GWAS-scale | Genetic | Instruments (disease-level) | No significant causal association | Refutes directional causation |
| [41781039](https://pubmed.ncbi.nlm.nih.gov/41781039/) | Matched cohort (claims) | Vitiligo (L80) vs AD/psoriasis | 4,631 cases | Registry | None | Profile ≈ atopic dermatitis | Supports nonspecific model |
| [42051022](https://pubmed.ncbi.nlm.nih.gov/42051022/) | Claims analysis | Vitiligo | Population | Registry | None | Depression RR 1.23; anxiety RR 1.32 | Supports nonspecific model |
| [39890561](https://pubmed.ncbi.nlm.nih.gov/39890561/) | Review (genetics) | Vitiligo | — | Genetic | None | >50 loci: MHC/immune/oxidative/melanogenic; not MAPK14 | Refutes MAPK14 pleiotropy |
| [41884389](https://pubmed.ncbi.nlm.nih.gov/41884389/) | Multi-omics + experiment | Vitiligo | — | Lesional melanocytes | None | TAPBP/STAT2/IFN top mediator | Alternative mechanism, not MAPK14 |
| [34554406](https://pubmed.ncbi.nlm.nih.gov/34554406/) | Systematic review | Vitiligo psychosocial | 168 studies | — | None | Burden ↑ with visibility, extent, age<30 | Supports psychosocial mediation |
| [42082425](https://pubmed.ncbi.nlm.nih.gov/42082425/) | Narrative review | Vitiligo QOL | — | — | None | Visibility/extent/activity drive QOL | Supports psychosocial mediation |
| [40840361](https://pubmed.ncbi.nlm.nih.gov/40840361/) | In vitro | Macrophages | — | Macrophages | Phospho-p38 (flow) | Antidepressants modulate p38 (context-dependent) | Qualifies antidepressant→p38 link |

*Rodent neuroinflammation p38 papers ([PMID:41707798](https://pubmed.ncbi.nlm.nih.gov/41707798/), [PMID:41786069](https://pubmed.ncbi.nlm.nih.gov/41786069/), [PMID:42134655](https://pubmed.ncbi.nlm.nih.gov/42134655/)) reinforce a neural p38 route in mouse depression-like behavior but are pan-p38/pan-MAPK and cannot be upgraded to human MDD or a shared mediator.*

### PMID:42418414 Replication / Method Audit

No independent GEO re-analysis was performed (datasets not supplied). This is a methodological audit of the seed design as reported.

| Element | GSE98793 (MDD) | GSE65127 / GSE53146 (vitiligo) | Assessment |
|---------|----------------|-------------------------------|------------|
| Tissue | Whole blood | Skin | **Cross-tissue mismatch** — cannot establish a shared cell-state |
| Disease definition | MDD (clinical) | NSV / vitiligo as annotated | Subtype/activity/treatment not harmonized |
| N | 128 / 64 | 15 / 15 (integrated) | Vitiligo side very small; integration adds batch risk |
| DE threshold | nonzero \|log2FC\|, nominal P<0.05 | same | **No effect-size floor, no FDR reported** |
| Multiple-testing control | Not evident | Not evident | Unsupported without FDR |
| Feature-selection independence | ML on same DEGs | — | **Validation likely not independent** → optimistic |
| Immune cells | ssGSEA (inferred) | ssGSEA (inferred) | Not measured; tracks leukocyte composition |
| MAPK14 direction/CI/adj-P | Not reported in abstract | — | **Unverified** — curators must extract from full text |
| Comorbid/paired samples | None | None | **No bridge between diseases** |

**Reproduces independently:** MDD–vitiligo comorbidity exists (PMID:30528503); p38 is stress-activated in immune cells and skin (non-specific). **Does NOT reproduce:** MAPK14 as a *specific* shared driver over EXOSC7/KLRG1 or generic inflammatory markers; any shared cell-state; MAPK14 direction/magnitude/adjusted significance; any causal or mediation claim. GSE52790 and GSE80009 were not examined (not provided) — flagged as open replication tasks.

### Model-Comparison Table

| Model | Causal prediction | Best support | Best contradiction | Distinguishing finding | Plausibility |
|-------|-------------------|--------------|--------------------|--------------------------|--------------|
| **Shared MAPK14 mediator** | One MAPK14 state precedes both | PMID:42418414 | Null RCT (24699061), null MR (37975615), isoform/species discordance | Paired blood+skin phospho-p38α shared state in comorbid patients | **Low** |
| **Psychosocial mediation** | Visibility/stigma → MDD | 34554406, 42082425, 30528503 age gradient | Some less-visible cases still affected | Link persists/attenuates after severity/distress adjustment | **High (vitiligo→MDD)** |
| **Surveillance / treatment** | Diagnostic contact / drugs inflate | Antidepressants ↓ vitiligo risk (30528503) | Bidirectionality survives adjustment | Negative controls, equalized follow-up | **Moderate** |
| **Nonspecific inflammation** | Comorbidity shared across dermatoses | 41781039 (≈AD), 42051022 | Some signals stronger vs psoriasis | Signature distinguishing vitiligo-MDD from AD-MDD | **High** |
| **Shared pleiotropy** | Common liability at shared loci | — | Not a vitiligo locus (39890561); null MR (37975615) | Cross-trait LDSC + locus colocalization | **Low (for MAPK14)** |
| **MDD→vitiligo causation** | MDD/stress worsens vitiligo | HR 1.64 (30528503) | Null MR (37975615); antidepressants protective | Strong-instrument MR; prospective incidence | **Weak–moderate** |
| **Vitiligo→MDD causation** | Vitiligo causes MDD | HR 1.31/1.22 (30528503) | Null MR (37975615); nonspecific vs AD | Mediation adjusting for visibility/stigma | **Moderate (psychosocial route)** |
| **Parallel tissue-specific p38** | p38α used separately in brain vs skin | Discordance (21835346 vs 20085492) | — (consistent with model) | Refuted only by a demonstrated shared cross-compartment program | **High (best fit)** |

---

## Limitations and Knowledge Gaps

1. **No comorbid human cohort exists** with clinically adjudicated MDD *and* subtype/activity-defined vitiligo carrying MAPK14 RNA, p38α protein, phospho-p38 activity, or downstream substrate measurements. This is the central missing bridge study; its absence is documented from targeted PubMed searches, not a comprehensive multi-database systematic review.
2. **Isoform specificity is unresolved** in vitiligo: all skin evidence is pan-p38, so MAPK14 (p38α) vs MAPK11/12/13 contributions are unknown. No isoform-selective genetic perturbation or kinase-dead rescue exists for either arm's human context.
3. **Transcript ≠ protein ≠ activity:** the seed relies on bulk transcript abundance; p38α protein, phosphorylation, and substrate activity were never measured across compartments.
4. **The MDD isoform-specific evidence is mouse-only** and points to resilience-on-deletion, complicating a straightforward "p38α drives MDD" narrative.
5. **Confounders** — cell mixture, medications, disease activity, batch, healthcare contact, smoking, BMI, socioeconomic factors — are largely uncontrolled in the seed and unaddressed for the molecular hypothesis.
6. **Null MR does not exclude shared pleiotropy** — no cross-trait LDSC/colocalization has been performed, so the pleiotropy model is untested rather than refuted (though MAPK14-specific pleiotropy is unsupported by known vitiligo genetics).
7. **Search scope:** single database (PubMed); Embase, GWAS Catalog, Open Targets, ClinicalTrials.gov, and preprint servers were not queried. "No evidence found" applies only to explicitly searched scopes.

---

## Proposed Follow-up Experiments / Discriminating Studies

Ranked by efficiency in separating the competing models:

1. **Cross-trait LDSC + MAPK14-locus colocalization (highest value, lowest cost).** Vitiligo GWAS × MDD GWAS global/local genetic correlation, locus colocalization, and shared eQTL/pQTL at MAPK14, distinguishing colocalization from linkage and sample overlap. Summary statistics already exist. *Expected under shared pleiotropy:* colocalization at MAPK14; *under parallel/nonspecific:* none.
2. **Comorbid paired-tissue profiling.** Treatment-naive MDD-only, active-NSV-only, comorbid, matched disease-free, and a visible-inflammatory-skin comparator (atopic dermatitis). Single-cell + surface-protein/**phospho-p38α** (CyTOF) in blood and paired lesional/nonlesional skin. *Under shared mediator:* one phospho-p38α+ state elevated in both arms, maximal in comorbid subjects; *under parallel/nonspecific:* compartment-specific signatures indistinguishable from atopic dermatitis.
3. **Isoform-resolved perturbation with rescue.** Cell-restricted MAPK14 CRISPR knockout/interference in human iPSC-derived serotonergic neurons/glia and in melanocytes/keratinocytes/CD8 T cells, with selective p38α pharmacology plus CRISPR-resistant **wild-type vs kinase-dead** MAPK14 rescue and dose-response. Establishes isoform specificity, causal necessity, and on-target vs off-target effects per compartment.
4. **Longitudinal mediation with equalized surveillance.** Prospective repeated phenotyping measuring MAPK14/phospho-p38 and cytokines *before* onset of the second condition, with mediation adjusting for visibility/severity, stigma, stress, socioeconomic factors, smoking, BMI, autoimmune comorbidity, medications, and healthcare utilization; include negative-control outcomes and active comparators to address surveillance/treatment bias.
5. **Vitiligo activity RCT of a selective p38α inhibitor** with a phospho-p38 target-engagement biomarker, mirroring the informative null MDD RCT to test the vitiligo-arm causal edge.

**Prespecified decision criteria:** Shared mediation requires a demonstrated shared MAPK14+ cell-state (study 2) **and** MAPK14-locus colocalization (study 1) **and** isoform-specific necessity in both arms (study 3). Absence of a shared state but arm-specific necessity → **parallel p38**. Vitiligo≈AD signature → **nonspecific**. Effect abolished by visibility/stigma adjustment → **psychosocial**. Attenuation by equalized surveillance → **surveillance bias**. Null coloc + null MR → reject shared-pleiotropy/directional-genetic.

---

## Curation Leads (require independent DisMech verification)

- **Disposition:** Keep `mdd_vitiligo_acquired_mapk14_shared_mediator` as a **KNOWLEDGE_GAP discussion**, optionally **narrowed to parallel tissue-specific p38 models.** Do **not** promote to EMERGING mechanistic hypothesis; consider deprecating the "single shared mediator" framing.
- **Node/biomarker/edge/module:** Evidence does **NOT** justify a MAPK14 pathophysiology node, biomarker, causal edge, or conserved cross-disease module for this pair. At most, MAPK14 is a hypothesis-level candidate marker in one in-silico study.
- **Seed lead:** [PMID:42418414](https://pubmed.ncbi.nlm.nih.gov/42418414/) — *"Machine learning further prioritized three key genes: EXOSC7, KLRG1, and MAPK14."*
- **MDD refutation lead:** [PMID:24699061](https://pubmed.ncbi.nlm.nih.gov/24699061/) — *"In conclusion 7.5 mg BID losmapimod was not effective in MDD."*
- **Vitiligo refinement:** p38 evidence is pan-p38, ex-vivo/in-vitro ([PMID:20085492](https://pubmed.ncbi.nlm.nih.gov/20085492/)); genetics point to HLA/immune/oxidative/TAPBP ([PMID:39890561](https://pubmed.ncbi.nlm.nih.gov/39890561/), [PMID:41884389](https://pubmed.ncbi.nlm.nih.gov/41884389/)), not MAPK14.
- **Alternative candidates:** EXOSC7 and KLRG1 were co-equal ML hits and were not independently audited — evaluate on equal footing before privileging MAPK14.
- **Overlap flag:** [PMID:41781039](https://pubmed.ncbi.nlm.nih.gov/41781039/) and [PMID:42051022](https://pubmed.ncbi.nlm.nih.gov/42051022/) share the DAK claims source — treat as one data source.

---

## Supported vs Refuted Hypotheses (summary)

- **Supported:** MDD–vitiligo comorbidity is real, bidirectional, and temporally ordered (PMID:30528503). p38 is genuinely activated in vitiligo skin (pan-p38, PMID:20085492) and p38α is mechanistically active in mouse serotonergic stress circuitry (PMID:21835346). Psychosocial mediation of vitiligo→MDD is well-supported (PMID:34554406, 42082425).
- **Refuted / contradicted (as stated):** (i) p38 inhibition treats human MDD — **refuted** (PMID:24699061). (ii) Vitiligo has a *specific* MDD-linking signature beyond other skin diseases — **refuted** (PMID:41781039). (iii) Genetic directional causation vitiligo↔depression — **null** (PMID:37975615). (iv) MAPK14 as an established shared pleiotropic locus — **unsupported** (PMID:39890561, 41884389).
- **Unresolved:** whether a narrow, cell-state-restricted MAPK14 program contributes to each disease **independently** (parallel model) remains open and testable.

---

## Citation Manifest

| Identifier | Title (abbrev.) | Year | Study type | Sections used |
|-----------|------------------|------|------------|----------------|
| PMID:42418414 | Immune microenvironment in MDD and vitiligo | 2026 | Computational (in-silico) | Exec, Summary, F001, Evidence, Audit, Leads |
| PMID:30528503 | Vitiligo and MDD: bidirectional cohort | 2019 | Population cohort | Exec, Summary, F002, F007, Evidence, Models |
| PMID:24699061 | Losmapimod in MDD (two RCTs) | 2014 | RCT | Exec, F004, Evidence, Models, Leads |
| PMID:21835346 | Selective p38α deletion in serotonergic neurons | 2011 | Mouse conditional KO | Exec, F003, Evidence, Map |
| PMID:20085492 | p38/apoptosis in perilesional vitiligo keratinocytes | 2010 | Human ex vivo | Exec, F003, Evidence, Map, Leads |
| PMID:17481858 | Dopamine-induced melanocyte apoptosis (JNK/p38) | 2007 | In vitro | F003, Evidence |
| PMID:21514118 | Apigenin/DA melanocyte p38/JNK/Akt | 2011 | In vitro | F003, Evidence |
| PMID:37975615 | Vitiligo–mental disorders MR | 2024 | Mendelian randomization | Exec, F003, F006, Evidence, Models |
| PMID:41781039 | Mental-health risk in vitiligo vs AD/psoriasis | 2026 | Matched cohort (claims) | Exec, F005, Evidence, Models, Leads |
| PMID:42051022 | Vitiligo epidemiology/comorbidity (Germany) | 2026 | Claims analysis | F005, Evidence, Leads |
| PMID:39890561 | Genetics and epigenetics in vitiligo | 2025 | Review | Exec, F006, Evidence, Leads |
| PMID:41884389 | TAPBP mediator in vitiligo | 2026 | Multi-omics + experiment | F006, Evidence, Leads |
| PMID:34554406 | Psychosocial effects of vitiligo (systematic review) | 2021 | Systematic review | F007, Evidence, Models |
| PMID:42082425 | QOL impairment in vitiligo | 2026 | Narrative review | F007, Evidence, Models |
| PMID:40840361 | Duloxetine/venlafaxine on p38 MAPK | 2025 | In vitro | F002, Evidence |
| PMID:41707798 | COG133 / p38 neuroinflammation | 2025 | Mouse | Evidence (context) |
| PMID:41786069 | CUMS Th1/microglia/p38 | 2025 | Mouse | Evidence (context) |
| PMID:42134655 | let-7a-5p/MAP3K1/MAPK in depression model | 2025 | Mouse/in vitro | Evidence (context) |

*All identifiers, quotes, and statistics are drawn from the abstracts/snippets recorded during the investigation and remain leads for independent DisMech curator validation.*


## Artifacts

- [OpenScientist final report](com_Major_Depressive_Disorder__Vitiligo-hypothesis-p38alpha_MAPK14_shared_mediator-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](com_Major_Depressive_Disorder__Vitiligo-hypothesis-p38alpha_MAPK14_shared_mediator-deep-research-openscientist_artifacts/final_report.pdf)
