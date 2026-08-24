"""
SED-ML / COMBINE-archive export for dismech-perturb model configs.

``models/<model_id>.config.yaml`` is, in substance, a private encoding of a
SED-ML simulation experiment: each ``scenarios`` entry is a set of pre-simulation
model changes, ``coupling`` is a uniform time course plus integrator settings,
and the disorder YAML's ``computational_models[].variables`` are the observables
to report. This module translates that private encoding into the COMBINE
standards, so any of the ~50 SED-ML-capable simulation engines (COPASI,
tellurium, VCell, AMICI, ...) can run a dismech scenario without dismech code.

Output per model, under ``exports/sedml/<model_id>/``:

* ``<sbml_file>``     — a copy of the SBML model
* ``simulation.sedml``— SED-ML L1V3 describing every scenario
* ``manifest.xml``    — COMBINE archive manifest

and, when ``--omex`` is passed, ``exports/sedml/<model_id>.omex`` — the zipped
archive. The archive is written with fixed timestamps so repeated exports are
byte-identical.

**Scenario semantics.** ``run_perturbation`` applies changes in a fixed order:
the disease-severity dial (``scenarios[].gfr`` → ``coupling.gfr_parameter``) is
set *absolutely*, then a gene effect multiplies its target, then
``param_overrides`` multiply theirs. Multiplicative changes are relative to the
value in force at that point, not to the SBML initial value. Rather than try to
encode that ordering in SED-ML, the exporter *resolves* each scenario to
absolute values against the SBML initial values and emits plain
``changeAttribute`` elements. The resulting archive is self-contained and
order-independent, and each derived model carries a SED-ML ``notes`` element
recording how its values were obtained.

**Not every config is exportable.** A config with an ``extension_file`` is a
coupled base+extension co-simulation with Hill-type feedback applied between
timesteps — that is a bespoke numerical scheme with no SED-ML equivalent, so
those models are reported as skipped rather than mis-exported.
"""

from __future__ import annotations

import argparse
import xml.etree.ElementTree as ET
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from dismech.perturb.simulate import (
    ModelConfig,
    load_model_config,
    resolve_scenario_dial,
)
from dismech.yaml_io import safe_load

SEDML_NS = "http://sed-ml.org/sed-ml/level1/version3"
MATHML_NS = "http://www.w3.org/1998/Math/MathML"
XHTML_NS = "http://www.w3.org/1999/xhtml"
OMEX_MANIFEST_NS = "http://identifiers.org/combine.specifications/omex-manifest"

#: KiSAO terms for the integrator and its settings. dismech-perturb runs
#: libRoadRunner's default stiff solver (CVODE) with the tolerances in
#: ``coupling``; these are the standard KiSAO identifiers for those knobs.
KISAO_CVODE = "KISAO:0000019"
KISAO_ABSOLUTE_TOLERANCE = "KISAO:0000211"
KISAO_RELATIVE_TOLERANCE = "KISAO:0000209"
KISAO_MAXIMUM_NUM_STEPS = "KISAO:0000415"

#: COMBINE archive format URIs used in the manifest.
FORMAT_OMEX = "http://identifiers.org/combine.specifications/omex"
FORMAT_MANIFEST = "http://identifiers.org/combine.specifications/omex-manifest"
FORMAT_SEDML = "http://identifiers.org/combine.specifications/sed-ml"
FORMAT_SBML = "http://identifiers.org/combine.specifications/sbml"

#: Fixed zip timestamp, so a re-export of unchanged inputs is byte-identical.
_ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)


def _fmt(value: float) -> str:
    """Format a float for XML as briefly as round-trips exactly.

    `repr` alone leaks binary-representation noise into the archive: the
    pioglitazone scenario's 0.45 x 1.6 reprs as "0.7200000000000001". 15
    significant digits renders that as "0.72" and covers every value these
    configs produce; anything that does not survive the round trip falls back to
    `repr`, so exactness is never traded for brevity.
    """
    value = float(value)
    if value == int(value) and abs(value) < 1e15:
        return str(int(value))
    text = f"{value:.15g}"
    return text if float(text) == value else repr(value)


