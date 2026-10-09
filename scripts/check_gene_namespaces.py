#!/usr/bin/env python3
"""Check where non-human gene identifiers may appear, and that NCBI Gene ones are real.

What the namespaces are for
---------------------------
A gene descriptor in dismech is bound to HGNC, which names human genes only.
That is right for a human disease's `genetic:` section and its pathophysiology
nodes, and wrong for a model system: a Coch knock-in mouse carries the mouse
gene, not `hgnc:2180`, and a zebrafish morphant knocks down `tmem165`, which
has no HGNC record at all. So `AnimalModel.genes` and `ExperimentalModel.genes`
take a `GeneOrProductDescriptor`, which also admits `NCBIGene:` (a non-human
gene) and `UniProtKB:` (a non-human gene product). Everywhere else stays HGNC.

The schema cannot say that by itself -- `GeneOrProductTerm` has no prefix
constraint, and neither does `GeneTerm` -- so this script is where the rule
lives.

What it gates on, and why each is a real defect
-----------------------------------------------
``NON_HUMAN_OUTSIDE_MODEL``
    An `NCBIGene:` or `UniProtKB:` binding anywhere except a model's `genes`.
    Those prefixes are admitted for naming a gene in a model's own species;
    anywhere else the claim is about human disease, and the gene is HGNC's.
``NCBIGENE_UNRESOLVED``
    An `NCBIGene:` identifier with no row in `cache/ncbigene/terms.csv`. The
    term validator cannot check this prefix: OAK's NCBI Gene adapter returns no
    label, and an unrouted prefix passes `just validate-terms` with any label at
    all. So this script is the check, and it is cache-first like the others.
    Run `just check-gene-namespaces-online` to resolve the identifier through
    NCBI E-utilities and write its row.
``NCBIGENE_LABEL_MISMATCH``
    An `NCBIGene:` identifier whose `label` is not the official symbol NCBI
    records for it (`Coch` for NCBIGene:12810).
``NCBIGENE_RETIRED``
    Online only: NCBI reports the record discontinued or replaced. Bind the
    current identifier instead.
``NCBIGENE_HUMAN``
    Online only: the identifier is a human gene (taxon 9606). A human gene is
    `hgnc:` everywhere, including in a model system.

`UniProtKB:` labels need no check here: that prefix is routed through OAK's
`uniprot:` adapter in conf/oak_config.yaml, so `just validate-terms` checks it.

What it reports without gating
------------------------------
``UNCHECKED_PREFIX``
    A model gene bound to some other prefix (`MGI:` today). Nothing resolves
    those, so the label is unchecked. Listed with `--format list`; rebinding
    to `NCBIGene:` makes them checkable.

Usage
-----
    python scripts/check_gene_namespaces.py                       # gate
    python scripts/check_gene_namespaces.py kb/disorders/X.yaml
    python scripts/check_gene_namespaces.py --format list         # also the advisory rows
    python scripts/check_gene_namespaces.py --online              # resolve uncached NCBIGene IDs
"""

from __future__ import annotations

import argparse
import csv
import os
import sys
from collections import Counter
from datetime import UTC, datetime
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

MODEL_SECTIONS = ("animal_models", "experimental_models")
NON_HUMAN_PREFIXES = ("NCBIGene:", "UniProtKB:")
MODEL_GENE_PREFIXES = ("hgnc:", *NON_HUMAN_PREFIXES)
HUMAN_TAXON = "9606"
GATING = (
    "NON_HUMAN_OUTSIDE_MODEL",
    "NCBIGENE_UNRESOLVED",
    "NCBIGENE_LABEL_MISMATCH",
    "NCBIGENE_RETIRED",
    "NCBIGENE_HUMAN",
)

NCBIGENE_CACHE = ROOT / "cache" / "ncbigene" / "terms.csv"
ESUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"


def load_ncbigene_cache(path: Path = NCBIGENE_CACHE) -> dict[str, str]:
    """CURIE -> official symbol, from the committed cache."""
    if not path.exists():
        return {}
    with path.open(newline="", encoding="utf-8") as handle:
        return {row["curie"]: row["label"] for row in csv.DictReader(handle)}


