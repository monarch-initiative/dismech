"""Tests for the pathograph -> synthetic-patient bridge.

Covers the prior exporter (``dismech.export.synthvae_export``), the sampler
(``scripts/synthvae_sampler.py``) and the QC layer (``scripts/synthvae_qc.py``).
"""
from __future__ import annotations

import importlib.util
import json
import random
from pathlib import Path

import yaml

from dismech.export import synthvae_export as sx

_SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"


def _load_script(name: str):
    spec = importlib.util.spec_from_file_location(name, _SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[union-attr]
    return module


sampler = _load_script("synthvae_sampler")
qc = _load_script("synthvae_qc")


def _write(path: Path, obj) -> None:
    path.write_text(yaml.safe_dump(obj, sort_keys=False))


def _graph(branch: str, phenotype: str, hp: str, *, unconnected: tuple[str, str] | None = None):
    nodes = [
        {"id": branch, "node_type": "pathophysiology"},
        {"id": phenotype, "node_type": "phenotype", "meta": {"term_id": hp}},
    ]
    if unconnected:
        nodes.append(
            {"id": unconnected[0], "node_type": "phenotype", "meta": {"term_id": unconnected[1]}}
        )
    return {
        "nodes": nodes,
        "edges": [{"source": branch, "target": phenotype, "predicate": "causes"}],
    }


def _shared_mondo_kb(tmp_path: Path) -> tuple[Path, Path]:
    """Two entries bound to one MONDO id, each with its own pathograph file."""
    kb = tmp_path / "disorders"
    pg = tmp_path / "pathographs"
    kb.mkdir()
    pg.mkdir()
    for name, hp in (("Alpha Cancer", "HP:0000001"), ("Beta Cancer", "HP:0000002")):
        _write(
            kb / f"{name.replace(' ', '_')}.yaml",
            {
                "name": name,
                "disease_term": {"term": {"id": "MONDO:0001056", "label": "gastric cancer"}},
                "phenotypes": [
                    {
                        "name": f"{name} sign",
                        "frequency": "VERY_FREQUENT",
                        "phenotype_term": {"term": {"id": hp, "label": f"{name} sign"}},
                    }
                ],
            },
        )
    (pg / "MONDO_0001056.json").write_text(
        json.dumps(_graph("Alpha Branch", "Alpha Cancer sign", "HP:0000001"))
    )
    (pg / "MONDO_0001056__Beta_Cancer.json").write_text(
        json.dumps(_graph("Beta Branch", "Beta Cancer sign", "HP:0000002"))
    )
    (pg / "index.json").write_text(
        json.dumps(
            {
                "MONDO:0001056": [
                    {"file": "MONDO_0001056.json", "name": "Alpha Cancer", "slug": "Alpha_Cancer"},
                    {
                        "file": "MONDO_0001056__Beta_Cancer.json",
                        "name": "Beta Cancer",
                        "slug": "Beta_Cancer",
                    },
                ]
            }
        )
    )
    return kb, pg


# --- exporter ---------------------------------------------------------------


def test_frequency_to_probability_sources() -> None:
    assert sx.frequency_to_probability({"frequency": "FREQUENT"}) == (0.55, "band")
    assert sx.frequency_to_probability({"description": "seen in 12% of cases"}) == (
        0.12,
        "literal",
    )
    assert sx.frequency_to_probability({"description": "3/20 patients"}) == (0.15, "literal")
    assert sx.frequency_to_probability({}) == (None, "unknown")


def test_entries_sharing_a_mondo_id_each_get_their_own_pathograph(tmp_path: Path) -> None:
    kb, pg = _shared_mondo_kb(tmp_path)
    alpha = sx.disease_prior(kb / "Alpha_Cancer.yaml", pg)
    beta = sx.disease_prior(kb / "Beta_Cancer.yaml", pg)

    assert alpha["pathograph"] == "MONDO_0001056.json"
    assert beta["pathograph"] == "MONDO_0001056__Beta_Cancer.json"
    assert alpha["phenotypes"][0]["branch"] == "Alpha Branch"
    # The second entry must read its own graph, not the plain MONDO file.
    assert beta["phenotypes"][0]["branch"] == "Beta Branch"


def test_without_an_index_a_shared_mondo_id_is_not_guessed(tmp_path: Path) -> None:
    _, pg = _shared_mondo_kb(tmp_path)
    (pg / "index.json").unlink()
    assert sx.resolve_pathograph("MONDO:0001056", "Beta Cancer", pg) is None


def test_only_causative_genes_are_recorded_with_subtype_and_case_fraction(
    tmp_path: Path,
) -> None:
    path = tmp_path / "X.yaml"
    _write(
        path,
        {
            "name": "X Syndrome",
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "x"}},
            "has_subtypes": [{"name": "Type 1"}, {"name": "Type 2"}],
            "genetic": [
                {
                    "name": "GENEA",
                    "relationship_type": "CAUSATIVE",
                    "subtype": "Type 1",
                    "case_fractions": [{"case_fraction_percent": 70}],
                    "gene_term": {"term": {"id": "hgnc:1", "label": "GENEA"}},
                },
                {
                    "name": "GENEB",
                    "relationship_type": "MODIFIER",
                    "gene_term": {"term": {"id": "hgnc:2", "label": "GENEB"}},
                },
            ],
            "pathophysiology": [
                {"name": "Node", "genes": [{"term": {"id": "hgnc:3", "label": "GENEC"}}]}
            ],
            "phenotypes": [
                {
                    "name": "Sign",
                    "subtype": "Type 2",
                    "phenotype_term": {"term": {"id": "HP:0000003", "label": "Sign"}},
                }
            ],
        },
    )
    prior = sx.disease_prior(path, tmp_path / "no-pathographs")
    assert prior["genes"] == [
        {
            "id": "hgnc:1",
            "label": "GENEA",
            "relationship_type": "CAUSATIVE",
            "subtype": "Type 1",
            "case_fraction": 0.7,
        }
    ]
    assert prior["phenotypes"][0]["subtype"] == "Type 2"
    assert prior["phenotypes"][0]["branch"] is None
    assert prior["subtypes"] == ["Type 1", "Type 2"]


