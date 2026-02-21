#!/usr/bin/env python3
"""QC checks for deep-research provider and citation coverage."""

from __future__ import annotations

import argparse
import csv
import glob
import os
import re
import sys
import time
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Set

import yaml


RESEARCH_FILE_RE = re.compile(
    r"^(?P<name>.+)-deep-research-(?P<provider>[^.]+)\.md(?:\.citations\.md)?$"
)
PMID_RE = re.compile(r"\bPMID\s*[:#]?\s*(\d{4,9})\b", re.IGNORECASE)
PUBMED_URL_RE = re.compile(
    r"https?://(?:www\.)?pubmed\.ncbi\.nlm\.nih\.gov/(\d{4,9})(?:/|\b)", re.IGNORECASE
)
DOI_URL_RE = re.compile(r"https?://(?:dx\.)?doi\.org/([^\s\],)]+)", re.IGNORECASE)
DOI_PREFIX_RE = re.compile(r"\bDOI\s*:\s*([^\s\],)]+)", re.IGNORECASE)
DOI_TOKEN_RE = re.compile(r"\b10\.\d{4,9}/[^\s\],;]+", re.IGNORECASE)

HOLDER_NAME = "Deep research literature mapping"


@dataclass
class DisorderQCRow:
    disorder: str
    has_research: bool
    providers: str
    target_provider_count: int
    second_provider_ok: bool
    cited_ref_count: int
    existing_ref_count: int
    missing_ref_count: int
    unresolved_cache_count: int
    missing_found_in_ref_count: int
    missing_found_in_link_count: int
    holder_bucket_present: bool


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Quality checks for deep-research coverage and citation-to-reference "
            "coverage in disorder YAML files."
        )
    )
    parser.add_argument("--kb-dir", default="kb/disorders")
    parser.add_argument("--research-dir", default="research")
    parser.add_argument("--references-cache-dir", default="references_cache")
    parser.add_argument("--output-dir", default="output")
    parser.add_argument(
        "--target-providers",
        nargs="+",
        default=["falcon", "openai", "cyberian", "cyberian-codex"],
    )
    parser.add_argument("--only", nargs="+", default=None)
    parser.add_argument(
        "--fail-on-second-provider",
        action="store_true",
        help="Exit non-zero if a disorder has research but <2 target providers.",
    )
    parser.add_argument(
        "--fail-on-missing-reference",
        action="store_true",
        help="Exit non-zero if deep-research citations are missing from YAML references/evidence.",
    )
    parser.add_argument(
        "--fail-on-unresolved-cache",
        action="store_true",
        help="Exit non-zero if missing refs are not available in references cache.",
    )
    parser.add_argument(
        "--fail-on-holder-bucket",
        action="store_true",
        help="Exit non-zero if legacy holder bucket is found in pathophysiology.",
    )
    parser.add_argument(
        "--fail-on-missing-found-in",
        action="store_true",
        help="Exit non-zero if cited refs do not include expected references[].found_in links.",
    )
    return parser.parse_args()


def normalize_doi(doi: str) -> str:
    value = doi.strip()
    value = value.split("?", 1)[0].split("#", 1)[0]
    value = value.rstrip(".,;)]")
    value = value.lstrip("(")
    for suffix in ("/full", "/pdf", "/abstract", "/epub"):
        if value.lower().endswith(suffix):
            value = value[: -len(suffix)]
            break
    return value


def valid_doi(doi: str) -> bool:
    if not doi.startswith("10.") or "/" not in doi:
        return False
    if doi.endswith(("/", ".")):
        return False
    if any(ch in doi for ch in ("|", "\\", "<", ">", "{", "}", '"', "'")):
        return False
    if doi.count("(") != doi.count(")"):
        return False
    if "%" in doi:
        return False
    return re.fullmatch(r"10\.\d{4,9}/\S+", doi) is not None


def canonical_ref(raw: str) -> str | None:
    ref = raw.strip()
    if ref.upper().startswith("PMID:"):
        digits = re.sub(r"\D", "", ref.split(":", 1)[1])
        return f"PMID:{digits}" if digits else None
    if ref.upper().startswith("DOI:"):
        doi = normalize_doi(ref.split(":", 1)[1]).lower()
        return f"DOI:{doi}" if valid_doi(doi) else None
    if re.fullmatch(r"\d{4,9}", ref):
        return f"PMID:{ref}"
    if ref.lower().startswith("10."):
        doi = normalize_doi(ref).lower()
        return f"DOI:{doi}" if valid_doi(doi) else None
    return None


