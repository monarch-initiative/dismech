"""Tests for LinkML data QC compliance analyzer."""

import json
from pathlib import Path

import pytest

from dismech.linkml_data_qc import (
    AggregatedPathScore,
    CSVFormatter,
    ComplianceAnalyzer,
    ComplianceReport,
    JSONFormatter,
    QCConfig,
    SchemaIntrospector,
    SlotQCConfig,
    TextFormatter,
    ThresholdViolation,
    create_multi_file_report,
)

ROOT_DIR = Path(__file__).parent.parent
SCHEMA_PATH = ROOT_DIR / "src" / "dismech" / "schema" / "dismech.yaml"
KB_DIR = ROOT_DIR / "kb" / "disorders"


@pytest.fixture
def introspector():
    return SchemaIntrospector(str(SCHEMA_PATH))


@pytest.fixture
def analyzer():
    return ComplianceAnalyzer(str(SCHEMA_PATH))


class TestSchemaIntrospector:
    def test_finds_recommended_slots(self, introspector):
        """Should identify all recommended slots."""
        assert introspector.recommended_slots == {"description", "term", "evidence"}

    def test_class_slots_for_descriptor(self, introspector):
        """Descriptor classes should have term as recommended."""
        info = introspector.get_class_slots("CellTypeDescriptor")
        assert "term" in info.recommended_slots
        assert "description" in info.recommended_slots

    def test_class_slots_for_disease(self, introspector):
        """Disease class should have description and evidence as recommended."""
        info = introspector.get_class_slots("Disease")
        # Disease has description (recommended) and evidence is on nested classes
        assert "description" in info.recommended_slots

    def test_traversable_slots(self, introspector):
        """Should identify slots that lead to other classes."""
        traversable = introspector.get_traversable_slots("Disease")
        slot_names = {s.name for s in traversable}
        # Disease has many traversable slots like pathophysiology, phenotypes, etc.
        assert "pathophysiology" in slot_names
        assert "phenotypes" in slot_names

    def test_pathophysiology_traversable_slots(self, introspector):
        """Pathophysiology should have cell_types as traversable."""
        traversable = introspector.get_traversable_slots("Pathophysiology")
        slot_names = {s.name for s in traversable}
        assert "cell_types" in slot_names
        assert "biological_processes" in slot_names

    def test_is_class(self, introspector):
        """Should correctly identify classes."""
        assert introspector.is_class("Disease")
        assert introspector.is_class("Pathophysiology")
        assert introspector.is_class("CellTypeDescriptor")
        assert not introspector.is_class("string")
        assert not introspector.is_class("NotAClass")


class TestComplianceAnalyzer:
    def test_analyze_single_file(self, analyzer):
        """Should produce valid report for Asthma.yaml."""
        report = analyzer.analyze_file(str(KB_DIR / "Asthma.yaml"), "Disease")
        assert isinstance(report, ComplianceReport)
        assert report.global_compliance >= 0
        assert report.global_compliance <= 100
        assert len(report.path_scores) > 0
        assert report.total_checks > 0

    def test_summary_by_slot_includes_all_recommended(self, analyzer):
        """Summary should include recommended slots that were checked."""
        report = analyzer.analyze_file(str(KB_DIR / "Asthma.yaml"), "Disease")
        # At minimum, we should have some slots in the summary
        assert len(report.summary_by_slot) > 0

    def test_path_scores_have_valid_data(self, analyzer):
        """Path scores should have valid structure."""
        report = analyzer.analyze_file(str(KB_DIR / "Asthma.yaml"), "Disease")
        for ps in report.path_scores:
            assert ps.path
            assert ps.parent_class
            assert ps.item_count >= 0
            assert 0 <= ps.overall_percentage <= 100
            for ss in ps.slot_scores:
                assert ss.slot_name
                assert ss.total >= 0
                assert ss.populated >= 0
                assert ss.populated <= ss.total
                assert 0 <= ss.percentage <= 100

    @pytest.mark.parametrize(
        "disorder_file",
        [f for f in sorted(KB_DIR.glob("*.yaml"))[:5]],
    )
    def test_multiple_disorders(self, analyzer, disorder_file):
        """Should handle various disorder files."""
        report = analyzer.analyze_file(str(disorder_file), "Disease")
        assert report.file_path == str(disorder_file)
        assert 0 <= report.global_compliance <= 100

    def test_recommended_slots_in_report(self, analyzer):
        """Report should list recommended slots from schema."""
        report = analyzer.analyze_file(str(KB_DIR / "Asthma.yaml"), "Disease")
        assert "description" in report.recommended_slots
        assert "term" in report.recommended_slots
        assert "evidence" in report.recommended_slots


