"""Gene pages: KB slice, ingest join, provedown-checked summaries, rendering.

Every test builds its own miniature ``kb/`` so it runs in the code lane; the
two tests that read committed files only parse them and never walk the KB.
"""

from __future__ import annotations

import csv
import textwrap
from pathlib import Path

import pytest
import yaml

from dismech.genes.curated import (
    CURATED_DIR,
    UnsafeSummaryError,
    check_document_safety,
    verify_summary,
)
from dismech.genes.ingest import (
    AGR_COLUMNS,
    AGR_FUNCTION_COLUMNS,
    AGR_FUNCTION_TERM_COLUMNS,
    HGNC_COLUMNS,
    INGEST_DIR,
    build_ingest,
    load_ingest,
)
from dismech.genes.slice import build_gene_index, normalize_hgnc_id

REPO = Path(__file__).resolve().parents[1]


def _gene(hgnc_id: str, symbol: str) -> dict:
    return {"preferred_term": symbol, "term": {"id": hgnc_id, "label": symbol}}


DISEASE_A = {
    "name": "Disease A",
    "genetic": [
        {
            "name": "GENE1",
            "gene_term": _gene("hgnc:1", "GENE1"),
            "relationship_type": "CAUSATIVE",
            "variant_origin": "GERMLINE",
            # A CURIE inside evidence is a quote, not a claim about the gene.
            "evidence": [
                {
                    "reference": "PMID:1",
                    "snippet": "GENE2 hgnc:2",
                    "supports": "SUPPORT",
                }
            ],
        }
    ],
    "pathophysiology": [
        {
            "name": "GENE1 Loss, With a Comma",
            "genes": [_gene("HGNC:1", "GENE1")],
            "conforms_to": "some_module#Some Node",
            "genetic_context": {"functional_impact_category": "LOSS_OF_FUNCTION"},
            "biological_processes": [
                {
                    "preferred_term": "x",
                    "term": {"id": "GO:0000001", "label": "process one"},
                }
            ],
        }
    ],
    "treatments": [
        {
            "name": "Silencer",
            "oligonucleotide_details": {"target_gene": _gene("hgnc:2", "GENE2")},
        }
    ],
}

DISEASE_B = {
    "name": "Disease B, Type 2",
    "genetic": [
        {
            "name": "GENE1",
            "gene_term": _gene("hgnc:1", "GENE1"),
            "association": "Causative",
        }
    ],
}


@pytest.fixture
def kb(tmp_path: Path) -> Path:
    root = tmp_path / "kb"
    (root / "disorders").mkdir(parents=True)
    for stem, doc in (("Disease_A", DISEASE_A), ("Disease_B", DISEASE_B)):
        (root / "disorders" / f"{stem}.yaml").write_text(
            yaml.safe_dump(doc), encoding="utf-8"
        )
    return root


def test_normalize_hgnc_id() -> None:
    assert normalize_hgnc_id("HGNC:746") == "hgnc:746"
    assert normalize_hgnc_id("hgnc:746") == "hgnc:746"
    assert normalize_hgnc_id("MGI:1") is None
    assert normalize_hgnc_id("hgnc:abc") is None


def test_slice_finds_structural_occurrences_only(kb: Path) -> None:
    index = build_gene_index(kb)
    gene1 = index["hgnc:1"]
    assert gene1.entries() == ["Disease A", "Disease B, Type 2"]
    assert gene1.relationship_types("Disease A") == ["CAUSATIVE"]
    assert gene1.relationship_types("Disease B, Type 2") == []
    assert gene1.mechanism_nodes("Disease A") == ["GENE1 Loss, With a Comma"]
    assert gene1.modules() == ["some_module"]
    # hgnc:2 is reached through the oligonucleotide target, never the snippet.
    gene2 = index["hgnc:2"]
    assert [(o.section, o.slots) for o in gene2.occurrences] == [
        ("treatments", ("oligonucleotide_details.target_gene",))
    ]


