---
title: OHDSI / OMOP Clinical Data Integration (Scoping)
status: IN_PROGRESS
nih_topics:
  - NIH_HT_79_data_usage_utility_to_advance_biomedical
tags:
  - EHR
  - PHENOTYPE_ALGORITHM
  - structured-sources
  - comorbidities
  - scoping
description: >-
  Scope and roadmap for integrating OHDSI / OMOP clinical-data resources
  (ATLAS/WebAPI cohorts, the OHDSI Phenotype Library, the Athena OMOP
  vocabulary, and OHDSI network characterization) into dismech. Records which
  resource feeds which existing surface, the evidence stance, and the two schema
  inconsistencies to resolve before OHDSI-sourced comorbidity signals land.
---

# OHDSI / OMOP Clinical Data Integration

This is a **scoping log**, not a curation drive. It records the deliberate
decision of *how* OHDSI/OMOP resources map onto dismech's existing machinery, so
that later implementation steps do not have to re-derive the design. Cite this
doc (and the [design register](../docs/explanation/design-decisions.md)) when
making OHDSI-related structural choices.

## Why this is a fit, not a new abstraction

dismech already exposes **two distinct integration surfaces**, and OHDSI
resources map cleanly onto both — no new top-level construct is needed:

| dismech surface | What exists today | The OHDSI analog |
|---|---|---|
| **`association_signals`** (on `kb/comorbidities/*.yaml`) | COHD via live API (`scripts/cohd_pair_to_signal.py`), ICEES via a bulk `StructuredSource`, Disease Trajectories via the `disease-trajectories` skill | OHDSI network characterization / cohort co-occurrence statistics |
| **`definitions`** (`definition_type: PHENOTYPE_ALGORITHM`) | ATLAS cohort JSON → `scope: OMOP CDM (OHDSI)` via the `create-definitions-from-ohdsi` skill + `scripts/ohdsi_cohort_to_definition.py` | ATLAS/WebAPI cohorts pulled live; the OHDSI Phenotype Library |

