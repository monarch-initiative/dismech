"""CLI for generating initial matching YAML files from phenopackets."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import yaml

from phenoagent.matching import (
    build_matching_run_from_phenopacket,
    load_phenopacket,
    resolve_disease_reference,
)


def _safe_token(value: str) -> str:
    """Convert arbitrary text to a filename-safe token."""
    token = re.sub(r"[^A-Za-z0-9._-]+", "_", value.strip())
    token = token.strip("_")
    return token or "unknown"


def _default_output_path(case_id: str, disease_slug: str) -> Path:
    """Return default output path for initial matching YAML."""
    return Path("output") / "matching" / f"{_safe_token(case_id)}__{_safe_token(disease_slug)}.yaml"


def create_initial_matching_file(
    phenopacket_path: Path,
    disease_reference: str,
    *,
    output_path: Path | None = None,
    kb_dir: Path | None = None,
) -> Path:
    """Generate and write an initial matching YAML file."""
    phenopacket = load_phenopacket(phenopacket_path)
    disease_slug, disease_path = resolve_disease_reference(disease_reference, kb_dir=kb_dir)

    run = build_matching_run_from_phenopacket(
        phenopacket,
        disease_slug=disease_slug,
        kb_dir=disease_path.parent,
        run_id=f"init-{_safe_token(str(phenopacket.get('id', 'unknown_case')))}-{_safe_token(disease_slug)}",
    )

    if output_path is None:
        output_path = _default_output_path(run["case_id"], disease_slug)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as stream:
        yaml.safe_dump(run, stream, sort_keys=False)
    return output_path


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate initial matching YAML from phenopacket and dismech disease")
    parser.add_argument("phenopacket_path", type=Path, help="Path to a GA4GH phenopacket JSON file")
    parser.add_argument("disease_reference", help="DisMech disease reference: slug, id, name, or YAML path")
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Optional output YAML path (default: output/matching/<case>__<slug>.yaml)",
    )
    parser.add_argument(
        "--kb-dir",
        type=Path,
        default=None,
        help="Optional disorder directory override (default: kb/disorders)",
    )
    return parser


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()

    output_path = create_initial_matching_file(
        phenopacket_path=args.phenopacket_path,
        disease_reference=args.disease_reference,
        output_path=args.output,
        kb_dir=args.kb_dir,
    )
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
