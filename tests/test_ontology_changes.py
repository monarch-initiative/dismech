"""Contract tests for proposed ontology edits and their independent lifecycles."""

import copy
import hashlib
import json

import pytest
import yaml

from dismech.ontology_changes import (
    load_registry,
    load_registry_bundle,
    main,
    render_request,
    validate_change_set,
    validate_record,
)
from dismech.repo_root import repo_root


@pytest.fixture
def proposal(tmp_path):
    artifact = tmp_path / "source.json"
    artifact.write_text('{"mapping": "old"}\n')
    return {
        "id": "mondo-example-change",
        "title": "Correct mapping scope",
        "change_type": "MAPPING_PREDICATE_CHANGE",
        "ontology": "MONDO",
        "about_node": {"id": "MONDO:0019503", "label": "anterior segment dysgenesis"},
        "mapping_target": {
            "id": "icd11.foundation:943599144",
            "label": "Broader category",
        },
        "mapping_representation": "MONDO_XREF_QUALIFIER",
        "old_value": "MONDO:equivalentTo",
        "new_value": "MONDO:mondoIsNarrowerThanSource",
        "origin": "SELF_PROPOSED",
        "confidence": "HIGH",
        "request_status": "NOT_FILED",
        "adoption_status": "NOT_APPLICABLE",
        "adoption_notes": "No local mapping uses the disputed target.",
        "justification": "Source definitions show the target has broader scope.",
        "ontology_state_verified": "2026-09-21",
        "source_snapshots": [
            {
                "id": "source",
                "resource": "MONDO",
                "version": "2026-09-01",
                "url": "https://example.org/2026-09-01/mondo.obo",
                "checked_at": "2026-09-21",
                "artifact": {
                    "path": "source.json",
                    "sha256": hashlib.sha256(artifact.read_bytes()).hexdigest(),
                },
            }
        ],
        "evidence": [
            {
                "source": "source",
                "locator": "/mapping",
                "observation": "Target is broader.",
                "supporting_text": "old",
            }
        ],
    }


def test_committed_registry():
    records, errors = load_registry()
    assert not errors
    assert records


@pytest.mark.parametrize(
    "field",
    [
        "mapping_target",
        "mapping_representation",
        "old_value",
        "new_value",
        "confidence",
        "request_status",
        "justification",
        "source_snapshots",
        "evidence",
    ],
)
def test_missing_proposal_information_rejected(proposal, tmp_path, field):
    del proposal[field]
    assert validate_record(proposal, tmp_path)


@pytest.mark.parametrize(
    "field,value",
    [
        ("new_value", "MONDO:equivalentTo"),
        ("new_value", "skos:broadMatch"),
        ("new_value", "not a CURIE"),
        ("confidence", 0.9),
        ("request_status", "FILED"),
        ("adoption_status", "ACCEPTED"),
        ("ontology_state_verified", "2026-02-30"),
        ("ontology_state_verified", "2026-09-22"),
        ("justification", "  "),
        ("stance", "AGREE"),
        ("unknown_field", "silently ignore this"),
        ("mapping_target", {"id": "broken", "label": "Bad identifier"}),
        ("source_snapshots", []),
        ("evidence", []),
        ("new_value", None),
    ],
)
def test_invalid_record_rejected(proposal, tmp_path, field, value):
    proposal[field] = value
    assert validate_record(proposal, tmp_path)


def test_upstream_origin_has_no_outbound_request(proposal, tmp_path):
    proposal.update(
        origin="UPSTREAM_APPLIED",
        stance="AGREE",
        adoption_status="NOT_STARTED",
        upstream_tracker_issue="https://github.com/monarch-initiative/mondo/issues/1",
    )
    assert validate_record(proposal, tmp_path)
    del proposal["confidence"], proposal["request_status"]
    assert not validate_record(proposal, tmp_path)


def test_filed_request_and_local_adoption_are_independent(proposal, tmp_path):
    proposal.update(
        request_status="ACCEPTED",
        adoption_status="NOT_STARTED",
        pull_request="https://github.com/monarch-initiative/mondo/pull/1",
    )
    assert not validate_record(proposal, tmp_path)


