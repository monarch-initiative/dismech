"""Tests for the SED-ML / COMBINE-archive exporter."""

from __future__ import annotations

import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

import pytest

from dismech.perturb.sedml_export import (
    SEDML_NS,
    ModelSymbol,
    _fmt,
    build_manifest,
    build_sedml,
    export_all,
    export_config,
    read_sbml_model_info,
    resolve_scenario,
    sanitize_sid,
    write_omex,
)
from dismech.perturb.simulate import load_model_config

REPO_ROOT = Path(__file__).resolve().parents[1]
MODELS_DIR = REPO_ROOT / "models"
EXPORT_DIR = REPO_ROOT / "exports" / "sedml"


@pytest.fixture(scope="module")
def urate_config():
    return load_model_config(MODELS_DIR / "urate_homeostasis.config.yaml")


@pytest.fixture(scope="module")
def urate_info():
    return read_sbml_model_info(MODELS_DIR / "urate_homeostasis.xml")


def test_read_sbml_model_info_finds_parameters_and_species(urate_info):
    assert urate_info.namespace == "http://www.sbml.org/sbml/level3/version2/core"
    assert urate_info.symbols["f_exc"].kind == "parameter"
    assert urate_info.symbols["f_exc"].initial == 1.0
    assert urate_info.symbols["U"].kind == "species"
    assert urate_info.symbols["U"].attribute == "initialConcentration"
    assert urate_info.symbols["U"].initial == 5.0


def test_xpath_targets_the_right_attribute():
    parameter = ModelSymbol("f_exc", "parameter", "value", 1.0)
    species = ModelSymbol("U", "species", "initialConcentration", 5.0)
    assert parameter.xpath() == (
        "/sbml:sbml/sbml:model/sbml:listOfParameters/sbml:parameter"
        "[@id='f_exc']/@value"
    )
    assert species.xpath() == (
        "/sbml:sbml/sbml:model/sbml:listOfSpecies/sbml:species"
        "[@id='U']/@initialConcentration"
    )
    # dataGenerator variables address the element, not one of its attributes.
    assert species.target().endswith("sbml:species[@id='U']")


def _changes(resolved):
    return {change.symbol.symbol_id: change.value for change in resolved.changes}


def test_severity_dial_is_absolute(urate_config, urate_info):
    resolved = resolve_scenario(
        "underexcretion", {"gfr": 0.5}, urate_config, urate_info
    )
    assert _changes(resolved) == {"f_exc": 0.5}
    assert not resolved.unresolved


def test_gene_effect_multiplies_the_dial_value(urate_config, urate_info):
    """`gfr` sets f_exc=1.0, then ABCG2 LoF multiplies it by 0.5."""
    resolved = resolve_scenario(
        "ABCG2_LoF",
        {"gene": "ABCG2", "effect": "LoF", "gfr": 1.0},
        urate_config,
        urate_info,
    )
    assert _changes(resolved) == {"f_exc": 0.5}


def test_param_overrides_compose_on_top_of_the_dial(urate_config, urate_info):
    """The combination scenario sets f_exc=0.5 then multiplies by 1.6 -> 0.8."""
    resolved = resolve_scenario(
        "combination",
        {"gfr": 0.5, "param_overrides": {"XO": 0.5, "f_exc": 1.6}},
        urate_config,
        urate_info,
    )
    assert _changes(resolved) == pytest.approx({"XO": 0.5, "f_exc": 0.8})


def test_param_override_multiplies_the_sbml_initial_value(urate_config, urate_info):
    """An override on an untouched parameter scales its SBML initial value."""
    resolved = resolve_scenario(
        "pegloticase",
        {"gfr": 0.5, "param_overrides": {"k_uricase": 800.0}},
        urate_config,
        urate_info,
    )
    # k_uricase initial is 0.001, so x800 -> 0.8 (not 800).
    assert _changes(resolved)["k_uricase"] == pytest.approx(0.8)


def test_unresolvable_references_are_reported_not_silently_dropped(
    urate_config, urate_info
):
    resolved = resolve_scenario(
        "bogus",
        {"gfr": 1.0, "gene": "NOT_A_GENE", "effect": "LoF", "param_overrides": {"nope": 2}},
        urate_config,
        urate_info,
    )
    assert any("NOT_A_GENE" in note for note in resolved.unresolved)
    assert any("nope" in note for note in resolved.unresolved)


def test_missing_gfr_falls_back_to_the_model_baseline(urate_config, urate_info):
    """Not to a hardcoded literal: the dial means something different per model."""
    resolved = resolve_scenario("no_dial", {}, urate_config, urate_info)
    assert _changes(resolved) == {"f_exc": urate_config.coupling.baseline_gfr}
    assert not resolved.unresolved


def test_fmt_never_trades_exactness_for_brevity():
    """The shortest form is used only where it round-trips to the same double.

    `0.45 * 1.6` is `0.7200000000000001`, and `f"{v:.15g}"` renders it as
    "0.72" — but `float("0.72")` is a *different* double. Shortening it would
    make the archive encode a value dismech-perturb never computes, so the long
    form stays. Values that genuinely are short stay short.
    """
    noisy = 0.45 * 1.6
    assert float(_fmt(noisy)) == noisy
    assert _fmt(noisy) == "0.7200000000000001"

    for value in (0.5, 0.8, 0.35, 2.5, 1e-12):
        assert float(_fmt(value)) == value
        assert _fmt(value) == f"{value:.15g}"

    assert _fmt(1.0) == "1"


