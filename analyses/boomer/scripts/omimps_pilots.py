"""Capture and solve five pinned OMIMPS pilots without changing saved analyses.

Capture requires the source git objects and local semantic-sql snapshots. Build
and solve use only the committed projections. Run --help for the stages.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import sqlite3
import subprocess
import sys
import tarfile
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[3]
OUT = REPO / "analyses/boomer/omimps-pilots"
CASES = {
    "bbs": ("209900", "70f732e3bfe", "kb/disorders/Bardet-Biedl_Syndrome.yaml"),
    "lal": (
        "278000",
        "790baff20fa863084cce942f1cc9f899b1936bdc",
        "kb/groupings/Lysosomal_Acid_Lipase_Deficiency_Spectrum.yaml",
    ),
    "cbl": (
        "236270",
        "bf2c4a6a5efdb3a4eff0e377186fdcab53ba2c2a",
        "kb/groupings/Homocystinuria-Megaloblastic_Anemia_Disorders.yaml",
    ),
    "msud": (
        "248600",
        "12e38bd36f3eae59d4a7c42ab640ee1e9b81d5b5",
        "kb/disorders/Maple_Syrup_Urine_Disease.yaml",
    ),
    "pnh": (
        "300818",
        "e98ca0e393a21f8d9c6228da25edc73a5bfdd197",
        "kb/disorders/Paroxysmal_Nocturnal_Hemoglobinuria.yaml",
    ),
}
FIELDS = (
    "name",
    "category",
    "disease_term",
    "mappings",
    "has_subtypes",
    "members",
    "grouping_basis",
    "grouping_rationale",
    "membership_criteria",
)


def sha(content):
    return hashlib.sha256(content).hexdigest()


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")


def git(*args):
    return subprocess.check_output(["git", *args], cwd=REPO)


def term_id(descriptor):
    return ((descriptor or {}).get("term") or descriptor or {}).get("id")


def catalog(commit):
    """Read tracked KB blobs, never the user's working files or term caches."""
    archive = git("archive", commit, "kb/disorders", "kb/groupings")
    records = {}
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        for item in tar:
            if not item.isfile() or not item.name.endswith(".yaml"):
                continue
            content = tar.extractfile(item).read()
            data = yaml.load(content, Loader=yaml.CSafeLoader)
            if isinstance(data, dict) and data.get("name"):
                records[item.name] = {
                    "path": item.name,
                    "blob_sha256": sha(content),
                    "data": {k: data[k] for k in FIELDS if k in data},
                }
    return records


def dependencies(records, root):
    by_name = {r["data"]["name"]: p for p, r in records.items()}
    selected = set()

    def visit(path):
        if path in selected:
            return
        selected.add(path)
        data = records[path]["data"]
        for member in data.get("members", []):
            visit(by_name[member["member"]])
        for subtype in data.get("has_subtypes", []):
            if subtype.get("curated_in"):
                visit("kb/disorders/" + subtype["curated_in"] + ".yaml")

    visit(root)
    return sorted(selected)


class Source:
    def __init__(self, path):
        if not path.is_file():
            raise FileNotFoundError(path)
        self.con = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
        with path.open("rb") as stream:
            digest = hashlib.file_digest(stream, "sha256").hexdigest()
        self.provenance = {
            "filename": path.name,
            "sha256": digest,
            "versions": sorted(
                {
                    o or v
                    for o, v in self.con.execute(
                        "select object,value from statements where predicate='owl:versionIRI'"
                    )
                    if o or v
                }
            ),
        }

    def objects(self, subject, predicate):
        return sorted(
            {
                o
                for (o,) in self.con.execute(
                    "select object from statements where subject=? and predicate=?",
                    (subject, predicate),
                )
                if o
            }
        )

    def record(self, curie):
        rows = self.con.execute(
            "select value from statements where subject=? and predicate='rdfs:label'",
            (curie,),
        ).fetchall()
        return {
            "label": rows[0][0] if rows else None,
            "parents": self.objects(curie, "rdfs:subClassOf"),
            "exact_matches": self.objects(curie, "skos:exactMatch"),
        }


def grounded(records):
    for path, record in sorted(records.items()):
        data = record["data"]
        for name, desc in [(data["name"], data.get("disease_term"))] + [
            (s["name"], s.get("subtype_term")) for s in data.get("has_subtypes", [])
        ]:
            if term_id(desc):
                yield {
                    "path": path,
                    "name": name,
                    "term": term_id(desc),
                    "blob_sha256": record["blob_sha256"],
                }


