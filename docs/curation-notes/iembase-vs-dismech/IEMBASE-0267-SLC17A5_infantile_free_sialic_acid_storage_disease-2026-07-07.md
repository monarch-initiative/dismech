# IEMbase 0267: SLC17A5-related Sialin deficiency, severe

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 267 |
| Nosology | 3.6.02.01 |
| Gene | SLC17A5 |
| External IDs | OMIM:269920; ORPHA:309334 |
| Generated mapping | AMBIGUOUS; `Free_Sialic_Acid_Storage_Disease.yaml#Salla Disease` and `Salla_Disease.yaml` |
| Candidate DisMech targets | `Free_Sialic_Acid_Storage_Disease.yaml#Infantile Free Sialic Acid Storage Disease`; `Salla_Disease.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as severe SLC17A5-related sialin deficiency, with
alternate labels infantile sialic acid storage disease, Salla disease, and
ISSD. The record is autosomal recessive and treatability is marked unknown,
with no treatment rows in the cached JSON.

Biochemical rows include increased urinary N-acetylneuraminic acid in the
neonatal, infancy, and childhood periods. Clinical rows include ataxia, distal
phalanges hypoplasia, fetal hydrops, growth retardation, hip dysplasia,
hypotonia, nystagmus, skeletal abnormalities, and widened metaphyses of the
elbows and knees.

## DisMech phenotype coverage

`Free_Sialic_Acid_Storage_Disease.yaml#Infantile Free Sialic Acid Storage
Disease` is the best canonical target. The local umbrella entry represents the
SLC17A5/FSASD severity spectrum and explicitly includes the severe infantile
subtype, historically called infantile free sialic acid storage disease or
ISSD. It covers impaired sialin-mediated lysosomal export, free
N-acetylneuraminic acid accumulation, increased free sialic acid, severe
developmental delay, coarse facial features, hepatosplenomegaly, cardiomegaly,
early mortality, fetal hydrops, hypotonia, ataxia, nystagmus, seizures, white
matter disease, genetic testing, supportive care, genetic counseling, and
investigational base editing.

`Salla_Disease.yaml` is useful secondary context for the milder classic Salla
end of the same spectrum, but it is not the best canonical target for this
severe/ISSD IEMbase record.

## Concordance and completeness

Judgement: generated ambiguity should resolve to the FSASD umbrella's infantile
subtype, not to standalone classic Salla disease.

IEMbase and DisMech agree on SLC17A5/sialin identity, autosomal recessive
inheritance, free sialic acid/N-acetylneuraminic acid accumulation, severe
infantile disease framing, fetal hydrops, hypotonia, ataxia, and nystagmus.
IEMbase adds skeletal specificity for distal phalangeal hypoplasia, hip
dysplasia, widened metaphyses, growth retardation, and skeletal abnormalities.
DisMech is richer for mechanism, severity spectrum, neurodevelopmental course,
visceral/cardiac features, and treatment/reproductive counseling context.

## Curation actions

- Resolve this record to
  `Free_Sialic_Acid_Storage_Disease.yaml#Infantile Free Sialic Acid Storage Disease`.
- Keep `Salla_Disease.yaml` as secondary spectrum context only.
- Use IEMbase's skeletal and growth rows as enrichment prompts for the severe
  infantile FSASD subtype.
