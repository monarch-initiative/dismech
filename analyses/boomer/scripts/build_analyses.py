"""Generate one boomer analysis folder per grounded dismech disorder.

By default, for every `kb/disorders/` entry whose `disease_term` and at least one
`has_subtypes[].subtype_term` are grounded in MONDO, this assembles a single
knowledge base holding everything that bears on that entry's grounding:

* **dismech** -- each `subtype ProperSubClassOf parent` edge (hard; it is what
  `has_subtypes` means), and namespace disjointness so two distinct entries
  cannot collapse into one
* **MONDO**   -- the subsumption edges and `owl:disjointWith` axioms relating the
  entry's term to each subtype's term (hard; we test dismech against MONDO, not
  MONDO against itself)
* **mappings** -- one identity claim per grounded term, as probabilistic facts,
  each with the competing `ProperSubClassOf` readings in both directions

`--scope mendelian` includes grounded Mendelian entries even without subtypes;
`--scope expanded` takes their union with the legacy subtype cohort. Selection
uses the KB's explicit `category: Mendelian` designation. `--add-only --index ...` preserves existing results.

One KB per *disorder* rather than per pair is deliberate: an entry's subtypes all
share a parent, so solving them together lets a conflict in one subtype bear on
the others. It also matches how a curator reads the result -- "what does boomer
say about this disease".

Each folder gets:

    README.md      what was checked, per-subtype verdicts, what boomer did
    proxy-merges.json  MONDO xref annotations, decisions, and source provenance
    kb.yaml        the boomer input, runnable as
                   `pyboomer solve kb.yaml -t 60`
    solution.yaml  boomer's output, machine-readable
    solution.md    boomer's output, rendered

Always set a timeout. `-C` limits hypotheses per clique and may remove interacting
hypotheses; lowering it is not a semantics-preserving performance optimization.
`--with-icd10` adds directional ICD mappings to Mendelian entries only.

Usage:
    uv run --with networkx python analyses/boomer/scripts/build_analyses.py \
        --out analyses/boomer/disorders --boomer-src ~/repos/boomer-py/src
"""

from __future__ import annotations

import argparse
import collections
import contextlib
import csv
import glob
import io
import json
import sqlite3
import sys
from collections import Counter
from pathlib import Path

import yaml

OAK_DIR = Path.home() / ".data/oaklib"
MONDO_DB = OAK_DIR / "mondo.db"
REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from dismech import kb_cache  # noqa: E402

# External vocabularies reachable from MONDO by CONFIRMED equivalency, for which a
# local semantic-sql build exists so their OWN hierarchy can be consulted. This is
# what makes the analysis N-source rather than 2-source: each of these is an
# independent opinion about whether a subtype really sits under its parent.
EXTERNAL_DBS = {
    "DOID": "doid.db",
    "NCIT": "ncit.db",
    "ORDO": "ordo.db",
    "OMIM": "omim.db",
    "ICD10CM": "icd10cm.db",
    "icd11f": "icd11f.db",
    "MESH": "mesh.db",
    "EFO": "efo.db",
}

# prior that a curated mapping means identity, and the competing readings
P_IDENTITY = 0.90

# A curated `mappings.mondo_mappings` predicate overrides the default identity
# prior for the entry's own disease_term. dismech's disease_term is a grounding,
# so absent any statement we assume identity -- but where a curator has said
# explicitly that the relationship is narrower/broader, asserting identity anyway
# would manufacture a contradiction out of correct curation.
PREDICATE_PRIORS = {
    "skos:exactMatch": 0.95,
    "skos:closeMatch": 0.70,
    "skos:narrowMatch": 0.05,  # MONDO term is NARROWER than the dismech entry
    "skos:broadMatch": 0.05,  # MONDO term is BROADER
    "skos:relatedMatch": 0.30,
}
P_NARROWER = 0.07
P_BROADER = 0.03

# MONDO's own skos:exactMatch links. Higher than a dismech mapping because they are
# curated identity assertions in a reference ontology rather than a grounding choice.
# Deliberately NOT oio:hasDbXref, which is a cross-reference of unstated strength --
# treating those as equivalencies would inject false identity into every KB.
P_MONDO_EXACT = 0.95


def load_boomer(src):
    sys.path.insert(0, str(Path(src).expanduser()))
    from boomer.model import KB, SearchConfig
    from boomer.renderers.markdown_renderer import MarkdownRenderer
    from boomer.renderers.yaml_renderer import YAMLRenderer
    from boomer.search import solve

    return KB, SearchConfig, solve, MarkdownRenderer, YAMLRenderer


