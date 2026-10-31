#!/usr/bin/env python3
"""Backfill ``Experiment.experiment_design`` from each experiment's own prose.

``experiment_design`` is the closed design-family enum added alongside
``executability`` (see ``docs/explanation/experiment-model.md``). It exists
because ``experiment_type`` -- an ontology-backed ``Descriptor`` -- was never
fillable in practice: across the KB it carries a few hundred values holding
*hundreds of distinct free-text strings* and almost no ontology CURIEs, because
OBI is absent from ``conf/oak_config.yaml`` and cannot be validated. Curators
were writing the family into prose instead.

What this script does
---------------------
It assigns a value only on an **unambiguous anchor** found in the experiment's
own *method statement* -- its ``name``, its ``experiment_type``, and the first
sentence of its ``description``. Everything else is left absent and written to a
worklist TSV for a curator.

This follows ``scripts/migrate_supports_enum.py``: a value no curator assessed
is not written. CLAUDE.md also records a treatment-modality backfill that was
tried and reverted for mis-tagging real drug therapies as ``BEHAVIORAL``, which
is the failure mode a looser rule here would reproduce at scale.

Why the method statement and not the whole description
------------------------------------------------------
Perturbation vocabulary in later sentences is usually describing a *control arm*
or *another published model*, not what this experiment does. Two measured
examples, both of which a whole-text match classified wrongly:

  * "Re-sequencing and expression analysis of the original C1532Y family" --
    whose description ends "...absent from the mouse knock-in". The knock-in is
    somebody else's model, cited as contrast; this experiment sequences a family.
  * "Cilium length and Hedgehog competence in patient fibroblasts ... alongside
    isogenic or unaffected-relative controls" -- where ``isogenic`` names the
    comparator, not the design.

The second case is guarded separately: when the *only* anchor is a weak
perturbation word and it sits next to "control", the experiment is skipped.

Two further guards, each added after a measured false positive
--------------------------------------------------------------
  * A screen must be named as one. "Create a CRISPR germline mutant ...
    providing a tractable vertebrate system for modifier and compound screens"
    is a targeted perturbation that mentions a screen as future work, so
    ``PERTURBATION_SCREEN`` requires "screen" in the experiment's ``name``.
  * Human study units ("relatives", "pedigree", "intrafamilial") are
    ``HUMAN_OBSERVATIONAL`` anchors. An omics study of family members therefore
    raises two anchors and is left for a curator rather than guessed as
    ``DESCRIPTIVE_PROFILING``.

Multiple anchors from different families are *not* resolved to ``MIXED``.
``MIXED`` is a curator's judgement that no single family dominates; a script
cannot tell that from a genuine two-family design. Only two orderings are
applied, where one family strictly contains the other: a library screen over a
targeted perturbation, and a randomized trial over the cohort it recruits.

Measured precision
------------------
Two blind stratified samples were read by hand against the enum definitions:
80% before the guards above, 94% after scoping to the method statement, and the
two residual failures in that second sample are what the screen-name and
human-study-unit guards fix. Precision is not 100% and this is an advisory
annotation, so the diff is meant to be reviewed.

Why a line edit and not a YAML round-trip
-----------------------------------------
Round-tripping hundreds of KB files through a YAML writer reflows folded
scalars, which is what ``just check-folded-hyphens`` exists to catch. Each file
is parsed read-only to classify, and edited as text: one line inserted after the
``experiment_id:`` line, at that key's indentation.

``experiment_id`` is a safe anchor. It is required and 100% populated, no file
in ``kb/`` contains a duplicate value, and in every file the regex match count
equals the parsed experiment count -- both checked before this script was
written, and re-asserted at runtime per file.

Usage
-----
    uv run python scripts/backfill_experiment_design.py --dry-run
    uv run python scripts/backfill_experiment_design.py --apply
"""

from __future__ import annotations

import argparse
import collections
import re
import sys
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from dismech.yaml_io import safe_load  # noqa: E402

WORKLIST = ROOT / "docs" / "reports" / "data" / (
    f"experiment-design-backfill-worklist-{datetime.now(UTC).date().isoformat()}.tsv"
)

