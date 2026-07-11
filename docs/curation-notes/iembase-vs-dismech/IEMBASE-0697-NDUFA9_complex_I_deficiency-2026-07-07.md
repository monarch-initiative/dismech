# IEMbase 0697: NDUFA9-related NADH dehydrogenase alpha subcomplex subunit 9 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 697 |
| Nosology | 7.1.12.01 |
| Nosology code | IEM0424 |
| Gene | NDUFA9 |
| External IDs | OMIM:618247 for NDUFA9/MC1DN26; IEMbase source lists OMIM:256000; ORPHA:255241 |
| Generated mapping | CANDIDATE to `COX11-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | Broad complex I/Leigh context only; no exact NDUFA9 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive NDUFA9-related NADH dehydrogenase alpha
subcomplex subunit 9 deficiency, also labeled mitochondrial complex I
deficiency, nuclear type 26.

The source lists OMIM:256000, while MONDO resolves mitochondrial complex I
deficiency nuclear type 26 to OMIM:618247 and NDUFA9. The broad source
identifier should therefore be checked before downstream use.

Biochemical rows show decreased fibroblast complex I activity and increased
plasma lactate through childhood. Clinical rows include abnormal brain MRI,
brainstem lesions, dysarthria, dysphagia, lactic acidosis, Leigh syndrome,
dystonia, and retinitis pigmentosa.

## DisMech phenotype coverage

No exact NDUFA9 or MC1DN26 local target was identified.

`Leigh_Syndrome.yaml` supplies broad overlap for complex I-linked Leigh disease,
lactate elevation, brainstem lesions, movement disorder, dysphagia, and
retinal/neurologic involvement, but it does not model NDUFA9 as a causal gene.

The generated `COX11-Related_COX_Deficiency.yaml` candidate is a complex IV
copper-delivery disorder, not an NDUFA9 complex I subunit disorder.

## Concordance and completeness

Judgement: true local gap with broad Leigh overlap only.

The IEMbase phenotype signal combines a complex I enzyme defect with Leigh
syndrome, brainstem MRI disease, bulbar dysfunction, dystonia, and retinitis
pigmentosa. That combination should not be collapsed into generic Leigh or into
COX11-related complex IV deficiency.

## Curation actions

- Add a dedicated NDUFA9/MC1DN26 target if curated.
- Reject COX11-related complex IV deficiency as exact coverage.
- Preserve the source OMIM discrepancy for review before downstream identifier
  use.
- Preserve decreased fibroblast complex I activity, increased plasma lactate,
  brain MRI abnormalities, brainstem lesions, dysarthria, dysphagia, lactic
  acidosis, Leigh syndrome, dystonia, and retinitis pigmentosa.
