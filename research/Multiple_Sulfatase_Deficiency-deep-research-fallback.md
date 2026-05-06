# Multiple sulfatase deficiency research fallback

## Provider attempts

- Falcon deep-research: initial call before YAML creation failed because the
  target disorder file did not yet exist; a bounded retry after YAML creation
  timed out after 75 seconds without producing an artifact.
- OpenAI deep-research: bounded attempt after YAML creation timed out after 75
  seconds without producing an artifact.
- Perplexity deep-research: skipped after bounded Falcon/OpenAI failures;
  curation proceeded from generated Orphanet, PubMed, and full-text caches.

## Literature scope used for curation

This fallback curation uses generated reference caches for ORPHA:585, primary
SUMF1/FGE mechanism papers (PMID:12757705, PMID:12757706), a full-text MSD
mechanism/clinical review (PMID:32414121), a systematic 80-case survey
(PMID:32620537), a complex-care consensus statement (PMID:29397290), an
ophthalmology literature review (PMID:36980153), a 2025 HCT case series
(PMID:39789203), and a 2025 preclinical AAV9/SUMF1 study (PMID:39870870).

## Curation synthesis

Multiple sulfatase deficiency is caused by biallelic SUMF1 variants affecting
formylglycine-generating enzyme, an ER protein required to activate cellular
sulfatases through post-translational FGly generation. Loss of FGE function
reduces multiple sulfatase activities, causing glycosaminoglycan and sulfatide
lysosomal storage, neurodegeneration, sensory involvement, ichthyosis,
hepatosplenomegaly, skeletal manifestations, and characteristic biochemical
findings. Established management is multidisciplinary and palliative/supportive;
HCT has limited human case-series evidence and AAV9/SUMF1 has preclinical
model-organism evidence.

## Key references

- ORPHA:585
- PMID:32414121
- PMID:32620537
- PMID:12757705
- PMID:12757706
- PMID:29397290
- PMID:36980153
- PMID:39789203
- PMID:39870870
