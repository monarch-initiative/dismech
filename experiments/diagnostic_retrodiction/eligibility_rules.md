# Eligibility rules for the diagnostic-retrodiction frame — version 2

Version 2 adds five rulings to version 1 (kept as `eligibility_rules.v1.md`):
subset tests (rule 1), a computed pre-test-era check (rule 2), a narrower
IMPROVEMENT (rule 3), combined rows (rule 4) and dating (rule 5). They are
marked **[v2 rule N]** where they appear below, and a reason changed by one ends
in `(v2 rule N)`. `eligibility_v2_changes.tsv` lists every row whose decision
changed between versions.

These rules decide which rows of `frame.tsv` are eligible disease/test pairs for
the retrodiction study. A pair is eligible when a dismech entry records a test,
run on an accessible specimen, that became the primary way the disease is
diagnosed, and that change can be dated to one primary research report from 1985 or
later. A time-sliced entry curated from literature before that publication
should then be able to show whether the test could have been anticipated.

The rules apply to every row of `frame.tsv` with `flag_nongenetic_specimen`
TRUE. A row is one test as dismech records it: one `diagnosis[]` or
`biochemical[]` item of one entry. Each row gets exactly one decision, INCLUDE or
EXCLUDE, and exactly one reason. An INCLUDE row also records a `subset`
(rule 1).

## What you need for each row

- `disease_name`, `row_type`, `row_name` and the bound term labels from
  `frame.tsv`. These identify the test.
- `specimen_basis` and `implicit_class`, which say how the frame decided the
  specimen.
- The disease's dismech entry, for context on what the test is used for.
- Knowledge of, or a literature search for, when and how the test entered
  diagnostic practice for this disease.

## Inclusion rule

**INCLUDE** a row only if all of the following hold:

1. It is a test performed on a specimen: blood, serum, plasma, blood cells,
   urine, CSF or a dried blood spot.
2. The specimen check (below) does not find a wrong specimen.
3. None of the exclusion reasons applies.
4. The test became a **primary diagnostic route** for this disease, or for a
   defined subset of the entry's patients (rule 1). It replaced at least one of
   these: biopsy; an invasive procedure; specialist testing, such as
   electrodiagnostics, nuclear medicine, imaging, or a dynamic or functional
   test; or diagnosis by clinical criteria alone. "Primary" means diagnosis can
   now proceed through this test in a typical case of the disease or subset,
   not that it is merely supportive.
5. Its entry into practice can be dated to **one primary research report** from
   1985 or later (rule 5).
6. The disease had a literature before the test (rule 2).

The reason for an INCLUDE row starts with `PRIMARY_ROUTE:`. It then says what
the test replaced, and gives the publication year (with first author where
known).

> Example: Membranous nephropathy, *Anti-PLA2R autoantibodies*. Serology
> replaced kidney biopsy in seropositive patients; primary report 2009.

### Rule 1: subset tests [v2 rule 1]

A test that became the primary route for a **defined subset** of the entry's
patients is INCLUDE, provided every other rule is met. The subset must be
nameable by the test result: antibody-defined forms of a disease, a genetic or
metabolic form found by the test, or a marker-defined type. Non-antibody
markers count; CSF hypocretin-1 for narcolepsy type 1 is an example.

Record the subset in the `subset` column, for example `LGI1-antibody limbic
encephalitis` or `GLUT1-deficiency absence epilepsy`. Write `ALL` when the test
is the route for the entry's disease as a whole. EXCLUDE rows record `NA`.

Rule 1 does not cover:
- a **differential test**, whose positive result means the patient does not
  have the entry's disease (AQP4-IgG in an ADEM entry);
- a test that **rules out another disease** (CSF hypocretin-1 in idiopathic
  hypersomnia);
- a test that **classifies** a disease already diagnosed some other way, where
  the diagnosis itself still rests elsewhere (AMH typing in persistent
  Müllerian duct syndrome).

This replaces version 1's standing decision that a subtype antibody in a broader
entry is NOT_PRIMARY_ROUTE.

Example: Glomerulonephritis, *Anti-PLA2R autoantibody*, INCLUDE, with subset
`PLA2R-antibody-positive membranous nephropathy`.

