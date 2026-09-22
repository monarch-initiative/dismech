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
   article XML (falling back to the PMC HTML page, exactly as
   ``PMCFullTextProvider.locate`` does) and run it through dismech's real
   patched extractor (``dismech.patch_reference_validator`` + the installed
   ``linkml_reference_validator``) to determine whether a body -- long enough
   to pass the same ``_MIN_PMC_FULLTEXT_CHARS`` floor production applies --
   and how many tables -- would actually be recovered. Each row also records
   the cache file's current ``full_text_attempted`` flag, so the
   attempted-vs-never-attempted policy split is a column, not a separate
   offline join someone has to remember to redo.
3. ``missing-tables`` -- offline. Counts already-cached ``full_text_xml``
   files that carry no ``## Table`` section yet (an upper bound on "papers
   that would gain a table on refetch", since some genuinely have none).

Each network phase is resumable: it appends to its output CSV and skips PMIDs
already recorded there. A *terminal* result (a real API answer, positive or
negative) is never retried; a *transient* one (``fetch_error``, ``error`` --
a dropped connection, a timeout) is retried on the next invocation, since it
is not actually an answer.

Usage::

    # full pipeline (can take a few hours for phase 2 over ~12k PMC-linked
    # candidates, since NCBI efetch without an API key is rate-limited to
    # ~3 req/s and a fraction of those also need the slower HTML fallback)
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

from dismech.frontmatter import split_frontmatter

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE_DIR = os.path.join(REPO_ROOT, "references_cache")

IDCONV_URL = "https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/"
EFETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
PMC_ARTICLE_URL = "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{pmcid}/"

PMID_RE = re.compile(r"^PMID_(\d+)\.md$")
CONTENT_TYPE_RE = re.compile(r"^content_type:\s*(\S+)\s*$", re.MULTILINE)
FULL_TEXT_ATTEMPTED_RE = re.compile(r"^full_text_attempted:\s*(\S+)\s*$", re.MULTILINE)
TABLE_HEADING_RE = re.compile(r"^## Table", re.MULTILINE)

# Matches PMCFullTextProvider._MIN_PMC_FULLTEXT_CHARS (etl/fulltext/pmc.py):
# a PMC XML/HTML response under ~1k chars is almost always a stub, and
# production rejects it and falls through -- so this census must too, or its
# "recoverable" count overstates what a real refetch would accept.
MIN_PMC_FULLTEXT_CHARS = 1000

# Non-retryable terminal statuses: a real API answer, not a transient hiccup.
IDCONV_TERMINAL_STATUSES = {"in_pmc", "not_in_pmc"}
RECOVERABILITY_TERMINAL_HAS_BODY = {"True", "False"}

MAX_RETRIES = 4


def _rate_limit_sleep(default: float) -> float:
    return 0.11 if os.environ.get("NCBI_API_KEY") else default


def _tool_email_params() -> str:
    key = os.environ.get("NCBI_API_KEY")
    # Matches upstream ReferenceValidationConfig's own default email domain
    # (linkml-reference-validator@example.com) -- a real NCBI contact address
    # would be better, but there is no dismech-wide convention for one yet,
    # and example.com at least behaves the way NCBI's own tooling expects.
    params = "tool=dismech-abstract-only-audit&email=dismech-audit@example.com"
    if key:
        params += f"&api_key={key}"
    return params


def iter_pmid_cache_files():
    for name in os.listdir(CACHE_DIR):
        m = PMID_RE.match(name)
        if m:
            yield m.group(1), os.path.join(CACHE_DIR, name)


def _read_frontmatter(path: str) -> str | None:
    """Return the properly-delimited YAML frontmatter text of a cache file.

    Uses the same delimiter-aware splitter as the rest of the codebase
    (``dismech.frontmatter.split_frontmatter``, also used by
    ``reference_cache_frontmatter.py``) rather than a fixed-size byte window.
    A window truncates: this repo's cache files routinely carry
    ``content_type`` past 4KB into the frontmatter (long author/keyword
    lists), so any fixed window silently drops those files from the count
    instead of raising an error -- the two window sizes this script used to
    use (2048 and 4096 bytes) disagreed with each other for exactly that
    reason. Cache files are small enough (622MB / 43k files, median ~3.5KB,
    p99 ~97KB) that reading them in full is not a performance concern.
    """
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            text = f.read()
    except OSError:
        return None
    split = split_frontmatter(text)
    return split.frontmatter if split is not None else None


