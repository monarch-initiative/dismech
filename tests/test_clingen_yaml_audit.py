from __future__ import annotations

from collections import Counter
from pathlib import Path

from dismech.structured_sources.clingen_yaml_audit import (
    audit_clingen_yaml,
    format_summary,
    format_tsv,
)


def test_audit_clingen_yaml_classifies_done_missing_and_blocked(tmp_path: Path):
    data_dir = tmp_path / "data" / "clingen"
    kb_dir = tmp_path / "kb" / "disorders"
    cache_dir = tmp_path / "references_cache"
    data_dir.mkdir(parents=True)
    kb_dir.mkdir(parents=True)
    cache_dir.mkdir()

    (data_dir / "gene_validity.csv").write_text(
        "\n".join(
            [
                "FILE CREATED: 2026-01-24",
                "WEBPAGE: https://search.clinicalgenome.org/kb/gene-validity",
                '"GENE SYMBOL","GENE ID (HGNC)","DISEASE LABEL","DISEASE ID (MONDO)","MOI","SOP","CLASSIFICATION","ONLINE REPORT","CLASSIFICATION DATE","GCEP"',
                '"GENE1","HGNC:1","Disease A","MONDO:0000001","AD","SOP10","Definitive","https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_done","2026-01-01T00:00:00.000Z","Panel"',
                '"GENE2","HGNC:2","Disease A","MONDO:0000001","AD","SOP10","Strong","https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_missing","2026-01-01T00:00:00.000Z","Panel"',
                '"GENE3","HGNC:3","Broad disease","MONDO:0000002","AD","SOP10","Moderate","https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_gene_specific","2026-01-01T00:00:00.000Z","Panel"',
                '"GENE4","HGNC:4","Disease B","MONDO:0000003","AR","SOP10","Limited","https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_label_mismatch","2026-01-01T00:00:00.000Z","Panel"',
                '"GENE5","HGNC:5","Disease A","MONDO:0000001","AR","SOP10","Refuted","https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_refuted","2026-01-01T00:00:00.000Z","Panel"',
                "",
            ]
        )
    )

    done_snippet = "**CGGV:assertion_done** - GENE1 / Disease A (Definitive)"
    (cache_dir / "CGGV_assertion_done.md").write_text(done_snippet)

    (kb_dir / "Disease_A.yaml").write_text(
        f"""
name: Disease A
disease_term:
  preferred_term: Disease A
  term:
    id: MONDO:0000001
    label: Disease A
genetic:
- name: GENE1
  gene_term:
    preferred_term: GENE1
    term:
      id: hgnc:1
      label: GENE1
  evidence:
  - reference: CGGV:assertion_done
    supports: SUPPORT
    snippet: "{done_snippet}"
""".lstrip()
    )
    (kb_dir / "GENE9_Broad_Disease.yaml").write_text(
        """
name: GENE9 Broad disease
disease_term:
  preferred_term: Broad disease
  term:
    id: MONDO:0000002
    label: Broad disease
genetic:
- name: GENE9
  gene_term:
    preferred_term: GENE9
    term:
      id: hgnc:9
      label: GENE9
""".lstrip()
    )
    (kb_dir / "Specific_Disease_B.yaml").write_text(
        """
name: Specific Disease B
disease_term:
  preferred_term: Specific Disease B
  term:
    id: MONDO:0000003
    label: Disease B
""".lstrip()
    )

    summary = audit_clingen_yaml(
        kb_dir=kb_dir,
        data_dir=data_dir,
        cache_dir=cache_dir,
    )

    assert summary.positive_assertions == 4
    assert len(summary.records) == 4
    assert summary.cggv_evidence_items == 1
    assert summary.cggv_disease_files == 1
    assert summary.missing_cache_files == ()
    assert summary.snippet_not_found_in_cache == ()
    assert summary.status_counts == Counter(
        {
            "done": 1,
            "missing_genetic_entry": 1,
            "blocked_gene_specific_title": 1,
            "blocked_label_mismatch": 1,
        }
    )

    rendered = format_summary(summary, limit=2)
    assert "primary-MONDO assertion/file matches: 4" in rendered
    assert "missing_genetic_entry: 1" in rendered
    assert "remaining examples:" in rendered

    tsv = format_tsv(summary, statuses=["blocked_label_mismatch"])
    assert tsv.splitlines()[0].startswith("status\tdisorder_path\tgene_symbol")
    assert "\nblocked_label_mismatch\t" in tsv
    assert "CGGV:assertion_label_mismatch" in tsv
    assert "CGGV:assertion_done" not in tsv