The years in the committed INCLUDE reasons were given from memory and have not
been checked against PubMed. `check_dating.py` exists to check them.

### FIRST or IMPROVEMENT

Every INCLUDE row records `first_or_improvement`. EXCLUDE rows record `NA`.

- **FIRST**: before this test, the disease had **no** primary diagnostic route on
  an accessible specimen. Diagnosis needed biopsy, an invasive or specialist
  test, or clinical criteria. Example: Smith-Lemli-Opitz syndrome, *serum
  7-dehydrocholesterol* (1994), which replaced clinical diagnosis.
- **IMPROVEMENT** [v2 rule 3]: the test replaced an **earlier accessible-specimen
  test** that was already the primary route, **and it measures a new analyte or
  target**. CSF counts as an accessible specimen here, so a blood test of a new
  analyte replacing a CSF test is an improvement. Example: Paroxysmal nocturnal
  hemoglobinuria, *flow cytometry for GPI-anchored proteins*, which replaced the
  Ham test's complement lysis.
- A **better method for the same analyte or target** is not an improvement. If
  the earlier route predates 1985, the row is EXCLUDE / PRE_1985. Examples:
  plasma free metanephrines (urinary metanephrines predate 1985), eGFR (creatinine
  clearance), DHR flow cytometry for CGD (NBT, the same oxidative burst), and the
  serotonin-release assay for HIT (platelet activation, as aggregation tests
  measured).

If the earlier accessible-specimen test existed but diagnosis still needed
biopsy, the new test is FIRST. Celiac disease is the example: endomysial
antibodies existed, but biopsy was still required, and anti-tTG IgA was the
first serology to remove the biopsy.

## Specimen check (rows with `specimen_basis` = IMPLICIT)

The frame marks a row IMPLICIT when no specimen is stated anywhere. In that case
it assumed blood because of the analyte class (`implicit_class`). For every
IMPLICIT row, set `specimen_check`:

- **CONFIRMED**: the assay is ordinarily run on an accessible specimen, even if
  the class label is wrong. Anti-Müllerian hormone is labelled AUTOANTIBODY,
  but it is a serum test, so it is CONFIRMED.
- **WRONG_SPECIMEN**: the assay is ordinarily run on something else, such as
  cultured fibroblasts, a muscle or liver biopsy, bone marrow, tumour tissue or
  an in vitro expression system. It also applies when the row is not a specimen
  test at all, for example imaging.

All other rows get `specimen_check` = `NA`.

A WRONG_SPECIMEN row is always EXCLUDE with reason WRONG_SPECIMEN, whatever else
applies.

## Rule 4: combined rows [v2 rule 4]

Some rows record two tests as one, such as an enzyme assay "with molecular
confirmation", or serology "plus renal biopsy". **Judge the non-genetic,
accessible-specimen component alone**, as if it were the whole row, and ignore
the genetic or tissue component. If the row has no such component (genetic
testing of blood and tissue, for instance), judge it as it stands. A clinical
score is not a specimen component.

Examples: Tay-Sachs disease, *combined enzyme and molecular diagnosis*, is
judged on the hexosaminidase A assay, giving PRE_1985. Membranous nephropathy,
*serology and target-antigen work-up*, is judged on PLA2R serology, giving
INCLUDE.

This replaces version 1's standing decision that a combined
biochemical-plus-molecular row is GERMLINE_SEQUENCING.

A row naming **two independently reported tests** of the same kind, such as
"AQP4 and MOG antibody testing", is NOT_DATABLE under rule 5. Each test is
judged on its own row where the entry records one.

## Rule 5: dating [v2 rule 5]

Date the test to the **first primary research report** establishing it for this
disease: a study that measured the test in patients with the disease. Reviews,
guidelines, classification criteria and consensus statements **do not count**,
even when they are what put the test into practice.

If no first primary research report can be identified, the row is NOT_DATABLE.
That includes routes assembled from several separately reported markers, where
no single report establishes the route; panels of many antibodies; and
profiling platforms whose founding reports are not about this disease.

Examples: FAS-related ALPS, *serum biomarker analysis*, dates to the 2009
research report of the biomarkers, not the 2010 revised criteria. Sézary
syndrome, *flow cytometry with KIR3DL2, CD7 and CD26*, is NOT_DATABLE, because
the route combines markers from separate reports and was fixed by consensus
criteria. Type 2 diabetes, *HbA1c*, is NOT_DATABLE because its diagnostic use is
dated by an expert-committee report.