def fetch_ncbigene(curies: list[str]) -> dict[str, tuple[str | None, str | None]]:
    """Ask NCBI E-utilities for each gene's official symbol.

    Returns CURIE -> (symbol, problem). `problem` is set when NCBI has no live
    record (unknown, discontinued, or replaced) or the record is a human gene.
    """
    import requests

    ids = [c.split(":", 1)[1] for c in curies]
    params = {"db": "gene", "id": ",".join(ids), "retmode": "json"}
    if os.environ.get("NCBI_API_KEY"):
        params["api_key"] = os.environ["NCBI_API_KEY"]
    response = requests.get(ESUMMARY_URL, params=params, timeout=60)
    response.raise_for_status()
    result = response.json().get("result", {})
    out: dict[str, tuple[str | None, str | None]] = {}
    for curie, gene_id in zip(curies, ids, strict=True):
        record = result.get(gene_id)
        if not record or record.get("error"):
            out[curie] = (None, "NCBI has no record for this ID")
        elif record.get("currentid"):
            out[curie] = (record.get("name"), f"replaced by NCBIGene:{record['currentid']}")
        elif str(record.get("status", "")) not in ("", "0"):
            out[curie] = (record.get("name"), f"discontinued (status {record.get('status')})")
        elif str((record.get("organism") or {}).get("taxid", "")) == HUMAN_TAXON:
            out[curie] = (record.get("name"), "human gene; bind it to hgnc: instead")
        else:
            out[curie] = (record.get("name"), None)
    return out


def write_ncbigene_cache(rows: dict[str, str], path: Path = NCBIGENE_CACHE) -> None:
    """Add rows to the cache, keeping existing rows and their timestamps."""
    existing: dict[str, tuple[str, str]] = {}
    if path.exists():
        with path.open(newline="", encoding="utf-8") as handle:
            existing = {r["curie"]: (r["label"], r["retrieved_at"]) for r in csv.DictReader(handle)}
    now = datetime.now(UTC).replace(tzinfo=None).isoformat()
    for curie, label in rows.items():
        if existing.get(curie, (None,))[0] != label:
            existing[curie] = (label, now)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["curie", "label", "retrieved_at"])
        for curie in sorted(existing):
            writer.writerow([curie, *existing[curie]])


class Finding:
    __slots__ = ("detail", "kind", "location", "path")

    def __init__(self, path: Path, location: str, kind: str, detail: str) -> None:
        self.path = path
        self.location = location
        self.kind = kind
        self.detail = detail


def _model_genes(data: object) -> list[tuple[str, dict]]:
    """(location, descriptor) for every gene on an animal or experimental model."""
    out: list[tuple[str, dict]] = []
    if not isinstance(data, dict):
        return out
    for section in MODEL_SECTIONS:
        for index, model in enumerate(data.get(section) or []):
            if not isinstance(model, dict):
                continue
            label = model.get("name") or index
            for gene_index, gene in enumerate(model.get("genes") or []):
                if isinstance(gene, dict):
                    out.append((f"{section}[{label}].genes[{gene_index}]", gene))
    return out


def _bindings(node: object, path: str = "", seen: set[int] | None = None) -> list[tuple[str, dict]]:
    """(location, term) for every `term: {id: ...}` mapping in the document.

    A YAML anchor makes one mapping reachable from two places; `seen` keeps the
    check from reporting it twice.
    """
    seen = set() if seen is None else seen
    found: list[tuple[str, dict]] = []
    if isinstance(node, dict):
        if id(node) in seen:
            return found
        seen.add(id(node))
        term = node.get("term")
        if isinstance(term, dict) and term.get("id"):
            found.append((path, node))
        for key, value in node.items():
            found.extend(_bindings(value, f"{path}.{key}" if path else str(key), seen))
    elif isinstance(node, list):
        for index, item in enumerate(node):
            name = item.get("name") if isinstance(item, dict) else None
            found.extend(_bindings(item, f"{path}[{name if name else index}]", seen))
    return found


