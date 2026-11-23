#!/usr/bin/env python3
"""Join MMRRC holdings to dismech entries through MGI alleles and HGNC orthologs.

Sorts every MMRRC holding into one of four buckets:

  BIND     the ortholog's dismech entry already lists a mouse model whose text names
           this gene, so the holding may be that model: attach its MGI allele and stock
  ADD      the ortholog is a causal gene of a dismech entry, but no mouse record there
           names the gene
  CURATE   the ortholog is not a causal gene of any dismech entry yet
  MULTI_GENE   more than five genes (deletion or consomic strains); not a gene model
  NO_ORTHOLOG  the holding carries no gene with an HGNC ortholog (wild-type strains,
           reporters, transgene-only constructs, unmapped loci)

Inputs (all public, fetched by ``just mmrrc-fetch`` into ``data/mmrrc/``, gitignored):

* ``imsr/p*.json``   IMSR (findmice.org) report.json pages filtered to repository MMRRC
* ``HGNC_AllianceHomology.rpt``   MGI's mouse-marker -> HGNC report

Outputs: a per-holding TSV and a markdown census. This is a lead generator, not
curation. A BIND row says a free-text record mentions the same gene, not that it is
the same allele; a curator has to read the record and the allele page before binding.
"""

from __future__ import annotations

import argparse
import collections
import csv
import html
import json
import re
import sys
from pathlib import Path

import yaml

try:
    Loader = yaml.CSafeLoader
except AttributeError:  # pragma: no cover
    Loader = yaml.SafeLoader

MARKER_RE = re.compile(r"informatics\.jax\.org/marker/(MGI:\d+)'[^>]*>([^<]+)</a>")
ALLELE_RE = re.compile(r"informatics\.jax\.org/allele/(MGI:\d+)'[^>]*>(.*?)</a>")
STATE_RE = re.compile(r'class="state ([^"]+)"')
TAG_RE = re.compile(r"<[^>]+>")
MOUSE_SPECIES = re.compile(r"\b(mouse|mice|mus musculus)\b", re.IGNORECASE)
GENE_SECTIONS = ("genetic", "has_subtypes", "pathophysiology")

# IMSR state classes. Anything other than an ES cell is a mouse line (live or cryopreserved).
MOUSE_STATES = {"live", "embryo", "sperm", "oocyte", "ovary", "archived"}
CAUSAL_TYPES = {None, "CAUSATIVE", "SOMATIC_DRIVER"}
MAX_GENES = 5  # above this: ENU pedigrees (Mtgx...Btlr), deletions, consomics; not a gene model
# Safe-harbour loci used to dock transgenes. An allele there carrying a construct,
# e.g. Hprt1<tm4(Ple88-EGFP)Ems>, is a reporter or expression line, not a model of
# the host gene, so the host gene is dropped from that holding.
DOCKING_LOCI = {"Hprt1", "Hprt", "Col1a1", "Igs2", "Igs7", "H11", "Tigre"}
# A transgene that only expresses a reporter or recombinase under a gene's promoter
# (GENSAT's Tg(Ptch1-EGFP)EZ56Gsat, Cre drivers) is a tool line, not a model of that gene.
REPORTER_RE = re.compile(r"(EGFP|GFP|YFP|CFP|RFP|Venus|tdTomato|mCherry|lacZ|LacZ|cre|Cre|icre|flp|Flp|"
                         r"luc|Luc|rtTA|tTA|tdT)", re.IGNORECASE)
# Marker alleles carried for coat colour, e.g. A<tm1Brd> in KOMP lines.
MARKER_ALLELES = {"MGI:3842513"}


def allele_symbol(raw: str) -> str:
    """IMSR writes superscripts as <SUP>; MGI's text form uses <...>."""
    s = raw.replace("<SUP>", "<").replace("</SUP>", ">")
    return html.unescape(s).strip()


