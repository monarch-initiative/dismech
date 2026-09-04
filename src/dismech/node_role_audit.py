"""Audit the free-text ``role`` slot on pathophysiology nodes against the graph.

This is step 1 of the "next step" list in the pathograph node-classification
design (``docs/superpowers/specs/2026-08-16-pathograph-node-classification-brainstorm.md``):
*migrate ``role`` mechanically where it is derivable, and see how much is left
over*. That leftover is the real curation job, and this module measures it.

Nothing here writes to ``kb/`` and no schema change is proposed. The output is
a worklist and a measurement, kept reproducible so the numbers in the design
doc can be re-derived rather than trusted.

What ``role`` has been asked to carry
-------------------------------------
``role`` is a plain ``string`` slot with no enum. Curators reached for it
because it was the only slot there, and it has accreted values answering at
least six different questions. Each normalised value is mapped, in
:data:`ROLE_FACETS`, to the facet it is actually answering:

``POSITION``
    Where the node sits in the causal chain (``trigger``, ``mediator``,
    ``consequence`` …). Fully computable from ``downstream`` edges, so the
    audit checks each such claim against the node's in/out-degree.
``INTERFACE``
    Whether something outside the chain touches the node
    (``therapeutic_vulnerability``, ``biomarker``). Fully computable from the
    linking slots (``treatments[].target_mechanisms``, ``biochemical[].readouts``
    …), so the audit checks whether the edge the role implies actually exists.
``DISPOSITION``, ``COMPENSATION``, ``NODE_CLASS``, ``RESISTANCE``
    Claims about what *kind* of thing the node is. These belong to the node-class
    tree (``DISPOSITION``, ``ALSO CLASSES > COMPENSATION``, the cascade tiers,
    ``TISSUE > immune evasion``), and no computation recovers them: they are the
    curated residue.
``EPISTEMIC``
    How sure we are (``provisional_effector``, ``disputed_branch``). Already has
    a home in ``mechanism_confidence``; the audit reports whether that slot is
    also set.
``UNMAPPED``
    A tail value this table has not seen. Not an error -- ``role`` is free text
    and new values arrive with every curation PR -- but each one is a data point
    about what the slot is being used for.

How a claim is checked
----------------------
Position is computed over ``downstream[].target`` edges restricted to targets
that resolve to a pathophysiology node **in the same file** (phenotype targets
are counted separately as ``phenotype_out``): ``SOURCE`` has out-edges and no
in-edges, ``SINK`` the reverse, ``INTERIOR`` both, ``ISOLATED`` neither. A
``POSITION`` role is ``DERIVED`` when the computed position is one the role
allows, otherwise ``CONTRADICTED``. Downstream-type roles (``consequence``,
``outcome`` …) allow ``INTERIOR`` as well as ``SINK`` -- the claim they make is
"caused by something upstream", and the design doc already established that
``consequence`` and ``outcome`` are indistinguishable from each other by
topology, so requiring a strict sink would manufacture disagreement. Plain
``effector`` is treated the same way: it says the node is driven by something
and does the damage, and a terminal effector (a glial scar, an acquired
resistance state) has nothing pathophysiological left to point at. The hub
roles -- ``mediator``, ``amplifier``, ``central_effector``, ``intermediate`` --
require ``INTERIOR``, because each claims something on both sides.

An ``INTERFACE`` role is ``DERIVED`` when the implied linking edge exists and
``CONTRADICTED`` when it does not. Every other facet is ``CURATED``: the audit
cannot check it, only count it.
"""

from __future__ import annotations

import csv
import sys
from collections import Counter, defaultdict
from collections.abc import Iterable, Iterator
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

DEFAULT_KB_DIRS = (Path("kb/disorders"), Path("kb/modules"))

SOURCE = "SOURCE"
INTERIOR = "INTERIOR"
SINK = "SINK"
ISOLATED = "ISOLATED"
POSITIONS = (SOURCE, INTERIOR, SINK, ISOLATED)

DERIVED = "DERIVED"
CONTRADICTED = "CONTRADICTED"
CURATED = "CURATED"
UNMAPPED = "UNMAPPED"

#: Position roles allow more than one computed position where the claim is
#: genuinely a set. ``INTERFACE`` expectations name the edge flag that must be
#: set on the node (see :class:`NodeRole`).
_UPSTREAM = frozenset({SOURCE})
_MIDDLE = frozenset({INTERIOR})
_DOWNSTREAM = frozenset({INTERIOR, SINK})

