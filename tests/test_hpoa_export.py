"""Tests for HPOA-extended exporter."""
from pathlib import Path

import pytest
import yaml

from dismech.export.hpoa_export import (
    export,
    hpoa_rows_for_disorder,
    normalize_frequency_enum,
    parse_frequency,
    slugify,
)


def _write(path: Path, payload: dict) -> Path:
    path.write_text(yaml.safe_dump(payload, sort_keys=False))
    return path


def test_slugify():
    assert slugify("22q11.2_Deletion_Syndrome") == "22q11-2-deletion-syndrome"
    assert slugify("Carpal Tunnel Syndrome") == "carpal-tunnel-syndrome"
    assert slugify("") == "unnamed"
    assert slugify("--leading---and---trailing--") == "leading-and-trailing"


def test_parse_frequency_percent_range():
    assert parse_frequency({"description": "occurs in 50-60% of patients"}) == "50-60%"


def test_parse_frequency_single_percent():
    assert (
        parse_frequency({"description": "Cardiac defects occur in 75% of patients"})
        == "75%"
    )


def test_parse_frequency_approximate():
    assert (
        parse_frequency({"description": "symptomatic in about 10% of reported patients"})
        == "10%"
    )


def test_parse_frequency_ratio():
    assert parse_frequency({"description": "observed in 12/45 patients"}) == "12/45"


def test_parse_frequency_falls_back_to_enum():
    assert parse_frequency({"description": "no number here", "frequency": "FREQUENT"}) == "HP:0040282"
    assert parse_frequency({"frequency": "VERY_RARE"}) == "HP:0040284"


def test_parse_frequency_returns_none_when_missing():
    assert parse_frequency({"description": "no number"}) is None
    assert parse_frequency({}) is None


def test_normalize_frequency_enum_tolerates_variants():
    assert normalize_frequency_enum("Frequent") == "FREQUENT"
    assert normalize_frequency_enum("very frequent") == "VERY_FREQUENT"
    assert normalize_frequency_enum("Very-Rare") == "VERY_RARE"
    # Orphanet-style banded labels: leading word is the canonical band
    assert normalize_frequency_enum("Frequent (79-30%)") == "FREQUENT"
    assert normalize_frequency_enum("Very frequent (99-80%)") == "VERY_FREQUENT"
    assert normalize_frequency_enum("Occasional (29-5%)") == "OCCASIONAL"
    # genuinely ambiguous free text is left unmapped rather than guessed
    assert normalize_frequency_enum("Common") is None
    assert normalize_frequency_enum("Rare") is None
    assert normalize_frequency_enum("Variable") is None
    assert normalize_frequency_enum(None) is None


def test_parse_frequency_enum_case_insensitive():
    assert parse_frequency({"frequency": "Frequent"}) == "HP:0040282"
    assert parse_frequency({"frequency": "very frequent"}) == "HP:0040281"


def test_parse_frequency_accepts_resolved_hp_term():
    assert parse_frequency({"frequency": "HP_0040281"}) == "HP:0040281"
    assert parse_frequency({"frequency": "HP:0040283"}) == "HP:0040283"


def test_excluded_frequency_emits_not_qualifier_and_blank_frequency(tmp_path):
    """frequency: EXCLUDED asserts absence -> NOT-qualified row, no frequency."""
    yaml_path = _write(
        tmp_path / "X.yaml",
        {
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "x"}},
            "creation_date": "2026-01-01T00:00:00Z",
            "phenotypes": [
                {
                    "name": "A",
                    "frequency": "EXCLUDED",
                    "phenotype_term": {"term": {"id": "HP:0000001", "label": "A"}},
                    "evidence": [
                        {"reference": "PMID:1", "evidence_source": "HUMAN_CLINICAL", "supports": "SUPPORT"},
                    ],
                },
            ],
        },
    )
    rows, _ = hpoa_rows_for_disorder(yaml_path)
    assert rows[0]["qualifier"] == "NOT"
    assert rows[0]["frequency"] == ""


def test_upstream_risk_phenotype_skipped_from_hpoa(tmp_path):
    """A phenotype driving a pathophysiology node is an upstream risk state, not a
    manifestation: it must NOT produce a phenotype.hpoa has_phenotype row."""
    yaml_path = _write(
        tmp_path / "X.yaml",
        {
            "disease_term": {"term": {"id": "MONDO:0007699", "label": "x"}},
            "creation_date": "2026-01-01T00:00:00Z",
            "pathophysiology": [{"name": "Thyroidal Oxidative Stress"}],
            "phenotypes": [
                {
                    "name": "Selenium Deficiency",
                    "phenotype_term": {
                        "term": {
                            "id": "HP:0033192",
                            "label": "Decreased circulating selenium concentration",
                        }
                    },
                    "sequelae": [{"target": "Thyroidal Oxidative Stress"}],
                    "evidence": [
                        {"reference": "PMID:1", "evidence_source": "HUMAN_CLINICAL", "supports": "SUPPORT"},
                    ],
                },
                {
                    "name": "Goiter",
                    "phenotype_term": {"term": {"id": "HP:0000853", "label": "Goiter"}},
                    "evidence": [
                        {"reference": "PMID:2", "evidence_source": "HUMAN_CLINICAL", "supports": "SUPPORT"},
                    ],
                },
            ],
        },
    )
    rows, _ = hpoa_rows_for_disorder(yaml_path)
    hpo_ids = {r["hpo_id"] for r in rows}
    assert "HP:0033192" not in hpo_ids  # upstream risk state skipped
    assert "HP:0000853" in hpo_ids  # real manifestation still emitted


