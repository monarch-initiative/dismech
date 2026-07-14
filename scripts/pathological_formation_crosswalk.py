"""Cross-walk of pathological-structure-formation ("pathological Xogenesis") anchors.

Purpose
-------
dismech has an emerging *family* of mechanism modules whose shared shape is the
**formation of a pathological material anatomical entity** X — cyst, calculus,
granuloma, thrombus, amyloid deposit, neoplasm, fibrous scar, aneurysm, and so
on. This script materializes the open-ontology anchor model for that family and
diffs it against both SNOMED (as an external census / gap detector) and the
current dismech module set.

The anchor model (all open ontologies; deliberately avoids GO's *programmed*
``anatomical structure formation`` genus, which presupposes normal development):

    process   : OGMS:0000061 pathological bodily process
                  -> OGMS:0000080 pathological transformation   (a canonical
                     structure BECOMES a pathological structure; e.g. cystogenesis)
                  -> OGMS:0000081 pathological derivation        (a NEW formation
                     replaces prior tissue; e.g. granuloma, thrombus, stone)
    output    : OGMS:0000078 pathological anatomical structure   (discrete structure)
                  OGMS:0000079 portion of pathological body substance (deposit/stone/fluid)
    species   : MPATH:603 pathological anatomical entity subtree  (the specific X)
    site      : UBERON anatomical entity                          (optional)
    bridge    : RO:0002297 results in formation of anatomical entity / RO:0002234 has output

SNOMED CT "Morphologically abnormal structure" (49755003) is used ONLY as a
guide/census to enumerate candidate X's and surface gaps; no SNOMED identifier is
bound in dismech data. SNOMED SCTIDs are intentionally omitted here (licensed,
and not resolvable from an OAK adapter in this repo) -- the SNOMED column is the
concept *label* to look up in a licensed browser.

Three gap classes fall out:
  GAP-1  entity present in the SNOMED census but with no MPATH class  -> OBO addition
  GAP-2  entity with an MPATH class but no dismech formation module    -> curation backlog
  GAP-3  existing dismech formation module carrying no anchor triple   -> retrofit

Usage
-----
    uv run python scripts/pathological_formation_crosswalk.py            # write research/ md + summary
    uv run python scripts/pathological_formation_crosswalk.py --stdout   # print md to stdout
"""

from __future__ import annotations

import argparse
import glob
import os
from dataclasses import dataclass, field

from oaklib import get_adapter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(ROOT, "kb", "modules")
OUT_PATH = os.path.join(ROOT, "research", "pathological_formation_crosswalk.md")

# OGMS anchor classes (process genus + output continuants).
OGMS_CLASSES = {
    "OGMS:0000061": "pathological bodily process",
    "OGMS:0000080": "pathological transformation",
    "OGMS:0000081": "pathological derivation",
    "OGMS:0000078": "pathological anatomical structure",
    "OGMS:0000079": "portion of pathological body substance",
}

# Short process-type word for the two formation sub-genera.
PROC_WORD = {"OGMS:0000080": "transformation", "OGMS:0000081": "derivation"}

# Cancer is captured as a decomposed set of hallmark modules rather than one
# "tumorigenesis" module; detect the family by these known stems.
CANCER_HALLMARK_STEMS = {
    "sustaining_proliferative_signaling",
    "evading_growth_suppressors",
    "resisting_cell_death",
    "enabling_replicative_immortality",
    "tumor_angiogenesis",
    "invasion_and_metastasis",
    "deregulated_cellular_energetics",
    "genome_instability_mutation",
    "tumor_promoting_inflammation",
    "viral_oncogenesis",
}


@dataclass
class Entity:
    """One pathological material entity X in the formation-module family."""

    name: str
    snomed_label: str          # concept under SNOMED "Morphologically abnormal structure"
    ogms_output: str           # OGMS:0000078 (structure) | OGMS:0000079 (substance)
    ogms_process: str          # OGMS:0000080 transformation | OGMS:0000081 derivation
    mpath_id: str | None       # MPATH:603-subtree species; None = MPATH gap
    site_uberon: str | None    # canonical site if singular; None if site-varies
    module: str | None         # dismech module stem, "SET:cancer" sentinel, or None
    note: str = ""


