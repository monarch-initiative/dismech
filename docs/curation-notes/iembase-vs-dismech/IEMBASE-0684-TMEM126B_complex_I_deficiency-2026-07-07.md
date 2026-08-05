# IEMbase 0684: TMEM126B-related transmembrane protein 126B deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 684 |
| Nosology | 7.1.1.01 |
| Nosology code | IEM0446 |
| Gene | TMEM126B |
| External IDs | OMIM:618250; ORPHA:2609 |
| Generated mapping | CANDIDATE to `COX11-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | Broad complex I/Leigh and ACAD9 context only; no exact TMEM126B target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive TMEM126B-related transmembrane protein
126B deficiency, also labeled mitochondrial complex I deficiency, nuclear type
29.

The cached biochemical row shows decreased fibroblast complex I activity across
all ages. Clinical rows include hypertrophic cardiomyopathy, myopathy, renal
tubular acidosis, and characteristic exercise intolerance from infancy through
adulthood.

## DisMech phenotype coverage

No exact TMEM126B or MC1DN29 local target was identified.

`Leigh_Syndrome.yaml` provides broad complex I/oxidative-phosphorylation context,
and `ACAD9_Deficiency.yaml` overlaps with exercise intolerance, hypertrophic
cardiomyopathy, and complex I deficiency. Neither is disease-level coverage for
TMEM126B deficiency.

The generated `COX11-Related_COX_Deficiency.yaml` candidate is a wrong-complex
match. COX11 is a complex IV copper-chaperone/assembly disorder, not a
TMEM126B-related complex I disease.

## Concordance and completeness

Judgement: true local gap.

The IEMbase row is a comparatively myopathic/cardiac complex I deficiency with
renal tubular acidosis and exercise intolerance. Generic Leigh and ACAD9 entries
should not be used to claim TMEM126B completeness.

## Curation actions

- Add a dedicated TMEM126B/MC1DN29 target if curated.
- Reject COX11-related complex IV deficiency as exact coverage.
- Preserve decreased fibroblast complex I activity, hypertrophic
  cardiomyopathy, myopathy, renal tubular acidosis, and exercise intolerance.
- Use ACAD9 only as broad complex I/cardiomyopathy/exercise-intolerance context.
