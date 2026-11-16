"""Endpoint analysis (DRAFT, to be frozen). Reads scored candidates and writes metrics.

Input: scored.jsonl, one row per candidate: case_id (or negative_id), arm, replicate (1|2),
run (1..3), rank, confidence, tier (final, after adjudication; "none" if no tier), and
adjudicated (bool). cases.json: per case_id its test_group, cutoff_date, split, packet_size,
has_measurable_node; per negative_id its h3_usable and packet_size.

Rules (README, *Endpoints*, *Decisions*):
  - A run hits a case at tier X and top-k when a candidate with rank <= k reaches X or better.
  - LLM arms: a case is a hit when it hits in >= 4 of its 6 runs (3 runs x 2 replicates). A1:
    a hit in both replicates. any-hit (>= 1 run) and the mean per-run hit rate are reported too.
  - Primary: top-10 T2, A2 vs A3, exact two-sided McNemar on paired per-case outcomes.
  - Confirmatory secondary: A2 vs A5. Exploratory (labelled): A1 vs A5, A2 vs A6.
  - Every comparison reports the paired difference with a 95% cluster-bootstrap CI (test_group
    clusters) and the discordant-pair odds ratio with an exact (Clopper-Pearson) CI.
  - H3: AUROC of case confidence (max over candidates and runs) for positives vs H3-usable
    negatives, pooled and within packet-size tertiles, with a 95% cluster-bootstrap CI (each
    negative its own cluster). Restricted to positives with a measurable node when that flag is
    present; unrestricted AUROC is also reported.
  - Sensitivity: one case per test_group (earliest cutoff, ties by case_id).
  - Every number is marked PROVISIONAL until every candidate is adjudicated and the human
    adjudication sample is complete.

Usage: python analysis.py scored.jsonl cases.json --out metrics.json [--seed 20261114 --boot 2000]
"""
from __future__ import annotations

import argparse
import json
import math
import random
from collections import defaultdict
from pathlib import Path

TIERS = {"none": 0, "T1": 1, "T2": 2, "T3": 3, "T4": 4}
LLM_ARMS = ("A2", "A3", "A4", "A5", "A6", "A7")


def run_hits(rows, tier="T2", k=10):
    """(unit_id, arm, replicate, run) -> hit, for every run that returned output."""
    hit = defaultdict(bool)
    for r in rows:
        key = (r.get("case_id") or r.get("negative_id"), r["arm"], r["replicate"], r["run"])
        hit[key] |= (r.get("rank") or 99) <= k and TIERS.get(r.get("tier", "none"), 0) >= TIERS[tier]
    return hit


def case_outcomes(rows, arm, tier="T2", k=10):
    h = run_hits([r for r in rows if r["arm"] == arm], tier, k)
    per = defaultdict(list)
    for (cid, _, rep, run), v in h.items():
        per[cid].append((rep, v))
    out = {}
    for cid, vals in per.items():
        n = sum(v for _, v in vals)
        if arm == "A1":
            hit = all(v for _, v in vals) and len(vals) >= 2
        else:
            hit = n >= 4
        out[cid] = {"hit": hit, "any": n >= 1, "mean": n / len(vals)}
    return out


def mcnemar_exact(b: int, c: int) -> float:
    n = b + c
    if n == 0:
        return 1.0
    k = min(b, c)
    p = sum(math.comb(n, i) for i in range(k + 1)) / 2 ** n
    return min(1.0, 2 * p)


def clopper_pearson(x: int, n: int, alpha=0.05):
    if n == 0:
        return (0.0, 1.0)

    def beta_ppf(q, a, b):  # bisection on the regularised incomplete beta via continued fraction
        lo, hi = 0.0, 1.0
        for _ in range(80):
            mid = (lo + hi) / 2
            (lo, hi) = (mid, hi) if betainc(a, b, mid) < q else (lo, mid)
        return (lo + hi) / 2
    lo = 0.0 if x == 0 else beta_ppf(alpha / 2, x, n - x + 1)
    hi = 1.0 if x == n else beta_ppf(1 - alpha / 2, x + 1, n - x)
    return lo, hi