# Curated census. The SNOMED labels enumerate the target axis; OGMS/MPATH/module
# columns are the open-ontology anchors and dismech coverage. MPATH ids are
# resolved live below so drift is caught.
ENTITIES: list[Entity] = [
    # --- structure BECOMES pathological (transformation) ---
    Entity("Cyst", "Cyst", "OGMS:0000078", "OGMS:0000080", "MPATH:62",
           None, "renal_cystogenesis",
           "renal covered; hepatic/pancreatic/arachnoid/odontogenic cysts uncovered"),
    Entity("Aneurysm", "Aneurysm", "OGMS:0000078", "OGMS:0000080", "MPATH:90",
           None, "aortopathy_tgfbeta_dysregulation", "thoracic-aortic arm only"),
    Entity("Polyp", "Polyp", "OGMS:0000078", "OGMS:0000080", "MPATH:491",
           None, None, ""),
    # --- NEW formation replaces prior tissue (derivation) ---
    Entity("Neoplasm", "Neoplasm", "OGMS:0000078", "OGMS:0000081", "MPATH:218",
           None, "SET:cancer", "decomposed across the hallmarks-of-cancer modules"),
    Entity("Granuloma", "Granuloma", "OGMS:0000078", "OGMS:0000081", "MPATH:847",
           None, None, ""),
    Entity("Abscess", "Abscess", "OGMS:0000078", "OGMS:0000081", "MPATH:608",
           None, None, ""),
    Entity("Thrombus", "Thrombus", "OGMS:0000079", "OGMS:0000081", "MPATH:125",
           None, None, "MPATH has the process 'thrombosis' (MPATH:125) but no 'thrombus' continuant"),
    Entity("Atheroma / atherosclerotic plaque", "Atheromatous plaque",
           "OGMS:0000078", "OGMS:0000081", None, None, None, "MPATH gap"),
    Entity("Hematoma", "Hematoma", "OGMS:0000079", "OGMS:0000081", "MPATH:121",
           None, None, ""),
    Entity("Infarct", "Infarct", "OGMS:0000078", "OGMS:0000081", "MPATH:124",
           None, None, "usually a consequence node rather than a standalone module"),
    # --- concretions / deposits -> pathological body substance (derivation) ---
    Entity("Renal calculus", "Calculus", "OGMS:0000079", "OGMS:0000081", "MPATH:614",
           "UBERON:0002113", "nephrolithiasis_crystal_nucleation",
           "MPATH has generic 'concretion' (MPATH:614); no specific 'calculus'"),
    Entity("Gallstone", "Calculus", "OGMS:0000079", "OGMS:0000081", "MPATH:614",
           None, "cholelithiasis_biliary_supersaturation", ""),
    Entity("Urate tophus", "Tophus", "OGMS:0000079", "OGMS:0000081", "MPATH:614",
           None, "gout_urate_crystal_inflammation", "tophus == urate concretion"),
    Entity("Amyloid deposit", "Amyloid", "OGMS:0000079", "OGMS:0000081", None,
           None, None, "MPATH gap"),
    Entity("Ectopic calcification", "Calcium deposit", "OGMS:0000079", "OGMS:0000081",
           "MPATH:36", None, None, "MPATH:36 'calcium deposition'"),
    Entity("Heterotopic ossification", "Ectopic bone", "OGMS:0000078", "OGMS:0000081",
           None, None, None, "MPATH gap"),
    # --- tissue-level structural change ---
    Entity("Fibrosis / scar", "Fibrosis", "OGMS:0000078", "OGMS:0000081", "MPATH:181",
           None, "fibrotic_response", "conserved multi-organ fibrotic response"),
    Entity("Sclerosis", "Sclerosis", "OGMS:0000078", "OGMS:0000081", "MPATH:184",
           None, None, ""),
    Entity("Lens opacity (cataract)", "Cataract", "OGMS:0000079", "OGMS:0000080",
           None, "UBERON:0000965", "cataract_lens_opacification",
           "edge case: crystallin aggregate / loss of transparency; no clean MPATH species"),
    Entity("Edema / effusion", "Edema", "OGMS:0000079", "OGMS:0000081", "MPATH:109",
           None, None, "edge case: fluid accumulation, arguably not a discrete formation"),
]


