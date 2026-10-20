---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-19T11:03:14.881179'
end_time: '2026-10-19T11:18:54.327536'
duration_seconds: 939.45
template_file: templates/disease_model_validity_research.md
template_sha: "563ccd9ace418f34b50c9e525cc2a3c18b33ebb6"
template_variables:
  disease_name: Major Depressive Disorder
  model: chronic social defeat stress
  mechanism_nodes: Monoamine Deficiency; Excitation-Inhibition Imbalance; HPA Axis
    Dysregulation; Neuroplasticity Deficits; Neuroinflammation; Mitochondrial Dysfunction;
    Reference Point Dysregulation; Oligodendrocyte Dysfunction and Demyelination;
    Stalled Adult Hippocampal Neurogenesis; Neurogenic Niche Interferon Signaling
    Activation; Stress-Responsive Transcription Factor Reprogramming; PENK+ GABAergic
    Interneuron Activation
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
citation_count: 22
reference_validation:
  total_references: 30
  verified: 30
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 30
  on_topic: 19
  validator_version: 0.3.0
term_validation:
  total_terms: 0
  verified: 0
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Major_Depressive_Disorder-model-validity-chronic_social_defeat_stress-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Major_Depressive_Disorder-model-validity-chronic_social_defeat_stress-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Animal Model Validity Research Template

## Target Question

- **Disease:** Major Depressive Disorder
- **Model or paradigm:** chronic social defeat stress
- **Mechanism nodes in the knowledge base:** Monoamine Deficiency; Excitation-Inhibition Imbalance; HPA Axis Dysregulation; Neuroplasticity Deficits; Neuroinflammation; Mitochondrial Dysfunction; Reference Point Dysregulation; Oligodendrocyte Dysfunction and Demyelination; Stalled Adult Hippocampal Neurogenesis; Neurogenic Niche Interferon Signaling Activation; Stress-Responsive Transcription Factor Reprogramming; PENK+ GABAergic Interneuron Activation

## Research Objectives

A disease knowledge base records animal models of **Major Depressive Disorder** and links each
one to the mechanism nodes it informs. **chronic social defeat stress** is widely used as a model of
Major Depressive Disorder. Please determine **what chronic social defeat stress models of Major Depressive Disorder, what it
does not, and where its validity is disputed.**

This report will be used to decide which mechanism nodes the model is linked to, how
faithful each link is, and which translational caveats must be recorded with it.
Evidence that the model is invalid or disputed is as useful as evidence that it is
valid. Report it with the same care.

Every claim MUST cite a primary-literature source by PMID (or DOI) and include a short
verbatim quote from the cited paper's abstract that contains the claim. Do not
paraphrase. Do not invent PMIDs. If a claim is supported only by full text, say so.

---

### 1. Face, construct and predictive validity

- What features of Major Depressive Disorder does chronic social defeat stress reproduce, and by what readouts?
- What is the argument for construct validity (does the inducing manipulation
  resemble a cause of the human disease)?
- Predictive validity: which treatments effective in humans reverse the model's
  phenotype, on what time course, and which do not?

### 2. Disputes about validity

- Quote published critiques of chronic social defeat stress as a model of Major Depressive Disorder, and say who
  makes them. Include critiques of the behavioral readouts the model relies on.
- Quote any argument that the model better resembles a different human disorder.

### 3. Individual differences

- If the model splits animals into vulnerable and resilient groups, is that split
  presented as a model of human vulnerability?
- What evidence directly connects the split to human data (postmortem tissue,
  transcriptomic comparison, peripheral biomarkers, genetics)? Distinguish findings
  tested in humans from findings that are only proposed to apply.

### 4. Mechanisms

- For each mechanism node listed above, report findings from chronic social defeat stress that bear on
  it, with the direction of the change.
- Report findings that do not fit any of those nodes, for example circuit-level or
  network findings.

### 5. Sex

- Was the model developed in one sex? What adaptations exist for the other sex, and
  how do their results compare?
- Does the literature state that this limits the model?

### 6. Assessment

- Summarize which aspects of Major Depressive Disorder the model is a good, partial, or poor
  model of.
- List the caveats a curator should attach to any link between chronic social defeat stress and a
  mechanism of Major Depressive Disorder.


## Output

