#!/usr/bin/env python3
"""Audit how dismech represents antigens on B and T cells.

Background
----------
The schema has no antigen concept at all: ``antigen`` does not appear once in
``src/dismech/schema/dismech.yaml``. Antigen identity — the thing an autoantibody
binds, the peptide a TCR sees, the lineage marker a therapy depletes — is
therefore carried entirely in free text, scattered across ``biochemical[].name``,
pathophysiology node names and descriptions, ``genetic[].association`` strings,
and evidence prose.

This script quantifies that. It answers four questions per entry, one for each
sense in which "B and T cells have different antigens":

1. **Autoantigen identity** — is a specific self-antigen named anywhere, and in
   which slot?
2. **Lymphocyte attribution** — is that antigen attached to a B-lineage or a
   T-lineage cell, or is the lineage unrecoverable from structure?
3. **HLA restriction** — is the presenting allele recorded, and structurally?
4. **Surface/lineage markers** — where do CD19/CD20/CD3/CD4/CD8 live?

Nothing here is a gate. It is a census: run it, read the numbers, decide whether
a schema change is worth it.

Usage
-----
    uv run python scripts/immune_antigen_audit.py                 # summary
    uv run python scripts/immune_antigen_audit.py --format tsv --out /tmp/a.tsv
    uv run python scripts/immune_antigen_audit.py --format list --cohort autoantigen
    uv run python scripts/immune_antigen_audit.py --entry Celiac_Disease
"""

from __future__ import annotations

import argparse
import collections
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from dismech.yaml_io import safe_load_path

REPO = Path(__file__).resolve().parents[1]

# --------------------------------------------------------------------------
# Lineage vocabularies.
#
# Matched on the curated CL label (and on preferred_term as a fallback), not on
# CURIE, because the KB binds a long tail of CL terms and new ones arrive with
# every immunology entry. Substring matching on the label is what keeps this
# from going stale silently.
# --------------------------------------------------------------------------
B_LINEAGE = (
    "b cell",
    "b-cell",
    "plasma cell",
    "plasmablast",
    "plasmacyte",
    "germinal center b",
    "germinal centre b",
    "memory b",
    "follicular b",
    "marginal zone b",
    "pro-b",
    "pre-b",
    "immature b",
)
T_LINEAGE = (
    "t cell",
    "t-cell",
    "thymocyte",
    "cd4-positive",
    "cd8-positive",
    "t follicular helper",
    "t helper",
    "regulatory t",
    "th1",
    "th2",
    "th17",
    "cytotoxic t",
    "gamma-delta",
)
# Antigen-presenting cells matter for the T-cell side of the question: an
# antigen named on a dendritic-cell node is a presented antigen even when no T
# cell is listed on that node.
APC_LINEAGE = (
    "dendritic cell",
    "macrophage",
    "langerhans",
    "antigen presenting",
    "antigen-presenting",
    "microglial cell",
    "kupffer",
)

# --------------------------------------------------------------------------
# Antigen-naming patterns.
#
# Deliberately generous — the point is to find every place an antigen is
# *named*, precisely because none of those places is a structured slot.
# --------------------------------------------------------------------------
ANTIGEN_PATTERNS = [
    ("anti_x_antibody", re.compile(r"\banti[-‐-―\s]([A-Za-z0-9][\w\-α-ω./()' ]{1,40}?)\s*(?:auto)?antibod", re.IGNORECASE)),
    ("anti_x_bare", re.compile(r"\banti[-‐-―]([A-Z][A-Za-z0-9\-]{1,20})\b")),
    ("autoantigen", re.compile(r"\bauto[-\s]?antigen\b", re.IGNORECASE)),
    ("epitope", re.compile(r"\bepitopes?\b", re.IGNORECASE)),
    ("epitope_spreading", re.compile(r"\bepitope spreading\b", re.IGNORECASE)),
    ("neoantigen", re.compile(r"\bneo[-\s]?antigens?\b", re.IGNORECASE)),
    ("superantigen", re.compile(r"\bsuper[-\s]?antigens?\b", re.IGNORECASE)),
    ("antigen_presentation", re.compile(r"\bantigen[- ]present", re.IGNORECASE)),
    ("antigen_generic", re.compile(r"\bantigens?\b", re.IGNORECASE)),
    ("molecular_mimicry", re.compile(r"\bmolecular mimicry\b", re.IGNORECASE)),
    ("citrullination", re.compile(r"\bcitrullinat", re.IGNORECASE)),
    ("deamidation", re.compile(r"\bdeamidat", re.IGNORECASE)),
]

