"""Data validation tests for dismech KB."""

import glob
import sys
import warnings
from collections import Counter
from functools import lru_cache
from pathlib import Path

import pytest
import yaml
from linkml.validator import Validator

# scripts/ is not a package; make its modules importable for tests that reuse
# validation logic shared with the CLI tools.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from dismech.yaml_io import safe_load

# Paths
ROOT_DIR = Path(__file__).parent.parent
SCHEMA_PATH = ROOT_DIR / "src" / "dismech" / "schema" / "dismech.yaml"
KB_DIR = ROOT_DIR / "kb" / "disorders"
COMORBIDITY_DIR = ROOT_DIR / "kb" / "comorbidities"
MODULES_DIR = ROOT_DIR / "kb" / "modules"
GROUPINGS_DIR = ROOT_DIR / "kb" / "groupings"
SYNTHESIS_SCHEMA_PATH = (
    ROOT_DIR / "src" / "dismech" / "schema" / "research_synthesis.yaml"
)
HYPOTHESIS_ASSESSMENT_SCHEMA_PATH = (
    ROOT_DIR / "src" / "dismech" / "schema" / "hypothesis_assessment.yaml"
)
RESEARCH_DIR = ROOT_DIR / "research"
HYPOTHESES_DIR = ROOT_DIR / "kb" / "hypotheses"

# Get all disorder YAML files (exclude history snapshots)
DISORDER_FILES = [
    f for f in glob.glob(str(KB_DIR / "*.yaml")) if not f.endswith(".history.yaml")
]
COMORBIDITY_FILES = glob.glob(str(COMORBIDITY_DIR / "*.yaml"))
GROUPING_FILES = glob.glob(str(GROUPINGS_DIR / "*.yaml"))
MODULE_FILES = glob.glob(str(MODULES_DIR / "*.yaml"))
# Every KB entry kind whose pathophysiology nodes may carry `conforms_to`.
# Groupings are excluded: they reference modules through criteria `module:`
# slots (checked by test_grouping_module_references), not `conforms_to`.
CONFORMS_TO_FILES = DISORDER_FILES + MODULE_FILES + COMORBIDITY_FILES
# Modules use the same Disease class and carry the same model sections, so
# model-link checks span both trees. The two older per-section foreign-key tests
# above predate this and still cover disorders only.
MODEL_BEARING_FILES = DISORDER_FILES + MODULE_FILES
# Model sections whose entries may carry `modeled_mechanisms` links.
MODEL_SECTIONS = ("experimental_models", "animal_models", "computational_models")
SYNTHESIS_FILES = glob.glob(str(RESEARCH_DIR / "*-research-synthesis.yaml"))
HYPOTHESIS_ASSESSMENT_FILES = glob.glob(
    str(HYPOTHESES_DIR / "*" / "*" / "assessments" / "*-assessment-by-*.yaml")
)

# Reference prefixes an evidence `reference:` may carry: literature/registry
# sources the reference validator fetches and snippet-checks, plus the structured
# database sources pre-cached under references_cache/ (see CLAUDE.md), plus the
# dataset-accession prefixes listed as `skip_prefixes` in
# conf/reference_validator_config.yaml. Compared case-insensitively -- the
# validator normalizes prefix case itself, and the KB uses both `GEO:` and `geo:`.
ALLOWED_REFERENCE_PREFIXES = (
    "PMID:",
    "DOI:",
    "PPR:",  # Europe PMC preprint IDs (supported by the reference validator)
    "clinicaltrials:",
    "file:",
    "url:",
    "GEO:",
    "ORPHA:",
    "CGGV:",
    "CGDS:",
    "CIVIC_ASSERTION:",
    "CIVIC_EID:",
    "ICEES:",  # ICEES KG comorbidity pairs
    "ICTRP:",  # WHO ICTRP trial registrations (ChiCTR, ISRCTN, EUCTR, JPRN, ...)
    "NCIT:",  # NCI Thesaurus predicate edges (e.g. NCIT:P302 therapeutic use)
    "metabolights:",  # dataset accession; skip_prefixes in the validator config
)


def _has_allowed_reference_prefix(reference):
    """True if `reference` starts with one of ALLOWED_REFERENCE_PREFIXES."""
    text = str(reference).lower()
    return any(text.startswith(p.lower()) for p in ALLOWED_REFERENCE_PREFIXES)


def _iter_evidence_lists(node, path=""):
    """Yield every ``(dotted_path, evidence_list)`` pair anywhere in a document.

    Evidence blocks are attached at many depths (top-level sections, nested
    `downstream` causal edges, `readouts`, `findings`, `members`, ...), so the
    only reliable way to check them all is to walk the whole tree.
    """
    if isinstance(node, dict):
        for key, value in node.items():
            child = f"{path}.{key}" if path else key
            if key == "evidence" and isinstance(value, list):
                yield child, value
            yield from _iter_evidence_lists(value, child)
    elif isinstance(node, list):
        for index, item in enumerate(node):
            yield from _iter_evidence_lists(item, f"{path}[{index}]")


