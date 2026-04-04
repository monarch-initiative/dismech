# G2P

## Scope

This project tracks how Gene2Phenotype (G2P) disease rows map onto dismech's
disease-centric knowledge model, with the goal of turning comparison output
into curation triage rather than a one-off research exercise.

## Canonical Locations

- Project note: [`docs/research/g2p_database_alignment.md`](../docs/research/g2p_database_alignment.md)
- Full-release audit snapshot:
  [`docs/research/g2p_all_genes_audit_2026_03_28.md`](../docs/research/g2p_all_genes_audit_2026_03_28.md)
- Row-level triage TSV:
  [`docs/research/g2p_all_genes_row_triage_2026_03_28.tsv`](../docs/research/g2p_all_genes_row_triage_2026_03_28.tsv)
- Gene-level summary TSV:
  [`docs/research/g2p_all_genes_gene_summary_2026_03_28.tsv`](../docs/research/g2p_all_genes_gene_summary_2026_03_28.tsv)

## Code Organization

Comparison code now lives under `src/dismech/compare/` instead of the package
top level:

- `src/dismech/compare/d2p.py`: disease-to-phenotype comparison flow
- `src/dismech/compare/g2p.py`: G2P-to-dismech comparison flow
- `src/dismech/compare/g2p_audit.py`: compatibility wrapper for the initial G2P
  audit CLI
- `src/dismech/compare/support.py`: shared comparison helpers

This keeps the G2P work aligned with the earlier D2P comparison architecture
instead of adding another top-level framework.

## Practical Commands

```bash
just g2p-compare PTEN
just g2p-compare-all PTEN FLNB PIK3CA FGFR2
just g2p-compare-release
just g2p-compare-release-triage
uv run python -m dismech.compare.g2p compare PTEN --format json
```

## Current Focus

- make row-status output actionable for curation
- identify genes where dismech has rooted disease coverage vs embedded-only
  coverage
- separate disease-identity alignment, PMID overlap, and mechanism-model
  alignment in the audit output
