"""Schema validation tests for PhenoCAM V2."""

import glob
import subprocess
from pathlib import Path

import pytest
import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin

ROOT_DIR = Path(__file__).parent.parent
SCHEMA_PATH = ROOT_DIR / "src" / "dismech" / "schema" / "phenocam" / "phenocam.yaml"
MODULES_DIR = ROOT_DIR / "causal_models" / "modules"
DISEASES_DIR = ROOT_DIR / "causal_models" / "diseases"


@pytest.fixture(scope="module")
def validator():
    return Validator(
        SCHEMA_PATH,
        validation_plugins=[JsonschemaValidationPlugin(closed=True)],
    )


def test_schema_exists():
    assert SCHEMA_PATH.exists(), f"Schema not found at {SCHEMA_PATH}"


def test_schema_loadable(validator):
    """Schema loads and contains the Module class."""
    schema_view = validator._schema
    assert "Module" in schema_view.classes, "Expected Module class in schema"


def test_module_validator_accepts_minimal_module(validator):
    data = {"id": "test_module", "name": "Test Module"}
    report = validator.validate(data, target_class="Module")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, f"Unexpected errors: {[str(e) for e in errors]}"



def test_molecular_entity_valid(validator):
    """MolecularEntity node validates with entity slot."""
    data = {
        "id": "test_module",
        "name": "Test",
        "molecular_entities": [
            {
                "id": "tnf_alpha",
                "entity": {"id": "CHEBI:75189", "label": "tumor necrosis factor"},
                "description": "TNF-alpha cytokine secreted by activated macrophages",
            }
        ],
    }
    report = validator.validate(data, target_class="Module")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, f"Errors: {[str(e) for e in errors]}"


def test_molecular_activity_valid(validator):
    """MolecularActivity node validates with gene and molecular_function."""
    data = {
        "id": "test_module",
        "name": "Test",
        "molecular_activities": [
            {
                "id": "smo_activity",
                "gene": {"symbol": "SMO", "hgnc_id": "hgnc:11119"},
                "molecular_function": {"id": "GO:0004930", "label": "G protein-coupled receptor activity"},
            }
        ],
    }
    report = validator.validate(data, target_class="Module")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, f"Errors: {[str(e) for e in errors]}"


def test_cellular_process_valid(validator):
    """CellularProcess validates with cell_type and biological_process."""
    data = {
        "id": "test_module",
        "name": "Test",
        "cellular_processes": [
            {
                "id": "macrophage_activation",
                "cell_type": {"id": "CL:0000235", "label": "macrophage"},
                "biological_process": {"id": "GO:0042116", "label": "macrophage activation"},
            }
        ],
    }
    report = validator.validate(data, target_class="Module")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, f"Errors: {[str(e) for e in errors]}"


def test_tissue_process_valid(validator):
    """TissueProcess validates with anatomy and biological_process."""
    data = {
        "id": "test_module",
        "name": "Test",
        "tissue_processes": [
            {
                "id": "epithelial_proliferation",
                "anatomy": {"id": "UBERON:0000483", "label": "epithelium"},
                "biological_process": {"id": "GO:0008283", "label": "cell population proliferation"},
            }
        ],
    }
    report = validator.validate(data, target_class="Module")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, f"Errors: {[str(e) for e in errors]}"


def test_invalid_perturbation_quality_rejected_with_slot(validator):
    """Schema rejects invalid quality value when quality slot is wired to PerturbationQualityEnum."""
    data = {
        "id": "test_module",
        "name": "Test",
        "molecular_activities": [
            {
                "id": "act1",
                "gene": {"symbol": "SMO", "hgnc_id": "hgnc:11119"},
                "quality": "NOT_A_VALID_QUALITY",
            }
        ],
    }
    report = validator.validate(data, target_class="Module")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert errors, "Expected validation error for invalid quality value"


def test_phenotype_node_valid(validator):
    """Phenotype node validates with hpo_term."""
    data = {
        "id": "test_module",
        "name": "Test",
        "phenotypes": [
            {
                "id": "bcc",
                "hpo_term": {"id": "HP:0002671", "label": "Basal cell carcinoma"},
            }
        ],
    }
    report = validator.validate(data, target_class="Module")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, f"Errors: {[str(e) for e in errors]}"


def test_modulator_valid(validator):
    """Modulator node validates with agent and role."""
    data = {
        "id": "test_module",
        "name": "Test",
        "modulators": [
            {
                "id": "vismodegib",
                "agent": {"id": "CHEBI:66903", "label": "vismodegib"},
                "role": "therapeutic",
                "description": "SMO inhibitor approved for BCC.",
            }
        ],
    }
    report = validator.validate(data, target_class="Module")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, f"Errors: {[str(e) for e in errors]}"


def test_disease_course_valid(validator):
    """Minimal DiseaseCourse validates correctly."""
    data = {
        "id": "gorlin_syndrome",
        "name": "Gorlin Syndrome",
        "realises_disease": {"id": "MONDO:0007187", "label": "nevoid basal cell carcinoma syndrome"},
    }
    report = validator.validate(data, target_class="DiseaseCourse")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, f"Errors: {[str(e) for e in errors]}"


