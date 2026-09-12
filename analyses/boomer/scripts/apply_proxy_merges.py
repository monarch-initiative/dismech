"""Migrate saved Mendelian inputs using pinned MONDO proxy-merge annotations.

Preflight all inputs before writing. Preserve hypotheses, baseline inputs and
solution hashes; mark changed results stale until the separate solver rerun.
Existing migration manifests are immutable and checked on repeat invocation.
"""

from __future__ import annotations

import argparse
from copy import deepcopy
import csv
import json
from pathlib import Path
import sys

import yaml

from build_analyses import INDEX_FIELDNAMES, REPO
from dismech import kb_cache
from enrich_icd10_inputs import tsv
from proxy_merges import DEFAULT_CATALOG, ProxyPolicy, digest, provenance

FIELDS = (
    "slug",
    "in_scope",
    "mondo",
    "vocabulary",
    "targets",
    "preferred_targets",
    "decision",
)


def migrate(base, disease_dir, policy, validate, graph_sources=None):
    index_path = base / "index.tsv"
    with index_path.open() as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        if reader.fieldnames != list(INDEX_FIELDNAMES):
            raise ValueError("Unexpected Boomer index columns")
        index = list(reader)
    if len({r["slug"] for r in index}) != len(index):
        raise ValueError("Duplicate Boomer index slugs")
    out = base / "proxy-merges"
    manifest_path = out / "updates.json"
    source_hash = digest(json.dumps(policy.catalog, sort_keys=True).encode())
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())
        if manifest["catalog_sha256"] != source_hash:
            raise ValueError("Annotation catalog changed; use a new migration")
        for slug, entry in manifest["inputs"].items():
            path = base / "disorders" / slug / "kb.yaml"
            if digest(path.read_bytes()) != entry["after_input_sha256"]:
                raise ValueError(f"{slug}: input changed since proxy migration")
        print(
            f"Verified {len(manifest['inputs'])} previously migrated inputs; no writes"
        )
        return manifest
    manifest = {
        "catalog_sha256": source_hash,
        "scope": "category: Mendelian",
        "inputs": {},
    }
    decisions, writes, pending = [], {}, []
    for row in index:
        slug = row["slug"]
        folder = base / "disorders" / slug
        path = folder / "kb.yaml"
        before = path.read_bytes()
        kb = kb_cache.load_document(path)
        disease = kb_cache.load_document(disease_dir / f"{slug}.yaml")
        in_scope = disease.get("category") == "Mendelian"
        rows = policy.decisions(kb)
        decisions.extend(
            {
                "slug": slug,
                "in_scope": in_scope,
                **{
                    k: "|".join(v) if isinstance(v, list) else v
                    for k, v in decision.items()
                },
            }
            for decision in rows
        )
        if not in_scope or not any(r["decision"] == "PERMIT_PROXY_MERGE" for r in rows):
            continue
        updated = deepcopy(kb)
        policy.apply(updated)
        if updated == kb:
            continue
        assert updated["pfacts"] == kb["pfacts"]
        assert updated.get("labels") == kb.get("labels")
        validate(updated)
        after = yaml.safe_dump(updated, sort_keys=False).encode()
        baseline = {}
        solution_hashes = {}
        if row["status"] != "NOT_RUN":
            for name in ("solution.yaml", "solution.md"):
                solution_hashes[name] = digest((folder / name).read_bytes())
            solution = kb_cache.load_document(folder / "solution.yaml")
            baseline = {
                key: solution.get(key)
                for key in (
                    "confidence",
                    "posterior_prob",
                    "number_of_satisfiable_combinations",
                    "timed_out",
                )
            }
            baseline["assignment"] = [
                p["truth_value"] for p in solution.get("solved_pfacts", [])
            ]
            # Retain the exact saved baseline for the existing low-confidence experiment.
            if slug in {"CANVAS", "Methylcobalamin_Deficiency_Type_cblE"}:
                writes[out / "baseline" / slug / "solution.yaml"] = (
                    folder / "solution.yaml"
                ).read_bytes()
        elif any((folder / name).exists() for name in ("solution.yaml", "solution.md")):
            raise ValueError(f"{slug}: NOT_RUN input unexpectedly has solution files")
        manifest["inputs"][slug] = {
            "before_input_sha256": digest(before),
            "after_input_sha256": digest(after),
            "previous_index": dict(row),
            "previous_solution_sha256": solution_hashes,
            "baseline": baseline,
        }
        writes[out / "baseline" / slug / "kb.yaml"] = before
        writes[path] = after
        writes[folder / "proxy-merges.json"] = (
            json.dumps(
                provenance(updated, policy, after, graph_sources),
                indent=2,
            )
            + "\n"
        ).encode()
        readme = folder / "README.md"
        original = readme.read_text()
        link = "MONDO proxy-merge exceptions: [annotations and decisions](proxy-merges.json).\n\n"
        # Keep provenance above the replaceable result section when solving later.
        if "## What boomer did" in original:
            original = original.replace(
                "## What boomer did", link + "## What boomer did", 1
            )
        else:
            original += "\n" + link
        if row["status"] != "NOT_RUN":
            original = (
                "> **STALE INPUT:** MONDO proxy-merge constraints changed after the saved solve.\n"
                "> The saved solutions below describe the previous input only; rerun the solver.\n"
                "> [Input hashes and previous results](../../proxy-merges/updates.json)\n\n"
            ) + original
            row["status"] = "STALE_INPUT"
        row["n_retracted"] = "NA"
        writes[readme] = original.encode()
        pending.append(
            {"slug": slug, "status": row["status"], "input_sha256": digest(after)}
        )
    writes[out / "decisions.tsv"] = tsv(decisions, FIELDS)
    writes[out / "pending.tsv"] = tsv(pending, ("slug", "status", "input_sha256"))
    writes[manifest_path] = (json.dumps(manifest, indent=2) + "\n").encode()
    ending = "\r\n" if b"\r\n" in index_path.read_bytes() else "\n"
    writes[index_path] = tsv(index, INDEX_FIELDNAMES, ending)
    for path, content in writes.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists() or path.read_bytes() != content:
            path.write_bytes(content)
    print(
        f"Migrated {len(pending)} Mendelian inputs; mapping hypotheses and priors unchanged"
    )
    return manifest


def main():
    kb_cache.default_off()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", type=Path, default=REPO / "analyses/boomer")
    parser.add_argument("--kb-dir", type=Path, default=REPO / "kb/disorders")
    parser.add_argument("--mapping-annotations", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--boomer-src", type=Path, required=True)
    args = parser.parse_args()
    sys.path.insert(0, str(args.boomer_src.expanduser()))
    from boomer.model import KB

    # These are historical graph snapshots, not a claim to have refreshed the graph.
    graph_sources = {
        "description": "Existing saved input graphs retained; only annotation policy refreshed",
        "snapshots": json.loads((args.base / "icd10/current/summary.json").read_text())[
            "snapshots"
        ]
        if (args.base / "icd10/current/summary.json").exists()
        else None,
    }
    migrate(
        args.base,
        args.kb_dir,
        ProxyPolicy.load(args.mapping_annotations),
        KB.model_validate,
        graph_sources,
    )


if __name__ == "__main__":
    main()
