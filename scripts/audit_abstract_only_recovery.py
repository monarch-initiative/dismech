#!/usr/bin/env python3
"""Census how many ``references_cache/PMID_*.md`` files cached as
``abstract_only`` actually have a recoverable PMC full text under the fixed
extractor (issue #10878, follow-up to the bug fixed in #10876).

#10876 fixed a bug in ``linkml-reference-validator``'s JATS extractor: it
discarded a paper's entire body if the word "restricted" appeared anywhere in
the document, rather than testing structurally for a non-empty ``<body>``.
#10878 asked whether that bug left other papers stranded as ``abstract_only``,
and explicitly asked for a *census* rather than a blanket refetch, since a bulk
rewrite of ``references_cache/`` would turn every open curation PR red on
merge (the same failure shape as #8623 and #10061).

This script performs that census in two network phases plus one offline phase:

1. ``idconv``  -- bulk-resolve every ``abstract_only`` PMID against the PMC ID
   Converter API (up to 200 IDs/request) to find which ones have a PMC record
   at all. This alone is a weak signal: most PMC records are **not** in the
   Open Access subset, so having a PMCID does not mean ``efetch`` will return
   a body -- see the ``not_open_access`` reason in phase 2.
2. ``recoverability`` -- for every PMID phase 1 found in PMC, fetch the actual
   article XML and run it through dismech's real patched extractor
   (``dismech.patch_reference_validator`` + the installed
   ``linkml_reference_validator``) to determine whether a body -- and how many
   tables -- would actually be recovered. This is the number that matters.
3. ``missing-tables`` -- offline. Counts already-cached ``full_text_xml``
   files that carry no ``## Table`` section yet (an upper bound on "papers
   that would gain a table on refetch", since some genuinely have none).

Each network phase is resumable: it appends to its output CSV and skips PMIDs
already recorded there, so an interrupted run (rate limiting, a dropped
connection) can just be re-invoked.

Usage::

    # full pipeline (can take ~2h for phase 2 over ~12k PMC-linked candidates,
    # since NCBI efetch without an API key is rate-limited to ~3 req/s)
    uv run python scripts/audit_abstract_only_recovery.py --phase all --out-dir tmp/abstract-only-census

    # just the offline table census (seconds)
    uv run python scripts/audit_abstract_only_recovery.py --phase missing-tables

    # resume an interrupted recoverability run
    uv run python scripts/audit_abstract_only_recovery.py --phase recoverability --out-dir tmp/abstract-only-census

An NCBI API key (``NCBI_API_KEY``) raises the E-utilities rate limit from 3 to
10 req/s and is picked up automatically if set.
"""
from __future__ import annotations

import argparse
import csv
import os
import re
import sys
import time
import urllib.error
import urllib.request

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE_DIR = os.path.join(REPO_ROOT, "references_cache")

IDCONV_URL = "https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/"
EFETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

PMID_RE = re.compile(r"^PMID_(\d+)\.md$")
CONTENT_TYPE_RE = re.compile(r"^content_type:\s*(\S+)\s*$", re.MULTILINE)
TABLE_HEADING_RE = re.compile(r"^## Table", re.MULTILINE)

MAX_RETRIES = 4


def _rate_limit_sleep(default: float) -> float:
    return 0.11 if os.environ.get("NCBI_API_KEY") else default


def _tool_email_params() -> str:
    key = os.environ.get("NCBI_API_KEY")
    params = "tool=dismech-abstract-only-audit&email=curation@dismech.invalid"
    if key:
        params += f"&api_key={key}"
    return params


def iter_pmid_cache_files():
    for name in os.listdir(CACHE_DIR):
        m = PMID_RE.match(name)
        if m:
            yield m.group(1), os.path.join(CACHE_DIR, name)


def enumerate_abstract_only() -> list[str]:
    """Offline. Returns bare PMIDs currently cached as abstract_only."""
    pmids = []
    for pmid, path in iter_pmid_cache_files():
        try:
            with open(path, encoding="utf-8", errors="replace") as f:
                head = f.read(4096)
        except OSError:
            continue
        m = CONTENT_TYPE_RE.search(head)
        if m and m.group(1) == "abstract_only":
            pmids.append(pmid)
    pmids.sort(key=int)
    return pmids