@lru_cache(maxsize=1)
def _disease_names():
    """Set of all Disease `name` values across kb/disorders/.

    Cached: this parses every file in kb/disorders/ (~2 minutes for the current
    corpus) and is called once per parametrization of the grouping foreign-key
    test, i.e. once per grouping. Uncached, that test alone took hours.
    """
    names = set()
    for fp in DISORDER_FILES:
        with open(fp) as f:
            data = safe_load(f)
        if isinstance(data, dict) and data.get("name"):
            names.add(data["name"])
    return names


def _module_stems():
    """Set of mechanism module filename stems (without .yaml) in kb/modules/."""
    return {Path(f).stem for f in glob.glob(str(MODULES_DIR / "*.yaml"))}


@lru_cache(maxsize=1)
def _module_node_names():
    """Map each module stem to the set of its pathophysiology node names.

    Used to resolve the `#Node Name` anchor of a `conforms_to` reference, which
    `_module_stems()` alone cannot check.
    """
    nodes = {}
    for fp in glob.glob(str(MODULES_DIR / "*.yaml")):
        with open(fp) as f:
            data = safe_load(f)
        if not isinstance(data, dict):
            continue
        nodes[Path(fp).stem] = {
            node.get("name")
            for node in data.get("pathophysiology") or []
            if isinstance(node, dict) and node.get("name")
        }
    return nodes


def _iter_conforms_to(node, path=""):
    """Yield every ``(dotted_path, conforms_to_value)`` pair in a document.

    `conforms_to` hangs off pathophysiology nodes, which appear at more than one
    depth across entry kinds, so the whole tree is walked rather than one slot.
    """
    if isinstance(node, dict):
        for key, value in node.items():
            child = f"{path}.{key}" if path else key
            if key == "conforms_to" and isinstance(value, str) and value.strip():
                yield child, value
            yield from _iter_conforms_to(value, child)
    elif isinstance(node, list):
        for index, item in enumerate(node):
            yield from _iter_conforms_to(item, f"{path}[{index}]")


@lru_cache(maxsize=1)
def _grouping_names():
    """Set of Grouping `name` values across kb/groupings/."""
    names = set()
    for fp in GROUPING_FILES:
        with open(fp) as f:
            data = safe_load(f)
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


@pytest.mark.kb_data
@pytest.mark.parametrize("filepath", DISORDER_FILES)
def test_valid_disorder_files(filepath, validator):
    """Test that all disorder files validate against the schema."""
    with open(filepath) as f:
        data = safe_load(f)

    report = validator.validate(data, target_class="Disease")

    # ValidationReport has a results list with ValidationResult objects
    # Only errors are issues, not informational messages
    errors = [r for r in report.results if r.severity.name == "ERROR"]

    assert not errors, f"Validation errors in {filepath}: {[str(e) for e in errors]}"


@pytest.mark.kb_data
@pytest.mark.parametrize("filepath", COMORBIDITY_FILES)
def test_valid_comorbidity_files(filepath, validator):
    """Test that all comorbidity files validate against the schema."""
    with open(filepath) as f:
        data = safe_load(f)

    report = validator.validate(data, target_class="ComorbidityAssociation")
    errors = [r for r in report.results if r.severity.name == "ERROR"]

    assert not errors, f"Validation errors in {filepath}: {[str(e) for e in errors]}"


@pytest.mark.kb_data
@pytest.mark.parametrize("filepath", DISORDER_FILES)
def test_disorder_has_required_fields(filepath):
    """Test that all disorders have required fields."""
    with open(filepath) as f:
        data = safe_load(f)

    assert "name" in data, f"Missing 'name' in {filepath}"
    assert data["name"], f"Empty 'name' in {filepath}"


@pytest.mark.kb_data
@pytest.mark.parametrize("filepath", DISORDER_FILES)
def test_evidence_items_have_references(filepath):
    """Test that evidence items use supported reference prefixes."""
    with open(filepath) as f:
        data = safe_load(f)

    allowed_prefix_message = ", ".join(ALLOWED_REFERENCE_PREFIXES)

    def check_evidence(evidence_list, path):
        """Check one ``evidence:`` list for missing/unprefixed references."""
        errors = []
        for i, item in enumerate(evidence_list):
            if not isinstance(item, dict):
                continue
            reference = item.get("reference")
            if not reference:
                errors.append(f"{path}[{i}]: missing reference")
            elif not _has_allowed_reference_prefix(reference):
                errors.append(
                    f"{path}[{i}]: reference should start with {allowed_prefix_message}: got {reference}"
                )
        return errors

    all_errors = []

    # Walk the whole document rather than a hand-listed set of sections. The
    # earlier version checked only pathophysiology/phenotypes/has_subtypes/
    # prevalence/progression, so evidence under clinical_trials, treatments,
    # datasets, diagnosis, biochemical, histopathology (and nested slots such as
    # pathophysiology[].downstream[]) was never prefix-checked -- which is how the
    # unprefixed `NCT06087757` reference in dismech#7288 reached main.
    for path, evidence_list in _iter_evidence_lists(data):
        all_errors.extend(check_evidence(evidence_list, path))

    assert not all_errors, f"Evidence errors in {Path(filepath).name}: {all_errors}"


