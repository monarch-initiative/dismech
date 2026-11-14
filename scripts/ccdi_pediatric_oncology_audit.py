#!/usr/bin/env python3
"""Compute the CCDI pediatric oncology diagnosis group for neoplasm entries.

The values of ``classifications.ccdi_pediatric_oncology_category`` are the
permissible values of caDSR CDE 16607972. caDSR binds each value to one or more
NCI Thesaurus concepts, so the value an entry should carry is computable:

1. read the entry's ``disease_term`` (MONDO);
2. read that term's ``NCIT:`` cross-references from MONDO (OLS);
3. walk each NCIt concept's ``is_a`` ancestors (OLS);
4. keep the values whose concept is the entry's concept or an ancestor of it;
5. drop a value whose concept is an ancestor of another kept value's concept,
   so the most specific one wins;
6. fall back to a residual ("Other ...") value only when no specific value is
   kept.

The report compares that proposal with what the entry records. It never
decides a tie: two specific values of which neither subsumes the other is
``AMBIGUOUS`` and is left for a curator. A recorded value the hierarchy cannot
derive is ``CURATED``: NCIt's "Wilms Tumor" is site-agnostic and so is not a
"Kidney Neoplasm", although CCDI files Wilms tumor under Renal Tumors.

``--apply`` writes the proposal into the ``classifications:`` block of the
files named on the command line, and only where the status is ``MISSING``.

Network-dependent (OLS) and therefore report-only and not part of ``just qc``.
Lookups are cached in ``tmp/ccdi_pediatric_oncology_ols.json``.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import textwrap
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from dismech import kb_cache
from dismech.yaml_io import safe_load_path

ENUM_PATH = (
    REPO_ROOT / "src/dismech/schema/classifications/ccdi_pediatric_oncology.yaml"
)
ENUM_NAME = "CCDIPediatricOncologyCategoryEnum"
SLOT = "ccdi_pediatric_oncology_category"
CACHE_PATH = REPO_ROOT / "tmp" / "ccdi_pediatric_oncology_ols.json"
OLS = "https://www.ebi.ac.uk/ols4/api/v2/ontologies"
DBXREF = "http://www.geneontology.org/formats/oboInOwl#hasDbXref"
TIMEOUT = 60

#: Same scope test as ``scripts/check_cancer_origin.py``: an entry is a
#: candidate when its name, categories or disease-term label reads as a
#: neoplasm, or it already carries an ICD-O morphology value.
NEOPLASM_RE = re.compile(
    r"cancer|neoplas|tumou?r|leuk[ae]m|lymphom|sarcom|carcinom|myelom|glioma"
    r"|blastoma|melanoma|malignan|mesotheliom|adenoma|myeloprolif|myelodysplas"
    r"|histiocytosis|ependymom|craniopharyngiom|teratoma|paragangliom",
    re.IGNORECASE,
)

STATUSES = ("MATCH", "MISSING", "CONFLICT", "AMBIGUOUS", "CURATED", "NO_NCIT", "NONE")


@dataclass(frozen=True)
class Category:
    """One permissible value and the NCIt concepts caDSR binds it to."""

    name: str
    concepts: tuple[str, ...]
    residual: bool


@dataclass
class Row:
    path: Path
    name: str
    mondo: str
    ncit: tuple[str, ...] = ()
    proposed: tuple[str, ...] = ()
    via: str = ""
    current: str = ""
    status: str = "NONE"
    detail: str = field(default="")


def load_categories(enum_path: Path = ENUM_PATH) -> list[Category]:
    """Read the value-to-concept bindings out of the enum module."""
    schema = safe_load_path(enum_path)
    values = schema["enums"][ENUM_NAME]["permissible_values"]
    categories = []
    for name, body in values.items():
        body = body or {}
        annotations = body.get("annotations") or {}
        if body.get("meaning"):
            categories.append(Category(name, (body["meaning"],), False))
        elif annotations.get("residual_of"):
            categories.append(Category(name, (annotations["residual_of"],), True))
        elif annotations.get("ncit_scope"):
            scope = tuple(str(annotations["ncit_scope"]).split())
            categories.append(Category(name, scope, False))
        else:
            raise ValueError(f"{name}: no meaning, residual_of or ncit_scope")
    return categories


class Ols:
    """Cached OLS lookups: a MONDO term's NCIt xrefs, an NCIt term's ancestors."""

    def __init__(self, cache_path: Path = CACHE_PATH, offline: bool = False):
        self.cache_path = cache_path
        self.offline = offline
        self.cache: dict[str, list[str]] = {}
        if cache_path.exists():
            self.cache = json.loads(cache_path.read_text())
        self.dirty = False
        self.unsaved = 0

    def save(self) -> None:
        if not self.dirty:
            return
        self.cache_path.parent.mkdir(parents=True, exist_ok=True)
        self.cache_path.write_text(json.dumps(self.cache, indent=1, sort_keys=True))
        self.dirty = False
        self.unsaved = 0

    @staticmethod
    def _class_url(curie: str) -> str:
        prefix, local = curie.split(":", 1)
        iri = f"http://purl.obolibrary.org/obo/{prefix}_{local}"
        quoted = urllib.parse.quote(urllib.parse.quote(iri, safe=""), safe="")
        return f"{OLS}/{prefix.lower()}/classes/{quoted}"

    def _get(self, url: str) -> dict | None:
        request = urllib.request.Request(url, headers={"Accept": "application/json"})
        try:
            with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            if error.code == 404:
                return None
            raise

    def _cached(self, key: str, fetch) -> list[str] | None:
        if key in self.cache:
            return self.cache[key]
        if self.offline:
            return None
        value = fetch()
        self.cache[key] = value
        self.dirty = True
        self.unsaved += 1
        if self.unsaved >= 25:  # an interrupted run keeps what it fetched
            self.save()
        return value

    def ncit_xrefs(self, mondo_id: str) -> list[str] | None:
        """``NCIT:`` cross-references MONDO records on a term."""

        def fetch() -> list[str]:
            payload = self._get(self._class_url(mondo_id)) or {}
            values = payload.get(DBXREF) or []
            if not isinstance(values, list):
                values = [values]
            found = []
            for value in values:
                text = value.get("value") if isinstance(value, dict) else value
                if isinstance(text, str) and text.startswith("NCIT:"):
                    found.append(text.strip())
            return sorted(set(found))

        return self._cached(f"xref:{mondo_id}", fetch)

    def ancestors(self, ncit_id: str) -> list[str] | None:
        """``is_a`` ancestors of an NCIt concept, not including itself."""

        def fetch() -> list[str]:
            found: list[str] = []
            page = 0
            while True:
                url = f"{self._class_url(ncit_id)}/ancestors?size=500&page={page}"
                payload = self._get(url)
                if payload is None:
                    break
                for element in payload.get("elements") or []:
                    curie = element.get("curie")
                    if isinstance(curie, str) and curie.startswith("NCIT:"):
                        found.append(curie)
                page += 1
                if page >= int(payload.get("totalPages") or 1):
                    break
            return sorted(set(found))

        return self._cached(f"anc:{ncit_id}", fetch)


def propose(
    concepts: tuple[str, ...], categories: list[Category], ols: Ols
) -> tuple[tuple[str, ...], str]:
    """Most specific value(s) for a disease's NCIt concepts, and the concept used."""
    closure: dict[str, set[str]] = {}
    for concept in concepts:
        ancestors = ols.ancestors(concept)
        if ancestors is None:
            continue
        closure[concept] = {concept, *ancestors}

    def matches(category: Category) -> str:
        for concept, reach in closure.items():
            if any(bound in reach for bound in category.concepts):
                return concept
        return ""

    specific = [(c, matches(c)) for c in categories if not c.residual]
    specific = [(c, via) for c, via in specific if via]
    pool = specific or [
        (c, via) for c in categories if c.residual and (via := matches(c))
    ]
    if not pool:
        return (), ""

    def subsumes(broad: Category, narrow: Category) -> bool:
        """True when every concept of ``narrow`` sits under a concept of ``broad``."""
        for concept in narrow.concepts:
            reach = set(ols.ancestors(concept) or [])
            if not any(bound in reach for bound in broad.concepts):
                return False
        return True

    kept = [
        (c, via)
        for c, via in pool
        if not any(other is not c and subsumes(c, other) for other, _ in pool)
    ]
    return tuple(c.name for c, _ in kept), kept[0][1]