def capture(out, oak):
    sources = {name: Source(oak / (name + ".db")) for name in ("mondo", "omim")}
    mondo, omim = sources["mondo"], sources["omim"]
    write_json(out / "sources.json", {k: s.provenance for k, s in sources.items()})
    for slug, (number, revision, root) in CASES.items():
        after = git("rev-parse", revision).decode().strip()
        before = (
            git("rev-parse", after + "^" if slug == "bbs" else "bef670f1707")
            .decode()
            .strip()
        )
        # Pin the shared pre-curation base, including multi-commit review fixes.
        catalogs = {"before": catalog(before), "after": catalog(after)}
        paths = dependencies(catalogs["after"], root)
        series = "OMIMPS:" + number
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
        projection = {"series": series, "root": root, "snapshots": {}}
        curies = {series, *members}
        for phase, commit in (("before", before), ("after", after)):
            records = {p: catalogs[phase][p] for p in paths if p in catalogs[phase]}
            candidates = list(grounded(catalogs[phase]))
            coverage = {}
            for member in members:
                matches = {
                    s
                    for (s,) in mondo.con.execute(
                        "select subject from statements where predicate='skos:exactMatch' and object=?",
                        (member,),
                    )
                    if s.startswith("MONDO:")
                }
                coverage[member] = {
                    "mondo_exact_matches": sorted(matches),
                    "curated_candidates": [
                        c for c in candidates if c["term"] in matches
                    ],
                }
                curies.update(matches)
            projection["snapshots"][phase] = {
                "commit": commit,
                "records": records,
                "coverage": coverage,
                "missing_paths": sorted(set(paths) - records.keys()),
            }
            curies.update(c["term"] for c in grounded(records))
            for record in records.values():
                for m in record["data"].get("members", []):
                    if term_id(m.get("disease_term")):
                        curies.add(term_id(m["disease_term"]))
        context = {}
        for curie in sorted(curies):
            source = mondo if curie.startswith("MONDO:") else omim
            context[curie] = source.record(curie)
            if curie.startswith("MONDO:"):
                context[curie]["disjoint_with"] = source.objects(
                    curie, "owl:disjointWith"
                )
                context[curie]["ancestors"] = sorted(
                    {
                        o
                        for (o,) in mondo.con.execute(
                            "select object from entailed_edge where subject=? and predicate='rdfs:subClassOf'",
                            (curie,),
                        )
                        if o.startswith("MONDO:")
                    }
                )
        # Labels for external mapping targets also belong to the frozen context.
        for record in list(context.values()):
            for target in record["exact_matches"]:
                if target.startswith(("OMIM:", "OMIMPS:")) and target not in context:
                    context[target] = omim.record(target)
        projection["ontology"] = context
        projection["series_members"] = members
        add_series_context(projection, mondo, omim)
        write_json(out / slug / "projection.json", projection)


def add_series_context(projection, mondo, omim):
    """Include MONDO's family-level opinion even for a new ungrounded grouping."""
    matches = sorted(
        {
            s
            for (s,) in mondo.con.execute(
                "select subject from statements where predicate='skos:exactMatch' and object=?",
                (projection["series"],),
            )
            if s.startswith("MONDO:")
        }
    )
    projection["series_mondo_exact_matches"] = matches
    targets = set(matches)
    for snapshot in projection["snapshots"].values():
        for record in snapshot["records"].values():
            data = record["data"]
            for entry in [data, *data.get("has_subtypes", [])]:
                for mapping in (entry.get("mappings") or {}).get("mondo_mappings", []):
                    targets.add(term_id(mapping))
    for term in sorted(targets):
        record = mondo.record(term)
        record["ancestors"] = sorted(
            {
                o
                for (o,) in mondo.con.execute(
                    "select object from entailed_edge where subject=? and predicate='rdfs:subClassOf'",
                    (term,),
                )
                if o.startswith("MONDO:")
            }
        )
        record["disjoint_with"] = mondo.objects(term, "owl:disjointWith")
        projection["ontology"][term] = record
        for target in record["exact_matches"]:
            if target.startswith(("OMIM:", "OMIMPS:")):
                projection["ontology"][target] = omim.record(target)


