#!/usr/bin/env python3
"""Audit MONDO classes mapped ``MONDO:equivalentTo`` an OMIM phenotypic series (OMIMPS).

Motivation (Mondo issue on ``has_characteristic inherited`` over broad grouping classes,
mirrored into dismech): the OMIM_phenotypic_series DOSDP pattern requires every class
carrying an ``OMIMPS:`` equivalentTo xref to be an inherited disease. Where the OMIMPS
covers only the Mendelian *subset* of a broad clinical entity -- or, worse, is a series of
GWAS **susceptibility loci** rather than of diseases at all (celiac disease, PS212750) --
that requirement relabels a whole subtree as hereditary.

This script answers the two dismech-side questions the ticket asks:

(a) does it make sense to mint a ``kb/groupings/`` entry for the OMIMPS-derived object?
(b) how heterogeneous is each series -- in particular does it mix genetic and acquired
    forms?

For each audited class it computes, straight from ``mondo.obo`` (no network at analysis
time), the is-a descendant profile:

* ``MENDELIAN``      -- descendant with ``has_material_basis_in_germline_mutation_in``
* ``SUSCEPTIBILITY`` -- descendant in the MONDO ``predisposition`` subset, or labelled
  "susceptibility to" (the OMIM ``{braces}`` convention -- a risk locus, not a disease)
* ``SOMATIC``        -- descendant with ``has_material_basis_in_somatic_mutation_in``
* ``INFECTIOUS``     -- descendant of ``MONDO:0005550`` / carrying an infectious agent
* ``ACQUIRED``       -- descendant whose label denotes a non-genetic acquired form
* ``UNMAPPED_LOCUS`` -- descendant with an OMIM equivalentTo xref but NO gene relation: the
  proxy for an OMIM phenotype-mapping-key-2 entry (linkage-mapped locus, gene unknown)
* ``UNSPECIFIED``    -- everything else (clinical subdivision, unclassified)

Descendants are only half the picture. MONDO deliberately keeps OMIM ``{susceptibility}``
entries OUT of the is-a tree of the disease they predispose to: they are
``is_a MONDO:0020573 inherited disease susceptibility`` with an explicit
``excluded_subClassOf`` and a ``predisposes_towards`` link. The count of such inbound
**predisposers** is therefore the sharpest single measure of "this OMIMPS is a
susceptibility-locus series, not a disease series", and is reported alongside the
descendant profile.

Alongside the MONDO profile it reports dismech coverage: which descendants are anchored by a
``kb/disorders`` entry (``disease_term`` / ``has_subtypes[].subtype_term`` /
``mappings.mondo_mappings``), how many DISTINCT entries that is, and whether an existing
``kb/groupings`` entry already collects them.

The **series kind** is then derived from the profile:

* ``SUSCEPTIBILITY_SERIES`` -- members are declared OMIM ``{braces}`` risk loci. The OMIMPS
  is not a set of diseases; there is nothing to group. Model as ONE dismech Disease with
  ``genetic:`` risk-factor rows. (celiac disease is the exemplar.)
* ``LOCUS_SERIES``          -- members are mostly numbered linkage intervals whose gene is
  unidentified (MYP1-25, IBD1-30, PBC1-5). Same disposition; add members as genes are found.
* ``MENDELIAN_SERIES``      -- typed members are germline-gene diseases and the parent has
  no acquired forms in MONDO. A dismech grouping over the members is well-formed.
* ``MIXED_GENETIC_ACQUIRED``-- parent is a broad clinical entity with both germline-gene
  members and infectious/acquired/somatic descendants. A dismech grouping must be minted
  over the *genetic subset*, never over the clinical parent.
* ``SPARSE``                -- too few typed descendants to characterise.

Caveat: the acquired count is a FLOOR. It can only see acquired forms MONDO actually models
under the class, and MONDO models them sparsely (it has no secondary craniosynostosis, no
acquired hypogonadotropic hypogonadism, no secondary parkinsonism).

Usage::

    uv run python scripts/omimps_grouping_audit.py --obo /path/to/mondo.obo
    uv run python scripts/omimps_grouping_audit.py --focus all --tsv out.tsv
    uv run python scripts/omimps_grouping_audit.py --detail MONDO:0005130
"""

