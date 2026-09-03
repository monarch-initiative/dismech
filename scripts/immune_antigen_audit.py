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

from dismech.yaml_io import safe_load_path  # noqa: E402

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
    ("anti_x_antibody", re.compile(r"\banti[-‐-―\s]([A-Za-z0-9][\w\-α-ω./()' ]{1,40}?)\s*(?:auto)?antibod", re.I)),
    ("anti_x_bare", re.compile(r"\banti[-‐-―]([A-Z][A-Za-z0-9\-]{1,20})\b")),
    ("autoantigen", re.compile(r"\bauto[-\s]?antigen\b", re.I)),
    ("epitope", re.compile(r"\bepitopes?\b", re.I)),
    ("epitope_spreading", re.compile(r"\bepitope spreading\b", re.I)),
    ("neoantigen", re.compile(r"\bneo[-\s]?antigens?\b", re.I)),
    ("superantigen", re.compile(r"\bsuper[-\s]?antigens?\b", re.I)),
    ("antigen_presentation", re.compile(r"\bantigen[- ]present", re.I)),
    ("antigen_generic", re.compile(r"\bantigens?\b", re.I)),
    ("molecular_mimicry", re.compile(r"\bmolecular mimicry\b", re.I)),
    ("citrullination", re.compile(r"\bcitrullinat", re.I)),
    ("deamidation", re.compile(r"\bdeamidat", re.I)),
]

