# IEMbase 0640: RXYLT1-related muscular dystrophy-dystroglycanopathy type A

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 640 |
| Nosology | 18.2.1.01 |
| Gene | RXYLT1 |
| External IDs | OMIM:615041; ORPHA:51577 |
| Generated mapping | MAPPED; `Lissencephaly_Spectrum_Disorders.yaml#Cobblestone` |
| Candidate DisMech targets | Better primary target: `Dystroglycanopathy.yaml`; phenotype-level target: `Lissencephaly_Spectrum_Disorders.yaml#Cobblestone` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive RXYLT1-CDG / muscular
dystrophy-dystroglycanopathy with congenital brain and eye anomalies, type A.

Biochemical rows include markedly increased plasma creatine kinase from the
neonatal period through adolescence, normal serum sialotransferrins, and an
abnormal matriglycan-specific antibody readout across ages. Clinical rows
emphasize optional cerebellar dysplasia, cobblestone lissencephaly, retinal
dysplasia, intellectual disability, gonadal dysgenesis, and neonatal neural
tube defect. Characteristic rows are hypotonia and muscular dystrophy.

## DisMech phenotype coverage

The generated `Lissencephaly_Spectrum_Disorders.yaml#Cobblestone` match is a
phenotype-level match, not a good disease-level target. That subtype captures
cobblestone lissencephaly as a dystroglycanopathy-associated lissencephaly
form, but it lists POMGNT1, POMT1, and POMT2 and does not model RXYLT1, CK
elevation, matriglycan readout, muscular dystrophy, or the CDG/dystroglycan
mechanism.

`Dystroglycanopathy.yaml` is the stronger local target. It includes an
`MDDG10 (RXYLT1)` gene subtype, a type A severity subtype, defective
alpha-dystroglycan O-mannosyl glycosylation, reduced matriglycan/laminin
binding readouts, muscular dystrophy, elevated CK, cobblestone lissencephaly,
intellectual disability, retinal dysplasia, seizures, hydrocephalus, and
neonatal hypotonia.

## Concordance and completeness

Judgement: locally covered at dystroglycanopathy-spectrum level, but the
generated disease-level mapping is misleading.

DisMech captures the core RXYLT1 mechanism and most of the IEMbase type A
phenotype signal if `Dystroglycanopathy.yaml` is used as the target. It does
not yet provide a single explicit RXYLT1 type A cross-product subtype, and the
RXYLT1-specific note is thinner than the general dystroglycanopathy mechanism.
IEMbase-specific prompts not clearly captured locally include gonadal
dysgenesis and neural tube defect.

## Curation actions

- Prefer `Dystroglycanopathy.yaml` over the lissencephaly-spectrum target for
  disease-level mapping.
- Keep the lissencephaly cobblestone subtype as phenotype-level context only.
- If row-level precision is needed, add or annotate an RXYLT1 / MDDG10 type A
  subtype under dystroglycanopathy.
- Preserve RXYLT1, CK elevation, normal sialotransferrins, abnormal matriglycan
  antibody, hypotonia, muscular dystrophy, cobblestone/cerebellar/retinal, ID,
  gonadal, and neural-tube prompts.
