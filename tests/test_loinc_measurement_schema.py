"""Tests for LOINC bindings: ``LoincTerm``, ``MeasurementDescriptor``, and the
``Diagnosis.measurements`` / ``Diagnosis.reference_ranges`` slots.

Until these landed, a LOINC code in ``kb/`` was unchecked twice over: no
adapter served the prefix, and ``loinc_term`` was a bare ``Term`` with no
``bindings:``, so the term validator never inspected it even when a cache row
existed. The binding is declared on the ``loinc_term`` slot itself rather than
by retyping it, so the existing ``{id, label}`` shape is unchanged and nothing
in flight is invalidated. The validator reads bindings off *induced* slots, so
the thing worth gating is that every class carrying a LOINC code still induces
one.
"""

from pathlib import Path

import csv

import pytest
from linkml_runtime.utils.schemaview import SchemaView

from dismech.kb_cache import load_document

ROOT_DIR = Path(__file__).parent.parent
SCHEMA_PATH = ROOT_DIR / "src" / "dismech" / "schema" / "dismech.yaml"
LOINC_CACHE = ROOT_DIR / "cache" / "loinc" / "terms.csv"
KB_DIRS = ("disorders", "modules", "comorbidities")

#: Every (class, slot) through which a LOINC CURIE enters the KB.
LOINC_BOUND_SLOTS = (
    ("ReferenceRange", "loinc_term"),
    ("Biochemical", "loinc_term"),
    ("MeasurementDescriptor", "term"),
)


@pytest.fixture(scope="module")
def schema_view() -> SchemaView:
    return SchemaView(str(SCHEMA_PATH))


def _kb_files_mentioning_loinc() -> list[Path]:
    """KB files that contain a LOINC CURIE at all.

    A substring scan is a few hundred milliseconds over the corpus; parsing
    every file is minutes. The parse itself goes through ``kb_cache`` so a
    file this test does open is shared with every other walk in the process.
    """
    files: list[Path] = []
    for name in KB_DIRS:
        for path in sorted((ROOT_DIR / "kb" / name).glob("*.yaml")):
            if "LOINC:" in path.read_text(encoding="utf-8"):
                files.append(path)
    return files


def _iter_loinc_terms(node, path=""):
    """Yield ``(path, term_dict)`` for every ``loinc_term`` block in a document."""
    if isinstance(node, dict):
        for key, value in node.items():
            child = f"{path}.{key}" if path else str(key)
            if key == "loinc_term" and isinstance(value, dict):
                yield child, value
                continue
            yield from _iter_loinc_terms(value, child)
    elif isinstance(node, list):
        for i, item in enumerate(node):
            yield from _iter_loinc_terms(item, f"{path}[{i}]")


def test_loinc_term_enum_is_label_only(schema_view):
    """``LoincTerm`` validates existence and label, with no hierarchy constraint.

    The ``monarch:`` adapter that serves LOINC answers ``label()`` and nothing
    else, so a ``reachable_from`` here would make every binding fail rather than
    make it stricter. Same contract as ``GeneTerm`` for HGNC.
    """
    enum = schema_view.get_enum("LoincTerm")
    assert enum is not None
    assert not enum.reachable_from
    assert not enum.permissible_values


@pytest.mark.parametrize("class_name,slot_name", LOINC_BOUND_SLOTS)
def test_every_loinc_entry_point_induces_a_binding(schema_view, class_name, slot_name):
    """The validator walks ``class_induced_slots``; each entry point must bind.

    ``loinc_term`` carries its binding on the slot definition, so a class that
    merely lists the slot inherits it -- that is what keeps the 68 existing
    ``{id, label}`` blocks valid without a shape change. ``MeasurementDescriptor``
    binds through ``slot_usage`` like every other descriptor.
    """
    induced = {s.name: s for s in schema_view.class_induced_slots(class_name)}
    assert slot_name in induced, f"{class_name} does not carry {slot_name}"
    ranges = [b.range for b in (induced[slot_name].bindings or [])]
    assert "LoincTerm" in ranges


def test_loinc_term_shape_is_unchanged(schema_view):
    """``loinc_term`` is still a plain ``Term`` -- the binding did not retype it."""
    slot = schema_view.get_slot("loinc_term")
    assert slot.range == "Term"
    assert not slot.multivalued


def test_measurement_descriptor_is_a_descriptor(schema_view):
    cls = schema_view.get_class("MeasurementDescriptor")
    assert cls.is_a == "Descriptor"
    assert "preferred_term" in {s.name for s in schema_view.class_induced_slots("MeasurementDescriptor")}


def test_diagnosis_carries_measurements_and_reference_ranges(schema_view):
    """The two new ``Diagnosis`` slots, and the legacy ``markers`` kept beside them."""
    slots = set(schema_view.get_class("Diagnosis").slots)
    assert {"measurements", "reference_ranges", "markers"} <= slots
    measurements = schema_view.get_slot("measurements")
    assert measurements.range == "MeasurementDescriptor"
    assert measurements.multivalued
    assert measurements.inlined_as_list
    # The string slot is superseded, not removed: narrowing it would invalidate
    # the 129 entries that carry it and every PR in flight.
    assert schema_view.get_slot("markers").range == "string"


def test_biochemical_can_carry_a_loinc_code_without_an_interval(schema_view):
    """``Biochemical.loinc_term`` is a sibling of ``reference_ranges``, not inside it."""
    assert "loinc_term" in schema_view.get_class("Biochemical").slots


def test_committed_loinc_labels_match_the_cache():
    """Every LOINC code in ``kb/`` is cached and its label is the cached one.

    The cache is populated through the term validator against the Monarch KG
    and is the offline authority for prefixes already seeded; this is the check
    ``just validate-terms`` performs, run over the whole KB so a label written
    from memory cannot land in a file CI did not select. A code with no cache
    row is reported as such rather than skipped silently: it means the cache
    was not refreshed after the code was added.
    """
    assert LOINC_CACHE.exists(), "cache/loinc/terms.csv is missing"
    cached: dict[str, str] = {}
    with LOINC_CACHE.open(encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            cached[row["curie"]] = row["label"]

    problems: list[str] = []
    seen = 0
    for path in _kb_files_mentioning_loinc():
        doc = load_document(path)
        for where, term in _iter_loinc_terms(doc):
            curie = term.get("id")
            if not isinstance(curie, str) or not curie.startswith("LOINC:"):
                continue
            seen += 1
            if curie not in cached:
                problems.append(f"{path.name}:{where}: {curie} has no cache row")
            elif term.get("label") != cached[curie]:
                problems.append(
                    f"{path.name}:{where}: {curie} label {term.get('label')!r} "
                    f"!= cached {cached[curie]!r}"
                )
    assert seen > 0, "no LOINC codes found in kb/ -- the walker is broken"
    assert not problems, "\n".join(problems)
