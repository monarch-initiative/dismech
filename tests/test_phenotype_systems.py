"""Tests for the phenotype-systems dashboard page (src/dismech/phenotype_systems.py)."""

import json
from pathlib import Path

import pytest

from dismech.phenotype_systems import (
    PHENOTYPE_SYSTEMS_BLOCK_END,
    PHENOTYPE_SYSTEMS_BLOCK_START,
    collect_phenotype_systems,
    effective_system_count,
    generate_phenotype_systems_report,
    profile_disorder,
    render_phenotype_systems_page,
)

CATEGORIES = {
    "HP:1": ["Eye"],
    "HP:2": ["Nervous System"],
    "HP:3": ["Musculoskeletal", "Nervous System"],  # an HP term under two branches
    "HP:4": [],  # cached, but outside Phenotypic abnormality
}


def _disorder(name: str, *hp_ids: str, unbound: int = 0) -> dict:
    phenotypes = [
        {"name": f"p{i}", "phenotype_term": {"term": {"id": hp_id}}}
        for i, hp_id in enumerate(hp_ids)
    ]
    phenotypes += [{"name": f"unbound{i}"} for i in range(unbound)]
    return {"name": name, "phenotypes": phenotypes}


@pytest.mark.parametrize(
    "counts, expected",
    [
        ({"Eye": 3}, 1.0),
        ({"Eye": 2, "Ear": 2}, 2.0),
        ({"A": 1, "B": 1, "C": 1, "D": 1}, 4.0),
        ({}, 0.0),
    ],
)
def test_effective_system_count_at_the_bounds(counts: dict, expected: float) -> None:
    assert effective_system_count(counts) == pytest.approx(expected)


def test_effective_system_count_sits_between_one_and_presence_count() -> None:
    counts = {"Nervous System": 40, "Musculoskeletal": 3, "Eye": 1, "Ear": 1}
    effective = effective_system_count(counts)
    assert 1.0 < effective < len(counts)
    assert effective < 2.0  # one system holds 89% of memberships


def test_profile_counts_a_multi_branch_term_once_per_system() -> None:
    profile = profile_disorder(_disorder("Demo", "HP:3"), CATEGORIES)
    assert profile.system_counts == {"Musculoskeletal": 1, "Nervous System": 1}
    assert profile.phenotype_count == 1
    assert profile.multi_system_phenotype_count == 1
    assert profile.system_count == 2
    assert profile.effective_system_count == pytest.approx(2.0)


def test_profile_reports_unbound_and_uncategorized_phenotypes() -> None:
    profile = profile_disorder(_disorder("Demo", "HP:4", "HP:missing", unbound=1), CATEGORIES)
    assert profile.system_counts == {}
    assert profile.phenotype_count == 2
    assert profile.uncategorized_count == 2
    assert profile.unbound_count == 1
    assert profile.dominant_system is None
    assert profile.dominant_share is None
    assert profile.effective_system_count == 0.0
    assert profile.to_record()["dominant_share"] is None


def test_profile_dominant_system_and_share() -> None:
    profile = profile_disorder(_disorder("Demo", "HP:2", "HP:2", "HP:2", "HP:1"), CATEGORIES)
    assert profile.dominant_system == "Nervous System"
    assert profile.dominant_share == pytest.approx(0.75)
    assert profile.slug == "Demo"


def test_profile_handles_missing_phenotypes_section() -> None:
    profile = profile_disorder({"name": "Bare"}, CATEGORIES)
    assert profile.system_counts == {}
    assert profile.phenotype_count == 0


def test_collect_pairs_report_lift_and_jaccard() -> None:
    disorders = [
        _disorder("A", "HP:1"),
        _disorder("B", "HP:1", "HP:2"),
        _disorder("C", "HP:2"),
        _disorder("D", "HP:1", "HP:2"),
    ]
    data = collect_phenotype_systems(disorders, CATEGORIES)

    assert [(s["system"], s["diseases"]) for s in data["systems"]] == [("Eye", 3), ("Nervous System", 3)]
    (pair,) = data["pairs"]
    assert pair["count"] == 2
    # expected under independence = 3 * 3 / 4 = 2.25
    assert pair["lift"] == pytest.approx(2 / 2.25, abs=1e-3)
    assert pair["jaccard"] == pytest.approx(2 / 4)

    combos = data["combinations"]
    assert combos["distinct"] == 3
    assert combos["unique_diseases"] == 2  # {Eye} and {Nervous System} each held by one disease
    assert combos["shared_2_to_4_diseases"] == 2
    assert combos["shared_5_plus_diseases"] == 0
    assert combos["top"][0] == {"systems": ["Eye", "Nervous System"], "diseases": 2}

    assert data["distribution"]["system_count"] == {"0": 0, "1": 2, "2": 2}
    assert data["summary"]["median_system_count"] == 1.5
    assert data["summary"]["unique_combination_percent"] == 50.0
    # diseases are ordered most-spread first, then by name
    assert [d["name"] for d in data["diseases"]] == ["B", "D", "A", "C"]


