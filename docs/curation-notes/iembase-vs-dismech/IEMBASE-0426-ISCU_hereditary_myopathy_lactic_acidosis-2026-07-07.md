# IEMbase 0426: ISCU-related hereditary myopathy with lactic acidosis

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 426 |
| Nosology | 8.2.1.01 |
| Gene | ISCU |
| External IDs | OMIM:255125; ORPHA:43115 |
| Generated mapping | UNMAPPED; low candidate `Charcot-Marie-Tooth_Disease.yaml#HNPP` |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents ISCU-related hereditary myopathy with lactic acidosis (HML),
an autosomal recessive disorder of lipoic-acid and iron-sulfur metabolism.
Biochemical rows include markedly increased plasma lactate, reduced muscle
aconitase, reduced muscle SDH histochemistry, decreased complexes I-III
activity, normal-to-increased or increased creatine kinase, and increased
urinary myoglobin. Clinical rows include exercise intolerance, muscle weakness,
myopathy, myoglobinuria, rhabdomyolysis, and occasional cardiomyopathy. There
are no treatment rows.

## DisMech phenotype coverage

There is no exact local DisMech target for ISCU-related hereditary myopathy with
lactic acidosis. The generated HNPP/Charcot-Marie-Tooth candidate is a false
positive: local CMT/HNPP entries concern inherited peripheral neuropathy,
especially PMP22 duplication/deletion, Schwann-cell dysfunction, and
length-dependent neuropathy or pressure palsies. They do not cover ISCU,
iron-sulfur cluster biogenesis, aconitase/SDH deficiency, exercise-induced
lactic acidosis, rhabdomyolysis, or myoglobinuria.

Local Friedreich ataxia mentions ISCU2 only as part of the mitochondrial Fe-S
cluster assembly machinery affected secondarily by frataxin deficiency; it is
not an ISCU-HML disease entry.

## Concordance and completeness

Judgement: true local gap; reject the CMT/HNPP candidate.

IEMbase's signal is a metabolic mitochondrial myopathy with iron-sulfur cluster
enzyme defects and exercise-triggered lactic acidosis. The candidate is a
phenotype-neighbor neuropathy grouping and does not share gene, proximal
mechanism, biochemical signature, or clinical course.

## Curation actions

- Keep this record unmapped until an ISCU hereditary myopathy with lactic
  acidosis target exists.
- Do not map to `Charcot-Marie-Tooth_Disease.yaml` or HNPP.
- If curated, include ISCU, autosomal recessive inheritance, Fe-S cluster
  biogenesis, reduced aconitase/SDH/complex I-III activity, lactate, exercise
  intolerance, myopathy, muscle weakness, rhabdomyolysis, myoglobinuria, and
  cardiomyopathy as an occasional feature.