def test_schema_validity(validator):
    """Test that the schema itself is valid LinkML."""
    # If we got here without errors, schema is valid
    assert validator is not None


def test_biological_scale_enum_and_pathophysiology_slot():
    """BiologicalScaleEnum has exactly the 4 expected scale values, and the
    biological_scale slot is wired into Pathophysiology.

    Guards against silent enum drift — the value set is load-bearing for the
    feasibility analysis in projects/PATHOPHYSIOLOGY_SCALE_FEASIBILITY.md and
    should only change with a corresponding design update.
    """
    from linkml_runtime.utils.schemaview import SchemaView

    sv = SchemaView(str(SCHEMA_PATH))

    enum = sv.get_enum("BiologicalScaleEnum")
    assert enum is not None, "BiologicalScaleEnum missing from schema"
    assert set(enum.permissible_values.keys()) == {
        "MOLECULAR",
        "CELLULAR",
        "TISSUE",
        "ORGANISM",
    }, (
        "BiologicalScaleEnum values changed unexpectedly; if intentional, update "
        "this test and projects/PATHOPHYSIOLOGY_SCALE_FEASIBILITY.md"
    )

    slot = sv.get_slot("biological_scale")
    assert slot is not None, "biological_scale slot missing from schema"
    assert slot.range == "BiologicalScaleEnum", (
        f"biological_scale slot range should be BiologicalScaleEnum, got {slot.range}"
    )

    assert "biological_scale" in sv.class_slots("Pathophysiology"), (
        "biological_scale slot not wired into Pathophysiology class"
    )


def test_biological_scale_pathophysiology_accepts_enum_value(validator):
    """A Pathophysiology entry with a biological_scale value should validate."""
    data = {
        "name": "Test Disease",
        "pathophysiology": [
            {
                "name": "Test node",
                "biological_scale": "MOLECULAR",
            }
        ],
    }
    report = validator.validate(data, target_class="Disease")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, f"Validation errors: {[str(e) for e in errors]}"


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
                        "id": "NCIT:C15447",
                        "label": "Dietary Intervention",
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
                        "id": "NCIT:C15447",
                        "label": "Dietary Intervention",
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
                    "term": {"id": "NCIT:C15419", "label": "Disease Screening"},
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


@pytest.mark.kb_data
@pytest.mark.parametrize("filepath", DISORDER_FILES)
def test_non_therapeutic_actions_do_not_use_treatment_targets(filepath):
    """Annotated non-therapeutic medical actions must not use treatment-style target links."""
    with open(filepath) as f:
        data = safe_load(f)

    errors = _non_therapeutic_action_target_errors(data)

    assert not errors, (
        f"Non-therapeutic action target links in {Path(filepath).name}: {errors}"
    )


def test_all_disorders_have_unique_names():
    """Test that all disorder names are unique."""
    names = []
    for filepath in DISORDER_FILES:
        with open(filepath) as f:
            data = safe_load(f)
        names.append(data.get("name"))

    duplicates = [name for name in names if names.count(name) > 1]
    assert not duplicates, f"Duplicate disorder names: {set(duplicates)}"


@pytest.mark.kb_data
@pytest.mark.parametrize("filepath", DISORDER_FILES)
def test_subtype_foreign_keys(filepath):
    """Test that subtype references match has_subtypes names."""
    with open(filepath) as f:
        data = safe_load(f)

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