def test_mondo_upstream_risk_phenotype_keeps_comorbidity_row(tmp_path):
    """A MONDO-typed upstream risk state still yields a comorbidity row.

    The comorbidity projection already emits the direction-neutral
    `biolink:associated_with`, so there is no `has_phenotype` inversion there to
    suppress — and KGX keeps the same edge. Dropping the row would make the two
    exporters disagree.
    """
    yaml_path = _write(
        tmp_path / "X.yaml",
        {
            "disease_term": {"term": {"id": "MONDO:0007699", "label": "x"}},
            "creation_date": "2026-01-01T00:00:00Z",
            "pathophysiology": [{"name": "Thyroidal Oxidative Stress"}],
            "phenotypes": [
                {
                    "name": "Vitamin D Deficiency",
                    "phenotype_term": {
                        "term": {"id": "MONDO:0100471", "label": "vitamin D deficiency"}
                    },
                    "sequelae": [{"target": "Thyroidal Oxidative Stress"}],
                    "evidence": [
                        {"reference": "PMID:1", "evidence_source": "HUMAN_CLINICAL", "supports": "SUPPORT"},
                    ],
                },
            ],
        },
    )
    rows, comorb_rows = hpoa_rows_for_disorder(yaml_path)
    assert rows == []  # never a has_phenotype row
    assert [r["comorbid_id"] for r in comorb_rows] == ["MONDO:0100471"]
    assert comorb_rows[0]["predicate"] == "biolink:associated_with"


def test_unbound_upstream_risk_phenotype_emits_no_row(tmp_path):
    """An ontology-unbound upstream risk state must not fall through to the
    synthetic `DISMECH:` id, which would be the same has_phenotype inversion."""
    yaml_path = _write(
        tmp_path / "X.yaml",
        {
            "disease_term": {"term": {"id": "MONDO:0007699", "label": "x"}},
            "creation_date": "2026-01-01T00:00:00Z",
            "pathophysiology": [{"name": "Thyroidal Oxidative Stress"}],
            "phenotypes": [
                {
                    "name": "Selenium Deficiency",
                    "sequelae": [{"target": "Thyroidal Oxidative Stress"}],
                    "evidence": [
                        {"reference": "PMID:1", "evidence_source": "HUMAN_CLINICAL", "supports": "SUPPORT"},
                    ],
                },
                {
                    "name": "Goiter",
                    "phenotype_term": {"term": {"id": "HP:0000853", "label": "Goiter"}},
                    "evidence": [
                        {"reference": "PMID:2", "evidence_source": "HUMAN_CLINICAL", "supports": "SUPPORT"},
                    ],
                },
            ],
        },
    )
    rows, _ = hpoa_rows_for_disorder(yaml_path)
    hpo_ids = {r["hpo_id"] for r in rows}
    assert not any(i.startswith("DISMECH:") for i in hpo_ids)
    assert hpo_ids == {"HP:0000853"}


def test_indirect_evidence_kept_as_positive(tmp_path):
    """Directness does not change the row: an indirect association is still one.

    HPOA has no slot for how directly the evidence bears on the claim, and an
    indirectly-evidenced phenotype association is still an association, so the
    row is positive with no qualifier.
    """
    yaml_path = _write(
        tmp_path / "X.yaml",
        {
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "x"}},
            "creation_date": "2026-01-01T00:00:00Z",
            "phenotypes": [
                {
                    "name": "A",
                    "phenotype_term": {"term": {"id": "HP:0000001", "label": "A"}},
                    "evidence": [
                        {
                            "reference": "PMID:1",
                            "evidence_source": "HUMAN_CLINICAL",
                            "supports": "SUPPORT",
                            "directness": "INDIRECT",
                        },
                    ],
                },
            ],
        },
    )
    rows, _ = hpoa_rows_for_disorder(yaml_path)
    assert len(rows) == 1
    assert rows[0]["qualifier"] == ""
    assert rows[0]["reference"] == "PMID:1"


def test_model_organism_evidence_dropped(tmp_path):
    yaml_path = _write(
        tmp_path / "Test_Disorder.yaml",
        {
            "name": "Test",
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "test"}},
            "creation_date": "2026-01-01T00:00:00Z",
            "phenotypes": [
                {
                    "name": "Phen A",
                    "frequency": "FREQUENT",
                    "phenotype_term": {"term": {"id": "HP:0000001", "label": "A"}},
                    "evidence": [
                        {"reference": "PMID:1", "evidence_source": "HUMAN_CLINICAL", "supports": "SUPPORT"},
                        {"reference": "PMID:2", "evidence_source": "MODEL_ORGANISM", "supports": "SUPPORT"},
                    ],
                },
            ],
        },
    )
    hpoa, _ = hpoa_rows_for_disorder(yaml_path)
    refs = [r["reference"] for r in hpoa]
    assert "PMID:1" in refs
    assert "PMID:2" not in refs


