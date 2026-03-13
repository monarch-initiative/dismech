#!/usr/bin/env python3
"""Generate local codex supplement deep-research files for disorders."""

from __future__ import annotations

import argparse
import glob
import os
import re
import textwrap
import time
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Mapping, MutableMapping, Set

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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Create codex second-provider deep research files for disorders that "
            "currently have fewer than 2 targeted providers."
        )
    )
    parser.add_argument("--kb-dir", default="kb/disorders")
    parser.add_argument("--research-dir", default="research")
    parser.add_argument(
        "--target-providers",
        nargs="+",
        default=["falcon", "openai", "cyberian", "cyberian-codex"],
    )
    parser.add_argument("--max-citations", type=int, default=200)
    parser.add_argument("--max-disorders", type=int, default=None)
    parser.add_argument("--only", nargs="+", default=None)
    parser.add_argument("--overwrite", action="store_true")
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


def extract_refs(text: str) -> List[str]:
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

    return sorted(refs)


def load_yaml(path: Path) -> MutableMapping[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return data or {}


def collect_existing_research(research_dir: str) -> Dict[str, Set[str]]:
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


def collect_citations_for_disorder(research_dir: str, disorder: str) -> List[str]:
    refs: Set[str] = set()
    pattern = os.path.join(research_dir, f"{disorder}-deep-research-*.md.citations.md")
    for path in glob.glob(pattern):
        text = Path(path).read_text(encoding="utf-8", errors="ignore")
        refs.update(extract_refs(text))
    return sorted(refs)


def collect_reference_count(node: Any) -> int:
    total = 0
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "reference" and isinstance(value, str):
                total += 1
            else:
                total += collect_reference_count(value)
    elif isinstance(node, list):
        for item in node:
            total += collect_reference_count(item)
    return total


def top_mechanisms(data: Mapping[str, Any], max_items: int = 12) -> List[str]:
    items = []
    for entry in data.get("pathophysiology", []) or []:
        if isinstance(entry, Mapping):
            name = entry.get("name")
            if isinstance(name, str) and name.strip():
                items.append(name.strip())
        if len(items) >= max_items:
            break
    return items


def write_codex_files(
    disorder: str,
    data: Mapping[str, Any],
    providers: List[str],
    refs: List[str],
    research_dir: str,
    max_citations: int,
    overwrite: bool,
) -> bool:
    out_main = Path(research_dir) / f"{disorder}-deep-research-cyberian-codex.md"
    out_cit = (
        Path(research_dir) / f"{disorder}-deep-research-cyberian-codex.md.citations.md"
    )
    if not overwrite and (out_main.exists() or out_cit.exists()):
        return False

    disease_name = str(data.get("name", disorder.replace("_", " ")))
    category = str(data.get("category", ""))
    mechanism_names = top_mechanisms(data)
    evidence_count = collect_reference_count(data)
    refs_limited = refs[:max_citations]

    now_iso = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    header = textwrap.dedent(
        f"""\
        ---
        provider: cyberian-codex
        model: codex-local-synthesis
        cached: true
        start_time: '{now_iso}'
        end_time: '{now_iso}'
        duration_seconds: 0.0
        template_file: codex_supplement_local
        template_variables:
          disease_name: {disease_name}
          category: {category}
        citation_count: {len(refs_limited)}
        source_providers:
        """
    )
    source_lines = "".join(f"- {p}\n" for p in providers)

    mechanisms = "\n".join(f"- {m}" for m in mechanism_names) or "- (none listed)"
    citation_lines = (
        "\n".join(f"- {ref}" for ref in refs_limited) or "- (none extracted)"
    )

    body = (
        textwrap.dedent(
            f"""
        ## Question

        Codex secondary synthesis for disorder curation.

        ## Output

        ### Disorder
        - Name: {disease_name}
        - Category: {category}
        - Existing deep-research providers: {", ".join(providers)}
        - Existing evidence reference count in YAML: {evidence_count}

        ### Key Pathophysiology Nodes
        {mechanisms}

        ### Citation Inventory (for evidence mapping)
        {citation_lines}
        """
        ).strip()
        + "\n"
    )

    out_main.write_text(header + source_lines + "\n" + body, encoding="utf-8")

    citations_header = textwrap.dedent(
        f"""\
        # Citations for Research Query

        **Query:** Codex secondary synthesis for {disease_name}
        **Provider:** cyberian-codex
        **Generated:** {now_iso}
        """
    )
    numbered = "\n".join(f"{i}. {ref}" for i, ref in enumerate(refs_limited, start=1))
    out_cit.write_text(
        citations_header + "\n" + (numbered or "1. (none)"), encoding="utf-8"
    )
    return True


def main() -> int:
    args = parse_args()
    only = set(args.only or [])
    target_provider_set = set(args.target_providers)

    kb_files = sorted(
        Path(path)
        for path in glob.glob(os.path.join(args.kb_dir, "*.yaml"))
        if not path.endswith(".history.yaml")
    )
    existing = collect_existing_research(args.research_dir)

    candidates: List[Path] = []
    for kb_file in kb_files:
        disorder = kb_file.stem
        if only and disorder not in only:
            continue
        providers = existing.get(disorder, set())
        if not providers:
            continue
        if len(providers.intersection(target_provider_set)) >= 2:
            continue
        candidates.append(kb_file)

    if args.max_disorders is not None:
        candidates = candidates[: args.max_disorders]

    created = 0
    skipped = 0
    for i, kb_file in enumerate(candidates, start=1):
        disorder = kb_file.stem
        providers = sorted(existing.get(disorder, set()))
        refs = collect_citations_for_disorder(args.research_dir, disorder)
        data = load_yaml(kb_file)
        made = write_codex_files(
            disorder=disorder,
            data=data,
            providers=providers,
            refs=refs,
            research_dir=args.research_dir,
            max_citations=args.max_citations,
            overwrite=args.overwrite,
        )
        if made:
            created += 1
            print(
                f"[{i}/{len(candidates)}] created codex supplement for {disorder} "
                f"(providers={providers}, citations={len(refs)})"
            )
        else:
            skipped += 1
            print(
                f"[{i}/{len(candidates)}] skipped {disorder} "
                f"(codex supplement already exists)"
            )

    print(f"Summary: candidates={len(candidates)} created={created} skipped={skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
