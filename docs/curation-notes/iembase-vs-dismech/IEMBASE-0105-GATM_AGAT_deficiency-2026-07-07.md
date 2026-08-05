# IEMbase 0105: GATM-related arginine:glycine amidinotransferase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 105 |
| Nosology | 5.3.01.01 |
| Gene | GATM |
| External IDs | OMIM:612718 |
| Generated mapping | MAPPED |
| Candidate DisMech targets | `AGAT_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as GATM-related arginine:glycine amidinotransferase
deficiency, with alternate labels AGAT and cerebral creatine deficiency syndrome
type 3. Treatability is marked yes.

The characteristic biochemical rows are markedly decreased brain creatine,
low-to-normal urinary creatine/creatinine ratio, markedly decreased
guanidinoacetic acid in CSF, plasma, and urine. Clinical rows are cerebral
creatine deficiency and myopathy.

Treatment is creatine.

## DisMech phenotype coverage

The generated mapping to `AGAT_Deficiency.yaml` is correct. The local entry
covers biallelic GATM variants, reduced glycine amidinotransferase activity,
reduced guanidinoacetate and creatine biosynthesis, cerebral creatine depletion,
peripheral creatine depletion, and treatable myopathy.

Phenotype and biochemical coverage includes global developmental delay,
cognitive impairment, speech-language delay, muscle weakness, myopathy,
hypotonia, reduced brain creatine by MRS, reduced tissue AGAT activity, reduced
circulating creatine, decreased urinary guanidinoacetic acid, decreased serum
and urinary creatinine, and occasional seizures or behavioral findings.
Treatment coverage includes creatine monohydrate supplementation.

## Concordance and completeness

Judgement: correct mapping with high concordance.

IEMbase is more explicit about CSF, plasma, urine, and brain compartments and
about the urinary creatine/creatinine ratio. DisMech is richer for molecular
mechanism, peripheral myopathy mechanism, treatment timing, and broader
developmental phenotype coverage.

## Curation actions

- Keep `AGAT_Deficiency.yaml` as the canonical target.
- Consider adding a structured urinary creatine/creatinine ratio biomarker if
  biomarker normalization work continues.
- No mapping correction needed.
