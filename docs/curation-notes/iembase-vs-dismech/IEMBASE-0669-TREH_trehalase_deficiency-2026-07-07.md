# IEMbase 0669: TREH-related trehalase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 669 |
| Nosology | 3.6.04.02 |
| Nosology code | IEM0319 |
| Gene | TREH |
| External IDs | OMIM:612119; ORPHA:103909 |
| Generated mapping | UNMAPPED; best candidate `Galactosemia.yaml` |
| Candidate DisMech targets | `Trehalase_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive TREH-related trehalase deficiency, also
labeled trehalose intolerance.

The clinical signal is adolescent/adult abdominal pain, diarrhea, and rectal
flatulence. The biochemical row reports normal stool reducing sugars in
adolescence and adulthood.

## DisMech phenotype coverage

`Trehalase_Deficiency.yaml` is an exact local target. It models brush-border
trehalase deficiency due to TREH variants, impaired hydrolysis of dietary
trehalose, and osmotic/fermentative gastrointestinal symptoms after
trehalose-containing foods, especially mushrooms. It also records that many
people can be asymptomatic or mildly affected.

The local entry includes diarrhea, vomiting, abdominal distention/flatulence,
dietary avoidance of trehalose-containing foods, oral trehalose tolerance
testing, and small-intestinal disaccharidase assay context.

The generated `Galactosemia.yaml` candidate is a sugar-intolerance false
positive and should not be used.

## Concordance and completeness

Judgement: false negative from stale generated mapping; current DisMech has an
exact TREH target.

IEMbase is more concise than DisMech, but the symptom direction is concordant:
post-dietary carbohydrate intolerance presenting as abdominal pain, diarrhea,
and flatulence. The normal stool reducing-sugars row is a useful diagnostic
caveat to preserve.

## Curation actions

- Resolve this record to `Trehalase_Deficiency.yaml`.
- Reject `Galactosemia.yaml` as the generated candidate.
- Preserve normal stool reducing sugars and adolescent/adult GI timing if row
  completeness is reviewed.
- Map rectal flatulence to the local flatulence/abdominal-distention phenotype
  concept if importing.
