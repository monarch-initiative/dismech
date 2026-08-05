# IEMbase 0693: NDUFS8-related NADH dehydrogenase iron-sulfur protein 8 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 693 |
| Nosology | 7.1.07.02 |
| Nosology code | IEM0419 |
| Gene | NDUFS8 |
| External IDs | OMIM:618222; ORPHA:255241 |
| Generated mapping | CANDIDATE to `COX11-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | Broad complex I/Leigh context only; no exact NDUFS8 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive NDUFS8-related NADH dehydrogenase
iron-sulfur protein 8 deficiency, also labeled mitochondrial complex I
deficiency, nuclear type 2.

The biochemical row shows decreased fibroblast complex I activity across all
ages. Clinical rows include Leigh syndrome, ataxia, dysarthria, hypotonia, and
characteristic hypertrophic cardiomyopathy, myopathy, and progressive external
ophthalmoplegia.

## DisMech phenotype coverage

No exact NDUFS8 or MC1DN2 local target was identified.

`Leigh_Syndrome.yaml` provides broad overlap for Leigh syndrome, hypotonia,
ataxia, ophthalmoplegia, and cardiomyopathy, but it does not model NDUFS8 or
this specific disease entity.

The generated `COX11-Related_COX_Deficiency.yaml` candidate is a complex IV
disorder and should be rejected as exact coverage.

## Concordance and completeness

Judgement: true local gap with broad Leigh overlap only.

The IEMbase row highlights a complex I biochemical defect with cardiomyopathy,
myopathy, dysarthria, ataxia, hypotonia, Leigh syndrome, and progressive
external ophthalmoplegia. These should not be attributed to COX11.

## Curation actions

- Add a dedicated NDUFS8/MC1DN2 target if curated.
- Reject COX11-related complex IV deficiency as exact coverage.
- Preserve decreased complex I activity, Leigh syndrome, ataxia, dysarthria,
  hypotonia, hypertrophic cardiomyopathy, myopathy, and progressive external
  ophthalmoplegia.
