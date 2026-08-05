# IEMbase 0584: SMS-related spermine synthase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 584 |
| Nosology | 2.4.11.01 |
| Gene | SMS |
| External IDs | OMIM:309583; OMIM:300105; ORPHA:477817 |
| Generated mapping | UNMAPPED; best candidate `GM3_Synthase_Deficiency.yaml` |
| Candidate DisMech targets | None exact |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents SMS-related spermine synthase deficiency, with alternate
labels Snyder-Robinson syndrome X-linked, SMS, and SRS. The record is
classified under disorders of polyamine metabolism, lists autosomal recessive
inheritance, has unknown treatability, and has no treatment rows.

The biochemical row is increased plasma N-acetylspermidine. Clinical rows
include epileptic encephalopathy and intellectual disability.

## DisMech phenotype coverage

`GM3_Synthase_Deficiency.yaml` is a false-positive generated candidate. That
entry models ST3GAL5-related GM3 synthase deficiency in glycosphingolipid
biology with severe neurodevelopmental and epilepsy phenotypes. It does not
match SMS, spermine synthase, Snyder-Robinson syndrome, polyamine metabolism,
or the N-acetylspermidine biomarker.

The local knowledge base contains only broad polyamine biology in other disease
contexts and no exact Snyder-Robinson / spermine synthase deficiency target was
identified.

## Concordance and completeness

Judgement: true local gap; reject GM3 synthase deficiency as an exact target.

The generated candidate shares neurologic severity and epilepsy but diverges on
gene, pathway, mechanism, biomarker, and disease identity. The IEMbase record
should be curated as a polyamine-metabolism disorder, not a glycosphingolipid
synthesis disorder.

The IEMbase inheritance and OMIM pairing should be source-reviewed during import
because the disease label itself names X-linked Snyder-Robinson syndrome.

## Curation actions

- Create or identify an exact SMS / Snyder-Robinson syndrome target before
  import.
- Reject `GM3_Synthase_Deficiency.yaml` as an exact mapping.
- Preserve the N-acetylspermidine, epileptic-encephalopathy, intellectual-
  disability, inheritance, and OMIM prompts for source review.
