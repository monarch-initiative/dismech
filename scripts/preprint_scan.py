#!/usr/bin/env python3
"""Generate deterministic weekly preprint-scan packets from Europe PMC.

Sibling of ``literature_scan.py`` / ``knowledge_gap_scan.py``. The difference is
the source: this scans Europe PMC ``SRC:PPR`` (preprints: bioRxiv / medRxiv /
Research Square / openRxiv) instead of ``SRC:MED`` (PubMed/MEDLINE), which the
other scanners restrict to and which excludes all preprints.

Why ``SRC:PPR`` and not the PubMed ``"preprint"[Publication Type]`` route: since
``linkml-reference-validator`` >= 0.2.1rc2 a preprint is a first-class reference
(``PPR:<pprid>``). ``just fetch-reference PPR:<id>`` resolves it gracefully -- the
full-text body when one is reachable (Europe PMC ``fulltextRepo`` PDF, or the
preprint-server HTML), otherwise the abstract -- and always produces a
snippet-validatable cache file. So a ``SRC:PPR`` candidate is directly citable, and
this scanner reuses the existing ``literature_scan`` Europe PMC machinery wholesale.

The query is intentionally NOT restricted to ``HAS_FT:Y``: Europe PMC's full-text
ingestion lags publication by months, so a full-text-only filter returns ~0 hits
for a weekly window. We surface fresh preprints and let the validator fetch full
text when available; for many recent leads only the abstract is retrievable at
scan time (full openRxiv full text is a later/S3-TDM concern, see
``research/preprint_fulltext_routes.md``).

Like its siblings this emits a deterministic packet only; it does not curate
disease YAML files and does not validate evidence snippets. Preprints are NOT
peer-reviewed, so downstream handoff issues are tagged accordingly and a preprint
must not become the sole support for a mechanism claim.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import literature_scan  # noqa: E402


def build_query(date_from: str, date_to: str, profile: str = "mechanisms") -> str:
    """Europe PMC query for recent preprints in the date window.

    Reuses the ``literature_scan`` mechanisms profile but swaps the source from
    ``SRC:MED`` to ``SRC:PPR``. No ``HAS_FT:Y`` filter (see module docstring:
    full-text ingestion lags, so it would empty a weekly window).

        >>> q = build_query("2026-01-01", "2026-01-08")
        >>> q.startswith("SRC:PPR AND FIRST_PDATE:[2026-01-01 TO 2026-01-08]")
        True
        >>> "HAS_FT" in q
        False
    """
    if profile not in literature_scan.PROFILE_QUERIES:
        profiles = ", ".join(sorted(literature_scan.PROFILE_QUERIES))
        raise ValueError(f"unknown profile {profile!r}; choose one of: {profiles}")
    profile_query = literature_scan.PROFILE_QUERIES[profile]
    excluded = " OR ".join(literature_scan.EXCLUDED_TITLE_TERMS)
    return (
        f"SRC:PPR AND FIRST_PDATE:[{date_from} TO {date_to}] "
        f"AND ({profile_query}) NOT ({excluded})"
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


def _suggested_reference(publication: literature_scan.Publication) -> str:
    """The reference id a curator should cite for this preprint.

    Preprints carry a Europe PMC ``SRC:PPR`` id (``PPRxxxxxxx``); that ``PPR:``
    form is what ``linkml-reference-validator`` resolves to full text.

    Note the intentional doubled ``PPR``: the ``PPR:`` prefix is the reference
    namespace and ``publication.id`` is the raw Europe PMC record id, which itself
    starts with ``PPR`` -- so e.g. record ``PPR1253390`` -> ``PPR:PPR1253390``.
    """
    return f"PPR:{publication.id}"


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
    terms, references_by_path = literature_scan.load_disease_terms(kb_dir)
    publications = [
        literature_scan.publication_from_record(record) for record in records
    ]
    seen_keys: set[str] = set()
    packet_records: list[dict[str, Any]] = []

    for publication in publications:
        # Every candidate is handed off as a `PPR:<id>` reference (built from the
        # Europe PMC SRC:PPR id), so a record without an id can't be cited — skip
        # it rather than emit a broken `PPR:` reference. SRC:PPR records always
        # carry an id; this is defensive. Dedupe on that id.
        key = publication.id
        if not key or key in seen_keys:
            continue
        seen_keys.add(key)

        ppr_reference = _suggested_reference(publication)
        matches = literature_scan.match_publication(
            publication,
            terms,
            references_by_path,
            max_matches,
        )
        # match_publication only knows PMID/DOI; also honour a PPR citation when
        # deciding whether the matched disease file already cites this preprint.
        for match in matches:
            existing_refs = references_by_path.get(match["path"], set())
            if ppr_reference in existing_refs:
                match["already_cited"] = True

        item = publication.__dict__.copy()
        item["ppr_id"] = publication.id
        item["suggested_reference"] = ppr_reference
        item["is_preprint"] = True
        item["candidate_existing_diseases"] = matches
        packet_records.append(item)

    packet_records.sort(
        key=lambda record: (
            not bool(record.get("candidate_existing_diseases")),
            record.get("publication_date") or "",
            record.get("title") or "",
        )
    )

    return {
        "generated_at": dt.datetime.now(dt.UTC).isoformat(),
        "profile": profile,
        "source": "preprints",
        "date_from": date_from,
        "date_to": date_to,
        "query": query,
        "hit_count": hit_count,
        "record_count": len(packet_records),
        "records": packet_records,
    }


def render_markdown(packet: dict[str, Any]) -> str:
    lines = [
        "# Weekly Preprint Scan Packet",
        "",
        f"- Generated: {packet['generated_at']}",
        f"- Profile: {packet['profile']}",
        "- Source: Europe PMC preprints (SRC:PPR)",
        f"- Date range: {packet['date_from']} to {packet['date_to']}",
        f"- Europe PMC hit count: {packet['hit_count']}",
        f"- Records in packet: {packet['record_count']}",
        "",
        "## Scope",
        "",
        "This packet is a deterministic high-recall lead generator for preprint",
        "handoff issues. It does not curate disease YAML files and it does not",
        "validate evidence snippets.",
        "",
        "Preprints are NOT peer-reviewed. Cite a candidate with its `PPR:` id",
        "(`just fetch-reference PPR:<id>` retrieves full text when available, else",
        "the abstract). A preprint must not be the sole support for a mechanism",
        "claim; prefer the peer-reviewed version when one exists.",
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
        title = record.get("title") or "Untitled"
        lines.extend(
            [
                f"### {index}. {title}",
                "",
                f"- Preprint ID: {record.get('ppr_id') or ''}",
                f"- Suggested reference: `{record.get('suggested_reference') or ''}`",
                f"- DOI: {record.get('doi') or ''}",
                f"- Server/date: {record.get('journal') or ''} {record.get('publication_date') or ''}".rstrip(),
                f"- Authors: {record.get('authors') or ''}",
                f"- Europe PMC: {record.get('europe_pmc_url') or ''}",
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
        description="Generate a deterministic Europe PMC preprint-scan packet."
    )
    parser.add_argument(
        "--profile", default="mechanisms", choices=sorted(literature_scan.PROFILE_QUERIES)
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
        default=Path("output/preprint_scan/preprint_scan.json"),
    )
    parser.add_argument(
        "--output-md",
        type=Path,
        default=Path("output/preprint_scan/preprint_scan.md"),
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
        f"Wrote {packet['record_count']} records from {hit_count} Europe PMC "
        f"preprint hits to {args.output_json} and {args.output_md}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
