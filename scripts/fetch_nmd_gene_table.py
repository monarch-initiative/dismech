"""Transcribe the Gene Table of Neuromuscular Disorders into a dismech gene-classification collection.

The Gene Table (https://musclegenetable.fr/) is a gene catalogue maintained by
Gisele Bonne and Francois Rivier and published annually in *Neuromuscular
Disorders*. Its rows are genes; its 17 disease groups are the filing system.

Each gene row carries an "All allelic disease phenotypes" column in which every
phenotype is followed by its coordinates in the table, written ``<group>.<entry>``.
A gene's group membership is therefore the set of leading group numbers across
that column -- which is set-valued, because a gene appears once per clinically
distinct allelic presentation. TTN spans six groups on exactly this basis.

Writes ``kb/gene_classifications/nmd_gene_table.yaml``. Regenerate rather than
hand-editing the output::

    uv run python scripts/fetch_nmd_gene_table.py

Gene symbols are resolved to HGNC identifiers from the HGNC complete set, which
also supplies previous and alias symbols so that a gene the table still lists
under an older symbol resolves to its current identifier rather than being
dropped.
"""

from __future__ import annotations

import argparse
import csv
import datetime
import html
import io
import re
import string
import sys
import urllib.request
from pathlib import Path

import yaml

GENE_TABLE_BASE = "https://musclegenetable.fr"
GENE_TABLE_HOME = f"{GENE_TABLE_BASE}/index.html"
HGNC_COMPLETE_SET = "https://storage.googleapis.com/public-download-files/hgnc/tsv/tsv/hgnc_complete_set.txt"
OUTPUT_PATH = Path("kb/gene_classifications/nmd_gene_table.yaml")

#: Group number -> permissible value of ``GeneTableNMDGroupEnum``. The order and
#: names are the table's own; see src/dismech/schema/classifications/gene_table_nmd.yaml.
GROUPS = {
    1: "muscular_dystrophies",
    2: "congenital_muscular_dystrophies",
    3: "congenital_myopathies",
    4: "distal_myopathies",
    5: "other_myopathies",
    6: "myotonic_syndromes",
    7: "ion_channel_muscle_diseases",
    8: "malignant_hyperthermia",
    9: "metabolic_myopathies",
    10: "hereditary_cardiomyopathies",
    11: "congenital_myasthenic_syndromes",
    12: "spinal_muscular_atrophies_motoneuron_diseases",
    13: "hereditary_ataxias",
    14: "hereditary_motor_and_sensory_neuropathies",
    15: "hereditary_paraplegias",
    16: "mitochondrial_myopathies",
    17: "other_neuromuscular_disorders",
}

_ROW_RE = re.compile(r"<tr[^>]*>(.*?)</tr>", re.S | re.I)
_CELL_RE = re.compile(r"<t[dh][^>]*>(.*?)</t[dh]>", re.S | re.I)
_TAG_RE = re.compile(r"<[^>]+>")
#: The gene cell renders as "<symbol><protein name>" with no separator, e.g.
#: "TTNTitin" or "ATP13A2ATPase type 13A2". The symbol boundary is not reliably
#: findable by pattern -- "ATP13A2AT" is a perfectly plausible-looking symbol --
#: so candidates are cut here and resolved by longest-prefix match against HGNC.
_CANDIDATE_RE = re.compile(r"^([A-Z][A-Za-z0-9orf\-]{0,24})")
#: Longest HGNC symbol worth trying as a prefix.
_MAX_SYMBOL_LEN = 15
_COORD_RE = re.compile(r"(\d{1,2})\.\d+")
#: "GT_NMD 2026 (updated 18/05/2026)"
_VERSION_RE = re.compile(r"(GT_NMD\s+\d{4})\s*\(updated\s+(\d{2})/(\d{2})/(\d{4})\)")


def _fetch(url: str, timeout: int = 120) -> str:
    with urllib.request.urlopen(url, timeout=timeout) as response:
        return response.read().decode("utf-8", "replace")


def _cells(row_html: str) -> list[str]:
    return [
        html.unescape(_TAG_RE.sub("", cell)).strip()
        for cell in _CELL_RE.findall(row_html)
    ]


