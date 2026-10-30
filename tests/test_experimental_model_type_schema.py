"""Tests for ExperimentalModelTypeEnum's CELL_FREE, PSC_DERIVED_MODEL and EX_VIVO_TISSUE values.

Every value the enum had before #16000 presupposed cells or tissue, so a
purified-protein or reconstitution assay could only be typed ``OTHER``.
``CELL_FREE`` covers a system with no intact cells present during the readout.
``PSC_DERIVED_MODEL`` (#12806) covers any pluripotent stem cell line, induced or
embryonic, and deprecates ``IPSC_DERIVED_MODEL``. ``EX_VIVO_TISSUE`` covers
explants, slices and organ cultures. All three are additive: ``OTHER`` and
``IPSC_DERIVED_MODEL`` stay valid.
"""

import re
from pathlib import Path

import pytest
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml_runtime.utils.schemaview import SchemaView

ROOT_DIR = Path(__file__).parent.parent
SCHEMA_PATH = ROOT_DIR / "src" / "dismech" / "schema" / "dismech.yaml"
TEMPLATE_PATH = ROOT_DIR / "src" / "dismech" / "templates" / "disorder.html.j2"


@pytest.fixture(scope="module")
def schema_view() -> SchemaView:
    return SchemaView(str(SCHEMA_PATH))


@pytest.fixture(scope="module")
def validator() -> Validator:
    return Validator(
        SCHEMA_PATH,
        validation_plugins=[JsonschemaValidationPlugin(closed=True)],
    )


def _errors(validator, model_type: str):
    data = {
        "name": "Example",
        "experimental_models": [
            {"name": "Example model", "experimental_model_type": model_type}
        ],
    }
    report = validator.validate(data, target_class="Disease")
    return [r for r in report.results if r.severity.name == "ERROR"]


def _values(schema_view):
    return schema_view.get_enum("ExperimentalModelTypeEnum").permissible_values


@pytest.mark.parametrize(
    "value",
    ["CELL_FREE", "PSC_DERIVED_MODEL", "EX_VIVO_TISSUE", "IPSC_DERIVED_MODEL", "OTHER"],
)
def test_model_type_validates(validator, value):
    errors = _errors(validator, value)
    assert not errors, [str(e) for e in errors]


def test_unknown_model_type_is_rejected(validator):
    assert _errors(validator, "IN_CHEMICO")


def test_ipsc_value_is_deprecated_in_favour_of_psc(schema_view):
    values = _values(schema_view)
    assert "PSC_DERIVED_MODEL" in values["IPSC_DERIVED_MODEL"].deprecated
    assert not values["PSC_DERIVED_MODEL"].deprecated


def test_cell_free_description_states_the_readout_test(schema_view):
    description = _values(schema_view)["CELL_FREE"].description
    assert "no intact cells present during the measurement" in description
    assert "BOUNDARY_OMISSION" in description


def test_every_typed_value_has_a_page_icon(schema_view):
    """The disorder page maps each type to an icon; a value missing there renders bare."""
    block = re.search(
        r"EXPERIMENTAL_MODEL_TYPE_ICONS = \{(.*?)\}", TEMPLATE_PATH.read_text(), re.S
    )
    assert block, "EXPERIMENTAL_MODEL_TYPE_ICONS not found in disorder.html.j2"
    iconed = set(re.findall(r"^\s*([A-Z_]+):", block.group(1), re.M))
    assert set(_values(schema_view)) - {"OTHER"} == iconed