@pytest.mark.parametrize("filepath", DISORDER_FILES)
def test_hypothesis_based_definition_attaches_to_foreign_keys(filepath):
    """Hypothesis-based phenotype algorithms must anchor in the pathograph (#6245).

    A `definitions[]` entry whose `derivation_basis` is MECHANISTIC_HYPOTHESIS
    is predicated on a specific disease mechanism, so it must `attaches_to` at
    least one node it operationalizes, and any *local* `pathophysiology#<name>`
    or `phenotype#<name>` reference must resolve to a real node/phenotype in the
    same entry (the same hash-anchor discipline `discussions.attaches_to` uses).
    Cross-file references (`<file>:<kind>#<name>`) are not resolved here.
    """
    with open(filepath) as f:
        data = safe_load(f)

    definitions = data.get("definitions", []) or []
    if not definitions:
        return

    patho_names = {n.get("name") for n in data.get("pathophysiology", []) or []}
    pheno_names = {p.get("name") for p in data.get("phenotypes", []) or []}

    errors = []
    for i, defn in enumerate(definitions):
        if defn.get("derivation_basis") != "MECHANISTIC_HYPOTHESIS":
            continue
        refs = defn.get("attaches_to", []) or []
        if not refs:
            errors.append(
                f"definitions[{i}] ({defn.get('name')!r}) has "
                f"derivation_basis: MECHANISTIC_HYPOTHESIS but no attaches_to"
            )
            continue
        for ref in refs:
            if "#" not in ref:
                errors.append(f"definitions[{i}].attaches_to={ref!r} lacks '#'")
                continue
            left, name = ref.split("#", 1)
            if ":" in left:
                # Cross-file reference — not resolved here.
                continue
            kind = left
            if kind == "pathophysiology" and name not in patho_names:
                errors.append(
                    f"definitions[{i}].attaches_to={ref!r} does not resolve to a "
                    f"pathophysiology node"
                )
            elif kind == "phenotype" and name not in pheno_names:
                errors.append(
                    f"definitions[{i}].attaches_to={ref!r} does not resolve to a "
                    f"phenotype"
                )

    assert not errors, (
        f"Hypothesis-based definition FK problems in {Path(filepath).name}: {errors}"
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


@pytest.mark.kb_data
@pytest.mark.parametrize("filepath", DISORDER_FILES)
def test_experimental_model_mechanism_targets(filepath):
    """Experimental model links should reference declared pathophysiology nodes."""
    with open(filepath) as f:
        data = safe_load(f)

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


@pytest.mark.kb_data
@pytest.mark.parametrize("filepath", DISORDER_FILES)
def test_computational_model_mechanism_targets(filepath):
    """Computational model links should reference declared pathophysiology nodes."""
    with open(filepath) as f:
        data = safe_load(f)

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


@pytest.mark.kb_data
@pytest.mark.parametrize("filepath", MODEL_BEARING_FILES)
def test_animal_model_mechanism_targets(filepath):
    """Animal model links should reference declared pathophysiology nodes."""
    with open(filepath) as f:
        data = safe_load(f)

    valid_targets = {
        item["name"]
        for item in data.get("pathophysiology", [])
        if isinstance(item, dict) and item.get("name")
    }
    if not valid_targets:
        return

    errors = []
    for i, model in enumerate(data.get("animal_models", [])):
        for j, link in enumerate(model.get("modeled_mechanisms", [])):
            target = link.get("target")
            if target and target not in valid_targets:
                errors.append(
                    f"animal_models[{i}].modeled_mechanisms[{j}].target={target!r}"
                )

    assert not errors, (
        f"Animal model mechanism mismatches in {Path(filepath).name}. "
        f"Valid targets: {valid_targets}. Bad refs: {errors}"
    )


def _animal_model_label(model):
    """Mirror of dismech.graph.animal_model_label, kept dependency-free here."""
    name = str(model.get("name") or "").strip()
    if name:
        return name
    parts = [
        str(model.get(key)).strip()
        for key in ("genotype", "species")
        if str(model.get(key) or "").strip()
    ]
    return " ".join(parts) or None


@pytest.mark.kb_data
@pytest.mark.parametrize("filepath", MODEL_BEARING_FILES)
def test_linked_animal_model_labels_are_unique(filepath):
    """An animal model that reaches the pathograph needs an unambiguous label.

    `AnimalModel` is the only pathograph-bearing class whose node identity is
    *derived* (`animal_model_label`) rather than a required `name`. Two models
    sharing a derived label collapse into one graph node -- the second
    description silently overwrites the first -- and render with the same HTML
    anchor id, so card links land on the wrong one.

    Gated on `modeled_mechanisms` deliberately: the ~400 legacy entries with no
    `name`, several of which do collide on species alone, are untouched until
    someone links them. This is what gives the "`name` is recommended once a
    model carries mechanism links" guidance teeth.
    """
    with open(filepath) as f:
        data = safe_load(f)

    models = [m for m in (data.get("animal_models") or []) if isinstance(m, dict)]
    label_counts = Counter(
        label for m in models if (label := _animal_model_label(m)) is not None
    )

    errors = [
        f"animal_models[{i}] label={label!r} is shared by "
        f"{label_counts[label]} models in this file; give it a `name`"
        for i, m in enumerate(models)
        if m.get("modeled_mechanisms")
        and (label := _animal_model_label(m)) is not None
        and label_counts[label] > 1
    ]

    assert not errors, (
        f"Ambiguous animal model labels in {Path(filepath).name}: {errors}"
    )


def _iter_mechanism_links(data):
    """Yield (section, model_index, link_index, model, link) across model sections."""
    for section in MODEL_SECTIONS:
        for i, model in enumerate(data.get(section, []) or []):
            if not isinstance(model, dict):
                continue
            for j, link in enumerate(model.get("modeled_mechanisms", []) or []):
                if isinstance(link, dict):
                    yield section, i, j, model, link


@pytest.mark.kb_data
@pytest.mark.parametrize("filepath", MODEL_BEARING_FILES)
def test_model_readout_targets_match_link(filepath):
    """A readout's target must repeat its link's target.

    `target` is required on ExperimentalReadout so a readout stays
    self-describing once the graph and KGX exporters lift it out of its link.
    That redundancy only holds if the two agree, so drift is an error.
    """
    with open(filepath) as f:
        data = safe_load(f)

    errors = []
    for section, i, j, _model, link in _iter_mechanism_links(data):
        link_target = link.get("target")
        for k, readout in enumerate(link.get("readouts", []) or []):
            if not isinstance(readout, dict):
                continue
            readout_target = readout.get("target")
            if readout_target != link_target:
                errors.append(
                    f"{section}[{i}].modeled_mechanisms[{j}].readouts[{k}]"
                    f".target={readout_target!r} != link target {link_target!r}"
                )

    assert not errors, f"Model readout target drift in {Path(filepath).name}: {errors}"


@pytest.mark.kb_data
@pytest.mark.parametrize("filepath", MODEL_BEARING_FILES)
def test_failure_to_recapitulate_links_are_substantiated(filepath):
    """FAILS_TO_RECAPITULATE is a negative claim and must be substantiated.

    Link evidence is only `recommended` in general, so incremental curation of
    the existing model entries is not blocked. Asserting that a model does NOT
    reproduce a human mechanism is a different matter: it is the structural
    signal behind a HUMAN_MODEL_MISMATCH discussion, so it requires both the
    caveat (`limitations`) and a citation.
    """
    with open(filepath) as f:
        data = safe_load(f)

    errors = []
    for section, i, j, _model, link in _iter_mechanism_links(data):
        if link.get("relationship") != "FAILS_TO_RECAPITULATE":
            continue
        where = f"{section}[{i}].modeled_mechanisms[{j}]"
        if not (link.get("limitations") or "").strip():
            errors.append(f"{where} missing limitations")
        if not link.get("evidence"):
            errors.append(f"{where} missing evidence")

    assert not errors, (
        f"Unsubstantiated FAILS_TO_RECAPITULATE links in "
        f"{Path(filepath).name}: {errors}"
    )


def test_duplicate_linked_animal_model_labels_are_caught(tmp_path):
    """Two linked models sharing a derived label must be caught.

    Without `name`, both collapse onto the same graph node and the same HTML
    anchor id. An unlinked duplicate is left alone -- that is the ~400 legacy
    entries, and flagging them would be noise.
    """
    disease = {
        "name": "Colliding Animal Labels",
        "pathophysiology": [{"name": "Real Node"}],
        "animal_models": [
            {
                "species": "Mus musculus",
                "description": "First mouse",
                "modeled_mechanisms": [{"target": "Real Node"}],
            },
            {
                "species": "Mus musculus",
                "description": "Second mouse",
                "modeled_mechanisms": [{"target": "Real Node"}],
            },
        ],
    }
    fake_path = tmp_path / "CollidingLabels.yaml"
    fake_path.write_text(yaml.safe_dump(disease, sort_keys=False))

    with pytest.raises(AssertionError, match="Mus musculus"):
        test_linked_animal_model_labels_are_unique(str(fake_path))


def test_unlinked_duplicate_animal_model_labels_are_allowed(tmp_path):
    """The legacy case: same derived label, no mechanism links, no complaint."""
    disease = {
        "name": "Legacy Duplicates",
        "pathophysiology": [{"name": "Real Node"}],
        "animal_models": [
            {"species": "Mus musculus", "description": "First"},
            {"species": "Mus musculus", "description": "Second"},
        ],
    }
    fake_path = tmp_path / "LegacyDuplicates.yaml"
    fake_path.write_text(yaml.safe_dump(disease, sort_keys=False))

    test_linked_animal_model_labels_are_unique(str(fake_path))


def test_animal_model_mechanism_fk_catches_bad_refs(tmp_path):
    """An animal-model link pointing at an undeclared node must be caught."""
    disease = {
        "name": "Bad Animal Link",
        "pathophysiology": [{"name": "Real Node"}],
        "animal_models": [
            {
                "name": "Probe mouse",
                "species": "Mus musculus",
                "modeled_mechanisms": [{"target": "Node 99 (not declared)"}],
            }
        ],
    }
    fake_path = tmp_path / "BadAnimalLink.yaml"
    fake_path.write_text(yaml.safe_dump(disease, sort_keys=False))

    with pytest.raises(AssertionError, match="Node 99"):
        test_animal_model_mechanism_targets(str(fake_path))


def test_readout_target_drift_is_caught(tmp_path):
    """A readout target that disagrees with its link target must be caught."""
    disease = {
        "name": "Drifted Readout",
        "pathophysiology": [{"name": "Real Node"}, {"name": "Other Node"}],
        "animal_models": [
            {
                "name": "Probe mouse",
                "species": "Mus musculus",
                "modeled_mechanisms": [
                    {
                        "target": "Real Node",
                        "readouts": [{"name": "R", "target": "Other Node"}],
                    }
                ],
            }
        ],
    }
    fake_path = tmp_path / "DriftedReadout.yaml"
    fake_path.write_text(yaml.safe_dump(disease, sort_keys=False))

    with pytest.raises(AssertionError, match="Other Node"):
        test_model_readout_targets_match_link(str(fake_path))


def test_unsubstantiated_failure_to_recapitulate_is_caught(tmp_path):
    """FAILS_TO_RECAPITULATE without limitations or evidence must be caught."""
    disease = {
        "name": "Bare Negative Claim",
        "pathophysiology": [{"name": "Real Node"}],
        "experimental_models": [
            {
                "name": "Probe organoid",
                "modeled_mechanisms": [
                    {
                        "target": "Real Node",
                        "relationship": "FAILS_TO_RECAPITULATE",
                    }
                ],
            }
        ],
    }
    fake_path = tmp_path / "BareNegative.yaml"
    fake_path.write_text(yaml.safe_dump(disease, sort_keys=False))

    with pytest.raises(AssertionError, match="missing limitations"):
        test_failure_to_recapitulate_links_are_substantiated(str(fake_path))


@pytest.mark.kb_data
@pytest.mark.parametrize("filepath", DISORDER_FILES)
def test_environmental_mechanism_targets(filepath):
    """Environmental factor links should reference declared pathograph nodes."""
    with open(filepath) as f:
        data = yaml.safe_load(f)

    # Pathophysiology is the preferred target, but phenotype targets are
    # allowed for exposures acting directly on a manifestation.
    valid_targets = {
        item["name"]
        for section in ("pathophysiology", "phenotypes")
        for item in data.get(section, []) or []
        if isinstance(item, dict) and item.get("name")
    }
    if not valid_targets:
        return

    errors = []
    for i, factor in enumerate(data.get("environmental", []) or []):
        if not isinstance(factor, dict):
            continue
        for j, link in enumerate(factor.get("influences_mechanisms", []) or []):
            target = link.get("target")
            if target and target not in valid_targets:
                errors.append(
                    f"environmental[{i}].influences_mechanisms[{j}].target={target!r}"
                )

    assert not errors, (
        f"Environmental mechanism mismatches in {Path(filepath).name}. "
        f"Valid targets: {valid_targets}. Bad refs: {errors}"
    )


@pytest.mark.kb_data
@pytest.mark.parametrize("filepath", DISORDER_FILES)
def test_subtypes_have_disease_term(filepath):
    """Test that has_subtypes items have a subtype_term with an ontology grounding.

    Each subtype should be grounded to a MONDO or NCIT disease term via
    the subtype_term descriptor so that subtypes are machine-queryable.
    """
    with open(filepath) as f:
        data = safe_load(f)

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
                        "evidence": [
                            {
                                "reference": "PMID:12345678",
                                "supports": "SUPPORT",
                                "snippet": "serum potassium reference interval",
                            }
                        ],
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


def test_reference_range_band_rejects_invalid_abnormal_flag():
    """An out-of-enum abnormal_flag on a band must fail strict validation.

    Uses a closed jsonschema validator because the lenient module-scoped
    ``validator`` fixture does not enforce enum membership.
    """
    from linkml.validator import Validator as _Validator
    from linkml.validator.plugins import JsonschemaValidationPlugin

    strict = _Validator(
        SCHEMA_PATH, validation_plugins=[JsonschemaValidationPlugin(closed=True)]
    )
    data = {
        "name": "Test Disease",
        "biochemical": [
            {
                "name": "Serum Calcium",
                "reference_ranges": [
                    {
                        "lower_bound": 8.5,
                        "upper_bound": 10.5,
                        "unit": "mg/dL",
                        "interpretation_bands": [
                            {
                                "name": "Bogus",
                                "lower_bound": 10.5,
                                "abnormal_flag": "PANIC",  # not in AbnormalFlagEnum
                            }
                        ],
                    }
                ],
            }
        ],
    }
    report = strict.validate(data, target_class="Disease")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert errors, "Expected a validation error for an invalid abnormal_flag value"


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


@pytest.mark.kb_data
@pytest.mark.parametrize("filepath", GROUPING_FILES)
def test_valid_grouping_files(filepath, validator):
    """All grouping files validate against the Grouping class."""
    with open(filepath) as f:
        data = safe_load(f)

    report = validator.validate(data, target_class="Grouping")
    errors = [r for r in report.results if r.severity.name == "ERROR"]

    assert not errors, f"Validation errors in {filepath}: {[str(e) for e in errors]}"


@pytest.fixture(scope="module")
def synthesis_validator():
    """Validator bound to the standalone research-synthesis schema."""
    return Validator(SYNTHESIS_SCHEMA_PATH)


@pytest.mark.kb_data
@pytest.mark.parametrize("filepath", SYNTHESIS_FILES)
def test_valid_research_synthesis_files(filepath, synthesis_validator):
    """All research-synthesis files validate against the ResearchSynthesis class."""
    with open(filepath) as f:
        data = safe_load(f)

    report = synthesis_validator.validate(data, target_class="ResearchSynthesis")
    errors = [r for r in report.results if r.severity.name == "ERROR"]

    assert not errors, f"Validation errors in {filepath}: {[str(e) for e in errors]}"


@pytest.mark.kb_data
@pytest.mark.parametrize("filepath", SYNTHESIS_FILES)
def test_synthesis_provider_references_resolve(filepath):
    """Every provider_support.provider must be declared in the top-level providers list."""
    with open(filepath) as f:
        data = safe_load(f)

    declared = {p.get("name") for p in data.get("providers", []) or []}
    errors = []
    for i, finding in enumerate(data.get("harmonized_findings", []) or []):
        for support in finding.get("provider_support", []) or []:
            provider = support.get("provider")
            if provider not in declared:
                errors.append(
                    f"harmonized_findings[{i}] references undeclared provider "
                    f"{provider!r} (declared: {sorted(declared)})"
                )

    assert not errors, f"Provider foreign-key errors in {filepath}: {errors}"


@pytest.mark.kb_data
@pytest.mark.parametrize("filepath", SYNTHESIS_FILES)
def test_synthesis_best_matching_text_verbatim(filepath):
    """Every best_matching_text must be a verbatim substring of its source_report."""
    from dismech.research_synthesis import iter_quote_problems

    problems = list(iter_quote_problems(filepath))
    assert not problems, f"Quote-verification problems in {filepath}: {problems}"


def test_synthesis_derive_consensus():
    """derive_consensus computes the consensus label from provider stances."""
    from dismech.research_synthesis import derive_consensus

    def finding(*stances):
        return {"provider_support": [{"stance": s} for s in stances]}

    assert derive_consensus(finding("CONCORDANT", "CONTRADICTORY")) == "CONFLICT"
    assert derive_consensus(finding("CONCORDANT", "SILENT")) == "SINGLE"
    assert derive_consensus(finding("CONCORDANT", "CONCORDANT")) == "UNANIMOUS"
    assert derive_consensus(finding("CONCORDANT", "PARTIAL")) == "MAJORITY"
    assert derive_consensus(finding("SILENT", "SILENT")) == "SINGLE"


@pytest.fixture(scope="module")
def hypothesis_assessment_validator():
    """Validator bound to the standalone hypothesis-assessment schema."""
    return Validator(HYPOTHESIS_ASSESSMENT_SCHEMA_PATH)


@pytest.mark.kb_data
@pytest.mark.parametrize("filepath", HYPOTHESIS_ASSESSMENT_FILES)
def test_valid_hypothesis_assessment_files(filepath, hypothesis_assessment_validator):
    """All assessment sidecars validate against the HypothesisAssessment class."""
    with open(filepath) as f:
        data = safe_load(f)

    report = hypothesis_assessment_validator.validate(
        data, target_class="HypothesisAssessment"
    )
    errors = [r for r in report.results if r.severity.name == "ERROR"]

    assert not errors, f"Validation errors in {filepath}: {[str(e) for e in errors]}"


@pytest.mark.kb_data
@pytest.mark.parametrize("filepath", HYPOTHESIS_ASSESSMENT_FILES)
def test_hypothesis_assessment_links_and_quotes(filepath):
    """Assessment sidecars have valid layout, artifacts, and verbatim report quotes."""
    from dismech.hypothesis_assessment import iter_assessment_problems

    problems = list(iter_assessment_problems(filepath))
    assert not problems, f"Assessment validation problems in {filepath}: {problems}"


@pytest.mark.kb_data
@pytest.mark.parametrize("filepath", GROUPING_FILES)
def test_grouping_member_foreign_keys(filepath):
    """Each grouping member must resolve to a real Disease, module, or grouping."""
    with open(filepath) as f:
        data = safe_load(f)

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
        elif mtype == "GROUPING" and ref not in grouping_names:
            errors.append(f"members[{i}].member={ref!r} (type GROUPING)")

    assert not errors, (
        f"Grouping member FK mismatches in {Path(filepath).name}. Bad refs: {errors}"
    )


@pytest.mark.kb_data
@pytest.mark.parametrize("filepath", GROUPING_FILES)
def test_grouping_module_references(filepath):
    """Every `module` reference in a grouping must resolve to a module file."""
    with open(filepath) as f:
        data = safe_load(f)

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


@pytest.mark.kb_data
@pytest.mark.parametrize("filepath", CONFORMS_TO_FILES)
def test_conforms_to_module_node_references(filepath):
    """Every `conforms_to` must resolve to a real module AND a real node in it.

    `test_grouping_module_references` checks the `module:` slots inside grouping
    membership criteria; nothing checked the `conforms_to` edges on entry
    pathophysiology nodes, which are what grouping CONFORMS_TO_MODULE criteria
    are actually evaluated against. A stale stem or a drifted node name makes an
    entry silently stop satisfying a criterion it is asserted to satisfy — the
    same class of contradiction the grouping audit reports, but caused by a
    dangling reference rather than a curation gap.
    """
    with open(filepath) as f:
        data = safe_load(f)
    if not isinstance(data, dict):
        return

    module_nodes = _module_node_names()
    errors = []

    for path, ref in _iter_conforms_to(data):
        stem, _, node = ref.partition("#")
        stem, node = stem.strip(), node.strip()
        if stem not in module_nodes:
            errors.append(f"{path}={ref!r}: no kb/modules/{stem}.yaml")
        elif node and node not in module_nodes[stem]:
            errors.append(
                f"{path}={ref!r}: module {stem!r} has no pathophysiology node "
                f"named {node!r}"
            )

    assert not errors, (
        f"Unresolved conforms_to references in {Path(filepath).name}: {errors}"
    )


def test_grouping_unique_names():
    """Grouping `name` values must be unique across kb/groupings/."""
    seen = {}
    for fp in GROUPING_FILES:
        with open(fp) as f:
            data = safe_load(f)
        name = data.get("name") if isinstance(data, dict) else None
        if name:
            seen.setdefault(name, []).append(Path(fp).name)
    dupes = {k: v for k, v in seen.items() if len(v) > 1}
    assert not dupes, f"Duplicate grouping names: {dupes}"


@pytest.mark.kb_data
@pytest.mark.parametrize("filepath", GROUPING_FILES)
def test_grouping_criteria_well_formed(filepath):
    """Structured membership-criteria expressions must be well-formed.

    Each LogicalCriterion node must be either a BRANCH (operator + operands) or
    a LEAF (criterion_predicate + matching payload), never both or neither.
    """
    from dismech.groupings import lint_criterion

    with open(filepath) as f:
        data = safe_load(f)

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


def test_grouping_overlap_expands_nested_grouping_members():
    """Overlap computation expands nested GROUPING members to disease entries."""
    from dismech.groupings import (
        DiseaseFacts,
        compute_grouping_overlaps,
        find_candidate_members,
        grouping_disease_members,
    )

    groupings = {
        "Child": {
            "name": "Child",
            "members": [
                {"member": "B", "member_type": "DISEASE"},
                {"member": "C", "member_type": "DISEASE"},
            ],
        },
        "Crosscut": {
            "name": "Crosscut",
            "members": [
                {"member": "C", "member_type": "DISEASE"},
                {"member": "D", "member_type": "DISEASE"},
            ],
        },
        "Far": {
            "name": "Far",
            "members": [{"member": "E", "member_type": "DISEASE"}],
        },
        "Parent": {
            "name": "Parent",
            "membership_criteria": [
                {
                    "criteria_semantics": "SUFFICIENT",
                    "logic": {
                        "criterion_predicate": "HAS_GENE",
                        "gene": {"term": {"id": "hgnc:1"}},
                    },
                }
            ],
            "members": [
                {"member": "A", "member_type": "DISEASE"},
                {"member": "Child", "member_type": "GROUPING"},
                {"member": "mechanism_module", "member_type": "MODULE"},
            ],
        },
    }

    assert grouping_disease_members("Parent", groupings) == {"A", "B", "C"}

    overlaps = compute_grouping_overlaps(
        groupings,
        selected_names=["Child", "Crosscut", "Far", "Parent"],
        include_zero=True,
    )
    by_pair = {(o.grouping_a, o.grouping_b): o for o in overlaps}

    assert by_pair[("Child", "Parent")].shared_members == ("B", "C")
    assert by_pair[("Child", "Parent")].relation == "A_SUBSET_B"
    assert by_pair[("Child", "Crosscut")].shared_members == ("C",)
    assert by_pair[("Child", "Crosscut")].relation == "PARTIAL_OVERLAP"
    assert by_pair[("Far", "Parent")].overlap_count == 0
    assert by_pair[("Far", "Parent")].relation == "DISJOINT"

    nonzero = compute_grouping_overlaps(
        groupings,
        selected_names=["Child", "Crosscut", "Far", "Parent"],
    )
    assert all(o.overlap_count for o in nonzero)

    index = {
        name: DiseaseFacts(name=name, gene_ids={"hgnc:1"})
        for name in ("A", "B", "C", "D")
    }
    assert find_candidate_members(groupings["Parent"], index, groupings) == ["D"]


@pytest.mark.kb_data
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
        grouping = safe_load(f)

    index = load_disease_index()
    for ev in evaluate_grouping(grouping, index):
        assert isinstance(ev.result, Satisfaction)


@pytest.mark.kb_data
@pytest.mark.parametrize("filepath", DISORDER_FILES)
def test_dataset_accession_prefix_and_shape(filepath):
    """Dataset accessions must use a known prefix whose shape they match.

    This is the offline half of the dataset-accession guard: it catches a
    typo'd or mis-prefixed accession (e.g. ``sra:PRJNA290729``, which is really
    a BioProject ID) without touching the network. The online half --
    confirming the record actually exists -- is
    ``scripts/verify_dataset_accessions.py`` / ``just verify-datasets``.
    """
    from verify_dataset_accessions import SHAPE, UNSUPPORTED_PREFIXES, split_accession

    with open(filepath) as f:
        data = yaml.safe_load(f)

    # Dataset records also hang off proposed experiments, which the verifier
    # walks; keep the offline guard's scope identical so nothing is checked by
    # one and not the other.
    records = list(data.get("datasets") or [])
    for disc in data.get("discussions") or []:
        for exp in (disc or {}).get("proposed_experiments") or []:
            records.extend((exp or {}).get("datasets") or [])

    errors = []
    for ds in records:
        if not isinstance(ds, dict):
            continue
        accession = ds.get("accession")
        if not accession:
            errors.append("dataset record with no accession")
            continue
        prefix, local_id = split_accession(str(accession))
        if not prefix:
            errors.append(f"{accession}: no repository prefix and shape not recognized")
            continue
        if prefix in UNSUPPORTED_PREFIXES:
            # PMID/DOI/cellxgene-style entries are tolerated for now; they are
            # reported as UNSUPPORTED by the verifier rather than failed.
            continue
        shape = SHAPE.get(prefix)
        if shape is None:
            errors.append(f"{accession}: unknown repository prefix '{prefix}'")
        elif not shape.match(local_id):
            actual = [p for p, pat in SHAPE.items() if pat.match(local_id)]
            hint = f" (looks like a '{actual[0]}' accession)" if actual else ""
            errors.append(f"{accession}: '{local_id}' does not match the {prefix} pattern{hint}")

    assert not errors, f"{Path(filepath).name} has malformed dataset accessions:\n" + "\n".join(
        f"  - {e}" for e in errors
    )
