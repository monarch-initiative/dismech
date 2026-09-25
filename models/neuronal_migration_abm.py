#!/usr/bin/env python3
"""Run the microtubule-dependent radial neuronal migration agent-based model.

Reads ``models/neuronal_migration_abm.yaml``, simulates each scenario and
parameter sweep on a one-dimensional cortical column, and writes a
deterministic JSON result file.

This model is authored in this repository, not taken from a publication, and it
is NOT wired to ``dismech-perturb``: that runner executes SBML through tellurium
and cannot run an agent-based simulation. Nothing here is fitted to data - the
rules are a transcription of the causal chain curated in
``kb/modules/microtubule_dependent_neuronal_migration_failure.yaml``, so the
output says what that chain implies under placeholder rates, not what any
disease does.

Usage::

    python models/neuronal_migration_abm.py            # write the committed results
    python models/neuronal_migration_abm.py --check    # verify committed results are current
    python models/neuronal_migration_abm.py --print    # human-readable summary

Requires only the standard library plus PyYAML. Every random draw comes from a
``random.Random`` seeded with a string, which PyYAML-independent CPython hashes
with SHA-512, so the committed results are reproducible across platforms.
"""

from __future__ import annotations

import argparse
import bisect
import json
import pathlib
import random
import statistics
import sys
from dataclasses import dataclass, field

import yaml

HERE = pathlib.Path(__file__).resolve().parent
SPEC_PATH = HERE / "neuronal_migration_abm.yaml"
RESULTS_PATH = HERE / "neuronal_migration_abm.results.json"

# Thresholds that turn readouts into the `pattern` label. Stated here, and
# copied into the results file, so a reader can see exactly what each label
# means without opening the runner.
PATTERN_THRESHOLDS = {
    "normal_min_plate_fraction": 0.95,
    "normal_min_lamination_fidelity": 0.95,
    "band_min_affected_arrested_fraction": 0.5,
    "band_min_unaffected_plate_fraction": 0.9,
    "band_min_band_score": 0.6,
    "failure_max_plate_fraction": 0.5,
    "band_half_width": 5.0,
}

INPUT_DEFAULTS = {
    "perturbation": 0.0,
    "affected_fraction": 0.0,
    "base_motility": 0.8,
    "arrest_rate": 0.0,
    "rescue": 0.0,
}


@dataclass
class Params:
    perturbation: float = 0.0
    affected_fraction: float = 0.0
    base_motility: float = 0.8
    arrest_rate: float = 0.0
    rescue: float = 0.0

    @classmethod
    def from_mapping(cls, mapping: dict, defaults: dict) -> "Params":
        values = dict(defaults)
        values.update({k: v for k, v in mapping.items() if k in values})
        return cls(**values)

    def as_dict(self) -> dict:
        return {
            "perturbation": self.perturbation,
            "affected_fraction": self.affected_fraction,
            "base_motility": self.base_motility,
            "arrest_rate": self.arrest_rate,
            "rescue": self.rescue,
        }


@dataclass
class Neuron:
    cohort: int
    affected: bool
    birth_time: int
    position: float
    state: str = "migrating"  # migrating | arrested | settled
    settle_rank: int = -1
    arrival_time: int = -1
    ever_left_iz: bool = False


@dataclass
class Column:
    """The cortical column: zone geometry plus the growing cortical plate."""

    vz_top: float
    plate_floor: float
    pia: float
    step_length: float
    settled_cell_thickness: float
    birth_position: float
    plate_top: float = field(init=False)
    n_settled: int = field(init=False, default=0)

    def __post_init__(self) -> None:
        self.plate_top = self.plate_floor

    def zone(self, position: float) -> str:
        if position < self.vz_top:
            return "ventricular_zone"
        if position < self.plate_floor:
            return "intermediate_zone"
        return "cortical_plate"


def load_spec(path: pathlib.Path = SPEC_PATH) -> dict:
    return yaml.safe_load(path.read_text())


def input_defaults(spec: dict) -> dict:
    defaults = dict(INPUT_DEFAULTS)
    for name, body in spec["inputs"].items():
        if isinstance(body, dict) and "default" in body:
            defaults[name] = body["default"]
    return defaults