def betainc(a, b, x):
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    lbeta = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
    front = math.exp(lbeta + a * math.log(x) + b * math.log(1 - x))
    if x > (a + 1) / (a + b + 2):
        return 1 - betainc(b, a, 1 - x)
    f, c, d = 1.0, 1.0, 0.0
    for i in range(200):
        m = i // 2
        if i == 0:
            num = 1.0
        elif i % 2 == 0:
            num = m * (b - m) * x / ((a + 2 * m - 1) * (a + 2 * m))
        else:
            num = -((a + m) * (a + b + m) * x) / ((a + 2 * m) * (a + 2 * m + 1))
        d = 1 + num * d
        d = 1 / d if abs(d) > 1e-30 else 1e30
        c = 1 + num / c if abs(c) > 1e-30 else 1e-30
        f *= c * d
        if abs(c * d - 1) < 1e-12:
            break
    return front * (f - 1) / a


def compare(out_a, out_b, cases, seed, boot):
    ids = sorted(set(out_a) & set(out_b))
    b = sum(out_a[i]["hit"] and not out_b[i]["hit"] for i in ids)
    c = sum(out_b[i]["hit"] and not out_a[i]["hit"] for i in ids)
    diff = (b - c) / len(ids) if ids else float("nan")
    clusters = defaultdict(list)
    for i in ids:
        clusters[cases[i]["test_group"]].append(i)
    rng, keys, ds = random.Random(seed), sorted(clusters), []
    for _ in range(boot if ids else 0):
        pick = [i for g in rng.choices(keys, k=len(keys)) for i in clusters[g]]
        ds.append(sum(out_a[i]["hit"] - out_b[i]["hit"] for i in pick) / len(pick))
    ds.sort()
    p_lo, p_hi = clopper_pearson(b, b + c)
    odds = (lambda p: p / (1 - p) if p < 1 else float("inf"))
    return {"n_cases": len(ids), "discordant_b": b, "discordant_c": c, "mcnemar_p": mcnemar_exact(b, c),
            "rate_a": sum(out_a[i]["hit"] for i in ids) / len(ids) if ids else None,
            "rate_b": sum(out_b[i]["hit"] for i in ids) / len(ids) if ids else None,
            "paired_difference": diff,
            "paired_difference_ci95": [ds[int(0.025 * len(ds))], ds[int(0.975 * len(ds)) - 1]] if ds else None,
            "discordant_odds_ratio": (b / c) if c else float("inf") if b else None,
            "discordant_odds_ratio_ci95": [odds(p_lo), odds(p_hi)] if b + c else None}


def auroc(pos, neg):
    if not pos or not neg:
        return None
    s = sum((p > n) + 0.5 * (p == n) for p in pos for n in neg)
    return s / (len(pos) * len(neg))


