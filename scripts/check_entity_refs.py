#!/usr/bin/env python3
"""Guard entity references (``<kind>#<name>``) across the whole KB.

``attaches_to``, ``Experiment.would_support`` / ``would_refute`` and the
perturbation/readout ``target`` slots point at another object in the same entry.
They are foreign keys, and a broken one is invisible to every other gate:
LinkML validation, term validation and snippet verification all pass while a
KNOWLEDGE_GAP hangs off a node that no longer exists.

Why this needs its own ungated, whole-KB pass
---------------------------------------------
The rules are already checked by ``test_entity_ref_foreign_keys`` in
``tests/test_data.py`` -- but that test never runs on the PRs that can break
them. ``.github/workflows/main.yaml`` selects pytest by changed path:

* the ``schema`` filter (``src/dismech/schema/**``, ``groupings.py``,
  ``tests/test_data.py``) gates ``just test-kb``;
* the ``python`` filter (``src/**``, ``tests/**/*.py``, ...) gates
  ``just test-python-code``, which is where the entity-ref tests actually live,
  since they carry no ``kb_data`` marker.

A curation PR touches ``kb/`` and nothing else, so it matches neither. It gets
the ungated shell checks plus ``just validate-disorders`` on its changed files
-- LinkML, terms and references, none of which resolve an entity reference. The
result is that the checks written to protect KB content are the ones a
content-only PR skips (issue #9473; the same shape as #7652 and #8909).

Two entries reached ``main`` that way with pre-#9394 alias prefixes, and the
gate added in #9224 -- prose must not go back into ``would_support`` -- would
have been unenforceable on exactly the curation PRs it was written for.

Whole-KB rather than changed-files, for the reason ``check_duplicate_yaml_keys``
is: these are *cross-file* invariants in the sense that matters here. Renaming a
node in file A breaks a reference in file A that the PR may not otherwise touch,
and a PR that only *deletes* a node selects no changed file carrying the dangling
ref at all. The whole sweep costs about the same as reading the KB once --
~13s on a CI runner, ~17s in a slower sandbox.

Usage
-----
    python scripts/check_entity_refs.py                    # gate: fail on any finding
    python scripts/check_entity_refs.py kb/disorders/Asthma.yaml
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dismech.entity_refs import entity_ref_errors
from dismech.yaml_io import safe_load

# The KB trees whose entries carry entity references. `kb/groupings` is included
# even though groupings use a different membership grammar: a grouping file is
# still parsed here, and a future reference slot on one would otherwise be
# checked by nothing. `history/` is excluded -- those records are append-only,
# so a finding there could not be fixed in place.
DEFAULT_ROOTS = (
    "kb/disorders",
    "kb/modules",
    "kb/comorbidities",
    "kb/groupings",
)

# Directories under `kb/` deliberately left out of the sweep, with the reason.
# Stated explicitly rather than by omission because "a tree nobody checks"
# is the exact bug this script exists to fix:
# `test_entity_ref_sweep_covers_every_kb_subtree` (tests/test_ci_batch_validation.py)
# fails when a new `kb/<something>/` appears in neither list, so the decision
# gets made rather than defaulted.
EXCLUDED_ROOTS = {
    # Provider hypothesis reports and their assessment sidecars. A different
    # schema, no reference-bearing slots today -- the only hash-anchor string
    # anywhere in the tree is inside a Markdown report, not a YAML slot.
    "kb/hypotheses": "hypothesis reports/assessments; no entity-ref slots",
    # Surrogate-endpoint records, likewise a separate schema with no
    # reference-bearing slots.
    "kb/surrogate_endpoints": "separate schema; no entity-ref slots",
}


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
            # failure with better detail than this check can; say which file it
            # was and let those speak, rather than failing the build twice for
            # one cause.
            print(f"{_display(path)}: could not parse ({exc})", file=sys.stderr)
            return 1
        findings.extend((path, error) for error in entity_ref_errors(data))

    if findings:
        print("Broken entity reference(s) detected in KB YAML.\n")
        print("These slots hold foreign keys into the same entry, written")
        print("`<kind>#<name>`. A dangling or mis-typed one resolves to nothing")
        print("and renders as a dead chip, while every other check stays green.")
        print("See the `Entity References Are Foreign Keys` section of")
        print("CLAUDE.md, and `src/dismech/entity_refs.py` for the sections a")
        print("`<kind>` may name.\n")
        for path, error in findings:
            print(f"{_display(path)}: {error}")
        print(f"\n{len(findings)} finding(s) across {len(files)} file(s).")
        return 1

    print(f"OK: entity references resolve in {len(files)} KB file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
