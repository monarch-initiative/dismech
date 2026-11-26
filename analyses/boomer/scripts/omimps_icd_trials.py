"""Add ORDO, ICD-10-CM and ICD-11 Foundation to three frozen PS models."""

from __future__ import annotations

import argparse
import json
import os
from copy import deepcopy
from pathlib import Path

import omimps_pilots as pilot
import yaml
from proxy_merges import ProxyPolicy

OUT = pilot.REPO / "analyses/boomer/omimps-icd-trials"
BASE = pilot.REPO / "analyses/boomer/omimps-followup"
BASE_COMMIT = "e7a0b07711b650b69d5983e04f07f29004c854ad"
CASES = {"gorlin": "after", "foxe3": "after", "waldenstrom": "before"}
DBS = {"ORDO": "ordo", "ICD10CM": "icd10cm", "icd11f": "icd11f"}
VARIANTS = {
    "baseline": [],
    "ordo": ["ORDO"],
    "icd10cm": ["ICD10CM"],
    "icd11f": ["icd11f"],
    "all": list(DBS),
}
PRECISION = {
    "MONDO:equivalentTo": "skos:exactMatch",
    "MONDO:mondoIsNarrowerThanSource": "skos:broadMatch",
    "MONDO:mondoIsBroaderThanSource": "skos:narrowMatch",
}


def pinned_bytes(path):
    content = path.read_bytes()
    relative = path.relative_to(pilot.REPO).as_posix()
    if content != pilot.git("show", BASE_COMMIT + ":" + relative):
        raise ValueError(f"Baseline source differs from pinned commit: {relative}")
    return content


def capture(out, oak):
    sources = {ns: pilot.Source(oak / (db + ".db")) for ns, db in DBS.items()}
    context_content = pinned_bytes(BASE / "source-context.json")
    context = json.loads(context_content)
    pilot.write_json(
        out / "sources.json",
        {
            "external_graphs": {ns: s.provenance for ns, s in sources.items()},
            "baseline_commit": BASE_COMMIT,
            "baseline_sources": json.loads(pinned_bytes(BASE / "sources.json")),
            "annotation_sha256": pilot.sha(context_content),
        },
    )
    for case, phase in CASES.items():
        path = BASE / case / phase / "kb.yaml"
        content = pinned_bytes(path)
        relative = path.relative_to(pilot.REPO).as_posix()
        kb = yaml.safe_load(content)
        subjects = sorted(t for t in kb["labels"] if t.startswith("MONDO:"))
        catalog = deepcopy(context["annotations"])
        catalog["terms"] = {t: catalog["terms"][t] for t in subjects}
        catalog["requested_terms"] = subjects
        records = {}
        for subject in subjects:
            for target in catalog["terms"][subject]["mappings"]:
                prefix = target.split(":")[0]
                if prefix not in sources or target in records:
                    continue
                s = sources[prefix]
                record = s.record(target)
                record["deprecated"] = any(
                    str(o or v).lower() == "true"
                    for o, v in s.con.execute(
                        "select object,value from statements where subject=? and predicate='owl:deprecated'",
                        (target,),
                    )
                )
                record["definitions"] = sorted(
                    {
                        v
                        for (v,) in s.con.execute(
                            "select value from statements where subject=? and predicate in ('IAO:0000115','skos:definition')",
                            (target,),
                        )
                        if v
                    }
                )
                record["ancestors"] = sorted(
                    {
                        o
                        for (o,) in s.con.execute(
                            "select object from entailed_edge where subject=? and predicate='rdfs:subClassOf'",
                            (target,),
                        )
                        if o.startswith(prefix + ":")
                    }
                )
                record["disjoint_with"] = s.objects(target, "owl:disjointWith")
                records[target] = record
        # Definitions of sibling categories give positive scope context for the
        # known ICD-11 parent/child pair, rather than relying on absent paths.
        s = sources["icd11f"]
        siblings = {}
        if case == "foxe3":
            for (term,) in s.con.execute(
                "select subject from statements where predicate='rdfs:subClassOf' and object='icd11f:943599144'"
            ):
                siblings[term] = s.record(term)
        pilot.write_json(
            out / case / "projection.json",
            {
                "baseline": {
                    "commit": BASE_COMMIT,
                    "path": relative,
                    "input_sha256": pilot.sha(content),
                    "text": content.decode(),
                    "kb": kb,
                },
                "catalog": catalog,
                "external": records,
                "icd11_parent_children": siblings,
                "mondo": {t: context["mondo"][t] for t in subjects},
            },
        )


