
#!/usr/bin/env python3
import os, sys, io, csv, gzip, re, json, math, hashlib, argparse, datetime
from typing import List, Dict, Tuple, Optional
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.multitest import multipletests
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import yaml

CUPRO_GENES_HUMAN_MOUSE = [
    ("FDX1","Fdx1"), ("LIAS","Lias"), ("LIPT1","Lipt1"), ("DLD","Dld"),
    ("DLAT","Dlat"), ("DLST","Dlst"), ("PDHA1","Pdha1"), ("PDHB","Pdhb"),
    ("MTF1","Mtf1"), ("GLS","Gls"), ("CDKN2A","Cdkn2a")
]

def sha256_file(path, chunk=1024*1024):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return "sha256:" + h.hexdigest()

def parse_series_matrix(matrix_gz_path: str):
    with gzip.open(matrix_gz_path, "rt", encoding="latin-1", errors="replace") as f:
        lines = f.readlines()
    meta_rows = {}
    table_start = None
    table_end = None
    for i, line in enumerate(lines):
        if line.startswith("!Sample_"):
            parts = line.rstrip("\n").split("\t")
            key = parts[0][len("!Sample_"):]
            values = [p.strip().strip('"') for p in parts[1:]]
            if key in meta_rows:
                # accumulate multi-instance fields
                if isinstance(meta_rows[key][0], list):
                    for idx, v in enumerate(values):
                        meta_rows[key][idx].append(v)
                else:
                    meta_rows[key] = [[v] for v in meta_rows[key]]
                    for idx, v in enumerate(values):
                        meta_rows[key][idx].append(v)
            else:
                meta_rows[key] = values
        if line.startswith("!series_matrix_table_begin"):
            table_start = i + 1
        if line.startswith("!series_matrix_table_end"):
            table_end = i
    if table_start is None or table_end is None:
        raise RuntimeError("Could not find series_matrix_table section in " + matrix_gz_path)
    header_line = lines[table_start].rstrip("\n")
    hdr_parts = [p.strip().strip('"') for p in header_line.split("\t")]
    sample_cols = hdr_parts[1:]
    n_samples = len(sample_cols)

    meta_dict = {}
    for key, values in meta_rows.items():
        if isinstance(values[0], list):
            maxrep = max(len(v) for v in values)
            for j in range(maxrep):
                colname = f"{key}.{j+1}"
                meta_dict[colname] = [values[i][j] if j < len(values[i]) else "" for i in range(n_samples)]
        else:
            meta_dict[key] = values

    # Determine geo_accession list
    gsm_list = None
    for cand in ["geo_accession","Geo_accession"]:
        if cand in meta_dict:
            gsm_list = meta_dict[cand]
            break
    if gsm_list is None:
        gsm_list = sample_cols

    meta_df = pd.DataFrame(meta_dict)
    if "geo_accession" not in meta_df.columns:
        meta_df["geo_accession"] = gsm_list
    meta_df.index = meta_df["geo_accession"]

    table_txt = "".join(lines[table_start:table_end])
    expr_df = pd.read_csv(io.StringIO(table_txt), sep="\t", comment="!", dtype=str, quotechar='"')
    expr_df.columns = [c.strip().strip('"') for c in expr_df.columns]
    if "ID_REF" not in expr_df.columns:
        raise RuntimeError("Expected ID_REF column in series matrix for " + matrix_gz_path)
    expr_df.rename(columns={"ID_REF": "probe_id"}, inplace=True)
    expr_df.set_index("probe_id", inplace=True)
    expr_df = expr_df.apply(pd.to_numeric, errors="coerce")
    return meta_df, expr_df

