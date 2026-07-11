# IEMbase 0123: HSD11B2-related 11-beta-Hydroxysteroid dehydrogenase 2 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 123 |
| Nosology | 24.2.21.01 |
| Gene | HSD11B2 |
| External IDs | OMIM:218030; ORPHA:320 |
| Generated mapping | CANDIDATE, medium confidence |
| Candidate DisMech targets | Generated candidate `46_XY_DSD_Due_to_17_Beta_Hydroxysteroid_Dehydrogenase_3_Deficiency.yaml`; no valid HSD11B2/apparent mineralocorticoid excess target found |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as HSD11B2-related 11-beta-hydroxysteroid dehydrogenase
2 deficiency, with alternate labels apparent mineralocorticoid excess and AME.
Treatability is marked unknown.

The characteristic biochemical rows are low potassium and a decreased urinary
tetrahydrocortisol/tetrahydrocortisone ratio. No clinical or treatment rows are
listed in the extract.

## DisMech phenotype coverage

The generated candidate points to
`46_XY_DSD_Due_to_17_Beta_Hydroxysteroid_Dehydrogenase_3_Deficiency.yaml`, but
that is an HSD17B3 androgen-biosynthesis disorder, not HSD11B2 apparent
mineralocorticoid excess. Its scope is 46,XY undervirilization from impaired
androstenedione-to-testosterone conversion.

No local standalone HSD11B2, apparent mineralocorticoid excess, or AME disease
target was found in the current DisMech disease set.

## Concordance and completeness

Judgement: false-positive generated candidate; current local disease gap.

The lexical overlap around hydroxysteroid dehydrogenase is misleading. HSD11B2
apparent mineralocorticoid excess is a cortisol-cortisone/mineralocorticoid
receptor protection disorder, whereas the generated candidate is a sex-steroid
conversion DSD. The IEMbase biochemical signal is sparse but points cleanly to
HSD11B2/AME and should not be mapped to HSD17B3 disease.

## Curation actions

- Reject the generated HSD17B3 DSD candidate for this IEMbase record.
- Treat HSD11B2-related apparent mineralocorticoid excess as an unmapped local
  disease gap.
- Future curation should add a standalone AME/HSD11B2 entry with hypokalemia,
  cortisol-cortisone metabolite-ratio abnormalities, mineralocorticoid
  hypertension physiology, and HSD11B2 mechanism.
