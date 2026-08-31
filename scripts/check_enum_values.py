#!/usr/bin/env python3
"""Guard against KB values that are not permissible in their slot's enum.

Why this needs a whole-KB sweep
-------------------------------
This is the schema-narrowing twin of ``check_duplicate_yaml_keys.py``. Both
catch a defect that arrives by *merge* rather than by authoring, so neither is
visible to the PR that introduces it.

Issue #10061 is the worked example. #10003 narrowed ``EvidenceItemSupportEnum``
from five values to three, retiring ``PARTIAL``, and migrated every occurrence
that existed on its own base. Meanwhile ~15 curation PRs were already open,
each carrying ``supports: PARTIAL`` -- legal when written, legal when validated
against the base they branched from. Every one of them was green. The moment
they merged, ``main`` held values the schema no longer accepted: 9 items within
90 seconds of the narrowing, 100 within a day.

Neither side could have caught it. The narrowing PR did not contain the curation
files; the curation PRs did not contain the narrowed enum. Only the merge result
holds both.

The existing whole-KB sweep (``just test-kb``) is gated on schema changes, on
the stated reasoning that "only a schema edit can flip a KB file's validity".
That reasoning is half right: a schema edit is indeed the only thing that flips
an *unchanged* file's validity, but it flips it for files that do not exist yet
as well -- and those arrive through PRs that touch no schema and so never run
the sweep. Ungated is the only cadence that closes that window.

What it checks, and what it deliberately does not
-------------------------------------------------
For each schema below, every induced slot whose range is an enum with static
``permissible_values`` is tracked, and every occurrence of that slot name in the
matching KB files is checked against those values.

* **Dynamic enums are skipped.** An enum with no ``permissible_values`` is a
  ``reachable_from`` ontology binding (DiseaseTerm, PhenotypeTerm, ...). Those
  are ``linkml-term-validator``'s job, are cache- and network-backed, and cannot
  be answered from the schema text alone.
* **Slots with a non-enum binding anywhere are skipped**, as are slots using
  ``any_of``. LinkML slot names are global, so one name can be an enum in one
  class and free text in another (``severity`` is enum-backed on descriptors and
  tolerated as free text on legacy phenotype summaries). Checking such a name
  would flag correct free text. Slots bound to *different* enums in different
  classes are still checked, against the union -- narrower than per-class typing,
  but enough to catch a value no enum in the schema has ever had, which is the
  retired-value shape this exists for.
* **Only the trees that validate against each schema are scanned.**
  ``kb/hypotheses/`` documents validate against ``hypothesis_assessment.yaml`` /
  ``hypothesis_reconciliation.yaml``, not ``dismech.yaml``; running the wrong
  schema against them reports five values (``status: PARTIAL``,
  ``REPORTED_ONLY``, ``SUCCEEDED``, ``FAILED``) that are perfectly legal where
  they sit. The globs below mirror the ``just validate-hypothesis-*-all``
  recipes so this check's scope tracks what is actually validated.
* ``experiments/`` is out of scope on purpose, as it is for every other
  validator here: those files are snapshots of what curators wrote during an
  inter-annotator study, and "fixing" one would change the measurement.

This is not a replacement for ``linkml-validate`` -- it checks one constraint,
not conformance. It is the cheap subset that can afford to run on every PR
(~20s, offline, no codegen) where the full sweep cannot.

Usage
-----
    python scripts/check_enum_values.py                    # gate: fail on any finding
    python scripts/check_enum_values.py kb/disorders/Asthma.yaml
"""
from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path

from linkml_runtime import SchemaView

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dismech.yaml_io import safe_load

SCHEMA_DIR = ROOT / "src" / "dismech" / "schema"

