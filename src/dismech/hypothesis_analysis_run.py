"""Hard-gate canonical computational hypothesis-analysis run bundles.

This module verifies the report marker, its binding to the exact manifest
bytes, manifest assertions, containment, and byte identity of declared
artifacts.  It deliberately never executes code from the bundle.  An external
replay in a clean environment is still required; the ``replay`` block is a
signed-off record of that separately performed check, not something this
validator can establish by trusting or running provider code.
"""

from __future__ import annotations

import hashlib
import re
import sys
from collections.abc import Iterable, Mapping
from pathlib import Path
from urllib.parse import parse_qsl, urlsplit

import yaml

from dismech.yaml_io import find_duplicate_keys, safe_load

_SUCCESS_MARKER = "ANALYSIS_STATUS: SUCCEEDED"
_FAILURE_MARKER = "ANALYSIS_STATUS: FAILED"
_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_PREFIXED_SHA256 = re.compile(r"^sha256:[0-9a-f]{64}$")
_REQUIRED_OUTPUT_ROLES = {"CODE", "ENVIRONMENT", "TABULAR_RESULT"}
_RESERVED_OUTPUT_ROOTS = {"raw", "local", "controlled", "replay"}
_SENSITIVE_QUERY_KEYS = {
    "access_key",
    "access_token",
    "api_key",
    "apikey",
    "auth",
    "authorization",
    "credential",
    "credentials",
    "password",
    "passwd",
    "secret",
    "sig",
    "signature",
    "token",
    "x_amz_credential",
    "x_amz_security_token",
    "x_amz_signature",
}


def _nonempty(value: object) -> bool:
    """Return whether a scalar-like manifest value contains useful text."""
    return value is not None and bool(str(value).strip())


def _positive_byte_count(value: object) -> bool:
    """Reject booleans and non-positive/non-integral byte counts."""
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _resolve_artifact_path(
    artifact_root: Path,
    value: object,
    *,
    label: str,
) -> tuple[Path | None, str | None]:
    """Resolve a nonempty relative path that remains inside ``artifact_root``."""
    if not isinstance(value, str) or not value.strip():
        return None, f"{label} must be a non-empty relative path"
    relative = Path(value)
    if relative.is_absolute():
        return None, f"{label} must be relative, not absolute: {value!r}"
    candidate = artifact_root / relative
    try:
        root = artifact_root.resolve()
        resolved = candidate.resolve()
    except (OSError, RuntimeError, ValueError) as error:
        return None, f"{label} cannot be resolved: {error}"
    if not resolved.is_relative_to(root):
        return None, f"{label} escapes the artifact directory: {value!r}"
    if candidate.is_symlink():
        return None, f"{label} must be a regular file, not a symlink"
    return resolved, None


def _iter_uri_problems(value: object, *, label: str) -> Iterable[str]:
    """Reject malformed or credential-bearing source URIs."""
    if not isinstance(value, str) or not value.strip():
        yield f"{label} must be a non-empty URI"
        return
    try:
        parsed = urlsplit(value)
    except ValueError as error:
        yield f"{label} is not a valid URI: {error}"
        return
    if not parsed.scheme:
        yield f"{label} must be an absolute URI with a scheme"
    try:
        has_userinfo = parsed.username is not None or parsed.password is not None
    except ValueError as error:
        yield f"{label} is not a valid URI: {error}"
        return
    if has_userinfo:
        yield f"{label} must not contain URL userinfo or credentials"
    for key, _value in parse_qsl(parsed.query, keep_blank_values=True):
        normalized_key = re.sub(r"[^a-z0-9]+", "_", key.casefold()).strip("_")
        if normalized_key in _SENSITIVE_QUERY_KEYS:
            yield f"{label} contains sensitive query key {key!r}"


