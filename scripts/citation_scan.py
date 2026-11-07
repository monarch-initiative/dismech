#!/usr/bin/env python3
"""Find new papers that cite the references a KB entry already relies on.

Sibling of ``literature_scan.py``. That scanner asks Europe PMC for recent
papers matching a keyword profile and then guesses which entry each one is
about from its title. This one runs the other way: it starts from every PMID
an entry cites and asks which papers indexed in the window cite them.

The signal is the overlap. A new paper citing one heavily cited review says
little; one citing four of an entry's thirty references is very likely about
that disease. Each overlapping reference is weighted down by how often it is
cited overall, so citing a 20-citation case series counts for more than citing
a 5,000-citation methods paper.

Steps, all deterministic:

1. Collect the PMIDs each entry cites (``literature_scan.collect_refs``).
2. Query Europe PMC in chunks of ``CITES:<pmid>_MED`` clauses, restricted to
   papers first *indexed* in the window. The index date, not the publication
   date, because citation links are often added after publication: a
   publication-date window misses those papers or sees them twice.
3. Fetch each candidate's reference list once and intersect it with every
   entry's references locally.
4. Weight each overlapping reference by its Europe PMC ``citedByCount``.
5. Drop candidates the entry already cites, and (PMID, entry) pairs a curator
   has already decided on, read from the GitHub issue ledger (``--ledger``).

The moving index-date window means a citing paper is normally considered once.
The ledger covers what the window cannot: the first backfill run, and an entry
gaining references so an old paper re-enters with a higher overlap.

Report-only. It writes a packet; nothing here edits ``kb/`` or opens issues.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import math
import re
import sys
import time
from collections.abc import Callable, Iterable
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import httpx

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import literature_scan

from dismech.yaml_io import safe_load

EUROPE_PMC_REST = "https://www.ebi.ac.uk/europepmc/webservices/rest"
SEARCH_POST_URL = f"{EUROPE_PMC_REST}/searchPOST"

# Europe PMC accepts 1,000 CITES clauses in one POST query; stay under it.
DEFAULT_CHUNK_SIZE = 500

# Publication types that are notices about another paper, not new findings.
EXCLUDED_PUB_TYPES = (
    "erratum",
    "retraction of publication",
    "retraction notice",
    "expression of concern",
)

LEDGER_MARKER_RE = re.compile(
    r"<!--\s*citation-scan\s+pmid=(?P<pmid>\d+)\s+entry=(?P<entry>\S+)"
    r"\s+overlap=(?P<overlap>\d+)\s*-->"
)
PMID_RE = re.compile(r"PMID:\s*(\d+)")
ENTRY_PATH_RE = re.compile(r"kb/disorders/[A-Za-z0-9_.\-]+\.yaml")

# A paper sharing one reference with an entry is mostly noise: the dry run's
# single-overlap hits included a picornavirus polymerase paper under ALS.
DEFAULT_MIN_OVERLAP = 2

# The score is a sum, so an entry citing 115 papers outscores one citing 10 on
# volume alone. Capping pairs per entry keeps small entries in the packet.
DEFAULT_MAX_PER_ENTRY = 3

BOOKSHELF_INDEXES = ("genereviews.csv", "statpearls.csv")

# A curator-rejected pair re-enters only if the paper now cites this many more
# of the entry's references than when it was rejected.
DEFAULT_RESURFACE_MARGIN = 2


@dataclass
class Entry:
    path: str
    name: str
    pmids: set[str]
    references: set[str]


@dataclass
class Candidate:
    pmid: str
    title: str = ""
    journal: str = ""
    publication_date: str = ""
    pub_type: str = ""
    doi: str = ""
    authors: str = ""
    abstract: str = ""
    references: set[str] = field(default_factory=set)

    @property
    def is_review(self) -> bool:
        return "review" in self.pub_type.lower()


@dataclass(frozen=True)
class LedgerDecision:
    number: int
    state: str
    state_reason: str
    pmid: str
    entry: str | None
    overlap: int | None


# --------------------------------------------------------------------------
# KB side


def load_entries(kb_dir: Path, only: Iterable[str] = ()) -> list[Entry]:
    """Every entry's cited PMIDs. ``only`` filters by file stem."""
    wanted = {name.removesuffix(".yaml") for name in only}
    entries: list[Entry] = []
    for path in sorted(kb_dir.glob("*.yaml")):
        if wanted and path.stem not in wanted:
            continue
        data = safe_load(path.read_text(encoding="utf-8")) or {}
        if not isinstance(data, dict):
            continue
        refs: set[str] = set()
        literature_scan.collect_refs(data, refs)
        pmids = {ref.split(":", 1)[1] for ref in refs if ref.startswith("PMID:")}
        entries.append(
            Entry(
                path=str(path),
                name=str(data.get("name") or path.stem.replace("_", " ")),
                pmids=pmids,
                references=refs,
            )
        )
    missing = wanted - {Path(entry.path).stem for entry in entries}
    if missing:
        raise SystemExit(f"no such entries in {kb_dir}: {', '.join(sorted(missing))}")
    return entries


