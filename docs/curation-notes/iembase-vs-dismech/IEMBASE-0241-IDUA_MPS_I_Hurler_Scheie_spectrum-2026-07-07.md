# IEMbase 0241: IDUA-related Alpha-iduronidase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 241 |
| Nosology | 20.2.01.01 |
| Gene | IDUA |
| External IDs | OMIM:607014; OMIM:607015; OMIM:607016; ORPHA:93473 |
| Generated mapping | MAPPED; `Hurler_syndrome.yaml` |
| Candidate DisMech targets | `Hurler_syndrome.yaml`; umbrella context `Mucopolysaccharidosis.yaml#MPS I (IDUA Mutations)` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as IDUA-related alpha-iduronidase deficiency, with
alternate labels spanning mucopolysaccharidosis type 1H/Hurler syndrome,
mucopolysaccharidosis type 1S/Scheie syndrome, and MPS I. The record is
autosomal recessive and treatability is marked yes.

Treatment rows include hematopoietic stem cell transplantation, intrathecal
iduronidase, and intravenous iduronidase. Biochemical rows include decreased
alpha-iduronidase activity and increased urinary dermatan sulfate, heparan
sulfate, and total glycosaminoglycans. Clinical and characteristic rows include
cardiomyopathy, cervical myelopathy, coronary artery disease, delayed tooth
eruption, diarrhea, genu valgum, glaucoma, hearing loss, intellectual
disability, joint contractures, restrictive lung disease, seizures, swallowing
difficulties, carpal tunnel syndrome, coarse facial features, corneal clouding,
dysostosis multiplex, hepatosplenomegaly, hernias, hydrocephalus, kyphosis,
macrocephaly, obstructive sleep apnea, retinal dystrophy, upper airway
obstruction, and valvular thickening.

## DisMech phenotype coverage

`Hurler_syndrome.yaml` is a high-concordance target for severe MPS I and also
contains explicit related entries for Hurler-Scheie and Scheie syndrome. It
covers biallelic IDUA disease, deficient alpha-L-iduronidase activity,
dermatan/heparan sulfate storage, elevated GAGs, multisystem skeletal,
cardiac, airway, ocular, neurologic, hepatic, and otologic disease, HSCT,
laronidase/enzyme replacement, and investigational IDUA-directed therapy.

`Mucopolysaccharidosis.yaml` additionally has an umbrella subtype entry for
`MPS I (IDUA Mutations)` that explicitly spans Hurler to attenuated Scheie
phenotypes.

## Concordance and completeness

Judgement: correct high-concordance mapping, with spectrum scope noted.

The generated mapping to `Hurler_syndrome.yaml` is valid because the local file
covers the canonical IDUA/GAG-storage mechanism and includes severe and
attenuated MPS I context. The main scope caveat is that the IEMbase label is an
MPS I spectrum record rather than a Hurler-only record. Future mapping display
should prefer the IDUA/MPS I spectrum when subtype-aware labels are available,
while retaining `Hurler_syndrome.yaml` as the current strongest disease file.

## Curation actions

- Keep the current mapping to `Hurler_syndrome.yaml`.
- Note the spectrum relationship to Hurler-Scheie and Scheie syndrome in any
  downstream curation queue.
- Use IEMbase's dental, orthopedic, hematologic, vascular, and treatment rows as
  enrichment prompts if MPS I coverage is refreshed.