def phase_missing_tables() -> None:
    total = 0
    has_table = 0
    no_table: list[str] = []
    for pmid, path in iter_pmid_cache_files():
        try:
            with open(path, encoding="utf-8", errors="replace") as f:
                content = f.read()
        except OSError:
            continue
        m = CONTENT_TYPE_RE.search(content[:2048])
        if not m or m.group(1) != "full_text_xml":
            continue
        total += 1
        if TABLE_HEADING_RE.search(content):
            has_table += 1
        else:
            no_table.append(pmid)

    print(f"Total full_text_xml PMID cache files: {total}")
    print(f"  already carrying a '## Table' section: {has_table}")
    print(f"  carrying NO table section (upper bound on 'missing tables'): {len(no_table)}")


def _http_get(url: str, timeout: int = 30) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "dismech-abstract-only-audit/1.0"})
    last_exc: Exception | None = None
    for attempt in range(MAX_RETRIES):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
            last_exc = exc
            time.sleep(2**attempt)
    raise RuntimeError(f"GET failed after {MAX_RETRIES} retries: {last_exc}")


def phase_idconv(out_dir: str, batch_size: int, sleep_seconds: float) -> None:
    import json

    os.makedirs(out_dir, exist_ok=True)
    pmids_path = os.path.join(out_dir, "abstract_only_pmids.txt")
    results_path = os.path.join(out_dir, "idconv_results.csv")

    all_pmids = enumerate_abstract_only()
    with open(pmids_path, "w") as f:
        f.write("\n".join(all_pmids) + "\n")

    done: set[str] = set()
    if os.path.exists(results_path):
        with open(results_path, newline="") as f:
            done = {row["pmid"] for row in csv.DictReader(f)}

    todo = [p for p in all_pmids if p not in done]
    print(f"abstract_only PMIDs: {len(all_pmids)}; already resolved: {len(done)}; remaining: {len(todo)}")

    new_file = not os.path.exists(results_path)
    sleep_seconds = _rate_limit_sleep(sleep_seconds)
    with open(results_path, "a", newline="") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(["pmid", "pmcid", "doi", "status"])

        n_batches = (len(todo) + batch_size - 1) // batch_size
        for i in range(0, len(todo), batch_size):
            batch = todo[i : i + batch_size]
            batch_num = i // batch_size + 1
            url = f"{IDCONV_URL}?ids={','.join(batch)}&format=json&{_tool_email_params()}"
            try:
                data = json.loads(_http_get(url).decode("utf-8"))
            except RuntimeError as exc:
                print(f"BATCH {batch_num}/{n_batches} failed: {exc}", file=sys.stderr)
                for pmid in batch:
                    writer.writerow([pmid, "", "", "fetch_error"])
                f.flush()
                continue

            by_pmid = {
                str(r.get("requested-id") or r.get("pmid") or ""): r for r in data.get("records", [])
            }
            for pmid in batch:
                r = by_pmid.get(pmid)
                if r is None:
                    writer.writerow([pmid, "", "", "no_response"])
                elif r.get("status") == "error":
                    writer.writerow([pmid, "", "", "not_in_pmc"])
                else:
                    writer.writerow([pmid, r.get("pmcid", ""), r.get("doi", ""), "in_pmc"])
            f.flush()

            if batch_num % 10 == 0 or batch_num == n_batches:
                print(f"  batch {batch_num}/{n_batches} ({i + len(batch)}/{len(todo)})")
            time.sleep(sleep_seconds)

    print(f"Wrote {results_path}")


