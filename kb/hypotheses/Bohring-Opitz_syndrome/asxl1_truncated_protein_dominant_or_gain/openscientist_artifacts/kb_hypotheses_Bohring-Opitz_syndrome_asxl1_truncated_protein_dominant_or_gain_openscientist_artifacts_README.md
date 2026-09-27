# Artifact bundle — BOS ASXL1 truncated-protein dominant/gain-of-function hypothesis

Hypothesis `asxl1_truncated_protein_dominant_or_gain` (KB status: ALTERNATIVE) for
**Bohring-Opitz syndrome**. Run date 2026-09-07. Verdict: **partially supported**.

## Contents
- `MANIFEST.yaml` — schema, status flags, data sources, analysis provenance, checksums, replay.
- `code/gnomad_query.graphql` — exact gnomAD GraphQL queries (constraint + transcript variants).
- `code/gnomad_asxl1_analysis.py` — analysis script (input -> method -> output).
- `data/gnomad_asxl1_constraint.csv` — ASXL1 LoF constraint (pLI, LOEUF).
- `data/gnomad_asxl1_plof_region_summary.csv` — pLoF density by protein region.
- `data/gnomad_asxl1_plof_top_hotspot_variants.csv` — top-AC hotspot variants vs CHIP/AML drivers.
- `data/evidence_matrix.csv` — literature + computational evidence matrix.
- `logs/pubmed_search_log.md` — all PubMed queries incl. negative searches.
- `logs/gnomad_execution_log.md` — sanitized execution trace incl. failed attempts.
- `env/environment.txt` — package versions and external services.

## One-line result
gnomAD v4 shows ASXL1 is NOT LoF-constrained (pLI≈0, LOEUF≈0.90) and its population truncation
hotspot (aa580-1000, led by p.Gly646fs = the canonical CHIP/AML driver = the recurrent germline BOS
allele) is a clonal-hematopoiesis signature, supporting a clonal-fitness gain-of-function for
NMD-escaping truncated ASXL1 — consistent with, but not proof of, the seed hypothesis in germline BOS.

## Key caveat
No accessed source directly demonstrates a stable endogenous truncated ASXL1 PROTEIN in germline BOS
patient tissue, nor formally excludes concurrent haploinsufficiency. See final_report.md (repo root).
