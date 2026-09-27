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
DEFAULT_ROOT = "build/jev-assessments"


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


OUTCOME_FIELDS = ("status", "assessed_at", "result")


def merge_input(left, right):
    """Combine observations without duplicating the canonical claim snapshot."""
    if left["claim"] != right["claim"]:
        raise ValueError("Conflicting snapshots for the same input hash")
    if right["first_seen_at"] < left["first_seen_at"]:
        for field in (
            "first_seen_at",
            "first_seen_revision",
            "origin",
            "evidence_metadata",
        ):
            left[field] = deepcopy(right[field])
    left["last_seen_at"] = max(left["last_seen_at"], right["last_seen_at"])
    if right["active_as_of"] > left["active_as_of"]:
        for field in ("active", "active_as_of", "occurrences"):
            left[field] = deepcopy(right[field])
    history = {
        digest(h): h
        for h in (*left.get("activity_history", []), *right.get("activity_history", []))
    }
    if history:
        left["activity_history"] = sorted(
            history.values(), key=lambda h: (h["observed_at"], digest(h))
        )


def upgrade(document):
    """Convert v1 without inference, retaining all responses and observed history."""
    if document.get("format_version") != 1:
        return document
    inputs = {}
    for key, record in document["assessments"].items():
        identity = record["input_sha256"]
        state = record["model_input"]
        if identity != digest(state) or key != record["assessment_sha256"]:
            raise ValueError("Invalid v1 assessment hash")
        claim = record["claim"]
        item = {
            field: deepcopy(record[field])
            for field in (
                "first_seen_at",
                "first_seen_revision",
                "last_seen_at",
                "active",
                "occurrences",
            )
        }
        item.update(
            claim=state,
            origin=claim.get("origin", {}),
            evidence_metadata={
                k: v
                for k, v in claim.get("selected_evidence", {}).items()
                if k not in state["selected_evidence"]
            },
        )
        if "activity_history" in record:
            item["activity_history"] = deepcopy(record["activity_history"])
        item["active_as_of"] = max(
            [
                item["last_seen_at"],
                *[h["observed_at"] for h in item.get("activity_history", [])],
            ]
        )
        if identity in inputs:
            merge_input(inputs[identity], item)
        else:
            inputs[identity] = item
        for field in (*item, "model_input", "assessment_sha256"):
            record.pop(field, None)
    document["format_version"] = 2
    document["inputs"] = inputs
    return document


