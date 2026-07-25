#!/usr/bin/env python3
"""Generate the NIHResearchPriorityEnum LinkML classification module.

Reads the dated snapshot in ``data/nih_highlighted_topics/topics.tsv`` (the NIH
"Highlighted Topics" funding-priority list) and emits
``src/dismech/schema/classifications/nih_research_priorities.yaml``.

This is a *secondary* classification: a soft, multivalued tag recording which NIH
highlighted funding topic(s) a disease entry or curation project is relevant to.
It is NOT a primary nosology.

The NIH topics are transient (each carries a ~2-year expiration). To refresh:
re-scrape the topic pages, update ``topics.tsv`` + ``MANIFEST.yaml``, then rerun
this script. Do NOT hand-edit the generated YAML.

Usage:
    python scripts/gen_nih_topics_enum.py            # write the enum
    python scripts/gen_nih_topics_enum.py --check    # fail if out of date
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TSV = ROOT / "data" / "nih_highlighted_topics" / "topics.tsv"
MANIFEST = ROOT / "data" / "nih_highlighted_topics" / "MANIFEST.yaml"
OUT = ROOT / "src" / "dismech" / "schema" / "classifications" / "nih_research_priorities.yaml"
TOPIC_URL = "https://grants.nih.gov/funding/find-a-fit-for-your-research/highlighted-topics"

# A handful of common ASCII substitutions so keys stay clean.
_TRANSLIT = {
    "‘": "'", "’": "'", "“": '"', "”": '"',
    "–": "-", "—": "-", "…": "",
}


def _clean(text: str) -> str:
    for bad, good in _TRANSLIT.items():
        text = text.replace(bad, good)
    return re.sub(r"\s+", " ", text).strip()


def _slug(title: str, max_words: int = 6) -> str:
    """Short, stable, lower-snake slug from the leading words of a title."""
    words = re.sub(r"[^a-z0-9]+", " ", _clean(title).lower()).split()
    # Drop leading filler verbs that add no discriminating value.
    filler = {"advancing", "accelerating", "enhancing", "research", "on", "the",
              "a", "of", "for", "and", "into", "using", "toward", "understanding",
              "developing", "supporting", "strengthening"}
    kept = [w for w in words if w not in filler] or words
    return "_".join(kept[:max_words])


def _read_snapshot_date() -> str:
    if MANIFEST.exists():
        for line in MANIFEST.read_text().splitlines():
            m = re.match(r'\s*snapshot_date:\s*"?([0-9-]+)"?', line)
            if m:
                return m.group(1)
    return "unknown"


def _yaml_dq(text: str) -> str:
    """Double-quoted YAML scalar."""
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def build() -> str:
    rows = list(csv.DictReader(TSV.open(encoding="utf-8"), delimiter="\t"))
    snapshot = _read_snapshot_date()

    lines: list[str] = []
    lines.append(
        "id: https://w3id.org/monarch-initiative/dismech/classifications/nih_research_priorities"
    )
    lines.append("name: dismech-nih-research-priorities")
    lines.append("title: NIH Highlighted Funding Topic Classification")
    lines.append("description: >-")
    lines.append(
        "  Secondary, non-primary classification tagging a disease entry or curation"
    )
    lines.append(
        "  project with the NIH \"Highlighted Topics\" funding-priority area(s) it is"
    )
    lines.append(
        "  relevant to. This captures grant-strategy relevance, NOT disease nosology, so"
    )
    lines.append(
        "  an entry may carry several tags or none. The topics are transient (each"
    )
    lines.append(
        "  expires ~2 years after posting); this enum is GENERATED from a dated snapshot"
    )
    lines.append(
        f"  ({snapshot}) by scripts/gen_nih_topics_enum.py -- do not hand-edit."
    )
    lines.append("")
    lines.append("imports:")
    lines.append("  - linkml:types")
    lines.append("")
    lines.append("prefixes:")
    lines.append("  linkml: https://w3id.org/linkml/")
    lines.append("  dismech: https://w3id.org/monarch-initiative/dismech/")
    lines.append("")
    lines.append("default_prefix: dismech")
    lines.append("")
    lines.append("enums:")
    lines.append("  NIHResearchPriorityEnum:")
    lines.append("    description: >-")
    lines.append(
        "      NIH Highlighted Topics funding-priority areas. Tag entries/projects with"
    )
    lines.append(
        "      the topic(s) whose research goals they advance. Snapshot: " + snapshot + "."
    )
    lines.append("    permissible_values:")

    seen: set[str] = set()
    for row in rows:
        num = row["topic_number"].strip()
        title = _clean(row["title"])
        exp = _clean(row.get("expiration_date", ""))
        key = f"NIH_HT_{num}_{_slug(title)}"
        # Guard against slug collisions (keep keys unique).
        base, i = key, 2
        while key in seen:
            key = f"{base}_{i}"
            i += 1
        seen.add(key)
        desc = f"{title} (NIH Highlighted Topic {num}"
        if exp:
            desc += f"; expires {exp}"
        desc += f"). {TOPIC_URL}/{num}"
        lines.append(f"      {key}:")
        lines.append(f"        description: {_yaml_dq(desc)}")

    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="Exit non-zero if the generated file is out of date.")
    args = ap.parse_args()

    content = build()
    if args.check:
        current = OUT.read_text() if OUT.exists() else ""
        if current != content:
            print(f"OUT OF DATE: {OUT.relative_to(ROOT)} "
                  f"differs from generator output. Run: python {Path(__file__).name}",
                  file=sys.stderr)
            return 1
        print(f"OK: {OUT.relative_to(ROOT)} is up to date.")
        return 0

    OUT.write_text(content)
    n = content.count("      NIH_HT_")
    print(f"Wrote {OUT.relative_to(ROOT)} with {n} topics.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