def test_causal_relation_valid(validator):
    """CausalRelation edge with required fields validates."""
    data = {
        "id": "test_module",
        "name": "Test",
        "molecular_activities": [
            {"id": "ptch1", "gene": {"symbol": "PTCH1", "hgnc_id": "hgnc:9585"}},
            {"id": "smo", "gene": {"symbol": "SMO", "hgnc_id": "hgnc:11119"}},
        ],
        "causal_relations": [
            {
                "subject": "ptch1",
                "predicate": {"id": "RO:0002630", "label": "directly negatively regulates"},
                "object": "smo",
                "eco": {"id": "ECO:0000304", "label": "traceable author statement used in manual assertion"},
            }
        ],
    }
    report = validator.validate(data, target_class="Module")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, f"Errors: {[str(e) for e in errors]}"


def test_hedgehog_module_file_valid(validator):
    """The hedgehog_signaling example module validates against the schema."""
    module_file = MODULES_DIR / "hedgehog_signaling.yaml"
    assert module_file.exists(), f"Example module not found: {module_file}"
    with open(module_file) as f:
        data = yaml.safe_load(f)
    report = validator.validate(data, target_class="Module")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, f"Validation errors in hedgehog_signaling.yaml: {[str(e) for e in errors]}"


def test_gorlin_disease_file_valid(validator):
    """The Gorlin Syndrome example disease course validates against the schema."""
    disease_file = DISEASES_DIR / "Gorlin_Syndrome.yaml"
    assert disease_file.exists(), f"Example disease not found: {disease_file}"
    with open(disease_file) as f:
        data = yaml.safe_load(f)
    report = validator.validate(data, target_class="DiseaseCourse")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, f"Validation errors in Gorlin_Syndrome.yaml: {[str(e) for e in errors]}"


def test_custom_validator_passes_hedgehog():
    """Custom validator passes on the hedgehog example module."""
    result = subprocess.run(
        [
            "uv", "run", "python", "scripts/phenocam_validate.py",
            str(MODULES_DIR / "hedgehog_signaling.yaml"),
            "--target-class", "Module",
        ],
        capture_output=True,
        text=True,
        cwd=ROOT_DIR,
    )
    assert result.returncode == 0, f"Validator failed:\n{result.stdout}\n{result.stderr}"


def test_custom_validator_passes_gorlin():
    """Custom validator passes on the Gorlin example disease."""
    result = subprocess.run(
        [
            "uv", "run", "python", "scripts/phenocam_validate.py",
            str(DISEASES_DIR / "Gorlin_Syndrome.yaml"),
            "--target-class", "DiseaseCourse",
        ],
        capture_output=True,
        text=True,
        cwd=ROOT_DIR,
    )
    assert result.returncode == 0, f"Validator failed:\n{result.stdout}\n{result.stderr}"


def test_custom_validator_catches_dangling_subject(tmp_path):
    """Custom validator catches a causal_relation with an unknown subject."""
    bad_disease = tmp_path / "bad_disease.yaml"
    bad_disease.write_text(
        "id: bad\nname: Bad\n"
        "realises_disease:\n  id: MONDO:0000001\n  label: test\n"
        "causal_relations:\n"
        "  - subject: nonexistent_node\n"
        "    predicate:\n      id: RO:0002411\n      label: causally upstream of\n"
        "    object: also_nonexistent\n"
    )
    result = subprocess.run(
        [
            "uv", "run", "python", "scripts/phenocam_validate.py",
            str(bad_disease), "--target-class", "DiseaseCourse",
        ],
        capture_output=True,
        text=True,
        cwd=ROOT_DIR,
    )
    assert result.returncode != 0, "Expected validator to fail on dangling subject"
    assert "nonexistent_node" in result.stdout


def test_custom_validator_catches_bad_import(tmp_path):
    """Custom validator catches an import referencing a non-existent module."""
    bad_disease = tmp_path / "bad_import.yaml"
    bad_disease.write_text(
        "id: bad\nname: Bad\n"
        "realises_disease:\n  id: MONDO:0000001\n  label: test\n"
        "imports:\n  - module: nonexistent_module\n"
    )
    result = subprocess.run(
        [
            "uv", "run", "python", "scripts/phenocam_validate.py",
            str(bad_disease), "--target-class", "DiseaseCourse",
        ],
        capture_output=True,
        text=True,
        cwd=ROOT_DIR,
    )
    assert result.returncode != 0, "Expected validator to fail on bad import"
    assert "nonexistent_module" in result.stdout


def test_custom_validator_catches_bad_hypothesis_tag(tmp_path):
    """Custom validator catches a hypothesis tag not declared in hypothesis_groups."""
    bad_module = tmp_path / "bad_tag.yaml"
    bad_module.write_text(
        "id: x\nname: Y\n"
        "hypothesis_groups:\n  - id: real_hyp\n    name: Real\n"
        "molecular_activities:\n"
        "  - id: n1\n    gene:\n      symbol: SMO\n      hgnc_id: hgnc:11119\n"
        "    hypotheses:\n      - fake_hyp\n"
    )
    result = subprocess.run(
        [
            "uv", "run", "python", "scripts/phenocam_validate.py",
            str(bad_module), "--target-class", "Module",
        ],
        capture_output=True,
        text=True,
        cwd=ROOT_DIR,
    )
    assert result.returncode != 0, "Expected validator to fail on undeclared hypothesis tag"
    assert "fake_hyp" in result.stdout
