# Tangier Disease Deep Research Fallback

## Provider attempts

- `timeout 120 just research-disorder falcon Tangier_Disease`
  - Result: timed out after 120 seconds.
  - Terminal output ended with: `Recipe research-disorder was terminated by signal 15`.
  - No `research/Tangier_Disease-deep-research-falcon.md` file was produced.
- `timeout 120 just research-disorder openai Tangier_Disease`
  - Result: timed out after 120 seconds.
  - Terminal output ended with: `Recipe research-disorder was terminated by signal 15`.
  - No `research/Tangier_Disease-deep-research-openai.md` file was produced.

## Evidence scope used

The curation proceeded from generated Orphanet cache `ORPHA:31150` plus
validator-fetched PubMed caches for the core Tangier disease literature:

- `PMID:22913675` - epidemiology, pathophysiology, and management review.
- `PMID:31751110` - GeneReviews Tangier disease entry.
- `PMID:33994407` - current diagnosis and management review.
- `PMID:10431236`, `PMID:10431237`, `PMID:10431238` - independent 1999
  ABCA1/Tangier disease discovery papers.
- `PMID:10525055` and `PMID:11309399` - ABCA1 lipid-efflux functional
  studies.
- `PMID:7130397` and `PMID:162820` - classic HDL/apolipoprotein kinetics and
  tissue pathology studies.
- `PMID:27565770` - HDL deficiency diagnosis and treatment review.
- `PMID:39817629` - pediatric clinical presentation and genetic diagnosis
  cohort.

## Curation conclusion

The evidence consistently supports a canonical mechanism in which biallelic
ABCA1 pathogenic variants impair apoA-I-mediated cholesterol and phospholipid
efflux, blocking HDL particle formation and causing extremely low HDL-C/apoA-I.
Reduced cellular cholesterol export leads to cholesteryl ester accumulation in
reticuloendothelial tissues and Schwann cells, explaining orange tonsils,
hepatosplenomegaly, lymphadenopathy, corneal/skin/nail findings, and peripheral
neuropathy. Cardiovascular risk is variable but supported by reviews of reported
cases; treatment remains non-curative and focuses on modifiable cardiovascular
risk, supportive neuropathy care, tonsillectomy when obstructive, and genetic
counseling/family screening.
