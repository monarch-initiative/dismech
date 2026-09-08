"""Audit ICD coverage without modifying Boomer inputs or disease curation.

Keep WHO ICD-10 and ICD-10-CM distinct. ORDO mappings are reached through
parent MONDO exact matches only, with their original SKOS predicates preserved.
Read both semantic-sql object and value columns: ORDO stores ICD mappings as
literals. All results describe local snapshots, not current coding guidance.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sqlite3
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "src"))
from dismech import kb_cache  # noqa: E402

PREDICATES = (
    "skos:exactMatch",
    "skos:broadMatch",
    "skos:narrowMatch",
    "skos:closeMatch",
    "skos:relatedMatch",
    "oio:hasDbXref",
)


def is_icd10(value):
    return isinstance(value, str) and value.startswith(
        ("ICD10CM:", "ICD10:", "ICD-10:")
    )


def icd_terms(value):
    """Find identifiers in facts/pfacts, excluding the labels dictionary."""
    if isinstance(value, dict):
        return set().union(*(icd_terms(v) for v in value.values()))
    if isinstance(value, list):
        return set().union(*(icd_terms(v) for v in value))
    return {value} if is_icd10(value) else set()


def mapping_index(connection):
    result = defaultdict(set)
    marks = ",".join("?" for _ in PREDICATES)
    for subject, predicate, obj, value in connection.execute(
        f"SELECT subject, predicate, object, value FROM statements "
        f"WHERE predicate IN ({marks})",
        PREDICATES,
    ):
        for target in (obj, value):
            if is_icd10(target):
                result[subject].add((predicate, target))
    return result


def write_tsv(path, rows, fields):
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(
            stream, fieldnames=fields, delimiter="\t", lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--oak-dir", type=Path, default=Path.home() / ".data/oaklib")
    parser.add_argument("--out", type=Path, default=REPO / "analyses/boomer/icd10")
    args = parser.parse_args()
    kb_cache.default_off()
    databases = {}
    snapshots = {}
    for name in ("mondo", "ordo"):
        path = (args.oak_dir / f"{name}.db").resolve()
        connection = sqlite3.connect(f"{path.as_uri()}?mode=ro", uri=True)
        databases[name] = connection
        with path.open("rb") as stream:
            checksum = hashlib.file_digest(stream, "sha256").hexdigest()
        snapshots[name] = {
            "sha256": checksum,
            "version": sorted(
                obj or value
                for obj, value in connection.execute(
                    "SELECT object, value FROM statements "
                    "WHERE predicate='owl:versionIRI'"
                )
                if obj or value
            ),
        }
    mondo = mapping_index(databases["mondo"])
    ordo = mapping_index(databases["ordo"])
    links = defaultdict(set)
    for subject, obj in databases["mondo"].execute(
        "SELECT subject, object FROM statements "
        "WHERE predicate='skos:exactMatch' AND object LIKE 'ORDO:%'"
    ):
        links[subject].add(obj)
    base = REPO / "analyses/boomer"
    with (base / "index.tsv").open() as stream:
        entries = list(csv.DictReader(stream, delimiter="\t"))
    coverage, mappings = [], []
    for entry in sorted(entries, key=lambda row: row["slug"]):
        slug, parent = entry["slug"], entry["parent_term"]
        disease = kb_cache.load_document(REPO / "kb/disorders" / f"{slug}.yaml")
        kb = kb_cache.load_document(base / "disorders" / slug / "kb.yaml")
        imported = icd_terms([kb.get("facts", []), kb.get("pfacts", [])])
        direct = (disease.get("mappings") or {}).get("icd10cm_mappings") or []
        evidence = []
        for mapping in direct:
            target = (mapping.get("term") or {}).get("id") or mapping.get("id")
            if target:
                evidence.append(
                    (
                        "dismech",
                        f"dismech:{slug}",
                        mapping.get("mapping_predicate", ""),
                        target,
                        mapping.get("mapping_source") or "UNSPECIFIED",
                    )
                )
        evidence.extend(
            ("mondo", parent, predicate, target, "mondo.db")
            for predicate, target in sorted(mondo[parent])
        )
        via_ordo = [
            ("ordo", source, predicate, target, "ordo.db")
            for source in sorted(links[parent])
            for predicate, target in sorted(ordo[source])
        ]
        evidence.extend(via_ordo)
        coverage.append(
            {
                "slug": slug,
                "name": entry["name"],
                "parent": parent,
                "mendelian": int(disease.get("category") == "Mendelian"),
                "solver_status": entry["status"],
                "boomer_icd10_terms": "|".join(sorted(imported)),
                "direct_icd10cm_count": sum(e[0] == "dismech" for e in evidence),
                "mondo_icd10_count": len(mondo[parent]),
                "exact_ordo_links": "|".join(sorted(links[parent])),
                "ordo_icd10_count": len(via_ordo),
                "ordo_predicates": "|".join(sorted({e[2] for e in via_ordo})),
                "no_mapping_found": int(not imported and not evidence),
            }
        )
        mappings.extend(
            dict(
                zip(
                    ("slug", "route", "subject", "predicate", "target", "source"),
                    (slug, *item),
                    strict=True,
                )
            )
            for item in evidence
        )
    for connection in databases.values():
        connection.close()
    summary = {"snapshots": snapshots, "cohorts": {}}
    for name, rows in (
        ("all", coverage),
        ("mendelian", [r for r in coverage if r["mendelian"]]),
    ):
        summary["cohorts"][name] = {
            "entries": len(rows),
            "boomer_icd10": sum(bool(r["boomer_icd10_terms"]) for r in rows),
            "direct_icd10cm": sum(bool(r["direct_icd10cm_count"]) for r in rows),
            "parent_mondo_icd10": sum(bool(r["mondo_icd10_count"]) for r in rows),
            "parent_ordo_icd10": sum(bool(r["ordo_icd10_count"]) for r in rows),
            "ordo_predicates_entry_counts": dict(
                Counter(p for r in rows for p in r["ordo_predicates"].split("|") if p)
            ),
            "no_mapping_found": sum(r["no_mapping_found"] for r in rows),
        }
    args.out.mkdir(parents=True, exist_ok=True)
    write_tsv(args.out / "coverage.tsv", coverage, list(coverage[0]))
    write_tsv(
        args.out / "mappings.tsv",
        mappings,
        ["slug", "route", "subject", "predicate", "target", "source"],
    )
    (args.out / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    (args.out / "missing-mendelian.txt").write_text(
        "".join(
            r["slug"] + "\n"
            for r in coverage
            if r["mendelian"] and r["no_mapping_found"]
        )
    )
    print(json.dumps(summary["cohorts"], indent=2))


if __name__ == "__main__":
    main()
