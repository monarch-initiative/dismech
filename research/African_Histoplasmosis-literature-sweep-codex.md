# African Histoplasmosis literature sweep

- **Curator:** Codex
- **Date:** 2026-11-14
- **Disease:** African histoplasmosis
- **MONDO:** MONDO:0001262

## Scope and search

I treated the African histoplasmosis stub as a candidate curation unit rather
than as an automatic subtype of either open Histoplasma umbrella stub. The sweep
focused on PubMed and PubMed Central records for:

- `African histoplasmosis`
- `Histoplasma capsulatum var. duboisii`
- `Histoplasma duboisii`
- `Hcd histoplasmosis`

The final curation used seven fetched references:

- PMID:32887981, a 1993-2019 case review of H. capsulatum var. duboisii.
- PMID:35202403, a 2022 narrative review of histoplasmosis in Africa.
- PMID:33956817, a Republic of Congo African histoplasmosis review.
- PMID:30334708, a Kimpese, Democratic Republic of the Congo, case series.
- PMID:18217546, a review of Hcd infection reported in people with HIV.
- PMID:15538817, an older African histoplasmosis review.
- PMID:15597674, an older review of Histoplasma in Africa.

## Lump/split assessment

African histoplasmosis is appropriate as a standalone disease entry because the
agent is a named Histoplasma capsulatum variety, MONDO carries the disease as a
separate leaf, and the clinical syndrome differs from classical histoplasmosis.
The curated entry records that Hcd disease most often affects skin,
subcutaneous tissue, lymph nodes, and bone; the broader Histoplasmosis and
Histoplasma capsulatum infectious disease stubs should remain open for later
umbrella curation. Histoplasmosis meningitis and Histoplasma pericarditis are
organ-specific concepts and should be decided independently.

## Mechanistic synthesis

Hcd is a thermally dimorphic fungus. Its saprophytic environmental niche is
incompletely defined, but a natural reservoir in soil admixed with bat guano has
been reported and recent African case series have suggested bat-infested homes
and guano fertilizer as putative exposure sources. The exact portal is still not
settled: inhalation of microconidia and direct cutaneous inoculation after
trauma are both proposed.

Human lesions contain large thick-walled oval yeasts and a granulomatous
giant-cell inflammatory response. That tissue pattern links the organism to the
three dominant clinical manifestations used in the entry: cutaneous or
subcutaneous granulomatous lesions, osteomyelitis or other bone infection, and
lymphadenopathy.

The best-supported management evidence is still review-level and case-based.
Itraconazole and amphotericin B are the main antifungal options; published
African histoplasmosis treatment has largely followed IDSA histoplasmosis
guidance developed for classical histoplasmosis because no Hcd clinical trial
or efficacy study is available.

The first pass under-modeled severe disease. PMID:32887981 reported
disseminated forms in 60.6% of its 1993-2019 cases and global mortality of
23.4% by the end of follow-up. PMID:33956817 defines disseminated Hcd infection
as infection of at least two noncontiguous body sites. PMID:32887981 also
reported an HIV co-infection rate of 20.8%; PMID:18217546 supports advanced
HIV-associated immunosuppression as a host context for disseminated Hcd by
reviewing HIV/Hcd case reports in which most well-described patients had poor
CD4 counts and disseminated infection.

## Open gaps

The entry intentionally keeps several uncertainties explicit:

- It does not assert an animal reservoir or intermediate host, because the
  available African histoplasmosis reviews describe possible reservoirs as an
  open research question.
- It does not choose between inhalation and transcutaneous inoculation as the
  dominant portal, because reviews describe both as proposed and the entry can
  be made more specific only after new Hcd-specific ecology studies.
- It does not model Hcd-specific virulence enzymes or immune evasion, because
  the accessible Hcd clinical reviews mainly support tissue yeast persistence
  and granulomatous inflammation rather than a resolved molecular chain.
- It treats HIV infection as a host susceptibility context feeding
  dissemination, not as the only or dominant driver of disseminated Hcd, because
  the 1993-2019 review reports no correlation between disseminated forms and HIV
  infection.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 1 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.
