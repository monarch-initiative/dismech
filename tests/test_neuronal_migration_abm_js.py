"""The browser port of the neuronal-migration ABM must reproduce run.py exactly.

``models/neuronal_migration_abm/run.js`` is inlined into the model's generated
page (``pages/models/neuronal_migration_abm.html``) so a reader can replay a
scenario agent by agent and rerun it with other parameters (#13123). The page
presents that replay as the model's run, which is only true if the port makes
the same draws and computes the same readouts. These tests hold it to that:
the whole ``results.json`` and a scenario's per-step trace must come out equal,
not merely close.

Skipped when ``node`` is not installed; GitHub's Ubuntu runners ship it.
"""

from __future__ import annotations

import hashlib
import json
import random
import shutil
import subprocess
from pathlib import Path

import pytest
import yaml

from tests.test_neuronal_migration_abm import RESULTS_PATH, SPEC_PATH, load_runner

REPO_ROOT = Path(__file__).resolve().parents[1]
JS_PATH = REPO_ROOT / "models" / "neuronal_migration_abm" / "run.js"
NODE = shutil.which("node")

pytestmark = pytest.mark.skipif(NODE is None, reason="node is not installed")


def run_node(script: str, payload: object) -> object:
    """Run ``script`` with the port loaded as ``m`` and ``input`` bound to payload."""
    program = (
        f"const m = require({json.dumps(str(JS_PATH))});\n"
        "const input = JSON.parse(require('fs').readFileSync(0, 'utf8'));\n"
        f"process.stdout.write(JSON.stringify(({script})));\n"
    )
    proc = subprocess.run(
        [NODE, "-e", program],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
        check=False,
        timeout=120,
    )
    assert proc.returncode == 0, proc.stderr
    return json.loads(proc.stdout)


@pytest.fixture(scope="module")
def spec() -> dict:
    return yaml.safe_load(SPEC_PATH.read_text())


def test_port_reproduces_committed_results(spec: dict) -> None:
    committed = json.loads(RESULTS_PATH.read_text())
    assert run_node("m.buildResults(input)", spec) == committed


def test_port_reproduces_a_scenario_trace(spec: dict) -> None:
    """The replay frames match run.py's --trace, not just the end state."""
    runner = load_runner()
    name = "mosaic_severe"
    params = runner.Params.from_mapping(
        spec["scenarios"][name], runner.input_defaults(spec)
    )
    trace: dict = {}
    readouts = runner.simulate(spec, params, f"scenario:{name}", trace=trace)
    js = run_node(
        "(() => { const t = {}; const d = m.inputDefaults(input.spec);"
        " const r = m.simulate(input.spec, m.paramsFrom(input.scenario, d),"
        " input.run, t); return {trace: t, readouts: r}; })()",
        {"spec": spec, "scenario": spec["scenarios"][name], "run": f"scenario:{name}"},
    )
    assert js["readouts"] == readouts
    assert js["trace"] == json.loads(json.dumps(trace))


@pytest.mark.parametrize(
    "text", ["", "abc", "20260925:sweep:rescue_severe:0.6", "é" * 200]
)
def test_sha512_matches_hashlib(text: str) -> None:
    got = run_node(
        "Buffer.from(m.sha512(new TextEncoder().encode(input))).toString('hex')", text
    )
    assert got == hashlib.sha512(text.encode()).hexdigest()


@pytest.mark.parametrize("seed", ["x", "20260925:scenario:wild_type", "ünïcode"])
def test_random_matches_cpython(seed: str) -> None:
    rng = random.Random(seed)
    expected = [rng.random() for _ in range(2000)]
    got = run_node(
        "(() => { const r = new m.PyRandom(input); "
        "return Array.from({length: 2000}, () => r.random()); })()",
        seed,
    )
    assert got == expected


def test_round_matches_cpython() -> None:
    # Exact binary ties (half-even), values just off a tie, and ordinary values.
    cases = [
        (0.125, 2),
        (0.375, 2),
        (2.675, 2),
        (0.5, 0),
        (1.5, 0),
        (2.5, 0),
        (0.74583333, 4),
        (-0.125, 2),
        (1e-7, 4),
        (123.456789, 2),
        (0.0, 4),
        (5 / 6, 4),
        (1 / 3, 1),
        (99.95, 1),
    ]
    got = run_node("input.map(([x, n]) => m.pyRound(x, n))", cases)
    assert got == [round(x, n) for x, n in cases]
