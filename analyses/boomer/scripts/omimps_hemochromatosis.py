"""Scoped SLC40A1 mapping experiment within an audited hemochromatosis series.

Capture pins the whole-KB coverage and source snapshots. Other stages need only
committed projections; normal search and exhaustive checks have hard deadlines.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from copy import deepcopy
from pathlib import Path

import omimps_pilots as pilot
import proxy_merges
import yaml
from omimps_followup import source_records

OUT = pilot.REPO / "analyses/boomer/omimps-hemochromatosis"
BASE = "5cefcf9230687cbe99f64c18f886bb95724425ea"  # checked by capture
ROOT = "kb/disorders/Hemochromatosis.yaml"
SERIES = "OMIMPS:235200"
SUBJECTS = {"MONDO:0006507", "MONDO:0011631", "MONDO:0011012"}
DBS = {
    "MONDO": "mondo",
    "OMIM": "omim",
    "DOID": "doid",
    "ORDO": "ordo",
    "ICD10CM": "icd10cm",
    "icd11f": "icd11f",
}
VARIANTS = {
    "baseline": [],
    "ordo": ["ORDO"],
    "icd10cm": ["ICD10CM"],
    "icd11f": ["icd11f"],
    "all": ["ORDO", "ICD10CM", "icd11f"],
    "repair": ["ORDO", "ICD10CM", "icd11f"],
}
PRECISION = {
    "MONDO:equivalentTo": "skos:exactMatch",
    "MONDO:mondoIsNarrowerThanSource": "skos:broadMatch",
    "MONDO:mondoIsBroaderThanSource": "skos:narrowMatch",
}
MONDO_REV = "ece3a53ce89e1064c482c2d389fb3812492d9922"
MONDO_URL = f"https://raw.githubusercontent.com/monarch-initiative/mondo/{MONDO_REV}/src/ontology/mondo-edit.obo"


def capture(out, oak, obo, commit):
    if (
        pilot.sha(obo.read_bytes())
        != "a132530100e30d0ade1e17aade7d0aeb015e112bf988a2b11467d24f0ef14853"
    ):
        raise ValueError("MONDO input differs from the pinned source")
    sources = {ns: pilot.Source(oak / f"{name}.db") for ns, name in DBS.items()}
    expected = json.loads((OUT / "sources.json").read_text())["sql"]
    for namespace, source in sources.items():
        if source.provenance != expected[namespace]:
            raise ValueError(f"{namespace} database differs from the pinned snapshot")
    mondo, omim = sources["MONDO"], sources["OMIM"]
    catalog = pilot.catalog(commit)
    full_record = catalog[ROOT]
    terms = {c["term"] for c in pilot.grounded({ROOT: full_record})} | SUBJECTS
    # The general qualifier extractor otherwise excludes PS identifiers.
    original_external = proxy_merges.EXTERNAL.copy()
    try:
        proxy_merges.EXTERNAL.add("OMIMPS")
        annotations = proxy_merges.extract(obo, terms, MONDO_URL)
    finally:
        proxy_merges.EXTERNAL.clear()
        proxy_merges.EXTERNAL.update(original_external)
    current = source_records(obo, terms)
    members = sorted(
        s
        for (s,) in omim.con.execute(
            "select subject from statements where predicate='rdfs:subClassOf' and object=?",
            (SERIES,),
        )
        if s.startswith("OMIM:")
    )
    candidates = list(pilot.grounded(catalog))
    coverage, context = {}, {}
    for member in members:
        matches = sorted(
            s
            for (s,) in mondo.con.execute(
                "select subject from statements where predicate='skos:exactMatch' and object=?",
                (member,),
            )
            if s.startswith("MONDO:")
        )
        coverage[member] = {
            "mondo_exact_matches": matches,
            "curated_candidates": [c for c in candidates if c["term"] in matches],
        }
    targets = {SERIES, *members, *terms}
    for t in terms:
        targets.update(annotations["terms"][t]["mappings"])
    for term in sorted(targets):
        ns = term.split(":")[0]
        source = sources.get("OMIM" if ns == "OMIMPS" else ns)
        if source is None:
            continue
        record = source.record(term)
        record["definitions"] = [
            v
            for (v,) in source.con.execute(
                "select value from statements where subject=? and predicate in ('IAO:0000115','skos:definition')",
                (term,),
            )
            if v
        ]
        record["ancestors"] = sorted(
            {
                v
                for (v,) in source.con.execute(
                    "select object from entailed_edge where subject=? and predicate='rdfs:subClassOf'",
                    (term,),
                )
                if v.startswith(ns + ":")
            }
        )
        record["deprecated"] = any(
            str(o or v).lower() == "true"
            for o, v in source.con.execute(
                "select object,value from statements where subject=? and predicate='owl:deprecated'",
                (term,),
            )
        )
        record["disjoint_with"] = source.objects(term, "owl:disjointWith")
        if ns == "MONDO":
            # Current qualified OMIM mappings, older explicitly pinned hierarchy.
            record["exact_matches"] = [
                k
                for k, v in annotations["terms"][term]["mappings"].items()
                if k.startswith(("OMIM:", "OMIMPS:"))
                and "MONDO:equivalentTo" in v["qualifiers"].get("source", [])
            ]
        context[term] = record
    selected = deepcopy(full_record)
    selected["data"]["has_subtypes"] = [
        s
        for s in selected["data"]["has_subtypes"]
        if pilot.term_id(s.get("subtype_term")) == "MONDO:0011631"
    ]
    projection = {
        "series": SERIES,
        "root": ROOT,
        "series_members": members,
        "series_mondo_exact_matches": ["MONDO:0006507"],
        "context_terms": ["MONDO:0011012"],
        "ontology": context,
        "annotations": annotations,
        "current_mondo": current,
        "full_record": full_record,
        "coverage": coverage,
        "scope": "Family and SLC40A1 subtype groundings plus African iron overload ontology context; other PS members are structural context, not additional grounding hypotheses.",
        "snapshots": {
            "current": {
                "commit": commit,
                "records": {ROOT: selected},
                "coverage": coverage,
                "missing_paths": [],
            }
        },
    }
    pilot.write_json(out / "projection.json", projection)
    pilot.write_json(
        out / "sources.json",
        {
            "checked_at": "2026-11-27",
            "coverage_commit": commit,
            "sql": {ns: s.provenance for ns, s in sources.items()},
            "mondo_annotations": {
                "url": MONDO_URL,
                "revision": MONDO_REV,
                "sha256": pilot.sha(obo.read_bytes()),
            },
        },
    )


def build_variant(projection, variant):
    kb, audit = pilot.compile_snapshot(projection, "current")
    included = {"DOID", *VARIANTS[variant]}
    decisions = []
    selected = set()
    for subject in sorted(SUBJECTS):
        record = projection["annotations"]["terms"][subject]
        for target, annotation in sorted(record["mappings"].items()):
            if target.split(":")[0] not in included:
                continue
            external = projection["ontology"][target]
            qualifiers = set(annotation["qualifiers"].get("source", []))
            precisions = qualifiers & PRECISION.keys()
            decision = {"subject": subject, "target": target, "annotation": annotation}
            if (
                record["obsolete"]
                or external["deprecated"]
                or "MONDO:equivalentObsolete" in qualifiers
            ):
                decision["decision"] = "EXCLUDE_OBSOLETE"
            elif not external["label"]:
                decision["decision"] = "EXCLUDE_TARGET_NOT_RETRIEVED"
            elif len(precisions) != 1:
                decision["decision"] = (
                    "EXCLUDE_UNQUALIFIED"
                    if not precisions
                    else "REVIEW_CONFLICTING_PRECISION"
                )
            else:
                predicate = PRECISION[next(iter(precisions))]
                if (
                    variant == "repair"
                    and subject == "MONDO:0011631"
                    and target == "ORDO:648562"
                ):
                    predicate = "skos:relatedMatch"
                decision.update(
                    decision="INCLUDE_QUALIFIED"
                    if predicate != "skos:relatedMatch"
                    else "PROPOSED_RELATED_MAPPING_NOT_APPLIED",
                    predicate=predicate,
                )
                if predicate == "skos:relatedMatch":
                    decisions.append(decision)
                    continue
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
                if not any(p["fact"] == fact for p in kb["pfacts"]):
                    kb["pfacts"].append({"fact": fact, "prob": 0.95})
                selected.add(target)
            decisions.append(decision)
    # Keep the repair's vocabulary/constraints fixed; change only its mapping hypothesis.
    if variant == "repair":
        selected.add("ORDO:648562")
    for target in sorted(selected):
        record = projection["ontology"][target]
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
                kb["facts"].append(
                    {"fact_type": "SubClassOf", "sub": target, "sup": parent}
                )
        for other in sorted(selected & set(record["disjoint_with"])):
            kb["facts"].append(
                {"fact_type": "DisjointWith", "sub": target, "sibling": other}
            )
    proxies = proxy_merges.ProxyPolicy(projection["annotations"]).apply(kb)
    kb["labels"] = dict(sorted(kb["labels"].items()))
    kb["name"] = f"{SERIES} family/SLC40A1/African iron overload scope: {variant}"
    audit.update(
        external_mapping_decisions=decisions,
        proxy_decisions=proxies,
        model_subjects=sorted(SUBJECTS),
        scope=projection["scope"],
    )
    return kb, audit


def build(out):
    projection = json.loads((out / "projection.json").read_text())
    for variant in VARIANTS:
        kb, audit = build_variant(projection, variant)
        folder = out / variant
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "kb.yaml").write_text(
            yaml.safe_dump(kb, sort_keys=False, allow_unicode=True)
        )
        pilot.write_json(folder / "audit.json", audit)
        print(variant, len(kb["pfacts"]), flush=True)


def run(out, source, timeout, verify=False):
    source = source.resolve()
    rev = subprocess.check_output(
        ["git", "-C", str(source.parent), "rev-parse", "HEAD"], text=True
    ).strip()
    if subprocess.check_output(
        ["git", "-C", str(source.parent), "status", "--porcelain"], text=True
    ).strip():
        raise ValueError("Use a clean Boomer checkout")
    for variant in VARIANTS:
        folder = out / variant
        content = (folder / "kb.yaml").read_bytes()
        meta = {
            "input_sha256": pilot.sha(content),
            "boomer_commit": rev,
            "timeout_seconds": timeout,
        }
        if verify:
            result = json.loads((folder / "result.json").read_text())
            if (
                result["input_sha256"] != meta["input_sha256"]
                or result["boomer_commit"] != rev
            ):
                raise ValueError("Stale solve or different solver revision")
            if len(yaml.safe_load(content)["pfacts"]) > 18:
                raise ValueError("Exhaustive verification limited to 18 hypotheses")
            output = folder / "enumeration.json"
            command = [
                sys.executable,
                str(Path(pilot.__file__)),
                "verify-worker",
                "--input",
                str(folder),
                "--boomer-src",
                str(source),
            ]
        else:
            output = folder / "result.json"
            for name in (
                "result.json",
                "solution.yaml",
                "solution.md",
                "enumeration.json",
            ):
                (folder / name).unlink(missing_ok=True)
            command = [
                sys.executable,
                str(Path(pilot.__file__).with_name("solve_pending.py")),
                "--worker",
                str(folder / "kb.yaml"),
                "--workdir",
                str(folder),
                "--timeout",
                str(timeout),
                "--boomer-src",
                str(source),
            ]
        output.unlink(missing_ok=True)
        try:
            completed = subprocess.run(
                command,
                check=False,
                capture_output=True,
                text=True,
                timeout=timeout + 15,
                env={**os.environ, "PYTHONHASHSEED": "0"},
            )
            if completed.returncode:
                raise RuntimeError(completed.stderr[-4000:])
            result = json.loads(output.read_text())
        except subprocess.TimeoutExpired:
            result = {
                "status": "ENUMERATION_TIMED_OUT" if verify else "TIMED_OUT_NO_RESULT"
            }
        pilot.write_json(output, {**result, **meta})
        print(variant, result["status"], flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=["capture", "build", "solve", "verify"])
    parser.add_argument("--out", type=Path, default=OUT)
    parser.add_argument("--oak-dir", type=Path, default=Path.home() / ".data/oaklib")
    parser.add_argument("--mondo-obo", type=Path)
    parser.add_argument("--commit", default=BASE)
    parser.add_argument("--boomer-src", type=Path)
    parser.add_argument("--timeout", type=int, default=60)
    args = parser.parse_args()
    if args.stage == "capture":
        capture(args.out, args.oak_dir, args.mondo_obo, args.commit)
    elif args.stage == "build":
        build(args.out)
    else:
        run(args.out, args.boomer_src, args.timeout, args.stage == "verify")


if __name__ == "__main__":
    main()
