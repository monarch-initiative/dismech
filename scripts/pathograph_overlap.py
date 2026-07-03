#!/usr/bin/env python3
"""Prototype: ontology-aware pairwise pathograph overlap across dismech disorders.

Qualitative mirror of PHBC (Nature Genetics 2026, s41588-026-02607-w): PHBC
quantifies *how much* genetic variance two diseases share; this computes *what*
mechanistic content (cell types, biological processes, genes) two disorder
pathographs share. We then test whether the overlap score tracks published
pairwise genetic correlations.

Inference is via specificity (IDF) weighting: a mechanism term shared by only a
few diseases is far more informative than one shared by many ("inflammation",
"apoptosis"). Ontology ancestor-expansion (near-parent matching) is the next
refinement; IDF is a cheap first-pass proxy for specificity.
"""
import glob
import math
import os
import sys
from collections import Counter, defaultdict

import yaml

DISORDER_DIR = "kb/disorders"

# Which ontology prefixes count as mechanistic content for the overlap.
TERM_PREFIXES = ("CL", "GO", "HP")


def walk_terms(obj, out):
    """Collect every {id,label} ontology term CURIE found anywhere in the tree."""
    if isinstance(obj, dict):
        tid = obj.get("id")
        if isinstance(tid, str) and ":" in tid:
            out.add(tid)
        for v in obj.values():
            walk_terms(v, out)
    elif isinstance(obj, list):
        for v in obj:
            walk_terms(v, out)


def gene_symbols(doc):
    """Gene symbols from the genetic section (normalized), plus any hgnc: ids."""
    syms = set()
    for g in doc.get("genetic", []) or []:
        if isinstance(g, dict):
            nm = g.get("name")
            if isinstance(nm, str) and nm.strip():
                syms.add("GENE:" + nm.strip().upper())
    return syms


def extract(path):
    doc = yaml.safe_load(open(path))
    if not isinstance(doc, dict):
        return None
    raw = set()
    walk_terms(doc.get("pathophysiology", []), raw)
    # phenotypes live at top level too
    walk_terms(doc.get("phenotypes", []), raw)
    terms = {t for t in raw if t.split(":")[0] in TERM_PREFIXES}
    terms |= gene_symbols(doc)
    return terms


def load_corpus():
    docs = {}
    for path in sorted(glob.glob(os.path.join(DISORDER_DIR, "*.yaml"))):
        if path.endswith(".history.yaml"):
            continue
        name = os.path.basename(path)[:-5]
        try:
            terms = extract(path)
        except Exception as e:
            print(f"skip {name}: {e}", file=sys.stderr)
            continue
        if terms:
            docs[name] = terms
    return docs


def idf_weights(docs):
    N = len(docs)
    df = Counter()
    for terms in docs.values():
        for t in terms:
            df[t] += 1
    return {t: math.log(N / c) for t, c in df.items()}, df


def weighted_overlap(a, b, w, min_shared=2):
    """Symmetric weighted Jaccard: shared weight / union weight.

    Jaccard (not overlap coefficient) so a 1-term disease fully contained in a
    large pathograph does NOT score 1.0 -- we want genuine bilateral mechanistic
    similarity, which is what should track a symmetric genetic correlation.
    Requires >= min_shared shared terms to score, to suppress single-term noise.
    """
    inter = a & b
    if len(inter) < min_shared:
        return 0.0
    def sw(s):
        return sum(w[t] for t in s)
    union = sw(a | b)
    return sw(inter) / union if union else 0.0


