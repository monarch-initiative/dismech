"""Five controlled follow-ups: source refresh, proposed scope repair and controls.

Capture uses pinned DisMech blobs, semantic-sql files and pinned source OBO files.
All subsequent stages use the frozen projections. The first pilot is read-only.
"""

from __future__ import annotations

import argparse
import json
import os
from copy import deepcopy
from pathlib import Path

import omimps_pilots as pilot
import yaml
from proxy_merges import extract

OUT = pilot.REPO / "analyses/boomer/omimps-followup"
BASE = "e22a6684a2076e5eff4e4f6558ef55c82f249c34"
CASES = {
    "gorlin": {
        "ps": "109400",
        "slug": "Gorlin_Syndrome",
        "revision": "0f93e8333acae054726a37ad8a0d65dbf3b0c5b7",
        "do_targets": ["DOID:2512", "DOID:0070365"],
        "subjects": ["MONDO:0007187", "MONDO:0958174"],
    },
    "praas": {
        "ps": "256040",
        "slug": "Proteasome_Associated_Autoinflammatory_Syndrome",
        "revision": "f923d7630deda4d7a0ef50e02f3b41568564e6a8",
        "do_targets": ["DOID:0060913", "DOID:0050553"],
        "subjects": ["MONDO:0009726", "MONDO:0054698"],
    },
    "tpmt": {
        "ps": "610460",
        "slug": "Thiopurine_S-methyltransferase_Deficiency",
        "revision": "4154918d9967242bca0c68972680e9d7e90ee605",
        "do_targets": ["DOID:0061004", "DOID:0080172"],
        "subjects": ["MONDO:0012503"],
    },
    "foxe3": {
        "ps": "107250",
        "slug": "FOXE3_Anterior_Segment_Dysgenesis",
        "revision": "4a5e3803772c52801fd00b4116e6e061e1ee7e56",
        "do_targets": [],
        "subjects": [],
    },
    "waldenstrom": {
        "ps": "153600",
        "slug": "Waldenstrom_Macroglobulinemia",
        "revision": "2d9b2e5c35c3471a85b2690a8dff3e72573785d1",
        "do_targets": [],
        "subjects": [],
    },
}


def source_records(path, selected):
    import fastobo

    result = {}
    for frame in fastobo.iter(path):
        term = str(frame.id)
        if term not in selected:
            continue
        record = {
            "label": None,
            "definition": None,
            "parents": [],
            "exact_matches": [],
            "stanza": str(frame),
        }
        for clause in frame:
            if isinstance(clause, fastobo.term.NameClause):
                record["label"] = str(clause.name)
            elif isinstance(clause, fastobo.term.DefClause):
                record["definition"] = str(clause.definition)
            elif isinstance(clause, fastobo.term.IsAClause):
                record["parents"].append(str(clause.term))
        result[term] = record
    if missing := selected - result.keys():
        raise ValueError(f"Missing source terms: {missing}")
    return result


