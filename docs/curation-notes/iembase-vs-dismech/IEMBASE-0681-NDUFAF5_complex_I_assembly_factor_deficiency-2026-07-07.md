# IEMbase 0681: NDUFAF5-related complex I assembly factor 5 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 681 |
| Nosology | 7.1.05.01 |
| Nosology code | IEM0441 |
| Gene | NDUFAF5 |
| External IDs | OMIM:618238; ORPHA:255241 |
| Generated mapping | CANDIDATE to `COX4I1-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | Broad complex I/Leigh context only; no exact NDUFAF5 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive NDUFAF5-related complex I assembly factor
5 deficiency, also labeled mitochondrial complex I deficiency, nuclear type 16.

Biochemical rows include decreased fibroblast complex I activity across all ages,
increased plasma lactate across all ages, and increased CSF lactate in the
neonatal and infantile periods. Clinical rows are broad: basal ganglia MRI
abnormalities, Leigh syndrome, lactic acidosis, hypotonia, dystonia, spasticity,
epilepsy or seizures, choreoathetosis, extrapyramidal signs, movement disorder,
intellectual disability, failure to thrive, brain MRI abnormality, and multiple
dysmorphology/developmental prompts including micrognathia, small chin, small
mouth, abnormal toes, facial dysmorphism, hair abnormality, intrauterine growth
retardation, and small sacral pit.

## DisMech phenotype coverage

No exact NDUFAF5 or MC1DN16 target was identified.

`Leigh_Syndrome.yaml` covers much of the shared syndrome-level neurologic
package, including complex I deficiency, lactic acidosis, hypotonia,
basal-ganglia involvement, dystonia/movement disorder, ataxia, seizures, and
failure to thrive. It does not cover the NDUFAF5 entity or the detailed
dysmorphology and congenital-anomaly prompts in this row.

The generated `COX4I1-Related_COX_Deficiency.yaml` candidate is a complex IV
deficiency and should not be accepted for a complex I assembly factor.

## Concordance and completeness

Judgement: true local gap with substantial broad Leigh overlap.

If curated, this record needs a gene-specific NDUFAF5 disease model rather than
being folded into generic Leigh syndrome. The non-Leigh detail in IEMbase is
important: facial/hair/toe findings, intrauterine growth retardation, sacral
pit, CSF lactate, choreoathetosis, and age-banded neurologic progression.

## Curation actions

- Add a dedicated NDUFAF5/MC1DN16 target if curated.
- Reject COX4I1-related complex IV deficiency as exact coverage.
- Preserve decreased complex I activity, plasma and CSF lactate, basal-ganglia
  MRI abnormalities, Leigh syndrome, movement disorder, seizures/epilepsy,
  spasticity, intellectual disability, and dysmorphology prompts.
- Use `Leigh_Syndrome.yaml` only for shared syndrome context.
