"""Apply the node-class tree to every pathophysiology node in the KB.

This is the executable half of the pathograph node-classification design
(``kb/node_classes/pathograph_node_classes.txt``). It reads the hand-built
GO-term seed table, walks ``kb/``, and assigns each pathophysiology node a
class at tier level — or flags it as a **debundle candidate** when its own
annotations disagree with each other.

Nothing here writes to ``kb/``; the tree and seed table are read-only inputs.
A node a curator has classified carries ``node_class``, and that value wins;
for every other node the result is a suggestion. The output is a worklist and
a measurement, deliberately kept reproducible so the numbers in the design doc
can be re-derived rather than trusted.

How a node is classified
------------------------
Rules are tried in order, and the first that fires wins. Each carries its own
confidence, because they are not equally trustworthy — the measurements behind
them are in the design doc:

0. **Curated ``node_class``** → the tier that value sits under (``CURATED``).
1. **GO biological_process, seeded, HIGH confidence.** Exactly one class among
   the node's HIGH-confidence seeded BP terms → that class (``HIGH``).
2. **GO biological_process, conflicting.** More than one class → ``CONFLICT``.
   This is the signal, not a failure: a node whose own annotations span two
   classes is making two claims.
3. **GO molecular_function present** → ``ACTIVITY`` (``MEDIUM``). This rule
   was ``HIGH`` until 2026-11 on the evidence that 91% of MF-bearing nodes
   carry the curator's ``MOLECULAR`` scale tag. That evidence cannot test it:
   ``MOLECULAR`` spans the GENOMIC, ACTIVITY, SUBSTANCE and PATHWAY tiers
   alike. The independent test is conformance, and the rule failed it: once
   ~3,000 nodes carried an MF term, the ``conforms_to`` pairs it decided
   disagreed 133 times in 232 (57%), against 7.4% for pairs decided by seeded
   GO BP terms on both sides. Most of those are lesion nodes such as
   ``Germline PTEN Loss of Function``, annotated with the wild-type activity
   of the affected gene, which says what the gene does rather than what kind
   of claim the node makes.
4. **CHEBI present** → ``SUBSTANCE`` (``MEDIUM``).
5. **Gene present** → ``GENOMIC`` (``LOW``). Deliberately low: a gene
   annotation does not distinguish a genomic lesion from a broken molecular
   activity, and those are different tiers.
6. **UBERON without CL** → ``TISSUE`` (``LOW``).
7. **CL present** → ``CELLULAR`` (``LOW``).

A node matching none of these is left unclassified rather than guessed at.

Known limitation: rule 1 beats rule 3, so a node carrying both a seeded BP term
and a GO MF term is classified from the BP term. That is sometimes visibly
wrong — ``ACADSB molecular function deficiency`` carries ``GO:0006550
L-isoleucine catabolic process`` (SUBSTANCE) and ``GO:0003995 acyl-CoA
dehydrogenase activity`` (ACTIVITY), and the node name says which one it means.
**Do not "fix" this by promoting MF above BP.** That was tested: 252 nodes carry
both, and moving MF first *lowers* conformance agreement from 90.0% to 87.3%,
because MF is frequently a secondary annotation on a node that really is about
the process. Discriminating these two needs more than slot presence, and is
unsolved.
"""

from __future__ import annotations

import csv
import sys
from collections import Counter
from collections.abc import Iterable, Iterator
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from dismech.conformance import iter_conforms_to
from dismech.node_classes import node_class_tiers

DEFAULT_SEED = Path("kb/node_classes/pathograph_node_class_go_seed.tsv")
DEFAULT_KB_DIRS = (Path("kb/disorders"), Path("kb/modules"))

CONFLICT = "CONFLICT"

