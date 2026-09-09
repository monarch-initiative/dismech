"""Directional ICD hypotheses, preserving source vocabulary and provenance."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import yaml

CONFIG = Path(__file__).resolve().parents[1] / "icd10/config.yaml"
SUPPORTED = {"skos:exactMatch", "skos:broadMatch", "skos:narrowMatch"}
FIELDS = (
    "slug",
    "route",
    "subject",
    "predicate",
    "source_target",
    "target",
    "source",
    "fact_type",
    "sub",
    "object",
    "prior",
    "status",
    "reason",
)


def fact_key(fact):
    copy = dict(fact)
    if copy["fact_type"] == "EquivalentTo":
        copy["sub"], copy["equivalent"] = sorted((copy["sub"], copy["equivalent"]))
    return json.dumps(copy, sort_keys=True)


def mapping_fact(subject, predicate, target):
    if predicate == "skos:exactMatch":
        return {"fact_type": "EquivalentTo", "sub": subject, "equivalent": target}
    if predicate == "skos:broadMatch":
        return {"fact_type": "ProperSubClassOf", "sub": subject, "sup": target}
    if predicate == "skos:narrowMatch":
        return {"fact_type": "ProperSubClassOf", "sub": target, "sup": subject}
    raise ValueError(f"No logical translation for {predicate}")


class ICD10Mappings:
    def __init__(self, external, oak_dir, config=CONFIG):
        from oaklib import get_adapter

        self.external = external
        if "ORDO" not in external.con:
            raise ValueError("ORDO OAK snapshot required for ICD enrichment")
        self.config = yaml.safe_load(Path(config).read_text())
        self.priors = self.config["priors"]
        if set(self.priors) != SUPPORTED or any(
            not 0 < probability < 1 for probability in self.priors.values()
        ):
            raise ValueError(
                "Expected explicit priors between 0 and 1 for exact/broad/narrow"
            )
        self.who_path = Path(oak_dir) / self.config["who"]["obo_file"]
        if not self.who_path.is_file():
            raise ValueError(
                "Run prepare_icd10.py first to prepare the pinned WHO snapshot"
            )
        if (
            hashlib.sha256(self.who_path.read_bytes()).hexdigest()
            != self.config["who"]["obo_sha256"]
        ):
            raise ValueError(
                "WHO OBO snapshot checksum mismatch; rerun prepare_icd10.py"
            )
        self.who = get_adapter(str(self.who_path))
        self._mappings, self._ancestors, self._labels = {}, {}, {}

    def provenance(self):
        snapshots = {}
        for name in ("ORDO", "ICD10CM"):
            connection = self.external.con.get(name)
            if connection is None:
                snapshots[name] = {"available": False}
                continue
            path = Path(connection.execute("PRAGMA database_list").fetchone()[2])
            with path.open("rb") as stream:
                sha = hashlib.file_digest(stream, "sha256").hexdigest()
            snapshots[name] = {"filename": path.name, "sha256": sha}
        return {"config": self.config, "snapshots": snapshots}

    def label(self, curie):
        if curie not in self._labels:
            self._labels[curie] = self.who.label(curie)
        return self._labels[curie]

    def ancestors(self, curie):
        if curie not in self._ancestors:
            self._ancestors[curie] = set(
                self.who.ancestors([curie], predicates=["rdfs:subClassOf"])
            ) - {curie}
        return self._ancestors[curie]

    def ordo_mappings(self, subject):
        if subject not in self._mappings:
            self._mappings[subject] = sorted(
                {
                    (predicate, target)
                    for predicate, obj, value in self.external.con["ORDO"].execute(
                        "SELECT predicate, object, value FROM statements WHERE subject=? "
                        "AND predicate LIKE 'skos:%'",
                        (subject,),
                    )
                    for target in (obj, value)
                    if target and target.startswith(("ICD-10:", "ICD10:"))
                }
            )
        return self._mappings[subject]

    def enrich(self, kb, slug, direct=()):
        """Append hypotheses and hard target hierarchy; return all source decisions.

        Uses ORDO nodes already connected in the saved input, including subtypes.
        Duplicate mapping paths do not multiply the prior for a single fact.
        Existing assertions, labels and probabilities are never overwritten.
        """
        facts = kb.setdefault("facts", [])
        pfacts = kb.setdefault("pfacts", [])
        labels = kb.setdefault("labels", {})
        hard = {fact_key(f) for f in facts}
        probabilities = {fact_key(p["fact"]): p["prob"] for p in pfacts}
        ordo_terms = sorted(
            {
                f[field]
                for f in facts + [p["fact"] for p in pfacts]
                for field in ("sub", "sup", "equivalent", "sibling")
                if isinstance(f.get(field), str) and f[field].startswith("ORDO:")
            }
        )
        candidates = [
            ("ordo", subject, predicate, target, "ordo.db", "")
            for subject in ordo_terms
            if not self.external.is_obsolete("ORDO", subject)
            for predicate, target in self.ordo_mappings(subject)
        ]
        for mapping in direct:
            term = mapping.get("term") or {}
            target = term.get("id") or mapping.get("id") or "UNSPECIFIED"
            source = mapping.get("mapping_source") or "UNSPECIFIED"
            candidates.append(
                (
                    "dismech",
                    f"dismech:{slug}",
                    mapping.get("mapping_predicate") or "UNSPECIFIED",
                    target,
                    source,
                    term.get("label") or "",
                )
            )
        rows = []
        for route, subject, predicate, raw_target, source, curated_label in sorted(
            set(candidates)
        ):
            target = raw_target.replace("ICD-10:", "ICD10:", 1)
            row = dict.fromkeys(FIELDS, "NA")
            row.update(
                slug=slug,
                route=route,
                subject=subject,
                predicate=predicate,
                source_target=raw_target,
                target=target,
                source=source,
                status="REVIEW",
            )
            rows.append(row)
            if route == "dismech" and source not in {"ICD10CM", "ICD-10-CM"}:
                row["reason"] = (
                    "WHO evidence does not verify ICD10CM identity or direction"
                    if source.startswith("ORPHA:")
                    else "ICD10CM provenance unspecified"
                )
                continue
            if predicate not in SUPPORTED:
                row["reason"] = "Predicate has no supported logical translation"
                continue
            vocab = "ICD10" if route == "ordo" else "ICD10CM"
            if not target.startswith(vocab + ":"):
                row["reason"] = "Unexpected target vocabulary"
                continue
            label = (
                self.label(target)
                if vocab == "ICD10"
                else self.external.label(vocab, target)
            )
            if not label:
                row["reason"] = (
                    "Target absent from classification; retain code qualifiers for review"
                )
                continue
            if vocab == "ICD10CM" and self.external.is_obsolete(vocab, target):
                row["reason"] = "Obsolete target"
                continue
            if curated_label and curated_label != label:
                row["reason"] = "Curated label differs from classification label"
                continue
            fact = mapping_fact(subject, predicate, target)
            key = fact_key(fact)
            probability = self.priors[predicate]
            row.update(
                fact_type=fact["fact_type"],
                sub=fact["sub"],
                object=fact.get("sup", fact.get("equivalent")),
                prior=probability,
            )
            if key in hard or (
                key in probabilities and probabilities[key] != probability
            ):
                row["reason"] = (
                    "Existing assertion strength retained; no duplicate added"
                )
                continue
            if key not in probabilities:
                pfacts.append({"fact": fact, "prob": probability})
                probabilities[key] = probability
            labels.setdefault(target, label)
            row.update(status="INCLUDED", reason="NA")

        def add(fact):
            key = fact_key(fact)
            if key not in hard:
                facts.append(fact)
                hard.add(key)

        # Only relationships from the target classification, never lexical code prefixes.
        for vocab in ("ICD10", "ICD10CM"):
            targets = sorted(
                {
                    f[field]
                    for f in facts + [p["fact"] for p in pfacts]
                    for field in ("sub", "sup", "equivalent", "sibling")
                    if isinstance(f.get(field), str)
                    and f[field].startswith(vocab + ":")
                }
            )
            for target in targets:
                add(
                    {
                        "fact_type": "MemberOfDisjointGroup",
                        "sub": target,
                        "group": vocab,
                    }
                )
                ancestors = (
                    self.ancestors(target)
                    if vocab == "ICD10"
                    else self.external.ancestors(vocab, target)
                )
                for parent in targets:
                    if parent != target and parent in ancestors:
                        add(
                            {
                                "fact_type": "ProperSubClassOf",
                                "sub": target,
                                "sup": parent,
                            }
                        )
        return rows
