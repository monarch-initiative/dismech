"""The general AOP -> dismech crosswalk, scripts/aop_dismech_crosswalk.py.

Two kinds of test. The first holds the general script to the findings of the
parkinsonism crosswalk (docs/reports/aop-parkinsonism-crosswalk-2026-10-25.md):
read from the aop-wiki-cli cache, the five parkinsonian AOPs give the Key Events
and Key Event Relationships that scripts/aop_parkinsonism_crosswalk.py transcribes,
and with conf/aop_crosswalk/parkinsonism.yaml the general script matches the same
nodes, on the same bases, as that script does on live entries. The second checks
the automatic matching on small synthetic entries.

The cache is the extract in tests/data/aop_crosswalk/, laid out as an aop-wiki-cli
data directory.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "tests" / "data" / "aop_crosswalk"
DATE = "10-03-2026"
PARKINSONIAN_AOPS = ["3", "587", "588", "589", "593"]
RULES_FILE = ROOT / "conf" / "aop_crosswalk" / "parkinsonism.yaml"

# Entries the parkinsonism report found Key Events in; the rules are compared on
# them. A renamed or removed entry is skipped rather than failed.
PARKINSONISM_ENTRIES = [
    "Parkinsons_Disease",
    "Multiple_System_Atrophy",
    "PRKN-Related_Juvenile_Parkinson_Disease",
    "PARK7-Related_Early-Onset_Parkinson_Disease",
    "LRRK2-Related_Parkinson_Disease",
    "Manganism",
    "Infantile_Parkinsonism-Dystonia",
    "FASTKD5-Related_COX_Deficiency",
    "Autosomal_Dominant_Progressive_External_Ophthalmoplegia",
    "Machado_Joseph_Disease",
]


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


crosswalk = _load("aop_dismech_crosswalk", ROOT / "scripts" / "aop_dismech_crosswalk.py")
parkinsonism = _load("aop_parkinsonism_crosswalk", ROOT / "scripts" / "aop_parkinsonism_crosswalk.py")


def cache(kind: str) -> dict:
    return crosswalk.load_cache(DATA_DIR, DATE, kind)


def rules() -> dict[str, dict]:
    return {str(k): v for k, v in yaml.safe_load(RULES_FILE.read_text())["key_events"].items()}


# ---------------------------------------------------------------------------
# Held to the parkinsonism crosswalk.


def test_cache_gives_the_parkinsonism_key_events():
    chosen = crosswalk.select_key_events(cache("events"), cache("aops"), PARKINSONIAN_AOPS, [])
    assert set(chosen) == set(parkinsonism.KES)


def test_cache_gives_the_parkinsonism_kers_with_their_endpoints_and_citations():
    chosen = crosswalk.select_key_events(cache("events"), cache("aops"), PARKINSONIAN_AOPS, [])
    kers = crosswalk.select_kers(cache("kers"), cache("aops"), PARKINSONIAN_AOPS, chosen)
    # The cache names every AOP a KER is in; the parkinsonism script names only these five.
    assert {
        ker: (
            info["upstream"],
            info["downstream"],
            sorted(set(info["aops"]) & set(PARKINSONIAN_AOPS)),
            info["cited"],
        )
        for ker, info in kers.items()
    } == {
        ker: (up, down, sorted(aops), cited)
        for ker, (up, down, aops, cited) in parkinsonism.KERS.items()
    }


def test_rules_file_covers_every_parkinsonism_rule():
    assert set(rules()) == set(parkinsonism.RULES) | {"896"}


@pytest.mark.parametrize("slug", PARKINSONISM_ENTRIES)
def test_rules_reproduce_the_parkinsonism_crosswalk(slug):
    path = ROOT / "kb" / "disorders" / f"{slug}.yaml"
    if not path.exists():
        pytest.skip(f"{slug} is no longer in kb/disorders/")
    record = yaml.safe_load(path.read_text())
    events, aops = cache("events"), cache("aops")
    chosen = crosswalk.select_key_events(events, aops, PARKINSONIAN_AOPS, [])
    key_events = {ke: crosswalk.key_event(events[ke]) for ke in chosen}
    kers = crosswalk.select_kers(cache("kers"), aops, PARKINSONIAN_AOPS, chosen)

    expected = parkinsonism.crosswalk(record, path)
    got = crosswalk.crosswalk(record, path, key_events, kers, rules(), crosswalk.Modules(ROOT))

    assert {
        ke: {name: match["bases"] for name, match in found.items()}
        for ke, found in got["key_events"].items()
    } == expected["key_events"]
    assert got["kers"] == expected["kers"]


def test_ke1543_has_no_components_so_only_its_rules_can_match_it():
    # The report's KE1543 match on GO:0004129 comes from the hand-written rules: the
    # cache gives the Event no components at all.
    ke = crosswalk.key_event(cache("events")["1543"])
    assert ke["term_ids"] == []
    node = {"name": "Cytochrome c oxidase deficiency", "molecular_functions": [_term("GO:0004129")]}
    assert crosswalk.match_automatic(node, ke, crosswalk.Modules(ROOT)) == []
    assert crosswalk.match_rules(node, rules()["1543"]) == ["GO GO:0004129", "name"]


# ---------------------------------------------------------------------------
# Automatic matching.


def _term(curie: str, label: str = "") -> dict:
    return {"preferred_term": label or curie, "term": {"id": curie, "label": label or curie}}


def ke826() -> dict:
    return crosswalk.key_event(cache("events")["826"])


def test_key_event_reads_component_terms_level_and_labels():
    ke = ke826()
    assert ke["level"] == "Cellular"
    assert ke["term_ids"] == ["GO:0002534", "GO:0032980"]
    assert ke["cell_label"] == "keratinocyte"
    assert ke["organ_label"] is None


def test_term_label_and_name_bases(tmp_path):
    node = {
        "name": "Keratinocyte activation and proinflammatory mediator release",
        "biological_scale": "CELLULAR",
        "biological_processes": [_term("GO:0032980", "keratinocyte activation")],
        "cell_types": [_term("CL:0000312", "keratinocyte")],
    }
    assert crosswalk.match_automatic(node, ke826(), crosswalk.Modules(tmp_path)) == [
        "term GO:0032980 (biological_processes)",
        "label keratinocyte (cell_types)",
        "name keratinocytes",
    ]
    assert crosswalk.level_agreement(node, ke826()) == "agrees"


def test_unrelated_node_does_not_match(tmp_path):
    node = {"name": "Epidermal barrier disruption", "biological_scale": "TISSUE"}
    assert crosswalk.match_automatic(node, ke826(), crosswalk.Modules(tmp_path)) == []


def test_conforms_to_basis_reads_the_module_node(tmp_path):
    modules = tmp_path / "kb" / "modules"
    modules.mkdir(parents=True)
    (modules / "skin_inflammation.yaml").write_text(
        yaml.safe_dump({
            "name": "skin_inflammation",
            "pathophysiology": [
                {"name": "Keratinocyte Activation", "biological_processes": [_term("GO:0032980")]}
            ],
        })
    )
    node = {"name": "Epidermal response", "conforms_to": "skin_inflammation#Keratinocyte Activation"}
    assert crosswalk.match_automatic(node, ke826(), crosswalk.Modules(tmp_path)) == [
        "conforms_to skin_inflammation#Keratinocyte Activation (term GO:0032980)"
    ]


def test_level_agreement_maps_organ_to_tissue_and_reports_a_difference():
    ke272 = crosswalk.key_event(cache("events")["272"])
    assert ke272["level"] == "Organ"
    assert crosswalk.level_agreement({"biological_scale": "TISSUE"}, ke272) == "agrees"
    assert crosswalk.level_agreement({"biological_scale": "CELLULAR"}, ke272) == "differs"
    assert crosswalk.level_agreement({}, ke272) == "node has no scale"


def test_phenotype_matches_on_a_component_mp_or_hp_term(tmp_path):
    ke890 = crosswalk.key_event(cache("events")["890"])
    record = {
        "pathophysiology": [],
        "phenotypes": [
            {"name": "Dopaminergic neuron loss", "phenotype_term": _term("MP:0003244")},
            {"name": "Tremor", "phenotype_term": _term("HP:0001337")},
        ],
    }
    matches = crosswalk.match_entry(record, {"890": ke890}, {}, crosswalk.Modules(tmp_path))
    assert matches["890"] == {
        "Dopaminergic neuron loss": {"kind": "phenotype", "bases": ["phenotype MP:0003244"]}
    }


# ---------------------------------------------------------------------------
# The command line.


def _entry(root: Path) -> None:
    disorders = root / "kb" / "disorders"
    disorders.mkdir(parents=True)
    (disorders / "Example_Dermatitis.yaml").write_text(
        yaml.safe_dump({
            "name": "Example Dermatitis",
            "pathophysiology": [
                {
                    "name": "Keratinocyte activation",
                    "biological_scale": "CELLULAR",
                    "biological_processes": [_term("GO:0032980", "keratinocyte activation")],
                    "downstream": [{"target": "Dendritic cell activation"}],
                },
                {
                    "name": "Dendritic cell activation",
                    "biological_scale": "TISSUE",
                    "cell_types": [_term("CL:0000451", "dendritic cell")],
                },
            ],
        })
    )


def test_main_reports_matches_levels_and_ker_coverage(tmp_path, capsys):
    _entry(tmp_path)
    code = crosswalk.main([
        "--data-dir", str(DATA_DIR), "--date", DATE, "--aop", "40",
        "--entry", "Example_Dermatitis", "--root", str(tmp_path), "--format", "json",
    ])
    assert code == 0
    result = json.loads(capsys.readouterr().out)
    entry = result["entries"][0]
    assert set(result["key_events"]) == {"396", "826", "398", "272", "827"}
    assert entry["key_events"]["826"]["Keratinocyte activation"]["level"] == "agrees"
    assert entry["key_events"]["398"]["Dendritic cell activation"] == {
        "kind": "node",
        "bases": ["label dendritic cell (cell_types)", "name dendritic,cells"],
        "scale": "TISSUE",
        "level": "differs",
    }
    assert entry["kers"]["834"] == {
        "status": "direct",
        "edges": [["Keratinocyte activation", "Dendritic cell activation"]],
    }
    assert entry["kers"]["833"] == {"status": "key event absent", "absent": ["396"]}


def test_main_rejects_an_iso_date(tmp_path):
    _entry(tmp_path)
    with pytest.raises(SystemExit, match="MM-DD-YYYY"):
        crosswalk.main([
            "--data-dir", str(DATA_DIR), "--date", "2026-10-03", "--aop", "40",
            "--entry", "Example_Dermatitis", "--root", str(tmp_path),
        ])