def _content_type_of(path: str) -> str | None:
    frontmatter = _read_frontmatter(path)
    if frontmatter is None:
        return None
    m = CONTENT_TYPE_RE.search(frontmatter)
    return m.group(1) if m else None


def _full_text_attempted(path: str) -> bool:
    frontmatter = _read_frontmatter(path)
    if frontmatter is None:
        return False
    m = FULL_TEXT_ATTEMPTED_RE.search(frontmatter)
    return bool(m) and m.group(1).lower() == "true"


def enumerate_abstract_only() -> list[str]:
    """Offline. Returns bare PMIDs currently cached as abstract_only."""
    pmids = []
    for pmid, path in iter_pmid_cache_files():
        if _content_type_of(path) == "abstract_only":
            pmids.append(pmid)
    pmids.sort(key=int)
    return pmids


def phase_missing_tables() -> None:
    total = 0
    has_table = 0
    no_table: list[str] = []
    for pmid, path in iter_pmid_cache_files():
        if _content_type_of(path) != "full_text_xml":
            continue
        total += 1
        try:
            with open(path, encoding="utf-8", errors="replace") as f:
                content = f.read()
        except OSError:
            continue
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
        except urllib.error.HTTPError as exc:
            # A deterministic client error (400/403/404/...) will not become
            # succeed on retry; only 429 (rate limited) is worth the backoff.
            # Retrying the rest just costs ~15s of sleep per occurrence for
            # no benefit.
            if exc.code != 429:
                raise RuntimeError(f"GET failed with HTTP {exc.code}: {exc}") from exc
            last_exc = exc
            time.sleep(2**attempt)
        except (urllib.error.URLError, TimeoutError) as exc:
            last_exc = exc
            time.sleep(2**attempt)
    raise RuntimeError(f"GET failed after {MAX_RETRIES} retries: {last_exc}")


