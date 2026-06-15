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
MODULES_DIR = ROOT_DIR / "kb" / "modules"
GROUPINGS_DIR = ROOT_DIR / "kb" / "groupings"

# Get all disorder YAML files (exclude history snapshots)
DISORDER_FILES = [
    f for f in glob.glob(str(KB_DIR / "*.yaml")) if not f.endswith(".history.yaml")
]
COMORBIDITY_FILES = glob.glob(str(COMORBIDITY_DIR / "*.yaml"))
GROUPING_FILES = glob.glob(str(GROUPINGS_DIR / "*.yaml"))


def _disease_names():
    """Set of all Disease `name` values across kb/disorders/."""
    names = set()
    for fp in DISORDER_FILES:
        with open(fp) as f:
            data = yaml.safe_load(f)
        if isinstance(data, dict) and data.get("name"):
            names.add(data["name"])
    return names


def _module_stems():
    """Set of mechanism module filename stems (without .yaml) in kb/modules/."""
    return {Path(f).stem for f in glob.glob(str(MODULES_DIR / "*.yaml"))}


def _grouping_names():
    """Set of Grouping `name` values across kb/groupings/."""
    names = set()
    for fp in GROUPING_FILES:
        with open(fp) as f:
            data = yaml.safe_load(f)
        if isinstance(data, dict) and data.get("name"):
            names.add(data["name"])
    return names


NON_THERAPEUTIC_ACTION_CATEGORIES = {
    "DIAGNOSTIC",
    "SCREENING",
    "MONITORING",
    "COUNSELING_INFORMATIONAL",
}


