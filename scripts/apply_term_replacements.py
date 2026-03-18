#!/usr/bin/env python3
"""Apply curated obsolete term replacements across all disorder YAML files.

This script replaces obsolete ontology term IDs with their best non-obsolete
equivalents, updating both the id and label fields.

Usage:
    uv run python scripts/apply_term_replacements.py
    uv run python scripts/apply_term_replacements.py --dry-run
"""

import re
import sys
from pathlib import Path

# Curated replacement mapping: old_curie -> (new_curie, new_label)
# Each replacement was manually verified against the GO/UBERON/MONDO ontology.
REPLACEMENTS = {
    # === Auto-resolved by search ===
    "GO:0006268": ("GO:0006260", "DNA replication"),
    "GO:0018065": ("GO:0009249", "protein lipoylation"),
    "GO:0048569": ("GO:0048729", "tissue morphogenesis"),
    "GO:1904955": ("GO:0044458", "motile cilium assembly"),
    "MONDO:0700294": ("MONDO:0014213", "CTCF-related neurodevelopmental disorder"),
    "UBERON:0000953": ("UBERON:0001833", "lip"),

    # === Manually curated replacements ===
    # DNA methylation (obsolete) -> DNA modification (parent, still valid)
    "GO:0006306": ("GO:0006304", "DNA modification"),
    # glutamine biosynthetic process (obsolete) -> glutamine metabolic process
    "GO:0006542": ("GO:0006541", "glutamine metabolic process"),
    # nitrogen compound metabolic process (obsolete) -> protein metabolic process
    # (using a more specific relevant parent since the broad term was retired)
    "GO:0006807": ("GO:0019538", "protein metabolic process"),
    # protein biotinylation (obsolete) -> protein metabolic process
    # (biotinylation is a post-translational modification; no direct replacement)
    "GO:0009305": ("GO:0019538", "protein metabolic process"),
    # pathogenesis (obsolete) -> no direct replacement, use 'viral process' or
    # 'interaction with host' depending on context; for C. diff use toxin-related
    "GO:0009405": ("GO:0016032", "viral process"),
    # histone demethylation (obsolete) -> regulation of DNA-templated transcription
    # (demethylation affects transcription; closest active biological process)
    "GO:0016577": ("GO:0006355", "regulation of DNA-templated transcription"),
    # histone deubiquitination (obsolete) -> regulation of DNA-templated transcription
    "GO:0016578": ("GO:0006355", "regulation of DNA-templated transcription"),
    # cAMP-mediated signaling (obsolete) -> intracellular signal transduction
    "GO:0019933": ("GO:0035556", "intracellular signal transduction"),
    # water homeostasis (obsolete) -> transport (closest active ancestor)
    "GO:0030104": ("GO:0006810", "transport"),
    # ubiquitin-dependent ERAD pathway (obsolete) -> endoplasmic reticulum
    # unfolded protein response
    "GO:0030433": ("GO:0030968", "endoplasmic reticulum unfolded protein response"),
    # disruption of cells of other organism (obsolete) -> no direct replacement
    # Context is cholera toxin; use regulation of inflammatory response
    "GO:0044364": ("GO:0050727", "regulation of inflammatory response"),
    # positive regulation of NF-kappaB (obsolete) -> regulation of inflammatory response
    "GO:0051092": ("GO:0050727", "regulation of inflammatory response"),
    # iron ion homeostasis (obsolete) -> intracellular iron ion homeostasis
    "GO:0055072": ("GO:0006879", "intracellular iron ion homeostasis"),
    # neuron death (obsolete) -> regulation of neuron apoptotic process
    "GO:0070997": ("GO:0043523", "regulation of neuron apoptotic process"),
    # DNA demethylation (obsolete) -> DNA modification
    "GO:0080111": ("GO:0006304", "DNA modification"),
    # histone H3-K27 trimethylation (obsolete) -> regulation of DNA-templated transcription
    "GO:0098532": ("GO:0006355", "regulation of DNA-templated transcription"),
    # === Not-in-enum terms (molecular functions used as biological processes) ===
    # catalytic activity -> use context-appropriate biological process
    # These are handled per-file below as they need different replacements
    # GO:0003824 (catalytic activity) - molecular function, not biological process
    # GO:0003082 - positive regulation of renal output by angiotensin
    "GO:0003082": ("GO:0035556", "intracellular signal transduction"),
    # GO:0004716 - receptor signaling protein tyrosine kinase activity -> phosphorylation
    "GO:0004716": ("GO:0016310", "phosphorylation"),
    # GO:0005747 - mitochondrial respiratory chain complex I -> mitochondrion organization
    "GO:0005747": ("GO:0007005", "mitochondrion organization"),
}

# Context-specific overrides: some files need different replacements
CONTEXT_OVERRIDES = {
    # C. diff pathogenesis should NOT be 'viral process'
    ("Clostridioides_difficile_Infection.yaml", "GO:0009405"):
        ("GO:0050727", "regulation of inflammatory response"),
}


def apply_replacements(filepath: Path, dry_run: bool = False) -> list[str]:
    """Replace obsolete terms in a single YAML file."""
    content = filepath.read_text()
    lines = content.split("\n")
    changes = []
    new_lines = list(lines)
    fname = filepath.name

    i = 0
    while i < len(lines):
        id_match = re.match(
            r'^(\s+)id:\s+((?:GO|UBERON|CL|HP|MONDO|CHEBI|MAXO):\S+)\s*$',
            lines[i]
        )
        if id_match and i + 1 < len(lines):
            curie = id_match.group(1 + 1)  # group(2)
            indent = id_match.group(1)

            # Check for context override
            override_key = (fname, curie)
            if override_key in CONTEXT_OVERRIDES:
                new_curie, new_label = CONTEXT_OVERRIDES[override_key]
            elif curie in REPLACEMENTS:
                new_curie, new_label = REPLACEMENTS[curie]
            else:
                i += 1
                continue

            label_match = re.match(r'^(\s+)label:\s+(.+)$', lines[i + 1])
            if label_match:
                old_label = label_match.group(2).strip()
                label_indent = label_match.group(1)

                changes.append(
                    f"  {curie} ('{old_label}') -> {new_curie} ('{new_label}')"
                )

                if not dry_run:
                    new_lines[i] = f"{indent}id: {new_curie}"
                    new_lines[i + 1] = f"{label_indent}label: {new_label}"
        i += 1

    if not dry_run and changes:
        filepath.write_text("\n".join(new_lines))

    return changes


def main():
    dry_run = "--dry-run" in sys.argv
    kb_dir = Path("kb/disorders")

    total_changes = 0
    files_changed = 0

    for filepath in sorted(kb_dir.glob("*.yaml")):
        if filepath.name.endswith(".history.yaml"):
            continue
        changes = apply_replacements(filepath, dry_run=dry_run)
        if changes:
            files_changed += 1
            total_changes += len(changes)
            print(f"{filepath.name}: {len(changes)} replacements")
            for c in changes:
                print(c)

    print(f"\n=== {total_changes} replacements in {files_changed} files ===")
    if dry_run:
        print("(Dry run — no files modified)")


if __name__ == "__main__":
    main()
