# Robustness check — is there a hidden PTGDS-high fibroblast subpopulation in rhinophyma?

Clustering-free orthogonal test on the rhinophyma sample (E-MTAB-16629, ROS; 7505 QC-passed cells).
Method: normalize_total(1e4)+log1p; rank cells by PTGDS; profile lineage-marker means in the
top-5% PTGDS cells vs the rest; and profile PTGDS in a stringent fibroblast gate.

## Result
- PTGDS detected in only **2.9%** of all rhinophyma cells (global mean 0.038; max 5.34 — so the gene is capturable, not a technical dropout of PTGDS itself).
- PTGDS-high cells (n=191) are **endothelial**, not fibroblast:
  - Endothelial score 1.244 (PTGDS-high) vs 0.532 (rest)
  - Fibroblast score 0.179 vs 0.098 (weak)
  - Myeloid/T/Mural/Keratinocyte: not enriched
- Stringent fibroblast gate (COL1A1>1 & DCN>0.5 & PECAM1<0.5 & LYZ<0.5; n=224):
  - PTGDS positive in only **4.0%** (mean 0.151)
  - ACTA2 positive in **46.9%**

## Interpretation
No hidden PTGDS-high fibroblast subpopulation is present in the rhinophyma sample; the residual PTGDS
signal localizes to endothelium. This makes the coarse-assignment artifact explanation unlikely and
reinforces the primary finding: rhinophyma fibroblasts are PTGDS-low and ACTA2-activated.

## Limitation
Single rhinophyma individual; a per-sample capture/batch effect that specifically lowers fibroblast
PTGDS cannot be fully excluded without additional rhinophyma donors or the papulopustular reference in a
joint embedding.
