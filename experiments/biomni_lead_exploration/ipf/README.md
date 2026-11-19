# Idiopathic pulmonary fibrosis: mechanism-led drug candidates

The second disease run with the method used for Sjögren's (`../sjogren/README.md`), chosen
because IPF is a Biomni Target Atlas disease with large unmet need and only two approved
antifibrotics, and because our entry is rich: 21 mechanism nodes. Done 2026-11-06.

## Method

1. `genes.tsv`: 22 genes. Some come from genes the dismech entry binds (TERT, MUC5B, CGAS,
   CPT1A). For nodes that name a pathway but bind no gene (IL-11 signalling, TGF-β, Wnt,
   senescent myofibroblast apoptosis resistance, macrophage recruitment) the obvious pathway
   genes were added. The rest are top genetic hits for IPF (`EFO_0000768`) in Open Targets
   (DSP, DPP9, AKAP13, FAM13A).
2. `../repurposing_candidates.py` with
   `--disease EFO_0000768 --pattern 'pulmonary fibrosis|\bIPF\b|interstitial lung'`.
   Output: `opentargets/candidates.tsv`. Our entry's `MONDO:0800504` is not in Open Targets.
3. Four candidates assessed by OpenScientist with `../repurposing_template.md`; reports in
   `reports/`.

## What the table shows

IPF differs from Sjögren's. Many of the targets here have already been tried and failed in
IPF: CTGF (pamrevlumab), LOXL2 (simtuzumab), TGF-β (fresolimumab), αvβ6 integrin (STX-100,
abituzumab), LPA1 (BMS-986020). Several of the entry's most specific nodes have **no drugs
mapped in Open Targets**: IL-11, cGAS, MUC5B, CPT1A, DSP, DPP9.

Untested in IPF, at phase 2 or beyond elsewhere, acting in the useful direction:

| Gene | Drug | Stage elsewhere |
|---|---|---|
| BCL2L1 (senolysis) | navitoclax | phase 3 myelofibrosis; Open Targets also lists "approval" for neoplasm, not confirmed |
| TGFBR1 | galunisertib, vactosertib | phase 2–3, oncology |
| CTNNB1 / PORCN (Wnt) | PRI-724, WNT-974 | phase 2, oncology |
| PDE4B | ensifentrine (inhaled PDE3/4) | approved for COPD |
| LOXL2 | lenumlostat | phase 2, myelofibrosis |
| CSF1R | pexidartinib | approved, tenosynovial giant cell tumour |

The PDE4B row also lists approved non-selective agents (dyphylline, flavoxate, amlexanox)
that are not plausible candidates; read that row for ensifentrine.

## OpenScientist assessments

Every cited PMID verified in all four reports (20, 18, 19 and 21 references), and no quote
failures.

| Candidate | Node in our entry | Verdict |
|---|---|---|
| navitoclax | Senescent myofibroblast persistence and apoptosis resistance; AT2 cell senescence and SASP | Target better validated than the drug. Never trialled in IPF; only small dasatinib + quercetin pilots exist. Senolysis repeatedly improves lung function and epithelial repair without shrinking established fibrosis. Dose-limiting thrombocytopenia; BCL-2 inhibition can worsen epithelial loss through ER stress. Suggests venetoclax (BCL-2-selective) as a safer route. |
| anti-IL-11 / IL-11RA antibody | IL-11 Autocrine Signalling in Lung Fibroblasts | Moderate. Biology among the best-replicated antifibrotic mechanisms, highest in IPF with pulmonary hypertension. No genetic support, and the class of downstream TGF-β effectors has repeatedly failed phase 3. LASN01 (NCT05331300) completed phase 1/2 in IPF/PF-ILD with no posted results. |
| ensifentrine | Fibroblast activation and myofibroblast differentiation | Plausible but speculative. The pathway is clinically validated by nerandomilast (FIBRONEER-IPF, PMID:40387033); ensifentrine itself has no fibrosis data at any level. Inhaled delivery may spare oral PDE4 side effects but must reach stiff, scarred lung. |
| cGAS or STING inhibitor | Self-DNA sensing through epithelial cGAS | Worth testing. Pathway active in IPF tissue; STING gain-of-function (SAVI) causes interstitial lung disease in humans; blockade reduces fibrosis in animal models. No inhibitor has been in an IPF trial, and the dominant cell may be the macrophage rather than the epithelium the node names. |

## Recurring themes

- **Pathway validated, molecule not.** Every candidate has strong pathway evidence and no
  trial data for the specific drug in IPF.
- **Function improves, fibrosis stays.** Senolysis and several other approaches improve lung
  function or repair in animals without reversing established fibrosis.
- **Downstream targets lack genetic support.** IPF risk genes are telomere, MUC5B,
  surfactant and host-defence genes; IL-11, cGAS-STING and PDE4 are downstream of them.
- **Biomarker-enriched phase 2** is the recommended test in all four: senescence or short
  telomeres, serum IL-11 or pulmonary hypertension, or an interferon / cGAMP signature.

## Leads for the dismech entry

- The cGAS node names the epithelium; the report argues macrophages carry much of the effect
  in models. Check the node's cell types against its evidence.
- SAVI (STING1 gain of function) as human genetic evidence on the cGAS node.
- LASN01 (NCT05331300) as a `clinical_trials` entry once results post.
