#!/usr/bin/env python3
"""Run yamlfix, refusing to write any result that changes parsed YAML data.

yamlfix 1.19.1 runs syntax-blind regexes over scalar content (#12101, #9613).
Use its public in-memory API so a destructive result never reaches the file.
"""

from __future__ import annotations

import argparse
import sys
import tomllib
from pathlib import Path

import yaml
from yamlfix import fix_code
from yamlfix.model import YamlfixConfig


def canonical_data(source: str) -> str:
    """Normalize parsed data, retaining types and exact string whitespace.

    Safe dumping handles timestamps, NaN and aliases as well as ordinary KB
    values. Comparing plain Python objects would equate True with 1 and would
    consider two NaNs unequal. Mapping order and scalar quoting are immaterial.
    """
    return yaml.safe_dump_all(
        yaml.safe_load_all(source), canonical=True, sort_keys=True
    )


def format_file(path: Path, config: YamlfixConfig) -> bool:
    """Write only a data-preserving result; return whether the file changed."""
    source = path.read_text(encoding="utf-8")
    before = canonical_data(source)
    formatted = fix_code(source, config)
    if before != canonical_data(formatted):
        raise ValueError(
            "yamlfix would change parsed YAML data; file left untouched. "
            "Check block scalars containing #N or lines ending in ': no' / '- no' "
            "(also yes/on/off). Use a double-quoted scalar preserving the original "
            "value, then retry. See dismech#12101 and dismech#9613."
        )
    if formatted == source:
        return False
    path.write_text(formatted, encoding="utf-8")
    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-c", "--config-file", type=Path, default=Path(".yamlfix.toml"))
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args(argv)
    config = YamlfixConfig(
        **tomllib.loads(args.config_file.read_text(encoding="utf-8"))
    )
    failed = False
    for path in args.files:
        try:
            if format_file(path, config):
                print(f"{path}: formatted; review and stage the changes")
                failed = True
        except Exception as exc:
            print(f"{path}: {exc}", file=sys.stderr)
            failed = True
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
