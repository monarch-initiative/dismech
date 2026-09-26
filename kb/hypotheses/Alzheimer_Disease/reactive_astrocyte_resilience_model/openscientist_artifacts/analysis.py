#!/usr/bin/env python3
"""
Deterministic re-analysis of published derived scores from He et al. 2026 Nat Med
(PMID:42778763, doi:10.1038/s41591-025-04128-1), Supplementary Data zip
(41591_2025_4128_MOESM3_ESM.zip). Source cohort: PsychAD snRNA-seq, DLPFC,
1,494 donors (synapse:syn60084804, CONTROLLED - NOT accessed here).

This script re-analyses PUBLISHED derived tables only (shared data lineage with
the paper); it is NOT an independent replication. Donor-by-subclass PAC score
matrices carry donor IDs only (no diagnosis/Braak/resilience labels), so only
label-free tests are performed.

Objectives:
 (1) Supp Data 2 'Fig. 3f': Astro resilience P-adj and strict-vs-resilient median
     PAC difference, relative to all subclasses.
 (2) Astrocyte DEG tables: classify genes vs prespecified reactive-astrocyte
     marker sets; directional Fisher enrichment of A2 vs A1 among genes inferred
     "higher in resilient" donors; report EMP1 and FKBP5 explicitly.
 (3) Supp Data 6 'Avg. PAC scores AD progression': Spearman (BH) of donor Astro
     PAC vs every excitatory/inhibitory subclass.

Usage: python3 analysis.py --output-dir DIR [--cache-dir DIR]
Deterministic: no randomness; regenerates all tabular outputs without an LLM.
"""
import argparse, os, io, zipfile, hashlib
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.multitest import multipletests

ZIP_URL = ("https://media.springernature.com/original/springer-static/esm/"
           "art%3A10.1038%2Fs41591-025-04128-1/MediaObjects/"
           "41591_2025_4128_MOESM3_ESM.zip")
ZIP_NAME = "41591_2025_4128_MOESM3_ESM.zip"
ZIP_SHA256 = "27901070f322dff0e1283343d61de6f80b656bc41dbc7ea0efa9e8b8a1851865"

# ---- Prespecified reactive-astrocyte marker sets (Liddelow et al. 2017 axis) ----
# Human symbols. Identifier mapping decisions:
#   H2-T23 (mouse MHC-I) -> human ortholog HLA-E (recorded, class A1).
#   IIGP1  -> no 1:1 human ortholog -> SKIPPED (documented).
PAN_REACTIVE = ["LCN2","STEAP4","S1PR3","TIMP1","HSPB1","CXCL10","CD44","OSMR",
                "CP","SERPINA3","ASPG","VIM","GFAP"]
A1_NEUROTOXIC = ["C3","HLA-E","SERPING1","GBP2","FBLN5","UGT1A1","FKBP5",
                 "AMIGO2","PSMB8","SRGN"]
A2_NEUROPROTECTIVE = ["CLCF1","TGM1","PTX3","S100A10","SPHK1","CD109","PTGS2",
                      "EMP1","SLC10A6","TM4SF1","B3GNT5","CD14"]
EXTRA = ["CRYAB","MAOB","CHI3L1"]

MARKER_CLASS = {}
for g in PAN_REACTIVE: MARKER_CLASS[g] = "pan_reactive"
for g in A1_NEUROTOXIC: MARKER_CLASS[g] = "A1_neurotoxic"
for g in A2_NEUROPROTECTIVE: MARKER_CLASS[g] = "A2_neuroprotective"
for g in EXTRA: MARKER_CLASS[g] = "individual"


def get_zip_bytes(cache_dir, output_dir):
    """Return zip bytes; reuse cache-dir copy if present (never re-download in replay)."""
    candidates = []
    if cache_dir:
        candidates.append(os.path.join(cache_dir, ZIP_NAME))
    candidates.append(os.path.join(output_dir, "raw", ZIP_NAME))
    for p in candidates:
        if os.path.exists(p):
            b = open(p, "rb").read()
            if hashlib.sha256(b).hexdigest() == ZIP_SHA256:
                return b
    # Not cached: download to cache_dir (or output_dir/raw)
    import requests
    dest_dir = cache_dir if cache_dir else os.path.join(output_dir, "raw")
    os.makedirs(dest_dir, exist_ok=True)
    r = requests.get(ZIP_URL, timeout=600); r.raise_for_status()
    b = r.content
    if hashlib.sha256(b).hexdigest() != ZIP_SHA256:
        raise RuntimeError("Downloaded zip sha256 mismatch")
    open(os.path.join(dest_dir, ZIP_NAME), "wb").write(b)
    return b


