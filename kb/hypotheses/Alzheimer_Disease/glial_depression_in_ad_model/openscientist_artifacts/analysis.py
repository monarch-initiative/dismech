#!/usr/bin/env python3
# analysis.py - Deterministic replication analysis for hypothesis
# glial_depression_in_ad_model (He et al. 2026 Nat Med, PMID 42778763).
# Standalone: retrieves/reuses the Supplementary Data zip and regenerates all
# tabular outputs with no LLM. Only re-analyses published derived scores.
import argparse, os, io, json, hashlib, zipfile, platform, sys
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.multitest import multipletests

ZIP_NAME = "41591_2025_4128_MOESM3_ESM.zip"
ZIP_URL = ("https://media.springernature.com/original/springer-static/esm/"
           "art%3A10.1038%2Fs41591-025-04128-1/MediaObjects/"
           "41591_2025_4128_MOESM3_ESM.zip")
EXPECTED_SHA256 = "27901070f322dff0e1283343d61de6f80b656bc41dbc7ea0efa9e8b8a1851865"

# Prespecified gene sets (unfolded protein response / ER stress; inflammatory signalling)
UPR_SET = ["HSPA5","DDIT3","ATF4","ATF6","XBP1","ERN1","EIF2AK3","HSP90B1",
           "PDIA4","PDIA6","CALR","DNAJB9","SEL1L","HERPUD1","MANF"]
INFLAM_SET = ["NFKBIA","IL1B","IL6","CXCL8","TNF","STAT3","SOCS3","C3",
              "CHI3L1","SERPINA3","CD44"]

def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()

def get_zip(cache_dir):
    path = os.path.join(cache_dir, ZIP_NAME)
    if os.path.exists(path):
        data = open(path, "rb").read()
    else:
        import requests
        os.makedirs(cache_dir, exist_ok=True)
        r = requests.get(ZIP_URL, timeout=600)
        r.raise_for_status()
        data = r.content
        open(path, "wb").write(data)
    return path, data

def read_sheet(zip_bytes, member, sheet):
    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as zf:
        raw = zf.read(member)
    return pd.read_excel(io.BytesIO(raw), sheet_name=sheet, header=None,
                         engine="openpyxl")

def norm_gene(x):
    if x is None: return None
    s = str(x).strip()
    if s == "" or s.lower() == "nan": return None
    return s.upper()

def parse_single_block(df):
    # find the header row containing 'Gene Name' in column 0
    hdr = None
    for i in range(min(20, len(df))):
        if str(df.iloc[i, 0]).strip() == "Gene Name":
            hdr = i; break
    if hdr is None:
        raise ValueError("Gene Name header not found")
    sub = df.iloc[hdr+1:, 0:5].copy()
    sub.columns = ["gene","score","log2FC","pval","padj"]
    sub["gene"] = sub["gene"].map(norm_gene)
    sub = sub.dropna(subset=["gene"])
    sub = sub[~sub["gene"].isin(["GENE NAME"])]
    for c in ["score","log2FC","pval","padj"]:
        sub[c] = pd.to_numeric(sub[c], errors="coerce")
    return sub.reset_index(drop=True)

def parse_supp7_astro(df):
    # row index 2 holds cell-type labels per 5-col block
    label_row = None
    for i in range(min(10, len(df))):
        if str(df.iloc[i, 0]).strip() == "Astrocyte":
            label_row = i; break
    if label_row is None:
        raise ValueError("Astrocyte label not found in Supp7")
    col = 0  # Astrocyte block starts at column 0
    # header row is label_row+1 (Gene Name ...)
    sub = df.iloc[label_row+2:, col:col+5].copy()
    sub.columns = ["gene","score","log2FC","pval","padj"]
    sub["gene"] = sub["gene"].map(norm_gene)
    sub = sub.dropna(subset=["gene"])
    sub = sub[~sub["gene"].isin(["GENE NAME"])]
    for c in ["score","log2FC","pval","padj"]:
        sub[c] = pd.to_numeric(sub[c], errors="coerce")
    return sub.reset_index(drop=True)

