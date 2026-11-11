# Amyotrophic lateral sclerosis: mechanism-led drug candidates

The third disease run with the method used for Sjögren's and IPF (`../sjogren/README.md`,
`../ipf/README.md`). ALS is a Biomni Target Atlas disease, our entry has 18 mechanism nodes,
and the field has a long record of failed trials to check candidates against. Done
2026-11-12.

## Method

1. `genes.tsv`: 24 genes. The entry's own node genes (SOD1, C9orf72, TARDBP, FUS, STMN2,
   UNC13A, TBK1, ERBB4, TREM2, PIKFYVE, HK1), druggable genes for nodes that bind none
   (glutamate excitotoxicity, neuroinflammation, senescence, axon degeneration), and
   SIGMAR1 from the Open Targets top hits.
2. `../repurposing_candidates.py` with
   `--disease MONDO_0004976 --pattern 'amyotrophic|\bALS\b|motor neuron disease'`.
   Output: `opentargets/candidates.tsv` (120 rows). Open Targets lists 6,329 genes and 185
   drugs for ALS.
3. Four candidates assessed by OpenScientist with `../repurposing_template.md`; reports in
   `reports/`.

## What the table shows

Open Targets maps **no drugs** to most of the genes that define ALS: C9orf72, ATXN2, FUS,
TARDBP, STMN2, UNC13A, TBK1, TREM2, SLC1A2, NLRP3, SARM1 and HK1, although antisense drugs
for several of them are in ALS trials. It also files drugs under targets that hide their ALS
trials: rapamycin is mapped to FKBP1A, not MTOR, and RIPK1 and DLK inhibitors tested in ALS
are not mapped to RIPK1 or MAP3K12. For ALS the "untested" column is much less reliable than
for Sjögren's or IPF.

Already tried in ALS, from the table: tofersen (SOD1), perampanel, talampanel and topiramate
(AMPA receptor), ravulizumab and zilucoplan (complement C5), apilimod (PIKFYVE),
dextromethorphan (sigma-1).

Untested, at phase 2 or beyond elsewhere, acting in the useful direction:

| Gene | Drug | Stage elsewhere |
|---|---|---|
| C5 | crovalimab, eculizumab, vilobelimab | approved or phase 4 |
| CSF1R | pexidartinib, axatilimab | approved |
| BCL2L1 | navitoclax | Open Targets lists approval for neoplasm, not confirmed |
| RIPK1 | GSK2982772 | phase 2, psoriasis and RA |
| MAP3K12 | CEP-1347 | phase 2/3, Parkinson's disease |
| GRIA2 | selurampanel, becampanel | phase 2, epilepsy |

## OpenScientist assessments

Every cited reference verified. The NLRP3 report's validator could not resolve
PMID:26444282 during a network outage; it is the 2015 anakinra pilot in ALS (PLoS One),
now cached, and the quote the report uses matches it.

| Candidate | Node in our entry | Verdict |
|---|---|---|
| NLRP3 inhibitor (dapansutrile) | Neuroinflammation | Mechanism active, treatment unproven. Inflammasome components are raised in ALS tissue, blood and CSF; misfolded SOD1 and TDP-43 both activate it; blocking its output extends survival in SOD1 mice. No NLRP3 inhibitor has been trialled in ALS, and anakinra (IL-1 receptor antagonist) did not slow progression in a 17-patient pilot (PMID:26444282). In some human studies the main NLRP3-expressing cell is the astrocyte. |
| SARM1 inhibitor | Axonal Transport Dysfunction (axon degeneration) | Moderately strong, and now being tested: NB-4746 is in a recruiting phase 1b/2 ALS trial (NCT07369076). Gain-of-function SARM1 variants are enriched more than fivefold in ALS (PMID:34991663). Sarm1 deletion protects axons and synapses in a TDP-43 model (PMID:31661035), but structural rescue has not translated into functional benefit in the models tested. |
| CSF1R inhibitor (pexidartinib) | Neuroinflammation | Target legitimate, drug and strategy weak. CSF1R signalling drives microgliosis in ALS cord and nerve, but ablating proliferating microglia did not slow motor neuron loss in SOD1 mice (PMID:18842883), microglia can be protective, and CSF1R loss of function itself causes a neurodegenerative leukoencephalopathy. Pexidartinib carries a boxed warning for fatal liver injury. |
| navitoclax | Cellular Senescence in Motor Cortex and Spinal Cord | Drug mismatched to the mechanism. Senescence is a real feature of ALS, but navitoclax inhibits BCL-2 and BCL-xL, which protect motor neurons: Bcl-2 overexpression attenuates degeneration in SOD1 mice (PMID:10582606). The only positive ALS senolytic result used dasatinib plus quercetin (PMID:40196013). |

## Recurring themes

- **Stratify.** Neuroinflammation is a feature of a definable subtype ("ALS-Glia"), not
  every patient; all four reports recommend biomarker-selected trials (CSF IL-18,
  genetic subgroup, inflammatory subtype).
- **Structure saved, function not.** SARM1 deletion, like senolysis in IPF, protects tissue
  in models without a matching functional benefit.
- **Same drug, opposite fit.** Navitoclax was a reasonable IPF candidate; in ALS it attacks
  a survival pathway the vulnerable neurons depend on. A senolytic has to be chosen for the
  tissue, not just the mechanism.

## Leads for the dismech entry

- SARM1 as a genetic risk factor (PMID:34991663) and a gene on the axon degeneration node.
- NB-4746 (NCT07369076) as a `clinical_trials` entry.
- The Neuroinflammation node names microglia and astrocytes but binds no gene; the reports
  support NLRP3 and CSF1R as its pathway genes.
