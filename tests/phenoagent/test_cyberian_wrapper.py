"""Tests for cyberian wrapper orchestration."""

from pathlib import Path
import re
import sys

from cyberian.models import Task
import yaml

from phenoagent import cyberian_wrapper


def test_build_cyberian_workflow_command_core_flags(tmp_path: Path):
    workflow_file = tmp_path / "workflow.yaml"
    workflow_file.write_text("name: test\n")
    matching_file = tmp_path / "matching.yaml"
    matching_file.write_text("matches: []\n")
    workdir = tmp_path / "workdir"
    workdir.mkdir()

    cmd = cyberian_wrapper.build_cyberian_workflow_command(
        workflow_file=workflow_file,
        matching_file=matching_file,
        workdir=workdir,
        agent_type="claude",
        agent_lifecycle="refresh",
        verbosity=2,
    )

    assert cmd[:4] == [sys.executable, "-m", "cyberian.cli", "workflow"]
    assert "run" in cmd
    assert str(workflow_file) in cmd
    assert "--workdir" in cmd and str(workdir) in cmd
    assert "--agent-type" in cmd and "claude" in cmd
    assert "--agent-lifecycle" in cmd and "refresh" in cmd
    assert "--skip-permissions" in cmd
    assert "--param" in cmd
    assert f"matching_file={matching_file}" in cmd
    assert cmd.count("-v") == 2


def test_run_matching_explanation_agent_dry_run(tmp_path: Path, monkeypatch):
    workflow_file = tmp_path / "workflow.yaml"
    workflow_file.write_text("name: test\n")
    monkeypatch.setattr(cyberian_wrapper, "WORKFLOW_FILE", workflow_file)

    output_file = tmp_path / "matching.yaml"
    output_file.write_text("matches: []\npr_is_diagnosis: 0.42\n")

    def fake_create_initial_matching_file(*args, **kwargs):
        return output_file

    def fail_subprocess_run(*args, **kwargs):
        raise AssertionError("subprocess.run should not be called in dry-run mode")

    expected_workdir = tmp_path / "workdirs" / "matching" / "case_001" / "Fanconi_Anemia" / "deadbeef"
    monkeypatch.setattr(cyberian_wrapper, "create_initial_matching_file", fake_create_initial_matching_file)
    monkeypatch.setattr(cyberian_wrapper, "_default_matching_workdir", lambda _: expected_workdir)
    monkeypatch.setattr(cyberian_wrapper.subprocess, "run", fail_subprocess_run)

    result = cyberian_wrapper.run_matching_explanation_agent(
        phenopacket_path=tmp_path / "input.json",
        disease_reference="Fanconi_Anemia",
        dry_run=True,
    )

    assert result.matching_file == output_file.resolve()
    assert result.workdir == expected_workdir.resolve()
    assert result.pr_is_diagnosis == 0.42
    assert expected_workdir.exists()


def test_default_matching_workdir_shape(tmp_path: Path):
    matching_file = tmp_path / "matching.yaml"
    matching_file.write_text(
        yaml.safe_dump(
            {
                "case_id": "PMID_28757203_Individual_3_P3",
                "disease_slug": "Fanconi_Anemia",
                "matches": [],
            },
            sort_keys=False,
        )
    )

    workdir = cyberian_wrapper._default_matching_workdir(matching_file, root_dir=tmp_path)
    rel = workdir.relative_to(tmp_path)
    rel_str = rel.as_posix()
    assert re.fullmatch(
        r"workdirs/matching/PMID_28757203_Individual_3_P3/Fanconi_Anemia/[0-9a-f]{8}",
        rel_str,
    )


def test_workflow_yaml_is_valid_cyberian_task():
    workflow_file = cyberian_wrapper.WORKFLOW_FILE
    assert workflow_file.exists()
    data = yaml.safe_load(workflow_file.read_text())
    task = Task(**data)
    assert task.name == "phenoagent_explanation_completion"
    assert task.loop_until is not None
    assert task.loop_until.status == "EXPLANATIONS_COMPLETE"


