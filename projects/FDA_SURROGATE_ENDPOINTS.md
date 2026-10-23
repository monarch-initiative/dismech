---
title: FDA Surrogate Endpoints Project
status: PLANNED
description: >-
  Connect each row of FDA's Surrogate Endpoint Table to the dismech biomarker
  and pathograph node it reads out, so that for any disease the KB can say
  which mechanistic branches an approved surrogate measures and which it does not.
tags: [REGULATORY, BIOMARKERS, PATHOGRAPH, CROSS_CUTTING]
diseases:
- Fabry_Disease
- Achondroplasia
- Asthma
- Beta_Thalassemia
- Chagas_Disease
- Chronic_Kidney_Disease
- Chronic_Obstructive_Pulmonary_Disease
- Cushings_Syndrome
- Cystic_Fibrosis
- Duchenne_Muscular_Dystrophy
- Gout
- Idiopathic_Pulmonary_Fibrosis
- Methylmalonic_Acidemia
- N-Acetylglutamate_Synthase_Deficiency
- Onchocerciasis
- Osteoporosis
- Phenylketonuria
- Polycystic_Kidney_Disease
- Primary_Biliary_Cholangitis
- Propionic_Acidemia
- Prostate_Adenocarcinoma
- Sickle_Cell_Disease
- Sitosterolemia
- Systemic_Sclerosis
- Type_2_Diabetes_Mellitus
- Type_I_Diabetes
- X-Linked_Hypophosphatemia
---

# FDA Surrogate Endpoints Project

## Overview

FDA publishes a table of the surrogate endpoints that have been the basis of a
drug or biologic approval. dismech holds a row-level transcription of it in
`kb/surrogate_endpoints/fda_surrogate_endpoints.yaml` (225 rows, FDA content
current as of 2026-04-29), imported by
`scripts/import_fda_surrogate_endpoints.py` and tracked in issue #2495.

A row says that FDA accepted a measurement for a disease, in a population, for a
drug mechanism, at a stated validation level. It does not say what the
measurement is a measurement *of*. The dismech pathograph can answer that: a
`Biochemical` marker's `readouts[]` names the pathophysiology node it reports
on, and `readouts[].regulatory_endpoint_refs` points that readout at the FDA
row. Once that link exists, the graph shows which downstream outcomes the
surrogate sits upstream of, and which sibling branches it never sees.

The aim is to make that link for every disease-specific row that has a dismech
entry, and to make the coverage gaps readable.

## Worked example: `Fabry_Disease`

FDA lists one Fabry marker across three rows: clearance of GL-3 (Gb3) inclusions
in biopsied renal peritubular capillaries.

| Row | Population | Approval | Drug mechanism | Validation level |
|---|---|---|---|---|
| `FDA-SE-adult-noncancer-024` | Adults | Traditional | Enzyme replacement therapy | Validated |
| `FDA-SE-pediatric-noncancer-019` | Age 2 and older | Traditional | Enzyme replacement therapy | Validated |
| `FDA-SE-adult-noncancer-025` | Amenable GLA variant | Accelerated | Pharmacological chaperone | Reasonably likely |

All three are attached to the `Renal Globotriaosylceramide Inclusions` marker,
whose readout targets `Renal glycosphingolipid storage and podocyte injury`.
That node leads to proteinuria, nephrotic syndrome and chronic kidney disease.
The other five branches of `Tissue-specific glycosphingolipid storage` (cardiac,
vascular endothelial, small-fiber/autonomic, ocular, cutaneous) carry no
FDA-recognized marker. The entry already records this for the heart: its
cardiomyocyte autophagy node is described as "not measured by the renal GL-3
surrogate". Plasma lyso-Gb3 is curated as a monitoring readout and is not on
the FDA table.

The same reading should be possible for every disease below.

## Current state

Counts from the committed table on 2026-10-10.

| `mapping_status` | Rows | Meaning |
|---|---|---|
| `EXACT_DISMECH_MATCH` | 32 | Disease label matches a dismech entry |
| `CURATED_DISMECH_MAPPING` | 12 | Matched by a hand-written rule in the import script |
| `CANDIDATE_DISMECH_MAPPING` | 1 | Proposed, not confirmed |
| `NEEDS_CURATION` | 133 | No mapping yet |
| `NOT_DISEASE_SPECIFIC` | 47 | Antiseptics, vaccines across pathogens, and similar |

