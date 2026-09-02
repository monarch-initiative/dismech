#!/usr/bin/env python3
"""Audit the biological-scale gap between a model and the mechanism it is linked to.

A ``ModelMechanismLink`` says a model is informative for a pathophysiology node.
It does not, by itself, say whether the model can actually *observe* that node.
A signalling-network model whose output node is named "bone erosion" still
observes only molecular or cellular state; the tissue-level outcome is inferred,
not measured. Before ``model_scale`` existed, that caveat survived only as prose
in ``limitations`` — unqueryable, and easy to omit entirely.

``ModelMechanismLink.model_scale`` records the scale the model observes, in the
same ``BiologicalScaleEnum`` as ``Pathophysiology.biological_scale``. This audit
derives the comparison rather than storing it, and the comparison is
**directional** — the two directions are not the same claim:

* ``MODEL_BELOW_TARGET`` — the model sits below its target's scale and is
  extrapolating upward. It cannot observe the outcome it is cited for. This is
  the state worth reviewing, and it is where ``limitations`` should be present.
* ``MODEL_ABOVE_TARGET`` — the model contains its target's scale. Normally
  unremarkable: a whole animal can report a molecular readout.
* ``ALIGNED`` — the model observes at its target's scale.
* ``UNDETERMINED`` — ``model_scale`` or the target's ``biological_scale`` is
  absent. Both slots are optional, so this is the default state for links that
  predate the slot, not a defect.

The gap is reported in enum steps (MOLECULAR < CELLULAR < TISSUE < ORGANISM), so
a 2-step upward extrapolation is visibly a stronger claim than a 1-step one.

Scale is only one way a model can diverge from its target, and this audit
deliberately does not try to be the others. A molecular model linked to a
molecular node reports ALIGNED even when it is a poor model for an unrelated
reason — pathway activation standing in for recombination fidelity, say. Read
``ALIGNED`` as "no *scale* gap", never as "good model".
"""

from __future__ import annotations

import argparse
import collections
import glob
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from dismech.yaml_io import safe_load  # noqa: E402

SCALE_ORDER = ["MOLECULAR", "CELLULAR", "TISSUE", "ORGANISM"]
MODEL_SECTIONS = ["experimental_models", "animal_models", "computational_models"]


def classify(model_scale, target_scale):
    """Return (verdict, gap_in_steps). gap is None when undetermined."""
    if not model_scale or not target_scale:
        return "UNDETERMINED", None
    if model_scale not in SCALE_ORDER or target_scale not in SCALE_ORDER:
        return "UNDETERMINED", None
    gap = SCALE_ORDER.index(target_scale) - SCALE_ORDER.index(model_scale)
    if gap == 0:
        return "ALIGNED", 0
    if gap > 0:
        return "MODEL_BELOW_TARGET", gap
    return "MODEL_ABOVE_TARGET", gap


def collect(paths):
    rows = []
    for path in paths:
        data = safe_load(open(path))
        if not isinstance(data, dict):
            continue
        scales = {
            n.get("name"): n.get("biological_scale")
            for n in (data.get("pathophysiology") or [])
            if isinstance(n, dict)
        }
        for section in MODEL_SECTIONS:
            for model in data.get(section) or []:
                if not isinstance(model, dict):
                    continue
                name = model.get("name") or model.get("species") or "(unnamed)"
                for link in model.get("modeled_mechanisms") or []:
                    if not isinstance(link, dict):
                        continue
                    target = link.get("target")
                    ms = link.get("model_scale")
                    ts = scales.get(target)
                    verdict, gap = classify(ms, ts)
                    rows.append(
                        {
                            "file": path,
                            "section": section,
                            "model": name,
                            "target": target,
                            "model_scale": ms,
                            "target_scale": ts,
                            "verdict": verdict,
                            "gap": gap,
                            "fidelity": link.get("fidelity"),
                            "relationship": link.get("relationship"),
                            "has_limitations": bool(link.get("limitations")),
                            "divergences": [
                                d.get("divergence_type")
                                for d in (link.get("divergences") or [])
                                if isinstance(d, dict)
                            ],
                        }
                    )
    return rows


