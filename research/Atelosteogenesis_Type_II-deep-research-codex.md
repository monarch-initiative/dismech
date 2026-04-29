# Atelosteogenesis Type II phenotype curation notes

Date: 2026-04-19
Curator: Codex
Scope: phenotype section only for `kb/disorders/Atelosteogenesis_Type_II.yaml`

## Sources used

- PMID:20301493, *SLC26A2-Related Atelosteogenesis.*
- PMID:1279661, *Atelosteogenesis type II: sonographic and radiological correlation.*
- PMID:3799721, *de la Chapelle dysplasia.*
- PMID:7632220, *De la Chapelle dysplasia (atelosteogenesis type II): case report and review of the literature [corrected].*

## Phenotypes added or tightened

- Added `Micromelia` from PMID:1279661.
- Added `Midface retrusion`, `Epicanthus`, `Ulnar deviation of the hand or of fingers of the hand`, and `Sandal gap` from PMID:20301493.
- Added `Coronal cleft vertebrae` and `Cervical kyphosis` from PMID:1279661.
- Added `Bowing of the long bones` and `Laryngeal stenosis` from PMID:3799721.
- Softened unsupported wording such as `hallmark`, `commonly`, and `frequent` in free-text descriptions where the cited abstracts did not make a frequency claim.

## Claims considered but not added

- `Protuberant abdomen` is present in the GeneReviews text, but I did not add it because I did not confirm a clean, repo-validated HPO mapping during this pass.
- `Metaphyseal and epiphyseal abnormalities`, `horizontal sacrum`, and `additional ossification centres in the pelvis` are clearly described in PMID:1279661, but I did not add them without a more confident term choice.
- `Ulna/fibula hypoplasia` is described in PMID:3799721, but the abstract wording supports severe reduction rather than a clean absent-versus-hypoplastic distinction, so I left it out rather than overstate the ontology mapping.

## Frequency and onset

- No new `frequency` values were added.
- No `onset` values were added.
- Although prenatal detection is reported in PMID:1279661, I left onset unset because the abstracts here more clearly support prenatal detectability than a disease-wide onset annotation policy for individual phenotypes.
