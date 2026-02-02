"""Data validation tests for dismech KB."""

import glob
import os
from pathlib import Path

import pytest
import yaml

from linkml.validator import Validator
from linkml_runtime.loaders import yaml_loader

# Paths
ROOT_DIR = Path(__file__).parent.parent
SCHEMA_PATH = ROOT_DIR / "src" / "dismech" / "schema" / "dismech.yaml"
KB_DIR = ROOT_DIR / "kb" / "disorders"
COMORBIDITY_DIR = ROOT_DIR / "kb" / "comorbidities"

# Get all disorder YAML files (exclude history snapshots)
DISORDER_FILES = [
    f for f in glob.glob(str(KB_DIR / "*.yaml"))
    if not f.endswith(".history.yaml")
]
COMORBIDITY_FILES = glob.glob(str(COMORBIDITY_DIR / "*.yaml"))


@pytest.fixture(scope="module")
def validator():
    """Create a validator instance for all tests."""
    return Validator(SCHEMA_PATH)


@pytest.mark.parametrize("filepath", DISORDER_FILES)
def test_valid_disorder_files(filepath, validator):
    """Test that all disorder files validate against the schema."""
    with open(filepath) as f:
        data = yaml.safe_load(f)

    report = validator.validate(data, target_class="Disease")

    # ValidationReport has a results list with ValidationResult objects
    # Only errors are issues, not informational messages
    errors = [r for r in report.results if r.severity.name == "ERROR"]

    assert not errors, f"Validation errors in {filepath}: {[str(e) for e in errors]}"


@pytest.mark.parametrize("filepath", COMORBIDITY_FILES)
def test_valid_comorbidity_files(filepath, validator):
    """Test that all comorbidity files validate against the schema."""
    with open(filepath) as f:
        data = yaml.safe_load(f)

    report = validator.validate(data, target_class="ComorbidityAssociation")
    errors = [r for r in report.results if r.severity.name == "ERROR"]

    assert not errors, f"Validation errors in {filepath}: {[str(e) for e in errors]}"


@pytest.mark.parametrize("filepath", DISORDER_FILES)
def test_disorder_has_required_fields(filepath):
    """Test that all disorders have required fields."""
    with open(filepath) as f:
        data = yaml.safe_load(f)

    assert "name" in data, f"Missing 'name' in {filepath}"
    assert data["name"], f"Empty 'name' in {filepath}"


@pytest.mark.parametrize("filepath", DISORDER_FILES)
def test_evidence_items_have_references(filepath):
    """Test that evidence items have PMID or DOI references."""
    with open(filepath) as f:
        data = yaml.safe_load(f)

    def check_evidence(evidence_list, path):
        """Recursively check evidence items for references."""
        if not evidence_list:
            return []
        errors = []
        for i, item in enumerate(evidence_list):
            if not item.get("reference"):
                errors.append(f"{path}[{i}]: missing reference")
            elif not (item["reference"].startswith("PMID:") or item["reference"].startswith("DOI:")):
                errors.append(f"{path}[{i}]: reference should start with PMID: or DOI: got {item['reference']}")
        return errors

    all_errors = []

    # Check evidence in pathophysiology
    for i, patho in enumerate(data.get("pathophysiology", [])):
        all_errors.extend(check_evidence(patho.get("evidence", []), f"pathophysiology[{i}].evidence"))

    # Check evidence in phenotypes
    for i, pheno in enumerate(data.get("phenotypes", [])):
        all_errors.extend(check_evidence(pheno.get("evidence", []), f"phenotypes[{i}].evidence"))

    # Check evidence in subtypes
    for i, subtype in enumerate(data.get("has_subtypes", [])):
        all_errors.extend(check_evidence(subtype.get("evidence", []), f"has_subtypes[{i}].evidence"))

    # Check evidence in prevalence
    for i, prev in enumerate(data.get("prevalence", [])):
        all_errors.extend(check_evidence(prev.get("evidence", []), f"prevalence[{i}].evidence"))

    # Check evidence in progression
    for i, prog in enumerate(data.get("progression", [])):
        all_errors.extend(check_evidence(prog.get("evidence", []), f"progression[{i}].evidence"))

    assert not all_errors, f"Evidence errors in {Path(filepath).name}: {all_errors}"


def test_schema_validity(validator):
    """Test that the schema itself is valid LinkML."""
    # If we got here without errors, schema is valid
    assert validator is not None


def test_all_disorders_have_unique_names():
    """Test that all disorder names are unique."""
    names = []
    for filepath in DISORDER_FILES:
        with open(filepath) as f:
            data = yaml.safe_load(f)
        names.append(data.get("name"))

    duplicates = [name for name in names if names.count(name) > 1]
    assert not duplicates, f"Duplicate disorder names: {set(duplicates)}"


def test_disorder_count():
    """Test that we have the expected number of disorders."""
    assert len(DISORDER_FILES) >= 50, f"Expected at least 50 disorders, got {len(DISORDER_FILES)}"
