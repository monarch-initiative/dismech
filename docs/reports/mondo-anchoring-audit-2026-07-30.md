# Mondo-anchoring audit (dismech → Mondo)

**Date:** 2026-07-30
**Issue:** [#7175](https://github.com/monarch-initiative/dismech/issues/7175) — tripartite gap-exchange (dismech ⇄ Monarch KG ⇄ Mondo)
**Scope:** `kb/disorders/*.yaml` (n = 1,640). Fully local, deterministic.
**Regenerate:**

```bash
uv run python scripts/mondo_anchor_audit.py                                   # summary
uv run python scripts/mondo_anchor_audit.py --tsv research/mondo_anchoring_worklist.tsv
```

This is the first of the six directed gap-flows in #7175 — the one that needs no
external data. It measures how well dismech disorder records are anchored to Mondo,
and surfaces the concrete `dismech → Mondo` handoff items (new-term / subtype
requests) plus dismech-internal fixes. It does **not** decide *how* any individual
concept should be modeled — that per-entry policy is [#7178](https://github.com/monarch-initiative/dismech/issues/7178).

## Headline

| Metric | Value |
|---|---|
| Disorders with a MONDO primary `disease_term` | **1,611 / 1,640 (98.2%)** |
| MONDO ids missing from the current Mondo release | **0** |
| MONDO ids obsolete/deprecated in Mondo | **0** |
| Stored-label drift vs Mondo canonical | **3** |
| Unanchored primary slot, **no** MONDO anywhere (Mondo candidates) | **17** |
| Unanchored primary slot, MONDO present elsewhere (promote-anchor fix) | **12** |
| `mondo_mappings` narrowMatch / broadMatch (granularity mismatch) | **5 / 7** |
| MONDO ids used as primary anchor by >1 entry | **22 ids / 54 entries** |

The anchoring layer is in good shape: no dangling or obsolete Mondo ids. The
actionable work splits cleanly into **dismech → Mondo requests** (17 concepts) and
**dismech-internal fixes** (3 label drifts + 12 anchor promotions).

## A. dismech → Mondo: new-term / subtype candidates (17)

Entries with no MONDO id anywhere in the file. Six carry an OMIM id that anchors a
Mondo lookup or new-term request; the remainder are exposure / iatrogenic / viral /
gene-level concepts that test Mondo's scope.

| Entry | OMIM anchor | Note |
|---|---|---|
| `EEFSEC_Deficiency` | OMIM:607695 | gene-level neurodevelopmental |
| `GOLGA2-Related_Golgin_A2_Deficiency` | OMIM:620240 | gene-level |
| `HAO1-Related_Glycolate_Oxidase_Deficiency` | OMIM:605023 | gene-level metabolic |
| `RAB5C-Related_Neurodevelopmental_Disorder_with_Macrocephaly` | OMIM:604037 | gene-level |
| `SLC26A6-Related_Hyperoxaluria_and_Nephrolithiasis` | OMIM:610068 | gene-level transporter |
| `VPS51-Related_Pontocerebellar_Hypoplasia-CDG` | OMIM:618606 | gene-level CDG |
| `KATNB1-related_Cortical_Malformation` | — | gene-level |
| `NDE1-related_Microcephaly_Lissencephaly` | — | gene-level |
| `TUBB_TUBB5-related_Microcephaly` | — | gene-level |
| `UGGT1-congenital_disorder_of_glycosylation` | — | gene-level CDG (has term, no id) |
| `Arsenic_Poisoning` | — | exposure/toxicology |
| `Chemotherapy_Induced_Nausea_and_Vomiting` | — | iatrogenic |
| `Spaceflight_Associated_Neuro-Ocular_Syndrome` | — | exposure/environmental |
| `Volumetric_Muscle_Loss` | — | acquired injury |
| `Transient_Neonatal_Pustular_Melanosis` | — | dermatologic (has term, no id) |
| `Human_Metapneumovirus_Infection` | — | infectious |
| `Seasonal_Coronavirus_Infection` | — | infectious |

## B. dismech-internal fixes (no Mondo action)

### B1. Label drift — stored `term.label` ≠ Mondo canonical (3)

| Entry | MONDO id | Stored label | Canonical label |
|---|---|---|---|
| `Chronic_Myeloid_Leukemia` | MONDO:0011996 | chronic myelogenous leukemia, BCR-ABL1 positive | chronic myeloid leukemia |
| `Minimal_Change_Disease` | MONDO:0006835 | lipoid nephrosis | minimal change disease |
| `Multiple_Mitochondrial_Dysfunctions_Syndrome_9B` | MONDO:0971174 | multiple mitochondrial dysfunctions syndrome 9B | multiple mitochondrial dysfunctions syndrome 9b |

The first two store a Mondo *synonym* rather than the canonical label; the third is a
case-only difference. `preferred_term` may stay as-is (it is allowed to differ);
`term.label` should be corrected to the canonical string.

### B2. Promote-anchor — MONDO present elsewhere but not in the primary slot (12)

These already reference a plausible MONDO id (in `mappings`/`genetic`) but leave
`disease_term.term.id` empty. The fix is to promote the correct id into the primary
slot — no Mondo request needed. Care is required where several MONDO ids appear (some
are comorbidities/related terms, not the entity's own class):

`AIP-related_pituitary_adenoma_predisposition`, `Acute_Post-Surgical_Pain`,
`Adenovirus_Respiratory_Infection`, `CKD-Mineral_Bone_Disorder`, `FICUS_syndrome`,
`GNAS-related_pituitary_adenoma_3`, `GPR101-related_pituitary_adenoma_2`,
`Green_Tobacco_Sickness`, `MCM9-related_gametogenic_failure`,
`SLC26A1-Related_Oxalate_Transporter_Deficiency`,
`SRPX2-related_Speech_Epilepsy_Polymicrogyria`, `USP8-related_pituitary_adenoma_4`.

The three pituitary-adenoma entries all point at MONDO:0006373 (pituitary adenoma) —
a signal they may want a shared intermediate anchor with gene-specific subtypes, which
is exactly the record-altitude question in #7178.

## C. Granularity mismatch (`mondo_mappings`)

These are candidate inputs to the **mechanism-gated split** decision (#7178), recorded
here only as discrepancies — not adjudicated.

- **narrowMatch (dismech finer than mapped Mondo), 5:** `ER_Positive_Breast_Cancer`,
  `Familial_Thoracic_Aortic_Aneurysm_and_Aortic_Dissection` (×9),
  `GABRG2-Related_Epilepsy`, `GRIN1-Related_Neurodevelopmental_Disorder` (×3),
  `Parkinsons_Disease`.
- **broadMatch (dismech broader than mapped Mondo), 7:** `Acetaminophen_Hepatotoxicity`,
  `Focal_Articular_Cartilage_Defect_of_the_Knee`, `GABRG2-Related_Epilepsy`,
  `Rhizomelic_Chondrodysplasia_Punctata_Plasmalogen_Synthesis_Defect` (×2),
  `Stargardt_Disease`, `Stickler_Syndrome_Type_1`, `Trimethylaminuria`.

`mondo_mappings` skos-predicate totals: exactMatch 288 · closeMatch 30 · narrowMatch 15
· relatedMatch 14 · broadMatch 8. (Predicate *occurrences*; the narrow/broad file
counts above are distinct entries.)

## D. Shared primary anchors (same MONDO id on >1 entry)

**22 MONDO ids are used as the primary `disease_term` by 54 entries.** Detected by
`scripts/mondo_anchor_audit.py`; per-entry counts are in the `shared_anchor_n` column
of the worklist TSV. Three tiers:

### Tier 1 — intentional finer-than-Mondo splits (~45 entries; correct as-is)

Precision-oncology driver subtypes and metastatic-stage variants sharing a parent term
because Mondo has no molecular-subtype term. Simultaneously a strong **dismech → Mondo
subtype-request** signal.

| MONDO id | Label | ×  | Entries |
|---|---|---|---|
| MONDO:0005061 | lung adenocarcinoma | 5 | EGFR / KRAS-G12C / MET-ex14 / RET / ROS1 NSCLC |
| MONDO:0005233 | non-small cell lung carcinoma | 4 | ALK / BRAF-V600E / Metastatic / generic |
| MONDO:0005575 | colorectal cancer | 4 | BRAF-V600E / HER2+ / MSI-high / Metastatic |
| MONDO:0005012 | cutaneous melanoma | 3 | BRAF-V600 / Metastatic / NRAS |
| MONDO:0005075 | thyroid gland papillary carcinoma | 3 | BRAF / generic / RET-fusion |
| MONDO:0007256 | hepatocellular carcinoma | 3 | Aflatoxin / generic / Metastatic |
| MONDO:0001056 | gastric cancer | 2 | EBV / HER2+ |
| MONDO:0003210 | intrahepatic cholangiocarcinoma | 2 | FGFR-altered / IDH-mutant |
| MONDO:0004950 | gastric carcinoma | 2 | H. pylori / Metastatic |
| MONDO:0004989 | breast carcinoma | 2 | Metastatic / PIK3CA |
| MONDO:0005086 | renal cell carcinoma | 2 | Metastatic / generic |
| MONDO:0005211 | ovarian serous adenocarcinoma | 2 | Metastatic / HGSC |
| MONDO:0008315 | prostate cancer | 2 | BRCA / Metastatic |
| MONDO:0007915 | systemic lupus erythematosus | 2 | Neuropsychiatric SLE / generic |
| MONDO:0100038 | complex neurodevelopmental disorder | 2 | ANK2 / BLOC1S1 (two-gene-at-generic-term) |

### Tier 2 — likely mis-anchor (a more specific Mondo term probably exists)

- **Confirmed:** the Waardenburg pair both sit on generic MONDO:0018094, but type-level
  terms exist — MONDO:0008670 (WS type 1) for `PAX3_Waardenburg_Spectrum`, MONDO:0019517
  (WS type 2) for `MITF_Waardenburg_Tietz_Spectrum`. *Caveat:* these are "spectrum"
  records and may be intentionally broader than one numbered type — curator's call.
- **Worth a targeted check** (OAK search inconclusive, not asserting absence):
  `Obesity_Due_to_MC4R_Pathway_Disruption` (on MONDO:0011122 obesity disorder);
  `SLC6A1-Related_Disorder` (on MONDO:0014633 *epilepsy with myoclonic-atonic seizures*,
  likely too narrow for the gene's full phenotype);
  `Malnutrition-related_Diabetes_Mellitus` (on the diabetes umbrella MONDO:0005015, which
  the umbrella entry itself already holds via `closeMatch`);
  `Pacak-Zhuang_syndrome` (on MONDO:0035540 pheochromocytoma-paraganglioma).

### Tier 3 — possible genuine redundancy / lump

- **`Neuromyelitis_Optica` + `Neuromyelitis_Optica_Spectrum_Disorder` → MONDO:0019100.**
  Mondo folds NMOSD into the same term (no separate NMOSD class found), so these may be
  the same entity modeled twice — the clearest duplication candidate.
- **`Chemotherapy_Induced_Diarrhea` + `Travelers_Diarrhea` → MONDO:0001673 (diarrheal
  disease).** Two etiologically unrelated conditions pinned to a generic symptom-level
  term; both are under-anchored.

Tiers 2/3 are flagged for curator review, not auto-fixed — they intersect the
record-altitude policy call ([#7178](https://github.com/monarch-initiative/dismech/issues/7178)).

## E. Groupings & modules anchoring

Different classes anchor differently, so the disorder audit doesn't apply verbatim.
Regenerate: `uv run python scripts/grouping_anchor_audit.py`.

**Groupings (`kb/groupings/`, n=48).** A `Grouping` carries an optional MONDO cross-ref in
`mappings.mondo_mappings` — not a `disease_term` (a grouping stands on its own curated
rationale and need not recapitulate a MONDO class).

- **29 map to MONDO — all valid** (0 missing / obsolete / label-drift).
- **19 have no MONDO mapping.** Two sub-cases (OAK `basic_search` is imperfect, so treat
  as provisional):
  - **Existing MONDO term → just add the mapping:** `Mucolipidoses` (MONDO:0019248).
  - **Likely novel mechanism/treatment-response unions → Mondo grouping-class candidates:**
    `Fibrotic Disorders`, `Polyglutamine Disorders`, `TDP-43 Proteinopathies`,
    `FGFR-Related Skeletal Dysplasias`, `DNA Repair Synthetic-Lethality Cancers`,
    `Immune Checkpoint-Responsive Cancers`, `Digenic and Oligogenic Disorders`,
    `Parkinsonism Dopaminergic Degeneration Disorders`, `Epilepsy Excitation-Inhibition
    Imbalance Disorders`, and others (full list in the script output). Many are
    mechanism-based unions Mondo is unlikely to carry — consistent with dismech leading
    Mondo on mechanism-defined groupings.

**Modules (`kb/modules/`, n=118).** Deliberately **not** Mondo-anchored — they model
conserved processes anchored to process ontologies (GO / OGMS / MPATH / UBERON), so they
are **out of scope for the Mondo dimension**. 0 carry a `disease_term`; the 11 with a stray
MONDO reference (in evidence/notes) carry no obsolete ids. (The MPATH continuant gaps for
Xogenesis modules — amyloid/thrombus/atheroma — are a separate OBO-request track.)

## Corrections to earlier ad-hoc figures

An earlier chat-level count (before this reproducible pass) was wrong on three points,
recorded here so the numbers don't propagate:

- "17 unanchored" → **29 primary-slot** (17 no-MONDO-anywhere + 12 promote-anchor).
- "9 narrowMatch subtype candidates" → **5** MONDO-narrower entries (the earlier count
  swept in ICD10CM/NCIT narrowMatches from other `*_mappings` blocks).
- "6 files with explicit gap flags" → a crude text-regex detector was unreliable and is
  omitted; explicit `MONDO lacks …` prose flags need a better pass before being trusted.

## Not covered here (follow-ups for #7175)

- **Groupings & modules** anchoring (`kb/groupings/`, `kb/modules/`) — same audit,
  different classes.
- **Mondo → dismech** (curation-target direction) — needs a scope call; suggested
  bound: Mondo children/siblings of terms dismech already uses.
- **Monarch KG ⇄ dismech / Mondo** — needs external KG data.

## Machine-readable worklist

Full per-disorder inventory (all 1,640 rows): `research/mondo_anchoring_worklist.tsv`
(`name`, `anchor_state`, `mondo_id`, `stored_label`, `oak_flag`, `mondo_mapping_preds`).
