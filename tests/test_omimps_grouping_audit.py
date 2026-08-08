"""Tests for the OMIM-phenotypic-series grouping audit (``scripts/omimps_grouping_audit.py``).

The audit answers whether an OMIMPS-derived MONDO class is a series of *diseases* (a
dismech grouping is well formed) or a series of *risk loci* (it is not — model one Disease
with ``genetic:`` risk-factor rows). Celiac disease / PS212750 is the motivating case: MONDO
holds its thirteen ``{susceptibility}`` members OUTSIDE the is-a tree, as
``predisposes_towards`` satellites with an explicit ``excluded_subClassOf``.

What is pinned here is the classification logic that decision rests on, against a synthetic
``mondo.obo`` fixture rather than the 53 MB release:

  * the descendant tier assignment and, specifically, its **precedence** — a declared
    susceptibility class stays SUSCEPTIBILITY even when MONDO also gives it a gene, and a
    gene-defined disease is never demoted to ACQUIRED by an unlucky label;
  * the ``UNMAPPED_LOCUS`` proxy for OMIM phenotype mapping key 2;
  * ``series_kind`` / ``heterogeneity_axes``, including that inbound predisposers count as
    risk-locus members even though they are not descendants (the celiac shape);
  * ``recipient_candidates``, which must not walk up through ``hereditary disease`` — the
    contaminated parent under audit — and mistake every hereditary class for a sibling.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
SCRIPT_PATH = ROOT / "scripts" / "omimps_grouping_audit.py"
SPEC = importlib.util.spec_from_file_location("omimps_grouping_audit", SCRIPT_PATH)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


# A miniature MONDO: a celiac-shaped susceptibility series, a cataract-shaped mixed class,
# and a craniosynostosis-shaped Mendelian series with a genetic-form recipient child.
FIXTURE_OBO = """format-version: 1.2

[Term]
id: MONDO:0003847
name: hereditary disease
intersection_of: MONDO:0700096 ! human disease
intersection_of: has_characteristic MONDO:0021152 ! inherited
relationship: has_characteristic MONDO:0021152 ! inherited

[Term]
id: MONDO:0005550
name: infectious disease

[Term]
id: MONDO:0009999
name: hereditary skin disorder
intersection_of: MONDO:0009998 ! skin disorder
intersection_of: has_characteristic MONDO:0021152 ! inherited

[Term]
id: MONDO:0000100
name: celiac disease
xref: OMIMPS:212750 {source="MONDO:equivalentTo"}
is_a: MONDO:0003847 ! hereditary disease
is_a: MONDO:0009999 ! hereditary skin disorder

[Term]
id: MONDO:0000101
name: celiac disease, susceptibility to, 1
subset: predisposition
xref: OMIM:212750 {source="MONDO:equivalentTo"}
is_a: MONDO:0020573 ! inherited disease susceptibility
relationship: excluded_subClassOf MONDO:0000100 ! celiac disease
relationship: predisposes_towards MONDO:0000100 ! celiac disease

[Term]
id: MONDO:0000102
name: celiac disease, susceptibility to, 2
subset: predisposition
is_a: MONDO:0020573 ! inherited disease susceptibility
relationship: predisposes_towards MONDO:0000100 ! celiac disease

[Term]
id: MONDO:0000103
name: Lane Hamilton syndrome
is_a: MONDO:0000100 ! celiac disease

[Term]
id: MONDO:0000200
name: cataract
xref: OMIMPS:116200 {source="MONDO:equivalentTo"}
is_a: MONDO:0003847 ! hereditary disease

[Term]
id: MONDO:0000201
name: cataract 1 multiple types
xref: OMIM:116200 {source="MONDO:equivalentTo"}
is_a: MONDO:0000200 ! cataract
relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4281 ! GJA8

[Term]
id: MONDO:0000206
name: cataract 2 multiple types
xref: OMIM:604307 {source="MONDO:equivalentTo"}
is_a: MONDO:0000200 ! cataract
relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/2705 ! CRYGC

[Term]
id: MONDO:0000202
name: senile cataract
is_a: MONDO:0000200 ! cataract

[Term]
id: MONDO:0000203
name: diabetic cataract
is_a: MONDO:0000200 ! cataract

[Term]
id: MONDO:0000204
name: cataract 40
xref: OMIM:302200 {source="MONDO:equivalentTo"}
is_a: MONDO:0000200 ! cataract

[Term]
id: MONDO:0000205
name: infectious cataract-like disorder
is_a: MONDO:0000200 ! cataract
is_a: MONDO:0005550 ! infectious disease

[Term]
id: MONDO:0000300
name: craniosynostosis
xref: OMIMPS:123100 {source="MONDO:equivalentTo"}
is_a: MONDO:0003847 ! hereditary disease

[Term]
id: MONDO:0000301
name: syndromic craniosynostosis
is_a: MONDO:0000300 ! craniosynostosis

[Term]
id: MONDO:0000302
name: Apert syndrome
is_a: MONDO:0000301 ! syndromic craniosynostosis
relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/3689 ! FGFR2

[Term]
id: MONDO:0000303
name: Crouzon syndrome
is_a: MONDO:0000301 ! syndromic craniosynostosis
relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/3689 ! FGFR2

[Term]
id: MONDO:0000304
name: Muenke syndrome
is_a: MONDO:0000301 ! syndromic craniosynostosis
relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/3688 ! FGFR3

[Term]
id: MONDO:0000305
name: diabetic craniosynostosis-like syndrome
is_a: MONDO:0000300 ! craniosynostosis
relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/9999 ! MADEUP

