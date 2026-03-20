#!/usr/bin/env python3
"""Backfill disorder evidence from deep-research citation files."""

from __future__ import annotations

import argparse
import csv
import glob
import os
import re
import subprocess
import time
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Set, Tuple

import yaml
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap, CommentedSeq


CITATION_FILE_RE = re.compile(r"^(?P<name>.+)-deep-research-[^.]+\.md\.citations\.md$")
PMID_RE = re.compile(r"\bPMID\s*[:#]?\s*(\d{4,9})\b", re.IGNORECASE)
PUBMED_URL_RE = re.compile(
    r"https?://(?:www\.)?pubmed\.ncbi\.nlm\.nih\.gov/(\d{4,9})(?:/|\b)", re.IGNORECASE
)
DOI_URL_RE = re.compile(r"https?://(?:dx\.)?doi\.org/([^\s\],)]+)", re.IGNORECASE)
DOI_PREFIX_RE = re.compile(r"\bDOI\s*:\s*([^\s\],)]+)", re.IGNORECASE)
DOI_TOKEN_RE = re.compile(r"\b10\.\d{4,9}/[^\s\],;]+", re.IGNORECASE)

HOLDER_NAME = "Deep research literature mapping"


@dataclass
class DisorderResult:
    disorder: str
    cited_refs: int
    existing_refs: int
    missing_refs: int
    added_refs: int
    unresolved_refs: int
    changed: bool


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Parse deep-research citation files and backfill missing references "
            "into disorder evidence blocks."
        )
    )
    parser.add_argument("--kb-dir", default="kb/disorders")
    parser.add_argument("--research-dir", default="research")
    parser.add_argument("--references-cache-dir", default="references_cache")
    parser.add_argument("--output-dir", default="output")
    parser.add_argument(
        "--max-disorders",
        type=int,
        default=None,
        help="Optional cap on disorders to process.",
    )
    parser.add_argument(
        "--only",
        nargs="+",
        default=None,
        help="Only process these disorder file stems.",
    )
    parser.add_argument(
        "--max-new-refs-per-disorder",
        type=int,
        default=None,
        help="Optional cap on new references added per disorder.",
    )
    parser.add_argument(
        "--fetch-missing-cache",
        action="store_true",
        help="Call `just fetch-reference` when a cited ID is not cached.",
    )
    parser.add_argument(
        "--fetch-timeout-seconds",
        type=int,
        default=45,
        help="Timeout for each fetch-reference call.",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write changes to files. Without this flag, run as dry-run.",
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


def canonical_ref(reference: str) -> str | None:
    ref = reference.strip()
    if ref.upper().startswith("PMID:"):
        digits = re.sub(r"\D", "", ref.split(":", 1)[1])
        return f"PMID:{digits}"
    if ref.upper().startswith("DOI:"):
        doi = normalize_doi(ref.split(":", 1)[1]).lower()
        if not valid_doi(doi):
            return None
        return f"DOI:{doi}"
    if re.fullmatch(r"\d{4,9}", ref):
        return f"PMID:{ref}"
    if ref.lower().startswith("10."):
        doi = normalize_doi(ref).lower()
        if not valid_doi(doi):
            return None
        return f"DOI:{doi}"
    return None


def valid_doi(doi: str) -> bool:
    if not doi:
        return False
    if not doi.startswith("10."):
        return False
    if "/" not in doi:
        return False
    if doi.endswith(("/", ".")):
        return False
    if any(ch in doi for ch in ("|", "\\", "<", ">", "{", "}", '"', "'")):
        return False
    if doi.count("(") != doi.count(")"):
        return False
    if "%" in doi:
        return False
    # Minimal structural check after normalization.
    return re.fullmatch(r"10\.\d{4,9}/\S+", doi) is not None


def extract_refs(text: str) -> Set[str]:
    refs: Set[str] = set()

    def add_ref(raw: str) -> None:
        value = canonical_ref(raw)
        if value and (value.startswith("PMID:") or value.startswith("DOI:")):
            refs.add(value)

    for pmid in PMID_RE.findall(text):
        add_ref(f"PMID:{pmid}")

    for pmid in PUBMED_URL_RE.findall(text):
        add_ref(f"PMID:{pmid}")

    for doi in DOI_URL_RE.findall(text):
        add_ref(f"DOI:{doi}")

    for doi in DOI_PREFIX_RE.findall(text):
        add_ref(f"DOI:{doi}")

    for doi in DOI_TOKEN_RE.findall(text):
        add_ref(f"DOI:{doi}")

    return refs


def citations_by_disorder(research_dir: str) -> Dict[str, Dict[str, Set[str]]]:
    by_disorder: Dict[str, Dict[str, Set[str]]] = defaultdict(lambda: defaultdict(set))
    for path in glob.glob(
        os.path.join(research_dir, "*-deep-research-*.md.citations.md")
    ):
        filename = os.path.basename(path)
        if filename.startswith("com_"):
            continue
        match = CITATION_FILE_RE.match(filename)
        if not match:
            continue
        disorder = match.group("name")
        research_file = filename.removesuffix(".citations.md")
        text = Path(path).read_text(encoding="utf-8", errors="ignore")
        refs = extract_refs(text)
        for ref in refs:
            by_disorder[disorder][ref].add(research_file)
    return by_disorder


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


def cache_path_for_ref(reference: str, references_cache_dir: str) -> Path:
    safe = reference.replace(":", "_").replace("/", "_")
    return Path(references_cache_dir) / f"{safe}.md"


def parse_cache_title(cache_path: Path) -> str | None:
    if not cache_path.exists():
        return None

    text = cache_path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    if len(lines) >= 3 and lines[0].strip() == "---":
        end_idx = None
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                end_idx = i
                break
        if end_idx is not None:
            frontmatter = "\n".join(lines[1:end_idx])
            try:
                meta = yaml.safe_load(frontmatter) or {}
                title = meta.get("title")
                if isinstance(title, str) and title.strip():
                    return title.strip()
            except Exception:
                pass

    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            if title:
                return title

    return None


def fetch_reference(reference: str, timeout_seconds: int) -> bool:
    cmd = ["just", "fetch-reference", reference]
    try:
        result = subprocess.run(
            cmd,
            check=False,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
        )
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        return False


def ensure_references_list(data: MutableMapping[str, Any]) -> CommentedSeq:
    refs = data.get("references")
    if refs is None:
        refs = CommentedSeq()
        data["references"] = refs
        return refs
    if isinstance(refs, CommentedSeq):
        return refs
    if isinstance(refs, list):
        out = CommentedSeq()
        out.extend(refs)
        data["references"] = out
        return out
    out = CommentedSeq()
    data["references"] = out
    return out


def append_publication_reference(
    refs: MutableMapping[str, Any] | CommentedSeq,
    reference: str,
    title: str,
    found_in: Iterable[str] | None = None,
) -> None:
    if not isinstance(refs, (list, CommentedSeq)):
        return
    ref_item = CommentedMap()
    ref_item["reference"] = reference
    ref_item["title"] = title
    if found_in:
        ref_item["found_in"] = CommentedSeq(sorted(set(found_in)))
    ref_item["findings"] = CommentedSeq()
    refs.append(ref_item)


def normalize_found_in_entries(value: Any) -> Set[str]:
    if isinstance(value, str):
        entry = value.strip()
        return {entry} if entry else set()
    if isinstance(value, list):
        out = set()
        for item in value:
            if isinstance(item, str):
                entry = item.strip()
                if entry:
                    out.add(entry)
        return out
    return set()


def merge_found_in(ref_item: MutableMapping[str, Any], found_in: Iterable[str]) -> bool:
    new_entries = {
        entry.strip() for entry in found_in if isinstance(entry, str) and entry.strip()
    }
    if not new_entries:
        return False

    existing_entries = normalize_found_in_entries(ref_item.get("found_in"))
    merged_entries = sorted(existing_entries.union(new_entries))
    if merged_entries == sorted(existing_entries):
        return False

    seq = CommentedSeq()
    seq.extend(merged_entries)
    ref_item["found_in"] = seq
    return True


def migrate_holder_to_references(
    data: MutableMapping[str, Any],
    references_cache_dir: str,
) -> int:
    """Move legacy deep-research holder evidence refs to top-level references."""
    pathophys = data.get("pathophysiology")
    if not isinstance(pathophys, (list, CommentedSeq)):
        return 0

    refs = ensure_references_list(data)
    existing_top_refs: Set[str] = set()
    for item in refs:
        if isinstance(item, Mapping) and isinstance(item.get("reference"), str):
            canon = canonical_ref(item.get("reference", ""))
            if canon:
                existing_top_refs.add(canon)

    moved = 0
    to_remove = []
    for idx, item in enumerate(pathophys):
        if not (isinstance(item, MutableMapping) and item.get("name") == HOLDER_NAME):
            continue
        ev = item.get("evidence")
        if isinstance(ev, list):
            for e in ev:
                if not isinstance(e, Mapping):
                    continue
                ref_val = e.get("reference")
                if not isinstance(ref_val, str):
                    continue
                canon = canonical_ref(ref_val)
                if not canon or canon in existing_top_refs:
                    continue
                title = None
                snip = e.get("snippet")
                if isinstance(snip, str) and snip.strip():
                    title = snip.strip()
                if not title:
                    cache_path = cache_path_for_ref(canon, references_cache_dir)
                    title = parse_cache_title(cache_path) or canon
                append_publication_reference(refs, canon, title)
                existing_top_refs.add(canon)
                moved += 1
        to_remove.append(idx)

    for idx in reversed(to_remove):
        del pathophys[idx]

    return moved


def main() -> int:
    args = parse_args()
    only = set(args.only or [])

    kb_paths = {
        Path(path).stem: Path(path)
        for path in glob.glob(os.path.join(args.kb_dir, "*.yaml"))
        if not path.endswith(".history.yaml")
    }
    deep_refs_by_disorder = citations_by_disorder(args.research_dir)

    disorders = sorted(name for name in deep_refs_by_disorder if name in kb_paths)
    if only:
        disorders = [name for name in disorders if name in only]
    if args.max_disorders is not None:
        disorders = disorders[: args.max_disorders]

    yaml_rt = YAML()
    yaml_rt.preserve_quotes = True
    yaml_rt.indent(mapping=2, sequence=2, offset=0)
    now_iso = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    results: List[DisorderResult] = []
    unresolved_rows: List[Tuple[str, str, str]] = []

    for idx, disorder in enumerate(disorders, start=1):
        yaml_path = kb_paths[disorder]
        cited_ref_to_files = deep_refs_by_disorder[disorder]
        cited_refs = set(cited_ref_to_files.keys())

        with yaml_path.open("r", encoding="utf-8") as handle:
            data = yaml_rt.load(handle)
        if data is None:
            continue

        existing_refs: Set[str] = set()
        collect_existing_refs(data, existing_refs)

        missing_refs = sorted(ref for ref in cited_refs if ref not in existing_refs)
        if args.max_new_refs_per_disorder is not None:
            missing_refs = missing_refs[: args.max_new_refs_per_disorder]

        print(
            f"[{idx}/{len(disorders)}] {disorder}: "
            f"cited={len(cited_refs)} existing={len(existing_refs)} missing={len(missing_refs)}"
        )

        added = 0
        unresolved = 0
        changed = False

        migrated = migrate_holder_to_references(
            data=data,
            references_cache_dir=args.references_cache_dir,
        )
        if migrated > 0:
            changed = True

        if missing_refs:
            refs = ensure_references_list(data)
            top_ref_items: Dict[str, MutableMapping[str, Any]] = {}
            for item in refs:
                if (
                    isinstance(item, MutableMapping)
                    and isinstance(item.get("reference"), str)
                    and (canon := canonical_ref(item.get("reference", "")))
                ):
                    top_ref_items[canon] = item

            for reference, found_in in cited_ref_to_files.items():
                existing_item = top_ref_items.get(reference)
                if existing_item and merge_found_in(existing_item, found_in):
                    changed = True

            for reference in missing_refs:
                if reference in top_ref_items:
                    continue

                cache_path = cache_path_for_ref(reference, args.references_cache_dir)
                if not cache_path.exists() and args.fetch_missing_cache:
                    fetch_reference(reference, args.fetch_timeout_seconds)

                title = parse_cache_title(cache_path)
                if not title:
                    unresolved += 1
                    unresolved_rows.append(
                        (disorder, reference, "cache_not_found_or_no_title")
                    )
                    continue

                append_publication_reference(
                    refs,
                    reference,
                    title,
                    found_in=cited_ref_to_files.get(reference, set()),
                )
                new_item = refs[-1]
                if isinstance(new_item, MutableMapping):
                    top_ref_items[reference] = new_item
                added += 1
                changed = True
        else:
            refs = ensure_references_list(data)
            for item in refs:
                if (
                    isinstance(item, MutableMapping)
                    and isinstance(item.get("reference"), str)
                    and (canon := canonical_ref(item.get("reference", "")))
                    and canon in cited_ref_to_files
                    and merge_found_in(item, cited_ref_to_files[canon])
                ):
                    changed = True

        if changed and args.apply:
            if "updated_date" in data:
                data["updated_date"] = now_iso
            with yaml_path.open("w", encoding="utf-8") as handle:
                yaml_rt.dump(data, handle)

        results.append(
            DisorderResult(
                disorder=disorder,
                cited_refs=len(cited_refs),
                existing_refs=len(existing_refs),
                missing_refs=len(missing_refs),
                added_refs=added,
                unresolved_refs=unresolved,
                changed=changed,
            )
        )

    Path(args.output_dir).mkdir(parents=True, exist_ok=True)
    ts = time.strftime("%Y%m%d-%H%M%S")
    summary_path = Path(args.output_dir) / f"deep_research_evidence_backfill_{ts}.tsv"
    unresolved_path = Path(args.output_dir) / f"deep_research_unresolved_refs_{ts}.tsv"

    with summary_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(
            [
                "disorder",
                "cited_refs",
                "existing_refs",
                "missing_refs",
                "added_refs",
                "unresolved_refs",
                "changed",
            ]
        )
        for row in results:
            writer.writerow(
                [
                    row.disorder,
                    row.cited_refs,
                    row.existing_refs,
                    row.missing_refs,
                    row.added_refs,
                    row.unresolved_refs,
                    str(row.changed),
                ]
            )

    with unresolved_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["disorder", "reference", "reason"])
        writer.writerows(unresolved_rows)

    total_added = sum(r.added_refs for r in results)
    total_missing = sum(r.missing_refs for r in results)
    total_unresolved = sum(r.unresolved_refs for r in results)
    changed_count = sum(1 for r in results if r.changed)
    mode = "APPLY" if args.apply else "DRY_RUN"
    print(
        f"{mode} summary: disorders={len(results)} changed={changed_count} "
        f"missing_refs={total_missing} added_refs={total_added} "
        f"unresolved_refs={total_unresolved}"
    )
    print(f"Summary report: {summary_path}")
    print(f"Unresolved refs: {unresolved_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
