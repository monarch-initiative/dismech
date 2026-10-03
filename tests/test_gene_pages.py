"""Gene pages: KB slice, ingest join, provedown-checked summaries, rendering.

Every test builds its own miniature ``kb/`` so it runs in the code lane; the
two tests that read committed files only parse them and never walk the KB.
"""

from __future__ import annotations

import csv
import subprocess
import textwrap
from dataclasses import dataclass
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
    CLINGEN_COLUMNS,
    HGNC_COLUMNS,
    INGEST_DIR,
    build_ingest,
    load_ingest,
)
from dismech.genes.slice import build_gene_index, normalize_hgnc_id
from dismech.structured_sources.base import ChecksumMismatchError, _sha256_of

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
    "disease_term": {
        "preferred_term": "b",
        "term": {"id": "MONDO:0000002", "label": "b"},
    },
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


def _pin(data_dir: Path, name: str) -> None:
    (data_dir / "MANIFEST.yaml").write_text(
        yaml.safe_dump(
            {
                "snapshot_date": "2026-01-01",
                "bulk_files": [
                    {
                        "name": name,
                        "url": "https://example.org/x",
                        "sha256": _sha256_of(data_dir / name),
                    }
                ],
            }
        )
    )


CLINGEN_CSV = textwrap.dedent(
    """\
    "CLINGEN GENE DISEASE VALIDITY CURATIONS","","","","","","","","",""
    "FILE CREATED: 2026-01-01","","","","","","","","",""
    "WEBPAGE: https://search.clinicalgenome.org/kb/gene-validity","","","","","","","","",""
    "+++++++++++","++++++++++++++","+++++++++++++","++++++++++++++++++","+++++++++","+++++++++","+++++++++++++++++","+++++++++++++++","+++++++++++++++++++++++","++++"
    "GENE SYMBOL","GENE ID (HGNC)","DISEASE LABEL","DISEASE ID (MONDO)","MOI","SOP","CLASSIFICATION","ONLINE REPORT","CLASSIFICATION DATE","GCEP"
    "+++++++++++","++++++++++++++","+++++++++++++","++++++++++++++++++","+++++++++","+++++++++","+++++++++++++++++","+++++++++++++++","+++++++++++++++++++++++","++++"
    "GENE1","HGNC:1","disease b","MONDO:0000002","AD","SOP10","Definitive","https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_aaa-2026-01-01T000000.000Z","2026-01-01T00:00:00.000Z","Panel"
    "GENE1","HGNC:1","disease c","MONDO:0000003","AR","SOP10","Limited","https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_bbb-2026-01-01T000000.000Z","2026-01-01T00:00:00.000Z","Panel"
    "GENE9","HGNC:9","not in the kb","MONDO:0000009","AD","SOP10","Definitive","https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_ccc-2026-01-01T000000.000Z","2026-01-01T00:00:00.000Z","Panel"
    """
)


@dataclass
class Sources:
    hgnc: Path
    agr: Path
    clingen: Path

    def build(self, kb: Path, out: Path):
        return build_ingest(
            kb_root=kb,
            hgnc_dir=self.hgnc,
            agr_dir=self.agr,
            clingen_dir=self.clingen,
            out_dir=out,
        )


@pytest.fixture
def ingest_sources(tmp_path: Path) -> Sources:
    hgnc_dir = tmp_path / "data" / "hgnc"
    hgnc_dir.mkdir(parents=True)
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
    _pin(hgnc_dir, "hgnc.txt")

    clingen_dir = tmp_path / "data" / "clingen-genes"
    clingen_dir.mkdir(parents=True)
    (clingen_dir / "gene_validity.csv").write_text(CLINGEN_CSV, encoding="utf-8")
    _pin(clingen_dir, "gene_validity.csv")

    agr_dir = tmp_path / "data" / "ai-gene-review"
    repo = agr_dir / "repo"
    (repo / "genes" / "human" / "GENE1").mkdir(parents=True)
    (repo / "genes" / "human" / "GENE2").mkdir(parents=True)
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
    (repo / "genes" / "human" / "GENE1" / "GENE1-ai-review.yaml").write_text(
        yaml.safe_dump(review)
    )
    # Same symbol as an HGNC gene but a different UniProt: must NOT be joined.
    (repo / "genes" / "human" / "GENE2" / "GENE2-ai-review.yaml").write_text(
        yaml.safe_dump({**review, "id": "Q99999", "gene_symbol": "GENE2"})
    )
    git = [
        "git",
        "-C",
        str(repo),
        "-c",
        "user.name=t",
        "-c",
        "user.email=t@example.org",
    ]
    subprocess.run(["git", "init", "-q", str(repo)], check=True)
    subprocess.run([*git, "add", "."], check=True)
    subprocess.run([*git, "commit", "-q", "-m", "fixture"], check=True)
    commit = subprocess.run(
        [*git, "rev-parse", "HEAD"], check=True, capture_output=True, text=True
    ).stdout.strip()
    (agr_dir / "MANIFEST.yaml").write_text(
        yaml.safe_dump(
            {
                "snapshot_date": "2026-01-01",
                "commit": commit,
                "repository": "x",
                "review_glob": "genes/human/*/*-ai-review.yaml",
            }
        )
    )
    return Sources(hgnc_dir, agr_dir, clingen_dir)


