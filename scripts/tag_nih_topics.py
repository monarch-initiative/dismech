#!/usr/bin/env python3
"""Bulk-tag disease entries with NIH Highlighted-Topic funding priorities.

This applies the *secondary* ``classifications.nih_research_priority``
classification (see docs/nih-research-priorities.md) using STRUCTURAL signals
already present in the KB — currently ``conforms_to`` module edges — so every
tag is mechanism-grounded and auditable, not keyword-guessed.

Only rules with an unambiguous structural signal are encoded. Topics that need
per-entry human judgement (e.g. rare-cancer status, pediatric onset, broad
autoimmune scope) are deliberately NOT auto-applied.

The script is idempotent: an entry that already carries the topic tag is left
unchanged. Formatting is preserved via ruamel round-trip.

Usage:
    python scripts/tag_nih_topics.py --dry-run   # report what would change
    python scripts/tag_nih_topics.py             # apply
"""

from __future__ import annotations

import argparse
import io
import re
from pathlib import Path

from ruamel.yaml import YAML

ROOT = Path(__file__).resolve().parent.parent
DISORDERS = ROOT / "kb" / "disorders"

# --- Rules -----------------------------------------------------------------
# Each rule tags entries whose pathophysiology conforms to any of `modules`
# with `topic`. `label` names each module for the generated note. Extend this
# table (or add new topic rules) as new structural signals become defensible.
AGING_HALLMARK_MODULES = {
    "cellular_senescence": "cellular senescence",
    "senescence_tumor_suppression": "senescence-mediated tumor suppression",
    "genomic_instability_aging": "genomic instability",
    "inflammaging": "inflammaging",
    "telomere_attrition": "telomere attrition",
    "loss_of_proteostasis": "loss of proteostasis",
}

RULES = [
    {
        "topic": "NIH_HT_89_cellular_quiescence_senescence_cell_death_in",
        "modules": AGING_HALLMARK_MODULES,
        "note": (
            "Pathophysiology conforms to the {modules} module(s) — "
            "senescence / hallmark-of-aging mechanism(s) — making this entry a "
            "relevant model for NIH Highlighted Topic 89 (cellular quiescence, "
            "senescence, and cell death in aging and disease)."
        ),
    },
]

_CONFORMS_RE = re.compile(r'conforms_to:\s*"?([a-zA-Z_]+)#')


def _matched_modules(text: str, module_labels: dict[str, str]) -> list[str]:
    found = {m for m in _CONFORMS_RE.findall(text) if m in module_labels}
    # Preserve the rule's declared order for a stable, readable note.
    return [module_labels[m] for m in module_labels if m in found]


def _existing_topics(classifications) -> set[str]:
    if not classifications:
        return set()
    out = set()
    for assign in classifications.get("nih_research_priority") or []:
        if isinstance(assign, dict) and assign.get("classification_value"):
            out.add(str(assign["classification_value"]))
    return out


def process(path: Path, apply: bool) -> list[str]:
    """Return a list of human-readable change descriptions for one file."""
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.width = 4096
    text = path.read_text()
    changes: list[str] = []

    pending = []  # (topic, note) to add
    for rule in RULES:
        labels = _matched_modules(text, rule["modules"])
        if not labels:
            continue
        pending.append((rule, labels))

    if not pending:
        return changes

    data = yaml.load(text)
    classifications = data.get("classifications")
    made_change = False
    for rule, labels in pending:
        topic = rule["topic"]
        if topic in _existing_topics(classifications):
            continue
        if classifications is None:
            classifications = {}
            data["classifications"] = classifications
        assignments = classifications.get("nih_research_priority")
        if assignments is None:
            assignments = []
            classifications["nih_research_priority"] = assignments
        modules_phrase = _join(labels)
        assignments.append({
            "classification_value": topic,
            "notes": rule["note"].format(modules=modules_phrase),
        })
        changes.append(f"{path.stem}: +{topic} (via {modules_phrase})")
        made_change = True

    if made_change and apply:
        buf = io.StringIO()
        yaml.dump(data, buf)
        path.write_text(buf.getvalue())
    return changes


def _join(items: list[str]) -> str:
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} and {items[1]}"
    return ", ".join(items[:-1]) + f", and {items[-1]}"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="Report without writing.")
    args = ap.parse_args()

    all_changes: list[str] = []
    for path in sorted(DISORDERS.glob("*.yaml")):
        all_changes.extend(process(path, apply=not args.dry_run))

    verb = "Would tag" if args.dry_run else "Tagged"
    print(f"{verb} {len(all_changes)} entr{'y' if len(all_changes) == 1 else 'ies'}:")
    for line in all_changes:
        print(f"  {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
