"""The cell of origin is derived, not stored, so the derivation needs pinning.

dismech has no ``cell_of_origin:`` slot and does not need one: a pathophysiology
node carrying ``genetic_context.variant_origin: SOMATIC`` already says *this is
where the transforming lesion happened*, and that node's ``cell_types`` already
say *in which cell*. ``scripts/check_cancer_origin.py`` reads the two together.

These tests fix the parts of that derivation that are easy to get subtly wrong:
the precedence between the three origin rules, the fallback that stops a strong
rule from discarding a weak rule's correct answer, and the separation of
microenvironment nodes from origin nodes.
"""

import subprocess
import sys
from pathlib import Path

# Inline the path rather than assigning ROOT first: ruff's E402 allows an
# import preceded by a `sys.path` preamble, but an intervening assignment
# breaks that allowance (see tests/test_causal_targets.py).
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from check_cancer_origin import (  # noqa: E402
    FINDING_CONTEXT,
    FINDING_MULTI,
    FINDING_NO_CELL,
    FINDING_NO_ORIGIN,
    RULE_ROLE,
    RULE_SOMATIC,
    RULE_TRIGGER,
    assess,
    find_origins,
    normalize_role,
)

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_cancer_origin.py"


def _cell(term_id, label):
    return {"preferred_term": label, "term": {"id": term_id, "label": label}}


def test_somatic_lesion_outranks_an_initiating_role():
    """A structured mutational claim beats a naming convention."""
    origins = find_origins(
        [
            {
                "name": "Chronic Inflammation",
                "role": "trigger",
                "cell_types": [_cell("CL:0000235", "macrophage")],
            },
            {
                "name": "KRAS Oncogene Activation",
                "genetic_context": {"variant_origin": "SOMATIC"},
                "cell_types": [_cell("CL:0002079", "pancreatic ductal cell")],
            },
        ]
    )
    assert [o.rule for o in origins] == [RULE_SOMATIC]
    assert origins[0].cell_ids == {"CL:0002079"}


def test_somatic_node_without_a_cell_falls_back_to_the_role_rule():
    """The strongest rule must not discard a weaker rule's actual answer.

    A lesion node routinely carries the gene and not the cell it occurred in.
    Letting rule 1 win outright there would report an entry that names its
    origin cell perfectly well as having none.
    """
    origins = find_origins(
        [
            {
                "name": "EWSR1-FLI1 Fusion",
                "genetic_context": {"variant_origin": "SOMATIC"},
            },
            {
                "name": "Permissive Progenitor Cell State",
                "role": "driver",
                "cell_types": [_cell("CL:0000134", "mesenchymal stem cell")],
            },
        ]
    )
    assert [o.rule for o in origins] == [RULE_ROLE]
    assert origins[0].cell_ids == {"CL:0000134"}


def test_no_rule_yielding_a_cell_still_reports_the_strongest_match():
    """Falling back must not degrade into reporting the entry as unmarked."""
    origins = find_origins(
        [
            {
                "name": "Somatic BRAF Codon-600 Driver",
                "genetic_context": {"variant_origin": "SOMATIC"},
            },
            {"name": "Downstream MAPK Activation"},
        ]
    )
    assert [o.rule for o in origins] == [RULE_SOMATIC]
    assert origins[0].cell_terms == []


def test_initiating_role_only_counts_on_a_root_node():
    """Off a root node, "trigger" names a step in the cascade, not the origin."""
    origins = find_origins(
        [
            {
                "name": "Upstream Lesion",
                "downstream": [{"target": "Inner Trigger"}],
            },
            {
                "name": "Inner Trigger",
                "role": "trigger",
                "cell_types": [_cell("CL:0000057", "fibroblast")],
            },
        ]
    )
    assert origins == []


def test_self_loop_does_not_make_a_node_non_root():
    """A node listed as its own downstream is issue #9896, not an incoming edge."""
    origins = find_origins(
        [
            {
                "name": "Clonal Expansion",
                "role": "trigger",
                "downstream": [{"target": "Clonal Expansion"}],
                "cell_types": [_cell("CL:0000037", "hematopoietic stem cell")],
            }
        ]
    )
    assert [o.name for o in origins] == ["Clonal Expansion"]


def test_exposure_trigger_covers_non_mutational_initiation():
    """An oncovirus leaves no host lesion to mark, but still names an origin."""
    origins = find_origins(
        [
            {
                "name": "HTLV-1 Infection of CD4 T Cells",
                "triggers": [{"preferred_term": "HTLV-1 infection"}],
                "cell_types": [_cell("CL:0000624", "CD4-positive T cell")],
            }
        ]
    )
    assert [o.rule for o in origins] == [RULE_TRIGGER]


def test_role_normalization_folds_case_and_separators():
    assert normalize_role("TRIGGER") == "trigger"
    assert normalize_role("Primary_Defect") == "primary defect"
    assert normalize_role(None) == ""


def test_microenvironment_node_is_flagged_not_silently_accepted(tmp_path):
    """The known failure mode of the role rule, kept visible.

    PDAC is the worked case: a "Chronic Pancreatic Inflammation" root node
    marked `role: trigger` derived macrophage + pancreatic stellate cell as the
    cell of origin, while the real origin sat one node over.
    """
    entry = tmp_path / "Fake_Carcinoma.yaml"
    entry.write_text(
        "name: Fake Carcinoma\n"
        "categories:\n- Solid Tumor\n"
        "pathophysiology:\n"
        "- name: Tumor Microenvironment Remodeling\n"
        "  role: trigger\n"
        "  cell_types:\n"
        "  - preferred_term: macrophage\n"
        "    term:\n"
        "      id: CL:0000235\n"
        "      label: macrophage\n"
    )
    report = assess(entry)
    assert report is not None
    assert FINDING_CONTEXT in report.findings


