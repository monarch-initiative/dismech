#!/usr/bin/env python3
"""Find candidate public datasets for a dismech disorder entry.

This is the deterministic complement to ``just research-datasets`` (which asks a
deep-research provider). Everything this script emits is **real by
construction**: candidates come back from the NCBI GEO DataSets index itself, so
the accession, title, organism, sample count, platform, and linked PMIDs are the
repository's own metadata rather than a model's recollection of it.

Search strategy, in order of specificity:

1. the disorder's own name and its MONDO term label
2. MONDO exact synonyms (pulled with OAK, so rare-disease aliases are covered)
3. causal genes from the entry's ``genetic:`` block, for rare disorders whose
   name never appears in a dataset title

Candidates are scored on how directly they speak to the disease (name in title
beats name anywhere; patient tissue beats cell line; human beats model organism;
having a linked publication and a usable sample count both help) so the top of
the list is what a curator should look at first.

Usage
-----
    # candidates for one disorder
    uv run python scripts/discover_datasets.py Asthma

    # machine-readable, for a curation agent
    uv run python scripts/discover_datasets.py Asthma --limit 15 --json out.json

    # which entries still have no datasets at all
    uv run python scripts/discover_datasets.py --coverage
    uv run python scripts/discover_datasets.py --coverage --format slugs
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass, field
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
KB_DIR = REPO_ROOT / "kb" / "disorders"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
USER_AGENT = "dismech-dataset-discovery (https://github.com/monarch-initiative/dismech)"

# GEO's free-text "gdstype" -> the schema's DatasetTypeEnum. Order matters: the
# first match wins, so put the more specific assay first.
GDSTYPE_TO_ENUM: list[tuple[str, str]] = [
    ("single cell", "SINGLE_CELL_RNA_SEQ"),
    ("spatial", "SPATIAL_TRANSCRIPTOMICS"),
    ("methylation profiling", "METHYLATION"),
    ("genome methylation", "METHYLATION"),
    ("genome binding/occupancy", "CHIP_SEQ"),
    ("chip-seq", "CHIP_SEQ"),
    ("atac", "ATAC_SEQ"),
    ("protein profiling", "PROTEOMICS"),
    ("metabolomic", "METABOLOMICS"),
    ("snp genotyping", "GWAS"),
    ("genome variation profiling", "GWAS"),
    ("expression profiling by high throughput sequencing", "BULK_RNA_SEQ"),
    ("expression profiling by array", "MICROARRAY"),
    ("non-coding rna profiling by array", "MICROARRAY"),
    ("non-coding rna profiling by high throughput sequencing", "BULK_RNA_SEQ"),
    ("genome variation profiling by high throughput sequencing", "WGS"),
]

# Words that indicate the samples are patient material rather than a cell line.
PRIMARY_TISSUE_HINTS = (
    "patient", "biopsy", "post-mortem", "postmortem", "autopsy", "cohort",
    "peripheral blood", "pbmc", "whole blood", "serum", "plasma", "primary",
    "surgical", "resection", "explant",
)
MODEL_HINTS = ("cell line", "hek293", "hela", "k562", "ipsc", "organoid", "knockout", "knock-out")


def http_json(url: str, retries: int = 3) -> dict | None:
    last: Exception | None = None
    for attempt in range(retries):
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                return json.loads(resp.read().decode("utf-8", "replace"))
        except Exception as exc:  # noqa: BLE001
            last = exc
            time.sleep(1.5 * (attempt + 1))
    print(f"WARN  NCBI request failed: {last}", file=sys.stderr)
    return None


def eutils_params(extra: dict) -> str:
    params = dict(extra)
    key = os.environ.get("NCBI_API_KEY")
    if key:
        params["api_key"] = key
    return urllib.parse.urlencode(params)


@dataclass
class Candidate:
    accession: str
    title: str = ""
    summary: str = ""
    data_type: str = ""
    gds_type: str = ""
    organism: str = ""
    sample_count: int | None = None
    platform: str = ""
    pubmed_ids: list[str] = field(default_factory=list)
    release_date: str = ""
    matched_query: str = ""
    score: float = 0.0
    score_notes: list[str] = field(default_factory=list)
    # DIRECT   -- the disease (or a synonym) is named in the dataset's own metadata
    # GENE_ONLY-- matched only via a causal gene; the dataset may be about an
    #             entirely different disease and MUST be triaged before curation
    relevance: str = "GENE_ONLY"


def map_data_type(gds_type: str) -> str:
    low = (gds_type or "").lower()
    hits = [enum for token, enum in GDSTYPE_TO_ENUM if token in low]
    if not hits:
        return ""
    if len(set(hits)) > 1:
        return "MULTI_OMICS"
    return hits[0]


def mondo_synonyms(mondo_id: str) -> list[str]:
    """Exact synonyms for a MONDO term, via the local OAK sqlite adapter."""
    if not mondo_id:
        return []
    try:
        out = subprocess.run(
            ["uv", "run", "runoak", "-i", "sqlite:obo:mondo", "info", mondo_id, "-O", "obo"],
            capture_output=True, text=True, timeout=180, cwd=REPO_ROOT,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return []
    syns = []
    for line in out.stdout.splitlines():
        m = re.match(r'\s*synonym:\s*"([^"]+)"\s+EXACT', line)
        if m:
            syns.append(m.group(1))
    return syns


def load_entry(slug: str) -> dict:
    path = KB_DIR / f"{slug}.yaml"
    if not path.exists():
        sys.exit(f"Error: no such disorder entry: {path}")
    return yaml.safe_load(path.read_text()) or {}


def build_queries(entry: dict, slug: str, use_synonyms: bool = True) -> list[tuple[str, str]]:
    """Return [(label, geo_search_term)] from most to least specific."""
    names: list[str] = []
    name = (entry.get("name") or slug).replace("_", " ")
    names.append(name)

    dt = entry.get("disease_term") or {}
    label = ((dt.get("term") or {}).get("label") or "").strip()
    mondo_id = ((dt.get("term") or {}).get("id") or "").strip()
    if label and label.lower() != name.lower():
        names.append(label)

    if use_synonyms:
        for syn in mondo_synonyms(mondo_id):
            # Skip acronyms and very short aliases: they generate noise in GEO.
            if len(syn) >= 8 and syn.lower() not in {n.lower() for n in names}:
                names.append(syn)

    queries: list[tuple[str, str]] = []
    for n in names[:6]:
        esc = n.replace('"', "")
        queries.append((f"name:{n}", f'"{esc}"[All Fields] AND "gse"[Entry Type]'))

    # Causal genes -- the fallback that rescues rare disorders whose name never
    # appears in a GEO title.
    genes = []
    for g in entry.get("genetic") or []:
        sym = (((g.get("gene_term") or {}).get("term") or {}).get("label") or g.get("name") or "").strip()
        if sym and re.fullmatch(r"[A-Z0-9orf\-]{2,10}", sym):
            genes.append(sym)
    for sym in list(dict.fromkeys(genes))[:4]:
        queries.append((f"gene:{sym}", f'"{sym}"[Title] AND "gse"[Entry Type]'))

    return queries


def search_geo(term: str, retmax: int) -> list[str]:
    data = http_json(f"{EUTILS}/esearch.fcgi?{eutils_params({'db': 'gds', 'term': term, 'retmode': 'json', 'retmax': str(retmax), 'sort': 'relevance'})}")
    return ((data or {}).get("esearchresult") or {}).get("idlist") or []


def summarize_geo(uids: list[str]) -> list[dict]:
    if not uids:
        return []
    docs: list[dict] = []
    for i in range(0, len(uids), 50):
        chunk = uids[i : i + 50]
        data = http_json(f"{EUTILS}/esummary.fcgi?{eutils_params({'db': 'gds', 'id': ','.join(chunk), 'retmode': 'json'})}")
        result = (data or {}).get("result") or {}
        for uid in chunk:
            if uid in result:
                docs.append(result[uid])
        time.sleep(0.12 if os.environ.get("NCBI_API_KEY") else 0.35)
    return docs


def score_candidate(cand: Candidate, disease_terms: list[str]) -> None:
    """Rank by how directly the dataset speaks to this disease."""
    score = 0.0
    notes = []
    hay_title = cand.title.lower()
    hay_all = f"{cand.title} {cand.summary}".lower()

    if any(t.lower() in hay_title for t in disease_terms):
        score += 5.0
        notes.append("disease named in title")
        cand.relevance = "DIRECT"
    elif any(t.lower() in hay_all for t in disease_terms):
        score += 2.0
        notes.append("disease named in summary")
        cand.relevance = "DIRECT"
    else:
        # Matched only through a causal gene. The dataset is real, but it is
        # very often about a different disease entirely (e.g. an FTL search for
        # neuroferritinopathy surfaces Alzheimer and medulloblastoma studies),
        # so it must never be curated on the strength of the match alone.
        score -= 2.0
        notes.append("GENE-ONLY match - triage before use")

    if "homo sapiens" in cand.organism.lower():
        score += 2.0
        notes.append("human")
    elif cand.organism:
        score += 0.5
        notes.append(f"model organism ({cand.organism})")

    if any(h in hay_all for h in PRIMARY_TISSUE_HINTS):
        score += 1.5
        notes.append("patient/primary material")
    elif any(h in hay_all for h in MODEL_HINTS):
        score += 0.5
        notes.append("model system")

    if cand.pubmed_ids:
        score += 1.5
        notes.append("linked publication")

    n = cand.sample_count or 0
    if n >= 100:
        score += 1.5
        notes.append(f"n={n}")
    elif n >= 20:
        score += 1.0
        notes.append(f"n={n}")
    elif n >= 6:
        score += 0.5
        notes.append(f"n={n}")
    elif n:
        notes.append(f"n={n} (small)")

    if cand.data_type in ("SINGLE_CELL_RNA_SEQ", "SPATIAL_TRANSCRIPTOMICS", "MULTI_OMICS"):
        score += 0.5
        notes.append("high-resolution assay")

    try:
        year = int((cand.release_date or "")[:4])
        if year >= 2018:
            score += 0.5
            notes.append(str(year))
    except ValueError:
        pass

    cand.score = round(score, 2)
    cand.score_notes = notes


def discover(slug: str, limit: int, per_query: int, use_synonyms: bool) -> list[Candidate]:
    entry = load_entry(slug)
    queries = build_queries(entry, slug, use_synonyms)
    disease_terms = [q[0].split(":", 1)[1] for q in queries if q[0].startswith("name:")]

    seen: dict[str, Candidate] = {}
    for label, term in queries:
        uids = search_geo(term, per_query)
        for doc in summarize_geo(uids):
            acc = doc.get("accession") or ""
            if not acc.startswith("GSE") or acc in seen:
                continue
            try:
                n = int(doc.get("n_samples") or 0) or None
            except (TypeError, ValueError):
                n = None
            cand = Candidate(
                accession=f"geo:{acc}",
                title=doc.get("title") or "",
                summary=(doc.get("summary") or "")[:1200],
                gds_type=doc.get("gdsType") or doc.get("gdstype") or "",
                organism=doc.get("taxon") or "",
                sample_count=n,
                platform=doc.get("gpl") or "",
                pubmed_ids=[str(p) for p in (doc.get("pubmedids") or [])],
                release_date=doc.get("pdat") or "",
                matched_query=label,
            )
            cand.data_type = map_data_type(cand.gds_type)
            score_candidate(cand, disease_terms)
            seen[acc] = cand

    ranked = sorted(seen.values(), key=lambda c: c.score, reverse=True)
    return ranked[:limit]


def coverage(fmt: str, only_missing: bool = True) -> int:
    rows = []
    for path in sorted(KB_DIR.glob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text()) or {}
        except Exception:  # noqa: BLE001
            continue
        ds = doc.get("datasets")
        n = len(ds) if isinstance(ds, list) else 0
        state = "MISSING" if n == 0 and ds is None else ("EMPTY" if n == 0 else "HAS")
        if only_missing and state == "HAS":
            continue
        rows.append((path.stem, state, n, doc.get("category") or ""))

    if fmt == "slugs":
        for slug, *_ in rows:
            print(slug)
    else:
        print("slug\tstate\tn_datasets\tcategory")
        for slug, state, n, cat in rows:
            print(f"{slug}\t{state}\t{n}\t{cat}")
        missing = sum(1 for r in rows if r[1] == "MISSING")
        empty = sum(1 for r in rows if r[1] == "EMPTY")
        total = len(list(KB_DIR.glob("*.yaml")))
        print(f"\n# {missing} entries with no datasets slot, {empty} with an empty one, "
              f"{total - missing - empty} already curated, {total} total", file=sys.stderr)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("disorder", nargs="?", help="disorder slug, e.g. Asthma")
    ap.add_argument("--limit", type=int, default=12, help="max candidates to report (default 12)")
    ap.add_argument("--per-query", type=int, default=20, help="GEO hits per search term (default 20)")
    ap.add_argument("--no-synonyms", action="store_true", help="skip the MONDO synonym expansion (faster)")
    ap.add_argument("--json", type=Path, help="write candidates to a JSON file")
    ap.add_argument("--coverage", action="store_true", help="report dataset coverage across the KB")
    ap.add_argument("--format", choices=("tsv", "slugs"), default="tsv", help="coverage output format")
    args = ap.parse_args()

    if args.coverage:
        return coverage(args.format)
    if not args.disorder:
        ap.error("pass a disorder slug, or --coverage")

    cands = discover(args.disorder, args.limit, args.per_query, not args.no_synonyms)
    if args.json:
        args.json.write_text(json.dumps([asdict(c) for c in cands], indent=2) + "\n")

    if not cands:
        print(f"No GEO candidates found for {args.disorder}.")
        print("This is a normal result for a rare disorder. Try `just research-datasets "
              f"openscientist {args.disorder}` for non-NCBI repositories.")
        return 0

    direct = sum(1 for c in cands if c.relevance == "DIRECT")
    print(f"{len(cands)} candidate dataset(s) for {args.disorder} "
          f"({direct} DIRECT, {len(cands) - direct} GENE_ONLY):\n")
    for c in cands:
        print(f"  [{c.score:>5}] {c.relevance:<9} {c.accession}  {c.data_type or '?'}  "
              f"n={c.sample_count or '?'}  {c.organism}")
        print(f"          {c.title[:120]}")
        print(f"          via {c.matched_query} | {', '.join(c.score_notes)}")
        if c.pubmed_ids:
            print(f"          PMID:{', PMID:'.join(c.pubmed_ids[:3])}")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
