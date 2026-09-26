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
#
# IMPORTANT: `gdstype` is a small controlled vocabulary and it does NOT
# distinguish assay resolution. Every single-cell, single-nucleus and spatial
# series is labelled "Expression profiling by high throughput sequencing", and
# ATAC-seq is labelled "Genome binding/occupancy profiling by high throughput
# sequencing" -- the same value as ChIP-seq. So `gdstype` alone cannot yield
# SINGLE_CELL_RNA_SEQ, SPATIAL_TRANSCRIPTOMICS or ATAC_SEQ, and an earlier
# version of this table silently mapped 156 such series to BULK_RNA_SEQ or
# CHIP_SEQ. `refine_data_type` below recovers them from the series text.
GDSTYPE_TO_ENUM: list[tuple[str, str]] = [
    ("methylation profiling", "METHYLATION"),
    ("genome methylation", "METHYLATION"),
    ("genome binding/occupancy", "CHIP_SEQ"),
    ("chip-seq", "CHIP_SEQ"),
    ("atac", "ATAC_SEQ"),
    ("protein profiling", "PROTEOMICS"),
    ("metabolomic", "METABOLOMICS"),
    ("expression profiling by high throughput sequencing", "BULK_RNA_SEQ"),
    ("expression profiling by array", "MICROARRAY"),
    ("non-coding rna profiling by array", "MICROARRAY"),
    ("non-coding rna profiling by high throughput sequencing", "BULK_RNA_SEQ"),
    ("genome variation profiling by high throughput sequencing", "WGS"),
]

# Assay signatures GEO's `gdstype` cannot express, recovered from the series
# title and summary. Order matters: a spatial single-cell study is spatial.
ASSAY_PATTERNS: list[tuple[re.Pattern, str]] = [
    (
        re.compile(
            r"\b(spatial(?:ly)?(?:[- ]?(?:resolved|transcriptom\w*)|"
            r"(?:\W+\w+){0,5}\W+transcriptom\w*)|visium|geomx|merfish|"
            r"xenium|cosmx|slide[- ]?seq|stereo[- ]?seq)\b",
            re.IGNORECASE,
        ),
        "SPATIAL_TRANSCRIPTOMICS",
    ),
    (
        re.compile(
            r"\b(atac[- ]?seq|(?:sc|sn)atac[- ]?seq|cut&tag|cut ?& ?run|cut&run)\b",
            re.IGNORECASE,
        ),
        "ATAC_SEQ",
    ),
    (
        re.compile(
            r"\b(single[- ]cell|single[- ]nucleus|single[- ]nuclei|sc ?rna[- ]?seq|"
            r"sn ?rna[- ]?seq|scrna|snrna|cite[- ]?seq|droplet[- ]based)\b",
            re.IGNORECASE,
        ),
        "SINGLE_CELL_RNA_SEQ",
    ),
    (
        re.compile(r"\b(chip[- ]?seq|chromatin immunoprecipitation)\b", re.IGNORECASE),
        "CHIP_SEQ",
    ),
    (
        re.compile(r"\b(mass spectrom\w*|proteom\w*)\b", re.IGNORECASE),
        "PROTEOMICS",
    ),
    (
        re.compile(
            r"\b(dna methylation|methylation profil\w*|methylome)\b",
            re.IGNORECASE,
        ),
        "METHYLATION",
    ),
]

BRACKETED_TITLE_ASSAYS: list[tuple[re.Pattern, str]] = [
    (re.compile(r"\[bulk rna[- ]?seq\]", re.IGNORECASE), "BULK_RNA_SEQ"),
    (re.compile(r"\[rna[- ]?seq\]", re.IGNORECASE), "BULK_RNA_SEQ"),
    (re.compile(r"\[chip[- ]?seq\]", re.IGNORECASE), "CHIP_SEQ"),
    (re.compile(r"\[atac[- ]?seq\]", re.IGNORECASE), "ATAC_SEQ"),
    (
        re.compile(r"\[(?:sc|sn)rna[- ]?seq\]", re.IGNORECASE),
        "SINGLE_CELL_RNA_SEQ",
    ),
]

