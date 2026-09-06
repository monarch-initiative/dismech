#!/usr/bin/env python3
"""Compare a bound gene's ontology label against the gene the entry names (#10948).

`just validate-terms` checks that a `term.label` is HGNC's canonical label for
that `term.id`. Nothing checks that the resolved gene is the gene the entry says
the record is about, so a self-consistent binding to the wrong gene validates
clean::

    genetic:
    - name: THAP11
      gene_term:
        preferred_term: THAP11
        term:
          id: hgnc:20856      # THAP1 -- a different gene (DYT6 dystonia)
          label: THAP1        # ...and the label agrees with the CURIE

Both `linkml-validate` and `linkml-term-validator` pass that. An *inconsistent*
pair (`hgnc:20856` labelled `THAP11`) is caught, which is the perverse part:
filling `label:` in from the ontology, the careful thing to do, converts a caught
error into a silent one.

This script closes that by comparing the resolved label against the entry's own
free text -- the two fields sitting directly above the binding that nothing else
reads.

What it looks at
----------------
Every `GeneDescriptor` in the KB carrying an `hgnc:` term: `genetic[].gene_term`,
`has_subtypes[].genes[]`, `pathophysiology[].gene`, `genetic[].variants[].gene`,
`aso_details.target_gene`, `computational_models[].perturbations[]`.

The comparison text is the descriptor's own `preferred_term`, plus -- for
`gene_term` only -- the enclosing `genetic[]` entry's `name`. `name` is the gene's
identity there by convention; on a `Pathophysiology` or a `Variant` it names a
mechanism or an HGVS change, so a gene symbol appearing in it is incidental and
is not read as a claim about the binding.

Classification
--------------
`ok`
    The bound label is named in that text, as a whole symbol token.

`names_another_gene`
    The text does not name the bound gene, and *does* name a different symbol
    that some other binding in the KB has already resolved. This is the #10948
    shape at full confidence: two known genes, and the entry disagrees with its
    own binding about which one it means.

`symbol_unexplained`
    The text does not name the bound gene, and names no symbol this script can
    resolve. Advisory. Three things live here and offline they are
    indistinguishable:
      * a previous or alias symbol -- the OBO HGNC build lags live renames
        (#10102), so `GBA1` bound to `hgnc:4177` (`GBA`) is *correct*;
      * a protein or product name (`sucrase-isomaltase` for `SI`);
      * a genuinely wrong binding whose intended gene nothing has cached yet.
    `--resolve` separates the first from the last; see below.

Tolerated, and reported as counts rather than findings:

`ortholog_case`
    Matches case-insensitively only: the model-organism symbol convention
    (`Adnp`, `Pkhd1`, `smchd1`), including a zebrafish paralog's trailing letter
    (`inppl1a` for `INPPL1`).

`hla_serotype`
    An HLA locus with serotype detail appended -- `HLA-B27` bound to `HLA-B`.
    Allele-level detail in a gene field is legitimate (#9017). Deliberately
    restricted to `HLA-*`: a general "label plus digits" tolerance would excuse
    `THAP1` under a `THAP11` entry, which is the defect this exists to find.

`uncached`
    The CURIE is not in `cache/hgnc/terms.csv`, so there is no label to compare
    and this script has no opinion.

Order matters: `names_another_gene` is decided before the tolerances, so a
tolerance can never swallow a confident finding.

`--resolve`
-----------
Asks the configured HGNC adapter about the `symbol_unexplained` rows. Needs
network the first time (OAK downloads the build); not part of any gate.

For each row it takes the symbols the text names and asks two questions:
a symbol that is a *synonym of the bound term* explains the row and reclassifies
it `previous_symbol` (`GBA1` -> `GBA`); a symbol that resolves to a *different*
HGNC id promotes the row to `names_another_gene` (`THAP11` -> `hgnc:23194`,
which is how the issue's demonstration is caught definitively). A symbol the
build has never heard of leaves the row where it was: the OBO build does not
carry every retired symbol -- `WDR34` is absent from `hgnc:28296` (`DYNC2I2`)
entirely -- and "the ontology does not know this string" is not evidence about
the binding.

Reporting posture
-----------------
Advisory by default, and exits 0 even with findings, because it is new and its
real rate should be visible before anything blocks on it (#10948). `--strict`
exits 1 on `names_another_gene` only -- never on `symbol_unexplained`, which is
mostly renames.

Usage
-----
    python scripts/check_gene_term_identity.py             # report, exit 0
    python scripts/check_gene_term_identity.py --format tsv
    python scripts/check_gene_term_identity.py --resolve   # split the advisory bucket
    python scripts/check_gene_term_identity.py --strict    # exit 1 on confident findings
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Iterable, NamedTuple

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dismech.yaml_io import safe_load

DEFAULT_ROOTS = ("kb/disorders", "kb/modules", "kb/comorbidities", "kb/groupings")

#: Slots whose range is ``GeneDescriptor`` in ``src/dismech/schema/dismech.yaml``.
GENE_SLOTS = ("gene_term", "gene", "genes", "target_gene", "perturbations")

#: Slots where the enclosing mapping's ``name`` names the gene. Only
#: ``Genetic.name`` does; a ``Pathophysiology`` or ``Variant`` ``name`` describes
#: a mechanism or an HGVS change, so a symbol in it says nothing about the
#: binding and reading it would invent disagreements.
NAME_BEARING_SLOTS = frozenset({"gene_term"})

#: A gene-symbol-shaped run: letters/digits, with internal hyphens, dots or
#: apostrophes (``MT-TE``, ``HLA-DQ2.5``, ``C21orf2``).
TOKEN_RE = re.compile(r"[A-Za-z0-9]+(?:[-.'][A-Za-z0-9]+)*")

OK = "ok"
NAMES_ANOTHER_GENE = "names_another_gene"
SYMBOL_UNEXPLAINED = "symbol_unexplained"
PREVIOUS_SYMBOL = "previous_symbol"
ORTHOLOG_CASE = "ortholog_case"
HLA_SEROTYPE = "hla_serotype"
UNCACHED = "uncached"

#: Reported as findings. ``symbol_unexplained`` is advisory; only the first gates
#: under ``--strict``.
FINDING_CLASSES = (NAMES_ANOTHER_GENE, SYMBOL_UNEXPLAINED)


class Binding(NamedTuple):
    path: str
    slot: str
    curie: str
    curated_label: str
    preferred_term: str
    entry_name: str

    @property
    def texts(self) -> tuple[str, ...]:
        """The free text that names the gene, for this slot."""
        parts = [self.preferred_term]
        if self.slot in NAME_BEARING_SLOTS:
            parts.append(self.entry_name)
        return tuple(p for p in parts if p)

    @property
    def where(self) -> str:
        """Where in the file to look. The enclosing ``name`` is shown as context
        for slots that do not carry the gene's identity in it."""
        if self.slot in NAME_BEARING_SLOTS:
            return self.slot
        if self.entry_name:
            return f"{self.slot} under {self.entry_name!r}"
        return self.slot


