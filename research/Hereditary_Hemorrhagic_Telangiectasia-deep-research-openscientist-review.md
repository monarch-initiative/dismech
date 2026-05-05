# Hereditary Hemorrhagic Telangiectasia OpenScientist Report Review

Date: 2026-04-24

## Scope

Review of the verbatim OpenScientist report at
`research/Hereditary_Hemorrhagic_Telangiectasia-deep-research-openscientist.md`
against the current curated YAML, the Falcon report, and fetched primary
references used during HHT curation.

## Overall assessment

- The report is useful as a lead-generation artifact for disease-level structure.
- It is not safe for direct ingestion without review.
- The strongest value was in surfacing the 2024 PATH-HHT pomalidomide trial.
- The report also contains at least one ontology-anchor error and several claims
  that are plausible but too loosely sourced for direct promotion.

## Findings That Held Up On Review

- Core disease framing as an autosomal dominant vascular dysplasia involving the
  BMP9/BMP10-ENG-ALK1-SMAD4 axis.
- Two-hit / focal lesion framing for AVM formation.
- Broad genotype-phenotype split:
  - `ENG` enriched for pulmonary and cerebral AVMs.
  - `ACVRL1` enriched for hepatic AVMs.
- High disease-burden framing around recurrent epistaxis, iron deficiency, and
  visceral AVM complications.
- Therapeutic significance of the PATH-HHT randomized trial (`PMID:39292928`).

## Review Findings

### 1. Incorrect ontology anchor in the verbatim report

The OpenScientist report uses `MONDO:0008535` as the HHT identifier. The current
validated repo entry uses `MONDO:0019180` in
`kb/disorders/Hereditary_Hemorrhagic_Telangiectasia.yaml`. This means the
verbatim report should be treated as informative text, not as ontology-safe
structured input.

### 2. One claim was clearly worth promotion after primary-source check

The report surfaced the pomalidomide Phase 3 result. After fetching the
underlying abstract (`PMID:39292928`), that evidence was strong enough to add a
new `Pomalidomide Therapy` treatment entry to the HHT YAML.

### 3. Several claims remain "interesting but not yet curation-safe"

These may be correct, but they were not promoted from the OpenScientist report
without additional source-level checking:

- pregnancy-risk summary values
- manganese-deposition / basal-ganglia MRI discussion
- sex-difference claims
- forward-looking therapeutic language such as "potential first-ever
  FDA-approved therapy"

These are exactly the kinds of statements that should stay in the verbatim file
until a reviewer fetches and checks the underlying papers.

### 4. Technical note on the provider run

For this HHT job, the OpenScientist `/status` endpoint continued to report
`running` even after the artifacts ZIP already contained `final_report.md`. The
verbatim report recovered cleanly from the ZIP, but this behavior means status
alone is not a reliable completion signal for eval bookkeeping.

## What Was Promoted From The Review

- `PMID:39292928` was fetched and used to support `Pomalidomide Therapy` in the
  curated HHT YAML.

## Specific Paper Check: PMC12274349

Paper:

- `PMC12274349`
- `PMID:40681766`
- DOI: `10.1038/s42003-025-08461-6`
- Title: `Overlapping upstream ORFs ending at c.125 lead to reduced Endoglin, contributing to Hereditary Hemorrhagic Telangiectasia.`

Result:

- This paper was **not surfaced** in the verbatim OpenScientist HHT report.
- It was also **not surfaced** in the verbatim Falcon HHT report.
- It is **not currently referenced** in the HHT YAML.

Evidence for that conclusion:

- repo search across the four HHT report artifacts found no hit for
  `PMC12274349`
- no hit for `PMID:40681766`
- no hit for `10.1038/s42003-025-08461-6`
- no hit for the title string

Interpretation:

- This omission is understandable. `PMID:40681766` is a narrower 2025 molecular
  diagnostics / `ENG` 5'UTR mechanistic paper, whereas both agent reports leaned
  toward disease-level reviews, cohort studies, and clinically central
  management papers.
- It is still potentially useful for a future refinement of the `ENG` genetics
  section, especially if we want better coverage of noncoding pathogenic
  mechanisms and molecular diagnosis edge cases.

## Bottom Line

Keep the OpenScientist file as the verbatim eval artifact. Use the review file to
record what survived cross-checking, what was promoted into YAML, and what still
needs source-level verification before curation.
