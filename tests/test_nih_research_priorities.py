"""Tests for the NIH Highlighted-Topic funding-priority classification.

This is a *secondary* classification (grant-strategy relevance, not a disease
nosology). The enum is GENERATED from a dated snapshot
(``data/nih_highlighted_topics/topics.tsv``) by
``scripts/gen_nih_topics_enum.py``. This suite pins:

  * the generated enum is in sync with the snapshot (regen was not forgotten);
  * the schema wires the enum into an assignment class + the
    ``DiseaseClassifications`` container;
  * enum keys follow the stable ``NIH_HT_<number>_<slug>`` format;
  * project ``nih_topics`` frontmatter resolves to display records.
"""

from __future__ import annotations

import importlib.util
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "gen_nih_topics_enum.py"
ENUM_PATH = ROOT / "src" / "dismech" / "schema" / "classifications" / "nih_research_priorities.yaml"
TSV = ROOT / "data" / "nih_highlighted_topics" / "topics.tsv"


def _enum_values() -> dict:
    doc = yaml.safe_load(ENUM_PATH.read_text())
    return doc["enums"]["NIHResearchPriorityEnum"]["permissible_values"]


def test_generated_enum_in_sync_with_snapshot() -> None:
    """`gen_nih_topics_enum.py --check` must pass (regen not forgotten)."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--check"],
        capture_output=True, text=True, cwd=ROOT,
    )
    assert result.returncode == 0, (
        "nih_research_priorities.yaml is stale — run "
        "`python scripts/gen_nih_topics_enum.py`.\n" + result.stdout + result.stderr
    )


def test_enum_covers_every_snapshot_topic() -> None:
    n_rows = sum(1 for _ in TSV.read_text().splitlines()[1:])
    assert len(_enum_values()) == n_rows == 72


def test_enum_key_format_is_stable() -> None:
    """Keys must be NIH_HT_<number>_<slug> so the numeric anchor is stable."""
    pat = re.compile(r"^NIH_HT_\d+_[a-z0-9_]+$")
    for key in _enum_values():
        assert pat.match(key), f"unexpected enum key format: {key}"


def test_key_topic_numbers_are_unique() -> None:
    numbers = [int(k.split("_")[2]) for k in _enum_values()]
    assert len(numbers) == len(set(numbers))


def test_schema_wires_classification() -> None:
    from linkml_runtime.utils.schemaview import SchemaView

    sv = SchemaView(str(ROOT / "src" / "dismech" / "schema" / "dismech.yaml"))
    assert sv.get_enum("NIHResearchPriorityEnum") is not None
    assignment = sv.get_class("NIHResearchPriorityAssignment")
    assert assignment is not None
    assert assignment.is_a == "ClassificationAssignment"
    container = sv.get_class("DiseaseClassifications")
    assert "nih_research_priority" in container.slots


def test_project_nih_topics_resolve_to_display_records() -> None:
    from dismech.render import _resolve_nih_topics

    key = next(iter(_enum_values()))
    records = _resolve_nih_topics({"nih_topics": [key]})
    assert len(records) == 1
    rec = records[0]
    assert rec["key"] == key
    assert rec["label"] and not rec["label"].startswith("NIH_HT_")
    assert rec["href"].startswith("https://grants.nih.gov/")


def test_resolver_tolerates_unknown_key() -> None:
    from dismech.render import _resolve_nih_topics

    records = _resolve_nih_topics({"nih_topics": ["NIH_HT_9999_not_real"]})
    assert records == [{"key": "NIH_HT_9999_not_real", "label": "NIH_HT_9999_not_real", "href": None}]


def _load_summary_module():
    import importlib.util
    script = ROOT / "scripts" / "gen_nih_topics_summary.py"
    spec = importlib.util.spec_from_file_location("gen_nih_topics_summary", script)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_summary_page_builds_and_embeds_all_topics() -> None:
    """The coverage page must embed all 72 topics and be valid HTML/JSON."""
    import json
    import re

    mod = _load_summary_module()
    html_out = mod.build()
    assert html_out.lstrip().startswith("<!doctype html>")
    m = re.search(r"const DATA = (\[.*?\]);\n", html_out, re.S)
    assert m, "embedded DATA array not found"
    data = json.loads(m.group(1))
    assert len(data) == len(_enum_values()) == 72
    # Every card has the fields the client script reads.
    for card in data:
        assert {"number", "title", "url", "diseases", "projects", "count"} <= card.keys()


def test_summary_collects_known_tags() -> None:
    """Known worked examples must show up in the aggregation."""
    mod = _load_summary_module()
    hits = mod._collect()
    t89 = "NIH_HT_89_cellular_quiescence_senescence_cell_death_in"
    t42 = "NIH_HT_42_rare_cancers_across_cancer_control_continuum"
    disease_names_89 = {d["name"] for d in hits.get(t89, {}).get("diseases", [])}
    assert any("Progeria" in n for n in disease_names_89)
    disease_names_42 = {d["name"] for d in hits.get(t42, {}).get("diseases", [])}
    assert any("Merkel" in n for n in disease_names_42)
    # At least one project tag was collected for a method topic.
    t66 = "NIH_HT_66_scientific_rigor_transparency_replicability"
    assert hits.get(t66, {}).get("projects")
