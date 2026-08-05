# IEMbase 0038: ALDH4A1-related pyrroline-5-carboxylate dehydrogenase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 38 |
| Nosology | 1.7.06.01 |
| Gene | ALDH4A1 |
| External IDs | OMIM:239510 |
| Generated mapping | UNMAPPED; best fuzzy candidate `Pyruvate_Dehydrogenase_Deficiency.yaml` |
| Candidate DisMech targets | none currently valid |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents ALDH4A1 deficiency as pyrroline-5-carboxylate
dehydrogenase deficiency, also called hyperprolinemia type 2. The biochemical
signal is high plasma proline, high urinary proline, increased urinary
pyrroline-5-carboxylate, variable-to-markedly increased urinary
4-hydroxyproline, and normal plasma 4-hydroxyproline.

The clinical signal is sparse and uncertain: possible febrile seizures,
possible pharmacoresistant seizures, and possible intellectual disability.
Treatability is marked yes, but no treatment rows are present in the cached
record.

## DisMech phenotype coverage

There is no current DisMech entry or subtype for ALDH4A1-related
hyperprolinemia type 2. The generated fuzzy candidate,
`Pyruvate_Dehydrogenase_Deficiency.yaml`, should be rejected. PDH deficiency is
a mitochondrial pyruvate-to-acetyl-CoA disorder with lactate/pyruvate
accumulation and neurodevelopmental disease, not a proline catabolism disorder
with elevated proline and P5C.

ALDH18A1-related P5CS deficiency is also not a match. It impairs proline and
ornithine biosynthesis and tends toward low or low-normal proline, whereas
ALDH4A1 deficiency blocks proline degradation and produces hyperprolinemia.

## Concordance and completeness

Judgement: generated unmapped status is correct; the PDH candidate is a false
positive.

IEMbase provides a biochemical target profile for future curation but only weak
clinical signal. The most important distinction to preserve is hyperprolinemia
type 2 with elevated P5C, not generic seizure disease and not ALDH18A1 P5CS
deficiency.

## Curation actions

- Do not map this record to PDH deficiency or ALDH18A1 deficiency.
- Consider future curation only if the proline-catabolism work package becomes
  a priority.
- If curated, anchor the entry on elevated plasma/urinary proline and urinary
  P5C, with seizures and intellectual disability treated as uncertain or
  variable clinical associations unless supported by stronger evidence.
