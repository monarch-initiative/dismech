#!/usr/bin/env python3
"""
Migrate string-valued ontology term fields to Descriptor objects.

Transforms:
    cell_types:
    - Neurons
    - Microglia

To:
    cell_types:
    - preferred_term: Neurons
    - preferred_term: Microglia
"""

import sys
from pathlib import Path
from ruamel.yaml import YAML

# Fields to migrate and their locations in the data structure
# Format: (field_name, [paths_to_parent_objects])
FIELD_MIGRATIONS = {
    "cell_types": [
        ["pathophysiology", "*"],
        ["biochemical", "*"],
        ["stages", "*", "pathophysiology", "*"],
        ["stages", "*", "substages", "*", "pathophysiology", "*"],
    ],
    "biological_processes": [
        ["pathophysiology", "*"],
        ["stages", "*", "pathophysiology", "*"],
        ["stages", "*", "substages", "*", "pathophysiology", "*"],
    ],
    "locations": [
        ["pathophysiology", "*"],
        ["has_subtypes", "*"],
        ["stages", "*", "pathophysiology", "*"],
        ["stages", "*", "substages", "*", "pathophysiology", "*"],
    ],
    "chemical_entities": [
        ["pathophysiology", "*"],
        ["stages", "*", "pathophysiology", "*"],
        ["stages", "*", "substages", "*", "pathophysiology", "*"],
    ],
    "genes": [
        ["pathophysiology", "*"],
        ["animal_models", "*"],
        ["stages", "*", "pathophysiology", "*"],
        ["stages", "*", "substages", "*", "pathophysiology", "*"],
    ],
    "gene": [  # singular version
        ["pathophysiology", "*"],
        ["variants", "*"],
        ["stages", "*", "pathophysiology", "*"],
        ["stages", "*", "substages", "*", "pathophysiology", "*"],
    ],
    "pathways": [
        ["pathophysiology", "*"],
        ["stages", "*", "pathophysiology", "*"],
        ["stages", "*", "substages", "*", "pathophysiology", "*"],
    ],
    "cellular_components": [
        ["pathophysiology", "*"],
        ["stages", "*", "pathophysiology", "*"],
        ["stages", "*", "substages", "*", "pathophysiology", "*"],
    ],
    "triggers": [
        ["pathophysiology", "*"],
        ["stages", "*", "pathophysiology", "*"],
        ["stages", "*", "substages", "*", "pathophysiology", "*"],
    ],
    "assays": [
        ["pathophysiology", "*"],
        ["biochemical", "*"],
        ["stages", "*", "pathophysiology", "*"],
        ["stages", "*", "substages", "*", "pathophysiology", "*"],
    ],
}


def migrate_field_value(value):
    """Convert a string value to a descriptor dict."""
    if isinstance(value, str):
        return {"preferred_term": value}
    elif isinstance(value, dict):
        # Already migrated or has other structure
        if "preferred_term" in value:
            return value
        # Unknown dict structure, leave as is
        return value
    else:
        return value


def migrate_field_in_object(obj, field_name):
    """Migrate a field within an object if it exists."""
    if not isinstance(obj, dict):
        return False

    if field_name not in obj:
        return False

    value = obj[field_name]
    if value is None:
        return False

    modified = False

    if isinstance(value, list):
        new_list = []
        for item in value:
            new_item = migrate_field_value(item)
            if new_item != item:
                modified = True
            new_list.append(new_item)
        if modified:
            obj[field_name] = new_list
    elif isinstance(value, str):
        # Single value (like 'gene' field)
        obj[field_name] = migrate_field_value(value)
        modified = True

    return modified


def get_objects_at_path(data, path):
    """
    Get all objects at a given path.
    Path is a list like ["pathophysiology", "*"] where "*" means iterate all items.
    """
    if not path:
        return [data]

    current = path[0]
    rest = path[1:]

    if current == "*":
        # Iterate all items if data is a list
        if isinstance(data, list):
            results = []
            for item in data:
                results.extend(get_objects_at_path(item, rest))
            return results
        else:
            return []
    else:
        # Navigate to named field
        if isinstance(data, dict) and current in data:
            return get_objects_at_path(data[current], rest)
        else:
            return []


def migrate_file(file_path: Path, fields_to_migrate: list[str], dry_run: bool = False) -> dict:
    """
    Migrate specified fields in a YAML file.

    Returns dict with migration stats.
    """
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.width = 4096  # Prevent line wrapping

    with open(file_path) as f:
        data = yaml.load(f)

    if data is None:
        return {"file": str(file_path), "migrated": 0, "error": "Empty file"}

    total_migrated = 0
    field_counts = {}

    for field_name in fields_to_migrate:
        if field_name not in FIELD_MIGRATIONS:
            continue

        paths = FIELD_MIGRATIONS[field_name]
        field_migrated = 0

        for path in paths:
            objects = get_objects_at_path(data, path)
            for obj in objects:
                if migrate_field_in_object(obj, field_name):
                    field_migrated += 1

        if field_migrated > 0:
            field_counts[field_name] = field_migrated
            total_migrated += field_migrated

    if total_migrated > 0 and not dry_run:
        with open(file_path, "w") as f:
            yaml.dump(data, f)

    return {
        "file": str(file_path),
        "migrated": total_migrated,
        "fields": field_counts,
    }


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Migrate ontology term fields to Descriptor objects")
    parser.add_argument("fields", nargs="+", help="Fields to migrate (e.g., cell_types biological_processes)")
    parser.add_argument("--kb-dir", default="kb/disorders", help="Directory containing disorder YAML files")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be changed without modifying files")
    parser.add_argument("--file", help="Migrate a single file instead of all files")

    args = parser.parse_args()

    # Validate fields
    for field in args.fields:
        if field not in FIELD_MIGRATIONS:
            print(f"Error: Unknown field '{field}'")
            print(f"Available fields: {', '.join(FIELD_MIGRATIONS.keys())}")
            sys.exit(1)

    if args.file:
        files = [Path(args.file)]
    else:
        kb_dir = Path(args.kb_dir)
        if not kb_dir.exists():
            print(f"Error: Directory {kb_dir} does not exist")
            sys.exit(1)
        files = sorted(kb_dir.glob("*.yaml"))

    print(f"Migrating fields: {', '.join(args.fields)}")
    if args.dry_run:
        print("DRY RUN - no files will be modified")
    print()

    total_files = 0
    total_changes = 0

    for file_path in files:
        result = migrate_file(file_path, args.fields, dry_run=args.dry_run)

        if result["migrated"] > 0:
            total_files += 1
            total_changes += result["migrated"]
            print(f"{file_path.name}: {result['migrated']} changes")
            for field, count in result.get("fields", {}).items():
                print(f"  - {field}: {count}")

    print()
    print(f"Summary: {total_changes} changes across {total_files} files")

    if args.dry_run and total_changes > 0:
        print("\nRe-run without --dry-run to apply changes")


if __name__ == "__main__":
    main()
