# IEMbase 0398: NOGENE-related Kearns Sayre Syndrome

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 398 |
| Nosology | 6.3.02.01 |
| Gene | No single gene; single large-scale mtDNA deletion disorder |
| External IDs | OMIM:530000; ORPHA:480 |
| Generated mapping | UNMAPPED; no candidate |
| Candidate DisMech targets | `Kearns-Sayre_Syndrome.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents Kearns-Sayre syndrome, abbreviated KSS. Clinical rows include
onset before 20 years, myopathy, ophthalmoparesis, ophthalmoplegia, pigmentary
retinopathy, ataxia, cardiomyopathy, cardiac conduction deficits, intellectual
disability, and short stature. Biochemical rows include increased CSF protein
and low-to-normal CSF 5-methyltetrahydrofolic acid. There are no treatment rows.

## DisMech phenotype coverage

The generated unmapped status is a false negative. Local
`Kearns-Sayre_Syndrome.yaml` models KSS as a single large-scale mitochondrial DNA
deletion syndrome with onset before age 20, post-mitotic tissue energy failure,
chronic progressive external ophthalmoplegia, pigmentary retinopathy, cardiac
conduction disease, ataxia, hearing and endocrine involvement, lactate stress,
and monitoring/treatment such as pacemaker consideration for conduction block.

Local DisMech is stronger for mtDNA deletion mechanism, tissue-specific energy
failure, and management rationale. IEMbase adds concise CSF protein and CSF
5-MTHF biomarker prompts and separates ophthalmoparesis from ophthalmoplegia.

## Concordance and completeness

Judgement: false negative; resolve to `Kearns-Sayre_Syndrome.yaml`.

The resources agree on KSS identity, lack of a single nuclear gene, single
large-scale mtDNA deletion disease class, onset before 20 years, myopathy/
ophthalmoplegia, pigmentary retinopathy, cardiac conduction disease, and
multisystem neurologic involvement.

## Curation actions

- Map this record to `Kearns-Sayre_Syndrome.yaml`.
- Consider adding IEMbase's CSF protein, CSF 5-MTHF, ophthalmoparesis,
  cardiomyopathy, intellectual disability, and short-stature prompts after
  source verification.
- Preserve the distinction between Pearson syndrome and KSS as separate disease
  entries within the same single large-scale mtDNA deletion continuum.
