"""Reproduce the FOXE3 tie and scoped counterfactuals without editing saved inputs."""

from __future__ import annotations

import argparse
import hashlib
import json
import signal
import subprocess
import sys
from copy import deepcopy
from math import isclose
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
BASE = HERE.parent

SOLVER = "744038e30741009930f57919ca2f03c6473ed198"
INPUT_SHA256 = "f701d83511d37b2fc769a9d2c090fc59e25faf1e3d8b7a9be686599e8015f154"


def main():
    sys.path.insert(0, str(BASE / "scripts"))
    from investigate_ties import enumerate_worlds

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--boomer-src", type=Path, required=True)
    parser.add_argument("--out", type=Path, default=HERE / "experiments.json")
    args = parser.parse_args()
    source = args.boomer_src.resolve()
    revision = subprocess.check_output(
        ["git", "-C", str(source), "rev-parse", "HEAD"], text=True
    ).strip()
    assert revision == SOLVER, revision
    assert not subprocess.check_output(
        ["git", "-C", str(source), "status", "--porcelain"], text=True
    ).strip(), "Use a clean solver checkout"
    sys.path.insert(0, str(source))
    from boomer import model
    from boomer.reasoners.nx_reasoner import NxReasoner

    assert Path(model.__file__).resolve().is_relative_to(source)
    folder = BASE / "disorders/FOXE3_Anterior_Segment_Dysgenesis"
    originals = {p: p.read_bytes() for p in folder.iterdir() if p.is_file()}
    input_bytes = originals[folder / "kb.yaml"]
    assert hashlib.sha256(input_bytes).hexdigest() == INPUT_SHA256
    data = yaml.safe_load(input_bytes)
    saved = yaml.safe_load(originals[folder / "solution.yaml"])
    metadata = json.loads(originals[folder / "solve.json"])
    assert metadata["input_sha256"] == INPUT_SHA256
    assert metadata["boomer_commit"] == SOLVER
    assert metadata["status"] == "RETRACTED" and metadata["solution_written"]
    assert not saved["timed_out"]
    assert data["pfacts"][6]["fact"]["equivalent"] == "icd11f:943599144"

    variants = {"saved_input": deepcopy(data)}
    broad = deepcopy(data)
    # The source change being proposed: MONDO is narrower than the ICD parent.
    broad["pfacts"][6]["fact"] = {
        "fact_type": "ProperSubClassOf",
        "sub": "MONDO:0019503",
        "sup": "icd11f:943599144",
    }
    variants["icd_parent_directional_at_same_prior"] = broad
    grounding = deepcopy(data)
    # Existing generator priors for an explicit skos:broadMatch to MONDO.
    for pf, prior in zip(grounding["pfacts"][:3], (0.05, 0.90, 0.03), strict=True):
        pf["prob"] = prior
    variants["dismech_broad_match_only"] = grounding
    both = deepcopy(broad)
    both["pfacts"][:3] = deepcopy(grounding["pfacts"][:3])
    variants["both_directional_changes"] = both
    dropped = deepcopy(data)
    # Current generator consumes MONDO exact matches, not every directional xref.
    del dropped["pfacts"][6]
    variants["exclude_parent_equivalence_only"] = dropped

    def expired(signum, frame):
        raise TimeoutError("FOXE3 enumeration exceeded 60 seconds")

    signal.signal(signal.SIGALRM, expired)
    results = {}
    for name, value in variants.items():
        signal.alarm(60)
        try:
            result = enumerate_worlds(
                model.KB.model_validate(value), model, NxReasoner()
            )
        finally:
            signal.alarm(0)
        results[name] = {"hypotheses": value["pfacts"], **result}
    baseline = results["saved_input"]
    assert baseline["confidence"] == saved["confidence"] == 0.5
    assert (
        baseline["distinct_solutions"]
        == saved["number_of_satisfiable_combinations"]
        == 48
    )
    assert isclose(baseline["best_posterior"], saved["posterior_prob"], abs_tol=1e-11)
    assert [p["truth_value"] for p in saved["solved_pfacts"]] in baseline[
        "optimal_assignments"
    ]
    for p, marginal in zip(saved["solved_pfacts"], baseline["marginals"], strict=True):
        assert isclose(p["posterior_prob"], marginal, abs_tol=1e-11)
    assert all(p.read_bytes() == content for p, content in originals.items())
    output = {
        "input_sha256": INPUT_SHA256,
        "solution_sha256": hashlib.sha256(
            originals[folder / "solution.yaml"]
        ).hexdigest(),
        "boomer_commit": revision,
        "timeout_seconds_per_scenario": 60,
        "method": "Exhaustive Boolean enumeration, each complete assignment counted once",
        "scope": "Counterfactuals on copies; production inputs and solutions unchanged",
        "scenarios": results,
    }
    args.out.write_text(json.dumps(output, indent=2) + "\n")
    for name, result in results.items():
        print(
            name,
            result["confidence"],
            result["distinct_solutions"],
            result["best_posterior"],
        )


if __name__ == "__main__":
    main()