def build_variant(projection, variant):
    baseline = projection["baseline"]
    if pilot.sha(baseline["text"].encode()) != baseline["input_sha256"]:
        raise ValueError("Baseline text does not match its recorded hash")
    kb = yaml.safe_load(baseline["text"])
    if kb != baseline["kb"]:
        raise ValueError("Baseline text and parsed projection disagree")
    included = VARIANTS["all"] if variant == "repair" else VARIANTS[variant]
    decisions, mappings, edges = [], [], []
    selected = set()
    for subject, term in sorted(projection["catalog"]["terms"].items()):
        for target, annotation in sorted(term["mappings"].items()):
            if target.split(":")[0] not in included:
                continue
            record = projection["external"][target]
            qualifiers = set(annotation["qualifiers"].get("source", []))
            precisions = qualifiers & PRECISION.keys()
            row = {"subject": subject, "target": target, "annotation": annotation}
            if term["obsolete"]:
                row["decision"] = "EXCLUDE_OBSOLETE_MONDO"
            elif "MONDO:equivalentObsolete" in qualifiers or record["deprecated"]:
                row["decision"] = "EXCLUDE_OBSOLETE_TARGET"
            elif not record["label"]:
                row["decision"] = "EXCLUDE_TARGET_NOT_RETRIEVED"
            elif len(precisions) != 1:
                row["decision"] = (
                    "EXCLUDE_UNQUALIFIED"
                    if not precisions
                    else "REVIEW_CONFLICTING_PRECISION"
                )
            else:
                predicate = PRECISION[next(iter(precisions))]
                row.update(decision="INCLUDE_QUALIFIED", predicate=predicate)
                if (
                    variant == "repair"
                    and subject == "MONDO:0019503"
                    and target == "icd11f:943599144"
                ):
                    predicate = "skos:broadMatch"
                    row.update(
                        predicate=predicate,
                        decision="PROPOSED_SCOPE_REPAIR_NOT_APPLIED_UPSTREAM",
                    )
                if predicate == "skos:exactMatch":
                    fact = {
                        "fact_type": "EquivalentTo",
                        "sub": subject,
                        "equivalent": target,
                    }
                elif predicate == "skos:broadMatch":
                    fact = {"fact_type": "SubClassOf", "sub": subject, "sup": target}
                else:
                    fact = {"fact_type": "SubClassOf", "sub": target, "sup": subject}
                pf = {"fact": fact, "prob": 0.95}
                if not any(p["fact"] == fact for p in kb["pfacts"]):
                    kb["pfacts"].append(pf)
                mappings.append(pf)
                selected.add(target)
            decisions.append(row)
    for target in sorted(selected):
        record = projection["external"][target]
        kb["labels"][target] = record["label"]
        kb["facts"].append(
            {
                "fact_type": "MemberOfDisjointGroup",
                "sub": target,
                "group": target.split(":")[0],
            }
        )
        for parent in sorted(selected & set(record["ancestors"])):
            if target != parent:
                edges.append({"fact_type": "SubClassOf", "sub": target, "sup": parent})
        for other in sorted(selected & set(record["disjoint_with"])):
            edges.append({"fact_type": "DisjointWith", "sub": target, "sibling": other})
    for fact in edges:
        if fact not in kb["facts"]:
            kb["facts"].append(fact)
    # Existing policy permits only explicitly annotated preferred proxy pairs.
    # There are no permitted pairs in these trials; audit decisions are retained.
    proxy = ProxyPolicy(projection["catalog"]).apply(kb) if selected else []
    return kb, {
        "variant": variant,
        "included_vocabularies": included,
        "mapping_decisions": decisions,
        "added_mappings": mappings,
        "external_edges": edges,
        "proxy_decisions": proxy,
        "baseline_sha256": projection["baseline"]["input_sha256"],
    }


def experiments():
    for case in CASES:
        for variant in VARIANTS:
            yield case, variant
    yield "foxe3", "repair"


def build(out):
    for case, variant in experiments():
        p = json.loads((out / case / "projection.json").read_text())
        kb, audit = build_variant(p, variant)
        folder = out / case / variant
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "kb.yaml").write_text(
            yaml.safe_dump(kb, sort_keys=False, allow_unicode=True)
        )
        pilot.write_json(folder / "audit.json", audit)
        print(case, variant, len(kb["pfacts"]), flush=True)


