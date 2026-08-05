# IEMbase 0097: GRHPR-related glyoxylate reductase/hydroxypyruvate reductase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 97 |
| Nosology | 13.1.01.01 |
| Gene | GRHPR |
| External IDs | OMIM:260000 |
| Generated mapping | UNMAPPED; best fuzzy candidate `Pyruvate_Dehydrogenase_Deficiency.yaml` |
| Candidate DisMech targets | `Primary_Hyperoxaluria_Type_2.yaml`; `Disorders_of_Glyoxylate_and_Oxalate_Metabolism.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive GRHPR-related glyoxylate
reductase/hydroxypyruvate reductase deficiency, with alternate labels primary
hyperoxaluria type 2, D-glycerate dehydrogenase deficiency, and PH2.
Treatability is marked unknown and no treatment rows are listed.

The characteristic biochemical rows are plasma and urinary oxalic acid and
urinary glyceric acid. The wider panel also includes plasma glyceric acid,
creatinine, and urea.

The characteristic clinical rows include failure to thrive, growth retardation,
nephrocalcinosis, nephrolithiasis, radiolucent metaphyseal bands, and renal
colic.

## DisMech phenotype coverage

The generated UNMAPPED status is a false negative. The best local disease target
is `Primary_Hyperoxaluria_Type_2.yaml`, with
`Disorders_of_Glyoxylate_and_Oxalate_Metabolism.yaml` as grouping context.

DisMech models PH2 as biallelic GRHPR deficiency disrupting glyoxylate-to-
glycolate and hydroxypyruvate-to-D-glycerate flux, producing increased urinary
oxalate and L-glycerate. The disease entry covers hyperoxaluria, calcium
oxalate nephrolithiasis, nephrocalcinosis, kidney failure, and systemic
oxalate deposition. The grouping explicitly differentiates GRHPR/PH2 from the
AGXT/PH1 mechanism.

`Pyruvate_Dehydrogenase_Deficiency.yaml` is a lexical false-positive candidate
from "hydroxypyruvate" and should not be used.

## Concordance and completeness

Judgement: false-negative mapping with high local mechanistic coverage.

DisMech is strong for the core gene, pathway, oxalate/glycerate chemistry, and
kidney-stone mechanism. IEMbase adds plasma-versus-urine compartment detail and
additional clinical rows such as growth retardation, renal colic, and
radiolucent metaphyseal bands.

## Curation actions

- Update the mapping logic or manual crosswalk to resolve this record to
  `Primary_Hyperoxaluria_Type_2.yaml`.
- Keep `Disorders_of_Glyoxylate_and_Oxalate_Metabolism.yaml` as grouping
  context.
- Consider adding explicit glyceric-acid biomarkers and the IEMbase renal-colic
  and skeletal-imaging clinical rows if evidence supports them.
