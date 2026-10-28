"""What an assay or model count gets wrong when it is taken the easy way.

Both inventory scripts exist because a count on one route says nothing about
the others, and both have a failure mode that exits 0 with a plausible number.

``assay_inventory`` must attribute each assay to exactly one of five routes. The
tempting implementation searches the document for any nested ``assays:`` key,
which cannot separate a proposed experiment's own readouts from a model link's
readouts *inside that same experiment* -- so it reports a measurement nobody has
made as one a curated model reports. The seizure entries are the natural
fixture: ``multielectrode array recording`` is the most-used assay name in the
corpus and every use of it is on a proposed experiment.

``model_inventory`` must walk all four homes of a ``ModelMechanismLink``. Walking
only the three top-level sections is the bug dismech#13427 found in two other
places, and it is silent: the script reports zero links for an entry that has
one.

The clustering is the third case. It is offered as a worklist, so it has to be
honest about what string matching can and cannot decide -- a cluster asserts two
names are one assay, and nothing in a name can establish that on its own.
"""

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import assay_inventory
import model_inventory
from assay_inventory import assays_in_entry, clusters, significant_tokens
from model_inventory import links_in_entry, model_name, models_in_entry

# A seizure entry shaped like the real ones: the MEA assay sits on a proposed
# experiment's readout (route 4b), which is where all 25 real uses sit, and the
# entry also has a curated animal model whose own readout carries an assay
# (route 3), which no entry in `kb/` currently fills.
SEIZURE_ENTRY = {
    "name": "Dravet syndrome",
    "pathophysiology": [
        {
            "name": "Neuronal Hyperexcitability",
            "assays": [{"preferred_term": "field potential recording"}],
        }
    ],
    "biochemical": [
        {
            "name": "Serum sodium",
            "assays": [{"preferred_term": "ion-selective electrode"}],
        }
    ],
    "animal_models": [
        {
            "name": "Scn1a+/- mouse",
            "species": "Mouse",
            "modeled_mechanisms": [
                {
                    "target": "Neuronal Hyperexcitability",
                    "relationship": "RECAPITULATES",
                    "fidelity": "MODERATE",
                    "model_scale": "ORGANISM",
                    "limitations": "Background strain modifies seizure threshold.",
                    "readouts": [
                        {
                            "name": "Spontaneous seizure frequency",
                            "target": "Neuronal Hyperexcitability",
                            "assays": [{"preferred_term": "video-EEG monitoring"}],
                        }
                    ],
                    "evidence": [{"reference": "PMID:00000000"}],
                }
            ],
        }
    ],
    "discussions": [
        {
            "kind": "KNOWLEDGE_GAP",
            "proposed_experiments": [
                {
                    "experiment_id": "mea_network_bursting",
                    "assays": [{"preferred_term": "seizure-liability panel"}],
                    "readouts": [
                        {
                            "name": "Network burst frequency",
                            "target": "pathophysiology#Neuronal Hyperexcitability",
                            "assays": [
                                {"preferred_term": "multielectrode array recording"},
                                {"preferred_term": "patch-clamp electrophysiology"},
                            ],
                        }
                    ],
                    # A model system that exists only inside the proposal. The
                    # fourth home of a link, and the one every earlier walk missed.
                    "model_systems": [
                        {
                            "name": "hiPSC-derived cortical neuron culture",
                            "experimental_model_type": "IPSC_DERIVED_MODEL",
                            "modeled_mechanisms": [
                                {
                                    "target": "Neuronal Hyperexcitability",
                                    "relationship": "MEASURES",
                                    "model_scale": "CELLULAR",
                                    "divergences": [
                                        {
                                            "divergence_type": "BOUNDARY_OMISSION",
                                            "description": "No blood-brain barrier.",
                                        }
                                    ],
                                    "readouts": [
                                        {
                                            "target": "Neuronal Hyperexcitability",
                                            "assays": [
                                                {
                                                    "preferred_term": "MEA network bursting",
                                                    "term": {
                                                        "id": "OBI:0000070",
                                                        "label": "assay",
                                                    },
                                                }
                                            ],
                                        }
                                    ],
                                }
                            ],
                        }
                    ],
                    "controls": [
                        {
                            "name": "Isogenic wild-type line",
                            "model_systems": [
                                {
                                    "name": "Isogenic control culture",
                                    "modeled_mechanisms": [
                                        {
                                            "target": "Neuronal Hyperexcitability",
                                            "relationship": "MEASURES",
                                        }
                                    ],
                                }
                            ],
                        }
                    ],
                }
            ],
        }
    ],
}