def simulate(spec: dict, params: Params, run_name: str) -> dict:
    """Simulate one parameter set and return its readouts."""
    dom = spec["domain"]
    cohorts = spec["cohorts"]
    column = Column(
        vz_top=float(dom["ventricular_zone_top"]),
        plate_floor=float(dom["cortical_plate_floor"]),
        pia=float(dom["pia"]),
        step_length=float(dom["step_length"]),
        settled_cell_thickness=float(dom["settled_cell_thickness"]),
        birth_position=float(dom["birth_position"]),
    )
    rng = random.Random(f"{spec['seed']}:{run_name}")

    n_cohorts = int(cohorts["count"])
    cohort_size = int(cohorts["size"])
    interval = int(cohorts["birth_interval"])
    last_birth = (n_cohorts - 1) * interval
    t_end = last_birth + int(cohorts["migration_window"])

    neurons: list[Neuron] = []
    for cohort in range(n_cohorts):
        for _ in range(cohort_size):
            affected = rng.random() < params.affected_fraction
            neurons.append(
                Neuron(
                    cohort=cohort,
                    affected=affected,
                    birth_time=cohort * interval,
                    position=column.birth_position,
                )
            )

    # Rules, applied per agent per step in the order the spec lists them.
    for t in range(t_end + 1):
        for n in neurons:
            if n.state != "migrating" or n.birth_time > t:
                continue
            # effective_perturbation
            e = params.perturbation * (1.0 - params.rescue) if n.affected else 0.0
            # arrest: confined to the intermediate zone
            if (
                params.arrest_rate > 0
                and e > 0
                and column.zone(n.position) == "intermediate_zone"
                and rng.random() < params.arrest_rate * e
            ):
                n.state = "arrested"
                continue
            # slowed_nucleokinesis
            if rng.random() < params.base_motility * (1.0 - e):
                n.position = min(n.position + column.step_length, column.pia)
            # inside_out_settling
            if n.position >= column.plate_top:
                n.state = "settled"
                n.settle_rank = column.n_settled
                n.arrival_time = t
                column.n_settled += 1
                column.plate_top = (
                    column.plate_floor
                    + column.settled_cell_thickness * column.n_settled
                )

    return score(neurons, column, n_cohorts, t_end)


def lamination_fidelity(settled: list[Neuron], n_cohorts: int) -> float | None:
    """Fraction of cross-cohort settled pairs in inside-out order.

    For cohorts a < b, a pair is concordant when the later-born neuron settled
    above the earlier-born one (higher settle_rank). Computed per cohort pair
    with a sorted list and bisect, so it is O(n log n) rather than O(n^2).
    """
    ranks_by_cohort: list[list[int]] = [[] for _ in range(n_cohorts)]
    for n in settled:
        ranks_by_cohort[n.cohort].append(n.settle_rank)
    for ranks in ranks_by_cohort:
        ranks.sort()
    concordant = 0
    total = 0
    for a in range(n_cohorts):
        for b in range(a + 1, n_cohorts):
            earlier = ranks_by_cohort[a]
            later = ranks_by_cohort[b]
            if not earlier or not later:
                continue
            for r in later:
                concordant += bisect.bisect_left(earlier, r)
            total += len(earlier) * len(later)
    if total == 0:
        return None
    return concordant / total


def score(neurons: list[Neuron], column: Column, n_cohorts: int, t_end: int) -> dict:
    total = len(neurons)
    settled = [n for n in neurons if n.state == "settled"]
    arrested = [n for n in neurons if n.state == "arrested"]
    in_transit = [n for n in neurons if n.state == "migrating"]
    ectopic = arrested + in_transit

    zone_counts = {"ventricular_zone": 0, "intermediate_zone": 0, "cortical_plate": 0}
    for n in ectopic:
        zone_counts[column.zone(n.position)] += 1

    affected = [n for n in neurons if n.affected]
    unaffected = [n for n in neurons if not n.affected]

    def plate_fraction(group: list[Neuron]) -> float | None:
        if not group:
            return None
        return sum(1 for n in group if n.state == "settled") / len(group)

    affected_ectopic = [n for n in affected if n.state != "settled"]
    affected_arrested = [n for n in affected if n.state == "arrested"]
    band_score = None
    band_median_depth = None
    if affected_arrested:
        depths = sorted(n.position for n in affected_arrested)
        band_median_depth = statistics.median(depths)
        half = PATTERN_THRESHOLDS["band_half_width"]
        band_score = sum(1 for d in depths if abs(d - band_median_depth) <= half) / len(
            depths
        )

    fidelity = lamination_fidelity(settled, n_cohorts)
    delays = [n.arrival_time - n.birth_time for n in settled]
    per_cohort_plate_fraction = []
    for c in range(n_cohorts):
        members = [n for n in neurons if n.cohort == c]
        per_cohort_plate_fraction.append(round(plate_fraction(members) or 0.0, 4))

    readouts = {
        "cortical_plate_fraction": round(len(settled) / total, 4),
        "ectopic_fraction": round(len(ectopic) / total, 4),
        "arrested_fraction": round(len(arrested) / total, 4),
        "in_transit_fraction": round(len(in_transit) / total, 4),
        "ectopic_by_zone": {k: round(v / total, 4) for k, v in zone_counts.items()},
        "lamination_fidelity": None if fidelity is None else round(fidelity, 4),
        "mean_arrival_delay": None
        if not delays
        else round(statistics.fmean(delays), 2),
        "cortical_plate_thickness": round(
            column.settled_cell_thickness * len(settled), 2
        ),
        "per_cohort_plate_fraction": per_cohort_plate_fraction,
        "affected_plate_fraction": None
        if not affected
        else round(plate_fraction(affected), 4),
        "unaffected_plate_fraction": None
        if not unaffected
        else round(plate_fraction(unaffected), 4),
        "affected_ectopic_fraction": None
        if not affected
        else round(len(affected_ectopic) / len(affected), 4),
        "affected_arrested_fraction": None
        if not affected
        else round(len(affected_arrested) / len(affected), 4),
        "band_score": None if band_score is None else round(band_score, 4),
        "band_median_depth": None
        if band_median_depth is None
        else round(band_median_depth, 2),
        "window_end": t_end,
    }
    readouts["pattern"] = classify(readouts)
    return readouts


