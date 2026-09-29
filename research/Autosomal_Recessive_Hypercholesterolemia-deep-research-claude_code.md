---
disease_name: Autosomal Recessive Hypercholesterolemia
mondo_id: MONDO:0011374
category: Mendelian
provider: claude_code
generation_mode: manual_pubmed_sweep_fallback
fell_back: true
requested_provider: claude_code
fallback_reason: >-
  The automated `just research-disorder claude_code Autosomal_Recessive_Hypercholesterolemia`
  run exited 0 but produced no report file: the shared build-host root filesystem was at
  100% capacity (ENOSPC) while a sibling curation session ran its own deep-research
  concurrently, so the report write failed silently. In place of the automated report,
  a manual PubMed sweep (NCBI E-utilities esearch/esummary/efetch) was performed and
  every cited reference was fetched with `just fetch-reference` and quoted from its
  cached abstract or full text.
date: "2026-09-03"
claim_issue: "#10721"
---

# Autosomal Recessive Hypercholesterolemia (ARH) — manual research sweep

## Summary

ARH (hypercholesterolemia, familial, 4; MONDO:0011374; OMIM:603813) is a
recessively inherited monogenic hypercholesterolemia caused by biallelic
loss-of-function variants in **LDLRAP1** (hgnc:18640), which encodes the LDL
receptor adaptor protein (ARH). ARH is a cytosolic adaptor whose phosphotyrosine
binding (PTB) domain recognizes the FDNPVY/NPxY motif in the LDL receptor
cytoplasmic tail and whose clathrin-box and AP-2-binding regions bridge the bound
receptor to the clathrin endocytic machinery. Its function is tissue specific —
required in hepatocytes but not fibroblasts (where Dab2 is redundant). Loss of ARH
leaves a structurally normal LDL receptor that reaches the hepatocyte surface but
cannot cluster into clathrin-coated pits and internalize LDL. Hepatic LDL clearance
fails, plasma LDL-C is markedly and lifelong elevated (homozygous-FH magnitude),
and patients develop tendon xanthomas, premature ASCVD, and aortic valve stenosis.
ARH behaves as a phenocopy of homozygous FH. It is ultra-rare, with a Sardinian
founder concentration (ARH1/ARH2 alleles). Because conventional receptor-dependent
therapies (statins, PCSK9 inhibitors) act by increasing receptor number and the ARH
receptor cannot internalize LDL, LDL-C stays far from target on conventional therapy;
LDL-receptor-independent approaches (lomitapide, ezetimibe, lipoprotein apheresis)
retain efficacy.

## Mechanism chain (as curated)

Biallelic LDLRAP1 loss-of-function → loss of ARH adaptor bridging of the LDL receptor
to clathrin (PTB↔NPxY, clathrin/AP-2) → impaired clathrin-mediated endocytosis of the
hepatocyte LDL receptor (liver-restricted; Dab2 redundant in fibroblasts) → impaired
hepatic clearance of plasma LDL → lifelong LDL-C elevation → premature ASCVD (coronary
atherosclerosis, aortic valve stenosis) and extravascular cholesterol deposition
(tendon xanthoma, xanthelasma, corneal arcus).

## References used (all fetched and snippet-verified against the local cache)

- **PMID:11326085** — Garcia et al., Science 2001. Founding gene-discovery paper:
  maps ARH to 1p35, identifies six LDLRAP1 mutations, PTB domain binding NPxY,
  tissue-specific role (liver not fibroblasts). *(HUMAN_CLINICAL)*
- **PMID:16179341** — Michaely et al., J Biol Chem 2005. ARH bridges the LDLR tail
  to clathrin/AP-2; PTB + clathrin-box/AP-2 required for LDLR clustering and
  internalization; cell-type-specific endocytic defect. *(IN_VITRO / WIF-B hepatocytes
  + Arh−/− mouse confirmation)*
- **PMID:32011344** — D'Erasmo et al., Curr Opin Lipidol 2020. ARH update: ultrarare,
  LDLRAP1, recessive, uniformly LOF; phenocopy of HoFH; elevated ASCVD and aortic
  valve stenosis risk; LDL-C far from target on conventional therapy; lomitapide as a
  new opportunity. *(HUMAN_CLINICAL review)*
- **PMID:36072671** — D'Erasmo et al., Front Genet 2022. Pan-European Lomitapide Study
  ARH subanalysis (n=9): mechanism (LDLRAP1 cytosolic adaptor, hepatocyte LDL
  internalization), ~90% xanthomata, ASCVD comparable to HoFH, PCSK9i efficacy disputed
  (residual-LDLR-dependent), lomitapide LDLR-independent → median on-treatment LDL-C
  101.7 mg/dL (60.4% reduction). *(HUMAN_CLINICAL cohort; full text cached)*
- **PMID:27079874** — Cameron et al./Tveten et al., ATVB 2016. PCSK9 inhibition
  (alirocumab) in ARH lymphocytes: surface LDLR higher in ARH than control; PCSK9's
  effect on LDLR expression/function less pronounced in ARH; partial potential in some
  patients. *(IN_VITRO)*
- **PMID:29153781** — Averna group, J Clin Lipidol 2018. Genetic epidemiology of ARH in
  Sicily/Sardinia: high mutated-allele frequency in Sardinia, ARH1/ARH2 founder alleles,
  ARH1 allele frequency 0.02% in Sicily, extremely rare outside Sardinia. *(HUMAN_CLINICAL)*
- **PMID:24404629** — GeneReviews: Familial Hypercholesterolemia (Adam et al.). Class-level
  FH chapter used for inheritance (biallelic LDLRAP1, autosomal recessive, obligate-carrier
  parents), clinical stigmata (MI, xanthelasma, corneal arcus), and management (LDL apheresis
  in established CAD). Tagged GeneReviews in the entry. *(HUMAN_CLINICAL / OTHER for management)*

## Reference Validation

All seven references were fetched with `just fetch-reference` and every evidence snippet
in the curated entry was verified as an exact substring against the local
`references_cache/` (49/49 snippets verified by `just validate` / `just validate-disorders`).
No fabricated identifiers; PMIDs preferred throughout (no DOI-only citations).

## Term Validation

All ontology CURIEs bound in the entry resolved against their ontologies and passed
`just validate-terms`. The one term not previously in the local cache
(`GO:0035615`, clathrin-cargo adaptor activity) was independently confirmed reachable
from `GO:0003674` (molecular_function) via local OAK before binding.

## Named Entity Confusion preflight

The hypercholesterolemia series is a high-NEC-risk numbered/lettered class (FH1/LDLR,
familial defective apoB-100/APOB, ADH3/PCSK9, ARH/LDLRAP1). Every mechanistic and
clinical claim here is anchored on **LDLRAP1/ARH** publications; the shared distal
LDL-to-plaque cascade is deliberately not re-derived from the dominant-FH entries. The
MONDO term MONDO:0011374 (hypercholesterolemia, familial, 4) and OMIM:603813 both key on
the LDLRAP1/ARH recessive entity.