ROLE_FACETS: dict[str, tuple[str, frozenset[str] | str | None]] = {
    # --- POSITION: computable from downstream edges ------------------------
    "trigger": ("POSITION", _UPSTREAM),
    "root": ("POSITION", _UPSTREAM),
    "primary": ("POSITION", _UPSTREAM),
    "initiator": ("POSITION", _UPSTREAM),
    "upstream": ("POSITION", _UPSTREAM),
    "upstream_effector": ("POSITION", _UPSTREAM),
    "pathogen-specific_initiating_mechanism": ("POSITION", _UPSTREAM),
    "proximal_toxic_mechanism": ("POSITION", _UPSTREAM),
    "primary_defect": ("POSITION", _UPSTREAM),
    "initiating_mechanism": ("POSITION", _UPSTREAM),
    "mediator": ("POSITION", _MIDDLE),
    "intermediate": ("POSITION", _MIDDLE),
    "intermediary": ("POSITION", _MIDDLE),
    "central_effector": ("POSITION", _MIDDLE),
    "central": ("POSITION", _MIDDLE),
    "effector": ("POSITION", _DOWNSTREAM),
    "amplifier": ("POSITION", _MIDDLE),
    "convergent_effector": ("POSITION", _MIDDLE),
    "alternative_effector": ("POSITION", _MIDDLE),
    "developmental_effector": ("POSITION", _MIDDLE),
    "signal_transmission": ("POSITION", _MIDDLE),
    "commitment_step": ("POSITION", _MIDDLE),
    "convergence_point": ("POSITION", _MIDDLE),
    "consequence": ("POSITION", _DOWNSTREAM),
    "outcome": ("POSITION", _DOWNSTREAM),
    "endpoint": ("POSITION", _DOWNSTREAM),
    "downstream": ("POSITION", _DOWNSTREAM),
    "downstream_pathology": ("POSITION", _DOWNSTREAM),
    "downstream_effector": ("POSITION", _DOWNSTREAM),
    "tissue_consequence": ("POSITION", _DOWNSTREAM),
    "late_effector": ("POSITION", _DOWNSTREAM),
    "gene_specific_consequence": ("POSITION", _DOWNSTREAM),
    "convergent_phenotype": ("POSITION", _DOWNSTREAM),
    # --- INTERFACE: computable from the linking slots -----------------------
    "therapeutic_vulnerability": ("INTERFACE", "targeted"),
    "biomarker": ("INTERFACE", "read_out"),
    # --- DISPOSITION: the tree's DISPOSITION class; curated -----------------
    "susceptibility": ("DISPOSITION", None),
    "susceptibility_factor": ("DISPOSITION", None),
    "predisposing_factor": ("DISPOSITION", None),
    "permissive": ("DISPOSITION", None),
    "modifier": ("DISPOSITION", None),
    "context-dependent_modifier": ("DISPOSITION", None),
    "modulator": ("DISPOSITION", None),
    "contributor": ("DISPOSITION", None),
    "regulatory": ("DISPOSITION", None),
    # --- COMPENSATION: the tree's ALSO CLASSES > COMPENSATION; curated ------
    "protective": ("COMPENSATION", None),
    "host_defense": ("COMPENSATION", None),
    "counter_regulatory": ("COMPENSATION", None),
    # --- RESISTANCE: domain content (therapy escape, immune evasion) --------
    "adaptive_escape": ("RESISTANCE", None),
    "intrinsic_resistance": ("RESISTANCE", None),
    "resistance_mechanism": ("RESISTANCE", None),
    "immune_evasion": ("RESISTANCE", None),
    "virulence": ("RESISTANCE", None),
    "virulence_factor": ("RESISTANCE", None),
    # --- NODE_CLASS: says what kind of thing the node is; the tree's job ----
    "mechanism": ("NODE_CLASS", None),
    "molecular_mechanism": ("NODE_CLASS", None),
    "cellular_mechanism": ("NODE_CLASS", None),
    "lesion_mechanism": ("NODE_CLASS", None),
    "pleiotropy_mechanism": ("NODE_CLASS", None),
    "pathological_process": ("NODE_CLASS", None),
    "pathway": ("NODE_CLASS", None),
    "organ_dysfunction": ("NODE_CLASS", None),
    "tissue_accumulation": ("NODE_CLASS", None),
    "driver": ("NODE_CLASS", None),
    "inflammatory_mechanism": ("NODE_CLASS", None),
    # --- EPISTEMIC: already has a slot (mechanism_confidence) ---------------
    "provisional_effector": ("EPISTEMIC", None),
    "emerging_mechanism": ("EPISTEMIC", None),
    "disputed_branch": ("EPISTEMIC", None),
    "provisional_trigger": ("EPISTEMIC", None),
    "candidate_effector": ("EPISTEMIC", None),
}