# Slots whose objects describe a therapy, so an "anti-X" there names a drug
# target rather than an autoantigen.
THERAPEUTIC_SLOTS = frozenset({"treatments", "clinical_trials"})

# Only these classes own `cell_types` in the schema, so only their instances can
# name the lymphocyte that sees an antigen. An evidence item or a treatment has
# no such slot: "no cell_types" there is structurally impossible, not a curation
# gap, and counting it as one inflates the unattributed rate.
#
# Matched on path, because iter_objects walks raw mappings with no class
# information. The match must end at the list index: an object is an instance of
# one of these classes only when the path's *last* segment is a member of that
# slot's list. `pathophysiology[0].downstream[1]` is a CausalLink and
# `pathophysiology[0].evidence[2]` an EvidenceItem, neither of which owns
# `cell_types`; treating the whole subtree as eligible would add 907 such nested
# objects and turn 64% into 88%.
#
# The prefix is deliberately unanchored so nesting is followed wherever the
# schema puts these slots -- `stages[0].pathophysiology[1]` is as much a
# Pathophysiology as a top-level one. Each of these three slot names has exactly
# one range in the schema and no class overrides it, so the suffix alone
# identifies the class.
CELL_TYPE_BEARING_PATH = re.compile(
    r"(?:^|\.)(pathophysiology|biochemical|experimental_models)\[\d+\]$"
)

# An HLA genetic row can only bind a gene_term when its name IS an HGNC gene
# symbol. A serotype (HLA-DQ2, HLA-B27), an allele (HLA-DRB1*03:01) or a
# haplotype (HLA-DR3-DQ2) names something no single gene identifies, so leaving
# it unbound is the correct call, not backlog.
HLA_GENE_SYMBOL_RE = re.compile(
    r"^HLA-(A|B|C|E|F|G|DRA|DRB[1-5]|DQA[12]|DQB[12]|DPA1|DPB1)$", re.IGNORECASE
)

HLA_RE = re.compile(r"\bHLA[-‐-―]?[A-Z]{1,3}\d?\b|\bMHC class [I]{1,2}\b|\bH2-[A-Z]", re.IGNORECASE)
# Fields that carry a curated identity (and so can hold an ontology label),
# as opposed to narrative prose.
LABEL_FIELDS = frozenset({"preferred_term", "label", "name"})

CD_MARKER_RE = re.compile(r"\bCD(?:19|20|3|4|8|21|22|27|38|138|79[ab])\b")

# Slots we report separately because they are the plausible homes for a future
# structured antigen field.
INTERESTING_SLOTS = (
    "biochemical",
    "pathophysiology",
    "genetic",
    "phenotypes",
    "treatments",
    "histopathology",
    "definitions",
    "environmental",
    "discussions",
    "mechanistic_hypotheses",
    "description",
    "notes",
)


def ranked(counter, limit=None):
    """`Counter.most_common`, with ties broken by key so runs are reproducible.

    Several counters here are fed from sets, whose iteration order varies with
    PYTHONHASHSEED. `most_common` preserves that order for equal counts, so the
    same tree produced differently-ordered output run to run.
    """
    items = sorted(counter.items(), key=lambda kv: (-kv[1], str(kv[0])))
    return items[:limit] if limit else items


def is_immune_entry(doc: dict, text: str) -> tuple[bool, str]:
    """Classify an entry into the immune cohort, recording *why*.

    Three tiers, most-structured first, so the report can say how much of the
    cohort is identifiable from curated structure versus only from prose.
    """
    cls = doc.get("classifications") or {}
    for row in cls.get("harrisons_chapter") or []:
        if isinstance(row, dict) and row.get("classification_value") == "IMMUNE_RHEUMATOLOGIC":
            return True, "classification"
    for key in ("iuis_immunodeficiency", "icimd"):
        if cls.get(key):
            return True, "classification"
    if re.search(r"\bauto[-\s]?immun|\bautoantibod|\bautoantigen", text, re.IGNORECASE):
        return True, "autoimmune_prose"
    if re.search(r"\bimmunodeficien|\bimmune[- ]mediated|\bhypersensitivit|\bvasculit", text, re.IGNORECASE):
        return True, "immune_prose"
    return False, ""