def check_document(path: Path, data: object, ncbigene: dict[str, str] | None = None) -> list[Finding]:
    findings: list[Finding] = []
    ncbigene = {} if ncbigene is None else ncbigene
    model_genes = _model_genes(data)
    allowed = {id(gene) for _, gene in model_genes}

    for location, descriptor in _bindings(data):
        curie = str(descriptor["term"]["id"])
        if curie.startswith(NON_HUMAN_PREFIXES) and id(descriptor) not in allowed:
            findings.append(
                Finding(path, location, "NON_HUMAN_OUTSIDE_MODEL",
                        f"{curie} is only admitted on animal_models[].genes or experimental_models[].genes")
            )

    for location, gene in model_genes:
        term = gene.get("term") or {}
        curie = term.get("id")
        if not curie:
            continue
        curie = str(curie)
        if not curie.startswith(MODEL_GENE_PREFIXES):
            findings.append(
                Finding(path, location, "UNCHECKED_PREFIX",
                        f"{curie}: no resolver checks this prefix; NCBIGene: would be checkable")
            )
        elif curie.startswith("NCBIGene:"):
            if curie not in ncbigene:
                findings.append(
                    Finding(path, location, "NCBIGENE_UNRESOLVED",
                            f"{curie} is not in cache/ncbigene/terms.csv; run just check-gene-namespaces-online")
                )
            elif term.get("label") != ncbigene[curie]:
                findings.append(
                    Finding(path, location, "NCBIGENE_LABEL_MISMATCH",
                            f"{curie} label {term.get('label')!r}, NCBI official symbol {ncbigene[curie]!r}")
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


def _load(path: Path) -> object | None:
    try:
        return safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:  # malformed YAML is check-duplicate-keys' job
        print(f"{_display(path)}: could not parse ({exc})", file=sys.stderr)
        return None


def resolve_online(paths: list[Path] | None = None) -> list[Finding]:
    """Fetch every NCBIGene identifier the KB uses that the cache lacks."""
    explicit = {p.resolve() for p in paths} if paths else set()
    cache = load_ncbigene_cache()
    wanted: dict[str, Path] = {}
    for path in _files(explicit):
        for _, descriptor in _bindings(_load(path)):
            curie = str(descriptor["term"]["id"])
            if curie.startswith("NCBIGene:"):
                wanted.setdefault(curie, path)
    missing = sorted(c for c in wanted if c not in cache)
    findings: list[Finding] = []
    resolved: dict[str, str] = {}
    for start in range(0, len(missing), 200):
        for curie, (symbol, problem) in fetch_ncbigene(missing[start:start + 200]).items():
            if problem and problem.startswith("human gene"):
                findings.append(Finding(wanted[curie], curie, "NCBIGENE_HUMAN", problem))
            elif problem:
                findings.append(Finding(wanted[curie], curie, "NCBIGENE_RETIRED", problem))
            elif symbol:
                resolved[curie] = symbol
    if resolved:
        write_ncbigene_cache(resolved)
        print(f"cache/ncbigene/terms.csv: added {len(resolved)} row(s)")
    return findings


def scan_repo(paths: list[Path] | None = None) -> list[Finding]:
    explicit = {p.resolve() for p in paths} if paths else set()
    ncbigene = load_ncbigene_cache()
    findings: list[Finding] = []
    for path in _files(explicit):
        data = _load(path)
        if data is not None:
            findings.extend(check_document(path, data, ncbigene))
    return findings


def main() -> int:
    # One walk, no second pass, so the parsed-KB cache is pure cost here.
    kb_cache.default_off()

    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="*", help="YAML files to check (default: all)")
    parser.add_argument(
        "--format",
        choices=("summary", "list"),
        default="summary",
        help="summary prints gating findings plus counts; list also prints the advisory rows",
    )
    parser.add_argument(
        "--online",
        action="store_true",
        help="first resolve uncached NCBIGene identifiers through NCBI E-utilities and cache them",
    )
    args = parser.parse_args()

    paths = [Path(p) for p in args.paths] or None
    findings = resolve_online(paths) if args.online else []
    findings += scan_repo(paths)
    counts = Counter(f.kind for f in findings)
    failures = [f for f in findings if f.kind in GATING]

    shown = findings if args.format == "list" else failures
    for finding in sorted(shown, key=lambda f: (f.kind, str(f.path), f.location)):
        print(f"{finding.kind}: {_display(finding.path)}: {finding.location}: {finding.detail}")

    summary = ", ".join(f"{kind}={counts[kind]}" for kind in sorted(counts)) or "none"
    print(f"\ngene namespace census: {summary}")

    if failures:
        print(f"\n{len(failures)} gating finding(s). See the module docstring for why each is a defect.")
        return 1
    print("OK: every NCBIGene/UniProtKB binding is on a model gene, and every NCBIGene binding is cached and correctly labelled.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
