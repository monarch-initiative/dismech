# IEMbase 0390: TRIP11-related Achondrogenesis type IA (CDG)

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 390 |
| Nosology | 19.6.09.01 |
| Gene | TRIP11 |
| External IDs | OMIM:200600; ORPHA:93299 |
| Generated mapping | UNMAPPED; low candidate `Achondrogenesis_Type_II.yaml` |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive TRIP11-related achondrogenesis type IA,
also listed as Husron-Harris type and GMAP210-CDG. The cached record is sparse:
clinical rows include achondrogenesis type IA, deficient ossification,
micromelia, stillbirth, early death, and macrocephaly due to soft-tissue edema.
The only biochemical row is serum sialotransferrins without a directionality
signal. There are no treatment rows.

## DisMech phenotype coverage

There is no exact local DisMech target for TRIP11/GMAP210-CDG. The generated
candidate `Achondrogenesis_Type_II.yaml` is a phenotype-neighbor false positive.
Local achondrogenesis type II models COL2A1/type II collagenopathy with
autosomal dominant or de novo inheritance, not TRIP11/GMAP210-related Golgi
trafficking disease.

The local ACG2 file contains a deep-research reference title for
achondrogenesis type IA/Houston-Harris, but that is not curated disease
coverage and does not establish a TRIP11 target.

## Concordance and completeness

Judgement: true TRIP11 achondrogenesis IA local gap; reject ACG2 as an exact
mapping.

The IEMbase and local candidate share lethal skeletal dysplasia features such
as micromelia, deficient ossification, and perinatal lethality. They differ in
gene, inheritance, mechanism, and disease identity.

## Curation actions

- Keep this record unmapped until a TRIP11/GMAP210-CDG or achondrogenesis IA
  target exists.
- Do not map to `Achondrogenesis_Type_II.yaml`.
- If curated, preserve the lethal skeletal dysplasia features, deficient
  ossification, soft-tissue edema/macrocephaly, stillbirth/early-death signal,
  autosomal recessive inheritance, and TRIP11/GMAP210 Golgi-trafficking frame.
