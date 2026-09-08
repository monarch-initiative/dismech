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
import types
from pathlib import Path
from typing import ClassVar

# See the note in test_causal_targets.py: the `sys.path` preamble must sit
# directly before the import for ruff's E402 allowance to apply.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import check_gene_term_identity as gti
from check_gene_term_identity import (
    NAMES_ANOTHER_GENE,
    NOT_HGNC,
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
    defaults = {
        "path": "x.yaml",
        "slot": "gene_term",
        "curie": "hgnc:20856",
        "curated_label": "THAP1",
        "preferred_term": "",
        "entry_name": "",
    }
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


def test_a_non_hgnc_term_is_out_of_scope_rather_than_uncached():
    """Nine animal-model `genes[]` entries bind mouse `MGI:` orthologs.

    This script resolves HGNC only, so it cannot have an opinion on those. They
    are kept apart from `uncached` because the remedies differ: an uncached HGNC
    CURIE is one `just validate-terms` run from being checkable, and an MGI one
    is not, so folding them together sends a curator chasing rows that will never
    resolve.
    """
    assert verdicts([binding(slot="genes", curie="MGI:94872")]) == [NOT_HGNC]


def test_hyphenated_prose_still_matches_the_bound_symbol():
    """`GUCY1A3-associated ...` is one greedy token, and the symbol is in it."""
    assert verdicts(
        [
            binding(
                curie="hgnc:4177",
                preferred_term="",
                entry_name="GBA-associated parkinsonism susceptibility",
            )
        ]
    ) == [OK]


def test_hyphen_parts_are_never_read_as_naming_another_gene():
    """Splitting in the accusing direction would invent findings out of
    punctuation: `MT-TE` would offer `TE` as the gene the entry "really" means.
    Parts satisfy a binding; only whole tokens may accuse one."""
    # `TE` is a known gene here; the whole token `MT-TE` is not. Splitting in
    # the accusing direction is what would turn this into a confident finding.
    labels = {**LABELS, "hgnc:11800": "TE"}
    (found,) = classify(
        [binding(slot="genes", curie="hgnc:4177", preferred_term="MT-TE")], labels
    )
    assert found.verdict == SYMBOL_UNEXPLAINED


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


def test_findings_only_is_refused_rather_than_ignored():
    """It filters the TSV rows; silently doing nothing to a report is worse than
    saying so."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--findings-only", "tests/data"],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=False,
    )
    assert result.returncode == 2
    assert "--findings-only applies to --format tsv" in result.stderr


def test_the_report_is_advisory_and_exits_zero():
    """New and unproven, so it reports rather than gates (#10948). Wiring this
    into `just qc` needs a decision about the advisory rows first."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "gene bindings examined:" in result.stdout


def _run(args, path):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args, str(path)],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=False,
    )


def test_strict_gates_a_confident_finding(tmp_path):
    """`--strict` exists for whoever gates this later, so it must fire here.

    The entry says GBA, the binding resolves to THAP1, and both symbols are
    bound elsewhere in `kb/` — so this is the confident class offline.
    """
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
    result = _run(["--strict"], named)
    assert result.returncode == 1, result.stdout
    assert "NAMES A DIFFERENT GENE             : 1" in result.stdout


def test_strict_stays_quiet_on_an_advisory_row(tmp_path):
    """An advisory row must not gate, however `--strict` is invoked.

    The text is a lowercase product name, so it can never be promoted to the
    confident class: the reverse lookup is case-sensitive and HGNC labels are
    symbols. That matters because this test used to assert exit 0 for the
    THAP11/THAP1 demonstration instead, which held only while no entry had
    cached `THAP11` — and then #10937 curated the cblL-type disease, cached
    `hgnc:23194`, and turned somebody else's correct curation into a red build
    here. A test must not encode which CURIEs the KB happens to have cached.
    """
    advisory = tmp_path / "advisory.yaml"
    advisory.write_text(
        "name: Demo\n"
        "genetic:\n"
        "- name: sucrase-isomaltase deficiency\n"
        "  gene_term:\n"
        "    preferred_term: sucrase-isomaltase\n"
        "    term:\n"
        "      id: hgnc:10856\n"
        "      label: SI\n",
        encoding="utf-8",
    )
    for args in (["--strict"], []):
        result = _run(args, advisory)
        assert result.returncode == 0, result.stdout
        assert "NAMES A DIFFERENT GENE             : 0" in result.stdout
        assert "symbol not named (advisory)        : 1" in result.stdout


def test_an_uncached_curie_never_gates(tmp_path):
    """`uncached` is "no opinion", so it cannot fail a build even under --strict."""
    unknown = tmp_path / "unknown.yaml"
    unknown.write_text(
        "name: Demo\n"
        "genetic:\n"
        "- name: NOTAGENE\n"
        "  gene_term:\n"
        "    preferred_term: NOTAGENE\n"
        "    term:\n"
        "      id: hgnc:99999999\n"
        "      label: NOTAGENE\n",
        encoding="utf-8",
    )
    result = _run(["--strict"], unknown)
    assert result.returncode == 0, result.stdout
    assert "HGNC CURIE not cached (no opinion) : 1" in result.stdout


