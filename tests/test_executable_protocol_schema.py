"""Tests for the ExecutableProtocol block on a proposed Experiment.

``Experiment.executable_protocols`` records that an orderable service exists
which would take a measurement a knowledge gap asks for. The facts it carries
about a provider's catalogue -- identifier, price, turnaround, throughput --
describe a live commercial listing that changes without notice and without a
version, so the one thing worth gating is that they are never recorded without
the date they were read: an un-dated price is a claim that cannot be checked or
aged, and it is the slot a curator is most likely to fill from memory.
"""

from pathlib import Path

import pytest
import yaml
from linkml_runtime.utils.schemaview import SchemaView

ROOT_DIR = Path(__file__).parent.parent
SCHEMA_PATH = ROOT_DIR / "src" / "dismech" / "schema" / "dismech.yaml"
KB_DIRS = ("disorders", "modules", "comorbidities")

#: Slots whose values are copied off a provider's live catalogue.
CATALOGUE_SLOTS = ("protocol_id", "list_price", "unit_price_usd", "turnaround", "throughput")


@pytest.fixture(scope="module")
def schema_view() -> SchemaView:
    return SchemaView(str(SCHEMA_PATH))


def _kb_files() -> list[Path]:
    files: list[Path] = []
    for name in KB_DIRS:
        files.extend(sorted((ROOT_DIR / "kb" / name).glob("*.yaml")))
    return files


def _iter_executable_protocols(node, path=""):
    """Yield ``(path, protocol)`` for every executable_protocols entry."""
    if isinstance(node, dict):
        for key, value in node.items():
            child = f"{path}.{key}" if path else str(key)
            if key == "executable_protocols" and isinstance(value, list):
                for i, item in enumerate(value):
                    if isinstance(item, dict):
                        yield f"{child}[{i}]", item
                continue
            yield from _iter_executable_protocols(value, child)
    elif isinstance(node, list):
        for i, item in enumerate(node):
            yield from _iter_executable_protocols(item, f"{path}[{i}]")


def test_executable_protocol_is_reachable_from_experiment(schema_view):
    """The slot is wired onto Experiment and ranges over the new class."""
    assert "executable_protocols" in schema_view.get_class("Experiment").slots
    slot = schema_view.get_slot("executable_protocols")
    assert slot.range == "ExecutableProtocol"
    assert slot.multivalued


def test_provider_is_free_text_and_venue_type_is_the_enum(schema_view):
    """Provider identity is open data; the venue classification is closed.

    An enum of laboratory names would need a schema PR per new provider, which
    is the mistake this split exists to avoid. If `provider` ever acquires a
    range, that reasoning has been lost.
    """
    assert schema_view.get_slot("provider").range == "string"
    assert schema_view.get_slot("venue_type").range == "ExecutionVenueEnum"
    assert set(schema_view.get_enum("ExecutionVenueEnum").permissible_values) == {
        "COMMERCIAL_CLOUD_LAB",
        "ACADEMIC_AUTOMATION_CORE",
        "LOCAL_LABORATORY",
        "OTHER",
    }


def test_measures_is_checked_as_an_entity_reference():
    """`measures` carries the hash-anchor grammar, so the FK checker must see it.

    It has no prose sibling -- a bare name in it is a mis-written reference,
    not a misfiled outcome -- so it belongs in KNOWN_KIND_SLOTS too, where an
    unrecognised prefix is an error rather than a gap in SECTION_KEYS.
    """
    from dismech import entity_refs

    assert "measures" in entity_refs.REF_SLOTS
    assert "measures" in entity_refs.KNOWN_KIND_SLOTS


@pytest.mark.kb_data
@pytest.mark.parametrize("filepath", _kb_files(), ids=lambda p: p.name)
def test_catalogue_facts_carry_a_retrieval_date(filepath: Path):
    """Any catalogue-derived fact is recorded with the date it was read."""
    with filepath.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        return

    errors: list[str] = []
    for path, protocol in _iter_executable_protocols(data):
        name = protocol.get("name") or "<unnamed>"
        present = [s for s in CATALOGUE_SLOTS if protocol.get(s) is not None]
        if present and not protocol.get("retrieved_date"):
            errors.append(
                f"{path} ({name}) records {', '.join(present)} from a provider "
                f"catalogue but no retrieved_date"
            )
        if not protocol.get("provider"):
            errors.append(f"{path} ({name}) has no provider")

    assert not errors, f"{filepath.name}:\n" + "\n".join(f"  - {e}" for e in errors)
