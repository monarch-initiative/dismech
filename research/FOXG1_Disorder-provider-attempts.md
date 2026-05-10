# FOXG1 Disorder Provider Attempts

Date: 2026-05-10

Deep-research attempts were run through the repository `just research-disorder`
workflow:

- `falcon`: started with `just research-disorder falcon FOXG1_Disorder`, produced
  no substantive output after two bounded polling intervals, and was terminated
  to avoid a long silent wait.
- `openai`: started with `just research-disorder openai FOXG1_Disorder`,
  likewise produced no substantive output after two bounded polling intervals,
  and was terminated.
- `asta`: completed successfully and generated
  `research/FOXG1_Disorder-deep-research-asta.md` plus citations.

The final curation uses the completed Asta retrieval artifact together with
targeted PubMed, GeneReviews, Orphanet, and ClinicalTrials.gov evidence.