def h3(rows, cases, arm, seed, boot):
    conf = defaultdict(float)
    for r in rows:
        if r["arm"] == arm:
            uid = r.get("case_id") or r.get("negative_id")
            conf[uid] = max(conf[uid], float(r.get("confidence") or 0))
    pos = [u for u in conf if u in cases and not cases[u].get("negative")]
    neg = [u for u in conf if u in cases and cases[u].get("negative") and cases[u].get("h3_usable") == "yes"]
    restricted = [u for u in pos if cases[u].get("has_measurable_node", True)]

    def one(p, n):
        res = {"auroc": auroc([conf[u] for u in p], [conf[u] for u in n]), "n_pos": len(p), "n_neg": len(n)}
        clusters = defaultdict(list)
        for u in p:
            clusters[("P", cases[u]["test_group"])].append(u)
        for u in n:
            clusters[("N", u)].append(u)
        rng, keys, vals = random.Random(seed), sorted(clusters), []
        for _ in range(boot if p and n else 0):
            pick = [u for g in rng.choices(keys, k=len(keys)) for u in clusters[g]]
            a = auroc([conf[u] for u in pick if u in p], [conf[u] for u in pick if u in n])
            if a is not None:
                vals.append(a)
        vals.sort()
        res["ci95"] = [vals[int(0.025 * len(vals))], vals[int(0.975 * len(vals)) - 1]] if vals else None
        return res

    sizes = sorted(cases[u]["packet_size"] for u in restricted + neg if cases[u].get("packet_size") is not None)
    cuts = [sizes[len(sizes) // 3], sizes[2 * len(sizes) // 3]] if len(sizes) >= 3 else None
    tert = {}
    if cuts:
        for t, (lo, hi) in enumerate([(-1, cuts[0]), (cuts[0], cuts[1]), (cuts[1], float("inf"))], 1):
            inside = (lambda u: lo < cases[u]["packet_size"] <= hi)
            tert[f"tertile_{t}"] = {**one([u for u in restricted if inside(u)], [u for u in neg if inside(u)]),
                                    "packet_size_range": [lo, hi]}
    return {"pooled_restricted": one(restricted, neg), "pooled_unrestricted": one(pos, neg), "by_packet_tertile": tert}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("scored", type=Path)
    ap.add_argument("cases", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--seed", type=int, default=20261114)
    ap.add_argument("--boot", type=int, default=2000)
    a = ap.parse_args()
    rows = [json.loads(l) for l in a.scored.read_text().splitlines() if l.strip()]
    cases = json.loads(a.cases.read_text())
    provisional = not rows or not all(r.get("adjudicated") for r in rows) or not cases.get("_human_sample_complete")
    cases.pop("_human_sample_complete", None)
    pos_rows = [r for r in rows if r.get("case_id")]
    arms = sorted({r["arm"] for r in rows})
    outc = {arm: case_outcomes(pos_rows, arm) for arm in arms}
    rep = {"status": "PROVISIONAL" if provisional else "FINAL", "arms": {}}
    for arm in arms:
        o = outc[arm]
        rep["arms"][arm] = {
            "n_cases": len(o), "hit_rate_T2_top10": sum(v["hit"] for v in o.values()) / len(o) if o else None,
            "any_hit_rate": sum(v["any"] for v in o.values()) / len(o) if o else None,
            "mean_run_hit_rate": sum(v["mean"] for v in o.values()) / len(o) if o else None,
            "tier_rates_top10": {t: _rate(case_outcomes(pos_rows, arm, t, 10)) for t in ("T1", "T2", "T3", "T4")},
            "T2_rates_topk": {k: _rate(case_outcomes(pos_rows, arm, "T2", k)) for k in (1, 3, 5, 10)},
        }
    pairs = {"primary_A2_vs_A3": ("A2", "A3"), "confirmatory_A2_vs_A5": ("A2", "A5"),
             "exploratory_A1_vs_A5": ("A1", "A5"), "exploratory_A2_vs_A6": ("A2", "A6")}
    rep["comparisons"] = {name: compare(outc[x], outc[y], cases, a.seed, a.boot)
                          for name, (x, y) in pairs.items() if x in outc and y in outc}
    reps = _representatives(cases)
    rep["sensitivity_one_case_per_group"] = {
        name: compare({i: v for i, v in outc[x].items() if i in reps}, {i: v for i, v in outc[y].items() if i in reps},
                      cases, a.seed, a.boot) for name, (x, y) in pairs.items() if x in outc and y in outc}
    rep["H3"] = {arm: h3(rows, cases, arm, a.seed, a.boot) for arm in arms}
    rep["alarms"] = sum(bool(r.get("alarms")) for r in rows)
    a.out.write_text(json.dumps(rep, indent=2) + "\n")
    print(f"{rep['status']}: {len(rows)} scored candidates, arms {arms}")


def _rate(o):
    return sum(v["hit"] for v in o.values()) / len(o) if o else None


def _representatives(cases):
    best = {}
    for cid, c in cases.items():
        if c.get("negative"):
            continue
        g = c["test_group"]
        if g not in best or (c["cutoff_date"], cid) < (cases[best[g]]["cutoff_date"], best[g]):
            best[g] = cid
    return set(best.values())


if __name__ == "__main__":
    main()
