"""CLI for LinkML data compliance analysis."""

import argparse
import sys
from pathlib import Path

from .analyzer import ComplianceAnalyzer
from .config import QCConfig
from .formatters import (
    CSVFormatter,
    JSONFormatter,
    TextFormatter,
    create_multi_file_report,
)


def main():
    parser = argparse.ArgumentParser(
        description="Analyze LinkML data files for recommended field compliance"
    )
    parser.add_argument(
        "data_path",
        nargs="+",
        help="Data file(s) or directory to analyze",
    )
    parser.add_argument(
        "-s",
        "--schema",
        required=True,
        help="Path to LinkML schema YAML",
    )
    parser.add_argument(
        "-t",
        "--target-class",
        required=True,
        help="Target class name for validation",
    )
    parser.add_argument(
        "-c",
        "--config",
        help="Path to QC configuration YAML file (for weights and thresholds)",
    )
    parser.add_argument(
        "-f",
        "--format",
        choices=["json", "csv", "text"],
        default="text",
        help="Output format (default: text)",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Output file (default: stdout)",
    )
    parser.add_argument(
        "--min-compliance",
        type=float,
        help="Minimum global compliance percentage (exit 1 if below)",
    )
    parser.add_argument(
        "--fail-on-violations",
        action="store_true",
        help="Exit with error code if any threshold violations occur",
    )
    parser.add_argument(
        "--pattern",
        default="*.yaml",
        help="Glob pattern for directory search (default: *.yaml)",
    )

    args = parser.parse_args()

    # Collect data files
    data_files: list[Path] = []
    for path_str in args.data_path:
        path = Path(path_str)
        if path.is_dir():
            data_files.extend(path.glob(args.pattern))
        elif path.exists():
            data_files.append(path)
        else:
            print(f"Warning: {path} does not exist, skipping", file=sys.stderr)

    if not data_files:
        print("No data files found", file=sys.stderr)
        sys.exit(1)

    # Create analyzer with optional config
    if args.config:
        analyzer = ComplianceAnalyzer.with_config_file(args.schema, args.config)
    else:
        analyzer = ComplianceAnalyzer(args.schema)

    # Analyze all files
    reports = [analyzer.analyze_file(str(f), args.target_class) for f in sorted(data_files)]

    # Select formatter
    formatter_map = {
        "json": JSONFormatter,
        "csv": CSVFormatter,
        "text": TextFormatter,
    }
    formatter = formatter_map[args.format]

    # Format output
    if len(reports) == 1:
        output = formatter.format(reports[0])
    else:
        multi = create_multi_file_report(reports)
        output = formatter.format_multi(multi)

    # Output
    if args.output:
        Path(args.output).write_text(output)
        print(f"Report written to {args.output}", file=sys.stderr)
    else:
        print(output)

    # Check for threshold violations
    all_violations = []
    for r in reports:
        all_violations.extend(r.threshold_violations)

    if all_violations and args.fail_on_violations:
        print(f"\n{len(all_violations)} threshold violation(s) found:", file=sys.stderr)
        for v in all_violations[:5]:  # Show first 5
            print(f"  {v.path}: {v.actual_compliance:.1f}% < {v.min_required:.1f}%", file=sys.stderr)
        if len(all_violations) > 5:
            print(f"  ... and {len(all_violations) - 5} more", file=sys.stderr)
        sys.exit(1)

    # Exit code based on global threshold
    if args.min_compliance is not None:
        total_checks = sum(r.total_checks for r in reports)
        total_populated = sum(r.total_populated for r in reports)
        avg = (total_populated / total_checks * 100) if total_checks > 0 else 100.0
        if avg < args.min_compliance:
            print(
                f"Compliance {avg:.1f}% is below threshold {args.min_compliance}%",
                file=sys.stderr,
            )
            sys.exit(1)


if __name__ == "__main__":
    main()
