# Diabetes mellitus: grouping refactor + pathophysiology migration map

**Status:** proposed (grouping file landed; umbrella not yet edited — awaiting decision on the shared-cascade question below)

## Problem

`kb/disorders/Diabetes_Mellitus.yaml` (3,367 lines) is an umbrella Disease that
carries (a) a large `has_subtypes` enumeration (T1D, T2D, LADA, gestational,
monogenic/MODY 1–14, neonatal, RCAD, MIDD, type 5, DKA) **and** (b) its own full
pathophysiology graph that *blends* autoimmune (type 1) and insulin-resistance
(type 2) mechanisms in one causal chain. Meanwhile the two major types already
exist as coherent standalone entries (`Type_I_Diabetes.yaml`,
`Type_2_Diabetes_Mellitus.yaml`), plus a `Malnutrition-related_Diabetes_Mellitus.yaml`
stub (type 5). This is redundancy + a mechanistically incoherent graph, not a
single source of truth.

Two consistency bugs found alongside:
- `Type_2_Diabetes_Mellitus.yaml` does **not** list `Diabetes Mellitus` as a
  parent, whereas T1D and type 5 do. → fix.
- The type-5 stub *does* carry a `Hyperglycemia` term but declares no
  `frequency:` band, so it shows `UNKNOWN` (not `NOT_SATISFIED`) in the grouping
  audit — an advisory artifact, not a missing term. Adding a sourced `frequency:`
  would turn it green. Low priority.

## Decision taken

Add `kb/groupings/Diabetes_Mellitus.yaml` (Grouping class) unioning the three
distinct standalone Disease entries — `grouping_basis: [SHARED_PHENOTYPE,
CLINICAL_CONVENTION]`, one `NECESSARY` criterion (chronic hyperglycemia,
HP:0003074), MONDO mapping to `MONDO:0005015`. Validated (schema + terms + audit).

## Umbrella pathophysiology node migration map (30 nodes)

Legend: **KEEP** = shared cross-subtype cascade, stays in the umbrella (or moves
to a module — see open question); **T1/T2/T5** = type-specific, belongs in that
entry; ✓ = destination already covers it (delete from umbrella); ➕ = destination
does not yet cover it (migrate content, don't just delete).

### Type 1 (autoimmune) → `Type_I_Diabetes.yaml`
| Umbrella node | Destination node | Status |
|---|---|---|
| Autoimmune diabetes genetic susceptibility | Genetic Susceptibility | ✓ |
| Interferon-driven beta-cell inflammatory priming | Interferon-Driven Beta Cell Response | ✓ |
| Autoimmune pancreatic beta-cell destruction | Autoimmune Destruction of Beta Cells | ✓ |
| Absolute insulin deficiency | Insulin Deficiency | ✓ |
| Increased lipolysis and ketogenesis | Increased Lipolysis + Diabetic Ketoacidosis (DKA) | ✓ |

### Type 2 (insulin resistance) → `Type_2_Diabetes_Mellitus.yaml`
| Umbrella node | Destination node | Status |
|---|---|---|
| Peripheral insulin resistance in insulin-sensitive tissues | Insulin Resistance | ✓ |
| Pancreatic beta-cell secretory dysfunction | Beta Cell Dysfunction | ✓ |
| Increased hepatic glucose output | Hepatic Glucose Overproduction | ✓ |
| Incretin axis dysfunction | Incretin Axis Dysfunction | ✓ |
| Mitochondrial dysfunction and oxidative stress in metabolic tissues | Mitochondrial Dysfunction and Oxidative Stress | ✓ |
| Early pancreatic beta-cell injury | Beta Cell Dysfunction (merge detail) | ➕ review |
| Prediabetic metabolic stress | (no node) | ➕ migrate |
| Reduced peripheral glucose disposal | Insulin Resistance (merge detail) | ➕ review |
| Relative insulin deficiency | (no node) | ➕ migrate |

### Type 5 (malnutrition / pancreatogenic) → `Malnutrition-related_Diabetes_Mellitus.yaml`
| Umbrella node | Destination node | Status |
|---|---|---|
| Pancreatogenic endocrine hormone loss (T5DM/fibro-inflammatory overlap) | (stub — enrich) | ➕ migrate |
| Pancreatogenic exocrine pancreatic insufficiency (T5DM/fibro-inflammatory overlap) | (stub — enrich) | ➕ migrate |

### Shared cross-subtype cascade — **KEEP** (chronic hyperglycemia → complications)
Chronic hyperglycemia · Hyperglycemia-induced oxidative stress ·
Hyperglycemia-driven AGE-RAGE pathway activation · Endothelial dysfunction ·
Vascular inflammation · Renal / Retinal / Neural microvascular injury ·
Diabetic renal hemodynamic dysregulation · Diabetic glomerular injury ·
Diabetic tubular injury · Diabetic renal inflammation · Diabetic renal fibrosis ·
Diabetic kidney disease · Macrovascular atherosclerotic disease ·
Arterial thrombosis and ischemia. *(16 nodes.)* Only the umbrella elaborates this
fully; T1D has a single `Chronic Complications` node and T2D has none.

### Other umbrella sections needing allocation (not line-mapped yet)
`phenotypes`, `biochemical`, `genetic`, `treatments`, `differential_diagnoses`,
`clinical_trials`, `datasets`, `computational_models`, `environmental` also blend
types. Cross-cutting items (diabetic complications, insulin, metformin, HbA1c)
stay with the shared cascade; type-specific items (islet autoantibodies vs.
metformin/GLP-1, HLA vs. TCF7L2) follow their type. To be detailed in the edit PR.

## OPEN QUESTION — where does the shared cascade live?

- **A1 (incremental, lower risk):** slim the `Diabetes_Mellitus.yaml` **Disease**
  down to the shared cascade + `has_subtypes` enumeration + disease-level framing
  (case definition, USPSTF screening algorithm), delete the type-specific nodes
  that are already covered, migrate the ➕ ones. Concept "diabetes mellitus" is
  then represented by *both* the residual Disease and the Grouping (both touch
  MONDO:0005015) — mild double-representation.
- **A2 (cleaner end-state, more work):** promote the shared cascade to a new
  mechanism module `diabetic_vascular_complications`; T1D/T2D/T5 each add a
  `conforms_to` node; retire the umbrella Disease's mechanism graph. "Diabetes
  mellitus" = Grouping (owns MONDO:0005015) + module + per-type entries. Needs the
  `create-module` skill and touches all three type entries.

Recommendation: **A2** long-term (the complication cascade is a genuine conserved
final-common-pathway and is exactly what modules are for), but **A1** is a safe
first step that can land now and be followed by A2. Decision needed before editing
the big file.