def term_id(descriptor):
    if not isinstance(descriptor, dict):
        return None
    return (descriptor.get("term") or {}).get("id") or descriptor.get("id")


class Mondo:
    def __init__(self, db):
        self.con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
        self._label: dict[str, str] = {}
        self._anc: dict[str, set[str]] = {}

    def versions(self):
        return sorted(
            obj or value
            for obj, value in self.con.execute(
                "SELECT object, value FROM statements WHERE predicate='owl:versionIRI'"
            )
            if obj or value
        )

    def label(self, curie):
        if curie not in self._label:
            row = self.con.execute(
                "select value from statements where subject=? and predicate='rdfs:label'",
                (curie,),
            ).fetchone()
            self._label[curie] = row[0] if row else curie
        return self._label[curie]

    def ancestors(self, curie):
        if curie not in self._anc:
            self._anc[curie] = {
                o
                for (o,) in self.con.execute(
                    "select object from entailed_edge where subject=? "
                    "and predicate='rdfs:subClassOf' and object like 'MONDO:%'",
                    (curie,),
                )
            }
        return self._anc[curie]

    def confirmed_equivalents(self, curie):
        """MONDO's ``skos:exactMatch`` targets, grouped by vocabulary.

        Only exactMatch. ``oio:hasDbXref`` is excluded on purpose: it asserts a
        cross-reference of unstated strength, and reading it as an equivalency
        would manufacture identity claims MONDO never made.
        """
        out = {}
        for (o,) in self.con.execute(
            "select object from statements where subject=? and predicate='skos:exactMatch' "
            "and object is not null",
            (curie,),
        ):
            out.setdefault(o.split(":")[0], set()).add(o)
        return out

    def disjoint_pairs(self, curies):
        placeholders = ",".join("?" * len(curies))
        return list(
            self.con.execute(
                f"select subject,object from statements where predicate='owl:disjointWith' "
                f"and subject in ({placeholders}) and object in ({placeholders})",
                (*curies, *curies),
            )
        )


class External:
    """Cached reader over the external ontologies' own hierarchies."""

    def __init__(self, oak_dir=OAK_DIR, dbs=None):
        if dbs is None:
            dbs = dict(EXTERNAL_DBS)
            # Reuse configured local OAK source names. OLS-backed validators do
            # not replace the local graph snapshots needed by this analysis.
            adapters = yaml.safe_load((REPO / "conf/oak_config.yaml").read_text())[
                "ontology_adapters"
            ]
            for vocab, adapter in adapters.items():
                if vocab in dbs and adapter.startswith("sqlite:obo:"):
                    dbs[vocab] = adapter.removeprefix("sqlite:obo:") + ".db"
        self.con = {}
        for vocab, filename in dbs.items():
            path = Path(oak_dir) / filename
            if path.exists():
                self.con[vocab] = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
        self._anc = {}
        self._labels = {}

    def label(self, vocab, curie):
        """Read a label from the same OAK snapshot used for this term's edges."""
        key = (vocab, curie)
        if key not in self._labels:
            con = self.con.get(vocab)
            row = (
                con.execute(
                    "select value from statements where subject=? "
                    "and predicate='rdfs:label' and value is not null "
                    "order by value limit 1",
                    (curie,),
                ).fetchone()
                if con is not None
                else None
            )
            self._labels[key] = row[0] if row else None
        return self._labels[key]

    def is_obsolete(self, vocab, curie):
        """True / False / None (term absent from the local build).

        Used to skip obsolete equivalency targets. MONDO merges propagate the
        merged-away class's xrefs onto the survivor, so a merged class can end up
        claiming identity with several terms in one vocabulary -- what MONDO calls
        a "proxy merge" (monarch-initiative/mondo#6331). Where the extra targets
        are obsolete in their source, MONDO calls it a *fake* proxy merge: the
        conflict is an artefact of stale xrefs, not a real disagreement, and
        feeding it to the solver was described upstream as "playing havoc with
        our attempts to use boomer".
        """
        key = ("obs", vocab, curie)
        if key not in self._anc:
            con = self.con.get(vocab)
            if con is None:
                self._anc[key] = None
            else:
                deprecated = con.execute(
                    "select 1 from statements where subject=? and predicate='owl:deprecated' "
                    "limit 1",
                    (curie,),
                ).fetchone()
                exists = con.execute(
                    "select 1 from statements where subject=? limit 1", (curie,)
                ).fetchone()
                self._anc[key] = True if deprecated else (False if exists else None)
        return self._anc[key]

    def ancestors(self, vocab, curie):
        key = (vocab, curie)
        if key not in self._anc:
            con = self.con.get(vocab)
            self._anc[key] = (
                {
                    o
                    for (o,) in con.execute(
                        "select object from entailed_edge where subject=? "
                        "and predicate='rdfs:subClassOf'",
                        (curie,),
                    )
                }
                if con
                else set()
            )
        return self._anc[key]

    def opinion(self, vocab, child_terms, parent_terms):
        """Does this vocabulary place any mapped child under any mapped parent?"""
        if any(
            p in self.ancestors(vocab, c) for c in child_terms for p in parent_terms
        ):
            return "AGREES"
        if any(
            c in self.ancestors(vocab, p) for c in child_terms for p in parent_terms
        ):
            return "REVERSED"
        return "SILENT"