def load_bookshelf_pmids(bookshelf_dir: Path) -> set[str]:
    """PMIDs of GeneReviews and StatPearls chapters.

    Europe PMC undercounts citations to Bookshelf chapters (it reports the
    GeneReviews Alkaptonuria chapter as cited once), so their counts would
    make them look like rare, highly informative references. Their weight is
    taken as unknown instead.
    """
    pmids: set[str] = set()
    for name in BOOKSHELF_INDEXES:
        path = bookshelf_dir / name
        if not path.exists():
            continue
        with path.open(encoding="utf-8") as handle:
            pmids.update(
                row["pmid"] for row in csv.DictReader(handle) if row.get("pmid")
            )
    return pmids


def cached_title(pmid: str, cache_dir: Path) -> str:
    path = cache_dir / f"PMID_{pmid}.md"
    if not path.exists():
        return ""
    for line in path.read_text(encoding="utf-8").splitlines()[:20]:
        if line.startswith("title:"):
            return line.split(":", 1)[1].strip().strip("'\"")
    return ""


# --------------------------------------------------------------------------
# Query construction


def chunked(items: list[str], size: int) -> Iterable[list[str]]:
    for start in range(0, len(items), size):
        yield items[start : start + size]


def build_cites_query(pmids: Iterable[str], date_from: str, date_to: str) -> str:
    clauses = " OR ".join(f"CITES:{pmid}_MED" for pmid in pmids)
    return f"({clauses}) AND SRC:MED AND FIRST_IDATE:[{date_from} TO {date_to}]"


def build_lookup_query(pmids: Iterable[str]) -> str:
    clauses = " OR ".join(f"EXT_ID:{pmid}" for pmid in pmids)
    return f"({clauses}) AND SRC:MED"


def is_notice(pub_type: str) -> bool:
    lowered = pub_type.lower()
    return any(term in lowered for term in EXCLUDED_PUB_TYPES)


# --------------------------------------------------------------------------
# Europe PMC client


class EuropePMC:
    """Thin client. Tests replace it with a stub exposing the same methods."""

    def __init__(self, timeout: float = 60.0, pause: float = 0.2) -> None:
        self.client = httpx.Client(timeout=timeout, follow_redirects=True)
        self.pause = pause
        self.requests = 0

    def _request(self, method: str, url: str, **kwargs: Any) -> dict[str, Any]:
        for attempt in range(4):
            try:
                response = self.client.request(method, url, **kwargs)
                self.requests += 1
                if response.status_code < 500:
                    response.raise_for_status()
                    time.sleep(self.pause)
                    return response.json()
            except httpx.TransportError:
                if attempt == 3:
                    raise
            time.sleep(2**attempt)
        response.raise_for_status()
        return response.json()

    def search(self, query: str, result_type: str = "lite") -> list[dict[str, Any]]:
        results: list[dict[str, Any]] = []
        cursor = "*"
        while True:
            payload = self._request(
                "POST",
                SEARCH_POST_URL,
                data={
                    "query": query,
                    "format": "json",
                    "pageSize": 1000,
                    "resultType": result_type,
                    "cursorMark": cursor,
                },
            )
            page = payload.get("resultList", {}).get("result", [])
            results.extend(page)
            next_cursor = payload.get("nextCursorMark")
            if not page or not next_cursor or next_cursor == cursor:
                return results
            cursor = next_cursor

    def references(self, pmid: str) -> set[str]:
        refs: set[str] = set()
        page = 1
        while True:
            payload = self._request(
                "GET",
                f"{EUROPE_PMC_REST}/MED/{pmid}/references",
                params={"format": "json", "pageSize": 1000, "page": page},
            )
            items = payload.get("referenceList", {}).get("reference", [])
            refs.update(
                str(item["id"])
                for item in items
                if item.get("source") == "MED" and item.get("id")
            )
            if len(items) < 1000:
                return refs
            page += 1


