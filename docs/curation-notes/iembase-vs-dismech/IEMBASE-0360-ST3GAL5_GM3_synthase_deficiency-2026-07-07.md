# IEMbase 0360: ST3GAL5-related GM3 synthase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 360 |
| Nosology | 18.3.00.01 |
| Gene | ST3GAL5 |
| External IDs | OMIM:609056; ORPHA:370938 |
| Generated mapping | MAPPED/HIGH to `GM3_Synthase_Deficiency.yaml` |
| Candidate DisMech targets | `GM3_Synthase_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents ST3GAL5-CDG, also listed as Amish infantile epilepsy, an
autosomal recessive lactosylceramide alpha-2,3-sialyltransferase deficiency.
Characteristic rows include cortical atrophy on MRI, failure to thrive, GM3
activity, GM3 ganglioside, intractable epilepsy, and lactosylceramide.

Additional clinical rows include acquired microcephaly, choreoathetosis,
sensorineural deafness, intellectual disability, optic nerve hypoplasia,
pigmentation, psychomotor regression, and visual impairment. Biochemical rows
include GM3 activity, GM3 ganglioside, lactate, and lactosylceramide. No
treatment rows are present.

## DisMech phenotype coverage

The generated MAPPED/HIGH status is correct. DisMech has a GM3 synthase
deficiency file for biallelic ST3GAL5 disease, describing loss of GM3 synthase
conversion of lactosylceramide to GM3, depletion of GM3 and downstream
gangliosides, and severe infantile neurodevelopmental disease.

Local coverage includes refractory seizures, developmental delay/regression,
profound intellectual disability, feeding difficulty, failure to thrive, visual
and hearing impairment, movement disorder, hypotonia, abnormal skin
pigmentation, reduced GM3 synthase activity, reduced GM3 ganglioside, and
lactosylceramide/downstream ganglioside abnormalities.

## Concordance and completeness

Judgement: correct mapping with high concordance.

The resources agree on ST3GAL5 identity, autosomal recessive inheritance, GM3
synthase deficiency, lactosylceramide/GM3 ganglioside biology, infantile
refractory epilepsy, neurodevelopmental regression or delay, failure to thrive,
hearing and visual involvement, movement disorder, microcephaly/cortical
atrophy context, and abnormal pigmentation.

One identifier detail needs review: IEMbase reports ORPHA:370938, while the
local DisMech file uses ORPHA:370933. The OMIM, gene, disease name, and
mechanism all support the mapping, but the ORPHA discrepancy should be checked
before reusing the ORPHA code.

## Curation actions

- Keep the mapping to `GM3_Synthase_Deficiency.yaml`.
- Review the ORPHA identifier discrepancy, `ORPHA:370938` in IEMbase versus
  local `ORPHA:370933`, before any identifier update.
- Consider future enrichment with lactate, plasma GM3/lactosylceramide row
  placement, optic nerve hypoplasia, acquired microcephaly, choreoathetosis,
  and cortical atrophy after source verification.
