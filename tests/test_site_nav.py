"""Guard tests for the shared site header (issue #14022).

Each page used to hand-write its own ``<nav>`` header, so the link sets and
even the project's capitalization drifted apart page by page. The header now
lives in one partial, ``src/dismech/templates/_site_nav.html.j2``. These tests
fail if a template writes its own header again, or if a hand-written page's
rendered copy has gone stale against the partial.
"""

import importlib.util
import re
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = REPO_ROOT / "src" / "dismech" / "templates"

_spec = importlib.util.spec_from_file_location(
    "sync_site_nav", REPO_ROOT / "scripts" / "sync_site_nav.py"
)
sync_site_nav = importlib.util.module_from_spec(_spec)
sys.modules["sync_site_nav"] = sync_site_nav
_spec.loader.exec_module(sync_site_nav)

_INCLUDE = re.compile(
    r"\{%-?\s*with\s+nav_root='(?P<root>[./]*)',\s*nav_active='(?P<active>[a-z-]*)'\s*-?%\}"
    r"\s*\{%-?\s*include\s+['\"]_site_nav\.html\.j2['\"]\s*-?%\}"
)


def _full_page_templates() -> list[Path]:
    return sorted(
        path
        for path in TEMPLATE_DIR.glob("*.html.j2")
        if not path.name.startswith("_")
    )


def _link_keys() -> set[str]:
    """Every link key the partial defines, read from its own link list."""
    text = (TEMPLATE_DIR / "_site_nav.html.j2").read_text()
    return set(re.findall(r"\('([a-z-]+)', '[^']+', '[^']+'\)", text)) | {"browse"}


def test_partial_defines_the_link_keys() -> None:
    """Sanity check so a changed tuple layout cannot make the tests vacuous."""
    assert {"browse", "modules", "genes", "docs", "schema"} <= _link_keys()


@pytest.mark.parametrize(
    "template", _full_page_templates(), ids=lambda path: path.name
)
def test_full_page_template_uses_the_shared_header(template: Path) -> None:
    text = template.read_text()
    match = _INCLUDE.search(text)
    assert match, f"{template.name} does not include _site_nav.html.j2"
    # Every template renders to pages/<section>/<page>.html.
    assert match.group("root") == "../../", template.name
    assert match.group("active") in _link_keys() | {""}, (
        f"{template.name}: nav_active={match.group('active')!r} is not a link "
        "key defined in _site_nav.html.j2"
    )
    assert 'class="nav-inner"' not in text, (
        f"{template.name} still carries a hand-written header"
    )


@pytest.mark.parametrize("page", sorted(sync_site_nav.STATIC_PAGES))
def test_static_page_header_matches_the_partial(page: str) -> None:
    nav_root, nav_active = sync_site_nav.STATIC_PAGES[page]
    assert nav_active in _link_keys() | {""}
    text = (REPO_ROOT / page).read_text()
    assert text.count(sync_site_nav.START) == 1, page
    assert sync_site_nav.synced_text(text, nav_root, nav_active) == text, (
        f"{page}: header is stale against _site_nav.html.j2; "
        "run `just sync-site-nav`"
    )


def test_rendered_links_resolve_from_every_depth() -> None:
    """Each internal link, prefixed for a page's depth, points at a real page.

    The targets under ``pages/`` and ``elements/`` are derived output, but they
    are committed by the page build, so a missing one is a broken link.
    """
    for page, (nav_root, nav_active) in sync_site_nav.STATIC_PAGES.items():
        html = sync_site_nav.render_nav(nav_root, nav_active)
        base = (REPO_ROOT / page).parent
        hrefs = re.findall(r'href="([^"]+)"', html)
        internal = [h for h in hrefs if not h.startswith("http")]
        assert len(internal) >= 15, page
        for href in internal:
            target = (base / href).resolve()
            assert target.is_relative_to(REPO_ROOT), (page, href)
            assert target.is_file(), f"{page}: {href} does not exist"


def test_project_name_is_spelled_one_way() -> None:
    html = sync_site_nav.render_nav("", "")
    assert '>DisMech</a>' in html