def _module_stems() -> set[str]:
    return {os.path.splitext(os.path.basename(f))[0]
            for f in glob.glob(os.path.join(MODULES_DIR, "*.yaml"))}


def _resolve_labels(curies: set[str], adapter_sel: str) -> dict[str, str | None]:
    labels: dict[str, str | None] = {}
    if not curies:
        return labels
    adapter = get_adapter(adapter_sel)
    for c in curies:
        try:
            labels[c] = adapter.label(c)
        except Exception:  # noqa: BLE001 - resolution best-effort
            labels[c] = None
    return labels


@dataclass
class Report:
    rows: list[dict] = field(default_factory=list)
    gap1: list[Entity] = field(default_factory=list)   # SNOMED census, no MPATH class
    gap2: list[Entity] = field(default_factory=list)   # MPATH class, no dismech module
    gap3: list[str] = field(default_factory=list)       # module with no anchor triple
    mpath_drift: list[str] = field(default_factory=list)
    orphan_modules: list[str] = field(default_factory=list)


def build() -> Report:
    stems = _module_stems()
    mpath_ids = {e.mpath_id for e in ENTITIES if e.mpath_id}
    mpath_labels = _resolve_labels(mpath_ids, "sqlite:obo:mpath")

    rep = Report()
    covered_stems: set[str] = set()

    for e in ENTITIES:
        # Resolve module coverage.
        if e.module == "SET:cancer":
            present = CANCER_HALLMARK_STEMS & stems
            covered_stems |= present
            module_disp = f"hallmarks-of-cancer set ({len(present)} modules)" if present else None
        elif e.module:
            exists = e.module in stems
            if exists:
                covered_stems.add(e.module)
            else:
                rep.mpath_drift.append(f"module '{e.module}' referenced for {e.name} not found")
            module_disp = e.module + ("" if exists else " (MISSING!)")
        else:
            module_disp = None

        # MPATH drift check.
        mp_label = mpath_labels.get(e.mpath_id) if e.mpath_id else None
        if e.mpath_id and mp_label is None:
            rep.mpath_drift.append(f"{e.mpath_id} ({e.name}) did not resolve in MPATH")

        rep.rows.append({
            "entity": e.name,
            "snomed": e.snomed_label,
            "ogms_process": e.ogms_process,
            "ogms_output": e.ogms_output,
            "mpath": f"{e.mpath_id} {mp_label}".strip() if e.mpath_id else "— (gap)",
            "site": e.site_uberon or "—",
            "module": module_disp or "—",
            "note": e.note,
        })

        if e.mpath_id is None:
            rep.gap1.append(e)
        if e.mpath_id is not None and module_disp is None:
            rep.gap2.append(e)

    # GAP-3: every dismech formation module that exists carries no anchor triple
    # yet (none are declared in schema today), so all covered stems are retrofit
    # targets.
    rep.gap3 = sorted(covered_stems)
    return rep


