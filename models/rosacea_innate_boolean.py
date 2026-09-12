#!/usr/bin/env python3
"""Run the rosacea innate-immune Boolean model.

Reads ``models/rosacea_innate_boolean.yaml``, simulates each scenario to its
attractor under synchronous update, scans single and paired interventions, and
writes a deterministic JSON result file.

This model is authored in this repository, not taken from a publication, and it
is NOT wired to ``dismech-perturb``: that runner executes SBML through tellurium
and cannot run a logical network. Nothing here is fitted to data - the rules are
a transcription of causal edges curated in ``kb/disorders/Rosacea.yaml``, so the
output says what those edges imply, not what the disease does.

Usage::

    python models/rosacea_innate_boolean.py            # write the committed results
    python models/rosacea_innate_boolean.py --check    # verify committed results are current
    python models/rosacea_innate_boolean.py --print    # human-readable summary

Requires only the standard library plus PyYAML.
"""
from __future__ import annotations

import argparse
import itertools
import json
import pathlib
import sys

import yaml

HERE = pathlib.Path(__file__).resolve().parent
SPEC_PATH = HERE / "rosacea_innate_boolean.yaml"
RESULTS_PATH = HERE / "rosacea_innate_boolean.results.json"
MAX_STEPS = 64


# ---------------------------------------------------------------------------
# A tiny parser for the rule language: names, and, or, not, parentheses.
# Deliberately not eval(): the grammar is three operators wide and a committed
# scientific artifact should not carry an interpreter escape hatch.
# ---------------------------------------------------------------------------
def tokenize(rule: str) -> list[str]:
    tokens: list[str] = []
    buf = ""
    for ch in rule:
        if ch in "()":
            if buf:
                tokens.append(buf)
                buf = ""
            tokens.append(ch)
        elif ch.isspace():
            if buf:
                tokens.append(buf)
                buf = ""
        else:
            buf += ch
    if buf:
        tokens.append(buf)
    return tokens


class Parser:
    def __init__(self, tokens: list[str], rule: str) -> None:
        self.tokens = tokens
        self.pos = 0
        self.rule = rule

    def peek(self) -> str | None:
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def take(self) -> str:
        token = self.tokens[self.pos]
        self.pos += 1
        return token

    def parse(self):
        node = self.parse_or()
        if self.pos != len(self.tokens):
            raise ValueError(f"trailing tokens in rule {self.rule!r}")
        return node

    def parse_or(self):
        node = self.parse_and()
        while self.peek() == "or":
            self.take()
            node = ("or", node, self.parse_and())
        return node

    def parse_and(self):
        node = self.parse_not()
        while self.peek() == "and":
            self.take()
            node = ("and", node, self.parse_not())
        return node

    def parse_not(self):
        if self.peek() == "not":
            self.take()
            return ("not", self.parse_not())
        return self.parse_atom()

    def parse_atom(self):
        token = self.peek()
        if token is None:
            raise ValueError(f"unexpected end of rule {self.rule!r}")
        if token == "(":
            self.take()
            node = self.parse_or()
            if self.peek() != ")":
                raise ValueError(f"unbalanced parentheses in rule {self.rule!r}")
            self.take()
            return node
        if token in {"and", "or", "not", ")"}:
            raise ValueError(f"unexpected {token!r} in rule {self.rule!r}")
        return ("var", self.take())


def parse_rule(rule: str):
    return Parser(tokenize(rule), rule).parse()


def evaluate(node, state: dict[str, bool]) -> bool:
    kind = node[0]
    if kind == "var":
        name = node[1]
        if name not in state:
            raise KeyError(f"rule references unknown node {name!r}")
        return state[name]
    if kind == "not":
        return not evaluate(node[1], state)
    if kind == "and":
        return evaluate(node[1], state) and evaluate(node[2], state)
    if kind == "or":
        return evaluate(node[1], state) or evaluate(node[2], state)
    raise ValueError(f"bad node {node!r}")


