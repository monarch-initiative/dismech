#!/usr/bin/env python3
"""Find dbGaP and ImmPort studies that are *specifically about* a dismech disease.

Why these two repositories
--------------------------
They are the only two in the NIH Dataset Catalog that hold primary biomedical
data, and dismech has almost no coverage of either (3 dbGaP accessions, 0
ImmPort). Neither is reachable by any other dismech discovery script, and
neither overlaps GEO/ArrayExpress/EGA/OmicsDI -- so unlike ArrayExpress
(73.6% GEO re-imports) or OmicsDI (89% duplicates), nothing found here can
duplicate an accession already in the KB under another prefix.

Why the native APIs rather than the catalog
-------------------------------------------
The catalog's selling point is coded MeSH disease indexing. But that coding is
*derived from dbGaP's own metadata* -- dbGaP publishes the same MeSH codes in a
searchable ``condition`` field, and ImmPort publishes a richer disease field of
its own. Going native is strictly better on every axis measured:

* **Same coverage** (dbGaP FHIR 3,582 studies vs catalog 3,604; ImmPort 1,502
  vs 1,500), so the catalog adds no records.
* **Better precision.** The catalog augments each record with subjects inferred
  from title, description, keywords, and linked PubMed records, so it returns
  strictly more -- and the surplus is exactly the incidental-mega-cohort noise.
  For bronchiectasis, dbGaP returns the 2 real studies; the catalog adds Yale
  Center for Mendelian Genomics and NIAID Centralized Sequencing.
* **More fields.** ImmPort supplies PMID, species, and enrollment, so records
  built here reach parity with the GEO path. The catalog supplies none of them
  for any repository.
* **Text search.** ``condition:text=`` searches MeSH *entry terms*; the
  catalog blocks ``REGEX``/``CONTAINS`` at its endpoint entirely.

See ``docs/reports/nlm-dataset-catalog-evaluation-2026-08-07.md``.

The relevance tiers
-------------------
Every hit is coded to the disease by the repository, so "is it real?" is not the
question -- "is it *about* this disease?" is. Hits are tiered:

``TITLE_MATCH``   the disease is named in the study's own title. Auto-approved.
``SUBJECT_ONLY``  coded to the disease, but the title does not name it. This is
                  the incidental-mega-cohort class: eMERGE and the Bogalusa
                  Heart Study are legitimately MeSH-indexed for asthma because
                  they measure it, among hundreds of other things. Proposed
                  but **not** auto-approved -- a curator decides.
``CONFLICT``      the title applies a competing qualifier to the disease's core
                  term (*hereditary* vs *acquired*), i.e. a sibling disease.
                  Vetoed.

Rare disease
------------
Entries whose MONDO maps only to a MeSH Supplementary Concept Record
(``MESH:C######``) get no coded query -- dbGaP indexes with descriptors only.
The text pass still runs, but expect nothing: spot-checking eight SCR-only
diseases returned zero, because dbGaP genuinely holds no studies for them.

Usage
-----
    uv run python scripts/discover_dbgap_immport.py Sjogrens_Syndrome
    uv run python scripts/discover_dbgap_immport.py --slugs-file batch.txt --out proposals.json
    uv run python scripts/discover_dbgap_immport.py Asthma --include-subject-only
"""

from __future__ import annotations

import argparse
import codecs
import datetime as dt
import html
import json
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from disease_title_match import compile_phrases, entry_phrases, match_title

REPO_ROOT = Path(__file__).resolve().parents[1]
KB_DIR = REPO_ROOT / "kb" / "disorders"

DBGAP_FHIR = "https://dbgap-api.ncbi.nlm.nih.gov/fhir/x1/ResearchStudy"
IMMPORT_SEARCH = "https://www.immport.org/shared/data/query/api/search/study"
USER_AGENT = "dismech-dataset-discovery (https://github.com/monarch-initiative/dismech)"

PAGE = 50
REQUEST_GAP = 0.34  # be a polite guest on both public endpoints

# ImmPort `assay_method` -> DatasetTypeEnum, only where the mapping is
# unambiguous. Anything vague ("Other", "ELISA") is left unset rather than
# guessed -- a wrong data_type is worse than a missing one.
ASSAY_TO_ENUM = {
    "rna sequencing": "BULK_RNA_SEQ",
    "transcription profiling": "BULK_RNA_SEQ",
    "single-cell rna sequencing": "SINGLE_CELL_RNA_SEQ",
    "dna microarray": "MICROARRAY",
    "array": "MICROARRAY",
    "mass spectrometry": "PROTEOMICS",
    "atac-seq": "ATAC_SEQ",
    "chip-seq": "CHIP_SEQ",
    "methylation profiling": "METHYLATION",
    "whole genome sequencing": "WGS",
    "exome sequencing": "WES",
}

