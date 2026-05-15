#!/usr/bin/env python3
"""Generate deterministic weekly literature-scan packets from Europe PMC."""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import httpx
import yaml


EUROPE_PMC_SEARCH_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"

PROFILE_QUERIES = {
    "mechanisms": (
        "(("
        + " OR ".join(
            [
                "TITLE:pathogenesis",
                "TITLE:pathophysiology",
                'TITLE:"molecular mechanism"',
                "TITLE:mechanism",
            ]
        )
        + ") AND (TITLE_ABS:disease OR TITLE_ABS:syndrome OR TITLE_ABS:disorder))"
        + " OR "
        + "(("
        + " OR ".join(
            [
                "TITLE:variant",
                "TITLE:mutation",
                "TITLE:genetic",
                "TITLE:gene",
            ]
        )
        + ") AND (TITLE_ABS:disease OR TITLE_ABS:syndrome OR TITLE_ABS:disorder))"
        + " OR "
        + "(("
        + " OR ".join(
            [
                "TITLE:treatment",
                "TITLE:therapy",
                "TITLE:therapeutic",
                "TITLE:trial",
            ]
        )
        + ") AND (TITLE_ABS:disease OR TITLE_ABS:syndrome OR TITLE_ABS:disorder))"
    )
}

EXCLUDED_TITLE_TERMS = (
    "TITLE:corrigendum",
    "TITLE:erratum",
    "TITLE:retraction",
    "TITLE:withdrawn",
)

GENERIC_DISEASE_TERMS = {
    "autosomal dominant",
    "autosomal recessive",
    "cancer",
    "carcinoma",
    "classic",
    "disease",
    "disorder",
    "genetic disease",
    "leukemia",
    "lung cancer",
    "missense",
    "moderate",
    "neonatal",
    "severe",
    "syndrome",
    "systemic",
    "tumor",
}


@dataclass(frozen=True)
class DiseaseTerm:
    normalized: str
    label: str
    path: str
    disease_name: str
    kind: str


@dataclass
class Publication:
    id: str
    source: str
    pmid: str
    doi: str
    title: str
    journal: str
    publication_date: str
    authors: str
    abstract: str
    europe_pmc_url: str
    pubmed_url: str


def normalize_text(value: Any) -> str:
    text = html.unescape(str(value or ""))
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def normalize_for_match(value: str) -> str:
    value = normalize_text(value).lower()
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


def canonical_ref(raw: str) -> str | None:
    value = raw.strip()
    if not value:
        return None
    if value.upper().startswith("PMID:"):
        digits = re.sub(r"\D", "", value.split(":", 1)[1])
        return f"PMID:{digits}" if digits else None
    if value.upper().startswith("DOI:"):
        doi = value.split(":", 1)[1].strip().lower()
        return f"DOI:{doi}" if doi else None
    return None


def build_query(date_from: str, date_to: str, profile: str = "mechanisms") -> str:
    if profile not in PROFILE_QUERIES:
        profiles = ", ".join(sorted(PROFILE_QUERIES))
        raise ValueError(f"unknown profile {profile!r}; choose one of: {profiles}")
    profile_query = PROFILE_QUERIES[profile]
    excluded = " OR ".join(EXCLUDED_TITLE_TERMS)
    return (
        f"SRC:MED AND FIRST_PDATE:[{date_from} TO {date_to}] "
        f"AND ({profile_query}) NOT ({excluded})"
    )


def default_date_range(days: int) -> tuple[str, str]:
    today = dt.datetime.now(dt.UTC).date()
    return (today - dt.timedelta(days=days)).isoformat(), today.isoformat()


def fetch_europe_pmc(
    query: str,
    *,
    max_records: int,
    page_size: int,
    timeout: float,
) -> tuple[int, list[dict[str, Any]]]:
    records: list[dict[str, Any]] = []
    hit_count = 0
    page = 1
    with httpx.Client(timeout=timeout, follow_redirects=True) as client:
        while len(records) < max_records:
            current_page_size = min(page_size, max_records - len(records))
            response = client.get(
                EUROPE_PMC_SEARCH_URL,
                params={
                    "query": query,
                    "format": "json",
                    "pageSize": current_page_size,
                    "page": page,
                    "resultType": "core",
                },
            )
            response.raise_for_status()
            payload = response.json()
            if page == 1:
                hit_count = int(payload.get("hitCount") or 0)
            page_records = payload.get("resultList", {}).get("result", [])
            if not page_records:
                break
            records.extend(page_records)
            if len(page_records) < current_page_size:
                break
            page += 1
    return hit_count, records


def collect_refs(node: Any, out: set[str]) -> None:
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "reference" and isinstance(value, str):
                ref = canonical_ref(value)
                if ref:
                    out.add(ref)
            else:
                collect_refs(value, out)
    elif isinstance(node, list):
        for item in node:
            collect_refs(item, out)


