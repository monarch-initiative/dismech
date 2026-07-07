# IEMbase 0080: CBLIF-related intrinsic factor deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 80 |
| Nosology | 21.9.01.01 |
| Gene | CBLIF |
| External IDs | OMIM:261000 |
| Generated mapping | MAPPED by `alias_exact:congenital pernicious anemia` |
| Candidate DisMech targets | `Hereditary_Intrinsic_Factor_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive CBLIF-related intrinsic factor
deficiency, with alternate labels congenital pernicious anemia, TCN III/TCN3
deficiency, and IFD. Treatability is marked yes.

The characteristic biochemical signal includes low plasma vitamin B12, elevated
plasma and urinary methylmalonic acid, and elevated total plasma homocysteine.
Additional rows include urinary homocysteine and total plasma protein.

Characteristic clinical rows include megaloblastic anemia, anorexia, apathy,
failure to thrive, and irritability.

The treatment row is vitamin B12.

## DisMech phenotype coverage

The generated mapping to `Hereditary_Intrinsic_Factor_Deficiency.yaml` is
correct.

DisMech models hereditary intrinsic factor deficiency as a rare autosomal
recessive cobalamin-absorption disorder caused by CBLIF/GIF variants. It covers
loss of gastric intrinsic factor, impaired intrinsic factor-dependent cobalamin
absorption, low serum cobalamin, methylmalonic aciduria, homocysteine
accumulation, megaloblastic and macrocytic anemia, pancytopenia,
gastrointestinal symptoms, neurologic abnormalities, and lifelong vitamin B12 or
hydroxocobalamin replacement.

The local entry also explicitly distinguishes CBLIF/GIF intrinsic factor
deficiency from CUBN/AMN Imerslund-Grasbeck syndrome in its differential
diagnoses.

## Concordance and completeness

Judgement: correct mapping and high concordance.

IEMbase is more compact, while DisMech is stronger for mechanism, differential
diagnosis, and treatment rationale. IEMbase adds specific clinical rows for
anorexia, apathy, and irritability that are not prominent in the local entry,
but these do not change the mapping decision.

## Curation actions

- Keep the generated mapping to `Hereditary_Intrinsic_Factor_Deficiency.yaml`.
- No separate CBLIF-only file is needed.
- Consider IEMbase's anorexia, apathy, irritability, and total-protein rows as
  optional future phenotype/biochemical enrichments.