class ResultCache:
    """One YAML per disease/task; inputs shared by all assessment configurations.

    Only one writer should use a checkout at a time. CI shards use separate
    checkouts and merge successful histories in a single writer job.
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
        self._path = self._document = None
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
            if not isinstance(document, dict):
                raise ValueError(f"Invalid assessment cache: {path}")
            document = upgrade(document)
            if (
                document.get("format_version") != 2
                or document.get("benchmark") != BENCHMARK
                or not isinstance(document.get("inputs"), dict)
                or not isinstance(document.get("assessments"), dict)
            ):
                raise ValueError(f"Invalid assessment cache: {path}")
            for identity, item in document["inputs"].items():
                if (
                    not isinstance(item, dict)
                    or digest(item.get("claim")) != identity
                    or not isinstance(item.get("active"), bool)
                ):
                    raise ValueError(f"Invalid input {identity} in {path}")
            for key, record in document["assessments"].items():
                if (
                    not isinstance(record, dict)
                    or record.get("status") != "assessed"
                    or record.get("input_sha256") not in document["inputs"]
                    or not isinstance(record.get("result", {}).get("answers"), dict)
                ):
                    raise ValueError(f"Invalid assessment {key} in {path}")
        else:
            document = {
                "format_version": 2,
                "benchmark": BENCHMARK,
                "source_file": file.as_posix(),
                "disease": disease or file.stem,
                "inventory": None,
                "inputs": {},
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
        result = record.get("reassessments", [])[-1:] or [record]
        return {name: deepcopy(result[0][name]) for name in OUTCOME_FIELDS}

    def put(self, row, key, outcome, tasks, model, revision=None):
        if outcome["status"] != "assessed" or cache_key(model, tasks) != key:
            raise ValueError(
                "Only successful responses with verified input hashes can be cached"
            )
        document = self._load(row["file"], row["disease"])
        identity = digest(tasks[0].state)
        inputs = document["inputs"]
        item = {
            "claim": deepcopy(tasks[0].state),
            "origin": deepcopy(row["claim"].get("origin", {})),
            "evidence_metadata": {
                k: v
                for k, v in row["claim"].get("selected_evidence", {}).items()
                if k not in tasks[0].state["selected_evidence"]
            },
            "first_seen_at": outcome["assessed_at"],
            "first_seen_revision": revision,
            "last_seen_at": outcome["assessed_at"],
            "active": True,
            "active_as_of": outcome["assessed_at"],
            "occurrences": [self._occurrence(row)],
        }
        if identity in inputs:
            # An imported historical response is not a new observation of the KB.
            if outcome["assessed_at"] < inputs[identity]["first_seen_at"]:
                for field in (
                    "first_seen_at",
                    "first_seen_revision",
                    "origin",
                    "evidence_metadata",
                ):
                    inputs[identity][field] = item[field]
        else:
            inputs[identity] = item
        records = document["assessments"]
        if key in records:
            record = records[key]
            previous = [record, *record.get("reassessments", [])]
            if not any(all(old[k] == outcome[k] for k in outcome) for old in previous):
                responses = [
                    {k: old[k] for k in OUTCOME_FIELDS} for old in previous
                ] + [deepcopy(outcome)]
                responses.sort(key=lambda r: (r["assessed_at"], digest(r)))
                if responses[0] == outcome:
                    record["assessment_source_revision"] = revision
                record.update(responses[0])
                record["reassessments"] = responses[1:]
        else:
            records[key] = {
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
                **deepcopy(outcome),
            }
        atomic_yaml(self._path, document)

    @staticmethod
    def _occurrence(row):
        return {
            k: row.get(k, "") for k in ("assertion_path", "evidence_path", "reference")
        }

    def reconcile(self, files=None, revision=None):
        """Refresh activity from complete files without inference or pruning.

        Incomplete/invalid extraction never retires a record. Explicit selections
        leave other diseases alone; no selection also checks deleted source files.
        Call from the disease repository so relative source paths resolve there.
        """
        from dismech.classifier.audit import inventory

        if files is None:
            files = [
                Path(safe_load(p.read_text())["source_file"])
                for p in sorted(self.root.glob(f"*/{BENCHMARK}.yaml"))
            ]
        for file in files:
            document = self._load(file)
            if not document["inputs"]:
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
                        document["disease"] = row["disease"]
                        present.setdefault(input_key(row["claim"]), []).append(
                            self._occurrence(row)
                        )
            previous = document["inventory"] or {}
            observed = (
                previous.get("observed_at")
                if previous.get("source_sha256") == source_hash
                and previous.get("extraction_sha256") == self.extraction_sha256
                and previous.get("complete") == valid
                else None
            ) or timestamp()
            for identity, item in document["inputs"].items():
                occurrences = present.get(identity, [])
                if not occurrences and not valid:
                    continue
                active = bool(occurrences)
                if item["active"] != active:
                    item.setdefault("activity_history", []).append(
                        {
                            "active": active,
                            "observed_at": observed,
                            "source_revision": revision,
                        }
                    )
                item["active"] = active
                item["active_as_of"] = max(item["first_seen_at"], observed)
                if active:
                    item["last_seen_at"] = max(item["first_seen_at"], observed)
                    item["occurrences"] = occurrences
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
        """Union successful histories from another checkout; reconcile activity later."""
        incoming = ResultCache(root)
        for path in sorted(incoming.root.glob(f"*/{BENCHMARK}.yaml")):
            source = safe_load(path.read_text())["source_file"]
            other = incoming._load(source)
            document = self._load(source, other["disease"])
            for identity, item in other["inputs"].items():
                if identity in document["inputs"]:
                    merge_input(document["inputs"][identity], item)
                else:
                    document["inputs"][identity] = deepcopy(item)
            for key, record in other["assessments"].items():
                if key not in document["assessments"]:
                    document["assessments"][key] = deepcopy(record)
                    continue
                ours = document["assessments"][key]
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
                    outcome = {k: entry[k] for k in OUTCOME_FIELDS}
                    responses[digest(outcome)] = outcome
                ordered = sorted(
                    responses.values(), key=lambda r: (r["assessed_at"], digest(r))
                )
                if record["assessed_at"] < ours["assessed_at"]:
                    ours["assessment_source_revision"] = record.get(
                        "assessment_source_revision"
                    )
                ours.update(deepcopy(ordered[0]))
                if len(ordered) > 1:
                    ours["reassessments"] = deepcopy(ordered[1:])
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