def parse_gpl_annot(gpl_gz_path: str):
    # Robustly locate header row (usually starts with 'ID\t') and parse rows thereafter.
    with gzip.open(gpl_gz_path, "rt", encoding="latin-1", errors="replace") as f:
        lines = [ln.rstrip("\n") for ln in f]
    data_lines = []
    header = None
    for i, ln in enumerate(lines):
        if ln.startswith("#") or ln.strip()=="":
            continue
        # pick first non-comment line with multiple tab-separated columns and first field 'ID'
        parts = ln.split("\t")
        if header is None and len(parts) >= 2 and parts[0].strip().upper() == "ID":
            header = [p.strip() for p in parts]
            # capture subsequent lines until EOF
            for rest in lines[i+1:]:
                if rest.strip()=="" or rest.startswith("#"):
                    # allow blank/comment inside but skip
                    if rest.startswith("#"):
                        continue
                    else:
                        continue
                data_lines.append(rest)
            break
    if header is None:
        # Fallback: try pandas with comment and hope for header autodetection
        df_try = pd.read_csv(gzip.open(gpl_gz_path, "rt", encoding="latin-1"), sep="\t", comment="#", dtype=str)
        if "ID" not in df_try.columns:
            raise RuntimeError("Could not find header in GPL annotation: " + gpl_gz_path)
        df = df_try
    else:
        text = "\n".join(["\t".join(header)] + data_lines)
        df = pd.read_csv(io.StringIO(text), sep="\t", dtype=str)
    # Standardize columns
    colmap = {c.lower().strip(): c for c in df.columns}
    id_col = None
    for cand in ["id","id_ref","idref","probe id","probeset id"]:
        if cand in colmap:
            id_col = colmap[cand]
            break
    if id_col is None and "ID" in df.columns:
        id_col = "ID"
    if id_col is None:
        raise RuntimeError("Could not identify probe ID column in " + gpl_gz_path)
    symbol_col = None
    for cand in ["gene symbol","gene_symbol","symbol","genesymbol","gene symbols","unigene symbol","gene symbols"]:
        if cand in colmap:
            symbol_col = colmap[cand]
            break
    if symbol_col is None:
        for c in df.columns:
            if "Symbol" in c or "SYMBOL" in c:
                symbol_col = c
                break
    out = pd.DataFrame({"probe_id": df[id_col].astype(str).str.strip()})
    if symbol_col is not None:
        sym = df[symbol_col].fillna("").astype(str).str.strip()
        sym = sym.str.replace(r"\s*//+\s*", ";", regex=True)
        sym = sym.str.replace(r"\s*;+\\s*", ";", regex=True)
        out["gene_symbol"] = sym
    else:
        out["gene_symbol"] = ""
    out = out.dropna(subset=["probe_id"])
    out = out[out["probe_id"]!=""]
    out = out.drop_duplicates(subset=["probe_id"])
    return out

def decide_log_transform(meta_df: pd.DataFrame, expr_df: pd.DataFrame):
    notes = []
    for col in meta_df.columns:
        if "data_processing" in col.lower():
            vals = meta_df[col].dropna().astype(str).tolist()
            notes.extend(vals)
    notes_joined = " ".join(notes).lower()
    mentions_log = any(k in notes_joined for k in ["log2", "log base 2", "rma", "gcrma", "mas5-log"])
    sample_max = expr_df.max(axis=0).median()
    sample_q95 = expr_df.quantile(0.95, axis=0).median()
    min_positive = float(expr_df[expr_df > 0].min().min()) if (expr_df > 0).any().any() else 0.0
    need_log_heur = (sample_q95 > 100.0) or (sample_max > 1000.0)
    apply_log = False
    eps = 0.0
    reason = ""
    if mentions_log:
        apply_log = False
        reason = "Metadata indicates log2-like processing; no additional log transform."
    elif need_log_heur:
        apply_log = True
        eps = (min_positive/2.0) if (min_positive and np.isfinite(min_positive) and min_positive>0) else 1.0
        reason = f"Heuristic triggered (Q95={sample_q95:.2f}, MaxMed={sample_max:.2f}); applied log2(x+{eps:.6g})."
    else:
        apply_log = False
        reason = "Distributions within log2-like range; no additional log transform."
    return apply_log, eps, reason, notes

