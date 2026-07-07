# IEMbase 0466: SLC25A38-related mitochondrial glycine transporter deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 466 |
| Nosology | 11.1.07.01 |
| Gene | SLC25A38 |
| External IDs | OMIM:205950; ORPHA:260305 |
| Generated mapping | UNMAPPED; low candidate `Primary_Carnitine_Deficiency.yaml` |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive SLC25A38-related mitochondrial glycine
transporter deficiency, also called pyridoxine-refractory sideroblastic anemia
type 2. The biochemical row records increased serum ferritin. Characteristic
clinical rows include microcytic hypochromic anemia, sideroblastic anemia, and
hepatosplenomegaly. There are no treatment rows.

## DisMech phenotype coverage

There is no exact local DisMech target for SLC25A38-related sideroblastic
anemia type 2. Local sideroblastic-anemia context exists in entries such as
`Myopathy_Lactic_Acidosis_and_Sideroblastic_Anemia.yaml` and
`Pearson_Syndrome.yaml`, but those model different diseases and mechanisms:
PUS1/YARS2/MT-ATP6 mitochondrial translation or complex V disease in MLASA, and
mitochondrial DNA deletion disease in Pearson syndrome. They are not a
SLC25A38 mitochondrial glycine transporter deficiency target.

The generated `Primary_Carnitine_Deficiency.yaml` candidate is a false
positive. Local primary carnitine deficiency is SLC22A5/OCTN2-mediated systemic
carnitine depletion with fatty-acid oxidation failure, cardiomyopathy, and
metabolic decompensation, not congenital sideroblastic anemia.

## Concordance and completeness

Judgement: true SLC25A38 sideroblastic anemia type 2 local gap; reject primary
carnitine deficiency as an exact mapping.

The only overlap with local files is broad anemia or mitochondrial wording. The
source gene, heme/sideroblast phenotype, and proximal transporter mechanism are
not represented by the generated candidate or by the existing MLASA/Pearson
contexts.

## Curation actions

- Keep this record unmapped until an SLC25A38 mitochondrial glycine transporter
  deficiency or sideroblastic anemia type 2 target exists.
- Do not map to `Primary_Carnitine_Deficiency.yaml`.
- Do not reuse MLASA, Pearson syndrome, or ALAS2 sideroblastic-anemia context as
  an exact target.
- If curated, include SLC25A38, autosomal recessive inheritance, mitochondrial
  glycine transport/heme-biosynthesis context, increased ferritin, microcytic
  hypochromic anemia, sideroblastic anemia, and hepatosplenomegaly.