def test_phenotype_without_human_evidence_still_emits_iea_row(tmp_path):
    """A phenotype with only model-organism evidence still emits one IEA row anchored on the disease."""
    yaml_path = _write(
        tmp_path / "X.yaml",
        {
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "x"}},
            "creation_date": "2026-01-01T00:00:00Z",
            "phenotypes": [
                {
                    "name": "A",
                    "frequency": "OCCASIONAL",
                    "phenotype_term": {"term": {"id": "HP:0000001", "label": "A"}},
                    "evidence": [
                        {"reference": "PMID:99", "evidence_source": "MODEL_ORGANISM"},
                    ],
                },
            ],
        },
    )
    hpoa, _ = hpoa_rows_for_disorder(yaml_path)
    assert len(hpoa) == 1
    assert hpoa[0]["reference"] == "MONDO:0000001"
    assert hpoa[0]["evidence"] == "IEA"


def test_in_vitro_evidence_kept_as_pcs(tmp_path):
    yaml_path = _write(
        tmp_path / "X.yaml",
        {
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "x"}},
            "creation_date": "2026-01-01T00:00:00Z",
            "phenotypes": [
                {
                    "name": "A",
                    "phenotype_term": {"term": {"id": "HP:0000001", "label": "A"}},
                    "evidence": [
                        {"reference": "PMID:5", "evidence_source": "IN_VITRO"},
                    ],
                },
            ],
        },
    )
    hpoa, _ = hpoa_rows_for_disorder(yaml_path)
    assert hpoa[0]["evidence"] == "PCS"


def test_untyped_phenotype_emits_dismech_curie(tmp_path):
    yaml_path = _write(
        tmp_path / "ATTR_Amyloidosis.yaml",
        {
            "disease_term": {"term": {"id": "MONDO:0007100", "label": "ATTR amyloidosis"}},
            "creation_date": "2026-01-01T00:00:00Z",
            "phenotypes": [
                {
                    "name": "Carpal Tunnel Syndrome",
                    "frequency": "OCCASIONAL",
                    "phenotype_term": {"preferred_term": "Carpal Tunnel Syndrome"},
                    "evidence": [{"reference": "PMID:30404120", "evidence_source": "HUMAN_CLINICAL"}],
                },
            ],
        },
    )
    hpoa, _ = hpoa_rows_for_disorder(yaml_path)
    assert len(hpoa) == 1
    assert hpoa[0]["hpo_id"] == "DISMECH:attr-amyloidosis#carpal-tunnel-syndrome"
    assert hpoa[0]["dismech_name"] == "Carpal Tunnel Syndrome"
    assert hpoa[0]["evidence"] == "PCS"


def test_mondo_typed_routes_to_comorbidity(tmp_path):
    yaml_path = _write(
        tmp_path / "Campylobacteriosis.yaml",
        {
            "disease_term": {"term": {"id": "MONDO:0005688", "label": "campylobacteriosis"}},
            "creation_date": "2026-01-01T00:00:00Z",
            "phenotypes": [
                {
                    "name": "Guillain-Barre syndrome",
                    "phenotype_term": {"term": {"id": "MONDO:0016218", "label": "Guillain-Barre syndrome"}},
                    "evidence": [{"reference": "PMID:1", "evidence_source": "HUMAN_CLINICAL"}],
                },
            ],
        },
    )
    hpoa, comorb = hpoa_rows_for_disorder(yaml_path)
    assert hpoa == []
    assert len(comorb) == 1
    assert comorb[0]["comorbid_id"] == "MONDO:0016218"
    assert comorb[0]["predicate"] == "biolink:associated_with"
    assert comorb[0]["evidence"] == "PCS"


def test_refute_emits_NOT_qualifier(tmp_path):
    yaml_path = _write(
        tmp_path / "X.yaml",
        {
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "x"}},
            "creation_date": "2026-01-01T00:00:00Z",
            "phenotypes": [
                {
                    "name": "A",
                    "phenotype_term": {"term": {"id": "HP:0000001", "label": "A"}},
                    "evidence": [
                        {"reference": "PMID:1", "evidence_source": "HUMAN_CLINICAL", "supports": "REFUTE"},
                    ],
                },
            ],
        },
    )
    rows, _ = hpoa_rows_for_disorder(yaml_path)
    assert rows[0]["qualifier"] == "NOT"


def test_no_evidence_support_dropped(tmp_path):
    """NO_EVIDENCE items are dropped; a SUPPORT sibling on the same phenotype survives."""
    yaml_path = _write(
        tmp_path / "X.yaml",
        {
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "x"}},
            "creation_date": "2026-01-01T00:00:00Z",
            "phenotypes": [
                {
                    "name": "A",
                    "phenotype_term": {"term": {"id": "HP:0000001", "label": "A"}},
                    "evidence": [
                        {"reference": "PMID:1", "evidence_source": "HUMAN_CLINICAL", "supports": "SUPPORT"},
                        {"reference": "PMID:2", "evidence_source": "HUMAN_CLINICAL", "supports": "NO_EVIDENCE"},
                    ],
                },
            ],
        },
    )
    hpoa, _ = hpoa_rows_for_disorder(yaml_path)
    refs = [r["reference"] for r in hpoa]
    assert refs == ["PMID:1"]


