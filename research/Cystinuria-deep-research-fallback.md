---
disorder: Cystinuria
provider: fallback
status: provider_failure_fallback
created: "2026-05-05T16:14:27Z"
attempts:
- provider: falcon
  command: just research-disorder falcon Cystinuria
  attempted_at: "2026-05-05T15:30:00Z"
  result: interrupted_after_bounded_silent_wait_no_artifact
- provider: openai
  command: just research-disorder openai Cystinuria
  attempted_at: "2026-05-05T16:00:00Z"
  result: connection_error_no_artifact
- provider: openscientist
  command: just research-disorder openscientist Cystinuria
  attempted_at: "2026-05-05T16:05:00Z"
  result: interrupted_after_bounded_silent_wait_no_artifact
evidence_scope: generated Orphanet and fetched PubMed/ClinicalTrials.gov caches
---

# Cystinuria Deep Research Fallback

## Provider Attempts

- 2026-05-05T15:30Z: `just research-disorder falcon Cystinuria`
  produced no artifact after a bounded silent wait and was interrupted.
- 2026-05-05T16:00Z: `just research-disorder openai Cystinuria`
  failed with an OpenAI connection error and produced no artifact.
- 2026-05-05T16:05Z: `just research-disorder openscientist Cystinuria`
  produced no artifact after a bounded silent wait and was interrupted.

No provider-generated deep-research narrative was available within the bounded
runtime. Curation therefore proceeded from generated structured Orphanet
evidence and fetched PubMed/ClinicalTrials.gov caches, without hand-editing any
`references_cache/*.md` files.

## Evidence Scope Used For Curation

- ORPHA:214 structured record for definition, inheritance, exact MONDO/OMIM
  mapping, prevalence bands, and HPO phenotype frequencies.
- ORPHA:93612 and ORPHA:93613 structured subtype records for Cystinuria type A
  and type B, including MONDO mappings, inheritance, and SLC3A1/SLC7A9 gene
  assertions.
- PMID:22480232 and PMID:20517292 for the renal b(0,+) transporter mechanism,
  SLC3A1/SLC7A9 subunits, proximal-tubule reabsorption failure, cystine
  precipitation, inheritance patterns, and clinical framing.
- PMID:18752446 and PMID:24045899 for human mutation cohorts, genetic
  heterogeneity, and synergistic/digenic diagnostic complexity.
- PMID:30515543 for detailed clinical burden, pediatric stone contribution,
  CKD risk, recurrence/procedure burden, transporter structure, current
  therapies, mouse models, crystal growth/aggregation, and investigational
  cystine-analog approaches.
- PMID:32066273 and PMID:36900678 for consensus/guideline treatment pathways:
  high fluid intake, dietary modification, urinary alkalinization,
  cystine-binding thiol drugs, and monitoring with cystine capacity.
- PMID:28165480 for alpha-lipoic acid model evidence increasing urinary cystine
  solubility and suppressing stone growth in Slc3a1 knockout mice.
- PMID:35822468 for pediatric overview, monogenic stone-disease burden, CKD
  framing, and alpha-lipoic acid as an emerging medical option.
- PMID:38814457 for long-term ureteroscopic/endoscopic management outcomes.
- ClinicalTrials.gov NCT02910531 and NCT03663855 for alpha-lipoic acid and
  tiopronin clinical trial context.

## Curation Conclusions

Cystinuria is a monogenic renal tubular aminoaciduria caused primarily by
pathogenic variants in SLC3A1 or SLC7A9, which encode the rBAT heavy subunit
and b(0,+)AT light subunit of the cystine/dibasic amino acid transporter. Loss
or reduction of transporter function impairs proximal tubular reabsorption of
filtered cystine, ornithine, lysine, and arginine. Cystine is the least soluble
of these amino acids, so high urinary cystine drives cystine crystalluria and
recurrent cystine nephrolithiasis. Recurrent stones and procedures can cause
obstruction, renal injury, chronic kidney disease, and hypertension.

Disease-directed management focuses on lowering urinary cystine supersaturation:
high urine volume, dietary sodium/protein moderation, urinary alkalinization,
and cystine-binding thiol drugs such as tiopronin or D-penicillamine when
conservative measures fail. Surgical/endoscopic stone removal remains necessary
for symptomatic or large stones. Alpha-lipoic acid and cystine crystal-growth
inhibitors remain investigational in the cited evidence.
