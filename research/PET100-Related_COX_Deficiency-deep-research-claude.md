---
provider: claude-deep-research
model: claude-opus-4-8
harness: dismech PR-shepherd literature sweep (targeted WebSearch + WebFetch, PubMed/OMIM/GeneReviews cross-check)
cached: false
generated: '2026-06-16T00:00:00Z'
template_variables:
  disease_name: PET100-Related COX Deficiency
  mondo_id: MONDO:0033646
  category: Mendelian
verification:
  searches_run: 2
  sources_fetched: 3
  primary_papers_found: 3
  primary_papers_cited_before: 2
  new_primary_papers_added: 1
note: >
  Provenance artifact generated to satisfy the new-entry deep-research requirement
  for PR #4397 (review by ai4c-agent, 2026-06-16). This was a targeted literature
  completeness sweep rather than the full fan-out adversarial harness: because
  PET100-related disease is ultra-rare with a near-complete primary literature, the
  goal was specifically to confirm whether any literature had been missed. It had:
  the sweep surfaced PMID:31406627 (Mansour et al. 2019), a third primary report of
  the Lebanese founder allele that the original entry did not cite. That paper has
  now been cached (`just fetch-reference PMID:31406627`) and added to
  kb/disorders/PET100-Related_COX_Deficiency.yaml with snippet-validated evidence.
  This file documents research provenance only; the authoritative, snippet-validated
  evidence lives in the YAML. Do not import claims from this file without
  re-verifying the snippet against the cited primary source via
  `just fetch-reference` + `just validate-references`.
---

# PET100-Related Cytochrome c Oxidase (Complex IV) Deficiency — Deep Research Report

**Disease:** PET100-Related COX Deficiency (mitochondrial complex IV deficiency,
nuclear type 12; MC4DN12)
**MONDO:** MONDO:0033646 &nbsp;|&nbsp; **OMIM phenotype:** 619055 &nbsp;|&nbsp;
**Gene:** PET100 (HGNC:40038; formerly C19orf79) &nbsp;|&nbsp; **Inheritance:** autosomal recessive

## Executive Summary

PET100-related Complex IV (cytochrome c oxidase, COX) deficiency is an ultra-rare
autosomal recessive mitochondrial disorder caused by biallelic loss-of-function
variants in the small nuclear-encoded inner-mitochondrial-membrane Complex IV
biogenesis factor **PET100** (formerly C19orf79). PET100 forms a ~300 kDa subcomplex
with COX subunits and is required for their incorporation into the maturing
holoenzyme; its loss produces an **isolated Complex IV biogenesis defect**.

The primary human literature is small and, after this sweep, considered essentially
complete. It comprises **three primary reports**:

1. **Lim et al., 2014 (PMID:24462369, Am J Hum Genet)** — the founder report:
   eight Complex IV-deficient Leigh syndrome individuals from six Lebanese families
   homozygous for the initiation-codon allele **c.3G>C (p.Met1?)**; seizures
   prominent (distinguishing them from SURF1 disease). PET100 localized to the
   inner membrane forming a ~300 kDa subcomplex with COX subunits.
2. **Oláhová et al., 2015 (PMID:25293719, Eur J Hum Genet)** — a single
   non-Lebanese (British Pakistani) neonate homozygous for the truncating allele
   **c.142C>T (p.Gln48*)** with fatal neonatal-onset multiorgan disease: severe
   lactic acidosis, microcephaly, hypoglycemia, generalized aminoaciduria,
   coagulopathy/hypoalbuminemia ("severely impaired liver function"), and raised
   creatine kinase. This extended the phenotype beyond the founder population.
3. **Mansour et al., 2019 (PMID:31406627, J Pediatr Genet)** — **newly surfaced by
   this sweep; was NOT cited in the original entry.** Two further Lebanese families
   (one consanguineous), four affected siblings total, again carrying the founder
   **c.3G>C (p.Met1?)** allele, with developmental delay, seizures, lactic acidosis,
   abnormal brain MRI, low (~30%) muscle Complex IV activity, and in the more severe
   sibship failure to thrive, muscular hypotonia, developmental regression, and
   respiratory insufficiency.

A **GeneReviews** overview, *Nuclear Gene-Encoded Leigh Syndrome Spectrum Overview*
(PMID:26425749), provides authoritative baseline context for the Leigh syndrome
spectrum to which PET100 disease belongs and has been added as a tagged top-level
reference.

No curative therapy exists; management is supportive (seizure control, buffering of
metabolic acidosis, developmental support).

## 1. Literature Completeness Check (the point of this sweep)

| Reference | Year | Cohort | Allele | Status in entry |
|-----------|------|--------|--------|-----------------|
| PMID:24462369 (Lim) | 2014 | 8 individuals / 6 Lebanese families | c.3G>C (p.Met1?) | cited |
| PMID:25293719 (Oláhová) | 2015 | 1 neonate (British Pakistani) | c.142C>T (p.Gln48*) | cited |
| PMID:31406627 (Mansour) | 2019 | 4 siblings / 2 Lebanese families | c.3G>C (p.Met1?) | **added in this PR** |
| PMID:26425749 (GeneReviews) | overview | — | — | **added in this PR (tag)** |

Two independent WebSearch queries (gene/disorder synonyms; recent-cohort framing
2020–2025) returned no additional primary clinical reports beyond the three above.
The 2020–2025 sweep surfaced only secondary resources (GeneCards, OMIM #619055, GTR,
PreventionGenetics test pages) — no new patient cohorts — supporting the conclusion
that the primary literature is near-complete and dominated by the Lebanese founder
allele.

## 2. Gene and Protein Function

- **PET100 (formerly C19orf79)** encodes a small (~9 kDa) Complex IV biogenesis
  factor localized to the mitochondrial inner membrane, exposed to the intermembrane
  space. It forms a ~300 kDa subcomplex with COX subunits and acts at an
  intermediate stage of holoenzyme assembly (PMID:24462369). In yeast the homolog
  acts late in COX assembly; human PET100 appears required earlier, for assembly of
  mtDNA-encoded COX subunits (PMID:25293719 discussion).
- Loss of PET100 destabilizes COX subunits and blocks assembly of fully formed
  Complex IV, yielding **isolated** Complex IV deficiency (other OXPHOS complexes
  intact on BN-PAGE).

## 3. Genotype–Phenotype Notes

- **c.3G>C (p.Met1?)** — Lebanese founder allele; infantile-onset Leigh / Leigh-like
  syndrome with prominent seizures, developmental delay, variable lactic acidosis,
  basal ganglia lesions; residual muscle COX activity ~30%. Recurs across Lebanese
  families (PMID:24462369, PMID:31406627).
- **c.142C>T (p.Gln48*)** — single truncating allele; far more severe, prenatal-onset
  with neonatal death, extreme lactic acidosis (peak 63 mmol/l), microcephaly,
  multiorgan involvement (hepatic, renal, skeletal muscle) not seen with the founder
  allele (PMID:25293719).

## 4. Treatment

No disease-modifying therapy. Supportive/metabolic care only (bicarbonate/THAM
buffering of acute acidosis, anticonvulsants, developmental support) — consistent
across all reports.

## Caveats

- This was a focused completeness sweep, not the full multi-angle adversarial
  harness; it was scoped to the literature-gap question the reviewer raised. All
  clinical claims used as evidence in the YAML are independently snippet-validated
  against `just fetch-reference`-cached primary sources via
  `just validate-references`.
- The primary literature is dominated by a single founder allele in one population;
  generalization of genotype–phenotype correlations is limited by small N (~13
  reported individuals total across three papers).
