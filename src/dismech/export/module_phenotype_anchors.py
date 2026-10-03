"""Module -> phenotype anchor matrix via pathograph-branch attribution.

The mechanism-module map (``dismech.export.module_map``) gives each module its
intrinsic CL/GO mechanism signature and the full disease<->module incidence, but
it deliberately stops short of attributing *phenotypes* to modules, because a
disease that conforms to several modules must not have all its phenotypes
blanket-assigned to every one -- that would reintroduce the mechanism conflation
the module factorization exists to avoid.

This exporter does that attribution correctly, by causal branch. For every
``conforms_to`` edge it walks **downstream** from the conforming pathophysiology
node, through the disease's own pathograph, to the phenotype nodes that node's
branch actually reaches -- and credits those phenotypes to the module. Aggregated
across every disease that conforms to a module, the result is the module's
*clinical* signature: which HPO phenotypes this mechanism produces, and in how
many conforming diseases.

That completes the supervised anchor matrix the mechanism-module factor model
needs (module -> phenotype, the factor->observable loadings), and it is a
standalone cross-disease view in its own right: "what does the fibrotic module
produce clinically, and where".

Source of the causal graph: the exported ``pathographs/MONDO_*.json`` (phenotype
nodes carry ``meta.term_id``; edges carry a predicate), the same artifacts
``synthvae_export`` reads. Coverage against the incidence is reported, since a
disease curated since the last page build may have no pathograph yet.
"""
from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from dismech.export import module_map

# Predicates along which disease progression flows downstream to phenotypes.
PROGRESSION_PREDICATES = frozenset({"causes", "leads_to", "contributes_to"})


class _PathographCache:
    """Load and index pathograph JSONs once each, keyed by MONDO id."""

    def __init__(self, pathograph_dir: Path) -> None:
        self._dir = pathograph_dir
        self._cache: dict[str, dict | None] = {}

    def _find(self, disease_mondo: str) -> Path | None:
        stem = disease_mondo.replace(":", "_")
        exact = self._dir / f"{stem}.json"
        if exact.exists():
            return exact
        matches = sorted(self._dir.glob(f"{stem}.json")) or sorted(
            self._dir.glob(f"{stem}__*.json")
        )
        return matches[0] if matches else None

    def downstream_phenotypes(
        self, disease_mondo: str, start_node: str
    ) -> list[tuple[str, str]] | None:
        """HP (id, label) phenotypes reachable downstream of ``start_node``.

        Returns None when no pathograph is found or the node is absent from it
        (so the caller can distinguish "no pathograph" from "branch is a dead
        end with no phenotype").
        """
        graph = self._load(disease_mondo)
        if graph is None:
            return None
        node_type = graph["node_type"]
        if start_node not in node_type:
            return None
        adj = graph["adjacency"]
        pheno_term = graph["pheno_term"]

        seen = {start_node}
        frontier = list(adj.get(start_node, ()))
        out: list[tuple[str, str]] = []
        while frontier:
            cur = frontier.pop()
            if cur in seen:
                continue
            seen.add(cur)
            if cur in pheno_term:
                out.append(pheno_term[cur])
            frontier.extend(adj.get(cur, ()))
        return out

    def _load(self, disease_mondo: str) -> dict | None:
        if disease_mondo in self._cache:
            return self._cache[disease_mondo]
        path = self._find(disease_mondo)
        graph: dict | None = None
        if path is not None:
            try:
                raw = json.loads(path.read_text())
            except (OSError, ValueError):
                raw = None
            if raw is not None:
                node_type = {n["id"]: n.get("node_type") for n in raw.get("nodes", [])}
                adjacency: dict[str, list[str]] = defaultdict(list)
                for e in raw.get("edges", []):
                    if e.get("predicate") in PROGRESSION_PREDICATES:
                        adjacency[e["source"]].append(e["target"])
                pheno_term: dict[str, tuple[str, str]] = {}
                for n in raw.get("nodes", []):
                    if n.get("node_type") == "phenotype":
                        hp = (n.get("meta") or {}).get("term_id")
                        if isinstance(hp, str) and hp.startswith("HP:"):
                            pheno_term[n["id"]] = (hp, n["id"])
                graph = {
                    "node_type": node_type,
                    "adjacency": adjacency,
                    "pheno_term": pheno_term,
                }
        self._cache[disease_mondo] = graph
        return graph


