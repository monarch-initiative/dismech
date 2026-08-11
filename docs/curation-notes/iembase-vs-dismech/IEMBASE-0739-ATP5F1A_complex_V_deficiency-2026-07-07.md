# IEMbase 0739: ATP5F1A-related mitochondrial ATP synthase F1 alpha deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 739 |
| Nosology | 7.5.01.02 |
| Nosology code | IEM0481 |
| Gene | ATP5F1A |
| External IDs | OMIM:616045; OMIM:615228; ORPHA:254913 |
| Generated mapping | CANDIDATE; fuzzy `SCO1-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | Broad complex V context only; no exact ATP5F1A target identified |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive ATP5F1A-related mitochondrial ATP
synthase F1 subunit alpha deficiency, with alternate labels combined oxidative
phosphorylation deficiency 22 and mitochondrial complex V deficiency, nuclear
type 4. The cached rows are sparse but neonatal/infantile: increased plasma
alanine, asymmetric white matter lesions, irritability, neonatal nystagmus,
infantile perinatal death, neonatal/infantile hypotonia, and
neonatal/infantile microcephaly.

## DisMech phenotype coverage

No exact ATP5F1A target was identified locally.

The generated `SCO1-Related_COX_Deficiency.yaml` candidate is a false positive.
SCO1 is a nuclear complex IV copper-delivery disorder with hepatic failure,
encephalopathy, lactic acidosis, seizures, and hypopituitarism; it is not an
ATP synthase F1 alpha subunit disease. `NARP_syndrome.yaml` and
`Myopathy_Lactic_Acidosis_and_Sideroblastic_Anemia.yaml` are useful complex V
context, but they are MT-ATP6/8 or syndrome-specific and do not model ATP5F1A.

## Concordance and completeness

Judgement: true ATP5F1A complex V local gap. Reject the SCO1 candidate as exact
coverage.

IEMbase supplies a concise neonatal phenotype seed: alanine elevation, white
matter lesions, irritability, nystagmus, hypotonia, microcephaly, and early
death. DisMech currently has no ATP5F1A-specific structural ATP synthase entry.

## Curation actions

- Add ATP5F1A-related mitochondrial complex V deficiency / COXPD22 to the
  complex V backlog.
- Reject `SCO1-Related_COX_Deficiency.yaml` as exact coverage.
- Preserve alanine, asymmetric white matter lesions, irritability, nystagmus,
  hypotonia, microcephaly, and perinatal-death prompts.
