---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-23T05:12:14.449022'
end_time: '2026-05-23T06:00:04.674083'
duration_seconds: 2870.23
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Long COVID
  category: Complex
  hypothesis_group_id: vascular_microclot_model
  hypothesis_label: Endothelial-Microclot Perfusion Model
  hypothesis_status: ALTERNATIVE
  hypothesis_yaml: "hypothesis_group_id: vascular_microclot_model\nhypothesis_label:\
    \ Endothelial-Microclot Perfusion Model\nstatus: ALTERNATIVE\ndescription: |\n\
    \  Fibrin amyloid microclots impair capillary flow and oxygen exchange, driving\
    \ fatigue, dyspnea, and energy deficits in a vascular-predominant subtype.\napplies_to_subtypes:\n\
    - Cardiopulmonary-dominant long COVID phenotype\nevidence:\n- reference: PMID:35195253\n\
    \  reference_title: 'A central role for amyloid fibrin microclots in long COVID/PASC:\
    \ origins and therapeutic\n    implications.'\n  supports: SUPPORT\n  evidence_source:\
    \ HUMAN_CLINICAL\n  snippet: the ability of these fibrin amyloid microclots (fibrinaloids)\
    \ to block up capillaries, and\n    thus to limit the passage of red blood cells\
    \ and hence O2 exchange, can actually underpin the majority\n    of these symptoms\n\
    \  explanation: Supports a perfusion-limitation mechanism that can coexist with\
    \ immune-driven models."
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
citation_count: 33
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Long COVID
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** vascular_microclot_model
- **Hypothesis Label:** Endothelial-Microclot Perfusion Model
- **Status in KB:** ALTERNATIVE

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: vascular_microclot_model
hypothesis_label: Endothelial-Microclot Perfusion Model
status: ALTERNATIVE
description: |
  Fibrin amyloid microclots impair capillary flow and oxygen exchange, driving fatigue, dyspnea, and energy deficits in a vascular-predominant subtype.
applies_to_subtypes:
- Cardiopulmonary-dominant long COVID phenotype
evidence:
- reference: PMID:35195253
  reference_title: 'A central role for amyloid fibrin microclots in long COVID/PASC: origins and therapeutic
    implications.'
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: the ability of these fibrin amyloid microclots (fibrinaloids) to block up capillaries, and
    thus to limit the passage of red blood cells and hence O2 exchange, can actually underpin the majority
    of these symptoms
  explanation: Supports a perfusion-limitation mechanism that can coexist with immune-driven models.
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


## Output

# Endothelial-Microclot Perfusion Model for Long COVID: Hypothesis Evaluation Report

**Hypothesis ID:** vascular_microclot_model  
**Hypothesis Label:** Endothelial-Microclot Perfusion Model  
**Current KB Status:** ALTERNATIVE  
**Evaluation Date:** 2026-05-23  
**Papers Reviewed:** 74

---

## Summary

The Endothelial-Microclot Perfusion Model proposes that fibrin amyloid microclots impair capillary flow and oxygen exchange, driving fatigue, dyspnea, and energy deficits in a vascular-predominant Long COVID subtype. After systematic evaluation of 74 primary research papers, the hypothesis is **partially supported** by converging but incomplete evidence. Three pillars of the model — endothelial dysfunction, anomalous fibrin amyloid microclot formation, and impaired peripheral oxygen extraction — each have empirical support from human clinical studies, *in vitro* experiments, and proteomics. Endothelial dysfunction in particular is one of the most robustly established features of both acute and post-acute COVID-19, confirmed by autopsy studies, proteomic analyses, cardiovascular magnetic resonance imaging, and expert consensus from multiple independent research groups worldwide.

However, the critical causal link — that microclots *in vivo* occlude capillaries and thereby cause clinical symptoms — remains undemonstrated. All core microclot evidence originates from a single research group (Pretorius, Kell, and colleagues at Stellenbosch University/University of Liverpool), and no independent laboratory has yet replicated the fluorescence microscopy–based microclot quantification in Long COVID plasma despite more than four years since the original publication. Furthermore, no randomized controlled trial has tested whether anticoagulant-mediated microclot dissolution reverses symptoms, and direct *in vivo* imaging of capillary occlusion by microclots has not been achieved in any human study.

The model likely applies to a cardiopulmonary-dominant subtype of Long COVID and coexists with — rather than replaces — competing mechanisms including viral persistence in gut tissue, autoimmunity, mitochondrial dysfunction, and autonomic dysregulation. Several of these alternative mechanisms have comparable or stronger independent evidence from multiple research groups and could operate in parallel with, upstream of, or downstream from the microclot pathway. The current KB status of ALTERNATIVE is appropriate; upgrade to SUPPORTED would require independent replication of microclot findings, *in vivo* evidence of capillary occlusion, or a positive RCT of anticoagulant-mediated symptom resolution.

---

## Key Findings

### Finding 1: Fibrin Amyloid Microclots Are Detectable in Long COVID Plasma and Resist Fibrinolysis

