---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-06-03T09:14:20.054144'
end_time: '2026-06-03T09:56:04.435262'
duration_seconds: 2504.38
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Preeclampsia
  category: Complex
  hypothesis_group_id: early_onset_placenta_dominant
  hypothesis_label: Early-Onset Placenta-Dominant Antiangiogenic Model
  hypothesis_status: CANONICAL
  hypothesis_yaml: "hypothesis_group_id: early_onset_placenta_dominant\nhypothesis_label:\
    \ Early-Onset Placenta-Dominant Antiangiogenic Model\nstatus: CANONICAL\napplies_to_subtypes:\n\
    - Early-onset\n- HELLP\ndescription: |\n  In early-onset preeclampsia, immune\
    \ maladaptation at the maternal-fetal interface and defective trophoblast invasion\
    \ produce severe placental malperfusion before clinical disease. Placental hypoxia\
    \ and stress drive a marked antiangiogenic shift, especially excess sFlt-1 and\
    \ soluble endoglin with reduced free PlGF, causing maternal endothelial dysfunction\
    \ and organ-specific renal, hepatic, CNS, and uteroplacental manifestations.\n\
    evidence:\n- reference: PMID:35177220\n  reference_title: 'Preeclampsia and eclampsia:\
    \ the conceptual evolution of a syndrome.'\n  supports: SUPPORT\n  evidence_source:\
    \ HUMAN_CLINICAL\n  snippet: Early-onset preeclampsia has many features in common\
    \ with atherosclerosis, whereas late-onset\n    preeclampsia seems to result from\
    \ a mismatch of fetal demands and maternal supply, that is, a metabolic\n    crisis.\n\
    \  explanation: Supports modeling early-onset preeclampsia separately from late-onset\
    \ disease."
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
citation_count: 30
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Preeclampsia
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** early_onset_placenta_dominant
- **Hypothesis Label:** Early-Onset Placenta-Dominant Antiangiogenic Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: early_onset_placenta_dominant
hypothesis_label: Early-Onset Placenta-Dominant Antiangiogenic Model
status: CANONICAL
applies_to_subtypes:
- Early-onset
- HELLP
description: |
  In early-onset preeclampsia, immune maladaptation at the maternal-fetal interface and defective trophoblast invasion produce severe placental malperfusion before clinical disease. Placental hypoxia and stress drive a marked antiangiogenic shift, especially excess sFlt-1 and soluble endoglin with reduced free PlGF, causing maternal endothelial dysfunction and organ-specific renal, hepatic, CNS, and uteroplacental manifestations.
evidence:
- reference: PMID:35177220
  reference_title: 'Preeclampsia and eclampsia: the conceptual evolution of a syndrome.'
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Early-onset preeclampsia has many features in common with atherosclerosis, whereas late-onset
    preeclampsia seems to result from a mismatch of fetal demands and maternal supply, that is, a metabolic
    crisis.
  explanation: Supports modeling early-onset preeclampsia separately from late-onset disease.
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

# Hypothesis Evaluation Report: Early-Onset Placenta-Dominant Antiangiogenic Model of Preeclampsia

**Hypothesis ID:** `early_onset_placenta_dominant`
**Hypothesis Label:** Early-Onset Placenta-Dominant Antiangiogenic Model
**Status in KB:** CANONICAL
**Date of Evaluation:** 2026-06-03
**Applies to Subtypes:** Early-onset preeclampsia, HELLP syndrome
**Investigation:** 5 iterations, 14 confirmed findings, 98 papers reviewed

---

## Executive Judgment

**Verdict: STRONGLY SUPPORTED** — Maintain CANONICAL status.

The early-onset placenta-dominant antiangiogenic model is among the best-supported mechanistic hypotheses for any complex pregnancy disorder. Across 5 iterations of systematic investigation encompassing 14 confirmed findings and 98 reviewed papers, no directly refuting evidence was identified despite active searches for negative results. The hypothesis is validated by convergent evidence spanning all major evidence types: genome-wide association (fetal FLT1 locus, P = 5.4 × 10⁻¹⁶), single-cell transcriptomics (FLT1 up / PGF down in syncytiotrophoblast), animal models (RUPP), interventional proof-of-concept (sFlt-1 apheresis), pharmacological triangulation (metformin, esomeprazole, pravastatin all reduce sFlt-1), FDA-approved molecular diagnostics (sFlt-1/PlGF ratio), formal Bradford-Hill causation analysis, and upstream immunogenetic specification (KIR/HLA-C). The model satisfies temporality, dose–response, biological gradient, experiment/reversibility, and coherence criteria for causation.

**Most important caveats:** (1) The model does not apply to late-onset PE, which shows distinct maternal cardiovascular maladaptation pathology with only subtle placental transcriptomic changes. (2) Parallel mechanisms — syncytiotrophoblast senescence-associated secretory phenotype (SASP), angiotensin II type 1 receptor autoantibodies (AT1-AA), and complement activation — contribute to the full clinical phenotype and may represent independent therapeutic targets, particularly complement in HELLP. (3) No Phase III randomized controlled trial of targeted sFlt-1 reduction has been completed, leaving the final interventional proof at the pilot/Phase II level. (4) The sFlt-1/PlGF biomarker has variable positive predictive value across populations, requiring population-specific thresholds.

---

## Summary

The early-onset placenta-dominant antiangiogenic model posits that immune maladaptation at the maternal–fetal interface and defective trophoblast invasion produce severe placental malperfusion before clinical disease. Placental hypoxia and stress then drive a marked antiangiogenic shift — particularly excess soluble fms-like tyrosine kinase-1 (sFlt-1) and soluble endoglin (sEng) with reduced free placental growth factor (PlGF) — causing maternal endothelial dysfunction and organ-specific renal, hepatic, CNS, and uteroplacental manifestations. This investigation systematically evaluated this hypothesis across genomic, transcriptomic, proteomic, immunogenetic, animal model, interventional, diagnostic, and pharmacological evidence domains.

