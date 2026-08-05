# IEMbase 0653: TPI1-related triosephosphate isomerase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 653 |
| Nosology | 3.3.09.01 |
| Nosology code | IEM0382 |
| Gene | TPI1 |
| External IDs | OMIM:615512; ORPHA:868 |
| Generated mapping | UNMAPPED; weak candidate `Hereditary_Intrinsic_Factor_Deficiency.yaml` |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive TPI1-related triosephosphate isomerase
deficiency, also labeled hemolytic anemia due to triosephosphate isomerase
deficiency and hereditary nonspherocytic hemolytic anemia due to
triosephosphate isomerase deficiency. Treatability is marked no.

Biochemical rows include decreased red-cell triosephosphate isomerase activity
and increased red-cell dihydroxyacetone phosphate. Clinical rows include
recurrent infections and hemolytic anemia, with optional cardiomyopathy,
dystonia, progressive muscle weakness, seizures, stroke, tremor, and
intellectual disability.

## DisMech phenotype coverage

`Hereditary_Intrinsic_Factor_Deficiency.yaml` is a false candidate based on
anemia wording. It models CBLIF/GIF-related cobalamin absorption failure,
methylmalonic aciduria, hyperhomocysteinemia, megaloblastic anemia, and vitamin
B12 replacement. It does not model glycolysis, TPI1, red-cell TPI activity,
dihydroxyacetone phosphate, nonspherocytic hemolysis, or the neuromuscular and
cardiac complications of TPI deficiency.

Local hemolytic-anemia entries and modules provide broad anemia context, but no
TPI1-specific disease anchor was found.

## Concordance and completeness

Judgement: true local TPI1 / triosephosphate isomerase deficiency gap.

The generated candidate should be rejected because the anemia mechanism is
different: cobalamin-dependent megaloblastic erythropoiesis versus a glycolytic
enzyme defect causing hemolytic anemia with systemic neurologic and muscular
features.

## Curation actions

- Keep this row unmapped until a TPI1 / triosephosphate isomerase deficiency
  target exists.
- Do not map to `Hereditary_Intrinsic_Factor_Deficiency.yaml`.
- Preserve red-cell TPI activity, dihydroxyacetone phosphate, hemolytic anemia,
  recurrent infections, cardiomyopathy, dystonia, progressive weakness,
  seizures, stroke, tremor, and intellectual-disability prompts.
