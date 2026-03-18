#!/usr/bin/env python3
"""Find replacements for obsolete GO/UBERON/MONDO terms and apply them.

For each obsolete term, tries:
1. Check for 'replaced_by' in OAK
2. Search for the file's label text to find the correct current term
3. If no replacement found, report it

Usage:
    uv run python scripts/fix_obsolete_terms.py
    uv run python scripts/fix_obsolete_terms.py --dry-run
"""

import re
import sys
from pathlib import Path

from oaklib import get_adapter

OAK_ADAPTERS = {
    "GO": "sqlite:obo:go",
    "UBERON": "sqlite:obo:uberon",
    "CL": "sqlite:obo:cl",
    "HP": "sqlite:obo:hp",
    "MONDO": "sqlite:obo:mondo",
    "CHEBI": "sqlite:obo:chebi",
    "MAXO": "sqlite:obo:maxo",
}

_adapters = {}


def get_oi(prefix):
    if prefix not in _adapters:
        adapter_str = OAK_ADAPTERS.get(prefix)
        if not adapter_str:
            return None
        _adapters[prefix] = get_adapter(adapter_str)
    return _adapters[prefix]


def find_replacement(curie: str, desired_label: str) -> tuple[str, str] | None:
    """Try to find a non-obsolete replacement for an obsolete term."""
    prefix = curie.split(":")[0]
    oi = get_oi(prefix)
    if not oi:
        return None

    # 1. Check replaced_by
    try:
        for rel, target in oi.simple_mappings_by_curie(curie):
            if rel == "replaced_by":
                target_label = oi.label(target)
                if target_label and not target_label.startswith("obsolete"):
                    return (target, target_label)
    except Exception:
        pass

    # 2. Search for the desired label
    try:
        results = list(oi.basic_search(desired_label))
        for result in results:
            label = oi.label(result)
            if label and not label.startswith("obsolete"):
                if label.lower() == desired_label.lower() or desired_label.lower() in label.lower():
                    return (result, label)
        # If exact match not found, try first non-obsolete result
        for result in results:
            label = oi.label(result)
            if label and not label.startswith("obsolete"):
                return (result, label)
    except Exception:
        pass

    return None


def main():
    dry_run = "--dry-run" in sys.argv
    kb_dir = Path("kb/disorders")

    # Collect all obsolete terms from files
    obsolete_terms = {}  # curie -> {file_label, files}

    for filepath in sorted(kb_dir.glob("*.yaml")):
        if filepath.name.endswith(".history.yaml"):
            continue
        content = filepath.read_text()
        lines = content.split("\n")

        for i, line in enumerate(lines):
            id_match = re.match(
                r'^\s+id:\s+((?:GO|UBERON|CL|HP|MONDO|CHEBI|MAXO):\S+)\s*$', line
            )
            if id_match and i + 1 < len(lines):
                curie = id_match.group(1)
                label_match = re.match(r'^\s+label:\s+(.+)$', lines[i + 1])
                if label_match:
                    file_label = label_match.group(1).strip().strip("'\"")
                    # Check if canonical is obsolete
                    prefix = curie.split(":")[0]
                    oi = get_oi(prefix)
                    if oi:
                        canonical = oi.label(curie)
                        if canonical and canonical.startswith("obsolete"):
                            if curie not in obsolete_terms:
                                obsolete_terms[curie] = {
                                    "file_label": file_label,
                                    "files": [],
                                }
                            obsolete_terms[curie]["files"].append(
                                (filepath, i, i + 1)
                            )

    print(f"Found {len(obsolete_terms)} unique obsolete terms\n")

    # Find replacements
    replacements = {}
    unresolved = []

    for curie, info in sorted(obsolete_terms.items()):
        file_label = info["file_label"]
        print(f"  {curie} ('{file_label}')...", end=" ", flush=True)
        replacement = find_replacement(curie, file_label)
        if replacement:
            new_curie, new_label = replacement
            print(f"-> {new_curie} ('{new_label}')")
            replacements[curie] = (new_curie, new_label, info)
        else:
            print("NO REPLACEMENT FOUND")
            unresolved.append((curie, info))

    # Apply replacements
    if not dry_run:
        files_modified = set()
        for old_curie, (new_curie, new_label, info) in replacements.items():
            for filepath, id_line, label_line in info["files"]:
                content = filepath.read_text()
                # Replace id
                content = content.replace(
                    f"id: {old_curie}", f"id: {new_curie}"
                )
                # Replace the old label with new canonical label on the same line pattern
                # Be careful: only replace in context of the label field
                old_label = info["file_label"]
                lines = content.split("\n")
                new_lines = []
                for line in lines:
                    if re.match(rf'^\s+label:\s+{re.escape(old_label)}\s*$', line):
                        line = re.sub(
                            rf'(label:\s+){re.escape(old_label)}',
                            rf'\g<1>{new_label}',
                            line
                        )
                    new_lines.append(line)
                filepath.write_text("\n".join(new_lines))
                files_modified.add(filepath.name)

        print(f"\n=== Applied {len(replacements)} replacements across {len(files_modified)} files ===")

    if unresolved:
        print(f"\n=== {len(unresolved)} unresolved obsolete terms ===")
        for curie, info in unresolved:
            print(f"  {curie}: '{info['file_label']}' in {len(info['files'])} file(s)")
            for fp, _, _ in info["files"]:
                print(f"    - {fp.name}")

    if dry_run:
        print("\n(Dry run — no files modified)")


if __name__ == "__main__":
    main()
