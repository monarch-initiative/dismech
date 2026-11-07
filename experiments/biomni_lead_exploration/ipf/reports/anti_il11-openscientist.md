---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-06T18:31:03.303766'
end_time: '2026-11-06T18:45:16.011151'
duration_seconds: 852.71
template_file: experiments/biomni_lead_exploration/repurposing_template.md
template_variables:
  disease_name: Idiopathic Pulmonary Fibrosis
  drug: an anti-IL-11 or anti-IL-11RA monoclonal antibody
  drug_action: neutralising interleukin-11 or blocking its receptor IL11RA
  mechanism: autocrine IL-11 signalling in lung fibroblasts driving myofibroblast
    differentiation and extracellular matrix production
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
citation_count: 18
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 17
  quotes_valid: 17
  relevance_assessed: 18
  on_topic: 16
  off_topic: 1
  off_topic_references:
  - PMID:12423677
  needs_review: true
  validator_version: 0.5.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: anti_il11-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: anti_il11-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Drug Repurposing Hypothesis Assessment

## The Hypothesis

- **Disease:** Idiopathic Pulmonary Fibrosis
- **Drug:** an anti-IL-11 or anti-IL-11RA monoclonal antibody
- **Drug's target and action:** neutralising interleukin-11 or blocking its receptor IL11RA
- **Disease mechanism the drug would act on:** autocrine IL-11 signalling in lung fibroblasts driving myofibroblast differentiation and extracellular matrix production

The hypothesis is that an anti-IL-11 or anti-IL-11RA monoclonal antibody, by neutralising interleukin-11 or blocking its receptor IL11RA, would benefit patients with
Idiopathic Pulmonary Fibrosis because it interrupts "autocrine IL-11 signalling in lung fibroblasts driving myofibroblast differentiation and extracellular matrix production". Your job is to assess this
hypothesis, not to advocate for it. Evidence against it is as valuable as evidence for it.

Every factual claim MUST cite a primary source by PMID (or DOI, or NCT number for a
trial registration) and include a short verbatim quote from the cited abstract or record.
Do not paraphrase quotes. Do not invent identifiers. Separate established findings from
your own inference, and label which is which.

## Questions

### 1. Is the mechanism active in this disease?

- Evidence that the drug's target or pathway is active, elevated or genetically implicated
  in patients with Idiopathic Pulmonary Fibrosis: in affected tissue, in blood, or through human genetics.
- Whether activity is uniform or confined to a subgroup of patients, and how that subgroup
  is identified (a biomarker, a clinical feature).

### 2. Does blocking it help?

- Clinical trials of an anti-IL-11 or anti-IL-11RA monoclonal antibody in Idiopathic Pulmonary Fibrosis: registration numbers, phase, status and
  reported results, if any exist.
- Trials of other drugs acting on the same target or pathway in Idiopathic Pulmonary Fibrosis, with their
  outcomes, including failures.
- Results of an anti-IL-11 or anti-IL-11RA monoclonal antibody in related diseases that share the mechanism, and how far those results
  should transfer here.
- Animal or human tissue experiments in which blocking the pathway changed
  Idiopathic Pulmonary Fibrosis-like features.

### 3. Reasons it might fail

- Redundant pathways, wrong cell compartment, wrong disease stage, drug not reaching the
  affected tissue, or trial endpoints that cannot detect the effect.
- Safety concerns specific to this patient population.

### 4. Verdict

- One paragraph: how strong is the case, and what single experiment or trial design would
  most efficiently test it?
- List the PMIDs and trial identifiers that carry the most weight, with one line each.


## Output

# Drug Repurposing Hypothesis Assessment: Anti-IL-11 / Anti-IL-11RA Monoclonal Antibody in Idiopathic Pulmonary Fibrosis

## Summary

