#!/usr/bin/env python3
"""Check that a deep-research report's quotes are verbatim in their cited abstracts.

A provider report pairs a block quote with a PMID. This fetches each cited
abstract from NCBI eutils and checks the quoted string actually appears in it,
with whitespace normalised. A paraphrase presented as a quote, or a quote
attributed to the wrong PMID, is the failure mode this catches, and it is the one
that survived review in the first run of
templates/disease_alternative_models_research.md.

It is a pre-curation gate, not a substitute for `--validate-references`: it reads
only the abstract, so a quote taken from a full text is reported as NOT_IN_ABSTRACT
rather than as a failure.

`just validate-research-reference` asks the same question with more behind it --
it attempts full text and caches what it fetches in references_cache/, so it can
confirm a quote this script can only report as NOT_IN_ABSTRACT. Two reasons to
run this one anyway: it needs no cache and no full-text fetch, so it is fast
enough for the generate-read-regenerate loop, and it pairs each quote with the
PMID the *report* attributes it to, which is how a quote cited to the wrong paper
is caught. A quote moved to a neighbouring citation still validates as real text
by the other route. Both fold text identically, by design -- see `normalise`.

    just check-report-quotes research/Some_Entry-alternative-models-deep-research-openscientist.md
    just check-report-quotes <report> --strict    # exit 1 on an unattributable quote
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
import urllib.parse
import urllib.request

from linkml_reference_validator.validation.supporting_text_validator import (
    SupportingTextValidator,
)

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
# A quote line, then within the next few lines the PMID it is attributed to.
QUOTE = re.compile(r"^>\s*\*?\"(?P<quote>[^\"]{25,})\"", re.MULTILINE)
PMID = re.compile(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d+)")
# What `--strict` fails on. NOT_IN_ABSTRACT is not here: see the flag's help.
FAILING = ("NO_PMID", "PMID_UNRESOLVED")


def normalise(text: str) -> str:
    """The comparison form `just validate-research-reference` uses, plus Markdown.

    The folding is delegated to linkml-reference-validator's own normaliser,
    because that is what decides a quote matches there. A stricter form here
    would report NOT_IN_ABSTRACT for quotes that check accepts, and a curator
    reading two gates that disagree learns nothing from either.

    Only the Markdown is this script's own business: a block quote wraps across
    lines, each continuation carrying its own "> ", and those markers have to go
    before any folding, or every multi-line quote fails to match its source.
    """
    text = re.sub(r"\n\s*>\s*", " ", text)
    return SupportingTextValidator.normalize_text(text)


def fetch_abstracts(pmids: list[str]) -> dict[str, str]:
    """Return {pmid: normalised abstract text} in one request."""
    if not pmids:
        return {}
    url = f"{EUTILS}/efetch.fcgi?" + urllib.parse.urlencode(
        {"db": "pubmed", "id": ",".join(pmids), "rettype": "abstract", "retmode": "text"}
    )
    with urllib.request.urlopen(url, timeout=120) as response:
        blob = response.read().decode("utf-8", "replace")
    # efetch's text mode separates records by a blank line then "N. Journal...".
    records = re.split(r"\n(?=\d+\.\s)", blob)
    out: dict[str, str] = {}
    for record in records:
        found = re.search(r"PMID:\s*(\d+)", record)
        if found:
            out[found.group(1)] = normalise(record)
    return out


def pairs(text: str) -> list[tuple[str, str | None]]:
    """Extract (quote, pmid) pairs, taking the first PMID after each quote."""
    result: list[tuple[str, str | None]] = []
    for match in QUOTE.finditer(text):
        tail = text[match.end() : match.end() + 600]
        pmid = PMID.search(tail)
        result.append((normalise(match.group("quote")), pmid.group(1) if pmid else None))
    return result


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("report", type=pathlib.Path)
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    # NOT_IN_ABSTRACT is deliberately not a failure: a report may legitimately
    # quote a full text this script cannot read. NO_PMID and PMID_UNRESOLVED
    # never are legitimate -- a quote with no citation, or one citing a PMID
    # PubMed does not return, cannot be curated either way.
    ap.add_argument(
        "--strict",
        action="store_true",
        help="exit 1 if any quote is NO_PMID or PMID_UNRESOLVED",
    )
    args = ap.parse_args()

    if not args.report.is_file():
        print(f"No such report: {args.report}", file=sys.stderr)
        return 1

    found = pairs(args.report.read_text())
    abstracts = fetch_abstracts(sorted({p for _, p in found if p}))

    rows = []
    for quote, pmid in found:
        if not pmid:
            verdict = "NO_PMID"
        elif pmid not in abstracts:
            verdict = "PMID_UNRESOLVED"
        elif quote in abstracts[pmid]:
            verdict = "VERBATIM"
        else:
            verdict = "NOT_IN_ABSTRACT"
        rows.append({"pmid": pmid, "verdict": verdict, "quote": quote})

    unattributable = [r for r in rows if r["verdict"] in FAILING]
    status = 1 if args.strict and unattributable else 0

    if args.json:
        print(json.dumps(rows, indent=2))
        return status

    counts: dict[str, int] = {}
    for row in rows:
        counts[row["verdict"]] = counts.get(row["verdict"], 0) + 1
    print(f"{len(rows)} quotes checked against {len(abstracts)} abstracts.\n")
    for verdict, count in sorted(counts.items()):
        print(f"- {verdict}: {count}")

    problems = [r for r in rows if r["verdict"] != "VERBATIM"]
    if problems:
        print("\nNeeding a look (a full-text quote shows here too):")
        for row in problems:
            print(f"\n  [{row['verdict']}] PMID:{row['pmid']}")
            print(f"    {row['quote'][:220]}")

    if status:
        plural = "quote" if len(unattributable) == 1 else "quotes"
        print(f"\n--strict: {len(unattributable)} {plural} cannot be attributed to a readable PMID.")
    return status


if __name__ == "__main__":
    raise SystemExit(main())
