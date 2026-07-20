# IEMbase 0114: UROD-related hepatic uroporphyrinogen decarboxylase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 114 |
| Nosology | 17.1.06.01 |
| Gene | UROD |
| External IDs | OMIM:176100; ORPHA:95159 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | `Inherited_Porphyria.yaml#Familial Porphyria Cutanea Tarda`; `Inherited_Porphyria.yaml#Hepatoerythropoietic Porphyria` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as UROD-related hepatic uroporphyrinogen decarboxylase
deficiency, with alternate labels porphyria cutanea tarda type I, II and III,
hepatoerythropoietic porphyria, and PCT. Treatability is marked yes.

The characteristic biochemical rows are increased heptacarboxylporphyrin in
plasma and urine, increased total porphyrins in plasma and urine, and increased
urocarboxylporphyrin in plasma and urine. The only clinical row is liver
dysfunction. Hemin is listed as pharmacological treatment.

## DisMech phenotype coverage

The generated unmapped status is partly a false negative. `Inherited_Porphyria.yaml`
already includes both UROD-related subtypes relevant to the IEMbase label:
familial porphyria cutanea tarda and hepatoerythropoietic porphyria. The local
entry captures UROD pathogenic variants, bullous photodermatitis/cutaneous
photosensitivity, and biallelic UROD-related hepatoerythropoietic porphyria.

However, DisMech does not yet provide a standalone PCT model and does not expose
the IEMbase biochemical pattern of urinary/plasma heptacarboxylporphyrin and
urocarboxylporphyrin as discrete biomarkers.

## Concordance and completeness

Judgement: false negative to existing subtype-level coverage, but the IEMbase
entity spans multiple UROD-related clinical categories.

The local entry is concordant for UROD-related PCT/HEP as inherited porphyria
subtypes and is stronger for disease-mechanism classification. IEMbase is more
specific for the diagnostic porphyrin fraction profile and liver-dysfunction
row. The treatment listing is discordant or at least suspicious for routine PCT:
hemin is a core acute hepatic porphyria therapy, whereas PCT management commonly
requires a separate treatment review rather than automatic inheritance from
acute porphyria treatment.

## Curation actions

- Resolve to `Inherited_Porphyria.yaml#Familial Porphyria Cutanea Tarda` and
  `#Hepatoerythropoietic Porphyria` rather than leaving this as no target.
- Review whether the local PCT/HEP subtype split needs a standalone PCT entry or
  richer subtype-specific phenotypes.
- Add or review UROD-specific biochemical markers before importing IEMbase's
  hemin treatment row.