def scoped_member_mappings(projection, phase, member):
    """Retain broader/narrower curated scope without counting it as equivalence."""
    snapshot = projection["snapshots"][phase]
    matches = snapshot["coverage"][member]["mondo_exact_matches"]
    candidates = []
    for path, record in snapshot["records"].items():
        data = record["data"]
        for entry in [data, *data.get("has_subtypes", [])]:
            for mapping in (entry.get("mappings") or {}).get("mondo_mappings", []):
                if term_id(mapping) in matches:
                    candidates.append(
                        {
                            "name": entry["name"],
                            "path": path,
                            "predicate": mapping.get(
                                "mapping_predicate", "UNSPECIFIED"
                            ),
                            "term": term_id(mapping),
                        }
                    )
    return candidates


def compile_snapshot(projection, phase):
    """Compile logical mappings; weak SKOS mappings remain non-entailing metadata."""
    snapshot = projection["snapshots"][phase]
    records, context = snapshot["records"], projection["ontology"]
    nodes, aliases, edges, annotations, hypotheses = {}, {}, [], [], []
    by_name = {r["data"]["name"]: p for p, r in records.items()}

    def node_id(path):
        return "dismech:" + Path(path).stem

    def add_node(node, name, term=None):
        if node in nodes and nodes[node]["term"] != term:
            raise ValueError(f"Incompatible alias grounding: {node}")
        nodes[node] = {"name": name, "term": term}

    for path, record in records.items():
        data = record["data"]
        add_node(node_id(path), data["name"], term_id(data.get("disease_term")))
    for path, record in records.items():
        for subtype in record["data"].get("has_subtypes", []):
            if not term_id(subtype.get("subtype_term")):
                continue
            node = node_id(path) + "#" + subtype["name"]
            target = subtype.get("curated_in")
            if target:
                canonical = node_id("kb/disorders/" + target + ".yaml")
                if nodes[canonical]["term"] != term_id(subtype["subtype_term"]):
                    raise ValueError(f"Alias term mismatch: {node}")
                aliases[node] = canonical
            else:
                canonical = node
                add_node(node, subtype["name"], term_id(subtype["subtype_term"]))
            edges.append(
                (canonical, node_id(path), "ProperSubClassOf", "curated subtype")
            )
    for path, record in records.items():
        for member in record["data"].get("members", []):
            member_path = by_name[member["member"]]
            child = node_id(member_path)
            if member.get("member_type") == "SUBTYPE":
                term = term_id(member.get("disease_term"))
                candidates = [
                    n
                    for n, d in nodes.items()
                    if n.startswith(child + "#") and d["term"] == term
                ]
                candidates += [
                    canonical
                    for alias, canonical in aliases.items()
                    if alias.startswith(child + "#")
                    and nodes[canonical]["term"] == term
                ]
                if len(set(candidates)) != 1:
                    raise ValueError(f"Unresolved subtype member: {member}")
                child = candidates[0]
            edges.append(
                (child, node_id(path), "SubClassOf", "curated grouping member")
            )

    def mapping(subject, target, predicate, source, prior=0.95):
        annotation = {
            "subject": subject,
            "target": target,
            "predicate": predicate,
            "source": source,
        }
        annotations.append(annotation)
        if predicate == "skos:exactMatch":
            fact = {"fact_type": "EquivalentTo", "sub": subject, "equivalent": target}
        elif predicate == "skos:broadMatch":
            fact = {"fact_type": "SubClassOf", "sub": subject, "sup": target}
        elif predicate == "skos:narrowMatch":
            fact = {"fact_type": "SubClassOf", "sub": target, "sup": subject}
        else:
            return
        # Repeated source assertions are provenance, not independent evidence.
        if not any(p["fact"] == fact for p in hypotheses):
            hypotheses.append({"fact": fact, "prob": prior})

    for node, data in nodes.items():
        if data["term"]:
            mapping(
                node,
                data["term"],
                "skos:exactMatch",
                "primary/subtype grounding assumption",
                0.9,
            )
    for path, record in records.items():
        for field in ("mondo_mappings", "omimps_mappings", "omim_mappings"):
            for m in (record["data"].get("mappings") or {}).get(field, []):
                mapping(
                    node_id(path),
                    term_id(m),
                    m.get("mapping_predicate", "UNSPECIFIED"),
                    {"path": path, "field": field, "mapping": m},
                )
        for subtype in record["data"].get("has_subtypes", []):
            node = node_id(path) + "#" + subtype["name"]
            node = aliases.get(node, node)
            if node not in nodes:
                continue
            for field in ("mondo_mappings", "omimps_mappings", "omim_mappings"):
                for m in (subtype.get("mappings") or {}).get(field, []):
                    mapping(
                        node,
                        term_id(m),
                        m.get("mapping_predicate", "UNSPECIFIED"),
                        {
                            "path": path,
                            "subtype": subtype["name"],
                            "field": field,
                            "mapping": m,
                        },
                    )
    terms = {d["term"] for d in nodes.values() if d["term"]}
    terms.update(projection["series_mondo_exact_matches"])
    terms.update(a["target"] for a in annotations)
    for term in sorted(terms.copy()):
        if term.startswith("MONDO:"):
            for target in context[term]["exact_matches"]:
                if target.startswith(("OMIM:", "OMIMPS:")):
                    mapping(
                        term,
                        target,
                        "skos:exactMatch",
                        "MONDO snapshot skos:exactMatch",
                    )
                    terms.add(target)
    terms.update(projection["series_members"])
    terms.add(projection["series"])
    facts = []
    provenance = []

    def edge(child, parent, kind, source):
        fact = {"fact_type": kind, "sub": child, "sup": parent}
        if fact not in facts:
            facts.append(fact)
            provenance.append({"fact": fact, "source": source})

    for child, parent, kind, source in edges:
        edge(child, parent, kind, source)
    for child in sorted(terms):
        for parent in sorted(terms):
            if child != parent and parent in context.get(child, {}).get(
                "ancestors", []
            ):
                edge(child, parent, "SubClassOf", "MONDO entailed hierarchy")
        for parent in context.get(child, {}).get("parents", []):
            if parent in terms:
                edge(child, parent, "SubClassOf", "snapshot asserted hierarchy")
    # Namespace assumptions are non-equivalence, not biological disjointness.
    for term in sorted(terms):
        namespace = term.split(":")[0]
        if namespace in {"MONDO", "OMIM", "OMIMPS"}:
            facts.append(
                {"fact_type": "MemberOfDisjointGroup", "sub": term, "group": namespace}
            )
    for child in sorted(terms):
        for target in context.get(child, {}).get("disjoint_with", []):
            if target in terms:
                facts.append(
                    {"fact_type": "DisjointWith", "sub": child, "sibling": target}
                )
    labels = {n: d["name"] for n, d in nodes.items()}
    labels.update({t: context.get(t, {}).get("label") or t for t in terms})
    kb = {
        "name": projection["series"] + " " + phase,
        "facts": facts,
        "pfacts": hypotheses,
        "labels": labels,
    }
    audit = {
        "nodes": nodes,
        "aliases": aliases,
        "mapping_assertions": annotations,
        "edge_provenance": provenance,
    }
    return kb, audit