Pretorius et al. (2021) provided the first demonstration that platelet-poor plasma (PPP) from Long COVID patients contains persistent anomalous amyloid deposits — termed fibrinaloid microclots — that are resistant to fibrinolysis ([PMID: 34425843](https://pubmed.ncbi.nlm.nih.gov/34425843/)). Using fluorescence microscopy with thioflavin T (ThT) staining, they showed that these deposits were substantially more abundant in Long COVID PPP compared to controls, and that levels of α2-antiplasmin were elevated. Follow-up proteomic analysis of microclots from 99 Long COVID patients versus 29 controls (Kruger et al., 2022) revealed that "these microclots entrap a substantial number of inflammatory molecules, including those that might prevent clot breakdown" ([PMID: 36131342](https://pubmed.ncbi.nlm.nih.gov/36131342/)). A subsequent bioinformatic analysis demonstrated that proteins entrapped in fibrinaloid microclots exhibit high amyloidogenic tendencies, suggesting their integration as cross-β elements into amyloid structures rather than simple physical entrapment — the data showed no correlation between plasma protein abundance and their presence in microclots, arguing against a passive trapping mechanism ([PMID: 39409138](https://pubmed.ncbi.nlm.nih.gov/39409138/)). Similar — though less extensive — microclots and platelet hyperactivation were also detected in ME/CFS patients, with microclot area commonly more than 10-fold greater than in healthy controls ([PMID: 36015078](https://pubmed.ncbi.nlm.nih.gov/36015078/)), suggesting a shared vascular pathology across post-viral fatigue syndromes.

**Confidence:** Moderate. The core findings are internally consistent, supported by proteomics and bioinformatic validation, but all originate from a single research group. No independent replication of the ThT-based microclot quantification method in Long COVID has been published as of the search date.

### Finding 2: Spike Protein S1 Directly Induces Fibrinolysis-Resistant Fibrin Amyloid Formation *In Vitro*

Grobbelaar et al. (2021) demonstrated that adding SARS-CoV-2 spike protein S1 to healthy platelet-poor plasma "results in structural changes to β and γ fibrin(ogen), complement 3, and prothrombin. These proteins were substantially resistant to trypsinization, in the presence of spike protein S1" ([PMID: 34328172](https://pubmed.ncbi.nlm.nih.gov/34328172/)). This provides a direct mechanistic link between the viral protein and anomalous clot formation, suggesting that even after acute viral clearance, residual spike protein — whether from persistent viral reservoirs or circulating fragments — could continue to seed microclot formation.

**Confidence:** Moderate. The *in vitro* demonstration is clear and mechanistically compelling, but the concentrations of spike protein used, the relevance to *in vivo* circulating spike levels in convalescent patients, and whether this mechanism operates at physiologically relevant timescales remain uncertain. No confirmatory study from an independent laboratory has been published.

### Finding 3: Impaired Peripheral Oxygen Extraction Demonstrated by Invasive CPET

Singh et al. (2022) used invasive cardiopulmonary exercise testing (iCPET) in 10 recovered COVID-19 patients versus 10 controls, finding that "patients who have recovered from COVID-19 without cardiopulmonary disease demonstrate a marked reduction in peak VO₂" with impaired peripheral oxygen extraction as a primary limiting mechanism ([PMID: 34389297](https://pubmed.ncbi.nlm.nih.gov/34389297/)). Jothi et al. (2025) confirmed similar exercise oxygen pathway abnormalities in 15 PASC and 11 CFS/ME patients versus 11 controls ([PMID: 40892700](https://pubmed.ncbi.nlm.nih.gov/40892700/)). A systematic review and meta-analysis of 38 CPET studies encompassing 2,160 individuals found that peak VO₂ was reduced by a mean of −4.9 mL/kg/min (95% CI: −6.4 to −3.4) among those with Long COVID symptoms, with "deconditioning and peripheral limitations (abnormal oxygen extraction)" being common, though dysfunctional breathing and chronotropic incompetence were also described ([PMID: 36223120](https://pubmed.ncbi.nlm.nih.gov/36223120/)).

**Confidence:** High for the phenomenology of impaired oxygen extraction; moderate-to-low for attributing this impairment specifically to microclot-mediated capillary occlusion, as mitochondrial dysfunction and autonomic dysregulation are equally plausible explanations for the same CPET pattern.

### Finding 4: Endothelial Dysfunction Is Robustly Established in Acute and Post-Acute COVID-19

Multiple independent lines of evidence establish endothelial dysfunction as a central feature of COVID-19 pathophysiology. The ESC Working Group position paper highlighted that "endothelial biomarkers and tests of function should be evaluated for their usefulness in risk stratification of COVID-19 patients" ([PMID: 32750108](https://pubmed.ncbi.nlm.nih.gov/32750108/)). Autopsy studies of 88 fatal COVID-19 cases demonstrated microvascular thrombosis with weak CD31 and high von Willebrand factor (vWF) expression in cardiac endothelium, with SARS-CoV-2 nucleocapsid protein detected in endothelial cells ([PMID: 41591353](https://pubmed.ncbi.nlm.nih.gov/41591353/)). Cardiovascular magnetic resonance studies showed abnormal coronary vascular response in Long COVID patients using oxygenation-sensitive CMR ([PMID: 40185235](https://pubmed.ncbi.nlm.nih.gov/40185235/)). Critically, proteomic studies revealed that "individuals who went on to develop PASC exhibited a distinct phenotypic signature between 1 and 35 days post-infection, such as significantly elevated plasma Factor-IX, Tissue factor, and tPA, which reflected hyperactivation of immunothrombotic pathways" ([PMID: 41372813](https://pubmed.ncbi.nlm.nih.gov/41372813/)) — this is notable because it demonstrates immunothrombotic activation *before* Long COVID symptom onset, suggesting a causal rather than merely correlative relationship. Systematic reviews confirmed the breadth of endothelial biomarker evidence across multiple cohorts worldwide ([PMID: 37175942](https://pubmed.ncbi.nlm.nih.gov/37175942/); [PMID: 36253560](https://pubmed.ncbi.nlm.nih.gov/36253560/)).

**Confidence:** High. This is the strongest pillar of the model, supported by >10 independent research groups using diverse methodologies including autopsy, imaging, proteomics, and clinical biomarkers.

### Finding 5: Competing Hypotheses Have Comparable or Stronger Multi-Group Evidence

Several alternative mechanistic hypotheses explain overlapping Long COVID features with evidence from multiple independent groups:

- **Viral persistence:** SARS-CoV-2 antigen reservoirs have been detected in gut-associated lymphoid tissue with associated persistent immune activation ([PMID: 41794369](https://pubmed.ncbi.nlm.nih.gov/41794369/)). Intestinal viral reservoirs disrupt VLCFA-peroxisome signaling, impairing epithelial repair and driving persistent GI symptoms ([PMID: 41494535](https://pubmed.ncbi.nlm.nih.gov/41494535/)).
- **Autoimmunity:** Antineuronal autoantibodies are detected in ~12% of PCC patients ([PMID: 40441540](https://pubmed.ncbi.nlm.nih.gov/40441540/)). However, anti-phospholipid antibodies specifically were NOT associated with Long COVID development (63.2% vs 66.3%, p = 0.79; [PMID: 40843001](https://pubmed.ncbi.nlm.nih.gov/40843001/)), and one study found autoantibody prevalence was higher in recovered than Long COVID patients ([PMID: 41459516](https://pubmed.ncbi.nlm.nih.gov/41459516/)).
- **Mitochondrial dysfunction:** Brain MRS at 7T showed elevated lactate in ME/CFS consistent with energetic stress; "a reduction in total choline in long COVID is of interest in the context of the recently reported association between blood clots and 'brain fog'" ([PMID: 40652046](https://pubmed.ncbi.nlm.nih.gov/40652046/)).
- **Autonomic dysregulation:** Long COVID and ME/CFS share an autonomic phenotype with "reduced orthostatic CBFv (92%/88% in Long COVID/ME/CFS), mild-to-moderate widespread autonomic failure (95%/89%), presence of SFN (67%/53%)" ([PMID: 41576003](https://pubmed.ncbi.nlm.nih.gov/41576003/)).

**Confidence:** High that multiple mechanisms coexist; the relative contribution of each likely varies by patient subtype and disease stage.

---

## Mechanistic Model and Causal Chain

{{figure:causal_chain.png|caption=Mechanistic causal chain from SARS-CoV-2 infection through endothelial injury, microclot formation, capillary occlusion, to clinical symptoms. Annotations indicate where evidence is strong (ESTABLISHED), emerging, or speculative.}}

The hypothesis implies the following causal sequence from upstream viral trigger to clinical manifestation:

```
SARS-CoV-2 infection
       │
       ▼
[1] Spike protein binds ACE2 on endothelial cells → direct endothelial injury
    Evidence: ESTABLISHED — multiple autopsy/biomarker studies, ESC consensus
       │
       ▼
[2] Endothelial activation → vWF release, complement activation, cytokine storm
    Evidence: ESTABLISHED — proteomic evidence, autopsy data, multiple groups
       │
       ▼
[3] Spike protein S1 interacts with fibrinogen → anomalous amyloid fibrin formation
    Evidence: EMERGING — in vitro demonstration only, single group
       │
       ▼
[4] Fibrin amyloid microclots form in plasma, entrap inflammatory molecules + α2-AP
    Evidence: EMERGING — ex vivo PPP evidence, single group, no replication
       │
       ▼
[5] Microclots resist fibrinolysis → persist for weeks/months post-infection
    Evidence: EMERGING — longitudinal persistence shown, single group
       │
       ▼
[6] Microclots occlude capillaries → block RBC passage → impair O₂ exchange
    Evidence: SPECULATIVE — no direct in vivo imaging evidence exists
       │
       ▼
[7] Tissue hypoxia → fatigue, dyspnea, brain fog, exercise intolerance
    Evidence: INDIRECT — iCPET shows impaired O₂ extraction, but attribution
              to microclots specifically is unproven
```

### Link-by-Link Assessment

| Causal Link | Status | Evidence Strength | Key References |
|-------------|--------|-------------------|----------------|
| SARS-CoV-2 → Endothelial dysfunction | **ESTABLISHED** | Multiple independent groups, autopsy, imaging, proteomics | PMID: 32750108, 41591353, 40185235, 41372813 |
| Spike protein → Fibrin amyloid formation | **EMERGING** | In vitro single-group data | PMID: 34328172 |
| Long COVID plasma → Detectable microclots | **EMERGING** | Single group, consistent across studies | PMID: 34425843, 36131342 |
| Microclots entrap inflammatory proteins | **EMERGING** | Proteomic + bioinformatic evidence, single group | PMID: 36131342, 39409138 |
| Microclots → Capillary occlusion (in vivo) | **SPECULATIVE** | No direct evidence; inferred from in vitro properties | None |
| Capillary occlusion → Impaired O₂ exchange | **SPECULATIVE** | Consistent with iCPET but alternative explanations exist | PMID: 34389297, 40892700 |
| Impaired O₂ → Fatigue/dyspnea/brain fog | **ESTABLISHED** | Robust physiological reasoning; iCPET data | PMID: 34389297, 36223120 |
| Microclot removal → Symptom improvement | **GAP** | No perturbation study exists | None |

The **critical missing steps** are links 6 (capillary occlusion) and the therapeutic corollary (microclot removal → clinical improvement). Without direct evidence for these, the chain from microclot formation to clinical symptoms remains inferential. The model's strongest elements — endothelial dysfunction and impaired oxygen extraction — are well-established but are not exclusive to the microclot mechanism; they are equally consistent with mitochondrial dysfunction or autonomic dysregulation of blood flow.

---

## Evidence Matrix

{{figure:evidence_matrix.png|caption=Evidence matrix summarizing key studies, evidence type, direction of support, mechanistic claims tested, and confidence levels for the Endothelial-Microclot Perfusion Model}}

| Citation | Evidence Type | Direction | Mechanistic Claim Tested | Key Finding | Subtype/Context | Confidence |
|----------|-------------|-----------|--------------------------|-------------|-----------------|------------|
| [PMID: 35195253](https://pubmed.ncbi.nlm.nih.gov/35195253/) | Review/Hypothesis | Supports | Microclots block capillaries and limit O₂ exchange | Theoretical framework for microclot-driven Long COVID symptoms | Long COVID general | Moderate — hypothesis paper |
| [PMID: 34425843](https://pubmed.ncbi.nlm.nih.gov/34425843/) | Human clinical | Supports | Persistent microclots in Long COVID plasma | Fibrinolysis-resistant microclots detected by ThT staining; elevated α2-antiplasmin | Long COVID vs controls | Moderate — single group |
| [PMID: 36131342](https://pubmed.ncbi.nlm.nih.gov/36131342/) | Human clinical (proteomics) | Supports | Microclots entrap pro-inflammatory molecules | 99 vs 29 proteomics; inflammatory proteins trapped in microclots | Long COVID vs controls | Moderate — single group |
| [PMID: 34328172](https://pubmed.ncbi.nlm.nih.gov/34328172/) | In vitro | Supports | Spike S1 induces amyloid fibrin | S1 causes fibrinolysis-resistant structural changes in fibrinogen, C3, prothrombin | Mechanistic | Moderate — in vitro only |
| [PMID: 39409138](https://pubmed.ncbi.nlm.nih.gov/39409138/) | Computational/proteomic | Supports | Amyloidogenic cross-seeding in microclots | Proteins in microclots have high amyloidogenic tendency; argues against simple entrapment | Mechanistic | Low-Moderate |
| [PMID: 34389297](https://pubmed.ncbi.nlm.nih.gov/34389297/) | Human clinical (iCPET) | Supports (indirect) | Impaired peripheral O₂ extraction | Marked reduction in peak VO₂ with peripheral extraction defect (n=10 vs 10) | Cardiopulmonary | Moderate — small n |
| [PMID: 40892700](https://pubmed.ncbi.nlm.nih.gov/40892700/) | Human clinical (iCPET) | Supports (indirect) | Shared exercise limitation in PASC and ME/CFS | Impaired O₂ extraction in both PASC and CFS/ME | Cardiopulmonary | Moderate |
| [PMID: 36223120](https://pubmed.ncbi.nlm.nih.gov/36223120/) | Meta-analysis | Supports (indirect) | Reduced exercise capacity in Long COVID | Peak VO₂ −4.9 mL/kg/min (95% CI: −6.4 to −3.4) in LC vs non-LC | Long COVID (38 studies, 2160 patients) | Moderate-High |
| [PMID: 41372813](https://pubmed.ncbi.nlm.nih.gov/41372813/) | Human clinical (proteomics) | Supports | Immunothrombotic pathway activation predicts PASC | Elevated Factor-IX, Tissue factor, tPA 1-35 days post-infection | Pre-symptomatic PASC | High — independent, longitudinal |
| [PMID: 32750108](https://pubmed.ncbi.nlm.nih.gov/32750108/) | Position paper (ESC) | Supports | Endothelial dysfunction central to COVID-19 | ESC Working Group consensus on vascular pathobiology | Acute + post-acute | High — expert consensus |
| [PMID: 41591353](https://pubmed.ncbi.nlm.nih.gov/41591353/) | Human clinical (autopsy) | Supports | Endothelial dysfunction + microvascular thrombosis | Weak CD31, high vWF, microvascular thrombosis in 88 autopsies | Fatal COVID-19 | High — independent |
| [PMID: 40185235](https://pubmed.ncbi.nlm.nih.gov/40185235/) | Human clinical (CMR) | Supports | Vascular dysfunction persists in Long COVID | Abnormal coronary vascular response by OS-CMR | Long COVID | Moderate — independent |
| [PMID: 37301958](https://pubmed.ncbi.nlm.nih.gov/37301958/) | Human clinical (proteomics) | Supports | HIF-mediated vasculoproliferation from hypoxia | Elevated ANGPT1, VEGFA; HIF-1 pathway activation in Long COVID plasma proteome | Long COVID outpatients | Moderate — independent |
| [PMID: 36015078](https://pubmed.ncbi.nlm.nih.gov/36015078/) | Human clinical | Qualifies | Microclots also found in ME/CFS | Microclot area >10-fold greater in ME/CFS; platelet hyperactivation | ME/CFS | Moderate — single group |
| [PMID: 40843001](https://pubmed.ncbi.nlm.nih.gov/40843001/) | Human clinical | Refutes (partial) | Antiphospholipid antibodies drive LC thrombosis | aPL positivity did NOT differ between LC and non-LC (63.2% vs 66.3%, p=0.79) | Autoimmune-thrombotic | Moderate |
| [PMID: 41459516](https://pubmed.ncbi.nlm.nih.gov/41459516/) | Human clinical | Qualifies | Autoantibodies drive Long COVID | Autoantibody prevalence: 37% recovered > 24% LC > 19% pre-pandemic | Black/mixed population | Moderate |
| [PMID: 41353681](https://pubmed.ncbi.nlm.nih.gov/41353681/) | RCT | Refutes (partial) | HCQ modulates endotheliopathy | HCQ had no effect on Ang-2, P-selectin, or D-dimer trajectories (n=293) | Acute COVID-19 | High — RCT |
| [PMID: 41794369](https://pubmed.ncbi.nlm.nih.gov/41794369/) | Human clinical | Competing | Viral persistence in gut drives Long COVID | Viral proteins persist in GALT with immune dysregulation | GI-dominant | High — independent |
| [PMID: 41494535](https://pubmed.ncbi.nlm.nih.gov/41494535/) | Human clinical + model | Competing | Intestinal viral reservoirs disrupt epithelial repair | VLCFA-peroxisome pathway disruption; GI symptoms | GI-dominant | High — multi-model |
| [PMID: 40652046](https://pubmed.ncbi.nlm.nih.gov/40652046/) | Human clinical (7T MRS) | Competing/Qualifies | Mitochondrial dysfunction vs. vascular pathology | Elevated brain lactate in ME/CFS; reduced choline in Long COVID | Neuro-metabolic | Moderate-High |
| [PMID: 41576003](https://pubmed.ncbi.nlm.nih.gov/41576003/) | Human clinical | Competing | Autonomic dysregulation is central | 92%/88% reduced orthostatic CBFv; widespread autonomic failure in 95%/89% | Neuro-autonomic | High — large cohort |

---

## Evidence Base: Literature Summary

### Core Microclot Studies (Single Group: Pretorius/Kell)

The microclot hypothesis originates from the Pretorius and Kell laboratory. Their foundational paper ([PMID: 34425843](https://pubmed.ncbi.nlm.nih.gov/34425843/)) demonstrated persistent fibrinolysis-resistant microclots in Long COVID platelet-poor plasma using thioflavin T fluorescence staining. The proteomic characterization ([PMID: 36131342](https://pubmed.ncbi.nlm.nih.gov/36131342/)) identified entrapped inflammatory molecules including those preventing clot breakdown. The *in vitro* spike protein study ([PMID: 34328172](https://pubmed.ncbi.nlm.nih.gov/34328172/)) established a direct viral trigger mechanism. Computational analyses ([PMID: 39409138](https://pubmed.ncbi.nlm.nih.gov/39409138/); [PMID: 39942772](https://pubmed.ncbi.nlm.nih.gov/39942772/)) supported amyloidogenic cross-seeding rather than passive entrapment. The extension to ME/CFS ([PMID: 36015078](https://pubmed.ncbi.nlm.nih.gov/36015078/)) broadened the hypothesis beyond Long COVID. The seed reference review ([PMID: 35195253](https://pubmed.ncbi.nlm.nih.gov/35195253/)) provided the theoretical framework linking microclots to capillary occlusion and symptom generation.

### Independent Endothelial Dysfunction Evidence

The endothelial dysfunction component is the model's strongest element, supported by multiple independent research groups. Key independent evidence includes the ESC position paper ([PMID: 32750108](https://pubmed.ncbi.nlm.nih.gov/32750108/)), autopsy studies demonstrating direct SARS-CoV-2 endothelial infection with microvascular thrombosis ([PMID: 41591353](https://pubmed.ncbi.nlm.nih.gov/41591353/)), proteomic demonstration that immunothrombotic pathway activation *predicts* PASC development before symptom onset ([PMID: 41372813](https://pubmed.ncbi.nlm.nih.gov/41372813/)), CMR evidence of persistent coronary vascular dysfunction ([PMID: 40185235](https://pubmed.ncbi.nlm.nih.gov/40185235/)), and multiple systematic reviews ([PMID: 37175942](https://pubmed.ncbi.nlm.nih.gov/37175942/); [PMID: 36253560](https://pubmed.ncbi.nlm.nih.gov/36253560/); [PMID: 41516301](https://pubmed.ncbi.nlm.nih.gov/41516301/)).

### Exercise Physiology Studies

iCPET studies from independent groups consistently show impaired peripheral oxygen extraction in Long COVID ([PMID: 34389297](https://pubmed.ncbi.nlm.nih.gov/34389297/); [PMID: 40892700](https://pubmed.ncbi.nlm.nih.gov/40892700/)), with a meta-analysis of 38 studies confirming reduced exercise capacity ([PMID: 36223120](https://pubmed.ncbi.nlm.nih.gov/36223120/)). Microvascular and immunometabolic interactions contributing to post-exertional malaise have been reviewed ([PMID: 39240417](https://pubmed.ncbi.nlm.nih.gov/39240417/)), highlighting the interplay between mitochondrial dysfunction, immune activation, and microcirculatory impairment.

### Competing Mechanism Evidence

Viral persistence has been independently demonstrated in gut tissue by multiple groups ([PMID: 41794369](https://pubmed.ncbi.nlm.nih.gov/41794369/); [PMID: 41494535](https://pubmed.ncbi.nlm.nih.gov/41494535/)). Autonomic dysregulation has been comprehensively characterized in large cohorts ([PMID: 41576003](https://pubmed.ncbi.nlm.nih.gov/41576003/)). Mitochondrial dysfunction has distinct metabolic signatures on 7T MRS ([PMID: 40652046](https://pubmed.ncbi.nlm.nih.gov/40652046/)). The autoimmune hypothesis is weakened by negative findings for antiphospholipid antibodies ([PMID: 40843001](https://pubmed.ncbi.nlm.nih.gov/40843001/)) and higher autoantibody prevalence in recovered than Long COVID patients ([PMID: 41459516](https://pubmed.ncbi.nlm.nih.gov/41459516/)).

---

## Limitations and Knowledge Gaps

{{figure:knowledge_gaps.png|caption=Summary of critical knowledge gaps in the Endothelial-Microclot Perfusion Model, including gap scope, importance, and resolving evidence needed}}

### Critical Gaps

**1. No Independent Replication of Microclot Quantification**

All microclot detection and quantification studies in Long COVID originate from the Pretorius/Kell group and direct collaborators. PubMed was searched for independent laboratories performing ThT-based microclot detection in Long COVID plasma; no independent replication was found as of the search date. After 4+ years since the first publication, this absence is concerning. Resolving this gap requires a multi-center blinded study with a standardized ThT staining protocol and quantitative image analysis across ≥3 independent laboratories.

**2. No RCT of Anticoagulation Targeting Microclots**

The hypothesis predicts that dissolving microclots via anticoagulation should resolve symptoms; only a preliminary uncontrolled report was referenced in the seed paper. No completed RCT results specifically targeting microclots in Long COVID were found in the literature. The STIMULATE-ICP trial and similar efforts were searched but no published results were identified. A placebo-controlled RCT of anticoagulant therapy in Long COVID patients stratified by microclot burden is the single most important missing piece of evidence.

**3. In Vivo Capillary Occlusion Undemonstrated**

The central claim that microclots physically block capillaries and impair red blood cell passage has no direct imaging evidence. A retinal microvascular study protocol has been registered ([PMID: 38041762](https://pubmed.ncbi.nlm.nih.gov/38041762/)) but results are not yet available. Intravital microscopy in animal models or sublingual videomicroscopy/retinal OCT-A correlated with plasma microclot load in patients would directly test this link.

### Major Gaps

**4. Distinguishing Microclot-Mediated O₂ Deficit from Mitochondrial Dysfunction**

Both microclot-mediated capillary occlusion and mitochondrial dysfunction predict impaired peripheral O₂ extraction on iCPET, but they require different therapeutic approaches. The 7T MRS finding that ME/CFS shows elevated brain lactate (consistent with mitochondrial dysfunction) while Long COVID shows reduced choline (potentially linked to clotting) suggests partially distinct mechanisms ([PMID: 40652046](https://pubmed.ncbi.nlm.nih.gov/40652046/)), but no study has simultaneously measured microclot burden, mitochondrial function (muscle biopsy), and exercise physiology in the same patients.

**5. Subtype Specificity Not Established**

The hypothesis claims applicability to a "cardiopulmonary-dominant" subtype, but no clustering study has validated this subtype or linked it to elevated microclot burden. Multi-omic studies show hemostasis/coagulation dysregulation across PACS patients regardless of POTS status ([PMID: 37981644](https://pubmed.ncbi.nlm.nih.gov/37981644/)), suggesting coagulation abnormalities may be more broadly distributed than the hypothesis assumes.

**6. Temporal Dynamics of Microclots Unknown**

No longitudinal study tracks microclot formation, persistence, and resolution over months in individual patients correlated with symptom trajectories. Understanding whether microclots wax and wane with symptoms would substantially strengthen or weaken the causal model.

**7. No Genetic Susceptibility Data**

No GenCC, ClinGen, or GWAS evidence for coagulation gene variants predisposing to Long COVID–associated microclots was found. Genetic susceptibility could explain why only a subset of patients develop persistent microclots.

**8. Dose-Response Relationship Absent**

No published study reports a quantitative correlation between microclot burden (e.g., ThT fluorescence area) and symptom severity scores. A dose-response relationship would strengthen causal inference.

---

## Alternative Models

### 1. Viral Persistence Hypothesis
- **Relationship:** Upstream cause / parallel mechanism
- **Evidence:** SARS-CoV-2 proteins persist in gut-associated lymphoid tissue 15–22 months post-infection ([PMID: 41794369](https://pubmed.ncbi.nlm.nih.gov/41794369/)). Intestinal viral reservoirs disrupt VLCFA-peroxisome signaling and epithelial repair ([PMID: 41494535](https://pubmed.ncbi.nlm.nih.gov/41494535/)). Viral reservoirs may also sustain microclot formation via persistent spike protein production, making the two hypotheses potentially complementary.
- **Assessment:** Stronger independent evidence base from multiple groups; explains GI symptoms that the microclot model does not directly address. Could be upstream of microclot formation.

### 2. Mitochondrial Dysfunction / Metabolic Reprogramming
- **Relationship:** Parallel mechanism / downstream consequence
- **Evidence:** 7T MRS showing elevated brain lactate in ME/CFS ([PMID: 40652046](https://pubmed.ncbi.nlm.nih.gov/40652046/)); impaired oxidative phosphorylation documented across multiple studies ([PMID: 42051540](https://pubmed.ncbi.nlm.nih.gov/42051540/); [PMID: 39240417](https://pubmed.ncbi.nlm.nih.gov/39240417/)).
- **Assessment:** Could explain impaired O₂ extraction independently of microclots. Has distinct therapeutic implications (CoQ10, molecular hydrogen). May have different weighting in ME/CFS vs. Long COVID.

### 3. Autonomic Dysregulation / Dysautonomia
- **Relationship:** Parallel mechanism
- **Evidence:** 92% of Long COVID and 88% of ME/CFS patients show reduced orthostatic cerebral blood flow; widespread autonomic failure in 95%/89%; small fiber neuropathy in 67%/53% ([PMID: 41576003](https://pubmed.ncbi.nlm.nih.gov/41576003/)). POTS is one of the most common Long COVID phenotypes.
- **Assessment:** Strong independent evidence for cerebral and systemic hypoperfusion via autonomic failure rather than capillary occlusion. Could produce brain fog and exercise intolerance without microclots.

### 4. Autoimmune / Trained Immunity Model
- **Relationship:** Upstream cause / parallel mechanism
- **Evidence:** Antineuronal antibodies in 12% of PCC patients ([PMID: 40441540](https://pubmed.ncbi.nlm.nih.gov/40441540/)). However, anti-phospholipid antibodies NOT associated with Long COVID ([PMID: 40843001](https://pubmed.ncbi.nlm.nih.gov/40843001/)), weakening the autoimmune-thrombotic subhypothesis specifically.
- **Assessment:** Mixed evidence. Some autoantibodies (anti-GPCR, anti-neuronal) may explain neurological symptoms more specifically than microclots.

### 5. Endothelial Senescence Model
- **Relationship:** Complementary / mechanistic variant
- **Evidence:** Virus-induced endothelial senescence with senescence-associated secretory phenotype (SASP) proposed as upstream unifying mechanism ([PMID: 41513611](https://pubmed.ncbi.nlm.nih.gov/41513611/)).
- **Assessment:** Shares the endothelial dysfunction core but emphasizes cellular aging over amyloid fibrin formation; could explain chronicity via immune failure to clear senescent cells.

### 6. Chronic Macrophage Activation / Impaired Resolution
- **Relationship:** Upstream cause
- **Evidence:** Persistent spike protein drives epigenetically "trained" macrophages into chronic inflammatory state ([PMID: 41516190](https://pubmed.ncbi.nlm.nih.gov/41516190/)). PASC framed as failed innate immune resolution with deficits in specialized pro-resolving mediators ([PMID: 41864480](https://pubmed.ncbi.nlm.nih.gov/41864480/)).
- **Assessment:** Potentially unifying framework that could encompass microclot persistence as a downstream consequence of failed immune resolution.

---

## Discriminating Tests

### Test 1: Multi-Center Independent Microclot Replication
- **Design:** Prospective cohort of ≥200 Long COVID patients stratified by symptom cluster, with ≥50 recovered COVID and ≥50 pre-pandemic controls
- **Biomarkers:** Standardized ThT fluorescence quantification of microclots in PPP, D-dimer, fibrinogen, α2-antiplasmin
- **Key feature:** Blinded assessment across ≥3 independent laboratories using identical protocol
- **Expected result if hypothesis true:** Significant microclot elevation in Long COVID, highest in cardiopulmonary subtype
- **Priority:** Highest — this single study would resolve the most fundamental question

### Test 2: Anticoagulation RCT with Microclot Endpoint
- **Design:** Double-blind, placebo-controlled RCT of targeted anticoagulant therapy (e.g., rivaroxaban 10 mg/day ± nattokinase) for 12 weeks
- **Enrollment:** Long COVID patients with elevated microclot burden at baseline (n=60–80)
- **Primary endpoint:** Change in microclot area at 4 weeks; secondary: 6MWT distance, SF-36 PF, peak VO₂
- **Expected result if hypothesis true:** Microclot reduction correlates with symptom improvement

### Test 3: Combined iCPET + Microcirculation + Microclot + Muscle Biopsy Study
- **Design:** Simultaneous invasive CPET, plasma microclot quantification, sublingual videomicroscopy, and quadriceps muscle biopsy for mitochondrial respiratory chain assessment
- **Cohort:** ≥30 Long COVID with exercise intolerance, ≥30 ME/CFS, ≥30 healthy controls
- **Discriminating prediction:** If microclot hypothesis is primary, impaired O₂ extraction correlates with microclot burden and reduced microcirculatory flow but NOT mitochondrial complex deficiency; if mitochondrial hypothesis is primary, the reverse

### Test 4: Longitudinal Spike Protein-Microclot Tracking
- **Design:** Serial plasma samples at 1, 3, 6, 12, 18 months post-infection in ≥50 acute COVID patients
- **Biomarkers:** Ultrasensitive spike protein quantification (Simoa), ThT microclot quantification
- **Expected result if hypothesis true:** Spike protein persistence correlates temporally with microclot burden, and both predict Long COVID development

### Test 5: Phenotype Clustering with Coagulation Biomarkers
- **Design:** Unsupervised clustering of ≥500 unselected Long COVID patients using full symptom profiling + coagulation panel + inflammatory markers + autonomic testing
- **Expected result if hypothesis true:** A distinct cardiopulmonary cluster emerges with the highest microclot burden, separable from neurological and GI-dominant clusters

---

## Curation Leads

*All items below are candidate updates for the KB, labeled as leads requiring curator verification.*

### Candidate Evidence References

1. **[PMID: 41372813](https://pubmed.ncbi.nlm.nih.gov/41372813/)** — Independent proteomic evidence of immunothrombotic pathway activation *predicting* PASC. Verified snippet: *"individuals who went on to develop PASC exhibited a distinct phenotypic signature between 1 and 35 days post-infection, such as significantly elevated plasma Factor-IX, Tissue factor, and tPA, which reflected hyperactivation of immunothrombotic pathways."* → Candidate SUPPORT evidence; notable because it demonstrates prospective rather than cross-sectional immunothrombotic activation.

2. **[PMID: 34389297](https://pubmed.ncbi.nlm.nih.gov/34389297/)** — iCPET evidence for impaired peripheral O₂ extraction. Verified snippet: *"Patients who have recovered from COVID-19 without cardiopulmonary disease demonstrate a marked reduction in peak VO₂."* → Candidate SUPPORT (indirect) evidence for the perfusion-limitation component.

3. **[PMID: 40843001](https://pubmed.ncbi.nlm.nih.gov/40843001/)** — Antiphospholipid antibodies NOT associated with Long COVID development. Verified snippet: *"aPL positivity did not differ significantly between patients with and without long COVID (63.2% vs. 66.3%, p = 0.79)."* → Candidate QUALIFIES evidence; limits the autoimmune-coagulation overlap mechanism.

4. **[PMID: 41576003](https://pubmed.ncbi.nlm.nih.gov/41576003/)** — Shared autonomic phenotype with reduced orthostatic CBFv in 92%/88% of Long COVID/ME/CFS. → Candidate COMPETING evidence; autonomic dysregulation explains perfusion deficits without requiring microclots.

5. **[PMID: 40652046](https://pubmed.ncbi.nlm.nih.gov/40652046/)** — 7T brain MRS distinguishing metabolic signatures. Verified snippet: *"A reduction in total choline in long COVID is of interest in the context of the recently reported association between blood clots and 'brain fog'."* → Candidate QUALIFIES/COMPETING evidence; suggests distinct metabolic pathology that may or may not relate to clotting.

### Candidate Pathophysiology Nodes and Edges

- **Node:** Fibrin amyloid microclots (fibrinaloids) — anomalous amyloid conformation of fibrin resistant to fibrinolysis
- **Edge:** Spike protein S1 → fibrinogen conformational change → fibrin amyloid formation (in vitro, PMID: 34328172)
- **Edge:** Endothelial dysfunction → platelet hyperactivation → microclot formation (multiple studies)
- **Edge:** α2-antiplasmin elevation → fibrinolysis resistance → microclot persistence (PMID: 34425843)
- **Edge (hypothesized, unconfirmed):** Microclots → capillary occlusion → impaired O₂ exchange
- **Edge (unconfirmed):** Microclot removal → symptom improvement

### Candidate Ontology Terms

- **Cell types:** Endothelial cells (CL:0000115), Platelets (CL:0000233), Monocyte-derived macrophages (CL:0000235)
- **Biological processes:** Blood coagulation/fibrin clot formation (GO:0072378), Fibrinolysis (GO:0042730), Amyloid fibril formation (GO:1990000), Response to hypoxia (GO:0001666)
- **Disease terms:** Post-acute sequelae of SARS-CoV-2 infection (MONDO:0100233)

### Candidate Subtype Restrictions

- The hypothesis should be explicitly tagged as most applicable to a **cardiopulmonary-dominant Long COVID phenotype**, pending validation by phenotype clustering studies
- Should be annotated as potentially extending to ME/CFS (PMID: 36015078), suggesting a general post-viral coagulopathy mechanism

### Candidate Status Change

- **Current status: ALTERNATIVE** → **Recommend maintaining ALTERNATIVE status**
- Upgrade to SUPPORTED would require: (1) independent replication of microclot detection, (2) in vivo capillary occlusion evidence, OR (3) positive RCT of microclot-targeted therapy
- The endothelial dysfunction component alone (without specific microclot claims) could be elevated to ESTABLISHED as a broader "endothelial dysfunction model"
- Consider adding a qualifier: "partially supported for vascular-predominant subtype; independent replication needed"

### Candidate Knowledge Gap Entries for KB

1. **Independent microclot replication absent** — All core microclot data from single group; 4+ years without independent confirmation
2. **No RCT testing microclot-targeted therapy** — Central therapeutic prediction untested
3. **In vivo capillary occlusion undemonstrated** — Core mechanistic claim lacks direct evidence
4. **Microclot-symptom dose-response absent** — No quantitative correlation published
5. **Subtype specificity untested** — No clustering study validates cardiopulmonary subtype association
6. **No genetic susceptibility data** — GenCC/ClinGen absence confirmed

### Discussion Prompts

1. Should the microclot hypothesis be considered a sub-mechanism of a broader "endothelial dysfunction" model, or does it make distinct predictions that require separate evaluation?
2. Is the impaired peripheral O₂ extraction on iCPET better explained by microclots, mitochondrial dysfunction, autonomic dysfunction, or a combination — and how should the KB represent this uncertainty?
3. How should the hypothesis account for Long COVID patients whose primary symptoms are neurological or GI rather than cardiopulmonary?
4. Given >4 years without independent replication, should the KB add a caveat about single-group provenance to the hypothesis entry?

---

*Report generated: May 2026. Based on systematic evaluation of 74 primary research papers. All PMID citations link to PubMed abstracts used as evidence sources. Findings, citations, and knowledge gaps reflect the literature as of the search date.*
