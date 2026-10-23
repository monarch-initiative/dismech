# Environment record

## Nature of computation in this run
- This hypothesis-search was a **literature-synthesis run**. No omics dataset, SPARQL endpoint, or
  scientific-compute pipeline was executed. No numerical/statistical analysis was performed on primary data.
- The only executed operations were: (a) MCP `search_pubmed` queries, and (b) shell file-creation and
  SHA-256 checksumming to assemble this artifact bundle.
- Therefore there are **no model weights, random seeds, or solver parameters** to record for a data analysis.

## Tools used
- MCP `search_pubmed` — NCBI E-utilities backend, accessed 2026-10-18.
- MCP `update_knowledge_state`, `save_iteration_summary`, `set_status`, `set_job_title`, `set_consensus_answer`.
- Shell (`bash`), `sha256sum`/`shasum`, `python3` (stdlib only) for checksums/MANIFEST assembly.

## Explicitly NOT run (would be needed for a computational test)
- GEO download + re-analysis of the PMID:39578560 snRNA/snATAC atlas (to quantify mTOR-pathway and
  RICTOR/RPTOR expression and chromatin accessibility by cell type and age). Skipped: accession not
  retrieved; n=8 underpowered; outside the scope/time of a 5-iteration literature run.
- GWAS Catalog programmatic enumeration of age-at-natural-menopause loci to formally test mTOR-gene
  enrichment vs DDR. Skipped.
- ClinicalTrials.gov API pull of NCT05836025 status/results. Skipped; cited from the seed YAML.

## Reproducibility note
Re-issuing the queries in config/queries.yaml against live PubMed may return additional newer records
than captured on 2026-10-18; the PMIDs cited here are stable identifiers.
