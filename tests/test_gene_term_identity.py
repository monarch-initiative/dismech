"""A gene binding has to name the gene the entry means, not just itself (#10948).

`linkml-term-validator` checks a `term.id` against its `term.label` and against
nothing else, so a binding only has to be *self-consistent*:

    genetic:
    - name: THAP11
      gene_term:
        preferred_term: THAP11
        term: {id: hgnc:20856, label: THAP1}   # THAP1 is a different gene

That passes both `just validate` and `just validate-terms`. The inconsistent
version (`hgnc:20856` labelled `THAP11`) is caught, which is the perverse part:
filling the label in from the ontology turns a caught error into a silent one.

`scripts/check_gene_term_identity.py` compares the resolved label against the
`name` and `preferred_term` sitting directly above the binding. These tests pin
the tolerances as much as the findings -- a check that fires on the KB's 27
model-organism symbols and 4 HLA serotypes would be turned off rather than fixed.
"""

import subprocess
import sys
from pathlib import Path

# See the note in test_causal_targets.py: the `sys.path` preamble must sit
# directly before the import for ruff's E402 allowance to apply.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import check_gene_term_identity as gti
from check_gene_term_identity import (
    NAMES_ANOTHER_GENE,
    OK,
    SYMBOL_UNEXPLAINED,
    UNCACHED,
    Binding,
    classify,
    iter_gene_bindings,
)

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_gene_term_identity.py"

LABELS = {
    "hgnc:20856": "THAP1",
    "hgnc:23194": "THAP11",
    "hgnc:4177": "GBA",
    "hgnc:15766": "ADNP",
    "hgnc:4932": "HLA-B",
    "hgnc:6080": "INPPL1",
    "hgnc:10856": "SI",
}


def binding(**kwargs) -> Binding:
    defaults = dict(
        path="x.yaml",
        slot="gene_term",
        curie="hgnc:20856",
        curated_label="THAP1",
        preferred_term="",
        entry_name="",
    )
    return Binding(**{**defaults, **kwargs})


def verdicts(bindings) -> list[str]:
    return [f.verdict for f in classify(bindings, LABELS)]


def test_the_gene_the_entry_names_is_clean():
    assert verdicts([binding(preferred_term="THAP1", entry_name="THAP1")]) == [OK]


def test_self_consistent_binding_to_the_wrong_gene_is_a_finding():
    """The #10948 demonstration: label agrees with the CURIE, both name THAP1,
    and the entry says THAP11 twice."""
    (found,) = classify([binding(preferred_term="THAP11", entry_name="THAP11")], LABELS)
    assert found.verdict == NAMES_ANOTHER_GENE
    assert found.ontology_label == "THAP1"
    assert found.detail == ("THAP11",)


def test_the_named_gene_is_reported_once_however_many_fields_carry_it():
    """`name` and `preferred_term` both saying THAP11 is one disagreement."""
    (found,) = classify([binding(preferred_term="THAP11", entry_name="THAP11")], LABELS)
    assert found.detail == ("THAP11",)


def test_a_symbol_no_binding_has_cached_stays_advisory():
    """Offline, the confident class needs the other gene to be *known*.

    Recognizing a symbol depends on some other entry having bound it, so a wrong
    binding whose intended gene appears nowhere else in the KB can only be
    reported as unexplained. Saying so is the point: `--resolve` is what promotes
    it, and overclaiming here would make the tool wrong rather than incomplete.
    """
    labels = {k: v for k, v in LABELS.items() if k != "hgnc:23194"}
    (found,) = classify([binding(preferred_term="THAP11", entry_name="THAP11")], labels)
    assert found.verdict == SYMBOL_UNEXPLAINED


def test_a_previous_symbol_is_advisory_not_a_finding():
    """`GBA1` bound to `hgnc:4177` (`GBA`) is CORRECT -- the OBO build lags the
    live rename (#10102). Nothing offline can tell it from a wrong binding, so it
    lands in the advisory class and must never reach the confident one."""
    (found,) = classify(
        [binding(curie="hgnc:4177", preferred_term="GBA1", entry_name="GBA1")],
        LABELS,
    )
    assert found.verdict == SYMBOL_UNEXPLAINED


def test_the_symbol_may_be_embedded_in_allele_level_text():
    """`name` legitimately carries variant detail around the symbol (#9017)."""
    assert verdicts(
        [
            binding(
                curie="hgnc:4177",
                preferred_term="GBA (glucocerebrosidase)",
                entry_name="Biallelic GBA loss-of-function variants",
            )
        ]
    ) == [OK]


def test_a_longer_symbol_containing_the_bound_one_is_not_a_match():
    """The whole defect: `THAP1` must not be satisfied by the text `THAP11`."""
    assert verdicts([binding(preferred_term="THAP11xyz")]) != [OK]


def test_model_organism_symbol_case_is_tolerated():
    """27 of the KB's bindings are mouse/zebrafish orthologs under animal
    models; flagging them would bury every real finding."""
    assert verdicts(
        [binding(slot="genes", curie="hgnc:15766", preferred_term="Adnp")]
    ) == [gti.ORTHOLOG_CASE]