def test_unfiled_record_cannot_claim_upstream_submission(proposal, tmp_path):
    proposal["pull_request"] = "https://github.com/monarch-initiative/mondo/pull/1"
    assert validate_record(proposal, tmp_path)


@pytest.mark.parametrize("path", ["missing.json", "../source.json", "/tmp/source.json"])
def test_invalid_artifact_path_rejected(proposal, tmp_path, path):
    proposal["source_snapshots"][0]["artifact"]["path"] = path
    assert validate_record(proposal, tmp_path)


def test_changed_artifact_rejected(proposal, tmp_path):
    (tmp_path / "source.json").write_text("Changed after capture")
    assert any("checksum mismatch" in e for e in validate_record(proposal, tmp_path))


def test_unknown_evidence_source_rejected(proposal, tmp_path):
    proposal["evidence"][0]["source"] = "not-captured"
    assert validate_record(proposal, tmp_path)


def test_unverifiable_quote_rejected(proposal, tmp_path):
    proposal["evidence"][0]["supporting_text"] = "Invented source text"
    assert any(
        "supporting_text not found" in e for e in validate_record(proposal, tmp_path)
    )


def test_decoded_json_quote(proposal, tmp_path):
    path = tmp_path / "source.json"
    path.write_text(json.dumps({"definition": 'Quoted "text" with\na line break'}))
    proposal["source_snapshots"][0]["artifact"]["sha256"] = hashlib.sha256(
        path.read_bytes()
    ).hexdigest()
    proposal["evidence"][0]["supporting_text"] = '"text" with\na line break'
    assert not validate_record(proposal, tmp_path)


def test_json_syntax_is_not_supporting_text(proposal, tmp_path):
    proposal["evidence"][0]["supporting_text"] = '"mapping": "old"'
    assert any(
        "supporting_text not found" in e for e in validate_record(proposal, tmp_path)
    )


def test_duplicate_snapshot_ids_rejected(proposal, tmp_path):
    proposal["source_snapshots"].append(copy.deepcopy(proposal["source_snapshots"][0]))
    assert validate_record(proposal, tmp_path)


def test_missing_affected_record_rejected(proposal, tmp_path):
    proposal["affected_records"] = ["kb/disorders/NotThere.yaml"]
    assert validate_record(proposal, tmp_path)


@pytest.mark.parametrize(
    "kind,fields",
    [
        (
            "MAPPING_CREATION",
            {
                "mapping_target": {"id": "X:1", "label": "External term"},
                "mapping_representation": "RDF_PREDICATE",
                "new_value": "skos:exactMatch",
            },
        ),
        (
            "REMOVE_MAPPING",
            {
                "mapping_target": {"id": "X:1", "label": "External term"},
                "mapping_representation": "RDF_PREDICATE",
                "old_value": "skos:exactMatch",
            },
        ),
        ("NODE_RENAME", {"old_value": "Old name", "new_value": "New name"}),
        (
            "NODE_TEXT_DEFINITION_CHANGE",
            {"old_value": "Old definition", "new_value": "New definition"},
        ),
        (
            "EDGE_CREATION",
            {
                "predicate": "rdfs:subClassOf",
                "edge_object": {"id": "MONDO:0000001", "label": "disease"},
            },
        ),
        (
            "EDGE_DELETION",
            {
                "predicate": "rdfs:subClassOf",
                "edge_object": {"id": "MONDO:0000001", "label": "disease"},
            },
        ),
    ],
)
def test_supported_change_shapes(proposal, tmp_path, kind, fields):
    for field in ("mapping_target", "mapping_representation", "old_value", "new_value"):
        del proposal[field]
    proposal.update(change_type=kind, **fields)
    assert not validate_record(proposal, tmp_path)
    proposal["mapping_target"] = {"id": "X:2", "label": "Stray field"}
    if kind not in {"REMOVE_MAPPING", "MAPPING_CREATION"}:
        assert validate_record(proposal, tmp_path)


