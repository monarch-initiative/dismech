# MONDO-Driven EHR Rare Disease Mapping Refactor

## Overview
Replace brittle, hand-maintained SQL `IN (...)` code lists with a reproducible MONDO-driven mapping pipeline that generates versioned SNOMED/ICD concept sets for OMOP queries.

Primary target: workflows currently represented in `~/repos/Rare-Disease-EHR-Codes` (class-level rare disease cohort extraction).

## Why This Project Exists
- Current approach hardcodes very large SNOMED and ICD lists in SQL.
- Updates are manual and error-prone.
- Provenance and mapping quality policies are not explicit in execution artifacts.
- Regeneration for new ontology/vocabulary releases is expensive.

## Deliverables
1. Deterministic generator: `MONDO -> xrefs -> OMOP concepts -> descendants -> class concept sets`.
2. Versioned outputs (CSV/TSV) with provenance metadata and mapping confidence fields.
3. SQL refactor to read generated tables instead of hardcoded lists.
4. Validation suite comparing legacy vs generated cohorts by class.
5. Maintainer docs and rerun playbook.

## Non-Goals
- Full replacement of all clinical phenotyping logic with MONDO alone.
- Building de novo disease definitions beyond code-based ascertainment.
- Rewriting all downstream analytics in this first pass.

## Proposed Architecture
- Source ontology: MONDO rare subset (`oio:inSubset = mondo#rare`), non-deprecated terms.
- Mapping layer: MONDO xrefs with explicit predicates (`exact`, related, narrow/broad handling).
- Vocabulary resolution: resolve mapped SNOMED/ICD codes to OMOP concepts.
- Expansion layer: controlled descendant expansion where policy allows.
- Classification layer: assign diseases to Orphanet/MONDO classes for class-level cohorts.
- Export layer: generate immutable dated artifacts consumed by SQL.

## Mapping Policy (Initial)
- Include: exact/equivalent mappings by default.
- Review queue: broad/narrow/related mappings.
- Exclude: obsolete/deprecated concepts.
- Track all mapping provenance fields in output:
  - `mondo_id`, `mondo_label`
  - `source_prefix`, `source_code`
  - `mapping_predicate`
  - `omop_concept_id`, `omop_vocabulary`
  - `expansion_mode`
  - `generator_version`, `run_date`

---
# STATUS

## Phase 0: Baseline and Design (0/6)
- [ ] Inventory all hardcoded SNOMED/ICD lists and owning SQL transforms
- [ ] Snapshot baseline cohort counts by disease class
- [ ] Define mapping predicate policy (exact/related/broad/narrow)
- [ ] Define descendant expansion policy (when to include descendants)
- [ ] Define artifact schema and file layout
- [ ] Write acceptance criteria for parity and drift thresholds

## Phase 1: Generator MVP (0/7)
- [ ] Build MONDO rare term loader (active terms only)
- [ ] Extract MONDO xrefs with predicates
- [ ] Resolve SNOMED/ICD to OMOP concept IDs
- [ ] Generate class-level concept sets (neurologic, neoplastic, etc.)
- [ ] Emit versioned artifacts with provenance fields
- [ ] Add unit checks for empty/duplicate/invalid concept rows
- [ ] Add CLI entrypoint for reproducible reruns

## Phase 2: SQL Integration (0/6)
- [ ] Replace one pilot class (`rare_neurologic_disease`) hardcoded SQL with artifact-driven join
- [ ] Validate pilot parity vs legacy query
- [ ] Expand to remaining classes
- [ ] Remove embedded hardcoded `IN (...)` lists
- [ ] Add guardrails for missing artifact tables
- [ ] Add migration notes for Foundry/N3C execution

## Phase 3: Validation and QA (0/7)
- [ ] Class-level cohort count comparison (legacy vs MONDO-driven)
- [ ] Delta analysis by person_id for each class
- [ ] Top gain/loss code audit sample for each class
- [ ] Rare/common incidence sanity checks
- [ ] Regression thresholds defined and enforced
- [ ] Produce validation report artifact
- [ ] Sign-off criteria documented

## Phase 4: Operations and Maintenance (0/5)
- [ ] Add scheduled regeneration workflow for ontology/vocabulary updates
- [ ] Add changelog output between runs (added/removed concepts)
- [ ] Add semantic versioning for artifact schema
- [ ] Document rollback procedure
- [ ] Publish maintainer runbook

## Phase 5: Upstream Contribution Plan (0/4)
- [ ] Split work into PR-ready branches (generator, SQL migration, docs)
- [ ] Open PR 1: artifact generator + tests
- [ ] Open PR 2: SQL migration for pilot + validation report
- [ ] Open PR 3: full rollout + operational docs

## Success Criteria
- No class-level SQL contains giant hardcoded code lists.
- Regeneration is one command and produces versioned artifacts.
- Cohort deltas are explainable and within agreed thresholds.
- Mapping provenance is queryable for every included concept.
- Update effort for new ontology release is measured in minutes, not days.

# NOTES

## 2026-03-02
- Project initialized from discussion about fragility of hardcoded SQL concept lists.
- Scope set to MONDO-driven mapping with OMOP resolution, not MONDO-only phenotyping.
- Execution strategy intentionally phased: pilot one class, validate, then scale.
