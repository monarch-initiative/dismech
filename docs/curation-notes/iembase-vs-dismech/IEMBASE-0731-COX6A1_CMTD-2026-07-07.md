# IEMbase 0731: COX6A1-related cytochrome c oxidase subunit 6A1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 731 |
| Nosology | 7.4.05.02 |
| Nosology code | IEM0466 |
| Gene | COX6A1 |
| External IDs | OMIM:616039; ORPHA:435998 |
| Generated mapping | UNMAPPED; weak candidate `COX6A2-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | No exact COX6A1/CMTD target identified |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive COX6A1-related cytochrome c oxidase
subunit 6A1 deficiency. The alternate-name field identifies recessive
intermediate Charcot-Marie-Tooth disease type D. The cached rows are sparse but
specific: adult hearing loss and polyneuropathy that begins in childhood and is
strongest in adulthood.

## DisMech phenotype coverage

No exact COX6A1 or recessive intermediate Charcot-Marie-Tooth disease type D
local target was identified.

The generated `COX6A2-Related_COX_Deficiency.yaml` candidate is not exact
coverage. COX6A2 is the striated-muscle isoform of cytochrome c oxidase subunit
VIa and causes a muscle-specific complex IV deficiency with weakness,
hypotonia, and sometimes cardiomyopathy. COX6A1 is a different isoform and the
IEMbase record is a neuropathy/CMTD phenotype. Local Charcot-Marie-Tooth files
provide broad neuropathy context only, not COX6A1-specific disease coverage.

## Concordance and completeness

Judgement: true local COX6A1/CMTD gap. The COX6A2 candidate should be rejected
as exact coverage.

The shared complex IV subunit-family language is not enough to map across
COX6A1 and COX6A2. IEMbase points to a neuropathy-dominant CMTD entity, whereas
the local COX6A2 entry is a muscle-specific COX deficiency.

## Curation actions

- Add a dedicated COX6A1/recessive intermediate Charcot-Marie-Tooth disease type
  D target if curated.
- Reject `COX6A2-Related_COX_Deficiency.yaml` as exact coverage.
- Preserve adult hearing loss and childhood-to-adult polyneuropathy.
- Use generic CMT content only as broad context, not as a resolved exact target.