def load_holdings(imsr_dir: Path) -> list[dict]:
    rows: dict[str, dict] = {}
    for path in sorted(imsr_dir.glob("p*.json")):
        for r in json.loads(path.read_text())["report"]["summaryRows"]:
            sid = r["strainId"]
            if sid in rows:
                continue
            genes = dict(MARKER_RE.findall(r.get("genes", "")))
            alleles = [(a, allele_symbol(s)) for a, s in ALLELE_RE.findall(r.get("alleles", ""))]
            alleles = [(a, s) for a, s in alleles if a not in MARKER_ALLELES]
            for mgi, sym in list(genes.items()):
                own = [s for _, s in alleles if s.startswith(sym + "<")]
                tg = [s for _, s in alleles if s.startswith("Tg(") and re.search(
                    rf"[(\-:]{re.escape(sym)}[-)]", s)]
                if not own and not tg:
                    # only a marker allele named this gene (e.g. nonagouti in KOMP lines)
                    if sym == "a":
                        del genes[mgi]
                    continue
                if sym in DOCKING_LOCI and own and all("(" in s for s in own) or not own and tg and all(REPORTER_RE.search(s) for s in tg):
                    del genes[mgi]
            states = sorted(set(STATE_RE.findall(r.get("states", ""))))
            rows[sid] = {
                "stock": sid,
                "designation": html.unescape(TAG_RE.sub("", r.get("designation", ""))).strip(),
                "states": states,
                "genes": genes,
                "alleles": alleles,
            }
    return list(rows.values())


def load_homology(path: Path) -> dict[str, tuple[str, str]]:
    """MGI marker ID -> (lowercase hgnc CURIE, mouse symbol)."""
    out = {}
    with path.open() as fh:
        for rec in csv.DictReader(fh, delimiter="\t"):
            h = (rec.get("HGNC ID") or "").strip()
            if h and h != "null":
                out[rec["MGI Accession ID"]] = ("hgnc:" + h.split(":")[1], rec["Marker Symbol"])
    return out


def walk_gene_terms(node, found: set[str]):
    if isinstance(node, dict):
        term = node.get("term")
        if isinstance(term, dict):
            tid = str(term.get("id", ""))
            if tid.lower().startswith("hgnc:"):
                found.add("hgnc:" + tid.split(":", 1)[1])
        for v in node.values():
            walk_gene_terms(v, found)
    elif isinstance(node, list):
        for v in node:
            walk_gene_terms(v, found)


def index_kb(kb_dir: Path):
    """Return (causal hgnc -> entries, any-mention hgnc -> entries, entry -> mouse text).

    Causal genes are ``genetic[]`` rows typed CAUSATIVE or SOMATIC_DRIVER (or untyped)
    plus ``has_subtypes[].genes``. Every other HGNC binding in the gene sections is a
    mention: it says the gene matters to the entry, not that the entry is its disease.
    """
    causal: dict[str, set[str]] = collections.defaultdict(set)
    mention: dict[str, set[str]] = collections.defaultdict(set)
    mouse_text: dict[str, list[str]] = {}
    for path in sorted(kb_dir.glob("*.yaml")):
        doc = yaml.load(path.read_text(), Loader=Loader) or {}
        slug = path.stem
        c: set[str] = set()
        for g in doc.get("genetic") or []:
            if isinstance(g, dict) and g.get("relationship_type") in CAUSAL_TYPES:
                walk_gene_terms(g.get("gene_term") or {}, c)
        for st in doc.get("has_subtypes") or []:
            if isinstance(st, dict):
                walk_gene_terms(st.get("genes") or [], c)
        m: set[str] = set()
        for sec in GENE_SECTIONS:
            walk_gene_terms(doc.get(sec) or [], m)
        for h in c:
            causal[h].add(slug)
        for h in m - c:
            mention[h].add(slug)
        blobs = []
        for mod in doc.get("animal_models") or []:
            if MOUSE_SPECIES.search(str(mod.get("species", ""))):
                blobs.append(" ".join(str(mod.get(k, "")) for k in ("name", "genotype", "description", "genes")))
        if blobs:
            mouse_text[slug] = blobs
    return causal, mention, mouse_text


