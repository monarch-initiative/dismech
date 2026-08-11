# IEMbase 0009: SLC22A5-related primary carnitine deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 9 |
| Nosology | 4.1.01.01 |
| Gene | SLC22A5 |
| External IDs | OMIM:212140 |
| Generated mapping | MAPPED by `alias_exact:primary carnitine deficiency` |
| DisMech target | `kb/disorders/Primary_Carnitine_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

Characteristic clinical features are cardiomyopathy, axial hypotonia, liver
dysfunction, rhabdomyolysis, and skeletal myopathy. IEMbase does not list a
separate additional clinical panel for this row.

The biochemical signature is detailed: low free carnitine in dried blood spot
and plasma, increased urinary free carnitine, decreased long-chain
acylcarnitines, decreased C16/C18 acylcarnitines, sometimes increased creatine
kinase and transaminases, low ketones during hypoglycemia, dicarboxylic
aciduria, and low/normal glucose.

Treatment is L-carnitine supplementation.

## DisMech phenotype coverage

DisMech captures the clinical disease well: dilated and hypertrophic
cardiomyopathy, hypoketotic hypoglycemia, hyperammonemia, skeletal myopathy,
hypotonia, lethargy, cardiac arrest, ventricular arrhythmia, and encephalopathy.
Biochemical entries include free carnitine, urinary carnitine, ammonia, blood
glucose, and creatine kinase. Treatments cover L-carnitine supplementation,
dietary management, acute decompensation management, newborn screening, cardiac
management, genetic counseling, and acetyl-L-carnitine for encephalopathy.

## Concordance and completeness

Judgement: high concordance. The generated mapping is correct, and DisMech is
broader for severe clinical/cardiac outcomes.

IEMbase is more granular for acylcarnitine species and organic aciduria. DisMech
does not explicitly model decreased long-chain acylcarnitines, C16/C18 species,
dicarboxylic aciduria, or liver dysfunction/transaminase elevation.

## Curation actions

- No mapping correction needed.
- Consider adding a more granular acylcarnitine-panel biochemical profile if it
  improves diagnostic modeling.
- Consider liver dysfunction/rhabdomyolysis details only with independent
  supporting evidence.
