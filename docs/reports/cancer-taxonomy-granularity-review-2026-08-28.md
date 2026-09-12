# Cancer taxonomy granularity review (2026-08-28)

**Question.** The lump/split rules for Mendelian disease are reasonably settled
(design decisions §3, issues #306/#7082). What is the right level of granularity
for cancer entries — variants, genes, pathways, or classic oncology (site +
histology)? This report reviews how the KB currently handles cancer, compares
it with the field's current classification practice, and proposes a decision
ladder for ratification in `docs/explanation/design-decisions.md`.

**TL;DR.** The field's answer is *none of the four alone*: the accepted backbone
is cell/tissue of origin + histology, with molecular alterations promoted into
the definition of an entity only where a classification body (WHO 5th edition,
ICC) has judged that the alteration defines a biologically and clinically
distinct disease. Below that level, genes and variants are treatment-selection
*strata*, not taxa; pathways are a cross-cutting *annotation layer*, not taxa;
and stage is orthogonal to taxonomy entirely. The KB is already ~80% aligned
with this — its pathway handling (hallmark modules + mechanism groupings) is
exactly right, and its WHO-integrated CNS/heme entries are exemplary — but it
carries three systematic deviations: biomarker-stratum entries that reuse their
parent's MONDO ID as `disease_term` (the #5121 collisions), ten `Metastatic_*`
stage entries curated as sibling diseases, and no recorded rule saying which
stratum a new cancer entry should land on.

---

## 1. What the KB does today

Cancer entries currently sit at **eight distinct granularity strata**, most of
them undocumented as strata:

| Stratum | Examples | Own MONDO ID? |
|---|---|---|
| Organ/system umbrella | `Lung_Carcinoma`, `Glioma`, `Lymphoma`, `Renal_Cell_Carcinoma`, `Cervical_Cancer`, `Esophageal_Carcinoma`, `Hodgkin_Lymphoma` | yes |
| Histologic entity (classic oncology; the bulk) | `Pancreatic_Ductal_Adenocarcinoma`, `Colon_Adenocarcinoma`, `Osteosarcoma`, `Diffuse_Large_B_Cell_Lymphoma`, `Small_Cell_Lung_Cancer`, `Clear_Cell_Renal_Cell_Carcinoma` | yes |
| WHO-integrated histo-molecular entity | `Glioblastoma_IDH_Wildtype`, `IDH_Mutant_Astrocytoma`, `IDH_Mutant_Oligodendroglioma`, `H3_K27_Altered_Diffuse_Midline_Glioma`, `Medulloblastoma_WNT_Activated`/`_SHH_Activated`, `APL_PML_RARA`, `Core_Binding_Factor_AML`, `Acute_Myeloid_Leukemia_with_CEBPA_Somatic_Mutations`, `B-Lymphoblastic_Leukemia_Lymphoma_With_Recurrent_Genetic_Abnormality` | yes (e.g. `MONDO:0850335`) |
| Biomarker/therapy stratum | 7 NSCLC driver entries (`EGFR_Mutant_NSCLC` … `ROS1_Rearranged_NSCLC`), `MSI_High_Colorectal_Cancer`, `HER2_Positive_Colorectal_Cancer`, `ER_Positive_Breast_Cancer`, `HER2_Positive_Breast_Cancer`, `Triple_Negative_Breast_Cancer`, `PIK3CA_Mutant_Breast_Cancer`, `FLT3_Mutant_AML`, `NPM1_Mutant_AML`, `IDH_Mutant_AML`, `FGFR_Altered_Cholangiocarcinoma`, `BRCA_Mutant_Prostate_Cancer`, … | **mostly no** — `disease_term` reuses the parent term |
| Variant level | `KRAS_G12C_Mutant_NSCLC`, `BRAF_V600E_Mutant_Colorectal_Cancer`, `BRAF_V600E_Mutant_NSCLC`, `BRAF_V600_Mutant_Melanoma`, `MET_Exon_14_Skipping_NSCLC`; plus variant tiers as `has_subtypes` *inside* `EGFR_Mutant_NSCLC` (exon 19 del / L858R / exon 20 ins / T790M) | mostly no |
| Tissue-agnostic biomarker indication | `NTRK_Fusion_Positive_Cancer` | yes (`MONDO:0700215`) |
| Etiology stratum | `HPV_Positive_Head_and_Neck_Cancer` / `HPV_Negative_…`, `EBV_Associated_Gastric_Cancer`, `Gastric_Cancer_H_pylori_Associated`, `Aflatoxin_Related_HCC`, `Arsenic_Related_Cancers` | mixed |
| Stage stratum | 10 `Metastatic_*` entries (NSCLC, Melanoma, CRC, Gastric, HCC, Ovarian, Prostate, Breast, RCC, Pancreatic) | no — parent term, `skos:closeMatch` |

Two other levels are handled *without* Disease entries, correctly:

- **Pathways / hallmark biology** live in `kb/modules/` (all ten Hanahan–
  Weinberg hallmarks exist as modules: `sustaining_proliferative_signaling`,
  `evading_growth_suppressors`, `resisting_cell_death`,
  `enabling_replicative_immortality`, `tumor_angiogenesis`,
  `invasion_and_metastasis`, `deregulated_cellular_energetics`,
  `genome_instability_mutation`, `tumor_promoting_inflammation`,
  `immune_checkpoint_blockade`, plus `senescence_tumor_suppression`) and in
  mechanism-based groupings (`Checkpoint_Responsive_Cancers`,
  `DNA_Repair_Synthetic_Lethality_Cancers`, `Hedgehog_Pathway_Activation_Disorders`).
- **Germline predisposition syndromes** (`Li-Fraumeni_Syndrome`,
  `Lynch_Syndrome`, `Familial_Adenomatous_Polyposis`, `Von_Hippel-Lindau_Disease`,
  `Hereditary_Breast_and_Ovarian_Cancer_Syndrome`, …) are curated as Mendelian
  diseases under the existing §3 rules, with the
  `Two-Hit_Tumor_Suppressor_Cancer_Predisposition_Syndromes` grouping over
  them. These are genuinely Mendelian and need no cancer-specific rule.

### Where the current policy came from

The only stated policy is `projects/CANCER.md` §"Molecular Subtypes as Discrete
Entities": *"Instead of one 'Breast Cancer' entry with subtypes, we have
HER2-Positive / Triple-Negative / ER-Positive / PIK3CA-Mutant Breast Cancer"*,
justified by different biology, treatment, prognosis, and biomarker-specific FDA
approvals. That is a project plan, not a ratified design decision — design
decisions §3 ("separate file only for a distinct MONDO identity **and** a
substantially independent mechanism") was written for Mendelian disease and is
violated by most of the biomarker-stratum entries, which have **no** distinct
MONDO identity.

### Measurable symptoms

- **MONDO anchor collisions (issue #5121), re-measured 2026-08-28: still 21
  MONDO IDs shared by >1 entry**, unchanged since the 2026-07 audits —
  steady-state, not shrinking. Of the 21, ~14 are cancer: `MONDO:0005061` (lung
  adenocarcinoma) ×5, `MONDO:0005575` (CRC) ×4, `MONDO:0005233` (NSCLC) ×4,
  `MONDO:0005075` (papillary thyroid) ×3, `MONDO:0005012` (melanoma) ×3, plus
  cholangiocarcinoma, gastric ×2, breast, prostate, HCC, ovarian, RCC pairs.
- **Missing ladder rungs.** The 5 lung-adenocarcinoma driver entries anchor to
  `MONDO:0005061` but there is no `Lung_Adenocarcinoma` entry; breast has four
  receptor strata and a `Metastatic_Breast_Carcinoma` but no base breast
  carcinoma entry. The strata float without their histologic parent.
- **Double representation without linkage.** `Non-Small_Cell_Lung_Cancer` lists
  `EGFR-mutant NSCLC` and `ALK-rearranged NSCLC` in `has_subtypes` while the
  same concepts exist as separate files; neither side references the other, so
  the two copies can silently diverge.
- **Non-disjoint siblings.** `FLT3_Mutant_AML` and `NPM1_Mutant_AML` co-occur
  in a large fraction of real patients (FLT3-ITD is enriched *within*
  NPM1-mutant AML); MSI-high CRC is enriched for BRAF V600E. Sibling Disease
  entries carry an implicit disjointness a reader will assume; nothing in the
  entries records that these strata overlap. (The `BRAF_V600E_Mutant_Colorectal_Cancer`
  entry partially handles this with MSI-H/MSS subtypes.)
- **Stage entries are thin.** The `Metastatic_*` entries carry ~5
  pathophysiology nodes each, largely duplicating the parent plus a
  dissemination arm that is exactly what the `invasion_and_metastasis` module
  exists for.

---

## 2. What the field currently does

The consensus across the current authorities is a **layered histogenesis-first
taxonomy with molecular promotion**, not a molecular taxonomy:

1. **WHO Classification of Tumours, 5th edition** (the "blue books",
   2019–2024) keeps site + cell lineage + histology as the backbone and
   promotes a molecular alteration into the *definition* of an entity only
   where it defines distinct biology and clinical behavior. CNS5 (2021) is the
   furthest along: "Glioblastoma, IDH-wildtype", "Diffuse midline glioma,
   H3 K27-altered", medulloblastoma molecular groups — delivered as a layered
   **integrated diagnosis** (histology layer + molecular layer + grade), per
   the cIMPACT-NOW process. WHO-HAEM5 and the ICC (both 2022) define AML by
   genetic abnormality (APL with *PML::RARA*, AML with *NPM1* mutation, AML
   with *CEBPA* bZIP mutation, CBF translocations) — but deliberately do
   **not** make "FLT3-mutant AML" an entity: FLT3 is a risk/therapy stratum
   that cuts across entities. Soft-tissue tumours similarly promote
   fusion-defined entities (Ewing, synovial sarcoma, *CIC*- and
   *BCOR*-rearranged sarcoma as separate entities).
2. **ICD-O-3.2** encodes topography × morphology — the two-axis classic
   backbone. The KB already stores `classifications.icdo_morphology`.
3. **OncoTree** (MSK; the de facto precision-oncology tree used by GENIE,
   cBioPortal) is explicitly histology-first; molecular biomarkers are
   annotations *on* samples, not tree nodes, with only a handful of
   molecularly defined nodes where the field treats them as entities.
4. **Precision-oncology knowledge bases** (OncoKB, CIViC, ESMO's ESCAT tiers)
   model gene/variant → (tumor type, therapy, evidence level) as an
   **actionability annotation joined to a histologic disease**, not as
   diseases. FDA tissue-agnostic approvals (pembrolizumab for MSI-H/TMB-H,
   larotrectinib/entrectinib for *NTRK* fusions, selpercatinib for *RET*,
   dabrafenib+trametinib for BRAF V600E) create *indications* spanning taxa —
   the one place the field itself talks about "NTRK fusion-positive cancer" as
   a quasi-entity.
5. **Why not variants or genes as the primary axis:** the same alteration is a
   different disease in a different lineage. BRAF V600E melanoma responds to
   BRAF inhibition; BRAF V600E colorectal cancer does not (EGFR-mediated
   feedback), which is why the combination is encorafenib **+ cetuximab** —
   the KB's own `BRAF_V600E_Mutant_Colorectal_Cancer` entry models precisely
   this mechanism. TCGA pan-cancer analyses (Hoadley et al.) found cell of
   origin dominates molecular clustering. Conversely, CML, APL, and Ewing
   sarcoma show a single lesion *can* define an entity when it is the
   initiating, universal, lineage-bound driver.
6. **Why not pathways:** pathway lesions (MAPK, PI3K, Hedgehog) recur across
   entities and even across cancer/non-cancer boundaries (RASopathies). The
   field uses them as cross-cutting biology and drug-development strata, never
   as taxa. The KB's hallmark modules + `conforms_to` + mechanism groupings
   are the correct rendering of this layer.

So, to the question "variants, genes, pathways, or classic oncology?": **classic
oncology is the backbone; molecular becomes taxonomic only by promotion; genes
and variants below that are strata; pathways are never taxa.** The nuance is
that promotion is a *judgment the field has already made, entity by entity* —
WHO/ICC did the arbitration, and MONDO tracks it (it has minted
`MONDO:0850335` IDH-wildtype GBM, `MONDO:0700215` NTRK fusion-positive cancer,
and per-entity heme terms).

---

## 3. Assessment: where dismech agrees and where it deviates

**Aligned (keep):**

- Pathways as modules/groupings, never entries — exactly the field's layer
  model.
- WHO-integrated CNS and heme entities as their own entries with their own
  MONDO IDs — this *is* current best practice (CANCER.md Tier 9 even cites
  WHO CNS 2021 as the rationale).
- Predisposition syndromes under the Mendelian rules; somatic cancer of the
  associated organ kept separate (Lynch vs `MSI_High_Colorectal_Cancer`,
  Gorlin vs `Basal_Cell_Carcinoma`).
- Variant tiers *inside* a stratum entry via `has_subtypes` (the
  `EGFR_Mutant_NSCLC` exon-19-del/L858R/T790M pattern) — matches how the field
  treats variant classes (sensitivity strata, not diseases).
- `stages:` for disease phases (CML chronic/accelerated/blast) per the
  cancer-curator skill.

**Deviating, but defensibly — formalize rather than revert:**

- The ~25 biomarker/therapy-stratum entries (NSCLC drivers, breast receptor
  classes, CRC MSI/BRAF/HER2, melanoma BRAF/NRAS/KIT, AML FLT3/IDH, …) are
  *ahead of* WHO but aligned with how precision oncology actually operates,
  and they pass issue #7082's disjunction test: each has its own initiating
  pathophysiology chain and its own first-line therapy, which `has_subtypes`'
  `subtype:` discriminator cannot scope (no `subtype:` slot exists on
  `Pathophysiology` or `Treatment`). For a *mechanism-first* KB this is the
  content that justifies existence as an entry. The
  `Molecularly_Defined_NSCLC_Subtypes` grouping records this reasoning.
  **The problem is not the split; it is that the split is unanchored and
  unregulated** — entries reuse the parent MONDO ID as `disease_term`
  (violating §3's own "distinct MONDO identity" clause and producing the
  #5121 many-to-one), no rule says when the next such entry is warranted, and
  overlap between non-disjoint strata is unrecorded.

**Deviating, and should be fixed:**

- **`Metastatic_*` entries.** No classification system treats stage as a
  taxon — TNM is deliberately orthogonal to ICD-O/WHO. These ten entries
  contradict the cancer-curator skill's own `stages` guidance, are thin
  (~5 nodes), duplicate the parent's biology, and account for a third of the
  #5121 collisions. Their real content (dissemination biology,
  treatment-line changes at metastasis) belongs in the parent entry as
  `stages:` + a `conforms_to` on the `invasion_and_metastasis` module, or in
  progression records.
- **Missing histologic parents / double representation.** Strata exist whose
  parent rung is absent (`Lung_Adenocarcinoma`, base breast carcinoma), and
  parents carry `has_subtypes` duplicating split files with no
  cross-reference either way.

---

## 4. Proposed decision ladder (draft for design-decisions.md)

Extend §3 with a cancer-specific clause, compatible with #7082's
disjunction/promotion machinery:

| Level | Represent as | Rule |
|---|---|---|
| **L1 Organ/system pool** ("lung cancer", "lymphoma") | Lean umbrella `Disease` entry *or* a `Grouping`; shared biology only | Never the curation target for mechanism content; every pathophysiology node must be true of all members |
| **L2 Histologic entity** (WHO blue-book entity: PDAC, SCLC, DLBCL, osteosarcoma) | `Disease` entry — **the default level for a new cancer entry** | This is "classic oncology"; anchor is the entity's MONDO term |
| **L3 Molecularly defined entity** (IDH-wildtype GBM, APL with PML::RARA, NPM1-mutant AML, Ewing) | `Disease` entry | Create when WHO/ICC defines the entity molecularly, i.e. the field has already promoted it; MONDO nearly always has the term |
| **L4 Biomarker/therapy stratum** (EGFR-mutant NSCLC, MSI-H CRC, TNBC, FLT3-mutant AML) | Default: `has_subtypes` on the L2/L3 entry. **Promote to its own entry** only when it passes #7082's test: ≥2 pathophysiology nodes not true of siblings **and** a distinct first-line therapy or diagnostic pathway | On promotion: (a) file a MONDO NTR (Monarch runs MONDO — the missing terms are fixable, and several precedents exist: `MONDO:0005494` TNBC, `MONDO:0003865` KIT-mutant melanoma); until granted, anchor to the parent term with `mapping_predicate: skos:narrowMatch` in `mondo_mappings` and a note, never a bare parent reuse; (b) record non-disjointness with sibling strata in `notes`/`differentiating_mechanisms`; (c) add/extend the covering `Grouping`; (d) leave a pointer subtype in the parent's `has_subtypes` naming the split file rather than a divergent copy |
| **L5 Variant tier** (exon 19 del vs L858R; V600E vs V600K) | `has_subtypes` inside the L4 entry | Never its own file. Exception: a variant *is* the L4 stratum when therapy is variant-specific (KRAS G12C is the stratum because sotorasib is G12C-covalent; "KRAS-mutant NSCLC" would be the wrong grain) |
| **Stage / metastasis** | `stages:`, progression records, `invasion_and_metastasis` module conformance | Never a `Disease` entry |
| **Etiologic stratum** (HPV± OPSCC, EBV-GC, H. pylori GC, aflatoxin HCC) | Case-by-case via the same L4 promotion test | HPV+ oropharyngeal SCC arguably passes (distinct mechanism, staging, prognosis — AJCC 8 already stages it separately); EBV-GC is a TCGA molecular subgroup and sits closer to a subtype |
| **Tissue-agnostic biomarker indication** (NTRK fusion, MSI-H/TMB-H pan-cancer) | One entry per biomarker, categorized `Tumor-Agnostic Indication`, MONDO-anchored | Do not also stamp it as a subtype of every organ cancer; organ-specific manifestations reference it |
| **Pathway / hallmark** | `kb/modules/` + mechanism `Grouping` only | Never a `Disease` entry (current practice, now stated) |

Germline predisposition syndromes remain under the existing Mendelian rules —
the cancer clause governs the somatic neoplasm entries only.

## 5. Recommended follow-up actions

1. **Ratify** (maintainer sign-off, per the register's process) a cancer
   granularity section in `docs/explanation/design-decisions.md` based on §4,
   resolving the CANCER.md-vs-§3 contradiction in favor of an explicit
   promotion rule. This also settles the cancer half of #306 and #7082.
2. **Resolve #5121 non-uniformly**, as its scanner comment already suggested:
   keep the driver splits (option 2) but require the narrowMatch-anchor
   convention + MONDO NTRs for promoted strata; lump the `Metastatic_*`
   entries (option 1) into their parents as `stages`; treat the non-oncology
   pairs separately.
3. **Fold the ten `Metastatic_*` entries** into their parents (stages +
   module conformance), preserving their evidence.
4. **De-duplicate parent `has_subtypes` vs split files** with the
   pointer-subtype pattern (start with `Non-Small_Cell_Lung_Cancer`).
5. **Create the missing L2 parents** (`Lung_Adenocarcinoma`; a base breast
   carcinoma entry) or explicitly document why the strata partition
   substitutes for them.
6. **Record stratum overlap** where siblings are non-disjoint (FLT3×NPM1 AML,
   MSI-H×BRAF-V600E CRC) — at minimum in `notes` and grouping
   `differentiating_mechanisms`; a structural "overlaps_with" is a possible
   schema follow-up but not required to start.
7. **Extend the `cancer-curator` skill** with the §4 ladder so new entries
   land on the right rung without re-deriving the policy.

## Provenance

Repo evidence: `kb/disorders/` census on this branch (2026-08-28); MONDO
anchor-collision scan re-run this date (21 shared IDs, listed in issue #5121's
buckets); `projects/CANCER.md`; `kb/groupings/Molecularly_Defined_NSCLC_Subtypes.yaml`;
`.claude/skills/cancer-curator/SKILL.md`; design decisions §3; issues #306,
#3881, #5121, #7082. Field practice: WHO Classification of Tumours 5th ed.
(incl. CNS5 2021 / cIMPACT-NOW integrated diagnosis), WHO-HAEM5 and ICC 2022,
ICD-O-3.2, OncoTree, OncoKB/CIViC/ESCAT actionability modeling, FDA
tissue-agnostic approvals.
