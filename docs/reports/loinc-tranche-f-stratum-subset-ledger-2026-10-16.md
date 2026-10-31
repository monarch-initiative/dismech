# LOINC Tranche F Stratum-Subset Ledger: Tumour Markers and Somatic Biomarker Tests

**Date:** 2026-10-16
**Scope:** `projects/LOINC_DIAGNOSTICS.md` Phase 3, Tranche F, biomarker-stratum
subset — entries whose own somatic biomarker is central to how the entry is
diagnosed. Most of the 27 are the design-decisions §3a L4 promoted strata
(EGFR-mutant NSCLC, HER2-positive breast cancer, MSI-H colorectal cancer, and
similar), whose promotion into a separate entry is justified by a distinct
diagnostic pathway. Five are not: `APL_PML_RARA`, `NPM1_Mutant_AML`,
`Glioblastoma_IDH_Wildtype`, `Anaplastic_Large_Cell_Lymphoma` and
`Alveolar_Rhabdomyosarcoma` are WHO/ICC-defined molecular or histologic
entities, which §3a treats as the *default* entry level rather than a
promoted stratum — no promotion-justification question applies to them, and
Finding 1 below is scoped accordingly. This ledger covers the four batches
that worked through the subset.
**PRs:** #14622 (batch 1), #14629 (batch 2), #14632 (batch 3), #14642
(batch 4), as of each batch PR's head commit on 2026-10-16 — all four were
still open and unmerged at that time, so a reader checking this after any of
them merges should treat the table below as a snapshot of that date, not of
current `main`.

## Durable: entries examined and their outcome

27 stratum entries were examined across the four batches; 26 carry at least
one binding, and one (`BRCA_Mutant_Prostate_Cancer`) carries none.

| Entry | Outcome | Code(s) |
|---|---|---|
| ALK_Rearranged_NSCLC | Bound (IHC + FISH); NGS left unbound | `LOINC:47303-3`, `LOINC:78205-2` |
| APL_PML_RARA | Bound | `LOINC:21551-7` |
| BRAF_V600E_Mutant_NSCLC | Bound (tissue + plasma, two rows) | `LOINC:58415-1`, `LOINC:93690-6` |
| BRAF_V600_Mutant_Melanoma | Bound (molecular + VE1 IHC, two rows) | `LOINC:97025-1`, `LOINC:85299-6` |
| Anaplastic_Large_Cell_Lymphoma | Bound | `LOINC:47303-3` |
| Alveolar_Rhabdomyosarcoma | Bound | `LOINC:93807-6` |
| HER2_Positive_Breast_Cancer | Bound (IHC + FISH, two rows) | `LOINC:85319-2`, `LOINC:49683-6` |
| MSI_High_Colorectal_Cancer | Bound (panel + 4-protein IHC + TMB, six rows) | `LOINC:81711-4`, `LOINC:81691-8/92/93/94`, `LOINC:94076-7` |
| EGFR_Mutant_NSCLC | Bound | `LOINC:21665-5` |
| FLT3_Mutant_AML | Bound (ITD + TKD, two rows) | `LOINC:79210-1`, `LOINC:92843-2` |
| NPM1_Mutant_AML | Bound (molecular); IHC row declined | `LOINC:54448-6` |
| IDH_Mutant_AML | Bound (D-2-HG + molecular, two rows) | `LOINC:79305-9`, `LOINC:95772-0` |
| ER_Positive_Breast_Cancer | Bound (ER + PR, two rows); Genomic Assays row declined | `LOINC:85337-4`, `LOINC:85339-0` |
| HER2_Positive_Gastric_Cancer | Bound (IHC + FISH, two rows) | `LOINC:18474-7`, `LOINC:49683-6` |
| HER2_Positive_Colorectal_Cancer | Bound (IHC + FISH + NGS, three rows) | `LOINC:18474-7`, `LOINC:49683-6`, `LOINC:42783-1` |
| KRAS_G12C_Mutant_NSCLC | Bound, with a recorded precision gap | `LOINC:21702-6` |
| Glioblastoma_IDH_Wildtype | Bound | `LOINC:60252-4` |
| MSI_High_Endometrial_Cancer | Bound (4-protein IHC + panel, five rows) | `LOINC:81691-8/92/93/94`, `LOINC:81711-4` |
| BRAF_Mutant_Thyroid_Cancer | Bound (two rows) | `LOINC:LP14697-4`, `LOINC:58415-1` |
| BRAF_V600E_Mutant_Colorectal_Cancer | Bound (molecular + VE1 IHC + MSI panel, three rows) | `LOINC:58415-1`, `LOINC:85299-6`, `LOINC:81711-4` |
| BRCA_Mutant_Prostate_Cancer | **Declined entirely** | — |
| HPV_Positive_Head_and_Neck_Cancer | Bound (p16); HPV DNA/RNA row declined | `LOINC:49556-4` |
| HPV_Negative_Head_and_Neck_Cancer | Bound (p16 + EGFR, two rows) | `LOINC:49556-4`, `LOINC:32581-1` |
| NTRK_Fusion_Positive_Cancer | Bound | `LOINC:93813-4` |
| RET_Rearranged_NSCLC | Bound | `LOINC:90927-5` |
| ROS1_Rearranged_NSCLC | Bound | `LOINC:81747-8` |
| Triple_Negative_Breast_Cancer | Bound (five rows) | `LOINC:85337-4`, `LOINC:85339-0`, `LOINC:85319-2`, `LOINC:49683-6`, `LOINC:105302-4`, `LOINC:50995-0` |