@pytest.mark.parametrize(
    "mutation",
    [
        "old_value",
        "missing_target",
        "missing_representation",
        "missing_value",
        "skos",
        "not_curie",
        "owner",
    ],
)
def test_mapping_creation_requires_absent_old_value_and_native_qualifier(
    proposal, tmp_path, mutation
):
    proposal["change_type"] = "MAPPING_CREATION"
    del proposal["old_value"]
    assert not validate_record(proposal, tmp_path)
    if mutation == "old_value":
        proposal["old_value"] = "MONDO:equivalentTo"
    elif mutation.startswith("missing_"):
        field = {
            "missing_target": "mapping_target",
            "missing_representation": "mapping_representation",
            "missing_value": "new_value",
        }[mutation]
        del proposal[field]
    elif mutation == "owner":
        proposal["about_node"]["id"] = "DOID:1"
    else:
        proposal["new_value"] = (
            "skos:exactMatch" if mutation == "skos" else "not a CURIE"
        )
    assert validate_record(proposal, tmp_path)


def write_registry(proposal, tmp_path):
    directory = tmp_path / "ontology_changes"
    directory.mkdir()
    path = directory / f"{proposal['id']}.yaml"
    path.write_text(yaml.safe_dump(proposal, sort_keys=False))
    return path


def test_duplicate_yaml_keys_rejected(proposal, tmp_path):
    path = write_registry(proposal, tmp_path)
    path.write_text(path.read_text() + "request_status: ACCEPTED\n")
    assert any("duplicate YAML keys" in e for e in load_registry(tmp_path)[1])


def test_registry_identity_rejected(proposal, tmp_path):
    path = write_registry(proposal, tmp_path)
    path.rename(path.with_name("wrong-name.yaml"))
    assert any("filename stem" in e for e in load_registry(tmp_path)[1])


def test_list_and_export(proposal, tmp_path, capsys):
    write_registry(proposal, tmp_path)
    args = ["--root", str(tmp_path)]
    assert (
        main(args + ["list", "--ontology", "MONDO", "--request-status", "NOT_FILED"])
        == 0
    )
    assert (
        json.loads(capsys.readouterr().out)[0]["mapping_target"]
        == proposal["mapping_target"]
    )
    assert main(args + ["list", "--ontology", "GO"]) == 0
    assert json.loads(capsys.readouterr().out) == []
    assert main(args + ["export", proposal["id"]]) == 0
    exported = capsys.readouterr().out
    assert exported == render_request(proposal)
    assert "icd11.foundation:943599144" in exported
    assert "MONDO:mondoIsNarrowerThanSource" in exported
    assert "NOT_FILED" in exported
    assert main(args + ["export", "absent"]) == 1


def test_invalid_registry_cannot_be_exported(proposal, tmp_path, capsys):
    proposal["request_status"] = "ACCEPTED"
    write_registry(proposal, tmp_path)
    assert main(["--root", str(tmp_path), "export", proposal["id"]]) == 1
    assert not capsys.readouterr().out


def test_default_registry_follows_working_tree_after_import(
    proposal, tmp_path, monkeypatch, capsys
):
    monkeypatch.delenv("DISMECH_ROOT", raising=False)
    for name in ("first", "second"):
        tree = tmp_path / name
        (tree / "kb").mkdir(parents=True)
        (tree / "justfile").write_text("")
        (tree / "source.json").write_bytes((tmp_path / "source.json").read_bytes())
        proposal["title"] = name
        write_registry(proposal, tree)
        monkeypatch.chdir(tree / "kb")
        assert not validate_record(proposal)
        records, errors = load_registry()
        assert not errors
        assert records[0]["title"] == name
        assert main(["list"]) == 0
        assert json.loads(capsys.readouterr().out)[0]["title"] == name


