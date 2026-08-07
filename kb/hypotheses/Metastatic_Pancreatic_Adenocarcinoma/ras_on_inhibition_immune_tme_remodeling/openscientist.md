---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-24T00:57:08.534932'
end_time: '2026-07-24T01:13:35.827549'
duration_seconds: 987.29
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Metastatic Pancreatic Adenocarcinoma
  category: ''
  hypothesis_group_id: ras_on_inhibition_immune_tme_remodeling
  hypothesis_label: RAS(ON) Inhibition Remodels the Immunosuppressive Microenvironment
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: ras_on_inhibition_immune_tme_remodeling\n\
    hypothesis_label: RAS(ON) Inhibition Remodels the Immunosuppressive Microenvironment\n\
    status: EMERGING\ndescription: Oncogenic RAS-MAPK signaling helps establish the\
    \ immunosuppressive, T-cell-excluded microenvironment\n  that renders metastatic\
    \ PDAC refractory to immune checkpoint blockade. This hypothesis proposes that\n\
    \  sustained RAS(ON) multiselective inhibition with daraxonrasib partially reverses\
    \ that state - increasing\n  tumor antigen presentation, relieving myeloid-derived\
    \ suppressor and regulatory-T-cell dominance, and\n  promoting effector T-cell\
    \ infiltration - thereby opening a therapeutic window for combination with checkpoint\n\
    \  inhibitors or other immunotherapies that single-agent approaches have not achieved\
    \ in PDAC. The testable\n  prediction is that daraxonrasib plus checkpoint blockade\
    \ yields deeper and more durable responses than\n  either alone, with the on-treatment\
    \ tumor immune contexture as the pharmacodynamic readout.\nnotes: Seed hypothesis\
    \ for OpenScientist deep-research exploration; supporting evidence on RAS/KRAS-inhibition-driven\n\
    \  immune remodeling in PDAC is to be gathered and verified through the deep-research\
    \ run rather than asserted\n  here."
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
citation_count: 13
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Metastatic Pancreatic Adenocarcinoma
- **Category:** 

## Target Hypothesis
- **Hypothesis ID:** ras_on_inhibition_immune_tme_remodeling
- **Hypothesis Label:** RAS(ON) Inhibition Remodels the Immunosuppressive Microenvironment
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: ras_on_inhibition_immune_tme_remodeling
hypothesis_label: RAS(ON) Inhibition Remodels the Immunosuppressive Microenvironment
status: EMERGING
description: Oncogenic RAS-MAPK signaling helps establish the immunosuppressive, T-cell-excluded microenvironment
  that renders metastatic PDAC refractory to immune checkpoint blockade. This hypothesis proposes that
  sustained RAS(ON) multiselective inhibition with daraxonrasib partially reverses that state - increasing
  tumor antigen presentation, relieving myeloid-derived suppressor and regulatory-T-cell dominance, and
  promoting effector T-cell infiltration - thereby opening a therapeutic window for combination with checkpoint
  inhibitors or other immunotherapies that single-agent approaches have not achieved in PDAC. The testable
  prediction is that daraxonrasib plus checkpoint blockade yields deeper and more durable responses than
  either alone, with the on-treatment tumor immune contexture as the pharmacodynamic readout.
notes: Seed hypothesis for OpenScientist deep-research exploration; supporting evidence on RAS/KRAS-inhibition-driven
  immune remodeling in PDAC is to be gathered and verified through the deep-research run rather than asserted
  here.
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

# RAS(ON) Inhibition Remodels the Immunosuppressive Microenvironment in Metastatic Pancreatic Adenocarcinoma

**Hypothesis ID:** `ras_on_inhibition_immune_tme_remodeling`
**Status in KB:** EMERGING
**Disease:** Metastatic Pancreatic Adenocarcinoma (mPDAC)
**Report date:** 2026-07-24

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED.**

The seed hypothesis holds that oncogenic RAS-MAPK signaling actively enforces the immunosuppressive, T-cell-excluded microenvironment that renders metastatic PDAC refractory to immune checkpoint blockade (ICB), and that sustained multiselective RAS(ON) inhibition with daraxonrasib partially reverses that state — boosting antigen presentation, relieving myeloid-derived suppressor cell (MDSC) and regulatory-T-cell (Treg) dominance, and promoting effector T-cell infiltration — thereby opening a therapeutic window for ICB combinations. The literature provides **strong preclinical support for the central spine of this causal chain**, but the specific therapeutic prediction and two of the three named immune arms remain unproven.

