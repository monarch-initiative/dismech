# IEMbase 0694: NDUFA1-related NADH dehydrogenase alpha subcomplex subunit 1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 694 |
| Nosology | 7.1.1.02 |
| Nosology code | IEM0422 |
| Gene | NDUFA1 |
| External IDs | OMIM:301020; ORPHA:2609 |
| Generated mapping | CANDIDATE to `PET100-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | Broad complex I/Leigh context only; no exact NDUFA1 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents X-linked NDUFA1-related NADH dehydrogenase alpha subcomplex
subunit 1 deficiency, also labeled mitochondrial complex I deficiency, nuclear
type 12.

The biochemical rows show decreased fibroblast complex I activity and increased
plasma lactate across neonatal, infantile, childhood, and adolescent windows.
Clinical rows include epilepsy, hypotonia, lactic acidosis, psychomotor
retardation, basal ganglia MRI abnormalities, and Leigh syndrome.

## DisMech phenotype coverage

No exact NDUFA1 or MC1DN12 local target was identified.

`Leigh_Syndrome.yaml` provides broad syndrome-level context for complex
I-deficient Leigh disease, lactate elevation, seizures, hypotonia, basal ganglia
lesions, and psychomotor/developmental impairment, but it does not model NDUFA1
or the X-linked MC1DN12 entity.

The generated `PET100-Related_COX_Deficiency.yaml` candidate is a complex IV
biogenesis disorder, not an NDUFA1 complex I subunit disorder. The match appears
to be driven by mitochondrial-complex/nuclear-type lexical overlap rather than
gene or mechanism concordance.

## Concordance and completeness

Judgement: true local gap with broad Leigh overlap only.

The IEMbase row is a gene-specific complex I deficiency with an X-linked
inheritance pattern and a compact Leigh/lactic-acidosis phenotype. Generic Leigh
coverage is useful context but is not sufficient disease-level coverage, and
PET100 should be rejected as exact coverage.

## Curation actions

- Add a dedicated NDUFA1/MC1DN12 target if curated.
- Reject PET100-related complex IV deficiency as exact coverage.
- Preserve decreased fibroblast complex I activity, increased plasma lactate,
  epilepsy, hypotonia, lactic acidosis, psychomotor retardation, basal ganglia
  MRI abnormalities, and Leigh syndrome.
- Use `Leigh_Syndrome.yaml` only as broad syndrome context.
