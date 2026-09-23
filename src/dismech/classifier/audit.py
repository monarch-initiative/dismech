"""Audit all disease assertion/snippet pairs with Jev (report only)."""

import hashlib
import json
import subprocess
import time
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from dataclasses import asdict
from pathlib import Path

import click
import httpx

from dismech import kb_cache
from dismech.classifier.aspects import aspect_output_schema, aspect_prompt
from dismech.classifier.base import ClassificationTask
from dismech.classifier.cache import (
    DEFAULT_ROOT,
    ResultCache,
    cache_key,
    digest,
    timestamp,
)
from dismech.classifier.claims import (
    ANNOTATIONS,
    class_slots,
    extract_claim,
    pointer,
    schema,
)
from dismech.classifier.rubric import CRITERIA
from dismech.classifier.structured import structured_claim_task
from dismech.classifier.typesafe import TypeSafeClassifier


def iter_assertions(document):
    """Visit every evidence-capable object, including ones with no evidence.

    Unknown containers are still traversed: evidence in a schema-invalid location
    must appear as an input error, rather than disappearing from the audit.
    """
    classes = schema().all_classes()

    def walk(value, parts, class_name):
        if isinstance(value, dict):
            slots = class_slots(class_name) if class_name in classes else {}
            if parts and ("evidence" in slots or "evidence" in value):
                yield pointer(parts), class_name, value
            for name, child in value.items():
                if name in ANNOTATIONS:
                    continue
                slot = slots.get(name)
                child_class = slot.range if slot else None
                yield from walk(child, parts + [name], child_class)
        elif isinstance(value, list):
            for index, child in enumerate(value):
                yield from walk(child, parts + [str(index)], class_name)

    yield from walk(document, [], "Disease")


def inventory(files, sections=(), limit=0):
    """Keep exact claim objects; never rewrite the KB or infer missing support."""
    count = 0
    for file in files:
        if limit and count >= limit:
            return
        base = {"file": file.as_posix(), "disease": file.stem}
        try:
            document = kb_cache.load_document(file)
            if not isinstance(document, dict) or not document.get("name"):
                raise ValueError("Expected a Disease object with a name")
        except Exception as exc:
            count += 1
            yield dict(
                base,
                status="invalid_input",
                error=type(exc).__name__,
                assertion_path="",
                evidence_path="",
                section="",
            )
            continue
        base["disease"] = document["name"]
        for path, class_name, assertion in iter_assertions(document):
            section = path.split("/")[1]
            if sections and section not in sections:
                continue
            row = dict(
                base, section=section, assertion_path=path, assertion_type=class_name
            )
            evidence = assertion.get("evidence")
            if evidence is None or evidence == []:
                candidates = [dict(row, status="no_evidence", evidence_path="")]
            elif not isinstance(evidence, list):
                candidates = [
                    dict(
                        row,
                        status="invalid_input",
                        evidence_path=path + "/evidence",
                        error="Evidence must be a list",
                    )
                ]
            else:
                candidates = []
                for index, item in enumerate(evidence):
                    candidate = dict(row, evidence_path=f"{path}/evidence/{index}")
                    if not isinstance(item, dict):
                        candidate.update(
                            status="invalid_input", error="Evidence must be an object"
                        )
                    else:
                        candidate.update(
                            reference=item.get("reference", ""),
                            snippet=item.get("snippet", ""),
                            supports=item.get("supports", ""),
                            directness=item.get("directness", ""),
                        )
                        if (
                            not isinstance(item.get("snippet"), str)
                            or not item["snippet"].strip()
                        ):
                            candidate.update(status="missing_snippet")
                        else:
                            try:
                                claim = extract_claim(
                                    document, candidate["evidence_path"]
                                )
                                # Validate the inference state before scheduling paid requests.
                                structured_claim_task(claim)
                                candidate.update(status="ready", claim=claim)
                            except Exception as exc:
                                candidate.update(status="invalid_input", error=str(exc))
                    candidates.append(candidate)
            for candidate in candidates:
                if limit and count >= limit:
                    return
                count += 1
                yield candidate


