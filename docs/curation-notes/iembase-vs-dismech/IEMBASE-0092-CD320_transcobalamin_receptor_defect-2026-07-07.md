# IEMbase 0092: CD320-related transcobalamin receptor defect

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 92 |
| Nosology | 21.9.06.01 |
| Gene | CD320 |
| External IDs | OMIM:613646 |
| Generated mapping | UNMAPPED; best fuzzy candidate `Methylmalonic_Acidemia.yaml` |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive CD320-related transcobalamin
receptor defect, with alternate labels TCR/CD320 defect, TCR, and methylmalonic
acidemia TCblR type. Treatability is marked unknown, although hydroxocobalamin
is listed as a treatment row.

The characteristic clinical row is "No consistent clinical picture".

The biochemical signal is narrow: characteristic urinary methylmalonic acid,
with total plasma homocysteine also represented in the biochemical panel.

## DisMech phenotype coverage

There is no exact DisMech disease entry or subtype for CD320/transcobalamin
receptor deficiency.

`Methylmalonic_Acidemia.yaml` is a false-positive fuzzy candidate. It covers
isolated methylmalonic acidemia caused by MMUT and adenosylcobalamin-handling
defects such as MMAA and MMAB, but it does not model CD320-mediated cellular
uptake of transcobalamin-bound cobalamin.

`Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml` is mechanistically
nearer because it includes cellular uptake and transport defects, but its
subtypes list TCN2, LMBRD1, ABCD4, and intracellular cobalamin groups rather
than CD320.

## Concordance and completeness

Judgement: no valid local disease-level target.

The local cobalamin umbrella has the right broad mechanism class, but it lacks
the CD320 receptor subtype. Mapping this record to isolated MMA would obscure
the upstream cobalamin uptake lesion and the IEMbase statement that there is no
consistent clinical picture.

## Curation actions

- Do not map this record to `Methylmalonic_Acidemia.yaml`.
- Consider a CD320/transcobalamin receptor defect entry or a CD320 subtype under
  the cobalamin metabolism and transport umbrella if disease-entry scope is
  accepted.
- If curated, capture the narrow biochemical signal separately from isolated
  MMUT/MMAA/MMAB methylmalonic acidemia.