def build(out):
    for slug in CASES:
        projection = json.loads((out / slug / "projection.json").read_text())
        for phase in ("before", "after"):
            kb, audit = compile_snapshot(projection, phase)
            folder = out / slug / phase
            folder.mkdir(parents=True, exist_ok=True)
            (folder / "kb.yaml").write_text(
                yaml.safe_dump(kb, sort_keys=False, allow_unicode=True)
            )
            write_json(folder / "audit.json", audit)
            print(slug, phase, len(kb["pfacts"]), "hypotheses", flush=True)


def solve_all(out, source, timeout):
    source = source.resolve()
    commit = subprocess.check_output(
        ["git", "-C", str(source.parent), "rev-parse", "HEAD"], text=True
    ).strip()
    if subprocess.check_output(
        ["git", "-C", str(source.parent), "status", "--porcelain"], text=True
    ).strip():
        raise ValueError("Use a clean Boomer checkout")
    worker = Path(__file__).with_name("solve_pending.py")
    for slug in CASES:
        for phase in ("before", "after"):
            folder = out / slug / phase
            content = (folder / "kb.yaml").read_bytes()
            # Never leave a previous successful result beside a failed attempt.
            for filename in ("result.json", "solution.yaml", "solution.md"):
                (folder / filename).unlink(missing_ok=True)
            metadata = {
                "input_sha256": sha(content),
                "boomer_commit": commit,
                "hash_seed": 0,
                "timeout_seconds": timeout,
            }
            try:
                run = subprocess.run(
                    [
                        sys.executable,
                        str(worker),
                        "--worker",
                        str(folder / "kb.yaml"),
                        "--workdir",
                        str(folder),
                        "--timeout",
                        str(timeout),
                        "--boomer-src",
                        str(source),
                    ],
                    check=False,
                    capture_output=True,
                    text=True,
                    timeout=timeout + 15,
                    env={**os.environ, "PYTHONHASHSEED": "0"},
                )
                if run.returncode:
                    metadata.update(
                        status="ERROR", error=(run.stderr or run.stdout)[-4000:]
                    )
                else:
                    metadata.update(json.loads((folder / "result.json").read_text()))
            except subprocess.TimeoutExpired:
                metadata.update(status="TIMED_OUT_NO_RESULT")
            write_json(folder / "result.json", metadata)
            print(slug, phase, metadata["status"], flush=True)