def test_no_evidence_only_phenotype_falls_back_to_iea(tmp_path):
    """A phenotype whose only evidence is NO_EVIDENCE still emits one IEA row on the disease."""
    yaml_path = _write(
        tmp_path / "X.yaml",
        {
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "x"}},
            "creation_date": "2026-01-01T00:00:00Z",
            "phenotypes": [
                {
                    "name": "A",
                    "phenotype_term": {"term": {"id": "HP:0000001", "label": "A"}},
                    "evidence": [
                        {"reference": "PMID:1", "evidence_source": "HUMAN_CLINICAL", "supports": "NO_EVIDENCE"},
                    ],
                },
            ],
        },
    )
    hpoa, _ = hpoa_rows_for_disorder(yaml_path)
    assert len(hpoa) == 1
    assert hpoa[0]["reference"] == "MONDO:0000001"
    assert hpoa[0]["evidence"] == "IEA"


def test_no_evidence_comorbidity_dropped(tmp_path):
    """A MONDO-typed phenotype with only NO_EVIDENCE produces no comorbidity row."""
    yaml_path = _write(
        tmp_path / "X.yaml",
        {
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "x"}},
            "creation_date": "2026-01-01T00:00:00Z",
            "phenotypes": [
                {
                    "name": "A",
                    "phenotype_term": {"term": {"id": "MONDO:0016218", "label": "comorbid"}},
                    "evidence": [
                        {"reference": "PMID:1", "evidence_source": "HUMAN_CLINICAL", "supports": "NO_EVIDENCE"},
                    ],
                },
            ],
        },
    )
    hpoa, comorb = hpoa_rows_for_disorder(yaml_path)
    assert hpoa == []
    assert comorb == []


def test_non_mondo_disease_skipped(tmp_path):
    yaml_path = _write(
        tmp_path / "X.yaml",
        {
            "disease_term": {"term": {"id": "OMIM:12345"}},
            "phenotypes": [{"name": "A", "phenotype_term": {"term": {"id": "HP:0000001"}}}],
        },
    )
    hpoa, comorb = hpoa_rows_for_disorder(yaml_path)
    assert hpoa == []
    assert comorb == []


def test_one_row_per_evidence_item(tmp_path):
    yaml_path = _write(
        tmp_path / "X.yaml",
        {
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "x"}},
            "creation_date": "2026-01-01T00:00:00Z",
            "phenotypes": [
                {
                    "name": "A",
                    "phenotype_term": {"term": {"id": "HP:0000001", "label": "A"}},
                    "evidence": [
                        {"reference": "PMID:1", "evidence_source": "HUMAN_CLINICAL"},
                        {"reference": "PMID:2", "evidence_source": "HUMAN_CLINICAL"},
                    ],
                },
            ],
        },
    )
    rows, _ = hpoa_rows_for_disorder(yaml_path)
    assert [r["reference"] for r in rows] == ["PMID:1", "PMID:2"]


def test_export_writes_files(tmp_path):
    kb = tmp_path / "kb"
    kb.mkdir()
    _write(
        kb / "Test.yaml",
        {
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "test"}},
            "creation_date": "2026-01-01T00:00:00Z",
            "phenotypes": [
                {
                    "name": "A",
                    "phenotype_term": {"term": {"id": "HP:0000001", "label": "A"}},
                    "evidence": [{"reference": "PMID:1", "evidence_source": "HUMAN_CLINICAL"}],
                },
            ],
        },
    )
    out = tmp_path / "out"
    n_hpoa, n_comorb = export(kb, out)
    assert n_hpoa == 1
    assert n_comorb == 0
    content = (out / "phenotype.dismech.hpoa").read_text()
    assert content.startswith("#description:")
    assert "MONDO:0000001\ttest\t" in content


def test_frequency_disagreement_must_not_be_curated_as_refute(tmp_path):
    """A band disagreement is not a phenotype exclusion, and `supports` cannot say it.

    `Phenotype` has one flat `evidence:` list and no frequency-scoped evidence
    slot, so `supports` is scoped to the phenotype-disease assertion -- "does
    this phenotype occur in this disease" -- and never to the `frequency:` band.
    `REFUTE` therefore means *absent*, and maps here to the HPOA `NOT` qualifier.

    Curating a source that reports a *higher* frequency as `REFUTE`, to record
    that its band was not adopted, exports a row asserting the phenotype is
    excluded -- sourced to a reference saying it is nearly universal, and
    contradicting the positive row the same reference also produces. That
    regression was introduced and reverted while migrating Marfan syndrome's
    ORPHA:558 pneumothorax row (PR #10003); the band disagreement belongs in
    `explanation` and the phenotype's `notes:` instead.

    See docs/frequency-evidence-guidelines.md, option 2.
    """
    yaml_path = _write(
        tmp_path / "X.yaml",
        {
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "x"}},
            "creation_date": "2026-01-01T00:00:00Z",
            "phenotypes": [
                {
                    "name": "Spontaneous Pneumothorax",
                    "phenotype_term": {
                        "term": {"id": "HP:0002108", "label": "Spontaneous pneumothorax"}
                    },
                    "frequency": "OCCASIONAL",
                    "notes": "Orphanet says Very frequent (99-80%); the 5-11% estimate is kept.",
                    "evidence": [
                        {
                            "reference": "PMID:1",
                            "evidence_source": "HUMAN_CLINICAL",
                            "supports": "SUPPORT",
                        },
                        {
                            "reference": "ORPHA:558",
                            "evidence_source": "OTHER",
                            "supports": "SUPPORT",
                        },
                    ],
                },
            ],
        },
    )
    rows, _ = hpoa_rows_for_disorder(yaml_path)
    hp_rows = [r for r in rows if r["hpo_id"] == "HP:0002108"]

    assert hp_rows, "the phenotype should still be exported"
    assert not [r for r in hp_rows if r["qualifier"] == "NOT"], (
        "a frequency-band disagreement must not export as an HPOA NOT row"
    )

    # And the contradiction shape itself: one reference must never yield both a
    # positive and a NOT row for the same HP term.
    by_reference = {}
    for row in hp_rows:
        by_reference.setdefault(row["reference"], set()).add(row["qualifier"])
    for reference, qualifiers in by_reference.items():
        assert qualifiers != {"", "NOT"}, (
            f"{reference} emits both a positive and a NOT row for HP:0002108"
        )