def source_version(home_html: str) -> tuple[str | None, str | None]:
    """Return the table's own version string and its "current as of" date."""
    match = _VERSION_RE.search(html.unescape(_TAG_RE.sub(" ", home_html)))
    if not match:
        return None, None
    version, day, month, year = match.groups()
    return re.sub(r"\s+", " ", version), f"{year}-{month}-{day}"


def scrape_gene_groups() -> dict[str, set[int]]:
    """Scrape candidate gene text -> set of group numbers from the gene table.

    Keys are the raw leading run of the gene cell (symbol plus however much of
    the protein name ran together with it); :func:`resolve_symbol` cuts them
    down to a real symbol.
    """
    gene_groups: dict[str, set[int]] = {}
    for letter in string.ascii_uppercase:
        page = _fetch(f"{GENE_TABLE_BASE}/4DACTION/GS/{letter}")
        for row_html in _ROW_RE.findall(page):
            cells = _cells(row_html)
            if len(cells) < 3:
                continue
            candidate_match = _CANDIDATE_RE.match(cells[0])
            if not candidate_match:
                continue
            groups = {int(g) for g in _COORD_RE.findall(cells[2])}
            groups &= set(GROUPS)
            if groups:
                gene_groups.setdefault(candidate_match.group(1), set()).update(groups)
    if not gene_groups:
        raise RuntimeError(
            "scraped no genes from the gene table; the site layout has probably changed"
        )
    return gene_groups


def resolve_symbol(
    candidate: str,
    approved: dict[str, tuple[str, str]],
    secondary: dict[str, tuple[str, str]],
) -> tuple[str, tuple[str, str]] | None:
    """Resolve a run-together gene cell to ``(symbol, (hgnc_curie, approved_symbol))``.

    Two passes, approved symbols first and only then previous/alias symbols.
    Within each pass the longest prefix wins, so "CACNA1SCalcium" resolves to
    CACNA1S rather than stopping at a shorter symbol that is also a prefix.

    The pass ordering matters more than it looks: a *longer* prefix will
    sometimes collide with some unrelated gene's retired symbol. Resolving
    "LAMB2Laminin, beta 2" by length alone yields LAMB2L, an alias of the
    pseudogene LAMB2P1, instead of LAMB2; and "ARAndrogen receptor" yields ARA,
    an alias of ABCC6, instead of AR. Preferring an approved symbol at any
    length over an alias at a longer one gets both right.
    """
    upper = candidate.upper()
    for index in (approved, secondary):
        for end in range(min(len(upper), _MAX_SYMBOL_LEN), 0, -1):
            resolved = index.get(upper[:end])
            if resolved is not None:
                return candidate[:end], resolved
    return None


def hgnc_symbol_index() -> tuple[
    dict[str, tuple[str, str]], dict[str, tuple[str, str]]
]:
    """Return (approved-symbol index, previous/alias-symbol index).

    Each maps an uppercased symbol to ``(hgnc_curie, approved_symbol)``. The two
    are kept separate so an approved symbol always wins over another gene's
    retired one.
    """
    text = _fetch(HGNC_COMPLETE_SET, timeout=300)
    approved: dict[str, tuple[str, str]] = {}
    secondary: dict[str, tuple[str, str]] = {}
    reader = csv.DictReader(io.StringIO(text), delimiter="\t")
    for record in reader:
        if record.get("status") != "Approved":
            continue
        # A disease-gene catalogue never cites a pseudogene, but pseudogene
        # aliases do collide with real symbols under prefix matching.
        if (record.get("locus_group") or "").strip() == "pseudogene":
            continue
        hgnc_id = (record.get("hgnc_id") or "").strip()
        symbol = (record.get("symbol") or "").strip()
        if not hgnc_id.startswith("HGNC:") or not symbol:
            continue
        # dismech uses the lowercase `hgnc:` prefix; see CLAUDE.md.
        entry = (hgnc_id.replace("HGNC:", "hgnc:"), symbol)
        approved[symbol.upper()] = entry
        for field in ("prev_symbol", "alias_symbol"):
            for alias in (record.get(field) or "").split("|"):
                alias = alias.strip().upper()
                if alias and alias not in secondary:
                    secondary[alias] = entry
    return approved, secondary


