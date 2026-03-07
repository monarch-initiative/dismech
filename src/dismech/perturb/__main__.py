"""CLI for causal perturbation analysis.

Usage:
    uv run python -m dismech.perturb kb/disorders/CKD-Mineral_Bone_Disorder.yaml --gene CASR --effect LoF
    uv run python -m dismech.perturb kb/disorders/CKD-Mineral_Bone_Disorder.yaml --all
    uv run python -m dismech.perturb kb/disorders/CKD-Mineral_Bone_Disorder.yaml --param OralPhos=2.0
"""

from pathlib import Path
from typing import Optional

import typer
import yaml

from dismech.perturb.graph import extract_causal_edges, trace_causal_paths
from dismech.perturb.simulate import load_model_config, run_perturbation, ModelConfig
from dismech.perturb.phenotypes import evaluate_phenotypes

app = typer.Typer(help="Causal perturbation analysis for dismech disorders.")


def _find_model_config(
    disorder: dict, models_dir: Path | None = None
) -> ModelConfig | None:
    """Find and load the model config for a disorder's computational model."""
    models = disorder.get("computational_models") or []
    if not models:
        return None

    search_dirs = [models_dir] if models_dir else [Path("models")]
    for model in models:
        model_id = model.get("model_id", "")
        if not model_id:
            continue
        for d in search_dirs:
            config_path = d / f"{model_id}.config.yaml"
            if config_path.exists():
                return load_model_config(config_path, disorder=disorder)

    return None


def _print_variable_table(
    result: dict[str, float],
    baseline: dict[str, float],
    reference: dict[str, float],
    config: ModelConfig,
) -> None:
    """Print a table of variable changes."""
    print(
        f"\n  {'Variable':<30} {'Unperturbed':>12} {'Perturbed':>12} {'Change':>10} {'vs Healthy':>12}"
    )
    print(f"  {'─' * 80}")

    for var_name, vm in config.variable_mappings.items():
        if var_name not in result:
            continue
        ref_v = reference.get(var_name, 0)
        pert_v = result[var_name]
        base_v = baseline.get(var_name, 0)
        delta_ref = ((pert_v - ref_v) / ref_v * 100) if ref_v != 0 else 0
        delta_base = ((pert_v - base_v) / base_v * 100) if base_v != 0 else 0
        marker = " <<<" if abs(delta_ref) > 20 else ""
        print(
            f"  {vm.label:<30} {ref_v:>12.2f} {pert_v:>12.2f} {delta_ref:>+9.1f}% {delta_base:>+11.1f}%{marker}"
        )


def _get_causal_edges(disorder: dict):
    """Extract causal edges from disorder YAML pathophysiology downstream entries."""
    return extract_causal_edges(disorder)


@app.command()
def perturb(
    disorder_yaml: Path = typer.Argument(..., help="Path to disorder YAML file"),
    gene: Optional[str] = typer.Option(None, "--gene", "-g", help="Gene to perturb"),
    effect: Optional[str] = typer.Option(None, "--effect", "-e", help="LoF or GoF"),
    param: Optional[list[str]] = typer.Option(
        None, "--param", "-p", help="Parameter override (name=multiplier)"
    ),
    gfr: float = typer.Option(
        2.0, "--gfr", help="GFR value (L/hr). 6.0=healthy, 2.0=CKD3b, 1.0=CKD4"
    ),
    all_scenarios: bool = typer.Option(
        False, "--all", "-a", help="Run all predefined scenarios"
    ),
    models_dir: Optional[Path] = typer.Option(
        None, "--models-dir", "-m", help="Directory containing model files"
    ),
    scenario: Optional[str] = typer.Option(
        None, "--scenario", "-s", help="Run a named scenario from config"
    ),
) -> None:
    """Run causal perturbation analysis on a disorder."""
    with open(disorder_yaml) as f:
        disorder = yaml.safe_load(f)

    disorder_name = disorder.get("name", disorder_yaml.stem)
    typer.echo(f"Disorder: {disorder_name}")

    config = _find_model_config(disorder, models_dir)
    if config is None:
        typer.echo(
            "No model config found. Check computational_models for model_id with matching .config.yaml"
        )
        raise typer.Exit(1)

    typer.echo(f"Model: {config.model_id}")
    typer.echo("Computing healthy baseline (GFR=6.0)...")
    baseline_result = run_perturbation(config, gfr=6.0)
    baseline = baseline_result.variables

    if all_scenarios:
        _run_all_scenarios(config, baseline, disorder)
    elif scenario:
        _run_named_scenario(config, baseline, scenario, disorder)
    else:
        _run_single(config, baseline, gene, effect, param, gfr)


