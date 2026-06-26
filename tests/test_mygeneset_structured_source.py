"""Tests for the MyGeneset / MSigDB gene-set structured source.

These run fully offline against fixture files written into ``tmp_path`` — the
network-backed ``refresh()`` is exercised separately/manually.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from dismech.reference_cache_frontmatter import check_cache_file
from dismech.structured_sources.mygeneset import MyGenesetSource


INTERP_YAML = """\
gene_set_id: MSIGDB:KEGG_ASTHMA
gene_set_name: KEGG_ASTHMA
collection: C2:CP:KEGG_LEGACY
msigdb_release: v2025.1.Hs
description: >-
  KEGG legacy asthma pathway gene set representing the allergic
  inflammatory cascade in asthma.
contexts:
  - term:
      id: MONDO:0004979
      label: asthma
    context_type: disease
  - term:
      id: UBERON:0002048
      label: lung
    context_type: anatomical_structure
associations:
  - term:
      id: GO:0045064
      label: T-helper 2 cell differentiation
    aspect: biological_process
    category: core_process
    confidence: high
  - term:
      id: GO:0006412
      label: translation
    aspect: biological_process
    category: nonspecific
    confidence: high
"""

MEMBERSHIP = [
    {"symbol": "IL4", "ncbigene": "3565"},
    {"symbol": "IL13", "ncbigene": "3596"},
    {"symbol": "CCL11", "ncbigene": "6356"},
]


@pytest.fixture()
def geneset_source(tmp_path: Path) -> MyGenesetSource:
    interp = tmp_path / "interpretations"
    member = tmp_path / "membership"
    interp.mkdir()
    member.mkdir()
    (interp / "KEGG_ASTHMA.yaml").write_text(INTERP_YAML, encoding="utf-8")
    (member / "KEGG_ASTHMA.json").write_text(json.dumps(MEMBERSHIP), encoding="utf-8")
    src = MyGenesetSource(tmp_path)
    src.index()
    return src


def test_local_id_strips_source_prefix():
    assert MyGenesetSource.local_id_from_gene_set_id("MSIGDB:KEGG_ASTHMA") == "KEGG_ASTHMA"
    assert MyGenesetSource.local_id_from_gene_set_id("KEGG_ASTHMA") == "KEGG_ASTHMA"


def test_index_reads_interpretation_and_membership(geneset_source: MyGenesetSource):
    idx = geneset_source.index()
    assert list(idx) == ["KEGG_ASTHMA"]
    rec = idx["KEGG_ASTHMA"]
    assert rec.gene_set_id == "MSIGDB:KEGG_ASTHMA"
    assert rec.source == "msigdb"
    assert rec.collection == "C2:CP:KEGG_LEGACY"
    assert [a.go_id for a in rec.associations] == ["GO:0045064", "GO:0006412"]
    assert [g.symbol for g in rec.genes] == ["IL4", "IL13", "CCL11"]


def test_identifiers(geneset_source: MyGenesetSource):
    assert list(geneset_source.identifiers()) == ["KEGG_ASTHMA"]


def test_serialize_blocks_and_frontmatter(geneset_source: MyGenesetSource):
    entry = geneset_source.serialize("KEGG_ASTHMA")
    assert entry.filename() == "MYGENESET_KEGG_ASTHMA.md"
    text = entry.render()

    assert 'reference_id: "MYGENESET:KEGG_ASTHMA"' in text
    assert 'database: "mygeneset.info"' in text
    assert 'content_type: "structured_record"' in text

    # Quotable rows — these are exactly what a curator would paste as a snippet.
    assert (
        "| GO:0045064 | T-helper 2 cell differentiation | biological_process | "
        "core_process | high |"
    ) in text
    assert "| IL4 | NCBIGene:3565 |" in text
    assert "| disease | MONDO:0004979 | asthma |" in text
    assert "## Members (3 genes)" in text
    assert "Upstream identifier: `MSIGDB:KEGG_ASTHMA`." in text


def test_serialize_accepts_prefixed_identifier(geneset_source: MyGenesetSource):
    a = geneset_source.serialize("KEGG_ASTHMA").render()
    b = geneset_source.serialize("MYGENESET:KEGG_ASTHMA").render()
    assert a == b


def test_serialize_unknown_id_raises(geneset_source: MyGenesetSource):
    with pytest.raises(KeyError):
        geneset_source.serialize("NOPE")


def test_cache_file_passes_frontmatter_contract(
    geneset_source: MyGenesetSource, tmp_path: Path
):
    out = tmp_path / "cache"
    path = geneset_source.write_cache_file("KEGG_ASTHMA", out)
    # check_cache_file returns None when the file satisfies the cache contract.
    assert check_cache_file(path) is None


def test_membership_optional(tmp_path: Path):
    """A set with no mygeneset membership still serializes (no Members block)."""
    interp = tmp_path / "interpretations"
    interp.mkdir()
    (interp / "KEGG_ASTHMA.yaml").write_text(INTERP_YAML, encoding="utf-8")
    (tmp_path / "membership").mkdir()
    src = MyGenesetSource(tmp_path)
    text = src.serialize("KEGG_ASTHMA").render()
    assert "## Members" not in text
    assert "## Curated GO interpretation" in text
