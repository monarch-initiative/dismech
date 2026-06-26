"""Tests for the gene-set BP aligner (offline; stub GO adapter)."""

from __future__ import annotations

from pathlib import Path

from dismech import genesets_align as ga


CACHE_MD = """\
---
reference_id: "MYGENESET:DEMO"
title: "DEMO"
content_type: "structured_record"
---

# MYGENESET:DEMO  DEMO

## Curated GO interpretation

| GO ID | Label | Aspect | Role | Confidence |
|---|---|---|---|---|
| GO:0000001 | exact core | biological_process | core_process | high |
| GO:0000002 | specific-in-pathograph core | biological_process | core_process | high |
| GO:0000003 | broader-only core | biological_process | core_process | medium |
| GO:0000004 | missing core | cellular_component | core_component | medium |
| GO:0000009 | noise present | biological_process | nonspecific | high |
| GO:0000008 | noise broader-only | biological_process | nonspecific | high |

## Members (1 genes)

| Symbol | Gene ID |
|---|---|
| FOO | hgnc:1 |
"""

DISEASE_YAML = """\
name: Demo Disease
pathophysiology:
- name: Node A
  biological_processes:
  - term: {id: GO:0000001, label: exact core}
  - term: {id: GO:0000002CHILD, label: specific child}
  - term: {id: GO:0000009, label: noise present}
  - term: {id: GO:9999999, label: unrelated}
"""


class _StubGO:
    """Minimal GO adapter: explicit ancestor/descendant maps."""

    def __init__(self, ancestors: dict, descendants: dict) -> None:
        self._anc = ancestors
        self._desc = descendants

    def ancestors(self, t, predicates=None):
        return self._anc.get(t, [])

    def descendants(self, t, predicates=None):
        return self._desc.get(t, [])


def _adapter() -> _StubGO:
    # GO:9999999 is present in the pathograph; making it an ancestor of the
    # broader-only BPs yields an ANCESTOR (not-counted) match.
    return _StubGO(
        ancestors={"GO:0000003": ["GO:9999999"], "GO:0000008": ["GO:9999999"]},
        descendants={"GO:0000002": ["GO:0000002CHILD"]},
    )


def test_read_set_bps(tmp_path: Path):
    p = tmp_path / "MYGENESET_DEMO.md"
    p.write_text(CACHE_MD, encoding="utf-8")
    bps = ga.read_set_bps(p)
    assert [b.go_id for b in bps] == [
        "GO:0000001",
        "GO:0000002",
        "GO:0000003",
        "GO:0000004",
        "GO:0000009",
        "GO:0000008",
    ]
    assert bps[0].category == "core_process"
    # The Members table must not leak into the BP list.
    assert all(b.go_id.startswith("GO:") for b in bps)


def test_extract_pathograph_bps(tmp_path: Path):
    p = tmp_path / "Demo.yaml"
    p.write_text(DISEASE_YAML, encoding="utf-8")
    bps = ga.extract_pathograph_bps(p)
    assert set(bps) == {"GO:0000001", "GO:0000002CHILD", "GO:0000009", "GO:9999999"}


def test_alignment_statuses_and_scoring(tmp_path: Path):
    (tmp_path / "MYGENESET_DEMO.md").write_text(CACHE_MD, encoding="utf-8")
    (tmp_path / "Demo.yaml").write_text(DISEASE_YAML, encoding="utf-8")
    set_bps = ga.read_set_bps(tmp_path / "MYGENESET_DEMO.md")
    pathograph = ga.extract_pathograph_bps(tmp_path / "Demo.yaml")

    result = ga.align("MYGENESET:DEMO", "Demo", set_bps, pathograph, _adapter())
    by_id = {r.bp.go_id: r for r in result.rows}

    assert by_id["GO:0000001"].status == ga.EXACT
    assert by_id["GO:0000002"].status == ga.DESCENDANT
    assert by_id["GO:0000002"].matched_id == "GO:0000002CHILD"
    assert by_id["GO:0000003"].status == ga.ANCESTOR
    assert by_id["GO:0000004"].status == ga.NONE
    assert by_id["GO:0000009"].status == ga.EXACT

    # Core covered = EXACT + DESCENDANT only (ANCESTOR does NOT count).
    assert result.core_total == 4  # GO:1, GO:2, GO:3, GO:4
    assert result.core_covered == 2  # GO:1, GO:2
    assert result.corroboration == 0.5

    # Gaps include the broader-only core BP and the truly-missing one.
    gap_ids = {r.bp.go_id for r in result.gaps}
    assert gap_ids == {"GO:0000003", "GO:0000004"}

    # Lint: a noise BP present (EXACT) flags; a noise BP matched only to an
    # ancestor does NOT.
    lint_ids = {r.bp.go_id for r in result.lint}
    assert lint_ids == {"GO:0000009"}


CACHE_WITH_CONTEXT = """\
---
reference_id: "MYGENESET:DEMO"
title: "DEMO"
---

## Context

| Type | Term | Label |
|---|---|---|
| disease | MONDO:1234567 | demo disease |

## Curated GO interpretation

| GO ID | Label | Aspect | Role | Confidence |
|---|---|---|---|---|
| GO:0000001 | exact core | biological_process | core_process | high |
"""

DISEASE_WITH_MONDO = """\
name: Demo Disease
disease_term:
  term: {id: MONDO:1234567, label: demo disease}
pathophysiology:
- name: N
  biological_processes:
  - term: {id: GO:0000001, label: exact core}
"""


def test_disease_context_mondo(tmp_path: Path):
    p = tmp_path / "MYGENESET_DEMO.md"
    p.write_text(CACHE_WITH_CONTEXT, encoding="utf-8")
    assert ga.disease_context_mondo(p) == "MONDO:1234567"


def test_build_mondo_index_and_sweep(tmp_path: Path):
    kb = tmp_path / "kb"
    cache = tmp_path / "cache"
    kb.mkdir()
    cache.mkdir()
    (kb / "Demo.yaml").write_text(DISEASE_WITH_MONDO, encoding="utf-8")
    (cache / "MYGENESET_DEMO.md").write_text(CACHE_WITH_CONTEXT, encoding="utf-8")

    index = ga.build_mondo_index(kb)
    assert index["MONDO:1234567"] == "Demo"

    entries = ga.sweep(cache, kb, adapter=None)
    assert len(entries) == 1
    e = entries[0]
    assert e.set_id == "DEMO" and e.disorder == "Demo"
    assert e.result is not None and e.result.core_covered == 1
    assert "Demo" in ga.format_sweep(entries)


def test_exact_only_without_adapter(tmp_path: Path):
    (tmp_path / "MYGENESET_DEMO.md").write_text(CACHE_MD, encoding="utf-8")
    (tmp_path / "Demo.yaml").write_text(DISEASE_YAML, encoding="utf-8")
    set_bps = ga.read_set_bps(tmp_path / "MYGENESET_DEMO.md")
    pathograph = ga.extract_pathograph_bps(tmp_path / "Demo.yaml")
    # No adapter -> only exact GO-id matches; descendant/ancestor unavailable.
    result = ga.align("MYGENESET:DEMO", "Demo", set_bps, pathograph, adapter=None)
    by_id = {r.bp.go_id: r for r in result.rows}
    assert by_id["GO:0000001"].status == ga.EXACT
    assert by_id["GO:0000002"].status == ga.NONE
    assert "Corroboration" in ga.format_report(result)