#: The scanner's label for each tier of the generated ``node_class`` enum. The
#: seed table uses the same labels.
TIER_LABELS = {
    "GENOMIC_EFFECT": "GENOMIC",
    "ENVIRONMENTAL_EFFECT": "ENVIRONMENTAL",
    "MOLECULAR_ACTIVITY_EFFECT": "ACTIVITY",
    "MOLECULAR_SUBSTANCE_EFFECT": "SUBSTANCE",
    "PATHWAY_EFFECT": "PATHWAY",
    "CELLULAR_EFFECT": "CELLULAR",
    "TISSUE_ORGAN_EFFECT": "TISSUE",
    "SYSTEMIC_EFFECT": "SYSTEMIC",
    "OUTCOME": "OUTCOME",
    "DISPOSITION": "DISPOSITION",
}

#: ``biological_scale`` values compatible with each tier, for ``--format
#: scale``. Two tiers span two scales because BiologicalScaleEnum's own
#: descriptions split them: it files a chemical that accumulates under
#: MOLECULAR and a chronically elevated metabolite under ORGANISM, and kinase
#: activity under MOLECULAR but intracellular signalling under CELLULAR. An
#: outcome can be a tissue transformation or a patient-level endpoint. A tier
#: absent here (an exposure, a disposition) can sit at any scale.
TIER_SCALES = {
    "GENOMIC": frozenset({"MOLECULAR"}),
    "ACTIVITY": frozenset({"MOLECULAR"}),
    "SUBSTANCE": frozenset({"MOLECULAR", "ORGANISM"}),
    "PATHWAY": frozenset({"MOLECULAR", "CELLULAR"}),
    "CELLULAR": frozenset({"CELLULAR"}),
    "TISSUE": frozenset({"TISSUE"}),
    "SYSTEMIC": frozenset({"ORGANISM"}),
    "OUTCOME": frozenset({"TISSUE", "ORGANISM"}),
}
#: Classes whose compatible scales differ from their tier's: a single failing
#: organ is TISSUE in BiologicalScaleEnum's terms.
CLASS_SCALES = {"ORGAN_FAILURE": frozenset({"TISSUE", "ORGANISM"})}

#: Rule confidences, weakest first. A conformance pair is only as trustworthy
#: as its weaker side, so the gate compares ranks rather than names. CURATED is
#: a class a curator recorded in ``node_class``, above every term-based rule.
CONFIDENCE_RANK = {"NONE": 0, "LOW": 1, "MEDIUM": 2, "HIGH": 3, "CURATED": 4}


@dataclass(frozen=True)
class Assignment:
    """One node's class and how it was reached.

    ``detail`` holds the curated value for a ``curated`` assignment and the
    clashing classes for a conflict; ``scale`` is the node's own
    ``biological_scale``, empty when it has none.
    """

    disease: str
    node: str
    node_class: str | None
    basis: str
    confidence: str
    detail: str = ""
    scale: str = ""

    @property
    def is_conflict(self) -> bool:
        return self.node_class == CONFLICT


@dataclass
class ScanResult:
    assignments: list[Assignment] = field(default_factory=list)
    #: (disease, node) -> assignment, for conformance lookups
    index: dict[tuple[str, str], Assignment] = field(default_factory=dict)
    #: (disease, node) -> every "module#Node Name" the node conforms to
    conforms_to: dict[tuple[str, str], list[str]] = field(default_factory=dict)


def load_seed(path: Path = DEFAULT_SEED) -> dict[str, tuple[str, str]]:
    """Read the GO-term seed table into ``{go_id: (class, confidence)}``."""
    seed: dict[str, tuple[str, str]] = {}
    with Path(path).open(encoding="utf-8") as fh:
        for line in fh:
            if line.startswith(("#", "go_id")) or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 5:
                raise ValueError(f"malformed seed row: {line!r}")
            seed[parts[0]] = (parts[2], parts[3])
    return seed


def _term_ids(node: dict[str, Any], slot: str) -> list[str]:
    out = []
    for item in node.get(slot) or []:
        term = (item or {}).get("term") or {}
        if term.get("id"):
            out.append(str(term["id"]))
    return out


