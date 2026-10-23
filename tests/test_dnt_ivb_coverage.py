"""Tests for the DNT in vitro battery coverage report.

Each test here pins a mistake the script has already made once. The two filters
it runs are a substring regex per endpoint and a neural-relevance check, and
both have been wrong in opposite directions: the regex matched a word it only
appeared to contain, and the neural check discarded the single most on-point
node in the corpus. Neither failure was visible in the output, which is why
they are pinned rather than left to review.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).parent.parent
SPEC = importlib.util.spec_from_file_location(
    "dnt_ivb_coverage", ROOT / "scripts" / "dnt_ivb_coverage.py"
)
assert SPEC and SPEC.loader
coverage = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = coverage
SPEC.loader.exec_module(coverage)

ENDPOINTS = {e.term: e for e in coverage.ENDPOINTS}


def _write(kb: Path, kind: str, stem: str, document: dict) -> None:
    directory = kb / kind
    directory.mkdir(parents=True, exist_ok=True)
    (directory / f"{stem}.yaml").write_text(yaml.safe_dump(document), encoding="utf-8")


def _nodes(kb: Path, term: str) -> list:
    return coverage.collect(kb)[term]


def test_the_battery_has_seventeen_distinct_endpoints() -> None:
    """Figure 1 shows 20 boxes; three appear in both versions."""
    assert len(coverage.ENDPOINTS) == 17
    assert len({e.term for e in coverage.ENDPOINTS}) == 17
    both = {e.term for e in coverage.ENDPOINTS if e.version == "v1.0+v2.0"}
    assert both == {"Neurite outgrowth", "Synaptogenesis", "Neural network formation"}


@pytest.mark.parametrize(
    "name",
    [
        "Pattern-Recognition Receptor Priming",
        "Antigenic variation-mediated immune recognition evasion",
        "Impaired COPI cargo recognition",
    ],
)
def test_recognition_does_not_match_learning_and_memory(name: str) -> None:
    """``cognit`` is a substring of *re-cognit-ion*, which pulled in 23 nodes."""
    assert not ENDPOINTS["Learning and memory"].pattern.search(name)


@pytest.mark.parametrize(
    "name",
    ["Cognitive Decline", "Learning and Memory Impairment", "Spatial memory deficit"],
)
def test_real_cognition_still_matches_learning_and_memory(name: str) -> None:
    assert ENDPOINTS["Learning and memory"].pattern.search(name)


def test_nmda_learning_and_memory_node_survives_the_neural_filter(
    tmp_path: Path,
) -> None:
    """The most on-point node for the endpoint, and nothing in it says "neuro".

    Its name, GO labels and file stem carry no neural word, so the filter
    discarded it until neurotransmitter vocabulary was added.
    """
    _write(
        tmp_path,
        "modules",
        "nmda_receptor_hypofunction",
        {
            "name": "NMDA Receptor Hypofunction Module",
            "pathophysiology": [
                {
                    "name": "Learning and Memory Impairment",
                    "biological_processes": [
                        {"term": {"id": "GO:0007612", "label": "learning"}},
                        {"term": {"id": "GO:0007613", "label": "memory"}},
                    ],
                }
            ],
        },
    )
    _write(tmp_path, "disorders", "placeholder", {"name": "Placeholder"})
    nodes = _nodes(tmp_path, "Learning and memory")
    assert [n.node for n in nodes] == ["Learning and Memory Impairment"]


def test_immunological_memory_is_still_excluded(tmp_path: Path) -> None:
    _write(
        tmp_path,
        "disorders",
        "Some_Immunodeficiency",
        {
            "name": "Some Immunodeficiency",
            "pathophysiology": [{"name": "Impaired CD8 T Cell Survival and Memory"}],
        },
    )
    assert _nodes(tmp_path, "Learning and memory") == []


def test_non_neural_progenitors_are_excluded(tmp_path: Path) -> None:
    """Bare ``progenitor`` used to pass the neural filter on its own."""
    _write(
        tmp_path,
        "disorders",
        "Cyclic_Hematopoiesis",
        {
            "name": "Cyclic Hematopoiesis",
            "pathophysiology": [
                {"name": "Apoptosis of Granulocytic Progenitors"},
                {"name": "Cytotoxic Insult to Proliferating Hematopoietic Progenitors"},
            ],
        },
    )
    assert _nodes(tmp_path, "NPC apoptosis") == []
    assert _nodes(tmp_path, "NPC proliferation") == []


def test_neural_progenitors_are_kept(tmp_path: Path) -> None:
    _write(
        tmp_path,
        "disorders",
        "Autosomal_Recessive_Primary_Microcephaly",
        {
            "name": "Autosomal Recessive Primary Microcephaly",
            "pathophysiology": [{"name": "Neural-Progenitor Proliferation Failure"}],
        },
    )
    assert [n.node for n in _nodes(tmp_path, "NPC proliferation")] == [
        "Neural-Progenitor Proliferation Failure"
    ]


def test_repeated_phenotype_names_get_the_renderer_s_suffix(tmp_path: Path) -> None:
    """``render.py`` claims phenotype anchors, so the second one takes ``-2``.

    Twenty-one phenotype names collide this way in the corpus. A link built
    without the suffix resolves to the first card, and ``--check-anchors``
    cannot catch it because the id it looks for does exist.
    """
    _write(
        tmp_path,
        "disorders",
        "Androgen_Insensitivity_Syndrome",
        {
            "name": "Androgen Insensitivity Syndrome",
            "phenotypes": [
                {"name": "Primary amenorrhea"},
                {"name": "Primary amenorrhea"},
                {"name": "Cognitive decline"},
            ],
        },
    )
    document = yaml.safe_load(
        (tmp_path / "disorders" / "Androgen_Insensitivity_Syndrome.yaml").read_text()
    )
    anchors = coverage._anchor_map(document, "disorder")
    assert (
        anchors[("phenotypes", "Primary amenorrhea")] == "phenotype-primary-amenorrhea"
    )
    assert anchors[("phenotypes", "Cognitive decline")] == "phenotype-cognitive-decline"


def test_page_url_uses_the_entry_name_not_the_file_stem(tmp_path: Path) -> None:
    """The two differ for about a sixth of matched entries; the stem 404s."""
    _write(
        tmp_path,
        "disorders",
        "ADCA-DN",
        {
            "name": "Autosomal Dominant Cerebellar Ataxia Deafness and Narcolepsy",
            "pathophysiology": [{"name": "Cognitive decline"}],
        },
    )
    (url,) = [n.url for n in _nodes(tmp_path, "Learning and memory")]
    assert "Autosomal_Dominant_Cerebellar_Ataxia_Deafness_and_Narcolepsy.html" in url
    assert "ADCA-DN.html" not in url
    assert url.endswith("#pathophysiology-cognitive-decline")


def test_module_pages_use_the_file_stem_and_module_anchor_prefix(
    tmp_path: Path,
) -> None:
    _write(
        tmp_path,
        "modules",
        "cns_myelin_failure",
        {
            "name": "CNS Oligodendrocyte and Myelin Failure Module",
            "pathophysiology": [{"name": "Deficient or Unstable CNS Myelin Sheath"}],
        },
    )
    _write(tmp_path, "disorders", "placeholder", {"name": "Placeholder"})
    (url,) = [n.url for n in _nodes(tmp_path, "Myelination")]
    assert "/modules/cns_myelin_failure.html" in url
    assert url.endswith(
        "#module-pathophysiology-deficient-or-unstable-cns-myelin-sheath"
    )