#: Anchor patterns per design family, matched against the method statement.
FAMILIES: list[tuple[str, list[str]]] = [
    ("INTERVENTIONAL_TRIAL", [
        r"\brandomi[sz]\w*\b(?=.{0,160}?\b(trial|participant|arm|placebo|endpoint|blind)\b)",
        r"\b(randomi[sz]ed controlled trial|double-blind|placebo-controlled)\b",
        r"\bphase[- ](?:i{1,3}v?|[1-4])\b.{0,40}\btrial\b",
        r"\bprospective international trial\b",
    ]),
    ("PERTURBATION_SCREEN", [
        r"\b(compound|chemical|drug|crispr|sirna|shrna|degrader|probe)\s+(librar\w+\s+)?screen\w*\b",
        r"\bscreen\w*\s+(compound|chemical|drug)\s+librar\w+",
        r"\b(high[- ]throughput|arrayed|pooled|plate[- ]based)\b.{0,60}\bscreen\w*\b",
        r"\bscreen\w*\b.{0,60}\b(compound librar\w+|chemical librar\w+|crispr librar\w+)\b",
    ]),
    ("IN_SILICO", [
        r"\bin silico\b",
        r"\bcomputational fluid dynamics\b",
        r"\bmolecular dynamics\b",
        r"\b(simulat\w+|digital twin|flux balance)\b",
        r"\b(machine[- ]learning|deep[- ]learning)\b",
        r"\bmolecular docking\b",
    ]),
    ("TARGETED_PERTURBATION", [
        r"\bknock[- ]?(out|in|down)\b",
        r"\ballele series\b",
        r"\b(sirna|shrna|morpholino|degron|protac)\b",
        r"\bconditional (deletion|knockout|ablation|depletion)\b",
        r"\boverexpress\w*\b",
        r"\bacute (depletion|degradation|inhibition)\b",
        r"\bcell[- ]type[- ]specific manipulation\b",
        r"\bhypomorphic\b",
        r"\bgenetic (ablation|correction|augmentation)\b",
        # Weak anchors: these two also name comparators, so CONTROL_ONLY guards them.
        r"\brescue\b",
        r"\bisogenic\b",
    ]),
    ("HUMAN_OBSERVATIONAL", [
        r"\bregistr(y|ies)\b",
        r"\bnatural[- ]history\b",
        r"\bcase[- ]control\b",
        r"\b(prospective|retrospective|longitudinal|birth|population)\b.{0,40}\bcohort\b",
        r"\bcohort\b.{0,40}\b(study|follow[- ]up)\b",
        r"\bcross[- ]sectional\b",
        r"\bpopulation[- ]scale\b",
        r"\bfamily[- ]based stud\w+\b",
        # Clinical "screening of patients" is not a library screen.
        r"\bscreening\b.{0,40}\b(adults?|patients?|individuals?|carriers?)\b",
        r"\b(asymptomatic |affected )?relatives\b",
        r"\bfamily members\b",
        r"\bintrafamilial\b",
        r"\bpedigree\b",
    ]),
    ("METHOD_DEVELOPMENT", [
        r"\bassay development\b",
        r"\banalytic(al)? validation\b",
        r"\bbiomarker qualification\b",
    ]),
    ("DESCRIPTIVE_PROFILING", [
        r"\b(atlas|postmortem|post[- ]mortem)\b",
        r"\bsingle[- ]cell\b.{0,30}\b(profil\w+|transcriptom\w+|atlas|sequencing|comparison)\b",
        r"\bspatial (transcriptom\w+|multi[- ]omics|profil\w+)\b",
        r"\b(proteomic|glycoproteomic|degradomic|metabolomic|n[- ]terminomics)\w*\b",
    ]),
]
COMPILED = [(n, [re.compile(p, re.I | re.S) for p in ps]) for n, ps in FAMILIES]

#: The two TARGETED_PERTURBATION anchors that also name a comparator.
WEAK_PERTURBATION = (re.compile(r"\brescue\b", re.I), re.compile(r"\bisogenic\b", re.I))
CONTROL_ONLY = re.compile(
    r"\b(isogenic|unaffected[- ]relative|wild[- ]?type)\b[^.]{0,40}\bcontrol", re.I
)
NAME_SCREEN = re.compile(r"\bscreen\w*\b", re.I)

#: One family strictly contains the other, so the order is safe to apply.
PRIORITY = [
    ("PERTURBATION_SCREEN", {"TARGETED_PERTURBATION"}),
    ("INTERVENTIONAL_TRIAL", {"HUMAN_OBSERVATIONAL"}),
]

EXPERIMENT_ID_LINE = re.compile(r"^(?P<lead>\s*(?:-\s+)?)experiment_id:\s*(?P<eid>\S+)\s*$")
DESIGN_LINE = re.compile(r"^\s*experiment_design:")


def method_statement(exp: dict) -> str:
    """Name + experiment_type + the first sentence of the description."""
    desc = (exp.get("description") or "").strip()
    first = re.split(r"(?<=[.;])\s", desc)[0] if desc else ""
    etype = (exp.get("experiment_type") or {}).get("preferred_term") or ""
    return " || ".join([exp.get("name") or "", etype, first])