def sanitize_sid(value: str) -> str:
    """Make a SED-ML SId out of an arbitrary label (e.g. a gene name).

    Public because anything that has to reconstruct a task/model id from a
    scenario id — the verification script, for one — must use this exact
    mapping. A private re-implementation diverges silently: the id simply fails
    to resolve and the lookup returns None rather than raising.
    """
    out = "".join(ch if (ch.isalnum() or ch == "_") else "_" for ch in str(value))
    if not out or out[0].isdigit():
        out = f"_{out}"
    return out


@dataclass
class ModelSymbol:
    """An SBML parameter or species the exporter can address and change."""

    symbol_id: str
    kind: str  # "parameter" | "species"
    attribute: str  # "value" | "initialConcentration" | "initialAmount"
    initial: float

    def xpath(self) -> str:
        if self.kind == "parameter":
            container = "sbml:listOfParameters/sbml:parameter"
        else:
            container = "sbml:listOfSpecies/sbml:species"
        return (
            f"/sbml:sbml/sbml:model/{container}"
            f"[@id='{self.symbol_id}']/@{self.attribute}"
        )

    def target(self) -> str:
        """XPath to the element itself (for dataGenerator variables)."""
        if self.kind == "parameter":
            container = "sbml:listOfParameters/sbml:parameter"
        else:
            container = "sbml:listOfSpecies/sbml:species"
        return f"/sbml:sbml/sbml:model/{container}[@id='{self.symbol_id}']"


@dataclass
class SbmlModelInfo:
    """The bits of an SBML file the exporter needs, read without libsbml."""

    namespace: str
    symbols: dict[str, ModelSymbol]


@dataclass
class ResolvedChange:
    """One scenario change, reduced to an absolute value."""

    symbol: ModelSymbol
    value: float
    reason: str


@dataclass
class ResolvedScenario:
    scenario_id: str
    label: str
    changes: list[ResolvedChange] = field(default_factory=list)
    unresolved: list[str] = field(default_factory=list)


def read_sbml_model_info(sbml_path: Path) -> SbmlModelInfo:
    """Read parameter/species initial values and the SBML core namespace."""
    root = ET.parse(sbml_path).getroot()
    namespace = root.tag.split("}")[0].lstrip("{")
    model = root.find(f"{{{namespace}}}model")
    if model is None:
        raise ValueError(f"{sbml_path}: no <model> element")

    symbols: dict[str, ModelSymbol] = {}

    params = model.find(f"{{{namespace}}}listOfParameters")
    for param in params if params is not None else []:
        symbol_id = param.get("id")
        raw = param.get("value")
        if symbol_id and raw is not None:
            symbols[symbol_id] = ModelSymbol(symbol_id, "parameter", "value", float(raw))

    species = model.find(f"{{{namespace}}}listOfSpecies")
    for item in species if species is not None else []:
        symbol_id = item.get("id")
        if not symbol_id:
            continue
        for attribute in ("initialConcentration", "initialAmount"):
            raw = item.get(attribute)
            if raw is not None:
                symbols[symbol_id] = ModelSymbol(
                    symbol_id, "species", attribute, float(raw)
                )
                break

    return SbmlModelInfo(namespace=namespace, symbols=symbols)


