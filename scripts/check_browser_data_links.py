#!/usr/bin/env python3
"""Fail when the browser index links to disorder pages that were never rendered.

``app/data.js`` is rebuilt from the whole KB on every ``generate-pages`` run,
but the disorder pages themselves may be built *incrementally*. When the two
halves disagree the browser UI ships dead links: an entry appears in search,
the user clicks it, and ``pages/disorders/<slug>.html`` 404s. PR #7903 shipped
205 such links (1826 ``data.js`` entries vs. 1621 rendered pages).

Nothing in the pipeline noticed. This script is the hard gate: it resolves
every ``page_url`` in ``window.searchData`` against the filesystem and exits
non-zero if any target is missing.

Usage::

    uv run python scripts/check_browser_data_links.py
    uv run python scripts/check_browser_data_links.py --data app/data.js --limit 25

Design invariant: **never silently pass.** A ``data.js`` whose structure this
script cannot parse is an error, not a clean run — the same fail-safe stance
``scripts/classify_page_build.py`` takes on an uncomputable diff.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

SEARCH_DATA_MARKER = "window.searchData = "
PAGE_URL_RE = re.compile(r'"page_url"\s*:\s*"([^"]+)"')


class BrowserDataError(RuntimeError):
    """Raised when ``data.js`` cannot be parsed into records."""


def parse_search_data(text: str) -> list[dict]:
    """Extract the ``window.searchData`` array from a ``data.js`` payload.

    The file is generated as ``window.searchData = <json array>;`` followed by
    a ``window.searchStats`` object, so the array ends at the first ``];`` that
    starts a line.
    """
    start = text.find(SEARCH_DATA_MARKER)
    if start < 0:
        raise BrowserDataError(f"no {SEARCH_DATA_MARKER!r} assignment found")
    start += len(SEARCH_DATA_MARKER)
    end = text.find("\n];", start)
    if end < 0:
        raise BrowserDataError("unterminated window.searchData array")
    try:
        records = json.loads(text[start : end + 2])
    except json.JSONDecodeError as exc:  # pragma: no cover - corrupt generator output
        raise BrowserDataError(f"window.searchData is not valid JSON: {exc}") from exc
    if not isinstance(records, list):
        raise BrowserDataError("window.searchData is not a JSON array")
    return records


def extract_page_urls(text: str) -> list[tuple[str, str]]:
    """Return ``(name, page_url)`` pairs for every record carrying a page link.

    Falls back to a regex scan of ``page_url`` values if the structured parse
    fails, so a change to the generator's framing degrades the error message
    rather than turning the gate off.
    """
    try:
        records = parse_search_data(text)
    except BrowserDataError:
        return [("<unparsed record>", url) for url in PAGE_URL_RE.findall(text)]
    pairs: list[tuple[str, str]] = []
    for record in records:
        if not isinstance(record, dict):
            continue
        url = record.get("page_url")
        if isinstance(url, str) and url:
            pairs.append((str(record.get("name") or "<unnamed>"), url))
    return pairs


def find_broken_links(data_path: Path) -> tuple[list[tuple[str, str]], int]:
    """Return the broken ``(name, page_url)`` pairs and the total link count.

    ``page_url`` values are relative to the directory holding ``data.js``
    (``app/``), matching how the browser resolves them.
    """
    text = data_path.read_text(encoding="utf-8")
    pairs = extract_page_urls(text)
    if not pairs:
        raise BrowserDataError(f"no page_url values found in {data_path}")
    base = data_path.parent
    broken = [pair for pair in pairs if not (base / pair[1]).exists()]
    return broken, len(pairs)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--data",
        default="app/data.js",
        type=Path,
        help="Path to the generated browser data file (default: app/data.js).",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=20,
        help="Maximum number of broken links to print (default: 20).",
    )
    args = parser.parse_args()

    if not args.data.exists():
        print(f"ERROR: {args.data} does not exist — run 'just gen-browser-data' first.")
        return 1

    try:
        broken, total = find_broken_links(args.data)
    except BrowserDataError as exc:
        print(f"ERROR: cannot verify {args.data}: {exc}")
        return 1

    if not broken:
        print(f"OK: all {total} page_url targets in {args.data} exist on disk.")
        return 0

    print(
        f"ERROR: {len(broken)} of {total} page_url targets in {args.data} "
        f"have no rendered page ({len(broken) / total:.1%} dead links)."
    )
    for name, url in broken[: args.limit]:
        print(f"  {name} -> {url}")
    if len(broken) > args.limit:
        print(f"  ... and {len(broken) - args.limit} more")
    print(
        "\nThe browser index was rebuilt from the whole KB but the pages were not.\n"
        "Fix with a full page build: 'just gen-pages' (or re-dispatch the\n"
        "generate-pages workflow, which forces mode=full on workflow_dispatch)."
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
