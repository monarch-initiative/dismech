#!/usr/bin/env python3
"""Map cached IEMbase disease JSON records to local DisMech entries.

Inputs are the raw JSON files produced by ``scripts/fetch_iembase_diseases.py``.
The crosswalk is deliberately conservative: strong identifier and exact alias
matches are marked as mapped; fuzzy name+gene hits are retained as review
candidates rather than silently treated as exact coverage.

Usage:
    just iembase-map
    uv run python scripts/map_iembase_to_dismech.py --output-tsv /tmp/map.tsv
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import unicodedata
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any


DEFAULT_IEMBASE_DIR = Path("data/iembase")
DEFAULT_KB_DIR = Path("kb/disorders")
DEFAULT_TSV = DEFAULT_IEMBASE_DIR / "dismech_mapping.tsv"
DEFAULT_JSON = DEFAULT_IEMBASE_DIR / "dismech_mapping.json"

TSV_COLUMNS = [
    "iembase_id",
    "iembase_nosology_code",
    "iembase_icimd_number",
    "iembase_name",
    "iembase_alt_names",
    "iembase_gene_sym",
    "iembase_omim",
    "iembase_orpha",
    "mapping_status",
    "match_confidence",
    "match_method",
    "dismech_name",
    "dismech_entry_type",
    "dismech_parent",
    "dismech_file",
    "dismech_entity_key",
    "dismech_mondo_id",
    "candidate_count",
    "candidate_entities",
    "best_candidate_name",
    "best_candidate_file",
    "best_candidate_score",
    "notes",
]

ROMAN_BY_VALUE = {
    "i": "1",
    "ii": "2",
    "iii": "3",
    "iv": "4",
    "v": "5",
    "vi": "6",
    "vii": "7",
    "viii": "8",
    "ix": "9",
    "x": "10",
}

FUZZY_STOP_TOKENS = {
    "abnormality",
    "acid",
    "congenital",
    "defect",
    "deficiency",
    "disease",
    "disorder",
    "familial",
    "hereditary",
    "metabolism",
    "related",
    "syndrome",
    "type",
}

EXACT_ALIAS_BLOCKLIST = {
    "autosomal dominant",
    "autosomal recessive",
    "congenital",
    "disorder",
    "inherited",
    "neurodevelopmental disorder",
}


@dataclass
class DismechEntity:
    entity_key: str
    entry_type: str
    name: str
    source_file: str
    parent_name: str = ""
    mondo_id: str = ""
    aliases: set[str] = field(default_factory=set)
    normalized_aliases: set[str] = field(default_factory=set)
    identifiers: set[str] = field(default_factory=set)
    genes: set[str] = field(default_factory=set)


@dataclass
class MatchResult:
    status: str
    confidence: str
    method: str = ""
    entities: list[DismechEntity] = field(default_factory=list)
    best_candidate: DismechEntity | None = None
    best_candidate_score: float = 0.0
    notes: str = ""


def clean_scalar(value: str) -> str:
    """Remove common YAML scalar quote/comment decoration from a simple value."""
    value = value.strip()
    if " #" in value:
        value = value.split(" #", 1)[0].rstrip()
    if len(value) >= 2 and value[0] == value[-1] and value.startswith(("'", '"')):
        return value[1:-1]
    return value


def normalize_text(value: str | None) -> str:
    """Normalize labels for conservative exact-name matching."""
    if not value:
        return ""
    value = value.replace("β", " beta ").replace("α", " alpha ").replace("γ", " gamma ")
    value = value.replace("–", "-").replace("—", "-")
    value = unicodedata.normalize("NFKD", value)
    value = "".join(c for c in value if not unicodedata.combining(c))
    value = value.casefold()
    value = re.sub(r"\btype\s+([ivx]+)([a-z]?)\b", _roman_type_repl, value)
    value = re.sub(r"\bmps\s+([ivx]+)([a-z]?)\b", _mps_roman_repl, value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return " ".join(value.split())


def _roman_type_repl(match: re.Match[str]) -> str:
    numeral = ROMAN_BY_VALUE.get(match.group(1), match.group(1))
    return f"type {numeral}{match.group(2)}"


def _mps_roman_repl(match: re.Match[str]) -> str:
    numeral = ROMAN_BY_VALUE.get(match.group(1), match.group(1))
    return f"mps {numeral}{match.group(2)}"


def alias_variants(value: str | None) -> set[str]:
    """Generate normalized aliases from one source label."""
    if not value:
        return set()
    raw_values = {value}
    without_parentheses = re.sub(r"\([^)]*\)", " ", value).strip()
    if without_parentheses and without_parentheses != value:
        raw_values.add(without_parentheses)
    stripped_related = re.sub(
        r"^[A-Za-z0-9,; /+-]+-related\s+",
        "",
        value,
        flags=re.IGNORECASE,
    ).strip()
    if stripped_related and stripped_related != value:
        raw_values.add(stripped_related)

    out: set[str] = set()
    for raw in raw_values:
        norm = normalize_text(raw)
        if norm:
            out.add(norm)
    return out


def alias_tokens(aliases: set[str]) -> set[str]:
    """Return distinctive tokens for narrowing fuzzy candidate pools."""
    tokens: set[str] = set()
    for alias in aliases:
        for token in alias.split():
            if len(token) < 4 or token in FUZZY_STOP_TOKENS:
                continue
            tokens.add(token)
    return tokens


def extract_top_level_value(text: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", text, flags=re.MULTILINE)
    return clean_scalar(match.group(1)) if match else ""


def extract_top_level_list(text: str, key: str) -> list[str]:
    body = extract_top_level_block(text, key)
    values: list[str] = []
    for match in re.finditer(r"^-\s+(.+?)\s*$", body, flags=re.MULTILINE):
        values.append(clean_scalar(match.group(1)))
    return values


def extract_top_level_block(text: str, key: str) -> str:
    match = re.search(
        rf"^{re.escape(key)}:\s*\n(?P<body>.*?)(?=^[A-Za-z_][A-Za-z0-9_]*:|\Z)",
        text,
        flags=re.MULTILINE | re.DOTALL,
    )
    return match.group("body") if match else ""


def first_mondo_id(block: str) -> str:
    match = re.search(r"^\s*id:\s*(MONDO:\d+)\s*$", block, flags=re.MULTILINE)
    return match.group(1) if match else ""


def first_term_label(block: str) -> str:
    match = re.search(r"^\s*label:\s*(.+?)\s*$", block, flags=re.MULTILINE)
    return clean_scalar(match.group(1)) if match else ""


def first_preferred_term(block: str) -> str:
    match = re.search(r"^\s*preferred_term:\s*(.+?)\s*$", block, flags=re.MULTILINE)
    return clean_scalar(match.group(1)) if match else ""


def identifiers_in_text(text: str) -> set[str]:
    identifiers = {f"ORPHA:{x}" for x in re.findall(r"ORPHA:(\d+)", text)}
    identifiers.update(f"OMIM:{x}" for x in re.findall(r"OMIM:(\d+)", text))
    return identifiers


def hgnc_labels_in_text(text: str) -> set[str]:
    labels: set[str] = set()
    for match in re.finditer(
        r"id:\s*hgnc:\d+\s*\n\s*label:\s*([A-Za-z0-9_.-]+)",
        text,
        flags=re.IGNORECASE,
    ):
        labels.add(match.group(1).upper())
    return labels


def add_alias(entity: DismechEntity, alias: str | None) -> None:
    if not alias:
        return
    alias = alias.strip()
    if not alias:
        return
    entity.aliases.add(alias)
    entity.normalized_aliases.update(alias_variants(alias))


def parse_dismech_entities(kb_dir: Path) -> list[DismechEntity]:
    entities: list[DismechEntity] = []
    for path in sorted(kb_dir.glob("*.yaml")):
        text = path.read_text(encoding="utf-8", errors="replace")
        disease_name = extract_top_level_value(text, "name") or path.stem.replace(
            "_", " "
        )
        disease_term = extract_top_level_block(text, "disease_term")
        entity = DismechEntity(
            entity_key=path.stem,
            entry_type="disease",
            name=disease_name,
            source_file=path.name,
            mondo_id=first_mondo_id(disease_term),
            identifiers=identifiers_in_text(text),
            genes=hgnc_labels_in_text(text),
        )
        for alias in [
            disease_name,
            path.stem.replace("_", " "),
            first_preferred_term(disease_term),
            first_term_label(disease_term),
            *extract_top_level_list(text, "synonyms"),
        ]:
            add_alias(entity, alias)
        entities.append(entity)

        for index, subtype_block in enumerate(extract_subtype_blocks(text), start=1):
            subtype_name = extract_block_value(subtype_block, "name")
            if not subtype_name:
                continue
            subtype_term = extract_nested_block(subtype_block, "subtype_term")
            subtype = DismechEntity(
                entity_key=f"{path.stem}#{subtype_name}",
                entry_type="subtype",
                name=subtype_name,
                source_file=path.name,
                parent_name=disease_name,
                mondo_id=first_mondo_id(subtype_term),
                identifiers=identifiers_in_text(subtype_block),
                genes=hgnc_labels_in_text(subtype_block),
            )
            for alias in [
                subtype_name,
                extract_block_value(subtype_block, "display_name"),
                first_preferred_term(subtype_term),
                first_term_label(subtype_term),
            ]:
                add_alias(subtype, alias)
            if not subtype.entity_key:
                subtype.entity_key = f"{path.stem}#subtype-{index}"
            entities.append(subtype)
    return entities


def extract_subtype_blocks(text: str) -> list[str]:
    body = extract_top_level_block(text, "has_subtypes")
    if not body:
        return []
    starts = [
        match.start() for match in re.finditer(r"^- name:\s*", body, flags=re.MULTILINE)
    ]
    blocks: list[str] = []
    for i, start in enumerate(starts):
        end = starts[i + 1] if i + 1 < len(starts) else len(body)
        blocks.append(body[start:end])
    return blocks


def extract_block_value(block: str, key: str) -> str:
    match = re.search(
        rf"^\s*-?\s*{re.escape(key)}:\s*(.+?)\s*$",
        block,
        flags=re.MULTILINE,
    )
    return clean_scalar(match.group(1)) if match else ""


def extract_nested_block(block: str, key: str) -> str:
    match = re.search(
        rf"^\s*{re.escape(key)}:\s*\n(?P<body>.*?)(?=^\s{{0,2}}[A-Za-z_][A-Za-z0-9_]*:|^\s*-\s+[A-Za-z_][A-Za-z0-9_]*:|\Z)",
        block,
        flags=re.MULTILINE | re.DOTALL,
    )
    return match.group("body") if match else ""


def split_identifiers(value: str | None, prefix: str) -> set[str]:
    if not value:
        return set()
    ids = set()
    for part in re.split(r"[;,\s]+", str(value)):
        part = part.strip()
        if part:
            ids.add(f"{prefix}:{part.removeprefix(prefix + ':')}")
    return ids


def iembase_aliases(record: dict[str, Any]) -> set[str]:
    aliases: set[str] = set()
    for key in ("name", "name_alt1", "name_alt2", "abbr"):
        aliases.update(alias_variants(record.get(key)))
    return aliases


def iembase_genes(record: dict[str, Any]) -> set[str]:
    genes: set[str] = set()
    for key in ("gene_sym", "hgnc_gene_sym"):
        raw = record.get(key)
        if not raw:
            continue
        for part in re.split(r"[;,/]\s*|\s+\+\s+", str(raw)):
            part = part.strip()
            if part and part.upper() != "NOGENE":
                genes.add(part.upper())
    return genes


def build_lookup(
    entities: list[DismechEntity],
) -> tuple[
    dict[str, list[DismechEntity]],
    dict[str, list[DismechEntity]],
    dict[str, list[DismechEntity]],
    dict[str, list[DismechEntity]],
    dict[str, list[DismechEntity]],
]:
    by_identifier: dict[str, list[DismechEntity]] = {}
    by_mondo: dict[str, list[DismechEntity]] = {}
    by_alias: dict[str, list[DismechEntity]] = {}
    by_gene: dict[str, list[DismechEntity]] = {}
    by_token: dict[str, list[DismechEntity]] = {}

    def add(
        mapping: dict[str, list[DismechEntity]], key: str, entity: DismechEntity
    ) -> None:
        if key:
            mapping.setdefault(key, []).append(entity)

    for entity in entities:
        add(by_mondo, entity.mondo_id, entity)
        for identifier in entity.identifiers:
            add(by_identifier, identifier, entity)
        for alias in entity.normalized_aliases:
            if alias in EXACT_ALIAS_BLOCKLIST:
                continue
            add(by_alias, alias, entity)
        for token in alias_tokens(entity.normalized_aliases):
            add(by_token, token, entity)
        for gene in entity.genes:
            add(by_gene, gene, entity)
    return by_identifier, by_mondo, by_alias, by_gene, by_token


def unique_entities(entities: list[DismechEntity]) -> list[DismechEntity]:
    seen: set[str] = set()
    out: list[DismechEntity] = []
    for entity in entities:
        if entity.entity_key in seen:
            continue
        seen.add(entity.entity_key)
        out.append(entity)
    return out


def exact_or_ambiguous(
    method: str,
    candidates: list[DismechEntity],
    *,
    confidence: str = "HIGH",
) -> MatchResult:
    candidates = unique_entities(candidates)
    if len(candidates) == 1:
        return MatchResult("MAPPED", confidence, method, candidates)
    return MatchResult(
        "AMBIGUOUS",
        "REVIEW",
        method,
        candidates,
        notes=f"{len(candidates)} DisMech entities share this match key",
    )


def match_record(
    record: dict[str, Any],
    *,
    entities: list[DismechEntity],
    by_identifier: dict[str, list[DismechEntity]],
    by_alias: dict[str, list[DismechEntity]],
    by_gene: dict[str, list[DismechEntity]],
    by_token: dict[str, list[DismechEntity]],
) -> MatchResult:
    identifiers = set()
    identifiers.update(split_identifiers(record.get("orphacode"), "ORPHA"))
    identifiers.update(split_identifiers(record.get("omim_no"), "OMIM"))
    for identifier in sorted(identifiers):
        if identifier in by_identifier:
            return exact_or_ambiguous(
                f"identifier:{identifier}", by_identifier[identifier]
            )

    aliases = iembase_aliases(record)
    for alias in sorted(aliases):
        if alias in by_alias:
            return exact_or_ambiguous(f"alias_exact:{alias}", by_alias[alias])

    candidate, score = best_fuzzy_candidate(
        aliases,
        iembase_genes(record),
        entities,
        by_gene,
        by_token,
    )
    if candidate and score >= 0.90:
        return MatchResult(
            "CANDIDATE",
            "MEDIUM",
            "fuzzy_alias_gene"
            if iembase_genes(record) & candidate.genes
            else "fuzzy_alias",
            [candidate],
            best_candidate=candidate,
            best_candidate_score=score,
            notes="Review candidate; not treated as exact mapped coverage.",
        )
    return MatchResult(
        "UNMAPPED",
        "NONE",
        "",
        [],
        best_candidate=candidate,
        best_candidate_score=score,
    )


def best_fuzzy_candidate(
    aliases: set[str],
    genes: set[str],
    entities: list[DismechEntity],
    by_gene: dict[str, list[DismechEntity]],
    by_token: dict[str, list[DismechEntity]],
) -> tuple[DismechEntity | None, float]:
    if not aliases:
        return None, 0.0
    gene_pool: list[DismechEntity] = []
    for gene in genes:
        gene_pool.extend(by_gene.get(gene, []))
    gene_pool = unique_entities(gene_pool)

    token_pool: list[DismechEntity] = []
    query_tokens = alias_tokens(aliases)
    for token in query_tokens:
        token_pool.extend(by_token.get(token, []))
    token_pool = unique_entities(token_pool)

    if gene_pool and token_pool:
        token_keys = {entity.entity_key for entity in token_pool}
        pool = [
            entity for entity in gene_pool if entity.entity_key in token_keys
        ] or gene_pool
    elif gene_pool:
        pool = gene_pool
    else:
        pool = token_pool

    if not pool:
        return None, 0.0
    if len(pool) > 250:
        token_counts = [
            (
                len(query_tokens & alias_tokens(entity.normalized_aliases)),
                len(entity.normalized_aliases),
                entity,
            )
            for entity in pool
        ]
        token_counts.sort(key=lambda item: (item[0], -item[1]), reverse=True)
        pool = [
            entity for count, _alias_count, entity in token_counts[:250] if count > 0
        ]

    best_entity: DismechEntity | None = None
    best_score = 0.0
    for entity in pool:
        for alias in aliases:
            for entity_alias in entity.normalized_aliases:
                if not (alias_tokens({alias}) & alias_tokens({entity_alias})):
                    continue
                score = SequenceMatcher(None, alias, entity_alias).ratio()
                if score > best_score:
                    best_score = score
                    best_entity = entity
    return best_entity, best_score


def load_iembase_records(iembase_dir: Path) -> list[dict[str, Any]]:
    index_path = iembase_dir / "disease_index.json"
    if not index_path.exists():
        raise FileNotFoundError(
            f"{index_path} not found; run `just iembase-prefetch` first"
        )
    index = json.loads(index_path.read_text(encoding="utf-8"))
    records: list[dict[str, Any]] = []
    for row in index.get("diseases", []):
        detail_path = iembase_dir / row["detail_json"]
        detail = json.loads(detail_path.read_text(encoding="utf-8"))
        detail["_index_row"] = row
        records.append(detail)
    records.sort(key=lambda record: int(record["_index_row"]["id"]))
    return records


def row_for_record(record: dict[str, Any], result: MatchResult) -> dict[str, str]:
    index_row = record["_index_row"]
    selected = result.entities[0] if len(result.entities) == 1 else None
    candidate_entities = unique_entities(result.entities)
    best = result.best_candidate
    if selected and not best:
        best = selected
        result.best_candidate_score = 1.0

    alt_names = "; ".join(
        str(record.get(key))
        for key in ("name_alt1", "name_alt2", "abbr")
        if record.get(key)
    )
    return {
        "iembase_id": str(index_row["id"]),
        "iembase_nosology_code": str(record.get("nosology_iem_code") or ""),
        "iembase_icimd_number": str(record.get("icimd_nosology_disorder_num") or ""),
        "iembase_name": str(record.get("name") or ""),
        "iembase_alt_names": alt_names,
        "iembase_gene_sym": str(record.get("gene_sym") or ""),
        "iembase_omim": str(record.get("omim_no") or ""),
        "iembase_orpha": str(record.get("orphacode") or ""),
        "mapping_status": result.status,
        "match_confidence": result.confidence,
        "match_method": result.method,
        "dismech_name": selected.name if selected else "",
        "dismech_entry_type": selected.entry_type if selected else "",
        "dismech_parent": selected.parent_name if selected else "",
        "dismech_file": selected.source_file if selected else "",
        "dismech_entity_key": selected.entity_key if selected else "",
        "dismech_mondo_id": selected.mondo_id if selected else "",
        "candidate_count": str(len(candidate_entities)),
        "candidate_entities": "; ".join(
            entity.entity_key for entity in candidate_entities
        ),
        "best_candidate_name": best.name if best else "",
        "best_candidate_file": best.source_file if best else "",
        "best_candidate_score": f"{result.best_candidate_score:.3f}" if best else "",
        "notes": result.notes,
    }


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=TSV_COLUMNS, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    tmp.replace(path)


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    tmp.replace(path)


def build_crosswalk(
    args: argparse.Namespace,
) -> tuple[list[dict[str, str]], dict[str, Any]]:
    entities = parse_dismech_entities(args.kb_dir)
    by_identifier, _by_mondo, by_alias, by_gene, by_token = build_lookup(entities)
    records = load_iembase_records(args.iembase_dir)

    rows: list[dict[str, str]] = []
    for record in records:
        result = match_record(
            record,
            entities=entities,
            by_identifier=by_identifier,
            by_alias=by_alias,
            by_gene=by_gene,
            by_token=by_token,
        )
        rows.append(row_for_record(record, result))

    status_counts: dict[str, int] = {}
    method_counts: dict[str, int] = {}
    for row in rows:
        status_counts[row["mapping_status"]] = (
            status_counts.get(row["mapping_status"], 0) + 1
        )
        method = row["match_method"] or "-"
        method_counts[method] = method_counts.get(method, 0) + 1
    summary = {
        "iembase_count": len(records),
        "dismech_entity_count": len(entities),
        "dismech_disease_count": sum(
            1 for entity in entities if entity.entry_type == "disease"
        ),
        "dismech_subtype_count": sum(
            1 for entity in entities if entity.entry_type == "subtype"
        ),
        "status_counts": dict(sorted(status_counts.items())),
        "method_counts": dict(sorted(method_counts.items())),
    }
    return rows, summary


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--iembase-dir", type=Path, default=DEFAULT_IEMBASE_DIR)
    parser.add_argument("--kb-dir", type=Path, default=DEFAULT_KB_DIR)
    parser.add_argument("--output-tsv", type=Path, default=DEFAULT_TSV)
    parser.add_argument("--output-json", type=Path, default=DEFAULT_JSON)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    rows, summary = build_crosswalk(args)
    write_tsv(args.output_tsv, rows)
    write_json(args.output_json, {"summary": summary, "rows": rows})
    print(
        f"Wrote {len(rows)} IEMbase→DisMech rows to {args.output_tsv} "
        f"and {args.output_json}"
    )
    print(
        "Status counts:",
        ", ".join(f"{k}={v}" for k, v in summary["status_counts"].items()),
    )


if __name__ == "__main__":
    main()
