#!/usr/bin/env python3
"""Write the shared site header into the hand-written site pages.

Every Jinja template includes ``src/dismech/templates/_site_nav.html.j2``. The
pages below are not rendered from a template, so they cannot include it; they
carry a rendered copy between two marker comments instead::

    <!-- site-nav:start -->
    ...rendered _site_nav.html.j2...
    <!-- site-nav:end -->

This script rewrites that region from the partial. ``--check`` writes nothing
and exits 1 if any page is out of date, which is what
``tests/test_site_nav.py`` runs. A page that still has a hand-written
``<nav>`` header and no markers is converted on its first run (issue #14022).

    just sync-site-nav          # rewrite the pages
    just sync-site-nav --check  # report only
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

REPO_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = REPO_ROOT / "src" / "dismech" / "templates"
PARTIAL = "_site_nav.html.j2"

START = "<!-- site-nav:start -->"
END = "<!-- site-nav:end -->"

#: page path -> (relative path to the site root, active link key).
#: The keys are the ones defined in the partial's link list.
STATIC_PAGES: dict[str, tuple[str, str]] = {
    "index.html": ("", ""),
    "app/index.html": ("../", "browse"),
    "app/discussions/index.html": ("../../", "discussions"),
    "app/models/index.html": ("../../", "models-browser"),
    "details/index.html": ("../", "docs"),
    "contributing/index.html": ("../", "contributing"),
    "downloads/index.html": ("../", "downloads"),
}

_MARKED = re.compile(
    r"(?P<indent>[ \t]*)" + re.escape(START) + r".*?" + re.escape(END), re.DOTALL
)
#: The hand-written header these pages carried before the shared one.
_LEGACY = re.compile(
    r"(?P<indent>[ \t]*)<nav(?: class=\"site-nav\")?>\s*<div class=\"nav-inner\">.*?</nav>",
    re.DOTALL,
)


def render_nav(nav_root: str, nav_active: str) -> str:
    """Render the partial exactly as a template's include would."""
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape=select_autoescape(["html", "j2"]),
    )
    return env.get_template(PARTIAL).render(
        nav_root=nav_root, nav_active=nav_active
    )


def _block(indent: str, html: str) -> str:
    body = "\n".join(
        (indent + line) if line.strip() else ""
        for line in html.strip("\n").splitlines()
    )
    return f"{indent}{START}\n{body}\n{indent}{END}"


def synced_text(text: str, nav_root: str, nav_active: str) -> str:
    """Return ``text`` with its header region replaced by the current partial."""
    html = render_nav(nav_root, nav_active)
    for pattern in (_MARKED, _LEGACY):
        match = pattern.search(text)
        if match:
            return (
                text[: match.start()]
                + _block(match.group("indent"), html)
                + text[match.end() :]
            )
    raise ValueError("no site-nav markers and no legacy <nav> header found")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "--check",
        action="store_true",
        help="write nothing; exit 1 if any page differs from the partial",
    )
    args = parser.parse_args(argv)

    stale = []
    for rel, (nav_root, nav_active) in STATIC_PAGES.items():
        path = REPO_ROOT / rel
        text = path.read_text()
        new = synced_text(text, nav_root, nav_active)
        if new == text:
            continue
        stale.append(rel)
        if not args.check:
            path.write_text(new)

    if args.check:
        if stale:
            print("Site header out of date (run `just sync-site-nav`):")
            for rel in stale:
                print(f"  {rel}")
            return 1
        print(f"Site header current on all {len(STATIC_PAGES)} static pages.")
        return 0
    print(f"Updated {len(stale)} of {len(STATIC_PAGES)} static pages.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
