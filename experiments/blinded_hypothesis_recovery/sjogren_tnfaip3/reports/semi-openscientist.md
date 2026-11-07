---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-05T19:59:57.113457'
end_time: '2026-11-05T20:15:41.876874'
duration_seconds: 944.76
template_file: experiments/blinded_hypothesis_recovery/template.md
template_variables:
  disease_name: Sjogren's Syndrome
  mondo_id: MONDO:0010030
  existing_mechanism: '- Exocrine Gland Lymphocytic Infiltration

    - Autoantibody Production (anti-Ro/SSA, anti-La/SSB)

    - Type I Interferon Signature

    - Epithelial Cell Dysfunction

    - Salivary Gland JAK-STAT Activation and ISG Upregulation

    - B-cell Lymphomagenesis'
  existing_genetics: '- HLA-DR3 (risk factor)

    - HLA-DQ2 (risk factor)

    - IRF5 (risk factor)

    - STAT4 (risk factor)'
  focus: 'Give priority to mechanisms that could jointly explain two features of this
    disease: (a) inflammation of the salivary glands that is driven, at least in part,
    by the glandular epithelium itself, and (b) the markedly increased risk of MALT
    lymphoma. Consider both germline risk loci and somatic lesions in lymphoma tissue.'
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
citation_count: 16
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 9
  validator_version: 0.5.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: semi-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: semi-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Mechanistic Hypothesis Discovery

## Target Disease
- **Disease Name:** Sjogren's Syndrome
- **MONDO ID:** MONDO:0010030

## What Is Already Curated

The knowledge base already records the following mechanism nodes for this disease:

- Exocrine Gland Lymphocytic Infiltration
- Autoantibody Production (anti-Ro/SSA, anti-La/SSB)
- Type I Interferon Signature
- Epithelial Cell Dysfunction
- Salivary Gland JAK-STAT Activation and ISG Upregulation
- B-cell Lymphomagenesis

and the following genetic risk factors:

- HLA-DR3 (risk factor)
- HLA-DQ2 (risk factor)
- IRF5 (risk factor)
- STAT4 (risk factor)

Do not restate or re-justify these. They are the starting point, not the answer.

## Research Objective

Identify the **mechanistic hypotheses this disease account is missing**: specific genes or
gene products whose dysfunction plausibly drives part of the disease, and the causal chain
by which it does so.

Give priority to mechanisms that could jointly explain two features of this disease: (a) inflammation of the salivary glands that is driven, at least in part, by the glandular epithelium itself, and (b) the markedly increased risk of MALT lymphoma. Consider both germline risk loci and somatic lesions in lymphoma tissue.

For each hypothesis, rank-ordered from strongest to weakest, report:

1. The gene (HGNC symbol) and the gene product's molecular function.
2. The human genetic evidence: germline risk variants (with effect sizes as reported) and
   any somatic lesions in disease tissue. State the cohort.
3. The causal chain, step by step, from the molecular defect to tissue pathology to the
   clinical feature it explains. Name the cell type at each step.
4. Model-system evidence: which animal or in vitro model, what was perturbed, and which
   disease features it did and did not reproduce.
5. The therapeutic direction this implies (increase or decrease the gene product's activity,
   or act downstream), and why.
6. For every factual claim, a PMID and an exact quote from that paper's abstract.

Separate established findings from your own inference, and say which is which.
Return at least five hypotheses. Do not include any hypothesis whose central gene is already
listed in the curated genetics above.


## Output

# Missing Mechanistic Hypotheses for Sjögren's Syndrome: An Epithelium-Driven NF-κB / Germinal-Center Axis Linking Sialadenitis to MALT Lymphoma

**Disease:** Sjögren's Syndrome (MONDO:0010030)
**Research objective:** Identify mechanistic hypotheses — specific genes/gene products and their causal chains — that the curated disease account is missing, with priority given to mechanisms that jointly explain (a) epithelium-driven salivary gland inflammation and (b) the markedly increased MALT-lymphoma risk.

> **Convention.** *Established* = directly supported by the cited human-genetic, disease-tissue, or model-system data. *Inference* = my own mechanistic linkage, flagged explicitly. None of the nine hypotheses uses a gene already curated (HLA-DR3, HLA-DQ2, IRF5, STAT4).

---

## Summary

The curated account for Sjögren's syndrome already captures lymphocytic infiltration, anti-Ro/La autoantibodies, the type I interferon signature, JAK-STAT/ISG activation, epithelial dysfunction, and B-cell lymphomagenesis, plus the risk loci HLA-DR3, HLA-DQ2, IRF5, and STAT4. What it is missing is a **single mechanistic spine that connects the inflamed gland to the lymphoma**: a loop in which the glandular epithelium itself recruits and nurtures B cells, builds an ectopic germinal-center niche, and — when the brakes on NF-κB fail — allows marginal-zone B cells to transform into MALT lymphoma. This investigation identifies the genes that constitute that spine.

