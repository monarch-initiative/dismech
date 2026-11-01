#!/usr/bin/env python3
"""Cross-walk the AOP-Wiki parkinsonian AOPs onto dismech pathographs.

AOP-Wiki carries five AOPs that end in parkinsonian motor deficits: AOP 3
(complex I, the only OECD-endorsed one), 587 (complex III), 588 (complex II),
589 (complex IV) and 593 (redox cycling). Between them they hold 12 Key Events
and 13 Key Event Relationships, and all five converge on the same three-event
tail -- KE177 mitochondrial dysfunction, KE890 nigrostriatal dopaminergic
degeneration, KE896 parkinsonian motor deficits.

This script asks, per dismech entry, which of those Key Events the pathograph
already holds and which Key Event Relationships its edges already assert. It
reports; it changes nothing, and it does not propose curation.

Why a script rather than a grep
-------------------------------
A Key Event matches a node on structure where structure exists -- a
``conforms_to`` into the right module node, or a GO/CL/UBERON binding the Key
Event's own Event Components imply -- and on a name or description cue only as a
fallback. Each match records which basis fired, so a reader can tell a binding
match from a word match and discount the second. Hand-run patterns cannot carry
that distinction, and cannot be re-run against a later AOP-Wiki snapshot.

What the AOP side is read from
------------------------------
Nothing here reads AOP-Wiki. The 12 Key Events, 13 Key Event Relationships and
their endpoints are transcribed below from the ``aop-wiki-cli`` 10-03-2026
snapshot, which is the pin the report cites. Re-deriving them means re-running
that tool, not changing this file -- see the ``aop-wiki`` skill.

Reusing the connectivity metric
-------------------------------
Whether an entry's parkinsonian phenotypes are causally explained is not
recomputed here. :func:`dismech.qc_plugins.causal_inlink_coverage` -- the metric
behind ``just list-disconnected-phenotypes`` and the gating
``compliance-connectivity`` score -- supplies it, so this report and those
recipes can never disagree on a number. This script only slices that result to
the parkinsonian phenotypes, which is the adverse outcome KE896 anchors on and
the one cut a corpus-level view cannot show.

    python scripts/aop_parkinsonism_crosswalk.py                  # summary
    python scripts/aop_parkinsonism_crosswalk.py --format json
    python scripts/aop_parkinsonism_crosswalk.py --format tsv     # one row per entry/KER
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import deque
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from dismech.kb_cache import load_document
from dismech.qc_plugins import CAUSAL_PREDICATES, causal_inlink_coverage

SNAPSHOT = "10-03-2026"
AOPS = {
    "3": "Complex I inhibition leads to parkinsonian motor deficits (WPHA/WNT Endorsed)",
    "587": "Complex III inhibition leads to parkinsonian motor deficits",
    "588": "Complex II inhibition leads to parkinsonian motor deficits",
    "589": "Complex IV inhibition leads to parkinsonian motor deficits",
    "593": "Redox cycling by mitochondria leads to nigrostriatal degeneration",
}
KES = {
    "888": "Binding of inhibitor, complex I",
    "887": "Inhibition, complex I",
    "1542": "Inhibition, complex III",
    "2118": "Succinate dehydrogenase (complex II), inhibited",
    "1543": "Complex IV inhibition",
    "2362": "Redox cycling of a chemical by mitochondria",
    "2363": "Elevated mitochondrial ROS and dysfunction",
    "177": "Increase, mitochondrial dysfunction",
    "889": "Proteostasis, impaired",
    "188": "Neuroinflammation",
    "890": "Degeneration of nigrostriatal dopaminergic neurons",
    "896": "Parkinsonian motor deficits",
}
# KER id -> (upstream KE, downstream KE, AOPs carrying it, references on the KER record)
KERS = {
    "933": ("888", "887", ["3"], True),
    "934": ("887", "177", ["3"], True),
    "904": ("177", "889", ["3"], True),
    "905": ("889", "890", ["3", "593"], True),
    "910": ("890", "896", ["3", "587", "588", "589", "593"], True),
    "907": ("890", "188", ["3"], True),
    "906": ("188", "890", ["3"], True),
    "908": ("177", "890", ["3", "587", "588", "589"], True),
    "3637": ("1542", "177", ["587"], True),
    "3554": ("2118", "177", ["588"], False),
    "3555": ("1543", "177", ["589"], False),
    "3629": ("2362", "2363", ["593"], True),
    "3650": ("2363", "889", ["593"], True),
}
# AOP-Wiki prototypical stressors for these five pathways.
STRESSORS = {
    "MPP+/MPTP": r"\bmptp\b|\bmpp\+|1-methyl-4-phenyl",
    "rotenone": r"rotenone",
    "deguelin": r"deguelin",
    "pyrimidifen": r"pyrimidifen",
    "fenpyroximate": r"fenpyroximate",
    "tebufenpyrad": r"tebufenpyrad",
    "antimycin A": r"antimycin",
    "picoxystrobin": r"picoxystrobin",
    "paraquat": r"paraquat",
}
# Parkinsonism and the cardinal motor signs, as HPO descendant closures.
PARKINSONIAN_HPO = frozenset(
    {
        "HP:0001300",  # Parkinsonism
        "HP:0002548",  # Parkinsonism with favorable response to dopaminergic medication
        "HP:0002067",  # Bradykinesia
        "HP:0002063",  # Rigidity
        "HP:0002396",  # Cogwheel rigidity
        "HP:0007076",  # Extrapyramidal muscular rigidity
        "HP:0007158",  # Progressive extrapyramidal muscular rigidity
        "HP:0002322",  # Resting tremor
        "HP:0025387",  # Pill-rolling tremor
        "HP:0002172",  # Postural instability
    }
)

# Key Event -> (conforms_to module-node prefixes, GO ids from Event Components,
#               node-name pattern). A prefix ending in "#" admits the whole
#               module only when the conformed node's own name fits the KE too.
RULES: dict[str, tuple[list[str], set[str], str]] = {
    "888": (
        [],
        set(),
        r"(complex i\b|nadh[:\- ]ubiquinone).*(inhibitor|binding)|rotenone|mpp\+|mptp",
    ),
    "887": (
        [
            "complex_i_deficiency#",
            "parkinsonism_dopaminergic_degeneration#Mitochondrial Complex I",
        ],
        {"GO:0006120", "GO:0008137", "GO:0032981"},
        r"complex i\b|nadh[:\- ]ubiquinone",
    ),
    "1542": (
        [],
        {"GO:0006122", "GO:0008121", "GO:0034551"},
        r"complex iii\b|cytochrome bc1|antimycin",
    ),
    "2118": (
        [],
        {"GO:0000104", "GO:0006121", "GO:0008177"},
        r"complex ii\b|succinate dehydrogenase|\bsdh",
    ),
    "1543": (
        ["complex_iv_assembly_deficiency#"],
        {"GO:0004129", "GO:0006123", "GO:0033617"},
        r"complex iv\b|cytochrome c oxidase|\bcox\b(?!-?2)",  # not COX-2 (cyclooxygenase)
    ),
    "2362": ([], set(), r"redox[- ]cycl|paraquat"),
    "2363": (
        [
            "mitochondrial_dysfunction#Bioenergetic Decline and Oxidative Stress",
            "xenobiotic_oxidative_phosphorylation_blockade#Secondary Mitochondrial Oxidative Stress",
            "parkinsonism_dopaminergic_degeneration#Mitochondrial Complex I Inhibition and Oxidative Stress",
        ],
        set(),
        r"mitochondrial (ros|reactive oxygen|oxidative|superoxide)",
    ),
    "177": (
        [
            "mitochondrial_dysfunction#",
            "complex_i_deficiency#Impaired",
            "complex_iv_assembly_deficiency#Impaired",
            "xenobiotic_oxidative_phosphorylation_blockade#Cellular ATP Depletion",
            "parkinsonism_dopaminergic_degeneration#Mitochondrial Complex I",
        ],
        {"GO:0007005", "GO:0006119", "GO:0042775", "GO:0009060", "GO:0022900"},
        r"mitochondri|oxidative phosphorylation|respiratory chain",
    ),
    "889": (
        [
            "loss_of_proteostasis#",
            "disabled_macroautophagy#",
            "polyglutamine_expansion_proteotoxicity#",
            "parkinsonism_dopaminergic_degeneration#Alpha-Synuclein",
        ],
        {
            "GO:0006457",
            "GO:0043161",
            "GO:0070841",
            "GO:0006914",
            "GO:0016236",
            "GO:0061684",
            "GO:0030968",
            "GO:0034976",
            "GO:0000422",
            "GO:0006511",
            "GO:0061077",
        },
        (
            r"aggregat|proteostas|proteasom|inclusion|misfold|autophag|lewy|unfolded protein|"
            r"er stress|endoplasmic reticulum stress|mitophag|proteotox|protein clearance"
        ),
    ),
    "188": (
        ["neuroinflammation_glial_activation#"],
        {"GO:0150076", "GO:0001774", "GO:0048143"},
        r"neuroinflam|microgli|astrogli|astrocytosis|gliosis|glial activation|brain inflammation",
    ),
    "890": (
        ["parkinsonism_dopaminergic_degeneration#Nigrostriatal"],
        set(),
        (
            r"(dopaminergic|nigr|substantia nigra).*(loss|degenerat|death|depigment|neurodegenerat)|"
            r"(loss|degenerat|death).*(dopaminergic|nigr)|striatonigral"
        ),
    ),
}
# dismech routinely splits KE890 -> KE896 across a dopamine-deficiency and a
# circuit node. Both are tracked so KER910 is not scored as absent on a record
# that models the step in more detail than the AOP does.
STRIATAL_PREFIX = "parkinsonism_dopaminergic_degeneration#Striatal"
STRIATAL_NAME = (
    r"striatal dopamine|dopamine (deficien|deplet|release)|dopamine (bio)?synthesis|"
    r"catecholamine deficien|monoamine (neurotransmitter )?deficien|"
    r"dopaminergic (denervation|dysfunction)|synaptic dopamine"
)
BASAL_GANGLIA_NAME = (
    r"basal ganglia|extrapyramidal|pallid|striatal (circuit|output|neuron)"
)

MAX_INDIRECT_HOPS = 3

# Respiratory-complex GO terms, per complex, for the KB-wide sweep behind the report's
# central finding. One set per AOP entry point, so the sweep answers the question for each of
# the five AOPs rather than only for complex I. Complex II is searched on succinate
# dehydrogenase as well as on the complex name, because that is what dismech calls it.
RESPIRATORY_COMPLEX_GO: dict[str, frozenset[str]] = {
    "complex I": frozenset({"GO:0006120", "GO:0008137", "GO:0032981"}),
    "complex II / SDH": frozenset(
        {"GO:0000104", "GO:0006121", "GO:0008177", "GO:0045281", "GO:0045273"}
    ),
    "complex III": frozenset({"GO:0006122", "GO:0008121", "GO:0034551", "GO:0005750"}),
    "complex IV": frozenset({"GO:0004129", "GO:0006123", "GO:0033617", "GO:0005751"}),
}
# Complex II is also reachable by its subunit genes, which is how several entries bind it.
SDH_GENES = frozenset({"SDHA", "SDHB", "SDHC", "SDHD", "SDHAF1", "SDHAF2"})


def _term_ids(node: dict, key: str) -> set[str]:
    return {(item.get("term") or {}).get("id") for item in node.get(key) or []}


def _conforms_to(node: dict) -> list[str]:
    value = node.get("conforms_to")
    if not value:
        return []
    return value if isinstance(value, list) else [value]


def match_key_event(node: dict, ke: str) -> list[str]:
    """Return the bases on which ``node`` matches Key Event ``ke`` (empty if none)."""
    prefixes, go_ids, name_pattern = RULES[ke]
    name = node["name"].lower()
    bases: list[str] = []

    for conformance in _conforms_to(node):
        for prefix in prefixes:
            whole_module = prefix.endswith("#")
            node_part = (
                conformance.split("#", 1)[1].lower() if "#" in conformance else ""
            )
            if conformance.startswith(prefix) and (
                not whole_module or re.search(name_pattern, node_part)
            ):
                bases.append(f"conforms_to {conformance}")
                break

    shared_go = (
        _term_ids(node, "biological_processes") | _term_ids(node, "molecular_functions")
    ) & go_ids
    if shared_go:
        bases.append("GO " + ",".join(sorted(shared_go)))

    if ke == "890":
        cells, locations = _term_ids(node, "cell_types"), _term_ids(node, "locations")
        if (
            "CL:0000700" in cells
            and "UBERON:0002038" in locations
            and re.search(r"loss|degenerat|death", name)
        ):
            bases.append("CL:0000700 + UBERON:0002038")
    if (
        ke == "188"
        and _term_ids(node, "cell_types") & {"CL:0000129", "CL:0000127"}
        and re.search(r"inflam|activat|reactiv|cytokine", name)
    ):
        bases.append("glial cell type + inflammation in name")

    if re.search(name_pattern, name):
        bases.append("name")

    if ke == "2363" and not bases:
        oxidative = _term_ids(node, "biological_processes") & {
            "GO:0006979",
            "GO:0072593",
            "GO:1903409",
            "GO:0000302",
        }
        description = (node.get("description") or "").lower()
        if (
            oxidative
            and "mitochondri" in description
            and re.search(r"oxidat|reactive oxygen|\bros\b|free radical|redox", name)
        ):
            bases.append("oxidative-stress GO + mitochondrial description")
    return bases


def respiratory_complex_sweep(root: Path) -> dict[str, dict[str, list[str]]]:
    """Entries anywhere in ``kb/disorders/`` binding each respiratory complex.

    The point of the sweep is the overlap with the selected parkinsonism entries. dismech
    curates respiratory-chain inhibition in depth under mitochondrial disease; whether any of
    that work is attached to a parkinsonism entry is the question these AOPs put to the KB,
    and it has to be asked once per complex because each is a different AOP's entry point.

    Complex II is searched by GO term and by SDH subunit gene, since dismech binds it both
    ways and "complex II" is not the name most of those entries use.
    """
    found: dict[str, dict[str, list[str]]] = {
        label: {} for label in RESPIRATORY_COMPLEX_GO
    }
    found["complex II by SDHx gene"] = {}
    for path in sorted((root / "kb/disorders").glob("*.yaml")):
        record = load_document(path)
        nodes = record.get("pathophysiology") or []
        for label, go_ids in RESPIRATORY_COMPLEX_GO.items():
            hits = [
                node["name"]
                for node in nodes
                if (
                    _term_ids(node, "biological_processes")
                    | _term_ids(node, "molecular_functions")
                    | _term_ids(node, "cellular_components")
                )
                & go_ids
            ]
            if hits:
                found[label][path.stem] = hits
        by_gene = [
            node["name"]
            for node in nodes
            if {(g.get("term") or {}).get("label") for g in node.get("genes") or []}
            & SDH_GENES
        ]
        if by_gene:
            found["complex II by SDHx gene"][path.stem] = by_gene
    return found


def causal_graph(nodes: list[dict]) -> dict[str, list[str]]:
    graph: dict[str, list[str]] = {}
    for node in nodes:
        for edge in node.get("downstream") or []:
            if edge.get("predicate", "causes") in CAUSAL_PREDICATES:
                graph.setdefault(node["name"], []).append(edge["target"])
    return graph


def shortest_path(
    graph: dict[str, list[str]], sources: set[str], targets: set[str]
) -> list[str] | None:
    best: list[str] | None = None
    for source in sources:
        queue = deque([(source, [source])])
        while queue:
            current, path = queue.popleft()
            if len(path) - 1 >= MAX_INDIRECT_HOPS:
                continue
            for nxt in graph.get(current, []):
                if nxt in path:
                    continue
                if nxt in targets:
                    if best is None or len(path) + 1 < len(best):
                        best = path + [nxt]
                    continue
                queue.append((nxt, path + [nxt]))
    return best


def crosswalk(record: dict, path: Path) -> dict:
    nodes = record.get("pathophysiology") or []
    graph = causal_graph(nodes)

    matches: dict[str, dict[str, list[str]]] = {ke: {} for ke in KES}
    striatal, basal_ganglia = [], []
    for node in nodes:
        for ke in RULES:
            bases = match_key_event(node, ke)
            if bases:
                matches[ke][node["name"]] = bases
        name = node["name"].lower()
        if any(c.startswith(STRIATAL_PREFIX) for c in _conforms_to(node)) or re.search(
            STRIATAL_NAME, name
        ):
            striatal.append(node["name"])
        if re.search(BASAL_GANGLIA_NAME, name):
            basal_ganglia.append(node["name"])

    parkinsonian = {
        p["name"]
        for p in record.get("phenotypes") or []
        if ((p.get("phenotype_term") or {}).get("term") or {}).get("id")
        in PARKINSONIAN_HPO
    }
    matches["896"] = {
        name: ["parkinsonian HPO phenotype"] for name in sorted(parkinsonian)
    }

    connected, total, unconnected = causal_inlink_coverage(record, CAUSAL_PREDICATES)
    stranded = sorted(parkinsonian & set(unconnected))

    kers = {}
    for ker, (upstream, downstream, _, _) in KERS.items():
        up, down = set(matches[upstream]), set(matches[downstream])
        direct = sorted(
            (s, t) for s in up for t in graph.get(s, []) if t in down and t != s
        )
        if direct:
            kers[ker] = {"status": "direct", "edges": direct}
        elif up & down:
            kers[ker] = {"status": "same node", "nodes": sorted(up & down)}
        elif up and down:
            via = shortest_path(graph, up, down)
            kers[ker] = (
                {"status": "indirect", "path": via} if via else {"status": "no path"}
            )
        else:
            kers[ker] = {
                "status": "key event absent",
                "absent": [
                    ke for ke, side in ((upstream, up), (downstream, down)) if not side
                ],
            }

    environmental = yaml.safe_dump(record.get("environmental") or []).lower()
    return {
        "path": str(path),
        "name": record.get("name"),
        "nodes": len(nodes),
        "key_events": matches,
        "key_events_present": sorted(ke for ke, m in matches.items() if m),
        "kers": kers,
        "striatal_bridge": striatal,
        "basal_ganglia_bridge": basal_ganglia,
        "phenotype_connectivity": {
            "connected": connected,
            "total": total,
            "parkinsonian": sorted(parkinsonian),
            "parkinsonian_stranded": stranded,
        },
        "aop_stressors_named": [
            s for s, rx in STRESSORS.items() if re.search(rx, environmental)
        ],
    }


def select_records(root: Path) -> list[Path]:
    """Entries carrying parkinsonism, or bradykinesia with a second cardinal sign."""
    chosen = []
    second_sign = PARKINSONIAN_HPO - {"HP:0001300", "HP:0002548", "HP:0002067"}
    for path in sorted((root / "kb/disorders").glob("*.yaml")):
        record = load_document(path)
        ids = {
            ((p.get("phenotype_term") or {}).get("term") or {}).get("id")
            for p in record.get("phenotypes") or []
        }
        has_parkinsonism = bool(ids & {"HP:0001300", "HP:0002548"})
        has_signs = "HP:0002067" in ids and bool(ids & second_sign)
        if has_parkinsonism or has_signs:
            chosen.append(path)
    return chosen


def render_complex_sweep(
    results: list[dict], sweep: dict[str, dict[str, list[str]]], out
) -> None:
    selected = {Path(r["path"]).stem for r in results}
    print(
        f"\nRespiratory-complex bindings KB-wide, and their overlap with the "
        f"{len(selected)} parkinsonism entries",
        file=out,
    )
    for label, entries in sweep.items():
        nodes = sum(len(v) for v in entries.values())
        overlap = sorted(set(entries) & selected)
        print(
            f"  {label:<26} {nodes:>3} nodes / {len(entries):>3} entries"
            f"   overlap: {len(overlap)}"
            + (f" ({', '.join(overlap)})" if overlap else ""),
            file=out,
        )


def render_summary(results: list[dict], out) -> None:
    print(
        f"AOP-Wiki snapshot {SNAPSHOT}; {len(results)} dismech entries with parkinsonian phenotypes\n",
        file=out,
    )
    print("Key Event presence", file=out)
    for ke, label in KES.items():
        n = sum(1 for r in results if r["key_events"][ke])
        print(f"  KE{ke:<5} {label:<52} {n:>3}/{len(results)}", file=out)

    print("\nKey Event Relationship coverage", file=out)
    for ker, (up, down, aops, refs) in KERS.items():
        counts: dict[str, int] = {}
        for r in results:
            status = r["kers"][ker]["status"]
            counts[status] = counts.get(status, 0) + 1
        cited = "cited" if refs else "UNCITED"
        print(
            f"  KER{ker:<5} KE{up}->KE{down} (AOP {','.join(aops)}; {cited})"
            f"  direct={counts.get('direct', 0)} indirect={counts.get('indirect', 0)}"
            f" same-node={counts.get('same node', 0)} no-path={counts.get('no path', 0)}"
            f" absent={counts.get('key event absent', 0)}",
            file=out,
        )

    stranded = [
        r for r in results if r["phenotype_connectivity"]["parkinsonian_stranded"]
    ]
    print(
        f"\nEntries whose parkinsonian phenotypes no causal edge explains: "
        f"{len(stranded)}/{len(results)}",
        file=out,
    )
    for r in sorted(
        stranded,
        key=lambda r: -len(r["phenotype_connectivity"]["parkinsonian_stranded"]),
    ):
        pc = r["phenotype_connectivity"]
        pct = 100 * pc["connected"] / pc["total"] if pc["total"] else 0
        print(
            f"  {Path(r['path']).stem[:50]:<50} entry {pct:5.1f}%  "
            f"stranded: {', '.join(pc['parkinsonian_stranded'])}",
            file=out,
        )


def render_tsv(results: list[dict], out) -> None:
    print("entry\tker\tupstream_ke\tdownstream_ke\tstatus\tdetail", file=out)
    for r in results:
        for ker, (up, down, _, _) in KERS.items():
            info = r["kers"][ker]
            detail = json.dumps(
                info.get("edges")
                or info.get("path")
                or info.get("nodes")
                or info.get("absent")
                or ""
            )
            print(
                f"{Path(r['path']).stem}\tKER{ker}\tKE{up}\tKE{down}\t{info['status']}\t{detail}",
                file=out,
            )


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--root", type=Path, default=Path.cwd(), help="dismech checkout (default: cwd)"
    )
    parser.add_argument(
        "--format", choices=["summary", "json", "tsv"], default="summary"
    )
    args = parser.parse_args()

    paths = select_records(args.root)
    results = [crosswalk(load_document(p), p.relative_to(args.root)) for p in paths]
    sweep = respiratory_complex_sweep(args.root)

    if args.format == "json":
        json.dump(
            {
                "snapshot": SNAPSHOT,
                "aops": AOPS,
                "key_events": KES,
                "respiratory_complex_sweep": sweep,
                "entries": results,
            },
            sys.stdout,
            indent=1,
        )
        print()
    elif args.format == "tsv":
        render_tsv(results, sys.stdout)
    else:
        render_summary(results, sys.stdout)
        render_complex_sweep(results, sweep, sys.stdout)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
