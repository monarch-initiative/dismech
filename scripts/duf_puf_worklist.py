#!/usr/bin/env python3
"""Build the first DUF/Pfam worklist from InterPro."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from dismech.dufmech.worklist import (
    InterProPfamClient,
    collect_worklist,
    load_interpro_fixture,
    render_json,
    render_tsv,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--search",
        default="DUF",
        help="InterPro Pfam search term (default: DUF)",
    )
    parser.add_argument(
        "--page-size",
        type=int,
        default=200,
        help="InterPro page size, max 200 (default: 200)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="stop after N normalized rows",
    )
    parser.add_argument(
        "--format",
        choices=("tsv", "json"),
        default="tsv",
        help="output format (default: tsv)",
    )
    parser.add_argument(
        "--include-false-positives",
        action="store_true",
        help="include Pfam search hits whose metadata does not look DUF-like",
    )
    parser.add_argument(
        "--input-json",
        type=Path,
        help="read a saved InterPro page or result list instead of fetching live",
    )
    parser.add_argument("--out", type=Path, help="write here instead of stdout")
    args = parser.parse_args(argv)

    if args.page_size < 1 or args.page_size > 200:
        parser.error("--page-size must be between 1 and 200")
    if args.limit is not None and args.limit < 1:
        parser.error("--limit must be positive")

    if args.input_json:
        payload = json.loads(args.input_json.read_text(encoding="utf-8"))
        entries = load_interpro_fixture(payload)
    else:
        entries = InterProPfamClient().iter_entries(
            search=args.search,
            page_size=args.page_size,
        )

    rows = collect_worklist(
        entries,
        include_false_positives=args.include_false_positives,
        limit=args.limit,
    )
    output = render_json(rows) if args.format == "json" else render_tsv(rows)

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(output + "\n", encoding="utf-8")
        print(f"wrote {args.out} ({len(rows)} rows)", file=sys.stderr)
    else:
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
