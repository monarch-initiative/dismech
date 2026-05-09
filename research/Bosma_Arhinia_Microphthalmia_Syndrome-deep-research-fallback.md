# Bosma Arhinia Microphthalmia Syndrome Deep Research Fallback

## Scope

This fallback artifact supports curation of Bosma arhinia microphthalmia
syndrome (BAMS), represented by MONDO:0011323 and the structured Orphanet record
ORPHA:2250.

## Structured Sources

- ORPHA:2250 provides the usable disease definition, synonyms, autosomal
  dominant/unknown inheritance rows, antenatal/neonatal onset, ultra-rare
  worldwide prevalence, SMCHD1 gene association, OMIM xref, and 32 HPO
  phenotype-frequency rows.
- ORPHA:1135 is a sparse legacy cross-reference record for
  arrhinia-choanal atresia-microphthalmia syndrome. It does not include
  definition, phenotype, gene, inheritance, or epidemiology rows.

## PubMed Sources Used

- PMID:6802865: original Bosma report describing severe nasal/ocular
  hypoplasia, smell/taste impairment, hypogonadism, hernias, cryptorchidism,
  and normal intelligence.
- PMID:16353241: clinical review/case report summarizing the syndrome and
  developmental candidate pathways.
- PMID:28067911: SMCHD1 discovery series with de novo ATPase-domain missense
  variants and Xenopus functional evidence.
- PMID:28067909: independent arhinia/BAMS sequencing cohort and zebrafish model
  evidence.
- PMID:31243061: SMCHD1 mutation-spectrum study distinguishing BAMS-associated
  ATPase-domain variants from FSHD2.
- PMID:34209568: patient-derived neural crest cell study supporting AKT,
  extracellular-matrix, adhesion, and migration defects.
- PMID:36968924: recent case report with diagnostic criteria and anatomic
  findings.
- PMID:36944600: congenital arhinia pedigree with targeted SMCHD1 sequencing
  and staged nasal construction.

## Curation Boundaries

- All ORPHA:2250 HPO phenotype rows are represented with Orphanet frequency
  evidence.
- Treatment curation is limited to staged nasal/midface reconstruction and
  genetic counseling because these have direct cached evidence. Endocrine
  treatment was not added because the cached abstracts used here do not provide
  a quotable treatment-support snippet.
- The entry treats ORPHA:1135 as a legacy alias/cross-reference record rather
  than as a separate subtype because the local record is sparse and lacks
  subtype-defining clinical content.

## Provider Attempts

- `timeout 75s just research-disorder falcon
  Bosma_Arhinia_Microphthalmia_Syndrome` was terminated by the timeout
  (signal 15 / exit 124) before producing a provider artifact.
- `timeout 75s just research-disorder openai
  Bosma_Arhinia_Microphthalmia_Syndrome` was terminated by the timeout
  (signal 15 / exit 124) before producing a provider artifact.

The curation was completed from structured Orphanet rows and cached PubMed
evidence to avoid blocking on provider availability.
