#!/usr/bin/env python3
"""Compare dismech's HPOA export against the HPO project's phenotype.hpoa release.

The existing disease-phenotype audits (``kg_phenotype_gap_audit.py`` and its
subsumption refinement) compare *dismech KB content* against HPOA as ingested by
the Monarch KG. This script compares the two **files**: the artifact
``dismech.export.hpoa_export`` writes, and the release
``phenotype.hpoa`` that the HPO project publishes.

Three things are checked, in increasing depth:

1. **Format conformance** -- header block, column names and order, and the value
   space of every column. A value dismech emits that never occurs anywhere in the
   HPO release is a portability risk for consumers, whether or not it is *wrong*.
2. **Disease-level join.** The two files do not share a key: HPOA is anchored on
   OMIM / ORPHA / DECIPHER, dismech on MONDO. The join goes through MONDO's own
   SSSOM mapping set (``skos:exactMatch`` only), so an unmappable dismech disease
   is reported rather than silently dropped. Because HPOA often splits by gene
   where dismech lumps, the join is computed twice: against the disease's own
   mappings, and against its MONDO subtree (``--mondo-obo``).
3. **Annotation-level agreement** on the diseases that do join: exact HP-id
   overlap, plus a subsumption-aware pass over the HP ``is_a`` hierarchy that
   separates granularity differences from genuinely novel dismech annotations.

Inputs are all local files; nothing is fetched. Obtain them with:

    curl -sSL -o phenotype.hpoa \\
      https://github.com/obophenotype/human-phenotype-ontology/releases/latest/download/phenotype.hpoa
    curl -sSL -o hp.obo \\
      https://github.com/obophenotype/human-phenotype-ontology/releases/latest/download/hp.obo
    curl -sSL -o mondo.sssom.tsv \\
      http://purl.obolibrary.org/obo/mondo/mappings/mondo.sssom.tsv
    curl -sSL -o mondo.obo http://purl.obolibrary.org/obo/mondo.obo
    just export-hpoa      # writes output/hpoa/phenotype.dismech.hpoa

Usage:
    uv run python scripts/hpoa_release_compare.py \\
        --dismech output/hpoa/phenotype.dismech.hpoa \\
        --hpo /path/to/phenotype.hpoa \\
        --sssom /path/to/mondo.sssom.tsv \\
        --hp-obo /path/to/hp.obo \\
        --mondo-obo /path/to/mondo.obo \\
        --out-md docs/reports/hpoa-export-vs-hpo-release.md \\
        --out-tsv docs/reports/data/hpoa-export-vs-hpo-release.tsv
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

# The 12 columns of the HPOA format, in order.
HPOA_COLUMNS = [
    "database_id",
    "disease_name",
    "qualifier",
    "hpo_id",
    "reference",
    "evidence",
    "onset",
    "frequency",
    "sex",
    "modifier",
    "aspect",
    "biocuration",
]

# Namespaces the HPO release keys its database_id column on.
HPOA_DISEASE_PREFIXES = ("OMIM", "ORPHA", "DECIPHER")

PERCENT_RE = re.compile(r"^\d+(\.\d+)?%$")
RATIO_RE = re.compile(r"^\d+/\d+$")


def obo_is_a_target(line: str) -> str:
    """The CURIE an ``is_a:`` line points at.

    Both files carry trailing comments (``! label``); mondo.obo additionally
    qualifies most of its is_a lines with a provenance block
    (``is_a: MONDO:0019391 {source="OMIM:227650"} ! Fanconi anemia``). Splitting
    on ``!`` alone leaves the braces attached, which silently produces a parent
    id that matches nothing — 45% of MONDO's is_a edges.
    """
    body = line.split(":", 1)[1].split("!")[0].split("{")[0].strip()
    return body.split()[0] if body else ""


def read_hpoa(path: Path) -> tuple[list[str], list[str], list[dict[str, str]]]:
    """Return (header comment lines, column names, rows) for an HPOA-format file."""
    comments: list[str] = []
    with path.open(encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    idx = 0
    while idx < len(lines) and lines[idx].startswith("#"):
        comments.append(lines[idx])
        idx += 1
    columns = lines[idx].split("\t")
    rows = [
        dict(zip(columns, line.split("\t"), strict=False))
        for line in lines[idx + 1 :]
        if line
    ]
    return comments, columns, rows


def load_mondo_xrefs(path: Path) -> dict[str, set[str]]:
    """MONDO CURIE -> HPOA-namespace disease ids, from SSSOM exactMatch rows only."""
    out: dict[str, set[str]] = defaultdict(set)
    with path.open(encoding="utf-8") as fh:
        rows = csv.DictReader(
            (ln for ln in fh if not ln.startswith("#")), delimiter="\t"
        )
        for row in rows:
            if row.get("predicate_id") != "skos:exactMatch":
                continue
            subject, obj = row.get("subject_id", ""), row.get("object_id", "")
            if not subject.startswith("MONDO:"):
                continue
            # SSSOM writes Orphanet:; the HPO release writes ORPHA:.
            if obj.startswith("Orphanet:"):
                obj = "ORPHA:" + obj.split(":", 1)[1]
            if obj.startswith(HPOA_DISEASE_PREFIXES):
                out[subject].add(obj)
    return out


def load_hp_parents(path: Path) -> dict[str, set[str]]:
    """HP term -> direct is_a parents, parsed from hp.obo."""
    parents: dict[str, set[str]] = defaultdict(set)
    current: str | None = None
    in_term = False
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if line.startswith("["):
                in_term = line == "[Term]"
                current = None
            elif in_term and line.startswith("id: "):
                current = line[4:].strip()
            elif in_term and current and line.startswith("is_a: "):
                target = obo_is_a_target(line)
                if target:
                    parents[current].add(target)
            elif in_term and current and line.startswith("is_obsolete: true"):
                parents.pop(current, None)
                current = None
    return parents


def load_mondo_children(path: Path) -> dict[str, set[str]]:
    """MONDO term -> direct is_a children, parsed from mondo.obo (non-obsolete only)."""
    children: dict[str, set[str]] = defaultdict(set)
    current: str | None = None
    in_term = False
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if line.startswith("["):
                in_term = line == "[Term]"
                current = None
            elif in_term and line.startswith("id: "):
                current = line[4:].strip()
            elif in_term and current and line.startswith("is_a: "):
                parent = obo_is_a_target(line)
                if parent.startswith("MONDO:") and current.startswith("MONDO:"):
                    children[parent].add(current)
            elif in_term and current and line.startswith("is_obsolete: true"):
                current = None
    return children


def descendants(
    term: str, children: dict[str, set[str]], memo: dict[str, set[str]]
) -> set[str]:
    """Transitive is_a descendants of a term (not including the term itself)."""
    if term in memo:
        return memo[term]
    memo[term] = set()  # cycle guard
    out: set[str] = set()
    for child in children.get(term, ()):
        out.add(child)
        out |= descendants(child, children, memo)
    memo[term] = out
    return out


def ancestors(
    term: str, parents: dict[str, set[str]], memo: dict[str, set[str]]
) -> set[str]:
    """Transitive is_a closure of a term (not including the term itself)."""
    if term in memo:
        return memo[term]
    memo[term] = set()  # cycle guard
    out: set[str] = set()
    for parent in parents.get(term, ()):
        out.add(parent)
        out |= ancestors(parent, parents, memo)
    memo[term] = out
    return out


def classify_frequency(value: str) -> str:
    if not value:
        return "(empty)"
    if value.startswith("HP:"):
        return "HP frequency term"
    if PERCENT_RE.match(value):
        return "percentage"
    if RATIO_RE.match(value):
        return "n/m ratio"
    return "other"


def prefix_of(value: str) -> str:
    return (
        value.split(":", 1)[0]
        if ":" in value
        else ("(empty)" if not value else "(no prefix)")
    )


def value_space(rows: list[dict[str, str]], column: str) -> Counter:
    return Counter(row.get(column, "") or "(empty)" for row in rows)


def pct(numerator: float, denominator: float) -> str:
    return f"{100.0 * numerator / denominator:.1f}%" if denominator else "n/a"


def fmt_int(value: int) -> str:
    return f"{value:,}"


def md_table(headers: list[str], rows: list[list[str]]) -> str:
    out = [
        "| " + " | ".join(headers) + " |",
        "|" + "|".join(["---"] * len(headers)) + "|",
    ]
    out += ["| " + " | ".join(row) + " |" for row in rows]
    return "\n".join(out)


def score_join(
    dis_by_disease: dict[str, set[str]],
    hpo_by_disease: dict[str, set[str]],
    join: dict[str, set[str]],
    parents: dict[str, set[str]],
    memo: dict[str, set[str]],
) -> tuple[Counter, list[dict[str, object]]]:
    """Score dismech HP terms against the release, for the diseases in ``join``.

    ``join`` maps a dismech MONDO id to the release disease ids it is compared
    against. Returns (totals, per-disease rows).
    """
    totals: Counter = Counter()
    per_disease: list[dict[str, object]] = []
    for mondo, matched in sorted(join.items()):
        d_terms = dis_by_disease[mondo]
        h_terms: set[str] = set()
        for hid in matched:
            h_terms |= hpo_by_disease[hid]
        overlap = d_terms & h_terms
        h_ancestors: set[str] = set()
        for term in h_terms:
            h_ancestors |= ancestors(term, parents, memo)
        more_specific: set[str] = set()
        more_general: set[str] = set()
        novel: set[str] = set()
        for term in d_terms - overlap:
            if ancestors(term, parents, memo) & h_terms:
                more_specific.add(term)
            elif term in h_ancestors:
                more_general.add(term)
            else:
                novel.add(term)
        totals["dismech"] += len(d_terms)
        totals["exact"] += len(overlap)
        totals["more_specific"] += len(more_specific)
        totals["more_general"] += len(more_general)
        totals["novel"] += len(novel)
        totals["hpo"] += len(h_terms)
        totals["hpo_only"] += len(h_terms - d_terms)
        per_disease.append(
            {
                "mondo_id": mondo,
                "disease_name": dis_names_global.get(mondo, ""),
                "hpoa_ids": ";".join(sorted(matched)),
                "n_dismech": len(d_terms),
                "n_hpoa": len(h_terms),
                "n_exact": len(overlap),
                "n_more_specific": len(more_specific),
                "n_more_general": len(more_general),
                "n_novel": len(novel),
                "n_hpoa_only": len(h_terms - d_terms),
                "novel_terms": ";".join(sorted(novel)),
            }
        )
    return totals, per_disease


def merge_join_rows(
    direct_rows: list[dict[str, object]], subtree_rows: list[dict[str, object]]
) -> list[dict[str, object]]:
    """One row per dismech disease, carrying both joins' scores side by side."""
    by_id: dict[str, dict[str, object]] = {}
    for rows, prefix in ((direct_rows, "direct"), (subtree_rows, "subtree")):
        for row in rows:
            mondo = str(row["mondo_id"])
            merged = by_id.setdefault(
                mondo,
                {
                    "mondo_id": mondo,
                    "disease_name": row["disease_name"],
                    "n_dismech": row["n_dismech"],
                },
            )
            for key, value in row.items():
                if key in ("mondo_id", "disease_name", "n_dismech"):
                    continue
                merged[f"{prefix}_{key}"] = value
    fields = [
        "mondo_id",
        "disease_name",
        "n_dismech",
        *[
            f"{p}_{k}"
            for p in ("direct", "subtree")
            for k in (
                "hpoa_ids",
                "n_hpoa",
                "n_exact",
                "n_more_specific",
                "n_more_general",
                "n_novel",
                "n_hpoa_only",
                "novel_terms",
            )
        ],
    ]
    return [{f: row.get(f, "") for f in fields} for row in by_id.values()]