def capture(out, oak, source_dir):
    sources = {name: pilot.Source(oak / f"{name}.db") for name in ("mondo", "omim")}
    mondo, omim = sources["mondo"], sources["omim"]
    manifest = json.loads((source_dir / "manifest.json").read_text())
    for name in ("mondo", "doid"):
        assert (
            pilot.sha((source_dir / f"{name}.obo").read_bytes())
            == manifest[name]["sha256"]
        )
    catalog = pilot.catalog(BASE)
    projections = {}
    selected_mondo = set()
    for case, config in CASES.items():
        revision = pilot.git("rev-parse", config["revision"]).decode().strip()
        path = f"kb/disorders/{config['slug']}.yaml"
        content = pilot.git("show", revision + ":" + path)
        data = yaml.safe_load(content)
        record = {
            "path": path,
            "blob_sha256": pilot.sha(content),
            "data": {key: data[key] for key in pilot.FIELDS if key in data},
        }
        records = {path: record}
        coverage_catalog = {**catalog, path: record}
        candidates = list(pilot.grounded(coverage_catalog))
        series = "OMIMPS:" + config["ps"]
        members = sorted(
            {
                s
                for (s,) in omim.con.execute(
                    "select subject from statements where predicate='rdfs:subClassOf' and object=?",
                    (series,),
                )
                if s.startswith("OMIM:")
            }
        )
        coverage = {}
        curies = {series, *members, *config["subjects"]}
        curies.update(c["term"] for c in pilot.grounded(records))
        for member in members:
            matches = sorted(
                {
                    s
                    for (s,) in mondo.con.execute(
                        "select subject from statements where predicate='skos:exactMatch' and object=?",
                        (member,),
                    )
                    if s.startswith("MONDO:")
                }
            )
            coverage[member] = {
                "mondo_exact_matches": matches,
                "curated_candidates": [c for c in candidates if c["term"] in matches],
            }
            curies.update(matches)
        snapshot = {
            "commit": revision,
            "records": records,
            "coverage": coverage,
            "missing_paths": [],
        }
        projection = {
            "series": series,
            "root": path,
            "series_members": members,
            "context_terms": config["subjects"],
            "snapshots": {"before": deepcopy(snapshot), "after": deepcopy(snapshot)},
            "ontology": {},
        }
        for term in sorted(curies):
            source = mondo if term.startswith("MONDO:") else omim
            context = source.record(term)
            if term.startswith("MONDO:"):
                context["ancestors"] = sorted(
                    {
                        o
                        for (o,) in mondo.con.execute(
                            "select object from entailed_edge where subject=? and predicate='rdfs:subClassOf'",
                            (term,),
                        )
                        if o.startswith("MONDO:")
                    }
                )
                context["disjoint_with"] = mondo.objects(term, "owl:disjointWith")
            projection["ontology"][term] = context
        pilot.add_series_context(projection, mondo, omim)
        for context in list(projection["ontology"].values()):
            for target in context["exact_matches"]:
                if target.startswith(("OMIM:", "OMIMPS:")):
                    projection["ontology"].setdefault(target, omim.record(target))
        selected_mondo.update(
            t for t in projection["ontology"] if t.startswith("MONDO:")
        )
        projections[case] = projection
    mondo_records = source_records(source_dir / "mondo.obo", selected_mondo)
    do_terms = {t for config in CASES.values() for t in config["do_targets"]}
    do_terms.update({"DOID:0070366", "DOID:0060996"})
    do_records = source_records(source_dir / "doid.obo", do_terms)
    annotations = extract(
        source_dir / "mondo.obo", selected_mondo, manifest["mondo"]["url"]
    )
    pilot.write_json(
        out / "sources.json",
        {
            "sql": {k: v.provenance for k, v in sources.items()},
            "current_obo": manifest,
            "coverage_base": pilot.git("rev-parse", BASE).decode().strip(),
        },
    )
    pilot.write_json(
        out / "source-context.json",
        {"mondo": mondo_records, "doid": do_records, "annotations": annotations},
    )
    for case, projection in projections.items():
        config = CASES[case]
        projection["ontology"].update(deepcopy(do_records))
        for phase in ("before", "after"):
            assertions = []
            for subject in config["subjects"]:
                if phase == "before" and case in {"gorlin", "praas"}:
                    exact = set(projection["ontology"][subject]["exact_matches"])
                    provenance = "September 2026 MONDO semantic-sql skos:exactMatch"
                else:
                    exact = {
                        t
                        for t, m in annotations["terms"][subject]["mappings"].items()
                        if "MONDO:equivalentTo" in m["qualifiers"].get("source", [])
                    }
                    provenance = {
                        "source_url": manifest["mondo"]["url"],
                        "qualifier": "MONDO:equivalentTo",
                    }
                for target in sorted(exact & set(config["do_targets"])):
                    predicate = "skos:exactMatch"
                    source = provenance
                    if case == "tpmt" and phase == "after" and target == "DOID:0080172":
                        predicate = "skos:broadMatch"
                        source = {
                            "status": "PROPOSED_NOT_APPLIED_UPSTREAM",
                            "rationale": "DO parent includes TPMT and NUDT15 subtypes; MONDO subject is TPMT-specific",
                            "original": provenance,
                        }
                    assertions.append(
                        {
                            "subject": subject,
                            "target": target,
                            "predicate": predicate,
                            "source": source,
                        }
                    )
            projection["snapshots"][phase]["source_mappings"] = assertions
        pilot.write_json(out / case / "projection.json", projection)


def compile_case(case, projection, phase):
    kb, audit = pilot.compile_snapshot(projection, phase)
    if case == "foxe3" and phase == "before":
        # Reconstruct the former primary-grounding behavior: implicit equality
        # at .90, alongside the explicitly curated broad mapping at .95.
        subject, target = "dismech:FOXE3_Anterior_Segment_Dysgenesis", "MONDO:0019503"
        for pf in kb["pfacts"]:
            if pf["fact"] == {"fact_type": "SubClassOf", "sub": subject, "sup": target}:
                pf["prob"] = 0.95
        kb["pfacts"].insert(
            0,
            {
                "fact": {
                    "fact_type": "EquivalentTo",
                    "sub": subject,
                    "equivalent": target,
                },
                "prob": 0.9,
            },
        )
        audit["mapping_assertions"].insert(
            0,
            {
                "subject": subject,
                "target": target,
                "predicate": "skos:exactMatch",
                "source": "LEGACY_COMPILER_ASSUMPTION: implicit primary grounding; not a curated exact mapping",
            },
        )
        audit["intervention"] = (
            "LEGACY_COMPILER_ASSUMPTION: unqualified equality despite explicit broadMatch"
        )
    if case == "waldenstrom" and phase == "after":
        subject, target = "MONDO:0100280", "OMIMPS:153600"
        fact = {"fact_type": "EquivalentTo", "sub": subject, "equivalent": target}
        assert sum(pf["fact"] == fact for pf in kb["pfacts"]) == 1
        kb["pfacts"] = [pf for pf in kb["pfacts"] if pf["fact"] != fact]
        for assertion in audit["mapping_assertions"]:
            if assertion["subject"] == subject and assertion["target"] == target:
                assertion["predicate"] = "skos:relatedMatch"
                assertion["source"] = (
                    "SENSITIVITY_ONLY: weaken source PS identity; not an applied or adjudicated upstream correction"
                )
        audit["intervention"] = (
            "Source PS equivalence removed as a non-entailing related-match sensitivity analysis"
        )
    return kb, audit


