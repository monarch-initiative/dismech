# Angiostrongyliasis literature sweep

## Scope decision

The `stubs/Angiostrongyliasis.yaml` candidate maps to `MONDO:0019143`.
Although the common-language genus disease can include both *Angiostrongylus
cantonensis* neuroangiostrongyliasis and *Angiostrongylus costaricensis*
abdominal angiostrongyliasis, the MONDO/Orphanet row is the rat-lungworm,
*A. cantonensis*, eosinophilic-meningitis concept. The KB entry was therefore
narrowed to the foodborne *A. cantonensis* disease in which ingested larvae
migrate to and are retained in the central nervous system.

PMID:42860813 explicitly frames human angiostrongyliasis as a two-species set;
this entry uses that review only for *A. cantonensis* rat-lungworm scope and
foodborne third-stage larval ingestion. PMID:38446236 was reviewed for the
separate *A. costaricensis* abdominal syndrome but was excluded from the YAML so
that this exact `MONDO:0019143` Disease record does not mix species-localized
syndromes.

## PubMed evidence selected

- PMID:42860813 — current narrative review covering the two principal human
  Angiostrongylus species, ingestion of third-stage larvae in gastropod or
  paratenic hosts or on produce, and the neuroangiostrongyliasis versus
  abdominal split; used only for *A. cantonensis* scope and transmission in this
  narrowed rat-lungworm entry.
- PMID:37111510 — neuroangiostrongyliasis consensus/guideline paper defining
  rodent definitive hosts, mollusk intermediate hosts, paratenic hosts,
  accidental human infection, exposure, CSF eosinophilia, neurologic findings,
  confirmatory criteria, incubation, and management for *A. cantonensis*
  disease.
- PMID:31972289 — systematic review of imported European cases, used for
  concrete neuroangiostrongyliasis phenotype frequencies: headache in 90% of
  cases with data, paresthesia in half, eosinophilia in 89%, CSF eosinophilia in
  93%, and elevated CSF protein in 92%.

No species-specific MONDO child was created in this pass. If MONDO later adds
separate `Neuroangiostrongyliasis` or `Abdominal_Angiostrongyliasis` children,
downstream curators can promote this rat-lungworm record or add an
*A. costaricensis* abdominal sibling without having to untangle a mixed
mechanism graph.