def render_markdown(rep: Report) -> str:
    ogms = _resolve_labels(set(OGMS_CLASSES), "sqlite:obo:ogms")
    lines: list[str] = []
    A = lines.append
    A("# Pathological-structure-formation cross-walk\n")
    A("> Generated by `scripts/pathological_formation_crosswalk.py` "
      "(`uv run python scripts/pathological_formation_crosswalk.py`). Do not hand-edit.\n")
    A("The open-ontology anchor for the dismech *pathological Xogenesis* module family. "
      "Deliberately avoids GO's programmed `anatomical structure formation` genus; the "
      "pathological process genus comes from OGMS, the specific entity from MPATH, the site "
      "from UBERON. SNOMED 'Morphologically abnormal structure' (49755003) is a census/gap "
      "guide only and is never bound in dismech data.\n")

    A("## Anchor classes\n")
    A("| CURIE | label (resolved) | role |")
    A("|---|---|---|")
    roles = {
        "OGMS:0000061": "process genus",
        "OGMS:0000080": "process: structure becomes pathological (transformation)",
        "OGMS:0000081": "process: new formation replaces prior tissue (derivation)",
        "OGMS:0000078": "output: discrete pathological structure",
        "OGMS:0000079": "output: pathological body substance (deposit/stone/fluid)",
    }
    for c, seeded in OGMS_CLASSES.items():
        A(f"| `{c}` | {ogms.get(c) or seeded} | {roles.get(c, '')} |")
    A("\nBridge relations: `RO:0002297` results in formation of anatomical entity; "
      "`RO:0002234` has output.\n")

    A("## Cross-walk\n")
    A("| Entity (X) | SNOMED census | OGMS process | OGMS output | MPATH species | Site | dismech module | Notes |")
    A("|---|---|---|---|---|---|---|---|")
    for r in rep.rows:
        A(f"| {r['entity']} | {r['snomed']} | `{r['ogms_process']}` | `{r['ogms_output']}` "
          f"| {r['mpath']} | {r['site']} | {r['module']} | {r['note']} |")

    A("\n## GAP-1 — SNOMED census entity with no MPATH class (OBO addition candidates)\n")
    if rep.gap1:
        for e in rep.gap1:
            A(f"- **{e.name}** ({e.snomed_label}) — output would be `{e.ogms_output}`; {e.note}")
    else:
        A("_none_")

    A("\n## GAP-2 — entity has an MPATH class but no dismech formation module (curation backlog)\n")
    if rep.gap2:
        for e in rep.gap2:
            word = PROC_WORD.get(e.ogms_process, "formation")
            A(f"- **{e.name}** — `{e.mpath_id}`; candidate {word} module "
              f"(process `{e.ogms_process}`, output `{e.ogms_output}`)")
    else:
        A("_none_")

    A("\n## GAP-3 — existing dismech formation module with no anchor triple (retrofit)\n")
    A("No module declares an (OGMS process, MPATH output, UBERON site) triple today. The "
      "single-entity formation modules below are direct retrofit targets:\n")
    cancer = sorted(s for s in rep.gap3 if s in CANCER_HALLMARK_STEMS)
    primary = [s for s in rep.gap3 if s not in CANCER_HALLMARK_STEMS]
    for stem in primary:
        A(f"- `{stem}`")
    if cancer:
        A("\nThe hallmarks-of-cancer modules form a neoplasm *collectively* (the output is "
          "emergent across the set), so a per-module `forms_structure: MPATH:218` triple is "
          f"likely inappropriate — handle at the set level: {', '.join('`'+s+'`' for s in cancer)}.")

    if rep.mpath_drift:
        A("\n## Drift / integrity warnings\n")
        for w in rep.mpath_drift:
            A(f"- ⚠️ {w}")

    A("")
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--stdout", action="store_true",
                    help="print markdown to stdout instead of writing research/ file")
    args = ap.parse_args()

    rep = build()
    md = render_markdown(rep)

    if args.stdout:
        print(md)
        return

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as fh:
        fh.write(md)
    print(f"Wrote {os.path.relpath(OUT_PATH, ROOT)}")
    print(f"  cross-walk rows : {len(rep.rows)}")
    print(f"  GAP-1 (MPATH)   : {len(rep.gap1)}  -> {', '.join(e.name for e in rep.gap1)}")
    print(f"  GAP-2 (module)  : {len(rep.gap2)}  -> {', '.join(e.name for e in rep.gap2)}")
    print(f"  GAP-3 (retrofit): {len(rep.gap3)}")
    if rep.mpath_drift:
        print("  WARNINGS:")
        for w in rep.mpath_drift:
            print(f"    - {w}")


if __name__ == "__main__":
    main()
