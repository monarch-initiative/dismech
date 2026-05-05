---
provider: manual-fallback
source_providers_attempted:
- falcon
- openai
status: provider_timeout_fallback
created_at: '2026-05-04T02:16:52Z'
disease_name: Cornelia de Lange syndrome
orpha_id: ORPHA:199
mondo_id: MONDO:0016033
cited_references:
- ORPHA:199
- PMID:15146185
- PMID:15146186
- PMID:23505322
- PMID:26701315
- PMID:19468298
- PMID:19763162
- PMID:25921057
- PMID:26581180
- PMID:29995837
---

# Cornelia de Lange Syndrome Research Fallback

Deep-research provider attempts were made after the ORPHA:199 direct
Orphanet/MONDO target was selected:

- `timeout 120 just research-disorder falcon Cornelia_de_Lange_Syndrome`
- `timeout 120 just research-disorder openai Cornelia_de_Lange_Syndrome`

Both commands printed the initial provider line, then stalled without producing
a research output file and were terminated by the timeout. The curation
therefore used the structured Orphanet cache plus fetched PubMed cache records
as the auditable evidence base.

## Literature Scope Checked

- `references_cache/ORPHA_199.md`: direct Orphanet leaf record for Cornelia de
  Lange syndrome, including definition, autosomal dominant and X-linked
  inheritance, exact MONDO and OMIM mappings, prevalence, age of onset,
  disease-gene assertions, and HPO phenotype rows.
- `references_cache/PMID_29995837.md`: international consensus statement
  supporting CdLS as a cohesin-complex gene disorder with intellectual
  disability, facial features, upper-limb anomalies, atypical growth, molecular
  diagnostics, and long-term management guidance.
- `references_cache/PMID_15146186.md`: human NIPBL gene-discovery evidence,
  including sporadic and familial CdLS cases and multisystem clinical
  manifestations.
- `references_cache/PMID_15146185.md`: NIPBL/delangin gene-discovery evidence
  connecting Scc2/Nipped-B homolog function to CdLS and limb-patterning
  defects.
- `references_cache/PMID_23505322.md`: human CdLS cohort evidence supporting
  frequent NIPBL somatic mosaicism and buccal swab DNA testing when blood
  testing is negative.
- `references_cache/PMID_26701315.md`: human NIPBL series supporting de novo
  heterozygous NIPBL variants, germline and somatic NIPBL mutations, and
  first-line buccal cell DNA analysis for diagnostic sensitivity.
- `references_cache/PMID_19468298.md`: human CdLS cell-line evidence for
  transcriptional dysregulation, cohesin regulatory-region binding, and
  phenotype-severity correlation.
- `references_cache/PMID_26581180.md`: SMC1A-mutant CdLS cell evidence that
  mutant cohesin affects RNA polymerase II regulation.
- `references_cache/PMID_19763162.md`: Nipbl heterozygous mouse-model evidence
  for multisystem defects and transcriptional dysregulation consistent with
  CdLS.
- `references_cache/PMID_25921057.md`: clinical management paper used only for
  the Bohring-Opitz syndrome differential diagnosis.

## Curation Conclusions

- Disease identity is the syndrome-level disorder `ORPHA:199`, exact to
  `MONDO:0016033` and `OMIM:122470`.
- The core disease mechanism is pathogenic variation in cohesin structural or
  regulatory genes, especially NIPBL, causing impaired cohesin loading,
  altered chromatin/regulatory-region binding, and developmental
  transcriptional dysregulation.
- Orphanet directly supports the curated phenotype profile, including
  synophrys, thick eyebrows, highly arched eyebrows, brachycephaly,
  microcephaly, micrognathia, high palate, long philtrum, downturned corners
  of mouth, short nose, depressed nasal bridge, anteverted nares, short neck,
  delayed eruption of teeth, generalized hirsutism, intellectual disability,
  hypertonia, anxiety, compulsive behaviors, attention deficit hyperactivity
  disorder, sleep abnormality, intrauterine growth retardation, short stature,
  delayed skeletal maturation, micromelia, small hand, toe syndactyly, short
  foot, oligodactyly, feeding difficulties, gastroesophageal reflux, hearing
  impairment, atresia of the external auditory canal, and ventricular septal
  defect.
- Evidence-backed management is supportive and multidisciplinary, with genetic
  counseling and molecular testing supported by the consensus statement,
  inheritance evidence, and buccal swab testing evidence for mosaic cases.