def verdict_for(mondo, child, parent):
    if child == parent:
        return "SAME_TERM"
    if parent in mondo.ancestors(child):
        return "AGREES"
    if child in mondo.ancestors(parent):
        return "REVERSED"
    return "SILENT"


def mendelian_reasons(data):
    """Use the KB's explicit category for the first Mendelian expansion."""
    return ["KB_CATEGORY_MENDELIAN"] if data.get("category") == "Mendelian" else []


def collect(kb_glob, mondo, external, scope="subtypes", selection=None):
    """Yield grounded subtype records and/or the explicitly selected Mendelian cohort."""
    for path in sorted(glob.glob(kb_glob)):
        data = kb_cache.load_document(path) or {}
        if not isinstance(data, dict):
            continue
        reasons = mendelian_reasons(data) if scope != "subtypes" else []
        parent_term = term_id(data.get("disease_term"))
        grounded = bool(parent_term and parent_term.startswith("MONDO:"))
        if reasons and selection is not None:
            selection.append(
                {
                    "slug": Path(path).stem,
                    "parent_term": parent_term or "",
                    "status": "ELIGIBLE" if grounded else "NO_MONDO_GROUNDING",
                    "selection_reason": ";".join(reasons),
                }
            )
        if scope == "mendelian" and not reasons:
            continue
        if not parent_term or not parent_term.startswith("MONDO:"):
            continue
        # a curated predicate on the entry's own disease_term, if stated
        curated_predicate = next(
            (
                m.get("mapping_predicate")
                for m in (data.get("mappings") or {}).get("mondo_mappings") or []
                if term_id(m) == parent_term and m.get("mapping_predicate")
            ),
            None,
        )
        parent_equivs = mondo.confirmed_equivalents(parent_term)
        pairs = []
        for subtype in data.get("has_subtypes") or []:
            child = term_id(subtype.get("subtype_term"))
            if not child or not child.startswith("MONDO:"):
                continue
            child_equivs = mondo.confirmed_equivalents(child)
            # every vocabulary in which BOTH sides have a confirmed equivalent can
            # give an independent opinion on the subsumption
            opinions = {
                vocab: external.opinion(
                    vocab, child_equivs[vocab], parent_equivs[vocab]
                )
                for vocab in sorted(
                    set(child_equivs) & set(parent_equivs) & set(external.con)
                )
            }
            pairs.append(
                {
                    "subtype": subtype.get("name"),
                    "term": child,
                    "label": mondo.label(child),
                    "verdict": verdict_for(mondo, child, parent_term),
                    "equivs": {v: sorted(t) for v, t in sorted(child_equivs.items())},
                    "opinions": opinions,
                    "corroborated_by": sorted(
                        v for v, o in opinions.items() if o == "AGREES"
                    ),
                    "contradicted_by": sorted(
                        v for v, o in opinions.items() if o == "REVERSED"
                    ),
                }
            )
        if pairs or (scope != "subtypes" and reasons):
            rec = {
                "slug": Path(path).stem,
                "name": data.get("name") or Path(path).stem,
                "parent_term": parent_term,
                "parent_label": mondo.label(parent_term),
                "parent_equivs": {
                    v: sorted(t) for v, t in sorted(parent_equivs.items())
                },
                "curated_predicate": curated_predicate,
                "category": data.get("category"),
                "direct_icd10cm": (data.get("mappings") or {}).get("icd10cm_mappings")
                or [],
                "pairs": pairs,
            }
            if reasons:
                rec["selection_reason"] = reasons
            yield rec