from __future__ import annotations

import argparse
import glob
import os
import re
import sys
import urllib.request
from collections import defaultdict

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))

from dismech.yaml_io import safe_load

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DISORDERS_DIR = os.path.join(ROOT, "kb", "disorders")
GROUPINGS_DIR = os.path.join(ROOT, "kb", "groupings")
MONDO_URL = "https://purl.obolibrary.org/obo/mondo.obo"

HEREDITARY = "MONDO:0003847"
INFECTIOUS = "MONDO:0005550"

# The 42 broad grouping classes flagged in the Mondo audit (2026-07-31). Ordered as in the
# audit table: descendant count descending.
AUDIT_CLASSES = [
    "MONDO:0021094", "MONDO:0004983", "MONDO:0015469", "MONDO:0005129", "MONDO:0018555",
    "MONDO:0005265", "MONDO:0015168", "MONDO:0000358", "MONDO:0001384", "MONDO:0000448",
    "MONDO:0005180", "MONDO:0020836", "MONDO:0005803", "MONDO:0016537", "MONDO:0003037",
    "MONDO:0018677", "MONDO:0016296", "MONDO:0005150", "MONDO:0015279", "MONDO:0007915",
    "MONDO:0019165", "MONDO:0015486", "MONDO:0005349", "MONDO:0005115", "MONDO:0019037",
    "MONDO:0016820", "MONDO:0005081", "MONDO:0006248", "MONDO:0005083", "MONDO:0005388",
    "MONDO:0005382", "MONDO:0004822", "MONDO:0019415", "MONDO:0016215", "MONDO:0009813",
    "MONDO:0000334", "MONDO:0100280", "MONDO:0007275", "MONDO:0005130", "MONDO:0019201",
    "MONDO:0005445", "MONDO:0005342",
]

# Label markers for an acquired (non-germline) form. Deliberately conservative: each is a
# word that names the acquiring process, not merely a clinical qualifier.
ACQUIRED_PATTERNS = [
    r"\bacquired\b", r"\bsenile\b", r"\bage-related\b", r"\bdrug-induced\b",
    r"\bradiation\b", r"\btraumatic\b", r"\bpost-?(?:infectious|traumatic|operative|surgical)\b",
    r"\bsecondary\b", r"\balcoholic\b", r"\btoxic\b", r"\biatrogenic\b",
    r"\binfectious\b", r"\bviral\b", r"\bbacterial\b", r"\bparasitic\b",
    r"\bdiabet(?:ic|es)\b",
]
ACQUIRED_RE = re.compile("|".join(ACQUIRED_PATTERNS), re.IGNORECASE)
SUSCEPTIBILITY_RE = re.compile(r"susceptib|predispos", re.IGNORECASE)

TIERS = ["MENDELIAN", "SUSCEPTIBILITY", "SOMATIC", "INFECTIOUS", "ACQUIRED", "UNMAPPED_LOCUS",
         "UNSPECIFIED"]


