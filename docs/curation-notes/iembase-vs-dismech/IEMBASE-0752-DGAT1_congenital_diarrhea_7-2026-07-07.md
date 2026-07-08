# IEMbase 0752: DGAT1-related diacylglycerol acyltransferase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 752 |
| Nosology | 14.4.05.01 |
| Nosology code | IEM0659 |
| Gene | DGAT1 |
| External IDs | OMIM:615863; ORPHA:329242 |
| Generated mapping | UNMAPPED; weak candidate `Travelers_Diarrhea.yaml` |
| Candidate DisMech targets | None exact |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase labels this autosomal recessive record as DGAT1-related
diacylglycerol acyltransferase deficiency, with alternate name congenital
diarrhea type 7. The source signal describes congenital enteropathy with
protein loss and immune complications: chronic diarrhea, vomiting, failure to
thrive, protein-losing enteropathy, recurrent infections, immunodeficiency,
anemia, acidosis, elevated transaminases, hypoalbuminemia, and low serum IgG.

## DisMech phenotype coverage

No exact DGAT1 / congenital diarrhea type 7 entry is present locally. Some
DisMech entries include chronic diarrhea, protein-losing enteropathy, immune
deficiency, or failure to thrive as phenotypes, but they do not represent this
monogenic DGAT1 disorder.

The generated `Travelers_Diarrhea.yaml` candidate is a false positive. That
entry concerns infectious acute enterotoxigenic Escherichia coli diarrhea in
travelers, not congenital autosomal recessive DGAT1 deficiency.

## Concordance and completeness

Judgement: true local gap.

The IEMbase record provides a strong phenotype cluster for DGAT1 disease and
should be curated separately from infectious diarrhea or nonspecific
protein-losing enteropathy contexts.

## Curation actions

- Add a distinct DGAT1 / congenital diarrhea type 7 target before treating this
  IEMbase disease as covered.
- Reject `Travelers_Diarrhea.yaml` as exact or phenotype-level disease
  coverage.
- Preserve chronic diarrhea, protein-losing enteropathy, hypoalbuminemia, low
  IgG, recurrent infections, immunodeficiency, failure to thrive, and
  transaminase elevation as high-priority prompts.
