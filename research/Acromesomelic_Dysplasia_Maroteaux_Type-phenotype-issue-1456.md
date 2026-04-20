## Phenotype curation note for issue #1456

Target file: `kb/disorders/Acromesomelic_Dysplasia_Maroteaux_Type.yaml`

Scope:
- phenotype section only
- add missing clinically important phenotypes only when directly PMID-backed
- remove or soften unsupported frequency and wording

Primary human sources used:
- PMID:34162036 - nine-patient AMDM series; supports acromesomelic shortening with spondylar dysplasia
- PMID:35368703 - 2022 AMDM report; supports severe disproportionate short stature and short hands/feet, and notes normal intelligence
- PMID:34178199 - mild AMDM case with useful full-text radiographic detail
- PMID:32694885 - single-patient clinical and radiographic description
- PMID:30359775 - unrelated AMDM families with core limb-shortening phenotype

Changes justified by the literature:
- Removed unsupported `frequency: OBLIGATE` from short stature, acromesomelia, and brachydactyly because the accessible PMID-backed evidence did not directly support universal frequency.
- Added `Short Feet` from PMID:35368703 and PMID:34178199.
- Added `Lumbar Interpedicular Narrowing` from the radiographic description in PMID:34178199.
- Strengthened acromesomelic limb-shortening evidence with the nine-patient series (PMID:34162036).
- Softened wording where the literature was narrower than the previous text, including the cone-epiphysis description and the short-metacarpal description.
- Removed model-organism evidence from the human `Radial Bowing` phenotype entry to keep the section human-clinical and phenotype-focused.

Phenotypes considered but not promoted to standalone entries:
- elbow limitation
- genu varum
- frontal bossing / short nose
- broad fingers

Reason:
- available accessible PMID-backed evidence was indirect, review-like, or too inconsistent to support a clean standalone HPO-grounded entry without overclaiming.
