"""The CCDI pediatric oncology classification axis and its audit (offline)."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "ccdi_pediatric_oncology_audit.py"

spec = importlib.util.spec_from_file_location("ccdi_pediatric_oncology_audit", SCRIPT)
audit = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = audit
spec.loader.exec_module(audit)


class FakeOls:
    """Stands in for OLS with a hand-written is_a table."""

    def __init__(
        self, parents: dict[str, list[str]], xrefs: dict[str, list[str]] | None = None
    ):
        self.parents = parents
        self.xrefs = xrefs or {}

    def ancestors(self, curie: str) -> list[str]:
        found: set[str] = set()
        stack = list(self.parents.get(curie, []))
        while stack:
            node = stack.pop()
            if node not in found:
                found.add(node)
                stack.extend(self.parents.get(node, []))
        return sorted(found)

    def ncit_xrefs(self, mondo_id: str) -> list[str]:
        return self.xrefs.get(mondo_id, [])


#: A fragment of NCIt, enough to exercise each rule. ``X:`` ids are invented
#: leaves; the bound concepts are the real ones from the enum.
PARENTS = {
    "NCIT:C6906": ["NCIT:C3808", "NCIT:C2907"],  # AT/RT is a rhabdoid tumor
    "X:alveolar_rms": ["NCIT:C3359"],
    "NCIT:C3359": ["NCIT:C9306"],  # pretend RMS sits under soft tissue sarcoma
    "X:pineal": ["NCIT:C2907"],
    "X:kidney_rhabdoid": ["NCIT:C3808", "NCIT:C3150"],
    "NCIT:C3172": ["NCIT:C27134"],
    "X:aml": ["NCIT:C3172"],
    "X:histiocytosis": ["NCIT:C27134"],
    "X:paraganglioma": ["NCIT:C3809"],
    "X:carcinoma": [],
}


@pytest.fixture(scope="module")
def categories():
    return audit.load_categories()


def test_every_permissible_value_is_bound(categories):
    schema = yaml.safe_load(audit.ENUM_PATH.read_text())
    values = schema["enums"][audit.ENUM_NAME]["permissible_values"]
    assert len(values) == 31, "caDSR CDE 16607972 has 31 permissible values"
    assert {c.name for c in categories} == set(values)
    assert all(c.concepts for c in categories)
    assert sum(c.residual for c in categories) == 4


def test_enum_is_imported_and_slot_is_in_the_container():
    schema = yaml.safe_load((REPO_ROOT / "src/dismech/schema/dismech.yaml").read_text())
    assert "classifications/ccdi_pediatric_oncology" in schema["imports"]
    container = schema["classes"]["DiseaseClassifications"]["slots"]
    assert audit.SLOT in container
    assignment = schema["classes"]["CCDIPediatricOncologyAssignment"]
    usage = assignment["slot_usage"]["classification_value"]
    assert usage["range"] == audit.ENUM_NAME


@pytest.mark.parametrize(
    ("concept", "expected"),
    [
        ("NCIT:C3222", ("Medulloblastoma",)),  # the bound concept itself
        ("X:alveolar_rms", ("Rhabdomyosarcoma",)),  # narrower value beats broader
        ("NCIT:C6906", ("Atypical Teratoid/Rhabdoid Tumors",)),
        ("X:aml", ("Myeloid Leukemia",)),  # a specific value suppresses the residual
        ("X:histiocytosis", ("Other Hematopoietic Tumors",)),
        ("X:pineal", ("Other Brain Tumors",)),
        ("X:paraganglioma", ("Endocrine and Neuroendocrine Tumors",)),
        ("X:carcinoma", ()),
    ],
)
def test_most_specific_value_wins(categories, concept, expected):
    proposed, _ = audit.propose((concept,), categories, FakeOls(PARENTS))
    assert proposed == expected


def test_incomparable_values_are_both_reported(categories):
    proposed, _ = audit.propose(("X:kidney_rhabdoid",), categories, FakeOls(PARENTS))
    assert set(proposed) == {"Rhabdoid Tumors", "Renal Tumors"}


def test_audit_statuses(tmp_path, categories):
    def entry(name: str, mondo: str, value: str | None) -> Path:
        data = {
            "name": name,
            "disease_term": {"term": {"id": mondo, "label": f"{name} neoplasm"}},
        }
        if value:
            data["classifications"] = {audit.SLOT: {"classification_value": value}}
        path = tmp_path / f"{name}.yaml"
        path.write_text(yaml.safe_dump(data))
        return path

    ols = FakeOls(
        PARENTS,
        xrefs={
            "MONDO:1": ["X:aml"],
            "MONDO:2": ["X:aml"],
            "MONDO:3": ["X:aml"],
            "MONDO:4": ["X:kidney_rhabdoid"],
        },
    )
    paths = [
        entry("a", "MONDO:1", "Myeloid Leukemia"),
        entry("b", "MONDO:2", None),
        entry("c", "MONDO:3", "Neuroblastoma"),
        entry("d", "MONDO:4", None),
        entry("e", "MONDO:5", None),
    ]
    statuses = {r.path.stem: r.status for r in audit.audit(paths, categories, ols)}
    assert statuses == {
        "a": "MATCH",
        "b": "MISSING",
        "c": "CONFLICT",
        "d": "AMBIGUOUS",
        "e": "NO_NCIT",
    }


def test_apply_writes_only_missing_and_records_the_derivation(tmp_path, categories):
    with_block = tmp_path / "with_block.yaml"
    with_block.write_text(
        "name: with_block leukemia\n"
        "disease_term:\n  term:\n    id: MONDO:1\n    label: x\n"
        "classifications:\n  icdo_morphology:\n    classification_value: Leukemia\n"
    )
    without_block = tmp_path / "without_block.yaml"
    without_block.write_text(
        "name: without_block leukemia\n"
        "disease_term:\n  term:\n    id: MONDO:2\n    label: x\n"
    )
    tied = tmp_path / "tied.yaml"
    tied.write_text(
        "name: tied tumor\ndisease_term:\n  term:\n    id: MONDO:4\n    label: x\n"
    )
    ols = FakeOls(
        PARENTS,
        xrefs={
            "MONDO:1": ["X:aml"],
            "MONDO:2": ["X:histiocytosis"],
            "MONDO:4": ["X:kidney_rhabdoid"],
        },
    )
    rows = audit.audit([with_block, without_block, tied], categories, ols)
    log = audit.apply(rows, categories)
    assert len(log) == 2 and all(line.startswith("WROTE") for line in log)

    first = yaml.safe_load(with_block.read_text())["classifications"]
    assert first["icdo_morphology"]["classification_value"] == "Leukemia"
    assert first[audit.SLOT]["classification_value"] == "Myeloid Leukemia"
    assert "X:aml is a descendant of NCIT:C3172" in first[audit.SLOT]["notes"]

    second = yaml.safe_load(without_block.read_text())["classifications"][audit.SLOT]
    assert second["classification_value"] == "Other Hematopoietic Tumors"
    assert "residual" in second["notes"]

    assert "classifications" not in yaml.safe_load(tied.read_text())
    again = audit.audit([with_block, without_block, tied], categories, ols)
    assert [r.status for r in again] == ["MATCH", "MATCH", "AMBIGUOUS"]