## Exclusion reasons

Assign the **first** reason in this list that applies. Each reason has a
one-line definition and an example from the frame.

1. **NOT_A_DIAGNOSTIC_TEST**: the row is not a specimen test at all. It is
   imaging, a physical measurement, a procedure, a clinical score, a criteria
   set, or a surveillance schedule. Example: Periprosthetic joint infection, *PJI
   diagnostic criteria*.
2. **WRONG_SPECIMEN**: an IMPLICIT row whose assay is not run on an accessible
   specimen (see the specimen check). Example: Mixed phenotype acute leukemia,
   *multiparameter flow cytometric immunophenotyping*, which is done on bone
   marrow.
3. **GERMLINE_SEQUENCING**: a test of constitutional DNA, such as gene
   sequencing, a panel, an exome, a karyotype, copy-number testing, or prenatal
   cell-free DNA for a fetal constitutional variant. Somatic or clonal variants
   assayed in blood are not excluded here. Example: Trisomy X, *peripheral blood
   karyotype analysis*.
4. **INFECTIOUS_AGENT**: a test directed at a pathogen, such as culture,
   microscopy for the organism, antigen detection, nucleic-acid testing,
   pathogen-specific antibody serology, or interferon-gamma release assays. Host
   markers measured in an infection are not this reason. Example: Rocky Mountain
   spotted fever, *paired-serum indirect immunofluorescence antibody assay*.
5. **TISSUE_REQUIRED**: this reason has two forms, and both exclude. Either the
   assay itself runs on tissue, marrow, lavage or cultured cells, or the
   diagnosis still requires a biopsy and the accessible-specimen test is only an
   adjunct to it. Example: Idiopathic multicentric Castleman disease,
   *interleukin-6*, because diagnosis still needs a lymph node biopsy.
6. **ROUTINE_NONSPECIFIC**: a routine laboratory measure that is not specific to
   the disease. This means blood count and indices, metabolic panel components,
   CRP, ESR, liver enzymes, CK, LDH, ferritin, lactate, ammonia, lipids or
   urinalysis. It does **not** apply when the routine measure is itself the
   defining test of the disease. A defining routine measure is then judged by
   the later reasons. Example: Idiopathic hypereosinophilic syndrome, *absolute
   eosinophil count*. Counter-example: Immune thrombocytopenia, *platelet
   count*, is the defining test and was judged PRE_1985.
7. **DISEASE_DEFINED_BY_TEST** [v2 rule 2]: the disease has too little literature
   before the test to retrodict from. This is decided by a count, not a
   judgment: `check_pretest_era.py` counts PubMed records matching
   `"<disease_name>"[tiab] AND hasabstract`, published up to 31 December of the
   year before the test's discovery. A count **below 100** is
   DISEASE_DEFINED_BY_TEST. `<disease_name>` is the dismech entry's own name,
   exactly as given, with no synonyms. Example: Brunner syndrome, *urinary
   monoamine metabolite analysis*: 0 records before 1993.

   Three properties of the count affect who fails it:
   - **The entry name is searched, not the name the literature used.** An entry
     named after a later or qualified term fails even when the disease had a
     large literature. "Acquired Thrombotic Thrombocytopenic Purpura" has 0
     records before 1998; "thrombotic thrombocytopenic purpura" has 690.
     "Stiff Person Syndrome" has 1 before 1988; "stiff-man syndrome" has 35.
   - **Rare diseases fall below 100 under any name.** "Canavan" anywhere in the
     title or abstract has 24 records before 1988.
   - **`hasabstract` drops most records before about 1975**, which PubMed holds
     without abstracts: "Canavan disease" has 8 records before 1988 with the
     filter and 13 without.

   The discovery year used is screener A's, from the INCLUDE reason, and has not
   been checked against PubMed.
8. **PRE_1985**: the test was already the primary route before 1985. Example:
   Congenital hypothyroidism, *elevated TSH*.