def tasks_for(claim):
    state = structured_claim_task(claim).state
    prompt = aspect_prompt()
    return [
        ClassificationTask(
            name=path,
            version=prompt["version"],
            state=state,
            instructions=prompt["instructions"] + "\n" + spec["description"],
            criteria=dict(CRITERIA),
        )
        for path, spec in aspect_output_schema(claim, fields=None)["properties"].items()
    ]


def classify(classifier, tasks):
    try:
        return {
            "status": "assessed",
            "assessed_at": timestamp(),
            "result": asdict(classifier.classify_many(tasks)),
        }
    except Exception as exc:
        # Do not copy HTTP response bodies, request headers or credentials to reports.
        status = (
            exc.response.status_code if isinstance(exc, httpx.HTTPStatusError) else None
        )
        return {
            "status": "api_error",
            "assessed_at": timestamp(),
            "error": type(exc).__name__,
            "http_status": status,
        }


def assess(
    rows, classifier, cache, workers, refresh=False, max_seconds=0, revision=None
):
    """Bound both concurrency and memory; checkpoint each completed request."""
    deadline = time.monotonic() + max_seconds if max_seconds else float("inf")
    iterator = iter(rows)
    pending = {}
    submitted = {}
    refreshed = set()
    exhausted = False
    fatal = False
    with ThreadPoolExecutor(max_workers=workers) as pool:
        while pending or not exhausted:
            while not exhausted and len(pending) < workers:
                try:
                    row = next(iterator)
                except StopIteration:
                    exhausted = True
                    break
                if row["status"] != "ready":
                    yield row
                    continue
                try:
                    tasks = tasks_for(row["claim"])
                except Exception as exc:
                    yield dict(row, status="invalid_input", error=str(exc))
                    continue
                key = cache_key(classifier.model, tasks)
                saved = (
                    None if refresh and key not in refreshed else cache.get(row, key)
                )
                if saved is not None:
                    yield dict(row, **saved, cache_key=key, cached=True)
                    continue
                if key in submitted and submitted[key] in pending:
                    pending[submitted[key]][0].append(row)
                    continue
                if fatal or time.monotonic() >= deadline:
                    reason = (
                        "API authentication failure"
                        if fatal
                        else "run time budget exhausted"
                    )
                    yield dict(row, status="not_assessed", error=reason)
                    continue
                future = pool.submit(classify, classifier, tasks)
                pending[future] = ([row], key, tasks)
                submitted[key] = future
            if not pending:
                continue
            done, _ = wait(pending, return_when=FIRST_COMPLETED)
            for future in done:
                waiting, key, tasks = pending.pop(future)
                submitted.pop(key, None)
                outcome = future.result()
                if outcome["status"] == "assessed":
                    if refresh:
                        refreshed.add(key)
                    cache.put(
                        waiting[0], key, outcome, tasks, classifier.model, revision
                    )
                elif outcome.get("http_status") in {401, 403}:
                    fatal = True
                for index, row in enumerate(waiting):
                    yield dict(row, **outcome, cache_key=key, cached=index > 0)


def read_jsonl(path):
    with path.open() as stream:
        for line in stream:
            yield json.loads(line)


def git_revision():
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=False
    )
    return result.stdout.strip() if result.returncode == 0 else None


