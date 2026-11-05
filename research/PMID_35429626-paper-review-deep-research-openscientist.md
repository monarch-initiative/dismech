---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-04T23:43:15.178901'
end_time: '2026-11-04T23:58:33.845254'
duration_seconds: 918.67
template_file: /tmp/claude-0/-home-user-dismech/fc7da921-0b4c-5bb8-bc26-16d7f5c447f6/scratchpad/paper_review_template.md
template_variables:
  paper_id: PMID:35429626
  paper_title: Altered default mode network associated with pesticide exposure in
    Latinx children from rural farmworker families.
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 20
reference_validation:
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 22
  on_topic: 11
  validator_version: 0.5.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PMID_35429626-paper-review-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PMID_35429626-paper-review-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Deep research: models, measured processes/endpoints, and disease relevance of PMID:35429626

## Paper
- Identifier: PMID:35429626 (DOI 10.1016/j.neuroimage.2022.119179)
- Title: "Altered default mode network associated with pesticide exposure in Latinx children from rural farmworker families."
- Bahrami M, Simpson SL, Burdette JH, Lyday RG, Quandt SA, Chen H, Arcury TA, Laurienti PJ. NeuroImage 2022.

Read the paper itself (PMC full text is open access) before anything else. Every claim about what
the paper did must be traceable to the paper; mark anything you infer as inference.

## Tasks

### 1. Study models / systems
Identify every model or system used to study the phenomenon (pesticide exposure and brain network
organization), e.g. the human cohort design (populations, n, ages, recruitment, comparison groups),
the exposure-assessment model (how "probable historic pesticide exposure" was estimated, time
windows, data source), the imaging acquisition, the brain-network construction (parcellation, edge
definition, thresholding), and the statistical model (mixed-effects network regression framework,
covariates). For each, state its limitations (e.g. cross-sectional design, proxy exposure measure,
confounding by urban/rural and socioeconomic differences).

Also, separately, list the main experimental models used in the wider literature on the same
phenomenon (developmental neurotoxicity of organophosphate and other pesticides): human birth
cohorts (e.g. CHAMACOS, Columbia CCCEH, Generation R), rodent (chlorpyrifos gestational/neonatal
exposure), zebrafish, and in vitro neural models. Label clearly which models are in this paper
and which are only in related work.

### 2. Biological processes and endpoints measured
Produce a table of the endpoints actually measured in the paper: the neuroimaging/network
measures (e.g. connection probability, clustering, global efficiency, degree, DMN-specific
topology), any cognitive or behavioural measures, and any exposure biomarkers. For each, give the
underlying biological process it is a readout of, and suggest the closest ontology terms where
reasonable (GO biological process, HPO phenotype, UBERON anatomy for DMN regions, ECTO exposure
term for pesticide/organophosphate exposure). Flag any suggested CURIE you are not sure of.
State the direction of each reported effect and the statistical strength as the paper reports it.

### 3. Disease relevance
Which diseases or disorders is this study relevant to, and how strongly? Consider at least:
neurodevelopmental disorders (ADHD, autism spectrum disorder, intellectual disability/learning
disability), pesticide/organophosphate poisoning and chronic organophosphate-induced
neurotoxicity, later-life neurodegeneration linked to pesticides (Parkinson disease), and
psychiatric disorders with DMN dysfunction (depression, schizophrenia). For each, rate relevance
(direct / indirect / speculative), give the mechanistic link (exposure -> molecular initiating
event such as acetylcholinesterase inhibition -> altered neurodevelopment -> DMN connectivity ->
cognitive phenotype), and cite the supporting literature with PMIDs. Be explicit that this paper
does not diagnose any disease in its participants.

### 4. Summary
A short summary of what this paper can and cannot support as evidence in a disease-mechanism
knowledge base, with exact quotes from the abstract or results that would be usable as evidence
snippets.


## Output

# Deep Research Report: Models, Measured Processes/Endpoints, and Disease Relevance of PMID:35429626

