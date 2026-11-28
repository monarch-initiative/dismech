#!/usr/bin/env python3
"""Tally every findings file of a module-review run.

    uv run python experiments/module_review/aggregate.py experiments/module_review/2026-11-28

Reads ``findings/<batch>.json``, ``facts/modules.json`` and ``batches.yaml`` and
writes three derived views, none of which is edited by hand:

- ``tally.md``: coverage, counts, the ranked module table, every HIGH finding
  and every cross-module finding;
- ``reports/<batch>.md``: each batch's findings as readable text;
- ``findings.tsv``: one row per finding, for sorting and filtering.

A findings file that fails ``validate_findings.py`` is reported and left out of
the counts, so a number here always comes from a file that met the contract.
"""

from __future__ import annotations

import collections
import csv
import json
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from validate_findings import validate

SEV_ORDER = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
VERDICT_ORDER = ["RESTRUCTURE", "MAJOR_ISSUES", "MINOR_ISSUES", "SOUND"]


def one_line(text: str | None) -> str:
    return " ".join((text or "").split()).replace("|", "\\|")


def main(run_dir: str) -> int:
    run = Path(run_dir)
    batches = yaml.safe_load((run / "batches.yaml").read_text())["batches"]
    facts = json.loads((run / "facts" / "modules.json").read_text())
    reports_dir = run / "reports"
    reports_dir.mkdir(exist_ok=True)

    modules, cross, rows, status = {}, [], [], []
    for batch in batches:
        bid = batch["id"]
        path = run / "findings" / f"{bid}.json"
        if not path.exists():
            status.append(
                (bid, batch["theme"], len(batch["modules"]), 0, "not started")
            )
            continue
        errors, _, _ = validate(run_dir, bid, partial=True)
        doc = json.loads(path.read_text())
        done = [m["module"] for m in doc.get("modules") or []]
        if errors:
            status.append(
                (
                    bid,
                    batch["theme"],
                    len(batch["modules"]),
                    len(done),
                    f"INVALID ({len(errors)} errors)",
                )
            )
            continue
        state = "complete" if set(done) >= set(batch["modules"]) else "in progress"
        status.append((bid, batch["theme"], len(batch["modules"]), len(done), state))
        for entry in doc.get("modules") or []:
            entry["batch"] = bid
            modules[entry["module"]] = entry
            for f in entry.get("findings") or []:
                rows.append({"batch": bid, "module": entry["module"], **f})
        for f in doc.get("cross_module_findings") or []:
            cross.append({"batch": bid, **f})
        write_batch_report(reports_dir / f"{bid}.md", batch, doc)

    write_tsv(run / "findings.tsv", rows, cross)
    write_tally(run / "tally.md", batches, status, modules, rows, cross, facts)
    total = sum(len(b["modules"]) for b in batches)
    print(
        f"{len(modules)}/{total} modules reviewed; {len(rows)} findings; {len(cross)} cross-module findings"
    )
    return 0


def write_batch_report(path: Path, batch: dict, doc: dict) -> None:
    out = [
        f"# {batch['id']}: {batch['theme']}",
        "",
        f"Reviewer session: `{doc.get('reviewer')}`. Commit reviewed: `{doc.get('reviewed_commit')}`.",
        "",
    ]
    if doc.get("limitations"):
        out += [
            "**Limits stated by the reviewer.** "
            + " ".join(doc["limitations"].split()),
            "",
        ]
    for entry in doc.get("modules") or []:
        s = entry.get("scores") or {}
        out += [
            f"## {entry['module']}",
            "",
            (
                f"**{entry.get('verdict')}** · logic {s.get('logic')} · biology {s.get('biology')} · "
                f"utility {s.get('utility')} · coherence {s.get('coherence')}"
            ),
            "",
            " ".join((entry.get("summary") or "").split()),
            "",
        ]
        if entry.get("strengths"):
            out += [
                "Strengths: "
                + "; ".join(" ".join(x.split()) for x in entry["strengths"]),
                "",
            ]
        for f in sorted(
            entry.get("findings") or [],
            key=lambda x: SEV_ORDER.get(x.get("severity"), 9),
        ):
            out += finding_block(f)
        if not entry.get("findings"):
            out += ["No findings.", ""]
    if doc.get("cross_module_findings"):
        out += ["## Cross-module findings", ""]
        for f in sorted(
            doc["cross_module_findings"],
            key=lambda x: SEV_ORDER.get(x.get("severity"), 9),
        ):
            out += [
                f"### {f['id']} · {f.get('severity')} · {f.get('category')} · confidence {f.get('confidence')}",
                "",
                "Modules: " + ", ".join(f"`{m}`" for m in f.get("modules") or []),
                "",
                "**Problem.** " + " ".join((f.get("problem") or "").split()),
                "",
                "**Suggestion.** " + " ".join((f.get("suggestion") or "").split()),
                "",
                "**Checked by.** " + " ".join((f.get("verification") or "").split()),
                "",
            ]
    path.write_text("\n".join(out) + "\n")


