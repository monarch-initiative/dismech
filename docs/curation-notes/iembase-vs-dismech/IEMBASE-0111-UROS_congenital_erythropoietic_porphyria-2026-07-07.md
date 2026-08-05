# IEMbase 0111: UROS-related uroporphyrinogen III synthase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 111 |
| Nosology | 17.1.05.01 |
| Gene | UROS |
| External IDs | OMIM:263700; ORPHA:79277 |
| Generated mapping | MAPPED, high confidence |
| Candidate DisMech targets | `Inherited_Porphyria.yaml#Congenital Erythropoietic Porphyria` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as UROS-related uroporphyrinogen III synthase
deficiency, with alternate labels congenital erythropoietic porphyria,
uroporphyrinogen cosynthase deficiency, and CEP. Treatability is marked yes.

The characteristic biochemical rows are increased type I porphyrin isomers in
plasma and urine and increased total porphyrins in plasma and urine across all
ages. The clinical rows are red-brown urine with pink fluorescence and intrinsic
dental staining. The treatment row is avoidance of sunlight.

## DisMech phenotype coverage

`Inherited_Porphyria.yaml` has a congenital erythropoietic porphyria subtype
anchored to UROS. The local entry models UROS loss in erythroid heme synthesis,
uroporphyrin I and coproporphyrin I accumulation, visible-light phototoxicity,
chronic hemolytic anemia, thrombocytopenia, corneal scarring, and cutaneous
photosensitivity.

DisMech also includes management context that is broader than IEMbase:
photoprotection and bone marrow or hematopoietic stem cell transplantation for
severe CEP.

## Concordance and completeness

Judgement: correct subtype-level mapping with complementary detail.

The mapping is concordant for UROS/CEP and for the photosensitive porphyrin
accumulation phenotype. DisMech is more complete for mechanism, hematologic
complications, corneal involvement, and transplant-level treatment. IEMbase is
more granular for the specific laboratory pattern of type I porphyrin isomers
in plasma and urine and for dental staining/red-brown fluorescent urine, which
are not represented as discrete local phenotype rows.

## Curation actions

- Keep the current target as `Inherited_Porphyria.yaml#Congenital
  Erythropoietic Porphyria`.
- Consider adding CEP-specific biochemical rows for plasma/urinary type I
  porphyrin isomers.
- Consider explicit phenotype review for erythrodontia/dental staining and
  red-brown fluorescent urine.
