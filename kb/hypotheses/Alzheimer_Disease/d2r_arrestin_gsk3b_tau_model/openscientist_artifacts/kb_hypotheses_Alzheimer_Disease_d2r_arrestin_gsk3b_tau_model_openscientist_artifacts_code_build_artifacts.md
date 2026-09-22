# Artifact build provenance

This bundle is **literature-synthesis only**. No dataset, omics matrix, cohort table,
or structural file was accessed or analyzed. There were therefore no computational
analyses to trace input->method->output beyond the construction of the evidence
matrix and search log from PubMed query results.

## Method
1. `search_pubmed` (NCBI eutils, db=pubmed) queried with the terms recorded in
   `search_logs/pubmed_search_log.json` (retrieval date 2026-09-21).
2. Returned titles/abstracts were read in-context; PMIDs and one-line findings were
   transcribed by hand into `tables/evidence_matrix.csv`.
3. Verbatim abstract snippets used for KB citations were validated by the
   `update_knowledge_state` tool against stored abstracts (one title-derived snippet
   for PMID:28720530 was rejected and is flagged in the report as verify-by-curator).
4. Checksums computed with coreutils `sha256sum` (the execute_code sandbox blocked
   `hashlib`/`sys`/`csv` and could not write to the `kb/` path, so files were authored
   with the Write tool and hashed via Bash).

## Reproduce
Re-run the queries in `pubmed_search_log.json` against PubMed; counts may drift as
the index updates. Recompute checksums with:
`sha256sum search_logs/pubmed_search_log.json tables/evidence_matrix.csv env/environment.txt`

## Execution outcomes
- PubMed searches: SUCCEEDED (13 queries; 2 returned zero results - recorded as negative).
- Dataset/omics/structural analysis: SKIPPED (none available/required for a literature hypothesis-search).
- Evidence-matrix construction: SUCCEEDED (manual transcription, inspectable CSV).
