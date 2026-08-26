"""Tests for the gene -> process jump scan (``just gene-activity-gaps``)."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT_PATH = ROOT / "scripts" / "gene_activity_gap_scan.py"
SPEC = importlib.util.spec_from_file_location("gene_activity_gap_scan", SCRIPT_PATH)
assert SPEC and SPEC.loader
scan = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = scan
SPEC.loader.exec_module(scan)


def _write(kb_dir: Path, slug: str, body: str) -> Path:
    kb_dir.mkdir(parents=True, exist_ok=True)
    path = kb_dir / f"{slug}.yaml"
    path.write_text(body, encoding="utf-8")
    return path


GENETIC = """genetic:
- name: ACP2 pathogenic variants
  gene_term:
    preferred_term: ACP2
    term:
      id: hgnc:123
      label: ACP2
"""


def _entry(node_block: str, genetic: str = GENETIC) -> str:
    return f"name: Test Disorder\n{genetic}pathophysiology:\n{node_block}"


BP_ONLY = """- name: Lysosomal Acid Phosphatase 2 Deficiency
  description: Reduced lysosomal acid phosphatase activity.
  genes:
  - preferred_term: ACP2
    term:
      id: hgnc:123
      label: ACP2
  biological_processes:
  - preferred_term: dephosphorylation
    term:
      id: GO:0016311
      label: dephosphorylation
"""

MF_BOUND = (
    BP_ONLY
    + """  molecular_functions:
  - preferred_term: acid phosphatase activity
    term:
      id: GO:0003993
      label: acid phosphatase activity
"""
)


@pytest.fixture
def seed() -> dict[str, str]:
    return {"GO:0016311": "SUBSTANCE", "GO:0060271": "CELLULAR"}


def test_bp_only_landing_node_is_a_process_jump(tmp_path, seed):
    path = _write(tmp_path, "Test_Disorder", _entry(BP_ONLY))
    jumps, counts = scan.scan_entry(path, seed)

    assert counts["gene_to_mechanism_edges"] == 1
    assert counts["PROCESS_JUMP"] == 1
    assert [jump.node for jump in jumps] == ["Lysosomal Acid Phosphatase 2 Deficiency"]
    assert jumps[0].genes == ["ACP2"]
    assert jumps[0].bp_terms == ["GO:0016311 dephosphorylation"]
    assert jumps[0].landing_classes == ["SUBSTANCE"]


def test_molecular_function_on_the_node_is_not_a_jump(tmp_path, seed):
    path = _write(tmp_path, "Test_Disorder", _entry(MF_BOUND))
    jumps, counts = scan.scan_entry(path, seed)

    assert jumps == []
    assert counts["ACTIVITY_BOUND"] == 1
    assert counts["PROCESS_JUMP"] == 0


def test_node_with_no_grounding_is_reported_separately(tmp_path, seed):
    node = """- name: ACP2 lesion
  genes:
  - preferred_term: ACP2
    term:
      id: hgnc:123
      label: ACP2
"""
    path = _write(tmp_path, "Test_Disorder", _entry(node))
    jumps, counts = scan.scan_entry(path, seed)

    assert jumps == []
    assert counts["UNGROUNDED"] == 1


def test_activity_prose_is_detected_in_name_and_description(tmp_path, seed):
    path = _write(tmp_path, "Test_Disorder", _entry(BP_ONLY))
    jump = scan.scan_entry(path, seed)[0][0]

    # "Acid Phosphatase" in the name and "activity" in the description: the
    # molecular function is already claimed, only the term is missing.
    assert jump.activity_prose is True
    assert jump.activity_in_name is True
    assert jump.verdict == "ANNOTATE_MF"


def test_a_node_making_no_activity_claim_is_not_flagged_as_prose(tmp_path, seed):
    node = BP_ONLY.replace(
        "- name: Lysosomal Acid Phosphatase 2 Deficiency",
        "- name: Lysosomal Storage",
    ).replace(
        "  description: Reduced lysosomal acid phosphatase activity.",
        "  description: Undegraded substrate accumulates in the lysosome.",
    )
    jump = scan.scan_entry(_write(tmp_path, "Test_Disorder", _entry(node)), seed)[0][0]

    assert jump.activity_prose is False
    assert jump.activity_in_name is False


def test_multi_gene_landing_node_is_a_debundle_target_not_an_annotation_gap():
    jump = scan.Jump(
        entry="Primary_Ciliary_Dyskinesia",
        path="kb/disorders/Primary_Ciliary_Dyskinesia.yaml",
        node="Ciliary Dysfunction",
        genes=["DNAH5", "RSPH1", "FOXJ1"],
        landing_classes=["CELLULAR"],
        activity_prose=True,
    )
    # Activity prose would otherwise say ANNOTATE_MF; the gene count outranks it,
    # because no single MF term is true of a dynein, a spoke and a TF at once.
    assert scan.decide(jump) == "DEBUNDLE_FIRST"


def test_pathway_landing_asks_for_a_chain_not_a_term():
    jump = scan.Jump(
        entry="Growth_Hormone_Insensitivity_Syndrome",
        path="kb/disorders/Growth_Hormone_Insensitivity_Syndrome.yaml",
        node="GH-IGF1 Axis Disruption",
        genes=["GHR"],
        landing_classes=["PATHWAY"],
    )
    assert scan.decide(jump) == "INSERT_CHAIN"


def test_distant_landing_with_no_activity_claim_needs_a_new_node():
    jump = scan.Jump(
        entry="Test",
        path="kb/disorders/Test.yaml",
        node="Some Cellular Process",
        genes=["GENE1"],
        landing_classes=["CELLULAR"],
    )
    assert scan.decide(jump) == "INSERT_ACTIVITY_NODE"


def test_several_gene_nodes_collapse_onto_one_landing_row(tmp_path, seed):
    genetic = (
        GENETIC
        + """- name: ACP2
  gene_term:
    preferred_term: ACP2
    term:
      id: hgnc:123
      label: ACP2
"""
    )
    path = _write(tmp_path, "Test_Disorder", _entry(BP_ONLY, genetic))
    jumps, counts = scan.scan_entry(path, seed)

    assert counts["PROCESS_JUMP"] == 2
    assert len(jumps) == 1
    assert jumps[0].gene_nodes == ["ACP2 pathogenic variants", "ACP2"]


def test_seed_table_parses_and_classifies_a_known_term():
    seed = scan.load_seed(ROOT / "docs/superpowers/pathograph_node_class_go_seed.tsv")
    assert seed, "the committed GO seed table should parse"
    assert seed["GO:0060271"] == "CELLULAR"  # cilium assembly