# ---------------------------------------------------------------------------
# Model
# ---------------------------------------------------------------------------
class BooleanModel:
    def __init__(self, spec: dict) -> None:
        self.spec = spec
        self.inputs = sorted(spec["inputs"])
        self.interventions = sorted(spec["interventions"])
        computed = {}
        for section in ("rules", "outputs"):
            for name, body in spec[section].items():
                computed[name] = parse_rule(body["rule"])
        self.computed_names = sorted(computed)
        self.computed = computed
        self.output_names = sorted(spec["outputs"])
        # Intervention targets are asserted false when the intervention is on.
        self.blocks = {name: body["inhibits"] for name, body in spec["interventions"].items()}

    def initial_state(self, active_inputs, active_interventions) -> dict[str, bool]:
        state = {name: name in set(active_inputs) for name in self.inputs}
        state.update({name: name in set(active_interventions) for name in self.interventions})
        state.update({name: False for name in self.computed_names})
        return state

    def step(self, state: dict[str, bool]) -> dict[str, bool]:
        new = dict(state)
        for name in self.computed_names:
            new[name] = evaluate(self.computed[name], state)
        # An intervention that names a node it does not gate inside a rule
        # (Acaricide -> Demodex, an input) is applied here.
        for intervention, target in self.blocks.items():
            if state.get(intervention) and target in new:
                new[target] = False
        return new

    def run(self, active_inputs, active_interventions=()):
        state = self.initial_state(active_inputs, active_interventions)
        # Interventions that block an input must apply from the first step.
        for intervention, target in self.blocks.items():
            if state.get(intervention) and target in state:
                state[target] = False
        seen: dict[tuple, int] = {}
        trajectory = []
        for step in range(MAX_STEPS):
            key = tuple(sorted(state.items()))
            if key in seen:
                cycle = trajectory[seen[key]:]
                return {
                    "attractor_type": "fixed_point" if len(cycle) == 1 else "cycle",
                    "cycle_length": len(cycle),
                    "steps_to_attractor": seen[key],
                    "state": dict(sorted(cycle[0].items())),
                }
            seen[key] = step
            trajectory.append(dict(state))
            state = self.step(state)
        raise RuntimeError("no attractor reached within MAX_STEPS")

    def active_outputs(self, state) -> list[str]:
        return [name for name in self.output_names if state[name]]


def build_results(model: BooleanModel) -> dict:
    spec = model.spec
    results: dict = {
        "model_id": spec["model_id"],
        "name": spec["name"],
        "formalism": spec["formalism"],
        "source_entry": spec["source_entry"],
        "provenance": {
            "generator": "models/rosacea_innate_boolean.py",
            "spec": "models/rosacea_innate_boolean.yaml",
            "note": (
                "Repository-authored model, not a published one, and not run by "
                "dismech-perturb. Rules transcribe curated causal edges; nothing "
                "is fitted to data."
            ),
        },
        "scenarios": {},
        "intervention_scan": {},
    }

    for key, scenario in spec["scenarios"].items():
        run = model.run(scenario.get("active_inputs") or [])
        results["scenarios"][key] = {
            "label": scenario["label"],
            "active_inputs": sorted(scenario.get("active_inputs") or []),
            "attractor_type": run["attractor_type"],
            "steps_to_attractor": run["steps_to_attractor"],
            "active_phenotypes": model.active_outputs(run["state"]),
            "state": run["state"],
        }

    scan_key = spec["intervention_scan_scenario"]
    scan_inputs = spec["scenarios"][scan_key]["active_inputs"]
    baseline = model.run(scan_inputs)
    baseline_active = model.active_outputs(baseline["state"])
    combos: list[tuple[str, ...]] = [()]
    combos += [(name,) for name in model.interventions]
    combos += list(itertools.combinations(model.interventions, 2))
    combos.append(tuple(model.interventions))

    scan = {}
    for combo in combos:
        run = model.run(scan_inputs, combo)
        active = model.active_outputs(run["state"])
        scan["+".join(combo) if combo else "none"] = {
            "interventions": list(combo),
            "active_phenotypes": active,
            "cleared": [p for p in baseline_active if p not in active],
            "persisting": [p for p in baseline_active if p in active],
        }
    results["intervention_scan"] = {
        "scenario": scan_key,
        "baseline_active_phenotypes": baseline_active,
        "results": scan,
    }
    return results


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=pathlib.Path, default=RESULTS_PATH)
    ap.add_argument("--check", action="store_true", help="fail if committed results are stale")
    ap.add_argument("--print", dest="show", action="store_true", help="print a summary")
    args = ap.parse_args()

    spec = yaml.safe_load(SPEC_PATH.read_text())
    model = BooleanModel(spec)
    results = build_results(model)

    # Sanity check: with no active input the network must be silent.
    healthy = results["scenarios"]["healthy"]["active_phenotypes"]
    if healthy:
        raise AssertionError(f"healthy scenario is not silent: {healthy}")

    payload = json.dumps(results, indent=2, sort_keys=True) + "\n"

    if args.check:
        if not args.output.exists():
            print(f"missing {args.output}", file=sys.stderr)
            return 1
        if args.output.read_text() != payload:
            print(f"{args.output} is stale; re-run {pathlib.Path(__file__).name}", file=sys.stderr)
            return 1
        print(f"{args.output} is current")
        return 0

    args.output.write_text(payload)
    print(f"wrote {args.output}")

    if args.show:
        for key, scenario in results["scenarios"].items():
            active = ", ".join(scenario["active_phenotypes"]) or "none"
            print(f"\n{scenario['label']}\n  phenotypes: {active}")
        scan = results["intervention_scan"]
        print(f"\nIntervention scan on '{scan['scenario']}' "
              f"(baseline: {', '.join(scan['baseline_active_phenotypes'])})")
        for name, row in scan["results"].items():
            persisting = ", ".join(row["persisting"]) or "none"
            print(f"  {name:45} persisting: {persisting}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