def test_zebrafish_paralog_suffix_is_tolerated():
    assert verdicts(
        [binding(slot="genes", curie="hgnc:6080", preferred_term="inppl1a")]
    ) == [gti.ORTHOLOG_CASE]


def test_hla_serotype_detail_is_tolerated():
    assert verdicts(
        [binding(slot="genes", curie="hgnc:4932", preferred_term="HLA-B27")]
    ) == [gti.HLA_SEROTYPE]


def test_the_serotype_tolerance_does_not_generalize_to_digit_suffixes():
    """`HLA-B27` -> `HLA-B` is tolerated; `THAP11` -> `THAP1` is the same shape
    and must not be. That is why the rule is restricted to the HLA loci."""
    assert not gti._is_hla_serotype("THAP1", "THAP11")
    assert gti._is_hla_serotype("HLA-B", "HLA-B27")


def test_a_confident_finding_beats_a_tolerance():
    """Tolerances are applied only after the confident class is decided, so a
    case-insensitive or serotype-shaped near-match can never swallow a binding
    whose text names a different known gene."""
    (found,) = classify([binding(preferred_term="Thap1 in the THAP11 locus")], LABELS)
    assert found.verdict == NAMES_ANOTHER_GENE


def test_an_uncached_curie_gets_no_opinion():
    assert verdicts([binding(curie="hgnc:99999")]) == [UNCACHED]


def test_enclosing_name_is_read_only_where_it_names_the_gene():
    """`Genetic.name` is the gene. A `Pathophysiology` or `Variant` `name` is a
    mechanism or an HGVS change, so a symbol appearing in it is incidental --
    reading it would invent disagreements out of unrelated prose."""
    on_pathophysiology = binding(
        slot="gene",
        curie="hgnc:20856",
        preferred_term="THAP1",
        entry_name="THAP11-driven transcriptional failure",
    )
    assert verdicts([on_pathophysiology]) == [OK]
    assert on_pathophysiology.texts == ("THAP1",)


def test_every_gene_descriptor_slot_is_walked():
    """All five slots whose range is `GeneDescriptor` in the schema."""
    data = {
        "genetic": [
            {
                "name": "A",
                "gene_term": {"term": {"id": "hgnc:1", "label": "A"}},
                "variants": [{"gene": {"term": {"id": "hgnc:2", "label": "B"}}}],
            }
        ],
        "has_subtypes": [{"genes": [{"term": {"id": "hgnc:3", "label": "C"}}]}],
        "treatments": [
            {"aso_details": {"target_gene": {"term": {"id": "hgnc:4", "label": "D"}}}}
        ],
        "computational_models": [
            {"perturbations": [{"term": {"id": "hgnc:5", "label": "E"}}]}
        ],
    }
    found = iter_gene_bindings(data, "x.yaml")
    assert {(b.slot, b.curie) for b in found} == {
        ("gene_term", "hgnc:1"),
        ("gene", "hgnc:2"),
        ("genes", "hgnc:3"),
        ("target_gene", "hgnc:4"),
        ("perturbations", "hgnc:5"),
    }


def test_a_descriptor_without_a_term_is_skipped():
    """An unbound `preferred_term` is a coverage gap, not an identity mismatch."""
    data = {"genetic": [{"name": "A", "gene_term": {"preferred_term": "A"}}]}
    assert iter_gene_bindings(data, "x.yaml") == []


def test_the_report_is_advisory_and_exits_zero():
    """New and unproven, so it reports rather than gates (#10948). Wiring this
    into `just qc` needs a decision about the 19 advisory rows first."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "gene bindings with an HGNC term:" in result.stdout


def test_strict_gates_the_confident_class_only(tmp_path):
    """`--strict` exists for whoever gates this later. It must fire on a wrong
    gene and stay quiet on the advisory rows, which are mostly renames."""
    wrong = tmp_path / "wrong.yaml"
    wrong.write_text(
        "name: Demo\n"
        "genetic:\n"
        "- name: THAP11\n"
        "  gene_term:\n"
        "    preferred_term: THAP11\n"
        "    term:\n"
        "      id: hgnc:20856\n"
        "      label: THAP1\n",
        encoding="utf-8",
    )
    for args, expected in ((["--strict"], 0), ([], 0)):
        # THAP11 is not itself bound anywhere in the KB, so offline this is the
        # advisory class and --strict stays quiet. Documented, not accidental.
        result = subprocess.run(
            [sys.executable, str(SCRIPT), *args, str(wrong)],
            capture_output=True,
            text=True,
            cwd=ROOT,
        )
        assert result.returncode == expected, result.stdout
        assert "hgnc:20856" in result.stdout

    named = tmp_path / "named.yaml"
    named.write_text(
        "name: Demo\n"
        "genetic:\n"
        "- name: GBA\n"
        "  gene_term:\n"
        "    preferred_term: GBA\n"
        "    term:\n"
        "      id: hgnc:20856\n"
        "      label: THAP1\n",
        encoding="utf-8",
    )
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--strict", str(named)],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    assert result.returncode == 1, result.stdout
    assert "NAMES A DIFFERENT GENE             : 1" in result.stdout