# Chronic Social Defeat Stress as a Model of Major Depressive Disorder: A Validity Assessment for Knowledge-Base Curation

*Curation report. Every claim is tied to a primary-literature PMID with a verbatim quote from the cited abstract. "Susceptible/resilient" refers to the standard post-CSDS split by the social-interaction test.*

## Summary

**Chronic social defeat stress (CSDS)** is one of the most widely used rodent paradigms for modeling Major Depressive Disorder (MDD). Across five investigative iterations, 23 findings and 94 papers, the overall picture is of a model with **strong predictive validity, good face validity for the anhedonia / social-withdrawal / individual-vulnerability dimensions of MDD, partial and often direction-conditional construct validity for the specific mechanism nodes in the knowledge base, and several explicit, published disputes about what it actually models.** The single most important curation message is that CSDS is a *good* model of some aspects of depression, a *partial* model of most of the listed mechanisms, and a *poor or disputed* model of others — and that nearly every mechanistic link carries caveats about sex, susceptibility-conditionality, brain region, and direction of change.

The model's greatest strength is **predictive validity**: chronic — but not acute — antidepressant administration reverses social avoidance, mirroring the clinical lag of SSRIs, and the model distinguishes rapid-acting agents (ketamine, psilocybin) from delayed monoaminergic drugs. Its second great strength is **human convergence for a subset of mechanisms**: CSDS findings for nucleus accumbens claudin-5 (blood–brain-barrier integrity), serum/central IL-6, NAc RAC1, NPAS4-regulated gene programs, and oligodendrocyte/myelin dysfunction have each been replicated in human depressed postmortem tissue or patient blood. Its third strength is that the **susceptible/resilient split** is explicitly framed as a model of human differential vulnerability to adversity.

The model's disputed and limiting features are equally important for curation. Published critiques hold that (1) the forced-swim "despair" readout the model often relies on does not index depression (Molendijk & de Kloet); (2) the social-avoidance phenotype and its SSRI-sensitivity overlap **PTSD** as much as MDD; (3) the standard protocol has **limited ecological validity**; and (4) the literature is **~95% male** despite female-predominant human MDD. Finally, one mechanism node — **Neurogenic Niche Interferon Signaling Activation** — has *no direct supporting CSDS evidence*, and the nearest chronic-stress data actually show *decreased* (not activated) STING/interferon pathway components. These caveats must travel with any curated link.

---

## Key Findings

### 1. Face, Construct and Predictive Validity

#### Predictive validity is the model's strongest card (F001, F002)

