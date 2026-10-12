"""Mechanism-module map: assemble dismech's curated cross-disease mechanism layer.

dismech curates ~90 mechanism modules (``kb/modules/``) and hundreds of
``conforms_to`` edges linking disorder pathophysiology nodes to module nodes, but
that layer is only ever used as a per-file consistency check -- never assembled
into a queryable whole. This extractor builds it:

1. **module -> mechanism signature** -- the CL / GO / UBERON / gene terms each
   module emits across its pathophysiology nodes. Modules encode mechanism (cell
   types + processes), *not* phenotypes, by design -- HP phenotype anchors are
   contributed by the conforming diseases' nodes, not the module itself, so the
   module -> phenotype anchor is a downstream construction over the pathograph
   (deliberately not naively aggregated here: a multi-module disease's phenotypes
   must be attributed by causal branch, not blanket-assigned to every module).
2. **disease <-> module incidence** -- which disorders conform to which modules,
   at which node, resolved against the module's actual node names;
3. **an audit** -- unused modules, modules with no intrinsic HP term (expected),
   unresolved ``conforms_to`` targets, diseases conforming to many modules, and
   terms shared across modules.

This is the standalone, browsable mechanism map *and* the supervised anchor
scaffold the mechanism-module factor model (mechanism-as-hidden-variable) needs:
module -> CL/GO signatures are the factor anchors, disease -> module incidence is
the observed loading matrix.
"""
from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml

try:  # libyaml when available (~10x faster over the whole KB), else pure Python
    from yaml import CSafeLoader as _SafeLoader
except ImportError:  # pragma: no cover
    from yaml import SafeLoader as _SafeLoader


def safe_load_path(path: Path) -> Any:
    """Load a YAML file with the fastest available safe loader."""
    with open(path) as stream:
        return yaml.load(stream, Loader=_SafeLoader)


# Ontology prefixes that make up a module's mechanism signature.
SIGNATURE_PREFIXES = ("HP", "CL", "GO", "UBERON", "hgnc")


def _bucket_terms(obj: Any, out: dict[str, set[str]]) -> None:
    """Recursively collect {id: CURIE} terms, bucketed by ontology prefix."""
    if isinstance(obj, dict):
        tid = obj.get("id")
        if isinstance(tid, str) and ":" in tid:
            prefix = tid.split(":", 1)[0]
            if prefix in SIGNATURE_PREFIXES:
                out.setdefault(prefix, set()).add(tid)
        for v in obj.values():
            _bucket_terms(v, out)
    elif isinstance(obj, list):
        for v in obj:
            _bucket_terms(v, out)


def _first_line(text: str | None) -> str:
    if not text:
        return ""
    return " ".join(str(text).split())[:200]


def module_signature(module_path: Path) -> dict[str, Any]:
    """Extract one module's mechanism signature (aggregate + per node)."""
    data = safe_load_path(module_path) or {}
    nodes = data.get("pathophysiology") or []
    node_names: list[str] = []
    per_node: list[dict[str, Any]] = []
    agg: dict[str, set[str]] = {}
    for node in nodes:
        if not isinstance(node, dict):
            continue
        name = node.get("name")
        if name:
            node_names.append(str(name))
        nterms: dict[str, set[str]] = {}
        _bucket_terms(node, nterms)
        for p, s in nterms.items():
            agg.setdefault(p, set()).update(s)
        per_node.append(
            {"name": name, "terms": {p: sorted(s) for p, s in sorted(nterms.items())}}
        )
    # module-level phenotypes (rare, but count them toward the signature)
    _bucket_terms(data.get("phenotypes") or [], agg)

    signature = {p: sorted(s) for p, s in sorted(agg.items())}
    return {
        "module": module_path.stem,
        "name": data.get("name") or module_path.stem,
        "description": _first_line(data.get("description")),
        "n_nodes": len(node_names),
        "node_names": node_names,
        "signature": signature,
        "n_hp": len(signature.get("HP", [])),
        "n_cl": len(signature.get("CL", [])),
        "n_go": len(signature.get("GO", [])),
        "nodes": per_node,
    }


def _iter_conforms(obj: Any, disorder_node: str | None = None):
    """Yield (conforms_to_string, enclosing_node_name) for every conforms_to found."""
    if isinstance(obj, dict):
        name = obj.get("name") if isinstance(obj.get("name"), str) else disorder_node
        ct = obj.get("conforms_to")
        if isinstance(ct, str) and ct.strip():
            yield ct.strip(), obj.get("name") or disorder_node
        for v in obj.values():
            yield from _iter_conforms(v, name)
    elif isinstance(obj, list):
        for v in obj:
            yield from _iter_conforms(v, disorder_node)


def _parse_conforms(ref: str) -> tuple[str, str | None]:
    """Split 'module_stem#Node Name' -> (stem, node) ; node None if absent."""
    if "#" in ref:
        stem, node = ref.split("#", 1)
        return stem.strip(), node.strip()
    return ref.strip(), None