class _FakeAdapter:
    """The three HGNC lookups `resolve_online` makes, backed by a fixed table."""

    LABELS: ClassVar[dict[str, str]] = {
        "hgnc:20856": "THAP1",
        "hgnc:23194": "THAP11",
        "hgnc:4177": "GBA",
        "hgnc:26019": "BPNT2",
    }
    ALIASES: ClassVar[dict[str, set[str]]] = {
        "hgnc:4177": {"GBA", "GBA1", "glucocerebrosidase"}
    }

    def label(self, curie):
        return self.LABELS.get(curie.lower())

    def entity_aliases(self, curie):
        return self.ALIASES.get(curie.lower(), {self.LABELS.get(curie.lower(), "")})

    def basic_search(self, symbol):
        return [c for c, label in self.LABELS.items() if label == symbol]


def _with_fake_adapter(monkeypatch):
    """`resolve_online` imports oaklib lazily, so stub the module it reaches for."""
    module = types.ModuleType("oaklib")
    module.get_adapter = lambda spec: _FakeAdapter()
    monkeypatch.setitem(sys.modules, "oaklib", module)


def test_resolve_gives_the_uncached_rows_a_verdict(monkeypatch):
    """Offline an uncached CURIE gets no opinion, so a wrong binding hides there.

    `--resolve` fetches the label and classifies the row as a cached one would be,
    which is what stops that being invisible in both modes.
    """
    _with_fake_adapter(monkeypatch)
    findings = classify([binding(preferred_term="THAP11", entry_name="THAP11")], {})
    assert [f.verdict for f in findings] == [UNCACHED]

    (resolved,) = gti.resolve_online(findings, {})
    assert resolved.verdict == NAMES_ANOTHER_GENE
    assert resolved.ontology_label == "THAP1"
    assert resolved.detail == ("THAP11",)


def test_resolve_explains_a_previous_symbol(monkeypatch):
    """`GBA1` is a synonym of `hgnc:4177`, so the binding is correct (#10102)."""
    _with_fake_adapter(monkeypatch)
    findings = classify(
        [binding(curie="hgnc:4177", preferred_term="GBA1")], {"hgnc:4177": "GBA"}
    )
    assert [f.verdict for f in findings] == [SYMBOL_UNEXPLAINED]

    (resolved,) = gti.resolve_online(findings, {"hgnc:4177": "GBA"})
    assert resolved.verdict == gti.PREVIOUS_SYMBOL
    assert resolved.detail == ("GBA1",)


def test_resolve_substitutes_uncached_rows_positionally(monkeypatch):
    """The subtlest part of the two-pass design, and the reason for a test.

    Pass one replaces only the `uncached` rows, identifying them by position
    because two identical `Binding`s compare equal — so a value-keyed lookup
    would collapse them. This pins order preservation with other verdicts
    interleaved, and that pass two still sees the rows pass one produced.
    """
    _with_fake_adapter(monkeypatch)
    labels = {"hgnc:4177": "GBA"}
    bindings = [
        binding(path="a.yaml", preferred_term="THAP11", entry_name="THAP11"),
        binding(path="b.yaml", curie="hgnc:4177", preferred_term="GBA"),
        binding(path="c.yaml", slot="genes", curie="MGI:94872"),
        binding(path="d.yaml", curie="hgnc:4177", preferred_term="GBA1"),
    ]
    offline = classify(bindings, labels)
    assert [f.verdict for f in offline] == [
        UNCACHED,
        OK,
        NOT_HGNC,
        SYMBOL_UNEXPLAINED,
    ]

    online = gti.resolve_online(offline, labels)
    assert [f.binding.path for f in online] == ["a.yaml", "b.yaml", "c.yaml", "d.yaml"]
    assert [f.verdict for f in online] == [
        NAMES_ANOTHER_GENE,
        OK,
        NOT_HGNC,
        gti.PREVIOUS_SYMBOL,
    ]


def test_resolve_leaves_an_unresolvable_uncached_row_alone(monkeypatch):
    """A CURIE the build has no label for stays `uncached`, not a finding.

    Silence from the ontology is a fact about the build, not about the binding.
    """
    _with_fake_adapter(monkeypatch)
    findings = classify([binding(curie="hgnc:99999", preferred_term="NOPE")], {})
    (resolved,) = gti.resolve_online(findings, {})
    assert resolved.verdict == UNCACHED


def test_resolve_keeps_an_uppercase_hgnc_binding_in_scope(monkeypatch):
    """#10948's report offered the CURIE as uppercase `HGNC:20856`.

    The prefix test runs on the lowercased CURIE, so an uppercase binding is
    still checked rather than dismissed as out-of-scope.
    """
    _with_fake_adapter(monkeypatch)
    findings = classify(
        [binding(curie="HGNC:20856", preferred_term="THAP11", entry_name="THAP11")],
        {},
    )
    assert [f.verdict for f in findings] == [UNCACHED]
    (resolved,) = gti.resolve_online(findings, {})
    assert resolved.verdict == NAMES_ANOTHER_GENE
