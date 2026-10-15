#!/usr/bin/env python3
"""Check which gene namespace a model or dataset uses, and that its identifiers are real.

What the namespaces are for
---------------------------
A gene descriptor in dismech is bound to HGNC, which names human genes only.
That is right for a human disease's `genetic:` section and its pathophysiology
nodes, and wrong for a model system: a Coch knock-in mouse carries the mouse
gene, not `hgnc:2180`, and a zebrafish morphant knocks down `tmem165`, which
has no HGNC record at all. So the `genes` of an `AnimalModel`, an
`ExperimentalModel` and a `Dataset` take a `GeneOrProductDescriptor`, which
admits a gene in its own species. Everywhere else stays HGNC.

The order of preference
-----------------------
1. ``hgnc:`` for a human gene, including a human transgene or a human cell line.
2. The species' **Alliance of Genome Resources** member database, where one
   exists: ``MGI:`` mouse, ``RGD:`` rat, ``ZFIN:`` zebrafish, ``Xenbase:``
   Xenopus, ``FB:`` Drosophila, ``WB:`` C. elegans, ``SGD:`` yeast. This holds
   whether the model acts on the gene or on its product.
3. Otherwise ``NCBIGene:`` (pig, dog, macaque), or ``UniProtKB:`` for a gene
   product.

This matches the Monarch KG, where the MOD identifier is the gene node and NCBI
Gene is ingested only for species without one. It is deliberately *not* the
Biolink `id_prefixes` order or Translator node normalization, both of which put
NCBIGene first. Prefix spellings are Biolink's, which the Monarch KG and GO
also use; GO's `MGI:MGI:` local-ID form and Bioregistry's `FlyBase`/`WormBase`
spellings are rejected.

The schema cannot say any of this by itself -- `GeneOrProductTerm` has no
prefix constraint, and neither does `GeneTerm` -- so this script is where the
rule lives.

What it gates on, and why each is a real defect
-----------------------------------------------
``NON_HUMAN_OUTSIDE_MODEL``
    A MOD, `NCBIGene:` or `UniProtKB:` binding anywhere except the `genes` of a
    model or dataset. Anywhere else the claim is about human disease, and the
    gene is HGNC's.
``MALFORMED_ID``
    A MOD identifier with the wrong prefix spelling (`XENBASE:`, `FlyBase:`) or
    local-ID shape (`MGI:MGI:1278313`, `ZFIN:tmem165`).
``UNRESOLVED``
    A MOD or `NCBIGene:` identifier with no row in its `cache/<prefix>/terms.csv`.
    The term validator cannot check these prefixes -- none is routed in
    conf/oak_config.yaml, and an unrouted prefix passes `just validate-terms`
    with any label at all -- so this script is the check, and it is cache-first
    like the others. Run `just check-gene-namespaces-online` to resolve the
    identifier and write its row.
``LABEL_MISMATCH``
    A MOD or `NCBIGene:` identifier whose `label` is not the official symbol
    (`Coch` for MGI:1278313). This is the defect that matters most: a wrong
    identifier carrying the right gene's symbol reads correctly to every human
    reviewer.
``MOD_PREFERRED``
    An `NCBIGene:` or `UniProtKB:` binding for a species that has a MOD. Offline
    this fires when the model or dataset records its `organism`; online it also
    fires from the taxon the record itself reports, which covers animal models
    (whose `species` is free text).
``RETIRED``
    Online only: the source reports the record discontinued, replaced, or
    inactive. Bind the current identifier instead.
``HUMAN_GENE``
    Online only: an `NCBIGene:` or `UniProtKB:` record for a human gene
    (taxon 9606). A human gene is `hgnc:` everywhere, including in a model.

`UniProtKB:` labels are not checked here: that prefix is routed through OAK's
`uniprot:` adapter, so `just validate-terms` checks them. This script checks
its species online.

What it reports without gating
------------------------------
``UNCHECKED_PREFIX``
    A model gene bound to some other prefix. Nothing resolves it.
``HGNC_IN_MOD_ORGANISM``
    An `hgnc:` gene on a model or dataset whose `organism` has a MOD. Usually
    the human ortholog standing in for the model's own gene, which should be
    rebound; sometimes a genuine human transgene, which is correct. Listed with
    `--format list` as a worklist.

Usage
-----
    python scripts/check_gene_namespaces.py                       # gate
    python scripts/check_gene_namespaces.py kb/disorders/X.yaml
    python scripts/check_gene_namespaces.py --format list         # also the advisory rows
    python scripts/check_gene_namespaces.py --online              # resolve uncached identifiers first
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys
import time
from collections import Counter
from dataclasses import dataclass
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

GENE_SECTIONS = ("animal_models", "experimental_models", "datasets")
HUMAN_TAXON = "9606"


@dataclass(frozen=True)
class Mod:
    prefix: str
    name: str
    local_id: re.Pattern[str]
    taxa: frozenset[str]


# The Alliance of Genome Resources members, in Biolink's prefix spelling. The
# taxa are the NCBITaxon ids the Alliance (and so the Monarch KG) files each
# MOD's genes under.
MODS: dict[str, Mod] = {
    mod.prefix: mod
    for mod in (
        Mod("MGI", "Mouse Genome Informatics", re.compile(r"\d+"), frozenset({"10090"})),
        Mod("RGD", "Rat Genome Database", re.compile(r"\d+"), frozenset({"10116"})),
        Mod("ZFIN", "Zebrafish Information Network", re.compile(r"ZDB-GENE-\d+-\d+"), frozenset({"7955"})),
        Mod("Xenbase", "Xenbase", re.compile(r"XB-GENE-\d+"), frozenset({"8355", "8364"})),
        Mod("FB", "FlyBase", re.compile(r"FBgn\d{7}"), frozenset({"7227"})),
        Mod("WB", "WormBase", re.compile(r"WBGene\d{8}"), frozenset({"6239"})),
        Mod("SGD", "Saccharomyces Genome Database", re.compile(r"S\d{9}"), frozenset({"559292", "4932"})),
    )
}
MOD_FOR_TAXON = {taxon: mod for mod in MODS.values() for taxon in mod.taxa}
# Spellings other resources use for the same databases, which a curator may copy.
MISSPELLINGS = {
    **{prefix.casefold(): prefix for prefix in MODS},
    "flybase": "FB",
    "wormbase": "WB",
}

FALLBACK_PREFIXES = ("NCBIGene", "UniProtKB")
NON_HUMAN_PREFIXES = (*MODS, *FALLBACK_PREFIXES)
CACHED_PREFIXES = (*MODS, "NCBIGene")
MODEL_GENE_PREFIXES = ("hgnc", *NON_HUMAN_PREFIXES)

GATING = (
    "NON_HUMAN_OUTSIDE_MODEL",
    "MALFORMED_ID",
    "UNRESOLVED",
    "LABEL_MISMATCH",
    "MOD_PREFERRED",
    "RETIRED",
    "HUMAN_GENE",
)

ESUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
ALLIANCE_GENE_URL = "https://www.alliancegenome.org/api/gene/{curie}"
UNIPROT_ENTRY_URL = "https://rest.uniprot.org/uniprotkb/{accession}.json"


def _prefix(curie: str) -> str:
    return curie.split(":", 1)[0]


def cache_path(prefix: str) -> Path:
    return ROOT / "cache" / prefix.lower() / "terms.csv"


def load_cache(prefix: str, path: Path | None = None) -> dict[str, str]:
    """CURIE -> official symbol, from the committed cache for one prefix."""
    path = cache_path(prefix) if path is None else path
    if not path.exists():
        return {}
    with path.open(newline="", encoding="utf-8") as handle:
        return {row["curie"]: row["label"] for row in csv.DictReader(handle)}


def load_caches() -> dict[str, str]:
    labels: dict[str, str] = {}
    for prefix in CACHED_PREFIXES:
        labels.update(load_cache(prefix))
    return labels


def write_cache(prefix: str, rows: dict[str, str], path: Path | None = None) -> None:
    """Add rows to one prefix's cache, keeping existing rows and their timestamps."""
    path = cache_path(prefix) if path is None else path
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