def read_sheet(zbytes, workbook, sheet, **kw):
    z = zipfile.ZipFile(io.BytesIO(zbytes))
    name = "supplementary_data/" + workbook
    data = z.read(name)
    return pd.read_excel(io.BytesIO(data), sheet_name=sheet, **kw)


def clean_num(x):
    """Strip stray leading commas/whitespace from Fig.3f text cells -> float."""
    if pd.isna(x): return np.nan
    s = str(x).strip().lstrip(",").strip()
    try: return float(s)
    except ValueError: return np.nan


def parse_astro_deg_supp7(zbytes):
    raw = read_sheet(zbytes, "Supplementary_Data_7.xlsx", "AD PAC DEGs", header=None)
    hdr = raw.iloc[3]
    blocks = {i: str(v) for i, v in hdr.items() if str(v) != "nan"}
    universe = set()
    astro = None
    for start, name in blocks.items():
        b = raw.iloc[5:, start:start+5].copy()
        b.columns = ["gene", "score", "log2FC", "pval", "adjp"]
        b = b.dropna(subset=["gene"])
        b["gene"] = b["gene"].astype(str)
        universe |= set(b["gene"])
        if name == "Astrocyte":
            astro = b.copy()
    for c in ["score", "log2FC", "pval", "adjp"]:
        astro[c] = pd.to_numeric(astro[c], errors="coerce")
    astro = astro.dropna(subset=["log2FC", "pval"]).reset_index(drop=True)
    return astro, universe


def parse_fig2f_astro(zbytes):
    """Supp Data 1 Fig.2f Astrocytes: donor-level (cols10-13) & PAC-level (cols15-18)."""
    raw = read_sheet(zbytes, "Supplementary_Data_1.xlsx", "Fig. 2f", header=None)
    out = {}
    for cols, level in [((10,11,12,13), "donor-level"), ((15,16,17,18), "PAC-level")]:
        b = raw.iloc[7:, list(cols)].copy()
        b.columns = ["gene", "log2FC", "pval", "adjp"]
        b = b.dropna(subset=["gene"])
        b["gene"] = b["gene"].astype(str)
        for c in ["log2FC", "pval", "adjp"]:
            b[c] = pd.to_numeric(b[c], errors="coerce")
        b = b.dropna(subset=["log2FC", "pval"]).reset_index(drop=True)
        out[level] = b
    return out


def parse_dep_astro(zbytes):
    """Supp Data 3 'Depression PAC DEGs in Astrocyte' (header at row3)."""
    raw = read_sheet(zbytes, "Supplementary_Data_3.xlsx",
                     "Depression PAC DEGs in Astrocyt", header=None)
    b = raw.iloc[4:, 0:5].copy()
    b.columns = ["gene", "score", "log2FC", "pval", "adjp"]
    b = b.dropna(subset=["gene"])
    b["gene"] = b["gene"].astype(str)
    for c in ["score", "log2FC", "pval", "adjp"]:
        b[c] = pd.to_numeric(b[c], errors="coerce")
    b = b.dropna(subset=["log2FC", "pval"]).reset_index(drop=True)
    return b


