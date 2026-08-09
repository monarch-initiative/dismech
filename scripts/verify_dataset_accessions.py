#!/usr/bin/env python3
"""Verify that ``datasets[].accession`` values resolve to real repository records.

The dismech validation stack checks literature references (PMID/DOI/NCT) but has
no equivalent for dataset accessions, so a hallucinated ``geo:GSE9999999`` passes
``just qc`` today. This script closes that gap by resolving each accession
against the authoritative repository API and reporting the record it found.

Supported repositories
----------------------
======================  =============================================
Prefix                  Resolver
======================  =============================================
``geo``                 NCBI E-utilities ``gds`` (GSE/GDS/GPL/GSM)
``sra``                 NCBI E-utilities ``sra`` (SRP/SRR/SRX/SRS/ERP/ERR/DRP)
``bioproject``          NCBI E-utilities ``bioproject`` (PRJNA/PRJEB/PRJDB)
``dbgap``               NCBI E-utilities ``gap`` (phs######)
``arrayexpress``        EBI BioStudies (E-MTAB-####, E-GEOD-####)
``scea``                EBI Single Cell Expression Atlas (E-####-####)
``pride``               EBI PRIDE (PXD######)
``metabolights``        EBI MetaboLights (MTBLS###)
``ega``                 EGA metadata API (EGAS/EGAD########)
``osdr`` / ``nasa_osdr``NASA OSDR (OSD-###)
``massive``             MassIVE (MSV#########)
``mgnify``              EBI MGnify (MGYS########)
======================  =============================================

Accessions whose prefix is a literature identifier (``PMID``, ``DOI``) or a
resource with no public per-record API (``cellxgene``, ``morphic``) are
reported as ``UNSUPPORTED`` rather than failed --
they are not verifiable here and need a human or a different check.

Usage
-----
    # audit everything already in the KB
    uv run python scripts/verify_dataset_accessions.py --all

    # verify one or more files (use before committing new curation)
    uv run python scripts/verify_dataset_accessions.py kb/disorders/Asthma.yaml

    # verify bare accessions, e.g. candidates from a deep-research report
    uv run python scripts/verify_dataset_accessions.py --accession geo:GSE67472

    # fail the process when anything is NOT_FOUND (for CI / batch gating)
    uv run python scripts/verify_dataset_accessions.py --all --strict

Results are cached in ``cache/dataset_accessions.json`` so repeat runs and CI do
not re-hit the public APIs. Use ``--refresh`` to bypass the cache.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
CACHE_PATH = REPO_ROOT / "cache" / "dataset_accessions.json"
KB_GLOBS = ("kb/disorders/*.yaml", "kb/modules/*.yaml", "kb/comorbidities/*.yaml")

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
USER_AGENT = "dismech-dataset-verifier (https://github.com/monarch-initiative/dismech)"

# Status values
OK = "OK"
NOT_FOUND = "NOT_FOUND"
UNSUPPORTED = "UNSUPPORTED"
MALFORMED = "MALFORMED"
ERROR = "ERROR"
# The record exists, but it is filed under the wrong repository prefix
# (e.g. `sra:PRJNA290729`, which is really a BioProject accession).
PREFIX_MISMATCH = "PREFIX_MISMATCH"

# How long a NOT_FOUND result is trusted before being re-checked. Datasets are
# often deposited under embargo and become visible only at publication.
NEGATIVE_CACHE_DAYS = 30

# Prefixes that are literature identifiers or lack a per-record public API.
UNSUPPORTED_PREFIXES = {
    "pmid": "literature identifier, not a dataset accession",
    "doi": "literature identifier, not a dataset accession",
    "clinicaltrials": "trial registry; verified by the reference validator",
    "cellxgene": "no stable per-collection metadata API contract",
    "gtex": "GTEx portal tissue pointer, not a per-record accession",
    "encode": "ENCODE portal pointer; use the ENCSR accession if one is known",
    "tcga": "TCGA project pointer; use the GDC/dbGaP accession if one is known",
    # Declared in the schema prefix map and legitimate to curate, but with no
    # per-record public metadata API to resolve against. Listed here so a
    # curator adding one gets "reported, not verifiable" rather than a CI error.
    "hca": "Human Cell Atlas project pointer; no per-record metadata API contract",
    "synapse": "Synapse entity pointer; access-controlled, no open metadata API",
    "clinvar": "variant database pointer, not a dataset accession",
    "morphic": "MorPhiC gene-level pointer, not a repository accession",
    "https": "bare URL; replace with a repository CURIE",
    "http": "bare URL; replace with a repository CURIE",
}

# accession shape checks, applied before hitting the network
SHAPE = {
    "geo": re.compile(r"^(GSE|GDS|GPL|GSM)\d+$", re.IGNORECASE),
    "sra": re.compile(r"^([SED]R[PRXS])\d+$", re.IGNORECASE),
    "bioproject": re.compile(r"^PRJ(NA|EB|DB)\d+$", re.IGNORECASE),
    "dbgap": re.compile(r"^phs\d+(\.v\d+)?(\.p\d+)?$", re.IGNORECASE),
    "arrayexpress": re.compile(r"^E-[A-Z]+-\d+$", re.IGNORECASE),
    "scea": re.compile(r"^E-[A-Z]+-\d+$", re.IGNORECASE),
    "pride": re.compile(r"^PXD\d+$", re.IGNORECASE),
    "metabolights": re.compile(r"^MTBLS\d+$", re.IGNORECASE),
    "ega": re.compile(r"^EGA[SD]\d+$", re.IGNORECASE),
    "osdr": re.compile(r"^OSD-\d+$", re.IGNORECASE),
    "massive": re.compile(r"^MSV\d+$", re.IGNORECASE),
    "mgnify": re.compile(r"^MGYS\d+$", re.IGNORECASE),
    "metabolomics_workbench": re.compile(r"^ST\d+$", re.IGNORECASE),
}

# Prefixes whose accession pattern is too permissive to serve as a fallback
# when another prefix's shape check fails (see verify_one).
NON_FALLBACK_PREFIXES: set[str] = set()

# Alternate spellings seen in the KB -> canonical prefix
PREFIX_ALIASES = {
    "nasa_osdr": "osdr",
    "geo_series": "geo",
    "ae": "arrayexpress",
    "proteomexchange": "pride",
}


@dataclass
class Result:
    accession: str
    prefix: str
    local_id: str
    status: str
    title: str = ""
    detail: str = ""
    extra: dict[str, Any] = field(default_factory=dict)
    sources: list[str] = field(default_factory=list)
    # ISO date this accession was last resolved against the live API
    checked: str = ""

    def as_row(self) -> str:
        return "\t".join(
            [
                self.status,
                self.accession,
                (self.title or self.detail).replace("\t", " ")[:110],
                ",".join(sorted(set(self.sources)))[:80],
            ]
        )


class Throttle:
    """NCBI allows 3 req/s anonymously, 10 req/s with an API key."""

    def __init__(self, per_second: float) -> None:
        self.interval = 1.0 / per_second
        self._last = 0.0

    def wait(self) -> None:
        delta = time.monotonic() - self._last
        if delta < self.interval:
            time.sleep(self.interval - delta)
        self._last = time.monotonic()


def http_json(url: str, throttle: Throttle | None = None, retries: int = 3) -> Any:
    last_err: Exception | None = None
    for attempt in range(retries):
        if throttle:
            throttle.wait()
        req = urllib.request.Request(
            url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"}
        )
        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                return json.loads(resp.read().decode("utf-8", "replace"))
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return None
            last_err = exc
            time.sleep(1.5 * (attempt + 1))
        except Exception as exc:
            last_err = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"request failed after {retries} attempts: {url} ({last_err})")


def http_text(
    url: str, throttle: Throttle | None = None, retries: int = 3
) -> str | None:
    """Fetch a text page, returning ``None`` for a definitive 404."""
    last_err: Exception | None = None
    for attempt in range(retries):
        if throttle:
            throttle.wait()
        req = urllib.request.Request(
            url, headers={"User-Agent": USER_AGENT, "Accept": "text/html"}
        )
        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                return resp.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return None
            last_err = exc
            time.sleep(1.5 * (attempt + 1))
        except Exception as exc:
            last_err = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"request failed after {retries} attempts: {url} ({last_err})")


# --------------------------------------------------------------------------- #
# Resolvers. Each returns (status, title, detail, extra).
# --------------------------------------------------------------------------- #


def _eutils_lookup(
    db: str, term: str, local_id: str, throttle: Throttle, api_key: str | None
):
    params = {"db": db, "term": term, "retmode": "json", "retmax": "5"}
    if api_key:
        params["api_key"] = api_key
    data = http_json(
        f"{EUTILS}/esearch.fcgi?{urllib.parse.urlencode(params)}", throttle
    )
    ids = (data or {}).get("esearchresult", {}).get("idlist") or []
    if not ids:
        return NOT_FOUND, "", f"no {db} record for {local_id}", {}

    sparams = {"db": db, "id": ids[0], "retmode": "json"}
    if api_key:
        sparams["api_key"] = api_key
    summary = http_json(
        f"{EUTILS}/esummary.fcgi?{urllib.parse.urlencode(sparams)}", throttle
    )
    doc = ((summary or {}).get("result") or {}).get(ids[0]) or {}

    # Defence in depth: confirm the record NCBI returned is the one asked for.
    # Field-restricted misses currently return count=0 rather than falling back
    # to an unrestricted search, but a silent fallback would otherwise turn a
    # nonexistent accession into a confident OK -- the one thing this script
    # exists to prevent.
    echoed = str(doc.get("accession") or doc.get("project_acc") or "").upper()
    if echoed and echoed != local_id.upper():
        return NOT_FOUND, "", f"{db} returned {echoed}, not {local_id}", {}

    title = (
        doc.get("title")
        or doc.get("project_title")
        or doc.get("d_study_name")
        or doc.get("expname")
        or ""
    )
    extra = {}
    for key, out in (
        ("gdstype", "gds_type"),
        ("n_samples", "sample_count"),
        ("taxon", "organism"),
        ("gpl", "platform"),
        ("pubmedids", "pubmed_ids"),
        ("summary", "summary"),
        ("project_data_type", "project_data_type"),
        ("d_study_name", "study_name"),
    ):
        if doc.get(key):
            extra[out] = doc[key]
    return OK, title, "", extra


def resolve_geo(local_id: str, throttle: Throttle, api_key: str | None):
    return _eutils_lookup("gds", f"{local_id}[ACCN]", local_id, throttle, api_key)


def resolve_sra(local_id: str, throttle: Throttle, api_key: str | None):
    return _eutils_lookup("sra", f"{local_id}[Accession]", local_id, throttle, api_key)


def resolve_bioproject(local_id: str, throttle: Throttle, api_key: str | None):
    return _eutils_lookup(
        "bioproject", f"{local_id}[Project Accession]", local_id, throttle, api_key
    )


def resolve_dbgap(local_id: str, throttle: Throttle, api_key: str | None):
    base = local_id.split(".")[0]
    return _eutils_lookup("gap", f"{base}[Study Accession]", base, throttle, api_key)


def resolve_arrayexpress(local_id: str, throttle: Throttle, api_key: str | None):
    data = http_json(
        f"https://www.ebi.ac.uk/biostudies/api/v1/studies/{urllib.parse.quote(local_id)}"
    )
    if not data:
        return NOT_FOUND, "", f"no BioStudies record for {local_id}", {}
    title = ""
    for attr in data.get("attributes", []) or []:
        if str(attr.get("name", "")).lower() == "title":
            title = attr.get("value", "")
            break
    section = data.get("section") or {}
    if not title:
        for attr in section.get("attributes", []) or []:
            if str(attr.get("name", "")).lower() == "title":
                title = attr.get("value", "")
                break
    return OK, title, "", {}


def resolve_scea(local_id: str, throttle: Throttle, api_key: str | None):
    page = http_text(
        "https://www.ebi.ac.uk/gxa/sc/experiments/" + urllib.parse.quote(local_id),
        throttle,
    )
    if page is None:
        return (
            NOT_FOUND,
            "",
            f"no Single Cell Expression Atlas experiment {local_id}",
            {},
        )
    match = re.search(
        r'<h3\s+id=["\']goto-experiment["\']>(.*?)</h3>',
        page,
        flags=re.IGNORECASE | re.DOTALL,
    )
    title = (
        html.unescape(re.sub(r"<[^>]+>", "", match.group(1))).strip() if match else ""
    )
    return OK, title, "", {}


def resolve_pride(local_id: str, throttle: Throttle, api_key: str | None):
    data = http_json(
        f"https://www.ebi.ac.uk/pride/ws/archive/v2/projects/{urllib.parse.quote(local_id)}"
    )
    if not data:
        return NOT_FOUND, "", f"no PRIDE project {local_id}", {}
    return OK, data.get("title", ""), "", {}


def resolve_metabolights(local_id: str, throttle: Throttle, api_key: str | None):
    data = http_json(
        f"https://www.ebi.ac.uk/metabolights/ws/studies/{urllib.parse.quote(local_id)}"
    )
    if not data:
        return NOT_FOUND, "", f"no MetaboLights study {local_id}", {}
    study = data.get("content") or data.get("study") or {}
    return OK, study.get("title", "") if isinstance(study, dict) else "", "", {}


def resolve_ega(local_id: str, throttle: Throttle, api_key: str | None):
    kind = "studies" if local_id.upper().startswith("EGAS") else "datasets"
    data = http_json(
        f"https://metadata.ega-archive.org/{kind}/{urllib.parse.quote(local_id)}"
    )
    if not data:
        return NOT_FOUND, "", f"no EGA {kind[:-1]} {local_id}", {}
    return OK, data.get("title") or data.get("description", "") or "", "", {}


def resolve_osdr(local_id: str, throttle: Throttle, api_key: str | None):
    num = local_id.split("-")[-1]
    data = http_json(
        f"https://osdr.nasa.gov/osdr/data/osd/meta/{urllib.parse.quote(num)}"
    )
    if not data:
        return NOT_FOUND, "", f"no OSDR study {local_id}", {}
    try:
        study = next(iter((data.get("study") or {}).values()))
        title = (
            (study.get("additionalInformation") or {}).get("description") or {}
        ).get("Study Title", "")
        if not title:
            title = (study.get("studies") or [{}])[0].get("title", "")
    except (StopIteration, AttributeError, IndexError):
        title = ""
    return OK, title, "", {}


def resolve_massive(local_id: str, throttle: Throttle, api_key: str | None):
    data = http_json(
        f"https://massive.ucsd.edu/ProteoSAFe/proxi/v0.1/datasets/{urllib.parse.quote(local_id)}"
    )
    if not data:
        return NOT_FOUND, "", f"no MassIVE dataset {local_id}", {}
    return OK, data.get("title", ""), "", {}


def resolve_mgnify(local_id: str, throttle: Throttle, api_key: str | None):
    data = http_json(
        f"https://www.ebi.ac.uk/metagenomics/api/v1/studies/{urllib.parse.quote(local_id)}"
    )
    if not data:
        return NOT_FOUND, "", f"no MGnify study {local_id}", {}
    attrs = (data.get("data") or {}).get("attributes") or {}
    return OK, attrs.get("study-name", ""), "", {}


def resolve_metabolomics_workbench(
    local_id: str, throttle: Throttle, api_key: str | None
):
    """Resolve a Metabolomics Workbench study (ST######) via its REST API."""
    data = http_json(
        f"https://www.metabolomicsworkbench.org/rest/study/study_id/"
        f"{urllib.parse.quote(local_id)}/summary"
    )
    if not data or not isinstance(data, dict) or not data.get("study_id"):
        return NOT_FOUND, "", f"no Metabolomics Workbench study {local_id}", {}
    extra = {}
    for src, dst in (
        ("number_of_samples", "sample_count"),
        ("analysis_type", "analysis_type"),
        ("species", "organism"),
    ):
        if data.get(src):
            extra[dst] = data[src]
    return OK, data.get("study_title", ""), "", extra


RESOLVERS = {
    "geo": resolve_geo,
    "sra": resolve_sra,
    "bioproject": resolve_bioproject,
    "dbgap": resolve_dbgap,
    "arrayexpress": resolve_arrayexpress,
    "scea": resolve_scea,
    "pride": resolve_pride,
    "metabolights": resolve_metabolights,
    "ega": resolve_ega,
    "osdr": resolve_osdr,
    "massive": resolve_massive,
    "mgnify": resolve_mgnify,
    "metabolomics_workbench": resolve_metabolomics_workbench,
}


def split_accession(accession: str) -> tuple[str, str]:
    """Return (canonical_prefix, local_id) for a dataset accession string."""
    raw = str(accession).strip()
    if ":" in raw and not raw.lower().startswith(("http://", "https://")):
        prefix, local = raw.split(":", 1)
    elif raw.lower().startswith(("http://", "https://")):
        return "https", raw
    else:
        # bare accession, e.g. "GSE12345" -- infer the repository from its shape
        prefix = ""
        for candidate, pattern in SHAPE.items():
            if pattern.match(raw):
                prefix = candidate
                break
        local = raw
    prefix = prefix.strip().lower()
    prefix = PREFIX_ALIASES.get(prefix, prefix)
    return prefix, local.strip()


def verify_one(
    accession: str, cache: dict, throttle: Throttle, api_key: str | None, refresh: bool
) -> Result:
    prefix, local_id = split_accession(accession)
    res = Result(accession=accession, prefix=prefix, local_id=local_id, status=ERROR)

    if not prefix:
        res.status = MALFORMED
        res.detail = "no repository prefix and shape not recognized"
        return res
    if prefix in UNSUPPORTED_PREFIXES:
        res.status = UNSUPPORTED
        res.detail = UNSUPPORTED_PREFIXES[prefix]
        return res
    if prefix not in RESOLVERS:
        res.status = UNSUPPORTED
        res.detail = f"no resolver for prefix '{prefix}'"
        return res

    shape = SHAPE.get(prefix)
    mismatch_from = ""
    if shape and not shape.match(local_id):
        # The declared prefix is wrong, but the accession may still be a real
        # record in a sibling repository (the common case is a BioProject
        # accession filed as `sra:`). Re-resolve against the repository whose
        # shape it actually matches, and report the correction.
        #
        actual = next(
            (
                p
                for p, pat in SHAPE.items()
                if p not in NON_FALLBACK_PREFIXES
                and pat.match(local_id)
                and p in RESOLVERS
            ),
            "",
        )
        if not actual:
            res.status = MALFORMED
            res.detail = f"'{local_id}' does not match the {prefix} accession pattern"
            return res
        mismatch_from, prefix = prefix, actual

    key = f"{prefix}:{local_id.upper()}"
    cached = cache.get(key) if not refresh else None
    # A NOT_FOUND is not necessarily permanent -- GEO accessions are routinely
    # embargoed until publication -- so negative results expire and get retried.
    if cached and cached.get("status") == NOT_FOUND:
        checked = cached.get("checked", "")
        try:
            age = (
                dt.datetime.now(dt.UTC).date() - dt.date.fromisoformat(checked[:10])
            ).days
        except (TypeError, ValueError):
            age = 10**6
        if age > NEGATIVE_CACHE_DAYS:
            cached = None

    if cached:
        status, title = cached["status"], cached.get("title", "")
        detail, extra = cached.get("detail", ""), cached.get("extra", {})
        res.checked = cached.get("checked", "")
    else:
        try:
            status, title, detail, extra = RESOLVERS[prefix](
                local_id, throttle, api_key
            )
        except Exception as exc:
            res.status = ERROR
            res.detail = str(exc)[:200]
            return res
        if status in (OK, NOT_FOUND):
            res.checked = dt.datetime.now(dt.UTC).date().isoformat()
            cache[key] = {
                "status": status,
                "title": title,
                "detail": detail,
                "extra": extra,
                "checked": res.checked,
            }

    if mismatch_from and status == OK:
        status = PREFIX_MISMATCH
        detail = (
            f"real {prefix} record; prefix should be '{prefix}:' not '{mismatch_from}:'"
        )

    res.prefix = prefix
    res.status, res.title, res.detail, res.extra = status, title, detail, extra
    return res


def collect_accessions(paths: Iterable[Path]) -> dict[str, list[str]]:
    """Map accession -> list of "file#dataset-title" sources."""
    found: dict[str, list[str]] = {}
    for path in paths:
        try:
            doc = yaml.safe_load(path.read_text())
        except Exception as exc:
            print(f"WARN  could not parse {path}: {exc}", file=sys.stderr)
            continue
        if not isinstance(doc, dict):
            continue
        for ds in doc.get("datasets") or []:
            if isinstance(ds, dict) and ds.get("accession"):
                found.setdefault(str(ds["accession"]), []).append(path.name)
        # datasets may also hang off proposed experiments
        for disc in doc.get("discussions") or []:
            for exp in (disc or {}).get("proposed_experiments") or []:
                for ds in (exp or {}).get("datasets") or []:
                    if isinstance(ds, dict) and ds.get("accession"):
                        found.setdefault(str(ds["accession"]), []).append(path.name)
    return found


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("files", nargs="*", type=Path, help="KB YAML files to check")
    ap.add_argument(
        "--all", action="store_true", help="check every dataset accession in kb/"
    )
    ap.add_argument(
        "--accession",
        action="append",
        default=[],
        help="check a bare accession (repeatable)",
    )
    ap.add_argument(
        "--strict",
        action="store_true",
        help="exit non-zero if any accession is NOT_FOUND/MALFORMED",
    )
    ap.add_argument(
        "--refresh", action="store_true", help="ignore the cache and re-query the APIs"
    )
    ap.add_argument("--json", type=Path, help="write full results to a JSON file")
    ap.add_argument(
        "--quiet", action="store_true", help="only print problems and the summary"
    )
    args = ap.parse_args()

    paths: list[Path] = list(args.files)
    if args.all:
        for pattern in KB_GLOBS:
            paths.extend(sorted(REPO_ROOT.glob(pattern)))
    if not paths and not args.accession:
        ap.error("pass files, --all, or --accession")

    sources = collect_accessions(paths)
    for acc in args.accession:
        sources.setdefault(acc, []).append("<cli>")
    if not sources:
        print("No dataset accessions found.")
        return 0

    api_key = None
    import os

    api_key = os.environ.get("NCBI_API_KEY")
    throttle = Throttle(9.0 if api_key else 2.5)

    cache: dict[str, Any] = {}
    if CACHE_PATH.exists():
        try:
            cache = json.loads(CACHE_PATH.read_text())
        except json.JSONDecodeError:
            cache = {}

    results: list[Result] = []
    total = len(sources)
    for idx, (acc, srcs) in enumerate(sorted(sources.items()), 1):
        res = verify_one(acc, cache, throttle, api_key, args.refresh)
        res.sources = srcs
        results.append(res)
        if not args.quiet or res.status not in (OK, UNSUPPORTED):
            print(f"[{idx}/{total}] {res.as_row()}", flush=True)

    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(json.dumps(cache, indent=2, sort_keys=True) + "\n")

    if args.json:
        args.json.write_text(
            json.dumps(
                [
                    {
                        "accession": r.accession,
                        "prefix": r.prefix,
                        "status": r.status,
                        "title": r.title,
                        "detail": r.detail,
                        "extra": r.extra,
                        "sources": r.sources,
                    }
                    for r in results
                ],
                indent=2,
            )
            + "\n"
        )

    counts: dict[str, int] = {}
    for r in results:
        counts[r.status] = counts.get(r.status, 0) + 1
    print("\n=== Dataset accession verification ===")
    for status in (OK, PREFIX_MISMATCH, NOT_FOUND, MALFORMED, UNSUPPORTED, ERROR):
        if counts.get(status):
            print(f"  {status:<12} {counts[status]}")
    print(f"  {'TOTAL':<12} {len(results)}")

    bad = [r for r in results if r.status in (NOT_FOUND, MALFORMED)]
    if bad:
        print("\nAccessions that do not resolve:")
        for r in bad:
            print(
                f"  {r.status}  {r.accession}  ({', '.join(sorted(set(r.sources)))})  {r.detail}"
            )

    if args.strict and bad:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