**The hypothesis is mechanistically compelling but clinically unproven.** The claim under assessment — that neutralising interleukin-11 (IL-11) or blocking its receptor IL11RA would benefit patients with Idiopathic Pulmonary Fibrosis (IPF) by interrupting autocrine IL-11 signalling in lung fibroblasts that drives myofibroblast differentiation and extracellular matrix (ECM) production — rests on an unusually well-replicated molecular mechanism. Multiple independent primary studies establish that IL-11 is the dominant TGFβ1-induced transcript in fibroblasts, that IL-11 and IL11RA are expressed specifically in fibroblasts, and that they drive a non-canonical, ERK-dependent autocrine loop required for fibrogenic protein synthesis. IL-11 and IL-11Rα are over-expressed in human IPF lung tissue and serum, with the highest levels in an identifiable subgroup (IPF with pulmonary hypertension). Anti-IL-11 antibodies arrest and reverse bleomycin-induced lung fibrosis in mice, and chronic IL-11 blockade appears broadly tolerated — even beneficial for healthspan — in aged mammals. This is a strong, druggable, biologically validated target.

**However, the case has three substantial weaknesses.** First, there is no human genetic support: large GWAS and resequencing studies of IPF consistently implicate MUC5B, TERT, FAM13A, DSP, and other telomere/host-defence/senescence genes — IL11 and IL11RA are absent from established IPF risk loci. Second, IL-11 is a *downstream* TGFβ effector of exactly the class (CTGF/pamrevlumab, autotaxin/ziritaxestat, pentraxin-2/zinpentraxin alfa) that has repeatedly failed Phase III in IPF, with failures attributed to mechanistic redundancy or insufficient target engagement. Third, and most decisively, no anti-IL-11 or anti-IL-11RA antibody has reported efficacy in IPF. One Phase 1/2 trial of the anti-IL-11RA antibody LASN01 (NCT05331300) enrolled IPF/PF-ILD patients and is marked completed, but no efficacy results are publicly posted. The only human efficacy signal for this drug class comes from a different fibroinflammatory disease — thyroid eye disease — where the anti-IL-11RA antibody LASN01 achieved statistically significant resolution of clinical activity score.

**Verdict: a moderate-strength repurposing hypothesis.** The biology is among the best-validated of any anti-fibrotic target, but the therapeutic class has a poor Phase III track record in IPF, the target lacks genetic support, and clinical efficacy in IPF remains entirely undemonstrated. The single most efficient test is a biomarker-enriched (serum IL-11-high / IPF-PH), add-on-to-standard-of-care, randomised Phase 2b trial with built-in target-engagement and anti-fibrotic pharmacodynamic readouts.

---

## Key Findings

### Finding 1 — The mechanism in the hypothesis is real, replicated, and required

