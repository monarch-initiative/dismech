#!/usr/bin/env python3
"""
Prespecified differential-expression replication for hypothesis
`calcium_clearance_failure_model` (Duchenne Muscular Dystrophy).

Dataset: GEO GSE299627, human skeletal myoblast RNA-seq (Illumina NovaSeq X Plus,
GPL34284, BioProject PRJNA1275763). Gene-level counts are distributed only as six
per-sample featureCounts files inside GSE299627_RAW.tar.

Comparison (one only): DMD (AB1071; GSM9042258, GSM9042259, GSM9042260)
versus healthy (AB1190; GSM9042255, GSM9042256, GSM9042257).

Deterministic: no random number use, no timestamps in any output file.

Usage:
    python3 analysis.py --output-dir OUT [--cache-dir RAW]
"""

import argparse
import gzip
import hashlib
import io
import json
import os
import platform
import sys
import tarfile

import numpy as np
import pandas as pd

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import requests

# ----------------------------------------------------------------------------
# Constants
# ----------------------------------------------------------------------------

GEO_TAR_URL = (
    "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE299nnn/GSE299627/suppl/"
    "GSE299627_RAW.tar"
)
HGNC_URL = (
    "https://storage.googleapis.com/public-download-files/hgnc/tsv/tsv/"
    "hgnc_complete_set.txt"
)

INPUTS = [
    {"filename": "GSE299627_RAW.tar", "url": GEO_TAR_URL, "accession": "GSE299627"},
    {"filename": "hgnc_complete_set.txt", "url": HGNC_URL, "accession": "HGNC_complete_set"},
]

# Per-sample metadata transcribed from the GEO series/sample records of GSE299627.
SAMPLES = [
    # accession, title, member file, cell line, genotype, group
    ("GSM9042255", "WT1",   "GSM9042255_WT1.counts.txt.gz",   "AB1190", "wildtype", "healthy"),
    ("GSM9042256", "WT2",   "GSM9042256_WT2.counts.txt.gz",   "AB1190", "wildtype", "healthy"),
    ("GSM9042257", "WT3",   "GSM9042257_WT3.counts.txt.gz",   "AB1190", "wildtype", "healthy"),
    ("GSM9042258", "DMD1",  "GSM9042258_DMD1.counts.txt.gz",  "AB1071", "DMD",      "DMD"),
    ("GSM9042259", "DMD2",  "GSM9042259_DMD2.counts.txt.gz",  "AB1071", "DMD",      "DMD"),
    ("GSM9042260", "DMD3",  "GSM9042260_DMD3.counts.txt.gz",  "AB1071", "DMD",      "DMD"),
]
ORGANISM = "Homo sapiens"
TISSUE = "skeletal muscle, paravertebral"
CELL_TYPE = "skeletal myoblasts"
TREATMENT = "untreated"
PLATFORM = "GPL34284"
DATASET = "GSE299627"
COMPARISON = "DMD_vs_healthy"

TARGET_GENES = [
    "FBN1", "FBN2", "FBN3",
    "LTBP1", "LTBP2", "LTBP3", "LTBP4",
    "ZNF277",
    "ATP2A1", "ATP2A2", "ATP2A3",
    "SLN", "PLN", "CASQ1", "CASQ2",
    "CALM1", "CALM2", "CALM3",
    "RYR1", "ITPR1",
    "ORAI1", "STIM1", "TRPC1", "TRPC3", "TRPC6", "PIEZO1",
    "DMD",
]
TARGET_SET = {
    "FBN1": "fibrillin (reported finding)",
    "FBN2": "fibrillin (reported finding)",
    "FBN3": "fibrillin",
    "LTBP1": "fibrillin-binding ECM partner",
    "LTBP2": "fibrillin-binding ECM partner",
    "LTBP3": "fibrillin-binding ECM partner",
    "LTBP4": "fibrillin-binding ECM partner / DMD modifier locus",
    "ZNF277": "proposed conserved transcriptional regulator",
    "ATP2A1": "SERCA paralog",
    "ATP2A2": "SERCA paralog",
    "ATP2A3": "SERCA paralog",
    "SLN": "SR calcium handling / SERCA regulator",
    "PLN": "SR calcium handling / SERCA regulator",
    "CASQ1": "SR calcium handling / SERCA regulator",
    "CASQ2": "SR calcium handling / SERCA regulator",
    "CALM1": "calmodulin",
    "CALM2": "calmodulin",
    "CALM3": "calmodulin",
    "RYR1": "SR calcium release",
    "ITPR1": "SR calcium release",
    "ORAI1": "sarcolemmal calcium entry (competing model)",
    "STIM1": "sarcolemmal calcium entry (competing model)",
    "TRPC1": "sarcolemmal calcium entry (competing model)",
    "TRPC3": "sarcolemmal calcium entry (competing model)",
    "TRPC6": "sarcolemmal calcium entry (competing model)",
    "PIEZO1": "sarcolemmal calcium entry (competing model)",
    "DMD": "positive control for the dystrophic genotype",
}

