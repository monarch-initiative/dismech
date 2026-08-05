# IEMbase 0006: PCBD1-related pterin carbinolamine-4a-dehydratase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 6 |
| Nosology | 21.1.07.01 |
| Gene | PCBD1 |
| External IDs | OMIM:264070 |
| Generated mapping | UNMAPPED |
| Likely DisMech target | `kb/disorders/Tetrahydrobiopterin_Deficiency.yaml#PCD Deficiency` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase describes a relatively mild profile. Characteristic clinical entries are
MODY3-like diabetes and transient alteration in tone; additional clinical
coverage is limited to mild hypotonia.

The biochemical profile includes increased plasma phenylalanine, BH4 loading
test response, abnormal pterin profile with primapterin in dried blood spot and
urine, and glucose/magnesium abnormalities.

Treatments are protein-defined diet and sapropterin/BH4 cofactor therapy.

## DisMech phenotype coverage

The generated crosswalk missed an existing subtype. `Tetrahydrobiopterin
Deficiency` includes `PCD Deficiency`, describes PCBD1-related transient
hyperphenylalaninemia with primapterinuria, and notes later MODY and
hypomagnesemia risk.

The top-level DisMech phenotype list does not currently expose the PCD-specific
clinical picture. It primarily covers the broader severe BH4 deficiency
phenotype: neurodevelopmental delay, hypotonia, dystonia, parkinsonism,
seizures, hyperphenylalaninemia, urinary pterin profile, and CSF
neurotransmitter metabolites.

## Concordance and completeness

Judgement: mapping false negative; local identity coverage exists but phenotype
coverage is partial.

DisMech has the correct subtype concept and mechanism, but IEMbase highlights
PCD-specific features that are not explicit as phenotype/biochemical records:
MODY3-like diabetes, hypomagnesemia, primapterinuria, and the comparatively mild
transient tone/hypotonia phenotype.

## Curation actions

- Add aliases or mapper normalization so the IEMbase PCBD1/PCD row maps to the
  `PCD Deficiency` subtype.
- Consider subtype-specific phenotype/biochemical records for primapterinuria,
  hypomagnesemia, and MODY-like diabetes if supported by accepted sources.
- Avoid importing the broad severe BH4 phenotype into PCD without subtype-level
  evidence.