def build_kb_dict(mondo, external, rec, icd10=None, proxy_policy=None):
    d_parent = f"dismech:{rec['slug']}"
    terms = {rec["parent_term"], *(p["term"] for p in rec["pairs"])}

    facts, seen = [], set()

    def add(fact):
        key = json.dumps(fact, sort_keys=True)
        if key not in seen:
            seen.add(key)
            facts.append(fact)

    add({"fact_type": "MemberOfDisjointGroup", "sub": d_parent, "group": "dismech"})
    for term in sorted(terms):
        add({"fact_type": "MemberOfDisjointGroup", "sub": term, "group": "MONDO"})

    labels = {
        d_parent: f"{rec['name']} (dismech entry)",
        rec["parent_term"]: rec["parent_label"],
    }
    predicate = rec.get("curated_predicate")
    p_identity = PREDICATE_PRIORS.get(predicate, P_IDENTITY)
    if predicate == "skos:narrowMatch":
        # curator has stated the MONDO term is NARROWER than this entry
        p_narrower, p_broader = 0.03, 0.90
    elif predicate == "skos:broadMatch":
        p_narrower, p_broader = 0.90, 0.03
    else:
        p_narrower, p_broader = P_NARROWER, P_BROADER
    pfacts = [
        {
            "fact": {
                "fact_type": "EquivalentTo",
                "sub": d_parent,
                "equivalent": rec["parent_term"],
            },
            "prob": p_identity,
        },
        {
            "fact": {
                "fact_type": "ProperSubClassOf",
                "sub": d_parent,
                "sup": rec["parent_term"],
            },
            "prob": p_narrower,
        },
        {
            "fact": {
                "fact_type": "ProperSubClassOf",
                "sub": rec["parent_term"],
                "sup": d_parent,
            },
            "prob": p_broader,
        },
    ]

    for pair in rec["pairs"]:
        d_child = f"dismech:{rec['slug']}#{pair['subtype']}"
        labels[d_child] = f"{rec['name']} / {pair['subtype']} (dismech subtype)"
        labels[pair["term"]] = pair["label"]
        add({"fact_type": "MemberOfDisjointGroup", "sub": d_child, "group": "dismech"})
        add({"fact_type": "ProperSubClassOf", "sub": d_child, "sup": d_parent})
        # MONDO's own opinion about this subtype term vs the entry's term
        for a, b in (
            (pair["term"], rec["parent_term"]),
            (rec["parent_term"], pair["term"]),
        ):
            if a != b and b in mondo.ancestors(a):
                add({"fact_type": "ProperSubClassOf", "sub": a, "sup": b})
        pfacts += [
            {
                "fact": {
                    "fact_type": "EquivalentTo",
                    "sub": d_child,
                    "equivalent": pair["term"],
                },
                "prob": P_IDENTITY,
            },
            {
                "fact": {
                    "fact_type": "ProperSubClassOf",
                    "sub": d_child,
                    "sup": pair["term"],
                },
                "prob": P_NARROWER,
            },
            {
                "fact": {
                    "fact_type": "ProperSubClassOf",
                    "sub": pair["term"],
                    "sup": d_child,
                },
                "prob": P_BROADER,
            },
        ]

    # --- external sources -------------------------------------------------
    # Each vocabulary MONDO confirms an equivalency into is a further opinion. Its
    # own subsumption edges enter as HARD facts (we are testing dismech against
    # these sources, not auditing them), and the MONDO<->external equivalency
    # enters as a pfact so boomer can retract it if the sources cannot be
    # reconciled.
    ext_terms = collections.defaultdict(set)
    for mondo_term, equivs in [
        (rec["parent_term"], rec["parent_equivs"]),
        *((p["term"], p["equivs"]) for p in rec["pairs"]),
    ]:
        for vocab, curies in equivs.items():
            if vocab not in external.con:
                continue
            for curie in curies:
                # an obsolete target cannot be an identity claim; including it
                # manufactures a "fake proxy merge" conflict
                if external.is_obsolete(vocab, curie):
                    continue
                ext_terms[vocab].add(curie)
                pfacts.append(
                    {
                        "fact": {
                            "fact_type": "EquivalentTo",
                            "sub": mondo_term,
                            "equivalent": curie,
                        },
                        "prob": P_MONDO_EXACT,
                    }
                )
    for vocab, curies in ext_terms.items():
        for curie in sorted(curies):
            add({"fact_type": "MemberOfDisjointGroup", "sub": curie, "group": vocab})
        for a in sorted(curies):
            for b in sorted(curies):
                if a != b and b in external.ancestors(vocab, a):
                    add({"fact_type": "SubClassOf", "sub": a, "sup": b})

    for s, o in mondo.disjoint_pairs(sorted(terms)):
        add({"fact_type": "DisjointWith", "sub": s, "sibling": o})

    kb_dict = {
        "name": f"dismech-{rec['slug']}",
        "description": (
            f"Grounding check for the dismech entry {rec['name']}: its "
            f"{len(rec['pairs'])} grounded subtype(s) against MONDO's hierarchy."
            if rec["pairs"]
            else f"Cross-source grounding check for the Mendelian dismech entry {rec['name']}; "
            "no grounded subtype pairs."
        ),
        "facts": facts,
        "pfacts": pfacts,
        "labels": labels,
    }
    for curie in add_external_labels(kb_dict, external):
        print(f"No label in local OAK snapshot: {curie}", file=sys.stderr)
    if icd10 is not None and rec.get("category") == "Mendelian":
        icd10.enrich(kb_dict, rec["slug"], rec.get("direct_icd10cm", []))
    from proxy_merges import default_policy

    (proxy_policy or default_policy()).apply(kb_dict)
    return kb_dict


