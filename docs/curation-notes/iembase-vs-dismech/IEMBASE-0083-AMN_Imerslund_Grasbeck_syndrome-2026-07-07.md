# IEMbase 0083: AMN-related amnionless deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 83 |
| Nosology | 21.9.03.01 |
| Gene | AMN |
| External IDs | OMIM:261100 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | Best fuzzy candidate `Hereditary_Orotic_Aciduria.yaml#Type III` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive AMN-related amnionless deficiency,
with alternate labels Najman-Imerslund-Grasbeck syndrome due to AMN,
megaloblastic anemia-1 Norwegian type, and IGS. The prevalence field records
about 1:200,000 in Finland and Norway. Treatability is marked yes.

The characteristic biochemical signal includes low plasma vitamin B12, elevated
plasma and urinary methylmalonic acid, urinary homocysteine, and elevated total
plasma homocysteine. Additional rows include total plasma protein.

Characteristic clinical rows include megaloblastic anemia, anorexia, apathy,
psychotic behavior, dementia, failure to thrive, and irritability.

The treatment row is cobalamin.

## DisMech phenotype coverage

No standalone DisMech entry for Imerslund-Grasbeck syndrome, amnionless
deficiency, or AMN-related inherited cobalamin malabsorption was found.

`Hereditary_Intrinsic_Factor_Deficiency.yaml` includes differential context for
AMN: it distinguishes CUBN or AMN receptor defects causing
Imerslund-Grasbeck syndrome from CBLIF/GIF intrinsic factor deficiency. This is
not sufficient to count as disease coverage for AMN deficiency.

The best fuzzy candidate, `Hereditary_Orotic_Aciduria.yaml#Type III`, is a false
positive. The shared features are megaloblastic anemia and failure to thrive,
but the mechanisms and diagnostic biochemical signatures are different.

## Concordance and completeness

Judgement: true local gap.

This record should be handled together with the CUBN IGS record. AMN also
collides textually with "adrenomyeloneuropathy" in unrelated X-linked
adrenoleukodystrophy content, so future mapping should key on AMN as the gene
and Imerslund-Grasbeck as the disease context.

## Curation actions

- Keep this IEMbase record unmapped for now.
- Add a future Imerslund-Grasbeck syndrome entry or grouping with AMN and CUBN
  subtype coverage.
- Include cobalamin treatment and the cobalamin-malabsorption biochemical panel
  when the entry is curated.
