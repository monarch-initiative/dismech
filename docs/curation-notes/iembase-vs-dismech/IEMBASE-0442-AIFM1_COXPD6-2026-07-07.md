# IEMbase 0442: AIFM1-related X-linked mitochondrial myopathy

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 442 |
| Nosology | 11.4.03.01 |
| Gene | AIFM1 |
| External IDs | OMIM:300816; ORPHA:101078 |
| Generated mapping | UNMAPPED; low candidate `X-linked_Nonsyndromic_Hearing_Loss.yaml` |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents AIFM1-related X-linked mitochondrial myopathy, also called
combined oxidative phosphorylation defect 6 (COXPD6). It records X-linked
inheritance. Biochemical rows include increased lactate in cerebrospinal fluid
and plasma. Clinical rows include hypotonia, neurologic deterioration,
perinatal death, psychomotor regression, areflexia, neuropathy, and seizures.
There are no treatment rows.

## DisMech phenotype coverage

There is no exact local target for the AIFM1 COXPD6 or X-linked infantile
mitochondrial myopathy phenotype. Local AIFM1 context exists in
`X-linked_Nonsyndromic_Hearing_Loss.yaml`, `Auditory_Neuropathy.yaml`, and
`Spondyloepimetaphyseal_Dysplasia_Bieganski_Type.yaml`, but those files describe
different AIFM1-associated presentations: DFNX hearing loss, auditory neuropathy
or ANSD-related mitochondrial neuronal injury, and a skeletal dysplasia with
hypomyelination and neurodegeneration.

The generated `X-linked_Nonsyndromic_Hearing_Loss.yaml` candidate is therefore
not an exact mapping for the IEMbase mitochondrial myopathy/COXPD6 record.

## Concordance and completeness

Judgement: true AIFM1 COXPD6 local gap; reject DFNX hearing loss as an exact
mapping, while retaining existing AIFM1 files as gene-spectrum context.

The generated candidate shares gene and inheritance but not the disease entity,
proximal phenotype, or combined OXPHOS mitochondrial myopathy framing.

## Curation actions

- Keep this record unmapped until an AIFM1-related X-linked mitochondrial
  myopathy or COXPD6 target exists, or until an explicit lumping decision places
  it into a broader AIFM1 mitochondrial disorder file.
- Do not map directly to `X-linked_Nonsyndromic_Hearing_Loss.yaml`.
- If curated, include AIFM1, X-linked inheritance, combined oxidative
  phosphorylation defect 6, increased plasma and CSF lactate, hypotonia,
  neurologic deterioration, psychomotor regression, areflexia, neuropathy,
  seizures, and perinatal death.