Critically, OMOP concept identifiers **already flow through** the codebase as
`OMOP:<id>` CURIEs on association signals (resolved today by COHD's live API), so
the OMOP vocabulary is already the de-facto join key — it is just not yet
resolved by anything deterministic the project controls.

## Target OHDSI resources

1. **ATLAS / WebAPI** (`https://atlas-demo.ohdsi.org/WebAPI`) — cohort
   definitions as JSON. Feeds the **`definitions`** surface.
2. **OHDSI Phenotype Library** — curated, community-reviewed computable
   phenotypes. The natural source of `derivation_basis: ESTABLISHED_CRITERIA`
   phenotype algorithms (design register §11).
3. **Athena** (`athena.ohdsi.org`) — the OMOP vocabulary bulk download; the
   deterministic OMOP ↔ MONDO/SNOMED/ICD crosswalk. A candidate `StructuredSource`
   that would turn COHD's opaque live concept lookup into a pinnable,
   snippet-citable mapping layer (like ORPHA/ICEES).
4. **OHDSI network characterization** (HADES `Characterization`, public network
   studies) — condition co-occurrence and treatment pathways. Feeds the
   **`association_signals`** surface, complementary to COHD/ICEES.

## Evidence stance (two guardrails)

- **The individual-data boundary holds.** dismech ingests *disease-level*
  aggregate statistics and *phenotype logic*, never patient-level or
  cohort-level OMOP records (see [individual data](../docs/explanation/individual-data.md)
  and design register §1). OHDSI's federated design fits this: we pull
  characterization statistics and cohort definitions, not row-level data.
- **Signals are prioritization, not evidence.** OHDSI co-occurrence plays the
  same role COHD / ICEES / Disease Trajectories already play — a queue for
  manual mechanistic literature curation — not standalone mechanistic evidence
  (mirroring `projects/COMORBIDITIES.md`).
- **Definitions are computable phenotype logic, not evidence.** An ATLAS cohort
  describes *how to find cases*; it does not assert a mechanism. Its epistemic
  grounding is recorded on `derivation_basis` / `validation_status`, not by
  attaching it as EvidenceItem support.

## Two inconsistencies to resolve before OHDSI signals land

These are recorded here so the later `association_signals` work (roadmap step 3)
does not silently paper over them:

1. **`AssociationSignalSourceEnum` has no `OHDSI`/`OMOP` value.** It currently
   lists `DISEASE_TRAJECTORIES`, `COHD`, `ICEES`, `LITERATURE`, `OTHER`
   (`src/dismech/schema/dismech.yaml`). An OHDSI-sourced signal must either get a
   new `OHDSI` permissible value (preferred, for symmetry with `COHD`/`ICEES`) or
   borrow `OTHER`. **Decide before ingesting the first OHDSI signal**, not after.
2. **The design register §6 accepted-reference allowlist omits live citation
   prefixes.** §6 lists PMID/DOI/NCT/`ORPHA:`/`CGGV:`/`CGDS:`/`CIVIC_*:` but not
   `ICEES:` — already a live evidence prefix — and, prospectively, not `OMOP:`.
   If Athena (step 2) becomes a citable structured source, §6 must be updated in
   the same PR. (This gap predates OHDSI work; flagged here because step 2 forces
   the question.)

## Roadmap

- [x] **Step 0 — Scoping decision (this doc).** Record resource→surface mapping,
      evidence stance, and the two inconsistencies above. No schema/enum change.
- [x] **Step 1 — ATLAS live fetch.** `scripts/ohdsi_cohort_to_definition.py`
      gained `--webapi-url` + `--cohort-id` (and `--timeout`) to fetch a cohort
      definition live from a WebAPI (`GET {base}/cohortdefinition/{id}`),
      normalizing the WebAPI envelope's JSON-string `expression` into the same
      shape the file-parse path expects. Reuses all existing mapping logic; the
      two input modes are mutually exclusive. The `create-definitions-from-ohdsi`
      SKILL documents both modes. This directly grows `PHENOTYPE_ALGORITHM`
      coverage and lets curators pull OHDSI Phenotype Library cohorts as
      `ESTABLISHED_CRITERIA`.
- [ ] **Step 2 — Athena OMOP crosswalk `StructuredSource`.** Subclass
      `StructuredSource` (ICEES pattern): pin `data/athena-vocab/MANIFEST.yaml`,
      emit `references_cache/OMOP_<id>.md` mapping rows
      (`OMOP:id | name | domain | MONDO:x | SNOMED:y | ICD10:z`), register one CLI
      branch. Turns COHD's opaque lookup into a pinnable, snippet-citable layer
      and gives every `OMOP:<id>` on a signal a resolvable identity. Requires the
      §6 allowlist update (inconsistency 2).
- [ ] **Step 3 — OHDSI comorbidity / characterization signals.** Add
      `source: OHDSI` handling (inconsistency 1) and a script emitting
      `association_signals` from OHDSI network characterization output, mirroring
      `scripts/cohd_add_signal_to_comorbidity.py`.
- [ ] **Step 4 — OHDSI Phenotype Library sweep.** Systematically pull validated
      library cohorts for already-curated disorders as `ESTABLISHED_CRITERIA`
      definitions.

## References

- Skill: `.claude/skills/create-definitions-from-ohdsi/` (mapping guide in
  `references/model-mapping.md`).
- Script: `scripts/ohdsi_cohort_to_definition.py` (synced copy under the skill's
  `scripts/`).
- Design register: [§1 scope](../docs/explanation/design-decisions.md),
  [§6 evidence policy](../docs/explanation/design-decisions.md),
  [§11 hypothesis-based phenotype algorithms](../docs/explanation/design-decisions.md).
- Related projects: `projects/COMORBIDITIES.md`,
  `projects/MONDO_EHR_MAPPINGS.md`,
  `projects/HYPOTHESIS_BASED_PHENOTYPE_ALGORITHMS.md`.
