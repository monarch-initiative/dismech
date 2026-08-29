#!/usr/bin/env python3
"""Check pathophysiology nodes for internally contradictory annotations.

Every existing gate validates one binding at a time. ``CL:0000057 fibroblast``
is a real term, ``GO:0001837 epithelial to mesenchymal transition`` is a real
term, and a node asserting both passes LinkML validation, term validation,
reference validation and every test in ``tests/``. It is still wrong: a
fibroblast is not epithelium, so it is not the cell that undergoes EMT.

The rules live in ``conf/logical_rules.yaml`` and the reasoning behind their
shape is in ``src/dismech/logical_rules.py`` and ``docs/logical-rules.md``.

**Report-only by default.** Biology has exceptions the Cell Ontology's is_a
graph cannot express, so a finding is a question for a curator, not a proven
defect -- the same posture ``check-source-defect-claims`` takes. Pass
``--strict`` to turn findings into a non-zero exit; a node that has been
looked at and judged correct carries its answer in ``review_notes`` rather
than in a baseline file, so the reasoning sits where the next curator reads it.

    python scripts/check_logical_rules.py                       # whole KB
    python scripts/check_logical_rules.py kb/disorders/Asthma.yaml
    python scripts/check_logical_rules.py --strict              # gate
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dismech.logical_rules import (  # noqa: E402
    DEFAULT_CLOSURE_DIR,
    DEFAULT_RULES_PATH,
    WAIVER_PREFIX,
    Finding,
    RuleConfigError,
    evaluate_entry,
    load_closures,
    load_rules,
    unusable_rules,
)
from dismech.yaml_io import safe_load  # noqa: E402

#: Whole-KB by default, for the reason ``check_entity_refs`` is: the rules are
#: per-node, but a curation PR that edits one file is exactly the PR that never
#: runs the path-gated pytest lanes.
DEFAULT_ROOTS = ("kb/disorders", "kb/modules", "kb/comorbidities")


def iter_yaml_files(paths: list[str]) -> list[Path]:
    if not paths:
        return sorted(
            path for root in DEFAULT_ROOTS for path in (ROOT / root).glob("*.yaml")
        )
    files: list[Path] = []
    for raw in paths:
        path = Path(raw)
        files.extend(sorted(path.glob("*.yaml")) if path.is_dir() else [path])
    return files


def _display(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def report(findings: list[Finding], scanned: int) -> None:
    if not findings:
        print(f"OK: no logical-rule findings in {scanned} KB file(s).")
        return

    print("Logical-rule finding(s): a pathophysiology node annotates a process")
    print("and a set of cell types that do not fit together.\n")
    print("Each is a question, not a verdict. Either repair the annotation, or,")
    print("if the pairing is correct here, record why on the node:\n")
    print(f'    review_notes: "{WAIVER_PREFIX} <rule-id>. <why it is correct>"\n')

    by_rule: dict[str, list[Finding]] = {}
    for finding in findings:
        by_rule.setdefault(finding.rule_id, []).append(finding)

    for rule_id in sorted(by_rule):
        group = by_rule[rule_id]
        print(f"[{rule_id}] {len(group)} finding(s)")
        for finding in sorted(group, key=lambda f: (str(f.path), f.node)):
            print(f"  {_display(finding.path)}: {finding.node}")
            print(f"      {finding.detail}")
        print()

    print(f"{len(findings)} finding(s) across {scanned} KB file(s).")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="KB YAML files or directories")
    parser.add_argument("--rules", type=Path, default=DEFAULT_RULES_PATH)
    parser.add_argument("--closure-dir", type=Path, default=DEFAULT_CLOSURE_DIR)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="exit non-zero on findings (default: report and exit 0)",
    )
    args = parser.parse_args()

    try:
        rules = load_rules(args.rules)
    except RuleConfigError as exc:
        print(exc, file=sys.stderr)
        return 2

    closures = load_closures(
        [root for rule in rules for root in rule.closure_roots], args.closure_dir
    )
    # A rule that cannot run is a broken check, not a clean one -- fail before
    # scanning rather than printing an OK the cache did not earn.
    unusable = unusable_rules(rules, closures)
    if unusable:
        print(
            "Closures missing -- these rules could not be evaluated:\n", file=sys.stderr
        )
        for line in unusable:
            print(f"  {line}", file=sys.stderr)
        return 2

    files = iter_yaml_files(args.paths)
    findings: list[Finding] = []
    for path in files:
        try:
            data = safe_load(path.read_text(encoding="utf-8"))
        except OSError as exc:  # pragma: no cover - unreadable file
            print(f"{_display(path)}: could not read ({exc})", file=sys.stderr)
            return 2
        except yaml.YAMLError as exc:
            # `check-duplicate-keys` and `linkml-validate` both report a parse
            # failure with better detail; name the file and let them speak.
            print(f"{_display(path)}: could not parse ({exc})", file=sys.stderr)
            return 2
        if not isinstance(data, dict):
            continue
        findings.extend(evaluate_entry(data, rules, closures, path))

    report(findings, len(files))
    return 1 if (findings and args.strict) else 0


if __name__ == "__main__":
    raise SystemExit(main())