class Mondo:
    """Minimal ``mondo.obo`` reader: labels, is-a graph, xrefs, subsets, relationships."""

    def __init__(self, path: str):
        self.label: dict[str, str] = {}
        self.parents: dict[str, list[str]] = defaultdict(list)
        self.children: dict[str, list[str]] = defaultdict(list)
        self.omimps: dict[str, list[str]] = defaultdict(list)
        self.omim: dict[str, list[str]] = defaultdict(list)
        self.subsets: dict[str, set[str]] = defaultdict(set)
        self.germline_genes: dict[str, list[str]] = defaultdict(list)
        self.somatic: set[str] = set()
        self.infectious_agent: set[str] = set()
        self.obsolete: set[str] = set()
        self.predisposers: dict[str, list[str]] = defaultdict(list)
        # Classes defined as "<genus> and has_characteristic some inherited" -- the classes a
        # spurious `inherited` claim silently pulls a disease into.
        self.inherited_equivalents: set[str] = set()
        self._ancestor_cache: dict[str, set[str]] = {}
        self._parse(path)
        for child, ps in self.parents.items():
            for p in ps:
                self.children[p].append(child)

    def _parse(self, path: str) -> None:
        cur = None
        in_term = False
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                line = line.rstrip("\n")
                if line.startswith("["):
                    in_term = line == "[Term]"
                    cur = None
                    continue
                if not in_term or not line:
                    continue
                tag, _, rest = line.partition(": ")
                if tag == "id":
                    cur = rest.strip()
                    continue
                if cur is None or not cur.startswith("MONDO:"):
                    continue
                if tag == "name":
                    self.label[cur] = rest
                elif tag == "is_a":
                    self.parents[cur].append(rest.split(" ", 1)[0].split("{")[0].strip())
                elif tag == "subset":
                    self.subsets[cur].add(rest.split(" ")[0].split("{")[0].strip())
                elif tag == "is_obsolete" and rest.strip() == "true":
                    self.obsolete.add(cur)
                elif tag == "xref":
                    if rest.startswith("OMIMPS:") and "MONDO:equivalentTo" in rest:
                        self.omimps[cur].append(rest.split(" ")[0])
                    elif rest.startswith("OMIM:") and "MONDO:equivalentTo" in rest:
                        self.omim[cur].append(rest.split(" ")[0])
                elif tag == "intersection_of" and rest.startswith("has_characteristic MONDO:0021152"):
                    self.inherited_equivalents.add(cur)
                elif tag == "relationship":
                    pred, _, obj = rest.partition(" ")
                    if pred == "has_material_basis_in_germline_mutation_in":
                        gene = obj.split("!")[-1].strip() if "!" in obj else obj.split(" ")[0]
                        self.germline_genes[cur].append(gene)
                    elif pred == "has_material_basis_in_somatic_mutation_in":
                        self.somatic.add(cur)
                    elif pred == "disease_has_infectious_agent":
                        self.infectious_agent.add(cur)
                    elif pred == "predisposes_towards":
                        target = obj.split(" ")[0].split("{")[0].strip()
                        if target.startswith("MONDO:"):
                            self.predisposers[target].append(cur)

    def descendants(self, term: str) -> set[str]:
        """Proper (non-reflexive) is-a descendants, obsoletes dropped."""
        seen: set[str] = set()
        stack = list(self.children.get(term, []))
        while stack:
            t = stack.pop()
            if t in seen or t in self.obsolete:
                continue
            seen.add(t)
            stack.extend(self.children.get(t, []))
        return seen

    def ancestors(self, term: str) -> set[str]:
        cached = self._ancestor_cache.get(term)
        if cached is not None:
            return cached
        seen: set[str] = set()
        stack = list(self.parents.get(term, []))
        while stack:
            t = stack.pop()
            if t in seen:
                continue
            seen.add(t)
            stack.extend(self.parents.get(t, []))
        self._ancestor_cache[term] = seen
        return seen

    def tier(self, term: str) -> str:
        """Assign ONE heterogeneity tier to a descendant class.

        Precedence is deliberate and load-bearing, not incidental: infectious first (an
        infectious disease is never a genetic one, whatever else it carries), then
        SUSCEPTIBILITY **before** MENDELIAN, so that an OMIM ``{braces}`` risk locus which
        MONDO has nonetheless given a gene relation still counts as a risk locus rather than
        as a Mendelian disease -- the whole distinction this audit turns on. Gene-defined
        classes are therefore MENDELIAN only if they are not declared susceptibility
        classes, and the label-based ACQUIRED test runs last so that a gene-defined disease
        whose label happens to contain e.g. "diabetic" is not miscounted as acquired.
        """
        label = self.label.get(term, "")
        if term in self.infectious_agent or INFECTIOUS in self.ancestors(term):
            return "INFECTIOUS"
        if "predisposition" in self.subsets.get(term, ()) or SUSCEPTIBILITY_RE.search(label):
            return "SUSCEPTIBILITY"
        if self.germline_genes.get(term):
            return "MENDELIAN"
        if term in self.somatic:
            return "SOMATIC"
        if ACQUIRED_RE.search(label):
            return "ACQUIRED"
        if self.omim.get(term):
            # An OMIM phenotype MONDO could not attach a gene to: mapping key 2 (locus
            # mapped by linkage, gene unknown) or an unresolved susceptibility entry.
            return "UNMAPPED_LOCUS"
        return "UNSPECIFIED"


