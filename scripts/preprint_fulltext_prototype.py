#!/usr/bin/env python3
"""Prototype: fetch full text for a preprint, for a future preprint-scan action.

This is a spike, NOT production code. It demonstrates two routes to preprint
full text and records which one actually works without special infrastructure.

Findings (verified 2026-06-28 against live services):

1. Europe PMC `fulltextRepo` (PRIMARY, works now)
   - Europe PMC indexes ~60k preprints with open-access full text
     (`SRC:PPR AND HAS_FT:Y`). The REST `/{src}/{id}/fullTextXML` endpoint
     404s for preprints, BUT each core record's `fullTextUrlList` carries a
     direct Europe-PMC-hosted PDF URL (`/api/fulltextRepo?pprId=...`) that
     downloads openly — no AWS, no Cloudflare challenge.
   - Caveat: coverage is the subset Europe PMC has ingested. The newest
     openRxiv preprints (2026, DOI prefix 10.64898) are not in Europe PMC yet,
     and a minority of HAS_FT records return a stale-filename error blob
     instead of the PDF, so callers MUST validate the `%PDF-` magic bytes.

2. openRxiv S3 TDM bucket (BULK fallback, needs credentials)
   - `s3://biorxiv-src-monthly/` and `s3://medrxiv-src-monthly/` are
     requester-pays buckets of MECA archives (JATS XML + PDF). They are the
     sanctioned bulk text-mining channel and cover ALL bioRxiv/medRxiv
     including the freshest openRxiv content as clean JATS.
   - Downsides: requires valid AWS credentials + requester-pays, and the
     layout is monthly MECA dumps (not addressable per-DOI without first
     building a DOI->key index from a month sync). Coded below but left
     untested here because the sandbox's AWS key is rejected (InvalidAccessKeyId).

3. Direct bioRxiv/openRxiv PDF URLs (NOT viable for automation)
   - `https://www.biorxiv.org/content/{doi}v{n}.full.pdf` is real and open to a
     browser, but sits behind a Cloudflare "Just a moment..." bot challenge
     (verified HTTP 403 challenge page). A scheduled GitHub Action on a
     datacenter IP will be challenged, so this route is deliberately omitted.

Usage:
    uv run python scripts/preprint_fulltext_prototype.py --query "tau AND mechanism"
    uv run python scripts/preprint_fulltext_prototype.py --doi 10.21203/rs.3.rs-9264510/v1
"""

from __future__ import annotations

import argparse
import io
import re
import sys
from dataclasses import dataclass
from typing import Any

import httpx

EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/"


@dataclass
class PreprintFullText:
    ppr_id: str
    doi: str
    title: str
    pdf_bytes: bytes
    text: str
    n_pages: int


def _epmc_record(client: httpx.Client, query: str) -> dict[str, Any] | None:
    resp = client.get(
        EPMC + "search",
        params={
            "query": f"({query}) AND SRC:PPR AND HAS_FT:Y",
            "resultType": "core",
            "format": "json",
            "pageSize": 25,
        },
    )
    resp.raise_for_status()
    results = resp.json().get("resultList", {}).get("result", [])
    return results or None


def _pdf_url(record: dict[str, Any]) -> str | None:
    for url in record.get("fullTextUrlList", {}).get("fullTextUrl", []):
        if url.get("documentStyle") == "pdf" and url.get("site") == "Europe_PMC":
            return url.get("url")
    return None


def _pdf_to_text(pdf_bytes: bytes, max_pages: int = 12) -> tuple[str, int]:
    from pypdf import PdfReader

    reader = PdfReader(io.BytesIO(pdf_bytes))
    pages = reader.pages
    chunks = [(pages[i].extract_text() or "") for i in range(min(max_pages, len(pages)))]
    text = re.sub(r"[ \t]+", " ", "\n".join(chunks))
    return text, len(pages)


def fetch_via_europe_pmc(
    client: httpx.Client, *, query: str | None, doi: str | None
) -> PreprintFullText | None:
    """PRIMARY route. Returns the first HAS_FT preprint whose PDF really resolves."""
    search = f'DOI:"{doi}"' if doi else query
    records = _epmc_record(client, search or "")
    if not records:
        return None
    for record in records:
        url = _pdf_url(record)
        if not url:
            continue
        resp = client.get(url)
        # Stale-filename records return an 85-byte JSON error blob, not a PDF.
        if resp.status_code != 200 or resp.content[:5] != b"%PDF-":
            continue
        text, n_pages = _pdf_to_text(resp.content)
        return PreprintFullText(
            ppr_id=str(record.get("id")),
            doi=str(record.get("doi") or ""),
            title=str(record.get("title") or ""),
            pdf_bytes=resp.content,
            text=text,
            n_pages=n_pages,
        )
    return None


def fetch_via_s3_meca(doi: str) -> bytes | None:  # pragma: no cover - needs creds
    """BULK fallback (sanctioned TDM). Requires valid AWS creds + requester-pays.

    The monthly buckets are not DOI-addressable: a real implementation must
    sync a `Current_Content/<Month_Year>/` prefix, read each MECA's manifest to
    map DOI -> key, then extract the JATS `.xml` from the MECA (a plain zip).
    This stub shows the boto3 call shape and is intentionally not wired into the
    CLI because the sandbox AWS key is rejected (InvalidAccessKeyId).
    """
    import zipfile

    import boto3

    s3 = boto3.client("s3")
    bucket, key = _resolve_meca_key(s3, doi)  # not implemented in the spike
    buf = io.BytesIO()
    s3.download_fileobj(bucket, key, buf, ExtraArgs={"RequestPayer": "requester"})
    with zipfile.ZipFile(buf) as meca:
        xml_name = next(n for n in meca.namelist() if n.endswith(".xml") and "manifest" not in n)
        return meca.read(xml_name)


def _resolve_meca_key(s3: Any, doi: str):  # pragma: no cover - spike placeholder
    raise NotImplementedError(
        "DOI->MECA-key indexing requires a monthly prefix sync; out of scope for the spike."
    )


def _first_excerpt(text: str, width: int = 400) -> str:
    for kw in ("we found", "we show", "we demonstrate", "results", "conclusion", "mechanism"):
        idx = text.lower().find(kw)
        if idx > 0:
            return re.sub(r"\s+", " ", text[idx : idx + width])
    return re.sub(r"\s+", " ", text[:width])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", help="Europe PMC free-text query (preprints)")
    parser.add_argument("--doi", help="Preprint DOI to resolve")
    parser.add_argument("--timeout", type=float, default=180.0)
    args = parser.parse_args()

    if not args.query and not args.doi:
        parser.error("provide --query or --doi")

    with httpx.Client(timeout=args.timeout, follow_redirects=True) as client:
        result = fetch_via_europe_pmc(client, query=args.query, doi=args.doi)

    if result is None:
        print("No open-access preprint full text found via Europe PMC.", file=sys.stderr)
        return 1

    print(f"Preprint:  {result.ppr_id}  (DOI {result.doi})")
    print(f"Title:     {result.title}")
    print(f"PDF bytes: {len(result.pdf_bytes):,}  pages: {result.n_pages}")
    print(f"Extracted: {len(result.text):,} chars of body text")
    print("\n--- quotable body excerpt ---")
    print(_first_excerpt(result.text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