class Finding(NamedTuple):
    binding: Binding
    verdict: str
    ontology_label: str
    #: Symbols the text names that resolve elsewhere, for ``names_another_gene``;
    #: the synonym that explains the row, for ``previous_symbol``.
    detail: tuple[str, ...] = ()


def load_hgnc_labels() -> dict[str, str]:
    """``hgnc:<id>`` -> canonical label, from the committed label cache."""
    labels: dict[str, str] = {}
    terms_csv = ROOT / "cache" / "hgnc" / "terms.csv"
    if not terms_csv.exists():
        return labels
    with terms_csv.open(encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            curie = (row.get("curie") or "").strip()
            label = (row.get("label") or "").strip()
            if curie and label:
                labels[curie.lower()] = label
    return labels


def index_by_label(labels: dict[str, str]) -> dict[str, set[str]]:
    """Canonical label -> the CURIE(s) carrying it.

    This is what makes the confident class possible offline: a symbol is
    recognizable only because some other entry in the KB has bound it, which is
    also the honest limit -- a wrong binding whose intended gene appears nowhere
    else in the KB cannot be promoted past ``symbol_unexplained``.
    """
    index: dict[str, set[str]] = {}
    for curie, label in labels.items():
        index.setdefault(label, set()).add(curie)
    return index


def iter_gene_bindings(data: Any, display: str) -> list[Binding]:
    found: list[Binding] = []

    def walk(node: Any) -> None:
        if isinstance(node, dict):
            enclosing = node.get("name")
            enclosing = enclosing if isinstance(enclosing, str) else ""
            for key, value in node.items():
                if key in GENE_SLOTS:
                    for descriptor in value if isinstance(value, list) else [value]:
                        if not isinstance(descriptor, dict):
                            continue
                        term = descriptor.get("term")
                        if not isinstance(term, dict) or not term.get("id"):
                            continue
                        preferred = descriptor.get("preferred_term")
                        found.append(
                            Binding(
                                path=display,
                                slot=key,
                                curie=str(term["id"]),
                                curated_label=str(term.get("label") or ""),
                                preferred_term=(
                                    preferred if isinstance(preferred, str) else ""
                                ),
                                entry_name=enclosing,
                            )
                        )
                walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(data)
    return found


def symbol_tokens(text: str) -> list[str]:
    return TOKEN_RE.findall(text)


def _matches_case_insensitively(label: str, token: str) -> bool:
    """The model-organism symbol convention, and zebrafish paralog suffixes.

    Mouse orthologs are title-cased (``Adnp``), zebrafish ones lower-cased and
    sometimes suffixed with a paralog letter (``inppl1a``). Neither is a
    disagreement about which gene is meant.
    """
    if token.lower() == label.lower():
        return True
    return (
        len(token) == len(label) + 1
        and token[-1].islower()
        and token[:-1].lower() == label.lower()
    )


def _is_hla_serotype(label: str, token: str) -> bool:
    """``HLA-B27`` under a binding to ``HLA-B``: allele-level detail (#9017).

    Restricted to the HLA loci on purpose. Generalizing it to "the label
    followed by digits" would tolerate ``THAP1`` under a ``THAP11`` entry, which
    is the exact defect #10948 was filed about.
    """
    if not label.startswith("HLA-") or not token.startswith(label):
        return False
    suffix = token[len(label) :]
    return bool(suffix) and all(ch.isdigit() or ch == "." for ch in suffix)


def classify(
    bindings: Iterable[Binding],
    labels: dict[str, str],
    by_label: dict[str, set[str]] | None = None,
) -> list[Finding]:
    """One verdict per binding, in source order."""
    if by_label is None:
        by_label = index_by_label(labels)
    results: list[Finding] = []
    for binding in bindings:
        curie = binding.curie.lower()
        label = labels.get(curie)
        if not label:
            results.append(Finding(binding, UNCACHED, ""))
            continue

        tokens = [t for text in binding.texts for t in symbol_tokens(text)]
        if label in tokens:
            results.append(Finding(binding, OK, label))
            continue

        # Before any tolerance: does the text name a *different* known gene?
        others = sorted(
            {t for t in tokens if t in by_label and curie not in by_label[t]}
        )
        if others:
            results.append(Finding(binding, NAMES_ANOTHER_GENE, label, tuple(others)))
            continue

        if any(_matches_case_insensitively(label, t) for t in tokens):
            results.append(Finding(binding, ORTHOLOG_CASE, label))
            continue
        if any(_is_hla_serotype(label, t) for t in tokens):
            results.append(Finding(binding, HLA_SEROTYPE, label))
            continue
        results.append(
            Finding(binding, SYMBOL_UNEXPLAINED, label, tuple(sorted(set(tokens))))
        )
    return results


def resolve_unexplained(
    findings: list[Finding], adapter_spec: str | None = None
) -> list[Finding]:
    """Ask HGNC about the advisory rows. Needs network on first use.

    A named symbol that is a synonym of the bound term explains the row; one that
    resolves to a different id condemns it. A symbol the build does not know
    leaves the row alone -- the OBO build carries only some retired symbols, so
    silence there is a fact about the build, not about the binding.
    """
    from oaklib import get_adapter

    if adapter_spec is None:
        conf = yaml.safe_load(
            (ROOT / "conf" / "oak_config.yaml").read_text(encoding="utf-8")
        )
        adapter_spec = conf["ontology_adapters"].get("hgnc") or "sqlite:obo:hgnc"
    adapter = get_adapter(adapter_spec)

    alias_cache: dict[str, set[str]] = {}
    symbol_cache: dict[str, set[str]] = {}

    def aliases(curie: str) -> set[str]:
        if curie not in alias_cache:
            try:
                alias_cache[curie] = {str(a) for a in adapter.entity_aliases(curie)}
            except Exception as exc:  # network/adapter trouble: say nothing
                print(f"  could not read aliases for {curie}: {exc}", file=sys.stderr)
                alias_cache[curie] = set()
        return alias_cache[curie]

    def resolve_symbol(symbol: str) -> set[str]:
        """CURIEs whose label or alias is exactly ``symbol``."""
        if symbol not in symbol_cache:
            hits: set[str] = set()
            try:
                for hit in adapter.basic_search(symbol):
                    candidate = str(hit)
                    # `basic_search` can match on more than the label, so confirm
                    # the string really is this entity's symbol before believing it.
                    if (
                        symbol in aliases(candidate)
                        or adapter.label(candidate) == symbol
                    ):
                        hits.add(candidate.lower())
            except Exception as exc:
                print(f"  could not resolve {symbol!r}: {exc}", file=sys.stderr)
            symbol_cache[symbol] = hits
        return symbol_cache[symbol]

    resolved: list[Finding] = []
    for finding in findings:
        if finding.verdict != SYMBOL_UNEXPLAINED:
            resolved.append(finding)
            continue
        curie = finding.binding.curie.lower()
        bound_aliases = aliases(finding.binding.curie)
        explained = [s for s in finding.detail if s in bound_aliases]
        if explained:
            resolved.append(
                Finding(
                    finding.binding,
                    PREVIOUS_SYMBOL,
                    finding.ontology_label,
                    tuple(explained),
                )
            )
            continue
        elsewhere = sorted(
            s
            for s in finding.detail
            if (hits := resolve_symbol(s)) and curie not in hits
        )
        if elsewhere:
            resolved.append(
                Finding(
                    finding.binding,
                    NAMES_ANOTHER_GENE,
                    finding.ontology_label,
                    tuple(elsewhere),
                )
            )
            continue
        resolved.append(finding)
    return resolved


def iter_yaml_files(paths: list[str]) -> list[Path]:
    if paths:
        files: list[Path] = []
        for raw in paths:
            path = Path(raw)
            files.extend(sorted(path.rglob("*.yaml")) if path.is_dir() else [path])
        return files
    files = []
    for root in DEFAULT_ROOTS:
        files.extend(sorted((ROOT / root).rglob("*.yaml")))
    return files


def _display(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def collect(paths: list[str]) -> list[Binding]:
    bindings: list[Binding] = []
    for path in iter_yaml_files(paths):
        try:
            data = safe_load(path.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError):
            continue
        if isinstance(data, (dict, list)):
            bindings.extend(iter_gene_bindings(data, _display(path)))
    return bindings


HEADLINE = {
    NAMES_ANOTHER_GENE: "names a different gene than it binds",
    SYMBOL_UNEXPLAINED: "binds a symbol the entry does not name",
}

EXPLAIN = {
    NAMES_ANOTHER_GENE: (
        "The entry's own text names a gene that resolves elsewhere in HGNC, and\n"
        "does not name the gene it binds. Check which one the disease is about;\n"
        "the label agreeing with the CURIE does not make the CURIE right (#10948)."
    ),
    SYMBOL_UNEXPLAINED: (
        "The bound gene's HGNC label is not named in the entry's text. Usually\n"
        "benign -- a previous symbol the OBO build has not caught up with\n"
        "(#10102), or a protein/product name -- but a wrong binding looks exactly\n"
        "like this too. `--resolve` separates a known previous symbol from the\n"
        "rest."
    ),
}


def print_report(findings: list[Finding], *, resolved: bool) -> None:
    counts = Counter(f.verdict for f in findings)
    total = len(findings)
    print(f"gene bindings with an HGNC term: {total}")
    print(f"  gene named by the entry            : {counts[OK]}")
    print(f"  NAMES A DIFFERENT GENE             : {counts[NAMES_ANOTHER_GENE]}")
    print(f"  symbol not named (advisory)        : {counts[SYMBOL_UNEXPLAINED]}")
    if resolved:
        print(f"  previous/alias symbol (benign)     : {counts[PREVIOUS_SYMBOL]}")
    print(f"  model-organism symbol case (benign): {counts[ORTHOLOG_CASE]}")
    print(f"  HLA serotype detail (benign)       : {counts[HLA_SEROTYPE]}")
    print(f"  CURIE not cached (no opinion)      : {counts[UNCACHED]}")

    for verdict in FINDING_CLASSES:
        rows = [f for f in findings if f.verdict == verdict]
        if not rows:
            continue
        print(f"\n{len(rows)} binding(s) that {HEADLINE[verdict]}.\n")
        print(EXPLAIN[verdict] + "\n")
        for finding in rows:
            binding = finding.binding
            print(f"  {binding.path}")
            print(f"     {binding.where}")
            print(f"     binding      : {binding.curie} -> {finding.ontology_label!r}")
            if binding.preferred_term:
                print(f"     preferred_term: {binding.preferred_term!r}")
            if binding.entry_name and binding.slot in NAME_BEARING_SLOTS:
                print(f"     name          : {binding.entry_name!r}")
            if verdict == NAMES_ANOTHER_GENE:
                print(f"     names instead : {', '.join(finding.detail)}")

    if counts[PREVIOUS_SYMBOL]:
        print(
            f"\n{counts[PREVIOUS_SYMBOL]} binding(s) use a previous or alias symbol "
            "HGNC still recognizes; these are correct bindings.\n"
        )
        for finding in findings:
            if finding.verdict != PREVIOUS_SYMBOL:
                continue
            print(
                f"  {finding.binding.path}: {', '.join(finding.detail)} -> "
                f"{finding.binding.curie} ({finding.ontology_label})"
            )


def print_tsv(findings: list[Finding]) -> None:
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(
        [
            "verdict",
            "file",
            "slot",
            "curie",
            "ontology_label",
            "curated_label",
            "preferred_term",
            "entry_name",
            "detail",
        ]
    )
    for f in findings:
        b = f.binding
        writer.writerow(
            [
                f.verdict,
                b.path,
                b.slot,
                b.curie,
                f.ontology_label,
                b.curated_label,
                b.preferred_term,
                b.entry_name if b.slot in NAME_BEARING_SLOTS else "",
                ",".join(f.detail),
            ]
        )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help=f"default: {', '.join(DEFAULT_ROOTS)}")
    parser.add_argument(
        "--format",
        choices=("report", "tsv"),
        default="report",
        help="report (default) or tsv of every binding",
    )
    parser.add_argument(
        "--findings-only",
        action="store_true",
        help="with --format tsv, emit only the two finding classes",
    )
    parser.add_argument(
        "--resolve",
        action="store_true",
        help="ask HGNC about the advisory rows (needs network; not for CI)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help=f"exit 1 on {NAMES_ANOTHER_GENE} findings (advisory otherwise)",
    )
    args = parser.parse_args(argv)

    findings = classify(collect(args.paths), load_hgnc_labels())
    if args.resolve:
        findings = resolve_unexplained(findings)

    if args.format == "tsv":
        print_tsv(
            [f for f in findings if f.verdict in FINDING_CLASSES]
            if args.findings_only
            else findings
        )
    else:
        print_report(findings, resolved=args.resolve)

    confident = sum(1 for f in findings if f.verdict == NAMES_ANOTHER_GENE)
    if args.strict and confident:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
