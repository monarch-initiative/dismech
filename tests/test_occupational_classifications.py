"""Tests for the occupational-disease and exposure/agent classification enums.

Covers the two disease-level occupational nosologies (ILO List of Occupational
Diseases, European schedule of occupational diseases) and the six agent-level
exposure axes, plus the structural invariants that make them safe to curate
against: no dangling ``is_a``, no fabricated numbering, and — the one that
matters most — that agent-level axes stay off ``Disease.classifications``.
"""

import re
from pathlib import Path

import pytest
import yaml
from linkml_runtime.utils.schemaview import SchemaView

from dismech.render import render_classification_pages

SCHEMA_PATH = Path("src/dismech/schema/dismech.yaml")
CLASSIFICATIONS_DIR = Path("src/dismech/schema/classifications")

DISEASE_LEVEL_ENUMS = {
    "ILOOccupationalDiseaseEnum": "ilo_occupational_category",
    "EUOccupationalScheduleEnum": "eu_occupational_category",
}

EXPOSURE_LEVEL_ENUMS = {
    "HazardAgentTypeEnum": "hazard_agent_type",
    "ExposureRouteEnum": "exposure_route",
    "ExposureDurationEnum": "exposure_duration",
    "IARCCarcinogenGroupEnum": "iarc_carcinogen_group",
    "GHSHealthHazardClassEnum": "ghs_health_hazard_class",
    "ExposomeDomainEnum": "exposome_domain",
}


@pytest.fixture(scope="module")
def schema_view() -> SchemaView:
    return SchemaView(str(SCHEMA_PATH))


@pytest.mark.parametrize("enum_name", [*DISEASE_LEVEL_ENUMS, *EXPOSURE_LEVEL_ENUMS])
def test_enum_is_defined(schema_view: SchemaView, enum_name: str) -> None:
    enum_def = schema_view.get_enum(enum_name)
    assert enum_def is not None, f"{enum_name} is not resolvable from dismech.yaml"
    assert enum_def.permissible_values, f"{enum_name} has no permissible values"


@pytest.mark.parametrize(
    "enum_name,slot_name",
    [*DISEASE_LEVEL_ENUMS.items(), *EXPOSURE_LEVEL_ENUMS.items()],
)
def test_slot_ranges_reach_the_enum(
    schema_view: SchemaView, enum_name: str, slot_name: str
) -> None:
    """Each slot must route to its enum via a ClassificationAssignment subclass."""
    slot = schema_view.get_slot(slot_name)
    assert slot is not None, f"slot {slot_name} is not defined"
    assignment = schema_view.get_class(slot.range)
    assert assignment is not None, f"{slot_name} range {slot.range} is not a class"
    assert assignment.is_a == "ClassificationAssignment", (
        f"{slot.range} must inherit ClassificationAssignment so it carries "
        "evidence and notes like every other classification assignment"
    )
    value_usage = assignment.slot_usage["classification_value"]
    assert value_usage.range == enum_name
    assert value_usage.required is True


@pytest.mark.parametrize("slot_name", DISEASE_LEVEL_ENUMS.values())
def test_disease_level_slots_are_on_disease_classifications(
    schema_view: SchemaView, slot_name: str
) -> None:
    assert slot_name in schema_view.get_class("DiseaseClassifications").slots


@pytest.mark.parametrize("slot_name", EXPOSURE_LEVEL_ENUMS.values())
def test_exposure_level_slots_are_not_on_disease_classifications(
    schema_view: SchemaView, slot_name: str
) -> None:
    """Agent-level axes must never leak into the disease-level container.

    An IARC group classifies the agent, not the disease. Putting it on
    ``DiseaseClassifications`` would assert that the disease itself carries the
    hazard classification.
    """
    assert slot_name in schema_view.get_class("ExposureClassifications").slots
    assert slot_name not in schema_view.get_class("DiseaseClassifications").slots


def test_environmental_carries_exposure_classifications(
    schema_view: SchemaView,
) -> None:
    assert "exposure_classifications" in schema_view.get_class("Environmental").slots


@pytest.mark.parametrize("enum_name", [*DISEASE_LEVEL_ENUMS, *EXPOSURE_LEVEL_ENUMS])
def test_no_dangling_is_a_and_every_value_documented(
    schema_view: SchemaView, enum_name: str
) -> None:
    """A dangling ``is_a`` silently drops a value out of the rendered tree."""
    values = schema_view.get_enum(enum_name).permissible_values
    for key, value in values.items():
        if value.is_a:
            assert value.is_a in values, (
                f"{enum_name}.{key} has is_a={value.is_a!r}, which is not a "
                "permissible value of the same enum"
            )
        assert value.description, f"{enum_name}.{key} has no description"


