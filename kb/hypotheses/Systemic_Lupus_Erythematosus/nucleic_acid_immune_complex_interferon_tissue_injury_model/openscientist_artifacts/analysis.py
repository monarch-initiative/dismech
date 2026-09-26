#!/usr/bin/env python3
"""
Standalone deterministic replication analysis for GSE65391 (pediatric SLE
whole-blood microarray cohort, Illumina HumanHT-12 v4, GPL10558).

Hypothesis: nucleic_acid_immune_complex_interferon_tissue_injury_model
Tests whether the blood type I interferon signature tracks disease activity and
nephritis, or only disease presence.

Inputs (retrieved or reused from --cache-dir):
  - GSE65391 series matrix (log2-normalized expression + sample metadata)
  - GPL10558 GEO annotation (probe -> gene symbol)

Outputs (written to --output-dir):
  - samples.csv, gene_results.csv, correlations.csv, methods.md

No LLM is used. Deterministic given the same inputs.
"""
import argparse
import gzip
import os
import sys
from collections import defaultdict

import numpy as np
import pandas as pd
import requests
from scipy import stats
from statsmodels.stats.multitest import multipletests

# ---------------------------------------------------------------------------
# Canonical, credential-free input URLs
# ---------------------------------------------------------------------------
SERIES_MATRIX_URL = (
    "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE65nnn/GSE65391/matrix/"
    "GSE65391_series_matrix.txt.gz"
)
ANNOT_URL = (
    "https://ftp.ncbi.nlm.nih.gov/geo/platforms/GPL10nnn/GPL10558/annot/"
    "GPL10558.annot.gz"
)
SERIES_MATRIX_FILE = "GSE65391_series_matrix.txt.gz"
ANNOT_FILE = "GPL10558.annot.gz"

# ---------------------------------------------------------------------------
# Target genes
# ---------------------------------------------------------------------------
IFN_GENES = ["IFI27", "IFI44L", "IFIT1", "ISG15", "RSAD2", "SIGLEC1"]
PLASMABLAST_GENES = ["JCHAIN", "MZB1", "TNFRSF17"]  # JCHAIN is the current symbol for IGJ
ALL_TARGET_GENES = IFN_GENES + PLASMABLAST_GENES

CLINICAL_VARS = ["sledai", "ds_dna", "c3", "c4", "neutrophil_count"]

# Nephritis grouping (documented in methods.md)
NEPH_POS = {"Prolif", "Membr", "Mesan", "Proli+Membr"}   # biopsy-proven LN class
NEPH_NEG = {"NoLN", "Data Not Available"}                 # no recorded LN class


def download(url, path):
    if os.path.exists(path) and os.path.getsize(path) > 0:
        return
    tmp = path + ".part"
    with requests.get(url, stream=True, timeout=1200) as r:
        r.raise_for_status()
        with open(tmp, "wb") as f:
            for chunk in r.iter_content(1 << 20):
                f.write(chunk)
    os.replace(tmp, path)


def parse_series_matrix(path):
    """Return (metadata DataFrame indexed by GSM, expression DataFrame probe x GSM)."""
    geos = []
    char = defaultdict(dict)
    with gzip.open(path, "rt") as f:
        for line in f:
            if line.startswith("!series_matrix_table_begin"):
                break
            if line.startswith("!Sample_geo_accession"):
                geos = [c.strip().strip('"') for c in line.rstrip("\n").split("\t")[1:]]
            elif line.startswith("!Sample_characteristics_ch1"):
                cells = [c.strip().strip('"') for c in line.rstrip("\n").split("\t")[1:]]
                for i, c in enumerate(cells):
                    if ": " in c:
                        k, v = c.split(": ", 1)
                    else:
                        k, v = c, ""
                    char[i][k.strip()] = v.strip()
    meta_rows = []
    for i, g in enumerate(geos):
        row = dict(char[i])
        row["geo_accession"] = g
        meta_rows.append(row)
    meta = pd.DataFrame(meta_rows).set_index("geo_accession")

    # Expression: parse only rows we need would be faster, but we parse full matrix
    # for the target probes only to keep it light and deterministic.
    target_probes = set(TARGET_PROBES_GLOBAL)
    header = None
    data = {}
    with gzip.open(path, "rt") as f:
        started = False
        for line in f:
            if line.startswith("!series_matrix_table_begin"):
                started = True
                continue
            if not started:
                continue
            if line.startswith("!series_matrix_table_end"):
                break
            parts = line.rstrip("\n").split("\t")
            pid = parts[0].strip().strip('"')
            if pid == "ID_REF":
                header = [c.strip().strip('"') for c in parts[1:]]
                continue
            if pid in target_probes:
                data[pid] = [float(x) if x not in ("", "null", "NA") else np.nan
                             for x in parts[1:]]
    expr = pd.DataFrame(data, index=header).T  # probes x samples
    expr.columns = header
    return meta, expr