def _iter_declared_file_problems(
    path: Path,
    *,
    label: str,
    expected_bytes: object,
    expected_sha256: object,
) -> Iterable[str]:
    """Verify a declared file's type, non-emptiness, size, and digest."""
    if path.is_symlink():
        yield f"{label} must be a regular file, not a symlink"
        return
    if not path.exists():
        yield f"{label} does not exist"
        return
    if not path.is_file():
        yield f"{label} is not a regular file"
        return
    actual_bytes = path.stat().st_size
    if actual_bytes <= 0:
        yield f"{label} is empty"
    if not _positive_byte_count(expected_bytes):
        yield f"{label} byte_count must be a positive integer"
    elif expected_bytes != actual_bytes:
        yield (
            f"{label} byte_count mismatch: manifest={expected_bytes}, "
            f"actual={actual_bytes}"
        )
    if not isinstance(expected_sha256, str) or not _SHA256.fullmatch(expected_sha256):
        yield f"{label} sha256 must be a 64-digit lowercase hexadecimal digest"
    elif actual_bytes > 0:
        actual_sha256 = _sha256(path)
        if expected_sha256.casefold() != actual_sha256:
            yield (
                f"{label} sha256 mismatch: manifest={expected_sha256.casefold()}, "
                f"actual={actual_sha256}"
            )


