# IEMbase 0740: ATP5F1E-related mitochondrial ATP synthase F1 epsilon deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 740 |
| Nosology | 7.5.03.01 |
| Nosology code | IEM0483 |
| Gene | ATP5F1E |
| External IDs | OMIM:614053 |
| Generated mapping | CANDIDATE; fuzzy `COX10-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | Broad complex V context only; no exact ATP5F1E target identified |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive ATP5F1E-related mitochondrial ATP
synthase F1 subunit epsilon deficiency, also labeled mitochondrial complex V
deficiency, nuclear type 3. The cached rows point to an adult presentation with
elevated plasma lactate, hypertrophic cardiomyopathy, hypotonia,
polyneuropathy, and psychomotor retardation.

## DisMech phenotype coverage

No exact ATP5F1E target was identified locally.

The generated `COX10-Related_COX_Deficiency.yaml` candidate is not an exact
match. COX10 is a complex IV heme A biosynthesis/assembly disorder, whereas
ATP5F1E encodes an ATP synthase F1 epsilon subunit. Local complex V context in
`NARP_syndrome.yaml` and
`Myopathy_Lactic_Acidosis_and_Sideroblastic_Anemia.yaml` does not cover the
ATP5F1E disease identity.

## Concordance and completeness

Judgement: true ATP5F1E complex V local gap. Reject the COX10 candidate as
exact coverage.

IEMbase gives a focused adult phenotype prompt: lactate elevation,
hypertrophic cardiomyopathy, hypotonia, polyneuropathy, and psychomotor delay.
Those features overlap with mitochondrial disease generally, but DisMech lacks
the ATP5F1E-specific entry.

## Curation actions

- Add ATP5F1E-related mitochondrial complex V deficiency, nuclear type 3, to
  the complex V backlog.
- Reject `COX10-Related_COX_Deficiency.yaml` as exact coverage.
- Preserve adult lactate, hypertrophic cardiomyopathy, hypotonia,
  polyneuropathy, and psychomotor-delay prompts.
