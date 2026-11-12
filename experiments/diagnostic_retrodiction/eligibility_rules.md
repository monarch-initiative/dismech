# Eligibility rules for the diagnostic-retrodiction frame

These rules decide which rows of `frame.tsv` are eligible disease/test pairs for
the retrodiction study. A pair is eligible when a dismech entry records a test,
run on an accessible specimen, that became the primary way the disease is
diagnosed, and that change can be dated to one primary publication from 1985 or
later. A time-sliced entry curated from literature before that publication
should then be able to show whether the test could have been anticipated.

The rules apply to every row of `frame.tsv` with `flag_nongenetic_specimen`
TRUE. A row is one test as dismech records it: one `diagnosis[]` or
`biochemical[]` item of one entry. Each row gets exactly one decision, INCLUDE or
EXCLUDE, and exactly one reason.

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
4. The test became a **primary diagnostic route** for this disease. It replaced
   at least one of these: biopsy; an invasive procedure; specialist testing, such
   as electrodiagnostics, nuclear medicine, imaging, or a dynamic or functional
   test; or diagnosis by clinical criteria alone. "Primary" means diagnosis can
   now proceed through this test in a typical case, not that it is merely
   supportive.
5. Its entry into practice can be dated to **one primary publication** from
   1985 or later.

The reason for an INCLUDE row starts with `PRIMARY_ROUTE:`. It then says what
the test replaced, and gives the publication year (with first author where
known).

> Example: Membranous nephropathy, *Anti-PLA2R autoantibodies*. Serology
> replaced kidney biopsy in seropositive patients; primary report 2009.

The years in the committed INCLUDE reasons were given from memory and have not
been checked against PubMed. `check_dating.py` exists to check them.

### FIRST or IMPROVEMENT

Every INCLUDE row records `first_or_improvement`. EXCLUDE rows record `NA`.

- **FIRST**: before this test, the disease had **no** primary diagnostic route on
  an accessible specimen. Diagnosis needed biopsy, an invasive or specialist
  test, or clinical criteria. Example: Smith-Lemli-Opitz syndrome, *serum
  7-dehydrocholesterol* (1994), which replaced clinical diagnosis.
- **IMPROVEMENT**: the test replaced an **earlier accessible-specimen test** that
  was already the primary route. CSF counts as an accessible specimen here, so a
  blood test replacing a CSF test is an improvement. Example: Pheochromocytoma
  and paraganglioma, *plasma free metanephrine*, which replaced urinary
  catecholamines.

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
7. **DISEASE_DEFINED_BY_TEST**: the disease was first described together with
   the test, so there was never a pre-test way of diagnosing it to retrodict.
   Example: Brunner syndrome, *urinary monoamine metabolite analysis*, since the
   syndrome was described with its urinary pattern in 1993.
8. **PRE_1985**: the test was already the primary route before 1985. Example:
   Congenital hypothyroidism, *elevated TSH*.
9. **NOT_DATABLE**: the route cannot be traced to one primary publication. This
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
- **A subtype antibody in a broader entry** is NOT_PRIMARY_ROUTE. It identifies
  one subtype rather than diagnosing the entry's disease. Examples: anti-PLA2R in
  the general *Glomerulonephritis* entry, and AQP4-IgG in *Optic Neuritis*.
- **The same test in a syndromic entry** is judged on what it diagnoses there.
  Plasma metanephrines are INCLUDE wherever the entry has a pheochromocytoma
  component (MEN2, VHL, EGLN1, Pacak-Zhuang), because there they are the route
  to that component.
- **A test recorded twice in one entry**, as a diagnosis row and as a biochemical
  row, gets the same decision on both rows. INCLUDE counts are therefore per row,
  not per disease/test pair.
- **A combined biochemical-plus-molecular row** is GERMLINE_SEQUENCING, marked
  ambiguous, because its genetic part decides it.

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
- It is unclear whether the disease existed as a diagnosis before the test.
- The KB row combines a qualifying and a non-qualifying test.

INCLUDE rows are never marked ambiguous. They are checked through a random
sample instead.

Every ambiguous EXCLUDE row, plus a seeded 20% sample of INCLUDE rows (seed
20261111), goes into `eligibility_review.tsv` for second review.

## How each reason was reached

The reason text ends with a tag recording how the decision was made:

- **`[judged]`**: decided individually for that row.
- **`[rule]`**: assigned by a pattern on the test's name and bound term label,
  after the row had been seen in a scan. The patterns are in
  `eligibility_work/build_eligibility.py`.
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