# There is deliberately no dbGaP study-design -> DatasetTypeEnum mapping.
# `category` records the *design* (Case-Control, Cohort, Cross-Sectional), not
# the assay, so inferring GWAS from "Case-Control" mislabelled an RNAseq study
# of salivary glands. A missing data_type is recoverable; a wrong one is not.


# dbGaP's FHIR service declares ``charset=iso-8859-1`` but serves *mixed*
# content: most text is valid UTF-8 while the odd eponym carries a raw latin-1
# byte (0xf6 for the "o" of Sjogren). Decoding the whole body as either charset
# alone is wrong, and ``errors="replace"`` silently plants U+FFFD in text that
# ends up in a curated ``description:``. Decode as UTF-8 and fall back to
# latin-1 for exactly the bytes that are not valid UTF-8.
def _latin1_fallback(err: UnicodeDecodeError):
    return err.object[err.start : err.end].decode("latin-1"), err.end


codecs.register_error("dismech_latin1_fallback", _latin1_fallback)


def decode_body(raw: bytes) -> str:
    return raw.decode("utf-8", errors="dismech_latin1_fallback")


def http_json(url: str, retries: int = 3):
    last: Exception | None = None
    for attempt in range(retries):
        time.sleep(REQUEST_GAP)
        req = urllib.request.Request(
            url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"}
        )
        try:
            with urllib.request.urlopen(req, timeout=90) as resp:
                return json.loads(decode_body(resp.read()))
        except Exception as exc:  # noqa: BLE001 - any failure is just a miss here
            last = exc
            time.sleep(1.5 * (attempt + 1))
    print(f"WARN  request failed: {url} ({last})", file=sys.stderr)
    return None


# --------------------------------------------------------------------------- #
# MONDO -> MeSH
# --------------------------------------------------------------------------- #


def mesh_descriptors(mondo_id: str) -> tuple[list[str], list[str]]:
    """Return (descriptor codes, SCR codes) cross-referenced from a MONDO term.

    Descriptors (``D######``) are what dbGaP codes with. SCRs (``C######``) are
    returned separately only so the caller can say *why* an entry got no coded
    query, rather than silently reporting zero.
    """
    if not mondo_id:
        return [], []
    try:
        out = subprocess.run(
            ["uv", "run", "runoak", "-i", "sqlite:obo:mondo", "info", mondo_id, "-O", "obo"],
            capture_output=True,
            text=True,
            timeout=300,
            cwd=REPO_ROOT,
            check=False,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError):
        print(f"WARN  MONDO lookup failed for {mondo_id}", file=sys.stderr)
        return [], []

    descriptors, scrs = [], []
    for line in out.stdout.splitlines():
        m = re.match(r"\s*xref:\s*MESH:([CD]\d+)", line)
        if not m:
            continue
        (descriptors if m.group(1).startswith("D") else scrs).append(m.group(1))
    return descriptors, scrs


# --------------------------------------------------------------------------- #
# Repository queries
# --------------------------------------------------------------------------- #


def _fhir_studies(query: str) -> list[dict]:
    data = http_json(f"{DBGAP_FHIR}?{query}&_count={PAGE}&_format=json")
    if not data or data.get("resourceType") == "OperationOutcome":
        return []
    return [e.get("resource") or {} for e in (data.get("entry") or [])]


def query_dbgap(mesh_codes: list[str], phrases: list[str]) -> dict[str, dict]:
    """Coded pass then text pass, merged by accession (coded wins on overlap)."""
    found: dict[str, dict] = {}

    def absorb(studies: list[dict], route: str) -> None:
        for study in studies:
            acc = next(
                (
                    str(i.get("value"))
                    for i in study.get("identifier") or []
                    if str(i.get("value", "")).lower().startswith("phs")
                ),
                "",
            )
            if not acc or acc in found:
                continue
            found[acc] = {
                "accession": f"dbgap:{acc}",
                "title": html.unescape(study.get("title") or ""),
                "description": html.unescape(study.get("description") or ""),
                "conditions": [
                    html.unescape(c["text"]) for c in study.get("condition") or [] if c.get("text")
                ][:8],
                "design": next(
                    (c.get("text", "") for c in study.get("category") or []), ""
                ),
                "pubmed_ids": [],
                "sample_count": None,
                "organism": "Homo sapiens",
                "route": route,
                "repository": "dbGaP",
            }

    for code in mesh_codes:
        absorb(_fhir_studies(f"condition={urllib.parse.quote(code)}"), f"MeSH {code}")
    for phrase in phrases:
        absorb(
            _fhir_studies(f"condition:text={urllib.parse.quote(phrase)}"),
            f'condition:text="{phrase}"',
        )
    return found


