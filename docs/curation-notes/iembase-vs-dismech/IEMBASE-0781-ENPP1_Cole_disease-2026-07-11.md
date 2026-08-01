# IEMbase 0781: ENPP1-related Cole disease

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 781 |
| Nosology | 16.3.13.01 |
| Nosology code | IEM0038 |
| Gene | ENPP1 |
| External IDs | OMIM:615522; ORPHA:324561 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | No exact local target; reject `Arterial_Calcification_of_Infancy.yaml` |
| Review date | 2026-07-11 |

## IEMbase phenotype signal

IEMbase labels this autosomal dominant record as ENPP1-related
ectonucleotide pyrophosphatase-phosphodiesterase 1 dimerization deficiency,
with alternate name Cole disease and abbreviation COLED. The phenotype signal
is dominated by dermatologic and ectopic-calcification findings:
hyperkeratotic papules, hypopigmented macules, punctate palmoplantar
keratoderma, calcinosis cutis, and calcific tendinopathy.

## DisMech phenotype coverage

`Arterial_Calcification_of_Infancy.yaml` contains extensive ENPP1 coverage, but
that entry is a recessive generalized arterial calcification of infancy model.
It represents biallelic ENPP1 loss of function, infantile arterial
calcification and stenosis, PPi/FGF23/rickets biology, hearing loss, and
survivor complications. It does not model dominant Cole disease or the
dimerization-defect skin phenotype.

## Concordance and completeness

Judgement: true local gap.

The shared ENPP1 gene is not enough to treat the GACI entry as coverage. The
inheritance, disease entity, clinical distribution, and primary phenotype set
are different: Cole disease is represented here as an autosomal dominant
cutaneous/soft-tissue mineralization disorder, whereas the local ENPP1 target
is an autosomal recessive infantile arterial calcification disorder.

## Curation actions

- Keep IEMbase 0781 unmapped for now; do not collapse Cole disease into
  ENPP1-related GACI.
- Future curation should create a distinct ENPP1/Cole disease entry or subtype
  only if the project decides that dominant ENPP1 dimerization deficiency is in
  scope as a separate DisMech entity.
- Preserve the IEMbase prompts for palmoplantar keratoderma, hypopigmented
  macules, hyperkeratotic papules, calcinosis cutis, and calcific tendinopathy.