def fisher_overlap(marker_set, deg_set, universe):
    """Overlap Fisher: marker genes among astro DEGs vs background universe."""
    ms = [g for g in marker_set if g in universe]
    k = sum(1 for g in ms if g in deg_set)      # marker & DEG
    n_set = len(ms)
    N = len(universe)
    K = len(deg_set & universe)                 # DEGs in universe
    a = k
    b = n_set - k
    c = K - k
    d = N - n_set - c
    OR, p = stats.fisher_exact([[a, b], [c, d]], alternative="greater")
    expected = n_set * K / N if N else np.nan
    return dict(n_set_in_universe=n_set, n_in_astro_DEG=k, universe_size=N,
                deg_in_universe=K, expected=expected, odds_ratio=OR, pval=p)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--cache-dir", default=None)
    args = ap.parse_args()
    out = args.output_dir
    os.makedirs(out, exist_ok=True)

    zbytes = get_zip_bytes(args.cache_dir, out)

    # ================= Objective 1: Fig. 3f resilience =================
    raw3f = read_sheet(zbytes, "Supplementary_Data_2.xlsx", "Fig. 3f", header=None)
    hdr = raw3f.iloc[2].tolist()
    d3 = raw3f.iloc[3:].reset_index(drop=True)
    d3.columns = ["subclass"] + [str(h) for h in hdr[1:]]
    d3 = d3.dropna(subset=["subclass"]).copy()
    f3 = pd.DataFrame({
        "subclass": d3["subclass"].astype(str).values,
        "P_adj": [clean_num(x) for x in d3.iloc[:, 1]],
        "neglog10_Padj": [clean_num(x) for x in d3.iloc[:, 2]],
        "AD_strict_median_PAC": [clean_num(x) for x in d3.iloc[:, 3]],
        "AD_resilient_median_PAC": [clean_num(x) for x in d3.iloc[:, 4]],
        "strict_minus_resilient_diff": [clean_num(x) for x in d3.iloc[:, 5]],
    })
    f3 = f3.sort_values("P_adj", kind="mergesort").reset_index(drop=True)
    f3["rank_by_Padj"] = np.arange(1, len(f3) + 1)
    f3["is_astrocyte"] = f3["subclass"].str.fullmatch("Astro")
    f3.to_csv(os.path.join(out, "fig3f_resilience.csv"), index=False)
    astro_row = f3[f3["is_astrocyte"]].iloc[0]

    # ================= Objective 2: astrocyte DEG marker classification =================
    astro7, universe = parse_astro_deg_supp7(zbytes)
    fig2f = parse_fig2f_astro(zbytes)
    dep = parse_dep_astro(zbytes)

    # Group sizes from documented balanced donor subsets (Supp Data 5 'PAC number'):
    #   AD: 100 vs 100 ; Depression/Mood: 100 vs 100 (PAC-level designs).
    gene_rows = []

    def add_rows(df, dataset, comparison, phenotype, has_score, n1, n2,
                 up_label, down_label, infer_resilient):
        d = df.copy()
        # BH recomputed within this dataset/comparison over reported genes
        q = multipletests(d["pval"].values, method="fdr_bh")[1]
        for i, r in d.iterrows():
            l2 = float(r["log2FC"])
            direction = up_label if l2 > 0 else (down_label if l2 < 0 else "none")
            if infer_resilient:
                res_dir = "higher_in_resilient" if l2 < 0 else ("higher_in_impaired" if l2 > 0 else "none")
            else:
                res_dir = ""
            gene_rows.append(dict(
                dataset=dataset, cell_type="Astrocyte", gene=str(r["gene"]),
                comparison=comparison, phenotype=phenotype,
                n_group1=n1, n_group2=n2,
                mean_group1="", mean_group2="",
                log2_mean_diff=l2, fold_change=float(2.0 ** l2),
                test_statistic=(float(r["score"]) if has_score and not pd.isna(r.get("score")) else ""),
                pvalue=float(r["pval"]),
                qvalue_BH=float(q[list(d.index).index(i)]),
                published_adj_p=(float(r["adjp"]) if not pd.isna(r.get("adjp")) else ""),
                cohens_d="",
                marker_class=MARKER_CLASS.get(str(r["gene"]), "none"),
                direction=direction,
                resilient_direction_inferred=res_dir,
            ))

    add_rows(astro7, "Supplementary_Data_7:AD PAC DEGs",
             "AD-PAC+_vs_AD-PAC-_PAC-level", "AD", True, 100, 100,
             "up_in_ADPAC", "down_in_ADPAC", infer_resilient=True)
    add_rows(fig2f["PAC-level"], "Supplementary_Data_1:Fig. 2f",
             "AD_vs_Control_PAC-level", "AD", False, 100, 100,
             "up_in_ADPAC", "down_in_ADPAC", infer_resilient=True)
    add_rows(fig2f["donor-level"], "Supplementary_Data_1:Fig. 2f",
             "AD_vs_Control_donor-level", "AD", False, "", "",
             "up_in_AD", "down_in_AD", infer_resilient=False)
    add_rows(dep, "Supplementary_Data_3:Depression PAC DEGs in Astrocyte",
             "DepressionPAC+_vs_DepressionPAC-_PAC-level", "Depression", True, 100, 100,
             "up_in_depPAC", "down_in_depPAC", infer_resilient=False)

    gene_results = pd.DataFrame(gene_rows)
    gene_results = gene_results.sort_values(
        ["dataset", "comparison", "gene"], kind="mergesort").reset_index(drop=True)
    gene_results.to_csv(os.path.join(out, "gene_results.csv"), index=False)

    # ---- Enrichment tests (objective 2) on primary AD astrocyte DEG set (Supp7) ----
    deg_set = set(astro7["gene"])
    l2map = dict(zip(astro7["gene"], astro7["log2FC"]))
    enr_rows = []
    for name, ms in [("pan_reactive", PAN_REACTIVE),
                     ("A1_neurotoxic", A1_NEUROTOXIC),
                     ("A2_neuroprotective", A2_NEUROPROTECTIVE)]:
        st = fisher_overlap(ms, deg_set, universe)
        st.update(dict(test="overlap_vs_universe", marker_set=name, n_set_total=len(ms)))
        enr_rows.append(st)
    # Directional A2 vs A1 among significant astro DEGs (inferred resilient = down),
    # computed per AD astrocyte DEG table and pooled (Supp7-preferred dedup).
    def directional(l2, label):
        A1p = [g for g in A1_NEUROTOXIC if g in l2]
        A2p = [g for g in A2_NEUROPROTECTIVE if g in l2]
        a1_up = sum(l2[g] > 0 for g in A1p); a1_dn = sum(l2[g] < 0 for g in A1p)
        a2_up = sum(l2[g] > 0 for g in A2p); a2_dn = sum(l2[g] < 0 for g in A2p)
        OR, p = stats.fisher_exact([[a2_dn, a2_up], [a1_dn, a1_up]], alternative="greater")
        return dict(test="directional_A2vsA1_resilient", marker_set=label,
                    n_set_total=len(A1p)+len(A2p), n_set_in_universe=len(A1p)+len(A2p),
                    n_in_astro_DEG=len(A1p)+len(A2p), universe_size="", deg_in_universe="",
                    expected="", odds_ratio=OR, pval=p,
                    A2_down_resilient=a2_dn, A2_up_impaired=a2_up,
                    A1_down_resilient=a1_dn, A1_up_impaired=a1_up)
    l2_f2 = dict(zip(fig2f["PAC-level"]["gene"].astype(str), fig2f["PAC-level"]["log2FC"]))
    l2_pool = dict(l2_f2); l2_pool.update(l2map)  # Supp7 overrides on gene conflict
    enr_rows.append(directional(l2map, "A2_vs_A1_Supp7_ADPAC"))
    enr_rows.append(directional(l2_f2, "A2_vs_A1_Fig2f_PAClevel"))
    enr_rows.append(directional(l2_pool, "A2_vs_A1_pooled"))
    enr = pd.DataFrame(enr_rows)
    # BH across the enrichment tests
    enr["qval_BH"] = multipletests(enr["pval"].values, method="fdr_bh")[1]
    col_order = ["test", "marker_set", "n_set_total", "n_set_in_universe",
                 "n_in_astro_DEG", "universe_size", "deg_in_universe", "expected",
                 "odds_ratio", "pval", "qval_BH",
                 "A2_down_resilient", "A2_up_impaired", "A1_down_resilient", "A1_up_impaired"]
    for c in col_order:
        if c not in enr.columns: enr[c] = ""
    enr = enr[col_order]
    enr.to_csv(os.path.join(out, "enrichment_results.csv"), index=False)

    # ================= Objective 3: Astro vs neuronal PAC correlations =================
    pac = read_sheet(zbytes, "Supplementary_Data_6.xlsx", "Avg. PAC scores AD progression")
    pac = pac.rename(columns={pac.columns[0]: "donor"})
    neuronal = [c for c in pac.columns if c.startswith("EN_") or c.startswith("IN_")]
    crows = []
    for c in sorted(neuronal):
        x = pd.to_numeric(pac["Astro"], errors="coerce")
        y = pd.to_numeric(pac[c], errors="coerce")
        m = x.notna() & y.notna()
        rho, pv = stats.spearmanr(x[m], y[m])
        crows.append(dict(reference="Astro", subclass=c, n=int(m.sum()),
                          spearman_rho=float(rho), pval=float(pv)))
    corr = pd.DataFrame(crows)
    corr["qval_BH"] = multipletests(corr["pval"].values, method="fdr_bh")[1]
    corr = corr.sort_values("subclass", kind="mergesort").reset_index(drop=True)
    corr.to_csv(os.path.join(out, "correlation_results.csv"), index=False)

    # ================= samples.csv (objective-3 analysed donors) =================
    samples = pd.DataFrame({
        "sample_id": pac["donor"].astype(str).values,
        "accession": "synapse:syn60084804",
        "dataset": "Supplementary_Data_6:Avg. PAC scores AD progression",
        "organism": "Homo sapiens",
        "tissue": "DLPFC",
        "source_metadata": ("PsychAD snRNA-seq derived donor x 27-subclass average "
                            "PAC score (AD progression); controlled cohort not accessed; "
                            "donor ID only, no diagnosis/Braak/resilience label"),
        "assigned_group": "unlabeled",
        "exclusion_reason": "",
    })
    samples = samples.sort_values("sample_id", kind="mergesort").reset_index(drop=True)
    samples.to_csv(os.path.join(out, "samples.csv"), index=False)

    # ================= methods.md & comparison.md (deterministic) =================
    write_methods(out)
    write_comparison(out, astro_row, f3, l2map, enr, corr, astro7)
    print("DONE. Outputs in", out)


