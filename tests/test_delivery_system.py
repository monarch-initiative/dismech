"""Tests for the Treatment-level `delivery_system` block and its consistency gate.

Two things are pinned here. The **schema** tests fix the shape of the
generalization: a carrier is a property of any treatment's formulation, so
`delivery_platform` must not be reachable only through `oligonucleotide_details`,
and the enums must keep the values that made the generalization worth doing
(`LIPOSOME` and `PROTEIN_NANOPARTICLE` name the two carriers the KB already had
curated with no slot to put them in).

The **check** tests fix what `scripts/check_delivery_system.py` treats as a
defect. Its job exists only because the nested copy was kept valid rather than
removed -- removing it would have invalidated the in-flight oligonucleotide
entries the way retiring `supports: PARTIAL` did in #10061 -- so for a while two
spellings are legal and something has to stop them drifting.

See scripts/check_delivery_system.py for why each gating class is a real defect
and why `LEGACY` is reported rather than gated.
"""

from pathlib import Path

import pytest
from linkml_runtime import SchemaView

from scripts.check_delivery_system import check_treatment, scan_repo

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "src" / "dismech" / "schema" / "dismech.yaml"


@pytest.fixture(scope="module")
def view() -> SchemaView:
    return SchemaView(str(SCHEMA))


def _check(tx: dict) -> set[str]:
    return {f.kind for f in check_treatment(Path("x.yaml"), "treatments[0]", tx)}


# --------------------------------------------------------------------- schema


def test_treatment_carries_delivery_system(view: SchemaView) -> None:
    assert "delivery_system" in view.class_slots("Treatment")


def test_delivery_system_carries_platform_and_targeting(view: SchemaView) -> None:
    slots = view.class_slots("DeliverySystem")
    for slot in (
        "delivery_platform",
        "targeting_ligand",
        "targeting_receptor",
        "target_cell_types",
    ):
        assert slot in slots, slot


def test_carrier_is_not_reachable_only_through_oligonucleotides(view: SchemaView) -> None:
    """The whole point of the change.

    `delivery_platform` has to be induced on a class a non-oligonucleotide
    treatment can actually reach, or an albumin-bound small molecule still has
    nowhere to record its carrier.
    """
    hosts = {
        cls
        for cls in view.all_classes()
        if "delivery_platform" in view.class_slots(cls)
    }
    assert "DeliverySystem" in hosts
    assert hosts != {"OligonucleotideDetail"}


def test_platform_enum_covers_the_carriers_the_kb_already_had(view: SchemaView) -> None:
    """LIPOSOME and PROTEIN_NANOPARTICLE are not speculative additions.

    Liposomal irinotecan (PDAC) and nab-sirolimus (PEComa) were curated before
    either value existed, with the carrier surviving only in a free-text
    `preferred_term`. LIPID_NANOPARTICLE is deliberately not a substitute for
    LIPOSOME: the ionizable lipid is what releases a nucleic-acid payload from
    the endosome, which a phospholipid bilayer vesicle does not do.
    """
    values = set(view.get_enum("DeliveryPlatformEnum").permissible_values)
    assert {"LIPOSOME", "PROTEIN_NANOPARTICLE", "LIPID_NANOPARTICLE"} <= values


def test_old_enum_names_survive_as_aliases(view: SchemaView) -> None:
    """Renaming an enum must not silently drop the name entries referred to."""
    assert "OligonucleotideDeliveryPlatformEnum" in (
        view.get_enum("DeliveryPlatformEnum").aliases or []
    )
    assert "OligonucleotideConjugationEnum" in (
        view.get_enum("TargetingLigandEnum").aliases or []
    )


def test_conjugation_is_deprecated_in_favour_of_targeting_ligand(view: SchemaView) -> None:
    """The nested spelling stays valid, but new entries must be steered away."""
    assert view.get_slot("conjugation").deprecated
    assert not view.get_slot("targeting_ligand").deprecated
    assert "targeting_ligand" in view.class_slots("OligonucleotideDetail")


# ---------------------------------------------------------------------- check


def test_conflicting_carrier_values_are_a_defect() -> None:
    assert "CONFLICT" in _check(
        {
            "name": "Conflicted",
            "delivery_system": {"delivery_platform": "LIPID_NANOPARTICLE"},
            "oligonucleotide_details": {"delivery_platform": "CONJUGATE"},
        }
    )


def test_same_value_in_both_homes_is_reported_but_not_a_conflict() -> None:
    kinds = _check(
        {
            "name": "Duplicated",
            "delivery_system": {"delivery_platform": "CONJUGATE"},
            "oligonucleotide_details": {"delivery_platform": "CONJUGATE"},
        }
    )
    assert kinds == {"DUPLICATE"}


def test_nested_only_carrier_is_legacy_not_a_failure() -> None:
    kinds = _check(
        {
            "name": "Nusinersen",
            "oligonucleotide_details": {
                "delivery_platform": "UNFORMULATED",
                "conjugation": "UNCONJUGATED",
            },
        }
    )
    assert kinds == {"LEGACY"}


def test_empty_delivery_system_is_a_defect() -> None:
    assert "EMPTY" in _check({"name": "Hollow", "delivery_system": {"notes": "tbd"}})


def test_receptor_without_a_ligand_to_reach_it_is_a_defect() -> None:
    """A named receptor plus UNCONJUGATED are contradictory claims.

    Passive accumulation is expressed by leaving the targeting slots absent, not
    by naming a receptor and then denying the means to bind it.
    """
    assert "LIGANDLESS_TARGET" in _check(
        {
            "name": "Contradictory",
            "delivery_system": {
                "delivery_platform": "LIPOSOME",
                "targeting_ligand": "UNCONJUGATED",
                "targeting_receptor": {"preferred_term": "ASGR1"},
            },
        }
    )


def test_passive_carrier_is_clean() -> None:
    assert _check({"name": "Doxil", "delivery_system": {"delivery_platform": "LIPOSOME"}}) == set()


def test_targeted_carrier_is_clean() -> None:
    assert (
        _check(
            {
                "name": "Vutrisiran",
                "delivery_system": {
                    "delivery_platform": "CONJUGATE",
                    "targeting_ligand": "GALNAC",
                    "targeting_receptor": {"preferred_term": "ASGR1"},
                    "target_cell_types": [{"preferred_term": "hepatocyte"}],
                },
            }
        )
        == set()
    )


def test_treatments_are_found_wherever_they_sit() -> None:
    """The walk is generic, not a `treatments:` lookup.

    A Treatment can sit at the disease level, in a module, or under a subtype.
    """
    from scripts.check_delivery_system import _walk

    found = _walk(
        {
            "has_subtypes": [
                {"treatments": [{"name": "Nested", "delivery_system": {"delivery_platform": "LIPOSOME"}}]}
            ]
        }
    )
    assert [name for name, _ in found] == ["has_subtypes[0].treatments[0] (Nested)"]


@pytest.mark.kb_data
def test_kb_has_no_gating_delivery_system_findings() -> None:
    failures = [
        f"{f.kind}: {f.path}: {f.location}: {f.detail}"
        for f in scan_repo()
        if f.kind in ("CONFLICT", "EMPTY", "LIGANDLESS_TARGET")
    ]
    assert not failures, "conflicting/empty/ligandless delivery_system record(s):\n  " + "\n  ".join(failures)
