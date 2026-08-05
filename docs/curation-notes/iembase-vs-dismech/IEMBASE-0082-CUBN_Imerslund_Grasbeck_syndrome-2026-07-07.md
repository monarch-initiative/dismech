# IEMbase 0082: CUBN-related cubilin deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 82 |
| Nosology | 21.9.02.01 |
| Gene | CUBN |
| External IDs | OMIM:261100 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | Best fuzzy candidate `Hereditary_Orotic_Aciduria.yaml#Type III` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive CUBN-related cubilin deficiency,
with alternate labels Najman-Imerslund-Grasbeck syndrome due to CUBN,
megaloblastic anemia-1 Finnish type, and IGS. The prevalence field records
about 1:200,000 in Finland and Norway. Treatability is marked unknown.

The characteristic biochemical signal includes low plasma vitamin B12, elevated
plasma and urinary methylmalonic acid, urinary homocysteine, and elevated total
plasma homocysteine. Additional rows include total plasma protein.

Characteristic clinical rows include megaloblastic anemia, anorexia, apathy,
psychotic behavior, dementia, failure to thrive, and irritability.

No treatment rows are present in the cached IEMbase record.

## DisMech phenotype coverage

No standalone DisMech entry for Imerslund-Grasbeck syndrome, cubilin deficiency,
or CUBN-related inherited cobalamin malabsorption was found.

`Hereditary_Intrinsic_Factor_Deficiency.yaml` includes useful differential
context: it states that CUBN or AMN receptor defects cause Imerslund-Grasbeck
syndrome, while GIF/CBLIF causes intrinsic factor deficiency. That is contextual
coverage only, not a modeled DisMech disease entry for CUBN deficiency.

The best fuzzy candidate, `Hereditary_Orotic_Aciduria.yaml#Type III`, is a false
positive driven by shared megaloblastic anemia/failure-to-thrive language.
Hereditary orotic aciduria is a UMPS and orotic-acid disorder, not a cobalamin
receptor-malabsorption disorder.

## Concordance and completeness

Judgement: true local gap.

The record should not be forced into hereditary intrinsic factor deficiency
because the local CBLIF entry explicitly treats Imerslund-Grasbeck syndrome as a
differential diagnosis with a different receptor-gene mechanism.

## Curation actions

- Keep this IEMbase record unmapped for now.
- Add a future Imerslund-Grasbeck syndrome entry or grouping with CUBN and AMN
  subtype coverage.
- Prioritize cobalamin malabsorption, methylmalonic acid/homocysteine readouts,
  megaloblastic anemia, neuropsychiatric rows, and proteinuria if supported by
  future curation evidence.