[Term]
id: MONDO:0000306
name: obsolete craniosynostosis 99
is_a: MONDO:0000300 ! craniosynostosis
is_obsolete: true
"""


def _mondo(tmp_path):
    path = tmp_path / "mini_mondo.obo"
    path.write_text(FIXTURE_OBO, encoding="utf-8")
    return audit.Mondo(str(path))


def test_parses_graph_xrefs_and_predisposers(tmp_path):
    m = _mondo(tmp_path)
    assert m.label["MONDO:0000100"] == "celiac disease"
    assert m.omimps["MONDO:0000100"] == ["OMIMPS:212750"]
    assert m.descendants("MONDO:0000100") == {"MONDO:0000103"}
    # Susceptibility satellites are NOT descendants -- MONDO excludes them on purpose.
    assert set(m.predisposers["MONDO:0000100"]) == {"MONDO:0000101", "MONDO:0000102"}
    # Obsolete descendants are dropped.
    assert "MONDO:0000306" not in m.descendants("MONDO:0000300")


def test_tier_assignment_and_precedence(tmp_path):
    m = _mondo(tmp_path)
    assert m.tier("MONDO:0000201") == "MENDELIAN"
    assert m.tier("MONDO:0000202") == "ACQUIRED"          # "senile"
    assert m.tier("MONDO:0000203") == "ACQUIRED"          # "diabetic"
    assert m.tier("MONDO:0000205") == "INFECTIOUS"        # infectious beats everything
    assert m.tier("MONDO:0000103") == "UNSPECIFIED"       # no OMIM xref, no gene, no marker
    # OMIM xref but no gene relation: the mapping-key-2 proxy.
    assert m.tier("MONDO:0000204") == "UNMAPPED_LOCUS"
    # Declared susceptibility outranks a gene relation...
    assert m.tier("MONDO:0000101") == "SUSCEPTIBILITY"
    # ...and a gene relation outranks an acquired-looking label, so a real Mendelian
    # disease is never miscounted as acquired.
    assert m.tier("MONDO:0000305") == "MENDELIAN"


def test_celiac_shape_is_a_susceptibility_series(tmp_path):
    m = _mondo(tmp_path)
    row = audit.analyse(m, "MONDO:0000100", {}, {}, {})
    assert row["kind"] == "SUSCEPTIBILITY_SERIES"
    assert row["axes"] == ["RISK_LOCUS"]
    assert len(row["predisposers"]) == 2
    assert row["counts"]["MENDELIAN"] == 0
    assert audit.recommend({**row, "recommendation": None}) == "SINGLE_DISEASE"


def test_mixed_and_mendelian_shapes(tmp_path):
    m = _mondo(tmp_path)
    cataract = audit.analyse(m, "MONDO:0000200", {}, {}, {})
    assert cataract["kind"] == "MIXED_GENETIC_ACQUIRED"
    assert cataract["axes"] == ["MENDELIAN", "RISK_LOCUS", "ACQUIRED"]

    cranio = audit.analyse(m, "MONDO:0000300", {}, {}, {})
    assert cranio["kind"] == "MENDELIAN_SERIES"
    assert cranio["axes"] == ["MENDELIAN"]


def test_inherited_superclasses_are_reported(tmp_path):
    m = _mondo(tmp_path)
    row = audit.analyse(m, "MONDO:0000100", {}, {}, {})
    # The lateral damage: not just 'hereditary disease' but every
    # '<genus> and has_characteristic some inherited' class the term falls under.
    assert row["inherited_superclasses"] == ["MONDO:0003847", "MONDO:0009999"]


def test_recipient_candidates_do_not_leak_through_hereditary_disease(tmp_path):
    m = _mondo(tmp_path)
    cranio = audit.recipient_candidates(m, "MONDO:0000300")
    assert [c[1] for c in cranio] == ["MONDO:0000301"]  # syndromic craniosynostosis, 3 genes
    # celiac shares the 'hereditary disease' parent with craniosynostosis and cataract;
    # walking that parent would offer them as siblings. It must not.
    assert audit.recipient_candidates(m, "MONDO:0000100") == []


def test_dismech_coverage_counts_distinct_entries(tmp_path):
    m = _mondo(tmp_path)
    # One dismech entry anchoring two MONDO ids is ONE member, not two: a single-entry
    # "series" is a has_subtypes catalog, not a grouping.
    disorders = {"MONDO:0000302": {"Apert Syndrome"}, "MONDO:0000303": {"Apert Syndrome"}}
    row = audit.analyse(m, "MONDO:0000300", disorders, {}, {})
    assert row["genetic_entries"] == ["Apert Syndrome"]
    assert audit.recommend({**row}) == "GROUPING_DEFERRED"

    disorders["MONDO:0000304"] = {"Muenke Syndrome"}
    disorders["MONDO:0000305"] = {"Third Entry"}
    row = audit.analyse(m, "MONDO:0000300", disorders, {}, {})
    assert len(row["genetic_entries"]) == 3
    assert audit.recommend({**row}) == "GROUPING_CANDIDATE"


def test_existing_grouping_overlap_suppresses_a_new_grouping(tmp_path):
    m = _mondo(tmp_path)
    disorders = {
        "MONDO:0000302": {"Apert Syndrome"},
        "MONDO:0000303": {"Crouzon Syndrome"},
        "MONDO:0000304": {"Muenke Syndrome"},
    }
    members = {"FGFR-Related Skeletal Dysplasias": {"Apert Syndrome", "Crouzon Syndrome"}}
    row = audit.analyse(m, "MONDO:0000300", disorders, {}, members)
    assert row["grouping_overlap"][0] == (2, "FGFR-Related Skeletal Dysplasias")
    assert audit.recommend({**row}) == "COVERED_BY_GROUPING"
