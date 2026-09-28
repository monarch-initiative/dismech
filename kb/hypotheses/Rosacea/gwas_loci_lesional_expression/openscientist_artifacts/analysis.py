#!/usr/bin/env python3
"""
Standalone deterministic replication analysis for the Disorder Mechanisms
Knowledge Base hypothesis:

  Disease:    Rosacea
  Hypothesis: gwas_loci_lesional_expression
  Label:      Rosacea GWAS susceptibility loci act through altered expression in
              lesional skin, including a TLR1-TLR2 heterodimer axis.

Dataset:   GEO GSE65914 ("Th1/Th17 Immune Response in Rosacea"), platform GPL570
           (Affymetrix Human Genome U133 Plus 2.0 Array), RMA-normalized (log2).

For each rosacea GWAS locus gene we compute a lesional-vs-healthy-control
expression contrast, separately for the erythematotelangiectatic (ETR),
papulopustular (PPR) and phymatous (PhR) subtypes and for all rosacea pooled.
Across all samples we compute the Spearman correlation of TLR1 with TLR2 and
test whether that correlation differs between rosacea and control (Fisher r-to-z).

The script is deterministic and LLM-free. It accepts --output-dir and optionally
--cache-dir, retrieves (or reuses cached) exact inputs, and regenerates every
tabular output.

Third-party dependencies: numpy, pandas, scipy, statsmodels, requests.
"""
import argparse
import gzip
import hashlib
import io
import os
import platform
import sys
from datetime import datetime, timezone

import numpy as np
import pandas as pd
import requests
import scipy
from scipy import stats
import statsmodels
from statsmodels.stats.multitest import multipletests

# ----------------------------------------------------------------------------
# Fixed configuration
# ----------------------------------------------------------------------------
INPUTS = {
    "GSE65914_series_matrix.txt.gz":
        "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE65nnn/GSE65914/matrix/GSE65914_series_matrix.txt.gz",
    "GPL570.annot.gz":
        "https://ftp.ncbi.nlm.nih.gov/geo/platforms/GPLnnn/GPL570/annot/GPL570.annot.gz",
}

# GWAS locus target genes and their locus class.
IMMUNE_GENES = ["HLA-DRA", "BTNL2", "HLA-DRB1", "HLA-DQB1", "HLA-DQA1",
                "IL13", "IRF1", "TLR1", "TLR2", "IRF4"]
PIGMENT_GENES = ["HERC2", "OCA2", "SLC45A2"]
TARGET_GENES = IMMUNE_GENES + PIGMENT_GENES
LOCUS_CLASS = {**{g: "immune" for g in IMMUNE_GENES},
               **{g: "pigmentation" for g in PIGMENT_GENES}}

# Map the GEO "group:" characteristic to an analysis group label.
GROUP_MAP = {
    "Healthy volunteer": "control",
    "erythematotelangiectatic rosacea (ETR)": "ETR",
    "papulopustular rosacea (PPR)": "PPR",
    "phymatous rosacea (PhR)": "PhR",
}
# Comparisons: (label, list-of-lesional-group-labels). Order is fixed.
COMPARISONS = [
    ("ETR_vs_control", ["ETR"]),
    ("PPR_vs_control", ["PPR"]),
    ("PhR_vs_control", ["PhR"]),
    ("rosacea_pooled_vs_control", ["ETR", "PPR", "PhR"]),
]

ROUND = 10  # decimal places for deterministic float serialization


# ----------------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------------
def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def ensure_input(name, cache_dir, download_dir):
    """Return path to input `name`, reusing it from cache_dir if present,
    otherwise downloading into download_dir. Never downloads if cached."""
    if cache_dir:
        cached = os.path.join(cache_dir, name)
        if os.path.exists(cached):
            return cached
    dest = os.path.join(download_dir, name)
    if os.path.exists(dest):
        return dest
    os.makedirs(download_dir, exist_ok=True)
    url = INPUTS[name]
    with requests.get(url, stream=True, timeout=300) as r:
        r.raise_for_status()
        with open(dest, "wb") as fh:
            for chunk in r.iter_content(chunk_size=1 << 20):
                fh.write(chunk)
    return dest