class TestAssayRoutes:
    def test_every_route_is_found(self):
        found = assays_in_entry(SEIZURE_ENTRY)
        assert len(found) == 7

    def test_each_assay_is_attributed_to_exactly_one_route(self):
        """A generic search for nested `assays:` keys cannot do this."""
        by_name = {a["name"]: a["route"] for a in assays_in_entry(SEIZURE_ENTRY)}
        assert by_name["field potential recording"] == "pathophysiology"
        assert by_name["ion-selective electrode"] == "biochemical"
        assert by_name["video-EEG monitoring"] == "model_link_readout"
        assert by_name["seizure-liability panel"] == "proposed_experiment"
        assert by_name["multielectrode array recording"] == (
            "proposed_experiment_readout"
        )

    def test_a_model_link_inside_a_proposal_is_route_3_not_4b(self):
        """The distinction a key search collapses, and the reason for route 3.

        `MEA network bursting` sits on a model link's readout; the model happens
        to live inside the proposed experiment. The experiment's own readout
        assays are route 4b. Reporting both as 4b would hide the only assays
        that say how a model measured something.
        """
        by_name = {a["name"]: a for a in assays_in_entry(SEIZURE_ENTRY)}
        assert by_name["MEA network bursting"]["route"] == "model_link_readout"
        assert by_name["patch-clamp electrophysiology"]["route"] == (
            "proposed_experiment_readout"
        )

    def test_a_proposed_assay_is_not_counted_as_measured(self):
        """Route 4a and 4b are proposals; 1, 2 and 3 record a measurement."""
        realized = {
            route for route, meta in assay_inventory.ROUTES.items() if meta["realized"]
        }
        assert realized == {"pathophysiology", "biochemical", "model_link_readout"}

    def test_paths_locate_the_assay_exactly(self):
        paths = {a["name"]: a["path"] for a in assays_in_entry(SEIZURE_ENTRY)}
        assert paths["multielectrode array recording"] == (
            "discussions[0].proposed_experiments[0].readouts[0].assays[0]"
        )
        assert paths["MEA network bursting"] == (
            "discussions[0].proposed_experiments[0].model_systems[0]"
            ".modeled_mechanisms[0].readouts[0].assays[0]"
        )

    def test_a_bound_term_is_reported_and_an_unbound_one_is_not_invented(self):
        by_name = {a["name"]: a for a in assays_in_entry(SEIZURE_ENTRY)}
        assert by_name["MEA network bursting"]["curie"] == "OBI:0000070"
        assert by_name["multielectrode array recording"]["curie"] == ""

    def test_an_entry_with_no_assays_yields_nothing(self):
        assert assays_in_entry({"name": "Nothing here"}) == []

    def test_a_malformed_assays_block_does_not_raise(self):
        """Curated YAML is not always the shape the schema asks for."""
        assert assays_in_entry({"pathophysiology": [{"assays": "a string"}]}) == []
        assert assays_in_entry({"biochemical": [None]}) == []


class TestAssayClustering:
    def test_a_generic_word_does_not_make_two_assays_different(self):
        names = {"immunoblot": 3, "immunoblot assay": 3}
        mechanical, _ = clusters(names)
        assert mechanical == [["immunoblot", "immunoblot assay"]]

    def test_punctuation_does_not_either(self):
        names = {"patch-clamp recording": 3, "patch clamp recording": 2}
        mechanical, _ = clusters(names)
        assert len(mechanical) == 1

    def test_a_word_that_could_name_an_assay_is_not_generic(self):
        """`electrophysiology` names an assay on its own, so stripping it would
        merge two real assays. The generic list is short for this reason."""
        assert "electrophysiology" in significant_tokens(
            "patch-clamp electrophysiology"
        )
        assert "imaging" in significant_tokens("live-cell imaging assay")

    def test_a_contained_name_is_a_candidate_not_a_cluster(self):
        """`immunostaining` vs `centrosome immunostaining` is a curator's call.

        One is plausibly the same assay written loosely, and one is plausibly a
        narrower assay. Merging them would assert the first without evidence.
        """
        names = {"immunostaining": 14, "centrosome immunostaining": 1}
        mechanical, candidates = clusters(names)
        assert mechanical == []
        assert candidates == [["immunostaining", "centrosome immunostaining"]]

    def test_one_shared_weak_word_is_not_a_candidate(self):
        """The reason candidates need containment rather than overlap.

        On the real corpus, flagging any shared word yielded ~1,700 groups --
        `cell` alone tied single-cell sequencing to a viability assay -- which
        is noise, not a worklist.
        """
        names = {"single-cell transcriptomic profiling": 23, "cell viability assay": 9}
        _, candidates = clusters(names)
        assert candidates == []

    def test_a_name_made_only_of_generic_words_pairs_with_nothing(self):
        """Caught in review on #15393, latent only because no name triggers it.

        `assay` reduces to an empty token set, and the empty set is a subset of
        every other set -- so without a guard it produced one candidate row per
        name in the corpus, 329 of them, burying every real row. Two
        generic-only names would also have clustered together as mechanical
        variation, asserting `assay` and `readout` are one assay.
        """
        names = {
            "assay": 1,
            "readout": 1,
            "immunostaining": 14,
            "histopathology": 5,
        }
        mechanical, candidates = clusters(names)
        assert mechanical == []
        assert candidates == []

    def test_synonymy_without_shared_words_is_reported_by_neither(self):
        """The limit of the whole approach, pinned so no caller over-reads it.

        These two are arguably one assay. No string comparison can say so, and
        the report must not imply the name list has been deduplicated.
        """
        names = {
            "single-cell transcriptomic profiling": 23,
            "single-cell RNA sequencing": 11,
        }
        mechanical, candidates = clusters(names)
        assert mechanical == []
        assert candidates == []