def test_ingest_joins_on_uniprot_not_symbol(
    kb: Path, ingest_sources, tmp_path: Path
) -> None:
    out = kb / "genes" / "ingest"
    report = ingest_sources.build(kb, out)
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


def test_clingen_rows_are_limited_to_kb_genes_and_joined_by_mondo(
    kb: Path, ingest_sources
) -> None:
    from dismech.genes.join import NOT_NAMED, UNTYPED, clingen_matches
    from dismech.genes.slice import entry_mondo_index

    out = kb / "genes" / "ingest"
    report = ingest_sources.build(kb, out)
    assert report.clingen_rows == 2  # GENE9 is named by no KB entry
    tables = load_ingest(out)
    assert [r["assertion_id"] for r in tables.clingen["hgnc:1"]] == [
        "CGGV:assertion_aaa-2026-01-01T000000.000Z",
        "CGGV:assertion_bbb-2026-01-01T000000.000Z",
    ]
    matches = clingen_matches(
        build_gene_index(kb)["hgnc:1"], tables.clingen["hgnc:1"], entry_mondo_index(kb)
    )
    by_disease = {m.row["disease_label"]: m.entries for m in matches}
    # Disease B's disease_term is MONDO:0000002 and its record is untyped.
    assert by_disease == {"disease b": {"Disease B, Type 2": UNTYPED}, "disease c": {}}
    assert NOT_NAMED != UNTYPED


def test_build_refuses_an_input_that_does_not_match_its_pin(
    kb: Path, ingest_sources
) -> None:
    with (ingest_sources.clingen / "gene_validity.csv").open("a") as fh:
        fh.write("\n")
    with pytest.raises(ChecksumMismatchError):
        ingest_sources.build(kb, kb / "genes" / "ingest")


def test_build_refuses_an_ai_gene_review_checkout_off_its_pinned_commit(
    kb: Path, ingest_sources
) -> None:
    manifest = ingest_sources.agr / "MANIFEST.yaml"
    data = yaml.safe_load(manifest.read_text())
    manifest.write_text(yaml.safe_dump({**data, "commit": "0" * 40}))
    with pytest.raises(RuntimeError, match="not the pinned commit"):
        ingest_sources.build(kb, kb / "genes" / "ingest")


def test_refused_refresh_keeps_the_pinned_file(ingest_sources, monkeypatch) -> None:
    from dismech.genes import ingest
    from dismech.structured_sources.base import StructuredSource

    pinned = (ingest_sources.clingen / "gene_validity.csv").read_bytes()
    monkeypatch.setattr(
        StructuredSource,
        "_download",
        staticmethod(lambda url, target: Path(target).write_text("a new release")),
    )
    with pytest.raises(ChecksumMismatchError):
        ingest.refresh_pinned_files(ingest_sources.clingen, force=True)
    assert (ingest_sources.clingen / "gene_validity.csv").read_bytes() == pinned
    assert not list(ingest_sources.clingen.glob("*.download"))


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
ClinGen rates it <span class="result" data-code="g.clingen('Disease B, Type 2')">definitive<span class="method"></span></span> there,
which leaves <span class="result" data-compare="names" data-code="g.clingen_but_untyped()">Disease B, Type 2<span class="method"></span></span> to type.
"""


@pytest.fixture
def summary_kb(kb: Path, ingest_sources, monkeypatch) -> Path:
    ingest_sources.build(kb, kb / "genes" / "ingest")
    (kb / "genes" / "curated").mkdir(parents=True)
    monkeypatch.setenv("DISMECH_GENES_KB_ROOT", str(kb))
    return kb


def test_summary_verifies_against_the_kb(summary_kb: Path) -> None:
    path = summary_kb / "genes" / "curated" / "hgnc_1.md"
    path.write_text(SUMMARY.format(count=2), encoding="utf-8")
    result = verify_summary(path)
    assert result.problems == []
    assert (result.state, result.passed) == ("verified", 9)


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
    assert "Stale: 1 of 9 claims" in page
    assert "no dismech entry" in page  # ClinGen disease c
    assert "CGGV:assertion_aaa" in page  # curated, re-verified
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
        ("clingen_gene_validity.tsv", CLINGEN_COLUMNS),
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


def test_disorder_page_links_only_genes_that_have_a_page(kb: Path, tmp_path: Path) -> None:
    """GENE1 is named by two disorders, so it has a page; GENE2 by one, so not."""
    from dismech.genes.render import gene_page_ids
    from dismech.render import render_disorder

    assert gene_page_ids(str(kb.resolve())) == frozenset({"hgnc:1"})
    out = render_disorder(kb / "disorders" / "Disease_A.yaml", tmp_path / "Disease_A.html")
    html = out.read_text()
    assert 'class="gene-page-link" href="../genes/hgnc_1.html"' in html
    assert "../genes/hgnc_2.html" not in html
