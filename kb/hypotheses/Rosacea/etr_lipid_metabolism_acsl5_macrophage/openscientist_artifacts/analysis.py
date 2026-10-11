#!/usr/bin/env python3
"""
Deterministic computational replication for hypothesis
`etr_lipid_metabolism_acsl5_macrophage` (Disease: Rosacea).

Prespecified contrast: erythematotelangiectatic rosacea (ETR) vs healthy
control in GEO series GSE65914 (Affymetrix HG-U133 Plus 2.0 / GPL570) for the
lipid-metabolism hub genes ACSL5 and ACADVL, the PPAR/fatty-acid genes PPARG
and CPT1A, and the macrophage markers CD68, CD163 and CD86. Within ETR samples,
Spearman correlation of ACSL5 with each macrophage marker.

The script is standalone and deterministic. It downloads (or reuses from a
cache) the exact GEO inputs and regenerates all tabular outputs with no LLM.

Usage:
    python analysis.py --output-dir <dir> [--cache-dir <dir>]

Third-party deps: numpy, pandas, scipy, statsmodels, requests (+ stdlib).
"""
import argparse
import gzip
import hashlib
import os

import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.multitest import multipletests

# ----------------------------------------------------------------------------
# Fixed inputs (canonical, credential-free URLs)
# ----------------------------------------------------------------------------
INPUTS = {
    "series_matrix": {
        "filename": "GSE65914_series_matrix.txt.gz",
        "url": "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE65nnn/GSE65914/matrix/GSE65914_series_matrix.txt.gz",
        "sha256": "70566f613ad356b7fc38aca9892a2aada43c2a48db821c09fa10d0c5977a14b4",
    },
    "platform_annot": {
        "filename": "GPL570.annot.gz",
        "url": "https://ftp.ncbi.nlm.nih.gov/geo/platforms/GPLnnn/GPL570/annot/GPL570.annot.gz",
        "sha256": "d7cd44352127b1e34f3a720ebea86093ef255a38f1612a85a2962b71bde8f394",
    },
}

# Prespecified target genes (order is fixed and deterministic).
LIPID_GENES = ["ACSL5", "ACADVL", "PPARG", "CPT1A"]
MACROPHAGE_MARKERS = ["CD68", "CD163", "CD86"]
TARGET_GENES = LIPID_GENES + MACROPHAGE_MARKERS

# Prespecified group labels (exact GSE65914 `group:` characteristic values).
GROUP_ETR = "erythematotelangiectatic rosacea (ETR)"
GROUP_CTRL = "Healthy volunteer"


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def ensure_input(key, cache_dir):
    """Return path to a raw input, reusing the cache if present else downloading."""
    meta = INPUTS[key]
    path = os.path.join(cache_dir, meta["filename"])
    if not os.path.exists(path):
        import requests  # local import; only needed when downloading
        os.makedirs(cache_dir, exist_ok=True)
        r = requests.get(meta["url"], timeout=600)
        r.raise_for_status()
        with open(path, "wb") as fh:
            fh.write(r.content)
    got = sha256_file(path)
    if got != meta["sha256"]:
        raise RuntimeError(
            "checksum mismatch for %s: expected %s got %s"
            % (meta["filename"], meta["sha256"], got)
        )
    return path


