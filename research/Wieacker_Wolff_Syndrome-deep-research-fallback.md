# Wieacker-Wolff Syndrome Deep Research Fallback

## Scope

This fallback artifact supports curation of Wieacker-Wolff syndrome, represented
by MONDO:0010758 and structured Orphanet records ORPHA:3454 and ORPHA:85283.

## Structured Sources

- ORPHA:3454 provides the primary Wieacker-Wolff syndrome definition, synonym,
  X-linked recessive inheritance, neonatal onset, ultra-rare worldwide
  prevalence, ZC4H2 gene association, HPO phenotype frequencies, and
  MONDO/OMIM cross-references.
- ORPHA:85283 provides a sparse legacy record for X-linked intellectual
  disability, Miles-Carpenter type. It is used only as a synonym/cross-reference
  source because the cache has no separate definition, phenotype table,
  inheritance, or gene assertion.

## PubMed Sources Used

- PMID:23623388: ZC4H2 discovery report linking X-linked arthrogryposis
  multiplex congenita plus intellectual disability to ZC4H2 mutations, with
  mouse neuronal evidence for altered dendritic spine density and zebrafish
  evidence for impaired alpha-motoneuron development.
- PMID:35121145: ophthalmic case report/review supporting ptosis, strabismus,
  oculomotor apraxia, arthrogryposis, and facial/bulbar weakness.
- PMID:34484757: prenatal case report supporting ultrasound recognition of
  fetal arthrogryposis, lower-limb anomalies, ZC4H2 deletion/sequencing, and
  genetic counseling.
- PMID:31885220: de novo female nonsense-variant case supporting whole-exome
  diagnosis, truncal hypotonia, scoliosis, rehabilitation training, and altered
  mutant ZC4H2 protein trafficking.
- PMID:29150902: female case report supporting the traditional X-linked
  recessive description and cleft palate as a reported manifestation.

## Curation Boundaries

- ORPHA:3454 phenotype frequencies are used only where directly supported by
  exact Orphanet phenotype rows. Additional PubMed-only phenotypes are included
  without frequency unless the cited source provides a quantitative frequency.
- ORPHA:85283 is not modeled as a distinct subtype because the local structured
  cache is a title/cross-reference-only legacy record.
- Treatment curation is limited to rehabilitation/physical therapy and genetic
  counseling because the cached sources do not provide disease-modifying or
  drug-specific therapy evidence.

## Provider Attempts

- `timeout 75s just research-disorder openai Wieacker_Wolff_Syndrome` remained
  silent after the startup line and was terminated by the timeout with exit 124
  before producing an OpenAI provider artifact.
- `timeout 75s just research-disorder falcon Wieacker_Wolff_Syndrome` was
  terminated by the timeout with exit 124 before producing a Falcon provider
  artifact.

The curation was completed from structured Orphanet rows and cached PubMed
evidence to avoid blocking on provider availability.
