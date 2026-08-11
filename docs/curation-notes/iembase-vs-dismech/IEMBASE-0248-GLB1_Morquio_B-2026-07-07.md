# IEMbase 0248: GLB1-related Beta-galactosidase 1 deficiency, Morquio B

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 248 |
| Nosology | 20.1.14.01 |
| Gene | GLB1 |
| External IDs | OMIM:253010; ORPHA:354 |
| Generated mapping | UNMAPPED; best candidate `Morquio_syndrome.yaml` score 0.862 |
| Candidate DisMech targets | `Morquio_syndrome.yaml#Type B` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as GLB1-related beta-galactosidase 1 deficiency,
Morquio B, with alternate labels Morquio syndrome type B,
mucopolysaccharidosis type IVB variant, and MPS IVB. The record is autosomal
recessive and treatability is marked unknown, with no treatment rows in the
cached JSON.

Biochemical rows include decreased beta-galactosidase activity and urinary
keratan sulfate and total glycosaminoglycans that range from normal to
increased. Clinical rows include coarse facial features, dysostosis multiplex,
hearing loss, liver dysfunction, odontoid hypoplasia, restrictive lung disease,
and sternal bulging. Characteristic rows include atlanto-axial instability,
cervical myelopathy, corneal clouding, degenerative hip dysplasia, genu valgum,
joint laxity, kyphosis, short stature, and valvular thickening.

## DisMech phenotype coverage

`Morquio_syndrome.yaml#Type B` is the correct local target despite the generated
unmapped status. The local file explicitly includes Type B/MPS IVB/GLB1
coverage and describes keratan-sulfate-dominant beta-galactosidase dysfunction
within the Morquio syndrome spectrum. It covers the same skeletal, cervical,
airway, ocular, auditory, and cardiac valve manifestations as the shared MPS IV
entry, while distinguishing Type B from GALNS-related Type A.

## Concordance and completeness

Judgement: generated false negative; manual target is
`Morquio_syndrome.yaml#Type B` with high concordance.

IEMbase and DisMech agree on GLB1/MPS IVB identity, beta-galactosidase
deficiency, keratan sulfate storage, skeletal dysplasia, joint laxity, odontoid
and atlanto-axial disease, corneal clouding, hearing loss, restrictive lung
disease, short stature, kyphosis, and valvular thickening. IEMbase is more
granular for the per-subtype clinical checklist, while DisMech is stronger for
mechanism and syndrome-level context.

## Curation actions

- Map this record to `Morquio_syndrome.yaml#Type B`.
- Review the crosswalk alias/normalization logic so Morquio syndrome type B,
  MPS IVB, and mucopolysaccharidosis type IVB variant resolve to the existing
  subtype.
- Use IEMbase's symptom checklist as enrichment prompts if the Morquio Type B
  subtype is expanded.
