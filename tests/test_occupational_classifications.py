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
    "ILOCausativeAgentEnum": "ilo_agent_category",
    "ILODiseaseCategoryEnum": "ilo_disease_category",
    "EUOccupationalScheduleEnum": "eu_occupational_category",
}

# The ILO list is biaxial; each axis gets its own enum so that a slot cannot
# accept a value from the other axis. These are the section roots per axis.
ILO_AXES = {
    "ILOCausativeAgentEnum": {
        "subset": "ilo_causative_agent_axis",
        "roots": {"caused_by_agents_arising_from_work", "occupational_cancer"},
    },
    "ILODiseaseCategoryEnum": {
        "subset": "ilo_disease_category_axis",
        "roots": {"by_target_organ_system", "other_diseases"},
    },
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
    """Across both axis enums: 4 sections, 8 subsections, 106 items."""
    all_values: dict = {}
    for enum_name, axis in ILO_AXES.items():
        values = _load_enum("ilo_occupational_diseases", enum_name)[
            "permissible_values"
        ]
        roots = {k for k, v in values.items() if not (v or {}).get("is_a")}
        assert roots == axis["roots"], (
            f"{enum_name} should be rooted at {axis['roots']}, got {roots}"
        )
        overlap = set(values) & set(all_values)
        assert not overlap, (
            f"{enum_name} shares permissible values with the other ILO axis: "
            f"{overlap}. Each item belongs to exactly one axis."
        )
        all_values.update(values)

    parents = {(v or {}).get("is_a") for v in all_values.values()}
    roots = {k for k, v in all_values.items() if not (v or {}).get("is_a")}
    assert len(roots) == 4, f"expected the 4 ILO sections as roots, got {roots}"
    # Section 4 carries its two items directly, with no intervening subsection,
    # so "children of a root" is the 8 subsections plus those two items.
    assert (
        len([k for k, v in all_values.items() if (v or {}).get("is_a") in roots]) == 10
    )
    assert len(all_values) == 118, "4 sections + 8 subsections + 106 items"
    assert len([k for k in all_values if k not in parents]) == 106


@pytest.mark.parametrize("enum_name", list(ILO_AXES))
def test_ilo_axis_enums_declare_their_subset(
    schema_view: SchemaView, enum_name: str
) -> None:
    """The axis must be machine-readable, not just implied by the enum name."""
    enum_def = schema_view.get_enum(enum_name)
    assert list(enum_def.in_subset) == [ILO_AXES[enum_name]["subset"]]
    assert ILO_AXES[enum_name]["subset"] in schema_view.all_subsets()


def test_ilo_slots_share_a_presentational_slot_group(schema_view: SchemaView) -> None:
    """slot_group is non-semantic in LinkML, so it must not be the only thing
    separating the axes - the separate enum ranges are what enforce that."""
    grouping = schema_view.get_slot("occupational_classification")
    assert grouping is not None
    assert grouping.is_grouping_slot is True

    members = ["ilo_agent_category", "ilo_disease_category", "eu_occupational_category"]
    for slot_name in members:
        assert (
            schema_view.get_slot(slot_name).slot_group == "occupational_classification"
        )

    # The real guard: the two ILO slots range over DIFFERENT enums.
    ranges = {
        schema_view.get_class(schema_view.get_slot(s).range)
        .slot_usage["classification_value"]
        .range
        for s in ("ilo_agent_category", "ilo_disease_category")
    }
    assert ranges == {"ILOCausativeAgentEnum", "ILODiseaseCategoryEnum"}


@pytest.mark.parametrize(
    "enum_name,expected_source",
    [
        ("EUOccupationalScheduleEnum", "http://data.europa.eu/eli/reco/2025/2609/oj"),
        ("ExposomeDomainEnum", "PMID:22296988"),
        (
            "IARCCarcinogenGroupEnum",
            "https://monographs.iarc.who.int/iarc-monographs-preamble-preamble-to-the-iarc-monographs/",
        ),
    ],
)
def test_provenance_lives_in_source_not_only_prose(
    schema_view: SchemaView, enum_name: str, expected_source: str
) -> None:
    """Citations belong in the ``source`` metaslot, not buried in description text."""
    assert schema_view.get_enum(enum_name).source == expected_source


def test_eu_amendment_items_carry_their_own_source() -> None:
    """Per-value ``source`` marks items added after the 2003 base schedule.

    A value having its own source is the signal that it is an amendment
    addition; everything else inherits the enum-level consolidated source.
    """
    values = _load_enum("eu_occupational_schedule", "EUOccupationalScheduleEnum")[
        "permissible_values"
    ]
    sourced = {
        k: (v or {})["source"] for k, v in values.items() if (v or {}).get("source")
    }

    covid = "http://data.europa.eu/eli/reco/2022/2337/oj"
    asbestos = "http://data.europa.eu/eli/reco/2025/2609/oj"
    assert sourced == {
        "covid_19": covid,
        "laryngeal_cancer_from_asbestos": asbestos,
        "ovarian_cancer_from_asbestos": asbestos,
        "asbestos_pleural_plaques_with_impairment": asbestos,
        "asbestos_non_malignant_pleural_effusion": asbestos,
        "suspected_colon_cancer_from_asbestos": asbestos,
        "suspected_rectal_cancer_from_asbestos": asbestos,
        "suspected_stomach_cancer_from_asbestos": asbestos,
    }


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
        ("ilo_occupational_diseases", "ILOCausativeAgentEnum", "ILO item "),
        ("ilo_occupational_diseases", "ILODiseaseCategoryEnum", "ILO item "),
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
    """The ILO list is numbered contiguously; a gap means a dropped item.

    Numbering is checked across BOTH axis enums together, because the split puts
    items 1.x/3.x in one enum and 2.x/4.x in the other — a gap would otherwise
    hide as "that item lives in the other enum".
    """
    values: dict = {}
    for enum_name in ILO_AXES:
        values.update(
            _load_enum("ilo_occupational_diseases", enum_name)["permissible_values"]
        )

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
    # Both silicosis items are section 2, i.e. the disease-category axis.
    assert classifications["ilo_disease_category"]
    assert "ilo_agent_category" not in classifications
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

    # Asbestosis sits on the disease-category axis (section 2); mesothelioma from
    # the same exposure sits on the causative-agent axis (section 3). The split
    # slots make that orthogonality visible in the data, not just in prose.
    asbestosis_items = {
        item["classification_value"]
        for item in asbestosis["classifications"]["ilo_disease_category"]
    }
    mesothelioma_items = {
        item["classification_value"]
        for item in mesothelioma["classifications"]["ilo_agent_category"]
    }

    assert asbestosis_items == {"pneumoconiosis_from_fibrogenic_mineral_dust"}
    assert mesothelioma_items == {"cancer_asbestos"}
    assert "ilo_agent_category" not in asbestosis["classifications"]
    assert "ilo_disease_category" not in mesothelioma["classifications"]


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


def test_every_disease_classification_slot_is_renderable() -> None:
    """The Classifications card is driven by the schema, not a hardcoded list.

    Regression guard: the template used to enumerate classification slots by
    hand, and had silently drifted — ``icimd_category`` (74 entries),
    ``isds_skeletal_category`` (168) and ``nih_research_priority`` (16) were
    curated but rendered nowhere. Anything in ``DiseaseClassifications`` must
    appear in the display spec, and must carry a human label.
    """
    from dismech.render import _classification_display_spec, _load_schema

    schema = _load_schema()
    declared = (schema["classes"]["DiseaseClassifications"])["slots"]
    spec = _classification_display_spec(schema)

    rendered = [m["slot"] for group in spec for m in group["members"]]
    assert sorted(rendered) == sorted(declared), (
        "every DiseaseClassifications slot must be in the render spec; "
        f"missing={sorted(set(declared) - set(rendered))}"
    )

    for group in spec:
        assert group["label"], "a classification group has no label"
        for member in group["members"]:
            label = member["label"]
            assert label and label != member["slot"], (
                f"{member['slot']} needs a LinkML `title` for its display label; "
                f"got {label!r}"
            )


def test_classification_spec_nests_by_slot_group() -> None:
    """slot_group's one legitimate job is presentation — use it for that."""
    from dismech.render import _classification_display_spec

    spec = _classification_display_spec()
    by_label = {group["label"]: group for group in spec}

    occupational = by_label["Occupational Disease"]
    assert [m["slot"] for m in occupational["members"]] == [
        "ilo_agent_category",
        "ilo_disease_category",
        "eu_occupational_category",
    ]

    # Ungrouped slots stand alone, one member each, labelled by their own title.
    harrisons = by_label["Harrison's Part"]
    assert [m["slot"] for m in harrisons["members"]] == ["harrisons_chapter"]


def _load_enum(module_stem: str, enum_name: str) -> dict:
    """Read an enum straight from its classifications/ module.

    Deliberately bypasses SchemaView: these assertions are about what the
    committed source file says (deprecation metadata, hierarchy shape), which
    is what a reviewer reads.
    """
    data = yaml.safe_load((CLASSIFICATIONS_DIR / f"{module_stem}.yaml").read_text())
    return data["enums"][enum_name]