# --------------------------------------------------------------------------
# Scoring


def reference_weight(cited_by_count: int | None) -> float:
    """1 for an uncited reference, falling slowly as citations rise.

    ``1 / log2(2 + n)``: 10 citations -> 0.28, 100 -> 0.15, 5,000 -> 0.08.
    An unknown count is treated as moderately cited (0.15) rather than rare,
    so a lookup failure cannot inflate a score.
    """
    if cited_by_count is None:
        cited_by_count = 100
    return 1.0 / math.log2(2 + max(cited_by_count, 0))


def score_overlaps(
    candidates: dict[str, Candidate],
    entries: list[Entry],
    cited_by: dict[str, int],
    min_overlap: int = 1,
) -> list[dict[str, Any]]:
    """One row per (candidate, entry) pair sharing at least one reference."""
    rows: list[dict[str, Any]] = []
    for candidate in candidates.values():
        for entry in entries:
            overlap = sorted(candidate.references & entry.pmids, key=int)
            if len(overlap) < max(min_overlap, 1):
                continue
            if f"PMID:{candidate.pmid}" in entry.references:
                continue
            weights = {pmid: reference_weight(cited_by.get(pmid)) for pmid in overlap}
            rows.append(
                {
                    "pmid": candidate.pmid,
                    "entry": entry.path,
                    "disease_name": entry.name,
                    "overlap": len(overlap),
                    "entry_pmid_count": len(entry.pmids),
                    "score": round(sum(weights.values()), 3),
                    "is_review": candidate.is_review,
                    "overlap_refs": [
                        {
                            "pmid": pmid,
                            "cited_by": cited_by.get(pmid),
                            "weight": round(w, 3),
                        }
                        for pmid, w in weights.items()
                    ],
                }
            )
    rows.sort(
        key=lambda row: (-row["score"], -row["overlap"], row["entry"], row["pmid"])
    )
    return rows


# --------------------------------------------------------------------------
# Ledger: curator decisions recorded as GitHub issues


def parse_ledger(issues: list[dict[str, Any]]) -> list[LedgerDecision]:
    """Decisions from ``gh issue list --state all --json number,title,state,stateReason,body``.

    A citation-scan issue carries a hidden marker naming the pair and the
    overlap it was filed at. An older literature-scan issue has no marker, so
    every PMID it mentions counts, against the entry it names if exactly one,
    else against every entry.
    """
    decisions: list[LedgerDecision] = []
    for issue in issues:
        text = f"{issue.get('title') or ''}\n{issue.get('body') or ''}"
        # `gh issue list --json` spells it stateReason; the REST API state_reason.
        reason = issue.get("stateReason") or issue.get("state_reason") or ""
        common = {
            "number": int(issue.get("number") or 0),
            "state": str(issue.get("state") or "").upper(),
            "state_reason": str(reason).upper(),
        }
        markers = list(LEDGER_MARKER_RE.finditer(text))
        if markers:
            for marker in markers:
                decisions.append(
                    LedgerDecision(
                        pmid=marker["pmid"],
                        entry=marker["entry"],
                        overlap=int(marker["overlap"]),
                        **common,
                    )
                )
            continue
        paths = set(ENTRY_PATH_RE.findall(text))
        entry = paths.pop() if len(paths) == 1 else None
        for pmid in sorted(set(PMID_RE.findall(text))):
            decisions.append(
                LedgerDecision(pmid=pmid, entry=entry, overlap=None, **common)
            )
    return decisions


def cap_per_entry(
    rows: list[dict[str, Any]], max_per_entry: int
) -> list[dict[str, Any]]:
    """Keep each entry's best ``max_per_entry`` rows; ``rows`` is already ranked."""
    if max_per_entry <= 0:
        return rows
    taken: dict[str, int] = {}
    kept: list[dict[str, Any]] = []
    for row in rows:
        if taken.get(row["entry"], 0) < max_per_entry:
            taken[row["entry"]] = taken.get(row["entry"], 0) + 1
            kept.append(row)
    return kept


