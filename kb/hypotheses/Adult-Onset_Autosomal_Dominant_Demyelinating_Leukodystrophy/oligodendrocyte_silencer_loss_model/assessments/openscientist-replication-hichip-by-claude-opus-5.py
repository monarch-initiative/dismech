"""Independent check of OpenScientist's HiChIP claims at the LMNB1 locus.

Reads only the needed chr5 slice of each remote 4DN .mcool (10 kb, raw counts;
these files carry no balancing weights) through HTTP range requests.

Metrics (defined here, because the provider saved no code):
  promoter_ratio = cis contacts of the LMNB1 TSS bin within 20 kb-1 Mb, divided
                   by the same quantity for the CANX TSS bin (housekeeping
                   comparator on the same chromosome).
  insulation     = log2(mean contacts in a 100 kb x 100 kb square straddling
                   each bin / regional mean of that score), chr5:125.5-128.0 Mb;
                   local minima are reported inside 126.0-126.8 Mb.
  overlap_oe     = contacts between the LMNB1 TSS bin and the bins of the
                   GRCh38 overlap of the two ADLD deletions, divided by the
                   distance-matched mean contact for that bin pair.

Usage: python -I hichip_lmnb1.py <out_csv> <label=accession> ...
"""
import csv
import json
import sys
import urllib.request

import cooler
import fsspec
import h5py
import numpy as np

RES = 10_000
CHROM = "chr5"
LMNB1_TSS = 126_776_623      # Ensembl GRCh38, + strand
CANX_TSS = 179_678_615       # Ensembl GRCh38, + strand
OVERLAP = (126_519_319, 126_707_361)  # Ensembl liftover of the two deletions
REGION = (125_500_000, 128_000_000)


def uuid_for(acc):
    url = f"https://data.4dnucleome.org/files-processed/{acc}/?format=json&frame=object"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    return json.load(urllib.request.urlopen(req, timeout=60))["uuid"]


def open_cooler(acc):
    url = (f"https://4dn-open-data-public.s3.amazonaws.com/fourfront-webprod/"
           f"wfoutput/{uuid_for(acc)}/{acc}.mcool")
    fh = fsspec.open(url, "rb", block_size=4 * 2**20).open()
    h5 = h5py.File(fh, "r")
    return cooler.Cooler(h5[f"resolutions/{RES}"]), url


def promoter_sum(clr, tss):
    start = max(0, tss - 1_000_000)
    m = clr.matrix(balance=False).fetch(f"{CHROM}:{start}-{tss + 1_000_000}")
    i = (tss - start) // RES
    row = m[i].astype(float)
    d = np.abs(np.arange(len(row)) - i)
    return row[(d >= 2) & (d <= 100)].sum()


def main(out_csv, pairs):
    rows = []
    for pair in pairs:
        label, acc = pair.split("=")
        clr, url = open_cooler(acc)
        assert CHROM in clr.chromnames, clr.chromnames[:5]
        lm, cx = promoter_sum(clr, LMNB1_TSS), promoter_sum(clr, CANX_TSS)
        m = clr.matrix(balance=False).fetch(f"{CHROM}:{REGION[0]}-{REGION[1]}").astype(float)
        n, w = len(m), 10
        ins = np.full(n, np.nan)
        for k in range(w, n - w):
            ins[k] = m[k - w:k, k + 1:k + 1 + w].mean()
        ins = np.log2(ins / np.nanmean(ins))
        lo, hi = (126_000_000 - REGION[0]) // RES, (126_800_000 - REGION[0]) // RES
        minima = [REGION[0] + k * RES for k in range(lo + 1, hi)
                  if ins[k] < ins[k - 1] and ins[k] < ins[k + 1] and ins[k] < -0.3]
        expected = {dd: np.nanmean(np.diagonal(m, dd)) for dd in range(n)}
        p = (LMNB1_TSS - REGION[0]) // RES
        a, b = (OVERLAP[0] - REGION[0]) // RES, (OVERLAP[1] - REGION[0]) // RES
        obs = m[p, a:b + 1]
        exp = np.array([expected[abs(p - j)] for j in range(a, b + 1)])
        rows.append({
            "label": label, "file": acc, "url": url,
            "lmnb1_promoter_contacts": int(lm), "canx_promoter_contacts": int(cx),
            "promoter_ratio": round(lm / cx, 3),
            "insulation_minima_126.0_126.8Mb": ";".join(f"{x/1e6:.2f}" for x in minima),
            "insulation_at_minimum": ";".join(
                f"{ins[(x - REGION[0]) // RES]:.2f}" for x in minima),
            "overlap_oe": round(obs.sum() / exp.sum(), 3),
        })
        print(rows[-1], flush=True)
    with open(out_csv, "w", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=list(rows[0]))
        wr.writeheader()
        wr.writerows(rows)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