class TestAssayReportOutputs:
    def test_the_json_output_carries_the_clustering_the_markdown_truncates(self):
        """Caught in review round 2 on #15393.

        The markdown table caps the candidate rows, and its note told the reader
        where to find the rest. There was nowhere: the JSON output dumped
        `collect()`, which holds the assays but none of the clustering, and the
        TSV is one row per assay. The note named an output that did not exist.
        """
        # Counts as the corpus has them: the containing name is the common one,
        # so it sorts first. With equal counts the order falls back to the name.
        names = ["immunostaining"] * 14 + ["centrosome immunostaining"] * 2
        res = {
            "assays": [
                {
                    "route": "pathophysiology",
                    "name": name,
                    "curie": "",
                    "path": "pathophysiology[0].assays[0]",
                    "entry": "E",
                    "file": "f.yaml",
                }
                for name in names
            ]
        }
        summary = assay_inventory.summarize(res)
        assert summary["candidates"] == [
            ["immunostaining", "centrosome immunostaining"]
        ]
        assert summary["total"] == 16
        assert summary["distinct_names"] == 2

    def test_the_markdown_cap_and_its_note_read_from_one_constant(self):
        """Two literals would drift: a note promising 40 beside a table of 25."""
        assert isinstance(assay_inventory.CANDIDATE_ROWS_SHOWN, int)
        source = Path(assay_inventory.__file__).read_text(encoding="utf-8")
        assert "candidates[:CANDIDATE_ROWS_SHOWN]" in source
        assert "candidates[:40]" not in source


class TestModelLinks:
    def test_all_four_homes_of_a_link_are_walked(self):
        """Three of the four was the dismech#13427 bug, and it was silent."""
        links = links_in_entry(SEIZURE_ENTRY)
        assert len(links) == 3
        assert sum(1 for link in links if link["proposed"]) == 2

    def test_a_link_inside_a_proposal_is_marked_proposed(self):
        links = {link["model"]: link for link in links_in_entry(SEIZURE_ENTRY)}
        assert links["Scn1a+/- mouse"]["proposed"] is False
        assert links["hiPSC-derived cortical neuron culture"]["proposed"] is True

    def test_a_control_arm_model_is_reached(self):
        models = {link["model"] for link in links_in_entry(SEIZURE_ENTRY)}
        assert "Isogenic control culture" in models

    def test_an_absent_fidelity_is_empty_rather_than_a_verdict(self):
        """Most links record no scale. Defaulting one would invent a claim."""
        links = {link["model"]: link for link in links_in_entry(SEIZURE_ENTRY)}
        control = links["Isogenic control culture"]
        assert control["fidelity"] == ""
        assert control["model_scale"] == ""
        assert control["limitations"] is False

    def test_curated_only_drops_the_proposed_links(self, tmp_path):
        entry_dir = tmp_path / "kb" / "disorders"
        entry_dir.mkdir(parents=True)
        (entry_dir / "Dravet_syndrome.yaml").write_text(
            yaml.safe_dump(SEIZURE_ENTRY), encoding="utf-8"
        )
        globs = ["kb/disorders/*.yaml"]

        everything = model_inventory.collect(tmp_path, globs, curated_only=False)
        curated = model_inventory.collect(tmp_path, globs, curated_only=True)

        assert len(everything["links"]) == 3
        assert [link["model"] for link in curated["links"]] == ["Scn1a+/- mouse"]

    def test_divergence_types_are_counted_from_the_typed_slot(self):
        links = {link["model"]: link for link in links_in_entry(SEIZURE_ENTRY)}
        hipsc = links["hiPSC-derived cortical neuron culture"]
        assert hipsc["divergence_types"] == ["BOUNDARY_OMISSION"]
        assert hipsc["divergences"] == 1

    def test_models_are_typed_by_their_own_section_slot(self):
        """Each section names a different kind of thing; there is no one slot."""
        models = models_in_entry(SEIZURE_ENTRY)
        assert [m["type_slot"] for m in models] == ["species"]
        assert models[0]["model_type"] == "Mouse"

    def test_a_proposed_model_system_is_not_a_top_level_model(self):
        """It is a link home, not a curated model, so it is not in the census."""
        names = {m["name"] for m in models_in_entry(SEIZURE_ENTRY)}
        assert names == {"Scn1a+/- mouse"}

    def test_an_unnamed_animal_model_falls_back_the_way_renderers_do(self):
        model = {"species": "Mouse", "genotype": "Scn1a+/-"}
        assert model_name(model, "animal_models") == "Scn1a+/- Mouse"
        assert model_name({}, "experimental_models") == "(unnamed)"
