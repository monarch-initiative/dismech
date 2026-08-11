# IEMbase 0674: PMVK-related phosphomevalonate kinase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 674 |
| Nosology | 14.7.03.01 |
| Nosology code | IEM0742 |
| Gene | PMVK |
| External IDs | OMIM:175800; ORPHA:735 |
| Generated mapping | UNMAPPED; best candidate `Mevalonate_Kinase_Deficiency.yaml` |
| Candidate DisMech targets | Broad mevalonate-pathway context only; no exact PMVK/POROK1 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal dominant PMVK-related phosphomevalonate kinase
deficiency, labeled porokeratosis type 1 and porokeratosis of Mibelli.

The cached phenotype signal is dermatologic only: actinic porokeratosis and
keratotic skin lesions in adolescence and adulthood. There are no biochemical
rows in the cached record.

## DisMech phenotype coverage

No exact PMVK, phosphomevalonate kinase deficiency, porokeratosis type 1, or
porokeratosis of Mibelli target was identified.

`Mevalonate_Kinase_Deficiency.yaml` is a biologically adjacent but incorrect
target. It models autosomal recessive MVK-related systemic autoinflammation
across the HIDS/mevalonic-aciduria spectrum, with recurrent fever, elevated
mevalonic acid, inflammasome activation, and neurologic features in severe
disease. It does not model autosomal dominant PMVK-associated porokeratosis.

`RNU12-related_Minor_Spliceopathy.yaml` includes porokeratosis as part of CDAGS
syndrome, but that is an unrelated congenital spliceopathy context rather than
PMVK disease coverage.

## Concordance and completeness

Judgement: true local gap. The generated mevalonate-kinase candidate is
understandable as a pathway-neighbor match, but it would import the wrong gene,
inheritance pattern, and systemic phenotype.

The IEMbase row is narrow, so the key preservation point is the adolescent/adult
actinic porokeratosis and keratotic-lesion dermatologic presentation rather than
classic mevalonate kinase deficiency features.

## Curation actions

- Add a dedicated PMVK/POROK1 target if this disease is curated.
- Do not map this record to MVK-related mevalonate kinase deficiency.
- Treat RNU12/CDAGS porokeratosis as unrelated differential context only.
- Preserve actinic porokeratosis and keratotic skin lesions as the core
  phenotype prompts.