def test_ilo_hierarchy_matches_the_published_list() -> None:
    """The 2010 revision has 4 sections, 8 subsections and 106 items."""
    enum_def = _load_enum("ilo_occupational_diseases", "ILOOccupationalDiseaseEnum")
    values = enum_def["permissible_values"]
    roots = [k for k, v in values.items() if not (v or {}).get("is_a")]
    assert len(roots) == 4, f"expected the 4 ILO sections as roots, got {roots}"

    parents = {(v or {}).get("is_a") for v in values.values()}
    subsections = [k for k, v in values.items() if (v or {}).get("is_a") in roots]
    # Section 4 carries its two items directly, with no intervening subsection,
    # so "children of a root" is subsections plus those two items.
    assert len(subsections) == 10
    assert len(values) == 118, "4 sections + 8 subsections + 106 items"

    # Every leaf must be reachable from a section.
    leaves = [k for k in values if k not in parents]
    assert len(leaves) == 106


def test_eu_schedule_has_two_annexes_and_flags_suspected_values() -> None:
    """Annex II values must be distinguishable from recognised Annex I ones."""
    enum_def = _load_enum("eu_occupational_schedule", "EUOccupationalScheduleEnum")
    values = enum_def["permissible_values"]

    roots = sorted(k for k, v in values.items() if not (v or {}).get("is_a"))
    assert roots == ["annex_i", "annex_ii"]

    def annex_of(key: str) -> str:
        while parent := (values[key] or {}).get("is_a"):
            key = parent
        return key

    # Chapter nodes are self-labelling (`annex_ii_*`); the assignable leaf items
    # are the ones that must never be mistaken for recognised diseases.
    for key, value in values.items():
        if key in roots:
            continue
        is_chapter = (value or {}).get("is_a") in roots
        if annex_of(key) == "annex_ii":
            assert key.startswith("annex_ii_" if is_chapter else "suspected_"), (
                f"{key} sits under Annex II (suspected occupational origin) but "
                "its key does not say so, so it reads as a recognised "
                "occupational disease"
            )
        else:
            assert not key.startswith("suspected_"), (
                f"{key} is an Annex I (recognised) item but is prefixed 'suspected_'"
            )


def test_eu_schedule_excludes_the_deleted_annex_ii_laryngeal_cancer() -> None:
    """Annex II item 2.308 was removed by Rec. (EU) 2025/2609.

    It was promoted into Annex I as item 311 (cancer of the larynx caused by
    asbestos). Carrying both would let a curator record the same disease as
    simultaneously recognised and merely suspected.
    """
    enum_def = _load_enum("eu_occupational_schedule", "EUOccupationalScheduleEnum")
    values = enum_def["permissible_values"]

    descriptions = " ".join(
        (value or {}).get("description", "") for value in values.values()
    )
    assert "item 2.308" not in descriptions
    assert "laryngeal_cancer_from_asbestos" in values
    assert "item 311" in (values["laryngeal_cancer_from_asbestos"] or {})["description"]


@pytest.mark.parametrize(
    "module_stem,enum_name,prefix",
    [
        ("ilo_occupational_diseases", "ILOOccupationalDiseaseEnum", "ILO item "),
        ("eu_occupational_schedule", "EUOccupationalScheduleEnum", "EU schedule item "),
    ],
)
def test_no_heading_bleed_in_item_descriptions(
    module_stem: str, enum_name: str, prefix: str
) -> None:
    """Item text must not have absorbed a neighbouring section heading.

    Both lists were transcribed from the published instruments, and the EU one
    was extracted mechanically from the consolidated EUR-Lex text. The failure
    mode that survives a schema check is an item whose description has run on
    into the next heading (item 508 originally swallowed the whole "ANNEX II
    Additional list of diseases suspected of being occupational in origin…"
    banner), which silently misstates what the item covers.
    """
    values = _load_enum(module_stem, enum_name)["permissible_values"]
    banners = (
        "ANNEX",
        "Additional list of diseases",
        "Occupational diseases by target organ systems",
        "Occupational diseases caused by exposure to agents",
    )
    for key, value in values.items():
        description = " ".join((value or {})["description"].split())
        if prefix not in description:
            continue  # section/chapter node, not an item
        for banner in banners:
            assert banner not in description, (
                f"{enum_name}.{key} description appears to have absorbed the "
                f"{banner!r} heading: {description[:160]}"
            )