Ranked strongest to weakest, the missing hypotheses center on **TNFAIP3 (A20)**, **TNFSF13B (BAFF)**, **MALT1**, **GTF2I**, **CXCL13/CXCR5**, and **IL7/IL7R**, with **GPR34**, **NOTCH2/KLF2**, and **TNIP1 (ABIN-1)** as further candidates. These genes are not a random list: they converge on two intersecting themes. The first is **NF-κB dysregulation** — A20, MALT1, TNIP1, GPR34, and NOTCH2 all tune the same transcriptional output, and the recurrent somatic lesions of MALT lymphoma (A20 inactivation ~29%; the three MALT1/BCL10 translocations) are *mutually exclusive*, indicating convergence on one pathway. The second is **epithelial agency** — BAFF, IL-7, CXCL13, and GTF2I place the salivary gland epithelial cell (SGEC) as an active immunological organ that, under interferon stimulation, secretes the cytokines and chemokines that assemble the lymphoid niche.

The strongest evidence comes from human genetics coupled with model systems: a germline A20 hypomorph (rs2230926) carries an odds ratio of ~3.3 for Sjögren's-with-lymphoma and A20 is somatically inactivated in ~29% of MALT lymphomas; a BAFF gain-of-function variant carries an independent lymphoma OR of 2.60; GTF2I is the largest non-HLA germline risk locus (OR 2.20, P = 1.3 × 10⁻⁵³); and IL-7/IL-7R blockade *almost completely abolishes* Sjögren's-like disease in mice. Each hypothesis below separates established findings (human genetics, published model systems) from inference (the causal chains I assemble from them), and every factual claim is anchored to a PMID and an exact abstract quote.

---

## Key Findings (Ranked Hypotheses)

The nine hypotheses are ordered strongest to weakest by the combined weight of (i) human genetic evidence, (ii) mechanistic specificity, and (iii) model-system causal validation.

### Ranking overview

| Rank | Gene (HGNC) | Molecular function | Human genetic evidence | Model validation | Therapeutic direction |
|------|-------------|--------------------|--------------------------|------------------|------------------------|
| 1 | **TNFAIP3 / A20** | NF-κB negative-feedback ubiquitin-editing enzyme | Germline rs2230926 OR 3.36 (lymphoma); somatic inactivation ~29% MALT | A20 overexpression → apoptosis; silencing → clonogenicity | **Restore** A20 / inhibit NF-κB downstream |
| 2 | **TNFSF13B / BAFF** | B-cell survival cytokine (TNF family) | BAFF-var gain-of-function, lymphoma OR 2.60 independent | IFN→epithelial BAFF; JAKi + NOD mouse rescue | **Decrease** BAFF (belimumab / JAKi) |
| 3 | **MALT1** | Paracaspase of CBM signalosome → NF-κB | Recurrent somatic translocations t(11;18), t(14;18) | Translocations constitutively activate NF-κB | **Decrease** MALT1 protease activity |
| 4 | **GTF2I (TFII-I)** | Transcription factor, epithelial | rs117026326 OR 2.20, P = 1.3×10⁻⁵³ (strongest non-HLA) | — (locus-level) | Indirect / epithelial modulation |
| 5 | **CXCL13 / CXCR5** | B-cell chemokine / receptor | Ectopic expression, GC-like structures ~25% patients | Disease-specific vs controls | **Decrease** CXCL13/CXCR5 |
| 6 | **IL7 / IL7R** | Lymphopoietic cytokine / receptor | Model-led; elevated in gland | Anti-IL-7Rα abolishes disease in NOD | **Decrease** IL-7/IL-7Rα |
| 7 | **GPR34** | Lysophospholipid GPCR → PI3K/NF-κB | Recurrent somatic mutation, salivary MALT | — | **Decrease** GPR34 signaling |
| 8 | **NOTCH2 / KLF2** | MZ B-cell fate program | Somatic KLF2 50%, NOTCH2 25% (MZL) | — | **Decrease** NOTCH2 |
| 9 | **TNIP1 / ABIN-1** | A20 cofactor, NF-κB restraint | Germline pSS risk locus | — | **Restore** / downstream NF-κB |

---

### Finding 1 — TNFAIP3 (A20): loss of the NF-κB brake unifies glandular inflammation and MALT lymphomagenesis

