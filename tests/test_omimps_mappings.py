"""Series mappings retain scope and cannot silently become OMIM member IDs."""

import copy
import subprocess
import sys
from pathlib import Path

import pytest
import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin

from dismech.render import render_disorder, render_grouping

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "src/dismech/schema/dismech.yaml"
MAPPING = {
    "term": {"id": "OMIMPS:209900", "label": "Bardet-Biedl syndrome"},
    "mapping_predicate": "skos:exactMatch",
    "mapping_source": "OMIM phenotypic series",
    "mapping_justification": "Series-level scope; no assertion of member completeness.",
}


def document(target_class):
    data = {
        "name": "Series fixture",
        "mappings": {"omimps_mappings": [copy.deepcopy(MAPPING)]},
    }
    if target_class == "Grouping":
        data["members"] = [{"member": "Member disease", "member_type": "DISEASE"}]
    return data


@pytest.fixture(scope="module")
def validator():
    return Validator(
        SCHEMA, validation_plugins=[JsonschemaValidationPlugin(closed=True)]
    )


@pytest.mark.parametrize("target_class", ["Disease", "Subtype", "Grouping"])
@pytest.mark.parametrize("defect", [None, "individual_record", "missing_justification"])
def test_series_mapping_schema(validator, target_class, defect):
    data = document(target_class)
    mapping = data["mappings"]["omimps_mappings"][0]
    if defect == "individual_record":
        mapping["term"]["id"] = "OMIM:209900"
    elif defect == "missing_justification":
        del mapping["mapping_justification"]
    errors = [
        r
        for r in validator.validate(data, target_class=target_class).results
        if r.severity.name == "ERROR"
    ]
    assert bool(errors) == bool(defect), errors


@pytest.mark.parametrize("target_class", ["Disease", "Grouping"])
@pytest.mark.parametrize("label", ["Bardet-Biedl syndrome", "Wrong series label"])
def test_series_labels_checked_offline(tmp_path, target_class, label):
    data = document(target_class)
    data["mappings"]["omimps_mappings"][0]["term"]["label"] = label
    path = tmp_path / "series.yaml"
    path.write_text(yaml.safe_dump(data))
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "linkml_term_validator.cli",
            "validate-data",
            str(path),
            "-s",
            str(SCHEMA),
            "-t",
            target_class,
            "--labels",
            "--no-dynamic-enums",
            "--offline",
            "-c",
            str(ROOT / "conf/oak_config.yaml"),
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    output = result.stdout + result.stderr
    assert (result.returncode == 0) == (label == "Bardet-Biedl syndrome"), output
    if result.returncode:
        assert "Bardet-Biedl syndrome" in output
        assert "OMIMPS:209900" in output


@pytest.mark.parametrize("target_class", ["Disease", "Grouping"])
def test_render_series_scope_and_link(tmp_path, target_class):
    data = document(target_class)
    # Related mappings must retain their predicate and explanation in the page.
    data["mappings"]["omimps_mappings"][0]["mapping_predicate"] = "skos:relatedMatch"
    path = tmp_path / "Series.yaml"
    path.write_text(yaml.safe_dump(data))
    output = tmp_path / "Series.html"
    if target_class == "Disease":
        render_disorder(path, output_path=output)
    else:
        disorders = tmp_path / "disorders"
        disorders.mkdir()
        (disorders / "Member.yaml").write_text("name: Member disease\n")
        render_grouping(path, output_path=output, disorders_dir=disorders)
    html = output.read_text()
    # Ignore the raw YAML viewer: these must be rendered as page content.
    assert 'href="https://omim.org/phenotypicSeries/PS209900"' in html
    assert '<span class="predicate">skos:relatedMatch</span>' in html
    assert f'<p class="mapping-notes">{MAPPING["mapping_justification"]}</p>' in html