def _run_single(
    config: ModelConfig,
    baseline: dict[str, float],
    gene: str | None,
    effect: str | None,
    param: list[str] | None,
    gfr: float,
) -> None:
    """Run a single perturbation."""
    param_overrides = {}
    if param:
        for p in param:
            if "=" not in p:
                typer.echo(f"Error: --param requires NAME=VALUE format, got '{p}'")
                raise typer.Exit(1)
            name, val = p.split("=", 1)
            param_overrides[name] = float(val)

    ref_result = run_perturbation(config, gfr=gfr)
    reference = ref_result.variables

    result = run_perturbation(
        config,
        gfr=gfr,
        gene=gene,
        effect=effect,
        param_overrides=param_overrides or None,
    )

    label = f"{gene} {effect}" if gene else f"params: {param_overrides}"
    print(f"\n{'=' * 90}")
    print(f"PERTURBATION: {label}")
    print(f"GFR: {gfr}")
    print(f"{'=' * 90}")

    _print_variable_table(result.variables, baseline, reference, config)

    activated = evaluate_phenotypes(
        result.variables, baseline, config.phenotype_thresholds
    )
    if activated:
        print("\n  ACTIVATED PHENOTYPES:")
        for a in activated:
            print(
                f"    [{a.severity:>15}] {a.hp_id} {a.hp_label} (value: {a.value_description})"
            )
    else:
        print("\n  No phenotypes activated.")


def _run_all_scenarios(
    config: ModelConfig, baseline: dict[str, float], disorder: dict
) -> None:
    """Run all predefined scenarios from the config."""
    print(f"\n{'=' * 100}")
    print("CAUSAL PERTURBATION ANALYSIS: All Scenarios")
    print(f"{'=' * 100}")

    for scenario_name, scenario in config.scenarios.items():
        _run_scenario(config, baseline, scenario_name, scenario, disorder)

    _print_gene_phenotype_matrix(config, baseline)


def _run_named_scenario(
    config: ModelConfig, baseline: dict[str, float], name: str, disorder: dict
) -> None:
    """Run a single named scenario."""
    if name not in config.scenarios:
        typer.echo(
            f"Unknown scenario: {name}. Available: {', '.join(config.scenarios.keys())}"
        )
        raise typer.Exit(1)
    _run_scenario(config, baseline, name, config.scenarios[name], disorder)


def _run_scenario(
    config: ModelConfig,
    baseline: dict[str, float],
    name: str,
    scenario: dict,
    disorder: dict,
) -> None:
    """Run one scenario and print results."""
    label = scenario.get("label", name)
    gene = scenario.get("gene")
    effect = scenario.get("effect")
    gfr = scenario.get("gfr", 2.0)
    param_overrides = scenario.get("param_overrides")

    print(f"\n{'─' * 100}")
    print(f"  PERTURBATION: {label}")
    if gene:
        print(f"  Gene: {gene}")
    print(f"  GFR: {gfr}")
    print(f"{'─' * 100}")

    ref_result = run_perturbation(config, gfr=gfr)
    result = run_perturbation(
        config,
        gfr=gfr,
        gene=gene,
        effect=effect,
        param_overrides=param_overrides,
    )

    _print_variable_table(result.variables, baseline, ref_result.variables, config)

    activated = evaluate_phenotypes(
        result.variables, baseline, config.phenotype_thresholds
    )
    if activated:
        print("\n  ACTIVATED PHENOTYPES:")
        for a in activated:
            print(
                f"    [{a.severity:>15}] {a.hp_id} {a.hp_label} (value: {a.value_description})"
            )

    causal_root = scenario.get("causal_root")
    if causal_root:
        edges = _get_causal_edges(disorder)
        paths = trace_causal_paths(causal_root, edges)
        if paths:
            long_paths = sorted(paths, key=len, reverse=True)[:3]
            print(f"\n  CAUSAL CHAINS (top {len(long_paths)}):")
            for j, path in enumerate(long_paths):
                chain_parts = [path[0].source]
                for edge in path:
                    chain_parts.append(f"--[{edge.relationship}]--> {edge.target}")
                print(f"    {j + 1}. {' '.join(chain_parts)}")
                print(f"       via: {path[-1].mechanism}")


def _print_gene_phenotype_matrix(
    config: ModelConfig, baseline: dict[str, float]
) -> None:
    """Print gene-to-phenotype activation matrix."""
    gene_scenarios = {k: v for k, v in config.scenarios.items() if v.get("gene")}
    if not gene_scenarios:
        return

    hp_labels = sorted(set(pt.hp_label for pt in config.phenotype_thresholds))

    print(f"\n\n{'=' * 100}")
    print("GENE -> PHENOTYPE MATRIX")
    print(f"{'=' * 100}")

    print(f"\n{'Gene':<20}", end="")
    for hp in hp_labels:
        print(f"{hp[:18]:>20}", end="")
    print()
    print("-" * (20 + 20 * len(hp_labels)))

    for scenario_name, scenario in gene_scenarios.items():
        result = run_perturbation(
            config,
            gfr=scenario.get("gfr", 2.0),
            gene=scenario.get("gene"),
            effect=scenario.get("effect"),
            param_overrides=scenario.get("param_overrides"),
        )
        activated = evaluate_phenotypes(
            result.variables, baseline, config.phenotype_thresholds
        )
        activated_map = {a.hp_label: a.severity for a in activated}

        gene_label = scenario.get("gene", scenario_name)
        print(f"{gene_label:<20}", end="")
        for hp in hp_labels:
            if hp in activated_map:
                print(f"{'[' + activated_map[hp] + ']':>20}", end="")
            else:
                print(f"{'·':>20}", end="")
        print()


def main():
    app()


if __name__ == "__main__":
    main()
