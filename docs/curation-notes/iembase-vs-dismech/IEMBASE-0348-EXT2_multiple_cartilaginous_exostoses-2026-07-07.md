# IEMbase 0348: EXT2-related multiple cartilaginous exostoses type II

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 348 |
| Nosology | 18.2.07.01 |
| Gene | EXT2 |
| External IDs | OMIM:133701; ORPHA:52022 |
| Generated mapping | UNMAPPED; low candidate `Multiple_Synostoses_Syndrome.yaml` |
| Candidate DisMech targets | No exact target; `Chondrosarcoma.yaml` is downstream context only |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents EXT2-CDG/multiple cartilaginous exostoses type II, an
autosomal dominant disorder with prevalence listed as 1:50,000. It has no
characteristic rows in the cached JSON. Clinical rows include chondrosarcoma,
hypertelorism, hypotonia, intellectual disability, kyphoscoliosis, low bone
mineral density, macrocephaly, and seizures. No biochemical or treatment rows
are present.

## DisMech phenotype coverage

The generated UNMAPPED status is correct. The low-score Multiple Synostoses
Syndrome candidate is not an appropriate mapping: it covers NOG/GDF5/GDF6/FGF9
joint-fusion biology rather than EXT2 exostosin glycosyltransferase disease.

As with EXT1, local chondrosarcoma coverage can provide downstream malignancy
context for EXT2-related exostoses, but it does not cover the primary multiple
cartilaginous exostoses type II diagnosis.

## Concordance and completeness

Judgement: true local gap; reject the Multiple Synostoses Syndrome candidate.

The disease-defining features are EXT2, autosomal dominant inheritance,
multiple cartilaginous exostoses type II, and chondrosarcoma risk. The
additional IEMbase neurodevelopmental and skeletal rows are useful review
prompts but should be verified before import because the cached row is sparse
and lacks characteristic markers.

## Curation actions

- Keep this record unmapped until a dedicated EXT2-related multiple hereditary
  exostoses/multiple cartilaginous exostoses target exists.
- Do not map to `Multiple_Synostoses_Syndrome.yaml`.
- Review the IEMbase-only hypotonia, intellectual disability, macrocephaly,
  seizures, kyphoscoliosis, and low bone-mineral-density rows before future
  import.
