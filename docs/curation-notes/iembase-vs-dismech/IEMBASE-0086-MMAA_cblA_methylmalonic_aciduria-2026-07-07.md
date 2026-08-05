# IEMbase 0086: MMAA-related methylmalonic aciduria, cblA type

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 86 |
| Nosology | 21.9.14.01 |
| Gene | MMAA |
| External IDs | OMIM:251100 |
| Generated mapping | MAPPED by `alias_exact:cbla` |
| Candidate DisMech targets | `Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml#cblA` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive MMAA-related methylmalonic
aciduria, vitamin B12-responsive cblA type. Treatability is marked yes.

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
`Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml#cblA` is correct.

DisMech models cblA as an MMAA subtype impairing mitochondrial
adenosylcobalamin handling, producing isolated and often B12-responsive
methylmalonic acidemia. The cobalamin umbrella covers the adenosylcobalamin
pathway, impaired methylmalonyl-CoA mutase activity, methylmalonic aciduria, and
hydroxocobalamin-based management.

`Methylmalonic_Acidemia.yaml` is also relevant secondary coverage. It explicitly
lists MMAA as the cblA complementation group, covers isolated MMA acute
decompensation, methylmalonic and methylcitric acid accumulation,
propionylcarnitine, hyperammonemia, protein-restricted diet,
hydroxocobalamin responsiveness, carnitine, crisis management, and liver or
combined liver-kidney transplantation.

## Concordance and completeness

Judgement: correct mapping and high concordance.

The cobalamin umbrella is the best direct subtype target, while the isolated MMA
entry provides richer acute-decompensation and treatment coverage. IEMbase adds
granular emergency and dialysis rows, plus carglumic acid and sodium benzoate,
that are not all enumerated in the local cblA subtype.

## Curation actions

- Keep the generated mapping to
  `Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml#cblA`.
- Treat `Methylmalonic_Acidemia.yaml` as important secondary context for
  phenotype and management coverage.
- No separate MMAA-only file is needed unless isolated MMA is later split by
  complementation group.
