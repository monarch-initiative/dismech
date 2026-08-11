# IEMbase 0596: SLC25A26-related S-adenosylmethionine carrier deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 596 |
| Nosology | 11.1.05.01 |
| Gene | SLC25A26 |
| External IDs | OMIM:616794; ORPHA:466784 |
| Generated mapping | UNMAPPED; best candidate `Hyperornithinemia_Hyperammonemia_Homocitrullinuria_Syndrome.yaml` |
| Candidate DisMech targets | None exact |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents SLC25A26-related S-adenosylmethionine carrier deficiency,
also labelled combined oxidative phosphorylation deficiency 28 / COXPD28. The
record is autosomal recessive, classified under disorders of mitochondrial
shuttles and carriers, has unknown treatability, and has no treatment rows.

Biochemical rows include decreased muscle respiratory chain activity and
increased plasma pyruvate. Clinical rows include cardiopulmonary failure,
developmental delay, hydrops, perinatal death, lactic acidosis, and muscle
weakness.

## DisMech phenotype coverage

`Hyperornithinemia_Hyperammonemia_Homocitrullinuria_Syndrome.yaml` is a
false-positive carrier-family candidate. HHH syndrome models biallelic
SLC25A15/ORNT1 mitochondrial ornithine transport failure, a urea-cycle transport
disorder with hyperornithinemia, hyperammonemia, and homocitrullinuria. It does
not represent SLC25A26, mitochondrial S-adenosylmethionine transport, COXPD28,
respiratory-chain deficiency, hydrops, or perinatal lethal cardiopulmonary
failure.

Local mitochondrial OXPHOS entries provide broad context, but no exact
SLC25A26/SAM carrier deficiency target was identified.

## Concordance and completeness

Judgement: true local gap; reject HHH syndrome as exact coverage.

The generated match is driven by the SLC25 mitochondrial carrier family and
mitochondrial transport wording. Disease mechanism and biochemical readouts are
different: SAM carrier/OXPHOS deficiency versus ornithine carrier/urea-cycle
transport disease.

## Curation actions

- Create or identify an exact SLC25A26 / COXPD28 target before import.
- Reject `Hyperornithinemia_Hyperammonemia_Homocitrullinuria_Syndrome.yaml` as
  an exact mapping.
- Preserve respiratory-chain activity, pyruvate, lactic acidosis, hydrops,
  cardiopulmonary failure, perinatal death, developmental delay, and muscle
  weakness prompts.