def finding_block(f: dict) -> list[str]:
    block = [
        f"### {f['id']} · {f.get('severity')} · {f.get('dimension')} / {f.get('category')} · confidence {f.get('confidence')}",
        "",
        f"Where: {f.get('location')}",
        "",
    ]
    if f.get("quote"):
        block += ["> " + " ".join(f["quote"].split()), ""]
    block += [
        "**Problem.** " + " ".join((f.get("problem") or "").split()),
        "",
        "**Suggestion.** " + " ".join((f.get("suggestion") or "").split()),
        "",
        "**Checked by.** " + " ".join((f.get("verification") or "").split()),
        "",
    ]
    if f.get("related_modules"):
        block += ["Related: " + ", ".join(f"`{m}`" for m in f["related_modules"]), ""]
    return block


def write_tsv(path: Path, rows: list[dict], cross: list[dict]) -> None:
    cols = [
        "batch",
        "module",
        "id",
        "severity",
        "dimension",
        "category",
        "confidence",
        "location",
        "problem",
        "suggestion",
        "verification",
        "quote",
        "related_modules",
    ]
    with path.open("w", newline="") as fh:
        writer = csv.writer(fh, delimiter="\t", lineterminator="\n")
        writer.writerow(cols)
        ordered = sorted(
            rows,
            key=lambda r: (
                SEV_ORDER.get(r.get("severity"), 9),
                r["batch"],
                r["module"],
                r.get("id", ""),
            ),
        )
        for r in ordered:
            writer.writerow(
                [
                    " ".join(
                        str(
                            ", ".join(r[c])
                            if isinstance(r.get(c), list)
                            else (r.get(c) or "")
                        ).split()
                    )
                    for c in cols
                ]
            )
        for r in sorted(
            cross, key=lambda r: (SEV_ORDER.get(r.get("severity"), 9), r.get("id", ""))
        ):
            writer.writerow(
                [
                    r["batch"],
                    ", ".join(r.get("modules") or []),
                    r.get("id"),
                    r.get("severity"),
                    "CROSS_MODULE",
                    r.get("category"),
                    r.get("confidence"),
                    "",
                    " ".join((r.get("problem") or "").split()),
                    " ".join((r.get("suggestion") or "").split()),
                    " ".join((r.get("verification") or "").split()),
                    "",
                    "",
                ]
            )


