# Fucosidosis Deep Research Fallback

## Provider Attempts

- 2026-05-04T15:50Z: `just research-disorder falcon Fucosidosis --max-tokens 6000`
  failed before provider execution because this deep-research-client version does
  not accept `--max-tokens`.
- 2026-05-04T15:51Z: `just research-disorder falcon Fucosidosis`
  produced no output after startup during the bounded wait and did not respond
  to stdin interrupt, so the provider process was terminated with SIGTERM.
- 2026-05-04T15:53Z: `just research-disorder openai Fucosidosis`
  also produced no output after startup during the bounded wait and was
  terminated with SIGTERM.

No provider-generated deep-research narrative was available within the bounded
runtime. Curation therefore proceeded from generated structured Orphanet
evidence and fetched PubMed caches, without hand-editing any
`references_cache/*.md` files.

## Evidence Scope Used For Curation

- ORPHA:349 structured record for the disease definition, exact MONDO and OMIM
  mappings, autosomal recessive inheritance, FUCA1 disease-gene association,
  epidemiology, age of onset, and all structured HPO phenotype rows.
- PMID:33266441 for the detailed human clinical review and case series covering
  FUCA1 genetics, alpha-L-fucosidase deficiency, fucose-rich substrate storage,
  phenotype frequencies, diagnostic approach, supportive care, and HSCT
  experience.
- PMID:39796208 for a recent review summarizing the FUCA1-to-enzyme-deficiency
  mechanism, lysosomal substrate accumulation, neuroinflammation, neuronal loss,
  and investigational treatment landscape.
- PMID:1873910 for patient lymphoid-cell evidence of markedly reduced
  alpha-L-fucosidase protein and catalytic activity.
- PMID:27491075 for a Fuca1-deficient mouse model showing lysosomal storage,
  enlarged CNS lysosomal compartments, neuroinflammation, Purkinje-cell loss,
  astrogliosis, and behavioral deficits.
- PMID:26537923 for the canine fucosidosis enzyme-replacement experiment showing
  CNS neuropathology, oligodendrocyte loss, hypomyelination, and partial
  neuropathologic improvement after intracisternal recombinant enzyme.
- PMID:11360116 for human unrelated donor bone marrow transplantation follow-up
  showing rising enzymatic levels and improved psychomotor development.
- PMID:27491218 for the fucosidosis therapy-development review describing
  supportive care limitations and hematopoietic transplant as the available
  disease-course-delaying intervention.
- PMID:38053939 for long-term adult sibling follow-up documenting clinical
  heterogeneity, slow neurologic deterioration, ataxia, angiokeratomas, and
  FUCA1 molecular diagnosis.

## Curation Conclusions

The accepted disease model is biallelic FUCA1 pathogenic variation causing
lysosomal alpha-L-fucosidase deficiency. The enzyme defect blocks degradation of
fucosylated glycoproteins, glycosphingolipids, and oligosaccharides, producing
lysosomal storage in neural, visceral, and cutaneous tissues. CNS storage causes
lysosomal expansion, secondary storage, neuroinflammation, neuronal loss,
oligodendrocyte loss, and hypomyelination, which explain progressive
developmental impairment, severe intellectual disability, seizures, spasticity,
and hearing impairment. Visceral and cutaneous storage contributes to
hepatomegaly, hyperhidrosis, hyperkeratosis, and vascular skin lesions. Current
management is mainly supportive, while carefully selected early hematopoietic
stem cell transplantation has limited human evidence for enzyme restoration and
clinical stabilization or improvement. Enzyme replacement remains preclinical in
the available evidence.