def ledger_verdict(
    row: dict[str, Any],
    decisions: list[LedgerDecision],
    resurface_margin: int = DEFAULT_RESURFACE_MARGIN,
) -> tuple[str, int | None]:
    """``("new", None)`` or the reason the pair is suppressed, with the issue.

    Any closed issue counts as decided, whatever its close reason: curators
    close scanner issues as completed or duplicate whether or not anything was
    added (none of the first 223 closed ones used not-planned), so the reason
    cannot separate a rejection from an addition. A paper that was added is
    dropped anyway, because the entry now cites it.
    """
    relevant = [
        decision
        for decision in decisions
        if decision.pmid == row["pmid"] and decision.entry in (None, row["entry"])
    ]
    for decision in sorted(relevant, key=lambda d: d.number, reverse=True):
        if decision.state == "OPEN":
            return "open_issue", decision.number
        if (
            decision.overlap is None
            or row["overlap"] < decision.overlap + resurface_margin
        ):
            return "closed_issue", decision.number
        return "resurfaced", decision.number
    return "new", None


# --------------------------------------------------------------------------
# Pipeline


def find_candidates(
    api: Any,
    entries: list[Entry],
    date_from: str,
    date_to: str,
    chunk_size: int,
    log: Callable[[str], None],
) -> dict[str, Candidate]:
    all_pmids = sorted(set().union(*(entry.pmids for entry in entries)), key=int)
    candidates: dict[str, Candidate] = {}
    chunks = list(chunked(all_pmids, chunk_size))
    for index, chunk in enumerate(chunks, start=1):
        for record in api.search(build_cites_query(chunk, date_from, date_to)):
            pmid = str(record.get("pmid") or record.get("id") or "")
            if not pmid.isdigit() or pmid in candidates:
                continue
            candidates[pmid] = Candidate(
                pmid=pmid,
                title=literature_scan.normalize_text(record.get("title")),
                journal=literature_scan.normalize_text(record.get("journalTitle")),
                publication_date=literature_scan.normalize_text(
                    record.get("firstPublicationDate")
                ),
                pub_type=literature_scan.normalize_text(record.get("pubType")),
                doi=literature_scan.normalize_text(record.get("doi")),
                authors=literature_scan.normalize_text(record.get("authorString")),
            )
        log(f"  query {index}/{len(chunks)}: {len(candidates)} candidates so far")
    return {pmid: c for pmid, c in candidates.items() if not is_notice(c.pub_type)}


def lookup_records(
    api: Any, pmids: Iterable[str], result_type: str
) -> dict[str, dict[str, Any]]:
    found: dict[str, dict[str, Any]] = {}
    for chunk in chunked(sorted(set(pmids), key=int), DEFAULT_CHUNK_SIZE):
        for record in api.search(build_lookup_query(chunk), result_type=result_type):
            pmid = str(record.get("pmid") or record.get("id") or "")
            if pmid:
                found[pmid] = record
    return found


