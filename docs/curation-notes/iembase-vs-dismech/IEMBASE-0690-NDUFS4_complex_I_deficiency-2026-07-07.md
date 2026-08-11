# IEMbase 0690: NDUFS4-related NADH dehydrogenase iron-sulfur protein 4 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 690 |
| Nosology | 7.1.08.01 |
| Nosology code | IEM0420 |
| Gene | NDUFS4 |
| External IDs | OMIM:252010; ORPHA:255241 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | Partial gene-level coverage in `Leigh_Syndrome.yaml`; no standalone NDUFS4 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive NDUFS4-related NADH dehydrogenase
iron-sulfur protein 4 deficiency, also labeled mitochondrial complex I
deficiency, nuclear type 1.

Biochemical rows include decreased fibroblast complex I activity, decreased
fibroblast complex III activity, increased plasma lactate, and low-to-normal
plasma glucose in early ages. Clinical rows include basal ganglia MRI
abnormalities, failure to thrive, hypotonia, and characteristic hypertrophic
cardiomyopathy, lactic acidosis, and Leigh syndrome.

## DisMech phenotype coverage

`Leigh_Syndrome.yaml` contains partial gene-level NDUFS4 coverage. Its genetic
section states that biallelic NDUFS4 loss-of-function causes complex
I-deficient Leigh syndrome, with evidence from the Ndufs4 mouse model. The
entry also covers shared Leigh features including complex I deficiency,
lactic acidosis, basal ganglia lesions, hypotonia, failure to thrive, and
cardiomyopathy.

There is no standalone NDUFS4 disease target or MC1DN1 subtype with the full
IEMbase biochemical and phenotype set.

## Concordance and completeness

Judgement: partial broad Leigh coverage only.

The NDUFS4 gene-to-Leigh relationship is represented locally, but row-level
completeness is not established. IEMbase adds complex III activity decrease,
low-to-normal glucose, age-banded fibroblast complex I activity, and
hypertrophic cardiomyopathy emphasis.

## Curation actions

- Keep `Leigh_Syndrome.yaml` as partial gene/syndrome context.
- Add a dedicated NDUFS4/MC1DN1 target or subtype if full disease-level coverage
  is desired.
- Preserve decreased complex I and complex III activity, increased lactate,
  low-to-normal glucose, basal ganglia abnormalities, failure to thrive,
  hypotonia, hypertrophic cardiomyopathy, lactic acidosis, and Leigh syndrome.