What is well established: In multiple genetically engineered and autochthonous PDAC models, lowering oncogenic KRAS activity remodels the immune compartment — increasing intratumoral CD8+ effector T cells, decreasing myeloid infiltration, reprogramming cancer-associated fibroblasts (CAFs), and inducing tumor-cell FAS — and, critically, **combining KRAS/MAPK inhibition with checkpoint blockade achieves durable, CD8-dependent regression that neither agent achieves alone** (PMIDs 37625401, 36824971, 37782788, 38727236). This is the core testable prediction of the hypothesis, and it is confirmed at the preclinical level. Daraxonrasib itself is now a clinically validated RAS(ON) agent in mPDAC, with a phase 3 survival benefit over chemotherapy (RASolute 302, PMID 42223072).

What limits the verdict to "partially supported": (1) The strongest **immune-remodeling + ICB-sensitization** data come from the KRAS-G12D-selective inhibitor **MRTX1133**, not daraxonrasib; the strongest **daraxonrasib-containing** immune-remodeling data are in KRAS-G12C **NSCLC**, not PDAC (PMID 41670434). (2) Daraxonrasib's PDAC clinical evidence to date is **monotherapy survival benefit only** — the pivotal daraxonrasib + ICB combination, with on-treatment tumor immune contexture as pharmacodynamic readout, is **clinically untested**. (3) The remodeling is **transient and self-reversing** via an adaptive CDK8→CXCL2 myeloid program that drives resistance (PMID 42436354), and counter-regulatory immunosuppression (IL6+ inflammatory CAFs, M2 macrophages) can follow RAS-pathway inhibition (PMID 38727236). (4) Two named arms are only weakly "owned" by RAS: the **antigen-presentation** arm is dominantly autophagy- and FAK-driven and largely RAS-independent (PMIDs 32376951/32459143, 36977556), and **no primary evidence was found** that RAS/daraxonrasib inhibition relieves Treg dominance in PDAC (source absence).

The hypothesis is therefore mechanistically credible and preclinically anchored, but its distinctive clinical claim — that daraxonrasib + ICB delivers deeper, more durable responses than either alone in patients — is an open, high-value, and currently untested question.

---

## Key Findings

### F1 — A RAS(ON) inhibitor doublet boosts antigen presentation and sensitizes an immune-refractory tumor to ICB (preclinical, NSCLC)

