"""Rank current completed Boomer results and explain residual low-confidence cases.

Read-only with respect to production inputs/results. Enumerate distinct Boolean
assignments, then test namespace-only and hypothetical full proxy relaxations.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sqlite3
import subprocess
import sys
from collections import Counter
from copy import deepcopy
from math import isclose
from pathlib import Path

from investigate_ties import enumerate_worlds, render_alternatives
from proxy_merges import REPO, ProxyPolicy
from solve_pending import table

from dismech import kb_cache

SOLVER = "744038e30741009930f57919ca2f03c6473ed198"
DOID_SHA256 = "e729a25090b71f8d71be3e1f5ad3cf8c51d2ba7fb8232ca4ab12ecf4be633db9"
COMPLETE = {"ALL_MAPPINGS_CONSISTENT", "RETRACTED"}
FIELDS = (
    "slug",
    "confidence",
    "status",
    "n_pfacts",
    "vocabulary",
    "targets",
    "target_labels",
    "strict_edge_in_input",
    "namespace_relaxed_confidence",
    "hypothetical_proxy_confidence",
    "input_sha256",
)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def select(base):
    selected, excluded, counts = [], Counter(), Counter()
    with (base / "index.tsv").open() as stream:
        index = list(csv.DictReader(stream, delimiter="\t"))
    for row in index:
        folder = base / "disorders" / row["slug"]
        if row["status"] not in COMPLETE:
            excluded[row["status"]] += 1
            continue
        metadata_path = folder / "solve.json"
        metadata = (
            json.loads(metadata_path.read_text()) if metadata_path.exists() else {}
        )
        if metadata.get("boomer_commit") != SOLVER:
            excluded["OLD_SOLVER"] += 1
            continue
        if metadata.get("input_sha256") != sha(folder / "kb.yaml"):
            excluded["STALE_INPUT"] += 1
            continue
        if metadata.get("status") != row["status"] or not metadata.get(
            "solution_written"
        ):
            raise ValueError(f"{row['slug']}: inconsistent solve metadata")
        solution = kb_cache.load_document(folder / "solution.yaml")
        assert not solution.get("timed_out")
        counts[str(solution["confidence"])] += 1
        if solution["confidence"] < 0.9:
            selected.append((row, folder, solution))
    return selected, {
        "completed_current": sum(counts.values()),
        "confidence_counts": dict(sorted(counts.items())),
        "excluded": dict(sorted(excluded.items())),
    }


def inspect_case(row, folder, saved, policy, model, reasoner):
    path = folder / "kb.yaml"
    original = path.read_bytes()
    data = kb_cache.load_document(path)
    kb = model.KB.model_validate(data)
    baseline = enumerate_worlds(kb, model, reasoner)
    baseline["saved_assignment"] = [p["truth_value"] for p in saved["solved_pfacts"]]
    assert baseline["saved_assignment"] in baseline["optimal_assignments"]
    assert baseline["confidence"] == saved["confidence"]
    assert baseline["distinct_solutions"] == saved["number_of_satisfiable_combinations"]
    assert isclose(baseline["best_posterior"], saved["posterior_prob"], abs_tol=1e-11)
    for marginal, pfact in zip(
        baseline["marginals"], saved["solved_pfacts"], strict=True
    ):
        assert isclose(marginal, pfact["posterior_prob"], abs_tol=1e-11)
    entry = {
        "input_sha256": sha(path),
        "solution_sha256": sha(folder / "solution.yaml"),
        "status": row["status"],
        "labels": deepcopy(data["labels"]),
        "hypotheses": [
            {"index": i, "fact": p.fact.model_dump(), "prior": p.prob}
            for i, p in enumerate(kb.pfacts)
        ],
        "baseline": baseline,
        "mapping_decisions": policy.decisions(data),
        "conflicts": [],
    }
    for decision in entry["mapping_decisions"]:
        if decision["decision"] == "PERMIT_PROXY_MERGE":
            continue
        pair = set(decision["targets"])
        # The current residual cohort has exactly one competing pair per case.
        assert len(pair) == 2
        indices = [
            i
            for i, p in enumerate(kb.pfacts)
            if p.fact.fact_type == "EquivalentTo"
            and p.fact.sub == decision["mondo"]
            and p.fact.equivalent in pair
        ]
        assert len(indices) == 2
        choices = [(i, True) for i in indices]
        assert not reasoner.reason(kb, choices).satisfiable
        namespace = [
            f
            for f in kb.facts
            if f.fact_type == "MemberOfDisjointGroup"
            and f.group == decision["vocabulary"]
        ]
        assert {f.sub for f in namespace} == pair
        namespace_relaxed = kb.model_copy(deep=True)
        namespace_relaxed.facts = [
            f for f in namespace_relaxed.facts if f not in namespace
        ]
        strict = [
            f
            for f in namespace_relaxed.facts
            if f.fact_type == "ProperSubClassOf" and {f.sub, f.sup} == pair
        ]
        proxy = namespace_relaxed.model_copy(deep=True)
        proxy.facts = [
            model.SubClassOf(sub=f.sub, sup=f.sup) if f in strict else f
            for f in proxy.facts
        ]
        conflict = {
            "mondo": decision["mondo"],
            "vocabulary": decision["vocabulary"],
            "targets": decision["targets"],
            "indices": indices,
            "namespace_constraints": [f.model_dump() for f in namespace],
            "strict_edges_in_saved_input": [f.model_dump() for f in strict],
            "namespace_only_relaxation": enumerate_worlds(
                namespace_relaxed, model, reasoner
            ),
            "namespace_only_all_equivalences_possible": reasoner.reason(
                namespace_relaxed, choices
            ).satisfiable,
            "hypothetical_proxy_relaxation": enumerate_worlds(proxy, model, reasoner),
            "hypothetical_proxy_all_equivalences_possible": reasoner.reason(
                proxy, choices
            ).satisfiable,
        }
        entry["conflicts"].append(conflict)
    assert path.read_bytes() == original
    return entry


def local_context(cases, oak_dir):
    """Pin the source context behind the saved constraints, including sibling subtypes."""
    terms = {"mondo": set(), "doid": set(), "mesh": set(), "icd11f": set()}
    for entry in cases.values():
        for hypothesis in entry["hypotheses"]:
            for value in hypothesis["fact"].values():
                if isinstance(value, str) and ":" in value:
                    prefix = value.split(":")[0].lower()
                    if prefix in terms:
                        terms[prefix].add(value)
    output = {}
    for prefix, subjects in terms.items():
        path = (oak_dir / f"{prefix}.db").resolve()
        con = sqlite3.connect(f"{path.as_uri()}?mode=ro", uri=True)
        records = {}
        for subject in sorted(subjects):
            children = [
                s
                for (s,) in con.execute(
                    "SELECT subject FROM statements WHERE predicate='rdfs:subClassOf' AND object=?",
                    (subject,),
                )
                if not s.startswith("_:")
            ]
            inspect = {subject, *children}
            for term in sorted(inspect):
                records[term] = [
                    list(r)
                    for r in con.execute(
                        "SELECT predicate, object, value FROM statements WHERE subject=? AND predicate IN ('rdfs:label','IAO:0000115','rdfs:subClassOf','oio:hasExactSynonym','oio:hasDbXref','skos:exactMatch','owl:deprecated','IAO:0100001') ORDER BY predicate,object,value",
                        (term,),
                    )
                ]
        output[prefix] = {
            "version": [
                o or v
                for o, v in con.execute(
                    "SELECT object,value FROM statements WHERE predicate='owl:versionIRI'"
                )
            ],
            "terms": records,
        }
        con.close()
    return output


def extract_source(path, wanted, url):
    import fastobo

    return {
        "url": url,
        "sha256": sha(path),
        "stanzas": {
            str(frame.id): str(frame)
            for frame in fastobo.iter(path)
            if str(frame.id) in wanted
        },
    }


def main():
    kb_cache.default_off()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--boomer-src", type=Path, required=True)
    parser.add_argument("--base", type=Path, default=REPO / "analyses/boomer")
    parser.add_argument("--oak-dir", type=Path, default=Path.home() / ".data/oaklib")
    parser.add_argument(
        "--out", type=Path, default=REPO / "analyses/boomer/remaining-low-confidence"
    )
    parser.add_argument("--mondo-obo", type=Path, required=True)
    parser.add_argument("--doid-obo", type=Path, required=True)
    args = parser.parse_args()
    source = args.boomer_src.expanduser().resolve()
    commit = subprocess.check_output(
        ["git", "-C", str(source), "rev-parse", "HEAD"], text=True
    ).strip()
    assert commit == SOLVER
    assert not subprocess.check_output(
        ["git", "-C", str(source), "status", "--porcelain"], text=True
    ).strip()
    sys.path.insert(0, str(source))
    from boomer import model, search

    selected, summary = select(args.base)
    reasoner = search.get_reasoner(model.SearchConfig().reasoner_class)
    policy = ProxyPolicy.load()
    cases = {
        row["slug"]: inspect_case(row, folder, saved, policy, model, reasoner)
        for row, folder, saved in selected
    }
    context = local_context(cases, args.oak_dir)
    source_context = {
        "mondo": extract_source(
            args.mondo_obo, set(context["mondo"]["terms"]), policy.catalog["source_url"]
        ),
        "doid": extract_source(
            args.doid_obo,
            set(context["doid"]["terms"]),
            "https://raw.githubusercontent.com/DiseaseOntology/HumanDiseaseOntology/ec05d8346757d228193d33e6ef7a565f430ebe39/src/ontology/doid.obo",
        ),
    }
    assert source_context["mondo"]["sha256"] == policy.catalog["source_sha256"]
    assert source_context["doid"]["sha256"] == DOID_SHA256
    rows = []
    for slug, entry in cases.items():
        conflicts = entry["conflicts"]
        conflict = conflicts[0] if conflicts else {}
        assert len(conflicts) <= 1
        rows.append(
            {
                "slug": slug,
                "confidence": entry["baseline"]["confidence"],
                "status": entry["status"],
                "n_pfacts": len(entry["hypotheses"]),
                "vocabulary": conflict.get("vocabulary", "NA"),
                "targets": "|".join(conflict.get("targets", [])) or "NA",
                "target_labels": "|".join(
                    entry["labels"][t] for t in conflict.get("targets", [])
                )
                or "NA",
                "strict_edge_in_input": bool(
                    conflict.get("strict_edges_in_saved_input")
                ),
                "namespace_relaxed_confidence": conflict.get(
                    "namespace_only_relaxation", {}
                ).get("confidence", "NA"),
                "hypothetical_proxy_confidence": conflict.get(
                    "hypothetical_proxy_relaxation", {}
                ).get("confidence", "NA"),
                "input_sha256": entry["input_sha256"],
            }
        )
    args.out.mkdir(parents=True, exist_ok=True)
    for name, data in (
        ("summary", summary),
        ("experiments", {"boomer_commit": commit, "cases": cases}),
        ("local-source-context", context),
        ("current-source-context", source_context),
    ):
        (args.out / f"{name}.json").write_text(json.dumps(data, indent=2) + "\n")
    (args.out / "triage.tsv").write_text(table(rows, FIELDS))
    for slug, entry in cases.items():
        (args.out / f"{slug}-alternatives.md").write_text(
            render_alternatives(slug, entry)
        )
    print(json.dumps(summary, indent=2))
    for row in rows:
        print(
            row["slug"],
            row["confidence"],
            row["namespace_relaxed_confidence"],
            row["hypothetical_proxy_confidence"],
        )


if __name__ == "__main__":
    main()