# `gdstype` values that describe only the broad modality, so the series text is
# the better authority when it names a specific assay.
UNSPECIFIC_GDSTYPES = ("expression profiling", "genome binding/occupancy", "other")


def refine_data_type(gds_type: str, text: str, mapped: str, title: str = "") -> str:
    """Upgrade a coarse `gdstype` mapping using the series' own title/summary.

    Only fires when `gdstype` is one of the broad values that cannot express
    assay resolution, so an explicit GEO label (methylation, proteomics, GWAS)
    is never overridden by a stray word in a summary.
    """
    for pattern, enum in BRACKETED_TITLE_ASSAYS:
        if pattern.search(title or ""):
            return enum

    low = (gds_type or "").lower()
    if not any(u in low for u in UNSPECIFIC_GDSTYPES):
        return mapped
    matches = {enum for pattern, enum in ASSAY_PATTERNS if pattern.search(text or "")}
    # Text may refine resolution within GEO's declared modality, but topic
    # words in a summary must not switch an RNA-seq series to proteomics,
    # methylation, or ChIP-seq.
    if "other" not in low:
        matches -= {"PROTEOMICS", "METHYLATION"}
    if "genome binding/occupancy" not in low and "other" not in low:
        matches.discard("CHIP_SEQ")
    # Comparative background text is not evidence that the submitted series
    # used a single-cell assay (for example, "Compared to single-cell
    # technologies, NETSseq ...").
    if matches == {"SINGLE_CELL_RNA_SEQ"} and re.search(
        r"\b(?:compared|in contrast) to single[- ]cell (?:technolog\w*|method\w*|approach\w*)\b",
        text or "",
        re.IGNORECASE,
    ):
        matches.clear()
    if matches == {"SPATIAL_TRANSCRIPTOMICS", "SINGLE_CELL_RNA_SEQ"}:
        return "SPATIAL_TRANSCRIPTOMICS"
    if len(matches) > 1:
        return "MULTI_OMICS"
    if matches:
        return matches.pop()
    return mapped


# Words that indicate the samples are patient material rather than a cell line.
PRIMARY_TISSUE_HINTS = (
    "patient",
    "biopsy",
    "post-mortem",
    "postmortem",
    "autopsy",
    "cohort",
    "peripheral blood",
    "pbmc",
    "whole blood",
    "serum",
    "plasma",
    "primary",
    "surgical",
    "resection",
    "explant",
)
MODEL_HINTS = (
    "cell line",
    "hek293",
    "hela",
    "k562",
    "ipsc",
    "organoid",
    "knockout",
    "knock-out",
)


def http_json(url: str, retries: int = 3) -> dict | None:
    last: Exception | None = None
    for attempt in range(retries):
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                return json.loads(resp.read().decode("utf-8", "replace"))
        except Exception as exc:
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
            [
                "uv",
                "run",
                "runoak",
                "-i",
                "sqlite:obo:mondo",
                "info",
                mondo_id,
                "-O",
                "obo",
            ],
            capture_output=True,
            text=True,
            timeout=180,
            cwd=REPO_ROOT,
            check=False,
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


# Leading qualifiers that make a dismech entry name clinically precise but stop
# it from ever matching a dataset title verbatim.
LEADING_QUALIFIERS = (
    "systemic",
    "acquired",
    "congenital",
    "primary",
    "secondary",
    "chronic",
    "acute",
    "familial",
    "hereditary",
    "idiopathic",
    "juvenile",
    "adult",
    "classic",
    "classical",
    "isolated",
    "generalized",
    "localized",
    "severe",
    "benign",
    "malignant",
    "recurrent",
    "progressive",
    "neonatal",
    "infantile",
)
STOPWORDS = {
    "and",
    "the",
    "of",
    "with",
    "due",
    "to",
    "type",
    "disease",
    "disorder",
    "syndrome",
}

