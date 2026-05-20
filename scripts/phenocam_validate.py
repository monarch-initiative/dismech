#!/usr/bin/env python3
"""Custom structural validator for PhenoCAM V2 files."""

import sys
from pathlib import Path
import yaml

MODULES_DIR = Path(__file__).parent.parent / "causal_models" / "modules"


def collect_node_ids(data: dict) -> set[str]:
    """Collect all declared node IDs from all node-kind collections."""
    ids = set()
    for collection in (
        "molecular_entities",
        "molecular_activities",
        "cellular_processes",
        "tissue_processes",
        "variants",
        "chemical_exposures",
        "environmental_factors",
        "phenotypes",
        "modulators",
    ):
        for node in data.get(collection) or []:
            if node_id := node.get("id"):
                ids.add(node_id)
    return ids


def collect_declared_tags(data: dict, group_field: str) -> set[str]:
    """Collect IDs declared in hypothesis_groups or has_subtypes."""
    return {g["id"] for g in (data.get(group_field) or []) if "id" in g}


def validate_file(path: Path, target_class: str) -> list[str]:
    errors = []
    with open(path) as f:
        data = yaml.safe_load(f)
    if data is None:
        errors.append("File is empty or contains no YAML content")
        return errors

    local_ids = collect_node_ids(data)
    # Only enforce tag resolution when groups are declared;
    # modules legitimately may omit hypothesis_groups entirely.
    hypothesis_ids = collect_declared_tags(data, "hypothesis_groups")
    subtype_ids = collect_declared_tags(data, "has_subtypes")

    # For DiseaseCourse: also include IDs resolvable from imported modules
    imported_ids: set[str] = set()
    if target_class == "DiseaseCourse":
        for imp in data.get("imports") or []:
            module_id = imp.get("module")
            if not module_id:
                continue
            module_path = MODULES_DIR / f"{module_id}.yaml"
            if not module_path.exists():
                errors.append(f"imports: module '{module_id}' not found at {module_path}")
                continue
            with open(module_path) as mf:
                module_data = yaml.safe_load(mf)
            imported_ids |= collect_node_ids(module_data or {})

    all_known_ids = local_ids | imported_ids

    # Check causal_relations subject/object resolution
    for i, rel in enumerate(data.get("causal_relations") or []):
        subj = rel.get("subject")
        obj = rel.get("object")
        if subj and subj not in all_known_ids:
            errors.append(
                f"causal_relations[{i}]: subject '{subj}' not found in any node collection"
            )
        if obj and obj not in all_known_ids:
            errors.append(
                f"causal_relations[{i}]: object '{obj}' not found in any node collection"
            )

        # Check hypothesis tags
        for tag in rel.get("hypotheses") or []:
            if hypothesis_ids and tag not in hypothesis_ids:
                errors.append(
                    f"causal_relations[{i}]: hypothesis tag '{tag}' not declared in hypothesis_groups"
                )

        # Check subtype tags
        for tag in rel.get("subtypes") or []:
            if subtype_ids and tag not in subtype_ids:
                errors.append(
                    f"causal_relations[{i}]: subtype tag '{tag}' not declared in has_subtypes"
                )

    # Check node-level tags
    for collection in (
        "molecular_entities", "molecular_activities", "cellular_processes",
        "tissue_processes", "variants", "chemical_exposures", "environmental_factors",
        "phenotypes", "modulators",
    ):
        for node in data.get(collection) or []:
            node_id = node.get("id", "?")
            for tag in node.get("hypotheses") or []:
                if hypothesis_ids and tag not in hypothesis_ids:
                    errors.append(
                        f"{collection} '{node_id}': hypothesis tag '{tag}' not declared in hypothesis_groups"
                    )
            for tag in node.get("subtypes") or []:
                if subtype_ids and tag not in subtype_ids:
                    errors.append(
                        f"{collection} '{node_id}': subtype tag '{tag}' not declared in has_subtypes"
                    )

    return errors


def main():
    import argparse

    parser = argparse.ArgumentParser(description="PhenoCAM V2 structural validator")
    parser.add_argument("file", type=Path, help="Path to module or disease YAML file")
    parser.add_argument(
        "--target-class",
        choices=["Module", "DiseaseCourse"],
        required=True,
        help="Which top-level class to validate against",
    )
    args = parser.parse_args()

    errors = validate_file(args.file, args.target_class)
    if errors:
        print(f"ERRORS in {args.file}:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print(f"✓ {args.file} passed structural validation")


if __name__ == "__main__":
    main()