def _taxon_problem(taxon: str) -> tuple[str, str] | None:
    """(kind, detail) when a fallback-prefix record belongs to a species it should not."""
    if taxon == HUMAN_TAXON:
        return "HUMAN_GENE", "human gene; bind it to hgnc: instead"
    if taxon in MOD_FOR_TAXON:
        mod = MOD_FOR_TAXON[taxon]
        return "MOD_PREFERRED", f"taxon {taxon} has a MOD; bind its {mod.prefix}: identifier ({mod.name}) instead"
    return None


def fetch_ncbigene(curies: list[str]) -> dict[str, tuple[str | None, tuple[str, str] | None]]:
    """Ask NCBI E-utilities for each gene's official symbol.

    Returns CURIE -> (symbol, problem), where problem is (kind, detail) when
    NCBI has no live record, or the record is a human or MOD-species gene.
    """
    import requests

    ids = [c.split(":", 1)[1] for c in curies]
    params = {"db": "gene", "id": ",".join(ids), "retmode": "json"}
    if os.environ.get("NCBI_API_KEY"):
        params["api_key"] = os.environ["NCBI_API_KEY"]
    response = requests.get(ESUMMARY_URL, params=params, timeout=60)
    response.raise_for_status()
    result = response.json().get("result", {})
    out: dict[str, tuple[str | None, tuple[str, str] | None]] = {}
    for curie, gene_id in zip(curies, ids, strict=True):
        record = result.get(gene_id)
        if not record or record.get("error"):
            out[curie] = (None, ("UNRESOLVED", "NCBI has no record for this ID"))
        elif record.get("currentid"):
            out[curie] = (record.get("name"), ("RETIRED", f"replaced by NCBIGene:{record['currentid']}"))
        elif str(record.get("status", "")) not in ("", "0"):
            out[curie] = (record.get("name"), ("RETIRED", f"discontinued (status {record.get('status')})"))
        else:
            taxon = str((record.get("organism") or {}).get("taxid", ""))
            out[curie] = (record.get("name"), _taxon_problem(taxon))
    return out


