"""Data validation tests for dismech KB."""

import glob
import warnings
from pathlib import Path

import pytest
import yaml

from linkml.validator import Validator

# Paths
ROOT_DIR = Path(__file__).parent.parent
SCHEMA_PATH = ROOT_DIR / "src" / "dismech" / "schema" / "dismech.yaml"
KB_DIR = ROOT_DIR / "kb" / "disorders"
COMORBIDITY_DIR = ROOT_DIR / "kb" / "comorbidities"

# Get all disorder YAML files (exclude history snapshots)
DISORDER_FILES = [
    f for f in glob.glob(str(KB_DIR / "*.yaml")) if not f.endswith(".history.yaml")
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
            elif not any(
                item["reference"].startswith(prefix)
                for prefix in (
                    "PMID:",
                    "DOI:",
                    "clinicaltrials:",
                    "file:",
                    "url:",
                    "GEO:",
                    "ORPHA:",
                )
            ):
                errors.append(
                    f"{path}[{i}]: reference should start with PMID:, DOI:, clinicaltrials:, file:, url:, GEO:, or ORPHA: got {item['reference']}"
                )
        return errors

    all_errors = []

    # Check evidence in pathophysiology
    for i, patho in enumerate(data.get("pathophysiology", [])):
        all_errors.extend(
            check_evidence(patho.get("evidence", []), f"pathophysiology[{i}].evidence")
        )

    # Check evidence in phenotypes
    for i, pheno in enumerate(data.get("phenotypes", [])):
        all_errors.extend(
            check_evidence(pheno.get("evidence", []), f"phenotypes[{i}].evidence")
        )

    # Check evidence in subtypes
    for i, subtype in enumerate(data.get("has_subtypes", [])):
        all_errors.extend(
            check_evidence(subtype.get("evidence", []), f"has_subtypes[{i}].evidence")
        )

    # Check evidence in prevalence
    for i, prev in enumerate(data.get("prevalence", [])):
        all_errors.extend(
            check_evidence(prev.get("evidence", []), f"prevalence[{i}].evidence")
        )

    # Check evidence in progression
    for i, prog in enumerate(data.get("progression", [])):
        all_errors.extend(
            check_evidence(prog.get("evidence", []), f"progression[{i}].evidence")
        )

    assert not all_errors, f"Evidence errors in {Path(filepath).name}: {all_errors}"


def test_schema_validity(validator):
    """Test that the schema itself is valid LinkML."""
    # If we got here without errors, schema is valid
    assert validator is not None


def test_environmental_food_source_slot_validates(validator):
    """Environmental entries may annotate a specific food, beverage, or nutrient source."""
    data = {
        "name": "Test Disease",
        "environmental": [
            {
                "name": "Coffee-triggered flushing",
                "food_source": {
                    "preferred_term": "coffee beverage",
                    "term": {
                        "id": "FOODON:00001244",
                        "label": "coffee beverage",
                    },
                },
            }
        ],
    }

    report = validator.validate(data, target_class="Disease")
    errors = [r for r in report.results if r.severity.name == "ERROR"]

    assert not errors, f"Validation errors: {[str(e) for e in errors]}"


def test_environmental_food_source_slot_accepts_chebi_nutrient(validator):
    """Environmental food_source also accepts CHEBI nutrients/minerals/supplements."""
    data = {
        "name": "Test Disease",
        "environmental": [
            {
                "name": "Vitamin trigger",
                "food_source": {
                    "preferred_term": "vitamin C",
                    "term": {
                        "id": "CHEBI:176783",
                        "label": "vitamin C",
                    },
                },
            }
        ],
    }

    report = validator.validate(data, target_class="Disease")
    errors = [r for r in report.results if r.severity.name == "ERROR"]

    assert not errors, f"Validation errors: {[str(e) for e in errors]}"


def test_environmental_context_slot_accepts_built_environment_terms(validator):
    """Environmental entries may annotate ENVO built-environment descendants."""
    data = {
        "name": "Test Disease",
        "environmental": [
            {
                "name": "Healthcare-associated exposure",
                "environment_context": {
                    "preferred_term": "healthcare facility",
                    "term": {
                        "id": "ENVO:03501134",
                        "label": "healthcare facility",
                    },
                },
            },
            {
                "name": "Industrial workplace exposure",
                "environment_context": {
                    "preferred_term": "factory",
                    "term": {
                        "id": "ENVO:01000536",
                        "label": "factory",
                    },
                },
            },
        ],
    }

    report = validator.validate(data, target_class="Disease")
    errors = [r for r in report.results if r.severity.name == "ERROR"]

    assert not errors, f"Validation errors: {[str(e) for e in errors]}"


def test_subtype_ncit_mappings_validate(validator):
    """Cancer subtype facets may carry MONDO/NCIT grounding without implying a local page."""
    data = {
        "name": "Test Pilocytic Astrocytoma",
        "disease_term": {
            "preferred_term": "pilocytic astrocytoma",
            "term": {"id": "MONDO:0016691", "label": "pilocytic astrocytoma"},
        },
        "has_subtypes": [
            {
                "name": "Pilomyxoid",
                "classification": "histology",
                "subtype_term": {
                    "preferred_term": "pilomyxoid astrocytoma",
                    "term": {
                        "id": "MONDO:0016692",
                        "label": "pilomyxoid astrocytoma",
                    },
                },
                "mappings": {
                    "mondo_mappings": [
                        {
                            "term": {
                                "id": "MONDO:0016692",
                                "label": "pilomyxoid astrocytoma",
                            },
                            "mapping_predicate": "skos:exactMatch",
                            "mapping_source": "MONDO",
                        }
                    ],
                    "ncit_mappings": [
                        {
                            "term": {
                                "id": "NCIT:C40315",
                                "label": "Pilomyxoid Astrocytoma",
                            },
                            "mapping_predicate": "skos:exactMatch",
                            "mapping_source": "NCIT",
                        }
                    ],
                },
            }
        ],
    }

    report = validator.validate(data, target_class="Disease")
    errors = [r for r in report.results if r.severity.name == "ERROR"]

    assert not errors, f"Validation errors: {[str(e) for e in errors]}"


def test_infectious_agent_food_source_slot_validates(validator):
    """Infectious agents may annotate a food or beverage vehicle of exposure."""
    data = {
        "name": "Test Disease",
        "infectious_agent": [
            {
                "name": "Vibrio vulnificus",
                "infectious_agent_term": {
                    "preferred_term": "Vibrio vulnificus",
                    "term": {
                        "id": "NCBITaxon:6725",
                        "label": "Vibrio vulnificus",
                    },
                },
                "food_source": {
                    "preferred_term": "shellfish food product",
                    "term": {
                        "id": "FOODON:00001293",
                        "label": "shellfish food product",
                    },
                },
            }
        ],
    }

    report = validator.validate(data, target_class="Disease")
    errors = [r for r in report.results if r.severity.name == "ERROR"]

    assert not errors, f"Validation errors: {[str(e) for e in errors]}"


def test_treatment_dietary_modifications_validate(validator):
    """Treatment descriptors may specify FOODON- or CHEBI-backed dietary additions or restrictions."""
    data = {
        "name": "Test Disease",
        "treatments": [
            {
                "name": "Dietary restriction",
                "treatment_term": {
                    "preferred_term": "dietary intervention",
                    "term": {
                        "id": "MAXO:0000088",
                        "label": "dietary intervention",
                    },
                    "dietary_modifications": [
                        {
                            "action": "AVOID",
                            "food": {
                                "preferred_term": "wheat food product",
                                "term": {
                                    "id": "FOODON:00001141",
                                    "label": "wheat food product",
                                },
                            },
                        }
                    ],
                },
            }
        ],
    }

    report = validator.validate(data, target_class="Disease")
    errors = [r for r in report.results if r.severity.name == "ERROR"]

    assert not errors, f"Validation errors: {[str(e) for e in errors]}"


def test_treatment_dietary_modifications_accept_chebi_nutrient(validator):
    """Dietary modifications may target CHEBI nutrients or supplements."""
    data = {
        "name": "Test Disease",
        "treatments": [
            {
                "name": "Vitamin supplementation",
                "treatment_term": {
                    "preferred_term": "dietary intervention",
                    "term": {
                        "id": "MAXO:0000088",
                        "label": "dietary intervention",
                    },
                    "dietary_modifications": [
                        {
                            "action": "ADD",
                            "food": {
                                "preferred_term": "vitamin C",
                                "term": {
                                    "id": "CHEBI:176783",
                                    "label": "vitamin C",
                                },
                            },
                        }
                    ],
                },
            }
        ],
    }

    report = validator.validate(data, target_class="Disease")
    errors = [r for r in report.results if r.severity.name == "ERROR"]

    assert not errors, f"Validation errors: {[str(e) for e in errors]}"


def test_all_disorders_have_unique_names():
    """Test that all disorder names are unique."""
    names = []
    for filepath in DISORDER_FILES:
        with open(filepath) as f:
            data = yaml.safe_load(f)
        names.append(data.get("name"))

    duplicates = [name for name in names if names.count(name) > 1]
    assert not duplicates, f"Duplicate disorder names: {set(duplicates)}"


@pytest.mark.parametrize("filepath", DISORDER_FILES)
def test_subtype_foreign_keys(filepath):
    """Test that subtype references match has_subtypes names."""
    with open(filepath) as f:
        data = yaml.safe_load(f)

    valid_subtypes = {s["name"] for s in data.get("has_subtypes", [])}
    if not valid_subtypes:
        return

    errors = []
    # Sections with a top-level subtype field
    for section in (
        "phenotypes",
        "biochemical",
        "genetic",
        "prevalence",
        "progression",
        "histopathology",
    ):
        for i, item in enumerate(data.get(section, [])):
            val = item.get("subtype")
            if val and val not in valid_subtypes:
                errors.append(f"{section}[{i}].subtype={val!r}")
            # Multivalued `subtypes` (plural) — issue #963
            for k, sval in enumerate(item.get("subtypes", []) or []):
                if sval and sval not in valid_subtypes:
                    errors.append(f"{section}[{i}].subtypes[{k}]={sval!r}")
            # Also check phenotype_contexts
            for j, ctx in enumerate(item.get("phenotype_contexts", [])):
                val = ctx.get("subtype")
                if val and val not in valid_subtypes:
                    errors.append(
                        f"{section}[{i}].phenotype_contexts[{j}].subtype={val!r}"
                    )

    # mechanistic_hypotheses.applies_to_subtypes
    for i, hyp in enumerate(data.get("mechanistic_hypotheses", [])):
        for val in hyp.get("applies_to_subtypes", []):
            if val not in valid_subtypes:
                errors.append(
                    f"mechanistic_hypotheses[{i}].applies_to_subtypes={val!r}"
                )

    assert not errors, (
        f"Subtype FK mismatches in {Path(filepath).name}. "
        f"Valid subtypes: {valid_subtypes}. Bad refs: {errors}"
    )


def test_phenotype_multivalued_subtypes_validates(validator, tmp_path):
    """Issue #963: a phenotype may be associated with multiple subtypes.

    A phenotype using the multivalued `subtypes` slot with a list of subtype
    names should validate against the schema, and the FK check should accept
    list values.
    """
    disease = {
        "name": "Test Multi-Subtype Disease",
        "disease_term": {
            "term": {"id": "MONDO:0000001", "label": "disease or disorder"}
        },
        "has_subtypes": [
            {"name": "Type 1", "description": "Subtype one."},
            {"name": "Type 2", "description": "Subtype two."},
        ],
        "phenotypes": [
            {
                "name": "Shared phenotype",
                "description": "A phenotype seen in both subtypes.",
                "subtypes": ["Type 1", "Type 2"],
            },
        ],
    }

    report = validator.validate(disease, target_class="Disease")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, f"Unexpected validation errors: {[str(e) for e in errors]}"

    # Reuse the FK check logic by writing to disk and invoking the test fn.
    fake_path = tmp_path / "TestMulti.yaml"
    fake_path.write_text(yaml.safe_dump(disease, sort_keys=False))
    test_subtype_foreign_keys(str(fake_path))


def test_phenotype_multivalued_subtypes_fk_catches_bad_refs(tmp_path):
    """Bad subtype name in the multivalued `subtypes` list must be caught."""
    disease = {
        "name": "Bad Multi-Subtype",
        "has_subtypes": [{"name": "Type 1"}],
        "phenotypes": [
            {"name": "P", "subtypes": ["Type 1", "Type 99 (not declared)"]},
        ],
    }
    fake_path = tmp_path / "BadMulti.yaml"
    fake_path.write_text(yaml.safe_dump(disease, sort_keys=False))

    with pytest.raises(AssertionError, match="Type 99"):
        test_subtype_foreign_keys(str(fake_path))


@pytest.mark.parametrize("filepath", DISORDER_FILES)
def test_experimental_model_mechanism_targets(filepath):
    """Experimental model links should reference declared pathophysiology nodes."""
    with open(filepath) as f:
        data = yaml.safe_load(f)

    valid_targets = {
        item["name"]
        for item in data.get("pathophysiology", [])
        if isinstance(item, dict) and item.get("name")
    }
    if not valid_targets:
        return

    errors = []
    for i, model in enumerate(data.get("experimental_models", [])):
        for j, link in enumerate(model.get("modeled_mechanisms", [])):
            target = link.get("target")
            if target and target not in valid_targets:
                errors.append(
                    f"experimental_models[{i}].modeled_mechanisms[{j}].target={target!r}"
                )

    assert not errors, (
        f"Experimental model mechanism mismatches in {Path(filepath).name}. "
        f"Valid targets: {valid_targets}. Bad refs: {errors}"
    )


@pytest.mark.parametrize("filepath", DISORDER_FILES)
def test_computational_model_mechanism_targets(filepath):
    """Computational model links should reference declared pathophysiology nodes."""
    with open(filepath) as f:
        data = yaml.safe_load(f)

    valid_targets = {
        item["name"]
        for item in data.get("pathophysiology", [])
        if isinstance(item, dict) and item.get("name")
    }
    if not valid_targets:
        return

    errors = []
    for i, model in enumerate(data.get("computational_models", [])):
        for j, link in enumerate(model.get("modeled_mechanisms", [])):
            target = link.get("target")
            if target and target not in valid_targets:
                errors.append(
                    f"computational_models[{i}].modeled_mechanisms[{j}].target={target!r}"
                )

    assert not errors, (
        f"Computational model mechanism mismatches in {Path(filepath).name}. "
        f"Valid targets: {valid_targets}. Bad refs: {errors}"
    )


@pytest.mark.parametrize("filepath", DISORDER_FILES)
def test_subtypes_have_disease_term(filepath):
    """Test that has_subtypes items have a subtype_term with an ontology grounding.

    Each subtype should be grounded to a MONDO or NCIT disease term via
    the subtype_term descriptor so that subtypes are machine-queryable.
    """
    with open(filepath) as f:
        data = yaml.safe_load(f)

    subtypes = data.get("has_subtypes", [])
    if not subtypes:
        return

    missing = []
    for i, s in enumerate(subtypes):
        term = s.get("subtype_term")
        if not term or not term.get("term", {}).get("id"):
            missing.append(s.get("name", f"has_subtypes[{i}]"))

    if missing:
        warnings.warn(
            f"{Path(filepath).name}: subtypes missing subtype_term: {missing}",
            stacklevel=1,
        )


def test_disorder_count():
    """Test that we have the expected number of disorders."""
    assert len(DISORDER_FILES) >= 50, (
        f"Expected at least 50 disorders, got {len(DISORDER_FILES)}"
    )
