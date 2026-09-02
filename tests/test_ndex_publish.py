"""Tests for versioned NDEx release construction and publication."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest
import yaml

from dismech.export import ndex_publish


def _write_disorder(path: Path) -> None:
    path.write_text(
        yaml.safe_dump(
            {
                "name": "Example Disease",
                "disease_term": {
                    "preferred_term": "example disease",
                    "term": {"id": "MONDO:0000001", "label": "disease"},
                },
                "pathophysiology": [
                    {
                        "name": "Upstream",
                        "downstream": [{"target": "Downstream"}],
                    },
                    {"name": "Downstream"},
                ],
            },
            sort_keys=False,
        )
    )


def _metadata() -> dict[str, object]:
    return {
        "version": "2026-09-test",
        "author": "DisMech contributors",
        "rights": "BSD-3-Clause",
        "rightsHolder": "Example rights holder",
        "methods": "Test export",
        "networkType": "directed causal mechanism network",
        "organism": "Homo sapiens",
    }


def test_build_release_writes_versioned_cx2_and_manifest(tmp_path: Path) -> None:
    kb_dir = tmp_path / "kb"
    kb_dir.mkdir()
    _write_disorder(kb_dir / "Example_Disease.yaml")
    output_dir = tmp_path / "cx2"
    manifest_path = tmp_path / "manifest.json"

    manifest = ndex_publish.build_release(
        kb_dir=kb_dir,
        output_dir=output_dir,
        manifest_path=manifest_path,
        previous_manifest_path=None,
        release_metadata=_metadata(),
        source_revision="abc123",
        fail_on_export_defects=True,
        require_disease_metadata=True,
    )

    record = manifest["networks"][0]
    cx2 = json.loads(Path(record["output_path"]).read_text())
    aspects = ndex_publish._aspect_map(cx2)
    attributes = aspects["networkAttributes"][0]
    assert attributes["version"] == "2026-09-test"
    assert attributes["author"] == "DisMech contributors"
    assert attributes["rightsHolder"] == "Example rights holder"
    assert attributes["source_revision"] == "abc123"
    assert attributes["networkType"] == "directed causal mechanism network"
    declarations = aspects["attributeDeclarations"][0]["networkAttributes"]
    assert declarations["networkType"] == {"d": "string"}
    assert record["status"] == "EXPORTED"
    assert manifest["summary"] == {
        "disorder_count": 1,
        "exported_count": 1,
        "skipped_count": 0,
        "export_defect_count": 0,
        "retired_network_count": 0,
    }
    assert manifest_path.exists()


@pytest.mark.parametrize(
    ("initial_status", "expect_update"),
    [("EXPORTED", True), ("UPLOADED_PRIVATE", False)],
)
def test_publish_release_uses_manifest_uuid_resumes_and_verifies_before_public(
    tmp_path: Path, monkeypatch, initial_status: str, expect_update: bool
) -> None:
    output_path = tmp_path / "Example_Disease.cx2.json"
    serialized = '[{"CXVersion":"2.0"}]'
    output_path.write_text(serialized)
    manifest_path = tmp_path / "manifest.json"
    manifest = {
        "source_revision": "abc123",
        "release_metadata": _metadata(),
        "summary": {},
        "export_defects": [],
        "networks": [
            {
                "slug": "Example_Disease",
                "name": "Example Disease",
                "output_path": str(output_path),
                "node_count": 2,
                "edge_count": 1,
                "sha256": hashlib.sha256(serialized.encode()).hexdigest(),
                "ndex_uuid": "stable-uuid",
                "status": initial_status,
                "staging_visibility": "PUBLIC",
            }
        ],
    }
    calls: list[tuple] = []
    state = {"visibility": "PUBLIC", "indexLevel": "META"}

    class FakeNdex2:
        def __init__(self, *, host, username, password):
            assert host == "https://www.ndexbio.org"
            assert username == "user"
            assert password == "secret"

        def make_network_private(self, network_id):
            calls.append(("private", network_id))
            state["visibility"] = "PRIVATE"

        def update_cx2_network(self, stream, network_id):
            calls.append(("update", network_id, json.load(stream)))

        def set_network_system_properties(self, network_id, properties):
            calls.append(("properties", network_id, properties))
            state["visibility"] = properties["visibility"]
            state["indexLevel"] = properties["index_level"]

        def make_network_public(self, network_id):
            calls.append(("public", network_id))
            state["visibility"] = "PUBLIC"

        def get_network_summary(self, network_id):
            return {
                "externalId": network_id,
                "name": "Example Disease",
                "version": "2026-09-test",
                "nodeCount": 2,
                "edgeCount": 1,
                "visibility": state["visibility"],
                "indexLevel": state["indexLevel"],
                "completed": True,
                "isValid": True,
                "warnings": [],
                "hasLayout": True,
                "properties": [
                    {"predicateString": key, "value": value}
                    for key, value in {
                        "author": "DisMech contributors",
                        "rights": "BSD-3-Clause",
                        "rightsHolder": "Example rights holder",
                        "source_revision": "abc123",
                    }.items()
                ],
            }

    monkeypatch.setattr(ndex_publish, "Ndex2", FakeNdex2)
    result = ndex_publish.publish_release(
        manifest,
        manifest_path=manifest_path,
        host="https://www.ndexbio.org",
        username="user",
        password="secret",
        visibility="PUBLIC",
        index_level="META",
    )

    assert any(call[0] == "update" for call in calls) is expect_update
    if expect_update:
        assert calls[0][0] == "update"
    assert not any(call[0] == "private" for call in calls)
    assert not any(call[0] == "public" for call in calls)
    assert not any(call[0] == "delete" for call in calls)
    assert result["networks"][0]["status"] == "VERIFIED_PUBLIC"
    assert result["summary"]["processed_count"] == 1


def test_publish_release_rejects_non_https_host(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="HTTPS"):
        ndex_publish.publish_release(
            {"release_metadata": _metadata(), "source_revision": "abc", "networks": []},
            manifest_path=tmp_path / "manifest.json",
            host="http://www.ndexbio.org",
            username="user",
            password="secret",
            visibility="PRIVATE",
            index_level="META",
        )


def test_verification_tolerates_one_completed_stale_summary() -> None:
    calls = 0

    class FakeClient:
        def get_network_summary(self, network_id):
            nonlocal calls
            calls += 1
            return {
                "name": "Example Disease",
                "version": "2026-09-test",
                "nodeCount": 1 if calls == 1 else 2,
                "edgeCount": 1,
                "visibility": "PRIVATE",
                "indexLevel": "META",
                "completed": True,
                "isValid": True,
                "warnings": [],
                "hasLayout": True,
                "properties": [
                    {"predicateString": key, "value": value}
                    for key, value in {
                        "author": "DisMech contributors",
                        "rights": "BSD-3-Clause",
                        "rightsHolder": "Example rights holder",
                        "source_revision": "abc123",
                    }.items()
                ],
            }

    summary = ndex_publish._wait_for_valid_summary(
        FakeClient(),
        "stable-uuid",
        record={"name": "Example Disease", "node_count": 2, "edge_count": 1},
        metadata=_metadata() | {"source_revision": "abc123"},
        expected_visibility="PRIVATE",
        expected_index_level="META",
        interval_seconds=0,
    )

    assert calls == 2
    assert summary["nodeCount"] == 2


def test_build_release_records_defects_before_refusing(tmp_path: Path) -> None:
    kb_dir = tmp_path / "kb"
    kb_dir.mkdir()
    disorder_path = kb_dir / "Example_Disease.yaml"
    _write_disorder(disorder_path)
    disorder = yaml.safe_load(disorder_path.read_text())
    disorder["pathophysiology"][0]["downstream"][0]["target"] = "Missing node"
    disorder_path.write_text(yaml.safe_dump(disorder, sort_keys=False))
    manifest_path = tmp_path / "manifest.json"

    with pytest.raises(RuntimeError, match="export defect"):
        ndex_publish.build_release(
            kb_dir=kb_dir,
            output_dir=tmp_path / "cx2",
            manifest_path=manifest_path,
            previous_manifest_path=None,
            release_metadata=_metadata(),
            source_revision="abc123",
            fail_on_export_defects=True,
            require_disease_metadata=True,
        )

    manifest = json.loads(manifest_path.read_text())
    assert manifest["summary"]["export_defect_count"] == 1
    assert manifest["export_defects"] == ["Example_Disease: 1 orphan node(s)"]


def test_build_release_reports_retired_networks(tmp_path: Path) -> None:
    kb_dir = tmp_path / "kb"
    kb_dir.mkdir()
    _write_disorder(kb_dir / "Example_Disease.yaml")
    previous_path = tmp_path / "uuid-registry.json"
    previous_path.write_text(
        json.dumps(
            {
                "networks": [
                    {
                        "slug": "Retired_Disease",
                        "ndex_uuid": "retired-uuid",
                        "status": "ACTIVE",
                    }
                ]
            }
        )
    )

    manifest = ndex_publish.build_release(
        kb_dir=kb_dir,
        output_dir=tmp_path / "cx2",
        manifest_path=tmp_path / "manifest.json",
        previous_manifest_path=previous_path,
        release_metadata=_metadata(),
        source_revision="abc123",
        fail_on_export_defects=True,
        require_disease_metadata=True,
    )

    assert manifest["summary"]["retired_network_count"] == 1
    assert manifest["retired_networks"] == [
        {
            "slug": "Retired_Disease",
            "ndex_uuid": "retired-uuid",
            "previous_status": "ACTIVE",
        }
    ]


def test_publish_release_rechecks_defects_and_content_hash(tmp_path: Path) -> None:
    output_path = tmp_path / "Example_Disease.cx2.json"
    output_path.write_text('[{"CXVersion":"2.0"}]')
    manifest = {
        "source_revision": "abc123",
        "release_metadata": _metadata(),
        "summary": {},
        "export_defects": ["Example_Disease: 1 orphan node(s)"],
        "networks": [
            {
                "slug": "Example_Disease",
                "output_path": str(output_path),
                "sha256": "wrong-hash",
                "status": "EXPORTED",
            }
        ],
    }

    with pytest.raises(RuntimeError, match="manifest contains 1 export defect"):
        ndex_publish.publish_release(
            manifest,
            manifest_path=tmp_path / "manifest.json",
            host="https://www.ndexbio.org",
            username="user",
            password="secret",
            visibility="PRIVATE",
            index_level="META",
        )
    manifest["export_defects"] = []
    with pytest.raises(RuntimeError, match="expected sha256"):
        ndex_publish.publish_release(
            manifest,
            manifest_path=tmp_path / "manifest.json",
            host="https://www.ndexbio.org",
            username="user",
            password="secret",
            visibility="PRIVATE",
            index_level="META",
        )


def test_publish_release_mints_and_checkpoints_new_uuid(
    tmp_path: Path, monkeypatch
) -> None:
    serialized = '[{"CXVersion":"2.0"}]'
    output_path = tmp_path / "Example_Disease.cx2.json"
    output_path.write_text(serialized)
    manifest_path = tmp_path / "manifest.json"
    manifest = {
        "source_revision": "abc123",
        "release_metadata": _metadata(),
        "summary": {},
        "export_defects": [],
        "retired_networks": [],
        "networks": [
            {
                "slug": "Example_Disease",
                "name": "Example Disease",
                "output_path": str(output_path),
                "sha256": hashlib.sha256(serialized.encode()).hexdigest(),
                "node_count": 2,
                "edge_count": 1,
                "ndex_uuid": None,
                "status": "EXPORTED",
            }
        ],
    }

    class FakeNdex2:
        def __init__(self, **kwargs):
            pass

        def save_new_cx2_network(self, cx2, visibility):
            assert visibility == "PRIVATE"
            return "https://www.ndexbio.org/v2/network/new-uuid"

        def set_network_system_properties(self, network_id, properties):
            checkpoint = json.loads(manifest_path.read_text())
            assert checkpoint["networks"][0]["ndex_uuid"] == "new-uuid"

        def get_network_summary(self, network_id):
            return {
                "name": "Example Disease",
                "version": "2026-09-test",
                "nodeCount": 2,
                "edgeCount": 1,
                "visibility": "PRIVATE",
                "indexLevel": "META",
                "completed": True,
                "isValid": True,
                "warnings": [],
                "hasLayout": True,
                "properties": [
                    {"predicateString": key, "value": value}
                    for key, value in {
                        "author": "DisMech contributors",
                        "rights": "BSD-3-Clause",
                        "rightsHolder": "Example rights holder",
                        "source_revision": "abc123",
                    }.items()
                ],
            }

    monkeypatch.setattr(ndex_publish, "Ndex2", FakeNdex2)
    result = ndex_publish.publish_release(
        manifest,
        manifest_path=manifest_path,
        host="https://www.ndexbio.org",
        username="user",
        password="secret",
        visibility="PRIVATE",
        index_level="META",
    )
    registry_path = tmp_path / "uuid-registry.json"
    registry = ndex_publish.write_uuid_registry(result, registry_path)

    assert result["networks"][0]["ndex_uuid"] == "new-uuid"
    assert result["networks"][0]["status"] == "VERIFIED_PRIVATE"
    assert registry == {
        "schema_version": "1.0",
        "networks": [
            {
                "slug": "Example_Disease",
                "ndex_uuid": "new-uuid",
                "status": "ACTIVE",
            }
        ],
    }