#: schema -> the glob patterns whose files are validated against it. Mirrors the
#: `just validate-*` recipes; see the module docstring on why this is per-schema.
TARGETS: tuple[tuple[str, tuple[str, ...]], ...] = (
    (
        "dismech.yaml",
        (
            "kb/disorders/**/*.yaml",
            "kb/modules/**/*.yaml",
            "kb/comorbidities/**/*.yaml",
            "kb/groupings/**/*.yaml",
            "kb/surrogate_endpoints/**/*.yaml",
        ),
    ),
    (
        "hypothesis_assessment.yaml",
        ("kb/hypotheses/*/*/assessments/*-assessment-by-*.yaml",),
    ),
    (
        "hypothesis_reconciliation.yaml",
        ("kb/hypotheses/*/*/reconciliation.yaml",),
    ),
)


def tracked_slots(schema_path: Path) -> dict[str, set[str]]:
    """Map slot name -> permissible values, for slots only ever bound to static enums.

    Uses induced slots so that ``slots``/``slot_usage``/``attributes`` are all
    resolved: ``GeneSetAssociation`` declares its enum-bound ``relationship``
    as an inline ``attributes:`` entry, which ``all_slots()`` does not reach.
    """
    view = SchemaView(str(schema_path))
    static = {
        name: set(enum.permissible_values or {})
        for name, enum in view.all_enums().items()
        if enum.permissible_values
    }

    allowed: dict[str, set[str]] = defaultdict(set)
    impure: set[str] = set()
    for class_name in view.all_classes():
        for slot in view.class_induced_slots(class_name):
            if slot.any_of or slot.range not in static:
                impure.add(slot.name)
            else:
                allowed[slot.name].update(static[slot.range])
    return {name: values for name, values in allowed.items() if name not in impure}


def find_violations(data: object, tracked: dict[str, set[str]], path: str = ""):
    """Yield ``(location, slot, value)`` for each value outside its slot's enum."""
    if isinstance(data, dict):
        for key, value in data.items():
            location = f"{path}.{key}" if path else key
            if key in tracked:
                for index, item in enumerate(value if isinstance(value, list) else [value]):
                    if isinstance(item, str) and item not in tracked[key]:
                        where = f"{location}[{index}]" if isinstance(value, list) else location
                        yield where, key, item
            yield from find_violations(value, tracked, location)
    elif isinstance(data, list):
        for index, item in enumerate(data):
            yield from find_violations(item, tracked, f"{path}[{index}]")


def _files_for(patterns: tuple[str, ...]) -> list[Path]:
    seen: dict[Path, None] = {}
    for pattern in patterns:
        for path in sorted(ROOT.glob(pattern)):
            seen.setdefault(path, None)
    return list(seen)


def _display(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        help="YAML files to check (default: every KB tree, against its own schema)",
    )
    args = parser.parse_args()

    explicit = {Path(p).resolve() for p in args.paths}
    findings: list[tuple[Path, str, str, str]] = []
    scanned = 0

    for schema_name, patterns in TARGETS:
        files = _files_for(patterns)
        if explicit:
            files = [f for f in files if f.resolve() in explicit]
        if not files:
            continue
        tracked = tracked_slots(SCHEMA_DIR / schema_name)
        for path in files:
            try:
                data = safe_load(path.read_text(encoding="utf-8"))
            except Exception as exc:  # malformed YAML is check-duplicate-keys' job
                print(f"{_display(path)}: could not parse ({exc})", file=sys.stderr)
                return 1
            scanned += 1
            for location, slot, value in find_violations(data, tracked):
                findings.append((path, location, slot, value))

    if explicit:
        matched = {f.resolve() for _, patterns in TARGETS for f in _files_for(patterns)}
        for unknown in sorted(explicit - matched):
            print(
                f"{_display(unknown)}: not in any schema's scope, skipped",
                file=sys.stderr,
            )

    if findings:
        print("Value(s) outside the permissible values of their slot's enum.\n")
        print("A value here was legal when it was written and is not legal now,")
        print("which usually means an enum was narrowed while this file was in")
        print("flight. Fix the value, or restore the permissible value.\n")
        for path, location, _slot, value in findings:
            print(f"{_display(path)}: {location} = {value!r}")
        print(f"\n{len(findings)} invalid value(s) across {scanned} file(s).")
        return 1

    print(f"OK: no out-of-enum values in {scanned} KB file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
