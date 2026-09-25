#!/usr/bin/env python
"""
Exploratory test of hypothesis phyma_fibroblast_identity.
Dataset: ArrayExpress/BioStudies E-MTAB-16629 (released 2026-02-18)
  "Distinct diversity of skin cell populations of rhinophyma and hypertrophic scar
   illustrated by scRNA-seq" (Homo sapiens, 10x 3' v3; one individual per condition).

Question: Do rhinophyma fibroblasts carry the PTGDS-high pro-inflammatory signature of
papulopustular rosacea (PMID:39384741), or an ACTA2/COL1A1 scar-myofibroblast signature?

Per-sample pipeline (run one sample per call because the executor has a 60s wall-clock
limit and no cross-call filesystem persistence).
Env: scanpy/anndata, scipy.io.mmread, requests. Seed np.random.seed(0).
Files served from:
  https://ftp.ebi.ac.uk/biostudies/fire/E-MTAB-/629/E-MTAB-16629/Files/
"""
import requests, os, numpy as np, scanpy as sc, anndata as ad, pandas as pd
from scipy.io import mmread
from scipy.sparse import csr_matrix
sc.settings.verbosity = 0
np.random.seed(0)

BASE = "https://ftp.ebi.ac.uk/biostudies/fire/E-MTAB-/629/E-MTAB-16629/Files/"
WD = "/tmp/e"; os.makedirs(WD, exist_ok=True)

def dl(f):
    p = os.path.join(WD, f)
    if not os.path.exists(p):
        open(p, "wb").write(requests.get(BASE + f, timeout=180).content)
    return p

SAMPLES = {  # key: (matrix, features, barcodes, condition)
    "ROS":     ("ROSmatrix.mtx.gz",    "ROSfeatures.tsv.gz",    "ROSbarcodes.tsv.gz",    "Rhinophyma"),
    "HS":      ("HS-Hmatrix.mtx.gz",   "HS-Hfeatures.tsv.gz",   "HS-Hbarcodes.tsv.gz",   "HypertrophicScar"),
    "Healthy": ("Skin-Hmatrix.mtx.gz", "Skin-Hfeatures.tsv.gz", "Skin-Hbarcodes.tsv.gz", "Healthy"),
}

LINEAGE_MARKERS = {
    "Fibroblast":   ["COL1A1","COL1A2","DCN","LUM","PDGFRA","COL3A1"],
    "Keratinocyte": ["KRT14","KRT5","KRT1","KRT10","KRT15","KRT6A"],
    "Endothelial":  ["PECAM1","VWF","CLDN5","CDH5"],
    "Myeloid":      ["LYZ","CD68","AIF1","ITGAX","HLA-DRA"],
    "TNK":          ["CD3D","CD3E","TRAC","NKG7","CD2"],
    "Melanocyte":   ["MLANA","PMEL","TYRP1","DCT"],
    "Mural":        ["RGS5","NOTCH3","PDGFRB","MYH11","MCAM"],  # ACTA2/TAGLN deliberately excluded so myofibroblasts stay in Fibroblast
    "Mast":         ["TPSAB1","CPA3","MS4A2"],
}
PROINFLAM = ["PTGDS","CXCL1","CXCL2","CXCL12","CCL19","IL6","PLA2G2A","C3","C7","CCL2","APOD","CFD"]
MYOFIB    = ["ACTA2","TAGLN","MYH11","POSTN","COL1A1","COL3A1","FN1","CTHRC1"]

def run(key):
    mtx, feat, bc, cond = SAMPLES[key]
    M = mmread(dl(mtx)).tocsr()                                  # genes x cells
    sym = pd.read_csv(dl(feat), sep="\t", header=None)[1].astype(str).values  # col 1 = HGNC symbol
    bcs = pd.read_csv(dl(bc), sep="\t", header=None)[0].values
    A = ad.AnnData(X=csr_matrix(M.T), obs=pd.DataFrame(index=bcs),
                   var=pd.DataFrame(index=sym))
    A.var_names_make_unique(); A.obs["condition"] = cond
    A.var["mt"] = A.var_names.str.startswith("MT-")
    sc.pp.calculate_qc_metrics(A, qc_vars=["mt"], inplace=True, percent_top=None)
    sc.pp.filter_cells(A, min_genes=200)
    A = A[A.obs.pct_counts_mt < 20].copy()
    sc.pp.filter_genes(A, min_cells=3)
    sc.pp.normalize_total(A, target_sum=1e4); sc.pp.log1p(A)
    present = {k: [g for g in v if g in A.var_names] for k, v in LINEAGE_MARKERS.items()}
    keys = [k for k, v in present.items() if v]
    for k in keys:
        sc.tl.score_genes(A, present[k], score_name="sc_" + k)
    A.obs["lineage"] = [keys[i] for i in A.obs[["sc_" + k for k in keys]].values.argmax(1)]
    fib = A[A.obs.lineage == "Fibroblast"].copy()
    sc.tl.score_genes(fib, [g for g in PROINFLAM if g in fib.var_names], score_name="proinflam")
    sc.tl.score_genes(fib, [g for g in MYOFIB   if g in fib.var_names], score_name="myofib")
    return A, fib

if __name__ == "__main__":
    for key in SAMPLES:          # in practice run one key per executor call
        A, fib = run(key)
        print(key, "fibroblasts n=", fib.n_obs,
              "proinflam=", round(fib.obs.proinflam.mean(), 3),
              "myofib=", round(fib.obs.myofib.mean(), 3))