# --------------------------------------------------------------------------
# Genetics validation: does pathograph overlap track published genetic rg?
# Illustrative consensus LDSC estimates from the cross-trait genetic-correlation
# literature (Bulik-Sullivan 2015 atlas; Brainstorm Consortium 2018; PGC
# cross-disorder; IBD/autoimmune LDSC). Approximate, for prototype ranking only.
# Each pair -> (|rg|, dismech_file_a, dismech_file_b).
# --------------------------------------------------------------------------
RG_PAIRS = [
    # strong (|rg| >= 0.45)
    (0.70, "Major_Depressive_Disorder", "Generalized_Anxiety_Disorder"),
    (0.68, "Schizophrenia", "Bipolar_Disorder"),
    (0.56, "Crohn_Disease", "Ulcerative_Colitis"),
    (0.49, "Type_2_Diabetes_Mellitus", "Obesity"),
    (0.45, "Graves_Disease", "Hashimotos_Thyroiditis"),
    # moderate (0.25 - 0.45)
    (0.42, "Attention_Deficit-Hyperactivity_Disorder", "Major_Depressive_Disorder"),
    (0.36, "Bipolar_Disorder", "Major_Depressive_Disorder"),
    (0.35, "Type_2_Diabetes_Mellitus", "Coronary_Artery_Disease"),
    (0.34, "Schizophrenia", "Major_Depressive_Disorder"),
    (0.34, "Rheumatoid_Arthritis", "Type_I_Diabetes"),
    (0.32, "Asthma", "Atopic_Dermatitis"),
    (0.30, "Celiac_Disease", "Type_I_Diabetes"),
    (0.30, "Coronary_Artery_Disease", "Ischemic_Stroke"),
    (0.28, "Rheumatoid_Arthritis", "Systemic_Lupus_Erythematosus"),
    (0.27, "Crohn_Disease", "Psoriasis"),
    # weak / near-zero negative controls (|rg| < 0.15)
    (0.12, "Obesity", "Major_Depressive_Disorder"),
    (0.10, "Parkinsons_Disease", "Major_Depressive_Disorder"),
    (0.08, "Multiple_Sclerosis", "Schizophrenia"),
    (0.05, "Schizophrenia", "Coronary_Artery_Disease"),
    (0.05, "Alzheimer_Disease", "Type_2_Diabetes_Mellitus"),
    (0.03, "Rheumatoid_Arthritis", "Coronary_Artery_Disease"),
    (0.02, "Schizophrenia", "Type_2_Diabetes_Mellitus"),
]


def _ranks(xs):
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    r = [0.0] * len(xs)
    i = 0
    while i < len(xs):
        j = i
        while j + 1 < len(xs) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1
        for k in range(i, j + 1):
            r[order[k]] = avg
        i = j + 1
    return r


def _corr(a, b):
    n = len(a)
    ma, mb = sum(a) / n, sum(b) / n
    cov = sum((a[i] - ma) * (b[i] - mb) for i in range(n))
    va = sum((x - ma) ** 2 for x in a) ** 0.5
    vb = sum((x - mb) ** 2 for x in b) ** 0.5
    return cov / (va * vb) if va and vb else float("nan")


def validate(docs, w):
    print("\n" + "=" * 72)
    print("GENETICS VALIDATION: pathograph overlap vs published genetic rg")
    print("=" * 72)
    rows, rg, ov = [], [], []
    for r, a, b in RG_PAIRS:
        if a not in docs or b not in docs:
            print(f"  [skip: missing] {a} / {b}")
            continue
        s = weighted_overlap(docs[a], docs[b], w)
        rows.append((r, s, a, b))
        rg.append(r)
        ov.append(s)
    rows.sort(reverse=True)
    print(f"\n{'|rg|':>5}  {'overlap':>7}   disease pair")
    for r, s, a, b in rows:
        print(f"{r:5.2f}  {s:7.3f}   {a}  <->  {b}")

    rho = _corr(_ranks(rg), _ranks(ov))
    pear = _corr(rg, ov)
    hi = [s for r, s, *_ in rows if r >= 0.30]
    lo = [s for r, s, *_ in rows if r < 0.15]
    print(f"\nn pairs tested            : {len(rows)}")
    print(f"Spearman rho(|rg|, overlap): {rho:.3f}")
    print(f"Pearson  r  (|rg|, overlap): {pear:.3f}")
    print(f"mean overlap  strong (|rg|>=0.30): {sum(hi)/len(hi):.3f}  (n={len(hi)})")
    print(f"mean overlap  weak   (|rg|<0.15) : {sum(lo)/len(lo):.3f}  (n={len(lo)})")


