# IEMbase 0685: NDUFV1-related NADH dehydrogenase flavoprotein 1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 685 |
| Nosology | 7.1.01.02 |
| Nosology code | IEM0413 |
| Gene | NDUFV1 |
| External IDs | OMIM:618225; ORPHA:255241 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | Partial gene-level coverage in `Leigh_Syndrome.yaml`; no standalone NDUFV1 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive NDUFV1-related NADH dehydrogenase
flavoprotein 1 deficiency, also labeled mitochondrial complex I deficiency,
nuclear type 4.

Biochemical rows include decreased fibroblast complex I activity and increased
plasma lactate from neonatal through adolescent ages. Clinical rows include
ataxia, basal ganglia lesions, hypertrophic cardiomyopathy, encephalopathy,
failure to thrive, lactic acidosis, Leigh syndrome, microcephaly,
ophthalmoplegia, psychomotor regression, and characteristic brainstem lesions on
MRI.

## DisMech phenotype coverage

`Leigh_Syndrome.yaml` contains partial gene-level coverage: its complex I
deficiency section lists NDUFV1 as a nuclear-encoded complex I gene whose
biallelic variants can cause complex I-deficient Leigh syndrome. The entry also
covers many shared phenotypes such as lactic acidosis, hypotonia/movement
disorder, basal-ganglia lesions, ophthalmoplegia, failure to thrive, and
cardiomyopathy.

However, there is no standalone NDUFV1 disease target or subtype with the
IEMbase row's specific phenotype package and age-banded biochemical signal.

## Concordance and completeness

Judgement: partial broad Leigh coverage only.

The local Leigh entry supports the general NDUFV1-to-complex-I-deficient-Leigh
relationship, but it does not prove row-level completeness for NDUFV1/MC1DN4.
Brainstem lesions, microcephaly, hypertrophic cardiomyopathy, ophthalmoplegia,
and psychomotor regression should be reviewed specifically if curated.

## Curation actions

- Keep `Leigh_Syndrome.yaml` as partial gene/syndrome context.
- Add a dedicated NDUFV1/MC1DN4 target or subtype if disease-level completeness
  is needed.
- Preserve decreased complex I activity, increased lactate, basal ganglia and
  brainstem MRI lesions, cardiomyopathy, ophthalmoplegia, microcephaly,
  psychomotor regression, failure to thrive, ataxia, and encephalopathy.