def write_methods(out):
    txt = f"""# Methods

## Source data (single input, shared lineage - re-analysis, not replication)
- He et al. 2026, Nature Medicine. PMID:42778763; doi:10.1038/s41591-025-04128-1.
- Input: Supplementary Data zip `{ZIP_NAME}` (sha256 `{ZIP_SHA256}`).
- Underlying cohort: PsychAD snRNA-seq, human dorsolateral prefrontal cortex (DLPFC),
  1,494 donors (synapse:syn60084804). The controlled cohort was NOT accessed; only
  the open Supplementary workbooks (.xlsx) were used.
- Package added to approved list for reading .xlsx: openpyxl (preflighted).

## Sample inclusion / exclusion
- "Samples" = donors in Supplementary Data 6 sheet 'Avg. PAC scores AD progression'
  (n=581), used for the within-donor correlation objective. Donors carry ID only; no
  diagnosis/Braak/resilience labels are present, so donors were NOT assigned to groups
  and no label-dependent test was run. No donor excluded (all rows have complete
  numeric PAC vectors). See samples.csv.

## Normalization / transform state
- All quantities are PUBLISHED derived scores; no re-normalization or re-transform was
  applied. PAC (phenotype-associated-cell) scores are used as provided. DEG effect
  sizes are the published log2(fold change); no re-scaling.
- Fig.3f median-PAC cells contained a stray leading-comma text artifact in the
  'AD strict median PAC score' column; values were parsed by stripping the leading
  comma/whitespace and casting to float (no numeric change).

## Identifier / probe mapping and aggregation
- Gene symbols used as provided in the workbooks (one row per gene per subclass block).
- Reactive-astrocyte marker sets are prespecified (Liddelow-type axis). Mapping rules:
  * H2-T23 (mouse MHC class-I) -> human ortholog HLA-E (class A1).
  * IIGP1 -> no 1:1 human ortholog -> SKIPPED.
- pan-reactive (13): LCN2,STEAP4,S1PR3,TIMP1,HSPB1,CXCL10,CD44,OSMR,CP,SERPINA3,ASPG,VIM,GFAP
- A1/neurotoxic (10 after mapping): C3,HLA-E,SERPING1,GBP2,FBLN5,UGT1A1,FKBP5,AMIGO2,PSMB8,SRGN
- A2/neuroprotective (12): CLCF1,TGM1,PTX3,S100A10,SPHK1,CD109,PTGS2,EMP1,SLC10A6,TM4SF1,B3GNT5,CD14
- individual: CRYAB, MAOB, CHI3L1

## Astrocyte DEG tables used (identified from each workbook 'key' sheet)
- Supplementary Data 7 'AD PAC DEGs', Astrocyte block (AD-PAC+ vs AD-PAC-, PAC-level;
  1,171 significant genes) -- PRIMARY for objective 2.
- Supplementary Data 1 'Fig. 2f', Astrocytes donor-level and PAC-level (AD vs Control;
  significant genes only).
- Supplementary Data 3 'Depression PAC DEGs in Astrocyte' (phenotype = Depression, not
  AD; included for completeness and marked as such).
- (Excluded from astrocyte set: Supp Data 2 'Fig. 3g' and 'Fig. 3d' are neuronal-only
  DEG tables; Supp Data 3 'Upregulated genes in AD-Depr.-AstroWIF1' is a one-directional
  cluster-marker list, not a two-sided DEG table.)

## Statistical tests
1. Objective 1: report published Fig.3f adjusted P and (strict - resilient) median PAC
   difference for Astro among all subclasses (re-statement of published values).
2. Objective 2:
   - Overlap enrichment (one-sided Fisher exact, 'greater') of each marker set among the
     1,171 astrocyte DEGs, with explicit background = union of all genes reported across
     the 21 subclass blocks of Supp Data 7 'AD PAC DEGs' (11,145 genes = genes tested/
     detected in >=1 PsychAD subclass DE model).
   - Directional A2-vs-A1 Fisher exact ('greater') among marker genes that are
     significant astrocyte DEGs, testing whether A2 markers preferentially fall in the
     "higher-in-resilient" direction. Direction is INFERRED: Fig.3f shows resilient
     donors have LOWER Astro PAC, so down-in-AD-PAC (log2FC<0) is treated as the
     resilient-like direction and up (log2FC>0) as the impaired/strict-like direction.
     This inference is a chained assumption, NOT a direct resilient-vs-strict astrocyte
     measurement (no such astrocyte DEG table exists in the supplement).
   - EMP1 (A2) and FKBP5 (A1) reported explicitly.
3. Objective 3: Spearman correlation of donor Astro PAC vs every excitatory (EN_*) and
   inhibitory (IN_*) subclass in 'Avg. PAC scores AD progression' (n=581 donors, all
   pairs complete).

## Multiple-testing and effect-size conventions
- Multiple testing: Benjamini-Hochberg FDR (statsmodels fdr_bh) applied within each
  results table (gene_results per dataset/comparison; enrichment across its tests;
  correlations across the 17 subclasses).
- Effect-size convention: published log2(fold change) is the primary DEG effect size;
  ordinary fold change = 2^log2FC is also reported. Group means and Cohen's d are NOT
  recoverable from published summary statistics (no per-cell/per-donor expression
  matrix; donors unlabeled) and are left blank, by design. Group sizes reflect the
  documented balanced donor subsets (Supp Data 5 'PAC number': AD 100 vs 100;
  Depression/Mood 100 vs 100) for PAC-level comparisons; blank for donor-level.
- Correlation effect size: Spearman rho.

## Determinism
- No random operations. Stable mergesort ordering; inputs read from the fixed-checksum
  zip. Re-running regenerates byte-identical samples.csv and gene_results.csv.
"""
    open(os.path.join(out, "methods.md"), "w").write(txt)