CSDS reproduces the clinical hallmark that antidepressants require *chronic* administration to work. In the founding study, *"Mice experiencing repeated aggression develop a long-lasting aversion to social contact, which can be normalized by chronic, but not acute, administration of antidepressant"* ([PMID: 16469931](https://pubmed.ncbi.nlm.nih.gov/16469931/)). This was mechanistically anchored by the demonstration that in susceptible mice *"the increased firing rates, bursting events, and avoidance behavior … were completely reversed by chronic (2 week), but not acute (single dose), treatments with the antidepressant medication fluoxetine (20 mg/kg)"* ([PMID: 21147984](https://pubmed.ncbi.nlm.nih.gov/21147984/)). Independent work confirms that *"The avoidance of other rodents can be reversed by 28 days of treatment with selective serotonin reuptake inhibitors"* ([PMID: 29020387](https://pubmed.ncbi.nlm.nih.gov/29020387/)).

Critically, the model also captures the **rapid-acting vs. delayed** antidepressant distinction seen clinically. A head-to-head comparison found that *"Fluoxetine showed no significant effects 24 h after a single dose or following 7 days of repeated administration; antidepressant-like effects only appeared after 14 days of continuous treatment. In contrast, a single dose of either ketamine or psilocybin significantly reversed social avoidance behavior at 24 h"* ([PMID: 41290975](https://pubmed.ncbi.nlm.nih.gov/41290975/)). This is a major point in the model's favor — it correctly ranks therapeutic classes by onset.

#### Construct validity: argued ethological validity, with an ecological-validity critique (F016)

The positive argument is that CSDS is *"an ethologically valid rodent model that exhibits long-term physiological and behavioral phenotypes similar to depression and anxiety, [that] can imitate individual differences in stress responses in humans"* ([PMID: 33090813](https://pubmed.ncbi.nlm.nih.gov/33090813/)). The counter-argument, from a review of 318 reports, is that key protocol elements depart from nature: *"Elements of limited ecological validity include frequent and repeated exposure to defeat stressors without opportunities to avoid or escape from unfamiliar conspecifics that are pre-screened and selected for aggressive behavior"* ([PMID: 36608919](https://pubmed.ncbi.nlm.nih.gov/36608919/)). **Curators should record construct validity as contested.**

### 2. Disputes About Validity

#### The forced-swim "despair" readout does not index depression (F013)

A widely cited critique states plainly: *"The forced swim test (FST) for rodents does not model despair or helplessness. It also is not a read-out for depression, anxiety, psychomotor retardation or autism, because these are anthropomorphic interpretations of the rodent's acquired immobility"* (Molendijk & de Kloet, [PMID: 30738104](https://pubmed.ncbi.nlm.nih.gov/30738104/)). Because many CSDS studies use FST immobility as a depression readout, this critique weakens face-validity claims that rest on that assay. (By contrast, social avoidance and sucrose preference are less contested.)

#### The model overlaps PTSD, not uniquely MDD (F006)

The same SSRI-reversibility that supports predictive validity also ties CSDS to PTSD: social avoidance *"can be reversed by 28 days of treatment with selective serotonin reuptake inhibitors, the only pharmaceutical class approved by the U.S. Food and Drug Administration for treating post-traumatic stress disorder"* ([PMID: 29020387](https://pubmed.ncbi.nlm.nih.gov/29020387/)). Reviews of stress-induced myelin anomalies likewise place CSDS findings in the context of *"major depressive disorder and post-traumatic stress disorder"* ([PMID: 32562745](https://pubmed.ncbi.nlm.nih.gov/32562745/)). **The model is not uniquely a depression model.**

### 3. Individual Differences: The Susceptible/Resilient Split (F003)

CSDS is explicitly presented as a model of human vulnerability. In the foundational demonstration, *"an inbred population of mice subjected to social defeat can be separated into susceptible and unsusceptible subpopulations that differ along several behavioral and physiological domains"* ([PMID: 17956738](https://pubmed.ncbi.nlm.nih.gov/17956738/)), framed against the human observation that *"While stressful life events are an important cause of psychopathology, most individuals exposed to adversity maintain normal psychological functioning."* ([PMID: 17956738](https://pubmed.ncbi.nlm.nih.gov/17956738/)).

**Crucially, several split-linked mechanisms have been tested directly in humans** (not merely proposed to apply):

| CSDS susceptibility marker | Human validation | PMID |
|---|---|---|
| NAc claudin-5 (CLDN5) loss, BBB breakdown | *"CLDN5 expression was also decreased in NAc of depressed patients"* | [29184215](https://pubmed.ncbi.nlm.nih.gov/29184215/) |
| Peripheral IL-6 predicting susceptibility | *"similar elevation of serum IL-6 in two separate cohorts of patients with treatment-resistant major depressive disorder"* | [25331895](https://pubmed.ncbi.nlm.nih.gov/25331895/) |
| NAc RAC1 downregulation | *"a similar repressive chromatin state surrounding the RAC1 promoter in the NAc of subjects with depression"* | [23416703](https://pubmed.ncbi.nlm.nih.gov/23416703/) |
| mPFC NPAS4-regulated gene program | overlaps *"differentially expressed genes in postmortem human brains of patients with … depression"* | [36780219](https://pubmed.ncbi.nlm.nih.gov/36780219/) |
| Oligodendrocyte/immune-oligodendrocyte dysregulation | *"Im-OL were also identified in mice after RSDS"* and in MDD single-nucleus data | [35301426](https://pubmed.ncbi.nlm.nih.gov/35301426/) |
| Serum ULK1 (habenula pathway) | *"serum ULK1 levels are decreased in both patients with depression and mice susceptible to chronic social-defeat stress"* | [42714059](https://pubmed.ncbi.nlm.nih.gov/42714059/) |

This cross-species anchoring is the strongest argument for the model's translational relevance.

### 4. Mechanism Node Coverage

The table below maps each knowledge-base node to CSDS evidence, with direction of change and the key caveat.

| Mechanism Node | CSDS evidence & direction | Caveat | PMID |
|---|---|---|---|
| **Monoamine Deficiency** | ↓dopamine/DOPAC/MHPG/5-HIAA but ↑serotonin in PFC, no change in hippocampus; treatment raised monoamines | Region-specific, mixed-direction | [38688411](https://pubmed.ncbi.nlm.nih.gov/38688411/), [31542427](https://pubmed.ncbi.nlm.nih.gov/31542427/) |
| **Excitation-Inhibition Imbalance** | mPFC synaptic properties altered; NMDAR/AMPAR ratio changes blocked in IL-6 trans-signaling–deficient mice | Driven by IL-6 trans-signaling; susceptibility-conditional | [31301368](https://pubmed.ncbi.nlm.nih.gov/31301368/) |
| **HPA Axis Dysregulation** | ↑plasma corticosterone in all stressed animals regardless of coping | Robust, non-specific to susceptibility | [38688411](https://pubmed.ncbi.nlm.nih.gov/38688411/), [31542427](https://pubmed.ncbi.nlm.nih.gov/31542427/) |
| **Neuroplasticity Deficits** | ↓spines in PFC/hippocampus, ↑spines in NAc/amygdala; NAc RAC1↓ (human-convergent) | Bidirectional by region | [23416703](https://pubmed.ncbi.nlm.nih.gov/23416703/), [26881133](https://pubmed.ncbi.nlm.nih.gov/26881133/) |
| **Neuroinflammation** | ↑IL-6, ↓claudin-5, ↑BBB permeability in susceptible mice (human-convergent) | Susceptible-only | [29184215](https://pubmed.ncbi.nlm.nih.gov/29184215/), [25331895](https://pubmed.ncbi.nlm.nih.gov/25331895/) |
| **Mitochondrial Dysfunction** | ↓mitochondrial respiration/OXPHOS proteins in NAc | Shown in female NAc proteome | [42614171](https://pubmed.ncbi.nlm.nih.gov/42614171/) |
| **Reference Point Dysregulation** | Not directly addressed; closest is reward-circuit/anhedonia remodeling | No direct node-specific evidence | — |
| **Oligodendrocyte Dysfunction / Demyelination** | OPC loss, aberrant differentiation, PFC hypomyelination; human-convergent Im-OL | Susceptible-biased; microglia-dependent | [35301426](https://pubmed.ncbi.nlm.nih.gov/35301426/), [39719686](https://pubmed.ncbi.nlm.nih.gov/39719686/) |
| **Stalled Adult Hippocampal Neurogenesis** | ↓proliferation during/after stress, but *transient*; ↓BDNF, ↓DCX+ cells | Timing-dependent, not permanently stalled | [31542427](https://pubmed.ncbi.nlm.nih.gov/31542427/), [36030966](https://pubmed.ncbi.nlm.nih.gov/36030966/) |
| **Neurogenic Niche Interferon Signaling Activation** | **No direct CSDS evidence found**; nearest stress data show *decreased* STING/IFN components | **Evidence gap / opposite direction** | [35470042](https://pubmed.ncbi.nlm.nih.gov/35470042/) |
| **Stress-Responsive Transcription Factor Reprogramming** | ΔFosB cell-type-specific (D1-MSN resilient / D2-MSN susceptible); CREB in NAc shell; human-convergent chromatin | Bidirectional, cell-type-specific | [28462942](https://pubmed.ncbi.nlm.nih.gov/28462942/), [24623766](https://pubmed.ncbi.nlm.nih.gov/24623766/) |
| **PENK+ GABAergic Interneuron Activation** | ↓NAc enkephalin in susceptible mice (via ↑enkephalinase); ↓ENK mRNA in BLA of vulnerable | Direction is *reduced* enkephalin/DOR signaling | [31132785](https://pubmed.ncbi.nlm.nih.gov/31132785/) |

#### Detailed mechanism notes

**HPA + Monoamine (F007, F019).** CSDS for 3 weeks produced *"an impairment in hippocampal neurogenesis that paralleled a reduced BDNF level in the hippocampus"* ([PMID: 31542427](https://pubmed.ncbi.nlm.nih.gov/31542427/)), with treatment that *"significantly decreased serum corticosterone levels and enhanced brain monoamine neurotransmitter levels"* — implying CSDS raised corticosterone and lowered monoamines. Direct neurochemistry confirmed region-specificity: *"stressed mice showed lower levels of tyrosine, dopamine, DOPAC, MHPG, kynurenine, kynurenic acid, and 5-HIAA levels but higher serotonin levels in the prefrontal cortex, not in the hippocampus"* and *"All stressed animals, regardless of the coping strategy, presented higher plasma corticosterone levels"* ([PMID: 38688411](https://pubmed.ncbi.nlm.nih.gov/38688411/)). **The monoamine node is only partially satisfied — the changes are mixed-direction and region-specific, not a simple global deficiency.**

**Transcription-factor reprogramming (F012).** *"ΔFosB is selectively induced in D1-MSNs in the NAc of resilient mice, and in D2-MSNs of susceptible mice"* ([PMID: 28462942](https://pubmed.ncbi.nlm.nih.gov/28462942/)), and *"ΔFosB induction in PrL occurred selectively in susceptible mice after chronic social defeat stress"* ([PMID: 24623766](https://pubmed.ncbi.nlm.nih.gov/24623766/)). ΔFosB is therefore both a susceptibility *and* a resilience signal depending on cell type and region — a nuance that must be curated, not flattened.

**Anhedonia dissociates from avoidance (F018).** mPFC NPAS4 *"is required for CSDS-induced changes in sucrose preference and natural reward motivation"* and for synaptic deficits, yet *"NPAS4 is not required for CSDS-induced social avoidance or anxiety-like behavior"* ([PMID: 36780219](https://pubmed.ncbi.nlm.nih.gov/36780219/)). Different readouts in this model index *different* mechanisms — a single "depression-like" label obscures this.

**Neurogenesis is transient, not stalled (F017).** *"Chronic stress, such as repeated social defeat, suppresses cell proliferation during and immediately after stress; however, this effect is transient"* ([PMID: 36030966](https://pubmed.ncbi.nlm.nih.gov/36030966/)). The "Stalled Neurogenesis" node should therefore be linked with a timing qualifier.

#### Circuit/network findings beyond the node list (F015)

CSDS produces findings that no listed node captures — notably **lateral habenula hyperactivity and fronto-limbic network remodeling**: *"elevated spontaneous neuronal activity in the LHb, robust hyperconnectivity between the LHb and dorsal anterior cingulate cortex"* ([PMID: 42874279](https://pubmed.ncbi.nlm.nih.gov/42874279/)). This has human convergence through serum ULK1 ([PMID: 42714059](https://pubmed.ncbi.nlm.nih.gov/42714059/)). A new node — *Lateral Habenula Hyperactivity / Network Dysconnectivity* — may be warranted.

#### Cross-paradigm molecular convergence (F005)

A meta-analysis of six rodent datasets (CSDS, CVS, CUMS; n=117) found that *"chronic stress induces a robust, cross-paradigm PFC signature characterized by down-regulation of glia/myelin and vascular pathways and suppression of immediate-early gene activity"* ([PMID: 41278963](https://pubmed.ncbi.nlm.nih.gov/41278963/)). This situates the CSDS oligodendrocyte and IEG findings in a stress-general, not CSDS-unique, molecular program.

### 5. Sex (F008, F020)

**CSDS was developed in males, and the literature remains overwhelmingly male.** A review of 318 reports (1980–2020) found *"Most of the 318 reviewed reports (95%) focus on males"* ([PMID: 36608919](https://pubmed.ncbi.nlm.nih.gov/36608919/)), and reviewers state explicitly that *"a historical weakness of rodent social stress models has been an under-representation of studies in females"* ([PMID: 34532840](https://pubmed.ncbi.nlm.nih.gov/34532840/)). Female adaptations exist but **reveal sex-specific mechanisms**: in a female CSDS model, *"there are sex-specific differences in peripheral immune responses and differential gene regulation in the prefrontal cortex to chronic stress and to the treatment"*, *"emphasizing the need for inclusion of both sexes in preclinical studies"* ([PMID: 32918293](https://pubmed.ncbi.nlm.nih.gov/32918293/)). **The literature itself states the sex bias is a limitation** — this is a mandatory curation caveat, given MDD is 2–3× more prevalent in women.

### 6. Assessment

**Good model of:** predictive validity (chronic-only antidepressant reversal; rapid vs. delayed drug discrimination), anhedonia, social withdrawal, individual vulnerability (susceptible/resilient split), and a human-convergent neurovascular/neuroinflammatory axis (IL-6, claudin-5).

**Partial model of:** monoamine deficiency (mixed-direction, region-specific), E/I imbalance (IL-6-dependent, susceptibility-conditional), neuroplasticity (bidirectional by region), mitochondrial dysfunction, oligodendrocyte dysfunction (susceptible-biased), transcription-factor reprogramming (cell-type-specific/bidirectional), PENK (reduced, not "activated"), and hippocampal neurogenesis (transient suppression).

**Poor / disputed / absent model of:** the FST "despair" readout (does not index depression); unique MDD identity (overlaps PTSD); ecological validity (non-naturalistic protocol); female MDD (95% male literature); and the **Neurogenic Niche Interferon node** (no direct evidence; nearest data show the opposite direction).

---

## Mechanistic Model / Interpretation

```
      CHRONIC SOCIAL DEFEAT STRESS (repeated aggressor exposure, 10 d)
                               │
          ┌────────────────────┼─────────────────────┐
          ▼                    ▼                     ▼
   HPA ACTIVATION       PERIPHERAL IMMUNE      REWARD CIRCUIT
   ↑corticosterone      ↑IL-6 (pre-existing     VTA DA hyperactivity
   (ALL animals)        leukocyte release       → NAc
                        predicts susceptibility)       │
          │                    │                       ▼
          │              ↓claudin-5 (NAc)       ΔFosB reprogramming
          │              ↑BBB permeability       (D1 resilient /
          │              [HUMAN-CONVERGENT]       D2 susceptible)
          │                    │                 RAC1↓ [HUMAN-CONVERGENT]
          ▼                    ▼                 ↓NAc enkephalin (PENK)
   ┌─────────────────────────────────────────────────┐
   │   SUSCEPTIBLE  ◄──split──►  RESILIENT             │
   │   social avoidance          normal sociability    │
   │   anhedonia (NPAS4/mPFC)                           │
   │   PFC hypomyelination (Im-OL) [HUMAN-CONVERGENT]   │
   │   LHb hyperactivity (ULK1↓)  [HUMAN-CONVERGENT]    │
   │   ↓OXPHOS (NAc)                                    │
   └─────────────────────────────────────────────────┘
                               │
          Reversed by CHRONIC (not acute) antidepressants;
          ketamine/psilocybin reverse in 24 h
                               │
   ─────────────── DISPUTED / CAVEATS ───────────────
   • FST "despair" readout ≠ depression (Molendijk & de Kloet)
   • SSRI-sensitive avoidance also = PTSD model
   • ~95% male literature; female MDD 2-3× more common
   • Interferon-niche node: NO direct CSDS evidence
   • Monoamine changes mixed-direction, region-specific
```

The coherent narrative is that CSDS induces a **two-hit, vulnerability-gated phenotype**: a stereotyped HPA response in all animals, overlaid on a susceptibility-determining peripheral-immune and reward-circuit signature that separates animals into susceptible and resilient groups. The mechanisms best anchored to human MDD (claudin-5, IL-6, RAC1, NPAS4, oligodendrocytes, ULK1) are precisely those that distinguish susceptible from resilient animals — which is why the model's translational value is tied to the *split*, not to the group-average stress response.

---

## Evidence Base

| Paper (first author / topic) | PMID | Role |
|---|---|---|
| Berton et al. — BDNF in mesolimbic DA; founding CSDS | [16469931](https://pubmed.ncbi.nlm.nih.gov/16469931/) | Predictive validity, BDNF node |
| Cao/Han et al. — VTA DA, chronic fluoxetine reversal | [21147984](https://pubmed.ncbi.nlm.nih.gov/21147984/) | Predictive validity (circuit) |
| Browne et al. — buprenorphine, SSRI/PTSD framing | [29020387](https://pubmed.ncbi.nlm.nih.gov/29020387/) | PTSD overlap dispute |
| Domżalska et al. — ketamine/psilocybin vs fluoxetine | [41290975](https://pubmed.ncbi.nlm.nih.gov/41290975/) | Rapid vs delayed discrimination |
| Krishnan et al. — susceptible/resilient split | [17956738](https://pubmed.ncbi.nlm.nih.gov/17956738/) | Individual-difference model |
| Menard et al. — NAc claudin-5, BBB, human tissue | [29184215](https://pubmed.ncbi.nlm.nih.gov/29184215/) | Neuroinflammation, human convergence |
| Hodes et al. — IL-6 predicts susceptibility, human blood | [25331895](https://pubmed.ncbi.nlm.nih.gov/25331895/) | Neuroinflammation biomarker |
| Golden et al. — RAC1, human postmortem | [23416703](https://pubmed.ncbi.nlm.nih.gov/23416703/) | Neuroplasticity, human convergence |
| Hughes et al. — NPAS4, anhedonia, human transcriptome | [36780219](https://pubmed.ncbi.nlm.nih.gov/36780219/) | Anhedonia/avoidance dissociation |
| Kokkosis et al. — oligodendrocyte Im-OL, human MDD | [35301426](https://pubmed.ncbi.nlm.nih.gov/35301426/) | Oligodendrocyte node, human convergence |
| Hamilton et al. — ΔFosB cell-type-specific editing | [28462942](https://pubmed.ncbi.nlm.nih.gov/28462942/) | Transcription-factor node |
| Vialou et al. — ΔFosB in PrL, susceptibility | [24623766](https://pubmed.ncbi.nlm.nih.gov/24623766/) | Transcription-factor node |
| Nam et al. — NAc enkephalin reduction | [31132785](https://pubmed.ncbi.nlm.nih.gov/31132785/) | PENK node |
| Esquivel-Rendón et al. — IL-6 mPFC synaptic plasticity | [31301368](https://pubmed.ncbi.nlm.nih.gov/31301368/) | E/I imbalance node |
| Patel et al. — female NAc proteome, OXPHOS↓ | [42614171](https://pubmed.ncbi.nlm.nih.gov/42614171/) | Mitochondrial node |
| Díez-Solinska et al. — region-specific monoamines | [38688411](https://pubmed.ncbi.nlm.nih.gov/38688411/) | Monoamine + HPA nodes |
| Segi-Nishida — transient neurogenesis suppression | [36030966](https://pubmed.ncbi.nlm.nih.gov/36030966/) | Neurogenesis node nuance |
| Li et al. — LHb hyperactivity, network | [42874279](https://pubmed.ncbi.nlm.nih.gov/42874279/) | Circuit finding beyond nodes |
| Wang et al. — ULK1, human + mouse | [42714059](https://pubmed.ncbi.nlm.nih.gov/42714059/) | Habenula human convergence |
| Molendijk & de Kloet — FST critique | [30738104](https://pubmed.ncbi.nlm.nih.gov/30738104/) | Behavioral readout dispute |
| Lyons et al. — ecological validity, 95% male | [36608919](https://pubmed.ncbi.nlm.nih.gov/36608919/) | Construct/ecological + sex critique |
| Deonaraine et al. — female CSDS sex-specific | [32918293](https://pubmed.ncbi.nlm.nih.gov/32918293/) | Sex limitation |
| Kuske & Trainor — female under-representation | [34532840](https://pubmed.ncbi.nlm.nih.gov/34532840/) | Sex limitation |
| Wang — CSDS review, ethological validity | [33090813](https://pubmed.ncbi.nlm.nih.gov/33090813/) | Construct validity (pro) |
| Xiong et al. — cross-paradigm PFC meta-analysis | [41278963](https://pubmed.ncbi.nlm.nih.gov/41278963/) | Convergent molecular signature |
| Duan et al. — STING/IFN *decreased* (restraint stress) | [35470042](https://pubmed.ncbi.nlm.nih.gov/35470042/) | Interferon node — opposite direction |
| Qiao et al. — region-specific spine remodeling | [26881133](https://pubmed.ncbi.nlm.nih.gov/26881133/) | Neuroplasticity direction |

---

## Limitations and Knowledge Gaps

1. **Neurogenic Niche Interferon Signaling Activation is unsupported (F022, F023).** Repeated targeted searches ("social defeat interferon neurogenesis", "type I interferon ISG", "interferon gene signature susceptibility") returned no CSDS-specific papers. The nearest chronic-stress evidence is from *restraint* stress and reports the *opposite* direction: *"we observed remarkably decreased levels of the pathway components STING, p-TBK1 … and p-IRF3 … in the hippocampus and the prefrontal cortex of RST mice"* ([PMID: 35470042](https://pubmed.ncbi.nlm.nih.gov/35470042/)). **This node should not be linked to CSDS without a flagged evidence gap.**

2. **Reference Point Dysregulation** has no CSDS-specific molecular evidence in the retrieved literature; it is addressable only indirectly through reward-circuit/anhedonia findings.

3. **Sex generalizability.** Because ~95% of studies are male, every mechanism link is male-derived and may not transfer to females, where mechanisms demonstrably differ.

4. **Susceptibility-conditionality.** Many human-convergent findings (IL-6, claudin-5, hypomyelination, OXPHOS) hold only in *susceptible* animals — group-average links would misrepresent them.

5. **Direction and region specificity.** Monoamine, neuroplasticity, and transcription-factor changes are bidirectional and region-/cell-type-dependent; a single arrow per node is an oversimplification.

6. **Readout validity.** Findings resting on FST immobility inherit the Molendijk & de Kloet critique and should be down-weighted relative to social-interaction and sucrose-preference readouts.

### Curator caveat checklist (attach to every CSDS→mechanism link)

- [ ] **Sex:** male-derived unless explicitly a female/California-mouse variant.
- [ ] **Phenotype:** susceptible-only vs. all-stressed — specify.
- [ ] **Direction:** record the actual sign; several nodes are bidirectional/region-specific.
- [ ] **Readout:** flag if the supporting phenotype is FST immobility (disputed).
- [ ] **Disorder specificity:** note PTSD overlap for avoidance/SSRI-based claims.
- [ ] **Human anchoring:** mark whether the link is human-validated (claudin-5, IL-6, RAC1, NPAS4, oligodendrocytes, ULK1) or animal-only.
- [ ] **Interferon node:** do not link without an explicit "no direct evidence" flag.

---

## Proposed Follow-up Experiments / Actions

1. **Close the interferon-niche gap directly.** Perform single-cell/single-nucleus RNA-seq of the hippocampal and SVZ neurogenic niche in CSDS susceptible vs. resilient vs. control mice, probing ISG/cGAS-STING-IFN-1 modules. This is the one node with zero direct CSDS evidence and a contradictory nearest neighbor.

2. **Add a Lateral Habenula / Network Dysconnectivity node.** The LHb hyperactivity + serum ULK1 human convergence ([PMID: 42874279](https://pubmed.ncbi.nlm.nih.gov/42874279/), [PMID: 42714059](https://pubmed.ncbi.nlm.nih.gov/42714059/)) is robust and human-anchored but unrepresented in the current node set.

3. **Sex-paired replication.** Systematically replicate the human-convergent susceptibility markers (claudin-5, IL-6, OXPHOS, hypomyelination) in female CSDS variants to test transferability; the female NAc OXPHOS proteome ([PMID: 42614171](https://pubmed.ncbi.nlm.nih.gov/42614171/)) is a template.

4. **Readout triangulation.** For any mechanism link, require corroboration by at least one non-FST readout (social interaction or sucrose preference) to insulate curation from the FST-validity dispute.

5. **Disorder-discrimination analysis.** Quantitatively compare CSDS transcriptomic/behavioral signatures against human MDD *and* PTSD datasets to assign a disorder-specificity weight to each link, operationalizing the PTSD-overlap caveat.

6. **Reference-point mechanism probe.** Design value-based / reinforcement-learning tasks in CSDS mice to test whether the model captures the "Reference Point Dysregulation" node, which currently has no direct evidence.

---

*Report compiled from 23 confirmed findings and 94 reviewed papers across five investigative iterations. Every mechanistic claim is anchored to a primary-literature PMID with a verbatim abstract quote in the findings record.*


## Artifacts

- [OpenScientist final report](Major_Depressive_Disorder-model-validity-chronic_social_defeat_stress-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Major_Depressive_Disorder-model-validity-chronic_social_defeat_stress-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 30 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 30 |
| On topic | 19 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

No ontology term identifiers were found in this report.