def iter_term_values(data: dict[str, Any], path: Path) -> Iterable[tuple[str, str]]:
    name = data.get("name")
    if isinstance(name, str):
        yield name, "name"

    yield path.stem.replace("_", " "), "filename"

    synonyms = data.get("synonyms")
    if isinstance(synonyms, list):
        for synonym in synonyms:
            if isinstance(synonym, str):
                yield synonym, "synonym"

    subtypes = data.get("has_subtypes")
    if isinstance(subtypes, list):
        for subtype in subtypes:
            if not isinstance(subtype, dict):
                continue
            for key in ("name", "display_name"):
                value = subtype.get(key)
                if isinstance(value, str):
                    yield value, f"subtype.{key}"


def keep_disease_term(term: str, kind: str) -> bool:
    normalized = normalize_for_match(term)
    if not normalized or normalized in GENERIC_DISEASE_TERMS:
        return False
    if kind.startswith("subtype.") and len(normalized.split()) < 2:
        return False
    return len(normalized) >= 6


def load_disease_terms(kb_dir: Path) -> tuple[list[DiseaseTerm], dict[str, set[str]]]:
    terms: list[DiseaseTerm] = []
    references_by_path: dict[str, set[str]] = {}
    for path in sorted(kb_dir.glob("*.yaml")):
        if path.name.endswith(".history.yaml"):
            continue
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        if not isinstance(data, dict):
            continue
        path_string = str(path)
        disease_name = str(data.get("name") or path.stem.replace("_", " "))
        refs: set[str] = set()
        collect_refs(data, refs)
        references_by_path[path_string] = refs
        seen: set[str] = set()
        for label, kind in iter_term_values(data, path):
            normalized = normalize_for_match(label)
            if normalized in seen or not keep_disease_term(label, kind):
                continue
            seen.add(normalized)
            terms.append(
                DiseaseTerm(
                    normalized=normalized,
                    label=label,
                    path=path_string,
                    disease_name=disease_name,
                    kind=kind,
                )
            )
    terms.sort(key=lambda term: len(term.normalized), reverse=True)
    return terms, references_by_path


def publication_from_record(record: dict[str, Any]) -> Publication:
    source = normalize_text(record.get("source"))
    record_id = normalize_text(record.get("id"))
    pmid = normalize_text(record.get("pmid"))
    if not pmid and source == "MED" and re.fullmatch(r"\d+", record_id):
        pmid = record_id
    europe_pmc_url = f"https://europepmc.org/article/{source}/{record_id}"
    pubmed_url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else ""
    return Publication(
        id=record_id,
        source=source,
        pmid=pmid,
        doi=normalize_text(record.get("doi")),
        title=normalize_text(record.get("title")),
        journal=normalize_text(record.get("journalTitle")),
        publication_date=normalize_text(record.get("firstPublicationDate")),
        authors=normalize_text(record.get("authorString")),
        abstract=normalize_text(record.get("abstractText")),
        europe_pmc_url=europe_pmc_url,
        pubmed_url=pubmed_url,
    )


def match_publication(
    publication: Publication,
    terms: list[DiseaseTerm],
    references_by_path: dict[str, set[str]],
    max_matches: int,
) -> list[dict[str, Any]]:
    normalized_title = normalize_for_match(publication.title)
    normalized_abstract = normalize_for_match(publication.abstract)
    padded_title = f" {normalized_title} "
    padded_all = f" {normalized_title} {normalized_abstract} "
    matches_by_path: dict[str, dict[str, Any]] = {}

    for term in terms:
        term_pattern = f" {term.normalized} "
        in_title = term_pattern in padded_title
        in_text = term_pattern in padded_all
        if not in_text:
            continue
        score = (4 if in_title else 1) + min(len(term.normalized) / 30, 3)
        existing = matches_by_path.get(term.path)
        if existing is None:
            existing_refs = references_by_path.get(term.path, set())
            references = set()
            if publication.pmid:
                references.add(f"PMID:{publication.pmid}")
            if publication.doi:
                references.add(f"DOI:{publication.doi.lower()}")
            matches_by_path[term.path] = {
                "path": term.path,
                "disease_name": term.disease_name,
                "score": round(score, 3),
                "matched_terms": [
                    {
                        "label": term.label,
                        "kind": term.kind,
                        "in_title": in_title,
                    }
                ],
                "already_cited": bool(references & existing_refs),
            }
            continue

        existing["score"] = round(max(float(existing["score"]), score), 3)
        existing["matched_terms"].append(
            {"label": term.label, "kind": term.kind, "in_title": in_title}
        )

    matches = sorted(
        matches_by_path.values(),
        key=lambda item: (-float(item["score"]), item["path"]),
    )
    return matches[:max_matches]