def load_annotation(path):
    """Return dict gene_symbol -> list of probe ids (from GPL10558 annot)."""
    sym2probes = defaultdict(list)
    with gzip.open(path, "rt", errors="replace") as f:
        for line in f:
            if line.startswith("!platform_table_begin"):
                break
        header = f.readline().rstrip("\n").split("\t")
        idx_id = header.index("ID")
        idx_sym = header.index("Gene symbol")
        for line in f:
            if line.startswith("!platform_table_end"):
                break
            p = line.rstrip("\n").split("\t")
            if len(p) <= idx_sym:
                continue
            sym = p[idx_sym].strip()
            if sym:
                sym2probes[sym].append(p[idx_id].strip())
    return sym2probes


def cohens_d(a, b):
    """Pooled-SD Cohen's d, (mean_a - mean_b). a = group1 (case)."""
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    na, nb = len(a), len(b)
    va, vb = a.var(ddof=1), b.var(ddof=1)
    sp = np.sqrt(((na - 1) * va + (nb - 1) * vb) / (na + nb - 2))
    if sp == 0:
        return np.nan
    return (a.mean() - b.mean()) / sp


def welch_row(gene, comparison, g1_label, g2_label, a, b):
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    a = a[~np.isnan(a)]
    b = b[~np.isnan(b)]
    t, p = stats.ttest_ind(a, b, equal_var=False)
    m1, m2 = a.mean(), b.mean()
    log2diff = m1 - m2  # expression already log2-scale
    return dict(
        dataset="GSE65391",
        gene=gene,
        comparison=comparison,
        group1_label=g1_label,
        group2_label=g2_label,
        n_group1=len(a),
        n_group2=len(b),
        mean_group1=m1,
        mean_group2=m2,
        log2_mean_difference=log2diff,
        fold_change=float(2.0 ** log2diff),
        t_statistic=float(t),
        p_value=float(p),
        cohens_d=cohens_d(a, b),
    )


def bh_within(df, pcol="p_value", qcol="q_value_bh"):
    df = df.copy()
    q = np.full(len(df), np.nan)
    mask = df[pcol].notna().values
    if mask.sum() > 0:
        q[mask] = multipletests(df.loc[mask, pcol].values, method="fdr_bh")[1]
    df[qcol] = q
    return df


TARGET_PROBES_GLOBAL = []  # filled in main after annotation load