def test_registry_honors_environment_override(proposal, tmp_path, monkeypatch, capsys):
    write_registry(proposal, tmp_path)
    monkeypatch.setenv("DISMECH_ROOT", str(tmp_path))
    assert main(["validate"]) == 0
    assert "Validated 1" in capsys.readouterr().out


def test_proposal_only_changes_one_current_mondo_qualifier():
    records, errors = load_registry()
    assert not errors
    record = next(
        r
        for r in records
        if r["id"] == "mondo-0019503-icd11-anterior-segment-broad-match"
    )
    source = next(s for s in record["source_snapshots"] if s["id"] == "mondo-current")
    stanza = json.loads((repo_root() / source["artifact"]["path"]).read_text())[
        "stanza"
    ]
    target_line = next(
        line
        for line in stanza.splitlines()
        if line.startswith(f"xref: {record['mapping_target']['id']} ")
    )
    assert f'source="{record["old_value"]}"' in target_line
    assert 'xref: icd11.foundation:1182282997 {source="MONDO:equivalentTo"}' in stanza
    assert record["new_value"] == "MONDO:mondoIsNarrowerThanSource"


@pytest.fixture
def mapping_move(proposal, tmp_path):
    removal = copy.deepcopy(proposal)
    removal.update(id="mondo-example-removal", change_type="REMOVE_MAPPING")
    del removal["new_value"]
    creation = copy.deepcopy(proposal)
    creation.update(
        id="mondo-example-creation",
        change_type="MAPPING_CREATION",
        about_node={"id": "MONDO:0000002", "label": "New subject"},
        new_value=removal["old_value"],
    )
    del creation["old_value"]
    change_set = {
        "id": "mondo-example-move",
        "title": "Move mapping to the matching subtype",
        "change_set_type": "MAPPING_MOVE",
        "removal": removal["id"],
        "creation": creation["id"],
    }
    for record in (removal, creation):
        assert not validate_record(record, tmp_path)
    return change_set, {r["id"]: r for r in (removal, creation)}


def write_move(mapping_move, tmp_path):
    change_set, proposals = mapping_move
    directory = tmp_path / "ontology_changes"
    directory.mkdir(exist_ok=True)
    sets = directory / "change_sets"
    sets.mkdir(exist_ok=True)
    for record in proposals.values():
        (directory / f"{record['id']}.yaml").write_text(yaml.safe_dump(record))
    path = sets / f"{change_set['id']}.yaml"
    path.write_text(yaml.safe_dump(change_set))
    return path


@pytest.mark.parametrize("role", ["removal", "creation"])
def test_change_set_requires_both_typed_references(mapping_move, role):
    change_set, proposals = mapping_move
    assert not validate_change_set(change_set, proposals)
    member = change_set.pop(role)
    assert validate_change_set(change_set, proposals)
    change_set[role] = "missing-proposal"
    assert any(
        "unknown proposal" in e for e in validate_change_set(change_set, proposals)
    )
    change_set[role] = change_set["creation" if role == "removal" else "removal"]
    assert any(
        "must reference" in e for e in validate_change_set(change_set, proposals)
    )
    change_set[role] = member
    assert not validate_change_set(change_set, proposals)


@pytest.mark.parametrize(
    "field,value,message",
    [
        ("ontology", "DOID", "retain ontology"),
        ("mapping_representation", "RDF_PREDICATE", "retain mapping_representation"),
        (
            "mapping_target",
            {"id": "X:2", "label": "Different target"},
            "retain mapping_target",
        ),
        ("new_value", "MONDO:relatedTo", "retain predicate/qualifier"),
        (
            "about_node",
            {"id": "MONDO:0019503", "label": "Same subject"},
            "distinct old and new subjects",
        ),
    ],
)
def test_move_changes_only_the_subject(mapping_move, field, value, message):
    change_set, proposals = mapping_move
    proposals[change_set["creation"]][field] = value
    assert any(message in e for e in validate_change_set(change_set, proposals))


