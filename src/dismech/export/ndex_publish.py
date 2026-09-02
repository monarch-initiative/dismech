"""Build and safely publish a versioned DisMech CX2 release to NDEx."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import subprocess
import time
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from ndex2.client import Ndex2

from dismech.export.cx2_export import disorder_to_cx2, load_disorder

PRODUCTION_NDEX_HOST = "https://www.ndexbio.org"
DEFAULT_METHODS = "Curated DisMech disorder pathograph exported from YAML to CX2."
DEFAULT_NETWORK_TYPE = "directed causal mechanism network"
DEFAULT_ORGANISM = "Homo sapiens"
REQUIRED_RELEASE_METADATA = ("version", "author", "rights", "rightsHolder")


def _aspect_map(cx2: list[dict[str, Any]]) -> dict[str, Any]:
    aspects: dict[str, Any] = {}
    for aspect in cx2:
        if isinstance(aspect, dict):
            aspects.update(aspect)
    return aspects


def _json_bytes(value: Any) -> bytes:
    return json.dumps(value, separators=(",", ":"), sort_keys=True).encode("utf-8")


def _read_verified_cx2(record: dict[str, Any]) -> list[dict[str, Any]]:
    output_path = Path(record["output_path"])
    payload = output_path.read_bytes()
    actual_hash = hashlib.sha256(payload).hexdigest()
    expected_hash = record.get("sha256")
    if actual_hash != expected_hash:
        raise RuntimeError(
            f"Refusing to upload {record['slug']}: expected sha256 "
            f"{expected_hash!r}, got {actual_hash!r}"
        )
    return json.loads(payload)


def _write_json_atomic(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    temporary.replace(path)


def _source_revision(explicit: str | None) -> str:
    if explicit:
        return explicit
    github_sha = os.getenv("GITHUB_SHA")
    if github_sha:
        return github_sha
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def _load_previous_networks(path: Path | None) -> dict[str, dict[str, Any]]:
    if path is None:
        return {}
    if not path.exists():
        raise FileNotFoundError(
            f"Previous manifest {path} does not exist; omit --previous-manifest "
            "only when intentionally minting a first release"
        )
    payload = json.loads(path.read_text())
    return {
        str(record["slug"]): record
        for record in payload.get("networks", [])
        if isinstance(record, dict) and record.get("slug")
    }


def write_uuid_registry(manifest: dict[str, Any], path: Path) -> dict[str, Any]:
    """Write the stable, reviewable subset of a release manifest."""
    unverified = [
        record["slug"]
        for record in manifest.get("networks", [])
        if record.get("ndex_uuid")
        and record.get("status") not in {"VERIFIED_PRIVATE", "VERIFIED_PUBLIC"}
    ]
    if unverified:
        raise RuntimeError(
            "Refusing to write an active UUID registry with unverified networks: "
            + ", ".join(unverified)
        )
    active = [
        {
            "slug": record["slug"],
            "ndex_uuid": record["ndex_uuid"],
            "status": "ACTIVE",
        }
        for record in manifest.get("networks", [])
        if record.get("ndex_uuid")
        and record.get("status") in {"VERIFIED_PRIVATE", "VERIFIED_PUBLIC"}
    ]
    retired = [
        {
            "slug": record["slug"],
            "ndex_uuid": record["ndex_uuid"],
            "status": "RETIRED",
        }
        for record in manifest.get("retired_networks", [])
        if record.get("ndex_uuid")
    ]
    registry = {
        "schema_version": "1.0",
        "networks": sorted(active + retired, key=lambda record: record["slug"]),
    }
    _write_json_atomic(path, registry)
    return registry


def _network_properties(summary: dict[str, Any]) -> dict[str, str]:
    return {
        str(item.get("predicateString")): str(item.get("value"))
        for item in summary.get("properties", []) or []
        if isinstance(item, dict) and item.get("predicateString") is not None
    }


def _summary_errors(
    summary: dict[str, Any],
    *,
    record: dict[str, Any],
    metadata: dict[str, Any],
    expected_visibility: str,
    expected_index_level: str,
) -> list[str]:
    errors: list[str] = []
    properties = _network_properties(summary)
    expected = {
        "name": record["name"],
        "version": metadata["version"],
        "nodeCount": record["node_count"],
        "edgeCount": record["edge_count"],
        "visibility": expected_visibility,
        "indexLevel": expected_index_level,
    }
    for key, value in expected.items():
        if summary.get(key) != value:
            errors.append(f"{key}: expected {value!r}, got {summary.get(key)!r}")
    if summary.get("completed") is not True:
        errors.append("completed is not true")
    if summary.get("isValid") is not True:
        errors.append(
            f"network is invalid: {summary.get('errorMessage') or 'unknown error'}"
        )
    if summary.get("warnings"):
        errors.append(f"network has warnings: {summary['warnings']!r}")
    if summary.get("hasLayout") is not True:
        errors.append("network has no layout")
    for key in ("author", "rights", "rightsHolder", "source_revision"):
        expected_value = metadata.get(key)
        if expected_value and properties.get(key) != expected_value:
            errors.append(
                f"property {key}: expected {expected_value!r}, got {properties.get(key)!r}"
            )
    return errors


def _wait_for_valid_summary(
    client: Ndex2,
    network_id: str,
    *,
    record: dict[str, Any],
    metadata: dict[str, Any],
    expected_visibility: str,
    expected_index_level: str,
    attempts: int = 30,
    interval_seconds: float = 2.0,
) -> dict[str, Any]:
    errors: list[str] = []
    summary: dict[str, Any] = {}
    previous_permanent_errors: tuple[str, ...] | None = None
    for attempt in range(attempts):
        summary = client.get_network_summary(network_id)
        errors = _summary_errors(
            summary,
            record=record,
            metadata=metadata,
            expected_visibility=expected_visibility,
            expected_index_level=expected_index_level,
        )
        if not errors:
            return summary
        permanent_prefixes = (
            "name:",
            "version:",
            "nodeCount:",
            "edgeCount:",
            "network is invalid:",
            "network has warnings:",
            "network has no layout",
            "property ",
        )
        permanent_errors = tuple(
            error for error in errors if error.startswith(permanent_prefixes)
        )
        if summary.get("completed") is True and permanent_errors:
            if permanent_errors == previous_permanent_errors:
                break
            previous_permanent_errors = permanent_errors
        else:
            previous_permanent_errors = None
        if attempt == attempts - 1:
            break
        time.sleep(interval_seconds)
    raise RuntimeError(
        f"NDEx verification failed for {network_id}: {'; '.join(errors)}"
    )


def build_release(
    *,
    kb_dir: Path,
    output_dir: Path,
    manifest_path: Path,
    previous_manifest_path: Path | None,
    release_metadata: dict[str, Any],
    source_revision: str,
    fail_on_export_defects: bool,
    require_disease_metadata: bool,
) -> dict[str, Any]:
    missing = [
        key for key in REQUIRED_RELEASE_METADATA if not release_metadata.get(key)
    ]
    if missing:
        raise ValueError(f"Missing required release metadata: {', '.join(missing)}")

    previous = _load_previous_networks(previous_manifest_path)
    output_dir.mkdir(parents=True, exist_ok=True)
    records: list[dict[str, Any]] = []
    defects: list[str] = []

    for source_path in sorted(kb_dir.glob("*.yaml")):
        slug = source_path.stem
        disorder = load_disorder(source_path)
        try:
            cx2 = disorder_to_cx2(
                disorder,
                source_path=source_path,
                release_metadata=release_metadata,
                source_revision=source_revision,
            )
        except ValueError as error:
            if str(error) != "Disorder does not contain any pathograph edges to export":
                raise
            records.append(
                {
                    "slug": slug,
                    "source_path": str(source_path),
                    "status": "SKIPPED_NO_EDGES",
                }
            )
            continue

        aspects = _aspect_map(cx2)
        network_attributes = aspects["networkAttributes"][0]
        nodes = aspects["nodes"]
        orphan_count = sum(
            (node.get("v") or {}).get("dismech_type") == "orphan" for node in nodes
        )
        unknown_count = sum(
            (node.get("v") or {}).get("dismech_type") == "unknown" for node in nodes
        )
        if orphan_count:
            defects.append(f"{slug}: {orphan_count} orphan node(s)")
        if unknown_count:
            defects.append(f"{slug}: {unknown_count} unknown node(s)")
        if require_disease_metadata and not network_attributes.get("disease"):
            defects.append(f"{slug}: missing disease metadata")

        output_path = output_dir / f"{slug}.cx2.json"
        serialized = json.dumps(cx2, indent=2) + "\n"
        output_path.write_text(serialized, encoding="utf-8")
        prior = previous.get(slug, {})
        records.append(
            {
                "slug": slug,
                "source_path": str(source_path),
                "output_path": str(output_path),
                "name": network_attributes["name"],
                "disease_term_id": network_attributes.get("disease_term_id"),
                "sha256": hashlib.sha256(serialized.encode("utf-8")).hexdigest(),
                "node_count": len(nodes),
                "edge_count": len(aspects["edges"]),
                "orphan_node_count": orphan_count,
                "unknown_node_count": unknown_count,
                "ndex_uuid": prior.get("ndex_uuid"),
                "status": "EXPORTED",
            }
        )

    exported_slugs = {
        record["slug"] for record in records if record["status"] == "EXPORTED"
    }
    retired_networks = [
        {
            "slug": slug,
            "ndex_uuid": record["ndex_uuid"],
            "previous_status": record.get("status"),
        }
        for slug, record in sorted(previous.items())
        if slug not in exported_slugs and record.get("ndex_uuid")
    ]
    manifest = {
        "schema_version": "1.0",
        "generated_at": datetime.now(UTC).isoformat(),
        "source_revision": source_revision,
        "release_metadata": release_metadata,
        "summary": {
            "disorder_count": len(records),
            "exported_count": sum(r["status"] == "EXPORTED" for r in records),
            "skipped_count": sum(r["status"].startswith("SKIPPED") for r in records),
            "export_defect_count": len(defects),
            "retired_network_count": len(retired_networks),
        },
        "export_defects": defects,
        "retired_networks": retired_networks,
        "networks": records,
    }
    _write_json_atomic(manifest_path, manifest)
    if defects and fail_on_export_defects:
        raise RuntimeError(
            f"Refusing publication because {len(defects)} export defect(s) were found; "
            f"see {manifest_path}"
        )
    return manifest


def publish_release(
    manifest: dict[str, Any],
    *,
    manifest_path: Path,
    host: str,
    username: str,
    password: str,
    visibility: str,
    index_level: str,
    allow_export_defects: bool = False,
) -> dict[str, Any]:
    visibility = visibility.upper()
    index_level = index_level.upper()
    if visibility not in {"PRIVATE", "PUBLIC"}:
        raise ValueError(f"Unsupported NDEx visibility: {visibility}")
    if index_level not in {"NONE", "META", "ALL"}:
        raise ValueError(f"Unsupported NDEx index level: {index_level}")
    if not host.startswith("https://"):
        raise ValueError("NDEx publication requires an explicit HTTPS host")
    if not username or not password:
        raise ValueError("NDEX_USERNAME and NDEX_PASSWORD are required")
    if "export_defects" not in manifest:
        raise ValueError("Release manifest is missing its export_defects audit")
    if manifest["export_defects"] and not allow_export_defects:
        raise RuntimeError(
            f"Refusing publication because the manifest contains "
            f"{len(manifest['export_defects'])} export defect(s)"
        )

    client = Ndex2(host=host, username=username, password=password)
    metadata = manifest["release_metadata"] | {
        "source_revision": manifest["source_revision"]
    }
    publishable = [
        record
        for record in manifest["networks"]
        if record["status"]
        in {
            "EXPORTED",
            "UPLOADED",
            "VERIFIED_PRIVATE",
            "VERIFIED_PUBLIC",
        }
    ]
    cx2_by_slug = {
        record["slug"]: _read_verified_cx2(record)
        for record in publishable
        if record["status"] == "EXPORTED"
    }

    for record in publishable:
        network_id = record.get("ndex_uuid")
        if record["status"] == "EXPORTED":
            cx2 = cx2_by_slug[record["slug"]]
            if network_id:
                previous_summary = client.get_network_summary(network_id)
                previous_visibility = str(
                    previous_summary.get("visibility") or "PRIVATE"
                ).upper()
                staging_visibility = (
                    "PUBLIC"
                    if visibility == "PUBLIC" and previous_visibility == "PUBLIC"
                    else "PRIVATE"
                )
                client.update_cx2_network(io.BytesIO(_json_bytes(cx2)), network_id)
            else:
                uploaded_url = client.save_new_cx2_network(cx2, visibility="PRIVATE")
                network_id = uploaded_url.rstrip("/").split("/")[-1]
                record["ndex_uuid"] = network_id
                staging_visibility = "PRIVATE"

            record["staging_visibility"] = staging_visibility
            record["status"] = "UPLOADED"
            _write_json_atomic(manifest_path, manifest)
        elif not network_id:
            raise ValueError(
                f"Cannot resume {record['slug']} from {record['status']} without an NDEx UUID"
            )

        recorded_staging_visibility = record.get("staging_visibility") or (
            "PUBLIC" if record["status"] == "VERIFIED_PUBLIC" else "PRIVATE"
        )
        staging_visibility = (
            "PRIVATE" if visibility == "PRIVATE" else recorded_staging_visibility
        )
        client.set_network_system_properties(
            network_id,
            {"visibility": staging_visibility, "index_level": index_level},
        )
        try:
            summary = _wait_for_valid_summary(
                client,
                network_id,
                record=record,
                metadata=metadata,
                expected_visibility=staging_visibility,
                expected_index_level=index_level,
            )
        except RuntimeError:
            if staging_visibility == "PUBLIC":
                client.make_network_private(network_id)
                record["staging_visibility"] = "PRIVATE"
            record["status"] = "UPLOADED"
            record.pop("verification", None)
            _write_json_atomic(manifest_path, manifest)
            raise
        record["status"] = f"VERIFIED_{staging_visibility}"
        record["viewer_url"] = f"{host}/viewer/networks/{network_id}"
        record["verification"] = {
            "is_valid": summary["isValid"],
            "completed": summary["completed"],
            "index_level": summary["indexLevel"],
            "visibility": summary["visibility"],
        }
        _write_json_atomic(manifest_path, manifest)

    if visibility == "PUBLIC":
        for record in publishable:
            if record["status"] == "VERIFIED_PUBLIC":
                continue
            network_id = record["ndex_uuid"]
            client.make_network_public(network_id)
            try:
                _wait_for_valid_summary(
                    client,
                    network_id,
                    record=record,
                    metadata=metadata,
                    expected_visibility="PUBLIC",
                    expected_index_level=index_level,
                )
            except RuntimeError:
                client.make_network_private(network_id)
                record["status"] = "VERIFIED_PRIVATE"
                record.setdefault("verification", {})["visibility"] = "PRIVATE"
                _write_json_atomic(manifest_path, manifest)
                raise
            record["status"] = "VERIFIED_PUBLIC"
            record["verification"]["visibility"] = "PUBLIC"
            _write_json_atomic(manifest_path, manifest)

    manifest["summary"]["processed_count"] = len(publishable)
    manifest["summary"]["visibility"] = visibility
    manifest["summary"]["index_level"] = index_level
    _write_json_atomic(manifest_path, manifest)
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kb-dir", type=Path, default=Path("kb/disorders"))
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--manifest-out", type=Path, required=True)
    parser.add_argument("--previous-manifest", type=Path)
    parser.add_argument("--release-version", required=True)
    parser.add_argument("--source-revision")
    parser.add_argument("--author", required=True)
    parser.add_argument("--rights", required=True)
    parser.add_argument("--rights-holder", required=True)
    parser.add_argument("--methods", default=DEFAULT_METHODS)
    parser.add_argument("--network-type", default=DEFAULT_NETWORK_TYPE)
    parser.add_argument("--organism", default=DEFAULT_ORGANISM)
    parser.add_argument("--upload", action="store_true")
    parser.add_argument("--host", default=PRODUCTION_NDEX_HOST)
    parser.add_argument(
        "--visibility", choices=("PRIVATE", "PUBLIC"), default="PRIVATE"
    )
    parser.add_argument(
        "--index-level", choices=("NONE", "META", "ALL"), default="META"
    )
    parser.add_argument("--allow-export-defects", action="store_true")
    parser.add_argument("--allow-missing-disease-metadata", action="store_true")
    args = parser.parse_args()

    metadata = {
        "version": args.release_version,
        "author": args.author,
        "rights": args.rights,
        "rightsHolder": args.rights_holder,
        "methods": args.methods,
        "networkType": args.network_type,
        "organism": args.organism,
    }
    manifest = build_release(
        kb_dir=args.kb_dir,
        output_dir=args.output_dir,
        manifest_path=args.manifest_out,
        previous_manifest_path=args.previous_manifest,
        release_metadata=metadata,
        source_revision=_source_revision(args.source_revision),
        fail_on_export_defects=not args.allow_export_defects,
        require_disease_metadata=not args.allow_missing_disease_metadata,
    )
    if args.upload:
        publish_release(
            manifest,
            manifest_path=args.manifest_out,
            host=args.host,
            username=os.getenv("NDEX_USERNAME", ""),
            password=os.getenv("NDEX_PASSWORD", ""),
            visibility=args.visibility,
            index_level=args.index_level,
            allow_export_defects=args.allow_export_defects,
        )


if __name__ == "__main__":
    main()