def build_collection(
    gene_groups: dict[str, set[int]],
    approved: dict[str, tuple[str, str]],
    secondary: dict[str, tuple[str, str]],
    version: str | None,
    current_as_of: str | None,
    retrieved: str,
) -> tuple[dict, list[str]]:
    merged: dict[str, dict] = {}
    unresolved: list[str] = []
    for candidate in sorted(gene_groups):
        resolution = resolve_symbol(candidate, approved, secondary)
        if resolution is None:
            unresolved.append(candidate)
            continue
        source_symbol, (curie, approved_symbol) = resolution
        entry = merged.setdefault(
            curie,
            {
                "approved_symbol": approved_symbol,
                "source_symbol": source_symbol,
                "groups": set(),
            },
        )
        entry["groups"].update(gene_groups[candidate])

    rows: list[dict] = []
    for curie in sorted(merged, key=lambda c: merged[c]["approved_symbol"]):
        entry = merged[curie]
        approved_symbol = entry["approved_symbol"]
        row: dict = {
            "gene": {
                "preferred_term": approved_symbol,
                "term": {"id": curie, "label": approved_symbol},
            },
            "values": [GROUPS[g] for g in sorted(entry["groups"])],
        }
        if entry["source_symbol"] != approved_symbol:
            row["source_label"] = entry["source_symbol"]
        rows.append(row)

    collection = {
        "name": "Gene Table of Neuromuscular Disorders (nuclear genome)",
        "description": (
            "Transcription of the Gene Table of Neuromuscular Disorders: which genes the "
            "table lists, and which of its 17 disease groups each gene appears in. A gene "
            "carries one value per clinically distinct allelic presentation, so membership "
            "is set-valued. Generated by scripts/fetch_nmd_gene_table.py; regenerate rather "
            "than hand-editing."
        ),
        "classification_system": "GENE_TABLE_NMD",
        "source_url": GENE_TABLE_HOME,
        "retrieved_date": retrieved,
        "genes": rows,
    }
    if version:
        collection["source_version"] = version
    if current_as_of:
        collection["source_content_current_as_of"] = current_as_of
    if unresolved:
        collection["notes"] = (
            "Symbols the HGNC complete set does not resolve as an approved, previous, or "
            "alias symbol, and which are therefore omitted: "
            + ", ".join(unresolved)
            + "."
        )
    # Key order: metadata first, then the gene rows.
    ordered_keys = [
        "name",
        "description",
        "classification_system",
        "source_url",
        "source_version",
        "source_content_current_as_of",
        "retrieved_date",
        "notes",
        "genes",
    ]
    return {k: collection[k] for k in ordered_keys if k in collection}, unresolved


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=OUTPUT_PATH,
        help=f"output path (default {OUTPUT_PATH})",
    )
    parser.add_argument(
        "--retrieved-date",
        default=datetime.date.today().isoformat(),
        help="retrieval date to record (default: today)",
    )
    args = parser.parse_args(argv)

    print("Fetching gene table version...", file=sys.stderr)
    version, current_as_of = source_version(_fetch(GENE_TABLE_HOME))
    print(
        f"  {version or 'unknown version'} (current as of {current_as_of or 'unknown'})",
        file=sys.stderr,
    )

    print("Scraping gene table A-Z...", file=sys.stderr)
    gene_groups = scrape_gene_groups()
    print(f"  {len(gene_groups)} genes", file=sys.stderr)

    print("Fetching HGNC complete set...", file=sys.stderr)
    approved, secondary = hgnc_symbol_index()
    print(
        f"  {len(approved)} approved symbols, {len(secondary)} previous/alias",
        file=sys.stderr,
    )

    collection, unresolved = build_collection(
        gene_groups, approved, secondary, version, current_as_of, args.retrieved_date
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        yaml.safe_dump(
            collection, handle, sort_keys=False, allow_unicode=True, width=100
        )

    print(f"Wrote {len(collection['genes'])} genes to {args.output}", file=sys.stderr)
    if unresolved:
        print(
            f"  {len(unresolved)} unresolved and omitted: {', '.join(unresolved)}",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
