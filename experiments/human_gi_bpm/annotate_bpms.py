#!/usr/bin/env python3
"""Annotate BPM-like module pairs from bpm_search.py with (a) functional
coherence against the Billmann et al. 2026 SAFE network-region bioprocess
assignments (File_S11) and (b) overlap with dismech-curated disease genes.

Coherence convention mirrors the enrichment reporting of the GIDEON paper:
a module is called coherent when >=50% of its annotated genes fall in one
SAFE bioprocess region; a BPM is same-process / different-process / one-side /
neither accordingly.
"""
import argparse
from collections import Counter

import pandas as pd


def region_call(genes, g2r):
    ann = [g2r[g] for g in genes if g in g2r]
    if not ann:
        return "", 0.0, 0
    top, n = Counter(ann).most_common(1)[0]
    return top, n / len(ann), len(ann)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bpms", default="bpms.tsv")
    ap.add_argument("--safe", default="File_S11.xlsx")
    ap.add_argument("--dismech-genes", default="dismech_genes.tsv")
    ap.add_argument("--out", default="bpms_annotated.tsv")
    ap.add_argument("--overlap-out", default="dismech_overlap.tsv")
    args = ap.parse_args()

    b = pd.read_csv(args.bpms, sep="\t").fillna("")
    safe = pd.read_excel(args.safe, sheet_name="Network clusters_gene list")
    g2r = dict(zip(safe["Gene Name"], safe["Network region_BioProcess enrichment"]))
    dg = pd.read_csv(args.dismech_genes, sep="\t",
                     names=["symbol", "kind", "entry", "path"])
    dis = dg[dg.kind == "disorder"].groupby("symbol")["entry"].apply(
        lambda s: sorted(set(s))).to_dict()

    rows, overlap = [], []
    for _, r in b.iterrows():
        A = r.query_module.split("|")
        B = r.library_module.split("|")
        a_top, a_frac, a_n = region_call(A, g2r)
        b_top, b_frac, b_n = region_call(B, g2r)
        a_coh = a_frac >= 0.5 and a_n >= 2
        b_coh = b_frac >= 0.5 and b_n >= 2
        if a_coh and b_coh:
            call = "same-process" if a_top == b_top else "different-process"
        elif a_coh or b_coh:
            call = "one-side"
        else:
            call = "neither"
        dis_a = sorted(g for g in A if g in dis)
        dis_b = sorted(g for g in B if g in dis)
        for side, genes in (("query_module", dis_a), ("library_module", dis_b)):
            for g in genes:
                for e in dis[g]:
                    overlap.append({"bpm_id": r.bpm_id, "side": side,
                                    "gene": g, "disorder": e})
        rows.append({**r.to_dict(),
                     "A_top_region": a_top, "A_region_frac": round(a_frac, 2),
                     "B_top_region": b_top, "B_region_frac": round(b_frac, 2),
                     "coherence_call": call,
                     "dismech_genes_A": "|".join(dis_a),
                     "dismech_genes_B": "|".join(dis_b),
                     "n_dismech_genes": len(dis_a) + len(dis_b)})

    out = pd.DataFrame(rows)
    out.to_csv(args.out, sep="\t", index=False)
    pd.DataFrame(overlap).to_csv(args.overlap_out, sep="\t", index=False)
    print(out.coherence_call.value_counts().to_dict())
    both = out[out.coherence_call.isin(["same-process", "different-process"])]
    print(f"{len(both)}/{len(out)} BPMs functionally coherent on both sides")
    print(f"{(out.n_dismech_genes > 0).sum()}/{len(out)} BPMs touch >=1 dismech gene")
    cross = out[(out.dismech_genes_A != "") & (out.dismech_genes_B != "")]
    print(f"{len(cross)} BPMs have dismech genes on BOTH sides")


if __name__ == "__main__":
    main()
