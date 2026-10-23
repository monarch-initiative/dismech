#!/usr/bin/env python3
"""
Standalone deterministic replication analysis for hypothesis
`ll37_nlrp3_il1b_papulopustular` (Rosacea) using GEO dataset GSE155141.

Two prespecified paired contrasts in papulopustular-rosacea explant RNA-seq:
  (1) lesional vs paired non-lesional (untreated) skin
  (2) IL-1beta-treated vs untreated non-lesional explants

Target genes: NLRP3, CASP1, PYCARD, IL1B, IL18, IL1RN, CAMP, KLK5

No LLM is involved. Given the same inputs and package versions the script
regenerates byte-identical samples.csv and gene_results.csv.

Usage:
  python analysis.py --output-dir OUT [--cache-dir RAW]

Only Python stdlib + numpy, pandas, scipy, requests are used.
"""
import argparse
import gzip
import hashlib
import io
import os

import numpy as np
import pandas as pd
import requests
from scipy import stats
from statsmodels.stats.multitest import multipletests

# ----------------------------------------------------------------------------
# Input registry: canonical, credential-free NCBI GEO URLs.
# ----------------------------------------------------------------------------
GSE = "GSE155141"
BASE = "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE155nnn/GSE155141"
INPUTS = {
    "GSE155141_series_matrix.txt.gz":
        BASE + "/matrix/GSE155141_series_matrix.txt.gz",
    "GSE155141_rawCount_rosacea_no_Tx.txt.gz":
        BASE + "/suppl/GSE155141_rawCount_rosacea_no_Tx.txt.gz",
    "GSE155141_rawCount_nonlesional_noTx_IL1.txt.gz":
        BASE + "/suppl/GSE155141_rawCount_nonlesional_noTx_IL1.txt.gz",
}

TARGET_GENES = ["NLRP3", "CASP1", "PYCARD", "IL1B", "IL18",
                "IL1RN", "CAMP", "KLK5"]

# GSM accessions in series-matrix order (subject x condition).
# Order verified from GSE155141_series_matrix.txt.gz !Sample_geo_accession.
GSM = {
    ("S1", "lesional"): "GSM4696228", ("S1", "nonlesional"): "GSM4696229",
    ("S1", "il1b"): "GSM4696230",
    ("S2", "lesional"): "GSM4696231", ("S2", "nonlesional"): "GSM4696232",
    ("S2", "il1b"): "GSM4696233",
    ("S3", "lesional"): "GSM4696234", ("S3", "nonlesional"): "GSM4696235",
    ("S3", "il1b"): "GSM4696236",
    ("S4", "lesional"): "GSM4696237", ("S4", "nonlesional"): "GSM4696238",
    ("S4", "il1b"): "GSM4696239",
    ("S5", "lesional"): "GSM4696240", ("S5", "nonlesional"): "GSM4696241",
    ("S5", "il1b"): "GSM4696242",
}
SUBJECT_AGE = {"S1": 82, "S2": 42, "S3": 92, "S4": 64, "S5": 73}
SUBJECTS = ["S1", "S2", "S3", "S4", "S5"]


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def fetch(fn, cache_dir):
    """Return raw bytes of an input, reusing cache_dir if present."""
    path = os.path.join(cache_dir, fn)
    if os.path.exists(path):
        with open(path, "rb") as fh:
            return fh.read()
    os.makedirs(cache_dir, exist_ok=True)
    r = requests.get(INPUTS[fn], timeout=300)
    r.raise_for_status()
    with open(path, "wb") as fh:
        fh.write(r.content)
    return r.content


def read_counts(raw_bytes):
    """Parse a headerless tab-delimited GEO raw-count file.

    Column 0 = gene symbol; remaining columns = integer counts, ordered by
    subject 1..5. Returns a DataFrame indexed by gene symbol.
    """
    idx, data = [], []
    with gzip.open(io.BytesIO(raw_bytes), "rt") as f:
        for line in f:
            p = line.rstrip("\n").split("\t")
            idx.append(p[0])
            data.append([int(x) for x in p[1:]])
    df = pd.DataFrame(data, index=idx)
    return df


def cpm_log2(counts):
    """Library-size CPM then log2(CPM + 1)."""
    lib = counts.sum(axis=0)
    cpm = counts.divide(lib, axis=1) * 1e6
    return np.log2(cpm + 1.0), cpm


def paired_stats(test_vals, ref_vals):
    """Paired statistics for one gene.

    test_vals / ref_vals are log2(CPM+1) arrays aligned by subject.
    Returns dict of statistics. Cohen's d is the paired dz =
    mean(diff)/sd(diff, ddof=1). log2_mean_diff and fold_change use log2(CPM+1)
    group means (test minus reference).
    """
    test_vals = np.asarray(test_vals, dtype=float)
    ref_vals = np.asarray(ref_vals, dtype=float)
    diff = test_vals - ref_vals
    mean_test = float(test_vals.mean())
    mean_ref = float(ref_vals.mean())
    log2_mean_diff = mean_test - mean_ref
    fold_change = float(2.0 ** log2_mean_diff)
    t_stat, p_val = stats.ttest_rel(test_vals, ref_vals)
    sd = diff.std(ddof=1)
    cohens_d = float(diff.mean() / sd) if sd > 0 else float("nan")
    return {
        "n_group1": len(ref_vals),
        "n_group2": len(test_vals),
        "mean_group1": mean_ref,
        "mean_group2": mean_test,
        "log2_mean_diff": float(log2_mean_diff),
        "fold_change": fold_change,
        "test_statistic": float(t_stat),
        "p_value": float(p_val),
        "cohens_d": cohens_d,
    }