The autocrine IL-11/IL11RA/ERK loop described in the hypothesis is not speculative; it is one of the best-documented molecular circuits in fibrosis biology. The foundational study (Schafer et al., *Nature* 2017) established that "upregulation of interleukin-11 (IL-11) is the dominant transcriptional response to TGFβ1 exposure and required for its pro-fibrotic effect. IL-11 and its receptor (IL11RA) are expressed specifically in fibroblasts, in which they drive non-canonical, ERK-dependent autocrine signalling that is required for fibrogenic protein synthesis" [PMID: 29160304](https://pubmed.ncbi.nlm.nih.gov/29160304/). Every clause of the hypothesis — autocrine signalling, fibroblast restriction, ERK dependence, and fibrogenic/ECM output — maps directly onto this finding.

Critically, this mechanism has been localised specifically to the pulmonary compartment relevant to IPF. The Ng/Cook/Schafer review (2020) states that "Transforming growth factor-beta (TGFβ) and other disease factors can initiate an autocrine loop of IL-11 signaling in pulmonary fibroblasts, which, in a largely ERK-dependent manner, triggers the translation of profibrotic proteins" [PMID: 33262481](https://pubmed.ncbi.nlm.nih.gov/33262481/). An independent 2025 review broadened the mechanism beyond simple fibroblast autocrine ERK signalling, noting that "IL-11 promotes lung cellular senescence and chronic inflammation through the activation of the JAK2/STAT3 and MEK/ERK1/2 pathways" [PMID: 40605040](https://pubmed.ncbi.nlm.nih.gov/40605040/). *(Established finding; the senescence/SASP framing is an additional mechanistic layer rather than a replacement.)*

### Finding 2 — IL-11 and IL-11Rα are elevated in human IPF tissue and serum, with an identifiable high-expression subgroup

The mechanism is not only active in cell culture and mouse models — it is elevated in human patients. Milara et al. (2022) studied control (n=20), IPF (n=20), and IPF with pulmonary hypertension (IPF-PH, n=20) human samples and found that "IL-11 and IL-11Rα were over-expressed in pulmonary arteries and serum of patients with PH associated to IPF vs IPF patients without PH" [PMID: 36376885](https://pubmed.ncbi.nlm.nih.gov/36376885/). A follow-up confirmed that "Serum and parenchyma levels of Interleukin 11 (IL-11) are elevated in IPF-PH patients" [PMID: 38561103](https://pubmed.ncbi.nlm.nih.gov/38561103/).

This is directly relevant to patient selection. The data suggest IL-11 activity is **not uniform** across IPF but enriched in the IPF-PH subgroup, which is identifiable clinically (presence of pulmonary hypertension) and biochemically (elevated serum IL-11). Supporting serum IL-11 as a patient-selection biomarker, work in the mechanistically related fibrotic disease systemic sclerosis found IL-11 "particularly elevated in those with ILD. This suggests that IL-11 could be a possible biomarker of ILD" [PMID: 37291792](https://pubmed.ncbi.nlm.nih.gov/37291792/). Notably, the existing antifibrotics pirfenidone and nintedanib partly inhibit IL-11-induced ERK1/2 signalling [PMID: 38561103](https://pubmed.ncbi.nlm.nih.gov/38561103/), which has implications for add-on trial design (see Limitations).

### Finding 3 — Anti-IL-11 antibodies arrest and reverse lung fibrosis in animal models

Pathway blockade is efficacious in vivo. The Ng/Cook/Schafer review reports that "In mice, therapeutic targeting of IL-11 with antibodies can arrest and reverse bleomycin-induced pulmonary fibrosis and inflammation" [PMID: 33262481](https://pubmed.ncbi.nlm.nih.gov/33262481/). This was independently confirmed in a different model: IL-11 neutralising antibodies "could effectively alleviate early and late pulmonary fibrosis in aging mice" via the TGF-β/NOX4/IL-11 axis [PMID: 42364821](https://pubmed.ncbi.nlm.nih.gov/42364821/). Convergent evidence from pharmacological pathway inhibition (fluorofenidone suppressing the IL-11/MEK/ERK pathway, [PMID: 36166195](https://pubmed.ncbi.nlm.nih.gov/36166195/)) and genetic receptor deletion corroborates that interrupting the pathway reduces pulmonary fibrosis. The preclinical anti-fibrotic efficacy package is strong and reproducible across laboratories and models.

### Finding 4 — An anti-IL-11RA antibody is clinically active in a *related* fibroinflammatory disease, but no IPF efficacy data exist

The first human efficacy signal for this drug class comes from thyroid eye disease (TED), not IPF. King et al. (2026) report that the anti-IL-11 receptor antibody LASN01 "is well tolerated and in a placebo-controlled phase II trial in TED, LASN01 resulted in a statistically significant resolution of clinical activity score (CAS) in 88% of treated patients (p = 0.028), but had lesser effects on proptosis" [PMID: 42069852](https://pubmed.ncbi.nlm.nih.gov/42069852/). This establishes that an anti-IL-11RA antibody can produce a statistically significant, clinically meaningful anti-inflammatory/anti-fibrotic effect in humans and is tolerable. Separately, antibody inhibitors of IL-11 signalling "are currently under evaluation in Phase I/II clinical trials" [PMID: 39756345](https://pubmed.ncbi.nlm.nih.gov/39756345/).

**The transferability caveat is important.** TED and IPF share an IL-11-driven fibroinflammatory mechanism, but differ in accessibility (orbit vs deep lung parenchyma), reversibility of disease, endpoint sensitivity (CAS resolution vs FVC decline over months), and chronicity. A positive TED result increases prior probability but cannot substitute for an IPF efficacy trial.

### Finding 5 — A completed Phase 1/2 trial enrolled IPF patients but has posted no efficacy results

The drug has reached the target population. **ClinicalTrials.gov NCT05331300** (Lassen Therapeutics), Phase 1/2, status **COMPLETED** (started 2022-06-06; primary completion 2024-11-27; actual enrolment n=75). The registration brief summary states: "LASN01 is a novel, fully human antibody directed against the human IL-11 receptor that is being developed to address the fibro-inflammatory pathology of pulmonary fibrosis and TED," evaluating "preliminary efficacy, immunogenicity, and pharmacokinetics of single and multiple doses of LASN01 in healthy participants and in patients with idiopathic pulmonary fibrosis (IPF) or progressive fibrosing interstiti[al lung disease]." **The record has NO results section posted.** A separate anti-IL-11 antibody, 9MW3811 (Mabwell), completed a first-in-human SAD Phase 1 in healthy subjects (NCT05740475, COMPLETED, n=32; target indications Pulmonary Fibrosis/Tumour) and is in Phase 2 for pathological scar (NCT07576608, RECRUITING). *(Established from trial registrations; the absence of posted efficacy results is the single largest evidence gap in this assessment.)*

### Finding 6 — Human genetics of IPF does NOT implicate IL11 or IL11RA

This is the most significant piece of evidence *against* target prioritisation. Large GWAS and resequencing studies consistently identify IPF risk at MUC5B, TERT, FAM13A, DSP, and telomere/host-defence/senescence genes. The most recent cross-ancestry study "identified loci on chromosomes 4 (FAM13A; rs7690839), 5 (TERT; rs7734992), 6 (DSP; rs2076295), and 11 (MUC5B; rs35705950) that were significantly associated with risk of IPF" [PMID: 42085270](https://pubmed.ncbi.nlm.nih.gov/42085270/). Neither IL11 nor IL11RA appears among established IPF risk genes. *(Established finding.)* **Inference:** drug targets with human genetic support have higher clinical success rates; IL-11's absence from IPF genetics does not refute the mechanism (IL-11 may be a downstream effector rather than an initiating cause), but it removes one of the strongest forms of causal human evidence and is consistent with IL-11 being a modifiable effector rather than a driver of disease initiation.

### Finding 7 — Downstream single-effector antifibrotics have repeatedly failed Phase III in IPF

IL-11 belongs to a therapeutic class with a poor clinical track record in IPF. A 2026 review concluded that "targeting broad-spectrum enzymes (e.g., autotaxin via ziritaxestat) or downstream effectors (e.g., Connective Tissue Growth Factor (CTGF) via pamrevlumab) has failed, likely due to mechanistic redundancy or insufficient target engagement" [PMID: 42094953](https://pubmed.ncbi.nlm.nih.gov/42094953/). The "Regression to the truth" analysis documents that promising Phase II IPF drugs (zinpentraxin alfa/pentraxin-2, ziritaxestat, pamrevlumab) failed in Phase III, warning that "positive phase II trial results may simply be a statistical anomaly rather than the result of true efficacy" [PMID: 40255293](https://pubmed.ncbi.nlm.nih.gov/40255293/). **Inference:** IL-11 is an analogous downstream TGFβ effector; the same redundancy that doomed CTGF and autotaxin blockade — multiple parallel profibrotic inputs (OSM/IL-6, PDGF, WNT/β-catenin) converging on myofibroblasts — is a direct and quantifiable risk for IL-11 monotherapy.

### Finding 8 — IL-11 has a documented dual role, complicating a simple "block it" model

Historical transgenic studies reveal nuance. Lung-specific IL-11 overexpression is directly pro-fibrotic: "the airways of IL-11 transgene (+) animals manifest nodular peribronchiolar mononuclear cell infiltrates and impressive airways remodeling with subepithelial fibrosis" [PMID: 8981933](https://pubmed.ncbi.nlm.nih.gov/8981933/). But the same body of work showed that "IL-11 was shown to inhibit asthma-like inflammation while stimulating airway fibrosis. This suggests that IL-11 elaboration is, in part, an attempt at airway healing" [PMID: 11734470](https://pubmed.ncbi.nlm.nih.gov/11734470/). **Inference:** IL-11 is simultaneously pro-fibrotic and anti-inflammatory/reparative. Blocking it to stop fibrosis could, in principle, disinhibit inflammation or impair epithelial repair — a theoretical risk that argues for careful safety monitoring but does not override the strong net-antifibrotic preclinical efficacy data.

### Finding 9 — Chronic IL-11 inhibition is broadly tolerated and may be beneficial in aged mammals

Safety signals for chronic blockade are reassuring. Widjaja et al. (*Nature* 2024), "Inhibition of IL-11 signalling extends mammalian healthspan and lifespan," showed long-term anti-IL-11 antibody dosing from mid-life reduced multi-morbidity and extended lifespan in mice, noting "For healthspan and lifespan, ERK, AMPK and mTORC1 represent critical pathways and inflammation is a centrally important hallmark" [PMID: 39020175](https://pubmed.ncbi.nlm.nih.gov/39020175/). This is directly relevant to the elderly IPF population. Human genetics reinforces developmental tolerability: biallelic IL11RA loss-of-function causes a Crouzon-like craniosynostosis syndrome but carriers survive to adulthood — "biallelic loss-of-function variants in the interleukin receptor 11 alpha gene IL11RA were found to be associated with a Crouzon-like craniosynostosis syndrome with associated dental anomalies (CRSDA)" [PMID: 30811827](https://pubmed.ncbi.nlm.nih.gov/30811827/).

### Finding 10 — On-target thrombopoietic safety considerations exist

IL-11 signals through the shared gp130 co-receptor and has physiological roles in thrombopoiesis. gp130 STAT truncation reduces circulating platelets: "the circulating platelet count was reduced by 30% in gp130(delta)/(delta) mice" [PMID: 12423677](https://pubmed.ncbi.nlm.nih.gov/12423677/), and recombinant IL-11 (oprelvekin) is an approved thrombopoietic agent. **Inference:** IL-11 neutralisation could affect platelet counts and other gp130-dependent tissues; platelet monitoring should be built into any IPF trial, though the viable human LOF phenotype and the clean tolerability of LASN01 in TED suggest this is manageable.

---

## Mechanistic Model / Interpretation

The evidence assembles into a coherent, testable mechanistic narrative:

```
   TGFβ1  ──┐
   WNT3a  ──┤ (converging profibrotic inputs)
   OSM/IL-6─┤
            ▼
   ┌─────────────────────────────┐
   │  Lung fibroblast            │
   │                             │
   │   IL11 ↑↑ (dominant         │
   │        TGFβ-induced gene)   │
   │        │                    │
   │        ▼ autocrine          │
   │   IL11 + IL11RA + gp130     │
   │        │                    │
   │        ▼ non-canonical      │
   │   ERK  (MEK/ERK1/2)         │  also: JAK2/STAT3, senescence/SASP
   │        │                    │
   │        ▼                    │
   │  Fibrogenic protein         │
   │  translation → αSMA,        │
   │  collagen I, fibronectin    │
   └─────────────────────────────┘
            │
            ▼
   Myofibroblast differentiation + ECM deposition → IPF progression

   Anti-IL-11 / anti-IL-11RA mAb  ──X──> breaks the autocrine loop
       (arrests & reverses fibrosis in mice; clinically active in TED)
```

**The strengths of the model** are its specificity (fibroblast-restricted IL11/IL11RA expression), its causal necessity (IL-11 *required* for TGFβ's profibrotic effect), its human tissue validation (elevated in IPF lung/serum), and its druggability (antibodies that arrest/reverse fibrosis preclinically and are tolerated in humans).

**The weakness of the model** is positional: IL-11 sits *downstream* of multiple redundant profibrotic inputs. Blocking one effector node in a network with parallel paths (WNT/β-catenin→IL-11, OSM, PDGF) risks incomplete fibrosis suppression — the precise failure mode seen for CTGF and autotaxin inhibitors. The dual pro-fibrotic/anti-inflammatory role adds a second-order uncertainty about net clinical effect.

### Evidence balance table

| Dimension | Direction | Strength | Key source |
|---|---|---|---|
| Mechanism active in fibroblasts | **For** | Very strong (replicated) | [PMID: 29160304](https://pubmed.ncbi.nlm.nih.gov/29160304/) |
| Elevated in human IPF tissue/serum | **For** | Strong | [PMID: 36376885](https://pubmed.ncbi.nlm.nih.gov/36376885/) |
| Identifiable responder subgroup (IPF-PH, serum IL-11) | **For** | Moderate | [PMID: 38561103](https://pubmed.ncbi.nlm.nih.gov/38561103/) |
| Antibody efficacy in animal models | **For** | Strong | [PMID: 33262481](https://pubmed.ncbi.nlm.nih.gov/33262481/) |
| Clinical activity in related disease (TED) | **For** | Moderate (transferability unclear) | [PMID: 42069852](https://pubmed.ncbi.nlm.nih.gov/42069852/) |
| Chronic blockade tolerability | **For** | Moderate–strong | [PMID: 39020175](https://pubmed.ncbi.nlm.nih.gov/39020175/) |
| Human genetic support in IPF | **Against** | Strong (clear absence) | [PMID: 42085270](https://pubmed.ncbi.nlm.nih.gov/42085270/) |
| Downstream-effector class failures in IPF | **Against** | Strong | [PMID: 42094953](https://pubmed.ncbi.nlm.nih.gov/42094953/) |
| Clinical efficacy in IPF | **Unknown** | — (no posted results) | NCT05331300 |
| Dual pro-fibrotic/anti-inflammatory role | **Caution** | Moderate | [PMID: 11734470](https://pubmed.ncbi.nlm.nih.gov/11734470/) |
| Thrombopoietic on-target safety | **Caution** | Moderate | [PMID: 12423677](https://pubmed.ncbi.nlm.nih.gov/12423677/) |

---

## Evidence Base

**Mechanism (supporting):**
- *IL-11 is a crucial determinant of cardiovascular fibrosis* [PMID: 29160304](https://pubmed.ncbi.nlm.nih.gov/29160304/) — foundational *Nature* study establishing IL-11/IL11RA/ERK autocrine loop as the required effector of TGFβ-driven fibrosis.
- *Interleukin-11 signaling underlies fibrosis... of the airway* [PMID: 33262481](https://pubmed.ncbi.nlm.nih.gov/33262481/) — localises the loop to pulmonary fibroblasts and reports antibody arrest/reversal of bleomycin fibrosis.
- *Aging-associated IL-11... targeted therapy of IPF* [PMID: 40605040](https://pubmed.ncbi.nlm.nih.gov/40605040/) — independent 2025 review confirming upregulation in IPF and the key caveat that clinical evidence is lacking.

**Human tissue/biomarker (supporting):**
- *IL-11 system participates in pulmonary artery remodeling... in pulmonary fibrosis* [PMID: 36376885](https://pubmed.ncbi.nlm.nih.gov/36376885/) — IL-11/IL-11Rα elevated in IPF, highest in IPF-PH.
- *Pirfenidone and nintedanib attenuate... IL-11* [PMID: 38561103](https://pubmed.ncbi.nlm.nih.gov/38561103/) — confirms elevated serum/parenchyma IL-11 in IPF-PH; existing drugs partly hit the pathway.
- *Elevated IL-11 in systemic sclerosis* [PMID: 37291792](https://pubmed.ncbi.nlm.nih.gov/37291792/) — supports serum IL-11 as an ILD biomarker.

**Preclinical efficacy (supporting):**
- *IL-11 neutralizing antibodies alleviate pulmonary fibrosis in aging mice* [PMID: 42364821](https://pubmed.ncbi.nlm.nih.gov/42364821/).
- *Fluorofenidone attenuates... IL-11/MEK/ERK* [PMID: 36166195](https://pubmed.ncbi.nlm.nih.gov/36166195/).

**Clinical (mixed):**
- *IL-11 receptor is a novel target... in fibro-inflammatory disease* [PMID: 42069852](https://pubmed.ncbi.nlm.nih.gov/42069852/) — LASN01 Phase II positive in TED.
- **NCT05331300** — LASN01 Phase 1/2 in IPF/PF-ILD, completed, no results posted.
- *De novo discovery of cyclic peptide inhibitors of IL-11* [PMID: 39756345](https://pubmed.ncbi.nlm.nih.gov/39756345/) — confirms the class is in Phase I/II.

**Against / cautionary:**
- *IPF risk loci in East Asian populations mirror European* [PMID: 42085270](https://pubmed.ncbi.nlm.nih.gov/42085270/) — IL11/IL11RA absent from IPF genetics.
- *Beyond attenuation: curative-intent targets in IPF* [PMID: 42094953](https://pubmed.ncbi.nlm.nih.gov/42094953/) — downstream-effector antifibrotics have failed.
- *"Regression to the truth": lessons from negative IPF trials* [PMID: 40255293](https://pubmed.ncbi.nlm.nih.gov/40255293/) — Phase II→III attrition and endpoint pitfalls.
- *Targeted expression of IL-11 in the murine airway* [PMID: 8981933](https://pubmed.ncbi.nlm.nih.gov/8981933/) and *Airway inflammation... IL-11 transgenic mice* [PMID: 11734470](https://pubmed.ncbi.nlm.nih.gov/11734470/) — dual role.
- *Hematopoietic abnormalities in gp130 signaling* [PMID: 12423677](https://pubmed.ncbi.nlm.nih.gov/12423677/) and *Craniosynostosis... IL11RA* [PMID: 30811827](https://pubmed.ncbi.nlm.nih.gov/30811827/) — safety context.
- *Inhibition of IL-11 signalling extends healthspan and lifespan* [PMID: 39020175](https://pubmed.ncbi.nlm.nih.gov/39020175/) — chronic tolerability.

---

## Limitations and Knowledge Gaps

1. **The decisive data are missing.** NCT05331300 (LASN01 Phase 1/2 in IPF/PF-ILD) is completed but has posted no efficacy results. Whether an anti-IL-11RA antibody changes any IPF outcome in humans is simply unknown. All "for" evidence is mechanistic, preclinical, or from a different disease.

2. **No human genetic causal anchor.** IL11/IL11RA are absent from IPF GWAS/resequencing hits. This does not disprove the mechanism (effectors need not be risk genes) but removes the strongest available form of human causal support and is a known negative predictor of drug-development success.

3. **Class-level pessimism.** IL-11 is a downstream TGFβ effector; the comparator drugs in this mechanistic class (pamrevlumab/CTGF, ziritaxestat/autotaxin, zinpentraxin/pentraxin-2) have failed Phase III, plausibly from redundancy. The preclinical "reversal" data are strong but preclinical reversal has not reliably predicted IPF clinical success.

4. **Biomarker/subgroup hypothesis is untested prospectively.** The IPF-PH / serum-IL-11-high responder subgroup is a cross-sectional association, not a validated predictive enrichment biomarker. It has never been used to stratify a trial.

5. **Endpoint sensitivity.** FVC decline — the standard IPF endpoint — is noisy and may miss true anti-fibrotic effects over short durations, a recurring theme in negative IPF trials. Positive TED data used a different, more sensitive endpoint (CAS), limiting transferability.

6. **Confounding by background therapy.** Pirfenidone/nintedanib already partly inhibit IL-11-induced ERK, which could blunt the incremental effect of add-on anti-IL-11 and complicate interpretation.

7. **Net-effect uncertainty from dual biology.** IL-11's anti-inflammatory/reparative role means blockade could have unintended effects on epithelial repair or inflammation that preclinical fibrosis-centric endpoints did not capture.

---

## Proposed Follow-up Experiments / Actions

1. **Obtain NCT05331300 outcomes (highest priority, zero-cost).** Pursue the LASN01 Phase 1/2 IPF/PF-ILD results via sponsor disclosure, conference presentations, or results posting. This single dataset would move the assessment more than any new experiment.

2. **Biomarker-enriched, add-on, randomised Phase 2b (the key efficiency experiment).** Design: IPF patients on stable background antifibrotic, enriched for serum-IL-11-high and/or IPF-PH phenotype, randomised to anti-IL-11RA mAb vs placebo. Build in (a) a target-engagement PD readout (e.g., downstream ERK/fibrogenic markers), (b) a sensitive structural endpoint such as quantitative HRCT fibrosis score alongside FVC, and (c) platelet monitoring. This directly tests efficacy, the redundancy risk, and the responder-subgroup hypothesis in one trial.

3. **Prospective validation of serum IL-11 as a predictive enrichment biomarker** using banked IPF cohorts with longitudinal FVC/outcome data, to confirm the IPF-PH / IL-11-high subgroup prior to committing to stratified enrolment.

4. **Human precision-cut lung slice (PCLS) studies** from IPF explants/biopsies, comparing anti-IL-11RA mAb alone vs combined blockade of parallel inputs (OSM/IL-6, PDGF, WNT) to quantify the redundancy risk directly in human tissue before a large trial.

5. **Safety sub-study on thrombopoiesis and epithelial repair** — monitor platelet kinetics and markers of alveolar epithelial repair during chronic dosing, given the gp130 thrombopoietic role and IL-11's reparative biology.

---

## Verdict

The anti-IL-11 / anti-IL-11RA repurposing hypothesis for IPF is **mechanistically among the best-supported anti-fibrotic hypotheses available** — the autocrine IL-11/IL11RA/ERK loop is a replicated, required driver of TGFβ-induced myofibroblast differentiation and ECM production, the ligand and receptor are elevated in human IPF tissue and serum, antibodies arrest and reverse fibrosis in animal models, and chronic blockade appears safe. **But the clinical case is unproven and carries specific red flags**: no human genetic support in IPF, membership in a downstream-effector drug class that has repeatedly failed Phase III through redundancy, and a completed IPF trial whose efficacy results are not public. The overall strength is **moderate**. The single most efficient test is a biomarker-enriched (serum IL-11-high / IPF-PH), add-on-to-standard-of-care, randomised Phase 2b with target-engagement and quantitative-imaging pharmacodynamic readouts.

### Highest-weight evidence (one line each)

- [PMID: 29160304](https://pubmed.ncbi.nlm.nih.gov/29160304/) — Establishes the required IL-11/IL11RA/ERK fibroblast autocrine mechanism central to the hypothesis.
- [PMID: 33262481](https://pubmed.ncbi.nlm.nih.gov/33262481/) — Localises the loop to pulmonary fibroblasts and shows antibodies arrest/reverse lung fibrosis in mice.
- [PMID: 36376885](https://pubmed.ncbi.nlm.nih.gov/36376885/) — Human IPF tissue/serum over-express IL-11/IL-11Rα, defining an IPF-PH responder subgroup.
- [PMID: 42069852](https://pubmed.ncbi.nlm.nih.gov/42069852/) — Anti-IL-11RA antibody (LASN01) clinically active and tolerated in a related fibroinflammatory disease (TED).
- **NCT05331300** — Completed LASN01 Phase 1/2 in IPF/PF-ILD; no efficacy results posted (the decisive missing datum).
- [PMID: 42085270](https://pubmed.ncbi.nlm.nih.gov/42085270/) — IPF risk genetics (MUC5B/TERT/FAM13A/DSP) do not implicate IL11/IL11RA.
- [PMID: 42094953](https://pubmed.ncbi.nlm.nih.gov/42094953/) — Downstream-effector antifibrotics (CTGF, autotaxin) have failed in IPF via redundancy — the class-level risk for IL-11.
- [PMID: 40255293](https://pubmed.ncbi.nlm.nih.gov/40255293/) — Documents Phase II→III failure pattern and endpoint pitfalls in IPF, tempering extrapolation.
- [PMID: 39020175](https://pubmed.ncbi.nlm.nih.gov/39020175/) — Chronic anti-IL-11 dosing is tolerated and extends healthspan/lifespan in aged mammals.


## Artifacts

- [OpenScientist final report](anti_il11-openscientist_artifacts/final_report.html)
- [OpenScientist final report](anti_il11-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 17 |
| Quoted claims found in source | 17 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 18 |
| On topic | 16 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:12423677` (7 mentions) - Hematopoietic abnormalities in mice deficient in gp130-mediated STAT signaling.
  - shared terms: genetic, drug

Weighed against this report's own most characteristic terms: `il-11`, `ipf`, `human`, `efficacy`, `fibrosis`, `phase`, `disease`, `il11ra`, `tissue`, `antibody`, `clinical`, `risk`, `genetic`, `mechanism`, `pulmonary`, `anti-il-11`, `serum`, `drug`, `lasn01`, `ipf-ph`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.
