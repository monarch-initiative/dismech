# Aicardi-Goutieres Syndrome Deep Research Fallback

## Provider Attempts

- `timeout 120 just research-disorder falcon Aicardi_Goutieres_Syndrome`
  timed out and was terminated by `timeout` with exit code 124.
- `timeout 120 just research-disorder openai Aicardi_Goutieres_Syndrome`
  timed out and was terminated by `timeout` with exit code 124.

## Evidence Scope Integrated

The curation proceeded from generated ORPHA:51 structured data and targeted
PubMed evidence cached with `just fetch-reference`. The YAML integrates:

- ORPHA:51 disease identity, MONDO exact mapping, autosomal dominant/recessive
  inheritance, current AGS genes, onset categories, and HPO frequency rows.
- GeneReviews PMID:20301648 for clinical characteristics, diagnosis/testing,
  genetic counseling, supportive management, and surveillance.
- Discovery and cohort papers for TREX1, RNASEH2A/B/C, SAMHD1, ADAR, IFIH1,
  LSM11, and RNU7-1 mechanisms: PMID:16845398, PMID:16845400, PMID:17846997,
  PMID:25604658, PMID:31130681, PMID:31559893, PMID:33230297, and
  PMID:35320431.
- Human treatment evidence for JAK inhibition and reverse-transcriptase
  inhibitor trials: PMID:32877590, PMID:30666809, PMID:33721182,
  PMID:30566312, PMID:39630935, and the clinical-spectrum treatment review
  PMID:36650407.

## Curation Notes

No provider-generated deep-research narrative was available within the bounded
runtime. The YAML therefore uses only exact snippets from ORPHA/PubMed reference
caches and avoids unsupported treatment claims. JAK inhibition is represented as
emerging mechanism-targeted therapy with human open-label/case evidence, while
reverse-transcriptase inhibition is represented as investigational with mixed
trial evidence.
