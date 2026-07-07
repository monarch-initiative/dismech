# IEMbase 0208: BCS1L-related GRACILE syndrome

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 208 |
| Nosology | 7.3.01.02 |
| Gene | BCS1L |
| External IDs | OMIM:603358; ORPHA:53693 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | `CALFAN_Syndrome.yaml` is a false-positive clinical-neighbor candidate |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as BCS1L-related GRACILE syndrome, with alternate
labels Fellman disease, Bjoernstad syndrome, and the acronym expansion growth
retardation, aminoaciduria, cholestasis, iron overload, lactic acidosis, and
early death. Treatability is marked unknown.

The biochemical rows include low-to-normal glucose, increased serum iron, and
increased plasma lactate. Characteristic clinical rows include sensorineural
deafness, early death, hemosiderosis, intrauterine growth retardation, lactic
acidosis, renal Fanconi syndrome, and proximal renal tubulopathy. Additional
rows include intrahepatic cholestasis, developmental delay, hypotonia, and pili
torti. No treatment rows are listed.

## DisMech phenotype coverage

No local DisMech entry covers BCS1L-related GRACILE syndrome. The generated best
candidate, `CALFAN_Syndrome.yaml`, is not a valid target: CALFAN is an
SCYL1-related Golgi trafficking disorder with recurrent low-GGT cholestasis,
acute liver failure, neurodegeneration, and growth/skeletal findings. It shares
neonatal/infantile liver and neurologic themes but not the BCS1L/complex III
mitochondrial mechanism, lactic acidosis, iron overload, Fanconi/proximal
tubulopathy, or GRACILE identity.

## Concordance and completeness

Judgement: true local disease gap; CALFAN is a false-positive clinical
neighbor.

IEMbase gives a distinctive BCS1L mitochondrial disease profile combining
growth restriction, aminoaciduria/Fanconi tubulopathy, cholestasis, iron
overload/hemosiderosis, lactic acidosis, sensorineural deafness, hypotonia,
pili torti, and early death. DisMech lacks a corresponding BCS1L/GRACILE entry.

## Curation actions

- Do not map this record to `CALFAN_Syndrome.yaml`.
- Consider a future BCS1L/GRACILE syndrome entry under mitochondrial respiratory
  chain complex III assembly disorders.
- Seed that future entry with plasma lactate elevation, serum iron overload,
  renal Fanconi/proximal tubulopathy, intrauterine growth retardation,
  cholestasis, sensorineural deafness, hypotonia, pili torti, and early death.
