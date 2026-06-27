# Fanconi Anemia — phenotype gap analysis vs. the Connelly et al. custom HPO profile

## Source

Connelly E, Laraway B, Mullen KR, Mungall CJ, Haendel MA, Hurwitz EG.
*A custom phenotypic profile for Fanconi anemia: Addressing gaps in existing
disease annotations.* medRxiv, 2026. **PMID:41728284**, PMCID:PMC12919158,
DOI:10.64898/2026.02.10.26346018.

Profile data (CC-BY-4.0): https://github.com/ehurwitz/FA-custom-profile
(`FA-custom-profile.hpoa`, HPO release 2026-02-16; curated from the Fanconi
Cancer Foundation Clinical Care Guidelines, 5th Edition, 2020).

## Method

The paper publishes a 264-term custom HPO profile for FA and an Excel
comparison table (`FA-custom-profile.xlsx`) of 446 terms cross-tabulated by
presence in OMIM, Orphanet, and the custom profile, with an anatomical-system
classification. We extracted the 264 custom-profile HP IDs and diffed them
against the HP IDs already present in `kb/disorders/Fanconi_Anemia.yaml`.

## Result (at time of analysis)

| Set | HP terms |
|-----|----------|
| Connelly custom profile | 264 |
| dismech `Fanconi_Anemia.yaml` (before this batch) | 98 |
| Shared | 61 |
| In profile, missing from dismech | 203 (150 novel — absent from OMIM *and* Orphanet) |
| In dismech, absent from profile | 37 |

The missing terms concentrate in the systems the paper highlights as
under-annotated: **musculoskeletal (57)**, **genitourinary (32)**, digestive
(17), head/neck-oral (12), nervous (12), neoplasm (12), integument (11). Many
of the 203 are finer-grained children of terms dismech already carries (e.g.
dismech has generic "Radial Ray Defects"; the profile enumerates absent
radius/scaphoid/trapezium), so the gap is partly granularity, not pure absence.

## Batch 1 additions (this PR)

17 new phenotypes were added with verified evidence, prioritising the paper's
emphasis areas. Evidence sources are deterministic and snippet-verified:

- **Orphanet structured record `ORPHA:84`** (each snippet is an exact row of
  the cached phenotype table): Triphalangeal thumb (HP:0001199), Spina bifida
  (HP:0002414), Tetralogy of Fallot (HP:0001636), High palate (HP:0000218),
  Frontal bossing (HP:0002007), Short palpebral fissure (HP:0012745),
  Azoospermia (HP:0000027), Hydroureter (HP:0000072), Hyperreflexia (HP:0001347).
- **PMID:19622403** (Auerbach AD, *Fanconi anemia and its diagnosis*, Mutat
  Res 2009 — IFAR series; exact-substring quotes): Microtia (HP:0008551),
  Low-set ears (HP:0000369), Posteriorly rotated ears (HP:0000358), Fusion of
  middle ear ossicles (HP:0005473), Aplastic clavicle (HP:0006660),
  Oligozoospermia (HP:0000798), Obesity (HP:0001513), Abnormal circulating
  lipid concentration (HP:0003119). Azoospermia is additionally corroborated
  by Auerbach.

This raises the entry from 98 to 115 unique HP terms.

## Remaining work (future batches)

~186 profile terms remain unmapped. The next-highest-value, well-attested
candidates needing PMID/Orphanet sourcing: renal structural anomalies
(horseshoe/ectopic kidney, hydronephrosis), additional radial-ray detail
(absent radius/scaphoid/trapezium, thumb hypoplasia grading), GI-functional
terms, and oral-mucosal terms (relevant to the FA head-and-neck SCC surveillance
context). The OntoGPT-extracted `.hpoa` annotations cite the FCF guideline URL
(evidence code TAS), which does not satisfy the dismech PMID/structured-snippet
evidence policy, so each addition must be independently sourced and verified.