def add_external_labels(kb_dict, external):
    """Add missing external labels without changing facts or existing labels.

    Return unresolved identifiers rather than manufacturing a label from a CURIE.
    Sorted additions keep repeated generation stable across hash seeds.
    """
    labels = kb_dict.setdefault("labels", {})
    facts = list(kb_dict.get("facts", [])) + [
        p["fact"] for p in kb_dict.get("pfacts", [])
    ]
    entities = {
        fact[field]
        for fact in facts
        for field in ("sub", "sup", "equivalent", "sibling")
        if field in fact and fact[field].split(":", 1)[0] in EXTERNAL_DBS
    }
    missing = []
    for curie in sorted(entities - labels.keys()):
        label = external.label(curie.split(":", 1)[0], curie)
        if label:
            labels[curie] = label
        else:
            missing.append(curie)
    return missing


def fill_labels(out_root, external, only=None):
    """Enrich saved inputs only; never re-solve or regenerate the source KB."""
    changed = added = 0
    missing = set()
    for path in sorted(Path(out_root).glob("*/kb.yaml")):
        if only and path.parent.name != only:
            continue
        original = path.read_text()
        kb_dict = yaml.safe_load(original)
        before = len(kb_dict.get("labels", {}))
        missing.update(add_external_labels(kb_dict, external))
        count = len(kb_dict["labels"]) - before
        if count:
            path.write_text(yaml.safe_dump(kb_dict, sort_keys=False))
            changed += 1
            added += count
    print(f"Added {added} labels in {changed} KB files; {len(missing)} unresolved IDs.")
    for curie in sorted(missing):
        print(f"No label in local OAK snapshot: {curie}", file=sys.stderr)
    return missing


# Posteriors accumulate in an order that depends on set/dict iteration, so repeated
# runs differ in the last bits of the float -- 0.3044046168087602 against
# 0.30440461680876013. Semantically identical, but it churns ~590 committed files
# per regeneration and makes review diffs useless. Rounding well below any
# meaningful precision, and dropping wall-clock timings (a property of the run, not
# of the result), makes regeneration byte-stable.
FLOAT_PRECISION = 12


def stabilise_floats(solution):
    """Round solution floats and drop timings so regeneration is byte-stable."""
    # time_elapsed is a read-only property computed from these two
    for attr in ("time_started", "time_finished"):
        with contextlib.suppress(AttributeError, ValueError, TypeError):
            setattr(solution, attr, None)
    for attr in (
        "confidence",
        "prior_prob",
        "posterior_prob",
        "proportion_of_combinations_explored",
    ):
        value = getattr(solution, attr, None)
        if isinstance(value, float):
            with contextlib.suppress(AttributeError, ValueError, TypeError):
                setattr(solution, attr, round(value, FLOAT_PRECISION))
    for solved in solution.solved_pfacts or []:
        if isinstance(getattr(solved, "posterior_prob", None), float):
            solved.posterior_prob = round(solved.posterior_prob, FLOAT_PRECISION)
    for sub in solution.sub_solutions or []:
        stabilise_floats(sub)


INDEX_FIELDNAMES = (
    "slug",
    "name",
    "parent_term",
    "n_subtypes",
    "n_pfacts",
    "agrees",
    "silent",
    "reversed",
    "same_term",
    "status",
    "n_retracted",
)


VERDICT_NOTE = {
    "AGREES": "MONDO has this subtype's term as a descendant of the entry's term.",
    "SILENT": "MONDO relates the two terms in neither direction - usually a missing MONDO `is_a` edge.",
    "REVERSED": "MONDO has the entry's term as a descendant of this subtype's term - backwards from dismech.",
    "SAME_TERM": "Subtype and entry are grounded to the same MONDO term.",
}