In immune-competent preclinical models, the multiselective RAS(ON) inhibitor **daraxonrasib** combined with the G12C-selective RAS(ON) inhibitor **elironrasib** produced immune-dependent complete regressions and sensitized an immunorefractory KRAS-G12C NSCLC model to checkpoint blockade. The verbatim mechanistic claim is that "the RAS(ON) inhibitor doublet enhances tumor immune recognition by boosting antigen presentation and remodeling the suppressive tumor microenvironment, thus promoting immune-dependent complete regressions and sensitization of an immunorefractory model to checkpoint blockade" ([PMID: 41670434](https://pubmed.ncbi.nlm.nih.gov/41670434/)). This is the most direct demonstration of the exact causal chain the seed hypothesis proposes, and it explicitly involves daraxonrasib — but the disease context is **NSCLC, not PDAC**. It is therefore the strongest daraxonrasib-specific evidence available, with the caveat that the immune biology of PDAC (dense desmoplastic stroma, near-zero baseline ICB response) differs materially from NSCLC.

### F2 — KRAS/MEK inhibition plus checkpoint blockade achieves durable regression in PDAC models; KRAS activity predicts immune composition

In PDAC preclinical models, lowering KRAS activity in established tumors "promotes immune infiltration, but with a limited antitumor effect, whereas combining KRAS/MEK inhibition with immune checkpoint blockade achieves durable regression in preclinical models" ([PMID: 37782788](https://pubmed.ncbi.nlm.nih.gov/37782788/)). KRAS activity scores predicted tumor immune composition and therapy response. This finding is central: it demonstrates both that RAS-pathway output is a determinant of the immune contexture and that **ICB combination is required for durable benefit** — mono-RAS-inhibition remodels but does not cure. This directly matches the seed hypothesis's testable prediction.

### F3 — RAS-pathway inhibition triggers counter-regulatory myeloid/stromal immunosuppression, requiring myeloid re-activation for durable ICB benefit

In KPCY PDAC models, combined SOS1 + MEK inhibition (SOS1i+MEKi) increased intratumoral CD8+ T cells but produced no durable responses. Single-cell RNA sequencing "revealed an increase in inflammatory cancer-associated fibroblasts (iCAF), M2 macrophages, and a decreased dendritic cell (DC) quality that ultimately resulted in a highly immunosuppressive microenvironment driven by IL6+ iCAFs" ([PMID: 38727236](https://pubmed.ncbi.nlm.nih.gov/38727236/)). Adding a CD40 agonist reverted macrophage polarization, and further adding checkpoint blockade produced "tumor-free mice with established immune memory." This **qualifies** the seed hypothesis: RAS-pathway inhibition does not simply relieve suppression — it triggers a counter-regulatory immunosuppressive rebound that must be actively countered (here, via CD40 agonism) before ICB can deliver durable cures.

### F4 — Daraxonrasib improves survival in metastatic PDAC (RASolute 302, phase 3) — clinical proof of RAS(ON) targeting, but immune readout untested

The phase 3 RASolute 302 trial (NCT06625320, n=500, 91.8% RAS-mutant primary subpopulation) showed that "among patients with previously treated mPDAC, treatment with daraxonrasib led to significantly longer overall survival and progression-free survival than chemotherapy" ([PMID: 42223072](https://pubmed.ncbi.nlm.nih.gov/42223072/)). An independent report described an "unprecedented doubling of overall survival" versus chemotherapy ([PMID: 42226659](https://pubmed.ncbi.nlm.nih.gov/42226659/)). This provides clinical proof that multiselective RAS(ON) inhibition benefits mPDAC — the exact disease context of the hypothesis — but the trial was **monotherapy versus chemotherapy**, with no ICB arm and no on-treatment tumor immune contexture readout. The immune-remodeling mechanism is thus inferred, not measured, in the clinical setting.

### F5 — KRAS-G12D inhibition (MRTX1133) reprograms the PDAC TME, increases CD8+ T cells via FAS, and synergizes with checkpoint blockade — strongest PDAC-specific support

Across 16 KRAS-G12D-driven PDAC models, MRTX1133 reversed tumor growth, "increases intratumoral CD8+ effector T cells, decreases myeloid infiltration, and reprograms cancer associated fibroblasts" ([PMID: 37625401](https://pubmed.ncbi.nlm.nih.gov/37625401/)). Mechanistically, "regression of advanced PDAC requires CD8+ T cells and immune checkpoint blockade therapy (iCBT) synergizes with MRTX1133 to eradicate PDAC and prolong overall survival," with KRAS-G12D inhibition inducing tumor-cell **FAS** to enable CD8+ T-cell-mediated death ([PMID: 36824971](https://pubmed.ncbi.nlm.nih.gov/36824971/)). This is the strongest PDAC-specific support for the full hypothesis chain — relief of myeloid suppression, effector T-cell infiltration, CAF reprogramming, and CD8-dependent ICB synergy — but it is achieved with the **G12D-selective** MRTX1133, not the multiselective daraxonrasib named in the hypothesis.

### F6 — Immune remodeling after KRAS-G12D/daraxonrasib inhibition is transient; CDK8-driven adaptive reversal drives resistance (key durability qualifier)

Integrated spatial transcriptomics, scRNA-seq, and CODEX spatial proteomics of PDAC models showed that "while KRAS-G12D inhibition by MRTX1133 initially increases CD11c+ cells and T cell infiltration proximal to cancer cells, long-term treatment results in reversal of the immune responses leading to resistance promoted by multiprotein mediator complex associated kinase CDK8" ([PMID: 42436354](https://pubmed.ncbi.nlm.nih.gov/42436354/)). Resistance was driven via CXCL2 chemokine secretion, FAS suppression, and TME remodeling toward immune evasion. The paper title explicitly covers resistance to both KRAS(G12D) inhibitors and daraxonrasib. This is a pivotal **durability qualifier**: the immune-remodeling window is self-limiting, and CDK8 is a candidate node whose co-targeting may be required to sustain the window daraxonrasib opens.

### F7 — Human PDAC metabolic-immune axis: KRAS-G12D-driven cholesterol metabolism promotes CD8 exhaustion; KRAS inhibition reverses it (USP20 node)

Integrating whole-exome sequencing, untargeted metabolomics, and scRNA-seq of human PDAC specimens plus autochthonous mouse and PDX models, KRAS-G12D was found to enhance cholesterol metabolism and promote CD8+ T-cell exhaustion, whereas KRAS-G12D inhibition reversed this. USP20 acts as a metabolic checkpoint orchestrating CD8+ T-cell function and modulating KRAS-G12D-inhibitor efficacy ([PMID: 42392864](https://pubmed.ncbi.nlm.nih.gov/42392864/)). This adds a **human-tissue-anchored** mechanistic layer (metabolic reprogramming → T-cell exhaustion) to the hypothesis and identifies USP20 as a druggable modifier of KRAS-inhibitor immune efficacy.

### F8 — The antigen-presentation arm is substantially RAS-independent: autophagy (NBR1) and FAK degrade/suppress MHC-I (competing mechanism)

Selective autophagy targets MHC-I for lysosomal degradation via NBR1 in PDAC; autophagy inhibition restores surface MHC-I and enhances anti-tumor CD8+ T-cell responses and ICB sensitivity ([PMID: 32376951](https://pubmed.ncbi.nlm.nih.gov/32376951/) / [PMID: 32459143](https://pubmed.ncbi.nlm.nih.gov/32459143/), Yamamoto et al., *Nature* 2020). Independently, cell-intrinsic FAK signaling suppresses the immunoproteasome and MHC-I; FAK loss increases antigen diversity and presentation and, with STAT3 co-depletion, drives tumor-reactive CD8 infiltration ([PMID: 36977556](https://pubmed.ncbi.nlm.nih.gov/36977556/)). Direct evidence that KRAS/daraxonrasib inhibition restores MHC-I specifically via the RAS-MAPK axis was **not found**. This means the "increased antigen presentation" arm of the hypothesis is better explained by parallel, RAS-independent (or only partly RAS-linked) pathways.

### F9 — Source/data absence: no direct evidence that RAS/daraxonrasib inhibition relieves Treg dominance in PDAC

Targeted PubMed searches for KRAS/RAS-inhibitor effects on regulatory T cells in pancreatic cancer returned no primary studies demonstrating Treg depletion or functional disarming after KRAS/daraxonrasib inhibition. The only RAS-Treg-adjacent hit was an unrelated adjuvant RAS-peptide yeast vaccine trial (GI-4000, [PMID: 33786412](https://pubmed.ncbi.nlm.nih.gov/33786412/)). By contrast, CD8+ effector infiltration, myeloid reduction, and CAF reprogramming after KRAS inhibition are well documented. This is a **curation-relevant source absence**: the Treg-relief edge in the hypothesis is currently unsupported.

---

## Mechanistic Model / Interpretation

The hypothesis implies the following causal chain. Below, each link is annotated with the strength of literature support.

```
 Oncogenic KRAS (G12D/G12V/G12C etc.)  ── mutation, ~90% of PDAC
        │  [STRONG: KRAS is the disease-defining driver]
        ▼
 Sustained RAS-MAPK signaling output
        │  [STRONG: KRAS activity score predicts immune composition — PMID 37782788]
        ▼
 Immunosuppressive, T-cell-excluded TME
   ├─ myeloid/MDSC dominance          [STRONG: reversed by KRAS-i — PMIDs 37625401, 36824971]
   ├─ CAF/desmoplastic exclusion      [STRONG: reprogrammed by KRAS-i — PMID 37625401]
   ├─ suppressed antigen presentation [WEAK for RAS: autophagy/FAK-driven — PMIDs 32376951, 36977556]
   ├─ Treg dominance                  [ABSENT: no primary PDAC RAS-i → Treg evidence — F9]
   └─ CD8 exhaustion (metabolic)      [MODERATE: cholesterol/USP20 axis — PMID 42392864]
        │
        ▼
 ICB-refractory metastatic PDAC (response <5%)
        │
   ┌────┴──── daraxonrasib / RAS(ON) inhibition ────┐
   ▼                                                 ▼
 Partial reversal of suppression            Counter-regulatory REBOUND
   ├─ ↑ CD8+ effector infiltration            ├─ IL6+ iCAFs, M2 macrophages (PMID 38727236)
   ├─ ↓ myeloid infiltration                  └─ CDK8→CXCL2 adaptive reversal (PMID 42436354)
   ├─ ↑ tumor FAS (CD8 killing)                     → transient window, resistance
   └─ CAF reprogramming
        │  [STRONG preclinical, chiefly MRTX1133]
        ▼
 Therapeutic window for ICB combination
        │  [STRONG preclinical: CD8-dependent durable regression — PMIDs 36824971, 37782788, 38727236]
        │  [UNTESTED clinically for daraxonrasib + ICB]
        ▼
 Deeper / more durable clinical responses
        │  [daraxonrasib MONOTHERAPY OS benefit proven — PMID 42223072]
        │  [daraxonrasib + ICB: NO clinical data]
        ▼
 Improved survival in mPDAC patients
```

**Interpretation.** The backbone — KRAS output → immunosuppressive TME → reversibility by RAS-pathway inhibition → CD8-dependent ICB synergy — is robustly supported in preclinical PDAC. The hypothesis is thus mechanistically sound as a *class* statement about RAS-pathway inhibition. The distinctive, curation-relevant weaknesses are three: (1) the agent gap (daraxonrasib's immune data are in NSCLC; PDAC immune data are MRTX1133's); (2) the durability problem (the window self-closes via CDK8/CXCL2 and iCAF/M2 rebound); and (3) two mis-attributed arms (antigen presentation is autophagy/FAK-owned; Treg relief is unsupported). The clinical keystone — daraxonrasib + ICB with immune contexture readout — is missing entirely.

---

## Evidence Matrix

| Citation (PMID) | Evidence type | Stance | Mechanistic claim tested | Key finding | Subtype / context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [41670434](https://pubmed.ncbi.nlm.nih.gov/41670434/) | Model organism (in vivo) | **Supports** | RAS(ON) doublet boosts antigen presentation + remodels TME + sensitizes to ICB | Daraxonrasib + elironrasib → immune-dependent complete regressions; ICB sensitization | KRAS-G12C **NSCLC** | High for mechanism; **wrong disease** (NSCLC not PDAC) |
| [37782788](https://pubmed.ncbi.nlm.nih.gov/37782788/) | Model organism | **Supports** | KRAS activity governs immune composition; KRAS/MEK-i + ICB → durable regression | Mono-inhibition promotes infiltration but limited effect; ICB combo needed | PDAC | High; preclinical only |
| [37625401](https://pubmed.ncbi.nlm.nih.gov/37625401/) | Model organism (16 models) | **Supports** | KRAS-G12D-i reprograms TME | ↑CD8 effectors, ↓myeloid, CAF reprogramming | KRAS-G12D PDAC | High; MRTX1133 (not daraxonrasib) |
| [36824971](https://pubmed.ncbi.nlm.nih.gov/36824971/) | Model organism | **Supports** | KRAS-G12D-i + ICB eradicates PDAC via CD8/FAS | Regression requires CD8; MRTX1133 induces tumor FAS; iCBT synergy | KRAS-G12D PDAC | High; MRTX1133; preclinical |
| [38727236](https://pubmed.ncbi.nlm.nih.gov/38727236/) | Model organism (scRNA-seq) | **Qualifies** | RAS-pathway-i triggers counter-regulatory suppression | SOS1i+MEKi → ↑CD8 but no cure; IL6+ iCAF/M2 rebound; CD40+ICB → cures | KPCY PDAC | High; shows rebound limits durability |
| [42436354](https://pubmed.ncbi.nlm.nih.gov/42436354/) | Model organism (spatial multi-omics) | **Qualifies** | Immune remodeling is transient; CDK8 drives reversal | Long-term MRTX1133 reverses immune gains via CDK8→CXCL2, FAS suppression | KRAS-G12D PDAC; names daraxonrasib | High; durability caveat |
| [42392864](https://pubmed.ncbi.nlm.nih.gov/42392864/) | Human + model organism | **Supports** | KRAS-G12D → cholesterol metabolism → CD8 exhaustion; reversible | USP20 metabolic checkpoint modulates KRAS-i efficacy | Human PDAC + mouse/PDX | Moderate-high; human tissue anchored |
| [42223072](https://pubmed.ncbi.nlm.nih.gov/42223072/) | **Human clinical (phase 3)** | **Supports (context)** | RAS(ON) inhibition benefits mPDAC | Daraxonrasib > chemo for OS and PFS (n=500) | Previously treated mPDAC | High for survival; **no immune readout, no ICB arm** |
| [42226659](https://pubmed.ncbi.nlm.nih.gov/42226659/) | Human clinical (report) | **Supports (context)** | Daraxonrasib survival magnitude | "Unprecedented doubling of OS" vs chemo | mPDAC | Corroborates 42223072 |
| [32376951](https://pubmed.ncbi.nlm.nih.gov/32376951/) / [32459143](https://pubmed.ncbi.nlm.nih.gov/32459143/) | In vitro + model organism | **Competing** | Antigen presentation is autophagy-controlled | NBR1 selective autophagy degrades MHC-I; inhibition restores it + ICB sensitivity | PDAC | High; RAS-independent axis |
| [36977556](https://pubmed.ncbi.nlm.nih.gov/36977556/) | In vitro + model organism | **Competing** | Antigen presentation is FAK-controlled | FAK loss ↑immunoproteasome/MHC-I, antigen diversity; +STAT3 loss → CD8 infiltration | Mouse + human PDAC | High; RAS-independent axis |
| [33786412](https://pubmed.ncbi.nlm.nih.gov/33786412/) | Human clinical (phase 2) | **Neutral / absence flag** | RAS-directed vaccine (not inhibitor) | Adjuvant GI-4000 RAS-peptide yeast vaccine; not a RAS-i, not Treg-relief evidence | Resected PDAC | Only RAS-Treg-adjacent hit found |
| [42465401](https://pubmed.ncbi.nlm.nih.gov/42465401/) | Model organism | **Qualifies** | Daraxonrasib resistance is allele-specific | Adaptive resistance routes differ by KRAS allele (e.g., CypA downregulation) | PDAC | Relevant to durability/salvage |
| [41329731](https://pubmed.ncbi.nlm.nih.gov/41329731/) | Model organism (GEMM + PDX) | **Supports (combination)** | Multi-node KRAS-network blockade prevents resistance | Daraxonrasib + afatinib (EGFR) + SD36 (STAT3) → complete regression, no relapse >200d | KRAS/TP53 PDAC | High; non-immune combination strategy |

---

## Alternative and Competing Models

1. **Antigen-presentation is autophagy/FAK-governed, not RAS-governed (competing / parallel).** MHC-I surface levels in PDAC are set principally by NBR1-mediated selective autophagy (PMIDs 32376951/32459143) and by FAK-driven immunoproteasome suppression (PMID 36977556), plus multiple ubiquitin/autolysosome nodes (USP18, OASL, ITGB4/BNIP3, PARP11). These operate largely in parallel to RAS-MAPK output. This is the strongest competitor to the hypothesis's antigen-presentation arm and better explains why MHC-I is low in PDAC.

2. **Myeloid/chemokine circuits as the dominant suppressive axis (parallel / downstream).** CCR1+ myeloid cells (PMID 42207977) and CXCR2+ tumor-associated neutrophils in ARID1A-deficient PDAC (PMID 42479087) sustain immunosuppression and can be targeted to sensitize to ICB independently of RAS inhibition. The CDK8→CXCL2 rebound (PMID 42436354) suggests myeloid chemokine programs, not RAS per se, are the durable gatekeepers.

3. **Counter-regulatory stromal rebound requires an additional myeloid-activating hit (qualifying / downstream).** PMID 38727236 shows RAS-pathway inhibition alone drives an IL6+ iCAF/M2 rebound; durable cures needed CD40 agonism + ICB. This reframes RAS inhibition as necessary-but-insufficient conditioning.

4. **Metabolic reprogramming → T-cell exhaustion (complementary / downstream-of-KRAS).** The KRAS→cholesterol→CD8-exhaustion/USP20 axis (PMID 42392864) is a complementary mechanism that is downstream of KRAS but acts through metabolism rather than direct immune-cell recruitment.

5. **Non-immune combination targeting of the KRAS network (alternative therapeutic model).** Daraxonrasib + EGFR (afatinib) + STAT3 (SD36) produced durable regressions with no immune combination at all (PMID 41329731), indicating durable benefit can be engineered without ICB — a competing therapeutic strategy to the immune-remodeling route.

---

## Limitations and Knowledge Gaps

| # | Gap | Scope | Why it matters | What was checked | What would resolve it |
|---|---|---|---|---|---|
| KG1 | **Daraxonrasib + ICB clinical data absent** | Clinical, PDAC | The pivotal prediction of the hypothesis | RASolute 302 (PMID 42223072) is monotherapy; no ICB arm | Randomized daraxonrasib ± anti-PD-1/PD-L1 trial with paired on-treatment biopsies |
| KG2 | **Agent gap: daraxonrasib immune-remodeling in PDAC unmeasured** | Preclinical, PDAC | Immune data are MRTX1133 (G12D) or daraxonrasib-in-NSCLC | PMIDs 37625401, 36824971 (MRTX1133); 41670434 (NSCLC) | Immune-competent PDAC GEMM treated with daraxonrasib + scRNA-seq/spatial immune profiling |
| KG3 | **Treg-relief edge unsupported** | Mechanistic, PDAC | Named arm of hypothesis has no primary support (F9) | Targeted PubMed searches; only GI-4000 vaccine (PMID 33786412) found | FACS/scTCR of Treg fraction and function before/after daraxonrasib in PDAC models and patients |
| KG4 | **Antigen-presentation arm mis-attributed** | Mechanistic, PDAC | MHC-I restoration is autophagy/FAK-driven, not RAS-owned | PMIDs 32376951, 36977556 (competing); no RAS→MHC-I direct evidence | Test whether daraxonrasib restores surface MHC-I independent of autophagy/FAK inhibition |
| KG5 | **Durability: adaptive reversal** | Mechanistic/therapeutic | Immune window self-closes via CDK8→CXCL2 and iCAF/M2 rebound | PMIDs 42436354, 38727236 | Test daraxonrasib + CDK8-i (or +CD40 agonist) + ICB for sustained immune contexture |
| KG6 | **Human on-treatment immune contexture data absent** | Clinical/translational | Mechanism is inferred, never measured in patients | RASolute 302 reports survival, not immune readout | Serial biopsies / multiplex IHC / spatial in daraxonrasib-treated patients |
| KG7 | **Allele-specificity of immune response** | Mechanistic | Immune architecture may differ by KRAS allele (G12D vs G12R vs G12C) | Review-level signal only (PMID 42226008) | Allele-stratified immune profiling under multiselective vs allele-selective inhibition |

---

## Discriminating Tests

1. **Daraxonrasib ± anti-PD-1 randomized trial with paired biopsies (definitive clinical test of KG1/KG6).** Stratify by KRAS allele and baseline CD8/myeloid contexture. Sample: pre-treatment and on-treatment (week 3-6) tumor biopsies. Readouts: multiplex IHC / CODEX (CD8, FoxP3 Tregs, CD11c DCs, CD68/CD206 M2, MHC-I), scRNA-seq. **Expected if hypothesis true:** combination yields deeper/more durable responses with on-treatment ↑CD8, ↓myeloid, and MHC-I restoration versus monotherapy.

2. **Daraxonrasib in an immune-competent KRAS-G12D/G12C PDAC GEMM with agent-matched comparison to MRTX1133 (resolves KG2).** Readout the same immune panel head-to-head. **Expected if hypothesis true:** daraxonrasib reproduces the MRTX1133 immune-remodeling signature (↑CD8, ↓myeloid, CAF reprogramming, tumor FAS) in PDAC.

3. **Treg-specific perturbation (resolves KG3).** Flow + scTCR quantify Treg fraction/suppressive function before/after daraxonrasib; compare with Treg depletion (anti-CD25 / FoxP3-DTR). **Expected if the Treg edge is real:** daraxonrasib reduces intratumoral Treg dominance; if not, the edge should be removed from the KB.

4. **Antigen-presentation ownership test (resolves KG4).** In PDAC lines, measure surface MHC-I after daraxonrasib alone, autophagy inhibition alone, FAK inhibition alone, and combinations. **Expected:** if MHC-I restoration requires autophagy/FAK inhibition and daraxonrasib adds little, the antigen-presentation arm belongs to the competing model.

5. **Durability rescue combination (resolves KG5).** Daraxonrasib + CDK8 inhibitor (or + CD40 agonist) + ICB versus daraxonrasib + ICB. **Expected if CDK8/CXCL2 reversal is causal:** CDK8-i/CD40 sustains the immune window and improves durable regression.

---

## Curation Leads (require curator verification)

**Candidate status:** Keep hypothesis **EMERGING**; do not upgrade to ESTABLISHED. Central preclinical chain is strong, but the daraxonrasib-specific PDAC immune data and the clinical ICB-combination keystone are absent.

**Candidate evidence references + snippets to verify:**
- PMID 41670434 — "the RAS(ON) inhibitor doublet enhances tumor immune recognition by boosting antigen presentation and remodeling the suppressive tumor microenvironment, thus promoting immune-dependent complete regressions and sensitization of an immunorefractory model to checkpoint blockade" (label: NSCLC context).
- PMID 37782788 — "combining KRAS/MEK inhibition with immune checkpoint blockade achieves durable regression in preclinical models."
- PMID 36824971 — "Regression of advanced PDAC requires CD8 + T cells and immune checkpoint blockade therapy (iCBT) synergizes with MRTX1133 to eradicate PDAC and prolong overall survival."
- PMID 38727236 — "increase in inflammatory cancer-associated fibroblasts (iCAF), M2 macrophages, and a decreased dendritic cell (DC) quality... driven by IL6+ iCAFs" and "The addition of checkpoint blockade to SOS1i+MEKi combination resulted in tumor-free mice with established immune memory."
- PMID 42436354 — "long-term treatment results in reversal of the immune responses leading to resistance promoted by multiprotein mediator complex associated kinase CDK8."
- PMID 42223072 — "treatment with daraxonrasib led to significantly longer overall survival and progression-free survival than chemotherapy."

**Candidate pathophysiology nodes/edges:**
- ADD edge: KRAS-MAPK output → myeloid/MDSC infiltration (relieved by RAS-i) — STRONG.
- ADD edge: KRAS-G12D-i → tumor-cell FAS induction → CD8-mediated killing — STRONG.
- ADD node: CDK8 → CXCL2 → adaptive immune reversal (resistance node) — STRONG (durability caveat).
- ADD node: USP20 metabolic checkpoint (cholesterol → CD8 exhaustion) — MODERATE.
- FLAG edge: RAS-i → increased antigen presentation — WEAK/competing (autophagy-NBR1 & FAK own this).
- FLAG edge: RAS-i → relief of Treg dominance — UNSUPPORTED (source absence).

**Candidate ontology terms:** CD8+ effector T cell; regulatory T cell (FoxP3+); myeloid-derived suppressor cell; M2 tumor-associated macrophage; inflammatory cancer-associated fibroblast (iCAF); conventional dendritic cell; MHC class I antigen presentation; selective autophagy; FAS/FASLG-mediated apoptosis; RAS-MAPK signaling; CDK8/Mediator kinase module.

**Candidate subtype restrictions:** Immune-remodeling evidence strongest in **KRAS-G12D** PDAC (MRTX1133 models); daraxonrasib multiselective immune data are **NSCLC/G12C**. Note allele-specificity (G12D vs G12R immune architecture) as an open modifier.

**Candidate `knowledge_gaps` / discussion prompts:** (1) No daraxonrasib + ICB clinical or PDAC immune-profiling data. (2) Treg-relief edge unsupported by primary literature. (3) Antigen-presentation arm attributable to autophagy/FAK, not RAS. (4) Immune remodeling transient/self-reversing via CDK8→CXCL2 and iCAF/M2 rebound. (5) Human on-treatment immune contexture never measured for daraxonrasib.

---

## Evidence Base (summary of key papers)

- **PMID 42223072 / 42226659** — Phase 3 RASolute 302: daraxonrasib monotherapy OS/PFS benefit in mPDAC. Establishes clinical relevance of the agent; provides no immune readout.
- **PMID 41670434** — RAS(ON) doublet (daraxonrasib + elironrasib) primes immune-refractory KRAS-G12C NSCLC for ICB. Strongest daraxonrasib-specific mechanistic support; wrong disease.
- **PMID 37625401 / 36824971** — MRTX1133 (KRAS-G12D-i) reprograms PDAC TME, induces tumor FAS, and synergizes with ICB in a CD8-dependent manner. Strongest PDAC-specific support; allele-selective agent.
- **PMID 37782788** — KRAS activity governs immune composition; ICB combination needed for durable regression. Core prediction confirmed preclinically.
- **PMID 38727236** — SOS1i+MEKi triggers IL6+ iCAF/M2 counter-regulatory suppression; CD40 + ICB needed for cures. Key qualifier.
- **PMID 42436354** — CDK8→CXCL2 drives adaptive reversal of KRAS-i immune remodeling (names daraxonrasib). Durability qualifier.
- **PMID 42392864** — Human PDAC KRAS→cholesterol→CD8-exhaustion/USP20 axis, reversible by KRAS-i. Human-tissue mechanistic anchor.
- **PMID 32376951 / 32459143 / 36977556** — Autophagy (NBR1) and FAK govern MHC-I / antigen presentation in PDAC. Competing mechanism for the antigen-presentation arm.
- **PMID 41329731** — Daraxonrasib + EGFR-i + STAT3-i achieves durable non-relapsing regression without ICB. Competing non-immune combination model.
- **PMID 42465401** — Allele-specific daraxonrasib resistance routes. Durability/salvage relevance.
- **PMID 33786412** — GI-4000 adjuvant RAS-peptide vaccine; only RAS-Treg-adjacent hit; not RAS-inhibitor Treg evidence.

---

## Proposed Follow-up Actions

1. **Prioritize the daraxonrasib + ICB clinical question** (KG1/KG6) — the single highest-value experiment; design with mandatory paired on-treatment biopsies and a pre-specified immune-contexture pharmacodynamic endpoint.
2. **Run an agent-matched daraxonrasib-vs-MRTX1133 immune-profiling study in PDAC GEMMs** (KG2) to close the agent gap and confirm daraxonrasib reproduces the immune-remodeling signature in PDAC.
3. **Explicitly test the Treg edge** (KG3); if unsupported, remove it from the hypothesis or reclassify as speculative.
4. **Resolve antigen-presentation ownership** (KG4) with a factorial daraxonrasib × autophagy-i × FAK-i MHC-I assay.
5. **Test durability-rescue combinations** (daraxonrasib + CDK8-i/CD40 + ICB) (KG5) to convert the transient window into durable benefit.
6. **Stratify all future work by KRAS allele** to capture allele-specific immune architecture (KG7).

---

*Report generated by OpenScientist autonomous discovery agent. All claims are attributed to the primary literature via PMID and verified against provided abstract snippets. Verdict: PARTIALLY SUPPORTED.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)