"""Durable Jev assessments, with exact inputs and observed claim lifetimes."""

import hashlib
import json
import os
import tempfile
from copy import deepcopy
from dataclasses import asdict
from datetime import UTC, datetime
from pathlib import Path

import click
import yaml

from dismech.classifier.structured import structured_claim_task
from dismech.yaml_io import find_duplicate_keys, safe_load

BENCHMARK = "evidence_claim_match"
DEFAULT_ROOT = "analysis/classification/jev"


def timestamp():
    return datetime.now(UTC).isoformat()


def digest(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, ensure_ascii=False).encode()
    ).hexdigest()


def cache_key(model, tasks):
    return digest({"format": 1, "model": model, "tasks": [asdict(t) for t in tasks]})


def input_key(claim):
    """Identity of the judged claim/excerpt, independent of model and questions."""
    return digest(structured_claim_task(claim).state)


def atomic_yaml(path, data):
    text = yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100)
    if path.exists() and path.read_text() == text:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
    try:
        with os.fdopen(descriptor, "w") as stream:
            stream.write(text)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        Path(temporary).unlink(missing_ok=True)


class ResultCache:
    """One YAML per disease/task. Successful assessments are never discarded.

    Only one writer should use a checkout at a time. CI shards use separate
    checkouts and merge their successful result streams in a single writer job.
    """

    def __init__(self, root):
        from dismech.classifier.claims import schema

        self.root = Path(root)
        self.extraction_sha256 = digest(
            {
                "schema": Path(schema().schema.source_file).read_text(),
                "code": {
                    name: (Path(__file__).parent / name).read_text()
                    for name in ("claims.py", "structured.py", "audit.py")
                },
            }
        )
        self._path = None
        self._document = None
        if self.root.is_file():
            raise ValueError("--cache must be a directory, not a SQLite file")

    def _load(self, file, disease=None):
        file = Path(file)
        path = self.root / file.stem / f"{BENCHMARK}.yaml"
        if self._path == path:
            document = self._document
        elif path.exists():
            text = path.read_text()
            if find_duplicate_keys(text):
                raise ValueError(f"Duplicate keys in assessment cache: {path}")
            document = safe_load(text)
            if (
                not isinstance(document, dict)
                or document.get("format_version") != 1
                or document.get("benchmark") != BENCHMARK
                or not isinstance(document.get("assessments"), dict)
            ):
                raise ValueError(f"Invalid assessment cache: {path}")
            for key, record in document["assessments"].items():
                if (
                    not isinstance(record, dict)
                    or record.get("status") != "assessed"
                    or record.get("input_sha256") != digest(record.get("model_input"))
                    or record.get("assessment_sha256") != key
                    or not isinstance(record.get("active"), bool)
                    or not isinstance(record.get("result", {}).get("answers"), dict)
                ):
                    raise ValueError(f"Invalid assessment {key} in {path}")
        else:
            document = {
                "format_version": 1,
                "benchmark": BENCHMARK,
                "source_file": file.as_posix(),
                "disease": disease or file.stem,
                "inventory": None,
                "assessments": {},
            }
        if Path(document["source_file"]).resolve() != file.resolve():
            raise ValueError(f"Disease filename collision in cache: {file}")
        if disease is not None:
            document["disease"] = disease
        self._path, self._document = path, document
        return document

    def get(self, row, key):
        record = self._load(row["file"], row["disease"])["assessments"].get(key)
        if record is None:
            return None
        if record["input_sha256"] != input_key(row["claim"]):
            raise ValueError("Assessment hash refers to a different input")
        # Explicit refreshes keep the previous results in history.
        result = record.get("reassessments", [])[-1:] or [record]
        return {
            name: deepcopy(result[0][name])
            for name in ("status", "assessed_at", "result")
        }

    def put(self, row, key, outcome, tasks, model, revision=None):
        if outcome["status"] != "assessed" or cache_key(model, tasks) != key:
            raise ValueError(
                "Only successful responses with verified input hashes can be cached"
            )
        document = self._load(row["file"], row["disease"])
        records = document["assessments"]
        if key in records:
            record = records[key]
            previous = [record, *record.get("reassessments", [])]
            if not any(all(old[k] == outcome[k] for k in outcome) for old in previous):
                record.setdefault("reassessments", []).append(deepcopy(outcome))
        else:
            identity = input_key(row["claim"])
            siblings = [r for r in records.values() if r["input_sha256"] == identity]
            first = (
                min(siblings, key=lambda r: r["first_seen_at"]) if siblings else None
            )
            records[key] = {
                "assessment_sha256": key,
                "input_sha256": identity,
                "configuration_sha256": digest(
                    {
                        "model": model,
                        "tasks": [
                            {k: v for k, v in asdict(t).items() if k != "state"}
                            for t in tasks
                        ],
                    }
                ),
                "model": model,
                "assessment_source_revision": revision,
                "claim": deepcopy(row["claim"]),
                "model_input": deepcopy(tasks[0].state),
                "first_seen_at": first["first_seen_at"]
                if first
                else outcome["assessed_at"],
                "first_seen_revision": first["first_seen_revision"]
                if first
                else revision,
                "last_seen_at": outcome["assessed_at"],
                "active": True,
                "occurrences": [self._occurrence(row)],
                **deepcopy(outcome),
            }
        atomic_yaml(self._path, document)

    @staticmethod
    def _occurrence(row):
        return {
            k: row.get(k, "") for k in ("assertion_path", "evidence_path", "reference")
        }

    def reconcile(self, files=None, revision=None):
        """Refresh activity from complete files, without inference or pruning.

        Incomplete/invalid extraction never retires a record. Explicit file
        selections leave other diseases alone; no selection checks all cached
        source files, including ones since deleted from the KB.
        """
        from dismech.classifier.audit import inventory

        if files is None:
            files = []
            for path in sorted(self.root.glob(f"*/{BENCHMARK}.yaml")):
                doc = safe_load(path.read_text())
                files.append(Path(doc["source_file"]))
        for file in files:
            document = self._load(file)
            if not document["assessments"]:
                continue
            source_hash = (
                hashlib.sha256(file.read_bytes()).hexdigest() if file.exists() else None
            )
            present = {}
            valid = True
            if file.exists():
                for row in inventory([file]):
                    if row["status"] == "invalid_input":
                        valid = False
                    elif row["status"] == "ready":
                        present.setdefault(input_key(row["claim"]), []).append(
                            self._occurrence(row)
                        )
            previous = document["inventory"] or {}
            # Unchanged files do not acquire a new timestamp on every run.
            observed = (
                previous.get("observed_at")
                if previous.get("source_sha256") == source_hash
                and previous.get("extraction_sha256") == self.extraction_sha256
                and previous.get("complete") == valid
                else None
            ) or timestamp()
            earliest = {}
            for record in document["assessments"].values():
                identity = record["input_sha256"]
                if (
                    identity not in earliest
                    or record["first_seen_at"] < earliest[identity]["first_seen_at"]
                ):
                    earliest[identity] = record
            for record in document["assessments"].values():
                first = earliest[record["input_sha256"]]
                record["first_seen_at"] = first["first_seen_at"]
                record["first_seen_revision"] = first["first_seen_revision"]
                occurrences = present.get(record["input_sha256"], [])
                if not occurrences and not valid:
                    continue
                active = bool(occurrences)
                if record["active"] != active:
                    record.setdefault("activity_history", []).append(
                        {
                            "active": active,
                            "observed_at": observed,
                            "source_revision": revision,
                        }
                    )
                record["active"] = active
                if active:
                    record["last_seen_at"] = max(record["first_seen_at"], observed)
                    record["occurrences"] = occurrences
            document["inventory"] = {
                "source_sha256": source_hash,
                "extraction_sha256": self.extraction_sha256,
                "source_revision": previous.get("source_revision")
                if observed == previous.get("observed_at")
                else revision,
                "observed_at": observed,
                "complete": valid,
                "source_exists": file.exists(),
            }
            atomic_yaml(self._path, document)

    def merge(self, root):
        """Union successful history from another checkout; recompute activity later."""
        incoming = ResultCache(root)
        for path in sorted(incoming.root.glob(f"*/{BENCHMARK}.yaml")):
            source = safe_load(path.read_text())["source_file"]
            other = incoming._load(source)
            document = self._load(source, other["disease"])
            records = document["assessments"]
            for key, record in other["assessments"].items():
                if key not in records:
                    records[key] = deepcopy(record)
                    continue
                ours = records[key]
                for field in ("input_sha256", "configuration_sha256", "model"):
                    if ours[field] != record[field]:
                        raise ValueError(f"Conflicting assessment identity: {key}")
                responses = {}
                for entry in (
                    ours,
                    *ours.get("reassessments", []),
                    record,
                    *record.get("reassessments", []),
                ):
                    outcome = {k: entry[k] for k in ("status", "assessed_at", "result")}
                    responses[digest(outcome)] = outcome
                ordered = sorted(
                    responses.values(), key=lambda r: (r["assessed_at"], digest(r))
                )
                ours.update(deepcopy(ordered[0]))
                if len(ordered) > 1:
                    ours["reassessments"] = deepcopy(ordered[1:])
                if record["first_seen_at"] < ours["first_seen_at"]:
                    for field in ("first_seen_at", "first_seen_revision"):
                        ours[field] = record[field]
                history = {
                    digest(h): h
                    for h in (
                        *ours.get("activity_history", []),
                        *record.get("activity_history", []),
                    )
                }
                if history:
                    ours["activity_history"] = sorted(
                        history.values(), key=lambda h: (h["observed_at"], digest(h))
                    )
            atomic_yaml(self._path, document)
        incoming.close()

    def close(self):
        self._path = self._document = None


