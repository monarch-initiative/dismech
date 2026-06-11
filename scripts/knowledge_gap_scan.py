#!/usr/bin/env python3
"""Generate deterministic mechanistic knowledge-gap scan packets from Europe PMC."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import literature_scan  # noqa: E402


GAP_SIGNAL_GROUPS = {
    "explicit_gap": (
        "knowledge gap",
        "knowledge gaps",
        "research gap",
        "research gaps",
        "unanswered question",
        "unanswered questions",
        "unresolved question",
        "unresolved questions",
    ),
    "unclear_unknown": (
        "poorly understood",
        "remains unclear",
        "remain unclear",
        "remained unclear",
        "largely unknown",
        "is unknown",
        "are unknown",
        "remain unknown",
        "remains unknown",
        "elusive",
        "not fully understood",
        "incompletely understood",
    ),
    "future_work": (
        "future studies",
        "future research",
        "future investigations",
        "further studies",
        "further research",
        "further investigations",
        "additional studies",
        "additional research",
    ),
    "controversy_conflict": (
        "controversial",
        "controversy",
        "conflicting evidence",
        "conflicting results",
        "conflicting findings",
        "contradictory evidence",
        "inconsistent evidence",
        "inconsistent results",
        "inconsistent findings",
    ),
    "limitations_barriers": (
        "limited evidence",
        "limited data",
        "limitations",
        "barriers",
        "challenges",
        "hindered by",
        "lack of evidence",
        "lack of data",
        "absence of evidence",
        "absence of data",
    ),
}

MECHANISM_CONTEXT_TERMS = (
    "pathogenesis",
    "pathophysiology",
    "mechanism",
    "mechanisms",
    "molecular mechanism",
    "disease mechanism",
    "etiology",
    "causal",
    "causality",
    "biomarker",
    "therapeutic target",
    "treatment response",
    "drug resistance",
)

DISEASE_CONTEXT_TERMS = (
    "disease",
    "diseases",
    "disorder",
    "disorders",
    "syndrome",
    "syndromes",
    "cancer",
    "tumor",
    "infection",
    "pathology",
)

EXCLUDED_TITLE_TERMS = (
    "TITLE:corrigendum",
    "TITLE:erratum",
    "TITLE:retraction",
    "TITLE:withdrawn",
)

ABBREVIATION_SENTINEL = {
    "H.": "H<PERIOD>",
    "e.g.": "e<PERIOD>g<PERIOD>",
    "i.e.": "i<PERIOD>e<PERIOD>",
    "vs.": "vs<PERIOD>",
    "Dr.": "Dr<PERIOD>",
    "Fig.": "Fig<PERIOD>",
}


def _field_or_terms(terms: tuple[str, ...], field: str = "TITLE_ABS") -> str:
    parts = []
    for term in terms:
        if " " in term or "-" in term:
            parts.append(f'{field}:"{term}"')
        else:
            parts.append(f"{field}:{term}")
    return "(" + " OR ".join(parts) + ")"


def build_query(date_from: str, date_to: str) -> str:
    signal_query = (
        "("
        + " OR ".join(
            _field_or_terms(tuple(terms)) for terms in GAP_SIGNAL_GROUPS.values()
        )
        + ")"
    )
    mechanism_query = _field_or_terms(MECHANISM_CONTEXT_TERMS)
    disease_query = _field_or_terms(DISEASE_CONTEXT_TERMS)
    excluded = " OR ".join(EXCLUDED_TITLE_TERMS)
    return (
        f"SRC:MED AND FIRST_PDATE:[{date_from} TO {date_to}] "
        f"AND ({signal_query}) "
        f"AND ({mechanism_query}) "
        f"AND ({disease_query}) "
        f"NOT ({excluded})"
    )


def default_date_range(days: int) -> tuple[str, str]:
    return literature_scan.default_date_range(days)


def fetch_europe_pmc(
    query: str,
    *,
    max_records: int,
    page_size: int,
    timeout: float,
) -> tuple[int, list[dict[str, Any]]]:
    return literature_scan.fetch_europe_pmc(
        query,
        max_records=max_records,
        page_size=page_size,
        timeout=timeout,
    )


def _restore_abbreviations(text: str) -> str:
    for original, sentinel in ABBREVIATION_SENTINEL.items():
        text = text.replace(sentinel, original)
    return text


def split_sentences(text: str) -> list[str]:
    normalized = literature_scan.normalize_text(text)
    if not normalized:
        return []
    for original, sentinel in ABBREVIATION_SENTINEL.items():
        normalized = normalized.replace(original, sentinel)
    return [
        _restore_abbreviations(part).strip()
        for part in re.split(r"(?<=[.!?])\s+", normalized)
        if part.strip()
    ]


def signal_categories(sentence: str) -> list[str]:
    normalized = sentence.casefold()
    categories = []
    for category, terms in GAP_SIGNAL_GROUPS.items():
        if any(term.casefold() in normalized for term in terms):
            categories.append(category)
    return categories


def extract_gap_signals(text: str, max_signals: int = 8) -> list[dict[str, Any]]:
    signals: list[dict[str, Any]] = []
    seen: set[str] = set()
    for sentence in split_sentences(text):
        categories = signal_categories(sentence)
        if not categories:
            continue
        key = literature_scan.normalize_for_match(sentence)
        if key in seen:
            continue
        seen.add(key)
        signals.append(
            {
                "categories": categories,
                "sentence": sentence,
            }
        )
        if len(signals) >= max_signals:
            break
    return signals


def signal_score(signals: list[dict[str, Any]]) -> int:
    weights = {
        "explicit_gap": 5,
        "unclear_unknown": 3,
        "controversy_conflict": 3,
        "future_work": 2,
        "limitations_barriers": 1,
    }
    score = 0
    for signal in signals:
        for category in signal.get("categories", []):
            score += weights.get(str(category), 0)
    return score


def build_packet(
    records: list[dict[str, Any]],
    *,
    hit_count: int,
    query: str,
    date_from: str,
    date_to: str,
    kb_dir: Path,
    max_matches: int,
    max_signals: int,
) -> dict[str, Any]:
    terms, references_by_path = literature_scan.load_disease_terms(kb_dir)
    publications = [
        literature_scan.publication_from_record(record) for record in records
    ]
    seen_keys: set[str] = set()
    packet_records: list[dict[str, Any]] = []

    for publication in publications:
        key = publication.pmid or f"{publication.source}:{publication.id}"
        if key in seen_keys:
            continue
        seen_keys.add(key)

        signals = extract_gap_signals(publication.abstract, max_signals=max_signals)
        item = publication.__dict__.copy()
        item["gap_signal_score"] = signal_score(signals)
        item["gap_signal_sentences"] = signals
        item["candidate_existing_diseases"] = literature_scan.match_publication(
            publication,
            terms,
            references_by_path,
            max_matches,
        )
        packet_records.append(item)

    packet_records.sort(
        key=lambda record: (
            -int(record.get("gap_signal_score") or 0),
            not bool(record.get("candidate_existing_diseases")),
            record.get("publication_date") or "",
            record.get("title") or "",
        )
    )

    return {
        "generated_at": dt.datetime.now(dt.UTC).isoformat(),
        "profile": "mechanistic_knowledge_gaps",
        "date_from": date_from,
        "date_to": date_to,
        "query": query,
        "hit_count": hit_count,
        "record_count": len(packet_records),
        "records": packet_records,
    }


def render_markdown(packet: dict[str, Any]) -> str:
    lines = [
        "# Mechanistic Knowledge-Gap Scan Packet",
        "",
        f"- Generated: {packet['generated_at']}",
        f"- Profile: {packet['profile']}",
        f"- Date range: {packet['date_from']} to {packet['date_to']}",
        f"- Europe PMC hit count: {packet['hit_count']}",
        f"- Records in packet: {packet['record_count']}",
        "",
        "## Scope",
        "",
        "This packet is a deterministic high-recall lead generator for mechanistic",
        "knowledge-gap handoff issues. It does not curate disease YAML files and it",
        "does not validate evidence snippets.",
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
                f"- Gap signal score: {record.get('gap_signal_score') or 0}",
                "",
                "Gap signal sentences:",
                "",
            ]
        )
        signals = record.get("gap_signal_sentences") or []
        if not signals:
            lines.append("- None found in the abstract after normalization.")
        for signal in signals:
            categories = ", ".join(signal.get("categories") or [])
            sentence = signal.get("sentence") or ""
            lines.append(f"- [{categories}] {sentence}")

        lines.extend(
            [
                "",
                "Abstract:",
                "",
                literature_scan.markdown_blockquote(record.get("abstract") or ""),
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
        description="Generate a deterministic mechanistic knowledge-gap scan packet."
    )
    parser.add_argument("--days", type=int, default=7)
    parser.add_argument("--date-from", default="")
    parser.add_argument("--date-to", default="")
    parser.add_argument("--max-records", type=int, default=200)
    parser.add_argument("--page-size", type=int, default=100)
    parser.add_argument("--max-matches", type=int, default=5)
    parser.add_argument("--max-signals", type=int, default=8)
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--kb-dir", type=Path, default=Path("kb/disorders"))
    parser.add_argument(
        "--output-json",
        type=Path,
        default=Path("output/knowledge_gap_scan/knowledge_gap_scan.json"),
    )
    parser.add_argument(
        "--output-md",
        type=Path,
        default=Path("output/knowledge_gap_scan/knowledge_gap_scan.md"),
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

    query = build_query(date_from, date_to)
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
        kb_dir=args.kb_dir,
        max_matches=args.max_matches,
        max_signals=args.max_signals,
    )
    write_outputs(packet, args.output_json, args.output_md)
    print(
        f"Wrote {packet['record_count']} records from {hit_count} Europe PMC hits "
        f"to {args.output_json} and {args.output_md}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
