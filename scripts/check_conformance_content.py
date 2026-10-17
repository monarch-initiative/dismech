#!/usr/bin/env python3
"""Report what a ``conforms_to`` link claims but nothing checks: the content.

A disorder node declares ``conforms_to: "module_stem#Node Name"`` to say it is
an organ-specific instance of a shared mechanism. Two things are already
enforced about that string, and neither of them looks at the node:

* ``groupings.module_node_names`` checks the anchor **resolves** -- the module
  file exists and carries a pathophysiology node of that name.
* ``check_entity_refs`` / ``check_causal_targets`` guard the *other* reference
  grammars, which ``conforms_to`` does not use.

What nobody checks is CLAUDE.md's own statement of the contract: *"If a node
declares conforms_to, it should include the expected biological processes and
causal edges from the module."* So a node can name an anchor it has nothing in
common with, and every gate passes. Across the corpus a little over half of
conforming nodes share no ontology term with the module node they claim.

That is **not** automatically a defect, which is why this script exits 0. The
four classes below have genuinely different causes, and three of them are
routinely correct:

``process_absent``
    The module node binds at least one GO process or molecular function and the
    conforming node binds none of them. Sometimes this is the real finding --
    an anchor picked by name, or a node that drifted after the module was
    written. Often it is legitimate: the module node binds a generic process
    (``GO:0006915`` apoptotic process) and the conformer binds the specific one
    its disease runs, which is the same substitution the primer asks for on
    cell types. The script cannot tell those apart without an ontology walk,
    and deliberately does not guess -- see *Why there is no closure check*.

``anchor_no_process``
    The module node binds no GO term at all, so there is nothing to compare.
    A judgement node (an outcome, a disposition) legitimately carries none.
    Reported separately so it never reads as agreement.

``cell_type_absent``
    The module node binds a cell type and the conforming node binds none.
    This is the organ-specific substitution the conformance model is *for*
    (module says ``fibroblast``, conformer says ``hepatic stellate cell``), so
    a conformer with no cell type at all has skipped the step that carries most
    of the module's value. Orthogonal to the process classes: a link can share
    a process and still land here.

``edges_absent``
    The module node has ``downstream`` edges and the conforming node has none,
    so the conformer took the node and dropped the chain it sits in. Also
    orthogonal.

Why there is no closure check
-----------------------------
The tempting fix is to accept a conformer whose term is a GO descendant of the
module's. That needs the 200 MB ``go.db`` build, which ``conf/oak_config.yaml``
deliberately routes around (issue #5160), and it would turn a report that runs
in seconds offline into one that cannot run in CI at all. The committed
``cache/closure/`` exists for exactly this and currently holds the HP and GO
terms the *grouping* criteria cite, not the module nodes' -- extending it is the
right way to make this stricter, and is left as a follow-up rather than
smuggled in behind a download.

Read the per-module ranking, not the corpus total. A module whose conformers
almost all share its terms is being used as intended; one where almost none do
is either anchored too generically or being cited as a label. ``--strict``
exists for whoever decides to gate a subset later; it is not wired into
``just qc``.
"""

from __future__ import annotations

import argparse
import os
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dismech import kb_cache

#: Sections whose entries may carry ``conforms_to``.
SCAN_DIRS = ("kb/disorders", "kb/comorbidities", "kb/modules")

#: Descriptor slots whose ``term.id`` counts as an ontology process binding.
PROCESS_SLOTS = ("biological_processes", "molecular_functions")

CLASSES = ("process_absent", "anchor_no_process", "cell_type_absent", "edges_absent")


@dataclass(frozen=True)
class Finding:
    path: str
    node: str
    anchor: str
    kind: str
    detail: str

    @property
    def module(self) -> str:
        return self.anchor.split("#", 1)[0]


def _term_ids(node: dict, slots: tuple[str, ...]) -> set[str]:
    out: set[str] = set()
    for slot in slots:
        for item in node.get(slot) or []:
            if not isinstance(item, dict):
                continue
            term = item.get("term")
            if isinstance(term, dict) and term.get("id"):
                out.add(str(term["id"]))
    return out


def _labels(node: dict, slots: tuple[str, ...]) -> list[str]:
    out: list[str] = []
    for slot in slots:
        for item in node.get(slot) or []:
            if not isinstance(item, dict):
                continue
            term = item.get("term")
            if isinstance(term, dict) and term.get("id"):
                out.append(f"{term['id']} {term.get('label') or ''}".strip())
    return out


def module_index(modules_dir: Path) -> dict[str, dict]:
    """Map ``stem#Node Name`` to the module node's comparable content."""
    index: dict[str, dict] = {}
    for path in sorted(modules_dir.glob("*.yaml")):
        doc = kb_cache.load_document(path)
        if not isinstance(doc, dict):
            continue
        stem = path.stem
        for node in doc.get("pathophysiology") or []:
            if not isinstance(node, dict) or not node.get("name"):
                continue
            index[f"{stem}#{node['name']}"] = {
                "processes": _term_ids(node, PROCESS_SLOTS),
                "process_labels": _labels(node, PROCESS_SLOTS),
                "cell_types": _term_ids(node, ("cell_types",)),
                "edges": len(node.get("downstream") or []),
            }
    return index


def iter_links(paths: list[Path]):
    """Yield ``(path, node, anchor)`` for every declared conformance link."""
    for path in paths:
        doc = kb_cache.load_document(path)
        if not isinstance(doc, dict):
            continue
        rel = os.path.relpath(path, ROOT)
        for node in doc.get("pathophysiology") or []:
            if not isinstance(node, dict):
                continue
            raw = node.get("conforms_to")
            if not raw:
                continue
            anchors = raw if isinstance(raw, list) else [raw]
            for anchor in anchors:
                if isinstance(anchor, str) and "#" in anchor:
                    yield rel, node, anchor


