"""The cell of origin is derived, not stored, so the derivation needs pinning.

dismech has no ``cell_of_origin:`` slot and does not need one: a pathophysiology
node carrying ``genetic_context.variant_origin: SOMATIC`` already says *this is
where the transforming lesion happened*, and that node's ``cell_types`` already
say *in which cell*. ``scripts/check_cancer_origin.py`` reads the two together.

The derivation reads two structured markers and nothing else: a somatic
``genetic_context``, and an ``environmental_effect: TRIGGERS`` link for
non-mutational initiation. An earlier version also read an initiating-sounding
``role`` string and chained fallbacks between the rules; both existed to cover
entries that had not recorded their origin, and both mis-fired. The records were
marked instead and the rules deleted, so these tests pin the two that remain --
including the one case where they must not both speak.
"""

import subprocess
import sys
from pathlib import Path

# Inline the path rather than assigning ROOT first: ruff's E402 allows an
# import preceded by a `sys.path` preamble, but an intervening assignment
# breaks that allowance (see tests/test_causal_targets.py).
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from check_cancer_origin import (
    FINDING_MULTI,
    FINDING_NO_CELL,
    FINDING_NO_ORIGIN,
    RULE_SOMATIC,
    RULE_TRIGGER,
    assess,
    find_origins,
)

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_cancer_origin.py"


def _cell(term_id, label):
    return {"preferred_term": label, "term": {"id": term_id, "label": label}}


def _entry(pathophysiology, environmental=None):
    data = {"pathophysiology": pathophysiology}
    if environmental is not None:
        data["environmental"] = environmental
    return data


