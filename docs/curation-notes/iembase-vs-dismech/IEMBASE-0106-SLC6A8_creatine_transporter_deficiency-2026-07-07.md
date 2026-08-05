# IEMbase 0106: SLC6A8-related creatine transporter deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 106 |
| Nosology | 5.3.04.01 |
| Gene | SLC6A8 |
| External IDs | OMIM:300352 |
| Generated mapping | CANDIDATE |
| Candidate DisMech targets | Generated candidate `AGAT_Deficiency.yaml` is false; correct target is `Creatine_Transporter_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as SLC6A8-related creatine transporter deficiency, with
alternate labels cerebral creatine deficiency syndrome type 1 and X-linked
creatine deficiency syndrome. Treatability is marked yes.

The characteristic biochemical row is increased urinary creatine/creatinine
ratio. Clinical rows are constipation and low muscle mass.

Treatments are arginine, creatine, and glycine.

## DisMech phenotype coverage

The generated CANDIDATE to `AGAT_Deficiency.yaml` is a false positive caused by
shared cerebral creatine deficiency wording. The correct local target is
`Creatine_Transporter_Deficiency.yaml`.

That entry covers X-linked SLC6A8-related creatine transporter deficiency,
impaired CRTR-mediated creatine uptake, cerebral creatine depletion, impaired
neuronal energy buffering, reduced brain creatine by MRS, global developmental
delay, intellectual disability, seizures, hypotonia, speech-language delay,
behavioral abnormalities, and occasional movement disorder. Its treatment
section captures creatine precursor supplementation with creatine, arginine, and
glycine, but explicitly notes that clinical improvement has not been proven
because the transporter defect limits CNS benefit.

## Concordance and completeness

Judgement: generated candidate is wrong, but a correct local standalone target
exists.

IEMbase is more explicit about the urinary creatine/creatinine ratio and adds
constipation and low muscle mass. DisMech is richer for the transporter-versus-
biosynthesis distinction, X-linked inheritance, reduced brain creatine by MRS,
neurodevelopmental phenotype surface, and treatment efficacy caveat.

## Curation actions

- Correct mapping to `Creatine_Transporter_Deficiency.yaml`.
- Do not map to `AGAT_Deficiency.yaml`.
- Consider adding urinary creatine/creatinine ratio as a structured biochemical
  readout and reviewing constipation/low muscle mass for future phenotype
  expansion.