def verify_worker(folder, source):
    sys.path.insert(0, str(source.resolve()))
    from boomer import model, search
    from investigate_ties import enumerate_worlds

    kb = model.KB.model_validate(yaml.safe_load((folder / "kb.yaml").read_text()))
    result = enumerate_worlds(
        kb, model, search.get_reasoner(model.SearchConfig().reasoner_class)
    )
    metadata = json.loads((folder / "result.json").read_text())
    if metadata["status"] not in {"ALL_MAPPINGS_CONSISTENT", "RETRACTED"}:
        result.update(
            status="EXHAUSTIVELY_ENUMERATED",
            input_sha256=sha((folder / "kb.yaml").read_bytes()),
            assignment_order="kb.yaml pfacts order",
            solver_comparison="NOT_COMPLETED_SEARCH",
        )
        write_json(folder / "enumeration.json", result)
        return
    saved = yaml.safe_load((folder / "solution.yaml").read_text())
    selected = {
        json.dumps(p["pfact"]["fact"], sort_keys=True): p["truth_value"]
        for p in saved["solved_pfacts"]
    }
    values = [
        selected[json.dumps(p.fact.model_dump(), sort_keys=True)] for p in kb.pfacts
    ]
    assert values in result["optimal_assignments"]
    assert result["distinct_solutions"] == saved["number_of_satisfiable_combinations"]
    from math import isclose

    assert isclose(result["confidence"], saved["confidence"], abs_tol=1e-10)
    assert isclose(result["best_posterior"], saved["posterior_prob"], abs_tol=1e-10)
    marginals = {
        json.dumps(p["pfact"]["fact"], sort_keys=True): p["posterior_prob"]
        for p in saved["solved_pfacts"]
    }
    for p, expected in zip(kb.pfacts, result["marginals"], strict=True):
        assert isclose(
            marginals[json.dumps(p.fact.model_dump(), sort_keys=True)],
            expected,
            abs_tol=1e-10,
        )
    result.update(
        status="VERIFIED",
        input_sha256=sha((folder / "kb.yaml").read_bytes()),
        assignment_order="kb.yaml pfacts order",
    )
    write_json(folder / "enumeration.json", result)


def certify_assignment(kb, reasoner):
    """Certify the two highest-weight worlds without computing the partition sum.

    If all priors exceed 1/2, all-true maximizes the unconstrained weight.
    Every different world loses at least min(p)/(1-min(p)) in weight. A
    satisfiable single flip at that minimum attains the bound exactly.
    This proves the optimum and runner-up, but says nothing about marginals.
    """
    from math import prod

    if not kb.pfacts or any(p.prob <= 0.5 or p.prob >= 1 for p in kb.pfacts):
        return {"status": "NOT_APPLICABLE"}
    values = [True] * len(kb.pfacts)
    if not reasoner.reason(kb, list(enumerate(values))).satisfiable:
        return {"status": "ALL_TRUE_INCONSISTENT"}
    minimum = min(p.prob for p in kb.pfacts)
    best = prod(p.prob for p in kb.pfacts)
    for index, p in enumerate(kb.pfacts):
        if p.prob != minimum:
            continue
        alternative = values.copy()
        alternative[index] = False
        if reasoner.reason(kb, list(enumerate(alternative))).satisfiable:
            second = best * (1 - minimum) / minimum
            return {
                "status": "CERTIFIED",
                "minimum_prior": minimum,
                "best_assignment": values,
                "second_assignment": alternative,
                "best_prior_weight": best,
                "second_prior_weight": second,
                "different_index": index,
                "confidence": best / (best + second),
                "mapping_marginals": "NOT_COMPUTED",
                "whole_solution_posterior": "NOT_COMPUTED",
            }
    return {"status": "ALL_TRUE_SATISFIABLE_SECOND_NOT_CERTIFIED"}


