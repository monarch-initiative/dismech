# Diabetes mellitus: grouping refactor + pathophysiology migration map

**Status:** Done. The umbrella Disease entry `kb/disorders/Diabetes_Mellitus.yaml`
has been retired. Diabetes mellitus is now the `Diabetes_Mellitus` grouping
(holding `MONDO:0005015` as an exactMatch), the `diabetic_vascular_complications`
module, and the member entries: type 1, type 2, type 5 and gestational diabetes,
plus a nested `Monogenic_Diabetes` grouping over maturity-onset diabetes of the
young, permanent and transient neonatal diabetes, and the syndromic monogenic
forms. The sections below record how it got there.

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

## Decision: A2 (taken)

The shared cascade was promoted to the mechanism module
`kb/modules/diabetic_vascular_complications.yaml` (5 nodes: Chronic Hyperglycemia
→ Hyperglycemia-Induced Oxidative Stress and AGE-RAGE Activation → **Endothelial
Dysfunction and Vascular Inflammation** [central_effector / key conformance
target] → Diabetic Micro- and Macrovascular Injury → Diabetic End-Organ
Complications; SGLT2-inhibitor drug-target on the trigger). The three type
entries now declare `conforms_to`:
- **Type I Diabetes** — existing `Hyperglycemia` node → `#Chronic Hyperglycemia`;
  existing `Chronic Complications` node → `#Diabetic End-Organ Complications`.
- **Type 2 Diabetes Mellitus** — added a `Chronic Hyperglycemia` pathophysiology
  node → `#Chronic Hyperglycemia` (wired downstream to its existing retinopathy /
  neuropathy phenotypes).
- **Malnutrition-Related Diabetes Mellitus** — added a `Chronic hyperglycemia and
  vascular complication risk` node → `#Chronic Hyperglycemia`.

End-state target: "diabetes mellitus" = Grouping + module + per-type entries.
Note on MONDO:0005015: because the umbrella Disease entry is deliberately
retained (for its `has_subtypes` catalog and disease-level framing) and keeps
`MONDO:0005015` as its `disease_term`, the Grouping does not exclusively "own"
that class — it maps to it via `skos:closeMatch` rather than `exactMatch`, so a
single MONDO class is not claimed by two entities at once. Fully transferring
ownership to the Grouping would require dropping the umbrella Disease's
`disease_term`, which is deferred with the rest of the umbrella slimming below.

## Remaining: umbrella slimming (`Diabetes_Mellitus.yaml`)

The blended 30-node pathophysiology graph in the umbrella Disease is now redundant
with the module + per-type entries and should be retired. **Wrinkle discovered
during A2:** the umbrella is NOT purely redundant — it is the only home for the
`has_subtypes` catalog (LADA, gestational, MODY 1–14, neonatal/transient/permanent,
RCAD, MIDD, lipoatrophic, DKA) that have **no standalone `Disease` entries** and
are **not** members of the 3-member Grouping. So the umbrella cannot simply be
deleted without losing that subtype enumeration.

Umbrella end-state — **steps 1–3 DONE** (blended `pathophysiology:` retired and
replaced with the single conforming node); **steps 4–5 DEFERRED**:
1. ✅ **Remove** the type-specific pathophysiology nodes already covered by the
   standalone entries (autoimmune arm → T1D; insulin-resistance arm → T2D;
   pancreatogenic arm → T5) and the shared-cascade nodes (now the module).
2. ✅ **Replace** the mechanism graph with a single pathophysiology node that
   `conforms_to: "diabetic_vascular_complications#Chronic Hyperglycemia"` (chosen
   over the central-effector node to match the node's glucose-homeostasis process
   and chronic-hyperglycemia evidence), so the umbrella still points at the shared
   mechanism without re-deriving it.
3. ✅ **Keep** `has_subtypes` (the subtype catalog), the case-definition and USPSTF
   screening `definitions`, and disease-level framing.
4. ✅ **Reallocate** the blended sections. Type-specific rows already covered
   by a per-type entry were deleted (T1/T2 susceptibility genes INS, PTPN22,
   IL2RA, CTLA4, TCF7L2, PPARG, KCNJ11, SLC30A8; obesity, hyperinsulinaemia,
   impaired glucose tolerance, DKA; metformin, GLP-1 RA, SGLT2i, tirzepatide,
   teplizumab; the four type 2 metabolic models and BioProject datasets; the
   type-specific exposures; two duplicate progression stages). Rows with no
   per-type counterpart were moved: HLA-DQA1/DQB1 (as HGNC-bound records beside
   the type 1 entry's DQ2/DQ8 haplotype rows), the teplizumab prevention trial
   and the UVA/Padova simulator to type 1; the tirzepatide and empagliflozin
   trials and the prediabetes stage to type 2; the pregnancy-onset stage to
   gestational diabetes. LADA and SAID moved to the type 1 entry's
   `has_subtypes`. What stays is cross-cutting: complication phenotypes, the
   osmotic symptoms, HbA1c and glucose, insulin, monitoring, diet and exercise,
   differential diagnoses, case definitions, drug- and checkpoint-inhibitor
   exposures, and the share-of-diabetes prevalence rows, plus the monogenic
   catalogue.
5. ✅ **Retire the umbrella.** The monogenic catalogue became three entries,
   each one genetically heterogeneous disease with a subtype per gene, the
   pattern used for other locus-heterogeneous Mendelian diseases and the way
   MONDO and GeneReviews divide them: `Maturity-Onset_Diabetes_of_the_Young`
   (MODY 1-4, 6, 8, 10, 12, 13 and renal cysts and diabetes), with KLF11, PAX4,
   BLK and APPL1 as DISPUTED genetic rows rather than subtypes;
   `Permanent_Neonatal_Diabetes_Mellitus` (PNDM1-4, PTF1A, EIF2B1, and a pointer
   to NDM-CH); and `Transient_Neonatal_Diabetes_Mellitus` (6q24 TNDM1, TNDM2,
   TNDM3). The single monogenic beta-cell node was split into mechanism nodes
   that state each gene's lost molecular function. Syndromic genes already
   curated in their own entries (WFS1, CISD2, EIF2AK3, SLC19A2, GLIS3) were
   not duplicated; heterozygous RFX6 stays a MODY gene, while biallelic RFX6 is
   Mitchell-Riley syndrome. The remaining cross-cutting rows moved to the per-type
   entries, except the disease-level case definition and a generic
   environmental-determinants row, which only framed "diabetes in general" and
   are carried by the grouping's description. Maternally-inherited diabetes and
   deafness and lipoatrophic diabetes, which had no curated content, are in the
   stub queue. Diabetic ketoacidosis, which MONDO places under diabetes
   mellitus, is curated as a phenotype of the type entries. The two comorbidity
   entries that anchored on the umbrella keep `MONDO:0005015` as their claim,
   because their sources do not stratify by type, and no longer carry a slug.