def test_sanitize_sid_is_the_single_source_of_id_mapping():
    assert sanitize_sid("NKX2-1_LoF") == "NKX2_1_LoF"
    assert sanitize_sid("2fast") == "_2fast"
    assert sanitize_sid("") == "_"


def test_build_sedml_emits_the_expected_skeleton(urate_config, urate_info):
    scenarios = [
        resolve_scenario("s1", {"gfr": 0.5}, urate_config, urate_info),
    ]
    xml = build_sedml(urate_config, urate_info, scenarios, disease_name="Gout")
    root = ET.fromstring(xml)

    assert root.tag == f"{{{SEDML_NS}}}sedML"
    assert root.get("level") == "1" and root.get("version") == "3"
    # The SBML namespace must be declared so the change XPaths resolve.
    assert urate_info.namespace in xml

    models = root.find(f"{{{SEDML_NS}}}listOfModels")
    assert [model.get("id") for model in models] == ["base_model", "model_s1"]
    change = models[1].find(
        f"{{{SEDML_NS}}}listOfChanges/{{{SEDML_NS}}}changeAttribute"
    )
    assert change.get("newValue") == "0.5"

    time_course = root.find(
        f"{{{SEDML_NS}}}listOfSimulations/{{{SEDML_NS}}}uniformTimeCourse"
    )
    assert time_course.get("outputEndTime") == "500"
    # duration 500 / dt 25 = 20 output points
    assert time_course.get("numberOfPoints") == "20"
    algorithm = time_course.find(f"{{{SEDML_NS}}}algorithm")
    assert algorithm.get("kisaoID") == "KISAO:0000019"

    task = root.find(f"{{{SEDML_NS}}}listOfTasks/{{{SEDML_NS}}}task")
    assert task.get("modelReference") == "model_s1"
    assert task.get("simulationReference") == "time_course"


def test_manifest_lists_every_archive_entry():
    manifest = build_manifest("urate_homeostasis.xml")
    root = ET.fromstring(manifest)
    locations = {content.get("location") for content in root}
    assert locations == {
        ".",
        "./manifest.xml",
        "./simulation.sedml",
        "./urate_homeostasis.xml",
    }
    masters = [content for content in root if content.get("master") == "true"]
    assert len(masters) == 1
    assert masters[0].get("location") == "./simulation.sedml"


def test_coupled_extension_configs_are_skipped_not_mis_exported(tmp_path):
    result = export_config(
        MODELS_DIR / "BIOMD0000000613.config.yaml",
        tmp_path,
        disorders_dir=REPO_ROOT / "kb" / "disorders",
    )
    assert result.archive_dir is None
    assert "extension_file" in result.skipped_reason


def test_omex_archive_is_deterministic(tmp_path):
    result = export_config(
        MODELS_DIR / "urate_homeostasis.config.yaml",
        tmp_path,
        disorders_dir=REPO_ROOT / "kb" / "disorders",
        write_archive=True,
    )
    first = result.omex_path.read_bytes()
    write_omex(result.archive_dir, result.omex_path)
    assert result.omex_path.read_bytes() == first

    with zipfile.ZipFile(result.omex_path) as archive:
        assert sorted(archive.namelist()) == [
            "manifest.xml",
            "simulation.sedml",
            "urate_homeostasis.xml",
        ]


def test_committed_exports_are_in_sync_with_the_configs(tmp_path):
    """`just sedml-export` output must be regenerated when a config changes."""
    results = export_all(
        MODELS_DIR, tmp_path, disorders_dir=REPO_ROOT / "kb" / "disorders"
    )
    exported = [result for result in results if result.archive_dir]
    assert exported, "expected at least one exportable model config"

    for result in exported:
        committed_dir = EXPORT_DIR / result.model_id
        assert committed_dir.is_dir(), f"missing committed export for {result.model_id}"
        for path in sorted(result.archive_dir.iterdir()):
            committed = committed_dir / path.name
            assert committed.exists(), f"{committed} missing — run `just sedml-export`"
            assert committed.read_bytes() == path.read_bytes(), (
                f"{committed} is stale — run `just sedml-export`"
            )


def test_committed_exports_validate_against_libsedml():
    """The reference SED-ML implementation must parse the archives cleanly."""
    libsedml = pytest.importorskip("libsedml")

    documents = sorted(EXPORT_DIR.glob("*/simulation.sedml"))
    assert documents, "no exported SED-ML documents found"
    for path in documents:
        document = libsedml.readSedML(str(path))
        severe = [
            document.getError(index)
            for index in range(document.getNumErrors())
            if document.getError(index).getSeverity() >= 2
        ]
        messages = [
            f"line {error.getLine()}: {error.getShortMessage()}" for error in severe
        ]
        assert not severe, f"{path}: {messages}"
        assert document.getNumTasks() > 0
        assert document.getNumDataGenerators() > 0
