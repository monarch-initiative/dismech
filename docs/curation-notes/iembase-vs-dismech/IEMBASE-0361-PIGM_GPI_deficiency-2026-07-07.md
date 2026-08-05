# IEMbase 0361: PIGM-related glycosylphosphatidylinositol deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 361 |
| Nosology | 18.3.00.12 |
| Gene | PIGM |
| External IDs | OMIM:610293; ORPHA:83639 |
| Generated mapping | UNMAPPED; low candidate `MHC_Class_II_Deficiency.yaml` |
| Candidate DisMech targets | No exact local target identified |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents PIGM-CDG/glycosylphosphatidylinositol deficiency, an
autosomal recessive phosphatidylinositolglycan class M disorder. Characteristic
rows include absence seizures, hepatic vein thrombosis, and portal vein
thrombosis.

Additional clinical rows include developmental delay, prominent skin veins, and
cerebral thrombosis. The biochemical row is flow cytometry of GPI markers.
IEMbase lists sodium phenylbutyrate as a treatment.

## DisMech phenotype coverage

The low MHC class II deficiency candidate is a false neighbor and should be
rejected. Local MHC class II deficiency is an immune transcription/antigen
presentation disorder involving CIITA/RFX genes; it does not cover PIGM, GPI
anchor biosynthesis, thrombosis, or GPI-marker flow cytometry.

No exact PIGM-CDG DisMech disease file was identified. Any local inherited GPI
deficiency family context would be pathway context only and should not be used
as a disease-level mapping unless it explicitly covers PIGM.

## Concordance and completeness

Judgement: true local gap; reject the generated MHC class II deficiency
candidate.

IEMbase supplies a distinctive PIGM-CDG signal: PIGM identity, autosomal
recessive inheritance, absence seizures, developmental delay, venous thromboses
in hepatic, portal, and cerebral sites, prominent skin veins, diagnostic
flow-cytometry GPI marker testing, and sodium phenylbutyrate treatment.

## Curation actions

- Do not map this record to `MHC_Class_II_Deficiency.yaml`.
- Create or prioritize a future PIGM-CDG/GPI anchor biosynthesis target if this
  disease enters active DisMech curation.
- Treat sodium phenylbutyrate, thrombosis, prominent skin veins, and
  flow-cytometry GPI markers as high-value enrichment prompts for future
  source-backed curation.