def test_collect_counts_diseases_with_no_system() -> None:
    data = collect_phenotype_systems([{"name": "Bare"}, _disorder("A", "HP:1")], CATEGORIES)
    assert data["combinations"]["no_system_diseases"] == 1
    assert data["distribution"]["system_count"] == {"0": 1, "1": 1}
    assert data["summary"]["total_memberships"] == 1


def test_collect_on_empty_corpus() -> None:
    data = collect_phenotype_systems([], CATEGORIES)
    assert data["summary"]["total_diseases"] == 0
    assert data["summary"]["median_system_count"] is None
    assert data["pairs"] == []
    assert data["diseases"] == []


def test_render_escapes_disease_names() -> None:
    data = collect_phenotype_systems([_disorder("<b>Bold</b>", "HP:1")], CATEGORIES)
    page = render_phenotype_systems_page(data, "2026-09-13 00:00 UTC")
    assert "&lt;b&gt;Bold&lt;/b&gt;" in page
    assert "<b>Bold</b>" not in page
    assert "Effective systems" in page


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")


def test_generate_report_writes_files_and_injects_index_link_once(tmp_path: Path) -> None:
    kb_dir = tmp_path / "kb" / "disorders"
    dashboard_dir = tmp_path / "dashboard"
    index_path = dashboard_dir / "index.html"
    cache_path = tmp_path / "hpo_category_cache.json"

    _write(
        kb_dir / "Disease_A.yaml",
        """
name: Disease A
phenotypes:
- name: Cataract
  phenotype_term:
    term:
      id: HP:1
      label: Cataract
- name: Seizure
  phenotype_term:
    term:
      id: HP:2
      label: Seizure
""",
    )
    _write(
        kb_dir / "Disease_B.yaml",
        """
name: Disease B
phenotypes:
- name: Scoliosis
  phenotype_term:
    term:
      id: HP:3
      label: Scoliosis
""",
    )
    _write(kb_dir / "Disease_A.history.yaml", "name: ignored")
    _write(cache_path, json.dumps(CATEGORIES))
    _write(
        index_path,
        """
<!DOCTYPE html>
<html>
<body>
  <section class="chart-card"><h2>Existing Section</h2></section>
  <footer>Generated by linkml-data-qc</footer>
</body>
</html>
""",
    )

    kwargs = dict(
        kb_dir=kb_dir,
        dashboard_dir=dashboard_dir,
        dashboard_index_path=index_path,
        hpo_category_cache_path=cache_path,
    )
    first = generate_phenotype_systems_report(**kwargs)
    second = generate_phenotype_systems_report(**kwargs)

    assert first["summary"]["total_diseases"] == 2
    assert first["index_updated"] is True
    assert second["summary"] == first["summary"]

    payload = json.loads((dashboard_dir / "phenotype_systems.json").read_text(encoding="utf-8"))
    assert payload["summary"]["total_diseases"] == 2
    assert payload["summary"]["multi_system_phenotypes"] == 1
    assert {d["name"] for d in payload["diseases"]} == {"Disease A", "Disease B"}

    page = (dashboard_dir / "phenotype_systems.html").read_text(encoding="utf-8")
    assert "Disease A" in page and "Disease B" in page
    assert "../pages/disorders/Disease_A.html" in page

    index = index_path.read_text(encoding="utf-8")
    assert "phenotype_systems.html" in index
    assert index.count(PHENOTYPE_SYSTEMS_BLOCK_START) == 1
    assert index.count(PHENOTYPE_SYSTEMS_BLOCK_END) == 1
    assert "Existing Section" in index


def test_generate_report_requires_the_category_cache(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError, match="gen-browser-data"):
        generate_phenotype_systems_report(
            kb_dir=tmp_path,
            dashboard_dir=tmp_path / "dashboard",
            hpo_category_cache_path=tmp_path / "missing.json",
        )