def _oak_parents(prefix, terms, cache="/tmp/oak_parents.json"):
    """Direct is_a parents per ontology via OAK, cached to JSON."""
    import json
    import subprocess
    store = {}
    if os.path.exists(cache):
        store = json.load(open(cache))
    want = sorted(t for t in terms if t not in store)
    onto = {"GO": "go", "CL": "cl", "HP": "hp"}[prefix]
    BATCH = 400
    for i in range(0, len(want), BATCH):
        chunk = want[i:i + BATCH]
        out = subprocess.run(
            ["uv", "run", "runoak", "-i", f"sqlite:obo:{onto}",
             "relationships", "-p", "i"] + chunk,
            capture_output=True, text=True, timeout=600).stdout
        for t in chunk:
            store.setdefault(t, [])
        for line in out.splitlines()[1:]:
            f = line.split("\t")
            if len(f) >= 3 and f[1] == "rdfs:subClassOf" and f[2].startswith(prefix):
                store[f[0]].append(f[2])
    json.dump(store, open(cache, "w"))
    return store


def expand_corpus(docs, hops=2):
    """Add k-hop is_a ancestors to each disorder's term set."""
    onto_terms = defaultdict(set)
    for terms in docs.values():
        for t in terms:
            p = t.split(":")[0]
            if p in ("GO", "CL", "HP"):
                onto_terms[p].add(t)
    parents = {}
    for p, ts in onto_terms.items():
        print(f"  fetching is_a parents for {len(ts)} {p} terms...", file=sys.stderr)
        parents.update(_oak_parents(p, ts))

    def ancestors(t):
        seen, frontier = set(), {t}
        for _ in range(hops):
            nxt = set()
            for x in frontier:
                nxt |= set(parents.get(x, []))
            nxt -= seen
            seen |= nxt
            frontier = nxt
        return seen

    out = {}
    for name, terms in docs.items():
        e = set(terms)
        for t in list(terms):
            if t.split(":")[0] in ("GO", "CL", "HP"):
                e |= ancestors(t)
        out[name] = e
    return out


def main():
    docs = load_corpus()
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode in ("expand", "validate-expand"):
        docs = expand_corpus(docs)
    w, df = idf_weights(docs)
    if mode in ("validate", "validate-expand"):
        validate(docs, w)
        return
    all_terms = set().union(*docs.values())
    by_prefix = Counter(t.split(":")[0] for t in all_terms)
    sizes = [len(v) for v in docs.values()]

    print(f"disorders with >=1 mechanistic term : {len(docs)}")
    print(f"unique mechanistic terms            : {len(all_terms)}")
    print(f"  by type: {dict(by_prefix)}")
    print(f"terms per disorder  median/mean/max : "
          f"{sorted(sizes)[len(sizes)//2]} / {sum(sizes)/len(sizes):.1f} / {max(sizes)}")

    print("\nMost ubiquitous terms (low specificity, IDF-downweighted):")
    for t, c in df.most_common(12):
        print(f"  {c:4d}  {t}")

    # Top overlapping pairs across the whole corpus.
    # Restrict ranking to reasonably rich pathographs (>=8 terms) to cut noise.
    names = [n for n in docs if len(docs[n]) >= 8]
    print(f"\nranking restricted to {len(names)} disorders with >=8 terms")
    print(f"\nComputing pairwise overlap over {len(names)} disorders "
          f"({len(names)*(len(names)-1)//2:,} pairs)...")
    top = []
    for i in range(len(names)):
        ai = docs[names[i]]
        for j in range(i + 1, len(names)):
            s = weighted_overlap(ai, docs[names[j]], w)
            if s > 0:
                top.append((s, names[i], names[j]))
    top.sort(reverse=True)
    print(f"pairs with nonzero overlap: {len(top):,}\n")
    print("Top 20 highest-overlap disorder pairs:")
    for s, a, b in top[:20]:
        print(f"  {s:.3f}  {a}  <->  {b}")

    return docs, w


if __name__ == "__main__":
    main()
