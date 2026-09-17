#!/usr/bin/env python3
"""Search for Between-Pathway-Model-like compensatory module pairs in the
Billmann et al. 2026 HAP1 quantitative genetic interaction map.

Adaptation of the BPM objective of GIDEON (Garcia et al. 2026,
doi:10.1093/bioinformatics/btag385) to a *bipartite* query x library qGI
matrix:

- module A is drawn from the 222 query genes (fully measured against the
  library, and against each other via the query-in-library rows);
- module B is drawn from the ~17.8k library genes;
- the objective mirrors GIDEON eq. (1): reward negative qGI across A x B and
  positive measured qGI within A; library-side (within-B) cohesion is not
  measured, so it is enforced structurally by qGI-profile correlation
  (the profile-similarity standard for this dataset), in the spirit of
  Kelley & Ideker 2005 using PPI edges for within-pathway support.

Greedy gene-centered growth from every stringent negative pair, iterative
trimming, minimum size 3 per module, Jaccard pruning at 0.66 -- thresholds
follow the GIDEON/LocalCut conventions where transferable.

Inputs: parquet conversions of Billmann File_S4 (qGI_scores, qGI_FDR).
Deterministic; no solver dependency.
"""
import argparse

import numpy as np
import pandas as pd

STD_Q, STD_FDR = 0.3, 0.1        # standard significance (paper's threshold)
STR_Q, STR_FDR = 0.6, 0.01       # stringent significance (seed edges)
PCC_MIN_B = 0.3                  # library-side profile cohesion floor (222-dim profiles)
PCC_MIN_A = 0.2                  # query-side profile cohesion floor (17.8k-dim profiles)
GAIN_MIN = 0.6                   # marginal gain needed to add a gene (~1 stringent edge)
WITHIN_A_FLOOR = -0.3            # do not add a query clearly antagonistic to module A
MAX_SIDE = 25                    # GIDEON/LocalCut module size cap
MIN_SIDE = 3                     # GIDEON/LocalCut module size floor
TRIM_MIN_EDGES = 2               # per-gene minimum significant cross edges
TRIM_MIN_CONTRIB = 0.02          # per-gene contribution / BPM size floor (GIDEON: 0.015)
JACCARD_MAX = 0.66               # diversity pruning (field convention)