def write_readme(folder, rec, sol, retracted, timed_out, inputs_only=False):
    counts = Counter(p["verdict"] for p in rec["pairs"])
    lines = [
        f"# {rec['name']}",
        "",
        (
            f"Boomer grounding analysis for [`kb/disorders/{rec['slug']}.yaml`]"
            f"(../../../../kb/disorders/{rec['slug']}.yaml)."
        ),
        "",
        (
            f"- **Entry term:** [`{rec['parent_term']}`]"
            f"(http://purl.obolibrary.org/obo/{rec['parent_term'].replace(':', '_')}) "
            f"{rec['parent_label']}"
        ),
        f"- **Grounded subtypes:** {len(rec['pairs'])}",
        "- **Verdicts:** "
        + (
            ", ".join(f"{v} {n}" for v, n in counts.most_common())
            or "Not applicable: no grounded subtype pairs"
        ),
    ]
    if rec.get("selection_reason"):
        lines += ["- **Mendelian selection:** " + "; ".join(rec["selection_reason"])]
    if rec["pairs"]:
        lines += [
            "",
            "## Subtypes",
            "",
            "| Subtype | MONDO term | Label | MONDO | Other sources |",
            "|---|---|---|---|---|",
        ]
    else:
        lines += [
            "",
            "This input checks the disease's cross-source mappings. It makes no",
            "subtype assertion, and agreement does not validate a subtype hierarchy.",
        ]
    for pair in rec["pairs"]:
        if pair["contradicted_by"]:
            others = "⚠ contradicted by " + ", ".join(pair["contradicted_by"])
        elif pair["corroborated_by"]:
            others = "✓ " + ", ".join(pair["corroborated_by"])
        elif pair["opinions"]:
            others = "silent (" + ", ".join(sorted(pair["opinions"])) + ")"
        else:
            others = "— no shared vocabulary"
        lines.append(
            f"| {pair['subtype']} | `{pair['term']}` | {pair['label']} | "
            f"`{pair['verdict']}` | {others} |"
        )

    corroborated = [
        p for p in rec["pairs"] if p["verdict"] == "SILENT" and p["corroborated_by"]
    ]
    if corroborated:
        lines += [
            "",
            "### Corroborated elsewhere",
            "",
            "MONDO asserts no relation for these, but at least one other ontology that",
            "MONDO confirms an equivalency into does place the subtype under the parent.",
            "That makes them evidenced MONDO gaps rather than open questions:",
            "",
        ]
        for pair in corroborated:
            srcs = ", ".join(
                f"{v} ({', '.join(pair['equivs'].get(v, []))})"
                for v in pair["corroborated_by"]
            )
            lines.append(f"- **{pair['subtype']}** — {srcs}")

    lines += ["", "## What boomer did", ""]
    if timed_out:
        lines += [
            "The search **timed out**, so the assignment below is the best found within the",
            "budget rather than a settled result. Treat it as indicative only.",
            "",
        ]
    if inputs_only:
        lines += [
            "The solver has **not been run** for this input. No mapping acceptance,",
            "retraction, posterior probability or global-consistency result is asserted.",
            "",
        ]
    elif retracted:
        lines += [
            "Boomer could **not** accept every mapping at once and retracted the following",
            "mapping claim(s) to restore consistency:",
            "",
        ]
        lines += [f"- `{sub}` {relation} `{obj}`" for sub, relation, obj in retracted]
        lines += [
            "",
            "A retraction means these assertions are jointly unsatisfiable, not that the",
            "retracted mapping is necessarily the wrong one. Which assertion to give up is a",
            "curation decision.",
            "",
        ]
    else:
        lines += [
            "All asserted high-prior mappings were accepted together.",
            "The included mapping and ontology constraints are jointly consistent for this entry.",
            "",
        ]
    if counts.get("SILENT"):
        lines += [
            f"{counts['SILENT']} subtype(s) are `SILENT`: MONDO asserts no path between the",
            "terms in either direction. That is consistent (nothing is violated) but",
            "uncorroborated, and generally indicates a missing `is_a` edge in MONDO rather",
            "than a dismech error. These are candidate MONDO enrichment proposals.",
            "",
        ]

    if counts:
        lines += [
            "## Verdict meanings",
            "",
            *[f"- **`{k}`** - {v}" for k, v in VERDICT_NOTE.items() if counts.get(k)],
            "",
        ]
    lines += [
        "## Files",
        "",
        "| File | What |",
        "|---|---|",
        "| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60`. |",
        *(
            []
            if inputs_only
            else [
                "| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |",
                "| [`solution.md`](solution.md) | Boomer output, rendered. |",
            ]
        ),
        "",
        "Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).",
        "",
    ]
    (folder / "README.md").write_text("\n".join(lines))