# Published values stated in the hypothesis record, for side-by-side reporting only.
PUBLISHED = {"FBN1": -1.2, "FBN2": -0.9}

MIN_COUNT = 10          # filtering rule: raw count >= MIN_COUNT ...
MIN_SAMPLES = 3         # ... in at least MIN_SAMPLES samples (smallest group size)
ALPHA = 0.05


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def fetch(url, dest):
    """Download `url` to `dest` unless `dest` already exists."""
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        return False
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with requests.get(url, stream=True, timeout=600) as r:
        r.raise_for_status()
        tmp = dest + ".part"
        with open(tmp, "wb") as fh:
            for chunk in r.iter_content(chunk_size=1 << 20):
                fh.write(chunk)
        os.replace(tmp, dest)
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--cache-dir", default=None)
    args = ap.parse_args()

    out = os.path.abspath(args.output_dir)
    cache = os.path.abspath(args.cache_dir) if args.cache_dir else os.path.join(out, "raw")
    os.makedirs(out, exist_ok=True)
    os.makedirs(cache, exist_ok=True)

    log_lines = []

    def log(msg):
        print(msg)
        log_lines.append(str(msg))

    # ---------------- retrieval ----------------
    input_records = []
    for spec in INPUTS:
        dest = os.path.join(cache, spec["filename"])
        downloaded = fetch(spec["url"], dest)
        rec = {
            "accession": spec["accession"],
            "filename": spec["filename"],
            "url": spec["url"],
            "path": dest,
            "byte_count": os.path.getsize(dest),
            "sha256": sha256_of(dest),
            "freshly_downloaded": downloaded,
        }
        input_records.append(rec)
        log(f"INPUT {spec['filename']} bytes={rec['byte_count']} sha256={rec['sha256']} "
            f"downloaded={downloaded}")

    tar_path = input_records[0]["path"]
    hgnc_path = input_records[1]["path"]

    # ---------------- assemble count matrix ----------------
    # featureCounts output: columns Geneid, Chr, Start, End, Strand, Length, <sample>
    counts = {}
    gene_length = None
    gene_order = None
    with tarfile.open(tar_path, "r") as tf:
        members = {m.name: m for m in tf.getmembers()}
        for acc, title, fname, _cl, _gt, _grp in SAMPLES:
            if fname not in members:
                raise RuntimeError(f"count file missing from archive: {fname}")
            raw = tf.extractfile(members[fname]).read()
            txt = gzip.GzipFile(fileobj=io.BytesIO(raw)).read().decode("utf-8")
            df = pd.read_csv(io.StringIO(txt), sep="\t")
            if df.columns[0] != "Geneid":
                raise RuntimeError(f"unexpected header in {fname}: {list(df.columns)[:3]}")
            ids = df["Geneid"].astype(str).to_numpy()
            if gene_order is None:
                gene_order = ids
                gene_length = df["Length"].to_numpy()
            elif not np.array_equal(gene_order, ids):
                raise RuntimeError(f"gene order mismatch in {fname}")
            counts[acc] = df.iloc[:, -1].to_numpy()
            log(f"parsed {fname}: {df.shape[0]} rows, count column '{df.columns[-1]}'")

    mat = pd.DataFrame(counts, index=pd.Index(gene_order, name="Geneid"))
    mat = mat[[s[0] for s in SAMPLES]]
    n_genes_raw = mat.shape[0]
    log(f"identifier type in count files: Ensembl gene ID (unversioned, e.g. {mat.index[0]})")
    log(f"genes in assembled matrix (Ensembl level): {n_genes_raw}")

    lib_sizes = mat.sum(axis=0)
    for acc in mat.columns:
        log(f"library size {acc}: {int(lib_sizes[acc])}")

    mat.to_csv(os.path.join(out, "count_matrix.csv"))

    # ---------------- identifier mapping ----------------
    hgnc = pd.read_csv(hgnc_path, sep="\t", dtype=str, low_memory=False)
    hgnc = hgnc[hgnc["status"] == "Approved"]
    hgnc = hgnc[["hgnc_id", "symbol", "ensembl_gene_id"]].dropna(subset=["ensembl_gene_id"])
    hgnc = hgnc.sort_values(["ensembl_gene_id", "hgnc_id"], kind="mergesort")
    hgnc = hgnc.drop_duplicates(subset=["ensembl_gene_id"], keep="first")
    ens2sym = dict(zip(hgnc["ensembl_gene_id"], hgnc["symbol"]))
    log(f"HGNC approved records with an Ensembl gene ID: {len(ens2sym)}")

    sym = pd.Series([ens2sym.get(g) for g in mat.index], index=mat.index)
    n_mapped = int(sym.notna().sum())
    log(f"Ensembl IDs mapped to an approved HGNC symbol: {n_mapped} / {n_genes_raw}")
    log(f"Ensembl IDs with no approved HGNC symbol (kept under their Ensembl ID): "
        f"{n_genes_raw - n_mapped}")

    feature_id = sym.where(sym.notna(), pd.Series(mat.index, index=mat.index))
    agg = mat.copy()
    agg["feature_id"] = feature_id.to_numpy()
    n_multi = int((agg.groupby("feature_id", sort=False).size() > 1).sum())
    agg = agg.groupby("feature_id", sort=True).sum()
    agg.index.name = "feature_id"
    log(f"symbols receiving counts from more than one Ensembl ID (summed): {n_multi}")
    log(f"features after aggregation to HGNC symbol / unmapped Ensembl ID: {agg.shape[0]}")

    # ---------------- filtering ----------------
    keep = (agg >= MIN_COUNT).sum(axis=1) >= MIN_SAMPLES
    filt = agg.loc[keep]
    log(f"filter rule: raw count >= {MIN_COUNT} in at least {MIN_SAMPLES} of 6 samples")
    log(f"features before filtering: {agg.shape[0]}; after filtering: {filt.shape[0]}")
    filt.to_csv(os.path.join(out, "count_matrix_filtered.csv"))

    # ---------------- samples.csv ----------------
    srows = []
    for acc, title, fname, cl, gt, grp in SAMPLES:
        srows.append({
            "sample_accession": acc,
            "sample_title": title,
            "dataset": DATASET,
            "platform": PLATFORM,
            "organism": ORGANISM,
            "tissue": TISSUE,
            "cell_type": CELL_TYPE,
            "cell_line": cl,
            "genotype": gt,
            "treatment": TREATMENT,
            "source_file": fname,
            "assigned_group": grp,
            "included": True,
            "exclusion_reason": "",
            "library_size_raw_counts": int(lib_sizes[acc]),
        })
    samples_df = pd.DataFrame(srows)
    samples_df.to_csv(os.path.join(out, "samples.csv"), index=False)

    # ---------------- DESeq2 ----------------
    import pydeseq2
    from pydeseq2.dds import DeseqDataSet
    from pydeseq2.ds import DeseqStats

    metadata = samples_df.set_index("sample_accession")[["assigned_group", "cell_line"]]
    metadata = metadata.rename(columns={"assigned_group": "group"})
    metadata["group"] = pd.Categorical(metadata["group"], categories=["healthy", "DMD"])

    dds = DeseqDataSet(
        counts=filt.T,
        metadata=metadata,
        design="~group",
        refit_cooks=True,
        n_cpus=1,
        quiet=True,
    )
    dds.deseq2()
    stats = DeseqStats(
        dds,
        contrast=["group", "DMD", "healthy"],
        independent_filter=False,  # plain BH over all tested genes, no NaN q-values
        cooks_filter=True,
        quiet=True,
    )
    stats.summary()
    res = stats.results_df.copy()
    log(f"pydeseq2 version: {pydeseq2.__version__} (DESeq2 model; "
        f"median-of-ratios size-factor normalization; Wald test; BH adjustment)")

    normed = pd.DataFrame(
        dds.layers["normed_counts"], index=dds.obs_names, columns=dds.var_names
    ).T
    normed.to_csv(os.path.join(out, "normalized_counts.csv"))

    h_cols = [s[0] for s in SAMPLES if s[5] == "healthy"]
    d_cols = [s[0] for s in SAMPLES if s[5] == "DMD"]
    mean_h = normed[h_cols].mean(axis=1)
    mean_d = normed[d_cols].mean(axis=1)

    lg = np.log2(normed + 1.0)
    n1, n2 = len(h_cols), len(d_cols)
    v1 = lg[h_cols].var(axis=1, ddof=1)
    v2 = lg[d_cols].var(axis=1, ddof=1)
    s_pooled = np.sqrt(((n1 - 1) * v1 + (n2 - 1) * v2) / (n1 + n2 - 2))
    cohens_d = (lg[d_cols].mean(axis=1) - lg[h_cols].mean(axis=1)) / s_pooled.replace(0.0, np.nan)

    out_df = pd.DataFrame({
        "dataset": DATASET,
        "comparison": COMPARISON,
        "gene": res.index,
        "n_healthy": n1,
        "n_dmd": n2,
        "mean_normalized_healthy": mean_h.reindex(res.index).to_numpy(),
        "mean_normalized_dmd": mean_d.reindex(res.index).to_numpy(),
        "base_mean": res["baseMean"].to_numpy(),
        "log2_fold_change": res["log2FoldChange"].to_numpy(),
        "lfc_se": res["lfcSE"].to_numpy(),
        "log2_mean_difference": (
            np.log2(mean_d.reindex(res.index) + 1.0) - np.log2(mean_h.reindex(res.index) + 1.0)
        ).to_numpy(),
        "fold_change": (
            (mean_d.reindex(res.index) + 1.0) / (mean_h.reindex(res.index) + 1.0)
        ).to_numpy(),
        "test_statistic_wald": res["stat"].to_numpy(),
        "p_value": res["pvalue"].to_numpy(),
        "q_value_bh": res["padj"].to_numpy(),
        "cohens_d": cohens_d.reindex(res.index).to_numpy(),
    })
    out_df = out_df.sort_values(["p_value", "gene"], kind="mergesort").reset_index(drop=True)
    out_df.to_csv(os.path.join(out, "gene_results.csv"), index=False)

    sig = out_df[out_df["q_value_bh"] < ALPHA]
    n_up = int((sig["log2_fold_change"] > 0).sum())
    n_down = int((sig["log2_fold_change"] < 0).sum())
    log(f"genome-wide BH q < {ALPHA}: {len(sig)} genes ({n_up} up in DMD, {n_down} down in DMD)")

    # ---------------- target-gene table ----------------
    idx = out_df.set_index("gene")
    present_all = set(agg.index)
    trows = []
    for g in TARGET_GENES:
        row = {
            "dataset": DATASET,
            "comparison": COMPARISON,
            "gene": g,
            "gene_category": TARGET_SET[g],
        }
        if g in idx.index:
            r = idx.loc[g]
            row.update({
                "status": "tested",
                "n_healthy": int(r["n_healthy"]),
                "n_dmd": int(r["n_dmd"]),
                "mean_normalized_healthy": float(r["mean_normalized_healthy"]),
                "mean_normalized_dmd": float(r["mean_normalized_dmd"]),
                "base_mean": float(r["base_mean"]),
                "log2_fold_change": float(r["log2_fold_change"]),
                "lfc_se": float(r["lfc_se"]),
                "log2_mean_difference": float(r["log2_mean_difference"]),
                "fold_change": float(r["fold_change"]),
                "test_statistic_wald": float(r["test_statistic_wald"]),
                "p_value": float(r["p_value"]),
                "q_value_bh": float(r["q_value_bh"]),
                "cohens_d": float(r["cohens_d"]),
                "significant_bh_0.05": bool(r["q_value_bh"] < ALPHA),
            })
        else:
            reason = ("present in matrix but removed by the low-expression filter"
                      if g in present_all else
                      "absent from the assembled count matrix (no Ensembl ID mapped to this symbol)")
            row.update({
                "status": reason,
                "n_healthy": n1, "n_dmd": n2,
                "mean_normalized_healthy": np.nan, "mean_normalized_dmd": np.nan,
                "base_mean": np.nan, "log2_fold_change": np.nan, "lfc_se": np.nan,
                "log2_mean_difference": np.nan, "fold_change": np.nan,
                "test_statistic_wald": np.nan, "p_value": np.nan, "q_value_bh": np.nan,
                "cohens_d": np.nan, "significant_bh_0.05": False,
            })
            if g in present_all:
                row["mean_raw_healthy"] = float(agg.loc[g, h_cols].mean())
                row["mean_raw_dmd"] = float(agg.loc[g, d_cols].mean())
        trows.append(row)
    targets = pd.DataFrame(trows)
    if "mean_raw_healthy" not in targets.columns:
        targets["mean_raw_healthy"] = np.nan
        targets["mean_raw_dmd"] = np.nan
    targets.to_csv(os.path.join(out, "target_gene_results.csv"), index=False)

    # ---------------- replication check ----------------
    rep = []
    for g, pub in PUBLISHED.items():
        obs = targets.set_index("gene").loc[g]
        agree_sign = (not pd.isna(obs["log2_fold_change"])) and (np.sign(obs["log2_fold_change"]) == np.sign(pub))
        agree_mag = (not pd.isna(obs["log2_fold_change"])) and abs(obs["log2_fold_change"] - pub) <= 0.3
        agree_sig = (not pd.isna(obs["p_value"])) and obs["p_value"] < 1e-4
        rep.append({
            "gene": g,
            "published_log2_fold_change": pub,
            "published_p_claim": "p < 0.0001",
            "observed_log2_fold_change": obs["log2_fold_change"],
            "observed_p_value": obs["p_value"],
            "observed_q_value_bh": obs["q_value_bh"],
            "same_sign": bool(agree_sign),
            "magnitude_within_0.3_log2": bool(agree_mag),
            "observed_p_below_1e-4": bool(agree_sig),
            "agrees_on_all_three": bool(agree_sign and agree_mag and agree_sig),
        })
    pd.DataFrame(rep).to_csv(os.path.join(out, "replication_check.csv"), index=False)

    # ---------------- summary json ----------------
    summary = {
        "dataset": DATASET,
        "comparison": "DMD (AB1071, n=3 technical/passage replicates of one line) vs "
                      "healthy (AB1190, n=3 replicates of one line)",
        "identifier_type_in_source_files": "Ensembl gene ID (unversioned)",
        "genes_before_mapping": int(n_genes_raw),
        "ensembl_ids_mapped_to_hgnc_symbol": int(n_mapped),
        "ensembl_ids_unmapped_kept_as_ensembl": int(n_genes_raw - n_mapped),
        "symbols_summed_from_multiple_ensembl_ids": int(n_multi),
        "features_after_aggregation": int(agg.shape[0]),
        "filter_rule": f"raw count >= {MIN_COUNT} in at least {MIN_SAMPLES} of 6 samples",
        "features_after_filtering": int(filt.shape[0]),
        "library_sizes": {k: int(v) for k, v in lib_sizes.items()},
        "size_factors": {s: float(f) for s, f in
                         zip(dds.obs_names, np.asarray(dds.obs["size_factors"]).ravel())},
        "normalization": "DESeq2 median-of-ratios (size factors)",
        "test": "DESeq2 negative-binomial Wald test, design ~group, contrast DMD vs healthy",
        "multiple_testing": "Benjamini-Hochberg over all tested genes (independent filtering disabled)",
        "pydeseq2_version": pydeseq2.__version__,
        "n_bh_significant": int(len(sig)),
        "n_bh_significant_up_in_dmd": n_up,
        "n_bh_significant_down_in_dmd": n_down,
        "limitation_design": (
            "Each group is a single immortalized cell line (healthy AB1190, DMD AB1071), so the "
            "three samples per group are replicates of one donor background rather than independent "
            "donors. Every differential-expression result from this design is confounded with "
            "cell-line identity. The analysis cannot attribute any difference to dystrophin "
            "deficiency as opposed to donor genotype, immortalization history, or passage. This is "
            "not n=6 independent samples."
        ),
        "limitation_scope": (
            "Transcript abundance is not pump activity and not calcium flux. This dataset cannot "
            "show that sarcoplasmic reticulum calcium clearance is impaired, that SERCA function is "
            "reduced, or that the clearance-based model is correct. Permitted conclusions concern "
            "transcript levels of the named genes in these two cell lines."
        ),
    }
    with open(os.path.join(out, "de_summary.json"), "w") as fh:
        json.dump(summary, fh, indent=2, sort_keys=True)

    # ---------------- figure ----------------
    plotd = targets[targets["status"] == "tested"].copy()
    plotd = plotd.set_index("gene").reindex([g for g in TARGET_GENES if g in set(plotd["gene"])])
    colors = []
    for g in plotd.index:
        c = TARGET_SET[g]
        if "fibrillin" in c:
            colors.append("#2b6cb0")
        elif "ECM partner" in c:
            colors.append("#4299e1")
        elif "SERCA" in c or "SR calcium" in c or "calmodulin" in c:
            colors.append("#dd6b20")
        elif "competing model" in c:
            colors.append("#38a169")
        else:
            colors.append("#718096")
    fig, ax = plt.subplots(figsize=(8, 0.33 * len(plotd) + 2))
    y = np.arange(len(plotd))
    ax.barh(y, plotd["log2_fold_change"], color=colors, edgecolor="black", linewidth=0.4)
    ax.set_yticks(y)
    ax.set_yticklabels(
        [g + (" *" if plotd.loc[g, "significant_bh_0.05"] else "") for g in plotd.index],
        fontsize=9,
    )
    ax.invert_yaxis()
    ax.axvline(0, color="black", linewidth=0.8)
    ax.set_xlabel("log2 fold change, DMD relative to healthy (DESeq2)")
    ax.set_title("GSE299627 target genes, DMD (AB1071) vs healthy (AB1190) myoblasts\n"
                 "* BH q < 0.05. One cell line per group: results confounded with cell line.",
                 fontsize=10)
    handles = [
        plt.Rectangle((0, 0), 1, 1, color="#2b6cb0"),
        plt.Rectangle((0, 0), 1, 1, color="#4299e1"),
        plt.Rectangle((0, 0), 1, 1, color="#dd6b20"),
        plt.Rectangle((0, 0), 1, 1, color="#38a169"),
        plt.Rectangle((0, 0), 1, 1, color="#718096"),
    ]
    ax.legend(handles, ["fibrillin", "LTBP / ECM partner", "SR calcium handling",
                        "sarcolemmal entry (competing)", "other"],
              fontsize=8, loc="lower left")
    fig.tight_layout()
    fig.savefig(os.path.join(out, "target_genes_log2fc.png"), dpi=150)
    plt.close(fig)

    # ---------------- environment ----------------
    import scipy, statsmodels, anndata, formulaic
    env = [
        f"python_version: {sys.version.split()[0]}",
        f"python_implementation: {platform.python_implementation()}",
        f"operating_system: {platform.platform()}",
        f"machine: {platform.machine()}",
        "",
        "third_party_packages (exact versions, as imported by analysis.py):",
        f"  numpy=={np.__version__}",
        f"  pandas=={pd.__version__}",
        f"  requests=={requests.__version__}",
        f"  matplotlib=={matplotlib.__version__}",
        f"  pydeseq2=={pydeseq2.__version__}",
        f"  scipy=={scipy.__version__}",
        f"  statsmodels=={statsmodels.__version__}",
        f"  anndata=={anndata.__version__}",
        f"  formulaic=={formulaic.__version__}",
        "",
        "standard library used: argparse, gzip, hashlib, io, json, os, platform, sys, tarfile",
        "statistical engine: DESeq2 model as implemented in PyDESeq2 (median-of-ratios "
        "normalization, negative-binomial GLM, Wald test, Benjamini-Hochberg adjustment)",
    ]
    with open(os.path.join(out, "environment.txt"), "w") as fh:
        fh.write("\n".join(env) + "\n")

    with open(os.path.join(out, "run_log.txt"), "w") as fh:
        fh.write("\n".join(log_lines) + "\n")

    with open(os.path.join(out, "input_manifest.json"), "w") as fh:
        json.dump([{k: v for k, v in r.items() if k != "freshly_downloaded"}
                   for r in input_records], fh, indent=2, sort_keys=True)

    print("DONE")


if __name__ == "__main__":
    main()
