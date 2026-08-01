#!/usr/bin/env python3
"""Find EGA studies that are *specifically about* a dismech disease.

The European Genome-phenome Archive holds the controlled-access human cohorts
that GEO structurally cannot see -- which is exactly the tail GEO-title search
failed on. Its metadata API has no server-side text search (``?query=`` is
silently ignored and returns an unfiltered first page), so this script pages
the whole study list into a local index and does the matching itself. That is
an advantage rather than a workaround: it puts the strictness of the match
under our control.

Deliberately narrow
-------------------
The single rule is that **the disease must be named in the study's own title**.

Not the description, not the abstract. A study whose title names the disease is
*about* that disease; a study that merely mentions it in an abstract is usually
about something else and is the source of most wrong-disease matches. This
trades recall for precision on purpose -- the GEO batches showed that a
description-level match is where sibling diseases, model systems, and
"we also profiled X" studies get in.

Two further guards, carried over from the GEO work:

* **Qualifier conflict.** A title applying a competing qualifier to the disease's
  core term (*hereditary* vs *acquired* angioedema, *juvenile* vs *adult*) is a
  sibling disease and is vetoed.
* **No gene fallback.** Causal genes are never searched. In GEO that produced
  Alzheimer data for neuroferritinopathy; there is no reason to expect better here.

Usage
-----
    uv run python scripts/discover_ega.py --refresh          # build the local index
    uv run python scripts/discover_ega.py Cystic_Fibrosis    # candidates for one entry
    uv run python scripts/discover_ega.py --slugs-file x.txt --out proposals.json
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from discover_datasets import (
    STOPWORDS,
    core_term,
    has_qualifier_conflict,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
KB_DIR = REPO_ROOT / "kb" / "disorders"
DATA_DIR = REPO_ROOT / "data" / "ega"
INDEX_PATH = DATA_DIR / "studies.json"
API = "https://metadata.ega-archive.org/studies"
USER_AGENT = "dismech-dataset-discovery (https://github.com/monarch-initiative/dismech)"

PAGE = 500
MAX_PAGES = 60  # ~30k studies; the archive is currently well under this

# EGA `study_type` -> DatasetTypeEnum, only where the mapping is unambiguous.
# Anything vague ("Cancer Genomics", "Other") is left unset rather than guessed.
STUDY_TYPE_TO_ENUM = {
    "whole genome sequencing": "WGS",
    "exome sequencing": "WES",
    "transcriptome analysis": "BULK_RNA_SEQ",
    "rna sequencing": "BULK_RNA_SEQ",
    "epigenetics": "METHYLATION",
    "metagenomics": "WGS",
}

# A title match on a very short or generic phrase is noise, not evidence.
MIN_PHRASE_LEN = 6

# Phrases too generic to be evidence of anything, even at full length. These
# turn up when an entry's `disease_term` is bound to a near-root MONDO class
# (Dorsalgia is currently bound to a term labelled simply "disease"), which
# would otherwise match a large fraction of the archive.
GENERIC_PHRASES = {
    "disease", "diseases", "syndrome", "syndromes", "disorder", "disorders",
    "deficiency", "cancer", "carcinoma", "tumor", "tumour", "infection",
    "inflammation", "neoplasm", "abnormality", "malformation", "failure",
}

# Head-nouns that name a *class* of disease rather than a disease. Safe inside a
# multi-word phrase ("AL Amyloidosis"), unsafe alone: bare "Sclerosis" matches
# multiple sclerosis, tuberous sclerosis and ALS alike. Only ever applied to a
# core term derived by stripping a qualifier, never to an entry's own name.
GENERIC_HEAD_NOUNS = {
    "sclerosis", "fibrosis", "anemia", "anaemia", "dystrophy", "atrophy",
    "ataxia", "neuropathy", "myopathy", "dysplasia", "palsy", "leukemia",
    "leukaemia", "lymphoma", "sarcoma", "hepatitis", "nephritis", "arthritis",
    "dermatitis", "colitis", "encephalopathy", "encephalitis", "myelitis",
    "retinopathy", "cardiomyopathy", "thalassemia", "porphyria", "amyloidosis",
    "hypertension", "hypotension", "diabetes", "epilepsy", "psoriasis",
    "vasculitis", "thrombocytopenia", "neutropenia", "immunodeficiency",
}


def http_json(url: str, retries: int = 3):
    last: Exception | None = None
    for attempt in range(retries):
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.loads(resp.read().decode("utf-8", "replace"))
        except Exception as exc:
            last = exc
            time.sleep(1.5 * (attempt + 1))
    print(f"WARN  EGA request failed: {url} ({last})", file=sys.stderr)
    return None


def refresh_index() -> dict:
    """Page the entire EGA study list into a local index."""
    studies: dict[str, dict] = {}
    for page in range(MAX_PAGES):
        offset = page * PAGE
        batch = http_json(f"{API}?limit={PAGE}&offset={offset}")
        if not batch:
            break
        for s in batch:
            acc = s.get("accession_id") or ""
            if not acc.startswith("EGAS"):
                continue
            studies[acc] = {
                "title": (s.get("title") or "").strip(),
                "description": (s.get("description") or "").strip()[:1500],
                "study_type": (s.get("study_type") or "").strip(),
                "pubmed_ids": s.get("pubmed_ids") or [],
                "released": s.get("released_date") or "",
            }
        print(f"  indexed {len(studies)} studies (offset {offset})", file=sys.stderr, flush=True)
        if len(batch) < PAGE:
            break
        time.sleep(0.2)

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(json.dumps(studies, indent=1, sort_keys=True) + "\n")
    (DATA_DIR / "RETRIEVED").write_text(dt.datetime.now(dt.UTC).date().isoformat() + "\n")
    print(f"Wrote {INDEX_PATH}: {len(studies)} studies")
    return studies


def load_index() -> dict:
    if not INDEX_PATH.exists():
        sys.exit(f"{INDEX_PATH} not found; run with --refresh first.")
    return json.loads(INDEX_PATH.read_text())


def _significant(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9]+", text.lower()) if len(w) > 2 and w not in STOPWORDS}


def _label_is_broader(name: str, label: str) -> bool:
    """True when the entry's own name carries qualifiers its MONDO label lacks.

    Several entries are bound to a *parent* concept: `BRCA_Mutant_Prostate_Cancer`
    to "prostate cancer", `NRAS_Mutant_Melanoma` to "cutaneous melanoma",
    `Arsenic_Related_Cancers` to "squamous cell carcinoma",
    `Hospital-Acquired_Acute_Kidney_Injury` to "kidney injury". Searching the
    bare label then retrieves the general disease -- exactly what this script is
    supposed to avoid -- so the label is dropped as a match phrase and only the
    entry's full name is used.
    """
    extra = _significant(name) - _significant(label)
    return bool(extra)


def entry_phrases(entry: dict, slug: str) -> tuple[list[str], list[tuple[str, str]]]:
    """Disease phrases to look for in a title, plus (core, qualifier) pairs."""
    names: list[str] = []
    name = (entry.get("name") or slug).replace("_", " ").strip()
    if name:
        names.append(name)
    label = (((entry.get("disease_term") or {}).get("term") or {}).get("label") or "").strip()
    if label and label.lower() != name.lower() and not _label_is_broader(name, label):
        names.append(label)

    cores: list[tuple[str, str]] = []
    for n in list(names):
        short, stripped = core_term(n)
        if not short or short.lower() in {x.lower() for x in names}:
            continue
        # A single-word core that is a generic pathology head-noun heads dozens
        # of distinct diseases: stripping "Systemic Sclerosis" to "Sclerosis"
        # matched Multiple Sclerosis. Keep the qualified form only.
        if " " not in short.strip() and short.strip().lower() in GENERIC_HEAD_NOUNS:
            continue
        names.append(short)
        cores.append((short, stripped))

    phrases = [
        n for n in names
        if len(n) >= MIN_PHRASE_LEN and n.strip().lower() not in GENERIC_PHRASES
    ]
    return phrases, cores


def match_entry(slug: str, index: dict) -> list[dict]:
    path = KB_DIR / f"{slug}.yaml"
    if not path.exists():
        return []
    entry = yaml.safe_load(path.read_text()) or {}
    phrases, cores = entry_phrases(entry, slug)
    if not phrases:
        return []

    # Word-boundary matching, not substring: "H Syndrome" must not match
    # "Denys-Drash Syndrome" or "MRKH syndrome".
    patterns = [(p, re.compile(rf"\b{re.escape(p.lower())}\b")) for p in phrases]

    hits = []
    for acc, s in index.items():
        title_l = s["title"].lower()
        matched = next((p for p, rx in patterns if rx.search(title_l)), None)
        if not matched:
            continue

        # Sibling-disease veto: a competing qualifier on the core term.
        conflict = ""
        for core, stripped in cores:
            if not stripped:
                continue
            if f"{stripped} {core}".lower() in title_l:
                continue
            competing = has_qualifier_conflict(title_l, stripped, core)
            if competing:
                conflict = f"title says '{competing} {core.lower()}', entry is '{stripped} {core.lower()}'"
                break

        hits.append(
            {
                "accession": f"ega:{acc}",
                "title": s["title"],
                "description": s["description"],
                "study_type": s["study_type"],
                "pubmed_ids": [str(p) for p in s["pubmed_ids"] if p],
                "matched_phrase": matched,
                "relevance": "CONFLICT" if conflict else "TITLE_MATCH",
                "conflict": conflict,
            }
        )
    hits.sort(key=lambda h: (h["relevance"] != "TITLE_MATCH", -len(h["matched_phrase"])))
    return hits


def to_record(h: dict, disease_name: str, retrieved: str) -> dict:
    rec: dict = {"accession": h["accession"], "title": h["title"]}
    desc = re.sub(r"\s+", " ", h["description"]).strip()
    if desc:
        rec["description"] = desc[:700].rsplit(". ", 1)[0] + "." if len(desc) > 700 else desc
    rec["organism"] = {"preferred_term": "human", "term": {"id": "NCBITaxon:9606", "label": "Homo sapiens"}}
    dt_enum = STUDY_TYPE_TO_ENUM.get(h["study_type"].lower())
    if dt_enum:
        rec["data_type"] = dt_enum
    if h["pubmed_ids"]:
        rec["publication"] = f"PMID:{h['pubmed_ids'][0]}"
    rec["notes"] = (
        f"European Genome-phenome Archive study, matched because the disease is named in the "
        f"study's own title (\"{h['matched_phrase']}\"); description-level mentions were not "
        f"accepted. EGA study_type: {h['study_type'] or 'unspecified'}. Controlled access -- "
        f"data require a Data Access Agreement. EGA metadata retrieved {retrieved}."
    )
    return rec


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("disorder", nargs="?")
    ap.add_argument("--slugs-file", type=Path)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--max-per-entry", type=int, default=3)
    args = ap.parse_args()

    if args.refresh:
        refresh_index()
        if not (args.disorder or args.slugs_file):
            return 0

    index = load_index()
    retrieved = (DATA_DIR / "RETRIEVED").read_text().strip() if (DATA_DIR / "RETRIEVED").exists() else "unknown"

    slugs = [args.disorder] if args.disorder else (
        [s.strip() for s in args.slugs_file.read_text().splitlines() if s.strip()] if args.slugs_file else []
    )
    if not slugs:
        ap.error("pass a disorder slug or --slugs-file")

    proposals, n_hit, n_conflict = [], 0, 0
    for i, slug in enumerate(slugs, 1):
        hits = match_entry(slug, index)
        good = [h for h in hits if h["relevance"] == "TITLE_MATCH"][: args.max_per_entry]
        n_conflict += sum(1 for h in hits if h["relevance"] == "CONFLICT")
        n_hit += len(good)
        if not hits:
            continue
        entry = yaml.safe_load((KB_DIR / f"{slug}.yaml").read_text()) or {}
        disease_name = (entry.get("name") or slug).replace("_", " ")

        if not args.out:
            for h in hits[:6]:
                flag = "OK  " if h["relevance"] == "TITLE_MATCH" else "CONF"
                print(f"  [{flag}] {slug}: {h['accession']}  {h['title'][:95]}")
                if h["conflict"]:
                    print(f"          -> {h['conflict']}")
        elif good:
            proposals.append({
                "slug": slug,
                "disease_name": disease_name,
                "n_candidates": len(hits),
                "records": [
                    {"approved": True, "matched_phrase": h["matched_phrase"],
                     "record": to_record(h, disease_name, retrieved)}
                    for h in good
                ],
            })
        if args.slugs_file and i % 200 == 0:
            print(f"  ...{i}/{len(slugs)}", file=sys.stderr, flush=True)

    if args.out is not None:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(proposals, indent=2) + "\n")
        total = sum(len(p["records"]) for p in proposals)
        print(f"\nWrote {args.out}: {total} records across {len(proposals)} entries")
    print(f"\nTITLE_MATCH: {n_hit}   CONFLICT (vetoed): {n_conflict}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
