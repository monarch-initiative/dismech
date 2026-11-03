# OpenScientist artifact bundle — ovarian_mtor_follicle_reserve_aging

Literature-synthesis hypothesis search (no primary omics accessed). See `MANIFEST.yaml` for schema,
status flags, checksums, and replay instructions.

- `MANIFEST.yaml` — canonical manifest (schema 1.0), checksummed inputs/outputs, provenance of computed claims.
- `logs/pubmed_search_log.md` — all 18 PubMed queries, record counts, used PMIDs, and recorded negative searches.
- `config/queries.yaml` — verbatim query strings (reproducibility).
- `tables/evidence_matrix.csv` — one row per evidence item (stance, claim, finding, limitations).
- `tables/data_source_inventory.csv` — every data source with access status and relevance.
- `env/environment.md` — tools used; explicit list of analyses NOT run and why.

The full report is at the job root: `final_report.md` (hashed in MANIFEST).

Key verdict: **partially supported** — mechanistically strong in model systems for the follicle-quantity
(mTORC1→activation→reserve depletion) axis; human evidence indirect; the "sets menopause timing" claim is
out-competed by DNA-damage-response genetics; mTORC2/RICTOR directionality is an open tension.