FACETS = ("POSITION", "INTERFACE", "DISPOSITION", "COMPENSATION",
          "RESISTANCE", "NODE_CLASS", "EPISTEMIC", "UNMAPPED")

#: Interior roles whose *distinction* from each other topology cannot recover.
#: Their position is derivable; which of these three a node is is the one part
#: of ``role`` the design doc argues is worth keeping curated.
CAUSAL_FUNCTION_RESIDUE = frozenset({"mediator", "amplifier", "central_effector"})


def normalize_role(value: Any) -> str:
    """``Trigger`` / ``TRIGGER`` / ``central effector`` -> one spelling."""
    return str(value).strip().lower().replace(" ", "_")


@dataclass(frozen=True)
class NodeRole:
    """One pathophysiology node's ``role`` claim and what the edges say."""

    disease: str
    node: str
    role_raw: str
    role: str
    facet: str
    position: str
    in_degree: int
    out_degree: int
    phenotype_out: int
    targeted: bool
    modeled: bool
    read_out: bool
    influenced: bool
    conforms: bool
    verdict: str
    detail: str = ""


@dataclass
class AuditResult:
    nodes: list[NodeRole] = field(default_factory=list)
    #: total pathophysiology nodes seen, tagged or not
    total_nodes: int = 0
    #: raw spelling -> count, for the casing report
    raw_spellings: Counter = field(default_factory=Counter)


def _targets(items: Iterable[Any], slot: str) -> Iterator[str]:
    for item in items or []:
        if not isinstance(item, dict):
            continue
        for link in item.get(slot) or []:
            if isinstance(link, dict) and link.get("target"):
                yield str(link["target"])


def _link_index(data: dict[str, Any]) -> dict[str, set[str]]:
    """Which pathograph-linking slots point at which node names."""
    idx: dict[str, set[str]] = {
        "targeted": set(), "modeled": set(), "read_out": set(), "influenced": set(),
    }
    idx["targeted"].update(_targets(data.get("treatments"), "target_mechanisms"))
    for section in ("experimental_models", "animal_models", "computational_models"):
        idx["modeled"].update(_targets(data.get(section), "modeled_mechanisms"))
    idx["read_out"].update(_targets(data.get("biochemical"), "readouts"))
    for section in ("investigations", "phenotypes"):
        idx["read_out"].update(_targets(data.get(section), "reports_on"))
    idx["influenced"].update(_targets(data.get("environmental"), "influences_mechanisms"))
    return idx


def compute_positions(
    nodes: list[dict[str, Any]], phenotype_names: set[str] | None = None
) -> dict[str, tuple[str, int, int, int]]:
    """``name -> (position, in_degree, out_degree, phenotype_out)``.

    Edges are ``downstream[].target`` strings matched verbatim against another
    pathophysiology node's ``name`` in the same list -- the same convention
    ``dismech.graph`` uses. A target naming a phenotype is reported separately
    as ``phenotype_out`` but still counts as an out-edge for the position: a
    trigger whose only downstream is a phenotype is a source, not an isolate.
    ``out_degree`` in the tuple counts pathophysiology targets only.
    """
    names = [str(n.get("name", "")) for n in nodes if isinstance(n, dict)]
    name_set = set(names)
    phen = phenotype_names or set()
    in_deg: Counter = Counter()
    out_deg: Counter = Counter()
    phen_out: Counter = Counter()
    for node in nodes:
        if not isinstance(node, dict):
            continue
        src = str(node.get("name", ""))
        for edge in node.get("downstream") or []:
            if not isinstance(edge, dict) or not edge.get("target"):
                continue
            tgt = str(edge["target"])
            if tgt in name_set and tgt != src:
                out_deg[src] += 1
                in_deg[tgt] += 1
            elif tgt in phen:
                phen_out[src] += 1
    out = {}
    for name in names:
        i, o, p = in_deg[name], out_deg[name], phen_out[name]
        if i and (o or p):
            pos = INTERIOR
        elif o or p:
            pos = SOURCE
        elif i:
            pos = SINK
        else:
            pos = ISOLATED
        out[name] = (pos, i, o, p)
    return out


