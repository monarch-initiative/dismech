"""Validate local design fixtures without changing the production schema or KB.

Run from the repository root:
  uv run python docs/reports/senescent-cell-representation/validate_design.py

Derived schemas and candidate data live only in a temporary directory. This
checks structural expressibility and graph targets, not biological truth or
ontology/reference validity (run the separate recipes recorded in the note).
"""

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import tempfile

import yaml

from dismech.graph import build_causal_graph


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SCHEMA = ROOT / "src/dismech/schema/dismech.yaml"


def validate(
    schema: Path, data: Path, expect_valid: bool, expected_error: str = ""
) -> dict:
    command = ["linkml-validate", "-s", str(schema), "-C", "Disease", str(data)]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if (result.returncode == 0) != expect_valid:
        raise RuntimeError(
            f"Unexpected validation result: {command}\n{result.stdout}\n{result.stderr}"
        )
    output = (result.stdout + result.stderr).strip()
    if expected_error and expected_error not in output:
        raise RuntimeError(
            f"Expected rejection reason {expected_error!r} missing: {output}"
        )
    return {
        "data": data.name,
        "schema": "production" if schema == SCHEMA else "proposal",
        "expected_valid": expect_valid,
        "exit_code": result.returncode,
        "output": output.replace(str(data.parent) + "/", "")
        if schema != SCHEMA or not expect_valid
        else output,
    }


def main() -> None:
    schema = yaml.safe_load(SCHEMA.read_text())
    delta = yaml.safe_load((HERE / "extension-delta.yaml").read_text())
    for name, definition in delta["classes"].items():
        if name in schema["classes"]:
            schema["classes"][name].setdefault("attributes", {}).update(
                definition["attributes"]
            )
        else:
            schema["classes"][name] = definition
    schema["enums"].update(delta["enums"])
    # Resolve the production schema's relative imports before placing the clone
    # outside its directory. LinkML's own prefixed import remains unchanged.
    schema["imports"] = [
        value if ":" in value else str(SCHEMA.parent / value)
        for value in schema["imports"]
    ]
    results = []
    with tempfile.TemporaryDirectory(prefix="dismech-senescence-design-") as tmp:
        tmpdir = Path(tmp)
        proposal = tmpdir / "proposal.yaml"
        proposal.write_text(yaml.safe_dump(schema, sort_keys=False))
        for name in ["existing-schema.yaml", "wound-context.yaml"]:
            path = HERE / name
            results.append(validate(SCHEMA, path, True))
            results.append(validate(proposal, path, True))
            graph = build_causal_graph(yaml.safe_load(path.read_text()))
            if graph.orphan_targets:
                raise RuntimeError(
                    f"Dangling graph targets in {name}: {graph.orphan_targets}"
                )
            results.append(
                {"data": name, "orphan_targets": [], "graph_edges": len(graph.edges)}
            )

        candidate = yaml.safe_load((HERE / "existing-schema.yaml").read_text())
        node = candidate["pathophysiology"][0]
        cell = node["cell_types"][0]
        cell["preferred_term"] = cell["term"]["label"]
        cell["cell_states"] = [
            {
                "state": "SENESCENT",
                "description": "The source identifies experimentally senescent dermal fibroblasts; "
                "HLA-E alone is not the basis for the state assignment. "
                "See the source's Figure 1 and accompanying marker assessment.",
                "evidence": node.pop("evidence"),
            }
        ]
        candidate_path = tmpdir / "candidate-state.yaml"
        candidate_path.write_text(
            yaml.safe_dump(candidate, sort_keys=False, allow_unicode=True)
        )
        results.append(validate(proposal, candidate_path, True))
        results.append(
            validate(SCHEMA, candidate_path, False, "'cell_states' was unexpected")
        )

        unsupported = deepcopy(candidate)
        unsupported["pathophysiology"][0]["cell_types"][0]["cell_states"][0][
            "state"
        ] = "EXHAUSTED"
        unsupported_path = tmpdir / "unsupported-state.yaml"
        unsupported_path.write_text(yaml.safe_dump(unsupported, sort_keys=False))
        results.append(
            validate(proposal, unsupported_path, False, "'EXHAUSTED' is not one of")
        )

        unsupported = deepcopy(candidate)
        unsupported["pathophysiology"][0]["cell_types"][0]["cell_states"][0][
            "evidence"
        ] = []
        unsupported_path = tmpdir / "missing-state-evidence.yaml"
        unsupported_path.write_text(yaml.safe_dump(unsupported, sort_keys=False))
        results.append(
            validate(proposal, unsupported_path, False, "[] should be non-empty")
        )
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