def test_marfan_pneumothorax_exports_no_exclusion():
    """The real entry, not a fixture, must not export a NOT row for HP:0002108.

    The synthetic test above pins that the *correct* shape exports cleanly, but
    it builds both evidence items as SUPPORT, so it cannot fail if a REFUTE is
    re-added to the real file. This one reads
    ``kb/disorders/Marfan_Syndrome.yaml`` directly, so re-introducing the
    regression fixed in PR #10003 fails here.

    Scoped to the one entry deliberately. The invariant "one reference must not
    yield both a positive and a NOT row for the same HP term" cannot yet be a
    whole-KB gate: 11 (reference, HP term) pairs already violate it across
    kb/disorders/, all pre-existing. Promoting it needs a baseline in the style
    of check-snippet-grading, which is its own piece of work.
    """
    path = Path(__file__).resolve().parent.parent / "kb" / "disorders" / "Marfan_Syndrome.yaml"
    if not path.exists():  # entry renamed or removed; nothing to assert
        pytest.skip(f"{path.name} is not present")

    rows, _ = hpoa_rows_for_disorder(path)
    hp_rows = [r for r in rows if r["hpo_id"] == "HP:0002108"]

    assert hp_rows, "spontaneous pneumothorax should still be exported for Marfan syndrome"
    excluded = [r for r in hp_rows if r["qualifier"] == "NOT"]
    assert not excluded, (
        "Marfan syndrome must not export spontaneous pneumothorax as excluded; "
        f"got NOT row(s) from {[r['reference'] for r in excluded]}. A frequency-band "
        "disagreement is not an absence claim -- see docs/frequency-evidence-guidelines.md."
    )


# --- subtype propagation -----------------------------------------------------


def _ev(ref="PMID:1", supports="SUPPORT"):
    return [{"reference": ref, "supports": supports, "evidence_source": "HUMAN_CLINICAL"}]


def _subtyped_entry(phenotypes, subtypes=None):
    return {
        "disease_term": {"term": {"id": "MONDO:0000001", "label": "parent disease"}},
        "creation_date": "2026-01-01T00:00:00Z",
        "has_subtypes": subtypes
        if subtypes is not None
        else [
            {"name": "Type 1", "subtype_term": {"term": {"id": "MONDO:0000011", "label": "type 1"}}},
            {"name": "Type 2", "subtype_term": {"term": {"id": "MONDO:0000012", "label": "type 2"}}},
            {"name": "Unbound"},
        ],
        "phenotypes": phenotypes,
    }


def _by_disease(rows):
    out = {}
    for r in rows:
        out.setdefault(r["database_id"], []).append(r)
    return out


def test_unscoped_phenotype_propagates_to_every_mondo_subtype(tmp_path):
    path = _write(
        tmp_path / "d.yaml",
        _subtyped_entry(
            [
                {
                    "name": "Seizure",
                    "frequency": "FREQUENT",
                    "phenotype_term": {"term": {"id": "HP:0001250", "label": "Seizure"}},
                    "evidence": _ev(),
                }
            ]
        ),
    )
    rows, _ = hpoa_rows_for_disorder(path)
    by = _by_disease(rows)
    assert set(by) == {"MONDO:0000001", "MONDO:0000011", "MONDO:0000012"}
    parent = by["MONDO:0000001"][0]
    assert parent["inherited_from"] == ""
    assert parent["frequency"] == "HP:0040282"
    for sub_id, label in (("MONDO:0000011", "type 1"), ("MONDO:0000012", "type 2")):
        (row,) = by[sub_id]
        assert row["inherited_from"] == "MONDO:0000001"
        assert row["disease_name"] == label
        assert row["reference"] == "PMID:1"
        # The parent's frequency is across all subtypes; it is not inherited.
        assert row["frequency"] == ""