def phase_recoverability(out_dir: str, sleep_seconds: float) -> None:
    sys.path.insert(0, os.path.join(REPO_ROOT, "src"))
    import dismech.patch_reference_validator as patch  # noqa: PLC0415
    from bs4 import BeautifulSoup  # noqa: PLC0415
    from linkml_reference_validator.etl.extract.xml import XMLExtractor  # noqa: PLC0415

    idconv_path = os.path.join(out_dir, "idconv_results.csv")
    results_path = os.path.join(out_dir, "recoverability_results.csv")
    if not os.path.exists(idconv_path):
        raise SystemExit(f"Run --phase idconv first; {idconv_path} does not exist.")

    candidates = []
    with open(idconv_path, newline="") as f:
        for row in csv.DictReader(f):
            if row["status"] == "in_pmc" and row["pmcid"]:
                candidates.append((row["pmid"], row["pmcid"]))

    done: set[str] = set()
    if os.path.exists(results_path):
        with open(results_path, newline="") as f:
            done = {row["pmid"] for row in csv.DictReader(f)}
    todo = [c for c in candidates if c[0] not in done]
    print(f"PMC-linked candidates: {len(candidates)}; already checked: {len(done)}; remaining: {len(todo)}")

    extractor = XMLExtractor()
    sleep_seconds = _rate_limit_sleep(sleep_seconds)

    def classify(data: bytes):
        text_data = data.decode("utf-8", errors="replace")
        if not text_data.strip() or "<article" not in text_data:
            return False, 0, "no_article_element"

        body_text = extractor.extract(data)
        has_body = bool(body_text and body_text.strip())

        try:
            soup = BeautifulSoup(text_data, "xml")
        except Exception:  # noqa: BLE001
            return has_body, 0, "" if has_body else "soup_parse_error"

        tables_text = patch._jats_tables_as_text(soup)
        num_tables = tables_text.count("\n\n## ") + (1 if tables_text.startswith("## ") else 0)

        if has_body:
            reason = ""
        elif soup.find("body") is None:
            not_oa_markers = ("does not allow downloading", 'pmc-prop-open-access"><meta-value>no')
            reason = "not_open_access" if any(m in text_data for m in not_oa_markers) else "no_body_element"
        else:
            reason = "empty_body"
        return has_body, num_tables, reason

    new_file = not os.path.exists(results_path)
    with open(results_path, "a", newline="") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(["pmid", "pmcid", "has_body", "num_tables", "reason"])

        for i, (pmid, pmcid) in enumerate(todo, 1):
            url = f"{EFETCH_URL}?db=pmc&id={pmcid}&rettype=xml&{_tool_email_params()}"
            try:
                data = _http_get(url)
                has_body, num_tables, reason = classify(data)
            except Exception as exc:  # noqa: BLE001
                writer.writerow([pmid, pmcid, "error", 0, str(exc)[:200]])
                f.flush()
                time.sleep(sleep_seconds)
                continue

            writer.writerow([pmid, pmcid, has_body, num_tables, reason])
            f.flush()
            if i % 200 == 0 or i == len(todo):
                print(f"  {i}/{len(todo)}")
            time.sleep(sleep_seconds)

    print(f"Wrote {results_path}")


def phase_summarize(out_dir: str) -> None:
    idconv_path = os.path.join(out_dir, "idconv_results.csv")
    recov_path = os.path.join(out_dir, "recoverability_results.csv")

    total_abstract_only = 0
    in_pmc = 0
    if os.path.exists(idconv_path):
        with open(idconv_path, newline="") as f:
            for row in csv.DictReader(f):
                total_abstract_only += 1
                if row["status"] == "in_pmc":
                    in_pmc += 1

    if not os.path.exists(recov_path):
        print(f"abstract_only PMIDs censused: {total_abstract_only}")
        print(f"  with a PMC record: {in_pmc}")
        print("(run --phase recoverability for true-recovery numbers)")
        return

    checked = 0
    recoverable = 0
    with_tables = 0
    total_tables = 0
    reasons: dict[str, int] = {}
    with open(recov_path, newline="") as f:
        for row in csv.DictReader(f):
            checked += 1
            if row["has_body"] == "True":
                recoverable += 1
                n = int(row["num_tables"] or 0)
                total_tables += n
                if n > 0:
                    with_tables += 1
            else:
                reasons[row["reason"] or "(unknown)"] = reasons.get(row["reason"] or "(unknown)", 0) + 1

    print(f"abstract_only PMIDs censused: {total_abstract_only}")
    print(f"  with a PMC record (idconv):            {in_pmc}")
    print(f"  checked for true recoverability:        {checked}")
    print(f"  TRUE positives -- body now recoverable: {recoverable}")
    print(f"    of those, carrying >=1 table:         {with_tables}  (tables found: {total_tables})")
    print("  non-recovery reasons among the rest:")
    for reason, count in sorted(reasons.items(), key=lambda x: -x[1]):
        print(f"    {reason}: {count}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--phase",
        choices=["idconv", "recoverability", "missing-tables", "summarize", "all"],
        default="summarize",
    )
    parser.add_argument("--out-dir", default="tmp/abstract-only-census", help="where CSV results are written/read")
    parser.add_argument("--batch-size", type=int, default=180, help="idconv PMIDs per request (max 200)")
    parser.add_argument("--sleep", type=float, default=0.4, help="seconds between requests (ignored if NCBI_API_KEY set)")
    args = parser.parse_args()

    if args.phase in ("missing-tables", "all"):
        phase_missing_tables()
    if args.phase in ("idconv", "all"):
        phase_idconv(args.out_dir, args.batch_size, args.sleep)
    if args.phase in ("recoverability", "all"):
        phase_recoverability(args.out_dir, args.sleep)
    if args.phase in ("summarize", "all"):
        phase_summarize(args.out_dir)


if __name__ == "__main__":
    main()