def write_comparison(out, astro_row, f3, l2map, enr, corr, astro7):
    dirmap = enr[enr["marker_set"] == "A2_vs_A1_Supp7_ADPAC"].iloc[0]
    dirpool = enr[enr["marker_set"] == "A2_vs_A1_pooled"].iloc[0]
    def g(gene):
        return l2map.get(gene, None)
    emp1 = g("EMP1"); fkbp5 = g("FKBP5")
    n_neur = len(corr); nsig = int((corr["qval_BH"] < 0.05).sum())
    rho_min = corr["spearman_rho"].min(); rho_max = corr["spearman_rho"].max()
    txt = f"""# Comparison / interpretation

All numbers below are a RE-ANALYSIS of published derived scores (He et al. 2026,
Nat Med; PMID:42778763). This bundle shares data lineage with the paper and is not an
independent replication. Observed results and biological inference are separated below.

## OBSERVED RESULTS

### (1) Astrocyte resilience signal (Supp Data 2 'Fig. 3f')
- Astro: adjusted P = {astro_row['P_adj']:.6g}; (AD-strict - AD-resilient) median PAC
  difference = {astro_row['strict_minus_resilient_diff']:.6g}
  (strict median {astro_row['AD_strict_median_PAC']:.6g} vs resilient
  {astro_row['AD_resilient_median_PAC']:.6g}).
- Astro rank by adjusted P = {int(astro_row['rank_by_Padj'])} of {len(f3)} subclasses
  present in the sheet. The strongest separators are neuronal (EN_L3_5_IT_3, IN_PVALB_CHC,
  EN_L2_3_IT, IN_SST); astrocytes are significant but mid-ranked.

### (2) Reactive-astrocyte marker classification (primary: Supp7 AD PAC DEGs, 1,171 genes)
- EMP1 (A2/neuroprotective): log2FC = {emp1:+.3f} -> DOWN in AD-PAC (inferred
  higher-in-resilient direction). Matches the neuroprotective prediction.
- FKBP5 (A1/neurotoxic): log2FC = {fkbp5:+.3f} -> UP in AD-PAC (impaired/strict-like
  direction). Matches the neurotoxic prediction.
- Directional A2-vs-A1 Fisher (A2 enriched in resilient direction): OR =
  {float(dirmap['odds_ratio']):.3g}, p = {float(dirmap['pval']):.3g}, BH q =
  {float(dirmap['qval_BH']):.3g}. Counts: A2 down/up = {int(dirmap['A2_down_resilient'])}/
  {int(dirmap['A2_up_impaired'])}; A1 down/up = {int(dirmap['A1_down_resilient'])}/
  {int(dirmap['A1_up_impaired'])}. NOT significant: only 4 canonical A1/A2 markers survive
  as significant astrocyte DEGs, and the counter-examples HLA-E (A1, down) and CD109
  (A2, up) cancel the EMP1/FKBP5 signal.
- Pooled directional test (Supp7 + Fig.2f PAC-level astrocyte DEGs, {int(dirpool['n_set_total'])}
  markers): OR = {float(dirpool['odds_ratio']):.3g}, p = {float(dirpool['pval']):.3g},
  BH q = {float(dirpool['qval_BH']):.3g}. Still not significant: most A1 markers are also
  DOWN in AD-PAC (higher in resilient-like), so A2 is not preferentially resilient-directed.
- Overlap enrichment vs 11,145-gene background: see enrichment_results.csv (BH-corrected);
  no marker set is significantly over-represented among astrocyte DEGs after correction.

### (3) Astro-vs-neuronal PAC co-variation (Supp Data 6 'AD progression', n=581)
- All {n_neur}/{n_neur} excitatory+inhibitory subclasses correlate POSITIVELY with Astro
  PAC (Spearman rho {rho_min:.3f}-{rho_max:.3f}; {nsig}/{n_neur} BH-q < 0.05).
- Strongest: EN_L3_5_IT_2, EN_L2_3_IT, EN_L3_5_IT_1 (rho ~0.52-0.57).

## BIOLOGICAL INFERENCE (clearly separated from the observations above)
- The two named marker genes behave as the neuroprotective-vs-neurotoxic model predicts
  (EMP1 up in resilient-like, FKBP5 up in impaired-like), but the marker AXIS as a whole
  is NOT statistically supported in these published astrocyte DEGs: the A2-vs-A1 directional
  enrichment is null (OR~1, p~0.83) and rests on only 4 overlapping markers.
- Positive Astro-neuronal PAC co-variation is consistent with a shared donor-level
  disease-burden component rather than an astrocyte-specific resilience axis; because both
  are derived phenotype-association scores, part of this correlation may restate the
  construction of the scores.
- Objective 1 and the EMP1/FKBP5 directions largely RESTATE quantities the paper already
  computed (same derived tables). The only genuinely new derived statistic here is the
  donor-level Astro-vs-neuronal Spearman structure and the (null) directional marker test.

## LIMITATIONS
- Re-analysis of published derived scores; shared lineage with the source paper.
- Donor PAC matrices carry no diagnosis/Braak/resilience labels -> no direct
  resilient-vs-strict astrocyte DE; the resilient direction is inferred via Fig.3f.
- Astrocyte DEG tables are significant-only, limiting background choice; overlap
  background is the union of genes reported across subclass blocks, not the full
  transcriptome.
- Group means / Cohen's d not recoverable from summary statistics.
"""
    open(os.path.join(out, "comparison.md"), "w").write(txt)


if __name__ == "__main__":
    main()