def test_workflow_success_criteria_runs_in_restricted_namespace(tmp_path: Path):
    workflow_file = cyberian_wrapper.WORKFLOW_FILE
    data = yaml.safe_load(workflow_file.read_text())
    task = Task(**data)
    assert task.success_criteria is not None
    assert task.success_criteria.python is not None

    matching_file = tmp_path / "matching.yaml"
    matching_file.write_text(
        yaml.safe_dump(
            {
                "run_id": "run-test",
                "case_id": "case-test",
                "disease_slug": "Test_Disease",
                "generated_at": "2026-02-11T00:00:00Z",
                "pr_is_diagnosis": 1.0,
                "explanations": [
                    {
                        "explanation_id": "NO_EXPLANATION",
                        "estimated_probability": 0.0,
                        "description": "default",
                    }
                ],
                "matches": [
                    {
                        "case_term_id": "HP:0001250",
                        "case_present": True,
                        "model_term_id": "HP:0001250",
                        "exact": True,
                        "case_is_broader": False,
                        "case_is_narrower": False,
                        "case_is_close": False,
                        "similarity_percent": 100.0,
                    }
                ],
            },
            sort_keys=False,
        )
    )

    code = task.success_criteria.python.replace("{{ matching_file }}", str(matching_file))
    namespace = {
        "__builtins__": {
            "__import__": __import__,
            "len": len,
            "open": open,
            "print": print,
            "sorted": sorted,
            "str": str,
            "int": int,
            "float": float,
            "bool": bool,
            "list": list,
            "dict": dict,
            "set": set,
            "True": True,
            "False": False,
            "None": None,
            "Exception": Exception,
            "ValueError": ValueError,
            "FileNotFoundError": FileNotFoundError,
        }
    }
    exec(code, namespace)
    assert namespace.get("result") is True


def test_workflow_success_criteria_fails_for_exact_false_without_explanation(tmp_path: Path):
    workflow_file = cyberian_wrapper.WORKFLOW_FILE
    data = yaml.safe_load(workflow_file.read_text())
    task = Task(**data)
    assert task.success_criteria is not None
    assert task.success_criteria.python is not None

    matching_file = tmp_path / "matching.yaml"
    matching_file.write_text(
        yaml.safe_dump(
            {
                "run_id": "run-test",
                "case_id": "case-test",
                "disease_slug": "Test_Disease",
                "generated_at": "2026-02-11T00:00:00Z",
                "pr_is_diagnosis": 1.0,
                "explanations": [
                    {
                        "explanation_id": "NO_EXPLANATION",
                        "estimated_probability": 0.0,
                        "description": "default",
                    },
                    {
                        "explanation_id": "EXP_RELATION",
                        "estimated_probability": 0.7,
                        "description": "placeholder",
                    },
                ],
                "matches": [
                    {
                        "case_term_id": "HP:0003128",
                        "case_present": True,
                        "model_term_id": "HP:0004902",
                        "exact": False,
                        "case_is_broader": True,
                        "case_is_narrower": False,
                        "case_is_close": False,
                        "similarity_percent": 75.0,
                    }
                ],
            },
            sort_keys=False,
        )
    )

    code = task.success_criteria.python.replace("{{ matching_file }}", str(matching_file))
    namespace = {
        "__builtins__": {
            "__import__": __import__,
            "len": len,
            "open": open,
            "print": print,
            "sorted": sorted,
            "str": str,
            "int": int,
            "float": float,
            "bool": bool,
            "list": list,
            "dict": dict,
            "set": set,
            "True": True,
            "False": False,
            "None": None,
            "Exception": Exception,
            "ValueError": ValueError,
            "FileNotFoundError": FileNotFoundError,
        }
    }
    exec(code, namespace)
    assert namespace.get("result") is False