def build_samples_table():
    """One row per included sample (all 15 included; none excluded)."""
    rows = []
    # column layout inside each raw-count file (verified empirically)
    layout = [
        # (subject, condition, group_label, count_file, col_index_0based)
    ]
    ros_file = "GSE155141_rawCount_rosacea_no_Tx.txt.gz"
    nl_file = "GSE155141_rawCount_nonlesional_noTx_IL1.txt.gz"
    for i, s in enumerate(SUBJECTS):
        layout.append((s, "lesional", "lesional_noTx", ros_file, i))
    for i, s in enumerate(SUBJECTS):
        layout.append((s, "nonlesional", "nonlesional_noTx", nl_file, i))
    for i, s in enumerate(SUBJECTS):
        layout.append((s, "il1b", "nonlesional_IL1b", nl_file, i + 5))
    source_name = {
        "lesional": "rosacea_no Tx",
        "nonlesional": "nonlesional_no Tx",
        "il1b": "nonlesional_IL1",
    }
    tissue_type = {
        "lesional": "lesional papulopustular rosacea human skin",
        "nonlesional": "non-lesional human skin",
        "il1b": "non-lesional human skin",
    }
    treatment = {
        "lesional": "none (no treatment)",
        "nonlesional": "none (no treatment)",
        "il1b": "50ng/mL IL-1beta",
    }
    for s, cond, grp, cf, col in layout:
        rows.append({
            "accession": GSM[(s, cond)],
            "dataset": GSE,
            "organism": "Homo sapiens",
            "tissue": "facial skin",
            "tissue_type": tissue_type[cond],
            "source_name": source_name[cond],
            "treatment": treatment[cond],
            "subject": s,
            "subject_age": SUBJECT_AGE[s],
            "count_file": cf,
            "count_column_index": col,
            "assigned_group": grp,
            "exclusion_reason": "",
        })
    df = pd.DataFrame(rows)
    df = df.sort_values(["assigned_group", "subject"]).reset_index(drop=True)
    return df


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--cache-dir", default=None)
    args = ap.parse_args()

    out = args.output_dir
    os.makedirs(out, exist_ok=True)
    cache = args.cache_dir if args.cache_dir else os.path.join(out, "raw")

    # ---- retrieve inputs ----
    raw = {fn: fetch(fn, cache) for fn in INPUTS}

    ros = read_counts(raw["GSE155141_rawCount_rosacea_no_Tx.txt.gz"])
    nl = read_counts(raw["GSE155141_rawCount_nonlesional_noTx_IL1.txt.gz"])
    assert list(ros.index) == list(nl.index), "gene order mismatch"
    assert ros.shape[1] == 5 and nl.shape[1] == 10, "unexpected column counts"

    # ---- normalize ----
    ros_log, _ = cpm_log2(ros)
    nl_log, _ = cpm_log2(nl)

    # condition matrices (columns ordered by subject S1..S5)
    lesional = ros_log.iloc[:, 0:5]          # 5 lesional
    nonlesional = nl_log.iloc[:, 0:5]        # 5 non-lesional untreated
    il1b = nl_log.iloc[:, 5:10]              # 5 non-lesional IL-1beta

    comparisons = [
        ("lesional_vs_nonlesional", lesional, nonlesional,
         "lesional_noTx", "nonlesional_noTx"),
        ("il1b_vs_untreated_nonlesional", il1b, nonlesional,
         "nonlesional_IL1b", "nonlesional_noTx"),
    ]

    records = []
    for cmp_name, test_mat, ref_mat, test_grp, ref_grp in comparisons:
        per_gene = []
        for g in TARGET_GENES:
            st = paired_stats(test_mat.loc[g].values, ref_mat.loc[g].values)
            st.update({
                "dataset": GSE,
                "gene": g,
                "comparison": cmp_name,
                "group1_label": ref_grp,
                "group2_label": test_grp,
            })
            per_gene.append(st)
        pvals = [r["p_value"] for r in per_gene]
        qvals = multipletests(pvals, method="fdr_bh")[1]
        for r, q in zip(per_gene, qvals):
            r["q_value"] = float(q)
        records.extend(per_gene)

    cols = ["dataset", "gene", "comparison", "group1_label", "group2_label",
            "n_group1", "n_group2", "mean_group1", "mean_group2",
            "log2_mean_diff", "fold_change", "test_statistic",
            "p_value", "q_value", "cohens_d"]
    gene_df = pd.DataFrame(records)[cols]
    gene_df = gene_df.sort_values(["comparison", "gene"]).reset_index(drop=True)

    samples_df = build_samples_table()

    # ---- deterministic CSV writing ----
    samples_df.to_csv(os.path.join(out, "samples.csv"),
                      index=False, lineterminator="\n")
    gene_df.to_csv(os.path.join(out, "gene_results.csv"),
                   index=False, float_format="%.10g", lineterminator="\n")
    print("Wrote samples.csv (%d rows) and gene_results.csv (%d rows)"
          % (len(samples_df), len(gene_df)))


if __name__ == "__main__":
    main()