def resolve_scenario(
    scenario_id: str,
    scenario: dict[str, Any],
    config: ModelConfig,
    info: SbmlModelInfo,
) -> ResolvedScenario:
    """Reduce one scenario to absolute model changes.

    Mirrors ``simulate.run_perturbation``'s ordering exactly: the severity dial
    is assigned, then the gene effect multiplies, then ``param_overrides``
    multiply — each against the value in force at that step.
    """
    resolved = ResolvedScenario(
        scenario_id=scenario_id,
        label=str(scenario.get("label") or scenario_id),
    )
    # Running values, seeded from the SBML initial values.
    current: dict[str, float] = {}
    reasons: dict[str, list[str]] = {}

    def record(symbol_id: str, value: float, reason: str) -> None:
        current[symbol_id] = value
        reasons.setdefault(symbol_id, []).append(reason)

    # 1. Disease-severity dial, set absolutely (only if the model exposes it).
    # A scenario without `gfr` resolves to the model's healthy baseline, the
    # same value every other execution path uses.
    dial = config.coupling.gfr_parameter
    dial_value = resolve_scenario_dial(config, scenario)
    if dial in info.symbols:
        record(dial, dial_value, f"severity dial {dial}={_fmt(dial_value)}")
    else:
        resolved.unresolved.append(
            f"severity dial '{dial}' is not a parameter or species of the model"
        )

    # 2. Gene effect, multiplicative on the value in force.
    gene = scenario.get("gene")
    effect = scenario.get("effect")
    if gene and effect:
        gene_effect = config.gene_effects.get(str(gene))
        multiplier = getattr(gene_effect, str(effect), None) if gene_effect else None
        target = (gene_effect.parameter or gene_effect.species) if gene_effect else None
        if gene_effect is None:
            resolved.unresolved.append(f"gene '{gene}' has no gene_effects entry")
        elif multiplier is None:
            resolved.unresolved.append(f"gene '{gene}' has no '{effect}' multiplier")
        elif not target or target not in info.symbols:
            resolved.unresolved.append(
                f"gene '{gene}' targets '{target}', absent from the model"
            )
        else:
            base = current.get(target, info.symbols[target].initial)
            record(
                target,
                base * float(multiplier),
                f"{gene} {effect} x{_fmt(float(multiplier))}",
            )

    # 3. Parameter overrides, multiplicative on the value in force.
    for name, multiplier in (scenario.get("param_overrides") or {}).items():
        if name not in info.symbols:
            resolved.unresolved.append(
                f"param_override '{name}' is absent from the model"
            )
            continue
        base = current.get(name, info.symbols[name].initial)
        record(name, base * float(multiplier), f"override x{_fmt(float(multiplier))}")

    for symbol_id, value in current.items():
        resolved.changes.append(
            ResolvedChange(
                symbol=info.symbols[symbol_id],
                value=value,
                reason="; ".join(reasons[symbol_id]),
            )
        )
    resolved.changes.sort(key=lambda change: change.symbol.symbol_id)
    return resolved


def _observable_symbols(
    config: ModelConfig, info: SbmlModelInfo
) -> list[tuple[str, ModelSymbol]]:
    """Model variables from the disorder YAML that exist in the SBML file."""
    observables: list[tuple[str, ModelSymbol]] = []
    for name, mapping in config.variable_mappings.items():
        symbol_id = mapping.dataset_identifier or mapping.sbml_species
        if symbol_id and symbol_id in info.symbols:
            observables.append((mapping.label or name, info.symbols[symbol_id]))
    return observables


def _add_notes(parent: ET.Element, text: str) -> None:
    """Attach a SED-ML ``notes`` element (XHTML content) to ``parent``.

    Free text has to go here rather than in an XML comment: libsedml rejects a
    comment inside ``listOfChanges`` as an unrecognized element in the SED-ML
    namespace, whereas ``notes`` is a valid child of every SedBase object.
    Notes must precede the object's other children.
    """
    notes = ET.SubElement(parent, f"{{{SEDML_NS}}}notes")
    paragraph = ET.SubElement(notes, f"{{{XHTML_NS}}}p")
    paragraph.text = text


