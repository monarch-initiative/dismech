#!/usr/bin/env python3
"""Derive the DepMap synthetic-lethality / selective-dependency TSV.

Turns a pinned DepMap Public release into the long-format TSV consumed by
``dismech.structured_sources.depmap.DepMapSource`` (which serializes it into
``references_cache/DEPMAP_*.md``). This is the *derivation* half deliberately
left out of the source module: it computes, for each configured
``dependency_gene × genomic-context`` hypothesis, the differential CRISPR
gene-effect between context-positive and context-negative cell-line models.

Frugal by design: the ~400 MB ``CRISPRGeneEffect`` matrix and ~340 MB
``OmicsSomaticMutations`` table are **streamed** (never saved whole to disk),
keeping only the needed dependency-gene columns and the context-gene mutation
memberships. Each release file's md5 is verified on the fly against the pins in
``RELEASE``.

Statistics are intentionally simple and stated as such in the emitted rows: an
unpaired, pan-cancer, Welch two-group comparison of the dependency gene's
Chronos gene-effect (more negative = stronger dependency), **not** corrected for
lineage, BRCA zygosity, or HRD status. DepMap dependencies are IN_VITRO evidence
and must never be the sole support for a human phenotype — the derived rows are
corroborating functional-genomic signal, not clinical proof.

Usage::

    uv run python scripts/derive_depmap_synthetic_lethality.py \
        --out data/depmap/depmap_synthetic_lethality.tsv

Currently ships a single validated relationship (PARP1 selective dependency in
BRCA1/BRCA2 loss-of-function models); add entries to ``RELATIONSHIPS`` to scale.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import math
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

import requests

# ---- Pinned DepMap release (figshare) -------------------------------------

RELEASE = {
    "name": "DepMap Public 24Q4",
    "article": "27993248",
    "doi": "10.25452/figshare.plus.27993248.v1",
    "license": "CC BY 4.0",
    "files": {
        "CRISPRGeneEffect.csv": {
            "figshare_file_id": "51064667",
            "md5": "6edf7ade09b9b34199210b559d4745d3",
        },
        "OmicsSomaticMutations.csv": {
            "figshare_file_id": "51065732",
            "md5": "7bdba347a1602fe96d5654a74d6e52f1",
        },
    },
}

_NDOWNLOADER = "https://ndownloader.figshare.com/files/{fid}"

# Repo-canonical lowercase HGNC ids for the genes we reference.
_HGNC = {
    "PARP1": "hgnc:270",
    "BRCA1": "hgnc:1100",
    "BRCA2": "hgnc:1101",
}


@dataclass(frozen=True)
class Relationship:
    """One dependency_gene × context hypothesis to test."""

    dependency_gene: str  # gene whose CRISPR dependency we measure
    context_genes: tuple[str, ...]  # LoF in ANY of these defines context-positive
    context_label: str  # human label for the context
    relationship: str  # DepMapSource relationship vocabulary


RELATIONSHIPS: tuple[Relationship, ...] = (
    Relationship(
        dependency_gene="PARP1",
        context_genes=("BRCA1", "BRCA2"),
        context_label="BRCA1/BRCA2 loss-of-function",
        relationship="SELECTIVE_DEPENDENCY",
    ),
)


# ---- Streaming download with on-the-fly md5 verification -------------------


def _stream_lines(figshare_file_id: str, expected_md5: str) -> Iterable[str]:
    """Yield decoded text lines from a figshare file, verifying md5 at EOF."""
    url = _NDOWNLOADER.format(fid=figshare_file_id)
    h = hashlib.md5()
    with requests.get(url, stream=True, timeout=300) as r:
        r.raise_for_status()
        buf = b""
        for chunk in r.iter_content(chunk_size=1 << 20):
            if not chunk:
                continue
            h.update(chunk)
            buf += chunk
            *lines, buf = buf.split(b"\n")
            for line in lines:
                yield line.decode("utf-8", "replace")
        if buf:
            yield buf.decode("utf-8", "replace")
    actual = h.hexdigest()
    if expected_md5 and actual != expected_md5:
        raise RuntimeError(
            f"md5 mismatch for figshare file {figshare_file_id}: "
            f"got {actual}, expected {expected_md5}"
        )


# ---- Extraction ------------------------------------------------------------


def extract_gene_effects(genes: set[str]) -> dict[str, dict[str, float]]:
    """Stream CRISPRGeneEffect.csv → {gene_symbol: {ModelID: gene_effect}}.

    The matrix header names columns ``SYMBOL (ENTREZ)``; column 0 is ModelID.
    Only the requested gene columns are retained.
    """
    meta = RELEASE["files"]["CRISPRGeneEffect.csv"]
    it = _stream_lines(meta["figshare_file_id"], meta["md5"])
    header = next(csv.reader([next(it)]))
    col_of: dict[str, int] = {}
    for idx, col in enumerate(header):
        sym = col.split(" (", 1)[0]
        if sym in genes:
            col_of[sym] = idx
    missing = genes - set(col_of)
    if missing:
        raise RuntimeError(f"genes not found in CRISPRGeneEffect header: {missing}")
    out: dict[str, dict[str, float]] = {g: {} for g in col_of}
    for row in csv.reader(it):
        if not row or not row[0]:
            continue
        model = row[0]
        for sym, idx in col_of.items():
            val = row[idx] if idx < len(row) else ""
            if val not in ("", "NA"):
                try:
                    out[sym][model] = float(val)
                except ValueError:
                    pass
    return out


def _truthy(v: str) -> bool:
    return v.strip().lower() in {"true", "1", "yes"}


def extract_lof_models(context_genes: set[str]) -> dict[str, set[str]]:
    """Stream OmicsSomaticMutations.csv → {gene: {ModelIDs with LikelyLoF}}."""
    meta = RELEASE["files"]["OmicsSomaticMutations.csv"]
    it = _stream_lines(meta["figshare_file_id"], meta["md5"])
    header = next(csv.reader([next(it)]))
    ci = {name: i for i, name in enumerate(header)}
    g_i, m_i, lof_i = ci["HugoSymbol"], ci["ModelID"], ci["LikelyLoF"]
    out: dict[str, set[str]] = {g: set() for g in context_genes}
    for row in csv.reader(it):
        if len(row) <= max(g_i, m_i, lof_i):
            continue
        gene = row[g_i]
        if gene in context_genes and _truthy(row[lof_i]):
            out[gene].add(row[m_i])
    return out


# ---- Statistics ------------------------------------------------------------


def _mean_sd(xs: list[float]) -> tuple[float, float]:
    n = len(xs)
    m = sum(xs) / n
    if n < 2:
        return m, 0.0
    var = sum((x - m) ** 2 for x in xs) / (n - 1)
    return m, math.sqrt(var)


def _welch_t(a: list[float], b: list[float]) -> float:
    ma, sa = _mean_sd(a)
    mb, sb = _mean_sd(b)
    na, nb = len(a), len(b)
    denom = math.sqrt((sa * sa) / na + (sb * sb) / nb) if na and nb else 0.0
    return (ma - mb) / denom if denom else 0.0


def _cohens_d(a: list[float], b: list[float]) -> float:
    ma, sa = _mean_sd(a)
    mb, sb = _mean_sd(b)
    na, nb = len(a), len(b)
    if na + nb <= 2:
        return 0.0
    sp = math.sqrt(((na - 1) * sa * sa + (nb - 1) * sb * sb) / (na + nb - 2))
    return (ma - mb) / sp if sp else 0.0


def _fmt(x: float, places: int = 4) -> str:
    return f"{x:.{places}f}"


@dataclass
class Row:
    gene_a_symbol: str
    gene_a_hgnc: str
    relationship: str
    context: str
    metric_type: str
    metric_value: str
    effect_size: str
    n_models: str
    release: str
    gene_b_symbol: str = ""
    gene_b_hgnc: str = ""


COLUMNS = [
    "gene_a_symbol", "gene_a_hgnc", "gene_b_symbol", "gene_b_hgnc",
    "relationship", "context", "metric_type", "metric_value",
    "effect_size", "n_models", "release",
]


def derive_rows() -> list[Row]:
    dep_genes = {r.dependency_gene for r in RELATIONSHIPS}
    ctx_genes = {g for r in RELATIONSHIPS for g in r.context_genes}
    sys.stderr.write(f"streaming CRISPRGeneEffect.csv for {sorted(dep_genes)} ...\n")
    effects = extract_gene_effects(dep_genes)
    sys.stderr.write(f"streaming OmicsSomaticMutations.csv for {sorted(ctx_genes)} ...\n")
    lof = extract_lof_models(ctx_genes)

    rows: list[Row] = []
    for rel in RELATIONSHIPS:
        eff = effects[rel.dependency_gene]
        ctx_models: set[str] = set()
        for g in rel.context_genes:
            ctx_models |= lof.get(g, set())
        pos = [eff[m] for m in eff if m in ctx_models]
        neg = [eff[m] for m in eff if m not in ctx_models]
        mp, _ = _mean_sd(pos) if pos else (float("nan"), 0.0)
        mn, _ = _mean_sd(neg) if neg else (float("nan"), 0.0)
        t = _welch_t(pos, neg)
        d = _cohens_d(pos, neg)
        hg = _HGNC[rel.dependency_gene]
        rel_name = rel.relationship
        rows.append(Row(
            rel.dependency_gene, hg, rel_name,
            f"{rel.context_label} (mutant)", "MEAN_GENE_EFFECT",
            _fmt(mp), "", str(len(pos)), RELEASE["name"],
        ))
        rows.append(Row(
            rel.dependency_gene, hg, rel_name,
            f"{rel.context_label} wild-type", "MEAN_GENE_EFFECT",
            _fmt(mn), "", str(len(neg)), RELEASE["name"],
        ))
        rows.append(Row(
            rel.dependency_gene, hg, rel_name,
            f"{rel.context_label} vs wild-type", "DIFFERENTIAL_DEPENDENCY_WELCH_T",
            _fmt(t), _fmt(d), str(len(pos)), RELEASE["name"],
        ))
        sys.stderr.write(
            f"{rel.dependency_gene}: mut mean={_fmt(mp)} (n={len(pos)}), "
            f"WT mean={_fmt(mn)} (n={len(neg)}), Welch t={_fmt(t)}, "
            f"Cohen d={_fmt(d)}\n"
        )
    return rows


def write_tsv(rows: list[Row], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(COLUMNS)
        for r in rows:
            w.writerow([
                r.gene_a_symbol, r.gene_a_hgnc, r.gene_b_symbol, r.gene_b_hgnc,
                r.relationship, r.context, r.metric_type, r.metric_value,
                r.effect_size, r.n_models, r.release,
            ])


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--out", type=Path,
        default=Path("data/depmap/depmap_synthetic_lethality.tsv"),
        help="Output TSV path (default: data/depmap/depmap_synthetic_lethality.tsv)",
    )
    args = ap.parse_args()
    rows = derive_rows()
    write_tsv(rows, args.out)
    sys.stderr.write(f"wrote {len(rows)} rows → {args.out}\n")


if __name__ == "__main__":
    main()
