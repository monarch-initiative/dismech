# Pheno-CAM Example: Gorlin Syndrome

This walkthrough describes the structure of the Gorlin Syndrome Pheno-CAM, the most complex
worked example in the system. The actual files are:

- **Module**: `causal_models/modules/hedgehog_signaling.yaml`
- **Disease**: `causal_models/diseases/Gorlin_Syndrome.yaml`

## Overview

| Aspect | Detail |
|--------|--------|
| Disease | Gorlin Syndrome (MONDO:0007187) |
| Module | `hedgehog_signaling` — 15 activities, 15 edges |
| Hypothesis groups | 2 (PTCH1-driven ~85%, SUFU-driven ~10%) |
| Disease-local activities | 4 (CCND1, BCL2, MYCN, GLI3 A/R imbalance) |
| Phenotype routes | 8 |
| Phenotype targets | 11 (across all routes) |
| has_phenotype entries | 11 |

## Module: hedgehog_signaling

The module covers the Hedgehog signaling cascade from PTCH1 inhibition of SMO through
ciliary transport (BBSome, IFT-B, GPR161), GLI3 repressor processing (PKA, GSK3B, BTRC),
and GLI activator release (DYRK2, MAPK1, SUFU).

Sources: 4 GO-CAM models + literature:
- `gomodel:693b3c0900000716` — GPR161 export via BBSome/IFT-B
- `gomodel:693b3c0900001501` — SMO/DYRK2 → GLI3 activator
- `gomodel:693b3c0900000157` — GPR161 → GLI3 repressor
- `gomodel:693b3c0900001389` — GLI1 transcription factor activation

## Hypothesis Groups

### PTCH1-driven (~85%)

**Perturbation**: `hedgehog_signaling:ptch1_inhibition` → `absent` (loss of function)

The mutation removes PTCH1's constitutive inhibition of SMO, causing the entire downstream
cascade to activate. This hypothesis has 18 propagated states covering all arms of the pathway:

- SMO becomes `constitutively_active`
- Ciliary transport arm: BBSome/IFT-B `increased` → GPR161 `absent` (removed from cilium)
- GLI3R processing arm collapses: PKA/GSK3B/BTRC `decreased` → GLI3R `absent`
- GLI activator arm: MAPK1/DYRK2 `increased` → SUFU sequestration `decreased` → GLI1/GLI3A `increased`
- Disease-local activities: CCND1/BCL2/MYCN `increased`, GLI3 A/R imbalance `increased`

The 4 disease-local activities have explicit `driven_by` edges (cross-boundary) pointing
back to module activities — e.g., `ccnd1_upregulation` is driven by `hedgehog_signaling:gli1_activation`.

### SUFU-driven (~10%)

**Perturbations**: Both `hedgehog_signaling:sufu_sequestering_gli1` and
`hedgehog_signaling:sufu_sequestering_gli3` → `absent` (loss of function)

Only 6 propagated states — SUFU mutations bypass SMO entirely, so the ciliary transport
arm and GLI3R processing arm are **unaffected**. GLI3R still provides some repression,
partially buffering pathway activation. Notably, `gli3_ar_imbalance` is NOT propagated
under this hypothesis.

SUFU mutations carry up to 20-fold higher medulloblastoma risk despite the "milder" overall
pathway activation.

## Phenotype Routes

All 8 routes are hypothesis-agnostic — they describe tissue-specific consequences regardless
of which upstream mutation caused the perturbation.

### BCC route
`ccnd1_upregulation` + `bcl2_upregulation` → basal cell proliferation (CL:0002187, UBERON:0002097) → Basal cell carcinoma (HP:0002671)

Two `driven_by` sources on the intermediate — CCND1 drives proliferation, BCL2 confers apoptosis resistance. Evidence is on the first `driven_by` entry.

### Keratocyst route
`hedgehog_signaling:gli1_activation` → dental epithelial proliferation (CL:0000066, UBERON:0001708) → Odontogenic keratocysts (HP:0010603)

Routes directly from a module activity (GLI1), not through a disease-local activity.

### Medulloblastoma route
`mycn_upregulation` → granule cell hyperproliferation (CL:0001031, UBERON:0002037) → Medulloblastoma (HP:0002885)

MYCN is the tissue-specific proliferative driver here, distinct from the CCND1-driven BCC pathway.

### Skeletal route
`hedgehog_signaling:gli3a_activation` + `gli3_ar_imbalance` → skeletal patterning disruption (UBERON:0004765) → 3 targets: Abnormal rib morphology (HP:0000772), Abnormal vertebral morphology (HP:0003468), Macrocephaly (HP:0000256)

This route has two `driven_by` sources on the intermediate and fans out to 3 phenotype targets. Because `gli3_ar_imbalance` is only propagated under the PTCH1 hypothesis, the viz shows this route differently per hypothesis.

### Palmar pit route
`hedgehog_signaling:gli1_activation` → keratinocyte differentiation defect (CL:0000312, UBERON:0008878) → Palmar pits (HP:0010610) + Plantar pits (HP:0010612)

### Falx calcification route
`hedgehog_signaling:gli1_activation` → ectopic meningeal calcification (UBERON:0006059) → Calcification of falx cerebri (HP:0005462)

### Cardiac fibroma route
`hedgehog_signaling:gli1_activation` → cardiac mesenchymal proliferation (CL:0000057, UBERON:0000948) → Cardiac fibroma (HP:0010617)

### Ovarian fibroma route
`hedgehog_signaling:gli1_activation` → ovarian stromal proliferation (UBERON:0000992) → Ovarian fibroma (HP:0010618)

## Key Structural Patterns Illustrated

1. **Module reuse**: The `hedgehog_signaling` module is disease-agnostic — it could be imported by Pallister-Hall, Meckel Syndrome, or SHH-activated medulloblastoma with different perturbation entry points.

2. **Cross-boundary driven_by**: Disease-local activities (CCND1, BCL2, MYCN, GLI3 A/R) need explicit `driven_by` edges from module activities because no module edge connects them.

3. **Hypothesis-dependent route activation**: The skeletal route depends on `gli3_ar_imbalance`, which is only propagated under PTCH1. The visualization dynamically shows/hides this based on the selected hypothesis.

4. **Multiple driven_by sources**: The BCC intermediate has two drivers (CCND1 + BCL2); the skeletal intermediate has two drivers (GLI3A + GLI3 A/R imbalance). Evidence goes on the first `driven_by` entry.

5. **Fan-out routes**: The skeletal route fans from 1 intermediate to 3 phenotype targets; the palmar pit route fans from 1 intermediate to 2 targets.

6. **Direct module→intermediate edges**: Some routes connect directly to module activities (keratocyst, palmar pit, falx, cardiac fibroma, ovarian fibroma routes all source from `hedgehog_signaling:gli1_activation`) rather than going through disease-local activities.