def extract_refs(text: str) -> Set[str]:
    refs: Set[str] = set()

    def add(raw: str) -> None:
        canon = canonical_ref(raw)
        if canon:
            refs.add(canon)

    for pmid in PMID_RE.findall(text):
        add(f"PMID:{pmid}")
    for pmid in PUBMED_URL_RE.findall(text):
        add(f"PMID:{pmid}")
    for doi in DOI_URL_RE.findall(text):
        add(f"DOI:{doi}")
    for doi in DOI_PREFIX_RE.findall(text):
        add(f"DOI:{doi}")
    for doi in DOI_TOKEN_RE.findall(text):
        add(f"DOI:{doi}")
    return refs


def cache_path_for_ref(reference: str, references_cache_dir: str) -> Path:
    safe = reference.replace(":", "_").replace("/", "_")
    return Path(references_cache_dir) / f"{safe}.md"


def research_provider_map(research_dir: str) -> Dict[str, Set[str]]:
    providers: Dict[str, Set[str]] = defaultdict(set)
    for path in glob.glob(os.path.join(research_dir, "*-deep-research-*.md*")):
        filename = os.path.basename(path)
        if filename.startswith("com_"):
            continue
        match = RESEARCH_FILE_RE.match(filename)
        if not match:
            continue
        providers[match.group("name")].add(match.group("provider"))
    return providers


def citation_ref_map(research_dir: str) -> Dict[str, Dict[str, Set[str]]]:
    refs: Dict[str, Dict[str, Set[str]]] = defaultdict(lambda: defaultdict(set))
    pattern = os.path.join(research_dir, "*-deep-research-*.md.citations.md")
    for path in glob.glob(pattern):
        filename = os.path.basename(path)
        if filename.startswith("com_"):
            continue
        match = RESEARCH_FILE_RE.match(filename)
        if not match:
            continue
        disorder = match.group("name")
        research_file = filename.removesuffix('.citations.md')
        text = Path(path).read_text(encoding="utf-8", errors="ignore")
        for ref in extract_refs(text):
            refs[disorder][ref].add(research_file)
    return refs


def collect_existing_refs(node: Any, out: Set[str]) -> None:
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "reference" and isinstance(value, str):
                canon = canonical_ref(value)
                if canon:
                    out.add(canon)
            else:
                collect_existing_refs(value, out)
    elif isinstance(node, list):
        for item in node:
            collect_existing_refs(item, out)


def collect_top_reference_found_in(data: Mapping[str, Any]) -> Dict[str, Set[str]]:
    out: Dict[str, Set[str]] = {}
    references = data.get("references")
    if not isinstance(references, list):
        return out

    for item in references:
        if not isinstance(item, Mapping):
            continue
        ref_value = item.get("reference")
        if not isinstance(ref_value, str):
            continue
        canon = canonical_ref(ref_value)
        if not canon:
            continue
        raw_found_in = item.get("found_in")
        found_in_set: Set[str] = set()
        if isinstance(raw_found_in, str):
            val = raw_found_in.strip()
            if val:
                found_in_set.add(val)
        elif isinstance(raw_found_in, list):
            for entry in raw_found_in:
                if isinstance(entry, str):
                    val = entry.strip()
                    if val:
                        found_in_set.add(val)
        out[canon] = found_in_set
    return out


def has_holder_bucket(data: Mapping[str, Any]) -> bool:
    pathophys = data.get("pathophysiology")
    if not isinstance(pathophys, list):
        return False
    for item in pathophys:
        if isinstance(item, Mapping) and item.get("name") == HOLDER_NAME:
            return True
    return False


def write_report(rows: List[DisorderQCRow], output_dir: str) -> Path:
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    ts = time.strftime("%Y%m%d-%H%M%S")
    path = Path(output_dir) / f"qc_deep_research_{ts}.tsv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(
            [
                "disorder",
                "has_research",
                "providers",
                "target_provider_count",
                "second_provider_ok",
                "cited_ref_count",
                "existing_ref_count",
                "missing_ref_count",
                "unresolved_cache_count",
                "missing_found_in_ref_count",
                "missing_found_in_link_count",
                "holder_bucket_present",
            ]
        )
        for r in rows:
            writer.writerow(
                [
                    r.disorder,
                    str(r.has_research),
                    r.providers,
                    r.target_provider_count,
                    str(r.second_provider_ok),
                    r.cited_ref_count,
                    r.existing_ref_count,
                    r.missing_ref_count,
                    r.unresolved_cache_count,
                    r.missing_found_in_ref_count,
                    r.missing_found_in_link_count,
                    str(r.holder_bucket_present),
                ]
            )
    return path