def _write_tsv(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


@pytest.fixture
def ingest_sources(tmp_path: Path) -> tuple[Path, Path]:
    hgnc_dir = tmp_path / "data" / "hgnc"
    hgnc_dir.mkdir(parents=True)
    (hgnc_dir / "MANIFEST.yaml").write_text(
        yaml.safe_dump(
            {
                "snapshot_date": "2026-01-01",
                "bulk_files": [{"name": "hgnc.txt", "sha256": "x"}],
            }
        )
    )
    base = {c: "" for c in HGNC_COLUMNS}
    _write_tsv(
        hgnc_dir / "hgnc.txt",
        [
            {
                **base,
                "hgnc_id": "HGNC:1",
                "symbol": "GENE1",
                "name": "gene one",
                "uniprot_ids": "P00001",
            },
            {
                **base,
                "hgnc_id": "HGNC:2",
                "symbol": "GENE2",
                "name": "gene two",
                "uniprot_ids": "P00002",
            },
        ],
    )
    agr_dir = tmp_path / "data" / "ai-gene-review"
    (agr_dir / "repo" / "genes" / "human" / "GENE1").mkdir(parents=True)
    (agr_dir / "repo" / "genes" / "human" / "GENE2").mkdir(parents=True)
    (agr_dir / "MANIFEST.yaml").write_text(
        yaml.safe_dump(
            {
                "snapshot_date": "2026-01-01",
                "commit": "abc",
                "repository": "x",
                "review_glob": "genes/human/*/*-ai-review.yaml",
            }
        )
    )
    review = {
        "id": "P00001",
        "gene_symbol": "OLDNAME",  # renamed upstream; the UniProt join must still find it
        "status": "COMPLETE",
        "description": "Does a thing.",
        "core_functions": [
            {
                "description": "the thing",
                "molecular_function": {
                    "id": "GO:0000002",
                    "label": "activity, with comma",
                },
                "directly_involved_in": [{"id": "GO:0000001", "label": "process one"}],
            }
        ],
    }
    (
        agr_dir / "repo" / "genes" / "human" / "GENE1" / "GENE1-ai-review.yaml"
    ).write_text(yaml.safe_dump(review))
    # Same symbol as an HGNC gene but a different UniProt: must NOT be joined.
    (
        agr_dir / "repo" / "genes" / "human" / "GENE2" / "GENE2-ai-review.yaml"
    ).write_text(yaml.safe_dump({**review, "id": "Q99999", "gene_symbol": "GENE2"}))
    return hgnc_dir, agr_dir


def test_ingest_joins_on_uniprot_not_symbol(
    kb: Path, ingest_sources, tmp_path: Path
) -> None:
    hgnc_dir, agr_dir = ingest_sources
    out = kb / "genes" / "ingest"
    report = build_ingest(kb_root=kb, hgnc_dir=hgnc_dir, agr_dir=agr_dir, out_dir=out)
    assert report.kb_genes == 2 and report.hgnc_rows == 2
    assert report.reviews_matched == 1
    assert report.reviews_symbol_only == ["GENE2"]
    tables = load_ingest(out)
    assert tables.hgnc["hgnc:1"]["symbol"] == "GENE1"
    assert tables.reviews["hgnc:1"]["review_symbol"] == "OLDNAME"
    assert "hgnc:2" not in tables.reviews
    [function] = tables.functions["hgnc:1"]
    assert function["terms"]["molecular_function"] == [
        ("GO:0000002", "activity, with comma")
    ]


SUMMARY = """\
---
hgnc_id: hgnc:1
symbol: GENE1
status: DRAFT
---

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:1")
</code></pre>

GENE1 is named by <span class="result" data-code="g.disorder_count()">{count}<span class="method"></span></span> disorders:
<span class="result" data-compare="names" data-code="g.disorders()">Disease A; and Disease B, Type 2<span class="method"></span></span>.
It is <span class="result" data-code="g.relationship('Disease A')">causative<span class="method"></span></span> in Disease A and
<span class="result" data-code="g.relationship('Disease B, Type 2')">untyped<span class="method"></span></span> in Disease B, via
<span class="result" data-code="g.node('Disease A', 'GENE1 Loss, With a Comma')">GENE1 Loss, With a Comma<span class="method"></span></span>,
with <span class="result" data-code="g.functional_impact('Disease A')">loss of function<span class="method"></span></span>.
They share <span class="result" data-compare="names" data-code="g.shared_processes()">process one<span class="method"></span></span>.
"""


@pytest.fixture
def summary_kb(kb: Path, ingest_sources, monkeypatch) -> Path:
    hgnc_dir, agr_dir = ingest_sources
    build_ingest(
        kb_root=kb, hgnc_dir=hgnc_dir, agr_dir=agr_dir, out_dir=kb / "genes" / "ingest"
    )
    (kb / "genes" / "curated").mkdir(parents=True)
    monkeypatch.setenv("DISMECH_GENES_KB_ROOT", str(kb))
    return kb


def test_summary_verifies_against_the_kb(summary_kb: Path) -> None:
    path = summary_kb / "genes" / "curated" / "hgnc_1.md"
    path.write_text(SUMMARY.format(count=2), encoding="utf-8")
    result = verify_summary(path)
    assert result.problems == []
    assert (result.state, result.passed) == ("verified", 7)


def test_summary_that_disagrees_with_the_kb_is_stale(summary_kb: Path) -> None:
    path = summary_kb / "genes" / "curated" / "hgnc_1.md"
    path.write_text(SUMMARY.format(count=3), encoding="utf-8")
    result = verify_summary(path)
    assert result.state == "stale"
    assert result.failed == 1
    assert "says '3'" in result.problems[0]


def test_summary_naming_a_missing_node_errors(summary_kb: Path) -> None:
    path = summary_kb / "genes" / "curated" / "hgnc_1.md"
    path.write_text(
        SUMMARY.format(count=2).replace(
            "'GENE1 Loss, With a Comma')", "'Invented Node')"
        ),
        encoding="utf-8",
    )
    result = verify_summary(path)
    assert result.state == "stale" and result.errored == 1
    assert "Invented Node" in result.problems[0]


@pytest.mark.parametrize(
    "code",
    [
        "import os\nos.system('touch PWNED')",
        "from dismech.genes.claims import gene\ng = gene('hgnc:1')\nopen('PWNED', 'w')",
        "from dismech.genes import claims",
    ],
)
def test_unsafe_code_is_refused_before_anything_runs(
    summary_kb: Path, code: str, tmp_path, monkeypatch
) -> None:
    monkeypatch.chdir(tmp_path)
    path = summary_kb / "genes" / "curated" / "hgnc_1.md"
    path.write_text(
        SUMMARY.format(count=2).replace(
            'from dismech.genes.claims import gene\ng = gene("hgnc:1")', code
        ),
        encoding="utf-8",
    )
    result = verify_summary(path)
    assert result.state == "unverified"
    assert any(p.startswith("refused to execute") for p in result.problems)
    assert not (tmp_path / "PWNED").exists()
    assert not (path.parent / "PWNED").exists()


@pytest.mark.parametrize(
    "expression",
    [
        "g._ingest",
        "__import__('os')",
        "open('x')",
        "[x for x in g.disorders()]",
        "g.disorders().__class__",
    ],
)
def test_unsafe_claim_expressions_are_refused(expression: str) -> None:
    from provedown.parser import parse_document

    doc = parse_document(
        '<code>from dismech.genes.claims import gene\ng = gene("hgnc:1")</code>\n'
        f'<span class="result" data-code="{expression}">x</span>'
    )
    with pytest.raises(UnsafeSummaryError):
        check_document_safety(doc)


def test_summary_frontmatter_must_match_file_name(summary_kb: Path) -> None:
    path = summary_kb / "genes" / "curated" / "hgnc_2.md"
    path.write_text(SUMMARY.format(count=2), encoding="utf-8")
    result = verify_summary(path)
    assert any("does not match the file name" in p for p in result.problems)
    assert result.state == "unverified"


def test_render_merges_layers_and_marks_stale(summary_kb: Path, tmp_path: Path) -> None:
    from dismech.genes.render import render_gene_pages

    (summary_kb / "genes" / "curated" / "hgnc_1.md").write_text(
        SUMMARY.format(count=3), encoding="utf-8"
    )
    out = tmp_path / "pages" / "genes"
    written = render_gene_pages(
        output_dir=out,
        min_disorders=2,
        kb_root=summary_kb,
        ingest_dir=summary_kb / "genes" / "ingest",
        curated_dir=summary_kb / "genes" / "curated",
    )
    assert sorted(p.name for p in written) == ["hgnc_1.html", "index.html"]
    page = (out / "hgnc_1.html").read_text()
    assert "gene one" in page  # ingest: HGNC
    assert "Does a thing." in page  # ingest: ai-gene-review
    assert "Stale: 1 of 7 claims" in page  # curated, re-verified
    assert "claim-fail" in page
    assert "../disorders/Disease_B,_Type_2.html" in page  # slice
    assert "untyped" in page
    index = (out / "index.html").read_text()
    assert 'href="hgnc_1.html"' in index
    # GENE2 is named by one disorder, so its index row links to that disorder.
    assert "../disorders/Disease_A.html" in index


def test_committed_ingest_tables_have_the_declared_columns() -> None:
    for name, columns in (
        ("hgnc.tsv", HGNC_COLUMNS),
        ("ai_gene_review.tsv", AGR_COLUMNS),
        ("ai_gene_review_core_functions.tsv", AGR_FUNCTION_COLUMNS),
        ("ai_gene_review_core_function_terms.tsv", AGR_FUNCTION_TERM_COLUMNS),
    ):
        with (REPO / INGEST_DIR / name).open(encoding="utf-8") as fh:
            assert tuple(fh.readline().rstrip("\n").split("\t")) == columns, name


@pytest.mark.parametrize(
    "path", sorted((REPO / CURATED_DIR).glob("*.md")), ids=lambda p: p.name
)
def test_committed_summaries_are_well_formed_and_safe(path: Path) -> None:
    """Static only: running the claims needs the whole KB (`just genes-verify`)."""
    result = verify_summary(path, execute=False)
    assert result.problems == [], textwrap.indent("\n".join(result.problems), "  ")
    assert result.claims == 0  # not executed