GENETIC_FORM_RE = re.compile(
    r"^(hereditary|familial|genetic|inherited|inborn|monogenic|syndromic|autosomal|x-linked|"
    r"congenital)\b", re.IGNORECASE)


def recipient_candidates(mondo: Mondo, term: str, minimum: int = 3) -> list[tuple[int, str, str]]:
    """Existing MONDO classes that could receive the OMIMPS mapping + the characteristic.

    The Mondo audit's recommended remedy is the ``hereditary.yaml`` pattern: mint a
    genetic-form child and move the mapping there. Often such a class ALREADY exists -- as a
    descendant ("syndromic craniosynostosis") or as a sibling ("inborn error of immunity").
    Returns (n gene-defined descendants, MONDO id, label), best first.
    """
    descs = mondo.descendants(term)
    label = mondo.label.get(term, "")
    # Content tokens of the class label: a candidate must be about the same entity, not
    # merely a "hereditary <something>" class reachable through the contaminated tree.
    generic = {"disease", "disorder", "syndrome", "failure", "primary", "chronic", "acute",
               "multiple", "inflammatory", "recurrent", "progressive", "congenita"}
    tokens = {w for w in re.findall(r"[a-z]{5,}", label.lower()) if w not in generic}

    def about_same_entity(cand_label: str) -> bool:
        low = cand_label.lower()
        hits = sum(1 for t in tokens if t in low)
        return hits >= 2 or (len(tokens) <= 2 and hits >= 1)

    # Siblings, EXCLUDING those reached through 'hereditary disease' itself (that parent is
    # the contamination under audit -- every hereditary class would look like a sibling).
    siblings = {s for p in mondo.parents.get(term, []) if p != HEREDITARY
                for s in mondo.children.get(p, [])} - {term}
    outside = {c for c, cl in mondo.label.items()
               if c not in descs and c != term
               and re.match(r"^(hereditary|familial|genetic|inherited)\b", cl, re.IGNORECASE)
               and about_same_entity(cl)}

    out = []
    for cand in sorted(set(descs) | siblings | outside):
        cl = mondo.label.get(cand, "")
        if cand in descs:
            if not GENETIC_FORM_RE.search(cl):
                continue
        elif not (GENETIC_FORM_RE.search(cl) and about_same_entity(cl)):
            continue
        n = sum(1 for x in mondo.descendants(cand) if mondo.germline_genes.get(x))
        if n >= minimum:
            out.append((n, cand, cl))
    return sorted(out, reverse=True)


def dismech_anchors() -> tuple[dict[str, set[str]], dict[str, set[str]], dict[str, set[str]]]:
    """Return (MONDO id -> disorder names, MONDO id -> grouping names, grouping -> members)."""
    disorders: dict[str, set[str]] = defaultdict(set)
    groupings: dict[str, set[str]] = defaultdict(set)
    grouping_members: dict[str, set[str]] = defaultdict(set)

    def mondo_ids_in(obj):
        if isinstance(obj, dict):
            term = obj.get("term")
            if isinstance(term, dict) and str(term.get("id", "")).startswith("MONDO:"):
                yield term["id"]
            for v in obj.values():
                yield from mondo_ids_in(v)
        elif isinstance(obj, list):
            for v in obj:
                yield from mondo_ids_in(v)

    for path in sorted(glob.glob(os.path.join(DISORDERS_DIR, "*.yaml"))):
        with open(path, encoding="utf-8") as fh:
            doc = safe_load(fh) or {}
        name = doc.get("name") or os.path.basename(path)[:-5]
        for block in (doc.get("disease_term"), doc.get("mappings"), doc.get("has_subtypes")):
            for mid in mondo_ids_in(block):
                disorders[mid].add(name)
    for path in sorted(glob.glob(os.path.join(GROUPINGS_DIR, "*.yaml"))):
        with open(path, encoding="utf-8") as fh:
            doc = safe_load(fh) or {}
        name = doc.get("name") or os.path.basename(path)[:-5]
        for mid in mondo_ids_in(doc.get("mappings")):
            groupings[mid].add(name)
        for member in doc.get("members") or []:
            if isinstance(member, dict) and member.get("member"):
                grouping_members[name].add(member["member"])
    return disorders, groupings, grouping_members