def classify_node(node: dict[str, Any], seed: dict[str, tuple[str, str]]) -> Assignment:
    """Assign one pathophysiology node a class. See module docstring."""
    name = str(node.get("name", ""))
    curated = node.get("node_class")
    tier = node_class_tiers().get(str(curated)) if curated else None
    if tier is not None:
        return Assignment("", name, TIER_LABELS[tier], "curated", "CURATED", str(curated))

    bp = _term_ids(node, "biological_processes")
    hits = {seed[c][0] for c in bp if c in seed and seed[c][1] == "HIGH"}

    if len(hits) == 1:
        return Assignment("", name, next(iter(hits)), "go_bp", "HIGH")
    if len(hits) > 1:
        return Assignment(
            "", name, CONFLICT, "go_bp", "HIGH", " + ".join(sorted(hits))
        )
    if _term_ids(node, "molecular_functions"):
        return Assignment("", name, "ACTIVITY", "go_mf", "MEDIUM")
    if _term_ids(node, "chemical_entities"):
        return Assignment("", name, "SUBSTANCE", "chebi", "MEDIUM")
    if node.get("genes") or node.get("gene"):
        return Assignment("", name, "GENOMIC", "gene", "LOW")
    has_cl = bool(_term_ids(node, "cell_types"))
    if _term_ids(node, "locations") and not has_cl:
        return Assignment("", name, "TISSUE", "uberon", "LOW")
    if has_cl:
        return Assignment("", name, "CELLULAR", "cl", "LOW")
    return Assignment("", name, None, "none", "NONE")


def scan(
    kb_dirs: Iterable[Path] = DEFAULT_KB_DIRS,
    seed_path: Path = DEFAULT_SEED,
) -> ScanResult:
    """Classify every pathophysiology node under the given KB directories."""
    from dismech.yaml_io import safe_load

    seed = load_seed(seed_path)
    result = ScanResult()
    for kb_dir in kb_dirs:
        for path in sorted(Path(kb_dir).glob("*.yaml")):
            try:
                data = safe_load(path.read_text(encoding="utf-8"))
            except Exception:  # a malformed KB file is not this tool's business
                continue
            for node in (data or {}).get("pathophysiology") or []:
                if not isinstance(node, dict):
                    continue
                base = classify_node(node, seed)
                assignment = Assignment(
                    disease=path.stem,
                    node=base.node,
                    node_class=base.node_class,
                    basis=base.basis,
                    confidence=base.confidence,
                    detail=base.detail,
                    scale=str(node.get("biological_scale") or ""),
                )
                result.assignments.append(assignment)
                result.index[(path.stem, assignment.node)] = assignment
                refs = [ref for ref in iter_conforms_to(node) if "#" in ref]
                if refs:
                    result.conforms_to[(path.stem, assignment.node)] = refs
    return result


def conformance_pairs(
    result: ScanResult, *, high_only: bool = True
) -> list[tuple[Assignment, Assignment, str]]:
    """Resolvable ``conforms_to`` pairs where both sides carry a class.

    ``high_only`` keeps only pairs where *both* classes are curated or came from
    a HIGH confidence rule (a seeded GO BP term). That gate matters: pairs with a
    MEDIUM or LOW side disagree several times more often than pairs where both
    sides are HIGH, so the fallback rules contribute mostly noise here. Run
    ``--format conformance-gates`` for the current numbers rather than quoting
    a figure from this docstring, which the KB's growth will outdate.
    """
    out = []
    pairs = [
        (key, ref)
        for key, refs in sorted(result.conforms_to.items())
        for ref in refs
    ]
    for key, ref in pairs:
        module_id, _, module_node = ref.partition("#")
        target = result.index.get((module_id.strip(), module_node.strip()))
        source = result.index[key]
        if target is None:
            continue
        if not target.node_class or not source.node_class:
            continue
        if CONFLICT in (target.node_class, source.node_class):
            continue
        if high_only and _weakest((source, target, ref)) < CONFIDENCE_RANK["HIGH"]:
            continue
        out.append((source, target, ref))
    return out