def test_stromal_cell_of_origin_is_not_mistaken_for_a_context_node(tmp_path):
    """Giant cell tumor of bone really does arise in mesenchymal stromal cells.

    The context-node test is on the node NAME and must not fire merely because
    a legitimate origin cell has "stromal" in its own name.
    """
    entry = tmp_path / "Fake_Bone_Tumor.yaml"
    entry.write_text(
        "name: Fake Bone Tumor\n"
        "categories:\n- Solid Tumor\n"
        "pathophysiology:\n"
        "- name: Somatic H3-3A G34W Mutation in Mesenchymal Stromal Cells\n"
        "  role: trigger\n"
        "  cell_types:\n"
        "  - preferred_term: mesenchymal stem cell\n"
        "    term:\n"
        "      id: CL:0000134\n"
        "      label: mesenchymal stem cell\n"
    )
    report = assess(entry)
    assert report is not None
    assert FINDING_CONTEXT not in report.findings


def test_multiple_origin_cells_are_reported_as_the_lump_split_signal(tmp_path):
    entry = tmp_path / "Fake_Pool.yaml"
    entry.write_text(
        "name: Fake Renal Sarcoma\n"
        "categories:\n- Sarcoma\n"
        "pathophysiology:\n"
        "- name: Malignant Transformation of Renal Mesenchyme\n"
        "  role: trigger\n"
        "  cell_types:\n"
        "  - preferred_term: mesenchymal stem cell\n"
        "    term:\n"
        "      id: CL:0000134\n"
        "      label: mesenchymal stem cell\n"
        "  - preferred_term: smooth muscle cell\n"
        "    term:\n"
        "      id: CL:0000192\n"
        "      label: smooth muscle cell\n"
    )
    report = assess(entry)
    assert report is not None
    assert FINDING_MULTI in report.findings
    assert len(report.origin_cells) == 2


def test_germline_predisposition_syndrome_is_skipped_not_failed(tmp_path):
    """Sec 3a keeps germline syndromes under the plain Mendelian rules."""
    entry = tmp_path / "Fake_Syndrome.yaml"
    entry.write_text(
        "name: Fake Cancer Predisposition Syndrome\n"
        "categories:\n- Hereditary Cancer Syndrome\n"
        "pathophysiology:\n- name: Germline Variant\n"
    )
    report = assess(entry)
    assert report is not None
    assert report.is_neoplasm
    assert report.is_predisposition
    assert report.findings == []


def test_non_neoplasm_entry_is_not_assessed(tmp_path):
    entry = tmp_path / "Fake_Asthma.yaml"
    entry.write_text(
        "name: Fake Asthma\ncategories:\n- Respiratory Disease\n"
        "pathophysiology:\n- name: Airway Inflammation\n"
    )
    report = assess(entry)
    assert report is not None
    assert not report.is_neoplasm
    assert report.findings == []


def test_unmarked_entry_reports_no_origin(tmp_path):
    entry = tmp_path / "Fake_Unmarked.yaml"
    entry.write_text(
        "name: Fake Adenocarcinoma\n"
        "categories:\n- Solid Tumor\n"
        "pathophysiology:\n"
        "- name: Some Mechanism\n"
        "  cell_types:\n"
        "  - preferred_term: epithelial cell\n"
        "    term:\n"
        "      id: CL:0000066\n"
        "      label: epithelial cell\n"
    )
    report = assess(entry)
    assert report is not None
    assert report.findings == [FINDING_NO_ORIGIN]
    # The cells are bound, they are just not attributed to an origin.
    assert report.all_cell_ids == {"CL:0000066"}


def test_marked_origin_without_a_cell_is_its_own_finding(tmp_path):
    entry = tmp_path / "Fake_Marked.yaml"
    entry.write_text(
        "name: Fake Leukemia\n"
        "categories:\n- Hematologic Malignancy\n"
        "pathophysiology:\n"
        "- name: Somatic Driver Mutation\n"
        "  genetic_context:\n"
        "    variant_origin: SOMATIC\n"
    )
    report = assess(entry)
    assert report is not None
    assert report.findings == [FINDING_NO_CELL]


def test_worked_exemplars_still_derive_their_documented_cell():
    """CML and PDAC are the committed worked examples; keep them working."""
    cml = assess(ROOT / "kb" / "disorders" / "Chronic_Myeloid_Leukemia.yaml")
    assert cml is not None
    assert cml.rules == [RULE_SOMATIC]
    assert [cid for cid, _ in cml.origin_cells] == ["CL:0000037"]

    pdac = assess(ROOT / "kb" / "disorders" / "Pancreatic_Ductal_Adenocarcinoma.yaml")
    assert pdac is not None
    assert pdac.rules == [RULE_SOMATIC]
    assert [cid for cid, _ in pdac.origin_cells] == ["CL:0002079"]
    # The stromal cells of the chronic-inflammation node must not come back.
    assert FINDING_CONTEXT not in pdac.findings


def test_script_is_advisory_by_default_and_gates_only_when_asked():
    """Most of the corpus is unmarked, so a default non-zero exit would be noise."""
    advisory = subprocess.run(
        [sys.executable, str(SCRIPT)], capture_output=True, text=True, cwd=ROOT
    )
    assert advisory.returncode == 0, advisory.stderr

    gated = subprocess.run(
        [sys.executable, str(SCRIPT), "--fail-on", FINDING_NO_ORIGIN],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    assert gated.returncode == 1