# Qualifiers that distinguish *sibling diseases* rather than just phrasing.
# "Acquired partial lipodystrophy" and "familial partial lipodystrophy" are
# different diseases; "systemic AL amyloidosis" and "AL amyloidosis" are the
# same one. When the entry name carries one of these and a candidate applies a
# competing qualifier to the same core term, the candidate is about a sibling
# disease and must not be curated here.
CONTRASTING_QUALIFIERS = (
    {"acquired"},
    {"hereditary", "familial", "congenital", "inherited", "genetic"},
    {"primary", "idiopathic"},
    {"secondary"},
    {"systemic", "generalized"},
    {"localized", "local", "cutaneous"},
    {"juvenile", "infantile", "neonatal", "pediatric", "childhood"},
    {"adult"},
    {"acute"},
    {"chronic"},
)


def qualifier_group(word: str) -> frozenset[str] | None:
    for grp in CONTRASTING_QUALIFIERS:
        if word.lower() in grp:
            return frozenset(grp)
    return None


# How many words before the core term to scan for a qualifying adjective.
QUALIFIER_WINDOW = 3


def has_qualifier_conflict(text: str, entry_qualifier: str, core: str) -> str:
    """Return the competing qualifier if `text` applies one to `core`, else "".

    Scans the words immediately preceding each occurrence of the core term and
    takes the *nearest* qualifier found. An earlier single-regex version tried
    to capture the qualifier positionally and silently missed cases: in
    "causes of hereditary angioedema" the optional-intervening-word branch let
    "of" claim the match, so "hereditary" was never examined and the sibling
    disease slipped through.
    """
    if not core:
        return ""
    own = qualifier_group(entry_qualifier) or frozenset({entry_qualifier.lower()})
    low, core_l = text.lower(), core.lower()

    for m in re.finditer(re.escape(core_l), low):
        preceding = re.findall(r"[a-z]+", low[: m.start()])[-QUALIFIER_WINDOW:]
        for word in reversed(preceding):  # nearest qualifier wins
            grp = qualifier_group(word)
            if grp is None:
                continue
            if word == entry_qualifier.lower() or grp == own:
                break  # the entry's own qualifier is the closest one: not a conflict
            return word
    return ""


def core_term(name: str) -> tuple[str, str]:
    """Shorten a precise entry name to the phrase a dataset would actually use.

    Returns ``(core, stripped_qualifier)``; e.g. "Systemic AL Amyloidosis" ->
    ("AL Amyloidosis", "systemic"). Both are "" when nothing useful is left.
    """
    words = name.split()
    stripped = ""
    while len(words) > 1 and words[0].lower() in LEADING_QUALIFIERS:
        stripped = stripped or words[0].lower()
        words = words[1:]
    short = " ".join(words)
    if short.lower() == name.lower() or len(short) < 5:
        return "", ""
    return short, stripped