def test_obligate_frequency_and_absence_are_inherited(tmp_path):
    path = _write(
        tmp_path / "d.yaml",
        _subtyped_entry(
            [
                {
                    "name": "Always",
                    "frequency": "OBLIGATE",
                    "phenotype_term": {"term": {"id": "HP:0000001", "label": "A"}},
                    "evidence": _ev(),
                },
                {
                    "name": "Never",
                    "frequency": "EXCLUDED",
                    "phenotype_term": {"term": {"id": "HP:0000002", "label": "B"}},
                    "evidence": _ev(),
                },
            ]
        ),
    )
    rows, _ = hpoa_rows_for_disorder(path)
    sub = {r["hpo_id"]: r for r in rows if r["database_id"] == "MONDO:0000011"}
    assert sub["HP:0000001"]["frequency"] == "HP:0040280"
    assert sub["HP:0000002"]["qualifier"] == "NOT"


def test_scoped_phenotype_goes_to_its_subtype_and_parent_only(tmp_path):
    path = _write(
        tmp_path / "d.yaml",
        _subtyped_entry(
            [
                {
                    "name": "Cataract",
                    "subtype": "Type 2",
                    "description": "Seen in 40% of type 2 patients.",
                    "phenotype_term": {"term": {"id": "HP:0000518", "label": "Cataract"}},
                    "evidence": _ev(),
                }
            ]
        ),
    )
    rows, _ = hpoa_rows_for_disorder(path)
    by = _by_disease(rows)
    assert set(by) == {"MONDO:0000001", "MONDO:0000012"}
    (row,) = by["MONDO:0000012"]
    assert row["inherited_from"] == ""
    # Stated of the subtype itself, so its own frequency is kept.
    assert row["frequency"] == "40%"


def test_subtype_statement_overrides_inherited_row(tmp_path):
    path = _write(
        tmp_path / "d.yaml",
        _subtyped_entry(
            [
                {
                    "name": "Hearing loss",
                    "phenotype_term": {"term": {"id": "HP:0000365", "label": "Hearing impairment"}},
                    "evidence": _ev("PMID:1"),
                },
                {
                    "name": "No hearing loss in type 1",
                    "subtype": "Type 1",
                    "frequency": "EXCLUDED",
                    "phenotype_term": {"term": {"id": "HP:0000365", "label": "Hearing impairment"}},
                    "evidence": _ev("PMID:2"),
                },
            ]
        ),
    )
    rows, _ = hpoa_rows_for_disorder(path)
    type1 = [r for r in rows if r["database_id"] == "MONDO:0000011"]
    assert [(r["qualifier"], r["reference"]) for r in type1] == [("NOT", "PMID:2")]
    type2 = [r for r in rows if r["database_id"] == "MONDO:0000012"]
    assert [(r["qualifier"], r["inherited_from"]) for r in type2] == [("", "MONDO:0000001")]


def test_scoped_phenotype_reaches_children_via_unbound_grouping(tmp_path):
    subtypes = [
        {"name": "Group A", "children": ["A1", "A2"]},
        {"name": "A1", "subtype_term": {"term": {"id": "MONDO:0000021", "label": "a1"}}},
        {"name": "A2", "subtype_term": {"term": {"id": "MONDO:0000022", "label": "a2"}}},
        {"name": "B", "subtype_term": {"term": {"id": "MONDO:0000023", "label": "b"}}},
    ]
    path = _write(
        tmp_path / "d.yaml",
        _subtyped_entry(
            [
                {
                    "name": "Anemia",
                    "subtype": "Group A",
                    "phenotype_term": {"term": {"id": "HP:0001903", "label": "Anemia"}},
                    "evidence": _ev(),
                }
            ],
            subtypes,
        ),
    )
    rows, _ = hpoa_rows_for_disorder(path)
    by = _by_disease(rows)
    assert set(by) == {"MONDO:0000001", "MONDO:0000021", "MONDO:0000022"}
    # Group A has no identifier of its own, so the rows name the parent.
    assert by["MONDO:0000021"][0]["inherited_from"] == "MONDO:0000001"


def test_pointer_and_self_mapped_subtypes_receive_nothing(tmp_path):
    subtypes = [
        {
            "name": "Promoted",
            "curated_in": "Other_Entry",
            "subtype_term": {"term": {"id": "MONDO:0000031", "label": "promoted"}},
        },
        {"name": "Same", "subtype_term": {"term": {"id": "MONDO:0000001", "label": "parent"}}},
        {"name": "Ncit", "subtype_term": {"term": {"id": "NCIT:C1", "label": "x"}}},
    ]
    path = _write(
        tmp_path / "d.yaml",
        _subtyped_entry(
            [
                {
                    "name": "A",
                    "phenotype_term": {"term": {"id": "HP:0000001", "label": "A"}},
                    "evidence": _ev(),
                }
            ],
            subtypes,
        ),
    )
    rows, _ = hpoa_rows_for_disorder(path)
    assert {r["database_id"] for r in rows} == {"MONDO:0000001"}


def test_two_subtype_names_on_one_term_emit_once(tmp_path):
    subtypes = [
        {"name": "X", "subtype_term": {"term": {"id": "MONDO:0000041", "label": "x"}}},
        {"name": "X alias", "subtype_term": {"term": {"id": "MONDO:0000041", "label": "x"}}},
    ]
    path = _write(
        tmp_path / "d.yaml",
        _subtyped_entry(
            [
                {
                    "name": "A",
                    "phenotype_term": {"term": {"id": "HP:0000001", "label": "A"}},
                    "evidence": _ev(),
                }
            ],
            subtypes,
        ),
    )
    rows, _ = hpoa_rows_for_disorder(path)
    assert sum(r["database_id"] == "MONDO:0000041" for r in rows) == 1