def current_value(data: dict) -> str:
    classifications = data.get("classifications")
    if not isinstance(classifications, dict):
        return ""
    assignment = classifications.get(SLOT)
    if isinstance(assignment, dict):
        return str(assignment.get("classification_value") or "")
    return ""


def is_candidate(data: dict, path: Path) -> bool:
    classifications = data.get("classifications")
    if isinstance(classifications, dict) and (
        classifications.get("icdo_morphology") or classifications.get(SLOT)
    ):
        return True
    term = (data.get("disease_term") or {}).get("term") or {}
    categories = " | ".join(str(c) for c in data.get("categories") or [] if c)
    haystack = f"{data.get('name', path.stem)} {categories} {term.get('label', '')}"
    return bool(NEOPLASM_RE.search(haystack))


def audit(paths: list[Path], categories: list[Category], ols: Ols) -> list[Row]:
    rows = []
    for path in paths:
        data = kb_cache.load_document(path)
        if not isinstance(data, dict) or not is_candidate(data, path):
            continue
        term = (data.get("disease_term") or {}).get("term") or {}
        mondo = str(term.get("id") or "")
        row = Row(path, str(data.get("name", path.stem)), mondo)
        row.current = current_value(data)
        if mondo.startswith("MONDO:"):
            row.ncit = tuple(ols.ncit_xrefs(mondo) or ())
        if not row.ncit:
            row.status = "CURATED" if row.current else "NO_NCIT"
            row.detail = "MONDO term has no NCIT cross-reference"
            rows.append(row)
            continue
        row.proposed, row.via = propose(row.ncit, categories, ols)
        if len(row.proposed) > 1:
            row.status = "AMBIGUOUS"
        elif not row.proposed:
            row.status = "CURATED" if row.current else "NONE"
        elif not row.current:
            row.status = "MISSING"
        elif row.current == row.proposed[0]:
            row.status = "MATCH"
        else:
            row.status = "CONFLICT"
        rows.append(row)
    return rows