def _resume_terminal_rows(results_path: str, fieldnames: list[str], is_terminal) -> set[str]:
    """Read a resumable-phase CSV, keep only terminal rows, rewrite the file
    with just those (dropping any transient-error rows from a prior partial
    run so a retried PMID does not end up with two rows), and return the set
    of PMIDs those terminal rows cover.

    A single read; callers must not treat a PMID outside the returned set as
    done, so a transient failure from a previous run is retried rather than
    silently counted as an answer (#11938 review finding 4).
    """
    if not os.path.exists(results_path):
        return set()
    with open(results_path, newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is not None and list(reader.fieldnames) != fieldnames:
            raise SystemExit(
                f"{results_path} has columns {reader.fieldnames}, expected {fieldnames}. "
                "This looks like output from an earlier version of this script; resuming onto "
                "it would silently blank the new columns instead of actually reprocessing those "
                "rows. Move or delete it and rerun from scratch."
            )
        rows = [row for row in reader if is_terminal(row)]
    with open(results_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return {row["pmid"] for row in rows}


def phase_idconv(out_dir: str, batch_size: int, sleep_seconds: float) -> None:
    import json

    os.makedirs(out_dir, exist_ok=True)
    pmids_path = os.path.join(out_dir, "abstract_only_pmids.txt")
    results_path = os.path.join(out_dir, "idconv_results.csv")
    fieldnames = ["pmid", "pmcid", "doi", "status"]

    all_pmids = enumerate_abstract_only()
    with open(pmids_path, "w") as f:
        f.write("\n".join(all_pmids) + "\n")

    done = _resume_terminal_rows(results_path, fieldnames, lambda row: row["status"] in IDCONV_TERMINAL_STATUSES)
    todo = [p for p in all_pmids if p not in done]
    print(f"abstract_only PMIDs: {len(all_pmids)}; already resolved: {len(done)}; remaining: {len(todo)}")

    new_file = not os.path.exists(results_path)
    sleep_seconds = _rate_limit_sleep(sleep_seconds)
    with open(results_path, "a", newline="") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(fieldnames)

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


def _fetch_pmc_html(pmcid: str) -> str | None:
    """Mirror ``PMCFullTextProvider._fetch_pmc_html`` exactly: same URL, same
    ``div.article-body`` / ``div.tsec`` selectors, same paragraph join."""
    from bs4 import BeautifulSoup

    # idconv returns pmcid already "PMC"-prefixed (e.g. "PMC5593426"), unlike
    # production's Entrez.elink path, which returns a bare numeric id -- so
    # the shared PMC_ARTICLE_URL template (itself a correct copy of upstream's
    # "PMC{pmcid}" f-string) needs the prefix stripped first here, or the
    # formatted URL doubles it into ".../PMCPMC5593426/" and every fetch 404s.
    url = PMC_ARTICLE_URL.format(pmcid=pmcid.removeprefix("PMC"))
    try:
        html_bytes = _http_get(url)
    except RuntimeError:
        return None
    soup = BeautifulSoup(html_bytes, "html.parser")
    article_body = soup.find("div", class_="article-body") or soup.find("div", class_="tsec")
    if article_body is None:
        return None
    paragraphs = article_body.find_all("p")
    if not paragraphs:
        return None
    return "\n\n".join(p.get_text() for p in paragraphs)


def phase_recoverability(out_dir: str, sleep_seconds: float) -> None:
    from bs4 import BeautifulSoup
    from linkml_reference_validator.etl.extract.xml import XMLExtractor

    import dismech.patch_reference_validator as patch

    idconv_path = os.path.join(out_dir, "idconv_results.csv")
    results_path = os.path.join(out_dir, "recoverability_results.csv")
    if not os.path.exists(idconv_path):
        raise SystemExit(f"Run --phase idconv first; {idconv_path} does not exist.")

    candidates = []
    with open(idconv_path, newline="") as f:
        for row in csv.DictReader(f):
            if row["status"] == "in_pmc" and row["pmcid"]:
                candidates.append((row["pmid"], row["pmcid"]))

    recov_fieldnames = [
        "pmid",
        "pmcid",
        "has_body",
        "text_len",
        "used_html_fallback",
        "num_tables",
        "full_text_attempted",
        "reason",
    ]
    done = _resume_terminal_rows(
        results_path, recov_fieldnames, lambda row: row["has_body"] in RECOVERABILITY_TERMINAL_HAS_BODY
    )
    todo = [c for c in candidates if c[0] not in done]
    print(f"PMC-linked candidates: {len(candidates)}; already checked: {len(done)}; remaining: {len(todo)}")

    extractor = XMLExtractor()
    sleep_seconds = _rate_limit_sleep(sleep_seconds)

    def classify_xml(data: bytes):
        """Returns (body_text_or_None, num_tables, reason_if_not_recovered)."""
        text_data = data.decode("utf-8", errors="replace")
        if not text_data.strip() or "<article" not in text_data:
            return None, 0, "no_article_element"

        # content_type matches PMCFullTextProvider.locate's own call
        # (pmc.py:61). XMLExtractor.extract ignores it either way, but
        # passing it removes the one textual difference from the production
        # call.
        body_text = extractor.extract(data, content_type="application/xml")

        try:
            soup = BeautifulSoup(text_data, "xml")
        except Exception:
            return body_text, 0, "" if body_text else "soup_parse_error"

        tables_text = patch._jats_tables_as_text(soup)
        num_tables = tables_text.count("\n\n## ") + (1 if tables_text.startswith("## ") else 0)

        if body_text:
            return body_text, num_tables, ""
        if soup.find("body") is None:
            # The real, closed-tag form NCBI emits for a non-OA record:
            # <meta-name>pmc-prop-open-access</meta-name><meta-value>no</meta-value>
            not_oa_markers = (
                "does not allow downloading",
                "<meta-name>pmc-prop-open-access</meta-name><meta-value>no</meta-value>",
            )
            reason = "not_open_access" if any(m in text_data for m in not_oa_markers) else "no_body_element"
            return None, num_tables, reason
        return None, num_tables, "empty_body"

    new_file = not os.path.exists(results_path)
    with open(results_path, "a", newline="") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(recov_fieldnames)

        for i, (pmid, pmcid) in enumerate(todo, 1):
            cache_path = os.path.join(CACHE_DIR, f"PMID_{pmid}.md")
            attempted = _full_text_attempted(cache_path)
            url = f"{EFETCH_URL}?db=pmc&id={pmcid}&rettype=xml&{_tool_email_params()}"
            try:
                data = _http_get(url)
                body_text, num_tables, reason = classify_xml(data)
                used_html_fallback = False

                # Match PMCFullTextProvider.locate exactly: XML is accepted
                # only past the same length floor, and HTML is tried when XML
                # yields nothing (or too little), not only when it yields
                # literally nothing -- a 400-char XML stub still falls
                # through to HTML in production.
                if not body_text or len(body_text) <= MIN_PMC_FULLTEXT_CHARS:
                    html_text = _fetch_pmc_html(pmcid)
                    if html_text and len(html_text) > MIN_PMC_FULLTEXT_CHARS:
                        body_text = html_text
                        used_html_fallback = True
                        reason = ""
                        # num_tables came from parsing the XML's <table-wrap>
                        # elements; a real refetch that stores this HTML text
                        # instead would carry no JATS tables at all, so a
                        # stale XML-derived count here would overstate what
                        # was actually cached.
                        num_tables = 0
                    elif not body_text:
                        pass  # keep classify_xml's reason
                    else:
                        reason = reason or "below_min_chars"
                    time.sleep(sleep_seconds)

                has_body = bool(body_text) and len(body_text) > MIN_PMC_FULLTEXT_CHARS
                text_len = len(body_text) if body_text else 0
                if not has_body and not reason:
                    reason = "below_min_chars"
            except Exception as exc:
                writer.writerow([pmid, pmcid, "error", "", "", 0, attempted, str(exc)[:200]])
                f.flush()
                time.sleep(sleep_seconds)
                continue

            writer.writerow([pmid, pmcid, has_body, text_len, used_html_fallback, num_tables, attempted, reason])
            f.flush()
            if i % 200 == 0 or i == len(todo):
                print(f"  {i}/{len(todo)}")
            time.sleep(sleep_seconds)

    print(f"Wrote {results_path}")


def phase_summarize(out_dir: str) -> None:
    idconv_path = os.path.join(out_dir, "idconv_results.csv")
    recov_path = os.path.join(out_dir, "recoverability_results.csv")

    if not os.path.exists(idconv_path):
        print(f"{idconv_path} does not exist -- run --phase idconv (or --phase all) first.")
        return

    total_abstract_only = 0
    in_pmc = 0
    idconv_errors = 0
    with open(idconv_path, newline="") as f:
        for row in csv.DictReader(f):
            total_abstract_only += 1
            if row["status"] == "in_pmc":
                in_pmc += 1
            elif row["status"] not in IDCONV_TERMINAL_STATUSES:
                idconv_errors += 1

    if not os.path.exists(recov_path):
        print(f"abstract_only PMIDs censused: {total_abstract_only}")
        print(f"  with a PMC record: {in_pmc}")
        if idconv_errors:
            print(f"  WARNING: {idconv_errors} idconv rows are non-terminal errors, excluded above -- rerun --phase idconv to retry them")
        print(f"{recov_path} does not exist -- run --phase recoverability (or --phase all) next.")
        return

    checked = 0
    recoverable = 0
    with_tables = 0
    total_tables = 0
    attempted_recoverable = 0
    never_attempted_recoverable = 0
    via_html_fallback = 0
    recov_errors = 0
    reasons: dict[str, int] = {}
    with open(recov_path, newline="") as f:
        for row in csv.DictReader(f):
            if row["has_body"] not in RECOVERABILITY_TERMINAL_HAS_BODY:
                recov_errors += 1
                continue
            checked += 1
            if row["has_body"] == "True":
                recoverable += 1
                n = int(row["num_tables"] or 0)
                total_tables += n
                if n > 0:
                    with_tables += 1
                if row.get("full_text_attempted") == "True":
                    attempted_recoverable += 1
                else:
                    never_attempted_recoverable += 1
                if row.get("used_html_fallback") == "True":
                    via_html_fallback += 1
            else:
                reasons[row["reason"] or "(unknown)"] = reasons.get(row["reason"] or "(unknown)", 0) + 1

    print(f"abstract_only PMIDs censused: {total_abstract_only}")
    print(f"  with a PMC record (idconv):            {in_pmc}")
    if idconv_errors:
        print(f"  WARNING: {idconv_errors} idconv rows are non-terminal errors, excluded above -- rerun --phase idconv to retry them")
    print(f"  checked for true recoverability:        {checked}")
    if recov_errors:
        print(f"  WARNING: {recov_errors} recoverability rows are non-terminal errors, excluded above -- rerun --phase recoverability to retry them")
    print(f"  TRUE positives -- body now recoverable: {recoverable}")
    print(f"    previously attempted (full_text_attempted: true), stuck anyway: {attempted_recoverable}")
    print(f"    never attempted for full text at all:                          {never_attempted_recoverable}")
    print(f"    of those, carrying >=1 table:         {with_tables}  (tables found: {total_tables})")
    print(f"    recovered via HTML fallback (will cache full_text_html, no tables): {via_html_fallback}")
    print(f"    recovered via XML (will cache full_text_xml): {recoverable - via_html_fallback}")
    print("  non-recovery reasons among the rest:")
    for reason, count in sorted(reasons.items(), key=lambda x: -x[1]):
        print(f"    {reason}: {count}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--phase",
        choices=["idconv", "recoverability", "missing-tables", "summarize", "all"],
        default="missing-tables",
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