def build_sedml(
    config: ModelConfig,
    info: SbmlModelInfo,
    scenarios: list[ResolvedScenario],
    *,
    disease_name: str | None = None,
) -> str:
    """Render the SED-ML L1V3 document for one model."""
    ET.register_namespace("", SEDML_NS)
    ET.register_namespace("math", MATHML_NS)
    ET.register_namespace("xhtml", XHTML_NS)

    root = ET.Element(
        f"{{{SEDML_NS}}}sedML",
        {"level": "1", "version": "3", "xmlns:sbml": info.namespace},
    )

    _add_notes(
        root,
        f"dismech-perturb scenarios for {config.model_id}"
        + (f" ({disease_name})" if disease_name else "")
        + f". Generated from models/{config.model_id}.config.yaml by "
        "dismech.perturb.sedml_export; do not hand-edit. Scenario changes are "
        "resolved to absolute values against the SBML initial values, in the "
        "order dismech-perturb applies them: severity dial, then gene effect, "
        "then parameter overrides.",
    )

    # --- models: one base + one derived model per scenario ------------------
    models_el = ET.SubElement(root, f"{{{SEDML_NS}}}listOfModels")
    ET.SubElement(
        models_el,
        f"{{{SEDML_NS}}}model",
        {
            "id": "base_model",
            "name": config.model_id,
            "language": "urn:sedml:language:sbml",
            "source": config.sbml_file,
        },
    )
    for scenario in scenarios:
        model_el = ET.SubElement(
            models_el,
            f"{{{SEDML_NS}}}model",
            {
                "id": f"model_{sanitize_sid(scenario.scenario_id)}",
                "name": scenario.label,
                "language": "urn:sedml:language:sbml",
                "source": "base_model",
            },
        )
        if not scenario.changes:
            continue
        _add_notes(
            model_el,
            "; ".join(
                f"{change.symbol.symbol_id}={_fmt(change.value)} ({change.reason})"
                for change in scenario.changes
            ),
        )
        changes_el = ET.SubElement(model_el, f"{{{SEDML_NS}}}listOfChanges")
        for change in scenario.changes:
            ET.SubElement(
                changes_el,
                f"{{{SEDML_NS}}}changeAttribute",
                {"target": change.symbol.xpath(), "newValue": _fmt(change.value)},
            )

    # --- simulation ---------------------------------------------------------
    simulations_el = ET.SubElement(root, f"{{{SEDML_NS}}}listOfSimulations")
    coupling = config.coupling
    number_of_points = max(1, int(coupling.duration_hours / coupling.dt_hours))
    time_course = ET.SubElement(
        simulations_el,
        f"{{{SEDML_NS}}}uniformTimeCourse",
        {
            "id": "time_course",
            "name": f"{coupling.duration_hours} h time course",
            "initialTime": "0",
            "outputStartTime": "0",
            "outputEndTime": _fmt(float(coupling.duration_hours)),
            "numberOfPoints": str(number_of_points),
        },
    )
    algorithm = ET.SubElement(
        time_course, f"{{{SEDML_NS}}}algorithm", {"kisaoID": KISAO_CVODE}
    )
    algorithm_params = ET.SubElement(
        algorithm, f"{{{SEDML_NS}}}listOfAlgorithmParameters"
    )
    for kisao, value in (
        (KISAO_ABSOLUTE_TOLERANCE, _fmt(coupling.abs_tol)),
        (KISAO_RELATIVE_TOLERANCE, _fmt(coupling.rel_tol)),
        (KISAO_MAXIMUM_NUM_STEPS, str(int(coupling.max_num_steps))),
    ):
        ET.SubElement(
            algorithm_params,
            f"{{{SEDML_NS}}}algorithmParameter",
            {"kisaoID": kisao, "value": value},
        )

    # --- tasks --------------------------------------------------------------
    tasks_el = ET.SubElement(root, f"{{{SEDML_NS}}}listOfTasks")
    for scenario in scenarios:
        ET.SubElement(
            tasks_el,
            f"{{{SEDML_NS}}}task",
            {
                "id": f"task_{sanitize_sid(scenario.scenario_id)}",
                "name": scenario.label,
                "modelReference": f"model_{sanitize_sid(scenario.scenario_id)}",
                "simulationReference": "time_course",
            },
        )

    # --- data generators ----------------------------------------------------
    observables = _observable_symbols(config, info)
    generators_el = ET.SubElement(root, f"{{{SEDML_NS}}}listOfDataGenerators")

    def add_generator(
        generator_id: str, name: str, task_id: str, symbol: ModelSymbol | None
    ) -> None:
        generator = ET.SubElement(
            generators_el,
            f"{{{SEDML_NS}}}dataGenerator",
            {"id": generator_id, "name": name},
        )
        variables = ET.SubElement(generator, f"{{{SEDML_NS}}}listOfVariables")
        variable_id = f"var_{generator_id}"
        attributes = {"id": variable_id, "taskReference": task_id}
        if symbol is None:
            attributes["symbol"] = "urn:sedml:symbol:time"
        else:
            attributes["target"] = symbol.target()
        ET.SubElement(variables, f"{{{SEDML_NS}}}variable", attributes)
        math = ET.SubElement(generator, f"{{{MATHML_NS}}}math")
        ci = ET.SubElement(math, f"{{{MATHML_NS}}}ci")
        ci.text = variable_id

    for scenario in scenarios:
        task_id = f"task_{sanitize_sid(scenario.scenario_id)}"
        suffix = sanitize_sid(scenario.scenario_id)
        add_generator(f"dg_time_{suffix}", "Time", task_id, None)
        for label, symbol in observables:
            add_generator(
                f"dg_{suffix}_{sanitize_sid(symbol.symbol_id)}", label, task_id, symbol
            )

    # --- outputs: one report + one plot per scenario -------------------------
    outputs_el = ET.SubElement(root, f"{{{SEDML_NS}}}listOfOutputs")
    for scenario in scenarios:
        suffix = sanitize_sid(scenario.scenario_id)
        report = ET.SubElement(
            outputs_el,
            f"{{{SEDML_NS}}}report",
            {"id": f"report_{suffix}", "name": scenario.label},
        )
        data_sets = ET.SubElement(report, f"{{{SEDML_NS}}}listOfDataSets")
        ET.SubElement(
            data_sets,
            f"{{{SEDML_NS}}}dataSet",
            {
                "id": f"ds_time_{suffix}",
                "label": "time",
                "name": "Time",
                "dataReference": f"dg_time_{suffix}",
            },
        )
        for label, symbol in observables:
            ET.SubElement(
                data_sets,
                f"{{{SEDML_NS}}}dataSet",
                {
                    "id": f"ds_{suffix}_{sanitize_sid(symbol.symbol_id)}",
                    "label": symbol.symbol_id,
                    "name": label,
                    "dataReference": f"dg_{suffix}_{sanitize_sid(symbol.symbol_id)}",
                },
            )

        if not observables:
            continue
        plot = ET.SubElement(
            outputs_el,
            f"{{{SEDML_NS}}}plot2D",
            {"id": f"plot_{suffix}", "name": scenario.label},
        )
        curves = ET.SubElement(plot, f"{{{SEDML_NS}}}listOfCurves")
        for label, symbol in observables:
            ET.SubElement(
                curves,
                f"{{{SEDML_NS}}}curve",
                {
                    "id": f"curve_{suffix}_{sanitize_sid(symbol.symbol_id)}",
                    "name": label,
                    "logX": "false",
                    "logY": "false",
                    "xDataReference": f"dg_time_{suffix}",
                    "yDataReference": f"dg_{suffix}_{sanitize_sid(symbol.symbol_id)}",
                },
            )

    ET.indent(root, space="  ")
    body = ET.tostring(root, encoding="unicode", xml_declaration=False)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n{body}\n'


