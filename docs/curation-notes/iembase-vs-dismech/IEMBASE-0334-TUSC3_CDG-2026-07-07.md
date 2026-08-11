# IEMbase 0334: TUSC3-related oligosaccharyltransferase subunit deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 334 |
| Nosology | 18.1.16.01 |
| Gene | TUSC3 |
| External IDs | OMIM:611093 |
| Generated mapping | UNMAPPED; low-score candidate `Growth_Hormone_Insensitivity_Syndrome.yaml` |
| Candidate DisMech targets | Reject `Growth_Hormone_Insensitivity_Syndrome.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents TUSC3-CDG, an autosomal recessive congenital disorder of
glycosylation involving an oligosaccharyltransferase subunit. The characteristic
rows are psychomotor delay, facial dysmorphism, and short stature. Additional
clinical rows include camptodactyly, deeply set eyes, hypertelorism, long face,
pointed chin, and syndactyly.

The only biochemical row is serum sialotransferrins, recorded as not abnormal
across the life stages in the cached JSON. No treatment rows are present.

## DisMech phenotype coverage

The generated growth-hormone-insensitivity candidate is a lexical and phenotype
neighbor, not a valid disease mapping. That DisMech entry models GH-IGF1 axis
defects with short stature, IGF-1 abnormalities, and GH/IGF pathway genes. It
does not include TUSC3, oligosaccharyltransferase dysfunction, or the CDG
nosology represented by this IEMbase record.

Local CDG module and grouping files provide broad glycosylation context, but no
standalone TUSC3-CDG entry exists.

## Concordance and completeness

Judgement: true local disease gap; reject the GHIS candidate.

The only real overlap with GHIS is short stature. The IEMbase record points to
TUSC3-related protein glycosylation disease with neurodevelopmental and
dysmorphic features, which is mechanistically distinct from GH receptor,
STAT5B, IGFALS, IGF1, or IGF1R axis disorders.

## Curation actions

- Add a standalone TUSC3-CDG target before treating this IEMbase record as
  mapped.
- Do not map this record to growth hormone insensitivity based on short stature
  alone.
- Preserve psychomotor delay, facial dysmorphism, short stature, camptodactyly,
  syndactyly, and the apparently non-diagnostic sialotransferrin row as
  future-curation prompts.
