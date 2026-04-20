## Osteogenesis Imperfecta Type VII phenotype curation notes

Date: 2026-04-19
Target file: `kb/disorders/Osteogenesis_Imperfecta_Type_VII.yaml`
Scope: phenotype section only

### Primary phenotype sources reviewed

- PMID:12110406 - founding eight-person Quebec cohort; strongest source for
  fractures at birth, bluish sclerae, lower-extremity deformity, coxa vara,
  osteopenia, and rhizomelia.
- PMID:19895918 - human OI type VII childhood cohort; supports impaired growth.
- PMID:18566967 - recessive CRTAP/LEPRE1 OI cohort; supports extremely low bone
  mineral density and "popcorn" epiphyses in the severe neonatal/surviving
  spectrum.
- PMID:38214665 - 2024 CRTAP paper; strongest recent source for early-onset
  recurrent fractures, severe osteoporosis, and bone deformities.
- PMID:35970273 - focused craniofacial study in two girls with CRTAP-related OI;
  supports platybasia and wormian bones.
- PMID:41064055 - 2025 clinical-variability paper; supports prenatal-vs-postnatal
  fracture variability and a cautious ocular expansion (high myopia with
  bilateral retinal detachment in one patient).

### Key phenotype decisions

- Softened `Severe short stature` to `Growth Delay` because the cited evidence
  supported impaired growth, not a uniform severe-short-stature claim.
- Removed unsupported `white sclerae` wording from the top description; retained
  `Blue sclerae` only because the founding abstract explicitly reports bluish
  sclerae.
- Added phenotype entries for osteoporosis, skeletal deformities, popcorn
  epiphyses, wormian bones, platybasia, high myopia, and retinal detachment.
- Kept ocular findings explicitly cautious because the 2025 paper reports them
  in one patient rather than as a core defining feature.

### Claims deliberately not added

- Dentinogenesis imperfecta exclusion: the 2022 craniofacial abstract reports
  absence in two girls only, which is too narrow to encode as a disorder-level
  excluded phenotype.
- Class III malocclusion / crossbite: clinically real in the 2022 abstract, but
  I did not add them because I could not quickly establish a clean, specific HPO
  mapping with the same confidence as the retained terms.
- Narrow chest, crumpled long bones, white/light-blue sclerae, and similar
  lethal-neonatal details from figures/full text were left out because this pass
  was constrained to abstract-validated PMID evidence.
