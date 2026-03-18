#!/usr/bin/env python3
"""Fix ontology term label mismatches across all disorder YAML files.

Uses OAK Python API directly for fast batch lookups instead of CLI calls.

Usage:
    uv run python scripts/fix_term_labels.py
    uv run python scripts/fix_term_labels.py --dry-run
"""

import re
import sys
from pathlib import Path

from oaklib import get_adapter


# Map prefixes to OAK adapters
OAK_ADAPTERS = {
    "GO": "sqlite:obo:go",
    "UBERON": "sqlite:obo:uberon",
    "CL": "sqlite:obo:cl",
    "HP": "sqlite:obo:hp",
    "MONDO": "sqlite:obo:mondo",
    "CHEBI": "sqlite:obo:chebi",
    "MAXO": "sqlite:obo:maxo",
    "GENO": "sqlite:obo:geno",
}

# Cache adapters
_adapters: dict[str, object] = {}
_label_cache: dict[str, str | None] = {}


def get_oi(prefix: str):
    if prefix not in _adapters:
        adapter_str = OAK_ADAPTERS.get(prefix)
        if not adapter_str:
            return None
        _adapters[prefix] = get_adapter(adapter_str)
    return _adapters[prefix]


def get_canonical_label(curie: str) -> str | None:
    if curie in _label_cache:
        return _label_cache[curie]

    prefix = curie.split(":")[0]
    oi = get_oi(prefix)
    if not oi:
        _label_cache[curie] = None
        return None

    try:
        label = oi.label(curie)
        _label_cache[curie] = label
        return label
    except Exception as e:
        print(f"  Error looking up {curie}: {e}", file=sys.stderr)
        _label_cache[curie] = None
        return None


def process_file(filepath: Path, dry_run: bool = False) -> list[str]:
    """Find id/label pairs in a YAML file and fix label mismatches."""
    content = filepath.read_text()
    lines = content.split("\n")
    changes = []

    new_lines = list(lines)
    i = 0
    while i < len(lines):
        id_match = re.match(
            r'^(\s+)id:\s+((?:GO|UBERON|CL|HP|MONDO|CHEBI|MAXO|GENO):\S+)\s*$',
            lines[i]
        )
        if id_match and i + 1 < len(lines):
            indent = id_match.group(1)
            curie = id_match.group(2)

            label_match = re.match(r'^(\s+)label:\s+(.+)$', lines[i + 1])
            if label_match:
                label_indent = label_match.group(1)
                current_label = label_match.group(2).strip()

                # Handle YAML line continuation
                full_label = current_label
                continuation_lines = []
                j = i + 2
                while j < len(lines):
                    cont_match = re.match(r'^(\s+)(\S.*)$', lines[j])
                    if cont_match and len(cont_match.group(1)) > len(indent) + 2:
                        full_label += " " + cont_match.group(2).strip()
                        continuation_lines.append(j)
                        j += 1
                    else:
                        break

                clean_label = full_label.strip("'\"")
                canonical = get_canonical_label(curie)

                if canonical and canonical != clean_label:
                    if canonical.startswith("obsolete "):
                        changes.append(
                            f"  OBSOLETE {curie}: file='{clean_label}' canonical='{canonical}'"
                        )
                        # Don't auto-fix obsolete — needs manual replacement
                    else:
                        changes.append(
                            f"  FIX {curie}: '{clean_label}' -> '{canonical}'"
                        )
                        if not dry_run:
                            new_lines[i + 1] = f"{label_indent}label: {canonical}"
                            for k in continuation_lines:
                                new_lines[k] = None
        i += 1

    if not dry_run and changes:
        filtered = [line for line in new_lines if line is not None]
        filepath.write_text("\n".join(filtered))

    return changes


def main():
    dry_run = "--dry-run" in sys.argv
    kb_dir = Path("kb/disorders")

    all_changes = {}
    total_fixes = 0
    total_obsolete = 0

    for filepath in sorted(kb_dir.glob("*.yaml")):
        if filepath.name.endswith(".history.yaml"):
            continue
        print(f"Processing {filepath.name}...", end=" ", flush=True)
        changes = process_file(filepath, dry_run=dry_run)
        if changes:
            all_changes[filepath.name] = changes
            fixes = sum(1 for c in changes if "FIX" in c)
            obsoletes = sum(1 for c in changes if "OBSOLETE" in c)
            total_fixes += fixes
            total_obsolete += obsoletes
            print(f"{fixes} fixes, {obsoletes} obsolete")
        else:
            print("OK")

    print("\n=== Summary ===")
    print(f"Label fixes applied: {total_fixes}")
    print(f"Obsolete terms (need manual fix): {total_obsolete}")

    if total_obsolete > 0:
        print("\nObsolete terms requiring manual replacement:")
        for fname, changes in all_changes.items():
            obs = [c for c in changes if "OBSOLETE" in c]
            if obs:
                print(f"\n{fname}:")
                for c in obs:
                    print(c)

    if dry_run:
        print("\n(Dry run — no files modified)")


if __name__ == "__main__":
    main()
