# LOINC Tranche K Closing Ledger: Prenatal and Fetal Screening

**Date:** 2026-10-17
**Scope:** `projects/LOINC_DIAGNOSTICS.md` tranche K — chromosomal disorders and
screening-programme panels, bounded by `kb/disorders/` entries carrying a
cfDNA/NIPT, maternal-serum, nuchal-translucency, or karyotype diagnostic row.
**PRs:** #14630 (batch 1, 6 entries), #14633 (batch 2, 8 entries) — both open,
neither merged as of this writing.

## Entries examined and their outcome

| Entry | Outcome | Code / reason |
|---|---|---|
| Down_syndrome | Bound | `LOINC:77011-5` Fetal Chromosome 21 trisomy [Presence] based on Plasma cell-free DNA by Sequencing |
| Trisomy_18 | Bound (split into two rows) | `LOINC:29770-5` Karyotype; `LOINC:50580-0` generic multi-condition maternal screen panel (no triple/quad/penta specificity stated by the source) |
| Anencephaly | Bound (split into two rows) | Maternal Serum AFP Screening row: `LOINC:48802-3` serum AFP panel. Amniotic Fluid AFP and Acetylcholinesterase row: `LOINC:58735-2` amniotic AFP panel, `LOINC:76478-7` amniotic acetylcholinesterase panel |
| Spina_Bifida_Cystica | Bound | `LOINC:48802-3`, `LOINC:58735-2` (same two codes as Anencephaly, added to the entry's existing single combined row) |
| Hemolytic_Disease_of_the_Fetus_and_Newborn | Bound | `LOINC:100670-9` RHD gene allele [Identifier] in Plasma cell-free DNA Nominal--fetus |
| 47_XYY_Syndrome | Bound (karyotype only) + citable absence (screening) | `LOINC:29770-5` (blood), `LOINC:33773-3` (amniotic fluid) for the two confirmatory karyotype rows; no cfDNA screening code exists for the aneuploidy itself |
| 22q11.2_Deletion_Syndrome | Bound | `LOINC:75576-9` Fetal 22q11.2 deletion risk [Likelihood] — not the chromosome-21-specific code, and not the joint aneuploidy-and-22q11.2 panel, which asserts a test this row does not claim |
| 15q11q13_Microduplication_Syndrome | **Citable absence** | no code for incidental maternal CNV detection during genome-wide NIPS (the row describes a maternal, not fetal, finding) |
| Thanatophoric_Dysplasia | **Citable absence** | no FGFR3 code specifies maternal plasma cell-free DNA as the specimen; only Blood/Tissue (postnatal) and Amniotic fluid/CVS (the invasive route the test exists to avoid) exist |
| 45_X_46_XY_Mixed_Gonadal_Dysgenesis | **Citable absence** | no code for the 45,X/46,XY mosaic pattern itself, distinct from LOINC's simple Monosomy X risk family |
| Achondrogenesis_Type_IA | Bound | `LOINC:33069-6` Fetal nuchal translucency measured by US — the entry reports an actual measured value (4.3 mm at 14 weeks) |
| Tonne-Kalscheuer_Syndrome | **Declined** | nuchal translucency named only inside one quoted case-report sentence, no dedicated row, no reported value |
| CHRNA1-associated_Fetal_Hypo-akinesia_Disorder_of_Prenatal_Onset | **Declined** | has a dedicated ultrasound diagnosis row, but nuchal translucency is named only categorically, with no number for the quantitative measurement code to attach to |
| Congenital_Isolated_ACTH_Deficiency | Bound | `LOINC:LP15559-5` Estriol.unconjugated, the Part code — the entry's claim is qualitative ("isolated low" estriol), with no number or Multiple-of-the-median value cited, so the MoM family does not apply |
| Aflatoxin_Related_HCC | **Declined — collision** | "cell-free DNA" matched on a liquid-biopsy ctDNA assay (droplet digital PCR for somatic TP53 R249S in hepatocellular carcinoma), not prenatal cfDNA |
| Brain_Arteriovenous_Malformation | **Declined — collision** | "cell-free DNA" matched on somatic lesion genotyping from peripheral blood (a liquid-biopsy route to the lesion's own somatic driver mutation), not prenatal cfDNA |

Across 16 entries examined, 9 carry at least one new LOINC binding, 4 are
recorded as citable absences (3 full entries plus the screening half of
47_XYY_Syndrome, whose confirmatory karyotype rows are bound), and 4 decline
outright with a stated reason — 2 for want of a performed measurement and 2
for the same acronym-collision shape found earlier in this campaign
(99mTc-DPD scintigraphy matching "DPD"; here, liquid-biopsy ctDNA matching
"cell-free DNA").

## Finding 1: the AFP/estriol `[Multiple of the median]` family, unused this tranche

LOINC carries a family of prenatal-screening-specific codes distinct from the
plain analyte concentration: `[Multiple of the median]`, with adjusted,
unadjusted, weight-adjusted, and (for some analytes) diabetes-adjusted
variants, for both AFP and unconjugated estriol, in both serum and amniotic
fluid. MoM is the reporting convention prenatal screening programmes actually
use in practice — a bare "AFP panel - Serum or Plasma" panel code is
identical whether the context is prenatal screening or tumour-marker
monitoring.

None of the four entries in this tranche that cite AFP or estriol
(Anencephaly, Spina_Bifida_Cystica, Trisomy_18, Congenital_Isolated_ACTH_Deficiency)
states a MoM value or a numeric threshold (a "2.0" or "2.5 MoM" style cutoff).
Each makes a qualitative claim ("elevated," "isolated low") without a number.
Per the rule established on this tranche — bind the MoM code only when the
entry's own row states a MoM value or threshold — the panel/Part codes stand
in all four entries, and no `interpretation_bands` were added.

**This is a lead, not a defect.** If a future pass sources a specific
screening-programme cutoff for any of these four entries (the quad-screen MoM
threshold for Down syndrome, trisomy 18, or an open neural tube defect is
widely published), the MoM-family code is the correct rebind and the cutoff
would support a genuinely sourced `interpretation_bands` entry — something
this tranche never had the citation to add.

## Finding 2: four citable LOINC absences, dated

Each of the following was confirmed by a fully-enumerated search (every
result read, not a truncated page) against the Monarch KG search API
(`https://api-v3.monarchinitiative.org/v3/api/search`, which carries the
LOINC table) on **2026-10-17**. LOINC adds cfDNA screening codes release to
release, so a later search could find a code where this one did not; these
are dated for exactly that reason, and are recorded as a note on the
affected row rather than left as a silent gap.

- **15q11q13_Microduplication_Syndrome** — "15q11 duplication cell-free DNA",
  "genome-wide cell-free DNA", and "microdeletion microduplication
  cell-free DNA" each return zero results of any kind (total=0 for all
  three, nothing to enumerate).
- **Thanatophoric_Dysplasia** — "FGFR3 cell-free DNA" returns zero results
  (total=0). The broader "FGFR3" search returns 277 results, all read to
  the end; the only FGFR3 molecular-testing LOINC codes in that set specify
  Blood or Tissue (postnatal) or Amniotic fluid/Chorionic villus sample (the
  invasive route the cfDNA test exists to avoid) as the specimen — none
  names cell-free DNA.
- **45_X_46_XY_Mixed_Gonadal_Dysgenesis** — "45,X/46,XY mosaicism
  cell-free DNA" and "sex chromosome mosaicism cell-free DNA" each return
  zero results (total=0 for both).
- **47_XYY_Syndrome** (the screening half of the entry; the confirmatory
  karyotype rows are bound) — "XYY cell-free DNA", "XXY cell-free DNA",
  "XXX cell-free DNA", and "fetal sex chromosome aneuploidy" each return
  zero results (total=0 for all four).

A pattern across three of these four: LOINC's cfDNA aneuploidy family covers
the autosomal trisomies (21, 18, 13) and simple Monosomy X. It does not cover
microdeletion/microduplication panels beyond 22q11.2 (which does have its own
code family, bound on `22q11.2_Deletion_Syndrome`), single-gene skeletal
dysplasias, or the extra-sex-chromosome aneuploidies (47,XXY; 47,XXX;
47,XYY). A candidate pool built on "this entry mentions cfDNA/NIPT" will keep
surfacing entries where the technology is real but LOINC has not (yet) coded
that specific target.

## Open design decision, not performed: bulk karyotype binding

Roughly 140 `kb/disorders/` entries name karyotype somewhere in their text.
`LOINC:29770-5` (Karyotype [Identifier] in Blood or Tissue Nominal) and
`LOINC:33773-3` (Karyotype [Identifier] in Amniotic fluid Nominal) — both
bound individually, on their own merits, to specific rows in this tranche —
would attach mechanically to nearly all of them: find a diagnosis row naming
karyotype, read its specimen (blood/tissue vs. amniotic fluid/CVS), bind the
matching code. The mechanical part of that is almost entirely pattern
matching, not judgment.

That is exactly why it should not simply be dispatched as a tranche batch.
Every binding this campaign has made has rested on reading one entry's own
claim and choosing among a family of candidate codes for it — the AFP
panel-vs-MoM question, the VKORC1-vs-CYP2C9-panel question, the karyotype
blood-vs-amniotic-fluid question this tranche's own entries raised. A
sweep that binds the same two codes to ~140 entries by pattern match is a
different kind of act: it would be the first campaign binding made by rule
rather than by reading each entry, and it would do it at a scale no other
single PR in this campaign has approached.

**The choice:** either (a) treat karyotype as in-scope for a future
dedicated pass that still reads each entry's row individually — slower, but
consistent with every binding this campaign has made so far — or (b) treat
it as a deliberately different, rule-based operation and decide separately
whether to run it as a bulk mechanical pass with its own review standard.

**Recommendation:** (a). The two karyotype bindings made in this tranche
each needed a real decision — which specimen, whether the row described a
screen or a confirmation, whether a more specific code existed for the
disease's own named test. A bulk pass by pattern match would get the
specimen choice right by coincidence as often as by reading, and `Karyotype
Analysis` is exactly the generic row name a pattern match would latch onto
without checking whether the entry's own karyotype claim says blood,
amniotic fluid, or something the pattern can't tell apart (a postmortem
sample, a buccal swab, a tissue biopsy). If the 140-entry number makes a
manual pass impractical, that argues for narrowing the pattern (a karyotype
row with its own `presence:` value naming a specific abnormal result, the
shape every binding in this tranche actually had) rather than lowering the
bar on what "binding a code" means everywhere else in this campaign.

## What landed, in one line

9 of 16 examined entries carry at least one new LOINC binding across PRs
#14630 and #14633 (both open); 4 are recorded as citable absences dated
2026-10-17; 4 decline outright, 2 of them the same acronym-collision shape
(cell-free DNA / ctDNA) already seen once in this campaign as 99mTc-DPD /
dihydropyrimidine dehydrogenase. The MoM family and the karyotype
bulk-binding question are recorded above for whoever next touches a
prenatal-screening or chromosomal entry.