def fetch_mod(curie: str) -> tuple[str | None, tuple[str, str] | None]:
    """Ask the Alliance API for a MOD gene's official symbol.

    The Alliance is where the MODs publish, and the Monarch KG builds its gene
    nodes from the same Alliance files, so the two agree on labels.
    """
    import requests

    response = requests.get(ALLIANCE_GENE_URL.format(curie=curie), timeout=60)
    if response.status_code in (400, 404):
        return None, ("UNRESOLVED", "the Alliance has no gene record for this ID")
    response.raise_for_status()
    gene = response.json().get("gene") or {}
    if gene.get("obsolete"):
        return None, ("RETIRED", "the Alliance reports this gene record obsolete")
    symbol = (gene.get("geneSymbol") or {}).get("displayText")
    taxon = (gene.get("taxon") or {}).get("curie", "").removeprefix("NCBITaxon:")
    if taxon and taxon not in MODS[_prefix(curie)].taxa:
        return symbol, ("UNRESOLVED", f"the Alliance files this gene under taxon {taxon}")
    if not symbol:
        return None, ("UNRESOLVED", "the Alliance record has no gene symbol")
    return symbol, None


def fetch_uniprot(curie: str) -> tuple[str, str] | None:
    """Ask UniProt whether an accession is live and which species it belongs to."""
    import requests

    accession = curie.split(":", 1)[1]
    response = requests.get(UNIPROT_ENTRY_URL.format(accession=accession), timeout=60)
    if response.status_code in (400, 404):
        return "UNRESOLVED", "UniProt has no entry for this accession"
    response.raise_for_status()
    entry = response.json()
    if str(entry.get("entryType", "")).casefold() == "inactive":
        return "RETIRED", "UniProt reports this entry inactive"
    return _taxon_problem(str((entry.get("organism") or {}).get("taxonId", "")))


class Finding:
    __slots__ = ("detail", "kind", "location", "path")

    def __init__(self, path: Path, location: str, kind: str, detail: str) -> None:
        self.path = path
        self.location = location
        self.kind = kind
        self.detail = detail


def _organism_taxon(record: dict) -> str | None:
    term = (record.get("organism") or {}).get("term") or {}
    curie = str(term.get("id") or "")
    return curie.removeprefix("NCBITaxon:") if curie.startswith("NCBITaxon:") else None


def _model_genes(data: object) -> list[tuple[str, dict, str | None]]:
    """(location, descriptor, organism taxon) for every gene on a model or dataset."""
    out: list[tuple[str, dict, str | None]] = []
    if not isinstance(data, dict):
        return out
    for section in GENE_SECTIONS:
        for index, record in enumerate(data.get(section) or []):
            if not isinstance(record, dict):
                continue
            label = record.get("name") or record.get("accession") or index
            taxon = _organism_taxon(record)
            for gene_index, gene in enumerate(record.get("genes") or []):
                if isinstance(gene, dict):
                    out.append((f"{section}[{label}].genes[{gene_index}]", gene, taxon))
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


def _malformed(curie: str) -> str | None:
    prefix, _, local = curie.partition(":")
    canonical = MISSPELLINGS.get(prefix.casefold())
    if canonical is None:
        return None
    if prefix != canonical:
        return f"{curie}: write the prefix as {canonical}:"
    if not MODS[canonical].local_id.fullmatch(local):
        return f"{curie}: a {canonical} gene identifier looks like {canonical}:{MODS[canonical].local_id.pattern}"
    return None