def report(out):
    for case in CASES:
        p = json.loads((out / case / "projection.json").read_text())
        lines = [
            f"# {case}: ORDO and ICD source additions",
            "",
            "The curated disease scope and baseline constraints are held fixed across variants.",
            "Absent or unqualified mappings are recorded explicitly, not promoted to equivalence.",
            "",
            "## Source entities",
            "",
            "| Entity | Canonical label | Definition |",
            "|---|---|---|",
        ]
        for term, record in sorted(p["external"].items()):
            definitions = (
                " ".join(record["definitions"]).replace("|", "\\|") or "Not retrieved"
            )
            lines.append(
                f"| {term} | {record['label'] or 'Not retrieved'} | {definitions} |"
            )
        lines += [
            "",
            "## Results",
            "",
            "| Variant | Hypotheses | Normal search | Enumeration | Confidence | Best whole-assignment posterior |",
            "|---|---:|---|---|---:|---:|",
        ]
        variants = list(VARIANTS) + (["repair"] if case == "foxe3" else [])
        for variant in variants:
            folder = out / case / variant
            result = json.loads((folder / "result.json").read_text())
            enum = json.loads((folder / "enumeration.json").read_text())
            lines.append(
                f"| [{variant}]({variant}/audit.json) | {result.get('n_pfacts', 'NA')} | {result['status']} | [{enum['status']}]({variant}/enumeration.json) | {enum.get('confidence', 'NA')} | {enum.get('best_posterior', 'NA')} |"
            )
        lines += [
            "",
            "Confidence compares the two best distinct complete assignments; it is not a",
            "mapping marginal or a clinical accuracy score. Compare decisions, not the",
            "whole-assignment posteriors of models with different numbers of hypotheses.",
            "",
        ]
        for variant in variants:
            folder = out / case / variant
            enum = json.loads((folder / "enumeration.json").read_text())
            top = enum.get("top_solutions", [])
            if len(top) < 2:
                continue
            kb, audit = build_variant(p, variant)
            lines += [
                f"## {variant}: differing choices in the best two assignments",
                "",
                f"Whole-assignment posteriors: A = {top[0]['posterior']}; B = {top[1]['posterior']}.",
                "",
                "| Hypothesis | Prior | A | B | Marginal |",
                "|---|---:|---|---|---:|",
            ]
            for i, pf in enumerate(kb["pfacts"]):
                a, b = top[0]["assignment"][i], top[1]["assignment"][i]
                if a == b:
                    continue
                f = pf["fact"]
                target = f.get("equivalent", f.get("sup"))
                symbol = "≡" if f["fact_type"] == "EquivalentTo" else "⊆"
                lines.append(
                    f"| {kb['labels'][f['sub']]} ({f['sub']}) {symbol} {kb['labels'][target]} ({target}) | {pf['prob']} | {'accept' if a else 'reject'} | {'accept' if b else 'reject'} | {enum['marginals'][i]} |"
                )
            excluded = [
                r
                for r in audit["mapping_decisions"]
                if r["decision"].startswith(("EXCLUDE", "REVIEW"))
            ]
            if excluded:
                lines += ["", "Mappings not imported:", ""]
                lines += [
                    f"- {r['subject']} → {r['target']}: {r['decision']}"
                    for r in excluded
                ]
            lines += [""]
        (out / case / "README.md").write_text("\n".join(lines))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "stage", choices=["capture", "build", "solve", "verify", "report"]
    )
    parser.add_argument("--out", type=Path, default=OUT)
    parser.add_argument("--oak-dir", type=Path, default=Path.home() / ".data/oaklib")
    parser.add_argument("--boomer-src", type=Path, default=os.environ.get("BOOMER_SRC"))
    parser.add_argument("--timeout", type=float, default=60)
    args = parser.parse_args()
    if args.stage == "capture":
        capture(args.out, args.oak_dir)
    elif args.stage == "build":
        build(args.out)
    elif args.stage == "report":
        report(args.out)
    else:
        if not args.boomer_src or args.timeout <= 0:
            parser.error("A clean Boomer source and positive timeout are required")
        pilot.CASES = CASES
        if args.stage == "solve":
            pilot.solve_all(args.out, args.boomer_src, args.timeout, phases=VARIANTS)
        else:
            pilot.verify_all(
                args.out,
                args.boomer_src,
                args.timeout,
                max_hypotheses=18,
                phases=VARIANTS,
            )
        pilot.CASES = {"foxe3": None}
        if args.stage == "solve":
            pilot.solve_all(args.out, args.boomer_src, args.timeout, phases=["repair"])
        else:
            pilot.verify_all(
                args.out,
                args.boomer_src,
                args.timeout,
                max_hypotheses=18,
                phases=["repair"],
            )


if __name__ == "__main__":
    main()
