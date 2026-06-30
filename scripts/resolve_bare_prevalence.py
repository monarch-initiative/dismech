#!/usr/bin/env python3
"""
Resolve the AMBIGUOUS_BARE_NUMBER prevalence backlog under the percent reading.

The prevalence remodel (scripts/migrate_prevalence.py) deliberately left records
whose `percentage` is a bare, unit-less number (e.g. `0.001`, `0.01-0.02`,
`9.79`) unconverted, because a bare number could mean a percent or a proportion.
In practice the field is *named* percentage and, checked against each record's
own evidence, the bare value is a percent for the overwhelming majority
(Apert 0.00124% = 1.24/100k, Alagille 0.001-0.01% = 1-10/100k, Acne 9.79%, ...).

This resolver therefore reads bare numbers as **percent** (rate_per_100000 =
value x 1000) and, as a guard, cross-checks the derived magnitude against any
unit-bearing rate it can extract from the record's notes/evidence:

  * CONFIRMED  - an extracted evidence rate is within `TOL` x of the percent rate
                 -> auto-convert.
  * NO_EVIDENCE - no unit-bearing rate found to cross-check -> NOT converted here
                 (listed for manual review; percent is likely but unverified).
  * DISAGREE   - evidence rates exist but none within `TOL` x -> NOT converted
                 (listed; the bare value may be a proportion or a per-100k rate,
                 or the extractor hit a spurious number - resolve by hand).

Conversion is additive (the deprecated `percentage` is preserved) and uses the
same idempotent textual upsert as the migration. Genuinely uncertain records are
never auto-guessed.

    uv run python scripts/resolve_bare_prevalence.py            # dry-run + report
    uv run python scripts/resolve_bare_prevalence.py --apply    # write CONFIRMED tier
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml as _pyyaml
import migrate_prevalence as M  # reuse parse/classify/upsert machinery

ROOT = Path(__file__).resolve().parent.parent
DISORDERS = ROOT / "kb" / "disorders"
REPORT = ROOT / "research" / "prevalence_bare_number_report.md"
TOL = 5.0  # order-of-magnitude-ish agreement gate


def _nums(bare: str):
    return [float(x) for x in re.findall(r"[\d.]+(?:[eE][-+]?\d+)?", bare)]


def percent_fields(bare: str, pop: str, snippets):
    """Structured fields reading the bare number as a percent (value x 1000 -> /100k)."""
    nums = _nums(bare)
    if not nums or max(nums) > 100:  # >100% impossible -> not a percent
        return None
    measure, inferred = M.detect_measure(f"{bare} | {pop}")
    if not measure:
        ev = M.detect_measure_from_evidence(snippets)
        if ev:
            measure, inferred = ev, False
    f = {}
    if measure:
        f["measure_type"] = measure
    elif inferred:
        f["measure_type"] = "POINT_PREVALENCE"
    if len(nums) == 1:
        rate = nums[0] * 1000
        f["rate_per_100000"] = round(rate, 6)
        f["prevalence_class"] = M._band_from_rate(rate)
    else:
        low, high = min(nums) * 1000, max(nums) * 1000
        f["rate_low"] = round(low, 6)
        f["rate_high"] = round(high, 6)
        f["prevalence_class"] = M._band_from_rate((low + high) / 2)
    return f


# Phrases that mark a bare percentage as something OTHER than population
# prevalence (survival, staging, complication, or fraction-of-category), which
# was wrongly placed in the prevalence slot. These must NOT be converted to a
# population rate_per_100000 — the evidence cross-check would otherwise falsely
# "confirm" them (a "46% 5-year survival" note matches the 46% percent reading).
NONPREV_RE = re.compile(
    r"\b(?:survival|survive[sd]?|5-?year|five-?year|"
    r"present(?:s|ed|ation)?\s+with|at\s+presentation|"
    r"advanced[ -]stage|localized|metastas|brain\s+metast|"
    r"histolog|account[s]?\s+for|relative\s+burden|burden\s+among|"
    r"share\s+of|dominant\s+share|represents?\s+the|"
    r"occur(?:s|red)?\s+in|affect[s]?\s+up\s+to|develop[s]?\s+in|"
    r"of\s+all\s+\w+\s+(?:cancers?|tumou?rs?|lymphomas?|cases)|"
    r"lymphoma\s+diagnoses|lymphoid\s+neoplasms|ovarian\s+cancers|"
    r"acute\s+coronary\s+syndrome|domestic\s+origin|"
    r"5-?year\s+survival|overall\s+survival)\b",
    re.I,
)


def looks_nonprevalence(notes, pop, snippets):
    blob = f"{notes} {pop} " + " ".join(snippets)
    return bool(NONPREV_RE.search(blob))


def evidence_rates(text):
    """High-precision unit-bearing rates (per 100k) from prose, for cross-check only."""
    s = " ".join(str(text).split())
    out = []
    for m in re.finditer(r"([\d.]+)\s*%", s):
        out.append(float(m.group(1)) * 1000)
    for m in re.finditer(
        r"([\d.]+)\s*(?:cases?|persons?|people|patients?|individuals?|births?)?\s*per\s*([\d ,]+|million|thousand)",
        s, re.I,
    ):
        den = M.DENOM_WORDS.get(m.group(2).lower()) or M._to_float(m.group(2))
        if den:
            out.append(float(m.group(1)) / den * 1e5)
    for m in re.finditer(r"(?:1|one)\s*(?:in|:)\s*([\d ,]+)", s, re.I):
        d = M._to_float(m.group(1))
        if d:
            out.append(1e5 / d)
    for m in re.finditer(r"\b(\d+)\s*/\s*([\d ,]{3,})", s):
        d = M._to_float(m.group(2))
        if d:
            out.append(float(m.group(1)) / d * 1e5)
    return [r for r in out if r > 0]


def tier_for(bare, pop, notes, snippets, fields):
    """CONFIRMED / NO_EVIDENCE / DISAGREE for a percent-converted bare record."""
    rate = fields.get("rate_per_100000")
    if rate is None:
        lo, hi = fields.get("rate_low"), fields.get("rate_high")
        rate = (lo + hi) / 2 if (lo is not None and hi is not None) else lo or hi
    if rate is None:
        return "NO_EVIDENCE"
    evr = evidence_rates(f"{notes} " + " ".join(snippets))
    if not evr:
        return "NO_EVIDENCE"
    if any(max(rate, e) / min(rate, e) <= TOL for e in evr if e > 0):
        return "CONFIRMED"
    return "DISAGREE"


# Auto-convert only low-value rare-disease prevalences. Contamination of the
# prevalence slot (survival rates, staging fractions, fraction-of-category) and
# legitimate-but-high common-disease prevalences both cluster at high percent
# values; routing everything above this to manual review keeps the auto pass
# near-zero-error.
AUTO_MAX_PERCENT = 2.0

REPORT_TIERS = ("CONFIRMED", "CONFIRMED_HIGH", "NO_EVIDENCE", "DISAGREE", "MISPLACED_STAT", "SKIP_GT100")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    report = {t: [] for t in REPORT_TIERS}
    files_changed = 0

    for path in sorted(DISORDERS.glob("*.yaml")):
        with open(path, "r", encoding="utf-8", newline="") as _fh:
            text = _fh.read()  # preserve CRLF/LF; never normalize
        try:
            data = _pyyaml.safe_load(text)
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        prev = data.get("prevalence")
        if not prev:
            continue
        records = prev if isinstance(prev, list) else [prev]

        records_fields = []
        for rec in records:
            if not isinstance(rec, dict):
                continue
            if "percentage" not in rec:
                continue
            # Already resolved (by the migration or a manual fix): keep as-is so
            # the report reflects current state, not a re-derivation from the
            # bare percentage.
            if any(k in rec for k in M.NEW_KEYS):
                records_fields.append({k: rec[k] for k in M.NEW_KEYS if k in rec})
                continue
            pct = rec.get("percentage")
            pop = str(rec.get("population") or "")
            notes = str(rec.get("notes") or "")
            snippets = [e.get("snippet", "") for e in (rec.get("evidence") or []) if isinstance(e, dict)]
            base_fields, flag = M.classify(pct, pop, notes, evidence_snippets=snippets)

            if flag != "AMBIGUOUS_BARE_NUMBER":
                records_fields.append(base_fields)  # unchanged (upsert no-op)
                continue

            pf = percent_fields(str(pct).strip(), pop, snippets)
            if pf is None:
                report["SKIP_GT100"].append((path.name, str(pct)))
                records_fields.append(base_fields)
                continue
            if looks_nonprevalence(notes, pop, snippets):
                report["MISPLACED_STAT"].append((path.name, str(pct), {}, []))
                records_fields.append(base_fields)
                continue
            tier = tier_for(str(pct).strip(), pop, notes, snippets, pf)
            # High-percent CONFIRMED records mix legitimate common-disease
            # prevalences with residual fraction-of-category leaks; route them to
            # manual review instead of auto-converting.
            if tier == "CONFIRMED" and max(_nums(str(pct).strip())) > AUTO_MAX_PERCENT:
                tier = "CONFIRMED_HIGH"
            report[tier].append((path.name, str(pct), pf, evidence_rates(f"{notes} " + " ".join(snippets))[:3]))
            # Only the (low-value) CONFIRMED tier is auto-written.
            records_fields.append(pf if tier == "CONFIRMED" else base_fields)

        if args.apply and any(records_fields):
            new_text, n = M.migrate_text(text, records_fields)
            if n:
                with open(path, "w", encoding="utf-8", newline="") as _fh:
                    _fh.write(new_text)  # write bytes as-is
                files_changed += 1

    write_report(report, args.apply, files_changed)


def write_report(report, applied, files_changed):
    lines = ["# Bare-number prevalence resolution\n"]
    lines.append(f"Mode: {'APPLIED' if applied else 'DRY-RUN'}  ")
    if applied:
        lines.append(f"Files changed: {files_changed}  ")
    for tier in REPORT_TIERS:
        lines.append(f"- {tier}: {len(report[tier])}")
    lines.append("")
    for tier in ("MISPLACED_STAT", "CONFIRMED_HIGH", "DISAGREE", "NO_EVIDENCE"):
        lines.append(f"## {tier} — needs manual review ({len(report[tier])})\n")
        lines.append("| File | percentage | percent-reading /100k | evidence /100k |")
        lines.append("|------|-----------|----------------------|----------------|")
        for item in sorted(report[tier], key=lambda r: (r[0], str(r[1]))):
            fn, pct = item[0], item[1]
            pf = item[2] if len(item) > 2 else {}
            evr = item[3] if len(item) > 3 else []
            rate = pf.get("rate_per_100000") or (pf.get("rate_low"), pf.get("rate_high"))
            lines.append(f"| {fn} | `{pct}` | {rate} | {[round(e,1) for e in evr]} |")
        lines.append("")
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines))
    print(f"{'APPLIED' if applied else 'DRY-RUN'}  files_changed={files_changed}")
    for tier in REPORT_TIERS:
        print(f"  {tier:16s} {len(report[tier])}")
    print(f"Report -> {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
