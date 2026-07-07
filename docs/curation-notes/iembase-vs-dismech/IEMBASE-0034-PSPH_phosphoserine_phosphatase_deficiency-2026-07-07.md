# IEMbase 0034: PSPH-related phosphoserine phosphatase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 34 |
| Nosology | 1.6.03.01 |
| Gene | PSPH |
| External IDs | OMIM:172480; OMIM:614023 |
| Generated mapping | UNMAPPED; best fuzzy candidate `Pyruvate_Dehydrogenase_Deficiency.yaml` |
| Candidate DisMech targets | none currently valid |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase presents PSPH deficiency as a serine-biosynthesis disorder. The
biochemical signature is low CSF serine and low-to-normal plasma serine.

The clinical signal is narrower than the PHGDH record: psychomotor delay,
tonic-clonic seizures, growth retardation, and intellectual disability. IEMbase
lists nutritional glycine and L-serine as treatments.

## DisMech phenotype coverage

There is no local DisMech entry or subtype for PSPH-related phosphoserine
phosphatase deficiency. The generated fuzzy candidate,
`Pyruvate_Dehydrogenase_Deficiency.yaml`, should be rejected. It contains a PDH
phosphatase regulatory subtype, but that is a mitochondrial pyruvate
dehydrogenase complex disorder with lactic acidosis and impaired pyruvate
oxidation, not a phosphoserine phosphatase defect in de novo serine synthesis.

## Concordance and completeness

Judgement: generated unmapped status is correct, and the PDH candidate is a
lexical false positive driven by the word phosphatase.

IEMbase supplies a compact phenotype set for a future PSPH curation target. Its
distinguishing features are low CSF serine, relatively mild or variable plasma
serine reduction, developmental delay, seizures, growth retardation, and
serine/glycine supplementation.

## Curation actions

- Do not map this record to `Pyruvate_Dehydrogenase_Deficiency.yaml`.
- Consider PSPH deficiency in the same future serine-biosynthesis work package
  as PHGDH and PSAT1 deficiency.
- Preserve the distinction between low CSF serine and low-to-normal plasma
  serine if a future entry is created.
