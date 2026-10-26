#!/usr/bin/env python3
"""Check ``animal_models[].model_mappings`` against a committed record cache.

What the slot holds
-------------------
A link from a DisMech animal model to the record for the same model in a model
organism database: an MGI genotype, a ZFIN fish, or an RGD strain (#15395).

Why ``validate-terms`` cannot check it
--------------------------------------
No OAK adapter serves these records, so a fabricated label passes the term
validator. Worse, MGI and RGD use one ID space for genes and for
genotypes/strains: ``MGI:1097716`` is the Arx *gene* and ``MGI:3844352`` an Arx
*genotype*, and the schema's id pattern accepts both. So this check reads each
record's **type** as well as its label from ``cache/mod_models/genotypes.csv``.

The cache
---------
One row per record: ``curie,label,category,taxon,source_label,retrieved_at``.
Filled with ``--resolve`` from the Monarch KG entity API, which carries the
Alliance genotype nodes with their Biolink category and NCBITaxon. Never
hand-edit a row; delete it and re-run ``--resolve``.

``source_label`` is the record's name as served, e.g.
``Npr2<sup>pwe</sup>/Npr2<sup>pwe</sup>  [background:] involves: C3H/HeJ``.
``label`` is that name normalized, which is what a curator writes in
``term.label``:

1. drop everything from ``[background:]`` on (the background goes in
   ``background:`` if it is worth recording);
2. remove every HTML tag except ``<sup>``;
3. turn ``<sup>x</sup>`` into ``<x>``, the MGI plain-text allele convention;
4. collapse whitespace.

So the label above is ``Npr2<pwe>/Npr2<pwe>``.

Findings (every one exits 1)
----------------------------
``UNCACHED``         the record is not in the cache; run with ``--resolve``.
``UNKNOWN_RECORD``   the API does not know the identifier.
``NOT_A_GENOTYPE``   the record is not a ``biolink:Genotype`` (usually a gene ID).
``LABEL_MISMATCH``   ``term.label`` is not the normalized label.
``BAD_PREDICATE``    not exactMatch / narrowMatch / broadMatch / relatedMatch.
``DUPLICATE``        one model maps the same record twice.
``SHARED_EXACT``     two models in one entry both claim exactMatch to one record.

Usage
-----
    python scripts/check_model_mappings.py                 # gate, offline
    python scripts/check_model_mappings.py kb/disorders/ADNP-Related_Syndrome.yaml
    python scripts/check_model_mappings.py --resolve       # fetch uncached records
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dismech import kb_cache
from dismech.yaml_io import safe_load

PATTERNS = (
    "kb/disorders/**/*.yaml",
    "kb/modules/**/*.yaml",
    "kb/comorbidities/**/*.yaml",
)

CACHE_PATH = ROOT / "cache" / "mod_models" / "genotypes.csv"
CACHE_FIELDS = ("curie", "label", "category", "taxon", "source_label", "retrieved_at")
API = "https://api.monarchinitiative.org/v3/api/entity/"

GENOTYPE_CATEGORY = "biolink:Genotype"
PREDICATES = frozenset(
    {"skos:exactMatch", "skos:narrowMatch", "skos:broadMatch", "skos:relatedMatch"}
)

_BACKGROUND = re.compile(r"\[background:\].*$", re.S)
_NON_SUP_TAG = re.compile(r"</?(?!sup\b)[A-Za-z][^>]*>")
_SUP = re.compile(r"<sup>(.*?)</sup>", re.S)


def normalize_label(source_label: str) -> str:
    """The curator-facing label for a record name as the API serves it."""
    text = _BACKGROUND.sub("", source_label)
    text = _NON_SUP_TAG.sub("", text)
    text = _SUP.sub(r"<\1>", text)
    return " ".join(text.split())


class Finding:
    __slots__ = ("detail", "kind", "location", "path")

    def __init__(self, path: Path, location: str, kind: str, detail: str) -> None:
        self.path = path
        self.location = location
        self.kind = kind
        self.detail = detail


def load_cache(path: Path = CACHE_PATH) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    with path.open(newline="", encoding="utf-8") as handle:
        return {row["curie"]: row for row in csv.DictReader(handle)}


def write_cache(rows: dict[str, dict[str, str]], path: Path = CACHE_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=CACHE_FIELDS, lineterminator="\n")
        writer.writeheader()
        for curie in sorted(rows):
            writer.writerow({field: rows[curie].get(field, "") for field in CACHE_FIELDS})


def fetch_record(curie: str) -> dict[str, str] | None:
    """One cache row from the Monarch entity API, or None if it is unknown."""
    url = API + urllib.parse.quote(curie, safe=":")
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            data = json.load(response)
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return None
        raise
    source_label = data.get("name")
    if not source_label:
        return None
    return {
        "curie": curie,
        "label": normalize_label(source_label),
        "category": data.get("category") or "",
        "taxon": data.get("in_taxon") or "",
        "source_label": source_label,
        "retrieved_at": datetime.now().isoformat(),
    }


def iter_mappings(data: object):
    """(location, model index, model, mapping) for every model_mappings item."""
    if not isinstance(data, dict):
        return
    for m_index, model in enumerate(data.get("animal_models") or []):
        if not isinstance(model, dict):
            continue
        for j, mapping in enumerate(model.get("model_mappings") or []):
            if isinstance(mapping, dict):
                label = model.get("name") or model.get("genotype") or f"[{m_index}]"
                yield f"animal_models[{m_index}] ({label}).model_mappings[{j}]", m_index, mapping


def check_document(
    path: Path, data: object, cache: dict[str, dict[str, str]]
) -> list[Finding]:
    findings: list[Finding] = []
    seen_in_model: set[tuple[int, str]] = set()
    exact_claims: dict[str, list[str]] = defaultdict(list)

    for location, m_index, mapping in iter_mappings(data):
        term = mapping.get("term") or {}
        curie = term.get("id")
        if not curie:
            continue  # a missing term is linkml-validate's job
        predicate = mapping.get("mapping_predicate")

        if predicate not in PREDICATES:
            findings.append(Finding(path, location, "BAD_PREDICATE", f"{predicate!r}"))
        if (m_index, curie) in seen_in_model:
            findings.append(Finding(path, location, "DUPLICATE", curie))
        seen_in_model.add((m_index, curie))
        if predicate == "skos:exactMatch":
            exact_claims[curie].append(location)

        row = cache.get(curie)
        if row is None:
            findings.append(
                Finding(path, location, "UNCACHED", f"{curie}; run with --resolve")
            )
            continue
        if not row.get("category"):
            findings.append(Finding(path, location, "UNKNOWN_RECORD", curie))
            continue
        if row["category"] != GENOTYPE_CATEGORY:
            findings.append(
                Finding(
                    path,
                    location,
                    "NOT_A_GENOTYPE",
                    f"{curie} is {row['category']} ({row['label']})",
                )
            )
        if term.get("label") != row["label"]:
            findings.append(
                Finding(
                    path,
                    location,
                    "LABEL_MISMATCH",
                    f"{curie}: {term.get('label')!r} != {row['label']!r}",
                )
            )

    for curie, locations in exact_claims.items():
        models = {loc.split(".model_mappings")[0] for loc in locations}
        if len(models) > 1:
            findings.append(
                Finding(path, "; ".join(sorted(models)), "SHARED_EXACT", curie)
            )
    return findings


def _files(explicit: set[Path]) -> list[Path]:
    seen: dict[Path, None] = {}
    for pattern in PATTERNS:
        for candidate in sorted(ROOT.glob(pattern)):
            seen.setdefault(candidate, None)
    files = list(seen)
    if explicit:
        files = [f for f in files if f.resolve() in explicit]
    return files


def _display(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def _load_documents(paths: list[Path] | None) -> list[tuple[Path, object]]:
    explicit = {p.resolve() for p in paths} if paths else set()
    documents = []
    for path in _files(explicit):
        text = path.read_text(encoding="utf-8")
        if "model_mappings" not in text:
            continue
        try:
            documents.append((path, safe_load(text)))
        except Exception as exc:  # malformed YAML is check-duplicate-keys' job
            print(f"{_display(path)}: could not parse ({exc})", file=sys.stderr)
    return documents


def resolve_uncached(documents, cache: dict[str, dict[str, str]]) -> int:
    """Fetch every referenced record missing from the cache; return rows added."""
    wanted = sorted(
        {
            (mapping.get("term") or {}).get("id")
            for _, data in documents
            for _, _, mapping in iter_mappings(data)
        }
        - set(cache)
        - {None}
    )
    added = 0
    for curie in wanted:
        row = fetch_record(curie)
        if row is None:
            row = dict.fromkeys(CACHE_FIELDS, "")
            row.update(curie=curie, retrieved_at=datetime.now().isoformat())
        cache[curie] = row
        added += 1
    if added:
        write_cache(cache)
    return added


def scan_repo(paths: list[Path] | None = None, cache=None) -> list[Finding]:
    cache = load_cache() if cache is None else cache
    findings: list[Finding] = []
    for path, data in _load_documents(paths):
        findings.extend(check_document(path, data, cache))
    return findings


def main() -> int:
    kb_cache.default_off()
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument(
        "--resolve",
        action="store_true",
        help="fetch uncached records from the Monarch API and write them to the cache",
    )
    args = parser.parse_args()

    cache = load_cache()
    documents = _load_documents(args.paths or None)
    if args.resolve:
        added = resolve_uncached(documents, cache)
        print(f"added {added} record(s) to {_display(CACHE_PATH)}")

    findings: list[Finding] = []
    count = 0
    for path, data in documents:
        count += sum(1 for _ in iter_mappings(data))
        findings.extend(check_document(path, data, cache))

    for f in findings:
        print(f"{_display(f.path)}: {f.location}: {f.kind}: {f.detail}")
    print(
        f"{count} model mapping(s) in {len(documents)} file(s); "
        f"{len(findings)} finding(s)"
    )
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
