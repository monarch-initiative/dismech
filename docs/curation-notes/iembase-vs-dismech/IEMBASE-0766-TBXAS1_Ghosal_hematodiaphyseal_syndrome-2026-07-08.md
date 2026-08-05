# IEMbase 0766: TBXAS1-related thromboxane synthase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 766 |
| Nosology | 14.3.01.01 |
| Nosology code | IEM0684 |
| Gene | TBXAS1 |
| External IDs | OMIM:231095; ORPHA:1802 |
| Generated mapping | UNMAPPED; weak candidate `3-Hydroxy-3-Methylglutaryl-CoA_Synthase_Deficiency.yaml` |
| Candidate DisMech targets | None exact |
| Review date | 2026-07-08 |

## IEMbase phenotype signal

IEMbase labels this autosomal recessive record as TBXAS1-related thromboxane
synthase deficiency, with alternate name Ghosal hematodiaphyseal syndrome. The
source signal combines skeletal dysplasia and hematologic disease:
diaphyseal and metaphyseal thickening from neonatal stages onward, anemia,
large-bone swelling or pain, leukocytosis, thrombocytopenia, splenomegaly, and
adolescent/adult cutis verticis gyrata.

## DisMech phenotype coverage

No exact TBXAS1 / Ghosal hematodiaphyseal syndrome entry is present locally.
The generated `3-Hydroxy-3-Methylglutaryl-CoA_Synthase_Deficiency.yaml`
candidate is a false positive. HMGCS2 deficiency is a ketogenesis disorder with
hypoketotic metabolic decompensation and does not cover thromboxane synthase
deficiency, hematodiaphyseal dysplasia, or the TBXAS1 gene.

Primary hypertrophic osteoarthropathy is also only phenotype context for
eicosanoid-related bone and skin findings; it is a distinct HPGD/SLCO2A1-PGE2
disorder and should not be used as TBXAS1 coverage.

## Concordance and completeness

Judgement: true local gap.

The IEMbase record is specific for Ghosal hematodiaphyseal syndrome and should
be curated as a distinct eicosanoid/thromboxane pathway disease. Existing
ketogenesis and prostaglandin E2 entries do not represent its identity or
mechanism.

## Curation actions

- Add a distinct TBXAS1 / Ghosal hematodiaphyseal syndrome target before
  treating this record as covered.
- Reject `3-Hydroxy-3-Methylglutaryl-CoA_Synthase_Deficiency.yaml` as exact
  coverage.
- Preserve diaphyseal/metaphyseal thickening, anemia, bone pain or swelling,
  thrombocytopenia, leukocytosis, splenomegaly, and cutis verticis gyrata as
  curation prompts.