def agreement_table(totals: Counter) -> str:
    semantic = totals["exact"] + totals["more_specific"] + totals["more_general"]
    return md_table(
        ["Match class", "HP assertions", "% of dismech"],
        [
            [
                "dismech HP assertions on joined diseases",
                fmt_int(totals["dismech"]),
                "100%",
            ],
            [
                "EXACT (same HP id)",
                fmt_int(totals["exact"]),
                pct(totals["exact"], totals["dismech"]),
            ],
            [
                "MORE_SPECIFIC (dismech finer)",
                fmt_int(totals["more_specific"]),
                pct(totals["more_specific"], totals["dismech"]),
            ],
            [
                "MORE_GENERAL (dismech coarser)",
                fmt_int(totals["more_general"]),
                pct(totals["more_general"], totals["dismech"]),
            ],
            [
                "**SEMANTIC overlap**",
                f"**{fmt_int(semantic)}**",
                f"**{pct(semantic, totals['dismech'])}**",
            ],
            [
                "UNMATCHED (novel to dismech)",
                fmt_int(totals["novel"]),
                pct(totals["novel"], totals["dismech"]),
            ],
        ],
    )


def union_value_table(
    d_rows: list[dict[str, str]],
    h_rows: list[dict[str, str]],
    column: str,
    limit: int = 12,
) -> str:
    """Value-space table over the union of values used by either file."""
    d_vals, h_vals = value_space(d_rows, column), value_space(h_rows, column)
    keys = sorted(
        set(d_vals) | set(h_vals),
        key=lambda k: (-d_vals.get(k, 0), -h_vals.get(k, 0), k),
    )
    shown, hidden = keys[:limit], keys[limit:]
    rows = [
        [
            f"`{k}`",
            fmt_int(d_vals.get(k, 0)) if d_vals.get(k) else "**0**",
            pct(d_vals.get(k, 0), len(d_rows)),
            fmt_int(h_vals.get(k, 0)) if h_vals.get(k) else "0",
            pct(h_vals.get(k, 0), len(h_rows)),
        ]
        for k in shown
    ]
    out = md_table(["value", "dismech rows", "%", "HPO rows", "%"], rows)
    if hidden:
        out += f"\n\n…and {len(hidden)} further values used only by the release."
    return out