def read_series_matrix(path):
    """Parse a GEO series_matrix file. Returns (expr_df [probe x sample],
    sample_meta DataFrame)."""
    with gzip.open(path, "rt", encoding="utf-8", errors="replace") as fh:
        lines = fh.readlines()

    def parse_bang(prefix):
        for ln in lines:
            if ln.startswith(prefix):
                parts = ln.rstrip("\n").split("\t")[1:]
                return [p.strip().strip('"') for p in parts]
        return None

    accessions = parse_bang("!Sample_geo_accession")
    titles = parse_bang("!Sample_title")
    chars = parse_bang("!Sample_characteristics_ch1")
    sources = parse_bang("!Sample_source_name_ch1")
    organisms = parse_bang("!Sample_organism_ch1")

    groups = []
    for c in chars:
        val = c.split("group:", 1)[1].strip() if "group:" in c else c
        groups.append(val)

    meta = pd.DataFrame({
        "accession": accessions,
        "title": titles,
        "source_name": sources,
        "organism": organisms,
        "group_raw": groups,
    })

    # locate data table
    b = e = None
    for i, ln in enumerate(lines):
        if ln.startswith("!series_matrix_table_begin"):
            b = i
        elif ln.startswith("!series_matrix_table_end"):
            e = i
            break
    table_text = "".join(lines[b + 1:e])
    expr = pd.read_csv(io.StringIO(table_text), sep="\t")
    expr = expr.rename(columns={expr.columns[0]: "ID_REF"})
    expr["ID_REF"] = expr["ID_REF"].astype(str)
    expr = expr.set_index("ID_REF")
    return expr, meta


def read_gpl_annotation(path):
    """Parse GPL570 .annot.gz. Returns dict probe_id -> list of gene symbols."""
    with gzip.open(path, "rt", encoding="utf-8", errors="replace") as fh:
        lines = fh.readlines()
    b = e = None
    for i, ln in enumerate(lines):
        if ln.startswith("!platform_table_begin"):
            b = i
        elif ln.startswith("!platform_table_end"):
            e = i
            break
    table_text = "".join(lines[b + 1:e])
    ann = pd.read_csv(io.StringIO(table_text), sep="\t", dtype=str)
    id_col = ann.columns[0]           # "ID"
    sym_col = "Gene symbol"
    mapping = {}
    for pid, sym in zip(ann[id_col], ann[sym_col]):
        pid = str(pid)
        if pd.isna(sym) or str(sym).strip() == "":
            mapping[pid] = []
        else:
            mapping[pid] = [s.strip() for s in str(sym).split("///") if s.strip()]
    return mapping


def gene_level_matrix(expr, probe2genes, genes):
    """For each target gene, aggregate matching probes by arithmetic mean on the
    (log2) expression scale. Returns (gene_expr_df [gene x sample], n_probes)."""
    samples = list(expr.columns)
    rows = {}
    n_probes = {}
    for g in genes:
        probes = [p for p in expr.index if g in probe2genes.get(p, [])]
        probes = sorted(probes)
        n_probes[g] = len(probes)
        if probes:
            rows[g] = expr.loc[probes, samples].mean(axis=0)
        else:
            rows[g] = pd.Series([np.nan] * len(samples), index=samples)
    gene_expr = pd.DataFrame(rows).T
    gene_expr.index.name = "gene"
    return gene_expr, n_probes


