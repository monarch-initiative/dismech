# Mucolipidosis Type III Alpha/Beta Deep Research Fallback

## Provider Attempts

- 2026-05-08T04:39Z: `just research-disorder openai Mucolipidosis_Type_III_Alpha_Beta`
  was attempted before the YAML existed and failed immediately because the
  disorder file was not found.
- 2026-05-08T04:53Z: `just research-disorder openai Mucolipidosis_Type_III_Alpha_Beta`
  started after YAML creation but produced no output during the bounded wait.
  The provider process did not accept stdin interrupt through the session, so
  the process tree was terminated with SIGTERM.

No provider-generated deep-research narrative was available within the bounded
runtime. Curation proceeded from regenerated Orphanet structured evidence and
fetched PubMed/DOI caches, without creating or hand-editing any
`references_cache/*.md` files.

## Evidence Scope Used

- ORPHA:423461 for the exact disease record, MONDO and OMIM mappings,
  autosomal recessive inheritance, GNPTAB disease-gene association,
  epidemiology, and all structured HPO phenotype frequency rows.
- PMID:20301730 for diagnostic enzyme testing, GNPTAB sequencing, management,
  surveillance, inheritance, and genetic counseling snippets, with the YAML
  noting that the cached GeneReviews chapter is archival/retired.
- DOI:10.1136/jmg.2009.067736 and PMID:19197337 for GNPTAB causation,
  phosphotransferase deficiency, and residual-activity genotype-phenotype
  framing.
- PMID:20367762 for natural history, lysosomal hydrolase disparity, skeletal
  radiographic changes, dysostosis multiplex, and osteodystrophy.
- PMID:21466370 for autopsy and histopathology evidence covering lysosomal
  granular storage in multiple organs, cartilage, bone, and cardiac valve
  pathology.
- PMID:29704188, PMID:10472261, PMID:12705498, and PMID:32818557 for adult
  skeletal disease, orthopedic intervention, physical therapy, pamidronate, and
  cardiac involvement.
- PMID:30208878 for a GNPTAB-confirmed ML III alpha/beta case report and
  diagnostic use of enzyme and genetic testing.

## Curation Conclusions

The curated model is biallelic GNPTAB pathogenic variation causing reduced
UDP-N-acetylglucosamine-1-phosphotransferase activity. Loss of the
mannose-6-phosphate recognition marker prevents efficient lysosomal targeting
of hydrolases, leading to extracellular hydrolase leakage, intracellular
lysosomal storage, and a multisystem but attenuated ML III phenotype. The most
evidence-backed clinical axis is skeletal and joint degeneration, with
secondary cardiac-valve, biochemical, ENT/hearing, growth, and mild cognitive
manifestations. Current management in the cached literature is supportive and
complication-directed, including physical therapy, orthopedic/carpal tunnel
surgery, pamidronate for bone pain in limited human evidence, surveillance, and
genetic counseling.
