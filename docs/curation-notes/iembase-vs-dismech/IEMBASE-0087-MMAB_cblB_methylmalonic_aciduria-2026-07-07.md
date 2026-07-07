# IEMbase 0087: MMAB-related methylmalonic aciduria, cblB type

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 87 |
| Nosology | 21.9.15.01 |
| Gene | MMAB |
| External IDs | OMIM:251110 |
| Generated mapping | MAPPED by `alias_exact:cblb` |
| Candidate DisMech targets | `Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml#cblB` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive MMAB-related methylmalonic
aciduria, vitamin B12-responsive cblB type. Treatability is marked yes.

The characteristic clinical rows include acidosis, dehydration, acute
encephalopathic crisis, failure to thrive, ketosis, life-threatening illness,
and vomiting.

The biochemical panel includes elevated urinary and plasma methylmalonic acid,
urinary methylcitric acid, urinary 3-hydroxypropionic acid, C3 propionylcarnitine
in blood or plasma, C3 acylcarnitine ratios, ammonia, anion gap, lactate, total
plasma homocysteine, and free carnitine in dried blood spot or plasma.

Treatment rows include antibiotics, avoidance of fasting, carnitine,
hemodialysis, hydroxycobalamin, liver and/or kidney transplantation,
carglumic acid, peritoneal dialysis, protein-defined diet, sick-day management,
and sodium benzoate.

## DisMech phenotype coverage

The generated mapping to
`Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml#cblB` is correct.

DisMech models cblB as an MMAB subtype impairing adenosylcobalamin synthesis and
producing isolated methylmalonic acidemia. The cobalamin umbrella covers the
adenosylcobalamin branch, impaired methylmalonyl-CoA mutase activity, elevated
methylmalonic acid, and hydroxocobalamin-based treatment context.

`Methylmalonic_Acidemia.yaml` is also relevant secondary coverage. It explicitly
lists MMAB as the cblB complementation group, notes that cblB-type MMA tends to
be more severe than cblA-type, and covers acute decompensation,
propionylcarnitine, methylcitric acid, hyperammonemia, chronic MMA
complications, protein-restricted diet, carnitine, hydroxocobalamin, crisis
management, and transplantation.

## Concordance and completeness

Judgement: correct mapping and high concordance.

The direct subtype target is the cobalamin umbrella. The isolated MMA entry is
useful for severity and management details. IEMbase adds granular emergency and
dialysis rows, plus carglumic acid and sodium benzoate, that are not all
enumerated in the local cblB subtype.

## Curation actions

- Keep the generated mapping to
  `Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml#cblB`.
- Treat `Methylmalonic_Acidemia.yaml` as important secondary context for
  phenotype and management coverage.
- No separate MMAB-only file is needed unless isolated MMA is later split by
  complementation group.