def certify_worker(folder, source):
    sys.path.insert(0, str(source.resolve()))
    from boomer import model, search

    content = (folder / "kb.yaml").read_bytes()
    kb = model.KB.model_validate(yaml.safe_load(content))
    result = certify_assignment(
        kb, search.get_reasoner(model.SearchConfig().reasoner_class)
    )
    result.update(
        input_sha256=sha(content),
        assignment_order="kb.yaml pfacts order",
        method="Certify only if all priors exceed 1/2 and all-true plus a minimum-prior single-flip world are satisfiable.",
    )
    write_json(folder / "certificate.json", result)


def verify_all(out, source, timeout):
    source = source.resolve()
    commit = subprocess.check_output(
        ["git", "-C", str(source.parent), "rev-parse", "HEAD"], text=True
    ).strip()
    if subprocess.check_output(
        ["git", "-C", str(source.parent), "status", "--porcelain"], text=True
    ).strip():
        raise ValueError("Use a clean Boomer checkout")
    for slug in CASES:
        for phase in ("before", "after"):
            folder = out / slug / phase
            kb = yaml.safe_load((folder / "kb.yaml").read_text())
            result = json.loads((folder / "result.json").read_text())
            if result["boomer_commit"] != commit:
                raise ValueError("Verification must use the recorded solver revision")
            path = folder / "enumeration.json"
            path.unlink(missing_ok=True)
            metadata = {"input_sha256": sha((folder / "kb.yaml").read_bytes())}
            certificate = folder / "certificate.json"
            certificate.unlink(missing_ok=True)
            try:
                run = subprocess.run(
                    [
                        sys.executable,
                        str(Path(__file__).resolve()),
                        "certify-worker",
                        "--input",
                        str(folder),
                        "--boomer-src",
                        str(source),
                    ],
                    capture_output=True,
                    text=True,
                    check=False,
                    timeout=timeout,
                    env={**os.environ, "PYTHONHASHSEED": "0"},
                )
                if run.returncode:
                    raise RuntimeError(run.stderr[-4000:])
            except subprocess.TimeoutExpired:
                write_json(
                    certificate, {**metadata, "status": "CERTIFICATION_TIMED_OUT"}
                )
            if len(kb["pfacts"]) > 15:
                write_json(
                    path, {**metadata, "status": "NOT_SMALL", "hypothesis_limit": 15}
                )
                continue
            try:
                run = subprocess.run(
                    [
                        sys.executable,
                        str(Path(__file__).resolve()),
                        "verify-worker",
                        "--input",
                        str(folder),
                        "--boomer-src",
                        str(source),
                    ],
                    capture_output=True,
                    text=True,
                    check=False,
                    timeout=timeout,
                    env={**os.environ, "PYTHONHASHSEED": "0"},
                )
                if run.returncode:
                    raise RuntimeError(run.stderr[-4000:])
            except subprocess.TimeoutExpired:
                write_json(
                    path,
                    {
                        **metadata,
                        "status": "ENUMERATION_TIMED_OUT",
                        "timeout_seconds": timeout,
                    },
                )
            print(slug, phase, json.loads(path.read_text())["status"], flush=True)


