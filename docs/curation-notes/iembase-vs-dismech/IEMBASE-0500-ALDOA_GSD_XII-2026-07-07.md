# IEMbase 0500: ALDOA-related aldolase A deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 500 |
| Nosology | 3.3.08.01 |
| Gene | ALDOA |
| External IDs | OMIM:611881; ORPHA:57 |
| Generated mapping | CANDIDATE; MEDIUM; `Glycogen_Storage_Disease_Type_I.yaml` |
| Candidate DisMech targets | `Glycogen_Storage_Disease_Type_I.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive ALDOA-related aldolase A deficiency as
glycogen storage disease type 12. No treatments are listed. Biochemical rows
include decreased RBC aldolase A activity, normal-to-increased plasma creatine
kinase, normal-to-increased liver and muscle glycogen, increased plasma
bilirubin, and increased blood reticulocytes. Clinical rows include hemolytic
anemia, optional rhabdomyolysis, muscle weakness, intellectual disability, short
stature, dysmorphic features, low-set ears, thin lips, triangular face, and wide
mouth.

## DisMech phenotype coverage

`Glycogen_Storage_Disease_Type_I.yaml` is not the correct target. The local GSD
I entry covers G6PC1/SLC37A4 glucose-6-phosphatase system deficiency and its
hepatic/renal metabolic consequences. It does not model ALDOA, aldolase A
enzyme deficiency, congenital nonspherocytic hemolytic anemia, or the
dysmorphic/neurodevelopmental features described by IEMbase.

`Glycogen_Storage_Disease_Type_VII.yaml` has a partial phenotypic neighbor in
the form of glycolytic myopathy plus hemolytic anemia, but that file is
PFKM/Tarui disease and should not be used as exact ALDOA coverage.

## Concordance and completeness

Judgement: false-positive candidate; true ALDOA/GSD XII local gap.

The generated candidate shares only "glycogen storage disease" vocabulary.
IEMbase's source disease combines glycolytic enzyme deficiency, RBC hemolysis,
muscle involvement, and developmental/dysmorphic features. The candidate
DisMech file is a different carbohydrate-metabolism disorder centered on
hepatic glucose release.

## Curation actions

- Do not map this record to `Glycogen_Storage_Disease_Type_I.yaml`.
- Track ALDOA-related aldolase A deficiency / GSD XII as a local curation gap.
- Preserve IEMbase prompts for RBC aldolase activity, hemolytic anemia,
  bilirubin/reticulocyte abnormalities, rhabdomyolysis, dysmorphic features,
  short stature, and intellectual disability for a future exact entry.