def retracted_mappings(sol):
    """Rejected high-prior identities and directions, excluding unassessed facts."""
    if sol is None:
        return []
    return sorted(
        (
            f.sub,
            "≡" if type(f).__name__ == "EquivalentTo" else "⊂",
            f.equivalent if type(f).__name__ == "EquivalentTo" else f.sup,
        )
        for gp in (sol.solved_pfacts or [])
        if type(f := gp.pfact.fact).__name__ in {"EquivalentTo", "ProperSubClassOf"}
        and gp.truth_value is False
        and gp.pfact.prob >= 0.5
    )


def main(argv=None):
    kb_cache.default_off()
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--kb", default=str(REPO / "kb/disorders/*.yaml"))
    ap.add_argument("--out", required=True)
    ap.add_argument("--db", default=str(MONDO_DB))
    ap.add_argument("--boomer-src", default="~/repos/boomer-py/src")
    ap.add_argument("--timeout", type=int, default=60)
    ap.add_argument(
        "--partition-threshold",
        type=int,
        default=6,
        help=(
            "Minimum pfacts before boomer attempts partitioning. This is not a cap "
            "on clique size and does not guarantee that a solve finishes before timeout."
        ),
    )
    ap.add_argument("--only", help="restrict to one slug (for debugging)")
    ap.add_argument(
        "--with-icd10",
        action="store_true",
        help="Include directional ICD mappings for Mendelian entries (requires prepared WHO snapshot)",
    )
    ap.add_argument("--index", help="TSV index to write")
    ap.add_argument(
        "--inputs-only",
        action="store_true",
        help="Generate KB inputs and reports marked NOT_RUN, without loading the solver",
    )
    ap.add_argument(
        "--scope",
        choices=("subtypes", "mendelian", "expanded"),
        default="subtypes",
        help="Legacy grounded subtype pairs, all selected Mendelian entries, or their union",
    )
    ap.add_argument(
        "--add-only",
        action="store_true",
        help="Preserve indexed analysis folders and add only new entries (requires --index)",
    )
    ap.add_argument(
        "--selection-report",
        help="Write the Mendelian cohort and selection reasons as TSV",
    )
    ap.add_argument(
        "--oak-dir", default=str(OAK_DIR), help="Local OAK ontology snapshots"
    )
    ap.add_argument(
        "--labels-only",
        action="store_true",
        help="Fill missing external labels in saved kb.yaml files; do not solve or change reports",
    )
    from proxy_merges import DEFAULT_CATALOG, ProxyPolicy, provenance

    ap.add_argument(
        "--mapping-annotations",
        type=Path,
        default=DEFAULT_CATALOG,
        help="Pinned MONDO xref annotation catalog for curated proxy-merge exceptions",
    )
    args = ap.parse_args(argv)

    existing = {}
    if args.add_only or (args.only and args.index):
        if not args.index or not Path(args.index).is_file() or args.labels_only:
            ap.error(
                "Updating indexed analyses requires an existing --index and cannot accompany --labels-only"
            )
        with Path(args.index).open() as fh:
            reader = csv.DictReader(fh, delimiter="\t")
            if reader.fieldnames != list(INDEX_FIELDNAMES):
                ap.error(
                    "Existing index columns do not match the analysis index format"
                )
            existing = {r["slug"]: r for r in reader}
        for slug in existing:
            names = (
                ("kb.yaml", "README.md")
                if existing[slug]["status"] == "NOT_RUN"
                else ("kb.yaml", "solution.yaml", "solution.md", "README.md")
            )
            for name in names:
                if not (Path(args.out) / slug / name).is_file():
                    ap.error(f"Indexed analysis is incomplete: {slug}/{name}")

    external = External(oak_dir=args.oak_dir)
    icd10 = None
    if args.with_icd10:
        from icd10_enrichment import ICD10Mappings

        icd10 = ICD10Mappings(external, args.oak_dir)
    if args.labels_only:
        if args.index:
            ap.error("--labels-only does not regenerate --index")
        fill_labels(args.out, external, args.only)
        return

    if not args.inputs_only:
        KB, SearchConfig, solve, MarkdownRenderer, YAMLRenderer = load_boomer(
            args.boomer_src
        )
    proxy_policy = ProxyPolicy.load(args.mapping_annotations)
    mondo = Mondo(args.db)
    graph_sources = {"mondo_version": mondo.versions()}
    cfg = (
        None
        if args.inputs_only
        else SearchConfig(
            timeout_seconds=args.timeout,
            partition_initial_threshold=args.partition_threshold,
        )
    )
    out_root = Path(args.out)
    out_root.mkdir(parents=True, exist_ok=True)

    index, tally, selection = [], Counter(), []
    records = [
        r
        for r in collect(args.kb, mondo, external, args.scope, selection)
        if not args.only or r["slug"] == args.only
    ]
    if args.add_only:
        records = [r for r in records if r["slug"] not in existing]
        for rec in records:
            if (out_root / rec["slug"]).exists():
                ap.error(f"Refusing to overwrite an unindexed folder: {rec['slug']}")
    if args.selection_report:
        with Path(args.selection_report).open("w", newline="") as fh:
            writer = csv.DictWriter(
                fh,
                fieldnames=("slug", "parent_term", "status", "selection_reason"),
                delimiter="\t",
            )
            writer.writeheader()
            writer.writerows(selection)
    print(
        f"Selected {len(records)} analyses to generate; preserving {len(existing)} indexed analyses.",
        flush=True,
    )
    for i, rec in enumerate(records, 1):
        kb_dict = build_kb_dict(mondo, external, rec, icd10, proxy_policy)
        sol = None
        if not args.inputs_only:
            kb = KB.model_validate(kb_dict)
            with contextlib.redirect_stdout(io.StringIO()):
                sol = solve(kb, cfg)
            # the markdown renderer titles the solution from this; unset it renders "## None"
            sol.name = kb_dict["name"]
            stabilise_floats(sol)

        # Include rejected high-prior directional mappings as well as identities.
        # Low-prior alternatives and unassessed (None) facts are not retractions.
        retracted = retracted_mappings(sol)
        timed_out = bool(sol and sol.timed_out)

        folder = out_root / rec["slug"]
        if args.inputs_only and any(
            (folder / name).exists() for name in ("solution.yaml", "solution.md")
        ):
            raise ValueError(
                f"Refusing to leave stale solutions beside new inputs: {folder}"
            )
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "kb.yaml").write_text(yaml.safe_dump(kb_dict, sort_keys=False))
        (folder / "proxy-merges.json").write_text(
            json.dumps(
                provenance(
                    kb_dict,
                    proxy_policy,
                    (folder / "kb.yaml").read_bytes(),
                    graph_sources,
                ),
                indent=2,
            )
            + "\n"
        )
        if sol is not None:
            (folder / "solution.yaml").write_text(YAMLRenderer().render(sol, kb))
            (folder / "solution.md").write_text(MarkdownRenderer().render(sol, kb))
        write_readme(folder, rec, sol, retracted, timed_out, args.inputs_only)

        readme = folder / "README.md"
        text = readme.read_text()
        link = "MONDO xref annotations and proxy-merge decisions: [provenance](proxy-merges.json).\n\n"
        if "## What boomer did" in text:
            text = text.replace("## What boomer did", link + "## What boomer did", 1)
        else:
            text += "\n" + link
        readme.write_text(text)

        counts = Counter(p["verdict"] for p in rec["pairs"])
        status = (
            "NOT_RUN"
            if args.inputs_only
            else "TIMED_OUT"
            if timed_out
            else ("RETRACTED" if retracted else "ALL_MAPPINGS_CONSISTENT")
        )
        tally[status] += 1
        for verdict, n in counts.items():
            tally[f"pair:{verdict}"] += n
        index.append(
            {
                "slug": rec["slug"],
                "name": rec["name"],
                "parent_term": rec["parent_term"],
                "n_subtypes": len(rec["pairs"]),
                "n_pfacts": len(kb_dict["pfacts"]),
                "agrees": counts.get("AGREES", 0),
                "silent": counts.get("SILENT", 0),
                "reversed": counts.get("REVERSED", 0),
                "same_term": counts.get("SAME_TERM", 0),
                "status": status,
                "n_retracted": "NA" if args.inputs_only else len(retracted),
            }
        )
        if i % 50 == 0:
            print(f"  {i}/{len(records)}", file=sys.stderr)

    if args.index:
        # explicit fieldnames: deriving them from index[0] truncates the file and
        # then raises IndexError when no record matched (e.g. a --only slug that
        # does not exist). Both sibling audit scripts already do this.
        with Path(args.index).open("w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(INDEX_FIELDNAMES), delimiter="\t")
            w.writeheader()
            merged = {**existing, **{row["slug"]: row for row in index}}
            w.writerows(merged[slug] for slug in sorted(merged))

    print(f"wrote {len(index)} disorder folders -> {out_root}")
    for k, n in sorted(tally.items()):
        print(f"  {n:5d}  {k}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