def run_scan(
    api: Any,
    entries: list[Entry],
    *,
    date_from: str,
    date_to: str,
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    ledger: list[LedgerDecision] | None = None,
    resurface_margin: int = DEFAULT_RESURFACE_MARGIN,
    max_candidates: int = 50,
    min_overlap: int = DEFAULT_MIN_OVERLAP,
    max_per_entry: int = DEFAULT_MAX_PER_ENTRY,
    workers: int = 4,
    cache_dir: Path = Path("references_cache"),
    bookshelf_dir: Path = Path("cache/bookshelf"),
    reference_lists: dict[str, list[str]] | None = None,
    log: Callable[[str], None] = lambda _msg: None,
) -> dict[str, Any]:
    log(
        f"Searching for papers citing {sum(len(e.pmids) for e in entries)} entry references"
    )
    candidates = find_candidates(api, entries, date_from, date_to, chunk_size, log)

    known = reference_lists if reference_lists is not None else {}
    for pmid, refs in known.items():
        if pmid in candidates:
            candidates[pmid].references = set(refs)
    to_fetch = [pmid for pmid in candidates if pmid not in known]
    log(f"Fetching reference lists for {len(to_fetch)} of {len(candidates)} candidates")
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(api.references, pmid): pmid for pmid in to_fetch}
        for index, future in enumerate(as_completed(futures), start=1):
            candidates[futures[future]].references = future.result()
            known[futures[future]] = sorted(candidates[futures[future]].references)
            if index % 200 == 0:
                log(f"  {index}/{len(to_fetch)}")

    overlapping = set().union(
        *(candidate.references for candidate in candidates.values()),
    ) & set().union(*(entry.pmids for entry in entries))
    log(f"Looking up citation counts for {len(overlapping)} overlapping references")
    cited_by = {
        pmid: int(record.get("citedByCount") or 0)
        for pmid, record in lookup_records(api, overlapping, "lite").items()
    }
    for pmid in load_bookshelf_pmids(bookshelf_dir):
        cited_by.pop(pmid, None)

    all_rows = score_overlaps(candidates, entries, cited_by)
    overlap_histogram: dict[str, int] = {}
    for row in all_rows:
        bucket = str(min(row["overlap"], 5)) + ("+" if row["overlap"] >= 5 else "")
        overlap_histogram[bucket] = overlap_histogram.get(bucket, 0) + 1
    rows = [row for row in all_rows if row["overlap"] >= min_overlap]
    decisions = ledger or []
    suppressed: dict[str, int] = {}
    kept: list[dict[str, Any]] = []
    for row in rows:
        verdict, issue = ledger_verdict(row, decisions, resurface_margin)
        row["ledger"] = verdict
        row["ledger_issue"] = issue
        if verdict in ("new", "resurfaced"):
            kept.append(row)
        else:
            suppressed[verdict] = suppressed.get(verdict, 0) + 1

    shown = cap_per_entry(kept, max_per_entry)[:max_candidates]
    abstracts = lookup_records(api, {row["pmid"] for row in shown}, "core")
    for row in shown:
        candidate = candidates[row["pmid"]]
        row.update(
            title=candidate.title,
            pub_type=candidate.pub_type,
            journal=candidate.journal,
            publication_date=candidate.publication_date,
            doi=candidate.doi,
            authors=candidate.authors,
            abstract=literature_scan.normalize_text(
                abstracts.get(row["pmid"], {}).get("abstractText")
            ),
            pubmed_url=f"https://pubmed.ncbi.nlm.nih.gov/{row['pmid']}/",
            europe_pmc_url=f"https://europepmc.org/article/MED/{row['pmid']}",
            marker=(
                f"<!-- citation-scan pmid={row['pmid']} entry={row['entry']} "
                f"overlap={row['overlap']} -->"
            ),
        )
        for ref in row["overlap_refs"]:
            ref["title"] = cached_title(ref["pmid"], cache_dir)

    return {
        "generated_at": dt.datetime.now(dt.UTC).isoformat(),
        "date_from": date_from,
        "date_to": date_to,
        "entry_count": len(entries),
        "entry_pmid_count": len(set().union(*(e.pmids for e in entries))),
        "candidate_count": len(candidates),
        "pair_count": len(all_rows),
        "overlap_histogram": dict(sorted(overlap_histogram.items())),
        "min_overlap": min_overlap,
        "max_per_entry": max_per_entry,
        "above_min_overlap": len(rows),
        "suppressed": suppressed,
        "reportable_count": len(kept),
        "record_count": len(shown),
        "europe_pmc_requests": getattr(api, "requests", None),
        "records": shown,
    }


# --------------------------------------------------------------------------
# Output