def judge(
    role: str, position: str, flags: dict[str, bool], mechanism_confidence: Any = None
) -> tuple[str, str, str]:
    """``(facet, verdict, detail)`` for one normalised role against its edges."""
    facet, expected = ROLE_FACETS.get(role, ("UNMAPPED", None))
    if facet == "POSITION":
        assert isinstance(expected, frozenset)
        if position in expected:
            return facet, DERIVED, position
        return facet, CONTRADICTED, f"{position} not in {'/'.join(sorted(expected))}"
    if facet == "INTERFACE":
        assert isinstance(expected, str)
        if flags.get(expected):
            return facet, DERIVED, expected
        return facet, CONTRADICTED, f"no {expected} edge"
    if facet == "EPISTEMIC":
        detail = (
            f"mechanism_confidence={mechanism_confidence}"
            if mechanism_confidence
            else "no mechanism_confidence"
        )
        return facet, CURATED, detail
    if facet == "UNMAPPED":
        return facet, UNMAPPED, ""
    return facet, CURATED, ""


def audit(kb_dirs: Iterable[Path] = DEFAULT_KB_DIRS) -> AuditResult:
    """Audit every ``role``-bearing pathophysiology node under ``kb_dirs``."""
    from dismech.yaml_io import safe_load

    result = AuditResult()
    for kb_dir in kb_dirs:
        for path in sorted(Path(kb_dir).glob("*.yaml")):
            try:
                data = safe_load(path.read_text(encoding="utf-8"))
            except Exception:  # a malformed KB file is not this tool's business
                continue
            if not isinstance(data, dict):
                continue
            nodes = [n for n in data.get("pathophysiology") or [] if isinstance(n, dict)]
            result.total_nodes += len(nodes)
            phenotypes = {
                str(p.get("name")) for p in data.get("phenotypes") or []
                if isinstance(p, dict) and p.get("name")
            }
            positions = compute_positions(nodes, phenotypes)
            links = _link_index(data)
            for node in nodes:
                raw = node.get("role")
                if raw is None or str(raw).strip() == "":
                    continue
                name = str(node.get("name", ""))
                role = normalize_role(raw)
                result.raw_spellings[str(raw)] += 1
                position, i, o, p = positions[name]
                flags = {
                    "targeted": name in links["targeted"],
                    "modeled": name in links["modeled"],
                    "read_out": name in links["read_out"],
                    "influenced": name in links["influenced"],
                    "conforms": bool(node.get("conforms_to")),
                }
                facet, verdict, detail = judge(
                    role, position, flags, node.get("mechanism_confidence")
                )
                result.nodes.append(
                    NodeRole(
                        disease=path.stem,
                        node=name,
                        role_raw=str(raw),
                        role=role,
                        facet=facet,
                        position=position,
                        in_degree=i,
                        out_degree=o,
                        phenotype_out=p,
                        verdict=verdict,
                        detail=detail,
                        **flags,
                    )
                )
    return result


# --- reports ------------------------------------------------------------------


def casing_variants(result: AuditResult) -> dict[str, list[tuple[str, int]]]:
    """Normalised value -> the raw spellings that collapse into it, when >1."""
    groups: dict[str, list[tuple[str, int]]] = defaultdict(list)
    for raw, n in result.raw_spellings.items():
        groups[normalize_role(raw)].append((raw, n))
    return {
        k: sorted(v, key=lambda t: -t[1]) for k, v in sorted(groups.items()) if len(v) > 1
    }


def crosstab(result: AuditResult) -> dict[str, Counter]:
    """role -> Counter of computed positions."""
    table: dict[str, Counter] = defaultdict(Counter)
    for n in result.nodes:
        table[n.role][n.position] += 1
    return table


def facet_table(result: AuditResult) -> list[tuple[str, int, int, int, int, int]]:
    """``(facet, roles, nodes, derived, contradicted, curated_or_unmapped)``."""
    rows = []
    for facet in FACETS:
        subset = [n for n in result.nodes if n.facet == facet]
        if not subset:
            continue
        verdicts = Counter(n.verdict for n in subset)
        rows.append((
            facet,
            len({n.role for n in subset}),
            len(subset),
            verdicts[DERIVED],
            verdicts[CONTRADICTED],
            verdicts[CURATED] + verdicts[UNMAPPED],
        ))
    return rows


def summarize(result: AuditResult) -> dict[str, Any]:
    tagged = len(result.nodes)
    verdicts = Counter(n.verdict for n in result.nodes)
    residue = [n for n in result.nodes if n.verdict != DERIVED]
    causal_function = sum(
        1 for n in result.nodes
        if n.verdict == DERIVED and n.role in CAUSAL_FUNCTION_RESIDUE
    )
    return {
        "total_nodes": result.total_nodes,
        "tagged": tagged,
        "raw_spellings": len(result.raw_spellings),
        "normalized_values": len({n.role for n in result.nodes}),
        "verdicts": verdicts,
        "residue": len(residue),
        "residue_by_facet": Counter(n.facet for n in residue),
        "causal_function_residue": causal_function,
        "unmapped_values": Counter(n.role for n in result.nodes if n.verdict == UNMAPPED),
    }