def test_somatic_lesion_is_read_from_the_marker_not_from_a_role_string():
    origins = find_origins(
        _entry(
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
    )
    assert [o.rule for o in origins] == [RULE_SOMATIC]
    assert origins[0].cell_ids == {"CL:0002079"}


def test_an_initiating_role_alone_marks_nothing():
    """`role` is free text with ~90 values in the KB; it is not a claim."""
    origins = find_origins(
        _entry(
            [
                {
                    "name": "Malignant Transformation",
                    "role": "trigger",
                    "cell_types": [_cell("CL:0000134", "mesenchymal stem cell")],
                }
            ]
        )
    )
    assert origins == []


def test_a_somatic_lesion_off_a_root_node_still_counts():
    """A transformation or second-hit lesion is still where a somatic event was."""
    origins = find_origins(
        _entry(
            [
                {"name": "Precursor Lesion", "downstream": [{"target": "Second Hit"}]},
                {
                    "name": "Second Hit",
                    "genetic_context": {
                        "variant_origin": "SOMATIC",
                        "allelic_hit_role": "FIRST_HIT",
                    },
                    "cell_types": [_cell("CL:0000066", "epithelial cell")],
                },
            ]
        )
    )
    assert [o.name for o in origins] == ["Second Hit"]
    assert origins[0].first_hit


def test_environmental_trigger_covers_non_mutational_initiation():
    """HPV, H. pylori, asbestos: no host lesion to mark, but a curated link."""
    origins = find_origins(
        _entry(
            [
                {
                    "name": "HPV Infection of Anal Squamous Epithelium",
                    "cell_types": [_cell("CL:0009066", "stratified squamous epithelial cell")],
                }
            ],
            environmental=[
                {
                    "name": "HPV exposure",
                    "influences_mechanisms": [
                        {
                            "target": "HPV Infection of Anal Squamous Epithelium",
                            "environmental_effect": "TRIGGERS",
                        }
                    ],
                }
            ],
        )
    )
    assert [o.rule for o in origins] == [RULE_TRIGGER]


def test_a_non_triggering_environmental_effect_marks_nothing():
    origins = find_origins(
        _entry(
            [{"name": "Some Node", "cell_types": [_cell("CL:0000066", "epithelial cell")]}],
            environmental=[
                {
                    "name": "Exposure",
                    "influences_mechanisms": [
                        {"target": "Some Node", "environmental_effect": "EXACERBATES"}
                    ],
                }
            ],
        )
    )
    assert origins == []


def test_a_recorded_lesion_silences_the_exposure_link():
    """The PDAC case, and the reason rule 2 yields to rule 1.

    Chronic pancreatitis genuinely TRIGGERS the inflammation node, which binds
    macrophage and pancreatic stellate cell. But the entry also records the
    transforming lesion, and the cell of origin is the cell that lesion occurred
    in -- so the exposure is upstream context, not the origin.
    """
    origins = find_origins(
        _entry(
            [
                {
                    "name": "Chronic Pancreatic Inflammation",
                    "cell_types": [_cell("CL:0000235", "macrophage")],
                },
                {
                    "name": "KRAS Oncogene Activation",
                    "genetic_context": {"variant_origin": "SOMATIC"},
                    "cell_types": [_cell("CL:0002079", "pancreatic ductal cell")],
                },
            ],
            environmental=[
                {
                    "name": "Chronic pancreatitis",
                    "influences_mechanisms": [
                        {
                            "target": "Chronic Pancreatic Inflammation",
                            "environmental_effect": "TRIGGERS",
                        }
                    ],
                }
            ],
        )
    )
    assert [o.rule for o in origins] == [RULE_SOMATIC]
    assert origins[0].cell_ids == {"CL:0002079"}


def test_a_paraneoplastic_syndrome_is_not_a_neoplasm(tmp_path):
    """It is a disease of a tumor's host; it has no cell of origin of its own."""
    entry = tmp_path / "Fake_Paraneoplastic.yaml"
    entry.write_text(
        "name: Paraneoplastic Something\ncategory: Autoimmune\n"
        "pathophysiology:\n- name: Autoantibody Production\n"
    )
    report = assess(entry)
    assert report is not None
    assert not report.is_neoplasm


def test_multiple_origin_cells_are_reported_as_the_lump_split_signal(tmp_path):
    entry = tmp_path / "Fake_Pool.yaml"
    entry.write_text(
        "name: Fake Renal Sarcoma\n"
        "categories:\n- Sarcoma\n"
        "pathophysiology:\n"
        "- name: Malignant Transformation of Renal Mesenchyme\n"
        "  genetic_context:\n    variant_origin: SOMATIC\n"
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
    assert "CL:0000235" not in {cid for cid, _ in pdac.origin_cells}


def test_script_is_advisory_by_default_and_gates_only_when_asked():
    """Most of the corpus is unmarked, so a default non-zero exit would be noise."""
    advisory = subprocess.run(
        [sys.executable, str(SCRIPT)],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=False,
    )
    assert advisory.returncode == 0, advisory.stderr

    gated = subprocess.run(
        [sys.executable, str(SCRIPT), "--fail-on", FINDING_NO_ORIGIN],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=False,
    )
    assert gated.returncode == 1


def test_format_list_prints_one_line_per_entry():
    """The docs promise a line per entry; it must actually be produced."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--format", "list"],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    lines = [
        line
        for line in result.stdout.splitlines()
        if line.startswith("kb/disorders/") and "\t" in line
    ]
    assert len(lines) > 100
    assert any("SOMATIC_LESION" in line for line in lines)


def test_viral_oncoprotein_entries_derive_through_the_exposure_rule():
    """HPV E7 inactivating pRB is not a host lesion (the HTLV-1 Tax precedent).

    These four entries were wrongly marked SOMATIC by the backfill, which also
    suppressed the exposure rule that should answer for them -- rule 1 takes
    precedence, so a spurious mark silences rule 2.
    """
    for slug in (
        "Anal_Canal_Carcinoma",
        "Cervical_Cancer",
        "Cervical_Squamous_Cell_Carcinoma",
        "HPV_Positive_Head_and_Neck_Cancer",
    ):
        report = assess(ROOT / "kb" / "disorders" / f"{slug}.yaml")
        assert report is not None, slug
        assert report.rules == [RULE_TRIGGER], (slug, report.rules)
        assert report.origin_cells, slug