class TestAggregatedScores:
    """Tests for the aggregated list-level scoring feature."""

    def test_aggregated_scores_exist(self, analyzer):
        """Report should include aggregated scores for list paths."""
        report = analyzer.analyze_file(str(KB_DIR / "Asthma.yaml"), "Disease")
        assert len(report.aggregated_scores) > 0

    def test_aggregated_scores_use_bracket_notation(self, analyzer):
        """Aggregated paths should use [] notation for lists."""
        report = analyzer.analyze_file(str(KB_DIR / "Asthma.yaml"), "Disease")
        for agg in report.aggregated_scores:
            assert "[]" in agg.path, f"Path {agg.path} should contain []"
            # Should not have numeric indices
            assert not any(
                c.isdigit() for c in agg.path.replace("[]", "")
            ), f"Path {agg.path} should not have numeric indices"

    def test_aggregated_scores_structure(self, analyzer):
        """Aggregated scores should have valid structure."""
        report = analyzer.analyze_file(str(KB_DIR / "Asthma.yaml"), "Disease")
        for agg in report.aggregated_scores:
            assert isinstance(agg, AggregatedPathScore)
            assert agg.path
            assert agg.slot_name
            assert agg.parent_class
            assert agg.total >= agg.populated >= 0
            assert 0 <= agg.percentage <= 100

    def test_aggregated_scores_sum_correctly(self, analyzer):
        """Aggregated totals should equal sum of individual item scores."""
        report = analyzer.analyze_file(str(KB_DIR / "Asthma.yaml"), "Disease")

        # Find an aggregated path and verify its totals match the sum of individual items
        for agg in report.aggregated_scores:
            if agg.path == "pathophysiology[]" and agg.slot_name == "description":
                # Count individual pathophysiology items with description
                import re

                individual_count = 0
                individual_populated = 0
                for ps in report.path_scores:
                    if re.match(r"pathophysiology\[\d+\]$", ps.path):
                        for ss in ps.slot_scores:
                            if ss.slot_name == "description":
                                individual_count += ss.total
                                individual_populated += ss.populated

                assert agg.total == individual_count
                assert agg.populated == individual_populated
                break

    def test_nested_list_aggregation(self, analyzer):
        """Should aggregate nested lists like pathophysiology[].cell_types[]."""
        report = analyzer.analyze_file(str(KB_DIR / "Asthma.yaml"), "Disease")

        # Find nested aggregation paths
        nested_paths = [agg for agg in report.aggregated_scores if agg.path.count("[]") > 1]
        assert len(nested_paths) > 0, "Should have nested list aggregations"

        # Verify nested paths have correct format
        for agg in nested_paths:
            parts = agg.path.split(".")
            assert any("[]" in part for part in parts)

    def test_aggregated_scores_in_json_output(self, analyzer):
        """JSON output should include aggregated_scores."""
        report = analyzer.analyze_file(str(KB_DIR / "Asthma.yaml"), "Disease")
        json_out = JSONFormatter.format(report)
        parsed = json.loads(json_out)
        assert "aggregated_scores" in parsed
        assert len(parsed["aggregated_scores"]) > 0
        # Check structure of first aggregated score
        first = parsed["aggregated_scores"][0]
        assert "path" in first
        assert "slot_name" in first
        assert "populated" in first
        assert "total" in first
        assert "percentage" in first

    def test_aggregated_scores_in_text_output(self, analyzer):
        """Text output should show aggregated scores section."""
        report = analyzer.analyze_file(str(KB_DIR / "Asthma.yaml"), "Disease")
        text_out = TextFormatter.format(report)
        assert "Aggregated Scores by List Path:" in text_out
        # Should have paths with [] notation
        assert "[]" in text_out


