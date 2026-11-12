"""Count the PubMed literature on a disease up to its verified cutoff date.

This computes the INSUFFICIENT_PRE_CUTOFF_LITERATURE exclusion of
eligibility_rules.md (version 3). A row is excluded when the disease has fewer
PubMed records on or before its cutoff date than the packet minimum, because
a time-sliced curation packet built from that literature would be too thin.

Input: dating.tsv, one row per disease/test pair to check, with columns
  disease      the frame's disease_name
  test         the frame's row_name
  row_type     optional; needed only when disease + test names two frame rows
  literature_alias  optional, ';'-separated extra terms OR'd into the query: a
               plain name is searched as "<name>"[tiab]; an item containing "["
               is a PubMed fragment used verbatim (in parentheses). It exists
               because a MONDO label can be a catalogue or subtype form that no
               abstract uses. alias_source, if present, is passed through.
  mondo_id     optional. When present (dating.tsv from build_dating.py carries
               it), it is used directly and no frame.tsv match is attempted:
               dating.tsv names each case's test once, which is not a frame
               row_name, and frame_idx is then NA
  cutoff_date  YYYY-MM-DD, the last date the packet may include
  quote_ok     the dating check's verdict; only TRUE rows count as verified
  dating_status  optional (build_dating.py writes it); when present, only
               ACCEPTED rows count as verified, so an ACCEPTED_FLAGGED cutoff
               is not used until its flag is resolved
Any other columns are passed through.

For each verified row, the disease is taken from its MONDO ID in frame.tsv and
the query is the OR of:
  - the disease's MeSH heading, from MONDO's MESH: cross-reference, as
    "<heading>"[MeSH Terms] (or [Supplementary Concept] for a C-number);
  - the MONDO label, as "<label>"[tiab];
  - each MONDO exact synonym, as "<synonym>"[tiab];
ANDed with ``hasabstract`` and limited to publication dates up to and including
cutoff_date. MONDO is read with ``runoak`` against the local MONDO build,
opened by file path (``sqlite:<path to mondo.db>``). That build is required:
the configured ols:mondo adapter does not serve synonyms or MeSH mappings, and
the script stops rather than download it. Fetch it with
``just fetch-ontology-dbs mondo``. The path form matters: ``sqlite:obo:mondo``
lets oaklib replace an existing build it considers stale, which silently changes
the MONDO release under the counts; a path adapter never downloads. The build's
date is recorded in ``mondo_build`` so the release behind each count is known.

Added columns:
  frame_idx        position among flagged frame rows (what build_eligibility.py joins on)
  mondo_id         from frame.tsv
  mondo_build      modification date of the mondo.db that was read
  mesh_id, mesh_heading
  n_synonyms       MONDO exact synonyms included
  lit_query        the PubMed query sent
  lit_count        PubMed's hit count
  packet_minimum   from RUN_CONFIG.yaml
  lit_ruling       INSUFFICIENT_PRE_CUTOFF_LITERATURE if lit_count < packet_minimum,
                   PASS otherwise; UNVERIFIED_CUTOFF when quote_ok is not TRUE or
                   cutoff_date is unusable; NA when a lookup or search failed

The packet minimum is read from ../diagnostic_retrodiction/RUN_CONFIG.yaml
(``packet_minimum``). NCBI_API_KEY is required; it is sent only as a request
parameter (by POST, so long synonym queries fit) and is never printed, cached,
or put in an error message. Responses are cached under tmp/pretest_cache/.

Usage:
    uv run python experiments/diagnostic_retrodiction/check_pretest_era.py \
        dating.tsv --out experiments/diagnostic_retrodiction/eligibility_work/pre_cutoff_literature.tsv
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
MONDO_ADAPTER = "sqlite:obo:mondo"  # named only to locate the build; never opened by name
REQUIRED = ("disease", "test", "cutoff_date", "quote_ok")
ADDED = ("frame_idx", "mondo_id", "mondo_build", "mesh_id", "mesh_heading", "n_synonyms", "lit_query",
         "lit_count", "packet_minimum", "lit_ruling")


def log(msg: str) -> None:
    print(msg, file=sys.stderr)


class EUtils:
    def __init__(self, api_key: str, cache: Path):
        self.api_key, self.cache = api_key, cache
        cache.mkdir(parents=True, exist_ok=True)

    def call(self, endpoint: str, params: dict) -> dict | None:
        key = hashlib.sha256(json.dumps([endpoint, params], sort_keys=True).encode()).hexdigest()[:24]
        path = self.cache / f"{endpoint.split('.')[0]}_{key}.json"
        if path.exists():
            return json.loads(path.read_text())
        body = urllib.parse.urlencode({**params, "retmode": "json", "tool": "dismech-retrodiction",
                                       "api_key": self.api_key}).encode()
        for attempt in range(4):
            try:
                with urllib.request.urlopen(urllib.request.Request(f"{EUTILS}/{endpoint}", data=body),
                                            timeout=60) as r:
                    data = json.load(r)
                time.sleep(0.11)
                path.write_text(json.dumps(data))
                return data
            except (urllib.error.URLError, TimeoutError, ValueError) as e:
                if attempt == 3:
                    # Type only: exception text can carry the request, which holds the key.
                    log(f"{endpoint} failed ({type(e).__name__})")
                    return None
                time.sleep(2 * (attempt + 1))
        return None

    def mesh_heading(self, mesh_id: str) -> str | None:
        """Heading for a MeSH descriptor (D...) or supplementary concept (C...)."""
        m = re.fullmatch(r"([DC])(\d+)", mesh_id)
        if not m:
            return None
        uid = ("68" if m.group(1) == "D" else "67") + m.group(2)
        data = self.call("esummary.fcgi", {"db": "mesh", "id": uid})
        try:
            return data["result"][uid]["ds_meshterms"][0]
        except (TypeError, KeyError, IndexError):
            return None

    def count(self, term: str, maxdate: str) -> int | None:
        data = self.call("esearch.fcgi", {"db": "pubmed", "term": term, "datetype": "pdat",
                                          "mindate": "1800/01/01", "maxdate": maxdate,
                                          "rettype": "count"})
        try:
            return int(data["esearchresult"]["count"])
        except (TypeError, KeyError, ValueError):
            return None


MONDO_PATH_ADAPTER = ""  # set in main(): sqlite:<absolute path to the local mondo.db>


def runoak(*args: str) -> str | None:
    proc = subprocess.run(["runoak", "-i", MONDO_PATH_ADAPTER, *args], cwd=REPO,
                          capture_output=True, text=True)
    if proc.returncode != 0:
        log(f"runoak {' '.join(args[:2])} failed: {(proc.stderr.strip().splitlines() or ['?'])[-1]}")
        return None
    return proc.stdout


def tsv_rows(text: str) -> list[dict]:
    lines = [l for l in text.splitlines() if l.strip() and not l.startswith("#")]
    return list(csv.DictReader(io.StringIO("\n".join(lines)), delimiter="\t"))


def mondo_terms(mondo_id: str) -> tuple[str | None, list[str], str | None]:
    """Return (label, exact synonyms, MeSH ID) for a MONDO term via runoak."""
    out = runoak("labels", mondo_id)
    rows = tsv_rows(out) if out else []
    label = (rows[0].get("label") or None) if rows else None

    synonyms: list[str] = []
    out = runoak("aliases", "--obo-model", mondo_id)
    for r in tsv_rows(out) if out else []:
        pred = next((v for k, v in r.items() if k and "pred" in k.lower()), "") or ""
        value = next((v for k, v in r.items() if k and k.lower() in ("alias", "synonym", "value")), "") or ""
        if pred.endswith("hasExactSynonym") and value and value != label:
            synonyms.append(value)

    mesh = None
    out = runoak("mappings", "-O", "sssom", mondo_id)
    found = []
    for r in tsv_rows(out) if out else []:
        obj = r.get("object_id") or ""
        if obj.upper().startswith(("MESH:", "MSH:")):
            found.append((r.get("predicate_id") or "", obj.split(":", 1)[1]))
    if found:
        exact = [m for p, m in found if p.endswith("exactMatch")]
        mesh = (exact or [m for _, m in found])[0]
    return label, sorted(set(synonyms)), mesh


def quote(s: str) -> str:
    return " ".join(s.replace('"', "").split())


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("dating", type=Path, help="dating.tsv with verified cutoff dates")
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--run-config", type=Path, default=HERE / "RUN_CONFIG.yaml")
    ap.add_argument("--cache", type=Path, default=REPO / "tmp" / "pretest_cache")
    a = ap.parse_args()

    api_key = os.environ.get("NCBI_API_KEY", "").strip()
    if not api_key:
        sys.exit("NCBI_API_KEY is not set; it is required for E-utilities requests.")
    config = yaml.safe_load(a.run_config.read_text()) or {}
    if not isinstance(config.get("packet_minimum"), int):
        sys.exit(f"{a.run_config} has no integer packet_minimum")
    minimum = config["packet_minimum"]

    sys.path.insert(0, str(REPO / "src"))
    from dismech.oak_db import adapter_build_name, local_build_path
    db = local_build_path(adapter_build_name(MONDO_ADAPTER))
    if not db.is_file():
        sys.exit("The local MONDO build is required (exact synonyms and MeSH mappings are not served "
                 "by ols:mondo). Run: just fetch-ontology-dbs mondo")
    global MONDO_PATH_ADAPTER
    MONDO_PATH_ADAPTER = f"sqlite:{db.resolve()}"
    mondo_build = dt.date.fromtimestamp(db.stat().st_mtime).isoformat()

    with open(HERE / "frame.tsv", newline="", encoding="utf-8") as f:
        frame = [r for r in csv.DictReader(f, delimiter="\t") if r["flag_nongenetic_specimen"] == "TRUE"]
    with open(a.dating, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        fields = list(reader.fieldnames or [])
        rows = list(reader)
    missing = [c for c in REQUIRED if c not in fields]
    if missing:
        sys.exit(f"dating input is missing required column(s): {', '.join(missing)}")

    eu = EUtils(api_key, a.cache)
    terms_cache: dict[str, tuple] = {}
    for row in rows:
        given_mondo = (row.get("mondo_id") or "").strip()
        row.update({c: "NA" for c in ADDED if c not in fields})
        row["packet_minimum"] = str(minimum)
        row["mondo_build"] = mondo_build
        row["lit_ruling"] = row["lit_count"] = row["lit_query"] = "NA"
        if given_mondo:
            mondo_id = given_mondo
            row["mondo_id"] = mondo_id
        else:
            hits = [i for i, fr in enumerate(frame)
                    if fr["disease_name"] == row["disease"] and fr["row_name"] == row["test"]
                    and (not row.get("row_type") or fr["row_type"] == row["row_type"])]
            if len(hits) != 1:
                log(f"{row['disease']} / {row['test']}: matches {len(hits)} frame rows; add row_type")
                continue
            i = hits[0]
            mondo_id = frame[i]["mondo_id"]
            row["frame_idx"], row["mondo_id"] = str(i), mondo_id

        try:
            cutoff = dt.date.fromisoformat((row["cutoff_date"] or "").strip())
        except ValueError:
            cutoff = None
        status_ok = "dating_status" not in row or (row["dating_status"] or "").strip() == "ACCEPTED"
        if cutoff is None or (row["quote_ok"] or "").strip().upper() != "TRUE" or not status_ok:
            row["lit_ruling"] = "UNVERIFIED_CUTOFF"
            continue
        if not mondo_id.startswith("MONDO:"):
            log(f"{row['disease']}: no MONDO ID")
            continue

        if mondo_id not in terms_cache:
            terms_cache[mondo_id] = mondo_terms(mondo_id)
        label, synonyms, mesh_id = terms_cache[mondo_id]
        heading = eu.mesh_heading(mesh_id) if mesh_id else None
        row["mesh_id"] = f"MESH:{mesh_id}" if mesh_id else "NA"
        row["mesh_heading"] = heading or "NA"
        row["n_synonyms"] = str(len(synonyms))

        parts = []
        if heading:
            field = "MeSH Terms" if mesh_id.startswith("D") else "Supplementary Concept"
            parts.append(f'"{quote(heading)}"[{field}]')
        parts += [f'"{quote(t)}"[tiab]' for t in ([label] if label else []) + synonyms]
        alias = (row.get("literature_alias") or "").strip()
        if alias and alias != "NA":
            for item in (x.strip() for x in alias.split(";")):
                if item:
                    parts.append(f"({item})" if "[" in item else f'"{quote(item)}"[tiab]')
        if not parts:
            log(f"{mondo_id}: no MeSH heading, label or synonyms found")
            continue
        term = f"({' OR '.join(parts)}) AND hasabstract"
        row["lit_query"] = term
        n = eu.count(term, cutoff.strftime("%Y/%m/%d"))
        if n is None:
            continue
        row["lit_count"] = str(n)
        row["lit_ruling"] = "INSUFFICIENT_PRE_CUTOFF_LITERATURE" if n < minimum else "PASS"

    a.out.parent.mkdir(parents=True, exist_ok=True)
    with open(a.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields + [c for c in ADDED if c not in fields],
                           delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    main()
