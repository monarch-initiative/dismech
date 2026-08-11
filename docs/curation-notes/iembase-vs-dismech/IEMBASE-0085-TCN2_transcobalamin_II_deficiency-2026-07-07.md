# IEMbase 0085: TCN2-related transcobalamin II deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 85 |
| Nosology | 21.9.05.01 |
| Gene | TCN2 |
| External IDs | OMIM:275350 |
| Generated mapping | MAPPED by `alias_exact:tcn2 deficiency` |
| Candidate DisMech targets | `Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml#TCN2 deficiency` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive TCN2-related transcobalamin 2
deficiency, with alternate labels transcobalamin II deficiency, TCN2 deficiency,
and TCD. Treatability is marked yes.

The characteristic biochemical signal includes low plasma vitamin B12, elevated
plasma and urinary methylmalonic acid, urinary homocysteine, and elevated total
plasma homocysteine.

Characteristic clinical rows include megaloblastic anemia, apathy, chronic
diarrhea, and failure to thrive.

Treatment rows are cyanocobalamin and hydroxycobalamin.

## DisMech phenotype coverage

The generated mapping to
`Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml#TCN2 deficiency` is
correct.

DisMech represents transcobalamin II deficiency as a subtype of the broader
cobalamin metabolism and transport umbrella. The local pathophysiology covers
defective cobalamin absorption, transport, and cellular uptake with TCN2 as an
explicit gene, decreased cobalamin transport, reduced cobalamin availability,
downstream impaired active-cofactor synthesis, methylmalonic aciduria,
homocystinuria, megaloblastic anemia, failure to thrive, and hydroxocobalamin
therapy.

## Concordance and completeness

Judgement: correct subtype mapping and high concordance.

IEMbase is more TCN2-specific for chronic diarrhea and apathy, while DisMech is
stronger for umbrella mechanism and treatment rationale. DisMech also includes
immunodeficiency in the TCN2 subtype description, a clinically useful detail not
prominent in the IEMbase characteristic rows.

## Curation actions

- Keep the generated mapping to
  `Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml#TCN2 deficiency`.
- No separate TCN2-only file is needed unless the project later splits
  transport disorders out of the cobalamin umbrella.
- Consider chronic diarrhea, apathy, and explicit cyanocobalamin treatment as
  optional future subtype enrichments.