@click.command()
@click.option(
    "--input",
    "inputs",
    multiple=True,
    type=click.Path(exists=True, path_type=Path),
    help="Disease YAML file or directory; repeatable. Default: kb/disorders.",
)
@click.option(
    "--output",
    type=click.Path(path_type=Path),
    default="reports/jev-audit",
    show_default=True,
)
@click.option(
    "--cache",
    "cache_path",
    type=click.Path(path_type=Path),
    default=DEFAULT_ROOT,
    show_default=True,
)
@click.option("--model", default="jev-1.13.0", show_default=True)
@click.option("--workers", type=click.IntRange(1, 32), default=4, show_default=True)
@click.option(
    "--section",
    "sections",
    multiple=True,
    help="Top-level section to include; repeatable. Default: all.",
)
@click.option(
    "--limit",
    type=click.IntRange(min=0),
    default=0,
    help="Limit assertion/evidence pairs, including missing evidence; 0 means all.",
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Inventory the entire selection without API calls or cache writes.",
)
@click.option(
    "--shard-count",
    type=click.IntRange(min=1),
    default=1,
    help="Split files into stable hash partitions for CI.",
)
@click.option("--shard-index", type=click.IntRange(min=0), default=0)
@click.option(
    "--max-seconds",
    type=click.IntRange(min=0),
    default=0,
    help="Stop new API calls after this time; still report cached and unassessed inputs. 0 means unlimited.",
)
@click.option(
    "--refresh",
    is_flag=True,
    help="Reassess cached inputs, preserving previous responses.",
)
def main(
    inputs,
    output,
    cache_path,
    model,
    workers,
    sections,
    limit,
    dry_run,
    refresh,
    shard_count,
    shard_index,
    max_seconds,
):
    """Assess snippet support for all disease assertions; write recuration CSVs.

    Results are model triage signals, not curator labels. Output reports are
    regenerated on each run; successful API responses persist in the cache.
    """
    from dismech.classifier.audit_report import write_reports

    kb_cache.default_off()
    inputs = inputs or (Path("kb/disorders"),)
    files = sorted(
        {
            file
            for path in inputs
            for file in (path.rglob("*.yaml") if path.is_dir() else [path])
        }
    )
    if shard_index >= shard_count:
        raise click.BadParameter("shard-index must be less than shard-count")
    files = [
        f
        for f in files
        if int(hashlib.sha256(f.as_posix().encode()).hexdigest(), 16) % shard_count
        == shard_index
    ]
    if not files:
        raise click.ClickException("No disease YAML files found")
    try:
        classifier = None if dry_run else TypeSafeClassifier(model)
    except ValueError as exc:
        raise click.ClickException(str(exc)) from exc
    output.mkdir(parents=True, exist_ok=True)
    metadata = {
        "started_at": timestamp(),
        "source_revision": git_revision(),
        "model": model,
        "inputs": [str(p) for p in inputs],
        "sections": list(sections),
        "limit": limit,
        "dry_run": dry_run,
        "refresh": refresh,
        "workers": workers,
        "prompt": aspect_prompt(),
        "criteria": CRITERIA,
        "aspect_fields": "all",
        "schema_sha256": hashlib.sha256(
            Path(schema().schema.source_file).read_bytes()
        ).hexdigest(),
        "complete": False,
        "shard_count": shard_count,
        "shard_index": shard_index,
        "files": len(files),
        "max_seconds": max_seconds,
        "classifier_sha256": digest(
            {p.name: p.read_text() for p in Path(__file__).parent.glob("*.py")}
        ),
    }
    manifest = output / "manifest.json"
    manifest.write_text(json.dumps(metadata, indent=2) + "\n")
    counts = {}
    with (output / "inventory.jsonl").open("w") as stream:
        for row in inventory(files, sections, limit):
            counts[row["status"]] = counts.get(row["status"], 0) + 1
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")
    metadata["inventory_counts"] = counts
    manifest.write_text(json.dumps(metadata, indent=2) + "\n")
    click.echo(f"Inventory: {sum(counts.values())} assertion/evidence pairs; {counts}")
    cache = None if dry_run else ResultCache(cache_path)
    try:
        if cache is not None:
            cache.reconcile(files, metadata["source_revision"])
        rows = read_jsonl(output / "inventory.jsonl")
        outcomes = (
            rows
            if dry_run
            else assess(
                rows,
                classifier,
                cache,
                workers,
                refresh,
                max_seconds,
                metadata["source_revision"],
            )
        )
        with (output / "results.jsonl").open("w") as stream:
            for index, row in enumerate(outcomes, 1):
                stream.write(json.dumps(row, ensure_ascii=False) + "\n")
                stream.flush()
                if index % 1000 == 0:
                    click.echo(f"Recorded {index} pairs", err=True)
        metadata["complete"] = True
    finally:
        if cache is not None:
            cache.reconcile(files, metadata["source_revision"])
            cache.close()
        metadata["finished_at"] = timestamp()
        if (output / "results.jsonl").exists():
            metadata.update(write_reports(output, complete=metadata["complete"]))
        manifest.write_text(json.dumps(metadata, indent=2) + "\n")
    click.echo(f"Reports: {output / 'entries.csv'} and {output / 'aspects.csv'}")
    if metadata.get("errors", 0):
        raise click.ClickException(
            f"{metadata['errors']} pairs could not be assessed; see reports"
        )


if __name__ == "__main__":
    main()
