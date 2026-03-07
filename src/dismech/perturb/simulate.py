"""ODE simulation for perturbation analysis.

Loads SBML models via tellurium, runs coupled base+extension simulations,
and applies gene/parameter perturbations from model config.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


@dataclass
class GeneEffect:
    """How a gene perturbation maps to model parameters."""

    parameter: str | None = None
    species: str | None = None
    in_extension: bool = False
    LoF: float | None = None
    GoF: float | None = None
    description: str = ""


@dataclass
class PhenotypeThreshold:
    """Threshold for activating a phenotype from model output."""

    hp_id: str
    hp_label: str
    model_variable: str
    direction: str  # "above" or "below"
    threshold: float
    severity_scale: list[tuple[float, str]] = field(default_factory=list)


@dataclass
class VariableMapping:
    """Maps a named variable to its model species/parameter."""

    dataset_identifier: str = ""
    label: str = ""
    # Legacy fields for backwards compatibility with sidecar configs
    sbml_species: str | None = None
    extension_species: str | None = None
    extension_assignment: str | None = None


@dataclass
class CouplingConfig:
    """Configuration for coupled base+extension simulation."""

    dt_hours: int = 168
    duration_hours: int = 26280
    base_to_extension: dict[str, str] = field(default_factory=dict)
    gfr_parameter: str = "GFR"
    gfr_ext_parameter: str = "GFR_ext"


@dataclass
class ModelConfig:
    """Complete configuration for a perturbable model."""

    model_id: str
    sbml_file: str
    extension_file: str | None = None
    gene_effects: dict[str, GeneEffect] = field(default_factory=dict)
    variable_mappings: dict[str, VariableMapping] = field(default_factory=dict)
    phenotype_thresholds: list[PhenotypeThreshold] = field(default_factory=list)
    scenarios: dict[str, dict[str, Any]] = field(default_factory=dict)
    coupling: CouplingConfig = field(default_factory=CouplingConfig)
    _config_dir: Path = field(default_factory=lambda: Path("."))


@dataclass
class SimulationResult:
    """Result of a perturbation simulation."""

    variables: dict[str, float] = field(default_factory=dict)
    label: str = ""


def extract_model_variables(
    disorder: dict, model_id: str
) -> tuple[dict[str, VariableMapping], list[PhenotypeThreshold]]:
    """Extract variable mappings and phenotype thresholds from disorder YAML.

    Reads computational_models[].variables where model_id matches, using
    dataset_identifier for the native model name and mappings_list entries
    with threshold/threshold_direction for phenotype activation.

    Args:
        disorder: Parsed disorder YAML data
        model_id: Model ID to match (e.g., "BIOMD0000000613")

    Returns:
        Tuple of (variable_mappings dict, phenotype_thresholds list)
    """
    var_mappings: dict[str, VariableMapping] = {}
    thresholds: list[PhenotypeThreshold] = []

    for model in disorder.get("computational_models") or []:
        if not isinstance(model, dict):
            continue
        if model.get("model_id") != model_id:
            continue

        for var in model.get("variables") or []:
            if not isinstance(var, dict):
                continue
            name = var.get("name", "")
            ds_id = var.get("dataset_identifier", "")
            if not ds_id:
                continue
            label = var.get("description") or name
            unit = var.get("unit", "")
            if unit:
                label = f"{name} ({unit})"
            var_mappings[name] = VariableMapping(
                dataset_identifier=ds_id,
                label=label,
            )

            for mapping in var.get("mappings_list") or []:
                if not isinstance(mapping, dict):
                    continue
                term = mapping.get("term") or {}
                term_id = term.get("id", "")
                term_label = term.get("label", "")
                thresh = mapping.get("threshold")
                direction = mapping.get("threshold_direction")
                if thresh is not None and direction and term_id.startswith("HP:"):
                    severity = []
                    for tier in mapping.get("severity_scale") or []:
                        if isinstance(tier, dict):
                            severity.append(
                                (float(tier["threshold"]), str(tier["name"]))
                            )
                    thresholds.append(
                        PhenotypeThreshold(
                            hp_id=term_id,
                            hp_label=term_label,
                            model_variable=name,
                            direction=direction,
                            threshold=float(thresh),
                            severity_scale=severity,
                        )
                    )
        break  # Found matching model

    return var_mappings, thresholds


def load_model_config(config_path: Path, disorder: dict | None = None) -> ModelConfig:
    """Load model configuration from sidecar YAML, enriched with disorder YAML.

    Variable mappings and phenotype thresholds are read from the disorder
    YAML's computational_models[].variables when available. The sidecar
    provides gene_effects, scenarios, coupling, and fallback values.

    Args:
        config_path: Path to the .config.yaml file
        disorder: Parsed disorder YAML data (optional; enriches with
            variable mappings and phenotype thresholds)

    Returns:
        ModelConfig with all perturbation settings
    """
    with open(config_path) as f:
        raw = yaml.safe_load(f)

    model_id = raw["model_id"]

    gene_effects = {}
    for gene_name, ge_raw in (raw.get("gene_effects") or {}).items():
        gene_effects[gene_name] = GeneEffect(
            parameter=ge_raw.get("parameter"),
            species=ge_raw.get("species"),
            in_extension=ge_raw.get("in_extension", False),
            LoF=ge_raw.get("LoF"),
            GoF=ge_raw.get("GoF"),
            description=ge_raw.get("description", ""),
        )

    # Try disorder YAML first for variable mappings and thresholds
    var_mappings: dict[str, VariableMapping] = {}
    thresholds: list[PhenotypeThreshold] = []
    if disorder:
        var_mappings, thresholds = extract_model_variables(disorder, model_id)

    # Fall back to sidecar variable_mappings if YAML didn't provide any
    if not var_mappings:
        for var_name, vm_raw in (raw.get("variable_mappings") or {}).items():
            var_mappings[var_name] = VariableMapping(
                sbml_species=vm_raw.get("sbml_species"),
                extension_species=vm_raw.get("extension_species"),
                extension_assignment=vm_raw.get("extension_assignment"),
                label=vm_raw.get("label", var_name),
            )

    # Fall back to sidecar phenotype_thresholds if YAML didn't provide any
    if not thresholds:
        for pt_raw in raw.get("phenotype_thresholds") or []:
            severity = []
            for item in pt_raw.get("severity_scale") or []:
                if isinstance(item, list) and len(item) == 2:
                    severity.append((float(item[0]), str(item[1])))
            thresholds.append(
                PhenotypeThreshold(
                    hp_id=pt_raw["hp_id"],
                    hp_label=pt_raw["hp_label"],
                    model_variable=pt_raw["model_variable"],
                    direction=pt_raw["direction"],
                    threshold=float(pt_raw["threshold"]),
                    severity_scale=severity,
                )
            )

    coupling_raw = raw.get("coupling") or {}
    coupling = CouplingConfig(
        dt_hours=coupling_raw.get("dt_hours", 168),
        duration_hours=coupling_raw.get("duration_hours", 26280),
        base_to_extension=coupling_raw.get("base_to_extension", {}),
        gfr_parameter=coupling_raw.get("gfr_parameter", "GFR"),
        gfr_ext_parameter=coupling_raw.get("gfr_ext_parameter", "GFR_ext"),
    )

    return ModelConfig(
        model_id=model_id,
        sbml_file=raw["sbml_file"],
        extension_file=raw.get("extension_file"),
        gene_effects=gene_effects,
        variable_mappings=var_mappings,
        phenotype_thresholds=thresholds,
        scenarios=raw.get("scenarios") or {},
        coupling=coupling,
        _config_dir=config_path.parent,
    )


def run_perturbation(
    config: ModelConfig,
    gfr: float = 6.0,
    gene: str | None = None,
    effect: str | None = None,
    param_overrides: dict[str, float] | None = None,
) -> SimulationResult:
    """Run a perturbation simulation.

    Args:
        config: Model configuration
        gfr: GFR value (L/hr). 6.0 = healthy, 2.0 = CKD3b, 1.0 = CKD4
        gene: Gene name to perturb (must be in config.gene_effects)
        effect: "LoF" or "GoF"
        param_overrides: Direct parameter multipliers {param_name: multiplier}

    Returns:
        SimulationResult with final variable values
    """
    import tellurium as te

    models_dir = config._config_dir
    sbml_path = models_dir / config.sbml_file

    r_base = te.loadSBMLModel(str(sbml_path))
    r_base[config.coupling.gfr_parameter] = gfr
    r_base.integrator.absolute_tolerance = 1e-12
    r_base.integrator.relative_tolerance = 1e-8
    r_base.integrator.max_num_steps = 100000

    # Load extension model if available
    r_ext = None
    if config.extension_file:
        ext_path = models_dir / config.extension_file
        if ext_path.exists():
            antimony_str = ext_path.read_text()
            r_ext = te.loada(antimony_str)

    # Apply gene effects
    if gene and effect:
        ge = config.gene_effects.get(gene)
        if ge:
            multiplier = getattr(ge, effect, None)
            if multiplier is not None:
                target_param = ge.parameter or ge.species
                if target_param:
                    runner = r_ext if (ge.in_extension and r_ext) else r_base
                    runner[target_param] = runner[target_param] * multiplier

    # Apply parameter overrides
    if param_overrides:
        for param, mult in param_overrides.items():
            if param in r_base.getGlobalParameterIds():
                r_base[param] = r_base[param] * mult
            elif r_ext and param in r_ext.getGlobalParameterIds():
                r_ext[param] = r_ext[param] * mult

    # Get CYP24A1 base value for feedback
    cyp24a1_base_t69 = r_base["T69"] if "T69" in r_base.getGlobalParameterIds() else 0.1

    # Run coupled simulation
    dt = config.coupling.dt_hours
    duration = config.coupling.duration_hours
    n_steps = int(duration / dt)

    last_fgf23 = 50.0  # default

    for i in range(n_steps):
        t_start = i * dt
        t_end = (i + 1) * dt

        # Bidirectional feedback: FGF23 suppresses CYP27B1
        if r_ext and i > 0:
            fgf23_suppression = 1 / (1 + (last_fgf23 / 50) ** 1.5)
            r_base["T69"] = cyp24a1_base_t69 / max(fgf23_suppression, 0.01)

        r_base.simulate(t_start, t_end, 2)

        if r_ext:
            # Forward coupling: base -> extension
            for base_var, ext_var in config.coupling.base_to_extension.items():
                r_ext[ext_var] = r_base[base_var]
            r_ext[config.coupling.gfr_ext_parameter] = gfr
            r_ext.simulate(t_start, t_end, 2)
            last_fgf23 = r_ext["FGF23"]

    # Collect final values
    base_ids = set(r_base.getFloatingSpeciesIds() + r_base.getGlobalParameterIds())
    ext_ids = set()
    if r_ext:
        ext_ids = set(r_ext.getFloatingSpeciesIds() + r_ext.getGlobalParameterIds())

    variables = {}
    for var_name, vm in config.variable_mappings.items():
        if vm.dataset_identifier:
            ds_id = vm.dataset_identifier
            if ds_id in base_ids:
                variables[var_name] = float(r_base[ds_id])
            elif r_ext and ds_id in ext_ids:
                variables[var_name] = float(r_ext[ds_id])
        elif vm.sbml_species:
            variables[var_name] = float(r_base[vm.sbml_species])
        elif vm.extension_species and r_ext:
            variables[var_name] = float(r_ext[vm.extension_species])
        elif vm.extension_assignment and r_ext:
            variables[var_name] = float(r_ext[vm.extension_assignment])

    return SimulationResult(variables=variables)