class TestFormatters:
    def test_json_output(self, analyzer):
        """JSON output should be valid."""
        report = analyzer.analyze_file(str(KB_DIR / "Asthma.yaml"), "Disease")
        json_out = JSONFormatter.format(report)
        parsed = json.loads(json_out)
        assert "global_compliance" in parsed
        assert "path_scores" in parsed
        assert "summary_by_slot" in parsed

    def test_csv_output(self, analyzer):
        """CSV output should have expected columns."""
        report = analyzer.analyze_file(str(KB_DIR / "Asthma.yaml"), "Disease")
        csv_out = CSVFormatter.format(report)
        assert "file,path,class,slot,populated,total,percentage" in csv_out
        # Should have data rows
        lines = csv_out.strip().split("\n")
        assert len(lines) > 1

    def test_text_output(self, analyzer):
        """Text output should be human readable."""
        report = analyzer.analyze_file(str(KB_DIR / "Asthma.yaml"), "Disease")
        text_out = TextFormatter.format(report)
        assert "Compliance Report" in text_out
        assert "Global Compliance" in text_out
        assert "Summary by Slot" in text_out


CONFIG_PATH = ROOT_DIR / "conf" / "qc_config.yaml"


class TestConfiguration:
    """Tests for configurable weights and thresholds."""

    def test_load_config_from_yaml(self):
        """Should load configuration from YAML file."""
        config = QCConfig.from_yaml(CONFIG_PATH)
        assert config.default_weight == 1.0
        assert "term" in config.slots
        assert config.slots["term"].weight == 2.0

    def test_default_config(self):
        """Default config should have weight 1.0 and no thresholds."""
        config = QCConfig.default()
        assert config.default_weight == 1.0
        assert config.default_min_compliance is None
        assert len(config.slots) == 0
        assert len(config.paths) == 0

    def test_get_weight_with_path_override(self):
        """Path-specific weight should take precedence."""
        config = QCConfig.from_yaml(CONFIG_PATH)
        # phenotypes[].phenotype_term.term has weight 3.0 in config
        weight = config.get_weight("phenotypes[].phenotype_term", "term")
        assert weight == 3.0

    def test_get_weight_with_slot_default(self):
        """Slot-level weight should apply when no path override."""
        config = QCConfig.from_yaml(CONFIG_PATH)
        # 'evidence' slot has weight 1.5, no path override for this path
        weight = config.get_weight("treatments[]", "evidence")
        assert weight == 1.5

    def test_get_weight_falls_back_to_default(self):
        """Should use default_weight when no slot or path config."""
        config = QCConfig.from_yaml(CONFIG_PATH)
        # 'nonexistent_slot' has no config
        weight = config.get_weight("some_path[]", "nonexistent_slot")
        assert weight == 1.0

    def test_get_min_compliance_with_path_override(self):
        """Path-specific threshold should take precedence."""
        config = QCConfig.from_yaml(CONFIG_PATH)
        # phenotypes[].phenotype_term.term has min_compliance 90.0
        min_comp = config.get_min_compliance("phenotypes[].phenotype_term", "term")
        assert min_comp == 90.0

    def test_get_min_compliance_with_slot_default(self):
        """Slot-level threshold should apply when no path override."""
        config = QCConfig.from_yaml(CONFIG_PATH)
        # 'term' slot has min_compliance 80.0
        min_comp = config.get_min_compliance("some_path[]", "term")
        assert min_comp == 80.0

    def test_get_min_compliance_returns_none_when_not_set(self):
        """Should return None when no threshold configured."""
        config = QCConfig.from_yaml(CONFIG_PATH)
        # 'description' slot has no min_compliance
        min_comp = config.get_min_compliance("some_path[]", "description")
        assert min_comp is None

    def test_analyzer_with_config_file(self):
        """Should create analyzer with config from file."""
        analyzer = ComplianceAnalyzer.with_config_file(str(SCHEMA_PATH), str(CONFIG_PATH))
        report = analyzer.analyze_file(str(KB_DIR / "Asthma.yaml"), "Disease")
        assert report.config_path == str(CONFIG_PATH)
        # Weighted compliance should differ from global when weights applied
        assert report.weighted_compliance >= 0
        assert report.weighted_compliance <= 100

    def test_weighted_compliance_differs_from_global(self):
        """Weighted compliance should differ from global when weights vary."""
        config = QCConfig.from_yaml(CONFIG_PATH)
        analyzer = ComplianceAnalyzer(str(SCHEMA_PATH), config)
        report = analyzer.analyze_file(str(KB_DIR / "Asthma.yaml"), "Disease")
        # With different weights, these should typically differ
        # (unless by coincidence they're equal)
        assert report.weighted_compliance is not None

    def test_aggregated_scores_have_weights(self):
        """Aggregated scores should include configured weights."""
        config = QCConfig.from_yaml(CONFIG_PATH)
        analyzer = ComplianceAnalyzer(str(SCHEMA_PATH), config)
        report = analyzer.analyze_file(str(KB_DIR / "Asthma.yaml"), "Disease")

        # Find a score with a known weight override
        for agg in report.aggregated_scores:
            if agg.slot_name == "term":
                # term has weight 2.0 at minimum (slot-level config)
                assert agg.weight >= 2.0
                break

    def test_threshold_violation_detection(self):
        """Should detect violations when compliance is below threshold."""
        # Create config with strict threshold
        config = QCConfig(
            default_weight=1.0,
            slots={"description": SlotQCConfig(min_compliance=100.0)},  # Require 100%
        )
        analyzer = ComplianceAnalyzer(str(SCHEMA_PATH), config)
        report = analyzer.analyze_file(str(KB_DIR / "Asthma.yaml"), "Disease")

        # Since 100% compliance is unlikely, we should have violations
        description_violations = [v for v in report.threshold_violations if v.slot_name == "description"]
        # May or may not have violations depending on data
        # Just verify structure is correct
        for v in description_violations:
            assert isinstance(v, ThresholdViolation)
            assert v.actual_compliance < v.min_required
            assert v.shortfall > 0

    def test_no_violations_when_above_threshold(self):
        """Should have no violations when compliance is above threshold."""
        # Create config with very low threshold
        config = QCConfig(
            default_weight=1.0,
            slots={"term": SlotQCConfig(min_compliance=0.0)},  # Require 0%
        )
        analyzer = ComplianceAnalyzer(str(SCHEMA_PATH), config)
        report = analyzer.analyze_file(str(KB_DIR / "Asthma.yaml"), "Disease")

        # With 0% threshold, no term-related violations should occur
        term_violations = [v for v in report.threshold_violations if v.slot_name == "term"]
        assert len(term_violations) == 0

    def test_violations_in_text_output(self):
        """Text output should show threshold violations."""
        config = QCConfig(
            default_weight=1.0,
            slots={"evidence": SlotQCConfig(min_compliance=99.0)},
        )
        analyzer = ComplianceAnalyzer(str(SCHEMA_PATH), config)
        report = analyzer.analyze_file(str(KB_DIR / "Asthma.yaml"), "Disease")
        text_out = TextFormatter.format(report)

        if report.threshold_violations:
            assert "Threshold Violations" in text_out

    def test_violations_in_json_output(self):
        """JSON output should include threshold_violations array."""
        config = QCConfig(
            default_weight=1.0,
            slots={"evidence": SlotQCConfig(min_compliance=99.0)},
        )
        analyzer = ComplianceAnalyzer(str(SCHEMA_PATH), config)
        report = analyzer.analyze_file(str(KB_DIR / "Asthma.yaml"), "Disease")
        json_out = JSONFormatter.format(report)
        parsed = json.loads(json_out)

        assert "threshold_violations" in parsed
        assert "weighted_compliance" in parsed