HLA_RE = re.compile(r"\bHLA[-‐-―]?[A-Z]{1,3}\d?\b|\bMHC class [I]{1,2}\b|\bH2-[A-Z]", re.I)
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
    if re.search(r"\bauto[-\s]?immun|\bautoantibod|\bautoantigen", text, re.I):
        return True, "autoimmune_prose"
    if re.search(r"\bimmunodeficien|\bimmune[- ]mediated|\bhypersensitivit|\bvasculit", text, re.I):
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
    """B/T/APC lineages named by this object's own ``cell_types``."""
    out = set()
    for ct in obj.get("cell_types") or []:
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
    for k, v in obj.items():
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
        # objects that name an antigen, split by whether their own cell_types
        # say which lymphocyte sees it
        "antigen_obj_total": 0,
        "antigen_obj_with_B": 0,
        "antigen_obj_with_T": 0,
        "antigen_obj_with_APC": 0,
        "antigen_obj_unattributed": 0,
        "b_nodes": 0,
        "t_nodes": 0,
        "bt_same_node": 0,
        "hla_mentions": 0,
        "hla_structured": False,
        "cd_markers": collections.Counter(),
        "cd_slots": collections.Counter(),
        "autoantibody_biomarkers": 0,
        "autoantibody_biomarkers_bound": 0,
    }

    for label, pat in ANTIGEN_PATTERNS:
        n = len(pat.findall(raw))
        if n:
            rec["antigen_hits"][label] = n

    THERAPEUTIC_SLOTS = {"treatments", "clinical_trials"}

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
                rec["antigen_obj_unattributed"] += 1

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

        # HLA recorded as a real gene binding rather than as prose
        gt = obj.get("gene_term") or (obj if obj.get("term") and "gene" in opath else None)
        if isinstance(gt, dict):
            lab = ((gt.get("term") or {}).get("label") or "") + (gt.get("preferred_term") or "")
            if lab.upper().startswith("HLA"):
                rec["hla_structured"] = True

    for b in doc.get("biochemical") or []:
        if not isinstance(b, dict):
            continue
        nm = b.get("name") or ""
        if re.search(r"\banti[-\s]|antibod|immunoglobulin", nm, re.I):
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
              f"none={r['antigen_obj_unattributed']:<3d}  {r['file']}")
    elif args.format == "tsv":
        cols = ["file", "name", "cohort_reason", "antigen_obj_total", "antigen_obj_with_B",
                "antigen_obj_with_T", "antigen_obj_with_APC", "antigen_obj_unattributed",
                "b_nodes", "t_nodes", "bt_same_node", "hla_mentions", "hla_structured",
                "autoantibody_biomarkers", "autoantibody_biomarkers_bound"]
        w("\t".join(cols))
        for r in sorted(cohort, key=lambda r: -r["antigen_obj_total"]):
            w("\t".join(str(r[c]) for c in cols))
    else:
        tot_slots = collections.Counter()
        tot_hits = collections.Counter()
        tot_cd = collections.Counter()
        tot_cd_slots = collections.Counter()
        reasons = collections.Counter()
        names = collections.Counter()
        drug_targets = collections.Counter()
        agg = collections.Counter()
        for r in immune:
            reasons[r["cohort_reason"]] += 1
            tot_slots.update(r["antigen_slots"])
            tot_hits.update(r["antigen_hits"])
            tot_cd.update(r["cd_markers"])
            tot_cd_slots.update(r["cd_slots"])
            for n in r["named_antigens"]:
                names[n] += 1
            for n in r["named_therapeutic_targets"]:
                drug_targets[n] += 1
            for k in ("antigen_obj_total", "antigen_obj_with_B", "antigen_obj_with_T",
                      "antigen_obj_with_APC", "antigen_obj_unattributed", "b_nodes",
                      "t_nodes", "bt_same_node", "hla_mentions",
                      "autoantibody_biomarkers", "autoantibody_biomarkers_bound"):
                agg[k] += r[k]

        w(f"entries scanned              {len(recs)}")
        w(f"immune cohort                {len(immune)}")
        for k, v in reasons.most_common():
            w(f"    via {k:<22} {v}")
        w(f"immune entries naming an antigen  {len(antigen)}"
          f"  ({100*len(antigen)/max(1,len(immune)):.0f}% of cohort)")
        w("")
        w("-- where antigen text lives (objects, immune cohort) --")
        for k, v in tot_slots.most_common(15):
            w(f"    {k:<28} {v}")
        w("")
        w("-- antigen pattern frequency (raw matches) --")
        for k, v in tot_hits.most_common():
            w(f"    {k:<28} {v}")
        w("")
        w("-- lymphocyte attribution of antigen-naming objects --")
        t = agg["antigen_obj_total"] or 1
        w(f"    objects naming an antigen   {agg['antigen_obj_total']}")
        w(f"    ... with a B-lineage cell   {agg['antigen_obj_with_B']} ({100*agg['antigen_obj_with_B']/t:.1f}%)")
        w(f"    ... with a T-lineage cell   {agg['antigen_obj_with_T']} ({100*agg['antigen_obj_with_T']/t:.1f}%)")
        w(f"    ... with an APC             {agg['antigen_obj_with_APC']} ({100*agg['antigen_obj_with_APC']/t:.1f}%)")
        w(f"    ... no cell_types at all    {agg['antigen_obj_unattributed']} ({100*agg['antigen_obj_unattributed']/t:.1f}%)")
        w("")
        w("-- pathophysiology nodes by lineage --")
        w(f"    nodes with a B-lineage cell {agg['b_nodes']}")
        w(f"    nodes with a T-lineage cell {agg['t_nodes']}")
        w(f"    nodes carrying both         {agg['bt_same_node']}")
        w("")
        w("-- HLA --")
        w(f"    prose mentions              {agg['hla_mentions']}")
        w(f"    entries with an HLA gene_term binding  {sum(1 for r in immune if r['hla_structured'])}")
        w("")
        w("-- autoantibody biomarkers --")
        w(f"    biochemical antibody rows   {agg['autoantibody_biomarkers']}")
        w(f"    ... with a biomarker_term   {agg['autoantibody_biomarkers_bound']}")
        w("")
        w("-- surface/lineage markers (CD) --")
        for k, v in tot_cd.most_common():
            w(f"    {k:<28} {v}")
        w("    slots:")
        for k, v in tot_cd_slots.most_common(8):
            w(f"        {k:<24} {v}")
        w("")
        w("-- most-named antigens outside treatments (free text, uncontrolled) --")
        for k, v in names.most_common(30):
            w(f"    {v:3d}  {k}")
        w("")
        w("-- 'anti-X' targets named inside treatments/clinical_trials --")
        w("   (drug targets, not autoantigens; the YAML gives no way to tell them apart)")
        for k, v in drug_targets.most_common(15):
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
