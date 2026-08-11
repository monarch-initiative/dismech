# IEMbase 0675: MVD-related mevalonate pyrophosphate decarboxylase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 675 |
| Nosology | 14.7.04.01 |
| Nosology code | IEM0743 |
| Gene | MVD |
| External IDs | OMIM:614714; ORPHA:79152 |
| Generated mapping | UNMAPPED; best candidate `Hereditary_Orotic_Aciduria.yaml` |
| Candidate DisMech targets | Broad mevalonate/sterol-pathway context only; no exact MVD/POROK7 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal dominant MVD-related mevalonate pyrophosphate
decarboxylase deficiency, labeled porokeratosis type 7.

The cached phenotype signal is dermatologic and concise: characteristic actinic
porokeratosis and keratotic skin lesions in adolescence and adulthood. No
biochemical rows are present in the cached record.

## DisMech phenotype coverage

No exact MVD, mevalonate pyrophosphate decarboxylase deficiency, or
porokeratosis type 7 local target was identified.

`Hereditary_Orotic_Aciduria.yaml` is a false positive and should not be used. It
is a pyrimidine-biosynthesis disorder, not a mevalonate/sterol-biosynthesis
porokeratosis disorder. `Mevalonate_Kinase_Deficiency.yaml` can orient the
upstream pathway, but it is MVK-related recessive autoinflammatory disease and
does not cover MVD-associated dominant porokeratosis.

## Concordance and completeness

Judgement: true local gap.

The IEMbase row is a narrow dermatologic porokeratosis record. Existing local
mevalonate-pathway content does not provide disease-level or phenotype-level
coverage for the MVD/POROK7 entity.

## Curation actions

- Add a dedicated MVD/POROK7 target if this disease is curated.
- Reject hereditary orotic aciduria as the generated candidate.
- Use mevalonate kinase deficiency only as broad pathway context, not as disease
  coverage.
- Preserve adolescent/adult actinic porokeratosis and keratotic skin lesions.
