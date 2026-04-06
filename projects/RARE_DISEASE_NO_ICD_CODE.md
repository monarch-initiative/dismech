# Rare Disease ICD Coverage Gaps (MONDO)

## Overview
Catalog rare MONDO diseases that lack ICD mappings, with priority on missing ICD-11 Foundation (`icd11f` / `icd11.foundation`) mappings.

## Scope and Method
- Source ontology cache: `sqlite:obo:mondo` (`~/.data/oaklib/mondo.db`)
- Independent target vocabulary: `sqlite:obo:icd11f` (`~/.data/oaklib/icd11f.db`)
- Rare disease set: terms with `oio:inSubset = obo:mondo#rare`
- Exclusions: deprecated MONDO terms
- ICD-11 Foundation coverage check: `oio:hasDbXref` values matching `icd11.foundation:%` or `icd11f:%`
- Any-ICD coverage check: xrefs matching `icd11.foundation:%`, `icd11f:%`, `ICD10CM:%`, `ICD10WHO:%`, or `ICD9:%`
- Independent search candidates: exact normalized MONDO `label` + `hasExactSynonym` matches against ICD-11F `rdfs:label`

## Catalog Artifacts
| Artifact | Description | Rows |
|----------|-------------|------|
| `projects/RARE_DISEASE_NO_ICD_CODE/rare_terms_icd_status.csv` | Full active rare MONDO catalog with ICD coverage flags | 15,938 |
| `projects/RARE_DISEASE_NO_ICD_CODE/rare_without_icd11f.csv` | Rare MONDO terms with no ICD-11 Foundation mapping | 12,582 |
| `projects/RARE_DISEASE_NO_ICD_CODE/rare_without_any_icd.csv` | Rare MONDO terms with no ICD mapping at all | 11,092 |
| `projects/RARE_DISEASE_NO_ICD_CODE/rare_without_icd11f_but_with_other_icd.csv` | Missing ICD-11F but has ICD10/ICD9 (high-priority bridge set) | 1,490 |

## Added Columns for Review
- Metadata: `definition`, `ordo_mappings`, `orphanet_mappings`, `omim_mappings`, `omimps_mappings`
- MONDO mapping status: `has_icd11f`, `icd11f_xrefs`, `has_any_icd`, `any_icd_xrefs`
- Independent candidate search: `independent_candidate_icd11f_*`
- Manual tracking flags in review queues:
  - `search_status` (`NOT_REVIEWED`, `IN_PROGRESS`, `MATCH_CONFIRMED`, `NO_MATCH_CONFIRMED`)
  - `search_method`, `search_date`, `searched_by`
  - `selected_icd11f_id`, `selected_icd11f_label`, `search_confidence`, `search_notes`

## Regeneration
- Run: `scripts/generate_rare_disease_no_icd_catalog.py`
- The generator preserves existing manual review fields when rerun.
- In this MONDO cache snapshot, `ORDO:*` xrefs are absent; use `orphanet_mappings` as the practical ORDO-adjacent mapping field.

## Summary Counts
- Active MONDO `rare` terms analyzed: **15,938**
- With ICD-11 Foundation mapping: **3,356**
- Without ICD-11 Foundation mapping: **12,582**
- With any ICD mapping (ICD11F/ICD10/ICD9): **4,846**
- Without any ICD mapping: **11,092**

---
# STATUS

## Baseline Catalog Build (5/5) ✓
- [x] Identified active MONDO `rare` term universe
- [x] Computed ICD-11 Foundation coverage for all terms
- [x] Computed any-ICD coverage for all terms
- [x] Added `definition`, `ORDO`, and `OMIM` mapping columns
- [x] Exported full and filtered CSV catalogs with manual search-status fields under `projects/RARE_DISEASE_NO_ICD_CODE/`

## Next Pass Curation (0/3)
- [ ] Triage `rare_without_icd11f_but_with_other_icd.csv` for ICD11F bridge candidates
- [ ] Partition `rare_without_any_icd.csv` by MONDO superclasses for batch review
- [ ] Add automated refresh workflow so counts track MONDO releases

# NOTES

## 2026-02-20
- Initialized project `RARE_DISEASE_NO_ICD_CODE`.
- Built baseline catalog from local MONDO SQLite cache.
- Generated full dataset plus ICD-gap subsets for project tracking and downstream curation.
- Added independent ICD-11F candidate search (exact normalized MONDO label/synonym match against ICD11F labels).
- Added per-term review status fields so each disease can be manually searched and tracked.
- Added reproducible generator: `scripts/generate_rare_disease_no_icd_catalog.py`.
