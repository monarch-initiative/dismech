## Leri-Weill Dyschondrosteosis phenotype curation notes

Date: 2026-04-18
Issue: #1483
Scope: phenotype section only for `kb/disorders/Leri-Weill_Dyschondrosteosis.yaml`

### Primary phenotype papers used

| PMID | Cohort / source | Phenotype signals used in curation |
| --- | --- | --- |
| 11739418 | 21 LWD families / 43 affected individuals with confirmed SHOX abnormalities | Madelung deformity present in 74% of children and adults; female predominance; high-arched palate and scoliosis reported in the LWD cohort. |
| 10599728 | 14 Japanese patients with SHOX-region haploinsufficiency | Mesomelia/LWD phenotype in 10/14; short 4th metacarpals and/or cubitus valgus; skeletal lesions worse with age and in females. |
| 17182655 | Multinational cohort of 1608 short children screened for SHOX defects | Short forearm/lower leg, cubitus valgus, Madelung deformity, high-arched palate, and muscular hypertrophy discriminate SHOX-deficient children from non-SHOX short stature controls. |
| 14557470 | School-age SHOX-haploinsufficient children with auxology/radiography | Lower extremity-trunk ratio; characteristic LWD wrist radiographic signs including triangularization of the distal radial epiphysis, pyramidalization of the distal carpal row, and lucency of the distal ulnar border of the radius. |
| 20301394 | GeneReviews | Core LWD triad; mesomelia may be evident in school age; Madelung deformity usually appears in mid-to-late childhood and is more severe in females. |
| 25110390 | Review anchored in SHOX-deficiency skeletal pathology | Characteristic auxological disproportion in LWD; impaired growth of radius/ulna/tibia/fibula; wrist pain and limited motion as symptomatic consequences of Madelung deformity. |
| 32295321 | 15 Turkish patients with SHOX variants/deletions (4 LMD, remainder LWD-compatible) | Short forearm, cubitus valgus, and muscular hypertrophy listed among the most common phenotypes. |
| 33143726 | 296 children with growth impairment or skeletal disproportion screened for SHOX deficiency | Increased sitting height/height ratio and decreased arm span/height ratio as the strongest auxological indicators; useful to support disproportionate growth pattern. |

### Curation decisions

- Kept an explicit `frequency:` only for Madelung deformity because PMID:11739418 directly reports `74%`, which maps to `FREQUENT`.
- Removed unsupported frequency bands from mesomelia, short forearm, short tibia, wrist limitation, cubitus valgus, high palate, short 4th metacarpal, and scoliosis.
- Replaced generic `Short stature` with `Disproportionate short stature` to better reflect the evidence-backed auxological pattern in LWD.
- Added `Wrist pain` because PMID:25110390 explicitly describes it as a clinical manifestation of Madelung deformity.
- Added `Muscle hypertrophy` because it is repeatedly reported as a recurrent SHOX-deficiency/LWD-compatible feature in PMIDs 17182655 and 32295321.
- Tightened `Bowing of the forearm bones` to `Radial bowing` for a more specific ontology mapping.
- Did not add separate radiographic phenotypes such as triangularization of the distal radial epiphysis or pyramidalization of the carpal row in the YAML because the ontology mapping was not obviously clean enough for a specific, validator-safe phenotype term in this pass.

### Validation expectations

- New phenotype PMIDs requiring cache refresh: 14557470, 32295321, 33143726.
- All snippets selected for YAML are abstract-safe except PMID:25110390, which already has a cached full-text-derived reference in this repo and was reused only with exact text already present in the cache.