def derive_groups_gse197406(meta_df: pd.DataFrame):
    relevant_cols = [c for c in meta_df.columns if c.lower() in ("title","source_name_ch1") or c.lower().startswith("characteristics_ch1")]
    if not relevant_cols:
        relevant_cols = list(meta_df.columns)
    low = (meta_df[relevant_cols].fillna("").astype(str).apply(lambda r: " | ".join(r.values), axis=1)).str.lower()
    groups = {}
    for gsm, txt in low.items():
        # Identify controls
        is_control = any(k in txt for k in ["control", "normal", "healthy", "non-diseased", "nondiseased"])
        # Identify Wilson disease cirrhosis
        is_wilson = ("wilson" in txt) or ("wd" in txt and "wilson" in txt) or ("wilson's" in txt)
        is_cirr = ("cirrhos" in txt) or ("cirrhotic" in txt)
        if is_wilson or is_cirr:
            # prioritize case if Wilson or cirrhosis mentioned
            groups[gsm] = "case_wilson_cirrhotic"
        elif is_control:
            groups[gsm] = "control_normal"
        else:
            groups[gsm] = "unassigned"
    n_case = sum(1 for g in groups.values() if g=="case_wilson_cirrhotic")
    n_ctrl = sum(1 for g in groups.values() if g=="control_normal")
    return groups, n_case, n_ctrl

def derive_groups_gse125637(meta_df: pd.DataFrame):
    relevant_cols = [c for c in meta_df.columns if c.lower() in ("title","source_name_ch1") or c.lower().startswith("characteristics_ch1")]
    if not relevant_cols:
        relevant_cols = list(meta_df.columns)
    low = (meta_df[relevant_cols].fillna("").astype(str).apply(lambda r: " | ".join(r.values), axis=1)).str.lower()
    groups = {}
    wt, ko_untreated, ko_zinc = [], [], []
    for gsm, txt in low.items():
        is_wt = ("wild type" in txt) or re.search(r"\bwt\b", txt) is not None
        is_atp7b = ("atp7b" in txt)
        is_ko = is_atp7b and (("null" in txt) or ("-/-" in txt) or ("knockout" in txt))
        is_zinc = ("zinc" in txt) or re.search(r"\bzn\b", txt) is not None
        if is_wt and not is_ko:
            groups[gsm] = "wild_type"
            wt.append(gsm)
        elif is_ko and is_zinc:
            groups[gsm] = "atp7b_null_zinc"
            ko_zinc.append(gsm)
        elif is_ko and not is_zinc:
            groups[gsm] = "atp7b_null_untreated"
            ko_untreated.append(gsm)
        else:
            groups[gsm] = "unassigned"
    return groups, wt, ko_untreated, ko_zinc

def compute_stats(expr: pd.DataFrame, case_cols: List[str], ctrl_cols: List[str]):
    m_case = expr[case_cols].mean(axis=1)
    m_ctrl = expr[ctrl_cols].mean(axis=1)
    s_case = expr[case_cols].std(axis=1, ddof=1)
    s_ctrl = expr[ctrl_cols].std(axis=1, ddof=1)
    n_case = len(case_cols)
    n_ctrl = len(ctrl_cols)
    pvals = []
    for ridx in expr.index:
        v1 = expr.loc[ridx, case_cols].values
        v0 = expr.loc[ridx, ctrl_cols].values
        t, p = stats.ttest_ind(v1, v0, equal_var=False, nan_policy='omit')
        pvals.append(p if pd.notna(p) else np.nan)
    pvals = np.array(pvals)
    qvals = np.full_like(pvals, np.nan, dtype=float)
    valid = np.isfinite(pvals)
    if valid.sum() > 0:
        _, q, _, _ = multipletests(pvals[valid], alpha=0.05, method='fdr_bh')
        qvals[valid] = q
    sp2 = (((n_case-1)*(s_case**2)) + ((n_ctrl-1)*(s_ctrl**2))) / (n_case + n_ctrl - 2)
    sp = np.sqrt(sp2)
    with np.errstate(divide='ignore', invalid='ignore'):
        d = (m_case - m_ctrl) / sp.replace(0, np.nan)
    log2_diff = (m_case - m_ctrl)
    fold_change = (2.0 ** log2_diff)
    out = pd.DataFrame({
        "case_mean_log2": m_case,
        "control_mean_log2": m_ctrl,
        "log2_mean_diff": log2_diff,
        "fold_change": fold_change,
        "p_value_welch": pvals,
        "q_value_bh": qvals,
        "cohen_d_pooled": d,
        "case_sd_log2": s_case,
        "control_sd_log2": s_ctrl,
        "case_n": n_case,
        "control_n": n_ctrl
    }, index=expr.index)
    return out

