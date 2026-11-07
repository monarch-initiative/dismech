---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-05T19:59:57.113420'
end_time: '2026-11-05T20:15:42.162110'
duration_seconds: 945.05
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
  focus: 'Consider any part of the disease: its immune, epithelial, genetic, or neoplastic
    features.'
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
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 12
  quotes_valid: 12
  relevance_assessed: 22
  on_topic: 8
  validator_version: 0.5.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: blind-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: blind-openscientist_artifacts/final_report.pdf
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

Consider any part of the disease: its immune, epithelial, genetic, or neoplastic features.

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

# Missing Mechanistic Driver Genes in Sjögren's Syndrome

**Disease:** Sjögren's Syndrome (MONDO:0010030)
**Objective:** Identify gene-level mechanistic hypotheses absent from the curated account, rank-ordered by strength of human genetic and mechanistic evidence.

---

## Summary

The curated Sjögren's syndrome (SS) account captures the disease's canonical axes — exocrine gland lymphocytic infiltration, anti-Ro/La autoantibodies, the type I interferon (IFN) signature, epithelial dysfunction, salivary JAK-STAT/ISG activation, B-cell lymphomagenesis, and the HLA-DR3/DQ2/IRF5/STAT4 risk loci. This investigation identifies **ten additional driver genes** that are not in that curated set but which carry human genetic evidence, functional validation, and/or model-system support. Each adds a mechanistically distinct piece of the disease, and each implies a concrete therapeutic direction.

The three strongest hypotheses rest on either large-effect or dual (germline + somatic) human genetics. **TNFAIP3/A20** ties a germline NF-κB risk locus to somatic 6q23 deletion in salivary-gland MALT lymphoma — a true two-hit chain from risk allele to neoplasm. **GTF2I** is the largest non-HLA risk locus known in SS (rs117026326, OR ≈ 2.2, P = 1.3×10⁻⁵³ in Han Chinese, independently replicated). **NCR3/NKp30** carries a functionally-validated protective promoter variant (rs11575837) that lowers receptor transcription and defines an NK-cell/type-II-IFN axis acting against epithelial B7H6. The next tier — **TNFSF13B/BAFF** (defined causal BAFF-var variant; transgenic over-expression reproduces sialadenitis), **TLR7** (duct and plasmacytoid dendritic cell over-signaling feeding the IFN loop and the female bias), **IKZF1/IKAROS** (meta-GWAS P = 4×10⁻⁸), and **IL12B/IL-12p40** (Mendelian-randomization-supported, ustekinumab-targetable) — carries solid but more moderate genetic support. The final tier — **LAMP3**, **CXCL13**, and **CHRM3** — is expression- or autoantibody-based but mechanistically specific, explaining dryness, ectopic germinal centers, and non-destructive secretory failure respectively.

Throughout, I separate **established findings** (reported in the cited literature) from my own **inference** (the causal-chain synthesis connecting them). The genetic associations, somatic lesions, model phenotypes, and in vitro effects are established; the step-by-step attribution of each gene to specific clinical features, and the ranking, are my inference built on those facts.

---

## Key Findings (Ranked Hypotheses)

### Hypothesis 1 — TNFAIP3 / A20: germline NF-κB risk meets somatic lymphoma driver

**Gene & molecular function.** *TNFAIP3* encodes A20, a ubiquitin-editing enzyme that is a negative regulator (inhibitor) of NF-κB signaling. (Established.)

