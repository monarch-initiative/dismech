# IEMbase 0677: NDUFAF1-related complex I assembly factor 1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 677 |
| Nosology | 7.1.01.01 |
| Nosology code | IEM0437 |
| Gene | NDUFAF1 |
| External IDs | OMIM:618234; ORPHA:289527 |
| Generated mapping | CANDIDATE to `COX20-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | Broad complex I/Leigh context only; no exact NDUFAF1 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive NDUFAF1-related complex I assembly factor
1 deficiency, also labeled mitochondrial complex I deficiency, nuclear type 11.

The biochemical rows show decreased fibroblast complex I activity and increased
plasma lactate from the neonatal period through adolescence. Clinical rows
include hypotonia, lactic acidosis, MELAS-like features, and characteristic
cardiomyopathy across the same age range, plus characteristic neonatal/infantile
failure to thrive.

## DisMech phenotype coverage

No exact NDUFAF1 or MC1DN11 target was identified.

`Leigh_Syndrome.yaml` provides broad complex I and mitochondrial energy-failure
context, including complex I deficiency, lactic acidosis, hypotonia, basal
ganglia vulnerability, and cardiomyopathy as a Leigh subtype. `ACAD9_Deficiency.yaml`
also discusses complex I assembly biology and mentions NDUFAF1 as an ACAD9
binding partner in the MCIA complex. Neither file is disease-level coverage for
NDUFAF1 deficiency.

The generated `COX20-Related_COX_Deficiency.yaml` candidate is a complex IV/COX
false positive and should not be used.

## Concordance and completeness

Judgement: true local gap with broad complex I context available.

The IEMbase row is specifically an assembly-factor complex I defect. Existing
complex IV files are wrong-complex matches, while Leigh and ACAD9 entries can
only support generic mechanism context.

## Curation actions

- Add a dedicated NDUFAF1/MC1DN11 target if curated.
- Reject COX20-related complex IV deficiency as exact coverage.
- Preserve decreased fibroblast complex I activity, increased plasma lactate,
  cardiomyopathy, failure to thrive, hypotonia, lactic acidosis, and MELAS-like
  features.
- Use `Leigh_Syndrome.yaml` only as broad syndrome context.