def check_document(path: Path, data: object, labels: dict[str, str] | None = None) -> list[Finding]:
    findings: list[Finding] = []
    labels = {} if labels is None else labels
    model_genes = _model_genes(data)
    allowed = {id(gene) for _, gene, _ in model_genes}

    for location, descriptor in _bindings(data):
        curie = str(descriptor["term"]["id"])
        prefix = _prefix(curie)
        if (prefix in NON_HUMAN_PREFIXES or prefix.casefold() in MISSPELLINGS) and id(descriptor) not in allowed:
            findings.append(
                Finding(path, location, "NON_HUMAN_OUTSIDE_MODEL",
                        f"{curie} is only admitted on the genes of an animal model, experimental model or dataset")
            )

    for location, gene, taxon in model_genes:
        term = gene.get("term") or {}
        curie = term.get("id")
        if not curie:
            continue
        curie = str(curie)
        prefix = _prefix(curie)
        mod = MOD_FOR_TAXON.get(taxon or "")

        if problem := _malformed(curie):
            findings.append(Finding(path, location, "MALFORMED_ID", problem))
            continue
        if prefix not in MODEL_GENE_PREFIXES:
            findings.append(
                Finding(path, location, "UNCHECKED_PREFIX", f"{curie}: no resolver checks this prefix")
            )
            continue
        if prefix == "hgnc":
            if mod:
                findings.append(
                    Finding(path, location, "HGNC_IN_MOD_ORGANISM",
                            f"{curie} on a taxon {taxon} record; unless this is a human transgene, "
                            f"bind the {mod.prefix}: gene")
                )
            continue
        if prefix in FALLBACK_PREFIXES and mod:
            findings.append(
                Finding(path, location, "MOD_PREFERRED",
                        f"{curie} on a taxon {taxon} record; bind its {mod.prefix}: identifier ({mod.name}) instead")
            )
        if prefix in CACHED_PREFIXES:
            if curie not in labels:
                findings.append(
                    Finding(path, location, "UNRESOLVED",
                            f"{curie} is not in cache/{prefix.lower()}/terms.csv; run just check-gene-namespaces-online")
                )
            elif term.get("label") != labels[curie]:
                findings.append(
                    Finding(path, location, "LABEL_MISMATCH",
                            f"{curie} label {term.get('label')!r}, official symbol {labels[curie]!r}")
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
    """Resolve every uncached MOD and NCBIGene identifier, and every UniProtKB one.

    A record that resolves cleanly gets a cache row. One that does not (retired,
    human, a MOD species on a fallback prefix) is reported and never cached, so
    the offline gate keeps failing on it as UNRESOLVED.
    """
    explicit = {p.resolve() for p in paths} if paths else set()
    labels = load_caches()
    wanted: dict[str, Path] = {}
    for path in _files(explicit):
        for _, gene, _ in _model_genes(_load(path)):
            curie = str((gene.get("term") or {}).get("id") or "")
            if _prefix(curie) in NON_HUMAN_PREFIXES and not _malformed(curie):
                wanted.setdefault(curie, path)

    findings: list[Finding] = []
    resolved: dict[str, dict[str, str]] = {}

    def record(curie: str, symbol: str | None, problem: tuple[str, str] | None) -> None:
        if problem:
            findings.append(Finding(wanted[curie], curie, *problem))
        elif symbol:
            resolved.setdefault(_prefix(curie), {})[curie] = symbol

    ncbigene = sorted(c for c in wanted if _prefix(c) == "NCBIGene" and c not in labels)
    for start in range(0, len(ncbigene), 200):
        for curie, (symbol, problem) in fetch_ncbigene(ncbigene[start:start + 200]).items():
            record(curie, symbol, problem)
    for curie in sorted(c for c in wanted if _prefix(c) in MODS and c not in labels):
        record(curie, *fetch_mod(curie))
        time.sleep(0.2)
    for curie in sorted(c for c in wanted if _prefix(c) == "UniProtKB"):
        record(curie, None, fetch_uniprot(curie))
        time.sleep(0.2)

    for prefix, rows in sorted(resolved.items()):
        write_cache(prefix, rows)
        print(f"cache/{prefix.lower()}/terms.csv: added or updated {len(rows)} row(s)")
    return findings


def scan_repo(paths: list[Path] | None = None) -> list[Finding]:
    explicit = {p.resolve() for p in paths} if paths else set()
    labels = load_caches()
    findings: list[Finding] = []
    for path in _files(explicit):
        data = _load(path)
        if data is not None:
            findings.extend(check_document(path, data, labels))
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
        help="first resolve uncached identifiers (Alliance API, NCBI E-utilities, UniProt) and cache them",
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
    print("OK: every non-human gene binding is on a model or dataset, uses its species' MOD where one "
          "exists, and every MOD and NCBIGene binding is cached and correctly labelled.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