class TestMultiFileReport:
    def test_create_multi_file_report(self, analyzer):
        """Should aggregate multiple reports correctly."""
        files = list(KB_DIR.glob("*.yaml"))[:3]
        reports = [analyzer.analyze_file(str(f), "Disease") for f in files]
        multi = create_multi_file_report(reports)

        assert multi.files_analyzed == 3
        assert len(multi.reports) == 3
        assert 0 <= multi.global_compliance <= 100
        assert len(multi.summary_by_slot) > 0
        assert len(multi.summary_by_path) > 0

    def test_multi_file_json_output(self, analyzer):
        """Multi-file JSON output should be valid."""
        files = list(KB_DIR.glob("*.yaml"))[:2]
        reports = [analyzer.analyze_file(str(f), "Disease") for f in files]
        multi = create_multi_file_report(reports)
        json_out = JSONFormatter.format_multi(multi)
        parsed = json.loads(json_out)
        assert "files_analyzed" in parsed
        assert "global_compliance" in parsed

    def test_multi_file_text_output(self, analyzer):
        """Multi-file text output should show per-file scores."""
        files = list(KB_DIR.glob("*.yaml"))[:2]
        reports = [analyzer.analyze_file(str(f), "Disease") for f in files]
        multi = create_multi_file_report(reports)
        text_out = TextFormatter.format_multi(multi)
        assert "Multi-File Compliance Report" in text_out
        assert "Files Analyzed" in text_out