def kb_files():
    return sorted(glob.glob("kb/disorders/*.yaml")) + sorted(glob.glob("kb/modules/*.yaml"))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*", help="KB files (default: all disorders + modules)")
    ap.add_argument("--format", choices=["summary", "list", "tsv"], default="summary")
    ap.add_argument("--verdict", help="Only rows with this verdict")
    ap.add_argument(
        "--strict",
        action="store_true",
        help="Exit 1 if any MODEL_BELOW_TARGET link carries no `limitations`.",
    )
    args = ap.parse_args()

    rows = collect(args.files or kb_files())
    if args.verdict:
        shown = [r for r in rows if r["verdict"] == args.verdict]
    else:
        shown = rows

    if args.format == "tsv":
        cols = ["file", "section", "model", "target", "model_scale", "target_scale", "verdict", "gap", "fidelity", "relationship", "has_limitations"]
        print("\t".join(cols))
        for r in shown:
            print("\t".join("" if r[c] is None else str(r[c]) for c in cols))
    elif args.format == "list":
        for r in shown:
            gap = "" if r["gap"] is None else f" (gap {r['gap']:+d})"
            print(f"{r['verdict']}{gap}\t{os.path.basename(r['file'])}\t{r['model']} -> {r['target']}")
    else:
        counts = collections.Counter(r["verdict"] for r in rows)
        total = len(rows)
        determined = total - counts["UNDETERMINED"]
        print(f"model->mechanism links: {total}")
        print(f"  scale-determined:     {determined} ({100 * determined / total:.1f}%)" if total else "")
        for v in ["ALIGNED", "MODEL_BELOW_TARGET", "MODEL_ABOVE_TARGET", "UNDETERMINED"]:
            if counts[v]:
                print(f"    {v:20s} {counts[v]:5d}")
        below = [r for r in rows if r["verdict"] == "MODEL_BELOW_TARGET"]
        if below:
            steps = collections.Counter(r["gap"] for r in below)
            print(f"\n  upward extrapolation by step size: {dict(sorted(steps.items()))}")
            unexplained = [r for r in below if not r["has_limitations"] and not r["divergences"]]
            print(f"  ...of which carry neither `limitations` nor `divergences`: {len(unexplained)}")
            for r in unexplained[:20]:
                print(f"      {os.path.basename(r['file'])}: {r['model']} -> {r['target']}")
            undeclared = [r for r in below if r["divergences"] and "SCALE_EXTRAPOLATION" not in r["divergences"]]
            if undeclared:
                print(
                    f"  ...typed, but without a SCALE_EXTRAPOLATION divergence: {len(undeclared)}"
                )
                for r in undeclared[:20]:
                    print(f"      {os.path.basename(r['file'])}: {r['model']} -> {r['target']}")

        typed = [r for r in rows if r["divergences"]]
        if typed:
            kinds = collections.Counter(k for r in typed for k in r["divergences"])
            print(f"\n  links carrying typed divergences: {len(typed)}")
            for k, n in kinds.most_common():
                print(f"    {k:26s} {n:4d}")
            # A SCALE_EXTRAPOLATION divergence asserts a gap the scale slots can check.
            contradicted = [
                r
                for r in rows
                if "SCALE_EXTRAPOLATION" in r["divergences"]
                and r["verdict"] in ("ALIGNED", "MODEL_ABOVE_TARGET")
            ]
            if contradicted:
                print(
                    f"\n  WARNING: {len(contradicted)} SCALE_EXTRAPOLATION divergence(s) "
                    f"contradicted by the scale comparison:"
                )
                for r in contradicted:
                    print(
                        f"      {os.path.basename(r['file'])}: {r['model']} -> {r['target']} "
                        f"({r['model_scale']} vs {r['target_scale']} = {r['verdict']})"
                    )

    if args.strict:
        bad = [
            r
            for r in rows
            if r["verdict"] == "MODEL_BELOW_TARGET"
            and not r["has_limitations"]
            and not r["divergences"]
        ]
        contradicted = [
            r
            for r in rows
            if "SCALE_EXTRAPOLATION" in r["divergences"]
            and r["verdict"] in ("ALIGNED", "MODEL_ABOVE_TARGET")
        ]
        if bad:
            print(
                f"\nFAIL: {len(bad)} upward-extrapolating link(s) with neither "
                f"`limitations` nor `divergences`.",
                file=sys.stderr,
            )
        if contradicted:
            print(
                f"\nFAIL: {len(contradicted)} SCALE_EXTRAPOLATION divergence(s) "
                f"contradicted by model_scale vs biological_scale.",
                file=sys.stderr,
            )
        if bad or contradicted:
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