def test_propagation_can_be_turned_off(tmp_path):
    path = _write(
        tmp_path / "d.yaml",
        _subtyped_entry(
            [
                {
                    "name": "A",
                    "phenotype_term": {"term": {"id": "HP:0000001", "label": "A"}},
                    "evidence": _ev(),
                }
            ]
        ),
    )
    rows, _ = hpoa_rows_for_disorder(path, propagate_subtypes=False)
    assert {r["database_id"] for r in rows} == {"MONDO:0000001"}


def test_subtype_with_its_own_entry_inherits_nothing(tmp_path):
    kb = tmp_path / "kb"
    kb.mkdir()
    _write(
        kb / "Parent.yaml",
        _subtyped_entry(
            [
                {
                    "name": "A",
                    "phenotype_term": {"term": {"id": "HP:0000001", "label": "A"}},
                    "evidence": _ev(),
                },
                {
                    "name": "B",
                    "subtype": "Type 1",
                    "phenotype_term": {"term": {"id": "HP:0000002", "label": "B"}},
                    "evidence": _ev(),
                },
            ]
        ),
    )
    _write(
        kb / "Type1.yaml",
        {
            "disease_term": {"term": {"id": "MONDO:0000011", "label": "type 1"}},
            "phenotypes": [
                {
                    "name": "C",
                    "phenotype_term": {"term": {"id": "HP:0000003", "label": "C"}},
                    "evidence": _ev(),
                }
            ],
        },
    )
    out = tmp_path / "out"
    export(kb, out)
    lines = [
        line.split("\t")
        for line in (out / "phenotype.dismech.hpoa").read_text().splitlines()
        if not line.startswith("#")
    ]
    header, body = lines[0], lines[1:]
    rows = [dict(zip(header, line)) for line in body]
    type1 = sorted(r["hpo_id"] for r in rows if r["database_id"] == "MONDO:0000011")
    # Its own entry's C, plus B stated of it directly by the parent; not A.
    assert type1 == ["HP:0000002", "HP:0000003"]
    type2 = [r["hpo_id"] for r in rows if r["database_id"] == "MONDO:0000012"]
    assert type2 == ["HP:0000001"]


def _chain_subtypes():
    return [
        {
            "name": "A",
            "children": ["A1"],
            "subtype_term": {"term": {"id": "MONDO:0000002", "label": "a"}},
        },
        {"name": "A1", "subtype_term": {"term": {"id": "MONDO:0000003", "label": "a1"}}},
    ]


def test_nearest_statement_wins_for_grandchildren(tmp_path):
    seizure = {"term": {"id": "HP:0001250", "label": "Seizure"}}
    path = _write(
        tmp_path / "d.yaml",
        _subtyped_entry(
            [
                {"name": "Seizure", "phenotype_term": seizure, "evidence": _ev("PMID:1")},
                {
                    "name": "No seizures in A",
                    "subtype": "A",
                    "phenotype_term": seizure,
                    "evidence": _ev("PMID:2", "REFUTE"),
                },
            ],
            _chain_subtypes(),
        ),
    )
    rows, _ = hpoa_rows_for_disorder(path)
    a1 = [(r["qualifier"], r["inherited_from"]) for r in rows if r["database_id"] == "MONDO:0000003"]
    # A states the term, so the parent's positive row stops at A.
    assert a1 == [("NOT", "MONDO:0000002")]


def test_unrelated_term_still_reaches_grandchildren(tmp_path):
    path = _write(
        tmp_path / "d.yaml",
        _subtyped_entry(
            [
                {
                    "name": "Seizure",
                    "phenotype_term": {"term": {"id": "HP:0001250", "label": "Seizure"}},
                    "evidence": _ev(),
                },
                {
                    "name": "Cataract in A",
                    "subtype": "A",
                    "phenotype_term": {"term": {"id": "HP:0000518", "label": "Cataract"}},
                    "evidence": _ev(),
                },
            ],
            _chain_subtypes(),
        ),
    )
    rows, _ = hpoa_rows_for_disorder(path)
    a1 = sorted(
        (r["hpo_id"], r["inherited_from"]) for r in rows if r["database_id"] == "MONDO:0000003"
    )
    assert a1 == [("HP:0000518", "MONDO:0000002"), ("HP:0001250", "MONDO:0000001")]


def test_mixed_parent_evidence_is_not_inherited(tmp_path):
    path = _write(
        tmp_path / "d.yaml",
        _subtyped_entry(
            [
                {
                    "name": "Immunodeficiency",
                    "phenotype_term": {"term": {"id": "HP:0002721", "label": "Immunodeficiency"}},
                    "evidence": _ev("PMID:1") + _ev("PMID:2", "REFUTE"),
                },
                {
                    "name": "Clean absence",
                    "phenotype_term": {"term": {"id": "HP:0000002", "label": "B"}},
                    "evidence": _ev("PMID:3", "REFUTE"),
                },
            ]
        ),
    )
    rows, _ = hpoa_rows_for_disorder(path)
    parent = sorted((r["hpo_id"], r["qualifier"]) for r in rows if r["database_id"] == "MONDO:0000001")
    assert parent == [("HP:0000002", "NOT"), ("HP:0002721", ""), ("HP:0002721", "NOT")]
    sub = [(r["hpo_id"], r["qualifier"]) for r in rows if r["database_id"] == "MONDO:0000011"]
    assert sub == [("HP:0000002", "NOT")]


