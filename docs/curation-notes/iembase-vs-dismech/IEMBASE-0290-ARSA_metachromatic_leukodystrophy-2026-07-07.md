# IEMbase 0290: ARSA-related Arylsulfatase A deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 290 |
| Nosology | 20.1.1.01 |
| Gene | ARSA |
| External IDs | OMIM:250100; ORPHA:512 |
| Generated mapping | MAPPED; `Metachromatic_Leukodystrophy.yaml` |
| Candidate DisMech targets | `Metachromatic_Leukodystrophy.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents metachromatic leukodystrophy due to ARSA deficiency.
Inheritance is autosomal recessive and treatability is marked yes.

Clinical rows include psychotic behavior, dysarthria, emotional lability, gait
disturbance, irritability, neurologic deterioration, and spasticity, with
age-patterning across late-infantile, juvenile, and adult presentations.
Biochemical rows list increased CSF protein and increased urinary sulfatide.
Treatment rows list OTL-200 stem-cell-based gene therapy and hematopoietic stem
cell transplant, each linked to neurologic and sulfatide endpoints.

## DisMech phenotype coverage

`Metachromatic_Leukodystrophy.yaml` is the correct local target. The local
entry models ARSA disease-causing variants, arylsulfatase A deficiency,
sulfatide storage, central and peripheral demyelination, neurodegeneration, and
late-infantile, early-juvenile, late-juvenile, and adult subtypes.

Local phenotypes include cognitive impairment, developmental regression,
dysphagia, seizures, hypotonia, and peripheral neuropathy. Local biochemical
entries include reduced arylsulfatase A activity, sulfatide storage burden, and
urinary sulfatide excretion. Treatments include hematopoietic stem cell
transplantation and atidarsagene autotemcel.

## Concordance and completeness

Judgement: correct mapping with strong biochemical and treatment concordance.

IEMbase and DisMech agree on ARSA/MLD identity, recessive inheritance,
urinary sulfatide accumulation, demyelinating neurologic disease, subtype
variation by onset, HSCT, and ex vivo stem-cell gene therapy. The IEMbase
OTL-200 row corresponds to the local atidarsagene autotemcel treatment.
DisMech is stronger for the sulfatide storage mechanism and subtype structure.

IEMbase adds review prompts for psychosis, emotional lability, dysarthria, gait
disturbance, irritability, spasticity, neurologic deterioration wording, and
increased CSF protein. These are clinically plausible and would improve local
phenotype granularity if supported with MLD-specific evidence.

## Curation actions

- Keep this record mapped to `Metachromatic_Leukodystrophy.yaml`.
- Treat IEMbase OTL-200 as concordant with local atidarsagene autotemcel.
- Review psychiatric/behavioral rows, gait/dysarthria/spasticity rows, and CSF
  protein as future phenotype or biomarker enrichment prompts.
