#!/usr/bin/env python3
"""Guard the community-source corroboration rule across the whole KB.

Design decision 6b: a reference tagged ``PatientOrganization`` or
``PatientCommunity`` may corroborate a curated claim but may never be its sole
support. The rule is invisible to every other gate -- LinkML validation, term
validation and snippet verification all pass on a phenotype whose only citation
is a patient-advocacy page, because that page is a real URL and the snippet is a
real quote from it.

Why this needs its own ungated, whole-KB pass
---------------------------------------------
The rule is already checked by ``test_community_sourced_evidence_is_not_sole_support``
in ``tests/test_data.py`` -- but that test never runs on the PRs that can break
it. ``.github/workflows/main.yaml`` selects pytest by changed path: the
``schema`` filter (``src/dismech/schema/**``, ``groupings.py``,
``entity_refs.py``, ``tests/test_data.py``) gates ``just test-kb``, which is
where anything marked ``kb_data`` runs.

A curation PR touches ``kb/`` and nothing else, so it matches neither that filter
nor ``python``. It gets the ungated shell checks plus ``just validate-disorders``
on its changed files -- none of which reads a reference tag. So the gate written
to police community sourcing would be skipped by exactly the PRs that introduce
it, which is the shape of #9473 (entity refs), #7652 and #8909.

Whole-KB rather than changed-files, for the reason ``check_entity_refs`` is:
tags live on the entry's top-level ``references:`` list while the evidence items
citing them live elsewhere in the same file, and a PR that adds a tag need not
touch every block that cites the reference.

Usage
-----
    python scripts/check_community_evidence.py                 # gate: fail on any finding
    python scripts/check_community_evidence.py kb/disorders/Asthma.yaml
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dismech.community_evidence import community_sole_support_errors
from dismech.yaml_io import safe_load

# KB trees whose entries carry a top-level `references:` list. `kb/groupings` is
# included because `Grouping` carries `references` too; `kb/comorbidities` is
# included even though `ComorbidityAssociation` does not, so that a reference
# slot added there later is checked by something rather than by nothing.
# `history/` is excluded: those records are append-only, so a finding there
# could not be fixed in place.
DEFAULT_ROOTS = (
    "kb/disorders",
    "kb/modules",
    "kb/comorbidities",
    "kb/groupings",
)


def iter_yaml_files(paths: list[str]) -> list[Path]:
    """Expand explicit paths, or the default roots when none are given."""
    if paths:
        return [Path(p) for p in paths]
    files: list[Path] = []
    for root in DEFAULT_ROOTS:
        files.extend(
            sorted(
                p
                for p in (ROOT / root).rglob("*.yaml")
                if not p.name.endswith(".history.yaml")
            )
        )
    return files


def _display(path: Path) -> str:
    """Repo-relative path when the file is inside the repo, else as given."""
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        help=f"KB YAML files to check (default: {', '.join(DEFAULT_ROOTS)})",
    )
    args = parser.parse_args()

    files = iter_yaml_files(args.paths)
    findings: list[tuple[Path, str]] = []
    for path in files:
        try:
            data = safe_load(path.read_text(encoding="utf-8"))
        except OSError as exc:  # pragma: no cover - unreadable file
            print(f"{_display(path)}: could not read ({exc})", file=sys.stderr)
            return 1
        except yaml.YAMLError as exc:
            # `check-duplicate-keys` and `linkml-validate` both report a parse
            # failure with better detail than this check can; name the file and
            # let those speak, rather than failing the build twice for one cause.
            print(f"{_display(path)}: could not parse ({exc})", file=sys.stderr)
            return 1
        findings.extend((path, error) for error in community_sole_support_errors(data))

    if findings:
        print("Community-sourced evidence is sole support in KB YAML.\n")
        print("A reference tagged PatientOrganization or PatientCommunity may")
        print("corroborate a curated claim but may not be the only thing")
        print("supporting it. Add a literature, registry or structured-database")
        print("reference to the block, or move the claim to `discussions` as an")
        print("explicitly unvalidated lead. See design decision 6b in")
        print("docs/explanation/design-decisions.md.\n")
        for path, error in findings:
            print(f"{_display(path)}: {error}")
        print(f"\n{len(findings)} finding(s) across {len(files)} file(s).")
        return 1

    print(f"OK: no community-only evidence blocks in {len(files)} KB file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