def iter_objects(node, path=""):
    """Yield ``(path, dict)`` for every mapping in the document."""
    if isinstance(node, dict):
        yield path, node
        for k, v in node.items():
            yield from iter_objects(v, f"{path}.{k}" if path else k)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from iter_objects(v, f"{path}[{i}]")


def lineage_of(obj: dict) -> set[str]:
    """B/T/APC lineages named by this object's own cell-type slots.

    Reads ``affected_cell_types`` (``FunctionalEffect``) as well as
    ``cell_types``: both record a lineage, and ignoring one undercounts.
    """
    out = set()
    for ct in (obj.get("cell_types") or []) + (obj.get("affected_cell_types") or []):
        if not isinstance(ct, dict):
            continue
        label = ((ct.get("term") or {}).get("label") or "") + " " + (ct.get("preferred_term") or "")
        low = label.lower()
        if any(w in low for w in B_LINEAGE):
            out.add("B")
        if any(w in low for w in T_LINEAGE):
            out.add("T")
        if any(w in low for w in APC_LINEAGE):
            out.add("APC")
    return out


def local_text(obj: dict) -> str:
    """Scalar text belonging to this object, excluding nested structures."""
    parts = []
    for v in obj.values():
        if isinstance(v, str):
            parts.append(v)
    return " ".join(parts)


def top_slot(path: str) -> str:
    return path.split(".")[0].split("[")[0] if path else "<root>"