# --- OMIM keying -------------------------------------------------------------


def _sssom(path: Path, rows) -> Path:
    lines = [
        "# curie_map:",
        "#   OMIM: https://omim.org/entry/",
        "subject_id\tsubject_label\tpredicate_id\tobject_id\tobject_label\tmapping_justification",
    ]
    lines += ["\t".join(r) + "\tsemapv:UnspecifiedMatching" for r in rows]
    path.write_text("\n".join(lines) + "\n")
    return path


def _read_tsv(path: Path) -> list[dict]:
    lines = [ln for ln in path.read_text().splitlines() if not ln.startswith("#")]
    header = lines[0].split("\t")
    return [dict(zip(header, ln.split("\t"))) for ln in lines[1:]]


def test_omim_key_rewrites_ids_and_reports_unmapped(tmp_path):
    kb = tmp_path / "kb"
    kb.mkdir()
    _write(
        kb / "Parent.yaml",
        _subtyped_entry(
            [
                {
                    "name": "Seizure",
                    "phenotype_term": {"term": {"id": "HP:0001250", "label": "Seizure"}},
                    "evidence": _ev(),
                },
                {
                    "name": "No evidence",
                    "phenotype_term": {"term": {"id": "HP:0000002", "label": "B"}},
                },
            ]
        ),
    )
    sssom = _sssom(
        tmp_path / "mondo.sssom.tsv",
        [
            # Type 1: a single exact OMIM match.
            ("MONDO:0000011", "type 1", "skos:exactMatch", "OMIM:100001", "TYPE 1 SYNDROME"),
            # Type 2: only a phenotypic series, and a non-exact OMIM match.
            ("MONDO:0000012", "type 2", "skos:exactMatch", "OMIMPS:100000", "SERIES"),
            ("MONDO:0000012", "type 2", "skos:closeMatch", "OMIM:100002", "CLOSE"),
            # Parent: two exact OMIM matches.
            ("MONDO:0000001", "parent", "skos:exactMatch", "OMIM:100003", "A"),
            ("MONDO:0000001", "parent", "skos:exactMatch", "OMIM:100004", "B"),
        ],
    )
    out = tmp_path / "out"
    export(kb, out, key="omim", sssom_path=sssom)

    rows = _read_tsv(out / "phenotype.dismech.omim.hpoa")
    assert {r["database_id"] for r in rows} == {"OMIM:100001"}
    by_hpo = {r["hpo_id"]: r for r in rows}
    assert by_hpo["HP:0001250"]["disease_name"] == "TYPE 1 SYNDROME"
    assert by_hpo["HP:0001250"]["mondo_id"] == "MONDO:0000011"
    assert by_hpo["HP:0001250"]["reference"] == "PMID:1"
    # Provenance stays in dismech's own namespace.
    assert by_hpo["HP:0001250"]["inherited_from"] == "MONDO:0000001"
    # An IEA row citing the parent itself keeps that citation: it names the
    # source disease, not this one.
    assert by_hpo["HP:0000002"]["reference"] == "MONDO:0000001"

    report = {r["mondo_id"]: r for r in _read_tsv(out / "omim_unmapped.tsv")}
    assert report["MONDO:0000001"]["reason"] == "multiple_omim"
    assert report["MONDO:0000001"]["candidates"] == "OMIM:100003 OMIM:100004"
    assert report["MONDO:0000001"]["rows_withheld"] == "2"
    assert report["MONDO:0000012"]["reason"] == "phenotypic_series_only"
    assert "MONDO:0000011" not in report


def test_omim_key_rewrites_self_citation(tmp_path):
    kb = tmp_path / "kb"
    kb.mkdir()
    _write(
        kb / "D.yaml",
        {
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "d"}},
            "phenotypes": [
                {"name": "A", "phenotype_term": {"term": {"id": "HP:0000001", "label": "A"}}}
            ],
        },
    )
    sssom = _sssom(
        tmp_path / "s.tsv",
        [("MONDO:0000001", "d", "skos:exactMatch", "OMIM:200000", "D SYNDROME")],
    )
    out = tmp_path / "out"
    n_hpoa, _ = export(kb, out, key="omim", sssom_path=sssom)
    (row,) = _read_tsv(out / "phenotype.dismech.omim.hpoa")
    assert n_hpoa == 1
    assert (row["database_id"], row["reference"], row["evidence"]) == (
        "OMIM:200000",
        "OMIM:200000",
        "IEA",
    )
    assert _read_tsv(out / "omim_unmapped.tsv") == []


def test_omim_key_needs_sssom(tmp_path):
    with pytest.raises(ValueError, match="sssom"):
        export(tmp_path, tmp_path / "out", key="omim")
