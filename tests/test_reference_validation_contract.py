"""Negative controls for the actual reference-validation gate (issue #7514).

Use the production shell wrapper, CLI, schema, and configuration. Only fetching
is replaced, with in-memory source records: no network access or hand-written
reference cache can accidentally make these tests pass.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest
import yaml
from linkml_reference_validator.cli.shared import load_validation_config
from linkml_reference_validator.models import ValidationSeverity

ROOT = Path(__file__).resolve().parents[1]
PRODUCTION_CONFIG = ROOT / "conf/reference_validator_config.yaml"
DEFAULT_CONFIG = ROOT / ".linkml-reference-validator.yaml"
SOURCE = "The treatment reduced the inflammatory response in affected cells."


@pytest.mark.parametrize("config_path", [PRODUCTION_CONFIG, DEFAULT_CONFIG])
def test_literature_references_cannot_be_exempted(config_path):
    """The test must fail if a future CI fix silently turns this gate off."""
    config = load_validation_config(config_path, load_custom_sources=False)
    skipped = {prefix.casefold() for prefix in config.skip_prefixes}
    assert not skipped.intersection({"doi", "pmid", "pmc", "ppr"})
    assert config.unknown_prefix_severity == ValidationSeverity.ERROR


def test_ci_runs_negative_controls_when_reference_policy_changes():
    workflow = yaml.safe_load((ROOT / ".github/workflows/main.yaml").read_text())
    steps = next(job["steps"] for job in workflow["jobs"].values() if "steps" in job)
    filters = yaml.safe_load(
        next(step["with"]["filters"] for step in steps if step.get("id") == "changes")
    )
    for path in (
        "conf/reference_validator_config.yaml",
        ".linkml-reference-validator.yaml",
        "scripts/run_reference_validator.sh",
        "src/**",
        "tests/**/*.py",
    ):
        assert path in filters["python"], (
            f"reference-policy changes must exercise the gate: {path}"
        )
    lane = next(step for step in steps if step.get("run") == "just test-python-code")
    assert "steps.changes.outputs.python" in lane["if"]


def test_default_snippet_audit_uses_the_production_prefix_policy():
    from dismech import reference_snippet_audit

    assert ROOT / reference_snippet_audit.DEFAULT_CONFIG == PRODUCTION_CONFIG
    config = load_validation_config(PRODUCTION_CONFIG, load_custom_sources=False)
    assert reference_snippet_audit.load_skip_prefixes(PRODUCTION_CONFIG) == {
        prefix.upper() for prefix in config.skip_prefixes
    }


@pytest.fixture
def run_gate(tmp_path):
    # Replace only `uv run python` with this test interpreter and deterministic
    # source fetching. The wrapper's Python code and exit-code handling both run
    # unchanged, including the compatibility patches and real validator CLI.
    fake_uv = tmp_path / "uv"
    fake_uv.write_text(
        f"#!{sys.executable}\n"
        "import json, os, socket, sys\n"
        "from pathlib import Path\n"
        "from linkml_reference_validator.etl.reference_fetcher import ReferenceFetcher\n"
        "from linkml_reference_validator.models import ReferenceContent\n"
        "def no_network(*args, **kwargs):\n"
        "    raise AssertionError('reference gate tests must stay offline')\n"
        "socket.socket.connect = no_network\n"
        "record = json.loads(os.environ['DISMECH_TEST_REFERENCE'])\n"
        "def fetch(self, reference_id, *args, **kwargs):\n"
        "    with Path(os.environ['DISMECH_TEST_FETCH_LOG']).open('a') as stream:\n"
        "        stream.write(reference_id + '\\n')\n"
        "    if record is None:\n"
        "        return None\n"
        "    return ReferenceContent(reference_id=reference_id, **record)\n"
        "ReferenceFetcher.fetch = fetch\n"
        "assert sys.argv[1:4] == ['run', 'python', '-c'], sys.argv\n"
        "code = sys.argv[4]\n"
        "sys.argv = ['python', *sys.argv[5:]]\n"
        "exec(compile(code, '<production-wrapper>', 'exec'))\n",
        encoding="utf-8",
    )
    fake_uv.chmod(0o755)

    def run(reference, snippet, record, *, explicit_config=True):
        entry = tmp_path / "entry.yaml"
        entry.write_text(
            json.dumps(
                {
                    "name": "Reference validation negative control",
                    "pathophysiology": [
                        {
                            "name": "Inflammatory response",
                            "evidence": [
                                {
                                    "reference": reference,
                                    "supports": "SUPPORT",
                                    "snippet": snippet,
                                }
                            ],
                        }
                    ],
                }
            ),
            encoding="utf-8",
        )
        fetch_log = tmp_path / "fetches.txt"
        command = [
            "bash",
            str(ROOT / "scripts/run_reference_validator.sh"),
            "validate",
            "data",
            str(entry),
            "--schema",
            str(ROOT / "src/dismech/schema/dismech.yaml"),
            "--target-class",
            "Disease",
            "--cache-dir",
            str(tmp_path / "unused-cache"),
            "--no-full-text",
        ]
        if explicit_config:
            command.extend(["--config", str(PRODUCTION_CONFIG)])
        env = {
            **os.environ,
            "PATH": f"{tmp_path}{os.pathsep}{os.environ['PATH']}",
            "PYTHONPATH": str(ROOT / "src"),
            "DISMECH_SKIP_SNIPPET_AUDIT": "1",
            "DISMECH_TEST_REFERENCE": json.dumps(record),
            "DISMECH_TEST_FETCH_LOG": str(fetch_log),
        }
        result = subprocess.run(
            command,
            cwd=ROOT,
            env=env,
            capture_output=True,
            text=True,
            check=False,
            timeout=60,
        )
        # A skipped prefix returns success without fetching at all. Assert that
        # both positive and negative controls actually reach source validation.
        assert fetch_log.exists(), result.stdout + result.stderr
        assert reference in fetch_log.read_text(encoding="utf-8").splitlines()
        assert "Traceback" not in result.stdout + result.stderr
        return result

    return run


@pytest.mark.parametrize(
    "explicit_config", [True, False], ids=["production", "default"]
)
@pytest.mark.parametrize(
    "reference", ["DOI:10.1000/control", "doi:10.1000/control", "PMID:1"]
)
@pytest.mark.parametrize(
    ("snippet", "valid"),
    [
        (SOURCE, True),
        ("The moon is made of green cheese.", False),
        (SOURCE.replace("reduced", "increased"), False),
    ],
    ids=["verbatim", "fabricated", "changed-result"],
)
def test_real_gate_checks_quotes(run_gate, explicit_config, reference, snippet, valid):
    result = run_gate(
        reference,
        snippet,
        {
            "title": "A controlled source",
            "content": SOURCE,
            "content_type": "abstract_only",
        },
        explicit_config=explicit_config,
    )
    assert (result.returncode == 0) is valid, result.stdout + result.stderr
    if not valid:
        assert "[ERROR]" in result.stdout


@pytest.mark.parametrize(
    "explicit_config", [True, False], ids=["production", "default"]
)
@pytest.mark.parametrize("reference", ["DOI:10.1000/control", "PMID:1"])
@pytest.mark.parametrize(
    "record",
    [None, {"title": "Metadata without source text", "content": None}],
    ids=["fetch-failed", "body-unavailable"],
)
def test_real_gate_fails_on_unverified_evidence(
    run_gate, explicit_config, reference, record
):
    result = run_gate(reference, SOURCE, record, explicit_config=explicit_config)
    assert result.returncode != 0, result.stdout + result.stderr
    assert "[ERROR]" in result.stdout
    assert (
        "Could not fetch reference" in result.stdout
        or "No content available" in result.stdout
    )
