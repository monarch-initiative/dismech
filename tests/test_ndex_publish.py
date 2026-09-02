"""Tests for versioned NDEx release construction and publication."""

from __future__ import annotations

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


def _metadata() -> dict[str, str]:
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
    assert record["status"] == "EXPORTED"
    assert manifest["summary"] == {
        "disorder_count": 1,
        "exported_count": 1,
        "skipped_count": 0,
        "export_defect_count": 0,
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
    output_path.write_text('[{"CXVersion":"2.0"}]')
    manifest_path = tmp_path / "manifest.json"
    manifest = {
        "source_revision": "abc123",
        "release_metadata": _metadata(),
        "summary": {},
        "networks": [
            {
                "slug": "Example_Disease",
                "name": "Example Disease",
                "output_path": str(output_path),
                "node_count": 2,
                "edge_count": 1,
                "ndex_uuid": "stable-uuid",
                "status": initial_status,
            }
        ],
    }
    calls: list[tuple] = []
    state = {"visibility": "PRIVATE", "indexLevel": "META"}

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
        assert calls[0] == ("private", "stable-uuid")
    assert calls[-1] == ("public", "stable-uuid")
    assert not any(call[0] == "delete" for call in calls)
    assert result["networks"][0]["status"] == "VERIFIED_PUBLIC"
    assert result["summary"]["processed_count"] == 1


def test_publish_release_rejects_non_https_host(tmp_path: Path) -> None:
    try:
        ndex_publish.publish_release(
            {"release_metadata": _metadata(), "source_revision": "abc", "networks": []},
            manifest_path=tmp_path / "manifest.json",
            host="http://www.ndexbio.org",
            username="user",
            password="secret",
            visibility="PRIVATE",
            index_level="META",
        )
    except ValueError as error:
        assert "HTTPS" in str(error)
    else:  # pragma: no cover
        raise AssertionError("non-HTTPS publication host was accepted")
