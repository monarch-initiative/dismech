# IEMbase 0765: ABHD12-related PHARC syndrome

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 765 |
| Nosology | 14.5.01.17 |
| Nosology code | IEM0674 |
| Gene | ABHD12 |
| External IDs | OMIM:612674; ORPHA:171848 |
| Generated mapping | UNMAPPED; weak candidate `PHARC_syndrome.yaml` |
| Candidate DisMech targets | `PHARC_syndrome.yaml` |
| Review date | 2026-07-08 |

## IEMbase phenotype signal

IEMbase labels this autosomal recessive record as ABHD12-related
polyneuropathy, hearing loss, ataxia, retinitis pigmentosa, and cataract
syndrome, with abbreviation PHARC. The source signal is concise and matches
the acronym: adult-predominant sensorineural deafness, peripheral demyelinating
neuropathy, cataract, cerebellar ataxia, and pigmentary retinopathy, with some
childhood or adolescent possible flags.

## DisMech phenotype coverage

`PHARC_syndrome.yaml` is the exact local target despite the generated unmapped
status. It carries the ABHD12 gene, MONDO PHARC identity, autosomal recessive
neurodegenerative description, ABHD12 lipid hydrolase loss, abnormal
lysophosphatidylserine signaling, microglial activation/neuroinflammation,
peripheral nerve degeneration, cerebellar degeneration, auditory pathway
degeneration, retinal degeneration, and phenotypes for peripheral neuropathy,
sensorineural hearing impairment, ataxia, retinitis pigmentosa, and cataract.

## Concordance and completeness

Judgement: false negative; exact local coverage exists.

The local PHARC entry is more complete mechanistically and covers all core
IEMbase phenotypes. IEMbase adds a compact age-coded emphasis on
adult-predominant hearing loss, neuropathy, and cataract, and uses
`peripheral demyelinating neuropathy` wording while local coverage uses broader
peripheral neuropathy / peripheral nerve degeneration.

## Curation actions

- Treat `PHARC_syndrome.yaml` as the exact mapping.
- Consider whether demyelinating neuropathy should be explicitly represented if
  supported by local evidence.
- Preserve the adult-predominant age pattern in future phenotype refinements.
