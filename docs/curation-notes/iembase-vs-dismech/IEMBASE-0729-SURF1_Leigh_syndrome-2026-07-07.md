# IEMbase 0729: SURF1-related COX IV deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 729 |
| Nosology | 7.4.07.01 |
| Nosology code | IEM0475 |
| Gene | SURF1 |
| External IDs | OMIM:256000; OMIM:616684; ORPHA:391351 |
| Generated mapping | UNMAPPED; weak candidate `SURF1-Related_Leigh_Syndrome.yaml` |
| Candidate DisMech targets | `SURF1-Related_Leigh_Syndrome.yaml` is exact local coverage |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive SURF1-related COX IV deficiency, with
alternate names Leigh syndrome due to COX IV deficiency and Charcot-Marie-Tooth
disease type 4K. The cached rows include increased CSF and plasma lactate,
basal ganglia and brainstem MRI abnormalities, possible hypertrophic
cardiomyopathy, epilepsy, feeding difficulties, hypertrichosis, hypotonia,
Leigh syndrome, regression, ophthalmoplegia, possible optic atrophy, perinatal
death, respiratory failure, psychomotor retardation, short stature, tremor,
vomiting, ataxia, failure to thrive, and nystagmus.

## DisMech phenotype coverage

DisMech has exact local coverage in `SURF1-Related_Leigh_Syndrome.yaml`. The
entry resolves to mitochondrial complex IV deficiency nuclear type 1
(MONDO:0700250) and describes biallelic SURF1 loss as an early complex IV
assembly-factor defect causing the prototypic nuclear-encoded Leigh syndrome.

Local phenotype coverage includes developmental regression, delayed growth and
development, brainstem abnormalities, lactic acidosis, encephalopathy, and
muscular hypotonia, with reduced COX activity as the defining biochemical
feature.

## Concordance and completeness

Judgement: false negative from the generated mapper. The correct target is
`SURF1-Related_Leigh_Syndrome.yaml`.

The IEMbase and local records align strongly on SURF1, autosomal recessive
complex IV assembly failure, Leigh syndrome, lactate, brainstem involvement,
basal ganglia disease, hypotonia, and regression. IEMbase adds useful prompts
for hypertrichosis, ophthalmoplegia, tremor, nystagmus, feeding/vomiting,
cardiomyopathy, optic atrophy, respiratory failure, perinatal death, and the
CMT4K alternate context.

## Curation actions

- Resolve IEMbase 729 to `SURF1-Related_Leigh_Syndrome.yaml`.
- Treat the generated UNMAPPED status as stale or overly strict.
- Preserve broad IEMbase phenotype prompts, especially hypertrichosis,
  ophthalmoplegia, tremor, nystagmus, and cardiomyopathy.
- Keep Charcot-Marie-Tooth type 4K as secondary alternate-name context, not as
  the primary mapping target for this Leigh/COX deficiency row.
