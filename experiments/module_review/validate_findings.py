#!/usr/bin/env python3
"""Check one batch's findings file against the contract in README.md.

    uv run python experiments/module_review/validate_findings.py <run_dir> <batch> [--partial]

Exits 1 on any error. ``--partial`` accepts a file that does not yet cover every
module of the batch, for commits made while a review is in progress.

The check that matters most is the quote: a finding's ``quote`` must be a span
of the module file it is about, compared after collapsing whitespace. A finding
that cannot point at the text it criticises does not get in.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path.cwd()
SEVERITIES = {"HIGH", "MEDIUM", "LOW"}
DIMENSIONS = {"LOGIC", "BIOLOGY", "UTILITY", "COHERENCE"}
CONFIDENCES = {"HIGH", "MEDIUM", "LOW"}
VERDICTS = {"SOUND", "MINOR_ISSUES", "MAJOR_ISSUES", "RESTRUCTURE"}
CROSS_CATEGORIES = {
    "OVERLAP",
    "CONTRADICTION",
    "BOUNDARY",
    "GRANULARITY",
    "NAMING",
    "COLLECTION",
    "MISSING_LINK",
    "OTHER",
}
SCORE_KEYS = {"logic", "biology", "utility", "coherence"}
MAX_LOW_PER_MODULE = 5


def squash(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def nonempty(value) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate(
    run_dir: str, batch_id: str, partial: bool
) -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []
    run = ROOT / run_dir
    batches = {
        b["id"]: b
        for b in yaml.safe_load((run / "batches.yaml").read_text())["batches"]
    }
    if batch_id not in batches:
        return [f"unknown batch {batch_id}"], warnings, {}
    expected = batches[batch_id]["modules"]
    all_modules = {p.stem for p in (ROOT / "kb" / "modules").glob("*.yaml")}
    path = run / "findings" / f"{batch_id}.json"
    if not path.exists():
        return [f"{path} does not exist"], warnings, {}
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{path} is not valid JSON: {exc}"], warnings, {}

    if doc.get("batch") != batch_id:
        errors.append(f"batch is {doc.get('batch')!r}, expected {batch_id!r}")
    for key in ("reviewer", "reviewed_commit"):
        if not nonempty(doc.get(key)):
            errors.append(f"top-level {key} is missing")
    if not partial and not nonempty(doc.get("limitations")):
        errors.append(
            "top-level limitations is missing (say what could not be checked)"
        )

    seen_ids: set[str] = set()
    tally = {"modules": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0, "cross": 0}
    reviewed = []
    for entry in doc.get("modules") or []:
        stem = entry.get("module")
        where = f"modules[{stem}]"
        reviewed.append(stem)
        if stem not in expected:
            errors.append(f"{where}: not a module of batch {batch_id}")
            continue
        tally["modules"] += 1
        text = squash(
            (ROOT / "kb" / "modules" / f"{stem}.yaml").read_text(encoding="utf-8")
        )
        if entry.get("verdict") not in VERDICTS:
            errors.append(
                f"{where}: verdict {entry.get('verdict')!r} not in {sorted(VERDICTS)}"
            )
        scores = entry.get("scores") or {}
        if set(scores) != SCORE_KEYS or not all(
            isinstance(v, int) and 1 <= v <= 5 for v in scores.values()
        ):
            errors.append(
                f"{where}: scores must be integers 1-5 for exactly {sorted(SCORE_KEYS)}"
            )
        if not nonempty(entry.get("summary")):
            errors.append(f"{where}: summary is missing")
        if not isinstance(entry.get("evidence_spot_checks"), int):
            errors.append(f"{where}: evidence_spot_checks must be an integer")
        if not isinstance(entry.get("conformers_read"), list):
            errors.append(f"{where}: conformers_read must be a list")
        findings = entry.get("findings")
        if not isinstance(findings, list):
            errors.append(f"{where}: findings must be a list (possibly empty)")
            findings = []
        severities = []
        for finding in findings:
            fid = finding.get("id")
            fw = f"{where}.findings[{fid}]"
            if not nonempty(fid) or not fid.startswith(f"{stem}-"):
                errors.append(f"{fw}: id must start with '{stem}-'")
            if fid in seen_ids:
                errors.append(f"{fw}: duplicate id")
            seen_ids.add(fid)
            sev = finding.get("severity")
            if sev not in SEVERITIES:
                errors.append(f"{fw}: severity {sev!r} not in {sorted(SEVERITIES)}")
            else:
                severities.append(sev)
                tally[sev] += 1
            if finding.get("dimension") not in DIMENSIONS:
                errors.append(
                    f"{fw}: dimension {finding.get('dimension')!r} not in {sorted(DIMENSIONS)}"
                )
            if finding.get("confidence") not in CONFIDENCES:
                errors.append(
                    f"{fw}: confidence {finding.get('confidence')!r} not in {sorted(CONFIDENCES)}"
                )
            for key in (
                "category",
                "location",
                "problem",
                "suggestion",
                "verification",
            ):
                if not nonempty(finding.get(key)):
                    errors.append(f"{fw}: {key} is missing")
            if "quote" not in finding:
                errors.append(
                    f"{fw}: quote is missing (use null for a finding about something absent)"
                )
            elif finding["quote"] is not None:
                if not nonempty(finding["quote"]):
                    errors.append(f"{fw}: quote is empty; use null instead")
                elif squash(finding["quote"]) not in text:
                    errors.append(
                        f"{fw}: quote is not a span of kb/modules/{stem}.yaml: {finding['quote'][:80]!r}"
                    )
            elif sev == "HIGH":
                warnings.append(
                    f"{fw}: HIGH finding with no quote; confirm it is about something absent"
                )
            for other in finding.get("related_modules") or []:
                if other not in all_modules:
                    errors.append(
                        f"{fw}: related module {other!r} is not in kb/modules"
                    )
        if severities.count("LOW") > MAX_LOW_PER_MODULE:
            errors.append(
                f"{where}: {severities.count('LOW')} LOW findings; keep the {MAX_LOW_PER_MODULE} that matter"
            )
        verdict = entry.get("verdict")
        if verdict == "SOUND" and any(s in ("HIGH", "MEDIUM") for s in severities):
            errors.append(f"{where}: verdict SOUND with a HIGH or MEDIUM finding")
        if verdict == "MINOR_ISSUES" and "HIGH" in severities:
            errors.append(f"{where}: verdict MINOR_ISSUES with a HIGH finding")
        if verdict == "MAJOR_ISSUES" and "HIGH" not in severities:
            errors.append(f"{where}: verdict MAJOR_ISSUES without a HIGH finding")

    dupes = sorted({m for m in reviewed if reviewed.count(m) > 1})
    if dupes:
        errors.append(f"modules reviewed twice: {dupes}")
    missing = [m for m in expected if m not in reviewed]
    if missing and not partial:
        errors.append(f"modules not reviewed yet: {missing}")
    elif missing:
        warnings.append(f"still to review: {missing}")

    for finding in doc.get("cross_module_findings") or []:
        fid = finding.get("id")
        fw = f"cross_module_findings[{fid}]"
        tally["cross"] += 1
        if not nonempty(fid) or not fid.startswith(f"{batch_id}-X"):
            errors.append(f"{fw}: id must start with '{batch_id}-X'")
        if fid in seen_ids:
            errors.append(f"{fw}: duplicate id")
        seen_ids.add(fid)
        if finding.get("severity") not in SEVERITIES:
            errors.append(f"{fw}: severity not in {sorted(SEVERITIES)}")
        if finding.get("category") not in CROSS_CATEGORIES:
            errors.append(
                f"{fw}: category {finding.get('category')!r} not in {sorted(CROSS_CATEGORIES)}"
            )
        if finding.get("confidence") not in CONFIDENCES:
            errors.append(f"{fw}: confidence not in {sorted(CONFIDENCES)}")
        mods = finding.get("modules")
        if not isinstance(mods, list) or len(mods) < 2:
            errors.append(f"{fw}: modules must list at least two modules")
        else:
            for other in mods:
                if other not in all_modules:
                    errors.append(f"{fw}: module {other!r} is not in kb/modules")
            if not any(m in expected for m in mods):
                errors.append(f"{fw}: none of {mods} is in batch {batch_id}")
        for key in ("problem", "suggestion", "verification"):
            if not nonempty(finding.get(key)):
                errors.append(f"{fw}: {key} is missing")
    return errors, warnings, tally


def main(argv: list[str]) -> int:
    args = [a for a in argv if not a.startswith("--")]
    if len(args) != 2:
        print(__doc__)
        return 2
    errors, warnings, tally = validate(args[0], args[1], "--partial" in argv)
    for line in warnings:
        print(f"warning: {line}")
    for line in errors:
        print(f"ERROR: {line}")
    if errors:
        print(f"{len(errors)} error(s) in {args[1]}")
        return 1
    print(
        f"OK {args[1]}: {tally['modules']} module(s), {tally['HIGH']} HIGH, {tally['MEDIUM']} MEDIUM, "
        f"{tally['LOW']} LOW, {tally['cross']} cross-module"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