def parse_series_matrix(path):
    """Parse a GEO series matrix into (sample_meta_df, expr_df[probe x sample])."""
    sample_accessions = None
    group_char = None
    titles = None
    sources = None
    organisms = None
    header = None
    data = {}
    with gzip.open(path, "rt", encoding="utf-8", errors="replace") as f:
        in_tab = False
        for line in f:
            if line.startswith("!Sample_geo_accession"):
                sample_accessions = [x.strip('"') for x in line.rstrip("\n").split("\t")[1:]]
            elif line.startswith("!Sample_title"):
                titles = [x.strip('"') for x in line.rstrip("\n").split("\t")[1:]]
            elif line.startswith("!Sample_source_name_ch1"):
                sources = [x.strip('"') for x in line.rstrip("\n").split("\t")[1:]]
            elif line.startswith("!Sample_organism_ch1"):
                organisms = [x.strip('"') for x in line.rstrip("\n").split("\t")[1:]]
            elif line.startswith("!Sample_characteristics_ch1"):
                vals = [x.strip('"') for x in line.rstrip("\n").split("\t")[1:]]
                if vals and vals[0].lower().startswith("group:"):
                    group_char = vals
            elif line.startswith("!series_matrix_table_begin"):
                in_tab = True
                continue
            elif line.startswith("!series_matrix_table_end"):
                break
            elif in_tab:
                if header is None:
                    header = [x.strip('"') for x in line.rstrip("\n").split("\t")]
                    continue
                parts = line.rstrip("\n").split("\t")
                probe = parts[0].strip('"')
                row = []
                for x in parts[1:]:
                    x = x.strip('"')
                    if x in ("", "null", "NA", "NaN"):
                        row.append(np.nan)
                    else:
                        row.append(float(x))
                data[probe] = row
    expr = pd.DataFrame.from_dict(data, orient="index", columns=header[1:])
    groups = [g.split(":", 1)[1].strip() for g in group_char]
    meta = pd.DataFrame(
        {
            "accession": sample_accessions,
            "dataset": "GSE65914",
            "organism": organisms,
            "tissue": sources,
            "title": titles,
            "source_group": groups,
        }
    )
    return meta, expr


def parse_annotation(path, genes):
    """Return {gene: [probe_ids...]} mapping using the curated `Gene symbol` column.
    Probes annotated to multiple genes ('///'-joined) match if the gene appears."""
    gset = set(genes)
    mapping = {g: [] for g in genes}
    with gzip.open(path, "rt", encoding="utf-8", errors="replace") as f:
        in_tab = False
        header = None
        sym_idx = None
        for line in f:
            if line.startswith("!platform_table_begin"):
                in_tab = True
                continue
            if line.startswith("!platform_table_end"):
                break
            if in_tab:
                if header is None:
                    header = line.rstrip("\n").split("\t")
                    sym_idx = header.index("Gene symbol")
                    continue
                parts = line.rstrip("\n").split("\t")
                probe = parts[0]
                syms = parts[sym_idx].split("///") if len(parts) > sym_idx else []
                syms = {s.strip() for s in syms}
                hit = gset & syms
                for g in hit:
                    mapping[g].append(probe)
    # deterministic probe order
    for g in mapping:
        mapping[g] = sorted(mapping[g])
    return mapping