dis_names_global: dict[str, str] = {}


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument(
        "--dismech", type=Path, default=Path("output/hpoa/phenotype.dismech.hpoa")
    )
    ap.add_argument("--hpo", type=Path, required=True)
    ap.add_argument("--sssom", type=Path, required=True)
    ap.add_argument("--hp-obo", type=Path, required=True)
    ap.add_argument("--mondo-obo", type=Path, help="enables the subtype-inclusive join")
    ap.add_argument("--out-md", type=Path)
    ap.add_argument("--out-tsv", type=Path)
    args = ap.parse_args()

    d_comments, d_columns, d_rows = read_hpoa(args.dismech)
    h_comments, h_columns, h_rows = read_hpoa(args.hpo)
    xrefs = load_mondo_xrefs(args.sssom)
    parents = load_hp_parents(args.hp_obo)
    memo: dict[str, set[str]] = {}

    hpo_version = next(
        (c.split(":", 1)[1].strip() for c in h_comments if c.startswith("#version:")),
        "?",
    )
    dismech_date = next(
        (c.split(":", 1)[1].strip() for c in d_comments if c.startswith("#date:")), "?"
    )

    # --- disease-level index -------------------------------------------------
    hpo_by_disease: dict[str, set[str]] = defaultdict(set)
    for row in h_rows:
        if not row.get("qualifier"):
            hpo_by_disease[row["database_id"]].add(row["hpo_id"])

    dis_by_disease: dict[str, set[str]] = defaultdict(set)
    for row in d_rows:
        dis_names_global.setdefault(row["database_id"], row.get("disease_name", ""))
        if not row.get("qualifier") and row["hpo_id"].startswith("HP:"):
            dis_by_disease[row["database_id"]].add(row["hpo_id"])

    direct_join: dict[str, set[str]] = {}
    mapped_absent: list[str] = []
    unmapped: list[str] = []
    for mondo in sorted(dis_by_disease):
        candidates = xrefs.get(mondo, set())
        present = {c for c in candidates if c in hpo_by_disease}
        if present:
            direct_join[mondo] = present
        elif candidates:
            mapped_absent.append(mondo)
        else:
            unmapped.append(mondo)

    subtree_join: dict[str, set[str]] = {}
    n_subtree_gained = 0
    if args.mondo_obo:
        children = load_mondo_children(args.mondo_obo)
        dmemo: dict[str, set[str]] = {}
        for mondo in sorted(dis_by_disease):
            ids = set(xrefs.get(mondo, set()))
            for child in descendants(mondo, children, dmemo):
                ids |= xrefs.get(child, set())
            present = {i for i in ids if i in hpo_by_disease}
            if present:
                subtree_join[mondo] = present
        n_subtree_gained = len(set(subtree_join) - set(direct_join))

    direct_totals, direct_rows = score_join(
        dis_by_disease, hpo_by_disease, direct_join, parents, memo
    )
    subtree_totals: Counter = Counter()
    subtree_rows: list[dict[str, object]] = []
    if subtree_join:
        subtree_totals, subtree_rows = score_join(
            dis_by_disease, hpo_by_disease, subtree_join, parents, memo
        )
    per_disease = merge_join_rows(direct_rows, subtree_rows)

    # --- strict-parser conformance ------------------------------------------
    bad_disease_prefix = sum(
        1 for r in d_rows if not r["database_id"].startswith(HPOA_DISEASE_PREFIXES)
    )
    bad_hpo_id = sum(1 for r in d_rows if not r["hpo_id"].startswith("HP:"))
    bad_frequency = sum(
        1 for r in d_rows if classify_frequency(r.get("frequency", "")) == "other"
    )
    hpo_ref_prefixes = {prefix_of(r.get("reference", "")) for r in h_rows}
    bad_reference = sum(
        1 for r in d_rows if prefix_of(r.get("reference", "")) not in hpo_ref_prefixes
    )
    self_reference = sum(1 for r in d_rows if r.get("reference") == r["database_id"])

    # --- report --------------------------------------------------------------
    n_dis_diseases = len(dis_by_disease)
    out: list[str] = []
    add = out.append
    add("# dismech HPOA export vs. the HPO project's phenotype.hpoa")
    add("")
    add(f"**Generated:** {dismech_date} · **HPO release compared:** {hpo_version}")
    add(
        "**Regenerate:** see the module docstring of `scripts/hpoa_release_compare.py`."
    )
    add("")
    add(
        "This compares the two **files** — the artifact `just export-hpoa` writes against the "
        "release the HPO project publishes. It is the file-level counterpart of "
        "[`kg-phenotype-gap-audit-2026-07-31.md`](kg-phenotype-gap-audit-2026-07-31.md), which "
        "compares dismech *KB content* against HPOA as ingested by the Monarch KG."
    )
    add("")
    add("## 1. Scale")
    add("")
    add(
        md_table(
            ["", "dismech export", "HPO release"],
            [
                ["Annotation rows", fmt_int(len(d_rows)), fmt_int(len(h_rows))],
                ["Diseases", fmt_int(n_dis_diseases), fmt_int(len(hpo_by_disease))],
                [
                    "Rows per disease (mean)",
                    f"{len(d_rows) / max(n_dis_diseases, 1):.1f}",
                    f"{len(h_rows) / max(len(hpo_by_disease), 1):.1f}",
                ],
                [
                    "Distinct HP terms",
                    fmt_int(
                        len(
                            {
                                r["hpo_id"]
                                for r in d_rows
                                if r["hpo_id"].startswith("HP:")
                            }
                        )
                    ),
                    fmt_int(len({r["hpo_id"] for r in h_rows})),
                ],
                ["Header comment lines", str(len(d_comments)), str(len(h_comments))],
                ["Columns", str(len(d_columns)), str(len(h_columns))],
            ],
        )
    )
    add("")
    add("## 2. Format conformance")
    add("")
    extra_cols = [c for c in d_columns if c not in HPOA_COLUMNS]
    missing_cols = [c for c in HPOA_COLUMNS if c not in d_columns]
    order_ok = d_columns[: len(HPOA_COLUMNS)] == HPOA_COLUMNS
    add(
        f"- First {len(HPOA_COLUMNS)} columns match the HPOA order: "
        f"**{'yes' if order_ok else 'NO'}**"
    )
    add(f"- Extra columns: {', '.join('`' + c + '`' for c in extra_cols) or 'none'}")
    add(
        f"- Missing columns: {', '.join('`' + c + '`' for c in missing_cols) or 'none'}"
    )
    add("")
    add("### Rows a strict HPOA consumer would reject")
    add("")
    add(
        md_table(
            ["Check", "dismech rows", "% of file"],
            [
                [
                    "`database_id` outside OMIM / ORPHA / DECIPHER (all rows are MONDO)",
                    fmt_int(bad_disease_prefix),
                    pct(bad_disease_prefix, len(d_rows)),
                ],
                [
                    "`hpo_id` is not an HP term (synthetic `DISMECH:` CURIE)",
                    fmt_int(bad_hpo_id),
                    pct(bad_hpo_id, len(d_rows)),
                ],
                [
                    "`frequency` is neither an HP term, a percentage, nor n/m (ranges like `30-79%`)",
                    fmt_int(bad_frequency),
                    pct(bad_frequency, len(d_rows)),
                ],
                [
                    "`reference` prefix never used by the release",
                    fmt_int(bad_reference),
                    pct(bad_reference, len(d_rows)),
                ],
                [
                    "`reference` is the row's own disease id (self-citation)",
                    fmt_int(self_reference),
                    pct(self_reference, len(d_rows)),
                ],
            ],
        )
    )
    add("")
    add("### Value spaces")
    add("")
    for column in ["qualifier", "evidence", "aspect", "sex", "onset", "modifier"]:
        if column not in d_columns:
            continue
        add(f"**`{column}`**")
        add("")
        add(union_value_table(d_rows, h_rows, column))
        add("")
    for column, classifier, label in (
        ("frequency", classify_frequency, "form"),
        ("reference", prefix_of, "prefix"),
    ):
        d_vals = Counter(classifier(r.get(column, "")) for r in d_rows)
        h_vals = Counter(classifier(r.get(column, "")) for r in h_rows)
        keys = sorted(
            set(d_vals) | set(h_vals),
            key=lambda k: (-d_vals.get(k, 0), -h_vals.get(k, 0), k),
        )
        add(f"**`{column}`** (by {label})")
        add("")
        add(
            md_table(
                [label, "dismech", "%", "HPO release", "%"],
                [
                    [
                        f"`{k}`",
                        fmt_int(d_vals.get(k, 0)),
                        pct(d_vals.get(k, 0), len(d_rows)),
                        fmt_int(h_vals.get(k, 0)),
                        pct(h_vals.get(k, 0), len(h_rows)),
                    ]
                    for k in keys
                ],
            )
        )
        add("")
    add("## 3. Disease-level join")
    add("")
    add(
        "The two files share no key: the release is anchored on OMIM / ORPHA / DECIPHER, "
        "dismech on MONDO. The join goes through MONDO's own SSSOM `skos:exactMatch` set."
    )
    add("")
    add(
        md_table(
            ["Bucket", "Diseases", "%"],
            [
                [
                    "dismech diseases with ≥1 positive HP row",
                    fmt_int(n_dis_diseases),
                    "100%",
                ],
                [
                    "→ map to a release-namespace id **and** that id is annotated in the release",
                    fmt_int(len(direct_join)),
                    pct(len(direct_join), n_dis_diseases),
                ],
                [
                    "→ map, but the mapped id carries no release annotations",
                    fmt_int(len(mapped_absent)),
                    pct(len(mapped_absent), n_dis_diseases),
                ],
                [
                    "→ no `exactMatch` into OMIM / ORPHA / DECIPHER at all",
                    fmt_int(len(unmapped)),
                    pct(len(unmapped), n_dis_diseases),
                ],
            ],
        )
    )
    add("")
    for label, bucket in (
        ("map to a release id that carries no annotations", mapped_absent),
        ("have no `exactMatch` into a release namespace", unmapped),
    ):
        examples = ", ".join(
            f"{dis_names_global.get(m, m)}"
            for m in sorted(bucket, key=lambda m: -len(dis_by_disease[m]))[:8]
        )
        add("")
        add(f"Largest dismech entries that {label}: {examples}.")
    add("")
    covered = {i for ids in direct_join.values() for i in ids}
    add(
        f"Release diseases dismech does not cover: "
        f"**{fmt_int(len(hpo_by_disease) - len(covered))}** of {fmt_int(len(hpo_by_disease))}."
    )
    if subtree_join:
        add("")
        add(
            f"Allowing a dismech entry to also match its MONDO **subtree** — the lump/split case, "
            f"where the release splits a disease into gene-specific OMIM entries that dismech "
            f"curates as one — joins **{fmt_int(len(subtree_join))}** diseases "
            f"({pct(len(subtree_join), n_dis_diseases)}), {fmt_int(n_subtree_gained)} more than "
            f"the direct join."
        )
    add("")
    add("## 4. Annotation agreement on the joined diseases")
    add("")
    add("**Direct join** (dismech entry ↔ its own `exactMatch` release ids):")
    add("")
    add(agreement_table(direct_totals))
    add("")
    add(
        f"Release HP assertions on the same diseases: **{fmt_int(direct_totals['hpo'])}**, of which "
        f"**{fmt_int(direct_totals['hpo_only'])}** "
        f"({pct(direct_totals['hpo_only'], direct_totals['hpo'])}) are absent from dismech."
    )
    if subtree_totals:
        add("")
        add("**Subtype-inclusive join** (also matching the entry's MONDO subtree):")
        add("")
        add(agreement_table(subtree_totals))
        add("")
        add(
            f"Release HP assertions on the same diseases: **{fmt_int(subtree_totals['hpo'])}**, of "
            f"which **{fmt_int(subtree_totals['hpo_only'])}** "
            f"({pct(subtree_totals['hpo_only'], subtree_totals['hpo'])}) are absent from dismech."
        )
    add("")
    ranked = subtree_rows or direct_rows
    top_novel = sorted(ranked, key=lambda d: -int(d["n_novel"]))[:15]
    add(
        "### Diseases contributing the most novel dismech annotations"
        + (" (subtype-inclusive join)" if subtree_rows else " (direct join)")
    )
    add("")
    add(
        md_table(
            [
                "Disease",
                "MONDO",
                "release id(s)",
                "dismech",
                "release",
                "exact",
                "novel",
            ],
            [
                [
                    str(d["disease_name"])[:44],
                    str(d["mondo_id"]),
                    str(d["hpoa_ids"])[:24],
                    fmt_int(int(d["n_dismech"])),
                    fmt_int(int(d["n_hpoa"])),
                    fmt_int(int(d["n_exact"])),
                    fmt_int(int(d["n_novel"])),
                ]
                for d in top_novel
            ],
        )
    )
    add("")

    report = "\n".join(out) + "\n"
    if args.out_md:
        args.out_md.parent.mkdir(parents=True, exist_ok=True)
        args.out_md.write_text(report, encoding="utf-8")
        print(f"wrote {args.out_md}")
    else:
        print(report)

    if args.out_tsv and per_disease:
        args.out_tsv.parent.mkdir(parents=True, exist_ok=True)
        with args.out_tsv.open("w", encoding="utf-8", newline="") as fh:
            writer = csv.DictWriter(
                fh, fieldnames=list(per_disease[0].keys()), delimiter="\t"
            )
            writer.writeheader()
            writer.writerows(
                sorted(
                    per_disease,
                    key=lambda d: (
                        -int(d.get("subtree_n_novel") or d.get("direct_n_novel") or 0)
                    ),
                )
            )
        print(f"wrote {args.out_tsv} ({len(per_disease)} rows)")


if __name__ == "__main__":
    main()