Every code above was read directly from the branch that carries it
(`origin/loinc-f-batch1` through `loinc-f-batch4`), each at the head commit
it carried on 2026-10-16. All four batch PRs were still open as of that
date (see Scope above), so a code listed here can drift from what actually
merges; re-check the table against each batch's merged content once it
lands, rather than trusting this snapshot indefinitely.

## Structural finding 1: most L4 strata examined have no `diagnosis:` section — but six of the 27 entries do, and five of the 27 are not L4 strata

Two counts are both correct here, because they describe different
populations: zero of the 21 entries in batches 2-4 carry a `diagnosis:`
section; six of the full 27-entry examined set do, and all six are in batch
1. Read either number only against its own stated population; the two are
not in tension. (Batch membership is not a cause of either count: every
`diagnosis:` section in this subset predates this tranche's curation and was
already on `main` before any batch touched its entry, so which batch an
entry landed in says nothing about why it does or does not carry one.)

Checking the six against this ledger's own classification (see Scope above)
rules out a tidier story: three of the six — `ALK_Rearranged_NSCLC`,
`BRAF_V600E_Mutant_NSCLC`, `BRAF_V600_Mutant_Melanoma` — are themselves §3a
L4 promoted biomarker strata, not WHO/ICC default-level entities; and two
entries without a `diagnosis:` section — `NPM1_Mutant_AML`,
`Glioblastoma_IDH_Wildtype` — are themselves non-L4 WHO/ICC entities. So
"WHO/ICC entity versus promoted stratum" does not cleanly separate the
diagnosis-bearing entries from the rest either; it predicts correctly for 22
of the 27, with these five as counter-examples in both directions.

What is worth carrying forward is narrower and still real, because it does
not depend on any classification this ledger could get wrong: among the 22
entries that are genuinely §3a L4 promoted strata — whose promotion is
justified by "a distinct first-line therapy or diagnostic pathway" — three
record that pathway structurally and nineteen do not, with no clean line
separating the two groups by anything this ledger classified. If this ledger
needs a sentence on why no clean line emerges, the honest one is that this
ledger's own classification does not explain the variation — not that some
other variable does. Whether the split reflects under-curation of the
nineteen, or a promotion criterion applied on clinical judgement that was
never meant to require structural backing, is a §3a question for whoever
revisits the ladder — not a LOINC one, and not one this ledger answers.

The six, with each row's `presence` value where the row sets one:

| Entry | First `diagnosis:` row | `presence` |
|---|---|---|
| `ALK_Rearranged_NSCLC` | Tumor ALK fusion testing | `REQUIRED_FOR_SUBTYPE_ASSIGNMENT` |
| `BRAF_V600E_Mutant_NSCLC` | Histologic NSCLC diagnosis with BRAF V600E confirmation | `REQUIRED_FOR_SUBTYPE_ASSIGNMENT` |
| `BRAF_V600_Mutant_Melanoma` | Clinicopathologic cutaneous melanoma diagnosis | `REQUIRED` |
| `APL_PML_RARA` | Morphologic Suspicion of APL | not set on this row |
| `Anaplastic_Large_Cell_Lymphoma` | Tissue Morphology and Immunohistochemistry | not set on this row |
| `Alveolar_Rhabdomyosarcoma` | Histologic and immunohistochemical classification | not set on this row |

Two of these (`ALK_Rearranged_NSCLC`, `BRAF_V600E_Mutant_NSCLC`) mark the
stratum-defining test `REQUIRED_FOR_SUBTYPE_ASSIGNMENT` — the entry already
records, structurally, that this test is how the stratum is assigned. All six
entries' new LOINC codes landed on the `diagnosis[].measurements` slot
CLAUDE.md's *LOINC Codes* section names as the natural home for exactly this
case — confirmed by reading each batch-1 diff against `main` directly
(`git diff origin/main origin/loinc-f-batch1 -- kb/disorders/<name>.yaml`) —
**not** on `biochemical[].loinc_term`. So wherever a `diagnosis:` row already
existed to attach to, the batches used it correctly; there is no binding here
that needs to be moved onto `measurements`. `biochemical[].loinc_term` was only ever the
fallback for an entry with no `diagnosis:` row to attach to (see
`EGFR_Mutant_NSCLC`, confirmed the same way), which is the actual shape of
the gap this finding is about.

The remaining three of the six (`APL_PML_RARA`, `Anaplastic_Large_Cell_Lymphoma`,
`Alveolar_Rhabdomyosarcoma`) are not design-decisions §3a L4 promoted strata at
all — see the Scope note above — so no promotion-justification question
applies to them; their `diagnosis:` sections exist simply because WHO/ICC
molecular/histologic entities normally carry one, independent of this
tranche's work. Their new LOINC codes also landed on `diagnosis[].measurements`,
for the same reason as the other three.

That leaves **21** of the 27 entries (27 minus the six above) with no
`diagnosis:` section at all. Two of those 21 — `NPM1_Mutant_AML` and
`Glioblastoma_IDH_Wildtype` — are themselves non-L4 WHO/ICC default-level
entities (the same set named in the Scope note above), so no
promotion-justification question applies to them either; their lacking a
`diagnosis:` section is simply a gap in the entry, unrelated to this
tranche's work.

That leaves the remaining **19** of the 27 entries — L4 promoted strata with
no `diagnosis:` section — where the finding as originally intended does hold:
these are the entries whose promotion into a *separate* entry (rather than a
`has_subtypes` row on the parent) is justified by having "a distinct
first-line therapy or diagnostic pathway," and the pathway that justifies the
promotion is not recorded anywhere structurally in the promoted entry — it
survives only as free-text `biochemical[]` notes, with no `diagnosis_term`,
no `measurements`, and no reference_ranges cut-off.

`BRCA_Mutant_Prostate_Cancer` is the sharpest instance among those 19: its
only biochemical row is PSA, the prostate-cancer-wide monitoring marker, not
a test for the BRCA mutation that defines its own stratum. A working,
Monarch-KG-resolvable LOINC code for combined BRCA1/2 testing exists
(`LOINC:50995-0`, bound without difficulty on `Triple_Negative_Breast_Cancer`
in the same batch), so this is not a LOINC coverage gap — the entry simply
never wrote a diagnostic-test row for the biomarker that defines it. This is
the exact failure mode the tranche's diagnostic-pathway check was designed
to surface, and it would not have been visible from reading the entry's
`genetic:` section alone, since that section describes the mutation's
biology without ever stating how it is tested for.

## Structural finding 2: LOINC has no Part-level identity code for any gene rearrangement

The Monarch KG search API (`q=gene rearrangements`,
`category=biolink:ClinicalMeasurement`) returns 98 results as of 2026-10-16,
fully enumerated (`limit=100` against a reported `total` of 98); zero carry
a `LP`/`LG` Part or panel prefix. This covers every gene family this subset
touched (ALK, RET, ROS1, NTRK1/2/3, FOXO1, PML::RARA, ERBB2). Unlike an
enzyme-activity assay,
where the method is incidental and a Part-level code is the correct
identity, a fusion/rearrangement biomarker has **no method-free identity
available at all** — FISH-specific and molecular-genetics-specific codes
are the only options LOINC provides. Two consequences worth carrying
forward for any future rearrangement-biomarker tranche work:

- Do not spend time searching for a Part code for a rearrangement family;
  none exists, and the search only costs time.
- LOINC codes some break-apart FISH probes by cytogenetic locus rather than
  gene symbol in the code's own label (`ROS1_Rearranged_NSCLC` binds
  `LOINC:81747-8`, labelled "Chromosome region 6q22 rearrangements," not
  "ROS1"). Confirm the mapping by searching the gene symbol directly and
  checking that the locus-named code is the one returned, rather than
  assuming a gene-symbol-free label means the code is for something else.

## Three narrower findings worth recording

- **A LOINC code names what was measured, not the result.** Two pairs in
  this subset are each other's complement on the same test:
  `HPV_Positive_Head_and_Neck_Cancer` / `HPV_Negative_Head_and_Neck_Cancer`
  bind the identical p16 IHC code (`LOINC:49556-4`), and
  `Triple_Negative_Breast_Cancer` reuses the identical breast-specimen
  ER/PR/HER2 codes bound on the positive-stratum entries. In both cases the
  entries differ in what the test *returns*, not in which test was run, and
  binding the same code on both sides is correct, not a collision to avoid.
- **An organ-specific LOINC label is a real trap, and it runs in both
  directions.** `LOINC:85319-2` ("HER2 [Presence] in **Breast cancer
  specimen**...") is correct on `HER2_Positive_Breast_Cancer` and
  `Triple_Negative_Breast_Cancer`, both genuinely breast cancer, and would
  have been wrong on `HER2_Positive_Gastric_Cancer` and
  `HER2_Positive_Colorectal_Cancer`, which bound the tissue-generic
  `LOINC:18474-7` instead because gastric and colorectal HER2 IHC are
  scored by different criteria than breast (the ToGA scheme, and proposed
  HERACLES criteria, respectively) — a real clinical difference, not only a
  coding one. Check what a candidate code's own label names before reusing
  it across organs, in either direction.
- **"Mutually exclusive with X" in an entry's own text means X is a
  differential, not that entry's own test.** `RET_Rearranged_NSCLC` and
  `ROS1_Rearranged_NSCLC` both matched the candidate pool on EGFR, ALK,
  ROS1/RET, and KRAS; both rows state outright that their own fusion is
  "mutually exclusive" with those other drivers, which settles that those
  genes are exclusionary differentials rather than this entry's own
  diagnostic pathway. Reading the row's own framing resolved both cases;
  neither needed a comprehensive-panel binding.

A fourth, narrower technical finding: `HPV_Positive_Head_and_Neck_Cancer`'s
HPV DNA/RNA row could not be bound at all, not because LOINC lacks a code —
its own NLM Clinical Table index carries dozens of high-risk HPV DNA and
E6/E7 mRNA codes — but because none of them resolve against the Monarch KG,
the authority this repository validates LOINC codes against. This is a
coverage gap in the KG's current LOINC ingestion rather than an absence from
LOINC itself, and is worth re-checking once the KG catches up.

## What remains unexamined

This ledger covers only the biomarker-stratum subset of tranche F. The
tranche's own scoping (`projects/LOINC_DIAGNOSTICS.md`, tranche F row) is
broader — "tumour markers and somatic biomarker tests" generally — and a
substantially larger population of non-stratum cancer entries in `kb/`
(histologic-entity and molecularly-defined-entity level, per the
design-decisions §3a ladder) has not been examined by this subset's
candidate pool at all. Whoever extends this tranche to that population
should expect the same two structural findings to recur only partially:
many of those entries are histologic-entity-level (L2/L3) rather than
biomarker-stratum (L4), so the "no `diagnosis:` section despite a stated
diagnostic-pathway justification" finding is specific to the L4 promotion
rule and may not generalize, while the rearrangement-family Part-code
finding is a fact about LOINC and will recur anywhere a fusion biomarker is
curated.