def audit_entry(path: Path) -> dict | None:
    try:
        doc = safe_load_path(path)
    except Exception as exc:  # a malformed file is another audit's problem
        print(f"# skipped {path.name}: {exc}", file=sys.stderr)
        return None
    if not isinstance(doc, dict):
        return None
    raw = path.read_text(encoding="utf-8")
    immune, why = is_immune_entry(doc, raw)

    rec = {
        "file": path.name,
        "name": doc.get("name") or path.stem,
        "immune": immune,
        "cohort_reason": why,
        "antigen_hits": collections.Counter(),
        "antigen_slots": collections.Counter(),
        "named_antigens": set(),
        "named_therapeutic_targets": set(),
        # objects that name an antigen, split by whether their own cell-type
        # slot says which lymphocyte sees it
        "antigen_obj_total": 0,
        "antigen_obj_with_B": 0,
        "antigen_obj_with_T": 0,
        "antigen_obj_with_APC": 0,
        # no lineage, separated by *why*: the slot is empty/absent, or it is
        # populated with a cell that is simply not a lymphocyte
        "antigen_obj_no_cell_types": 0,
        "antigen_obj_cell_types_non_lymphoid": 0,
        # the honest denominator: objects whose class can own a cell-type slot
        "antigen_obj_eligible": 0,
        "antigen_obj_eligible_with_lineage": 0,
        "antigen_obj_eligible_without_lineage": 0,
        "b_nodes": 0,
        "t_nodes": 0,
        "bt_same_node": 0,
        "hla_mentions": 0,
        "hla_structured": False,
        "cd_markers": collections.Counter(),
        "cd_slots": collections.Counter(),
        # CD4/CD8 exist as CL labels ("CD8-positive, alpha-beta T cell") while
        # CD19/CD20/CD3 do not, so where a marker is written says whether it is
        # queryable or just prose.
        "cd_in_label": collections.Counter(),
        "cd_in_prose": collections.Counter(),
        "autoantibody_biomarkers": 0,
        "autoantibody_biomarkers_bound": 0,
        # An unbound HLA row is not automatically a gap. A serotype or haplotype
        # label (HLA-DQ2, HLA-DR3) has no single HGNC gene to bind, and entries
        # that worked this out say so in `notes`. Counting those as backlog
        # would invite a backfill over a considered decision.
        "hla_rows": 0,
        "hla_rows_bound": 0,
        "hla_rows_unbound_explained": 0,
        "hla_rows_unbound_unexplained": 0,
        "hla_rows_unbound_gene_symbol": 0,
        "hla_rows_unbound_not_a_gene": 0,
    }

    for label, pat in ANTIGEN_PATTERNS:
        n = len(pat.findall(raw))
        if n:
            rec["antigen_hits"][label] = n

    rec["hla_mentions"] = len(HLA_RE.findall(raw))

    for opath, obj in iter_objects(doc):
        text = local_text(obj)
        slot = top_slot(opath)

        bucket = ("named_therapeutic_targets" if slot in THERAPEUTIC_SLOTS
                  else "named_antigens")
        for m in ANTIGEN_PATTERNS[0][1].finditer(text):
            rec[bucket].add(m.group(1).strip().rstrip(".,;"))
        for m in ANTIGEN_PATTERNS[1][1].finditer(text):
            rec[bucket].add(m.group(1).strip())

        if any(pat.search(text) for _, pat in ANTIGEN_PATTERNS):
            rec["antigen_slots"][slot] += 1
            rec["antigen_obj_total"] += 1
            lin = lineage_of(obj)
            if "B" in lin:
                rec["antigen_obj_with_B"] += 1
            if "T" in lin:
                rec["antigen_obj_with_T"] += 1
            if "APC" in lin:
                rec["antigen_obj_with_APC"] += 1
            if not lin:
                if obj.get("cell_types") or obj.get("affected_cell_types"):
                    rec["antigen_obj_cell_types_non_lymphoid"] += 1
                else:
                    rec["antigen_obj_no_cell_types"] += 1
            if CELL_TYPE_BEARING_PATH.search(opath):
                rec["antigen_obj_eligible"] += 1
                key = ("antigen_obj_eligible_with_lineage" if lin
                       else "antigen_obj_eligible_without_lineage")
                rec[key] += 1

        if slot == "pathophysiology":
            lin = lineage_of(obj)
            if "B" in lin:
                rec["b_nodes"] += 1
            if "T" in lin:
                rec["t_nodes"] += 1
            if {"B", "T"} <= lin:
                rec["bt_same_node"] += 1

        for cd in CD_MARKER_RE.findall(text):
            rec["cd_markers"][cd] += 1
            rec["cd_slots"][slot] += 1
        for field, value in obj.items():
            if not isinstance(value, str):
                continue
            where = "cd_in_label" if field in LABEL_FIELDS else "cd_in_prose"
            for cd in CD_MARKER_RE.findall(value):
                rec[where][cd] += 1

        # HLA recorded as a real gene binding rather than as prose
        gt = obj.get("gene_term") or (obj if obj.get("term") and "gene" in opath else None)
        if isinstance(gt, dict):
            lab = ((gt.get("term") or {}).get("label") or "") + " " + (gt.get("preferred_term") or "")
            if lab.upper().startswith("HLA"):
                rec["hla_structured"] = True

    for g in doc.get("genetic") or []:
        if not isinstance(g, dict) or "HLA" not in (g.get("name") or "").upper():
            continue
        rec["hla_rows"] += 1
        if g.get("gene_term"):
            rec["hla_rows_bound"] += 1
            continue
        # unbound: record both whether the name *could* bind a gene, and whether
        # the curator wrote down why it does not
        bindable = HLA_GENE_SYMBOL_RE.match((g.get("name") or "").strip())
        rec["hla_rows_unbound_gene_symbol" if bindable
            else "hla_rows_unbound_not_a_gene"] += 1
        explained = re.search(
            r"serotype|haplotype|not a single|not by a single|HGNC-resolvable",
            str(g.get("notes") or ""), re.IGNORECASE)
        rec["hla_rows_unbound_explained" if explained
            else "hla_rows_unbound_unexplained"] += 1

    for b in doc.get("biochemical") or []:
        if not isinstance(b, dict):
            continue
        nm = b.get("name") or ""
        if re.search(r"\banti[-\s]|antibod|immunoglobulin", nm, re.IGNORECASE):
            rec["autoantibody_biomarkers"] += 1
            if b.get("biomarker_term"):
                rec["autoantibody_biomarkers_bound"] += 1

    return rec


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--format", choices=("summary", "tsv", "list"), default="summary")
    ap.add_argument("--cohort", choices=("immune", "autoantigen", "all"), default="immune")
    ap.add_argument("--entry", help="audit one entry by file stem")
    ap.add_argument("--out", type=Path)
    ap.add_argument("--paths", nargs="*", default=["kb/disorders", "kb/modules"])
    args = ap.parse_args()

    files: list[Path] = []
    for p in args.paths:
        files.extend(sorted((REPO / p).glob("*.yaml")))
    if args.entry:
        files = [f for f in files if f.stem == args.entry]
        if not files:
            print(f"no entry named {args.entry}", file=sys.stderr)
            return 1

    recs = [r for r in (audit_entry(f) for f in files) if r]
    immune = [r for r in recs if r["immune"]]
    antigen = [r for r in immune if r["antigen_obj_total"]]

    cohort = {"immune": immune, "autoantigen": antigen, "all": recs}[args.cohort]

    lines: list[str] = []
    w = lines.append

    if args.format == "list":
        for r in sorted(cohort, key=lambda r: -r["antigen_obj_total"]):
            w(f"{r['antigen_obj_total']:4d}  B={r['antigen_obj_with_B']:<3d} T={r['antigen_obj_with_T']:<3d} "
              f"none={r['antigen_obj_no_cell_types'] + r['antigen_obj_cell_types_non_lymphoid']:<3d}  {r['file']}")
    elif args.format == "tsv":
        cols = ["file", "name", "cohort_reason", "antigen_obj_total", "antigen_obj_with_B",
                "antigen_obj_with_T", "antigen_obj_with_APC",
                "antigen_obj_no_cell_types", "antigen_obj_cell_types_non_lymphoid",
                "antigen_obj_eligible", "antigen_obj_eligible_with_lineage",
                "antigen_obj_eligible_without_lineage",
                "b_nodes", "t_nodes", "bt_same_node", "hla_mentions", "hla_structured",
                "hla_rows", "hla_rows_bound", "hla_rows_unbound_explained",
                "hla_rows_unbound_unexplained", "hla_rows_unbound_gene_symbol",
                "hla_rows_unbound_not_a_gene",
                "autoantibody_biomarkers", "autoantibody_biomarkers_bound"]
        w("\t".join(cols))
        for r in sorted(cohort, key=lambda r: -r["antigen_obj_total"]):
            w("\t".join(str(r[c]) for c in cols))
    else:
        tot_slots = collections.Counter()
        tot_hits = collections.Counter()
        tot_cd = collections.Counter()
        tot_cd_slots = collections.Counter()
        tot_cd_label = collections.Counter()
        tot_cd_prose = collections.Counter()
        reasons = collections.Counter()
        names = collections.Counter()
        drug_targets = collections.Counter()
        agg = collections.Counter()
        for r in cohort:
            reasons[r["cohort_reason"]] += 1
            tot_slots.update(r["antigen_slots"])
            tot_hits.update(r["antigen_hits"])
            tot_cd.update(r["cd_markers"])
            tot_cd_slots.update(r["cd_slots"])
            tot_cd_label.update(r["cd_in_label"])
            tot_cd_prose.update(r["cd_in_prose"])
            for n in r["named_antigens"]:
                names[n] += 1
            for n in r["named_therapeutic_targets"]:
                drug_targets[n] += 1
            for k in ("antigen_obj_total", "antigen_obj_with_B", "antigen_obj_with_T",
                      "antigen_obj_with_APC", "antigen_obj_no_cell_types",
                      "antigen_obj_cell_types_non_lymphoid", "antigen_obj_eligible",
                      "antigen_obj_eligible_with_lineage",
                      "antigen_obj_eligible_without_lineage", "b_nodes",
                      "t_nodes", "bt_same_node", "hla_mentions",
                      "hla_rows", "hla_rows_bound", "hla_rows_unbound_explained",
                      "hla_rows_unbound_unexplained", "hla_rows_unbound_gene_symbol",
                      "hla_rows_unbound_not_a_gene",
                      "autoantibody_biomarkers", "autoantibody_biomarkers_bound"):
                agg[k] += r[k]

        w(f"entries scanned              {len(recs)}")
        w(f"immune cohort                {len(immune)}")
        if args.cohort != "immune":
            w(f"AGGREGATING OVER --cohort {args.cohort} ({len(cohort)} entries)")
        for k, v in ranked(reasons):
            w(f"    via {k:<22} {v}")
        w(f"immune entries naming an antigen  {len(antigen)}"
          f"  ({100*len(antigen)/max(1,len(immune)):.0f}% of cohort)")
        w("")
        w("-- where antigen text lives (objects, immune cohort) --")
        for k, v in ranked(tot_slots, 15):
            w(f"    {k:<28} {v}")
        w("")
        w("-- antigen pattern frequency (raw matches) --")
        for k, v in ranked(tot_hits):
            w(f"    {k:<28} {v}")
        w("")
        w("-- lymphocyte attribution of antigen-naming objects --")
        t = agg["antigen_obj_total"] or 1
        w(f"    objects naming an antigen   {agg['antigen_obj_total']}")
        w(f"    ... with a B-lineage cell   {agg['antigen_obj_with_B']} ({100*agg['antigen_obj_with_B']/t:.1f}%)")
        w(f"    ... with a T-lineage cell   {agg['antigen_obj_with_T']} ({100*agg['antigen_obj_with_T']/t:.1f}%)")
        w(f"    ... with an APC             {agg['antigen_obj_with_APC']} ({100*agg['antigen_obj_with_APC']/t:.1f}%)")
        no_lin = agg["antigen_obj_no_cell_types"] + agg["antigen_obj_cell_types_non_lymphoid"]
        w(f"    ... no B/T/APC lineage      {no_lin} ({100*no_lin/t:.1f}%)")
        w(f"        cell-type slot empty      {agg['antigen_obj_no_cell_types']}")
        w(f"        slot set, non-lymphoid    {agg['antigen_obj_cell_types_non_lymphoid']}")
        w("")
        w("-- attribution over objects whose class CAN own a cell-type slot --")
        w("   (only Pathophysiology, Biochemical and ExperimentalModel do; for every")
        w("    other class 'no cell_types' is structurally impossible, not a gap)")
        e = agg["antigen_obj_eligible"] or 1
        w(f"    eligible objects            {agg['antigen_obj_eligible']}")
        w(f"    ... naming a B/T/APC lineage {agg['antigen_obj_eligible_with_lineage']}"
          f" ({100*agg['antigen_obj_eligible_with_lineage']/e:.1f}%)")
        w(f"    ... not                     {agg['antigen_obj_eligible_without_lineage']}"
          f" ({100*agg['antigen_obj_eligible_without_lineage']/e:.1f}%)")
        ineligible = agg["antigen_obj_total"] - agg["antigen_obj_eligible"]
        w(f"    ineligible (no such slot)   {ineligible} ({100*ineligible/t:.1f}%)")
        w("")
        w("-- pathophysiology nodes by lineage --")
        w(f"    nodes with a B-lineage cell {agg['b_nodes']}")
        w(f"    nodes with a T-lineage cell {agg['t_nodes']}")
        w(f"    nodes carrying both         {agg['bt_same_node']}")
        w("")
        w("-- HLA --")
        w(f"    prose mentions              {agg['hla_mentions']}")
        w(f"    entries with an HLA gene_term binding  {sum(1 for r in cohort if r['hla_structured'])}")
        w(f"    genetic rows naming HLA     {agg['hla_rows']}")
        w(f"        bound to a gene_term      {agg['hla_rows_bound']}")
        w(f"        unbound, notes explain    {agg['hla_rows_unbound_explained']}")
        w(f"        unbound, unexplained      {agg['hla_rows_unbound_unexplained']}")
        w("    of the unbound rows, the name is:")
        w(f"        an HGNC gene symbol       {agg['hla_rows_unbound_gene_symbol']}  (bindable)")
        w(f"        a serotype/allele/region  {agg['hla_rows_unbound_not_a_gene']}  (no single gene to bind)")
        w("")
        w("-- autoantibody biomarkers --")
        w(f"    biochemical antibody rows   {agg['autoantibody_biomarkers']}")
        w(f"    ... with a biomarker_term   {agg['autoantibody_biomarkers_bound']}")
        w("")
        w("-- surface/lineage markers (CD) --")
        w("    marker        total   in name/preferred_term/label      in prose")
        for k, v in ranked(tot_cd):
            lab, pro = tot_cd_label[k], tot_cd_prose[k]
            tot_lp = lab + pro or 1
            w(f"    {k:<10} {v:>7}   {lab:>10} ({100*lab/tot_lp:>4.1f}%)   {pro:>13}")
        w("    slots:")
        for k, v in ranked(tot_cd_slots, 8):
            w(f"        {k:<24} {v}")
        w("")
        w("-- most-named antigens outside treatments (free text, uncontrolled) --")
        for k, v in ranked(names, 30):
            w(f"    {v:3d}  {k}")
        w("")
        w("-- 'anti-X' targets named inside treatments/clinical_trials --")
        w("   (drug targets, not autoantigens; the YAML gives no way to tell them apart)")
        for k, v in ranked(drug_targets, 15):
            w(f"    {v:3d}  {k}")

    out = "\n".join(lines)
    if args.out:
        args.out.write_text(out + "\n", encoding="utf-8")
        print(f"wrote {args.out}")
    else:
        print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
