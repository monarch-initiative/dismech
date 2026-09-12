"""Batch solves preserve input bytes and distinguish partial results from verdicts."""

import csv
import json
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

SCRIPTS = Path(__file__).resolve().parents[1] / "analyses/boomer/scripts"
sys.path.insert(0, str(SCRIPTS))
import solve_pending as batch


def test_timed_out_report_does_not_claim_completed_consistency():
    previous = "> **STALE INPUT:** previous solve\n\n# Disease\n\n## What boomer did\n\nOld verdict\n"
    report = batch.result_readme(
        previous,
        {
            "status": "TIMED_OUT",
            "solution_written": True,
            "retractions": [["ORDO:1", "⊂", "ICD10:A00"]],
        },
    )
    assert "provisional" in report
    assert "completed search accepted" not in report
    assert "Old verdict" not in report
    assert "STALE INPUT" not in report
    assert "`ORDO:1` ⊂ `ICD10:A00`" in report


def test_watchdog_retains_existing_solutions(tmp_path, monkeypatch):
    folder = tmp_path / "disorders/Example"
    folder.mkdir(parents=True)
    (folder / "kb.yaml").write_text("name: example\n")
    for name in ("solution.yaml", "solution.md"):
        (folder / name).write_text("historical solution\n")

    def timeout(*args, **kwargs):
        raise subprocess.TimeoutExpired(args[0], kwargs["timeout"])

    monkeypatch.setattr(batch.subprocess, "run", timeout)
    args = SimpleNamespace(base=tmp_path, boomer_src=tmp_path, timeout=1)
    result, files = batch.run_one({"slug": "Example", "n_pfacts": "3"}, args)
    assert result["status"] == "TIMED_OUT_NO_RESULT"
    assert result["n_retracted"] == "NA"
    assert not files
    assert not result["solution_written"]
    for name in ("solution.yaml", "solution.md"):
        assert (folder / name).read_text() == "historical solution\n"


@pytest.mark.parametrize("rerun", [False, True])
def test_batch_checkpoints_and_resumes_without_rerunning_completed_entries(
    tmp_path, monkeypatch, rerun
):
    rows = []
    for slug, status in [
        ("Fresh", "NOT_RUN"),
        ("Stale", "STALE_INPUT"),
        ("Existing", "RETRACTED"),
    ]:
        folder = tmp_path / "disorders" / slug
        folder.mkdir(parents=True)
        (folder / "kb.yaml").write_text(f"name: {slug}\n")
        (folder / "README.md").write_text(
            f"# {slug}\n\n## What boomer did\n\nOld result\n"
        )
        row = dict.fromkeys(batch.INDEX_FIELDNAMES, "0")
        row.update(
            slug=slug,
            status="ALL_MAPPINGS_CONSISTENT" if rerun else status,
            n_pfacts="3",
        )
        rows.append(row)
    index = tmp_path / "index.tsv"
    index.write_text(batch.table(rows, batch.INDEX_FIELDNAMES))
    inputs = {p: p.read_bytes() for p in tmp_path.glob("disorders/*/kb.yaml")}
    argv = ["solve_pending", "--base", str(tmp_path), "--boomer-src", str(tmp_path)]
    source = tmp_path / "historical.tsv"
    if rerun:
        source.write_text(
            batch.table(
                [
                    {
                        "slug": slug,
                        "status": "ALL_MAPPINGS_CONSISTENT",
                        "input_sha256": batch.sha(
                            inputs[tmp_path / "disorders" / slug / "kb.yaml"]
                        ),
                    }
                    for slug in ("Fresh", "Stale")
                ],
                ("slug", "status", "input_sha256"),
            )
        )
        argv += [
            "--rerun-from",
            str(source),
            "--run-name",
            "corrected",
            "--status",
            "ALL_MAPPINGS_CONSISTENT",
        ]
    source_before = source.read_bytes() if rerun else None
    calls = []

    def run(row, args):
        calls.append(row["slug"])
        slug = row["slug"]
        result = {
            "slug": slug,
            "status": "ALL_MAPPINGS_CONSISTENT" if slug == "Fresh" else "TIMED_OUT",
            "input_sha256": batch.sha(
                inputs[tmp_path / "disorders" / slug / "kb.yaml"]
            ),
            "n_pfacts": 3,
            "n_retracted": 0 if slug == "Fresh" else "NA",
            "candidate_retractions": 0,
            "elapsed_seconds": 1.0,
            "solution_written": True,
            "error": "NA",
            "retractions": [],
        }
        return result, {"solution.yaml": "new output\n", "solution.md": "new output\n"}

    monkeypatch.setattr(batch, "run_one", run)
    monkeypatch.setattr(
        batch.subprocess,
        "check_output",
        lambda command, **kwargs: "test-commit\n" if command[-1] == "HEAD" else "",
    )
    monkeypatch.setattr(
        sys,
        "argv",
        argv,
    )
    batch.main()
    assert set(calls) == {"Fresh", "Stale"}
    current = {r["slug"]: r for r in csv.DictReader(index.open(), delimiter="\t")}
    assert current["Existing"] == rows[2]
    assert current["Stale"]["status"] == "TIMED_OUT"
    assert current["Stale"]["n_retracted"] == "NA"
    assert (
        json.loads((tmp_path / "disorders/Fresh/solve.json").read_text())[
            "boomer_commit"
        ]
        == "test-commit"
    )
    before = {p: p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}
    batch.main()
    assert len(calls) == 2
    assert before == {p: p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}
    assert all(p.read_bytes() == content for p, content in inputs.items())
    if rerun:
        assert source.read_bytes() == source_before
        # A different solver cannot silently reuse a previous run's ledger.
        monkeypatch.setattr(
            batch.subprocess,
            "check_output",
            lambda command, **kwargs: "other-commit\n" if command[-1] == "HEAD" else "",
        )
        with pytest.raises(ValueError, match="Run manifest changed"):
            batch.main()
        assert before == {p: p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}