def build_manifest(sbml_filename: str) -> str:
    """Render the COMBINE archive manifest."""
    ET.register_namespace("", OMEX_MANIFEST_NS)
    root = ET.Element(f"{{{OMEX_MANIFEST_NS}}}omexManifest")
    for location, fmt, master in (
        (".", FORMAT_OMEX, False),
        ("./manifest.xml", FORMAT_MANIFEST, False),
        ("./simulation.sedml", FORMAT_SEDML, True),
        (f"./{sbml_filename}", FORMAT_SBML, False),
    ):
        attributes = {"location": location, "format": fmt}
        if master:
            attributes["master"] = "true"
        ET.SubElement(root, f"{{{OMEX_MANIFEST_NS}}}content", attributes)
    ET.indent(root, space="  ")
    body = ET.tostring(root, encoding="unicode", xml_declaration=False)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n{body}\n'


def write_omex(archive_dir: Path, omex_path: Path) -> None:
    """Zip an archive directory into a .omex with deterministic metadata."""
    omex_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(omex_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(archive_dir.rglob("*")):
            if not path.is_file():
                continue
            entry = zipfile.ZipInfo(
                str(path.relative_to(archive_dir)), date_time=_ZIP_TIMESTAMP
            )
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o644 << 16
            archive.writestr(entry, path.read_bytes())


def find_disorder_for_model(model_id: str, disorders_dir: Path) -> dict[str, Any] | None:
    """Find the disorder entry curating ``model_id`` (for variables/thresholds)."""
    if not disorders_dir.exists():
        return None
    for path in sorted(disorders_dir.glob("*.yaml")):
        if path.name.endswith(".history.yaml"):
            continue
        with open(path) as handle:
            entry = safe_load(handle) or {}
        for model in entry.get("computational_models") or []:
            if isinstance(model, dict) and model.get("model_id") == model_id:
                return entry
    return None


@dataclass
class ExportResult:
    model_id: str
    archive_dir: Path | None = None
    omex_path: Path | None = None
    scenario_count: int = 0
    observable_count: int = 0
    warnings: list[str] = field(default_factory=list)
    skipped_reason: str | None = None


def export_config(
    config_path: Path,
    output_root: Path,
    *,
    disorders_dir: Path = Path("kb/disorders"),
    write_archive: bool = False,
) -> ExportResult:
    """Export one ``models/<model_id>.config.yaml`` to a COMBINE archive."""
    with open(config_path) as handle:
        raw = safe_load(handle) or {}
    model_id = str(raw.get("model_id") or config_path.stem)

    if raw.get("extension_file"):
        return ExportResult(
            model_id=model_id,
            skipped_reason=(
                "config declares an extension_file: the run is a coupled "
                "base+extension co-simulation with inter-step Hill feedback, "
                "which SED-ML cannot express"
            ),
        )

    disorder = find_disorder_for_model(model_id, disorders_dir)
    config = load_model_config(config_path, disorder=disorder)

    sbml_path = config_path.parent / config.sbml_file
    if not sbml_path.exists():
        return ExportResult(
            model_id=model_id, skipped_reason=f"SBML file not found: {sbml_path}"
        )
    info = read_sbml_model_info(sbml_path)

    scenarios = [
        resolve_scenario(scenario_id, scenario or {}, config, info)
        for scenario_id, scenario in config.scenarios.items()
    ]
    warnings = [
        f"{scenario.scenario_id}: {note}"
        for scenario in scenarios
        for note in scenario.unresolved
    ]

    archive_dir = output_root / model_id
    archive_dir.mkdir(parents=True, exist_ok=True)
    (archive_dir / config.sbml_file).write_bytes(sbml_path.read_bytes())
    (archive_dir / "simulation.sedml").write_text(
        build_sedml(
            config, info, scenarios, disease_name=(disorder or {}).get("name")
        )
    )
    (archive_dir / "manifest.xml").write_text(build_manifest(config.sbml_file))

    omex_path = None
    if write_archive:
        omex_path = output_root / f"{model_id}.omex"
        write_omex(archive_dir, omex_path)

    return ExportResult(
        model_id=model_id,
        archive_dir=archive_dir,
        omex_path=omex_path,
        scenario_count=len(scenarios),
        observable_count=len(_observable_symbols(config, info)),
        warnings=warnings,
    )


def export_all(
    models_dir: Path = Path("models"),
    output_root: Path = Path("exports/sedml"),
    *,
    disorders_dir: Path = Path("kb/disorders"),
    write_archive: bool = False,
) -> list[ExportResult]:
    return [
        export_config(
            path,
            output_root,
            disorders_dir=disorders_dir,
            write_archive=write_archive,
        )
        for path in sorted(models_dir.glob("*.config.yaml"))
    ]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export dismech-perturb model configs as SED-ML / COMBINE archives"
    )
    parser.add_argument("--models-dir", default="models")
    parser.add_argument("--disorders-dir", default="kb/disorders")
    parser.add_argument("--output", "-o", default="exports/sedml")
    parser.add_argument(
        "--id", help="Export only this model_id (default: every config found)"
    )
    parser.add_argument(
        "--omex",
        action="store_true",
        help="Also write the zipped .omex archive (derived; not committed)",
    )
    args = parser.parse_args()

    models_dir = Path(args.models_dir)
    paths = sorted(models_dir.glob("*.config.yaml"))
    if args.id:
        paths = [path for path in paths if path.name == f"{args.id}.config.yaml"]
        if not paths:
            parser.error(f"no config found for model_id '{args.id}' in {models_dir}")

    for path in paths:
        result = export_config(
            path,
            Path(args.output),
            disorders_dir=Path(args.disorders_dir),
            write_archive=args.omex,
        )
        if result.skipped_reason:
            print(f"SKIP  {result.model_id}: {result.skipped_reason}")
            continue
        print(
            f"OK    {result.model_id}: {result.scenario_count} scenarios, "
            f"{result.observable_count} observables -> {result.archive_dir}"
            + (f" (+ {result.omex_path})" if result.omex_path else "")
        )
        for warning in result.warnings:
            print(f"  WARN {warning}")


if __name__ == "__main__":
    main()
