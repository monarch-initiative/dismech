"""The backfill writes structure from prose, so its refusals are the interesting part.

``scripts/backfill_cancer_origin.py`` marks a pathophysiology node as the somatic
origin lesion when the node's own name already says so. Everything that makes it
safe is a *negative*: what it declines to mark, and what it must not silently
drop while writing. Those are what these tests pin.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from backfill_cancer_origin import (
    Proposal,
    apply_proposal,
    propose,
)

ROOT = Path(__file__).parent.parent

ENTRY_HEAD = "name: Fake Carcinoma\ncategories:\n- Solid Tumor\npathophysiology:\n"
CELL = (
    "  cell_types:\n  - preferred_term: epithelial cell\n"
    "    term:\n      id: CL:0000066\n      label: epithelial cell\n"
)


def _write(tmp_path, body):
    path = tmp_path / "Fake_Carcinoma.yaml"
    path.write_text(ENTRY_HEAD + body)
    return path


def test_a_viral_oncoprotein_node_is_never_proposed(tmp_path):
    """No host variant exists, so variant_origin has nothing to describe."""
    path = _write(
        tmp_path,
        "- name: E7 Oncoprotein-Mediated pRB Inactivation\n"
        "  description: HPV E7 binds and inactivates pRB.\n" + CELL,
    )
    proposals, status = propose(path)
    assert proposals == []
    assert status == "no-candidate"


def test_an_acquired_resistance_node_is_never_proposed(tmp_path):
    """A real somatic event, but one that happens years after the disease starts."""
    path = _write(
        tmp_path,
        "- name: ESR1 Mutation-Driven Endocrine Resistance\n" + CELL,
    )
    proposals, status = propose(path)
    assert proposals == []
    assert status == "no-candidate"


def test_a_germline_node_is_never_proposed(tmp_path):
    path = _write(
        tmp_path,
        "- name: TP53 Mutation\n"
        "  description: Germline TP53 variant inherited in this syndrome.\n" + CELL,
    )
    proposals, _ = propose(path)
    assert proposals == []


def test_a_pathway_state_is_not_a_lesion(tmp_path):
    path = _write(tmp_path, "- name: MAPK/ERK Pathway Activation\n" + CELL)
    proposals, _ = propose(path)
    assert proposals == []


def test_bare_hypermethylation_is_not_a_lesion(tmp_path):
    """Epithelioid sarcoma: H3K27 hypermethylation sits under SMARCB1 loss."""
    path = _write(
        tmp_path, "- name: EZH2/PRC2 Dependency and H3K27 Hypermethylation\n" + CELL
    )
    proposals, _ = propose(path)
    assert proposals == []


def test_gene_loss_with_a_parenthetical_alias_is_a_lesion(tmp_path):
    """"SMARCB1 (INI1) Loss" is the real lesion node and must be reachable."""
    path = _write(tmp_path, "- name: SMARCB1 (INI1) Loss\n" + CELL)
    proposals, status = propose(path)
    assert status == "ready"
    assert [p.node_name for p in proposals] == ["SMARCB1 (INI1) Loss"]


def test_a_named_lesion_is_proposed(tmp_path):
    path = _write(tmp_path, "- name: KRAS Oncogene Hotspot Mutation\n" + CELL)
    proposals, status = propose(path)
    assert status == "ready"
    assert proposals[0].cell_ids == ["CL:0000066"]


def test_a_borrowed_cell_is_written_when_the_node_already_has_genetic_context(tmp_path):
    """The silent partial-apply: the node was marked but never bound.

    A node carrying a genetic_context gets `variant_origin` merged into it
    rather than a second block, and an early return there skipped the
    borrowed-cell write while the run still reported success.
    """
    path = tmp_path / "Fake_Carcinoma.yaml"
    path.write_text(
        ENTRY_HEAD
        + "- name: BRAF Somatic Driver Mutation\n"
        "  genetic_context:\n"
        "    functional_impact_category: GAIN_OF_FUNCTION\n"
    )
    proposal = Proposal(
        path=path,
        node_name="BRAF Somatic Driver Mutation",
        cell_ids=["CL:0000148"],
        cell_labels=["melanocyte"],
        is_root=True,
        matched="mutation",
        has_genetic_context=True,
        borrowed_cell=True,
    )
    assert apply_proposal(path, [proposal])
    written = path.read_text()
    assert "variant_origin: SOMATIC" in written
    assert "id: CL:0000148" in written
    # exactly one genetic_context block: a second would be a duplicate YAML key
    assert written.count("genetic_context:") == 1
