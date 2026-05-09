# Amniotic Band Syndrome Deep Research Fallback

## Scope

This fallback artifact supports a bounded curation of amniotic band syndrome
(MONDO:0015167; ORPHA:295000) from local Orphanet cache rows and PubMed
abstracts fetched into `references_cache/`.

## Structured Sources

- ORPHA:295000 supplies the disease definition, synonyms, antenatal/neonatal
  onset, Europe birth-prevalence class, MONDO/OMIM mappings, and 28 HPO
  phenotype-frequency rows.
- MONDO:0015167 also lists ORPHA:1034, but the local Orphadata snapshot did not
  contain ORPHA:1034 when rebuilt with `just structured-rebuild-orphanet --id
  1034`; ORPHA:295000 is the usable structured Orphanet record.

## PubMed Sources Used

- PMID:29756715: review covering epidemiology, etiologic theories, clinical
  characteristics, diagnosis, genetic counseling, treatment, and prognosis.
- PMID:24247024: prenatal diagnosis case series supporting fetal
  structural-anomaly-based diagnosis and phenotypic variability.
- PMID:24528986: fetoscopic release series supporting limb functional outcomes,
  umbilical-cord involvement, and fetal-demise risk.
- PMID:32951245: fetoscopic release update supporting feasibility and prevention
  of amputation/dysfunction.
- PMID:36116114: fetoscopic surgery case series reporting functional limb
  outcomes and procedure-related preterm risks.
- PMID:36584346: EUROCAT registry study supporting prevalence and phenotypic
  spectrum.
- PMID:31424867: StatPearls overview supporting fetal entanglement in the amnion
  and disruption/deformation/malformation sequence framing.

## Curation Boundaries

- No Mendelian gene or inheritance section was added because the evidence used
  here supports ABS as a sporadic, multifactorial congenital disruption sequence
  rather than a single-gene syndrome.
- Treatment curation was limited to fetoscopic release, postnatal surgical
  repair, and genetic counseling because these are directly supported by cached
  snippets.

## Provider Attempts

- `timeout 75s just research-disorder falcon Amniotic_Band_Syndrome` was
  terminated by the timeout with signal 15 and produced no provider artifact.
- `timeout 75s just research-disorder openai Amniotic_Band_Syndrome` was
  terminated by the timeout with signal 15 and produced no provider artifact.

The curation therefore proceeds from structured Orphanet rows and cached PubMed
abstracts. Literature scope was bounded to Orphanet, MONDO cross-references,
PubMed relevance searches for amniotic band syndrome/sequence, EUROCAT
prevalence evidence, clinical diagnostic series, and fetoscopic treatment
series/reviews.