def assess(path: str, node: dict, anchor: str, index: dict[str, dict]) -> list[Finding]:
    """Classify one conformance link. Returns [] when it agrees on everything."""
    target = index.get(anchor)
    name = str(node.get("name") or "<unnamed>")
    if target is None:
        # The anchor is already a foreign key elsewhere; say so rather than
        # silently scoring it as agreement.
        return [
            Finding(path, name, anchor, "unresolvable", "anchor names no module node")
        ]

    found: list[Finding] = []
    mine = _term_ids(node, PROCESS_SLOTS)
    if not target["processes"]:
        found.append(
            Finding(
                path, name, anchor, "anchor_no_process", "module node binds no GO term"
            )
        )
    elif not (target["processes"] & mine):
        want = ", ".join(sorted(target["process_labels"])) or "-"
        got = ", ".join(sorted(_labels(node, PROCESS_SLOTS))) or "none"
        found.append(
            Finding(
                path, name, anchor, "process_absent", f"module: {want} | node: {got}"
            )
        )

    if target["cell_types"] and not _term_ids(node, ("cell_types",)):
        found.append(
            Finding(
                path,
                name,
                anchor,
                "cell_type_absent",
                f"module binds {len(target['cell_types'])} cell type(s), node binds none",
            )
        )

    if target["edges"] and not (node.get("downstream") or []):
        found.append(
            Finding(
                path,
                name,
                anchor,
                "edges_absent",
                f"module node has {target['edges']} downstream edge(s), node has none",
            )
        )
    return found


def collect(
    paths: list[Path], index: dict[str, dict]
) -> tuple[list[Finding], int, Counter]:
    """Assess every link in one pass, counting links per module as we go.

    The per-module total is accumulated here rather than by re-walking, because
    the parsed-document cache is off (see ``main``) and a second walk would
    re-parse the corpus.
    """
    findings: list[Finding] = []
    per_module_links: Counter = Counter()
    links = 0
    for path, node, anchor in iter_links(paths):
        links += 1
        per_module_links[anchor.split("#", 1)[0]] += 1
        findings.extend(assess(path, node, anchor, index))
    return findings, links, per_module_links


def resolve_paths(args_files: list[str]) -> list[Path]:
    if args_files:
        return [Path(f).resolve() for f in args_files]
    out: list[Path] = []
    for rel in SCAN_DIRS:
        out.extend(sorted((ROOT / rel).glob("*.yaml")))
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Report conforms_to links whose content does not match the module node.",
    )
    parser.add_argument(
        "files", nargs="*", help="Specific KB files (default: whole KB)."
    )
    parser.add_argument(
        "--format",
        choices=("summary", "list", "tsv"),
        default="summary",
        help="summary: counts plus the per-module ranking. list: one line per finding.",
    )
    parser.add_argument(
        "--kind",
        choices=CLASSES + ("unresolvable",),
        action="append",
        help="Restrict to one finding class (repeatable).",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit 1 if any finding survives the filters. Not wired into `just qc`.",
    )
    args = parser.parse_args(argv)

    # One walk over kb/disorders, so the parsed-document cache is pure cost
    # (CLAUDE.md, Parsed-KB Cache). kb/modules is read twice -- once for the
    # anchor index -- but that is 189 small files.
    kb_cache.default_off()

    index = module_index(ROOT / "kb" / "modules")
    paths = resolve_paths(args.files)
    findings, links, totals = collect(paths, index)
    if args.kind:
        findings = [f for f in findings if f.kind in set(args.kind)]

    if args.format == "tsv":
        print("path\tnode\tanchor\tkind\tdetail")
        for f in findings:
            print(f"{f.path}\t{f.node}\t{f.anchor}\t{f.kind}\t{f.detail}")
    elif args.format == "list":
        for f in findings:
            print(
                f"{f.kind}\t{f.path}\n    node:   {f.node!r}\n    anchor: {f.anchor}\n    {f.detail}"
            )
    else:
        by_kind = Counter(f.kind for f in findings)
        print(f"{links} conformance link(s) in {len(paths)} file(s).\n")
        shared = links - by_kind["process_absent"] - by_kind["anchor_no_process"]
        print(f"  {shared:5}  share >=1 GO term with the module node")
        for kind in CLASSES + ("unresolvable",):
            if by_kind[kind]:
                print(f"  {by_kind[kind]:5}  {kind}")
        print(
            "\nThe process classes partition the links; cell_type_absent and "
            "edges_absent are orthogonal to them.\n"
            "A process_absent link is often a legitimate specific-for-generic "
            "substitution, so read the ranking, not the total.\n"
        )

        per_module: Counter = Counter()
        for f in findings:
            if f.kind == "process_absent":
                per_module[f.module] += 1
        # Ranked by COUNT, not ratio: a module with 1 of 1 conformer diverging
        # tops a ratio ranking and is one node's work, while one with 57 of 63
        # is a real worklist. The ratio is printed beside it.
        ranked = sorted(
            ((m, n, totals[m]) for m, n in per_module.items()),
            key=lambda row: (-row[1], row[0]),
        )
        print("Modules whose conformers most often share no GO term (absent/links):")
        for module, absent, total in ranked[:20]:
            print(f"  {absent:4}/{total:4}  {module}")
        if not ranked:
            print("  (none)")

    if args.strict and findings:
        print(f"\n{len(findings)} finding(s) (--strict).")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