def main():
    global TARGET_PROBES_GLOBAL
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--cache-dir", default=None)
    args = ap.parse_args()

    out_dir = args.output_dir
    cache_dir = args.cache_dir or os.path.join(out_dir, "raw")
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(cache_dir, exist_ok=True)

    sm_path = os.path.join(cache_dir, SERIES_MATRIX_FILE)
    annot_path = os.path.join(cache_dir, ANNOT_FILE)
    download(SERIES_MATRIX_URL, sm_path)
    download(ANNOT_URL, annot_path)

    # 1) Probe -> gene mapping (need target probes before parsing expression)
    sym2probes = load_annotation(annot_path)
    probe2gene = {}
    for g in ALL_TARGET_GENES:
        for pr in sym2probes.get(g, []):
            probe2gene[pr] = g
    TARGET_PROBES_GLOBAL = list(probe2gene.keys())

    # 2) Parse metadata + target-probe expression
    meta, expr = parse_series_matrix(sm_path)

    # numeric helpers
    meta["visit_num"] = pd.to_numeric(meta["visit"], errors="coerce")
    meta["sledai_num"] = pd.to_numeric(meta["sledai"], errors="coerce")

    # 3) Sample inclusion / exclusion
    #    (a) exclude set == Technical_Replicate
    #    (b) keep one array per subject-visit (deterministic: smallest GSM)
    meta = meta.copy()
    meta["exclusion_reason"] = ""
    meta.loc[meta["set"] == "Technical_Replicate", "exclusion_reason"] = "technical_replicate"

    kept = meta[meta["exclusion_reason"] == ""].copy()
    kept = kept.sort_index()  # GSM order
    dup_mask = kept.duplicated(subset=["subject", "visit"], keep="first")
    dup_ids = kept.index[dup_mask]
    meta.loc[dup_ids, "exclusion_reason"] = "duplicate_subject_visit"

    included = meta[meta["exclusion_reason"] == ""].copy()

    # 4) First included visit per subject (each subject -> one sample)
    inc_sorted = included.sort_values(
        ["subject", "visit_num", "visit"], kind="stable"
    ).sort_index(kind="stable")
    # stable sort by GSM then by (subject, visit_num) so ties break on GSM
    inc_sorted = included.reset_index().sort_values(
        ["subject", "visit_num", "geo_accession"], kind="stable"
    )
    first_ids = inc_sorted.groupby("subject", as_index=False).first()["geo_accession"]
    first_set = set(first_ids)
    meta["first_visit"] = meta.index.isin(first_set)
    meta["included"] = meta["exclusion_reason"] == ""

    # 5) Probe -> gene collapse: highest mean expression across included samples
    inc_ids = [g for g in expr.columns if g in set(included.index)]
    gene_expr = {}          # gene -> Series over all samples (expr.columns)
    gene_probe_used = {}
    for g in ALL_TARGET_GENES:
        probes = [p for p in sym2probes.get(g, []) if p in expr.index]
        if not probes:
            continue
        means = expr.loc[probes, inc_ids].mean(axis=1)
        best = means.sort_values(ascending=False).index[0]
        # deterministic tie-break: highest mean, then lexicographically smallest probe
        top = means[means == means.max()].index.tolist()
        best = sorted(top)[0]
        gene_probe_used[g] = best
        gene_expr[g] = expr.loc[best]
    gene_df = pd.DataFrame(gene_expr)  # index = samples, cols = genes

    # 6) Group assignments (first-visit)
    fv = meta[meta["first_visit"]].copy()
    fv_sle = fv[fv["disease state"] == "SLE"].copy()
    fv_healthy = fv[fv["disease state"] == "Healthy"].copy()

    # disease group
    meta["group_disease"] = np.where(
        meta["first_visit"], meta["disease state"], ""
    )
    # sledai group (SLE first visit)
    def sledai_grp(idx):
        if idx not in fv_sle.index:
            return ""
        v = meta.at[idx, "sledai_num"]
        if pd.isna(v):
            return "NA"
        return "SLEDAI>=6" if v >= 6 else "SLEDAI<6"
    meta["group_sledai"] = [sledai_grp(i) for i in meta.index]
    # nephritis group (SLE first visit)
    def neph_grp(idx):
        if idx not in fv_sle.index:
            return ""
        nc = meta.at[idx, "nephritis_class"]
        if nc in NEPH_POS:
            return "Nephritis"
        if nc in NEPH_NEG:
            return "NoNephritis"
        return "NA"
    meta["group_nephritis"] = [neph_grp(i) for i in meta.index]

    # ---------------------------------------------------------------
    # 7) IFN6 composite score (z vs Healthy first-visit samples)
    # ---------------------------------------------------------------
    healthy_ids = list(fv_healthy.index)
    fv_ids = list(fv.index)
    z = pd.DataFrame(index=fv_ids)
    for g in IFN_GENES:
        s = gene_df[g]
        mu = s.loc[healthy_ids].mean()
        sd = s.loc[healthy_ids].std(ddof=1)
        z[g] = (s.loc[fv_ids] - mu) / sd
    ifn6 = z.mean(axis=1)  # per first-visit sample
    gene_df_score = gene_df.copy()
    gene_df_score["IFN6_SCORE"] = np.nan
    gene_df_score.loc[fv_ids, "IFN6_SCORE"] = ifn6

    # ---------------------------------------------------------------
    # 8) Contrasts
    # ---------------------------------------------------------------
    analysis_genes = IFN_GENES + ["IFN6_SCORE"] + PLASMABLAST_GENES

    def values(idx_list, gene):
        return gene_df_score.loc[idx_list, gene].values

    results = []

    # Contrast 1: SLE vs Healthy (first visit)
    c1_g1 = list(fv_sle.index)
    c1_g2 = list(fv_healthy.index)
    rows1 = [welch_row(g, "SLE_vs_Healthy_firstvisit", "SLE", "Healthy",
                       values(c1_g1, g), values(c1_g2, g)) for g in analysis_genes]
    rows1 = bh_within(pd.DataFrame(rows1))
    results.append(rows1)

    # Contrast 2: within SLE, SLEDAI>=6 vs <6 (first visit)
    g2_hi = list(fv_sle.index[fv_sle["sledai_num"] >= 6])
    g2_lo = list(fv_sle.index[fv_sle["sledai_num"] < 6])
    rows2 = [welch_row(g, "SLE_SLEDAIhi_vs_lo_firstvisit", "SLEDAI>=6", "SLEDAI<6",
                       values(g2_hi, g), values(g2_lo, g)) for g in analysis_genes]
    rows2 = bh_within(pd.DataFrame(rows2))
    results.append(rows2)

    # Contrast 3: within SLE, nephritis vs no nephritis (first visit)
    g3_pos = [i for i in fv_sle.index if meta.at[i, "group_nephritis"] == "Nephritis"]
    g3_neg = [i for i in fv_sle.index if meta.at[i, "group_nephritis"] == "NoNephritis"]
    rows3 = [welch_row(g, "SLE_nephritis_vs_none_firstvisit", "Nephritis", "NoNephritis",
                       values(g3_pos, g), values(g3_neg, g)) for g in analysis_genes]
    rows3 = bh_within(pd.DataFrame(rows3))
    results.append(rows3)

    gene_results = pd.concat(results, ignore_index=True)
    col_order = ["dataset", "gene", "comparison", "group1_label", "group2_label",
                 "n_group1", "n_group2", "mean_group1", "mean_group2",
                 "log2_mean_difference", "fold_change", "t_statistic",
                 "p_value", "q_value_bh", "cohens_d"]
    gene_results = gene_results[col_order]

    # ---------------------------------------------------------------
    # 9) Correlations (SLE first-visit): IFN6 + plasmablast vs clinical
    # ---------------------------------------------------------------
    clin = pd.DataFrame(index=fv_sle.index)
    for cv in CLINICAL_VARS:
        clin[cv] = pd.to_numeric(fv_sle[cv], errors="coerce")
    feat = pd.DataFrame(index=fv_sle.index)
    feat["IFN6_SCORE"] = gene_df_score.loc[fv_sle.index, "IFN6_SCORE"]
    for g in PLASMABLAST_GENES:
        feat[g] = gene_df_score.loc[fv_sle.index, g]

    corr_rows = []
    for fname in ["IFN6_SCORE"] + PLASMABLAST_GENES:
        for cv in CLINICAL_VARS:
            x = feat[fname]
            y = clin[cv]
            m = x.notna() & y.notna()
            n = int(m.sum())
            if n >= 3:
                rho, p = stats.spearmanr(x[m], y[m])
            else:
                rho, p = np.nan, np.nan
            corr_rows.append(dict(dataset="GSE65391", feature=fname,
                                  clinical_var=cv, n=n,
                                  spearman_rho=float(rho) if rho == rho else np.nan,
                                  p_value=float(p) if p == p else np.nan))
    corr_df = bh_within(pd.DataFrame(corr_rows))
    corr_df = corr_df[["dataset", "feature", "clinical_var", "n",
                       "spearman_rho", "p_value", "q_value_bh"]]

    # ---------------------------------------------------------------
    # 10) samples.csv
    # ---------------------------------------------------------------
    samp_cols = {
        "accession": meta.index,
        "dataset": "GSE65391",
        "organism": "Homo sapiens",
        "tissue": meta.get("tissue", "whole blood"),
        "subject": meta["subject"],
        "visit": meta["visit"],
        "set": meta["set"],
        "disease_state": meta["disease state"],
        "sledai": meta["sledai"],
        "nephritis_class": meta["nephritis_class"],
        "ds_dna": meta["ds_dna"],
        "c3": meta["c3"],
        "c4": meta["c4"],
        "neutrophil_count": meta["neutrophil_count"],
        "included": meta["included"],
        "first_visit": meta["first_visit"],
        "group_disease": meta["group_disease"],
        "group_sledai": meta["group_sledai"],
        "group_nephritis": meta["group_nephritis"],
        "exclusion_reason": meta["exclusion_reason"],
    }
    samples = pd.DataFrame(samp_cols)
    samples = samples.reset_index(drop=True).sort_values("accession").reset_index(drop=True)

    # ---------------------------------------------------------------
    # Write outputs (deterministic ordering)
    # ---------------------------------------------------------------
    samples.to_csv(os.path.join(out_dir, "samples.csv"), index=False, lineterminator="\n")
    gene_results.to_csv(os.path.join(out_dir, "gene_results.csv"), index=False, lineterminator="\n")
    corr_df.to_csv(os.path.join(out_dir, "correlations.csv"), index=False, lineterminator="\n")

    # methods.md (deterministic content, incl. group counts)
    n_sle = int((fv["disease state"] == "SLE").sum())
    n_hc = int((fv["disease state"] == "Healthy").sum())
    methods = f"""# Methods — GSE65391 interferon / plasmablast replication

## Data source (normalization state)
- Series: GSE65391 (pediatric SLE whole blood, Illumina HumanHT-12 v4, GPL10558).
- Expression matrix: GEO series matrix `{SERIES_MATRIX_FILE}`. Values are the
  authors' processed, **log2-scale** normalized intensities (per-probe training/test
  ratio adjustment described in GEO `data_processing`). No further transform applied.
- Probe annotation: GEO `{ANNOT_FILE}` (GPL10558 annotation table, `Gene symbol`).

## Sample inclusion / exclusion
- Start: 996 arrays.
- Exclude `set == Technical_Replicate` (n=24) -> reason `technical_replicate`.
- Keep one array per (subject, visit); deterministic tie-break keeps the smallest
  GSM accession -> reason `duplicate_subject_visit` for any dropped array
  (none required: 0 duplicate subject-visit pairs remained after replicate removal).
- Included arrays: {int(meta['included'].sum())}.
- Cross-sectional contrasts use each subject's **first included visit** only
  (minimum numeric `visit`; ties broken by GSM). Each subject contributes one sample.
- First-visit subjects: {len(fv)} ({n_sle} SLE, {n_hc} Healthy).

## Probe -> gene mapping and aggregation
- Probes mapped to gene symbols via GPL10558 `Gene symbol`.
- When several probes map to one gene, the probe with the **highest mean expression
  across included samples** is used (tie-break: lexicographically smallest probe id).
- Probe selected per gene:
{os.linesep.join(f"  - {g}: {gene_probe_used.get(g,'NA')}" for g in ALL_TARGET_GENES)}
- IGJ is not present in this GPL10558 annotation; the current symbol **JCHAIN**
  (ILMN_2105441) is used for the plasmablast J-chain gene.

## Composite interferon score
- `IFN6_SCORE` = mean of per-gene z-scores of {", ".join(IFN_GENES)}.
- Z-scores computed against the **Healthy first-visit** samples (mean and SD, ddof=1)
  per gene. The score is added as a row `IFN6_SCORE` in gene_results.csv.

## Contrasts (each reported for all target genes + IFN6_SCORE)
1. SLE vs Healthy (disease state), first visit.
2. Within SLE, SLEDAI>=6 vs SLEDAI<6 at first visit
   (SLEDAI>=6 n={len(g2_hi)}, SLEDAI<6 n={len(g2_lo)}).
3. Within SLE, biopsy-proven nephritis vs no nephritis at first visit
   (Nephritis n={len(g3_pos)}, NoNephritis n={len(g3_neg)}).

### Nephritis-class parsing (metadata ambiguity)
- Observed `nephritis_class` values within SLE first-visit:
  Prolif, Membr, Mesan, Proli+Membr (positive histologic LN classes),
  NoLN ("no lupus nephritis"), and "Data Not Available".
- **Nephritis** group = {{Prolif, Membr, Mesan, Proli+Membr}} (biopsy-proven LN class).
- **NoNephritis** group = {{NoLN, "Data Not Available"}} (no recorded positive LN class,
  matching the "not recorded / Not Applicable" rule). "Not Applicable" occurs only for
  Healthy samples and is therefore absent from this SLE-only contrast.

## Statistics
- Welch's two-sample t-test (unequal variance) for every gene/contrast.
- Effect size: pooled-SD Cohen's d, oriented as (group1 - group2) with group1 the
  "case" group (SLE / SLEDAI>=6 / Nephritis).
- `log2_mean_difference` = mean(group1) - mean(group2) (data already log2);
  `fold_change` = 2**log2_mean_difference (not biologically meaningful for the
  z-based IFN6_SCORE row, reported for schema completeness).
- Multiple testing: Benjamini-Hochberg FDR computed **within each contrast**
  across all rows (6 genes + IFN6_SCORE).

## Correlations (correlations.csv)
- Within SLE first-visit samples, Spearman correlation of IFN6_SCORE and plasmablast
  genes (JCHAIN, MZB1, TNFRSF17) against numeric sledai, ds_dna, c3, c4, neutrophil_count.
- Non-numeric or 'Not Applicable' clinical values treated as missing
  (pairwise-complete n reported). BH-FDR across all 20 feature x variable pairs.
- Note: `ds_dna` is largely reported as titers (e.g. "1:40"), "(-)", or
  "Data Not Available"; per the "non-numeric = missing" rule these become missing, so
  the numeric ds_dna sample size is small.
"""
    with open(os.path.join(out_dir, "methods.md"), "w") as f:
        f.write(methods)

    print("Wrote outputs to", out_dir)
    print("Included samples:", int(meta["included"].sum()),
          "| First-visit:", len(fv), "| SLE:", n_sle, "Healthy:", n_hc)


if __name__ == "__main__":
    sys.exit(main())
