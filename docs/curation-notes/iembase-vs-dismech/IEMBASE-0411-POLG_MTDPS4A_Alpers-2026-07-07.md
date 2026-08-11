# IEMbase 0411: POLG-related mitochondrial DNA polymerase gamma deficiency 4A

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 411 |
| Nosology | 9.2.01.01 |
| Gene | POLG |
| External IDs | OMIM:203700; ORPHA:726 |
| Generated mapping | CANDIDATE; `Mitochondrial_Neurogastrointestinal_Encephalomyopathy.yaml` |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents POLG-related mitochondrial DNA polymerase gamma catalytic
subunit deficiency 4A, with aliases mitochondrial depletion syndrome 4A,
Alpers-Huttenlocher syndrome, and MTDPS4A. It records autosomal dominant and
autosomal recessive inheritance. Biochemical rows include liver mtDNA depletion,
urinary 3-methylglutaconic acid, and increased plasma lactate. Clinical rows
include ataxia, developmental delay, hypotonia, intellectual disability,
perinatal death, impaired vision, vomiting, intractable epilepsy, progressive
liver failure, psychomotor retardation, and valproate-induced fatal liver
toxicity.

## DisMech phenotype coverage

The generated MNGIE candidate is not an exact match. Local
`Mitochondrial_Neurogastrointestinal_Encephalomyopathy.yaml` includes a rare
POLG-related MNGIE-like subtype, but the defining syndrome there is
gastrointestinal dysmotility/cachexia, ptosis/ophthalmoplegia, neuropathy, and
leukoencephalopathy, not the Alpers-Huttenlocher/hepatocerebral
epilepsy-liver-failure phenotype.

Local `Sensory_Ataxic_Neuropathy_Dysarthria_Ophthalmoparesis.yaml` is useful
POLG context and includes mtDNA instability and a valproate avoidance warning,
but it is a SANDO/ataxia-neuropathy target. Local
`Mitochondrial_DNA_Depletion_Syndrome_7.yaml` has Alpers-like hepatocerebral
features but is TWNK-related, not POLG MTDPS4A.

## Concordance and completeness

Judgement: true POLG Alpers-Huttenlocher/MTDPS4A local gap; reject MNGIE as an
exact mapping.

The available local POLG entries cover adjacent POLG-spectrum disease, but none
represents the IEMbase combination of POLG, infantile/childhood mtDNA depletion,
intractable epilepsy, progressive liver failure, psychomotor regression, and
valproate-triggered fatal hepatotoxicity as the primary disease identity.

## Curation actions

- Keep this record unmapped until a POLG Alpers-Huttenlocher syndrome or MTDPS4A
  target exists.
- Do not map to `Mitochondrial_Neurogastrointestinal_Encephalomyopathy.yaml`.
- Use local SANDO/POLG material only as general POLG-spectrum context.
- If curated, include POLG, liver mtDNA depletion, lactate,
  3-methylglutaconic acid, intractable epilepsy, progressive liver failure,
  psychomotor regression, and explicit valproate contraindication.