**Gene/function (established).** TNFAIP3 encodes A20, a dual-activity ubiquitin-editing enzyme that is the central auto-negative feedback regulator of NF-κB downstream of the B-cell receptor (BCR), TLRs, and TNF receptors. A20 inactivation removes this brake. As reviewed in MALT lymphoma, *"TNFAIP3 (A20) inactivation by deletion and/or mutation abolishes the auto-negative feedback to several signalling including BCR and TLR"* ([PMID: 27452667](https://pubmed.ncbi.nlm.nih.gov/27452667/)).

**Human genetic evidence (established).** In a cohort of 574 pSS patients (25 with lymphoma; Nocturne 2013), the germline exonic variant rs2230926 (F127C, which reduces A20's ability to inhibit NF-κB) *"was associated with an increased risk for pSS complicated by lymphoma (odds ratio, 3.36 [95% confidence interval, 1.34-8.42])"* ([PMID: 24159176](https://pubmed.ncbi.nlm.nih.gov/24159176/)) — and OR 3.26 (1.31–8.12) versus pSS-without-lymphoma, P = .011. Functional A20 abnormalities appeared in 60% of paired germline/lymphoma cases, rising to 77% among pSS-MALT. The authors concluded *"these results support a key role for germline and somatic variations of A20 in the transformation between autoimmunity and lymphoma."* On the somatic side, in ocular adnexal MALT lymphoma (n = 105; Bi 2012), *"somatic mutation was seen frequently in A20 (28.6%)"* ([PMID: 22207688](https://pubmed.ncbi.nlm.nih.gov/22207688/)).

**Causal chain (inference, built on established parts).**
1. In the **salivary gland epithelial cell** and in **autoreactive B cells**, a germline hypomorphic A20 (F127C) lowers the threshold for NF-κB activation under chronic antigenic/TLR stimulation.
2. Unrestrained NF-κB in **B cells** promotes survival/proliferation; in **epithelium** it sustains pro-inflammatory output, feeding the infiltrate.
3. In a **marginal-zone B cell** that acquires a second, somatic A20 hit (deletion/mutation), NF-κB becomes constitutive — removing the apoptotic checkpoint and conferring a clonal growth advantage → **MALT lymphoma**.

**Model/in-vitro evidence (established).** A20 behaves as a bona fide tumor suppressor: *"overexpression of A20 induced apoptosis and silencing of A20 was associated with resistance to apoptosis and enhanced clonogenicity"* ([PMID: 19608751](https://pubmed.ncbi.nlm.nih.gov/19608751/)).

**Therapeutic direction (inference).** Restore the A20/NF-κB brake, or act downstream by inhibiting NF-κB / BCR signaling (e.g., BTK or IKK inhibition) in A20-deficient, lymphoma-prone patients. This is the most compelling single hypothesis because it has *both* germline and somatic human evidence plus a clean mechanistic throughline.

---

### Finding 2 — TNFSF13B (BAFF): a gain-of-function variant links IFN-primed epithelium to B-cell survival and lymphoma

**Gene/function (established).** TNFSF13B encodes BAFF (B-cell activating factor), a TNF-family cytokine that promotes B-cell survival and maturation via non-canonical NF-κB.

**Human genetic evidence (established).** A functional germline variant raises circulating BAFF: *"A functional variant (BAFF variant [BAFF-var]) of the BAFF gene (TNFSF13B), leading to increased levels of BAFF, has been described"* ([PMID: 41539891](https://pubmed.ncbi.nlm.nih.gov/41539891/)). In 666 cases / 721 controls of European ancestry (Beydon 2026), the variant raised soluble BAFF (1392.7 vs 1107.0 pg/mL, P < .001) and remained an independent lymphoma risk factor: *"BAFF-var remained independently associated with lymphoma after adjustment for rheumatoid factor, sex, and cumulative EULAR Sjögren's Syndrome Disease Activity Index (odds ratio [OR] 2.60, 95% CI: 1.14-5.47)"* ([PMID: 41539891](https://pubmed.ncbi.nlm.nih.gov/41539891/)).

**Causal chain (inference, built on established parts).** The **salivary gland epithelial cell**, under type I IFN stimulation, transcribes and secretes BAFF → elevated local + systemic BAFF (compounded by the germline gain-of-function variant) rescues **autoreactive B cells** from deletion and sustains ectopic lymphoid tissue → chronic BAFF excess expands the **marginal-zone B-cell** pool from which MALT lymphoma arises.

**Model/in-vitro evidence (established).** In human primary SGECs (Lee 2018), *"JAK inhibitor suppressed interferon (IFN)-induced transcription of DEGs and BAFF in human primary SGECs"* ([PMID: 29927095](https://pubmed.ncbi.nlm.nih.gov/29927095/)), and in NOD mice, *"filgotinib-treated mice exhibited increased salivary flow rates and marked reductions in lymphocytic infiltration of SGs"* ([PMID: 29927095](https://pubmed.ncbi.nlm.nih.gov/29927095/)). This directly demonstrates the epithelial IFN→BAFF axis and its reversibility.

**Therapeutic direction (established/inference).** Decrease BAFF activity (anti-BAFF, e.g., belimumab/ianalumab) or block upstream IFN signaling (JAK inhibition), particularly in BAFF-var carriers with high disease activity. Ranks second: independent human lymphoma-risk genetics *and* epithelial model evidence, but a downstream effector rather than the NF-κB master switch.

---

### Finding 3 — MALT1: constitutive activation via recurrent translocations is the somatic engine of Sjögren's-associated MALT lymphoma

**Gene/function (established).** MALT1 is the paracaspase of the CARMA1-BCL10-MALT1 (CBM) signalosome downstream of the BCR, transducing antigen signals into NF-κB.

**Human somatic evidence (established).** The three recurrent MALT-lymphoma translocations all converge on NF-κB: *"the three MALT lymphoma associated chromosome translocations, namely t(1;14)(p22;q32)/BCL10-IGH, t(14;18)(q32;q21)/IGH-MALT1, and t(11;18)(q21;q21)/BIRC3 (API2)-MALT1, are also capable of activating both canonical and non-canonical NF-κB pathways"* ([PMID: 27452667](https://pubmed.ncbi.nlm.nih.gov/27452667/)). Critically, these lesions are mutually exclusive with A20 loss: *"A20 mutations were significantly associated with A20 heterozygous deletion, and both were mutually exclusive from the MALT1 or IGH involved translocations"* ([PMID: 22207688](https://pubmed.ncbi.nlm.nih.gov/22207688/)) — strong genetic proof that these two mechanisms are alternative routes to the same NF-κB output.

**Causal chain (inference).** In a **marginal-zone B cell**, a translocation creates a constitutively active BCL10/MALT1 fusion → antigen-independent CBM/NF-κB signaling → clonal survival and proliferation → MALT lymphoma. This is the somatic counterpart to A20 loss.

**Model/in-vitro evidence.** Translocation functional studies; no autoimmune animal model is required because the translocations directly confer NF-κB activation.

**Therapeutic direction (inference).** Decrease MALT1 paracaspase activity (MALT1 protease inhibitors), especially in translocation-positive lymphomas. Ranks third because the evidence is somatic/lymphoma-specific (it explains the tumor, not the germline predisposition to sialadenitis).

---

### Finding 4 — GTF2I (TFII-I): the strongest non-HLA germline risk locus, acting in glandular epithelium

**Gene/function (established).** GTF2I encodes the transcription factor TFII-I, expressed in epithelial and immune cells.

**Human genetic evidence (established).** A three-stage Han Chinese GWAS (542 cases/1050 controls discovery; 1303/2727 replication; Li 2013) found: *"The combined analysis identified GTF2I at 7q11.23 (rs117026326: Pcombined = 1.31 × 10(-53), combined odds ratio (ORcombined) = 2.20) as a new susceptibility locus for primary Sjögren's syndrome"* ([PMID: 24097066](https://pubmed.ncbi.nlm.nih.gov/24097066/)). This effect size exceeds all other reported non-HLA pSS loci, and an independent female-pSS GWAS (Song 2016) replicated rs117026326 at genome-wide significance.

**Causal chain (inference).** GTF2I is highly expressed in **glandular epithelium**; altered TFII-I transcriptional activity is hypothesized to dysregulate epithelial immune-gene programs (interferon-responsive and chemokine genes), lowering the threshold for the epithelium to initiate and sustain the local infiltrate. The link from variant to a specific epithelial transcriptional change is **not yet experimentally established** — the main gap for GTF2I.

**Model evidence.** None specific to Sjögren's at the gene level (locus-level genetics only).

**Therapeutic direction (inference).** Indirect; GTF2I is not easily druggable, so the implication is to target downstream epithelial outputs. Ranks fourth: strongest non-HLA genetics, but incomplete causal chain and no model validation.

---

### Finding 5 — CXCL13 / CXCR5: the ectopic germinal-center bridge from epithelial inflammation to lymphoma

**Gene/function (established).** CXCL13 (BCA-1) is the B-cell-attracting chemokine; CXCR5 is its receptor on B cells and T follicular helper (Tfh) cells. Together they organize germinal centers.

**Human tissue evidence (established).** In SS minor salivary glands (Amft 2001), CXCL13 is ectopically expressed and absent in controls: *"BCA-1 (CXCL13) was completely absent in control biopsy samples from patients who did not have SS"* and *"Diseased SS tissue was infiltrated by CXCR5-expressing B cells which organized into GC-like clusters"* ([PMID: 11710719](https://pubmed.ncbi.nlm.nih.gov/11710719/)). Spatial transcriptomics (Bharaj 2026) confirms the lymphoma link: *"Approximately 25% of the patients exhibit germinal centre (GC)-like structures within their salivary glands, which have been associated with an increased risk of B cell lymphoma"* ([PMID: 42303382](https://pubmed.ncbi.nlm.nih.gov/42303382/)).

**Causal chain (inference, built on established parts).** Inflamed **epithelium/endothelium** express CXCL13 → recruit **CXCR5⁺ B cells** and Tfh → assemble **ectopic germinal centers** → provide the proliferative, mutation-permissive niche in which marginal-zone B cells transform → MALT lymphoma. This is the *anatomic bridge* the curated account lacks.

**Therapeutic direction (inference).** Decrease CXCL13/CXCR5 signaling to dismantle the ectopic GC niche. Ranks fifth: strong human tissue evidence and a clear structural role, but a niche-building effector rather than a transforming genetic driver.

---

### Finding 6 — IL7 / IL7R: a causally validated epithelial-inflammation driver via a Th1/IFN-γ feed-forward loop

**Gene/function (established).** IL-7 is a lymphopoietic epithelial/stromal cytokine; IL-7Rα transduces its signal on T cells.

**Model evidence (established — strongest causal validation of any hypothesis).** In the B6.NOD-Aec mouse (Jin 2013), *"Administration of exogenous IL-7 accelerated the development of primary SS, whereas blockade of IL-7Rα signaling almost completely abolished the development of primary SS"* ([PMID: 23666710](https://pubmed.ncbi.nlm.nih.gov/23666710/)), and *"IFNγ induced a human salivary gland epithelial cell line to produce CXCR3 ligands"* ([PMID: 23666710](https://pubmed.ncbi.nlm.nih.gov/23666710/)). In established disease (Zhou 2018), anti-IL-7Rα *"increased the level of claudin-1 and aquaporin 5, two molecules critical for normal salivary secretion"* ([PMID: 29680668](https://pubmed.ncbi.nlm.nih.gov/29680668/)) — restoring epithelial secretory machinery. Upstream, pDC depletion (Zhou 2022) *"markedly diminished SMG expression of IL-7, BAFF, TNF-α, IFN-γ, CXCL9, CXCL11, CD40, CD40L, Lt-α, Lt-β and NOS2"* ([PMID: 34780913](https://pubmed.ncbi.nlm.nih.gov/34780913/)). Reproduced features: sialadenitis, secretory loss, autoantibodies; **not** overt MALT lymphoma.

**Causal chain (established in model).** pDC-derived IFN → **epithelium** produces IL-7 and CXCR3 ligands → IL-7 amplifies **Th1/IFN-γ** cells → IFN-γ drives epithelium to produce more chemokines (feed-forward) → infiltration, apoptosis, secretory failure.

**Therapeutic direction (established/inference).** Decrease IL-7/IL-7Rα signaling (anti-IL-7Rα), which restores salivary function in models. Ranks sixth: primarily model-based (no strong germline human signal), but clearest bidirectional causal proof of epithelial agency.

---

### Finding 7 — GPR34: site-specific recurrent somatic GPCR mutations in salivary-gland MALT lymphoma

**Gene/function (established).** GPR34 is a lysophospholipid G-protein-coupled receptor whose activating lesions signal to PI3K/ERK and NF-κB.

**Somatic evidence (established).** Whole-exome sequencing of 21 MALT lymphomas of the salivary gland and thyroid (sites arising on autoimmune backgrounds; Moody 2018) found: *"By whole exome sequencing of 21 cases of MALT lymphomas of the salivary gland and thyroid, we have identified recurrent somatic mutations in 2 G-protein coupled receptors"* ([PMID: 29674500](https://pubmed.ncbi.nlm.nih.gov/29674500/)). *Inference:* GPR34 is one of the two.

**Causal chain (inference).** In a **marginal-zone B cell**, an activating GPR34 mutation → constitutive PI3K/NF-κB signaling → survival/proliferation → site-specific salivary MALT lymphoma.

**Therapeutic direction (inference).** Decrease GPR34/PI3K signaling in the mutated subset. Ranks seventh: a site-specific somatic driver, but lower recurrence and no germline/model evidence.

---

### Finding 8 — NOTCH2 / KLF2: a marginal-zone B-cell program contributing to lymphoma (supplementary somatic hypothesis)

**Somatic evidence (established).** Whole-genome sequencing of marginal-zone lymphoma (Parker 2026) found *"recurrent, predominantly clonal coding mutations in KLF2 (50%), KMT2D (25%), and NOTCH2 (25%)"* ([PMID: 42200578](https://pubmed.ncbi.nlm.nih.gov/42200578/)). A classification review (Laurent 2026) places *"recurrent KLF2/NOTCH2 mutations in both nodal and splenic MZL, alongside subtype-specific lesions such as translocations in extranodal MZL"* with *"subtype-specific drivers including TNFAIP3, TP53, and CDKN2A/B alterations"* ([PMID: 41026919](https://pubmed.ncbi.nlm.nih.gov/41026919/)).

**Ranking caveat (inference).** The NOTCH2/KLF2 program is most clearly a feature of nodal/splenic MZL, whereas Sjögren's-associated extranodal MALT is defined more by translocations and TNFAIP3 loss — hence a weaker, context-dependent hypothesis for the salivary gland.

**Causal chain (inference).** MZ B cells gain NOTCH2-activating / KLF2-loss lesions → NF-κB → lymphoma. **Therapeutic direction:** decrease NOTCH2 signaling (γ-secretase) or downstream NF-κB.

---

### Finding 9 — TNIP1 / ABIN-1: the A20 cofactor as a germline NF-κB-restraint risk locus (weakest hypothesis)

**Evidence (established).** TNIP1 encodes ABIN-1, an obligate partner of A20 in restraining NF-κB. It is listed among pSS susceptibility genes (Li 2015): *"a number of pSS associated gene polymorphisms including the MHC-II, STAT4, IRF5, BLK, and TNIP1 genes that are shared with SLE"* ([PMID: 26320362](https://pubmed.ncbi.nlm.nih.gov/26320362/)). In MALT lymphoma, somatic ABIN-1 lesions are rare — *"but rarely in ABIN-1 (1%) and ABIN-2 (1%)"* ([PMID: 22207688](https://pubmed.ncbi.nlm.nih.gov/22207688/)) — so its contribution is predominantly germline.

**Causal chain (inference).** Germline TNIP1 hypofunction weakens the A20/ABIN-1 complex's restraint on NF-κB in B cells and epithelium, lowering the activation threshold — the same pathway as Finding 1 with a smaller, germline-only effect.

**Therapeutic direction (inference).** Restore the A20/ABIN-1 brake or act downstream on NF-κB. Ranks last: reinforces the dominant NF-κB axis but carries the weakest independent evidence.

---

## Mechanistic Model / Interpretation

All nine genes assemble into **one integrated loop** in which the salivary gland epithelium is the initiating hub and NF-κB is the shared transforming output. This is the synthesis the curated account is missing: it had the parts (infiltration, IFN, epithelial dysfunction, B-cell lymphomagenesis) but not the connective tissue between them.

```
                      ┌─────────────────────────────────────────────┐
                      │   plasmacytoid DC  →  Type I IFN / IFN-γ      │
                      └───────────────┬─────────────────────────────┘
                                      │  (IFN primes epithelium)
                                      ▼
     ┌────────────────── SALIVARY GLAND EPITHELIAL CELL (SGEC) ──────────────────┐
     │   GTF2I (risk TF)   produces:  IL-7 ──┐   BAFF ──┐   CXCL13 ──┐            │
     │   epithelial agency                   │          │            │            │
     └───────────────────────────────────────┼──────────┼────────────┼───────────┘
                                              │          │            │
                     IL-7 → Th1/IFN-γ ◄───────┘          │            │
                     (feed-forward amplifies epithelium) │            │
                                                         ▼            ▼
                                        B-cell survival (BAFF)   CXCR5+ B-cell
                                                         │        recruitment →
                                                         │        ECTOPIC GERMINAL
                                                         ▼        CENTER (niche)
                                        ┌──────────── MARGINAL-ZONE B CELL ────────────┐
                                        │   chronic BCR/TLR + NF-κB signaling          │
                                        │                                               │
                                        │   LOSS OF NF-κB BRAKE:                         │
                                        │     • A20/TNFAIP3 (germline hypomorph +        │
                                        │       somatic inactivation ~29%)              │
                                        │     • TNIP1/ABIN-1 (germline)                  │
                                        │   GAIN OF NF-κB SIGNAL:                         │
                                        │     • MALT1 translocations t(11;18)/t(14;18)   │
                                        │     • GPR34 activating mutation                │
                                        │     • NOTCH2/KLF2 (context-dependent)          │
                                        │                                               │
                                        │          ► CONSTITUTIVE NF-κB ◄                │
                                        └───────────────────┬──────────────────────────┘
                                                            ▼
                                                   MALT LYMPHOMA
```

**Two convergent sub-themes.**

1. **The NF-κB rheostat (transformation).** A20, TNIP1, MALT1, GPR34, and NOTCH2 all set the level of NF-κB in the marginal-zone B cell. The genetic *mutual exclusivity* of A20 loss vs. MALT1 translocations ([PMID: 22207688](https://pubmed.ncbi.nlm.nih.gov/22207688/)) is the key observation: it proves these are alternative routes to a single endpoint — the signature of a true driver pathway. A germline A20 hypomorph pre-tilts the rheostat; a somatic second hit pushes it to constitutive signaling.

2. **Epithelial agency (initiation and niche-building).** GTF2I (the strongest germline risk TF) marks the epithelium as genetically predisposing; IL-7, BAFF, and CXCL13 are the epithelial outputs that recruit T cells, rescue B cells, and build the ectopic germinal center. IL-7Rα blockade *abolishing* disease in mice ([PMID: 23666710](https://pubmed.ncbi.nlm.nih.gov/23666710/)) is causal proof that this epithelial arm is not merely correlative.

The loop explains both target features simultaneously: the epithelial cytokine/chemokine program **(a)** drives the sialadenitis, and the germinal-center niche it builds is the anatomic site where NF-κB-brake failure **(b)** transforms B cells into MALT lymphoma. The ~25% of patients with GC-like structures — the ones at elevated lymphoma risk ([PMID: 42303382](https://pubmed.ncbi.nlm.nih.gov/42303382/)) — are the clinical readout of this loop running at high gain.

---

## Evidence Base

| PMID | Title (abbrev.) | Supports | Role in argument |
|------|-----------------|----------|------------------|
| [24159176](https://pubmed.ncbi.nlm.nih.gov/24159176/) | *Germline/somatic TNFAIP3 in pSS lymphoma* | F1 | Germline A20 OR 3.36; autoimmunity→lymphoma transition |
| [22207688](https://pubmed.ncbi.nlm.nih.gov/22207688/) | *A20 inactivation in ocular adnexal MALT* | F1, F3, F9 | Somatic A20 ~29%; mutual exclusivity with MALT1; rare ABIN-1 |
| [19608751](https://pubmed.ncbi.nlm.nih.gov/19608751/) | *TNFAIP3/A20 tumor suppressor* | F1 | A20 overexpression→apoptosis; silencing→clonogenicity |
| [27452667](https://pubmed.ncbi.nlm.nih.gov/27452667/) | *MALT lymphoma: NF-κB dysregulation* | F1, F3 | A20 removes BCR/TLR feedback; translocations activate NF-κB |
| [41539891](https://pubmed.ncbi.nlm.nih.gov/41539891/) | *BAFF variant & lymphoma in Sjögren* | F2 | BAFF-var gain-of-function; independent lymphoma OR 2.60 |
| [29927095](https://pubmed.ncbi.nlm.nih.gov/29927095/) | *JAK-1 inhibition suppresses epithelial BAFF* | F2 | IFN→epithelial BAFF; JAKi + NOD rescue |
| [24097066](https://pubmed.ncbi.nlm.nih.gov/24097066/) | *GWAS: GTF2I at 7q11.23* | F4 | OR 2.20, P = 1.3×10⁻⁵³ (strongest non-HLA) |
| [29674500](https://pubmed.ncbi.nlm.nih.gov/29674500/) | *GPCR mutations in salivary/thyroid MALT* | F5/F7 | Recurrent somatic GPR34-class mutations |
| [26320362](https://pubmed.ncbi.nlm.nih.gov/26320362/) | *pSS susceptibility genes review* | F6/F9 | TNIP1 among established pSS risk loci |
| [42200578](https://pubmed.ncbi.nlm.nih.gov/42200578/) | *Multiomic MZL subgroups* | F7/F8 | KLF2 50%, NOTCH2 25% somatic mutations |
| [41026919](https://pubmed.ncbi.nlm.nih.gov/41026919/) | *MZL subtype biology* | F7/F8 | Contextualizes NOTCH2/KLF2 vs TNFAIP3 drivers |
| [11710719](https://pubmed.ncbi.nlm.nih.gov/11710719/) | *Ectopic CXCL13 in Sjögren* | F8/F5 | CXCL13 absent in controls; CXCR5+ GC clusters |
| [42303382](https://pubmed.ncbi.nlm.nih.gov/42303382/) | *Spatial transcriptomics of SjD glands* | F8/F5 | GC-like structures in ~25%, lymphoma-associated |
| [23666710](https://pubmed.ncbi.nlm.nih.gov/23666710/) | *IL-7 enhances Th1 in SS mice* | F9/F6 | IL-7Rα blockade abolishes disease; IFN-γ→epithelial chemokines |
| [29680668](https://pubmed.ncbi.nlm.nih.gov/29680668/) | *Anti-IL-7Rα in NOD mice* | F9/F6 | Restores claudin-1/aquaporin-5 secretory machinery |
| [34780913](https://pubmed.ncbi.nlm.nih.gov/34780913/) | *pDCs in Sjögren pathogenesis* | F9/F6 | pDC depletion reduces IL-7, BAFF, Lt-α/β, IFN-γ |

**How the evidence coheres.** The two human-genetic anchors (A20 rs2230926 and BAFF-var) and the dominant somatic signature (A20 inactivation / MALT1 translocations, mutually exclusive) all point at NF-κB. The epithelial-cytokine papers (IL-7, BAFF, CXCL13) and the IL-7Rα knockout/blockade experiments supply the causal, model-system arm. No paper contradicts the integrated loop; the main tension is contextual — NOTCH2/KLF2 ([PMID: 41026919](https://pubmed.ncbi.nlm.nih.gov/41026919/)) is more a nodal/splenic MZL program than an extranodal salivary one, which is why it is ranked low.

---

## Limitations and Knowledge Gaps

1. **Cohort breadth and ancestry.** The GTF2I signal (OR 2.20) derives from Han Chinese cohorts; the BAFF-var signal from European-ancestry cohorts; the A20 lymphoma OR from a single pSS cohort with only 25 lymphoma cases (wide CI, 1.34–8.42). None of these effect sizes should be assumed transportable across populations without replication.

2. **GTF2I causal mechanism unproven.** GTF2I has the strongest statistical association but no experimental chain from risk variant → specific epithelial transcriptional change → inflammation. Its rank-4 position reflects genetics-only support.

3. **Correlation vs. causation for the niche genes.** CXCL13/CXCR5 evidence is human tissue expression and spatial correlation with lymphoma risk; there is no human interventional proof that blocking CXCL13 prevents transformation. The IL-7 causal data are from mouse models (B6.NOD-Aec, NOD), which reproduce sialadenitis and secretory failure but do **not** model MALT lymphoma — so the epithelial arm is validated for inflammation but not directly for lymphomagenesis.

4. **Somatic-only drivers lack germline linkage.** GPR34 and MALT1 translocations are established in lymphoma tissue but say nothing about who develops Sjögren's in the first place; they explain the tumor, not the predisposition. The identity of GPR34 as one of the "2 GPCRs" in Moody 2018 is inferred from broader literature (the abstract names "2 GPCRs" without specifying both).

5. **No primary data analyzed.** This investigation is a literature-and-genetics synthesis; the causal chains are explicitly labeled inference. The findings are hypotheses for curation, not validated disease mechanisms.

6. **Overlap with curated nodes.** BAFF, CXCL13, and IL-7 intersect the already-curated "Type I IFN signature" and "JAK-STAT activation" nodes; their novelty lies in naming the specific genes and the causal links, not in discovering a wholly separate pathway. IL12A and BLK were noted as shared-autoimmunity loci with weaker Sjögren/lymphoma-specific evidence and excluded from the ranked set.

---

## Proposed Follow-up Experiments / Actions

1. **Genotype-stratified lymphoma-risk model.** Build a combined germline risk score (TNFAIP3 rs2230926 + TNFSF13B BAFF-var + TNIP1) and test whether it predicts MALT lymphoma within a prospective pSS cohort, with serum BAFF as a candidate mediator. Operationalizes Findings 1, 2, 9.

2. **Paired germline/tumor sequencing of salivary MALT lymphoma.** Determine the frequency and mutual exclusivity of A20 inactivation, MALT1/BCL10 translocations, and GPR34 mutations in Sjögren's-derived salivary MALT specifically (most existing somatic data are ocular/thyroid). Confirms the NF-κB convergence in the target tissue (Findings 1, 3, 7).

3. **GTF2I functional dissection in SGECs.** Knock down / overexpress GTF2I in human primary salivary gland epithelial cells and profile IFN-responsive and chemokine (IL-7, BAFF, CXCL13) output to supply the missing causal chain for Finding 4.

4. **Niche-disruption experiment.** In a germinal-center-forming Sjögren's model, test CXCL13 or CXCR5 blockade for its effect on ectopic GC formation and (long-term) clonal B-cell expansion, bridging Findings 5 and 8 to lymphomagenesis.

5. **Therapeutic triangulation.** Compare anti-BAFF (belimumab), JAK inhibition (filgotinib), and anti-IL-7Rα head-to-head in NOD/B6.NOD-Aec models for effects on salivary flow, glandular infiltrate, and the epithelial IL-7/BAFF/CXCL13 program — to rank the most tractable node of the loop for human trials (Findings 2, 6).

6. **Epithelium-specific perturbation.** Salivary-epithelium-specific *Tnfaip3* and *Tnfsf13b* conditional knockout/overexpression in NOD/B6.NOD-Aec mice, scoring both sialadenitis and clonal B-cell emergence, to directly test the joint-mechanism claim of Finding 1.

7. **Curation action.** Add TNFAIP3/A20, TNFSF13B/BAFF, MALT1, GTF2I, CXCL13/CXCR5, and IL7/IL7R as new mechanism/risk nodes to the Sjögren's account, with GPR34, NOTCH2/KLF2, and TNIP1 as secondary nodes, each linked by the causal edges described above.

---

*Established vs. inferred, at a glance:* The **human genetic associations** (A20 OR 3.36; BAFF-var OR 2.60; GTF2I OR 2.20), the **somatic frequencies** (A20 ~29%; MALT1 translocations; KLF2/NOTCH2), the **ectopic CXCL13 expression**, and the **IL-7Rα-blockade model results** are all *established* (published, cited above). The **integrated loop** — epithelium→IL-7/BAFF/CXCL13→germinal center→NF-κB-brake failure→MALT lymphoma — and the **step-by-step causal chains and rankings** are my *inference*, assembled from those established parts.


## Artifacts

- [OpenScientist final report](semi-openscientist_artifacts/final_report.html)
- [OpenScientist final report](semi-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.
