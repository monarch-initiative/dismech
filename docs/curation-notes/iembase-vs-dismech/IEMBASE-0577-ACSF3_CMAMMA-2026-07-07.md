# IEMbase 0577: ACSF3-related combined malonic and methylmalonic aciduria

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 577 |
| Nosology | 12.1.22.01 |
| Gene | ACSF3 |
| External IDs | OMIM:614245; ORPHA:289504 |
| Generated mapping | UNMAPPED; best candidate `3-Hydroxy-3-Methylglutaryl-CoA_Synthase_Deficiency.yaml` |
| Candidate DisMech targets | `Combined_Malonic_and_Methylmalonic_Aciduria.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents ACSF3-related acyl-CoA synthetase 3 deficiency, with
alternate label combined malonic and methylmalonic aciduria and abbreviation
MMA/MA. The record is autosomal recessive, idiopathic subtype, of unknown
treatability, and has no treatment rows.

Biochemical rows include normal blood/plasma propionylcarnitine, increased
malonylcarnitine, low-to-normal free carnitine, increased urinary malonic acid,
increased plasma and urinary methylmalonic acid, increased urinary MMA/MA
ratio, variable base excess, low-to-normal cholesterol and glucose, and
normal-to-high plasma lactate. Clinical and characteristic rows include autism
spectrum disorder, cardiomyopathy, coma, dystonia, failure to thrive, feeding
difficulties, white-matter/brainstem/cerebellar T2 MRI changes, hypoglycemia,
axial hypotonia, ketoacidosis, lethargy, liver dysfunction, loss of speech,
memory problems, microcephaly, ocular migraine, mild dysmorphic features,
seizures, vomiting, developmental delay, and metabolic acidosis.

## DisMech phenotype coverage

`Combined_Malonic_and_Methylmalonic_Aciduria.yaml` is the correct local target.
It models autosomal recessive ACSF3 deficiency, mitochondrial malonyl-CoA /
methylmalonyl-CoA synthetase deficiency, failure to activate malonate and
methylmalonate to CoA thioesters, combined malonic and methylmalonic aciduria,
mitochondrial metabolic inefficiency, and a variable clinical spectrum ranging
from favorable screen-detected outcomes to neurologic or childhood metabolic
presentations.

The generated HMG-CoA synthase candidate is a false positive from organic-acid
metabolism similarity and does not match ACSF3/CMAMMA.

## Concordance and completeness

Judgement: generated false negative; resolve to
`Combined_Malonic_and_Methylmalonic_Aciduria.yaml`.

IEMbase and DisMech agree on ACSF3 identity, recessive inheritance, combined
malonic and methylmalonic aciduria, elevated malonic and methylmalonic acids,
mitochondrial metabolite-repair framing, variable neurologic/metabolic
presentation, seizures, developmental delay, failure to thrive, hypoglycemia,
ketoacidosis, microcephaly, dystonia, axial hypotonia, and liver dysfunction.
DisMech is stronger for the metabolite-activation mechanism and the caution
that unselected cohorts may be mild.

IEMbase adds useful prompts for malonylcarnitine, propionylcarnitine normality,
free carnitine, cholesterol, lactate, cardiomyopathy, autism, white-matter MRI
changes, speech loss, memory problems, ocular migraine, vomiting, and
dysmorphic features.

## Curation actions

- Promote this record to `Combined_Malonic_and_Methylmalonic_Aciduria.yaml`.
- Reject `3-Hydroxy-3-Methylglutaryl-CoA_Synthase_Deficiency.yaml` as an exact
  mapping.
- Consider reviewing IEMbase acylcarnitine, imaging, cardiomyopathy,
  neurodevelopmental, and broader clinical prompts against the local
  generally-mild-course caveat before import.