def classify(r: dict) -> str:
    th = PATTERN_THRESHOLDS
    plate = r["cortical_plate_fraction"]
    fidelity = r["lamination_fidelity"] if r["lamination_fidelity"] is not None else 0.0
    if (
        plate >= th["normal_min_plate_fraction"]
        and fidelity >= th["normal_min_lamination_fidelity"]
    ):
        return "normal"
    if (
        r["affected_arrested_fraction"] is not None
        and r["unaffected_plate_fraction"] is not None
        and r["band_score"] is not None
        and r["affected_arrested_fraction"] >= th["band_min_affected_arrested_fraction"]
        and r["unaffected_plate_fraction"] >= th["band_min_unaffected_plate_fraction"]
        and r["band_score"] >= th["band_min_band_score"]
    ):
        return "band_heterotopia"
    if plate < th["failure_max_plate_fraction"]:
        return "migration_failure"
    if plate >= th["normal_min_plate_fraction"]:
        return "delayed_lamination"
    return "diffuse_ectopia"


def build_results(spec: dict) -> dict:
    defaults = input_defaults(spec)
    scenarios = {}
    for name, body in spec["scenarios"].items():
        params = Params.from_mapping(body, defaults)
        scenarios[name] = {
            "description": body.get("description", ""),
            "params": params.as_dict(),
            "readouts": simulate(spec, params, f"scenario:{name}"),
        }
    sweeps = {}
    for name, body in spec["sweeps"].items():
        rows = []
        for value in body["values"]:
            mapping = dict(body.get("fixed", {}))
            mapping[body["vary"]] = value
            params = Params.from_mapping(mapping, defaults)
            readouts = simulate(spec, params, f"sweep:{name}:{value}")
            rows.append(
                {
                    body["vary"]: value,
                    "cortical_plate_fraction": readouts["cortical_plate_fraction"],
                    "arrested_fraction": readouts["arrested_fraction"],
                    "in_transit_fraction": readouts["in_transit_fraction"],
                    "lamination_fidelity": readouts["lamination_fidelity"],
                    "mean_arrival_delay": readouts["mean_arrival_delay"],
                    "band_score": readouts["band_score"],
                    "affected_arrested_fraction": readouts[
                        "affected_arrested_fraction"
                    ],
                    "unaffected_plate_fraction": readouts["unaffected_plate_fraction"],
                    "pattern": readouts["pattern"],
                }
            )
        sweeps[name] = {
            "vary": body["vary"],
            "fixed": body.get("fixed", {}),
            "rows": rows,
        }
    return {
        "model_id": spec["model_id"],
        "source_entry": spec["source_entry"],
        "seed": spec["seed"],
        "pattern_thresholds": PATTERN_THRESHOLDS,
        "scenarios": scenarios,
        "sweeps": sweeps,
    }


def render(results: dict) -> str:
    lines = [f"{results['model_id']}  (seed {results['seed']})", ""]
    lines.append("Scenarios:")
    for name, body in results["scenarios"].items():
        r = body["readouts"]
        lines.append(
            f"  {name:32s} plate={r['cortical_plate_fraction']:.2f} arrested={r['arrested_fraction']:.2f} "
            f"in_transit={r['in_transit_fraction']:.2f} fidelity={r['lamination_fidelity']} "
            f"delay={r['mean_arrival_delay']} band={r['band_score']}  -> {r['pattern']}"
        )
    for name, sweep in results["sweeps"].items():
        lines.append("")
        lines.append(f"Sweep {name} (vary {sweep['vary']}, fixed {sweep['fixed']}):")
        for row in sweep["rows"]:
            lines.append(
                f"  {sweep['vary']}={row[sweep['vary']]:<5} plate={row['cortical_plate_fraction']:.2f} "
                f"arrested={row['arrested_fraction']:.2f} transit={row['in_transit_fraction']:.2f} "
                f"fidelity={row['lamination_fidelity']} delay={row['mean_arrival_delay']} "
                f"band={row['band_score']} -> {row['pattern']}"
            )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--check", action="store_true", help="exit 1 if the committed results are stale"
    )
    parser.add_argument(
        "--print", action="store_true", help="print a human-readable summary"
    )
    args = parser.parse_args(argv)

    spec = load_spec()
    results = build_results(spec)
    payload = json.dumps(results, indent=2, sort_keys=True) + "\n"

    if args.print:
        print(render(results))
        return 0
    if args.check:
        if not RESULTS_PATH.exists() or RESULTS_PATH.read_text() != payload:
            print(
                f"{RESULTS_PATH.relative_to(HERE.parent)} is stale; re-run this script",
                file=sys.stderr,
            )
            return 1
        print("results are current")
        return 0
    RESULTS_PATH.write_text(payload)
    print(f"wrote {RESULTS_PATH.relative_to(HERE.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
