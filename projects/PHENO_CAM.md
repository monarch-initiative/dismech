# Pheno-CAM: Phenotype Causal Activity Models

## Overview

Pheno-CAMs are structured causal models that connect disease-causing mutations through
molecular mechanisms (grounded in GO-CAMs) to clinical phenotypes (HPO). They extend
dismech's pathophysiology representation with formal molecular grounding, perturbation
state tracking, and reusable mechanistic modules.

- **Data model**: [causal_models/PHENOCAM_DATA_MODEL.md](../causal_models/PHENOCAM_DATA_MODEL.md)
- **Original design spec**: [docs/pheno-cam-design.md](../docs/pheno-cam-design.md) (outdated — superseded by data model doc)
- **Data directory**: `causal_models/` (modules + disease overlays)
- **Key scripts**: `scripts/fetch_gocam_models.py`, `scripts/visualize_phenocam.py`
- **Skill**: `.claude/skills/pheno-cam/`

## Background

The dismech `pathophysiology` entries capture causal relationships but lack formal molecular
grounding, normal-vs-perturbed state distinction, and typed causal edges. Pheno-CAMs add
these by layering disease-specific perturbation overlays on top of reusable normal-biology
modules derived from GO-CAMs.

This work supports two pivotal use cases identified at the Mar 10, 2026 CZI meeting:
1. **Variant interpretation**: predict how a variant perturbs the causal model
2. **Drug target identification**: find intervention points in the perturbation cascade

## Phases and Progress

### Phase 1: GO-CAM Programmatic Access
- [x] Build `scripts/fetch_gocam_models.py`
- [x] Test against Gorlin GO-CAM models (SMO, SUFU, GLI1, GLI2 — 6 models found)
- [x] Test against Noonan genes (PTPN11, SOS1, HRAS — 12 models found)
- [x] Verify output structure matches module YAML format

**Demo**: Automated GO-CAM model discovery and parsing from gene lists.

**Findings**:
- GO-CAM browser static index (`data.json`) has 1,862 models (1,093 human) — reliable and fast
- Model detail API (`api.geneontology.org/api/go-cam/{id}`) returns full JSON with activities and causal edges
- SPARQL and REST gene-product endpoints are unreliable (500s, timeouts)
- PTCH1 has no GO-CAM models yet (acts as inhibitor, not `enabled_by` actor)
- BRAF/RAF1/KRAS also not yet curated into GO-CAMs
- Coverage is good for: PTPN11, SOS1, HRAS, SMO, SUFU, GLI1, GLI2

### Phase 2: Data Model and Worked Examples
- [x] Finalize module YAML structure
- [x] Finalize disease perturbation YAML structure
- [x] Create Gorlin Syndrome module (`hedgehog_signaling`) + disease file
- [x] Create Noonan Syndrome module (`ras_mapk_cascade`) + disease file
- [x] Create Ehlers-Danlos Syndrome module (`collagen_v_assembly`) + disease file
- [x] Demonstrate module reuse (Noonan ↔ CFC syndrome shared RAS/MAPK module)
- [x] Data model review: resolve 7 consistency/generality issues
- [x] Interactive D3 visualization (`scripts/visualize_phenocam.py`)
- [x] Write standalone data model documentation (`causal_models/PHENOCAM_DATA_MODEL.md`)

**Created files**:
- `causal_models/modules/hedgehog_signaling.yaml` — 15 activities, 15 edges, sourced from GO-CAMs + literature
- `causal_models/modules/ras_mapk_cascade.yaml` — 10 activities, 9 edges, sourced from 5 GO-CAMs + literature
- `causal_models/modules/collagen_v_assembly.yaml` — 4 activities, 3 edges, literature sourced
- `causal_models/diseases/Gorlin_Syndrome.yaml` — 2 hypothesis groups (PTCH1/SUFU), 4 disease-local activities, 8 phenotype routes
- `causal_models/diseases/Noonan_Syndrome.yaml` — 4 hypothesis groups (PTPN11/SOS1/RAF1/LZTR1), 6 phenotype routes
- `causal_models/diseases/Cardiofaciocutaneous_Syndrome.yaml` — 4 hypothesis groups (BRAF/MEK1/MEK2/KRAS), 6 phenotype routes
- `causal_models/diseases/Ehlers-Danlos_Syndrome_COL5A1.yaml` — 1 hypothesis group, 7 phenotype routes
- `causal_models/PHENOCAM_DATA_MODEL.md` — standalone data model documentation

**Data model review** (7 issues resolved):
1. Fixed RO:0002200 direction — `has_phenotype` replaces `driven_by` on disease node
2. Fixed orphaned targets — all routes have intermediates with explicit `driven_by`
3. Eliminated dual edge representation — module topology is single source of truth
4. Migrated route-level evidence to edge-level
5. Documented propagated states as overlays (by design) with uniqueness validation
6. Formalized `perturbed_state` enum (5 values)
7. Harmonized `process` → `biological_process` field name

**Demo**: Module reuse validated — CFC and Noonan import the same `ras_mapk_cascade`
module but enter the cascade at different points (BRAF/MEK vs PTPN11/SOS1).

### Phase 3: Skill-Driven Curation
- [x] Rework `pheno-cam` skill with automated workflow
- [ ] Curate Parkinson's Disease (complex/temporal test case)
- [ ] Iterate data model based on what breaks

**Demo**: End-to-end skill-driven pheno-CAM creation for Parkinson's.

### Phase 4: Visualization and Validation
- [ ] Extend D3+Dagre renderer with new node types
- [ ] Build LinkML schema for causal models
- [ ] Add validation hook for `causal_models/`
- [ ] Add pheno-CAM tab to disorder HTML pages

**Demo**: Interactive pheno-CAM graphs on disorder pages.

### Phase 5: Pivotal Use Case Prototyping
- [ ] Variant interpretation: trace perturbation cascade from novel variant
- [ ] Drug target identification: find intervention points for perturbed nodes

**Demo**: Working variant interpretation and drug target examples.

## Worked Examples

| Disease | Phase | Why |
|---|---|---|
| Gorlin Syndrome | 2 | Two hypothesis groups (PTCH1/SUFU), Hh pathway, disease-local activities, cross-boundary edges |
| Noonan Syndrome | 2 | RASopathy, 4 genes converging on ERK, cardiac + developmental phenotypes |
| CFC Syndrome | 2 | Module reuse demo — shares ras_mapk_cascade with Noonan, different entry points |
| EDS (COL5A1) | 2 | Simplest model (1 hypothesis, hub-and-spoke routes), structural protein pathway |
| Parkinson's Disease | 3 | Multiple hypotheses, progressive, rich KB entry, module reuse |

## Key Decisions

- **Separate data layer** (`causal_models/`) rather than modifying `kb/disorders/` —
  avoids disrupting existing pipeline, allows aggressive iteration
- **Shared module library** for normal biology, disease-specific overlays for perturbation
- **Fully automated GO-CAM integration** — no human review of intermediate steps
- **Controlled vocabulary** for perturbation states with ontology mappings where available
- **Migration path**: eventual `causal_model:` field in Disease schema
