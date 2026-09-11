"""Run Boomer on saved pending inputs with checkpoints and per-process deadlines.

No input regeneration or hypothesis pruning. Each worker solves one whole KB;
the supervisor imposes a wall-clock deadline in addition to Boomer's timeout.
Successful results, including explicitly marked partial results, replace the old
solutions. Failed attempts retain historical solutions and label them as such.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time

import yaml

from build_analyses import INDEX_FIELDNAMES, REPO, retracted_mappings, stabilise_floats

PENDING = {"NOT_RUN", "STALE_INPUT"}
REPORT_FIELDS = (
    "slug",
    "status",
    "input_sha256",
    "n_pfacts",
    "n_retracted",
    "candidate_retractions",
    "elapsed_seconds",
    "solution_written",
    "error",
)


def sha(content):
    return hashlib.sha256(content).hexdigest()


def table(rows, fields):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(
        stream, fieldnames=fields, delimiter="\t", lineterminator="\n"
    )
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue()


def atomic_text(path, text):
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(text)
    temporary.replace(path)


def worker(args):
    sys.path.insert(0, str(args.boomer_src.expanduser()))
    from boomer.model import KB, SearchConfig
    from boomer.search import solve
    from boomer.renderers.markdown_renderer import MarkdownRenderer
    from boomer.renderers.yaml_renderer import YAMLRenderer

    content = args.worker.read_bytes()
    kb = KB.model_validate(yaml.safe_load(content))
    # Disable count caps as well as lossy clique limits: only timeout stops search.
    config = SearchConfig(
        timeout_seconds=args.timeout,
        partition_initial_threshold=len(kb.pfacts),
        max_pfacts_per_clique=None,
        max_candidate_solutions=0,
        max_iterations=2**63 - 1,
    )
    solution = solve(kb, config)
    solution.name = kb.name
    retractions = retracted_mappings(solution)
    status = (
        "TIMED_OUT"
        if solution.timed_out
        else "NO_SATISFIABLE_SOLUTION"
        if not solution.number_of_satisfiable_combinations
        else "RETRACTED"
        if retractions
        else "ALL_MAPPINGS_CONSISTENT"
    )
    result = {
        "status": status,
        "input_sha256": sha(content),
        "n_pfacts": len(kb.pfacts),
        "n_retracted": len(retractions)
        if status in {"RETRACTED", "ALL_MAPPINGS_CONSISTENT"}
        else "NA",
        "candidate_retractions": len(retractions),
        "retractions": retractions,
        "solution_written": True,
        "error": "NA",
        "number_of_satisfiable_combinations": solution.number_of_satisfiable_combinations,
        "number_of_combinations": solution.number_of_combinations,
        "search_config": config.model_dump(),
    }
    stabilise_floats(solution)
    (args.workdir / "solution.yaml").write_text(YAMLRenderer().render(solution, kb))
    (args.workdir / "solution.md").write_text(MarkdownRenderer().render(solution, kb))
    (args.workdir / "result.json").write_text(json.dumps(result))


def run_one(row, args):
    folder = args.base / "disorders" / row["slug"]
    input_hash = sha((folder / "kb.yaml").read_bytes())
    started = time.monotonic()
    with tempfile.TemporaryDirectory(prefix="boomer-solve-") as directory:
        output = Path(directory)
        command = [
            sys.executable,
            str(Path(__file__).resolve()),
            "--worker",
            str(folder / "kb.yaml"),
            "--workdir",
            str(output),
            "--timeout",
            str(args.timeout),
            "--boomer-src",
            str(args.boomer_src),
        ]
        result = dict(
            slug=row["slug"],
            status="ERROR",
            input_sha256=input_hash,
            n_pfacts=int(row["n_pfacts"]),
            n_retracted="NA",
            candidate_retractions="NA",
            solution_written=False,
            error="NA",
        )
        files = {}
        try:
            process = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=args.timeout + 15,
                env={**os.environ, "PYTHONHASHSEED": "0"},
            )
            if process.returncode:
                result["error"] = (process.stderr or process.stdout)[-4000:].strip()
            else:
                result.update(json.loads((output / "result.json").read_text()))
                files = {
                    name: (output / name).read_text()
                    for name in ("solution.yaml", "solution.md")
                }
        except subprocess.TimeoutExpired:
            result.update(
                status="TIMED_OUT_NO_RESULT",
                error="Worker exceeded supervisor deadline",
            )
        if (
            result["input_sha256"] != input_hash
            or sha((folder / "kb.yaml").read_bytes()) != input_hash
        ):
            result.update(
                status="INPUT_CHANGED",
                solution_written=False,
                error="Input changed during solve",
            )
            files = {}
        result["elapsed_seconds"] = round(time.monotonic() - started, 3)
        return result, files


def result_readme(original, result):
    if not result["solution_written"]:
        return (
            f"> **Latest solve: {result['status']}.** No new solution was produced.\n"
            "> Any retained solution files and report below are historical. See `solve.json`.\n\n"
            + original
        )
    # Preserve disease grounding and subtype context, replacing the old result section.
    if original.startswith("> **STALE INPUT:"):
        original = original.split("\n\n", 1)[1]
    prefix = original.split("## What boomer did", 1)[0]
    lines = [
        prefix.rstrip(),
        "",
        "## What boomer did",
        "",
        f"**Status: `{result['status']}`**",
        "",
    ]
    if result["status"] == "TIMED_OUT":
        lines += [
            "The full joint search reached its time limit. Any assignment and posterior",
            "below are provisional; this is not a completed consistency verdict.",
            "",
        ]
        if result.get("number_of_satisfiable_combinations") == 0:
            lines += ["No satisfiable candidate was found before the timeout.", ""]
    elif result["status"] == "NO_SATISFIABLE_SOLUTION":
        lines += [
            "Boomer returned no satisfiable assignment. No mapping verdict is asserted.",
            "",
        ]
    elif result["status"] == "RETRACTED":
        lines += ["Boomer rejected the following high-prior mapping hypotheses:", ""]
    else:
        lines += [
            "The completed search accepted all high-prior mapping hypotheses together.",
            "",
        ]
    if result.get("retractions"):
        if result["status"] == "TIMED_OUT":
            lines += ["High-prior rejections in the provisional candidate:", ""]
        lines += [
            f"- `{s}` {relation} `{o}`" for s, relation, o in result["retractions"]
        ]
        lines += [""]
    lines += [
        "## Files",
        "",
        "- [`kb.yaml`](kb.yaml): unchanged input.",
        "- [`solution.yaml`](solution.yaml): current machine-readable solver output.",
        "- [`solution.md`](solution.md): rendered solver output.",
        "- [`solve.json`](solve.json): input hash, configuration, and run status.",
        "",
        "The search used the entire KB, with no hypothesis-dropping clique limit.",
        "",
    ]
    return "\n".join(lines)


def write_retractions(base, results, run_dir):
    from dismech import kb_cache

    rows = []
    for slug, row in sorted(results.items()):
        if row["status"] != "RETRACTED":
            continue
        folder = base / "disorders" / slug
        metadata = json.loads((folder / "solve.json").read_text())
        labels = kb_cache.load_document(folder / "kb.yaml").get("labels", {})
        for subject, relation, obj in metadata["retractions"]:
            rows.append(
                dict(
                    slug=slug,
                    subject=subject,
                    subject_label=labels.get(subject, subject),
                    relation=relation,
                    object=obj,
                    object_label=labels.get(obj, obj),
                )
            )
    path = run_dir / "retractions.tsv"
    content = table(
        rows, ("slug", "subject", "subject_label", "relation", "object", "object_label")
    )
    if not path.exists() or path.read_text() != content:
        atomic_text(path, content)


def main():
    from dismech import kb_cache

    kb_cache.default_off()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", type=Path, default=REPO / "analyses/boomer")
    parser.add_argument(
        "--boomer-src", type=Path, default=Path.home() / "repos/boomer-py/src"
    )
    parser.add_argument("--timeout", type=float, default=60)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--run-name", default="pending", help="Directory under runs/")
    parser.add_argument(
        "--rerun-from", type=Path, help="Previous attempts.tsv to rerun"
    )
    parser.add_argument("--status", nargs="+", help="Select statuses in --rerun-from")
    parser.add_argument("--worker", type=Path, help=argparse.SUPPRESS)
    parser.add_argument("--workdir", type=Path, help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.worker:
        worker(args)
        return
    if args.timeout <= 0 or args.workers < 1:
        parser.error("Positive timeout and worker count required")
    if Path(args.run_name).name != args.run_name or args.run_name in {".", ".."}:
        parser.error("--run-name must be a single directory name")
    if args.status and not args.rerun_from:
        parser.error("--status requires --rerun-from")
    index_path = args.base / "index.tsv"
    index_hash = sha(index_path.read_bytes())
    with index_path.open() as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        if reader.fieldnames != list(INDEX_FIELDNAMES):
            raise ValueError("Unexpected index columns")
        index = {row["slug"]: row for row in reader}
    run_dir = args.base / "runs" / args.run_name
    if args.rerun_from and args.rerun_from.resolve().parent == run_dir.resolve():
        parser.error("Reruns require a different output directory from the source run")
    run_dir.mkdir(parents=True, exist_ok=True)
    report_path = run_dir / "attempts.tsv"
    results = {}
    if report_path.exists():
        with report_path.open() as stream:
            results = {
                row["slug"]: row for row in csv.DictReader(stream, delimiter="\t")
            }
    version = subprocess.check_output(
        ["git", "-C", str(args.boomer_src.expanduser()), "rev-parse", "HEAD"], text=True
    ).strip()
    dirty = subprocess.check_output(
        ["git", "-C", str(args.boomer_src.expanduser()), "status", "--porcelain"],
        text=True,
    ).strip()
    if dirty:
        raise ValueError("Boomer checkout is dirty; need a reproducible solver version")
    if args.rerun_from:
        with args.rerun_from.open() as stream:
            source_rows = list(csv.DictReader(stream, delimiter="\t"))
        selected = {
            row["slug"]: row
            for row in source_rows
            if not args.status or row["status"] in args.status
        }
        if not selected:
            raise ValueError("No matching inputs in the source run")
        if set(selected) - set(index) or set(results) - set(selected):
            raise ValueError("Run cohort does not match index or existing results")
        hashes = {}
        for slug, row in sorted(selected.items()):
            hashes[slug] = sha(
                (args.base / "disorders" / slug / "kb.yaml").read_bytes()
            )
            if hashes[slug] != row["input_sha256"]:
                raise ValueError(f"Input changed since source run: {slug}")
        manifest = {
            "boomer_commit": version,
            "timeout_seconds": args.timeout,
            "workers": args.workers,
            "source_sha256": sha(args.rerun_from.read_bytes()),
            "inputs": hashes,
        }
        manifest_path = run_dir / "manifest.json"
        if manifest_path.exists():
            if json.loads(manifest_path.read_text()) != manifest:
                raise ValueError("Run manifest changed; use a new --run-name")
        elif results:
            raise ValueError("Existing rerun results have no manifest")
        else:
            atomic_text(manifest_path, json.dumps(manifest, indent=2) + "\n")
        # The ledger is written before the index. Require both checkpoints so
        # an interrupted install is completed on resume.
        pending = []
        for slug in selected:
            recorded = results.get(slug)
            metadata_path = args.base / "disorders" / slug / "solve.json"
            metadata = (
                json.loads(metadata_path.read_text()) if metadata_path.exists() else {}
            )
            if (
                not recorded
                or recorded["status"] != index[slug]["status"]
                or recorded["input_sha256"] != hashes[slug]
                or metadata.get("boomer_commit") != version
                or metadata.get("input_sha256") != hashes[slug]
                or metadata.get("status") != recorded["status"]
            ):
                pending.append(index[slug])
    else:
        pending = [r for r in index.values() if r["status"] in PENDING]
    pending.sort(key=lambda r: (int(r["n_pfacts"]), r["slug"]))
    print(
        f"Running {len(pending)} saved inputs with {args.workers} workers, {args.timeout}s each; Boomer {version}",
        flush=True,
    )
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(run_one, row, args): row for row in pending}
        for done, future in enumerate(as_completed(futures), 1):
            result, files = future.result()
            slug = result["slug"]
            if sha(index_path.read_bytes()) != index_hash:
                raise ValueError(
                    "Index changed outside this runner; refusing to overwrite it"
                )
            folder = args.base / "disorders" / slug
            result["boomer_commit"] = version
            result["hash_seed"] = 0
            result["timeout_seconds"] = args.timeout
            if sha((folder / "kb.yaml").read_bytes()) != result["input_sha256"]:
                result.update(
                    status="INPUT_CHANGED",
                    solution_written=False,
                    error="Input changed before save",
                )
                files = {}
            for name, text in files.items():
                atomic_text(folder / name, text)
            atomic_text(folder / "solve.json", json.dumps(result, indent=2) + "\n")
            atomic_text(
                folder / "README.md",
                result_readme((folder / "README.md").read_text(), result),
            )
            index[slug].update(
                status=result["status"], n_retracted=result["n_retracted"]
            )
            results[slug] = {key: result[key] for key in REPORT_FIELDS}
            # Write reports before the index so a checkpointed status always has its output.
            atomic_text(
                report_path, table([results[s] for s in sorted(results)], REPORT_FIELDS)
            )
            text = table([index[s] for s in sorted(index)], INDEX_FIELDNAMES).replace(
                "\n", "\r\n"
            )
            atomic_text(index_path, text)
            index_hash = sha(index_path.read_bytes())
            if done % 10 == 0 or done == len(pending):
                from collections import Counter

                counts = Counter(str(r["status"]) for r in results.values())
                print(
                    f"{done}/{len(pending)} this invocation: {dict(counts)}", flush=True
                )
    write_retractions(args.base, results, run_dir)


if __name__ == "__main__":
    main()
