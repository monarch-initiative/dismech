# IEMbase 0108: ALAS2-related erythroid 5-aminolevulinate synthase superactivity

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 108 |
| Nosology | 17.1.02.01 |
| Gene | ALAS2 |
| External IDs | OMIM:300752 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | `Inherited_Porphyria.yaml#Erythropoietic Protoporphyria` as current umbrella/subtype context |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as ALAS2-related erythroid 5-aminolevulinate synthase
superactivity, with alternate label X-linked protoporphyria (XLDPP). Treatability
is marked yes.

The biochemical rows are increased erythrocyte delta-ALA synthase activity,
normal urinary total porphyrins, markedly increased erythrocyte protoporphyrin
IX, and increased erythrocyte zinc protoporphyrin IX. The cached JSON has no
clinical rows.

Treatment is pyridoxine.

## DisMech phenotype coverage

The generated UNMAPPED status is a false negative for current local coverage.
DisMech does not have a standalone X-linked protoporphyria entry, but
`Inherited_Porphyria.yaml` explicitly models ALAS2-related X-linked
protoporphyria in the erythropoietic protoporphyria/protoporphyria branch. The
entry includes X-linked inheritance, increased ALAS2 activity, protoporphyrin IX
accumulation, severe cutaneous phototoxicity, liver-risk context, increased
erythrocyte or plasma protoporphyrin, and afamelanotide pharmacotherapy.

The existing subtype anchor is `Inherited_Porphyria.yaml#Erythropoietic
Protoporphyria`, whose description includes FECH-related or ALAS2-related
protoporphyria rather than splitting XLP as a separate subtype.

## Concordance and completeness

Judgement: false negative to local umbrella/subtype coverage, with a future
split decision needed.

DisMech is richer for clinical phototoxicity, mechanism, and group-level
treatment context. IEMbase is richer for the XLP-specific diagnostic lab
pattern: erythrocyte ALAS2 activity, normal urine porphyrins, erythrocyte PPIX,
and zinc protoporphyrin IX. The treatment rows differ: IEMbase lists pyridoxine,
while DisMech currently emphasizes afamelanotide for EPP/XLP light tolerance.

## Curation actions

- Resolve to `Inherited_Porphyria.yaml#Erythropoietic Protoporphyria` for now,
  noting that this is subtype-context coverage rather than a standalone XLP
  disease file.
- Consider adding a distinct X-linked protoporphyria subtype or standalone entry
  if porphyria curation moves below umbrella level.
- Review pyridoxine and XLP-specific biomarker rows before adding them locally.