def build(out):
    for case in CASES:
        projection = json.loads((out / case / "projection.json").read_text())
        for phase in ("before", "after"):
            kb, audit = compile_case(case, projection, phase)
            folder = out / case / phase
            folder.mkdir(parents=True, exist_ok=True)
            (folder / "kb.yaml").write_text(
                yaml.safe_dump(kb, sort_keys=False, allow_unicode=True)
            )
            pilot.write_json(folder / "audit.json", audit)
            print(case, phase, len(kb["pfacts"]), "hypotheses", flush=True)


def report(out):
    pilot.report(out)
    source = json.loads((out / "source-context.json").read_text())
    for case, config in CASES.items():
        projection = json.loads((out / case / "projection.json").read_text())
        lines = [
            "",
            "## Controlled intervention and distinct alternatives",
            "",
            "Curation is held fixed between these phases. See the [case interpretation](../README.md)",
            "for the source correction, compiler change, or sensitivity experiment being tested.",
            "A higher model score does not establish biological scope.",
            "",
        ]
        terms = config["subjects"] + config["do_targets"]
        if terms:
            lines += [
                "| Source entity | Canonical label | Relevant source parents |",
                "|---|---|---|",
            ]
            for term in terms:
                record = source["doid" if term.startswith("DOID:") else "mondo"][term]
                lines.append(
                    f"| {term} | {record['label']} | {', '.join(record['parents'])} |"
                )
        for phase in ("before", "after"):
            folder = out / case / phase
            enumerated = json.loads((folder / "enumeration.json").read_text())
            top = enumerated.get("top_solutions", [])
            lines += ["", f"### {phase}: best two distinct complete assignments", ""]
            if len(top) < 2:
                lines.append(
                    "Complete alternatives are unavailable; see the recorded enumeration status."
                )
                continue
            kb, _ = compile_case(case, projection, phase)
            lines += [
                f"Whole-assignment posteriors: A = {top[0]['posterior']}; B = {top[1]['posterior']}.",
                f"Best-versus-next-best confidence: {enumerated['confidence']}.",
                "Only hypotheses with different truth values are shown; every other choice is identical.",
                "",
                "| Hypothesis | Input prior | A | B | Mapping marginal |",
                "|---|---:|---|---|---:|",
            ]
            for i, pf in enumerate(kb["pfacts"]):
                a, b = top[0]["assignment"][i], top[1]["assignment"][i]
                if a == b:
                    continue
                fact = pf["fact"]
                target = fact.get("equivalent", fact.get("sup"))
                symbol = "≡" if fact["fact_type"] == "EquivalentTo" else "⊆"
                label = f"{kb['labels'][fact['sub']]} ({fact['sub']}) {symbol} {kb['labels'][target]} ({target})"
                lines.append(
                    f"| {label} | {pf['prob']} | {'accept' if a else 'reject'} | {'accept' if b else 'reject'} | {enumerated['marginals'][i]} |"
                )
        path = out / case / "README.md"
        path.write_text(path.read_text() + "\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "stage", choices=("capture", "build", "solve", "verify", "report")
    )
    parser.add_argument("--out", type=Path, default=OUT)
    parser.add_argument("--oak-dir", type=Path, default=Path.home() / ".data/oaklib")
    parser.add_argument("--source-dir", type=Path)
    parser.add_argument("--boomer-src", type=Path, default=os.environ.get("BOOMER_SRC"))
    parser.add_argument("--timeout", type=float, default=60)
    args = parser.parse_args()
    # Reuse only orchestration/reporting; frozen projections remain separate.
    pilot.CASES = CASES
    if args.stage == "capture":
        if not args.source_dir:
            parser.error(
                "capture requires --source-dir with pinned OBOs and manifest.json"
            )
        capture(args.out, args.oak_dir, args.source_dir)
    elif args.stage == "build":
        build(args.out)
    elif args.stage == "report":
        report(args.out)
    else:
        if not args.boomer_src or args.timeout <= 0:
            parser.error("solve/verify require --boomer-src and a positive timeout")
        if args.stage == "solve":
            pilot.solve_all(args.out, args.boomer_src, args.timeout)
        else:
            pilot.verify_all(args.out, args.boomer_src, args.timeout, max_hypotheses=18)


if __name__ == "__main__":
    main()