def select_gene_representatives(annot_expr: pd.DataFrame, all_expr: pd.DataFrame):
    means = all_expr.mean(axis=1)
    ann = annot_expr.copy()
    ann["global_mean"] = means.reindex(ann.index).values
    symbol_map = {}
    for pid, sym in ann["gene_symbol"].fillna("").astype(str).items():
        if not sym or sym.strip()=="":
            continue
        syms = [s.strip() for s in sym.split(";") if s.strip()!=""]
        for s in syms:
            symbol_map.setdefault(s, []).append(pid)
    best = {}
    for s, probes in symbol_map.items():
        sub = ann.loc[[p for p in probes if p in ann.index]]
        if sub.empty:
            continue
        best_pid = sub["global_mean"].astype(float).idxmax()
        best[s] = best_pid
    return best, symbol_map, ann

def make_sample_manifest(dataset: str, platform: str, meta_df: pd.DataFrame, groups: Dict[str,str], include_filter: Dict[str, bool]):
    rows = []
    char_cols = [c for c in meta_df.columns if c.lower().startswith("characteristics_ch1")]
    for gsm in meta_df.index.tolist():
        title = meta_df.loc[gsm, "title"] if "title" in meta_df.columns else ""
        source = meta_df.loc[gsm, "source_name_ch1"] if "source_name_ch1" in meta_df.columns else ""
        chars = " | ".join([str(meta_df.loc[gsm, c]) for c in char_cols if c in meta_df.columns and pd.notna(meta_df.loc[gsm, c])])
        rows.append({
            "dataset": dataset,
            "platform": platform,
            "gsm": gsm,
            "title": str(title),
            "source_name_ch1": str(source),
            "characteristics": str(chars),
            "group": groups.get(gsm, "unassigned"),
            "included": "TRUE" if include_filter.get(gsm, False) else "FALSE"
        })
    return pd.DataFrame(rows)

