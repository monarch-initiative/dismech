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

It also catches a second, sneakier shape. A page can render perfectly on the
build machine and still never reach the published site, because ``.gitignore``
drops it from the commit — ``pages/disorders/Holt-Oram_syndrome.html`` sat in
the ``.gitignore`` "Local files" block and was therefore a *permanent* dead
link that an on-disk existence check cannot see. ``git check-ignore`` reports
only ignored **and untracked** paths, which is exactly the failing set.

Usage::

    uv run python scripts/check_browser_data_links.py
    uv run python scripts/check_browser_data_links.py --data app/data.js --limit 25
    uv run python scripts/check_browser_data_links.py --data app/discussions/data.js
    uv run python scripts/check_browser_data_links.py --data app/models/data.js

Design invariant: **never silently pass.** A ``data.js`` whose structure this
script cannot parse is an error, not a clean run — the same fail-safe stance
``scripts/classify_page_build.py`` takes on an uncomputable diff.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

SEARCH_DATA_MARKER = "window.searchData = "
PAGE_URL_RE = re.compile(r'"page_url"\s*:\s*"([^"]+)"')


class BrowserDataError(RuntimeError):
    """Raised when ``data.js`` cannot be parsed into records."""


def parse_search_data(text: str) -> list[dict]:
    """Extract the ``window.searchData`` array from a ``data.js`` payload.

    The file is generated as ``window.searchData = <json array>;`` followed by
    a ``window.searchMetrics`` object, so the array ends at the first ``];`` that
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


def page_target(url: str) -> str:
    """Strip the in-page fragment from a ``page_url`` to get the file it names.

    The sibling indexes ``app/discussions/data.js`` and ``app/models/data.js``
    point at an anchor within a disorder page
    (``../../pages/disorders/Crohn_Disease.html#computational-model-…``), so the
    raw value is not a path. The page file is what has to exist.
    """
    return url.split("#", 1)[0]


def find_ignored_paths(paths: list[Path], cwd: Path) -> set[str]:
    """Return the subset of ``paths`` that git would refuse to commit.

    ``git check-ignore`` reports a path only when it is ignored **and**
    untracked, which is precisely the set that renders locally but never
    reaches the published site. Returns an empty set when git is unavailable or
    ``cwd`` is not a repository — the on-disk check still applies.
    """
    if not paths:
        return set()
    try:
        proc = subprocess.run(
            # -c core.quotePath=false: git otherwise C-quotes non-ASCII paths
            # ("Alstr\303\266m_syndrome.html"), which would not match our keys.
            ["git", "-c", "core.quotePath=false", "check-ignore", "--stdin"],
            input="\n".join(str(p) for p in paths),
            capture_output=True,
            text=True,
            cwd=cwd,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return set()
    # 0 = some paths ignored, 1 = none ignored; anything else means git could
    # not answer (not a repo, etc.) and the check simply does not apply.
    if proc.returncode not in (0, 1):
        return set()
    return {line.strip() for line in proc.stdout.splitlines() if line.strip()}


def find_broken_links(data_path: Path) -> tuple[list[tuple[str, str, str]], int]:
    """Return the broken ``(name, page_url, reason)`` triples and total link count.

    ``page_url`` values are relative to the directory holding ``data.js``
    (``app/``), matching how the browser resolves them. A link is broken when
    the target is ``missing`` from disk, or present but ``git-ignored`` — the
    latter renders on the build machine and is then dropped from the commit.
    """
    text = data_path.read_text(encoding="utf-8")
    pairs = extract_page_urls(text)
    if not pairs:
        raise BrowserDataError(f"no page_url values found in {data_path}")
    base = data_path.parent

    broken: list[tuple[str, str, str]] = []
    present: list[tuple[str, str]] = []
    for name, url in pairs:
        if (base / page_target(url)).exists():
            present.append((name, url))
        else:
            broken.append((name, url, "missing"))

    resolved = {
        str((base / page_target(url)).resolve()): (name, url) for name, url in present
    }
    for ignored in find_ignored_paths([Path(p) for p in resolved], base):
        # .get(): a git build that still quotes the path would otherwise take a
        # fail-closed gate down with a KeyError instead of reporting.
        pair = resolved.get(ignored)
        if pair is not None:
            broken.append((pair[0], pair[1], "git-ignored"))

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

    n_missing = sum(1 for *_, reason in broken if reason == "missing")
    n_ignored = len(broken) - n_missing
    print(
        f"ERROR: {len(broken)} of {total} page_url targets in {args.data} "
        f"will be dead links ({len(broken) / total:.1%}): "
        f"{n_missing} never rendered, {n_ignored} rendered but git-ignored."
    )
    for name, url, reason in broken[: args.limit]:
        print(f"  [{reason}] {name} -> {url}")
    if len(broken) > args.limit:
        print(f"  ... and {len(broken) - args.limit} more")
    if n_missing:
        print(
            "\nmissing: the browser index was rebuilt from the whole KB but the\n"
            "pages were not. Fix with a full page build: 'just gen-pages' (or\n"
            "re-dispatch generate-pages, which forces mode=full on dispatch)."
        )
    if n_ignored:
        print(
            "\ngit-ignored: the page renders here but .gitignore drops it from the\n"
            "commit, so it can never reach the published site. Remove the pattern\n"
            "from .gitignore (check with 'git check-ignore -v <path>')."
        )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
