# Artifact Bundle — ADNP NMD-Escaping Truncation Branch

Supports the hypothesis-search report at `../../../../final_report.md`.
Search/analysis date: 2026-09-07.

## Contents
- `MANIFEST.yaml` — schema, inputs/outputs, status flags, replay notes, key result.
- `code/adnp_clinvar_nmd_analysis.py` — reproducible analysis (ClinVar + Ensembl → NMD-escape mapping).
- `tables/summary_stats.json` — aggregate result (303 P/LP; 150/165 truncating escape NMD = 90.9%).
- `tables/class_counts.csv` — variant class distribution.
- `tables/nmd_sensitive_early_variants.csv` — the 15 NMD-sensitive (early-exon) truncating variants.
- `tables/gnomad_adnp_constraint.json` — gnomAD constraint (pLI=1.0, LOEUF=0.11).
- `environment/packages.txt` — package versions.
- `logs/clinvar_search_log.txt`, `logs/iter3_4_search_log.txt` — sanitized query/search logs incl. negatives.

## Execution outcomes
- ClinVar NMD-escape analysis: **succeeded**.
- gnomAD constraint lookup: **succeeded**.
- ClinGen dosage/validity retrieval: **failed** (API 404; page is HTML SPA) — logged, unverified, no fallback claimed.

## Not produced / external
- Figure `figures/truncating_variant_positions.png`: generated in code sandbox (/tmp, separate container) and NOT persisted to job FS; regenerate by running the code locally.
- Input checksums: not computed (hashlib unavailable in sandbox); inputs regenerable from pinned queries.
- No patient-level or controlled-access data were downloaded or bundled.

## Key computed claim → provenance
"~91% of pathogenic ADNP truncating variants escape NMD"
  → input: ClinVar query (see MANIFEST inputs.clinvar_adnp_plp) + Ensembl ENST00000621696
  → method: code/adnp_clinvar_nmd_analysis.py
  → output: tables/summary_stats.json (truncating_nmd_escape_pct: 90.9)
