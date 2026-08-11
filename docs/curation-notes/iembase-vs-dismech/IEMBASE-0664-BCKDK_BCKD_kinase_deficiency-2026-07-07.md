# IEMbase 0664: BCKDK-related branched-chain ketoacid dehydrogenase kinase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 664 |
| Nosology | 1.3.06.01 |
| Nosology code | IEM0112 |
| Gene | BCKDK |
| External IDs | OMIM:614923; ORPHA:308410 |
| Generated mapping | MAPPED to `BCKDK_Deficiency.yaml` |
| Candidate DisMech targets | `BCKDK_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive BCKDK-related branched-chain ketoacid
dehydrogenase kinase deficiency.

The biochemical signature is decreased plasma isoleucine, leucine, and valine
across infancy, childhood, and adolescence. Clinical rows emphasize autism,
intellectual disability, delayed or abnormal speech, and possible seizures and
stereotyped hand movements.

## DisMech phenotype coverage

`BCKDK_Deficiency.yaml` is an exact local target. It models loss of the kinase
that normally phosphorylates and inhibits BCKDH, causing constitutive BCKDH
activation, excessive branched-chain amino-acid catabolism, and low plasma/CSF
leucine, isoleucine, and valine.

The local phenotype set includes autistic behavior, intellectual disability,
global developmental delay, epileptic encephalopathy, seizures, microcephaly,
and the biochemical low-BCAA pattern. It also records BCAA-enriched nutritional
support and related treatment cautions.

## Concordance and completeness

Judgement: exact high-concordance mapping.

IEMbase and DisMech agree on the inverse MSUD-like biochemical direction:
BCKDK loss lowers BCAAs rather than increasing them. DisMech is richer for
mechanism and treatment. IEMbase adds row-level reminders for delayed or absent
speech and stereotyped hand movements that should be checked before claiming
phenotype completeness.

## Curation actions

- Keep `BCKDK_Deficiency.yaml` as the disease-level target.
- Preserve low leucine, isoleucine, and valine as the defining biochemical
  signature.
- Review whether speech abnormality and stereotyped hand movements are captured
  explicitly enough in the local phenotype model.
- Keep this separate from MSUD and PPM1K mild MSUD despite shared BCKDH pathway
  biology.
