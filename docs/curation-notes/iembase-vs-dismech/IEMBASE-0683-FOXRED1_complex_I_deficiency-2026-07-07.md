# IEMbase 0683: FOXRED1-related mitochondrial complex I deficiency, nuclear type 19

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 683 |
| Nosology | 7.1.07.01 |
| Nosology code | IEM0443 |
| Gene | FOXRED1 |
| External IDs | OMIM:618241; ORPHA:255241 |
| Generated mapping | CANDIDATE to `PET117-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | Broad complex I/Leigh context only; no exact FOXRED1 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive FOXRED1-related mitochondrial complex I
deficiency, nuclear type 19.

Biochemical rows include decreased fibroblast complex I activity and increased
plasma lactate across all ages. Clinical rows include epilepsy, hypotonia, Leigh
syndrome, characteristic hypertrophic cardiomyopathy in infancy/childhood,
characteristic cerebellar atrophy on MRI across all ages, and characteristic
pulmonary hypertension from infancy through adolescence.

## DisMech phenotype coverage

No exact FOXRED1 or MC1DN19 target was identified.

`Leigh_Syndrome.yaml` provides broad overlap for complex I deficiency,
mitochondrial energy failure, lactic acidosis, hypotonia, seizures, basal
ganglia/brainstem vulnerability, and cardiomyopathy-associated Leigh syndrome.
It does not model FOXRED1 or the pulmonary-hypertension/cerebellar-atrophy
phenotype package.

The generated `PET117-Related_COX_Deficiency.yaml` candidate is a complex IV
assembly-factor disorder and should be rejected as exact coverage.

## Concordance and completeness

Judgement: true local gap with broad Leigh/complex I context only.

The IEMbase row is a gene-specific complex I deficiency with useful extra
features beyond generic Leigh syndrome: hypertrophic cardiomyopathy, cerebellar
atrophy, and pulmonary hypertension.

## Curation actions

- Add a dedicated FOXRED1/MC1DN19 target if curated.
- Reject PET117-related complex IV deficiency as exact coverage.
- Preserve decreased complex I activity, increased lactate, epilepsy, hypotonia,
  Leigh syndrome, hypertrophic cardiomyopathy, cerebellar atrophy, and pulmonary
  hypertension.
- Use broad Leigh syndrome context only for shared mitochondrial neurologic
  features.