@pytest.mark.parametrize(
    "field,value",
    [("request_status", "ACCEPTED"), ("title", " "), ("change_set_type", "OTHER")],
)
def test_change_set_has_no_duplicate_lifecycle_or_freeform_kind(
    mapping_move, field, value
):
    change_set, proposals = mapping_move
    change_set[field] = value
    assert validate_change_set(change_set, proposals)


def test_registry_rejects_broken_sets_and_export_fails_closed(
    mapping_move, tmp_path, capsys
):
    path = write_move(mapping_move, tmp_path)
    change_set, _ = mapping_move
    (tmp_path / "ontology_changes" / f"{change_set['creation']}.yaml").unlink()
    assert any("unknown proposal" in e for e in load_registry(tmp_path)[1])
    assert main(["--root", str(tmp_path), "export", change_set["removal"]]) == 1
    assert not capsys.readouterr().out
    path.unlink()
    assert not load_registry(tmp_path)[1]  # Standalone removals remain valid.


def test_member_cannot_belong_to_two_sets(mapping_move, tmp_path):
    path = write_move(mapping_move, tmp_path)
    change_set, _ = mapping_move
    other = dict(change_set, id="mondo-second-move")
    (path.parent / "mondo-second-move.yaml").write_text(yaml.safe_dump(other))
    assert any("multiple change sets" in e for e in load_registry(tmp_path)[1])


@pytest.mark.parametrize("defect", ["filename", "duplicate_key", "id_collision"])
def test_change_set_registry_identity(mapping_move, tmp_path, defect):
    path = write_move(mapping_move, tmp_path)
    change_set, _ = mapping_move
    if defect == "filename":
        path.rename(path.with_name("wrong-name.yaml"))
    elif defect == "duplicate_key":
        path.write_text(path.read_text() + "title: Duplicate\n")
    else:
        change_set["id"] = change_set["removal"]
        path.unlink()
        write_move(mapping_move, tmp_path)
    assert load_registry(tmp_path)[1]


def test_move_queries_and_export_show_both_halves_with_partial_status(
    mapping_move, tmp_path, capsys
):
    change_set, proposals = mapping_move
    removal = proposals[change_set["removal"]]
    removal.update(request_status="ACCEPTED", pull_request="https://example.org/pull/1")
    write_move(mapping_move, tmp_path)
    records, sets, errors = load_registry_bundle(tmp_path)
    assert not errors
    assert len(records) == 2 and sets == [change_set]
    args = ["--root", str(tmp_path)]
    assert main(args + ["list-change-sets"]) == 0
    assert json.loads(capsys.readouterr().out) == [change_set]
    assert main(args + ["list", "--change-set", change_set["id"]]) == 0
    assert {r["id"] for r in json.loads(capsys.readouterr().out)} == set(proposals)
    assert (
        main(
            args
            + ["list", "--change-set", change_set["id"], "--request-status", "ACCEPTED"]
        )
        == 0
    )
    assert [r["id"] for r in json.loads(capsys.readouterr().out)] == [removal["id"]]
    assert main(args + ["list", "--change-set", "missing-move"]) == 1
    capsys.readouterr()
    outputs = []
    for key in (change_set["id"], change_set["removal"], change_set["creation"]):
        assert main(args + ["export", key]) == 0
        outputs.append(capsys.readouterr().out)
    assert outputs[0] == outputs[1] == outputs[2]
    for expected in (
        "MONDO:0019503",
        "MONDO:0000002",
        "icd11.foundation:943599144",
        "Mapping absent",
        "request: ACCEPTED",
        "request: NOT_FILED",
    ):
        assert expected in outputs[0]


def test_committed_moves_preserve_atomic_records():
    records, sets, errors = load_registry_bundle()
    assert not errors
    assert {s["id"] for s in sets} >= {
        "mondo-gorlin-ptch1-mapping-move",
        "mondo-praas1-mapping-move",
    }
    by_id = {r["id"]: r for r in records}
    for change_set in sets:
        removal, creation = (
            by_id[change_set[role]] for role in ("removal", "creation")
        )
        assert "new_value" not in removal and "old_value" not in creation
