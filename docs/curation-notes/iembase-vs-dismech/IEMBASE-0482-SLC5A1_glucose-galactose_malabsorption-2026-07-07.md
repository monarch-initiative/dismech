# IEMbase 0482: SLC5A1-related intestinal sodium-glucose cotransporter 1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 482 |
| Nosology | 3.6.04.01 |
| Gene | SLC5A1 |
| External IDs | OMIM:606824; ORPHA:35710 |
| Generated mapping | UNMAPPED; best candidate `Glycogen_Storage_Disease_Type_I.yaml` |
| Candidate DisMech targets | `Glucose-Galactose_Malabsorption.yaml`; rejected lexical candidate `Glycogen_Storage_Disease_Type_I.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive SLC5A1-related intestinal
sodium-glucose cotransporter 1 deficiency as glucose-galactose malabsorption.
It records fructose-based carbohydrate-free formula as treatment. Biochemical
rows include normal oral fructose loading, positive oral glucose and galactose
loading tests, decreased glucose and galactose uptake by enterocytes,
normal-to-increased urinary glucose, increased stool reducing sugars, and
normal-to-high plasma sodium. Clinical rows include failure to thrive and
urolithiasis.

## DisMech phenotype coverage

`Glucose-Galactose_Malabsorption.yaml` is the exact local target. The entry
models biallelic SLC5A1/SGLT1 loss of function in small-intestinal enterocytes,
failure of active glucose/galactose absorption, spared fructose absorption via
GLUT5, osmotic diarrhea and dehydration, dietary rechallenge recurrence,
neonatal-onset watery diarrhea, hypernatremic dehydration, failure to thrive,
abdominal distension/bloating, nephrolithiasis, elevated stool reducing
substances, positive hydrogen breath testing, and fructose-based
glucose/galactose-free formula.

## Concordance and completeness

Judgement: false negative generated mapping; resolve to
`Glucose-Galactose_Malabsorption.yaml`.

The GSD I candidate is a false-positive carbohydrate-metabolism neighbor.
IEMbase and DisMech agree on SLC5A1/SGLT1 identity, recessive inheritance,
selective glucose/galactose malabsorption with fructose sparing, stool reducing
substances, failure to thrive, stone risk, and fructose-based formula. IEMbase
adds explicit oral loading-test and enterocyte uptake rows, urinary glucose, and
plasma sodium. DisMech is stronger on the causal diarrhea/dehydration path and
on the distinction from renal SLC5A2/SGLT2 disease.

## Curation actions

- Treat this as covered by `Glucose-Galactose_Malabsorption.yaml`.
- Reject `Glycogen_Storage_Disease_Type_I.yaml` as an exact mapping.
- Consider evidence-backed additions for the oral glucose/galactose/fructose
  loading tests, enterocyte uptake assays, urinary glucose, and plasma sodium.