def load_pac(zip_bytes, sheet):
    member = "supplementary_data/Supplementary_Data_6.xlsx"
    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as zf:
        raw = zf.read(member)
    df = pd.read_excel(io.BytesIO(raw), sheet_name=sheet, engine="openpyxl")
    df = df.rename(columns={df.columns[0]: "donor"})
    df["donor"] = df["donor"].astype(str).str.strip()
    df = df.set_index("donor")
    df = df.apply(pd.to_numeric, errors="coerce")
    return df

def cohens_d_paired(diff):
    diff = np.asarray(diff, dtype=float)
    sd = diff.std(ddof=1)
    if sd == 0 or np.isnan(sd):
        return np.nan
    return diff.mean()/sd

def fold_stats(m1, m2):
    a1, a2 = abs(m1), abs(m2)
    if a1 == 0 or a2 == 0:
        return np.nan, np.nan
    fc = a1/a2
    return fc, np.log2(fc)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--cache-dir", default=None)
    args = ap.parse_args()
    out = args.output_dir
    os.makedirs(out, exist_ok=True)
    cache = args.cache_dir if args.cache_dir else os.path.join(out, "raw")
    os.makedirs(cache, exist_ok=True)

    zip_path, zip_bytes = get_zip(cache)
    got_sha = sha256_bytes(zip_bytes)

    # ---- Load PAC score matrices (Supp Data 6) ----
    dep = load_pac(zip_bytes, "Avg. PAC scores DepressionMood")
    adp = load_pac(zip_bytes, "Avg. PAC scores AD progression")
    subclasses = sorted([c for c in dep.columns if c in adp.columns])
    common = sorted(set(dep.index) & set(adp.index))

    # ---- Analysis 1: subclass correlation Depression vs AD-progression ----
    rows = []
    for sc in subclasses:
        x = dep.loc[common, sc].astype(float)
        y = adp.loc[common, sc].astype(float)
        mask = (~x.isna()) & (~y.isna())
        xv, yv = x[mask].values, y[mask].values
        n = int(mask.sum())
        if n >= 3 and np.std(xv) > 0 and np.std(yv) > 0:
            rho, p = stats.spearmanr(xv, yv)
        else:
            rho, p = np.nan, np.nan
        m1, m2 = float(np.mean(xv)), float(np.mean(yv))
        fc, l2 = fold_stats(m1, m2)
        d = cohens_d_paired(xv - yv)
        rows.append(dict(dataset="Supp6_PAC", gene=sc,
            comparison="DepressionPAC_vs_ADprogressionPAC_spearman",
            n1=n, n2=n, mean1=m1, mean2=m2, log2_mean_diff=l2,
            fold_change=fc, test_statistic=rho, p_value=p, cohens_d=d))
    gr = pd.DataFrame(rows)
    valid = gr["p_value"].notna()
    gr["q_value"] = np.nan
    if valid.sum() > 0:
        gr.loc[valid, "q_value"] = multipletests(gr.loc[valid, "p_value"],
            method="fdr_bh")[1]
    gr = gr[["dataset","gene","comparison","n1","n2","mean1","mean2",
             "log2_mean_diff","fold_change","test_statistic","p_value",
             "q_value","cohens_d"]].sort_values("gene").reset_index(drop=True)
    gr.to_csv(os.path.join(out, "gene_results.csv"), index=False)
    gr.to_csv(os.path.join(out, "subclass_correlation.csv"), index=False)

    # ---- SHAP ranking (Supp Data 6, DepressionMood) ----
    shap = load_pac(zip_bytes, "SHAP values DepressionMood")
    shp = (shap[subclasses].abs().mean(axis=0)
           .rename("mean_abs_shap").reset_index()
           .rename(columns={"index":"subclass"}))
    shp = shp.sort_values("mean_abs_shap", ascending=False).reset_index(drop=True)
    shp["rank"] = np.arange(1, len(shp)+1)
    shp.to_csv(os.path.join(out, "shap_ranking.csv"), index=False)

    # ---- Load DEG gene sets ----
    m3 = "supplementary_data/Supplementary_Data_3.xlsx"
    dep_astro = parse_single_block(read_sheet(zip_bytes, m3,
        "Depression PAC DEGs in Astrocyt"))
    wif1_up = parse_single_block(read_sheet(zip_bytes, m3,
        "Upregulated genes in AD-Depr.-A"))
    oli_down = parse_single_block(read_sheet(zip_bytes, m3,
        "Downregulated genes in AD-Depr."))
    m7 = "supplementary_data/Supplementary_Data_7.xlsx"
    ad_astro = parse_supp7_astro(read_sheet(zip_bytes, m7, "AD PAC DEGs"))

    dep_astro_genes = set(dep_astro["gene"])
    wif1_up_genes = set(wif1_up["gene"])
    oli_down_genes = set(oli_down["gene"])
    ad_astro_genes = set(ad_astro["gene"])

    # explicit gene universe = union of all loaded DEG-table genes + prespecified sets
    universe = (dep_astro_genes | wif1_up_genes | oli_down_genes |
                ad_astro_genes | set(UPR_SET) | set(INFLAM_SET))
    N_deg_union = len(universe)
    N_genomic = 19000  # approx protein-coding background (sensitivity)

    def enrich(deg_name, deg_set, set_name, gene_set, N, usource):
        gs = set(gene_set) & universe if usource == "deg_union" else set(gene_set)
        setN = len(gs)
        dN = len(deg_set)
        k = len(deg_set & set(gene_set))
        # contingency: [[k, setN-k],[dN-k, N-dN-setN+k]]
        a = k; b = setN - k; c = dN - k; d = N - dN - setN + k
        table = [[a, b], [c, d]]
        try:
            odds, p = stats.fisher_exact(table, alternative="greater")
        except Exception:
            odds, p = np.nan, np.nan
        overlap_genes = ";".join(sorted(deg_set & set(gene_set)))
        return dict(universe_source=usource, universe_N=N,
            deg_set=deg_name, deg_N=dN, gene_set=set_name, set_N=setN,
            overlap_k=k, odds_ratio=odds, p_value=p, overlap_genes=overlap_genes)

    deg_sets = [("Supp3_DepressionAstro_DEGs", dep_astro_genes),
                ("Supp3_AstroWIF1_up", wif1_up_genes)]
    gene_sets = [("UPR_ERstress", UPR_SET), ("Inflammatory", INFLAM_SET)]
    erows = []
    for usrc, N in [("deg_union", N_deg_union), ("genomic_19000", N_genomic)]:
        for dn, ds in deg_sets:
            for gn, gs in gene_sets:
                erows.append(enrich(dn, ds, gn, gs, N, usrc))
    en = pd.DataFrame(erows)
    en["q_value"] = multipletests(en["p_value"], method="fdr_bh")[1]
    en = en[["universe_source","universe_N","deg_set","deg_N","gene_set",
             "set_N","overlap_k","odds_ratio","p_value","q_value",
             "overlap_genes"]].sort_values(
             ["universe_source","deg_set","gene_set"]).reset_index(drop=True)
    en.to_csv(os.path.join(out, "enrichment_results.csv"), index=False)

    # ---- Analysis 3: overlap depression-astro vs AD-astro DEGs ----
    A = dep_astro_genes; B = ad_astro_genes
    inter = A & B; uni = A | B
    jacc = len(inter)/len(uni) if uni else np.nan
    all_pre = set(UPR_SET) | set(INFLAM_SET)
    upr_in_dep = sorted(set(UPR_SET) & A)
    upr_in_ad = sorted(set(UPR_SET) & B)
    upr_dep_specific = sorted((set(UPR_SET) & A) - B)
    orow = [dict(comparison="Supp3_DepressionAstro_vs_Supp7_ADAstro",
        setA="Supp3_DepressionAstro_DEGs", sizeA=len(A),
        setB="Supp7_ADAstro_DEGs", sizeB=len(B),
        intersection=len(inter), union=len(uni), jaccard=jacc,
        UPR_in_depression=";".join(upr_in_dep),
        UPR_in_AD=";".join(upr_in_ad),
        UPR_depression_specific=";".join(upr_dep_specific),
        INFLAM_in_depression=";".join(sorted(set(INFLAM_SET)&A)),
        INFLAM_in_AD=";".join(sorted(set(INFLAM_SET)&B)))]
    ov = pd.DataFrame(orow)
    ov.to_csv(os.path.join(out, "overlap_results.csv"), index=False)

    # ---- gene-level membership of prespecified genes (diagnostic) ----
    mrows = []
    for gset_name, gset in [("UPR_ERstress", UPR_SET), ("Inflammatory", INFLAM_SET)]:
        for g in gset:
            mrows.append(dict(gene=g, gene_set=gset_name,
                in_universe=int(g in universe),
                in_Supp3_DepressionAstro=int(g in dep_astro_genes),
                in_Supp3_AstroWIF1_up=int(g in wif1_up_genes),
                in_Supp3_OligoOPALIN_down=int(g in oli_down_genes),
                in_Supp7_ADAstro=int(g in ad_astro_genes)))
    mem = pd.DataFrame(mrows).sort_values(["gene_set","gene"]).reset_index(drop=True)
    mem.to_csv(os.path.join(out, "gene_membership.csv"), index=False)

    # ---- samples.csv (donors) ----
    srows = []
    for don in sorted(set(dep.index) | set(adp.index)):
        in_dep = don in dep.index
        in_adp = don in adp.index
        included = in_dep and in_adp
        if included:
            group = "used_in_depression_vs_ADprogression_correlation"
            excl = ""
        else:
            group = "unlabeled"
            excl = "not present in both Depression and AD-progression PAC sheets"
        srows.append(dict(accession=don, dataset="Supp6_PAC",
            organism="Homo sapiens", tissue="DLPFC",
            source_metadata="PsychAD snRNA-seq (syn60084804); labels not provided in Supp Data 6",
            in_DepressionMood_PAC=int(in_dep),
            in_ADprogression_PAC=int(in_adp),
            assigned_group=group, included=int(included),
            exclusion_reason=excl))
    samp = pd.DataFrame(srows).sort_values("accession").reset_index(drop=True)
    samp.to_csv(os.path.join(out, "samples.csv"), index=False)

    # ---- provenance json (not a tabular result) ----
    prov = dict(zip_sha256=got_sha, zip_expected_sha256=EXPECTED_SHA256,
        zip_sha256_match=(got_sha == EXPECTED_SHA256),
        zip_bytes=len(zip_bytes), zip_url=ZIP_URL,
        n_common_donors=len(common), n_subclasses=len(subclasses),
        universe_N=N_deg_union,
        sheets_read=[
            ["Supplementary_Data_6.xlsx","Avg. PAC scores DepressionMood"],
            ["Supplementary_Data_6.xlsx","Avg. PAC scores AD progression"],
            ["Supplementary_Data_6.xlsx","SHAP values DepressionMood"],
            ["Supplementary_Data_3.xlsx","Depression PAC DEGs in Astrocyt"],
            ["Supplementary_Data_3.xlsx","Upregulated genes in AD-Depr.-A"],
            ["Supplementary_Data_3.xlsx","Downregulated genes in AD-Depr."],
            ["Supplementary_Data_7.xlsx","AD PAC DEGs"]])
    with open(os.path.join(out, "provenance.json"), "w") as f:
        json.dump(prov, f, indent=2, sort_keys=True)
    print("DONE", json.dumps(prov))

if __name__ == "__main__":
    main()
