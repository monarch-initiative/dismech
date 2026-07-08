# IEMbase 0750: LPIN1-related lipin 1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 750 |
| Nosology | 14.4.03.01 |
| Nosology code | IEM0657 |
| Gene | LPIN1 |
| External IDs | OMIM:268200; ORPHA:99845 |
| Generated mapping | UNMAPPED; weak candidate `Autosomal_Recessive_Multiple_Pterygium_Syndrome.yaml` |
| Candidate DisMech targets | None exact; phenotype overlap with several rhabdomyolysis disorders |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase labels this autosomal recessive record as LPIN1-related lipin 1
deficiency, with alternate name acute recurrent autosomal recessive
myoglobinuria. The source signal is centered on severe recurrent
rhabdomyolysis: very high plasma creatine kinase and urinary myoglobin, muscle
cramps, myoglobinuria, episodic or exercise-induced rhabdomyolysis, acute renal
failure, and possible death. Most findings are present from childhood through
adulthood, with possible infantile flags.

## DisMech phenotype coverage

No exact LPIN1 / recurrent rhabdomyolysis entry is present locally. Several
DisMech diseases carry rhabdomyolysis, myoglobinuria, or exercise intolerance
phenotypes, including fatty acid oxidation and glycogen storage disorders, but
those are different gene-disease entities.

The generated `Autosomal_Recessive_Multiple_Pterygium_Syndrome.yaml` candidate
is a false positive. That entry concerns CHRNG-related fetal akinesia,
contractures, and pterygia rather than LPIN1 phosphatidic acid phosphatase
deficiency or recurrent rhabdomyolysis.

## Concordance and completeness

Judgement: true local gap.

The IEMbase record provides a compact but strong phenotype and biochemical
profile for LPIN1 deficiency. Existing rhabdomyolysis entries should be used as
comparison context only; they do not cover LPIN1 disease identity.

## Curation actions

- Add a distinct LPIN1 / lipin 1 deficiency target before treating this
  IEMbase disease as covered.
- Reject `Autosomal_Recessive_Multiple_Pterygium_Syndrome.yaml` as exact
  coverage.
- Preserve CK elevation, myoglobinuria, exercise-induced or episodic
  rhabdomyolysis, acute renal failure, and death as high-priority curation
  prompts.