def cohens_d(a, b):
    """Cohen's d = (mean_a - mean_b) / pooled_sd, pooled over both groups."""
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    na, nb = len(a), len(b)
    va = a.var(ddof=1)
    vb = b.var(ddof=1)
    sp = np.sqrt(((na - 1) * va + (nb - 1) * vb) / (na + nb - 2))
    if sp == 0:
        return np.nan
    return (a.mean() - b.mean()) / sp


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--cache-dir", default=None)
    args = ap.parse_args()

    out_dir = args.output_dir
    cache_dir = args.cache_dir if args.cache_dir else os.path.join(out_dir, "raw")
    os.makedirs(out_dir, exist_ok=True)

    sm_path = ensure_input("series_matrix", cache_dir)
    an_path = ensure_input("platform_annot", cache_dir)

    meta, expr = parse_series_matrix(sm_path)
    mapping = parse_annotation(an_path, TARGET_GENES)

    # --- sample inclusion / exclusion -------------------------------------
    def assign(g):
        if g == GROUP_ETR:
            return "ETR", ""
        if g == GROUP_CTRL:
            return "control", ""
        return "excluded", "not part of prespecified ETR-vs-healthy-control contrast"

    assigned = meta["source_group"].map(lambda g: assign(g)[0])
    reason = meta["source_group"].map(lambda g: assign(g)[1])
    samples = meta.copy()
    samples["assigned_group"] = assigned.values
    samples["exclusion_reason"] = reason.values
    samples = samples.sort_values("accession").reset_index(drop=True)
    samples.to_csv(os.path.join(out_dir, "samples.csv"), index=False)

    etr_ids = samples.loc[samples.assigned_group == "ETR", "accession"].tolist()
    ctrl_ids = samples.loc[samples.assigned_group == "control", "accession"].tolist()

    # --- gene-level expression (mean of mapped probes, log2 scale) --------
    gene_expr = {}
    probe_rows = []
    for g in TARGET_GENES:
        probes = [p for p in mapping[g] if p in expr.index]
        for p in probes:
            probe_rows.append({"gene": g, "probe": p})
        sub = expr.loc[probes]
        gene_expr[g] = sub.mean(axis=0)  # mean across probes per sample
    gene_expr = pd.DataFrame(gene_expr).T  # gene x sample
    pd.DataFrame(probe_rows).to_csv(
        os.path.join(out_dir, "probe_gene_map.csv"), index=False
    )

    # --- contrast: ETR vs control -----------------------------------------
    rows = []
    for g in TARGET_GENES:
        e = gene_expr.loc[g, etr_ids].astype(float).values
        c = gene_expr.loc[g, ctrl_ids].astype(float).values
        m_e, m_c = e.mean(), c.mean()
        log2_diff = m_e - m_c  # values already on log2 scale
        fold_change = float(2.0 ** log2_diff)
        t, p = stats.ttest_ind(e, c, equal_var=False)  # Welch's t-test
        d = cohens_d(e, c)
        rows.append(
            {
                "dataset": "GSE65914",
                "gene": g,
                "gene_class": "lipid_metabolism" if g in LIPID_GENES else "macrophage_marker",
                "comparison": "ETR_vs_healthy_control",
                "n_ETR": len(e),
                "n_control": len(c),
                "mean_ETR_log2": m_e,
                "mean_control_log2": m_c,
                "log2_mean_diff": log2_diff,
                "fold_change": fold_change,
                "t_statistic": float(t),
                "p_value": float(p),
                "cohens_d": float(d),
            }
        )
    res = pd.DataFrame(rows)
    # BH-FDR across the prespecified gene set
    res["q_value_BH"] = multipletests(res["p_value"].values, method="fdr_bh")[1]
    # deterministic column order
    res = res[
        [
            "dataset", "gene", "gene_class", "comparison", "n_ETR", "n_control",
            "mean_ETR_log2", "mean_control_log2", "log2_mean_diff", "fold_change",
            "t_statistic", "p_value", "q_value_BH", "cohens_d",
        ]
    ]
    res.to_csv(os.path.join(out_dir, "gene_results.csv"), index=False)

    # --- Spearman: ACSL5 vs macrophage markers within ETR -----------------
    srows = []
    acsl5_etr = gene_expr.loc["ACSL5", etr_ids].astype(float).values
    for mk in MACROPHAGE_MARKERS:
        mk_etr = gene_expr.loc[mk, etr_ids].astype(float).values
        rho, p = stats.spearmanr(acsl5_etr, mk_etr)
        srows.append(
            {
                "dataset": "GSE65914",
                "group": "ETR",
                "n": len(etr_ids),
                "gene_x": "ACSL5",
                "gene_y": mk,
                "spearman_rho": float(rho),
                "p_value": float(p),
            }
        )
    scorr = pd.DataFrame(srows)
    scorr["q_value_BH"] = multipletests(scorr["p_value"].values, method="fdr_bh")[1]
    scorr.to_csv(
        os.path.join(out_dir, "spearman_acsl5_macrophage.csv"), index=False
    )

    print("Wrote outputs to", out_dir)
    print(res.to_string(index=False))
    print(scorr.to_string(index=False))


if __name__ == "__main__":
    main()