def iter_analysis_run_problems(
    report_path: str | Path,
    artifact_dir: str | Path,
) -> Iterable[str]:
    """Yield every hard-gate problem found in one analysis run bundle."""
    report_path = Path(report_path)
    artifact_dir = Path(artifact_dir)
    report_provider: str | None = None
    report_manifest_sha256: str | None = None

    expected_artifact_dir = report_path.parent / f"{report_path.stem}_artifacts"
    try:
        if artifact_dir.resolve() != expected_artifact_dir.resolve():
            yield (
                "artifact directory must be the canonical sibling "
                f"{expected_artifact_dir} for report {report_path}"
            )
    except (OSError, RuntimeError, ValueError) as error:
        yield f"report/artifact sibling paths cannot be resolved: {error}"

    if report_path.is_symlink():
        yield f"report {report_path} must be a regular file, not a symlink"
    elif not report_path.exists():
        yield f"report {report_path} does not exist"
    elif not report_path.is_file():
        yield f"report {report_path} is not a regular file"
    elif report_path.stat().st_size <= 0:
        yield f"report {report_path} is empty"
    else:
        try:
            report_lines = report_path.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeError) as error:
            yield f"report {report_path} cannot be read as UTF-8: {error}"
        else:
            success_count = report_lines.count(_SUCCESS_MARKER)
            failure_count = report_lines.count(_FAILURE_MARKER)
            if success_count != 1:
                yield f"report must contain an exact line {_SUCCESS_MARKER!r}"
            if failure_count:
                yield f"successful report must not contain {_FAILURE_MARKER!r}"
            output_indexes = [
                index for index, line in enumerate(report_lines) if line == "## Output"
            ]
            if len(output_indexes) != 1:
                yield "report must contain exactly one '## Output' section"
            elif success_count == 1:
                marker_index = report_lines.index(_SUCCESS_MARKER)
                if marker_index <= output_indexes[0]:
                    yield "success marker must occur inside the report's ## Output section"

            if not report_lines or report_lines[0] != "---":
                yield "report must begin with YAML frontmatter"
            else:
                try:
                    frontmatter_end = report_lines.index("---", 1)
                except ValueError:
                    yield "report YAML frontmatter is not closed"
                else:
                    try:
                        report_metadata = safe_load(
                            "\n".join(report_lines[1:frontmatter_end])
                        )
                    except Exception as error:
                        yield f"report YAML frontmatter cannot be parsed safely: {error}"
                    else:
                        if not isinstance(report_metadata, Mapping):
                            yield "report YAML frontmatter must be a mapping"
                        else:
                            if not _nonempty(report_metadata.get("provider")):
                                yield "report YAML frontmatter requires provider"
                            else:
                                report_provider = str(
                                    report_metadata["provider"]
                                ).strip()
                            manifest_checksum = report_metadata.get(
                                "artifact_manifest_sha256"
                            )
                            if not isinstance(
                                manifest_checksum, str
                            ) or not _PREFIXED_SHA256.fullmatch(manifest_checksum):
                                yield (
                                    "report YAML frontmatter requires "
                                    "artifact_manifest_sha256 as "
                                    "'sha256:<64 lowercase hex>'"
                                )
                            else:
                                report_manifest_sha256 = manifest_checksum

    if artifact_dir.is_symlink():
        yield f"artifact directory {artifact_dir} must not be a symlink"
        return
    if not artifact_dir.exists():
        yield f"artifact directory {artifact_dir} does not exist"
        return
    if not artifact_dir.is_dir():
        yield f"artifact directory {artifact_dir} is not a directory"
        return
    try:
        if not any(artifact_dir.iterdir()):
            yield f"artifact directory {artifact_dir} is empty"
            return
    except OSError as error:
        yield f"artifact directory {artifact_dir} cannot be read: {error}"
        return

    manifest_path = artifact_dir / "MANIFEST.yaml"
    if manifest_path.is_symlink():
        yield "MANIFEST.yaml must be a regular file, not a symlink"
        return
    if not manifest_path.exists():
        yield "artifact directory must contain MANIFEST.yaml"
        return
    if not manifest_path.is_file():
        yield "MANIFEST.yaml is not a regular file"
        return
    if manifest_path.stat().st_size <= 0:
        yield "MANIFEST.yaml is empty"
        return
    try:
        manifest_bytes = manifest_path.read_bytes()
        manifest_text = manifest_bytes.decode("utf-8")
        duplicates = find_duplicate_keys(manifest_text)
        manifest = safe_load(manifest_text)
    except (OSError, UnicodeError, ValueError, yaml.YAMLError) as error:
        yield f"MANIFEST.yaml cannot be parsed safely: {error}"
        return
    actual_manifest_sha256 = f"sha256:{hashlib.sha256(manifest_bytes).hexdigest()}"
    if (
        report_manifest_sha256 is not None
        and report_manifest_sha256 != actual_manifest_sha256
    ):
        yield (
            "report artifact_manifest_sha256 does not match MANIFEST.yaml bytes: "
            f"report={report_manifest_sha256}, actual={actual_manifest_sha256}"
        )
    for location, key, line in duplicates:
        yield f"MANIFEST.yaml has duplicate key {key!r} at {location} (line {line})"
    if not isinstance(manifest, Mapping):
        yield "MANIFEST.yaml document root must be a mapping"
        return

    if str(manifest.get("schema_version")) != "1.0":
        yield "schema_version must be 1.0"
    if manifest.get("status") != "SUCCEEDED":
        yield "manifest status must be SUCCEEDED"
    manifest_provider = manifest.get("provider")
    if not _nonempty(manifest_provider):
        yield "manifest provider is required"
    elif (
        report_provider
        and str(manifest_provider).casefold() != report_provider.casefold()
    ):
        yield (
            f"manifest provider {manifest_provider!r} does not match report provider "
            f"{report_provider!r}"
        )
    if manifest.get("fallback_used") is not False:
        yield "fallback_used must be false"
    if manifest.get("direct_analysis_completed") is not True:
        yield "direct_analysis_completed must be true"

    inputs_value = manifest.get("inputs")
    if not isinstance(inputs_value, list) or not inputs_value:
        yield "inputs must be a non-empty list"
        inputs: list[object] = []
    else:
        inputs = inputs_value

    declared_paths: dict[Path, str] = {}
    for index, input_record in enumerate(inputs):
        label = f"inputs[{index}]"
        if not isinstance(input_record, Mapping):
            yield f"{label} must be a mapping"
            continue
        if not _nonempty(input_record.get("identifier")):
            yield f"{label}.identifier is required"
        source_uri_fields = [
            field
            for field in ("canonical_url", "uri")
            if _nonempty(input_record.get(field))
        ]
        if not source_uri_fields:
            yield f"{label} requires canonical_url or uri"
        for field in source_uri_fields:
            yield from _iter_uri_problems(
                input_record.get(field), label=f"{label}.{field}"
            )
        if not any(
            _nonempty(input_record.get(field))
            for field in ("retrieved_at", "retrieval_time_utc")
        ):
            yield f"{label} requires retrieved_at or retrieval_time_utc"
        byte_count = input_record.get("byte_count")
        checksum = input_record.get("sha256")
        if not _positive_byte_count(byte_count):
            yield f"{label}.byte_count must be a positive integer"
        if not isinstance(checksum, str) or not _SHA256.fullmatch(checksum):
            yield f"{label}.sha256 must be a 64-digit lowercase hexadecimal digest"

        if "local_path" not in input_record:
            continue
        local_path, problem = _resolve_artifact_path(
            artifact_dir,
            input_record.get("local_path"),
            label=f"{label}.local_path",
        )
        if problem:
            yield problem
            continue
        assert local_path is not None
        previous = declared_paths.get(local_path)
        if previous:
            yield f"{label}.local_path duplicates declared path from {previous}"
        else:
            declared_paths[local_path] = f"{label}.local_path"
        yield from _iter_declared_file_problems(
            local_path,
            label=f"{label}.local_path",
            expected_bytes=byte_count,
            expected_sha256=checksum,
        )

    outputs_value = manifest.get("outputs")
    if not isinstance(outputs_value, list) or not outputs_value:
        yield "outputs must be a non-empty list"
        outputs: list[object] = []
    else:
        outputs = outputs_value

    roles: set[str] = set()
    output_paths: set[Path] = set()
    tabular_output_paths: dict[str, Path] = {}
    for index, output_record in enumerate(outputs):
        label = f"outputs[{index}]"
        if not isinstance(output_record, Mapping):
            yield f"{label} must be a mapping"
            continue
        role = output_record.get("role")
        if not isinstance(role, str) or not role.strip():
            yield f"{label}.role is required"
            normalized_role = ""
        else:
            normalized_role = role.strip().upper().replace("-", "_")
            roles.add(normalized_role)
        output_path, problem = _resolve_artifact_path(
            artifact_dir,
            output_record.get("path"),
            label=f"{label}.path",
        )
        if problem:
            yield problem
            continue
        assert output_path is not None
        relative_parts = output_path.relative_to(artifact_dir.resolve()).parts
        if relative_parts and relative_parts[0].casefold() in _RESERVED_OUTPUT_ROOTS:
            yield (
                f"{label}.path must not be under reserved output directory "
                f"{relative_parts[0]!r}"
            )
        previous = declared_paths.get(output_path)
        if previous:
            yield f"{label}.path duplicates declared path from {previous}"
        else:
            declared_paths[output_path] = f"{label}.path"
        output_paths.add(output_path)
        if normalized_role == "TABULAR_RESULT":
            tabular_output_paths[str(output_record.get("path"))] = output_path
        yield from _iter_declared_file_problems(
            output_path,
            label=f"{label}.path",
            expected_bytes=output_record.get("byte_count"),
            expected_sha256=output_record.get("sha256"),
        )

    missing_roles = sorted(_REQUIRED_OUTPUT_ROLES - roles)
    if missing_roles:
        yield "outputs are missing required role(s): " + ", ".join(missing_roles)

    replay = manifest.get("replay")
    if not isinstance(replay, Mapping):
        yield "replay must be a mapping"
        return
    if not _nonempty(replay.get("command")):
        yield "replay.command is required"
    if replay.get("verified") is not True:
        yield "replay.verified must be true"
    byte_identity = replay.get("byte_identity")
    if not isinstance(byte_identity, Mapping) or not byte_identity:
        yield "replay.byte_identity must be a non-empty mapping"
        return
    byte_identity_refs = {str(path) for path in byte_identity}
    expected_tabular_refs = set(tabular_output_paths)
    for missing_ref in sorted(expected_tabular_refs - byte_identity_refs):
        yield f"replay.byte_identity is missing TABULAR_RESULT {missing_ref!r}"
    for extra_ref in sorted(byte_identity_refs - expected_tabular_refs):
        yield f"replay.byte_identity has non-TABULAR_RESULT path {extra_ref!r}"
    for replay_path_ref, identical in byte_identity.items():
        replay_label = f"replay.byte_identity[{replay_path_ref!r}]"
        if identical is not True:
            yield f"{replay_label} must be true"
        replay_path, problem = _resolve_artifact_path(
            artifact_dir,
            replay_path_ref,
            label=replay_label,
        )
        if problem:
            yield problem
        elif replay_path not in output_paths:
            yield f"{replay_label} must name a declared output path"

    replay_assets_value = replay.get("assets")
    if not isinstance(replay_assets_value, list) or not replay_assets_value:
        yield "replay.assets must be a non-empty list"
        return
    replay_assets: dict[str, Path] = {}
    for index, replay_asset in enumerate(replay_assets_value):
        label = f"replay.assets[{index}]"
        if not isinstance(replay_asset, Mapping):
            yield f"{label} must be a mapping"
            continue
        replay_asset_ref = replay_asset.get("path")
        replay_asset_path, problem = _resolve_artifact_path(
            artifact_dir,
            replay_asset_ref,
            label=f"{label}.path",
        )
        if problem:
            yield problem
            continue
        assert replay_asset_path is not None
        relative_parts = replay_asset_path.relative_to(artifact_dir.resolve()).parts
        if not relative_parts or relative_parts[0].casefold() != "replay":
            yield f"{label}.path must be beneath the replay directory"
        replay_asset_ref_text = str(replay_asset_ref)
        if replay_asset_ref_text in replay_assets:
            yield f"{label}.path duplicates replay asset {replay_asset_ref_text!r}"
        else:
            replay_assets[replay_asset_ref_text] = replay_asset_path
        yield from _iter_declared_file_problems(
            replay_asset_path,
            label=f"{label}.path",
            expected_bytes=replay_asset.get("byte_count"),
            expected_sha256=replay_asset.get("sha256"),
        )

    for primary_ref, primary_path in tabular_output_paths.items():
        replay_ref = str(Path("replay") / primary_ref)
        replay_path = replay_assets.get(replay_ref)
        if replay_path is None:
            yield (
                f"replay.assets must include {replay_ref!r} for TABULAR_RESULT "
                f"{primary_ref!r}"
            )
            continue
        if (
            primary_path.is_file()
            and replay_path.is_file()
            and (
                primary_path.stat().st_size != replay_path.stat().st_size
                or _sha256(primary_path) != _sha256(replay_path)
            )
        ):
            yield f"replay asset {replay_ref!r} is not byte-identical to {primary_ref!r}"


def main(argv: list[str] | None = None) -> int:
    """Validate one report/artifact-directory pair from the command line."""
    argv = list(sys.argv[1:] if argv is None else argv)
    if len(argv) != 2:
        print(
            "usage: python -m dismech.hypothesis_analysis_run "
            "<report.md> <artifact_dir>"
        )
        return 2
    report_path, artifact_dir = argv
    problems = list(iter_analysis_run_problems(report_path, artifact_dir))
    for problem in problems:
        print(f"{artifact_dir}: {problem}")
    if problems:
        print(f"\n✗ {len(problems)} hypothesis-analysis-run validation problem(s).")
        return 1
    print("✓ Hypothesis analysis run bundle passed the hard gate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