def _weakest(pair: tuple[Assignment, Assignment, str]) -> int:
    """Rank of the less trustworthy side of a conformance pair."""
    return min(CONFIDENCE_RANK.get(a.confidence, 0) for a in pair[:2])


def conformance_mismatches(
    result: ScanResult, *, high_only: bool = True
) -> list[tuple[Assignment, str, str, str]]:
    """Disorder nodes whose class differs from the module node they conform to.

    A conforming node is curated as the same *kind* of thing as its module
    target, by a process entirely independent of this classification — which is
    what makes the agreement rate a genuine check on the classes rather than a
    restatement of them. Where they differ, either the mapping is wrong or one
    of the two nodes is bundled.

    Returns ``(assignment, reference, module_class, disorder_class)``.
    """
    return [
        (source, ref, target.node_class or "", source.node_class or "")
        for source, target, ref in conformance_pairs(result, high_only=high_only)
        if source.node_class != target.node_class
    ]


def conformance_gate_table(result: ScanResult) -> list[tuple[str, int, int]]:
    """Mismatch rate under each confidence gate, as ``(label, bad, total)``.

    The gate is the finding, not a knob: the fallback rules are useful for
    coverage and useless for adjudication, and this table is what says so. A
    pair is filed under its *weaker* side, so each row measures one confidence
    level. Every row is derived from the same pair list the ``conformance``
    format prints, so the numbers quoted in the spec can be re-derived rather
    than taken on trust.
    """
    every = conformance_pairs(result, high_only=False)
    by_rank: dict[int, list[tuple[Assignment, Assignment, str]]] = {}
    for pair in every:
        by_rank.setdefault(_weakest(pair), []).append(pair)

    def bad(pairs: list[tuple[Assignment, Assignment, str]]) -> int:
        return sum(1 for src, tgt, _ in pairs if src.node_class != tgt.node_class)

    rows = [
        ("both sides curated (node_class)", "CURATED"),
        ("weakest side HIGH (seeded GO BP)", "HIGH"),
        ("weakest side MEDIUM (GO MF or CHEBI)", "MEDIUM"),
        ("weakest side LOW (gene, UBERON or CL)", "LOW"),
    ]
    table = []
    for label, level in rows:
        pairs = by_rank.get(CONFIDENCE_RANK[level], [])
        table.append((label, bad(pairs), len(pairs)))
    table.append(("all pairs", bad(every), len(every)))
    return table


def scale_disagreements(result: ScanResult) -> list[tuple[Assignment, frozenset[str]]]:
    """Curated nodes whose ``node_class`` tier and ``biological_scale`` disagree.

    Report-only. Both slots are curated, so a disagreement is a question rather
    than a defect: one of the two is wrong, or the node describes one thing at
    two scales and is bundling two claims. Nodes classified only by the term
    rules are not checked; their tier is a suggestion. Returns ``(assignment,
    compatible scales)``.
    """
    rows = []
    for a in result.assignments:
        if a.basis != "curated" or not a.scale:
            continue
        expected = CLASS_SCALES.get(a.detail) or TIER_SCALES.get(a.node_class or "")
        if expected is not None and a.scale not in expected:
            rows.append((a, expected))
    return rows


def summarize(result: ScanResult) -> dict[str, Any]:
    total = len(result.assignments)
    classes = Counter(
        a.node_class for a in result.assignments if a.node_class and not a.is_conflict
    )
    bases = Counter(a.basis for a in result.assignments)
    conflicts = sum(1 for a in result.assignments if a.is_conflict)
    unclassified = sum(1 for a in result.assignments if a.node_class is None)
    return {
        "total": total,
        "classified": total - conflicts - unclassified,
        "conflicts": conflicts,
        "unclassified": unclassified,
        "classes": classes,
        "bases": bases,
    }