def _non_therapeutic_action_target_errors(data):
    """Find annotated non-therapeutic medical actions that link to pathograph nodes."""
    errors = []
    for i, treatment in enumerate(data.get("treatments", []) or []):
        category = treatment.get("action_category")
        if category not in NON_THERAPEUTIC_ACTION_CATEGORIES:
            continue
        invalid_target_slots = [
            slot
            for slot in ("target_mechanisms", "target_phenotypes")
            if treatment.get(slot)
        ]
        if invalid_target_slots:
            slot_list = ", ".join(invalid_target_slots)
            name = treatment.get("name", f"treatments[{i}]")
            errors.append(
                f"treatments[{i}] {name!r} has action_category={category!r} "
                f"but also has treatment-style target slots: {slot_list}"
            )
    return errors


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
    """Test that evidence items use supported reference prefixes."""
    with open(filepath) as f:
        data = yaml.safe_load(f)

    allowed_reference_prefixes = (
        "PMID:",
        "DOI:",
        "clinicaltrials:",
        "file:",
        "url:",
        "GEO:",
        "ORPHA:",
        "CGGV:",
        "CGDS:",
        "CIVIC_ASSERTION:",
        "CIVIC_EID:",
    )
    allowed_prefix_message = ", ".join(allowed_reference_prefixes)

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
                for prefix in allowed_reference_prefixes
            ):
                errors.append(
                    f"{path}[{i}]: reference should start with {allowed_prefix_message}: got {item['reference']}"
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


def test_discussion_knowledge_gap_proposed_experiment_validates(validator):
    """Knowledge-gap discussions can carry structured proposed experiments."""
    data = {
        "name": "Test Disease",
        "discussions": [
            {
                "discussion_id": "gap_test_mechanism",
                "prompt": "Which experiment would resolve the missing mechanism?",
                "kind": "KNOWLEDGE_GAP",
                "status": "OPEN",
                "attaches_to": ["pathophysiology#Missing Mechanism"],
                "proposed_experiments": [
                    {
                        "experiment_id": "exp_test",
                        "name": "Isogenic perturbation assay",
                        "experiment_type": {
                            "preferred_term": "controlled perturbation experiment"
                        },
                        "model_systems": [
                            {
                                "name": "Human organ-on-chip model",
                                "experimental_model_type": "ORGAN_ON_CHIP",
                                "namo_type": "namo:OrganOnChip",
                                "organism": {
                                    "preferred_term": "human",
                                    "term": {
                                        "id": "NCBITaxon:9606",
                                        "label": "Homo sapiens",
                                    },
                                },
                            }
                        ],
                        "perturbations": [
                            {
                                "name": "Gene correction",
                                "target": "gene#TEST1",
                                "gene": {"preferred_term": "TEST1"},
                            }
                        ],
                        "readouts": [
                            {
                                "name": "Cell-state readout",
                                "target": "pathophysiology#Missing Mechanism",
                                "biological_processes": [
                                    {
                                        "preferred_term": "autophagy",
                                        "term": {
                                            "id": "GO:0006914",
                                            "label": "autophagy",
                                        },
                                    }
                                ],
                                "direction": "POSITIVE",
                            }
                        ],
                        "controls": [{"name": "Isogenic wild-type control"}],
                        "decision_criterion": "Rescue should normalize the readout.",
                        "would_support": ["pathophysiology#Missing Mechanism"],
                    }
                ],
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


def test_treatment_action_category_validates(validator):
    """Treatment entries may be categorized as broader medical actions."""
    data = {
        "name": "Test Disease",
        "treatments": [
            {
                "name": "Newborn screening",
                "action_category": "SCREENING",
                "treatment_term": {
                    "preferred_term": "disease screening",
                    "term": {"id": "MAXO:0000124", "label": "disease screening"},
                },
            }
        ],
    }

    report = validator.validate(data, target_class="Disease")
    errors = [r for r in report.results if r.severity.name == "ERROR"]

    assert not errors, f"Validation errors: {[str(e) for e in errors]}"


def test_non_therapeutic_action_target_check_catches_counseling():
    """Annotated non-therapeutic actions must not link as pathograph treatments."""
    data = {
        "name": "Test Disease",
        "treatments": [
            {
                "name": "Genetic counseling",
                "action_category": "COUNSELING_INFORMATIONAL",
                "target_mechanisms": [{"target": "Primary mechanism"}],
            }
        ],
    }

    errors = _non_therapeutic_action_target_errors(data)

    assert errors
    assert "Genetic counseling" in errors[0]
    assert "target_mechanisms" in errors[0]


def test_non_therapeutic_action_target_check_catches_screening_phenotypes():
    """Non-therapeutic actions must not use phenotype targets that render as treats edges."""
    data = {
        "name": "Test Disease",
        "treatments": [
            {
                "name": "Newborn screening",
                "action_category": "SCREENING",
                "target_phenotypes": [{"preferred_term": "Screening marker"}],
            }
        ],
    }

    errors = _non_therapeutic_action_target_errors(data)

    assert errors
    assert "Newborn screening" in errors[0]
    assert "target_phenotypes" in errors[0]


def test_therapeutic_action_target_check_allows_mechanism_targets():
    """Therapeutic actions may continue to target pathophysiology nodes."""
    data = {
        "name": "Test Disease",
        "treatments": [
            {
                "name": "Enzyme replacement",
                "action_category": "THERAPEUTIC",
                "target_mechanisms": [{"target": "Primary mechanism"}],
            }
        ],
    }

    assert not _non_therapeutic_action_target_errors(data)


@pytest.mark.parametrize("filepath", DISORDER_FILES)
def test_non_therapeutic_actions_do_not_use_treatment_targets(filepath):
    """Annotated non-therapeutic medical actions must not use treatment-style target links."""
    with open(filepath) as f:
        data = yaml.safe_load(f)

    errors = _non_therapeutic_action_target_errors(data)

    assert not errors, (
        f"Non-therapeutic action target links in {Path(filepath).name}: {errors}"
    )


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


def test_reference_range_on_biochemical_validates(validator):
    """ReferenceRange entries on a Biochemical block should pass schema validation."""
    data = {
        "name": "Test Disease",
        "biochemical": [
            {
                "name": "Serum Potassium",
                "reference_ranges": [
                    {
                        "loinc_term": {
                            "id": "LOINC:2823-3",
                            "label": "Potassium [Moles/volume] in Serum or Plasma",
                        },
                        "lower_bound": 3.5,
                        "upper_bound": 5.0,
                        "unit": "mmol/L",
                        "population": "adults",
                        "source": "KDIGO 2017",
                    }
                ],
            }
        ],
    }
    report = validator.validate(data, target_class="Disease")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, f"Unexpected validation errors: {[str(e) for e in errors]}"


def test_reference_range_interpretation_bands_validate(validator):
    """Graded interpretation bands on a ReferenceRange should pass validation."""
    data = {
        "name": "Test Disease",
        "biochemical": [
            {
                "name": "Hemoglobin",
                "reference_ranges": [
                    {
                        "loinc_term": {
                            "id": "LOINC:718-7",
                            "label": "Hemoglobin [Mass/volume] in Blood",
                        },
                        "lower_bound": 12.0,
                        "upper_bound": 16.0,
                        "unit": "g/dL",
                        "population": "adult female",
                        "interpretation_bands": [
                            {
                                "name": "Severe",
                                "upper_bound": 8.0,
                                "unit": "g/dL",
                                "abnormal_flag": "CRITICAL_LOW",
                                "severity": "SEVERE",
                                "interpretation": "Severe anemia.",
                            },
                            {
                                "name": "Moderate",
                                "lower_bound": 8.0,
                                "upper_bound": 11.0,
                                "unit": "g/dL",
                                "abnormal_flag": "LOW",
                                "severity": "MODERATE",
                            },
                            {
                                "name": "Mild",
                                "lower_bound": 11.0,
                                "upper_bound": 12.0,
                                "unit": "g/dL",
                                "abnormal_flag": "LOW",
                                "severity": "MILD",
                            },
                            {
                                "name": "Normal",
                                "lower_bound": 12.0,
                                "upper_bound": 16.0,
                                "unit": "g/dL",
                                "abnormal_flag": "NORMAL",
                            },
                        ],
                    }
                ],
            }
        ],
    }
    report = validator.validate(data, target_class="Disease")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, f"Unexpected validation errors: {[str(e) for e in errors]}"


def test_disorder_count():
    """Test that we have the expected number of disorders."""
    assert len(DISORDER_FILES) >= 50, (
        f"Expected at least 50 disorders, got {len(DISORDER_FILES)}"
    )


# --- Disease grouping tests ---


def _iter_logic_nodes(node):
    """Yield every LogicalCriterion node in a (possibly nested) expression."""
    if not isinstance(node, dict):
        return
    yield node
    for child in node.get("operands", []) or []:
        yield from _iter_logic_nodes(child)


def _module_stem(ref):
    """Strip an optional '#Node Name' anchor from a module reference."""
    return ref.split("#", 1)[0].strip() if ref else ref


@pytest.mark.parametrize("filepath", GROUPING_FILES)
def test_valid_grouping_files(filepath, validator):
    """All grouping files validate against the Grouping class."""
    with open(filepath) as f:
        data = yaml.safe_load(f)

    report = validator.validate(data, target_class="Grouping")
    errors = [r for r in report.results if r.severity.name == "ERROR"]

    assert not errors, f"Validation errors in {filepath}: {[str(e) for e in errors]}"


@pytest.mark.parametrize("filepath", GROUPING_FILES)
def test_grouping_member_foreign_keys(filepath):
    """Each grouping member must resolve to a real Disease, module, or grouping."""
    with open(filepath) as f:
        data = yaml.safe_load(f)

    disease_names = _disease_names()
    module_stems = _module_stems()
    grouping_names = _grouping_names()

    errors = []
    for i, member in enumerate(data.get("members", [])):
        ref = member.get("member")
        mtype = member.get("member_type", "DISEASE")
        if not ref:
            continue
        if mtype in ("DISEASE", "SUBTYPE"):
            # SUBTYPE members still name their parent Disease entry.
            if ref not in disease_names:
                errors.append(f"members[{i}].member={ref!r} (type {mtype})")
        elif mtype == "MODULE":
            if _module_stem(ref) not in module_stems:
                errors.append(f"members[{i}].member={ref!r} (type MODULE)")
        elif mtype == "GROUPING":
            if ref not in grouping_names:
                errors.append(f"members[{i}].member={ref!r} (type GROUPING)")

    assert not errors, (
        f"Grouping member FK mismatches in {Path(filepath).name}. Bad refs: {errors}"
    )


@pytest.mark.parametrize("filepath", GROUPING_FILES)
def test_grouping_module_references(filepath):
    """Every `module` reference in a grouping must resolve to a module file."""
    with open(filepath) as f:
        data = yaml.safe_load(f)

    module_stems = _module_stems()
    errors = []

    # Module refs inside the structured membership criteria expressions.
    for c, criteria in enumerate(data.get("membership_criteria", []) or []):
        for node in _iter_logic_nodes(criteria.get("logic")):
            ref = node.get("module")
            if ref and _module_stem(ref) not in module_stems:
                errors.append(f"membership_criteria[{c}].logic module={ref!r}")

    # Module refs inside per-member differentiating mechanisms.
    for i, member in enumerate(data.get("members", [])):
        for j, mech in enumerate(member.get("differentiating_mechanisms", []) or []):
            ref = mech.get("module")
            if ref and _module_stem(ref) not in module_stems:
                errors.append(
                    f"members[{i}].differentiating_mechanisms[{j}].module={ref!r}"
                )

    assert not errors, (
        f"Grouping module reference mismatches in {Path(filepath).name}. "
        f"Bad refs: {errors}"
    )


def test_grouping_unique_names():
    """Grouping `name` values must be unique across kb/groupings/."""
    seen = {}
    for fp in GROUPING_FILES:
        with open(fp) as f:
            data = yaml.safe_load(f)
        name = data.get("name") if isinstance(data, dict) else None
        if name:
            seen.setdefault(name, []).append(Path(fp).name)
    dupes = {k: v for k, v in seen.items() if len(v) > 1}
    assert not dupes, f"Duplicate grouping names: {dupes}"


@pytest.mark.parametrize("filepath", GROUPING_FILES)
def test_grouping_criteria_well_formed(filepath):
    """Structured membership-criteria expressions must be well-formed.

    Each LogicalCriterion node must be either a BRANCH (operator + operands) or
    a LEAF (criterion_predicate + matching payload), never both or neither.
    """
    from dismech.groupings import lint_criterion

    with open(filepath) as f:
        data = yaml.safe_load(f)

    errors = []
    for c, criteria in enumerate(data.get("membership_criteria", []) or []):
        errors.extend(
            lint_criterion(criteria.get("logic"), f"membership_criteria[{c}].logic")
        )
    assert not errors, f"Malformed criteria in {Path(filepath).name}: {errors}"


def test_grouping_node_classification():
    """classify_node distinguishes BRANCH, LEAF, and INVALID nodes."""
    from dismech.groupings import NodeKind, classify_node

    assert classify_node({"operator": "AND", "operands": []}) is NodeKind.BRANCH
    assert classify_node({"criterion_predicate": "HAS_GENE"}) is NodeKind.LEAF
    # Both operator and predicate -> invalid.
    assert (
        classify_node({"operator": "AND", "criterion_predicate": "HAS_GENE"})
        is NodeKind.INVALID
    )
    # Neither -> invalid.
    assert classify_node({"description": "x"}) is NodeKind.INVALID


def test_grouping_lint_catches_bad_nodes():
    """The structural linter flags malformed leaves and branches."""
    from dismech.groupings import lint_criterion

    # Leaf predicate missing its required payload.
    assert lint_criterion({"criterion_predicate": "HAS_GENE"})
    # Branch operator with no operands.
    assert lint_criterion({"operator": "AND", "operands": []})
    # A well-formed expression yields no errors.
    good = {
        "operator": "AND",
        "operands": [
            {
                "criterion_predicate": "HAS_GENE",
                "gene": {"term": {"id": "hgnc:5391"}},
            }
        ],
    }
    assert lint_criterion(good) == []


def test_grouping_three_valued_logic():
    """AND/OR/NOT combine SATISFIED/NOT_SATISFIED/UNKNOWN correctly."""
    from dismech.groupings import (
        DiseaseFacts,
        Satisfaction,
        _eval_node,
    )

    facts = DiseaseFacts(name="x", gene_ids={"hgnc:5391"}, go_ids={"GO:0006027"})

    has_gene = {
        "criterion_predicate": "HAS_GENE",
        "gene": {"term": {"id": "hgnc:5391"}},
    }
    missing_gene = {
        "criterion_predicate": "HAS_GENE",
        "gene": {"term": {"id": "hgnc:9999"}},
    }
    unknown = {"criterion_predicate": "OTHER", "description": "unscored"}

    assert _eval_node(has_gene, facts) is Satisfaction.SATISFIED
    assert _eval_node(missing_gene, facts) is Satisfaction.NOT_SATISFIED
    assert _eval_node(unknown, facts) is Satisfaction.UNKNOWN

    # AND: a NOT_SATISFIED operand dominates.
    assert (
        _eval_node({"operator": "AND", "operands": [has_gene, missing_gene]}, facts)
        is Satisfaction.NOT_SATISFIED
    )
    # OR: a SATISFIED operand dominates.
    assert (
        _eval_node({"operator": "OR", "operands": [has_gene, missing_gene]}, facts)
        is Satisfaction.SATISFIED
    )
    # NOT flips.
    assert (
        _eval_node({"operator": "NOT", "operands": [missing_gene]}, facts)
        is Satisfaction.SATISFIED
    )
    # negated leaf flips.
    negated = dict(missing_gene, negated=True)
    assert _eval_node(negated, facts) is Satisfaction.SATISFIED


@pytest.mark.parametrize("filepath", GROUPING_FILES)
def test_grouping_evaluation_runs(filepath):
    """The membership evaluator executes and returns structured results.

    This is advisory (criteria may be aspirational), so it asserts the evaluator
    runs and produces valid Satisfaction values, not that members satisfy.
    """
    from dismech.groupings import (
        Satisfaction,
        evaluate_grouping,
        load_disease_index,
    )

    with open(filepath) as f:
        grouping = yaml.safe_load(f)

    index = load_disease_index()
    for ev in evaluate_grouping(grouping, index):
        assert isinstance(ev.result, Satisfaction)