def build_packet(
    records: list[dict[str, Any]],
    *,
    hit_count: int,
    query: str,
    date_from: str,
    date_to: str,
    profile: str,
    kb_dir: Path,
    max_matches: int,
) -> dict[str, Any]:
    terms, references_by_path = load_disease_terms(kb_dir)
    publications = [publication_from_record(record) for record in records]
    seen_keys: set[str] = set()
    packet_records: list[dict[str, Any]] = []
    for publication in publications:
        key = publication.pmid or f"{publication.source}:{publication.id}"
        if key in seen_keys:
            continue
        seen_keys.add(key)
        item = publication.__dict__.copy()
        item["candidate_existing_diseases"] = match_publication(
            publication,
            terms,
            references_by_path,
            max_matches,
        )
        packet_records.append(item)

    return {
        "generated_at": dt.datetime.now(dt.UTC).isoformat(),
        "profile": profile,
        "date_from": date_from,
        "date_to": date_to,
        "query": query,
        "hit_count": hit_count,
        "record_count": len(packet_records),
        "records": packet_records,
    }


def markdown_blockquote(text: str) -> str:
    if not text:
        return "> No abstract available."
    return "\n".join(f"> {line}" if line else ">" for line in text.splitlines())


def render_markdown(packet: dict[str, Any]) -> str:
    lines = [
        "# Weekly Literature Scan Packet",
        "",
        f"- Generated: {packet['generated_at']}",
        f"- Profile: {packet['profile']}",
        f"- Date range: {packet['date_from']} to {packet['date_to']}",
        f"- Europe PMC hit count: {packet['hit_count']}",
        f"- Records in packet: {packet['record_count']}",
        "",
        "## Query",
        "",
        "```text",
        packet["query"],
        "```",
        "",
        "## Records",
        "",
    ]

    for index, record in enumerate(packet["records"], start=1):
        pmid = record.get("pmid") or "no PMID"
        title = record.get("title") or "Untitled"
        lines.extend(
            [
                f"### {index}. {title}",
                "",
                f"- PMID: {pmid}",
                f"- DOI: {record.get('doi') or ''}",
                f"- Journal: {record.get('journal') or ''}",
                f"- Publication date: {record.get('publication_date') or ''}",
                f"- Authors: {record.get('authors') or ''}",
                f"- Europe PMC: {record.get('europe_pmc_url') or ''}",
                f"- PubMed: {record.get('pubmed_url') or ''}",
                "",
                "Abstract:",
                "",
                markdown_blockquote(record.get("abstract") or ""),
                "",
                "Candidate existing disease files:",
                "",
            ]
        )
        matches = record.get("candidate_existing_diseases") or []
        if not matches:
            lines.append("- None found deterministically.")
        for match in matches:
            terms = ", ".join(
                item["label"] for item in match.get("matched_terms", [])[:4]
            )
            cited = "yes" if match.get("already_cited") else "no"
            title_match = (
                "yes"
                if any(item.get("in_title") for item in match.get("matched_terms", []))
                else "no"
            )
            lines.append(
                f"- `{match['path']}` ({match['disease_name']}); "
                f"matched terms: {terms}; title match: {title_match}; "
                f"score: {match['score']}; already cited: {cited}"
            )
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def write_outputs(packet: dict[str, Any], output_json: Path, output_md: Path) -> None:
    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    output_md.write_text(render_markdown(packet), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a deterministic Europe PMC literature-scan packet."
    )
    parser.add_argument(
        "--profile", default="mechanisms", choices=sorted(PROFILE_QUERIES)
    )
    parser.add_argument("--days", type=int, default=7)
    parser.add_argument("--date-from", default="")
    parser.add_argument("--date-to", default="")
    parser.add_argument("--max-records", type=int, default=100)
    parser.add_argument("--page-size", type=int, default=100)
    parser.add_argument("--max-matches", type=int, default=5)
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--kb-dir", type=Path, default=Path("kb/disorders"))
    parser.add_argument(
        "--output-json",
        type=Path,
        default=Path("output/literature_scan/literature_scan.json"),
    )
    parser.add_argument(
        "--output-md",
        type=Path,
        default=Path("output/literature_scan/literature_scan.md"),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.date_from and args.date_to:
        date_from, date_to = args.date_from, args.date_to
    elif args.date_from or args.date_to:
        print("--date-from and --date-to must be provided together", file=sys.stderr)
        return 2
    else:
        date_from, date_to = default_date_range(args.days)

    query = build_query(date_from, date_to, args.profile)
    hit_count, records = fetch_europe_pmc(
        query,
        max_records=args.max_records,
        page_size=args.page_size,
        timeout=args.timeout,
    )
    packet = build_packet(
        records,
        hit_count=hit_count,
        query=query,
        date_from=date_from,
        date_to=date_to,
        profile=args.profile,
        kb_dir=args.kb_dir,
        max_matches=args.max_matches,
    )
    write_outputs(packet, args.output_json, args.output_md)
    print(
        f"Wrote {packet['record_count']} records from {hit_count} Europe PMC hits "
        f"to {args.output_json} and {args.output_md}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
