# IEMbase 0205: neonatal hemochromatosis

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 205 |
| Nosology | 22.2.17.01 |
| Gene | NOGENE |
| External IDs | OMIM:231100; ORPHA:446 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | `Hemochromatosis.yaml` is a false-positive pathway/label neighbor |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as neonatal hemochromatosis, with alternate labels
congenital alloimmune hepatitis and NH. Treatability is marked unknown.

The biochemical rows include increased serum ferritin, increased liver iron,
and increased transferrin saturation. The characteristic clinical row is liver
fibrosis. No additional clinical or treatment rows are listed in this cached
record.

## DisMech phenotype coverage

`Hemochromatosis.yaml` is not a valid target for this record. The local entry
models hereditary hemochromatosis due to HFE and non-HFE hepcidin-pathway genes
such as HJV, HAMP, TFR2, BMP6, and SLC40A1. IEMbase 0205 instead represents a
neonatal/congenital alloimmune liver disease label with no causal gene and a
neonatal iron-overload/liver-fibrosis phenotype. That entity should not be
collapsed into adult or juvenile inherited hepcidin-deficiency hemochromatosis.

## Concordance and completeness

Judgement: true local gap; generated best candidate is not equivalent.

IEMbase and local hemochromatosis share generic iron-overload terms such as high
ferritin, high liver iron, high transferrin saturation, and fibrosis. The
identity, scope, and mechanism differ: neonatal hemochromatosis/congenital
alloimmune hepatitis is not HFE/HJV/HAMP/TFR2-type hereditary hemochromatosis.

## Curation actions

- Do not map this record to `Hemochromatosis.yaml`.
- Consider a future neonatal hemochromatosis / gestational alloimmune liver
  disease entry if this entity is in DisMech scope.
- Seed that future entry with neonatal liver fibrosis, high ferritin, high
  hepatic iron, high transferrin saturation, and the congenital alloimmune
  hepatitis/GALD scope distinction.
