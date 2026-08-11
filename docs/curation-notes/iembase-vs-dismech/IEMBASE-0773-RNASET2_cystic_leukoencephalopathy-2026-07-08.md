# IEMbase 0773: RNASET2-related ribonuclease T2 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 773 |
| Nosology | 16.3.05.02 |
| Nosology code | IEM0030 |
| Gene | RNASET2 |
| External IDs | OMIM:612951; ORPHA:85136 |
| Generated mapping | UNMAPPED; weak candidate `COA8-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | None accepted |
| Review date | 2026-07-08 |

## IEMbase phenotype signal

IEMbase labels this autosomal recessive record as RNASET2-related ribonuclease
T2 deficiency, with alternate name cystic leukoencephalopathy without
megalencephaly. The phenotype signal is a congenital or early childhood
leukoencephalopathy with psychomotor delay, spasticity, cerebral atrophy,
cystic leukoencephalopathy without megalencephaly, microcephaly, intracerebral
calcifications, seizures, dystonia, athetosis, sensorineural deafness, and
nystagmus. Biochemical rows list CSF lymphocytes, CSF interferon-alpha, and
interferon-stimulated gene signature as normal-to-high rather than strongly
elevated.

## DisMech phenotype coverage

No local DisMech disease or subtype represents RNASET2-related cystic
leukoencephalopathy. The generated weak candidate, `COA8-Related_COX_Deficiency.yaml`,
shares broad words such as leukoencephalopathy, seizures, and hearing
impairment, but it is a COA8/APOPT1 mitochondrial complex IV assembly disorder
with COX deficiency and mitochondrial myopathy features. That mechanism, gene,
and disease identity are not compatible with RNASET2 ribonuclease deficiency.

`Aicardi_Goutieres_Syndrome.yaml` also overlaps at the level of brain
calcification, leukodystrophy, spasticity, and interferon-related context, but
it does not include RNASET2 as a subtype or causal gene and should not be used
as exact coverage.

## Concordance and completeness

Judgement: true local gap; reject the COA8 candidate.

The local KB has phenotype-level neighbors but lacks the disease entity needed
for exact mapping. RNASET2 disease is especially easy to over-map because it
combines leukoencephalopathy, calcifications, and interferon-adjacent laboratory
rows, but the IEMbase record is molecularly distinct from both AGS and complex
IV deficiency.

## Curation actions

- Treat IEMbase 0773 as an unmapped RNASET2 disease gap.
- Reject `COA8-Related_COX_Deficiency.yaml` as an exact or partial disease
  match.
- If curated later, preserve the specific cystic leukoencephalopathy without
  megalencephaly identity, congenital/early neuroimaging pattern,
  microcephaly, spasticity, psychomotor delay, seizures/movement disorder,
  sensorineural hearing loss, and normal-to-high interferon/CSF rows.