def cohens_d(a, b):
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    n1, n2 = len(a), len(b)
    s1, s2 = a.var(ddof=1), b.var(ddof=1)
    pooled = np.sqrt(((n1 - 1) * s1 + (n2 - 1) * s2) / (n1 + n2 - 2))
    if pooled == 0:
        return np.nan
    return (a.mean() - b.mean()) / pooled


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--cache-dir", default=None,
                    help="Directory to reuse already-downloaded raw inputs from.")
    args = ap.parse_args()

    out = args.output_dir
    os.makedirs(out, exist_ok=True)
    # raw downloads (only used if cache miss) go under output/raw
    download_dir = args.cache_dir if args.cache_dir else os.path.join(out, "raw")

    # ---- retrieve inputs ----
    matrix_path = ensure_input("GSE65914_series_matrix.txt.gz",
                               args.cache_dir, download_dir)
    annot_path = ensure_input("GPL570.annot.gz", args.cache_dir, download_dir)

    expr, meta = read_series_matrix(matrix_path)
    probe2genes = read_gpl_annotation(annot_path)

    # ---- assign groups ----
    meta["group"] = meta["group_raw"].map(GROUP_MAP)
    meta["dataset"] = "GSE65914"
    meta["tissue"] = "facial skin biopsy"
    meta["exclusion_reason"] = ""
    # any sample whose group is not mapped would be excluded
    unmapped = meta["group"].isna()
    meta.loc[unmapped, "exclusion_reason"] = "group_not_in_analysis_map"

    included = meta[~unmapped].copy()
    sample_group = dict(zip(included["accession"], included["group"]))
    all_samples = [s for s in expr.columns if s in sample_group]

    def samples_for(labels):
        return [s for s in all_samples if sample_group[s] in labels]

    control_samples = samples_for(["control"])

    # ---- gene-level matrix ----
    gene_expr, n_probes = gene_level_matrix(expr, probe2genes, TARGET_GENES)

    # ---- per gene x comparison contrasts ----
    records = []
    for g in TARGET_GENES:
        for comp_label, les_labels in COMPARISONS:
            les_s = samples_for(les_labels)
            ctrl_s = control_samples
            les = gene_expr.loc[g, les_s].astype(float).values
            ctrl = gene_expr.loc[g, ctrl_s].astype(float).values
            les = les[~np.isnan(les)]
            ctrl = ctrl[~np.isnan(ctrl)]
            if len(les) >= 2 and len(ctrl) >= 2 and n_probes[g] > 0:
                mean_les = float(np.mean(les))
                mean_ctrl = float(np.mean(ctrl))
                log2_diff = mean_les - mean_ctrl
                fc = float(2.0 ** log2_diff)
                t_stat, p_val = stats.ttest_ind(les, ctrl, equal_var=False)
                d = cohens_d(les, ctrl)
            else:
                mean_les = mean_ctrl = log2_diff = fc = t_stat = p_val = d = np.nan
            records.append({
                "dataset": "GSE65914",
                "gene": g,
                "locus_class": LOCUS_CLASS[g],
                "comparison": comp_label,
                "n_probes": n_probes[g],
                "n_lesional": len(les),
                "n_control": len(ctrl),
                "mean_lesional": mean_les,
                "mean_control": mean_ctrl,
                "log2_mean_diff": log2_diff,
                "fold_change": fc,
                "t_statistic": float(t_stat) if pd.notna(t_stat) else np.nan,
                "p_value": float(p_val) if pd.notna(p_val) else np.nan,
                "cohens_d": float(d) if pd.notna(d) else np.nan,
            })

    gene_results = pd.DataFrame.from_records(records)
    # BH-FDR across all gene x comparison tests jointly (deterministic)
    mask = gene_results["p_value"].notna()
    gene_results["q_value_BH"] = np.nan
    if mask.any():
        _, q, _, _ = multipletests(gene_results.loc[mask, "p_value"].values,
                                   method="fdr_bh")
        gene_results.loc[mask, "q_value_BH"] = q

    # deterministic ordering: gene alphabetical, then fixed comparison order
    comp_order = {c[0]: i for i, c in enumerate(COMPARISONS)}
    gene_results["_c"] = gene_results["comparison"].map(comp_order)
    gene_results = gene_results.sort_values(["gene", "_c"]).drop(columns="_c")
    col_order = ["dataset", "gene", "locus_class", "comparison", "n_probes",
                 "n_lesional", "n_control", "mean_lesional", "mean_control",
                 "log2_mean_diff", "fold_change", "t_statistic", "p_value",
                 "q_value_BH", "cohens_d"]
    gene_results = gene_results[col_order]
    float_cols = ["mean_lesional", "mean_control", "log2_mean_diff",
                  "fold_change", "t_statistic", "p_value", "q_value_BH",
                  "cohens_d"]
    gene_results[float_cols] = gene_results[float_cols].round(ROUND)

    # ---- TLR1-TLR2 Spearman correlation ----
    ros_samples = samples_for(["ETR", "PPR", "PhR"])
    def spearman(sub):
        x = gene_expr.loc["TLR1", sub].astype(float).values
        y = gene_expr.loc["TLR2", sub].astype(float).values
        rho, p = stats.spearmanr(x, y)
        return float(rho), float(p), len(sub)

    rho_all, p_all, n_all = spearman(all_samples)
    rho_ros, p_ros, n_ros = spearman(ros_samples)
    rho_ctrl, p_ctrl, n_ctrl = spearman(control_samples)
    # Fisher r-to-z difference test (rosacea vs control)
    z1 = np.arctanh(rho_ros)
    z2 = np.arctanh(rho_ctrl)
    se = np.sqrt(1.0 / (n_ros - 3) + 1.0 / (n_ctrl - 3))
    z_diff = (z1 - z2) / se
    p_diff = float(2 * (1 - stats.norm.cdf(abs(z_diff))))
    tlr = pd.DataFrame([{
        "dataset": "GSE65914",
        "gene_x": "TLR1",
        "gene_y": "TLR2",
        "method": "spearman",
        "n_all": n_all, "rho_all": rho_all, "p_all": p_all,
        "n_rosacea": n_ros, "rho_rosacea": rho_ros, "p_rosacea": p_ros,
        "n_control": n_ctrl, "rho_control": rho_ctrl, "p_control": p_ctrl,
        "fisher_z_diff": float(z_diff), "p_diff_rosacea_vs_control": p_diff,
    }])
    tlr_float = ["rho_all", "p_all", "rho_rosacea", "p_rosacea",
                 "rho_control", "p_control", "fisher_z_diff",
                 "p_diff_rosacea_vs_control"]
    tlr[tlr_float] = tlr[tlr_float].round(ROUND)

    # ---- samples.csv ----
    samples = meta.copy()
    samples["assigned_group"] = samples["group"].fillna("EXCLUDED")
    samples = samples[["accession", "dataset", "organism", "tissue",
                       "source_name", "title", "group_raw", "assigned_group",
                       "exclusion_reason"]]
    samples = samples.sort_values("accession").reset_index(drop=True)

    # ---- write outputs (deterministic) ----
    samples.to_csv(os.path.join(out, "samples.csv"), index=False,
                   lineterminator="\n")
    gene_results.to_csv(os.path.join(out, "gene_results.csv"), index=False,
                        lineterminator="\n")
    tlr.to_csv(os.path.join(out, "tlr_correlation.csv"), index=False,
               lineterminator="\n")

    # ---- environment.txt ----
    env_lines = [
        f"python_version: {platform.python_version()}",
        f"platform: {platform.platform()}",
        f"numpy: {np.__version__}",
        f"pandas: {pd.__version__}",
        f"scipy: {scipy.__version__}",
        f"statsmodels: {statsmodels.__version__}",
        f"requests: {requests.__version__}",
    ]
    with open(os.path.join(out, "environment.txt"), "w") as fh:
        fh.write("\n".join(env_lines) + "\n")

    print("Wrote outputs to", out)
    print(gene_results.to_string(index=False))
    print(tlr.to_string(index=False))


if __name__ == "__main__":
    main()
