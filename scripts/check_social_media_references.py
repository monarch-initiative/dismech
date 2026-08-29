#!/usr/bin/env python3
"""Fail any KB reference pointing at a user-generated social-media host.

Design decision 6b: published patient-advocacy content is citable, user-generated
social-media content is not. Nothing else catches a forum citation -- the URL
resolves, the snippet is a real quote from the page, and LinkML, term and
reference validation all pass. The sibling corroboration gate does not cover it
either, because that rule is opt-in by tagging and an untagged forum URL is
invisible to it.

Ungated and whole-KB in CI for the same reason `check_entity_refs` is: the PRs
that would introduce a forum citation are curation PRs touching only `kb/`, which
match no `src/` or `tests/` path filter.

Usage
-----
    python scripts/check_social_media_references.py                 # gate
    python scripts/check_social_media_references.py kb/disorders/Asthma.yaml
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dismech.social_media_refs import SOCIAL_MEDIA_HOSTS, social_media_reference_errors
from dismech.yaml_io import safe_load

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
            print(f"{_display(path)}: could not parse ({exc})", file=sys.stderr)
            return 1
        findings.extend((path, error) for error in social_media_reference_errors(data))

    if findings:
        print("Social-media reference(s) cited in KB YAML.\n")
        print("Public forums and social platforms are not citable sources")
        print("(design decision 6b). A patient-advocacy organization's published")
        print("page is; a forum thread is not. Where a community signal needs")
        print("quantifying, a national patient registry is the consented")
        print("substitute. If the signal has no citable source, record it in")
        print("`discussions` as an unvalidated lead instead.\n")
        for path, error in findings:
            print(f"{_display(path)}: {error}")
        print(f"\n{len(findings)} finding(s) across {len(files)} file(s).")
        return 1

    print(
        f"OK: no social-media references in {len(files)} KB file(s) "
        f"({len(SOCIAL_MEDIA_HOSTS)} hosts checked)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
