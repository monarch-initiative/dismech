#!/usr/bin/env python3
"""Find PRIDE (proteomics) and MetaboLights (metabolomics) datasets for an entry.

Both archives already had accession *resolvers* in this project but no
*discovery* route. Worse, the OmicsDI pass actively discarded 1,899 PRIDE and
923 MetaboLights hits on the mistaken grounds that they were "already covered".
They were not. This script closes that gap.

Why these two matter disproportionately: proteomics and metabolomics are the
right assays for inborn errors of metabolism and other rare disease, which is
where GEO performed worst. The only GEO candidate for maple syrup urine disease
was a BCKD-*kinase* study that had to be rejected as the mechanistic opposite of
MSUD; a metabolomics archive is a far better place to look.

Unlike EGA and ArrayExpress, both archives expose a real server-side keyword
search, so this queries per disease rather than bulk-indexing. Matching still
applies the shared narrow rules (:mod:`disease_title_match`): the disease must
be named in the dataset's own title, genes are never searched, and
sibling-disease qualifier conflicts are vetoed.

Usage
-----
    uv run python scripts/discover_ebi_omics.py Phenylketonuria
    uv run python scripts/discover_ebi_omics.py --slugs-file x.txt --out proposals.json
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

from disease_title_match import compile_phrases, entry_phrases, match_title

REPO_ROOT = Path(__file__).resolve().parents[1]
KB_DIR = REPO_ROOT / "kb" / "disorders"
PRIDE = "https://www.ebi.ac.uk/pride/ws/archive/v2/search/projects"
METABOLIGHTS = "https://www.ebi.ac.uk/ebisearch/ws/rest/metabolights"
USER_AGENT = "dismech-dataset-discovery (https://github.com/monarch-initiative/dismech)"

PAGE_SIZE = 50
THROTTLE_S = 0.3


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
    print(f"WARN  request failed ({last}): {url[:90]}", file=sys.stderr)
    return None


def search_pride(term: str) -> list[dict]:
    term = sanitise(term)
    data = http_json(f"{PRIDE}?keyword={urllib.parse.quote(term)}&pageSize={PAGE_SIZE}")
    out = []
    for p in data or []:
        if not isinstance(p, dict):
            continue
        out.append({
            "accession": f"pride:{p.get('accession')}",
            "title": (p.get("title") or "").strip(),
            "description": (p.get("projectDescription") or "").strip(),
            "source": "PRIDE",
            "data_type": "PROTEOMICS",
        })
    return out


def sanitise(term: str) -> str:
    """EBI Search rejects some punctuation outright with HTTP 400.

    A slash in a disease name ("Adult T-Cell Leukemia/Lymphoma",
    "Cleft Lip/Palate", "1p/19q-Codeleted") returned 400 and silently skipped
    15 entries on the first run.
    """
    return " ".join(re.sub(r"[/\\(),:;]", " ", term).split())


def search_metabolights(term: str) -> list[dict]:
    term = sanitise(term)
    url = (f"{METABOLIGHTS}?query={urllib.parse.quote(term)}&format=json&size={PAGE_SIZE}"
           f"&fields=name,description")
    data = http_json(url)
    out = []
    for e in (data or {}).get("entries") or []:
        f = e.get("fields") or {}
        title = (f.get("name") or [""])[0]
        desc = (f.get("description") or [""])[0]
        out.append({
            "accession": f"metabolights:{e.get('id')}",
            "title": (title or "").strip(),
            "description": (desc or "").strip(),
            "source": "MetaboLights",
            "data_type": "METABOLOMICS",
        })
    return out


def to_record(hit: dict, matched: str, today: str) -> dict:
    rec: dict = {"accession": hit["accession"], "title": hit["title"]}
    desc = " ".join((hit.get("description") or "").split())
    if desc:
        rec["description"] = desc[:600]
    rec["data_type"] = hit["data_type"]
    rec["notes"] = (
        f"{hit['source']} dataset, matched because the disease is named in the dataset's own title "
        f"(\"{matched}\"). Proteomics and metabolomics archives are searched because they carry the "
        f"assay types most relevant to metabolic and rare disease, which transcriptomic archives "
        f"cover poorly. Accession resolved against the {hit['source']} API. Retrieved {today}."
    )
    return rec


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("disorder", nargs="?")
    ap.add_argument("--slugs-file", type=Path)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--max-per-entry", type=int, default=3)
    args = ap.parse_args()

    slugs = [args.disorder] if args.disorder else (
        [s.strip() for s in args.slugs_file.read_text().splitlines() if s.strip()] if args.slugs_file else []
    )
    if not slugs:
        ap.error("pass a disorder slug or --slugs-file")

    today = dt.datetime.now(dt.UTC).date().isoformat()
    proposals, n_keep, n_conf = [], 0, 0

    for i, slug in enumerate(slugs, 1):
        path = KB_DIR / f"{slug}.yaml"
        if not path.exists():
            continue
        entry = yaml.safe_load(path.read_text()) or {}
        phrases, cores = entry_phrases(entry, slug)
        if not phrases:
            continue
        disease_name = (entry.get("name") or slug).replace("_", " ")
        patterns = compile_phrases(phrases)

        hits = search_pride(disease_name)
        time.sleep(THROTTLE_S)
        hits += search_metabolights(disease_name)
        time.sleep(THROTTLE_S)

        keep = []
        for h in hits:
            if not h["title"] or not h["accession"].split(":", 1)[1]:
                continue
            matched, conflict = match_title(h["title"], patterns, cores)
            if not matched:
                continue
            if conflict:
                n_conf += 1
                continue
            keep.append((h, matched))
        keep = keep[: args.max_per_entry]
        n_keep += len(keep)

        if keep and args.out is not None:
            proposals.append({
                "slug": slug,
                "disease_name": disease_name,
                "n_candidates": len(keep),
                "records": [
                    {"approved": True, "matched_phrase": m, "source": h["source"],
                     "record": to_record(h, m, today)}
                    for h, m in keep
                ],
            })
        elif keep:
            for h, m in keep:
                print(f"  [OK] {slug}: {h['accession']}  ({h['source']})  {h['title'][:66]}")
        if args.slugs_file and i % 100 == 0:
            print(f"  ...{i}/{len(slugs)}  kept={n_keep}", file=sys.stderr, flush=True)

    if args.out is not None:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(proposals, indent=2) + "\n")
        print(f"\nWrote {args.out}: {sum(len(p['records']) for p in proposals)} records "
              f"across {len(proposals)} entries")
    print(f"\nkept: {n_keep}   vetoed: {n_conf}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