9. **NOT_DATABLE**: the route cannot be traced to a first primary research report (rule 5). This
   covers profiling platforms shared across many disorders (organic acids,
   amino acids, acylcarnitines, newborn-screening panels, transferrin
   isoelectric focusing, glycan or oligosaccharide profiles, steroid profiles)
   and panels of many separately reported antibodies. Example: Paraneoplastic
   neurological syndromes, *high- or intermediate-risk neural autoantibodies*.
10. **NOT_PRIMARY_ROUTE**: the test is real, specimen-based, post-1985 and
    datable, but did not become the primary route. That includes supportive,
    prognostic, monitoring, research, screening-only and differential-diagnosis
    tests. Example: Acute disseminated encephalomyelitis, *serum MOG-IgG
    cell-based assay*, which reassigns cases to MOGAD rather than diagnosing
    ADEM.

One more reason applies only to rows that are not in the frame:

- **KB_GAP**: a known disease/test pair (from `recall_report.tsv`) whose test has
  no `diagnosis[]` or `biochemical[]` row in dismech, so the frame cannot carry
  it. These rows are appended with reason `KB_GAP: test not recorded in
  dismech`. Example: Lambert-Eaton myasthenic syndrome, *VGCC antibody*.

### Standing decisions for recurring cases

- **Newborn screening** is NOT_PRIMARY_ROUTE, because screening is followed by
  confirmatory testing. The one exception is TREC newborn screening for severe
  combined immunodeficiency. It is a new analyte (2005) that became the route by
  which cases are found, replacing recognition after infection.
- **A subset test** is decided by rule 1. Version 1's NOT_PRIMARY_ROUTE ruling
  for a subtype antibody in a broader entry no longer applies.
- **The same test in a syndromic entry** is judged on what it diagnoses there.
  Plasma metanephrines are INCLUDE wherever the entry has a pheochromocytoma
  component (MEN2, VHL, EGLN1, Pacak-Zhuang), because there they are the route
  to that component.
- **A test recorded twice in one entry**, as a diagnosis row and as a biochemical
  row, gets the same decision on both rows. INCLUDE counts are therefore per row,
  not per disease/test pair.
- **A combined row** is decided by rule 4. Version 1's GERMLINE_SEQUENCING
  ruling for biochemical-plus-molecular rows no longer applies.

## Marking ambiguous rows

An EXCLUDE reason is marked **ambiguous** when a careful reviewer could
reasonably reach a different decision or a different reason. The marker is
written straight after the reason code, for example
`TISSUE_REQUIRED (ambiguous): desmoglein ELISA supports but biopsy with DIF
remains required`.

Typical triggers:
- Guidelines differ on whether a biopsy is still needed.
- The publication year is close to the 1985 cutoff.
- The test came out of research and its clinical uptake is uneven.
- (Version 1 only: whether the disease existed as a diagnosis before the test.
  Rule 2 now decides this by count, so these rows are no longer marked.)
- The KB row combines a qualifying and a non-qualifying test.

INCLUDE rows are never marked ambiguous. They are checked through a random
sample instead.

Every ambiguous EXCLUDE row, plus a seeded 20% sample of INCLUDE rows (seed
20261111), goes into `eligibility_review.tsv` for second review.

## How each reason was reached

The reason text ends with a tag recording how the decision was made:

- **`[judged]`**: decided individually for that row.
- **`[rule]`**: assigned mechanically: by a pattern on the test's name and bound
  term label, after the row had been seen in a scan (the patterns are in
  `eligibility_work/build_eligibility.py`), or by the rule-2 count.
- **`[scanned-default]`**: the row was read in a full scan and not identified as
  meeting the inclusion rule, so it was assigned NOT_PRIMARY_ROUTE without an
  individual reason. This bucket mixes supportive markers with long-established
  analytes that could also be PRE_1985. It is the least specific reason in the
  file.

The order of exclusion reasons above is the rule. In the committed file, a row
where two reasons apply occasionally records a later one: some profiling
platforms are recorded PRE_1985 rather than NOT_DATABLE. Either reason excludes
the row, so no decision depends on the order.

`eligibility_work/build_eligibility.py` regenerates `eligibility.tsv` and
`eligibility_review.tsv` from `frame.tsv` and the judgment tables, and `--check`
confirms they match the committed files byte for byte.