def _iter_tsv(result: ScanResult) -> Iterator[list[str]]:
    yield ["disease", "node", "class", "basis", "confidence", "detail"]
    for a in result.assignments:
        yield [
            a.disease,
            a.node,
            a.node_class or "",
            a.basis,
            a.confidence,
            a.detail,
        ]


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(
        prog="python -m dismech.node_class_scan",
        description="Apply the candidate node-class tree across kb/.",
    )
    parser.add_argument(
        "--format",
        choices=("summary", "tsv", "debundle", "conformance", "conformance-gates", "scale"),
        default="summary",
    )
    parser.add_argument("--seed", default=str(DEFAULT_SEED))
    parser.add_argument(
        "--include-low",
        action="store_true",
        help="conformance: also compare pairs where a side was classified by a "
        "MEDIUM or LOW rule (mostly noise; --format conformance-gates gives "
        "the rate at each level)",
    )
    parser.add_argument(
        "--kb-dir",
        action="append",
        default=None,
        help="repeatable; default: kb/disorders and kb/modules",
    )
    args = parser.parse_args(argv)

    kb_dirs = [Path(d) for d in (args.kb_dir or [str(d) for d in DEFAULT_KB_DIRS])]
    missing = [d for d in kb_dirs if not d.is_dir()]
    if missing:
        print("error: not a directory: " + ", ".join(map(str, missing)), file=sys.stderr)
        return 2
    if not Path(args.seed).is_file():
        print(f"error: no seed table at {args.seed}", file=sys.stderr)
        return 2

    result = scan(kb_dirs, Path(args.seed))

    if args.format == "tsv":
        writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
        writer.writerows(_iter_tsv(result))
        return 0

    if args.format == "scale":
        rows = scale_disagreements(result)
        for a, expected in rows:
            print(
                f"{a.detail:30s} scale {a.scale:9s} (expected "
                f"{'|'.join(sorted(expected))})  {a.node}  [{a.disease}]"
            )
        curated = [a for a in result.assignments if a.basis == "curated"]
        both = sum(1 for a in curated if a.scale)
        print(
            f"\n{len(curated)} nodes carry node_class, {both} of them also "
            f"biological_scale; {len(rows)} disagree (report-only)",
            file=sys.stderr,
        )
        return 0

    if args.format == "debundle":
        rows = [a for a in result.assignments if a.is_conflict]
        for a in rows:
            print(f"{a.detail:24s} {a.node}  [{a.disease}]")
        print(f"\n{len(rows)} debundle candidates", file=sys.stderr)
        return 0

    if args.format == "conformance-gates":
        for label, bad, total in conformance_gate_table(result):
            pct = f"{100 * bad / total:5.1f}%" if total else "     -"
            print(f"{label:42s} {pct}  ({bad}/{total})")
        return 0

    if args.format == "conformance":
        rows = conformance_mismatches(result, high_only=not args.include_low)
        for a, ref, module_class, disorder_class in rows:
            print(f"{disorder_class:10s} != {module_class:10s}  {a.node}  [{a.disease}]")
            print(f"{'':24s}conforms_to {ref}")
        checked = len(conformance_pairs(result, high_only=not args.include_low))
        gate = "all-confidence" if args.include_low else "both-sides-HIGH"
        pct = 100 * len(rows) / checked if checked else 0.0
        print(
            f"\n{len(rows)}/{checked} ({pct:.1f}%) class mismatches "
            f"over {gate} conforms_to pairs",
            file=sys.stderr,
        )
        return 0

    s = summarize(result)
    total = s["total"] or 1
    print(f"pathophysiology nodes      {s['total']}")
    print(f"  classified               {s['classified']:6d}  ({100*s['classified']/total:.1f}%)")
    print(f"  debundle candidates      {s['conflicts']:6d}  ({100*s['conflicts']/total:.1f}%)")
    print(f"  unclassified             {s['unclassified']:6d}  ({100*s['unclassified']/total:.1f}%)")
    print("\nby class:")
    for name, n in s["classes"].most_common():
        print(f"  {name:12s} {n:6d}  ({100*n/s['classified']:.1f}%)")
    print("\nby rule that fired:")
    for name, n in s["bases"].most_common():
        print(f"  {name:12s} {n:6d}  ({100*n/total:.1f}%)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