def main() -> int:
    args = parse_args()
    only = set(args.only or [])
    target_provider_set = set(args.target_providers)

    disorder_paths = sorted(
        Path(path)
        for path in glob.glob(os.path.join(args.kb_dir, "*.yaml"))
        if not path.endswith(".history.yaml")
    )
    if only:
        disorder_paths = [p for p in disorder_paths if p.stem in only]

    provider_map = research_provider_map(args.research_dir)
    citation_map = citation_ref_map(args.research_dir)

    rows: List[DisorderQCRow] = []

    for path in disorder_paths:
        disorder = path.stem
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        existing_refs: Set[str] = set()
        collect_existing_refs(data, existing_refs)

        providers = provider_map.get(disorder, set())
        target_count = len(providers.intersection(target_provider_set))
        has_research = len(providers) > 0
        second_ok = (not has_research) or (
            len(providers) >= 2 and target_count >= 1
        )

        cited_ref_to_files = citation_map.get(disorder, {})
        cited_refs = set(cited_ref_to_files.keys())
        missing_refs = cited_refs.difference(existing_refs)
        unresolved = [
            ref
            for ref in missing_refs
            if not cache_path_for_ref(ref, args.references_cache_dir).exists()
        ]
        top_ref_found_in = collect_top_reference_found_in(data)
        missing_found_in_refs = 0
        missing_found_in_links = 0
        for ref, expected_files in cited_ref_to_files.items():
            existing_files = top_ref_found_in.get(ref, set())
            missing_files = expected_files.difference(existing_files)
            if missing_files:
                missing_found_in_refs += 1
                missing_found_in_links += len(missing_files)

        row = DisorderQCRow(
            disorder=disorder,
            has_research=has_research,
            providers=",".join(sorted(providers)),
            target_provider_count=target_count,
            second_provider_ok=second_ok,
            cited_ref_count=len(cited_refs),
            existing_ref_count=len(existing_refs),
            missing_ref_count=len(missing_refs),
            unresolved_cache_count=len(unresolved),
            missing_found_in_ref_count=missing_found_in_refs,
            missing_found_in_link_count=missing_found_in_links,
            holder_bucket_present=has_holder_bucket(data),
        )
        rows.append(row)

    with_research = [r for r in rows if r.has_research]
    bad_second = [r for r in with_research if not r.second_provider_ok]
    bad_missing = [r for r in rows if r.missing_ref_count > 0]
    bad_unresolved = [r for r in rows if r.unresolved_cache_count > 0]
    bad_found_in = [r for r in rows if r.missing_found_in_ref_count > 0]
    bad_holder = [r for r in rows if r.holder_bucket_present]

    total_cited = sum(r.cited_ref_count for r in rows)
    total_missing = sum(r.missing_ref_count for r in rows)
    total_unresolved = sum(r.unresolved_cache_count for r in rows)
    total_missing_found_in_refs = sum(r.missing_found_in_ref_count for r in rows)
    total_missing_found_in_links = sum(r.missing_found_in_link_count for r in rows)

    print("Deep Research QC Summary")
    print(f"- disorders_total: {len(rows)}")
    print(f"- disorders_with_research: {len(with_research)}")
    print(
        "- disorders_meeting_second_provider: "
        f"{len(with_research) - len(bad_second)}/{len(with_research)}"
    )
    print(f"- disorders_with_missing_refs: {len(bad_missing)}")
    print(f"- total_cited_refs: {total_cited}")
    print(f"- total_missing_refs: {total_missing}")
    print(f"- total_unresolved_cache_refs: {total_unresolved}")
    print(f"- disorders_with_missing_found_in: {len(bad_found_in)}")
    print(f"- total_missing_found_in_refs: {total_missing_found_in_refs}")
    print(f"- total_missing_found_in_links: {total_missing_found_in_links}")
    print(f"- disorders_with_holder_bucket: {len(bad_holder)}")

    if bad_missing:
        top = sorted(bad_missing, key=lambda r: (-r.missing_ref_count, r.disorder))[:15]
        print("- top_missing_ref_disorders:")
        for r in top:
            print(f"  - {r.disorder}: missing={r.missing_ref_count}")

    report_path = write_report(rows, args.output_dir)
    print(f"- report: {report_path}")

    failures: List[str] = []
    if args.fail_on_second_provider and bad_second:
        failures.append(f"{len(bad_second)} disorder(s) missing second provider")
    if args.fail_on_missing_reference and bad_missing:
        failures.append(f"{len(bad_missing)} disorder(s) missing cited references")
    if args.fail_on_unresolved_cache and bad_unresolved:
        failures.append(
            f"{len(bad_unresolved)} disorder(s) have unresolved uncached references"
        )
    if args.fail_on_missing_found_in and bad_found_in:
        failures.append(
            f"{len(bad_found_in)} disorder(s) have missing references[].found_in links"
        )
    if args.fail_on_holder_bucket and bad_holder:
        failures.append(f"{len(bad_holder)} disorder(s) still contain holder bucket")

    if failures:
        print("FAIL:")
        for f in failures:
            print(f"- {f}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