@click.command()
@click.option(
    "--cache",
    "root",
    type=click.Path(path_type=Path),
    default=DEFAULT_ROOT,
    show_default=True,
)
@click.option(
    "--import-results",
    "results",
    multiple=True,
    type=click.Path(exists=True, path_type=Path),
    help="Import successful JSONL results without inference; repeatable.",
)
@click.option(
    "--merge-cache",
    "sources",
    multiple=True,
    type=click.Path(exists=True, file_okay=False, path_type=Path),
    help="Merge saved YAML histories from another checkout; repeatable.",
)
def main(root, results, sources):
    """Import successful results and update active flags against the current KB."""
    from dismech import kb_cache
    from dismech.classifier.audit import git_revision, read_jsonl, tasks_for

    kb_cache.default_off()
    cache = ResultCache(root)
    revision = git_revision()
    for source in sources:
        cache.merge(source)
    # Validate every imported hash before writing anything; do not silently reuse
    # results made with another extraction, prompt or model configuration.
    for path in results:
        for row in read_jsonl(path):
            if row["status"] == "assessed":
                tasks = tasks_for(row["claim"])
                if cache_key(row["result"]["model"], tasks) != row["cache_key"]:
                    raise click.ClickException(f"Incompatible assessment in {path}")
    for path in results:
        manifest = path.parent / "manifest.json"
        source_revision = (
            json.loads(manifest.read_text()).get("source_revision")
            if manifest.exists()
            else None
        )
        for row in read_jsonl(path):
            if row["status"] == "assessed":
                outcome = {k: row[k] for k in ("status", "assessed_at", "result")}
                cache.put(
                    row,
                    row["cache_key"],
                    outcome,
                    tasks_for(row["claim"]),
                    row["result"]["model"],
                    source_revision,
                )
    cache.reconcile(revision=revision)
    cache.close()


if __name__ == "__main__":
    main()
