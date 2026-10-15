"""Preserve MONDO xref annotations and compile curated proxy-merge exceptions."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from functools import lru_cache
from itertools import combinations
from pathlib import Path

from dismech import kb_cache

REPO = Path(__file__).resolve().parents[3]
DEFAULT_CATALOG = REPO / "analyses/boomer/proxy-merges/mondo-mappings.json"
EXTERNAL = {"DOID", "NCIT", "ORDO", "OMIM", "ICD10CM", "icd11f", "MESH", "EFO", "ICD10"}
ALIASES = {
    "Orphanet": "ORDO",
    "ORPHA": "ORDO",
    "icd11.foundation": "icd11f",
    "MIM": "OMIM",
    "MeSH": "MESH",
}


def normalize(curie):
    prefix, separator, local = curie.partition(":")
    return ALIASES.get(prefix, prefix) + separator + local


def digest(content):
    return hashlib.sha256(content).hexdigest()


def extract(obo_path, terms, source_url):
    """Parse OBO syntax, including xref qualifiers; never infer equivalence from a bare xref."""
    import fastobo

    records = {}
    for frame in fastobo.iter(obo_path):
        subject = str(frame.id)
        if subject not in terms:
            continue
        mappings = {}
        obsolete = False
        for clause in frame:
            if isinstance(clause, fastobo.term.IsObsoleteClause):
                obsolete = clause.obsolete
            if not isinstance(clause, fastobo.term.XrefClause):
                continue
            raw_target = str(clause.xref.id)
            target = normalize(raw_target)
            if target.split(":")[0] not in EXTERNAL:
                continue
            qualifiers = defaultdict(set)
            for qualifier in clause.qualifiers or []:
                qualifiers[str(qualifier.key)].add(str(qualifier.value))
            record = mappings.setdefault(target, {"raw_targets": [], "qualifiers": {}})
            record["raw_targets"] = sorted(set(record["raw_targets"]) | {raw_target})
            for key, values in qualifiers.items():
                record["qualifiers"][key] = sorted(
                    set(record["qualifiers"].get(key, [])) | values
                )
        records[subject] = {
            "obsolete": obsolete,
            "mappings": dict(sorted(mappings.items())),
        }
    return {
        "source_url": source_url,
        "source_sha256": digest(obo_path.read_bytes()),
        "selection": "MONDO subjects in saved Boomer mapping hypotheses",
        "requested_terms": sorted(terms),
        "missing_terms": sorted(terms - records.keys()),
        "terms": dict(sorted(records.items())),
    }


class ProxyPolicy:
    def __init__(self, catalog):
        self.catalog = catalog

    @classmethod
    def load(cls, path=DEFAULT_CATALOG):
        return cls(json.loads(Path(path).read_text()))

    def decisions(self, kb):
        targets = defaultdict(set)
        for pfact in kb.get("pfacts", []):
            fact = pfact["fact"]
            if fact["fact_type"] == "EquivalentTo" and fact["sub"].startswith("MONDO:"):
                target = fact["equivalent"]
                prefix = target.split(":")[0]
                if prefix in EXTERNAL:
                    targets[fact["sub"], prefix].add(target)
        decisions = []
        for (subject, prefix), members in sorted(targets.items()):
            if len(members) < 2:
                continue
            term = self.catalog["terms"].get(subject, {})
            mappings = term.get("mappings", {})
            equivalent = {
                target: record
                for target, record in mappings.items()
                if target.startswith(prefix + ":")
                and "MONDO:equivalentTo" in record["qualifiers"].get("source", [])
            }
            preferred = sorted(
                target
                for target, record in equivalent.items()
                if "MONDO:preferredExternal" in record["qualifiers"].get("source", [])
            )
            if term.get("obsolete"):
                decision = "REVIEW_OBSOLETE_MONDO"
            elif not members <= equivalent.keys():
                decision = "REVIEW_UNCONFIRMED_MAPPING"
            elif len(preferred) != 1:
                decision = "REVIEW_PREFERENCE_COUNT"
            elif preferred[0] not in members:
                decision = "REVIEW_PREFERRED_TARGET_ABSENT"
            else:
                decision = "PERMIT_PROXY_MERGE"
            decisions.append(
                {
                    "mondo": subject,
                    "vocabulary": prefix,
                    "targets": sorted(members),
                    "preferred_targets": preferred,
                    "decision": decision,
                }
            )
        return decisions

    def apply(self, kb):
        """Keep all priors; omit only non-equivalence pairs justified by this policy.

        Call on generator-owned inputs: same-vocabulary strict external hierarchy
        edges in these inputs were synthesized from ordinary source subclass edges.
        Curator-authored dismech subtype edges and MONDO constraints remain intact.
        """
        decisions = self.decisions(kb)
        permitted = defaultdict(set)
        for row in decisions:
            if row["decision"] == "PERMIT_PROXY_MERGE":
                permitted[row["vocabulary"]].update(combinations(row["targets"], 2))
        members = defaultdict(set)
        for fact in kb["facts"]:
            if (
                fact["fact_type"] == "MemberOfDisjointGroup"
                and fact["group"] in permitted
            ):
                members[fact["group"]].add(fact["sub"])
        facts = []
        for fact in kb["facts"]:
            if (
                fact["fact_type"] == "MemberOfDisjointGroup"
                and fact["group"] in permitted
            ):
                continue
            if fact["fact_type"] == "ProperSubClassOf":
                prefix = fact["sub"].split(":")[0]
                if prefix in EXTERNAL and fact["sup"].startswith(prefix + ":"):
                    fact = {**fact, "fact_type": "SubClassOf"}
            if fact not in facts:
                facts.append(fact)
        for prefix, entities in sorted(members.items()):
            for left, right in combinations(sorted(entities), 2):
                if (left, right) not in permitted[prefix]:
                    # Two-member groups also support Boomer's inference of
                    # ProperSubClassOf from SubClassOf + non-equivalence.
                    # NegatedFact(EquivalentTo) currently only checks violations.
                    group = "proxy-distinct:" + json.dumps(
                        [left, right], separators=(",", ":")
                    )
                    for entity in (left, right):
                        fact = {
                            "fact_type": "MemberOfDisjointGroup",
                            "sub": entity,
                            "group": group,
                        }
                        if fact not in facts:
                            facts.append(fact)
        kb["facts"] = facts
        return decisions


@lru_cache(maxsize=1)
def default_policy():
    return ProxyPolicy.load()


def provenance(kb, policy, input_bytes, graph_sources=None):
    return {
        "policy": "mondo_curated_proxy_merge_v1",
        "source_url": policy.catalog["source_url"],
        "source_sha256": policy.catalog["source_sha256"],
        "input_sha256": digest(input_bytes),
        "graph_sources": graph_sources,
        "annotations": {
            subject: policy.catalog["terms"].get(subject)
            for subject in sorted(
                {
                    p["fact"]["sub"]
                    for p in kb.get("pfacts", [])
                    if p["fact"].get("sub", "").startswith("MONDO:")
                }
            )
        },
        "decisions": policy.decisions(kb),
    }


def main():
    kb_cache.default_off()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--obo", type=Path, required=True)
    parser.add_argument("--source-url", required=True)
    parser.add_argument("--base", type=Path, default=REPO / "analyses/boomer")
    parser.add_argument("--out", type=Path, default=DEFAULT_CATALOG)
    args = parser.parse_args()
    terms = {
        p["fact"]["sub"]
        for path in sorted((args.base / "disorders").glob("*/kb.yaml"))
        for p in kb_cache.load_document(path).get("pfacts", [])
        if p["fact"]["fact_type"] == "EquivalentTo"
        and p["fact"]["sub"].startswith("MONDO:")
    }
    result = extract(args.obo, terms, args.source_url)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Extracted annotations for {len(result['terms'])} MONDO terms")


if __name__ == "__main__":
    main()