def test_untyped_genes_are_used_only_when_no_row_is_causative(tmp_path: Path) -> None:
    path = tmp_path / "Y.yaml"
    _write(
        path,
        {
            "name": "Y Syndrome",
            "disease_term": {"term": {"id": "MONDO:0000002", "label": "y"}},
            "genetic": [
                {"name": "GENEA", "gene_term": {"term": {"id": "hgnc:1", "label": "GENEA"}}},
                {
                    "name": "GENEB",
                    "relationship_type": "SUSCEPTIBILITY",
                    "gene_term": {"term": {"id": "hgnc:2", "label": "GENEB"}},
                },
            ],
            "phenotypes": [
                {"name": "Sign", "phenotype_term": {"term": {"id": "HP:0000003", "label": "S"}}}
            ],
        },
    )
    genes = sx.disease_prior(path, tmp_path)["genes"]
    assert [(g["id"], g["relationship_type"]) for g in genes] == [("hgnc:1", None)]


# --- sampler ----------------------------------------------------------------


def _prior(**overrides):
    prior = {
        "disease_id": "MONDO:0000001",
        "disease_name": "x",
        "dismech_name": "X Syndrome",
        "pathograph": "MONDO_0000001.json",
        "subtypes": [],
        "genes": [],
        "phenotypes": [
            {"hpo_id": "HP:0000010", "label": "a", "probability": 0.1, "branch": "B"},
            {"hpo_id": "HP:0000011", "label": "b", "probability": 0.2, "branch": "B"},
            {"hpo_id": "HP:0000012", "label": "c", "probability": 0.15, "branch": None},
        ],
    }
    prior.update(overrides)
    return prior


def test_branch_mode_keeps_marginals_with_default_min_features() -> None:
    n = 20000
    patients = sampler.generate([_prior()], n, "branch", seed=1, disease_filter=None,
                                min_features=0)
    assert len(patients) == n
    counts = {"HP:0000010": 0, "HP:0000011": 0, "HP:0000012": 0}
    both = 0
    for pkt in patients:
        ids = {f["type"]["id"] for f in pkt["phenotypicFeatures"]}
        for hp in counts:
            counts[hp] += hp in ids
        both += {"HP:0000010", "HP:0000011"} <= ids
    for hp, p in (("HP:0000010", 0.1), ("HP:0000011", 0.2), ("HP:0000012", 0.15)):
        assert abs(counts[hp] / n - p) < 0.015
    # Same-branch phenotypes co-occur: the rarer one always comes with the other.
    assert both == counts["HP:0000010"]


def test_min_features_conditions_the_marginals_upward() -> None:
    n = 5000
    kept = sampler.generate([_prior()], n, "branch", seed=2, disease_filter=None,
                            min_features=1)
    rate = sum(
        any(f["type"]["id"] == "HP:0000011" for f in pkt["phenotypicFeatures"]) for pkt in kept
    ) / len(kept)
    assert rate > 0.3  # well above the curated 0.2


