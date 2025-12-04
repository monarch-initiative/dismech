#!/usr/bin/env python
"""
Term validation script using OAK.

Validates that:
1. All term IDs are valid in their respective ontologies
2. All labels match the canonical label from the ontology

This walks all nested structures looking for objects with {id: ..., label: ...}
and validates them against OAK adapters.
"""

import sys
import yaml
from pathlib import Path
from dataclasses import dataclass, field
from oaklib import get_adapter


@dataclass
class ValidationError:
    file: str
    path: str
    term_id: str
    expected_label: str
    actual_label: str | None
    error_type: str  # "invalid_id" or "label_mismatch"


@dataclass
class ValidationResult:
    errors: list[ValidationError] = field(default_factory=list)
    terms_checked: int = 0
    files_checked: int = 0


# Initialize adapters once (cached)
print("Loading ontology adapters (this may take a moment on first run)...")
ADAPTERS = {
    "MONDO": get_adapter("sqlite:obo:mondo"),
    "CL": get_adapter("sqlite:obo:cl"),
    "HP": get_adapter("sqlite:obo:hp"),
    "GO": get_adapter("sqlite:obo:go"),
    "UBERON": get_adapter("sqlite:obo:uberon"),
    "CHEBI": get_adapter("sqlite:obo:chebi"),
    "HGNC": get_adapter("sqlite:obo:hgnc"),
}
print("Adapters loaded.\n")


def get_adapter_for_id(term_id: str):
    """Get the appropriate adapter for a term ID."""
    prefix = term_id.split(":")[0].upper() if ":" in term_id else None
    return ADAPTERS.get(prefix)


def normalize_term_id(term_id: str) -> str:
    """Normalize term ID to match OBO format (some use lowercase prefixes)."""
    if term_id.startswith("HGNC:"):
        return term_id.replace("HGNC:", "hgnc:")
    return term_id


def validate_term(term_id: str, label: str, file_path: str, json_path: str, result: ValidationResult):
    """Validate a single term ID and label."""
    adapter = get_adapter_for_id(term_id)
    if not adapter:
        # Unknown prefix, skip
        return

    result.terms_checked += 1
    normalized_id = normalize_term_id(term_id)
    actual_label = adapter.label(normalized_id)

    if actual_label is None:
        result.errors.append(ValidationError(
            file=file_path,
            path=json_path,
            term_id=term_id,
            expected_label=label,
            actual_label=None,
            error_type="invalid_id"
        ))
    elif actual_label != label:
        result.errors.append(ValidationError(
            file=file_path,
            path=json_path,
            term_id=term_id,
            expected_label=label,
            actual_label=actual_label,
            error_type="label_mismatch"
        ))


def extract_terms(obj, path="", terms=None):
    """Recursively extract all term objects (with id and label) from nested structure."""
    if terms is None:
        terms = []

    if isinstance(obj, dict):
        # Check if this is a term object (has id and label)
        if "id" in obj and "label" in obj:
            term_id = obj.get("id")
            label = obj.get("label")
            if term_id and label and ":" in str(term_id):
                terms.append((term_id, label, path))

        # Recurse into nested structures
        for key, value in obj.items():
            new_path = f"{path}.{key}" if path else key
            extract_terms(value, new_path, terms)

    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            extract_terms(item, f"{path}[{i}]", terms)

    return terms


def validate_file(file_path: Path, result: ValidationResult):
    """Validate all terms in a single file."""
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)

    if not data:
        return

    terms = extract_terms(data)
    for term_id, label, json_path in terms:
        validate_term(term_id, label, str(file_path.name), json_path, result)


def main():
    kb_dir = Path(__file__).parent.parent / "kb" / "disorders"

    # Check for specific file argument
    if len(sys.argv) > 1:
        files = [Path(sys.argv[1])]
    else:
        files = sorted(kb_dir.glob("*.yaml"))

    result = ValidationResult()

    for file_path in files:
        print(f"Validating: {file_path.name}")
        result.files_checked += 1
        validate_file(file_path, result)

    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)
    print(f"Files checked: {result.files_checked}")
    print(f"Terms checked: {result.terms_checked}")
    print(f"Errors found: {len(result.errors)}")

    if result.errors:
        print("\nERRORS:")
        print("-" * 60)
        for err in result.errors:
            if err.error_type == "invalid_id":
                print(f"  INVALID ID: {err.file}")
                print(f"    Path: {err.path}")
                print(f"    Term: {err.term_id}")
                print(f"    Label: {err.expected_label}")
                print()
            else:
                print(f"  LABEL MISMATCH: {err.file}")
                print(f"    Path: {err.path}")
                print(f"    Term: {err.term_id}")
                print(f"    Expected: {err.expected_label}")
                print(f"    Actual: {err.actual_label}")
                print()
        sys.exit(1)
    else:
        print("\n✓ All terms valid!")
        sys.exit(0)


if __name__ == "__main__":
    main()
