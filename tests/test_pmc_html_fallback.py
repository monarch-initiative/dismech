"""Regression coverage for real PMC HTML fallback shapes."""

from types import SimpleNamespace

import pytest
import requests
from linkml_reference_validator.etl.fulltext.base import FullTextProviderRegistry
from linkml_reference_validator.models import (
    ReferenceIdentifiers,
    ReferenceValidationConfig,
)

import dismech.patch_reference_validator  # noqa: F401 -- installs the provider patch


def _provider(monkeypatch, html, xml=None):
    provider = FullTextProviderRegistry.get("pmc")
    calls = []

    def fetch_xml(pmcid, config):
        if isinstance(xml, Exception):
            raise xml
        return xml

    def get(url, **kwargs):
        calls.append(url)
        return SimpleNamespace(status_code=200, content=html.encode())

    monkeypatch.setattr(provider, "_fetch_pmc_xml_bytes", fetch_xml)
    monkeypatch.setattr(requests, "get", get)
    return provider, calls


@pytest.mark.parametrize("pmcid", ["3060324", "PMC3060324"])
@pytest.mark.parametrize(
    "xml",
    [b"<article><front>No XML body</front></article>", OSError("XML unavailable")],
)
def test_public_article_survives_unavailable_xml(monkeypatch, pmcid, xml):
    body = "The Results and Discussion contain the clinical observations. " * 25
    html = f"""<html><nav>Do not include navigation</nav><article>
      <h2>Results</h2><p>{body}</p>
      <figure><figcaption><p>The siblings show strabismus.</p></figcaption></figure>
      <table><caption><p>Table 2</p></caption>
        <tr><th>Feature</th><th>Patient 9</th><th>Siblings 10–11</th><th>Patient 12</th></tr>
        <tr><td><p>Micrognathia</p></td><td>−</td><td>+</td><td>−</td></tr>
        <tr><td>Neuro<i>genesis</i> and Ca<sup>2+</sup><br/>signal<p>Next</p><p>block</p></td><td>+</td><td>+</td><td></td></tr>
        <tr><td>Large wide spaced teeth</td><td>+</td><td>+</td><td></td></tr>
      </table><script>Never quote scripts</script></article></html>"""
    provider, calls = _provider(monkeypatch, html, xml)
    result = provider.locate(
        ReferenceIdentifiers(pmcid=pmcid), ReferenceValidationConfig(rate_limit_delay=0)
    )
    assert result.format_hint == "html"
    assert result.provider == "pmc"
    assert result.url == "https://pmc.ncbi.nlm.nih.gov/articles/PMC3060324/"
    assert calls == [result.url]
    assert "The siblings show strabismus." in result.text
    assert "Table 2" in result.text
    assert "Feature | Patient 9 | Siblings 10–11 | Patient 12" in result.text
    assert result.text.count("Micrognathia") == 1
    assert "Micrognathia | − | + | −" in result.text
    assert "Large wide spaced teeth | + | + |" in result.text
    assert "Neurogenesis and Ca2+ signal Next block | + | + |" in result.text
    assert "Do not include navigation" not in result.text
    assert "Never quote scripts" not in result.text
    assert all(line == line.rstrip() for line in result.text.splitlines())


def test_available_xml_remains_preferred(monkeypatch):
    body = "Clinical findings are available in the XML article body. " * 25
    provider, calls = _provider(
        monkeypatch,
        "<article><p>HTML fallback</p></article>",
        f"<article><body><p>{body}</p></body></article>".encode(),
    )
    result = provider.locate(
        ReferenceIdentifiers(pmcid="3060324"),
        ReferenceValidationConfig(rate_limit_delay=0),
    )
    assert result.format_hint == "xml"
    assert body.strip() in result.text
    assert calls == []


@pytest.mark.parametrize(
    "html",
    [
        "<html><main><p>Checking your browser "
        + "challenge " * 200
        + "</p></main></html>",
        "<article><p>Only a short abstract.</p></article>",
        '<article><section class="abstract"><p>'
        + "Long abstract only. " * 100
        + '</p></section><section class="ref-list">'
        + "Bibliographic material. " * 100
        + "</section></article>",
    ],
)
def test_challenge_pages_and_short_stubs_are_not_full_text(monkeypatch, html):
    provider, _ = _provider(monkeypatch, html)
    result = provider.locate(
        ReferenceIdentifiers(pmcid="3060324"),
        ReferenceValidationConfig(rate_limit_delay=0),
    )
    assert result is None


@pytest.mark.parametrize(
    "container", ["article", 'div class="article-body"', 'div class="tsec"']
)
def test_inline_whitespace_and_legacy_containers(monkeypatch, container):
    tag = container.split()[0]
    filler = "Clinical observations from the body. " * 40
    html = f"<{container}><p>{filler}</p><p>Neuro<i>genesis</i> and Ca<sup>2+</sup> in <i>islet</i> cells.</p></{tag}>"
    provider, _ = _provider(monkeypatch, html)
    result = provider._fetch_pmc_html(
        "3060324", ReferenceValidationConfig(rate_limit_delay=0)
    )
    assert result.endswith("Neurogenesis and Ca2+ in islet cells.")


def test_oversized_tables_do_not_displace_the_article(monkeypatch):
    body = "Keep the article paragraph. " * 40
    html = (
        f"<article><p>{body}</p><table>"
        + "<tr><td>Data dump</td></tr>" * 201
        + "</table></article>"
    )
    provider, _ = _provider(monkeypatch, html)
    result = provider._fetch_pmc_html(
        "3060324", ReferenceValidationConfig(rate_limit_delay=0)
    )
    assert result == body.strip()