def heterogeneity_axes(counts: dict[str, int], n_predisposers: int) -> list[str]:
    """Which kinds of member the class actually mixes -- the ticket's question (b)."""
    axes = []
    if counts["MENDELIAN"]:
        axes.append("MENDELIAN")
    if counts["SUSCEPTIBILITY"] or counts["UNMAPPED_LOCUS"] or n_predisposers:
        axes.append("RISK_LOCUS")
    if counts["INFECTIOUS"] or counts["ACQUIRED"] or counts["SOMATIC"]:
        axes.append("ACQUIRED")
    return axes


def series_kind(counts: dict[str, int], n_predisposers: int) -> str:
    genetic = counts["MENDELIAN"]
    acquired = counts["INFECTIOUS"] + counts["ACQUIRED"] + counts["SOMATIC"]
    # High-confidence risk-locus members: OMIM {braces} entries, sitting either inside the
    # tree (predisposition subset / "susceptibility to" label) or, where MONDO has already
    # excluded them from it, outside it as predisposers.
    declared_susc = counts["SUSCEPTIBILITY"] + n_predisposers
    unmapped = counts["UNMAPPED_LOCUS"]
    if declared_susc >= 2 and declared_susc >= genetic:
        return "SUSCEPTIBILITY_SERIES"
    if unmapped >= 3 and unmapped > genetic:
        return "LOCUS_SERIES"
    if genetic >= 2 and acquired:
        return "MIXED_GENETIC_ACQUIRED"
    if genetic >= 2:
        return "MENDELIAN_SERIES"
    return "SPARSE"


def analyse(mondo: Mondo, term: str, disorders, groupings, grouping_members) -> dict:
    descs = mondo.descendants(term)
    counts = {t: 0 for t in TIERS}
    tiers: dict[str, str] = {}
    for d in descs:
        t = mondo.tier(d)
        tiers[d] = t
        counts[t] += 1
    covered = {d: sorted(disorders[d]) for d in descs if d in disorders}
    genetic_covered = {d: v for d, v in covered.items() if tiers[d] == "MENDELIAN"}
    # Distinct dismech ENTRIES, not distinct MONDO ids: one entry can anchor several ids
    # through has_subtypes, and a one-entry "series" is a subtype catalog, not a grouping.
    genetic_entries = {n for v in genetic_covered.values() for n in v}
    # Is some existing dismech grouping already collecting these entries?
    overlaps = sorted(
        ((len(genetic_entries & mem), g) for g, mem in grouping_members.items()
         if genetic_entries & mem), reverse=True)
    predisposers = [p for p in mondo.predisposers.get(term, []) if p not in mondo.obsolete]
    return {
        "id": term,
        "label": mondo.label.get(term, "?"),
        "omimps": ",".join(mondo.omimps.get(term, [])),
        "descendants": len(descs),
        "counts": counts,
        "predisposers": predisposers,
        "axes": heterogeneity_axes(counts, len(predisposers)),
        "kind": series_kind(counts, len(predisposers)),
        "self_entry": sorted(disorders.get(term, [])),
        "self_grouping": sorted(groupings.get(term, [])),
        "covered": covered,
        "genetic_covered": genetic_covered,
        "genetic_entries": sorted(genetic_entries),
        "grouping_overlap": overlaps[:2],
        "recipients": recipient_candidates(mondo, term),
        "inherited_superclasses": sorted(
            mondo.ancestors(term) & mondo.inherited_equivalents,
            key=lambda x: mondo.label.get(x, "")),
        "tiers": tiers,
    }


