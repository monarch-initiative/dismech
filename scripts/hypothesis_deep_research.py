#!/usr/bin/env python3
"""Run deep research against disease-level mechanistic hypotheses.

OpenScientist operational notes (learned the hard way):

* Jobs are long-running (~50-90 min each). The OpenScientist provider's
  client-side poll ``timeout`` defaults to 3600s and *cancels a still-running
  job* at that mark, even though the backend would let it finish. This script
  therefore auto-injects ``--param timeout=7200`` (the API maximum) for the
  ``openscientist`` provider unless you override it, and defaults the subprocess
  wall-clock timeout above that. See OPENSCIENTIST_JOB_TIMEOUT_SECONDS.

* Keep OpenScientist concurrency LOW (~2-3 jobs at once). The backend does not
  scale to many simultaneous jobs: submitting ~9-10 at once starves them so most
  never finish inside the 2h window, whereas the same jobs run at concurrency
  <=3 complete in ~50-65 min. Do not fan out a large batch in parallel; run in
  small waves and commit finished outputs between waves.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from dismech.hypothesis_analysis_run import iter_analysis_run_problems
from dismech.research_reports import AlignmentError, align_report_provider
from dismech.yaml_io import safe_load

DEFAULT_KB_DIR = Path("kb/disorders")
DEFAULT_OUTPUT_ROOT = Path("kb/hypotheses")
DEFAULT_TEMPLATE = Path("templates/hypothesis_deep_research.md")
FRONTMATTER_DELIMITER = "---"
PROVIDER_ALIASES = {
    "edison": "falcon",
}

# OpenScientist runs iterative hypothesis-driven jobs that routinely take
# 60-90 minutes. The provider's *client-side* poll timeout (deep-research-client
# OpenScientist `timeout` param) defaults to only 3600s, so the client cancels
# still-running jobs at the 60-minute mark even though the OpenScientist backend
# would let them finish (observed completions at ~3800s). We therefore default
# the OpenScientist poll window to the API-allowed maximum (7200s / 2h) unless
# the caller overrides it via `-- --param timeout=<seconds>`.
OPENSCIENTIST_JOB_TIMEOUT_SECONDS = 7200
# The subprocess wall-clock timeout MUST exceed the provider poll window above,
# or subprocess.run() kills the client before the job can complete. Keep this
# comfortably above OPENSCIENTIST_JOB_TIMEOUT_SECONDS.
DEFAULT_SUBPROCESS_TIMEOUT_SECONDS = 7800

# Ontology term validation for the report this script generates, mirroring the
# `dr_term_validation` variable the justfile research recipes use. Reports made
# here suggest HP/GO/CL/UBERON/MONDO terms like every other deep-research report,
# and nothing checked them before deep-research-client 0.2.11.
#
# HGNC is skipped because gene CURIEs cannot be checked reliably: `sqlite:obo:hgnc`
# holds them under the lowercase `hgnc:` this repo uses, so an uppercase
# `HGNC:4283` resolves to nothing and is reported as invented, while `ols:`
# resolves the same CURIE to "mitochondrial chromosome". Both are false alarms.
#
# Unlike reference validation, this path does not read or write
# `references_cache/`, so it does not need the `patch_reference_validator`
# repairs that `scripts/run_deep_research_client.sh` applies.
#
# Note what is still missing here, since it is the asymmetry a reader will hit:
# this script does NOT reference-validate (no `--validate-references`), unlike
# every justfile research recipe. That gap predates term validation. Closing it
# means moving this script onto `scripts/run_deep_research_client.sh` first --
# the reference path reads and writes `references_cache/` and must not run
# unpatched.
TERM_VALIDATION_ARGS = [
    "--validate-terms",
    "--term-cache-dir",
    "terms_cache",
    "--term-skip-prefix",
    "HGNC",
]


class LiteralString(str):
    """Marker class for multiline YAML block scalars."""


class HypothesisDumper(yaml.SafeDumper):
    """Safe dumper with readable multiline strings."""


def _represent_literal_string(
    dumper: yaml.SafeDumper, data: LiteralString
) -> yaml.nodes.ScalarNode:
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")


HypothesisDumper.add_representer(LiteralString, _represent_literal_string)


@dataclass(frozen=True)
class HypothesisRecord:
    disease_slug: str
    disease_name: str
    category: str
    hypothesis_group_id: str
    hypothesis_label: str
    status: str
    data: Mapping[str, Any]


@dataclass(frozen=True)
class ExistingHypothesisOutput:
    provider: str
    path: Path
    citations_path: Path
    citations_exists: bool
    artifact_dir: Path
    artifact_exists: bool


@dataclass(frozen=True)
class RunResult:
    record: HypothesisRecord
    provider: str
    status: str
    returncode: int | str
    duration_seconds: float
    output_file: Path
    citations_file: Path
    command: list[str]
    detail: str


def normalize_provider(provider: str) -> str:
    value = provider.strip().lower()
    return PROVIDER_ALIASES.get(value, value)


def load_yaml(path: Path) -> Mapping[str, Any]:
    data = safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, Mapping):
        raise ValueError(f"Expected mapping at top level of {path}")
    return data


def resolve_disorder_path(kb_dir: Path, disorder: str) -> Path:
    exact_matches = [
        path
        for path in kb_dir.glob("*.yaml")
        if not path.name.endswith(".history.yaml") and path.stem == disorder
    ]
    if len(exact_matches) == 1:
        return exact_matches[0]
    wanted = disorder.casefold()
    matches = [
        path
        for path in kb_dir.glob("*.yaml")
        if not path.name.endswith(".history.yaml") and path.stem.casefold() == wanted
    ]
    if len(matches) == 1:
        return matches[0]
    if not matches:
        raise FileNotFoundError(f"Disorder file not found for {disorder!r} in {kb_dir}")
    raise ValueError(f"Multiple disorder files match {disorder!r}: {matches}")


def extract_hypotheses(path: Path) -> list[HypothesisRecord]:
    data = load_yaml(path)
    disease_slug = path.stem
    disease_name = str(data.get("name") or disease_slug.replace("_", " "))
    category = str(data.get("category") or "")
    raw_hypotheses = data.get("mechanistic_hypotheses") or []
    if not isinstance(raw_hypotheses, list):
        raise ValueError(f"mechanistic_hypotheses must be a list in {path}")

    records: list[HypothesisRecord] = []
    for item in raw_hypotheses:
        if not isinstance(item, Mapping):
            continue
        hypothesis_id = item.get("hypothesis_group_id")
        if not hypothesis_id:
            continue
        records.append(
            HypothesisRecord(
                disease_slug=disease_slug,
                disease_name=disease_name,
                category=category,
                hypothesis_group_id=str(hypothesis_id),
                hypothesis_label=str(item.get("hypothesis_label") or hypothesis_id),
                status=str(item.get("status") or ""),
                data=item,
            )
        )
    return records


def all_hypotheses(kb_dir: Path) -> list[HypothesisRecord]:
    records: list[HypothesisRecord] = []
    for path in sorted(kb_dir.glob("*.yaml")):
        if path.name.endswith(".history.yaml"):
            continue
        records.extend(extract_hypotheses(path))
    return records


def find_hypothesis(
    kb_dir: Path, disorder: str, hypothesis_group_id: str
) -> HypothesisRecord:
    path = resolve_disorder_path(kb_dir, disorder)
    records = extract_hypotheses(path)
    for record in records:
        if record.hypothesis_group_id == hypothesis_group_id:
            return record
    wanted = hypothesis_group_id.casefold()
    for record in records:
        if record.hypothesis_group_id.casefold() == wanted:
            return record
    available = ", ".join(record.hypothesis_group_id for record in records) or "(none)"
    raise ValueError(
        f"Hypothesis {hypothesis_group_id!r} not found in {path}; available: {available}"
    )


def literalize_multiline(value: Any) -> Any:
    if isinstance(value, str) and "\n" in value:
        return LiteralString(value)
    if isinstance(value, list):
        return [literalize_multiline(item) for item in value]
    if isinstance(value, Mapping):
        return {key: literalize_multiline(val) for key, val in value.items()}
    return value


def dump_hypothesis_yaml(record: HypothesisRecord) -> str:
    return yaml.dump(
        literalize_multiline(dict(record.data)),
        Dumper=HypothesisDumper,
        sort_keys=False,
        allow_unicode=True,
        width=100,
    ).rstrip()


def output_dir_for(record: HypothesisRecord, output_root: Path) -> Path:
    return output_root / record.disease_slug / record.hypothesis_group_id


def output_file_for(record: HypothesisRecord, output_root: Path, provider: str) -> Path:
    return output_dir_for(record, output_root) / f"{normalize_provider(provider)}.md"


def has_reviewable_artifacts(artifact_dir: Path) -> bool:
    """Return whether a bundle contains a non-empty, reviewable file.

    Raw, local-only, and controlled payload directories deliberately do not
    count: their presence says nothing about whether code, a manifest, or a
    derived result was preserved for review.
    """
    excluded_parts = {"raw", "local", "controlled"}
    if not artifact_dir.is_dir():
        return False
    return any(
        path.is_file()
        and path.stat().st_size > 0
        and excluded_parts.isdisjoint(path.relative_to(artifact_dir).parts)
        for path in artifact_dir.rglob("*")
    )


def existing_outputs(
    record: HypothesisRecord, output_root: Path
) -> list[ExistingHypothesisOutput]:
    directory = output_dir_for(record, output_root)
    if not directory.exists():
        return []
    outputs: list[ExistingHypothesisOutput] = []
    for path in sorted(directory.glob("*.md")):
        if path.name.endswith(".citations.md"):
            continue
        citations_path = Path(f"{path}.citations.md")
        artifact_dir = path.parent / f"{path.stem}_artifacts"
        outputs.append(
            ExistingHypothesisOutput(
                provider=path.stem,
                path=path,
                citations_path=citations_path,
                citations_exists=citations_path.exists()
                and citations_path.stat().st_size > 0,
                artifact_dir=artifact_dir,
                artifact_exists=has_reviewable_artifacts(artifact_dir),
            )
        )
    return outputs


def build_provider_args(provider: str) -> list[str]:
    normalized = normalize_provider(provider)
    if normalized == "cborg":
        return ["--use-cborg"]
    if normalized == "cyberian-codex":
        return ["--provider", "cyberian", "--param", "agent_type=codex"]
    return ["--provider", normalized]


def template_vars(
    record: HypothesisRecord,
    *,
    artifact_dir: Path | None = None,
    overrides: Mapping[str, str] | None = None,
) -> dict[str, str]:
    values = {
        "disease_name": record.disease_name,
        "category": record.category,
        "hypothesis_group_id": record.hypothesis_group_id,
        "hypothesis_label": record.hypothesis_label,
        "hypothesis_status": record.status,
        "hypothesis_yaml": dump_hypothesis_yaml(record),
    }
    if artifact_dir is not None:
        values["artifact_dir"] = str(artifact_dir)
    if overrides:
        values.update(overrides)
    return values


def passthrough_template_vars(extra_args: Sequence[str]) -> dict[str, str]:
    """Collect explicit deep-research-client ``--var key=value`` arguments."""
    values: dict[str, str] = {}
    for index, argument in enumerate(extra_args[:-1]):
        if argument != "--var":
            continue
        assignment = str(extra_args[index + 1])
        if "=" in assignment:
            key, value = assignment.split("=", 1)
            values[key] = value
    return values


def template_placeholders(template: Path) -> set[str]:
    """Return simple named placeholders required by one research template."""
    try:
        text = template.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return set()
    return set(re.findall(r"(?<!\{)\{([A-Za-z_][A-Za-z0-9_]*)\}(?!\})", text))


def build_command(
    record: HypothesisRecord,
    *,
    provider: str,
    output_root: Path,
    template: Path,
    extra_args: Sequence[str],
    validate_terms: bool = True,
    template_overrides: Mapping[str, str] | None = None,
) -> list[str]:
    normalized = normalize_provider(provider)
    output_file = output_file_for(record, output_root, normalized)
    artifact_dir = output_file.parent / f"{output_file.stem}_artifacts"
    command = [
        "uv",
        "run",
        "deep-research-client",
        "research",
        "--template",
        str(template),
    ]
    for key, value in template_vars(
        record, artifact_dir=artifact_dir, overrides=template_overrides
    ).items():
        command.extend(["--var", f"{key}={value}"])
    command.extend(build_provider_args(normalized))
    command.extend(provider_default_params(normalized, extra_args))
    if validate_terms:
        command.extend(term_validation_args(extra_args))
    command.extend(
        [
            "--output",
            str(output_file),
            "--separate-citations",
            f"{output_file}.citations.md",
        ]
    )
    command.extend(extra_args)
    return command


def term_validation_args(extra_args: Sequence[str]) -> list[str]:
    """Return the default term-validation flags, unless the caller set their own.

    Any explicit ``--validate-terms`` or ``--term-*`` argument passed after ``--``
    means the caller is steering term validation themselves, so the defaults step
    aside rather than appearing twice on the command line.

    ``--no-term-labels`` is the one ``--term-``-prefixed spelling this does not
    match, since it begins ``--no-term-``. That is the behaviour we want -- the
    caller is turning label comparison off, not taking over the cache directory
    or the skipped prefixes -- so the defaults still apply and the run validates
    terms with labels off.

    Args:
        extra_args: Arguments the caller passed through after ``--``.

    Returns:
        The default flags, or an empty list when the caller supplied their own.
    """
    if any(
        str(arg).startswith("--validate-terms") or str(arg).startswith("--term-")
        for arg in extra_args
    ):
        return []
    return list(TERM_VALIDATION_ARGS)


def provider_default_params(provider: str, extra_args: Sequence[str]) -> list[str]:
    """Inject provider-specific default --param values not already supplied.

    OpenScientist's default 3600s poll timeout prematurely cancels long jobs, so
    we raise it to the API maximum unless the caller passed an explicit
    ``--param timeout=...``.
    """
    normalized = normalize_provider(provider)
    if normalized == "openscientist":
        if any(str(arg).startswith("timeout=") for arg in extra_args):
            return []
        return ["--param", f"timeout={OPENSCIENTIST_JOB_TIMEOUT_SECONDS}"]
    if normalized == "biomni":
        defaults: list[str] = []
        supplied_params = {
            str(extra_args[index + 1]).split("=", 1)[0]
            for index, arg in enumerate(extra_args[:-1])
            if arg == "--param" and "=" in str(extra_args[index + 1])
        }
        lake_root = os.getenv("BIOMNI_DATA_PATH") or str(Path.home() / ".biomni-lake")
        if "path" not in supplied_params:
            defaults.extend(["--param", f"path={Path(lake_root).expanduser()}"])
        if "skip_data_lake" not in supplied_params:
            defaults.extend(["--param", "skip_data_lake=false"])
        return defaults
    return []


def shell_join(parts: Sequence[str]) -> str:
    return " ".join(subprocess.list2cmdline([part]) for part in parts)


def tail_detail(result: subprocess.CompletedProcess[str]) -> str:
    text = (result.stderr or result.stdout or "").strip()
    if not text:
        return ""
    return text.splitlines()[-1][:500]


def bind_report_to_artifact_manifest(report_path: Path, artifact_dir: Path) -> str:
    """Bind a newly written DRC report to the exact canonical manifest bytes.

    The provider response becomes the report body, so it cannot populate DRC's
    YAML frontmatter itself. The runner performs this one post-processing step
    immediately after a new report is written and before invoking the hard gate.
    Existing reports are never rebound during validation.
    """
    manifest_path = artifact_dir / "MANIFEST.yaml"
    if manifest_path.is_symlink() or not manifest_path.is_file():
        return f"cannot bind report: {manifest_path} is not a regular file"
    if report_path.is_symlink() or not report_path.is_file():
        return f"cannot bind report: {report_path} is not a regular file"

    try:
        if manifest_path.stat().st_size <= 0:
            return f"cannot bind report: {manifest_path} is empty"
        manifest_bytes = manifest_path.read_bytes()
        report_text = report_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        return f"cannot bind report to manifest: {error}"

    report_lines = report_text.splitlines()
    if not report_lines or report_lines[0] != FRONTMATTER_DELIMITER:
        return "cannot bind report: report must begin with YAML frontmatter"
    try:
        frontmatter_end = report_lines.index(FRONTMATTER_DELIMITER, 1)
        metadata = safe_load("\n".join(report_lines[1:frontmatter_end]))
    except (ValueError, yaml.YAMLError) as error:
        return f"cannot bind report: invalid YAML frontmatter: {error}"
    if not isinstance(metadata, Mapping):
        return "cannot bind report: YAML frontmatter must be a mapping"

    updated_metadata = dict(metadata)
    updated_metadata["artifact_manifest_sha256"] = (
        f"sha256:{hashlib.sha256(manifest_bytes).hexdigest()}"
    )
    try:
        rendered_metadata = yaml.safe_dump(
            updated_metadata,
            sort_keys=False,
            allow_unicode=True,
        ).rstrip()
    except yaml.YAMLError as error:
        return f"cannot bind report: YAML frontmatter cannot be serialized: {error}"
    body = "\n".join(report_lines[frontmatter_end + 1 :])
    updated_report = (
        f"{FRONTMATTER_DELIMITER}\n{rendered_metadata}\n{FRONTMATTER_DELIMITER}"
    )
    if body:
        updated_report += f"\n{body}"
    if report_text.endswith(("\n", "\r")):
        updated_report += "\n"
    try:
        report_path.write_text(updated_report, encoding="utf-8")
    except OSError as error:
        return f"cannot bind report to manifest: {error}"
    return ""


def analysis_contract_status(
    report_path: Path,
    artifact_dir: Path,
    *,
    required: bool = False,
) -> tuple[str | None, str]:
    """Classify an explicit computational-run marker and hard-gate success.

    Ordinary literature reports carry neither marker and retain the historical
    runner behavior. A provider cannot, however, turn an explicit failed
    analysis into ``OK`` merely by exiting zero or returning useful prose.
    """
    try:
        lines = report_path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as error:
        return "INVALID_ANALYSIS_RUN", f"cannot inspect analysis status: {error}"

    success_marker = "ANALYSIS_STATUS: SUCCEEDED"
    failure_marker = "ANALYSIS_STATUS: FAILED"
    if failure_marker in lines:
        return "ANALYSIS_FAILED", "provider explicitly reported a failed analysis"
    if success_marker not in lines:
        if required:
            return (
                "INVALID_ANALYSIS_RUN",
                "analysis template requires an exact ANALYSIS_STATUS marker",
            )
        return None, ""

    problems = list(iter_analysis_run_problems(report_path, artifact_dir))
    if problems:
        return "INVALID_ANALYSIS_RUN", problems[0][:500]
    return "OK", ""


def template_requires_analysis_contract(template: Path) -> bool:
    """Return whether template frontmatter opts into the computational gate."""
    try:
        text = template.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return False
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return False
    try:
        frontmatter_end = lines.index("---", 1)
        metadata = safe_load("\n".join(lines[1:frontmatter_end]))
    except (ValueError, OSError, UnicodeError, yaml.YAMLError):
        return False
    return (
        isinstance(metadata, Mapping)
        and str(metadata.get("analysis_contract", "")).casefold() == "required"
    )


def existing_output_is_complete(
    output: ExistingHypothesisOutput, *, analysis_contract_required: bool
) -> bool:
    """Return whether an existing provider output is safe to treat as complete."""
    status, _detail = analysis_contract_status(
        output.path,
        output.artifact_dir,
        required=analysis_contract_required,
    )
    return status in {None, "OK"}


def quarantine_existing_artifacts(artifact_dir: Path) -> Path | None:
    """Move pre-overwrite artifacts outside the worktree to prevent stale reuse."""
    if not artifact_dir.exists():
        return None
    backup_root = Path(tempfile.mkdtemp(prefix=f"{artifact_dir.name}-pre-overwrite-"))
    shutil.move(str(artifact_dir), str(backup_root / artifact_dir.name))
    return backup_root


def finish_artifact_quarantine(
    backup_root: Path | None, *, status: str, detail: str
) -> str:
    """Discard an intentional overwrite backup only after a valid new run."""
    if backup_root is None:
        return detail
    if status == "OK":
        shutil.rmtree(backup_root)
        return detail
    message = f"pre-overwrite artifacts preserved at {backup_root}"
    return f"{detail}; {message}" if detail else message


def run_record(
    record: HypothesisRecord,
    *,
    provider: str,
    output_root: Path,
    template: Path,
    extra_args: Sequence[str],
    timeout_seconds: int,
    dry_run: bool,
    overwrite: bool,
    validate_terms: bool = True,
    template_overrides: Mapping[str, str] | None = None,
) -> RunResult:
    normalized = normalize_provider(provider)
    output_file = output_file_for(record, output_root, normalized)
    citations_file = Path(f"{output_file}.citations.md")
    artifact_dir = output_file.parent / f"{output_file.stem}_artifacts"
    analysis_contract_required = template_requires_analysis_contract(template)
    command = build_command(
        record,
        provider=normalized,
        output_root=output_root,
        template=template,
        extra_args=extra_args,
        validate_terms=validate_terms,
        template_overrides=template_overrides,
    )

    supplied_template_vars = template_vars(
        record,
        artifact_dir=artifact_dir,
        overrides=template_overrides,
    )
    passthrough_vars = passthrough_template_vars(extra_args)
    supplied_template_vars.update(passthrough_vars)
    nonblank_template_vars = {
        key for key, value in supplied_template_vars.items() if str(value).strip()
    }
    missing_template_vars = sorted(
        template_placeholders(template) - nonblank_template_vars
    )
    canonical_artifact_dir = str(artifact_dir)
    if (
        "artifact_dir" in passthrough_vars
        and passthrough_vars["artifact_dir"] != canonical_artifact_dir
    ):
        missing_detail = (
            "artifact_dir is runner-controlled and must equal "
            f"{canonical_artifact_dir!r}"
        )
    elif missing_template_vars:
        missing_detail = "missing template variable(s): " + ", ".join(
            missing_template_vars
        )
    else:
        missing_detail = ""
    if missing_detail:
        return RunResult(
            record=record,
            provider=normalized,
            status="INVALID_TEMPLATE_VARIABLES",
            returncode=2,
            duration_seconds=0.0,
            output_file=output_file,
            citations_file=citations_file,
            command=command,
            detail=missing_detail,
        )

    if dry_run:
        return RunResult(
            record=record,
            provider=normalized,
            status="DRY_RUN",
            returncode=0,
            duration_seconds=0.0,
            output_file=output_file,
            citations_file=citations_file,
            command=command,
            detail="",
        )

    if output_file.exists() and not overwrite:
        contract_status, contract_detail = analysis_contract_status(
            output_file,
            artifact_dir,
            required=analysis_contract_required,
        )
        if contract_status not in {None, "OK"}:
            return RunResult(
                record=record,
                provider=normalized,
                status=contract_status,
                returncode=0,
                duration_seconds=0.0,
                output_file=output_file,
                citations_file=citations_file,
                command=command,
                detail=contract_detail,
            )
        return RunResult(
            record=record,
            provider=normalized,
            status="SKIPPED_EXISTS",
            returncode=0,
            duration_seconds=0.0,
            output_file=output_file,
            citations_file=citations_file,
            command=command,
            detail="use --overwrite to replace existing output",
        )

    output_file.parent.mkdir(parents=True, exist_ok=True)
    artifact_backup = quarantine_existing_artifacts(artifact_dir) if overwrite else None
    started = time.monotonic()
    try:
        result = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
        )
        duration = time.monotonic() - started
        output_ok = output_file.exists() and output_file.stat().st_size > 0
        detail = tail_detail(result)
        if result.returncode == 0 and output_ok:
            try:
                report_claims_analysis_success = (
                    "ANALYSIS_STATUS: SUCCEEDED"
                    in output_file.read_text(encoding="utf-8").splitlines()
                )
            except (OSError, UnicodeError):
                report_claims_analysis_success = False
            binding_detail = (
                bind_report_to_artifact_manifest(output_file, artifact_dir)
                if report_claims_analysis_success
                else ""
            )
            if binding_detail:
                status = "INVALID_ANALYSIS_RUN"
                detail = binding_detail
            else:
                contract_status, contract_detail = analysis_contract_status(
                    output_file,
                    artifact_dir,
                    required=analysis_contract_required,
                )
                status = contract_status or "OK"
                if contract_detail:
                    detail = contract_detail
        elif result.returncode == 0:
            status = "MISSING_OUTPUT"
        else:
            status = f"ERROR_{result.returncode}"
        provider_ran = normalized

        # A run that fell back to another provider wrote a report named for the
        # provider we asked for. The output path is how a provider is read back
        # here (`existing_outputs`) exactly as it is in the justfile recipes, so
        # the report is renamed to whoever actually produced it.
        #
        # Gated on the report existing rather than on the run succeeding, which
        # is what the justfile recipes do and for the same reason: the client
        # writes the report BEFORE validating it and exits 3 when validation
        # fails, so an ERROR_3 run leaves a real report on disk. Aligning only
        # on OK would leave exactly that report misnamed.
        if output_ok:
            try:
                alignment = align_report_provider(output_file, normalized)
            except AlignmentError as error:
                # Do not overwrite a status that already records a real failure:
                # an ERROR_3 run failed validation, and that is the more useful
                # thing to report. Only a run that otherwise succeeded becomes
                # ERROR_ALIGN.
                if status == "OK":
                    status = "ERROR_ALIGN"
                    detail = str(error)
                else:
                    detail = f"{detail}; alignment failed: {error}".lstrip("; ")
            else:
                if alignment.fell_back and alignment.actual_provider:
                    provider_ran = alignment.actual_provider
                    output_file = alignment.report
                    citations_file = Path(f"{output_file}.citations.md")
                    fallback_note = (
                        f"{normalized} could not run this job; "
                        f"{provider_ran} produced the report instead"
                    )
                    detail = (
                        f"{fallback_note}; {detail}".rstrip("; ")
                        if detail
                        else fallback_note
                    )

        detail = finish_artifact_quarantine(
            artifact_backup, status=status, detail=detail
        )
        return RunResult(
            record=record,
            provider=provider_ran,
            status=status,
            returncode=result.returncode,
            duration_seconds=duration,
            output_file=output_file,
            citations_file=citations_file,
            command=command,
            detail=detail,
        )
    except subprocess.TimeoutExpired:
        duration = time.monotonic() - started
        detail = finish_artifact_quarantine(
            artifact_backup,
            status="TIMEOUT",
            detail=f"timeout after {timeout_seconds}s",
        )
        return RunResult(
            record=record,
            provider=normalized,
            status="TIMEOUT",
            returncode="timeout",
            duration_seconds=duration,
            output_file=output_file,
            citations_file=citations_file,
            command=command,
            detail=detail,
        )


def list_records(
    records: Sequence[HypothesisRecord],
    *,
    output_root: Path,
    provider: str | None,
    missing_provider: str | None,
) -> None:
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(
        [
            "disorder",
            "disease_name",
            "category",
            "hypothesis_group_id",
            "hypothesis_label",
            "status",
            "providers",
            "provider_count",
            "has_target_provider",
            "output_dir",
        ]
    )
    target_provider = normalize_provider(provider or missing_provider or "")
    displayed = 0
    for record in records:
        outputs = existing_outputs(record, output_root)
        providers = sorted(output.provider for output in outputs)
        has_target = bool(target_provider and target_provider in providers)
        if missing_provider and has_target:
            continue
        displayed += 1
        writer.writerow(
            [
                record.disease_slug,
                record.disease_name,
                record.category,
                record.hypothesis_group_id,
                record.hypothesis_label,
                record.status,
                ",".join(providers),
                len(providers),
                "yes" if has_target else "no" if target_provider else "",
                output_dir_for(record, output_root),
            ]
        )
    print("# summary")
    print(f"# hypotheses_total\t{len(records)}")
    print(f"# rows_displayed\t{displayed}")
    if target_provider:
        print(f"# target_provider\t{target_provider}")


def write_run_report(
    results: Sequence[RunResult], output_root: Path, provider: str
) -> Path:
    output_root.mkdir(parents=True, exist_ok=True)
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    path = output_root / f"hypothesis_deep_research_{provider}_{timestamp}.tsv"
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(
            [
                "disorder",
                "hypothesis_group_id",
                "provider",
                "status",
                "returncode",
                "duration_seconds",
                "output_file",
                "citations_file",
                "command",
                "detail",
            ]
        )
        for result in results:
            writer.writerow(
                [
                    result.record.disease_slug,
                    result.record.hypothesis_group_id,
                    result.provider,
                    result.status,
                    result.returncode,
                    f"{result.duration_seconds:.2f}",
                    result.output_file,
                    result.citations_file,
                    shell_join(result.command),
                    result.detail,
                ]
            )
    return path


def print_run_result(result: RunResult) -> None:
    print(
        f"{result.record.disease_slug}/{result.record.hypothesis_group_id} "
        f"provider={result.provider} status={result.status}"
    )
    print(f"output={result.output_file}")
    print(f"citations={result.citations_file}")
    print(f"command={shell_join(result.command)}")
    if result.detail:
        print(f"detail={result.detail}")


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    if argv is None:
        argv = sys.argv[1:]

    research_args: list[str] = []
    if "--" in argv:
        separator_index = list(argv).index("--")
        research_args = list(argv[separator_index + 1 :])
        argv = [*argv[:separator_index]]

    parser = argparse.ArgumentParser(
        description="Run deep research against mechanistic_hypotheses in disorder YAML."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    def add_common_flags(subparser: argparse.ArgumentParser) -> None:
        subparser.add_argument("--kb-dir", type=Path, default=DEFAULT_KB_DIR)
        subparser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)

    def add_dataset_template_flags(subparser: argparse.ArgumentParser) -> None:
        subparser.add_argument("--dataset-inputs")
        subparser.add_argument("--target-variables")
        subparser.add_argument("--analysis-objective")

    list_parser = subparsers.add_parser("list", help="List hypothesis research status.")
    add_common_flags(list_parser)
    list_parser.add_argument("--disorder")
    list_parser.add_argument("--provider")
    list_parser.add_argument("--missing-provider")

    run_parser = subparsers.add_parser("run", help="Run one hypothesis search.")
    add_common_flags(run_parser)
    add_dataset_template_flags(run_parser)
    run_parser.add_argument("provider")
    run_parser.add_argument("disorder")
    run_parser.add_argument("hypothesis_group_id")
    run_parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    run_parser.add_argument("--dry-run", action="store_true")
    run_parser.add_argument("--overwrite", action="store_true")
    run_parser.add_argument(
        "--no-term-validation",
        action="store_true",
        help="Skip ontology term validation of the generated report.",
    )
    run_parser.add_argument(
        "--timeout-seconds", type=int, default=DEFAULT_SUBPROCESS_TIMEOUT_SECONDS
    )

    missing_parser = subparsers.add_parser(
        "run-missing", help="Run hypothesis searches missing a provider."
    )
    add_common_flags(missing_parser)
    missing_parser.add_argument("provider")
    missing_parser.add_argument("--disorder")
    missing_parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    missing_parser.add_argument("--dry-run", action="store_true")
    missing_parser.add_argument("--overwrite", action="store_true")
    missing_parser.add_argument(
        "--no-term-validation",
        action="store_true",
        help="Skip ontology term validation of the generated reports.",
    )
    missing_parser.add_argument("--report-dir", type=Path, default=Path("output"))
    missing_parser.add_argument(
        "--timeout-seconds", type=int, default=DEFAULT_SUBPROCESS_TIMEOUT_SECONDS
    )
    missing_parser.add_argument("--max-hypotheses", type=int)
    missing_parser.add_argument("--stop-on-error", action="store_true")

    args = parser.parse_args(argv)
    args.research_args = research_args
    return args


def cli_template_overrides(args: argparse.Namespace) -> dict[str, str]:
    """Collect optional dataset-template variables from runner flags."""
    return {
        key: value
        for key in ("dataset_inputs", "target_variables", "analysis_objective")
        if (value := getattr(args, key, None)) is not None
    }


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)

    if args.command == "list":
        if args.disorder:
            records = extract_hypotheses(
                resolve_disorder_path(args.kb_dir, args.disorder)
            )
        else:
            records = all_hypotheses(args.kb_dir)
        list_records(
            records,
            output_root=args.output_root,
            provider=args.provider,
            missing_provider=args.missing_provider,
        )
        return 0

    if args.command == "run":
        record = find_hypothesis(args.kb_dir, args.disorder, args.hypothesis_group_id)
        result = run_record(
            record,
            provider=args.provider,
            output_root=args.output_root,
            template=args.template,
            extra_args=args.research_args,
            timeout_seconds=args.timeout_seconds,
            dry_run=args.dry_run,
            overwrite=args.overwrite,
            validate_terms=not args.no_term_validation,
            template_overrides=cli_template_overrides(args),
        )
        print_run_result(result)
        return 0 if result.status in {"OK", "DRY_RUN", "SKIPPED_EXISTS"} else 1

    if args.command == "run-missing":
        provider = normalize_provider(args.provider)
        analysis_contract_required = template_requires_analysis_contract(args.template)
        if analysis_contract_required:
            print(
                "execution-gated dataset templates require an explicit disorder and "
                "hypothesis; use the run command, not run-missing",
                file=sys.stderr,
            )
            return 2
        if args.disorder:
            records = extract_hypotheses(
                resolve_disorder_path(args.kb_dir, args.disorder)
            )
        else:
            records = all_hypotheses(args.kb_dir)
        records = [
            record
            for record in records
            if not any(
                output.provider == provider
                and existing_output_is_complete(
                    output,
                    analysis_contract_required=analysis_contract_required,
                )
                for output in existing_outputs(record, args.output_root)
            )
        ]
        if args.max_hypotheses is not None:
            records = records[: args.max_hypotheses]

        results: list[RunResult] = []
        print(f"provider={provider}")
        print(f"candidate_hypotheses={len(records)}")
        for index, record in enumerate(records, start=1):
            print(
                f"[{index}/{len(records)}] "
                f"{record.disease_slug}/{record.hypothesis_group_id}"
            )
            result = run_record(
                record,
                provider=provider,
                output_root=args.output_root,
                template=args.template,
                extra_args=args.research_args,
                timeout_seconds=args.timeout_seconds,
                dry_run=args.dry_run,
                overwrite=args.overwrite,
                validate_terms=not args.no_term_validation,
                template_overrides=cli_template_overrides(args),
            )
            results.append(result)
            print_run_result(result)
            if args.stop_on_error and result.status not in {
                "OK",
                "DRY_RUN",
                "SKIPPED_EXISTS",
            }:
                break

        report_path = write_run_report(results, args.report_dir, provider)
        failures = [
            result
            for result in results
            if result.status not in {"OK", "DRY_RUN", "SKIPPED_EXISTS"}
        ]
        print(
            f"summary: results={len(results)} failures={len(failures)} report={report_path}"
        )
        return 1 if failures else 0

    raise AssertionError(f"unhandled command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
