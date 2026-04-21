# Kniest Dysplasia Phenotype Curation Notes

Date: 2026-04-18

Scope: targeted phenotype-section cleanup for `kb/disorders/Kniest_Dysplasia.yaml`.

## Main phenotype sources used

- `PMID:10406661` supports the core overview phenotype: short trunk and limbs, kyphoscoliosis, midface hypoplasia, severe myopia, and hearing loss.
- `PMID:25592122` provides the strongest disease-specific ophthalmic series and also supports enlarged joints with restricted mobility, marked hand arthropathy, clefting abnormalities, hearing impairment, abnormal vitreous architecture, high myopia, and retinal detachment risk.
- `PMID:40475174` supports narrow thorax, short extremities, short stature, cleft palate, platyspondyly, coronal clefts, and dumbbell-shaped long bones in an infant with molecularly confirmed disease.
- `PMID:41378240` supports adult short stature, cataract, retinal detachment, kyphoscoliosis, and epiphyseal enlargement.
- `PMID:2931448` supports abnormal odontoid morphology and craniofacial retrusion.
- `PMID:27303468` supports clubfoot and radial head dislocation as reported radiographic associations in a 4-patient Kniest series.
- `PMID:14644246` supports retinal detachment in an adolescent patient.
- `PMID:7700721` supports cleft palate and progressive arthropathy as classic Kniest manifestations.

## Curatorial decisions

- Added missing clinically important phenotypes: hand arthropathy, narrow thorax, cataract, clubfoot, and radial head dislocation.
- Replaced the unsupported `Malar Flattening` entry with PMID-backed `Midface Hypoplasia`.
- Kept odontoid involvement but rewrote it to direct Kniest evidence instead of mixed-COL2A1 cohort frequencies.
- Removed the weak `Coxa Vara` phenotype because the cited evidence did not actually support a Kniest-specific coxa vara claim.
- Removed or softened mixed-cohort frequency/onset statements for myopia, retinal detachment, hearing loss, and odontoid hypoplasia unless directly supported by Kniest-specific abstracts.