def recommend(row: dict) -> str:
    """dismech-side disposition (not a Mondo edit recommendation)."""
    kind, n_gen = row["kind"], len(row["genetic_entries"])
    if row["self_grouping"]:
        return "GROUPING_EXISTS"
    # Members already collected by an existing dismech grouping: no new grouping needed.
    if row["grouping_overlap"] and row["grouping_overlap"][0][0] >= max(2, n_gen // 2):
        return "COVERED_BY_GROUPING"
    if kind in ("SUSCEPTIBILITY_SERIES", "LOCUS_SERIES") and n_gen < 3:
        return "SINGLE_DISEASE"
    if n_gen >= 3:
        return "GROUPING_CANDIDATE"
    if n_gen >= 1:
        return "GROUPING_DEFERRED"
    return "NO_DISMECH_BASIS"


def ensure_obo(path: str | None) -> str:
    if path and os.path.exists(path):
        return path
    dest = path or os.path.join(ROOT, ".cache", "mondo.obo")
    os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
    if not os.path.exists(dest):
        sys.stderr.write(f"downloading {MONDO_URL} -> {dest}\n")
        urllib.request.urlretrieve(MONDO_URL, dest)
    return dest


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--obo", help="path to mondo.obo (downloaded to .cache/mondo.obo if absent)")
    ap.add_argument("--focus", choices=["audit", "all"], default="audit",
                    help="'audit': the 42 flagged broad classes; 'all': every OMIMPS-equivalent class")
    ap.add_argument("--tsv", help="write the per-class table here")
    ap.add_argument("--detail", help="print the full descendant breakdown for one MONDO id")
    args = ap.parse_args()

    mondo = Mondo(ensure_obo(args.obo))
    disorders, groupings, grouping_members = dismech_anchors()

    if args.detail:
        row = analyse(mondo, args.detail, disorders, groupings, grouping_members)
        print(f"# {row['label']} ({row['id']}) {row['omimps']}  kind={row['kind']}")
        for d in sorted(row["tiers"], key=lambda x: (row["tiers"][x], mondo.label.get(x, ""))):
            mark = "*" if d in row["covered"] else " "
            print(f"{mark} {row['tiers'][d]:<15} {d:<16} {mondo.label.get(d, '?')}")
        for p in sorted(row["predisposers"], key=lambda x: mondo.label.get(x, "")):
            print(f"  {'PREDISPOSES_TO':<15} {p:<16} {mondo.label.get(p, '?')}")
        print("(* = has a dismech kb/disorders entry)")
        for n, cid, cl in row["recipients"]:
            print(f"  recipient candidate: {cid} {cl} ({n} gene-defined descendants)")
        for n, g in row["grouping_overlap"]:
            print(f"  existing dismech grouping: {g} shares {n} member entries")
        return

    if args.focus == "all":
        terms = sorted({t for t in mondo.omimps if mondo.omimps[t]},
                       key=lambda t: -len(mondo.descendants(t)))
    else:
        terms = AUDIT_CLASSES

    rows = [analyse(mondo, t, disorders, groupings, grouping_members) for t in terms]
    for r in rows:
        r["recommendation"] = recommend(r)

    header = ["mondo_id", "label", "omimps", "descendants", *[t.lower() for t in TIERS],
              "predisposers", "series_kind", "heterogeneity_axes",
              "dismech_entry_on_class", "dismech_grouping",
              "inherited_superclasses", "dismech_covered", "dismech_member_entries",
              "existing_grouping_overlap", "mondo_recipient_candidate", "recommendation",
              "member_entry_names"]
    lines = ["\t".join(header)]
    for r in rows:
        lines.append("\t".join([
            r["id"], r["label"], r["omimps"], str(r["descendants"]),
            *[str(r["counts"][t]) for t in TIERS], str(len(r["predisposers"])),
            r["kind"], "+".join(r["axes"]),
            ";".join(r["self_entry"]), ";".join(r["self_grouping"]),
            "; ".join(mondo.label.get(x, x) for x in r["inherited_superclasses"]),
            str(len(r["covered"])), str(len(r["genetic_entries"])),
            "; ".join(f"{g} ({n})" for n, g in r["grouping_overlap"]),
            "; ".join(f"{cid} {cl}" for _, cid, cl in r["recipients"][:2]),
            r["recommendation"], "; ".join(r["genetic_entries"])[:400],
        ]))
    out = "\n".join(lines)
    if args.tsv:
        with open(args.tsv, "w", encoding="utf-8") as fh:
            fh.write(out + "\n")
        sys.stderr.write(f"wrote {args.tsv} ({len(rows)} classes)\n")
    else:
        print(out)


if __name__ == "__main__":
    main()