def mentions(symbol: str, blobs: list[str]) -> bool:
    pat = re.compile(rf"(?<![A-Za-z0-9]){re.escape(symbol)}(?![a-z0-9])", re.IGNORECASE)
    return any(pat.search(b) for b in blobs)


def classify(h, homology, causal, mouse_text):
    mapped = [(m, *homology[m]) for m in h["genes"] if m in homology]
    if not mapped:
        return "NO_ORTHOLOG", [], [], []
    if len(mapped) > MAX_GENES:
        return "MULTI_GENE", mapped, [], []
    entries = sorted({e for _, hg, _ in mapped for e in causal.get(hg, ())})
    if not entries:
        return "CURATE", mapped, [], []
    bind = sorted(
        e for e in entries
        if any(mentions(sym, mouse_text.get(e, [])) for _, _, sym in mapped)
    )
    return ("BIND" if bind else "ADD"), mapped, entries, bind


def kind(h) -> str:
    return "MOUSE" if MOUSE_STATES & set(h["states"]) else "ES_CELL"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--data", default="data/mmrrc", type=Path)
    ap.add_argument("--kb", default="kb/disorders", type=Path)
    ap.add_argument("--tsv", default="tmp/mmrrc_join.tsv", type=Path)
    ap.add_argument("--census", default=None, type=Path, help="markdown census output")
    ap.add_argument("--include-es-cells", action="store_true",
                    help="keep holdings that exist only as ES cells (excluded by default)")
    args = ap.parse_args(argv)

    holdings = load_holdings(args.data / "imsr")
    if not holdings:
        sys.exit(f"no IMSR pages under {args.data/'imsr'}; run `just mmrrc-fetch`")
    homology = load_homology(args.data / "HGNC_AllianceHomology.rpt")
    causal, mention, mouse_text = index_kb(args.kb)

    n_all = len(holdings)
    if not args.include_es_cells:
        holdings = [h for h in holdings if kind(h) == "MOUSE"]

    args.tsv.parent.mkdir(parents=True, exist_ok=True)
    counts = collections.Counter()
    genes_by_bucket = collections.defaultdict(set)
    entry_lines = collections.Counter()
    with args.tsv.open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["bucket", "kind", "stock", "states", "designation", "alleles", "mouse_genes",
                    "hgnc", "causal_entries", "entries_with_mouse_mention", "other_entries"])
        for h in sorted(holdings, key=lambda x: x["stock"]):
            bucket, mapped, entries, bind = classify(h, homology, causal, mouse_text)
            others = sorted({e for _, hg, _ in mapped for e in mention.get(hg, ())} - set(entries)) \
                if bucket != "MULTI_GENE" else []
            counts[bucket] += 1
            for _, hg, _ in mapped:
                genes_by_bucket[bucket].add(hg)
            for e in entries:
                entry_lines[e] += 1
            w.writerow([
                bucket, kind(h), h["stock"], ";".join(h["states"]), h["designation"],
                ";".join(f"{a} {s}" for a, s in h["alleles"]),
                ";".join(f"{m} {sym}" for m, _, sym in mapped),
                ";".join(hg for _, hg, _ in mapped),
                ";".join(entries), ";".join(bind), ";".join(others),
            ])

    total = sum(counts.values())
    lines = [f"MMRRC holdings in IMSR: {n_all}; joined: {total}"
             + ("" if args.include_es_cells else " (mouse lines only; ES-cell-only holdings excluded)")]
    for b in ("BIND", "ADD", "CURATE", "MULTI_GENE", "NO_ORTHOLOG"):
        lines.append(f"  {b:<12} {counts[b]:>6} holdings  {len(genes_by_bucket[b]):>5} human genes")
    lines.append("Entries with the most MMRRC holdings for their genes:")
    for e, n in entry_lines.most_common(15):
        lines.append(f"  {n:>5}  {e}{'  (has mouse records)' if e in mouse_text else '  (NO mouse records)'}")
    print("\n".join(lines))
    if args.census:
        args.census.write_text("```\n" + "\n".join(lines) + "\n```\n")


if __name__ == "__main__":
    main()