def build_queries(
    entry: dict, slug: str, use_synonyms: bool = True
) -> tuple[list[tuple[str, str]], list[str], list[list[str]], list[tuple[str, str]]]:
    """Build the GEO queries and the terms used to judge relevance.

    Returns ``(queries, phrases, wordsets, cores)``:
    ``queries`` are ``(label, geo_search_term)`` from most to least specific;
    ``phrases``/``wordsets`` decide DIRECT vs GENE_ONLY; ``cores`` are
    ``(core_term, stripped_qualifier)`` pairs used to detect sibling diseases.
    """
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

    # Add shortened forms so a precise entry name still reaches real datasets.
    cores: list[tuple[str, str]] = []
    for n in list(names):
        short, stripped = core_term(n)
        if short and short.lower() not in {x.lower() for x in names}:
            names.append(short)
            cores.append((short, stripped))

    queries: list[tuple[str, str]] = []
    seen_terms: set[str] = set()

    def add(label: str, term: str) -> None:
        if term not in seen_terms:
            seen_terms.add(term)
            queries.append((label, term))

    for n in names[:8]:
        esc = n.replace('"', "")
        add(f"name:{n}", f'"{esc}"[All Fields] AND "gse"[Entry Type]')

    # An unquoted AND of the significant words, as a fallback for names whose
    # exact phrasing never appears in GEO ("Systemic AL Amyloidosis").
    for n in names[:3]:
        words = [
            w
            for w in re.findall(r"[A-Za-z0-9\-]+", n)
            if len(w) >= 3 and w.lower() not in STOPWORDS
        ]
        if len(words) >= 2:
            term = (
                " AND ".join(f'"{w}"[All Fields]' for w in words)
                + ' AND "gse"[Entry Type]'
            )
            add(f"words:{' '.join(words)}", term)

    # Causal genes -- the fallback that rescues rare disorders whose name never
    # appears in a GEO title.
    genes = []
    for g in entry.get("genetic") or []:
        sym = (
            ((g.get("gene_term") or {}).get("term") or {}).get("label")
            or g.get("name")
            or ""
        ).strip()
        if sym and re.fullmatch(r"[A-Z0-9orf\-]{2,10}", sym):
            genes.append(sym)
    for sym in list(dict.fromkeys(genes))[:4]:
        add(f"gene:{sym}", f'"{sym}"[Title] AND "gse"[Entry Type]')

    # Terms used to decide DIRECT vs GENE_ONLY: any phrase matching, or a
    # word-set where every significant word is present.
    phrases = [n for n in names if len(n) >= 5]
    wordsets = []
    for n in names[:3]:
        words = [
            w.lower()
            for w in re.findall(r"[A-Za-z0-9\-]+", n)
            if len(w) >= 4 and w.lower() not in STOPWORDS
        ]
        if len(words) >= 2:
            wordsets.append(words)

    return queries, phrases, wordsets, cores


def search_geo(term: str, retmax: int) -> list[str]:
    data = http_json(
        f"{EUTILS}/esearch.fcgi?{eutils_params({'db': 'gds', 'term': term, 'retmode': 'json', 'retmax': str(retmax), 'sort': 'relevance'})}"
    )
    return ((data or {}).get("esearchresult") or {}).get("idlist") or []


def summarize_geo(uids: list[str]) -> list[dict]:
    if not uids:
        return []
    docs: list[dict] = []
    for i in range(0, len(uids), 50):
        chunk = uids[i : i + 50]
        data = http_json(
            f"{EUTILS}/esummary.fcgi?{eutils_params({'db': 'gds', 'id': ','.join(chunk), 'retmode': 'json'})}"
        )
        result = (data or {}).get("result") or {}
        for uid in chunk:
            if uid in result:
                docs.append(result[uid])
        time.sleep(0.12 if os.environ.get("NCBI_API_KEY") else 0.35)
    return docs