def assignment_block(row: Row, category: Category) -> str:
    """The YAML lines recording a derived value, with its derivation in notes."""
    bound = " or ".join(category.concepts)
    relation = "is" if row.via in category.concepts else "is a descendant of"
    what = (
        "the parent concept of this residual value"
        if category.residual
        else ("the concept caDSR binds this value to")
    )
    sentence = (
        f"caDSR CDE 16607972. Derived from {row.mondo}, whose NCIT "
        f"cross-reference {row.via} {relation} {bound}, {what}."
    )
    if category.residual:
        sentence += " No specific value of the CDE subsumes it."
    wrapped = textwrap.wrap(sentence, width=72, break_on_hyphens=False)
    lines = [
        f"  {SLOT}:",
        f"    classification_value: {category.name}",
        "    notes: >-",
        *[f"      {line}" for line in wrapped],
    ]
    return "\n".join(lines) + "\n"


def apply(rows: list[Row], categories: list[Category]) -> list[str]:
    """Write MISSING proposals into their entries; return what was done."""
    by_name = {c.name: c for c in categories}
    log = []
    for row in rows:
        if row.status != "MISSING":
            continue
        text = row.path.read_text()
        marker = "\nclassifications:\n"
        block = assignment_block(row, by_name[row.proposed[0]])
        if text.count(marker) == 1:
            row.path.write_text(text.replace(marker, marker + block))
        elif marker not in text and not text.startswith("classifications:"):
            # No block yet: open one at the end of the file.
            row.path.write_text(text.rstrip("\n") + marker + block)
        else:
            log.append(f"SKIPPED {row.path.name}: duplicate classifications: key")
            continue
        log.append(f"WROTE   {row.path.name}: {row.proposed[0]}")
    return log


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument(
        "--format", choices=("summary", "list", "tsv"), default="summary"
    )
    parser.add_argument("--status", action="append", choices=STATUSES)
    parser.add_argument(
        "--offline", action="store_true", help="use cached lookups only"
    )
    parser.add_argument("--strict", action="store_true", help="exit 1 on CONFLICT")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="write MISSING proposals into the files named on the command line",
    )
    args = parser.parse_args(argv)

    kb_cache.default_off()
    paths = args.files or sorted((REPO_ROOT / "kb" / "disorders").glob("*.yaml"))
    categories = load_categories()
    ols = Ols(offline=args.offline)
    try:
        rows = audit(paths, categories, ols)
    finally:
        ols.save()

    if args.apply:
        if not args.files:
            parser.error("--apply needs explicit files; it never sweeps the KB")
        print("\n".join(apply(rows, categories)))
        return 0

    shown = [r for r in rows if not args.status or r.status in args.status]
    if args.format == "tsv":
        print("file\tname\tmondo\tncit\tvia\tproposed\tcurrent\tstatus")
        for r in shown:
            print(
                f"{r.path.name}\t{r.name}\t{r.mondo}\t{' '.join(r.ncit)}\t{r.via}"
                f"\t{' | '.join(r.proposed)}\t{r.current}\t{r.status}"
            )
    else:
        counts = {s: sum(r.status == s for r in rows) for s in STATUSES}
        print(f"neoplasm entries assessed: {len(rows)}")
        for status in STATUSES:
            print(f"  {status:<11} {counts[status]}")
        wanted = args.status or (
            STATUSES if args.format == "list" else ("CONFLICT", "AMBIGUOUS", "MISSING")
        )
        for status in wanted:
            for r in rows:
                if r.status != status:
                    continue
                proposed = " | ".join(r.proposed) or "-"
                print(
                    f"{status:<10} {r.path.name}: proposed [{proposed}]"
                    f" via {r.via or '-'}; recorded [{r.current or '-'}]"
                )
    return 1 if args.strict and any(r.status == "CONFLICT" for r in rows) else 0


if __name__ == "__main__":
    sys.exit(main())