def query_immport(phrases: list[str]) -> dict[str, dict]:
    """ImmPort's disease field, not its free-text index.

    ``conditionOrDisease=`` restricts the match to the study's disease field;
    the free ``term=`` matches anywhere in the record and roughly doubles the
    hit count with material that is not about the disease (asthma: 56 -> 29).
    """
    found: dict[str, dict] = {}
    for phrase in phrases:
        data = http_json(f"{IMMPORT_SEARCH}?conditionOrDisease={urllib.parse.quote(phrase)}")
        for hit in ((data or {}).get("hits") or {}).get("hits") or []:
            src = hit.get("_source") or {}
            acc = str(src.get("study_accession") or "")
            if not acc or acc in found:
                continue
            species = src.get("species") or []
            found[acc] = {
                "accession": f"immport:{acc}",
                "title": (src.get("brief_title") or "").strip(),
                "description": (src.get("brief_description") or "").strip(),
                "conditions": src.get("condition_or_disease") or [],
                "design": "; ".join(src.get("assay_method") or [])[:120],
                "pubmed_ids": [str(p) for p in (src.get("pubmed_id") or []) if p],
                "sample_count": src.get("actual_enrollment"),
                "organism": species[0] if species else "",
                "route": f'conditionOrDisease="{phrase}"',
                "repository": "ImmPort",
                "assay_methods": src.get("assay_method") or [],
            }
    return found


# --------------------------------------------------------------------------- #
# Relevance tiering and record construction
# --------------------------------------------------------------------------- #

ORGANISM_TERMS = {
    "homo sapiens": ("human", "NCBITaxon:9606", "Homo sapiens"),
    "mus musculus": ("mouse", "NCBITaxon:10090", "Mus musculus"),
    "macaca mulatta": ("rhesus macaque", "NCBITaxon:9544", "Macaca mulatta"),
}


def tier(hit: dict, patterns, cores) -> tuple[str, str, str]:
    """Return (tier, matched_phrase, conflict_reason)."""
    matched, conflict = match_title(hit["title"], patterns, cores)
    if conflict:
        return "CONFLICT", matched, conflict
    if matched:
        return "TITLE_MATCH", matched, ""
    return "SUBJECT_ONLY", "", ""


def infer_data_type(hit: dict) -> str:
    for method in hit.get("assay_methods") or []:
        enum = ASSAY_TO_ENUM.get(str(method).strip().lower())
        if enum:
            return enum
    return ""


def to_record(hit: dict, tier_name: str, matched: str, retrieved: str) -> dict:
    rec: dict = {"accession": hit["accession"], "title": hit["title"]}

    desc = re.sub(r"\s+", " ", hit.get("description") or "").strip()
    if desc:
        rec["description"] = (
            desc[:700].rsplit(". ", 1)[0] + "." if len(desc) > 700 else desc
        )

    org = ORGANISM_TERMS.get(str(hit.get("organism") or "").strip().lower())
    if org:
        rec["organism"] = {
            "preferred_term": org[0],
            "term": {"id": org[1], "label": org[2]},
        }

    data_type = infer_data_type(hit)
    if data_type:
        rec["data_type"] = data_type
    if hit.get("sample_count"):
        rec["sample_count"] = int(hit["sample_count"])
    if hit.get("pubmed_ids"):
        rec["publication"] = f"PMID:{hit['pubmed_ids'][0]}"

    if tier_name == "TITLE_MATCH":
        why = f'the disease is named in the study\'s own title ("{matched}")'
    else:
        coded = ", ".join(hit.get("conditions") or []) or "the disease"
        why = (
            f"the repository codes this study to {coded}, but the disease is NOT named "
            f"in the study title -- verify it is not a broad cohort that merely "
            f"measures the disease among many others"
        )
    access = (
        " Controlled access -- data require dbGaP authorization."
        if hit["repository"] == "dbGaP"
        else ""
    )
    rec["notes"] = (
        f"{hit['repository']} study, found via {hit['route']}; matched because {why}."
        f"{access} Repository metadata retrieved {retrieved}."
    )
    return rec