def collapse_screens(scores: pd.DataFrame, fdr: pd.DataFrame):
    """Collapse replicate screens (media/timepoints) to one column per query
    gene, keeping for each (library gene, query gene) the entry with the
    lowest FDR (ties: largest |qGI|)."""
    qgenes = sorted({c.split("_")[0] for c in scores.columns})
    Q = pd.DataFrame(index=scores.index, columns=qgenes, dtype=float)
    FD = pd.DataFrame(index=scores.index, columns=qgenes, dtype=float)
    for g in qgenes:
        cols = [c for c in scores.columns if c.split("_")[0] == g]
        s = scores[cols].to_numpy()
        f = fdr[cols].to_numpy()
        # rank: lowest FDR wins, |qGI| breaks ties
        f_filled = np.where(np.isnan(f), np.inf, f)
        order = np.lexsort((-np.abs(np.nan_to_num(s)), f_filled), axis=1)
        best = order[:, 0]
        rows = np.arange(s.shape[0])
        Q[g] = s[rows, best]
        FD[g] = f[rows, best]
    return Q, FD


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-dir", default=".")
    ap.add_argument("--out", default="bpms.tsv")
    args = ap.parse_args()

    scores = pd.read_parquet(f"{args.data_dir}/qGI_scores.parquet")
    fdr = pd.read_parquet(f"{args.data_dir}/qGI_FDR.parquet")
    Q, FD = collapse_screens(scores, fdr)
    lib = Q.index.to_numpy()
    queries = np.array(Q.columns)
    nq = len(queries)
    qv = Q.to_numpy()
    fv = FD.to_numpy()

    sig_std = (np.abs(qv) > STD_Q) & (fv < STD_FDR)
    sig_str = (np.abs(qv) > STR_Q) & (fv < STR_FDR)
    # denoised effect matrix: significant entries only (sparsification analog)
    E = np.where(sig_std, qv, 0.0)

    lib_pos = {g: i for i, g in enumerate(lib)}

    # within-A (query x query) measured qGI, symmetrized over the two
    # directions where the partner query is itself in the library
    W = np.full((nq, nq), np.nan)
    for i, a in enumerate(queries):
        ra = lib_pos.get(a)
        for j, b in enumerate(queries):
            if i == j:
                continue
            vals = []
            rb = lib_pos.get(b)
            if rb is not None and sig_std[rb, i]:
                vals.append(qv[rb, i])
            if ra is not None and sig_std[ra, j]:
                vals.append(qv[ra, j])
            if vals:
                W[i, j] = float(np.mean(vals))
    Wn = np.nan_to_num(W)

    # z-scored library profiles (rows) for B-side PCC cohesion
    P = np.nan_to_num(qv)
    P = P - P.mean(axis=1, keepdims=True)
    norm = np.linalg.norm(P, axis=1, keepdims=True)
    norm[norm == 0] = 1.0
    P = P / norm
    # z-scored query profiles (columns, 17.8k-dim) for A-side PCC cohesion
    Pq = np.nan_to_num(qv).T
    Pq = Pq - Pq.mean(axis=1, keepdims=True)
    nq_norm = np.linalg.norm(Pq, axis=1, keepdims=True)
    nq_norm[nq_norm == 0] = 1.0
    Pq = Pq / nq_norm

    # seeds: stringent negative (library, query) pairs
    seeds = np.argwhere(sig_str & (qv < 0))
    print(f"{len(seeds)} stringent negative seed pairs")

    bpms = []
    for li, qi in seeds:
        A = {qi}          # query-gene module
        B = {li}          # library-gene module
        changed = True
        while changed:
            changed = False
            # grow B: library genes negatively tied to A, profile-coherent with B
            a_idx = sorted(A)
            cross = -E[:, a_idx].sum(axis=1)          # want negative qGI -> positive gain
            nsig = (E[:, a_idx] < 0).sum(axis=1)
            centroid = P[sorted(B)].mean(axis=0)
            pcc = P @ centroid
            cand = np.where((cross >= GAIN_MIN) & (nsig >= 1) & (pcc >= PCC_MIN_B))[0]
            cand = [c for c in cand if c not in B]
            if cand and len(B) < MAX_SIDE:
                best = max(cand, key=lambda c: cross[c])
                B.add(int(best))
                changed = True
                continue
            # grow A: queries negatively tied to B, non-antagonistic and
            # profile-coherent within A; best gain wins
            b_idx = sorted(B)
            if len(A) < MAX_SIDE:
                centroid_a = Pq[a_idx].mean(axis=0)
                pcc_a = Pq @ centroid_a
                best_q, best_gain = None, GAIN_MIN
                for cq in range(nq):
                    if cq in A:
                        continue
                    within = Wn[cq, a_idx].sum()
                    if within < WITHIN_A_FLOOR or pcc_a[cq] < PCC_MIN_A:
                        continue
                    gain = -E[b_idx, cq].sum() + within
                    if gain >= best_gain:
                        best_q, best_gain = cq, gain
                if best_q is not None:
                    A.add(int(best_q))
                    changed = True
        # iterative trim
        while True:
            a_idx, b_idx = sorted(A), sorted(B)
            size = len(A) + len(B)
            removed = False
            for cq in list(A):
                contrib = -E[b_idx, cq].sum() + Wn[cq, a_idx].sum()
                nneg = int((E[b_idx, cq] < 0).sum())
                if nneg < TRIM_MIN_EDGES or contrib / size < TRIM_MIN_CONTRIB:
                    A.remove(cq)
                    removed = True
            a_idx = sorted(A)
            for cl in list(B):
                contrib = -E[cl, a_idx].sum()
                nneg = int((E[cl, a_idx] < 0).sum())
                if nneg < TRIM_MIN_EDGES or contrib / size < TRIM_MIN_CONTRIB:
                    B.remove(cl)
                    removed = True
            if not removed:
                break
        # GIDEON centering analog: the BPM must still be "about" its seed
        if qi not in A or li not in B:
            continue
        if len(A) < MIN_SIDE or len(B) < MIN_SIDE:
            continue
        a_idx, b_idx = sorted(A), sorted(B)
        cross_neg = float(-E[b_idx][:, a_idx][E[b_idx][:, a_idx] < 0].sum())
        cross_pos = float(E[b_idx][:, a_idx][E[b_idx][:, a_idx] > 0].sum())
        within_a = float(Wn[np.ix_(a_idx, a_idx)].sum() / 2)
        score = (cross_neg - cross_pos + within_a) / (len(A) + len(B))
        bpms.append({
            "seed": f"{queries[qi]}~{lib[li]}",
            "score": score,
            "A": frozenset(queries[i] for i in A),
            "B": frozenset(lib[i] for i in B),
            "cross_neg": cross_neg,
            "cross_pos": cross_pos,
            "within_a": within_a,
        })

    # Jaccard pruning
    bpms.sort(key=lambda b: -b["score"])
    kept = []
    for b in bpms:
        u = b["A"] | b["B"]
        ok = True
        for k in kept:
            ku = k["A"] | k["B"]
            if len(u & ku) / len(u | ku) >= JACCARD_MAX:
                ok = False
                break
        if ok:
            kept.append(b)
    print(f"{len(bpms)} raw BPMs -> {len(kept)} after Jaccard pruning")

    rows = []
    for i, b in enumerate(kept):
        rows.append({
            "bpm_id": f"BPM{i+1:04d}",
            "score": round(b["score"], 4),
            "n_query_module": len(b["A"]),
            "n_library_module": len(b["B"]),
            "seed_pair": b["seed"],
            "cross_negative_weight": round(b["cross_neg"], 3),
            "cross_positive_weight": round(b["cross_pos"], 3),
            "within_query_weight": round(b["within_a"], 3),
            "query_module": "|".join(sorted(b["A"])),
            "library_module": "|".join(sorted(b["B"])),
        })
    pd.DataFrame(rows).to_csv(args.out, sep="\t", index=False)
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
