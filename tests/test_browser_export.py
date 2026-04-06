"""Tests for browser data exporter."""

import tempfile
from pathlib import Path

import yaml

from dismech.export.browser_export import BrowserExporter


def test_extract_disorder_with_null_fields():
    """Test that extract_disorder handles null/None fields correctly."""
    # Create a disorder with fields explicitly set to None (like empty YAML fields)
    disorder = {
        "name": "Test Disorder",
        "category": "Test",
        "parents": [],
        "genetic": None,  # This is what causes the bug
        "treatments": None,
        "environmental": None,
        "biochemical": None,
        "has_subtypes": None,
        "pathophysiology": None,
        "phenotypes": None,
    }

    exporter = BrowserExporter()
    # This should not raise a TypeError
    record = exporter.extract_disorder(disorder, "test.yaml")

    # Verify that the record has empty lists for these fields
    assert record["genes"] == []
    assert record["treatments"] == []
    assert record["environmental"] == []
    assert record["biochemical"] == []
    assert record["subtypes"] == []
    assert record["pathophysiology"] == []
    assert record["phenotypes"] == []


def test_extract_disorder_with_valid_data():
    """Test that extract_disorder works correctly with valid data."""
    disorder = {
        "name": "Test Disorder",
        "category": "Test",
        "parents": ["Parent1"],
        "genetic": [
            {"name": "GENE1", "association": "Risk"},
            {"name": "GENE2", "association": "Pathogenic"},
        ],
        "treatments": [
            {"name": "Treatment A"},
            {"name": "Treatment B"},
        ],
        "environmental": [
            {"name": "Environmental Factor 1"},
        ],
        "biochemical": [
            {"name": "Biomarker 1"},
        ],
    }

    exporter = BrowserExporter()
    record = exporter.extract_disorder(disorder, "test.yaml")

    # Verify that the record has the expected data
    assert record["name"] == "Test Disorder"
    assert record["category"] == "Test"
    assert record["parents"] == ["Parent1"]
    assert record["genes"] == ["GENE1", "GENE2"]
    assert record["treatments"] == ["Treatment A", "Treatment B"]
    assert record["environmental"] == ["Environmental Factor 1"]
    assert record["biochemical"] == ["Biomarker 1"]


def test_export_to_js_with_problematic_file():
    """Test that export_to_js can handle files with null fields."""
    # Create a temporary YAML file with null fields
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        yaml_file = tmpdir_path / "test_disorder.yaml"

        # Write a YAML file with null fields (simulating empty fields in YAML)
        with open(yaml_file, "w") as f:
            f.write("""name: Test Disorder
category: Test
genetic:
treatments:
environmental:
biochemical:
""")

        # Load it to verify it has None values
        with open(yaml_file) as f:
            data = yaml.safe_load(f)
        assert data["genetic"] is None
        assert data["treatments"] is None

        # Now try to export it
        output_file = tmpdir_path / "output.js"
        exporter = BrowserExporter()

        # This should not raise a TypeError
        exporter.export_to_js([yaml_file], output_file)

        # Verify the output file was created
        assert output_file.exists()

        # Verify the content is valid JavaScript
        with open(output_file) as f:
            content = f.read()
        assert "window.searchData" in content
        assert "Test Disorder" in content
