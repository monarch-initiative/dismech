# IEMbase 0628: PIGC-related developmental disability with drug-responsive epilepsy

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 628 |
| Nosology | 18.3.00.03 |
| Gene | PIGC |
| External IDs | OMIM:615716; ORPHA:88616 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | None exact; `IRX5-related_Craniofacial_Dysostosis_with_Osteopenia_Intellectual_Disability_and_Dental_Anomalies.yaml` is a false candidate |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents PIGC-related developmental disability, severe intellectual
disability, and drug-responsive epilepsy / PIGC-CDG as an autosomal recessive
disorder with unknown treatability. The cached record has no treatment rows
despite the drug-responsive epilepsy wording in the disease name.

Biochemical rows include decreased GPI markers by flow cytometry. Clinical and
characteristic rows include ataxia, optional cerebellar atrophy, coarse facial
features, hypotonia, intractable seizures, and intellectual disability.

## DisMech phenotype coverage

No exact PIGC-CDG entry was identified. The IRX5-related craniofacial
dysostosis candidate is a nonspecific craniofacial/intellectual-disability
overlap and should be rejected as exact.

## Concordance and completeness

Judgement: true local gap.

The disease-name treatment clue should be source-reviewed before importing any
specific medication claim because the IEMbase cached treatment table is empty.

## Curation actions

- Do not map to the IRX5-related craniofacial dysostosis candidate.
- Curate PIGC-CDG as a separate GPI-anchor biosynthesis disorder if selected.
- Preserve decreased GPI markers, intractable seizures, intellectual
  disability, ataxia, cerebellar atrophy, hypotonia, and facial-feature prompts.
- Source-review the drug-responsive epilepsy wording before adding treatment
  content.