def build(
    modules_dir: Path, disorders_dir: Path, pathograph_dir: Path
) -> dict[str, Any]:
    """Attribute phenotypes to modules by walking each conforming branch."""
    mm = module_map.build(modules_dir, disorders_dir)
    cache = _PathographCache(pathograph_dir)

    # module -> hpo_id -> {label, diseases:set}
    anchors: dict[str, dict[str, dict[str, Any]]] = defaultdict(
        lambda: defaultdict(lambda: {"label": "", "diseases": set()})
    )
    cov = {
        "resolved_edges": 0,
        "edges_no_mondo": 0,
        "edges_no_pathograph": 0,
        "edges_node_absent": 0,
        "edges_reached_phenotype": 0,
    }

    for row in mm["incidence"]:
        if not row["resolves"]:
            continue
        cov["resolved_edges"] += 1
        mondo = row.get("disease_mondo")
        node = row.get("disorder_node")
        if not mondo or not node:
            cov["edges_no_mondo"] += 1
            continue
        reached = cache.downstream_phenotypes(mondo, node)
        if reached is None:
            # distinguish no-pathograph from node-absent for the audit
            if cache._load(mondo) is None:
                cov["edges_no_pathograph"] += 1
            else:
                cov["edges_node_absent"] += 1
            continue
        if reached:
            cov["edges_reached_phenotype"] += 1
        for hpo_id, label in reached:
            slot = anchors[row["module"]][hpo_id]
            slot["label"] = label
            slot["diseases"].add(row["disease"])

    # finalize: sort each module's phenotypes by # conforming diseases
    result_modules: dict[str, list[dict[str, Any]]] = {}
    for mod, phens in anchors.items():
        rows = [
            {
                "hpo_id": hp,
                "label": v["label"],
                "n_diseases": len(v["diseases"]),
                "diseases": sorted(v["diseases"]),
            }
            for hp, v in phens.items()
        ]
        rows.sort(key=lambda r: (-r["n_diseases"], r["hpo_id"]))
        result_modules[mod] = rows

    return {
        "modules": result_modules,
        "coverage": cov,
        "n_modules_with_phenotype_anchors": len(result_modules),
    }


def write_outputs(result: dict[str, Any], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "module_phenotype_anchors.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    with (out_dir / "module_phenotype_anchors.tsv").open("w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["module", "hpo_id", "label", "n_diseases"])
        for mod in sorted(result["modules"]):
            for r in result["modules"][mod]:
                w.writerow([mod, r["hpo_id"], r["label"], r["n_diseases"]])


def _print_summary(result: dict[str, Any]) -> None:
    c = result["coverage"]
    print("=" * 64)
    print("MODULE -> PHENOTYPE ANCHORS (pathograph-branch attribution)")
    print("=" * 64)
    print(f"modules with >=1 phenotype anchor : {result['n_modules_with_phenotype_anchors']}")
    print(f"resolved conforms_to edges        : {c['resolved_edges']}")
    print(f"  edge's branch reached a phenotype : {c['edges_reached_phenotype']}")
    print(f"  no pathograph for disease         : {c['edges_no_pathograph']}")
    print(f"  conforming node absent in graph   : {c['edges_node_absent']}")
    print(f"  edge had no MONDO/node            : {c['edges_no_mondo']}")
    top = sorted(
        result["modules"].items(),
        key=lambda kv: -sum(r["n_diseases"] for r in kv[1]),
    )[:12]
    print("\nmodules with the richest clinical signature (sum of disease hits):")
    for mod, rows in top:
        lead = ", ".join(f"{r['label']}({r['n_diseases']})" for r in rows[:3])
        print(f"  {mod}: {lead}")
    print("=" * 64)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--modules-dir", type=Path, default=Path("kb/modules"))
    ap.add_argument("--disorders-dir", type=Path, default=Path("kb/disorders"))
    ap.add_argument("--pathograph-dir", type=Path, default=Path("pathographs"))
    ap.add_argument(
        "--out-dir", type=Path, default=Path("output/module_map")
    )
    args = ap.parse_args()
    result = build(args.modules_dir, args.disorders_dir, args.pathograph_dir)
    write_outputs(result, args.out_dir)
    _print_summary(result)
    print(f"\nwrote module_phenotype_anchors.json + .tsv -> {args.out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