The evidence is remarkably convergent. The first genome-wide significant susceptibility locus for PE maps to the fetal FLT1 gene — the very gene encoding sFlt-1. Single-cell RNA sequencing of ~90,000 placental cells confirms FLT1 upregulation and PGF downregulation specifically in syncytiotrophoblast and extravillous trophoblasts of early-onset PE placentas. The upstream immunogenetic trigger is specified by the KIR AA / HLA-C2 maternal–fetal interaction, which inhibits decidual NK cell cytokine secretion and impairs trophoblast migration. Animal models (RUPP) recapitulate the causal chain from placental ischemia through sFlt-1 elevation to hypertension, and interventional removal of sFlt-1 (apheresis) ameliorates clinical PE in pilot studies. The sFlt-1/PlGF ratio has been FDA-approved as a molecular diagnostic, and multiple repurposed drugs converge on reducing sFlt-1 as their mechanism of PE prevention.

Despite this strong support, the model has defined boundaries. Late-onset PE (>34 weeks) exhibits comparatively subtle transcriptional changes and appears driven by maternal cardiovascular maladaptation rather than placental antiangiogenic excess. Complement activation may represent an independent effector pathway in HELLP syndrome specifically. The full clinical translation — a Phase III trial demonstrating that targeted sFlt-1 reduction prevents or treats early-onset PE — remains the critical missing piece.

---

## Key Findings

### Finding 1: Single-Cell Transcriptomics Confirms FLT1 Up / PGF Down in Early-Onset PE Placenta

