# IEMbase 0347: EXT1-related multiple cartilaginous exostoses type I

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 347 |
| Nosology | 18.2.06.01 |
| Gene | EXT1 |
| External IDs | OMIM:133700; ORPHA:55880 |
| Generated mapping | UNMAPPED; low candidate `Multiple_Synostoses_Syndrome.yaml` |
| Candidate DisMech targets | No exact target; `Chondrosarcoma.yaml` is downstream context only |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents EXT1-CDG/multiple cartilaginous exostoses type I, an
autosomal dominant disorder. Characteristic rows include osteochondroma,
functional joint impairment, chondrosarcoma, and normal sialotransferrins.
The additional clinical row is bone deformities. No treatment rows are
present.

## DisMech phenotype coverage

The generated UNMAPPED status is correct. The low-score Multiple Synostoses
Syndrome candidate is not an appropriate mapping: it covers progressive joint
fusion involving NOG/GDF5/GDF6/FGF9 BMP signaling, not EXT1-related exostosin
glycosyltransferase disease.

DisMech has chondrosarcoma context that includes EXT1/EXT2 as predisposition
genes, but that is not equivalent to a primary multiple hereditary
exostoses/multiple cartilaginous exostoses disease entry. It should be treated
as downstream malignancy context only.

## Concordance and completeness

Judgement: true local gap; reject the Multiple Synostoses Syndrome candidate.

IEMbase is sparse but disease-specific: EXT1, autosomal dominant inheritance,
multiple cartilaginous exostoses type I, osteochondroma, bone deformities,
functional joint impairment, and chondrosarcoma risk. Current local coverage
does not represent that primary disorder.

## Curation actions

- Keep this record unmapped until a dedicated EXT1-related multiple hereditary
  exostoses/multiple cartilaginous exostoses target exists.
- Do not map to `Multiple_Synostoses_Syndrome.yaml`.
- Use `Chondrosarcoma.yaml` only as malignancy-risk context, not as disease
  identity coverage.