def render_markdown(packet: dict[str, Any]) -> str:
    suppressed = ", ".join(f"{k}: {v}" for k, v in sorted(packet["suppressed"].items()))
    lines = [
        "# Citation Scan Packet",
        "",
        "New papers citing references that KB entries already rely on.",
        "",
        f"- Generated: {packet['generated_at']}",
        f"- Index-date window: {packet['date_from']} to {packet['date_to']}",
        (
            f"- Entries scanned: {packet['entry_count']} "
            f"({packet['entry_pmid_count']} distinct PMIDs)"
        ),
        f"- Citing papers found: {packet['candidate_count']}",
        f"- (paper, entry) pairs: {packet['pair_count']}; by shared references: "
        + ", ".join(f"{k}: {v}" for k, v in packet["overlap_histogram"].items()),
        f"- Pairs sharing at least {packet['min_overlap']}: {packet['above_min_overlap']}",
        f"- Suppressed by the issue ledger: {suppressed or 'none'}",
        (
            f"- Reportable pairs: {packet['reportable_count']}; "
            f"shown: {packet['record_count']} (at most {packet['max_per_entry']} per entry)"
        ),
        "",
        "Score: sum over shared references of 1/log2(2 + times that reference is",
        "cited). Citing a rarely cited paper counts for more than citing a classic.",
        "",
        "## Candidates",
        "",
    ]
    for index, row in enumerate(packet["records"], start=1):
        lines.extend(
            [
                f"### {index}. {row['title'] or 'Untitled'}",
                "",
                f"- Entry: `{row['entry']}` ({row['disease_name']})",
                f"- Shares {row['overlap']} of the entry's {row['entry_pmid_count']} "
                f"PMID references; score {row['score']}"
                + (
                    " (resurfaced after an earlier rejection)"
                    if row["ledger"] == "resurfaced"
                    else ""
                ),
                f"- PMID: {row['pmid']}",
                f"- Publication type: {row['pub_type']}"
                + (" (review)" if row["is_review"] else ""),
                f"- DOI: {row['doi']}",
                f"- Journal: {row['journal']}",
                f"- Publication date: {row['publication_date']}",
                f"- Authors: {row['authors']}",
                f"- PubMed: {row['pubmed_url']}",
                f"- Europe PMC: {row['europe_pmc_url']}",
                "",
                "Shared references:",
                "",
            ]
        )
        for ref in row["overlap_refs"]:
            cited = "unknown" if ref["cited_by"] is None else ref["cited_by"]
            lines.append(
                f"- PMID:{ref['pmid']} (cited {cited} times, weight {ref['weight']})"
                + (f" — {ref['title']}" if ref.get("title") else "")
            )
        lines.extend(
            [
                "",
                "Abstract:",
                "",
                literature_scan.markdown_blockquote(row["abstract"]),
                "",
                f"Ledger marker: `{row['marker']}`",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("entries", nargs="*", help="Entry file stems; default all.")
    parser.add_argument("--days", type=int, default=7)
    parser.add_argument("--date-from", default="")
    parser.add_argument("--date-to", default="")
    parser.add_argument("--kb-dir", type=Path, default=Path("kb/disorders"))
    parser.add_argument("--chunk-size", type=int, default=DEFAULT_CHUNK_SIZE)
    parser.add_argument("--max-candidates", type=int, default=50)
    parser.add_argument(
        "--workers", type=int, default=4, help="Parallel reference-list fetches."
    )
    parser.add_argument("--min-overlap", type=int, default=DEFAULT_MIN_OVERLAP)
    parser.add_argument(
        "--max-per-entry",
        type=int,
        default=DEFAULT_MAX_PER_ENTRY,
        help="Pairs shown per entry; 0 for no cap.",
    )
    parser.add_argument(
        "--reference-cache",
        type=Path,
        help="JSON of candidate reference lists, read and rewritten, to re-score without refetching.",
    )
    parser.add_argument(
        "--ledger",
        type=Path,
        help="JSON from `gh issue list --state all --json number,title,state,stateReason,body`.",
    )
    parser.add_argument(
        "--resurface-margin", type=int, default=DEFAULT_RESURFACE_MARGIN
    )
    parser.add_argument(
        "--output-json",
        type=Path,
        default=Path("output/citation_scan/citation_scan.json"),
    )
    parser.add_argument(
        "--output-md", type=Path, default=Path("output/citation_scan/citation_scan.md")
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if bool(args.date_from) != bool(args.date_to):
        print("--date-from and --date-to must be provided together", file=sys.stderr)
        return 2
    if args.date_from:
        date_from, date_to = args.date_from, args.date_to
    else:
        date_from, date_to = literature_scan.default_date_range(args.days)

    entries = [
        entry for entry in load_entries(args.kb_dir, args.entries) if entry.pmids
    ]
    ledger = None
    if args.ledger:
        ledger = parse_ledger(json.loads(args.ledger.read_text(encoding="utf-8")))

    reference_lists: dict[str, list[str]] = {}
    if args.reference_cache and args.reference_cache.exists():
        reference_lists = json.loads(args.reference_cache.read_text(encoding="utf-8"))

    def log(message: str) -> None:
        print(message, file=sys.stderr, flush=True)

    packet = run_scan(
        EuropePMC(),
        entries,
        date_from=date_from,
        date_to=date_to,
        chunk_size=args.chunk_size,
        ledger=ledger,
        resurface_margin=args.resurface_margin,
        max_candidates=args.max_candidates,
        workers=args.workers,
        min_overlap=args.min_overlap,
        max_per_entry=args.max_per_entry,
        reference_lists=reference_lists,
        log=log,
    )
    if args.reference_cache:
        args.reference_cache.parent.mkdir(parents=True, exist_ok=True)
        args.reference_cache.write_text(json.dumps(reference_lists, sort_keys=True))
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_md.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    args.output_md.write_text(render_markdown(packet), encoding="utf-8")
    print(
        f"{packet['candidate_count']} citing papers, {packet['pair_count']} pairs, "
        f"{packet['reportable_count']} reportable; wrote {args.output_md}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