The 45 mapped rows point at 27 disorder entries. Of the FDA row IDs, 24 are
cited by a `regulatory_endpoint_refs` somewhere in `kb/`, across 15 files.

**Mapped but not wired.** These entries have FDA rows mapped to them and no
`regulatory_endpoint_refs` citing those rows:

- `Achondroplasia` (1 row)
- `Asthma` (2)
- `Chagas_Disease` (1)
- `Cushings_Syndrome` (1)
- `Methylmalonic_Acidemia` (2)
- `N-Acetylglutamate_Synthase_Deficiency` (2)
- `Onchocerciasis` (1)
- `Osteoporosis` (3)
- `Propionic_Acidemia` (2)
- `Type_2_Diabetes_Mellitus` (2)
- `Type_I_Diabetes` (2)
- `X-Linked_Hypophosphatemia` (2)

**Unmapped rows whose disease has a likely entry.** Spot-checked by file name;
each needs a curator to confirm the entity is the same before mapping:
Type 1 Gaucher disease (`Gaucher_Disease` has-subtype), alkaptonuria,
lysosomal acid lipase deficiency (`Wolman_Disease` covers the infantile form
only), cystinuria, primary hyperoxaluria type 1, arginase 1 deficiency,
cerebrotendinous xanthomatosis, familial chylomicronemia syndrome,
hypercholesterolemia, hepatitis B, C and D, influenza, pertussis, Alzheimer's
disease, Cushing's disease.

The largest unmapped groups (17 hematological-malignancy rows, 9 solid-tumor
rows, 8 nonmalignant-hematology rows) are FDA umbrella labels and will usually
map to several entries or to none. Treat them last.

## Work plan

### Tranche 1: wire the mapped-but-unwired entries

For each entry in the list above:

1. Find or add the `Biochemical` marker the FDA endpoint measures.
2. Give it a `readouts[]` item targeting the pathophysiology node the marker
   reports on, with `regulatory_endpoint_refs` naming the FDA row IDs.
3. Cite evidence for the readout link itself. The FDA row is a regulatory
   record, not evidence that the marker reads out that node.
4. Where no marker can honestly be placed on a node (a composite clinical
   score, a functional test), say so in the entry's `notes` rather than forcing
   a readout.

### Tranche 2: confirm the mapping candidates

Work through the unmapped-with-likely-entry list. A confirmed match goes into
`MANUAL_MAPPINGS` in `scripts/import_fda_surrogate_endpoints.py` and the table
is regenerated. Never hand-edit `fda_surrogate_endpoints.yaml`. A row whose
population is narrower than the entry (an amenable-variant population, a
subtype) should map to the subtype where one exists.

### Tranche 3: branch-coverage report

Write a report-only script (in the style of `just list-disconnected-phenotypes`)
that, for each wired FDA row, walks the pathograph from the readout's target
node and lists:

- the downstream phenotypes the surrogate sits upstream of;
- the sibling branches from the nearest shared upstream node that the surrogate
  does not reach.

Fabry is the reference output. The report must not be a gate: a surrogate that
covers one branch is a property of the regulatory record, not a curation defect.

### Tranche 4: surrogacy evidence

For rows marked `REASONABLY_LIKELY_SURROGATE_ENDPOINT` (29 rows), the open
question is whether the surrogate-to-outcome link has since been confirmed.
`just research-surrogacy <provider> <disease> "<surrogate>" "<outcome>"` exists
for this. Results are leads for the entry's evidence, not KB content.

## Open questions

- **No slot for "this surrogate does not measure this branch".** Today the Fabry
  entry says it in a node `description`. If the tranche 3 report proves useful,
  decide whether it stays derived (preferred: it is computable from the graph)
  or needs a field. Consult `docs/explanation/design-decisions.md` and the
  `extend-schema` skill before proposing one.
- **LOINC.** `projects/LOINC_DIAGNOSTICS.md` tranche N puts the LOINC code on
  the same `Biochemical` marker this project wires. Coordinate so the two
  tranches touch each marker once.
- **Refresh cadence.** The table is a dated snapshot. A re-import should report
  rows added, removed or changed in validation level, since an upgrade from
  accelerated to traditional approval changes what an entry can say.

## Commands

```bash
just validate-surrogate-endpoints        # schema-validate the table
just research-surrogacy openscientist Fabry_Disease \
  "renal peritubular capillary GL-3 clearance" "chronic kidney disease"
just validate-disorders kb/disorders/<Entry>.yaml
just gen-project-pages                   # render this page
```