**Human genetic evidence.** *Germline:* a Han Chinese pSS GWAS confirmed the European TNFAIP3 association ([PMID: 24097066](https://pubmed.ncbi.nlm.nih.gov/24097066/)). *Somatic:* A20 is the target of 6q23.3 deletion in MALT lymphoma. High-resolution chromosome-6 array-CGH "*identified NF-kappaB inhibitor A20 as the target of 6q23.3 deletion*," and "*A20 deletion occurred in MALT lymphoma of the ocular adnexa (8/42=19%), salivary gland (2/24=8%), thyroid (1/9=11%)*," exclusively in translocation-negative cases and predicting shorter relapse-free survival ([PMID: 19006194](https://pubmed.ncbi.nlm.nih.gov/19006194/)). Premature stop codons in *TNFAIP3* are also seen in ocular adnexal marginal-zone lymphoma ([PMID: 22382892](https://pubmed.ncbi.nlm.nih.gov/22382892/)). (Established.)

**Causal chain (inference built on established facts).** Germline A20 hypofunction lowers the NF-κB inhibition threshold in B cells → chronic antigenic/BAFF stimulation in the salivary gland sustains a clonal marginal-zone B-cell population → somatic 6q23.3 deletion removes the remaining A20 allele → unrestrained NF-κB drives the transition to salivary-gland MALT lymphoma, the neoplastic complication of SS. The cell type at each step is the gland-resident (marginal-zone) B cell.

**Model-system evidence.** The salivary/ocular MALT lesions documented above are the human in-situ evidence; array-CGH and sequencing define the somatic lesion. (A dedicated A20-conditional SS mouse was not identified in this investigation — a gap.)

**Therapeutic direction.** Because the defect is loss of an NF-κB brake, act **downstream**: inhibit NF-κB-activating signaling (e.g., BTK inhibition) in A20-deficient clones rather than attempting to restore A20.

### Hypothesis 2 — GTF2I: the largest non-HLA risk locus

**Gene & molecular function.** *GTF2I* (7q11.23) encodes General Transcription Factor II-I (TFII-I), a transcription factor. (Established.)

**Human genetic evidence.** A three-stage GWAS in Han Chinese (542 cases/1,050 controls discovery; +1,303 cases/2,727 controls replication) found that "*the combined analysis identified GTF2I at 7q11.23 (rs117026326: Pcombined = 1.31 × 10(-53), combined odds ratio (ORcombined) = 2.20) as a new susceptibility locus for primary Sjögren's syndrome*" ([PMID: 24097066](https://pubmed.ncbi.nlm.nih.gov/24097066/)). An independent Taiwanese female cohort replicated it: "*We identified rs117026326 on GTF2I with GWAS significance*" ([PMID: 27503288](https://pubmed.ncbi.nlm.nih.gov/27503288/)). The same allele is shared with SLE ([PMID: 26320362](https://pubmed.ncbi.nlm.nih.gov/26320362/)). The OR ≈ 2.2 exceeds that of most curated loci (IRF5/STAT4 ORs ≈ 1.2–1.5). (Established.)

**Causal chain (inference).** Risk-allele-altered TFII-I activity reshapes the transcriptional program of lymphocytes, lowering the threshold for autoimmune activation in the gland-infiltrating immune compartment; the shared SLE signal argues for a general humoral-autoimmunity mechanism rather than a gland-specific one.

**Model-system evidence.** None specific to SS was identified — the gene's mechanistic role in SS tissue is unresolved (a gap). The strength here is genetic magnitude and replication, not mechanism.

**Therapeutic direction.** Indirect; TFII-I is not readily druggable. Value is as a stratification biomarker and a pointer to the downstream lymphocyte programs it controls.

### Hypothesis 3 — NCR3 / NKp30: an NK-cell / type-II-IFN axis

**Gene & molecular function.** *NCR3* encodes NKp30, an activating natural-killer (NK) cell receptor. (Established.)

**Human genetic evidence.** In a multinational pSS consortium case-control study, promoter SNP "*rs11575837 (G>A) residing in the promoter was associated with reduced gene transcription and function as well as protection to pSS*" ([PMID: 23884468](https://pubmed.ncbi.nlm.nih.gov/23884468/)) — a functional, direction-of-effect-consistent variant. (Established.)

**Causal chain (established + inference).** Established: circulating NKp30 is increased in pSS and correlates with NKp30-dependent (not CD16-dependent) IFN-γ secretion by NK cells; "*excess accumulation of NK cells in minor salivary glands correlated with the severity of the exocrinopathy. B7H6, the ligand of NKp30, was expressed by salivary epithelial cells*" ([PMID: 23884468](https://pubmed.ncbi.nlm.nih.gov/23884468/)). Inference: stressed salivary epithelial cells display B7H6 → NKp30⁺ NK cells engage and secrete type-II IFN (IFN-γ) → epithelial injury and amplified inflammation → worse exocrinopathy. NKp30 is further upregulated in ectopic lymphoid structures and reduced by rituximab ([PMID: 34594326](https://pubmed.ncbi.nlm.nih.gov/34594326/)). The cell types: epithelial cell (B7H6) and NK cell (NKp30).

**Model-system evidence.** The human in-situ B7H6/NK correlation and the transcription-reporter effect of rs11575837 constitute the functional validation; no dedicated animal model was identified.

**Therapeutic direction.** **Decrease** NKp30/B7H6 engagement (block NKp30 or its ligand) — the protective allele lowers NKp30, so reducing its activity is predicted to be beneficial.

### Hypothesis 4 — TNFSF13B / BAFF: sufficient to produce sialadenitis

**Gene & molecular function.** *TNFSF13B* encodes BAFF/BLyS, a B-cell survival cytokine. (Established.)

**Human genetic evidence.** In Sardinian case-control samples, "*an insertion-deletion variant, GCTGT→A (in which A is the risk allele), yielded a shorter transcript that escaped microRNA inhibition and increased production of so[luble BAFF]*," and "*the disease-risk allele was also associated with up-regulated humoral immunity through increased levels of soluble BAFF, B lymphocytes, and immunoglobulins*" ([PMID: 28445677](https://pubmed.ncbi.nlm.nih.gov/28445677/)) — a defined causal germline mechanism across autoimmunity. (Established.)

**Causal chain (established).** Model evidence: "*BAFF Tg mice, as they age, develop a secondary pathology reminiscent of Sjögren's syndrome (SS), which is manifested by severe sialadenitis, decreased saliva production, and destruction of submaxillary glands*," and "*SS also correlates with elevated levels of circulating BAFF, as well as a dramatic upregulation of BAFF expression in inflamed salivary glands*" ([PMID: 11781351](https://pubmed.ncbi.nlm.nih.gov/11781351/)). The cellular requirement was isolated genetically: "*in contrast to old BAFF Tg mice, aging LTbetaDelta-BTg mice no longer developed sialadenitis*" — marginal-zone B cells are necessary for BAFF-driven gland disease, while nephritis persists ([PMID: 16906535](https://pubmed.ncbi.nlm.nih.gov/16906535/)).

**Model-system evidence.** BAFF-transgenic mouse reproduces sialadenitis, reduced saliva, and gland destruction (the hallmark exocrine features); LTβ-deficient BAFF-Tg dissociates sialadenitis (abolished) from nephritis (retained), proving the marginal-zone B-cell dependence.

**Therapeutic direction.** **Decrease** BAFF activity — belimumab (anti-BAFF) or ianalumab (anti-BAFF-R). Strong translational rationale.

### Hypothesis 5 — TLR7: duct/pDC over-signaling drives the IFN loop and female bias

**Gene & molecular function.** *TLR7* encodes Toll-like receptor 7, an X-linked endosomal RNA sensor upstream of type I IFN. (Established.)

**Human expression evidence.** In labial salivary glands, "*ducts from pSS patients dominantly expressed TLR-7, and TLR-7 in the ducts co-expressed with MyD88, TRAF6 and IRF7*," and TLR7 ligand drove TRAF6/IRF7 nuclear translocation and type I IFN in salivary epithelial cells ([PMID: 30446998](https://pubmed.ncbi.nlm.nih.gov/30446998/)). Plasmacytoid dendritic cells (pDCs) "*derived from pSS exhibited higher expression levels of Toll-like receptor 7 in the resting state*" ([PMID: 41328603](https://pubmed.ncbi.nlm.nih.gov/41328603/)). (Established; germline variant burden not established here — expression-level evidence.)

**Causal chain (inference built on established expression).** Endogenous RNA/immune-complex ligands over-stimulate TLR7 in ductal epithelium and pDCs → MyD88/TRAF6/IRF7 → type I IFN → feeds the curated IFN signature and ISG upregulation. X-linkage and TLR7 gene-dose plausibly contribute to the strong female predominance (inference).

**Model-system evidence.** In vitro: loxoribine-driven IFN in patient SGECs ([PMID: 30446998](https://pubmed.ncbi.nlm.nih.gov/30446998/)). Downstream TBK1 inhibition (BX795) reduces ISGs in pSS PBMCs ([PMID: 29673738](https://pubmed.ncbi.nlm.nih.gov/29673738/)).

**Therapeutic direction.** **Decrease** TLR7 signaling (TLR7 antagonists, or downstream TBK1/IRAK4 inhibition).

### Hypothesis 6 — IKZF1 / IKAROS: an independent susceptibility locus

**Gene & molecular function.** *IKZF1* "*encodes a transcription factor related to chromatin remodeling, regulates lymphocyte differentiation*" ([PMID: 28552951](https://pubmed.ncbi.nlm.nih.gov/28552951/)). (Established.)

**Human genetic evidence.** In 665 Han Chinese pSS cases vs 863 controls, "*rs4917129: P-value = 5.5e-4, OR (odds ratio) = 0.72, 95% CI (confidence interval) = 0.60-0.87*"; meta-analysis with prior GWAS reached rs4917129 Pmeta = 4.24×10⁻⁸ (OR 0.70) and rs4917014 Pmeta = 6.0×10⁻⁸ (OR 0.72). The SNPs lie in a putative immune-cell enhancer ([PMID: 28552951](https://pubmed.ncbi.nlm.nih.gov/28552951/)). (Established.)

**Causal chain (inference).** Enhancer variants alter IKAROS dosage → shifted lymphocyte differentiation/activation thresholds → predisposition to the gland-infiltrating autoimmune response.

**Model-system evidence.** None SS-specific identified (gap). Strength is genome-wide-significant meta-analytic association.

**Therapeutic direction.** Indirect; IKAROS is targetable pharmacologically (cereblon modulators) but SS-specific rationale is not yet established.

### Hypothesis 7 — IL12B / IL-12p40: Mendelian-randomization-supported, drug-targetable

**Gene & molecular function.** *IL12B* encodes the p40 subunit shared by IL-12 and IL-23, driving Th1/Th17 polarization. (Established.)

**Human genetic evidence.** Mendelian randomization with protein-QTL instruments (3,232 cases, 17,481 controls): "*there was a negative association between genetically predicted IL-12p40 (encoded by IL12B) and primary Sjögren's disease. In the two independent exposure datasets odds ratio (OR), 0.79 (95% CI 0.68-0.93; P-value = 0.004) and OR 0.86 (95% CI 0.78-0.95; P-value = 0.003) per S.D. decrease in genetically predicted IL-12p40*" — i.e., higher IL-12p40 raises risk ([PMID: 39222420](https://pubmed.ncbi.nlm.nih.gov/39222420/)). IL-12Rβ2 and IL-23R did not pass thresholds. This matters because classical pSS genetics mostly yields weak-effect loci: "*only a number of genes have been identified to be associated with SS, and these have only a weak or moderate effect*" ([PMID: 28476436](https://pubmed.ncbi.nlm.nih.gov/28476436/)). (Established.)

**Causal chain (inference).** Higher IL-12p40 → enhanced Th1 polarization and IFN-γ → amplified gland inflammation.

**Model-system evidence.** None SS-specific here; the MR provides human causal-inference evidence in lieu of a model.

**Therapeutic direction.** **Decrease** IL-12p40 — ustekinumab (anti-p40) is an existing, repurposable drug.

### Hypothesis 8 — LAMP3: lysosomal degradation of AQP5 as a direct epithelial cause of dryness

**Gene & molecular function.** *LAMP3* encodes a lysosome-associated membrane protein. (Established.)

**Evidence & causal chain (established).** "*Its ectopic expression in salivary gland epithelial cells (SGECs) is induced by type I interferon (IFN) signaling and is further amplified through Toll-like receptor 7 (TLR7) activation*," and "*this aberrant up-regulation disrupts glandular function by promoting endolysosomal degradation of aquaporin 5 (AQP5) and sodium-potassium-chloride cotransporter 1, leading to impaired fluid secretion and associated clinical sequelae (eg, dry mouth)*" ([PMID: 40757483](https://pubmed.ncbi.nlm.nih.gov/40757483/)). This directly connects the IFN/TLR7 loop (Hyp. 5) to the water channel and the cardinal symptom. Cell type: salivary gland epithelial cell. (Established mechanism; no germline genetics.)

**Therapeutic direction.** **Decrease** LAMP3 activity / protect AQP5 — act downstream of IFN/TLR7 to preserve the water channel and residual secretion.

### Hypothesis 9 — CXCL13: ectopic germinal centers bridging sialadenitis to lymphoma

**Gene & molecular function.** *CXCL13* (BCA-1) is a B-cell-attracting chemokine; its receptor is CXCR5. (Established.)

**Evidence (established).** "*BCA-1 (CXCL13) was expressed within lymphoid aggregates in SS, which shared many structural features with GCs in tonsil. BCA-1 (CXCL13) was completely absent in control biopsy samples from patients who did not have SS*" ([PMID: 11710719](https://pubmed.ncbi.nlm.nih.gov/11710719/)). In the UK Primary Sjögren's Registry (48 HC, 273 pSS without NHL, 38 with NHL), "*serum CXCL13 levels were higher in all pSS groups compared to controls (p < 0.0001), and in pSS-NHL+ compared to pSS-nonL patients (p = 0.0204)*" ([PMID: 32047959](https://pubmed.ncbi.nlm.nih.gov/32047959/)). Spatial data localize CXCL13/CXCR5 and Tfh signalling to focal infiltrates and GC-like structures ([PMID: 42303382](https://pubmed.ncbi.nlm.nih.gov/42303382/)).

**Causal chain (inference built on established expression).** Ectopic CXCL13 recruits CXCR5⁺ B cells and Tfh cells → ectopic germinal-center-like structures → clonal B-cell expansion → bridge to MALT lymphoma (quantitatively higher CXCL13 in lymphoma cases).

**Therapeutic direction.** **Decrease** CXCL13/CXCR5 signalling to disrupt ectopic GC formation; serum CXCL13 doubles as a lymphoma-risk biomarker.

### Hypothesis 10 — CHRM3: anti-M3R autoantibodies silence secretion without destroying the gland

**Gene & molecular function.** *CHRM3* encodes the M3 muscarinic acetylcholine receptor that drives cholinergic fluid secretion in gland epithelium. (Established.)

**Evidence (established).** "*Synthetic cyclic peptides M3RP(205-221) and M3RP(520-527) showed significantly high reactivity with pSS IgG compared to the control IgG*," and "*pSS IgG increased the interaction of membrane M3R with MHC I and induced their internalization in primary human submandibular gland cells*," an effect blocked by filipin ([PMID: 25784251](https://pubmed.ncbi.nlm.nih.gov/25784251/)).

**Causal chain (inference built on established in vitro data).** Functional anti-M3R autoantibodies bind the receptor on submandibular gland epithelial cells → drive M3R internalization/downregulation → block cholinergic fluid secretion → dryness **independent of glandular destruction**, explaining the frequent mismatch between symptom severity and histologic damage.

**Therapeutic direction.** Act **downstream** / increase residual signalling — muscarinic agonists (pilocarpine, cevimeline) stimulate remaining receptors; autoantibody removal/blockade is a longer-term direction.

---

## Mechanistic Model / Interpretation

The ten genes are not independent — they map onto four converging modules that together extend the curated account from "what the disease looks like" to "which molecular levers set it in motion."

```
                      ┌─────────────────────────────────────────────┐
   FEMALE BIAS  ◄─────┤  TLR7 (X-linked) over-signaling             │
                      │  in ducts + pDCs → type I IFN               │
                      └───────────────┬─────────────────────────────┘
                                      │ IFN / TLR7
                      ┌───────────────▼─────────────────────────────┐
  EPITHELIAL MODULE   │  LAMP3 induced → AQP5/NKCC1 degraded        │──► DRY MOUTH
                      │  CHRM3 autoantibodies → M3R internalized    │──► SECRETORY FAILURE
                      │  B7H6 displayed → NKp30(NCR3) NK engagement │──► IFN-γ, epithelial injury
                      └───────────────┬─────────────────────────────┘
                                      │ epithelial stress / antigen
                      ┌───────────────▼─────────────────────────────┐
  B-CELL / HUMORAL    │  BAFF(TNFSF13B) survival signal ↑           │
     MODULE           │  CXCL13 → ectopic germinal centers          │──► AUTOANTIBODIES
                      │  IL12B/Th1, GTF2I/IKZF1 lymphocyte programs │
                      └───────────────┬─────────────────────────────┘
                                      │ chronic clonal B-cell stimulation
                      ┌───────────────▼─────────────────────────────┐
  NEOPLASTIC MODULE   │  TNFAIP3/A20 germline hypofunction          │
                      │     + somatic 6q23 deletion (2nd hit)       │──► SALIVARY MALT LYMPHOMA
                      └─────────────────────────────────────────────┘
```

| Module | Genes | Clinical feature explained | Strongest evidence type |
|---|---|---|---|
| IFN amplifier | TLR7 | IFN signature, female bias | Human in-situ expression + in vitro |
| Epithelial effector | LAMP3, CHRM3, NCR3 | Dry mouth, secretory failure, exocrinopathy severity | In vitro + functional germline variant (NCR3) |
| B-cell / humoral | TNFSF13B, CXCL13, IL12B, GTF2I, IKZF1 | Autoantibodies, ectopic GCs, risk | GWAS, MR, causal variant, transgenic model |
| Neoplastic | TNFAIP3 | MALT lymphoma | Germline GWAS + somatic deletion |

**Why the ranking.** Tiering follows the strength and type of human evidence. Tier 1 (TNFAIP3, GTF2I, NCR3) has either dual germline+somatic genetics, the largest non-HLA effect size, or a functionally-validated variant. Tier 2 (TNFSF13B, TLR7, IKZF1, IL12B) has a defined causal variant with a reproducing model, genome-wide-significant meta-GWAS, or MR support. Tier 3 (LAMP3, CXCL13, CHRM3) lacks germline genetics but offers mechanistically specific, experimentally demonstrated routes to named clinical features.

| Rank | Gene | Genetics tier | Model/functional | Therapeutic direction |
|---|---|---|---|---|
| 1 | TNFAIP3/A20 | Germline GWAS + somatic deletion | Human MALT tissue | ↓ downstream NF-κB (BTK) |
| 2 | GTF2I | GWAS OR 2.2, replicated | None SS-specific | Biomarker/indirect |
| 3 | NCR3/NKp30 | Functional protective variant | In situ B7H6/NK | ↓ NKp30/B7H6 |
| 4 | TNFSF13B/BAFF | Causal BAFF-var variant | Transgenic mouse | ↓ BAFF (belimumab) |
| 5 | TLR7 | Expression only | In vitro IFN | ↓ TLR7 / TBK1 |
| 6 | IKZF1 | Meta-GWAS P=4×10⁻⁸ | None SS-specific | Indirect |
| 7 | IL12B | Mendelian randomization | None SS-specific | ↓ p40 (ustekinumab) |
| 8 | LAMP3 | Expression only | In vitro AQP5 | ↓ LAMP3 / protect AQP5 |
| 9 | CXCL13 | Serum/expression | In situ GCs | ↓ CXCL13/CXCR5 |
| 10 | CHRM3 | Autoantibody | In vitro M3R | ↑ residual (muscarinic agonist) |

---

## Evidence Base

| PMID | Role in this report | Gene(s) |
|---|---|---|
| [24097066](https://pubmed.ncbi.nlm.nih.gov/24097066/) | GWAS: GTF2I OR 2.2, P=1.3×10⁻⁵³; confirms TNFAIP3 | GTF2I, TNFAIP3 |
| [27503288](https://pubmed.ncbi.nlm.nih.gov/27503288/) | Independent replication of GTF2I | GTF2I |
| [26320362](https://pubmed.ncbi.nlm.nih.gov/26320362/) | GTF2I shared with SLE | GTF2I |
| [19006194](https://pubmed.ncbi.nlm.nih.gov/19006194/) | Somatic A20 deletion in salivary/ocular MALT | TNFAIP3 |
| [22382892](https://pubmed.ncbi.nlm.nih.gov/22382892/) | TNFAIP3 stop codons in marginal-zone lymphoma | TNFAIP3 |
| [23884468](https://pubmed.ncbi.nlm.nih.gov/23884468/) | NCR3 protective promoter variant; B7H6/NK axis | NCR3 |
| [34594326](https://pubmed.ncbi.nlm.nih.gov/34594326/) | NKp30 upregulated in ectopic lymphoid structures, reduced by rituximab | NCR3 |
| [11781351](https://pubmed.ncbi.nlm.nih.gov/11781351/) | BAFF-Tg sialadenitis; human BAFF upregulation | TNFSF13B |
| [16906535](https://pubmed.ncbi.nlm.nih.gov/16906535/) | MZ-B-cell requirement for BAFF-driven sialadenitis | TNFSF13B |
| [28445677](https://pubmed.ncbi.nlm.nih.gov/28445677/) | BAFF-var causal germline variant | TNFSF13B |
| [30446998](https://pubmed.ncbi.nlm.nih.gov/30446998/) | TLR7-dominant duct signaling → IFN | TLR7 |
| [41328603](https://pubmed.ncbi.nlm.nih.gov/41328603/) | Elevated resting TLR7 in pSS pDCs | TLR7 |
| [29673738](https://pubmed.ncbi.nlm.nih.gov/29673738/) | TBK1 inhibition reduces ISGs downstream | TLR7 (downstream) |
| [28552951](https://pubmed.ncbi.nlm.nih.gov/28552951/) | IKZF1 meta-GWAS P=4×10⁻⁸ | IKZF1 |
| [39222420](https://pubmed.ncbi.nlm.nih.gov/39222420/) | MR: IL-12p40 causal for pSS | IL12B |
| [28476436](https://pubmed.ncbi.nlm.nih.gov/28476436/) | Context: weak-effect classical SS loci | (context) |
| [40757483](https://pubmed.ncbi.nlm.nih.gov/40757483/) | LAMP3 → AQP5 degradation → dry mouth | LAMP3 |
| [11710719](https://pubmed.ncbi.nlm.nih.gov/11710719/) | CXCL13 disease-specific ectopic GCs | CXCL13 |
| [32047959](https://pubmed.ncbi.nlm.nih.gov/32047959/) | Serum CXCL13 tracks lymphoma risk | CXCL13 |
| [42303382](https://pubmed.ncbi.nlm.nih.gov/42303382/) | Spatial Tfh/CXCL13/CXCR5 in GC-like structures | CXCL13 |
| [25784251](https://pubmed.ncbi.nlm.nih.gov/25784251/) | Anti-M3R autoantibodies internalize M3R | CHRM3 |
| [39912633](https://pubmed.ncbi.nlm.nih.gov/39912633/) | Salivary MALT genetics (GPR34), broader context | (context) |

**How papers challenge/qualify findings.** The MALT-lymphoma review ([PMID: 39912633](https://pubmed.ncbi.nlm.nih.gov/39912633/)) notes that salivary-gland EMZL genesis may be closely tied to **GPR34** activation and lymphoepithelial-lesion paracrine stimulation — a reminder that A20 is one of several routes to salivary lymphoma, not the sole one. The ocular-adnexal series ([PMID: 22382892](https://pubmed.ncbi.nlm.nih.gov/22382892/)) shows A20 stop codons occur against biased VH4-34 usage, implying A20 loss cooperates with (rather than replaces) autoantigen-driven selection.

---

## Limitations and Knowledge Gaps

1. **Genetic ancestry skew.** GTF2I, IKZF1, and the core SS GWAS data derive largely from Han Chinese cohorts; TNFSF13B BAFF-var comes from Sardinians. Effect sizes may not transfer across ancestries, and few loci are validated in European or admixed SS cohorts for these specific genes.
2. **Expression ≠ causation for Tier 3.** LAMP3, CXCL13, and CHRM3 rest on in-situ expression, serum levels, or in vitro autoantibody effects — none has germline genetic anchoring in SS, so reverse causation (consequence of inflammation) cannot be excluded.
3. **Missing SS-specific animal models.** For TNFAIP3, GTF2I, NCR3, IKZF1, and IL12B, no dedicated gene-perturbation SS model was identified in this investigation. The causal chains for these are inference layered on human genetics + in vitro data, not demonstrated in vivo.
4. **TLR7 germline burden not quantified.** The TLR7 argument is expression/mechanism-based; a germline dose/variant association specific to SS (as exists for SLE) was not established here.
5. **MR assumptions.** The IL12B evidence depends on pQTL-instrument validity (no pleiotropy); IL12A instruments were too weak, so the p40 vs p35 attribution is partial.
6. **A20 two-hit timing.** The temporal order (germline hypofunction → clonal persistence → somatic deletion) is a plausible model, not a longitudinally demonstrated sequence in SS patients.

---

## Proposed Follow-up Experiments / Actions

1. **A20 two-hit test (highest priority).** Genotype germline *TNFAIP3* risk alleles in SS patients and sequence paired salivary-MALT lymphoma tissue for somatic 6q23.3 deletion; test whether germline carriers are enriched among those who acquire the somatic second hit and progress to lymphoma. Pair with a B-cell-conditional *Tnfaip3* knockout on an SS-prone background.
2. **NKp30/B7H6 blockade in ex vivo gland cultures.** Use patient minor-salivary-gland explants or SGEC–NK co-cultures to test whether anti-NKp30 or anti-B7H6 reduces IFN-γ and epithelial injury, validating the protective-allele direction.
3. **Trans-ancestry replication.** Genotype GTF2I (rs117026326), IKZF1 (rs4917129/rs4917014), and TNFSF13B BAFF-var in European and admixed SS cohorts to establish generalizability and refine effect sizes.
4. **LAMP3 → AQP5 rescue.** In IFN/TLR7-stimulated SGECs, knock down *LAMP3* or inhibit lysosomal degradation and quantify AQP5 membrane retention and fluid secretion — a direct test of the dryness mechanism and a drug-screen readout.
5. **Repurposing trials / biomarker stratification.** (a) Ustekinumab (anti-IL-12/23 p40) proof-of-concept in MR-predicted IL12B-high patients. (b) Prospective serum CXCL13 monitoring as a lymphoma-risk biomarker, integrated with the Fragkioudaki score. (c) TLR7-antagonist or TBK1/IRAK4-inhibitor trial in IFN-high endotype patients.
6. **Anti-M3R functional assay standardization.** Develop a validated functional anti-M3R internalization assay to stratify "autoantibody-driven secretory failure" patients who may respond better to muscarinic agonists than to immunosuppression.

---

*Established vs. inference, stated throughout:* All genetic associations, somatic lesions, transgenic/in-vitro phenotypes, and quoted statistics are **established** (cited). The module assignment, the step-by-step causal chains attributing each gene to a named clinical feature, and the rank ordering are my **inference** built on those established facts.


## Artifacts

- [OpenScientist final report](blind-openscientist_artifacts/final_report.html)
- [OpenScientist final report](blind-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 12 |
| Quoted claims found in source | 12 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 22 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.