def report(out):
    for slug in CASES:
        projection = json.loads((out / slug / "projection.json").read_text())
        context = projection["ontology"]
        lines = [
            f"# {context[projection['series']]['label']} ({projection['series']})",
            "",
            "## Source entities and member coverage",
            "",
            "Candidates below are grounded entries or subtypes whose MONDO term has an explicit",
            "exact match to the numbered OMIM record. This is a mapping-based coverage audit,",
            "not independent evidence of clinical equivalence. A family entry alone is not",
            "counted as individual member coverage. Directional mappings in the selected records",
            "are also shown with their predicates; these are not exact member coverage.",
            "",
            "| OMIM member | Source label | MONDO exact matches | Before candidates | After candidates |",
            "|---|---|---|---|---|",
        ]
        for member in projection["series_members"]:
            cells = []
            for phase in ("before", "after"):
                matches = projection["snapshots"][phase]["coverage"][member][
                    "curated_candidates"
                ]
                directional = scoped_member_mappings(projection, phase, member)
                cells.append(
                    "; ".join(
                        [f"{c['name']} (`{c['path']}`)" for c in matches]
                        + [
                            f"{c['name']} — {c['predicate']} to {c['term']}"
                            for c in directional
                        ]
                    )
                    or "No grounded candidate"
                )
            terms = projection["snapshots"]["after"]["coverage"][member][
                "mondo_exact_matches"
            ]
            lines.append(
                f"| {member} | {context[member]['label']} | {', '.join(terms) or 'Not retrieved'} | {cells[0]} | {cells[1]} |"
            )
        lines += [
            "",
            "## Joint solver comparison",
            "",
            "| Snapshot | Curation commit | Hypotheses | Search status | Search confidence | Distinct satisfying assignments found | Enumeration | MAP certificate |",
            "|---|---|---:|---|---:|---:|---|---|",
        ]
        for phase in ("before", "after"):
            folder = out / slug / phase
            result = json.loads((folder / "result.json").read_text())
            solution = (
                yaml.safe_load((folder / "solution.yaml").read_text())
                if (folder / "solution.yaml").exists()
                else {}
            )
            verification = json.loads((folder / "enumeration.json").read_text())
            certificate = json.loads((folder / "certificate.json").read_text())
            lines.append(
                f"| [{phase}]({phase}/solution.md) | `{projection['snapshots'][phase]['commit']}` | {result.get('n_pfacts', 'NA')} | {result['status']} | {solution.get('confidence', 'NA')} | {result.get('number_of_satisfiable_combinations', 'NA')} | {verification['status']} | [{certificate['status']}]({phase}/certificate.json) |"
            )
        lines += [
            "",
            "Confidence compares the best two distinct complete assignments. It is not a",
            "mapping marginal or proof of biological equivalence. Timeout values are provisional.",
            "A separate MAP certificate proves the optimal all-true assignment and a distinct",
            "runner-up when its sufficient conditions hold; it does not compute marginals or",
            "whole-assignment posteriors. Both complete assignments are recorded in that file.",
            "",
            "### Exhaustive enumeration (complete probabilities)",
            "",
            "| Snapshot | Status | Distinct satisfying assignments | Confidence | Best whole-assignment posterior | Rejected mappings in optimal assignments |",
            "|---|---|---:|---:|---:|---|",
        ]
        for phase in ("before", "after"):
            enumerated = json.loads(
                (out / slug / phase / "enumeration.json").read_text()
            )
            lines.append(
                f"| [{phase}]({phase}/enumeration.json) | {enumerated['status']} | {enumerated.get('distinct_solutions', 'NA')} | {enumerated.get('confidence', 'NA')} | {enumerated.get('best_posterior', 'NA')} | {'None' if enumerated.get('rejected_high_prior_indices') == [[]] else enumerated.get('rejected_high_prior_indices', 'NA')} |"
            )
        lines += [
            "",
            "The complete source assertions, aliases, logical edges and mapping provenance are in",
            "[before/audit.json](before/audit.json) and [after/audit.json](after/audit.json).",
            "Frozen selected curation fields, source blob hashes, source labels and hierarchy are in",
            "[projection.json](projection.json). The parent directory documents assumptions and limitations.",
            "",
        ]
        (out / slug / "README.md").write_text("\n".join(lines))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "stage",
        choices=(
            "capture",
            "build",
            "solve",
            "verify",
            "verify-worker",
            "certify-worker",
            "report",
        ),
    )
    parser.add_argument("--out", type=Path, default=OUT)
    parser.add_argument("--oak-dir", type=Path, default=Path.home() / ".data/oaklib")
    parser.add_argument("--boomer-src", type=Path, default=os.environ.get("BOOMER_SRC"))
    parser.add_argument("--timeout", type=float, default=60)
    parser.add_argument("--input", type=Path)
    args = parser.parse_args()
    if args.stage == "capture":
        capture(args.out, args.oak_dir)
    elif args.stage == "build":
        build(args.out)
    elif args.stage == "report":
        report(args.out)
    else:
        if not args.boomer_src or args.timeout <= 0:
            parser.error("solve requires --boomer-src and a positive timeout")
        if args.stage in {"verify-worker", "certify-worker"}:
            if not args.input:
                parser.error("verify-worker requires --input")
            if args.stage == "verify-worker":
                verify_worker(args.input, args.boomer_src)
            else:
                certify_worker(args.input, args.boomer_src)
        elif args.stage == "verify":
            verify_all(args.out, args.boomer_src, args.timeout)
        else:
            solve_all(args.out, args.boomer_src, args.timeout)


if __name__ == "__main__":
    main()