def test_ilo_item_numbering_is_complete_and_gapless() -> None:
    """The ILO list is numbered contiguously; a gap means a dropped item."""
    values = _load_enum("ilo_occupational_diseases", "ILOOccupationalDiseaseEnum")[
        "permissible_values"
    ]

    numbers: list[str] = []
    for value in values.values():
        description = " ".join((value or {})["description"].split())
        # Open items read "ILO item 1.1.41 (open item): …", so the number is not
        # always followed directly by the colon.
        match = re.match(r"ILO item (\d+(?:\.\d+)*)", description)
        if match:
            numbers.append(match.group(1))

    expected = {
        "1.1": 41,
        "1.2": 7,
        "1.3": 9,
        "2.1": 12,
        "2.2": 4,
        "2.3": 8,
        "2.4": 2,
        "3.1": 21,
    }
    for subsection, count in expected.items():
        found = sorted(
            int(n.rsplit(".", 1)[1])
            for n in numbers
            if n.rsplit(".", 1)[0] == subsection
        )
        assert found == list(range(1, count + 1)), (
            f"ILO subsection {subsection} should hold items 1..{count}, got {found}"
        )

    # Section 4 numbers its two items directly, with no subsection level.
    assert sorted(n for n in numbers if n.startswith("4.")) == ["4.1", "4.2"]
    assert len(numbers) == 106


def test_iarc_group_4_is_deprecated_not_removed() -> None:
    """Group 4 was withdrawn in 2019 but must stay resolvable."""
    enum_def = _load_enum("exposure_classification", "IARCCarcinogenGroupEnum")
    group_4 = enum_def["permissible_values"]["GROUP_4"]
    assert group_4.get("deprecated"), "GROUP_4 must be marked deprecated"
    # No replacement exists: the category was dissolved, not renamed.
    assert "deprecated_element_has_possible_replacement" not in group_4

    for still_current in ("GROUP_1", "GROUP_2A", "GROUP_2B", "GROUP_3"):
        assert not enum_def["permissible_values"][still_current].get("deprecated")


def test_worked_examples_carry_both_classification_families() -> None:
    """The exemplars must demonstrate the disease/agent split, not just one side."""
    silicosis = yaml.safe_load(Path("kb/disorders/Silicosis.yaml").read_text())

    classifications = silicosis["classifications"]
    assert classifications["ilo_occupational_category"]
    assert classifications["eu_occupational_category"]

    exposure = silicosis["environmental"][0]["exposure_classifications"]
    assert exposure["iarc_carcinogen_group"]["classification_value"] == "GROUP_1"
    assert {item["classification_value"] for item in exposure["exposure_route"]} == {
        "INHALATION"
    }


def test_asbestos_exemplars_use_orthogonal_ilo_sections() -> None:
    """Same exposure, different ILO section — the point of the multivalued slot.

    Asbestosis is a section 2 (target organ system) item; mesothelioma from the
    same asbestos exposure is a section 3 (occupational cancer) item.
    """
    asbestosis = yaml.safe_load(Path("kb/disorders/Asbestosis.yaml").read_text())
    mesothelioma = yaml.safe_load(
        Path("kb/disorders/Malignant_Mesothelioma.yaml").read_text()
    )

    asbestosis_items = {
        item["classification_value"]
        for item in asbestosis["classifications"]["ilo_occupational_category"]
    }
    mesothelioma_items = {
        item["classification_value"]
        for item in mesothelioma["classifications"]["ilo_occupational_category"]
    }

    assert asbestosis_items == {"pneumoconiosis_from_fibrogenic_mineral_dust"}
    assert mesothelioma_items == {"cancer_asbestos"}
    assert not asbestosis_items & mesothelioma_items


def test_exposure_classifications_reach_the_rendered_enum_pages(
    tmp_path: Path,
) -> None:
    """Agent-level assignments are nested under environmental[], so they need
    explicit collection to show up as usages on the classification pages."""
    input_dir = tmp_path / "kb" / "disorders"
    output_dir = tmp_path / "pages" / "classifications"
    input_dir.mkdir(parents=True)
    (input_dir / "Benzene_Exposure_Disorder.yaml").write_text(
        yaml.safe_dump(
            {
                "name": "Benzene Exposure Disorder",
                "environmental": [
                    {
                        "name": "Occupational benzene exposure",
                        "exposure_classifications": {
                            "iarc_carcinogen_group": {
                                "classification_value": "GROUP_1"
                            },
                            "exposure_route": [
                                {"classification_value": "INHALATION"},
                                {"classification_value": "DERMAL"},
                            ],
                        },
                    }
                ],
            },
            sort_keys=False,
        )
    )

    render_classification_pages(input_dir=input_dir, output_dir=output_dir)

    iarc_html = (output_dir / "IARCCarcinogenGroupEnum.html").read_text()
    assert "Benzene Exposure Disorder" in iarc_html

    route_html = (output_dir / "ExposureRouteEnum.html").read_text()
    # Both values of the multivalued slot must be picked up, not just the first.
    assert route_html.count("Benzene Exposure Disorder") >= 2


def _load_enum(module_stem: str, enum_name: str) -> dict:
    """Read an enum straight from its classifications/ module.

    Deliberately bypasses SchemaView: these assertions are about what the
    committed source file says (deprecation metadata, hierarchy shape), which
    is what a reviewer reads.
    """
    data = yaml.safe_load((CLASSIFICATIONS_DIR / f"{module_stem}.yaml").read_text())
    return data["enums"][enum_name]
