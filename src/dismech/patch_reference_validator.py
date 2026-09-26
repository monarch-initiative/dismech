"""The two linkml-reference-validator patches dismech still applies.

dismech uses the validator as a library. This module is the exception, and both
patches in it exist in order to be deleted -- each names the upstream issue that
removes it, and `tests/test_upstream_validator_behaviours.py` fails if a third
appears without one.

``_wrap_url_fetch`` strips scripts, comments and tag attributes out of the raw
HTML ``URLSource`` caches. This repository commits its reference cache to a
public git repository and upstream does no extraction on that path at all; 150
of its 199 ``content_type: url`` entries carry a script block.
Tracked as linkml/linkml-reference-validator#92.

``_wrap_jstage_pdf_title`` recovers a title for a PDF URL, which ``URLSource``
otherwise leaves set to the URL itself -- 53 J-STAGE references here. A
URL-as-title is either a blocked title check or a URL copied into the KB as
though it were the paper's name.
Tracked as linkml/linkml-reference-validator#93.

The ten that used to live here are gone: their defects are fixed upstream
(#66-74, #85, #87, #88), and the behaviours dismech relies on are pinned by
``tests/test_upstream_validator_behaviours.py``. See the ``dismech-references``
skill for why a patch here is always temporary.
"""

import logging
import re
from functools import wraps
from urllib.parse import urlsplit, urlunsplit

from bs4 import BeautifulSoup
from linkml_reference_validator.etl.acquire import ContentAcquirer

logger = logging.getLogger("linkml_reference_validator.patch")


def _wrap_url_fetch(original):
    """Cache HTML evidence without executable code or page configuration.

    URLSource returns raw HTML rather than using HTMLExtractor. Page scripts
    and data attributes can contain incidental credentials (including signed
    download URLs) unrelated to the reference text. Retain body markup and
    table structure, but remove code, comments and other attributes before the
    fetcher writes the generated cache. Plain text, XML and extracted PDFs are
    unchanged. This is source extraction, not a browser visibility test.
    """

    @wraps(original)
    def wrapper(self, *args, **kwargs):
        result = original(self, *args, **kwargs)
        if result is None or result.content_type != "url" or not result.content:
            return result
        content = result.content
        if content.lstrip().startswith("<?xml"):
            return result
        soup = BeautifulSoup(content, "html.parser")
        if soup.find("html") is None and not re.search(
            r"<!doctype\s+html\b", content, re.IGNORECASE
        ):
            return result
        from bs4 import Comment

        for tag in soup(["script", "style", "noscript", "template"]):
            tag.decompose()
        for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
            comment.extract()
        for tag in soup.find_all(True):
            structural = {}
            if tag.name in {"td", "th"}:
                for attribute in ("rowspan", "colspan"):
                    value = tag.get(attribute)
                    if value is not None and str(value).isdigit():
                        structural[attribute] = value
                if tag.get("scope") in {"row", "col", "rowgroup", "colgroup"}:
                    structural["scope"] = tag["scope"]
            tag.attrs = structural
        result.content = str(soup)
        return result

    return wrapper


def _jstage_article_url_for_pdf(pdf_url: str) -> str | None:
    """Return J-STAGE's article landing page URL for a direct PDF URL."""
    parts = urlsplit(pdf_url)
    if parts.netloc != "www.jstage.jst.go.jp":
        return None
    if not parts.path.endswith("/_pdf"):
        return None
    return urlunsplit(
        (
            parts.scheme,
            parts.netloc,
            f"{parts.path.removesuffix('/_pdf')}/_article",
            "",
            "",
        )
    )


def _extract_jstage_citation_title(html: bytes) -> str | None:
    """Extract the Highwire citation title J-STAGE exposes on article pages."""
    soup = BeautifulSoup(html.decode("utf-8", errors="replace"), "html.parser")
    meta = soup.find("meta", attrs={"name": "citation_title"})
    if meta is None:
        return None
    title = (meta.get("content") or "").strip()
    return title or None


def _fetch_jstage_pdf_title(pdf_url: str, config) -> str | None:
    """Fetch a J-STAGE PDF's sibling article page and recover its citation title."""
    article_url = _jstage_article_url_for_pdf(pdf_url)
    if article_url is None:
        return None

    try:
        data, _content_type = ContentAcquirer().fetch_bytes(article_url, config)
    except Exception as exc:  # external URL fetch boundary
        logger.warning(
            "Could not fetch J-STAGE article metadata for %s: %s: %s",
            pdf_url,
            type(exc).__name__,
            exc,
        )
        return None
    if data is None:
        return None
    return _extract_jstage_citation_title(data)


def _wrap_jstage_pdf_title(original):
    """Recover J-STAGE PDF titles from the sibling ``_article`` metadata page."""

    @wraps(original)
    def wrapper(self, identifier, config, *args, **kwargs):
        content = original(self, identifier, config, *args, **kwargs)
        if (
            content is not None
            and content.content_type == "full_text_pdf"
            and content.title == identifier.strip()
        ):
            title = _fetch_jstage_pdf_title(identifier.strip(), config)
            if title:
                content.title = title
        return content

    return wrapper


def apply_patch():
    """Install both patches. Idempotent.

    Each is removed when its upstream issue lands (#92, #93).
    """
    try:
        from linkml_reference_validator.etl.sources.url import URLSource
    except ImportError:
        logger.debug("linkml-reference-validator not installed; no patch applied")
        return

    if not getattr(URLSource, "_html_page_code_patch_applied", False):
        URLSource.fetch = _wrap_url_fetch(URLSource.fetch)
        URLSource._html_page_code_patch_applied = True
        logger.debug("Applied URL HTML sanitization patch to URLSource")

    if not getattr(URLSource, "_jstage_pdf_title_patch_applied", False):
        URLSource.fetch = _wrap_jstage_pdf_title(URLSource.fetch)
        URLSource._jstage_pdf_title_patch_applied = True
        logger.debug("Applied J-STAGE PDF title patch to URLSource")


# Auto-apply on import: callers rely on the import side-effect.
apply_patch()
