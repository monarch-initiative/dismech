#!/usr/bin/env python3
"""
Migrate the overloaded prevalence.percentage field to structured slots.

Background
----------
``prevalence.percentage`` was an ``Any`` (float | int | string) field that, in
practice, conflated four independent dimensions in mutually incompatible
notations: the measure type (point prevalence vs incidence vs birth prevalence
vs literature case-count), the rate and its denominator (``%``, ``per 100,000``,
``per million``, ``1 in N``, Orphanet ``N / M`` bands), an uncertainty range, and
a qualitative fallback ("rare", "common"). See
``docs/explanation/design-decisions.md`` (Prevalence remodel).

This migration is **non-destructive**: it leaves ``percentage`` in place (now
schema-``deprecated``) and *adds*, where it can be derived deterministically:

  * ``measure_type``      -> PrevalenceMeasureEnum
  * ``prevalence_class``  -> PrevalenceClassEnum (Orphanet bands + qualitative)
  * ``rate_per_100000``   -> normalized point estimate (cases per 100,000)
  * ``rate_low`` / ``rate_high`` -> normalized range bounds

Genuinely ambiguous records (bare numbers with no unit; free prose head-counts)
are **not** guessed at; they are written to the report flagged for manual review.

Usage
-----
    uv run python scripts/migrate_prevalence.py            # dry-run + report
    uv run python scripts/migrate_prevalence.py --apply    # write YAML in place

The report is written to ``research/prevalence_migration_report.md`` either way.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml as _pyyaml  # read-only parsing; we never re-dump whole files

ROOT = Path(__file__).resolve().parent.parent
DISORDERS = ROOT / "kb" / "disorders"
REPORT = ROOT / "research" / "prevalence_migration_report.md"

# New slots, emitted in schema order immediately before the (now-deprecated)
# `percentage` line of each record. We insert raw text rather than re-dumping the
# whole YAML file: these KB files were not authored by a single YAML emitter, so a
# round-trip rewrite reflows unrelated wrapped scalars and produces thousands of
# lines of spurious churn. Textual insertion keeps the diff purely additive.
NEW_KEYS = ["measure_type", "prevalence_class", "rate_per_100000", "rate_low", "rate_high"]

DENOM_WORDS = {
    "thousand": 1_000,
    "million": 1_000_000,
    "billion": 1_000_000_000,
}

# Qualitative prose -> PrevalenceClassEnum. Order matters (most specific first).
QUAL_PATTERNS = [
    (r"ultra[\s-]?rare", "ULTRA_RARE"),
    (r"extremely rare", "ULTRA_RARE"),
    (r"very rare", "ULTRA_RARE"),
    (r"not yet documented", "NOT_YET_DOCUMENTED"),
    (r"not (?:been )?(?:well[\s-]?)?(?:established|documented)", "NOT_YET_DOCUMENTED"),
    (r"\brare\b", "RARE"),
    (r"\bcommon\b", "COMMON"),
    (r"endemic", "COMMON"),
    (r"\bunknown\b", "UNKNOWN"),
]

CASE_COUNT_RE = re.compile(
    r"reported (?:case|patient|individual|famil|male|affected)"
    r"|documented (?:case|individual|patient)"
    r"|reported affected"
    r"|molecularly characterized"
    r"|reported (?:families|individuals|patients|cases)"
    r"|\bcases worldwide\b"
    r"|fewer than \d+"
    r"|<\s*\d+ reported"
    r"|\d+ reported",
    re.I,
)


def _to_float(token: str) -> float | None:
    """Parse a number with comma/space thousands separators."""
    token = token.strip().replace(",", "").replace(" ", "")
    if not token:
        return None
    try:
        return float(token)
    except ValueError:
        return None


def detect_measure(text: str) -> tuple[str | None, bool]:
    """Return (measure_type, inferred). inferred=True means defaulted, not stated."""
    t = text.lower()
    if "carrier" in t:
        return "CARRIER_FREQUENCY", False
    if CASE_COUNT_RE.search(t):
        return "CASES_IN_LITERATURE", False
    # Any word-boundary "birth" (birth prevalence/cohort/estimate, at birth,
    # live birth, births), "newborn", or "neonat"(al/e/es) signals a
    # birth-denominator measure (neonatal-screening prevalence ~ birth prevalence).
    if re.search(r"\bbirth", t) or "newborn" in t or "neonat" in t:
        return "BIRTH_PREVALENCE", False
    if "point prevalence" in t:
        return "POINT_PREVALENCE", False
    if "lifetime" in t:
        return "LIFETIME_PREVALENCE", False
    if "period prevalence" in t or "five-year" in t or "5-year" in t:
        return "PERIOD_PREVALENCE", False
    if "incidence" in t and "prevalence" not in t:
        return "ANNUAL_INCIDENCE", False
    if "per year" in t or "per annum" in t or "annually" in t or "annual" in t:
        return "ANNUAL_INCIDENCE", False
    return None, True


# Controlled measure-type labels as they appear verbatim in Orphanet structured
# evidence snippets ("N / M | Region | <label> | PMID..."). These are validated
# exact quotes, so matching them is high-precision — unlike free-text notes.
ORPHA_MEASURE_LABELS = [
    ("prevalence at birth", "BIRTH_PREVALENCE"),
    ("annual incidence", "ANNUAL_INCIDENCE"),
    ("lifetime prevalence", "LIFETIME_PREVALENCE"),
    ("period prevalence", "PERIOD_PREVALENCE"),
    ("point prevalence", "POINT_PREVALENCE"),
    ("cases/families in the literature", "CASES_IN_LITERATURE"),
    ("cases in the literature", "CASES_IN_LITERATURE"),
]


def detect_measure_from_evidence(snippets) -> str | None:
    """
    Read the measure type from a controlled Orphanet snippet label, but ONLY when
    it appears as a pipe-delimited table cell (the Orphanet structured-row format
    `N / M | Region | <Measure> | PMID`). Requiring the leading pipe binds the
    label to that row's rate and avoids the multi-measure-prose trap: a free-text
    snippet such as "(prevalence: 1.5/100000) with an annual incidence of
    0.19/100000" names two measures, and a bare substring match would wrongly tag
    the prevalence value as an incidence.
    """
    text = " ".join(str(s) for s in snippets).lower()
    for label, measure in ORPHA_MEASURE_LABELS:
        if re.search(r"\|\s*" + re.escape(label) + r"\b", text):
            return measure
    return None


def _band_from_rate(r: float) -> str:
    """Bucket a per-100,000 rate into an Orphanet-aligned class."""
    r = round(float(r), 6)  # avoid float-boundary artifacts (1e-6*1e5 -> 0.0999...)
    if r >= 100:
        return "ABOVE_1_IN_1000"
    if r >= 10:
        return "BAND_1_5_PER_10000"
    if r >= 1:
        return "BAND_1_9_PER_100000"
    if r >= 0.1:
        return "BAND_1_9_PER_1000000"
    return "BELOW_1_IN_1000000"


def parse_rate(raw: str):
    """
    Parse a numeric occurrence expression -> dict(point, low, high, klass) in
    cases per 100,000, or None if nothing numeric/unit-bearing is recognized.
    """
    s = " ".join(str(raw).split())

    # --- Open-ended bands: ">1 / 1,000", "<1 / 1,000,000", "<1 per 1,000,000",
    #     "Less than 1 per 1,000,000", "more than 1 per 1,000". The bound may use
    #     "/", "per", or ":" and may be written with a comparator OR with words.
    m = re.search(
        r"(?:([<>])|\b(less than|fewer than|under|below)\b|\b(more than|greater than|over|at least)\b)"
        r"\s*([\d.]+)\s*(?:/|per|:)\s*([\d ,]+|million|thousand|billion)",
        s, re.I,
    )
    if m:
        denom = DENOM_WORDS.get((m.group(5) or "").lower()) or _to_float(m.group(5))
        num = _to_float(m.group(4))
        if denom and num is not None:
            rate = num / denom * 1e5
            less = m.group(1) == "<" or bool(m.group(2))
            more = m.group(1) == ">" or bool(m.group(3))
            if less:
                klass = "BELOW_1_IN_1000000" if rate <= 0.1 else _band_from_rate(rate)
                return {"low": None, "high": rate, "point": None, "klass": klass}
            if more:
                klass = "ABOVE_1_IN_1000" if rate >= 100 else _band_from_rate(rate)
                return {"low": rate, "high": None, "point": None, "klass": klass}

    # --- "N / M" or "N-M / M" Orphanet band, integer numerator -------------
    m = re.search(r"\b(\d+)\s*-\s*(\d+)\s*/\s*([\d ,]+)", s)
    if m:
        a, b, denom = _to_float(m.group(1)), _to_float(m.group(2)), _to_float(m.group(3))
        if denom and a is not None and b is not None:
            low, high = a / denom * 1e5, b / denom * 1e5
            return {"low": low, "high": high, "point": None, "klass": _band_from_rate((low + high) / 2)}

    # --- "X per N", "X-Y per N", "X per million", "X/N" (decimal ok) --------
    # Allow an optional unit noun between the number and "per" (e.g. "5-10
    # cases per 100,000", "0.6 patients per million").
    unit_noun = r"(?:\s*(?:cases?|persons?|people|individuals?|patients?|births?|inhabitants?))?"
    m = re.search(
        rf"([\d.]+)\s*(?:-|to)\s*([\d.]+){unit_noun}\s*(?:per|/)\s*([\d ,]+|million|thousand|billion)",
        s, re.I,
    )
    if m:
        a, b = _to_float(m.group(1)), _to_float(m.group(2))
        denom = DENOM_WORDS.get(m.group(3).lower()) or _to_float(m.group(3))
        if denom and a is not None and b is not None:
            low, high = a / denom * 1e5, b / denom * 1e5
            return {"low": low, "high": high, "point": None, "klass": _band_from_rate((low + high) / 2)}
    m = re.search(rf"([\d.]+){unit_noun}\s*(?:per|/)\s*([\d ,]+|million|thousand|billion)", s, re.I)
    if m:
        a = _to_float(m.group(1))
        denom = DENOM_WORDS.get(m.group(2).lower()) or _to_float(m.group(2))
        if denom and a is not None:
            rate = a / denom * 1e5
            return {"low": None, "high": None, "point": rate, "klass": _band_from_rate(rate)}

    # --- "1 in N [to|- N]" ratios (also "one in N") ------------------------
    denoms = [_to_float(x) for x in re.findall(r"(?:1|one)\s*(?:in|:)\s*([\d ,]+)", s, re.I)]
    # pick up a trailing second bound without a repeated "1 in": "1 in 30,000-50,000"
    if len(denoms) == 1:
        tail = re.search(r"(?:1|one)\s*(?:in|:)\s*[\d ,]+\s*(?:-|to)\s*([\d ,]{3,})", s, re.I)
        if tail:
            d2 = _to_float(tail.group(1))
            if d2:
                denoms.append(d2)
    denoms = [d for d in denoms if d]
    if denoms:
        rates = sorted(1e5 / d for d in denoms)
        if len(rates) == 1:
            return {"low": None, "high": None, "point": rates[0], "klass": _band_from_rate(rates[0])}
        return {"low": rates[0], "high": rates[-1], "point": None,
                "klass": _band_from_rate((rates[0] + rates[-1]) / 2)}

    # --- explicit percent: "~11%", "Up to 2%", "0.01-0.05%" ----------------
    m = re.search(r"([\d.]+)\s*(?:-|to)\s*([\d.]+)\s*%", s)
    if m:
        a, b = _to_float(m.group(1)), _to_float(m.group(2))
        if a is not None and b is not None:
            low, high = a * 1000, b * 1000
            return {"low": low, "high": high, "point": None, "klass": _band_from_rate((low + high) / 2)}
    m = re.search(r"([\d.]+)\s*%", s)
    if m:
        a = _to_float(m.group(1))
        if a is not None:
            rate = a * 1000
            if re.search(r"up to|<|under|below", s, re.I):
                return {"low": None, "high": rate, "point": None, "klass": _band_from_rate(rate)}
            return {"low": None, "high": None, "point": rate, "klass": _band_from_rate(rate)}

    return None


def qualitative_class(text: str) -> str | None:
    t = text.lower()
    for pat, klass in QUAL_PATTERNS:
        if re.search(pat, t):
            return klass
    return None


def classify(pct, population: str, notes: str, evidence_snippets=()):
    """
    Returns (fields_dict, flag) where fields_dict holds the new slot values to
    write and flag is a short category string for the report.
    """
    pop = population or ""
    fields: dict = {}

    if pct is None:
        return fields, "NO_PERCENTAGE"

    raw = str(pct).strip()
    # Measure type and qualitative class are detected from the percentage value
    # and the population label ONLY. The free-text `notes` field is deliberately
    # excluded: it routinely mentions "newborn screening", "carrier frequency",
    # or "incidence" as background context, which would otherwise mislabel an
    # ordinary point-prevalence record. Records whose measure lives only in notes
    # fall through to POINT_PREVALENCE (inferred) and are listed for verification.
    measure_text = f"{raw} | {pop}"
    measure, inferred = detect_measure(measure_text)

    numeric = parse_rate(raw)
    if numeric is None:
        # try qualitative prose
        klass = qualitative_class(raw) or qualitative_class(measure_text)
        if klass:
            if measure:
                fields["measure_type"] = measure
            fields["prevalence_class"] = klass
            return fields, "QUALITATIVE"
        # a small literature head-count ("26 reported cases", "approximately 8
        # reported affected individuals from 6 families") => ultra-rare with no
        # population rate.
        if measure == "CASES_IN_LITERATURE":
            fields["measure_type"] = measure
            fields["prevalence_class"] = "ULTRA_RARE"
            return fields, "QUALITATIVE"
        # bare number / range with no unit (incl. scientific notation), or
        # unparseable prose -> ambiguous / needs manual review.
        if re.fullmatch(r"[~<>]?\s*\d[\d.]*(?:[eE][-+]?\d+)?(?:\s*-\s*[\d.]+)?\s*", raw):
            return fields, "AMBIGUOUS_BARE_NUMBER"
        return fields, "UNPARSED_PROSE"

    # numeric recognized. If the value/population gave no measure, fall back to
    # the controlled Orphanet measure label in this record's own (validated-quote)
    # evidence snippet before defaulting to POINT_PREVALENCE. This is
    # high-precision and only applied where a real rate exists (never on
    # Unknown/qualitative records, where a measure_type would be incoherent).
    if not measure:
        ev_measure = detect_measure_from_evidence(evidence_snippets)
        if ev_measure:
            measure, inferred = ev_measure, False
    if measure:
        fields["measure_type"] = measure
    elif inferred:
        measure = "POINT_PREVALENCE"
        fields["measure_type"] = measure
    fields["prevalence_class"] = numeric["klass"]
    if numeric.get("point") is not None:
        fields["rate_per_100000"] = round(numeric["point"], 6)
    if numeric.get("low") is not None:
        fields["rate_low"] = round(numeric["low"], 6)
    if numeric.get("high") is not None:
        fields["rate_high"] = round(numeric["high"], 6)

    flag = "OK"
    if inferred and measure == "POINT_PREVALENCE":
        flag = "OK_MEASURE_INFERRED"
    return fields, flag


def fmt_value(key, value) -> str:
    """Render a field value for textual YAML emission."""
    if key in ("rate_per_100000", "rate_low", "rate_high"):
        v = round(float(value), 6)
        if v == int(v):
            return f"{int(v)}.0"
        return f"{v:.6f}".rstrip("0").rstrip(".")
    return str(value)  # enum tokens are bare scalars


def find_prevalence_block(lines):
    """Return (start, end) line indices of the top-level `prevalence:` block body."""
    start = None
    for i, line in enumerate(lines):
        if re.match(r"^prevalence:\s*$", line):
            start = i + 1
            break
    if start is None:
        return None
    end = len(lines)
    for j in range(start, len(lines)):
        line = lines[j]
        if line and not line[0].isspace() and not line.startswith("-"):
            end = j
            break
    return start, end


def migrate_text(text, records_fields):
    """
    Insert new field lines before each record's `percentage:` line.

    `records_fields` is the per-record fields dict in document order, restricted
    to records that carry a `percentage` key (1:1 with `percentage:` lines in the
    prevalence block). Returns (new_text, n_records_modified) or (text, 0).

    CRLF-safe: a file's existing newline style is detected and reused so a
    CRLF-terminated file is not silently normalized to LF (which would diff the
    whole file).
    """
    newline = "\r\n" if "\r\n" in text else "\n"
    lines = text.split(newline)
    blk = find_prevalence_block(lines)
    if blk is None:
        return text, 0
    start, end = blk

    # Absolute indices of `percentage:` lines within the block, in order.
    pct_line_idxs = [
        i for i in range(start, end) if re.match(r"^\s*percentage:", lines[i])
    ]
    if len(pct_line_idxs) != len(records_fields):
        # Counts disagree (unexpected layout); skip rather than corrupt the file.
        print(
            f"!! percentage-line/record count mismatch "
            f"({len(pct_line_idxs)} lines vs {len(records_fields)} records); skipping",
            file=sys.stderr,
        )
        return text, 0

    insertions = {}  # abs pct-line idx -> list of fresh new-key text lines
    drop = set()      # abs indices of stale new-key lines to remove (upsert)
    new_key_re = re.compile(rf"^\s*(?:{'|'.join(NEW_KEYS)}):")
    modified = 0
    for idx, fields in zip(pct_line_idxs, records_fields):
        indent = lines[idx][: len(lines[idx]) - len(lines[idx].lstrip())]
        # Find any existing new-key lines directly above this percentage line
        # (a prior migration run) so we can replace rather than duplicate them.
        existing = []
        j = idx - 1
        while j >= start and new_key_re.match(lines[j]):
            existing.append(j)
            j -= 1
        old_block = [lines[k] for k in sorted(existing)]
        new_block = [f"{indent}{k}: {fmt_value(k, fields[k])}" for k in NEW_KEYS if k in fields]
        if old_block == new_block:
            continue  # no change
        drop.update(existing)
        if new_block:
            insertions[idx] = new_block
        modified += 1

    if not modified:
        return text, 0

    out = []
    for i, line in enumerate(lines):
        if i in drop:
            continue
        if i in insertions:
            out.extend(insertions[i])
        out.append(line)
    return newline.join(out), modified


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write YAML files in place")
    args = ap.parse_args()

    rows = []
    files_changed = 0

    for path in sorted(DISORDERS.glob("*.yaml")):
        with open(path, "r", encoding="utf-8", newline="") as _fh:
            text = _fh.read()  # preserve CRLF/LF; never normalize
        try:
            data = _pyyaml.safe_load(text)
        except Exception as e:  # noqa
            print(f"!! parse error {path.name}: {e}", file=sys.stderr)
            continue
        if not isinstance(data, dict):
            continue
        prev = data.get("prevalence")
        if not prev:
            continue
        records = prev if isinstance(prev, list) else [prev]

        records_fields = []  # fields for records that carry a `percentage` key
        for rec in records:
            if not isinstance(rec, dict):
                continue
            has_pct_key = "percentage" in rec
            pct = rec.get("percentage")
            pop = rec.get("population")
            notes = rec.get("notes")
            snippets = [
                e.get("snippet", "")
                for e in (rec.get("evidence") or [])
                if isinstance(e, dict)
            ]
            fields, flag = classify(pct, str(pop) if pop is not None else "",
                                    str(notes) if notes is not None else "",
                                    evidence_snippets=snippets)
            rows.append((path.name, pop, pct, fields, flag))
            if has_pct_key:
                records_fields.append(fields)

        if args.apply and records_fields:
            new_text, n = migrate_text(text, records_fields)
            if n:
                with open(path, "w", encoding="utf-8", newline="") as _fh:
                    _fh.write(new_text)  # write bytes as-is
                files_changed += 1

    write_report(rows, applied=args.apply, files_changed=files_changed)


def write_report(rows, applied, files_changed):
    from collections import Counter
    flags = Counter(r[4] for r in rows)
    total = len(rows)

    lines = []
    lines.append("# Prevalence migration report\n")
    lines.append(f"Mode: {'APPLIED (files written)' if applied else 'DRY-RUN (no files written)'}  ")
    lines.append(f"Total prevalence records: **{total}**  ")
    if applied:
        lines.append(f"Files changed: **{files_changed}**  ")
    lines.append("")
    lines.append("## Outcome breakdown\n")
    lines.append("| Flag | Count | Meaning |")
    lines.append("|------|------:|---------|")
    meaning = {
        "OK": "Numeric rate parsed; measure type stated.",
        "OK_MEASURE_INFERRED": "Numeric rate parsed; measure type defaulted to POINT_PREVALENCE (verify).",
        "QUALITATIVE": "No number; mapped to a qualitative prevalence_class.",
        "AMBIGUOUS_BARE_NUMBER": "Bare number/range with no unit — NOT converted, needs manual unit.",
        "UNPARSED_PROSE": "Free prose / head-count not auto-convertible — needs manual review.",
        "NO_PERCENTAGE": "Record had no percentage value; left untouched.",
    }
    for flag, n in flags.most_common():
        lines.append(f"| {flag} | {n} | {meaning.get(flag, '')} |")
    lines.append("")

    # Ambiguous bare numbers: show what they'd become under each interpretation
    # to accelerate manual resolution (the field is *named* percentage, so the
    # percent reading is the most likely intent, but it is not guaranteed).
    sub = sorted(r for r in rows if r[4] == "AMBIGUOUS_BARE_NUMBER")
    if sub:
        lines.append(f"## Records needing manual review — ambiguous bare numbers ({len(sub)})\n")
        lines.append(
            "`percentage` is bare (no unit). Hints show cases/100,000 under each "
            "reading: **as %** (value x1000) vs **as proportion** (value x100,000). "
            "Pick one, then set rate_per_100000/prevalence_class.\n"
        )
        lines.append("| File | population | percentage (raw) | as % -> /100k | as proportion -> /100k |")
        lines.append("|------|------------|------------------|---------------|------------------------|")
        for fname, pop, pct, _fields, _flag in sub:
            first = re.match(r"[~<>]?\s*([\d.]+(?:[eE][-+]?\d+)?)", str(pct))
            if first:
                v = float(first.group(1))
                hint_pct = f"{v * 1000:g}"
                hint_prop = f"{v * 1e5:g}"
            else:
                hint_pct = hint_prop = "?"
            lines.append(f"| {fname} | {str(pop)!r} | {str(pct)!r} | {hint_pct} | {hint_prop} |")
        lines.append("")

    for section, want in [
        ("Records needing manual review — unparsed prose", "UNPARSED_PROSE"),
        ("Measure type inferred (defaulted to POINT_PREVALENCE) — verify", "OK_MEASURE_INFERRED"),
    ]:
        sub = [r for r in rows if r[4] == want]
        if not sub:
            continue
        lines.append(f"## {section} ({len(sub)})\n")
        lines.append("| File | population | percentage (raw) |")
        lines.append("|------|------------|------------------|")
        for fname, pop, pct, _fields, _flag in sorted(sub):
            lines.append(f"| {fname} | {str(pop)!r} | {str(pct)!r} |")
        lines.append("")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines))
    # console summary
    print(f"{'APPLIED' if applied else 'DRY-RUN'}: {total} records")
    for flag, n in flags.most_common():
        print(f"  {flag:24s} {n}")
    print(f"Report -> {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