def classify(exp: dict) -> tuple[str | None, str]:
    """Return (design, reason). ``design`` is None when nothing is unambiguous."""
    text = method_statement(exp)
    found = {n for n, pats in COMPILED if any(p.search(text) for p in pats)}

    if "PERTURBATION_SCREEN" in found and not NAME_SCREEN.search(exp.get("name") or ""):
        found.discard("PERTURBATION_SCREEN")

    if found == {"TARGETED_PERTURBATION"} and CONTROL_ONLY.search(text):
        strong = [
            p
            for _, pats in COMPILED
            if _ == "TARGETED_PERTURBATION"
            for p in pats
            if p.pattern not in {w.pattern for w in WEAK_PERTURBATION}
        ]
        if not any(p.search(text) for p in strong):
            return None, "perturbation_word_is_comparator_only"

    if not found:
        return None, "no_anchor"
    if len(found) > 1:
        for winner, losers in PRIORITY:
            if winner in found and found <= ({winner} | losers):
                return winner, "priority"
        return None, "multi:" + "+".join(sorted(found))
    return found.pop(), "single"


def iter_experiments(doc: dict):
    """Yield every proposed experiment in a parsed KB document."""
    for disc in doc.get("discussions") or []:
        for exp in disc.get("proposed_experiments") or []:
            if isinstance(exp, dict) and exp.get("experiment_id"):
                yield exp


def patch_file(path: Path, assignments: dict[str, str]) -> tuple[int, list[str]]:
    """Insert experiment_design after each matching experiment_id line.

    Returns (lines inserted, ids skipped because a value was already present).
    """
    lines = path.read_text().splitlines(keepends=True)
    out: list[str] = []
    inserted = 0
    already: list[str] = []
    for i, line in enumerate(lines):
        out.append(line)
        m = EXPERIMENT_ID_LINE.match(line)
        if not m:
            continue
        eid = m.group("eid").strip("\"'")
        design = assignments.get(eid)
        if not design:
            continue
        # Idempotence: a value already in this block wins.
        key_indent = " " * len(m.group("lead"))
        if any(DESIGN_LINE.match(nxt) for nxt in lines[i + 1 : i + 60]):
            already.append(eid)
            continue
        out.append(f"{key_indent}experiment_design: {design}\n")
        inserted += 1
    if inserted:
        path.write_text("".join(out))
    return inserted, already


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dry-run", action="store_true", help="report without writing")
    group.add_argument("--apply", action="store_true", help="rewrite files and worklist")
    args = parser.parse_args()

    assigned: dict[Path, dict[str, str]] = collections.defaultdict(dict)
    worklist: list[tuple[str, str, str, str]] = []
    counts: collections.Counter = collections.Counter()
    reasons: collections.Counter = collections.Counter()
    total = 0

    for path in sorted((ROOT / "kb").rglob("*.yaml")):
        try:
            doc = safe_load(path.open())
        except Exception:
            continue
        if not isinstance(doc, dict):
            continue
        exps = list(iter_experiments(doc))
        if not exps:
            continue
        # Re-assert the anchor's reliability for this file before editing it.
        text = path.read_text()
        n_anchors = len(re.findall(r"(?m)^\s*(?:-\s+)?experiment_id:", text))
        if n_anchors != len(exps):
            print(f"SKIP (anchor count {n_anchors} != {len(exps)} parsed): {path}")
            continue
        ids = [e["experiment_id"] for e in exps]
        if len(set(ids)) != len(ids):
            print(f"SKIP (duplicate experiment_id): {path}")
            continue

        for exp in exps:
            total += 1
            design, reason = classify(exp)
            counts[design] += 1
            reasons[reason.split(":")[0]] += 1
            if design:
                assigned[path][exp["experiment_id"]] = design
            else:
                worklist.append((
                    str(path.relative_to(ROOT)),
                    exp["experiment_id"],
                    reason,
                    (exp.get("name") or "").replace("\t", " "),
                ))

    n_assigned = sum(v for k, v in counts.items() if k)
    print(f"experiments {total}   assigned {n_assigned} ({100 * n_assigned / total:.1f}%)"
          f"   left for a curator {counts[None]}")
    for family, n in counts.most_common():
        if family:
            print(f"   {family:24s} {n:5d}")
    print(f"skip reasons: {dict(reasons)}")

    if args.dry_run:
        print(f"\ndry run: nothing written ({len(assigned)} files would change)")
        return 0

    touched = 0
    total_inserted = 0
    for path, mapping in sorted(assigned.items()):
        n, already = patch_file(path, mapping)
        if n:
            touched += 1
            total_inserted += n
        for eid in already:
            print(f"   kept existing experiment_design: {path.name}:{eid}")
    print(f"\ninserted {total_inserted} experiment_design lines across {touched} files")

    WORKLIST.parent.mkdir(parents=True, exist_ok=True)
    with WORKLIST.open("w") as fh:
        fh.write("file\texperiment_id\treason\tname\n")
        for row in worklist:
            fh.write("\t".join(row) + "\n")
    print(f"worklist ({len(worklist)} rows): {WORKLIST.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