def score_candidate(
    cand: Candidate,
    phrases: list[str],
    wordsets: list[list[str]],
    cores: list[tuple[str, str]] | None = None,
) -> None:
    """Rank by how directly the dataset speaks to this disease."""
    score = 0.0
    notes = []
    hay_title = cand.title.lower()
    hay_all = f"{cand.title} {cand.summary}".lower()

    # A literal disease-name hit under a ``non-`` qualifier denotes the
    # complementary disease class (for example, non-clear-cell RCC), not this
    # entry. This must run even when the entry has no removable leading
    # qualifier; the sibling-disease check below only handles names such as
    # chronic versus acute disease.
    for phrase in phrases:
        phrase_pattern = re.escape(phrase.lower()).replace(r"\ ", r"[- ]+")
        if re.search(rf"\bnon[- ]+{phrase_pattern}\b", hay_title):
            cand.relevance = "CONFLICT"
            cand.score = -10.0
            cand.score_notes = [f"title negates disease name: 'non-{phrase.lower()}'"]
            return

    # A candidate that applies a competing qualifier to the disease's core term
    # is about a sibling disease (hereditary vs acquired angioedema), no matter
    # how well the rest of it scores.
    for core, stripped in cores or []:
        if not stripped:
            continue
        # If the entry's own qualified name is also present ("chronic kidney
        # disease" for a Chronic_ entry), the dataset covers this disease as
        # well as its sibling -- comparative studies routinely name both -- so
        # the veto would throw away a genuine hit.
        if f"{stripped} {core}".lower() in hay_all:
            continue
        competing = has_qualifier_conflict(hay_all, stripped, core)
        if competing:
            cand.relevance = "CONFLICT"
            cand.score = -10.0
            cand.score_notes = [
                (
                    f"names '{competing} {core.lower()}' but this entry is "
                    f"'{stripped} {core.lower()}' - likely a sibling disease"
                )
            ]
            return

    def hits(hay: str) -> bool:
        if any(p.lower() in hay for p in phrases):
            return True
        return any(all(w in hay for w in ws) for ws in wordsets)

    if hits(hay_title):
        score += 5.0
        notes.append("disease named in title")
        cand.relevance = "DIRECT"
    elif hits(hay_all):
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

    if cand.data_type in (
        "SINGLE_CELL_RNA_SEQ",
        "SPATIAL_TRANSCRIPTOMICS",
        "MULTI_OMICS",
    ):
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


def discover(
    slug: str, limit: int, per_query: int, use_synonyms: bool
) -> list[Candidate]:
    entry = load_entry(slug)
    queries, phrases, wordsets, cores = build_queries(entry, slug, use_synonyms)

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
            cand.data_type = refine_data_type(
                cand.gds_type,
                f"{cand.title} {cand.summary}",
                map_data_type(cand.gds_type),
                cand.title,
            )
            score_candidate(cand, phrases, wordsets, cores)
            seen[acc] = cand

    ranked = sorted(seen.values(), key=lambda c: c.score, reverse=True)
    return ranked[:limit]


def coverage(fmt: str, only_missing: bool = True) -> int:
    rows = []
    for path in sorted(KB_DIR.glob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text()) or {}
        except Exception:
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
        print(
            f"\n# {missing} entries with no datasets slot, {empty} with an empty one, "
            f"{total - missing - empty} already curated, {total} total",
            file=sys.stderr,
        )
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("disorder", nargs="?", help="disorder slug, e.g. Asthma")
    ap.add_argument(
        "--limit", type=int, default=12, help="max candidates to report (default 12)"
    )
    ap.add_argument(
        "--per-query",
        type=int,
        default=20,
        help="GEO hits per search term (default 20)",
    )
    ap.add_argument(
        "--no-synonyms",
        action="store_true",
        help="skip the MONDO synonym expansion (faster)",
    )
    ap.add_argument("--json", type=Path, help="write candidates to a JSON file")
    ap.add_argument(
        "--coverage", action="store_true", help="report dataset coverage across the KB"
    )
    ap.add_argument(
        "--format",
        choices=("tsv", "slugs"),
        default="tsv",
        help="coverage output format",
    )
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
        print(
            "This is a normal result for a rare disorder. Try `just research-datasets "
            f"openscientist {args.disorder}` for non-NCBI repositories."
        )
        return 0

    tally: dict[str, int] = {}
    for c in cands:
        tally[c.relevance] = tally.get(c.relevance, 0) + 1
    breakdown = ", ".join(f"{n} {k}" for k, n in sorted(tally.items()))
    print(f"{len(cands)} candidate dataset(s) for {args.disorder} ({breakdown}):\n")
    for c in cands:
        print(
            f"  [{c.score:>5}] {c.relevance:<9} {c.accession}  {c.data_type or '?'}  "
            f"n={c.sample_count or '?'}  {c.organism}"
        )
        print(f"          {c.title[:120]}")
        print(f"          via {c.matched_query} | {', '.join(c.score_notes)}")
        if c.pubmed_ids:
            print(f"          PMID:{', PMID:'.join(c.pubmed_ids[:3])}")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