def build(modules_dir: Path, disorders_dir: Path) -> dict[str, Any]:
    """Assemble module signatures + disease<->module incidence + audit."""
    modules: dict[str, dict[str, Any]] = {}
    module_nodes: dict[str, set[str]] = {}
    for mp in sorted(modules_dir.glob("*.yaml")):
        if mp.name.endswith(".history.yaml"):
            continue
        sig = module_signature(mp)
        modules[sig["module"]] = sig
        module_nodes[sig["module"]] = set(sig["node_names"])

    incidence: list[dict[str, Any]] = []
    unresolved: list[dict[str, Any]] = []
    for dp in sorted(disorders_dir.glob("*.yaml")):
        if dp.name.endswith(".history.yaml"):
            continue
        data = safe_load_path(dp) or {}
        disease = data.get("name") or dp.stem
        mondo = (((data.get("disease_term") or {}).get("term") or {}).get("id"))
        for ref, dnode in _iter_conforms(data.get("pathophysiology") or []):
            stem, mnode = _parse_conforms(ref)
            stem_ok = stem in modules
            node_ok = stem_ok and (mnode is None or mnode in module_nodes[stem])
            row = {
                "disease": disease,
                "disease_mondo": mondo,
                "module": stem,
                "module_node": mnode,
                "disorder_node": dnode,
                "resolves": bool(stem_ok and node_ok),
            }
            incidence.append(row)
            if not row["resolves"]:
                unresolved.append(
                    {**row, "reason": "unknown module" if not stem_ok else "unknown node"}
                )

    module_to_diseases: dict[str, list[str]] = defaultdict(list)
    disease_to_modules: dict[str, set[str]] = defaultdict(set)
    for r in incidence:
        module_to_diseases[r["module"]].append(r["disease"])
        disease_to_modules[r["disease"]].add(r["module"])

    # term -> modules that carry it (cross-module reuse)
    term_to_modules: dict[str, set[str]] = defaultdict(set)
    for stem, sig in modules.items():
        for terms in sig["signature"].values():
            for t in terms:
                term_to_modules[t].add(stem)
    shared_terms = {t: sorted(ms) for t, ms in term_to_modules.items() if len(ms) > 1}

    used = {r["module"] for r in incidence if r["resolves"]}
    audit = {
        "n_modules": len(modules),
        "n_conforms_edges": len(incidence),
        "n_edges_resolved": sum(1 for r in incidence if r["resolves"]),
        "n_diseases_conforming": len(disease_to_modules),
        "modules_used": len(used),
        "modules_unused": sorted(set(modules) - used),
        "modules_without_intrinsic_hp": sorted(
            m for m, s in modules.items() if s["n_hp"] == 0
        ),
        "unresolved_conforms": unresolved,
        "top_diseases_by_module_count": Counter(
            {d: len(ms) for d, ms in disease_to_modules.items()}
        ).most_common(15),
        "top_modules_by_disease_count": Counter(
            {m: len(set(ds)) for m, ds in module_to_diseases.items()}
        ).most_common(15),
        "n_terms_shared_across_modules": len(shared_terms),
    }

    return {
        "modules": modules,
        "incidence": incidence,
        "module_to_diseases": {m: sorted(set(ds)) for m, ds in module_to_diseases.items()},
        "disease_to_modules": {d: sorted(ms) for d, ms in disease_to_modules.items()},
        "shared_terms": shared_terms,
        "audit": audit,
    }


def write_outputs(result: dict[str, Any], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "module_map.json").write_text(json.dumps(result, indent=2) + "\n")

    with (out_dir / "module_signatures.tsv").open("w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["module", "name", "n_nodes", "n_hp", "n_cl", "n_go",
                    "n_conformers", "hp_terms", "cl_terms", "go_terms"])
        m2d = result["module_to_diseases"]
        for stem, s in sorted(result["modules"].items()):
            sig = s["signature"]
            w.writerow([
                stem, s["name"], s["n_nodes"], s["n_hp"], s["n_cl"], s["n_go"],
                len(m2d.get(stem, [])),
                "|".join(sig.get("HP", [])), "|".join(sig.get("CL", [])),
                "|".join(sig.get("GO", [])),
            ])

    with (out_dir / "disease_module_incidence.tsv").open("w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["disease", "disease_mondo", "module", "module_node",
                    "disorder_node", "resolves"])
        for r in result["incidence"]:
            w.writerow([r["disease"], r["disease_mondo"] or "", r["module"],
                        r["module_node"] or "", r["disorder_node"] or "", r["resolves"]])


def _print_summary(a: dict[str, Any]) -> None:
    print("=" * 64)
    print("MECHANISM-MODULE MAP")
    print("=" * 64)
    print(f"modules                       : {a['n_modules']}  ({a['modules_used']} used)")
    print(f"conforms_to edges             : {a['n_conforms_edges']}  ({a['n_edges_resolved']} resolve)")
    print(f"diseases conforming           : {a['n_diseases_conforming']}")
    print(f"terms shared across modules   : {a['n_terms_shared_across_modules']}")
    if a["unresolved_conforms"]:
        print(f"\nUNRESOLVED conforms_to ({len(a['unresolved_conforms'])}):")
        for r in a["unresolved_conforms"][:12]:
            print(f"  {r['disease']}: {r['module']}#{r['module_node']}  [{r['reason']}]")
    if a["modules_without_intrinsic_hp"]:
        print(
            f"\nmodules with no intrinsic HP term (expected — modules encode "
            f"CL/GO mechanism): {len(a['modules_without_intrinsic_hp'])}/{a['n_modules']}"
        )
    print("\ntop modules by # conforming diseases:")
    for m, c in a["top_modules_by_disease_count"]:
        print(f"  {c:3d}  {m}")
    print("\ndiseases conforming to the most modules:")
    for d, c in a["top_diseases_by_module_count"]:
        print(f"  {c:3d}  {d}")
    print("=" * 64)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--modules-dir", type=Path, default=Path("kb/modules"))
    ap.add_argument("--disorders-dir", type=Path, default=Path("kb/disorders"))
    ap.add_argument("--out-dir", type=Path, default=Path("output/module_map"))
    args = ap.parse_args()
    result = build(args.modules_dir, args.disorders_dir)
    write_outputs(result, args.out_dir)
    _print_summary(result["audit"])
    print(f"\nwrote module_map.json + 2 TSVs -> {args.out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
