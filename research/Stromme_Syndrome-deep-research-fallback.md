# Stromme Syndrome Deep Research Fallback

## Scope

This fallback artifact supports curation of Stromme syndrome, represented by
MONDO:0009477 and structured Orphanet records ORPHA:506307 and ORPHA:444069.

## Structured Sources

- ORPHA:506307 provides the primary Stromme syndrome definition, synonyms,
  autosomal recessive inheritance, antenatal onset, ultra-rare worldwide
  prevalence, CENPF gene association, and MONDO/OMIM cross-references.
- ORPHA:444069 provides the severe fetal CENPF-associated ciliopathy spectrum
  with mid-gestation lethality, hydrocephalus, cerebellar vermis hypoplasia,
  corpus callosum agenesis, duodenal atresia, gastrointestinal malrotation,
  bilateral renal hypoplasia, and craniofacial features.

## PubMed Sources Used

- PMID:26820108: CENPF discovery report for classic Stromme syndrome sibling
  pairs, including autosomal recessive inheritance, whole-exome sequencing,
  truncating CENPF mutations, and the classic apple-peel intestinal atresia,
  ocular anomaly, and microcephaly triad.
- PMID:28407396: independent affected sibling family with homozygous truncating
  frameshift CENPF mutation and classic clinical features.
- PMID:18203155: pre-CENPF clinical report supporting the classic phenotype,
  including apple-peel intestinal atresia, microcephaly, microphthalmia,
  anterior chamber anomalies, corneal clouding, and visual impairment.
- PMID:25564561: human fetal, cell, and zebrafish evidence linking CENPF to a
  severe fetal ciliopathy, IFT88 ciliary targeting, short renal epithelial
  cilia, ciliary function, and cortical neurogenesis.

## Curation Boundaries

- ORPHA:506307 has no HPO phenotype table in the local structured cache, so
  phenotype frequencies are intentionally omitted unless supported by an exact
  quantitative source.
- ORPHA:444069 is modeled as a severe fetal CENPF-associated subtype/spectrum
  within MONDO:0009477 rather than as a separate disorder entry.
- Treatment curation is limited to symptom-directed supportive care and genetic
  counseling because the cached Stromme-specific sources do not provide direct
  drug or disease-modifying therapy evidence.

## Provider Attempts

- `just research-disorder openai Stromme_Syndrome` was started and remained
  silent after the startup line for about 60 seconds. The process was
  terminated with signal 15 before producing an OpenAI provider artifact.
- `timeout 60s just research-disorder falcon Stromme_Syndrome` was terminated
  by the timeout (signal 15 / exit 124) before producing a Falcon provider
  artifact.

The curation was completed from structured Orphanet rows and cached PubMed
evidence to avoid blocking on provider availability.
