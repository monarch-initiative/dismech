"""The two patches dismech still applies over linkml-reference-validator.

``_wrap_url_fetch`` (upstream #92) and ``_wrap_jstage_pdf_title`` (upstream #93).
When those land, this file and ``src/dismech/patch_reference_validator.py`` are
both deleted.

Everything else that used to be tested here is now
``tests/test_upstream_validator_behaviours.py``, which asserts the behaviour
dismech needs rather than the patch that used to provide it.
"""


import pytest
from linkml_reference_validator.models import ReferenceValidationConfig


def test_url_html_fetch_removes_page_configuration_but_keeps_evidence(monkeypatch):
    from bs4 import BeautifulSoup
    from linkml_reference_validator.etl.acquire import ContentAcquirer
    from linkml_reference_validator.etl.sources.url import URLSource

    from dismech.patch_reference_validator import apply_patch

    apply_patch()
    page = b"""<!doctype html><html><head><title>Clinical guideline</title>
    <script>window.configuration = 'script-only-value';</script>
    <style>.private { content: 'style-only-value'; }</style></head>
    <body><!-- comment-only-value -->
    <div data-page='{"token":"attribute-only-value"}'>
    <p>For <abbr title="abbreviation-only-value">AVSD</abbr>, PVR &lt;5.</p>
    <table><tr><th rowspan="2" scope="rowgroup">Outcome</th>
    <td colspan="2">2 of 3</td></tr><tr><td>A</td><td>B</td></tr></table>
    <a href="https://example.org/?token=link-only-value">Study source</a>
    <template>template-only-value</template>
    </div></body></html>"""
    monkeypatch.setattr(
        ContentAcquirer, "fetch_bytes", lambda *_: (page, "text/html; charset=utf-8")
    )
    result = URLSource().fetch(
        "https://example.org/guideline", ReferenceValidationConfig()
    )
    assert result.title == "Clinical guideline"
    assert result.reference_id == "url:https://example.org/guideline"
    assert result.content_type == "url"
    assert "only-value" not in result.content
    soup = BeautifulSoup(result.content, "html.parser")
    assert soup.p.get_text() == "For AVSD, PVR <5."
    assert soup.th.get_text() == "Outcome"
    assert soup.th.attrs == {"rowspan": "2", "scope": "rowgroup"}
    assert soup.td.get_text() == "2 of 3"
    assert soup.td.attrs == {"colspan": "2"}
    assert soup.a.get_text() == "Study source"


@pytest.mark.parametrize(
    "content, content_type",
    [
        ("Plain text including <5 and >10", "url"),
        ('<?xml version="1.0"?><body id="preserved">XML content</body>', "url"),
        ('<article><body id="preserved"><p>JATS content</p></body></article>', "url"),
        ("Extracted PDF text with <html> quoted literally", "full_text_pdf"),
    ],
)


def test_url_page_code_removal_preserves_non_html_sources(content, content_type):
    from types import SimpleNamespace

    from dismech.patch_reference_validator import _wrap_url_fetch

    reference = SimpleNamespace(content=content, content_type=content_type)
    wrapped = _wrap_url_fetch(lambda *_: reference)
    assert wrapped(None) is reference
    assert reference.content == content


def test_jstage_pdf_title_patch_reads_sibling_article_metadata(monkeypatch):
    """Direct J-STAGE PDF URLs should not be cached with the URL as title."""
    from linkml_reference_validator.etl.sources.url import URLSource
    from linkml_reference_validator.models import ReferenceContent

    import dismech.patch_reference_validator as patch

    seen_urls = []

    class _Acquirer:
        def fetch_bytes(self, url, _config):
            seen_urls.append(url)
            return (
                b'<meta name="citation_title" content="Recovered J-STAGE Title" />',
                "text/html",
            )

    def _fetch_pdf(self, identifier, _config):
        return ReferenceContent(
            reference_id=f"url:{identifier}",
            title=identifier,
            content="Extracted PDF body",
            content_type="full_text_pdf",
            full_text_url=identifier,
        )

    monkeypatch.setattr(patch, "ContentAcquirer", _Acquirer)

    content = patch._wrap_jstage_pdf_title(_fetch_pdf)(
        URLSource(),
        "https://www.jstage.jst.go.jp/article/jhs/52/3/52_3_259/_pdf",
        ReferenceValidationConfig(),
    )

    assert content.title == "Recovered J-STAGE Title"
    assert seen_urls == [
        "https://www.jstage.jst.go.jp/article/jhs/52/3/52_3_259/_article"
    ]


def test_jstage_pdf_title_patch_leaves_unrelated_pdf_titles_alone(monkeypatch):
    """The J-STAGE title lookup must stay scoped to J-STAGE direct PDFs."""
    from linkml_reference_validator.etl.sources.url import URLSource
    from linkml_reference_validator.models import ReferenceContent

    import dismech.patch_reference_validator as patch

    def _fetch_pdf(self, identifier, _config):
        return ReferenceContent(
            reference_id=f"url:{identifier}",
            title=identifier,
            content="Extracted PDF body",
            content_type="full_text_pdf",
            full_text_url=identifier,
        )

    def _forbidden_acquirer():
        raise AssertionError("non-J-STAGE PDFs should not fetch an article page")

    monkeypatch.setattr(patch, "ContentAcquirer", _forbidden_acquirer)

    content = patch._wrap_jstage_pdf_title(_fetch_pdf)(
        URLSource(),
        "https://example.org/paper.pdf",
        ReferenceValidationConfig(),
    )

    assert content.title == "https://example.org/paper.pdf"