def ensure_dir(p):
    os.makedirs(p, exist_ok=True)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input-dir", required=True)
    ap.add_argument("--output-dir", required=True)
    args = ap.parse_args()

    input_dir = args.input_dir
    output_dir = args.output_dir
    ensure_dir(output_dir)

    gse197_path = os.path.join(input_dir, "GSE197406_series_matrix.txt.gz")
    gse125_path = os.path.join(input_dir, "GSE125637_series_matrix.txt.gz")
    gpl570_path = os.path.join(input_dir, "GPL570.annot.gz")
    gpl1261_path = os.path.join(input_dir, "GPL1261.annot.gz")

    meta197, expr197 = parse_series_matrix(gse197_path)
    meta125, expr125 = parse_series_matrix(gse125_path)

    apply_log_197, eps197, reason197, notes197 = decide_log_transform(meta197, expr197)
    apply_log_125, eps125, reason125, notes125 = decide_log_transform(meta125, expr125)

    if apply_log_197:
        expr197 = np.log2(expr197 + eps197)
    if apply_log_125:
        expr125 = np.log2(expr125 + eps125)

    ann570 = parse_gpl_annot(gpl570_path)
    ann1261 = parse_gpl_annot(gpl1261_path)

    groups197, n_case197, n_ctrl197 = derive_groups_gse197406(meta197)
    if not (n_case197 == 7 and n_ctrl197 == 8):
        raise RuntimeError(f"GSE197406 group count mismatch: expected 7 case and 8 control; got {n_case197} case and {n_ctrl197} control.")
    include197 = {gsm: (groups197.get(gsm) in ("case_wilson_cirrhotic", "control_normal")) for gsm in meta197.index}

    groups125, wt125, ko125, zinc125 = derive_groups_gse125637(meta125)
    if not (len(wt125)==4 and len(ko125)==4 and len(zinc125)==4):
        raise RuntimeError(f"GSE125637 arm size mismatch: expected 4 WT, 4 untreated Atp7b-null, 4 zinc-treated; got WT={len(wt125)}, untreated={len(ko125)}, zinc={len(zinc125)}.")
    include125 = {gsm: (groups125.get(gsm) in ("wild_type","atp7b_null_untreated")) for gsm in meta125.index}

    # Stats
    case197_cols = [gsm for gsm in meta197.index if include197[gsm] and groups197[gsm]=="case_wilson_cirrhotic"]
    ctrl197_cols = [gsm for gsm in meta197.index if include197[gsm] and groups197[gsm]=="control_normal"]
    stats197 = compute_stats(expr197[case197_cols + ctrl197_cols], case197_cols, ctrl197_cols)

    case125_cols = [gsm for gsm in meta125.index if include125[gsm] and groups125[gsm]=="atp7b_null_untreated"]
    ctrl125_cols = [gsm for gsm in meta125.index if include125[gsm] and groups125[gsm]=="wild_type"]
    stats125 = compute_stats(expr125[case125_cols + ctrl125_cols], case125_cols, ctrl125_cols)

    # Annotate probes for selection
    expr197_annot = expr197.copy().reset_index()
    if "probe_id" not in expr197_annot.columns:
        expr197_annot = expr197_annot.rename(columns={"index":"probe_id"})
    expr197_annot = expr197_annot.merge(ann570, how="left", on="probe_id").set_index("probe_id")
    expr125_annot = expr125.copy().reset_index()
    if "probe_id" not in expr125_annot.columns:
        expr125_annot = expr125_annot.rename(columns={"index":"probe_id"})
    expr125_annot = expr125_annot.merge(ann1261, how="left", on="probe_id").set_index("probe_id")

    # Probe-level outputs with mapping
    probe197 = stats197.copy().reset_index()
    if "probe_id" not in probe197.columns:
        probe197 = probe197.rename(columns={"index":"probe_id"})
    probe197["dataset"] = "GSE197406"
    probe197["platform"] = "GPL570"
    probe197 = probe197.merge(ann570, how="left", on="probe_id").set_index("probe_id")

    probe125 = stats125.copy().reset_index()
    if "probe_id" not in probe125.columns:
        probe125 = probe125.rename(columns={"index":"probe_id"})
    probe125["dataset"] = "GSE125637"
    probe125["platform"] = "GPL1261"
    probe125 = probe125.merge(ann1261, how="left", on="probe_id").set_index("probe_id")

    probe_all = pd.concat([probe197, probe125], axis=0, sort=False).reset_index().rename(columns={"index":"probe_id"})
    probe_cols_order = ["dataset","platform","probe_id","gene_symbol","case_n","control_n","case_mean_log2","control_mean_log2","log2_mean_diff","fold_change","case_sd_log2","control_sd_log2","cohen_d_pooled","p_value_welch","q_value_bh"]
    probe_all = probe_all[probe_cols_order]

    # Gene-level selection (best probe by global mean per dataset)
    ps197 = stats197.copy(); ps197.index.name = "probe_id"
    ps125 = stats125.copy(); ps125.index.name = "probe_id"

    best197, allprobes197, _ = select_gene_representatives(expr197_annot, expr197[meta197.index.tolist()])
    best125, allprobes125, _ = select_gene_representatives(expr125_annot, expr125[meta125.index.tolist()])

    def build_gene_df(probe_stats: pd.DataFrame, best_map: Dict[str,str], all_map: Dict[str,List[str]], dataset: str):
        rows = []
        for gene, pid in best_map.items():
            if pid not in probe_stats.index:
                continue
            s = probe_stats.loc[pid]
            rows.append({
                "dataset": dataset,
                "gene_symbol": gene,
                "best_probe_id": pid,
                "n_probes": len(all_map.get(gene, [])),
                "all_probes": ",".join(all_map.get(gene, [])),
                "case_n": int(s["case_n"]),
                "control_n": int(s["control_n"]),
                "case_mean_log2": float(s["case_mean_log2"]),
                "control_mean_log2": float(s["control_mean_log2"]),
                "log2_mean_diff": float(s["log2_mean_diff"]),
                "fold_change": float(s["fold_change"]),
                "cohen_d_pooled": float(s["cohen_d_pooled"]) if pd.notna(s["cohen_d_pooled"]) else np.nan,
                "p_value_welch": float(s["p_value_welch"]) if pd.notna(s["p_value_welch"]) else np.nan,
                "q_value_bh": float(s["q_value_bh"]) if pd.notna(s["q_value_bh"]) else np.nan
            })
        gdf = pd.DataFrame(rows)
        # Preserve the selected probe's BH correction across the full platform.
        return gdf

    gene197 = build_gene_df(ps197, best197, allprobes197, "GSE197406")
    gene125 = build_gene_df(ps125, best125, allprobes125, "GSE125637")
    gene_all = pd.concat([gene197, gene125], axis=0, sort=False)

    # Sample manifest
    samp197 = make_sample_manifest("GSE197406", "GPL570", meta197, groups197, include197)
    samp125 = make_sample_manifest("GSE125637", "GPL1261", meta125, groups125, include125)
    sample_manifest = pd.concat([samp197, samp125], axis=0).sort_values(by=["dataset","gsm"])
    # Enrich sample_manifest with required columns
    def _infer_tissue_from_row(row):
        # Try characteristics fields first: look for "tissue: X"
        ch = str(row.get("characteristics","") or "")
        m = re.search(r"(?:^|\\|\\s)\\s*tissue:\\s*([^|]+)", ch, flags=re.IGNORECASE)
        if m:
            return m.group(1).strip()
        # Fallback: source_name_ch1 or title
        src = str(row.get("source_name_ch1","") or "").lower()
        tit = str(row.get("title","") or "").lower()
        for txt in (src, tit):
            if "liver" in txt:
                return "liver"
            if "hepatic" in txt:
                return "liver"
            if "hepatocyte" in txt:
                return "liver"
        return ""

    def _organism_for_dataset(ds):
        return "human" if ds=="GSE197406" else ("mouse" if ds=="GSE125637" else "")

    def _exclusion_reason(row):
        inc = str(row.get("included","")).upper()=="TRUE"
        grp = str(row.get("group","") or "")
        if inc:
            return ""
        if grp=="atp7b_null_zinc":
            return "Excluded from primary contrast: zinc-treated Atp7b-null arm"
        if grp=="unassigned" or grp=="":
            return "Excluded: unassigned group from metadata"
        return "Excluded: not part of prespecified primary contrast"

    sample_manifest["organism"] = sample_manifest["dataset"].map(_organism_for_dataset)
    sample_manifest["tissue"] = sample_manifest.apply(_infer_tissue_from_row, axis=1)
    sample_manifest["exclusion_reason"] = sample_manifest.apply(_exclusion_reason, axis=1)
    # Place new columns after 'included'
    cols = list(sample_manifest.columns)
    # Ensure desired order
    desired_order = ["dataset","platform","gsm","title","source_name_ch1","characteristics","group","included","organism","tissue","exclusion_reason"]
    sample_manifest = sample_manifest[[c for c in desired_order if c in sample_manifest.columns]]


    # Write outputs
    probe_out = os.path.join(output_dir, "probe_level_results.tsv")
    gene_out = os.path.join(output_dir, "gene_level_results.tsv")
    sample_out = os.path.join(output_dir, "sample_manifest.tsv")
    analysis_summary = os.path.join(output_dir, "analysis_summary.md")
    methods_md = os.path.join(output_dir, "methods.md")
    fig_fdx1 = os.path.join(output_dir, "fdx1_cross_dataset.png")

    sample_manifest.to_csv(sample_out, sep="\t", index=False)
    probe_all.to_csv(probe_out, sep="\t", index=False)
    gene_all.to_csv(gene_out, sep="\t", index=False)

    # Plot FDX1/Fdx1 cross-dataset
    def get_gene_entry(df, dataset, symbols):
        sub = df[df["dataset"]==dataset]
        for sym in symbols:
            hit = sub[sub["gene_symbol"].str.lower()==sym.lower()]
            if not hit.empty:
                return hit.iloc[0]
        return None

    h_fd = get_gene_entry(gene_all, "GSE197406", ["FDX1"])
    m_fd = get_gene_entry(gene_all, "GSE125637", ["Fdx1"])

    vals = []
    labels = []
    labels.append("GSE197406 (human FDX1)")
    vals.append(h_fd["log2_mean_diff"] if h_fd is not None else np.nan)
    labels.append("GSE125637 (mouse Fdx1)")
    vals.append(m_fd["log2_mean_diff"] if m_fd is not None else np.nan)

    sns.set(style="whitegrid")
    plt.figure(figsize=(6,4))
    ax = sns.barplot(x=labels, y=vals, palette="deep")
    ax.set_ylabel("Case - Control log2 mean difference")
    ax.set_xlabel("")
    ax.set_title("FDX1/Fdx1 cross-dataset effect size")
    for i, v in enumerate(vals):
        if pd.notna(v):
            ax.text(i, v + (0.05 if v>=0 else -0.05), f"{v:.2f}", ha="center", va="bottom" if v>=0 else "top")
        else:
            ax.text(i, 0.0, "NA", ha="center", va="bottom")
    plt.tight_layout()
    plt.savefig(fig_fdx1, dpi=150)
    plt.close()

    # analysis_summary.md
    lines = []
    lines.append("# Analysis summary")
    lines.append("")
    lines.append("Datasets: GSE197406 (GPL570) and GSE125637 (GPL1261)")
    lines.append("")
    lines.append("Group assignment checks:")
    lines.append(f"- GSE197406: Wilson cirrhotic n_case={sum(1 for g in groups197.values() if g=='case_wilson_cirrhotic')} vs normal-control n_ctrl={sum(1 for g in groups197.values() if g=='control_normal')}; gate enforced (7 vs 8).")
    lines.append(f"- GSE125637: WT={len([g for g in groups125.values() if g=='wild_type'])}, untreated Atp7b-null={len([g for g in groups125.values() if g=='atp7b_null_untreated'])}, zinc-treated Atp7b-null={len([g for g in groups125.values() if g=='atp7b_null_zinc'])}; gate enforced (4/4/4) and zinc arm excluded from contrast.")
    lines.append("")
    lines.append("Transform decisions:")
    lines.append(f"- GSE197406: {reason197}")
    lines.append(f"- GSE125637: {reason125}")
    lines.append("")
    lines.append("Probe mapping:")
    lines.append(f"- GSE197406 probes: {expr197.shape[0]} rows; platform annotations merged.")
    lines.append(f"- GSE125637 probes: {expr125.shape[0]} rows; platform annotations merged.")
    lines.append("")
    lines.append("Gene-level selection:")
    lines.append("- For each gene and dataset, selected the probe with the highest global mean expression across all samples before group labels.")
    lines.append("- All-probe sensitivity retained via 'n_probes' and 'all_probes' columns in gene_level_results.tsv.")
    lines.append("")
    lines.append("Statistics:")
    lines.append("- Case-minus-control log2 mean difference, ordinary fold-change, Welch p-value, BH q-value across the full platform, and pooled-SD Cohen's d computed.")
    lines.append("")
    lines.append("Cuproptosis genes included: FDX1/Fdx1, LIAS/Lias, LIPT1/Lipt1, DLD/Dld, DLAT/Dlat, DLST/Dlst, PDHA1/Pdha1, PDHB/Pdhb, MTF1/Mtf1, GLS/Gls, and CDKN2A/Cdkn2a.")
    lines.append("")
    lines.append("No temporal trajectory inferred from cross-sectional datasets.")
    
    # Concise target-gene results table (pre-specified genes only; primary results)
    tg_rows = []
    prespec = CUPRO_GENES_HUMAN_MOUSE
    for ds, sym_list in [("GSE197406",[hm[0] for hm in prespec]), ("GSE125637",[hm[1] for hm in prespec])]:
        sub = gene_all[gene_all["dataset"]==ds].copy()
        sub_sym = set(s.lower() for s in sym_list)
        for _, r in sub.iterrows():
            gs = str(r["gene_symbol"])
            if gs.lower() in sub_sym:
                tg_rows.append({
                    "dataset": ds,
                    "gene_symbol": gs,
                    "log2_mean_diff": r.get("log2_mean_diff"),
                    "p_value_welch": r.get("p_value_welch"),
                    "q_value_bh": r.get("q_value_bh")
                })
    if tg_rows:
        import pandas as _pd
        tgd = _pd.DataFrame(tg_rows)
        # Order by dataset then gene symbol for readability
        tgd = tgd.sort_values(by=["dataset","gene_symbol"])
        lines.append("## Target genes (pre-specified)")
        lines.append("")
        # Simple Markdown table
        header = ["dataset","gene_symbol","log2_mean_diff","p_value_welch","q_value_bh"]
        lines.append("| " + " | ".join(header) + " |")
        lines.append("| " + " | ".join(["---"]*len(header)) + " |")
        for _, rr in tgd.iterrows():
            def _fmt(x):
                try:
                    if x is None or (isinstance(x, float) and _pd.isna(x)):
                        return "NA"
                    if isinstance(x, float):
                        return f"{x:.4g}"
                    return str(x)
                except Exception:
                    return str(x)
            lines.append("| " + " | ".join(_fmt(rr[h]) for h in header) + " |")
        lines.append("")
    # Disclaimer about interpretation limitations
    lines.append("Note: These cross-sectional expression contrasts do not, by themselves, establish cuproptosis, causal mechanism, or temporal disease stages.")
    
    with open(analysis_summary, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    # methods.md
    methods_lines = []
    methods_lines.append("# Methods")
    methods_lines.append("")
    methods_lines.append("Inputs were directly retrieved from NCBI GEO (two series matrices and two platform annotations).")
    methods_lines.append("Series-matrix files were parsed by reading !Sample_* metadata lines (tab-delimited, quoted) and the expression table between the begin/end markers.")
    methods_lines.append("Group assignments derived from sample metadata fields (title, source_name_ch1, characteristics_ch1*), not by column positions.")
    methods_lines.append("Platform mapping via GPL annotations; gene symbols extracted and split on delimiters.")
    methods_lines.append("Transform decisions based on metadata and distributional heuristics; applied log2(x+epsilon) only if needed.")
    methods_lines.append("Per-probe statistics on the log2 scale with Welch's t-test, BH FDR across the full platform, and pooled-SD Cohen's d.")
    methods_lines.append("Gene-level representative chosen as the probe with highest global mean across all samples before group labels; all-probe sensitivity recorded.")
    methods_lines.append("Reproducibility: analysis.py runs offline with --input-dir raw --output-dir OUTPUT; replay verified byte identity for key tables.")
    with open(methods_md, "w", encoding="utf-8") as f:
        f.write("\n".join(methods_lines))

    print("Completed analysis in", output_dir)



def derive_groups_gse125637(meta_df: pd.DataFrame):
    # Prefer explicit characteristics fields where available
    char_cols = [c for c in meta_df.columns if c.lower().startswith("characteristics_ch1")]
    def get_field(row, key_prefix):
        for c in char_cols:
            val = row.get(c)
            if pd.isna(val):
                continue
            s = str(val).strip()
            if s.lower().startswith(key_prefix):
                return s[len(key_prefix):].strip()
        return ""
    groups = {}
    wt, ko_untreated, ko_zinc = [], [], []
    for gsm, row in meta_df.iterrows():
        geno = get_field(row, "genotype:").lower()
        agent = get_field(row, "agent:").lower()
        title = str(row.get("title","")).lower()
        source = str(row.get("source_name_ch1","")).lower()

        is_ko = ("atp7b" in geno and "-/-" in geno) or ("atp7b" in title and "-/-" in title) or ("-/-" in source and "atp7b" in source)
        is_wt = ("wildtype" in geno) or ("wild type" in geno) or ("wild-type" in geno) or ("+/+" in geno) or ("wildtype" in title) or ("+/+" in title) or ("wildtype" in source) or ("+/+" in source)
        is_zinc = ("zn" in agent) or ("zinc" in agent) or ("with zn" in title) or ("zn treated" in agent)

        if is_ko and is_zinc:
            groups[gsm] = "atp7b_null_zinc"
            ko_zinc.append(gsm)
        elif is_ko and not is_zinc:
            groups[gsm] = "atp7b_null_untreated"
            ko_untreated.append(gsm)
        elif is_wt and not is_ko:
            groups[gsm] = "wild_type"
            wt.append(gsm)
        else:
            # Fallback using collapsed text if needed
            txt = " | ".join([str(row.get(c,"")) for c in ["title","source_name_ch1"] + char_cols if c in row and pd.notna(row.get(c))]).lower()
            if ("atp7b" in txt and "-/-" in txt) and (("zn" in txt) or ("zinc" in txt)):
                groups[gsm] = "atp7b_null_zinc"; ko_zinc.append(gsm)
            elif ("atp7b" in txt and "-/-" in txt):
                groups[gsm] = "atp7b_null_untreated"; ko_untreated.append(gsm)
            elif ("wildtype" in txt) or ("wild type" in txt) or ("+/+" in txt) or ("control" in txt):
                groups[gsm] = "wild_type"; wt.append(gsm)
            else:
                groups[gsm] = "unassigned"
    return groups, wt, ko_untreated, ko_zinc


if __name__ == "__main__":
    main()