# --------------------------------------------------------------------------- #


def discover(slug: str) -> tuple[list[dict], str]:
    """Return (tiered hits, note explaining an empty result)."""
    path = KB_DIR / f"{slug}.yaml"
    if not path.exists():
        return [], f"{slug}: no such entry"
    entry = yaml.safe_load(path.read_text()) or {}

    phrases, cores = entry_phrases(entry, slug)
    if not phrases:
        return [], f"{slug}: no usable disease phrase"
    patterns = compile_phrases(phrases)

    mondo = (((entry.get("disease_term") or {}).get("term") or {}).get("id")) or ""
    descriptors, scrs = mesh_descriptors(mondo)

    hits = {**query_dbgap(descriptors, phrases), **query_immport(phrases)}

    tiered = []
    for hit in hits.values():
        tier_name, matched, conflict = tier(hit, patterns, cores)
        tiered.append({**hit, "tier": tier_name, "matched_phrase": matched, "conflict": conflict})
    order = {"TITLE_MATCH": 0, "SUBJECT_ONLY": 1, "CONFLICT": 2}
    tiered.sort(key=lambda h: (order[h["tier"]], h["accession"]))

    note = ""
    if not tiered and not descriptors:
        note = (
            f"{slug}: MONDO {mondo or '(none)'} has no MeSH descriptor"
            + (f" (only SCR {', '.join(scrs)})" if scrs else "")
            + " -- dbGaP indexes descriptors only, so no coded query was possible"
        )
    return tiered, note


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("disorder", nargs="?")
    ap.add_argument("--slugs-file", type=Path)
    ap.add_argument("--out", type=Path, help="write a triage-ready proposals JSON")
    ap.add_argument("--max-per-entry", type=int, default=3)
    ap.add_argument(
        "--include-subject-only",
        action="store_true",
        help="also propose hits coded to the disease whose title does not name it "
        "(never auto-approved; they are written with approved=false)",
    )
    args = ap.parse_args()

    slugs = (
        [args.disorder]
        if args.disorder
        else (
            [s.strip() for s in args.slugs_file.read_text().splitlines() if s.strip()]
            if args.slugs_file
            else []
        )
    )
    if not slugs:
        ap.error("pass a disorder slug or --slugs-file")

    retrieved = dt.datetime.now(dt.UTC).date().isoformat()
    proposals: list[dict] = []
    counts = {"TITLE_MATCH": 0, "SUBJECT_ONLY": 0, "CONFLICT": 0}

    for i, slug in enumerate(slugs, 1):
        hits, note = discover(slug)
        for hit in hits:
            counts[hit["tier"]] += 1
        if note:
            print(f"  [SKIP] {note}", file=sys.stderr)

        approved = [h for h in hits if h["tier"] == "TITLE_MATCH"][: args.max_per_entry]
        proposed = list(approved)
        if args.include_subject_only:
            proposed += [h for h in hits if h["tier"] == "SUBJECT_ONLY"][: args.max_per_entry]

        if not args.out:
            for hit in hits[:8]:
                print(f"  [{hit['tier']:12s}] {slug}: {hit['accession']}  {hit['title'][:80]}")
                if hit["conflict"]:
                    print(f"       -> {hit['conflict']}")
        elif proposed:
            entry = yaml.safe_load((KB_DIR / f"{slug}.yaml").read_text()) or {}
            proposals.append(
                {
                    "slug": slug,
                    "disease_name": (entry.get("name") or slug).replace("_", " "),
                    "n_candidates": len(hits),
                    "records": [
                        {
                            "approved": h["tier"] == "TITLE_MATCH",
                            "tier": h["tier"],
                            "matched_phrase": h["matched_phrase"],
                            "record": to_record(h, h["tier"], h["matched_phrase"], retrieved),
                        }
                        for h in proposed
                    ],
                }
            )
        if args.slugs_file and i % 25 == 0:
            print(f"  ...{i}/{len(slugs)}", file=sys.stderr, flush=True)

    if args.out is not None:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(proposals, indent=2) + "\n")
        total = sum(len(p["records"]) for p in proposals)
        print(f"\nWrote {args.out}: {total} records across {len(proposals)} entries")

    print(
        f"\nTITLE_MATCH: {counts['TITLE_MATCH']}   "
        f"SUBJECT_ONLY (needs triage): {counts['SUBJECT_ONLY']}   "
        f"CONFLICT (vetoed): {counts['CONFLICT']}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
