---
provider: openai
model: gpt-5.4
generated_at: "2026-04-13T05:44:53Z"
disease_name: Mycosis Fungoides
---

# Mycosis Fungoides Deep Research

## Modeling choices

This curation follows the cancer-modeling guidance from dismech issue #1198.
The dismech page is the disease-level mechanism graph for `Mycosis_Fungoides`,
not a page-per-subclass decomposition. I kept the disease anchor MONDO-first at
`MONDO:0009691` and treated WHO-EORTC-recognized variants as flat subtype
facets rather than separate disease pages. That means folliculotropic mycosis
fungoides, localized pagetoid reticulosis, and granulomatous slack skin are
represented as subtype values under one MF entry. Large-cell transformation was
modeled as progression biology within MF rather than as a separate disease file.

NCIT was used where it adds oncology-specific value under the current schema,
especially for histopathology and treatment terms. I did not add disease-level
or subtype-level NCIT mappings because the present schema exposes MONDO disease
mapping slots but not a parallel `ncit_mappings` structure for disease/subtype
anchors.

## Disease identity and subtype structure

Recent reviews consistently describe MF as the most common cutaneous T-cell
lymphoma and as a disease centered on malignant T-cell infiltration of skin
(PMID:40721285, PMID:37124514). Clinical staging remains the core disease axis:
patch, plaque, and tumor stages are explicit in recent reviews (PMID:40721285,
PMID:34541796). WHO-EORTC-recognized clinicopathologic variants include
folliculotropic MF, pagetoid reticulosis, and granulomatous slack skin
(PMID:37124514, PMID:29726638, PMID:35485962, PMID:11411914).

The resulting subtype model in YAML is intentionally flat:

- `classification: clinicopathologic_variant`
- `classification: skin_stage`

This preserves clinically meaningful subtype structure without implying that
every ontology subclass needs its own dismech page.

## Histopathology and diagnosis

The strongest disease-level histopathology signal available in recent MF review
abstracts is the characteristic epidermotropic infiltrate of small-to-medium
lymphocytes, especially in early patch-stage disease, alongside the need for
repeated biopsies and careful clinicopathologic correlation (PMID:40721285,
PMID:34541796). Folliculotropism is clinically important because it is tied to
recognized variant structure and poorer prognosis in infiltrated head/neck
plaques and tumors (PMID:37124514). Diagnostic workflow is anchored to skin
biopsy with histopathology and immunohistochemistry (PMID:37124514).

## Pathophysiology

I kept the mechanistic graph atomic and avoided bundled nodes. The main disease
mechanisms supported by the literature are:

1. Cutaneous homing and accumulation of malignant T-cell clones in skin
   (PMID:40721285).
2. Deregulated TCR/PLCG1 signaling as a core driver axis (PMID:33923722).
3. Recurrent JAK/STAT activation supported both by integrative review and
   contemporary MF genomics (PMID:33923722, PMID:41008827).
4. TNFRSF1B/TNFR2-driven non-canonical NF-kappaB signaling as a recurrent
   human genomic mechanism (PMID:26258847).
5. Cancer-associated fibroblast and collagen-remodeling programs during early
   progression (PMID:40163757).
6. Interleukin-4-associated transcriptional activation during patch-to-plaque
   evolution (PMID:40163757).
7. M2 macrophage enrichment and exhaustion-linked immune suppression in
   progressive lesions (PMID:40163757).
8. RAS-signaling acquisition in large-cell transformation, modeled as MF
   progression rather than a new disease anchor (PMID:34771672).

## Genetics

The genetics section emphasizes lesions that help explain MF mechanism or
progression:

- `TNFRSF1B` recurrent mutation/gain and TNFR2 signaling (PMID:26258847)
- `CTLA4-CD28` fusion (PMID:26258847)
- recurrent `FAT1`, `KMT2D`, `TP53`, and `JAK3` alterations in a 2025 national
  genomics analysis (PMID:41008827)
- transformation-associated `RAS` mutations in aggressive large-cell
  transformation (PMID:34771672)

This keeps the disease page focused on driver axes rather than turning the
entry into an exhaustive mutation inventory.

## Phenotypes

The phenotype set emphasizes disease-defining cutaneous morphology and clinically
important symptom burden:

- patch/plaque/tumor lesion spectrum (PMID:34541796)
- plaque lesions as a canonical stage feature (PMID:40721285)
- erythrodermic evolution in some MF cases (PMID:34541796)
- pruritus as a patient-relevant symptom tracked in therapeutic studies
  (PMID:17577020)

## Treatments

The treatment section was kept disease-relevant and ontology-grounded, with NCIT
preferred when it gives materially better oncology specificity:

- narrowband UVB under `NCIT:C15344` UV Light Therapy (PMID:17986058)
- total skin electron beam radiation therapy with the exact NCIT procedure term
  `NCIT:C93341` (PMID:16207183)
- mogamulizumab (PMID:30100375)
- brentuximab vedotin (PMID:28600132)
- vorinostat (PMID:17577020)

This avoids mixing in very broad generic MAXO treatment labels when a more
oncology-specific NCIT procedure is available, while still using `MAXO:0000058`
for systemic pharmacotherapy actions paired with specific antineoplastic agents.