**Target paper:** Bahrami M, Simpson SL, Burdette JH, Lyday RG, Quandt SA, Chen H, Arcury TA, Laurienti PJ. *Altered default mode network associated with pesticide exposure in Latinx children from rural farmworker families.* NeuroImage 2022;256:119179. [PMID: 35429626](https://pubmed.ncbi.nlm.nih.gov/35429626/) (DOI: 10.1016/j.neuroimage.2022.119179; open access PMC9251855)

*Every factual claim about the paper below is traceable to the open-access full text. Items marked **[inference]** are interpretation, not statements made by the authors.*

---

## Summary

This paper is a **cross-sectional resting-state fMRI study** of 78 Latinx 8-year-old children — 48 from rural farmworker (FW) families and 30 from urban non-farmworker (NFW) families — that asks whether probable historic pesticide exposure is associated with the organization of the brain's **default mode network (DMN)**. The authors constructed whole-brain functional networks from a Shen 268-region parcellation, defined edges with Pearson correlations, and applied a **two-part mixed-effects network regression framework** (WFU_MMNET) that separately models the *probability* a connection exists and the *strength* of connections, correcting for multiple comparisons with an adaptive FDR procedure and covarying for sociodemographic and anatomical-distance factors. The headline result is specific and bounded: pesticide exposure is associated with a reorganization of **DMN-specific topology at the connection-probability level only** — higher exposure shifts DMN connections toward being governed more by local **clustering (segregation)** and less by **global efficiency (integration)**.

The effect is graded with exposure. In the primary group contrast (FW vs. NFW within the DMN), the probability–clustering interaction was β = 0.4790 (p < 0.0001) and the probability–global-efficiency interaction was β = −0.4793 (p < 0.0001). In a secondary analysis restricted to the 48 FW children, a continuous measure of parent-reported historic exposure (prenatal through 96 months) reproduced the same directional pattern (clustering β = 0.1444, p < 0.0001; global efficiency β = −0.0705, p = 0.0304). Crucially, **all connection-strength terms and all non-DMN (global) terms were non-significant**, making the finding a narrow, well-isolated signal rather than a diffuse whole-brain effect.

For a disease-mechanism knowledge base, this paper supplies one specific, citable mechanistic edge — *probable pesticide exposure → reorganized DMN connection-probability topology in developing children* — anchored in a vulnerable, understudied population. It provides **direct evidence relevant to organophosphate developmental neurotoxicity** and, through the DMN's established role in attention and higher cognition, to **ADHD and cognitive-deficit risk**. It is **indirectly relevant** to psychiatric disorders characterized by DMN dysfunction (depression, schizophrenia, autism) and **speculatively relevant** to later-life pesticide-linked neurodegeneration (Parkinson disease). The paper's hard limits must be stated plainly: it **diagnoses no disease** in its participants, measures **no cognitive or behavioral outcomes**, uses a **residential-proximity proxy rather than a pesticide biomarker**, and its **cross-sectional design cannot establish causality**.

---

## Key Findings

### Finding 1 — The core result: exposure-graded, DMN-specific topology reorganization at the connection-probability level

The paper's central claim is that **pesticide exposure is associated with default mode network-specific topological reorganization**, and that this signal appears specifically at the level of *whether a connection exists* (connection probability), not *how strong* existing connections are, and specifically *within the DMN*, not across the whole brain.

**Study system.** The cohort comprised **n = 78 children** (48 rural FW, 30 urban NFW), all Latinx, mean age ≈ 8.3–8.4 years. Brain networks were built from the **Shen 268-region functional parcellation**, with edges defined by **Pearson correlation** between regional time series (negative correlations set to zero). The DMN was represented by **37 regions of interest**. Analysis used the **two-part mixed-effects network regression** implemented in WFU_MMNET: Part I models connection probability with a logistic link; Part II models connection strength. Models were **adaptive-FDR corrected** and covaried for maternal education and race, preschool education, parents' occupation, and inter-ROI anatomical distance plus distance².

**Primary results (FW vs. NFW contrast, within DMN).** The probability–clustering interaction was **β_{r,COI×DMN×Clust} = 0.4790 (p < 0.0001)**, with a contrast sum **β_{r,COI×Clust} + β_{r,COI×DMN×Clust} = 0.5226 (p < 0.0001)** indicating that FW children's DMN connections are *more positively* governed by clustering. The probability–global-efficiency interaction was **β_{r,COI×DMN×Eglob} = −0.4793 (p < 0.0001)**, contrast sum **= −0.5058 (p < 0.0001)**, indicating FW children's DMN connections are *more negatively* related to global efficiency.

**Secondary results (continuous historic exposure, FW only, prenatal–96 months).** The same directional pattern held: probability–clustering **β = 0.1444 (p < 0.0001)**, contrast = 0.1284 (p = 0.0003); probability–efficiency **β = −0.0705 (p = 0.0304)**, contrast = −0.0759 (p = 0.0466). Low-exposure FW children resembled the NFW group; high-exposure FW children resembled the FW group as a whole.

**Specificity / negative controls.** Every **connection-strength** term was non-significant (p = 0.36–0.99), and every **non-DMN global** term was non-significant. This is what makes the finding interpretable: the effect is confined to DMN connection probability.

**Directional interpretation.** Higher exposure → DMN connection probability increasingly governed by **clustering (local segregation)** and decreasingly by **global efficiency (long-range integration)** — a shift toward a more segregated, less integrated DMN.

The authors' own verbatim framing captures both the result and its associational character:

> "We found that network topology was differently associated with the connection probability between FW and NFW children in the DMN. Our results also indicated that, among 48 FW children, historic reports of exposure to pesticides from prenatal to 96 months old were significantly associated with DMN topology, as hypothesized." — [PMID: 35429626](https://pubmed.ncbi.nlm.nih.gov/35429626/)

> "the observed associations between network connectivity/topology and historic exposure reports in FW children provide compelling evidence for a contribution of pesticide exposure on altering the DMN network organization in this vulnerable population" — [PMID: 35429626](https://pubmed.ncbi.nlm.nih.gov/35429626/)

### Finding 2 — Convergent prior evidence: organophosphate exposure alters DMN-constituent structure/connectivity, and the same farmworker-network signature appears in adults

Three independent human neuroimaging lines converge on DMN-region vulnerability and contextualize this paper's rationale and result:

1. **Rauh et al. 2012** ([PMID: 22547821](https://pubmed.ncbi.nlm.nih.gov/22547821/)) — structural MRI of 40 children found prenatal **chlorpyrifos** associated with cortical enlargement including the **cuneus/precuneus and mesial superior frontal gyrus** — core DMN midline hubs. Verbatim: *"enlarged superior frontal gyrus, gyrus rectus, cuneus, and precuneus along the mesial wall of the right hemisphere."*

2. **van den Dries et al. 2020** (Generation R; [PMID: 32805249](https://pubmed.ncbi.nlm.nih.gov/32805249/)) — in n = 518 preadolescents, prenatal **dimethyl-OP metabolites** were associated with lower fractional anisotropy (B = −1.00, 95% CI −1.80, −0.20 per 10-fold increase) in white-matter tracts interconnecting DMN regions. Verbatim: *"a 10-fold increase in averaged DM metabolite concentrations across pregnancy was associated with lower FA."*

3. **Bahrami et al. 2017** ([PMID: 28583619](https://pubmed.ncbi.nlm.nih.gov/28583619/)) — the same research group's adult Latino farmworker study found *"brain networks in farmworkers had more clustered and modular structures when compared to non-farmworkers,"* with erythrocyte cholinesterase activity tracking the differences. This mirrors the increased-segregation signature seen in the children's DMN and ties it to the cholinergic molecular anchor.

Together these establish that (a) DMN hub regions are structurally and microstructurally sensitive to prenatal OP exposure, and (b) the increased-segregation network phenotype is reproducible across the lifespan within this research program.

### Finding 3 — Disease relevance: direct for OP developmental neurotoxicity/ADHD-cognitive risk, indirect for psychiatric DMN disorders, speculative for Parkinson disease

The paper **diagnoses no disease**: only 3 of 78 children had any parent-reported learning disability, and no cognitive outcomes were measured. Disease relevance is therefore **mechanistic/exposure-pathway based**, graded as follows:

| Disease / disorder | Relevance | Mechanistic basis | Key citation(s) |
|---|---|---|---|
| Chronic OP developmental neurotoxicity | **Direct** | Prenatal OP exposure → lower mental development, attention problems | [PMID: 24291036](https://pubmed.ncbi.nlm.nih.gov/24291036/), [PMID: 26896854](https://pubmed.ncbi.nlm.nih.gov/26896854/) |
| ADHD / attention & learning phenotypes | **Indirect→Direct** | DMN implicated in ADHD; OP/pyrethroid exposure linked to ADHD | [PMID: 18824195](https://pubmed.ncbi.nlm.nih.gov/18824195/), [PMID: 20478945](https://pubmed.ncbi.nlm.nih.gov/20478945/) |
| Psychiatric DMN disorders (depression, schizophrenia, autism) | **Indirect** | DMN segregation/integration imbalance is a shared feature | [PMID: 18824195](https://pubmed.ncbi.nlm.nih.gov/18824195/) |
| Parkinson disease / later-life neurodegeneration | **Speculative** (for pediatric sample) | Pesticide exposure ~2-fold PD risk; developmental OP perturbs PD-risk gene transcription | [PMID: 23713084](https://pubmed.ncbi.nlm.nih.gov/23713084/), [PMID: 21968025](https://pubmed.ncbi.nlm.nih.gov/21968025/) |

Supporting verbatim evidence:

- *"Most of the studies evaluating prenatal exposure observed a negative effect on mental development and an increase in attention problems in preschool and school children."* — [PMID: 24291036](https://pubmed.ncbi.nlm.nih.gov/24291036/)
- *"We relate DMN dysfunction to dementia, schizophrenia, epilepsy, anxiety and depression, autism and attention deficit/hyperactivity disorder"* — [PMID: 18824195](https://pubmed.ncbi.nlm.nih.gov/18824195/)
- *"Exposure to paraquat or maneb/mancozeb was associated with about a 2-fold increase in risk."* — [PMID: 23713084](https://pubmed.ncbi.nlm.nih.gov/23713084/)
- *"Epidemiologic studies support a connection between organophosphate pesticide exposures and subsequent risk of Parkinson's disease"* — [PMID: 21968025](https://pubmed.ncbi.nlm.nih.gov/21968025/)

**The paper itself does not diagnose any disease in its participants** — this must be emphasized in any knowledge-base encoding.

### Finding 4 — Ontology mapping (verified) and the acetylcholinesterase molecular-initiating-event anchor

To represent this paper in a structured knowledge base, the following CURIEs were **verified via EBI OLS4**:

| Entity | Term | CURIE | Status |
|---|---|---|---|
| Precuneus (DMN hub) | precuneus cortex | UBERON:0006093 | verified |
| Posterior cingulate cortex | PCC | UBERON:0022353 | verified |
| Medial prefrontal cortex | mPFC | UBERON:4450000 | verified |
| Inferior parietal cortex | IPC | UBERON:0006088 | verified |
| Default mode network | (no UBERON class) | MeSH:D000082702 | verified |
| Exposure to pesticide | — | ECTO:0000530 | verified |
| Exposure to organophosphorus compound | — | ECTO:9000284 | verified |
| Specific learning disability | — | HP:0001328 | verified |
| Neurodevelopmental abnormality | — | HP:0012759 | verified |
| ADHD | — | HP:0007018 | verified |
| Autism | — | HP:0000717 | verified |
| Molecular initiating event | acetylcholinesterase inhibitor | CHEBI:38462 | verified |

**Flagged correction:** earlier iteration-1 guesses (ECTO:9000078, ECTO:9000541, UBERON:0002976, UBERON:0022352) were **incorrect** and are superseded by the verified IDs above.

The molecular-initiating-event anchor is **acetylcholinesterase inhibition**, the canonical OP mechanism, broadened by evidence that OP esters also act through **non-cholinergic pathways** (cAMP, glutamate/GABA, endocrine). Verbatim: *"organophosphate esters can alter neurodevelopmental processes by interfering with noncholinergic pathways at environmentally relevant doses"* ([PMID: 34612677](https://pubmed.ncbi.nlm.nih.gov/34612677/)). Lower-level mechanistic models (absent from the paper, present in related work) include **zebrafish** OP developmental neurotoxicity — chlorpyrifos → AChE inhibition + down-regulated *mbp/syn2a/α1-tubulin* + locomotor deficits ([PMID: 32730898](https://pubmed.ncbi.nlm.nih.gov/32730898/), [PMID: 29605586](https://pubmed.ncbi.nlm.nih.gov/29605586/), [PMID: 27018022](https://pubmed.ncbi.nlm.nih.gov/27018022/)). Verbatim zebrafish anchor: *"The STC test accurately detected the effect of 8 out of 11 neuroactive substances (chlorpyrifos, chlorpyrifos-oxon, diazinon..."* ([PMID: 32730898](https://pubmed.ncbi.nlm.nih.gov/32730898/)).

### Finding 5 — The residential-proximity exposure proxy is externally validated against autism, ADHD, and IQ loss

PMID:35429626 defines exposure as **parent-reported months living next to agricultural fields** — a residential-proximity proxy. Independent studies using the same proxy class or OP biomarkers link this exposure to downstream neurodevelopmental disease, strengthening the exposure arm of the inferred pathway:

| Study | Cohort | Exposure measure | Outcome | Effect |
|---|---|---|---|---|
| Shelton 2014 ([PMID: 24954055](https://pubmed.ncbi.nlm.nih.gov/24954055/)) | CHARGE | Residential proximity to OP application | ASD | ~60% ↑ risk; 2nd-trimester chlorpyrifos OR = 3.3 (1.5–7.4) |
| Gunier 2017 ([PMID: 28557711](https://pubmed.ncbi.nlm.nih.gov/28557711/)) | — | Prenatal proximity to OP use | IQ | −2.2 Full-Scale IQ points (−3.9, −0.5) |
| Sagiv 2018 ([PMID: 29701446](https://pubmed.ncbi.nlm.nih.gov/29701446/)) | CHAMACOS | Prenatal urinary DAP | Social behavior | +2.7 SRS-2 T-score points per 10-fold DAP (age 14) |
| Bouchard 2010 ([PMID: 20478945](https://pubmed.ncbi.nlm.nih.gov/20478945/)) | NHANES | Urinary DMAP | ADHD | OR = 1.55 (1.14–2.10) |
| Wagner-Schuman 2015 ([PMID: 26017680](https://pubmed.ncbi.nlm.nih.gov/26017680/)) | NHANES | Pyrethroid 3-PBA > LOD | ADHD | OR = 2.42 (1.06–5.57) |

Verbatim anchors:
- *"Proximity to organophosphates at some point during gestation was associated with a 60% increased risk for ASD, higher for third-trimester exposures"* — [PMID: 24954055](https://pubmed.ncbi.nlm.nih.gov/24954055/)
- *"We observed a decrease of 2.2 points [95% confidence interval (CI): −3.9, −0.5] in Full-Scale IQ"* — [PMID: 28557711](https://pubmed.ncbi.nlm.nih.gov/28557711/)
- *"A 10-fold increase in DMAP concentration was associated with an odds ratio of 1.55"* — [PMID: 20478945](https://pubmed.ncbi.nlm.nih.gov/20478945/)

---

## Study Models / Systems

### Models used *in this paper*

| Component | Description | Key limitations |
|---|---|---|
| **Human cohort design** | 78 Latinx children: 48 rural FW vs. 30 urban NFW; age ≈ 8.3–8.4 y; recruited from the PACE5 study of farmworker families | Cross-sectional; FW vs. NFW confounded by **urban/rural** and **socioeconomic** differences; modest n (esp. 30 NFW); single age snapshot |
| **Exposure-assessment model** | "Probable historic pesticide exposure" = **parent-reported months living adjacent to agricultural fields**, prenatal → 96 months; a residential-proximity proxy | **Proxy, not a biomarker**; parent recall bias; no chemical speciation; no dose/intensity; collinear with rural residence |
| **Imaging acquisition** | Resting-state fMRI | Standard rs-fMRI confounds (motion, physiological noise); no task validation of DMN function |
| **Network construction** | Shen 268-region parcellation; Pearson-correlation edges (negatives zeroed); DMN = 37 ROIs | Parcellation/thresholding choices affect topology; zeroing negatives discards anticorrelation information |
| **Statistical model** | Two-part mixed-effects network regression (WFU_MMNET): Part I = connection probability (logistic); Part II = strength; adaptive-FDR; covariates: maternal education/race, preschool education, parents' occupation, distance + distance² | Associational; residual confounding; covariate set cannot fully separate pesticide from poverty/rurality |

### Models in the wider literature (NOT in this paper)

- **Human birth cohorts:** CHAMACOS ([PMID: 29701446](https://pubmed.ncbi.nlm.nih.gov/29701446/)), Columbia CCCEH (Rauh, [PMID: 22547821](https://pubmed.ncbi.nlm.nih.gov/22547821/)), Generation R ([PMID: 32805249](https://pubmed.ncbi.nlm.nih.gov/32805249/)), CHARGE ([PMID: 24954055](https://pubmed.ncbi.nlm.nih.gov/24954055/)), ECHO, Rhea — these use **urinary DAP biomarkers** or **pesticide-use-registry proximity**, measures this paper's proxy approximates.
- **Rodent:** chlorpyrifos/diazinon/parathion gestational and neonatal exposure (e.g., [PMID: 18941570](https://pubmed.ncbi.nlm.nih.gov/18941570/), [PMID: 20026089](https://pubmed.ncbi.nlm.nih.gov/20026089/)).
- **Zebrafish:** chlorpyrifos and OP flame retardants → locomotor and transcriptional neurodevelopmental deficits ([PMID: 32730898](https://pubmed.ncbi.nlm.nih.gov/32730898/), [PMID: 29605586](https://pubmed.ncbi.nlm.nih.gov/29605586/), [PMID: 27018022](https://pubmed.ncbi.nlm.nih.gov/27018022/)).
- **In vitro:** PC12 and neuronal cultures revealing cAMP-cascade convergence ([PMID: 20026089](https://pubmed.ncbi.nlm.nih.gov/20026089/), [PMID: 21968025](https://pubmed.ncbi.nlm.nih.gov/21968025/)).

---

## Biological Processes and Endpoints Measured

| Endpoint (in paper) | Biological process it reads out | Ontology anchor (verified) | Direction & strength as reported |
|---|---|---|---|
| **DMN connection probability** | Existence of functional coupling between DMN regions | DMN = MeSH:D000082702; hubs UBERON:0006093 (precuneus), UBERON:0022353 (PCC), UBERON:4450000 (mPFC), UBERON:0006088 (IPC) | Primary effect — reorganized with exposure |
| **Clustering governing probability** | Local **functional segregation** | — | ↑ with exposure: β = 0.4790 (p<0.0001) group; 0.1444 (p<0.0001) continuous |
| **Global efficiency governing probability** | Long-range **functional integration** | — | ↓ with exposure: β = −0.4793 (p<0.0001) group; −0.0705 (p=0.0304) continuous |
| **Connection strength** | Magnitude of functional coupling | — | **No significant effects** (p = 0.36–0.99) |
| **Non-DMN (global) topology** | Whole-brain network organization | — | **No significant effects** (negative control) |
| **Exposure measure** | Probable historic pesticide/OP exposure | ECTO:0000530 (pesticide), ECTO:9000284 (organophosphorus) | Graded dose-response within FW group |

No cognitive, behavioral, or exposure-biomarker endpoints were measured in the paper. The molecular-initiating event (not measured here) is **acetylcholinesterase inhibition** (CHEBI:38462). **[inference]** The CURIEs above are proposed mappings; the DMN has no UBERON class, so MeSH D000082702 is used.

---

## Mechanistic Model / Interpretation

The findings assemble into a candidate **Adverse Outcome Pathway (AOP)** in which this paper supplies one specific, empirically supported edge (the DMN-reorganization step):

```
   Pesticide exposure            MOLECULAR INITIATING EVENT        NEURODEVELOPMENTAL         NETWORK-LEVEL                 COGNITIVE / CLINICAL
   (residential proximity,  -->  Acetylcholinesterase inhibition   PERTURBATION         -->  KEY EVENT                -->  OUTCOME
    prenatal-96 mo)              (± non-cholinergic: cAMP,     -->  (altered maturation        Reorganized DMN topology:     (future risk; NOT
    [ECTO:0000530 /              glutamate/GABA, endocrine)         of late-maturing           ↑ clustering/segregation,     measured in this paper)
     ECTO:9000284]               [CHEBI:38462]                      DMN hubs)                  ↓ global efficiency/          ADHD, cognitive deficit,
                                                                                               integration                   ASD traits, ...
    -- validated externally --   -- rodent/zebrafish/in vitro --    -- Rauh, Generation R --   <== THIS PAPER (35429626) ==  -- epidemiology --
```

The **direction of the network change** — more clustering, less global efficiency — denotes a DMN that is more locally segregated and less globally integrated. Because DMN hubs (precuneus/PCC, mPFC, IPC) are **late-maturing** and support self-referential and higher-order cognition, a developmentally-timed shift toward segregation is a biologically plausible substrate for the attention and cognitive phenotypes repeatedly linked to OP exposure in the epidemiological literature (Findings 3 and 5) **[inference]**. The adult farmworker replication of the increased-segregation signature ([PMID: 28583619](https://pubmed.ncbi.nlm.nih.gov/28583619/)), together with its link to erythrocyte cholinesterase activity, strengthens the mechanistic plausibility of the cholinergic anchor.

Importantly, the knowledge-base representation should encode this as an **association edge with a proxy exposure node**, not a causal/diagnostic edge. The paper supports the middle of the AOP; the molecular-initiating event and the clinical outcome are imported from other model systems and cohorts.

---

## Evidence Base

| PMID | Role | How it supports / challenges |
|---|---|---|
| [35429626](https://pubmed.ncbi.nlm.nih.gov/35429626/) | **Target paper** | Establishes exposure-graded DMN connection-probability reorganization (↑clustering, ↓efficiency) |
| [22547821](https://pubmed.ncbi.nlm.nih.gov/22547821/) | Supports | Prenatal chlorpyrifos alters precuneus/cuneus and mPFC — DMN hubs |
| [32805249](https://pubmed.ncbi.nlm.nih.gov/32805249/) | Supports | Large cohort: prenatal OP metabolites → lower white-matter FA in DMN-connecting tracts |
| [28583619](https://pubmed.ncbi.nlm.nih.gov/28583619/) | Supports | Same group: adult farmworkers show increased clustering/modularity tied to cholinesterase |
| [24291036](https://pubmed.ncbi.nlm.nih.gov/24291036/) | Supports | Prenatal OP → poorer mental development, attention problems |
| [26896854](https://pubmed.ncbi.nlm.nih.gov/26896854/) | Supports | Systematic review: prenatal OP → neurodevelopmental disturbances; pesticide → PD risk |
| [18824195](https://pubmed.ncbi.nlm.nih.gov/18824195/) | Supports | DMN dysfunction common across ADHD, autism, depression, schizophrenia |
| [23713084](https://pubmed.ncbi.nlm.nih.gov/23713084/) | Supports (speculative arm) | Pesticide exposure → ~2-fold Parkinson disease risk |
| [21968025](https://pubmed.ncbi.nlm.nih.gov/21968025/) | Supports (speculative arm) | Developmental OP exposure perturbs PD-risk gene transcription |
| [34612677](https://pubmed.ncbi.nlm.nih.gov/34612677/) | Supports (mechanism) | Non-cholinergic OP neurodevelopmental mechanisms |
| [32730898](https://pubmed.ncbi.nlm.nih.gov/32730898/), [29605586](https://pubmed.ncbi.nlm.nih.gov/29605586/), [27018022](https://pubmed.ncbi.nlm.nih.gov/27018022/) | Supports (lower-level models) | Zebrafish OP neurotoxicity: AChE inhibition, marker down-regulation, locomotor deficits |
| [24954055](https://pubmed.ncbi.nlm.nih.gov/24954055/), [28557711](https://pubmed.ncbi.nlm.nih.gov/28557711/), [29701446](https://pubmed.ncbi.nlm.nih.gov/29701446/), [20478945](https://pubmed.ncbi.nlm.nih.gov/20478945/), [26017680](https://pubmed.ncbi.nlm.nih.gov/26017680/) | Supports (exposure proxy validity + outcomes) | Proximity/biomarker proxies linked to ASD, IQ loss, ADHD |

---

## Limitations and Knowledge Gaps

1. **Cross-sectional design** — cannot establish causality or temporal ordering; no longitudinal trajectory.
2. **Proxy exposure** — parent-reported residential proximity, not a measured pesticide biomarker; no chemical speciation, no intensity/dose; subject to recall bias.
3. **Confounding by rurality and SES** — FW vs. NFW differ in urban/rural residence and socioeconomic status; covariate adjustment cannot fully disentangle pesticide exposure from correlated deprivation and environmental factors.
4. **No clinical or cognitive outcomes** — the paper measures network topology only; it **diagnoses no disease** and cannot link the DMN change to any behavioral phenotype in these children (only 3/78 had any parent-reported learning disability).
5. **Modest sample** — 78 total (30 NFW) limits power and generalizability.
6. **Analytic choices** — Shen-268 parcellation, correlation thresholding, and negative-edge zeroing all influence topology; robustness to alternative pipelines is untested here.
7. **Specificity but not localization** — the effect is DMN-specific and probability-specific, but the paper does not identify which individual DMN edges/hubs drive it.

---

## Proposed Follow-up Experiments / Actions

1. **Longitudinal re-imaging** of the PACE5 FW cohort to test whether the DMN segregation shift persists, worsens, or recovers, and whether it predicts later cognitive/attention outcomes.
2. **Add pesticide biomarkers** (urinary DAP metabolites, erythrocyte cholinesterase activity) to convert the proximity proxy into a quantified, speciated exposure and test dose-response at the molecular level.
3. **Couple imaging to cognition** — administer standardized attention/executive and IQ batteries (SRS-2, Conners, WISC) to directly connect DMN topology to clinically meaningful phenotypes.
4. **Edge-level localization** — identify which DMN hubs (precuneus/PCC vs. mPFC vs. IPC) drive the connection-probability effect to sharpen the UBERON-level knowledge-base annotation.
5. **Better control groups** — recruit rural non-farmworker and low-exposure rural children to decouple pesticide exposure from rurality/SES.
6. **Cross-species anchoring** — align the human DMN-segregation readout with zebrafish/rodent AChE-inhibition and connectivity endpoints to formalize the AOP from MIE to network key event.
7. **Knowledge-base encoding** — represent this as an *association* edge: `exposure to organophosphorus compound (ECTO:9000284) → altered DMN (MeSH:D000082702) connection-probability topology`, with the MIE node `acetylcholinesterase inhibitor (CHEBI:38462)` imported from related models and an explicit "no disease diagnosed" flag.

---

## What this paper can and cannot support as evidence

**Can support:** a specific, exposure-graded **association** between probable historic pesticide exposure and **DMN-specific connection-probability topology** (↑ clustering/segregation, ↓ global efficiency/integration) in developing Latinx children — a mechanistic key-event edge for an OP developmental-neurotoxicity knowledge base.

**Cannot support:** any disease diagnosis, any causal claim, any cognitive/behavioral outcome, or any molecular measurement — these must be imported from other cohorts and model systems.

**Usable verbatim evidence snippets (from the paper):**
- *"We found that network topology was differently associated with the connection probability between FW and NFW children in the DMN."*
- *"among 48 FW children, historic reports of exposure to pesticides from prenatal to 96 months old were significantly associated with DMN topology, as hypothesized."*
- *"the observed associations between network connectivity/topology and historic exposure reports in FW children provide compelling evidence for a contribution of pesticide exposure on altering the DMN network organization in this vulnerable population."*


## Artifacts

- [OpenScientist final report](PMID_35429626-paper-review-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PMID_35429626-paper-review-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 22 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.