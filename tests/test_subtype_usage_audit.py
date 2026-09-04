"""Tests for the ``has_subtypes`` usage / subtype-gene wiring audit."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
SCRIPT_PATH = ROOT / "scripts" / "subtype_usage_audit.py"
SPEC = importlib.util.spec_from_file_location("subtype_usage_audit", SCRIPT_PATH)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


def _write(tmp_path: Path, slug: str, body: str) -> Path:
    path = tmp_path / f"{slug}.yaml"
    path.write_text(body, encoding="utf-8")
    return path


WIRED_DIRECT_ENTRY = """name: Wired Disease
has_subtypes:
- name: Type 1
  genes:
  - preferred_term: ABCA4
    term:
      id: hgnc:34
      label: ABCA4
pathophysiology:
- name: Transporter Failure
  genes:
  - preferred_term: ABCA4
    term:
      id: hgnc:34
      label: ABCA4
  downstream:
  - target: Vision Loss
phenotypes:
- name: Vision Loss
  subtype: Type 1
"""

GENETIC_UNWIRED_ENTRY = """name: Floating Disease
has_subtypes:
- name: Type A
  genes:
  - preferred_term: GENE1
    term:
      id: hgnc:11111
      label: GENE1
genetic:
- name: GENE1
  gene_term:
    preferred_term: GENE1
    term:
      id: hgnc:11111
      label: GENE1
pathophysiology:
- name: GENE1 Loss of Function
  downstream:
  - target: Some Phenotype
phenotypes:
- name: Some Phenotype
"""

NONCAUSAL_ENTRY = """name: Modifier Disease
has_subtypes:
- name: Type M
  genes:
  - preferred_term: MODG
    term:
      id: hgnc:22222
      label: MODG
genetic:
- name: MODG
  relationship_type: MODIFIER
  gene_term:
    preferred_term: MODG
    term:
      id: hgnc:22222
      label: MODG
pathophysiology:
- name: Core Mechanism
"""

ABSENT_ENTRY = """name: Absent Disease
has_subtypes:
- name: Type X
  genes:
  - preferred_term: MISSING1
    term:
      id: hgnc:33333
      label: MISSING1
pathophysiology:
- name: Core Mechanism
phenotypes:
- name: Some Phenotype
"""


def test_wired_direct(tmp_path):
    path = _write(tmp_path, "Wired_Disease", WIRED_DIRECT_ENTRY)
    census, rows = audit.audit_entry(path)
    assert census is not None
    assert census.n_subtypes == 1
    assert census.n_referenced == 1
    assert [row.status for row in rows] == ["WIRED_DIRECT"]


def test_genetic_unwired_with_name_mention(tmp_path):
    path = _write(tmp_path, "Floating_Disease", GENETIC_UNWIRED_ENTRY)
    census, rows = audit.audit_entry(path)
    assert census is not None
    # The subtype is never the target of a subtype: foreign key.
    assert census.n_referenced == 0
    (row,) = rows
    assert row.status == "GENETIC_UNWIRED"
    # GENE1 appears in a pathophysiology node *name* but not as a descriptor,
    # so the advisory flag fires while the graph-contract verdict stays unwired.
    assert row.name_mention is True
    assert row.genetic_nodes == ["GENE1"]


def test_noncausal_genetic_item(tmp_path):
    path = _write(tmp_path, "Modifier_Disease", NONCAUSAL_ENTRY)
    _, rows = audit.audit_entry(path)
    (row,) = rows
    assert row.status == "GENETIC_NONCAUSAL"


def test_absent_gene(tmp_path):
    path = _write(tmp_path, "Absent_Disease", ABSENT_ENTRY)
    _, rows = audit.audit_entry(path)
    (row,) = rows
    assert row.status == "ABSENT"
    assert row.name_mention is False


def test_entry_without_subtypes_is_skipped(tmp_path):
    path = _write(tmp_path, "Plain_Disease", "name: Plain Disease\n")
    census, rows = audit.audit_entry(path)
    assert census is None
    assert rows == []


def test_nested_children_are_counted(tmp_path):
    body = """name: Nested Disease
has_subtypes:
- name: Parent Type
  children:
  - name: Child Type
    genes:
    - preferred_term: MISSING2
      term:
        id: hgnc:44444
        label: MISSING2
"""
    path = _write(tmp_path, "Nested_Disease", body)
    census, rows = audit.audit_entry(path)
    assert census is not None
    assert census.n_subtypes == 2
    (row,) = rows
    assert row.subtype == "Child Type"
    assert row.status == "ABSENT"
