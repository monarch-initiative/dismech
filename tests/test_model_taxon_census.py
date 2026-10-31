"""The census's two joins, which an alternative-model research prompt quotes.

`just alternative-models-research` sends a provider a table of this entry's
pathograph nodes marked "already modelled" or not, and tells it the unmodelled
ones are the point of the exercise. So a wrong "no" spends a run on a node that
is already covered, and a wrong clade makes a mammal-only entry look diverse.
Both figures are computed, not written down, and nothing else checks them.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import model_taxon_census as census


@pytest.mark.parametrize(
    ("species", "clade"),
    [
        ("Mouse (Mus musculus)", "mammal"),
        ("mouse", "mammal"),
        ("Zebrafish (Danio rerio)", "fish"),
        ("Drosophila melanogaster", "invertebrate"),
        ("Xenopus laevis", "amphibian"),
        # Two species in one string: counted once, under the first clade the
        # ordered CLADES table matches, which is why MAMMAL comes first.
        ("Mouse and Drosophila melanogaster", "mammal"),
        ("", "unclassified"),
        ("Tardigrade", "unclassified"),
    ],
)
def test_classify_reads_a_free_text_species_string(species: str, clade: str) -> None:
    assert census.classify(species) == clade


def test_an_unmatched_species_string_is_reported_rather_than_bucketed() -> None:
    """`--unclassified` can only list what `scan_entry` kept, so it keeps the string."""
    row = census.scan_entry(
        Path("kb/disorders/Fake.yaml"),
        {"animal_models": [{"name": "m", "species": "Tardigrade"}]},
    )

    assert row["unclassified"] == ["Tardigrade"]
    assert row["mammal_only"] is False


ENTRY = {
    "pathophysiology": [
        {"name": "Modelled In A Mouse", "biological_scale": "ORGANISM"},
        {"name": "Modelled In An Organoid", "biological_scale": "TISSUE"},
        {"name": "Modelled Nowhere", "biological_scale": "MOLECULAR"},
        {"name": "Scale Not Stated"},
    ],
    "animal_models": [
        {
            "name": "Some knockout",
            "species": "Mouse (Mus musculus)",
            "modeled_mechanisms": [{"target": "Modelled In A Mouse"}],
        }
    ],
    "experimental_models": [
        {
            "name": "Some organoid",
            "experimental_model_type": "ORGANOID",
            "modeled_mechanisms": [{"target": "Modelled In An Organoid"}],
        }
    ],
    "discussions": [
        {
            "proposed_experiments": [
                {
                    "model_systems": [
                        {
                            "name": "A model nobody has built",
                            "modeled_mechanisms": [{"target": "Modelled Nowhere"}],
                        }
                    ]
                }
            ]
        }
    ],
}


def test_a_node_modelled_by_an_experimental_model_counts_as_modelled() -> None:
    """The link has four homes; reading only `animal_models` marks three as unmodelled."""
    table = census.render_mechanism_nodes(ENTRY)

    assert "| Modelled In An Organoid | TISSUE | yes (experimental_models) |" in table
    assert "| Modelled In A Mouse | ORGANISM | yes (animal_models) |" in table


def test_a_model_that_only_exists_in_a_proposed_experiment_does_not_count() -> None:
    """The prompt asks what models exist, not what someone suggested building."""
    table = census.render_mechanism_nodes(ENTRY)

    assert "| Modelled Nowhere | MOLECULAR | **no** |" in table


def test_an_unstated_scale_is_marked_rather_than_left_blank() -> None:
    table = census.render_mechanism_nodes(ENTRY)

    assert "| Scale Not Stated | **not stated** | **no** |" in table


def test_existing_models_names_an_experimental_model_by_its_schema_slot() -> None:
    """The slot is `experimental_model_type`; reading `model_type` renders every one
    of the 600-odd entries that have one as "type not stated"."""
    block = census.render_existing_models(ENTRY)

    assert "- **Some organoid** (ORGANOID)" in block
    assert "type not stated" not in block
    assert "linked to: Modelled In An Organoid" in block


def test_clades_stay_an_animal_model_count() -> None:
    """Only AnimalModel carries `species`, so an organoid must not become a clade."""
    row = census.scan_entry(Path("kb/disorders/Fake.yaml"), ENTRY)

    assert row["n_models"] == 1
    assert dict(row["clades"]) == {"mammal": 1}
    assert row["mammal_only"] is True
    # The node join, by contrast, spans the blocks.
    assert row["linked_nodes"] == {"Modelled In A Mouse", "Modelled In An Organoid"}
    assert row["unlinked_nodes"] == ["Modelled Nowhere", "Scale Not Stated"]


def test_an_entry_with_no_models_is_not_mammal_only() -> None:
    row = census.scan_entry(Path("kb/disorders/Empty.yaml"), {"pathophysiology": []})

    assert row["mammal_only"] is False
    assert row["linked_nodes"] == set()