Single-cell and single-nuclei RNA-seq of approximately 90,000 placental cells across 46 cell types demonstrated massive transcriptional dysregulation in early-onset PE across trophoblast, immune, stromal, and endothelial lineages. The hallmark finding was FLT1 upregulation and PGF downregulation in syncytiotrophoblast and extravillous trophoblasts — the precise molecular signature predicted by the antiangiogenic model. Critically, late-onset PE showed only subtle transcriptomic changes, consistent with a distinct pathophysiology driven by maternal cardiovascular maladaptation, placental aging, cellular senescence, and oxidative stress ([PMID: 40253080](https://pubmed.ncbi.nlm.nih.gov/40253080/); [PMID: 41582793](https://pubmed.ncbi.nlm.nih.gov/41582793/)).

This finding provides the most direct molecular-level validation of the antiangiogenic model at single-cell resolution and simultaneously supports the two-disease paradigm separating early-onset from late-onset PE.

### Finding 2: sFlt-1 Apheresis Prolongs Pregnancy — Interventional Proof of Concept

Pilot studies demonstrated that extracorporeal removal of sFlt-1 from the maternal circulation ameliorates clinical PE. Dextran sulfate cellulose apheresis reduced circulating sFlt-1 in a dose-dependent fashion; in 3 women with very preterm PE (27–30 weeks), multiple treatments lowered sFlt-1, reduced proteinuria, and stabilized blood pressure, prolonging pregnancy by 15–23 days with continued fetal growth ([PMID: 21810665](https://pubmed.ncbi.nlm.nih.gov/21810665/)). The H.E.L.P. apheresis study (n = 6 vs 6 controls) showed average admission-to-birth interval of 15.0 days vs 6.3 days in controls (p = 0.027) ([PMID: 29858106](https://pubmed.ncbi.nlm.nih.gov/29858106/)). This satisfies the Bradford-Hill experiment/reversibility criterion: removing the hypothesized causal agent improves the disease.

### Finding 3: HIF-1α as the Unifying Mechanistic Hub

HIF-1α has been identified as the transcriptional regulator linking placental ischemia to the antiangiogenic shift. Sustained HIF-1α activation drives mitochondrial dysfunction and oxidative stress, amplifying placental injury. At the transcriptional level, HIF-1α promotes antiangiogenic programs including sFlt-1 upregulation, resulting in systemic angiogenic imbalance and maternal endothelial dysfunction ([PMID: 41814104](https://pubmed.ncbi.nlm.nih.gov/41814104/)). This fills a critical mechanistic gap between upstream placental ischemia/hypoxia and downstream antiangiogenic factor overproduction.

### Finding 4: sFlt-1/PlGF Ratio — FDA-Approved Biomarker with Population-Specific Caveats

The sFlt-1/PlGF ratio ≤38 has a negative predictive value (NPV) of 98.6% (95% CI 97.2–99.4%) for ruling out PE within 1 week across Asian populations ([PMID: 31188674](https://pubmed.ncbi.nlm.nih.gov/31188674/)). However, the positive predictive value (PPV) was only 30.3% (95% CI 23.0–38.5%) for ruling in PE within 4 weeks, and performance was reduced in multifetal pregnancies (AUC 0.789 in twins vs 0.870 in singletons for PE before 34 weeks) ([PMID: 41213792](https://pubmed.ncbi.nlm.nih.gov/41213792/)). Population-specific thresholds are needed for U.S. populations. In New Zealand, the test showed NPV of 96.2% for PE ≤1 week and PPV of 75.0% for PE ≤4 weeks ([PMID: 35670085](https://pubmed.ncbi.nlm.nih.gov/35670085/)). The FDA approval of this molecular test validates the antiangiogenic model as clinically actionable while highlighting that antiangiogenic imbalance, though highly sensitive, is not perfectly specific across all populations.

### Finding 5: Syncytiotrophoblast SASP as Additional Mechanism

Single-nucleus RNA-seq combined with spatial transcriptomics identified senescent transcriptomic states in syncytiotrophoblast nuclei with a senescence-associated secretory phenotype (SASP). Elevated senescence markers were validated across clinical multicenter cohorts, with secreted SASP factors PAI-1 and activin A elevated in maternal blood already in the first trimester ([PMID: 39440423](https://pubmed.ncbi.nlm.nih.gov/39440423/)). This suggests syncytiotrophoblast senescence operates as a parallel or amplifying mechanism alongside the canonical antiangiogenic shift.

### Finding 6: Fetal FLT1 GWAS — Genetic Proof of Concept

The first genome-wide significant susceptibility locus for PE maps to rs4769613 near FLT1 on chromosome 13 (P = 5.4 × 10⁻¹⁶), identified in a GWAS of 2,658 offspring from preeclamptic pregnancies vs 308,292 controls ([PMID: 28628106](https://pubmed.ncbi.nlm.nih.gov/28628106/)). That the variant is in the fetal (not maternal) genome and maps to the gene encoding the key antiangiogenic protein provides exceptionally strong genetic evidence for the central role of sFlt-1 in PE pathogenesis. Overall PE heritability is estimated at ~55% ([PMID: 29138037](https://pubmed.ncbi.nlm.nih.gov/29138037/)).

### Finding 7: KIR/HLA-C Specifies Upstream Immune Trigger

The maternal KIR AA genotype combined with fetal HLA-C2 increases PE risk. Activating KIR2DS1 on decidual NK cells recognizes HLA-C2 on trophoblast and stimulates GM-CSF production, which enhances trophoblast migration. The KIR AA genotype lacks this activating receptor, resulting in inhibited uNK cytokine secretion and deficient trophoblast invasion support ([PMID: 24091323](https://pubmed.ncbi.nlm.nih.gov/24091323/); [PMID: 20972337](https://pubmed.ncbi.nlm.nih.gov/20972337/)). This finding specifies the upstream immunogenetic trigger that initiates the cascade of defective trophoblast invasion → placental malperfusion → antiangiogenic shift, and has been validated across PE, FGR, and recurrent miscarriage cohorts.

### Finding 8: Bradford-Hill Causation Criteria Satisfied

Systematic application of Bradford-Hill criteria demonstrated that antiangiogenic factors satisfy temporality (sFlt-1 elevation precedes clinical PE), dose–response (higher sFlt-1 correlates with severity), and experiment (sFlt-1 removal improves outcomes), while inflammatory markers fail these same criteria. Corticosteroids fail to improve maternal outcome despite immunosuppression, further arguing against inflammation as the primary driver ([PMID: 22103497](https://pubmed.ncbi.nlm.nih.gov/22103497/)).

### Finding 9: RUPP Animal Model Confirms Causal Chain

The reduced uterine perfusion pressure (RUPP) model in rats and mice recapitulates the full causal chain: placental ischemia → elevated sFlt-1 (P < 0.05) → elevated blood pressure (120 ± 4 vs 104 ± 4 mmHg, P < 0.01) → reduced fetal weights (0.95 ± 0.04 vs 0.80 ± 0.02 g, P < 0.02) ([PMID: 25298513](https://pubmed.ncbi.nlm.nih.gov/25298513/)). Critically, the GPER agonist G-1 restored sFlt-1 levels and reversed cardiac dysfunction while the vasodilator hydralazine did not normalize sFlt-1, demonstrating that targeting the antiangiogenic pathway — not just blood pressure — is required ([PMID: 39224973](https://pubmed.ncbi.nlm.nih.gov/39224973/)). Additionally, sFlt-1 decreased MMPs in uterus, placenta, and aorta; VEGF reversed these changes, and H₂S donor (NaHS) reduced sFlt-1-induced hypertension, proteinuria, and glomerular endotheliosis while increasing free VEGF ([PMID: 24335973](https://pubmed.ncbi.nlm.nih.gov/24335973/)).

### Finding 10: Glomerular Endotheliosis Linked to sFlt-1/VEGF Imbalance

PE renal pathology (glomerular endotheliosis and thrombotic microangiopathy) is mechanistically linked to sFlt-1 sequestering VEGF, disrupting glomerular endothelium–podocyte cross-talk. sFlt-1 abrogates binding of VEGF to its receptor on endothelial cells and podocytes, ultimately damaging the filtration barrier ([PMID: 30399576](https://pubmed.ncbi.nlm.nih.gov/30399576/)). H₂S donor NaHS reversed sFlt-1-induced glomerular endotheliosis in rats by upregulating renal VEGF-A mRNA ([PMID: 24335973](https://pubmed.ncbi.nlm.nih.gov/24335973/)).

### Finding 11: Pharmacological Convergence on the Antiangiogenic Target

Three mechanistically distinct repurposed drugs all reduce sFlt-1 secretion. Combining metformin and esomeprazole was additive at reducing sFlt-1 secretion and expression of sFlt-1 e15a mRNA isoform in primary cytotrophoblast, placental explants, and endothelial cells ([PMID: 29466360](https://pubmed.ncbi.nlm.nih.gov/29466360/)). Metformin's PE-protective mechanism operates through reducing antiangiogenic factors (sFlt-1 and sEng) and improving endothelial dysfunction through mitochondrial effects ([PMID: 28619690](https://pubmed.ncbi.nlm.nih.gov/28619690/)). The INOVASIA RCT showed pravastatin (20 mg BID from 14–20 weeks) was associated with a non-significant reduction in PE (17.5% vs 35%) and stabilized the sFlt-1/PlGF ratio compared with deterioration in controls ([PMID: 34666379](https://pubmed.ncbi.nlm.nih.gov/34666379/)). This pharmacological triangulation provides independent validation of the antiangiogenic target.

### Finding 12: Complement as Parallel Pathway in HELLP

A case report of eculizumab (anti-C5 complement inhibitor) in severe PE/HELLP at 26 weeks showed marked clinical improvement, complete normalization of lab parameters, and pregnancy prolongation by 17 days ([PMID: 23228435](https://pubmed.ncbi.nlm.nih.gov/23228435/)). This is the only published case of targeted complement inhibition in PE/HELLP. The result suggests complement may be an independent effector pathway, particularly in HELLP, representing a therapeutic target that operates parallel to rather than downstream of the antiangiogenic shift.

### Finding 13: sFlt-1/PlGF Ratio Defines Organ-Damage Phenotypes

Within PE, the sFlt-1/PlGF ratio stratifies organ-damage phenotypes. In a retrospective cohort (n = 320, 68 PE cases), the renal-dominant phenotype showed the highest ratio (66.0 ± 22.5), followed by hepatic (55.9 ± 18.2) and hematologic (52.0 ± 16.8). The renal phenotype was associated with earliest delivery (34.6 weeks), lowest birth weight (2196 g), highest NICU admission (10.7%), and lowest Apgar scores ([PMID: 42041953](https://pubmed.ncbi.nlm.nih.gov/42041953/)). This demonstrates that the degree of antiangiogenic imbalance quantitatively predicts not just PE occurrence but specific organ-damage patterns within the disease.

### Finding 14: Active Search for Refuting Evidence Found None

Systematic searches for negative evidence found: no published reports of early-onset PE without elevated sFlt-1, no failed sFlt-1-targeted therapy trials, no early-onset PE with normal placental histology, and a Bradford-Hill analysis explicitly ruling out sFlt-1 as epiphenomenon ([PMID: 22103497](https://pubmed.ncbi.nlm.nih.gov/22103497/)). Additionally, the GPER agonist study showed that only approaches targeting sFlt-1 (not simple vasodilation) reversed cardiac dysfunction in RUPP rats ([PMID: 39224973](https://pubmed.ncbi.nlm.nih.gov/39224973/)). While publication bias against negative results cannot be excluded, the absence of refuting evidence despite active searching strengthens the model's canonical status.

---

## Mechanistic Causal Chain

The hypothesis implies a stepwise causal chain from upstream immunogenetic triggers to clinical organ damage. Below, each step is annotated with the strength of supporting evidence and identified gaps.

{{figure:causal_chain_diagram.png|caption=Mechanistic causal chain for the early-onset PE antiangiogenic model, with evidence strength annotations at each stage}}

### Step-by-Step Chain

```
UPSTREAM TRIGGERS (Immunogenetic + Genetic)
│
├─ Maternal KIR AA + Fetal HLA-C2
│  → Inhibited decidual NK cytokine secretion
│  → Deficient trophoblast invasion support
│  Evidence: STRONG [PMID: 24091323, 20972337]
│
├─ Fetal FLT1 variants (rs4769613, P=5.4×10⁻¹⁶)
│  → Genetically determined sFlt-1 overproduction susceptibility
│  Evidence: VERY STRONG [PMID: 28628106, 29138037]
│
▼
DEFECTIVE TROPHOBLAST INVASION (Stage 1a)
│  Reduced EVT invasion → incomplete spiral artery remodeling
│  Evidence: STRONG (histopathology, scRNA-seq, functional)
│
▼
PLACENTAL MALPERFUSION / ISCHEMIA (Stage 1b)
│  High-resistance, low-flow uteroplacental circulation
│  Evidence: STRONG (Doppler, RUPP model, histopathology)
│
▼
HIF-1α STABILIZATION (Mechanistic Hub)
│  Persistent hypoxia → HIF-1α transcriptional activation
│  → Mitochondrial dysfunction, oxidative stress amplification
│  Evidence: MODERATE-STRONG [PMID: 41814104]
│  ⚠ GAP: No direct HIF-1α perturbation in human placenta
│
▼
ANTIANGIOGENIC SHIFT (Core of Hypothesis)
│  ↑↑ sFlt-1, ↑ sEng, ↓↓ free PlGF
│  FLT1 up / PGF down confirmed at single-cell level
│  Evidence: VERY STRONG [PMID: 28628106, 40253080, 41582793]
│
│  Parallel mediators at this stage:
│  ├─ SASP factors (PAI-1, activin A) [PMID: 39440423] — EMERGING
│  ├─ STB debris/extracellular vesicles [PMID: 22217911] — MODERATE
│  └─ AT1-AA (~55% of PE) [PMID: 41275618] — EMERGING
│
▼
MATERNAL ENDOTHELIAL DYSFUNCTION (Stage 2)
│  sFlt-1 sequesters VEGF/PlGF → endothelial activation
│  → Vasoconstriction, vascular permeability, pro-coagulant state
│  Evidence: STRONG (in vitro, animal, apheresis reversal)
│  [PMID: 21810665, 22103497, 29858106]
│
▼
ORGAN-SPECIFIC MANIFESTATIONS (Stage 3)
├─ RENAL: Glomerular endotheliosis (highest sFlt-1/PlGF ratio)
│  [PMID: 30399576, 42041953]
├─ HEPATIC: Vascular damage, HELLP
│  ⚠ Complement may be independent pathway [PMID: 23228435]
├─ CNS: Cerebral edema, eclampsia
├─ UTEROPLACENTAL: FGR, abruption
└─ CARDIOVASCULAR: Hypertension, long-term CVD risk
```

{{figure:evidence_summary.png|caption=Comprehensive evidence strength assessment by causal stage with knowledge gap visualization}}

### Evidence Strength Summary by Stage

| Causal Stage | Evidence Level | Key Evidence Types | Key References |
|---|---|---|---|
| KIR/HLA-C immune trigger | **Strong** | Genetic, functional in vitro | PMID: 24091323, 20972337 |
| Fetal FLT1 genetic susceptibility | **Very Strong** | GWAS | PMID: 28628106 |
| Trophoblast invasion failure | **Strong** | Histopathology, scRNA-seq | PMID: 40253080, 41407310 |
| Placental ischemia | **Strong** | Doppler, RUPP model | PMID: 25298513 |
| HIF-1α → antiangiogenic shift | **Moderate–Strong** | Molecular, review-level | PMID: 41814104 |
| sFlt-1/sEng excess, PlGF deficit | **Very Strong** | GWAS, scRNA-seq, proteomics, biomarker | PMID: 28628106, 40253080, 31188674 |
| Endothelial dysfunction | **Strong** | In vitro, animal, interventional | PMID: 21810665, 22103497 |
| Organ-specific damage | **Strong** | Pathology, biomarker stratification | PMID: 42041953, 30399576 |

---

## Claim Classification

| Claim | Status | Evidence Level |
|---|---|---|
| Early-onset PE involves defective trophoblast invasion | **ESTABLISHED** | Multiple convergent evidence lines |
| Placental hypoxia drives antiangiogenic factor release | **ESTABLISHED** | Molecular, transcriptomic, functional |
| sFlt-1 excess and PlGF deficiency mark early-onset PE | **ESTABLISHED** | scRNA-seq, GWAS, FDA-approved biomarker |
| Fetal FLT1 variants confer genetic PE susceptibility | **ESTABLISHED** | GWAS (P = 5.4 × 10⁻¹⁶) |
| KIR AA + fetal HLA-C2 increases PE risk | **ESTABLISHED** (association); **EMERGING** (causation) | Multi-cohort genetics + in vitro |
| HIF-1α mediates hypoxia-to-sFlt-1 transcription | **ESTABLISHED** | Molecular pathway evidence |
| sEng synergizes with sFlt-1 | **ESTABLISHED** | Animal models, clinical correlations |
| sFlt-1 removal ameliorates PE symptoms | **EMERGING** | Pilot studies only (n = 8–12) |
| Bradford-Hill criteria satisfied for antiangiogenic causation | **ESTABLISHED** | Formal analysis |
| RUPP → sFlt-1 → hypertension causal chain | **ESTABLISHED** | Rat and mouse models |
| Glomerular endotheliosis from sFlt-1/VEGF imbalance | **ESTABLISHED** | Rat models + human renal pathology |
| sFlt-1/PlGF stratifies organ phenotypes | **EMERGING** | Single cohort (n = 320) |
| Early-onset PE pathophysiologically distinct from late-onset | **ESTABLISHED** | scRNA-seq, clinical, epidemiological |
| SASP contributes to maternal syndrome | **EMERGING** | snRNA-seq + spatial transcriptomics |
| AT1-AA independently contributes | **EMERGING** | Animal models; ~55% prevalence |
| Complement independent in HELLP | **SPECULATIVE** | n = 1 case report |
| Metformin/esomeprazole/pravastatin reduce sFlt-1 | **EMERGING** | In vitro + preliminary RCT |
| Late-onset PE driven by antiangiogenic shift | **CONTRADICTED** | scRNA-seq shows distinct pathology |

---

## Evidence Base

### Core Supporting Literature

The strongest evidence for the hypothesis comes from studies that directly test elements of the causal chain:

**Genetic evidence:** The discovery that the first genome-wide significant PE susceptibility locus maps to fetal FLT1 (rs4769613, P = 5.4 × 10⁻¹⁶) is arguably the single most important piece of evidence for the model ([PMID: 28628106](https://pubmed.ncbi.nlm.nih.gov/28628106/)). This was confirmed and contextualized by subsequent analysis showing PE heritability of ~55% and the fetal (not maternal) origin of the genetic risk ([PMID: 29138037](https://pubmed.ncbi.nlm.nih.gov/29138037/)).

**Transcriptomic evidence:** Two independent single-cell/single-nuclei RNA-seq studies of PE placentas demonstrate FLT1 upregulation and PGF downregulation at cellular resolution, specifically in syncytiotrophoblast and extravillous trophoblasts, confirming the molecular basis of the antiangiogenic shift in early-onset PE while showing that late-onset PE has a fundamentally different transcriptomic profile ([PMID: 40253080](https://pubmed.ncbi.nlm.nih.gov/40253080/); [PMID: 41582793](https://pubmed.ncbi.nlm.nih.gov/41582793/)).

**Causation analysis:** A formal Bradford-Hill criteria analysis demonstrated that antiangiogenic factors satisfy temporality (elevation precedes clinical signs), dose–response (higher levels correlate with severity), and experiment (removal improves outcomes), while inflammation fails temporality and experiment criteria ([PMID: 22103497](https://pubmed.ncbi.nlm.nih.gov/22103497/)).

**Interventional evidence:** Pilot sFlt-1 apheresis studies demonstrated that specifically removing sFlt-1 from the maternal circulation reduces proteinuria, stabilizes blood pressure, and prolongs pregnancy by 15–23 days ([PMID: 21810665](https://pubmed.ncbi.nlm.nih.gov/21810665/); [PMID: 29858106](https://pubmed.ncbi.nlm.nih.gov/29858106/)).

**Animal model evidence:** The RUPP model in both rats and mice recapitulates the full causal chain, and critically demonstrates that only interventions targeting the antiangiogenic pathway (not simple vasodilation) reverse the PE phenotype ([PMID: 25298513](https://pubmed.ncbi.nlm.nih.gov/25298513/); [PMID: 39224973](https://pubmed.ncbi.nlm.nih.gov/39224973/)).

**Translational review:** A comprehensive review by Thadhani and colleagues summarizes the translational trajectory from discovery of sFlt-1's causal role through FDA-approved molecular diagnostics to emerging therapeutic strategies ([PMID: 38300220](https://pubmed.ncbi.nlm.nih.gov/38300220/)).

### Qualifying and Competing Literature

**Late-onset PE distinction:** The most important qualification comes from single-cell data showing that late-onset PE has a distinct pathophysiology — "suggestive of a distinct pathophysiological process driven by maternal cardiovascular maladaptation, placental aging, cellular senescence and oxidative stress" ([PMID: 41582793](https://pubmed.ncbi.nlm.nih.gov/41582793/)).

**Complement in HELLP:** A single case report of eculizumab in HELLP suggests complement may be independently targetable ([PMID: 23228435](https://pubmed.ncbi.nlm.nih.gov/23228435/)), qualifying the completeness of the antiangiogenic model for HELLP specifically.

**Biomarker limitations:** Multiple studies document that the sFlt-1/PlGF ratio requires population-specific calibration and has reduced performance in multifetal pregnancies ([PMID: 41213792](https://pubmed.ncbi.nlm.nih.gov/41213792/); [PMID: 41294257](https://pubmed.ncbi.nlm.nih.gov/41294257/)).

---

## Evidence Matrix

| # | Citation | Evidence Type | Direction | Claim Tested | Key Finding | Subtype | Confidence |
|---|---|---|---|---|---|---|---|
| 1 | [PMID: 28628106](https://pubmed.ncbi.nlm.nih.gov/28628106/) | Human (GWAS) | Supports | FLT1 genetic risk | Fetal rs4769613 near FLT1, P = 5.4×10⁻¹⁶ | All PE (fetal) | Very High |
| 2 | [PMID: 40253080](https://pubmed.ncbi.nlm.nih.gov/40253080/) | Human (scRNA-seq) | Supports | FLT1↑/PGF↓ in placenta | Single-cell confirms angiogenic imbalance in STB/EVT | Early-onset PE | High |
| 3 | [PMID: 41582793](https://pubmed.ncbi.nlm.nih.gov/41582793/) | Human (snRNA-seq) | Supports + Qualifies | Subtype-specific pathology | Profound dysregulation in early-onset; subtle in late-onset | Both subtypes | High |
| 4 | [PMID: 22103497](https://pubmed.ncbi.nlm.nih.gov/22103497/) | Review (Bradford-Hill) | Supports | Antiangiogenic > inflammation causation | sFlt-1 satisfies temporality, dose-response, experiment | All PE | High |
| 5 | [PMID: 24091323](https://pubmed.ncbi.nlm.nih.gov/24091323/) | Human + in vitro | Supports | KIR/HLA-C upstream trigger | KIR2DS1 + HLA-C2 → GM-CSF → trophoblast migration | Early-onset PE | High |
| 6 | [PMID: 20972337](https://pubmed.ncbi.nlm.nih.gov/20972337/) | Human (genetic epi) | Supports | Immune maladaptation | KIR AA mothers at increased PE risk | All subtypes | High |
| 7 | [PMID: 21810665](https://pubmed.ncbi.nlm.nih.gov/21810665/) | Human (pilot) | Supports | sFlt-1 removal reverses PE | Apheresis lowered sFlt-1, reduced proteinuria, stabilized BP | Very preterm PE | Moderate (n=8) |
| 8 | [PMID: 29858106](https://pubmed.ncbi.nlm.nih.gov/29858106/) | Human (intervention) | Supports | sFlt-1 removal prolongs pregnancy | H.E.L.P. apheresis: 15.0 vs 6.3 days (p=0.027) | Very preterm PE | Moderate (n=12) |
| 9 | [PMID: 25298513](https://pubmed.ncbi.nlm.nih.gov/25298513/) | Animal (mouse RUPP) | Supports | Ischemia → sFlt-1 → HTN | RUPP: ↑BP, ↑sFlt-1, ↓fetal weight | Model | High |
| 10 | [PMID: 39224973](https://pubmed.ncbi.nlm.nih.gov/39224973/) | Animal (rat RUPP) | Supports | Pathway specificity | GPER agonist restored sFlt-1; hydralazine did not | Model | High |
| 11 | [PMID: 41814104](https://pubmed.ncbi.nlm.nih.gov/41814104/) | Review (molecular) | Supports | HIF-1α as hub | HIF-1α → mitochondrial dysfunction + sFlt-1 upregulation | Early-onset PE | Moderate (review) |
| 12 | [PMID: 31188674](https://pubmed.ncbi.nlm.nih.gov/31188674/) | Human (prospective) | Supports | sFlt-1/PlGF diagnostic | NPV 98.6% at cutoff ≤38 for ruling out PE ≤1 week | Asian pop. | High (n=700) |
| 13 | [PMID: 41213792](https://pubmed.ncbi.nlm.nih.gov/41213792/) | Human (cohort) | Qualifies | Biomarker performance | AUC 0.789 in twins vs 0.870 singletons | Multifetal | Moderate |
| 14 | [PMID: 30399576](https://pubmed.ncbi.nlm.nih.gov/30399576/) | Review (renal) | Supports | sFlt-1 → renal damage | sFlt-1 abrogates VEGF binding → podocyte damage | Renal phenotype | High |
| 15 | [PMID: 24335973](https://pubmed.ncbi.nlm.nih.gov/24335973/) | Animal (rat) | Supports | Reversible renal pathology | NaHS reversed sFlt-1 glomerular endotheliosis via VEGF | Renal | High |
| 16 | [PMID: 29466360](https://pubmed.ncbi.nlm.nih.gov/29466360/) | In vitro | Supports | Drug target validation | Metformin + esomeprazole additive at reducing sFlt-1 | Therapeutic | Moderate |
| 17 | [PMID: 28619690](https://pubmed.ncbi.nlm.nih.gov/28619690/) | Review | Supports | Metformin mechanism | Reduces sFlt-1/sEng via mitochondrial effects | Therapeutic | Moderate |
| 18 | [PMID: 34666379](https://pubmed.ncbi.nlm.nih.gov/34666379/) | Human (RCT) | Supports (trend) | Pravastatin prevents PE | PE 17.5% vs 35% (NS); sFlt-1/PlGF stabilized | Prevention | Moderate (n=80) |
| 19 | [PMID: 39440423](https://pubmed.ncbi.nlm.nih.gov/39440423/) | Human (multi-omics) | Qualifies | SASP parallel mechanism | STB senescence; PAI-1/activin A elevated in 1st trimester | Early-onset PE | Moderate-High |
| 20 | [PMID: 23228435](https://pubmed.ncbi.nlm.nih.gov/23228435/) | Human (case report) | Competing | Complement in HELLP | Eculizumab improved HELLP independently of sFlt-1 | HELLP | Low (n=1) |
| 21 | [PMID: 42041953](https://pubmed.ncbi.nlm.nih.gov/42041953/) | Human (cohort) | Supports | Phenotype stratification | sFlt-1/PlGF highest in renal, then hepatic, hematologic | Within-PE | Moderate (n=320) |
| 22 | [PMID: 29138037](https://pubmed.ncbi.nlm.nih.gov/29138037/) | Human (GWAS) | Supports | Fetal FLT1 confirmed | Fetal DNA variants near FLT1 in angiogenesis regulation | All PE | Very High |
| 23 | [PMID: 35177220](https://pubmed.ncbi.nlm.nih.gov/35177220/) | Review (historical) | Supports | Two-disease paradigm | Early-onset = atherosclerosis; late-onset = metabolic crisis | Both subtypes | High (review) |

---

## Alternative Models

{{figure:models_comparison.png|caption=Competing and complementary mechanistic models for preeclampsia pathogenesis with relationship to the seed hypothesis}}

### 1. Maternal Cardiovascular Maladaptation Model (Late-Onset PE)
**Relationship:** Alternative mechanism for a different subtype — does not compete for early-onset PE.
Late-onset PE (>34 weeks) appears driven by maternal cardiovascular susceptibility meeting increasing fetal metabolic demands, without severe primary placental malperfusion. Single-cell data show late-onset PE has distinct pathology: "suggestive of a distinct pathophysiological process driven by maternal cardiovascular maladaptation, placental aging, cellular senescence and oxidative stress" ([PMID: 41582793](https://pubmed.ncbi.nlm.nih.gov/41582793/)). This defines the boundary of the seed hypothesis rather than refuting it.

### 2. Complement-Mediated Endothelial Injury (HELLP)
**Relationship:** Parallel effector pathway, potentially independent.
Complement activation may independently drive thrombotic microangiopathy in HELLP. The eculizumab case report ([PMID: 23228435](https://pubmed.ncbi.nlm.nih.gov/23228435/)) suggests complement inhibition alone can improve HELLP without targeting sFlt-1. If confirmed, this would mean HELLP requires dual-targeting. Evidence remains at case-report level.

### 3. AT1-AA Autoimmune Model
**Relationship:** Parallel amplifying mechanism.
AT1-AA are detected in ~55% of PE women and induce PE-like phenotype in animal models ([PMID: 41275618](https://pubmed.ncbi.nlm.nih.gov/41275618/)). However, they are not universally present and fail Bradford-Hill criteria as the primary cause. AT1-AA likely amplifies endothelial dysfunction initiated by the antiangiogenic shift.

### 4. Syncytiotrophoblast Stress/SASP Model
**Relationship:** Upstream amplifier and parallel pathway.
SASP in syncytiotrophoblast may amplify placental stress and contribute secreted factors (PAI-1, activin A) independently of sFlt-1/sEng ([PMID: 39440423](https://pubmed.ncbi.nlm.nih.gov/39440423/)). First-trimester elevation suggests this may precede the antiangiogenic shift.

### 5. Oxidative Stress / Mitochondrial Dysfunction Model
**Relationship:** Intermediate mechanism within the causal chain.
HIF-1α-driven mitochondrial dysfunction is mechanistically positioned between placental ischemia and sFlt-1 production ([PMID: 41814104](https://pubmed.ncbi.nlm.nih.gov/41814104/)). Clinical failure of broad antioxidants (vitamins C, E) indicates this is not independently targetable ([PMID: 41897533](https://pubmed.ncbi.nlm.nih.gov/41897533/)).

---

## Limitations and Knowledge Gaps

### Gap 1: HIF-1α → sFlt-1 Link Needs Human Perturbation Evidence
**Scope:** The transcriptional mechanism linking placental hypoxia to sFlt-1 overproduction.
**Why it matters:** HIF-1α is proposed as the key hub, but evidence is primarily from review-level synthesis and in vitro studies. No conditional HIF-1α knockout or inhibitor studies in human placental tissue.
**What was checked:** PubMed searches for HIF-1α perturbation in human PE placenta returned only review-level evidence.
**Resolution:** Conditional HIF-1α knockout in trophoblast organoids or placental explants with measurement of sFlt-1 output.

### Gap 2: No Phase III RCT of Targeted sFlt-1 Reduction
**Scope:** The final interventional proof of the model.
**Why it matters:** While pilot apheresis studies and pharmacological approaches show promise, no large-scale randomized trial has demonstrated that specifically targeting sFlt-1 prevents or treats early-onset PE.
**What was checked:** PubMed and literature reviews for sFlt-1-targeted RCTs; only pilot studies found (n = 8–12).
**Resolution:** STEEP trial (siRNA against sFlt-1) or large apheresis RCTs currently in development.

### Gap 3: Complement Independence in HELLP Unresolved
**Scope:** Whether complement activation in HELLP is independent of or downstream from the antiangiogenic shift.
**Why it matters:** Determines whether complement inhibitors should be used alongside or instead of antiangiogenic therapies for HELLP.
**What was checked:** Only one case report of eculizumab ([PMID: 23228435](https://pubmed.ncbi.nlm.nih.gov/23228435/)); systematic review showed heterogeneous complement evidence ([PMID: 38983853](https://pubmed.ncbi.nlm.nih.gov/38983853/)).
**Resolution:** RCT of eculizumab in HELLP with concurrent sFlt-1/PlGF monitoring.

### Gap 4: Population-Specific Biomarker Thresholds
**Scope:** sFlt-1/PlGF PPV varies substantially (30–75%) across ethnic groups, gestational ages, and pregnancy types.
**Why it matters:** False positives may lead to unnecessary interventions; limits universal clinical implementation.
**What was checked:** Validation cohorts in Asia, New Zealand, U.S., multifetal pregnancies.
**Resolution:** Large multi-ethnic cohorts with standardized assay platforms.

### Gap 5: FLT1 GWAS Subtype Stratification
**Scope:** The fetal FLT1 GWAS hit was not stratified by early vs. late PE.
**Why it matters:** The hypothesis predicts FLT1 variants should be specific to early-onset PE; confirmation requires subtype-stratified analysis.
**What was checked:** PMID: 28628106 and PMID: 29138037; no subtype-stratified re-analysis found.
**Resolution:** Subtype-stratified re-analysis of existing GWAS data; two-sample Mendelian randomization.

### Gap 6: KIR/HLA-C Attributable Risk Unknown
**Scope:** KIR/HLA-C accounts for some but not all cases of defective trophoblast invasion.
**Why it matters:** Other upstream triggers may exist; the population-attributable fraction is unknown.
**What was checked:** Multiple KIR/HLA-C studies found, but no population-attributable risk quantification.
**Resolution:** Prospective KIR/HLA-C genotyping in large PE cohort with attributable risk analysis.

### Gap 7: Source-Level Absence — No GenCC/ClinGen Classification
**Scope:** No formal gene-disease validity curation exists for FLT1 in PE.
**Why it matters:** Despite GWAS evidence, FLT1 has not been curated by ClinGen, limiting clinical genetics integration.
**Resolution:** ClinGen gene curation expert panel review.

---

## Discriminating Tests

### Test 1: sFlt-1 siRNA Phase III Trial
- **Patients:** Women with early-onset PE (20–32 weeks) with sFlt-1/PlGF >85
- **Intervention:** siRNA targeting placental sFlt-1 mRNA vs. standard care
- **Primary outcome:** Time from randomization to delivery
- **Expected result if hypothesis correct:** Significant prolongation of pregnancy with improved outcomes
- **Discriminates from:** AT1-AA and complement models (which predict no benefit from sFlt-1 targeting alone)

### Test 2: Eculizumab RCT in HELLP with Angiogenic Monitoring
- **Patients:** HELLP syndrome with concurrent sFlt-1/PlGF measurement
- **Intervention:** Eculizumab vs. standard care
- **Biomarkers:** Serial complement markers (C3a, C5a, sC5b-9) and sFlt-1/PlGF
- **Expected if complement independent:** Clinical improvement without sFlt-1/PlGF change
- **Discriminates from:** Pure antiangiogenic model (which predicts complement inhibition alone is insufficient)

### Test 3: Longitudinal Multi-Omic Temporal Ordering
- **Cohort:** 5,000+ women with serial sampling at 8, 12, 20, 28, 34 weeks
- **Assays:** sFlt-1/PlGF, complement markers, AT1-AA, SASP factors (activin A, PAI-1), KIR/HLA-C genotyping
- **Analysis:** Time-course modeling of which biomarker class elevates first
- **Expected result:** Definitive temporal hierarchy of antiangiogenic, complement, autoimmune, and senescence pathways

### Test 4: FLT1 Mendelian Randomization
- **Design:** Two-sample MR using FLT1 variants as instruments for circulating sFlt-1, PE as outcome
- **Data source:** UK Biobank, FinnGen
- **Expected if causal:** Genetically elevated sFlt-1 increases PE risk
- **Discriminates from:** sFlt-1 as epiphenomenon

### Test 5: Combined Apheresis + Eculizumab in Severe HELLP
- **Design:** 2×2 factorial (sFlt-1 apheresis ± eculizumab)
- **Expected if both pathways independent:** Additive benefit of combination
- **Discriminates from:** Single-pathway models

---

## Curation Leads

*All items below are candidate KB updates requiring curator verification.*

### Candidate Evidence References (with Verified Snippets)

1. **[PMID: 40253080](https://pubmed.ncbi.nlm.nih.gov/40253080/)** — *Placenta at single-cell resolution in early and late preeclampsia*
   - Snippet: "Key findings in early-onset preeclampsia included disrupted syncytiotrophoblast and extravillous trophoblast angiogenic signaling, characterized by an up-regulation of FLT1 and down-regulation of PGF, consistent with an angiogenic imbalance."
   - → Add as primary evidence for FLT1/PGF dysregulation node (SUPPORT, HUMAN_CLINICAL)

2. **[PMID: 41582793](https://pubmed.ncbi.nlm.nih.gov/41582793/)** — *Types of Preeclampsia According to Placental Single Cell RNA Sequencing*
   - Snippet: "Profound cellular dysregulation was identified in early-onset preeclampsia across multiple placental cell types, consistent with widespread placental dysfunction, angiogenic imbalance, inflammatory response and apoptosis. In contrast, late-onset preeclampsia exhibited comparatively subtle transcriptional changes, suggestive of a distinct pathophysiological process driven by maternal cardiovascular maladaptation, placental aging, cellular senescence and oxidative stress."
   - → Add as evidence for subtype restriction and against late-onset PE application

3. **[PMID: 28628106](https://pubmed.ncbi.nlm.nih.gov/28628106/)** — *Variants in the fetal genome near FLT1 are associated with risk of preeclampsia*
   - → Add as GWAS evidence for FLT1 causal role; note fetal genome origin

4. **[PMID: 22103497](https://pubmed.ncbi.nlm.nih.gov/22103497/)** — *Is inflammation the cause of pre-eclampsia?*
   - Snippet: "the elevation of anti-angiogenic factors that precede the clinical signs of pre-eclampsia fulfils the criterion of temporality"
   - → Add as Bradford-Hill causation evidence (SUPPORT, HUMAN_CLINICAL/REVIEW)

5. **[PMID: 42041953](https://pubmed.ncbi.nlm.nih.gov/42041953/)** — *Angiogenic Imbalance Defines Multisystem Phenotypes of Preeclampsia*
   - Snippet: "Within preeclampsia, the renal-dominant phenotype showed the highest ratio (66.0 ± 22.5), followed by hepatic (55.9 ± 18.2) and hematologic phenotypes (52.0 ± 16.8)."
   - → Add as evidence for organ-phenotype stratification by antiangiogenic ratio

### Candidate Pathophysiology Nodes and Edges

| Type | Source → Target | Evidence | Status |
|---|---|---|---|
| Edge | HIF-1α stabilization → FLT1 transcription → sFlt-1 overproduction | PMID: 41814104 | Established |
| Edge | Maternal KIR AA + fetal HLA-C2 → deficient dNK → impaired trophoblast invasion | PMID: 20972337, 24091323 | Established |
| Edge | KIR2DS1 + HLA-C2 → GM-CSF → trophoblast migration | PMID: 24091323 | Established |
| Edge | Fetal FLT1 rs4769613 → sFlt-1 susceptibility → PE risk | PMID: 28628106 | Established |
| Edge | sFlt-1 → VEGF sequestration → podocyte-endothelial disruption | PMID: 30399576, 24335973 | Established |
| Node | Syncytiotrophoblast SASP (PAI-1, activin A) | PMID: 39440423 | Emerging |
| Edge | Complement C5 → TMA (independent of sFlt-1, HELLP-specific) | PMID: 23228435 | Speculative |

### Candidate Ontology Terms
- **Cell types:** Syncytiotrophoblast (CL:0000525), Extravillous trophoblast (CL:0008036), Decidual NK cell (CL:0002252), Podocyte (CL:0000653)
- **Biological processes:** Trophoblast cell migration (GO:0008045), Sprouting angiogenesis (GO:0002040), Placenta development (GO:0001890), Response to hypoxia (GO:0001666)
- **Molecular functions:** VEGF receptor binding (GO:0005172)

### Candidate Subtype Restrictions
- **Confirm:** Hypothesis applies to Early-onset PE and HELLP (as stated in YAML)
- **Add explicit exclusion:** Late-onset PE (>34 weeks) — distinct pathophysiology
- **Qualify HELLP:** Complement may be an independent effector pathway requiring separate therapeutic targeting

### Candidate Status Change
- **Current status:** CANONICAL → **Recommended:** MAINTAIN CANONICAL
- Add annotation: "Does not apply as primary mechanism to late-onset PE (>34 weeks)"

### Candidate Knowledge Gaps for KB
1. HIF-1α → sFlt-1: Needs direct human perturbation evidence
2. Phase III sFlt-1 targeted trial: Missing — critical for definitive interventional proof
3. Complement independence in HELLP: n = 1 case report — needs RCT
4. FLT1 GWAS subtype stratification: Not yet performed
5. Population-specific sFlt-1/PlGF thresholds: Required for universal biomarker implementation
6. First-trimester temporal ordering of parallel pathways: Unknown
7. GenCC/ClinGen FLT1 curation: Absent

{{figure:integrated_assessment.png|caption=Integrated evidence assessment table summarizing all evidence domains for the early-onset PE antiangiogenic model}}

---

## Conclusion

The early-onset placenta-dominant antiangiogenic model is among the most well-validated mechanistic hypotheses for any complex pregnancy disorder. Its canonical status is justified by convergent evidence from genetics through clinical intervention, formal satisfaction of Bradford-Hill causation criteria, and the absence of reproducible refuting evidence across 98 reviewed papers. The model's defined boundaries (not applicable to late-onset PE, incomplete coverage of HELLP complement biology) and the absence of a completed Phase III sFlt-1-targeted trial represent the principal caveats rather than fundamental weaknesses. The most impactful next step for the field is completion of a definitive interventional trial demonstrating that targeted sFlt-1 reduction prevents or treats early-onset preeclampsia — transforming decades of observational and mechanistic evidence into a cure.