def _iter_tsv(result: AuditResult) -> Iterator[list[str]]:
    yield [
        "disease", "node", "role_raw", "role", "facet", "verdict", "detail",
        "position", "in_degree", "out_degree", "phenotype_out",
        "targeted", "modeled", "read_out", "influenced", "conforms",
    ]
    for n in result.nodes:
        yield [
            n.disease, n.node, n.role_raw, n.role, n.facet, n.verdict, n.detail,
            n.position, str(n.in_degree), str(n.out_degree), str(n.phenotype_out),
            *(str(int(b)) for b in (n.targeted, n.modeled, n.read_out, n.influenced, n.conforms)),
        ]


def _print_summary(result: AuditResult) -> None:
    s = summarize(result)
    tagged = s["tagged"] or 1
    print(f"pathophysiology nodes      {s['total_nodes']}")
    print(f"  carrying a role          {s['tagged']:6d}  ({100*s['tagged']/(s['total_nodes'] or 1):.1f}%)")
    print(f"  raw spellings            {s['raw_spellings']:6d}")
    print(f"  after normalisation      {s['normalized_values']:6d}")
    print("\nby facet the role is answering:")
    print(f"  {'facet':14s} {'roles':>5s} {'nodes':>6s} {'derived':>8s} {'contra':>7s} {'curated':>8s}")
    for facet, roles, n, derived, contra, curated in facet_table(result):
        print(f"  {facet:14s} {roles:5d} {n:6d} {derived:8d} {contra:7d} {curated:8d}")
    v = s["verdicts"]
    print("\nverdict:")
    for name in (DERIVED, CONTRADICTED, CURATED, UNMAPPED):
        print(f"  {name:14s} {v[name]:6d}  ({100*v[name]/tagged:.1f}%)")
    print(
        f"\nresidue (not recoverable from edges)  {s['residue']}  "
        f"({100*s['residue']/tagged:.1f}% of tagged nodes)"
    )
    for facet, n in s["residue_by_facet"].most_common():
        print(f"  {facet:14s} {n:6d}")
    print(
        f"\nderived, but keeping a curated causal-function distinction "
        f"(mediator / amplifier / central_effector)  {s['causal_function_residue']}"
    )
    if s["unmapped_values"]:
        print("\nunmapped tail values:")
        for role, n in s["unmapped_values"].most_common():
            print(f"  {n:4d}  {role}")


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(
        prog="python -m dismech.node_role_audit",
        description="Audit the free-text pathophysiology `role` slot against graph edges.",
    )
    parser.add_argument(
        "--format",
        choices=("summary", "tsv", "casing", "crosstab", "residue"),
        default="summary",
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

    result = audit(kb_dirs)

    if args.format == "tsv":
        writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
        writer.writerows(_iter_tsv(result))
        return 0

    if args.format == "casing":
        variants = casing_variants(result)
        for norm, raws in variants.items():
            spelled = ", ".join(f"{raw!r} x{n}" for raw, n in raws)
            print(f"{norm:28s} <- {spelled}")
        print(f"\n{len(variants)} values with more than one spelling", file=sys.stderr)
        return 0

    if args.format == "crosstab":
        table = crosstab(result)
        print(f"{'role':40s} {'n':>5s} " + " ".join(f"{p:>9s}" for p in POSITIONS))
        for role, counts in sorted(table.items(), key=lambda kv: -sum(kv[1].values())):
            n = sum(counts.values())
            cells = " ".join(f"{100*counts[p]/n:8.0f}%" for p in POSITIONS)
            print(f"{role:40s} {n:5d} {cells}")
        return 0

    if args.format == "residue":
        rows = [n for n in result.nodes if n.verdict != DERIVED]
        rows.sort(key=lambda n: (n.facet, n.verdict, n.role, n.disease, n.node))
        for n in rows:
            tail = f"  -- {n.detail}" if n.detail else ""
            print(f"{n.facet:12s} {n.verdict:12s} {n.role:28s} {n.node}  [{n.disease}]{tail}")
        print(f"\n{len(rows)} role-tagged nodes not recoverable from edges", file=sys.stderr)
        return 0

    _print_summary(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