def test_one_gene_and_one_subtype_per_patient() -> None:
    prior = _prior(
        subtypes=["Type 1", "Type 2"],
        genes=[
            {"id": "hgnc:1", "label": "GENEA", "subtype": "Type 1", "case_fraction": None},
            {"id": "hgnc:2", "label": "GENEB", "subtype": "Type 2", "case_fraction": None},
        ],
        phenotypes=[
            {"hpo_id": "HP:0000020", "label": "t1", "probability": 1.0, "branch": None,
             "subtype": "Type 1"},
            {"hpo_id": "HP:0000021", "label": "t2", "probability": 1.0, "branch": None,
             "subtype": "Type 2"},
        ],
    )
    patients = sampler.generate([prior], 200, "branch", seed=3, disease_filter=None,
                                min_features=0)
    seen_genes = set()
    for pkt in patients:
        gis = pkt["interpretations"][0]["diagnosis"]["genomicInterpretations"]
        assert len(gis) == 1
        gi = gis[0]
        assert gi["interpretationStatus"] == "CAUSATIVE"
        gene = gi["gene"]["valueId"]
        assert gene.startswith("HGNC:")
        seen_genes.add(gene)
        ids = {f["type"]["id"] for f in pkt["phenotypicFeatures"]}
        # Never both subtypes' features, and always the gene's own subtype.
        expected = "HP:0000020" if gene == "HGNC:1" else "HP:0000021"
        assert ids == {expected}
    assert seen_genes == {"HGNC:1", "HGNC:2"}


def test_case_fractions_weight_the_gene_draw() -> None:
    genes = [
        {"id": "hgnc:1", "label": "A", "subtype": None, "case_fraction": 0.9},
        {"id": "hgnc:2", "label": "B", "subtype": None, "case_fraction": 0.1},
    ]
    rng = random.Random(4)
    draws = [sampler.sample_gene_and_subtype(_prior(genes=genes), rng)[0]["id"]
             for _ in range(2000)]
    assert 0.85 < draws.count("hgnc:1") / len(draws) < 0.95


# --- QC ---------------------------------------------------------------------


def test_qc_separates_causally_connected_from_merely_listed() -> None:
    prior = _prior()
    pkt = {
        "id": "p1",
        "diseases": [{"term": {"id": "MONDO:0000001"}}],
        "phenotypicFeatures": [
            {"type": {"id": "HP:0000010"}},
            {"type": {"id": "HP:0000012"}},
            {"type": {"id": "HP:0009999"}},
        ],
    }
    rec = qc.run([pkt], [prior])["patients"][0]
    assert rec["on_graph"] == ["HP:0000010"]
    assert rec["listed_unconnected"] == ["HP:0000012"]
    assert rec["off_graph"] == ["HP:0009999"]
    assert rec["coverage"] == round(1 / 3, 3)
    assert rec["listed_coverage"] == round(2 / 3, 3)
    assert rec["branches_activated"] == {"B": 1}


def test_qc_resolves_a_shared_mondo_id_only_through_the_named_pathograph() -> None:
    alpha = _prior(dismech_name="Alpha", pathograph="MONDO_0000001.json")
    beta = _prior(dismech_name="Beta", pathograph="MONDO_0000001__Beta.json")
    base = {
        "id": "p",
        "diseases": [{"term": {"id": "MONDO:0000001"}}],
        "phenotypicFeatures": [{"type": {"id": "HP:0000010"}}],
    }
    named = dict(base, metaData={"externalReferences": [
        {"id": "MONDO_0000001__Beta.json", "description": "dismech pathograph"}
    ]})
    report = qc.run([base, named], [alpha, beta])["patients"]
    assert report[0]["match_basis"] == "mondo_ambiguous"
    assert report[0]["matched_disease"] is None
    assert report[1]["match_basis"] == "mondo"
    assert report[1]["matched_name"] == "Beta"


def test_sampler_output_round_trips_through_qc(tmp_path: Path) -> None:
    kb, pg = _shared_mondo_kb(tmp_path)
    priors = [sx.disease_prior(kb / f, pg) for f in ("Alpha_Cancer.yaml", "Beta_Cancer.yaml")]
    patients = sampler.generate(priors, 10, "branch", seed=5, disease_filter=None,
                                min_features=0)
    assert len({p["id"] for p in patients}) == 20  # entries never share patient ids
    summary = qc.run(patients, priors)["summary"]
    assert summary["n_matched"] == 20


def test_patients_without_terms_are_left_out_of_the_coverage_mean() -> None:
    base = {"diseases": [{"term": {"id": "MONDO:0000001"}}]}
    full = dict(base, id="full", phenotypicFeatures=[{"type": {"id": "HP:0000010"}}])
    empty = dict(base, id="empty", phenotypicFeatures=[])
    summary = qc.run([full, empty], [_prior()])["summary"]
    assert summary["mean_coverage_matched"] == 1.0
    assert summary["n_matched_without_terms"] == 1