def write_tally(path, batches, status, modules, rows, cross, facts) -> None:
    total = sum(len(b["modules"]) for b in batches)
    out = [
        "# Module review tally",
        "",
        "Generated by `aggregate.py` from the findings files. Do not edit; rerun the script.",
        "",
        f"**{len(modules)} of {total} modules reviewed**, {len(rows)} per-module findings, {len(cross)} cross-module findings.",
        "",
        "## Coverage",
        "",
        "| Batch | Theme | Modules | Reviewed | State |",
        "|---|---|---|---|---|",
    ]
    out += [
        f"| [{b}](reports/{b}.md) | {t} | {n} | {d} | {s} |" for b, t, n, d, s in status
    ]

    sev = collections.Counter(r.get("severity") for r in rows)
    dim = collections.Counter((r.get("dimension"), r.get("severity")) for r in rows)
    out += [
        "",
        "## Findings by dimension and severity",
        "",
        "| Dimension | HIGH | MEDIUM | LOW | Total |",
        "|---|---|---|---|---|",
    ]
    for d in ("LOGIC", "BIOLOGY", "UTILITY", "COHERENCE"):
        counts = [dim[(d, s)] for s in ("HIGH", "MEDIUM", "LOW")]
        out.append(f"| {d} | {counts[0]} | {counts[1]} | {counts[2]} | {sum(counts)} |")
    out.append(
        f"| **All** | {sev['HIGH']} | {sev['MEDIUM']} | {sev['LOW']} | {len(rows)} |"
    )
    csev = collections.Counter(r.get("severity") for r in cross)
    out.append(
        f"| Cross-module | {csev['HIGH']} | {csev['MEDIUM']} | {csev['LOW']} | {len(cross)} |"
    )

    cat = collections.Counter((r.get("dimension"), r.get("category")) for r in rows)
    high_cat = collections.Counter(
        (r.get("dimension"), r.get("category"))
        for r in rows
        if r.get("severity") == "HIGH"
    )
    out += [
        "",
        "## Findings by category",
        "",
        "| Dimension | Category | Findings | of which HIGH |",
        "|---|---|---|---|",
    ]
    out += [
        f"| {d} | {c} | {n} | {high_cat[(d, c)]} |" for (d, c), n in cat.most_common()
    ]

    verdicts = collections.Counter(m.get("verdict") for m in modules.values())
    out += ["", "## Verdicts", "", "| Verdict | Modules |", "|---|---|"]
    out += [f"| {v} | {verdicts[v]} |" for v in VERDICT_ORDER]

    out += [
        "",
        "## Modules, worst first",
        "",
        "Sorted by verdict, then by the sum of the four scores (lower is worse). Conformers are `conforms_to` links into the module.",
        "",
        "| Module | Batch | Verdict | Logic | Biology | Utility | Coherence | HIGH | MED | LOW | Conformer links | Summary |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    per_module = collections.defaultdict(collections.Counter)
    for r in rows:
        per_module[r["module"]][r.get("severity")] += 1

    def rank(item):
        stem, m = item
        s = m.get("scores") or {}
        return (
            VERDICT_ORDER.index(m["verdict"])
            if m.get("verdict") in VERDICT_ORDER
            else 9,
            sum(s.values()) if s else 99,
            stem,
        )

    for stem, m in sorted(modules.items(), key=rank):
        s, c = m.get("scores") or {}, per_module[stem]
        links = (facts.get(stem) or {}).get("conformers", {}).get("links", "?")
        out.append(
            f"| `{stem}` | [{m['batch']}](reports/{m['batch']}.md) | {m.get('verdict')} | {s.get('logic')} | {s.get('biology')} | "
            f"{s.get('utility')} | {s.get('coherence')} | {c['HIGH']} | {c['MEDIUM']} | {c['LOW']} | {links} | {one_line(m.get('summary'))} |"
        )

    out += [
        "",
        "## HIGH findings",
        "",
        "| Finding | Module | Dimension / category | Confidence | Problem | Suggestion |",
        "|---|---|---|---|---|---|",
    ]
    for r in sorted(
        (r for r in rows if r.get("severity") == "HIGH"),
        key=lambda r: (r["batch"], r["module"], r.get("id", "")),
    ):
        out.append(
            f"| {r.get('id')} | `{r['module']}` | {r.get('dimension')} / {r.get('category')} | {r.get('confidence')} | "
            f"{one_line(r.get('problem'))} | {one_line(r.get('suggestion'))} |"
        )

    out += [
        "",
        "## Cross-module findings",
        "",
        "| Finding | Severity | Category | Modules | Confidence | Problem | Suggestion |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in sorted(
        cross, key=lambda r: (SEV_ORDER.get(r.get("severity"), 9), r.get("id", ""))
    ):
        out.append(
            f"| {r.get('id')} | {r.get('severity')} | {r.get('category')} | {', '.join(f'`{m}`' for m in r.get('modules') or [])} | "
            f"{r.get('confidence')} | {one_line(r.get('problem'))} | {one_line(r.get('suggestion'))} |"
        )
    path.write_text("\n".join(out) + "\n")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
